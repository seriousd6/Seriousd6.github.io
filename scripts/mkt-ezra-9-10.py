"""
MKT Ezra chapters 9–10 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezra-9-10.py

Translation decisions:
- H3068 (יהוה): "LORD" in L and M; "the LORD" in T. Consistent with all prior Ezra scripts.
- H430 (אֱלֹהִים): "God" throughout all three tiers. Divine epithets "God of Israel,"
  "God of our fathers," "God of heaven" preserved as given.
- H2617 (חֶסֶד): In 9:9 ("his mercy toward us"). Rendered "steadfast love" in L and M;
  "steadfast love" in T also — the covenantal-loyalty sense is primary here: God's faithfulness
  to captive Israel despite their unfaithfulness.
- H4604 (מַעַל, noun) / H4603 (מָעַל, verb): The root means culpable unfaithfulness, breach
  of trust toward a patron/God. L: "trespass" (noun) / "transgressed" (verb); M:
  "unfaithfulness" / "been unfaithful"; T: "faithlessness" / "broken faith." This carries
  more covenantal weight than generic "sin."
- H819 (אַשְׁמָה): guilt, culpability from wrongdoing. Distinct from H5771 (iniquity).
  L/M: "guilt"; T: "culpability" on first use, "guilt" thereafter.
- H5771 (עָוֹן): iniquity, moral wrong and its accumulated consequence. L: "iniquity";
  M: "iniquity"; T: "wrongdoing" where it pairs with אַשְׁמָה, "iniquity" elsewhere.
- H8441 (תּוֹעֵבָה): abominations — ritually impure practices. "Abominations" L/M/T.
- H3489 (יָתֵד) in 9:8: lit. peg, tent peg, stake. The image is of a stake driven into
  the ground to anchor a tent — a secured foothold. L: "a peg in his holy place"; M:
  "a secure foothold in his holy place"; T: "a stake driven into his holy ground, a
  secured presence." This is Ezra's image for the return itself.
- H4241 (מִחְיָה) in 9:8,9: reviving, sustenance. L: "reviving"; M: "brief revival" (9:8),
  "revival" (9:9); T: "a moment of renewal" (9:8), "renewed life" (9:9).
- H6413 (פְּלֵיטָה): remnant that escaped/survived. L: "escaped remnant"; M: "a surviving
  remnant"; T: "a handful of survivors" (9:8), "a remnant that escaped" (9:13-15).
- H8467 (תְּחִנָּה) in 9:8: grace, undeserved favor. L: "grace"; M: "grace"; T: "unlooked-for
  grace."
- H8451 (תּוֹרָה) in 10:3: law/Torah. L: "the law"; M: "the Law"; T: "the Torah."
- H1285 (בְּרִית) in 10:3: covenant, formal oath-bound agreement. L/M: "covenant"; T:
  "covenant" — the same solemn structure Israel has always known from Sinai.
- H5237 (נָכְרִי): foreign, strange. "Foreign" throughout in reference to wives.
- H2763 (חָרַם) in 10:8: the ḥerem — in warfare context this means "devoted to destruction."
  In this civil/community context it means "forfeited, placed under communal ban." L:
  "forfeited"; M: "forfeited and banned"; T: "confiscated and placed under ban." The
  gravity of the covenant sanction is preserved without importing the warfare sense.
- 9:4 H4503 (מִנְחָה) = the afternoon/evening grain offering (the minchah). "Evening
  offering" in L/M; "time of the evening offering" in T — Ezra's prayer is set at
  the most solemn hour of the temple liturgical day.
- 9:8–9 structural note: Two parallel "and now" grace statements — God gave (1) a brief
  window of divine favor and (2) an extension of steadfast love even in captivity. The
  T tier surfaces this parallelism.
- 10:15 textual note: The Hebrew is ambiguous — Jonathan, Jahzeiah, Meshullam, and
  Shabbethai are either opponents of the measure or people appointed to oversee it. The
  majority reading (ESV, NRSV) has Jonathan and Jahzeiah opposing and Meshullam/Shabbethai
  supporting the opposition. T acknowledges the interpretive difficulty.
- 9:11–12: These verses are Ezra's citation of the prophetic prohibition on intermarriage —
  a composite of Deuteronomy 7:1-4 and similar texts, framed as prophetic speech. T
  surfaces the deliberate citation structure.
- OT echoes: 9:6 "our iniquities have risen higher than our heads" echoes Ps 38:4. The
  phrase "holy seed" (9:2) echoes Isa 6:13 — the remnant as the seed of restoration. The
  confessional structure of 9:6–15 mirrors Nehemiah 9, Daniel 9, and the pattern of the
  great penitential psalms (Ps 51, 78). T surfaces these where natural.
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

EZRA = {
  "9": {
    "1": {
      "L": "Now when these things were done, the princes came to me, saying: 'The people of Israel and the priests and the Levites have not separated themselves from the peoples of the lands, doing according to their abominations—the Canaanites, the Hittites, the Perizzites, the Jebusites, the Ammonites, the Moabites, the Egyptians, and the Amorites.'",
      "M": "When these things had been completed, the leaders came to me with this report: 'The people of Israel—including the priests and the Levites—have not separated themselves from the peoples of the surrounding lands. They have adopted the abominable practices of the Canaanites, Hittites, Perizzites, Jebusites, Ammonites, Moabites, Egyptians, and Amorites.'",
      "T": "When all the initial work was complete, the community leaders came to Ezra with a devastating report: the people of Israel—priests and Levites included—had not kept themselves separate from the surrounding peoples. They had conformed to those peoples' abominations: the Canaanites, Hittites, Perizzites, Jebusites, Ammonites, Moabites, Egyptians, and Amorites."
    },
    "2": {
      "L": "For they have taken of their daughters for themselves and for their sons, so the holy seed has mingled with the peoples of the lands; and the hand of the princes and rulers has been chief in this trespass.",
      "M": "They have taken women from these peoples as wives for themselves and their sons, so that the holy offspring has become mixed with the peoples of the surrounding lands—and the officials and leaders have been the first to act in this unfaithfulness.",
      "T": "They had taken their daughters as wives for themselves and their sons, interweaving the holy seed—Isaiah's image for the remnant of restoration (Isa 6:13)—with the surrounding nations. Worse still, the officials and leaders had led the way in this faithlessness."
    },
    "3": {
      "L": "And when I heard this thing, I tore my garment and my robe, and plucked off the hair of my head and of my beard, and sat down appalled.",
      "M": "When I heard this, I tore my garment and robe, pulled out hair from my head and beard, and sat down in shock.",
      "T": "When Ezra heard this he tore his garment and robe, pulled out hair from his head and beard, and sat down devastated—the visible signs of a man for whom the news was not merely administrative but catastrophic."
    },
    "4": {
      "L": "Then all who trembled at the words of the God of Israel assembled to me, because of the trespass of the returned exiles; and I sat appalled until the evening offering.",
      "M": "Then all who trembled at the words of the God of Israel gathered around me over the unfaithfulness of the returned exiles, while I sat appalled until the time of the evening offering.",
      "T": "Around him gathered all who still trembled at the word of the God of Israel—those who took the covenant seriously and were horrified by what the exiles had done. Ezra sat in silence, undone, until the hour of the evening offering."
    },
    "5": {
      "L": "And at the evening offering I arose from my self-abasement—with my garment and my robe torn—and fell upon my knees and spread out my hands to the LORD my God,",
      "M": "At the time of the evening offering I rose from my self-abasement, with my garment and robe still torn, and fell on my knees and stretched out my hands to the LORD my God,",
      "T": "At the hour of the evening offering Ezra rose from his prostration—garment and robe still torn—and dropped to his knees, spreading his hands toward the LORD his God. The prayer that follows is one of the Bible's great confessional prayers:"
    },
    "6": {
      "L": "saying: 'O my God, I am ashamed and blush to lift my face to you, my God; for our iniquities have risen higher than our heads, and our guilt has mounted up to the heavens.",
      "M": "'O my God, I am too ashamed and disgraced to lift my face to you, my God; for our iniquities have risen over our heads, and our guilt has grown as high as the heavens.",
      "T": "'O my God—I am ashamed, too humiliated to lift my face toward you. Our iniquities have risen over our heads; our guilt has piled up to the sky itself (cf. Ps 38:4). There is nowhere to hide from it.'"
    },
    "7": {
      "L": "'From the days of our fathers to this day we have been in great guilt; and for our iniquities we, our kings, and our priests have been given into the hand of the kings of the lands, to the sword, to captivity, to plundering, and to utter shame, as it is this day.",
      "M": "'From the days of our ancestors to this very day we have been deeply guilty. Because of our iniquities, we, our kings, and our priests have been given over to the kings of the surrounding nations—to the sword, to captivity, to pillaging, and to utter disgrace, as it still is today.",
      "T": "'From our ancestors to this very moment the pattern has been the same: great guilt. And because of our iniquity, we—our kings, our priests, everyone—have been handed over to the nations: to the sword, to exile, to plundering, to the kind of public shame that leaves a people faceless. As it still is today.'"
    },
    "8": {
      "L": "'And now for a brief moment grace has been shown by the LORD our God, to leave us an escaped remnant and to give us a peg in his holy place, that our God may lighten our eyes and grant us a little reviving in our slavery.",
      "M": "'But now, for a brief moment, grace has been shown to us by the LORD our God, who has left us a surviving remnant and given us a secure foothold in his holy place—so that our God might give light to our eyes and grant us a little revival even in our captivity.",
      "T": "'And yet—for a brief window—the LORD our God has shown unlooked-for grace. He has left us a handful of survivors and driven a stake into his holy ground for us: a secured presence, a foothold among his people. He has done this to brighten our eyes and to give us a moment of renewal even here in our bondage. We did not deserve this.'"
    },
    "9": {
      "L": "'For we are slaves; yet our God has not forsaken us in our slavery, but has extended to us his steadfast love before the kings of Persia, to give us revival, to set up the house of our God, to repair its ruins, and to give us a wall of protection in Judah and Jerusalem.",
      "M": "'Though we are slaves, our God has not abandoned us in our captivity. He has extended his steadfast love to us in the sight of the kings of Persia, granting us renewed life—to rebuild the house of our God, to restore its ruins, and to give us a protective enclosure in Judah and Jerusalem.",
      "T": "'We are still slaves—let no one forget that. Yet our God did not abandon us in our bondage. He extended his steadfast love toward us before the very eyes of the Persian kings: giving us renewed life, the rebuilt temple, the restored ruins, and a sheltering wall around his people in Judah and Jerusalem. The whole return was this—an act of his love.'"
    },
    "10": {
      "L": "'And now, O our God, what shall we say after this? For we have forsaken your commandments,",
      "M": "'And now, our God, what can we say after all this? For we have abandoned your commandments,",
      "T": "'What can we say after all of that, O our God? The grace you showed—and then this? We turned and abandoned your commandments.'"
    },
    "11": {
      "L": "'which you commanded by your servants the prophets, saying, \"The land you are entering to possess is a land impure with the impurity of the peoples of the lands, with their abominations that have filled it from end to end with their uncleanness.",
      "M": "'the very commands you gave through your servant prophets, saying: \"The land you are entering to take possession of is a land polluted with the impurity of its peoples—their abominations have filled it from end to end with their filth.",
      "T": "'You had made your will plain through the prophets: \"The land you are about to enter and possess is saturated with the uncleanness of those peoples—their abominations have polluted it from border to border. You are walking into a defiled land.\""
    },
    "12": {
      "L": "'\"Therefore do not give your daughters to their sons, nor take their daughters for your sons; and never seek their peace or their prosperity, that you may be strong and eat the good of the land and leave it for an inheritance to your children forever.\"",
      "M": "'\"Therefore do not give your daughters to their sons or take their daughters for your sons. Never pursue their peace or prosperity—so that you may be strong, enjoy the good of the land, and pass it on to your children as an inheritance forever.\"",
      "T": "'\"Therefore: no intermarriage. Never give your daughters to their sons, never take their daughters for your sons. Never seek their peace or their prosperity. Keep the boundary—so that you can take hold of the land, enjoy its goodness, and hand it on to your children forever\" (cf. Deut 7:3-4). This was the command. This is what we broke.'"
    },
    "13": {
      "L": "'And after all that has come upon us for our evil deeds and our great guilt—seeing that you, our God, have punished us less than our iniquities deserved and have given us such an escaped remnant as this—",
      "M": "'After everything that has come upon us because of our evil deeds and our great guilt—and you, our God, have punished us far less than our sins deserved, and have given us even this surviving remnant—",
      "T": "'After every consequence our wickedness brought on us—and you, our God, held back the full measure of what our iniquity deserved, and still gave us this remnant that escaped—'"
    },
    "14": {
      "L": "'shall we again break your commandments and intermarry with the peoples who practice these abominations? Would you not be angry with us until you had consumed us, so that there is no remnant or any who escape?",
      "M": "'shall we break your commandments again and intermarry with peoples who commit these abominations? Would you not then be angry with us until you destroyed us completely, leaving no remnant and no one to escape?",
      "T": "'—shall we turn and break your commandments again? Shall we intermarry again with these very peoples and their abominations? If we do, would you not be right to let your anger consume us entirely—until there is no remnant left, not a single survivor?'"
    },
    "15": {
      "L": "'O LORD, God of Israel, you are righteous; for we are left an escaped remnant, as it is this day. Behold, we are before you in our guilt, for none can stand before you because of this.'",
      "M": "'O LORD, God of Israel, you are righteous; you have left us a remnant that has escaped, as it is today. Here we stand before you in our guilt—because of this, not one of us can stand before you.'",
      "T": "'O LORD, God of Israel—you are righteous. You have left us a remnant that survived, exactly as today shows. But here we stand before you: guilty. Not one of us can face you on our own merits. The guilt is ours. The righteousness is yours alone.'"
    }
  },
  "10": {
    "1": {
      "L": "Now while Ezra prayed and made confession, weeping and casting himself down before the house of God, there assembled to him from Israel a very great congregation of men, women, and children; for the people wept bitterly.",
      "M": "While Ezra prayed and made his confession, weeping and throwing himself down before the house of God, a very large assembly of Israelite men, women, and children gathered around him, and the people wept with intense grief.",
      "T": "While Ezra prayed and confessed—weeping, prostrate on the ground before God's house—an enormous crowd assembled around him: men, women, and children out of all Israel. They wept bitterly. His grief had become the community's grief."
    },
    "2": {
      "L": "And Shechaniah son of Jehiel, of the sons of Elam, addressed Ezra: 'We have broken faith with our God and have married foreign women from the peoples of the land; yet now there is hope for Israel in spite of this.",
      "M": "Then Shechaniah son of Jehiel, of the family of Elam, spoke up to Ezra: 'We have been unfaithful to our God by marrying foreign women from the peoples of the land. But even now there is hope for Israel in spite of this.",
      "T": "Then Shechaniah son of Jehiel, of the family of Elam, spoke up—and what he said turned crisis into possibility: 'We have broken faith with our God. We have taken foreign wives from the surrounding peoples. That is the truth. And yet—even now there is hope for Israel.'"
    },
    "3": {
      "L": "'Now therefore let us make a covenant with our God to put away all these wives and all who have been born to them, according to the counsel of my lord and of those who tremble at the commandment of our God; and let it be done according to the Law.",
      "M": "'So let us now make a covenant with our God to send away all these foreign wives and their children, following the advice of my lord and of those who fear God's commandment. Let it be done in accordance with the Law.",
      "T": "'So let us make a covenant with our God—a formal, binding agreement—to send away all these foreign wives and the children born to them. Let this be done following the counsel of my lord Ezra and all who tremble at God's commandment. And let it be done according to the Torah—lawfully, not rashly.'"
    },
    "4": {
      "L": "'Arise, for it is your duty, and we are with you; be strong and do it.'",
      "M": "'Rise up, for this task is yours to lead, and we are with you. Be courageous and act.'",
      "T": "'Get up. This is your responsibility—no one else can lead this. We stand with you. Be strong and do it.'"
    },
    "5": {
      "L": "Then Ezra arose and made the chief priests, the Levites, and all Israel swear to do according to this word. So they swore.",
      "M": "Then Ezra stood up and put the leading priests, the Levites, and all Israel under oath to carry out what had been proposed. They took the oath.",
      "T": "Ezra rose and administered the oath to the chief priests, the Levites, and all Israel—binding them to carry out Shechaniah's proposal. They swore. The covenant was set."
    },
    "6": {
      "L": "Then Ezra rose from before the house of God and went to the chamber of Jehohanan son of Eliashib, where he spent the night, neither eating bread nor drinking water; for he was mourning over the unfaithfulness of the returned exiles.",
      "M": "Then Ezra left the area in front of God's house and went to the room of Jehohanan son of Eliashib. He spent the night there, eating no bread and drinking no water, for he was mourning deeply over the faithlessness of the returned exiles.",
      "T": "Ezra withdrew from before God's house and went to the chamber of Jehohanan son of Eliashib. He spent the night there—no food, no water—continuing his mourning over the faithlessness of those who had come back from exile. The fast continued even after the prayer."
    },
    "7": {
      "L": "And they made proclamation throughout Judah and Jerusalem to all the returned exiles that they should assemble at Jerusalem,",
      "M": "A proclamation was sent throughout Judah and Jerusalem to all the returned exiles, directing them to gather in Jerusalem.",
      "T": "A proclamation went out through all Judah and Jerusalem: every returned exile was summoned to gather at Jerusalem."
    },
    "8": {
      "L": "and that whoever did not come within three days, according to the counsel of the officials and elders all his property would be forfeited, and he himself separated from the congregation of the exiles.",
      "M": "Anyone who failed to appear within three days would, by order of the officials and elders, have all his property forfeited and would be expelled from the congregation of the returned exiles.",
      "T": "The stakes were clear: any who refused to come within three days would, by ruling of the officials and elders, have all their property confiscated and be placed under communal ban—cut off from the returning community entirely. The gravity of the situation demanded it."
    },
    "9": {
      "L": "Then all the men of Judah and Benjamin assembled at Jerusalem within the three days. It was the ninth month, on the twentieth day of the month; and all the people sat in the open square before the house of God, trembling because of this matter and because of the heavy rain.",
      "M": "All the men of Judah and Benjamin gathered at Jerusalem within the three-day deadline. It was the ninth month, the twentieth day—and all the people sat in the open plaza before God's house, trembling both over this matter and because of the heavy rain.",
      "T": "Within three days every man from Judah and Benjamin had come to Jerusalem. It was the twentieth day of the ninth month—Kislev, late autumn, the rainy season at its worst. They sat in the open square before God's house, shivering in the downpour, trembling at the weight of what they had to face."
    },
    "10": {
      "L": "And Ezra the priest stood up and said to them: 'You have transgressed and have married foreign women, thus increasing the guilt of Israel.",
      "M": "Then Ezra the priest stood and said to them: 'You have been unfaithful—you have married foreign women, adding to Israel's guilt.",
      "T": "Ezra the priest stood and addressed the assembly: 'You have broken faith. You have taken foreign wives—and in doing so you have added to the guilt that already weighs on Israel.'"
    },
    "11": {
      "L": "'Now therefore make confession to the LORD, the God of your fathers, and do his will. Separate yourselves from the peoples of the land and from the foreign wives.'",
      "M": "'Now make confession to the LORD, the God of your ancestors, and do what pleases him. Separate yourselves from the peoples of the land and from the foreign wives.'",
      "T": "'Now—make your confession to the LORD, the God of your fathers. Do what he requires. Separate yourselves from the surrounding peoples and from the foreign wives. That is the path back.'"
    },
    "12": {
      "L": "Then all the congregation answered with a loud voice: 'Yes, it is our duty to do as you have said.'",
      "M": "The whole assembly responded with a loud voice: 'Yes! We must do exactly as you have said.'",
      "T": "The entire assembly answered together, raising their voices: 'Yes—we must do as you have said.' The commitment was made publicly, out in the rain."
    },
    "13": {
      "L": "'But the people are many, and it is a time of heavy rain, and we are not able to stand in the open. Nor is this a task for one or two days, for many of us have transgressed in this matter.'",
      "M": "'However, there are many people involved, it is the rainy season and we cannot remain standing out here, and this is not a matter that can be resolved in one or two days—for a great number of us have violated this commandment.'",
      "T": "'But we need a workable plan. The people involved are many; the rain is heavy and we cannot stand here indefinitely; and this is not a one-day matter—the number of transgressions is large. We are committed, but we need a proper process.'"
    },
    "14": {
      "L": "'Let our officials stand for the whole congregation; and let all in our cities who have taken foreign wives come at appointed times, together with the elders and judges of every city, until the fierce wrath of our God over this matter is turned away from us.'",
      "M": "'Let our officials represent the whole assembly. Let everyone in our cities who has married a foreign wife appear at scheduled times, with the elders and judges of their city, until the fierce anger of our God over this matter is turned away from us.'",
      "T": "'Here is what we propose: let our officials act on behalf of the whole assembly. Then let everyone across our cities who has taken a foreign wife come at designated times, with their city elders and judges as witnesses, until the LORD's fierce anger over this is appeased. Do it properly, city by city, case by case.'"
    },
    "15": {
      "L": "Only Jonathan son of Asahel and Jahzeiah son of Tikvah opposed this, and Meshullam and Shabbethai the Levite supported them.",
      "M": "Only Jonathan son of Asahel and Jahzeiah son of Tikvah opposed the plan, with Meshullam and Shabbethai the Levite backing them.",
      "T": "Only Jonathan son of Asahel and Jahzeiah son of Tikvah dissented—and Meshullam and Shabbethai the Levite stood with them. The text does not explain their objection; whether they opposed the reform entirely or only the proposed procedure, the narrator does not say."
    },
    "16": {
      "L": "Then the returned exiles did so. Ezra the priest selected men, heads of fathers' houses, by their fathers' houses, each designated by name; and they sat down on the first day of the tenth month to examine the matter.",
      "M": "The returned exiles proceeded accordingly. Ezra the priest designated specific men—heads of families, listed by name according to their clans—and they convened on the first day of the tenth month to investigate the cases.",
      "T": "The returning community moved forward. Ezra appointed named heads of households—a proper committee organized by family—and on the first day of the tenth month they sat down to examine every case. Due process, not summary action."
    },
    "17": {
      "L": "And by the first day of the first month they had finished examining all the men who had married foreign women.",
      "M": "By the first day of the first month they had completed their review of all the men who had taken foreign wives.",
      "T": "Three months of careful case-by-case examination—and by the first day of the first month, the investigation of every man who had married a foreign wife was complete."
    },
    "18": {
      "L": "And there were found among the sons of the priests some who had married foreign women: of the sons of Jeshua son of Jozadak and his brothers: Maaseiah, Eliezer, Jarib, and Gedaliah.",
      "M": "Among the priests, the following were found to have married foreign women. From the sons of Jeshua son of Jozadak and his brothers: Maaseiah, Eliezer, Jarib, and Gedaliah.",
      "T": "The list of offenders begins with the priests—the most serious cases, since priestly purity was the foundation of the community's holiness. From the sons of Jeshua son of Jozadak and his brothers: Maaseiah, Eliezer, Jarib, and Gedaliah."
    },
    "19": {
      "L": "They pledged themselves to put away their wives; and being guilty, they offered a ram of the flock as their guilt offering.",
      "M": "They pledged to put away their foreign wives; and acknowledging their guilt, they brought a ram from the flock as a guilt offering.",
      "T": "These men gave their word that they would send away their foreign wives. And, acknowledging their culpability before God, they offered a ram from the flock as a guilt offering. The ritual acknowledged what the act had cost."
    },
    "20": {
      "L": "Of the sons of Immer: Hanani and Zebadiah.",
      "M": "From the sons of Immer: Hanani and Zebadiah.",
      "T": "From the priestly family of Immer: Hanani and Zebadiah."
    },
    "21": {
      "L": "Of the sons of Harim: Maaseiah, Elijah, Shemaiah, Jehiel, and Uzziah.",
      "M": "From the sons of Harim: Maaseiah, Elijah, Shemaiah, Jehiel, and Uzziah.",
      "T": "From the family of Harim: Maaseiah, Elijah, Shemaiah, Jehiel, and Uzziah."
    },
    "22": {
      "L": "Of the sons of Pashur: Elioenai, Maaseiah, Ishmael, Nethaneel, Jozabad, and Elasah.",
      "M": "From the sons of Pashur: Elioenai, Maaseiah, Ishmael, Nethaneel, Jozabad, and Elasah.",
      "T": "From the family of Pashur: Elioenai, Maaseiah, Ishmael, Nethaneel, Jozabad, and Elasah."
    },
    "23": {
      "L": "Of the Levites: Jozabad, Shimei, Kelaiah (that is, Kelita), Pethahiah, Judah, and Eliezer.",
      "M": "Of the Levites: Jozabad, Shimei, Kelaiah (also known as Kelita), Pethahiah, Judah, and Eliezer.",
      "T": "Among the Levites: Jozabad, Shimei, Kelaiah (the same man as Kelita), Pethahiah, Judah, and Eliezer."
    },
    "24": {
      "L": "Of the singers: Eliashib. Of the gatekeepers: Shallum, Telem, and Uri.",
      "M": "Of the singers: Eliashib. Of the gatekeepers: Shallum, Telem, and Uri.",
      "T": "From the temple singers: Eliashib. From the gatekeepers: Shallum, Telem, and Uri."
    },
    "25": {
      "L": "And of Israel: of the sons of Parosh: Ramiah, Izziah, Malchijah, Mijamin, Eleazar, Malchijah, and Benaiah.",
      "M": "Among the lay Israelites: from the sons of Parosh: Ramiah, Izziah, Malchijah, Mijamin, Eleazar, Malchijah, and Benaiah.",
      "T": "Now the lay Israelites—not clergy but ordinary members of the community—from the family of Parosh: Ramiah, Izziah, Malchijah, Mijamin, Eleazar, Malchijah, and Benaiah."
    },
    "26": {
      "L": "Of the sons of Elam: Mattaniah, Zechariah, Jehiel, Abdi, Jeremoth, and Elijah.",
      "M": "From the sons of Elam: Mattaniah, Zechariah, Jehiel, Abdi, Jeremoth, and Elijah.",
      "T": "From the family of Elam: Mattaniah, Zechariah, Jehiel, Abdi, Jeremoth, and Elijah."
    },
    "27": {
      "L": "Of the sons of Zattu: Elioenai, Eliashib, Mattaniah, Jeremoth, Zabad, and Aziza.",
      "M": "From the sons of Zattu: Elioenai, Eliashib, Mattaniah, Jeremoth, Zabad, and Aziza.",
      "T": "From the family of Zattu: Elioenai, Eliashib, Mattaniah, Jeremoth, Zabad, and Aziza."
    },
    "28": {
      "L": "Of the sons of Bebai: Jehohanan, Hananiah, Zabbai, and Athlai.",
      "M": "From the sons of Bebai: Jehohanan, Hananiah, Zabbai, and Athlai.",
      "T": "From the family of Bebai: Jehohanan, Hananiah, Zabbai, and Athlai."
    },
    "29": {
      "L": "Of the sons of Bani: Meshullam, Malluch, Adaiah, Jashub, Sheal, and Jeremoth.",
      "M": "From the sons of Bani: Meshullam, Malluch, Adaiah, Jashub, Sheal, and Jeremoth.",
      "T": "From the family of Bani: Meshullam, Malluch, Adaiah, Jashub, Sheal, and Jeremoth."
    },
    "30": {
      "L": "Of the sons of Pahathmoab: Adna, Chelal, Benaiah, Maaseiah, Mattaniah, Bezaleel, Binnui, and Manasseh.",
      "M": "From the sons of Pahathmoab: Adna, Chelal, Benaiah, Maaseiah, Mattaniah, Bezaleel, Binnui, and Manasseh.",
      "T": "From the family of Pahathmoab: Adna, Chelal, Benaiah, Maaseiah, Mattaniah, Bezaleel, Binnui, and Manasseh."
    },
    "31": {
      "L": "Of the sons of Harim: Eliezer, Ishijah, Malchijah, Shemaiah, Shimeon,",
      "M": "From the sons of Harim: Eliezer, Ishijah, Malchijah, Shemaiah, Shimeon,",
      "T": "From the lay family of Harim: Eliezer, Ishijah, Malchijah, Shemaiah, Shimeon,"
    },
    "32": {
      "L": "Benjamin, Malluch, and Shemariah.",
      "M": "Benjamin, Malluch, and Shemariah.",
      "T": "Benjamin, Malluch, and Shemariah."
    },
    "33": {
      "L": "Of the sons of Hashum: Mattenai, Mattattah, Zabad, Eliphelet, Jeremai, Manasseh, and Shimei.",
      "M": "From the sons of Hashum: Mattenai, Mattattah, Zabad, Eliphelet, Jeremai, Manasseh, and Shimei.",
      "T": "From the family of Hashum: Mattenai, Mattattah, Zabad, Eliphelet, Jeremai, Manasseh, and Shimei."
    },
    "34": {
      "L": "Of the sons of Bani: Maadai, Amram, Uel,",
      "M": "From the sons of Bani: Maadai, Amram, Uel,",
      "T": "From the family of Bani—the longest list in this register—beginning: Maadai, Amram, Uel,"
    },
    "35": {
      "L": "Bedeiah, Chelluh, Vaniah,",
      "M": "Bedeiah, Chelluh, Vaniah,",
      "T": "Bedeiah, Chelluh, Vaniah,"
    },
    "36": {
      "L": "Meremoth, Eliashib,",
      "M": "Meremoth, Eliashib,",
      "T": "Meremoth, Eliashib,"
    },
    "37": {
      "L": "Mattenai, Mattaniah, Jaasau,",
      "M": "Mattenai, Mattaniah, Jaasau,",
      "T": "Mattenai, Mattaniah, Jaasau,"
    },
    "38": {
      "L": "Binnui, Shimei,",
      "M": "Binnui, Shimei,",
      "T": "Binnui, Shimei,"
    },
    "39": {
      "L": "Shelemiah, Nathan, Adaiah,",
      "M": "Shelemiah, Nathan, Adaiah,",
      "T": "Shelemiah, Nathan, Adaiah,"
    },
    "40": {
      "L": "Machnadebai, Shashai, Sharai,",
      "M": "Machnadebai, Shashai, Sharai,",
      "T": "Machnadebai, Shashai, Sharai,"
    },
    "41": {
      "L": "Azareel, Shelemiah, Shemariah,",
      "M": "Azareel, Shelemiah, Shemariah,",
      "T": "Azareel, Shelemiah, Shemariah,"
    },
    "42": {
      "L": "Shallum, Amariah, and Joseph.",
      "M": "Shallum, Amariah, and Joseph.",
      "T": "Shallum, Amariah, and Joseph."
    },
    "43": {
      "L": "Of the sons of Nebo: Jeiel, Mattithiah, Zabad, Zebina, Jaddai, Joel, and Benaiah.",
      "M": "From the sons of Nebo: Jeiel, Mattithiah, Zabad, Zebina, Jaddai, Joel, and Benaiah.",
      "T": "From the family of Nebo: Jeiel, Mattithiah, Zabad, Zebina, Jaddai, Joel, and Benaiah."
    },
    "44": {
      "L": "All these had married foreign women, and some of the women had borne children.",
      "M": "All of these had married foreign women; and some of the women had already borne children.",
      "T": "Every name on this list had taken a foreign wife. For some, children had already been born—a detail that underscores both the depth of the problem and the real human cost of what the covenant required. The book ends here, without telling us whether every case was resolved."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezra')
        merge_tier(existing, EZRA, tier_key)
        save(tier_dir, 'ezra', existing)
    print('Ezra 9–10 written.')

if __name__ == '__main__':
    main()
