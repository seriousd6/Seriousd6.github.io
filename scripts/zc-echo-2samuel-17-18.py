"""
Echo Commentary — 2 Samuel chapters 17–18
Run: python3 scripts/zc-echo-2samuel-17-18.py

Ch17: Ahithophel's counsel rejected — divine sovereignty overturning human wisdom;
      Ahithophel's suicide as the type of Judas
Ch18: David's intercession for Absalom — the father's love for the rebel son;
      Absalom caught by his glory-hair — pride that traps;
      David's lament 'would I had died instead of you'

Key OT→NT echo connections:
- 17:14 → 1 Cor 1:25 / Prov 19:21: divine wisdom confounding human counsel
- 17:23 → Matt 27:5 / Ps 41:9: the betrayer-friend who hangs himself
- 18:5 → Rom 5:10: the king's mercy toward his rebel enemy
- 18:33 → Luke 15:20 / 2 Cor 5:21: the father's substitutionary lament
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

ECHO = {
  "17": {
    "14": [
      {"type": "allusion", "target": "Prov 19:21", "note": "The narrator's theological aside — 'YHWH had ordained to defeat the good counsel of Ahithophel, so that YHWH might bring harm upon Absalom' — is the clearest statement in the Succession Narrative of divine sovereignty operating through the apparent randomness of human deliberation. Proverbs 19:21 ('many are the plans in a person's heart, but it is the purpose of YHWH that will stand') and 21:30 ('there is no wisdom or understanding or counsel against YHWH') are the proverbial condensations of what the narrative demonstrates: the best human strategy is rendered futile when YHWH has purposed otherwise."},
      {"type": "allusion", "target": "1 Cor 1:25", "note": "Ahithophel's counsel was genuinely excellent — Hushai's competing advice is presented as inferior militarily, yet it prevails because YHWH ordained it. Paul's argument in 1 Cor 1:25 ('the foolishness of God is wiser than men, and the weakness of God is stronger than men') is the theological principle being narratively demonstrated: what appears as the foolish choice (Hushai's delay plan) overturns what appears as the wise choice (Ahithophel's immediate strike), precisely because divine purpose operates above the calculus of human wisdom."}
    ],
    "23": [
      {"type": "allusion", "target": "Matt 27:5", "note": "Ahithophel's suicide by hanging — after his counsel is rejected and he foresees the outcome — is the OT's most direct type of Judas's suicide. Both were the trusted inner-circle advisor of the anointed king; both betrayed the king to his enemies; both hanged themselves when their betrayal moved toward its inevitable end. Psalm 41:9, attributed to David during Absalom's rebellion, describes the prototype: 'even my close friend in whom I trusted, who ate my bread, has lifted his heel against me.' Jesus applies this psalm to Judas in John 13:18, making explicit the typological chain from Ahithophel through Ps 41 to Judas."},
      {"type": "allusion", "target": "Ps 41:9", "note": "Ahithophel's betrayal narrative provides the historical backstory to Ps 41:9 ('my close friend in whom I trusted, who ate my bread, has lifted his heel against me'). David's psalm describes the reality of intimate betrayal by a covenant partner — the one who shared the table. Jesus's citation in John 13:18 ('I am not speaking of all of you; I know whom I have chosen. But the Scripture will be fulfilled, &ldquo;He who ate my bread has lifted his heel against me&rdquo;') establishes the typological chain: Ahithophel → Ps 41:9 → Judas. The betrayer who once ate at the king's table and then betrayed him to his enemies appears three times in redemptive history."}
    ]
  },
  "18": {
    "5": [
      {"type": "allusion", "target": "Rom 5:10", "note": "David's command to his commanders — 'deal gently for my sake with the young man Absalom' — is the king's explicit intercession of mercy for the son who had sought to kill him. Absalom is the enemy-son: he has stolen the kingdom, driven his father into exile, slept with his concubines in public, and sent armies to destroy him. Yet David's one command is mercy. Paul's statement in Rom 5:10 — 'while we were enemies, we were reconciled to God through the death of his Son' — is the NT counterpart: the Father's mercy toward the rebel children who had made themselves enemies. David's ḥanʿū lî layyeled lᵉʾaḇšālôm (deal gently for my sake with Absalom) is the OT narrative type of the divine mercy that seeks the redemption of the rebel."}
    ],
    "33": [
      {"type": "allusion", "target": "Luke 15:20", "note": "David's lament over Absalom — 'O my son Absalom, my son, my son Absalom! Would I had died instead of you, O Absalom, my son, my son!' — is the OT's most agonized expression of the father's love for the lost rebel son. Jesus's parable of the prodigal son (Luke 15:11-24) draws on exactly this emotional register: the father who runs to meet his returning son, who was 'dead and is alive, was lost and is found.' David's lament articulates what the parable assumes — the father's heart that breaks over the lost rebel rather than celebrating his just punishment."},
      {"type": "allusion", "target": "2 Cor 5:21", "note": "David's wish — 'would I had died instead of you' — is the substitutionary wish that David cannot actually fulfill; he would have died in place of Absalom if he could. This is the typological pointer to what the true David-son does accomplish: 2 Cor 5:21 ('for our sake he made him to be sin who knew no sin, so that in him we might become the righteousness of God'). The father-king who weeps 'would I had died instead of you' but cannot, points to the Son of David who does die instead of the rebellious sons — the substitutionary death that David's lament anticipates and Christ's atonement fulfills."}
    ]
  }
}

def main():
    e = load_echo('2samuel')
    merge_echo(e, ECHO)
    save_echo('2samuel', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'2samuel echo: wrote {count} verses across ch 17-18')

if __name__ == '__main__':
    main()
