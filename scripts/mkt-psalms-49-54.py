"""
MKT Psalms chapters 49–54 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-49-54.py

=== Overview of this unit ===

Ps 49 (20 v) — Wisdom psalm of the Sons of Korah. Universal address: rich and poor,
    high and low, all peoples — the teacher opens a dark saying (chidah, H2420) and a
    parable (mashal, H4912). The theme: wealth cannot buy life. No one can ransom
    another from death (vv7–9). Wise and fool alike die and leave their wealth behind
    (v10). The refrain appears at v12 and v20 with a crucial variation: v12 says man
    in honor "does not endure" (yālin, H3885 — does not lodge even overnight); v20
    adds "and does not understand" — ignorance of one's mortality is the deepest folly.
    The theological pivot is v15: God will ransom my soul from Sheol's power — a
    confidence unavailable to the wealthy who trust in themselves.

Ps 50 (23 v) — Psalm of Asaph. A divine courtroom scene. Three divine names stack in
    v1: El–Elohim–YHWH ("The Mighty One, God, the LORD") — ancient theophanic
    language. God summons heaven and earth as witnesses, gathers his covenant people
    (hasidim, H2623), and brings two charges: (1) against the "faithful" who have
    misunderstood sacrifice as feeding God (vv8–15); (2) against the wicked who recite
    the covenant while practicing deceit (vv16–21). The resolution: thanksgiving
    (todah, H8426) is the true sacrifice; ordered living is the path to God's salvation.

Ps 51 (19 v) — David's great penitential psalm. Historical anchor: Nathan's confrontation
    after Bathsheba (2 Sam 12). Three Hebrew sin-terms are stacked in v1–3:
    pesha (H6588, willful rebellion), avon (H5771, twisted guilt/iniquity), chattat
    (H2403, missing the mark). The three purification verbs: blot out (H4229), wash
    (H3526 — laundry-level scrubbing), cleanse (H2891). Four occurrences of ruach
    (H7307, spirit) in vv10–12,17: "right spirit" / "Holy Spirit" (God's own, v11 —
    the one place in Psalms where the Spirit is explicitly God's Holy Spirit) / "willing
    spirit" / "broken spirit." Bara (H1254, create, v10) is the Genesis 1:1 word —
    reserved in Hebrew for divine creation from nothing; David is asking for new creation.
    Vv18–19 are likely a later exilic addition applying David's penitence to the
    community's need for Jerusalem's restoration; translated faithfully within the psalm.

Ps 52 (9 v) — David against Doeg the Edomite (1 Sam 21–22). Doeg reported David's
    visit to Ahimelech to Saul, leading to the slaughter of the priests of Nob. The
    psalm's frame: chesed (H2617, steadfast love) in v1 ("God's steadfast love endures")
    and v8 ("I trust in God's steadfast love forever") — Doeg's power is brief; God's
    covenant loyalty is permanent. The wicked man's weapon is his tongue (vv2–4);
    God's response is total destruction (v5). Counter-image: the psalmist is a green
    olive tree (H2132, zayit, v8) rooted in God's house — alive, bearing fruit.

Ps 53 (6 v) — Nearly identical to Psalm 14, with Elohim substituted for YHWH throughout
    (the Elohistic Psalter characteristic of Ps 42–89). The "fool" (naval, H5036) is
    not a dunce but a moral bankrupt — one who lives as if there is no God to answer to.
    Naval denotes practical atheism, not intellectual skepticism. The key difference
    from Ps 14 is v5, which describes God scattering the bones of Israel's enemies —
    more militarily specific than Ps 14's parallel.

Ps 54 (7 v) — Brief lament-petition of David when the Ziphites betrayed his location
    to Saul (1 Sam 23:19–20). Notable: ezer (H5826, helper) in v4 — the same word used
    of Eve as the "helper suitable for" Adam (Gen 2:18). God as helper is the deepest
    OT assurance in crisis. The psalm moves from danger (v3) through confidence (v4) to
    vow (v6) and testimony in advance (v7) — a compressed lament-to-praise arc.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M throughout. In T: "the LORD."
    Consistent with all prior Psalms scripts.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Psalms 49–54 fall in the Elohistic Psalter
    (Ps 42–89), which predominantly uses Elohim. Preserved naturally as "God."

H410 (אֵל, El) in Ps 50:1: "Mighty One" — first of three stacked divine names:
    El–Elohim–YHWH. Rendered "The Mighty One, God, the LORD" to reflect the theophanic
    accumulation. Not flattened to one name.

H7585 (שְׁאוֹל, Sheol): "Sheol" in all tiers (L/M/T). Not "grave" (flattens meaning —
    Sheol is the realm of the dead, not just a burial site) and not "hell" (anachronistic
    NT coloring). The Hebrew proper noun is preserved throughout.

H6299 (פָּדָה, padah): "ransom/redeem" — Ps 49:7,15. The exodus-covenant term for
    deliverance by substitutionary payment. In v7: no human can ransom another; in v15:
    God will ransom the psalmist. The contrast is theologically load-bearing.

H5315 (נֶפֶשׁ, nefesh): "soul" — Ps 49:8,15,18; 54:3,4. The embodied self, not a Greek
    immaterial soul. "Soul" maintains the psalmic register; "life" or "self" used in T
    where clarity requires it.

H2617 (חֶסֶד, chesed): "steadfast love" — Ps 50:5 (implied in "hasidim"); 51:1; 52:1,8.
    Covenant loyalty + active kindness. "Lovingkindness" is archaic; "mercy" loses the
    loyalty dimension. Consistent with all prior Psalms scripts.

H7307 (רוּחַ, ruach) in Ps 51 — four occurrences:
    v10: "right spirit" (spirit of uprightness/steadiness)
    v11: "Holy Spirit" (capitalized — God's own Spirit, the one explicitly named here;
         cf. Isa 63:10–11; this is the single instance in Psalms of "your holy Spirit")
    v12: "willing spirit" (nedib spirit — generosity, readiness, freedom)
    v17: "broken spirit" (human ruach crushed by guilt)
    In L: "spirit" throughout; M/T distinguish by context.

H1254 (בָּרָא, bara, Ps 51:10): "create" — the Genesis 1:1 verb, used only of divine
    action from nothing. Not "make" or "form." David's request is for new creation of
    the heart — nothing less will do.

H5036 (נָבָל, naval, Ps 53:1): "fool" — moral bankruptcy, not stupidity. The naval
    is one who lives as if there is no God — practical atheism expressed in lifestyle.
    Same word used of Nabal in 1 Sam 25.

H7356 (רַחֲמִים, rachamim, Ps 51:1): "tender mercies / compassion" — plural of rechem
    (womb). The image is of womb-tenderness, motherly compassion. In L: "tender mercies";
    M: "great compassion"; T: "womb-tenderness" (unpacked).

H1285 (בְּרִית, covenant, Ps 50:5): "covenant" — the formal oath-bound relationship.
    Those who made a covenant "by sacrifice" are the hasidim, the faithful ones.

H2623 (חָסִיד, hasid, Ps 50:5): "faithful ones / godly ones" — those characterized by
    chesed, the covenant-loyal people. In L: "faithful ones"; M/T: "faithful people."

H8426 (תּוֹדָה, todah, Ps 50:14; 54:6): "thanksgiving / thank-offering" — both the
    internal attitude and the formal sacrifice of gratitude. In Ps 50 it is the true
    sacrifice God desires; in Ps 54 it motivates the psalmist's freewill offering.

H5826 (עֵזֶר, ezer, Ps 54:4): "helper" — same word as Gen 2:18 (Eve as the "helper
    suitable for" Adam). In Ps 54 it describes God's role in David's crisis. Rendered
    "helper" in all tiers; the Genesis echo is noted in T.

=== Ps 49:12 / 49:20 — refrain variation ===

The refrain appears twice: v12 "Man in his splendor will not endure; he is like the
beasts that perish" and v20 "Man in his splendor, yet without understanding, is like the
beasts that perish." The addition of "without understanding" (H995, bin) in v20 is the
psalm's sharpening close: the problem is not merely mortality but failure to reckon
with it. The T tier surfaces this escalation.

=== Ps 50:23 — todah as sacrifice ===

"Whoever offers thanksgiving (todah) as sacrifice glorifies me" — the prophetic critique
of sacrifice without relationship reaches its peak here. The liturgical sacrifice of
gratitude is not the abolition of ritual but its proper heart. Consistent with Ps 51's
parallel move ("sacrifices of God are a broken spirit").

=== Ps 51:18–19 — exilic addition note ===

These verses (rebuild Jerusalem's walls / then burnt offerings will be accepted) shift
from singular confession to communal prayer. Likely added by an exilic editor who saw
the entire psalm as applicable to Israel's corporate guilt and need for restoration.
Translated faithfully; the postexilic application is noted in the T tier.

=== Aspect and tense notes ===

Ps 49 — Wisdom-discourse style: gnomic imperfects and participles for timeless truths
    (vv6–14). The pivot in v15 uses a perfect of confident certainty: "God will ransom"
    (expressed as a completed act in Hebrew — certainty of future).
Ps 50 — Divine speech in vv7–15,16–23 uses first-person imperfects (ongoing divine
    stance). The courtroom summons in vv1–4 uses perfects of completed divine action.
Ps 51 — Petitionary imperfects throughout. v10 imperative (bara): direct creation-command
    addressed to God. v13 uses a consequential perfect ("then I will teach").
Ps 52 — The accusation in vv2–4 uses participles (characterizing the tongue's ongoing
    work). The divine response in v5 uses perfects of confident future (God will act).
Ps 53 — Gnomic perfects for universal moral observation (vv1–3). v5 is eschatological.
Ps 54 — Petition imperfects (vv1–2); affirmative perfects in v7 (testimony in advance).

=== OT echo notes ===

Ps 49:15 — "God will ransom my soul from the power of Sheol, for he will receive me"
    (laqach, H3947, receive/take). The same verb used of Enoch in Gen 5:24 ("God took
    him") and Elijah in 2 Kgs 2:3. The T tier marks this resonance.
Ps 50:1 — El–Elohim–YHWH: the stacking of divine names recalls Deut 6:4 (YHWH our
    Elohim, YHWH is one) and Joshua 22:22 (El Elohim YHWH, El Elohim YHWH).
Ps 51:7 — Hyssop (H231, ezov): the purification plant of Lev 14 (cleansing of lepers)
    and Num 19 (cleansing from corpse impurity). David uses the highest available
    purification ritual image. Also: hyssop was used at the Passover (Exod 12:22).
Ps 53:6 — "When God restores the fortunes (shevut, H7622) of his people" — this phrase
    appears throughout Jeremiah and Ezekiel as the promise of post-exile restoration.
    Its presence in Ps 53 is one marker of later editing/application.
Ps 54:4 — ezer (helper): Gen 2:18 echo noted above.
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


PSALMS = {

  # ============================================================
  # Psalm 49 — The Wisdom of Mortality: Wealth Cannot Buy Life
  # ============================================================
  "49": {
    "1": {
      "L": "To the chief Musician. For the Sons of Korah. A Psalm. Hear this, all peoples! Give ear, all inhabitants of the world,",
      "M": "To the director of music. Of the Sons of Korah. A Psalm. Hear this, all peoples! Listen, all who live in the world—",
      "T": "To the choirmaster. Of the Sons of Korah. A Psalm.\nHear this—all nations, all peoples!\nEvery soul alive in this world: listen."
    },
    "2": {
      "L": "both low and high, rich and poor together.",
      "M": "the humble and the great alike, the rich and the poor together.",
      "T": "The nobodies and the powerful.\nThe destitute and the wealthy.\nAll of you."
    },
    "3": {
      "L": "My mouth shall speak wisdom, and the meditation of my heart shall be understanding.",
      "M": "My mouth will speak wisdom, and the reflection of my heart will be understanding.",
      "T": "What comes from my mouth will be wisdom.\nWhat rises from my heart will be understanding."
    },
    "4": {
      "L": "I will incline my ear to a proverb; I will open my dark saying upon the harp.",
      "M": "I bend my ear to a proverb; I will open my riddle with the harp.",
      "T": "I lean my ear toward a parable—a dark riddle—\nand open its meaning with the harp."
    },
    "5": {
      "L": "Why should I fear in days of evil, when the iniquity of those who would trip me surrounds me?",
      "M": "Why should I be afraid in evil days, when the guilt of my accusers closes in around me?",
      "T": "Why should I be afraid when evil days come,\nwhen enemies who would trip me up press in on every side?"
    },
    "6": {
      "L": "Those who trust in their wealth and boast in the multitude of their riches—",
      "M": "those who trust in their wealth and boast of their great riches—",
      "T": "What can people who boast in their money do to me?\nThose who crow about the size of their fortune?"
    },
    "7": {
      "L": "truly, not one of them can redeem another, nor give to God a ransom for him—",
      "M": "truly no one can ransom another person, or give God a payment for their life—",
      "T": "Not one of them can ransom even their closest friend.\nNo one can buy a substitute before God—"
    },
    "8": {
      "L": "for the ransom of their soul is too precious, and it must cease forever—",
      "M": "for the price of their life is too high; the payment would never be enough—",
      "T": "the price of a life is so far beyond reach\nit can never be paid. Not ever."
    },
    "9": {
      "L": "that he should live on forever and never see the Pit.",
      "M": "no sum could keep him alive forever, safe from seeing Sheol.",
      "T": "No price can buy a person immortality\nor keep them from going down to Sheol."
    },
    "10": {
      "L": "For he sees that wise men die; the fool and the brutish alike perish and leave their wealth to others.",
      "M": "He sees that even the wise die—the fool and the senseless alike perish and leave their wealth behind for others.",
      "T": "Look around—the wise die.\nThe fool and the dull-witted—all the same, all of them\nleaving their wealth behind for strangers."
    },
    "11": {
      "L": "Their inward thought is that their houses are forever, their dwelling places to all generations; they called their lands after their own names.",
      "M": "In their hearts they imagined their homes would last forever, their estates from generation to generation; they stamped their own names on their lands.",
      "T": "Deep down they believed it: 'My house will stand forever;\nmy estate will go on for every generation.'\nSo they put their name on the land.\nBut the land has outlasted them all."
    },
    "12": {
      "L": "But man in his splendor will not endure; he is like the beasts that perish.",
      "M": "Man in all his honor will not last; he is like the animals that die.",
      "T": "Honor doesn't last.\nHuman splendor doesn't last.\nA person in all their glory—\nis no different from a beast that perishes."
    },
    "13": {
      "L": "This is the way of those who trust in themselves, and the end of those who are pleased with their own words. Selah",
      "M": "This is the fate of those who are confident in themselves, and after them people applaud their talk. Selah",
      "T": "This is where self-trust leads.\nAnd still—generation after generation comes along and admires them,\nclapping for the same foolishness.\nSelah."
    },
    "14": {
      "L": "Like sheep they are destined for Sheol; Death shall be their shepherd; and the upright shall rule over them in the morning. Their form shall waste away in Sheol, away from their great dwelling.",
      "M": "Like sheep they are headed for Sheol; Death will be their shepherd, and the upright will have dominion over them in the morning. Their bodies will decay in Sheol, with no home left for them.",
      "T": "They are sheep—and Sheol is where they are headed.\nDeath itself is their shepherd now.\nBut the upright will have the last word when morning comes—\nwhen the new day dawns, dominion belongs to them.\nAs for the rich: their form rots in Sheol,\nfar from every great house they built."
    },
    "15": {
      "L": "But God will ransom my soul from the power of Sheol, for he will receive me. Selah",
      "M": "But God will ransom my life from the grip of Sheol, for he will take me to himself. Selah",
      "T": "But God—God will ransom me.\nHe will reach into Sheol and take me.\n[The verb 'receive/take' — laqach — is the word used of Enoch: 'God took him' (Gen 5:24). Of Elijah (2 Kgs 2:3). The psalmist plants himself in that tradition.]\nSelah."
    },
    "16": {
      "L": "Do not be afraid when a man grows rich, when the glory of his house increases,",
      "M": "Do not be frightened when someone becomes rich, when the splendor of their household grows—",
      "T": "Don't let it unsettle you when someone gets rich,\nwhen their household swells into an empire."
    },
    "17": {
      "L": "for when he dies he will carry nothing away; his glory will not descend after him.",
      "M": "for when they die they take nothing with them; their glory will not follow them down.",
      "T": "They take nothing when they die—\nnot a coin, not an inch of reputation.\nNone of it follows them down."
    },
    "18": {
      "L": "Though in his lifetime he counts himself blessed—and men will praise you when you do well for yourself—",
      "M": "Though in their lifetime they counted themselves fortunate—and people praised them for prospering—",
      "T": "They congratulated themselves their whole life.\n'You've done well!'—everyone said so.\nPeople always praise the prosperous."
    },
    "19": {
      "L": "they shall go to the generation of their fathers; they will never again see the light.",
      "M": "but they will go to join their ancestors and never again see the light.",
      "T": "But they go down to join their ancestors in the dark.\nThey will never see light again."
    },
    "20": {
      "L": "Man in his splendor, yet without understanding, is like the beasts that perish.",
      "M": "Man in all his honor, but without understanding, is like the animals that die.",
      "T": "Human splendor without wisdom—\nall the wealth and honor in the world\nwithout understanding that this is where it ends—\nis no different from an animal that perishes."
    }
  },

  # ============================================================
  # Psalm 50 — Asaph: The Divine Court; True Worship
  # ============================================================
  "50": {
    "1": {
      "L": "A Psalm of Asaph. The Mighty God, God, the LORD, has spoken and summoned the earth from the rising of the sun to its setting.",
      "M": "A Psalm of Asaph. The Mighty One, God, the LORD, speaks and summons the earth from east to west.",
      "T": "A Psalm of Asaph.\nThe Mighty One—God—the LORD—has spoken.\nHe summons the whole earth,\nfrom the place the sun rises to where it sets."
    },
    "2": {
      "L": "Out of Zion, the perfection of beauty, God shines forth.",
      "M": "Out of Zion, perfect in beauty, God blazes out.",
      "T": "From Zion—beautiful, perfect Zion—\nGod blazes forth."
    },
    "3": {
      "L": "Our God shall come and shall not keep silence; before him is a devouring fire, and around him a mighty tempest.",
      "M": "Our God comes and will not stay silent; fire devours before him, and a fierce storm rages around him.",
      "T": "Our God comes—he does not come quietly.\nFire tears a path ahead of him;\na raging storm swirls all around him."
    },
    "4": {
      "L": "He calls to the heavens above and to the earth, that he may judge his people:",
      "M": "He calls out to the heavens above and to the earth, to judge his people:",
      "T": "He calls heaven and earth as witnesses.\nHe is bringing his people to court."
    },
    "5": {
      "L": "'Gather to me my faithful ones, who made a covenant with me by sacrifice.'",
      "M": "'Bring together my faithful people, those who sealed covenant with me by sacrifice.'",
      "T": "'Bring my faithful people before me—\nthe ones who bound themselves to me with sacrifice.'"
    },
    "6": {
      "L": "And the heavens declare his righteousness, for God himself is judge. Selah",
      "M": "The heavens declare his righteousness, for God himself is the judge. Selah",
      "T": "The heavens themselves declare his righteousness.\nGod is the judge here—no one else.\nSelah."
    },
    "7": {
      "L": "'Hear, O my people, and I will speak; O Israel, and I will testify against you. I am God, your God.'",
      "M": "'Listen, my people, and I will speak; I will testify against you, O Israel. I am God, your God.'",
      "T": "'Listen, my people—I have something to say.\nIsrael—I am bringing my case against you.\nI am God. Your God.'"
    },
    "8": {
      "L": "'Not for your sacrifices do I rebuke you; your burnt offerings are before me continually.'",
      "M": "'My rebuke is not over your sacrifices; your burnt offerings are always before me.'",
      "T": "'I am not calling you to account over your sacrifices—\nyou have been bringing burnt offerings faithfully enough.'"
    },
    "9": {
      "L": "'I will not take a bull from your house, or he-goats from your folds.'",
      "M": "'I do not need a bull from your household or goats from your pens.'",
      "T": "'I don't want a bull from your barns\nor a goat from your flocks.'"
    },
    "10": {
      "L": "'For every beast of the forest is mine, the cattle on a thousand hills.'",
      "M": "'Every animal of the forest is mine—the cattle on a thousand hills.'",
      "T": "'Every animal in the forest already belongs to me.\nThe cattle on a thousand hills—mine.'"
    },
    "11": {
      "L": "'I know all the birds of the mountains, and everything that moves in the field is mine.'",
      "M": "'I know every bird in the hills; everything that moves in the open fields is mine.'",
      "T": "'I know every bird that nests in the mountains.\nEverything that stirs in the open field—mine.'"
    },
    "12": {
      "L": "'If I were hungry, I would not tell you, for the world and its fullness are mine.'",
      "M": "'If I were hungry, I would not come to you—the world and everything in it is mine.'",
      "T": "'If I were hungry—which I am not—I would not come to you.\nThe world is mine. Everything in it.'"
    },
    "13": {
      "L": "'Do I eat the flesh of bulls, or drink the blood of goats?'",
      "M": "'Do I eat bull meat? Do I drink the blood of goats?'",
      "T": "'Do you think I eat bull meat?\nThat I drink the blood of goats?'"
    },
    "14": {
      "L": "'Offer to God a sacrifice of thanksgiving, and fulfill your vows to the Most High.'",
      "M": "'Bring God a thank-offering as your sacrifice, and keep your vows to the Most High.'",
      "T": "'What I want is your thanksgiving—offered as sacrifice.\nKeep the vows you made to the Most High.'"
    },
    "15": {
      "L": "'And call upon me in the day of trouble; I will deliver you, and you shall glorify me.'",
      "M": "'Call on me when trouble comes; I will rescue you, and you will honor me.'",
      "T": "'When trouble comes—call out to me.\nI will deliver you.\nAnd that deliverance will be your praise.'"
    },
    "16": {
      "L": "But to the wicked God says: 'What right have you to recite my statutes, or to take my covenant on your lips?'",
      "M": "But to the wicked, God says: 'What right do you have to quote my laws, or to take my covenant on your lips?'",
      "T": "But to the wicked, God says this:\n'What business do you have reciting my laws?\nHow dare you take my covenant on your lips?'"
    },
    "17": {
      "L": "'For you hate discipline, and you have thrown my words behind you.'",
      "M": "'You despise correction and fling my words aside.'",
      "T": "'You hate being corrected.\nYou toss my words over your shoulder.'"
    },
    "18": {
      "L": "'When you see a thief, you join with him, and you share with adulterers.'",
      "M": "'When you see a thief you go along with him, and you make yourself at home with adulterers.'",
      "T": "'You see a thief and fall right in with him.\nYou are comfortable with adulterers.'"
    },
    "19": {
      "L": "'You give your mouth to evil, and your tongue frames deceit.'",
      "M": "'You let your mouth run loose into evil, and your tongue is busy weaving lies.'",
      "T": "'Your mouth runs loose—straight into evil.\nYour tongue is a craftsman of deception.'"
    },
    "20": {
      "L": "'You sit and speak against your brother; you slander your own mother's son.'",
      "M": "'You sit and talk against your own brother; you slander your mother's son.'",
      "T": "'You sit there tearing your own brother apart.\nYou slander the son of your mother's womb.'"
    },
    "21": {
      "L": "'These things you have done, and I kept silent; you thought that I was one altogether like yourself. But now I will rebuke you and lay the charge before your face.'",
      "M": "'You did all these things, and I said nothing. You concluded I must be just like you. But now I rebuke you and lay everything out before your eyes.'",
      "T": "'You did all this, and I kept quiet.\nYou took my silence as approval—\nassumed I was made of the same stuff as you.\n\nBut now I am speaking.\nNow I set the charge down before you, point by point.'"
    },
    "22": {
      "L": "'Now consider this, you who forget God, lest I tear you apart, and there be none to deliver.'",
      "M": "'Take this seriously, you who have forgotten God, or I will tear you apart, and no one will rescue you.'",
      "T": "'Think carefully, you who have forgotten God—\nbefore I tear you apart\nand there is no one left to save you.'"
    },
    "23": {
      "L": "'The one who offers a sacrifice of thanksgiving glorifies me; and to the one who orders his way rightly I will show the salvation of God.'",
      "M": "'Whoever brings thanksgiving as their sacrifice glorifies me; to the one who walks a right path I will show the salvation of God.'",
      "T": "'The person who brings me thanksgiving—that person honors me.\nThe one who lays out a right way of living before me—\nI will show that person the rescue that only God can give.'"
    }
  },

  # ============================================================
  # Psalm 51 — David's Penitential Psalm: Create in Me a Clean Heart
  # ============================================================
  "51": {
    "1": {
      "L": "To the chief Musician. A Psalm of David, when Nathan the prophet came to him, after he had gone in to Bathsheba. Have mercy upon me, O God, according to your steadfast love; according to the abundance of your tender mercies, blot out my transgressions.",
      "M": "To the director of music. A Psalm of David, when the prophet Nathan came to him after David had slept with Bathsheba. Have mercy on me, O God, in keeping with your steadfast love; in your great compassion, blot out my transgressions.",
      "T": "To the choirmaster. Of David. After Nathan the prophet came to him—after what happened with Bathsheba.\nGod—have mercy on me.\nIn your steadfast love—your relentless, covenantal love—have mercy.\nIn your great compassion—your womb-tenderness—\nwipe away everything I have done wrong."
    },
    "2": {
      "L": "Wash me thoroughly from my iniquity, and cleanse me from my sin.",
      "M": "Scrub away my guilt completely, and purify me from my sin.",
      "T": "Scrub me—work the stain all the way out.\nCleanse me from my sin."
    },
    "3": {
      "L": "For I acknowledge my transgressions, and my sin is ever before me.",
      "M": "For I know my rebellions, and my sin is before me at every moment.",
      "T": "I know what I have done.\nMy sin is there—in front of me—every waking moment."
    },
    "4": {
      "L": "Against you, you only, have I sinned and done what is evil in your sight, so that you are justified when you speak and blameless when you judge.",
      "M": "Against you—you alone—have I sinned and done what is evil in your sight, so that you are proved right when you speak and blameless when you judge.",
      "T": "Against you—and only you—have I sinned.\nWhat I did was evil in your sight—I know it.\nAnd because of that, whatever judgment you pronounce is right.\nYou are blameless in all of it."
    },
    "5": {
      "L": "Behold, in iniquity I was brought forth, and in sin my mother conceived me.",
      "M": "Surely I was brought forth into guilt, and in sin my mother conceived me.",
      "T": "I was born into this.\nIniquity was there at my beginning—\nsin was present at the moment of conception.\nI am not making excuses—I am naming the depth of the problem."
    },
    "6": {
      "L": "Behold, you desire truth in the inward parts; in the hidden place you teach me wisdom.",
      "M": "You desire truth deep inside a person; in the hidden place you are teaching me wisdom.",
      "T": "What you want is truth all the way down—\nin the parts no one else can see.\nAnd in that hidden depth, you are teaching me what wisdom actually is."
    },
    "7": {
      "L": "Purge me with hyssop, and I shall be clean; wash me, and I shall be whiter than snow.",
      "M": "Cleanse me with hyssop, and I will be clean; wash me, and I will be whiter than snow.",
      "T": "Take the hyssop—the purification branch of Leviticus and the Passover—and cleanse me.\nAnd I will be clean.\nWash me, and I will be whiter than snow."
    },
    "8": {
      "L": "Let me hear joy and gladness; let the bones which you have crushed rejoice.",
      "M": "Let me hear the sounds of joy and gladness; let the bones you have crushed be glad.",
      "T": "Let me hear joy again—let me hear gladness.\nThese bones you have broken—\nlet even them rejoice."
    },
    "9": {
      "L": "Hide your face from my sins, and blot out all my iniquities.",
      "M": "Look away from my sins; wipe out all my guilt.",
      "T": "Turn your face from my sins.\nBlot out every last piece of my guilt."
    },
    "10": {
      "L": "Create in me a clean heart, O God, and renew a right spirit within me.",
      "M": "Create a pure heart in me, O God, and renew a steadfast spirit within me.",
      "T": "Create in me a clean heart, God.\n[Bara — the Genesis 1 word for divine creation from nothing. Nothing less than new creation will fix what is wrong in me.]\nRenew a right spirit deep inside me."
    },
    "11": {
      "L": "Cast me not away from your presence, and take not your Holy Spirit from me.",
      "M": "Do not banish me from your presence; do not take your Holy Spirit from me.",
      "T": "Don't send me away from you.\nDon't take your Holy Spirit from me—\nthe Spirit that is yours, that is holy—\nthe one gift I cannot live without."
    },
    "12": {
      "L": "Restore to me the joy of your salvation, and uphold me with a willing spirit.",
      "M": "Give back to me the joy of your rescue, and sustain me with a generous, willing spirit.",
      "T": "Give me back the joy of being saved by you.\nGive me a spirit that is willing and open—\none that won't drag me back into this."
    },
    "13": {
      "L": "Then I will teach transgressors your ways, and sinners will return to you.",
      "M": "Then I will show other rebels your ways, and sinners will come back to you.",
      "T": "Then—only then—I will be able to show other rebels the way back.\nAnd sinners will actually turn and come home to you."
    },
    "14": {
      "L": "Deliver me from bloodguiltiness, O God, O God of my salvation, and my tongue shall sing aloud of your righteousness.",
      "M": "Rescue me from the guilt of bloodshed, O God—God of my salvation—and my tongue will ring out your righteousness.",
      "T": "Free me from the blood on my hands, God—\nGod, the God who saves me.\nThen my tongue will break into song\nabout your righteousness—how right you are in all of this."
    },
    "15": {
      "L": "O Lord, open my lips, and my mouth shall show forth your praise.",
      "M": "O Lord, open my lips, and my mouth will declare your praise.",
      "T": "Lord—open my lips.\nI cannot even praise you properly right now.\nYou have to open the door yourself.\nThen my mouth will declare your praise."
    },
    "16": {
      "L": "For you desire not sacrifice, or I would give it; you take no pleasure in burnt offering.",
      "M": "You do not want sacrifice—otherwise I would bring it; you take no delight in burnt offerings.",
      "T": "You don't actually want animal sacrifices—\nif you did, I would bring them by the cartload.\nBurnt offerings don't move you."
    },
    "17": {
      "L": "The sacrifices of God are a broken spirit; a broken and contrite heart, O God, you will not despise.",
      "M": "What God wants as sacrifice is a broken spirit; a broken and crushed heart, O God, you will not reject.",
      "T": "What you want is a broken spirit—\nthat is the sacrifice.\nA heart shattered by the weight of what it has done.\nA crushed and contrite heart, God—\nyou will never turn that away."
    },
    "18": {
      "L": "Do good to Zion in your good pleasure; build up the walls of Jerusalem.",
      "M": "In your favor, do good to Zion; build up the walls of Jerusalem.",
      "T": "Be good to Zion, LORD—in your grace and goodwill.\nBuild Jerusalem's walls.\n[These final verses likely carry the community's prayer—David's penitence applied to the city's need, shaped by exile and the longing for restoration.]"
    },
    "19": {
      "L": "Then you will delight in righteous sacrifices, in burnt offerings and whole burnt offerings; then bulls will be offered on your altar.",
      "M": "Then you will be pleased with right sacrifices, with burnt offerings and whole offerings; then bulls will go up on your altar.",
      "T": "Then—and only then—will the sacrifices mean something.\nThe burnt offerings, the whole offerings—they will be real.\nBulls will go up on your altar, and it will matter,\nbecause the heart behind them will be right."
    }
  },

  # ============================================================
  # Psalm 52 — Maschil of David: Doeg and the Enduring Olive Tree
  # ============================================================
  "52": {
    "1": {
      "L": "To the chief Musician. Maschil of David. When Doeg the Edomite came and told Saul, and said to him, 'David has come to the house of Ahimelech.' Why do you boast of evil, O mighty man? The steadfast love of God endures all the day.",
      "M": "To the director of music. A Maskil of David. When Doeg the Edomite came and told Saul: 'David has gone to the house of Ahimelech.' Why do you boast of evil, O powerful man? The steadfast love of God holds all the day.",
      "T": "To the choirmaster. A Maskil of David. When Doeg the Edomite went to Saul and reported: 'David has come to the house of Ahimelech.'\nO strong man—why boast about the evil you have done?\nDoeg's power lasts a day.\nGod's steadfast love holds every day."
    },
    "2": {
      "L": "Your tongue plots destruction, like a sharp razor, working deceitfully.",
      "M": "Your tongue plots harm, sharp as a razor blade—you craftsman of deceit.",
      "T": "Your tongue is a blade—\nsharp, well-honed—\nand you work it to cut and destroy."
    },
    "3": {
      "L": "You love evil more than good, and lying more than speaking righteousness. Selah",
      "M": "You love evil rather than good, and lies rather than truth. Selah",
      "T": "You prefer evil to goodness.\nYou prefer the lie to what is true.\nSelah."
    },
    "4": {
      "L": "You love all words that devour, O deceitful tongue.",
      "M": "You love every word that destroys, you treacherous tongue.",
      "T": "Every word you love is a word that tears down.\nYou deceitful thing."
    },
    "5": {
      "L": "But God will break you down forever; he will snatch and tear you from your tent; he will uproot you from the land of the living. Selah",
      "M": "But God will pull you down permanently; he will grab and rip you from your home; he will tear you out of the land of the living. Selah",
      "T": "But God will unmake you—completely, permanently.\nHe will snatch you right out of your comfortable life.\nHe will pull you up by the root\nfrom the land of the living.\nSelah."
    },
    "6": {
      "L": "The righteous shall see and fear, and shall laugh at him:",
      "M": "The righteous will see and be filled with awe, and they will laugh:",
      "T": "The righteous will watch what happens.\nThey will be struck with awe—\nand then they will laugh:"
    },
    "7": {
      "L": "'Here is the man who did not make God his refuge, but trusted in the abundance of his riches, and made himself strong in his mischief.'",
      "M": "'Here is the man who would not take refuge in God, but relied on his great wealth and found his strength in destruction.'",
      "T": "'Look at this man—\nhe would not make God his hiding place.\nHe trusted in money—mountains of it.\nHe made his home in his own capacity for harm.'"
    },
    "8": {
      "L": "But I am like a green olive tree in the house of God; I trust in the steadfast love of God forever and ever.",
      "M": "But I am like a flourishing olive tree in the house of God; I trust in God's steadfast love forever and ever.",
      "T": "But me—I am a green olive tree, rooted in God's house.\nAlive. Bearing fruit.\nI trust in his steadfast love—\nnot for a season. Forever."
    },
    "9": {
      "L": "I will praise you forever, because you have done it; and I will wait for your name, for it is good, in the presence of your faithful ones.",
      "M": "I will give you thanks forever, because of what you have done; I will hope in your name, for it is good, before your faithful people.",
      "T": "I will praise you forever—because of what you have done.\nI will anchor my hope in your name.\nYour name is good.\nAnd I will do it all before your faithful people,\nyour gathered saints."
    }
  },

  # ============================================================
  # Psalm 53 — Maschil of David: The Fool's Practical Atheism
  # ============================================================
  "53": {
    "1": {
      "L": "To the chief Musician upon Mahalath. Maschil of David. The fool has said in his heart, 'There is no God.' They are corrupt and have done abominable iniquity; there is none who does good.",
      "M": "To the director of music. On Mahalath. A Maskil of David. The fool has said in his heart, 'There is no God.' They are corrupt and have done vile deeds; not one of them does good.",
      "T": "To the choirmaster. On Mahalath. A Maskil of David.\nThe fool—the moral bankrupt—says in his heart: 'There is no God.'\nNot a philosopher's conclusion; a lived conviction.\nHe lives as if there is no God to answer to.\nThey are corrupt. They do abominable things.\nNot one does what is good."
    },
    "2": {
      "L": "God has looked down from heaven upon the children of men to see if there are any who understand, who seek after God.",
      "M": "God looked down from heaven on all humanity to see if anyone understands, if anyone seeks after God.",
      "T": "God looked down from heaven—\nscanned across all of humanity—\nto find anyone who actually understands,\nanyone genuinely seeking him."
    },
    "3": {
      "L": "Every one of them has turned back; they have together become corrupt; there is none who does good, not even one.",
      "M": "Every single one has turned aside; together they have become rotten; there is no one who does good—not a single person.",
      "T": "Every one—turned away.\nAll of them together, rotted through.\nNot one who does what is good.\nNot one."
    },
    "4": {
      "L": "Have those who work iniquity no knowledge, who eat up my people as they eat bread and do not call upon God?",
      "M": "Don't those who work evil know anything—those who devour my people the way they eat bread and never call on God?",
      "T": "Are these people completely without understanding—\nthose who consume my people like a meal,\nwho never once call out to God?"
    },
    "5": {
      "L": "There they were in great dread where no dread was, for God has scattered the bones of him who encamps against you; you have put them to shame, because God has rejected them.",
      "M": "But there they are, overwhelmed with terror where there was no terror, for God scattered the bones of those who attacked you; you put them to shame, for God has rejected them.",
      "T": "Watch what happens:\nthere they are—seized by terror they never saw coming,\nin a place they thought was safe.\nGod scatters the bones of the armies that moved against his people.\nGod shames them.\nGod has rejected them."
    },
    "6": {
      "L": "Oh, that the salvation of Israel would come from Zion! When God restores the fortunes of his people, let Jacob rejoice and Israel be glad.",
      "M": "Oh, that Israel's rescue would come out of Zion! When God restores the fortunes of his people, Jacob will rejoice and Israel will be glad.",
      "T": "Oh—if only the rescue of Israel would come out of Zion!\nWhen God brings his people back from captivity—\nlet Jacob erupt in joy,\nlet Israel burst into gladness."
    }
  },

  # ============================================================
  # Psalm 54 — Maschil of David: Save Me by Your Name
  # ============================================================
  "54": {
    "1": {
      "L": "To the chief Musician on Neginoth. Maschil of David. When the Ziphites came and said to Saul, 'Is not David hiding himself among us?' O God, save me by your name, and vindicate me by your might.",
      "M": "To the director of music. With stringed instruments. A Maskil of David. When the Ziphites came to Saul and said, 'Is not David hiding among us?' O God, save me by your name; vindicate me by your strength.",
      "T": "To the choirmaster. With stringed instruments. A Maskil of David. When the Ziphites came to Saul and said: 'Isn't David hiding here among us?'\nGod—save me.\nBy your name—your very character and reputation—save me.\nBy your power, make my case."
    },
    "2": {
      "L": "Hear my prayer, O God; give ear to the words of my mouth.",
      "M": "Hear my prayer, O God; listen to what I am saying.",
      "T": "Hear my prayer, God.\nListen to what I am saying."
    },
    "3": {
      "L": "For strangers have risen against me, and ruthless men seek my life; they have not set God before them. Selah",
      "M": "For outsiders are threatening me; violent men are hunting my life—people who have no thought of God. Selah",
      "T": "People who owe me nothing have turned against me.\nBrutal, ruthless men—hunting my life.\nGod is nowhere in their thinking.\nSelah."
    },
    "4": {
      "L": "Behold, God is my helper; the Lord is the upholder of my life.",
      "M": "But God is my helper; the Lord is the one who sustains my life.",
      "T": "But here is what I know:\nGod is my helper—my ezer.\n[The same word as Eden: 'a helper suitable for him.' God himself takes that role.]\nThe Lord is the one holding my life up."
    },
    "5": {
      "L": "He will return evil upon my enemies; in your faithfulness, put an end to them.",
      "M": "He will bring the evil back on my enemies; in your faithfulness, silence them.",
      "T": "He will turn the harm back on those who would harm me.\nIn your faithfulness, LORD—silence them."
    },
    "6": {
      "L": "With a freewill offering I will sacrifice to you; I will praise your name, O LORD, for it is good.",
      "M": "With a generous, willing heart I will offer sacrifice to you; I will give thanks to your name, LORD, for it is good.",
      "T": "I will bring you an offering—freely, gladly, from an open hand.\nI will give praise to your name, LORD.\nYour name is good."
    },
    "7": {
      "L": "For he has delivered me from all trouble, and my eye has looked upon my enemies.",
      "M": "For he has rescued me from every distress, and my eye has seen the downfall of my enemies.",
      "T": "He has rescued me from everything that threatened to undo me.\nAnd my own eyes have seen my enemies undone."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 49–54 written.')

if __name__ == '__main__':
    main()
