"""World maps for a paper's literature map: (left) countries named in titles/abstracts of corpus records (setting proxy), (right) countries of author affiliations.
Usage: python country_map.py <bibliometrics_dir> [highlight ISO-3 codes comma separated, e.g. IND,GBR,USA,SGP]
Reads tables/py_countries_named_in_text.csv (written by figures.py) and master.csv; boundaries from open GeoJSON cached in _tools/geo. Writes figures/py_11_country_map.png/.svg,
tables/py_country_map_counts.csv and appends a caption."""
import os, sys, json
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import pycountry
sys.path.insert(0, r"D:\Research-Publishing\_tools\biblio-kit")
import topic_util as T

B = os.path.abspath(sys.argv[1]); HL = (sys.argv[2].split(",") if len(sys.argv) > 2 else [])
M, cfg = T.load(B)
world = json.load(open(r"D:\Research-Publishing\_tools\geo\countries.geojson", encoding="utf-8"))


def a3_from_name(n):
    fix = {"Tanzania, United Republic of": "TZA", "Russian Federation": "RUS", "Korea, Republic of": "KOR", "Iran, Islamic Republic of": "IRN", "Viet Nam": "VNM", "Turkey": "TUR", "Türkiye": "TUR", "Czechia": "CZE", "Taiwan, Province of China": "TWN", "Palestine, State of": "PSE", "Bolivia, Plurinational State of": "BOL", "Venezuela, Bolivarian Republic of": "VEN", "Moldova, Republic of": "MDA", "Syrian Arab Republic": "SYR", "Brunei Darussalam": "BRN", "Lao People's Democratic Republic": "LAO"}
    if n in fix:
        return fix[n]
    try:
        return pycountry.countries.lookup(n).alpha_3
    except LookupError:
        return None


named = pd.read_csv(os.path.join(B, "tables", "py_countries_named_in_text.csv"))
named["a3"] = named.country_named.map(a3_from_name)
cn = dict(zip(named.a3, named.documents))
ac = M.countries.str.split("; ").explode()
ac = ac[ac.str.len() == 2].value_counts()
a2to3 = {}
for c2 in ac.index:
    try:
        a2to3[c2] = pycountry.countries.get(alpha_2=c2).alpha_3
    except Exception:
        pass
auth = {a2to3[c]: int(n) for c, n in ac.items() if c in a2to3}
out = pd.DataFrame({"named_in_title_abstract": pd.Series(cn), "author_affiliation_records": pd.Series(auth)}).fillna(0).astype(int)
out.index.name = "iso3"; out.sort_values("named_in_title_abstract", ascending=False).to_csv(os.path.join(B, "tables", "py_country_map_counts.csv"), encoding="utf-8-sig")


def draw(ax, data, cmapname, title):
    vmax = max(data.values()) if data else 1
    cm = plt.get_cmap(cmapname)
    for f in world["features"]:
        a3 = f["properties"].get("ISO3166-1-Alpha-3"); nm = f["properties"].get("name", "")
        if nm == "Antarctica":
            continue
        n = data.get(a3, 0)
        g = f["geometry"]; polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poly in polys:
            ring = np.array(poly[0])
            if len(ring) > 60:
                ring = ring[::4]
            ax.add_patch(Polygon(ring, closed=True, facecolor=cm(0.15 + 0.85 * n / vmax) if n else "#ececec", edgecolor="#d00000" if a3 in HL else "white", lw=0.7 if a3 in HL else 0.25))
    if "SGP" in HL:
        ax.scatter([103.8], [1.35], s=90, facecolors="none", edgecolors="#d00000", linewidths=1.4, zorder=5)
    ax.set_xlim(-170, 180); ax.set_ylim(-58, 84); ax.set_aspect(1.2); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title, fontsize=10, loc="left")
    sm = plt.cm.ScalarMappable(cmap=cm, norm=plt.Normalize(0, vmax)); plt.colorbar(sm, ax=ax, shrink=0.6, pad=0.01, label="Records")
    top = sorted(data.items(), key=lambda kv: -kv[1])[:6]
    ax.text(-168, -56, "Most: " + "; ".join(f"{k} {v}" for k, v in top), fontsize=8, va="bottom")


fig, axs = plt.subplots(2, 1, figsize=(11, 9.5), constrained_layout=True)
draw(axs[0], cn, "YlOrRd", "Countries named in titles/abstracts (setting proxy)")
draw(axs[1], auth, "Blues", "Countries of author affiliations (records with affiliation data)")
hl = (" Red outline = " + ", ".join(HL) + " (Singapore ringed).") if HL else ""
fig.suptitle(f"Where do the studies come from? {len(M)} corpus records ({cfg['paper_id']}){hl}", x=0.01, ha="left", fontweight="bold", fontsize=11)
T.save(fig, B, "py_11_country_map")
T.caption(B, "py_11_country_map.png", "Country map of where the studies come from",
          "Top: world map shaded by how many corpus records name each country in the title or abstract. Bottom: shaded by the countries of author affiliations. Red outlines mark the study's focus jurisdictions.",
          "Country names matched in title+abstract (table py_countries_named_in_text.csv) and OpenAlex author-affiliation country codes (master.csv); boundaries from open GeoJSON (datasets/geo-countries) cached in _tools/geo; counts in tables/py_country_map_counts.csv.",
          "A country named in an abstract is a proxy for setting, not proof; many law records have no abstract or no affiliation data (OpenAlex covers law and non-English journals poorly), so thin shading can mean thin indexing rather than thin scholarship.")
print(out.sort_values("named_in_title_abstract", ascending=False).head(8))
