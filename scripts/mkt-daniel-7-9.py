"""
MKT Daniel chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-daniel-7-9.py

=== CHAPTER OVERVIEW ===

Chapter 7 (Aramaic — the Aramaic section Dan 2:4–7:28 ends here):
  The Four Beasts and the Ancient of Days. Daniel's own night vision:
  four monsters from the churning sea, the divine court, the Ancient of Days
  enthroned, and one "like a son of man" who comes on clouds to receive an
  eternal kingdom. Heavenly interpreter explains: four beastly empires, then
  the saints of the Most High receive the kingdom forever.

Chapter 8 (Hebrew — returns to Hebrew after 7:28):
  The Ram and the Goat. A second vision: Media-Persia (two-horned ram),
  Greece (shaggy goat, great horn = Alexander), four successor kingdoms, and
  a fierce little horn (Antiochus IV) who abolishes the daily sacrifice and
  desecrates the sanctuary. Gabriel interprets. 2,300 evenings-mornings.
  Daniel is shattered and ill for days afterward.

Chapter 9 (Hebrew):
  Daniel's penitential prayer and the Seventy Weeks. Daniel reads Jeremiah's
  70-year prophecy and turns to God in sackcloth and ashes, confessing Israel's
  sin with deep communal lament. Gabriel arrives at the evening sacrifice with
  the Seventy Weeks oracle — the most contested chronological prophecy in the OT.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / LORD): Rendered "LORD" (all-caps convention) in L/M throughout.
  T uses "the LORD" or "Yahweh" — in ch. 9's prayer the personal divine name
  occurs repeatedly; T keeps "the LORD" for rhythmic prayer register. Decision:
  no switch to "Yahweh" in these chapters; "the LORD" is sufficiently personal.

- H430 (אֱלֹהִים / God): "God" throughout in all tiers.

- H2617 (חֶסֶד / hesed, "steadfast love"): In Dan 9:4 Daniel addresses God as
  "keeping covenant and steadfast love." L/M: "steadfast love." T: "faithful
  covenant love" or "steadfast love" — keeping the combined loyalty-and-kindness
  sense (no English equivalent; documented in guide §6).

- "Son of man" (Dan 7:13, Aramaic כְּבַר אֱנָשׁ / k'var enash): The most
  theologically significant phrase in the chapter — the human figure who comes
  on clouds and receives eternal sovereignty from the Ancient of Days. Jesus
  applies this title to himself explicitly (Matt 26:64 and parallels). L/M/T all
  render "one like a son of man" — preserving the Aramaic idiom. T notes the
  contrast (beasts from below vs. human from above) but does not substitute
  "Son of God" or "Messiah."

- H5943 (Aramaic עִלַּי / Most High): Rendered "the Most High" in all tiers,
  consistent with chs 4–6.

- H6922 (Aramaic קַדִּישִׁין / holy ones, "saints"): In ch. 7 this refers to
  the people of God, not the polytheistic "holy gods" expression of chs 4–6.
  L/M: "the holy ones." T: "the holy ones of the Most High" in full phrasing.
  Capitalisation: not "Holy Ones" — the Aramaic has no capitals; lowercase
  maintains textual integrity.

- H4899 (מָשִׁיחַ / Mashiach / Anointed One): In Dan 9:25–26, "Messiah the
  Prince" and "Messiah shall be cut off." L/M: "Anointed One" (more literal)
  for the first occurrence; "Messiah" is also used in the header and T. All
  tiers: "Anointed One" in L, "Anointed One" in M, "Messiah" permitted in T
  where it surfaces the theological weight. Note: English "Anointed One" is a
  transparent rendering; "Messiah" is the Hebrew loanword in English tradition.
  Decision: L uses "Anointed One"; M uses "Anointed One"; T uses "Messiah."

- H7620 (שָׁבוּעַ / shabuah / sevens/weeks): The unit in the 70-weeks prophecy.
  Literally "a group of seven" (a heptad). L: "sevens" (preserves the numerical
  ambiguity). M: "weeks" (conventional English translation). T: "sevens" (surfaces
  the unusual unit and resists flattening to the modern-day-week concept).

- H8251/H8074 (שִׁקּוּץ שֹׁמֵם / abomination of desolation): Dan 9:27. All tiers
  retain this language — it is a fixed prophetic terminus technicus referenced by
  Jesus (Matt 24:15). L: "abominations" + "makes desolate." M: "abomination of
  desolation." T: same, with context.

- H2380 (חָזוֹן / chazon / vision): "Vision" throughout; not "prophecy" in L/M.

- "Ancient of Days" (H6268 עַתִּיק יוֹמַיָּא, Aramaic): Established epithet in all
  three tiers. Not paraphrased.

- "Time, times, and half a time" (7:25): Aramaic עִדָּן וְעִדָּנִין וּפְלַג עִדָּן —
  lit. "a time and times and the dividing of a time." L/M/T: "a time, times, and
  half a time" — the conventional rendering; the ambiguity is part of the text.

- Aspect (Aramaic/Hebrew): Narrative perfects treated as completed acts (past in
  L/M, vivid past in T). Imperfects in the angelic interpretations treated as
  ongoing or future. The 70-weeks oracle (9:24-27) is dominated by Niph'al
  perfects with future referent — rendered as future in all tiers.

- "Sanctuary" vs "temple": H4720 (מִקְדָּשׁ) = sanctuary/holy place. L/M: "sanctuary."
  T: "sanctuary" or "temple" depending on context; no change from L/M in these chapters.

- Dan 8:11 "prince of the host": H8269 שַׂר הַצָּבָא — rendered "Prince of the host"
  (L/M) / "Prince of the heavenly host" (T). This is God or his appointed angelic
  commander; the defiance of the little horn against him is the crux of the chapter.

- "Desolating transgression" (8:13 H6588 + H8074): "The transgression that makes
  desolate" in L/M; T: "the desolating rebellion."
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

DANIEL = {
  "7": {
    "1": {
      "L": "In the first year of Belshazzar king of Babylon, Daniel saw a dream and visions of his head upon his bed. Then he wrote down the dream and told the sum of the matters.",
      "M": "In the first year of Belshazzar king of Babylon, Daniel had a dream and visions of his head while lying on his bed. He wrote down the dream and gave the sum of the matters.",
      "T": "In the first year of Belshazzar king of Babylon, Daniel was given a dream—visions sweeping through his sleeping mind. He wrote the dream down and recorded its chief contents."
    },
    "2": {
      "L": "Daniel declared, I saw in my vision by night, and behold, the four winds of the heavens were stirring up the great sea.",
      "M": "Daniel said, 'I saw in my vision by night, and there were the four winds of heaven stirring up the great sea.'",
      "T": "Daniel spoke: 'In my night vision I looked, and all four winds of heaven were churning up the great sea, driving it into chaos.'"
    },
    "3": {
      "L": "And four great beasts came up from the sea, diverse one from another.",
      "M": "And four great beasts came up from the sea, each different from the others.",
      "T": "Out of that churning sea rose four enormous beasts, each unlike the others."
    },
    "4": {
      "L": "The first was like a lion and had eagles' wings. I watched until its wings were plucked off, and it was lifted up from the earth and made to stand on two feet as a man, and a man's heart was given to it.",
      "M": "The first was like a lion and had eagle's wings. I watched until its wings were plucked off and it was lifted up from the ground and set on two feet like a human being, and a human mind was given to it.",
      "T": "The first was lion-like, with eagle's wings—but as I watched, the wings were torn off. It was lifted from the earth and made to stand upright like a human, and a human mind was placed inside it."
    },
    "5": {
      "L": "And behold, another beast, a second one, like a bear. It was raised up on one side; it had three ribs in its mouth between its teeth; and they said to it, Arise, devour much flesh.",
      "M": "Then another beast appeared, a second one, like a bear. It was raised up on one of its sides, and three ribs were in its mouth between its teeth. They said to it, 'Arise, devour much flesh!'",
      "T": "Then came a second beast—like a massive bear, rearing up on one side, three ribs clenched between its teeth. A voice commanded it: 'Arise! Devour much flesh!'"
    },
    "6": {
      "L": "After this I looked, and behold, another, like a leopard, which had upon its back four wings of a fowl; the beast also had four heads; and dominion was given to it.",
      "M": "After this I looked, and there was another beast, like a leopard, with four wings of a bird on its sides. It also had four heads, and dominion was given to it.",
      "T": "Next came a third beast—leopard-like, but with four bird's wings spread across its back. It had four heads, and sovereignty was granted to it."
    },
    "7": {
      "L": "After this I saw in the night visions, and behold, a fourth beast, terrible and dreadful and exceedingly strong. And it had great iron teeth; it devoured and broke in pieces and stamped the residue with its feet. It was different from all the beasts before it, and it had ten horns.",
      "M": "After this I looked in the night visions and there was a fourth beast—terrifying, dreadful, and overwhelmingly strong. It had great iron teeth; it devoured and crushed, and what remained it trampled with its feet. It was different from all the other beasts, and it had ten horns.",
      "T": "Then in my night vision I saw a fourth beast—and nothing could prepare me for it. Dreadful. Overwhelming. Terrifyingly powerful. Its teeth were iron. It devoured, crushed, and ground everything to nothing, then trampled the remains underfoot. Unlike any of the others. It had ten horns."
    },
    "8": {
      "L": "I was considering the horns, and behold, there came up among them another horn, a little one, before which three of the first horns were plucked up by the roots; and behold, in this horn were eyes like the eyes of a man, and a mouth speaking great things.",
      "M": "As I was thinking about the horns, another horn—a small one—came up among them, and three of the first horns were uprooted before it. This horn had eyes like human eyes and a mouth that spoke boastfully.",
      "T": "As I stared at the horns, a smaller horn pushed up among them—and three of the original horns were ripped out to make room for it. This little horn had eyes like a human's and a mouth that boasted without restraint."
    },
    "9": {
      "L": "I watched until thrones were placed, and the Ancient of Days took his seat. His raiment was white as snow, and the hair of his head like pure wool. His throne was of fiery flame; its wheels burning fire.",
      "M": "As I looked, thrones were set in place and the Ancient of Days took his seat. His clothing was white as snow, and the hair of his head was like pure wool. His throne was ablaze with flames, and its wheels were burning fire.",
      "T": "Then thrones were arranged—and the Ancient of Days took his seat. His robes were white as snow, his hair white as washed wool. His throne blazed with fire, its wheels a river of living flame."
    },
    "10": {
      "L": "A stream of fire issued and came out from before him; a thousand thousands served him, and ten thousand times ten thousand stood before him; the judgment was set, and the books were opened.",
      "M": "A river of fire flowed out from before him; thousands upon thousands attended him, and myriads upon myriads stood before him. The court was seated and the books were opened.",
      "T": "A river of fire streamed from his presence. Thousands upon thousands served him; ten thousand times ten thousand stood before him. The court convened. The record books were opened."
    },
    "11": {
      "L": "I watched then because of the sound of the great words that the horn was speaking; I watched until the beast was slain, and its body destroyed and given to the burning flame.",
      "M": "I continued to watch because of the boastful words the horn was speaking. Then the beast was killed and its body destroyed and thrown into the fire.",
      "T": "I kept watching—the horn's monstrous boasting filled my ears. Then the beast was killed. Its body was destroyed and thrown into the flames."
    },
    "12": {
      "L": "As for the rest of the beasts, they had their dominion taken away, yet their lives were prolonged for a season and a time.",
      "M": "As for the rest of the beasts, their dominion was taken away, but their lives were prolonged for a season and a time.",
      "T": "The other beasts also had their power stripped from them—but they were allowed to live on for an appointed season."
    },
    "13": {
      "L": "I saw in the night visions, and behold, with the clouds of heaven there came one like a son of man, and he came to the Ancient of Days and was presented before him.",
      "M": "In my night visions I looked, and there before me was one like a son of man, coming with the clouds of heaven. He came to the Ancient of Days and was led into his presence.",
      "T": "Still watching in the night visions, I saw him: one like a son of man—a human figure—coming on the clouds of heaven. He was brought before the Ancient of Days and presented to him."
    },
    "14": {
      "L": "And there was given to him dominion and glory and a kingdom, that all peoples, nations, and languages should serve him; his dominion is an everlasting dominion, which shall not pass away, and his kingdom one that shall not be destroyed.",
      "M": "He was given authority, glory, and sovereign power. All peoples, nations, and languages worshiped him. His dominion is an everlasting dominion that will never pass away, and his kingdom is one that will never be destroyed.",
      "T": "Then authority, glory, and royal sovereignty were given to him—a kingdom over all peoples, nations, and tongues, and all of them serving him. His is the dominion that does not end, the kingdom that cannot be broken."
    },
    "15": {
      "L": "As for me Daniel, my spirit was troubled in the midst of my body, and the visions of my head troubled me.",
      "M": "As for me, Daniel, my spirit was troubled within me and the visions of my head dismayed me.",
      "T": "As for me, Daniel—I was shaken to my core. The visions had cut through me and left me trembling."
    },
    "16": {
      "L": "I came near unto one of them that stood by, and asked him the truth of all this. So he told me, and made me know the interpretation of the things.",
      "M": "I approached one of those standing nearby and asked him the true meaning of all this. He told me and made known to me the interpretation of these things.",
      "T": "I went to one of those standing near the throne and asked him directly: what does all this mean? He answered and gave me the interpretation."
    },
    "17": {
      "L": "These great beasts, which are four, are four kings, who shall arise out of the earth.",
      "M": "These four great beasts are four kings who will rise from the earth.",
      "T": "The four great beasts represent four kings who will rise up out of the earth."
    },
    "18": {
      "L": "But the holy ones of the Most High shall receive the kingdom, and possess the kingdom for ever, even for ever and ever.",
      "M": "But the holy ones of the Most High will receive the kingdom and will possess it forever—yes, forever and ever.",
      "T": "But the holy ones of the Most High will take possession of the kingdom—and they will hold it forever, through every age that follows."
    },
    "19": {
      "L": "Then I desired to know the truth concerning the fourth beast, which was different from all the others, exceeding dreadful, whose teeth were of iron, and his nails of brass; which devoured, brake in pieces, and stamped the residue with his feet.",
      "M": "Then I wanted to know the truth about the fourth beast, which was different from all the others, exceedingly terrifying, with teeth of iron and claws of bronze, which devoured and crushed and trampled what remained.",
      "T": "But what I most needed to understand was the fourth beast—the one unlike any of the others, the most terrifying of all, with iron teeth and bronze claws that devoured, crushed, and trampled everything left behind."
    },
    "20": {
      "L": "And of the ten horns that were in his head, and of the other which came up, and before whom three fell; even of that horn that had eyes, and a mouth that spake very great things, whose look was more stout than his fellows.",
      "M": "I also wanted to know about the ten horns on its head and the other horn that came up and before which three fell—the horn that had eyes and a mouth that boasted greatly, and that appeared more imposing than its companions.",
      "T": "And especially that horn—the one that came up and uprooted three others, the one with human eyes and a boastful mouth, the one that looked more formidable than all the rest."
    },
    "21": {
      "L": "I beheld, and the same horn made war with the holy ones, and prevailed against them.",
      "M": "As I watched, this horn was waging war against the holy ones and prevailing over them.",
      "T": "I watched as that horn waged open war against the holy ones of God—and for a time, it was winning."
    },
    "22": {
      "L": "Until the Ancient of Days came, and judgment was given to the holy ones of the Most High; and the time came that the holy ones possessed the kingdom.",
      "M": "Until the Ancient of Days came and pronounced judgment in favor of the holy ones of the Most High, and the time arrived for the holy ones to take possession of the kingdom.",
      "T": "Until the Ancient of Days came. Then judgment was rendered in favor of the holy ones. The appointed time arrived, and the holy ones took possession of the kingdom."
    },
    "23": {
      "L": "Thus he said, The fourth beast shall be the fourth kingdom upon earth, which shall be diverse from all kingdoms, and shall devour the whole earth, and shall tread it down, and break it in pieces.",
      "M": "He told me: 'The fourth beast is a fourth kingdom that will appear on earth, different from all the others. It will devour the whole earth, trampling it down and crushing it.'",
      "T": "'The fourth beast,' he said, 'is a fourth kingdom that will arise on earth—unlike any that came before. It will swallow the whole earth, trample it, and shatter it completely.'"
    },
    "24": {
      "L": "And the ten horns out of this kingdom are ten kings that shall arise; and another shall rise after them; and he shall be diverse from the first, and he shall subdue three kings.",
      "M": "The ten horns are ten kings who will arise from this kingdom; after them another king will arise, different from the earlier ones, who will subdue three kings.",
      "T": "'The ten horns are ten kings who will come out of this kingdom. After them another will rise—different from all his predecessors—and he will bring down three kings.'"
    },
    "25": {
      "L": "And he shall speak great words against the most High, and shall wear out the holy ones of the most High, and think to change times and laws; and they shall be given into his hand until a time and times and the dividing of time.",
      "M": "He will speak words against the Most High and will wear down the holy ones of the Most High. He will attempt to change set times and law, and the holy ones will be handed over to him for a time, times, and half a time.",
      "T": "'He will hurl blasphemies against the Most High. He will grind down the holy ones relentlessly. He will try to overturn the sacred calendar and God's law itself. And the holy ones will be handed into his power for a time, and times, and half a time.'"
    },
    "26": {
      "L": "But the judgment shall sit, and they shall take away his dominion, to consume and to destroy it unto the end.",
      "M": "But the court will sit in judgment, and his dominion will be taken away—utterly consumed and destroyed forever.",
      "T": "'Then the divine court will convene. His power will be stripped away—consumed, annihilated, gone forever.'"
    },
    "27": {
      "L": "And the kingdom and the dominion, and the greatness of the kingdoms under the whole heaven, shall be given to the people of the holy ones of the Most High; his kingdom is an everlasting kingdom, and all dominions shall serve and obey him.",
      "M": "Then the sovereignty, power, and greatness of all the kingdoms under heaven will be handed over to the people of the holy ones of the Most High. His kingdom is an everlasting kingdom, and all rulers will worship and obey him.",
      "T": "'And the sovereignty, the power, the greatness of every kingdom under all of heaven—all of it will be given to the people of the holy ones of the Most High. His will be the kingdom that endures forever; every dominion will bow down and obey him.'"
    },
    "28": {
      "L": "Hitherto is the end of the matter. As for me Daniel, my cogitations much troubled me, and my countenance changed in me; but I kept the matter in my heart.",
      "M": "This is the end of the account. As for me, Daniel, my thoughts greatly troubled me and my color changed, but I kept the matter in my heart.",
      "T": "And that is where the account ends. As for me, Daniel—the visions left me deeply shaken. My face drained of color. But I locked all of it within my heart."
    }
  },
  "8": {
    "1": {
      "L": "In the third year of the reign of King Belshazzar a vision appeared to me, even to me Daniel, after that which appeared to me at the first.",
      "M": "In the third year of King Belshazzar's reign, a vision appeared to me, Daniel, after the one that had appeared to me previously.",
      "T": "It was the third year of King Belshazzar's reign when a second vision came to me—Daniel—following the first one I had already received."
    },
    "2": {
      "L": "And I saw in a vision; and it came to pass, when I saw, that I was at Shushan in the palace, which is in the province of Elam; and I saw in a vision, and I was by the river of Ulai.",
      "M": "In the vision I saw myself in Susa, the citadel in the province of Elam. In the vision I was beside the Ulai canal.",
      "T": "In the vision I found myself at Susa—the royal fortress in the province of Elam—standing by the Ulai canal."
    },
    "3": {
      "L": "Then I lifted up mine eyes, and saw, and behold, there stood before the river a ram which had two horns; and the two horns were high; but one was higher than the other, and the higher came up last.",
      "M": "I looked up and saw a ram standing before the canal. It had two horns, and both were high, but one was higher than the other, and the higher one came up last.",
      "T": "I looked up and saw a ram standing by the canal. It had two horns—both impressive, though one rose higher than the other, and that taller horn had grown up after the first."
    },
    "4": {
      "L": "I saw the ram pushing westward, and northward, and southward; so that no beasts might stand before him, neither was there any that could deliver out of his hand; but he did according to his will, and became great.",
      "M": "I saw the ram charging westward, northward, and southward. No animal could stand against him, and no one could rescue from his power. He did as he pleased and became great.",
      "T": "The ram charged westward, northward, southward—unstoppable. No creature could withstand him; nothing could escape his reach. He did whatever he liked, and he grew mighty."
    },
    "5": {
      "L": "And as I was considering, behold, a he-goat came from the west over the face of the whole earth, and touched not the ground; and the goat had a notable horn between his eyes.",
      "M": "While I was thinking about this, suddenly a male goat came from the west across the whole face of the earth, without touching the ground. This goat had a prominent horn between his eyes.",
      "T": "As I pondered all of this, a goat appeared from the west—sweeping across the face of the whole earth at incredible speed, barely touching the ground. Between its eyes jutted a single prominent horn."
    },
    "6": {
      "L": "And he came to the ram that had two horns, which I had seen standing before the river, and ran unto him in the fury of his power.",
      "M": "He approached the ram with the two horns that I had seen standing by the canal, and charged at him with furious force.",
      "T": "He rushed at the two-horned ram I had seen by the canal—charging with unstoppable fury."
    },
    "7": {
      "L": "And I saw him come close unto the ram, and he was moved with choler against him, and smote the ram, and brake his two horns; and there was no power in the ram to stand before him, but he cast him down to the ground, and stamped upon him: and there was none that could deliver the ram out of his hand.",
      "M": "He struck the ram and shattered both his horns. The ram had no strength to resist him; he knocked him to the ground and trampled him. No one could rescue the ram from his power.",
      "T": "He hit the ram with full fury, shattering both horns. The ram was helpless before him—thrown to the ground, trampled. There was nothing anyone could do to save the ram."
    },
    "8": {
      "L": "Therefore the he goat waxed very great; and when he was strong, the great horn was broken; and for it came up four notable ones toward the four winds of heaven.",
      "M": "The male goat became exceedingly great, but at the height of his power the great horn was broken off, and in its place four prominent horns grew up toward the four winds of heaven.",
      "T": "The goat grew enormously powerful—but at the very peak of his strength, the great horn was snapped off. In its place, four prominent horns grew up, pointing toward the four winds of heaven."
    },
    "9": {
      "L": "And out of one of them came forth a little horn, which waxed exceeding great, toward the south, and toward the east, and toward the pleasant land.",
      "M": "Out of one of these four horns came another horn, which started small but grew exceedingly great toward the south, toward the east, and toward the beautiful land.",
      "T": "From one of these four horns there sprouted a small horn—but it grew until it was enormous, spreading southward, eastward, and toward the glorious land."
    },
    "10": {
      "L": "And it waxed great, even to the host of heaven; and it cast down some of the host and of the stars to the ground, and stamped upon them.",
      "M": "It grew great, even to the host of heaven, and some of the host of heaven and some of the stars it hurled to the ground and trampled them.",
      "T": "It grew to challenge heaven itself—casting down some of the starry host to the earth and trampling them underfoot."
    },
    "11": {
      "L": "Yea, he magnified himself even to the prince of the host, and by him the daily sacrifice was taken away, and the place of his sanctuary was cast down.",
      "M": "It magnified itself even against the Prince of the host. The regular burnt offering was taken away, and the site of his sanctuary was thrown down.",
      "T": "It even dared to exalt itself against the Prince of the heavenly host—abolishing the daily sacrifice and desecrating his sanctuary."
    },
    "12": {
      "L": "And an host was given him against the daily sacrifice by reason of transgression, and it cast down the truth to the ground; and it practised, and prospered.",
      "M": "Because of transgression, a host was given over along with the regular offering. Truth was cast to the ground, and the horn acted and prospered.",
      "T": "An army was handed over to it along with the daily offering—as punishment for the people's rebellion. Truth was flung to the ground, and in its defiance the horn thrived."
    },
    "13": {
      "L": "Then I heard one holy one speaking; and another holy one said unto that certain one which spake, How long shall be the vision concerning the daily sacrifice, and the transgression of desolation, to give both the sanctuary and the host to be trodden under foot?",
      "M": "Then I heard a holy one speaking, and another holy one said to the one who spoke, 'How long will the vision last—the regular offering abolished, the transgression that desolates, and the sanctuary and the host given over to be trampled?'",
      "T": "Then I heard a holy being speak, and another asked him: 'How long will this go on? The daily sacrifice stopped, the desolating rebellion unchecked, the sanctuary and the host of God trampled—how long?'"
    },
    "14": {
      "L": "And he said unto me, Unto two thousand and three hundred days; then shall the sanctuary be cleansed.",
      "M": "He said to me, 'For 2,300 evenings and mornings; then the sanctuary will be restored to its rightful state.'",
      "T": "'Two thousand three hundred evenings and mornings,' he answered. 'Then the sanctuary will be set right again.'"
    },
    "15": {
      "L": "And it came to pass, when I, even I Daniel, had seen the vision, and sought for the meaning, then, behold, there stood before me as the appearance of a man.",
      "M": "When I, Daniel, had seen the vision, I was seeking to understand it. Then suddenly there stood before me someone who looked like a man.",
      "T": "As I, Daniel, was watching the vision and trying to grasp its meaning, a figure appeared before me—with the form of a man."
    },
    "16": {
      "L": "And I heard a man's voice between the banks of Ulai, which called, and said, Gabriel, make this man to understand the vision.",
      "M": "I heard a human voice between the banks of the Ulai calling, 'Gabriel, help this man understand the vision.'",
      "T": "Then a voice rang out from between the banks of the Ulai canal: 'Gabriel—make this man understand what he has seen.'"
    },
    "17": {
      "L": "So he came near where I stood: and when he came, I was afraid, and fell upon my face; but he said unto me, Understand, O son of man: for at the time of the end shall be the vision.",
      "M": "He came near to where I stood, and when he approached I was terrified and fell on my face. He said to me, 'Understand, son of man, that the vision pertains to the time of the end.'",
      "T": "He came toward me, and terror swept through me—I fell facedown. But he spoke: 'Understand, son of man: this vision pertains to the time of the end.'"
    },
    "18": {
      "L": "Now as he was speaking with me, I was in a deep sleep on my face toward the ground: but he touched me, and set me upright.",
      "M": "While he was speaking to me, I fell into a deep sleep with my face to the ground. But he touched me and raised me to my feet.",
      "T": "As he spoke, I fell into a deep stupor, face to the ground—but he touched me and set me upright."
    },
    "19": {
      "L": "And he said, Behold, I will make thee know what shall be in the last end of the indignation: for at the time appointed the end shall be.",
      "M": "He said, 'I am going to tell you what will take place in the latter period of the wrath, for it refers to the appointed time of the end.'",
      "T": "'Listen,' he said, 'I am going to show you what will happen at the end of the period of divine wrath—for all of this points to the appointed time of the end.'"
    },
    "20": {
      "L": "The ram which thou sawest having two horns are the kings of Media and Persia.",
      "M": "The ram that you saw with two horns represents the kings of Media and Persia.",
      "T": "'The two-horned ram—that is the kingdom of Media and Persia.'"
    },
    "21": {
      "L": "And the rough goat is the king of Grecia; and the great horn that is between his eyes is the first king.",
      "M": "The shaggy goat is the king of Greece, and the great horn between his eyes is the first king.",
      "T": "'The shaggy goat is the kingdom of Greece. The great horn between its eyes—that is the first king.'"
    },
    "22": {
      "L": "Now that being broken, whereas four stood up for it, four kingdoms shall stand up out of the nation, but not in his power.",
      "M": "The four horns that replaced the one that was broken represent four kingdoms that will arise from that nation, but without the original king's power.",
      "T": "'When that great horn was broken, four kingdoms rose in its place from the same nation—but none of them will have the power the first king had.'"
    },
    "23": {
      "L": "And in the latter time of their kingdom, when the transgressors are come to the full, a king of fierce countenance, and understanding dark sentences, shall stand up.",
      "M": "At the end of their rule, when rebels have reached their limit, a king of bold face, skilled in intrigue, will arise.",
      "T": "'At the end of their reign, when the cup of rebellion has been filled to the brim, a king of brazen face will rise—a master of deceit and cunning.'"
    },
    "24": {
      "L": "And his power shall be mighty, but not by his own power: and he shall destroy wonderfully, and shall prosper, and practise, and shall destroy the mighty and the holy people.",
      "M": "His power will be great, but not from his own strength. He will cause devastating destruction and will succeed in everything he does. He will destroy the powerful and the people of the holy ones.",
      "T": "'His power will be immense—but it does not come from himself. He will achieve appalling destruction. He will prosper in all he does. He will crush the powerful, and he will destroy the holy people of God.'"
    },
    "25": {
      "L": "And through his policy also he shall cause craft to prosper in his hand; and he shall magnify himself in his heart, and by peace shall destroy many: he shall also stand up against the Prince of princes; but he shall be broken without hand.",
      "M": "Through his cunning he will cause deceit to flourish, and he will consider himself great. When they feel most secure, he will destroy many. He will even oppose the Prince of princes—but he will be broken, though not by human hands.",
      "T": "'Through his cleverness he will make deception thrive. His arrogance will swell without limit. When people feel most safe he will strike and destroy many. He will dare to rise up against the Prince of princes—and then he will be shattered, not by any human hand, but by God himself.'"
    },
    "26": {
      "L": "And the vision of the evening and the morning which was told is true: wherefore shut thou up the vision; for it shall be for many days.",
      "M": "The vision of the evenings and mornings that has been told is true. But seal up the vision, for it concerns the distant future.",
      "T": "'The vision of the 2,300 evenings and mornings is true. But seal it away—it speaks of days still far off.'"
    },
    "27": {
      "L": "And I Daniel fainted, and was sick certain days; afterward I rose up, and did the king's business; and I was astonished at the vision, but none understood it.",
      "M": "I, Daniel, was exhausted and ill for several days. Then I got up and carried out the king's business, but I was appalled by the vision and could not understand it.",
      "T": "I was undone. I lay ill for days. Then I pulled myself up and went back to the king's business—but the vision haunted me. Its meaning was beyond my grasp."
    }
  },
  "9": {
    "1": {
      "L": "In the first year of Darius the son of Ahasuerus, of the seed of the Medes, which was made king over the realm of the Chaldeans;",
      "M": "In the first year of Darius son of Ahasuerus, of Median descent, who was appointed king over the realm of the Chaldeans—",
      "T": "In the first year of Darius the Mede, son of Ahasuerus, who had been appointed king over Babylon—"
    },
    "2": {
      "L": "In the first year of his reign I Daniel understood by books the number of the years, whereof the word of the LORD came to Jeremiah the prophet, that he would accomplish seventy years in the desolations of Jerusalem.",
      "M": "in the first year of his reign, I, Daniel, understood from the Scriptures—according to the word of the LORD given to Jeremiah the prophet—that the desolation of Jerusalem would last seventy years.",
      "T": "in the first year of his reign, I, Daniel, was studying the Scriptures. I came to the word the LORD had spoken through Jeremiah the prophet: the desolation of Jerusalem would last seventy years. I began to reckon the time."
    },
    "3": {
      "L": "And I set my face unto the Lord God, to seek by prayer and supplications, with fasting, and sackcloth, and ashes.",
      "M": "Then I turned my face toward the Lord God and devoted myself to prayer and pleading, with fasting, sackcloth, and ashes.",
      "T": "I turned my face toward the Lord God—fully devoted, going before him in prayer and earnest supplication, fasting, wearing sackcloth and sitting in ashes."
    },
    "4": {
      "L": "And I prayed unto the LORD my God, and made my confession, and said, O Lord, the great and dreadful God, keeping the covenant and mercy to them that love him, and to them that keep his commandments;",
      "M": "I prayed to the LORD my God and confessed, saying: 'O Lord, the great and awesome God, who keeps his covenant and steadfast love toward those who love him and obey his commandments—'",
      "T": "I prayed to the LORD my God and poured out my confession: 'O Lord—great, awesome God—you who faithfully keep covenant and show steadfast love to all who love you and keep your commandments:'"
    },
    "5": {
      "L": "We have sinned, and have committed iniquity, and have done wickedly, and have rebelled, even by departing from thy precepts and from thy judgments:",
      "M": "'We have sinned and acted perversely and done wickedly and rebelled, turning away from your commandments and ordinances.'",
      "T": "'We have sinned. We have done wrong. We have acted wickedly. We have been openly rebellious, turning our backs on your commandments and laws.'"
    },
    "6": {
      "L": "Neither have we hearkened unto thy servants the prophets, which spake in thy name to our kings, our princes, and our fathers, and to all the people of the land.",
      "M": "'We have not listened to your servants the prophets, who spoke in your name to our kings, our princes, our ancestors, and all the people of the land.'",
      "T": "'We would not listen to your servants the prophets, who faithfully spoke your word to our kings, our leaders, our ancestors—to all the people of the land. We refused to hear.'"
    },
    "7": {
      "L": "O Lord, righteousness belongeth unto thee, but unto us confusion of faces, as at this day; to the men of Judah, and to the inhabitants of Jerusalem, and unto all Israel, that are near, and that are far off, through all the countries whither thou hast driven them, because of their trespass that they have trespassed against thee.",
      "M": "'To you, O Lord, belongs righteousness, but to us belongs open shame—as it is this day—to the people of Judah, to the inhabitants of Jerusalem, and to all Israel, near and far, in all the lands where you have scattered them because of the unfaithfulness they committed against you.'",
      "T": "'Righteousness belongs to you, O Lord. Shame belongs to us—we carry it openly to this day: the people of Judah, the people of Jerusalem, all Israel—scattered near and far across every land where your judgment has driven us, because of our repeated betrayal of you.'"
    },
    "8": {
      "L": "O Lord, to us belongeth confusion of face, to our kings, to our princes, and to our fathers, because we have sinned against thee.",
      "M": "'To us, O LORD, belongs open shame—to our kings, our princes, and our ancestors—because we have sinned against you.'",
      "T": "'Yes, shame belongs to us, O LORD—to our kings, our officials, our fathers—all of us who have sinned against you.'"
    },
    "9": {
      "L": "To the Lord our God belong mercies and forgivenesses, though we have rebelled against him;",
      "M": "'To the Lord our God belong mercy and forgiveness, even though we have rebelled against him.'",
      "T": "'But to you, O LORD our God, belong compassion and forgiveness—even for those of us who have rebelled against you.'"
    },
    "10": {
      "L": "Neither have we obeyed the voice of the LORD our God, to walk in his laws, which he set before us by his servants the prophets.",
      "M": "'We have not obeyed the voice of the LORD our God by following his laws, which he placed before us through his servants the prophets.'",
      "T": "'We have not obeyed the voice of the LORD our God. We have not walked in the laws he placed before us through his servants the prophets.'"
    },
    "11": {
      "L": "Yea, all Israel have transgressed thy law, even by departing, that they might not obey thy voice; therefore the curse is poured upon us, and the oath that is written in the law of Moses the servant of God, because we have sinned against him.",
      "M": "'All Israel has transgressed your law, turning away so as not to obey you. Therefore the curse and sworn judgment written in the Law of Moses the servant of God have been poured out on us, because we sinned against him.'",
      "T": "'All Israel—every tribe and generation—has transgressed your law and turned away from you. And so the curse written in the Law of Moses, your servant, has fallen on us—the oath sealed in that covenant, now poured out on our heads—because we sinned against you.'"
    },
    "12": {
      "L": "And he hath confirmed his words, which he spake against us, and against our judges that judged us, by bringing upon us a great evil: for under the whole heaven hath not been done as hath been done upon Jerusalem.",
      "M": "'He has confirmed the words he spoke against us and against our rulers by bringing upon us great disaster. Nothing like what has happened to Jerusalem has ever been done under the whole heaven.'",
      "T": "'He has done exactly what he said he would do—against us and against our leaders. He has brought upon us a catastrophe without parallel. What has befallen Jerusalem is unlike anything that has happened anywhere on earth.'"
    },
    "13": {
      "L": "As it is written in the law of Moses, all this evil is come upon us: yet made we not our prayer before the LORD our God, that we might turn from our iniquities, and understand thy truth.",
      "M": "'Just as it is written in the Law of Moses, all this disaster has come upon us. Yet we have not sought the favor of the LORD our God by turning from our sins and giving heed to his truth.'",
      "T": "'All of this—exactly as the Law of Moses warned us—has come upon us. And still we have not turned to the LORD our God. We have not humbled ourselves before him, repented of our sins, or taken his truth to heart.'"
    },
    "14": {
      "L": "Therefore hath the LORD watched upon the evil, and brought it upon us: for the LORD our God is righteous in all his works which he doeth: for we obeyed not his voice.",
      "M": "'So the LORD was watching for the right moment to bring this disaster upon us, for the LORD our God is righteous in all he does—but we did not obey him.'",
      "T": "'And so the LORD watched for the moment and brought this calamity upon us. He is completely righteous in everything he has done. We are the ones who would not obey.'"
    },
    "15": {
      "L": "And now, O Lord our God, that hast brought thy people forth out of the land of Egypt with a mighty hand, and hast gotten thee renown, as at this day; we have sinned, we have done wickedly.",
      "M": "'And now, O Lord our God, who brought your people out of Egypt with a mighty hand and won for yourself renown that endures to this day—we have sinned, we have done wrong.'",
      "T": "'And now, O LORD our God—you who brought your people out of Egypt with a mighty hand, who made your name great, a name still honored to this day—we have sinned, we have done evil.'"
    },
    "16": {
      "L": "O Lord, according to all thy righteousness, I beseech thee, let thine anger and thy fury be turned away from thy city Jerusalem, thy holy mountain: because for our sins, and for the iniquities of our fathers, Jerusalem and thy people are become a reproach to all that are about us.",
      "M": "'O Lord, in keeping with all your righteous acts, turn away your anger and wrath from your city Jerusalem, your holy mountain. For because of our sins and the iniquities of our ancestors, Jerusalem and your people have become a disgrace to all those around us.'",
      "T": "'O Lord, in keeping with your faithfulness and all your saving acts—turn your anger and fury away from Jerusalem, your holy city, your holy mountain. For our sins, and the sins of our fathers before us, Jerusalem and your people have become a shameful spectacle to every nation around us.'"
    },
    "17": {
      "L": "Now therefore, O our God, hear the prayer of thy servant, and his supplications, and cause thy face to shine upon thy sanctuary that is desolate, for the Lord's sake.",
      "M": "'Now therefore, O our God, hear the prayer of your servant and his pleas for mercy. For your own sake, O Lord, let your face shine on your desolate sanctuary.'",
      "T": "'So now, O our God—hear your servant's prayer. Listen to his plea for mercy. For your own sake, O Lord, let your face shine on your sanctuary that lies in ruins.'"
    },
    "18": {
      "L": "O my God, incline thine ear, and hear; open thine eyes, and behold our desolations, and the city which is called by thy name: for we do not present our supplications before thee for our righteousnesses, but for thy great mercies.",
      "M": "'O my God, hear and incline your ear. Open your eyes and see our desolations and the city that bears your name. We do not lay our petitions before you on the ground of our own righteousness, but on the ground of your great mercy.'",
      "T": "'O my God—lean down and listen. Open your eyes and see what has happened to us, and to this city that bears your name. We do not come before you with our own goodness as our argument. We come with nothing but your great mercy.'"
    },
    "19": {
      "L": "O Lord, hear; O Lord, forgive; O Lord, hearken and do; defer not, for thine own sake, O my God: for thy city and thy people are called by thy name.",
      "M": "'O Lord, hear! O Lord, forgive! O Lord, listen and act! Do not delay, for your own sake, O my God, because your city and your people bear your name.'",
      "T": "'Hear, O LORD! Forgive, O LORD! Listen and act, O LORD! Do not wait—act now—for your own sake, my God. Your city, your people—they carry your name. Your name is at stake.'"
    },
    "20": {
      "L": "And whiles I was speaking, and praying, and confessing my sin and the sin of my people Israel, and presenting my supplication before the LORD my God for the holy mountain of my God;",
      "M": "While I was speaking and praying, confessing my sin and the sin of my people Israel, and presenting my plea before the LORD my God for the holy mountain of my God—",
      "T": "Even while I was still speaking—pouring out my confession, my sin and my people's sin before the LORD, pleading for God's holy mountain—"
    },
    "21": {
      "L": "Yea, whiles I was speaking in prayer, even the man Gabriel, whom I had seen in the vision at the beginning, being caused to fly swiftly, touched me about the time of the evening oblation.",
      "M": "while I was still speaking in prayer, the man Gabriel, whom I had seen in the earlier vision, came to me in swift flight at the time of the evening offering.",
      "T": "while my prayer was still on my lips, Gabriel came—the one I had seen in the earlier vision—flying swiftly, arriving at the time of the evening sacrifice, and touching me."
    },
    "22": {
      "L": "And he informed me, and talked with me, and said, O Daniel, I am now come forth to give thee skill and understanding.",
      "M": "He spoke with me and said, 'O Daniel, I have now come to give you insight and understanding.'",
      "T": "He spoke to me: 'Daniel, I have been sent to give you understanding and insight.'"
    },
    "23": {
      "L": "At the beginning of thy supplications the commandment came forth, and I am come to shew thee; for thou art greatly beloved: therefore understand the matter, and consider the vision.",
      "M": "'At the beginning of your pleas, a word went out, and I have come to tell you, for you are greatly beloved. Therefore consider the matter carefully and understand the vision.'",
      "T": "'The moment you began to pray, a command went out from the throne, and I was sent to bring you the answer—because you are deeply loved by God. So listen carefully. Take in what you are about to hear.'"
    },
    "24": {
      "L": "Seventy weeks are determined upon thy people and upon thy holy city, to finish the transgression, and to make an end of sins, and to make reconciliation for iniquity, and to bring in everlasting righteousness, and to seal up the vision and prophecy, and to anoint the most Holy.",
      "M": "'Seventy weeks are decreed for your people and your holy city: to finish the transgression, to put an end to sin, to atone for iniquity, to bring in everlasting righteousness, to seal up vision and prophecy, and to anoint the Most Holy.'",
      "T": "'Seventy sevens have been decreed for your people and your holy city—to complete the full measure of rebellion, to seal off all sin, to atone for iniquity, to bring in a righteousness that endures forever, to seal up vision and prophecy for good, and to anoint the Most Holy.'"
    },
    "25": {
      "L": "Know therefore and understand, that from the going forth of the commandment to restore and to build Jerusalem unto the Anointed One the Prince shall be seven weeks, and threescore and two weeks: the street shall be built again, and the wall, even in troublous times.",
      "M": "'Know and understand this: From the issuing of the decree to restore and rebuild Jerusalem until the Anointed One, the prince, will be seven weeks and sixty-two weeks. It will be rebuilt with streets and a trench, but in times of trouble.'",
      "T": "'Mark this and understand it: from the time the decree goes out to restore and rebuild Jerusalem until the Messiah, the Prince, appears will be seven sevens—and then sixty-two sevens more. Jerusalem will be rebuilt, its streets and its walls restored, though in distressing times.'"
    },
    "26": {
      "L": "And after threescore and two weeks shall the Anointed One be cut off, but not for himself: and the people of the prince that shall come shall destroy the city and the sanctuary; and the end thereof shall be with a flood, and unto the end of the war desolations are determined.",
      "M": "'After the sixty-two weeks, the Anointed One will be cut off and will have nothing. The people of the prince who is to come will destroy the city and the sanctuary. Its end will come like a flood, and until the end of the war, desolations are decreed.'",
      "T": "'After those sixty-two sevens, the Messiah will be cut off—not for his own sake, but for others. Then the people of a coming prince will sweep in and destroy the city and the sanctuary. The end will come like a flood. War will run on to the very end. Desolation has been decreed.'"
    },
    "27": {
      "L": "And he shall confirm the covenant with many for one week: and in the midst of the week he shall cause the sacrifice and the oblation to cease, and for the overspreading of abominations he shall make it desolate, even until the consummation, and that determined shall be poured upon the desolate.",
      "M": "'He will make a firm covenant with many for one week. In the middle of the week he will put an end to sacrifice and offering. And on the wing of abominations will come one who makes desolate, until the decreed destruction is poured out on the desolator.'",
      "T": "'In the final seven, a covenant will be made with many—strong and binding. But in the middle of that seven, the sacrifice and the grain offering will be abolished. And on the crest of abominations will come the desolator—until the end that has been decreed falls on the one who desolates.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'daniel')
        merge_tier(existing, DANIEL, tier_key)
        save(tier_dir, 'daniel', existing)
    print('Daniel 7–9 written.')

if __name__ == '__main__':
    main()
