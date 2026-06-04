"""
MKT Micah chapter 7 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-micah-7-7.py

=== CHAPTER OVERVIEW ===

Micah 7 is the concluding chapter of the book, structured in four movements:

  vv.1–6   — Lament: the prophet speaks for the community about moral collapse;
              the godly are gone, corruption saturates every social bond.
  vv.7–10  — Pivot to faith: a personal confession + patient trust despite
              endured judgment. The enemy's taunt "Where is your God?" is
              answered not by argument but by outlasting the darkness.
  vv.11–17 — Oracle of restoration: walls rebuilt, exiles returning from every
              direction; nations humbled and brought to dread before Yahweh.
  vv.18–20 — Closing doxology: "Who is a God like you?" — covenant mercy,
              forgiveness, and the inviolable oath sworn to Abraham and Jacob.

The chapter is arguably the most rhetorically complete unit in the Twelve:
lament → confession → oracle → doxology. v.6 is quoted verbatim in Matthew
10:35–36; vv.18–20 form a liturgical staple in Jewish High Holy Day services.

=== TEXTUAL NOTES ===

- v.11: H2706 (חֹק / decree) "far removed" — most probably means the oppressive
  foreign ordinance restricting Israel will be lifted; the idiom parallels
  "walls rebuilt" and anticipates restored sovereignty.
- v.12: The sequence "sea to sea, mountain to mountain" is a merism for
  universal scope (cf. Ps 72:8). Assyria and Egypt are the extremities of
  the known world — the verse envisions a full reversal of the Exile.
- vv.18–20: The doxology names Yahweh three times by implication: the God
  who pardons (v.18), who hurls sins into the sea (v.19), and who fulfils
  the Abrahamic oath (v.20). The three verses are often treated as a
  carefully crafted hymn fragment.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention throughout).
  T: "Yahweh" in direct-address / oracle contexts (vv.7, 10, 17, 18, 20);
  "the LORD" in narrative clauses (v.8, v.9).
  Reason: T surfaces the personal divine name where the text is most
  intimate or climactic; "LORD" in L/M follows standard English OT convention.

- H2617 (חֶסֶד / chesed):
  "steadfast love" in all three tiers throughout (vv.18, 20).
  Reason: chesed in this doxology is covenantal and irreversible —
  "loyal love" or "unfailing love" are acceptable synonyms but "steadfast
  love" has become the consistent choice across all prior OT scripts and
  captures both the loyalty and the active kindness.

- H5315 (נֶפֶשׁ / nephesh) in v.1:
  L: "my soul" (preserves the Hebrew idiom literally).
  M: "my soul" (the idiom is intelligible in English here).
  T: "my whole self" (nephesh = the whole embodied person, not a Greek
  immaterial soul; "my soul craved" in T would mislead readers into
  Platonic dualism).

- H6666 (צְדָקָה / tsedaqah) in v.9:
  L: "his righteousness" (primary gloss, preserves the lexical range).
  M: "his righteousness" (accurate; the context is legal vindication).
  T: "his vindication" (surfaces the forensic/court idiom — God ruling
  in favour of the plaintiff, not merely being morally good).

- H4941 (מִשְׁפָּט / mishpat) in v.9:
  L: "judgment" (the lexical word).
  M: "justice" (natural English for legal settlement in favour of the
  aggrieved party).
  T: "his verdict" (the metaphor of the courtroom case [H7379, rib] is
  explicit in the same verse — "plead my cause and render his verdict").

- H5771 (עָוֹן / awon) = iniquity/guilt:
  L: "iniquity" (technical term for guilt-laden moral wrong).
  M: "iniquity" (retained; familiar and precise).
  T: "our guilt" where the meaning is the state of being guilty;
  "our wrongdoing" where it refers to the acts themselves.

- H6588 (פֶּשַׁע / pesha) = transgression/rebellion:
  L: "transgression" (standard gloss).
  M: "transgression" (retained; complementary to iniquity in v.18
  — the pair signals total moral failure).
  T: "rebellion" (pesha has the force of a wilful political defection
  against a sovereign; "rebellion" captures this more vividly than
  "transgression").

- OT echo, v.19b: "cast all our sins into the depths of the sea" deliberately
  recalls the Egyptian army drowned in the Red Sea (Exod 15:4–5); the T tier
  makes this connection explicit.
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

MICAH = {
  "7": {
    "1": {
      "L": "Woe to me! For I am like one gathering summer fruit, like the gleanings of the vintage — there is no cluster to eat; my soul desired a first-ripe fig.",
      "M": "Woe is me! I am like a gleaner at the summer harvest, like one picking through the remnants of the vintage — no cluster to eat, and my soul craved the first-ripe fruit.",
      "T": "I am bereft! I am like a gleaner in a stripped vineyard — searching for one cluster, one first-ripe fig, and finding nothing. What my whole self longed for has been harvested away."
    },
    "2": {
      "L": "The godly has perished from the earth, and there is no upright person among men; all of them lie in wait for blood; each hunts his brother with a net.",
      "M": "The faithful have vanished from the land; there is no one upright among people. They all lie in ambush for blood; each one hunts his neighbor with a net.",
      "T": "The devout are gone from the earth — not one honest soul remains. Every person is hunting the next, lying in ambush, casting nets for blood. Brotherhood has become predation."
    },
    "3": {
      "L": "Both hands are on evil to do it well — the prince demands, and the judge asks for a reward; and the great man speaks the evil desire of his soul; thus they weave it together.",
      "M": "They are diligent at doing evil — the prince demands a bribe, the judge accepts a payment, and the powerful man states the craving of his heart; and so they weave the scheme together.",
      "T": "They have mastered the craft of corruption: the official names his price, the judge names his reward, the powerful simply state what they want — and together they weave it all into policy."
    },
    "4": {
      "L": "The best of them is like a briar; the most upright is sharper than a thorn hedge. The day of your watchmen, your visitation, has come; now is their confusion.",
      "M": "The best among them is like a briar; the most upright is sharper than a thorn hedge. The day your watchmen warned of — the day of your judgment — has arrived; now they are thrown into bewilderment.",
      "T": "Even their best people draw blood like a briar; even their most upright tear like thornbush. The day the prophets forewarned has come — judgment has arrived — and now the wicked stagger in confusion."
    },
    "5": {
      "L": "Trust not in a companion; put no confidence in a guide; guard the doors of your mouth from her who lies in your bosom.",
      "M": "Put no trust in a neighbor; place no confidence in a close friend. Guard what you say even from the one who lies in your arms.",
      "T": "Trust no one — not your neighbor, not your closest confidant. Even the words spoken in your own bed must be guarded. Intimacy itself has become dangerous."
    },
    "6": {
      "L": "For a son dishonors a father, a daughter rises against her mother, a daughter-in-law against her mother-in-law; a man's enemies are the men of his own house.",
      "M": "For the son treats his father with contempt, the daughter rises against her mother, the daughter-in-law against her mother-in-law; a person's enemies are the members of their own household.",
      "T": "The household itself has fractured: son against father, daughter against mother, daughter-in-law against mother-in-law. Your worst enemies sleep under your own roof."
    },
    "7": {
      "L": "But as for me, I will look to the LORD; I will wait for the God of my salvation; my God will hear me.",
      "M": "As for me, I will watch expectantly for the LORD; I will wait for the God who saves me. My God will hear me.",
      "T": "But I — I will fix my eyes on Yahweh. I will wait, however long it takes, for the God who saves. He will hear me."
    },
    "8": {
      "L": "Rejoice not over me, O my enemy; when I fall, I shall arise; when I sit in darkness, the LORD will be a light to me.",
      "M": "Do not gloat over me, my enemy. Though I have fallen, I will rise. Though I sit in darkness, the LORD is a light for me.",
      "T": "Do not celebrate my fall, enemy. I have gone down — but I will rise. I sit in the dark now; but the LORD himself is my light."
    },
    "9": {
      "L": "I will bear the indignation of the LORD because I have sinned against him, until he pleads my cause and executes judgment for me. He will bring me out to the light; I shall behold his righteousness.",
      "M": "I will endure the LORD's anger, for I have sinned against him, until he takes up my case and brings justice for me. He will lead me out into the light; I shall see his righteousness.",
      "T": "I will accept Yahweh's wrath — I have earned it by my sin — and I will wait until he rises to argue my case and render his verdict. He will bring me into the light; I will see his vindication with my own eyes."
    },
    "10": {
      "L": "Then my enemy shall see, and shame shall cover her who said to me, 'Where is the LORD your God?' My eyes shall behold her; now she shall be trodden down like mud in the streets.",
      "M": "My enemy will see it; shame will cover the one who taunted me, 'Where is the LORD your God?' My own eyes will look upon her; now she will be trampled like mud in the streets.",
      "T": "Then my enemy will see it — the one who sneered, 'Where is your God now?' Shame will cover her face. I will watch it happen with my own eyes: she who mocked will be trampled into the mud of the streets."
    },
    "11": {
      "L": "A day for building your walls; in that day the decree shall be far removed.",
      "M": "A day is coming for rebuilding your walls; on that day the foreign decree will be lifted far away.",
      "T": "A day is coming to rebuild your walls. On that day every ordinance that constrained you will be swept away, and your borders will stretch to their widest."
    },
    "12": {
      "L": "In that day they shall come to you from Assyria and the cities of Egypt, from Egypt to the River, from sea to sea and from mountain to mountain.",
      "M": "In that day people will come to you from Assyria and the cities of Egypt — from Egypt to the Euphrates, from sea to sea and from mountain to mountain.",
      "T": "On that day the scattered will come home — from Assyria, from Egypt, from the great River to the farthest sea, from mountain range to mountain range — streaming back to you from every direction."
    },
    "13": {
      "L": "But the earth shall be desolate because of its inhabitants, for the fruit of their deeds.",
      "M": "But the land will become desolate because of its inhabitants — the result of their deeds.",
      "T": "But first the earth must be stripped bare — a desolation earned by those who live there, the bitter harvest of what they have sown."
    },
    "14": {
      "L": "Shepherd your people with your staff, the flock of your inheritance, who dwell alone in a forest in the midst of a garden land; let them graze in Bashan and Gilead as in the days of old.",
      "M": "Shepherd your people with your staff — the flock of your inheritance — who dwell isolated in a forest surrounded by fertile land. Let them graze in Bashan and Gilead as in ancient days.",
      "T": "Take up your shepherd's staff, O LORD, and lead your people — the flock that is yours alone. They live now like creatures hidden in woodland at the edge of a garden. Lead them out to graze freely in Bashan and Gilead again, as they did in the days of old."
    },
    "15": {
      "L": "As in the days of your coming out of the land of Egypt, I will show them marvelous things.",
      "M": "As in the days when you came out of the land of Egypt, I will show them wonders.",
      "T": "I will do for them what I did when you marched out of Egypt. New wonders, just as astonishing, for a new generation to witness."
    },
    "16": {
      "L": "Nations shall see and be ashamed of all their might; they shall lay their hand on their mouth; their ears shall be deaf.",
      "M": "The nations will see and be put to shame despite all their power; they will put their hand over their mouth; their ears will be stopped.",
      "T": "The nations will watch what God does — and all their vaunted power will wilt into shame. They will cover their mouths in stunned silence; they will be deaf to the sound of their own boasting."
    },
    "17": {
      "L": "They shall lick the dust like a serpent, like the crawling things of the earth; they shall come trembling from their strongholds; they shall turn in dread to the LORD our God, and they shall fear you.",
      "M": "They will lick the dust like a snake, like creatures that crawl on the earth; they will come trembling out of their fortresses; they will turn in dread to the LORD our God, and will be in fear of you.",
      "T": "They will lick the dust like serpents, crawling from their strongholds in terror. Nations that once fielded armies will come out trembling, cringing before Yahweh our God — all their former pride collapsed into fear."
    },
    "18": {
      "L": "Who is a God like you, pardoning iniquity and passing over transgression for the remnant of his inheritance? He does not retain his anger forever, because he delights in steadfast love.",
      "M": "Who is a God like you, forgiving iniquity and passing over transgression for the remnant of his inheritance? He does not keep his anger forever, for he delights in steadfast love.",
      "T": "Who is there like you, O God? You pardon our iniquity; you pass over rebellion — for the sake of those who remain as your inheritance. Your anger has an end because your deepest delight is the love that never lets go."
    },
    "19": {
      "L": "He will again have compassion on us; he will tread down our iniquities. You will cast all our sins into the depths of the sea.",
      "M": "He will again have compassion on us; he will trample our iniquities underfoot. You will hurl all our sins into the depths of the sea.",
      "T": "He will have compassion again — compassion that circles back even to the guilty. He will crush our wrongdoing beneath his feet. Every sin we have ever committed will be hurled into the deepest abyss of the sea, as he once hurled Pharaoh's army into the deep, never to return."
    },
    "20": {
      "L": "You will show faithfulness to Jacob and steadfast love to Abraham, as you swore to our fathers from the days of old.",
      "M": "You will be faithful to Jacob and show steadfast love to Abraham, just as you swore to our fathers in days long past.",
      "T": "You will keep the oath — faithfulness to Jacob, covenant love to Abraham — the very promises sworn to our ancestors in the ancient days. The God who made those vows still stands by every one of them."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'micah')
        merge_tier(existing, MICAH, tier_key)
        save(tier_dir, 'micah', existing)
    print('Micah 7 written.')

if __name__ == '__main__':
    main()
