"""
MKT Ezekiel chapters 13–15 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-13-15.py

Translation decisions (carrying forward all conventions from mkt-ezekiel-10-12.py):

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T, especially for the recognition
  formula, oracle introductions, and divine-oath formula ("as I live").
  Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Adonai-Yahweh): "Lord GOD" in L/M (small-caps GOD);
  "Lord Yahweh" in T. The combined form dominates Ezekiel's oracle style.

- H7307 (רוּחַ): Context-sensitive, as Ezekiel uses all three senses in these chapters:
  - 13:3 "follow their own spirit" (H7307) = the human spirit / inner impulse → "spirit"
    (lowercase) in L/M/T — these are the prophets' own hearts speaking, not God.
  - 13:11, 13:13 "stormy wind" (H7307 + H5591) = atmospheric wind → "wind" in all tiers.

- H5315 (נֶפֶשׁ / soul/life): Ch. 13:17-23 is the prophetess passage where the operative
  word is "hunting souls" (H6679 + H5315). The Hebrew נֶפֶשׁ here means persons/lives
  rather than Greek-style immaterial souls. L preserves "souls" (Strong's-accurate);
  M uses "lives/people" where the English flows better; T surfaces the hunting image
  with "people" or "lives" depending on rhythm.

- H7965 (שָׁלוֹם / peace): 13:10, 13:16 — the false peace oracle. "Peace" in all three
  tiers; the phrase "Peace, and there is no peace" is iconic and preserved verbatim in L.

- H3577/H7723 (כָּזָב / lies; שָׁוְא / vanity/falsehood): Both appear in the false prophet
  condemnation. "Lies" for H3577; "false/empty/falsehood" for H7723 in L. M and T
  use natural English equivalents in context. The semantic pair (empty vision + lying
  divination) is kept parallel across tiers.

- H2434/H8602 (חַיִץ / flimsy wall; תָּפֵל / whitewash/untempered mortar): The wall/plaster
  metaphor (13:10-16). L preserves the literal material language (wall, plaster, whitewash,
  untempered mortar). M clarifies "whitewash" consistently. T develops the image: false
  comfort = plastering a crumbling wall and calling it secure.

- H3704/H4555 (כְּסָתוֹת / magic bands/pillows; מִסְפָּחוֹת / veils/kerchiefs): The prophetess
  sign-act materials (13:18-21). These are occult instruments — arm-bands and head-veils
  used in some form of soul-binding sorcery. L uses "pillows/kerchiefs" (traditional KJV
  rendering); M uses "magic bands/veils" (modern scholarly consensus that these are
  divinatory/magical garments). T names them as occult instruments directly.

- H1544 (גִּלּוּלִים / idols): "Idols" in all tiers throughout ch. 14. The word is
  Ezekiel's characteristic term for images — possibly a contemptuous formation related
  to dung/logs. L/M preserve "idols"; T may use "idols in your heart" or "heart-idols"
  where the inner location is theologically emphasized.

- H4383 (מִכְשׁוֹל / stumbling block): 14:3, 4, 7 — "the stumblingblock of their iniquity."
  "Stumbling block" in L/M; "idol of their iniquity set as a trap before their own eyes"
  in T, where the self-placed danger is surfaced.

- H6666 (צְדָקָה / righteousness): 14:14, 20 — Noah, Daniel, Job deliver "by their
  righteousness." This is personal, enacted righteousness (cf. Ezekiel's own usage in
  ch. 3 and 18), not imputed status. L/M: "righteousness"; T: "their own righteousness"
  to clarify it is personal conduct, not forensic standing.

- Daniel (H1840 דָּנִיֵּאל) in 14:14, 20: This is almost certainly the same Daniel as
  the book of Daniel — a contemporary of Ezekiel already known for wisdom and
  righteousness in Babylonian exile. Some scholars propose a different "Dan'el" from
  Ugaritic tradition (Aqhat), but the Babylonian-exile context and Ezekiel's co-location
  with Daniel's generation makes the biblical Daniel the most natural referent.
  L/M: "Daniel" (transliterated). T: "Daniel" with contextual note of his recognized
  righteousness, relevant because both Ezekiel and Daniel are in Babylon simultaneously.

- The vine image (ch. 15): Jerusalem as a fruitless vine whose wood is useless even
  before burning. The metaphor inverts the common OT vine-as-Israel image (Ps 80,
  Isa 5, Jer 2). Here the vine is not assessed for its fruit but for its timber —
  which is worthless. T develops the contrast: a vine's only purpose is fruit; when
  it does not bear fruit, it has nothing — not even good wood. This sets up the
  extended allegory of ch. 16.

- H4603/H4604 (מָעַל / trespass/faithlessness): 14:13, 15:8. This is covenant
  unfaithfulness — the technical term for breach of a sacred trust. L preserves
  "trespass"; M/T use "faithlessness" where it captures the relational betrayal.

- Aspect notes:
  - The oracle-formula "Thus says the Lord GOD" (אָמַר אֲדֹנָי יְהוִה) is consistently
    past or present-declarative in Hebrew; translated as "says/declares" in M and T.
  - The judgment announcements in chs. 13–14 use the Hebrew perfect with waw-consecutive
    (prophetic perfect) — future events described as certain as if already accomplished.
    English future tense is used throughout.
  - The divine oath "as I live" (חַי-אָנִי, 14:16, 18, 20) is Yahweh's self-pledge;
    T renders it as an oath formula: "by my life" or "as I live."
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

EZEKIEL = {
  "13": {
    "1": {
      "L": "And the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, prophesy against the prophets of Israel that prophesy, and say thou unto them that prophesy out of their own hearts: Hear ye the word of the LORD.",
      "M": "Son of man, prophesy against the prophets of Israel who are prophesying, and say to those who prophesy out of their own hearts: Hear the word of the LORD!",
      "T": "Son of man, prophesy against the prophets of Israel who prophesy. Say to those who speak from their own hearts — who generate visions and words from within themselves rather than from me: Hear the word of Yahweh!"
    },
    "3": {
      "L": "Thus saith the Lord GOD: Woe unto the foolish prophets, that follow their own spirit and have seen nothing.",
      "M": "Thus says the Lord GOD: Woe to the foolish prophets who follow their own spirit and have seen nothing!",
      "T": "The Lord Yahweh says: Woe to the fools who call themselves prophets. They follow their own inner spirit — their own impulse — and name it vision. They have seen nothing. And yet they speak."
    },
    "4": {
      "L": "O Israel, thy prophets are like the foxes in the deserts.",
      "M": "Your prophets are like foxes among ruins, O Israel.",
      "T": "O Israel, your prophets are foxes skulking through ruins — scavengers making their dens in what has already been destroyed, contributing nothing to what needs to be rebuilt."
    },
    "5": {
      "L": "Ye have not gone up into the gaps, neither made up the hedge for the house of Israel to stand in the battle in the day of the LORD.",
      "M": "You have not gone up into the breaches or built up the wall for the house of Israel to stand in battle on the day of the LORD.",
      "T": "A true prophet stands in the breach — steps into the gap in the wall and holds it. These have done none of that. They have not stepped into the broken places. They have not built the hedge that would protect Israel when the day of Yahweh arrives. They abandoned their post."
    },
    "6": {
      "L": "They have seen vanity and lying divination, saying: The LORD saith; and the LORD hath not sent them; and they have made others to hope that they would confirm the word.",
      "M": "They see false visions and utter lying divinations, saying 'The LORD declares' — but the LORD has not sent them; yet they expect their word to be confirmed.",
      "T": "False visions — that is what they see. Lying divination — that is what they speak. And they stamp it with Yahweh's name: 'The LORD says this.' But Yahweh never sent them. They then wait for events to validate them, hoping the word they invented will somehow come true."
    },
    "7": {
      "L": "Have ye not seen a vain vision and have ye not spoken a lying divination, whereas ye say: The LORD saith it; albeit I have not spoken?",
      "M": "Have you not seen a false vision and spoken a lying divination when you say 'The LORD declares,' even though I have not spoken?",
      "T": "Is this not the truth of it: your vision was empty, your divination a lie? And then you went ahead and stamped my name on it — 'The LORD says' — when I had said nothing of the kind."
    },
    "8": {
      "L": "Therefore thus saith the Lord GOD: Because ye have spoken vanity, and seen lies, therefore, behold, I am against you, saith the Lord GOD.",
      "M": "Therefore thus says the Lord GOD: Because you have spoken falsehood and seen lies, I am against you, declares the Lord GOD.",
      "T": "Therefore the Lord Yahweh says: Because you spoke what was false and called it vision — because you saw lies and proclaimed them — I am set against you. The Lord Yahweh declares it."
    },
    "9": {
      "L": "And mine hand shall be upon the prophets that see vanity and that divine lies; they shall not be in the assembly of my people, neither shall they be written in the writing of the house of Israel, neither shall they enter into the land of Israel; and ye shall know that I am the Lord GOD.",
      "M": "My hand will be against the prophets who see false visions and divine lies; they will not be in the council of my people, nor will their names be written in the register of the house of Israel, nor will they enter the land of Israel — and you will know that I am the Lord GOD.",
      "T": "My hand moves against them: the prophets who see falsehood and speak it as divination. Three punishments, stripping away everything: excluded from the community assembly; names struck from Israel's register; barred from the land of Israel. Cut off from people, from record, and from land. Then you will know that I am the Lord Yahweh."
    },
    "10": {
      "L": "Because, even because they have seduced my people, saying: Peace; and there was no peace; and one built up a wall, and lo, others daubed it with untempered morter.",
      "M": "Because they have led my people astray, saying 'Peace' when there is no peace — and when someone builds a flimsy wall, others come and plaster it with whitewash.",
      "T": "Here is the indictment: they told my people 'Peace' — and there was no peace. A thin, unstable wall goes up; these prophets hurry to plaster it over and call it secure. False peace and false construction — the same deception in two images."
    },
    "11": {
      "L": "Say unto them which daub it with untempered morter that it shall fall; there shall be an overflowing shower, and ye, O great hailstones, shall fall; and a stormy wind shall rend it.",
      "M": "Say to those who plaster with whitewash that it will fall — a flooding rain will come, great hailstones will fall, and a stormy wind will break it apart.",
      "T": "Say to the plasterers: your wall is coming down. A torrential rain will pound it. Hailstones will batter it. A gale-force wind will tear through it. You built nothing that can stand before the storm."
    },
    "12": {
      "L": "Lo, when the wall is fallen, shall it not be said unto you: Where is the daubing wherewith ye have daubed it?",
      "M": "When the wall falls, will it not be said to you: 'Where is the plaster you covered it with?'",
      "T": "When the wall collapses — and it will collapse — someone will ask: where is all that fine plastering now? The false prophet's comfort evaporates at the first real storm."
    },
    "13": {
      "L": "Therefore thus saith the Lord GOD: I will even rend it with a stormy wind in my fury; and there shall be an overflowing shower in mine anger, and great hailstones in my fury to consume it.",
      "M": "Therefore thus says the Lord GOD: I will tear it down with a stormy wind in my wrath; there will be a flooding rain in my anger, and great hailstones in my fury to destroy it.",
      "T": "The Lord Yahweh says: I will tear it down myself — with a raging wind driven by my fury, with a torrential rain from my anger, with hailstones from my wrath. I am the very storm these false prophets never warned about."
    },
    "14": {
      "L": "So will I break down the wall that ye have daubed with untempered morter, and bring it down to the ground, so that the foundation thereof shall be discovered; and it shall fall, and ye shall be consumed in the midst thereof; and ye shall know that I am the LORD.",
      "M": "I will tear down the wall you plastered with whitewash and bring it to the ground, so that its foundation is exposed; it will fall and you will be destroyed in the rubble. Then you will know that I am the LORD.",
      "T": "I will pull down the wall you whitewashed — down to the foundation, fully exposed for what it always was. The wall falls. You will be buried in it. And in the rubble you will know that I am Yahweh."
    },
    "15": {
      "L": "Thus will I accomplish my wrath upon the wall and upon them that have daubed it with untempered morter; and will say unto you: The wall is no more, neither they that daubed it.",
      "M": "So I will spend my wrath on the wall and on those who plastered it, and I will declare: The wall is gone, and those who plastered it are gone.",
      "T": "My wrath will be spent on both — the wall and the plasterers together. And the verdict will be simple: wall gone, plasterers gone. False comfort and its makers, swept away in the same collapse."
    },
    "16": {
      "L": "To wit, the prophets of Israel which prophesy concerning Jerusalem, and which see visions of peace for her, and there is no peace, saith the Lord GOD.",
      "M": "These are the prophets of Israel who prophesy concerning Jerusalem and see visions of peace for her when there is no peace, declares the Lord GOD.",
      "T": "These are the prophets who specialized in Jerusalem — who offered the city vision after vision of peace, peace, peace, while the city stood on the edge of ruin. There was no peace. The Lord Yahweh has spoken."
    },
    "17": {
      "L": "Likewise, thou son of man, set thy face against the daughters of thy people, which prophesy out of their own heart; and prophesy thou against them.",
      "M": "And you, son of man, set your face against the daughters of your people who prophesy out of their own hearts; prophesy against them.",
      "T": "Son of man, now turn to the women who are doing the same thing — prophetesses who speak from their own imagination, not from me. Set your face against them. Prophesy against them."
    },
    "18": {
      "L": "And say: Thus saith the Lord GOD: Woe to the women that sew pillows to all armholes, and make kerchiefs upon the head of every stature to hunt souls. Will ye hunt the souls of my people, and will ye save the souls alive that come unto you?",
      "M": "Say: Thus says the Lord GOD: Woe to the women who sew magic bands on all wrists and make veils for the heads of persons of every height to trap lives! Will you trap my people's lives and keep alive the lives you choose?",
      "T": "Say from the Lord Yahweh: Woe to the women who are sewing these occult arm-bands and fashioning ritual veils to place on the heads of every person they ensnare. They are hunting lives — capturing people through sorcery, deciding by their dark craft who lives and who dies. Do you think you can take my people's lives into your own hands like this?"
    },
    "19": {
      "L": "And will ye pollute me among my people for handfuls of barley and for pieces of bread, to slay the souls that should not die and to save the souls alive that should not live, by your lying to my people that hear lies?",
      "M": "You have profaned me among my people for handfuls of barley and pieces of bread — killing people who should not die and keeping alive people who should not live — by lying to my people who love to hear lies.",
      "T": "You have dragged my name through dishonor among my people — and what did you charge for it? Handfuls of barley. A few pieces of bread. For that price you took lives that should not have been taken and preserved lives that needed judgment. You lied to my people and they were glad to hear it. Cheap sorcery for people who preferred cheap comfort to truth."
    },
    "20": {
      "L": "Wherefore thus saith the Lord GOD: Behold, I am against your pillows, wherewith ye there hunt the souls to make them fly; and I will tear them from your arms, and will let the souls go, even the souls that ye hunt to make them fly.",
      "M": "Therefore thus says the Lord GOD: I am against your magic bands with which you hunt lives like birds — I will tear them from your arms and release the lives you snare like birds.",
      "T": "The Lord Yahweh says: I am against your magic bands. You have been using them to snare people like birds caught in a net. I will tear the bands off your arms — and I will release the people you have been trapping, every one of them."
    },
    "21": {
      "L": "Your kerchiefs also will I tear, and deliver my people out of your hand, and they shall be no more in your hand to be hunted; and ye shall know that I am the LORD.",
      "M": "I will also tear off your veils and deliver my people from your grip; they will no longer be prey in your hands. And you will know that I am the LORD.",
      "T": "Your ritual veils will be torn away as well. My people will be pulled free from your grip. They will no longer be your prey. And then you will know that I am Yahweh."
    },
    "22": {
      "L": "Because with lies ye have made the heart of the righteous sad, whom I have not made sad; and strengthened the hands of the wicked that he should not return from his wicked way, by promising him life.",
      "M": "Because with lies you have discouraged the righteous person, whom I had not grieved, and you have strengthened the hands of the wicked so that he does not turn from his evil way — you promised him life.",
      "T": "Here is the specific charge, and it is a double inversion: you discouraged the righteous — people whose hearts were right with me — by falsely condemning them, though I had not placed grief on them. And you strengthened the wicked by promising them life, safety, no consequences — so they had no reason to turn from their evil. You condemned the innocent and comforted the guilty. You reversed everything."
    },
    "23": {
      "L": "Therefore ye shall see no more vanity, nor divine divinations; for I will deliver my people out of your hand; and ye shall know that I am the LORD.",
      "M": "Therefore you shall no longer see false visions or practice divination; I will deliver my people from your hand, and you will know that I am the LORD.",
      "T": "So: no more false visions for you. No more divination. I will pull my people completely free from your hands. And you will know, then, that I am Yahweh."
    }
  },
  "14": {
    "1": {
      "L": "Then came certain of the elders of Israel unto me, and sat before me.",
      "M": "Then some of the elders of Israel came to me and sat down before me.",
      "T": "Some of the elders of Israel came and sat before me, seeking a word from God. They did not look at themselves clearly."
    },
    "2": {
      "L": "And the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "3": {
      "L": "Son of man, these men have set up their idols in their heart, and put the stumblingblock of their iniquity before their face: should I be enquired of at all by them?",
      "M": "Son of man, these men have set up their idols in their hearts and placed the stumbling block of their iniquity right before their faces. Should I actually be inquired of by them?",
      "T": "Son of man, look at these men carefully. Their idols are not in a shrine — they are in their hearts. They have erected the stumbling block of their own iniquity and placed it directly before their eyes. Given this, should I allow them to treat me as a divine consultant while their hearts remain given over to idols?"
    },
    "4": {
      "L": "Therefore speak unto them and say unto them: Thus saith the Lord GOD: Every man of the house of Israel that setteth up his idols in his heart, and putteth the stumblingblock of his iniquity before his face, and cometh to the prophet — I the LORD will answer him that cometh according to the multitude of his idols.",
      "M": "Therefore speak to them and say: Thus says the Lord GOD: Any man of the house of Israel who sets up his idols in his heart and places the stumbling block of his iniquity before his face, and then comes to a prophet — I the LORD will answer him according to the multitude of his idols.",
      "T": "So speak to them. The Lord Yahweh says: Any Israelite who has enthroned idols in his heart — who has made his iniquity a stumbling block he keeps before his eyes — and then comes to a prophet seeking a word from me: I, Yahweh, will answer him. But I will answer him through his idols. The response he receives will correspond to what he is carrying inside."
    },
    "5": {
      "L": "That I may take the house of Israel in their own heart, because they are all estranged from me through their idols.",
      "M": "This is to lay hold of the house of Israel in their own hearts — for they have all become estranged from me through their idols.",
      "T": "The purpose: to confront Israel in the very location where the problem lives — their hearts. Every one of them has drifted away from me through idol-devotion. I will address the disease at its root, not just treat the symptom."
    },
    "6": {
      "L": "Therefore say unto the house of Israel: Thus saith the Lord GOD: Repent and turn yourselves from your idols; and turn away your faces from all your abominations.",
      "M": "Therefore say to the house of Israel: Thus says the Lord GOD: Repent and turn away from your idols; turn your faces away from all your abominations.",
      "T": "So say to the house of Israel from the Lord Yahweh: Turn around. Turn away from your idols. Stop facing in the direction of your abominations — physically, decisively, completely — and face me instead."
    },
    "7": {
      "L": "For every one of the house of Israel, or of the stranger that sojourneth in Israel, which separateth himself from me, and setteth up his idols in his heart, and putteth the stumblingblock of his iniquity before his face, and cometh to a prophet to enquire of him concerning me — I the LORD will answer him by myself.",
      "M": "For any man of the house of Israel, or any foreigner who lives in Israel, who separates himself from me, sets up his idols in his heart, places the stumbling block of his iniquity before his face, and then comes to a prophet to inquire of me — I the LORD will answer him personally.",
      "T": "The policy applies to everyone under Israel's covenant umbrella — native Israelite or resident foreigner who has bound himself to Israel's community. Anyone who separates from me on the inside while seeking me through a prophet on the outside: I will answer them directly. Not through the prophet. Personally — and the answer will match what they have chosen to carry in their hearts."
    },
    "8": {
      "L": "And I will set my face against that man, and will make him a sign and a proverb, and I will cut him off from the midst of my people; and ye shall know that I am the LORD.",
      "M": "I will set my face against that man, make him a sign and a byword, and cut him off from the midst of my people; and you will know that I am the LORD.",
      "T": "I will set my face against that person — a concentrated divine attention that brings only judgment. I will make him a cautionary tale, a proverb on lips across Israel: this is what happens. I will cut him out of the community entirely. And then my people will know that I am Yahweh."
    },
    "9": {
      "L": "And if the prophet be deceived when he hath spoken a thing, I the LORD have deceived that prophet; and I will stretch out my hand upon him, and will destroy him from the midst of my people Israel.",
      "M": "And if a prophet is deceived and speaks a word, I the LORD have deceived that prophet; I will stretch out my hand against him and destroy him from the midst of my people Israel.",
      "T": "A warning for the prophet as well: if an idolatrous inquirer comes and the prophet delivers an answer — even if the prophet was drawn into error by the question — I, Yahweh, permitted that deception to occur. My hand will then move against the prophet too, and I will remove him from among my people. A corrupt question corrupts the prophetic channel; both parties bear the weight."
    },
    "10": {
      "L": "And they shall bear the punishment of their iniquity; the punishment of the prophet shall be even as the punishment of him that seeketh unto him.",
      "M": "They shall bear the consequences of their iniquity — the punishment of the prophet and the punishment of the one who inquired will be the same.",
      "T": "Both will carry the full weight of their guilt. The prophet who answered an idolater and the idolater who came seeking — equal punishment, equal accountability. There is no moral distance between them."
    },
    "11": {
      "L": "That the house of Israel may go no more astray from me, neither be polluted any more with all their transgressions; but that they may be my people and I may be their God, saith the Lord GOD.",
      "M": "This is so that the house of Israel may no longer wander away from me, nor defile themselves with all their transgressions, but that they may be my people and I may be their God, declares the Lord GOD.",
      "T": "The purpose behind the judgment is not destruction — it is restoration. The goal: that Israel would stop drifting away from me; that they would no longer contaminate themselves with rebellion; that the covenant would be what it was always meant to be — they my people, I their God. The Lord Yahweh has declared it."
    },
    "12": {
      "L": "The word of the LORD came again to me, saying:",
      "M": "The word of the LORD came to me again:",
      "T": "Yahweh's word came to me again:"
    },
    "13": {
      "L": "Son of man, when the land sinneth against me by trespassing grievously, then will I stretch out mine hand upon it, and will break the staff of the bread thereof, and will send famine upon it, and will cut off man and beast from it.",
      "M": "Son of man, when a land sins against me by acting in grievous faithlessness, I will stretch out my hand against it, break its supply of bread, send famine upon it, and cut off both man and beast from it.",
      "T": "Son of man — consider a land that sins against me with sustained faithlessness, deliberate and deep. Here is the response: my hand stretched out against it, the food supply snapped like a broken staff, famine moving in, both people and animals removed. This is the weight of sustained covenant violation."
    },
    "14": {
      "L": "Though these three men, Noah, Daniel, and Job, were in it, they should deliver but their own souls by their righteousness, saith the Lord GOD.",
      "M": "Even if these three men — Noah, Daniel, and Job — were in it, they would deliver only their own lives by their righteousness, declares the Lord GOD.",
      "T": "Not even the three greatest righteous men could change this outcome. Noah, who found grace in a generation given over entirely to judgment. Daniel, standing righteous in Babylonian exile at this very moment — known to Ezekiel's audience as a contemporary whose righteousness was already legend. Job, whom God himself declared righteous after the whirlwind. Three such men — and still they could save only themselves. The land's judgment would stand."
    },
    "15": {
      "L": "If I cause noisome beasts to pass through the land, and they spoil it, so that it be desolate, that no man may pass through because of the beasts.",
      "M": "If I send wild beasts through the land and they ravage it, making it desolate so that no one can travel through because of the animals.",
      "T": "Or instead of famine — wild beasts. Predators moving through the land, stripping it bare, making every road impassable. A land abandoned to the teeth of the wilderness."
    },
    "16": {
      "L": "Though these three men were in it, as I live, saith the Lord GOD, they shall deliver neither sons nor daughters; they only shall be delivered, but the land shall be desolate.",
      "M": "Though these three men were in it, as I live, declares the Lord GOD, they would deliver neither sons nor daughters — they alone would be saved, but the land would be desolate.",
      "T": "Even with those three righteous men present — by my own life, the Lord Yahweh swears it — they could not pull sons and daughters through. Their righteousness covers themselves alone. The land: desolate. The oath is absolute."
    },
    "17": {
      "L": "Or if I bring a sword upon that land and say: Sword, go through the land; so that I cut off man and beast from it.",
      "M": "Or if I bring a sword upon that land and command: 'Sword, pass through the land,' so that I cut off man and beast from it.",
      "T": "Or a sword — God commanding the weapon directly, as if addressing it by name: Sword, pass through. A military campaign of total devastation, man and beast removed."
    },
    "18": {
      "L": "Though these three men were in it, as I live, saith the Lord GOD, they shall deliver neither sons nor daughters, but they only shall be delivered themselves.",
      "M": "Though these three men were in it, as I live, declares the Lord GOD, they would deliver neither sons nor daughters — they alone would be saved.",
      "T": "Once more — the same verdict. Three righteous men present; sons and daughters still cannot be saved by proximity to their righteousness. What they possess stands for them; it does not transfer."
    },
    "19": {
      "L": "Or if I send a pestilence into that land, and pour out my fury upon it in blood, to cut off from it man and beast.",
      "M": "Or if I send plague into that land and pour out my fury upon it in bloodshed, cutting off from it man and beast.",
      "T": "Or plague — wrath made visible in epidemic and death, poured out in blood, consuming everything alive."
    },
    "20": {
      "L": "Though Noah, Daniel, and Job, were in it, as I live, saith the Lord GOD, they shall deliver neither son nor daughter; they shall but deliver their own souls by their righteousness.",
      "M": "Though Noah, Daniel, and Job were in it, as I live, declares the Lord GOD, they would deliver neither son nor daughter — they would deliver only their own lives by their own righteousness.",
      "T": "Noah, Daniel, Job — even the three together could not extend their own righteousness to cover their children. By my life — the Lord Yahweh swears it — only their own lives would be secured. Righteousness is not inherited, not transferred, not shared across the gap of another person's choices."
    },
    "21": {
      "L": "For thus saith the Lord GOD: How much more when I send my four sore judgments upon Jerusalem, the sword, and the famine, and the noisome beast, and the pestilence, to cut off from it man and beast?",
      "M": "For thus says the Lord GOD: How much more when I send my four devastating judgments upon Jerusalem — sword, famine, wild beast, and plague — to cut off from it man and beast!",
      "T": "The argument arrives at Jerusalem. How much more severe when I send not one but all four judgments on her simultaneously — sword, famine, wild beasts, and plague — cutting off every living thing? All four gathered against one city at once. No righteous remnant, however great, could turn that tide."
    },
    "22": {
      "L": "Yet, behold, therein shall be left a remnant that shall be brought forth, both sons and daughters; behold, they shall come forth unto you, and ye shall see their way and their doings; and ye shall be comforted concerning the evil that I have brought upon Jerusalem, even concerning all that I have brought upon it.",
      "M": "Yet behold — there will be a remnant left in it who will be brought out, sons and daughters; they will come to you, and you will see their conduct and their deeds, and you will be comforted regarding the disaster I have brought upon Jerusalem — all that I have brought upon it.",
      "T": "And yet — a remnant. Sons and daughters will come out, will arrive among you exiles in Babylon. When you see them, when you observe how they live and what they carry in themselves, you will find something unexpected: comfort. Not the comfort of ease or escape, but the comfort of understanding. These survivors will show you, by the way they are, why Jerusalem had to fall."
    },
    "23": {
      "L": "And they shall comfort you when ye see their ways and their doings; and ye shall know that I have not done without cause all that I have done in it, saith the Lord GOD.",
      "M": "They will comfort you when you see their ways and their deeds, and you will know that I have not acted without cause in all that I have done to it, declares the Lord GOD.",
      "T": "They will comfort you by being living evidence — walking testimony that the judgment was just. When you see how they lived, how they chose, what they became, you will know: everything I brought on Jerusalem, I brought with cause. Not arbitrary devastation. Covenant consequence, exact and justified. The Lord Yahweh has said it."
    }
  },
  "15": {
    "1": {
      "L": "And the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, what is the vine tree more than any tree, or than a branch which is among the trees of the forest?",
      "M": "Son of man, how is the wood of the vine better than any other tree — the vine branch among the trees of the forest?",
      "T": "Son of man, consider the vine. What is special about its wood? Among all the trees in a forest, how does a vine branch distinguish itself?"
    },
    "3": {
      "L": "Shall wood be taken thereof to do any work? Or will men take a pin of it to hang any vessel thereon?",
      "M": "Is its wood taken to make anything useful? Can someone even cut a peg from it to hang a vessel on?",
      "T": "You cannot build with vine wood. You cannot even cut a peg from it strong enough to hold a pot. The vine produces one thing: fruit. Strip away the fruit, and it has no use at all."
    },
    "4": {
      "L": "Behold, it is cast into the fire for fuel; the fire devoureth both the ends of it, and the midst of it is burned: is it meet for any work?",
      "M": "It is thrown into the fire for fuel; the fire consumes both ends, and the middle chars — is it then useful for anything?",
      "T": "Into the fire it goes — fuel and nothing more. The fire takes both ends; the middle chars black. At that point, brittle and spent, is there any use left in it at all?"
    },
    "5": {
      "L": "Behold, when it was whole, it was meet for no work: how much less shall it be meet yet for any work, when the fire hath devoured it, and it is burned?",
      "M": "When it was whole it was not useful for any work — how much less after the fire has consumed it and it is charred!",
      "T": "When the vine was whole and unburned, it still had no craft use. Now that fire has taken it, now that it is blackened and brittle — the uselessness is only more complete. There is nothing left to work with. This is Jerusalem."
    },
    "6": {
      "L": "Therefore thus saith the Lord GOD: As the vine tree among the trees of the forest, which I have given to the fire for fuel, so will I give the inhabitants of Jerusalem.",
      "M": "Therefore thus says the Lord GOD: As I have given the vine wood among the trees of the forest to the fire for fuel, so have I given up the inhabitants of Jerusalem.",
      "T": "The Lord Yahweh makes the application unmistakable: As the vine wood — the most useless timber in any forest — goes to the fire, so the inhabitants of Jerusalem are given to the fire. They were chosen not for the quality of their wood but to bear fruit for me. They bore none. The fire receives them."
    },
    "7": {
      "L": "And I will set my face against them; they shall go out from one fire, and another fire shall devour them; and ye shall know that I am the LORD, when I set my face against them.",
      "M": "I will set my face against them; though they escape from one fire, another fire will consume them — and you will know that I am the LORD when I set my face against them.",
      "T": "I set my face against them — and when Yahweh's face turns toward someone for judgment, there is no shelter to be found. They may escape one fire only to meet another. Fire follows them because I am following them. In this — in the impossibility of escape — you will know that I am Yahweh."
    },
    "8": {
      "L": "And I will make the land desolate, because they have committed a trespass, saith the Lord GOD.",
      "M": "I will make the land desolate, because they have acted faithlessly, declares the Lord GOD.",
      "T": "The land itself will be made desolate — not as collateral damage but as a direct covenant consequence. They broke faith with me, and the land that was to be the visible sign of covenant blessing becomes instead the visible sign of covenant judgment. The Lord Yahweh has spoken."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 13–15 written.')

if __name__ == '__main__':
    main()
