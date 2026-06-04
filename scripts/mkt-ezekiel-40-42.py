"""
MKT Ezekiel chapters 40–42 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-40-42.py

=== CHAPTER OVERVIEW ===

Chapters 40–42 form the opening of the "New Temple Vision" (chs. 40–48), the climactic
section of Ezekiel's book. After the oracles of judgment (chs. 1–32) and the oracles of
restoration (chs. 33–39), the prophet receives a comprehensive vision of the rebuilt temple
that will house God's returning glory. The measuring angel surveys every gate, court, wall,
and chamber with mathematical precision — this is not accident but theological intent:
God's new dwelling is ordered, complete, and already designed before Israel returns from exile.

Chapter 40 — The Outer and Inner Gates and Courts
  vv. 1–4:   Date, transport-vision to Israel, introduction of the measuring angel
  vv. 5–16:  The outer east gate: seven-step approach, six guardrooms (three per side),
              vestibule, posts, recessed windows, palm-tree motifs
  vv. 17–19: The outer court: thirty chambers, lower pavement, 100-cubit span
  vv. 20–27: North and south outer gates (same dimensions as east gate)
  vv. 28–37: Inner south, east, and north gates (8-step approach; vestibules face outer court)
  vv. 38–46: Chambers for sacrifice preparation, singers' chambers, priests of Zadok
  vv. 47–49: Inner court (100×100 cubits), altar before the house, the temple vestibule

Chapter 41 — The Temple Building Interior
  vv. 1–4:   The nave (Holy Place) and inner sanctuary (Holy of Holies)
  vv. 5–11:  Three-tiered side chambers around the temple; winding stairway; open space
  vv. 12–15: The separate yard (גִּזְרָה) and overall 100-cubit measurements
  vv. 16–20: Interior woodwork — paneling from floor to windows, cherubim and palm trees
  vv. 21–26: The squared doorposts; the wooden altar table; double doors; vestibule canopy

Chapter 42 — The Priests' Chambers and Overall Enclosure
  vv. 1–12:  North and south priests' chambers: three-story galleries facing the separate
              yard and pavement; internal corridor; dimensions matched to the nave
  vv. 13–14: Function of the chambers — eating the most holy offerings; garment protocol
  vv. 15–20: Final perimeter measurement: 500 reeds on all four sides; the enclosing wall
              that "makes a separation between the holy and the common"

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה): "LORD" in L/M (small-caps convention). "Yahweh" in T — especially at
  40:1 (hand of the LORD), 40:46 (come near to the LORD), 41:22 (table before the LORD),
  and 42:13 (approach the LORD). Consistent with all prior Ezekiel scripts.

- H430 (אֱלֹהִים / God): Used only at 40:2 ("visions of God"). L/M: "God." T: "God."
  No special decision; grammatically plural but context = singular divine vision.

- H7307 (רוּחַ / spirit, wind, breath, side/direction): This word appears in Ezekiel 42:16–20
  NOT as "spirit" but in its Hebrew idiom meaning "side / direction" (compass quarter).
  The four occurrences refer to the east side, north side, south side, west side.
  L/M/T: "side" in all tiers for all four occurrences. Do not render as "spirit" here.
  This is a documented deviation from the usual "spirit/Spirit" rendering — the context
  (five-hundred-reed measurement on each compass quarter) makes the direction-sense certain.
  Documented so future agents do not incorrectly import the spiritual-sense rendering here.

- H6944 (קֹדֶשׁ / holy / holy place): 41:4 — "This is the Most Holy Place" (קֹדֶשׁ
  הַקֳּדָשִׁים, the doubled superlative). L: "holy of holies." M: "Most Holy Place." T:
  "the Holy of Holies" or equivalent.
  42:13 — "most holy offerings" and "holy chamber" — context-sensitive rendering throughout.

- H352 (אַיִל / doorpost, pilaster, post): The architectural term for the structural pier or
  jamb flanking a gateway. L: "post" (source-accurate but technical). M: "doorpost."
  T: "doorpost" or "pilaster" where the architectural sense is being surfaced.

- H197 (אוּלָם / vestibule, porch, portico): The covered entry chamber of a gate or building.
  L/M: "vestibule" consistently. T: "vestibule" or "entry porch" depending on context.

- H8372 (תָּא / alcove, guardroom, side room): The flanking chambers inside the gate passage.
  L: "alcove." M: "guardroom." T: "guardroom" — these are the flanking watch-rooms of the gate.

- H361 (אֵלַמָּה / portico, arch, colonnade): The arched or colonnaded section of the gate.
  L/M/T: "portico." Some translations use "vestibule" but that is reserved for H197.

- H1508 (גִּזְרָה / separate yard, separate place): The open area between the temple building
  proper and the outer enclosing wall to the west and sides. L: "separate place." M/T:
  "separate yard." This is a technical term for the buffer zone around the temple building.

- H6763 (צֵלָע / side chamber): The three-tiered lateral rooms built around the temple walls.
  L/M/T: "side chamber." Distinct from H3957 (לִשְׁכָּה / chamber, room) which are the
  free-standing chambers in the outer courts.

- H8561 (תִּמֹרָה / palm tree): Decorative palm-tree motifs carved on walls, doorposts, and
  doors throughout the temple. L/M/T: "palm tree." This Eden motif is consistent in Ezekiel's
  temple and echoes 1 Kgs 6–7 (Solomon's temple paneling).

- H3742 (כְּרוּב / cherub): The composite angelic figures carved on the interior walls and
  doors. L/M/T: "cherub/cherubim." Each cherub had two faces — human and lion (41:18–19),
  contrasting with the four-faced living creatures of ch. 1 and 10.

- Zadok (H6659, צָדוֹק): The priestly lineage that remained faithful when others apostasized
  (cf. Ezek 44:15). 40:46 names them as those who "come near to the LORD to minister."
  L/M: "sons of Zadok." T surfaces their faithfulness as the theological reason for their
  privileged altar-service assignment.

- "Hand of the LORD" idiom (40:1): The standard phrase for prophetic transport (H3027 + H3068).
  L: "the hand of the LORD was upon me." M: "the hand of the LORD came upon me." T: makes
  the divine compulsion explicit.

- H520 (אַמָּה / cubit): The standard unit of measurement. In 40:5 the "long cubit" is a
  cubit + a handbreadth (= ~52 cm vs. ~45 cm). L/M: "cubit." T notes the "long cubit"
  specification at 40:5 since it affects all subsequent measurements.

- H7070 (קָנֶה / reed, measuring reed): The six-cubit measuring staff. L/M: "reed." T uses
  "measuring reed" to distinguish the instrument from the plant.

- Recognition formula (absent in chs. 40–42): The "you shall know that I am the LORD" formula
  characteristic of earlier Ezekiel oracles does not appear in the temple-vision chapters.
  These chapters are measurement and description, not judgment or promise oracles.

=== ASPECT / TENSE NOTES ===

- The predominant verbal mood in chs. 40–42 is wayyiqtol (waw-consecutive imperfect), the
  standard Hebrew narrative past. L/M/T: simple past throughout ("he measured," "he brought").
  The vision is narrated as a completed event, not an ongoing process.

- Chapter 40:4 has imperatives — "look," "hear," "set your heart." These are direct commands
  to Ezekiel and all three tiers preserve the imperative force.

- 42:13–14 contains imperfect verbs for priestly duties: "shall eat," "shall lay," "must not
  go out." These describe permanent institutional regulations. L: "shall." M/T: "shall/must."

=== OT INTERTEXTUALITY ===

- 40:1–2: The transport-vision to "a very high mountain" echoes Sinai (Ex 19, 24) where Moses
  received the tabernacle pattern. Compare also Isa 2:2 / Mic 4:1 ("the mountain of the LORD's
  house shall be established as the highest mountain"). T surfaces the Sinai echo at 40:2.

- 40:2: The angel as measuring figure echoes Zech 2:1–2 and Rev 11:1; 21:15–16. The visionary
  measuring of sacred space is a recurring prophetic motif.

- 40:16, 26, 31, 34, 37; 41:18, 20, 25, 26: Palm tree motifs throughout echo Solomon's temple
  (1 Kgs 6:29, 32, 35) and ultimately Eden (Gen 2–3). The restored temple is a restored garden.

- 41:18–19: Cherubim with human and lion faces — compare ch. 1 (four faces each) and ch. 10
  (full cherub vision). The temple carving simplifies to the human and lion pair, perhaps
  marking the transition from the frightening living-creatures vision to the ordered sanctuary.

- 41:22: "The table that is before the LORD" — the altar of incense / table of bread in the
  Holy Place. Compare Ex 25:23–30 (table of showbread), 30:1–10 (incense altar). The term
  "table before the LORD" conflates both functions here.

- 42:20: The final wall "making a separation between the holy and the common" (H914, בָּדַל,
  the verb used at creation for God's act of separating, Gen 1:4, 6, 7, 14) ties the temple's
  perimeter wall to the cosmic act of creation-separation. T surfaces this echo.

- The entire temple vision (chs. 40–48) is the OT background for Rev 21–22 (New Jerusalem).
  The 500-reed perimeter (42:15–20) and the river of life (47) are taken up in Revelation's
  vision of the city of God.
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
  "40": {
    "1": {
      "L": "In the twenty-fifth year of our captivity, at the beginning of the year, on the tenth day of the month, in the fourteenth year after the city was struck — on that very day the hand of the LORD was upon me and he brought me there.",
      "M": "In the twenty-fifth year of our exile, at the start of the year, on the tenth of the month, fourteen years after the city had fallen — on that very day the hand of the LORD came upon me and brought me there.",
      "T": "Twenty-five years into exile — 573 BC, the tenth of the first month, fourteen years after Jerusalem's fall — the hand of Yahweh seized Ezekiel and carried him away. The vision begins at the deepest point of Israel's loss, in order to show what God has already designed to replace what was destroyed."
    },
    "2": {
      "L": "In the visions of God he brought me into the land of Israel and set me down upon a very high mountain, on which was something like the structure of a city toward the south.",
      "M": "In divine visions he brought me to the land of Israel and set me on a very high mountain, on whose southern slope was something resembling a city.",
      "T": "God carries the prophet to Israel in vision and sets him on a towering mountain — the echo of Sinai, where Moses received the tabernacle pattern. The city-like structure to the south is the restored temple complex, shown to Ezekiel before it exists, as God once showed Moses the heavenly blueprint."
    },
    "3": {
      "L": "And he brought me there, and behold, there was a man whose appearance was like the appearance of bronze, with a linen cord and a measuring reed in his hand, standing in the gate.",
      "M": "He brought me there, and I saw a man whose appearance was like gleaming bronze, holding a linen measuring cord and a measuring reed, standing in the gateway.",
      "T": "In the gateway stood a man blazing like polished bronze — an angelic architect carrying a linen cord for long distances and a reed for gate-by-gate precision. His appearance recalls the divine messenger of Ezekiel 1 and anticipates the one in Daniel 10. God's house will be measured to exact, holy specification."
    },
    "4": {
      "L": "And the man said to me, 'Son of man, see with your eyes and hear with your ears, and set your heart upon all that I am showing you, for you were brought here in order that I might show it to you. Declare all that you see to the house of Israel.'",
      "M": "The man said to me, 'Son of man, look with your eyes, hear with your ears, and fix your attention on everything I am showing you — for you were brought here precisely so that I might show it to you. Report everything you see to the house of Israel.'",
      "T": "'Son of man, look, listen, concentrate' — the commission echoes Ezekiel 1 and 2 but with a crucial difference: here the vision is not a theophany of terror but a blueprint of hope. Ezekiel's task is to carry the architectural plans of the future temple back to a people who have no temple. The detailed measurements are the message: while Israel sits in Babylon, God is already designing what comes next."
    },
    "5": {
      "L": "And behold, a wall outside the house all around; and in the man's hand a measuring reed six cubits long, each cubit a cubit and a handbreadth. So he measured the wall's thickness: one reed; and the height: one reed.",
      "M": "There was a wall surrounding the outside of the temple complex. The measuring reed in the man's hand was six long cubits in length, each cubit being a standard cubit plus a handbreadth. He measured the thickness of the wall: one reed; and its height: one reed.",
      "T": "The first measurement is the boundary wall — one reed thick, one reed high (about three meters each way on the long-cubit scale). The massive perimeter wall is the first thing measured because separation is the first principle of this temple: the wall announces what the entire vision is about — the boundary between the holy and the common world."
    },
    "6": {
      "L": "Then he came to the gate that faces toward the east and went up its steps; he measured the threshold of the gate: one reed in depth.",
      "M": "He came to the east-facing gate, climbed its steps, and measured the threshold of the gate: one reed deep.",
      "T": "The vision begins with the east gate — the gate through which God's glory had departed in Ezekiel 10–11, and through which it will return in chapter 43. The measuring of the east gate is therefore the first movement of the restoration: the way is being prepared for the return of the King."
    },
    "7": {
      "L": "The alcoves were one reed long and one reed wide; and between the alcoves five cubits; and the threshold of the gate, from the vestibule of the gate within, one reed.",
      "M": "The guardrooms were each one reed long and one reed wide; the spaces between the guardrooms were five cubits; and the threshold by the gate's inner vestibule was one reed.",
      "T": "Six identical guardrooms — three per side — each a perfect reed-square, flanking the gate passage. Five-cubit gaps between each room allowed movement and passage. The gate is not merely an entrance but a structured corridor through guarded space: one does not stumble carelessly into God's courts."
    },
    "8": {
      "L": "He also measured the porch of the gate within: one reed.",
      "M": "He measured the inner porch of the gate: one reed.",
      "T": "Even the inner vestibule — the transitional threshold between the gate passage and the court — receives its precise measurement. In God's house, every threshold matters; no boundary is left undefined."
    },
    "9": {
      "L": "Then he measured the porch of the gate: eight cubits; and its posts: two cubits; and the porch of the gate was inward.",
      "M": "He measured the gate's entry porch: eight cubits; its doorposts: two cubits. The entry porch faced inward.",
      "T": "Eight cubits for the entry porch — a wide, authoritative threshold — flanked by two-cubit doorposts. The porch opens inward, drawing the worshiper deeper in. The gate architecture is designed not to keep people out but to govern the manner of entry."
    },
    "10": {
      "L": "And the guardrooms of the gate toward the east were three on this side and three on that side — the three were of one measure; and the posts on this side and that side were of one measure.",
      "M": "The guardrooms of the east gate — three on one side, three on the other — were all the same size; the doorposts on either side matched as well.",
      "T": "Six identical guardrooms, perfectly bilateral. The symmetry is a theological statement: God's sanctuary is ordered, not improvised. The equal flanking architecture declares that no side of God's court is an afterthought."
    },
    "11": {
      "L": "He measured the width of the entrance of the gate: ten cubits; and the length of the gate: thirteen cubits.",
      "M": "He measured the width of the gate opening: ten cubits, and the gate passage's total length: thirteen cubits.",
      "T": "Ten cubits wide — ample for the processional movement of worshipers and offerings. Thirteen cubits long — the full depth of the gateway. These are not cramped passages but generous entryways, sized for the dignity of approaching the King."
    },
    "12": {
      "L": "And the boundary space before the guardrooms: one cubit on this side and one cubit on that side; and the guardrooms: six cubits on this side and six cubits on that side.",
      "M": "A low barrier of one cubit stood in front of each guardroom on either side, and each guardroom measured six cubits square.",
      "T": "A one-cubit barrier before each guardroom kept the gateway floor clear for movement. Each room stood six cubits — one full measuring-reed — square. The consistent unit of measurement ties every element of the vision into a single, unified system of sacred proportion."
    },
    "13": {
      "L": "He measured the gate from the ceiling of the one guardroom to the ceiling of the other: breadth twenty-five cubits — door opposite door.",
      "M": "He measured the full width of the gate, ceiling to ceiling across the opposite guardrooms: twenty-five cubits, door facing door.",
      "T": "Twenty-five cubits — the internal width at the gate's broadest span. The phrase 'door opposite door' confirms the bilateral symmetry: the guardrooms face each other across the open passage, creating the ordered corridor that every entrant must traverse."
    },
    "14": {
      "L": "He made the posts sixty cubits; and to the post of the court all around the gate.",
      "M": "He made the doorposts sixty cubits high, and the court ran around the gate on every side.",
      "T": "Sixty-cubit doorposts — architectural columns of commanding height — framed the gate against the surrounding court. Their grandeur signaled that the worshiper was entering a space of royal and divine significance."
    },
    "15": {
      "L": "From the face of the entrance gate to the face of the vestibule of the inner gate: fifty cubits.",
      "M": "From the outer face of the gate entrance to the inner face of the gate's vestibule: fifty cubits.",
      "T": "Fifty cubits — the full depth of the gateway complex from its public threshold to its inner vestibule. The worshiper traversed fifty cubits before reaching the court itself: a measured journey, not a sudden arrival. The approach to God is always a traversal of defined, sacred distance."
    },
    "16": {
      "L": "And recessed windows to the guardrooms and to their posts within the gate all around, and likewise to the vestibules — windows all around within — and upon the posts: palm trees.",
      "M": "There were recessed windows facing inward in the guardrooms and their doorposts, and in the vestibules as well — windows all around the interior. Palm trees adorned each doorpost.",
      "T": "Recessed windows — narrow on the outside, wider within — filled the gate interior with light without exposing the sacred space. Palm trees carved on every doorpost announced the recurring Eden motif: to enter this gate is to approach the garden of God's presence. The tree of life stands at every threshold."
    },
    "17": {
      "L": "Then he brought me into the outer court, and behold, there were chambers and a pavement made for the court all around — thirty chambers alongside the pavement.",
      "M": "He brought me into the outer court; I saw chambers arranged all around and a pavement running the circuit, with thirty chambers fronting the pavement.",
      "T": "The outer court: a paved expanse ringed by thirty chambers — ten per side — where Israel gathered. This is the place of the assembly, the zone open to the whole people. The pavement is the common ground; the chambers serve the needs of pilgrims, Levites, and worship functions. Everyone may stand here, though not all may advance."
    },
    "18": {
      "L": "And the pavement alongside the gates, corresponding to the length of the gates — this was the lower pavement.",
      "M": "The pavement ran alongside the gates, matching their length; this was called the lower pavement.",
      "T": "The 'lower pavement' — so named because the inner court is elevated — runs parallel to the gate structures. The graduated elevation of the courts encodes a spatial theology: outer/lower, inner/higher, most holy/highest. Approach to God is also an ascent."
    },
    "19": {
      "L": "Then he measured the width from the front of the lower gate to the outside of the inner court: a hundred cubits eastward and northward.",
      "M": "He measured the distance from the front of the lower outer gate to the exterior of the inner court: a hundred cubits on the east and a hundred cubits on the north.",
      "T": "One hundred cubits — the span of the outer court on each measured side. This hundred-cubit interval between outer and inner courts is the architectural expression of graded holiness: the outer court welcomes all, but the inner court admits only those who draw nearer to God's presence."
    },
    "20": {
      "L": "And the gate of the outer court that faced north — he measured its length and its width.",
      "M": "He then measured the length and width of the north-facing gate of the outer court.",
      "T": "The measuring angel now moves systematically to the north outer gate. The comprehensive survey of all gates and courts communicates that the entire perimeter of God's house is equally ordered: no gate is neglected, no approach is left approximate."
    },
    "21": {
      "L": "Its guardrooms were three on this side and three on that side; and its posts and its vestibules were according to the measure of the first gate — fifty cubits its length and twenty-five cubits its breadth.",
      "M": "The guardrooms — three on each side — and its doorposts and vestibule matched the first gate's dimensions: fifty cubits long, twenty-five cubits wide.",
      "T": "The north gate is identical to the east gate in every proportion. Uniformity is the point: no gate of God's house is more or less significant than another. Access is equally ordered from every direction."
    },
    "22": {
      "L": "And its windows and its vestibule and its palm trees were after the measure of the gate that faces the east; and they went up by seven steps, and its vestibule was before them.",
      "M": "Its windows, vestibule, and palm trees matched the dimensions of the east gate; seven steps led up to it, with the vestibule in front.",
      "T": "Seven steps — the number of completeness — ascending to every outer gate. The approach is liturgical: seven steps is a movement through fullness before arrival. Palm trees at the vestibule mark the threshold as a garden passage. The identical motifs of every gate signal that there is one God whose house is approached from everywhere with the same honor."
    },
    "23": {
      "L": "And the gate of the inner court was opposite the gate on the north and opposite the gate on the east; and he measured from gate to gate: a hundred cubits.",
      "M": "The inner court had gates directly opposite the north and east outer gates; the measured distance from outer gate to inner gate was a hundred cubits.",
      "T": "Inner gates aligned with outer gates — axial corridors ran from each outer gate through the outer court to the corresponding inner gate. These sightlines directed the worshiper: you could look from the street straight through to the inner sanctuary. The approach to God has both direction and destination."
    },
    "24": {
      "L": "Then he led me toward the south, and behold, there was a gate toward the south; and he measured its posts and its vestibule according to these same measurements.",
      "M": "He led me southward, where I saw a south gate; its doorposts and vestibule were measured according to the same standard.",
      "T": "South, north, east — all three outer gates receive equal treatment. God's temple is not monumental on one side and modest on another; every direction of approach is equally honored."
    },
    "25": {
      "L": "And it and its vestibule had windows all around, like those other windows — fifty cubits the length and twenty-five cubits the breadth.",
      "M": "It and its vestibule had windows all around, like the other gates, and measured fifty cubits long by twenty-five cubits wide.",
      "T": "The same recessed windows, the same proportions. Repetition in this vision is not monotony — it is the architectural statement that divine order is consistent, thorough, and without exception."
    },
    "26": {
      "L": "And there were seven steps going up to it, and its vestibule was before them; and it had palm trees, one on this side and one on that side, upon its posts.",
      "M": "Seven steps led up to it, the vestibule facing them; palm trees adorned its doorposts, one on each side.",
      "T": "Palm trees on the doorposts of every gate — Eden's signature at every threshold. The seven ascending steps invite the worshiper into a rhythmic, measured approach: each step is a movement upward toward the holy."
    },
    "27": {
      "L": "And there was a gate in the inner court toward the south; and he measured from gate to gate toward the south: a hundred cubits.",
      "M": "There was a south-facing gate in the inner court; he measured a hundred cubits from outer gate to inner gate on the south side.",
      "T": "The three outer-to-inner alignments complete the symmetrical layout: east, north, and south each hold a hundred-cubit span between outer and inner gates. The geometry of the court embodies divine order: measurable, consistent, complete."
    },
    "28": {
      "L": "Then he brought me to the inner court by the south gate; and he measured the south gate according to these same measurements.",
      "M": "He brought me through the south gate into the inner court and measured the south gate; its measurements were the same as all the others.",
      "T": "Passing through the south gate into the inner court, the prophet now stands in the elevated, more restricted zone of holiness. The same beautiful proportions govern this gate as governed the outer gates — but the space it opens onto is reserved, set apart, one step closer to the presence of God."
    },
    "29": {
      "L": "And its guardrooms and its posts and its vestibule were according to these same measurements; and it and its vestibule had windows all around — fifty cubits the length and twenty-five cubits the breadth.",
      "M": "Its guardrooms, doorposts, and vestibule matched the standard dimensions; it and its vestibule had windows all around — fifty cubits long, twenty-five cubits wide.",
      "T": "The inner gates replicate the outer gates in every detail. Continuity of form at a deeper level of holiness: the same pattern, the same proportions, the same palm trees and windows — but now within the inner court."
    },
    "30": {
      "L": "And there were vestibules all around: twenty-five cubits length and five cubits breadth.",
      "M": "The vestibules around the gates were twenty-five cubits long and five cubits wide.",
      "T": "A consistent portico system flanked every gate — twenty-five by five cubits, creating a sheltered transitional space at every threshold. In God's house, every crossing point is ceremonially marked."
    },
    "31": {
      "L": "Its vestibule faced the outer court; and palm trees were on its posts; and its stairway had eight steps.",
      "M": "Its vestibule faced the outer court, with palm trees adorning its doorposts; its stairway had eight steps.",
      "T": "The inner gates face outward — their vestibules look back toward the outer court, welcoming the ascending worshiper. Eight steps (one beyond the outer gates' seven) mark the inner gates as a higher ascent: the approach to the inner court costs an additional step of devotion."
    },
    "32": {
      "L": "And he brought me to the inner court toward the east; and he measured the gate according to these same measurements.",
      "M": "He brought me to the east side of the inner court and measured the east inner gate; it matched the standard dimensions.",
      "T": "The east inner gate — the culminating threshold on the axis that leads directly to the temple building. The measuring angel is drawing in toward the center: outer east gate, outer court, inner east gate, inner court, temple porch."
    },
    "33": {
      "L": "And its guardrooms and its posts and its vestibule were according to these same measurements; and it and its vestibule had windows all around — fifty cubits the length and twenty-five cubits the breadth.",
      "M": "Its guardrooms, doorposts, and vestibule matched the same standard dimensions; it and its vestibule had windows all around — fifty cubits long, twenty-five cubits wide.",
      "T": "The repetition of measurements throughout this chapter is itself a theological act: God's order is consistent through every level of the approach. The text's insistence on identical proportions is not poor editing — it is the architectural liturgy of a God who does all things in proportion and completeness."
    },
    "34": {
      "L": "And its vestibule faced the outer court; and it had palm trees on its posts on this side and on that side; and its stairway had eight steps.",
      "M": "Its vestibule faced the outer court, with palm trees on its doorposts on each side; its stairway had eight steps.",
      "T": "Palm trees at every inner gate as at every outer gate — the Eden imagery is relentless. The garden of God surrounds every threshold. Eight steps at every inner gate: the full ascent, one step beyond the outer gates, marking the advance into holier territory."
    },
    "35": {
      "L": "And he brought me to the north gate and measured it — according to these same measurements.",
      "M": "He brought me to the north inner gate and measured it; it was the same as all the others.",
      "T": "The north inner gate — the sixth and final gate of the systematic survey. The angel has now measured every gate: three outer, three inner, all identical. The comprehensive survey declares that no gate is afterthought, no entry is accidental."
    },
    "36": {
      "L": "Its guardrooms, its posts, and its vestibule — and it had windows all around: fifty cubits length and twenty-five cubits breadth.",
      "M": "Its guardrooms, doorposts, and vestibule all measured the same; windows ran around all sides — fifty cubits long and twenty-five cubits wide.",
      "T": "The last gate's measurements complete what has been true throughout: perfect regularity. The vision is almost mathematical in its insistence — and that precision is itself the revelation. God's house is not improvised; it is designed."
    },
    "37": {
      "L": "And its vestibule faced the outer court; and it had palm trees on its posts on this side and on that side; and its stairway had eight steps.",
      "M": "Its vestibule faced the outer court, with palm trees on its doorposts on each side; its stairway had eight steps.",
      "T": "Eight steps, palm trees, outward-facing vestibule — every inner gate ends with the same signature. The motifs form a unified language: Eden imagery (palm trees), ordered ascent (eight steps), welcoming orientation (facing the outer court). The six gates speak with one voice."
    },
    "38": {
      "L": "And a chamber with its entrance was beside the posts of the gates — there they washed the burnt offering.",
      "M": "A chamber with its doorway was built beside the inner gate's doorposts, where the burnt offering was washed before presentation.",
      "T": "Practical holiness: beside the inner gate, a preparation chamber for washing the burnt offering before it reached the altar. The temple vision provides not only grand architectural visions but the mundane infrastructure of daily worship — because holiness extends to every act of preparation, not only to the culminating moment of sacrifice."
    },
    "39": {
      "L": "And in the vestibule of the gate were two tables on this side and two tables on that side, on which they slaughtered the burnt offering, the sin offering, and the guilt offering.",
      "M": "In the gate's vestibule, two tables stood on each side — four in total — on which the burnt offering, sin offering, and guilt offering were slaughtered.",
      "T": "Four tables in the gate vestibule — the burnt offering (total consecration to God), the sin offering (atonement for unintentional transgression), the guilt offering (reparation for breach of covenant). All three major sacrifice types are prepared here, at the threshold between outer and inner court. The entire sacrificial system is concentrated at this gateway."
    },
    "40": {
      "L": "And at the outer side of the porch as one goes up to the entrance of the north gate: two tables on this side and two tables on that side at the porch of the gate.",
      "M": "On the outside, beside the porch at the entrance of the north gate, two tables stood on each side of the gate porch.",
      "T": "The preparation tables extend even to the exterior side of the inner gate vestibule — two more on each side, accessible from the outer court. The architecture of worship is thoroughly provisioned: no part of the sacrificial process is left without its assigned place."
    },
    "41": {
      "L": "Four tables on this side and four tables on that side at the side of the gate: eight tables in all on which they slaughtered.",
      "M": "Four tables on each side of the gate — eight tables in total — on which the sacrificial animals were slaughtered.",
      "T": "Eight tables for slaughter — a bilateral, complete arrangement. Eight: one beyond the fullness of seven, the number of new beginning. The new temple's worship begins with thorough provision for sacrifice, because atonement is the foundation on which all approach to God rests."
    },
    "42": {
      "L": "And the four tables of hewn stone for the burnt offering were a cubit and a half long, a cubit and a half wide, and one cubit high — on them they laid the instruments with which they slaughtered the burnt offering and the sacrifice.",
      "M": "The four tables for the burnt offering were of cut stone, each one and a half cubits long, a cubit and a half wide, and one cubit high. On them were laid the implements used for slaughtering the burnt offering and the sacrifice.",
      "T": "Hewn stone — not wood, which absorbs blood, but durable, washable stone — for the sacrifice tables. One cubit high: working height, ergonomically designed for the priest to stand and prepare. One and a half cubits each way: proportioned for the work. Even the tools of slaughter had their assigned resting place on these tables. Holiness is not vague; it governs the details."
    },
    "43": {
      "L": "And double hooks, a handbreadth long, were fastened within, all around; and upon the tables was the flesh of the offering.",
      "M": "Double hooks, a handbreadth long, were fastened all around the inside walls, and the flesh of the offerings rested on the tables.",
      "T": "Hooks on the interior walls held carcasses for butchering; the tables received the cut portions for presentation. The vision provides for the full ritual workflow from slaughter to offering — every functional detail assigned its place, every act of preparation structured within the sacred order."
    },
    "44": {
      "L": "And outside the inner gate were the chambers of the singers in the inner court: one beside the north gate facing south, and one beside the south gate facing north.",
      "M": "Outside the inner gate in the inner court were chambers for the singers: one beside the north inner gate facing south, and one beside the south inner gate facing north.",
      "T": "The singers — Levitical musicians — have their own chambers built into the inner court architecture, positioned to face each other across the open space. Song is not peripheral to this temple; it is built in. The restored worship of God includes music, art, and voice as structural elements, not ornaments."
    },
    "45": {
      "L": "And he said to me, 'This chamber that faces south is for the priests who keep the charge of the house.'",
      "M": "He said to me, 'This south-facing chamber is for the priests who are responsible for the care of the temple.'",
      "T": "The angel interprets the architecture: the south-facing priests' chamber (watching the approach from the south) belongs to those who guard and maintain the sanctuary itself. Priestly ministry includes not only sacrifice but the daily work of keeping the house of God in order — custodianship as a sacred vocation."
    },
    "46": {
      "L": "And the chamber that faces north is for the priests who keep the charge of the altar. These are the sons of Zadok, who from among the sons of Levi come near to the LORD to minister to him.",
      "M": "The north-facing chamber is for the priests who have charge of the altar. These are the sons of Zadok — those Levites who draw near to the LORD to serve him.",
      "T": "'The sons of Zadok' — the priestly family singled out in Ezekiel for their faithfulness when the rest of Israel's priests led the nation into idolatry (44:15). Their reward is built into the very floor plan: the altar-keepers, those who stand closest to Yahweh, are the ones who remained loyal when loyalty was costly. The temple vision rewards faithfulness with nearness."
    },
    "47": {
      "L": "So he measured the court: a hundred cubits in length and a hundred cubits in breadth, a square; and the altar was before the house.",
      "M": "He measured the inner court: a hundred cubits long and a hundred cubits wide — a perfect square. The altar stood in front of the temple.",
      "T": "The inner court is a perfect square: a hundred by a hundred cubits — the number of fullness and completeness in a bounded space. The altar stands 'before the house,' on the axis between the inner gate and the temple entrance. This is where heaven and earth meet in sacrifice: the geographic and theological center of the entire vision."
    },
    "48": {
      "L": "Then he brought me to the vestibule of the house and measured each post of the vestibule: five cubits on this side and five cubits on that side; and the breadth of the gate was three cubits on this side and three cubits on that side.",
      "M": "He brought me to the temple vestibule and measured its doorposts: five cubits on each side. The width of the gate passage was three cubits on each side.",
      "T": "The prophet now stands at the threshold of the temple building itself — the outer face of God's house. Five-cubit doorposts flanking a three-cubit-wide passage: narrower than the great outer gates, more intimate, more demanding. The nearer one approaches the presence of God, the more precisely one must orient oneself to enter."
    },
    "49": {
      "L": "The length of the vestibule was twenty cubits and the breadth eleven cubits; and by steps they went up to it; and there were pillars beside the posts, one on this side and one on that side.",
      "M": "The vestibule was twenty cubits long and eleven cubits wide; steps led up to it, and columns flanked the doorposts on either side.",
      "T": "Twenty by eleven cubits — a wide, welcoming approach before the narrow temple door. The flanking columns echo Solomon's famous pillars Jachin and Boaz (1 Kgs 7:21), tying this restored temple to the one it replaces. Steps leading up to the vestibule complete the layered ascent: outer court at ground level, inner court elevated, temple porch elevated further. The worshiper has been climbing the whole time."
    }
  },
  "41": {
    "1": {
      "L": "Then he brought me to the nave and measured the pilasters: six cubits on this side and six cubits on that side — the breadth of the tabernacle.",
      "M": "He brought me to the nave of the temple and measured the doorposts: six cubits wide on each side — that was the width of the tabernacle entrance.",
      "T": "The nave — the Holy Place — is entered through six-cubit doorposts on each side. The word 'tabernacle' (אֹהֶל, tent) echoes here: this permanent stone structure carries the theological heritage of the portable tent where God first dwelt with Israel in the wilderness. The new temple inherits the old sanctuary's meaning."
    },
    "2": {
      "L": "And the breadth of the entrance was ten cubits; and the sides of the entrance were five cubits on this side and five cubits on that side. He measured the length of the nave: forty cubits; and the breadth: twenty cubits.",
      "M": "The entrance was ten cubits wide; the sides of the entrance measured five cubits on each side. He measured the length of the nave: forty cubits; and its breadth: twenty cubits.",
      "T": "Forty cubits long by twenty cubits wide — the nave of the Holy Place. The number forty recurs throughout Israel's sacred history: forty years in the wilderness, forty-day fasts, forty-year reigns. The Holy Place is a room proportioned to the weight of that history. Ten-cubit entrance: wide enough for priests carrying holy implements but not a casual doorway."
    },
    "3": {
      "L": "Then he went inside and measured the post of the entrance: two cubits; and the entrance: six cubits; and the breadth of the entrance: seven cubits.",
      "M": "He went inside and measured the doorpost of the inner entrance: two cubits; the entrance itself: six cubits; and the breadth of the entrance: seven cubits.",
      "T": "The measuring angel enters the Most Holy Place alone — Ezekiel waits at the nave threshold, for only the high priest could enter the innermost room, once a year. Seven cubits: the breadth of the holiest threshold carries the number of divine completeness. The entrance to the Most Holy Place is seven cubits wide."
    },
    "4": {
      "L": "He measured the length: twenty cubits; and the breadth: twenty cubits before the nave. And he said to me, 'This is the Most Holy Place.'",
      "M": "He measured the inner room's length: twenty cubits; and its breadth: twenty cubits — the room in front of the nave. He said to me, 'This is the Most Holy Place.'",
      "T": "'This is the Most Holy Place' — a perfect cube: twenty by twenty cubits. As Solomon's Holy of Holies was a perfect cube of twenty cubits (1 Kgs 6:20), this room maintains that sacred geometry. A cube in Scripture is the shape of completeness: in Revelation 21, the New Jerusalem is also a cube. The Most Holy Place is the architectural center of the cosmos where God's presence dwells."
    },
    "5": {
      "L": "Then he measured the wall of the house: six cubits; and the breadth of the side chambers: four cubits all around the house.",
      "M": "He measured the wall of the temple: six cubits thick; and the side chambers surrounding the temple: four cubits wide, all around.",
      "T": "Six-cubit walls for the temple building — massive, permanent, secure. The four-cubit side chambers built around the exterior of the walls provided structural buttressing and storage. The temple is not a thin-walled pavilion but a fortified treasury of the holy."
    },
    "6": {
      "L": "And the side chambers were three stories one over another, thirty in each story; they entered into the wall of the house for the side chambers all around, so that they would have a hold, but they did not have a hold in the wall of the house.",
      "M": "The side chambers were arranged in three tiers, thirty to each tier. They set into the offsets of the temple wall all around so that they could be supported — but they were not fastened into the main temple wall itself.",
      "T": "Ninety side chambers in three tiers, thirty per story — an enormous storage and service infrastructure surrounding the temple. Built into the wall offsets rather than the wall itself, they were structurally attached but not structurally dependent: the temple's integrity was independent of its annexed chambers, just as the holiness of God's presence is not dependent on the structures that serve it."
    },
    "7": {
      "L": "The side chambers widened as they rose — the winding passage around the house went upward and upward; therefore the house was wider at the top. So from the lowest story they went up to the highest through the middle story.",
      "M": "The side chambers grew wider as they rose, because the winding stairway around the temple went upward and the temple was broader above; so one ascended from the lowest story to the highest by way of the middle.",
      "T": "The tiered side chambers widened at each level — an architectural inversion of what one might expect. The temple building broadened upward, and the chambers grew with it. The winding stairway spiraling upward through the three stories carried worshipers and priests through a literally ascending journey: everything in this temple moves upward toward the holy."
    },
    "8": {
      "L": "I saw also the height of the house all around: the foundations of the side chambers were a full reed — six cubits — to the joints.",
      "M": "I also saw the height of the temple complex all around: the foundations of the side chambers rose to a full reed, six cubits high.",
      "T": "The platform on which the entire temple stood was elevated one full reed above the surrounding terrain. The house of God sat literally higher than the world around it. Physical elevation expressed spiritual elevation: the temple was the highest point — architecturally and theologically — in restored Israel."
    },
    "9": {
      "L": "The thickness of the wall for the side chambers was five cubits; and the free space between the side chambers of the house and the chambers of the court was twenty cubits wide all around the house.",
      "M": "The outer wall of the side chambers was five cubits thick, and the open space between the temple's side chambers and the outer buildings was twenty cubits wide, circling the temple.",
      "T": "Twenty cubits of open space surrounded the temple on all sides between the side chambers and the outer courts — a buffer zone of light and air that separated the temple proper from everything else. Even the space around the Most Holy was ordered, measured, and maintained as sacred distance."
    },
    "10": {
      "L": "And between the chambers was a width of twenty cubits all around the house on every side.",
      "M": "Between the chambers and the house was a twenty-cubit width all around on every side.",
      "T": "The twenty-cubit open space recurs on every side — a consistent moat of separation around the temple. No structure pressed against the walls of the house of God; it stood alone in its own measured space."
    },
    "11": {
      "L": "And the doors of the side chambers were toward the free space — one door toward the north and one door toward the south; and the breadth of the free space was five cubits all around.",
      "M": "The doors of the side chambers opened into the free space: one door facing north, another facing south; and the free space was five cubits wide all around.",
      "T": "The side chambers opened not toward the temple wall but toward the open space — their doors faced north and south, giving access to the lateral service corridors. Five cubits: a narrow but navigable passage, sufficient for priestly movement and supply."
    },
    "12": {
      "L": "The building facing the separate yard on the west side was seventy cubits wide; the wall of the building was five cubits thick all around; and its length was ninety cubits.",
      "M": "The building that faced the separate yard on the west side was seventy cubits wide; its walls were five cubits thick on every side; and it was ninety cubits long.",
      "T": "The large western building — facing the 'separate yard' (the buffer zone between temple and outer wall) — was ninety by seventy cubits with five-cubit walls. Its function is not identified here; it lies behind the temple, west of the Most Holy Place, in the most restricted zone of the complex. Its scale suggests a significant but unnamed sacred purpose."
    },
    "13": {
      "L": "So he measured the house: a hundred cubits long; and the separate yard and the building with its walls: a hundred cubits long.",
      "M": "He measured the temple: a hundred cubits long. The separate yard and the western building with its walls also measured a hundred cubits.",
      "T": "The temple and the adjacent western complex both span a hundred cubits — the east-west axis of the entire sacred precinct measures in hundreds. The hundred-cubit module structures the entire temple plan, just as the inner court measured a hundred by a hundred cubits."
    },
    "14": {
      "L": "Also the breadth of the face of the house and of the separate yard toward the east: a hundred cubits.",
      "M": "The width of the temple's front face and the separate yard on the east side was also a hundred cubits.",
      "T": "East, west, north, south — in every direction, the dimensions of the temple complex resolve into consistent hundreds. The architectural plan is not accidental but deliberately proportioned to a hundred-cubit module, declaring the completeness and finality of God's design."
    },
    "15": {
      "L": "He measured the length of the building facing the separate yard that was behind it, and its galleries on this side and on that side: a hundred cubits. And the inner nave and the vestibules of the court —",
      "M": "He measured the length of the western building, facing the separate yard behind the temple, along with its galleries on each side: a hundred cubits. This included the inner nave and the vestibules of the court.",
      "T": "A final hundred-cubit confirmation: the building behind the temple, including its flanking galleries, matched the master module. The inner nave and court vestibules are named here in a summary reference — everything has been measured, everything fits."
    },
    "16": {
      "L": "The thresholds and the recessed windows and the galleries all around their three stories opposite the threshold were paneled with wood all around — from the ground to the windows, and the windows were covered.",
      "M": "The thresholds, recessed windows, and galleries — all three stories facing the threshold — were paneled with wood throughout, from floor to windows, and the windows were covered.",
      "T": "The interior surfaces of the temple were entirely wood-paneled — thresholds, windows, all three levels of the galleries. Wood covered the stone walls, creating warmth and resonance inside the house of God. The windows were covered (perhaps with lattice or screen), filtering light into the interior with controlled dignity."
    },
    "17": {
      "L": "To above the doorway, and to the inner room, and on the outside, and on all the walls all around, inside and outside — by measure.",
      "M": "Above the doorway, in the inner room, and on the outside, and on all the walls inside and out — all was measured and paneled.",
      "T": "Every surface — above every door, the inner sanctuary walls, all exterior faces — received paneling, and every panel was measured. 'By measure' is the refrain of this vision: nothing in God's house is eyeballed or approximated. Precision in materials, precision in dimensions, precision in finish."
    },
    "18": {
      "L": "And it was made with cherubim and palm trees — a palm tree between cherub and cherub — and each cherub had two faces.",
      "M": "The paneling was carved with cherubim and palm trees: a palm tree between each pair of cherubim, and each cherub had two faces.",
      "T": "Cherubim alternating with palm trees covered every paneled wall — a single image of Eden's guardians and Eden's garden woven together. Every surface declared the same thing: you are standing in the presence of the Holy One, in the garden of God, guarded by his heavenly attendants."
    },
    "19": {
      "L": "A human face toward the palm tree on one side, and the face of a young lion toward the palm tree on the other side. It was carved throughout the whole house all around.",
      "M": "Each cherub had a human face toward the palm tree on one side and the face of a young lion toward the palm tree on the other side — carved throughout the entire temple.",
      "T": "Two-faced cherubim — human and lion. Not the fearsome four-faced creatures of Ezekiel 1 and 10, but a domesticated, decorative pair: wisdom (human) and authority (lion). The temple's carvings distill the cherubim to their two most human-facing aspects, appropriate for the space where God dwells with his redeemed people."
    },
    "20": {
      "L": "From the ground to above the door were cherubim and palm trees carved on the wall.",
      "M": "From floor to above the doors, the walls were carved with cherubim and palm trees.",
      "T": "Floor to ceiling, Eden motifs. No inch of the wall left plain. The worshiper entering the Holy Place was surrounded on all sides by the imagery of the garden and its guardians — standing, in a sense, inside the very boundary of paradise that human sin had closed."
    },
    "21": {
      "L": "The doorposts of the nave were squared; and the face of the sanctuary — the appearance was as the appearance of the other.",
      "M": "The doorposts of the nave were squared, and the appearance of the sanctuary's face matched that of the nave.",
      "T": "Squared doorposts — the precise, clean lines of a perfectly crafted threshold. The symmetry between nave and sanctuary confirmed that the two inner rooms shared a unified aesthetic: one architectural language spoke from nave to Most Holy Place, from the outer approach to the innermost chamber."
    },
    "22": {
      "L": "The altar was of wood — three cubits high and two cubits long — with its corners, its base, and its walls of wood. And he said to me, 'This is the table that is before the LORD.'",
      "M": "There was a wooden altar, three cubits high and two cubits long, with its corners, base, and walls all of wood. He said to me, 'This is the table that stands before the LORD.'",
      "T": "The wooden altar in the Holy Place — called here 'the table before the LORD,' combining the incense altar and the table of showbread. Wood, not stone or bronze: the table of intimate presentation, not the altar of consuming fire. This table stands before the divine presence in the innermost accessible room. 'Before the LORD' — the phrase used for the table of bread in the tabernacle (Ex 25:30). The continual offering of bread and incense is maintained in the restored temple."
    },
    "23": {
      "L": "And the nave and the sanctuary had each two doors.",
      "M": "The nave and the Holy Place each had double doors.",
      "T": "Double doors for both the nave and the Most Holy Place — pairs of doors, as in Solomon's temple (1 Kgs 6:31–35), adding solemnity to each threshold. A single door can be pushed open carelessly; double doors require intention."
    },
    "24": {
      "L": "And the double doors had two leaves each — two swinging leaves for the one door and two swinging leaves for the other.",
      "M": "Each double door had two leaves — two swinging panels for each door.",
      "T": "Four panels in total, two for each doorway — each panel turning on its own hinge, each requiring its own deliberate opening. The layered, multiplied thresholds of the temple make every entry a conscious act, every passage an intentional crossing."
    },
    "25": {
      "L": "And there were carved on them — on the doors of the nave — cherubim and palm trees, like those carved on the walls; and there was a wooden canopy on the face of the vestibule on the outside.",
      "M": "The doors of the nave were carved with cherubim and palm trees, matching the carvings on the walls. A canopy of thick wooden planks covered the outside of the vestibule.",
      "T": "Cherubim and palm trees followed the worshiper even to the doors — the Eden motif carved into every surface that divides sacred space. The wooden canopy over the outer vestibule provided both shelter and architectural dignity: entering the temple was sheltered passage, not exposure."
    },
    "26": {
      "L": "And there were recessed windows and palm trees on each side, on the sidewalls of the vestibule and on the side chambers of the house and on the canopy beams.",
      "M": "Recessed windows and palm trees adorned both sidewalls of the vestibule and the side chambers of the house and the canopy beams.",
      "T": "Palm trees and recessed windows everywhere — down to the canopy beams and sidewalls of the vestibule. The Eden imagery was not reserved for the holiest rooms; it extended to every surface that framed the approach. God's house is a unified whole: from the perimeter wall to the canopy beam, every element proclaimed the same sacred reality."
    }
  },
  "42": {
    "1": {
      "L": "Then he brought me out into the outer court, the way toward the north, and he led me into the chamber that was over against the separate yard and over against the building toward the north.",
      "M": "He led me out into the outer court toward the north and brought me to the chambers that faced the separate yard and the building on the north side.",
      "T": "The measuring angel now turns to the northern priests' chambers — the functional infrastructure of the temple complex. Chapter 42 closes the architectural survey by showing where the priests will live and work: adjacent to the separate yard, in chambers that maintain both practicality and holiness."
    },
    "2": {
      "L": "Before the length of a hundred cubits was the north door; and the breadth was fifty cubits.",
      "M": "The building's length facing north was a hundred cubits, and its breadth fifty cubits.",
      "T": "A hundred-cubit length by fifty-cubit breadth — the chamber complex matches the hundred-cubit module that governs the entire temple plan. Even the priests' living quarters participate in the sacred geometry."
    },
    "3": {
      "L": "Over against the twenty cubits of the inner court and over against the pavement of the outer court was gallery against gallery in three stories.",
      "M": "Opposite the twenty-cubit space of the inner court and opposite the pavement of the outer court, balconies ran in three stories facing each other.",
      "T": "Three stories of galleries ran between the inner court's twenty-cubit buffer and the outer court's pavement — tiered balconies creating a visual and spatial bridge between the two zones of the court. The priests who served in both courts could inhabit the space between them."
    },
    "4": {
      "L": "And before the chambers was a passageway of ten cubits breadth inward, a way of one cubit; and their doors were toward the north.",
      "M": "In front of the chambers, a passageway ran along the inside, ten cubits wide and a hundred cubits long, with the chamber doors facing north.",
      "T": "A ten-cubit-wide internal corridor ran the full length of the chamber building — a hundred-cubit passage giving access to every room along the north. The doors opened north, away from the sanctuary proper, maintaining the spatial logic that servants do not stand in the way of the One they serve."
    },
    "5": {
      "L": "Now the upper chambers were shorter, for the galleries took away from them more than from the lower and middle chambers of the building.",
      "M": "The upper chambers were shorter than the lower and middle ones, because the balconies ate into more of their space.",
      "T": "A structural necessity: the projecting galleries reduced the floor area of the upper story. The tiered complexity of the chambers reflects both practical engineering and a kind of organic hierarchy — even the priests' quarters have a spatial order, lower and upper, practical and symbolic."
    },
    "6": {
      "L": "For they were in three stories and had no pillars as the pillars of the courts; therefore the building was narrowed more than the lowest and middle from the ground.",
      "M": "Because they were in three stories without pillars like those of the courts, the upper chambers were set back further from the ground than the lower and middle ones.",
      "T": "The chambers had no court pillars to bear their weight — they rose by their own walls, without external columns. The lack of open colonnades meant each story had to be stepped back to distribute weight, creating the tiered profile. Even without the grand colonnade of the outer court, the priests' chambers were solidly built — sufficient, purposeful, unceremonious."
    },
    "7": {
      "L": "And the wall that was without, parallel to the chambers, toward the outer court on the forepart of the chambers — its length was fifty cubits.",
      "M": "The outer wall running parallel to the chambers, facing the outer court on the front side, was fifty cubits long.",
      "T": "A fifty-cubit outer wall defined the edge of the chamber complex facing the outer court. This wall created the visual boundary between the public court and the priestly residential zone — separating where the people gathered from where the servants of the sanctuary lived."
    },
    "8": {
      "L": "For the length of the chambers that were in the outer court was fifty cubits; and behold, before the temple were a hundred cubits.",
      "M": "The chambers facing the outer court were fifty cubits long, while those facing the nave extended to a hundred cubits.",
      "T": "Fifty cubits toward the outer court, a hundred cubits toward the temple — the priests' chambers extended deeper on the sacred side than on the public side. Proximity to the Most Holy shaped even the length of the service rooms."
    },
    "9": {
      "L": "And from under these chambers was the entry on the east side, as one goes into them from the outer court.",
      "M": "Below these chambers, on the east side, was an entrance for going into them from the outer court.",
      "T": "A ground-level entry on the east side — the eastern approach maintained even to the service quarters. One entered the priests' chambers from the outer court, ascending to the inner levels from there: even the service workers moved through the court of assembly before entering their own domain."
    },
    "10": {
      "L": "The chambers were in the thickness of the wall of the court toward the east, over against the separate yard and over against the building.",
      "M": "The chambers on the south side were set into the thickness of the court wall facing east, across from the separate yard and the western building.",
      "T": "The southern priests' chambers mirrored the northern ones, built into the court wall on the east side, facing the separate yard. The architecture maintained strict bilateral symmetry: north and south priests' chambers matched in position and proportion."
    },
    "11": {
      "L": "And the way before them was like the appearance of the chambers that were toward the north — as long as they and as broad as they — and all their exits and their arrangements and their doors were according to those on the north.",
      "M": "The passageway before them was like that of the north chambers — the same length, the same width, the same exits, the same arrangements, and the same doors as those to the north.",
      "T": "North and south chambers were identical — same corridor, same dimensions, same exits, same doors. The bilateral symmetry that governed the gates governed the service quarters as well. In God's house, order extends to every room, every passage, every arrangement."
    },
    "12": {
      "L": "And according to the doors of the chambers that were toward the south was a door at the head of the way, even the way directly before the wall toward the east, as one enters.",
      "M": "Corresponding to the south chamber doors was a door at the top of the passageway — the pathway that ran directly beside the wall on the east — by which one entered.",
      "T": "A door at the head of the south passageway gave access from the east wall corridor. Every entry point was intentional, every passage assigned a direction. The priests could move through a network of corridors and chambers, all mapped and measured, without confusion or improvisation."
    },
    "13": {
      "L": "Then he said to me, 'The north chambers and the south chambers that are before the separate yard — they are holy chambers where the priests who approach the LORD shall eat the most holy offerings. There they shall place the most holy things — the grain offering and the sin offering and the guilt offering — for the place is holy.'",
      "M": "He said to me, 'The north and south chambers facing the separate yard are holy chambers where the priests who approach the LORD shall eat the most holy offerings. There they shall deposit the most holy things — the grain offering, the sin offering, and the guilt offering — for the place is holy.'",
      "T": "'The priests who approach Yahweh' — the defining phrase for the Zadokite priesthood in Ezekiel (43:19; 44:15; 45:4). The holiest portions of every sacrifice — the portions not burned on the altar but eaten by the priests — were consumed here, in these chambers, in the presence of God. The meal of the holy things was itself an act of priestly worship: to eat what is holy is to participate in holiness."
    },
    "14": {
      "L": "'When the priests enter there, they shall not go out from the holy place into the outer court; but there they shall lay their garments in which they minister, for they are holy. They shall put on other garments, and then they shall approach that which is for the people.'",
      "M": "'When the priests enter the holy area, they must not go directly out into the outer court; they must first lay down their ministry garments — for these are holy — and put on other clothes before drawing near to the area designated for the people.'",
      "T": "The garment protocol: priestly vestments were holy — charged with the holiness of the sanctuary — and could not be worn into the common space of the outer court. The priests changed clothes before entering the people's space. The boundary between holy and common was maintained in fabric as well as in stone. Holiness is not ambient; it must be deliberately managed at every transition."
    },
    "15": {
      "L": "Now when he had made an end of measuring the inner house, he brought me out by way of the gate whose prospect is toward the east, and measured it all around.",
      "M": "When he had finished measuring the interior of the temple area, he led me out through the east gate and measured the complex all around.",
      "T": "The interior survey is complete; the measuring angel exits through the east gate — the gate of arrival, the gate of God's returning glory. The final measurements will be the overall dimensions, the grand summary. The east gate frames both the beginning and the end of the survey."
    },
    "16": {
      "L": "He measured the east side with the measuring reed: five hundred reeds by the measuring reed all around.",
      "M": "He measured the east side with the measuring reed: five hundred reeds, measured all around.",
      "T": "Five hundred reeds on the east side — each reed six long cubits, making the enclosure roughly 1,550 meters on a side by the long-cubit calculation. This is not a temple but a city-scale sacred precinct. The vast scale of the final enclosure surpasses anything built in Israel's history and signals that this vision is eschatological: a temple to fit an age of full restoration."
    },
    "17": {
      "L": "He measured the north side: five hundred reeds by the measuring reed all around.",
      "M": "He measured the north side: five hundred reeds by the measuring reed, all around.",
      "T": "North side: five hundred reeds, identical to the east. The measurement is consistent — a perfect square on a massive scale. Nothing in God's restored sanctuary is lopsided or approximate."
    },
    "18": {
      "L": "He measured the south side: five hundred reeds by the measuring reed.",
      "M": "He measured the south side: five hundred reeds by the measuring reed.",
      "T": "South side: five hundred reeds. Three sides measured, all matching. The symmetry of the eschatological temple is absolute — it does not favor any compass direction, any approach, any people. God's house is equally vast on every side."
    },
    "19": {
      "L": "He turned about to the west side and measured: five hundred reeds by the measuring reed.",
      "M": "He turned to the west side and measured: five hundred reeds by the measuring reed.",
      "T": "West side: five hundred reeds. The measuring is complete. Every direction has yielded the same measurement. The enclosure is a perfect square of five hundred reeds — geometrically complete, theologically complete, eschatologically complete."
    },
    "20": {
      "L": "He measured it on the four sides. It had a wall all around — five hundred reeds long and five hundred reeds wide — to make a separation between the holy and the common.",
      "M": "He measured it on all four sides. A wall surrounded the entire complex — five hundred reeds on each side — to make a separation between the holy and the common.",
      "T": "The final verse of the architectural survey gives its purpose in seven words: 'to make a separation between the holy and the common.' The Hebrew verb is בָּדַל — the same word used in Genesis 1 when God separated light from darkness, waters above from waters below. The perimeter wall of the temple is a creation act: the establishment of sacred order over undifferentiated common space. The temple vision ends where Genesis 1 begins — with God's decisive act of separation, the first movement of all creation."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 40–42 written.')

if __name__ == '__main__':
    main()
