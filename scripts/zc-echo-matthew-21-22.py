"""
Echo layer — Matthew chapters 21–22 (Triumphal entry through debates)
Output: data/echoes/matthew.json (adds ch21-22)

Ch21: Triumphal entry (Zech 9:9), temple cleansing (Isa 56, Jer 7), fig tree,
      Parable of the two sons, parable of the tenants (Ps 118, Isa 5).
Ch22: Parable of the wedding banquet; debates (taxes, resurrection, great commandment, David's son).
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
  "21": {
    "5": [
      {"type": "fulfillment", "target": "Zech 9:9", "note": "Behold, your king is coming to you, humble and mounted on a donkey — Matthew cites Zech 9:9 as fulfilled in the triumphal entry; the meek king riding on a donkey (not a war horse) is the Zecharian profile of the messianic king"},
      {"type": "allusion", "target": "Isa 62:11", "note": "Say to the daughter of Zion — the announcement to Zion that salvation is coming; Matthew combines Zech 9:9 with this Isaianic announcement"}
    ],
    "9": [
      {"type": "fulfillment", "target": "Ps 118:25-26", "note": "Hosanna to the Son of David! Blessed is he who comes in the name of the LORD! — the pilgrim-processional Psalm cited as the crowd's cry; hosanna (save now) + blessed is he who comes = messianic entry into Jerusalem"}
    ],
    "13": [
      {"type": "fulfillment", "target": "Isa 56:7", "note": "My house shall be called a house of prayer — the Isaianic vision of the temple as a house of prayer for all nations; Jesus cites it as the standard the money-changers have violated"},
      {"type": "quote", "target": "Jer 7:11", "note": "But you have made it a den of robbers — Jeremiah's temple sermon (the temple as a false security while robbery continues); Jesus combines Isa 56 with Jer 7 to interpret the temple's corruption"}
    ],
    "16": [
      {"type": "fulfillment", "target": "Ps 8:2", "note": "From the mouths of infants and nursing babies you have prepared praise — Jesus cites Ps 8:2 against the chief priests who are indignant at the children's Hosannas. In context Ps 8 speaks of YHWH's majestic name being acclaimed even by the weakest voices, silencing the enemy and the avenger; the children's perception of Jesus contrasts with the leaders' deliberate blindness."}
    ],
    "19": [
      {"type": "allusion", "target": "Jer 8:13", "note": "There will be no figs on the tree and its leaves will wither — Jeremiah's oracle of judgment uses a barren fig tree as the image of Israel under divine judgment. The cursed fig tree with leaves but no fruit enacts this symbol: the temple establishment has the form of fruitfulness but produces nothing."},
      {"type": "allusion", "target": "Mic 7:1", "note": "There is no cluster of grapes to eat, none of the early figs that I crave — Micah's lament for Israel uses fig-hunger as a metaphor for the failure of the covenant community to produce the righteous fruit God sought. Jesus's curse of the barren fig tree acts out this prophetic verdict."}
    ],
    "33": [
      {"type": "fulfillment", "target": "Isa 5:1-7", "note": "A man planted a vineyard, put a fence around it, dug a winepress — the Parable of the Tenants is built directly on Isaiah's Song of the Vineyard (Isa 5:1-7); Israel as the vineyard, the tenants as the leaders"}
    ],
    "38": [
      {"type": "allusion", "target": "Gen 37:20", "note": "Come, let us kill him and seize his inheritance — the tenants articulate verbally what Joseph's brothers said about Joseph: come, let us kill the heir. The pattern of the rejected son who is killed but whose story ends in vindication and the salvation of his brothers is embedded in the parable's logic."}
    ],
    "42": [
      {"type": "fulfillment", "target": "Ps 118:22-23", "note": "The stone that the builders rejected has become the cornerstone — Jesus cites Ps 118:22 as fulfilled in his own rejection and vindication; the rejected stone becoming the cornerstone = the crucifixion and resurrection"}
    ],
    "44": [
      {"type": "allusion", "target": "Dan 2:34-35", "note": "The stone cut without hands that struck the statue and became a great mountain filling the earth — Jesus's warning that the one who falls on this stone will be broken, and the one on whom it falls will be crushed, draws on Daniel's image of the divine stone as an unstoppable judgment force that destroys all earthly kingdoms."}
    ]
  },
  "22": {
    "2": [
      {"type": "allusion", "target": "Isa 25:6", "note": "On this mountain the LORD of hosts will make for all peoples a feast of rich food — Isaiah's eschatological banquet where YHWH destroys death and wipes away tears; the parable of the wedding banquet enacts this promised celebration, centered on the king's son."}
    ],
    "4": [
      {"type": "allusion", "target": "Isa 25:6", "note": "The Parable of the Wedding Banquet: the king prepared a banquet — on this mountain the LORD of hosts will make for all peoples a feast of rich food; the eschatological banquet of Isaiah fulfilled in the kingdom-banquet Jesus announces"}
    ],
    "11": [
      {"type": "allusion", "target": "Isa 61:10", "note": "He has clothed me with garments of salvation — the wedding garment as the clothing of God's righteousness; the guest without a garment represents one who attends the feast on their own terms rather than clothed in the righteousness the king provides. Isaiah's imagery of garments of salvation at the eschatological banquet underlies the parable's final image."}
    ],
    "13": [
      {"type": "allusion", "target": "Dan 12:2", "note": "Bind him and cast him into the outer darkness — everlasting contempt for those who do not awaken to life; the outer darkness of the parable echoes the Danielic judgment on those excluded from resurrection-life"}
    ],
    "21": [
      {"type": "allusion", "target": "Gen 1:26-27", "note": "Render to Caesar the things that are Caesar's, and to God the things that are God's — the denarius bears Caesar's image (eikon); humans bear God's image (Gen 1:26-27). Jesus's answer turns on the image question: what bears Caesar's image belongs to Caesar; what bears God's image (human beings) belongs to God."}
    ],
    "24": [
      {"type": "quote", "target": "Deut 25:5", "note": "If brothers are living together and one of them dies without a son, his widow must not marry outside the family — the Sadducees cite the levirate marriage law directly; their reductio ad absurdum is designed to make resurrection theologically absurd by piling up a legal scenario that becomes unsolvable if resurrection is true."}
    ],
    "32": [
      {"type": "quote", "target": "Exod 3:6", "note": "I am the God of Abraham, the God of Isaac, and the God of Jacob — the burning bush self-identification; Jesus argues for resurrection from the present-tense I AM (not I was): God is the God of the living, not the dead"}
    ],
    "37": [
      {"type": "quote", "target": "Deut 6:5", "note": "You shall love the LORD your God with all your heart and with all your soul and with all your mind — the Shema command; Jesus identifies this as the great and first commandment"},
      {"type": "allusion", "target": "Deut 6:4", "note": "Hear O Israel: The Lord our God, the Lord is one — the Shema declaration that precedes the love command; loving God with all heart/soul/strength flows from and rests on God's oneness. Jesus's citation of the love command implicitly invokes the monotheistic foundation of Israel's covenant identity."}
    ],
    "39": [
      {"type": "quote", "target": "Lev 19:18", "note": "You shall love your neighbor as yourself — the second great commandment from the Holiness Code; Jesus pairs Deut 6:5 with Lev 19:18 as the double-love summary of all Torah and the Prophets"}
    ],
    "44": [
      {"type": "quote", "target": "Ps 110:1", "note": "The LORD said to my Lord: Sit at my right hand until I put your enemies under your feet — David in the Spirit calls his son Lord; Jesus cites Ps 110:1 to show that the Messiah is more than David's descendant, being David's Lord"},
      {"type": "allusion", "target": "Ps 110:4", "note": "You are a priest forever after the order of Melchizedek — Ps 110 unites royal enthronement at the right hand with the eternal priesthood of Melchizedek; Matthew's citation opens the royal dimension; the priestly dimension (foundational to Hebrews' Christology) is also present in the psalm Jesus quotes."}
    ]
  }
}

def main():
    existing = load_echo('matthew')
    merge_echo(existing, ECHOES)
    save_echo('matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
