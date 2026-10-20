# Scopus and Web of Science queries - paper 06 (minors as founders)

Status: **not run.** There is no Scopus or Web of Science login on this machine. `scopus-drop\` was empty on 2026-10-13.

Read this first
- Citation databases cover legal scholarship poorly. Scopus and WoS index a minority of law journals (mostly peer-reviewed, commercially published ones); most US student-edited law reviews, almost all Indian law journals, practitioner texts, Law Commission reports and treatises are missing. Expect small result sets for sub-literatures A and C.
- The databases that actually cover this literature need a library login: **HeinOnline** (Law Journal Library), **Westlaw / Lexis+** (journals and commentary), **SCC OnLine** and **Manupatra** (India), **LawNet** (Singapore). Suggested strings for those are at the end.
- Save Scopus/WoS exports into `bibliometrics\scopus-drop\` (CSV, BibTeX or plain text with cited references) and re-run `R\bibliometrix_analysis.R`.

## A. Minors' contractual capacity and the infancy doctrine

Scopus
```
TITLE-ABS-KEY ( "infancy doctrine" OR "infancy defen?e" OR "minors' contract*" OR "minor's contract*" OR "contracts with minors" OR "contracts by minors" OR "age of majority" OR "Mohori Bibee" OR "emancipat* minor*"
  OR ( ( minor OR minors OR infant* OR children OR adolescent* OR teenager* OR "young person*" ) W/8 ( "contractual capacity" OR "capacity to contract" OR "legal capacity" OR disaffirm* OR voidable OR necessaries ) ) )
AND NOT TITLE ( medical OR "consent to treatment" OR health OR abortion OR contracept* OR vaccin* OR sexual OR marriage OR criminal OR "juvenile justice" OR asylum OR disabilit* OR dementia OR psychiatr* OR voting )
AND ( LIMIT-TO ( SUBJAREA , "SOCI" ) OR LIMIT-TO ( SUBJAREA , "BUSI" ) OR LIMIT-TO ( SUBJAREA , "ECON" ) OR LIMIT-TO ( SUBJAREA , "ARTS" ) )
```
Web of Science
```
TS=("infancy doctrine" OR "infancy defen$e" OR "minors' contract*" OR "minor's contract*" OR "contracts with minors" OR "contracts by minors" OR "age of majority" OR "Mohori Bibee" OR "emancipat* minor*"
  OR ((minor OR minors OR infant* OR children OR adolescent* OR teenager* OR "young person*") NEAR/8 ("contractual capacity" OR "capacity to contract" OR "legal capacity" OR disaffirm* OR voidable OR necessaries)))
NOT TI=(medical OR "consent to treatment" OR health OR abortion OR contracept* OR vaccin* OR sexual OR marriage OR criminal OR "juvenile justice" OR asylum OR disabilit* OR dementia OR psychiatr* OR voting)
```
Refine by Web of Science Categories: Law; Business; Family Studies; Social Issues.

## B. Youth and adolescent entrepreneurship

Scopus
```
TITLE-ABS-KEY ( "youth entrepreneur*" OR "young entrepreneur*" OR "adolescent entrepreneur*" OR "teen* entrepreneur*" OR "child entrepreneur*" OR kidpreneur* OR "minor entrepreneur*"
  OR ( ( adolescen* OR teenager* OR "high school student*" OR "secondary school student*" OR minors OR "under 18" ) W/8 ( entrepreneur* OR "start-up*" OR startup* OR "business ownership" OR "self-employ*" ) ) )
AND PUBYEAR > 1989 AND ( LIMIT-TO ( LANGUAGE , "English" ) )
AND ( LIMIT-TO ( SUBJAREA , "BUSI" ) OR LIMIT-TO ( SUBJAREA , "ECON" ) OR LIMIT-TO ( SUBJAREA , "SOCI" ) OR LIMIT-TO ( SUBJAREA , "PSYC" ) )
```
Web of Science
```
TS=("youth entrepreneur*" OR "young entrepreneur*" OR "adolescent entrepreneur*" OR "teen* entrepreneur*" OR "child entrepreneur*" OR kidpreneur* OR "minor entrepreneur*"
  OR ((adolescen* OR teenager* OR "high school student*" OR "secondary school student*" OR minors OR "under 18") NEAR/8 (entrepreneur* OR "start-up*" OR startup* OR "business ownership" OR "self-employ*")))
AND PY=(1990-2026) AND LA=(English)
```

## C. Company, partnership and LLP law on member and director eligibility

Scopus
```
TITLE-ABS-KEY ( ( ( director* OR shareholder* OR incorporat* OR "Companies Act" OR partnership OR LLP OR "limited liability partnership" ) W/10 ( minor OR minors OR infant* OR "under age" OR underage OR "minimum age" OR "age limit*" OR "age requirement*" OR "under 18" OR "under 16" ) )
  OR "director* eligibility" OR "directors' qualification*" OR "qualification of directors" OR "disqualification of directors" OR "director disqualification" OR "eligibility to be a director" OR "minor partner*" OR "minor shareholder*" OR "benefits of partnership" )
AND NOT TITLE ( "minority shareholder*" OR mining OR mineral* )
AND ( LIMIT-TO ( SUBJAREA , "SOCI" ) OR LIMIT-TO ( SUBJAREA , "BUSI" ) OR LIMIT-TO ( SUBJAREA , "ECON" ) )
```
Web of Science
```
TS=(((director* OR shareholder* OR incorporat* OR "Companies Act" OR partnership OR LLP OR "limited liability partnership") NEAR/10 (minor OR minors OR infant* OR "under age" OR underage OR "minimum age" OR "age limit*" OR "age requirement*" OR "under 18" OR "under 16"))
  OR "director* eligibility" OR "directors' qualification*" OR "qualification of directors" OR "disqualification of directors" OR "director disqualification" OR "eligibility to be a director" OR "minor partner*" OR "minor shareholder*" OR "benefits of partnership")
NOT TI=("minority shareholder*" OR mining OR mineral*)
```

## Narrow "direct analogue" query (run first)

Scopus
```
TITLE-ABS-KEY ( ( minor OR minors OR "under 18" OR underage OR adolescen* OR teenager* OR child* ) AND ( entrepreneur* OR founder* OR "start-up*" OR startup* OR "business owner*" )
  AND ( "legal capacity" OR "contractual capacity" OR "capacity to contract" OR "infancy doctrine" OR "age of majority" OR "Companies Act" OR incorporat* OR "company law" OR "partnership law" OR "legal barrier*" ) )
```
Web of Science
```
TS=((minor OR minors OR "under 18" OR underage OR adolescen* OR teenager* OR child*) AND (entrepreneur* OR founder* OR "start-up*" OR startup* OR "business owner*")
  AND ("legal capacity" OR "contractual capacity" OR "capacity to contract" OR "infancy doctrine" OR "age of majority" OR "Companies Act" OR incorporat* OR "company law" OR "partnership law" OR "legal barrier*"))
```

## Strings for the legal databases (need a library or mentor login)

HeinOnline (Law Journal Library, full-text, "Advanced Search")
```
("infancy doctrine" OR "minors' contracts" OR "contractual capacity of minors" OR "capacity of infants") AND (business OR entrepreneur* OR "sole proprietor*" OR partnership OR corporation OR "limited liability company")
```
```
(minor OR infant) w/10 (director OR incorporator OR shareholder OR "member of a limited liability company" OR partner) AND (capacity OR eligib* OR "age requirement")
```
Westlaw / Lexis+ (Secondary Sources: Law Reviews & Journals; terms-and-connectors)
```
(infan! minor) /s (disaffirm! void! capacit!) /p (business entrepreneur! partnership corporat! "limited liability company" L.L.C.)
```
SCC OnLine / Manupatra (India; journals and case law)
```
"minor" AND ("admitted to the benefits of partnership" OR "section 30" OR "Mohori Bibee" OR "section 11" OR "competent to contract") 
"minor" AND ("director" OR "shareholder" OR "member of a company" OR "designated partner" OR "LLP")
```
LawNet (Singapore) / Singapore Academy of Law Journal
```
(minor OR infant) AND ("Minors' Contracts Act" OR "Civil Law Act" OR "section 35" OR "age of majority" OR "section 145 Companies Act" OR director)
```
