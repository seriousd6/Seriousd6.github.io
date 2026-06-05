"""
Echo Commentary — Hebrews chapters 12–13
Run: python3 scripts/zc-echo-hebrews-12-13.py

Key decisions:
- 12:5-6 Prov 3:11-12 = quote (explicit citation)
- 12:12-13 Isa 35:3 = allusion (not explicit but verbal parallel)
- 12:16 Esau: Gen 25:29-34 = shadow (selling birthright); Gen 27 = consequence type
- 12:18-21 Sinai theophany: Exod 19-20 = type/shadow
- 12:22 heavenly Zion: Ps 48, Isa 24:23 = fulfillment
- 12:26 Hag 2:6 = fulfillment (explicit citation)
- 12:29 Deut 4:24 = quote
- 13:6 Ps 118:6 = quote; 13:15 Hos 14:2 = allusion; 13:20 Isa 63:11 = allusion
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

HEBREWS = {
  "12": {
    "1": [
      {"type": "theme", "target": "Isa 40:31", "note": "\"They shall run and not be weary; they shall walk and not faint\" — the endurance-race imagery for the community's pilgrimage participates in the Isaianic promise of renewed strength for those who wait on the LORD. The 'great cloud of witnesses' (11:4-38) who endured frames the running metaphor."},
      {"type": "allusion", "target": "Ps 22:4–5", "note": "\"In you our fathers trusted; they trusted, and you delivered them. To you they cried and were saved\" — the ancestral trust-and-deliverance pattern is the OT background for the cloud of witnesses whose faith-examples surround the community. The Psalter's appeal to ancestral faith motivates perseverance."}
    ],
    "2": [
      {"type": "fulfillment", "target": "Ps 110:1", "note": "\"Sit at my right hand\" — Hebrews 12:2 returns once more to Ps 110:1 as the destination of Jesus's endurance: 'who for the joy that was set before him endured the cross, despising the shame, and is seated at the right hand of the throne of God.' The right-hand session is the completed eschatological reality that the community looks toward as the race's destination."}
    ],
    "5": [
      {"type": "quote", "target": "Prov 3:11–12", "note": "\"My son, do not regard lightly the discipline of the Lord... For the Lord disciplines the one he loves, and chastises every son whom he receives\" — Hebrews 12:5-6 cites Prov 3:11-12 as the interpretive key for the community's present suffering. The father-son discipline relationship of Proverbs establishes that God's chastisement of the community is evidence of his fatherly love, not his rejection."}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 35:3", "note": "\"Strengthen the weak hands, and make firm the feeble knees. Say to those who have an anxious heart, 'Be strong; fear not! Behold, your God will come with vengeance'\" — Hebrews 12:12's 'strengthen your drooping hands and weak knees' is a verbal echo of Isa 35:3, applied to the community under discipline-suffering. The eschatological strengthening promised to the exiles in Isaiah's restoration oracle is now applied to the new-covenant community's endurance."}
    ],
    "13": [
      {"type": "allusion", "target": "Prov 4:26", "note": "\"Ponder the path of your feet; then all your ways will be sure\" — Hebrews 12:13's 'make straight paths for your feet, so that what is lame may not be put out of joint but rather be healed' echoes Prov 4:26 LXX (<em>orthas trochiας poiei tois posin sou</em> = make straight tracks for your feet). The wisdom tradition's counsel about the right path is applied to the community's moral-spiritual direction under discipline."}
    ],
    "15": [
      {"type": "allusion", "target": "Deut 29:18", "note": "\"Beware lest there be among you a man or woman or clan or tribe whose heart is turning away today from the LORD our God to go and serve the gods of those nations. Beware lest there be among you a root bearing poisonous and bitter fruit\" — the 'root of bitterness' (Heb 12:15) is a direct echo of Deut 29:18 LXX (<em>rhiza anō phyousa en cholē kai pikria</em>). The Mosaic warning against covenant apostasy is the OT background for the Hebrews community's warning."}
    ],
    "16": [
      {"type": "shadow", "target": "Gen 25:29–34", "note": "Esau selling his birthright for a single meal — who was 'sexually immoral or unholy like Esau, who sold his birthright for a single meal' — is the OT paradigm of the one who trades the eschatological inheritance for immediate earthly satisfaction. Hebrews 12:16 reads Esau as the negative paradigm of those who would fall from grace for short-term relief."},
      {"type": "shadow", "target": "Gen 27:30–40", "note": "Esau's failed attempt to repent after losing the blessing — 'he found no chance to repent, though he sought it with tears' — is the OT warning case for the irreversibility of apostasy. Esau's bitter tears could not recover what he had traded away; his post-blessing repentance is the type of the irreversibility that Hebrews 6:4-6 and 10:26-27 also warn against."}
    ],
    "18": [
      {"type": "shadow", "target": "Exod 19:10–24", "note": "The Sinai theophany — fire, darkness, gloom, tempest, trumpet blast, terrifying divine voice — is the OT type-event that Hebrews 12:18-21 contrasts with the new covenant assembly. The community that has come to Mount Zion stands in deliberate contrast to the Sinai assembly: the terror of the presence-without-mediation (which Israel could not bear) is contrasted with the joyful assembly in the heavenly Jerusalem."},
      {"type": "shadow", "target": "Deut 4:11–12", "note": "\"You came near and stood at the foot of the mountain, while the mountain burned with fire to the heart of heaven, wrapped in darkness, cloud, and gloom\" — Moses's description of Sinai in Deuteronomy provides Hebrews' quotation material for the terrifying mountain that could not be touched."}
    ],
    "20": [
      {"type": "quote", "target": "Exod 19:12–13", "note": "\"If even a beast touches the mountain, it shall be stoned\" — Hebrews 12:20 cites the Sinai access prohibition to underscore the unbearable holiness of the first covenant's theophany. Even Moses was terrified (12:21: 'I am terrified and trembling') — the Sinai revelation, for all its glory, was a terrifying encounter that the community could not approach."}
    ],
    "22": [
      {"type": "fulfillment", "target": "Ps 48:1–2", "note": "\"Great is the LORD and greatly to be praised in the city of our God! His holy mountain, beautiful in elevation... Mount Zion\" — the Psalter's celebration of Zion as the city of God and mountain of his assembly is the OT background for Hebrews' 'you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem.' The earthly Zion of the Psalms is the type; the heavenly Jerusalem is the eschatological reality."},
      {"type": "fulfillment", "target": "Isa 24:23", "note": "\"Then the moon will be confounded and the sun ashamed, for the LORD of hosts reigns on Mount Zion and in Jerusalem\" — the eschatological Mount Zion where God reigns over the nations is the OT vision that Hebrews' 'heavenly Jerusalem' inhabits. The new covenant community has already arrived at the eschatological destination."}
    ],
    "24": [
      {"type": "allusion", "target": "Gen 4:10", "note": "\"The voice of your brother's blood is crying to me from the ground\" — Hebrews 12:24 contrasts the blood of Jesus, which 'speaks a better word than the blood of Abel.' Abel's blood cried for vengeance; Jesus's blood speaks the better word of forgiveness and new-covenant access. The Abel-blood comparison places Jesus's cross in the entire OT trajectory from the first murder to the final atonement."}
    ],
    "26": [
      {"type": "fulfillment", "target": "Hag 2:6", "note": "\"Yet once more I will shake the heavens and the earth and the sea and the dry land\" — Hebrews 12:26 cites Hag 2:6 as the eschatological shaking that distinguishes the unshakeable kingdom from the shakeable creation. The once-more shaking that Haggai promises is interpreted by Hebrews as the apocalyptic removal of the created order, leaving only the eternal kingdom that cannot be shaken."}
    ],
    "29": [
      {"type": "quote", "target": "Deut 4:24", "note": "\"For the LORD your God is a consuming fire, a jealous God\" — Hebrews 12:29 closes the section with a direct citation of Deut 4:24, applying Moses's characterization of God as consuming fire to the new covenant community's context. The same God who terrified Israel at Sinai and Haggai's shaking-God is the one who now receives the unshakeable kingdom — the fire of divine holiness continues."}
    ]
  },
  "13": {
    "2": [
      {"type": "shadow", "target": "Gen 18:1–8", "note": "Abraham's hospitality to the three visitors at Mamre — who proved to be divine messengers — is the OT paradigm behind 'do not neglect to show hospitality to strangers, for thereby some have entertained angels unawares.' The patriarch's radical hospitality to unknown travelers rewarded by divine visit is the prototype of the hospitality that the new covenant community practices."},
      {"type": "shadow", "target": "Gen 19:1–3", "note": "Lot's hospitality to the two angels at Sodom's gate — welcome and protection in a hostile environment — is the second OT paradigm of entertaining divine messengers unawares that Heb 13:2 draws on."}
    ],
    "5": [
      {"type": "allusion", "target": "Deut 31:6", "note": "\"Be strong and courageous. Do not fear or be in dread of them, for it is the LORD your God who goes with you. He will not leave you or forsake you\" — the divine promise to Israel entering the land (and specifically to Joshua leading them) is the OT background for Hebrews' 'he has said, I will never leave you nor forsake you.' The exodus-community's assurance of divine presence is applied to the new covenant community under financial anxiety."}
    ],
    "6": [
      {"type": "quote", "target": "Ps 118:6", "note": "\"The LORD is on my side; I will not fear. What can man do to me?\" — Hebrews 13:6 cites Ps 118:6 LXX as the confident response to the divine 'I will never leave you.' The Hallel psalm's declaration of confidence in the face of human threat is the scriptural voice of the community's fearlessness."}
    ],
    "11": [
      {"type": "type", "target": "Lev 16:27", "note": "\"The bull for the sin offering and the goat for the sin offering, whose blood was brought in to make atonement in the Holy Place, shall be carried outside the camp and burned up\" — Hebrews 13:11 uses the burning-outside-the-camp requirement for the atonement-animals as the OT type for Jesus's suffering 'outside the gate' of Jerusalem. The discarded sacrifice placed outside the community's boundary is fulfilled in Jesus's crucifixion outside the city."}
    ],
    "12": [
      {"type": "fulfillment", "target": "Lev 16:27", "note": "\"So Jesus also suffered outside the gate in order to sanctify the people through his own blood\" — the explicit typological application: the atonement animals burned outside the camp = Jesus crucified outside Jerusalem's gate. The spatial-theological logic is the same: the sacrifice that cleanses is removed from the holy space to carry the impurity away."}
    ],
    "13": [
      {"type": "shadow", "target": "Num 12:15", "note": "\"Miriam was shut outside the camp seven days\" — the principle of going outside the camp as shame-bearing is the OT background for Hebrews 13:13's call to 'go to him outside the camp and bear the reproach he endured.' Joining the shamed, excluded one is the new covenant community's characteristic posture."}
    ],
    "14": [
      {"type": "allusion", "target": "Heb 11:10", "note": "\"For here we have no lasting city, but we seek the city that is to come\" — the cross-reference to the pilgrim-faith of Hebrews 11 (especially 11:10: 'he was looking forward to the city that has foundations, whose designer and builder is God') grounds the outside-the-gate posture: the community has no permanent residence in the present order and so can willingly accept exile-status."}
    ],
    "15": [
      {"type": "allusion", "target": "Hos 14:2", "note": "\"Take with you words and return to the LORD... we will pay with bulls the vows of our lips\" — Hebrews 13:15's 'fruit of lips that acknowledge his name' (literally: 'the fruit of lips') translates Hos 14:2 LXX (<em>anapausome ton karpon tōn cheiloōn hēmōn</em>). The prophetic replacement of animal sacrifice with the sacrifice of lips-praise is the OT anticipation of the new covenant's spiritual worship."}
    ],
    "20": [
      {"type": "allusion", "target": "Isa 63:11", "note": "\"Then he remembered the days of old, of Moses and his people. Where is he who brought them up out of the sea with the shepherds of his flock?\" — Hebrews 13:20's 'God of peace who brought again from the dead our Lord Jesus, the great shepherd of the sheep' echoes the Isaianic language of the shepherd-God who led his flock out through the sea. Moses-as-shepherd is now fulfilled in Jesus as the great shepherd brought through the sea of death."},
      {"type": "fulfillment", "target": "Ezek 37:24–26", "note": "\"My servant David shall be king over them, and they shall all have one shepherd... I will make a covenant of peace with them. It shall be an everlasting covenant with them\" — Hebrews 13:20's 'blood of the eternal covenant' with the great shepherd echoes Ezekiel's new David-covenant promise: the one shepherd over all God's people established through an everlasting covenant. Jesus is the Davidic shepherd of Ezekiel's vision."}
    ]
  }
}

def main():
    existing = load_echo('hebrews')
    merge_echo(existing, HEBREWS)
    save_echo('hebrews', existing)
    total = sum(len(vlist) for ch in existing.values() for vlist in ch.values())
    print(f'Hebrews echoes: {len(existing)} chapters, {total} total connections.')

if __name__ == '__main__':
    main()
