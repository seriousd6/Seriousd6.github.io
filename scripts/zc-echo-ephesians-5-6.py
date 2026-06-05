"""
Echo Commentary — Ephesians chapters 5–6
Run: python3 scripts/zc-echo-ephesians-5-6.py

Key decisions:
- Eph 5:2 fragrant-offering language: Lev 1:9 + Gen 8:21 as shadow; Ps 40:6-8 as type (willing obedience replaces animal sacrifice)
- Eph 5:14 "awake O sleeper" baptismal fragment: Isa 26:19 as primary echo, Isa 60:1-2 as secondary
- Eph 5:25-32 husband-wife/Christ-church: Gen 2:24 as explicit quote; Isa 54:5-8, Hos 2:19-20, Ezek 16:8 as the marriage covenant OT background
- Eph 6:2-3: Exod 20:12 = fulfillment (explicit quote)
- Eph 6:10-17 armor of God: Isa 59:14-17 as primary type; Isa 52:7 for feet; Isa 11:5 for belt; Ps 91:4 for shield
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

EPHESIANS = {
  "5": {
    "1": [
      {"type": "allusion", "target": "Deut 14:1–2", "note": "Israel is called to be 'children of the LORD your God' — the identity of son-of-God grounds the ethical imitation commanded. Paul extends this creational-covenantal pattern: beloved children imitate their divine Father."},
      {"type": "theme", "target": "Lev 19:2", "note": "\"Be holy, for I the LORD your God am holy\" — the Leviticus summons to holiness by divine imitation is the OT structural parallel to Paul's exhortation to imitate God as beloved children."}
    ],
    "2": [
      {"type": "shadow", "target": "Gen 8:21", "note": "Noah's burnt offering produces a 'pleasing aroma' (nichoach) that prompts God's covenant commitment. The fragrant-offering language establishes the pattern that pleasing sacrifice opens a new era of divine-human relationship — fulfilled in Christ's self-offering."},
      {"type": "shadow", "target": "Lev 1:9", "note": "The 'pleasing aroma' (reah nichoach / osmē euōdias in LXX) terminology for burnt offerings recurs throughout the sacrificial legislation. Paul applies the precise technical term to Christ's self-offering, placing the cross within the sacrificial logic of Leviticus."},
      {"type": "type", "target": "Ps 40:6–8", "note": "The Psalmist declares that God does not desire sacrifice and offering but rather obedience — 'I delight to do your will, O my God.' Hebrews 10 reads this psalm as the Son speaking his entry into the world; Paul's 'Christ loved us and gave himself' reflects the same willing-obedience-as-sacrifice pattern that replaces the animal-sacrifice system."}
    ],
    "5": [
      {"type": "allusion", "target": "Deut 29:20", "note": "The one who turns to idols 'will have no share in all these blessings' — the inheritance-exclusion for idolatry is the OT pattern behind Paul's declaration that the sexually immoral and covetous (idolater) has no inheritance in the kingdom."},
      {"type": "theme", "target": "1 Cor 6:9–10", "note": "Paul's own earlier catalog of the unrighteous who will not inherit the kingdom treats the same vices — the consistent NT application of the OT exclusion-of-the-impure-from-God's-presence principle."}
    ],
    "8": [
      {"type": "fulfillment", "target": "Isa 9:2", "note": "\"The people who walked in darkness have seen a great light; those who dwelt in a land of deep darkness, on them has light shined.\" Paul's contrast of darkness (former pagan state) with light (new identity in Christ) enacts the Isaianic promise of the great light coming to those in darkness."},
      {"type": "allusion", "target": "Isa 60:1–3", "note": "\"Arise, shine, for your light has come, and the glory of the LORD has risen upon you... nations shall come to your light.\" The Gentile-inclusion and light-spreading mission of the Ephesian community participates in the restoration-of-Zion light that Isaiah envisioned as the eschatological transformation of the nations."}
    ],
    "9": [
      {"type": "theme", "target": "Gal 5:22–23", "note": "The fruit of light (goodness, righteousness, truth) parallels the fruit of the Spirit in Galatians — both describe the organic moral output of the new-creation life, contrasted with the works of darkness/flesh."}
    ],
    "14": [
      {"type": "allusion", "target": "Isa 26:19", "note": "\"Your dead shall live; their bodies shall rise. You who dwell in the dust, awake and sing for joy! For your dew is a dew of light, and the earth will give birth to the dead.\" The 'awake... arise from the dead' language of Paul's probable baptismal fragment activates the Isaiah resurrection-dawn imagery."},
      {"type": "allusion", "target": "Isa 60:1", "note": "\"Arise, shine, for your light has come, and the glory of the LORD has risen upon you\" — the 'Christ will shine on you' promise echoes Isaiah's eschatological light-dawn as the new creation condition of the awakened sleeper."},
      {"type": "shadow", "target": "Ezek 37:1–14", "note": "The valley of dry bones: God commands the dead to hear the word, breath/spirit enters them, and they live. The pattern of divine address awakening the dead prefigures the baptismal awakening Paul's fragment describes."}
    ],
    "17": [
      {"type": "theme", "target": "Prov 2:1–6", "note": "The Wisdom tradition commands attentiveness to understand the will of the LORD — discernment of God's will as the goal of the wise person. Paul's 'understand what the will of the Lord is' places the Ephesian community within the wisdom-seeking tradition, now located christologically."}
    ],
    "18": [
      {"type": "fulfillment", "target": "Joel 2:28–29", "note": "\"I will pour out my Spirit on all flesh; your sons and daughters will prophesy\" — the Spirit-filling promised at Pentecost (Acts 2:17-18 citing Joel) is the eschatological background to Paul's imperative to be filled with the Spirit. Eph 5:18-19's Spirit-enabled worship (psalms, hymns, spiritual songs) instantiates the community dimension of the Spirit-outpouring."}
    ],
    "19": [
      {"type": "allusion", "target": "Ps 96:1–2", "note": "\"Sing to the LORD a new song... bless his name; tell of his salvation from day to day\" — the Psalter's invitation to the nations to sing new songs to God is taken up in Paul's instruction to sing psalms, hymns, and spiritual songs to the Lord."},
      {"type": "allusion", "target": "Ps 33:1–3", "note": "\"Shout for joy in the LORD, O you righteous! ... Sing to him a new song\" — the community praise commanded in the Psalter becomes the Spirit-enabled worship of the new-covenant assembly."}
    ],
    "20": [
      {"type": "theme", "target": "Ps 107:1", "note": "\"Give thanks to the LORD, for he is good; his steadfast love endures forever\" — the thanksgiving-always pattern echoes the Psalter's repeated summons to gratitude as the appropriate posture of the redeemed community before God."}
    ],
    "22": [
      {"type": "shadow", "target": "Gen 3:16", "note": "The post-fall condition includes the husband's rule over the wife. Paul's household code does not restore a patriarchal hierarchy by bare command but situates submission within the mutual submission of v21 and the Christ-analogy of vv25-32 — reframing the post-fall dynamic in terms of the cross-shaped love that transforms it."}
    ],
    "25": [
      {"type": "allusion", "target": "Isa 54:5–8", "note": "\"Your Maker is your husband... he has called you like a wife deserted and grieved in spirit... but with great compassion I will gather you.\" The covenantal marriage of God to Israel, expressed in Isaiah's oracle of restoration, is the OT background for the Christ-church relationship that grounds Paul's instruction to husbands."},
      {"type": "allusion", "target": "Hos 3:1", "note": "\"Love her as the LORD loves the people of Israel\" — Hosea's marriage to Gomer as enacted metaphor of God's persevering covenant love for unfaithful Israel becomes the pattern for husbands' love. Paul's 'as Christ loved the church' inherits Hosea's logic: the husband's love mirrors the divine covenant love that pursues the unfaithful."},
      {"type": "type", "target": "Ezek 16:8", "note": "\"I spread the corner of my garment over you and covered your nakedness; I made my vow to you and entered into a covenant with you\" — the covenant-as-marriage metaphor in Ezekiel 16 (God the husband taking Israel as wife) provides the structural background for the Christ-church marriage analogy of Ephesians 5."}
    ],
    "26": [
      {"type": "allusion", "target": "Ezek 36:25", "note": "\"I will sprinkle clean water on you, and you shall be clean from all your uncleannesses\" — the washing-with-water as purification is the background to Paul's 'having cleansed her by the washing of water with the word,' placing baptism within the Ezekielian new-covenant cleansing promise."}
    ],
    "27": [
      {"type": "allusion", "target": "Song 4:7", "note": "\"You are altogether beautiful, my love; there is no flaw in you\" — the beloved in the Song presented as without blemish or spot is the literary background to Paul's vision of the church 'without spot or wrinkle or any such thing,' presented holy and blameless."},
      {"type": "shadow", "target": "Lev 22:19–20", "note": "The sacrificial animal must be 'without blemish' (tamim) to be acceptable. Paul applies the unblemished-offering standard to the church that Christ presents to himself — the community is the acceptable offering of the new covenant."}
    ],
    "31": [
      {"type": "quote", "target": "Gen 2:24", "note": "\"Therefore a man shall leave his father and mother and hold fast to his wife, and the two shall become one flesh\" — Paul explicitly cites the creation ordinance as Scripture (\"as it is written\") and then interprets the 'one flesh' as a mysterion pointing beyond the human marriage to the Christ-church union. The citation controls the entire discussion of marriage in 5:22-33."},
      {"type": "shadow", "target": "Jer 31:31–32", "note": "The new covenant oracle contrasts with the old covenant made 'when I took them by the hand to bring them out of the land of Egypt, my covenant that they broke, though I was their husband' — the broken marriage-covenant of the old covenant gives way to a new covenant in which God will be their God. Paul's Christ-church marriage participates in this new covenant restoration."}
    ],
    "32": [
      {"type": "theme", "target": "Isa 62:5", "note": "\"As a bridegroom rejoices over the bride, so shall your God rejoice over you\" — the eschatological marriage of God and his people that Isaiah envisions as the restoration's goal is the background to Paul's identification of the deep mystery: the one-flesh union points to Christ and the church."}
    ]
  },
  "6": {
    "1": [
      {"type": "allusion", "target": "Prov 1:8", "note": "\"Hear, my son, your father's instruction, and forsake not your mother's teaching\" — the wisdom tradition's summons to filial obedience frames Paul's household instruction. The 'for this is right' grounds the command in natural-order wisdom, not only Mosaic command."}
    ],
    "2": [
      {"type": "quote", "target": "Exod 20:12", "note": "\"Honor your father and your mother\" — Paul explicitly cites the fifth commandment from the Decalogue, identifying it as 'the first commandment with a promise.' The citation of Exodus 20 (and Deut 5:16 with its attached promise) grounds the household code in Torah's covenantal ethics even while the wider law-keeping of Torah is not required of Gentile believers."},
      {"type": "quote", "target": "Deut 5:16", "note": "\"Honor your father and your mother, as the LORD your God commanded you, that your days may be long, and that it may go well with you in the land\" — the Deuteronomy version carries the extended promise ('that it may go well with you') that Paul incorporates into his citation. Paul applies the land-promise eschatologically to life in God's kingdom."}
    ],
    "4": [
      {"type": "allusion", "target": "Deut 6:7", "note": "\"You shall teach them diligently to your children, and shall talk of them when you sit in your house, and when you walk by the way\" — the Shema-context command to teach children is the OT background for Paul's instruction to bring children up in the discipline and instruction of the Lord."},
      {"type": "allusion", "target": "Prov 22:6", "note": "\"Train up a child in the way he should go; even when he is old he will not depart from it\" — the wisdom tradition's parental training mandate aligns with Paul's 'bring them up in the discipline and instruction of the Lord.'"}
    ],
    "5": [
      {"type": "theme", "target": "Lev 25:42–55", "note": "Israelite debt-slaves are the LORD's servants — their ultimate belonging is to God, not to human masters. Paul's instruction to slaves finds its OT background in this principle: service rendered to human masters is ultimately rendered to God (v7: 'as to the Lord and not to men')."}
    ],
    "9": [
      {"type": "allusion", "target": "Job 31:13–15", "note": "\"If I have rejected the cause of my servant... what then shall I do when God rises up? When he inquires, what shall I answer him? Did not he who made me in the womb make him?\" — Job's recognition that the creator holds masters accountable for treatment of servants is the wisdom-tradition background to Paul's 'he who is both their Master and yours is in heaven, and there is no partiality with him.'"},
      {"type": "theme", "target": "Deut 10:17", "note": "\"The LORD your God is God of gods and Lord of lords... who is not partial and takes no bribe\" — divine impartiality as the basis for just treatment of the vulnerable is the Deuteronomic background to Paul's warning that there is no partiality with God, applicable to masters."}
    ],
    "10": [
      {"type": "allusion", "target": "Ps 118:14", "note": "\"The LORD is my strength and my song\" — the Psalter's repeated location of strength in the LORD is the OT background to 'be strong in the Lord and in the strength of his might.'"},
      {"type": "allusion", "target": "Ps 27:1", "note": "\"The LORD is my light and my salvation; whom shall I fear? The LORD is the stronghold of my life\" — the Psalter's warrior-God confessions frame the armor-of-God section that follows: divine strength is the source of the community's resistance to evil."}
    ],
    "11": [
      {"type": "type", "target": "Isa 59:14–17", "note": "Isaiah depicts God himself donning the full armor of a divine warrior to execute justice when no human champion can: righteousness as breastplate, salvation as helmet, garments of vengeance. Paul transfers this divine-warrior armor to believers — they put on what God himself wore. The divine warrior who fought for Israel now equips the church with his own armor for spiritual warfare."},
      {"type": "shadow", "target": "Wis 5:17–20", "note": "The Wisdom of Solomon adapts Isaiah's divine warrior imagery: God takes 'his zeal as his whole armor and arms all creation to repel his enemies.' Paul draws on this apocalyptic divine-warrior tradition when he instructs believers to put on the full armor (panoplia) of God."}
    ],
    "14": [
      {"type": "allusion", "target": "Isa 11:5", "note": "\"Righteousness shall be the belt of his waist, and faithfulness the belt of his loins\" — the messianic king in Isaiah 11 wears righteousness as his belt. Paul distributes the messianic armor to all believers: the belt of truth and the breastplate of righteousness are drawn from the Isaianic portrait of the righteous Davidic king-warrior."},
      {"type": "allusion", "target": "Isa 59:17", "note": "\"He put on righteousness as a breastplate, and a helmet of salvation on his head\" — the direct source for Paul's breastplate-of-righteousness and helmet-of-salvation is Isaiah 59:17's picture of God the divine warrior. Paul's armor is the LXX Isaiah tradition translated into the believer's spiritual equipment."}
    ],
    "15": [
      {"type": "fulfillment", "target": "Isa 52:7", "note": "\"How beautiful upon the mountains are the feet of him who brings good news, who publishes peace, who brings good news of happiness, who publishes salvation\" — Paul's 'feet fitted with the readiness of the gospel of peace' directly enacts Isaiah 52:7's vision of the messenger whose feet carry the good news of peace. Romans 10:15 also cites this verse; here it becomes the third piece of the divine-warrior armor."}
    ],
    "16": [
      {"type": "allusion", "target": "Ps 91:4", "note": "\"He will cover you with his pinions, and under his wings you will find refuge; his faithfulness is a shield and buckler\" — the Psalmist's confidence in God's shielding faithfulness is the background to the shield of faith that extinguishes the flaming arrows of the evil one. The believer's faith functions as the divine shield the Psalmist trusted."},
      {"type": "allusion", "target": "Ps 7:10", "note": "\"My shield is with God, who saves the upright in heart\" — the Psalter's repeated appeal to God as shield is the OT background for the shield-of-faith imagery, where faith grasps the divine protection that the psalmists appealed to directly."}
    ],
    "17": [
      {"type": "allusion", "target": "Isa 49:2", "note": "\"He made my mouth like a sharp sword; in the shadow of his hand he hid me\" — the Servant's mouth as a sharp sword is the background to the sword of the Spirit which is the word of God. The Spirit's sword continues the Servant's sharp-mouthed proclamation that is God's own weapon."},
      {"type": "allusion", "target": "Isa 59:17", "note": "\"A helmet of salvation on his head\" — the third direct use of Isaiah 59:17 in the armor passage. The helmet of salvation in Paul is the divine warrior's own helmet, transferred to the community in Christ."},
      {"type": "theme", "target": "Isa 11:4", "note": "\"He shall strike the earth with the rod of his mouth, and with the breath of his lips he shall kill the wicked\" — the messianic king's word as his weapon of justice is the background for the Spirit-sword as God's offensive weapon in the believer's hands."}
    ],
    "18": [
      {"type": "allusion", "target": "Ps 55:17", "note": "\"Evening and morning and at noon I utter my complaint and moan, and he hears my voice\" — the Psalter's pattern of continuous, three-daily prayer is the OT background to Paul's 'praying at all times in the Spirit with all prayer and supplication.'"},
      {"type": "allusion", "target": "Dan 6:10", "note": "Daniel prays three times daily facing Jerusalem even under threat of death — a model of persevering prayer whose constancy Paul commends to the Ephesian community as the sustained posture of the armor-wearing soldier."}
    ],
    "19": [
      {"type": "allusion", "target": "Dan 2:19–23", "note": "Daniel prays that God would reveal the mystery (raz), and God reveals it to him — the mysterion-disclosure prayer pattern is the OT background for Paul's request for prayer that he may boldly make known the mystery of the gospel. The one who prays opens the channel for divine mystery-disclosure."},
      {"type": "allusion", "target": "Amos 3:7", "note": "\"Surely the Lord GOD does nothing without revealing his secret to his servants the prophets\" — the pattern of God revealing divine secrets to commissioned messengers is the background for the apostolic mysterion that Paul is tasked with proclaiming."}
    ],
    "20": [
      {"type": "allusion", "target": "Jer 15:20", "note": "\"I will make you to this people a fortified wall of bronze; they will fight against you, but they shall not prevail over you, for I am with you to save you and deliver you\" — God's commission to the prophet to speak boldly despite opposition is the OT pattern for the apostolic boldness Paul requests. The ambassador in chains enacts Jeremiah's commissioned-but-imprisoned prophetic role."}
    ]
  }
}

def main():
    existing = load_echo('ephesians')
    merge_echo(existing, EPHESIANS)
    save_echo('ephesians', existing)
    total = sum(len(v) for ch in existing.values() for v in ch.values())
    print(f'Ephesians echoes: {len(existing)} chapters, {total} total connections written.')

if __name__ == '__main__':
    main()
