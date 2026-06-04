"""
MKT Ezekiel chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-1-3.py

Translation decisions:

- H3068 (יהוה): "LORD" in L/M (standard small-caps convention). "Yahweh" in T at theophanic
  peaks and commissioning moments (1:3, 1:28, 3:12, 3:14, 3:16, 3:22, 3:23), where the
  covenant name's personal weight is the theological point. The vision and the call are
  Yahweh-events, not generic divine-power events.

- H3069 + H136 (אֲדֹנָי יהוה): "Lord GOD" in L/M — following the convention where YHWH is
  rendered GOD when Adonai precedes it (to avoid "Lord LORD"). This is Ezekiel's signature
  divine-address formula, appearing ~200 times. In T: "the Sovereign LORD" to surface the
  double emphasis on authority. Appears in 2:4; 3:11, 27.

- H7307 (רוּחַ): Three distinct senses are present, and must be rendered differently:
  (1) Meteorological — 1:4 "stormy wind" (רוּחַ סְעָרָה). L: "stormy wind" / M: "storm wind" /
      T: "tempest."
  (2) Animating spirit within the creatures — 1:12, 1:20, 1:21 "the spirit of the living
      creature." L: "the spirit" (lowercase, creature-spirit sense) / M: same / T: same.
  (3) Divine Spirit acting on Ezekiel — 2:2; 3:12, 3:14, 3:24. L/M: "the Spirit" (capital) /
      T: "the Spirit" with fuller interpretive phrasing. Greek pneuma and Hebrew ruach share
      this range; context determines; Greek has no caps, but capitalization here is a
      theological signal the T tier makes explicit.

- H2830 (חַשְׁמַל): A hapax of uncertain meaning, appearing only in Ezekiel (1:4, 1:27; 8:2).
  Ancient versions vary: LXX "electrum" (gold-silver alloy), Peshitta "amber," Talmud
  associates it with the cherubic fire. Modern consensus leans toward a gleaming metal or
  alloy. L: "amber" (traditional/KJV, preserving the foreignness of the term). M: "gleaming
  metal." T: "burnished amber-fire" (evoking the combined color-and-light sense). Consistent
  across 1:4 and 1:27.

- H2416 (חַיּוֹת): "living creatures" in all tiers. Later identified as cherubim in ch. 10.
  No need to import "cherubim" here since Ezekiel himself uses that identification
  retrospectively; the T tier may note the fourfold-creation symbolism at 1:10 (human /
  lion / ox / eagle = four orders: reasoning, wild, domestic, avian).

- H1823 / H4758 (דְּמוּת / מַרְאֶה): "likeness / appearance." Ezekiel's deliberate
  theological veiling — "the likeness of the appearance of" rather than "the glory of God"
  directly — is preserved in all tiers. In L the constructions are kept as awkward chains;
  in M they are smoothed while the indirection is kept; in T the indirection is explicitly
  noted in 1:28 where the full formula appears.

- H3519 (כָּבוֹד): "glory" in all tiers. The theophanic glory of the LORD. Not "honor" or
  "weight" but the visible manifestation of divine presence.

- H1121 בֶּן-אָדָם "son of man": This address (used 93 times in Ezekiel) stresses the prophet's
  creaturely humanity before the overwhelming divine presence. L/M: "Son of man." T: "son
  of man" (lowercase in T — the address is not the Danielic/NT "Son of Man" title but a
  Hebrew idiom meaning "human being"). Preserved literally because the contrast with the
  divine glory is the point.

- H5315 (נֶפֶשׁ): "soul" in 3:19, 3:21 where it means Ezekiel's own self / life. L: "soul."
  M: "yourself" (natural English for the reflexive sense). T: same. Not the Greek immortal
  soul; the embodied self is meant.

- H4805 / H4775 (מְרִי / מֶרֶד): "rebellious" — the characteristic accusation against
  Israel in this commissioning section. L/M: "rebellious." T: "defiant" or "rebellious"
  depending on the shade; documented per verse where varied.

- Aspect notes:
  - Ezekiel 1 uses participial and nominal clauses extensively (visionary present) —
    the creatures "have" four faces, "are" gleaming. These are preserved in L/M as
    ongoing descriptions, not past-tense narrative.
  - The waw-consecutive narrative in 1:1 ("and I saw") is classic OT narrative past.
  - Watchman oracle (3:17–21): the casuistic "if ... then" structure is preserved as
    legal-covenant prose in all three tiers.

- OT intertextuality:
  - 1:4 storm from the north echoes Jeremiah's "disaster from the north" oracles
    (Jer 1:14; 4:6) and signals Babylon's direction of approach — not incidental.
  - 1:26–28 throne-vision echoes Isaiah 6 (throne high and lifted up) and Dan 7
    (ancient of days on a throne). Ezekiel's version is the most elaborate.
  - 1:28 rainbow around the glory echoes the Noahic covenant sign (Gen 9:13–16),
    suggesting this theophany extends, not abolishes, covenant relationship.
  - 3:1–3 scroll-eating echoes Jer 15:16 ("your words were found and I ate them");
    T surfaces this in v.3.
  - 3:17–21 watchman theme recurs and is expanded in Ezekiel 33.

- Verse 1:25 note: In the Hebrew the verse reads somewhat abruptly and some commentators
  treat it as a doublet with v.24b. It is preserved as a distinct verse here — the silence
  when the creatures stand is a structural beat before the voice from above.
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
  "1": {
    "1": {
      "L": "Now it came to pass in the thirtieth year, in the fourth month, on the fifth day of the month, as I was among the exiles by the River Chebar, that the heavens were opened and I saw visions of God.",
      "M": "In the thirtieth year, on the fifth day of the fourth month, while I was among the exiles at the River Chebar, the heavens opened and I saw divine visions.",
      "T": "It was the thirtieth year, the fifth day of the fourth month. I was living among the exiles on the banks of the Chebar canal when the sky split open and visions of God poured through."
    },
    "2": {
      "L": "On the fifth day of the month — which was the fifth year of the captivity of King Jehoiachin —",
      "M": "(It was the fifth day of the month, in the fifth year of King Jehoiachin's exile —",
      "T": "That date fell in the fifth year of King Jehoiachin's exile —"
    },
    "3": {
      "L": "the word of the LORD came expressly to Ezekiel the priest, the son of Buzi, in the land of the Chaldeans by the River Chebar; and the hand of the LORD was upon him there.",
      "M": "the word of the LORD came to Ezekiel the priest, son of Buzi, in the land of the Chaldeans by the River Chebar, and the hand of the LORD was upon him there.",
      "T": "when Yahweh's word came with full force to Ezekiel — priest, son of Buzi — in the land of the Chaldeans beside the Chebar canal. The hand of Yahweh rested upon him there."
    },
    "4": {
      "L": "And I looked, and behold, a stormy wind came out of the north, a great cloud with fire flashing continually and brightness all around it, and in the midst of the fire as it were the color of amber.",
      "M": "As I looked, I saw a stormy wind coming from the north — an immense cloud with lightning flashing and brightness all around it, and in the center of the fire something like gleaming metal.",
      "T": "What confronted me was a tempest driving in from the north: an enormous thundercloud seething with lightning, ringed with blinding radiance. At the heart of the fire gleamed something like burnished amber-fire."
    },
    "5": {
      "L": "And from the midst of it came the likeness of four living creatures. And this was their appearance: they had the likeness of a human form.",
      "M": "From the center of the fire came what looked like four living creatures. Their appearance was this: each had a human form.",
      "T": "Out of the storm's blazing core four living beings emerged. They were shaped like humans — and yet nothing like any human creature I had ever seen."
    },
    "6": {
      "L": "And each had four faces, and each of them had four wings.",
      "M": "Each had four faces and four wings.",
      "T": "Each had four faces and four wings."
    },
    "7": {
      "L": "And their legs were straight, and the soles of their feet were like the sole of a calf's foot; and they sparkled like the gleam of burnished bronze.",
      "M": "Their legs were straight, and the soles of their feet were like a calf's hoof, gleaming like polished bronze.",
      "T": "Their legs were straight and rigid, their feet rounded like a calf's hooves, and they shone like burnished bronze — dazzling, relentless."
    },
    "8": {
      "L": "Under their wings on their four sides they had human hands. And their faces and their wings — the four of them each had these.",
      "M": "Under their wings on each of their four sides they had human hands. All four had the same faces and wings.",
      "T": "Beneath each wing on all four sides were human hands. Every creature had the same arrangement of faces and wings — fourfold, perfectly symmetrical."
    },
    "9": {
      "L": "Their wings touched one another. They did not turn when they went; each went straight forward.",
      "M": "Their wings touched those of their neighbors. When they moved, they went straight ahead without turning.",
      "T": "Wingtip to wingtip the creatures were joined. They moved in absolute straight lines — never turning, always direct, a single purposeful motion."
    },
    "10": {
      "L": "As for the likeness of their faces: each had a human face in front; on the right side all four had a lion's face, on the left side all four had an ox's face, and all four had an eagle's face at the back.",
      "M": "As for their faces: each had a human face in front, a lion's face on the right, an ox's face on the left, and an eagle's face at the back.",
      "T": "Four faces apiece: the face of a human looking forward, a lion on the right, an ox on the left, an eagle at the back — commanding all four orders of the living world: the rational, the wild, the domestic, the aerial."
    },
    "11": {
      "L": "Such were their faces. And their wings were spread out above; each had two that touched the wings of another creature, and two that covered their bodies.",
      "M": "Those were their faces. Above, their wings spread outward; two wings touched those of the neighboring creature, and two covered their bodies.",
      "T": "Their wings formed one connected canopy above: two reaching out to meet the neighbors', binding the four into a single moving structure; two more folded down to cover each creature's form."
    },
    "12": {
      "L": "And each went straight forward. Wherever the spirit was to go, they went, without turning as they went.",
      "M": "Each moved straight ahead. Wherever the spirit directed them to go, they went without turning.",
      "T": "They moved in complete unison, straight ahead. Whatever direction the animating spirit within them willed, they went — not a degree of deviation."
    },
    "13": {
      "L": "As for the likeness of the living creatures, their appearance was like burning coals of fire, like the appearance of torches. The fire moved to and fro among the living creatures; the fire was bright, and from the fire went forth lightning.",
      "M": "The creatures had the appearance of burning coals of fire, like blazing torches. Fire moved back and forth among them — it was intense and bright — and lightning flashed from it.",
      "T": "The creatures blazed like live coals, like firebrands hurled into their midst. Flame darted back and forth among them, brilliant and searing, hurling bolts of lightning."
    },
    "14": {
      "L": "And the living creatures darted back and forth like the appearance of a flash of lightning.",
      "M": "And the creatures moved to and fro with the appearance of a lightning flash.",
      "T": "The creatures shot back and forth like lightning — there and gone before the eye could register it."
    },
    "15": {
      "L": "Now as I looked at the living creatures, I saw one wheel on the earth beside the living creatures, one for each of the four of them.",
      "M": "As I watched the living creatures, I saw a wheel on the ground beside each of the four creatures.",
      "T": "While I took in the sight of the living beings, I noticed something further: beside each creature, right on the ground, stood a wheel."
    },
    "16": {
      "L": "The appearance of the wheels and their construction was like the gleam of beryl; all four had the same likeness, their appearance and construction being as it were a wheel within a wheel.",
      "M": "The wheels gleamed like beryl. All four had the same form — in appearance and structure like a wheel intersecting a wheel.",
      "T": "The wheels shone with the pale-green luster of beryl, all four identical in design — each one crossed at its center by another wheel, so the whole mechanism could roll in any direction without turning."
    },
    "17": {
      "L": "When they moved, they went in any of their four directions without turning as they went.",
      "M": "When they moved, they could go in any of the four directions without needing to turn.",
      "T": "They could move instantly in any direction — forward, back, sideways — without pivoting."
    },
    "18": {
      "L": "And their rims were tall and awesome, and the rims of all four were full of eyes all around.",
      "M": "Their rims were high and awe-inspiring, and the rims of all four were covered with eyes all around.",
      "T": "The rims towered and filled me with dread — every inch of them covered with eyes, watching in every direction at once."
    },
    "19": {
      "L": "And when the living creatures went, the wheels went beside them; and when the living creatures were lifted up from the earth, the wheels were lifted up.",
      "M": "When the creatures moved, the wheels moved with them; when the creatures rose from the ground, the wheels rose with them.",
      "T": "Every movement the creatures made, the wheels mirrored: advance, rise, halt — the wheels were inseparable from them."
    },
    "20": {
      "L": "Wherever the spirit was to go, they went, thither was their spirit to go; and the wheels were lifted up alongside them, for the spirit of the living creature was in the wheels.",
      "M": "Wherever the spirit directed them, they went; wherever the spirit was to go, the wheels rose alongside them — for the spirit of the living creature was in the wheels.",
      "T": "The spirit within the creatures directed everything. Where it willed to go, the whole assembly went — and the wheels rose with them, because the same animating spirit that lived in the creatures lived in the wheels."
    },
    "21": {
      "L": "When those went, these went; and when those stood, these stood; and when those were lifted up from the earth, the wheels were lifted up alongside them, for the spirit of the living creature was in the wheels.",
      "M": "When the creatures moved, the wheels moved; when they stood still, the wheels stood still; when they rose from the earth, the wheels rose alongside them — for the spirit of the living creature was in the wheels.",
      "T": "Move — the wheels moved. Stand — the wheels stood. Rise — the wheels rose. One spirit animated both, creatures and wheels indivisible."
    },
    "22": {
      "L": "Over the heads of the living creatures was the likeness of a firmament, awesome and gleaming like ice, spread out over their heads above.",
      "M": "Spread out above the heads of the creatures was the likeness of a firmament, gleaming like crystal, awesome in its appearance.",
      "T": "Above the creatures' heads stretched a vast expanse — crystal-clear, brilliant, terrible, like a dome of frozen sky arching over them."
    },
    "23": {
      "L": "And under the firmament their wings were stretched out straight, one toward another. And each had two that covered their bodies on either side.",
      "M": "Under the firmament their wings were spread straight out, touching those of the neighboring creature. Each creature also had two wings covering its body on either side.",
      "T": "Under the crystal vault the creatures' outstretched wings reached toward each other; two more wings folded down on each side to cover their forms."
    },
    "24": {
      "L": "And when they went, I heard the sound of their wings like the sound of many waters, like the thunder of the Almighty, a sound of tumult like the sound of a great army. When they stood still, they let down their wings.",
      "M": "When they moved, I heard the sound of their wings like the roar of many waters, like the voice of the Almighty, a great rumbling like the noise of an army. When they stood still, they lowered their wings.",
      "T": "When they moved, the sound was overwhelming — the ocean in full roar, the thunder of the Almighty, the din of a vast army all at once. When they halted, the wings folded into silence."
    },
    "25": {
      "L": "And there came a voice from above the firmament that was over their heads. When they stood still, they let down their wings.",
      "M": "Then a voice came from above the firmament over their heads. When they stood still, they lowered their wings.",
      "T": "A voice descended from beyond the crystal vault high above. The creatures stilled themselves, lowering their wings — listening."
    },
    "26": {
      "L": "And above the firmament over their heads was the likeness of a throne, in appearance like sapphire stone; and seated above the likeness of the throne was the likeness of a human appearance.",
      "M": "Above the firmament over their heads was what looked like a throne, with the appearance of sapphire stone. And above the likeness of the throne was a form with a human appearance.",
      "T": "Above the crystal vault rose something like a throne of sapphire. And upon the throne — the likeness of a form that looked like a human being."
    },
    "27": {
      "L": "And I saw what appeared to be gleaming metal, like the appearance of fire all around within it, from what appeared to be his loins and upward; and from what appeared to be his loins and downward I saw what appeared to be fire, with brightness all around.",
      "M": "From what appeared to be his waist upward I saw something like gleaming metal — fire enclosed all around. And from what appeared to be his waist downward I saw something like fire, surrounded by radiance.",
      "T": "From the waist up the enthroned figure blazed like burnished amber-fire, as if fire were sealed inside fire. From the waist down, the same fire, ringed with light on every side."
    },
    "28": {
      "L": "Like the appearance of the bow that is in the cloud on a day of rain, so was the appearance of the surrounding brightness. Such was the appearance of the likeness of the glory of the LORD. And when I saw it, I fell on my face and heard the voice of one speaking.",
      "M": "Like the rainbow that appears in the clouds on a rainy day, so was the radiance that surrounded him. Such was the appearance of the likeness of the glory of the LORD. When I saw it, I fell on my face and heard the voice of one speaking.",
      "T": "Around the whole figure the brightness spread like a rainbow on a storm-day — many-colored, diffuse, impossible to fix. This was the appearance of what the glory of Yahweh looks like. The instant I saw it I collapsed face-down. Then I heard a voice."
    }
  },
  "2": {
    "1": {
      "L": "And he said to me, 'Son of man, stand upon your feet, and I will speak with you.'",
      "M": "He said to me, 'Son of man, stand on your feet, and I will speak with you.'",
      "T": "'Stand up, son of man,' the voice said. 'Get on your feet — I have words for you.'"
    },
    "2": {
      "L": "And a spirit entered into me when he spoke to me and set me upon my feet, and I heard him speaking to me.",
      "M": "As he spoke to me, the Spirit entered into me and set me on my feet, and I heard him speaking.",
      "T": "The moment he spoke, the Spirit entered me and lifted me to my feet. Then I could hear him clearly."
    },
    "3": {
      "L": "And he said to me, 'Son of man, I am sending you to the children of Israel, to a nation of rebels who have rebelled against me; they and their fathers have transgressed against me to this very day.'",
      "M": "He said to me, 'Son of man, I am sending you to the Israelites — to nations that have rebelled against me. They and their ancestors have transgressed against me right up to this day.'",
      "T": "'I am sending you,' he said, 'to the people of Israel — a nation in open revolt. Generation after generation, they and their ancestors have defied me, and they have not stopped.'"
    },
    "4": {
      "L": "'The children are impudent and stubborn. I am sending you to them, and you shall say to them, “Thus says the Lord GOD.”'",
      "M": "'They are brazen-faced and stubborn-hearted. I am sending you to them, and you shall say, “Thus says the Lord GOD.”'",
      "T": "'They are shameless and obstinate to the core. You will go to them and open with these words: “This is what the Sovereign LORD declares.”'"
    },
    "5": {
      "L": "'And they, whether they hear or refuse to hear — for they are a rebellious house — will know that a prophet has been among them.'",
      "M": "'Whether they listen or refuse — for they are a rebellious house — they will know that a prophet has been among them.'",
      "T": "'They may hear you or they may not — they are a people of defiance. But this much will stand: when it is over, they will know that a prophet was sent to them.'"
    },
    "6": {
      "L": "'And you, son of man, do not be afraid of them, nor be dismayed at their faces, though they are a rebellious house. Do not be afraid of their words nor be dismayed at their faces, though briers and thorns are with you and you sit among scorpions. Do not be afraid of their words nor be dismayed at their faces, for they are a rebellious house.'",
      "M": "'And you, son of man — do not be afraid of them, or be terrified by their looks, though they are a rebellious house. Do not fear their words or be dismayed at their faces, even if briers and thorns surround you and scorpions are beneath you. Do not be afraid of their words or terrified by their looks, for they are a rebellious house.'",
      "T": "'But you, son of man — do not let their faces frighten you. They will surround you with hostility, thorns and briars underfoot, scorpions in every direction. None of this should shake you. Do not let their rage or contempt move you. They are defiant; you are immovable.'"
    },
    "7": {
      "L": "'But you shall speak my words to them, whether they hear or refuse to hear, for they are most rebellious.'",
      "M": "'You shall speak my words to them, whether they listen or not, for they are utterly rebellious.'",
      "T": "'Your only task is to speak my words — whatever their response. Their stubbornness runs to the bone, but my word must go out.'"
    },
    "8": {
      "L": "'But you, son of man, hear what I say to you: do not be rebellious like that rebellious house. Open your mouth and eat what I give you.'",
      "M": "'But you, son of man — listen to what I tell you. Do not be like that rebellious house. Open your mouth and eat what I give you.'",
      "T": "'Now, son of man, listen to me: do not become like them — defiant, closed, refusing. Open your mouth and receive what I am about to put into it.'"
    },
    "9": {
      "L": "And when I looked, behold, a hand was stretched out to me; and behold, in it was a scroll of a book.",
      "M": "As I looked, a hand stretched out toward me, and in it was a written scroll.",
      "T": "As I looked, a hand reached toward me, holding a scroll."
    },
    "10": {
      "L": "And he spread it before me, and it was written on the front and on the back; and written on it were words of lamentation and mourning and woe.",
      "M": "He unrolled it before me — it had writing on both sides — and on it were lamentations, mourning, and woe.",
      "T": "He unrolled it for me. Both sides were covered in writing: lament, grief, and disaster — the full weight of what was coming, already inscribed."
    }
  },
  "3": {
    "1": {
      "L": "And he said to me, 'Son of man, eat what you find; eat this scroll and go, speak to the house of Israel.'",
      "M": "He said to me, 'Son of man, eat what is before you — eat this scroll, then go and speak to the house of Israel.'",
      "T": "'Son of man, eat what is in front of you,' he said. 'Eat this scroll; then go and carry my word to Israel.'"
    },
    "2": {
      "L": "So I opened my mouth, and he gave me that scroll to eat.",
      "M": "I opened my mouth, and he gave me the scroll to eat.",
      "T": "I opened my mouth, and he placed it on my tongue."
    },
    "3": {
      "L": "And he said to me, 'Son of man, feed your stomach and fill your bowels with this scroll that I give you.' Then I ate it, and it was in my mouth as sweet as honey.",
      "M": "He said to me, 'Son of man, eat this scroll I am giving you and fill your stomach with it.' So I ate it, and in my mouth it was as sweet as honey.",
      "T": "'Son of man, take this scroll deep into yourself — let it fill you completely.' I ate it. It was sweet as honey on my tongue — the word of God, tasted before it was spoken. As Jeremiah had said: your words became my food."
    },
    "4": {
      "L": "And he said to me, 'Son of man, go to the house of Israel and speak my words to them.'",
      "M": "He said to me, 'Son of man, go to the house of Israel and deliver my words to them.'",
      "T": "'Now go,' he said. 'Speak exactly my words to Israel.'"
    },
    "5": {
      "L": "'For you are not being sent to a people of foreign speech and hard language, but to the house of Israel —'",
      "M": "'For you are not being sent to a people of foreign speech and a difficult language, but to the house of Israel —'",
      "T": "'I am not sending you to foreigners whose tongue you cannot follow. You are going to your own people, Israel —'"
    },
    "6": {
      "L": "'— not to many peoples of foreign speech and hard language whose words you cannot understand. Surely, if I sent you to them, they would listen to you.'",
      "M": "'— not to many peoples of unfamiliar speech and difficult language whose words you cannot understand. If I had sent you to them, they would have listened.'",
      "T": "'— not to the far nations with alien tongues. If I had sent you there, they would have heard and heeded. But you go to those who know exactly what I am saying — and choose to refuse.'"
    },
    "7": {
      "L": "'But the house of Israel will not be willing to listen to you, for they are not willing to listen to me; for all the house of Israel are hard of forehead and stubborn of heart.'",
      "M": "'But the house of Israel will not listen to you, because they will not listen to me; for all the house of Israel is hard-headed and stubborn-hearted.'",
      "T": "'Israel will not hear you — because they have refused to hear me. The whole house of Israel has iron in its forehead and stone in its heart.'"
    },
    "8": {
      "L": "'Behold, I have made your face strong against their faces, and your forehead strong against their foreheads.'",
      "M": "'But I have made your face as hard as their faces, and your forehead as hard as their foreheads.'",
      "T": "'So I have matched you to them — forehead against forehead, face against face, hardness meeting hardness.'"
    },
    "9": {
      "L": "'Like adamant, harder than flint, have I made your forehead. Do not fear them, nor be dismayed at their faces, for they are a rebellious house.'",
      "M": "'I have made your forehead like adamant, harder than flint. Do not be afraid of them or dismayed at their looks, for they are a rebellious house.'",
      "T": "'Your forehead is set like diamond — harder than flint. Do not flinch before their contempt. They are rebels; you are my messenger. Those are not the same thing.'"
    },
    "10": {
      "L": "Moreover, he said to me, 'Son of man, all my words that I speak to you, receive in your heart and hear with your ears.'",
      "M": "He said to me, 'Son of man, take all my words into your heart and hear them with your ears.'",
      "T": "'Son of man,' he continued, 'do not just carry my words — let them go down into your heart, not merely past your ears.'"
    },
    "11": {
      "L": "'And go, get yourself to the exiles, to the children of your people, and speak to them and say to them, “Thus says the Lord GOD” — whether they hear or refuse to hear.'",
      "M": "'Then go to the exiles, to your own people. Speak to them and say, “Thus says the Lord GOD” — whether they listen or not.'",
      "T": "'Now go to the exiles — your own people. Stand before them with this oracle: “This is what the Sovereign LORD declares.” Give it whether they want it or not.'"
    },
    "12": {
      "L": "Then the Spirit lifted me up, and I heard behind me a voice of a great rushing: 'Blessed be the glory of the LORD from his place!'",
      "M": "Then the Spirit lifted me up, and behind me I heard a great rumbling sound: 'Blessed be the glory of the LORD from his place!'",
      "T": "The Spirit caught me up. From behind me came a roar of departure — a great thundering rush, and within it a voice of praise: 'Blessed be the glory of Yahweh from his dwelling place!'"
    },
    "13": {
      "L": "— the sound of the wings of the living creatures touching one another, and the sound of the wheels beside them, and the sound of a great rumbling.",
      "M": "It was the sound of the creatures' wings touching each other and the sound of the wheels alongside them, and the noise of a great roar.",
      "T": "The roaring was the sound of wingtip meeting wingtip, the grinding thunder of the wheels, the whole vast apparatus of divine presence lifting off."
    },
    "14": {
      "L": "The Spirit lifted me up and took me, and I went in bitterness, in the heat of my spirit, the hand of the LORD being strong upon me.",
      "M": "The Spirit lifted me up and carried me away. I went in bitterness and grief of spirit, with the hand of the LORD resting powerfully upon me.",
      "T": "The Spirit seized me and swept me away. I went in anguish — bitter and shaken — but Yahweh's hand held me in an irresistible grip."
    },
    "15": {
      "L": "And I came to the exiles at Tel-abib, who were dwelling by the River Chebar, and I sat where they were sitting; and I remained there among them seven days, astonished.",
      "M": "I came to the exiles at Tel-abib, who lived by the River Chebar. I sat where they sat and remained among them for seven days, overwhelmed.",
      "T": "I found the exiles at Tel-abib on the Chebar. I sat down among them exactly where they sat. For seven days I could not move or speak — simply overwhelmed by everything I had seen and been told."
    },
    "16": {
      "L": "And at the end of seven days, the word of the LORD came to me, saying:",
      "M": "At the end of seven days, the word of the LORD came to me:",
      "T": "Seven days of silence. Then the word of Yahweh broke through:"
    },
    "17": {
      "L": "'Son of man, I have made you a watchman for the house of Israel. Whenever you hear a word from my mouth, you shall warn them from me.'",
      "M": "'Son of man, I have made you a watchman for the house of Israel. When you hear a word from my mouth, give them warning from me.'",
      "T": "'Son of man, I am setting you as a watchman over Israel. Every word that comes from my mouth, you carry to them as warning from me.'"
    },
    "18": {
      "L": "'When I say to the wicked, “You shall surely die,” and you do not warn him, nor speak to warn the wicked from his wicked way, in order to save his life — that wicked person shall die in his iniquity, but his blood I will require at your hand.'",
      "M": "'If I say to the wicked, “You will certainly die,” and you give no warning or say nothing to turn him from his evil way to save his life, that wicked person will die for his sin, but I will hold you responsible for his blood.'",
      "T": "'If I sentence the wicked to death and you say nothing — no warning, no call to turn — he dies for his own sin. But his blood I will demand from you.'"
    },
    "19": {
      "L": "'But if you warn the wicked and he does not turn from his wickedness or from his wicked way, he shall die in his iniquity, but you will have delivered your soul.'",
      "M": "'But if you warn the wicked and he does not turn from his wickedness or his wicked way, he will die in his iniquity, but you will have saved yourself.'",
      "T": "'But if you warn him and he refuses to turn, he dies for his own choices. You have done your part — you are clear.'"
    },
    "20": {
      "L": "'When a righteous man turns from his righteousness and commits iniquity, and I place a stumbling block before him, he shall die. Because you did not warn him, he shall die in his sin, and his righteous deeds which he did shall not be remembered; but his blood I will require at your hand.'",
      "M": "'And if a righteous person turns from their righteousness and commits sin, and I place a stumbling block before them, they will die. Because you gave no warning, they will die in their sin, their past righteousness forgotten — and I will hold you accountable for their blood.'",
      "T": "'And if someone righteous abandons their integrity, falls into sin, and I bring a crisis to test them — if you gave no warning, they fall and die, all their earlier faithfulness wiped out. Their blood too falls on you.'"
    },
    "21": {
      "L": "'But if you warn the righteous person not to sin, and he does not sin, he shall surely live because he took warning; and you will have delivered your soul.'",
      "M": "'But if you warn the righteous not to sin, and they heed the warning and do not sin, they will surely live because they took warning — and you will have saved yourself.'",
      "T": "'But if you warn the righteous and they listen and do not sin, they live. And once again — you are clear.'"
    },
    "22": {
      "L": "And the hand of the LORD was upon me there, and he said to me, 'Rise, go out to the valley, and I will speak with you there.'",
      "M": "The hand of the LORD came upon me there, and he said to me, 'Get up and go out to the valley, and I will speak with you there.'",
      "T": "Then Yahweh's hand came upon me again. 'Rise,' he said. 'Go out to the open plain. I will meet you there.'"
    },
    "23": {
      "L": "So I arose and went out to the valley, and behold, the glory of the LORD stood there, like the glory that I had seen by the River Chebar; and I fell on my face.",
      "M": "I got up and went out to the valley. The glory of the LORD was standing there, just like the glory I had seen by the River Chebar, and I fell on my face.",
      "T": "I went out to the plain, and there it was again — the glory of Yahweh, the same overwhelming presence I had seen at the Chebar. I fell to the ground."
    },
    "24": {
      "L": "And the Spirit entered into me and set me on my feet, and he spoke with me and said to me, 'Go, shut yourself within your house.'",
      "M": "The Spirit entered into me and set me on my feet. He spoke to me and said, 'Go into your house and shut yourself inside.'",
      "T": "The Spirit entered me and raised me up again. 'Go home,' he said. 'Lock yourself inside.'"
    },
    "25": {
      "L": "'And you, son of man, behold, cords will be placed on you, and you shall be bound with them, so that you cannot go out among the people.'",
      "M": "'But you, son of man — cords will be put on you, and you will be tied with them so you cannot go out among the people.'",
      "T": "'Son of man, you will be bound with ropes — confined, unable to move freely among the people.'"
    },
    "26": {
      "L": "'And I will make your tongue cling to the roof of your mouth, so that you shall be mute and unable to reprove them, for they are a rebellious house.'",
      "M": "'I will make your tongue stick to the roof of your mouth, and you will be silent — unable to rebuke them — for they are a rebellious house.'",
      "T": "'I will seal your mouth. Your tongue will go still against your palate. You will have no rebuke to deliver, because they are a people who have chosen defiance. The silence is my judgment on their refusal to hear.'"
    },
    "27": {
      "L": "'But when I speak with you, I will open your mouth and you shall say to them, “Thus says the Lord GOD.” He who hears, let him hear; and he who refuses to hear, let him refuse, for they are a rebellious house.'",
      "M": "'But whenever I speak to you, I will open your mouth, and you will say to them, “Thus says the Lord GOD.” Whoever listens, let him listen; and whoever refuses, let him refuse — for they are a rebellious house.'",
      "T": "'But whenever I choose to speak, I will open your mouth and you will deliver my oracle: “This is what the Sovereign LORD declares.” Those who choose to hear will hear; those who refuse will refuse. The choice is theirs — but the word has been given, and they are without excuse.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 1–3 written.')

if __name__ == '__main__':
    main()
