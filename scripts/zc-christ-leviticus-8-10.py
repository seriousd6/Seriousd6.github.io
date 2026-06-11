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
  "8": {
    "1": "<p>A type: YHWH commands Moses to ordain Aaron — the priesthood is constituted by divine appointment, not human ambition. Heb 5:4-5 cites this pattern directly: &ldquo;no one takes this honor for himself, but only when called by God, just as Aaron was. So also Christ did not exalt himself to be made a high priest, but was appointed by him who said to him, &lsquo;You are my Son.&rsquo;&rdquo; Christ's high priesthood is divinely ordained, not self-assumed.</p>",
    "2": "<p>A type: the items assembled for ordination — garments, oil, sin offering, burnt offering, unleavened bread — prefigure the full equipment of Christ's priestly ministry: righteousness (garments), the Spirit (anointing oil), substitutionary atonement (sin offering), total self-offering (burnt offering), and his body as the bread of life (unleavened bread). Each element is gathered because each will be needed in the definitive priestly work.</p>",
    "3": "<p>A type: the congregation assembles as witnesses of Aaron's ordination. Christ's designation as High Priest is similarly public: declared at the baptism (&ldquo;This is my beloved Son&rdquo;, Matt 3:17), confirmed at the transfiguration (Matt 17:5), and proclaimed at the resurrection (Rom 1:4: &ldquo;declared to be the Son of God in power&hellip;by his resurrection from the dead&rdquo;).</p>",
    "4": "<p>A type: Moses, who stands closer to YHWH than any other (Exod 33:11), installs Aaron. God the Father installs Christ as High Priest by the sworn oath of Ps 110:4: &ldquo;The Lord has sworn and will not change his mind, &lsquo;You are a priest forever after the order of Melchizedek.&rsquo;&rdquo; (Heb 7:21). The Father's oath is the ultimate ordination.</p>",
    "5": "<p>A type: &ldquo;This is the thing that YHWH has commanded to be done&rdquo; — the formula of divine appointment. Christ's priesthood fulfills every &ldquo;as YHWH commanded&rdquo; in the Levitical system. His obedience to the Father's commission was total: &ldquo;I glorified you on earth, having accomplished the work that you gave me to do&rdquo; (John 17:4).</p>",
    "6": "<p>A type: washing precedes consecration. Christ's baptism in the Jordan (Matt 3:13-17) is the NT counterpart: though he had no sin to remove, his immersion publicly aligned him with sinful humanity and inaugurated his priestly ministry. The descent of the Spirit at baptism is the NT anointing of the priest (v. 12); washing and anointing are the twin entries into the priestly office.</p>",
    "7": "<p>A type: Aaron is clothed in the priestly garments. Christ is clothed in perfect righteousness — not as an external garment but as his very nature (Heb 7:26: &ldquo;holy, innocent, unstained, separated from sinners&rdquo;). Those who believe are in turn &ldquo;clothed in Christ&rdquo; (Gal 3:27), receiving the priestly dignity that derives from his righteousness, not their own.</p>",
    "8": "<p>A type: the Urim and Thummim placed in the breastpiece — the instruments of divine disclosure. Christ is the one in whom &ldquo;all the treasures of wisdom and knowledge are hidden&rdquo; (Col 2:3). The need for external oracular instruments points toward the Son himself, through whom God has &ldquo;spoken to us&rdquo; definitively (Heb 1:2). In Christ, the question-and-answer device is replaced by the Word himself.</p>",
    "9": "<p>A type: the golden plate &ldquo;Holy to YHWH&rdquo; on the high priest's turban atones for the people's inadvertent offenses. Christ is intrinsically holy (Heb 7:26) and bears the people's guilt not on a metal plate but in his own body. The crown of thorns placed on Jesus' head (John 19:2) is a grotesque inversion of this holy crown — the soldiers unknowingly enacted the priestly type: the holy one bears the people's guilt on his head.</p>",
    "10": "<p>A type: the anointing of the tabernacle precedes the anointing of Aaron. Christ consecrates the heavenly sanctuary itself (Heb 9:23-24: &ldquo;the heavenly things themselves needed to be purified with better sacrifices&rdquo;); he enters the true tent &ldquo;set up by the Lord and not by man&rdquo; (Heb 8:2). Heaven is the space prepared for his eternal priestly ministry.</p>",
    "11": "<p>A type: the sevenfold anointing of the altar — complete consecration of the place of sacrifice. Christ's cross is the ultimate altar, consecrated by his own blood; his sacrifice sanctifies all who approach by faith (Heb 10:14: &ldquo;by a single offering he has perfected for all time those who are being sanctified&rdquo;). The completeness of the sevenfold anointing points to the completeness of his atoning work.</p>",
    "12": "<p>A fulfillment: Moses pours the anointing oil on Aaron's head — the <em>mashiach</em> (anointed one) is constituted. Jesus is the Christ (<em>Christos</em> = anointed), the one on whom the Spirit descended at the Jordan &ldquo;in bodily form like a dove&rdquo; (Luke 3:22). Peter's Pentecost sermon declares the fulfillment: &ldquo;God has made him both Lord and Christ, this Jesus whom you crucified&rdquo; (Acts 2:36).</p>",
    "13": "<p>A type: Aaron's sons are clothed in the priestly garments — the priestly order extends beyond the high priest to all who share in his consecration. Christ is the High Priest; believers are &ldquo;a royal priesthood&rdquo; (1 Pet 2:9) by virtue of union with him. The sons' consecration follows from the head's consecration — &ldquo;if the dough offered as firstfruits is holy, so is the whole lump&rdquo; (Rom 11:16).</p>",
    "14": "<p>A type: the sin offering is performed first — atonement precedes dedication. Christ deals with sin before presenting himself as the dedicated priest-king. His death (sin-offering) precedes his resurrection (new-life offering). He could not ascend to the Father's right hand until the sin question was settled — once for all, at the cross (Heb 9:26: &ldquo;he has appeared once for all at the end of the ages to put away sin by the sacrifice of himself&rdquo;).</p>",
    "15": "<p>A type: blood applied to the altar's horns consecrates it as the site of atonement. Christ's blood consecrates the heavenly altar — the mercy seat — as the definitive place of meeting between YHWH and humanity. Paul describes Christ as the <em>hilasterion</em> (mercy seat/propitiation) in Rom 3:25: &ldquo;whom God put forward as a propitiation by his blood.&rdquo; The altar's horns that Israelites grasped for refuge (1 Kings 1:50) are a type of clinging to the cross as the place of safety.</p>",
    "16": "<p>A type: the fat portions — the richest, most inward parts — are burned for YHWH. Christ offers what is most interior, most essential: his own soul (<em>nefesh</em>) as an offering for sin (Isa 53:10: &ldquo;when his soul makes an offering for guilt&rdquo;). He holds back nothing, not even his own life (Phil 2:8: &ldquo;obedient to the point of death&rdquo;).</p>",
    "17": "<p>A fulfillment: the sin-offering carcass burned outside the camp. Heb 13:11-12 reads this as a direct type of the crucifixion: &ldquo;so Jesus also suffered outside the gate in order to sanctify the people through his own blood.&rdquo; Golgotha was outside the walls of Jerusalem — the spatial correspondence is exact. The burning outside the camp is the enacted theology of what the cross accomplishes: sin removed, expelled, destroyed.</p>",
    "18": "<p>A type: the burnt offering ram — entirely consumed, nothing reserved. Christ's total self-offering: &ldquo;he loved us and gave himself up for us, a fragrant offering and sacrifice to God&rdquo; (Eph 5:2). The burnt offering has no portion for the priest or offerer — it ascends entirely to YHWH. Christ's offering was similarly unreserved: &ldquo;I lay it down of my own accord&rdquo; (John 10:18).</p>",
    "19": "<p>A type: blood thrown against all four sides of the altar — comprehensive coverage. Christ's blood covers every approach to God, every direction from which sinners come, every category of human guilt: &ldquo;he is the propitiation for our sins, and not for ours only but also for the sins of the whole world&rdquo; (1 John 2:2).</p>",
    "20": "<p>A type: even the entrails and legs are washed and burned — the offering's completeness reaches every part. Christ held nothing back: not his reputation (Phil 2:7), not his comfort (Luke 9:58), not his life (John 15:13). The offering is comprehensive because the need is comprehensive.</p>",
    "21": "<p>A fulfillment: the whole burnt offering rises as a <em>reyach nichoch</em> (pleasing aroma) to YHWH. Paul cites this formula directly for Christ's sacrifice: &ldquo;Christ loved us and gave himself up for us, a fragrant offering and sacrifice to God&rdquo; (Eph 5:2). The divine reception of Christ's death as &ldquo;pleasing&rdquo; declares that the Father's wrath is fully satisfied. What was type in the burnt offering is substance in the cross.</p>",
    "22": "<p>A type: the ram of the <em>milu'im</em> — the offering that fills Aaron's hands with the priestly office. Christ's hands are filled with his completed sacrifice: &ldquo;when Christ had offered for all time a single sacrifice for sins, he sat down at the right hand of God&rdquo; (Heb 10:12). His hands, pierced at Golgotha, are now the hands of the enthroned High Priest whose ordination-work is permanently and completely done.</p>",
    "23": "<p>A type: blood applied to the right earlobe, right thumb, right big toe — consecrating hearing, work, and walk. Christ is the priest whose hearing was perfectly obedient (John 5:30), whose work was wholly dedicated (John 17:4), and whose walk was without sin (1 Pet 2:22). The blood-consecration of the three extremities is fully enacted in his perfect humanity.</p>",
    "24": "<p>A type: Aaron's sons receive the same blood application — the priestly order shares in the high priest's consecration. Those in Christ share in his consecration: &ldquo;you are a chosen race, a royal priesthood&rdquo; (1 Pet 2:9). The blood that constitutes Aaron's priestly access to YHWH is the same blood that constitutes the new covenant community as a priestly people.</p>",
    "25": "<p>A type: fat portions and bread joined in a single composite offering. Christ's self-offering encompasses his full humanity: body and soul, will and affection. He offers himself as both the sacrificial animal (his shed blood) and the bread of life (John 6:35). The composite ordination offering points to the comprehensive character of his self-gift.</p>",
    "26": "<p>A type: the three unleavened bread types placed on the fat portions. The unleavened character (no leaven = no sin) points to Christ as the one whose priestly service was untainted: &ldquo;holy, innocent, unstained&rdquo; (Heb 7:26). The loaves mixed with oil (Spirit-saturated) point to the Spirit-anointed character of his whole ministry.</p>",
    "27": "<p>A type: Moses waves the composite offering before YHWH. Christ is the wave offering presented before the Father and consecrated as the eternal High Priest. John 17:19: &ldquo;for their sake I consecrate myself, that they also may be sanctified in truth&rdquo; — the ordination wave offering logic, enacted in Christ's self-consecration for the sake of his priestly community.</p>",
    "28": "<p>A type: the entire ordination offering is burned — nothing reserved. The founding sacrifice of Christ's priesthood was total. His death was complete; the cup was not partially drunk (John 18:11). The uniqueness of the ordination as an unreserved burning marks the once-for-all character of Christ's founding sacrifice.</p>",
    "29": "<p>A type: Moses receives the wave-breast as the officiant's portion. In Christ's case there is no human officiant — the Father receives the entirety. Christ is both priest and offering (Heb 9:14), with no division between the one who offers and the one offered. His perfected priesthood is the Father's complete satisfaction.</p>",
    "30": "<p>A fulfillment: oil and blood mixed and sprinkled on the priests and their garments. Christ's work provides exactly this for those who are &ldquo;in him&rdquo;: the blood of propitiation (atonement secured) and the oil of the Spirit (consecration applied). 1 John 2:27: &ldquo;the anointing that you received from him abides in you&rdquo; — the Spirit's anointing is the permanent mark of those consecrated by Christ's blood.</p>",
    "31": "<p>A type: the ordination meal eaten at the tent entrance — the priestly community eats the meal of their consecration. Christ instituted the new covenant meal as the ordination feast of the new priestly community: &ldquo;Do this in remembrance of me&rdquo; (Luke 22:19). The Last Supper is the NT ordination meal — eaten at the threshold of the new covenant, sealing the community into its priestly identity.</p>",
    "32": "<p>A type: no leftovers — everything is either eaten or burned. Christ's body was not left in the grave — the resurrection is the sign that YHWH received the sacrifice without remainder (Acts 2:31: &ldquo;his flesh did not see corruption&rdquo;). The offering was complete, consumed, and accepted; nothing remained in the realm of death.</p>",
    "33": "<p>A type: seven days at the entrance — the liminal period of the new priestly order. The forty days of Christ's post-resurrection appearances (Acts 1:3) is the extended liminal period during which the new priestly order is established: the disciples receive the risen priest, are commissioned, and await the Spirit. The ordination period gives way to the active priestly ministry — the eighth day (ch. 9) / Pentecost.</p>",
    "34": "<p>A fulfillment: &ldquo;YHWH commanded this to be done, to make atonement for you.&rdquo; Christ's entire life of obedience — from incarnation through resurrection — is an atonement event. Heb 10:14: &ldquo;by a single offering he has perfected for all time those who are being sanctified&rdquo; — the ordination's atonement-language is fulfilled in the permanent, once-for-all character of what Christ accomplished.</p>",
    "35": "<p>A type: day and night at the tent entrance — the priestly vocation is total and continuous. Christ's intercession at the Father's right hand is unceasing: &ldquo;he always lives to make intercession for them&rdquo; (Heb 7:25). The seven-day vigil was temporary; Christ's priestly ministry is eternal — he &ldquo;holds his priesthood permanently, because he continues forever&rdquo; (Heb 7:24).</p>",
    "36": "<p>A fulfillment: &ldquo;Aaron and his sons did all the things that YHWH commanded by Moses.&rdquo; Christ's obedience was total: &ldquo;although he was a son, he learned obedience through what he suffered. And being made perfect, he became the source of eternal salvation&rdquo; (Heb 5:8-9). The ordination narrative ends with perfect compliance; Christ's life ends with the same: &ldquo;It is finished&rdquo; (John 19:30).</p>"
  },
  "9": {
    "1": "<p>A fulfillment: the eighth day — the day beyond the seven-day creation week, the first day of a new order. Christ rises on the first day of the week (John 20:1), the &ldquo;eighth day&rdquo; of the early church's calendar — the day of new creation inaugurating the new priestly order. The seven-day ordination confinement gives way to the eighth-day ministry; the burial-and-waiting gives way to the resurrection morning.</p>",
    "2": "<p>A fulfillment: Aaron offers for his own sin first. Heb 7:27 draws the explicit contrast: &ldquo;unlike those high priests, he has no need to offer sacrifices daily, first for his own sins and then for those of the people, since he did this once for all when he offered up himself.&rdquo; The Aaronic pattern (self-offering first) is the system's built-in acknowledgment of its own inadequacy. Christ bypasses this step — he has nothing to atone for in himself.</p>",
    "3": "<p>A type: a male goat for the people's sin offering. The goat as sin offering prefigures Christ as the one who &ldquo;bore the sin of many&rdquo; (Isa 53:12); John identifies him as the comprehensive sin-bearer: &ldquo;the Lamb of God, who takes away the sin of the world&rdquo; (John 1:29). Both Yom Kippur goats (Lev 16) — one killed, one sent away — find their fulfillment in Christ alone.</p>",
    "4": "<p>A type: &ldquo;today YHWH will appear to you&rdquo; — the promised theophany at the end of the sacrificial sequence. Christ's resurrection is the ultimate theophany-after-sacrifice: the Father's visible validation of the Son's completed offering. The cult's goal — divine presence — is achieved through sacrifice; Christ achieves it once for all (John 17:24).</p>",
    "5": "<p>A type: the congregation assembles to witness the first sacrificial service. The crowd at Golgotha (Luke 23:35: &ldquo;the people stood by, watching&rdquo;) witnessed the definitive sacrifice. The assembly at Pentecost (Acts 2:1-6) witnesses its validation — the theophanic fire of the Spirit at Pentecost is the NT counterpart to the divine fire of Lev 9:24.</p>",
    "6": "<p>A type: obedience to the prescription leads to the appearing of divine glory. Christ's perfect obedience to the Father's will (Luke 22:42: &ldquo;not my will, but yours, be done&rdquo;) was the path by which the Spirit was poured out and the glory of God made visible in the resurrection. Obedience and theophany are structurally linked in the Levitical system — and in Christ.</p>",
    "7": "<p>A type: &ldquo;draw near to the altar and offer&rdquo; — the command to approach. Christ needed no command from a mediator; he came willingly: &ldquo;I lay it down of my own accord. I have authority to lay it down, and I have authority to take it up again&rdquo; (John 10:18). The command-structure of the Levitical system (Moses commanding Aaron) is replaced by the Son's own initiative in perfect alignment with the Father's will.</p>",
    "8": "<p>A type: Aaron slaughters his sin offering with his own hand. Christ is simultaneously the priest who offers and the offering that is presented: &ldquo;through the eternal Spirit offered himself without blemish to God&rdquo; (Heb 9:14). The structural separation between priest and victim in Leviticus is collapsed in Christ, who is both the one who offers and the one offered.</p>",
    "9": "<p>A type: Aaron's sons bring the blood to him. Christ presents his own blood in the heavenly sanctuary with no intermediary: &ldquo;he entered once for all into the holy places, not by means of the blood of goats and calves but by means of his own blood, thus securing an eternal redemption&rdquo; (Heb 9:12). The slaughter-site-to-altar transport is overcome in Christ who is both sacrifice and presenting priest.</p>",
    "10": "<p>A type: fat portions burned for Aaron's personal sin offering. Christ had no personal sin offering — the critical point Hebrews makes (Heb 7:26-27). The Aaronic system's requirement that the high priest offer for himself before offering for the people is a structural limitation built in to signal the system's own inadequacy and to point toward the priest who needs no such provision.</p>",
    "11": "<p>A fulfillment: Aaron's sin offering burned outside the camp. Heb 13:12: &ldquo;so Jesus also suffered outside the gate in order to sanctify the people through his own blood.&rdquo; The burning outside the camp — removing the sin-bearing sacrifice completely from the community's midst — is enacted in Christ's crucifixion outside Jerusalem's walls.</p>",
    "12": "<p>A type: Aaron's burnt offering — total self-dedication in the priestly role. Christ's complete dedication to the Father's mission: &ldquo;he humbled himself by becoming obedient to the point of death, even death on a cross&rdquo; (Phil 2:8). The burnt offering has no human portion — it ascends entirely to YHWH; Christ's self-offering was wholly for the Father's glory and the people's salvation.</p>",
    "13": "<p>A type: Aaron's sons present the pieces of the burnt offering. The disciples' apostolic witness is the NT counterpart: &ldquo;you will be my witnesses in Jerusalem and in all Judea and Samaria, and to the end of the earth&rdquo; (Acts 1:8). The church does not re-sacrifice; it presents what was once sacrificed by bearing witness to the completed offering.</p>",
    "14": "<p>A type: the entrails and legs are washed before burning — every part pure. Christ's sacrifice was wholly pure: &ldquo;like that of a lamb without blemish or spot&rdquo; (1 Pet 1:19). There was no element of his offering that required cleansing. In bearing sin, he underwent the ultimate washing — the removal and destruction of sin through the cross, whose purity and sin-bearing are both absolute.</p>",
    "15": "<p>A fulfillment: Aaron presents the sin offering for the people — the priesthood's primary function. Christ's definitive enactment: &ldquo;when Christ had offered for all time a single sacrifice for sins, he sat down at the right hand of God&rdquo; (Heb 10:12). The Aaronic high priest presents the people's sin offering annually; Christ presents the once-for-all offering that requires no repetition.</p>",
    "16": "<p>A fulfillment: Aaron offers &ldquo;according to the rule&rdquo; (<em>kamishpat</em>). Christ fulfills every prescribed rule: &ldquo;I have not come to abolish the Law or the Prophets but to fulfill them&rdquo; (Matt 5:17). His priestly ministry is not an innovation but the perfect execution of every rule the system prescribed — executed at the level of reality rather than shadow (Heb 10:1).</p>",
    "17": "<p>A type: the grain offering added to the burnt offering. Christ is both the bread of life (John 6:35) and the sacrificed Lamb (John 1:29). His Eucharistic words at the Last Supper bring these together: &ldquo;this is my body&rdquo; (grain offering) and &ldquo;this is my blood of the covenant&rdquo; (sacrificial blood). The combined offering of Lev 9:17 is the type of the Eucharistic self-gift.</p>",
    "18": "<p>A type: the peace offerings for the people — the offering of reconciliation. Christ is our peace: &ldquo;since we have been justified by faith, we have peace with God through our Lord Jesus Christ&rdquo; (Rom 5:1; Eph 2:14: &ldquo;he himself is our peace&rdquo;). The peace offering's communion meal is fulfilled in the Lord's Supper: a participation in the reconciliation Christ enacted (1 Cor 10:16).</p>",
    "19": "<p>A type: the sons present the fat portions designated for YHWH. The church's role is not to sacrifice but to present: &ldquo;present your bodies as a living sacrifice&rdquo; (Rom 12:1). The community's participation in presenting the portions is now enacted in Spirit-led self-dedication in response to Christ's completed work.</p>",
    "20": "<p>A type: the fat on the breast — the divine portion covers the priestly portion. Christ's sacrifice encompasses both what he offers to the Father (the fat burned on the altar) and what he gives to his people (the breast eaten by the priests). His death is simultaneously the offering to the Father and the nourishment of the church.</p>",
    "21": "<p>A fulfillment: Aaron waves the breast and right thigh before YHWH — the wave offering enacts presentation-and-return. Christ's resurrection is the great wave offering: presented to the Father in death, received, and returned as the living Lord. &ldquo;Christ has been raised from the dead, the firstfruits of those who have fallen asleep&rdquo; (1 Cor 15:20) — the firstfruits waved before YHWH are the type; Christ's resurrection is the reality.</p>",
    "22": "<p>A fulfillment: Aaron lifts his hands toward the people and blesses them. Luke 24:50-51: &ldquo;lifting up his hands he blessed them. While he blessed them, he parted from them and was carried up into heaven.&rdquo; Christ's ascension is the ultimate Aaronic blessing — the High Priest performs the Num 6:24-26 benediction as he departs. Every spiritual blessing in the heavenly places is now poured out in him (Eph 1:3).</p>",
    "23": "<p>A fulfillment: Moses and Aaron enter the tent together; the glory of YHWH appears. The Pentecost event is the NT counterpart: the Spirit descends on the assembled disciples (Acts 2:1-4). The theophanic fire that validates Aaron's first sacrifice is the type; the tongues of fire at Pentecost are the fulfillment — the Father's confirmation that Christ's sacrifice has been accepted.</p>",
    "24": "<p>A fulfillment: divine fire consumes the sacrifice; the people shout and fall on their faces. The resurrection and Pentecost are the NT enactments: divine fire (the Spirit) validates the sacrifice (the cross); the crowd's response is both conviction and rejoicing. Acts 2:37: &ldquo;cut to the heart&rdquo; — the falling-on-their-faces response to the fire that validates the sacrifice. The fire of Lev 9:24 descends at Pentecost as the Spirit who empowers the church.</p>"
  },
  "10": {
    "1": "<p>A type: Nadab and Abihu offer unauthorized fire — approach to YHWH outside the appointed mediator brings judgment. Christ is the only authorized way of approach: &ldquo;I am the way, the truth, and the life. No one comes to the Father except through me&rdquo; (John 14:6). Those who reject the appointed high priest face the consuming fire rather than the blessing (Heb 10:26-29).</p>",
    "2": "<p>A type: fire from YHWH consumes the unauthorized offerers. The divine holiness that accepted the authorized sacrifice (9:24) now destroys those who bypass it. This is the wrath Christ absorbed in his own body for those who approach through him. &ldquo;Our God is a consuming fire&rdquo; (Heb 12:29) — those in Christ are not consumed because he absorbed the fire on their behalf.</p>",
    "3": "<p>A fulfillment: &ldquo;through those near me I will show myself holy.&rdquo; Christ is the one nearest the Father (John 1:18: &ldquo;at the Father's side&rdquo;) who is also perfectly holy. His holiness makes YHWH's holiness visible: &ldquo;Father, glorify your name&rdquo; (John 12:28). The cross is the supreme act through which the holy God is glorified before all the people.</p>",
    "4": "<p>A type: the bodies are removed outside the camp — judgment is expelled from the community's midst. Christ bears the judgment outside the gate (Heb 13:12) so that those within the covenant are not destroyed. The removal of the judged bodies enacts what the sin-offering outside the camp enacts: divine judgment is removed from the community through a representative who bears it away.</p>",
    "5": "<p>A type: the bodies are carried out in their priestly tunics — the office remains honorable even in judgment. Christ dies as the High Priest, in the fullness of his consecration, bearing the people's sins. His burial cloths (John 20:6-7, left folded in the tomb) testify to the completion of the priestly act — the priest laid aside his working garments because the work was fully done.</p>",
    "6": "<p>A type: Aaron must not mourn — the priestly vocation supersedes personal grief. Christ &ldquo;endured the cross, despising the shame&rdquo; (Heb 12:2), maintaining his priestly purposefulness in the face of death, not for his own consolation but for those he represented. He sustained his mission &ldquo;for the joy that was set before him&rdquo; — the priestly focus that transcends personal anguish.</p>",
    "7": "<p>A type: &ldquo;the anointing oil of YHWH is upon you&rdquo; — the consecration constrains the priest to remain at his post. Christ's anointing by the Spirit was a permanent commission that bound him to the mission until its completion. He did not descend from the cross (Matt 27:40-42) — the anointing kept him at his post, completing what could not be interrupted.</p>",
    "8": "<p>A fulfillment: YHWH speaks directly to Aaron — the only direct divine address to Aaron in Leviticus. In Christ, the Father speaks to humanity directly and definitively: &ldquo;in these last days he has spoken to us by his Son&rdquo; (Heb 1:2). The new covenant, inaugurated by Christ, is characterized by direct access: &ldquo;you have come to Jesus, the mediator of a new covenant&rdquo; (Heb 12:24).</p>",
    "9": "<p>A type: no wine or strong drink — the priest must maintain full cognitive clarity for holy ministry. At the crucifixion, Jesus refused the wine offered to dull his pain (Matt 27:34) — full consciousness was required for the atoning act. He would not have the boundary between holy and common blurred by compassionate sedation; he received wine only when the work was finished (John 19:30).</p>",
    "10": "<p>A type: &ldquo;distinguish (<em>lehavdil</em>) between the holy and the common.&rdquo; The verb <em>havdil</em> is the verb of creation (Gen 1:4) — the priest's distinguishing function mirrors the divine act of separating ordered reality from chaos. Christ is the ultimate distinction: in him, the holy God approaches the common world; through faith in him, the common is made holy (1 Cor 6:11: &ldquo;you were sanctified&hellip;in the name of the Lord Jesus Christ&rdquo;).</p>",
    "11": "<p>A fulfillment: the priest must teach the statutes. Christ is the ultimate Teacher whose priestly authority extends to definitive interpretation of YHWH's will: the Sermon on the Mount (Matt 5-7) is the climactic priestly-teaching act of the new covenant. &ldquo;You have heard that it was said&hellip; but I say to you&rdquo; — Christ teaches as the priest who not only knows the law but embodies it.</p>",
    "12": "<p>A fulfillment: eat the grain offering at the altar — the priestly meal of consecration. The Eucharist is the NT fulfillment: &ldquo;this is my body, which is given for you. Do this in remembrance of me&rdquo; (Luke 22:19). The grain offering eaten by the priest in the sanctuary becomes Christ's body received by the new covenant community in the Lord's Supper.</p>",
    "13": "<p>A type: &ldquo;it is your due and your sons' due&rdquo; — the priestly portion is both a right and a gracious provision. Believers' inheritance in Christ is both a right (Rom 8:17: &ldquo;heirs of God and fellow heirs with Christ&rdquo;) and pure grace (Eph 2:8-9). The priestly inheritance — a share in the sacrificial provisions — is the type of the believer's share in everything Christ has secured.</p>",
    "14": "<p>A type: the priestly meal eaten in any clean place — not restricted to the sanctuary precinct. The gospel is the new covenant priestly meal received anywhere in the world by any who have been made clean through Christ. The new covenant extends the priestly meal universally: &ldquo;Go therefore and make disciples of all nations&rdquo; (Matt 28:19).</p>",
    "15": "<p>A type: the wave offering always comes with the fat portions. In Christ, there is no separation between what belongs to God (the divine glory secured by the atonement) and what is given to his people (the priestly provision). His self-offering is simultaneously the glorification of the Father and the enrichment of the church: &ldquo;for their sake I consecrate myself, that they also may be sanctified&rdquo; (John 17:19).</p>",
    "16": "<p>A type: Moses seeks the sin offering goat with concern. Christ is the one who &ldquo;came to seek and to save the lost&rdquo; (Luke 19:10). The priestly zeal for proper completion of the atoning mechanism is fulfilled in Christ's relentless pursuit of those for whom his sacrifice was made: no sin offering is lost or burned without effect.</p>",
    "17": "<p>A fulfillment: eating the sin offering &ldquo;bears the iniquity of the congregation, to make atonement for them.&rdquo; This is Leviticus's most explicit statement of substitutionary mediation. Christ bears the iniquity of the many: &ldquo;he himself bore our sins in his body on the tree&rdquo; (1 Pet 2:24; Isa 53:11: &ldquo;he shall bear their iniquities&rdquo;). The eating-as-bearing in Lev 10:17 is the type; the incarnation-and-cross is the substance.</p>",
    "18": "<p>A type: blood not brought into the inner sanctuary means the flesh must be eaten in the outer court — outside. Christ's blood was shed outside Jerusalem (Golgotha), therefore his body is received in the world, by faith, outside the temple precinct. The gospel goes out to the world (Matt 28:19). The priestly meal is now available wherever the gospel is proclaimed and received (Matt 18:20).</p>",
    "19": "<p>A type: Aaron's explanation is accepted by Moses — the priestly judgment is received. The Father always accepts the Son's mediatorial judgment: &ldquo;I knew that you always hear me&rdquo; (John 11:42). Christ's priestly decisions are always accepted by the Father because he acts in perfect alignment with the Father's will. The pastoral discernment within the priestly system points forward to Christ's perfect and continuously accepted intercession.</p>",
    "20": "<p>A fulfillment: Moses heard and it was &ldquo;acceptable (<em>yitav</em>) in his sight.&rdquo; The Father is fully satisfied by Christ's atoning work — the NT doctrine of propitiation. Isa 53:11: &ldquo;he shall see the travail of his soul and be satisfied.&rdquo; The priestly account is in order; the work is done; the Father is pleased (Matt 3:17: &ldquo;this is my beloved Son, with whom I am well pleased&rdquo;).</p>"
  },
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
