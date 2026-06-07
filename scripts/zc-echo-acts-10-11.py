"""
MKT Echo Layer — Acts chapters 10–11
Output: data/echoes/acts.json
Run: python3 scripts/zc-echo-acts-10-11.py

Key decisions:
- Acts 10–11 is the watershed Gentile-inclusion episode, saturated with OT echoes:
  Cornelius's piety echoes righteous Gentiles in the OT (Rahab, Ruth, Naaman);
  Peter's vision overturns Leviticus 11's clean/unclean taxonomy as a type fulfilled;
  the Spirit on Cornelius's household echoes Joel 2 and Num 11:29;
  Peter's sermon cites Isa 61, Deut 10:17, Ps 107 implicitly, Dan 7/12;
  Agabus's famine prophecy echoes Elisha/Elijah in 1 Kgs 17, 2 Kgs 4, 8.
- Echo entries anchor to the verse where the echo is most concentrated;
  multi-verse scenes use the initiating verse.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echoes(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echoes(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echoes(existing, new_data):
    # INTENT: Add new chapter/verse echo entries without overwriting existing ones — safe to re-run.
    # CHANGE? If echo JSON structure changes from {ch:{v:[entries]}}, update this traversal.
    # VERIFY: Re-running should produce identical verse counts (no duplicated entries).
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries

ACTS_ECHOES = {
"10": {
    "1": [
        {
            "type": "typology",
            "target": "Josh 2:1",
            "note": "Cornelius, a Gentile soldier who fears God and gives alms, stands in the line of OT righteous Gentiles — Rahab who sheltered the spies (Josh 2), Ruth who cleaved to Israel's God (Ruth 1:16), Naaman who came to be healed (2 Kgs 5). In each case, YHWH's purposes break through Israel's ethnic boundaries through a Gentile who seeks the God of Israel."
        }
    ],
    "2": [
        {
            "type": "allusion",
            "target": "Ps 41:1",
            "note": "'Blessed is the one who considers the poor' — Cornelius's almsgiving and constant prayer is the portrait of the Psalter's righteous man (Ps 41:1; 112:9 — 'he has distributed freely; he has given to the poor'). His piety is evaluated in OT terms: the fear of God, prayer, and care for the poor are the marks of the covenant-faithful that the Psalter celebrates."
        }
    ],
    "3": [
        {
            "type": "typology",
            "target": "Dan 10:5-7",
            "note": "The angel appearing 'clearly' in a vision during prayer at the ninth hour echoes the angel-appearance to Daniel during his three-week fast — the divine messenger comes to those whose prayer and fasting marks them as seekers. The ninth hour (3 pm) is the hour of the evening sacrifice in the temple: prayer aligned with the temple times receives the temple's heavenly counterpart."
        }
    ],
    "9": [
        {
            "type": "allusion",
            "target": "Gen 28:12",
            "note": "Peter's rooftop vision of heaven opened and a sheet descending echoes the opening of heaven in biblical vision narratives — most directly Ezekiel 1:1 ('the heavens were opened, and I saw visions of God') and Genesis 28:12 (the ladder between heaven and earth). The opened heaven is the condition of prophetic revelation throughout the OT; now it opens over a rooftop in Joppa."
        }
    ],
    "11": [
        {
            "type": "typology",
            "target": "Gen 1:24-25",
            "note": "The great sheet containing 'all kinds of animals and reptiles and birds of the air' — the four-footed animals, reptiles, and birds — recapitulates the taxonomy of Genesis 1:24-25 (cattle, creeping things, beasts of the earth, birds). The vision recollects creation's categories precisely in order to announce their recategorization: what the Creator made is declared clean by the Creator's word."
        }
    ],
    "13": [
        {
            "type": "fulfillment",
            "target": "Lev 11:1-47",
            "note": "'Rise, Peter; kill and eat' — the command to eat what Leviticus 11 had declared unclean is the fulfillment-dissolution of the clean/unclean food law as a type. The dietary laws functioned as a boundary-marker separating Israel from the nations (Lev 20:25-26: 'I have separated you from the peoples... you shall not make yourselves detestable by beast or bird'). The law's purpose is now fulfilled in Christ; the boundary is taken down as the Gentile mission opens."
        }
    ],
    "15": [
        {
            "type": "fulfillment",
            "target": "Isa 65:25",
            "note": "'What God has made clean, do not call common' — the divine reversal of the clean/unclean taxonomy fulfills the new-creation vision of Isaiah where former distinctions and enmities are overcome: 'The wolf and the lamb shall graze together; the lion shall eat straw like the ox' (Isa 65:25). The new creation does not maintain the distinctions necessary in the old creation's condition of enmity and sin."
        }
    ],
    "28": [
        {
            "type": "allusion",
            "target": "Deut 7:3",
            "note": "Peter's explanation that 'it is unlawful for a Jew to associate with or to visit anyone of another nation' references the Mosaic separation-commands (Deut 7:3 — 'you shall not intermarry with them'; Ezra 9–10 — the crisis of mixed marriages). The rooftop vision has shown Peter that the old purity-boundary between Jew and Gentile is being redrawn — the social law follows from the food-law's dissolution."
        }
    ],
    "34": [
        {
            "type": "fulfillment",
            "target": "Deut 10:17",
            "note": "'God shows no partiality' (prosōpolēmptēs ouk estin ho theos) directly quotes the LXX of Deuteronomy 10:17 — 'the LORD your God is God of gods and Lord of lords... who is not partial and takes no bribe.' The impartiality-of-God that Deuteronomy applied within Israel is now applied across nations: the same God who plays no favorites among Israelites plays no favorites between Israel and the Gentiles."
        }
    ],
    "36": [
        {
            "type": "fulfillment",
            "target": "Isa 52:7",
            "note": "'Preaching good news of peace through Jesus Christ' (euangelizomenos eirēnēn dia Iēsou Christou) translates Isaiah 52:7 — 'how beautiful are the feet of him who brings good news, who publishes peace.' The Isaiah herald's message of peace was always intended for 'all the peoples' (Isa 52:10 — 'all the ends of the earth shall see the salvation of our God'). Peter's sermon to Cornelius is the fulfillment of the herald's message reaching its intended scope."
        }
    ],
    "38": [
        {
            "type": "fulfillment",
            "target": "Isa 61:1",
            "note": "'God anointed Jesus of Nazareth with the Holy Spirit and with power' is Peter's prose summary of what Jesus himself announced at Nazareth (Luke 4:18) as the fulfillment of Isaiah 61:1 — 'The Spirit of the Lord GOD is upon me, because the LORD has anointed me to bring good news to the poor.' The anointing is the Spirit-baptism at the Jordan (Luke 3:22); the power is the healing and exorcism ministry that followed."
        }
    ],
    "42": [
        {
            "type": "allusion",
            "target": "Dan 7:13-14",
            "note": "'He is the one appointed by God to be judge of the living and the dead' echoes Daniel 7:13-14, where the Son of Man is given dominion over 'all peoples, nations, and languages' — universal authority that includes authority to judge. The 'living and the dead' extends the judgment's scope: the risen one who has conquered death judges both those who still live and those who have died."
        }
    ],
    "43": [
        {
            "type": "fulfillment",
            "target": "Isa 33:24",
            "note": "'Everyone who believes in him receives forgiveness of sins through his name' — the universal scope of forgiveness through the name of Jesus fulfills the new-creation forgiveness promises: Isaiah 33:24 ('the inhabitant will not say, I am sick; the people who dwell there will be forgiven their iniquity'), Jeremiah 31:34 ('I will forgive their iniquity, and I will remember their sin no more'), and Micah 7:18 ('who is a God like you, pardoning iniquity')."
        }
    ],
    "44": [
        {
            "type": "fulfillment",
            "target": "Joel 2:28-29",
            "note": "The Holy Spirit falling on the Gentile household 'while Peter was still speaking' is the second Pentecost — the Joel 2:28-29 fulfillment extending beyond Jews to Gentiles: 'I will pour out my Spirit on all flesh... even on the male and female servants in those days I will pour out my Spirit.' The 'all flesh' of Joel's promise is demonstrably all-ethnic, not merely all-Israelite."
        }
    ],
    "46": [
        {
            "type": "allusion",
            "target": "Num 11:29",
            "note": "The circumcised believers' astonishment that the Spirit was poured out on Gentiles recalls Moses's wish at Kibroth-hattaavah: 'Would that all the LORD's people were prophets, that the LORD would put his Spirit on them!' (Num 11:29). What Moses wished for Israel, the Spirit accomplishes for all nations. The gift of Spirit-tongues at Cornelius's house is the answer to Moses's prayer, expanded beyond Israel's borders."
        }
    ]
},
"11": {
    "5": [
        {
            "type": "typology",
            "target": "Gen 28:12",
            "note": "Peter's retelling of the sheet-vision in his own words uses identical imagery to his original account. The opened heaven and the descending object echoes the vision-convention of the prophets (Ezek 1:1; Isa 6:1; Dan 7:9) — heaven opened is the precondition of prophetic revelation. Peter's defense is structured as a prophetic testimony: he has seen what prophets see and now reports it."
        }
    ],
    "12": [
        {
            "type": "allusion",
            "target": "Deut 19:15",
            "note": "'These six brothers also accompanied me' — Peter explicitly counts his Gentile witnesses (six, plus Peter = seven, matching the legal minimum for testimony). The Deuteronomic witness-standard (Deut 19:15 — 'a matter shall be established by the evidence of two or three witnesses') is exceeded: seven witnesses from the Joppa community confirm what happened at Cornelius's house."
        }
    ],
    "16": [
        {
            "type": "fulfillment",
            "target": "Isa 44:3",
            "note": "Peter's recollection of Jesus's promise — 'John baptized with water, but you will be baptized with the Holy Spirit' — and its fulfillment on the Gentiles echoes Isaiah's water/Spirit promise: 'I will pour water on the thirsty land and streams on the dry ground; I will pour my Spirit upon your offspring and my blessing on your descendants' (Isa 44:3). The Spirit-as-water poured out is the refreshing of the dry ground of Gentile spiritual aridity."
        }
    ],
    "17": [
        {
            "type": "allusion",
            "target": "Num 11:25-29",
            "note": "'If God gave the same gift to them as he gave to us when we believed in the Lord Jesus Christ, who was I that I could stand in God's way?' echoes Moses's response to the elders prophesying in the camp: he refused to stop them and wished all the LORD's people were prophets (Num 11:25-29). Peter, like Moses, refuses to obstruct what the Spirit is doing beyond the expected boundaries."
        }
    ],
    "18": [
        {
            "type": "fulfillment",
            "target": "Isa 49:6",
            "note": "'Then to the Gentiles also God has granted repentance that leads to life' — the Jerusalem church's astonished praise recognizes the fulfillment of Isaiah's Servant-mission: 'I will make you a light for the nations, that my salvation may reach to the end of the earth.' The 'end of the earth' begins in Caesarea with a Roman centurion's household receiving repentance and life."
        }
    ],
    "19": [
        {
            "type": "allusion",
            "target": "Isa 66:19",
            "note": "Scattered believers preaching in Phoenicia, Cyprus, and Antioch after Stephen's martyrdom echoes Isaiah's vision of survivors sent 'to the nations, to Tarshish, Pul, and Lud... to the coastlands far away, that have not heard my fame or seen my glory' (Isa 66:19). The persecution-scattering that appears to be defeat is the mechanism of Isaiah's Gentile-proclamation — the survivors become the heralds."
        }
    ],
    "20": [
        {
            "type": "fulfillment",
            "target": "Isa 66:18",
            "note": "'Some of them... spoke to the Hellenists also, preaching the Lord Jesus' — the first deliberate preaching to Gentiles (Hellenists) fulfills Isaiah's vision that God will 'come to gather all nations and tongues, and they shall come and shall see my glory' (Isa 66:18). The gathering begins not by bringing Gentiles to Jerusalem but by bringing the word of Jerusalem's risen Lord to Gentiles."
        }
    ],
    "23": [
        {
            "type": "typology",
            "target": "1 Kgs 12:20",
            "note": "Barnabas sent from Jerusalem to Antioch as the church's representative echoes the pattern of Jerusalem sending authorized agents to new communities of faith — similar to the pattern of the Jerusalem council's delegates (Acts 15:22-29) and the Sanhedrin's agents (Acts 9:2). The center-to-periphery sending is the structural pattern of how the covenant community responds to Spirit-outbreaks at the boundaries."
        }
    ],
    "26": [
        {
            "type": "allusion",
            "target": "Isa 62:2",
            "note": "'In Antioch the disciples were first called Christians' — the giving of a new name to the community of the new covenant echoes Isaiah's promise: 'the nations shall see your righteousness... and you shall be called by a new name that the mouth of the LORD will give' (Isa 62:2). The new name 'Christian' is the name of those who belong to the Anointed One (Christos) — the messianic community identified by its Lord's title."
        }
    ],
    "28": [
        {
            "type": "typology",
            "target": "1 Kgs 17:1",
            "note": "Agabus's Spirit-prophesied famine 'over all the world' echoes the great famine-prophecies of the OT prophets — most directly Elijah's announcement of famine to Ahab (1 Kgs 17:1 — 'there shall be neither dew nor rain these years, except by my word'). As in the OT, famine-prophecy is authenticated by the Spirit and is the occasion for covenant generosity to those in need."
        },
        {
            "type": "typology",
            "target": "Gen 41:29-30",
            "note": "The prophet who predicts a coming famine that will affect a wide region recalls Joseph's interpretation of Pharaoh's dream: seven years of plenty followed by seven years of famine 'throughout all the earth' (Gen 41:29-30). The prophetic forewarning enables preparation and relief — the same pattern that the Antioch believers follow by sending relief to Judea."
        }
    ],
    "29": [
        {
            "type": "fulfillment",
            "target": "Deut 15:11",
            "note": "'Each of the disciples determined to send relief, everyone according to his ability, to the brothers living in Judea' — the voluntary, ability-proportioned giving echoes and fulfills Deuteronomy 15:11: 'you shall open wide your hand to your brother, to the needy and to the poor.' The Antioch Gentile community's care for Jewish believers in Jerusalem is the enacted reversal of the Gentile-Israel barrier: former outsiders now care for insiders as covenant brothers."
        }
    ]
}
}

def main():
    existing = load_echoes('acts')
    merge_echoes(existing, ACTS_ECHOES)
    save_echoes('acts', existing)
    for ck in ['10', '11']:
        n = len(existing.get(ck, {}))
        print(f'Acts ch {ck}: {n} echo entries')

if __name__ == '__main__':
    main()
