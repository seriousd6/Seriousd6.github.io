"""
MKT Jeremiah chapters 16–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-16-18.py

Translation decisions (consistent with mkt-jeremiah-1-3.py, mkt-jeremiah-10-12.py,
and mkt-jeremiah-13-15.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where personal-name force is
  significant (oracles, covenant declarations, divine soliloquy, lament address).
  Narrative formulas use "Yahweh" in T for directness.

- H430 (אֱלֹהִים): "God" in all tiers; "gods" for foreign deities (16:11, 16:13, 17:2).

- H2617 (חֶסֶד): 16:5 — "my steadfast love" in L; "my steadfast covenant love" in M/T.
  The term denotes covenant loyalty + active kindness; "lovingkindness" (KJV) is archaic;
  "steadfast love" (ESV/RSV) is retained as the standard rendering established in prior scripts.

- H7307 (רוּחַ): 18:17 = "east wind" — physical scorching wind as agent of divine judgment;
  not Spirit. Consistent with 13:24 (desert wind) and 14:6 (air/breath).

- H5162 (נָחַם): 18:8, 18:10 — Niphal: "I will relent" in L/M; "I will change the
  judgment / take back the good" in T. Not sin-repentance but a sovereign recalibration;
  the Niphal form indicates reflexive action on Yahweh's own plan, not moral guilt.

- H6121 (עָקֹב): 17:9 — "deceitful" in L/M (lit. "crooked, like a heel-grabber" — the
  same root as Jacob's name); "deceitful beyond all reckoning" in T to capture the
  superlative force of the adverb "above all things."

- H605 (אָנוּשׁ): 17:9 — "desperately sick" in L/M; "sick to the point of corruption"
  in T. Same root as H605 in 15:18 ("incurable wound"); both share the semantic field of
  terminal illness / hopeless condition.

- H7451 (רָעָה): Context-sensitive throughout. Divine judgment arriving: "disaster" (16:10,
  18:7, 18:8, 18:11). Human moral state: "evil/wickedness" (16:12, 17:9, 18:12).

- H3335 (יָצַר): 18:2–11 — as noun "potter" (L/M/T); as verb "forming/shaping" (L),
  "shaping" (M/T). The same Hebrew root underlies both the noun (potter) and verb (form/shape)
  — this word-play is the engine of the parable. Rendered "shaping disaster" in 18:11 to
  preserve the pottery metaphor in Yahweh's speech ("I am the potter at the wheel").

- H2563 (חֹמֶר): 18:4, 18:6 — "clay" in all tiers; the raw material that has no will of
  its own, entirely in the potter's hands.

- 17:4 (H8058 שְׁמַט + H5157 נָחַל): lit. "you shall release/drop your hand from your
  inheritance." Translated as "through your own actions you will forfeit the inheritance."
  The MT reads ambiguously as either 2nd-person (you will let go) or causative (I will cause
  you to let go). Following the natural MT reading as addressee action.

- 17:12: "A glorious throne set on high from the beginning" — a parenthetical confession
  that functions as the positive counterpart to the shame of v. 13. The temple/ark as
  Yahweh's earthly throne-room; "from the beginning" echoes the primordial founding at Sinai.
  Rendered as an exclamatory confession in T to mark the rhetorical transition.

Structural notes:
  Ch. 16 — The sign-act of Jeremiah's enforced celibacy (vv. 1–13): Jeremiah must not marry,
  not mourn, not feast — his life itself is a living sermon. Then an unexpected turn: restoration
  hope embedded within judgment (vv. 14–15, paralleling 23:7–8). Then the hunt imagery (vv. 16–18)
  and a remarkable eschatological vision: the nations confessing their idolatrous inheritance (vv.
  19–21). The chapter ends not on doom but on the nations coming to Yahweh.

  Ch. 17 — Three distinct units loosely connected by the theme of the heart/trust:
  (a) Judah's sin engraved on the heart (vv. 1–4); (b) the Psalm-1 contrast of cursed/blessed
  (vv. 5–8 — the closest Jeremiah comes to pure wisdom poetry); (c) the heart's deceitfulness and
  Yahweh's all-seeing judgment (vv. 9–11); (d) the temple-throne meditation and Jeremiah's
  lament-prayer (vv. 12–18); (e) the Sabbath exhortation and conditional promise/threat (vv.
  19–27). The Sabbath passage is often treated as secondary but it fits the pattern of covenant
  obedience as the hinge of blessing and curse.

  Ch. 18 — The potter's house (vv. 1–11): Yahweh's sovereignty is dynamic, not mechanical;
  the parable insists that both judgment and blessing remain responsive to human repentance or
  apostasy. Israel's hard refusal (vv. 12–17) follows immediately — the very people who should
  be re-shaped by the parable refuse re-shaping. Then the conspiracy against Jeremiah (v. 18)
  and his fierce imprecatory prayer (vv. 19–23) — among the rawest of his confessions.

OT echoes:
  16:5 — "I have taken away my peace (שָׁלוֹם) and my steadfast love (חֶסֶד)" — the two great
    covenant blessings. Their withdrawal is the structural inverse of the Aaronic blessing
    (Num 6:24–26: "the LORD give you peace" and "show his steadfast love").
  16:14–15 — The new Exodus formula closely parallels 23:7–8; both passages interrupt doom
    with eschatological hope, suggesting the final editor placed them as structural markers.
  17:5–8 — Almost verbatim parallel to Psalm 1. Both texts contrast the cursed/blessed by
    the tree/desert-shrub image. Probable common tradition or direct literary dependence.
  17:13 — "fountain of living waters" echoes 2:13 (Yahweh as the spring Israel abandoned);
    anticipates John 4:10 and 7:38.
  18:1–10 — Potter parable. Cited by Paul at Romans 9:21 ("does the potter not have authority
    over the clay?"); alluded to at Isaiah 64:8 ("we are the clay, you are the potter").
    The theological key is that divine sovereignty is responsive, not rigid.
  18:20 — "I stood before you to speak good for them" — Jeremiah as intercessor echoes Moses
    (Exod 32:11) and anticipates Ezekiel 22:30 ("I sought a man to stand in the gap").
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
            if v not in existing[ch]:
                existing[ch][v] = tiers[tier_key]

JEREMIAH = {
  "16": {
    "1": {
      "L": "The word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Then Yahweh's word came to me:"
    },
    "2": {
      "L": "You shall not take a wife, and you shall have no sons or daughters in this place.",
      "M": "You must not marry or have sons or daughters in this place.",
      "T": "Do not marry. Do not have children here."
    },
    "3": {
      "L": "For thus says the LORD concerning the sons and daughters born in this place, and concerning their mothers who bore them and their fathers who fathered them in this land:",
      "M": "For this is what the LORD says about the sons and daughters born in this place, and about their mothers who bore them and their fathers who fathered them in this land:",
      "T": "For Yahweh says this about every child being born here — and about every mother who bears them and every father who brings them into this land:"
    },
    "4": {
      "L": "They shall die of grievous diseases; they shall not be lamented or buried; they shall be as dung upon the surface of the ground. By sword and famine they shall be consumed, and their corpses shall be food for the birds of the sky and for the beasts of the earth.",
      "M": "They will die of terrible diseases; no one will mourn for them or bury them — they will lie like dung on the surface of the ground. They will be killed by sword and famine, and their bodies will become food for the birds of the sky and the animals of the earth.",
      "T": "They will die of terrible diseases, left unlamented, left unburied — their bodies lying like dung on the open ground. Sword and famine will finish them, and their corpses will be food for birds and beasts. No one will care enough to grieve."
    },
    "5": {
      "L": "For thus says the LORD: Do not enter the house of mourning; do not go to lament or bemoan them; for I have taken away my peace from this people, says the LORD — even my steadfast love and my mercy.",
      "M": "For this is what the LORD says: Do not go into a house of mourning; do not go to lament or grieve over them; for I have withdrawn my peace from this people, declares the LORD — and my steadfast covenant love and my compassion.",
      "T": "Yahweh says: Do not enter a house of mourning. Do not go to lament or grieve. For I have withdrawn my peace from this people — and my steadfast covenant love, and my compassion. I have taken them all back."
    },
    "6": {
      "L": "Both great and small shall die in this land; they shall not be buried, and no one shall lament for them, or cut themselves, or shave themselves bald for them.",
      "M": "Both the great and the small will die in this land; no one will bury them, and no one will mourn for them — no one will cut themselves in grief or shave their heads for the dead.",
      "T": "Great and small alike will die in this land, unburied and unmourned. No one will cut themselves in grief. No one will shave their head for the dead. The old mourning rites will simply stop."
    },
    "7": {
      "L": "Neither shall anyone break bread for the mourner to comfort him for the dead, nor shall the cup of consolation be given to him to drink for his father or for his mother.",
      "M": "No one will offer food to the mourner to comfort him for the dead, and no one will give him the cup of consolation to drink for his father or his mother.",
      "T": "No one will bring food to comfort the mourner. No one will pass the cup of consolation to the one who has just buried a father or mother. The ordinary kindness of grief — even that will be gone."
    },
    "8": {
      "L": "You shall not go into the house of feasting to sit with them, to eat and to drink.",
      "M": "You shall not go into any house of feasting to sit and eat and drink with them either.",
      "T": "Nor are you to enter a house of celebration — no sitting down with them, no eating, no drinking."
    },
    "9": {
      "L": "For thus says the LORD of hosts, the God of Israel: Behold, I am causing to cease from this place, before your eyes and in your days, the voice of joy and the voice of gladness, the voice of the bridegroom and the voice of the bride.",
      "M": "For this is what the LORD of hosts, the God of Israel, says: I am about to silence in this place — within your own sight and within your own lifetime — the sound of joy and gladness, the voice of the bridegroom and the voice of the bride.",
      "T": "Yahweh God of hosts says: In your own lifetime, before your own eyes, I will silence this place. The sound of joy — gone. The sound of celebration — gone. The voice of the bridegroom, the voice of the bride — silenced."
    },
    "10": {
      "L": "And when you declare all these words to this people and they say to you: Why has the LORD pronounced all this great disaster against us? What is our iniquity? What sin have we committed against the LORD our God?",
      "M": "And when you announce all these things to this people and they ask you: Why has the LORD declared all this great disaster against us? What is our iniquity? What sin have we committed against the LORD our God?",
      "T": "When you announce all this and they challenge you — 'Why is Yahweh declaring all this disaster against us? What iniquity? What sin have we committed against Yahweh our God?' —"
    },
    "11": {
      "L": "Then you shall say to them: Because your fathers forsook me, says the LORD, and went after other gods and served them and worshipped them, and forsook me and did not keep my law.",
      "M": "Then say to them: Because your ancestors forsook me, declares the LORD, and went after other gods and served and worshipped them; they abandoned me and did not keep my law.",
      "T": "— answer them: Because your fathers walked away from Yahweh. They chased other gods, served them, bowed down to them. They abandoned me and refused to keep my law."
    },
    "12": {
      "L": "And you have done worse than your fathers; for behold, every one of you walks after the stubbornness of his evil heart and will not listen to me.",
      "M": "And you have done even worse than your fathers, for every one of you follows the stubborn evil of your own heart and refuses to listen to me.",
      "T": "And you are worse than your fathers. Every single one of you follows the hardness of your own evil heart. Not one of you will listen."
    },
    "13": {
      "L": "Therefore I will hurl you out of this land into a land that you have not known — neither you nor your fathers; and there you shall serve other gods day and night, for I will show you no favor.",
      "M": "Therefore I will cast you out of this land into a land that neither you nor your ancestors have ever known; and there you shall serve other gods day and night, for I will show you no mercy.",
      "T": "So I will throw you out of this land — into a land you have never known, that your fathers never knew. There you will serve other gods, day and night without ceasing, because I will show you no favor."
    },
    "14": {
      "L": "Therefore, behold, days are coming, says the LORD, when it shall no more be said: As the LORD lives who brought up the children of Israel out of the land of Egypt,",
      "M": "But days are coming, declares the LORD, when people will no longer say: As the LORD lives who brought Israel out of Egypt —",
      "T": "But a day is coming, says Yahweh, when that old oath — 'As the LORD lives who brought Israel out of Egypt' — will no longer be the one people swear by."
    },
    "15": {
      "L": "but: As the LORD lives who brought up the children of Israel from the land of the north and from all the lands where he had driven them; for I will bring them back to their own land that I gave to their fathers.",
      "M": "Instead they will say: As the LORD lives who brought Israel back from the land of the north and from all the countries where he had driven them. For I will bring them back to the land I gave to their ancestors.",
      "T": "Instead they will swear: 'As the LORD lives who brought Israel back from the north, from every land where he scattered them.' For I will bring them home — back to the land I gave their fathers."
    },
    "16": {
      "L": "Behold, I am sending for many fishers, says the LORD, and they shall fish them; and afterward I will send for many hunters, and they shall hunt them from every mountain and from every hill and out of the clefts of the rocks.",
      "M": "I am sending for many fishermen, declares the LORD, and they will fish them out; and after that I will send many hunters, who will hunt them down from every mountain and hill and out of every crevice in the rocks.",
      "T": "But before that restoration, there is judgment. I am calling fishers first — they will drag them out from wherever they hide. Then I am sending hunters, who will track them down from every mountain, every hill, every crack in the rock. There is no place they will not be found."
    },
    "17": {
      "L": "For my eyes are on all their ways; they are not hidden from before me, and their iniquity is not concealed from my eyes.",
      "M": "For my eyes are on all their ways; they are not hidden from my sight, and their guilt is not concealed from my eyes.",
      "T": "My eyes are on all of it. Nothing they do is hidden from me. Their guilt is not buried deep enough that I cannot see it."
    },
    "18": {
      "L": "And first I will repay double their iniquity and their sin, because they have defiled my land with the carcasses of their detestable idols and have filled my inheritance with their abominations.",
      "M": "First I will repay their guilt and their sin in double measure, because they have defiled my land with the lifeless images of their detestable idols and have crammed my inheritance with their abominations.",
      "T": "First comes the double repayment — their guilt, their sin, paid back in full and then again — because they defiled my land with the rotting carcasses of their idols and packed my inheritance full of their abominations."
    },
    "19": {
      "L": "O LORD, my strength and my stronghold and my refuge in the day of distress, to you the nations shall come from the ends of the earth and say: Our fathers have inherited nothing but falsehood, worthless things in which there is no profit.",
      "M": "O LORD, my strength and my fortified refuge in the day of distress, to you the nations will come from the ends of the earth and say: Our ancestors inherited only lies — empty things that are of no use at all.",
      "T": "O LORD, you are my strength, my fortress, my place of safety when disaster comes. The nations will come to you one day from the very ends of the earth and confess: Our fathers handed us nothing but lies — empty idols, worthless gods, not a shred of real help in any of them."
    },
    "20": {
      "L": "Can a man make for himself gods? But they are no gods!",
      "M": "Can a person make gods for himself? But they are no gods at all!",
      "T": "Can a human being manufacture a god? What a person makes is no god. It is nothing."
    },
    "21": {
      "L": "Therefore, behold, I am making them know — this once I will make them know my power and my might; and they shall know that my name is the LORD.",
      "M": "Therefore, I am going to make them know — this time I will make them know my hand and my strength; and they shall know that my name is the LORD.",
      "T": "So now I am going to show them. This time, they will learn what my hand can do — what my power truly is. And they will know that my name is Yahweh."
    }
  },
  "17": {
    "1": {
      "L": "The sin of Judah is written with a pen of iron; with a point of diamond it is engraved on the tablet of their heart and on the horns of their altars.",
      "M": "Judah's sin is written with an iron stylus; with a diamond tip it is engraved on the tablet of their heart and on the horns of their altars.",
      "T": "Judah's sin is not scratched lightly — it is cut deep with an iron pen, with a diamond point, engraved on the very tablets of their hearts and on the horns of their altars. It does not rub off."
    },
    "2": {
      "L": "While their children remember their altars and their Asherah poles beside the trees upon the high hills.",
      "M": "Even their children remember their altars and their Asherah poles beside every spreading tree on every high hill.",
      "T": "Their children have grown up learning this — altars on every hill, Asherah poles under every spreading tree. The next generation has it memorized."
    },
    "3": {
      "L": "O mountain in the field, your wealth and all your treasures I will give as plunder, with your high places for sin throughout all your territory.",
      "M": "O mountain in the open country, I will hand over your wealth and all your treasures as plunder, along with your high shrines, on account of sin throughout all your borders.",
      "T": "You, hill city standing in the open land — I will hand over your wealth and all your treasures as plunder. Your high shrines across every border will go with them, the price of your sin."
    },
    "4": {
      "L": "And by your own hand you shall forfeit your heritage that I gave you; and I will make you serve your enemies in a land you do not know; for you have kindled a fire in my anger that shall burn forever.",
      "M": "Through your own actions you will forfeit the inheritance I gave you; I will make you serve your enemies in a land you do not know; for you have lit a fire in my anger that will burn on without end.",
      "T": "You will let go of your own inheritance — the land I gave you, you will throw it away with your own hands. I will put you to work serving your enemies in a land you don't know. Because you lit a fire in my anger — and it will not go out."
    },
    "5": {
      "L": "Thus says the LORD: Cursed is the man who trusts in man and makes flesh his arm, and whose heart turns away from the LORD.",
      "M": "This is what the LORD says: Cursed is the one who puts his trust in human beings, who relies on human strength and turns his heart away from the LORD.",
      "T": "Yahweh says: The one who puts his trust in people — who leans on human strength as if it were an arm of iron, whose heart has drifted away from Yahweh — that person is cursed."
    },
    "6": {
      "L": "He shall be like a shrub in the desert and shall not see good when it comes; he shall inhabit the parched places in the wilderness, a salty, uninhabited land.",
      "M": "He will be like a desert shrub that never benefits when good comes; he will dwell in the parched places of the wilderness, a barren, salty land where no one lives.",
      "T": "He is like a desert thornbush — even when the rain falls he gets none of it. He lives in the burnt wastelands, in the salt flats where nothing grows and no one settles."
    },
    "7": {
      "L": "Blessed is the man who trusts in the LORD, whose trust is the LORD.",
      "M": "Blessed is the one who trusts in the LORD, whose confidence rests in the LORD.",
      "T": "But the one who trusts in Yahweh — whose sole confidence is Yahweh — that person is truly blessed."
    },
    "8": {
      "L": "He shall be like a tree planted by water, that sends out its roots by the stream; it shall not fear when heat comes; its leaves shall remain green; in the year of drought it is not anxious, and it does not cease to bear fruit.",
      "M": "He will be like a tree planted beside a stream, sending its roots out to the water. It does not fear when the heat comes; its leaves stay green; in a year of drought it is not anxious and never stops bearing fruit.",
      "T": "That person is like a tree planted by a stream — roots reaching down to the water, leaves staying green through the hottest summer, unhurried in years of drought, never stopping its fruit-bearing. Unshaken by whatever the season brings."
    },
    "9": {
      "L": "Deceitful is the heart above all things, and desperately sick; who can know it?",
      "M": "The heart is more deceitful than anything else and is desperately sick — who can understand it?",
      "T": "The human heart — deceitful beyond all reckoning, sick to the point of corruption. Who can possibly know it from the inside?"
    },
    "10": {
      "L": "I the LORD search the heart; I test the mind to give to each man according to his ways, according to the fruit of his deeds.",
      "M": "I, the LORD, examine the heart and test the inner mind, to give everyone what their conduct and actions deserve.",
      "T": "I, Yahweh, search the heart. I probe the inner mind. I give to each person exactly what their conduct and their choices deserve."
    },
    "11": {
      "L": "Like a partridge that gathers a brood she did not hatch, so is the one who makes riches but not by justice; in the middle of his days they shall leave him, and at his end he shall be a fool.",
      "M": "Like a partridge brooding over eggs she did not lay, so is the one who gains wealth unjustly; in the middle of his life his riches will leave him, and at the end he will prove to be a fool.",
      "T": "The person who accumulates wealth by unjust means is like a partridge hatching eggs she didn't lay — the chicks will leave her. In the middle of life his wealth will walk out on him, and at the end he will be exposed for the fool he always was."
    },
    "12": {
      "L": "A throne of glory, set on high from the beginning, is the place of our sanctuary.",
      "M": "A glorious throne, exalted from the beginning, is the place of our sanctuary.",
      "T": "A throne of glory, raised high from the very beginning — that is where our sanctuary stands. That is what we are defending."
    },
    "13": {
      "L": "O LORD, the hope of Israel, all who forsake you shall be put to shame; those who turn away from you shall be written in the earth, for they have forsaken the LORD, the fountain of living waters.",
      "M": "O LORD, the hope of Israel, all who forsake you will be put to shame; those who turn from you will have their names written in the dust, for they have abandoned the LORD, the source of living water.",
      "T": "O LORD — Israel's hope, Israel's only hope — all who abandon you will end in shame. Those who turn away will have their names written in the dust, not in stone, because they have walked away from Yahweh, the spring of living water."
    },
    "14": {
      "L": "Heal me, O LORD, and I shall be healed; save me, and I shall be saved; for you are my praise.",
      "M": "Heal me, O LORD, and I will truly be healed; save me, and I will truly be saved; for you are the one I praise.",
      "T": "Heal me, LORD — if you heal me, I will be healed for real. Save me — if you save me, I will be truly safe. You are the only one I praise."
    },
    "15": {
      "L": "Behold, they say to me: Where is the word of the LORD? Let it come!",
      "M": "See how they taunt me: Where is the word of the LORD? Let it come, if it is real!",
      "T": "Listen to what they say to me: 'Where is this word of Yahweh you keep threatening us with? Let it show up — if it is ever going to.'"
    },
    "16": {
      "L": "But I have not hastened away from following you as a shepherd, nor have I desired the day of the wound; you know what came forth from my lips — it was before your face.",
      "M": "But I have not run away from the calling of being your shepherd; the day of disaster is not something I have longed for — you know this; what my lips spoke was in your presence.",
      "T": "I never ran from the calling — never fled from being your prophet-shepherd. I never wanted the day of disaster. You know everything I said; all of it was spoken in your presence. I asked for nothing I should not have."
    },
    "17": {
      "L": "Do not be a terror to me; you are my refuge in the day of disaster.",
      "M": "Do not be a source of dread to me; you are my shelter in the day of disaster.",
      "T": "Do not be the very thing I fear. You are supposed to be my safe place when disaster comes."
    },
    "18": {
      "L": "Let my persecutors be shamed, but let me not be shamed; let them be dismayed, but let me not be dismayed; bring upon them the day of disaster, and destroy them with double destruction.",
      "M": "Let those who persecute me be shamed — but not me; let them be dismayed — but not me; bring the day of disaster upon them, and destroy them with double destruction.",
      "T": "Let those who hound me be the ones who end in shame — not me. Let them be the ones who are dismayed — not me. Bring the day of disaster down on them. Destroy them completely — twice what they deserve."
    },
    "19": {
      "L": "Thus said the LORD to me: Go and stand in the gate of the sons of the people, by which the kings of Judah come in and by which they go out, and in all the gates of Jerusalem.",
      "M": "Thus the LORD said to me: Go and stand at the People's Gate, through which the kings of Judah enter and leave, and at all the gates of Jerusalem.",
      "T": "Yahweh said to me: Go stand at the gate the people use — the one the kings of Judah pass through going in and out — and at every gate of Jerusalem."
    },
    "20": {
      "L": "And say to them: Hear the word of the LORD, you kings of Judah, and all Judah, and all the inhabitants of Jerusalem who enter by these gates.",
      "M": "Say to them: Hear the word of the LORD, you kings of Judah, all of Judah, and all the inhabitants of Jerusalem who come in through these gates.",
      "T": "Say this to them: Kings of Judah, all of Judah, every inhabitant of Jerusalem who walks through these gates — hear the word of Yahweh."
    },
    "21": {
      "L": "Thus says the LORD: Take heed for the sake of your lives, and do not carry any burden on the Sabbath day or bring it in through the gates of Jerusalem.",
      "M": "This is what the LORD says: Take care for your own sakes and do not carry any load on the Sabbath day or bring it in through the gates of Jerusalem.",
      "T": "Yahweh says: Guard your lives by doing this — carry no load on the Sabbath. Do not bring cargo through the gates of Jerusalem on that day."
    },
    "22": {
      "L": "And do not carry a burden out of your houses on the Sabbath day, and do no work on it; but keep the Sabbath day holy, as I commanded your fathers.",
      "M": "Do not carry burdens out of your houses on the Sabbath day, and do no work on it. Keep the Sabbath day holy, as I commanded your ancestors.",
      "T": "Do not carry loads out of your houses on the Sabbath. Do no work. Keep the Sabbath holy — this is what I commanded your fathers."
    },
    "23": {
      "L": "Yet they did not listen or incline their ear; they hardened their neck so as not to hear and not to receive discipline.",
      "M": "But they did not listen or pay attention; they stiffened their neck and would not hear or accept correction.",
      "T": "But they did not listen. They did not lean in to hear. They stiffened their necks against both the instruction and the correction."
    },
    "24": {
      "L": "But if you truly listen to me, says the LORD, and bring no burden through the gates of this city on the Sabbath day, and keep the Sabbath day holy by doing no work on it,",
      "M": "But if you truly listen to me, declares the LORD, and bring no load through the gates of this city on the Sabbath day, and keep the Sabbath holy by doing no work on it,",
      "T": "But if you will only listen — says Yahweh — if you carry nothing through these gates on the Sabbath, if you keep it holy and do no work on it,"
    },
    "25": {
      "L": "then there shall enter through the gates of this city kings and princes sitting on the throne of David, riding in chariots and on horses — they and their princes, the men of Judah and the inhabitants of Jerusalem — and this city shall remain inhabited forever.",
      "M": "then kings and princes sitting on David's throne will enter through the gates of this city — riding in chariots and on horses, they and their officials, the men of Judah and the inhabitants of Jerusalem. This city will be inhabited forever.",
      "T": "— then kings will ride through these gates on chariots and horses, kings sitting on the throne of David, with all their officials, the people of Judah, and every inhabitant of Jerusalem. This city will stand forever, inhabited and full."
    },
    "26": {
      "L": "And they shall come from the cities of Judah and from the places around Jerusalem, from the land of Benjamin, from the Shephelah, from the hill country, and from the Negev, bringing burnt offerings and sacrifices and grain offerings and frankincense, and bringing thank offerings to the house of the LORD.",
      "M": "People will come from the towns of Judah and the villages around Jerusalem, from the land of Benjamin, from the Shephelah, from the hill country, and from the Negev, bringing burnt offerings and sacrifices, grain offerings and frankincense, and thank offerings to the house of the LORD.",
      "T": "People will stream in from every corner — from Judah's towns, from the countryside around Jerusalem, from Benjamin, from the western foothills, from the hill country, from the Negev — bringing burnt offerings, sacrifices, grain offerings, incense, and thank offerings to the house of Yahweh."
    },
    "27": {
      "L": "But if you will not listen to me to keep the Sabbath day holy, and to not carry a burden while entering through the gates of Jerusalem on the Sabbath day, then I will kindle a fire in its gates, and it shall devour the palaces of Jerusalem and shall not be quenched.",
      "M": "But if you will not listen to me — if you refuse to keep the Sabbath day holy, and insist on carrying loads through the gates of Jerusalem on the Sabbath — then I will kindle a fire in those gates, and it will devour the palaces of Jerusalem and will not be put out.",
      "T": "But if you will not listen — if you refuse the Sabbath, if you keep hauling loads through these gates on that day — I will set fire to the very gates. The fire will eat through the palaces of Jerusalem. And it will not be put out."
    }
  },
  "18": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD:",
      "M": "This is the word that came to Jeremiah from the LORD:",
      "T": "This is the word that came to Jeremiah from Yahweh:"
    },
    "2": {
      "L": "Arise and go down to the potter's house, and there I will cause you to hear my words.",
      "M": "Get up and go down to the potter's house, and there I will let you hear my words.",
      "T": "Get up and go to the potter's house. I will speak to you there."
    },
    "3": {
      "L": "So I went down to the potter's house, and there he was working at his wheel.",
      "M": "So I went down to the potter's house, and he was there, working at the wheel.",
      "T": "I went to the potter's house. There he was at the wheel, working."
    },
    "4": {
      "L": "And the vessel that he was making of clay was spoiled in the potter's hand; so he reworked it into another vessel, as it seemed good to the potter to do.",
      "M": "The clay vessel he was shaping was ruined in his hands; so he reworked it into another vessel, as seemed best to him.",
      "T": "The pot he was shaping was ruined in his hands. So he took the same clay and worked it again, reshaping it into a different vessel — whatever seemed right to him."
    },
    "5": {
      "L": "Then the word of the LORD came to me:",
      "M": "Then the word of the LORD came to me:",
      "T": "Then Yahweh's word came to me:"
    },
    "6": {
      "L": "Can I not do to you as this potter has done, O house of Israel? — declares the LORD. Behold, like the clay in the potter's hand, so are you in my hand, O house of Israel.",
      "M": "Can I not deal with you as this potter has dealt with the clay, O house of Israel? — declares the LORD. Like clay in the potter's hand, so are you in my hand, house of Israel.",
      "T": "Israel, can I not do with you what the potter does with clay? Of course I can, says Yahweh. You are in my hands exactly as clay is in the potter's hands."
    },
    "7": {
      "L": "At one moment I may speak concerning a nation or a kingdom, to pluck up and to break down and to destroy it;",
      "M": "There are times when I pronounce concerning a nation or kingdom that I will uproot it, tear it down, and destroy it;",
      "T": "Sometimes I pronounce a word of judgment over a nation or kingdom — that I will uproot it, pull it down, and destroy it."
    },
    "8": {
      "L": "but if that nation against which I have spoken turns from its evil, I will relent of the disaster I planned to bring upon it.",
      "M": "but if that nation turns from its evil, I will relent concerning the disaster I intended to bring on it.",
      "T": "But if that nation turns from its evil — I will relent. I will change the judgment I had planned."
    },
    "9": {
      "L": "And at another moment I may speak concerning a nation or a kingdom, to build and to plant it;",
      "M": "And there are times when I declare concerning a nation or kingdom that I will build and plant it;",
      "T": "At other times I pronounce a word of blessing — that I will build up a nation, plant it firmly."
    },
    "10": {
      "L": "but if it does evil in my sight by not listening to my voice, I will relent of the good with which I said I would benefit it.",
      "M": "but if that nation does evil in my sight and does not obey me, I will relent of the good I said I would do for it.",
      "T": "But if that nation does evil in my sight and refuses to listen — I will take back the good I had promised."
    },
    "11": {
      "L": "Now therefore speak to the men of Judah and to the inhabitants of Jerusalem: Thus says the LORD: Behold, I am shaping disaster against you and devising a plan against you. Return now, every man from his evil way, and make your ways and your deeds good.",
      "M": "Now therefore speak to the men of Judah and the inhabitants of Jerusalem: This is what the LORD says — I am shaping disaster against you right now and devising a plan against you. Turn back, each of you from your evil way, and amend your ways and your conduct.",
      "T": "So go now and tell the men of Judah and the people of Jerusalem: Yahweh says — I am shaping a disaster, I am working out a plan against you right now. Turn back — every one of you, turn from your evil. Fix your ways. Fix your conduct. There is still time."
    },
    "12": {
      "L": "But they said: It is hopeless! For we will follow our own plans, and each of us will act according to the stubbornness of his evil heart.",
      "M": "But they say: It is useless! We will follow our own plans and act according to the stubborn evil of our own hearts.",
      "T": "But they say: It is hopeless. We are going to do what we planned. Every one of us will follow the hardness of our own evil heart. We are not turning."
    },
    "13": {
      "L": "Therefore thus says the LORD: Ask among the nations — who has heard such a thing? The virgin of Israel has done a very horrible thing.",
      "M": "Therefore this is what the LORD says: Ask around among the nations — who has ever heard anything like this? The virgin Israel has done a truly horrifying thing.",
      "T": "So Yahweh says: Ask anywhere — ask any nation you like — has anyone ever heard anything like this? Israel, once as pure as a virgin, has done a monstrous, horrifying thing."
    },
    "14": {
      "L": "Does the snow of Lebanon leave the rocky crags of the field? Shall the cold flowing waters from afar be forsaken?",
      "M": "Does the snow of Lebanon ever leave the mountain crags? Do the cold streams flowing down from distant heights ever run dry?",
      "T": "Does the snow ever leave the peaks of Lebanon? Do the cold mountain streams from far away ever stop flowing? Of course not. Nature stays faithful to its course — and yet —"
    },
    "15": {
      "L": "For my people have forgotten me; they burn offerings to worthless things, and they have stumbled in their ways, in the ancient paths, and have gone into byroads not built up.",
      "M": "Yet my people have forgotten me; they burn offerings to worthless idols. They have stumbled off the ancient paths and gone down side trails — roads no one laid out.",
      "T": "— my people have forgotten me. They burn offerings to nothing — to empty, worthless idols. They have stumbled off the ancient paths and gone wandering down makeshift trails that lead nowhere."
    },
    "16": {
      "L": "Making their land a desolation, an object of hissing forever; everyone who passes by it shall be horrified and shake his head.",
      "M": "They have made their land a desolation, a thing to be hissed at forever; everyone who passes by will be horrified and shake their head.",
      "T": "They have turned their own land into a permanent wasteland — a ruin that travelers will hiss at and walk away from shaking their heads in disbelief."
    },
    "17": {
      "L": "Like an east wind I will scatter them before the enemy; I will show them my back and not my face in the day of their disaster.",
      "M": "Like a scorching east wind I will scatter them before the enemy; I will show them my back, not my face, in the day of their calamity.",
      "T": "Like a scorching east wind I will scatter them before their enemies. In the day of their ruin I will turn my back on them — not my face. They will see only my back as I walk away."
    },
    "18": {
      "L": "Then they said: Come, let us devise plans against Jeremiah; for the law shall not perish from the priest, nor counsel from the wise, nor the word from the prophet. Come, let us strike him with the tongue, and let us not give heed to any of his words.",
      "M": "Then they said: Come, let us make plans against Jeremiah, for instruction will still come from the priests, counsel from the wise, and a word from the prophets. Come, let us attack him with our words, and let us not pay attention to anything he says.",
      "T": "Then they began to scheme against me: 'Come — let us deal with Jeremiah. The priests will still give instruction. The wise men will still give counsel. The prophets will still give us a word from God. We do not need him. Let us attack him with words. Let us make sure no one pays attention to what he says.'"
    },
    "19": {
      "L": "Give heed to me, O LORD, and listen to the voice of my opponents.",
      "M": "Give attention to me, O LORD; listen to what my adversaries are saying.",
      "T": "Listen to me, LORD. Hear what my enemies are planning."
    },
    "20": {
      "L": "Shall evil be repaid for good? For they have dug a pit for my life. Remember how I stood before you to speak good for them, to turn back your wrath from them.",
      "M": "Should good be paid back with evil? Yet they have dug a pit for my life. Remember how I stood before you and pleaded for them, to turn your wrath away from them.",
      "T": "Is this how they repay good — with a pit dug for my life? I stood before you and pleaded their case. I asked you to pull your anger back from them. And this is what they give me in return."
    },
    "21": {
      "L": "Therefore give their children over to famine, and deliver them into the power of the sword; let their wives become childless and widowed; let their men be struck down by death, their young men slain by the sword in battle.",
      "M": "Therefore hand their children over to famine; give them into the power of the sword; let their wives be left childless and widowed; let their men be struck down by plague, their young men killed by the sword in battle.",
      "T": "So let their children be given over to famine. Hand them over to the sword. Let their wives lose their children and become widows. Let pestilence cut down their men, the sword their young men in the field."
    },
    "22": {
      "L": "Let a cry be heard from their houses when you bring raiders against them suddenly; for they have dug a pit to catch me and laid snares for my feet.",
      "M": "Let a cry be heard from their houses when you bring marauders against them without warning; for they have dug a pit to trap me and laid snares for my feet.",
      "T": "Let a cry tear through their houses when you send raiders on them without warning — because they dug a pit to catch me, they laid traps for my feet."
    },
    "23": {
      "L": "Yet you, O LORD, know all their plotting against me to put me to death; do not forgive their iniquity, nor blot out their sin from your sight; let them be overthrown before you; deal with them in the time of your anger.",
      "M": "But you, O LORD, know all their schemes against my life. Do not forgive their guilt or erase their sin from your sight. Let them be brought down before you; deal with them in the time of your anger.",
      "T": "And you, LORD — you know every detail of what they are plotting against me. Do not forgive their guilt. Do not wipe their sin clean. Let them stumble and fall before you. Deal with them in your time of wrath."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 16–18 written.')

if __name__ == '__main__':
    main()
