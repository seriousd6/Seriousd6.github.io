"""
Echo Layer — Ezra chapters 4–7
Run: python3 scripts/zc-echo-ezra-4-7.py

Key echo connections in this range:
- 4:3: "You have no share with us" — the exclusion of syncretistic worshipers → John 4:22; Neh 2:20
- 4:5: Hired counselors to thwart God's work → Matt 28:12-13 (hired opposition to resurrection)
- 5:1: Haggai and Zechariah prophesy → Zech 4:6 (not by might but by Spirit)
- 5:5: "Eye of their God was on the elders" → Ps 34:15; Zech 4:10
- 6:19: Passover after exile → 1 Cor 5:7 (Christ our Passover sacrificed)
- 6:21: Separated from Gentile impurity to seek YHWH → Acts 2:41 (receive word, be baptized)
- 6:22: LORD turns the heart of the king → Prov 21:1
- 7:10: Study/practice/teach triad → 2 Tim 3:16-17; Matt 7:29
- 7:12: Artaxerxes "king of kings" → Rev 17:14; 19:16
- 7:27-28: Ezra's doxology; divine sovereignty over imperial heart → Rom 13:1
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
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

EZRA_ECHO_4_7 = {
  "4": {
    "3": [
      {"type": "allusion", "target": "Neh 2:20", "note": "Zerubbabel and the Israelite leaders tell the mixed-worship petitioners: &#8220;You have no share with us (<em>ʾên-lāḵem ḥēleq</em>) in building a house to our God; but we ourselves together will build to the LORD, the God of Israel, as King Cyrus... commanded us&#8221; — the exact formula Nehemiah will later use when Sanballat, Tobiah, and Geshem approach him: &#8220;you have no portion or right or memorial in Jerusalem&#8221; (Neh 2:20); the recurring exclusion of those whose worship is syncretistic from participation in the covenant community&#8217;s building project; Jesus similarly clarifies the boundaries of his community: &#8220;salvation is from the Jews&#8221; (John 4:22) — the covenant lineage of worship matters"},
      {"type": "allusion", "target": "John 4:22", "note": "The returned exiles&#8217; refusal of the Samaritans&#8217; offer to build with them — &#8220;you worship what you do not know; we worship what we know&#8221; (John 4:22) — is the NT equivalent of Ezra 4:3; Jesus acknowledges the distinction between genuine covenant worship and syncretistic practice, while also pointing to the coming universality: &#8220;a time is coming when you will worship the Father neither on this mountain nor in Jerusalem&#8221; (John 4:21); the exclusion of Ezra 4:3 is provisional, not final — the same Samaritans receive the gospel in Acts 8:5-8"}
    ],
    "5": [
      {"type": "allusion", "target": "Matt 28:12", "note": "The adversaries &#8220;hired counselors (<em>yōʿᵃṣîm</em> sōḵārîm) against them to thwart their plans throughout the reign of Cyrus&#8221; — paid opposition deployed to frustrate the covenant community&#8217;s building work; the exact parallel occurs at the resurrection: &#8220;the chief priests... gave the soldiers a large sum of money, telling them, &#8216;You are to say, His disciples came during the night and stole him away&#8217;&#8221; (Matt 28:12-13); paid opposition to suppress the evidence of divine work is the recurring instrument of the adversary&#8217;s strategy"}
    ],
    "24": [
      {"type": "allusion", "target": "Hag 1:2", "note": "&#8220;At that point the work on God&#8217;s house in Jerusalem stopped — and it remained halted until the second year of Darius king of Persia&#8221;; the halt in building is precisely what Haggai 1:2 describes from the people&#8217;s perspective: &#8220;the time has not come, the time to rebuild the LORD&#8217;s house&#8221; — the people have rationalized the delay; Haggai&#8217;s ministry begins at exactly the moment described here, and his prophetic provocation (1:7-11) breaks the sixteen-year paralysis that ended the Persian-authorized building effort"}
    ]
  },
  "5": {
    "1": [
      {"type": "allusion", "target": "Zech 4:6", "note": "&#8220;The prophets Haggai and Zechariah son of Iddo prophesied to the Jews in Judah and Jerusalem in the name of the God of Israel&#8221; — the dual prophetic stimulus that restarts the stalled temple project; Zechariah&#8217;s key oracle to Zerubbabel the builder is the theological center of the prophetic accompaniment: &#8220;Not by might, nor by power, but by my Spirit, says the LORD of hosts&#8221; (Zech 4:6); the divine Spirit working through the prophetic word — not human capability — is what makes impossible building projects possible; Acts 1:8 applies the same principle to the mission that the disciples found impossible without the Spirit"}
    ],
    "5": [
      {"type": "allusion", "target": "Ps 34:15", "note": "&#8220;The eye of their God (<em>ʿên ʾĕlāhᵉhôn</em>) was on the elders of the Jews, so the officials could not stop them until the report could go to Darius&#8221; — divine watchfulness creating space for legitimate inquiry rather than arbitrary suppression; Ps 34:15: &#8220;The eyes of the LORD are toward the righteous and his ears toward their cry&#8221;; the divine gaze on the building community is the protective sovereignty that delays hostile action long enough for truth to prevail; 1 Pet 3:12 applies this Psalm to the NT community under pressure"},
      {"type": "allusion", "target": "Zech 4:10", "note": "The single eye of God watching over the builders (&#8220;the eye of their God&#8221;) connects to Zechariah&#8217;s vision of the seven eyes on the stone laid before Joshua (Zech 3:9) and the seven eyes of YHWH &#8220;which range through the whole earth&#8221; (Zech 4:10) — the same prophetic context (Zechariah prophesied to this same community at this same time); the divine omniscience expressed as watchful gaze is central to Zechariah&#8217;s consolation of the post-exilic community; Rev 5:6 applies the seven eyes to the Lamb himself"}
    ]
  },
  "6": {
    "14": [
      {"type": "allusion", "target": "Isa 45:1", "note": "The temple is built and prospers &#8220;by decree of the God of Israel and by decree of Cyrus, Darius, and Artaxerxes king of Persia&#8221; — three successive Persian emperors serve YHWH&#8217;s temple-building purpose across three generations; this is the literal fulfillment of Isaiah&#8217;s prophecy that Cyrus would be YHWH&#8217;s shepherd and anointed (Isa 44:28; 45:1), now extended through his dynasty; the pagan empire as involuntary servant of the covenant community&#8217;s restoration is the pattern Paul sees behind Roman imperial order: &#8220;there is no authority except from God&#8221; (Rom 13:1)"}
    ],
    "19": [
      {"type": "type", "target": "1 Cor 5:7", "note": "The returned exiles keep the Passover on the 14th of the first month — the first Passover on covenant soil since the exile; the Passover meal simultaneously commemorates the Egyptian exodus and enacts the return from the Babylonian exile, making this Passover doubly a celebration of redemption; Paul&#8217;s declaration that &#8220;Christ, our Passover lamb, has been sacrificed&#8221; (1 Cor 5:7) identifies the Passover that Ezra&#8217;s community celebrates as the type of the ultimate sacrifice; the exile-and-return Passover is the clearest OT type of the death-and-resurrection Passover that Christ enacts"}
    ],
    "20": [
      {"type": "allusion", "target": "Heb 10:22", "note": "All the priests and Levites &#8220;had purified themselves; they were all ritually clean&#8221; — the comprehensive purity before the Passover sacrifice; the post-exilic community&#8217;s preparation for the Passover through ritual purity is the type of the NT community&#8217;s preparation through Christ&#8217;s cleansing: &#8220;having our hearts sprinkled to cleanse us from a guilty conscience and having our bodies washed with pure water, let us draw near to God with a sincere heart and with the full assurance that faith brings&#8221; (Heb 10:22); the ritual purification of Ezra 6:20 is fulfilled by the heart-purification of the new covenant"}
    ],
    "21": [
      {"type": "allusion", "target": "Acts 2:41", "note": "The returned exiles eat the Passover &#8220;along with all who had separated themselves from the impurity of the peoples of the land to seek the LORD, the God of Israel&#8221; — inclusion in the Passover feast extended to any who separated from idolatry and oriented themselves toward YHWH; the criterion is not ethnic origin but covenant orientation; Acts 2:41 describes the same inclusive-but-boundary-maintaining pattern: &#8220;those who accepted his message were baptized, and about three thousand were added to their number that day&#8221; — the addition to the covenant community is through reception of the word and separation from the old life, not through ethnicity"}
    ],
    "22": [
      {"type": "allusion", "target": "Prov 21:1", "note": "&#8220;The LORD had filled them with joy and had turned the heart of the king of Assyria to them, so that he supported them in the work on God&#8217;s house&#8221; — YHWH turns the king&#8217;s heart (the Artaxerxes identified here as &#8220;king of Assyria&#8221; by the Chronicler&#8217;s historical-theological typology, since Assyria = the empire that controlled the region) to support the community; Prov 21:1: &#8220;The king&#8217;s heart is a stream of water in the hand of the LORD; he turns it wherever he will&#8221;; the NT applies the same sovereignty: &#8220;there is no authority except that which God has established&#8221; (Rom 13:1)"}
    ]
  },
  "7": {
    "5": [
      {"type": "allusion", "target": "Heb 7:11", "note": "Ezra&#8217;s genealogy culminates in &#8220;Aaron the high priest&#8221; — the full priestly lineage from Aaron established across 16 generations; the author of Hebrews similarly traces the insufficiency of the Aaronic lineage: &#8220;if perfection could have been attained through the Levitical priesthood... why was there still need for another priest to come?&#8221; (Heb 7:11); Ezra represents the Aaronic priesthood at its most faithful — scribe, student, and teacher of the Torah — yet his mission to re-establish the law in Israel only partially succeeds; the permanent priesthood that Hebrews describes is not Aaronic but Melchizedekan (Ps 110:4; Heb 7:17)"}
    ],
    "10": [
      {"type": "allusion", "target": "2 Tim 3:16", "note": "&#8220;Ezra had devoted himself to studying the law of the LORD, practicing it, and teaching its statutes and ordinances in Israel&#8221; — the three-stage sequence: <em>liḏrōš</em> (study/seek), <em>laʿăśôṯ</em> (practice/do), <em>wᵉlᵉlammēḏ</em> (teach) — is the paradigmatic engagement with divine revelation; 2 Tim 3:16-17 uses the same triad structure for Scripture&#8217;s purpose: &#8220;teaching, rebuking, correcting and training in righteousness, so that the servant of God may be thoroughly equipped for every good work&#8221;; Ezra is the OT model for the &#8220;man of God&#8221; that 2 Tim 3:17 describes"},
      {"type": "allusion", "target": "Matt 7:29", "note": "Ezra&#8217;s threefold engagement — study, practice, teach — produces the paradigmatic teacher of the law; yet Jesus is distinguished from even the best teachers of the law: &#8220;he taught them as one who had authority, and not as their teachers of the law&#8221; (Matt 7:29); what distinguishes Christ from even Ezra&#8217;s model is that he speaks the word as its author, not merely its student — &#8220;you have heard it said... but I say to you&#8221; (Matt 5:21-22) is beyond anything Ezra could claim; Ezra points to the need for the one who does not merely transmit the Torah but is its embodied fulfillment (Matt 5:17)"}
    ],
    "12": [
      {"type": "allusion", "target": "Rev 19:16", "note": "Artaxerxes addresses himself as &#8220;king of kings (<em>melek malkayāʾ</em>)&#8221; — the Aramaic superlative claiming universal sovereignty used by Persian and Babylonian kings (Dan 2:37: &#8220;You are the king of kings; the God of heaven has given you the kingdom&#8221;); Revelation transfers the title definitively to Christ: &#8220;on his robe and on his thigh he has this name written: King of kings and Lord of lords&#8221; (Rev 19:16); every human &#8220;king of kings&#8221; is a temporary holder of a title that belongs to the one who lives forever and ever (Rev 4:9-10); the Persian king who uses the title to authorize Ezra&#8217;s mission is himself authorized by the one to whom the title ultimately belongs"}
    ],
    "27": [
      {"type": "allusion", "target": "Rom 13:1", "note": "Ezra&#8217;s spontaneous doxology upon receiving the imperial letter: &#8220;Blessed be the LORD, the God of our ancestors, who put this in the king&#8217;s heart — to honor the house of the LORD in Jerusalem&#8221; — the theological recognition that YHWH works through the heart of the pagan emperor to achieve his covenant purposes; Prov 21:1: &#8220;The king&#8217;s heart is in the hand of the LORD&#8221;; Rom 13:1: &#8220;the authorities that exist have been established by God&#8221;; Ezra&#8217;s doxology is the model for recognizing divine providence in unexpected sources of support — the surprise of grace coming through the empire&#8217;s bureaucracy rather than despite it"}
    ]
  }
}

def main():
    existing = load_echo('ezra')
    merge_echo(existing, EZRA_ECHO_4_7)
    save_echo('ezra', existing)
    print('Ezra 4-7 echo layer written.')

if __name__ == '__main__':
    main()
