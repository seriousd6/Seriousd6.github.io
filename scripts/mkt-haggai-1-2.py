"""
MKT Haggai chapters 1–2 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-haggai-1-2.py

=== BOOK OVERVIEW ===

Haggai prophesied in 520 BCE, the second year of Darius I (Hystaspes), eighteen
years after Cyrus's decree allowed the exiles to return. The temple foundation had
been laid in 536 BCE but work had halted for sixteen years under opposition. Haggai
is the first post-exilic prophet; his book is the most precisely dated in the OT,
with four oracles delivered within four months.

Structure:
  1:1–15   — First oracle: accusation and call to rebuild (month 6, day 1)
  2:1–9    — Second oracle: the latter glory (month 7, day 21)
  2:10–19  — Third oracle: the holiness/uncleanness instruction (month 9, day 24)
  2:20–23  — Fourth oracle: Zerubbabel as signet ring (month 9, day 24)

Haggai's central argument is that the community's economic suffering (drought,
crop failure, wage drain) is not bad luck but covenant consequence: they have
withheld from Yahweh what is his, so the covenant curses of Deut 28 have
operated. Once they build, the blessing will be reversed (2:19).

The book closes with a messianic-laden promise to Zerubbabel as Yahweh's signet
ring — a deliberate reversal of Jer 22:24 where Coniah/Jehoiachin was pulled off
as a signet and thrown away. Zerubbabel (Coniah's grandson, Matt 1:12) is
restored to Davidic-dynastic significance.

=== TEXTUAL NOTES ===

- 1:6: The list of futility curses echoes Deut 28:38–40 — sowing much, harvesting
  little; eating without satisfaction; drinking without filling. This is not
  Haggai's rhetoric; it is Moses's. The connection is deliberate.
- 1:11: H2721 (ḥoreb, drought) echoes H2022 (mountain) phonetically in Hebrew
  (ḥāreb / har). Haggai's wordplay: drought comes on the "ḥoreb" — the mountains
  they should have climbed to cut timber (1:8).
- 2:5: "According to the covenant I made with you when you came out of Egypt" —
  this clause is absent in the LXX. It is present in the MT and connects the
  Sinai covenant explicitly to the promise "my Spirit remains in your midst."
  I retain the MT reading.
- 2:7: H2532 (ḥemdāh, "desirable thing / treasure") is grammatically feminine
  singular as a subject, but its verb בָּאוּ is plural — suggesting a collective
  ("desirable things / treasures"). The KJV "the Desire of all Nations" as a
  messianic title follows the Vulgate and patristic tradition but cannot be
  sustained from the Hebrew grammar. Rendered "precious things" (L), "treasures"
  (M), and "all that the nations treasure" (T). The eschatological filling of the
  temple is the primary sense; messianic resonance is a secondary typological
  reading for which the T tier notes the temple-Christology trajectory.
- 2:9: H7965 (shalom) is not merely "peace" but comprehensive well-being and
  wholeness. T expands slightly. This promise may look beyond the rebuilt temple
  toward the eschatological peace of the new creation.
- 2:23: H2368 (ḥôtām, signet ring). The reversal of Jer 22:24 is the key. Where
  Jehoiachin was torn off as a signet ("even if Coniah were a signet ring on my
  right hand, I would pull him off"), Zerubbabel is reinstated to the same
  imagery. Davidic-messianic trajectory runs through Zerubbabel to Jesus in
  Matthew 1:12–13. T makes this explicit.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention) throughout.
  T: "Yahweh" in direct address, oracle closings, and climactic declarations;
     "the LORD" in narrative transitions. Consistent with Zephaniah, Habakkuk,
     and all prior Minor Prophets in this translation series.

- H6635 (צְבָאוֹת / tseba'ot, hosts):
  L/M: "of hosts" (standard: "the LORD of hosts").
  T: "of Armies" (rendering the divine warrior epithet more concretely).

- H430 (אֱלֹהִים / Elohim):
  Rendered "God" throughout; no tier distinction required in Haggai.

- H7307 (רוּחַ / ruach):
  1:14 — refers to the human inner resolve of Zerubbabel, Joshua, and the people:
    L/M/T: lowercase "spirit" (the human spirit that Yahweh stirs).
  2:5 — refers to the divine Presence promised in the Exodus covenant:
    L/M/T: capitalized "Spirit" (God's animating presence among his people).

- H2532 (חֶמְדָּה / ḥemdāh, desirable things):
  2:7: L: "the precious things of all nations"
       M: "the treasures of all nations"
       T: "all that the nations treasure" — grammatically collective; the sense is
          material wealth flowing to the temple in the eschatological vision, not
          a messianic title. The Christological reading is valid typologically
          (temple → Christ, Heb 9) but should not override the plain syntax.

- H7965 (שָׁלוֹם / shalom):
  2:9: L/M: "peace"
       T: "wholeness and peace" — shalom encompasses both.

- H4397 (מַלְאָךְ / mal'ak, messenger):
  1:13: "messenger" in all tiers. Haggai is called Yahweh's messenger
  (mal'ak) — the same word used for angels. This is the only place in the
  OT where a prophet is explicitly called by this title in the text itself.

- H2368 (חוֹתָם / ḥôtām, signet ring):
  2:23: "signet ring" in L/M; "seal of my authority" in T apposition.

- Covenant-curse language in chapter 1: The drought/futility motifs deliberately
  echo Deuteronomy 28. No paraphrase needed — the allusion is structural and
  conveyed by accurate rendering.
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

HAGGAI = {
  "1": {
    "1": {
      "L": "In the second year of Darius the king, in the sixth month, on the first day of the month, the word of the LORD came by Haggai the prophet to Zerubbabel the son of Shealtiel, governor of Judah, and to Joshua the son of Jehozadak, the high priest.",
      "M": "In the second year of King Darius, on the first day of the sixth month, the word of the LORD came through the prophet Haggai to Zerubbabel son of Shealtiel, governor of Judah, and to Joshua son of Jehozadak, the high priest.",
      "T": "In the second year of Darius the king — on the first day of the sixth month — the word of Yahweh came through his prophet Haggai to two leaders: Zerubbabel son of Shealtiel, governor of Judah, and Joshua son of Jehozadak, the high priest."
    },
    "2": {
      "L": "Thus says the LORD of hosts: This people say, 'The time has not yet come, even the time for the house of the LORD to be built.'",
      "M": "This is what the LORD of Hosts says: 'These people are saying, \"The time has not yet come to rebuild the LORD's house.\"'",
      "T": "Thus says Yahweh of Armies: Listen to what these people are telling themselves — 'The time has not come yet. The LORD's house can wait.'"
    },
    "3": {
      "L": "Then the word of the LORD came by Haggai the prophet, saying:",
      "M": "Then the word of the LORD came through the prophet Haggai:",
      "T": "Then Yahweh spoke again through Haggai the prophet:"
    },
    "4": {
      "L": "Is it time for you yourselves to dwell in your paneled houses while this house lies in ruins?",
      "M": "Is this really the time for you to be living in your paneled houses while this house lies in ruins?",
      "T": "So it is not yet time for the LORD's house — but somehow it is already time for you to be living in your fine, ceiled houses? And all the while, my house lies in rubble."
    },
    "5": {
      "L": "Now therefore thus says the LORD of hosts: Consider your ways.",
      "M": "So now this is what the LORD of Hosts says: Think carefully about the path you are on.",
      "T": "This is what Yahweh of Armies says: Stop and look honestly at the road you have been walking."
    },
    "6": {
      "L": "You have sown much, and harvested little; you eat, but you never have enough; you drink, but you never have your fill; you clothe yourselves, but no one is warm; and he who earns wages earns wages to put them into a bag with holes.",
      "M": "You have planted much but harvested little. You eat, but never have enough. You drink, but never have your fill. You clothe yourselves, but no one is warm enough. You earn wages, only to put them in a purse full of holes.",
      "T": "You plant much — and bring in little. You eat — and still go hungry. You drink — and still go thirsty. You dress yourselves — and still feel the cold. You work for wages — and watch them drain away as if your pocket had holes. Every abundance slips through your fingers. These are the covenant curses you once heard read, now walking in your fields."
    },
    "7": {
      "L": "Thus says the LORD of hosts: Consider your ways.",
      "M": "This is what the LORD of Hosts says: Think carefully about the path you are on.",
      "T": "Yahweh of Armies says it again: Look honestly at the life you are building."
    },
    "8": {
      "L": "Go up to the hills and bring wood and build the house, and I will take pleasure in it and I will be glorified, says the LORD.",
      "M": "Go up to the mountains, bring down wood, and build the house — so that I may take pleasure in it and be glorified, says the LORD.",
      "T": "Go up to the hills. Cut timber. Come back and build my house. Then I will take pleasure in it. Then I will be honored. Yahweh has spoken."
    },
    "9": {
      "L": "You looked for much, and behold, it came to little; and when you brought it home, I blew it away. Why? declares the LORD of hosts. Because of my house that lies in ruins, while each of you runs to his own house.",
      "M": "You expected much, but it came to little. And what you brought home, I blew away. Why? declares the LORD of Hosts. Because my house lies in ruins while every one of you is busy taking care of his own house.",
      "T": "You expected abundance — what came was almost nothing. And even what you carried home, I scattered with a single breath. Why? Yahweh of Armies answers his own question: Because my house is lying in ruins. Because every one of you is too busy running toward your own home to look at mine."
    },
    "10": {
      "L": "Therefore, because of you the heavens have withheld the dew, and the earth has withheld its produce.",
      "M": "Therefore, on your account, the sky has withheld its dew and the earth has withheld its produce.",
      "T": "That is why the skies have held back the dew. That is why the earth has refused its harvest. The connection is direct: you withheld from my house, so I withheld the rain."
    },
    "11": {
      "L": "And I have called for a drought on the land and the hills, on the grain, the new wine, the oil, on what the ground brings forth, on men and on cattle, and on all the labor of their hands.",
      "M": "I have decreed a drought on the land and the hills, on the grain, the new wine, and the oil — on everything the ground produces, on people and animals, and on all the work of their hands.",
      "T": "I have called down drought — on the farmland and the highland pastures, on the grain, the wine, the olive oil, on everything that grows from the soil, on people and livestock alike, on every project human hands have attempted. Nothing is exempt."
    },
    "12": {
      "L": "Then Zerubbabel the son of Shealtiel, and Joshua the son of Jehozadak, the high priest, with all the remnant of the people, obeyed the voice of the LORD their God and the words of Haggai the prophet, as the LORD their God had sent him; and the people feared before the LORD.",
      "M": "Then Zerubbabel son of Shealtiel, Joshua son of Jehozadak the high priest, and all the remnant of the people obeyed the voice of the LORD their God and the words of the prophet Haggai — as the LORD their God had sent him. And the people stood in awe of the LORD.",
      "T": "The response was immediate. Zerubbabel son of Shealtiel and Joshua son of Jehozadak the high priest — together with every last person in the remnant — listened. They obeyed the voice of Yahweh their God and the words Haggai had brought, for Yahweh himself had sent him. And the people stood in fear before Yahweh."
    },
    "13": {
      "L": "Then Haggai, the messenger of the LORD, spoke to the people with the LORD's message, saying: 'I am with you, declares the LORD.'",
      "M": "Then Haggai, the LORD's messenger, delivered the LORD's message to the people: 'I am with you,' declares the LORD.",
      "T": "Then Haggai — Yahweh's own messenger, bearing Yahweh's own word — spoke to the people: 'I am with you.' That is all. But it is everything. Yahweh has spoken."
    },
    "14": {
      "L": "And the LORD stirred up the spirit of Zerubbabel the son of Shealtiel, governor of Judah, and the spirit of Joshua the son of Jehozadak, the high priest, and the spirit of all the remnant of the people; and they came and worked on the house of the LORD of hosts, their God,",
      "M": "The LORD stirred up the spirit of Zerubbabel son of Shealtiel, governor of Judah, the spirit of Joshua son of Jehozadak the high priest, and the spirit of all the remnant of the people; and they came and began work on the house of the LORD of Hosts, their God,",
      "T": "Yahweh reached down and stirred the inner resolve of Zerubbabel son of Shealtiel, governor of Judah, of Joshua son of Jehozadak the high priest, and of the whole remnant of the people — stirred it awake from within. They came. They worked. They worked on the house of Yahweh of Armies, their God —"
    },
    "15": {
      "L": "on the twenty-fourth day of the sixth month, in the second year of Darius the king.",
      "M": "on the twenty-fourth day of the sixth month, in the second year of King Darius.",
      "T": "— on the twenty-fourth day of the sixth month, in the second year of King Darius. Twenty-three days after the first oracle. That is how quickly they moved."
    }
  },
  "2": {
    "1": {
      "L": "In the seventh month, on the twenty-first day of the month, the word of the LORD came by the hand of Haggai the prophet, saying:",
      "M": "On the twenty-first day of the seventh month, the word of the LORD came through the prophet Haggai:",
      "T": "On the twenty-first day of the seventh month — fifty days into the work — the word of Yahweh came through Haggai the prophet again:"
    },
    "2": {
      "L": "Speak now to Zerubbabel the son of Shealtiel, governor of Judah, and to Joshua the son of Jehozadak, the high priest, and to all the remnant of the people, saying:",
      "M": "Speak to Zerubbabel son of Shealtiel, governor of Judah, and to Joshua son of Jehozadak the high priest, and to all the remnant of the people. Say to them:",
      "T": "Speak to Zerubbabel son of Shealtiel, governor of Judah, to Joshua son of Jehozadak the high priest, and to every person left in the community. Tell them this:"
    },
    "3": {
      "L": "Who is left among you who saw this house in its former glory? How do you see it now? Is it not as nothing in your eyes?",
      "M": "Who among you is still alive who saw this house in its former splendor? And how does it appear to you now? Does it not seem like nothing to you?",
      "T": "Is anyone among you old enough to have seen Solomon's temple in its glory? Now look at what is being built. Is there any comparison? In your eyes it seems like nothing, doesn't it. The question hangs in the air unanswered, because the answer is obvious."
    },
    "4": {
      "L": "Yet now be strong, O Zerubbabel, declares the LORD; and be strong, O Joshua, son of Jehozadak, the high priest; and be strong, all the people of the land, declares the LORD; and work, for I am with you, declares the LORD of hosts,",
      "M": "But now be strong, Zerubbabel, declares the LORD. Be strong, Joshua son of Jehozadak, the high priest. Be strong, all you people of the land, declares the LORD — and work! For I am with you, declares the LORD of Hosts,",
      "T": "Even so — be strong, Zerubbabel. Be strong, Joshua son of Jehozadak. Be strong, every one of you who remains. Yahweh says it three times over: be strong. Work. Because I am with you — and that is the declaration of Yahweh of Armies —"
    },
    "5": {
      "L": "according to the word which I covenanted with you when you came out of Egypt; my Spirit remains in your midst; fear not.",
      "M": "in keeping with the covenant I made with you when you came out of Egypt. My Spirit remains in your midst; do not be afraid.",
      "T": "— exactly as I promised in the covenant made when I brought you out of Egypt. My Spirit has not left. I am still here in your midst. You have no reason to be afraid."
    },
    "6": {
      "L": "For thus says the LORD of hosts: Yet once more, in a little while, I will shake the heavens and the earth and the sea and the dry land.",
      "M": "For this is what the LORD of Hosts says: Once more, in just a little while, I will shake the heavens, the earth, the sea, and the dry land.",
      "T": "For this is what Yahweh of Armies declares: Once more — and it is not far off — I will shake the heavens and the earth, the sea and the dry land. A shaking is coming that will reorder everything."
    },
    "7": {
      "L": "And I will shake all the nations, and the precious things of all nations shall come in, and I will fill this house with glory, says the LORD of hosts.",
      "M": "I will shake all the nations so that the treasures of all nations will come, and I will fill this house with glory, says the LORD of Hosts.",
      "T": "I will shake every nation to its foundations, and all that the nations treasure will flow into this house. Then I will fill it with my glory. Yahweh of Armies has spoken."
    },
    "8": {
      "L": "The silver is mine, and the gold is mine, declares the LORD of hosts.",
      "M": "The silver is mine and the gold is mine, declares the LORD of Hosts.",
      "T": "The silver — it is mine. The gold — it is mine. Yahweh of Armies has no shortage of resources. What fills the temple will come from him, not from the poverty of the builders."
    },
    "9": {
      "L": "The latter glory of this house shall be greater than the former, says the LORD of hosts; and in this place I will give peace, declares the LORD of hosts.",
      "M": "The future splendor of this house will surpass its former glory, says the LORD of Hosts. And in this place I will give peace, declares the LORD of Hosts.",
      "T": "The glory of this house in the age to come will surpass the glory of what stood before. This is what Yahweh of Armies promises. And in this very place I will give wholeness and peace — shalom. Yahweh of Armies has spoken."
    },
    "10": {
      "L": "On the twenty-fourth day of the ninth month, in the second year of Darius, the word of the LORD came to Haggai the prophet, saying:",
      "M": "On the twenty-fourth day of the ninth month, in the second year of Darius, the word of the LORD came to the prophet Haggai:",
      "T": "On the twenty-fourth day of the ninth month — still in the second year of Darius — the word of Yahweh came to Haggai the prophet a third time:"
    },
    "11": {
      "L": "Thus says the LORD of hosts: Ask now the priests for a ruling on the law:",
      "M": "This is what the LORD of Hosts says: Ask the priests for a ruling on the law:",
      "T": "Yahweh of Armies says: Put a question to the priests — let them render a formal decision from the law:"
    },
    "12": {
      "L": "If someone carries holy meat in the fold of his garment, and with his fold touches bread, or stew, or wine, or oil, or any food, does it become holy? The priests answered and said, No.",
      "M": "If someone carries holy meat in the fold of his garment and his garment touches bread, stew, wine, oil, or any other food, does that food become holy? The priests answered: No.",
      "T": "Suppose someone is carrying consecrated meat wrapped in the fold of his robe. Does holiness transfer — if that robe touches bread, or stew, or wine, or oil, or any food, does the food become holy? The priests answered: No. Holiness does not spread outward by contact."
    },
    "13": {
      "L": "Then Haggai said, If someone who is unclean through contact with a dead body touches any of these, does it become unclean? The priests answered and said, It does become unclean.",
      "M": "Then Haggai said: If someone who is defiled by contact with a corpse touches any of these things, does it become defiled? The priests answered: It does become defiled.",
      "T": "Then Haggai asked the second question: What if someone defiled by contact with a dead body touches any of these things — does the uncleanness spread to them? Yes, the priests answered without hesitation. Uncleanness spreads."
    },
    "14": {
      "L": "Then Haggai answered and said, So is this people, and so is this nation before me, declares the LORD; and so is every work of their hands, and what they offer there is unclean.",
      "M": "Then Haggai answered: That is exactly how it is with this people and this nation before me, declares the LORD — and with every work of their hands. Whatever they offer there is defiled.",
      "T": "Then Haggai drew the conclusion: That is exactly the situation of this people — of this nation — before me, declares Yahweh. Everything their hands touch is made unclean by what they themselves are. Every offering they bring to the altar is defiled. Not because the ritual is wrong, but because the worshipers are unclean. Uncleanness spreads; holiness does not."
    },
    "15": {
      "L": "Now therefore consider from this day onward. Before a stone was placed upon a stone in the temple of the LORD,",
      "M": "Now consider carefully from this day forward. Before one stone was set upon another in the LORD's temple,",
      "T": "Now — consider carefully. Think back before the foundation of Yahweh's temple was laid, before a single stone was set on another —"
    },
    "16": {
      "L": "when one came to a heap of twenty measures, there were but ten; when one came to the wine vat to draw fifty, there were but twenty.",
      "M": "how did you fare? When someone came to a grain pile expecting twenty measures, there were only ten. When one came to the wine vat to draw out fifty, there were only twenty.",
      "T": "— what was life like in those years? You came to the grain pile expecting twenty measures and found ten. You came to the wine press expecting fifty jars and found twenty. Half of everything, every time. You noticed the shortage but did not understand the reason."
    },
    "17": {
      "L": "I struck you and all the products of your toil with blight and mildew and hail, yet you did not turn to me, declares the LORD.",
      "M": "I struck you and all the products of your labor with blight, mildew, and hail — yet you did not return to me, declares the LORD.",
      "T": "I was the one behind every failure — striking your fields with blight, mildew, and hail, striking everything your hands worked for. And through it all, through every sign, you never turned back to me. Yahweh declares this."
    },
    "18": {
      "L": "Consider now from this day onward, from the twenty-fourth day of the ninth month. From the day when the foundation of the LORD's temple was laid, consider:",
      "M": "Consider carefully from this day on — the twenty-fourth day of the ninth month — from the day the LORD's temple foundation was laid. Consider:",
      "T": "So consider from this very day forward — from the twenty-fourth of the ninth month, the day the foundation of Yahweh's temple was formally laid. From today, consider what changes:"
    },
    "19": {
      "L": "Is the seed still in the barn? The vine, the fig tree, the pomegranate, and the olive tree have not yet yielded. But from this day I will bless you.",
      "M": "Is the seed still in the granary? The vine, the fig tree, the pomegranate, and the olive tree have not yet produced. But from this day on I will bless you.",
      "T": "The seed is still in the storehouse; the vine, the fig tree, the pomegranate, the olive — none of them have borne fruit yet. The harvest has not come. But from this day on, I will bless you. The moment of reversal is now. Watch."
    },
    "20": {
      "L": "The word of the LORD came a second time to Haggai on the twenty-fourth day of the month, saying:",
      "M": "The word of the LORD came a second time to Haggai on the twenty-fourth day of the month:",
      "T": "That same day — the twenty-fourth — the word of Yahweh came to Haggai a second time, a fourth oracle in a single day:"
    },
    "21": {
      "L": "Speak to Zerubbabel, governor of Judah, saying: I am about to shake the heavens and the earth,",
      "M": "Speak to Zerubbabel, governor of Judah, and say: I am about to shake the heavens and the earth,",
      "T": "Tell Zerubbabel, governor of Judah: I am about to shake the heavens and the earth —"
    },
    "22": {
      "L": "and to overthrow the throne of kingdoms, and to destroy the strength of the kingdoms of the nations; and I will overthrow the chariots and their riders; and the horses and their riders shall go down, every one by the sword of his brother.",
      "M": "I will overturn royal thrones and shatter the power of the kingdoms of the nations. I will overturn chariots and their riders; the horses and their riders will go down, each by the sword of his fellow.",
      "T": "— overturning every throne, breaking the military power of every kingdom on earth. Chariots will be overturned. Riders will fall. And in the chaos, armies will turn against themselves — brother killing brother. Every empire built on human strength will be brought down."
    },
    "23": {
      "L": "On that day, declares the LORD of hosts, I will take you, O Zerubbabel my servant, the son of Shealtiel, declares the LORD, and will make you like a signet ring, for I have chosen you, declares the LORD of hosts.",
      "M": "On that day, declares the LORD of Hosts, I will take you, Zerubbabel my servant son of Shealtiel, and make you like a signet ring, for I have chosen you, declares the LORD of Hosts.",
      "T": "On that day, declares Yahweh of Armies, I will take you — you, Zerubbabel my servant, son of Shealtiel — and make you like a signet ring. Once Jehoiachin was torn off like a signet and cast away; now his grandson is restored to that place of royal authority. You are the seal of my ownership, the mark of my intention. For I have chosen you. Yahweh of Armies has spoken."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'haggai')
        merge_tier(existing, HAGGAI, tier_key)
        save(tier_dir, 'haggai', existing)
    print('Haggai 1–2 written.')

if __name__ == '__main__':
    main()
