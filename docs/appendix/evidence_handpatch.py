import pandas as pd, os
os.chdir(r"D:\Research-Publishing\06-minors-as-founders\bibliometrics")
e = pd.read_csv(r"data\clean\evidence-table.autogen.csv", keep_default_na=False)
RN = "depth\\reading-notes\\"
drop = e.citation.str.contains("Palmer's company law manual", regex=False)
dropped = e[drop][['rank', 'citation']].copy()
dropped['reason'] = "metadata contaminated: OpenAlex assigns the book to a Medical Entomology and Zoology source; not checked against the book itself"
e = e[~drop].copy().reset_index(drop=True)
notes = {'Godha': 'godha-2018-capacity-of-minor.md', 'Cheong': 'cheong-2023-legal-transplant.md', 'Gilbert': 'gilbert-2009-minors-contracts-act.md',
         'Star, Divyangana': 'star-2022-minors-contracts.md', 'Pooja Jain': 'jain-2025-minors-indian-commercial-law.md', 'Austen': 'austen-baker-2020-infants-history.md',
         'Ho et al': 'ho-2018-adolescent-training.md', 'Campo-Ternera': 'campo-ternera-2022-adolescent-skills.md', 'Lalit Sharma, Pankaj Madan': 'sharma-2014-youth-entrepreneurship-uttarakhand.md',
         'Empowering Young Entrepreneurs': 'anon-2025-empowering-young-entrepreneurs.md', 'Moravec': 'moravec-2015-director-disqualification.md', 'Salleh': 'salleh-2019-infant-shareholders.md',
         'Winandra': 'winandra-2023-notary-minors.md', 'Taufiqurrahman': 'taufiqurrahman-2026-indonesia-capacity.md', 'Moon-Ho Ringo Ho': 'ho-2018-adolescent-training.md'}
full = {'Cheong', 'Gilbert', 'Star, Divyangana', 'Austen', 'Salleh'}
whole = {'Pooja Jain', 'Empowering Young Entrepreneurs', 'Godha'}
e['depth_reading_note'] = ''
for i, r in e.iterrows():
    for k, v in notes.items():
        if k in r.citation:
            e.at[i, 'depth_reading_note'] = RN + v
            e.at[i, 'read_status'] = 'full text read (key sections; see note)' if k in full else ('whole text read (short paper)' if k in whole else 'text partly read (abstract, key sections; see note)')
            break
e['rank'] = range(1, len(e) + 1)
e.to_csv('evidence-table.csv', index=False, encoding='utf-8-sig')
dropped.to_csv(r'tables\evidence_hand_screen_removed.csv', index=False, encoding='utf-8-sig')
print(len(e), e.read_status.value_counts().to_dict())
