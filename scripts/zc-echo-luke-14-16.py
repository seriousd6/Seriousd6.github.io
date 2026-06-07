"""
Echo layer — Luke chapters 14–16
Output: data/echoes/luke.json (adds chs 14–16)
Run: python3 scripts/zc-echo-luke-14-16.py

Key OT resonances:
- ch 14: Great Banquet (Isa 25:6); Sabbath healing (Isa 58:6)
- ch 15: Lost sheep (Ezek 34:11-12); Prodigal (Isa 49:15; Hos 11:1-4)
- ch 16: Two masters (Deut 6:5; Josh 24:15); Law to John (Mal 4:5);
         Rich man / Lazarus (Amos 6:4-6; Gen 25:8; Isa 63:16; Deut 31:9)

Chs 14-15 were written by a prior agent; merge_echo skips already-present keys.
This script adds ch 16 and re-asserts chs 14-15 for safety.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    # INTENT: Merge new echo entries without overwriting existing verse keys.
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

ECHOES = {
  "14": {
    "16": [
      {"type": "fulfillment", "target": "Isa 25:6", "note": "On this mountain the LORD Almighty will prepare a feast of rich food for all peoples — the Great Banquet parable enacts Isaiah's eschatological feast on Zion. The host's invitation to 'all peoples' that the invited guests reject (vv.18-20) fulfills the Isaianic pattern: the feast prepared for Israel is opened to outsiders (vv.21-23) when Israel refuses."}
    ]
  },
  "15": {
    "4": [
      {"type": "allusion", "target": "Ezek 34:11-12", "note": "I myself will search for my sheep and look after them. As a shepherd looks after his scattered flock when he is with them, so will I look after my sheep — the divine shepherd who searches for lost sheep (Ezek 34:11-12, 16) is the direct antecedent for the parable's searching shepherd. Jesus presents himself as YHWH fulfilling the Ezekiel promise to seek the lost personally."}
    ],
    "20": [
      {"type": "allusion", "target": "Isa 49:15", "note": "Can a mother forget the baby at her breast and have no compassion on the child she has borne? Though she may forget, I will not forget you — the divine compassion that surpasses even maternal love (Isa 49:15-16) is embodied in the father who runs to the returning son. The parable presents the running father as YHWH whose compassion exceeds every human comparison."}
    ]
  },
  "16": {
    "13": [
      {"type": "allusion", "target": "Josh 24:15", "note": "But if serving the LORD seems undesirable to you, then choose for yourselves this day whom you will serve — Joshua's covenant-renewal challenge at Shechem (choose this day whom you will serve) is the structural antecedent for 'no one can serve two masters.' The Deuteronomic framework of undivided loyalty to YHWH (Deut 6:4-5) underlies the saying; Joshua's binary (serve YHWH or the gods of the land) is the model that Jesus applies to wealth."},
      {"type": "allusion", "target": "1 Kgs 18:21", "note": "How long will you waver between two opinions? If the LORD is God, follow him; but if Baal is God, follow him — Elijah's challenge at Carmel is the prophetic form of the two-masters principle: divided loyalty to YHWH and Baal is incoherent. Jesus's saying applies the same binary to God and mammon, treating wealth-service as the functional equivalent of Baal-worship in the new covenant context."}
    ],
    "16": [
      {"type": "fulfillment", "target": "Mal 4:5-6", "note": "See, I will send the prophet Elijah before that great and dreadful day of the LORD comes — the Law and the Prophets proclaimed until John describes the era closed by Malachi's final word (the Elijah-promise that ends the OT canon). John's arrival is the fulfillment of Mal 4:5-6; the era of kingdom proclamation beginning with John is the era that Malachi's closing promise anticipated."},
      {"type": "allusion", "target": "Isa 61:1-2", "note": "The Spirit of the Sovereign LORD is on me, because the LORD has anointed me to proclaim good news to the poor — the 'good news of the kingdom of God being preached' since John (v.16) echoes the anointed herald of Isa 61:1-2 whom Jesus identified as himself (Luke 4:18-21). The preaching of the kingdom is the proclamation of the year of the LORD's favor."}
    ],
    "17": [
      {"type": "allusion", "target": "Ps 119:89", "note": "Your word, LORD, is eternal; it stands firm in the heavens — the permanence of God's word in Ps 119:89 is the OT ground for Jesus's statement that it is easier for heaven and earth to pass than for one stroke of the Law to drop out. The Torah's permanence is grounded in the divine character; Jesus is not abrogating the Law but affirming its absolute divine authority, which his own fulfillment of it honors and confirms."}
    ],
    "19": [
      {"type": "allusion", "target": "Amos 6:4-6", "note": "You lie on beds adorned with ivory and lounge on your couches. You dine on choice lambs and fattened calves... you drink wine by the bowlful and use the finest lotions, but you do not grieve over the ruin of Joseph — Amos's woe against the wealthy who feast while the poor suffer is the prophetic template for the rich man of Luke 16:19-31. The purple, fine linen, and daily luxury (v.19) describe precisely the Amos type; the neglect of Lazarus at his gate is the prophetic indictment enacted in narrative."}
    ],
    "22": [
      {"type": "allusion", "target": "Gen 25:8", "note": "Then Abraham breathed his last and died at a good old age, an old man and full of years; and he was gathered to his people — the phrase 'gathered to his people' / resting with the ancestors is the OT idiom for the blessed death of the righteous patriarch. 'Abraham's bosom/side' (v.22) is the narrative development of this patriarchal rest: the righteous dead share the place of the covenant father, as Abraham himself was gathered to his people."}
    ],
    "24": [
      {"type": "allusion", "target": "Isa 63:16", "note": "But you are our Father, though Abraham does not know us or Israel acknowledge us; you, LORD, are our Father, our Redeemer from of old is your name — Isaiah 63:16 notes that Abraham might not recognize his descendants in judgment, which makes the rich man's appeal 'Father Abraham' poignant and theologically ironic. The appeal to Abrahamic paternity (as also in John 8:39-44) does not guarantee participation in Abraham's blessing; faith and covenant faithfulness do."}
    ],
    "29": [
      {"type": "allusion", "target": "Deut 31:9-11", "note": "So Moses wrote down this law and gave it to the Levitical priests... Read this law before all Israel in their hearing — 'Moses and the Prophets' as the authoritative witness invokes the canonical shape of the OT: the Torah given through Moses (Deut 31:9) and the prophetic writings that followed it. The sufficiency of these witnesses for guiding the living to repentance is the claim; the rich man's request for a resurrection sign is the request for additional evidence the Scripture has already provided."}
    ],
    "31": [
      {"type": "allusion", "target": "Isa 26:19", "note": "But your dead will live, LORD; their bodies will rise — let those who dwell in the dust wake up and shout for joy — the prophetic promise of resurrection (Isa 26:19; Dan 12:2) is the OT backdrop for the parable's climax. 'Even if someone rises from the dead' anticipates Jesus's own resurrection and the Pharisees' rejection of it (Matt 28:11-15); the parable predicts that those who ignore Moses and the Prophets will not be convinced by the resurrection."},
      {"type": "allusion", "target": "Ezek 37:12-14", "note": "I am going to open your graves and bring you up from them; I will bring you back to the land of Israel — Ezekiel's valley of dry bones is the prophetic ground for resurrection hope. The parable's reference to 'someone rising from the dead' invokes this tradition. The rich man's implicit request for a resurrection-witness to persuade his brothers would have seemed to a Jewish audience like the fulfillment of Ezekiel's promise — but the parable predicts it will not suffice without prior covenant faithfulness."}
    ]
  }
}

def main():
    existing = load_echo('luke')
    merge_echo(existing, ECHOES)
    save_echo('luke', existing)
    ch14 = len(existing.get('14', {}))
    ch15 = len(existing.get('15', {}))
    ch16 = len(existing.get('16', {}))
    print(f'Luke echo: ch 14 = {ch14} verses, ch 15 = {ch15} verses, ch 16 = {ch16} verses.')

if __name__ == '__main__':
    main()
