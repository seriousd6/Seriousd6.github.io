"""
MKT Jonah chapters 1–4 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jonah-1-4.py

=== BOOK OVERVIEW ===

Jonah is the most narrative of the Minor Prophets — a short story rather than an
oracle collection. Jonah ben-Amittai appears elsewhere only at 2 Kings 14:25
(active under Jeroboam II, c. 780 BCE). The book's literary sophistication and
theological irony suggest a later composition using that historical figure.

The book unfolds in two parallel movements:
  Act I (chs. 1–2): Jonah flees; storm; sailors repent; fish; Jonah's prayer.
  Act II (chs. 3–4): Jonah preaches (minimally); Nineveh repents; Jonah rages.
The structural parallel highlights the irony: pagan sailors and Ninevites respond
with immediate, wholehearted repentance; the prophet of Israel sulks.

The book is polemical theology — challenging a narrow nationalism that would restrict
Yahweh's mercy to Israel alone. The final verse (4:11) is a question left unanswered,
drawing the reader into Yahweh's logic of mercy.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention in plain text, as throughout the OT).
  T: "Yahweh" in divine-speech, covenantal, and eschatological contexts;
     "the LORD" in purely narrative references where the name is incidental.
  Follows Obadiah, Joel, Hosea, and Amos conventions.

- H430 (אֱלֹהִים / Elohim):
  "God" throughout all tiers. In ch.1 it refers to the sailors' various deities
  (plural object "their god"), then shifts to the Ninevites calling on Israel's
  God. Context disambiguates without needing different renderings.

- H410 (אֵל / El, 4:2):
  "God" — part of the divine-attributes formula Jonah quotes from Exod 34:6.

- H7307 (רוּחַ / ruach):
  In 1:4 ("a great wind") and 4:8 ("a scorching east wind"): clearly meteorological
  in both contexts. All three tiers: "wind" — no Spirit/breath ambiguity here.

- H5315 (נֶפֶשׁ / nephesh):
  1:14: "life" (innocent blood / life). 2:5: "soul" (water covering the soul =
  near death). 2:7: "soul" (soul fainted = inner being). 4:3: "life" (take my life).
  4:8: "within himself" (desired in his nephesh = inwardly). The embodied sense
  is preserved — not an immaterial Greek psychē.

- H2617 (חֶסֶד / hesed):
  2:8: Rendered "steadfast love" (L), "steadfast love" (M), "the mercy that could
  have been theirs" (T) — those who cling to idols forfeit the covenant loyalty
  Yahweh offers.
  4:2: Part of the classical divine-attributes formula (Exod 34:6 echo). L: "abounding
  in steadfast love." M: "overflowing with steadfast love." T: "overflowing with
  loyal love." Distinction from mere sentimentality is maintained.

- H5162 (נָחַם / naham, "relent/repent/be moved"):
  3:9: "turn and relent" (God). 3:10: "relented" (God). 4:2: "relents from disaster"
  (Jonah quoting divine attribute). This is the key theological term: God's
  willingness to change course when circumstances change — not divine inconstancy
  but responsive covenant faithfulness. L: "relented" / "repented"; M: "relented";
  T: "relented" / "pulled back his judgment." The same root appears in 3:9 for
  Nineveh's hope that God may naham; all three tiers make this visible.

- H4487 (מָנָה / manah, "prepare/appoint"):
  Used four times of divine provision: 1:17 (fish), 4:6 (plant), 4:7 (worm),
  4:8 (wind). L: "appointed." M: "provided." T: varies to show divine intention —
  "appointed," "caused to grow," "sent." The point is each is a purposeful divine
  act, not accident.

- H7021 (קִיקָיוֹן / qiqayon, the shade plant of ch.4):
  Species uncertain (castor oil plant / ricinus communis is most likely; some
  propose gourd or ivy). L: "gourd" (KJV tradition, not botanically precise but
  historically conventional). M/T: "leafy plant" (neutral, avoids false precision).

- H5521 (סֻכָּה / sukkah, 4:5, "booth"):
  Jonah builds a temporary shelter. L: "booth." M: "shelter." T: "lean-to" (captures
  the provisional, makeshift character of his wait).

- Jonah's "prayer" in ch. 2:
  The prayer is structured as a Hebrew thanksgiving psalm (todah), written in past
  tense recounting deliverance already experienced — a literary device signalling
  that Jonah's deliverance is certain even as he prays from inside the fish.
  The T tier preserves the psalm's poetic line structure with line breaks.
  L/M render as flowing prose with implied line structure.

- 3:4 "overthrown" (H2015, haphak):
  The same verb used of Sodom's overthrow. L/M: "overthrown." T: "destroyed."
  The ambiguity in the Hebrew (haphak can also mean "turned/transformed") may
  be intentional — Nineveh was indeed "overthrown" in the sense of being turned
  around, not just destroyed. The T tier preserves "destroyed" but readers familiar
  with Hebrew will note the double meaning.

- 1:17 numbering convention:
  In Hebrew manuscripts ch.1:17 is ch.2:1 in the MT — BHS puts the fish verse
  at the start of ch.2. English Bibles (KJV, ESV) number it 1:17. This script
  follows English chapter/verse numbering throughout (ch.1 has 17 verses,
  ch.2 begins at the prayer).

- Aspect notes:
  The narrative uses waw-consecutive imperfects (wayiqtol) for sequential past
  action throughout — rendered as simple English past tense. Jonah's prayer (ch.2)
  uses qatal (perfect) forms, rendered as simple past to preserve the psalm's
  retrospective character. The divine-attribute formula in 4:2 uses participles
  (ongoing characterization of God's nature).
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


JONAH = {
    "1": {
        "1": {
            "L": "And the word of the LORD came to Jonah the son of Amittai, saying,",
            "M": "The word of the LORD came to Jonah son of Amittai:",
            "T": "Yahweh's word came to Jonah ben-Amittai:"
        },
        "2": {
            "L": "'Arise, go to Nineveh, that great city, and cry out against it, for their evil has come up before me.'",
            "M": "'Get up and go to Nineveh, that great city, and proclaim against it, for their wickedness has come up before me.'",
            "T": "'Get up and go to Nineveh—that great city—and cry out against it. Their wickedness has come up before my face.'"
        },
        "3": {
            "L": "But Jonah rose to flee to Tarshish from the presence of the LORD. He went down to Joppa and found a ship going to Tarshish. So he paid the fare and went down into it, to go with them to Tarshish, away from the presence of the LORD.",
            "M": "But Jonah got up to flee to Tarshish, away from the LORD's presence. He went down to Joppa and found a ship bound for Tarshish, paid the fare, and went aboard to sail with them to Tarshish—away from the LORD's presence.",
            "T": "Jonah bolted in the opposite direction—toward Tarshish, as far from Yahweh's face as a ship could carry him. He went down to Joppa, found a vessel heading for Tarshish, paid his passage, and went down into it—heading away, away from the presence of Yahweh."
        },
        "4": {
            "L": "But the LORD hurled a great wind upon the sea, and there was a mighty tempest on the sea, so that the ship was about to be broken up.",
            "M": "But the LORD sent a powerful wind across the sea, and a violent storm arose so that the ship threatened to break apart.",
            "T": "Then Yahweh hurled a great wind onto the sea. The storm grew so fierce the ship groaned—on the verge of breaking apart."
        },
        "5": {
            "L": "Then the mariners were afraid, and each cried out to his god. They hurled the wares that were in the ship into the sea, to lighten it. But Jonah had gone down into the inner parts of the ship and lay down and was fast asleep.",
            "M": "The sailors were terrified, and each one called on his own god. They threw the cargo overboard to lighten the ship. But Jonah had gone down into the hold, where he lay fast asleep.",
            "T": "The sailors were seized with panic—each crying to his own god, heaving the cargo into the sea to lighten the load. Meanwhile Jonah had gone below into the ship's hold and was lying there in a deep sleep."
        },
        "6": {
            "L": "So the captain came to him and said, 'What do you mean, you sleeper? Arise, call out to your god! Perhaps the god will give us a thought, so that we may not perish.'",
            "M": "The captain went to him and said, 'How can you sleep? Get up and call on your god! Maybe he will spare a thought for us and we won't die.'",
            "T": "The captain found him and said, 'How can you sleep at a time like this? Get up and pray to your God! Maybe he will notice us and we won't perish.'"
        },
        "7": {
            "L": "And each said to his fellow, 'Come, let us cast lots, that we may know on whose account this evil has come upon us.' So they cast lots, and the lot fell on Jonah.",
            "M": "Then the sailors said to each other, 'Let's cast lots to find out who is responsible for this disaster.' They cast lots, and the lot fell on Jonah.",
            "T": "The men said to one another, 'Let's cast lots and find out who has brought this trouble on us.' They cast the lots—and the lot fell on Jonah."
        },
        "8": {
            "L": "Then they said to him, 'Tell us on whose account this evil has come upon us. What is your occupation? And where do you come from? What is your country? And of what people are you?'",
            "M": "They said to him, 'Tell us—who is responsible for bringing this disaster on us? What is your trade? Where are you from? What country and what people do you belong to?'",
            "T": "'Tell us who's caused this,' they demanded. 'What is your trade? Where are you from? What nation do you belong to?'"
        },
        "9": {
            "L": "And he said to them, 'I am a Hebrew, and I fear the LORD, the God of heaven, who made the sea and the dry land.'",
            "M": "He answered, 'I am a Hebrew, and I worship the LORD, the God of heaven, who made both the sea and the dry land.'",
            "T": "'I am a Hebrew,' he said. 'I worship Yahweh—the God of heaven—the one who made the sea and the dry land.'"
        },
        "10": {
            "L": "Then the men were exceedingly afraid and said to him, 'What is this that you have done?' For the men knew that he was fleeing from the presence of the LORD, because he had told them.",
            "M": "This terrified them, and they said, 'What have you done?' For they knew he was fleeing from the LORD's presence, because he had told them.",
            "T": "The men were seized with terror. 'What have you done?' they said. They already knew he was running from Yahweh—he had told them himself."
        },
        "11": {
            "L": "Then they said to him, 'What shall we do to you, that the sea may quiet down for us?' For the sea grew more and more tempestuous.",
            "M": "They asked him, 'What must we do with you to make the sea calm down?' For the sea was growing rougher and rougher.",
            "T": "'What do we do with you to stop this sea?' they asked. The storm was growing worse by the moment."
        },
        "12": {
            "L": "He said to them, 'Pick me up and hurl me into the sea; then the sea will quiet down for you, for I know it is because of me that this great tempest has come upon you.'",
            "M": "He told them, 'Pick me up and throw me into the sea, and it will calm down. I know it is my fault that this terrible storm has come on you.'",
            "T": "'Pick me up and throw me into the sea,' Jonah told them, 'and it will go calm. I know this violent storm has come because of me.'"
        },
        "13": {
            "L": "Nevertheless the men rowed hard to get back to dry land, but they could not, for the sea grew more and more tempestuous against them.",
            "M": "Instead, the men rowed hard trying to reach shore, but they could not, for the sea was surging against them.",
            "T": "The sailors tried to row for shore—they didn't want his blood on their hands—but the sea heaved against them and they made no headway."
        },
        "14": {
            "L": "Therefore they called out to the LORD, 'O LORD, let us not perish for this man's life, and lay not on us innocent blood, for you, O LORD, have done as it pleased you.'",
            "M": "Then they cried out to the LORD: 'Please, LORD, do not let us die for taking this man's life. Do not hold us guilty of innocent blood, for you, LORD, have done as you saw fit.'",
            "T": "So they cried out to Yahweh: 'LORD, please—do not let us perish for this man's life. Do not hold innocent blood against us. You, Yahweh, have done what you willed.'"
        },
        "15": {
            "L": "So they picked up Jonah and hurled him into the sea, and the sea ceased from its raging.",
            "M": "Then they picked up Jonah and threw him into the sea, and the sea stopped raging.",
            "T": "They lifted Jonah and threw him into the sea—and at once the raging stopped."
        },
        "16": {
            "L": "Then the men feared the LORD exceedingly, and they offered a sacrifice to the LORD and made vows.",
            "M": "The men were filled with deep reverence for the LORD, and they offered a sacrifice to him and made vows.",
            "T": "The sailors were filled with awe before Yahweh. They offered him a sacrifice and made vows to him."
        },
        "17": {
            "L": "And the LORD appointed a great fish to swallow up Jonah. And Jonah was in the belly of the fish three days and three nights.",
            "M": "But the LORD appointed a great fish to swallow Jonah, and Jonah was inside the fish three days and three nights.",
            "T": "Yahweh had appointed a great fish to swallow Jonah—and Jonah was in the fish's belly three days and three nights."
        }
    },
    "2": {
        "1": {
            "L": "Then Jonah prayed to the LORD his God from the belly of the fish,",
            "M": "From inside the fish, Jonah prayed to the LORD his God.",
            "T": "From inside the fish's belly, Jonah prayed to Yahweh his God."
        },
        "2": {
            "L": "saying, 'I called out to the LORD, out of my distress, and he answered me; out of the belly of Sheol I cried, and you heard my voice.'",
            "M": "He said: 'In my distress I called to the LORD, and he answered me. From the depths of Sheol I cried for help, and you heard my voice.'",
            "T": "He said:\nIn my anguish I called to Yahweh—\nand he answered me.\nFrom the depths of Sheol I cried out,\nand you heard my voice."
        },
        "3": {
            "L": "'For you cast me into the deep, into the heart of the seas, and the flood surrounded me; all your waves and your billows passed over me.'",
            "M": "'You hurled me into the deep, into the very heart of the seas; the current surrounded me, and all your waves and breakers swept over me.'",
            "T": "You threw me into the deep—\ninto the heart of the seas;\nthe current swept around me,\nall your waves and breakers crashing over me."
        },
        "4": {
            "L": "'Then I said, I am driven away from your sight; yet I shall again look toward your holy temple.'",
            "M": "'I thought I had been banished from your presence; yet I will look again toward your holy temple.'",
            "T": "I thought: I am cut off from your sight.\nYet I will look again\ntoward your holy temple."
        },
        "5": {
            "L": "'The waters closed in over me to take my life; the deep surrounded me; weeds were wrapped about my head.'",
            "M": "'The water closed in over me to the point of death; the depths wrapped around me; seaweed was tangled about my head.'",
            "T": "The waters closed over me—threatening my very life;\nthe depths surrounded me;\nseaweed wrapped around my head."
        },
        "6": {
            "L": "'At the roots of the mountains I went down; the earth with her bars closed upon me forever; yet you brought up my life from the pit, O LORD my God.'",
            "M": "'I sank to the roots of the mountains; the earth with its bars shut me in forever. But you, LORD my God, brought my life up from the grave.'",
            "T": "I sank to the roots of the mountains;\nthe gates of the earth closed behind me—\na prison forever.\nBut you, Yahweh my God, brought my life up from the pit."
        },
        "7": {
            "L": "'When my life was fainting away, I remembered the LORD, and my prayer came to you, into your holy temple.'",
            "M": "'As my life was ebbing away, I remembered the LORD, and my prayer reached you in your holy temple.'",
            "T": "When my breath was fading,\nI remembered Yahweh—\nand my prayer reached you,\ninto your holy temple."
        },
        "8": {
            "L": "'Those who pay regard to worthless idols forsake their steadfast love.'",
            "M": "'Those who cling to worthless idols forfeit the steadfast love that could have been theirs.'",
            "T": "Those who cling to hollow idols\nwalk away from the mercy that could have been theirs."
        },
        "9": {
            "L": "'But I with the voice of thanksgiving will sacrifice to you; what I have vowed I will pay. Salvation belongs to the LORD!'",
            "M": "'But I will bring a sacrifice of thanksgiving to you; I will fulfill every vow I made. Salvation comes from the LORD.'",
            "T": "But I—I will worship you with a shout of thanks;\nI will keep every vow I made.\nDeliverance belongs to Yahweh!"
        },
        "10": {
            "L": "And the LORD spoke to the fish, and it vomited Jonah out upon the dry land.",
            "M": "Then the LORD commanded the fish, and it vomited Jonah onto dry land.",
            "T": "Yahweh spoke to the fish—and it heaved Jonah up onto dry ground."
        }
    },
    "3": {
        "1": {
            "L": "Then the word of the LORD came to Jonah the second time, saying,",
            "M": "The word of the LORD came to Jonah a second time:",
            "T": "Yahweh's word came to Jonah a second time:"
        },
        "2": {
            "L": "'Arise, go to Nineveh, that great city, and call out against it the message that I tell you.'",
            "M": "'Get up and go to Nineveh, that great city, and proclaim to it the message I give you.'",
            "T": "'Get up. Go to Nineveh—that great city—and declare the message I will give you.'"
        },
        "3": {
            "L": "So Jonah arose and went to Nineveh, according to the word of the LORD. Now Nineveh was an exceedingly great city, three days' journey in breadth.",
            "M": "So Jonah went to Nineveh, just as the LORD had commanded. Now Nineveh was an enormously large city—it took three days to walk through.",
            "T": "Jonah got up and went to Nineveh, just as Yahweh had said. Nineveh was a vast city—three days' journey across."
        },
        "4": {
            "L": "Jonah began to go into the city, going a day's journey. And he called out, 'Yet forty days, and Nineveh shall be overthrown!'",
            "M": "On the first day, Jonah went into the city and proclaimed, 'Forty more days and Nineveh will be overthrown!'",
            "T": "After one day's walk into the city, Jonah proclaimed: 'Forty days—and Nineveh is finished!'"
        },
        "5": {
            "L": "And the people of Nineveh believed God. They called for a fast and put on sackcloth, from the greatest of them to the least of them.",
            "M": "The people of Nineveh believed God. They proclaimed a fast and put on sackcloth—from the greatest to the least.",
            "T": "The Ninevites believed God. They proclaimed a fast and put on sackcloth—every person, from the greatest to the least."
        },
        "6": {
            "L": "The word reached the king of Nineveh, and he arose from his throne, removed his robe, covered himself with sackcloth, and sat in ashes.",
            "M": "When the news reached the king of Nineveh, he rose from his throne, took off his royal robe, covered himself with sackcloth, and sat in the dust.",
            "T": "Word reached the king of Nineveh. He rose from his throne, stripped off his royal robe, put on sackcloth, and sat in the ash heap."
        },
        "7": {
            "L": "And he issued a proclamation and published it through Nineveh: 'By the decree of the king and his nobles: Let neither man nor beast, herd nor flock, taste anything. Let them not feed or drink water.'",
            "M": "He then issued a proclamation throughout Nineveh: 'By order of the king and his officials: No person or animal, no herd or flock, is to eat or drink anything.'",
            "T": "He issued a decree through Nineveh: 'By royal command—no person or animal, no cattle or sheep, shall eat or drink anything.'"
        },
        "8": {
            "L": "'But let man and beast be covered with sackcloth, and let them call out mightily to God. Let every one turn from his evil way and from the violence that is in his hands.'",
            "M": "'Let people and animals be covered with sackcloth. Let everyone call urgently on God. Let each person turn from their evil ways and from the violence they have committed.'",
            "T": "'Let humans and animals alike wear sackcloth and cry out to God with everything they have. Let every person turn from their wicked ways and from the violence on their hands.'"
        },
        "9": {
            "L": "'Who knows? God may turn and relent and turn from his fierce anger, so that we may not perish.'",
            "M": "'Who knows? God may yet relent and turn from his fierce anger, and we will not die.'",
            "T": "'Who knows—perhaps God will turn and relent, pulling back his fierce anger, and we will not perish.'"
        },
        "10": {
            "L": "When God saw what they did, how they turned from their evil way, God relented of the disaster that he had said he would do to them, and he did not do it.",
            "M": "When God saw what they did—how they had turned from their evil ways—he relented and did not bring on them the disaster he had threatened.",
            "T": "God saw their actions—they had genuinely turned from their evil ways—and he relented. He did not bring the judgment he had announced."
        }
    },
    "4": {
        "1": {
            "L": "But it was greatly displeasing to Jonah, and he was angry.",
            "M": "But this greatly displeased Jonah, and he became angry.",
            "T": "Jonah was furious. This was the last thing he had wanted."
        },
        "2": {
            "L": "And he prayed to the LORD and said, 'O LORD, is not this what I said when I was yet in my country? That is why I made haste to flee to Tarshish; for I knew that you are a gracious God and merciful, slow to anger and abounding in steadfast love, and relenting from disaster.'",
            "M": "He prayed to the LORD: 'LORD, isn't this exactly what I said before I left home? That is why I ran to Tarshish in the first place. I knew you were a gracious and compassionate God, slow to anger and overflowing with steadfast love—a God who relents from disaster.'",
            "T": "He prayed to Yahweh: 'This is exactly what I said back home, Yahweh—why I fled to Tarshish in the first place. I knew who you were: gracious and compassionate, slow to anger, overflowing with loyal love, a God who turns back from disaster. I knew you would do this.'"
        },
        "3": {
            "L": "'Therefore now, O LORD, please take my life from me, for it is better for me to die than to live.'",
            "M": "'So now, LORD, please take my life—it would be better for me to die than to live.'",
            "T": "'So take me now, Yahweh. Death is better than watching this.'"
        },
        "4": {
            "L": "And the LORD said, 'Do you do well to be angry?'",
            "M": "But the LORD replied, 'Is it right for you to be angry?'",
            "T": "Yahweh answered him: 'Is your anger really justified?'"
        },
        "5": {
            "L": "Jonah went out of the city and sat to the east of the city and made a booth for himself there. He sat under it in the shade, till he should see what would become of the city.",
            "M": "Jonah left the city and sat down east of it. He built himself a shelter there and sat in its shade to see what would happen to the city.",
            "T": "Jonah stalked out of the city and sat east of it. He built himself a lean-to for shade and settled in to watch—waiting to see what would happen to Nineveh."
        },
        "6": {
            "L": "Now the LORD God appointed a plant and made it grow up over Jonah, to be shade over his head, to save him from his discomfort. So Jonah was exceedingly glad because of the plant.",
            "M": "Then the LORD God provided a leafy plant and made it grow up over Jonah to give shade for his head and to ease his discomfort. Jonah was overjoyed about the plant.",
            "T": "Yahweh God caused a large leafy plant to grow up over Jonah's head—shelter from the sun, relief from his misery. Jonah was delighted with it."
        },
        "7": {
            "L": "But when dawn came up the next day, God appointed a worm that attacked the plant, so that it withered.",
            "M": "But at dawn the next day God sent a worm that chewed through the plant, and it withered.",
            "T": "But at sunrise the next morning, God sent a worm to gnaw through the plant's stem, and it withered."
        },
        "8": {
            "L": "When the sun rose, God appointed a scorching east wind, and the sun beat down on the head of Jonah so that he was faint. And he asked that he might die and said, 'It is better for me to die than to live.'",
            "M": "When the sun rose, God sent a scorching east wind, and the blazing sun beat down on Jonah's head so that he grew faint. He wanted to die and said, 'It would be better for me to die than to live.'",
            "T": "Then God sent a searing east wind, and the sun hammered down on Jonah's bare head until he nearly collapsed. He begged to die: 'Death is better than this life.'"
        },
        "9": {
            "L": "But God said to Jonah, 'Do you do well to be angry for the plant?' And he said, 'Yes, I do well to be angry, angry enough to die.'",
            "M": "But God said to Jonah, 'Is it right for you to be angry about the plant?' 'Yes,' he said, 'it is right—I am angry enough to die.'",
            "T": "God asked Jonah: 'Is your anger over the plant really justified?' Jonah snapped back: 'Yes—justified enough to die over it.'"
        },
        "10": {
            "L": "And the LORD said, 'You pity the plant, for which you did not labor, nor did you make it grow, which came into being in a night and perished in a night.'",
            "M": "But the LORD said, 'You are concerned about a plant that you did not tend or cultivate—it appeared overnight and died overnight.'",
            "T": "Then Yahweh said: 'You feel sorry for a plant you never planted, never watered—it sprang up overnight and was gone in a night.'"
        },
        "11": {
            "L": "'And should not I pity Nineveh, that great city, in which there are more than 120,000 persons who do not know their right hand from their left, and also much cattle?'",
            "M": "'And should I not be concerned about Nineveh, that great city, in which there are more than 120,000 people who cannot tell right from wrong—and so many animals as well?'",
            "T": "'And should I not care about Nineveh—that great city—with more than a hundred and twenty thousand people who cannot tell right from wrong? And all the animals besides?'"
        }
    }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jonah')
        merge_tier(existing, JONAH, tier_key)
        save(tier_dir, 'jonah', existing)
    print('Jonah 1–4 written.')

if __name__ == '__main__':
    main()
