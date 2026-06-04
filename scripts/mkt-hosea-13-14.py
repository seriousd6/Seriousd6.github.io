"""
MKT Hosea chapters 13–14 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hosea-13-14.py

=== CHAPTER OVERVIEW ===

Chapter 13: The Death Sentence on Ephraim.
  The chapter opens with Ephraim's former glory ("when Ephraim spoke, the nations
  trembled") contrasted with his present death through Baal worship (v.1). Four
  metaphors of transience describe their coming disappearance: morning mist, dew,
  chaff, smoke (v.3). God reasserts his identity as the Exodus-covenant LORD and
  sole savior (v.4); the wilderness provision (v.5) is met with the predictable
  forgetting-born-from-fullness (v.6).

  The predator sequence (vv.7–8) escalates: lion → leopard → mother bear bereaved
  of cubs — the most ferocious of all (cf. 2 Sam 17:8). The bear tears open the
  "caul of their heart" — i.e., the pericardium, the membrane around the heart,
  making the imagery of total exposure visceral.

  vv.9–11: A devastating play on the monarchy. The people cried for a king
  (1 Sam 8); now "where is your king to save you?" Yahweh gave a king in anger
  and took him back in wrath.

  v.12: Sin bound up, stored, kept on file — not forgotten, awaiting the day of
  its unsealing.

  v.13: Birth-canal image. Ephraim is an unwise child who, at the crucial moment
  of emergence, refuses to come out. The image of new life available but refused.

  v.14: The great ambiguous verse — translated as judgment in its OT context
  (see below), yet quoted by Paul in 1 Cor 15:55 as triumphant resurrection
  language. Both are authentic readings of the Hebrew; the docstring notes the
  tension explicitly.

  v.15: The east wind (sirocco) as the LORD's judgment — the pun on Ephraim's
  name ("Fruitful") makes the irony sharp. The wind dries every spring and
  fountain; the invading army plunders everything.

  v.16: Samaria's fall depicted in brutal ANE terms — the standard formula of
  conquest (infants dashed, pregnant women ripped open). Historically realized
  in the Assyrian conquest of 722 BCE.

Chapter 14: The Call and the Promise of Return.
  The sharpest reversal in Hosea. After ch. 13's unrelenting judgment, ch. 14
  opens with a direct call to return (v.1), a prescribed prayer of confession
  (vv.2–3), and Yahweh's reply of free, unconditional love (v.4).

  vv.5–7: The restoration described in botanical images of extraordinary beauty —
  dew, lily, Lebanon's roots, olive oil, fragrance, grain, vine, wine. The same
  agricultural blessings that Israel had attributed to the Baals (2:8) are now
  given freely by Yahweh without covenantal conditions.

  v.8: Ephraim's conversion expressed in his own words. Yahweh responds: "I am
  like a green cypress — all your fruitfulness comes from me." (Another echo of
  Ephraim's name.)

  v.9: The Wisdom closing formula (cf. Ps 107:43; Prov 1:5–6). The prophetic
  word becomes wisdom literature: those who are wise will understand; the
  righteous will walk in these ways; transgressors will stumble. Hosea ends
  where Wisdom literature begins — the fear of the LORD.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh): Consistent with mkt-hosea-1-6.py: L/M = "LORD" (small
  caps convention). T = "Yahweh" in prophetic-oracle contexts (13:4, 13:15,
  14:1, 14:9) where the covenant name is covenantally weighted.

- H430 (אֱלֹהִים / Elohim / God): "God" in all tiers throughout. 13:4 is the
  covenant formula "I am the LORD your God" — kept as-is in all tiers.

- H7585 (שְׁאוֹל / Sheol): L: "Sheol." M: "the grave." T: "Sheol" (retaining the
  Hebrew name when Death is personified in 13:14, as Paul does in 1 Cor 15:55).

- H4194 (מָוֶת / mavet / Death): L/M: "death." T: "Death" (capital) in 13:14
  where Death is personified and addressed directly as a power.

- 13:14 — taunt or promise? The Hebrew grammar allows both readings:
  (a) PROMISE: "I will ransom them from the power of Sheol / I will redeem them
      from death" — as in KJV, and as Paul quotes in 1 Cor 15:55 triumphantly.
  (b) TAUNT/SUMMONS (contextual): The chapter 13 context is unremitting judgment
      (vv.3, 7–9, 12–13, 15–16), making a sudden promise of rescue jarring. The
      final line ("Repentance/compassion is hidden from my eyes") seals the
      judgment reading. Many modern commentators (Stuart, Andersen-Freedman,
      Wolff) read vv.14a–b as rhetorical questions: "Shall I ransom? Shall I
      redeem?" with an implied "No!" — followed by a summons to Death and Sheol
      to do their worst.
  DECISION: L keeps the Hebrew ambiguous (literal interrogatives). M renders as
  the judgment-summons reading (fits the OT context). T renders as summons but
  notes the NT reversal in a parenthetical phrase — both meanings are authentic,
  the latter being the prophetic original, the former Paul's inspired inversion.

- H4878 (מְשׁוּבָה / meshuvah / backsliding): L: "backsliding." M: "waywardness."
  T: "faithlessness" (14:4). The word is the noun form of the verb shuv
  ("return") — it denotes the failure to return, i.e., persistent turning away.
  The irony that the same root appears in the call to "return" (14:1) and in
  the disease to be healed (14:4) is surfaced in T.

- H2919 (טַל / tal / dew): 14:5 — "I will be as the dew unto Israel." In an arid
  climate, dew is life-giving. L/M: "dew." T: "morning dew" to surface the
  life-giving aspect in a summer-dry land context.

- H1265 (בְּרוֹשׁ / berosh / fir/cypress tree): 14:8 — "I am like a green
  fir/cypress tree." L: "fir tree." M/T: "cypress" — the berosh is more likely
  a juniper or cypress than a true fir; it is tall, evergreen, and associated
  with Lebanon. "Cypress" is the more natural English equivalent.

- H6499 / H8193 in 14:2 ("calves of our lips"): A hapax construction. L keeps
  "calves of our lips" (the literal image, also reflecting the animal sacrifice
  vocabulary). M/T render as "the praise of our lips" — i.e., verbal sacrifice
  replacing animal sacrifice; this interpretation is reflected in Heb 13:15 LXX
  tradition ("fruit of lips"). The T tier makes explicit that this is an offering
  of words in place of animals.

- H6500 (פָּרַה / parah / to be fruitful) in 13:15: The pun on Ephraim (H669,
  etymologically from parah = "to be fruitful"). T surfaces the wordplay: "Even
  though he bears the name Fruitful..."

- Poetic structure: Ch. 14:5–9 is poetry with sustained botanical parallelism.
  T tier uses line breaks to preserve the parallelism and cadence. M uses
  flowing prose. L preserves word order.

- Aspect (Hebrew perfect/imperfect): Ch. 13 uses prophetic perfects (judgment
  already as good as done) throughout; rendered as English futures in L/M where
  they function as predictions, with T sometimes shifting to present-tense
  dramatic immediacy to reflect the prophetic certainty of the judgment.

- OT intertextuality:
  - 13:4: Exodus covenant formula ("I am the LORD your God from the land of
    Egypt") — echoes Ex 20:2 / Deut 5:6; surfaced explicitly in T.
  - 13:9: The people's self-destruction echoes Deut 32 (the Song of Moses).
  - 13:10–11: The demand for a king (1 Sam 8) and its bitter result surfaced
    in T's ironic reading.
  - 13:14: Paul's quotation in 1 Cor 15:55 is noted in the header; not inserted
    into verse text but surfaces in T's phrasing.
  - 14:2: "Calves of our lips" — anticipates Heb 13:15 LXX "fruit of lips."
  - 14:9: Wisdom closing — echoes Ps 107:43 ("Whoever is wise, let him observe
    these things").
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

HOSEA = {
    "13": {
        "1": {
            "L": "When Ephraim spoke, there was trembling; he was exalted in Israel. But when he offended in Baal, he died.",
            "M": "When Ephraim spoke, the nations trembled; he was the great power in Israel. But when he became guilty through Baal worship, he died.",
            "T": "Once, when Ephraim spoke, the whole land trembled at his authority — he was the dominant force in Israel. But when he made himself guilty through Baal, he was finished."
        },
        "2": {
            "L": "And now they sin more and more, and have made for themselves molten images of their silver, idols according to their own understanding — all of it the work of craftsmen. They say of them, Let the men that sacrifice kiss the calves.",
            "M": "Now they sin more and more, making molten images from their silver, idols shaped according to their own devising — all the work of craftsmen. They say of them, Let the men who sacrifice kiss the calf idols.",
            "T": "Their sinning only deepens. They have smelted their silver into molten images — idols designed from their own imaginations, manufactured by hired craftsmen. And the priests tell the worshippers: 'Kiss the calves.' This is what Israelite worship has become."
        },
        "3": {
            "L": "Therefore they shall be as the morning cloud, and as the early dew that passeth away, as the chaff driven from the threshing floor by the whirlwind, and as the smoke out of the window.",
            "M": "Therefore they will be like morning mist, like the early dew that disappears, like chaff swept from a threshing floor by a storm wind, and like smoke through a window.",
            "T": "They will vanish —\nlike morning mist when the sun rises,\nlike dew gone by midmorning,\nlike chaff the wind scatters from the threshing floor,\nlike smoke that slips out through a window and is gone.\nNothing will remain of them."
        },
        "4": {
            "L": "Yet I am the LORD thy God from the land of Egypt, and thou shalt know no god but me: for there is no saviour beside me.",
            "M": "But I am the LORD your God from the land of Egypt, and you shall acknowledge no god but me; there is no savior except me.",
            "T": "But I — I am Yahweh your God, the one who brought you out of Egypt. You are to know no god but me. There is no deliverer but me. There never was."
        },
        "5": {
            "L": "I knew thee in the wilderness, in the land of great drought.",
            "M": "I knew you in the wilderness, in a land of scorching heat.",
            "T": "In that wilderness — that burning, waterless land — I was the one who knew you and kept you alive."
        },
        "6": {
            "L": "When they were fed they were filled, and when they were filled their heart was lifted up; therefore have they forgotten me.",
            "M": "When I fed them, they were satisfied; when they were satisfied, their hearts grew proud; therefore they forgot me.",
            "T": "I fed them; they were satisfied. Satisfaction became pride, and pride became forgetting. They forgot me. It is the oldest pattern in Israel's story."
        },
        "7": {
            "L": "Therefore I will be unto them as a lion: as a leopard by the way will I observe them.",
            "M": "So I will be to them like a lion; I will lurk like a leopard on the road.",
            "T": "So now I become their predator — a lion in their path, a leopard crouching in ambush by the road."
        },
        "8": {
            "L": "I will meet them as a bear robbed of her whelps, and will rend the caul of their heart, and there will I devour them like a lion: the wild beast shall tear them.",
            "M": "I will attack them like a bear robbed of her cubs; I will tear open their chests and devour them there like a lion. The wild animals will mangle them.",
            "T": "I will come at them like a mother bear whose cubs have been taken — nothing is more fierce. I will rip open their rib cages, lay bare their hearts, and devour them like a lion. Whatever is left, the beasts of the open country will finish."
        },
        "9": {
            "L": "O Israel, thou hast destroyed thyself; but in me is thine help.",
            "M": "O Israel, you have destroyed yourself; but your help is in me alone.",
            "T": "Israel — you have done this to yourself. But I remain the only one who could have saved you."
        },
        "10": {
            "L": "Where is thy king now, that he may save thee in all thy cities? and thy judges of whom thou saidst, Give me a king and princes?",
            "M": "Where is your king now, that he may save you in all your cities? Where are the rulers of whom you said, Give us a king and princes?",
            "T": "Where is your king now? Where is he to save you in all your cities? Where are all the rulers you demanded — when you cried, 'Give us a king! Give us leaders!' — as if a human king could be your salvation?"
        },
        "11": {
            "L": "I gave thee a king in mine anger, and took him away in my wrath.",
            "M": "I gave you a king in my anger, and I took him away in my wrath.",
            "T": "I gave you a king in my rage — and in my fury I reclaimed him. The monarchy was never a gift; it was a concession to your rebellion."
        },
        "12": {
            "L": "The iniquity of Ephraim is bound up; his sin is stored away.",
            "M": "The iniquity of Ephraim is stored up; his sin is kept on record.",
            "T": "Ephraim's guilt has been bound up, sealed, filed away — not forgotten, but kept. It waits for the day it will be unsealed."
        },
        "13": {
            "L": "The sorrows of a travailing woman shall come upon him: he is an unwise son; for he should not tarry long in the place of the breaking forth of children.",
            "M": "The pains of a woman in childbirth will come upon him. He is an unwise child — for when the time comes he does not present himself at the moment of birth.",
            "T": "The labor pains of childbirth will seize him. But Ephraim is a fool of a child: at the very moment he should emerge into new life, he refuses to come out. He cannot seize the moment that would remake him."
        },
        "14": {
            "L": "Shall I ransom them from the power of Sheol? Shall I redeem them from death? O Death, where are thy plagues? O Sheol, where is thy destruction? Repentance is hid from mine eyes.",
            "M": "Shall I ransom them from the power of the grave? Shall I redeem them from death? Come, Death, with your plagues! Come, Grave, with your destruction! No compassion will be hid from my eyes — I will show them none.",
            "T": "Will I rescue them from Death's grip — redeem them from Sheol? No. Death, bring your plagues! Sheol, unleash your destruction! I will show them no pity. — These words later ring through Paul's lips in 1 Corinthians 15 as a victory taunt over a defeated enemy; here, in Hosea's mouth, they are a terrible summons: God calling Death to do its work."
        },
        "15": {
            "L": "Though he be fruitful among his brothers, an east wind shall come, the wind of the LORD rising from the wilderness, and his spring shall become dry and his fountain shall be dried up: he shall spoil the treasure of all precious vessels.",
            "M": "Though he flourishes among his brothers, an east wind will come — the LORD's wind rising from the wilderness — and his spring will fail and his fountain dry up. That wind will strip away the treasure of every precious thing.",
            "T": "Ephraim's very name means Fruitful — and for a season he lived up to it. But an east wind is coming, rising out of the wilderness, driven by Yahweh himself. The sirocco dries every spring and shrivels every fountain. And the army that follows that wind will plunder every precious thing they own."
        },
        "16": {
            "L": "Samaria shall be held desolate; for she hath rebelled against her God: they shall fall by the sword: their infants shall be dashed in pieces, and their women with child shall be ripped up.",
            "M": "Samaria will be held guilty, for she has rebelled against her God. They will fall by the sword; their infants will be dashed to pieces, and their pregnant women will be ripped open.",
            "T": "Samaria will bear her guilt — she has defied her God. They will die by the sword. Their babies will be dashed against the stones; their pregnant women will be cut open. This is what ancient conquest looked like, and Yahweh will not shield a people who have refused him."
        }
    },
    "14": {
        "1": {
            "L": "Return, O Israel, unto the LORD thy God; for thou hast fallen by thine iniquity.",
            "M": "Return, O Israel, to the LORD your God, for your sins have caused you to stumble.",
            "T": "Come back, Israel — come back to Yahweh your God. You have fallen because of your own sin; only he can raise you."
        },
        "2": {
            "L": "Take with you words, and return to the LORD: say unto him, Take away all iniquity, and receive us graciously: so will we render the calves of our lips.",
            "M": "Take words with you and return to the LORD; say to him, Forgive all our sins and receive us graciously, and we will offer the praise of our lips as our sacrifice.",
            "T": "Come to Yahweh with words — not animals, but words. Say this to him: 'Lift every sin away from us. Receive us back in grace. We will pay you back with the only offering we have left — the praise that rises from our lips, our words of thanksgiving instead of calves on an altar.'"
        },
        "3": {
            "L": "Asshur shall not save us; we will not ride upon horses; neither will we say any more to the work of our hands, Ye are our gods: for in thee the fatherless findeth mercy.",
            "M": "Assyria will not save us; we will not ride on horses; we will never again say to what our hands have made, You are our gods. For in you the orphan finds compassion.",
            "T": "We will not look to Assyria to save us. We will not trust in cavalry or military power. We will never again bow to anything our own hands have made and call it God. For in you — you alone — the helpless find mercy, and the fatherless find a Father."
        },
        "4": {
            "L": "I will heal their backsliding, I will love them freely: for mine anger is turned away from him.",
            "M": "I will heal their waywardness; I will love them freely, for my anger has turned away from them.",
            "T": "I will cure them of their turning-away — their persistent faithlessness. I will love them freely, without condition, without price. My anger is over. It has turned and gone."
        },
        "5": {
            "L": "I will be as the dew unto Israel: he shall blossom as the lily, and cast forth his roots as Lebanon.",
            "M": "I will be like the dew to Israel; he will blossom like a lily and take root like the cedars of Lebanon.",
            "T": "I will come to Israel like the morning dew — bringing life where there was only dust.\nHe will burst into flower like the lily\nand drive his roots down deep as the cedars of Lebanon."
        },
        "6": {
            "L": "His shoots shall spread, and his beauty shall be as the olive tree, and his fragrance as Lebanon.",
            "M": "His branches will spread out; his beauty will be like the olive tree, and his fragrance like that of Lebanon.",
            "T": "His new branches will spread wide;\nhe will carry the beauty of the olive —\nand the whole air around him will carry the fragrance of Lebanon's forests."
        },
        "7": {
            "L": "They that dwell under his shadow shall return; they shall revive as the grain, and blossom as the vine: the scent thereof shall be as the wine of Lebanon.",
            "M": "Those who dwell in his shade will flourish again; they will thrive like grain and blossom like the vine; his fragrance will be like the wine of Lebanon.",
            "T": "All who shelter under his shade will come alive again —\ngrowing like grain in a good year,\nblooming like a flourishing vine.\nAnd the name of Israel will carry a fragrance\nlike the fine wine that comes from Lebanon's vineyards."
        },
        "8": {
            "L": "Ephraim shall say, What have I to do any more with idols? I have answered him, and I observe him: I am like a green cypress tree. From me is thy fruit found.",
            "M": "Ephraim will say, What do I have to do with idols any longer? I am the one who answers him and watches over him; I am like a flourishing cypress. Your fruit comes from me.",
            "T": "Then Ephraim will say at last: 'What do I want with idols anymore?'\nAnd Yahweh answers: 'I am the one who answers you; I am the one who has been watching over you all along.\nI am like an ever-green cypress —\nand every fruit you bear has always come from me.'"
        },
        "9": {
            "L": "Who is wise, and he shall understand these things? prudent, and he shall know them? for the ways of the LORD are right, and the just shall walk in them: but the transgressors shall fall therein.",
            "M": "Who is wise? Let him understand these things. Who is discerning? Let him know them. For the ways of the LORD are right, and the righteous walk in them, but transgressors stumble in them.",
            "T": "Whoever is wise — let him take these words to heart.\nWhoever has understanding — let him grasp what has been said here.\nYahweh's ways are straight and right:\nthe righteous walk in them and live,\nbut those who refuse to turn will stumble and fall in the very same path."
        }
    }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hosea')
        merge_tier(existing, HOSEA, tier_key)
        save(tier_dir, 'hosea', existing)
    print('Hosea 13–14 written.')

if __name__ == '__main__':
    main()
