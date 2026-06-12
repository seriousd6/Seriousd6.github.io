"""
1-2 Chronicles + Ezra + Nehemiah + Esther — all four layers.
These books cover: return from exile, temple rebuilding, Davidic genealogy recapitulation,
Esther's providential rescue of the Jewish people (implicit theology).
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

CHRON1_ECHO = {
  "6": {
    "4": [
      {"type": "shadow", "target": "Heb 7:11", "note": "Eleazar to Phinehas — the Aaronic priestly succession traced here is the very lineage Hebrews addresses when asking whether perfection was attainable through the Levitical priesthood; the unbroken Aaronic line sets up the argument that a different priest after Melchizedek's order was needed."}
    ],
    "31": [
      {"type": "allusion", "target": "Rev 5:9", "note": "David appointed Levites over the service of song before the ark — the organized temple singers established here anticipate the heavenly choir of Revelation 5:9 singing a new song before the Lamb; the Chronicler's emphasis on worship music points forward to eternal worship."}
    ],
    "49": [
      {"type": "type", "target": "Heb 9:6-7", "note": "Aaron and his sons offering on the altar of burnt offering and the altar of incense — the Chronicler's summary of the Aaronic sacrificial ministry (burnt offering and incense) maps exactly onto what Hebrews 9:6-7 describes as the pattern the Levitical priests performed continuously, which Christ fulfills once for all as the high priest who passed through the greater and more perfect tent."},
      {"type": "allusion", "target": "Rev 8:3", "note": "The altar of incense (v49) maintained by Aaron's sons anticipates the golden altar of incense in Revelation 8:3-4, where an angel offers incense with the prayers of all the saints before God's throne — the OT incense ministry finding its eschatological completion."}
    ],
    "57": [
      {"type": "shadow", "target": "Heb 6:18", "note": "The cities of refuge assigned to Aaron's descendants — the institution of the city of refuge (a place where the inadvertent manslayer could flee and be safe from the avenger of blood) is the image behind Hebrews 6:18's 'we who have fled for refuge to lay hold of the hope set before us'; Christ is the ultimate city of refuge, the one to whom sinners flee and find safety from judgment."}
    ]
  },
  "17": {
    "13": [
      {"type": "fulfillment", "target": "Heb 1:5", "note": "I will be to him a father and he shall be to me a son — Chronicles repeats the Davidic covenant promise of 2 Sam 7:14; Hebrews cites it to establish Christ's superiority to angels as the eternal Son who holds the Davidic throne"}
    ]
  },
  "29": {
    "11": [
      {"type": "allusion", "target": "Matt 6:13", "note": "Yours O LORD is the greatness and the power and the glory and the victory and the majesty — David's prayer at the temple offering is the OT source behind the doxology appended to the Lord's Prayer in Matthew 6:13: For yours is the kingdom and the power and the glory forever"}
    ]
  }
}

CHRON1_ORIGINAL = {
  "1": {
    "1": "<p>1 Chronicles begins with nine chapters of genealogies (chs. 1-9) — from Adam to the post-exilic community. The genealogical prologue serves a theological purpose: to demonstrate the continuity of YHWH's covenant people through the Babylonian exile. The lists trace: Adam to Israel (ch. 1), the twelve tribes (chs. 2-9), with special focus on the line of David (ch. 3, which includes the post-exilic Davidic line down to the 6th generation after Zerubbabel — into the 5th century BCE). Matthew's genealogy (Matt 1:1-17) is a direct descendant of the Chronicler's method: beginning with Abraham, structured in three sets of fourteen, it traces the covenant line to the Messiah through the same Davidic focus that Chronicles establishes.</p>"
  }
}

CHRON1_CONTEXT = {
  "1": {
    "1": "<p>1-2 Chronicles was written to the post-exilic community (ca. 400-350 BCE) as a theological retelling of the monarchy. The Chronicler's perspective differs from Samuel-Kings: (1) he focuses almost exclusively on Judah and the Davidic line (the northern kingdom barely appears); (2) he omits many of David's failures (Bathsheba, Absalom) while including his worship and temple preparations; (3) he emphasizes the Levitical worship structure, the temple, and its proper celebration; (4) he ends on an upbeat note (Cyrus's decree, 2 Chr 36:22-23) rather than Kings' ambiguous ending (Jehoiachin's release). The Chronicler is writing a theology of hope for the restored community: YHWH's covenant with David is still in force; the temple worship is the proper center of life; the exile was judgment but not the end.</p>"
  }
}

CHRON1_CHRIST = {
  "17": {
    "14": "<p>A fulfillment: 'I will confirm him in my house and in my kingdom forever, and his throne shall be established forever.' Chronicles' retelling of the Davidic covenant (2 Sam 7) emphasizes its eternal dimension even more than the original: 'forever' appears three times in 17:12-14. The post-exilic community lived under Persian rule with no Davidic king on the throne — the eternal throne promise seemed broken. The NT's answer: the Davidic king now reigns from heaven (Acts 2:34-36: God has made him both Lord and Christ, this Jesus whom you crucified); the eternal throne is not a political throne in Jerusalem but the heavenly throne from which the risen Christ exercises his universal lordship. Chronicles' eschatological emphasis is fulfilled in Christ's resurrection-enthronement.</p>"
  }
}

CHRON2_ECHO = {
  "7": {
    "14": [
      {"type": "allusion", "target": "Jas 4:10", "note": "If my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin — the covenant principle at the temple dedication (2 Chr 7:14) is the OT's definitive statement of the prayer-of-repentance promise; James applies the same principle (Humble yourselves before the Lord and he will exalt you) in the new covenant context"}
    ]
  }
}

CHRON2_ORIGINAL = {
  "7": {
    "14": "<p><strong>veyikane'u ami asher nikra shemi aleihem veyitpallelu viyivakshu fanai viyashuvu midarkeihem hara'im vaani eshma min hashamayim veaeslach lechata'tam vearpeh et artzam</strong>: 'If my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land.' This verse contains the fourfold condition for covenant restoration: humble, pray, seek face, turn from evil. The promise has three parts: hear, forgive, heal. The verse became the central prayer-promise of post-exilic Israel and has been applied by successive generations as the conditions for revival. Its structure is Deuteronomic repentance theology at its most concentrated: the exile is reversible; covenant restoration is possible; the initiative is human repentance, the result is divine forgiveness.</p>"
  }
}

CHRON2_CONTEXT = {
  "36": {
    "22": "<p>2 Chronicles ends with Cyrus's decree (536 BCE) permitting the Jewish exiles to return and rebuild the temple — the same decree that opens Ezra. This ending was the Chronicler's editorial choice: rather than ending with Jerusalem's destruction (as Kings does), Chronicles ends with the first words of restoration. The last word of the Hebrew canon (as traditionally ordered) is this: 'Whoever is among you of all his people, may the LORD his God be with him. Let him go up.' The Chronicler makes the exile the penultimate chapter, not the final one; the return from exile is YHWH's faithfulness to his covenant promise. The NT reads the exile-and-return pattern as a type of death-and-resurrection: the people 'died' in Babylon and were 'raised' in the return; Christ dies and rises as the ultimate exile-and-return.</p>"
  }
}

CHRON2_CHRIST = {
  "36": {
    "23": "<p>A type: 'Thus says Cyrus king of Persia, The LORD, the God of heaven, has given me all the kingdoms of the earth, and he has charged me to build him a house at Jerusalem, which is in Judah. Whoever is among you of all his people, may the LORD his God be with him. Let him go up.' Cyrus's decree is Isaiah's prediction (Isa 44:28; 45:1-4 — naming Cyrus over a century before his birth) and Chronicles' fulfillment. Cyrus is called YHWH's 'anointed' (<em>meshicho</em>, Isa 45:1) — a Gentile king given the title used of the Davidic Messiah, showing that YHWH's sovereign purposes can work through unexpected agents. The pattern (a king's decree liberates an enslaved people to rebuild the temple) is the type for the NT's proclamation: the King of Kings' word liberates humanity from sin's exile to become the living temple of the Spirit (1 Cor 3:16-17).</p>"
  }
}

EZRA_ECHO = {
  "1": {
    "1": [
      {"type": "allusion", "target": "Luke 4:18", "note": "The LORD stirred up the spirit of Cyrus king of Persia — the fulfillment of Jeremiah's seventy-year prophecy through Cyrus's decree; Jesus's proclamation of liberty to captives (Isa 61:1, quoted in Luke 4:18) is the greater fulfillment: Christ proclaims the ultimate release from the ultimate exile (sin and death)"}
    ]
  },
  "3": {
    "11": [
      {"type": "allusion", "target": "Rev 4:8", "note": "They sang to YHWH: for he is good, for his steadfast love endures forever — the refrain sung at the temple foundation-laying; the same acclamation of YHWH's eternal goodness and love appears in Revelation's heavenly worship; the worship that began at the temple foundation continues eternally in the new creation temple"}
    ]
  }
}

EZRA_ORIGINAL = {
  "3": {
    "12": "<p>The elders who had seen the first temple wept when the second temple's foundation was laid — while the younger generation shouted for joy (Ezra 3:12). The mixture of weeping and rejoicing at the restoration point to the ambiguity of the return from exile: it was genuinely wonderful (YHWH's covenant faithfulness demonstrated) but genuinely less than the prophets had promised (the new temple was smaller and less glorious; the Davidic king was absent; the full restoration had not arrived). The prophets Haggai and Zechariah address this exact ambiguity: 'Who has despised the day of small things?' (Zech 4:10). The NT's answer is that the greater glory came not through a rebuilt temple but through the incarnation: the Word dwelling among us, the Shekinah glory in human form (John 1:14).</p>"
  }
}

EZRA_CONTEXT = {
  "1": {
    "1": "<p>Ezra narrates the return from Babylonian exile in two waves: the first under Zerubbabel (chs. 1-6, ca. 536-516 BCE, culminating in the temple's completion), and the second under Ezra the scribe (chs. 7-10, ca. 458 BCE). Ezra is a priestly figure who prioritizes the Torah — his mission is the reform of the community according to the law of Moses. His concern with mixed marriages (chs. 9-10) reflects the Deuteronomic prohibition of intermarriage with Canaanites (Deut 7:1-4) and the covenant community's identity boundaries. The return from exile should have been the full realization of the prophetic promises (Isa 40-66, Jer 31, Ezek 36-37), but the post-exilic community experienced only a partial restoration — which generated the eschatological hope for a greater future restoration that the NT identifies with the Messiah.</p>"
  }
}

EZRA_CHRIST = {
  "9": {
    "6": "<p>A shadow: 'O my God, I am ashamed and blush to lift my face to you, my God, for our iniquities have risen higher than our heads, and our guilt has mounted up to the heavens.' Ezra's prayer of corporate confession (Ezra 9:6-15) models the penitential posture of identifying with the community's sin even when personally innocent — the same posture that Daniel assumes in Dan 9 and Nehemiah in Neh 1. This is the OT's most developed example of representative intercession: a righteous individual taking on the burden of corporate guilt. Christ fulfills this to its ultimate degree: he who knew no sin was made sin for us (2 Cor 5:21); he prayed for his persecutors and bore the corporate sin-debt to the cross. Ezra's corporate repentance is the shadow; Christ's corporate sin-bearing is the substance.</p>"
  }
}

NEH_ECHO = {
  "8": {
    "8": [
      {"type": "allusion", "target": "Luke 24:45", "note": "They read from the book, from the Law of God, clearly, and they gave the sense, so that the people understood the reading — Ezra's public reading and explanation of the Torah is the OT model for the expository sermon; Jesus opened the disciples' minds to understand the Scriptures (Luke 24:45) in the same pattern: the text is read, its meaning explained, the people understand"}
    ]
  }
}

NEH_ORIGINAL = {
  "9": {
    "17": "<p>Nehemiah 9 is one of the OT's longest prayers — a historical survey from creation through the exodus, wilderness, conquest, judges, and exile, culminating in confession and petition. The prayer distills the Deuteronomic theology of the OT: YHWH is faithful and merciful; Israel repeatedly rebels; YHWH judges and then restores in mercy. The recurring phrase 'but you did not forsake them' (<em>ve-atah lo-azavtam</em>, v. 17, 19, 31) is the prayer's theological spine: YHWH's faithfulness to his covenant people despite their faithlessness is the basis for the current petition. Paul's statement 'but God demonstrates his own love for us in this: while we were still sinners, Christ died for us' (Rom 5:8) is the Nehemiah-9 theological pattern at its ultimate expression.</p>"
  }
}

NEH_CONTEXT = {
  "1": {
    "1": "<p>Nehemiah was the Jewish cupbearer to the Persian king Artaxerxes I (465-424 BCE) who received permission to return to Jerusalem and rebuild its walls (ca. 445 BCE). His memoirs (Neh 1-7 and parts of 11-13) are some of the most personal first-person narrative in the OT. The wall-building project (completed in 52 days, Neh 6:15) faced external opposition (Sanballat, Tobiah, Geshem) and internal socioeconomic problems (the poor were being exploited by the rich, ch. 5). Nehemiah's prayer-while-working pattern ('They who built the wall and those who carried burdens loaded themselves so that each labored on the work with one hand and held his weapon with the other', 4:17) became a model for Christian ministry combining spiritual and practical dimensions.</p>"
  }
}

NEH_CHRIST = {
  "9": {
    "38": "<p>A shadow: 'Because of all this we make a firm covenant in writing.' The community's covenant renewal at the end of Nehemiah 9 (written, sealed by the leaders, affirmed by the whole community) is the post-exilic attempt to re-enter the covenant relationship on the basis of the Mosaic law. Its failure is built in: the same generation that renewed the covenant (Neh 10) broke it within a generation (Neh 13: Sabbath violations, mixed marriages, Levites abandoned). Jeremiah's new covenant promise (Jer 31:31-34) is the response to this pattern: the problem with the Mosaic covenant is not the words but the hearts; no written covenant renewal can produce the internal transformation that is needed. Christ is the covenant-keeper in whom the law is fulfilled, and his Spirit is the power for covenant-faithfulness that Nehemiah's community lacked.</p>"
  }
}

ESTHER_ECHO = {
  "4": {
    "14": [
      {"type": "allusion", "target": "Acts 17:26-27", "note": "Who knows whether you have not come to the kingdom for such a time as this — Mordecai's appeal to Esther's providential position; God's sovereign ordering of human affairs and timing (though never named in the book) is the same providence Paul describes in Acts 17: God determined the times and boundaries of nations so that people might seek him and find him"}
    ]
  }
}

ESTHER_ORIGINAL = {
  "4": {
    "16": "<p><strong>kach kenos et kol hayehudim hanmitsa'im beShushan vetzumu alai ve'al tochlu ve'al tishtu shloses yamim layla vayhom</strong>: 'Go, gather all the Jews to be found in Susa, and hold a fast on my behalf, and do not eat or drink for three days, night or day.' Esther's three-day fast before entering the king's presence uninvited has been read as the book's implicit theological center: prayer (fasting was always associated with prayer) precedes the moment of potential death and the unexpected reversal. The three-day pattern (three days, then appearance before the king/enemy) resonates with the NT's three-day resurrection pattern — though this is a literary and structural echo rather than a direct typological prediction.</p>"
  }
}

ESTHER_CONTEXT = {
  "1": {
    "1": "<p>Esther is unique among OT books in never mentioning God — a deliberate literary choice that highlights the hiddenness of divine providence. The book is set in the Persian court of Ahasuerus (Xerxes I, ca. 483-473 BCE) and narrates the deliverance of the Jewish people from Haman's genocide. The Feast of Purim (chs. 9-10) celebrates this deliverance annually. The 'coincidences' of the narrative (the king cannot sleep and has the chronicles read to him just when Mordecai's unrewarded act is reached; Haman enters the court just as the king wants to honor Mordecai; Haman falls on Esther's couch at the exact moment the king returns) are the book's theological method: divine providence operates through the appearance of coincidence. Luther and others questioned its canonical status; Calvin rarely cited it; its canonical place has always been accepted in the Jewish tradition as the Purim festival's theological warrant.</p>"
  }
}

ESTHER_CHRIST = {
  "4": {
    "14": "<p>A type: 'Who knows whether you have not come to the kingdom for such a time as this?' Esther's providential placement as queen — a Jew in the Persian court at the moment her people face extermination — is one of the OT's clearest examples of divine providence operating through human circumstance. Her willingness to risk death to save her people ('if I perish, I perish', 4:16) is the type of Christ's redemptive mission: he came in the fullness of time (Gal 4:4) — the divine timing that Mordecai glimpses in Esther's story — and willingly went to death to save his people. The structural parallel: an intercessor enters the presence of the supreme authority uninvited, risking death, to plead for the life of the condemned people. Esther's mediation is temporal and partial; Christ's is eternal and complete.</p>"
  }
}

def main():
    books = [
        ('1chronicles', CHRON1_ECHO, CHRON1_ORIGINAL, CHRON1_CONTEXT, CHRON1_CHRIST),
        ('2chronicles', CHRON2_ECHO, CHRON2_ORIGINAL, CHRON2_CONTEXT, CHRON2_CHRIST),
        ('ezra', EZRA_ECHO, EZRA_ORIGINAL, EZRA_CONTEXT, EZRA_CHRIST),
        ('nehemiah', NEH_ECHO, NEH_ORIGINAL, NEH_CONTEXT, NEH_CHRIST),
        ('esther', ESTHER_ECHO, ESTHER_ORIGINAL, ESTHER_CONTEXT, ESTHER_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books:
        e = load_echo(book); merge_echo(e, echo_d); save_echo(book, e)
        c = load_comm('mkt-original', book); merge_comm(c, orig_d); save_comm('mkt-original', book, c)
        c = load_comm('mkt-context', book); merge_comm(c, ctx_d); save_comm('mkt-context', book, c)
        c = load_comm('mkt-christ', book); merge_comm(c, chr_d); save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
