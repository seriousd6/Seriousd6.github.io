"""
MKT Numbers chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-numbers-13-18.py

Covers: the twelve spies sent to Canaan and their report (ch. 13), the people's rebellion
and the forty-year sentence (ch. 14), supplementary offerings / Sabbath-breaker / tassels
(ch. 15), Korah's rebellion and its aftermath (ch. 16), Aaron's budding staff (ch. 17),
priestly and Levitical duties and tithes (ch. 18).

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps) in L/M; "the LORD" in T — matches all prior Numbers scripts
- H430 (אֱלֹהִים): "God" all tiers
- H5387 (נָשִׂיא): "leader" throughout, not "prince" — carries forward from chs 7–12
- H5303 (נְפִילִים): "giants" in L (interlinear gloss); "Nephilim" in M; "the Nephilim — ancient warrior-giants" in T
  — the MT term is Nephilim; T names and explains; L follows the traditional gloss for transparency
- H2617 (חֶסֶד): "mercy" in L (14:18,19 — interlinear gloss); "steadfast love" in M/T — covenant faithfulness
- H1681 (דִּבָּה): "evil report" in L; "bad report" in M; "slanderous report" in T (13:32; 14:36–37)
- H5771 (עָוֹן): "iniquity" L/M; "guilt" T
- H6588 (פֶּשַׁע): "transgression" L/M; "rebellion" T
- H4294 (מַטֶּה): context-split — "tribe" in ch. 13 (tribal context); "rod/staff" in ch. 17 (Aaron's rod)
- H7307 (רוּחַ): in 14:24 (Caleb's "different spirit") = personal disposition, not divine Spirit → "spirit" all tiers (lowercase)
- H8453/H1616 (תּוֹשָׁב/גֵּר — sojourner/stranger): "stranger" in L; "resident alien" in M/T
- H4289 (מַחְתָּה): "censer" L/M; "incense pan" T — ch. 16
- H6734 (צִיצִת): "fringe" L; "tassels" M/T — ch. 15
- H8504 (תְּכֵלֶת): "blue" L; "blue cord" M/T
- H4643 (מַעֲשֵׂר): "tithe" all tiers — ch. 18
- H4905 (מֶלַח — salt covenant): "covenant of salt" all tiers — 18:19; ancient Near Eastern idiom for permanent,
  binding covenant (salt preserves; the covenant endures)
- H7585 (שְׁאוֹל): "pit" L; "Sheol" M/T — 16:30,33
- Chapter 13 note: Joshua's renaming in v. 16 (Hoshea → Joshua, "the LORD saves") is the first appearance
  of the name in Numbers; rendered with a brief gloss in T tier.
- Chapter 14 note: Moses's intercession in vv. 17–19 quotes the Sinai theophany (Exod 34:6–7) almost
  verbatim — a deliberate invocation of the covenant formula. T tier surfaces the echo.
- Chapter 14:34 note: "breach of promise / alienation" (H8569, תְּנוּאָה) = the LORD experiencing their
  opposition; rendered "displeasure" in M; "the cost of opposing me" in T.
- Chapter 15 note: The Sabbath-breaker episode (vv. 32–36) follows immediately after the section on
  deliberate sin (vv. 30–31). The juxtaposition is not accidental — the narrative illustrates the law.
- Chapter 16 note: Korah is a Kohathite Levite (the tribe closest to the sanctuary); his rebellion is
  specifically about the boundary between Levitical service and Aaronic priesthood. T tier surfaces this
  patron-client and honor-shame dynamic. Aaron stopping the plague with incense (vv. 46–48) is the ultimate
  vindication: the very act Korah claimed the right to perform is what saves Israel.
- Chapter 17 note: The overnight blossoming of Aaron's staff (v. 8 — buds, blossoms, and ripe almonds
  simultaneously) is a sign of miraculous, unambiguous divine choice. T tier notes the impossibility.
- Chapter 18 note: "covenant of salt" (v. 19) — salt preserves and prevents decay; the idiom signals a
  permanent, inviolable agreement. Documented in T tier.
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

NUMBERS = {
  "13": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Send thou men, that they may spy out the land of Canaan, which I give unto the children of Israel; of every tribe of their fathers shall ye send a man, every one a ruler among them.",
      "M": "Send men to spy out the land of Canaan, which I am giving to the Israelites. From each of their ancestral tribes send one man — every one a leader among them.",
      "T": "Send scouts into Canaan — the land I am giving to Israel. One man from each tribe, a recognized leader whose report will carry weight."
    },
    "3": {
      "L": "And Moses sent them from the wilderness of Paran at the commandment of the LORD: all those men were heads of the children of Israel.",
      "M": "So Moses sent them from the wilderness of Paran at the LORD's command. All of them were leading men among the Israelites.",
      "T": "Moses dispatched them from the Paran wilderness at the LORD's command. Every one was a man of standing in Israel."
    },
    "4": {
      "L": "And these were their names: of the tribe of Reuben, Shammua the son of Zaccur.",
      "M": "These were their names: from the tribe of Reuben, Shammua son of Zaccur.",
      "T": "Their names: from Reuben — Shammua son of Zaccur."
    },
    "5": {
      "L": "Of the tribe of Simeon, Shaphat the son of Hori.",
      "M": "From the tribe of Simeon, Shaphat son of Hori.",
      "T": "From Simeon — Shaphat son of Hori."
    },
    "6": {
      "L": "Of the tribe of Judah, Caleb the son of Jephunneh.",
      "M": "From the tribe of Judah, Caleb son of Jephunneh.",
      "T": "From Judah — Caleb son of Jephunneh."
    },
    "7": {
      "L": "Of the tribe of Issachar, Igal the son of Joseph.",
      "M": "From the tribe of Issachar, Igal son of Joseph.",
      "T": "From Issachar — Igal son of Joseph."
    },
    "8": {
      "L": "Of the tribe of Ephraim, Oshea the son of Nun.",
      "M": "From the tribe of Ephraim, Hoshea son of Nun.",
      "T": "From Ephraim — Hoshea son of Nun."
    },
    "9": {
      "L": "Of the tribe of Benjamin, Palti the son of Raphu.",
      "M": "From the tribe of Benjamin, Palti son of Raphu.",
      "T": "From Benjamin — Palti son of Raphu."
    },
    "10": {
      "L": "Of the tribe of Zebulun, Gaddiel the son of Sodi.",
      "M": "From the tribe of Zebulun, Gaddiel son of Sodi.",
      "T": "From Zebulun — Gaddiel son of Sodi."
    },
    "11": {
      "L": "Of the tribe of Joseph, namely, of the tribe of Manasseh, Gaddi the son of Susi.",
      "M": "From the tribe of Joseph — from the tribe of Manasseh — Gaddi son of Susi.",
      "T": "From Joseph, specifically from Manasseh — Gaddi son of Susi."
    },
    "12": {
      "L": "Of the tribe of Dan, Ammiel the son of Gemalli.",
      "M": "From the tribe of Dan, Ammiel son of Gemalli.",
      "T": "From Dan — Ammiel son of Gemalli."
    },
    "13": {
      "L": "Of the tribe of Asher, Sethur the son of Michael.",
      "M": "From the tribe of Asher, Sethur son of Michael.",
      "T": "From Asher — Sethur son of Michael."
    },
    "14": {
      "L": "Of the tribe of Naphtali, Nahbi the son of Vophsi.",
      "M": "From the tribe of Naphtali, Nahbi son of Vophsi.",
      "T": "From Naphtali — Nahbi son of Vophsi."
    },
    "15": {
      "L": "Of the tribe of Gad, Geuel the son of Machi.",
      "M": "From the tribe of Gad, Geuel son of Machi.",
      "T": "From Gad — Geuel son of Machi."
    },
    "16": {
      "L": "These are the names of the men which Moses sent to spy out the land. And Moses called Oshea the son of Nun Jehoshua.",
      "M": "These are the names of the men Moses sent to spy out the land. Moses called Hoshea son of Nun, Joshua.",
      "T": "These were the twelve scouts Moses sent into Canaan. He also renamed Hoshea son of Nun: Joshua — 'the LORD saves.'"
    },
    "17": {
      "L": "And Moses sent them to spy out the land of Canaan, and said unto them, Get you up this way southward, and go up into the mountain:",
      "M": "Moses sent them to spy out the land of Canaan and said to them: Go up through the Negeb and up into the hill country.",
      "T": "Moses gave them their orders: 'Go up through the Negeb and into the hill country.'"
    },
    "18": {
      "L": "And see the land, what it is; and the people that dwelleth therein, whether they be strong or weak, few or many;",
      "M": "See what the land is like, and whether the people living there are strong or weak, whether they are few or many,",
      "T": "Assess everything: the land itself, its people — strong or weak, few or many —"
    },
    "19": {
      "L": "And what the land is that they dwell in, whether it be good or bad; and what cities they be that they dwell in, whether in tents, or in strong holds;",
      "M": "and whether the land they live in is good or bad, and whether the cities they inhabit are open camps or fortified strongholds,",
      "T": "— whether the land is good or poor, whether the settlements are open villages or walled fortresses —"
    },
    "20": {
      "L": "And what the land is, whether it be fat or lean, whether there be wood therein, or not. And be ye of good courage, and bring of the fruit of the land. Now the time was the time of the firstripe grapes.",
      "M": "and whether the land is fertile or lean, and whether there are trees in it or not. Be bold, and bring back some of the fruit of the land. Now it was the season of the first ripe grapes.",
      "T": "— whether the soil is rich or thin, whether there is timber. Be bold — and bring back fruit from the land.' It was the season of the first ripe grapes."
    },
    "21": {
      "L": "So they went up, and searched the land from the wilderness of Zin unto Rehob, as men come to Hamath.",
      "M": "So they went up and spied out the land from the wilderness of Zin to Rehob, near Lebo-hamath.",
      "T": "The twelve scouts swept the entire length of the land — from the Zin wilderness in the south all the way north to Rehob near Lebo-hamath."
    },
    "22": {
      "L": "And they ascended by the south, and came unto Hebron; where Ahiman, Sheshai, and Talmai, the children of Anak, were. (Now Hebron was built seven years before Zoan in Egypt.)",
      "M": "They went up through the Negeb and came to Hebron. Ahiman, Sheshai, and Talmai, the descendants of Anak, were there. Hebron had been built seven years before Zoan in Egypt.",
      "T": "Pushing into the Negeb, they reached Hebron — an ancient city, already standing seven years before Egypt's Zoan was built. There they encountered Ahiman, Sheshai, and Talmai, of Anak's clan."
    },
    "23": {
      "L": "And they came unto the brook of Eshcol, and cut down from thence a branch with one cluster of grapes, and they bare it between two upon a staff; and they brought of the pomegranates, and of the figs.",
      "M": "They came to the valley of Eshcol and cut down from there a branch with a single cluster of grapes, which they carried on a pole between two men; they also brought back pomegranates and figs.",
      "T": "At the valley of Eshcol they found grapes so heavy that one cluster required two men and a carrying-pole. They also brought pomegranates and figs — the land's abundance made tangible."
    },
    "24": {
      "L": "The place was called the brook Eshcol, because of the cluster of grapes which the children of Israel cut down from thence.",
      "M": "That place was called the valley of Eshcol, because of the cluster the Israelites cut down there.",
      "T": "They named the valley Eshcol — Cluster — for that one bunch of grapes that took two men to carry."
    },
    "25": {
      "L": "And they returned from searching the land after forty days.",
      "M": "After forty days they returned from spying out the land.",
      "T": "After forty days in the land, the scouts came home."
    },
    "26": {
      "L": "And they went and came to Moses, and to Aaron, and to all the congregation of the children of Israel, unto the wilderness of Paran, to Kadesh; and brought back word unto them, and unto all the congregation, and shewed them the fruit of the land.",
      "M": "They came to Moses and Aaron and to the whole congregation of Israel in the wilderness of Paran at Kadesh. They brought back word to them and to the whole congregation and showed them the fruit of the land.",
      "T": "They returned to Kadesh in the Paran wilderness and reported to Moses, Aaron, and the whole congregation, setting the land's fruit before everyone."
    },
    "27": {
      "L": "And they told him, and said, We came unto the land whither thou sentest us, and surely it floweth with milk and honey; and this is the fruit of it.",
      "M": "They told Moses: We came to the land you sent us to, and it does indeed flow with milk and honey. Here is its fruit.",
      "T": "'We went to the land you sent us to — it is everything you said. Milk and honey. Here is the proof.' They held up the grapes."
    },
    "28": {
      "L": "Nevertheless the people be strong that dwell in the land, and the cities are walled, and very great: and moreover we saw the children of Anak there.",
      "M": "However, the people living in the land are strong and the cities are large and fortified. We also saw the descendants of Anak there.",
      "T": "But — the people are formidable. Their cities are massive and walled. And we saw Anak's descendants there."
    },
    "29": {
      "L": "The Amalekites dwell in the land of the south: and the Hittites, and the Jebusites, and the Amorites, dwell in the mountains: and the Canaanites dwell by the sea, and by the coast of Jordan.",
      "M": "The Amalekites dwell in the Negeb. The Hittites, Jebusites, and Amorites live in the hill country. The Canaanites dwell by the sea and along the Jordan.",
      "T": "The Amalekites hold the Negeb. The Hittites, Jebusites, and Amorites occupy the hills. The Canaanites hold the coast and the Jordan valley. The land is fully garrisoned."
    },
    "30": {
      "L": "And Caleb stilled the people before Moses, and said, Let us go up at once, and possess it; for we are well able to overcome it.",
      "M": "But Caleb quieted the people before Moses and said, Let us go up at once and occupy it, for we are well able to overcome it.",
      "T": "Caleb cut through the noise: 'We should go up now and take it. We can do this.'"
    },
    "31": {
      "L": "But the men that went up with him said, We be not able to go up against the people; for they are stronger than we.",
      "M": "But the men who had gone up with him said, We are not able to go up against the people, for they are stronger than we are.",
      "T": "The other scouts pushed back: 'We cannot attack those people. They are stronger than we are.'"
    },
    "32": {
      "L": "And they brought up an evil report of the land which they had searched unto the children of Israel, saying, The land, through which we have gone to search it, is a land that eateth up the inhabitants thereof; and all the people that we saw in it are men of a great stature.",
      "M": "So they brought a bad report of the land to the Israelites, saying: The land we traveled through to spy out is a land that devours its inhabitants, and all the people we saw there are of great stature.",
      "T": "They spread a slanderous report through Israel: 'That land eats its own people. Every person we saw was enormous.'"
    },
    "33": {
      "L": "And there we saw the giants, the sons of Anak, which come of the giants: and we were in our own sight as grasshoppers, and so we were in their sight.",
      "M": "We saw the Nephilim there — the descendants of Anak, who come from the Nephilim. We seemed to ourselves like grasshoppers, and so we seemed to them.",
      "T": "We saw the Nephilim — ancient warrior-giants, Anak's line. Standing next to them we felt like grasshoppers. And that is exactly how we looked to them."
    }
  },
  "14": {
    "1": {
      "L": "And all the congregation lifted up their voice, and cried; and the people wept that night.",
      "M": "Then all the congregation raised a loud cry, and the people wept that night.",
      "T": "The whole camp broke into weeping. The cry rose through the night."
    },
    "2": {
      "L": "And all the children of Israel murmured against Moses and against Aaron: and the whole congregation said unto them, Would God that we had died in the land of Egypt! or would God we had died in this wilderness!",
      "M": "All the Israelites grumbled against Moses and Aaron. The whole congregation said to them: If only we had died in the land of Egypt! Or if only we had died in this wilderness!",
      "T": "'Why didn't we die in Egypt? Why not here in the wilderness?' The entire congregation turned on Moses and Aaron."
    },
    "3": {
      "L": "And wherefore hath the LORD brought us unto this land, to fall by the sword, that our wives and our children should be a prey? were it not better for us to return into Egypt?",
      "M": "Why is the LORD bringing us into this land, to fall by the sword? Our wives and children will become prey. Would it not be better to go back to Egypt?",
      "T": "'The LORD is leading us to our deaths. Our families will be taken as plunder. Egypt is better than this.'"
    },
    "4": {
      "L": "And they said one to another, Let us make a captain, and let us return into Egypt.",
      "M": "And they said to one another: Let us appoint a leader and return to Egypt.",
      "T": "They began electing an alternative leader among themselves: 'We are going back to Egypt.'"
    },
    "5": {
      "L": "Then Moses and Aaron fell on their faces before all the assembly of the congregation of the children of Israel.",
      "M": "Then Moses and Aaron fell facedown before the whole assembly of the congregation of Israel.",
      "T": "Moses and Aaron fell facedown before the whole congregation — an act of intercession, not defeat."
    },
    "6": {
      "L": "And Joshua the son of Nun, and Caleb the son of Jephunneh, which were of them that searched the land, rent their clothes:",
      "M": "And Joshua son of Nun and Caleb son of Jephunneh, who were among those who had spied out the land, tore their clothes",
      "T": "Joshua son of Nun and Caleb son of Jephunneh — the two faithful scouts — tore their garments in grief and protest."
    },
    "7": {
      "L": "And they spake unto all the company of the children of Israel, saying, The land, which we passed through to search it, is an exceeding good land.",
      "M": "and said to the whole congregation of Israel: The land we traveled through to spy out is an exceedingly good land.",
      "T": "They cried out to the assembly: 'The land is extraordinarily good. We saw it with our own eyes.'"
    },
    "8": {
      "L": "If the LORD delight in us, then he will bring us into this land, and give it us; a land which floweth with milk and honey.",
      "M": "If the LORD is pleased with us, he will bring us into this land and give it to us — a land that flows with milk and honey.",
      "T": "'If the LORD is with us — and he is — he will bring us into it and give it to us. A land of milk and honey. It is ours to receive.'"
    },
    "9": {
      "L": "Only rebel not ye against the LORD, neither fear ye the people of the land; for they are bread for us: their defence is departed from them, and the LORD is with us: fear them not.",
      "M": "Only do not rebel against the LORD, and do not fear the people of the land, for they are bread for us. Their protection is removed from them, and the LORD is with us. Do not fear them.",
      "T": "'Do not rebel against the LORD. Do not be afraid of those people — they are food for us. Their protection has been stripped away. The LORD is with us. Fear nothing.'"
    },
    "10": {
      "L": "But all the congregation bade stone them with stones. And the glory of the LORD appeared in the tabernacle of the congregation before all the children of Israel.",
      "M": "But the whole congregation said to stone them with stones. Then the glory of the LORD appeared at the tent of meeting to all the Israelites.",
      "T": "The crowd called for their execution. Then the glory of the LORD blazed out at the tent of meeting — seen by all Israel."
    },
    "11": {
      "L": "And the LORD said unto Moses, How long will this people provoke me? and how long will it be ere they believe me, for all the signs which I have shewed among them?",
      "M": "The LORD said to Moses: How long will this people despise me? And how long will they not believe me, in spite of all the signs I have done among them?",
      "T": "The LORD said to Moses: 'How long will this people treat me with contempt? How long before they trust me, after everything they have seen me do?'"
    },
    "12": {
      "L": "I will smite them with the pestilence, and disinherit them, and will make of thee a nation greater and mightier than they.",
      "M": "I will strike them with pestilence and disinherit them, and I will make of you a nation greater and mightier than they.",
      "T": "'I will wipe them out with plague and disown them. From you alone I will build a greater nation.'"
    },
    "13": {
      "L": "And Moses said unto the LORD, Then the Egyptians shall hear it, for thou broughtest up this people in thy might from among them;",
      "M": "But Moses said to the LORD: If you do this, the Egyptians will hear of it — for you brought this people up from among them by your great power —",
      "T": "Moses appealed: 'Wait. Egypt will hear what happened. You brought this people out of Egypt with visible, undeniable power —'"
    },
    "14": {
      "L": "And they will tell it to the inhabitants of this land: for they have heard that thou LORD art among this people, that thou LORD art seen face to face, and that thy cloud standeth over them, and that thou goest before them, by day time in a pillar of a cloud, and in a pillar of fire by night.",
      "M": "and they will tell the inhabitants of this land. They have heard that you, LORD, are in the midst of this people, that you, LORD, are seen face to face, that your cloud stands over them, and that you go before them in a pillar of cloud by day and in a pillar of fire by night.",
      "T": "'— and Canaan's peoples already know. They know you are visibly among Israel: your cloud overhead, your pillar of fire ahead. You have been seen face to face among your people.'"
    },
    "15": {
      "L": "Now if thou shalt kill all this people as one man, then the nations which have heard the fame of thee will speak, saying,",
      "M": "If you kill this people as one man, then the nations who have heard your fame will say,",
      "T": "'If you destroy all Israel at a stroke, every nation that has heard your name will draw one conclusion:'"
    },
    "16": {
      "L": "Because the LORD was not able to bring this people into the land which he sware unto them, therefore he hath slain them in the wilderness.",
      "M": "The LORD was not able to bring this people into the land he swore to give to them, and so he has killed them in the wilderness.",
      "T": "'He could not deliver what he promised. He abandoned them in the wilderness.' Your name will be mocked among the nations."
    },
    "17": {
      "L": "And now, I beseech thee, let the power of my Lord be great, according as thou hast spoken, saying,",
      "M": "And now, please let the power of the Lord be great as you have promised, saying,",
      "T": "Moses pressed on: 'Now let your power be shown as great — shown in exactly the way you yourself declared at Sinai:'"
    },
    "18": {
      "L": "The LORD is longsuffering, and of great mercy, forgiving iniquity and transgression, and by no means clearing the guilty, visiting the iniquity of the fathers upon the children unto the third and fourth generation.",
      "M": "The LORD is slow to anger and abounding in steadfast love, forgiving iniquity and transgression, but by no means clearing the guilty, visiting the iniquity of the fathers on the children to the third and fourth generation.",
      "T": "'The LORD is slow to anger and rich in covenant love — forgiving iniquity and rebellion, yet never leaving guilt unaddressed, its weight passing through three and four generations.' Moses quoted the Sinai covenant formula back to God."
    },
    "19": {
      "L": "Pardon, I beseech thee, the iniquity of this people according unto the greatness of thy mercy, and as thou hast forgiven this people, from Egypt even until now.",
      "M": "Please pardon the iniquity of this people according to the greatness of your steadfast love, just as you have forgiven this people from Egypt until now.",
      "T": "'Pardon their iniquity — let your covenant love be equal to the moment, as it has been from Egypt to this day.'"
    },
    "20": {
      "L": "And the LORD said, I have pardoned according to thy word:",
      "M": "The LORD said: I have pardoned, according to your word.",
      "T": "The LORD answered: 'I have pardoned them, as you asked.'"
    },
    "21": {
      "L": "But as truly as I live, all the earth shall be filled with the glory of the LORD:",
      "M": "But as I live, and as all the earth shall be filled with the glory of the LORD,",
      "T": "'But hear this: as truly as I live, the whole earth will one day be filled with my glory —'"
    },
    "22": {
      "L": "Because all those men which have seen my glory, and my miracles, which I did in Egypt and in the wilderness, and have tempted me now these ten times, and have not hearkened to my voice;",
      "M": "none of the men who have seen my glory and my signs that I did in Egypt and in the wilderness, and yet have tested me these ten times and not obeyed my voice,",
      "T": "'— none of those who saw my glory in Egypt, who witnessed my signs in the wilderness, and who have tested me ten times now, defying my voice each time —'"
    },
    "23": {
      "L": "Surely they shall not see the land which I sware unto their fathers, neither shall any of them that provoked me see it:",
      "M": "shall see the land I swore to give to their fathers. None of those who despised me shall see it.",
      "T": "'— not one of those contemptuous people will set foot in the land I swore to their ancestors. They will not see it.'"
    },
    "24": {
      "L": "But my servant Caleb, because he had another spirit with him, and hath followed me fully, him will I bring into the land whereinto he went; and his seed shall possess it.",
      "M": "But my servant Caleb, because he has a different spirit and has followed me fully, I will bring into the land where he went, and his descendants shall possess it.",
      "T": "'Caleb is different. He has a different spirit — one of trust and full allegiance. He followed me without reservation. I will bring him into the very land he scouted, and his descendants will inherit it.'"
    },
    "25": {
      "L": "Now the Amalekites and the Canaanites dwelt in the valley. To morrow turn ye, and get you into the wilderness by the way of the Red sea.",
      "M": "Since the Amalekites and the Canaanites dwell in the valleys, turn back tomorrow and set out for the wilderness by the way to the Red Sea.",
      "T": "The Amalekites and Canaanites hold the valleys — the direct route to Canaan is blocked. Turn back; head toward the wilderness and the Red Sea."
    },
    "26": {
      "L": "And the LORD spake unto Moses and unto Aaron, saying,",
      "M": "The LORD spoke to Moses and Aaron, saying,",
      "T": "The LORD spoke to Moses and Aaron:"
    },
    "27": {
      "L": "How long shall I bear with this evil congregation, which murmur against me? I have heard the murmurings of the children of Israel, which they murmur against me.",
      "M": "How long shall I bear with this wicked congregation that grumbles against me? I have heard the grumbling of the Israelites, which they grumble against me.",
      "T": "'How long must I endure this? This community's grumbling has reached me again — aimed directly against me.'"
    },
    "28": {
      "L": "Say unto them, As truly as I live, saith the LORD, as ye have spoken in mine ears, so will I do to you:",
      "M": "Say to them: As I live, declares the LORD, I will do to you just what you have said in my hearing:",
      "T": "'Tell them: as I live — the LORD's own word — I will give them precisely what they demanded in my hearing.'"
    },
    "29": {
      "L": "Your carcases shall fall in this wilderness; and all that were numbered of you, according to your whole number, from twenty years old and upward, which have murmured against me,",
      "M": "your dead bodies shall fall in this wilderness, and of all your number who were registered in the census from twenty years old and upward, who have grumbled against me —",
      "T": "'Every person twenty and older who was registered and who grumbled against me — their bodies will lie in this wilderness.'"
    },
    "30": {
      "L": "Doubtless ye shall not come into the land, concerning which I sware to make you dwell therein, save Caleb the son of Jephunneh, and Joshua the son of Nun.",
      "M": "Not one of you shall come into the land where I swore to settle you — except Caleb son of Jephunneh and Joshua son of Nun.",
      "T": "Not one of them will enter the promised land — except Caleb son of Jephunneh and Joshua son of Nun."
    },
    "31": {
      "L": "But your little ones, which ye said should be a prey, them will I bring in, and they shall know the land which ye have despised.",
      "M": "But your little ones, who you said would become prey — I will bring them in, and they shall know the land you have rejected.",
      "T": "'The children you said would become plunder — they will enter. They will know and inhabit the land their parents despised.'"
    },
    "32": {
      "L": "But as for you, your carcases, they shall fall in this wilderness.",
      "M": "But as for you, your dead bodies shall fall in this wilderness.",
      "T": "The parents: their bones will bleach in this wilderness."
    },
    "33": {
      "L": "And your children shall wander in the wilderness forty years, and bear your whoredoms, until your carcases be wasted in the wilderness.",
      "M": "Your children shall wander in the wilderness for forty years and shall bear the weight of your faithlessness, until the last of your dead bodies lies in the wilderness.",
      "T": "Their children will wander forty years, bearing the consequence of their parents' infidelity — until the last faithless body is gone."
    },
    "34": {
      "L": "After the number of the days in which ye searched the land, even forty days, each day for a year, shall ye bear your iniquities, even forty years, and ye shall know my breach of promise.",
      "M": "According to the number of days you spied out the land — forty days — a year for each day, you shall bear your iniquity for forty years, and you shall know the cost of opposing me.",
      "T": "Forty days of scouting: forty years of consequence. One year per day. They will learn, at length, what it costs to oppose the LORD."
    },
    "35": {
      "L": "I the LORD have said, I will surely do it unto all this evil congregation, that are gathered together against me: in this wilderness they shall be consumed, and there they shall die.",
      "M": "I, the LORD, have spoken. Surely I will do this to all this wicked congregation gathered together against me: in this wilderness they shall come to a full end, and there they shall die.",
      "T": "The LORD has spoken it and will not retract it: every person in this rebellious community who united against him — they will be worn down to nothing in this wilderness. Here they will die."
    },
    "36": {
      "L": "And the men, which Moses sent to search the land, who returned, and made all the congregation to murmur against him, by bringing up a slander upon the land,",
      "M": "The men Moses sent to spy out the land, who returned and made the whole congregation grumble against him by bringing back a bad report about the land —",
      "T": "The scouts who brought back the slanderous report — who ignited the whole congregation's rebellion against Moses —"
    },
    "37": {
      "L": "Even those men that did bring up the evil report upon the land, died by the plague before the LORD.",
      "M": "those men who brought up a bad report about the land died by plague before the LORD.",
      "T": "— were struck by plague and died before the LORD. The punishment was immediate."
    },
    "38": {
      "L": "But Joshua the son of Nun, and Caleb the son of Jephunneh, which were of the men that went to search the land, lived still.",
      "M": "Of those men who went to spy out the land, only Joshua son of Nun and Caleb son of Jephunneh remained alive.",
      "T": "Only Joshua and Caleb survived among the scouts — the two who had refused to lie."
    },
    "39": {
      "L": "And Moses told these sayings unto all the children of Israel: and the people mourned greatly.",
      "M": "Moses told these words to all the Israelites, and the people mourned greatly.",
      "T": "When Moses delivered the LORD's verdict to Israel, the grief was overwhelming."
    },
    "40": {
      "L": "And they rose up early in the morning, and gat them up into the top of the mountain, saying, Lo, we be here, and will go up unto the place which the LORD hath promised: for we have sinned.",
      "M": "They rose early in the morning and went up toward the heights of the hill country, saying: Here we are. We will go up to the place the LORD promised, for we have sinned.",
      "T": "By morning they had reversed course: 'We were wrong. We will go up to the land the LORD promised.' They started climbing toward Canaan."
    },
    "41": {
      "L": "And Moses said, Wherefore now do ye transgress the commandment of the LORD? but it shall not prosper.",
      "M": "But Moses said: Why are you now transgressing the LORD's command? This will not succeed.",
      "T": "Moses warned them: 'Why do you transgress the LORD's command now? It is too late. This will not succeed.'"
    },
    "42": {
      "L": "Go not up, for the LORD is not among you; that ye be not smitten before your enemies.",
      "M": "Do not go up, for the LORD is not among you, lest you be struck down before your enemies.",
      "T": "'Do not go. The LORD is not with you. You will be cut down by your enemies.'"
    },
    "43": {
      "L": "For the Amalekites and the Canaanites are there before you, and ye shall fall by the sword: because ye are turned away from the LORD, therefore the LORD will not be with you.",
      "M": "For the Amalekites and the Canaanites are there before you, and you shall fall by the sword. Because you have turned back from the LORD, the LORD will not be with you.",
      "T": "'The Amalekites and Canaanites are waiting ahead of you. You have turned away from the LORD, and the LORD has withdrawn from you. The sword is what you will meet.'"
    },
    "44": {
      "L": "But they presumed to go up unto the hill top: nevertheless the ark of the covenant of the LORD, and Moses, departed not out of the camp.",
      "M": "But they presumed to go up to the heights of the hill country, even though the ark of the covenant of the LORD and Moses had not left the camp.",
      "T": "They went anyway — presumptuously, without the ark, without Moses, without the LORD. They marched toward disaster."
    },
    "45": {
      "L": "Then the Amalekites came down, and the Canaanites which dwelt in that hill, and smote them, and discomfited them, even unto Hormah.",
      "M": "Then the Amalekites and the Canaanites who lived in that hill country came down and defeated them, driving them back as far as Hormah.",
      "T": "The Amalekites and Canaanites swarmed down and crushed them — routing Israel all the way to Hormah."
    }
  },
  "15": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto the children of Israel, and say unto them, When ye be come into the land of your habitations, which I give unto you,",
      "M": "Speak to the Israelites and say to them: When you come into the land you are to inhabit, which I am giving you,",
      "T": "Tell the Israelites: When you enter the land I am giving you as your home —"
    },
    "3": {
      "L": "And will make an offering by fire unto the LORD, a burnt offering, or a sacrifice in performing a vow, or in a freewill offering, or in your solemn feasts, to make a sweet savour unto the LORD, of the herd, or of the flock:",
      "M": "and you make a food offering by fire to the LORD — a burnt offering, or a sacrifice to fulfill a vow, or a freewill offering, or at your appointed festivals — to produce a pleasing aroma to the LORD, from herd or flock,",
      "T": "when you offer a fire offering to the LORD — burnt offering, vow fulfillment, freewill offering, or festival sacrifice — from herd or flock, a pleasing aroma before the LORD —"
    },
    "4": {
      "L": "Then shall he that offereth his offering unto the LORD bring a meat offering of a tenth deal of flour mingled with the fourth part of an hin of oil.",
      "M": "the one presenting the offering shall bring a grain offering of one-tenth of an ephah of fine flour mixed with one-quarter of a hin of oil.",
      "T": "— the accompanying grain offering is one-tenth of an ephah of fine flour mixed with a quarter hin of oil."
    },
    "5": {
      "L": "And the fourth part of an hin of wine for a drink offering shalt thou prepare with the burnt offering or sacrifice, for one lamb.",
      "M": "Also prepare a quarter of a hin of wine for a drink offering to accompany the burnt offering or sacrifice for each lamb.",
      "T": "Add a quarter hin of wine as a drink offering alongside each lamb."
    },
    "6": {
      "L": "Or for a ram, thou shalt prepare for a meat offering two tenth deals of flour mingled with the third part of an hin of oil.",
      "M": "For a ram, prepare a grain offering of two-tenths of an ephah of fine flour mixed with one-third of a hin of oil,",
      "T": "For a ram: two-tenths of an ephah of fine flour, one-third hin of oil —"
    },
    "7": {
      "L": "And for a drink offering thou shalt offer the third part of an hin of wine, for a sweet savour unto the LORD.",
      "M": "and for a drink offering offer one-third of a hin of wine, a pleasing aroma to the LORD.",
      "T": "— and a third hin of wine as a drink offering, a pleasing aroma to the LORD."
    },
    "8": {
      "L": "And when thou preparest a bullock for a burnt offering, or for a sacrifice in performing a vow, or peace offerings unto the LORD:",
      "M": "When you prepare a young bull as a burnt offering, or a sacrifice to fulfill a vow, or as a fellowship offering to the LORD,",
      "T": "When the offering is a bull — burnt offering, vow fulfillment, or fellowship offering —"
    },
    "9": {
      "L": "Then shall he bring with a bullock a meat offering of three tenth deals of flour mingled with half an hin of oil.",
      "M": "bring with the bull a grain offering of three-tenths of an ephah of fine flour mixed with half a hin of oil,",
      "T": "— bring three-tenths of an ephah of fine flour mixed with half a hin of oil,"
    },
    "10": {
      "L": "And thou shalt bring for a drink offering half an hin of wine, for an offering made by fire, of a sweet savour unto the LORD.",
      "M": "and for a drink offering bring half a hin of wine, a food offering, a pleasing aroma to the LORD.",
      "T": "— and half a hin of wine as a drink offering. A pleasing aroma before the LORD."
    },
    "11": {
      "L": "Thus shall it be done for one bullock, or for one ram, or for a lamb, or a kid.",
      "M": "This shall be done for each bull, each ram, and each lamb or goat.",
      "T": "These proportions apply to each animal — bull, ram, lamb, or goat."
    },
    "12": {
      "L": "According to the number that ye shall prepare, so shall ye do to every one according to their number.",
      "M": "Whatever the number of animals you offer, do this for each one according to their number.",
      "T": "Multiply the proportions by the number of animals. Every offering receives its full accompaniment."
    },
    "13": {
      "L": "All that are born of the country shall do these things after this manner, in offering an offering made by fire, of a sweet savour unto the LORD.",
      "M": "Every native Israelite shall follow this procedure when presenting a food offering of pleasing aroma to the LORD.",
      "T": "Every native-born Israelite who brings a fire offering to the LORD follows these rules."
    },
    "14": {
      "L": "And if a stranger sojourn with you, or whosoever be among you in your generations, and will offer an offering made by fire, of a sweet savour unto the LORD; as ye do, so he shall do.",
      "M": "And if a resident alien living among you, or anyone else with you throughout your generations, presents a food offering of pleasing aroma to the LORD, he shall do just as you do.",
      "T": "If a foreigner living among you — in any generation — brings a fire offering to the LORD, the same procedure applies."
    },
    "15": {
      "L": "One ordinance shall be both for you of the congregation, and also for the stranger that sojourneth with you, an ordinance for ever in your generations: as ye are, so shall the stranger be before the LORD.",
      "M": "There shall be one statute for the congregation — for you and for the resident alien living with you — a permanent statute throughout your generations. Before the LORD, the resident alien shall be the same as you.",
      "T": "One law, one standard — for the native-born and the resident alien alike, permanent through every generation. Before the LORD, the foreigner stands equal to the native Israelite."
    },
    "16": {
      "L": "One law and one manner shall be for you, and for the stranger that sojourneth with you.",
      "M": "One law and one rule shall apply to you and to the resident alien living among you.",
      "T": "One law. One ordinance. No distinction at the altar."
    },
    "17": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "18": {
      "L": "Speak unto the children of Israel, and say unto them, When ye come into the land whither I bring you,",
      "M": "Speak to the Israelites and say to them: When you come into the land to which I am bringing you",
      "T": "Tell the Israelites: When you enter the land I am bringing you into,"
    },
    "19": {
      "L": "Then it shall be, that, when ye eat of the bread of the land, ye shall offer up an heave offering unto the LORD.",
      "M": "and you eat from the produce of the land, you shall present a contribution as a gift to the LORD.",
      "T": "when you eat the land's grain, set aside a contribution for the LORD."
    },
    "20": {
      "L": "Ye shall offer up a cake of the first of your dough for an heave offering: as ye do the heave offering of the threshingfloor, so shall ye heave it.",
      "M": "From the first of your dough you shall present a loaf as a contribution — as with the contribution from the threshing floor, you shall present it.",
      "T": "From the first batch of dough, bring a loaf as a contribution — the same principle as the threshing-floor firstfruits."
    },
    "21": {
      "L": "Of the first of your dough ye shall give unto the LORD an heave offering in your generations.",
      "M": "From the first of your dough you shall give the LORD a contribution throughout your generations.",
      "T": "In every generation: the first bread belongs to the LORD."
    },
    "22": {
      "L": "And if ye have erred, and not observed all these commandments, which the LORD hath spoken unto Moses,",
      "M": "But if you sin unintentionally and do not observe all these commandments that the LORD spoke to Moses —",
      "T": "If the community sins unintentionally — failing to observe some commandment the LORD gave through Moses —"
    },
    "23": {
      "L": "Even all that the LORD hath commanded you by the hand of Moses, from the day that the LORD commanded Moses, and henceforward among your generations;",
      "M": "all that the LORD commanded you through Moses, from the day the LORD gave the command and onward throughout your generations —",
      "T": "— any of the LORD's commands given through Moses, from the beginning onward through every generation —"
    },
    "24": {
      "L": "Then it shall be, if ought be committed by ignorance without the knowledge of the congregation, that all the congregation shall offer one young bullock for a burnt offering, for a sweet savour unto the LORD, with his meat offering, and his drink offering, according to the manner, and one kid of the goats for a sin offering.",
      "M": "if it was done unintentionally, without the congregation's knowledge, then the whole congregation shall offer one young bull for a burnt offering as a pleasing aroma to the LORD, with its prescribed grain offering and drink offering, and one male goat for a sin offering.",
      "T": "if this happened without the community realizing it, the whole congregation shall offer one bull as a burnt offering with its grain and drink offering, and one male goat as a sin offering. The community bears the unintentional mistake together."
    },
    "25": {
      "L": "And the priest shall make an atonement for all the congregation of the children of Israel, and it shall be forgiven them; for it is ignorance: and they shall bring their offering, a sacrifice made by fire unto the LORD, and their sin offering before the LORD, for their ignorance:",
      "M": "The priest shall make atonement for the whole congregation of Israel, and they shall be forgiven, for it was unintentional. They shall bring their offering — a food offering to the LORD — and their sin offering before the LORD for their unintentional sin.",
      "T": "The priest makes atonement for the whole community and they receive forgiveness — because it was unintentional. The sacrifice covers the community's accidental failure."
    },
    "26": {
      "L": "And it shall be forgiven all the congregation of the children of Israel, and the stranger that sojourneth among them; seeing all the people were in ignorance.",
      "M": "The whole congregation of Israel shall be forgiven, along with the resident alien living among them, since all the people acted unintentionally.",
      "T": "The entire community is forgiven — native Israelite and resident foreigner alike. When the failure was genuinely unintentional, the atonement covers everyone."
    },
    "27": {
      "L": "And if any soul sin through ignorance, then he shall bring a she goat of the first year for a sin offering.",
      "M": "If only one person sins unintentionally, that person shall bring a yearling female goat for a sin offering.",
      "T": "If an individual sins unintentionally, they bring a yearling female goat as a sin offering."
    },
    "28": {
      "L": "And the priest shall make an atonement for the soul that sinneth ignorantly, when he sinneth by ignorance before the LORD, to make an atonement for him; and it shall be forgiven him.",
      "M": "The priest shall make atonement before the LORD for the person who sinned unintentionally, making atonement for that person, and he or she shall be forgiven.",
      "T": "The priest makes atonement for the individual and they receive forgiveness. The provision for unintentional sin exists precisely to be used."
    },
    "29": {
      "L": "Ye shall have one law for him that sinneth through ignorance, both for him that is born among the children of Israel, and for the stranger that sojourneth among them.",
      "M": "You shall have one law for the person who acts unintentionally, whether native-born among the Israelites or a resident alien living among them.",
      "T": "One provision covers everyone: the same law for the unintentional failure of the native-born and the sojourner alike."
    },
    "30": {
      "L": "But the soul that doeth ought presumptuously, whether he be born in the land, or a stranger, the same reproacheth the LORD; and that soul shall be cut off from among his people.",
      "M": "But the person who acts defiantly, whether native-born or a resident alien — that person blasphemes the LORD and shall be cut off from among the people.",
      "T": "But deliberate defiance is different. Anyone — Israelite or foreigner — who acts with a raised fist against the LORD treats him with contempt. That person is cut off from Israel."
    },
    "31": {
      "L": "Because he hath despised the word of the LORD, and hath broken his commandment, that soul shall utterly be cut off; his iniquity shall be upon him.",
      "M": "Because he has despised the word of the LORD and broken his commandment, that person shall be utterly cut off; his guilt is upon him.",
      "T": "They despised the LORD's word and broke his commandment deliberately. Cut off completely. The guilt stays with them."
    },
    "32": {
      "L": "And while the children of Israel were in the wilderness, they found a man that gathered sticks upon the sabbath day.",
      "M": "While the Israelites were in the wilderness, they found a man gathering wood on the Sabbath day.",
      "T": "While Israel was still in the wilderness, a man was found gathering firewood on the Sabbath."
    },
    "33": {
      "L": "And they that found him gathering sticks brought him unto Moses and Aaron, and unto all the congregation.",
      "M": "Those who found him gathering wood brought him to Moses and Aaron and to the whole congregation.",
      "T": "He was brought before Moses, Aaron, and the whole community."
    },
    "34": {
      "L": "And they put him in ward, because it was not declared what should be done to him.",
      "M": "They put him in custody, because it had not been made clear what should be done to him.",
      "T": "They held him in custody while waiting for the LORD's ruling — the specific penalty had not yet been stated."
    },
    "35": {
      "L": "And the LORD said unto Moses, The man shall be surely put to death: all the congregation shall stone him with stones without the camp.",
      "M": "The LORD said to Moses: The man shall be put to death; the whole congregation shall stone him with stones outside the camp.",
      "T": "The LORD ruled: death. The whole community will stone him outside the camp."
    },
    "36": {
      "L": "And all the congregation brought him without the camp, and stoned him with stones, and he died; as the LORD commanded Moses.",
      "M": "So all the congregation brought him outside the camp and stoned him to death, as the LORD had commanded Moses.",
      "T": "The community carried out the sentence outside the camp. The Sabbath boundary was absolute, and the cost of treating it otherwise was absolute."
    },
    "37": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "38": {
      "L": "Speak unto the children of Israel, and bid them that they make them fringes in the borders of their garments throughout their generations, and that they put upon the fringe of the borders a ribband of blue:",
      "M": "Speak to the Israelites and tell them to make tassels on the corners of their garments throughout their generations, and to put a blue cord on the tassel of each corner.",
      "T": "Tell Israel: sew tassels on the corners of every garment — in every generation — and thread a blue cord through each tassel."
    },
    "39": {
      "L": "And it shall be unto you for a fringe, that ye may look upon it, and remember all the commandments of the LORD, and do them; and that ye seek not after your own heart and your own eyes, after which ye use to go a whoring:",
      "M": "The tassels shall be for you to look at, so that you may remember all the LORD's commandments and do them, and not follow your own heart and eyes, which lead you astray.",
      "T": "You will see the tassels and remember every commandment of the LORD — and keep them. They are a check on the heart and the eyes, which tend to chase after what is forbidden."
    },
    "40": {
      "L": "That ye may remember, and do all my commandments, and be holy unto your God.",
      "M": "So you shall remember and do all my commandments, and you shall be holy to your God.",
      "T": "Remembering leads to obedience; obedience leads to holiness — being set apart for the LORD your God."
    },
    "41": {
      "L": "I am the LORD your God, which brought you out of the land of Egypt, to be your God: I am the LORD your God.",
      "M": "I am the LORD your God, who brought you out of the land of Egypt to be your God. I am the LORD your God.",
      "T": "I am the LORD your God — the one who brought you out of Egypt to be your God. I am the LORD your God."
    }
  },
  "16": {
    "1": {
      "L": "Now Korah, the son of Izhar, the son of Kohath, the son of Levi, and Dathan and Abiram, the sons of Eliab, and On the son of Peleth, sons of Reuben, took men:",
      "M": "Now Korah son of Izhar son of Kohath son of Levi, and Dathan and Abiram sons of Eliab, and On son of Peleth — sons of Reuben — took action.",
      "T": "Korah son of Izhar, a Kohathite Levite, joined with Dathan and Abiram sons of Eliab, and On son of Peleth — Reubenites — and mounted a challenge."
    },
    "2": {
      "L": "And they rose up before Moses, with certain of the children of Israel, two hundred and fifty princes of the congregation, famous in the congregation, men of renown:",
      "M": "They rose up against Moses, together with 250 Israelites who were leaders of the congregation — men called to the assembly, men of repute.",
      "T": "With them came 250 leading men of Israel — established names, known voices in the assembly. Together they confronted Moses."
    },
    "3": {
      "L": "And they gathered themselves together against Moses and against Aaron, and said unto them, Ye take too much upon you, seeing all the congregation are holy, every one of them, and the LORD is among them: wherefore then lift ye up yourselves above the congregation of the LORD?",
      "M": "They assembled against Moses and Aaron and said to them: You have gone too far! The whole congregation is holy, every one of them, and the LORD is in their midst. Why then do you exalt yourselves above the assembly of the LORD?",
      "T": "'You have overstepped,' they charged. 'Every person in this congregation is holy. The LORD is among all of us equally. Who made you leaders over the LORD's people?'"
    },
    "4": {
      "L": "And when Moses heard it, he fell upon his face:",
      "M": "When Moses heard this, he fell facedown.",
      "T": "Moses's response to the challenge: he fell on his face before the LORD."
    },
    "5": {
      "L": "And he spake unto Korah and unto all his company, saying, Even to morrow the LORD will shew who are his, and who is holy; and will cause him to come near unto him: even him whom he hath chosen will he cause to come near unto him.",
      "M": "Then he spoke to Korah and all his company, saying: Tomorrow morning the LORD will show who is his and who is holy, and will bring that person near to himself. The one he chooses he will bring near.",
      "T": "He said to Korah and his company: 'Wait until morning. The LORD himself will show who belongs to him, who is truly holy, who he has chosen. He will draw that person near.'"
    },
    "6": {
      "L": "This do; Take you censers, Korah, and all his company;",
      "M": "Do this: take censers, Korah and all your company,",
      "T": "Moses set the terms of the test: 'You want the priesthood? Very well — take your incense pans, Korah and all your company.'"
    },
    "7": {
      "L": "And put fire therein, and put incense in them before the LORD to morrow: and it shall be that the man whom the LORD doth choose, he shall be holy: ye take too much upon you, ye sons of Levi.",
      "M": "put fire in them and place incense on them before the LORD tomorrow. The man the LORD chooses shall be the holy one. It is you Levites who have gone too far.",
      "T": "'Stand before the LORD tomorrow with fire and incense. The man the LORD chooses as holy — that will settle who belongs at the altar. It is you Levites who have gone too far.'"
    },
    "8": {
      "L": "And Moses said unto Korah, Hear, I pray you, ye sons of Levi:",
      "M": "Moses also said to Korah: Listen now, you sons of Levi.",
      "T": "Then Moses spoke directly to Korah: 'Sons of Levi — listen carefully.'"
    },
    "9": {
      "L": "Seemeth it but a small thing unto you, that the God of Israel hath separated you from the congregation of Israel, to bring you near to himself to do the service of the tabernacle of the LORD, and to stand before the congregation to minister unto them?",
      "M": "Is it too small a thing for you that the God of Israel has separated you from the congregation of Israel to bring you near to himself — to do the service of the tabernacle of the LORD and to stand before the congregation to minister to them?",
      "T": "'Is what you already have not enough? The God of Israel separated you from all Israel and brought you near to himself — to serve at his tabernacle, to stand before the whole community on their behalf. That is an extraordinary honor.'"
    },
    "10": {
      "L": "And he hath brought thee near to him, and all thy brethren the sons of Levi with thee: and seek ye the priesthood also?",
      "M": "He has brought you near, and all your fellow Levites with you. And yet you seek the priesthood too?",
      "T": "'He brought you near — all of you, the entire Levite tribe. And now you want the priesthood as well? Where does the ambition end?'"
    },
    "11": {
      "L": "For which cause both thou and all thy company are gathered together against the LORD: and what is Aaron, that ye murmur against him?",
      "M": "Therefore it is against the LORD that you and all your company have gathered. For what is Aaron, that you grumble against him?",
      "T": "'Your quarrel is not with Aaron. It is with the LORD who chose him. Aaron is nothing by himself — your anger is aimed at God.'"
    },
    "12": {
      "L": "And Moses sent to call Dathan and Abiram, the sons of Eliab: which said, We will not come up:",
      "M": "Moses summoned Dathan and Abiram sons of Eliab, but they said: We will not come up.",
      "T": "Moses sent for Dathan and Abiram. Their answer: 'We refuse to come.'"
    },
    "13": {
      "L": "Is it a small thing that thou hast brought us up out of a land that floweth with milk and honey, to kill us in the wilderness, except thou make thyself altogether a prince over us?",
      "M": "Is it too small a thing that you have brought us up out of a land flowing with milk and honey to kill us in the wilderness? Must you also make yourself a ruler over us?",
      "T": "'Was it not enough to drag us out of Egypt — the land of milk and honey — to die in this wilderness? Now you want to rule over us as well?'"
    },
    "14": {
      "L": "Moreover thou hast not brought us into a land that floweth with milk and honey, or given us inheritance of fields and vineyards: wilt thou put out the eyes of these men? we will not come up.",
      "M": "You have not brought us into a land flowing with milk and honey, nor have you given us an inheritance of fields and vineyards. Do you think you can blind these men? We will not come up.",
      "T": "'You have not delivered a promised land. No fields, no vineyards. Do you think you can deceive us forever? We are not coming.'"
    },
    "15": {
      "L": "And Moses was very wroth, and said unto the LORD, Respect not thou their offering: I have not taken one ass from them, neither have I hurt one of them.",
      "M": "Then Moses was very angry and said to the LORD: Do not accept their offering. I have not taken one donkey from them, nor have I harmed one of them.",
      "T": "Moses was furious. He prayed: 'LORD, do not accept their offering. I have not taken so much as a donkey from any of them. I have not wronged a single person.'"
    },
    "16": {
      "L": "And Moses said unto Korah, Be thou and all thy company before the LORD, thou, and they, and Aaron, to morrow:",
      "M": "Moses said to Korah: Tomorrow you and all your company shall appear before the LORD — you and they and Aaron.",
      "T": "Moses addressed Korah: 'Tomorrow. You, your whole company, and Aaron — all before the LORD.'"
    },
    "17": {
      "L": "And take every man his censer, and put incense in them, and bring ye before the LORD every man his censer, two hundred and fifty censers; thou also, and Aaron, each of you his censer.",
      "M": "Each man shall take his censer, put incense in it, and bring his censer before the LORD — 250 censers in all, together with yours and Aaron's, each with his own.",
      "T": "'Each man brings his own incense pan with incense burning — 250 pans, plus yours and Aaron's. Every man presents himself, and the LORD decides.'"
    },
    "18": {
      "L": "And they took every man his censer, and put fire in them, and laid incense thereon, and stood in the door of the tabernacle of the congregation with Moses and Aaron.",
      "M": "So each man took his censer, put fire in it, placed incense on it, and stood at the entrance of the tent of meeting with Moses and Aaron.",
      "T": "The 250 men each lit their censers and took their place at the entrance of the tent of meeting with Moses and Aaron. The test was set."
    },
    "19": {
      "L": "And Korah gathered all the congregation against them unto the door of the tabernacle of the congregation: and the glory of the LORD appeared unto all the congregation.",
      "M": "Korah gathered the whole congregation against them at the entrance of the tent of meeting. And the glory of the LORD appeared to the whole congregation.",
      "T": "Korah assembled the whole congregation at the tent of meeting entrance — as if numbers would sway the verdict. Then the glory of the LORD blazed out before all of them."
    },
    "20": {
      "L": "And the LORD spake unto Moses and unto Aaron, saying,",
      "M": "The LORD spoke to Moses and Aaron, saying,",
      "T": "The LORD spoke to Moses and Aaron:"
    },
    "21": {
      "L": "Separate yourselves from among this congregation, that I may consume them in a moment.",
      "M": "Separate yourselves from this congregation so that I may consume them in an instant.",
      "T": "'Step away from this congregation. I am about to consume them in a moment.'"
    },
    "22": {
      "L": "And they fell upon their faces, and said, O God, the God of the spirits of all flesh, shall one man sin, and wilt thou be wroth with all the congregation?",
      "M": "But they fell facedown and said: O God, the God of the spirits of all flesh, shall one man sin and you be angry with the whole congregation?",
      "T": "Moses and Aaron fell facedown and prayed: 'O God — God who holds the life-breath of every person — when one man sins, must the whole congregation bear it?'"
    },
    "23": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "24": {
      "L": "Speak unto the congregation, saying, Get you up from about the tabernacle of Korah, Dathan, and Abiram.",
      "M": "Tell the congregation to move away from the dwellings of Korah, Dathan, and Abiram.",
      "T": "'Warn the congregation: clear away from the tents of Korah, Dathan, and Abiram.'"
    },
    "25": {
      "L": "And Moses rose up and went unto Dathan and Abiram; and the elders of Israel followed him.",
      "M": "Moses rose and went to Dathan and Abiram, and the elders of Israel followed him.",
      "T": "Moses went straight to Dathan and Abiram, the elders of Israel walking with him."
    },
    "26": {
      "L": "And he spake unto the congregation, saying, Depart, I pray you, from the tents of these wicked men, and touch nothing of theirs, lest ye be consumed in all their sins.",
      "M": "He spoke to the congregation, saying: Move away from the tents of these wicked men and touch nothing that belongs to them, lest you be swept away in all their sins.",
      "T": "He called to the congregation: 'Get away from these men's tents. Touch nothing of theirs. If you stay near, their punishment may sweep you away with them.'"
    },
    "27": {
      "L": "So they gat up from the tabernacle of Korah, Dathan, and Abiram, on every side: and Dathan and Abiram came out, and stood in the door of their tents, and their wives, and their sons, and their little children.",
      "M": "So they moved away from the dwellings of Korah, Dathan, and Abiram on every side. And Dathan and Abiram came out and stood at the entrance of their tents, together with their wives, their sons, and their little children.",
      "T": "The congregation drew back on all sides. Dathan and Abiram stepped out and stood defiantly at their tent doors — their wives, sons, and small children gathered around them."
    },
    "28": {
      "L": "And Moses said, Hereby ye shall know that the LORD hath sent me to do all these works; for I have not done them of mine own mind.",
      "M": "Moses said: By this you shall know that the LORD has sent me to do all these works, and that it has not been of my own accord:",
      "T": "Moses addressed all Israel: 'This is how you will know the LORD sent me — and that none of this has been my own idea:'"
    },
    "29": {
      "L": "If these men die the common death of all men, or if they be visited after the visitation of all men; then the LORD hath not sent me.",
      "M": "If these men die the common death of all mankind, or if they are visited by the fate that comes to all, then the LORD has not sent me.",
      "T": "'If these men die ordinary deaths — the kind every human being dies — then the LORD did not send me.'"
    },
    "30": {
      "L": "But if the LORD make a new thing, and the earth open her mouth, and swallow them up, with all that appertain unto them, and they go down quick into the pit; then ye shall understand that these men have provoked the LORD.",
      "M": "But if the LORD creates something entirely new — if the ground opens its mouth and swallows them with all that belongs to them, so that they go down alive into Sheol — then you will know that these men have despised the LORD.",
      "T": "'But if the LORD does something unprecedented — if the ground opens and swallows them alive, descending to Sheol with everything that is theirs — then you will know for certain these men have defied the LORD.'"
    },
    "31": {
      "L": "And it came to pass, as he had made an end of speaking all these words, that the ground clave asunder that was under them:",
      "M": "As soon as he finished speaking all these words, the ground under them split apart.",
      "T": "The moment Moses finished speaking, the ground split open beneath them."
    },
    "32": {
      "L": "And the earth opened her mouth, and swallowed them up, and their houses, and all the men that appertained unto Korah, and all their goods.",
      "M": "The earth opened its mouth and swallowed them up, along with their households, all the people belonging to Korah, and all their possessions.",
      "T": "The earth swallowed them — tents, households, every person and possession attached to Korah."
    },
    "33": {
      "L": "They, and all that appertained to them, went down alive into the pit, and the earth closed upon them: and they perished from among the congregation.",
      "M": "They went down alive into Sheol, they and all who belonged to them. The earth closed over them, and they perished from the midst of the congregation.",
      "T": "They descended alive into Sheol. The ground sealed over them. They were excised from Israel in an instant."
    },
    "34": {
      "L": "And all Israel that were round about them fled at the cry of them: for they said, Lest the earth swallow us up also.",
      "M": "And all the Israelites around them fled at their cry, for they said: Lest the earth swallow us up also!",
      "T": "Everyone nearby ran at the sound of their screaming — the terrifying thought in every mind: 'We could be next.'"
    },
    "35": {
      "L": "And there came out a fire from the LORD, and consumed the two hundred and fifty men that offered incense.",
      "M": "Fire also came out from the LORD and consumed the 250 men who were offering incense.",
      "T": "Then fire came out from the LORD and burned up the 250 men who had stood at the entrance with their censers."
    },
    "36": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "37": {
      "L": "Speak unto Eleazar the son of Aaron the priest, that he take up the censers out of the burning, and scatter thou the fire yonder; for they are hallowed.",
      "M": "Tell Eleazar son of Aaron the priest to take up the censers from the burning, and scatter the coals at a distance, for the censers are holy.",
      "T": "Tell Eleazar son of Aaron to gather the censers from among the charred remains and scatter the coals away. The censers themselves are holy —"
    },
    "38": {
      "L": "The censers of these sinners against their own souls, let them make them broad plates for a covering of the altar: for they offered them before the LORD, therefore they are hallowed: and they shall be a sign unto the children of Israel.",
      "M": "The censers of these men who sinned at the cost of their own lives — have them hammered into flat sheets as a covering for the altar. For they were presented before the LORD and are holy. They shall be a sign to the Israelites.",
      "T": "— even these sinners' censers carry consecration, having been lifted before the LORD. Hammer them into altar plating: a permanent warning to every generation of what happens when unauthorized hands reach for the priesthood."
    },
    "39": {
      "L": "And Eleazar the priest took the brasen censers, wherewith they that were burnt had offered; and they were made broad plates for a covering of the altar:",
      "M": "So Eleazar the priest took the bronze censers with which the burned men had offered incense and had them hammered flat to cover the altar,",
      "T": "Eleazar collected the bronze censers from the incinerated men and had them beaten flat as altar plating —"
    },
    "40": {
      "L": "To be a memorial unto the children of Israel, that no stranger, which is not of the seed of Aaron, come near to offer incense before the LORD; that he be not as Korah, and as his company: as the LORD said to him by the hand of Moses.",
      "M": "a reminder to the Israelites that no unauthorized person — not of Aaron's line — should come near to offer incense before the LORD, or he would end up like Korah and his company. This was as the LORD had directed through Moses.",
      "T": "— a permanent visual warning embedded in the altar itself: no outsider, no one not of Aaron's descent, approaches the incense altar. The plating said without words: this is what happened to Korah."
    },
    "41": {
      "L": "But on the morrow all the congregation of the children of Israel murmured against Moses and against Aaron, saying, Ye have killed the people of the LORD.",
      "M": "But the next day the whole congregation of Israel grumbled against Moses and Aaron, saying: You have killed the people of the LORD.",
      "T": "The very next morning, the whole congregation turned on Moses and Aaron: 'You killed the LORD's people.'"
    },
    "42": {
      "L": "And it came to pass, when the congregation was gathered against Moses and against Aaron, that they looked toward the tabernacle of the congregation: and, behold, the cloud covered it, and the glory of the LORD appeared.",
      "M": "When the congregation assembled against Moses and Aaron, they turned toward the tent of meeting — the cloud had covered it and the glory of the LORD appeared.",
      "T": "As the mob formed against Moses and Aaron, they looked toward the tent of meeting — and the cloud had already covered it. The glory of the LORD was visibly present."
    },
    "43": {
      "L": "And Moses and Aaron came before the tabernacle of the congregation.",
      "M": "Moses and Aaron went to the front of the tent of meeting.",
      "T": "Moses and Aaron went forward and stood before the tent of meeting."
    },
    "44": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "45": {
      "L": "Get you up from among this congregation, that I may consume them as in a moment. And they fell upon their faces.",
      "M": "Get away from this congregation so that I may consume them in an instant. And they fell facedown.",
      "T": "'Move away from this congregation — I am about to destroy them instantly.' Moses and Aaron fell facedown."
    },
    "46": {
      "L": "And Moses said unto Aaron, Take a censer, and put fire therein from off the altar, and put on incense, and go quickly unto the congregation, and make an atonement for them: for there is wrath gone out from the LORD; the plague is begun.",
      "M": "Moses said to Aaron: Take your censer, put fire from the altar in it, place incense on it, and carry it quickly to the congregation and make atonement for them. For wrath has gone out from the LORD; the plague has begun.",
      "T": "Moses turned to Aaron: 'Take your censer. Fire from the altar, incense on it — run to the people and make atonement. The LORD's wrath has gone out — the plague has already started.'"
    },
    "47": {
      "L": "And Aaron took as Moses commanded, and ran into the midst of the congregation; and, behold, the plague was begun among the people: and he put on incense, and made an atonement for the people.",
      "M": "Aaron took his censer as Moses had said, ran into the middle of the congregation — the plague had indeed begun among the people — placed incense on the censer, and made atonement for the people.",
      "T": "Aaron ran into the thick of the congregation with his censer smoking. The plague was already spreading through the camp. He stood between the living and the dead and made atonement."
    },
    "48": {
      "L": "And he stood between the dead and the living; and the plague was stayed.",
      "M": "He stood between the dead and the living, and the plague was stopped.",
      "T": "He stood at the boundary between death and life, and the plague stopped."
    },
    "49": {
      "L": "Now they that died in the plague were fourteen thousand and seven hundred, beside them that died about the matter of Korah.",
      "M": "Those who died in the plague were 14,700, besides those who had died in the matter of Korah.",
      "T": "Fourteen thousand seven hundred died in the plague — apart from those who had died with Korah."
    },
    "50": {
      "L": "And Aaron returned unto Moses unto the door of the tabernacle of the congregation: and the plague was stayed.",
      "M": "Then Aaron returned to Moses at the entrance of the tent of meeting, for the plague had been stopped.",
      "T": "Aaron returned to Moses at the tent of meeting. The plague was over."
    }
  },
  "17": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto the children of Israel, and take of every one of them a rod according to the house of their fathers, from all their leaders according to the house of their fathers, twelve rods: write thou every man's name upon his rod.",
      "M": "Speak to the Israelites and collect from them one staff per ancestral house — from all their leaders, one staff per ancestral house — twelve staffs in all. Write each man's name on his staff.",
      "T": "Collect from Israel's leaders one staff per ancestral house — twelve staffs in all. Write each leader's name on his staff."
    },
    "3": {
      "L": "And thou shalt write Aaron's name upon the rod of Levi: for one rod shall be for the head of the house of their fathers.",
      "M": "Write Aaron's name on Levi's staff, for there shall be one staff for each ancestral house.",
      "T": "Write Aaron's name on Levi's staff — one staff, one tribe, one name represents the house."
    },
    "4": {
      "L": "And thou shalt lay them up in the tabernacle of the congregation before the testimony, where I will meet with you.",
      "M": "Place them in the tent of meeting before the covenant document, where I meet with you.",
      "T": "Place all the staffs before the covenant tablets in the tent of meeting — where I meet with you."
    },
    "5": {
      "L": "And it shall come to pass, that the man's rod, whom I shall choose, shall blossom: and I will make to cease from me the murmurings of the children of Israel, whereby they murmur against you.",
      "M": "The man I choose — his staff will sprout. In this way I will put an end to the Israelites' grumbling against you, which they keep grumbling against you.",
      "T": "The staff of the man I have chosen will blossom. This will settle, once and for all, who is chosen — and silence Israel's endless grumbling."
    },
    "6": {
      "L": "And Moses spake unto the children of Israel, and every one of their princes gave him a rod apiece, for each prince one, according to their fathers' houses, even twelve rods: and the rod of Aaron was among their rods.",
      "M": "Moses spoke to the Israelites, and each of their leaders gave him a staff — one staff per leader, twelve staffs by their ancestral houses. Aaron's staff was among them.",
      "T": "Moses relayed the command and collected the staffs — one from each leader, twelve in all, Aaron's among them."
    },
    "7": {
      "L": "And Moses laid up the rods before the LORD in the tabernacle of witness.",
      "M": "Moses placed the staffs before the LORD in the tent of the covenant.",
      "T": "Moses laid all twelve staffs before the LORD in the tent of meeting."
    },
    "8": {
      "L": "And it came to pass, that on the morrow Moses went into the tabernacle of witness; and, behold, the rod of Aaron for the house of Levi was budded, and brought forth buds, and bloomed blossoms, and yielded almonds.",
      "M": "The next day Moses went into the tent of the covenant, and there was Aaron's staff — representing the house of Levi — it had budded, put out buds, produced blossoms, and borne ripe almonds.",
      "T": "By the next morning, Aaron's staff had burst into life: buds, blossoms, and ripe almonds — all overnight, without soil or water. It was unmistakable."
    },
    "9": {
      "L": "And Moses brought out all the rods from before the LORD unto all the children of Israel: and they looked, and took every man his rod.",
      "M": "Moses brought out all the staffs from before the LORD to all the Israelites. They looked, and each man took his own staff.",
      "T": "Moses brought out the twelve staffs and showed them to all Israel. Eleven were unchanged. Aaron's alone had bloomed."
    },
    "10": {
      "L": "And the LORD said unto Moses, Bring Aaron's rod again before the testimony, to be kept for a token against the rebels; and thou shalt quite take away their murmurings from me, that they die not.",
      "M": "The LORD said to Moses: Put Aaron's staff back before the covenant document, to be kept as a sign against the rebels, to put an end to their grumbling against me, so that they do not die.",
      "T": "The LORD told Moses: 'Keep Aaron's staff in front of the covenant tablets — a permanent sign against rebellion. Let it end the grumbling before the grumbling ends them.'"
    },
    "11": {
      "L": "And Moses did so: as the LORD commanded him, so did he.",
      "M": "Moses did so; he did just as the LORD commanded him.",
      "T": "Moses obeyed."
    },
    "12": {
      "L": "And the children of Israel spake unto Moses, saying, Behold, we die, we perish, we all perish.",
      "M": "The Israelites said to Moses: We are dying, we are perishing, we are all lost.",
      "T": "Israel cried out to Moses: 'We are dying! We are ruined! Every approach to the holy place kills us!'"
    },
    "13": {
      "L": "Whosoever cometh any thing near unto the tabernacle of the LORD shall die: shall we be consumed with dying?",
      "M": "Anyone who comes near the tabernacle of the LORD shall die. Are we all going to die?",
      "T": "'Anyone who draws near the tabernacle dies. Is there no end to the dying?'"
    }
  },
  "18": {
    "1": {
      "L": "And the LORD said unto Aaron, Thou and thy sons and thy father's house with thee shall bear the iniquity of the sanctuary: and thou and thy sons with thee shall bear the iniquity of your priesthood.",
      "M": "The LORD said to Aaron: You and your sons and your ancestral house with you shall bear the guilt of sins against the sanctuary, and you and your sons alone shall bear the guilt of sins against your priesthood.",
      "T": "The LORD told Aaron: 'You and your sons and your father's house — you carry the consequences of any breach at the sanctuary. You and your sons bear the weight of the priesthood's failures.'"
    },
    "2": {
      "L": "And thy brethren also of the tribe of Levi, the tribe of thy father, bring thou with thee, that they may be joined unto thee, and minister unto thee: but thou and thy sons with thee shall minister before the tabernacle of witness.",
      "M": "Also bring with you your kinsmen from the tribe of Levi, your father's tribe, so that they may join you and assist you when you and your sons serve before the tent of the covenant.",
      "T": "Bring your fellow Levites — your kinsmen by birth — to serve alongside you as assistants. You and your sons remain responsible before the tent of meeting."
    },
    "3": {
      "L": "And they shall keep thy charge, and the charge of all the tabernacle: only they shall not come nigh the vessels of the sanctuary and the altar, that neither they, nor ye also, die.",
      "M": "They shall fulfill their duties to you and to the whole tent, but they shall not come near the furnishings of the sanctuary or the altar, lest both they and you die.",
      "T": "The Levites serve the tabernacle under your oversight — but they must not touch the sacred furnishings or the altar. That boundary is the difference between life and death."
    },
    "4": {
      "L": "And they shall be joined unto thee, and keep the charge of the tabernacle of the congregation, for all the service of the tabernacle: and a stranger shall not come nigh unto you.",
      "M": "They shall join you and keep the charge of the tent of meeting — all the service of the tent — and no unauthorized person shall come near you.",
      "T": "They join you in maintaining the tent of meeting. No unauthorized person may approach you."
    },
    "5": {
      "L": "And ye shall keep the charge of the sanctuary, and the charge of the altar: that there be no wrath any more upon the children of Israel.",
      "M": "You shall be responsible for the sanctuary and the altar, so that wrath does not fall on the Israelites again.",
      "T": "You and your sons guard the altar and sanctuary. Your faithfulness is Israel's protection against divine wrath."
    },
    "6": {
      "L": "And I, behold, I have taken your brethren the Levites from among the children of Israel: to you they are given as a gift for the LORD, to do the service of the tabernacle of the congregation.",
      "M": "Behold, I myself have taken your kinsmen the Levites from among the Israelites. They are given to you as a gift for the LORD, to do the service of the tent of meeting.",
      "T": "I have given you the Levites — drawn from Israel as a gift to me, now given to you — to serve at the tent of meeting under your oversight."
    },
    "7": {
      "L": "Therefore thou and thy sons with thee shall keep your priest's office for every thing of the altar, and within the veil; and ye shall serve: I have given your priest's office unto you as a service of gift: and the stranger that cometh nigh shall be put to death.",
      "M": "But you and your sons shall attend to your priestly duties for everything at the altar and within the veil, and you shall serve. I give you your priesthood as a gift of service. Any unauthorized person who comes near shall be put to death.",
      "T": "You and your sons alone attend to the priestly work — at the altar and within the curtain before the Most Holy Place. I give you this priesthood as a gift. Anyone else who approaches dies."
    },
    "8": {
      "L": "And the LORD spake unto Aaron, Behold, I also have given thee the charge of mine heave offerings of all the hallowed things of the children of Israel; unto thee have I given them by reason of the anointing, and to thy sons, by an ordinance for ever.",
      "M": "The LORD said to Aaron: I also give you charge of the contributions made to me from all the holy gifts of the Israelites. I give them to you and your sons as your portion — a perpetual statute.",
      "T": "The LORD said to Aaron: 'I give you charge of all the contributions brought to me — the holy gifts of Israel. They belong to you and your sons as your allotted portion — a permanent provision.'"
    },
    "9": {
      "L": "This shall be thine of the most holy things, reserved from the fire: every oblation of theirs, every meat offering of theirs, and every sin offering of theirs, and every trespass offering of theirs, which they shall render unto me, shall be most holy for thee and for thy sons.",
      "M": "From the most holy portion — whatever is not burned up — every offering, every grain offering, every sin offering, and every guilt offering they bring to me as most holy shall belong to you and your sons.",
      "T": "From the most holy offerings — what is not consumed by fire — every grain offering, sin offering, and guilt offering brought to me as most holy belongs to you and your sons."
    },
    "10": {
      "L": "In the most holy place shalt thou eat it; every male shall eat it: it shall be holy unto thee.",
      "M": "In the most holy place you shall eat it; every male shall eat it. It is most holy for you.",
      "T": "You eat it in the most holy place — only the males of your household. It is most holy."
    },
    "11": {
      "L": "And this is thine; the heave offering of their gift, with all the wave offerings of the children of Israel: I have given them unto thee, and to thy sons and to thy daughters with thee, by a statute for ever: every one that is clean in thy house shall eat of it.",
      "M": "This also is yours: the contribution of their gift, together with all the wave offerings of the Israelites. I give them to you and your sons and daughters as a permanent statute. Everyone in your household who is ceremonially clean may eat it.",
      "T": "Also yours: the wave offerings and contributions Israel brings — for you, your sons, and daughters. Every clean person in your household may share in this."
    },
    "12": {
      "L": "All the best of the oil, and all the best of the wine, and of the wheat, the firstfruits of them which they shall offer unto the LORD, them have I given thee.",
      "M": "All the best of the oil and all the best of the wine and grain — the firstfruits they give to the LORD — I give to you.",
      "T": "The finest of the oil, the finest wine and grain — the very best of Israel's firstfruits — these belong to you."
    },
    "13": {
      "L": "And whatsoever is first ripe in the land, which they shall bring unto the LORD, shall be thine; every one that is clean in thine house shall eat of it.",
      "M": "The first ripe produce of all that is in their land, which they bring to the LORD, shall be yours. Everyone in your household who is clean may eat it.",
      "T": "The first ripe fruits of the land brought to the LORD are yours. All clean members of your household may eat."
    },
    "14": {
      "L": "Every thing devoted in Israel shall be thine.",
      "M": "Everything in Israel that is devoted to destruction shall be yours.",
      "T": "Everything in Israel placed under the ban — devoted entirely to the LORD — becomes yours."
    },
    "15": {
      "L": "Every thing that openeth the matrix in all flesh, which they bring unto the LORD, whether it be of men or beasts, shall be thine: nevertheless the firstborn of man shalt thou surely redeem, and the firstling of unclean beasts shalt thou redeem.",
      "M": "Every firstborn of all flesh, whether human or animal, that they offer to the LORD shall be yours. Nevertheless, you shall redeem every firstborn human, and the firstborn of unclean animals you shall also redeem.",
      "T": "Every firstborn that opens the womb — human or animal — brought to the LORD is yours. But every firstborn human must be redeemed, and every unclean animal's firstborn must be redeemed."
    },
    "16": {
      "L": "And those that are to be redeemed from a month old shalt thou redeem, according to thine estimation, for the money of five shekels, after the shekel of the sanctuary, which is twenty gerahs.",
      "M": "Their redemption price, from a month old, you shall fix at five shekels of silver by the sanctuary shekel — twenty gerahs.",
      "T": "The redemption price, paid from one month old onward: five sanctuary shekels — twenty gerahs each."
    },
    "17": {
      "L": "But the firstling of a cow, or the firstling of a sheep, or the firstling of a goat, thou shalt not redeem; they are holy: thou shalt sprinkle their blood upon the altar, and shalt burn their fat for an offering made by fire, for a sweet savour unto the LORD.",
      "M": "But the firstborn of a cow, a sheep, or a goat you shall not redeem; they are holy. Sprinkle their blood on the altar and burn their fat as a food offering, a pleasing aroma to the LORD.",
      "T": "The firstborn of ox, sheep, or goat cannot be redeemed — they are holy to the LORD. Their blood is sprinkled on the altar, their fat burned as a pleasing offering."
    },
    "18": {
      "L": "And the flesh of them shall be thine, as the wave breast and as the right shoulder are thine.",
      "M": "Their meat shall be yours — like the breast of the wave offering and the right thigh, it belongs to you.",
      "T": "The meat is yours — like the wave-offering breast and the right thigh that always belong to the priest."
    },
    "19": {
      "L": "All the heave offerings of the holy things, which the children of Israel offer unto the LORD, have I given thee, and thy sons and thy daughters with thee, by a statute for ever: it is a covenant of salt for ever before the LORD unto thee and to thy seed with thee.",
      "M": "All the contributions of the holy gifts that the Israelites offer to the LORD I give to you and your sons and daughters as a permanent statute. It is an everlasting covenant of salt before the LORD for you and your descendants.",
      "T": "All the holy contributions Israel brings to the LORD — given to you, your sons and daughters, as a lasting covenant. A covenant of salt: enduring, binding, preserved against decay, unbreakable before the LORD forever."
    },
    "20": {
      "L": "And the LORD spake unto Aaron, Thou shalt have no inheritance in their land, neither shalt thou have any part among them: I am thy part and thine inheritance among the children of Israel.",
      "M": "The LORD said to Aaron: You shall have no inheritance in their land, nor shall you have any portion among them. I am your portion and your inheritance among the Israelites.",
      "T": "The LORD said to Aaron: 'You will own no land. You receive no territorial allotment. I am your inheritance — I myself, among all Israel.'"
    },
    "21": {
      "L": "And, behold, I have given the children of Levi all the tenth in Israel for an inheritance, for their service which they serve, even the service of the tabernacle of the congregation.",
      "M": "To the Levites I have given all the tithes in Israel as their inheritance in return for the service they perform — the service of the tent of meeting.",
      "T": "I give all of Israel's tithes to the Levites as their inheritance — payment for their service at the tent of meeting."
    },
    "22": {
      "L": "Neither must the children of Israel henceforth come nigh the tabernacle of the congregation, lest they bear sin, and die.",
      "M": "The Israelites must not come near the tent of meeting, lest they bear sin and die.",
      "T": "Israel at large must not approach the tent of meeting. To cross that boundary is to risk death."
    },
    "23": {
      "L": "But the Levites shall do the service of the tabernacle of the congregation, and they shall bear their iniquity: it shall be a statute for ever throughout your generations, that among the children of Israel they have no inheritance.",
      "M": "Only the Levites shall serve at the tent of meeting, and they shall bear responsibility for any offenses against it. This is a permanent statute throughout your generations: among the Israelites the Levites shall have no inheritance.",
      "T": "The Levites serve at the tent of meeting and bear the weight of any breach there. And their portion is not land — in every generation, they receive no territorial inheritance among Israel."
    },
    "24": {
      "L": "But the tithes of the children of Israel, which they offer as an heave offering unto the LORD, I have given to the Levites to inherit: therefore I have said unto them, Among the children of Israel they shall have no inheritance.",
      "M": "For the tithe of the Israelites, which they present as a contribution to the LORD, I have given to the Levites for an inheritance. Therefore I have said of them: Among the Israelites they shall have no inheritance.",
      "T": "The Israelites' tithe — which they lift to the LORD as an offering — goes to the Levites. That is their inheritance. Therefore they receive no land."
    },
    "25": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "26": {
      "L": "Thus speak unto the Levites, and say unto them, When ye take of the children of Israel the tithes which I have given you from them for your inheritance, then ye shall offer up an heave offering of it for the LORD, even a tenth part of the tithe.",
      "M": "Speak to the Levites and say to them: When you receive from the Israelites the tithe that I have given you as your inheritance, you shall present a contribution from it to the LORD — a tithe of the tithe.",
      "T": "Tell the Levites: When you receive the tithe from Israel as your inheritance, you in turn are to present a tithe of that tithe to the LORD."
    },
    "27": {
      "L": "And this your heave offering shall be reckoned unto you, as though it were the corn of the threshingfloor, and as the fulness of the winepress.",
      "M": "Your contribution shall be credited to you as though it were the grain of the threshing floor and the produce of the winepress.",
      "T": "This tithe-of-a-tithe you present will be counted for you exactly as if it were firstfruits from the threshing floor or the winepress."
    },
    "28": {
      "L": "Thus ye also shall offer an heave offering unto the LORD of all your tithes, which ye receive of the children of Israel; and ye shall give thereof the LORD'S heave offering to Aaron the priest.",
      "M": "So you shall also present a contribution to the LORD from all your tithes that you receive from the Israelites, and from these you shall give the LORD's contribution to Aaron the priest.",
      "T": "From everything the Levites receive from Israel, they present a portion to the LORD — and that portion goes to Aaron."
    },
    "29": {
      "L": "Out of all your gifts ye shall offer every heave offering of the LORD, of all the best thereof, even the hallowed part thereof out of it.",
      "M": "Out of all the gifts you receive, you shall present every contribution owed to the LORD from the very best of it — the holy portion from it.",
      "T": "Give the LORD's portion from the best of what you receive — the holiest, finest part."
    },
    "30": {
      "L": "Therefore thou shalt say unto them, When ye have heaved the best thereof from it, then it shall be counted unto the Levites as the increase of the threshingfloor, and as the increase of the winepress.",
      "M": "Say to them: When you have presented the best of it, the remainder shall be counted to the Levites as the produce of the threshing floor and the produce of the winepress.",
      "T": "Once you have lifted the best portion to the LORD, the remainder counts for you just as the farmer's harvest counts — yours to enjoy."
    },
    "31": {
      "L": "And ye shall eat it in every place, ye and your households: for it is your reward for your service in the tabernacle of the congregation.",
      "M": "You and your households may eat it anywhere, for it is your payment for your service at the tent of meeting.",
      "T": "You and your families may eat the rest freely, anywhere you choose — it is your earned wage for service at the tent of meeting."
    },
    "32": {
      "L": "And ye shall bear no sin by reason of it, when ye have heaved from it the best of it: neither shall ye pollute the holy things of the children of Israel, lest ye die.",
      "M": "You will bear no guilt because of it, once you have contributed the best of it. But do not profane the holy gifts of the Israelites, or you will die.",
      "T": "No guilt attaches to eating the rest, once you have given the LORD's portion from the best. But handle the holy gifts carelessly and it will cost your life."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'numbers')
        merge_tier(existing, NUMBERS, tier_key)
        save(tier_dir, 'numbers', existing)
    print('Numbers 13–18 written.')

if __name__ == '__main__':
    main()
