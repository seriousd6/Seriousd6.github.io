"""
MKT Exodus chapters 31–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-exodus-31-36.py

Covers: craftsmen appointed (ch. 31), the golden calf and Moses' intercession (ch. 32),
God's presence and Moses' request to see glory (ch. 33), covenant renewal and the divine
name proclaimed (ch. 34), freewill offerings for the tabernacle (ch. 35), and the
construction of the tabernacle structure (ch. 36).

Translation decisions:
- H3068 (יהוה): "the LORD" in L/M/T — consistent with prior Exodus scripts
- H430 (אֱלֹהִים): "God" throughout
- H7307 (רוּחַ) at 31:3: "Spirit of God" in all tiers — capital S; context is clearly divine
  endowment, not wind or breath
- H2450 (חָכָם) "wise-hearted": L="wise in heart/wise-hearted", M="skilled", T="gifted craftsman"
  — the Hebrew idiom lēb ḥāḵām means practical wisdom residing in the heart; English
  "wise" undersells the craft dimension
- H7676 (שַׁבָּת): "Sabbath" throughout; no glossing as "rest day"
- H4150 (מוֹעֵד): "tent of meeting" — the pre-tabernacle meeting structure in ch. 33
- H3519 (כָּבוֹד) at 33:18,22; 34:6: "glory" in all tiers — the weighty luminous presence
- H6440 (פָּנִים) at 33:11,14-15,20,23; 34:29-35: "face" in L/M;
  T uses "presence" where the theological point is God's accompanying nearness
- H5695 (עֵגֶל): "calf" — no softening to "young bull"; the diminutive is deliberately
  contemptuous in context
- H2617 (חֶסֶד) at 34:6-7: L="steadfast love", M="faithful love", T="covenant loyalty" —
  consistent with Exodus 19-24 script
- H571 (אֱמֶת) at 34:6: "faithfulness/truth" — L="faithfulness", M="faithfulness",
  T="absolute reliability" to distinguish from חֶסֶד
- H5375 (נָשָׂא) + H5771 (עָוֹן) at 34:7: "forgiving iniquity" — the image is of bearing/
  carrying the weight of guilt; L preserves "bearing", M/T use "forgiving"
- H7121 (קָרַן) at 34:29,30,35: L="shone", M="was radiant", T="blazed with light" — Moses'
  face actually became luminous from contact with God; not metaphorical; the same root
  gives "horn" (Jerome's Vulgate mistranslation: cornuta = horned)
- H4539 (מָסָוֶה) at 34:33-35: "veil" — L/M/T consistent
- H5071 (נְדָבָה) at 35:29: "freewill offering" / "willing offering" — the emphasis is the
  volunteer character, not the legal category; T renders "gift of an open hand"
- H7521 (נָדַב) at 35:21: "stirred/moved/willing" — L="stirred him up", M/T="willing heart"
- H1285 (בְּרִית) at 34:10,27,28: "covenant" — formal, oath-bound relationship
- Decalogue echo at 34:28: "ten commandments" = עֲשֶׂרֶת הַדְּבָרִים (ten words) — L="ten
  words", M="Ten Commandments", T="the Ten Words of the Covenant"
- Golden calf episode (ch. 32): the theological weight is massive — this is covenant
  apostasy at the moment of covenant ratification (ch. 24 just concluded). Moses'
  intercession (32:11-14,31-32) is the paradigm for prophetic intercession in the OT.
  Moses offering to be "blotted from your book" (32:32) anticipates Paul in Rom 9:3.
- 33:11 "face to face, as a man speaks to his friend" — highest intimacy formula for
  Moses' prophetic status; contrast 33:20 where direct vision of God's face is fatal.
  These are not contradictory: 33:11 = dialogic intimacy; 33:20 = ontological vision.
- 34:6-7: The Thirteen Attributes (Shelosh Esreh Middot) — this is arguably the most
  cited verse in the Hebrew Bible, echoed in Num 14:18, Neh 9:17, Ps 86:15, Joel 2:13,
  Jonah 4:2. T tier must convey its weight as a creedal formula.
- Tabernacle construction (chs. 35-36): the detailed repetition echoes Genesis creation;
  both end with "and it was so" type formulas. T tier can surface this connection.
  The freewill giving of the people mirrors the willing ordering of creation.
- Bezalel's name (H1212): means "in the shadow/protection of God" — note in T tier at 31:2
- Oholiab's name (H171): "tent of the father" — note in T tier at 31:6
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

EXODUS = {
  "31": {
    "1": {
      "L": "And the LORD spoke to Moses, saying:",
      "M": "Then the LORD said to Moses:",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "'See, I have called by name Bezalel the son of Uri, the son of Hur, of the tribe of Judah;'",
      "M": "'See, I have chosen by name Bezalel son of Uri, the son of Hur, of the tribe of Judah,'",
      "T": "'Look — I have personally chosen Bezalel son of Uri son of Hur, of the tribe of Judah. His very name means \"in God's shelter,\" and I have placed him there.'"
    },
    "3": {
      "L": "'and I have filled him with the Spirit of God, with skill, and with understanding, and with knowledge, and in all manner of workmanship,'",
      "M": "'and I have filled him with the Spirit of God, giving him skill, understanding, and knowledge in every kind of craft,'",
      "T": "'I have filled him with the Spirit of God — practical wisdom, creative intelligence, deep knowledge, mastery in every form of skilled work.'"
    },
    "4": {
      "L": "'to devise skillful works, to work in gold, and in silver, and in bronze,'",
      "M": "'to make artistic designs for work in gold, silver, and bronze,'",
      "T": "'He can envision and execute: gold, silver, bronze —'"
    },
    "5": {
      "L": "'and in cutting of stones for setting, and in carving of wood, to work in all manner of workmanship.'",
      "M": "'in cutting and setting stones, in carving wood, and in every kind of craft.'",
      "T": "'the cutting and setting of gemstones, the carving of wood, every form of skilled craft.'"
    },
    "6": {
      "L": "'And behold, I have appointed with him Oholiab the son of Ahisamach, of the tribe of Dan; and in the hearts of all who are wise-hearted I have put wisdom, that they may make all that I have commanded you:'",
      "M": "'Moreover, I have appointed Oholiab son of Ahisamach, of the tribe of Dan, to work with him. I have also given skill to all the gifted craftsmen so that they can make everything I have commanded you:'",
      "T": "'And alongside him I have appointed Oholiab son of Ahisamach of the tribe of Dan — his name means \"my father's tent,\" and he will help build mine. I have placed wisdom in the hearts of every skilled craftsman so that all I have commanded can be made:'"
    },
    "7": {
      "L": "'the tent of meeting, and the ark of the testimony, and the mercy seat that is upon it, and all the furnishing of the tent,'",
      "M": "'the tent of meeting, the ark of the covenant law with the atonement cover on it, and all the other furnishings of the tent —'",
      "T": "'the Tent of Meeting, the ark of the covenant law and its atonement cover, all the furnishings of the Tent —'"
    },
    "8": {
      "L": "'the table and its utensils, and the pure lampstand with all its utensils, and the altar of incense,'",
      "M": "'the table and its articles, the pure gold lampstand and all its accessories, the altar of incense,'",
      "T": "'the table and all its vessels, the pure gold lampstand with all its fittings, the altar of incense,'"
    },
    "9": {
      "L": "'the altar of burnt offering with all its utensils, and the basin and its stand,'",
      "M": "'the altar of burnt offering with all its utensils, the basin with its stand,'",
      "T": "'the altar of burnt offering with all its equipment, the washbasin and its base,'"
    },
    "10": {
      "L": "'the woven garments, and the holy garments for Aaron the priest, and the garments of his sons for their service as priests,'",
      "M": "'the woven garments, both the sacred garments for Aaron the priest and the garments for his sons when they serve as priests,'",
      "T": "'the woven vestments — the sacred garments for Aaron the priest and for his sons in their priestly ministry,'"
    },
    "11": {
      "L": "'and the anointing oil, and the fragrant incense for the Holy Place; according to all that I have commanded you they shall do.'",
      "M": "'and the anointing oil and fragrant incense for the Holy Place. They are to make them just as I commanded you.'",
      "T": "'and the anointing oil and the aromatic incense for the Holy Place. Let them make everything exactly as I have commanded you.'"
    },
    "12": {
      "L": "And the LORD spoke to Moses, saying:",
      "M": "Then the LORD said to Moses:",
      "T": "The LORD spoke to Moses again:"
    },
    "13": {
      "L": "'Speak also to the children of Israel, saying: \"Verily my Sabbaths you shall keep, for it is a sign between me and you throughout your generations, that you may know that I the LORD sanctify you.\"'",
      "M": "'Say to the Israelites, \"You must observe my Sabbaths. This will be a sign between me and you for the generations to come, so that you may know that I am the LORD, who makes you holy.\"'",
      "T": "'Tell the people of Israel: My Sabbaths you shall keep above all else — this is the sign between me and you across every generation, the covenant marker by which you will know that I, the LORD, am the one who sets you apart.'"
    },
    "14": {
      "L": "'Observe the Sabbath, because it is holy to you. Everyone who profanes it shall surely be put to death; for whoever does any work on it, that soul shall be cut off from among his people.'",
      "M": "'Observe the Sabbath, because it is holy to you. Anyone who desecrates it is to be put to death; those who do any work on that day must be cut off from their people.'",
      "T": "'Keep the Sabbath — it is holy, set apart for me and for you. Whoever treats it as ordinary will be put to death; whoever works on it will be cut off from the community of Israel.'"
    },
    "15": {
      "L": "'Six days work shall be done, but the seventh day is the Sabbath of solemn rest, holy to the LORD; whoever does any work on the Sabbath day shall surely be put to death.'",
      "M": "'For six days work may be done, but the seventh day is a day of sabbath rest, sacred to the LORD. Whoever does any work on the Sabbath day is to be put to death.'",
      "T": "'Six days you work — the seventh is Sabbath, complete rest, consecrated to the LORD. Whoever labors on that day must be put to death.'"
    },
    "16": {
      "L": "'Therefore the children of Israel shall keep the Sabbath, to observe the Sabbath throughout their generations as a perpetual covenant.'",
      "M": "'The Israelites are to observe the Sabbath, celebrating it for the generations to come as a lasting covenant.'",
      "T": "'The people of Israel shall observe the Sabbath — keeping it across every generation as a perpetual covenant bond between us.'"
    },
    "17": {
      "L": "'It is a sign between me and the children of Israel forever; for in six days the LORD made heaven and earth, and on the seventh day he rested and was refreshed.'",
      "M": "'It will be a sign between me and the Israelites forever, for in six days the LORD made the heavens and the earth, and on the seventh day he rested and was refreshed.'",
      "T": "'It is an eternal sign between me and Israel: in six days the LORD made sky and earth, and on the seventh day he rested — he let himself be restored. The Sabbath re-enacts creation's completion.'"
    },
    "18": {
      "L": "And he gave to Moses, when he had finished speaking with him on Mount Sinai, the two tablets of the testimony, tablets of stone, written with the finger of God.",
      "M": "When the LORD finished speaking to Moses on Mount Sinai, he gave him the two tablets of the covenant law, the tablets of stone inscribed by the finger of God.",
      "T": "When God had finished speaking with Moses on Sinai, he placed in his hands the two stone tablets of the covenant — written by the very finger of God."
    }
  },
  "32": {
    "1": {
      "L": "And when the people saw that Moses delayed to come down from the mountain, the people gathered themselves together against Aaron and said to him, 'Come, make us gods who shall go before us; for as for this Moses, the man who brought us up out of the land of Egypt, we do not know what has become of him.'",
      "M": "When the people saw that Moses was so long in coming down from the mountain, they gathered around Aaron and said to him, 'Come, make us gods who will go before us. As for this Moses who brought us up out of Egypt—we don't know what has happened to him.'",
      "T": "Moses was a long time on the mountain. The people grew restless, assembled around Aaron, and demanded: 'Make us gods to lead us. This Moses who brought us out of Egypt — we have no idea what has become of him.'"
    },
    "2": {
      "L": "And Aaron said to them, 'Take off the rings of gold that are in the ears of your wives, your sons, and your daughters, and bring them to me.'",
      "M": "Aaron answered them, 'Take off the gold earrings that your wives, your sons and your daughters are wearing, and bring them to me.'",
      "T": "Aaron said to them, 'Pull the gold earrings off the ears of your wives and children and bring them here.'"
    },
    "3": {
      "L": "So all the people took off the rings of gold that were in their ears and brought them to Aaron.",
      "M": "So all the people took off their earrings and brought them to Aaron.",
      "T": "The whole assembly pulled off their gold earrings and laid them before Aaron."
    },
    "4": {
      "L": "And he received the gold from their hand, and he fashioned it with a graving tool and made a golden calf. And they said, 'These are your gods, O Israel, who brought you up out of the land of Egypt!'",
      "M": "He took what they handed him and made it into an idol cast in the shape of a calf, fashioning it with a tool. Then they said, 'These are your gods, Israel, who brought you up out of Egypt!'",
      "T": "Aaron took the gold, worked it with a tool, and cast it into the shape of a calf. And the people said, 'These are your gods, O Israel — the gods who brought you up from Egypt!'"
    },
    "5": {
      "L": "When Aaron saw this, he built an altar before it. And Aaron made a proclamation and said, 'Tomorrow shall be a feast to the LORD.'",
      "M": "When Aaron saw this, he built an altar in front of the calf and announced, 'Tomorrow there will be a festival to the LORD.'",
      "T": "Seeing what the people had done, Aaron built an altar before the calf and announced: 'Tomorrow will be a feast day for the LORD.' He tried to contain the catastrophe by wrapping it in the LORD's name."
    },
    "6": {
      "L": "And they rose up early the next day and offered burnt offerings and brought peace offerings. And the people sat down to eat and to drink and rose up to play.",
      "M": "So the next day the people rose early and sacrificed burnt offerings and presented fellowship offerings. Afterward they sat down to eat and drink and got up to indulge in revelry.",
      "T": "The next morning they rose early, offered burnt offerings, and ate fellowship meals. Then the celebration slid into something else — they ate, drank, and gave themselves over to the kind of play that has nothing holy in it."
    },
    "7": {
      "L": "And the LORD said to Moses, 'Go, get you down; for your people, whom you brought out of the land of Egypt, have corrupted themselves.'",
      "M": "Then the LORD said to Moses, 'Go down, because your people, whom you brought up out of Egypt, have become corrupt.'",
      "T": "The LORD told Moses, 'Go down — now. The people you brought out of Egypt have destroyed themselves.'"
    },
    "8": {
      "L": "'They have turned aside quickly out of the way that I commanded them. They have made for themselves a golden calf and have worshiped it and sacrificed to it and said, \"These are your gods, O Israel, who brought you up out of the land of Egypt!\"'",
      "M": "'They have been quick to turn away from what I commanded them and have made themselves an idol cast in the shape of a calf. They have bowed down to it and sacrificed to it and have said, \"These are your gods, Israel, who brought you up out of Egypt.\"'",
      "T": "'They have bolted from the path I set them on — they made a golden calf, bowed to it, slaughtered offerings before it, and declared it the god who rescued them from Egypt. The ink is barely dry on my covenant.'"
    },
    "9": {
      "L": "And the LORD said to Moses, 'I have seen this people, and behold, it is a stiff-necked people.'",
      "M": "'I have seen these people,' the LORD said to Moses, 'and they are a stiff-necked people.'",
      "T": "'I have seen this people,' the LORD said to Moses, 'and they are utterly stiff-necked — they bend to no one.'"
    },
    "10": {
      "L": "'Now therefore let me alone, that my wrath may burn hot against them and I may consume them, in order that I may make a great nation of you.'",
      "M": "'Now leave me alone so that my anger may burn against them and that I may destroy them. Then I will make you into a great nation.'",
      "T": "'Now stand aside — let my anger have its way with them. I will consume them and make a great nation from you alone.'"
    },
    "11": {
      "L": "But Moses implored the LORD his God and said, 'Why, O LORD, does your wrath burn hot against your people, whom you brought out from the land of Egypt with great power and with a mighty hand?'",
      "M": "But Moses sought the favor of the LORD his God. 'LORD,' he said, 'why should your anger burn against your people, whom you brought out of Egypt with great power and a mighty hand?'",
      "T": "Moses planted himself before the LORD his God and argued: 'LORD — why would your anger burn against your own people? These are the ones you brought out of Egypt with a display of great power and a strong hand.'"
    },
    "12": {
      "L": "'Why should the Egyptians say, \"With evil intent he brought them out, to kill them in the mountains and to consume them from the face of the earth\"? Turn from your burning anger and relent from this disaster against your people.'",
      "M": "'Why should the Egyptians say, \"It was with evil intent that he brought them out, to kill them in the mountains and to wipe them off the face of the earth\"? Turn from your fierce anger; relent and do not bring this disaster on your people.'",
      "T": "'If you destroy them, Egypt will say you brought them into the wilderness to slaughter them — that your rescue was a trap. Turn from your burning anger. Relent from this disaster you have threatened against your own people.'"
    },
    "13": {
      "L": "'Remember Abraham, Isaac, and Israel, your servants, to whom you swore by yourself, and said to them, \"I will multiply your offspring as the stars of heaven, and all this land that I have promised I will give to your offspring, and they shall inherit it forever.\"'",
      "M": "'Remember your servants Abraham, Isaac and Israel, to whom you swore by your own self: \"I will make your descendants as numerous as the stars in the sky and I will give your descendants all this land I promised them, and it will be their inheritance forever.\"'",
      "T": "'Remember Abraham, Isaac, and Israel — your own servants. You swore by yourself, because there was nothing greater to swear by: \"I will multiply your descendants like the stars of the sky, and I will give them all this land I promised, as their inheritance forever.\" Will you now break that oath?'"
    },
    "14": {
      "L": "And the LORD relented from the disaster that he had spoken of bringing on his people.",
      "M": "Then the LORD relented and did not bring on his people the disaster he had threatened.",
      "T": "And the LORD relented. He did not bring on his people the disaster he had threatened."
    },
    "15": {
      "L": "Then Moses turned and went down from the mountain with the two tablets of the testimony in his hand, tablets that were written on both sides; on the front and on the back they were written.",
      "M": "Moses turned and went down the mountain with the two tablets of the covenant law in his hands. They were inscribed on both sides, front and back.",
      "T": "Moses turned and came down the mountain, the two covenant tablets in his hands — inscribed on both sides, front and back."
    },
    "16": {
      "L": "The tablets were the work of God, and the writing was the writing of God, engraved on the tablets.",
      "M": "The tablets were the work of God; the writing was the writing of God, engraved on the tablets.",
      "T": "The tablets themselves were the work of God; the script carved into them was the writing of God."
    },
    "17": {
      "L": "When Joshua heard the noise of the people as they shouted, he said to Moses, 'There is a noise of war in the camp.'",
      "M": "When Joshua heard the noise of the people shouting, he said to Moses, 'There is the sound of war in the camp.'",
      "T": "Joshua, waiting lower on the mountain, heard the shouting from the camp and said to Moses, 'It sounds like war down there.'"
    },
    "18": {
      "L": "But he said, 'It is not the sound of the shout of victory, nor is it the sound of the cry of defeat; it is the sound of singing that I hear.'",
      "M": "Moses replied: 'It is not the sound of victory, it is not the sound of defeat; it is the sound of singing that I hear.'",
      "T": "Moses said, 'No — not a victory shout, not a battle cry. What I hear is singing.'"
    },
    "19": {
      "L": "And as soon as he came near the camp and saw the calf and the dancing, Moses' anger burned hot, and he threw the tablets out of his hands and broke them at the foot of the mountain.",
      "M": "When Moses approached the camp and saw the calf and the dancing, his anger burned and he threw the tablets out of his hands, breaking them to pieces at the foot of the mountain.",
      "T": "Moses came within sight of the camp — he saw the calf, he saw the dancing — and his anger blazed. He hurled the stone tablets from his hands and shattered them at the base of the mountain."
    },
    "20": {
      "L": "And he took the calf that they had made and burned it with fire and ground it to powder and scattered it on the water and made the people of Israel drink it.",
      "M": "And he took the calf the people had made and burned it in the fire; then he ground it to powder, scattered it on the water and made the Israelites drink it.",
      "T": "He seized the golden calf, melted it down, ground the remains to powder, scattered it over water, and made Israel drink it — forcing them to ingest the proof of their own guilt."
    },
    "21": {
      "L": "And Moses said to Aaron, 'What did this people do to you that you have brought such a great sin upon them?'",
      "M": "He said to Aaron, 'What did these people do to you, that you led them into such great sin?'",
      "T": "Moses turned on Aaron: 'What did they do to you that you led them into sin this great?'"
    },
    "22": {
      "L": "And Aaron said, 'Let not the anger of my lord burn hot. You know the people, that they are set on evil.'",
      "M": "'Do not be angry, my lord,' Aaron answered. 'You know how prone these people are to evil.'",
      "T": "'Please — don't be furious,' Aaron said. 'You know this people; they are bent toward trouble.'"
    },
    "23": {
      "L": "'They said to me, \"Make us gods who shall go before us; for as for this Moses, the man who brought us up out of the land of Egypt, we do not know what has become of him.\"'",
      "M": "'They said to me, \"Make us gods who will go before us. As for this Moses who brought us up out of Egypt, we don't know what has happened to him.\"'",
      "T": "'They said to me, \"Make us gods to lead us — Moses who brought us out of Egypt has vanished.\" What was I supposed to do?'"
    },
    "24": {
      "L": "'So I said to them, \"Whoever has any gold, let them take it off.\" So they gave it to me, and I threw it into the fire, and out came this calf.'",
      "M": "'So I told them, \"Whoever has any gold jewelry, take it off.\" Then they gave me the gold, and I threw it into the fire, and out came this calf!'",
      "T": "'I told them to give me their gold. They did — I threw it in the fire — and this calf walked out.' Aaron offered the oldest excuse: I am not responsible for what the materials produced."
    },
    "25": {
      "L": "And Moses saw that the people had broken loose, for Aaron had let them break loose, to their shame before their enemies.",
      "M": "Moses saw that the people were running wild and that Aaron had let them get out of control and so become a laughingstock to their enemies.",
      "T": "Moses saw plainly: the people had broken loose — Aaron had dropped the reins — and they had become a mockery before their enemies."
    },
    "26": {
      "L": "Then Moses stood in the gate of the camp and said, 'Who is on the LORD's side? Come to me.' And all the sons of Levi gathered around him.",
      "M": "So he stood at the entrance to the camp and said, 'Whoever is for the LORD, come to me.' And all the Levites rallied to him.",
      "T": "Moses stood at the camp gate and called out: 'Whoever is on the LORD's side — come to me.' Every Levite moved to stand with him."
    },
    "27": {
      "L": "And he said to them, 'Thus says the LORD God of Israel: \"Put your sword at your side each of you, and go to and fro from gate to gate throughout the camp, and each of you kill his brother and his companion and his neighbor.\"'",
      "M": "Then he said to them, 'This is what the LORD, the God of Israel, says: \"Each man strap a sword to his side. Go back and forth through the camp from one end to the other, each killing his brother and friend and neighbor.\"'",
      "T": "He told them, 'The LORD God of Israel commands: strap on your swords. Move through this camp from end to end — strike down brother, companion, neighbor.' Covenant loyalty to God takes precedence over every human bond."
    },
    "28": {
      "L": "And the sons of Levi did according to the word of Moses. And that day about three thousand men of the people fell.",
      "M": "The Levites did as Moses commanded, and that day about three thousand of the people died.",
      "T": "The Levites obeyed. That day approximately three thousand men of the people fell."
    },
    "29": {
      "L": "And Moses said, 'Today you have been ordained for the service of the LORD, each one at the cost of his son and of his brother, that he may bestow a blessing upon you this day.'",
      "M": "Then Moses said, 'You have been set apart to the LORD today, for you were against your own sons and brothers, and he has blessed you this day.'",
      "T": "Moses said to the Levites, 'Today you have consecrated yourselves to the LORD's service — you did not spare son or brother. Because of this, he bestows his blessing on you today.' Their willingness to bear cost purchased their vocation."
    },
    "30": {
      "L": "The next day Moses said to the people, 'You have sinned a great sin. And now I will go up to the LORD; perhaps I can make atonement for your sin.'",
      "M": "The next day Moses said to the people, 'You have committed a terrible sin. But now I will go up to the LORD; perhaps I can make atonement for your sin.'",
      "T": "The next morning Moses told the people, 'You have committed a catastrophic sin. Now I am going up to the LORD — perhaps I can make atonement for what you have done.'"
    },
    "31": {
      "L": "So Moses returned to the LORD and said, 'Alas, this people has sinned a great sin. They have made for themselves gods of gold.'",
      "M": "So Moses went back to the LORD and said, 'Oh, what a great sin these people have committed! They have made themselves gods of gold.'",
      "T": "Moses returned to the LORD and said, 'This people has committed a terrible sin — they made themselves gods of gold.'"
    },
    "32": {
      "L": "'But now, if you will forgive their sin—but if not, please blot me out of your book that you have written.'",
      "M": "'But now, please forgive their sin—but if not, then blot me out of the book you have written.'",
      "T": "'If you will forgive their sin — do so. But if not, then erase me from the book you have written. I will not be saved while they are lost.' Moses offered his own eternal standing as surety for Israel."
    },
    "33": {
      "L": "But the LORD said to Moses, 'Whoever has sinned against me, I will blot out of my book.'",
      "M": "The LORD replied to Moses, 'Whoever has sinned against me I will blot out of my book.'",
      "T": "The LORD replied to Moses: 'Each person who has sinned against me bears their own account. I will blot out the guilty — I do not transfer guilt.'"
    },
    "34": {
      "L": "'But now go, lead the people to the place about which I have spoken to you; behold, my angel shall go before you. Nevertheless, in the day when I visit, I will visit their sin upon them.'",
      "M": "'Now go, lead the people to the place I spoke of, and my angel will go before you. However, when the time comes for me to punish, I will punish them for their sin.'",
      "T": "'Now go — lead the people toward the land I promised. My angel will go ahead of you. But know this: on the day of my reckoning, I will hold this sin against them.'"
    },
    "35": {
      "L": "And the LORD struck the people with a plague, because they made the calf, the one that Aaron made.",
      "M": "And the LORD struck the people with a plague because of what they did with the calf Aaron had made.",
      "T": "The LORD struck the people with a plague — because of the calf. Aaron had made it, but the people had worshiped it."
    }
  },
  "33": {
    "1": {
      "L": "The LORD said to Moses, 'Depart; go up from here, you and the people whom you have brought up out of the land of Egypt, to the land of which I swore to Abraham, Isaac, and Jacob, saying, \"To your offspring I will give it.\"'",
      "M": "Then the LORD said to Moses, 'Leave this place, you and the people you brought up out of Egypt, and go up to the land I promised on oath to Abraham, Isaac and Jacob, saying, \"I will give it to your descendants.\"'",
      "T": "The LORD said to Moses, 'Move out from here — you and the people you brought from Egypt. Head to the land I swore to give to the offspring of Abraham, Isaac, and Jacob.'"
    },
    "2": {
      "L": "'I will send an angel before you, and I will drive out the Canaanites, the Amorites, the Hittites, the Perizzites, the Hivites, and the Jebusites.'",
      "M": "'I will send an angel before you and drive out the Canaanites, Amorites, Hittites, Perizzites, Hivites and Jebusites.'",
      "T": "'I will send my angel ahead of you to clear the way — Canaanites, Amorites, Hittites, Perizzites, Hivites, Jebusites, all of them.'"
    },
    "3": {
      "L": "'Go up to a land flowing with milk and honey; but I will not go up among you, for you are a stiff-necked people, lest I consume you on the way.'",
      "M": "'Go up to the land flowing with milk and honey. But I will not travel with you, because you are a stiff-necked people and I might destroy you on the way.'",
      "T": "'The land is rich — milk and honey. But I will not go up among you. You are stiff-necked, and if I traveled in your midst I might destroy you on the road.'"
    },
    "4": {
      "L": "When the people heard this disastrous word, they mourned, and no one put on his ornaments.",
      "M": "When the people heard these distressing words, they began to mourn and no one put on any ornaments.",
      "T": "When the people heard this devastating news — that God would not go with them — they mourned. No one put on their jewelry."
    },
    "5": {
      "L": "For the LORD had said to Moses, 'Say to the children of Israel, \"You are a stiff-necked people; if for a single moment I should go up among you, I would consume you. So now take off your ornaments, that I may know what to do with you.\"'",
      "M": "For the LORD had said to Moses, 'Tell the Israelites, \"You are a stiff-necked people. If I were to go with you even for a moment, I might destroy you. Now take off your ornaments and I will decide what to do with you.\"'",
      "T": "The LORD had told Moses, 'Say to Israel: You are stiff-necked. One moment of my presence traveling among you and I would consume you. Strip off your ornaments — I must consider what to do with you.'"
    },
    "6": {
      "L": "So the children of Israel stripped themselves of their ornaments from Mount Horeb onward.",
      "M": "So the Israelites stripped off their ornaments at Mount Horeb.",
      "T": "From Mount Horeb onward, Israel put away their jewelry. It was an act of national mourning."
    },
    "7": {
      "L": "Now Moses used to take the tent and pitch it outside the camp, far off from the camp, and he called it the tent of meeting. And everyone who sought the LORD would go out to the tent of meeting, which was outside the camp.",
      "M": "Now Moses used to take a tent and pitch it outside the camp some distance away, calling it the 'tent of meeting.' Anyone inquiring of the LORD would go to the tent of meeting outside the camp.",
      "T": "Moses would take a tent and pitch it well outside the camp, calling it the Tent of Meeting. Anyone who wanted to seek the LORD went there — outside the camp, which had made itself unclean."
    },
    "8": {
      "L": "Whenever Moses went out to the tent, all the people would rise up, and each man would stand at his tent door and watch Moses until he had gone into the tent.",
      "M": "Whenever Moses went out to the tent, all the people rose and stood at the entrances to their tents, watching Moses until he entered the tent.",
      "T": "Every time Moses went out to the Tent, the whole camp rose to its feet and stood watching at their own tent doors, eyes following him until he disappeared inside."
    },
    "9": {
      "L": "When Moses entered the tent, the pillar of cloud would descend and stand at the entrance of the tent, and the LORD would speak with Moses.",
      "M": "As Moses went into the tent, the pillar of cloud would come down and stay at the entrance, while the LORD spoke with Moses.",
      "T": "As Moses entered, the pillar of cloud would descend and station itself at the entrance of the Tent. Then the LORD would speak with Moses."
    },
    "10": {
      "L": "And when all the people saw the pillar of cloud standing at the entrance of the tent, all the people would rise up and worship, each at his tent door.",
      "M": "Whenever the people saw the pillar of cloud standing at the entrance to the tent, they all stood and worshiped, each at the entrance to their own tent.",
      "T": "When all the people saw the pillar of cloud at the Tent entrance, the whole camp rose and worshiped — each from the door of their own tent."
    },
    "11": {
      "L": "Thus the LORD used to speak to Moses face to face, as a man speaks to his friend. When Moses turned again into the camp, his assistant Joshua the son of Nun, a young man, would not depart from the tent.",
      "M": "The LORD would speak to Moses face to face, as one speaks to a friend. Then Moses would return to the camp, but his young aide Joshua son of Nun did not leave the tent.",
      "T": "The LORD spoke to Moses face to face — the way a man speaks openly with his closest friend. Afterward Moses returned to the camp, but his young attendant Joshua son of Nun did not leave the Tent."
    },
    "12": {
      "L": "Moses said to the LORD, 'See, you say to me, \"Bring up this people,\" but you have not let me know whom you will send with me. Yet you have said, \"I know you by name, and you have also found favor in my sight.\"'",
      "M": "Moses said to the LORD, 'You have been telling me, \"Lead these people,\" but you have not let me know whom you will send with me. You have said, \"I know you by name and you have found favor with me.\"'",
      "T": "Moses pressed the LORD: 'You keep telling me to lead these people, but you haven't told me who you'll send with me. You said you know me by name — that I've found favor with you.'"
    },
    "13": {
      "L": "'Now therefore, if I have found favor in your sight, please show me now your ways, that I may know you in order to find favor in your sight. Consider too that this nation is your people.'",
      "M": "'If you are pleased with me, teach me your ways so I may know you and continue to find favor with you. Remember that this nation is your people.'",
      "T": "'If that favor is real, then show me your ways — let me truly know you, not just serve you. And consider this: these people are yours. You cannot abandon your own.'"
    },
    "14": {
      "L": "And he said, 'My presence will go with you, and I will give you rest.'",
      "M": "The LORD replied, 'My Presence will go with you, and I will give you rest.'",
      "T": "The LORD answered simply: 'My presence goes with you. I will give you rest.'"
    },
    "15": {
      "L": "And he said to him, 'If your presence will not go with me, do not bring us up from here.'",
      "M": "Then Moses said to him, 'If your Presence does not go with us, do not send us up from here.'",
      "T": "Moses replied, 'If your presence does not go with us, do not move us from this place. We go nowhere without you.'"
    },
    "16": {
      "L": "'For how shall it be known that I have found favor in your sight, I and your people? Is it not in your going with us, so that we are distinct, I and your people, from every other people on the face of the earth?'",
      "M": "'How will anyone know that you are pleased with me and with your people unless you go with us? What else will distinguish me and your people from all the other people on the face of the earth?'",
      "T": "'How else will the nations know that you are pleased with me and with your people? It is only your presence going with us that sets Israel apart from every other people on earth. Without that, we are nothing special.'"
    },
    "17": {
      "L": "And the LORD said to Moses, 'This very thing that you have spoken I will do, for you have found favor in my sight, and I know you by name.'",
      "M": "And the LORD said to Moses, 'I will do the very thing you have asked, because I am pleased with you and I know you by name.'",
      "T": "The LORD said to Moses, 'I will do exactly what you have asked — because you have found favor with me, and because I know you — personally, by name.'"
    },
    "18": {
      "L": "Then Moses said, 'Please show me your glory.'",
      "M": "Then Moses said, 'Now show me your glory.'",
      "T": "Moses pushed further: 'Show me your glory.'"
    },
    "19": {
      "L": "And he said, 'I will make all my goodness pass before you and will proclaim before you my name, the LORD. And I will be gracious to whom I will be gracious, and will show mercy on whom I will show mercy.'",
      "M": "And the LORD said, 'I will cause all my goodness to pass in front of you, and I will proclaim my name, the LORD, in your presence. I will have mercy on whom I will have mercy, and I will have compassion on whom I will have compassion.'",
      "T": "'I will make all my goodness pass before you, and I will proclaim my own name — the LORD — in your hearing. I will be gracious to whom I choose to be gracious, and I will show compassion on whom I choose to show compassion.' God's mercy is not mechanical; it flows from his sovereign character."
    },
    "20": {
      "L": "But he said, 'You cannot see my face, for man shall not see me and live.'",
      "M": "But,' he said, 'you cannot see my face, for no one may see me and live.'",
      "T": "'But my face you cannot see. No human being can see me and survive.'"
    },
    "21": {
      "L": "And the LORD said, 'Behold, there is a place by me where you shall stand on the rock,'",
      "M": "Then the LORD said, 'There is a place near me where you may stand on a rock.'",
      "T": "Then the LORD said, 'There is a place alongside me where you may stand — a rock.'"
    },
    "22": {
      "L": "'and while my glory passes by I will put you in a cleft of the rock, and I will cover you with my hand until I have passed by.'",
      "M": "'When my glory passes by, I will put you in a cleft in the rock and cover you with my hand until I have passed by.'",
      "T": "'While my glory passes by, I will shelter you in a cleft of the rock and cover you with my hand until I have gone past.'"
    },
    "23": {
      "L": "'Then I will take away my hand, and you shall see my back; but my face shall not be seen.'",
      "M": "'Then I will remove my hand and you will see my back; but my face must not be seen.'",
      "T": "'Then I will remove my hand, and you will see the afterglow of where I have been — my back. My face remains unseen.'"
    }
  },
  "34": {
    "1": {
      "L": "The LORD said to Moses, 'Cut for yourself two tablets of stone like the first, and I will write on the tablets the words that were on the first tablets, which you broke.'",
      "M": "The LORD said to Moses, 'Chisel out two stone tablets like the first ones, and I will write on them the words that were on the first tablets, which you broke.'",
      "T": "The LORD told Moses, 'Cut two stone tablets like the first ones — the ones you shattered. I will write on them again the same words that were on the first tablets.'"
    },
    "2": {
      "L": "'Be ready by the morning, and come up in the morning to Mount Sinai, and present yourself there to me on the top of the mountain.'",
      "M": "'Be ready in the morning, and then come up on Mount Sinai. Present yourself to me there on top of the mountain.'",
      "T": "'Be ready at first light. Come up Sinai in the morning and present yourself to me at the summit.'"
    },
    "3": {
      "L": "'No one shall come up with you, and let no one be seen throughout all the mountain. Let no flocks or herds graze opposite that mountain.'",
      "M": "'No one is to come with you or be seen anywhere on the mountain; not even the flocks and herds may graze in front of the mountain.'",
      "T": "'Come alone. No one else may be visible anywhere on the mountain — not even flocks or herds grazing near its base.'"
    },
    "4": {
      "L": "So Moses cut two tablets of stone like the first. And he rose early in the morning and went up on Mount Sinai, as the LORD had commanded him, and took in his hand two tablets of stone.",
      "M": "So Moses chiseled out two stone tablets like the first ones and went up Mount Sinai early in the morning, as the LORD had commanded him; and he carried the two stone tablets in his hands.",
      "T": "Moses cut two stone tablets like the first ones. He rose early in the morning, climbed Mount Sinai as the LORD had commanded, and carried the two stone tablets in his hands."
    },
    "5": {
      "L": "And the LORD descended in the cloud and stood with him there, and proclaimed the name of the LORD.",
      "M": "Then the LORD came down in the cloud and stood there with him and proclaimed his name, the LORD.",
      "T": "The LORD descended in the cloud and stood there with Moses. He proclaimed his own name: the LORD."
    },
    "6": {
      "L": "The LORD passed before him and proclaimed, 'The LORD, the LORD, a God merciful and gracious, slow to anger, and abounding in steadfast love and faithfulness,'",
      "M": "And he passed in front of Moses, proclaiming, 'The LORD, the LORD, the compassionate and gracious God, slow to anger, abounding in faithful love and faithfulness,'",
      "T": "The LORD passed before him and proclaimed his own character: 'The LORD, the LORD — compassionate and gracious, unhurried in anger, overflowing with covenant loyalty and absolute faithfulness,'"
    },
    "7": {
      "L": "'keeping steadfast love for thousands, forgiving iniquity and transgression and sin, but who will by no means clear the guilty, visiting the iniquity of the fathers on the children and the children's children, to the third and the fourth generation.'",
      "M": "'maintaining faithful love to thousands, and forgiving wickedness, rebellion and sin. Yet he does not leave the guilty unpunished; he punishes the children and their children for the sin of the parents to the third and fourth generation.'",
      "T": "'bearing covenant loyalty for thousands of generations, forgiving iniquity and rebellion and sin — yet who will by no means let the guilty go unpunished, carrying the consequences of a father's guilt into the third and fourth generation.' This is the creedal heart of the Hebrew Bible — grace and holiness held together without compromise."
    },
    "8": {
      "L": "And Moses quickly bowed his head toward the earth and worshiped.",
      "M": "Moses bowed to the ground at once and worshiped.",
      "T": "Moses dropped to the ground and worshiped."
    },
    "9": {
      "L": "And he said, 'If now I have found favor in your sight, O Lord, please let the Lord go in the midst of us, for it is a stiff-necked people, and pardon our iniquity and our sin, and take us for your inheritance.'",
      "M": "'Lord, if I have found favor in your eyes,' he said, 'then let the Lord go with us. Although this is a stiff-necked people, forgive our wickedness and our sin, and take us as your inheritance.'",
      "T": "He prayed, 'Lord — if I have truly found favor with you — go among us, even though we are stiff-necked. Forgive our iniquity and our sin, and claim us as your own inheritance. Do not abandon what belongs to you.'"
    },
    "10": {
      "L": "And he said, 'Behold, I am making a covenant. Before all your people I will do wonders, such as have not been created in all the earth or in any nation. And all the people among whom you are shall see the work of the LORD, for it is a terrifying thing that I will do with you.'",
      "M": "Then the LORD said: 'I am making a covenant with you. Before all your people I will do wonders never before done in any nation in all the world. The people you live among will see how awesome is the work that I, the LORD, will do for you.'",
      "T": "The LORD declared, 'I am making a covenant. Before all your people I will perform wonders — things that have never been done in any nation anywhere on earth. All the peoples surrounding you will see the awesome work of the LORD that I am doing with you.'"
    },
    "11": {
      "L": "'Observe what I command you this day. Behold, I will drive out before you the Amorites, the Canaanites, the Hittites, the Perizzites, the Hivites, and the Jebusites.'",
      "M": "'Obey what I command you today. I will drive out before you the Amorites, Canaanites, Hittites, Perizzites, Hivites and Jebusites.'",
      "T": "'Keep carefully what I command you today. I will drive out before you the Amorites, Canaanites, Hittites, Perizzites, Hivites, and Jebusites.'"
    },
    "12": {
      "L": "'Take care, lest you make a covenant with the inhabitants of the land to which you go, lest it become a snare in your midst.'",
      "M": "'Be careful not to make a treaty with those who live in the land where you are going, or they will be a snare among you.'",
      "T": "'Be on your guard. Do not make any treaty with the people of the land you are entering — that path leads to a trap.'"
    },
    "13": {
      "L": "'You shall tear down their altars and break their pillars and cut down their Asherah poles.'",
      "M": "'Break down their altars, smash their sacred stones and cut down their Asherah poles.'",
      "T": "'Tear down their altars, shatter their sacred pillars, chop down their Asherah poles.'"
    },
    "14": {
      "L": "'For you shall not worship any other god, for the LORD, whose name is Jealous, is a jealous God.'",
      "M": "'Do not worship any other god, for the LORD, whose name is Jealous, is a jealous God.'",
      "T": "'Worship no other god. The LORD's name is Jealous — he is a God who does not share what belongs to him.'"
    },
    "15": {
      "L": "'Lest you make a covenant with the inhabitants of the land, and they whore after their gods and sacrifice to their gods and invite you, and you eat of his sacrifice,'",
      "M": "'Be careful not to make a treaty with those who live in the land; for when they prostitute themselves to their gods and sacrifice to them, they will invite you and you will eat their sacrifices.'",
      "T": "'Do not make treaties with the people of the land. When they offer sacrifices to their gods and invite you to eat, you will go — and the first step down that road ends in spiritual prostitution.'"
    },
    "16": {
      "L": "'and you take of their daughters for your sons, and their daughters whore after their gods and make your sons whore after their gods.'",
      "M": "'And when you choose some of their daughters as wives for your sons and those daughters prostitute themselves to their gods, they will lead your sons to do the same.'",
      "T": "'When your sons marry their daughters, those daughters will draw your sons after their gods. Generation by generation, the infection spreads.'"
    },
    "17": {
      "L": "'You shall not make for yourself any molten gods.'",
      "M": "'Do not make any idols.'",
      "T": "'Cast no metal gods for yourselves.'"
    },
    "18": {
      "L": "'The Feast of Unleavened Bread you shall keep. Seven days you shall eat unleavened bread, as I commanded you, at the time appointed in the month Abib; for in the month Abib you came out from Egypt.'",
      "M": "'Celebrate the Festival of Unleavened Bread. For seven days eat bread made without yeast, as I commanded you. Do this at the appointed time in the month of Abib, for in that month you came out of Egypt.'",
      "T": "'Keep the Feast of Unleavened Bread — seven days of unleavened bread at the appointed time in the month of Abib, the month you marched out of Egypt. Let the bread itself remember the exodus.'"
    },
    "19": {
      "L": "'All that opens the womb is mine, all your male livestock, the firstborn of cow and sheep.'",
      "M": "'The first offspring of every womb belongs to me, including all the firstborn males of your livestock, whether from herd or flock.'",
      "T": "'Every firstborn belongs to me — the first to open every womb among your livestock, cattle and sheep alike.'"
    },
    "20": {
      "L": "'The firstborn of a donkey you shall redeem with a lamb, or if you will not redeem it you shall break its neck. All the firstborn of your sons you shall redeem. And none shall appear before me empty-handed.'",
      "M": "'Redeem the firstborn donkey with a lamb, but if you do not redeem it, break its neck. Redeem all your firstborn sons. No one is to appear before me empty-handed.'",
      "T": "'The firstborn donkey — redeem it with a lamb, or break its neck. All your firstborn sons must be redeemed. When you come before me, come with something in your hands.'"
    },
    "21": {
      "L": "'Six days you shall work, but on the seventh day you shall rest. In plowing time and in harvest you shall rest.'",
      "M": "'Six days you shall labor, but on the seventh day you shall rest; even during the plowing season and harvest you must rest.'",
      "T": "'Work six days; rest the seventh — even in plowing season, even in harvest. The Sabbath bends for no emergency.'"
    },
    "22": {
      "L": "'You shall observe the Feast of Weeks, the firstfruits of wheat harvest, and the Feast of Ingathering at the year's end.'",
      "M": "'Celebrate the Festival of Weeks with the firstfruits of the wheat harvest, and the Festival of Ingathering at the turn of the year.'",
      "T": "'Keep the Feast of Weeks — the firstfruits of the wheat harvest — and the Feast of Ingathering at year's end.'"
    },
    "23": {
      "L": "'Three times in the year shall all your males appear before the LORD God, the God of Israel.'",
      "M": "'Three times a year all your men are to appear before the Sovereign LORD, the God of Israel.'",
      "T": "'Three times every year all your men shall appear before the LORD, the God of Israel.'"
    },
    "24": {
      "L": "'For I will cast out nations before you and enlarge your borders; no one shall covet your land, when you go up to appear before the LORD your God three times in the year.'",
      "M": "'I will drive out nations before you and enlarge your territory, and no one will covet your land when you go up three times each year to appear before the LORD your God.'",
      "T": "'I will dispossess the nations before you and enlarge your territory. And when you go up to appear before me three times a year, I will keep your land safe — no one will covet it while you are away.'"
    },
    "25": {
      "L": "'You shall not offer the blood of my sacrifice with anything leavened, or let the sacrifice of the Feast of the Passover remain until the morning.'",
      "M": "'Do not offer the blood of a sacrifice to me along with anything containing yeast, and do not let any of the sacrifice from the Passover Festival remain until morning.'",
      "T": "'Do not offer my sacrificial blood alongside anything leavened. Do not let the Passover sacrifice remain through the night.'"
    },
    "26": {
      "L": "'The best of the firstfruits of your ground you shall bring to the house of the LORD your God. You shall not boil a young goat in its mother's milk.'",
      "M": "'Bring the best of the firstfruits of your soil to the house of the LORD your God. Do not cook a young goat in its mother's milk.'",
      "T": "'Bring the finest of your firstfruits to the house of the LORD your God. Do not boil a kid in its mother's milk — do not use the source of life to destroy life.'"
    },
    "27": {
      "L": "And the LORD said to Moses, 'Write these words, for in accordance with these words I have made a covenant with you and with Israel.'",
      "M": "Then the LORD said to Moses, 'Write down these words, for in accordance with these words I have made a covenant with you and with Israel.'",
      "T": "The LORD told Moses, 'Write down these words — for by these words I have sealed my covenant with you and with Israel.'"
    },
    "28": {
      "L": "So he was there with the LORD forty days and forty nights. He neither ate bread nor drank water. And he wrote on the tablets the words of the covenant, the ten words.",
      "M": "Moses was there with the LORD forty days and forty nights without eating bread or drinking water. And he wrote on the tablets the words of the covenant—the Ten Commandments.",
      "T": "Moses remained on the mountain with the LORD forty days and forty nights, eating nothing, drinking nothing. He wrote on the tablets the words of the covenant — the Ten Words, the Decalogue."
    },
    "29": {
      "L": "When Moses came down from Mount Sinai, with the two tablets of the testimony in his hand as he came down from the mountain, Moses did not know that the skin of his face shone because he had been talking with God.",
      "M": "When Moses came down from Mount Sinai with the two tablets of the covenant law in his hands, he was not aware that his face was radiant because he had spoken with the LORD.",
      "T": "Moses came down from Sinai carrying the two covenant tablets. He did not know that the skin of his face had become radiant from his conversation with God."
    },
    "30": {
      "L": "Aaron and all the children of Israel saw Moses, and behold, the skin of his face shone, and they were afraid to come near him.",
      "M": "When Aaron and all the Israelites saw Moses, his face was radiant, and they were afraid to come near him.",
      "T": "Aaron and all Israel looked at Moses — his face blazed with light. They were afraid to approach him."
    },
    "31": {
      "L": "But Moses called to them, and Aaron and all the rulers of the congregation returned to him, and Moses talked with them.",
      "M": "But Moses called to them; so Aaron and all the leaders of the community came back to him, and he spoke to them.",
      "T": "Moses called to them. Aaron and all the community leaders came back to him, and Moses spoke with them."
    },
    "32": {
      "L": "Afterward all the children of Israel came near, and he commanded them all that the LORD had spoken with him on Mount Sinai.",
      "M": "Afterward all the Israelites came near him, and he gave them all the commands the LORD had given him on Mount Sinai.",
      "T": "Then all of Israel came near. Moses gave them every command the LORD had spoken with him on Sinai."
    },
    "33": {
      "L": "And when Moses had finished speaking with them, he put a veil over his face.",
      "M": "When Moses finished speaking to them, he put a veil over his face.",
      "T": "When Moses finished speaking, he covered his face with a veil."
    },
    "34": {
      "L": "But whenever Moses went in before the LORD to speak with him, he would remove the veil, until he came out. And when he came out and told the people of Israel what he was commanded,",
      "M": "But whenever he entered the LORD's presence to speak with him, he removed the veil until he came out. And when he came out and told the Israelites what he had been commanded,",
      "T": "But whenever Moses went in before the LORD to speak with him, he removed the veil — and left it off until he came out. Coming out, he told the people what he had been commanded."
    },
    "35": {
      "L": "the people of Israel would see the face of Moses, that the skin of Moses' face shone. And Moses would put the veil over his face again, until he went in to speak with him.",
      "M": "they saw that his face was radiant. Then Moses would put the veil back over his face until he went in to speak with the LORD.",
      "T": "The people could see Moses' face blazing with light. Then Moses would replace the veil until the next time he went in to speak with God."
    }
  },
  "35": {
    "1": {
      "L": "Moses assembled all the congregation of the children of Israel and said to them, 'These are the things that the LORD has commanded you to do:'",
      "M": "Moses assembled the whole Israelite community and said to them, 'These are the things the LORD has commanded you to do:'",
      "T": "Moses gathered the whole community of Israel and said, 'These are the things the LORD has commanded you to do:'"
    },
    "2": {
      "L": "'Six days work shall be done, but on the seventh day there shall be to you a holy day, a Sabbath of solemn rest to the LORD; whoever does any work on it shall be put to death.'",
      "M": "'For six days, work is to be done, but the seventh day shall be your holy day, a day of sabbath rest to the LORD. Whoever does any work on it is to be put to death.'",
      "T": "'Six days you may work, but the seventh day shall be holy to you — a Sabbath of complete rest for the LORD. Whoever does any work on it must be put to death.'"
    },
    "3": {
      "L": "'You shall kindle no fire in all your dwelling places on the Sabbath day.'",
      "M": "'Do not light a fire in any of your dwellings on the Sabbath day.'",
      "T": "'On the Sabbath day, light no fire in any of your homes.' Even the work of building the tabernacle must yield to the Sabbath."
    },
    "4": {
      "L": "Moses said to all the congregation of the children of Israel, 'This is the thing that the LORD has commanded, saying:'",
      "M": "Moses said to the whole Israelite community, 'This is what the LORD has commanded:'",
      "T": "Moses addressed the whole assembly of Israel: 'This is what the LORD has commanded:'"
    },
    "5": {
      "L": "'Take from among you a contribution to the LORD; whoever is of a willing heart, let him bring the LORD's contribution: gold, silver, and bronze;'",
      "M": "'From what you have, take an offering for the LORD. Everyone who is willing is to bring to the LORD an offering of gold, silver and bronze;'",
      "T": "'From what you have, bring an offering to the LORD. Let everyone whose heart is willing bring gold, silver, and bronze;'"
    },
    "6": {
      "L": "'blue and purple and scarlet yarns and fine twined linen, and goats' hair;'",
      "M": "'blue, purple and scarlet yarn and fine linen; goat hair;'",
      "T": "'blue, purple, and scarlet thread, fine linen, goats' hair;'"
    },
    "7": {
      "L": "'ram skins dyed red, and goatskins, and acacia wood;'",
      "M": "'ram skins dyed red, another type of durable leather; acacia wood;'",
      "T": "'rams' skins dyed red, fine leather, acacia wood;'"
    },
    "8": {
      "L": "'oil for the light, spices for the anointing oil and for the fragrant incense;'",
      "M": "'olive oil for the light, spices for the anointing oil and for the fragrant incense;'",
      "T": "'oil for the lampstand, spices for the anointing oil and the aromatic incense;'"
    },
    "9": {
      "L": "'onyx stones and stones to be set, for the ephod and for the breastpiece.'",
      "M": "'and onyx stones and other gems to be mounted on the ephod and breastpiece.'",
      "T": "'onyx stones and other gemstones to be set in the ephod and the breastpiece.'"
    },
    "10": {
      "L": "'And let every skillful craftsman among you come and make all that the LORD has commanded:'",
      "M": "'All who are skilled among you are to come and make everything the LORD has commanded:'",
      "T": "'Let every craftsman with skill come and make all that the LORD has commanded:'"
    },
    "11": {
      "L": "'the tabernacle, its tent and its covering, its clasps and its frames, its bars, its pillars, and its bases;'",
      "M": "'the tabernacle with its tent and its covering, clasps, frames, crossbars, posts and bases;'",
      "T": "'the tabernacle — its tent and outer covering, its clasps, frames, crossbars, posts, and bases;'"
    },
    "12": {
      "L": "'the ark with its poles, the mercy seat, and the veil of the screen;'",
      "M": "'the ark with its poles and the atonement cover, and the curtain that shields it;'",
      "T": "'the ark with its poles, the atonement cover, the inner veil that shields it;'"
    },
    "13": {
      "L": "'the table with its poles and all its utensils, and the bread of the Presence;'",
      "M": "'the table with its poles and all its articles and the bread of the Presence;'",
      "T": "'the table with its poles and all its vessels, the bread of the Presence;'"
    },
    "14": {
      "L": "'the lampstand also for the light, with its utensils and its lamps, and the oil for the light;'",
      "M": "'the lampstand that is for light with its accessories, lamps and oil for the light;'",
      "T": "'the lampstand for the light with its fittings, its lamps, and oil for the light;'"
    },
    "15": {
      "L": "'and the altar of incense, with its poles, and the anointing oil, and the fragrant incense, and the screen for the entrance, at the door of the tabernacle;'",
      "M": "'the altar of incense with its poles, the anointing oil and the fragrant incense, and the curtain for the entrance to the tabernacle;'",
      "T": "'the incense altar and its poles, the anointing oil and the aromatic incense, the curtain for the tabernacle entrance;'"
    },
    "16": {
      "L": "'the altar of burnt offering with its bronze grating, its poles, and all its utensils, the basin and its stand;'",
      "M": "'the altar of burnt offering with its bronze grating, its poles and all its utensils, the bronze basin with its stand;'",
      "T": "'the altar of burnt offering with its bronze grate, poles, and all equipment, the bronze washbasin and its base;'"
    },
    "17": {
      "L": "'the hangings of the court, its pillars and its bases, and the screen for the gate of the court;'",
      "M": "'the curtains of the courtyard with its posts and bases, and the curtain for the entrance to the courtyard;'",
      "T": "'the courtyard hangings with their posts and bases, the curtain for the courtyard gate;'"
    },
    "18": {
      "L": "'the pegs of the tabernacle and the pegs of the court, and their cords;'",
      "M": "'the tent pegs for the tabernacle and for the courtyard, and their ropes;'",
      "T": "'the tent pegs for the tabernacle and courtyard with their cords;'"
    },
    "19": {
      "L": "'the finely worked garments for ministering in the holy place, the holy garments for Aaron the priest, and the garments of his sons, for their service as priests.'",
      "M": "'the woven garments worn for ministering in the sanctuary—both the sacred garments for Aaron the priest and the garments for his sons when they serve as priests.'",
      "T": "'the woven vestments for serving in the sanctuary — the sacred garments for Aaron the priest and the garments for his sons in their priestly service.'"
    },
    "20": {
      "L": "Then all the congregation of the children of Israel departed from the presence of Moses.",
      "M": "Then the whole Israelite community withdrew from Moses' presence.",
      "T": "The whole community of Israel withdrew from before Moses."
    },
    "21": {
      "L": "And they came, everyone whose heart stirred him, and everyone whose spirit moved him, and brought the LORD's contribution to be used for the tent of meeting, and for all its service, and for the holy garments.",
      "M": "And everyone who was willing and whose heart moved them came and brought an offering to the LORD for the work on the tent of meeting, for all its service, and for the sacred garments.",
      "T": "Then they came — everyone whose heart was stirred, everyone whose spirit moved them — and brought offerings to the LORD for the Tent of Meeting, for all its service, and for the sacred garments."
    },
    "22": {
      "L": "So they came, both men and women. All who were of a willing heart brought brooches and earrings and signet rings and armlets, all sorts of gold objects, every man dedicating an offering of gold to the LORD.",
      "M": "All who were willing, men and women alike, came and brought gold jewelry of all kinds: brooches, earrings, rings and ornaments. They all presented their gold as a wave offering to the LORD.",
      "T": "Men and women together — all with willing hearts — brought brooches, earrings, signet rings, armbands, every kind of gold ornament. They lifted their gold as an offering to the LORD."
    },
    "23": {
      "L": "And everyone who possessed blue or purple or scarlet yarns or fine linen or goats' hair or tanned rams' skins or goatskins brought them.",
      "M": "Everyone who had blue, purple or scarlet yarn or fine linen, or goat hair, ram skins dyed red or the other durable leather brought them.",
      "T": "Everyone who had blue, purple, or scarlet yarn, fine linen, goats' hair, red-dyed rams' skins, or fine leather brought them."
    },
    "24": {
      "L": "Everyone who could make a contribution of silver or bronze brought it as the LORD's contribution. And everyone who possessed acacia wood of any use in the work brought it.",
      "M": "Those presenting an offering of silver or bronze brought it as an offering to the LORD, and everyone who had acacia wood for any part of the work brought it.",
      "T": "Those with silver or bronze brought their contributions. Those with acacia wood brought it if it could be used in the work."
    },
    "25": {
      "L": "And every skillful woman spun with her hands, and they all brought what they had spun in blue and purple and scarlet yarns and fine twined linen.",
      "M": "Every skilled woman spun with her hands and brought what she had spun—blue, purple or scarlet yarn or fine linen.",
      "T": "Every woman with skill in spinning worked with her hands and brought what she had made — blue, purple, scarlet yarn, and fine linen."
    },
    "26": {
      "L": "All the women whose hearts stirred them with skill spun the goats' hair.",
      "M": "And all the women who were willing and had the skill spun the goat hair.",
      "T": "And all the women whose hearts were stirred and whose hands were skilled spun the goats' hair."
    },
    "27": {
      "L": "And the leaders brought onyx stones and stones to be set, for the ephod and for the breastpiece,",
      "M": "The leaders brought onyx stones and other gems to be mounted on the ephod and breastpiece.",
      "T": "The leaders contributed the onyx stones and gemstones for the ephod and breastpiece."
    },
    "28": {
      "L": "and spices and oil for the light, and for the anointing oil, and for the fragrant incense.",
      "M": "They also brought spices and olive oil for the light, for the anointing oil, and for the fragrant incense.",
      "T": "They also brought spices and oil — for the lampstand, for the anointing oil, and for the aromatic incense."
    },
    "29": {
      "L": "All the men and women, the children of Israel, whose heart moved them freely to bring anything for the work that the LORD had commanded by Moses to be done brought it as a freewill offering to the LORD.",
      "M": "All the Israelite men and women who were willing brought to the LORD freewill offerings for all the work the LORD through Moses had commanded them to do.",
      "T": "Every Israelite man and woman whose heart moved them freely brought it — everything given was a gift of an open hand, a freewill offering to the LORD for all the work Moses had commanded."
    },
    "30": {
      "L": "Then Moses said to the children of Israel, 'See, the LORD has called by name Bezalel the son of Uri, the son of Hur, of the tribe of Judah;'",
      "M": "Then Moses said to the Israelites, 'See, the LORD has chosen Bezalel son of Uri, the son of Hur, of the tribe of Judah,'",
      "T": "Moses told the Israelites, 'Look — the LORD has called by name Bezalel son of Uri son of Hur, of the tribe of Judah.'"
    },
    "31": {
      "L": "'and he has filled him with the Spirit of God, with skill, with intelligence, with knowledge, and with all craftsmanship,'",
      "M": "'and he has filled him with the Spirit of God, with wisdom, with understanding, with knowledge and with all kinds of skills—'",
      "T": "'He has filled him with the Spirit of God — wisdom, understanding, knowledge, mastery in every craft —'"
    },
    "32": {
      "L": "'to devise artistic works, to work in gold and in silver and in bronze,'",
      "M": "'to make artistic designs for work in gold, silver and bronze,'",
      "T": "'to design and execute work in gold, silver, and bronze,'"
    },
    "33": {
      "L": "'in cutting of stones for setting, and in carving of wood, to work in every skillful craft.'",
      "M": "'to cut and set stones, to work in wood and to engage in all kinds of artistic crafts.'",
      "T": "'to cut and set stones, to carve wood — every skilled craft.'"
    },
    "34": {
      "L": "'And he has put in his heart the ability to teach, both he and Oholiab the son of Ahisamach of the tribe of Dan.'",
      "M": "'And he has given both him and Oholiab son of Ahisamach, of the tribe of Dan, the ability to teach others.'",
      "T": "'And he has given both Bezalel and Oholiab son of Ahisamach of the tribe of Dan the gift of teaching — not only to make but to transmit the skill.'"
    },
    "35": {
      "L": "'He has filled them with skill to do every sort of work done by an engraver or by a designer or by an embroiderer in blue and purple and scarlet yarns and fine twined linen, and by a weaver — by any sort of workman or skilled designer.'",
      "M": "'He has filled them with skill to do all kinds of work as engravers, designers, embroiderers in blue, purple and scarlet yarn and fine linen, and weavers—all of them skilled workers and designers.'",
      "T": "'He has filled them with every skill needed — engraving, designing, embroidering in blue, purple, and scarlet thread and fine linen, weaving — every kind of skilled work and artistic design.'"
    }
  },
  "36": {
    "1": {
      "L": "Bezalel and Oholiab and every craftsman in whom the LORD has put skill and understanding to know how to do any work in the construction of the sanctuary shall work in accordance with all that the LORD has commanded.",
      "M": "So Bezalel, Oholiab and every skilled person to whom the LORD has given skill and ability to know how to carry out all the work of constructing the sanctuary are to do the work just as the LORD has commanded.",
      "T": "Bezalel and Oholiab and every craftsman in whom the LORD had placed skill and understanding — everyone capable of doing the sanctuary work — were to carry it out exactly as the LORD had commanded."
    },
    "2": {
      "L": "And Moses called Bezalel and Oholiab and every craftsman in whose mind the LORD had put skill, everyone whose heart stirred him up to come to do the work.",
      "M": "Then Moses summoned Bezalel and Oholiab and every skilled person to whom the LORD had given ability and who was willing to come and do the work.",
      "T": "Moses summoned Bezalel and Oholiab and every craftsman the LORD had gifted — everyone whose heart moved them to come forward and do the work."
    },
    "3": {
      "L": "And they received from Moses all the contribution that the children of Israel had brought for doing the work on the sanctuary. They still kept bringing him freewill offerings every morning,",
      "M": "They received from Moses all the offerings the Israelites had brought to carry out the work of constructing the sanctuary. And the people continued to bring freewill offerings morning after morning.",
      "T": "They received from Moses all the contributions the Israelites had brought. And still the people kept bringing freewill offerings morning after morning."
    },
    "4": {
      "L": "so that all the craftsmen who were doing every sort of task on the sanctuary came, each from the task that he was doing,",
      "M": "So all the skilled workers who were doing all the work on the sanctuary left what they were doing",
      "T": "The craftsmen working on the sanctuary had to stop what they were doing"
    },
    "5": {
      "L": "and said to Moses, 'The people bring much more than enough for doing the work that the LORD has commanded us to do.'",
      "M": "and said to Moses, 'The people are bringing more than enough for doing the work the LORD commanded to be done.'",
      "T": "and came to Moses with an extraordinary report: 'The people are bringing far more than we need for all this work.'"
    },
    "6": {
      "L": "So Moses gave command, and word was proclaimed throughout the camp, 'Let no man or woman do anything more for the contribution for the sanctuary.' So the people were restrained from bringing,",
      "M": "Then Moses gave an order and they sent this word throughout the camp: 'No man or woman is to make anything else as an offering for the sanctuary.' And so the people were restrained from bringing more,",
      "T": "Moses issued an order, and it was proclaimed throughout the camp: 'No man or woman is to bring any more for the sanctuary offering.' The people were stopped from bringing."
    },
    "7": {
      "L": "for the material they had was sufficient to do all the work, and more.",
      "M": "because what they already had was more than enough to do all the work.",
      "T": "What they had already given was more than sufficient for all the work — and then some."
    },
    "8": {
      "L": "And all the skilled craftsmen among those who worked made the tabernacle with ten curtains of fine twined linen and blue and purple and scarlet yarns; with cherubim skillfully worked they made them.",
      "M": "All those who were skilled among the workers made the tabernacle with ten curtains of finely twisted linen and blue, purple and scarlet yarn, with cherubim woven into them by expert hands.",
      "T": "The skilled craftsmen made the tabernacle itself with ten curtains of fine twisted linen — blue, purple, and scarlet — with cherubim worked into them by expert hands."
    },
    "9": {
      "L": "The length of each curtain was twenty-eight cubits, and the breadth of each curtain four cubits; all the curtains were the same size.",
      "M": "Each curtain was twenty-eight cubits long and four cubits wide; all the curtains were the same size.",
      "T": "Each curtain measured twenty-eight cubits long and four cubits wide — all eleven were identical."
    },
    "10": {
      "L": "He coupled five of the curtains to one another, and the other five curtains he coupled to one another.",
      "M": "They joined five of the curtains together and did the same with the other five.",
      "T": "He joined five curtains together into one set and the remaining five into another set."
    },
    "11": {
      "L": "He made loops of blue on the edge of the outermost curtain of the first set. Likewise he made them on the edge of the outermost curtain of the second set.",
      "M": "Then they made loops of blue material along the edge of the end curtain in one set, and the same was done with the end curtain in the other set.",
      "T": "Along the outer edge of the last curtain in each set he made loops of blue thread, facing each other."
    },
    "12": {
      "L": "He made fifty loops on the one curtain, and he made fifty loops on the edge of the curtain that was in the second set. The loops were opposite one another.",
      "M": "They made fifty loops on one curtain and fifty loops on the end curtain of the other set, with the loops opposite each other.",
      "T": "Fifty loops on one side, fifty loops on the other — each loop aligned with its pair across the joining."
    },
    "13": {
      "L": "And he made fifty clasps of gold, and coupled the curtains one to the other with the clasps. So the tabernacle was a single whole.",
      "M": "Then they made fifty gold clasps and used them to fasten the two sets of curtains together so that the tabernacle was a unit.",
      "T": "He made fifty gold clasps and fastened the two sets of curtains together with them. The tabernacle became one unified whole."
    },
    "14": {
      "L": "He also made curtains of goats' hair for a tent over the tabernacle. He made eleven curtains.",
      "M": "They made curtains of goat hair for the tent over the tabernacle—eleven curtains in all.",
      "T": "He made an outer covering of eleven goats' hair curtains to go over the tabernacle."
    },
    "15": {
      "L": "The length of each curtain was thirty cubits, and the breadth of each curtain was four cubits. The eleven curtains were the same size.",
      "M": "Each curtain was thirty cubits long and four cubits wide; the eleven curtains were the same size.",
      "T": "Each curtain was thirty cubits long and four cubits wide — all eleven identical."
    },
    "16": {
      "L": "He coupled five of the curtains by themselves, and six curtains by themselves.",
      "M": "They joined five of the curtains together into one set and six curtains into another set.",
      "T": "He joined five curtains as one set and six as another."
    },
    "17": {
      "L": "He made fifty loops on the edge of the outermost curtain of the one set, and fifty loops on the edge of the curtain of the other connecting set.",
      "M": "Then they made fifty loops along the edge of the end curtain in one set and also along the edge of the end curtain of the second set.",
      "T": "Fifty loops on the outer edge of each set's connecting curtain, aligned to meet each other."
    },
    "18": {
      "L": "He made fifty clasps of bronze to couple the tent together that it might be a single whole.",
      "M": "Then they made fifty bronze clasps to fasten the tent together as a unit.",
      "T": "Fifty bronze clasps joined the tent into one whole."
    },
    "19": {
      "L": "And he made for the tent a covering of tanned rams' skins, and a covering of goatskins on top.",
      "M": "For the tent they made a covering of ram skins dyed red, and over that a covering of the other durable leather.",
      "T": "Over the tent he made an outer covering of red-dyed rams' skins and over that a layer of fine leather."
    },
    "20": {
      "L": "Then he made the upright frames for the tabernacle of acacia wood.",
      "M": "They made upright frames of acacia wood for the tabernacle.",
      "T": "He made the upright frames for the tabernacle from acacia wood."
    },
    "21": {
      "L": "Ten cubits was the length of a frame, and a cubit and a half was the breadth of each frame.",
      "M": "Each frame was ten cubits long and a cubit and a half wide,",
      "T": "Each frame stood ten cubits high and a cubit and a half wide."
    },
    "22": {
      "L": "Each frame had two tenons for fitting together. He did this for all the frames of the tabernacle.",
      "M": "with two projecting tabs parallel to each other. They made all the frames of the tabernacle in this way.",
      "T": "Each frame had two tenons for locking into bases — identical in construction, every one."
    },
    "23": {
      "L": "He made the frames for the tabernacle: twenty frames for the south side.",
      "M": "They made twenty frames for the south side of the tabernacle",
      "T": "Twenty frames for the south side of the tabernacle,"
    },
    "24": {
      "L": "And he made forty bases of silver under the twenty frames, two bases under one frame for its two tenons, and two bases under the next frame for its two tenons.",
      "M": "and made forty silver bases to go under them—two bases for each frame, one under each projection.",
      "T": "with forty silver bases beneath them — two bases under each frame, one for each tenon."
    },
    "25": {
      "L": "For the second side of the tabernacle, on the north side, he made twenty frames",
      "M": "For the other side, the north side of the tabernacle, they made twenty frames",
      "T": "Twenty frames for the north side,"
    },
    "26": {
      "L": "and their forty silver bases, two bases under one frame and two bases under the next frame.",
      "M": "and forty silver bases—two under each frame.",
      "T": "and forty silver bases — two under each frame."
    },
    "27": {
      "L": "For the rear of the tabernacle westward he made six frames.",
      "M": "For the far end, that is, the west end of the tabernacle, they made six frames,",
      "T": "For the rear wall — the western end — six frames."
    },
    "28": {
      "L": "He made two frames for corners of the tabernacle at the rear.",
      "M": "and two frames were made for the corners of the tabernacle at the far end.",
      "T": "And two frames for the two rear corners."
    },
    "29": {
      "L": "And they were separate at the bottom but joined at the top at the first ring. He did this for both of them; they formed the two corners.",
      "M": "At these two corners the frames were double from the bottom all the way to the top and fitted into a single ring; both were made alike.",
      "T": "The corner frames were joined at the bottom but met at the top in a single ring — both corners built the same way."
    },
    "30": {
      "L": "There were eight frames with their silver bases: sixteen bases, under every frame two bases.",
      "M": "So there were eight frames and sixteen silver bases—two under each frame.",
      "T": "Eight frames in all, sixteen silver bases — two under each frame."
    },
    "31": {
      "L": "He made bars of acacia wood, five for the frames of the one side of the tabernacle,",
      "M": "They also made crossbars of acacia wood: five for the frames on one side of the tabernacle,",
      "T": "Five crossbars of acacia wood for the frames along one side of the tabernacle,"
    },
    "32": {
      "L": "and five bars for the frames of the other side of the tabernacle, and five bars for the frames of the tabernacle at the rear westward.",
      "M": "five for those on the other side, and five for the frames on the west, at the far end of the tabernacle.",
      "T": "five for the other side, and five for the west end."
    },
    "33": {
      "L": "He made the middle bar to pass through the middle of the frames from end to end.",
      "M": "They made the center crossbar so that it extended from end to end at the middle of the frames.",
      "T": "He made the center bar to run the full length of the frames at mid-height, from one end to the other."
    },
    "34": {
      "L": "He overlaid the frames with gold and made their rings of gold for holders for the bars, and overlaid the bars with gold.",
      "M": "They overlaid the frames with gold and made gold rings to hold the crossbars. They also overlaid the crossbars with gold.",
      "T": "He covered the frames with gold, made gold rings to hold the crossbars, and covered the crossbars with gold."
    },
    "35": {
      "L": "He made the veil of blue and purple and scarlet yarns and fine twined linen; with cherubim skillfully worked he made it.",
      "M": "For the inner curtain they made a curtain of blue, purple and scarlet yarn and finely twisted linen, with cherubim woven into it by a skilled worker.",
      "T": "He made the inner veil — blue, purple, and scarlet thread with fine twisted linen — cherubim woven through it by expert hands."
    },
    "36": {
      "L": "And he made for it four pillars of acacia and overlaid them with gold. Their hooks were of gold, and he cast for them four bases of silver.",
      "M": "For the curtain they made four posts of acacia wood and overlaid them with gold. They made gold hooks for them and cast four silver bases for them.",
      "T": "For the veil he made four acacia posts covered with gold, with gold hooks, set in four silver bases."
    },
    "37": {
      "L": "He also made a screen for the entrance to the tent, of blue and purple and scarlet yarns and fine twined linen, embroidered with needlework,",
      "M": "For the entrance to the tent they made a curtain of blue, purple and scarlet yarn and finely twisted linen—the work of an embroiderer;",
      "T": "For the tent entrance he made a hanging curtain — blue, purple, and scarlet thread with fine twisted linen — the intricate work of an embroiderer."
    },
    "38": {
      "L": "and its five pillars with their hooks. He overlaid their capitals and their fillets with gold, but their five bases were of bronze.",
      "M": "and the five posts with their hooks. They overlaid the tops of the posts and their bands with gold and made their five bases of bronze.",
      "T": "Five posts with hooks, their capitals and connecting rods covered with gold — but the five bases were bronze."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'exodus')
        merge_tier(existing, EXODUS, tier_key)
        save(tier_dir, 'exodus', existing)
    print('Exodus 31–36 written.')

if __name__ == '__main__':
    main()
