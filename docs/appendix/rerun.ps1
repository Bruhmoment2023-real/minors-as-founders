<#
Rebuild the main results of paper 06 (legal capacity of under-18s to found and run businesses: India, UK, US, Singapore) from raw data.
This is a study of the law: there is no statistical analysis code. The reproducible part is the literature map and depth layers 2-3.
Usage:  powershell -File rerun.ps1 [-Quick]
  -Quick  check that D: is present, the kit is intact, and that master.csv / citation_edges.csv load; no network.
Full run: about 1.5 hours, mostly waiting for the OpenAlex / Crossref / Semantic Scholar APIs (rate-limited). A later date gives a different corpus.
Nothing here writes to followup\ or raw\ .
#>
param([switch]$Quick)
$ErrorActionPreference = 'Stop'
if (-not (Test-Path 'D:\')) { throw 'D: is missing - stopping.' }
$P = 'D:\Research-Publishing\06-minors-as-founders'; $b = "$P\bibliometrics"
$bpy = 'D:\Research-Publishing\_tools\biblio-venv\Scripts\python.exe'
$env:PYTHONIOENCODING = 'utf-8'
if ($Quick) {
  & $bpy -c "import pandas as pd; m=pd.read_csv(r'$b\data\clean\master.csv',keep_default_na=False); e=pd.read_csv(r'$b\data\clean\citation_edges.csv'); print('master rows',len(m),'edges',len(e))"
  foreach ($f in 'pipeline.py','figures.py','pdfs.py','docs.py','law_supplement.py','topic_chart_06.py') { & $bpy -c "import ast; ast.parse(open(r'D:\Research-Publishing\_tools\biblio-kit\$f',encoding='utf-8').read()); print('syntax ok: $f')" }
  return
}
& $bpy 'D:\Research-Publishing\_tools\biblio-kit\pipeline.py' $b search enrich snowball refs master
if (Test-Path "$b\data\clean\handscreen_exclusions.json") { & $bpy 'D:\Research-Publishing\_tools\biblio-kit\handscreen.py' $b apply; & $bpy 'D:\Research-Publishing\_tools\biblio-kit\pipeline.py' $b master }
& powershell -NoProfile -File 'D:\Research-Publishing\_tools\biblio-kit\finish.ps1' '06-minors-as-founders'   # R, figures, law supplement, evidence table, PDFs, docs
Copy-Item "$b\evidence-table.csv" "$b\data\clean\evidence-table.autogen.csv" -Force
& $bpy "$P\depth\appendix\evidence_handpatch.py"   # hand-screened evidence table
& $bpy 'D:\Research-Publishing\_tools\depth-kit\burst_mainpath.py' $b
& $bpy 'D:\Research-Publishing\_tools\depth-kit\country_map.py' $b IND,GBR,USA,SGP
& $bpy 'D:\Research-Publishing\_tools\depth-kit\citations.py' $P "$P\depth\citations\extra_nodoi.json"
& $bpy 'D:\Research-Publishing\_tools\depth-kit\appendix.py' $P "$P\depth\appendix\_extra_dictionary.md"
