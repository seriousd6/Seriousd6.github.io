"""
Echo layer — Matthew chapters 1–4
Output: data/echoes/matthew.json

Matthew is the most OT-dense Gospel, with explicit formula citations
(hina plerothe to rethen hypo... legontos = that it might be fulfilled which was spoken by...)
and dense allusions throughout. Key types: Moses/Exodus, David/kingdom, Isaiah's Servant.
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
  "1": {
    "1": [
      {"type": "allusion", "target": "Gen 5:1", "note": "Book of the genealogy (biblos geneseos) — same LXX phrase as Gen 5:1, the book of the generations of Adam; Matthew presents Jesus as the new Adam"},
      {"type": "fulfillment", "target": "2 Sam 7:12-16", "note": "Son of David — the Davidic covenant promise of an everlasting dynasty and throne; Matthew opens by naming Jesus as the fulfillment"},
      {"type": "fulfillment", "target": "Gen 22:18", "note": "Son of Abraham — in your offspring shall all the nations be blessed; Jesus as the seed in whom the Abrahamic blessing reaches all peoples"}
    ],
    "2": [
      {"type": "allusion", "target": "Gen 12:1-3", "note": "Abraham begot Isaac — the covenant line from Abraham through which the nations are to be blessed; the genealogy traces this promise-line"},
      {"type": "allusion", "target": "Ruth 4:18-22", "note": "The Boaz-through-Obed line to David — Ruth 4 ends with this same genealogical chain, linking Gentile Ruth into the Messianic line"}
    ],
    "5": [
      {"type": "shadow", "target": "Josh 2:1-21", "note": "Rahab the Gentile prostitute included in the messianic genealogy — the scarlet cord typology; Gentile inclusion and grace to the disqualified"},
      {"type": "shadow", "target": "Ruth 1:4", "note": "Ruth the Moabite in the messianic line — explicit inclusion of Gentile women as carriers of the Davidic promise"}
    ],
    "6": [
      {"type": "allusion", "target": "2 Sam 11:1-12:25", "note": "Uriah's wife (Bathsheba) — Matthew names her by her husband (the wronged man) rather than her name, embedding the scandal and grace into the genealogy"}
    ],
    "17": [
      {"type": "type", "target": "1 Kgs 6:1", "note": "The 3x14 structure (Abraham to David, David to exile, exile to Christ) — 14 = 2x7 (two weeks), and David in Hebrew numerology = 4+6+4 = 14; the genealogy is a theological pattern, not merely a biological register"}
    ],
    "21": [
      {"type": "allusion", "target": "Ps 130:8", "note": "He will save his people from their sins — YHWH will redeem Israel from all their iniquities; the Psalmic redemption-from-sin now accomplished by the one named Jesus (YHWH saves)"}
    ],
    "22": [
      {"type": "fulfillment", "target": "Isa 7:14", "note": "Behold the virgin shall conceive and bear a son, and they shall call his name Immanuel — Matthew cites this as fulfilled in the virgin birth of Jesus; God-with-us as the defining signature of Christ's person"}
    ],
    "23": [
      {"type": "fulfillment", "target": "Isa 7:14", "note": "Immanuel (God with us) — the name-theology: Matthew's Gospel is bracketed by Immanuel (1:23) and the promise of Christ's continuing presence (28:20)"}
    ]
  },
  "2": {
    "1": [
      {"type": "allusion", "target": "Num 24:17", "note": "Magi following the star from the East — Balaam's prophecy (a star shall come out of Jacob, a scepter shall rise out of Israel) as the background for the star-following Gentiles"}
    ],
    "2": [
      {"type": "fulfillment", "target": "Num 24:17", "note": "We saw his star — the star of Jacob-prophecy now appearing as the birth-sign of the King of the Jews; Gentile wise men recognizing what Israel's king refuses to see"}
    ],
    "6": [
      {"type": "fulfillment", "target": "Mic 5:2", "note": "And you, Bethlehem, in the land of Judah, are by no means least — Micah's Bethlehem prophecy cited by the chief priests as the birthplace of the Messiah; fulfilled in Jesus's birth location"}
    ],
    "11": [
      {"type": "allusion", "target": "Ps 72:10-11", "note": "The kings of Sheba and Seba bring gifts and bow down — the Solomonic Psalm of universal homage to the king fulfilled in type in the Magi's worship and gifts to the newborn King"}
    ],
    "13": [
      {"type": "type", "target": "Gen 46:1-7", "note": "Joseph led to Egypt — Matthew's Joseph echoes patriarch Joseph; both Josephs go to Egypt through divine revelation, both preserve the covenant line from death"}
    ],
    "14": [
      {"type": "fulfillment", "target": "Hos 11:1", "note": "Out of Egypt I called my son — Hosea's retrospective on the Exodus is applied to Jesus's return from Egypt; Jesus as the true Israel reliving and fulfilling the Exodus pattern"}
    ],
    "15": [
      {"type": "fulfillment", "target": "Hos 11:1", "note": "That it might be fulfilled: Out of Egypt I called my son — Matthew's formula citation; Israel is the typological son, Jesus is the antitypical Son whose exodus fulfills and surpasses Israel's"}
    ],
    "18": [
      {"type": "fulfillment", "target": "Jer 31:15", "note": "Rachel weeping for her children — Jeremiah's lament over the Babylonian exile deaths is applied to Herod's massacre; Matthew hears the voice of Rachel at Bethlehem as the slaughter of the innocents"}
    ],
    "23": [
      {"type": "fulfillment", "target": "Isa 11:1", "note": "He shall be called a Nazarene — possibly Netzer (branch/shoot from the stump of Jesse in Isa 11:1), or Nazir (consecrated one in Judg 13:5 Samson); Matthew hears a composite fulfillment in the place-name"}
    ]
  },
  "3": {
    "3": [
      {"type": "fulfillment", "target": "Isa 40:3", "note": "The voice of one crying in the wilderness: Prepare the way of the LORD — Isaiah's comfort passage (the new Exodus return from Babylon) now applied to John the Baptist; the return of the LORD to Zion takes the form of Jesus coming to his people"}
    ],
    "9": [
      {"type": "allusion", "target": "Ezek 36:26-27", "note": "God can raise up children to Abraham from these stones — the covenant promise of new hearts is behind John's warning; physical descent from Abraham cannot substitute for the Spirit-given transformation that constitutes true Abraham-children"}
    ],
    "11": [
      {"type": "shadow", "target": "Isa 44:3", "note": "I will baptize you with the Holy Spirit and fire — the Spirit poured out on thirsty ground (Isa 44:3) and the refining fire (Isa 4:4, Mal 3:2-3) converge in John's announcement of the Coming One's twofold baptism"}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 41:15-16", "note": "The winnowing fork / burning the chaff — the threshing-floor imagery of divine judgment: YHWH winnowing the nations; applied to the Coming One's eschatological discrimination between wheat and chaff"}
    ],
    "16": [
      {"type": "allusion", "target": "Gen 1:2", "note": "The Spirit of God descending as a dove — the Spirit hovering (merahephet) over the waters at creation; the baptism is the inauguration of new creation with the same Spirit-presence"},
      {"type": "fulfillment", "target": "Isa 42:1", "note": "Behold my servant whom I uphold, my chosen in whom my soul delights — the Servant Song; the voice from heaven at baptism echoes the Servant investiture; Jesus is installed as the Isaianic Servant of YHWH"}
    ],
    "17": [
      {"type": "fulfillment", "target": "Ps 2:7", "note": "This is my beloved Son with whom I am well pleased — the royal sonship of Ps 2:7 (You are my Son, today I have begotten you) combined with the servant-election of Isa 42:1; king and servant in one declaration"},
      {"type": "fulfillment", "target": "Isa 42:1", "note": "My beloved / in whom I am well pleased — the Servant Song election formula; Jesus is publicly designated as the chosen Servant at the Jordan, inaugurating his mission of justice to the nations"}
    ]
  },
  "4": {
    "4": [
      {"type": "quote", "target": "Deut 8:3", "note": "Man shall not live by bread alone but by every word that comes from the mouth of God — Jesus quotes Moses to defeat the temptation; where Israel failed in the wilderness (grumbling for bread), Jesus succeeds by trusting the Father's provision"}
    ],
    "6": [
      {"type": "quote", "target": "Ps 91:11-12", "note": "He will command his angels concerning you — Satan quotes Ps 91 (the protection-psalm) to tempt Jesus to test God; the irony is that the psalm describes trust in God, which testing God would violate"}
    ],
    "7": [
      {"type": "quote", "target": "Deut 6:16", "note": "You shall not put the Lord your God to the test — Jesus quotes Moses again, as Israel was warned not to test YHWH at Massah; the second Adam passes the test the first Adam (and Israel) failed"}
    ],
    "10": [
      {"type": "quote", "target": "Deut 6:13", "note": "You shall worship the Lord your God and him only shall you serve — the Shema-adjacent command that makes exclusive worship of YHWH the covenant foundation; Jesus applies it to reject the devil's offer of all the kingdoms"}
    ],
    "14": [
      {"type": "fulfillment", "target": "Isa 9:1-2", "note": "That it might be fulfilled which was spoken by the prophet Isaiah — Matthew cites Isa 9:1-2 as the explanation for Jesus beginning his ministry in Galilee of the Gentiles; the land of darkness sees the great light"}
    ],
    "15": [
      {"type": "fulfillment", "target": "Isa 9:1", "note": "The land of Zebulun and the land of Naphtali, the way of the sea, beyond the Jordan, Galilee of the Gentiles — Isa 9:1 names the very territories that Jesus first lights up with his ministry; geographic fulfillment"}
    ],
    "16": [
      {"type": "fulfillment", "target": "Isa 9:2", "note": "The people dwelling in darkness have seen a great light — the Isaianic promise of light to the northern territories (humiliated by Assyrian invasion) fulfilled as Jesus begins his Galilean proclamation of the kingdom"}
    ],
    "17": [
      {"type": "allusion", "target": "Dan 2:44", "note": "Repent, for the kingdom of heaven is at hand — the Danielic stone-kingdom that will shatter all earthly kingdoms is now proclaimed as near; the kingdom-arrival that Daniel saw is Jesus's opening proclamation"}
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
