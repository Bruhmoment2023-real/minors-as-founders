# Search protocol - 06-minors-as-founders

- Paper question: The legal capacity of under-18s to found and run businesses in India, the UK, the US and Singapore
- Date of search and data pull: **2026-10-13**
- Years covered: 1950-2026; language: English (OpenAlex language field `en` or missing)
- Built by an AI agent (Claude) with the scripts in `python\` and `R\`; all numbers below are read from the run logs.

## 1. Databases

| Role | Database | Access | Note |
|---|---|---|---|
| Discovery | Crossref REST API | free, no key, `mailto` polite pool | relevance-ranked keyword search; top N per query |
| Discovery | Semantic Scholar Graph API (bulk search) | free, no key | boolean search on title/abstract; top N by citations per query |
| Discovery | ERIC API | free, no key | education topics only |
| Discovery | arXiv API | free, no key | preprints |
| Enrichment (authors, institutions, countries, topics, keywords, abstracts, references, citation counts, OA links) | **OpenAlex** single-record lookups (`/works/doi:...`, `/works/mag:...`, `/works/W...`) | free, no key | see limit 1 below |
| Forward citations for snowballing | OpenCitations Index API v2 | free, no key | DOI-to-DOI citations only |
| Cross-check | Crossref (per-DOI), Semantic Scholar (batch) | free, no key | citation counts and reference-list coverage compared in `tables\coverage_crosscheck.csv` |
| Not used | Scopus, Web of Science, Lens, Dimensions | need accounts | equivalent strings are in `scopus-queries.md` |
| Not usable | RePEc/IDEAS | its API needs a registered access code; the public search page returned no parseable result list to a script | economics working papers still enter via Crossref, Semantic Scholar and snowballing |

**Why OpenAlex was not the search engine.** Since 2026 OpenAlex charges keyless list/search calls against a small daily budget shared by everyone on the same IP address ($0.10/day). On the day of the pull that budget was already exhausted by other work on this network, and an API key needs an account (ruled out). Single-record lookups remain free and unlimited, so records were *discovered* in Crossref / Semantic Scholar / ERIC / arXiv and then *enriched* one by one from OpenAlex. Consequence: a work that is in OpenAlex but not found by any of the four discovery databases is missed, except where snowballing caught it.

## 2. Exact search strings

### A_minors_contractual_capacity: Minors' contractual capacity and the infancy doctrine

| database | query | hits in database | records retrieved | status |
|---|---|---|---|---|
| crossref | infancy doctrine contracts minors | 113849.0 | 250 | ok |
| crossref | minors contractual capacity law | 1705453.0 | 250 | ok |
| crossref | contracts with minors voidable disaffirmance necessaries | 54726.0 | 250 | ok |
| crossref | minor's agreement Indian Contract Act Mohori Bibee | 1050111.0 | 250 | ok |
| crossref | Minors' Contracts Act 1987 capacity | 1559064.0 | 250 | ok |
| crossref | children online contracts capacity law | 3773433.0 | 250 | ok |
| crossref | age of majority contract law reform | 2407794.0 | 250 | ok |
| s2 | "infancy doctrine" \| "infancy law doctrine" \| "minors' contracts" \| "contracts with minors" \| "contractual capacity of minors" \| "minor's contract" \| "minors contracts" | 107.0 | 107 | ok |
| s2 | (minor \| minors \| infants \| children \| adolescents) + ("capacity to contract" \| "contractual capacity" \| disaffirm \| disaffirmance \| "voidable contract" \| "voidable contracts" \| necessaries) | 183.0 | 183 | ok |
| s2 | (minors \| children \| teenagers) + contracts + (online \| "e-commerce" \| internet \| "social media" \| gaming \| influencers) + (law \| legal \| capacity) | 562.0 | 562 | ok |
| s2 | "age of majority" + (contract \| contracts \| capacity \| law) | 451.0 | 451 | ok |
| s2 | "Mohori Bibee" \| ("Indian Contract Act" + (minor \| minors)) | 5.0 | 5 | ok |

### C_company_partnership_eligibility: Company, partnership and LLP law on member/director eligibility

| database | query | hits in database | records retrieved | status |
|---|---|---|---|---|
| crossref | minor as partner Partnership Act admitted to benefits of partnership | 523129.0 | 250 | ok |
| crossref | minimum age company director Companies Act | 1296184.0 | 250 | ok |
| crossref | minors as shareholders members of a company law | 1648199.0 | 250 | ok |
| crossref | eligibility qualifications of company directors law | 1579242.0 | 250 | ok |
| crossref | limited liability partnership partners capacity minors | 558406.0 | 250 | ok |
| crossref | disqualification of company directors law | 1566119.0 | 250 | ok |
| s2 | (minor \| minors \| "minimum age" \| "under 18") + (director \| directors \| shareholder \| shareholders) + (company \| "Companies Act" \| corporate) + law | 137.0 | 137 | ok |
| s2 | (minor \| minors) + (partnership \| "Partnership Act" \| LLP \| "limited liability partnership") + (law \| legal \| capacity) | 373.0 | 373 | ok |
| s2 | "director eligibility" \| "directors' qualifications" \| "qualification of directors" \| "disqualification of directors" \| "minimum age for directors" \| "directors disqualification" | 245.0 | 245 | ok |

### B_youth_entrepreneurship: Youth and adolescent entrepreneurship

| database | query | hits in database | records retrieved | status |
|---|---|---|---|---|
| crossref | youth entrepreneurship | 407651.0 | 250 | ok |
| crossref | adolescent entrepreneurship teenage entrepreneurs | 469193.0 | 250 | ok |
| crossref | young entrepreneurs legal barriers age business registration | 3306856.0 | 250 | ok |
| crossref | entrepreneurship education secondary school students entrepreneurial intention | 5153986.0 | 250 | ok |
| crossref | minors as entrepreneurs legal capacity business | 1919547.0 | 250 | ok |
| s2 | "youth entrepreneurship" \| "young entrepreneurs" \| "adolescent entrepreneurship" \| "teen entrepreneurs" \| "teenage entrepreneurs" \| "child entrepreneurs" \| kidpreneurs \| "minor entrepreneurs" | 4410.0 | 800 | ok |
| s2 | (adolescents \| adolescence \| teenagers \| "high school students" \| "secondary school students") + (entrepreneurship \| entrepreneurial \| "entrepreneurial intention" \| "business ownership") | 2514.0 | 800 | ok |
| s2 | (youth \| "young people") + ("self-employment" \| entrepreneurship) + (barriers \| legal \| regulation \| "access to finance" \| age) | 2095.0 | 800 | ok |
| eric | "youth entrepreneurship" OR (entrepreneurship AND adolescents) | 124.0 | 124 | ok |
| eric | entrepreneurship AND ("high school students" OR "secondary school students") | 297.0 | 297 | ok |

Per-query retrieval caps: crossref = 250, s2 = 800, eric = 300, arxiv = 50. Crossref totals are large because its search is an OR-type relevance ranking; only the top-ranked records were taken. Raw responses for every query are in `data\raw\<database>\`.

### Seed papers (known key works, each verified to exist by a Crossref title match; they bypass the keyword rules)

| seed title | result |
|---|---|
| Infancy Doctrine Inquiries | NOT MATCHED in Crossref |
| CyberInfants | NOT MATCHED in Crossref |
| Youth Entrepreneurship: Meeting the Key Policy Challenges | NOT MATCHED in Crossref |
| Pathways to successful entrepreneurship: Parenting, personality, early entrepreneurial competence, and interests | matched 10.1016/j.jvb.2003.10.007 |
| Entrepreneurship as a twenty-first century skill: entrepreneurial alertness and intention in the transition to adulthood | matched 10.1007/s11187-016-9798-6 |
| Fostering Youth Entrepreneurship: Preliminary Findings From the Young Entrepreneurs Study | matched 10.1111/jora.12086 |
| Minors' Contracts: A Major Problem with the Indian Contract Act, 1872 | matched 10.1093/slr/hmy034 |
| The Minors' Contracts Act 1987 | NOT MATCHED in Crossref |
| Contracts for the Sale of Goods to Minors | NOT MATCHED in Crossref |
| Entrepreneurship among adolescents | NOT MATCHED in Crossref |

## 3. Inclusion and exclusion rules (applied identically to search hits and snowballed records)

A record is **included** if all of the following hold:
1. It resolves to an OpenAlex work record (by DOI, MAG id, or a Crossref title match of at least 93% similarity).
2. OpenAlex type is article, review, preprint, book chapter, book, dissertation, report or other (editorials, errata, paratext, datasets, peer reviews are dropped).
3. Publication year 1950-2026; language English or unrecorded.
4. It satisfies at least one sub-literature rule below: every `include` pattern must match in title + abstract, and every `title_must` pattern must match in the title.
5. Its title does not match the exclusion pattern.

Book-series and proceedings trap: a record whose abstract is a series/proceedings blurb (detected by wording such as 'this volume constitutes the refereed proceedings', or the same abstract shared by 3+ records) is screened on its title alone; whole-volume records (titles starting 'Proceedings of', 'Front matter', etc.) are dropped.

The patterns are case-insensitive regular expressions (`\b` = word boundary, `\w*` = any word ending, `.{0,80}` = within 80 characters).

**A_minors_contractual_capacity - Minors' contractual capacity and the infancy doctrine**

- include (title+abstract): `(infancy doctrine|infancy defen[cs]e|minors?'? ?contracts?|contracts? (with|by|of|made by|involving) (a )?(minors?|infants?|children)|\b(minors|a minor|minor's|infants?|children'?s?|adolescents?|young persons?|teenagers?)\b.{0,80}(contractual capacity|capacity to contract|contractual incapacity|legal capacity|disaffirm\w*|voidable|necessaries|enforceab\w+ (of )?contracts?)|(contractual capacity|capacity to contract|contractual incapacity|legal capacity|disaffirm\w*|voidable|necessaries).{0,80}\b(minors|a minor|minor's|infants?|children|adolescents?|teenagers?)\b|age of majority|mohori bibee|minors'? agreements?|emancipat\w+ (of )?minors?|emancipated minors?)`
- title_must (title): `(minors?\b|infan\w+|child\w*|adolescen\w+|teen\w*|young|youth|age of majority|under[- ]?age|capacity|emancipat\w+|\bkids?\b)`
- title_must (title): `(contract\w*|capacity|doctrine|majority|disaffirm\w*|emancipat\w+|agreements?|liabilit\w+|\blaw\b|legal|\bact\b|necessaries|e-?commerce|online|consumer)`

**C_company_partnership_eligibility - Company, partnership and LLP law on member/director eligibility**

- include (title+abstract): `((directors?|shareholders?|incorporat\w+|compan(y|ies) act|partnership|\bllp\b|limited liability partnership|corporat\w+).{0,90}(\bminors\b|\ba minor\b|\bminor's\b|\binfants?\b|under[- ]?age|minimum age|age (limit|requirement|restriction)s?|under (16|18|eighteen|sixteen))|(\bminors\b|\ba minor\b|\bminor's\b|\binfants?\b|under[- ]?age|minimum age|age (limit|requirement|restriction)s?).{0,90}(directors?|shareholders?|partnership|incorporat\w+|compan(y|ies) act|\bllp\b|limited liability partnership)|director(s|s'|ship)? (eligibility|qualifications?|disqualifications?)|disqualification of (company )?directors|eligibility (of|to be|for) (a )?(company )?(directors?|partners?)|minor (as )?(a )?(partner|shareholder|member|director)s?|benefits of (the )?partnership)`
- title_must (title): `(director\w*|shareholder\w*|partner\w*|compan\w+|corporat\w+|\bllp\b|incorporat\w+)`

**B_youth_entrepreneurship - Youth and adolescent entrepreneurship**

- include (title+abstract): `(\b(youth|young (people|persons?|entrepreneurs?|founders?|adults?)|adolescen\w+|teen\w*|minors|children|child|kid\w*|high school|secondary school|under[- ]?18)\b.{0,60}(entrepreneur\w*|start-?ups?|business (owners?|founders?|ownership|creation)|self[- ]employ\w*)|(entrepreneur\w*|start-?ups?|self[- ]employ\w*).{0,60}\b(youth|young (people|persons?|adults?)|adolescen\w+|teen\w*|minors|children|high school|secondary school)\b|kidpreneur\w*|teenpreneur\w*)`
- title_must (title): `(entrepreneur\w*|start-?ups?|business\w*|self[- ]employ\w*|enterpris\w+|venture\w*|founder\w*)`
- title_must (title): `(youth|young|adolescen\w+|teen\w*|minors?\b|child\w*|kid\w*|school\w*|juvenile|students?)`

**Exclusion pattern (title):** `(\bmedical|consent to (medical )?treatment|\bhealth|abortion|contracept|vaccin|sexual|marriage|criminal|juvenile justice|asylum|migra|disabilit|dementia|mental|psychiatr|elder|voting|suffrage|malaria|infect|\bhiv\b|infant (mortality|feeding|formula|nutrition|industr)|neonat|breast|pediatric|paediatric|preterm|\bbirth|alcohol|tobacco|smoking|drinking|firearm|driving|soldier|labou?r market|child labou?r|trafficking|custody|adoption|minority shareholder|mining|\bmineral|compensation|board (functions|committee)|clerkship|minor shareholders?|juvenile delinquen|child support|penal|land acquisition|best interests)`

A record matching several rules is assigned to the first one in the order listed (its other matches are kept in `sublits_all`).

## 4. Snowballing (one round)

- Central papers: the 25 corpus records ranked highest on local citations + topical relevance + log(global citations) - listed in `data\clean\snowball_central_papers.csv`.
- Backward: every OpenAlex `referenced_works` entry of those papers not already in the corpus (729 candidates).
- Forward: citing DOIs from OpenCitations, up to 150 per central paper (1072 candidates). OpenCitations only knows DOI-to-DOI links, so citing preprints and books without DOIs are missed.
- All candidates were looked up in OpenAlex and screened with the rules in section 3: 6 backward and 60 forward records were added.

## 5. PRISMA-style counts

| stage | n |
|---|---|
| Records identified through database searching (all query hits) | 9404 |
|    of which from crossref | 4500 |
|    of which from eric | 421 |
|    of which from s2 | 4463 |
|    of which from seed | 20 |
| Duplicates removed (same DOI / id / title across queries and databases) | 2052 |
| Unique records screened on title (+ abstract where the database supplied one) | 7352 |
| Removed at title pre-screen (off-topic) | 5817 |
| Records looked up in OpenAlex | 1535 |
| Duplicates removed after OpenAlex matching (same work / same title) | 13 |
| Excluded at full screen: offtopic_fails_inclusion_rule | 413 |
| Excluded at full screen: no_openalex_record (no DOI / not indexed) | 109 |
| Excluded at full screen: type_excluded | 57 |
| Excluded at full screen: language_not_english | 15 |
| Included after search screening | 928 |
| Snowball: central papers used | 25 |
| Snowball: backward-reference candidates | 729 |
| Snowball: forward-citation candidates (OpenCitations) | 1072 |
| Snowball: duplicates of corpus records | 4 |
| Snowball excluded: offtopic_fails_inclusion_rule | 1196 |
| Snowball excluded: no_openalex_record | 332 |
| Snowball excluded: offtopic_exclusion_term_in_title | 85 |
| Snowball excluded: language_not_english | 70 |
| Snowball excluded: type_excluded | 43 |
| Snowball excluded: year_out_of_range | 4 |
| Snowball excluded: paratext_or_container_record | 1 |
| Snowball: included (backward) | 6 |
| Snowball: included (forward) | 60 |
| Corpus before hand-screening | 994 |
| Removed at hand-screening (see tables/hand_screen_removed.csv) | 68 |
| FINAL CORPUS | 926 |
|    with abstract | 781 |
|    with DOI | 710 |
|    with a reference list in OpenAlex | 612 |
| Distinct cited references / resolved to metadata | 18230 / 4725 |

Figure: `figures\py_01_prisma_flow.png`.

## 6. Hand-screening

After rule screening and snowballing, the agent read the titles (with source and year) of the whole corpus and removed 68 records as off-topic or mis-matched; every removal and its reason is in `tables\hand_screen_removed.csv`. This is a single-screener pass by an AI agent on titles, not a two-person human screen; borderline records were kept.

Removal reasons:
- Off-topic: not about minors' legal capacity to contract or found/run businesses (medicine, forensic age estimation, criminology, family or human-rights law); hand-screened by title, 17 Oct 2026: 37
- Off-topic: not company/partnership/LLP member or director eligibility (health or school 'directors', finance or governance studies, Chinese 'minor' = minority shareholder papers); hand-screened by title, 17 Oct 2026: 31

## 7. Coverage and cross-checks

| item | value |
|---|---|
| corpus records | 926.0 |
| records with DOI | 710.0 |
| found in Crossref (DOI lookup) | 696.0 |
| found in Semantic Scholar (batch DOI lookup) | 682.0 |
| Spearman corr. OpenAlex vs Crossref cited-by | 0.928 |
| Spearman corr. OpenAlex vs Semantic Scholar cited-by | 0.893 |
| median cited-by: OpenAlex | 5.0 |
| median cited-by: Crossref | 4.0 |
| median cited-by: Semantic Scholar | 7.0 |
| records with no reference list in OpenAlex | 314.0 |
|   of which Crossref holds a reference list | 9.0 |
| records with no institution/country data | 320.0 |
| records without abstract | 145.0 |
| open-access records (OpenAlex) | 539.0 |
| origin: search | 841.0 |
| origin: snowball_forward | 60.0 |
| origin: seed | 19.0 |
| origin: snowball_backward | 6.0 |
| retrieved by: s2 | 830.0 |
| retrieved by: openalex_snowball | 66.0 |
| retrieved by: eric | 63.0 |
| retrieved by: seed | 19.0 |


- 109 title-screened candidates could not be matched to any OpenAlex record (no DOI or MAG id, or not indexed) and are **not** in the corpus. They are listed in `data\clean\unresolved_candidates.csv` (s2: 74, eric: 34, crossref: 1). ERIC reports and theses and Indian or legal journal articles without DOIs dominate this list.

- Cited references: 18230 distinct works are cited by the corpus (27086 links); 4725 of the 5000 outside the corpus were resolved to metadata for the co-citation and RPYS analyses.


### Named prior work (seed list / the substance agent's saved papers) - is it in the corpus?

| id | kind | in_corpus |
|---|---|---|
| 10.1007/s10991-022-09298-3 | doi | 1 |
| 10.1007/s10991-022-09308-4 | doi | 1 |
| 10.1080/14729342.2023.2189359 | doi | 1 |
| 10.1093/iclqaj/27.1.215 | doi | 1 |
| 10.1093/slr/hmy034 | doi | 1 |
| 10.17161/1808.20249 | doi | 1 |
| 10.2139/ssrn.1708215 | doi | 1 |
| 10.2139/ssrn.1918391 | doi | 1 |
| 10.2139/ssrn.2713782 | doi | 1 |
| 10.2139/ssrn.3526991 | doi | 1 |
| 10.2139/ssrn.6253578 | doi | 1 |
| 10.2307/1118483 | doi | 1 |
| 10.26686/vuwlr.v40i4.5254 | doi | 1 |
| 10.31142/ijtsrd16999 | doi | 1 |
| 10.31305/rrijm.2021.v06.i09.008 | doi | 1 |
| 10.37136/0515-016-002-014 | doi | 1 |

## 8. API failures during the run

- api.openalex.org: failed after retries: {"error":"Rate limit exceeded","message":"Rate l (x359)
- api.core.ac.uk: failed after retries:  (x27)
- api.core.ac.uk: failed after retries: {"message":"The HTTP status code \u00220\u0022 i (x9)


## 9. Scopus / Web of Science exports
- `scopus-drop\`: EMPTY - no Scopus/WoS export to merge; corpus is OpenAlex-only.
- Ready-to-paste strings: `scopus-queries.md`.
