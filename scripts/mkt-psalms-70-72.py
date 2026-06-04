"""
MKT Psalms chapters 70–72 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-70-72.py

=== Overview of this unit ===

Ps 70 (5 v) — "Make Haste, O God" — An urgent rescue cry, nearly identical to
    Ps 40:13–17. The psalm stands alone as a separate liturgical unit under the
    superscription לְהַזְכִּיר (lehazkir, "to bring to remembrance / for the memorial
    offering"), which connects it to the grain-offering ritual (Lev 2:2; 24:7).
    The brevity is its force: nothing but raw urgency. Two matching petitions —
    "make haste to deliver me" (v1) and "do not delay" (v5) — bracket three verses
    of imprecation (vv2–3) and intercession (v4). The "Aha! Aha!" (H1889 × 2) of v3
    is the mocking cry of enemies who savor the psalmist's downfall. v4 pivots to
    corporate praise: those who seek God are told to rejoice and declare "God is great."
    v5 closes with the psalmist's admission of poverty and need — "I am poor and
    needy" — the posture that makes the petition genuine. No Selah in this psalm.

Ps 71 (24 v) — "From Youth to Old Age; I Will Not Be Forsaken" — One of the few
    Psalms in the Hebrew MT with no superscription. The LXX assigns it to David and
    to the sons of Jonadab and those first taken captive, but the MT stands without
    attribution. Structurally it has deep roots in Ps 22, 31, 35, and 40 — there are
    verbal echoes across all four. The psalm is voiced by someone in old age (vv9, 18:
    "time of old age," "old and gray-haired") who looks back on a life of trust from
    the womb (v6) and forward in renewed hope (vv20–21). The theological centre:
    God has never abandoned this person from birth, and is being petitioned not to
    start now. Enemies use the old man's weakness as evidence of divine abandonment
    (vv10–11: "God has forsaken him — pursue him!"). The psalm refuses that verdict.
    It ends with a commitment to lifelong praise (vv14–16, 22–24) and a hope in
    resurrection-like revival (v20: "from the depths of the earth you will bring me
    up again"). The address "Holy One of Israel" (v22, H6918+H3478) is a title
    most associated with Isaiah; its appearance here is theologically rich. No Selah.

Ps 72 (20 v) — "The Ideal King; Doxology Closing Book II" — Superscription: "A
    Psalm of Solomon" (לִשְׁלֹמֹה). The Hebrew preposition לְ is ambiguous — could mean
    "of Solomon" (he wrote it) or "for Solomon" (written on his behalf, possibly by
    David in light of v20's colophon). All three tiers use "of Solomon" as the more
    natural reading; the header notes the alternative. Structurally: petition for the
    just king (vv1–4), cosmic duration of his reign (vv5–7), universal dominion
    (vv8–11), the king's care for the poor (vv12–14), prosperity and lasting fame
    (vv15–17), then the doxology of Book II (vv18–19), and finally the colophon (v20:
    "the prayers of David the son of Jesse are ended"). The whole psalm is in the
    jussive/optative mood — "may he…" — a royal prayer rather than description of a
    current reality. No earthly Solomonic reign fulfilled it; the vision is messianic
    in the broader sense. Key echoes: v17b ("all nations shall be blessed in him")
    deliberately invokes Gen 12:3; 22:18; 26:4 — the Abrahamic covenant blessing
    transferred to the royal son. The closing doxology (vv18–19) formally closes
    Book II (Ps 42–72); v20 is a collection colophon. No Selah.

=== Superscriptions ===

Convention (established PSA-1 through PSA-11): superscription text is merged into v1
of each psalm, separated from the verse body by a period or a blank line in T tier.

Ps 70: "To the chief Musician, A Psalm of David, to bring to remembrance" —
    לְהַזְכִּיר rendered "to bring to remembrance" in L/M; "for the memorial offering"
    is the cultic background (T keeps "to bring to remembrance" for readability).
Ps 71: No superscription in Hebrew MT. v1 begins directly with the prayer.
Ps 72: "A Psalm of Solomon" — לִשְׁלֹמֹה. "Of Solomon" in all tiers.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M. In T: "the LORD"
    or "LORD" as the line requires. Consistent with all prior Psalms scripts.
    Appears in Ps 70:1,5; Ps 72:18 (in the doxology).

H430 (אֱלֹהִים, Elohim): "God" in all tiers. These psalms are within the Elohistic
    Psalter (Ps 42–83), where Elohim predominates over Yahweh. Translation follows
    the MT naturally.

H136 (אֲדֹנָי, Adonai): "Lord" (single capital, not LORD) in all tiers.
    Ps 71:5 and 71:16 pair H136 (Adonai) with H3069 (YHWH written as Adonai, i.e.,
    the Tetragrammaton with Adonai vowels) → rendered "Lord GOD" in all tiers per
    the standard rendering of אֲדֹנָי יְהוִה (= Adonai YHWH).

H2617 (חֶסֶד, hesed): "steadfast love" in all tiers. MKT standard throughout
    the Psalms. Does not appear explicitly in Ps 70–72 tokens but shapes the
    covenantal trust assumed throughout Ps 71.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M. In T: contextually "life" (Ps 70:2 where
    "seek my life" is more natural), "soul" (Ps 71:10 where the stalking imagery
    requires it), "lives" (Ps 72:13–14 where saving lives is the point).

H5542 (סֶלָה, Selah): Does not appear in Psalms 70, 71, or 72. No Selah markers
    to include.

H1889 (הֶאָח, he'ach, "Aha!"): The mocking exclamation in Ps 70:3. Rendered "Aha!"
    (doubled) in L/M to preserve the emphatic repetition; T: "Aha! Aha!" similarly.

H6451 (Ps 72:16, פִּסַּת, pissat): Hapax or rare form — "an abundance/handful."
    Context: grain abundant even on mountaintops. Rendered "abundance of grain"
    (L), "be abundant" (M), and contextually in T.

H5104 (נָהָר, nahar, "the River") in Ps 72:8: The definite "the River" = the
    Euphrates, the traditional eastern boundary of the Promised Land (Gen 15:18;
    Deut 1:7). Rendered "the River" in L/M; T: "the Euphrates" for clarity.

H6728 (צִיִּי, tsiyyiy, "desert-dwellers/those of the wilderness") in Ps 72:9:
    Nomadic peoples of the desert regions. Rendered "those who dwell in the
    wilderness" in L; "desert peoples" in M/T.

לִשְׁלֹמֹה (Ps 72 superscription): "A Psalm of Solomon" in all tiers. The
    lamed-preposition could mean "for" (written in Solomon's honor by David,
    cf. v20) or "of" (Solomon as author). "Of Solomon" follows convention and
    the most natural reading; the textual ambiguity is noted here.

=== Aspect and tense notes ===

Ps 70 — The opening verbs are imperative/cohortative: "make haste" (H2363
    חוּשָׁה, imperative), "deliver me," "help me." The imprecations (vv2–3) use
    jussives: "let them be ashamed," "let them be turned." v4 is also jussive:
    "let them rejoice," "let God be magnified." v5 resumes the urgent imperative.
    The whole psalm is petitionary — no indicative of past rescue.

Ps 71 — The psalm mixes tenses richly: past perfects of completed trust ("I have
    leaned from the womb," v6; "you have taught me from my youth," v17), present
    imperfects of ongoing action ("I will praise," "I will sing," vv22–23), and
    future promises ("you will revive me again," v20; "you will bring me up," v20).
    The enemies' action in v10–11 is described in imperfect (ongoing threat).
    The psalm's structure enacts what it describes: remembered trust → present
    petition → renewed vow of praise.

Ps 72 — The jussive mood dominates: "may he judge," "let the mountains bring,"
    "may they fear," "let him have dominion." The verbs are wishes and prayers,
    not descriptions of present reality. vv12–14 shift to indicative (describing
    the kind of king who can be trusted): "for he delivers," "he has pity,"
    "he redeems." This shift from "may he" to "he does" grounds the prayer in
    the king's known character. The doxology (vv18–19) is indicative + imperative:
    "Blessed be the LORD" (indicative of praise) + "may the whole earth be filled"
    (jussive of intercession).

=== OT echo notes ===

Ps 70 — Near-verbatim repetition of Ps 40:13–17. The two psalms share the same
    prayer; the separate existence of Ps 70 as its own unit emphasizes that these
    words can stand alone as pure urgent petition, stripped of Ps 40's narrative
    context. The liturgical superscription (lehazkir) may have assigned it to a
    particular service of the grain offering.

Ps 71:3 — "Rock of refuge… rock and fortress" echoes Ps 18:2; 31:2–3;
    the fortress-rock metaphor for God is one of the Psalter's most recurring images.

Ps 71:6 — "You took me from my mother's womb" echoes Ps 22:9–10. Both psalms
    use the womb-origin of divine care to anchor a cry for rescue in adult crisis.

Ps 71:20 — "From the depths of the earth you will bring me up again" — the
    "depths of the earth" (תַּהֲלֻמּוֹת הָאָרֶץ = tehomot ha'aretz, depths of the
    deep/earth) anticipates the resurrection language of Ezek 37:12–13 and
    Dan 12:2. This is not yet explicit resurrection theology but the conceptual
    soil from which it grows.

Ps 71:22 — "Holy One of Israel" (קְדוֹשׁ יִשְׂרָאֵל) appears here in the Psalter
    but is most characteristic of Isaiah (25+ occurrences). Its use here by an
    individual psalmist reflects a common theological vocabulary that Isaiah later
    develops into a major divine title.

Ps 72:8 — "From sea to sea, from the River to the ends of the earth" —
    the boundaries of the Davidic/Messianic kingdom. Quoted and fulfilled in
    Zech 9:10 (the coming king whose dominion extends from sea to sea). The NT
    reads this as fulfilled in Christ's universal lordship.

Ps 72:17 — "May all nations be blessed in him" — a deliberate echo of the
    Abrahamic covenant: Gen 12:3 ("all families of the earth shall be blessed
    through you"), 22:18, 26:4. The royal psalm makes the Davidic king the
    channel of the Abrahamic blessing to the nations. Paul cites Gen 12:3 in
    Gal 3:8 as fulfilled in Christ; Ps 72:17 bridges that covenant to the king.
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
  # Psalm 70 — "Make Haste, O God": Urgent Rescue Petition
  # ============================================================
  "70": {
    "1": {
      "L": "To the chief Musician. A Psalm of David, to bring to remembrance. O God, make haste to deliver me; O LORD, make haste to help me!",
      "M": "To the director of music. A Psalm of David, to bring to remembrance. O God, hurry to deliver me! O LORD, make haste to help me!",
      "T": "To the choirmaster. A Psalm of David, to bring to remembrance.\nO God—hurry!\nDeliver me!\nLORD—come quickly!\nHelp me!"
    },
    "2": {
      "L": "Let them be ashamed and confounded who seek my soul; let them be turned backward and put to confusion who desire my hurt.",
      "M": "Let those who seek my life be put to shame and confusion; let those who delight in my harm be turned back and brought to dishonor.",
      "T": "Let those who are hunting my life be covered in shame and confusion.\nLet every one who delights in my destruction\nbe driven back in disgrace."
    },
    "3": {
      "L": "Let them be turned back because of their shame, who say, 'Aha, aha!'",
      "M": "Let them be turned back in their shame—those who say, 'Aha, aha!'",
      "T": "Let those who mock me—'Aha! Aha!'—\nbe sent reeling by the very shame they dish out."
    },
    "4": {
      "L": "Let all those who seek you rejoice and be glad in you; and let those who love your salvation say continually, 'Let God be magnified!'",
      "M": "But let all who seek you rejoice and be glad in you; let those who love your salvation say always, 'God is great!'",
      "T": "Let everyone who is looking for you\nburst out in joy and gladness.\nLet those who love your salvation keep saying it:\n'God is great!'"
    },
    "5": {
      "L": "But I am poor and needy; make haste to me, O God! You are my help and my deliverer; O LORD, do not delay.",
      "M": "But I am poor and needy; hurry to me, O God! You are my help and my deliverer; O LORD, do not tarry.",
      "T": "Here I am—poor, needy, desperate.\nO God—come quickly!\nYou are my help.\nYou are the one who delivers me.\nLORD—don't wait."
    }
  },

  # ============================================================
  # Psalm 71 — "From Youth to Old Age; Do Not Forsake Me"
  # (No superscription in Hebrew MT)
  # ============================================================
  "71": {
    "1": {
      "L": "In thee, O LORD, do I take refuge; let me never be put to confusion.",
      "M": "In you, O LORD, I take refuge; let me never be put to shame.",
      "T": "LORD, you are the place I run to.\nLet me never be shamed."
    },
    "2": {
      "L": "In your righteousness deliver me and cause me to escape; incline your ear to me and save me.",
      "M": "In your righteousness deliver me and rescue me; incline your ear to me and save me.",
      "T": "Deliver me by your righteousness.\nBring me to safety.\nBend your ear toward me—save me."
    },
    "3": {
      "L": "Be to me a rock of refuge, to which I may continually come; you have given the command to save me, for you are my rock and my fortress.",
      "M": "Be for me a sheltering rock, a place I can always come to; you have commanded my salvation, for you are my rock and my fortress.",
      "T": "Be the rock I can always run back to.\nYou have already issued the order to save me.\nYou are my rock.\nYou are my fortress."
    },
    "4": {
      "L": "Rescue me, O my God, from the hand of the wicked, from the grasp of the unrighteous and cruel man.",
      "M": "Rescue me, O my God, from the hand of the wicked, from the grip of the unjust and cruel.",
      "T": "God—pull me out of the wicked man's grip,\nout of the clutches of those who are unjust and violent."
    },
    "5": {
      "L": "For you are my hope, O Lord GOD; you are my trust from my youth.",
      "M": "For you, O Lord GOD, are my hope, my trust from my earliest years.",
      "T": "Lord GOD—you are the hope I have always had.\nFrom my youth I have trusted no one but you."
    },
    "6": {
      "L": "Upon you I have leaned from the womb; from my mother's belly you took me; my praise is continually of you.",
      "M": "I have depended on you from before I was born; you drew me safely out of my mother's womb. My praise is forever of you.",
      "T": "Before I was born I was already leaning on you.\nYou drew me out of my mother's womb.\nYou have been the subject of my praise every day since."
    },
    "7": {
      "L": "I have been as a wonder to many; you are my strong refuge.",
      "M": "I have been like an astonishing sign to many, but you are my strong shelter.",
      "T": "To many my life has seemed like a wonder—a sign that God does something with what looks like nothing.\nBut you are the strong refuge where I have always been safe."
    },
    "8": {
      "L": "Let my mouth be filled with your praise and with your honour all the day.",
      "M": "My mouth is full of your praise and your glory all the day long.",
      "T": "My mouth is completely full of your praise.\nAll day long—your glory."
    },
    "9": {
      "L": "Do not cast me off in the time of old age; forsake me not when my strength fails.",
      "M": "Do not reject me when old age comes; do not abandon me when my strength gives out.",
      "T": "Don't throw me away when I am old.\nDon't leave me when my strength runs dry."
    },
    "10": {
      "L": "For mine enemies speak against me; they that lay wait for my soul take counsel together.",
      "M": "For my enemies speak about me; those who watch for my life conspire together.",
      "T": "My enemies are talking about me right now.\nThose who are stalking me have put their heads together."
    },
    "11": {
      "L": "Saying, 'God has forsaken him; pursue and seize him, for there is none to deliver.'",
      "M": "They say, 'God has abandoned him; run him down and take him, for there is no one to rescue him.'",
      "T": "'God has left him behind,' they say.\n'Chase him down. Take him.\nNo one is coming to save him.'"
    },
    "12": {
      "L": "O God, be not far from me; O my God, make haste to help me.",
      "M": "O God, do not be far from me; O my God, come quickly to my aid.",
      "T": "God—don't be far away.\nGod—hurry to help!"
    },
    "13": {
      "L": "Let them be confounded and consumed who are adversaries to my soul; let them be covered with reproach and dishonour who seek my hurt.",
      "M": "Let those who attack my life be put to shame and consumed; let those who seek my harm be wrapped in reproach and dishonor.",
      "T": "Let my accusers be exposed and destroyed.\nWrap them in shame—\nlet scorn and disgrace be the only clothes they have."
    },
    "14": {
      "L": "But I will hope continually and will add to all your praise.",
      "M": "But I will hope continually and will praise you more and more.",
      "T": "I choose to keep hoping—without stopping.\nAnd I will keep adding to the praise I give you."
    },
    "15": {
      "L": "My mouth shall tell of your righteousness and your salvation all the day; for I know not the numbers thereof.",
      "M": "My mouth will proclaim your righteousness and your saving acts all the day long, for I cannot count their number.",
      "T": "All day long my mouth will be telling it—\nyour righteousness, your saving acts.\nThere are more of them than I can count."
    },
    "16": {
      "L": "I will go in the strength of the Lord GOD; I will make mention of your righteousness, even of yours only.",
      "M": "I will come in the strength of the Lord GOD; I will declare your righteousness—yours and no one else's.",
      "T": "I will come in the might of the Lord GOD.\nI will speak of your righteousness—and yours alone."
    },
    "17": {
      "L": "O God, you have taught me from my youth; and hitherto have I declared your wondrous works.",
      "M": "O God, you have taught me from my youth, and to this day I am still declaring your wonderful deeds.",
      "T": "God—you have been teaching me since I was young.\nAnd all these years I have been telling people what you do."
    },
    "18": {
      "L": "Now also when I am old and grayheaded, O God, forsake me not until I have declared your strength to this generation, your power to every one that is to come.",
      "M": "And even now in old age, with gray hair, O God, do not forsake me until I have proclaimed your strength to this generation and your power to all who are yet to come.",
      "T": "Even now—old, my hair turning gray—don't leave me yet, God.\nLet me live long enough\nto tell this generation what kind of strength you have,\nto show every generation still to come what your power looks like."
    },
    "19": {
      "L": "Your righteousness also, O God, is very high; you who have done great things, O God—who is like you?",
      "M": "Your righteousness, O God, reaches the high heavens; you who have done such great things, O God—who is like you?",
      "T": "Your righteousness, O God, towers into the sky.\nYou have done great things.\nWho is like you?"
    },
    "20": {
      "L": "You who have shown me great and sore troubles shall quicken me again; and shall bring me up again from the depths of the earth.",
      "M": "You who have made me experience many bitter troubles will revive me again; from the depths of the earth you will bring me up once more.",
      "T": "You are the one who showed me every one of those troubles.\nBut you will bring me back to life.\nFrom the very depths you will lift me up again."
    },
    "21": {
      "L": "You shall increase my greatness and comfort me on every side.",
      "M": "You will increase my honor and surround me with comfort.",
      "T": "You will restore what I have lost—more than before.\nYou will surround me with comfort on every side."
    },
    "22": {
      "L": "I will also praise you with the psaltery, even your truth, O my God; I will sing praises to you with the harp, O Holy One of Israel.",
      "M": "I will praise you with the lyre for your faithfulness, O my God; I will sing to you with the harp, O Holy One of Israel.",
      "T": "I will take up the lyre and praise you, my God—your faithfulness deserves it.\nI will sing to you with the harp,\nyou Holy One of Israel."
    },
    "23": {
      "L": "My lips shall greatly rejoice when I sing unto you; and my soul, which you have redeemed.",
      "M": "My lips will shout for joy when I sing praises to you; and my soul, which you have redeemed, will also rejoice.",
      "T": "When I sing to you—\nmy lips will burst open with joy.\nMy whole redeemed self will be rejoicing too."
    },
    "24": {
      "L": "My tongue also shall talk of your righteousness all the day long; for they are confounded, for they are brought to shame, that seek to do me hurt.",
      "M": "And my tongue will speak of your righteous deeds all day long, for those who sought to harm me have been put to shame and humiliated.",
      "T": "My tongue will keep talking about your righteousness—all day long.\nBecause those who wanted to harm me?\nThey are the ones who ended up ashamed."
    }
  },

  # ============================================================
  # Psalm 72 — "The Ideal King"; Doxology Closing Book II
  # ============================================================
  "72": {
    "1": {
      "L": "A Psalm of Solomon. Give the king your justice, O God, and your righteousness to the royal son.",
      "M": "A Psalm of Solomon. O God, give the king your justice, and your righteousness to the king's son.",
      "T": "A Psalm of Solomon.\nGod—give the king your own sense of justice.\nGive the royal son your righteousness."
    },
    "2": {
      "L": "He shall judge your people with righteousness and your poor with just judgment.",
      "M": "May he judge your people with righteousness and your poor with justice.",
      "T": "May he govern your people rightly,\nand bring real justice to the poor."
    },
    "3": {
      "L": "The mountains shall bring peace to the people, and the little hills by righteousness.",
      "M": "May the mountains bring peace to the people, and the hills, through righteousness.",
      "T": "May the mountains themselves carry peace down to the people.\nMay every hill overflow with it—through righteousness."
    },
    "4": {
      "L": "He shall judge the poor of the people; he shall save the children of the needy and shall break in pieces the oppressor.",
      "M": "May he defend the cause of the poor of the people, give deliverance to the children of the needy, and crush the oppressor.",
      "T": "May he take up the case of the poor.\nMay he deliver the children of those who have nothing.\nMay he crush whoever crushes them."
    },
    "5": {
      "L": "They shall fear you as long as the sun and moon endure, throughout all generations.",
      "M": "May they fear you as long as the sun and moon endure, through all generations.",
      "T": "May the fear of you last as long as the sun and moon—\nthrough every generation, without end."
    },
    "6": {
      "L": "He shall come down like rain upon the mown grass, like showers that water the earth.",
      "M": "May he be like rain falling on newly mown grass, like showers that water the earth.",
      "T": "May his reign come down like rain on fresh-cut grass,\nlike showers soaking into dry ground."
    },
    "7": {
      "L": "In his days shall the righteous flourish; and abundance of peace, until the moon is no more.",
      "M": "In his days may the righteous flourish, and peace abound, until the moon is no more.",
      "T": "May the righteous thrive in his day.\nMay peace multiply and overflow—\nuntil there is no moon left to watch it."
    },
    "8": {
      "L": "He shall have dominion also from sea to sea, and from the River to the ends of the earth.",
      "M": "May he have dominion from sea to sea, from the River to the ends of the earth.",
      "T": "Let his rule stretch from sea to sea,\nfrom the Euphrates to the farthest edge of the world."
    },
    "9": {
      "L": "They that dwell in the wilderness shall bow before him; and his enemies shall lick the dust.",
      "M": "May desert peoples bow before him, and his enemies lick the dust.",
      "T": "May even the desert peoples kneel before him.\nMay his enemies eat dust."
    },
    "10": {
      "L": "The kings of Tarshish and of the isles shall bring presents; the kings of Sheba and Seba shall offer gifts.",
      "M": "May the kings of Tarshish and the coastlands bring tribute; may the kings of Sheba and Seba offer gifts.",
      "T": "Let the kings of Tarshish and the far coastlands bring tribute.\nLet the kings of Sheba and Seba lay their gifts at his feet."
    },
    "11": {
      "L": "Yea, all kings shall fall down before him; all nations shall serve him.",
      "M": "Yes, may all kings bow down before him; may all nations serve him.",
      "T": "Every king—bowing before him.\nEvery nation—his to serve."
    },
    "12": {
      "L": "For he shall deliver the needy when he cries; the poor also, and him that hath no helper.",
      "M": "For he delivers the needy when they cry for help, the poor and those who have no one to help them.",
      "T": "He rescues the poor when they cry out.\nHe reaches for the destitute—\nthe ones nobody else comes to help."
    },
    "13": {
      "L": "He shall spare the poor and needy, and shall save the souls of the needy.",
      "M": "He has compassion on the weak and the needy, and saves the lives of the poor.",
      "T": "He looks on the helpless with tenderness.\nHe saves the lives of those who have nothing."
    },
    "14": {
      "L": "He shall redeem their soul from deceit and violence, and precious shall their blood be in his sight.",
      "M": "He redeems their life from oppression and violence, and their blood is precious in his eyes.",
      "T": "He redeems their lives from extortion and brutality.\nIn his eyes their blood is not cheap."
    },
    "15": {
      "L": "And he shall live, and to him shall be given of the gold of Sheba; and prayer shall be made for him continually; and daily shall he be praised.",
      "M": "Long may he live! May gold from Sheba be given to him! May prayer be made for him continually and blessings pronounced for him all day long.",
      "T": "May he live long!\nMay Sheba's gold be laid before him!\nMay people pray for him every day, all day,\nand speak his praises without stopping."
    },
    "16": {
      "L": "There shall be an abundance of grain in the earth upon the top of the mountains; its fruit shall shake like Lebanon, and they of the city shall flourish like grass of the earth.",
      "M": "May grain be abundant throughout the land; may it wave on the mountaintops; may its yield be like Lebanon, and may the people of the cities flourish like the grass of the fields.",
      "T": "May grain grow in such abundance\nthat even the mountaintops are full of it, waving in the wind.\nMay the harvest be as rich as Lebanon's cedar forests.\nMay city-dwellers bloom like grass after rain."
    },
    "17": {
      "L": "His name shall endure for ever; his name shall continue as long as the sun: and men shall be blessed in him; all nations shall call him blessed.",
      "M": "May his name endure forever; may it continue as long as the sun endures! May all peoples find blessing through him, and all nations call him blessed.",
      "T": "May his name last forever—\ncontinuing as long as the sun exists.\nMay all peoples find their blessing in him,\nand every nation call him blessed—\nthis is the promise made to Abraham, now placed on the royal son."
    },
    "18": {
      "L": "Blessed be the LORD God, the God of Israel, who only doeth wondrous things.",
      "M": "Blessed be the LORD, the God of Israel, who alone does wondrous things.",
      "T": "Blessed be the LORD, Israel's God—\nthe one who alone does wonders."
    },
    "19": {
      "L": "And blessed be his glorious name for ever; and let the whole earth be filled with his glory. Amen and Amen.",
      "M": "Blessed be his glorious name forever; may the whole earth be filled with his glory! Amen and Amen.",
      "T": "Blessed be his glorious name forever.\nMay the whole earth be filled with his glory.\nAmen.\nAmen."
    },
    "20": {
      "L": "The prayers of David the son of Jesse are ended.",
      "M": "The prayers of David, the son of Jesse, are ended.",
      "T": "Here end the prayers of David son of Jesse."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 70–72 written.')

if __name__ == '__main__':
    main()
