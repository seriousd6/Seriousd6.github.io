"""
echo — 2 Kings 6–8
run: python3 scripts/zc-echo-2kings-6-8.py

Ch6: Iron axe-head; heavenly army (v17); blinded Arameans fed; Samaria besieged
Ch7: Siege lifted; lepers declare "a day of good news" (v9); unbelief punished
Ch8: Shunamite restored; Hazael anointed; lamp promise keeps Judah (v19)
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

KINGS2_ECHO = {
  "6": {
    "17": [
      {"type": "allusion", "target": "2 Cor 4:18", "note": "Elisha prays for his servant: YHWH, open his eyes that he may see — and the servant sees the mountain full of horses and chariots of fire surrounding Elisha; the invisible army of YHWH is more numerous than the Aramean force; Paul's exhortation to fix the eyes not on what is seen but on what is unseen (2 Cor 4:18) is the epistemological principle that Elisha's prayer demonstrates concretely: the unseen is the more real"},
      {"type": "allusion", "target": "Rom 8:31", "note": "Elisha's word to his frightened servant — do not be afraid, for those who are with us are more than those who are with them (v16) — is the experiential precedent for Paul's rhetorical question in Rom 8:31: if God is for us, who can be against us? The heavenly army visible to Elisha's servant is the same invisible divine protection Paul grounds Christian confidence in; the arithmetic of divine presence reverses the calculus of visible odds"}
    ],
    "22": [
      {"type": "allusion", "target": "Rom 12:20", "note": "Elisha instructs the king not to kill the captured Aramean army but to feed them and send them home — bread and water before them, so they ate and drank and went away; this is the most extended OT enactment of enemy-love before the Sermon on the Mount; Paul quotes Prov 25:21-22 in Rom 12:20 — if your enemy is hungry, feed him; if he is thirsty, give him something to drink — and Elisha's action is the narrative embodiment of that proverb; the radical hospitality that disarms enmity flows from YHWH's own character"}
    ]
  },
  "7": {
    "9": [
      {"type": "allusion", "target": "Isa 52:7", "note": "The four lepers at the gate of Samaria discover the abandoned Aramean camp and say to one another: We are not doing right. This is a day of good news (<em>yôm bəśôrāh</em>) and we are keeping silent — the first proclamation of deliverance comes from social outcasts; <em>bəśôrāh</em> is the Hebrew root of εὐαγγέλιον (gospel); Isa 52:7 celebrates the feet of the one who brings good news (<em>məbaśśēr</em>) of peace and salvation; Mark 1:15 announces the kingdom of God in the same vocabulary; the lepers at Samaria's gate enact the Isaianic pattern: the announcement of unexpected deliverance from an unlikely messenger"},
      {"type": "allusion", "target": "Mark 1:15", "note": "The lepers' declaration that this is a day of good news (<em>yôm bəśôrāh</em>) anticipates the inauguration of the gospel age; Jesus announces in Mark 1:15: the time is fulfilled, and the kingdom of God is at hand — repent and believe in the gospel (<em>euangelion</em>); the same structure: an unexpected reversal of siege (the Aramean army flees at the sound YHWH creates), announced by marginal figures, demanding a response; the lepers model the duty of those who receive good news: they cannot keep silent"}
    ],
    "20": [
      {"type": "allusion", "target": "Heb 3:19", "note": "Elisha prophesies that a seah of flour will sell for a shekel at the gate of Samaria by tomorrow (v1); the king's officer scoffs: if YHWH should make windows in heaven, could this happen? (v2); Elisha replies: you will see it with your eyes but you will not eat of it (v2); the prophecy is fulfilled exactly, and the officer is trampled to death at the gate — he sees the abundance but does not participate; Heb 3:19 articulates the same pattern: they were unable to enter because of unbelief; seeing the salvation without receiving it is the form unbelief takes when prophecy is fulfilled"}
    ]
  },
  "8": {
    "13": [
      {"type": "allusion", "target": "Jer 17:9", "note": "When Elisha tells Hazael he will become king of Aram and will do terrible things to Israel, Hazael recoils: what is your servant, who is a dog, that he should do this great thing? — the denial is sincere; Hazael cannot imagine himself capable of burning Israelite cities and killing children; yet he immediately murders Ben-hadad the next day (v15) and goes on to do exactly what Elisha predicted; the pattern is the same as Jer 17:9 — the heart is deceitful above all things, who can know it? — and as Peter's self-confident denial (Matt 26:35) that he would deny Jesus; the capacity for betrayal the self-assessment cannot see is the archetypal human blind spot"}
    ],
    "19": [
      {"type": "fulfillment", "target": "Luke 1:78", "note": "Though Jehoram king of Judah walked in the sins of the house of Ahab, YHWH was not willing to destroy Judah for the sake of David his servant, since he had promised to give him a lamp (<em>nēr</em>) for his sons always; this is the lamp/horn promise of 2 Sam 7:12-16, the linchpin of the Davidic covenant — even the apostasy of an Ahab-linked king cannot extinguish it; Luke 1:78 announces the fulfillment: the dawn from on high has visited us, to give light to those who sit in darkness and in the shadow of death; the lamp that YHWH refuses to extinguish through centuries of Judahite apostasy is finally, definitively lit in the incarnation of the Son of David"},
      {"type": "allusion", "target": "Ps 132:17", "note": "The lamp promise in v19 — YHWH gave a lamp to David and to his sons always — is the same <em>nēr</em> theology celebrated in Ps 132:17: there I will make a horn to sprout for David; I have prepared a lamp for my anointed; Elijah's complaint that he is the last faithful one (1 Kgs 19:10), the Baal-marriage of Jehoshaphat's son to Ahab's daughter, the attempted extermination of the Davidic line by Athaliah (2 Kgs 11) — all are the forces that should extinguish the lamp; the lamp endures not because of dynastic merit but because YHWH bound himself to the Davidic promise"}
    ]
  }
}

def main():
    e = load_echo('2kings')
    merge_echo(e, KINGS2_ECHO)
    save_echo('2kings', e)
    print('2kings ch6-8 echo: done')

if __name__ == '__main__':
    main()
