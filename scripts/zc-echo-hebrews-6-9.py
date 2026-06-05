"""
Echo Commentary — Hebrews chapters 6–9
Run: python3 scripts/zc-echo-hebrews-6-9.py

Key decisions:
- Ch7: Melchizedek typology is the heart; Gen 14 shadow and Ps 110:4 fulfillment dominate
- Ch8: Jer 31:31-34 new covenant quote = fulfillment (author explicitly cites it as such)
- Ch9: Tabernacle/Levitical system is type; each element mapped specifically to Christ's ministry
- Num 19 (red heifer) = shadow for ch9's cleansing blood argument
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
  "6": {
    "1": [
      {"type": "theme", "target": "Deut 30:2", "note": "\"Return to the LORD your God and obey his voice\" — the language of repentance (<em>metanoia</em>) from dead works is grounded in the OT prophetic summons to turn back to God. The Hebrews community is being warned not to need to re-lay the foundational repentance that marked their conversion."}
    ],
    "4": [
      {"type": "allusion", "target": "Num 14:20–23", "note": "The wilderness generation who saw God's mighty acts and tasted his goodness — the manna and the signs — yet hardened their hearts is the OT type behind the warning of 6:4-6. Those who have 'tasted the heavenly gift' and 'shared in the Holy Spirit' and then fall away are enacting the Meribah pattern: apostasy by those who experienced the covenant grace."}
    ],
    "7": [
      {"type": "allusion", "target": "Gen 3:17–19", "note": "\"Cursed is the ground because of you... thorns and thistles it shall bring forth for you\" — the land that produces thorns and thistles bears the curse (6:8). Hebrews applies the agricultural curse imagery of Genesis 3 to the apostate community: the community that produces thorns is 'near to being cursed,' echoing the ground cursed at the Fall."},
      {"type": "allusion", "target": "Isa 5:1–7", "note": "The vineyard that God cultivated which produced wild grapes instead of good fruit — Isaiah's parable of judgment is the background to the land-that-produces-thorns imagery. The community is the cultivated field; unfruitfulness leads to curse and burning."}
    ],
    "13": [
      {"type": "quote", "target": "Gen 22:16–17", "note": "\"By myself I have sworn, declares the LORD, because you have done this... I will surely bless you\" — Hebrews 6:13-14 cites God's oath to Abraham after the Aqedah (binding of Isaac). The divine self-swearing (swearing by himself since there is no greater) grounds the certainty of the promise. Abraham's patient endurance receiving the promise is the example of faith-and-patience that the community is to imitate."}
    ],
    "19": [
      {"type": "type", "target": "Lev 16:1–4", "note": "The high priest who enters behind the curtain into the Most Holy Place on the Day of Atonement is the OT type for Christ as forerunner entering the heavenly sanctuary. The curtain-threshold between the Holy Place and Most Holy Place is the structural type for the threshold that Christ crosses as the community's representative and forerunner."}
    ],
    "20": [
      {"type": "fulfillment", "target": "Ps 110:4", "note": "\"A priest forever, after the order of Melchizedek\" — 6:20 returns to Ps 110:4 as Jesus the forerunner becomes a high priest after the order of Melchizedek, setting up the extended exposition of Melchizedek's significance in chapter 7."}
    ]
  },
  "7": {
    "1": [
      {"type": "shadow", "target": "Gen 14:18–20", "note": "\"Melchizedek king of Salem brought out bread and wine. He was priest of God Most High. And he blessed him, and said, 'Blessed be Abram by God Most High, Possessor of heaven and earth'\" — Hebrews 7:1-3 retells Genesis 14:18-20 with typological attention. Every feature of the Genesis narrative is read as significant for the Son's priesthood: priest-king combination, no genealogy given, blessing the patriarch, receiving tithes. The historical episode becomes the shadow whose features point forward to the Son."}
    ],
    "3": [
      {"type": "shadow", "target": "Gen 14:18", "note": "Melchizedek appears in Genesis 14 without father, mother, genealogy, beginning of days, or end of life — not because these did not exist historically but because the Genesis text's silence about them is typologically significant. Hebrews 7:3 reads the narrative's silence as a designed type: Melchizedek 'resembling the Son of God' in his textual/typological existence, continues as a priest in the Genesis narrative without recorded death."}
    ],
    "7": [
      {"type": "theme", "target": "Gen 14:19", "note": "\"Blessed be Abram by God Most High\" — Hebrews 7:7 draws out the implication of the Genesis blessing: the lesser is blessed by the greater. Abraham, the patriarch from whom the Levitical priesthood descends, was blessed by Melchizedek — establishing Melchizedek's superiority over the entire Levitical order."}
    ],
    "9": [
      {"type": "shadow", "target": "Gen 14:20", "note": "\"And Abram gave him a tenth of everything\" — Levi, as unborn descendant of Abraham, can be said to have paid tithes through Abraham to Melchizedek (Heb 7:9-10). The Genesis tithes become the basis for arguing that the Levitical order itself acknowledges the Melchizedekian order's superiority."}
    ],
    "11": [
      {"type": "type", "target": "Lev 8:1–9:7", "note": "The Levitical priesthood instituted at Sinai through Aaron's ordination is the OT type that Hebrews 7 declares insufficient for perfection. The existence of Ps 110:4's Melchizedekian priest after the Levitical institution proves (to Hebrews' argument) that the Levitical order could not achieve what was needed — a different order of priest was required."}
    ],
    "17": [
      {"type": "fulfillment", "target": "Ps 110:4", "note": "\"You are a priest forever, after the order of Melchizedek\" — cited again in 7:17 as the scriptural testimony to the Son's eternal priestly office. The <em>kata taxin Melchisedek</em> (after the order/pattern of Melchizedek) is Hebrews' technical formula for the non-Levitical, oath-backed, eternal priesthood."}
    ],
    "18": [
      {"type": "shadow", "target": "Num 18:1–7", "note": "The Levitical regulations setting out the priests' duties and limitations represent the 'former commandment' that is set aside because of its weakness and uselessness (Heb 7:18). The regulatory framework of the Levitical priesthood, however detailed, could not bring perfection — its own structure (requiring repeated offerings, limited by death) demonstrates its provisional character."}
    ],
    "21": [
      {"type": "fulfillment", "target": "Ps 110:4", "note": "\"The Lord has sworn and will not change his mind, 'You are a priest forever'\" — Hebrews 7:21 emphasizes the oath dimension of Ps 110:4: unlike the Levitical priests installed without an oath, the Son is installed by God's sworn oath. The oath makes the Son's priestly appointment irrevocable — God cannot change his mind about it."}
    ],
    "25": [
      {"type": "allusion", "target": "Isa 53:12", "note": "\"He bore the sin of many, and makes intercession for the transgressors\" — the Servant's ongoing intercession is the OT background for Christ's living to make intercession for those who draw near through him. The Servant who bore sin and intercedes is the pattern fulfilled in the risen, interceding high priest."}
    ],
    "27": [
      {"type": "type", "target": "Lev 9:7", "note": "The high priest's offering for his own sins and then for the people's is the Levitical type that Christ surpasses: he had no need to offer for himself, offered once (not daily), and offered himself (not animals). The Day of Atonement structure of Lev 9 and Lev 16 provides the three-fold contrast."},
      {"type": "type", "target": "Lev 16:6", "note": "\"Aaron shall offer the bull as a sin offering for himself and make atonement for himself and for his house\" — the high priest's annual self-offering is the type that Christ fulfills and supersedes by his single, self-offered sacrifice that required no self-atonement."}
    ],
    "28": [
      {"type": "fulfillment", "target": "Ps 110:4", "note": "The Son perfected forever (appointed by the oath-word of Ps 110:4) contrasts with the law that appoints priests in their weakness. The oath came after the law, superseding it — the scriptural argument for the Melchizedekian priesthood's priority over the Levitical."}
    ]
  },
  "8": {
    "1": [
      {"type": "fulfillment", "target": "Ps 110:1", "note": "\"Sit at my right hand\" — Hebrews 8:1 returns to the right-hand session of Ps 110:1 as the summary of its argument: the high priest who is seated at the right hand of the Majesty in heaven. The heavenly session and the Melchizedekian priesthood are two aspects of the one Ps 110 reality."}
    ],
    "2": [
      {"type": "type", "target": "Exod 26:30", "note": "\"Then you shall erect the tabernacle according to the plan for it that you were shown on the mountain\" — the tabernacle built according to the heavenly pattern shown to Moses is the OT type-structure. The earthly sanctuary is a copy (<em>hypodeigma kai skia</em>, copy and shadow) of the heavenly reality. The type-antitype relationship between earthly and heavenly sanctuary is the conceptual basis for Hebrews' entire argument."}
    ],
    "4": [
      {"type": "shadow", "target": "Num 3:1–10", "note": "The Levitical priests' service at the earthly tabernacle/temple is the shadow-service of which Jesus's heavenly service is the reality. The shadow-service has genuine authority in its own sphere ('according to the law') but is shadow, not substance."}
    ],
    "5": [
      {"type": "quote", "target": "Exod 25:40", "note": "\"See that you make everything according to the pattern that was shown you on the mountain\" — Hebrews 8:5 cites Exod 25:40 as proof that Moses knew the earthly tabernacle was a copy of the heavenly original. The divine command to follow the pattern implies the existence of the pattern — the heavenly sanctuary is the reality, the earthly its shadow."}
    ],
    "8": [
      {"type": "fulfillment", "target": "Jer 31:31–34", "note": "\"Behold, the days are coming, declares the LORD, when I will make a new covenant with the house of Israel and the house of Judah, not like the covenant that I made with their fathers... I will put my law within them... I will remember their sin no more\" — Hebrews 8:8-12 cites Jer 31:31-34 in full as the decisive scriptural proof that the Mosaic covenant was designed to be superseded. The new covenant's internal law, universal God-knowledge, and complete forgiveness are the specific improvements that Hebrews identifies as the Mosaic covenant's counterparts that it could not achieve."}
    ],
    "13": [
      {"type": "fulfillment", "target": "Jer 31:31", "note": "\"A new covenant\" — Hebrews 8:13 applies the logical principle: when God says 'new,' he implies the old is becoming obsolete. The citation of Jer 31's 'new covenant' is the scriptural self-testimony that the Mosaic covenant was provisional — the Scripture itself declares its own obsolescence through the new-covenant promise."}
    ]
  },
  "9": {
    "1": [
      {"type": "type", "target": "Exod 25:1–27:21", "note": "The tabernacle furnishings and layout described in Exodus 25-27 are the OT types that Hebrews 9:1-5 inventories: the lampstand, the table, the showbread, the incense altar, the ark, the cherubim, the mercy seat. Each item in the earthly sanctuary corresponds typologically to a heavenly reality enacted in Christ's high-priestly ministry."}
    ],
    "2": [
      {"type": "type", "target": "Exod 26:1–37", "note": "The two-room structure of the tabernacle — the Holy Place and the Most Holy Place separated by the curtain — is the type for Hebrews' spatial theology: the Holy Place represents the earthly-access realm; the Most Holy Place (where the ark and mercy seat stood) represents the divine presence into which only the high priest could enter. Christ enters the true Most Holy Place — heaven itself (9:24)."}
    ],
    "4": [
      {"type": "type", "target": "Exod 16:33–34", "note": "The gold jar of manna placed before the Testimony in the Most Holy Place is one of the ark's contents that Hebrews 9:4 catalogs. The preserved manna in the ark typologically connects to Christ as the true bread from heaven (John 6:35) — the eschatological manna preserved in the heavenly sanctuary."},
      {"type": "type", "target": "Num 17:8–10", "note": "Aaron's staff that budded — placed before the Testimony as a sign — is the second item in the ark's contents (Heb 9:4). The priestly staff that produced life out of deadness typologically anticipates the resurrection of the true high priest whose life-from-death validates his priestly appointment."}
    ],
    "7": [
      {"type": "type", "target": "Lev 16:1–34", "note": "The Day of Atonement ritual — the high priest alone entering the Most Holy Place once a year with blood for himself and the people — is the central OT type for Hebrews 9. Every element of Lev 16's ritual becomes a type: the annual repetition, the blood requirement, the self-offering for sin, the sprinkling on the mercy seat, the access restriction. Christ fulfills and surpasses each element."}
    ],
    "8": [
      {"type": "shadow", "target": "Lev 16:2", "note": "\"The LORD said to Moses, 'Tell Aaron your brother not to come at any time into the Holy Place inside the veil... so that he may not die'\" — the restriction on high priestly access is the typological signal that the way into God's presence had not yet been opened. The Holy Spirit was indicating, through the access restriction, that the path to God was not yet fully disclosed."}
    ],
    "11": [
      {"type": "fulfillment", "target": "Lev 16:15–17", "note": "The high priest's entry into the Most Holy Place with blood to make atonement is fulfilled by Christ's entry into the heavenly sanctuary with his own blood. The structural parallel: priest enters sacred space with blood, makes atonement, emerges — but in Christ the blood is his own, the space is the true heavenly sanctuary, and the atonement is eternal."}
    ],
    "13": [
      {"type": "shadow", "target": "Num 19:1–22", "note": "The red heifer ritual — burning a red heifer without blemish, mixing the ashes with water, sprinkling on the ceremonially unclean — is one of the purification rites Hebrews 9:13 cites alongside the goat and bull blood of Lev 16. The heifer ashes and blood purified outward/fleshly uncleanness; Christ's blood purifies the conscience. The shadow-reality structure of Num 19 is the type for the greater purification."},
      {"type": "shadow", "target": "Lev 16:3", "note": "The bull and goat blood that consecrated and cleansed the people are the OT shadows of the blood-offering that Hebrews 9:13 references. The animal blood's purifying effect was real but limited — external, repeated, unable to perfect the conscience."}
    ],
    "15": [
      {"type": "fulfillment", "target": "Jer 31:34", "note": "\"I will forgive their iniquity, and I will remember their sin no more\" — the complete forgiveness promised in the new covenant (Jer 31:34) is what Christ's death achieves: redemption from the transgressions under the first covenant, so that those called may receive the promised eternal inheritance. The death that redeems backward (transgressions under the first covenant) enacts the Jeremianic complete forgiveness."}
    ],
    "19": [
      {"type": "type", "target": "Exod 24:3–8", "note": "\"Then he took the Book of the Covenant and read it in the hearing of the people... Moses took the blood and threw it on the people and said, 'Behold the blood of the covenant that the LORD has made with you'\" — the Sinai covenant ratification with blood is the OT type for Hebrews 9:19-20. The first covenant's blood-inauguration establishes the principle that 'without the shedding of blood there is no forgiveness of sins' (9:22)."}
    ],
    "20": [
      {"type": "quote", "target": "Exod 24:8", "note": "\"This is the blood of the covenant that God commanded for you\" — Hebrews 9:20 cites Exod 24:8 (with minor variation from MT/LXX; cf. Jesus's words at the Last Supper in Mark 14:24 / Matt 26:28: 'This is my blood of the covenant'). The citation establishes the covenantal blood-principle that governs both Sinai and Calvary."}
    ],
    "22": [
      {"type": "theme", "target": "Lev 17:11", "note": "\"The life of the flesh is in the blood, and I have given it for you on the altar to make atonement for your souls, for it is the blood that makes atonement by the life\" — the Levitical blood-theology grounds Hebrews 9:22's summary: 'without the shedding of blood there is no forgiveness.' Lev 17:11 is the OT basis for the blood-forgiveness connection that runs through the entire sacrificial system and that Christ's blood-offering fulfills."}
    ],
    "24": [
      {"type": "type", "target": "Exod 25:40", "note": "The earthly sanctuary as a copy of the true heavenly sanctuary — Hebrews 9:24 identifies the heavenly sanctuary explicitly as 'not a hand-made holy place, a copy of the true, but into heaven itself.' The Exodus 25:40 pattern-command establishes that the earthly sanctuary's significance lay in its pointing to the heavenly."}
    ],
    "26": [
      {"type": "fulfillment", "target": "Dan 9:24", "note": "\"Seventy weeks are decreed about your people... to atone for iniquity, to bring in everlasting righteousness\" — Hebrews 9:26's 'at the end of the ages he has appeared to put away sin by the sacrifice of himself' participates in the Danielic periodization of history that leads to the atoning of iniquity at the end of the appointed time."}
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
