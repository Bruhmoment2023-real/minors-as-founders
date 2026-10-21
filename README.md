# Ownership without agency: the legal position of founders under 18 in India, compared with England and Wales, California and New York

Sean Solano Paul, Independent researcher, Bengaluru, India. Funding: none. Competing interests: none.

## Summary

A growing business needs its founder to sign contracts, hold shares, sit on a board or join a
partnership, open accounts and register for tax. This is a legal and comparative study of which of
those acts a person under 18 may lawfully perform in India, compared with England and Wales,
California and New York. There is no statistical analysis and no analysis code: the "data" are
hand-built comparison tables, source notes citing the statutes and cases, and verification records.
A second check on 21 October 2026 replaced the paper's "not verified" cells: 20 were verified or
narrowed from official texts, and 8 (mostly New York common-law and banking-practice rows) now read
"not examined" (record in `docs/verification/not-verified-cells-2026-10-21.md`; for those cells it
supersedes the tables in `data/`). These are research notes, not legal advice, and no qualified lawyer has checked them.

## Layout

| Path | Contents |
|---|---|
| `data/03-comparison-table.csv` / `.md` | First comparison table (act by jurisdiction) with verification codes |
| `data/03-comparison-table-v2.csv` / `.md` | Revised table after the follow-up verification round |
| `docs/sources/02-sources-{india,uk,us,singapore}.md` | Source notes per jurisdiction: statute section, case, URL, access date |
| `docs/01-prior-work.md`, `docs/04-argument-map.md` | Prior-work review and the argument map |
| `docs/verification/` | Follow-up records: `cases.md`, `sources-official.md`, `singapore-uk-points.md`, `novelty-final.md`, and `not-verified-cells-2026-10-21.md` (second check of the England and Wales, US and Singapore cells) |
| `docs/citations/` | `references.bib`, `references.ris` |
| `docs/appendix/` | Data dictionary for the literature map, `evidence_handpatch.py`, `rerun.ps1` |
| `bibliometrics/` | Literature map (926 records): scripts, search protocol, cleaned corpus tables, figures |

## How to reproduce

The comparison tables are built by hand from the sources listed in `docs/sources/`. To check a cell,
open the cited statute or case at the URL and access date given. The only code is the optional
literature-map pipeline in `bibliometrics/python/` and `bibliometrics/R/` (Python 3.12 with
`pip install -r requirements.txt`; R 4.5 with the bibliometrix package). It needs network access,
takes about 1.5 hours, and returns a different corpus on a later date. `docs/appendix/rerun.ps1`
shows the order used; its paths are the author's and need editing.

## Data sources and licences

| Source | Used for | Licence / status |
|---|---|---|
| Statutes and case reports (India Code, legislation.gov.uk, California and New York codes, Singapore Statutes Online, case databases) | Cited by section, case, URL and access date in `docs/sources/` | Not copied into this repository; read at the cited URLs |
| OpenAlex, Crossref, Semantic Scholar, ERIC metadata | Literature map | Open metadata (OpenAlex CC0); email addresses in third-party records redacted |
| Author's comparison tables, notes, figures | | CC BY 4.0 (`LICENSE-DATA.md`); code MIT (`LICENSE`) |

## Not included and why

- Abstract text of third-party papers (the `abstract`/`AB` columns and abstract-derived quote columns of the bibliographic tables, and abstract fields in the OpenAlex JSON). Identifiers, titles, years, venues, keywords and citation data are kept; re-fetch abstracts with the bibliometrics pipeline if needed.
- Per-paper reading notes on the literature (they contain quotations from copyrighted papers) and the literature gap-analysis note (scoping). The scripts that built the notes are kept; run them on your own copies of the papers.
- Saved copies of statute pages, case reports and web pages (`raw/`, `followup/raw/`, about 550 files, including Wayback copies and case JSON): publishers' terms may apply and most are not public-domain government text. Use the citations and URLs in `docs/sources/` instead.
- Journal-article PDFs and extracted full text (`bibliometrics/pdfs/`, `depth/reading-notes/_text/`): copyrighted; fetch via DOIs in `docs/citations/references.bib`.
- Raw per-query literature API dumps (`bibliometrics/data/raw/{crossref,eric,openalex,s2}`): reproducible with `bibliometrics/python/pipeline.py`. `all_hits.csv` is kept, emails redacted.
- Internal status/venue/outline/checklist files, caches, virtual environments.
- No file larger than 50 MB was found.

## Citation

See `CITATION.cff`. Solano Paul, S. (2026). *Ownership without agency: the legal position of founders under 18 in India, compared with England and Wales, California and New York* (source tables and notes). Independent researcher. A Zenodo DOI will be added when the repository is made public.
