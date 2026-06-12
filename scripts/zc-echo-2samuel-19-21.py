"""
echo — 2 Samuel 19–21
run: python3 scripts/zc-echo-2samuel-19-21.py

Ch19: David's return to Jerusalem — grief over Absalom, mercy to Shimei
Ch20: Sheba's rebellion — the rejected-king cry; wise woman of Abel
Ch21: Gibeonite reparations — bloodguilt atonement; Rizpah's vigil; the lamp of Israel
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

SAMUEL2_ECHO = {
  "19": {
    "4": [
      {"type": "allusion", "target": "Luke 15:20", "note": "David wept as he went, crying: O my son Absalom, O Absalom, my son, my son! — the king's consuming grief over the rebellious son who tried to kill him and who is now dead is the OT's most raw image of paternal love that outweighs the son's offense; it provides emotional content for the parable of the prodigal: when the father saw him a long way off he ran to meet him — the father's posture of longing, not vindication, is what drives the reunion"},
      {"type": "allusion", "target": "2 Cor 5:19", "note": "David's grief: he would rather have died in Absalom's place — the king who would substitute himself for the guilty son is the emotional ground for the NT substitution theology: God was in Christ reconciling the world to himself, not counting their trespasses against them; the father's willingness to absorb the son's penalty rather than enforce it is the logic of the atonement"}
    ],
    "23": [
      {"type": "allusion", "target": "Luke 23:34", "note": "David said to Shimei: You shall not die — on the day of the king's return in victory, David extends full pardon to the man who had cursed him during his flight; the victorious king's first acts include mercy to his enemies; Jesus's first words from the cross after his enemies have crucified him are: Father, forgive them, for they know not what they do"}
    ]
  },
  "20": {
    "1": [
      {"type": "allusion", "target": "John 1:11", "note": "Sheba the Benjaminite blew the trumpet and said: We have no portion in David, and we have no inheritance in the son of Jesse; every man to his tents, O Israel — the exact cry that fractures the kingdom after Solomon (1 Kgs 12:16); the pattern is the pattern of John 1:11: he came to his own and his own people did not receive him; the rejection of the Davidic king by the northern tribes anticipates the rejection of the Davidic Messiah by Israel"},
      {"type": "allusion", "target": "1 Kgs 12:16", "note": "Sheba's cry — We have no portion in David — is word-for-word the secessionist formula that will split the kingdom after Solomon; 2 Sam 20 is the dress rehearsal for the permanent division; the Davidic claim to rule all Israel is contested from within his own lifetime, and the contest intensifies through the divided monarchy until the exile"}
    ]
  },
  "21": {
    "3": [
      {"type": "allusion", "target": "Heb 9:22", "note": "David asks the Gibeonites: How shall I make atonement (kaphar), that you may bless the heritage of YHWH? — the question assumes that bloodguilt requires blood to be answered; the Gibeonites refuse silver and gold (v4) and demand seven of Saul's male descendants; the principle that without the shedding of blood there is no forgiveness of sins (Heb 9:22) is operative here: the accumulated bloodguilt of Saul's violation of the Gibeonite covenant (Josh 9) can only be resolved by death, not by financial compensation"}
    ],
    "17": [
      {"type": "allusion", "target": "John 8:12", "note": "Abishai saves David from Ishbi-benob; his men swear: You shall no longer go out with us to battle, lest you quench the lamp of Israel — David is called the lamp of Israel (ner yisrael), the dynastic light whose continuation is essential to the covenant people; the metaphor is developed in the Psalms (Ps 132:17: I have prepared a lamp for my anointed) and reaches its fulfillment in Jesus: I am the light of the world; whoever follows me will not walk in darkness but will have the light of life (John 8:12)"},
      {"type": "allusion", "target": "Rev 21:23", "note": "The lamp of Israel (ner yisrael) — David as the bearer of the dynastic light whose extinction would leave Israel in darkness — is the OT root of the NT lamplight imagery; Revelation applies the same logic to Christ in the new Jerusalem: the city has no need of sun or moon, for the glory of God gives it light, and its lamp is the Lamb; the Davidic lamp is fulfilled in the eternal Lamb who is the light that cannot be quenched"}
    ]
  }
}

def main():
    e = load_echo('2samuel')
    merge_echo(e, SAMUEL2_ECHO)
    save_echo('2samuel', e)
    print('2samuel ch19-21 echo: done')

if __name__ == '__main__':
    main()
