"""
echo | leviticus | ch 24-25
Key connections: showbread → Jesus as bread of life (John 6:35); David's showbread
cited by Jesus (Matt 12:4); blasphemy law (24:16) → irony of Jesus's condemnation
(Matt 26:65); lex talionis (24:20) → superseded in Matt 5:38; Jubilee (25:10) →
Luke 4:18-19 (Jesus's Nazareth proclamation, his explicit mission statement);
go'el/kinsman-redeemer (25:25) → Christ as redeemer (Gal 4:4-5).
Run: python3 scripts/zc-echo-leviticus-24-25.py
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

LEVITICUS_ECHOES = {
  "24": {
    "5": [
      {"type": "typology", "target": "John 6:35",
       "note": "The twelve loaves of showbread (*lechem hapanim*, bread of presence) set before YHWH on the pure gold table every Sabbath — twelve loaves for twelve tribes, perpetually in YHWH's presence; Jesus declares himself the bread of life (John 6:35), the true bread of presence who feeds not twelve tribes but the whole world; the feeding of the 5,000 (John 6:1-14) deliberately echoes this by producing abundant bread in the presence of God"}
    ],
    "8": [
      {"type": "allusion", "target": "Matt 12:4",
       "note": "Aaron arranges the showbread before YHWH every Sabbath — a covenant obligation; Jesus cites David's eating of the showbread (1 Sam 21:6) to justify his disciples' grain-plucking on the Sabbath (Matt 12:4), using the showbread's only other narrative appearance; Jesus's point is that mercy and human need have always had priority over the letter of the bread-of-presence rules, even in David's day"}
    ],
    "16": [
      {"type": "typology", "target": "Matt 26:65",
       "note": "Whoever blasphemes the name of YHWH shall be put to death — this is the law under which the Sanhedrin condemns Jesus: when he says you will see the Son of Man seated at the right hand of Power (Matt 26:64), the high priest tears his robes and declares He has blasphemed (Matt 26:65), invoking Lev 24:16; the supreme irony is that the one who is the divine Name incarnate is executed under the law protecting that Name"}
    ],
    "20": [
      {"type": "fulfillment", "target": "Matt 5:38",
       "note": "Fracture for fracture, eye for eye, tooth for tooth — the lex talionis establishes proportional justice; Jesus explicitly cites this law in the Sermon on the Mount (Matt 5:38) and supersedes it with non-retaliation (v. 39), not because the law was wrong but because the kingdom operates by absorbing wrong rather than matching it — the cross is the ultimate expression of this: God absorbs the full penalty rather than imposing it"}
    ]
  },
  "25": {
    "10": [
      {"type": "fulfillment", "target": "Luke 4:18",
       "note": "Proclaim freedom throughout the land to all its inhabitants — the Jubilee proclamation is the direct OT source for Jesus's Nazareth synagogue reading of Isa 61:1-2: the Spirit of the Lord is on me to proclaim the year of the Lord's favor (Luke 4:18-19); by saying Today this Scripture is fulfilled in your hearing (Luke 4:21) Jesus announces that his ministry is the eschatological Jubilee — liberation from debt, slavery, and alienation not by the 50-year calendar but by his own person"},
      {"type": "allusion", "target": "Gal 5:1",
       "note": "It shall be a year of release for you — the Jubilee releases slaves, restores land, cancels debts, and restores family relationships; Paul's declaration for freedom Christ has set us free; stand firm therefore and do not submit again to a yoke of slavery (Gal 5:1) applies the Jubilee principle to the new covenant: Christ's redemption is the permanent Jubilee, freeing those enslaved under the law"}
    ],
    "25": [
      {"type": "typology", "target": "Gal 4:5",
       "note": "If your brother becomes poor and sells his property, his nearest redeemer (*go'el*) shall come and redeem what his brother has sold — the *go'el* (kinsman-redeemer) is the relative who steps in to buy back land or persons fallen into poverty; this institution underlies Paul's redemption language in Gal 4:4-5: God sent his Son, born under the law, to redeem those who were under the law; Christ is the divine kinsman who becomes human (the necessary kinship) in order to exercise the *go'el* right and buy back those enslaved to debt and law"}
    ],
    "42": [
      {"type": "allusion", "target": "Rom 8:15",
       "note": "They are my servants whom I brought out of Egypt; they shall not be sold as slaves — YHWH's ownership of Israel (purchased by the Exodus) grounds the prohibition against re-enslavement; Paul applies the same logic to believers: you did not receive the spirit of slavery to fall back into fear, but you have received the spirit of adoption (Rom 8:15); those whom God has redeemed by the greater Exodus cannot be sold back into slavery"}
    ]
  }
}

def main():
    e = load_echo('leviticus')
    merge_echo(e, LEVITICUS_ECHOES)
    save_echo('leviticus', e)

if __name__ == '__main__':
    main()
