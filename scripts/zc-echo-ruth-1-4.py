"""
Ruth + 1-2 Samuel — all four layers.
Ruth: kinsman-redeemer Boaz (type of Christ), Gentile inclusion in covenant community, genealogy to David/Christ.
1 Samuel: Samuel (prophet-judge-priest), Saul's failure, David's anointing, Spirit-empowered leadership.
2 Samuel: Davidic covenant (7:12-16), David's sin and restoration, Psalm 51 background.
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

# ============================
# RUTH
# ============================

RUTH_ECHO = {
  "1": {
    "16": [
      {"type": "allusion", "target": "John 10:16", "note": "Where you go I will go, and where you stay I will stay. Your people will be my people and your God my God — Ruth's covenant loyalty (hesed) to Naomi is the supreme expression of voluntary covenant commitment; her Gentile adoption into Israel's covenant community is a type of the Gentile church being grafted in"}
    ]
  },
  "2": {
    "20": [
      {"type": "allusion", "target": "Gal 3:13", "note": "The man is a close relative of ours, one of our guardian-redeemers — Boaz as kinsman-redeemer (go'el) is one of the OT's clearest types of Christ's redemptive work: a near kinsman who has the right and takes on the obligation to redeem the distressed family member; Christ redeems as the one who became our kinsman (incarnation) and paid our ransom (cross)"}
    ]
  },
  "3": {
    "9": [
      {"type": "allusion", "target": "Ezek 16:8", "note": "Ruth asks Boaz to 'spread your garment over your servant' — Hebrew <em>kānāp</em> (wing/hem), the same word Boaz used in 2:12 when blessing Ruth for sheltering under YHWH's wings. Ezek 16:8 uses identical language for YHWH's covenant with Israel: 'I spread the corner of my garment over you and you became mine.' Ruth's request asks Boaz to embody the divine wing-shelter he prayed she would receive; the goel's act is a human form of divine covenant love."},
      {"type": "type", "target": "Heb 2:17", "note": "Ruth invokes Boaz's <em>goel</em> status — he qualifies to redeem because he shares her people's kinship. This is the structural parallel Hebrews applies to Christ: he 'had to be made like his brothers in every respect, so that he might become a merciful and faithful high priest' and make propitiation for the people. The redeemer's qualification (kinship) mirrors the incarnation's purpose."}
    ],
    "12": [
      {"type": "shadow", "target": "Rom 8:3", "note": "Boaz acknowledges there is a nearer kinsman who has the prior legal claim and must be offered the right of redemption first. The nearer kinsman has the right but in ch 4 declines because it would jeopardize his own inheritance. Rom 8:3 — 'what the law could not do, weak as it was through the flesh, God did by sending his own Son' — reflects the same pattern: the law (nearer kinsman) has the prior claim but cannot carry out the redemption that restores the inheritance; grace (Boaz/Christ) then acts."}
    ],
    "15": [
      {"type": "shadow", "target": "Eph 1:13-14", "note": "Before the legal redemption is finalized, Boaz gives Ruth six measures of barley — a substantial pledge she carries back to Naomi. Eph 1:14 calls the Spirit 'the pledge of our inheritance until we acquire full possession of it.' Naomi's counsel 'stay still until you know how the matter will turn out' (v18) is the posture of those who have received the Spirit's earnest while awaiting the fullness of redemption (Rom 8:23)."}
    ]
  },
  "4": {
    "17": [
      {"type": "allusion", "target": "Matt 1:5", "note": "They named him Obed. He was the father of Jesse, the father of David — Ruth the Moabite is in the genealogical line of David and therefore of the Messiah (Matt 1:5); a Gentile woman's covenant loyalty becomes the vehicle for the Davidic line through which the Messiah comes; the Gentile inclusion in the covenant community is literal and genealogical"}
    ]
  }
}

RUTH_ORIGINAL = {
  "2": {
    "20": "<p><strong>qorov lanu ha-ish, mige-aleinu hu</strong>: 'The man is a close relative of ours, one of our redeemers.' The <em>go'el</em> (kinsman-redeemer) is a legal institution in Israelite law: a near male relative who has the right and duty to redeem a family member's sold land (Lev 25:25), to marry a brother's childless widow (Deut 25:5-10, levirate marriage), to redeem a relative sold into slavery (Lev 25:47-55), and to avenge the blood of a murdered kinsman (the <em>go'el hadam</em>). Boaz fulfills the first two functions. Paul in Galatians uses the redemption/buying-back vocabulary (<em>exagorazo</em>, 'redeemed from the curse of the law', Gal 3:13; 4:5) to describe Christ's work — the kinsman-redeemer framework is the legal-theological background for NT redemption language.</p>"
  }
}

RUTH_CONTEXT = {
  "1": {
    "1": "<p>Ruth is set in the period of the judges ('in the days when the judges ruled', Ruth 1:1) and is a counter-narrative to the chaos of that era: while Judges ends with 'everyone did what was right in his own eyes,' Ruth depicts a community where covenant loyalty (<em>hesed</em>) is practiced across ethnic lines and social classes. The book's theological center is the keyword <em>hesed</em> (steadfast love, covenant loyalty) — used three times (1:8; 2:20; 3:10). It serves as an introduction to the Davidic narrative: its genealogy (4:17-22) links it directly to 1 Samuel and the rise of David, making Ruth the backstory of the royal family. Matthew's genealogy (Matt 1:5) includes Ruth alongside Tamar, Rahab, and Bathsheba — four women with irregular stories through whom the messianic line runs.</p>"
  }
}

RUTH_CHRIST = {
  "2": {
    "20": "<p>A type: 'The man is a close relative of ours, one of our guardian-redeemers.' Boaz is the OT's most fully developed type of Christ as redeemer: (1) he is near of kin — Christ became our kinsman through the incarnation (Heb 2:14-15: he shared in flesh and blood that through death he might destroy him who has the power of death); (2) he has the right to redeem — as the sinless son of God, Christ alone qualifies; (3) he is willing to redeem — another go'el existed but declined (Ruth 4:6); Christ took on the obligation no one else could fulfill; (4) he pays the redemption price — Boaz redeems the land and takes Ruth; Christ redeems his people by his blood and takes them as his bride (Eph 5:25-27; Rev 19:7-9). The kinsman-redeemer motif is the book of Ruth's entire Christological contribution.</p>"
  }
}

# ============================
# 1 SAMUEL
# ============================

SAMUEL1_ECHO = {
  "2": {
    "1": [
      {"type": "allusion", "target": "Luke 1:46-55", "note": "Hannah's prayer: My heart exults in YHWH; my horn is exalted in YHWH — Mary's Magnificat (Luke 1:46-55) is a conscious echo and expansion of Hannah's prayer; both are songs of the lowly being lifted up, the proud being brought down, and the faithful YHWH-servant being vindicated through an unexpected birth"}
    ]
  },
  "3": {
    "1": [
      {"type": "allusion", "target": "Amos 8:11-12", "note": "The word of YHWH was rare in those days; there was no frequent vision — the period of prophetic silence before Samuel's emergence; Amos prophesies a future famine of hearing YHWH's word; both point to the darkness before divine speech resumes"}
    ]
  },
  "13": {
    "14": [
      {"type": "allusion", "target": "Acts 13:22", "note": "YHWH has sought out a man after his own heart — Paul in the Pisidian Antioch synagogue quotes this divine verdict on David to introduce the gospel: God raised up David as a witness, and from his offspring God has brought to Israel a Savior, Jesus, as he promised"}
    ]
  },
  "16": {
    "13": [
      {"type": "allusion", "target": "Matt 3:16", "note": "The Spirit of YHWH rushed upon David from that day forward — David's anointing by Samuel and the Spirit's coming upon him is the OT pattern for the messianic anointing; at Jesus's baptism the Spirit descends and remains (John 1:32), the permanent and ungrieved anointing that Saul's experience foreshadowed and forfeited"}
    ]
  }
}

SAMUEL1_ORIGINAL = {
  "2": {
    "2": "<p><strong>ein qadosh kaYHWH ki ein biltecha vein tzur kebogheinu</strong>: 'There is none holy like YHWH: for there is none besides you; there is no rock like our God.' Hannah's prayer is the OT's most concentrated statement of YHWH's incomparable holiness and sovereignty — expressed through the reversal-of-fortunes theme (vv. 4-8: the bows of the mighty are broken, but the feeble bind on strength). The pattern is: YHWH exalts the lowly and humbles the proud, not based on human merit but on divine grace and election. Paul's 'God chose what is weak in the world to shame the strong' (1 Cor 1:27) is the Christological application of Hannah's insight: the cross itself is YHWH's ultimate reversal, where the weak and crucified Son defeats the strong.</p>"
  }
}

SAMUEL1_CONTEXT = {
  "1": {
    "1": "<p>1 Samuel narrates the transition from the period of the judges to the monarchy (ca. 1100-1011 BCE). Its theological structure revolves around three figures: Samuel (the last and greatest judge, the transitional prophet-priest-judge), Saul (the failed king, rejected because of disobedience), and David (the man after God's own heart, the model for the Davidic covenant). The contrast between Saul and David is theologically instructive: Saul has the outward appearance (tall, handsome, from the right tribe) but lacks the inner heart-alignment; David lacks the outward qualifications (youngest, overlooked, a shepherd) but has the heart that YHWH seeks (1 Sam 16:7: YHWH looks on the heart). This contrast between external appearance and internal reality runs from 1 Samuel through Paul's theology of the Spirit vs. the flesh.</p>"
  }
}

SAMUEL1_CHRIST = {
  "16": {
    "13": "<p>A type: 'And the Spirit of the LORD rushed upon David from that day forward.' David's anointing by Samuel is the OT's paradigmatic messianic event — the word <em>mashiach</em> (anointed one) derives its ultimate meaning from this moment. David is anointed as YHWH's chosen king; the Spirit comes upon him as the empowering for his royal vocation. Jesus's baptism is the typological fulfillment: he is anointed (the meaning of <em>christos</em>, the Greek equivalent of <em>mashiach</em>) by the Spirit who descends and remains (John 1:32-33). The crucial difference: the Spirit rushed upon David from that day forward, but left Saul (1 Sam 16:14); on Jesus the Spirit descends and remains — the permanent anointing that makes him the Messiah whose Spirit-empowered rule will never end.</p>"
  }
}

# ============================
# 2 SAMUEL
# ============================

SAMUEL2_ECHO = {
  "7": {
    "12": [
      {"type": "fulfillment", "target": "Luke 1:32-33", "note": "I will raise up your offspring after you, who shall come from your body, and I will establish his kingdom — the Davidic covenant promise (Nathan's oracle) is directly cited in the annunciation: the Lord God will give him the throne of his father David, and he will reign over the house of Jacob forever, and of his kingdom there will be no end"},
      {"type": "fulfillment", "target": "Acts 2:30", "note": "God had sworn with an oath to him that he would set one of his descendants on his throne — Peter's Pentecost sermon cites the Davidic covenant (2 Sam 7 + Ps 16 + Ps 110) as the OT basis for Jesus's resurrection and exaltation; the resurrection is the fulfillment of the promise to raise up David's offspring"},
      {"type": "fulfillment", "target": "Rev 22:16", "note": "I am the root and the descendant of David — Revelation's final identification of Jesus as the Davidic heir fulfills the 2 Sam 7 promise in its full scope: not merely a political successor but the eternal Son who receives an eternal kingdom"}
    ],
    "14": [
      {"type": "fulfillment", "target": "Heb 1:5", "note": "I will be to him a father and he shall be to me a son — the father-son language of the Davidic covenant (2 Sam 7:14) is applied to Christ in Heb 1:5 as proof of his superiority to angels; no angel was ever called God's Son in this royal, covenantal sense"}
    ]
  }
}

SAMUEL2_ORIGINAL = {
  "7": {
    "12": "<p><strong>vakimoti et zarecha achareicha asher yetze mimeecha vehakhinoti et mamlaChto</strong>: 'I will raise up your offspring after you, who shall come from your body, and I will establish his kingdom.' The Davidic covenant (2 Sam 7:12-16) is the OT's central messianic text — the foundational oracle to which all subsequent messianic prophecy refers. Its key elements: (1) a son who builds a house (temple/dynasty); (2) a father-son relationship (<em>ani ehyeh lo le-av vehu yihyeh li le-ben</em>); (3) discipline for sin but not abandonment; (4) an eternal throne (<em>venekkon kisso ad olam</em>, I will establish his throne forever). The covenant applies both to the immediate heir Solomon and, in an escalating way, to the ultimate heir — which Psalms 2, 89, 110 and the prophets develop into the eschatological Messiah.</p>"
  }
}

SAMUEL2_CONTEXT = {
  "7": {
    "1": "<p>The Davidic covenant (2 Sam 7) is spoken through the prophet Nathan when David, having consolidated his kingdom in Jerusalem, desires to build a temple for YHWH. YHWH's reversal — 'you will not build me a house; I will build you a house (dynasty)' — is the pivot of the OT's messianic program. The word <em>bayit</em> (house) operates on three levels simultaneously: the physical temple David wants to build, the dynastic household YHWH promises, and the future son who will build both. The oracle has a near fulfillment (Solomon builds the temple, 1 Kings 6-8) and a far fulfillment (the eternal son whose kingdom has no end). The 'already and not yet' hermeneutic of NT fulfillment readings is modeled on 2 Samuel 7 itself, which already operates on two temporal levels.</p>"
  }
}

SAMUEL2_CHRIST = {
  "7": {
    "12": "<p>A direct revelation: 'When your days are fulfilled and you lie down with your fathers, I will raise up your offspring after you, who shall come from your body, and I will establish his kingdom ... and I will establish the throne of his kingdom forever.' The Davidic covenant is the OT's formal contract establishing the messianic expectation. Jesus of Nazareth's Davidic lineage is asserted by both Matthew (1:1-17) and Luke (3:23-38), confirmed by Paul (Rom 1:3: descended from David according to the flesh), and by Jesus himself (Mark 12:35-37). The eternal throne (v. 13, 16) is fulfilled in the resurrection: unlike David's physical descendants who all died, Christ rose and will reign forever. Peter's Pentecost sermon (Acts 2:29-36) explicitly applies 2 Sam 7 + Ps 16 + Ps 110 to the risen Christ: the Davidic covenant's promise of an unending throne is fulfilled not in an earthly dynasty but in the resurrection-life of the Son.</p>"
  }
}

def main():
    books = [
        ('ruth', RUTH_ECHO, RUTH_ORIGINAL, RUTH_CONTEXT, RUTH_CHRIST),
        ('1samuel', SAMUEL1_ECHO, SAMUEL1_ORIGINAL, SAMUEL1_CONTEXT, SAMUEL1_CHRIST),
        ('2samuel', SAMUEL2_ECHO, SAMUEL2_ORIGINAL, SAMUEL2_CONTEXT, SAMUEL2_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books:
        e = load_echo(book); merge_echo(e, echo_d); save_echo(book, e)
        c = load_comm('mkt-original', book); merge_comm(c, orig_d); save_comm('mkt-original', book, c)
        c = load_comm('mkt-context', book); merge_comm(c, ctx_d); save_comm('mkt-context', book, c)
        c = load_comm('mkt-christ', book); merge_comm(c, chr_d); save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
