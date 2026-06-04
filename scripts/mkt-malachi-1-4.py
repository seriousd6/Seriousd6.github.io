"""
MKT Malachi chapters 1–4 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-malachi-1-4.py

=== BOOK OVERVIEW ===

Malachi is the last voice of Hebrew prophecy — and the last book of the OT canon
in Protestant ordering. Its four chapters are structured as six disputations (rîb
pattern): Yahweh makes a charge, the people or priests challenge it ("How? / When?
/ Wherein?"), and Yahweh answers with evidence. This confrontational form is
intentional: it dramatizes Israel's inability to see its own condition.

The book targets two audiences simultaneously: the priests (chs 1–2) and the whole
people (chs 2:17–4:6). Its accusations — polluted offerings, faithless marriages,
withheld tithes, cynical speech — are not abstract; they are the visible symptoms
of a community that has drifted from covenantal loyalty while maintaining religious
form. The final two verses (4:5–6) serve as the capstone of the entire OT: Elijah
is coming before the great day of the LORD, and with him the possibility of
intergenerational reconciliation — or else utter destruction.

The name "Malachi" (H4401) means "my messenger" — the same word (malʾāk) used in
3:1 for the forerunner and for the messenger of the covenant. The author's identity
is woven into the book's central theme.

=== TEXTUAL NOTES ===

- 1:11: One of the most striking verses in the Minor Prophets — Yahweh's name is
  great among the Gentiles and pure offerings are being made across the whole earth.
  The tense is disputed (present or future). The T tier takes it as a present
  reality that shames Israel's current practice.

- 2:15: Textually difficult. The MT "And not one has done so who has a remnant of
  spirit" is obscure. Most modern translations follow the sense: God made husband
  and wife one flesh, holding back the divine spirit for this purpose, seeking
  godly offspring. The T tier follows this reading.

- 2:16: "I hate divorce" (or "he hates divorce") — the Hebrew is 3ms + infinitive
  construct (śānēʾ śallēaḥ), lit. "hating, sending away." Most modern translations
  follow LXX and make Yahweh the subject: "I hate divorce." This is the reading
  adopted throughout all three tiers.

- 3:1: The verse has three figures: (1) "my messenger" (the forerunner = Elijah of
  4:5, = John the Baptist per Mark 1:2 / Matt 11:10); (2) "the Lord" (hāʾādôn) who
  comes to his temple; (3) "the messenger of the covenant" (likely the same as the
  Lord). The T tier makes the NT identification explicit.

- 3:6: "For I am the LORD, I change not" — the theological hinge of the entire book.
  The permanence of God's character is simultaneously the ground of judgment and
  the ground of mercy.

- 4:2: "Sun of righteousness" — the only occurrence of this phrase in the OT.
  Whether it is a title or a metaphor, the image of a sun rising with healing in
  its wings is one of the most vivid eschatological promises in the prophets. The
  wings (kānāp) may echo the wings of the cherubim over the ark or the image of
  God as a bird sheltering his own.

- 4:5–6: These verses serve as the closing appendix of the whole Hebrew prophetic
  corpus. The Elijah promise is cited in Matthew 11:14 (Jesus: "he is the Elijah
  who was to come"), Luke 1:17 (the angel's description of John the Baptist), and
  Mark 9:12–13. The final word of the Hebrew OT (H2764, ḥērem, "curse/ban") is
  stark: the alternative to the forerunner's work is total destruction.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention) throughout.
  T: "Yahweh" in divine speech, oracle closings, and climactic declarations;
     "the LORD" in narrative transitions and reported speech. Consistent with
     Zechariah, Haggai, and all prior Minor Prophets in this series.

- H6635 (צְבָאוֹת / tseba'ot, hosts):
  L/M: "of hosts" (standard).
  T: "of Armies" — consistent with the prior Minor Prophet scripts.

- H430 (אֱלֹהִים / Elohim):
  "God" throughout all tiers.

- H136 (אֲדֹנָי / Adonai):
  1:14 "the Lord" (Adonai, not Yahweh); 3:1 "the Lord" (hāʾādôn) — distinct
  from H3068 (Yahweh). Rendered "the Lord" (lowercase) to distinguish from LORD.

- H1285 (בְּרִית / bĕrît, covenant):
  "covenant" throughout all three tiers. The Levitical covenant (2:4–8) and the
  marriage covenant (2:14) are distinct applications of the same term.

- H4397 (מַלְאָך / malʾāk, messenger/angel):
  2:7: "messenger" (the priest as messenger of the LORD) — lowercase.
  3:1: "my messenger" (the forerunner, distinct from the Lord who comes);
       "messenger of the covenant" (the Lord himself, or identical with "the Lord").
  Lowercase throughout — the angelic/prophetic ambiguity is honored.

- H7307 (רוּחַ / ruach, spirit/Spirit):
  2:15: lowercase "spirit" — the creative breath/spirit of life present in the
  marriage union; not the Holy Spirit in a NT pneumatological sense, though
  theologically connected.
  2:16: lowercase "spirit" in the heed-your-spirit warning.

- H5459 (סְגֻלָּה / sĕgullāh, treasured possession):
  3:17: "special possession" (L), "treasured possession" (M/T) — the covenant
  term from Exodus 19:5, deliberately echoed here.

- H2764 (חֵרֶם / ḥērem, ban/curse):
  4:6: "utter destruction" (L/M); "the ban of total destruction" (T) — the
  herem, the most severe covenant sanction: devoted to destruction, as Jericho was.

- H5121 (Sun of Righteousness):
  4:2: H8121 (shemesh, sun) + H6666 (tsedaqah, righteousness) — rendered "Sun of
  Righteousness" with initial caps as a title/eschatological figure throughout all
  tiers.
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

MALACHI = {
  "1": {
    "1": {
      "L": "The burden of the word of the LORD to Israel by the hand of Malachi.",
      "M": "An oracle: the word of the LORD to Israel through Malachi.",
      "T": "The divine burden — Yahweh's word pressing down on Israel with prophetic weight — delivered through his messenger Malachi. His name means 'my messenger,' and he is exactly that: the last prophetic voice in the Hebrew canon before a silence of four centuries falls."
    },
    "2": {
      "L": "I have loved you, says the LORD. Yet you say, 'Wherein have you loved us?' Was not Esau Jacob's brother? declares the LORD. Yet I loved Jacob.",
      "M": "I have loved you, says the LORD. But you ask, 'How have you loved us?' Was not Esau Jacob's brother? declares the LORD. Yet I loved Jacob.",
      "T": "'I love you,' Yahweh says — and Israel's first response is to demand proof. 'How? What does that look like?' The answer is not sentiment but election: Esau and Jacob were brothers, twins from the same father, equally positioned for the covenant inheritance. Yahweh chose Jacob. The love is not feeling but covenantal commitment — free, unconditional, preceding all human merit."
    },
    "3": {
      "L": "But Esau I hated, and I laid his mountains waste and gave his heritage to the jackals of the wilderness.",
      "M": "But Esau I hated. I made his mountains a wasteland and gave his inheritance over to the jackals of the desert.",
      "T": "But Esau — Jacob's own twin — Yahweh set aside. His mountain strongholds became desolation; his proud heritage was surrendered to wild animals. This is not casual favoritism: it is the sovereign freedom of the God who owes nothing to either line, yet chose one. Paul reaches back to this passage in Romans 9 as the ground of divine election."
    },
    "4": {
      "L": "Though Edom says, 'We are beaten down, but we will return and rebuild the ruined places,' thus says the LORD of hosts: 'They shall build, but I will throw down; and they shall be called the territory of wickedness, and the people against whom the LORD has indignation forever.'",
      "M": "If Edom says, 'We have been devastated, but we will return and rebuild the ruins,' this is what the LORD of Hosts says: 'They may build, but I will demolish. They will be called the wicked country — the people against whom the LORD's anger burns forever.'",
      "T": "Edom refuses to accept its ruin. 'We will rebuild,' they announce. Yahweh of Armies answers: 'Go ahead. Whatever you build, I will pull down.' Edom will carry a permanent designation — land of wickedness, people under perpetual divine anger. Their arrogant resilience only confirms the verdict. The border of Esau was not merely historically destroyed; it stands under a continuing and irrevocable divine judgment."
    },
    "5": {
      "L": "And your eyes shall see it, and you shall say, 'The LORD is great beyond the border of Israel.'",
      "M": "Your own eyes will see it, and you will say, 'The LORD is great — even beyond the borders of Israel!'",
      "T": "Israel will witness Edom's fate with their own eyes, and the sight will force a confession: Yahweh's greatness is not confined within Israel's borders — it extends over every nation. The God who judged Edom is Lord of the whole earth, not merely the patron deity of one people."
    },
    "6": {
      "L": "A son honors his father, and a servant his master. If then I am a father, where is my honor? And if I am a master, where is my fear? says the LORD of hosts to you, O priests, who despise my name. But you say, 'How have we despised your name?'",
      "M": "A son honors his father, and a servant his master. If I am a father, where is my honor? If I am a master, where is my reverence? says the LORD of Hosts to you, O priests, who despise my name. But you say, 'How have we despised your name?'",
      "T": "The argument is elemental: a son respects his father; a servant respects his master — these are the basic patterns of every ordered society. Now apply it upward: Yahweh is Father to Israel, Master over his priests. But where is the honor? Where is the reverent fear? He names the accused directly: the priests. And before he can lay out the case, they interrupt with a challenge — 'When have we despised you?' Their inability to see their own offense is itself part of the offense."
    },
    "7": {
      "L": "In that you offer polluted bread upon mine altar. But you say, 'How have we polluted you?' In that you say, 'The table of the LORD is contemptible.'",
      "M": "By placing defiled food on my altar. But you ask, 'How have we defiled you?' By saying, 'The table of the LORD is contemptible.'",
      "T": "The evidence: the food laid on God's altar is polluted — ritually defiled offerings treated as acceptable. They protest: 'How?' Yahweh's answer is precise: by treating his table as something beneath contempt. The altar is not a burden to be discharged with leftovers — it is the table of the living God."
    },
    "8": {
      "L": "And when you offer the blind for sacrifice, is it not evil? And when you offer the lame and the sick, is it not evil? Offer it now to your governor; will he be pleased with you or show you favor? says the LORD of hosts.",
      "M": "When you offer blind animals as sacrifices, is that not wrong? And when you offer those that are lame or sick, is that not wrong? Try presenting such an animal to your governor — would he receive you? Would he show you any favor? says the LORD of Hosts.",
      "T": "The test is simple: would you give a blind, crippled, or diseased animal to your governor as a gift? Of course not — the insult would be obvious. Yet these are the offerings being laid on Yahweh's altar. If you would not dare dishonor a human official this way, what does it reveal that you dare dishonor the Lord of Armies?"
    },
    "9": {
      "L": "And now I pray you, beseech God that he will be gracious to us. With this kind of offering from your hand, will he accept your persons? says the LORD of hosts.",
      "M": "Now then, plead for God's favor — beg him to be gracious to us. This has come about through your doing. Will he show any of you favor? says the LORD of Hosts.",
      "T": "Go ahead: pray for God's grace, beg for his favor. But consider who is praying and with what in their hands. The priests who brought contemptible offerings are now asking for divine mercy. Will God overlook the offense? Will he look favorably on the very faces that despised him? Yahweh of Armies says: No."
    },
    "10": {
      "L": "Who is there even among you that would shut the doors, that you might not kindle fire on mine altar for nought? I have no pleasure in you, says the LORD of hosts, and I will not accept an offering from your hand.",
      "M": "Would that someone among you would shut the temple doors so that you could not kindle a useless fire on my altar! I take no pleasure in you, says the LORD of Hosts, and I will not accept any offering from your hand.",
      "T": "Yahweh of Armies makes a startling declaration: he would rather the temple doors were locked and the altar fires dead than receive one more polluted sacrifice. Worship that dishonors God is worse than no worship at all. He does not say this with indifference — he says it with active rejection. 'I take no pleasure in you. I will not accept what you bring.' The priests have turned the sanctuary into a theater of contempt."
    },
    "11": {
      "L": "For from the rising of the sun even to its going down my name is great among the Gentiles; and in every place incense is offered to my name, and a pure offering; for my name is great among the nations, says the LORD of hosts.",
      "M": "For from the rising of the sun to its setting, my name is great among the nations. In every place incense is offered to my name, and a pure offering. For my name is great among the nations, says the LORD of Hosts.",
      "T": "And here the horizon widens beyond Israel to the whole earth: from east to west, across every people and nation, Yahweh's name is great. Pure offerings are being made to him among the nations in ways Israel is not matching. This is one of the most surprising verses in the OT prophets: Gentile worship, unguided by Mosaic law, is seen as purer than what the priests at Jerusalem are bringing. What God rejects at his own altar, he is finding acceptable across the whole earth."
    },
    "12": {
      "L": "But you profane it in that you say, 'The table of the LORD is polluted, and the fruit thereof, even its meat, is contemptible.'",
      "M": "But you desecrate it by saying, 'The LORD's table is defiled, and its produce — the food — is contemptible.'",
      "T": "But they go right on doing it. In their casual attitudes, in their dismissive speech, in the way they treat the whole sacrificial system as a burden — they profane the table of the LORD. 'The table is polluted anyway. The food on it doesn't really matter.' This is what falls from the mouths of the men entrusted to represent the nation before God."
    },
    "13": {
      "L": "You also said, 'What a weariness this is!' and you have sniffed at it, says the LORD of hosts. And you brought that which was taken by violence, and the lame, and the sick; thus you brought the offering. Should I accept this of your hand? says the LORD.",
      "M": "You say, 'What a burden!' and you treat it with contempt, says the LORD of Hosts. You bring animals that are injured, lame, or sick and call that an offering! Should I accept it from you? says the LORD.",
      "T": "The mask slips. They say it openly: 'What a burden this is.' And they sniff at the whole business as something beneath them. Then they bring what was seized by force, the animal too lame to work, the one too sick to sell — and they lay it on the altar as though that counts. 'Should I accept this?' Yahweh says. The contempt is complete: they despise the worship while still performing it."
    },
    "14": {
      "L": "But cursed be the deceiver who has in his flock a male and vows it, and yet sacrifices to the LORD a blemished thing; for I am a great King, says the LORD of hosts, and my name is feared among the nations.",
      "M": "Cursed is the deceiver who has an acceptable male in his flock, vows it, but then sacrifices a blemished animal to the LORD. For I am a great King, says the LORD of Hosts, and my name is to be feared among the nations.",
      "T": "The sharpest condemnation: cursed is the man who has a perfect animal — who knows exactly what an acceptable sacrifice looks like — makes a solemn vow to bring it, and then substitutes a damaged one. That is not carelessness; it is calculated fraud against the King. Yahweh of Armies is not a minor local deity who can be cheated: he is the great King, and his name inspires awe across every nation. What Israel's priests dare offer him, they would not dare offer the governor — let alone the great King."
    }
  },
  "2": {
    "1": {
      "L": "And now, O ye priests, this commandment is for you.",
      "M": "Now this command is for you, O priests.",
      "T": "The first chapter indicted the priests' conduct. Now comes the formal charge — a commandment directed specifically at them, not at the people they serve."
    },
    "2": {
      "L": "If you will not hear, and if you will not lay it to heart, to give glory unto my name, says the LORD of hosts, I will even send a curse upon you, and I will curse your blessings; yea, I have cursed them already, because you do not lay it to heart.",
      "M": "If you do not listen and do not take it to heart to honor my name, says the LORD of Hosts, then I will send a curse on you and curse your blessings. Indeed, I have already cursed them, because you have not taken it to heart.",
      "T": "The condition is stated plainly: if they will not listen, if the word does not reach their hearts and move them to honor Yahweh's name — the curse falls. And more than that: the blessings themselves turn to curses. Every priestly benediction becomes the opposite when spoken by men who despise the one whose name they pronounce. In fact, Yahweh says, this has already happened — not a future warning but a present reality."
    },
    "3": {
      "L": "Behold, I will rebuke your seed and spread dung upon your faces, even the dung of your solemn feasts; and one shall take you away unto it.",
      "M": "Watch: I will rebuke your descendants, smear the dung of your festival offerings on your faces, and have you carried off along with it.",
      "T": "The punishment is deliberate and humiliating: the offal of the sacrifices they treated so casually will be smeared on their faces. This is the inversion of priestly honor — instead of faces lifted in the Aaronic blessing over Israel, faces covered in dung from the very offerings they corrupted. The priest's dignity, the priest's public role, the priest's authority: all undone. Carried off with the refuse."
    },
    "4": {
      "L": "And you shall know that I have sent this commandment unto you, that my covenant might be with Levi, says the LORD of hosts.",
      "M": "Then you will know that I have sent this command to you, so that my covenant with Levi may continue, says the LORD of Hosts.",
      "T": "The judgment's purpose is not destruction but preservation: Yahweh is acting precisely so that the covenant he made with the tribe of Levi does not collapse entirely. The Levitical covenant — life and peace in exchange for reverence and faithful teaching — is worth preserving. The priests' corruption is not only their personal failure; it threatens the covenant structure that holds Israel's worship together."
    },
    "5": {
      "L": "My covenant with him was of life and peace, and I gave them to him that he might fear; and he feared me, and was afraid before my name.",
      "M": "My covenant with him was life and peace, and I gave these to him; it called for reverence, and he revered me and stood in awe of my name.",
      "T": "This is what the Levitical covenant actually looked like when it functioned rightly: life and peace from God's side; genuine reverence from the priest's. He was afraid before Yahweh's name — not manufactured religious performance, but authentic awe. He knew what kind of God he served, and he conducted himself accordingly."
    },
    "6": {
      "L": "The law of truth was in his mouth, and iniquity was not found in his lips; he walked with me in peace and equity, and turned many away from iniquity.",
      "M": "True teaching was in his mouth, and no deceit was on his lips. He walked with me in peace and integrity and turned many people away from sin.",
      "T": "The ideal Levitical priest: his teaching was true, his lips were clean. He walked alongside Yahweh in a relationship of peace and moral integrity — and that life was fruitful. Many turned from iniquity because of him. He taught, he modeled, he led. This is the measure against which the current priests are being judged, and by which they fail on every count."
    },
    "7": {
      "L": "For the priest's lips should keep knowledge, and they should seek the law at his mouth; for he is the messenger of the LORD of hosts.",
      "M": "A priest's lips should preserve knowledge, and people should seek instruction from his mouth, for he is the messenger of the LORD of Hosts.",
      "T": "The priest's fundamental vocation: to carry and transmit the knowledge of God. The word 'messenger' (malʾāk) is the same root as Malachi's own name. The priest is a malʾāk — an emissary of Yahweh of Armies. The community has every right to come to him and receive instruction in the ways of God. That is precisely what he exists for. And precisely what the current priests have abandoned."
    },
    "8": {
      "L": "But you are departed out of the way; you have caused many to stumble at the law; you have corrupted the covenant of Levi, says the LORD of hosts.",
      "M": "But you have turned from the way, causing many to stumble through your instruction. You have corrupted the covenant of Levi, says the LORD of Hosts.",
      "T": "The indictment: they abandoned the way, and their teaching — which should have guided people toward God — caused them to stumble instead. Bad teaching is not merely failure; it is a weapon that harms those who receive it. And the consequence is the gravest possible: they have corrupted the very covenant Yahweh made with Levi. The priests entrusted to preserve the covenant have become its destroyers."
    },
    "9": {
      "L": "Therefore have I also made you contemptible and base before all the people, according as ye have not kept my ways, but have been partial in the law.",
      "M": "So I have also made you despised and humiliated before all the people, in proportion to the way you have not kept my ways and have shown partiality in applying the law.",
      "T": "The punishment fits the crime precisely: because they made themselves contemptible before God, he makes them contemptible before the people. The priests who showed favoritism in their rulings — bending the Torah for those with influence — have forfeited the authority that made them worth consulting. They sought respect while behaving without integrity; now they will have neither."
    },
    "10": {
      "L": "Have we not all one father? Has not one God created us? Why do we deal treacherously every man against his brother, by profaning the covenant of our fathers?",
      "M": "Do we not all have one father? Did not one God create us? Why then do we act faithlessly toward one another, violating the covenant of our ancestors?",
      "T": "The argument shifts from the priesthood to the whole people — and specifically to Israelite men divorcing their covenant wives for foreign women. The logic is theological: one Father, one Creator, one covenant family. If that is true, then faithlessness to a covenant wife is not merely a personal matter — it is covenant violation, a tearing of the fabric Yahweh wove around his people. The same God who created every Israelite is dishonored when they treat each other treacherously."
    },
    "11": {
      "L": "Judah hath dealt treacherously, and an abomination is committed in Israel and in Jerusalem; for Judah hath profaned the holiness of the LORD which he loved, and hath married the daughter of a strange god.",
      "M": "Judah has acted faithlessly, and a detestable thing has been done in Israel and in Jerusalem. Judah has desecrated the sanctuary the LORD loves by marrying the daughter of a foreign god.",
      "T": "The specific violation: Israelite men are marrying women devoted to foreign gods — daughters of other religious systems, women whose worship shapes the household. This is not cultural marriage; it is a theological act, a desecration. The 'holiness of the LORD which he loves' — the covenant people set apart for him — has been given away. An abomination is not merely something bad; it is something that violates the fundamental order of the covenant."
    },
    "12": {
      "L": "The LORD will cut off the man that doeth this, the master and the scholar, out of the tabernacles of Jacob, and him that offereth an offering unto the LORD of hosts.",
      "M": "May the LORD cut off from the tents of Jacob the man who does this — whether teacher or student — even if he still brings an offering to the LORD of Hosts.",
      "T": "The prayer of judgment: let Yahweh cut the offender off entirely from the covenant community — every man who does this, whether high or low, teacher or taught. And the addition is pointed: even if he still maintains the forms of worship, bringing his offering to the altar, it avails him nothing. The corruption of covenant loyalty cannot be covered by religious performance."
    },
    "13": {
      "L": "And this have you done again, covering the altar of the LORD with tears, with weeping, and with crying out, insomuch that he regardeth not the offering any more, or receiveth it with good will at your hand.",
      "M": "Here is another thing you do: you flood the LORD's altar with tears, weeping and wailing, because he no longer accepts your offerings with favor.",
      "T": "And there is a second offense layered on the first. They flood the altar with tears — genuine distress, audible weeping and groaning — because their offerings are being rejected. But the weeping is self-interested: they want the system to work for them while continuing to violate the covenant that gives it meaning. They grieve the consequences of their sin, not the sin itself. Yahweh is not moved."
    },
    "14": {
      "L": "Yet you say, 'Wherefore?' Because the LORD hath been witness between thee and the wife of thy youth, against whom thou hast dealt treacherously; yet is she thy companion, and the wife of thy covenant.",
      "M": "But you ask, 'Why?' Because the LORD is a witness between you and the wife of your youth, the wife you have been faithless to — your partner and your wife by covenant.",
      "T": "They still don't see it. 'Why won't God accept our worship?' Because Yahweh himself witnessed the marriage covenant they swore to the wife of their youth — and they have broken it. This woman who was their companion, their equal, their covenant partner — dismissed for a foreign woman. Marriage is not a contract between two parties; it is a covenant witnessed by God. And he does not forget what he witnessed."
    },
    "15": {
      "L": "And did not one God make her? Both flesh and spirit are his. And wherefore one? That he might seek a godly seed. Therefore take heed to your spirit, and let none deal treacherously against the wife of his youth.",
      "M": "Did he not make them one? He had a portion of the Spirit in view for this. And why one? Because he was seeking godly offspring. So watch your spirit, and do not be faithless to the wife of your youth.",
      "T": "The reason God made husband and wife one flesh is not accidental: he was pursuing something — godly offspring, children raised in covenant households. The spirit of life present in that union has a purpose. And because the stakes are this high — the formation of a generation that will know and fear God — there must be vigilance over one's own spirit, one's own inner disposition toward the one covenant partner. Do not betray her."
    },
    "16": {
      "L": "For the LORD, the God of Israel, saith that he hateth putting away; for one covereth violence with his garment, saith the LORD of hosts. Therefore take heed to your spirit, that ye deal not treacherously.",
      "M": "For the LORD God of Israel says, 'I hate divorce, because the man who divorces his wife covers his garment with violence,' says the LORD of Hosts. So guard yourselves in your spirit and do not act faithlessly.",
      "T": "'I hate divorce,' says Yahweh God of Israel — one of the plainest divine statements on marriage anywhere in Scripture. Divorce is not merely a social arrangement coming undone; it is an act of violence covered up, like blood soaked into a garment and hidden under a respectable exterior. The man who discards his covenant wife to pursue another woman is not free to worship as though nothing happened. His garment is stained. Guard the spirit, Yahweh warns them twice: the choices of the interior life determine the faithfulness of the covenant kept outwardly."
    },
    "17": {
      "L": "Ye have wearied the LORD with your words. Yet ye say, 'Wherein have we wearied him?' When ye say, 'Every one that doeth evil is good in the sight of the LORD, and he delighteth in them'; or, 'Where is the God of judgment?'",
      "M": "You have wearied the LORD with your words. But you ask, 'How have we wearied him?' By saying, 'Everyone who does evil is good in the LORD's sight, and he is pleased with them,' or by asking, 'Where is the God of justice?'",
      "T": "The final indictment of chapter 2: they have worn Yahweh out with their words — not their silence, but their actual speech. What are they saying? Two things equally damaging: first, that God approves of evildoers — that he has abandoned any moral distinction between good and evil. Second, the cynical complaint: 'Where is the God of justice?' They have inverted everything. They call evil good before God; then they demand why God doesn't act against evil. The contradiction is total, and Yahweh has heard enough."
    }
  },
  "3": {
    "1": {
      "L": "Behold, I will send my messenger, and he shall prepare the way before me; and the Lord, whom you seek, shall suddenly come to his temple, even the messenger of the covenant, whom you delight in; behold, he shall come, says the LORD of hosts.",
      "M": "Watch: I am sending my messenger to prepare the way before me. Then suddenly the Lord you are seeking will come to his temple — the messenger of the covenant in whom you delight. He is coming, says the LORD of Hosts.",
      "T": "The book's defining verse — and the verse that answers the cynical question of 2:17. Yahweh announces a forerunner: a messenger (malʾāk — the same word as Malachi's name) who prepares the road before him. Then the Lord himself suddenly arrives at his temple. This is the answer to 'Where is the God of justice?' He is coming. But coming is not the same as arriving comfortably. The messenger of the covenant — the one they claim to want — brings the refiner's fire. Mark 1:2 quotes this verse directly, applying it to John the Baptist as the forerunner of Jesus."
    },
    "2": {
      "L": "But who may abide the day of his coming? And who shall stand when he appeareth? For he is like a refiner's fire, and like fullers' soap.",
      "M": "But who can endure the day of his coming? Who can stand when he appears? For he is like a refiner's fire and like a launderer's soap.",
      "T": "The coming that was longed for is not comfortable. The question is not 'when is he coming?' but 'who can survive his arrival?' A refiner's fire burns off everything impure; fuller's soap scours away every stain. When the Lord comes, nothing unclean survives the process intact. The priests who wanted God to appear and vindicate them will find the fire has them in mind first."
    },
    "3": {
      "L": "And he shall sit as a refiner and purifier of silver; and he shall purify the sons of Levi, and purge them as gold and silver, that they may offer unto the LORD an offering in righteousness.",
      "M": "He will sit as a refiner and purifier of silver. He will purify the sons of Levi and refine them like gold and silver, until they present offerings to the LORD in righteousness.",
      "T": "The refinement is not destruction but restoration. He sits — patiently, deliberately — like a silversmith watching the crucible, who knows the metal is ready when he can see his own reflection in it. The sons of Levi are the first target of the refining, precisely because they are the ones entrusted to lead worship. When they come through the fire, they will offer what they could not offer before: righteousness. Not the corrupted sacrifices of chapter 1, but offerings made with integrity, by purified priests."
    },
    "4": {
      "L": "Then shall the offering of Judah and Jerusalem be pleasant unto the LORD, as in the days of old, and as in former years.",
      "M": "Then Judah's and Jerusalem's offerings will be pleasing to the LORD, as in days gone by, as in years long past.",
      "T": "The goal is not judgment but restoration. Once the priests are purified, the worship of the whole community recovers. Judah and Jerusalem bring offerings that actually please Yahweh — not because the ritual forms have changed, but because the hearts and integrity of those performing them have been transformed. The 'days of old' gestures toward the ideal moments of covenant faithfulness. That is where the refiner's fire aims to bring them."
    },
    "5": {
      "L": "And I will come near to you to judgment; and I will be a swift witness against the sorcerers, and against the adulterers, and against false swearers, and against those that oppress the hireling in his wages, the widow and the fatherless, and that turn aside the stranger from his right, and fear not me, says the LORD of hosts.",
      "M": "I will come near to you for judgment. I will be a swift witness against sorcerers, adulterers, those who swear falsely, those who cheat workers of their wages, and those who oppress widows, orphans, and foreigners — all of whom do not fear me, says the LORD of Hosts.",
      "T": "When the Lord comes to his temple, he comes as judge — and the docket is specific. He is a swift witness: immediate and certain accountability, not a slow or uncertain legal process. Sorcerers trafficking in forbidden powers. Adulterers breaking covenant with spouse and God simultaneously. False swearers invoking the divine name in service of lies. Employers cheating workers of earned wages. Those who trample widows, orphans, and immigrants — the traditional vulnerable classes whose protection marks a just society. The thread binding all these together: they do not fear God. Every violation on this list flows from that single root."
    },
    "6": {
      "L": "For I am the LORD, I change not; therefore ye sons of Jacob are not consumed.",
      "M": "For I the LORD do not change; and so you, descendants of Jacob, have not been destroyed.",
      "T": "This is the theological hinge of the entire book. Yahweh does not change. His character is constant. His covenant commitments do not expire. And because he does not change, Israel — despite every failure catalogued in these chapters — has not been consumed. The very constancy that makes him an unyielding judge is the same constancy that makes his covenant mercy permanent. They are not destroyed because the God they have disobeyed is still the God who bound himself to Jacob."
    },
    "7": {
      "L": "Even from the days of your fathers ye are gone away from mine ordinances, and have not kept them. Return unto me, and I will return unto you, says the LORD of hosts. But ye said, 'Wherein shall we return?'",
      "M": "From the days of your ancestors you have turned away from my statutes and have not kept them. Return to me, and I will return to you, says the LORD of Hosts. But you ask, 'How are we to return?'",
      "T": "The accusation spans generations: this is not a recent failure but a pattern stretching back to the ancestors. Yet the invitation is still open: 'Return to me, and I will return to you.' This is the covenant formula of restoration — the same formula used by Zechariah, Hosea, Joel, and Jeremiah before Malachi. God's call to return always precedes his restoration. But they have drifted so far that they cannot even recognize what returning would look like."
    },
    "8": {
      "L": "Will a man rob God? Yet ye have robbed me. But ye say, 'Wherein have we robbed thee?' In tithes and offerings.",
      "M": "Can a person rob God? Yet you are robbing me. You ask, 'How are we robbing you?' In tithes and contributions.",
      "T": "The question is almost absurd: can a creature rob its Creator? And yet the LORD says plainly: that is exactly what is happening. The tithe was not an optional charitable contribution — it was the designated portion belonging to God, set apart for the Levites and the poor. Withholding it is not merely stinginess; it is theft. Theft from God. The priests who served with contemptible offerings and the people who withheld their tithes are part of the same pattern: treating the claims of God as negotiable."
    },
    "9": {
      "L": "Ye are cursed with a curse; for ye have robbed me, even this whole nation.",
      "M": "You are under a curse — the whole nation of you — because you are robbing me.",
      "T": "The curse is collective: not this individual or that tribe, but the whole nation together. When the covenant obligations of worship and provision for the Levites and the poor are systematically violated, the whole community bears the consequences. The agricultural curse — drought, crop failure, scarcity — falls not on isolated offenders but on the land that belongs to a disobedient people."
    },
    "10": {
      "L": "Bring ye all the tithes into the storehouse, that there may be meat in mine house, and prove me now herewith, says the LORD of hosts, if I will not open you the windows of heaven and pour you out a blessing, that there shall not be room enough to receive it.",
      "M": "Bring the full tithe into the storehouse, so there will be food in my house. Test me in this, says the LORD of Hosts, and see if I will not open the windows of heaven and pour out a blessing for you beyond what you can contain.",
      "T": "Here is the extraordinary offer: put Yahweh to the test. This is one of the only places in Scripture where God invites testing — because the terms are specific and the promise is certain. Bring the whole tithe, not a partial one: fill the storehouse, provide for the Levites and the poor who depend on it. And watch. The windows of heaven will open. The blessing that pours down will overflow every container they have. This is not a general prosperity gospel; it is a specific covenant promise attached to a specific covenant obligation."
    },
    "11": {
      "L": "And I will rebuke the devourer for your sakes, and he shall not destroy the fruits of your ground; neither shall your vine cast her fruit before the time in the field, says the LORD of hosts.",
      "M": "I will rebuke the devourer for your benefit so that it will not ruin the produce of your land, and your vines in the field will not lose their fruit, says the LORD of Hosts.",
      "T": "And the protection will be as active as the blessing: the devourer — locust, drought, blight, whatever strips the harvest — Yahweh will personally rebuke on their behalf. The vines will hold their fruit to full ripeness. Nothing will strip the land bare. This is the agricultural reversal of the curse in 3:9 — obedience in the tithe becomes protection of the very ground that produces the abundance to tithe."
    },
    "12": {
      "L": "And all nations shall call you blessed; for ye shall be a delightsome land, says the LORD of hosts.",
      "M": "Then all nations will call you blessed, for your land will be a delight, says the LORD of Hosts.",
      "T": "The testimony of Israel's faithfulness will reach the nations. They will look at the land of Yahweh's people and say: Blessed. The land of delight — fruitful, abundantly provided for — becomes a witness to the character of the God who keeps his covenant when his people keep theirs. What began as a reproach among the nations becomes an occasion for all nations to honor the God who blesses faithfully."
    },
    "13": {
      "L": "Your words have been stout against me, says the LORD. Yet ye say, 'What have we spoken so much against thee?'",
      "M": "Your words have been harsh against me, says the LORD. But you ask, 'What have we said against you?'",
      "T": "There is a pattern running through this book: God makes a charge, Israel deflects with 'When did we do that?' But Yahweh hears the words they actually speak — in private, in casual cynicism, among themselves — not the words they intend to project. What they have spoken has been hard and harsh against him, spoken so consistently that they no longer even recognize it as speech against God."
    },
    "14": {
      "L": "Ye have said, 'It is vain to serve God; and what profit is it that we have kept his ordinance, and that we have walked mournfully before the LORD of hosts?'",
      "M": "You have said, 'It is useless to serve God. What do we gain by carrying out his requirements and walking around in mourning before the LORD of Hosts?'",
      "T": "This is the most naked form of the complaint: religion has no return on investment. 'We fasted, we mourned, we kept the ordinances — and what did we get?' The question reveals a transactional view of worship: God is useful when he delivers, worthless when he doesn't. The covenant has been reduced to a contract, and they are dissatisfied with the terms. This is what cynicism sounds like from the inside — not atheism, but practical disillusionment with a God who costs something and gives nothing visible in return."
    },
    "15": {
      "L": "And now we call the proud happy; yea, they that work wickedness are set up; yea, they that tempt God are even delivered.",
      "M": "So now we call the arrogant happy. Evildoers are actually established, and those who test God escape.",
      "T": "The logic collapses all the way to its conclusion: the wicked prosper. The arrogant are the ones who get blessed. Those who openly challenge God — who test him with their defiance — suffer no consequence anyone can see. If piety costs and impiety is free, why be pious? This is the argument from practical observation that Job wrestles with and that Psalm 73 takes to the edge of apostasy. Malachi's people are not asking the question anymore — they have answered it in the wrong direction."
    },
    "16": {
      "L": "Then they that feared the LORD spake often one to another: and the LORD hearkened, and heard it, and a book of remembrance was written before him for them that feared the LORD, and that thought upon his name.",
      "M": "At that point, those who feared the LORD spoke with one another, and the LORD listened and heard. A book of remembrance was written before him for those who feared the LORD and honored his name.",
      "T": "Among the cynics and the complainers, there is a remnant — a small community of those who still fear Yahweh. They find each other. They speak to each other about Yahweh, about his ways, about the things worth cherishing when the world around them has decided they are worthless. And Yahweh hears. Not passive hearing: he listens, he attends. He has a record written — a book of remembrance, a ledger of those who feared him when fear of him was unfashionable. This is what the remnant always looks like: faithful, small, and known."
    },
    "17": {
      "L": "And they shall be mine, saith the LORD of hosts, in that day when I make up my jewels; and I will spare them, as a man spareth his own son that serveth him.",
      "M": "They will be mine, says the LORD of Hosts, on the day when I assemble my special possession. I will spare them the way a man spares a son who serves him.",
      "T": "Yahweh makes his claim: on the day when he gathers what is truly his own — his treasured possession, his sĕgullāh, the covenant word used of Israel at Sinai (Exodus 19:5) — those who feared him will be gathered with it. And they will be spared the way a father spares a faithful son. The remnant does not escape because they are stronger or more numerous; they are gathered because they belong to Yahweh. His fatherly protection is the operative force, not their own merit."
    },
    "18": {
      "L": "Then shall ye return and discern between the righteous and the wicked, between him that serveth God and him that serveth him not.",
      "M": "Then you will again see the distinction between the righteous and the wicked, between one who serves God and one who does not.",
      "T": "The practical cynicism of 3:14–15 will be answered not by argument but by reality. On that day the distinctions that seemed invisible — between the faithful and the faithless, between the servant of God and the one who walked away — will be obvious to all. What seemed like an arbitrary and unrewarded piety will be revealed as the wisest possible orientation. Righteousness and wickedness are not equivalent; the day comes when everyone sees it clearly."
    }
  },
  "4": {
    "1": {
      "L": "For behold, the day cometh, that shall burn as an oven; and all the proud, yea, and all that do wickedly, shall be stubble; and the day that cometh shall burn them up, saith the LORD of hosts, that it shall leave them neither root nor branch.",
      "M": "For look, the day is coming that will burn like a furnace. All the arrogant and every evildoer will be like stubble. The coming day will set them ablaze, says the LORD of Hosts, leaving them neither root nor branch.",
      "T": "The day of the LORD arrives in the imagery of absolute combustion: an oven at full heat, stubble fed into it. The proud — the arrogant who called wickedness blessed, who said there was no profit in serving God — and every evildoer with them: all of it burns. Root and branch both gone, so that nothing can regrow from the stock. The judgment is complete in both directions: what stands above ground and what lies below it. No recovery, no remnant, no comeback for those under this verdict."
    },
    "2": {
      "L": "But unto you that fear my name shall the Sun of righteousness arise with healing in his wings; and ye shall go forth, and grow up as calves of the stall.",
      "M": "But for you who fear my name, the Sun of Righteousness will rise with healing in its wings. You will go out and leap like calves released from the stall.",
      "T": "For those who feared Yahweh's name — the ones whose names are in the book of remembrance — the same day that brings burning brings sunrise. The Sun of Righteousness rises with healing tucked into its wings: warmth, restoration, wholeness for those the darkness had worn down. And the response to that healing is not quiet gratitude but wild joy — calves released from winter pens, free at last, leaping in the open field. This is what the day of the LORD looks like from inside the remnant: not mere survival, but exuberance."
    },
    "3": {
      "L": "And ye shall tread down the wicked; for they shall be ashes under the soles of your feet in the day that I shall do this, says the LORD of hosts.",
      "M": "You will trample the wicked, who will be ashes under the soles of your feet on the day when I act, says the LORD of Hosts.",
      "T": "What the day of the LORD does to the proud: it reduces them to ash. And those who feared Yahweh will walk through that day on the ground where the arrogant used to stand. This is covenant-reversal language — what Deuteronomy promised would follow obedience, made real at the cosmic scale. The power structures that exalted the wicked and crushed the faithful are overturned. The faithful walk on the ash."
    },
    "4": {
      "L": "Remember ye the law of Moses my servant, which I commanded unto him in Horeb for all Israel, with the statutes and judgments.",
      "M": "Remember the law of my servant Moses, the statutes and ordinances I commanded him at Horeb for all Israel.",
      "T": "Before the closing promise, a final call to the foundation: remember the Torah of Moses. Everything Malachi has indicted — the corrupt priests, the polluted offerings, the broken marriages, the withheld tithes, the cynical speech — is a violation of what God commanded at Horeb. The law given at the mountain of God for all Israel is not a preliminary stage to be superseded; it is the covenantal ground on which Israel stands, the document of the relationship they keep abandoning. Until the forerunner comes, the Torah is the guide."
    },
    "5": {
      "L": "Behold, I will send you Elijah the prophet before the coming of the great and dreadful day of the LORD.",
      "M": "Look: I am going to send you the prophet Elijah before the great and awesome day of the LORD comes.",
      "T": "The book ends with a name: Elijah. Not simply a messenger, but the fiery prophet of the northern kingdom — the one who confronted Ahab and Jezebel, who called down fire on Carmel, who fled into the wilderness and heard the still small voice, who was taken up without dying. He is coming back — or one in his spirit and power is coming. Luke 1:17 applies this to John the Baptist: going before the Lord 'in the spirit and power of Elijah.' Matthew 17:12–13 confirms the disciples understood it the same way. The forerunner of 3:1 now has a name."
    },
    "6": {
      "L": "And he shall turn the heart of the fathers to the children, and the heart of the children to their fathers, lest I come and smite the earth with a curse.",
      "M": "He will turn the hearts of fathers to their children and the hearts of children to their fathers, or else I will come and strike the land with utter destruction.",
      "T": "The work of the Elijah-forerunner is reconciliation across the fracture of generations — turning fathers toward their children and children toward their fathers. In a book that has indicted faithless marriages, corrupt priests, and cynical worship, this final promise names the most fundamental human relationship: the family. The fractures within families mirror the fractures in the covenant. When those are healed, the community has a foundation for what is coming. And if they are not healed — if the forerunner's work is refused — what comes is the ban of total destruction, the ḥērem, the most severe covenant sanction. The Hebrew Bible ends on this note: the choice still open, the forerunner still coming, the outcome still depending on the response."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'malachi')
        merge_tier(existing, MALACHI, tier_key)
        save(tier_dir, 'malachi', existing)
    print('Malachi 1–4 written.')

if __name__ == '__main__':
    main()
