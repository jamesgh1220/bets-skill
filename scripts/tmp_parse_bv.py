#!/usr/bin/env python3
"""Parse a BettingView markdown dump saved by webfetch and compute best (max) odds per outcome column for a given market table."""
import sys, re

def nonblank(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return [ln.strip() for ln in fh if ln.strip() != ""]

def parse(path, market):
    toks = nonblank(path)
    # locate market header line
    idx = None
    for i, t in enumerate(toks):
        if t.startswith("## ") and market.lower() in t.lower():
            idx = i
            break
    if idx is None:
        return None
    # move to Bookmaker
    bm = None
    for j in range(idx, min(idx + 40, len(toks))):
        if toks[j] == "Bookmaker":
            bm = j
            break
    if bm is None:
        return None
    # headers until Payout
    payout = None
    for j in range(bm + 1, min(bm + 12, len(toks))):
        if toks[j] == "Payout":
            payout = j
            break
    if payout is None:
        return None
    headers = toks[bm + 1:payout]  # outcome column names
    step = 2 + len(headers) + 1
    rows = []
    k = payout + 1
    while k + step <= len(toks):
        chunk = toks[k:k + step]
        if not chunk[-1].endswith("%"):
            break
        if re.fullmatch(r"[A-Z]{2}", chunk[0]):
            name = chunk[1]
            vals = chunk[2:2 + len(headers)]
            rows.append((name, vals))
            k += step
        else:
            break
    # compute best per column
    best = {}
    for ci, h in enumerate(headers):
        bv, bn = None, None
        for name, vals in rows:
            try:
                v = float(vals[ci])
            except (ValueError, IndexError):
                continue
            if bv is None or v > bv:
                bv, bn = v, name
        best[h] = (bv, bn)
    return headers, rows, best

if __name__ == "__main__":
    path = sys.argv[1]
    market = sys.argv[2]
    r = parse(path, market)
    if not r:
        print("NOT FOUND")
        sys.exit(1)
    headers, rows, best = r
    print("market:", market)
    print("headers:", headers)
    for h in headers:
        print(f"  best {h}: {best[h][0]} ({best[h][1]})")
