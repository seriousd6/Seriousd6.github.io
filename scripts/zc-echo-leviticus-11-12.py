"""
Leviticus — all four layers.
Leviticus is the NT's primary type-source for atonement theology and the priesthood.
Key: Yom Kippur (16), purity laws (11-15), Holiness Code (17-26), Levitical offerings.
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

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ECHO = {
  "1": {
    "4": [
      {"type": "allusion", "target": "Heb 9:14", "note": "He shall lay his hand on the head of the burnt offering and it shall be accepted for him to make atonement — the laying of hands transfers the offerer's identity to the animal; this identification mechanism is the type of Christ's substitution: he bore our sins in his body on the tree (1 Pet 2:24)"}
    ]
  },
  "11": {
    "7": [
      {"type": "allusion", "target": "Acts 10:14", "note": "The pig is unclean because it does not chew the cud — the Levitical dietary laws declare pork definitively unclean; Peter's protest at the sheet vision ('I have never eaten anything that is common or unclean') quotes the Levitical clean/unclean framework; YHWH's response ('What God has made clean, do not call common') overturns the dietary boundary as a dividing wall between Jew and Gentile in the new covenant era"},
      {"type": "allusion", "target": "Mark 7:19", "note": "The pig is unclean — Mark 7:19 explicitly notes that Jesus declared all foods clean, nullifying the Levitical dietary distinction for new covenant believers; the editorial comment interprets Jesus's teaching on what defiles (coming from the heart, not the mouth) as abrogating the Mosaic food laws as an ongoing obligation for the church"}
    ],
    "44": [
      {"type": "fulfillment", "target": "1 Pet 1:16", "note": "You shall be holy, for I am holy — 1 Pet 1:16 quotes Lev 11:44-45 (also 19:2; 20:7) verbatim as the ground of the new covenant call to holiness; the same divine character that required separation from unclean foods now requires separation from sinful desires; Peter applies the Levitical holiness principle to Gentile believers, showing that the underlying demand transcends the specific food-law mechanism"}
    ],
    "45": [
      {"type": "allusion", "target": "1 Pet 1:15", "note": "I am YHWH who brought you up out of the land of Egypt to be your God; you shall therefore be holy, for I am holy — the redemption-grounds-holiness pattern of Lev 11:45 is precisely the pattern of 1 Pet 1:13-16: because you have been ransomed (v. 18-19), therefore be holy in all your conduct (v. 15); redemption precedes obligation in both testaments"}
    ]
  },
  "12": {
    "3": [
      {"type": "fulfillment", "target": "Luke 2:21", "note": "On the eighth day the flesh of his foreskin shall be circumcised — the Levitical requirement for circumcision on the eighth day following birth; Luke 2:21 records the circumcision of Jesus on the eighth day, explicitly fulfilling the law: when the time came to circumcise him, he was called Jesus; the incarnate Son submitted to the law's demands from the very first days of his life (Gal 4:4)"}
    ],
    "6": [
      {"type": "fulfillment", "target": "Luke 2:22", "note": "When the days of her purification are completed she shall bring a lamb... and a pigeon or a turtledove — the prescribed offering at the end of the mother's purification period; Luke 2:22-24 records that Mary and Joseph brought Jesus to the temple to present him to the Lord and to offer the sacrifice according to the Law of the Lord"}
    ],
    "8": [
      {"type": "fulfillment", "target": "Luke 2:24", "note": "If she cannot afford a lamb, she shall take two turtledoves or two young pigeons — the poor woman's substitute offering for purification after childbirth; Luke 2:24 notes that Mary and Joseph offered a pair of turtledoves or two young pigeons, quoting the Lev 12:8 poor-woman's provision; the detail establishes that Mary's family was poor, and signals that the one born to fulfill the law entered in poverty from the first day of his temple presentation"}
    ]
  },
  "16": {
    "2": [
      {"type": "fulfillment", "target": "Heb 9:7", "note": "But into the second tent only the high priest goes, and only once a year, and not without blood — the structure of Yom Kippur (Lev 16) is Hebrews' central OT text for demonstrating that the Levitical system was designed to be temporary and pointing forward to a greater reality: Christ enters the true holy of holies once for all by his own blood"}
    ],
    "15": [
      {"type": "fulfillment", "target": "Heb 9:12", "note": "He shall make atonement for the Holy Place because of the uncleannesses of the people — Aaron enters with the blood of a bull and a goat (Lev 16:14-15); Christ by his own blood entered once for all into the holy places (Heb 9:12), securing eternal redemption rather than annual covering"},
      {"type": "fulfillment", "target": "Heb 10:4", "note": "The blood of bulls and goats cannot take away sins — the Yom Kippur ritual (Lev 16) required annual repetition because animal blood could not permanently remove sin-guilt; this annual repetition was the system's built-in indication of its provisional character"}
    ],
    "20": [
      {"type": "allusion", "target": "John 1:29", "note": "The live goat — the scapegoat (Azazel) that bears the people's sins and is sent into the wilderness; Behold the Lamb of God who takes away the sin of the world: Christ is both the sacrificed goat whose blood atones (v. 15) and the scapegoat who removes sin by bearing it away"}
    ],
    "29": [
      {"type": "allusion", "target": "Heb 13:11-12", "note": "The bodies of those animals whose blood is brought into the holy places are burned outside the camp — Jesus also suffered outside the gate in order to sanctify the people through his own blood (Heb 13:12); the burning of the sin-offering carcass outside the camp is the type of the crucifixion outside Jerusalem"}
    ]
  },
  "17": {
    "11": [
      {"type": "fulfillment", "target": "Heb 9:22", "note": "For the life of the flesh is in the blood and I have given it for you on the altar to make atonement for your souls — the blood-for-life principle (Lev 17:11) is the theological foundation of all sacrificial atonement; without the shedding of blood there is no forgiveness of sins (Heb 9:22) applies this principle to Christ's death"}
    ]
  },
  "19": {
    "18": [
      {"type": "fulfillment", "target": "Matt 22:39", "note": "You shall love your neighbor as yourself — the great commandment from the Holiness Code (Lev 19:18); Jesus names this as the second great commandment and Paul calls it the fulfillment of the whole law (Gal 5:14; Rom 13:9); James calls it the royal law (Jas 2:8)"},
      {"type": "allusion", "target": "Gal 5:14", "note": "For the whole law is fulfilled in one word: You shall love your neighbor as yourself — Paul cites Lev 19:18 as the summary of the entire Mosaic law's ethical demand; the law's social obligations are summed in neighbor-love, which is the character of the Spirit-filled life"}
    ]
  },
  "26": {
    "12": [
      {"type": "fulfillment", "target": "2 Cor 6:16", "note": "I will walk among you and will be your God and you shall be my people — the covenant formula of Lev 26:12 is the OT's recurring covenant-relationship phrase (also Ezek 36:28; Jer 31:33); Paul quotes it in 2 Cor 6:16 as the basis for the church as the temple of the living God; it is fulfilled in the Spirit's indwelling of the new covenant community"}
    ]
  }
}

ORIGINAL = {
  "1": {
    "4": "<p><strong>vesomach yado al rosh haolah veratzon lo lekapper alav</strong>: 'He shall lay his hand on the head of the burnt offering, and it shall be accepted for him to make atonement for him.' The <em>semikah</em> (laying of hands) is the key act of self-identification with the sacrifice: the offerer transfers his identity to the animal, which then represents him before YHWH. The term <em>kopher</em> (ransom/atonement, verb <em>kipper</em>) has its root either in 'to cover' or 'to ransom/substitute' (the latter supported by the Semitic cognate). The NT takes both senses: Christ's blood covers/forgives sin (Col 2:13-14) and he gives his life as a ransom (<em>lytron</em>) for many (Mark 10:45).</p>"
  },
  "16": {
    "2": "<p>Yom Kippur (Day of Atonement) is the annual reset of Israel's covenant relationship: the accumulated sin of the year is dealt with by the high priest's double ritual — (1) the bull's blood for his own sin, (2) one goat killed for the people's sin (the sacrificed goat), (3) one goat bearing the sins symbolically into the wilderness (the scapegoat, <em>azazel</em>). The two-goat ritual together communicates the complete theology of atonement: blood-payment (the dead goat) + removal (the scapegoat). Christ fulfills both aspects: his blood makes propitiation and his bearing of sin removes it ('as far as the east is from the west, so far does he remove our transgressions from us', Ps 103:12).</p>"
  },
  "17": {
    "11": "<p><strong>ki nefesh habasar badam hi vaani netatihu lachem al hamizbeach lekapper al nafshoteichem ki hadam hu bakafra banefesh</strong>: 'For the life [<em>nefesh</em>] of the flesh is in the blood, and I have given it for you on the altar to make atonement for your souls [<em>nefesh</em>], for it is the blood that makes atonement by the life.' The blood-for-life exchange is the theological axiom underlying all sacrifice: blood (= life) offered for life (= the offerer's forfeit life). The principle is stated as divine appointment — 'I have given it for you on the altar' — sacrifice is not a human invention but a divinely ordained mechanism of atonement. Hebrews 9:22's 'without the shedding of blood there is no forgiveness of sins' is a direct application of Lev 17:11 to Christ's death.</p>"
  },
  "19": {
    "18": "<p><strong>veahavta lereiacha kamocha ani YHWH</strong>: 'You shall love your neighbor as yourself: I am YHWH.' The neighbor-love command concludes with the divine self-identification formula (<em>ani YHWH</em>) — the obligation is grounded not in a social contract but in YHWH's own character and authority. The scope of <em>rea</em> (neighbor) in Leviticus 19 extends throughout the chapter to include resident aliens (v. 34: 'love him as yourself, for you were aliens in Egypt'). Jesus's parable of the Good Samaritan expands the neighbor-category to include the unexpected outsider, but the Levitical warrant is already broader than its surface reading.</p>"
  }
}

CONTEXT = {
  "1": {
    "1": "<p>Leviticus is the central book of the Torah and the most liturgical: it contains the instructions for the five primary offerings (burnt, grain, peace, sin, guilt), the ordination of the Aaronic priesthood, the purity laws, the Holiness Code (chs. 17-26), and the festival calendar. Its context is the completed tabernacle (Exod 40) — YHWH's glory has filled the structure, and now YHWH speaks from within it (Lev 1:1: YHWH called to Moses and spoke to him from the tent of meeting). The book addresses the central problem of how a holy God can dwell among a sinful people — the answer is a complex system of sacrifice, priesthood, purification, and consecration. Hebrews reads Leviticus as the most detailed typological preparation for Christ's high-priestly work.</p>"
  },
  "16": {
    "1": "<p>Yom Kippur (the Day of Atonement, Lev 23:27-28) became the most solemn day in the Jewish calendar — the only mandatory communal fast in the Torah. In Second Temple Judaism, it was the one day the high priest entered the most holy place. When the temple was destroyed in 70 CE, the entire Yom Kippur sacrificial system became inoperative — Hebrews' argument that Christ's once-for-all sacrifice supersedes the annual Yom Kippur ritual became immediately relevant to Jewish Christians watching the temple system collapse. The phrase 'once for all' (<em>ephapax</em>, Heb 9:12; 10:10) is Hebrews' direct response to Yom Kippur's annual repetition.</p>"
  }
}

CHRIST = {
  "16": {
    "2": "<p>A fulfillment: 'YHWH said to Moses, Tell Aaron your brother not to come at any time into the Holy Place inside the veil, before the mercy seat that is on the ark, so that he may not die. For I will appear in the cloud over the mercy seat.' The entire Yom Kippur ritual — its restrictions, its blood-sprinkling, its once-per-year access, its careful approach protocol — is the OT's most detailed type of Christ's high-priestly work. Hebrews 9:1-14 maps the Yom Kippur elements onto Christ systematically: the holy of holies → heaven; the high priest → Christ; bull and goat blood → Christ's own blood; annual repetition → once for all; the mercy seat → Christ as <em>hilasterion</em> (Rom 3:25). Every element of Leviticus 16 is the shadow; Christ is the substance.</p>"
  },
  "17": {
    "11": "<p>A direct revelation: 'For the life of the flesh is in the blood, and I have given it for you on the altar to make atonement for your souls, for it is the blood that makes atonement by the life.' This verse is the theological axiom that explains why Christ had to die a bloody death — not a natural death, not a symbolic death, but a sacrificial death involving the shedding of blood. The divine appointment ('I have given it for you on the altar') means that blood-atonement is not a primitive accommodation to human psychology but a divine mechanism built into creation-order: life given for life, blood for blood. Christ's death fulfills this principle at its ultimate level: his blood, the blood of the God-man, atones not for one year or one nation but once for all humanity (Heb 9:12).</p>"
  },
  "19": {
    "18": "<p>A direct revelation: 'You shall love your neighbor as yourself: I am YHWH.' Jesus elevates Lev 19:18 to the second-greatest commandment (Matt 22:39) and Paul calls it the fulfillment of the whole law (Gal 5:14; Rom 13:9). But Christ does not merely cite the command — he embodies it: 'Greater love has no one than this, that someone lay down his life for his friends' (John 15:13). The neighbor-love of Lev 19:18 reaches its ultimate expression in the cross, where Christ loved his neighbors — his enemies — at the cost of his life (Rom 5:8: God demonstrates his love for us in that while we were still sinners, Christ died for us).</p>"
  }
}

def main():
    e = load_echo('leviticus')
    merge_echo(e, ECHO)
    save_echo('leviticus', e)

    c = load_comm('mkt-original', 'leviticus')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', 'leviticus', c)

    c = load_comm('mkt-context', 'leviticus')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', 'leviticus', c)

    c = load_comm('mkt-christ', 'leviticus')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', 'leviticus', c)

    print('leviticus: all 4 layers written')

if __name__ == '__main__':
    main()
