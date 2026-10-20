# Data dictionary: 06-minors-as-founders - bibliometrics files

Generated 2026-10-17 by `_tools/depth-kit/appendix.py`. All files below were built from free databases (OpenAlex, Crossref, Semantic Scholar, ERIC, arXiv, OpenCitations) on the dates in `data/raw/query_log.csv`; access date = pull date unless a row says otherwise.

## Files

| Path (under `bibliometrics\`) | What it is | Rows | Columns | Known problems |
|---|---|---|---|---|
| `config.json` | every setting of the run: queries, inclusion/exclusion rules, seeds, manual_exclude (hand-screen exclusions with reasons), evidence relation text | 16 | JSON |  |
| `evidence-table.csv` | the 30-60 most relevant papers with study type, data, method, one-line finding, read status, relation to the paper | 61 | 19 | Findings from abstracts unless read_status says full text; hand-screened and patched after the automatic selection. |
| `data/api_log.json` | log of API calls, cache hits and errors | 395 | JSON | Contains no personal identifier. |
| `data/clean/bibliometrix_M.rds` | bibliometrix data frame (M) as saved R object |  | R data frame |  |
| `data/clean/bibliometrix_input.csv` | master table reshaped to Web of Science field tags for bibliometrix | 926 | 29 | CR (cited references) built from OpenAlex referenced_works labels; only references resolved within the cap are labelled. |
| `data/clean/citation_edges.csv` | direct citation links between corpus records (citing, cited: OpenAlex ids) | 1058 | 2 | Only links where OpenAlex has the reference list. |
| `data/clean/cited_references.csv` | works cited by corpus records, with how often and how many are in the corpus | 4934 | 10 | Capped number of references resolved to metadata (see refs_stats.json). |
| `data/clean/corpus_final.jsonl.gz` | corpus after one snowball round, raw OpenAlex JSON per line | 994 | JSON per line | Written BEFORE hand-screen exclusions: master.csv has fewer rows (the exclusions in config.json manual_exclude are applied in the master stage). |
| `data/clean/corpus_stage1.jsonl.gz` | OpenAlex records that passed the title pre-screen and the topical screen (before snowballing) | 928 | JSON per line | Raw OpenAlex JSON per line. |
| `data/clean/evidence-table.autogen.csv` | the automatic evidence table before hand-screening (kept for comparison) | 62 | 18 |  |
| `data/clean/evidence_candidates.json` | ranked candidates for the evidence table | 70 | JSON |  |
| `data/clean/evidence_notes.json` | per-paper evidence-table fields (study type, method, finding from abstract, relation) | 62 | JSON | Findings come from abstracts only. |
| `data/clean/handscreen_exclusions.json` | OpenAlex ids excluded by hand-screen, with reason | 68 | JSON |  |
| `data/clean/master.csv` | one row per corpus record: the cleaned master table | 926 | 49 | Abstracts missing for part of the records; keywords are OpenAlex machine-assigned. |
| `data/clean/master.rds` | master.csv as an R data frame |  | R data frame |  |
| `data/clean/prisma_search.json` | PRISMA-style counts for the search stage | 10 | JSON |  |
| `data/clean/prisma_snowball.json` | PRISMA-style counts for the snowball stage | 11 | JSON |  |
| `data/clean/refs_stats.json` | counts of cited references and how many were resolved | 6 | JSON |  |
| `data/clean/screening_log_search.csv` | decision and reason for every candidate screened in the search stage | 1535 | 8 |  |
| `data/clean/screening_log_snowball.csv` | decision and reason for every candidate screened in the snowball stage | 1801 | 7 |  |
| `data/clean/snowball_central_papers.csv` | the most central corpus papers whose references and citations were snowballed | 25 | 6 |  |
| `data/clean/unresolved_candidates.csv` | search hits with no OpenAlex match (no DOI or not indexed) | 109 | 7 | These are lost to the map; check by hand if important. |
| `data/raw/all_hits.csv` | every hit returned by the discovery queries (Crossref, Semantic Scholar, ERIC, arXiv, seeds), before de-duplication | 9404 | 16 | Hits include off-topic records; duplicates across databases. |
| `data/raw/prior_work_ids.json` | OpenAlex ids/titles of papers named in the pack's prior-work notes, used as seeds | 3 | JSON | Titles that could not be matched are listed in run_search.log. |
| `data/raw/query_log.csv` | one row per query: database, search string, hits retrieved, date | 41 | 8 | Totals reported by Crossref are for the whole index, not for the topic. |
| `data/raw/crossref/` | raw API responses, 18 files, 3.5 MB (one file per query page; cached in `_tools/biblio-cache`) | | | Response formats differ by database; OpenAlex rate-limits. |
| `data/raw/eric/` | raw API responses, 2 files, 0.9 MB (one file per query page; cached in `_tools/biblio-cache`) | | | Response formats differ by database; OpenAlex rate-limits. |
| `data/raw/openalex/` | raw API responses, 3 files, 8.6 MB (one file per query page; cached in `_tools/biblio-cache`) | | | Response formats differ by database; OpenAlex rate-limits. |
| `data/raw/s2/` | raw API responses, 11 files, 9.1 MB (one file per query page; cached in `_tools/biblio-cache`) | | | Response formats differ by database; OpenAlex rate-limits. |
| `tables/` | 66 CSV tables: the numbers behind every figure (`R_*` from bibliometrix, `py_*` from Python) | | | see `figures/captions.md` for each caution |

## Variables

### master.csv

| Variable | Meaning and units |
|---|---|
| oa_id | OpenAlex work id (W...) |
| doi | DOI without URL prefix |
| title / year / date / type / language | bibliographic basics (OpenAlex) |
| source / source_type / publisher / issn | journal or venue and its type |
| authors / n_authors / first_author | author names, ';'-separated |
| institutions / countries / first_author_country / corresponding_country / international_collab | affiliations and ISO-2 country codes; international_collab = more than one country |
| cited_by_count / fwci / local_citations / n_refs | OpenAlex citations at pull date; field-weighted citation impact; citations from other corpus records; length of reference list |
| is_oa / oa_status / oa_url / best_pdf_url / all_pdf_urls / best_oa_landing | open-access status and links (OpenAlex) |
| sublit / sublits_all / origin / found_in / relevance | which sub-literature the record was found for; how it entered (search, snowball, seed); databases that returned it; relevance score used to rank evidence |
| primary_topic / subfield / field / domain / keywords / topics / concepts | OpenAlex classification (machine-assigned) |
| abstract / has_abstract | abstract text rebuilt from OpenAlex inverted index; flag |
| is_retracted | OpenAlex retraction flag |
| sr | short reference label used in bibliometrix |
| crossref_cited_by / crossref_n_refs / s2_citation_count / s2_pdf_url | cross-checks from Crossref and Semantic Scholar |

### evidence-table.csv

| Variable | Meaning and units |
|---|---|
| rank, citation, year, doi_or_link, open_access_link, oa_status, pdf_in_folder | identification and access |
| sub_literature, study_type, country_or_setting, data, method | coding by the agent from title and abstract |
| main_finding_from_abstract, read_status | one line from the abstract; 'abstract read' or 'metadata only' (no record was read in full unless marked) |
| relation_to_seans_paper | agent's judgement |
| local_citations, global_citations_openalex, openalex_id | citation counts at pull date |

### citation_edges.csv

| Variable | Meaning and units |
|---|---|
| citing, cited | OpenAlex ids; edge = citing record lists cited record in its references |

### tables/R_*.csv, tables/py_*.csv

| Variable | Meaning and units |
|---|---|
| (varies) | each table holds the numbers behind the figure of the same name; see figures/captions.md |

Counts (citations, records) have no unit beyond 'number of'; years are calendar years; `fwci` is a ratio (1 = world average for field, year and type).


---

# Paper-specific data (outside `bibliometrics\`)

This is a study of the law, not a statistical study: the "data" are saved official texts, case reports and secondary sources, and hand-built comparison tables. **Research notes, not legal advice; no qualified lawyer has verified them** (`followup\lawyer-check.md` lists what a lawyer must check). Sean is an adult; the study concerns the law on under-18s.

| Path | Source and access date | Size | Content, variables and problems |
|---|---|---|---|
| `raw\*.html`, `raw\*.txt` | Official statute pages and databases saved on 13-14 Oct 2026 (India Code, legislation.gov.uk, state code sites for California and Delaware, Singapore Statutes Online, ACRA, MCA pages and similar; file-name prefixes such as `acra_`, `ca_fam_`, `ca_corp_`), one `.html` raw capture and a `.txt` text extraction each | 277 files, 23 MB | Official or archive text. Some pages could not be read (MCA FAQ, several sites); where a capture failed the comparison table marks the cell "N". Statute text can change; the access date matters. |
| `followup\raw\*` | Second round of captures (Wayback copies, CourtListener-style case JSON `capx_*`, CDX indexes `cdx_*`, `bailii_wb_*`) by the follow-up agent, 17 Oct 2026 and earlier; log in `followup\raw\_fetch-log.txt` | 302 files | Read only by me for the dictionary; do not write there. |
| `03-comparison-table.csv` | hand-built from the sources above | 62 data rows x 6 columns | founder_act (the founder's act: age of majority, contract in own name, partner, LLP member, shareholder, director and so on), jurisdiction (India, UK (England and Wales), US, Singapore), status (the rule in one line), authority (statute section or case), verification (confidence code), note. |
| `followup\03-comparison-table-v2.csv` | the follow-up revision of the same table | 62 data rows x 8 columns | same columns plus `changed` (YES/no) and `what_changed` (the earlier value). Supersedes v1 where `changed` is YES. |
| Verification codes | defined in `03-comparison-table.md` | | (O) official text read; (O-IA) official text read through an Internet Archive capture; (S) reliable secondary copy read; (N) not read, rests on memory or practitioner notes and **must not be relied on**. |
| `02-sources-{india,uk,us,singapore}.md`, `followup\sources-official.md`, `followup\cases.md`, `followup\singapore-uk-points.md`, `followup\lawyer-check.md` | annotated source lists and checks | text | which source was opened in full, abstract only or metadata only. |

## Known problems
- Several statutory cells rest on secondary or unread sources (code N or S); the Singapore common-law age of 21 had no primary source read in the first table.
- US law is state law (California and Delaware were sampled).
- The literature map for this paper covers law poorly: citation databases hold few law-review articles and almost no Indian law-journal references. A separate open-repository supplement (`bibliometrics\tables\law_supplement_open_repositories.csv`) lists records from repositories that are **not** in the bibliometric corpus.
