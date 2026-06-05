"""
Echo layer — Luke chapter 1 (Prologue, annunciations, Magnificat, Benedictus)
Output: data/echoes/luke.json (creates file, adds ch1)

Key OT resonances:
- vv.5-25: barren-mother type (Sarah, Hannah); Nazarite vow (Num 6); Mal 4:5-6 (Elijah);
           Gabriel to Daniel (Dan 8-9)
- vv.26-38: Nathan's Davidic oracle (2 Sam 7); tabernacle-cloud overshadowing (Exod 40:35)
- vv.46-55: Magnificat modelled on Hannah's prayer (1 Sam 2:1-10) with Ps 103, 111, Isa 41
- vv.67-79: Benedictus draws on Ps 132, Mic 7:20, Gen 22, Mal 3:1, Isa 9:2, Mal 4:2
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
    "7": [
      {"type": "type", "target": "Gen 11:30", "note": "Sarah was barren; she had no children — the barren wife whose son becomes the covenant instrument is the governing type of Luke 1. Elizabeth recapitulates Sarah (barrenness, old age, divine opening of the womb) as the mother of the covenant forerunner, just as Sarah was the mother of the covenant heir."},
      {"type": "type", "target": "1 Sam 1:5-6", "note": "The LORD had closed Hannah's womb — Hannah is the closer parallel: like Elizabeth, she was the barren wife of a faithful Levitical husband, received a specific prophetic promise, and her miraculous son (Samuel) was set apart for God's service as a forerunner of the Davidic era. The Magnificat (vv.46-55) will explicitly model itself on Hannah's prayer."}
    ],
    "13": [
      {"type": "type", "target": "Judg 13:3-5", "note": "An angel appeared and said: You are barren and childless, but you are going to conceive and give birth to a son — the angel's announcement to Manoah's wife (Samson's mother) follows the same sequence as the announcement to Zechariah: barrenness stated, conception promised, son's name given, son's role declared, Nazarite consecration required. Luke presents John's annunciation as the fulfilment of this type."}
    ],
    "15": [
      {"type": "allusion", "target": "Num 6:3", "note": "He is never to take wine or other fermented drink — the Nazarite vow (Num 6:1-21) required abstention from all grape products as the outward mark of total consecration to YHWH. John is consecrated from the womb, as Samson was (Judg 13:4-5) and possibly Samuel (1 Sam 1:11 LXX). The vow marks him as wholly set apart, outside the normal channels of priestly or social life."},
      {"type": "allusion", "target": "Judg 13:4-5", "note": "Now see to it that you drink no wine or other fermented drink... because the boy is to be a Nazirite — the command to Samson's mother directly parallels the angel's word about John; both sons are Nazarites from the womb, consecrated to a particular divine mission before birth."}
    ],
    "17": [
      {"type": "fulfillment", "target": "Mal 4:5-6", "note": "See, I will send the prophet Elijah before that great and dreadful day of the LORD comes. He will turn the hearts of the parents to their children — Luke 1:17 is a near-verbatim echo of Mal 4:5-6, naming both the Elijah typology and the specific family-reconciliation mission. Malachi closes the OT canon with this promise; Luke opens the NT narrative with its fulfillment in John."},
      {"type": "allusion", "target": "Mal 3:1", "note": "I will send my messenger, who will prepare the way before me — the companion text to Mal 4:5-6; the messenger who prepares the way of the Lord is identified with the Elijah figure. John's mission (prepare the way) fuses both Malachi texts."}
    ],
    "19": [
      {"type": "allusion", "target": "Dan 8:16", "note": "I heard a human voice calling across the Ulai: Gabriel, tell this man the meaning of the vision — Gabriel is named in only two OT contexts: Dan 8:16 and Dan 9:21. Both are interpretive angelic appearances to Daniel in response to prayer, delivering eschatological revelation. Gabriel's appearance to Zechariah ('I stand in the presence of God') signals that this is an event of similar eschatological weight."},
      {"type": "allusion", "target": "Dan 9:21", "note": "Gabriel... came to me in swift flight about the time of the evening sacrifice — Daniel 9 is the closest structural parallel: Gabriel arrives at the time of the evening offering (exactly Zechariah's situation in the temple), responds to Daniel's prayer, and announces a seventy-weeks timetable for the coming of the anointed one. Luke's annunciation scene echoes this in setting, character, and eschatological content."}
    ],
    "25": [
      {"type": "allusion", "target": "Gen 30:23", "note": "God has taken away my disgrace — Rachel's identical declaration when Joseph was born, after years of barrenness and shame. Elizabeth's words are a conscious echo of Rachel's; both women experienced barrenness as public disgrace in an honor-shame culture where fertility was the primary measure of a wife's value, and both interpret the miraculous birth as divine removal of that shame."}
    ],
    "32": [
      {"type": "fulfillment", "target": "2 Sam 7:12-13", "note": "I will raise up your offspring to succeed you... and I will establish his throne forever — Nathan's oracle to David (the foundational Davidic covenant promise) is fulfilled in the annunciation: 'The Lord God will give him the throne of his father David, and he will reign over Jacob's descendants forever.' The eternal Davidic throne promised in 2 Sam 7 is explicitly applied to Jesus."},
      {"type": "allusion", "target": "Isa 9:6-7", "note": "Of the greatness of his government and peace there will be no end. He will reign on David's throne... forever — Isaiah's throne-promise (already cited by Matthew for Galilee) underpins the annunciation's royal language. 'Son of the Most High' and the eternal throne together invoke Isaiah's royal-Davidic prophecy."}
    ],
    "33": [
      {"type": "allusion", "target": "Dan 7:14", "note": "His dominion is an everlasting dominion that will not pass away, and his kingdom is one that will never be destroyed — Daniel's vision of the Son of Man receiving eternal kingship from the Ancient of Days provides the language of 'kingdom that will never end.' Luke's annunciation language fuses the Davidic covenant (2 Sam 7) with the Daniel 7 vision of eternal dominion."}
    ],
    "35": [
      {"type": "allusion", "target": "Exod 40:35", "note": "Moses could not enter the tent of meeting because the cloud had settled on it, and the glory of the LORD filled the tabernacle — the Greek episkiazō (overshadow) in Luke 1:35 is the same word the LXX uses in Exod 40:35 for the Shekinah cloud covering the tabernacle. Mary as the new tabernacle — the dwelling place of the divine presence — is the typological point: as the glory filled the tent, the Spirit comes upon Mary."},
      {"type": "allusion", "target": "Gen 1:2", "note": "The Spirit of God was hovering over the waters — the Spirit's creative activity at the first creation (ruach hovering over the formless void) is echoed in the Spirit 'coming upon' Mary for the new creation. The annunciation is a creation event: the Spirit who initiated the first creation initiates the new creation through the virginal conception."}
    ],
    "37": [
      {"type": "allusion", "target": "Gen 18:14", "note": "Is anything too hard for the LORD? — YHWH's response to Sarah's laughter about conceiving in old age is the verbal precedent for Gabriel's assurance to Mary: 'no word from God will ever fail.' The annunciation to Mary echoes the annunciation to Sarah; both women receive impossible birth promises, both receive divine assurance of God's power over biological impossibility."}
    ],
    "42": [
      {"type": "allusion", "target": "Judg 5:24", "note": "Most blessed of women is Jael, the wife of Heber the Kenite, most blessed of tent-dwelling women — Deborah's victory song declares Jael 'blessed among women' for delivering Israel from its enemy. Elizabeth's identical declaration over Mary situates Mary in the line of women through whom YHWH accomplished decisive salvific acts, but now for an even greater deliverance."},
      {"type": "allusion", "target": "Jdt 13:18", "note": "You are blessed by the Most High God above all women on earth — Judith is blessed 'above all women' after delivering Israel by killing Holofernes. The formula 'blessed among/above women' was attached to women who brought Israel salvation through divine enablement; Elizabeth applies it to the one carrying the ultimate salvation."}
    ],
    "46": [
      {"type": "type", "target": "1 Sam 2:1", "note": "My heart rejoices in the LORD; in the LORD my horn is lifted high — Hannah's prayer (1 Sam 2:1-10) is the structural model for the Magnificat. Both songs: open with the speaker's soul/heart exulting in God; move through divine reversals (low exalted, proud scattered, hungry filled, powerful brought down); ground the praise in God's covenant faithfulness; conclude with the Davidic promise. Mary's song is a typological realization of Hannah's."}
    ],
    "47": [
      {"type": "allusion", "target": "Hab 3:18", "note": "I will rejoice in the LORD, I will be joyful in God my Savior — Habakkuk's closing song of trust amid catastrophe uses identical language: 'my spirit rejoices in God my Savior.' Both are songs of joy grounded not in present circumstances but in divine character and covenant faithfulness."}
    ],
    "49": [
      {"type": "allusion", "target": "Ps 111:9", "note": "He provided redemption for his people; he ordained his covenant forever — holy and awesome is his name — the Psalm's declaration that YHWH's name is holy and awesome in the context of his covenant provision is echoed in Mary's 'holy is his name.' The Magnificat draws on the hymnic tradition of Ps 111 for its doxological affirmations."}
    ],
    "50": [
      {"type": "allusion", "target": "Ps 103:17", "note": "But from everlasting to everlasting the LORD's love is with those who fear him — the Psalm's statement that covenant mercy extends across generations to those who fear YHWH is the direct antecedent for 'his mercy extends to those who fear him, from generation to generation.' Mary's Magnificat integrates this psalmic covenant-mercy tradition."}
    ],
    "51": [
      {"type": "allusion", "target": "Ps 89:10", "note": "You crushed Rahab like one of the slain; with your strong arm you scattered your enemies — YHWH's mighty arm scattering his enemies is the Exodus-combat tradition preserved in Ps 89 and throughout the Psalter. Mary's 'he has performed mighty deeds with his arm' draws on this Exodus-power language, applying the divine warrior tradition to the coming salvation."}
    ],
    "52": [
      {"type": "allusion", "target": "1 Sam 2:7-8", "note": "The LORD sends poverty and wealth; he humbles and he exalts. He raises the poor from the dust and lifts the needy from the ash heap — Hannah's prayer articulates the same divine reversal that structures Mary's Magnificat: rulers brought down, humble lifted up. The Magnificat's social reversals are drawn directly from Hannah's vocabulary of YHWH's overturning of human power structures."}
    ],
    "53": [
      {"type": "allusion", "target": "1 Sam 2:5", "note": "Those who were full hire themselves out for food, but those who were hungry are hungry no more — Hannah's prayer provides the specific filled/hungry reversal that Mary echoes. The Magnificat's 'filled the hungry with good things but sent the rich away empty' is a near-quotation of Hannah's reversal-language, transposed from past tense (Hannah describing what God did) to aorist (Mary describing what God is doing)."}
    ],
    "54": [
      {"type": "allusion", "target": "Isa 41:8-9", "note": "But you, Israel, my servant, Jacob, whom I have chosen, you descendants of Abraham my friend — I took you from the ends of the earth... I said, You are my servant — Isaiah's servant-Israel language (the covenant language of election and sustained help) underlies 'he has helped his servant Israel.' The Magnificat situates the annunciation within Second Exodus theology: Israel as YHWH's servant being helped, now in its ultimate mode."}
    ],
    "55": [
      {"type": "allusion", "target": "Mic 7:20", "note": "You will be faithful to Jacob, and show love to Abraham, as you pledged on oath to our ancestors in days long ago — Micah's closing covenantal declaration (fidelity to Abraham and Jacob) is echoed in 'just as he promised our ancestors.' The Magnificat closes by grounding the annunciation in the Abrahamic covenant — the oldest layer of the divine promise that the entire narrative is fulfilling."}
    ],
    "59": [
      {"type": "allusion", "target": "Gen 17:12", "note": "Every male among you who is eight days old must be circumcised — the Abrahamic covenant's sign was circumcision on the eighth day (Gen 17:12; Lev 12:3). John's circumcision on the eighth day places his entry into the covenant community within the foundational Abrahamic rite. The naming occasion (culturally associated with circumcision) becomes the moment when the prophetic name overrides the family tradition."}
    ],
    "69": [
      {"type": "allusion", "target": "Ps 132:17", "note": "Here I will make a horn grow for David and set up a lamp for my anointed one — the 'horn of salvation in the house of his servant David' in the Benedictus draws on Ps 132:17, the covenantal psalm promising that YHWH will raise up a Davidic ruler from Zion. The horn (keren) is the standard OT symbol of military strength and royal power."},
      {"type": "allusion", "target": "1 Sam 2:10", "note": "He will give strength to his king and exalt the horn of his anointed — Hannah's prayer closes with the first occurrence of 'his anointed' (mashiach) in the OT, in the context of a horn being raised for the king. The Benedictus's 'horn of salvation' citation closes the loop: Hannah's prayer (which opened the messianic-king hope) is now being fulfilled in the forerunner's birth announcement."}
    ],
    "72": [
      {"type": "allusion", "target": "Gen 17:7", "note": "I will establish my covenant as an everlasting covenant between me and you and your descendants after you — the Abrahamic covenant as an 'everlasting covenant' is what Zechariah identifies as the theological ground for the coming salvation: 'to remember his holy covenant.' The entire redemptive movement is a covenant-memory event — YHWH fulfilling what he swore to Abraham."}
    ],
    "73": [
      {"type": "allusion", "target": "Gen 22:16-18", "note": "I swear by myself, declares the LORD, that because you have done this and have not withheld your son... I will surely bless you — the oath YHWH swore to Abraham after the binding of Isaac is the specific oath Zechariah identifies: 'the oath he swore to our father Abraham.' The most solemn Abrahamic oath (sworn at Moriah after Isaac's near-sacrifice) is the covenant basis the Benedictus invokes as now being fulfilled."}
    ],
    "76": [
      {"type": "fulfillment", "target": "Mal 3:1", "note": "I will send my messenger, who will prepare the way before me — Zechariah identifies John's role explicitly: 'you will go on before the Lord to prepare the way for him.' Mal 3:1 is the direct source. Combined with Mal 4:5-6 (already cited at v.17), the Benedictus grounds John's entire vocation in the Malachi forerunner texts that close the prophetic canon."},
      {"type": "fulfillment", "target": "Isa 40:3", "note": "A voice of one calling: In the wilderness prepare the way for the LORD — the second forerunner text: the herald in the desert preparing the road for YHWH's return to Zion. Zechariah's blessing applies both the Malachi and Isaianic forerunner traditions to John, as Luke will later confirm explicitly (3:4-6)."}
    ],
    "78": [
      {"type": "allusion", "target": "Mal 4:2", "note": "But for you who revere my name, the sun of righteousness will rise with healing in its rays — the 'rising sun' (anatole) that will come from heaven echoes Malachi's 'sun of righteousness rising with healing.' Both texts promise a dawn-figure bringing light and healing after a time of darkness and judgment. The Benedictus closes Zechariah's song by pointing to the coming dawn that John will announce."},
      {"type": "allusion", "target": "Num 24:17", "note": "A star will come out of Jacob; a scepter will rise out of Israel — Balaam's oracle of the rising star (used messianically in the Dead Sea Scrolls and by Matthew's Magi narrative) may also underlie the 'rising sun from heaven.' The anatole (rising, appearing) was used both for celestial and messianic-dawn imagery in Second Temple texts."}
    ],
    "79": [
      {"type": "allusion", "target": "Isa 9:2", "note": "The people walking in darkness have seen a great light; on those living in the land of deep darkness a light has dawned — Isaiah 9:2 is the direct source for 'shine on those living in darkness and in the shadow of death.' The Benedictus closes by pointing to the same Isaiah text that Matthew cited for the beginning of Jesus's Galilean ministry (Matt 4:16), establishing that the light Isaiah prophesied is the one John prepares."},
      {"type": "allusion", "target": "Ps 107:10-14", "note": "Some sat in darkness and the deepest gloom, prisoners suffering in iron chains... He brought them out of darkness and the deepest gloom and broke away their chains — the psalm of redemption from darkness and shadow of death uses the same paired imagery (darkness / shadow of death) that Zechariah applies to those awaiting the dawn. The Benedictus draws on the psalmic tradition of YHWH delivering from death-darkness."}
    ]
  }
}

def main():
    existing = load_echo('luke')
    merge_echo(existing, ECHOES)
    save_echo('luke', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Luke echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
