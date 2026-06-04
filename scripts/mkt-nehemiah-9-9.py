"""
MKT Nehemiah chapter 9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-nehemiah-9-9.py

Translation decisions:
- H3068 (יהוה): "LORD" in L and M; "the LORD" in T — consistent with mkt-nehemiah-7-8.py.
- H430 (אֱלֹהִים): "God" throughout. The opening address "our God" (v6 onwards) is preserved
  as the characteristic prayer register of Nehemiah.
- H2617 (חֶסֶד) at vv17 and 32: "steadfast love" in L and M. T at v17 expands — hesed is
  covenant loyalty that structurally overflows what the covenant formally requires; the
  combination "slow to anger and abounding in steadfast love" is the classic covenant formula
  from Exodus 34:6. At v32 T notes that "keeps covenant and steadfast love" is shorthand for
  the full divine character declaration of Deut 10:17.
- H7307 (רוּחַ) at v20 ("your good Spirit") and v30 ("by your Spirit"): capital S in all tiers.
  Both instances unambiguously denote the divine Spirit — at v20 instructing Israel in the
  wilderness, at v30 speaking through the prophets. This is not wind or breath.
- H5547 (סַלָּח) at v17: a remarkable Hebrew hapax — a participial adjective meaning
  "habitually/characteristically forgiving." It occurs in the OT only as a description of God
  (Ps 86:5 and here). L renders "a God ready to forgive"; M "a God who forgives"; T surfaces
  the uniqueness: "the Forgiver by nature, always ready to forgive."
- H8451 (תּוֹרָה) at vv14 and 29: "law" in L/M. T uses "Torah" where the full covenant-charter
  sense is theologically important.
- H1285 (בְּרִית) at vv8 and 38: "covenant" throughout. At v38 the verb כּוֹרְתִים ("cutting
  a covenant") is surfaced in T — the ancient covenant-making ritual translated into written form.
- Leviticus 18:5 echo at v29 ("by which if a person does them, he shall live by them"): quoted
  directly by the prayer. T names the source — this is the foundational Mosaic statement about
  the Torah's life-giving character.
- Chapter structure: vv1-3 (context — assembly on 24th day with fasting/sackcloth);
  vv4-5 (Levites call the congregation); vv6-31 (the great historical prayer — creation through
  exile); vv32-37 (present petition); v38 (covenant commitment). The prayer is one of the
  longest in the OT and forms the theological spine of the Nehemiah narrative.
- The Judges-era cycle of vv27-28 is compressed but complete: sin → oppression → cry →
  deliverance → rest → sin. T names this as the pattern and traces its culmination in exile.
- Aspect: narrative past (waw-consecutive imperfect) throughout the historical sections;
  the petition in v32 moves to present/imperative. T's register shifts accordingly —
  narrative past in vv6-31 becomes urgent present in vv32-38.
- Exodus 34:6 parallel at v17: the combination of gracious, compassionate, slow to anger,
  abounding in steadfast love is the classic divine self-declaration at Sinai. T names the echo.
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
  "9": {
    "1": {
      "L": "Now on the twenty-fourth day of this month the children of Israel were assembled with fasting and with sackclothes and with earth upon them.",
      "M": "On the twenty-fourth day of this month, the Israelites gathered together with fasting, wearing sackcloth, and with dust on their heads.",
      "T": "Just two days after the great feast ended—on the twenty-fourth of the seventh month—the whole assembly shifted register. Where feasting had been, there was now fasting. Where fine booths had stood, there was now sackcloth and earth on their heads. The covenant renewal had passed from celebration into penitence."
    },
    "2": {
      "L": "And the seed of Israel separated themselves from all foreigners and stood and confessed their sins and the iniquities of their fathers.",
      "M": "The Israelites separated themselves from all foreigners. They stood and confessed their own sins and the iniquities of their ancestors.",
      "T": "The Israelites drew a deliberate boundary—they separated themselves from all who were not of the covenant people. Then they stood, the standing of accountability before God, and confessed. Not only their own sins, but those of their fathers. The great prayer that follows will carry this generational scope throughout."
    },
    "3": {
      "L": "And they stood in their place and read from the Book of the Law of the LORD their God for a quarter of the day, and for another quarter they confessed and worshiped the LORD their God.",
      "M": "Standing in their places, they read from the Book of the Law of the LORD their God for a quarter of the day; for another quarter they confessed their sins and worshiped the LORD their God.",
      "T": "The liturgy had two movements—each consuming roughly a quarter of the day, some three hours apiece. Three hours of the Torah read aloud. Three hours of confession and prostrate worship before the LORD their God. The word of God and the response of the people: hear, then confess; receive, then bow."
    },
    "4": {
      "L": "Then Jeshua, Bani, Kadmiel, Shebaniah, Bunni, Sherebiah, Bani, and Chenani stood on the platform of the Levites and cried out with a loud voice to the LORD their God.",
      "M": "Then Jeshua, Bani, Kadmiel, Shebaniah, Bunni, Sherebiah, Bani, and Chenani stood on the Levites' platform and cried out with a loud voice to the LORD their God.",
      "T": "Eight Levites mounted the elevated platform and raised their voices together in a great cry to the LORD. The cry (זָעַק) is not merely prayer—it is the desperate call of people in need, the same verb used when Israel cried out under Pharaoh in Egypt. Now they cry not against an earthly oppressor, but toward heaven itself."
    },
    "5": {
      "L": "Then the Levites—Jeshua, Kadmiel, Bani, Hashabneiah, Sherebiah, Hodiah, Shebaniah, and Pethahiah—said: 'Rise and bless the LORD your God from everlasting to everlasting. May your glorious name be blessed and exalted above all blessing and praise!'",
      "M": "Then the Levites—Jeshua, Kadmiel, Bani, Hashabneiah, Sherebiah, Hodiah, Shebaniah, and Pethahiah—said: 'Stand up and bless the LORD your God from everlasting to everlasting. Blessed be your glorious name—exalted above all blessing and praise!'",
      "T": "'Stand up—and bless the LORD your God,' the Levites called to the congregation. 'From everlasting to everlasting.' The crowd rose. Then came the opening doxology: 'May your glorious name be blessed and exalted far above all the blessing and praise that human lips can offer.' The prayer begins not with petition, not with confession, but with the declaration that God's name stands above everything that can be said of him."
    },
    "6": {
      "L": "You are the LORD, you alone. You made heaven, the heaven of heavens, with all their host, the earth and all that is on it, the seas and all that is in them; and you preserve them all; and the host of heaven worships you.",
      "M": "You alone are the LORD. You made the heavens, even the highest heaven, with all their host, the earth and everything on it, the seas and all they contain. You give life to all things, and the heavenly hosts bow in worship before you.",
      "T": "The prayer opens with creation, because everything else flows from it: 'You alone are the LORD.' Not one among many; not a regional deity; not a god among gods. You made the layered heavens—the visible sky and the highest heaven above it—and all their armies of stars and angels. You made the earth and the seas and every creature in them. You sustain all things. And before you, the host of heaven bows down. The foundation of everything that follows is ontological: the God we have sinned against is the Creator and Sustainer of all that exists."
    },
    "7": {
      "L": "You are the LORD the God who chose Abram and brought him out of Ur of the Chaldeans and gave him the name Abraham.",
      "M": "You are the LORD, the God who chose Abram and brought him out of Ur of the Chaldeans, giving him the name Abraham.",
      "T": "From creation the prayer moves immediately to election: you chose Abram. Not because of anything in him—the text makes no claim about his prior merit. You brought him out of Ur of the Chaldeans, that ancient Mesopotamian city, and gave him a new name: Abraham. The renaming is itself a covenant act—God gives a man a new identity that embeds the promise within it."
    },
    "8": {
      "L": "You found his heart faithful before you, and made with him the covenant to give the land of the Canaanites, the Hittites, the Amorites, the Perizzites, the Jebusites, and the Girgashites—to give it to his seed. And you have kept your words, for you are righteous.",
      "M": "You found his heart faithful before you and made a covenant with him to give his descendants the land of the Canaanites, the Hittites, the Amorites, the Perizzites, the Jebusites, and the Girgashites. You have kept your word, for you are righteous.",
      "T": "'You found his heart faithful before you'—the faithfulness God finds in Abraham is covenant loyalty, not sinless perfection. On the basis of that relationship God made the covenant: a formally sworn, oath-bound promise to give the land of six named nations to Abraham's descendants. And the prayer declares: you kept it. Not because Abraham's line deserved it, but because you are righteous—your character commits you to your word."
    },
    "9": {
      "L": "And you saw the affliction of our fathers in Egypt and heard their cry at the Red Sea.",
      "M": "You saw the affliction of our ancestors in Egypt and heard their cry at the Red Sea.",
      "T": "Egypt: the place of affliction—the Hebrew word connotes brutal degradation. God saw it. Then when the armies closed in and the water lay ahead, God heard their cry at the sea. The two verbs—'saw' and 'heard'—deliberately echo Exodus 2:24-25, the moment God turned his face toward Israel's bondage. The prayer cites that pattern because it is the pattern being invoked now."
    },
    "10": {
      "L": "And you performed signs and wonders against Pharaoh and all his servants and all the people of his land, for you knew that they acted arrogantly against our fathers. And you made yourself a name, as it is to this day.",
      "M": "You performed signs and wonders against Pharaoh and all his servants and all the people of his land, because you knew how arrogantly they treated our ancestors. And you made for yourself a name that endures to this day.",
      "T": "The plagues were not merely liberation—they were public judgment. God performed signs and wonders against Pharaoh, his court, and his whole people, because God knew their arrogance. The Hebrew verb (זוּד) for 'acted arrogantly' carries the sense of deliberate, knowing defiance—they knew better and chose defiance. The result was a Name: God established his reputation in the Exodus, a reputation that endures to this day, testified in scripture and repeated in the prayers of every generation."
    },
    "11": {
      "L": "And you divided the sea before them, so that they went through the sea on dry ground, and their pursuers you cast into the depths as a stone into mighty waters.",
      "M": "You divided the sea before them, so they walked through it on dry ground. You hurled their pursuers into the depths like a stone thrown into mighty waters.",
      "T": "The sea parted. Israel walked through on dry ground. The Egyptian army God threw into the depths like a stone—not a struggle at the water's edge, but a single decisive cast. The image is from the Song of Moses (Exodus 15:5), and the prayer is praying the scriptures back to God: what you did then, you can do again."
    },
    "12": {
      "L": "In a pillar of cloud you led them by day, and in a pillar of fire by night to light the way for them by which they should go.",
      "M": "You guided them with a pillar of cloud by day and a pillar of fire by night to illuminate the path they should take.",
      "T": "Through the wilderness God made himself present in visible form: a column of cloud that moved by day, a column of fire that blazed by night. Navigation and protection in one. The people never lacked guidance—God's own presence was the light ahead of them. The prayer rehearses these provisions of grace because they preceded, and outlasted, Israel's repeated failures."
    },
    "13": {
      "L": "You came down on Mount Sinai and spoke with them from heaven and gave them right ordinances and true laws, good statutes and commandments.",
      "M": "You came down on Mount Sinai and spoke with them from heaven. You gave them just ordinances and true laws, and good statutes and commandments.",
      "T": "Sinai: God descended—the verb is vivid and physical—and yet spoke from heaven simultaneously. The paradox of transcendence meeting immanence. What he gave was not arbitrary: the ordinances were right (יָשָׁר—straight, honest, corresponding to reality), the laws were true (אֱמֶת), the statutes and commandments were good. This is the prayer's counter to Israel's later rejection: the law you were given was not a burden. It was a gift. It was right and true and good."
    },
    "14": {
      "L": "And you made known to them your holy Sabbath and commanded them commandments, statutes, and a law through Moses your servant.",
      "M": "You revealed your holy Sabbath to them and gave them commandments, statutes, and law through Moses your servant.",
      "T": "Among all the Sinai gifts, the Sabbath is singled out: 'your holy Sabbath'—not merely a rest day but belonging to God, marked off as his own. The summary that follows names the full Mosaic corpus: commandments (specific directives), statutes (categorical laws), and the Torah as a whole—all delivered through Moses, who is here given the highest honorific the prayer knows: 'your servant.'"
    },
    "15": {
      "L": "Bread from heaven you gave them for their hunger, and water from the rock you brought out for their thirst, and you told them to go in and possess the land that you had sworn to give them.",
      "M": "You gave them bread from heaven when they were hungry and brought water out of the rock when they were thirsty. You commanded them to go in and take possession of the land you had sworn to give them.",
      "T": "Manna and water from the rock: two miracles that sustained life in a place where life could not otherwise be sustained. And alongside the provision came the promise renewed: 'Go in and possess the land I swore to give you.' Every act of provision in the wilderness was simultaneously a step toward the destination. God's grace was not an end in itself—it was moving Israel toward home."
    },
    "16": {
      "L": "But they and our fathers dealt presumptuously and hardened their neck and did not heed your commandments.",
      "M": "But they—our ancestors—acted arrogantly, stiffened their necks, and refused to obey your commandments.",
      "T": "Here the prayer pivots: 'But they.' All that grace—all that guidance, all that bread, all that water, all those words at Sinai—and they acted with presumption (זוּד again, the deliberate arrogance of people who know what they are doing). They hardened their necks—the image of an ox that will not accept the yoke—and would not listen. The prayer says 'they and our fathers': the assembly praying in the ruins of exile does not exempt itself from the pattern."
    },
    "17": {
      "L": "They refused to listen and were not mindful of the wonders you did among them, but they hardened their neck, and in their rebellion they appointed a leader to return to their slavery in Egypt. But you are a God ready to forgive, gracious and compassionate, slow to anger and abounding in steadfast love, and you did not forsake them.",
      "M": "They refused to obey and forgot the wonders you performed for them. They stiffened their neck and, in their rebellion, appointed a leader to take them back to slavery in Egypt. But you are a God who forgives—gracious and compassionate, slow to anger and abounding in steadfast love—and you did not abandon them.",
      "T": "The rebellion reached its nadir: the people proposed to elect a new leader and march back to Egypt—back to slavery, back to chains—rather than trust the God who had brought them this far. It is the most astonishing betrayal imaginable. And yet: 'But you.' The prayer's first great turning. God is declared to be: the Forgiver by nature, habitually and characteristically ready to forgive (H5547 סַלָּח—a Hebrew participial form that occurs as a divine description only here and in Psalm 86:5); gracious (חַנּוּן); compassionate (רַחוּם); slow to anger; abounding in steadfast love (חֶסֶד)—the classic covenant formula of Exodus 34:6, repeated here in full. And because of all this, he did not forsake them. The first 'but you' in Israel's prayer is not an excuse; it is a declaration of God's character."
    },
    "18": {
      "L": "Even when they had made for themselves a golden calf and said, 'This is your God who brought you up out of Egypt,' and had committed great blasphemies—",
      "M": "Even when they made a golden calf and said, 'This is your god who brought you up from Egypt'—committing great acts of contempt—",
      "T": "The golden calf is the defining apostasy. While Moses was still on the mountain receiving the Torah, the people below were casting their own substitute. The claim made over the calf—'This is your god who brought you out of Egypt'—was a deliberate reassignment of God's saving act to an image made by human hands. The prayer calls it 'great blasphemies' (H5007 נְאָצוֹת—acts of contempt, provocations, deliberate desecration). Even so—"
    },
    "19": {
      "L": "you in your great mercies did not forsake them in the wilderness. The pillar of cloud to lead them in the way did not depart from them by day, nor the pillar of fire by night to light for them the way by which they should go.",
      "M": "you in your great compassion did not abandon them in the wilderness. The pillar of cloud continued to lead them by day, and the pillar of fire by night to light the way ahead.",
      "T": "—even then, you did not abandon them. 'In your great mercies'—the plural רַחֲמִים, rooted in the Hebrew word for a mother's womb, denotes a deep and visceral tenderness. Even after the golden calf, the cloud column did not lift. The fire column did not go out. God remained present, remained guiding. Mercy outlasted apostasy."
    },
    "20": {
      "L": "And you gave your good Spirit to instruct them and did not withhold your manna from their mouth and gave them water for their thirst.",
      "M": "You gave your good Spirit to instruct them. You did not withhold manna from their mouths, and you gave them water when they were thirsty.",
      "T": "Three gifts sustained the wilderness generation: the Spirit of God—called 'your good Spirit' here, the only explicit description of the divine Spirit as 'good' in the OT—who instructed them from within; manna that appeared every morning at their tent doors; and water from the rock for the thirsty. The Spirit who taught, the bread that came down, the water given for the thirsty—the prayer is not rehearsing history for its own sake; it is naming the character of a God who is still capable of all this."
    },
    "21": {
      "L": "Forty years you sustained them in the wilderness, and they lacked nothing. Their clothes did not wear out and their feet did not swell.",
      "M": "For forty years you provided for them in the wilderness, and they lacked nothing. Their clothes did not wear out, and their feet did not swell.",
      "T": "Forty years. Not one year, not ten—forty years of daily miracle. Their clothes lasted; their feet stayed sound. In a desert where ordinary sandals wore through in months, their garments held. The detail is deliberately mundane: God's faithfulness extended not only to the dramatic—manna, water—but to the ordinary: clothing that endured, feet that did not blister. Nothing was beneath his sustaining care."
    },
    "22": {
      "L": "And you gave them kingdoms and peoples and allotted them to every corner. So they took possession of the land of Sihon king of Heshbon and the land of Og king of Bashan.",
      "M": "You gave them kingdoms and peoples, distributing the land to them in every direction. They took possession of the land of Sihon king of Heshbon and the land of Og king of Bashan.",
      "T": "The conquest period begins: God started delivering kingdoms. Sihon king of Heshbon and Og king of Bashan were the first major defeats east of the Jordan—the opening victories that proved the conquest was possible and that God's promise would be kept. He gave them kingdoms and peoples 'allotted to every corner'—the language of a sovereign distributing territory. The land was his gift before it was their accomplishment."
    },
    "23": {
      "L": "And you multiplied their children as the stars of heaven and brought them into the land that you had told their fathers to go in and possess.",
      "M": "You increased their numbers like the stars in the sky and brought them into the land you had promised their fathers they would enter and take possession of.",
      "T": "The promise to Abraham—descendants as the stars of heaven—was now visibly fulfilled. That generation who entered the land was the living proof that God had kept what he swore to the patriarch centuries before. The prayer is threading the Abrahamic covenant of Genesis through the entire history of Israel, showing that what is happening in Nehemiah's day is the continuation of a story that began with one childless man called out of Mesopotamia."
    },
    "24": {
      "L": "So the descendants went in and possessed the land, and you subdued before them the inhabitants of the land, the Canaanites, and gave them into their hands, with their kings and the peoples of the land, to do with them as they wished.",
      "M": "Their descendants went in and took possession of the land. You subdued the Canaanites before them, delivering their kings and peoples into Israel's hands to deal with as they saw fit.",
      "T": "The conquest was God's doing. The prayer does not credit Israelite military prowess; it credits God for subduing the inhabitants. He delivered kings and whole peoples into Israel's hands—and gave them authority to dispose of them as they chose. The land was not won; it was given. Conquest was grace, not achievement."
    },
    "25": {
      "L": "And they captured fortified cities and a rich land and took possession of houses full of all good things, cisterns already hewn, vineyards, olive orchards, and fruit trees in abundance. So they ate and were filled and grew fat and delighted in your great goodness.",
      "M": "They captured fortified cities and a fertile land—houses stocked with every good thing, hewn cisterns, vineyards, olive groves, and abundant fruit trees. They ate and were satisfied; they grew prosperous and delighted in your great goodness.",
      "T": "The land flowed with everything: fortified cities already built, cisterns already dug, vineyards already planted, orchards already bearing fruit. Israel inherited a civilization in progress—they moved into what others had built and feasted on a goodness that was not the product of their own labor. They 'grew fat' (שָׁמַן)—the Hebrew is honest about prosperity's tendency to breed self-satisfaction. They delighted in God's great goodness. The next verse shows how quickly that delight turned to forgetfulness."
    },
    "26": {
      "L": "Nevertheless they were disobedient and rebelled against you and cast your law behind their back and killed your prophets who had testified against them to turn them back to you, and they committed great blasphemies.",
      "M": "But they were disobedient and rebelled against you. They threw your law behind their backs, killed your prophets who warned them to return to you, and committed great acts of contempt.",
      "T": "The Judges-era pattern: the same people who had inherited such overwhelming grace turned their backs on it—literally. 'Cast your law behind their back' is the prayer's image for what happened to the Torah: taken and thrown over the shoulder, dismissed, made irrelevant to daily life. When the prophets came to warn them, they killed them. Not metaphorically—murdered them. The word (הָרַג) is the word for killing. From Elijah through Jeremiah, the prophets of the pre-exilic era were silenced by the people who did not want to hear what God was saying."
    },
    "27": {
      "L": "Therefore you gave them into the hand of their enemies who oppressed them. And in the time of their distress they cried out to you and you heard from heaven, and according to your great mercies you gave them saviors who saved them from the hand of their enemies.",
      "M": "So you handed them over to their enemies, who oppressed them. But when they suffered and cried out to you, from heaven you heard them. In your great compassion you raised up deliverers who rescued them from their enemies.",
      "T": "The Judges cycle compressed into a single verse. God honored the covenant with consequences: he handed them to their enemies. But when the suffering became unbearable and they cried out—God heard. 'From heaven'—the cry went up; the hearing came down. And God sent deliverers: Othniel, Deborah, Gideon, and the others—all described here simply as 'saviors,' God's instruments, sent in mercy, to rescue the people from what they had brought on themselves."
    },
    "28": {
      "L": "But after they had rest, they did evil again before you, and you abandoned them to the hand of their enemies, so that the enemies had dominion over them. Yet when they turned and cried to you, you heard from heaven, and many times you delivered them according to your mercies.",
      "M": "But once they had rest, they again did what was evil before you, and you again handed them over to their enemies, who ruled over them. Yet whenever they turned and cried out to you, from heaven you heard them, and many times over you delivered them in your compassion.",
      "T": "The cycle repeated. Rest led to forgetfulness; forgetfulness led to evil; evil led to enemies; suffering led to crying out; crying out led to deliverance; deliverance led to rest—and rest again led to forgetfulness. The prayer says 'many times': this was not an exception, it was the pattern. And God heard 'many times': his mercy was not depleted by the first repetition or the fifth or the tenth. The prayer is building toward a confession that this cycle did not eventually end; it culminated in the exile that produced the present generation of slaves."
    },
    "29": {
      "L": "And you testified against them to turn them back to your law. Yet they acted presumptuously and did not obey your commandments, but sinned against your rules, by which if a person does them, he shall live by them, and they turned a stubborn shoulder and stiffened their neck and would not obey.",
      "M": "You warned them to turn back to your law, but they acted arrogantly and refused to obey your commandments. They sinned against your ordinances—by which if a person keeps them, he will live—and they turned a stubborn shoulder, stiffened their neck, and would not listen.",
      "T": "The Torah contains within itself the terms of life: 'the one who does these things shall live by them'—the prayer quietly quotes Leviticus 18:5 without naming it. The ordinances were not arbitrary constraints; they were the path of life. To reject them was to choose death. And yet Israel 'turned a stubborn shoulder'—the image of an ox that will not be guided by the yoke—and stiffened their neck and shut their ears. The body language of rebellion described in precise physical terms: shoulder turned away, neck rigid, ears closed."
    },
    "30": {
      "L": "Many years you bore with them and testified against them by your Spirit through your prophets. Yet they would not give ear. Therefore you gave them into the hand of the peoples of the lands.",
      "M": "For many years you were patient with them and warned them through your Spirit by means of your prophets. But they refused to listen, so you gave them over to the peoples of the surrounding lands.",
      "T": "God's patience is counted in years—'many years.' He did not respond to the first rebellion with the exile, nor the second, nor the tenth. He sent the prophets—and the prayer names what was happening: 'by your Spirit through your prophets.' The prophetic word was Spirit-driven, not human opinion. The divine Spirit was speaking through human voices for generations. They would not hear. And so at last God gave them to the surrounding nations. This is the exile—the final consequence of the long, patient, repeated pattern of grace refused."
    },
    "31": {
      "L": "Nevertheless, in your great mercies you did not make an end of them or forsake them, for you are a gracious and merciful God.",
      "M": "But in your great compassion you did not put an end to them or abandon them, for you are a gracious and merciful God.",
      "T": "'Nevertheless'—the word the prayer has been building toward. Even the exile was not the end. God did not make a complete end (כָּלָה—total destruction, annihilation) of them. He did not forsake them even in Babylon. Because: you are a gracious (חַנּוּן) and merciful (רַחוּם) God. The entire history of Israel, with all its failures, has been held together not by Israel's faithfulness but by God's character. He did not finish the people he had chosen. He never does."
    },
    "32": {
      "L": "Now therefore, our God, the great, the mighty, and the awesome God, who keeps covenant and steadfast love, do not let all the hardship seem little to you that has come upon us, upon our kings, our princes, our priests, our prophets, our fathers, and all your people, from the days of the kings of Assyria until this day.",
      "M": "Now therefore, our God—great, mighty, and awesome, who keeps covenant and steadfast love—do not let it seem trivial to you, all the hardship that has fallen upon us: our kings, our princes, our priests, our prophets, our ancestors, and all your people, from the time of the Assyrian kings to this very day.",
      "T": "The prayer arrives at the present. 'Now therefore' is the pivot from history to petition. It addresses God in his fullness: great, mighty, and awesome—the three adjectives of Deuteronomy 10:17 that frame who God is—and adds 'keeper of covenant and steadfast love' (חֶסֶד). Everything the prayer has rehearsed is implied in those words. The petition itself is modest and precise: 'Do not let it seem trivial to you.' We are not asking you to overlook our sins. We are asking you to register the full weight of our suffering. The suffering spans from the Assyrian conquest—nearly three centuries earlier—to this present day of Persian servitude."
    },
    "33": {
      "L": "Yet you are righteous in all that has come upon us, for you have dealt faithfully and we have done wickedly.",
      "M": "You have been righteous in everything that has happened to us, for you have acted faithfully while we have acted wickedly.",
      "T": "'You are righteous'—this is the prayer's explicit confession of God's justice in the exile. Everything that came was deserved. The prayer does not argue with God; it agrees with him. You were faithful; we were not. The exile was not divine cruelty; it was divine consistency. The same God who upheld covenant blessings for the obedient upheld covenant curses for the disobedient. The prayer vindicates God before making any petition of him."
    },
    "34": {
      "L": "Our kings, our princes, our priests, and our fathers have not kept your law or paid attention to your commandments and your warnings that you gave them.",
      "M": "Our kings, princes, priests, and ancestors did not obey your law or pay attention to the commands and warnings you gave them.",
      "T": "The full social hierarchy is implicated—kings, princes, priests, fathers. There is no exemption for the religious leadership: the priests share fully in the indictment. None of them kept the Torah; none of them heeded the commandments; none of them listened to the warnings. The prayer refuses to blame only the laity or only the monarchy. The failure was systemic and complete."
    },
    "35": {
      "L": "Even in their own kingdom, with your great goodness that you gave them, and in the large and rich land that you set before them, they did not serve you or turn from their evil deeds.",
      "M": "Even while they had their own kingdom, even with the great goodness you had given them and the spacious, fertile land you placed before them, they did not serve you or turn from their wicked ways.",
      "T": "The indictment sharpens: even during the era of the monarchy—when Israel had a land, a king, a temple, every political and spiritual gift—even then they did not serve God. The contrast is stark: God gave a large, rich land; they gave back evil deeds. Service was the expected response to gift; they withheld it. The prayer is saying: we had no excuse. The land was good. Your goodness was overwhelming. We had everything, and we still would not serve you."
    },
    "36": {
      "L": "Behold, we are slaves this day. In the land that you gave to our fathers to enjoy its fruit and its good gifts—behold, we are slaves.",
      "M": "Look—we are slaves today. In the very land you gave our ancestors to enjoy its fruit and its abundance—we are slaves here.",
      "T": "'Behold'—the prayer makes the assembly look at what they are. Slaves. On their own soil. The land God gave to Abraham, the land God cleared of the Canaanites, the land of milk and honey and great goodness—this land now belongs to a Persian king. The people who eat from it are tenants and subjects, not owners and sons. The repetition—'behold... behold'—lands twice: look at this. Look at what we are. The prayer does not soften it."
    },
    "37": {
      "L": "And its rich yield goes to the kings whom you have set over us because of our sins. They rule over our bodies and over our livestock at their pleasure, and we are in great distress.",
      "M": "The land's rich produce goes to the kings you have placed over us because of our sins. They rule over our bodies and our livestock as they please, and we are in great distress.",
      "T": "The Persian kings take the harvest. They take the labor of the body. They take the cattle. Not because they are unjust by Persian standards—but because God placed them there, 'because of our sins.' The political oppression is not blind misfortune; it is the Deuteronomic consequence. And the word for distress (צָרָה) is the same word used for the straits Israel was in when they cried out to God through the judges. The prayer ends where it began: in great distress, calling on the God of heaven."
    },
    "38": {
      "L": "Because of all this we are making a firm covenant in writing; on the sealed document are the names of our princes, our Levites, and our priests.",
      "M": "Because of all this, we are drawing up a binding agreement in writing. On the sealed document are the names of our leaders, our Levites, and our priests.",
      "T": "The prayer ends in covenant. All that history—creation, Abraham, Exodus, wilderness, conquest, Judges cycles, prophets, exile, present slavery—has led to this moment: a formal, written, sealed covenant. The Hebrew is כּוֹרְתִים אֲמָנָה—'we are cutting a firm covenant,' the language of the ancient covenant-making ritual now translated into a document with names and seals. This is not sentiment; it is legal and solemn. What the prayer has confessed, the covenant will now commit. Chapter 10 lists the signatories."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'nehemiah')
        merge_tier(existing, NEHEMIAH, tier_key)
        save(tier_dir, 'nehemiah', existing)
    print('Nehemiah 9 written.')

if __name__ == '__main__':
    main()
