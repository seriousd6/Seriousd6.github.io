"""
MKT Nehemiah chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-nehemiah-1-3.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L and M; "the LORD" in T. Consistent with
  the completed Ezra scripts (mkt-ezra-1-2.py, mkt-ezra-3-6.py, mkt-ezra-7-8.py).
- H430 (אֱלֹהִים): "God" throughout. "God of heaven" preserved as a fixed divine title
  in all three tiers — it is Nehemiah's characteristic address for God in prayer.
- H2617 (חֶסֶד): at 1:5. Rendered "steadfast love" in L and M; "covenant faithfulness" in T.
  The pairing "keeping covenant and steadfast love" (1:5) is a formula drawn from Deut 7:9
  and Dan 9:4 — T notes this intertextual weight.
- H1285 (בְּרִית, covenant): "covenant" throughout. In the prayer (1:5-9) it is the
  foundational Mosaic covenant whose curse/blessing structure Nehemiah invokes.
- H3027 (יָד, hand): "the hand of my God" / "good hand of my God" (2:8, 2:18) — the same
  Ezra motif for divine providential care. L/M keep "hand"; T expands the phrase's meaning
  without paraphrasing it away.
- H2388 (חָזַק, repair/strengthen): The primary verb of chapter 3. Rendered "repaired" in L
  and M (standard rendering for restoration of the wall). T uses "repaired" except where
  "rebuilt" or "restored" is more natural for a specific structure.
- 1:5 OT echo: The address "O LORD God of heaven, the great and awesome God who keeps
  covenant and steadfast love" echoes Deuteronomy 7:9 precisely. T surfaces this.
- 1:8-9 OT echo: Nehemiah quotes Moses' covenant threat (Lev 26:33 / Deut 28:64: "I will
  scatter you") and promise (Deut 30:2-5: "gather from the ends of heaven"). These are
  not loose allusions but near-verbatim covenant citations. T notes this.
- 2:2 "I was very afraid": honor-shame register. Persian court — displaying sadness before
  the king without permission could be interpreted as disrespect or even treasonous intent.
  T surfaces the danger of the moment.
- 2:4 "I prayed to the God of heaven": Nehemiah prays silently while the king waits for his
  answer. T captures the urgency and the hidden nature of the prayer.
- 2:8 "the king granted me what I asked, for the good hand of my God was upon me": The
  king's favor is theologically interpreted — the same motif as Ezra 7:6, 7:9.
- 3:5 "their nobles did not put their necks to the work of their lord": honor-shame dynamics
  — the Tekoite nobles refused communal labor, a pointed social observation in a text that
  celebrates communal effort. T surfaces this.
- 3:12 "Shallum and his daughters" repaired: women participating in construction is
  remarkable enough that the text explicitly notes it. T flags the significance.
- Chapter 3 structure: The repair register is a literary tour around the city — each
  community/guild is assigned a section, and the list creates a symbolic picture of all
  Israel working together. T honors the communal and theological significance.
- Aspect: Hebrew narrative past throughout (waw-consecutive imperfect). Chapter 3 uses
  the qal imperfect with waw-consecutive for each repair entry — narrative sequence.
- H5315 (נֶפֶשׁ), H7307 (רוּחַ): not significant in this passage.
"""

import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

NEHEMIAH = {
  "1": {
    "1": {
      "L": "The words of Nehemiah the son of Hacaliah. Now in the month of Chislev, in the twentieth year, as I was in Susa the capital,",
      "M": "The words of Nehemiah son of Hacaliah. In the month of Chislev, in the twentieth year, while I was at the citadel of Susa,",
      "T": "These are the words of Nehemiah son of Hacaliah. In the month of Chislev, in the twentieth year of Artaxerxes, I was at the citadel of Susa—far from Jerusalem."
    },
    "2": {
      "L": "Hanani, one of my brothers, came with certain men from Judah. And I asked them about the Jews who escaped, who had survived the exile, and about Jerusalem.",
      "M": "Hanani, one of my brothers, arrived with some men from Judah. I asked them about the Jewish remnant that had survived the exile and about Jerusalem.",
      "T": "Hanani, one of my kinsmen, arrived with a group of men from Judah. I asked them for news: how were the Jews who had survived the exile? What was the state of Jerusalem?"
    },
    "3": {
      "L": "And they said to me, 'The remnant there in the province who survived the captivity are in great trouble and shame. The wall of Jerusalem is broken down and its gates have been destroyed by fire.'",
      "M": "They replied, 'The survivors of the exile who are back in the province are in great misery and disgrace. The wall of Jerusalem is broken down, and its gates have been burned with fire.'",
      "T": "Their report was devastating: 'The survivors still there in the province are in terrible trouble and dishonor. The wall of Jerusalem lies in rubble. Its gates are ash.'"
    },
    "4": {
      "L": "As soon as I heard these words I sat down and wept and mourned for days, and I continued fasting and praying before the God of heaven.",
      "M": "When I heard these words, I sat down and wept. I mourned for days, fasting and praying before the God of heaven.",
      "T": "When I heard this, I sat down and wept. For days I mourned—fasting and praying before the God of heaven, unable to move past the ruin of the city that bore my people's name."
    },
    "5": {
      "L": "And I said, 'O LORD God of heaven, the great and awesome God who keeps covenant and steadfast love with those who love him and keep his commandments,",
      "M": "'O LORD, God of heaven, the great and awesome God who keeps his covenant and steadfast love with those who love him and obey his commandments:',",
      "T": "'O LORD, God of heaven—the great and awe-inspiring God who is faithful to his covenant, who shows steadfast love to all who love him and keep his commandments—' (this is the covenant formula of Deuteronomy 7:9, Moses' own words — Nehemiah addresses God by his covenant title):"
    },
    "6": {
      "L": "let your ear be attentive and your eyes open, to hear the prayer of your servant that I now pray before you day and night for the people of Israel your servants, confessing the sins of the people of Israel, which we have sinned against you. Even I and my father's house have sinned.",
      "M": "let your ear be attentive and your eyes open to hear the prayer of your servant that I now pray before you day and night for your servants, the people of Israel, confessing the sins that we Israelites have committed against you—I and my father's house included.",
      "T": "'Let your ear be bent low and your eyes be open to hear the prayer I bring before you day and night—for your servants, the people of Israel. I am confessing our sins: the sins Israel has committed against you. I include myself and my own family—we are not bystanders to this guilt.'"
    },
    "7": {
      "L": "We have acted very corruptly against you and have not kept the commandments, the statutes, and the rules that you commanded your servant Moses.",
      "M": "We have acted wickedly against you, failing to keep the commandments, statutes, and ordinances you gave your servant Moses.",
      "T": "'We have acted with open corruption before you. We did not keep the commandments, the statutes, or the ordinances you entrusted to your servant Moses.'"
    },
    "8": {
      "L": "Remember the word that you commanded your servant Moses: If you are unfaithful, I will scatter you among the peoples,",
      "M": "Remember the word you commanded your servant Moses: If you act unfaithfully, I will scatter you among the nations,",
      "T": "'Call to mind what you told your servant Moses: If you are faithless, I will scatter you among the nations—'"
    },
    "9": {
      "L": "but if you return to me and keep my commandments and do them, though your outcasts are in the uttermost parts of heaven, from there I will gather them and bring them to the place that I have chosen, to make my name dwell there.",
      "M": "but if you return to me and obey my commandments and keep them, then even if your exiles are at the far ends of the heavens, I will gather them from there and bring them to the place where I have chosen to make my name dwell.",
      "T": "'—but if you return to me and obey my commandments, I will gather you from the ends of the heavens—however scattered you may be—and bring you home to the place I have chosen as the dwelling of my name.' (Nehemiah cites Moses' covenant promise from Deuteronomy 30:2-5 as the legal basis of his petition.)"
    },
    "10": {
      "L": "They are your servants and your people, whom you have redeemed by your great power and by your strong hand.",
      "M": "They are your servants and your people, whom you redeemed by your great power and your mighty hand.",
      "T": "'These are your servants, your people—the ones you redeemed with your great power and your outstretched hand. The redemption stands; the obligation endures.'"
    },
    "11": {
      "L": "O Lord, let your ear be attentive to the prayer of your servant, and to the prayer of your servants who delight to fear your name, and give success to your servant today, and grant him mercy in the sight of this man.' Now I was cupbearer to the king.",
      "M": "O Lord, let your ear be attentive to the prayer of your servant and to the prayer of your servants who revere your name. Give success to your servant today, and grant him favor before this man.' Now I was cupbearer to the king.",
      "T": "'O Lord, hear the prayer of your servant—and the prayers of all who delight to honor your name. Grant your servant success today, and give him favor before this man.' The man was the king. I was his cupbearer."
    }
  },
  "2": {
    "1": {
      "L": "In the month of Nisan, in the twentieth year of King Artaxerxes, when wine was before him, I took up the wine and gave it to the king. Now I had not been sad in his presence before.",
      "M": "In the month of Nisan, in the twentieth year of King Artaxerxes, when wine was set before him, I took the wine and presented it to the king. I had never been downcast in his presence before.",
      "T": "Four months after Hanani's report, in the month of Nisan—still the twentieth year of Artaxerxes—I was at my post, presenting wine to the king. Until that day I had never let my grief show before him."
    },
    "2": {
      "L": "And the king said to me, 'Why is your face sad, seeing you are not sick? This is nothing but sadness of the heart.' Then I was very much afraid.",
      "M": "The king said to me, 'Why does your face look sad when you are not ill? This can only be sadness of heart.' I became very frightened.",
      "T": "The king looked at me and said: 'Why is your face sad? You are not sick. This is nothing other than grief of heart.' My fear was immediate and sharp—displaying sorrow before a Persian king without permission was no small thing."
    },
    "3": {
      "L": "I said to the king, 'Let the king live forever! Why should not my face be sad, when the city, the place of my fathers' graves, lies in ruins and its gates have been destroyed by fire?'",
      "M": "I said to the king, 'May the king live forever! How could my face not be sad, when the city where my ancestors are buried lies in ruins and its gates have been burned down?'",
      "T": "'Long live the king!' I said. 'How could I not be sad? The city where my fathers are buried lies in ruins, and its gates are nothing but ash.'"
    },
    "4": {
      "L": "Then the king said to me, 'What are you requesting?' So I prayed to the God of heaven.",
      "M": "The king asked me, 'What is it you want?' So I prayed to the God of heaven,",
      "T": "The king said, 'What are you asking for?' In the space of a breath I sent a prayer up to the God of heaven—"
    },
    "5": {
      "L": "and I said to the king, 'If it pleases the king, and if your servant has found favor in your sight, that you send me to Judah, to the city of my fathers' graves, that I may rebuild it.'",
      "M": "—and then said to the king, 'If it pleases the king, and if your servant has found favor in your sight, send me to Judah, to the city of my ancestors' tombs, so that I may rebuild it.'",
      "T": "—and then I answered him: 'If the king is pleased, and if I have found any favor in your sight, send me to Judah—to the city where my fathers are buried—so that I may rebuild it.'"
    },
    "6": {
      "L": "And the king said to me (the queen also sitting beside him), 'How long will your journey take, and when will you return?' So it pleased the king to send me, and I gave him a time.",
      "M": "The king, with the queen sitting beside him, asked me, 'How long will your journey be, and when will you return?' So the king was pleased to let me go, and I gave him a specific time.",
      "T": "The king—the queen was seated beside him—asked: 'How long will the journey take, and when will you be back?' I gave him a time, and the king was pleased to let me go."
    },
    "7": {
      "L": "And I said to the king, 'If it pleases the king, let letters be given me to the governors of the province Beyond the River, that they may let me pass through until I come to Judah,",
      "M": "I also said to the king, 'If the king is willing, let letters be given to the governors of Trans-Euphrates so that they will allow me safe passage until I reach Judah,",
      "T": "I pressed the advantage: 'If the king is willing, let me have letters to the governors of Trans-Euphrates, authorizing safe passage through the region until I reach Judah,'"
    },
    "8": {
      "L": "and a letter to Asaph, keeper of the king's forest, that he may give me timber to make beams for the gates of the fortress that is by the temple, and for the wall of the city, and for the house that I shall occupy.' And the king granted me what I asked, for the good hand of my God was upon me.",
      "M": "and a letter to Asaph, keeper of the king's forest, that he may supply me with timber for the beams of the gates of the temple fortress, for the city wall, and for the house I will live in.' The king granted me everything I asked, for the good hand of my God was upon me.",
      "T": "'—and a letter to Asaph the keeper of the royal forest, authorizing timber for the beams of the temple gateway, the city wall, and my own residence.' The king gave me everything I requested. The good hand of my God was upon me."
    },
    "9": {
      "L": "Then I came to the governors of the province Beyond the River and gave them the king's letters. Now the king had sent with me officers of the army and cavalry.",
      "M": "I went to the governors of Trans-Euphrates and presented the king's letters to them. The king had also sent army officers and cavalry with me.",
      "T": "I traveled to the governors of Trans-Euphrates and delivered the king's letters. Artaxerxes had also provided me with an escort of army officers and cavalry—the military protection that Ezra had declined."
    },
    "10": {
      "L": "But when Sanballat the Horonite and Tobiah the Ammonite servant heard this, it displeased them greatly that someone had come to seek the welfare of the people of Israel.",
      "M": "When Sanballat the Horonite and Tobiah the Ammonite official heard this, they were greatly displeased that someone had come to promote the welfare of Israel.",
      "T": "When Sanballat the Horonite and Tobiah the Ammonite official learned of my mission, they were deeply disturbed that someone had come to advance the welfare of Israel's people."
    },
    "11": {
      "L": "So I came to Jerusalem and was there three days.",
      "M": "I arrived in Jerusalem and rested there three days.",
      "T": "I arrived in Jerusalem and spent three days in silence, gathering myself before doing anything."
    },
    "12": {
      "L": "Then I arose in the night, I and a few men with me. And I told no one what my God had put into my heart to do for Jerusalem. There was no animal with me but the one on which I rode.",
      "M": "Then I got up in the night, I and a few men with me. I had not told anyone what my God had put in my heart to do for Jerusalem. The only animal with me was the one I was riding.",
      "T": "Late at night I slipped out—just myself and a small group. I had told no one what God had placed in my heart to do for Jerusalem. The only animal was the one I was riding."
    },
    "13": {
      "L": "I went out by night through the Valley Gate past the Dragon Spring to the Dung Gate, and I inspected the walls of Jerusalem that were broken down and its gates that had been consumed by fire.",
      "M": "I went out by night through the Valley Gate, past the Dragon Spring, to the Dung Gate, inspecting the walls of Jerusalem that had been broken down and its gates that had been burned.",
      "T": "I went out through the Valley Gate, skirted past the Dragon Spring, and continued to the Dung Gate, surveying the broken stretches of wall and the burned-out gate openings in the dark."
    },
    "14": {
      "L": "Then I passed on to the Fountain Gate and to the King's Pool, but there was no place for the animal that was under me to pass.",
      "M": "I moved on to the Fountain Gate and the King's Pool, but there was no room for the animal under me to get through.",
      "T": "I pressed on to the Fountain Gate and the King's Pool—but the rubble was so dense that my mount could not get through."
    },
    "15": {
      "L": "Then I went up in the night along the valley and inspected the wall, and I turned back and entered through the Valley Gate, and so returned.",
      "M": "So I went up through the valley by night and examined the wall; then I turned back and reentered through the Valley Gate, returning the way I had come.",
      "T": "I climbed up through the ravine in the dark, examined the remaining wall, then doubled back and returned through the Valley Gate to complete the circuit."
    },
    "16": {
      "L": "And the officials did not know where I had gone or what I was doing, and I had not yet told the Jews, the priests, the nobles, the officials, and the rest who were to do the work.",
      "M": "The officials had no idea where I had gone or what I was doing, for I had not yet said anything to the Jews, the priests, the nobles, the officials, or any of the others who would be doing the work.",
      "T": "No official knew where I had gone or what I was planning. I had said nothing yet to the Jewish community—no priests, no nobles, no officials, none of the workers. The reconnaissance was mine alone."
    },
    "17": {
      "L": "Then I said to them, 'You see the trouble we are in, how Jerusalem lies in ruins with its gates burned. Come, let us build the wall of Jerusalem, that we may no longer be a reproach.'",
      "M": "Then I said to them, 'You see the distress we are in—how Jerusalem lies in ruins with its gates burned. Come, let us rebuild the wall of Jerusalem so that we will no longer be a disgrace.'",
      "T": "Then I called them together and said it plainly: 'You see what we are—Jerusalem is ruins and its gates are ash, and we are the shame of the nations. Come. Let us build the wall and end our disgrace.'"
    },
    "18": {
      "L": "And I told them of the hand of my God that had been upon me for good, and also of the words that the king had spoken to me. And they said, 'Let us rise up and build.' So they strengthened their hands for the good work.",
      "M": "I also told them how the good hand of my God had been upon me and what the king had said to me. They replied, 'Let us rise up and build.' And they resolved to undertake the good work.",
      "T": "I told them how the hand of God had been on me through the whole journey—and what the king had said and done. 'Let us rise up and build,' they said. And with those words, they committed themselves to the good work."
    },
    "19": {
      "L": "But when Sanballat the Horonite and Tobiah the Ammonite servant and Geshem the Arab heard of it, they mocked us and despised us and said, 'What is this thing that you are doing? Are you rebelling against the king?'",
      "M": "When Sanballat the Horonite, Tobiah the Ammonite official, and Geshem the Arab heard of it, they mocked and ridiculed us, saying, 'What is this thing you are doing? Are you rebelling against the king?'",
      "T": "When Sanballat the Horonite, Tobiah the Ammonite, and Geshem the Arab heard about it, they laughed us to scorn. 'What is this project you're mounting?' they taunted. 'Are you rebelling against the king?'"
    },
    "20": {
      "L": "Then I replied to them, 'The God of heaven will make us prosper, and we his servants will arise and build, but you have no portion or right or claim in Jerusalem.'",
      "M": "I answered them, 'The God of heaven will give us success. We, his servants, will rise and build. But you have no share, no right, and no stake in Jerusalem.'",
      "T": "I gave them a direct answer: 'The God of heaven will prosper us. We—his servants—will rise and build. But you: you have no share in this, no ancestral right, no standing in Jerusalem. None.'"
    }
  },
  "3": {
    "1": {
      "L": "Then Eliashib the high priest arose with his brothers the priests, and they built the Sheep Gate. They consecrated it and set up its doors. They consecrated it as far as the Tower of the Hundred, as far as the Tower of Hananel.",
      "M": "Then Eliashib the high priest and his fellow priests set to work and rebuilt the Sheep Gate. They dedicated it and hung its doors, and they dedicated it as far as the Tower of the Hundred and as far as the Tower of Hananel.",
      "T": "Eliashib the high priest led the way—he and his fellow priests rose up and rebuilt the Sheep Gate. They consecrated it and hung its doors, setting apart the section as far as the Tower of the Hundred and the Tower of Hananel. The priests began, and what they built they made holy."
    },
    "2": {
      "L": "And next to him the men of Jericho built. And next to them Zaccur the son of Imri built.",
      "M": "Next to him the men of Jericho built; and next to them Zaccur son of Imri built.",
      "T": "Next to them the men of Jericho took up their section; and next to the Jerichoans, Zaccur son of Imri."
    },
    "3": {
      "L": "The sons of Hassenaah built the Fish Gate. They laid its beams and set up its doors, its bolts, and its bars.",
      "M": "The sons of Hassenaah built the Fish Gate, laying its beams and hanging its doors with bolts and bars.",
      "T": "The sons of Hassenaah rebuilt the Fish Gate—laying the beams, hanging the doors, fitting the bolts and bars."
    },
    "4": {
      "L": "And next to them Meremoth the son of Urijah, son of Koz, repaired. And next to them Meshullam the son of Berechiah, son of Meshezabel, repaired. And next to them Zadok the son of Baana repaired.",
      "M": "Next to them Meremoth son of Uriah, son of Hakkoz, made repairs; and next to him Meshullam son of Berechiah, son of Meshezabel, made repairs; and next to him Zadok son of Baana made repairs.",
      "T": "Next: Meremoth son of Uriah, son of Hakkoz. Next: Meshullam son of Berechiah, son of Meshezabel. Next: Zadok son of Baana."
    },
    "5": {
      "L": "And next to them the Tekoites repaired, but their nobles did not put their necks to the work of their Lord.",
      "M": "Next to them the Tekoites made repairs, though their nobles would not put their shoulders to the work of their supervisors.",
      "T": "Next to them the Tekoites repaired—but the Tekoite nobles refused to stoop to the work. They would not put their necks to the service of their Lord. The common people worked; the elite stood apart."
    },
    "6": {
      "L": "And Joiada the son of Paseah and Meshullam the son of Besodeiah repaired the Jeshanah Gate. They laid its beams and set up its doors, its bolts, and its bars.",
      "M": "Joiada son of Paseah and Meshullam son of Besodeiah repaired the Jeshanah Gate, laying its beams and hanging its doors with bolts and bars.",
      "T": "Joiada son of Paseah and Meshullam son of Besodeiah repaired the Old Gate—laying beams, hanging doors, fitting bolts and bars."
    },
    "7": {
      "L": "And next to them repaired Melatiah the Gibeonite and Jadon the Meronothite, the men of Gibeon and of Mizpah, to the seat of the governor of the province Beyond the River.",
      "M": "Next to them Melatiah the Gibeonite and Jadon the Meronothite, men of Gibeon and Mizpah, made repairs up to the official residence of the governor of Trans-Euphrates.",
      "T": "Next: Melatiah the Gibeonite and Jadon the Meronothite, representing the men of Gibeon and Mizpah—working up to the seat of the Trans-Euphrates governor."
    },
    "8": {
      "L": "Next to him Uzziel the son of Harhaiah, goldsmiths, repaired. Next to him Hananiah, one of the perfumers, repaired. And they restored Jerusalem as far as the Broad Wall.",
      "M": "Next to him Uzziel son of Harhaiah, one of the goldsmiths, made repairs; and next to him Hananiah, one of the perfumers, made repairs. They restored Jerusalem as far as the Broad Wall.",
      "T": "Next: Uzziel son of Harhaiah of the goldsmiths' guild. Next: Hananiah of the perfumers. They restored the stretch all the way to the Broad Wall."
    },
    "9": {
      "L": "And next to them Rephaiah the son of Hur, ruler of half the district of Jerusalem, repaired.",
      "M": "Next to them Rephaiah son of Hur, ruler of a half-district of Jerusalem, made repairs.",
      "T": "Next: Rephaiah son of Hur, governor of a half-district of Jerusalem."
    },
    "10": {
      "L": "Next to them Jedaiah the son of Harumaph repaired opposite his house. And next to him Hattush the son of Hashabniah repaired.",
      "M": "Next to him Jedaiah son of Harumaph made repairs opposite his own house; and next to him Hattush son of Hashabniah made repairs.",
      "T": "Next: Jedaiah son of Harumaph—he repaired the section directly opposite his own house. Next: Hattush son of Hashabniah."
    },
    "11": {
      "L": "Malchijah the son of Harim and Hasshub the son of Pahath-moab repaired another section and the Tower of the Ovens.",
      "M": "Malchijah son of Harim and Hasshub son of Pahath-moab repaired another section, including the Tower of the Ovens.",
      "T": "Malchijah son of Harim and Hasshub son of Pahath-moab took on another section, including the Tower of the Ovens."
    },
    "12": {
      "L": "And next to him Shallum the son of Hallohesh, ruler of half the district of Jerusalem, repaired, he and his daughters.",
      "M": "Next to him Shallum son of Hallohesh, ruler of a half-district of Jerusalem, made repairs—he and his daughters.",
      "T": "Next: Shallum son of Hallohesh, governor of a half-district of Jerusalem—and his daughters worked alongside him. The text singles them out: women building the city wall."
    },
    "13": {
      "L": "Hanun and the inhabitants of Zanoah repaired the Valley Gate. They rebuilt it and set up its doors, its bolts, and its bars, and they repaired a thousand cubits of the wall, as far as the Dung Gate.",
      "M": "Hanun and the residents of Zanoah repaired the Valley Gate. They rebuilt it and hung its doors with bolts and bars, and they also repaired a thousand cubits of wall as far as the Dung Gate.",
      "T": "Hanun and the residents of Zanoah repaired the Valley Gate—hanging its doors, fitting bolts and bars—and also restored a thousand cubits of wall all the way to the Dung Gate."
    },
    "14": {
      "L": "Malchijah the son of Rechab, ruler of the district of Beth-haccherem, repaired the Dung Gate. He rebuilt it and set up its doors, its bolts, and its bars.",
      "M": "Malchijah son of Rechab, ruler of the district of Beth-haccherem, repaired the Dung Gate. He rebuilt it and hung its doors with bolts and bars.",
      "T": "Malchijah son of Rechab, governor of the Beth-haccherem district, repaired the Dung Gate—rebuilding it and hanging its doors with bolts and bars."
    },
    "15": {
      "L": "And Shallun the son of Col-hozeh, ruler of the district of Mizpah, repaired the Fountain Gate. He rebuilt it and covered it and set up its doors, its bolts, and its bars. He also repaired the wall of the Pool of Shelah of the king's garden, as far as the stairs that go down from the City of David.",
      "M": "Shallun son of Col-hozeh, ruler of the district of Mizpah, repaired the Fountain Gate. He rebuilt and roofed it and hung its doors with bolts and bars. He also repaired the wall of the Pool of Siloam near the king's garden, as far as the steps going down from the City of David.",
      "T": "Shallun son of Col-hozeh, governor of the Mizpah district, repaired the Fountain Gate—rebuilding, roofing, and fitting it with doors, bolts, and bars. He also restored the wall of the Siloam Pool beside the king's garden, extending to the steps that descend from the City of David."
    },
    "16": {
      "L": "After him Nehemiah the son of Azbuk, ruler of half the district of Beth-zur, repaired to a point opposite the tombs of David, and to the artificial pool, and to the house of the mighty men.",
      "M": "After him Nehemiah son of Azbuk, ruler of a half-district of Beth-zur, made repairs as far as a point opposite the tombs of David, to the man-made pool, and to the house of the warriors.",
      "T": "After him, Nehemiah son of Azbuk—governor of a half-district of Beth-zur—repaired as far as the tombs of David, the artificial pool, and the house of the warriors."
    },
    "17": {
      "L": "After him the Levites repaired: Rehum the son of Bani. Next to him Hashabiah, ruler of half the district of Keilah, repaired for his district.",
      "M": "After him the Levites made repairs: Rehum son of Bani. Next to him Hashabiah, ruler of a half-district of Keilah, made repairs for his district.",
      "T": "After him, the Levites took their section: Rehum son of Bani. Next: Hashabiah, governor of a half-district of Keilah, repairing the stretch assigned to his territory."
    },
    "18": {
      "L": "After him their brothers repaired: Bavvai the son of Henadad, ruler of half the district of Keilah.",
      "M": "After him their fellow Levites made repairs: Bavvai son of Henadad, ruler of a half-district of Keilah.",
      "T": "After him their Levitical kinsmen: Bavvai son of Henadad, governor of the other half-district of Keilah."
    },
    "19": {
      "L": "And next to him Ezer the son of Jeshua, ruler of Mizpah, repaired another section, opposite the ascent to the armory at the turning of the wall.",
      "M": "Next to him Ezer son of Jeshua, ruler of Mizpah, repaired another section, from a point opposite the ascent to the armory at the corner of the wall.",
      "T": "Next: Ezer son of Jeshua, governor of Mizpah—another section, opposite the ascent to the armory at the wall's corner."
    },
    "20": {
      "L": "After him Baruch the son of Zabbai repaired another section, from the turning of the wall to the door of the house of Eliashib the high priest.",
      "M": "After him Baruch son of Zabbai zealously repaired another section, from the corner to the entrance of the house of Eliashib the high priest.",
      "T": "After him Baruch son of Zabbai—and the text notes he worked eagerly—repaired the section from the corner to the entrance of the high priest Eliashib's house."
    },
    "21": {
      "L": "After him Meremoth the son of Urijah, son of Koz, repaired another section, from the door of the house of Eliashib to the end of the house of Eliashib.",
      "M": "After him Meremoth son of Uriah, son of Hakkoz, repaired another section, from the entrance to the end of Eliashib's house.",
      "T": "After him Meremoth son of Uriah, son of Hakkoz, took another section—from the entrance of Eliashib's house to its far end."
    },
    "22": {
      "L": "And after him the priests, the men of the surrounding plain, repaired.",
      "M": "After him the priests from the surrounding region made repairs.",
      "T": "After them, priests from the villages of the surrounding plain repaired the next stretch."
    },
    "23": {
      "L": "After him Benjamin and Hasshub repaired opposite their house. After him Azariah the son of Maaseiah, son of Ananiah repaired beside his own house.",
      "M": "After him Benjamin and Hasshub made repairs opposite their house. After him Azariah son of Maaseiah, son of Ananiah, made repairs beside his own house.",
      "T": "After them, Benjamin and Hasshub—repairing the section right in front of their home. After them, Azariah son of Maaseiah, son of Ananiah—working beside his own house."
    },
    "24": {
      "L": "After him Binnui the son of Henadad repaired another section, from the house of Azariah to the turning of the wall and to the corner.",
      "M": "After him Binnui son of Henadad repaired another section, from the house of Azariah to the angle and the corner.",
      "T": "After him Binnui son of Henadad—from Azariah's house all the way to the wall's angle and the corner."
    },
    "25": {
      "L": "Palal the son of Uzai repaired opposite the turning and the tower projecting from the upper house of the king at the court of the guard. After him Pedaiah the son of Parosh repaired.",
      "M": "Palal son of Uzai made repairs opposite the angle and the tower projecting from the upper house of the king at the court of the guard. After him Pedaiah son of Parosh made repairs.",
      "T": "Palal son of Uzai worked opposite the wall's angle, beside the tower projecting from the upper palace, near the court of the guard. After him, Pedaiah son of Parosh."
    },
    "26": {
      "L": "The temple servants living on Ophel repaired to a point opposite the Water Gate on the east and the projecting tower.",
      "M": "The temple servants living on the hill of Ophel made repairs as far as a point opposite the Water Gate on the east and the projecting tower.",
      "T": "The temple servants stationed on the Ophel hill repaired as far as the Water Gate on the east side, and to the projecting tower."
    },
    "27": {
      "L": "After him the Tekoites repaired another section, from opposite the great projecting tower as far as the wall of Ophel.",
      "M": "After him the Tekoites repaired another section, from a point opposite the great projecting tower to the wall of Ophel.",
      "T": "After him the Tekoites—who had already worked one section—took on another: from the great projecting tower to the wall of Ophel. The common Tekoites persisted even as their nobles had refused."
    },
    "28": {
      "L": "Above the Horse Gate the priests repaired, each one opposite his own house.",
      "M": "Above the Horse Gate the priests made repairs, each one opposite his own house.",
      "T": "Above the Horse Gate each priest repaired the section directly opposite his own house—personal responsibility, street by street."
    },
    "29": {
      "L": "After them Zadok the son of Immer repaired opposite his own house. After him Shemaiah the son of Shechaniah, the keeper of the East Gate, repaired.",
      "M": "After them Zadok son of Immer made repairs opposite his house. After him Shemaiah son of Shecaniah, keeper of the East Gate, made repairs.",
      "T": "After them, Zadok son of Immer—opposite his own house. After him, Shemaiah son of Shecaniah, the keeper of the East Gate."
    },
    "30": {
      "L": "After him Hananiah the son of Shelemiah and Hanun the sixth son of Zalaph repaired another section. After him Meshullam the son of Berechiah repaired opposite his chamber.",
      "M": "After him Hananiah son of Shelemiah and Hanun, the sixth son of Zalaph, repaired another section. After him Meshullam son of Berechiah made repairs opposite his room.",
      "T": "After him, Hananiah son of Shelemiah and Hanun the sixth son of Zalaph—another section together. After them, Meshullam son of Berechiah—opposite the room where he lived."
    },
    "31": {
      "L": "After him Malchijah, one of the goldsmiths, repaired as far as the house of the temple servants and of the merchants, opposite the Muster Gate, and to the upper chamber of the corner.",
      "M": "After him Malchijah, one of the goldsmiths, made repairs as far as the house of the temple servants and merchants, opposite the Inspection Gate, and to the upper room of the corner.",
      "T": "After him, Malchijah of the goldsmiths' guild—from the houses of the temple servants and merchants to the Muster Gate, up to the upper chamber at the corner."
    },
    "32": {
      "L": "And between the upper chamber of the corner and the Sheep Gate, the goldsmiths and the merchants repaired.",
      "M": "Between the upper room of the corner and the Sheep Gate, the goldsmiths and merchants made repairs.",
      "T": "Between the upper chamber at the corner and the Sheep Gate, the goldsmiths and merchants completed the circuit—ending where the priests had begun. The wall was whole."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'nehemiah')
        merge_tier(existing, NEHEMIAH, tier_key)
        save(tier_dir, 'nehemiah', existing)
    print('Nehemiah 1–3 written.')

if __name__ == '__main__':
    main()
