"""Calibración de probabilidades del ensemble (Platt scaling / isotonic) para 1X2, O/U 2.5 y BTTS.

Método elegido por validación out-of-sample (split temporal + CV repetida):

- Over/Under 2.5 ......... Platt         (mejora Brier y LogLoss)
- 1X2 Local (1), Visitante (2) ....... Platt (mejora Brier y LogLoss)
- 1X2 Empate (X) ......... identidad     (calibrar no mejora OOS)
- BTTS ................... identidad     (calibrar no mejora OOS)

La calibración es determinista y parametrizada (a, b) en espacio logit, por lo
que se persiste como configuración en el modelo (sin requerir sklearn en runtime).
"""
import json
import math


def _logit(p):
    p = max(min(float(p), 0.9999), 0.0001)
    return math.log(p / (1.0 - p))


def _sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def _binary_targets(outcomes, mode):
    targets = []
    for h, a in outcomes:
        if mode == "over_2_5":
            targets.append(1 if h + a > 2 else 0)
        elif mode == "under_2_5":
            targets.append(1 if h + a < 3 else 0)
        elif mode == "btts_yes":
            targets.append(1 if h > 0 and a > 0 else 0)
        else:
            raise ValueError(f"Modo binario no soportado: {mode}")
    return targets


def _one_hot_1x2(outcomes):
    labels = []
    for h, a in outcomes:
        if h > a:
            labels.append(0)
        elif h == a:
            labels.append(1)
        else:
            labels.append(2)
    return labels


def fit_platt(xs, ys):
    """Ajusta logistic(a*logit(x)+b) sobre y via máxima verosimilitud (Newton)."""
    from sklearn.linear_model import LogisticRegression

    X = [_logit(x) for x in xs]
    clf = LogisticRegression()
    clf.fit([[x] for x in X], [int(y) for y in ys])
    a = float(clf.coef_[0][0])
    b = float(clf.intercept_[0])
    return a, b


class PlattCalibration:
    """Calibración paramétrica (Platt) sobre logit. Persistible en JSON."""

    def __init__(self, params=None):
        self.params = params or {}  # {"1": {"a":..,"b":..}, "over_2_5": {...}, ...}

    def fit(self, rows):
        """rows: list[dict] con "probs" y "outcome". Calcula coeficientes por mercado."""
        outcomes = [r["outcome"] for r in rows]
        p = self.params

        # Over/Under 2.5
        xs = [r["probs"]["over_2_5"] for r in rows]
        ys = _binary_targets(outcomes, "over_2_5")
        a, b = fit_platt(xs, ys)
        p["over_2_5"] = {"a": a, "b": b}

        # BTTS (se ajusta para diagnóstico; rutina de transform lo respeta si está en enabled)
        xs = [r["probs"]["btts_yes"] for r in rows]
        ys = _binary_targets(outcomes, "btts_yes")
        a, b = fit_platt(xs, ys)
        p["btts_yes"] = {"a": a, "b": b}

        # 1X2 one-vs-rest
        labels = _one_hot_1x2(outcomes)
        for cls, key in ((0, "1"), (1, "X"), (2, "2")):
            xs = [r["probs"][key] for r in rows]
            ys = [1 if lbl == cls else 0 for lbl in labels]
            a, b = fit_platt(xs, ys)
            p[key] = {"a": a, "b": b}

        self.params = p
        return self

    def transform_market(self, key, prob, enabled):
        """Aplica calibración a un mercado. Si no está habilitado, devuelve prob sin cambio."""
        if not enabled or key not in self.params:
            return float(prob)
        coeff = self.params[key]
        return _sigmoid(coeff["a"] * _logit(prob) + coeff["b"])

    def transform(self, probs, enabled_markets=None):
        """probs: dict crudo del ensemble. Devuelve dict calibrado (0/1) + derivados."""
        if enabled_markets is None:
            enabled_markets = set(self.params.keys())
        out = {}

        # 1X2: calibrar locales/empate/visitante y renormalizar.
        raw = {
            "1": self.transform_market("1", probs["1"], "1" in enabled_markets),
            "X": self.transform_market("X", probs["X"], "X" in enabled_markets),
            "2": self.transform_market("2", probs["2"], "2" in enabled_markets),
        }
        s = raw["1"] + raw["X"] + raw["2"]
        if s > 0:
            for k in ("1", "X", "2"):
                out[k] = raw[k] / s
        else:
            out.update({k: 1.0 / 3 for k in ("1", "X", "2")})

        p1, px, p2 = out["1"], out["X"], out["2"]
        out["1x"] = p1 + px
        out["x2"] = px + p2
        out["12"] = p1 + p2
        out["dnb_home"] = p1
        out["dnb_away"] = p2

        # Goles: over/under 2.5
        over = self.transform_market("over_2_5", probs["over_2_5"], "over_2_5" in enabled_markets)
        out["over_2_5"] = over
        out["under_2_5"] = 1.0 - over

        # Goles: over/under 3.5 (aditivo; identidad si no está habilitado)
        if "over_3_5" in probs:
            over3 = self.transform_market("over_3_5", probs["over_3_5"], "over_3_5" in enabled_markets)
            out["over_3_5"] = over3
            out["under_3_5"] = 1.0 - over3

        # BTTS
        btts = self.transform_market("btts_yes", probs["btts_yes"], "btts_yes" in enabled_markets)
        out["btts_yes"] = btts
        out["btts_no"] = 1.0 - btts

        return out

    def save_json(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.params, f, ensure_ascii=False, indent=1)
        return path


# ------------------------------------------------------------------ metrics
def brier_binary(probs, outcomes):
    return sum((p - o) ** 2 for p, o in zip(probs, outcomes)) / len(probs)


def logloss_binary(probs, outcomes):
    eps = 1e-9
    return -sum(
        o * math.log(max(p, eps)) + (1 - o) * math.log(max(1 - p, eps))
        for p, o in zip(probs, outcomes)
    ) / len(probs)


def calibration_error(probs, outcomes, nbins=5):
    err = 0.0
    bins = [[[], []] for _ in range(nbins)]
    for p, o in zip(probs, outcomes):
        idx = min(nbins - 1, int(p * nbins))
        bins[idx][0].append(p)
        bins[idx][1].append(o)
    for pv, ov in bins:
        if not pv:
            continue
        mp = sum(pv) / len(pv)
        fo = sum(ov) / len(ov)
        err += (len(pv) / len(probs)) * abs(mp - fo)
    return err


def report_single(market, probs, outcomes):
    return {
        "market": market,
        "n": len(probs),
        "frequency": round(sum(outcomes) / len(outcomes), 4),
        "mean_prob": round(sum(probs) / len(probs), 4),
        "brier": round(brier_binary(probs, outcomes), 4),
        "log_loss": round(logloss_binary(probs, outcomes), 4),
        "calibration_error": round(calibration_error(probs, outcomes), 4),
    }