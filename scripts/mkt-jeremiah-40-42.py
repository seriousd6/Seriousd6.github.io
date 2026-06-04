"""
MKT Jeremiah chapters 40–42 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-40-42.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-33-36.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name force
  matters — oracle delivery, divine address, confrontation, swearing formulas. The formula
  "declares the LORD" → "Yahweh declares it" in T. "the word of the LORD came" → "Yahweh's
  word came" in T.

- H430 (אֱלֹהִים, ʾĕlōhîm): "God" consistently in all tiers. "the LORD your God" → "Yahweh
  your God" in T when direct address to the people.

- "captain of the guard" (רַב-טַבָּחִים, rab-ṭabbāḥîm): literally "chief of the executioners/
  slaughterers." L/M: "captain of the guard"; T: "the chief of the guard" — the slaughter
  connotation is implicit context, not surfaced explicitly in these chapters.

- H2233 (זֶרַע, zeraʿ, "seed/offspring"): 41:1 — "of the royal seed" (מִזֶּרַע הַמְּלוּכָה).
  Ishmael's Davidic bloodline made his act both a political claim and a betrayal. L: "of
  the royal seed"; M: "of royal descent"; T: "from the royal line" — his blood claim is
  surfaced in T's framing.

- H5162 (נִחַם, niḥam, "repent/relent"): 42:10 — "for I relent of the disaster I brought
  upon you." This is divine pathos (Heschel): God does not admit sin but announces a
  turning-point in his purpose. L: "for I repent of the evil I have done to you"; M: "for
  I relent of the disaster I have brought upon you"; T: "for I am turning from the
  disaster I brought upon you." The Hebrew idiom is preserved in L for transparency; M and
  T use relent/turning to avoid the misleading sense that God sinned.

- Build/plant — pull down/pluck up (42:10): The covenant-restoration dyad from Jer 1:10
  and 31:28 ("I set you over nations... to pluck up and break down... and to build and to
  plant"). L: literal verbs; M: same; T: highlights the covenant-formula resonance.

- H6960 (qiwwâ, "wait/hope") and H2671 (ḥēṣ, "arrow") not prominent; standard rendering.

- "execration / horror / curse / reproach" (42:18): the four-fold judgment formula recurs
  throughout Jeremiah (cf. 24:9; 25:18; 29:18). L: technical terms preserved; M: natural
  English equivalents; T: surfaces the shame-culture force — these are terms of public
  contempt, not merely private suffering.

- "dissembled in your hearts" (42:20, הִתְעֵיתֶם): literally "you have led astray in your
  souls" — a strong accusation of insincerity. L: "you have deceived your own souls";
  M: "you were being dishonest"; T: "you were acting in bad faith from the start."

Structural and contextual notes for chapters 40–42:

- Ch. 40: The fall of Jerusalem is now past. Nebuzaradan's speech (vv.2-3) is remarkable:
  a Babylonian commander articulates Israel's theology — the Lord punished them because
  they sinned. Gedaliah's governorship represents the last attempt at indigenous leadership
  in the land. His naïve refusal to believe Johanan's warning is the tragic pivot.

- Ch. 41: Ishmael's treachery is multiple: he murders Gedaliah during a meal of hospitality
  (the ancient Near East's ultimate violation of covenant); he then massacres mourning
  pilgrims coming to worship; he fills Asa's cistern with corpses (the historical cistern
  of 1 Kgs 15:22 — Asa built Mizpah as a defense line; now that defensive work becomes
  a mass grave). The king's daughters (v.10) are the surviving royals entrusted to
  Gedaliah; Ishmael's seizure of them implies a dynastic counter-claim. He is of "the
  royal seed" — making his violence a bid for power, not just murder.

- Ch. 42: The waiting period of ten days (v.7) is significant — God does not answer
  instantly; the people must wait and hold themselves open. The double "whether it is good
  or bad, we will obey" (v.6) is an oath formula. Jeremiah's final charge (vv.19-22)
  exposes the bad faith: they had already decided to go to Egypt; the consultation was
  a pretense. This is the last time Jeremiah has free access to this remnant as their
  prophet. Chapter 43 will show them going to Egypt despite everything.

OT intertextuality:
- 40:4 — "all the land is before you": echoes Gen 13:9 (Abram to Lot), 20:15 (Abimelech
  to Abraham). The phrase marks an open grant of territory.
- 41:9 — Asa's cistern: 1 Kgs 15:22 — Asa conscripted all Israel to build Geba and
  Mizpah. Now Ishmael fills that civic work with the dead.
- 42:10 — "build / plant": Jer 1:10; 31:28 — the covenant-restoration formula stated in
  Jeremiah's commission and the new covenant chapter.
- 42:18 — four-fold shame formula: 24:9; 25:18; 29:18 — a characteristic Jeremianic
  judgment-catalogue.
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


JEREMIAH = {
  "40": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD after Nebuzaradan the captain of the guard had let him go from Ramah, when he had taken him — bound in chains among all the captives of Jerusalem and Judah who were being exiled to Babylon.",
      "M": "The word that came to Jeremiah from the LORD after Nebuzaradan the captain of the guard had released him from Ramah, where he had been taken in chains among all the exiles of Jerusalem and Judah who were being deported to Babylon.",
      "T": "This is the word Yahweh gave to Jeremiah after Nebuzaradan, the chief of the royal guard, released him from Ramah — where Jeremiah had been found bound in chains among all the exiles of Jerusalem and Judah being marched off to Babylon."
    },
    "2": {
      "L": "The captain of the guard took Jeremiah and said to him: The LORD your God pronounced this disaster upon this place.",
      "M": "The captain of the guard took Jeremiah and said to him: The LORD your God pronounced this disaster against this place.",
      "T": "The chief of the guard took Jeremiah aside and said: Yahweh your God declared this catastrophe over this city."
    },
    "3": {
      "L": "The LORD has brought it about and done as he said, because you sinned against the LORD and did not obey his voice; therefore this thing has come upon you.",
      "M": "The LORD has brought it about and done exactly as he said, because you sinned against the LORD and did not obey his voice — that is why this thing has happened to you.",
      "T": "Yahweh made it happen. He did exactly what he said he would do — because you sinned against him and refused to listen to his voice. That is why all this has fallen on you."
    },
    "4": {
      "L": "And now behold, I release you this day from the chains that are on your hands. If it seems good to you to come with me to Babylon, come, and I will take good care of you. But if it seems wrong to you to come with me to Babylon, do not; see, all the land is before you — go wherever it seems good and right to you.",
      "M": "But now, I am releasing you this very day from the chains on your hands. If it seems good to you to come with me to Babylon, come, and I will look after you well. But if it seems wrong to come with me to Babylon, then do not; all the land is before you — go wherever seems good and right in your eyes.",
      "T": "But here and now, I am removing the chains from your wrists. If you want to come with me to Babylon, come — I will take care of you well. But if you do not want to come with me, then do not. All the land lies open before you. Go wherever you see fit."
    },
    "5": {
      "L": "Or if you choose to remain, then return to Gedaliah the son of Ahikam, son of Shaphan, whom the king of Babylon has appointed over the cities of Judah, and stay with him among the people. Go wherever it seems right to you to go.' So the captain of the guard gave him a ration of food and a gift and let him go.",
      "M": "Or if you prefer to remain, then go back to Gedaliah the son of Ahikam, son of Shaphan, whom the king of Babylon has set over the cities of Judah, and stay with him among the people — or go wherever you choose.' Then the captain of the guard gave him a food ration and a gift and let him go.",
      "T": "Or if you prefer to stay in the land, go to Gedaliah son of Ahikam son of Shaphan, whom the king of Babylon has made governor over the towns of Judah, and settle there among the people — or go wherever you like.' The chief of the guard gave Jeremiah a food allowance and a parting gift and released him."
    },
    "6": {
      "L": "Then Jeremiah went to Gedaliah the son of Ahikam at Mizpah and lived with him among the people who were left in the land.",
      "M": "So Jeremiah went to Gedaliah the son of Ahikam at Mizpah and lived with him among the people remaining in the land.",
      "T": "Jeremiah went to Gedaliah son of Ahikam at Mizpah and settled there with him, among all who were still left in the land."
    },
    "7": {
      "L": "When all the captains of the forces who were in the open country and their men heard that the king of Babylon had appointed Gedaliah the son of Ahikam over the land and had committed to him men, women, children, and some of the poorest of the land who had not been taken into exile to Babylon,",
      "M": "When all the captains of the forces in the open country and their men heard that the king of Babylon had appointed Gedaliah the son of Ahikam as governor over the land and had entrusted to him men, women, children, and some of the poorest people of the land — those who had not been taken into exile to Babylon —",
      "T": "When all the militia commanders scattered through the countryside — and their troops — heard that the king of Babylon had appointed Gedaliah son of Ahikam as governor over the land, and had placed under his care the men, women, children, and the very poorest of the people who had not been deported to Babylon,"
    },
    "8": {
      "L": "they came to Gedaliah at Mizpah: Ishmael the son of Nethaniah, and Johanan and Jonathan the sons of Kareah, and Seraiah the son of Tanhumeth, and the sons of Ephai the Netophathite, and Jezaniah the son of the Maachathite, they and their men.",
      "M": "they came to Gedaliah at Mizpah: Ishmael son of Nethaniah, Johanan and Jonathan sons of Kareah, Seraiah son of Tanhumeth, the sons of Ephai the Netophathite, and Jezaniah son of the Maachathite — they and their men.",
      "T": "they came to Gedaliah at Mizpah: Ishmael son of Nethaniah, Johanan and Jonathan sons of Kareah, Seraiah son of Tanhumeth, the sons of Ephai the Netophathite, Jezaniah son of the Maachathite — all of them with their men."
    },
    "9": {
      "L": "Gedaliah the son of Ahikam, son of Shaphan, swore to them and to their men: Do not be afraid to serve the Chaldeans; dwell in the land and serve the king of Babylon, and it shall be well with you.",
      "M": "Gedaliah son of Ahikam, son of Shaphan, swore to them and their men: Do not be afraid to serve the Chaldeans. Settle in the land, serve the king of Babylon, and it will go well with you.",
      "T": "Gedaliah son of Ahikam son of Shaphan made a solemn oath to them and to their men: Do not be afraid to submit to the Chaldeans. Settle in the land. Serve the king of Babylon. Do that, and it will be well with you."
    },
    "10": {
      "L": "As for me, I will dwell at Mizpah to stand before the Chaldeans who will come to us. But as for you, gather wine and summer fruits and oil, and put them in your vessels, and dwell in your cities that you have taken.",
      "M": "As for me, I will stay at Mizpah to represent you before the Chaldeans who come to us. But you — gather wine and summer fruits and oil; store them in your containers and settle in the towns you have occupied.",
      "T": "I will stay here at Mizpah to deal with whatever Chaldean officials come to us. As for you — gather in the wine, the late harvest fruits, the oil. Store them up. Settle into the towns you now hold."
    },
    "11": {
      "L": "Likewise, when all the Jews who were in Moab and among the Ammonites and in Edom and in all the other lands heard that the king of Babylon had left a remnant in Judah and had appointed over them Gedaliah the son of Ahikam, son of Shaphan,",
      "M": "Likewise, when all the Jews living in Moab, among the Ammonites, in Edom, and in all the other countries heard that the king of Babylon had left a remnant in Judah and had appointed Gedaliah son of Ahikam, son of Shaphan, over them,",
      "T": "Meanwhile, all the Jews who had taken refuge in Moab, among the Ammonites, in Edom, and in every other land heard the news: the king of Babylon had left a remnant in Judah and set Gedaliah son of Ahikam son of Shaphan over them."
    },
    "12": {
      "L": "then all the Jews returned from all the places where they had been driven and came to the land of Judah, to Gedaliah at Mizpah, and they gathered much wine and summer fruits.",
      "M": "then all the Jews returned from all the places to which they had been scattered, and came to the land of Judah and to Gedaliah at Mizpah. And they harvested a great quantity of wine and summer fruits.",
      "T": "They came back — all of them — from every place they had been scattered to. They came to the land of Judah, to Gedaliah at Mizpah. It was a season of abundance: they brought in great quantities of wine and late-harvest fruit."
    },
    "13": {
      "L": "Now Johanan the son of Kareah and all the captains of the forces in the open country came to Gedaliah at Mizpah",
      "M": "Now Johanan son of Kareah and all the captains of the forces in the open country came to Gedaliah at Mizpah",
      "T": "Then Johanan son of Kareah and all the other militia commanders came to Gedaliah at Mizpah"
    },
    "14": {
      "L": "and said to him: Do you know that Baalis the king of the Ammonites has sent Ishmael the son of Nethaniah to take your life? But Gedaliah the son of Ahikam did not believe them.",
      "M": "and said to him: Do you know that Baalis the king of the Ammonites has sent Ishmael the son of Nethaniah to assassinate you? But Gedaliah son of Ahikam refused to believe them.",
      "T": "and told him: Do you know that Baalis king of the Ammonites has dispatched Ishmael son of Nethaniah to kill you? But Gedaliah son of Ahikam would not believe it."
    },
    "15": {
      "L": "Then Johanan the son of Kareah spoke secretly to Gedaliah at Mizpah, saying: Let me go and strike down Ishmael the son of Nethaniah — and no man will know. Why should he take your life, so that all the Jews who are gathered to you would be scattered and the remnant of Judah would perish?",
      "M": "Then Johanan son of Kareah spoke privately to Gedaliah at Mizpah: Please, let me go and kill Ishmael son of Nethaniah — no one will know. Why should he take your life and let all the Jews gathered around you scatter, and the remnant of Judah perish?",
      "T": "Then Johanan son of Kareah took Gedaliah aside at Mizpah and said quietly: Let me go and put Ishmael son of Nethaniah down. No one needs to know. Why should he kill you and undo everything — scatter all these people who have come back to you, and wipe out the last remnant of Judah?"
    },
    "16": {
      "L": "But Gedaliah the son of Ahikam said to Johanan the son of Kareah: You shall not do this thing, for you are speaking falsely about Ishmael.",
      "M": "But Gedaliah son of Ahikam said to Johanan son of Kareah: You must not do this. What you are saying about Ishmael is not true.",
      "T": "But Gedaliah son of Ahikam said to Johanan son of Kareah: Do not do it. What you are saying about Ishmael is not true."
    }
  },
  "41": {
    "1": {
      "L": "In the seventh month, Ishmael the son of Nethaniah, son of Elishama, of the royal seed, came with ten men to Gedaliah the son of Ahikam at Mizpah. As they ate bread together there at Mizpah,",
      "M": "In the seventh month, Ishmael son of Nethaniah, son of Elishama, who was of royal descent, came with ten men to Gedaliah son of Ahikam at Mizpah. While they were eating together there at Mizpah,",
      "T": "In the seventh month, Ishmael son of Nethaniah son of Elishama — a man of the royal line — came to Gedaliah son of Ahikam at Mizpah, bringing ten men with him. As they sat together eating at the table in Mizpah,"
    },
    "2": {
      "L": "Ishmael the son of Nethaniah and the ten men who were with him rose up and struck down Gedaliah the son of Ahikam, son of Shaphan, with the sword, and killed him — whom the king of Babylon had appointed governor over the land.",
      "M": "Ishmael son of Nethaniah and the ten men with him rose up and struck down Gedaliah son of Ahikam, son of Shaphan, with the sword, killing the man whom the king of Babylon had appointed as governor over the land.",
      "T": "Ishmael son of Nethaniah and his ten men rose up and cut down Gedaliah son of Ahikam son of Shaphan with the sword — murdering the man Babylon's king had made governor over the land."
    },
    "3": {
      "L": "Ishmael also struck down all the Jews who were with Gedaliah at Mizpah, and the Chaldean soldiers who happened to be found there.",
      "M": "Ishmael also killed all the Jews who were with Gedaliah at Mizpah, as well as the Chaldean soldiers who were there.",
      "T": "Ishmael killed all the Jews who were with Gedaliah in Mizpah, and the Chaldean troops stationed there as well."
    },
    "4": {
      "L": "On the second day after he had killed Gedaliah, when no one yet knew of it,",
      "M": "On the second day after the killing of Gedaliah, before anyone knew of it,",
      "T": "The next day — the day after the murder, before word had spread to anyone —"
    },
    "5": {
      "L": "eighty men came from Shechem, from Shiloh, and from Samaria, with their beards shaved and their clothes torn and their bodies gashed, bringing grain offerings and incense to the house of the LORD.",
      "M": "eighty men came from Shechem, Shiloh, and Samaria with their beards shaved, their clothes torn, and their bodies cut, bringing grain offerings and incense to the house of the LORD.",
      "T": "eighty men arrived from Shechem, Shiloh, and Samaria — beards shaved, clothes torn, bodies gashed — pilgrims bearing grain offerings and incense for Yahweh's temple."
    },
    "6": {
      "L": "Ishmael the son of Nethaniah went out from Mizpah to meet them, weeping as he went. As he met them, he said to them: Come to Gedaliah the son of Ahikam.",
      "M": "Ishmael son of Nethaniah went out from Mizpah to meet them, weeping all the way. When he met them, he said: Come to Gedaliah son of Ahikam.",
      "T": "Ishmael son of Nethaniah went out from Mizpah to meet them, weeping as he walked. When he reached them he said: Come and see Gedaliah son of Ahikam."
    },
    "7": {
      "L": "But when they came into the town, Ishmael the son of Nethaniah slaughtered them and threw them into a pit — he and the men who were with him.",
      "M": "But when they came into the town, Ishmael son of Nethaniah slaughtered them and cast them into a pit — he and the men with him.",
      "T": "But once they were inside the town, Ishmael son of Nethaniah and his men butchered them and threw their bodies into a pit."
    },
    "8": {
      "L": "But ten men among them said to Ishmael: Do not kill us, for we have stores of wheat, barley, oil, and honey hidden in the field. So he held back and did not kill them among their brothers.",
      "M": "But ten of the men said to Ishmael: Do not kill us — we have stores of wheat, barley, oil, and honey hidden in the field. So he held back and did not kill them along with their companions.",
      "T": "But ten of the men spoke up: Do not kill us. We have stores hidden in the field — wheat, barley, oil, honey. So Ishmael spared them and did not kill them with the others."
    },
    "9": {
      "L": "Now the pit into which Ishmael had cast all the dead bodies of the men he had killed — it was the large pit that King Asa had made as a defense against Baasha king of Israel. Ishmael the son of Nethaniah filled it with the slain.",
      "M": "The pit into which Ishmael threw all the bodies of the men he had killed was the large cistern that King Asa had constructed as a defense against Baasha king of Israel. Ishmael son of Nethaniah filled it with the slain.",
      "T": "The pit where Ishmael threw the bodies was the great cistern that King Asa had built long ago as a fortification against Baasha king of Israel. Ishmael son of Nethaniah filled it with the dead."
    },
    "10": {
      "L": "Then Ishmael took captive all the rest of the people who were in Mizpah — the king's daughters and all the people remaining in Mizpah whom Nebuzaradan the captain of the guard had committed to Gedaliah the son of Ahikam. Ishmael the son of Nethaniah took them captive and departed to cross over to the Ammonites.",
      "M": "Then Ishmael took captive all the rest of the people in Mizpah — including the king's daughters and all those remaining in Mizpah whom Nebuzaradan the captain of the guard had entrusted to Gedaliah son of Ahikam. Ishmael son of Nethaniah took them captive and set out to go across to the Ammonites.",
      "T": "Then Ishmael rounded up everyone left in Mizpah — including the royal daughters and all the people Nebuzaradan the guard commander had placed in Gedaliah's care. He took them captive and headed out toward Ammonite territory."
    },
    "11": {
      "L": "But when Johanan the son of Kareah and all the captains of the forces with him heard of all the evil that Ishmael the son of Nethaniah had done,",
      "M": "But when Johanan son of Kareah and all the captains of the forces with him heard of all the evil that Ishmael son of Nethaniah had done,",
      "T": "When Johanan son of Kareah and all the militia commanders with him heard what Ishmael son of Nethaniah had done — every atrocity of it —"
    },
    "12": {
      "L": "they took all their men and went to fight with Ishmael the son of Nethaniah. They overtook him by the great pool that is at Gibeon.",
      "M": "they took all their men and went to fight against Ishmael son of Nethaniah. They caught up with him by the great pool at Gibeon.",
      "T": "they gathered all their men and set out to intercept Ishmael son of Nethaniah. They caught up with him at the great pool of Gibeon."
    },
    "13": {
      "L": "And when all the people whom Ishmael had carried away captive saw Johanan the son of Kareah and all the captains of the forces with him, they were glad.",
      "M": "When all the people Ishmael had taken captive saw Johanan son of Kareah and all the captains of the forces with him, they were overjoyed.",
      "T": "When all the captives Ishmael had taken saw Johanan son of Kareah and the commanders coming with their men, they were flooded with relief."
    },
    "14": {
      "L": "So all the people whom Ishmael had carried away captive from Mizpah turned about and came back to Johanan the son of Kareah.",
      "M": "All the people Ishmael had taken captive from Mizpah turned and went back to Johanan son of Kareah.",
      "T": "Every captive Ishmael had taken from Mizpah turned around and went to Johanan son of Kareah."
    },
    "15": {
      "L": "But Ishmael the son of Nethaniah escaped from Johanan with eight men and went to the Ammonites.",
      "M": "But Ishmael son of Nethaniah escaped from Johanan with eight men and fled to the Ammonites.",
      "T": "But Ishmael son of Nethaniah slipped away from Johanan with eight men and escaped to the Ammonites."
    },
    "16": {
      "L": "Then Johanan the son of Kareah and all the captains of the forces with him took all the remnant of the people whom he had recovered from Ishmael the son of Nethaniah from Mizpah — after he had slain Gedaliah the son of Ahikam — the men of war, the women, the children, and the court officials whom he had brought back from Gibeon.",
      "M": "Then Johanan son of Kareah and all the captains of the forces with him took all the remnant of the people whom he had recovered from Ishmael son of Nethaniah, from Mizpah — after the killing of Gedaliah son of Ahikam — soldiers, women, children, and court officials, whom he had brought back from Gibeon.",
      "T": "Johanan son of Kareah and all the commanders with him gathered up everyone they had rescued from Ishmael son of Nethaniah — soldiers, women, children, court officials — everyone Ishmael had taken from Mizpah after murdering Gedaliah son of Ahikam, and whom Johanan had now recovered at Gibeon."
    },
    "17": {
      "L": "And they departed and dwelt in Geruth Chimham which is by Bethlehem, intending to go to Egypt,",
      "M": "They set out and stayed at Geruth Chimham near Bethlehem, intending to go on to Egypt,",
      "T": "They set out and camped at Geruth Chimham near Bethlehem, with Egypt as their destination —"
    },
    "18": {
      "L": "because of the Chaldeans, for they were afraid of them, since Ishmael the son of Nethaniah had killed Gedaliah the son of Ahikam, whom the king of Babylon had appointed governor over the land.",
      "M": "because they were afraid of the Chaldeans, since Ishmael son of Nethaniah had killed Gedaliah son of Ahikam, whom the king of Babylon had made governor over the land.",
      "T": "afraid of the Chaldeans, because Ishmael son of Nethaniah had murdered Gedaliah son of Ahikam — the man Babylon's king had placed in charge of the land. They feared the Chaldean reprisal."
    }
  },
  "42": {
    "1": {
      "L": "Then all the captains of the forces, with Johanan the son of Kareah and Jezaniah the son of Hoshaiah, and all the people from the least to the greatest, came near",
      "M": "Then all the captains of the forces, along with Johanan son of Kareah and Jezaniah son of Hoshaiah, and all the people from the least to the greatest, approached",
      "T": "Then all the militia commanders — Johanan son of Kareah, Jezaniah son of Hoshaiah, every one of them — with all the people, from the smallest to the greatest, came forward"
    },
    "2": {
      "L": "and said to Jeremiah the prophet: Let our plea for mercy come before you, and pray to the LORD your God for all this remnant — for we are left but a few, as your eyes can see us.",
      "M": "and said to Jeremiah the prophet: Please hear our plea for mercy, and pray to the LORD your God for us — for this entire remnant. As you can see with your own eyes, we are only a few left out of many.",
      "T": "and said to Jeremiah the prophet: Please — hear our request. Pray to Yahweh your God for us, for this whole remnant. As you can see with your own eyes, we are barely anyone. Once we were many; now we are a handful."
    },
    "3": {
      "L": "That the LORD your God may show us the way in which we should walk and the thing that we should do.",
      "M": "Ask that the LORD your God will show us the way we should go and what we should do.",
      "T": "Ask Yahweh your God to show us the road we should take and what we should do when we get there."
    },
    "4": {
      "L": "Jeremiah the prophet said to them: I have heard you. Behold, I will pray to the LORD your God according to your words, and whatever the LORD answers you, I will declare to you — I will keep nothing back from you.",
      "M": "Jeremiah the prophet said to them: I have heard you. I will pray to the LORD your God as you have asked, and whatever the LORD answers, I will tell you in full — I will withhold nothing.",
      "T": "Jeremiah the prophet said to them: I have heard you. I will bring your request before Yahweh your God exactly as you have stated it. Whatever answer Yahweh gives, I will tell you every word of it — I will hold nothing back."
    },
    "5": {
      "L": "Then they said to Jeremiah: May the LORD be a true and faithful witness against us if we do not act according to all the word that the LORD your God sends you to tell us.",
      "M": "Then they said to Jeremiah: May the LORD be a true and faithful witness against us if we do not act in accordance with all that the LORD your God sends you to tell us.",
      "T": "Then they said to Jeremiah: Let Yahweh be a true and reliable witness against us if we fail to do everything Yahweh your God sends you back to tell us."
    },
    "6": {
      "L": "Whether it is good or bad, we will obey the voice of the LORD our God to whom we are sending you, so that it may go well with us when we obey the voice of the LORD our God.",
      "M": "Whether it is good or bad, we will obey the voice of the LORD our God to whom we are sending you, so that it may go well with us when we comply with the voice of the LORD our God.",
      "T": "Good news or bad news — whatever it is, we will obey the voice of Yahweh our God, to whom we are sending you. We do this so that things may go well with us — because we have obeyed Yahweh our God."
    },
    "7": {
      "L": "At the end of ten days the word of the LORD came to Jeremiah.",
      "M": "At the end of ten days the word of the LORD came to Jeremiah.",
      "T": "Ten days passed. Then Yahweh's word came to Jeremiah."
    },
    "8": {
      "L": "Then he called Johanan the son of Kareah and all the captains of the forces who were with him, and all the people from the least to the greatest,",
      "M": "Then Jeremiah summoned Johanan son of Kareah and all the captains of the forces who were with him, and all the people from the least to the greatest,",
      "T": "Jeremiah called Johanan son of Kareah, all the commanders who were with him, and all the people — from the smallest to the greatest —"
    },
    "9": {
      "L": "and said to them: Thus says the LORD, the God of Israel, to whom you sent me to present your supplication before him:",
      "M": "and said to them: Thus says the LORD, the God of Israel, to whom you sent me to bring your petition:",
      "T": "and said to them: This is what Yahweh, the God of Israel, says — the one to whom you sent me to lay your request:"
    },
    "10": {
      "L": "If you will stay in this land, then I will build you up and not tear you down, and I will plant you and not uproot you, for I repent of the evil that I have done to you.",
      "M": "If you will remain in this land, I will build you up and not tear you down, and I will plant you and not uproot you, for I relent of the disaster I have brought upon you.",
      "T": "If you will stay in this land, I will build you up and not pull you down; I will plant you and not uproot you. For I am turning from the disaster I brought upon you."
    },
    "11": {
      "L": "Do not be afraid of the king of Babylon, of whom you are afraid. Do not be afraid of him, declares the LORD, for I am with you, to save you and to deliver you from his hand.",
      "M": "Do not be afraid of the king of Babylon, whom you now fear. Do not be afraid of him, declares the LORD, for I am with you to save you and to rescue you from his power.",
      "T": "Do not be afraid of the king of Babylon — I know you are afraid of him. Do not fear him. Yahweh declares it: I am with you to save you and to pull you free from his grip."
    },
    "12": {
      "L": "And I will grant you mercy, that he may show mercy to you and allow you to return to your own land.",
      "M": "I will show you compassion, so that he will have compassion on you and let you return to your own land.",
      "T": "I will move him to show you mercy, so that you may come home to your own land."
    },
    "13": {
      "L": "But if you say: We will not stay in this land — disobeying the voice of the LORD your God,",
      "M": "But if you say: We will not stay in this land — disobeying the voice of the LORD your God —",
      "T": "But if you say: We will not stay in this land — refusing to obey Yahweh your God —"
    },
    "14": {
      "L": "saying: No, but we will go to the land of Egypt, where we will see no war, and hear no sound of the trumpet, and not be hungry for bread; then",
      "M": "saying: No, we will go to the land of Egypt, where we will not see war or hear the trumpet or go hungry for bread — then",
      "T": "— saying instead: No, we are going to Egypt, where there is no war, where we will not hear the alarm of battle, where we will not go hungry — then"
    },
    "15": {
      "L": "Now therefore hear the word of the LORD, O remnant of Judah: Thus says the LORD of hosts, the God of Israel — If you fully set your faces to go to Egypt and go to sojourn there,",
      "M": "hear the word of the LORD, O remnant of Judah: Thus says the LORD of hosts, the God of Israel — If you are firmly resolved to go to Egypt and settle there as foreigners,",
      "T": "then hear the word of Yahweh, remnant of Judah. Yahweh of hosts, the God of Israel, says this: If you are set on going to Egypt, if you intend to settle there as immigrants,"
    },
    "16": {
      "L": "then the sword that you fear shall overtake you there in the land of Egypt, and the famine that you dread shall follow close after you there in Egypt, and there you shall die.",
      "M": "then the sword you fear will overtake you there in Egypt, and the famine you dread will pursue you right into Egypt, and there you will die.",
      "T": "then the very sword you are fleeing will catch up to you in Egypt. The very famine you dread will follow you right into Egypt. And there you will die."
    },
    "17": {
      "L": "All the men who set their faces to go to Egypt to sojourn there shall die by the sword, by famine, and by pestilence — not one of them shall remain or escape from the disaster that I will bring upon them.",
      "M": "All who set their faces to go to Egypt to live there shall die by the sword, by famine, and by pestilence. Not one of them will survive or escape the disaster I will bring upon them.",
      "T": "Every person who turns their face toward Egypt and goes there to live will die — by sword, by famine, by plague. Not one will survive or escape the disaster I bring upon them."
    },
    "18": {
      "L": "For thus says the LORD of hosts, the God of Israel: As my anger and my wrath were poured out on the inhabitants of Jerusalem, so my wrath will be poured out on you when you enter Egypt. You will become an execration and a horror and a curse and a reproach — and you shall see this place no more.",
      "M": "For thus says the LORD of hosts, the God of Israel: Just as my anger and wrath were poured out on the inhabitants of Jerusalem, so my wrath will be poured out on you when you enter Egypt. You will become an object of execration, of horror, of cursing, and of contempt — and you shall never see this place again.",
      "T": "For this is what Yahweh of hosts, the God of Israel, says: Just as I poured out my anger and fury on the people of Jerusalem, I will pour my fury out on you when you enter Egypt. You will become a byword of contempt — a thing people shudder at, a curse, a disgrace. And you will never see this land again."
    },
    "19": {
      "L": "The LORD has said to you, O remnant of Judah: Do not go into Egypt. Know this day that I have warned you.",
      "M": "The LORD has spoken to you, O remnant of Judah: Do not go to Egypt. Know for certain this day that I have warned you.",
      "T": "Yahweh has spoken to you, remnant of Judah: Do not go to Egypt. Take this to heart today: I have given you a clear warning."
    },
    "20": {
      "L": "For you have deceived your own souls, for you yourselves sent me to the LORD your God, saying: Pray for us to the LORD our God, and whatever the LORD our God says, tell us and we will do it.",
      "M": "For you have been dishonest with yourselves. You sent me to the LORD your God saying: Pray for us to the LORD our God, and whatever the LORD our God says, declare it to us and we will obey.",
      "T": "You have been acting in bad faith from the start. You sent me to Yahweh your God with those words: Pray for us. Tell us what Yahweh our God says. We will do it."
    },
    "21": {
      "L": "And I have declared it to you this day, but you have not obeyed the voice of the LORD your God — not in anything for which he sent me to you.",
      "M": "I have declared it to you today, but you have not obeyed the voice of the LORD your God in anything he sent me to tell you.",
      "T": "Today I delivered his answer — every word of it. And you will not obey the voice of Yahweh your God. Not in a single thing he sent me to tell you."
    },
    "22": {
      "L": "Now therefore know certainly that you shall die by the sword, by famine, and by pestilence in the place where you desire to go to sojourn.",
      "M": "Now therefore know for certain that you will die by the sword, by famine, and by pestilence in the place where you want to go to settle.",
      "T": "So know this with certainty: You will die by sword, by famine, by plague — in the very place you are determined to go."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 40–42 written.')

if __name__ == '__main__':
    main()
