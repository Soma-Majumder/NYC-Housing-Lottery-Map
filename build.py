"""Rebuild index.html from template.html and the files in data/.

data/buildings.txt  one building per line: lat_offset lng_offset lottery_index borough units address
                    lat = 40 + lat_offset/1e4, lng = lng_offset/1e4 - 74.3
                    borough: 0 Manhattan, 1 Bronx, 2 Brooklyn, 3 Queens, 4 Staten Island
data/lotteries.txt  one lottery per line: name|status|end YYMMDD|flags|income tiers
                    status: 0 open, 1 reviewing, 2 filled, 3 closed
                    flags: 1 preservation, 2 senior; tiers: ext low.very low.low.moderate.middle.above
data/boroughs.json  simplified borough outlines as SVG paths (same projection as below)
Source: NYC Open Data, HPD Housing Connect lotteries (nibs-na6y, vy5i-a666).
"""
import json, math, re

C = math.cos(math.radians(40.7)); K = 1000
def proj(lng, lat): return (round((lng + 74.27) * C * K, 1), round((40.93 - lat) * K, 1))

B = []
for line in open("data/buildings.txt").read().rstrip("\n").split("\n"):
    a, b, i, bo, u, addr = line.split(" ", 5)
    x, y = proj(int(b) / 1e4 - 74.3, 40 + int(a) / 1e4)
    B.append([x, y, int(i), int(bo), int(u), addr])
L = open("data/lotteries.txt").read().rstrip("\n").split("\n")
labels = {"Manhattan": proj(-73.985, 40.80), "Bronx": proj(-73.87, 40.865), "Brooklyn": proj(-73.95, 40.64),
          "Queens": proj(-73.80, 40.715), "Staten Island": proj(-74.15, 40.585)}

t = open("template.html").read()
t = t.replace("__BOROS__", open("data/boroughs.json").read())
t = t.replace("__L__", json.dumps(L, ensure_ascii=False, separators=(",", ":")))
t = t.replace("__B__", json.dumps(B, ensure_ascii=False, separators=(",", ":")))
t = re.sub(r"const LBL=\{.*?\};", "const LBL=" + json.dumps({k: list(v) for k, v in labels.items()}) + ";", t)
open("index.html", "w").write(t)
print("wrote index.html")
