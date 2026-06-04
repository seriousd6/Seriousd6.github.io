"""
MKT Daniel chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-daniel-10-12.py

=== CHAPTER OVERVIEW ===

Chapter 10 (Hebrew, prose):
  Prologue to the final vision. In the third year of Cyrus, Daniel fasts and
  mourns three weeks. A glorious heavenly figure—described in terms that
  anticipate Revelation 1 and echo Ezekiel 1—appears by the Tigris; Daniel
  collapses, is touched and restored. The messenger explains he was delayed
  21 days by the "prince of Persia" until Michael came to help. He now comes
  to reveal what will happen "in the latter days." Michael is named "your prince"—
  the guardian angel of Israel, consistent with ch. 12:1.

Chapter 11 (Hebrew, prose — the most detailed prophetic history in the OT):
  The messenger recounts the succession of Persian kings, Alexander's conquest,
  the division of his kingdom (vv. 2–4), and the prolonged struggle between the
  Ptolemies (king of the south) and Seleucids (king of the north) through roughly
  vv. 5–35, culminating in the actions of Antiochus IV Epiphanes who profanes the
  sanctuary and sets up the abomination (v. 31). Vv. 36–45 describe a "willful
  king" who sets himself above all gods — whether this is Antiochus continued or
  an eschatological figure is the primary interpretive divide; translation is kept
  neutral to allow both readings.

Chapter 12 (Hebrew, prose):
  The eschatological conclusion. Michael stands up at the great tribulation.
  Daniel 12:2 is one of the clearest OT resurrection texts. The sealing of
  the book until the time of the end. The "time, times, and half a time" connects
  to 7:25. The numbered days (1,290 / 1,335) have no consensus interpretation;
  translation preserves the numbers without forcing a resolution.

=== CONTESTED-TERM DECISIONS (continuing from mkt-daniel-7-9.py) ===

- H3068 (יהוה / LORD): "LORD" (small-caps convention) in L/M. In T context
  where the personal relational name is invoked (9:2 type usage), "the LORD"
  is used in T. Ch. 10:12 has "before your God" (H430 אֱלֹהִים), not יהוה.

- H430 (אֱלֹהִים / God): "God" throughout all tiers.

- H5943 / H5945 (עֶלְיוֹן / Most High): "the Most High" in all tiers — used in
  ch. 11:36 "God of gods." Maintains chs 4–9 convention.

- H4480 (מִקְדָּשׁ / sanctuary): "sanctuary" in L/M; "temple" is acceptable in T
  when the building rather than the holiness concept is primary.

- H7227 (רַב / great/many): In 12:2 "many" — preserved as such in L/M; T notes
  the OT idiom (cf. Isa 53:11–12 where "many" does not exclude "all" but
  foregrounds the astonishing scope of the act).

- H5769 (עוֹלָם / ʿolam): "everlasting" in L/M for חַיֵּי עוֹלָם (12:2, "everlasting
  life"). T uses "the life of the age to come" once to surface the temporal/
  qualitative dimension (life belonging to the coming age, not merely duration).
  For 12:3 "forever and ever" (לְעוֹלָם וָעֶד): retained in all tiers.

- H4899 (מָשִׁיחַ / Anointed One / Messiah): Does not appear in chs 10–12.

- H7760 / H8251 (שִׁקּוּץ שֹׁמֵם / abomination of desolation): Carried forward
  from 8:13 and 9:27. L/M: "the abomination that makes desolate." T: same.
  This is a fixed prophetic term; do not paraphrase.

- "King of the south" / "king of the north": Retained verbatim in all three
  tiers throughout ch. 11 — these are geographic-dynastic designators that
  function as technical terms in the passage. Substituting "Ptolemy" or
  "Seleucid" would impose a specific identification the text keeps open.

- H4915 / H7764 (עֵרֶל עָרֵל / Kittim): In 11:30 "ships of Kittim" — a
  Hebrew designation for western maritime peoples (originally Cyprus, then
  broadly: Greeks, Romans). L/M: "ships of Kittim." T: "ships of Kittim
  (western fleet)" — supplying minimal gloss in context.

- H8269 (שַׂר / prince/commander): Michael is called "one of the chief princes"
  (10:13) and "the great prince" (12:1). L/M: "prince." T: "prince" or
  "guardian prince" for clarity where the protective role is foregrounded.

- "Time, times, and half a time" (12:7): Matches 7:25. Aramaic root עִדָּן;
  Hebrew equivalent here. L/M/T: "a time, times, and half a time" — the
  conventional and intentionally ambiguous rendering.

- H7919 (מַשְׂכִּיל / wise/insightful): "wise" in L/M; "discerning" or "the wise"
  in T. In 12:3 T may render "those who lead many to righteousness" to unpack
  "מַצְדִּיקֵי הָרַבִּים" (those who make the many righteous/just).

- H2617 (חֶסֶד / steadfast love): Not prominent in chs 10–12.

- The "book" (12:1, "written in the book"): The book of life/names — L/M: "the
  book." T: "the scroll of life" or "the book of life" where context invites it.

- Aspect: Hebrew narrative perfects rendered as completed/past acts in L/M.
  Future actions in direct speech rendered as future. The angelic speech of
  ch. 11 is dominated by Niphal and Hiphil imperfects describing historical
  events that are future from Daniel's vantage point — rendered as future in
  English throughout.

- Chapter 11 interpretive stance on vv. 36–45: Translation is kept historically
  neutral. The "willful king" section is translated to allow both the Antiochus
  continuation reading and the eschatological reading. No identifying gloss is
  added in any tier.
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
  "10": {
    "1": {
      "L": "In the third year of Cyrus king of Persia a word was revealed to Daniel, whose name was called Belteshazzar. And the word was true, and it was a great conflict. He understood the word and had understanding of the vision.",
      "M": "In the third year of Cyrus king of Persia, a message was revealed to Daniel, who was called Belteshazzar. The message was true, and it concerned a great conflict. Daniel understood the message and had understanding of the vision.",
      "T": "In the third year of Cyrus king of Persia, a revelation came to Daniel—the man known also by his Babylonian name, Belteshazzar. The word was true. It spoke of great warfare and upheaval. Daniel grasped the message, and the vision opened itself to him."
    },
    "2": {
      "L": "In those days I, Daniel, was mourning for three full weeks.",
      "M": "At that time, I, Daniel, had been mourning for three full weeks.",
      "T": "For three full weeks I, Daniel, went into mourning—fasting, grieving, waiting."
    },
    "3": {
      "L": "I ate no delicacies, no meat or wine entered my mouth, and I did not anoint myself at all, until three full weeks had been fulfilled.",
      "M": "I ate no choice food, no meat or wine passed my lips, and I used no lotions until the three weeks were over.",
      "T": "I ate no rich food. Meat and wine did not touch my lips. I did not anoint myself. Three weeks of this—until the time of mourning was complete."
    },
    "4": {
      "L": "And on the twenty-fourth day of the first month, as I was on the bank of the great river—that is, the Hiddekel—",
      "M": "On the twenty-fourth day of the first month, while I was standing on the bank of the great river—the Tigris—",
      "T": "On the twenty-fourth day of the first month, I was standing on the bank of the great Tigris River—"
    },
    "5": {
      "L": "I lifted up my eyes and looked, and behold, a certain man clothed in linen, his waist girded with gold of Uphaz.",
      "M": "I looked up and saw a man dressed in linen, with a belt of fine gold from Uphaz around his waist.",
      "T": "—when I looked up. A figure stood before me: a man clothed in linen, his waist bound with a girdle of pure gold from Uphaz."
    },
    "6": {
      "L": "His body was like beryl, his face like the appearance of lightning, his eyes like torches of fire, his arms and his feet like the gleam of burnished bronze, and the sound of his words like the sound of a multitude.",
      "M": "His body was like chrysolite, his face shone like lightning, his eyes were like flaming torches, his arms and legs gleamed like polished bronze, and his voice sounded like the roar of a great multitude.",
      "T": "His body gleamed like polished beryl. His face blazed like lightning. His eyes burned like torches of fire. His arms and legs shone like burnished bronze. When he spoke, the sound was like the roar of an army—like the noise of a vast crowd."
    },
    "7": {
      "L": "And I, Daniel, alone saw the vision, for the men who were with me did not see the vision; but a great trembling fell upon them, and they fled to hide themselves.",
      "M": "I, Daniel, was the only one who saw the vision; the men with me did not see it, yet a great terror overwhelmed them, and they fled and hid themselves.",
      "T": "I, Daniel, was the only one who saw the vision. Those who were with me saw nothing—yet the terror hit them all the same, sweeping over them in a wave, and they fled to hide."
    },
    "8": {
      "L": "So I was left alone and saw this great vision, and no strength was left in me. My radiant appearance was fearfully changed, and I retained no strength.",
      "M": "Left alone with this great vision, all my strength drained away. My face turned deathly pale, and I had no strength left.",
      "T": "Left alone before the vision, every ounce of strength drained out of me. My face went ashen. I had nothing left—no power to stand, no breath to speak."
    },
    "9": {
      "L": "Then I heard the sound of his words; and as I heard the sound of his words, I fell on my face in deep sleep, with my face to the ground.",
      "M": "When I heard the sound of his words, I fell into a deep sleep with my face to the ground.",
      "T": "When the sound of his voice reached me, I fell forward—face to the ground—plunged into a stupor, unable to move."
    },
    "10": {
      "L": "And behold, a hand touched me and set me trembling upon my hands and knees.",
      "M": "Then a hand touched me and set me trembling on my hands and knees.",
      "T": "Then a hand touched me—and I was roused, shaking, onto my hands and knees."
    },
    "11": {
      "L": "And he said to me, 'O Daniel, man greatly beloved, understand the words that I speak to you, and stand upright, for I have now been sent to you.' And when he had spoken this word to me, I stood up trembling.",
      "M": "He said to me, 'Daniel, you who are highly esteemed, consider carefully the words I am about to speak to you, and stand up, for I have now been sent to you.' And when he said this to me, I stood up, though I was trembling.",
      "T": "'O Daniel,' he said, 'you who are deeply loved—take in every word I am about to say to you, and stand up. I have been sent to you.' At those words I pulled myself to my feet, still trembling."
    },
    "12": {
      "L": "Then he said to me, 'Fear not, Daniel, for from the first day that you set your heart to understand and humbled yourself before your God, your words were heard, and I have come because of your words.'",
      "M": "'Do not be afraid, Daniel. Since the first day you set your heart to understand and to humble yourself before your God, your prayers were heard. I have come in response to them.'",
      "T": "'Fear nothing, Daniel. From the very first day you turned your heart toward understanding—from the first day you humbled yourself before God—your prayers were heard in heaven. I was sent in response to your words.'"
    },
    "13": {
      "L": "'The prince of the kingdom of Persia withstood me twenty-one days, but Michael, one of the chief princes, came to help me, for I was left there with the kings of Persia.'",
      "M": "'But the prince of the Persian kingdom resisted me twenty-one days. Then Michael, one of the chief princes, came to help me, because I was detained there with the king of Persia.'",
      "T": "'But the angelic prince assigned to Persia blocked my way for twenty-one days. Then Michael—one of the foremost of heaven's princes—came to my aid. I had been held in that contest against the powers of Persia.'"
    },
    "14": {
      "L": "'Now I have come to make you understand what will befall your people in the latter days. For the vision is for many days yet to come.'",
      "M": "'I have come to explain to you what will happen to your people in the days to come, for the vision concerns a time yet in the future.'",
      "T": "'Now I am here to open to you what will befall your people in the days ahead—the last days. The vision reaches far into the future.'"
    },
    "15": {
      "L": "When he had spoken to me according to these words, I turned my face toward the ground and was mute.",
      "M": "While he was saying this to me, I looked down at the ground and could not speak.",
      "T": "When he had said these things, I turned my face downward and fell silent—words gone from me entirely."
    },
    "16": {
      "L": "And behold, one in the likeness of the sons of man touched my lips. Then I opened my mouth and spoke. I said to him who stood before me, 'O my lord, by reason of the vision, anguish has overcome me, and I retain no strength.'",
      "M": "Then one who appeared to be a man touched my lips, and I opened my mouth and spoke. I said to the one standing before me, 'My lord, the vision has filled me with anguish and I have no strength left.'",
      "T": "Then one with a human form touched my lips. I opened my mouth and found my voice again. I said to the one standing before me: 'My lord—this vision has flooded me with anguish. All my strength is gone.'"
    },
    "17": {
      "L": "'How can my lord's servant speak with my lord? For no strength remains in me now, and no breath is left in me.'",
      "M": "'How can I, your servant, speak with you, my lord? My strength is gone and I can hardly breathe.'",
      "T": "'How can someone like me—your servant—even speak to you, my lord? I have no strength. There is barely breath in me.'"
    },
    "18": {
      "L": "Again one having the appearance of a man touched me and strengthened me.",
      "M": "Once more one who looked like a man touched me and gave me strength.",
      "T": "Again the figure—with the form of a man—reached out and touched me. Strength returned."
    },
    "19": {
      "L": "And he said, 'O man greatly beloved, fear not, peace be to you; be strong and be of good courage.' And when he spoke to me, I was strengthened and said, 'Let my lord speak, for you have strengthened me.'",
      "M": "He said, 'O man highly esteemed, do not be afraid. Peace! Be strong now; be strong.' When he spoke to me, I was strengthened and said, 'Speak, my lord, since you have given me strength.'",
      "T": "'O man deeply loved,' he said, 'fear nothing. Peace to you. Be strong—be very strong.' As he spoke, the strength flowed back into me. 'Speak, my lord,' I said. 'You have given me strength enough to hear.'"
    },
    "20": {
      "L": "Then he said, 'Do you know why I have come to you? Now I will return to fight against the prince of Persia; and when I go out, behold, the prince of Greece will come.'",
      "M": "'Do you know why I have come to you?' he said. 'Soon I will return to fight against the prince of Persia, and when I leave, the prince of Greece will come.'",
      "T": "'Do you understand why I have come?' he asked. 'When I leave you, I return to the battle against the prince of Persia—and after that the prince of Greece will come. The conflict among the heavenly powers over the nations goes on.'"
    },
    "21": {
      "L": "'But I will tell you what is inscribed in the writing of truth. There is none who contends alongside me against these except Michael your prince.'",
      "M": "'But first I will tell you what is written in the Book of Truth. No one supports me against them except Michael, your prince.'",
      "T": "'First, I will declare to you what is written in the scroll of truth. In this heavenly contest, no one stands with me against these powers except Michael—your prince, the guardian of your people.'"
    }
  },
  "11": {
    "1": {
      "L": "'And as for me, in the first year of Darius the Mede, I stood up to confirm and strengthen him.'",
      "M": "'And in the first year of Darius the Mede, I took my stand to support and strengthen him.'",
      "T": "'I should tell you—in the first year of Darius the Mede, I was the one who stood up to strengthen and support Michael in his work. Now let me tell you the truth of what lies ahead.'"
    },
    "2": {
      "L": "'And now I will tell you the truth. Behold, three more kings shall arise in Persia, and a fourth shall be far richer than all of them. And when he has grown strong through his riches, he shall stir up all against the kingdom of Greece.'",
      "M": "'Now I will tell you the truth. Three more kings will arise in Persia, and then a fourth, who will be far richer than all the others. When he has gained power through his wealth, he will stir up everyone against the kingdom of Greece.'",
      "T": "'Here is the truth. Three more kings will come to power in Persia, and after them a fourth—richer than all the rest. When his wealth has made him powerful enough, he will throw everything he has against the kingdom of Greece.'"
    },
    "3": {
      "L": "'Then a mighty king shall arise, who shall rule with great dominion and do as he wills.'",
      "M": "'Then a powerful king will arise who will rule with great power and do whatever he pleases.'",
      "T": "'Then a mighty king will rise—one who rules with enormous power and bends history to his own will.'"
    },
    "4": {
      "L": "'And as soon as he has arisen, his kingdom shall be broken and divided toward the four winds of heaven, but not to his posterity, nor according to his dominion with which he ruled; for his kingdom shall be plucked up and given to others besides these.'",
      "M": "'Yet as soon as he appears, his kingdom will be shattered and broken up toward the four winds of heaven. It will not go to his descendants, nor will it have the power he wielded, because his kingdom will be uprooted and given to others.'",
      "T": "'But at the very height of his power, his kingdom will be shattered—split in four directions like the four winds of heaven. It will not pass to his heirs. It will not hold the power he had. His empire will be torn apart and parceled out to others.'"
    },
    "5": {
      "L": "'The king of the south shall be strong, but one of his princes shall be stronger than he and shall rule, and his dominion shall be a great dominion.'",
      "M": "'The king of the south will become powerful, but one of his commanders will become even more powerful and will rule over a vast domain.'",
      "T": "'The king of the south will grow strong—but one of his own generals will surpass him, rising to rule a domain even greater than his master's.'"
    },
    "6": {
      "L": "'And at the end of years they shall make an alliance, and the daughter of the king of the south shall come to the king of the north to make a peace agreement. But she shall not retain the strength of her arm, and he and his arm shall not stand; she shall be given up, and those who brought her, and he who fathered her, and he who strengthened her in those times.'",
      "M": "'After some years, they will enter into an alliance. The daughter of the king of the south will come to the king of the north to cement the agreement. But she will not be able to maintain her position, and neither he nor his support will last. She will be abandoned, along with those who escorted her, the one who fathered her, and the one who supported her.'",
      "T": "'Years later they will negotiate an alliance. The daughter of the southern king will be sent to the northern king as a diplomatic bride to seal the peace. But the arrangement will fall apart. She will not be strong enough to hold her position. Neither her husband nor those who supported her will endure. She will be abandoned—along with her escort, her father's backing, and all who had propped her up.'"
    },
    "7": {
      "L": "'And from a branch from her roots one shall arise in his place. He shall come against the army and enter the fortress of the king of the north, and he shall deal with them and prevail.'",
      "M": "'One from her family line will arise and attack the army of the king of the north. He will enter his fortress and act against them and prevail.'",
      "T": "'But from her own family line—a branch from the same roots—a man will rise up. He will march against the northern army, breach the northern king's fortress, and defeat them decisively.'"
    },
    "8": {
      "L": "'He shall also carry off to Egypt their gods and their metal images with their precious vessels of silver and gold, and for some years he shall refrain from attacking the king of the north.'",
      "M": "'He will carry their gods, their metal images, and their valuable articles of silver and gold as plunder to Egypt. For some years he will leave the king of the north alone.'",
      "T": "'He will haul back to Egypt great spoils—the gods of the north, their cast images, their silver and gold vessels. For years afterward the northern king will be left undisturbed by him.'"
    },
    "9": {
      "L": "'Then the king of the north shall come into the realm of the king of the south but shall return to his own land.'",
      "M": "'Then the king of the north will invade the realm of the king of the south but will retreat to his own country.'",
      "T": "'The northern king will eventually push into the south—but he will turn back and go home again, achieving nothing lasting.'"
    },
    "10": {
      "L": "'His sons shall be stirred up and shall assemble a great multitude of forces, which shall keep coming and overflow and pass through; then he shall return and carry the war to his fortress.'",
      "M": "'His sons will prepare for war and assemble a great army, which will sweep forward like a flood and drive all the way to his enemy's fortress.'",
      "T": "'The northern king's sons will take up the cause. They will raise a vast army that moves like a flood—driving through, sweeping over everything—carrying the war all the way to the enemy's stronghold.'"
    },
    "11": {
      "L": "'Then the king of the south, moved with anger, shall come out and fight against the king of the north. And the king of the north shall raise a great multitude, but the multitude shall be given into his hand.'",
      "M": "'The king of the south, furious, will march out to fight the king of the north, who will raise a large army—but that army will be handed over to his opponent.'",
      "T": "'The southern king, burning with anger, will march out to meet him in battle. The northern king will field a massive army—but it will be delivered into the southern king's hands.'"
    },
    "12": {
      "L": "'And when the multitude is taken away, his heart shall be exalted, and he shall cast down tens of thousands, but he shall not prevail.'",
      "M": "'When he has defeated the army, he will become arrogant and slaughter tens of thousands, yet he will not maintain his advantage.'",
      "T": "'His victory will make him proud. He will cut down tens of thousands. But the arrogance of that victory will be his undoing—he will not hold what he has won.'"
    },
    "13": {
      "L": "'For the king of the north shall again raise a multitude, greater than the first. And after some years he shall come on with a great army and with much equipment.'",
      "M": "'The king of the north will raise another army, larger than the first. After several years he will advance with a huge army fully supplied.'",
      "T": "'Because the northern king will regroup and raise an even greater army than before. Years will pass—then he will come again with overwhelming force and abundant resources.'"
    },
    "14": {
      "L": "'In those times many shall rise against the king of the south, and the violent ones among your own people shall lift themselves up to fulfill the vision, but they shall fail.'",
      "M": "'In those times many will rise against the king of the south. Some violent men among your own people will rebel in order to fulfill the vision, but without success.'",
      "T": "'In that same era many forces will move against the southern king. Among your own people, violent men will try to seize the moment—imagining they are fulfilling the prophetic vision—but they will fall.'"
    },
    "15": {
      "L": "'Then the king of the north shall come and throw up siege works and take a fortified city. And the forces of the south shall not stand, or even his finest troops; there shall be no strength to withstand.'",
      "M": "'Then the king of the north will come and build siege ramps and capture a well-fortified city. The southern forces will be powerless to resist; even their finest troops will not be strong enough to stand.'",
      "T": "'The northern king will come in force—throwing up siege ramps, capturing a heavily fortified city. The southern forces will collapse before him. Even the cream of the south's army will have no strength to hold the line.'"
    },
    "16": {
      "L": "'But he who comes against him shall do as he wills, and none shall stand before him. And he shall stand in the glorious land, with destruction in his hand.'",
      "M": "'The invader will do as he pleases; no one will be able to oppose him. He will establish himself in the beautiful land and will have the power to destroy it.'",
      "T": "'The conqueror will have his way—unstoppable, unchallenged. He will plant himself in the glorious land, and he will hold destruction in his hand like a weapon.'"
    },
    "17": {
      "L": "'He shall set his face to come with the strength of his whole kingdom, and he shall bring upright terms; he shall perform them. He shall give him the daughter of women to corrupt her, but she shall not stand or be to his advantage.'",
      "M": "'He will determine to come with the full power of his kingdom and will negotiate a peace agreement and carry it out. He will give him his daughter in marriage in order to overthrow him, but his plan will not succeed or help him.'",
      "T": "'He will marshal the full power of his kingdom and then offer seemingly fair terms—a treaty backed by his own daughter given in marriage. His real aim is to bring the southern kingdom down from within. But it will not work. The plan will turn against him.'"
    },
    "18": {
      "L": "'Afterward he shall turn his face to the coastlands and shall capture many of them. But a commander shall put an end to his insolence; indeed, he shall turn his insolence back on him.'",
      "M": "'Then he will turn his attention to the coastlands and will take many of them. But a commander will put an end to his arrogance and will turn his contempt back on him.'",
      "T": "'He will pivot to the coastlands next and seize many of them. But a foreign commander will halt his march—throwing his own contempt back in his face and ending his campaigns.'"
    },
    "19": {
      "L": "'Then he shall turn his face back toward the fortresses of his own land, but he shall stumble and fall, and shall not be found.'",
      "M": "'He will then turn back toward the fortresses of his own country but will stumble and fall, to be seen no more.'",
      "T": "'He will turn home toward his own strongholds—but he will stumble and fall. He will simply vanish from the stage of history.'"
    },
    "20": {
      "L": "'Then shall arise in his place one who shall send a tax collector through the glory of the kingdom, but within a few days he shall be broken, neither in anger nor in battle.'",
      "M": "'His successor will send a tax collector through the most prestigious part of the kingdom, but he will be destroyed within a few days—not in anger or in battle.'",
      "T": "'His successor will send a tax collector through the finest provinces of the kingdom—extracting tribute from the realm's glory. But within a few days he will be gone—brought down not by rage or open war, but quietly.'"
    },
    "21": {
      "L": "'In his place shall arise a despicable person to whom royal honor has not been given. He shall come in without warning and obtain the kingdom by smooth words.'",
      "M": "'He will be succeeded by a contemptible person who has not been given the honor of royalty. He will invade the kingdom when its people feel secure and seize power through flattery.'",
      "T": "'In his place will arise a despised man—one whom no one considered fit to be king. He will slip in when people feel secure and win the kingdom through smooth talk and manipulation, not through legitimate succession.'"
    },
    "22": {
      "L": "'Armies shall be utterly swept away before him and broken, even the prince of the covenant.'",
      "M": "'An overwhelming army will be swept away before him and shattered, and the prince of the covenant will also be destroyed.'",
      "T": "'Whole armies will be swept aside before him like a flooding river. Even the prince of the covenant will be broken.'"
    },
    "23": {
      "L": "'And from the time that an alliance is made with him he shall act deceitfully, and he shall become strong with a small following.'",
      "M": "'After making an alliance with him, he will act deceitfully, and with only a small force he will rise to power.'",
      "T": "'Once an agreement has been struck with him, he will work in deception. Starting with only a handful of followers, he will build his power.'"
    },
    "24": {
      "L": "'Without warning he shall come into the richest parts of the province, and he shall do what neither his fathers nor his fathers' fathers have done, scattering among them plunder, spoil, and goods. He shall devise plans against strongholds, but only for a time.'",
      "M": "'Without warning he will invade the most productive areas of a province and will accomplish what his ancestors never did—distributing plunder, loot, and wealth among his followers. He will make plans to attack fortified strongholds, but only for a limited time.'",
      "T": "'He will descend without warning on the most fertile regions, doing what no king before him ever did: lavishly distributing plunder among his followers to buy their loyalty. He will set his schemes against the great strongholds—but the clock is ticking. His time is limited.'"
    },
    "25": {
      "L": "'And he shall stir up his power and his heart against the king of the south with a great army. And the king of the south shall wage war with an exceedingly great and mighty army, but he shall not stand, for plots shall be devised against him.'",
      "M": "'He will stir up his strength and his courage against the king of the south with a large army. The king of the south will wage war with a large and powerful army, but he will not be able to stand because of the plots devised against him.'",
      "T": "'He will rouse all his courage and power and move against the southern king with an immense army. The southern king will meet him with an even greater force—but he will not hold. The plots forming around his own table will undo him.'"
    },
    "26": {
      "L": "'Those who eat from his provisions shall break him. His army shall be swept away, and many shall fall slain.'",
      "M": "'The people who eat from the king's table will destroy him. His army will be swept away, and many will fall in battle.'",
      "T": "'His own table-companions—the men he has fed and trusted—will bring him down. His army will be shattered. The battlefield will be covered with the slain.'"
    },
    "27": {
      "L": "'And as for the two kings, their hearts shall be set on doing evil. They shall speak lies at the same table, but it shall not prosper, for the end is still at the appointed time.'",
      "M": "'The two kings, with their hearts bent on evil, will sit at the same table and lie to each other, but to no avail, because an end will still come at the appointed time.'",
      "T": "'The two kings will sit at the same table—and both will be lying. Their hearts will be fixed on harm; their words will be hollow. Nothing will come of it. The end is not yet. It waits for its appointed time.'"
    },
    "28": {
      "L": "'And he shall return to his land with great wealth, but his heart shall be set against the holy covenant. He shall take action and return to his own land.'",
      "M": "'The northern king will return to his own country with great wealth, but his heart will be set against the holy covenant. He will take action against it and then go back to his own land.'",
      "T": "'He will go home rich—laden with plunder—but his heart will be turned against God's holy covenant. He will strike against it before returning to his land.'"
    },
    "29": {
      "L": "'At the time appointed he shall return and come into the south, but it shall not be this time as it was before.'",
      "M": "'At the appointed time he will invade the south again, but this time the outcome will be different from what it was before.'",
      "T": "'When the appointed time comes, he will strike south again. But this campaign will not go as the first one did.'"
    },
    "30": {
      "L": "'For ships of Kittim shall come against him, and he shall be afraid and withdraw, and shall turn back and be enraged against the holy covenant and take action. He shall return and give attention to those who forsake the holy covenant.'",
      "M": "'Ships of Kittim will come against him, and he will lose heart and withdraw. Then, furious, he will turn back and take out his anger on the holy covenant. On his return, he will show favor to those who abandon the holy covenant.'",
      "T": "'A western fleet will come against him—and the confrontation will break his nerve. He will pull back, but his retreat will turn into rage against everything sacred. He will redirect his fury against the holy covenant, and he will cultivate allies among those who have already abandoned it.'"
    },
    "31": {
      "L": "'His forces shall arise and profane the sanctuary fortress, and shall take away the regular burnt offering. And they shall set up the abomination that makes desolate.'",
      "M": "'His armed forces will arise and desecrate the temple fortress and abolish the daily sacrifice. Then they will set up the abomination that makes desolate.'",
      "T": "'His armies will march in and desecrate the temple—stripping away the regular daily sacrifice. And they will erect the abomination that makes desolate in the holy place.'"
    },
    "32": {
      "L": "'He shall corrupt with smooth words those who act wickedly against the covenant, but the people who know their God shall stand firm and take action.'",
      "M": "'With flattery he will corrupt those who have violated the covenant, but the people who know their God will firmly resist him.'",
      "T": "'With smooth words he will draw into his camp those who have already sold out the covenant. But the people who truly know their God will be unmoved. They will act.'"
    },
    "33": {
      "L": "'And the wise among the people shall make many understand, though for some days they shall stumble by sword and flame, by captivity and plunder.'",
      "M": "'Those who are wise will instruct many, though for a time they will fall by the sword or be burned, or taken captive or plundered.'",
      "T": "'The discerning among the people will teach many—spreading understanding even in the darkest days. But they will suffer for it: sword, fire, captivity, plunder—these will take them down for a season.'"
    },
    "34": {
      "L": "'When they stumble, they shall receive a little help. And many shall join themselves to them with smooth words.'",
      "M": "'When they fall, they will receive a little help, and many who join them will do so insincerely.'",
      "T": "'When they fall, a little relief will come to them—but many who attach themselves to the cause in that hour will do so with flattery, not faith.'"
    },
    "35": {
      "L": "'And some of the wise shall stumble, so that they may be refined and purified and made white, until the time of the end, for it is still for the appointed time.'",
      "M": "'Some of the wise will stumble, so that they may be refined, purified, and made spotless until the time of the end, for it will still come at the appointed time.'",
      "T": "'Some of the wise will fall—not because God has abandoned them, but because the falling is itself the refining. They are being purified, made clean, made white. And the end has its appointed time. It will not come early.'"
    },
    "36": {
      "L": "'And the king shall do as he wills. He shall exalt himself and magnify himself above every god, and shall speak astonishing things against the God of gods. He shall prosper until the indignation is accomplished, for what is determined shall be done.'",
      "M": "'The king will do as he pleases. He will exalt and magnify himself above every god and will say unheard-of things against the God of gods. He will succeed until the time of wrath is complete, for what has been determined must take place.'",
      "T": "'The king will act with total self-will. He will raise himself above every god, blaspheming the God of gods with breathtaking arrogance. He will prosper—but only until the period of divine wrath has run its course. What has been decreed cannot be undone.'"
    },
    "37": {
      "L": "'He shall pay no attention to the gods of his fathers, or to the one desired by women. He shall not pay attention to any god, for he shall magnify himself above all.'",
      "M": "'He will show no regard for the gods of his ancestors or for the one desired by women, nor will he regard any god, but will exalt himself above them all.'",
      "T": "'He will acknowledge nothing—not the gods of his own heritage, not the deity women have honored, not any god at all. He has placed himself above every power, human or divine.'"
    },
    "38": {
      "L": "'But in his place he shall honor the god of fortresses; a god whom his fathers did not know he shall honor with gold and silver, with precious stones and costly gifts.'",
      "M": "'Instead, he will honor a god of fortresses—a god his ancestors did not know—with gold, silver, precious stones, and expensive gifts.'",
      "T": "'Instead, he will lavish gold and silver, precious stones and rich offerings on a god of fortresses—some power of military strength and conquest that his ancestors never acknowledged.'"
    },
    "39": {
      "L": "'He shall deal with the strongest fortresses with the help of a foreign god. Whoever acknowledges him he shall fill with honor. He shall make them rulers over many and shall divide the land as a reward.'",
      "M": "'He will attack the mightiest fortresses with the help of a foreign god and will greatly honor those who acknowledge him. He will make them rulers over many people and will distribute the land at a price.'",
      "T": "'With this foreign power behind him, he will breach the strongest fortresses. He will heap honors on those who bend the knee to him—making them lords over whole peoples, distributing land as payment for their loyalty.'"
    },
    "40": {
      "L": "'At the time of the end, the king of the south shall thrust at him, but the king of the north shall rush against him like a whirlwind, with chariots and horsemen and with many ships. And he shall come into countries and shall overflow and pass through.'",
      "M": "'At the time of the end, the king of the south will engage him in battle, and the king of the north will storm out against him with chariots, cavalry, and a large fleet of ships. He will invade many countries and sweep through them like a flood.'",
      "T": "'At the time of the end, the southern king will provoke him. But the northern king will come back at him like a whirlwind—chariots, cavalry, a great fleet—sweeping through country after country like a flooding river, unstoppable.'"
    },
    "41": {
      "L": "'He shall come into the glorious land. And tens of thousands shall fall, but these shall be delivered out of his hand: Edom and Moab and the main part of the Ammonites.'",
      "M": "'He will also invade the beautiful land. Many countries will fall, but Edom, Moab, and the leaders of Ammon will be delivered from his hand.'",
      "T": "'He will enter the glorious land. Tens of thousands will fall before him—but Edom, Moab, and the principal part of Ammon will escape his hand.'"
    },
    "42": {
      "L": "'He shall stretch out his hand against the countries, and the land of Egypt shall not escape.'",
      "M": "'He will extend his power over many countries; Egypt will not escape.'",
      "T": "'He will reach out his hand across the nations. Egypt will not be spared.'"
    },
    "43": {
      "L": "'He shall become ruler over the treasures of gold and of silver, and all the precious things of Egypt, and the Libyans and the Cushites shall follow at his heels.'",
      "M": "'He will gain control of the treasures of gold and silver and all the riches of Egypt, with the Libyans and Cushites in his train.'",
      "T": "'He will seize Egypt's treasuries—gold, silver, all its precious wealth—and the Libyans and Cushites will trail at his steps like servants.'"
    },
    "44": {
      "L": "'But reports from the east and from the north shall alarm him, and he shall go out with great fury to destroy and devote many to destruction.'",
      "M": "'But reports from the east and the north will alarm him, and he will set out in a great rage to destroy and annihilate many.'",
      "T": "'Then disturbing news will reach him from the east and the north—and it will throw him into a fury. He will march out with murderous intent, bent on total destruction.'"
    },
    "45": {
      "L": "'And he shall pitch his palatial tents between the sea and the glorious holy mountain. Yet he shall come to his end, with none to help him.'",
      "M": "'He will set up his royal tents between the sea and the beautiful holy mountain. Yet he will come to his end, and no one will help him.'",
      "T": "'He will plant his royal pavilions between the sea and the holy mountain—poised as if he owns the world. And then he will come to his end. No rescue will come. No one will help him.'"
    }
  },
  "12": {
    "1": {
      "L": "'At that time shall arise Michael, the great prince who stands over your people. And there shall be a time of trouble, such as never has been since there was a nation until that time. But at that time your people shall be delivered, every one whose name shall be found written in the book.'",
      "M": "'At that time Michael, the great prince who watches over your people, will arise. There will be a time of distress unlike any since nations first existed. But at that time your people will be rescued—every one who is found written in the book.'",
      "T": "'At that time Michael will stand up—the great guardian prince who watches over your people. It will be a time of anguish unlike anything since a nation first walked the earth. But at that time your people will be delivered—every last one whose name is written in the book of life.'"
    },
    "2": {
      "L": "'And many of those who sleep in the dust of the earth shall awake, some to everlasting life, and some to shame and everlasting contempt.'",
      "M": "'Multitudes who sleep in the dust of the earth will awake: some to everlasting life, others to shame and everlasting contempt.'",
      "T": "'The dead will rise from the dust—many of them, awakened from the long sleep. Some will wake to the life of the age to come. Others will wake to shame, to contempt that never ends.'"
    },
    "3": {
      "L": "'And those who are wise shall shine like the brightness of the sky above, and those who turn many to righteousness, like the stars forever and ever.'",
      "M": "'Those who are wise will shine like the brightness of the heavens, and those who lead many to righteousness, like the stars forever and ever.'",
      "T": "'The wise—those who have understood and endured—will blaze like the brightness of the open sky. Those who have led many to righteousness will shine like stars, forever and ever, age upon age.'"
    },
    "4": {
      "L": "'But you, Daniel, shut up the words and seal the book, until the time of the end. Many shall run to and fro, and knowledge shall increase.'",
      "M": "'But you, Daniel, roll up and seal the words of this scroll until the time of the end. Many will go here and there to increase knowledge.'",
      "T": "'But you, Daniel—close up this scroll and seal it until the time of the end. When that time comes, many will search it through; understanding will grow.'"
    },
    "5": {
      "L": "Then I, Daniel, looked, and behold, two others stood, one on this bank of the stream and one on that bank of the stream.",
      "M": "Then I, Daniel, looked and saw two others standing there, one on this side of the river and one on the opposite bank.",
      "T": "I looked again—and there were two figures standing there, one on each bank of the river."
    },
    "6": {
      "L": "And one said to the man clothed in linen, who was above the waters of the stream, 'How long shall it be until the end of these wonders?'",
      "M": "One of them said to the man dressed in linen, who was above the waters of the river, 'How long will it be before these astonishing things are fulfilled?'",
      "T": "One of them called out to the man in linen—the one standing above the river's waters: 'How long will it be until the end of these extraordinary things?'"
    },
    "7": {
      "L": "And I heard the man clothed in linen, who was above the waters of the stream; he raised his right hand and his left hand toward heaven and swore by him who lives forever that it would be for a time, times, and half a time, and that when the shattering of the power of the holy people comes to an end, all these things would be finished.",
      "M": "The man dressed in linen, who was above the waters of the river, lifted his right hand and his left hand toward heaven, and I heard him swear by him who lives forever, saying it would be for a time, times and half a time. When the power of the holy people has been finally broken, all these things will be completed.",
      "T": "The man in linen—standing above the river—raised both hands toward heaven and swore by the One who lives forever: 'A time, times, and half a time.' When the power of the holy people has at last been shattered, all these things will reach their end."
    },
    "8": {
      "L": "I heard, but I did not understand. Then I said, 'O my lord, what shall be the outcome of these things?'",
      "M": "I heard, but I did not understand. So I asked, 'My lord, what will the outcome of all this be?'",
      "T": "I heard it all—but it was beyond me. 'My lord,' I said, 'what will the end of these things look like?'"
    },
    "9": {
      "L": "He said, 'Go your way, Daniel, for the words are shut up and sealed until the time of the end.'",
      "M": "He replied, 'Go your way, Daniel, because the words are rolled up and sealed until the time of the end.'",
      "T": "'Go, Daniel,' he said. 'These words are sealed shut until the time of the end. They are not for now.'"
    },
    "10": {
      "L": "'Many shall purify themselves and make themselves white and be refined, but the wicked shall act wickedly. And none of the wicked shall understand, but those who are wise shall understand.'",
      "M": "'Many will be purified, made spotless and refined, but the wicked will continue to be wicked. None of the wicked will understand, but those who are wise will understand.'",
      "T": "'Many will be purified through suffering—made clean and white, refined like metal in fire. But the wicked will go on being wicked, oblivious to the end. The wicked will never grasp it. The wise will.'"
    },
    "11": {
      "L": "'And from the time that the regular burnt offering is taken away and the abomination that makes desolate is set up, there shall be 1,290 days.'",
      "M": "'From the time that the daily sacrifice is abolished and the abomination that causes desolation is set up, there will be 1,290 days.'",
      "T": "'From the moment the daily sacrifice is removed and the abomination that makes desolate is installed—count 1,290 days.'"
    },
    "12": {
      "L": "'Blessed is he who waits and arrives at the 1,335 days.'",
      "M": "'Blessed is the one who waits for and reaches the end of the 1,335 days.'",
      "T": "'Blessed—truly blessed—is the one who holds on and lives to see the 1,335th day.'"
    },
    "13": {
      "L": "'But as for you, go your way till the end. And you shall rest and shall stand in your allotted place at the end of the days.'",
      "M": "'As for you, go your way till the end. You will rest, and then at the end of the days you will rise to receive your allotted inheritance.'",
      "T": "'As for you, Daniel—go. Walk out the rest of your days. You will rest in death. But at the end of all days, you will rise and take your appointed place.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'daniel')
        merge_tier(existing, DANIEL, tier_key)
        save(tier_dir, 'daniel', existing)
    print('Daniel 10–12 written.')

if __name__ == '__main__':
    main()
