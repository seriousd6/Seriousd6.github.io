"""
MKT Exodus chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-exodus-7-12.py

Covers the heart of the plague narrative: Aaron's serpent sign, plagues 1–9 (blood,
frogs, gnats, flies, livestock disease, boils, hail, locusts, darkness), the announcement
of plague 10, the institution of the Passover in chapter 12, the tenth plague (firstborn),
and the Exodus itself.

Translation decisions:
- H3068 (יהוה): "the LORD" in L and M; "Yahweh" in T — Exodus is the book of the divine-name
  revelation (3:14–15; 6:3). The T tier uses "Yahweh" throughout to surface the theological
  weight of the name being asserted against Pharaoh.
- H430 (אֱלֹהִים): "God" throughout all tiers; "gods" when referring to Egyptian deities (12:12).
- H2388 (חָזַק) heart hardening: rendered "hardened" in L/M. In T: "stayed rigid" / "remained hard"
  — this verb implies forceful making-firm, Pharaoh's own active stubbornness.
- H3513 (כָּבַד) heart hardening: "hardened" in L/M. In T: "stone-heavy" / "made heavy" —
  this verb's primary meaning is weight/heaviness; the T tier surfaces that physical metaphor.
  Distinction: H2388 = active self-hardening; H3513 = passive heaviness. Both are present
  in the Exodus narrative with different agents (God, Pharaoh, and unspecified).
- H1818 (דָּם): "blood" throughout. The glossary draft gloss "-guiltiness" is incorrect;
  the plain meaning "blood" is required in every plague-1 context.
- H226 (אוֹת): "sign" in L/M; "sign" in T (occasionally "mark" for the Passover blood token).
- H4159 (מוֹפֵת): "wonder" / "miracle" in L/M; "portent" in T when the ominous sense dominates.
- H6453 (פֶּסַח): "passover" in L; "Passover" (capitalized) in M and T.
- H7971 (שָׁלַח): "let go" / "send away" depending on clause; "release" preferred in T tier.
- H3820/H3824 (לֵב/לֵבָב): "heart" in L/M; T uses "heart" but can add "mind" when the
  cognitive dimension is primary.
- Hardening agent: in 7:13, 8:15, 8:32, 9:34–35 Pharaoh hardens his own heart (active);
  in 9:12, 10:1, 10:20, 10:27, 11:10 the LORD hardens it (divine agency). Both are treated
  as part of one divine design (9:16) — the T tier surfaces this.
- פֶּסַח etymology: "passing over" in the sense of sparing/protecting, not merely skipping
  past; 12:23 uses the verb with the destroyer as subject, implying Yahweh restrains him.
  The T tier at 12:13 and 12:23 notes this protective connotation.
- 12:37 "six hundred thousand men": rendered as stated; the scale is part of the epic register
  of the narrative. No harmonization.
- H4714 (מִצְרַיִם): "Egypt" / "Egyptians" as context requires.
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

EXODUS = {
  "7": {
    "1": {
      "L": "And the LORD said unto Moses, See, I have made thee a god to Pharaoh; and Aaron thy brother shall be thy prophet.",
      "M": "The LORD said to Moses, 'See, I have made you like God to Pharaoh, and Aaron your brother will be your prophet.'",
      "T": "Yahweh said to Moses, 'Pay attention: I have set you in the place of God before Pharaoh — his authority finds its limit in you — and Aaron your brother will speak as your prophet.'"
    },
    "2": {
      "L": "Thou shalt speak all that I command thee; and Aaron thy brother shall speak unto Pharaoh, that he send the children of Israel out of his land.",
      "M": "You are to speak everything I command you, and Aaron your brother will tell Pharaoh to let the Israelites go from his land.",
      "T": "You will say every word I give you, and Aaron will relay it to Pharaoh — that he must release the children of Israel from his land."
    },
    "3": {
      "L": "And I will harden Pharaoh's heart, and multiply my signs and my wonders in the land of Egypt.",
      "M": "But I will harden Pharaoh's heart, and I will multiply my signs and wonders in the land of Egypt.",
      "T": "I will make Pharaoh's heart stubborn, and I will multiply my signs and portents throughout the land of Egypt."
    },
    "4": {
      "L": "But Pharaoh shall not hearken unto you, that I may lay my hand upon Egypt, and bring forth mine armies, my people the children of Israel, out of the land of Egypt by great judgments.",
      "M": "Pharaoh will not listen to you. So I will lay my hand on Egypt and bring out my hosts — my people the Israelites — from the land of Egypt with great acts of judgment.",
      "T": "Pharaoh will not listen. Then I will stretch my hand over Egypt and march out my armies — my own people, the children of Israel — from Egypt with sweeping acts of judgment."
    },
    "5": {
      "L": "And the Egyptians shall know that I am the LORD, when I stretch forth mine hand upon Egypt, and bring out the children of Israel from among them.",
      "M": "Then the Egyptians will know that I am the LORD, when I stretch out my hand against Egypt and bring the Israelites out from among them.",
      "T": "When I reach my hand against Egypt and lead Israel out from their midst, Egypt will be forced to acknowledge: I am Yahweh."
    },
    "6": {
      "L": "And Moses and Aaron did so; as the LORD commanded them, so did they.",
      "M": "Moses and Aaron did just as the LORD had commanded them.",
      "T": "Moses and Aaron carried out everything Yahweh had commanded — without deviation."
    },
    "7": {
      "L": "And Moses was fourscore years old, and Aaron fourscore and three years old, when they spake unto Pharaoh.",
      "M": "Moses was eighty years old and Aaron was eighty-three when they spoke to Pharaoh.",
      "T": "Moses was eighty and Aaron eighty-three when they stood before Pharaoh — old men carrying a young God's commission."
    },
    "8": {
      "L": "And the LORD spake unto Moses and unto Aaron, saying,",
      "M": "The LORD said to Moses and Aaron,",
      "T": "Yahweh spoke to both Moses and Aaron:"
    },
    "9": {
      "L": "When Pharaoh shall speak unto you, saying, Shew a miracle for you: then thou shalt say unto Aaron, Take thy rod, and cast it before Pharaoh, and it shall become a serpent.",
      "M": "'When Pharaoh says to you, \"Show us a miracle,\" tell Aaron: Take your staff and throw it down before Pharaoh, and it will become a snake.'",
      "T": "'When Pharaoh demands a sign from you, tell Aaron to throw down his staff before Pharaoh — it will become a serpent.'"
    },
    "10": {
      "L": "And Moses and Aaron went in unto Pharaoh, and they did so as the LORD had commanded: and Aaron cast down his rod before Pharaoh, and before his servants, and it became a serpent.",
      "M": "So Moses and Aaron went in to Pharaoh and did exactly as the LORD had commanded. Aaron threw down his staff before Pharaoh and his officials, and it became a snake.",
      "T": "Moses and Aaron came before Pharaoh and did as Yahweh had commanded. Aaron threw his staff to the ground before Pharaoh and his entire court — and it became a serpent."
    },
    "11": {
      "L": "Then Pharaoh also called the wise men and the sorcerers: now the magicians of Egypt, they also did in like manner with their enchantments.",
      "M": "But Pharaoh summoned his own wise men and sorcerers, and the Egyptian magicians also turned their staffs into snakes by their occult arts.",
      "T": "Pharaoh called in his wise men and sorcerers — Egypt's own magicians — and they duplicated the feat with their secret arts, each throwing down a staff that became a serpent."
    },
    "12": {
      "L": "For they cast down every man his rod, and they became serpents: but Aaron's rod swallowed up their rods.",
      "M": "Each man threw down his staff and it became a snake. But Aaron's staff swallowed up their staffs.",
      "T": "Every magician's staff became a serpent — but Aaron's serpent devoured them all."
    },
    "13": {
      "L": "And he hardened Pharaoh's heart, that he hearkened not unto them; as the LORD had said.",
      "M": "But Pharaoh's heart was hardened, and he would not listen to them, just as the LORD had said.",
      "T": "Yet Pharaoh's heart remained rigid; he would not listen — exactly as Yahweh had foretold."
    },
    "14": {
      "L": "And the LORD said unto Moses, Pharaoh's heart is hardened, he refuseth to let the people go.",
      "M": "The LORD said to Moses, 'Pharaoh's heart is heavy; he refuses to let the people go.'",
      "T": "Yahweh said to Moses, 'Pharaoh's heart is stone-heavy; he will not release my people.'"
    },
    "15": {
      "L": "Get thee unto Pharaoh in the morning; lo, he goeth out unto the water; and thou shalt stand by the river's brink against he come; and the rod which was turned to a serpent shalt thou take in thine hand.",
      "M": "Go to Pharaoh in the morning. Watch for him as he goes out to the river, and stand on the bank to meet him. Take in your hand the staff that was changed into a snake.",
      "T": "Go to Pharaoh at dawn — he goes out to the Nile. Station yourself on the riverbank to confront him, holding in your hand the staff that became a serpent."
    },
    "16": {
      "L": "And thou shalt say unto him, The LORD God of the Hebrews hath sent me unto thee, saying, Let my people go, that they may serve me in the wilderness: and, behold, hitherto thou wouldest not hear.",
      "M": "Say to him: The LORD, the God of the Hebrews, has sent me to you with this message: Let my people go, so that they may worship me in the wilderness. But up to now you have not listened.",
      "T": "Tell him: Yahweh, the God of the Hebrews, has sent me to you. His demand stands: Release my people so they can worship me in the desert. And still you have not listened."
    },
    "17": {
      "L": "Thus saith the LORD, In this thou shalt know that I am the LORD: behold, I will smite with the rod that is in mine hand upon the waters which are in the river, and they shall be turned to blood.",
      "M": "This is what the LORD says: By this you will know that I am the LORD — I am going to strike the water of the Nile with the staff in my hand, and it will be changed into blood.",
      "T": "Yahweh's word to you: Here is how you will know that I am Yahweh — I will strike the waters of the Nile with this staff, and they will turn to blood."
    },
    "18": {
      "L": "And the fish that is in the river shall die, and the river shall stink; and the Egyptians shall lothe to drink of the water of the river.",
      "M": "The fish in the Nile will die, and the river will stink so badly that the Egyptians will not be able to drink its water.",
      "T": "The fish will die, the river will reek, and Egypt will gag at the very water they live by."
    },
    "19": {
      "L": "And the LORD spake unto Moses, Say unto Aaron, Take thy rod, and stretch out thine hand upon the waters of Egypt, upon their streams, upon their rivers, and upon their ponds, and upon all their pools of water, that they may become blood; and that there may be blood throughout all the land of Egypt, both in vessels of wood, and in vessels of stone.",
      "M": "The LORD said to Moses, 'Tell Aaron: Take your staff and stretch out your hand over the waters of Egypt — over its rivers, canals, ponds, and all its reservoirs — and they will become blood. There will be blood throughout the whole land of Egypt, even in wooden and stone containers.'",
      "T": "Yahweh told Moses to instruct Aaron: Extend your staff over all of Egypt's waters — the Nile, canals, ponds, every reservoir — and they will become blood. Blood will saturate the entire land, even the water stored in wooden and stone vessels."
    },
    "20": {
      "L": "And Moses and Aaron did so, as the LORD commanded; and he lifted up the rod, and smote the waters that were in the river, in the sight of Pharaoh, and in the sight of his servants; and all the waters that were in the river were turned to blood.",
      "M": "Moses and Aaron did just as the LORD commanded. In full view of Pharaoh and his officials, Aaron raised the staff and struck the water of the Nile, and all the water was turned to blood.",
      "T": "Moses and Aaron obeyed Yahweh's command. Aaron raised the staff and struck the Nile in plain sight of Pharaoh and his court — and the entire river ran with blood."
    },
    "21": {
      "L": "And the fish that was in the river died; and the river stank, and the Egyptians could not drink of the water of the river; and there was blood throughout all the land of Egypt.",
      "M": "The fish in the Nile died, and the river smelled so bad that the Egyptians could not drink its water. Blood was everywhere throughout Egypt.",
      "T": "The fish died. The river reeked. Egypt could not drink from the Nile. Blood had spread through the whole land."
    },
    "22": {
      "L": "And the magicians of Egypt did so with their enchantments: and Pharaoh's heart was hardened, neither did he hearken unto them; as the LORD had said.",
      "M": "But the Egyptian magicians did the same thing with their secret arts, and Pharaoh's heart was hardened; he would not listen to Moses and Aaron, just as the LORD had said.",
      "T": "The Egyptian magicians performed the same act with their secret arts — a hollow triumph over waters already ruined. Pharaoh's heart stayed rigid; he would not listen, exactly as Yahweh had said."
    },
    "23": {
      "L": "And Pharaoh turned and went into his house, neither did he set his heart to this also.",
      "M": "Pharaoh turned and went into his palace, paying no attention to this either.",
      "T": "Pharaoh turned his back and walked into his palace, his heart untouched by the ruined river."
    },
    "24": {
      "L": "And all the Egyptians digged round about the river for water to drink; for they could not drink of the water of the river.",
      "M": "All the Egyptians dug along the banks of the Nile for drinking water, because they could not drink the river water.",
      "T": "All across Egypt people dug along the riverbank, searching for water they could actually drink — the Nile itself was useless."
    },
    "25": {
      "L": "And seven days were fulfilled, after that the LORD had smitten the river.",
      "M": "Seven days passed after the LORD had struck the Nile.",
      "T": "Seven days went by from the time Yahweh had struck the Nile."
    }
  },
  "8": {
    "1": {
      "L": "And the LORD spake unto Moses, Go unto Pharaoh, and say unto him, Thus saith the LORD, Let my people go, that they may serve me.",
      "M": "Then the LORD said to Moses, 'Go to Pharaoh and say to him: This is what the LORD says — Let my people go, so that they may worship me.'",
      "T": "Yahweh said to Moses, 'Go back to Pharaoh and deliver this: Yahweh demands it — release my people so they can worship me.'"
    },
    "2": {
      "L": "And if thou refuse to let them go, behold, I will smite all thy borders with frogs.",
      "M": "If you refuse to let them go, I will plague your whole country with frogs.",
      "T": "If you still refuse, I will send frogs swarming across every inch of your land."
    },
    "3": {
      "L": "And the river shall bring forth frogs abundantly, which shall go up and come into thine house, and into thy bedchamber, and upon thy bed, and into the house of thy servants, and upon thy people, and into thine ovens, and into thy kneadingtroughs.",
      "M": "The Nile will teem with frogs. They will come up and enter your palace, your bedroom, your bed, the houses of your officials and your people, and even your ovens and kneading bowls.",
      "T": "The Nile will vomit frogs. They will crawl into your palace, invade your bedroom, climb onto your bed, overrun your servants' quarters, infest your people's homes — even your ovens and bread bowls will be thick with them."
    },
    "4": {
      "L": "And the frogs shall come up both on thee, and upon thy people, and upon all thy servants.",
      "M": "The frogs will swarm over you, your people, and all your officials.",
      "T": "Frogs will crawl on you personally, on your people, on every one of your courtiers."
    },
    "5": {
      "L": "And the LORD spake unto Moses, Say unto Aaron, Stretch forth thine hand with thy rod over the streams, over the rivers, and over the ponds, and cause frogs to come up upon the land of Egypt.",
      "M": "The LORD said to Moses, 'Tell Aaron: Stretch out your hand with your staff over the rivers, canals, and ponds, and make frogs come up onto the land of Egypt.'",
      "T": "Yahweh told Moses to instruct Aaron: Extend your staff over Egypt's rivers, canals, and ponds — command the frogs up onto the land."
    },
    "6": {
      "L": "And Aaron stretched out his hand over the waters of Egypt; and the frogs came up, and covered the land of Egypt.",
      "M": "So Aaron stretched out his hand over the waters of Egypt, and frogs came up and covered the land.",
      "T": "Aaron extended his hand over Egypt's waters — and frogs came up and blanketed the land."
    },
    "7": {
      "L": "And the magicians did so with their enchantments, and brought up frogs upon the land of Egypt.",
      "M": "The magicians did the same with their secret arts and brought up more frogs over Egypt.",
      "T": "The magicians matched them with their occult arts — producing yet more frogs on an already smothered land."
    },
    "8": {
      "L": "Then Pharaoh called for Moses and Aaron, and said, Intreat the LORD, that he may take away the frogs from me, and from my people; and I will let the people go, that they may do sacrifice unto the LORD.",
      "M": "Pharaoh summoned Moses and Aaron and said, 'Pray to the LORD to take the frogs away from me and my people, and I will let the people go to offer sacrifices to the LORD.'",
      "T": "Pharaoh summoned Moses and Aaron. 'Pray to the LORD,' he said, 'and get rid of these frogs. Then I will let the people go to sacrifice to the LORD.'"
    },
    "9": {
      "L": "And Moses said unto Pharaoh, Glory over me: when shall I intreat for thee, and for thy servants, and for thy people, to destroy the frogs from thee and thy houses, that they may remain in the river only?",
      "M": "Moses said to Pharaoh, 'I leave to you the honor of setting the time — when should I pray for you, your officials, and your people, that the frogs be removed from you and your houses and remain only in the Nile?'",
      "T": "Moses replied, 'Name the hour — when would you like me to pray for you, your court, and your people, that the frogs be driven back to the Nile alone? The choice is yours.'"
    },
    "10": {
      "L": "And he said, To morrow. And he said, Be it according to thy word: that thou mayest know that there is none like unto the LORD our God.",
      "M": "Pharaoh said, 'Tomorrow.' Moses answered, 'It will be as you say — so that you may know there is no one like the LORD our God.'",
      "T": "'Tomorrow,' said Pharaoh. Moses answered, 'Done — so that you will know there is no one like Yahweh our God.'"
    },
    "11": {
      "L": "And the frogs shall depart from thee, and from thy houses, and from thy servants, and from thy people; they shall remain in the river only.",
      "M": "The frogs will leave you and your houses, your officials and your people; they will remain only in the Nile.",
      "T": "The frogs will withdraw from you, your palace, your officials, and your people — retreating to the Nile alone."
    },
    "12": {
      "L": "And Moses and Aaron went out from Pharaoh: and Moses cried unto the LORD because of the frogs which he had brought against Pharaoh.",
      "M": "After Moses and Aaron left Pharaoh, Moses cried out to the LORD about the frogs he had brought on Pharaoh.",
      "T": "Moses and Aaron left Pharaoh's presence, and Moses called out to Yahweh about the frogs he had unleashed on Egypt."
    },
    "13": {
      "L": "And the LORD did according to the word of Moses; and the frogs died out of the houses, out of the villages, and out of the fields.",
      "M": "The LORD did what Moses asked. The frogs died in the houses, the courtyards, and the fields.",
      "T": "Yahweh answered Moses' prayer. Frogs died everywhere — in the houses, the yards, the open fields."
    },
    "14": {
      "L": "And they gathered them together upon heaps: and the land stank.",
      "M": "People piled them into great heaps, and the land reeked.",
      "T": "The Egyptians heaped the dead frogs into mounds — and the whole land stank."
    },
    "15": {
      "L": "But when Pharaoh saw that there was respite, he hardened his heart, and hearkened not unto them; as the LORD had said.",
      "M": "But when Pharaoh saw that there was relief, he hardened his heart and would not listen to Moses and Aaron, just as the LORD had said.",
      "T": "The moment Pharaoh had breathing room, his heart turned to stone again. He refused to listen — exactly as Yahweh had said."
    },
    "16": {
      "L": "And the LORD said unto Moses, Say unto Aaron, Stretch out thy rod, and smite the dust of the land, that it may become lice throughout all the land of Egypt.",
      "M": "Then the LORD said to Moses, 'Tell Aaron: Stretch out your staff and strike the dust of the ground, and it will become gnats throughout all of Egypt.'",
      "T": "Yahweh said to Moses, 'Tell Aaron to strike the dust of the earth with his staff — it will swarm into gnats across the entire land of Egypt.'"
    },
    "17": {
      "L": "And they did so; for Aaron stretched out his hand with his rod, and smote the dust of the earth, and it became lice in man, and in beast; all the dust of the land became lice throughout all the land of Egypt.",
      "M": "They did this. Aaron stretched out his staff and struck the ground, and the dust turned into gnats on people and animals throughout all the land of Egypt.",
      "T": "Aaron raised his staff and struck the earth — and all the dust of Egypt became gnats, swarming on humans and animals alike, everywhere."
    },
    "18": {
      "L": "And the magicians did so with their enchantments to bring forth lice, but they could not: so there were lice upon man, and upon beast.",
      "M": "The magicians tried to produce gnats with their secret arts, but they could not. The gnats were on people and animals.",
      "T": "The magicians attempted to replicate this — and failed. Their power had reached its limit. Gnats covered people and animals with no remedy."
    },
    "19": {
      "L": "Then the magicians said unto Pharaoh, This is the finger of God: and Pharaoh's heart was hardened, and he hearkened not unto them; as the LORD had said.",
      "M": "The magicians said to Pharaoh, 'This is the finger of God!' But Pharaoh's heart was hardened and he would not listen to them, just as the LORD had said.",
      "T": "The magicians admitted to Pharaoh: 'This is the finger of God.' Even so, Pharaoh's heart stayed rigid and he would not listen — as Yahweh had said."
    },
    "20": {
      "L": "And the LORD said unto Moses, Rise up early in the morning, and stand before Pharaoh; lo, he cometh forth to the water; and say unto him, Thus saith the LORD, Let my people go, that they may serve me.",
      "M": "The LORD said to Moses, 'Get up early in the morning and confront Pharaoh as he goes to the water. Say to him: This is what the LORD says — Let my people go, so that they may worship me.'",
      "T": "Yahweh said to Moses, 'Be up early — go meet Pharaoh when he goes to the Nile. Give him this: Yahweh's demand stands — release my people so they can worship me.'"
    },
    "21": {
      "L": "Else, if thou wilt not let my people go, behold, I will send swarms of flies upon thee, and upon thy servants, and upon thy people, and into thy houses: and the houses of the Egyptians shall be full of swarms of flies, and also the ground whereon they are.",
      "M": "If you will not let my people go, I will send swarms of flies on you, your officials, your people, and into your houses. Egyptian homes will be full of flies, and so will the ground.",
      "T": "If you will not let them go, I will unleash swarms of flies on you, your court, your people, and their homes. Egypt will drown in flies — on people, in houses, covering the very ground."
    },
    "22": {
      "L": "And I will sever in that day the land of Goshen, in which my people dwell, that no swarms of flies shall be there; to the end thou mayest know that I am the LORD in the midst of the earth.",
      "M": "But I will set apart the land of Goshen, where my people live, so that no flies will be there. By this you will know that I, the LORD, am at work in the midst of this land.",
      "T": "But Goshen — where my people dwell — will be exempt. Not a single fly will land there. This distinction will prove to you that I, Yahweh, am at work right here in the middle of this land."
    },
    "23": {
      "L": "And I will put a division between my people and thy people: to morrow shall this sign be.",
      "M": "I will make a distinction between my people and your people. This sign will occur tomorrow.",
      "T": "I am drawing a clear line between my people and yours. Tomorrow this sign will appear."
    },
    "24": {
      "L": "And the LORD did so; and there came a grievous swarm of flies into the house of Pharaoh, and into his servants' houses, and into all the land of Egypt: the land was corrupted by reason of the swarm of flies.",
      "M": "The LORD did this. Dense swarms of flies poured into Pharaoh's palace and the houses of his officials, and throughout Egypt. The land was ruined by the flies.",
      "T": "Yahweh delivered. Thick swarms of flies flooded into Pharaoh's palace, his courtiers' homes, and all across Egypt — the land was devastated by the infestation."
    },
    "25": {
      "L": "And Pharaoh called for Moses and for Aaron, and said, Go ye, sacrifice to your God in the land.",
      "M": "Pharaoh summoned Moses and Aaron and said, 'Go, sacrifice to your God — but do it here in the land.'",
      "T": "Pharaoh called Moses and Aaron in. 'Fine,' he said, 'go sacrifice to your God — but stay within this land.'"
    },
    "26": {
      "L": "And Moses said, It is not meet so to do; for we shall sacrifice the abomination of the Egyptians to the LORD our God: lo, shall we sacrifice the abomination of the Egyptians before their eyes, and will they not stone us?",
      "M": "But Moses said, 'That would not be right. The sacrifices we offer to the LORD our God are detestable to the Egyptians. If we sacrifice what is offensive to them right in front of them, won't they stone us?'",
      "T": "Moses refused: 'That cannot work. The animals we must sacrifice to Yahweh our God are held sacred by the Egyptians — if we slaughter them before their eyes, they will stone us.'"
    },
    "27": {
      "L": "We will go three days' journey into the wilderness, and sacrifice to the LORD our God, as he shall command us.",
      "M": "We must take a three-day journey into the wilderness to offer sacrifices to the LORD our God, as he commands us.",
      "T": "We must travel three days into the desert to sacrifice to Yahweh our God as he directs us — no other arrangement will do."
    },
    "28": {
      "L": "And Pharaoh said, I will let you go, that ye may sacrifice to the LORD your God in the wilderness; only ye shall not go very far away: intreat for me.",
      "M": "Pharaoh said, 'I will let you go to sacrifice to the LORD your God in the wilderness, but you must not go very far. And pray for me.'",
      "T": "Pharaoh relented: 'I will let you go sacrifice to Yahweh your God in the desert — but not far. And pray for me.'"
    },
    "29": {
      "L": "And Moses said, Behold, I will go out from thee, and I will intreat the LORD that the swarms of flies may depart from Pharaoh, from his servants, and from his people, to morrow: but let not Pharaoh deal deceitfully any more in not letting the people go to sacrifice to the LORD.",
      "M": "Moses replied, 'As soon as I leave you, I will pray to the LORD, and tomorrow the flies will depart from Pharaoh, his officials, and his people. But Pharaoh must not be deceitful again by refusing to let the people go to sacrifice to the LORD.'",
      "T": "'When I walk out of here,' Moses said, 'I will pray to Yahweh — and tomorrow the flies will leave you, your court, and your people. But Pharaoh must stop playing games. No more breaking your word about letting the people go.'"
    },
    "30": {
      "L": "And Moses went out from Pharaoh, and intreated the LORD.",
      "M": "Then Moses left Pharaoh and prayed to the LORD.",
      "T": "Moses went out from Pharaoh's presence and prayed to Yahweh."
    },
    "31": {
      "L": "And the LORD did according to the word of Moses; and he removed the swarms of flies from Pharaoh, from his servants, and from his people; there remained not one.",
      "M": "The LORD did what Moses asked and removed the flies from Pharaoh, his officials, and his people — not a single fly remained.",
      "T": "Yahweh answered. Every fly was removed from Pharaoh, his court, and all his people. Not one remained."
    },
    "32": {
      "L": "And Pharaoh hardened his heart at this time also, neither would he let the people go.",
      "M": "But Pharaoh hardened his heart even this time and would not let the people go.",
      "T": "But Pharaoh hardened his heart again. This time too he refused to let the people go."
    }
  },
  "9": {
    "1": {
      "L": "Then the LORD said unto Moses, Go in unto Pharaoh, and tell him, Thus saith the LORD God of the Hebrews, Let my people go, that they may serve me.",
      "M": "The LORD said to Moses, 'Go to Pharaoh and tell him: This is what the LORD, the God of the Hebrews, says — Let my people go, so that they may worship me.'",
      "T": "Yahweh said to Moses, 'Go back to Pharaoh. This is Yahweh the God of the Hebrews speaking: Release my people so they can worship me.'"
    },
    "2": {
      "L": "For if thou refuse to let them go, and wilt hold them still:",
      "M": "If you refuse to let them go and continue to hold them,",
      "T": "If you refuse again and keep holding them back,"
    },
    "3": {
      "L": "Behold, the hand of the LORD is upon thy cattle which is in the field, upon the horses, upon the asses, upon the camels, upon the oxen, and upon the sheep: there shall be a very grievous murrain.",
      "M": "the hand of the LORD will bring a severe plague on your livestock that are in the field — your horses, donkeys, camels, cattle, and sheep.",
      "T": "the hand of Yahweh will fall on your field animals — your horses, donkeys, camels, oxen, and flocks — with a devastating plague."
    },
    "4": {
      "L": "And the LORD shall sever between the cattle of Israel and the cattle of Egypt: and there shall nothing die of all that is the children's of Israel.",
      "M": "But the LORD will make a distinction between Israel's livestock and Egypt's. Not one animal belonging to the Israelites will die.",
      "T": "But Yahweh will draw a line between Israel's animals and Egypt's. Not one belonging to Israel will die."
    },
    "5": {
      "L": "And the LORD appointed a set time, saying, To morrow the LORD shall do this thing in the land.",
      "M": "The LORD set a time and said, 'Tomorrow the LORD will do this throughout the land.'",
      "T": "Yahweh set the hour: 'Tomorrow I will do this across the land.'"
    },
    "6": {
      "L": "And the LORD did that thing on the morrow, and all the cattle of Egypt died: but of the cattle of the children of Israel died not one.",
      "M": "The next day the LORD did it. All the livestock of the Egyptians died, but not one of the Israelites' animals died.",
      "T": "The next day Yahweh did it. Every animal Egypt owned in the field was dead — but among Israel's herds, not one had fallen."
    },
    "7": {
      "L": "And Pharaoh sent, and, behold, there was not one of the cattle of the Israelites dead. And the heart of Pharaoh was hardened, and he did not let the people go.",
      "M": "Pharaoh sent messengers to investigate, and indeed not a single one of Israel's animals had died. Yet Pharaoh's heart was hardened, and he would not let the people go.",
      "T": "Pharaoh sent to verify — and confirmed: not one Israelite animal was dead. Even then his heart stayed hard, and he would not let the people go."
    },
    "8": {
      "L": "And the LORD said unto Moses and unto Aaron, Take to you handfuls of ashes of the furnace, and let Moses sprinkle it toward the heaven in the sight of Pharaoh.",
      "M": "Then the LORD said to Moses and Aaron, 'Take handfuls of furnace soot and have Moses toss it into the air in the presence of Pharaoh.'",
      "T": "Yahweh told Moses and Aaron: 'Take handfuls of furnace soot and let Moses throw it toward the sky in Pharaoh's presence.'"
    },
    "9": {
      "L": "And it shall become small dust in all the land of Egypt, and shall be a boil breaking forth with blains upon man, and upon beast, throughout all the land of Egypt.",
      "M": "It will become fine dust over all of Egypt, and festering boils will break out on people and animals throughout the land.",
      "T": "It will scatter as fine dust over all Egypt and break out as festering sores on people and animals across the whole land."
    },
    "10": {
      "L": "And they took ashes of the furnace, and stood before Pharaoh; and Moses sprinkled it up toward heaven; and it became a boil breaking forth with blains upon man, and upon beast.",
      "M": "So they took furnace soot, stood before Pharaoh, and Moses threw it into the air. Festering boils broke out on people and animals.",
      "T": "They gathered the soot, stood before Pharaoh, and Moses flung it skyward — and festering boils erupted on people and animals throughout Egypt."
    },
    "11": {
      "L": "And the magicians could not stand before Moses because of the boils; for the boil was upon the magicians, and upon all the Egyptians.",
      "M": "The magicians could not even stand before Moses because of the boils; they were afflicted like all the other Egyptians.",
      "T": "The magicians could not even appear before Moses — they were covered in sores like everyone else. Egypt's occult professionals were helpless."
    },
    "12": {
      "L": "And the LORD hardened the heart of Pharaoh, and he hearkened not unto them; as the LORD had spoken unto Moses.",
      "M": "But the LORD hardened Pharaoh's heart, and he would not listen to Moses and Aaron, just as the LORD had said to Moses.",
      "T": "Yahweh himself hardened Pharaoh's heart — and Pharaoh would not listen, exactly as Yahweh had told Moses would happen."
    },
    "13": {
      "L": "And the LORD said unto Moses, Rise up early in the morning, and stand before Pharaoh, and say unto him, Thus saith the LORD God of the Hebrews, Let my people go, that they may serve me.",
      "M": "Then the LORD said to Moses, 'Get up early in the morning and stand before Pharaoh. Say to him: This is what the LORD, the God of the Hebrews, says — Let my people go, so that they may worship me.'",
      "T": "Yahweh said to Moses, 'Be up early and station yourself before Pharaoh. This is Yahweh the God of the Hebrews: Let my people go to worship me.'"
    },
    "14": {
      "L": "For I will at this time send all my plagues upon thine heart, and upon thy servants, and upon thy people; that thou mayest know that there is none like me in all the earth.",
      "M": "For this time I will send all my plagues against you personally, your officials, and your people, so that you may know there is no one like me in all the earth.",
      "T": "This time I am sending the full force of my judgments against you personally, your court, and your people — so you will know that there is no one like me anywhere on earth."
    },
    "15": {
      "L": "For now I will stretch out my hand, that I may smite thee and thy people with pestilence; and thou shalt be cut off from the earth.",
      "M": "For by now I could have stretched out my hand and struck you and your people with a plague that would have wiped you from the earth.",
      "T": "I could already have reached out and struck you and your people with a plague that erased you from the earth."
    },
    "16": {
      "L": "And in very deed for this cause have I raised thee up, for to shew in thee my power; and that my name may be declared throughout all the earth.",
      "M": "But I have raised you up for this very purpose: to display my power through you and to make my name known throughout all the earth.",
      "T": "But this is why I have let you stand — to display my power through you, so that my name would be proclaimed across the whole earth."
    },
    "17": {
      "L": "As yet exaltest thou thyself against my people, that thou wilt not let them go?",
      "M": "You are still setting yourself against my people by refusing to let them go.",
      "T": "And still you set yourself up against my people. Still you refuse to release them."
    },
    "18": {
      "L": "Behold, to morrow about this time I will cause it to rain a very grievous hail, such as hath not been in Egypt since the foundation thereof even until now.",
      "M": "Therefore, tomorrow at this time I will send the most severe hailstorm that has ever fallen on Egypt, from the day it was founded until now.",
      "T": "Tomorrow at this very hour I will unleash hail the likes of which Egypt has never seen — from its founding down to this moment."
    },
    "19": {
      "L": "Send therefore now, and gather thy cattle, and all that thou hast in the field; for upon every man and beast which shall be found in the field, and shall not be brought home, the hail shall come down upon them, and they shall die.",
      "M": "Give the order now to bring your livestock and everything in the field to shelter. Every person and animal left in the field will die when the hail falls on them.",
      "T": "Send word now: bring every animal and every person in from the open fields. Anything left unprotected when the hail falls will die."
    },
    "20": {
      "L": "He that feared the word of the LORD among the servants of Pharaoh made his servants and his cattle flee into the houses.",
      "M": "Those among Pharaoh's officials who feared the word of the LORD rushed their servants and livestock inside.",
      "T": "The officials who took Yahweh's warning seriously brought their servants and animals indoors without delay."
    },
    "21": {
      "L": "And he that regarded not the word of the LORD left his servants and his cattle in the field.",
      "M": "But those who disregarded the word of the LORD left their servants and animals in the field.",
      "T": "Those who dismissed Yahweh's word left their people and animals in the open."
    },
    "22": {
      "L": "And the LORD said unto Moses, Stretch forth thine hand toward heaven, that there may be hail in all the land of Egypt, upon man, and upon beast, and upon every herb of the field, throughout the land of Egypt.",
      "M": "Then the LORD said to Moses, 'Stretch out your hand toward the sky so that hail will fall all over Egypt — on people, animals, and everything growing in the fields.'",
      "T": "Yahweh said to Moses, 'Raise your hand toward the sky — hail will fall across all Egypt, on people, on animals, on every plant growing in the open field.'"
    },
    "23": {
      "L": "And Moses stretched forth his rod toward heaven: and the LORD sent thunder and hail, and the fire ran along upon the ground; and the LORD rained hail upon the land of Egypt.",
      "M": "When Moses raised his staff toward the sky, the LORD sent thunder and hail, and lightning flashed down to the ground. The LORD rained hail on the land of Egypt.",
      "T": "Moses lifted his staff skyward — and Yahweh unleashed thunder, hail, and lightning searing across the ground. Yahweh rained hail on the land of Egypt."
    },
    "24": {
      "L": "So there was hail, and fire mingled with the hail, very grievous, such as there was none like it in all the land of Egypt since it became a nation.",
      "M": "The hail was very severe, with lightning flashing through it — the worst storm in the history of Egypt as a nation.",
      "T": "Hail and lightning struck together — a violent, unprecedented storm. Nothing like it had ever fallen on Egypt in all its history."
    },
    "25": {
      "L": "And the hail smote throughout all the land of Egypt all that was in the field, both man and beast; and the hail smote every herb of the field, and brake every tree of the field.",
      "M": "The hail struck down everything in the fields throughout Egypt — people, animals, and all the crops. It beat down every plant and shattered every tree.",
      "T": "The hail struck everything in the open across Egypt — people, animals, crops, trees. Nothing standing in the field was spared."
    },
    "26": {
      "L": "Only in the land of Goshen, where the children of Israel were, was there no hail.",
      "M": "Only in the land of Goshen, where the Israelites lived, was there no hail.",
      "T": "Only in Goshen — where Israel lived — did no hail fall."
    },
    "27": {
      "L": "And Pharaoh sent, and called for Moses and Aaron, and said unto them, I have sinned this time: the LORD is righteous, and I and my people are wicked.",
      "M": "Pharaoh sent for Moses and Aaron. 'This time I have sinned,' he said. 'The LORD is in the right, and I and my people are in the wrong.'",
      "T": "Pharaoh sent for Moses and Aaron. 'I have sinned this time,' he confessed. 'Yahweh is right. I and my people are in the wrong.'"
    },
    "28": {
      "L": "Intreat the LORD (for it is enough) that there be no more mighty thunderings and hail; and I will let you go, and ye shall stay no longer.",
      "M": "Pray to the LORD, for there has been enough of this deadly thunder and hail. I will let you go; you will not need to stay any longer.",
      "T": "'Pray to Yahweh — this thunder and hail have gone on long enough and it is killing us. I will release you; you won't need to stay another day.'"
    },
    "29": {
      "L": "And Moses said unto him, As soon as I am gone out of the city, I will spread abroad my hands unto the LORD; and the thunder shall cease, neither shall there be any more hail; that thou mayest know how that the earth is the LORD's.",
      "M": "Moses replied, 'As soon as I leave the city, I will spread out my hands to the LORD. The thunder will stop and there will be no more hail, so that you may know that the earth belongs to the LORD.'",
      "T": "'The moment I leave the city,' Moses answered, 'I will spread out my hands toward Yahweh — and the thunder and hail will cease. You will know then that the whole earth belongs to Yahweh.'"
    },
    "30": {
      "L": "But as for thee and thy servants, I know that ye will not yet fear the LORD God.",
      "M": "But as for you and your officials, I know that you still do not truly fear the LORD God.",
      "T": "'But I know you, Pharaoh — you and your officials still do not genuinely fear Yahweh God.'"
    },
    "31": {
      "L": "And the flax and the barley was smitten: for the barley was in the ear, and the flax was bolled.",
      "M": "The flax and barley were ruined because the barley had headed out and the flax was in bloom.",
      "T": "The flax was destroyed — it was in full bloom — and the barley with it, for the barley had already formed its heads."
    },
    "32": {
      "L": "But the wheat and the rie were not smitten: for they were not grown up.",
      "M": "But the wheat and spelt were not ruined because they ripen later.",
      "T": "The wheat and spelt, however, escaped — they were still young and not yet up."
    },
    "33": {
      "L": "And Moses went out of the city from Pharaoh, and spread abroad his hands unto the LORD: and the thunders and hail ceased, and the rain was not poured upon the earth.",
      "M": "Moses left Pharaoh and went outside the city. He spread out his hands toward the LORD, and the thunder and hail stopped and the rain no longer poured down.",
      "T": "Moses left Pharaoh and walked outside the city. He spread his hands toward Yahweh — and the thunder stopped, the hail stopped, the rain ceased."
    },
    "34": {
      "L": "And when Pharaoh saw that the rain and the hail and the thunders were ceased, he sinned yet more, and hardened his heart, he and his servants.",
      "M": "But when Pharaoh saw that the rain, hail, and thunder had stopped, he sinned again and hardened his heart — he and his officials.",
      "T": "The moment Pharaoh saw the storm was over, he sinned again. He and his officials hardened their hearts once more."
    },
    "35": {
      "L": "And the heart of Pharaoh was hardened, neither would he let the children of Israel go; as the LORD had spoken by Moses.",
      "M": "Pharaoh's heart was hardened, and he would not let the Israelites go, just as the LORD had said through Moses.",
      "T": "Pharaoh's heart stayed stone-hard — he would not let the children of Israel go. It was exactly as Yahweh had told Moses."
    }
  },
  "10": {
    "1": {
      "L": "And the LORD said unto Moses, Go in unto Pharaoh: for I have hardened his heart, and the heart of his servants, that I might shew these my signs before him.",
      "M": "Then the LORD said to Moses, 'Go to Pharaoh, for I have hardened his heart and the hearts of his officials so that I may perform these signs of mine among them.'",
      "T": "Yahweh said to Moses, 'Go to Pharaoh. I have hardened his heart and his officials' hearts so that I could display these signs of mine among them.'"
    },
    "2": {
      "L": "And that thou mayest tell in the ears of thy son, and of thy son's son, what things I have wrought in Egypt, and my signs which I have done among them; that ye may know how that I am the LORD.",
      "M": "And so that you may tell your children and grandchildren how I dealt with the Egyptians and performed my signs among them, and that you may know that I am the LORD.",
      "T": "And so that you will have this story to tell — your children and grandchildren will hear how I dealt with Egypt, what signs I showed there. That is how every generation will know: I am Yahweh."
    },
    "3": {
      "L": "And Moses and Aaron came in unto Pharaoh, and said unto him, Thus saith the LORD God of the Hebrews, How long wilt thou refuse to humble thyself before me? let my people go, that they may serve me.",
      "M": "So Moses and Aaron went to Pharaoh and said to him, 'This is what the LORD, the God of the Hebrews, says: How long will you refuse to humble yourself before me? Let my people go, so that they may worship me.'",
      "T": "Moses and Aaron came before Pharaoh. 'This is Yahweh the God of the Hebrews speaking: How long will you refuse to bow before me? Let my people go to worship me.'"
    },
    "4": {
      "L": "Else, if thou refuse to let my people go, behold, to morrow will I bring the locusts into thy coast.",
      "M": "If you refuse to let my people go, I will bring locusts into your land tomorrow.",
      "T": "If you refuse again, tomorrow I will bring locusts swarming into your country."
    },
    "5": {
      "L": "And they shall cover the face of the earth, that one cannot be able to see the earth: and they shall eat the residue of that which is escaped, which remaineth unto you from the hail, and shall eat every tree which groweth for you out of the field.",
      "M": "They will cover the ground until it cannot be seen. They will devour what little escaped the hail and eat every tree still growing in your fields.",
      "T": "They will blanket the ground until you cannot see the earth. They will devour every plant the hail left standing — and strip every tree still growing in your fields."
    },
    "6": {
      "L": "And they shall fill thy houses, and the houses of all thy servants, and the houses of all the Egyptians; which neither thy fathers, nor thy fathers' fathers have seen, since the day that they were upon the earth unto this day. And he turned himself, and went out from Pharaoh.",
      "M": "They will fill your palace and the houses of all your officials and all the Egyptians — something neither your fathers nor your forefathers have ever seen since the day they lived on this earth.' Then Moses turned and left Pharaoh.",
      "T": "They will pour into your palace, your officials' homes, every Egyptian household — the likes of which your ancestors never witnessed in all their days on earth.' Moses turned and walked out of Pharaoh's presence."
    },
    "7": {
      "L": "And Pharaoh's servants said unto him, How long shall this man be a snare unto us? let the men go, that they may serve the LORD their God: knowest thou not yet that Egypt is destroyed?",
      "M": "Pharaoh's officials said to him, 'How long will this man be a trap for us? Let the Israelites go to worship the LORD their God. Don't you realize that Egypt is ruined?'",
      "T": "Pharaoh's own officials said to him, 'How long are you going to let this man destroy us? Let the people go to worship Yahweh their God. Can you not see that Egypt is already finished?'"
    },
    "8": {
      "L": "And Moses and Aaron were brought again unto Pharaoh: and he said unto them, Go, serve the LORD your God: but who are they that shall go?",
      "M": "So Moses and Aaron were brought back to Pharaoh, and he said to them, 'Go, worship the LORD your God. But exactly who will be going?'",
      "T": "Moses and Aaron were brought back to Pharaoh, who said, 'Go ahead — worship Yahweh your God. But which ones exactly are going?'"
    },
    "9": {
      "L": "And Moses said, We will go with our young and with our old, with our sons and with our daughters, with our flocks and with our herds will we go; for we must hold a feast unto the LORD.",
      "M": "Moses answered, 'We will go with our young and old, our sons and daughters, and our flocks and herds, because we are to celebrate a festival to the LORD.'",
      "T": "Moses answered, 'Everyone is going — young and old, sons and daughters, our flocks and herds — because we have a feast to celebrate before Yahweh.'"
    },
    "10": {
      "L": "And he said unto them, Let the LORD be so with you, as I will let you go, and your little ones: look to it; for evil is before you.",
      "M": "Pharaoh said, 'The LORD be with you — if I let you and your little ones go! Clearly you are bent on mischief.'",
      "T": "'The LORD be with you indeed!' Pharaoh replied sarcastically. 'You think I'm letting you take your children? You're obviously planning far more than you've admitted.'"
    },
    "11": {
      "L": "Not so: go now ye that are men, and serve the LORD; for that did ye desire. And they were driven out from Pharaoh's presence.",
      "M": "No — just the men may go and worship the LORD, since that's what you've been asking for.' And Moses and Aaron were driven away from Pharaoh's presence.",
      "T": "'No. The men can go and worship Yahweh — that's all you asked for in the first place.' And they were expelled from Pharaoh's presence."
    },
    "12": {
      "L": "And the LORD said unto Moses, Stretch out thine hand over the land of Egypt for the locusts, that they may come up upon the land of Egypt, and eat every herb of the land, even all that the hail hath left.",
      "M": "Then the LORD said to Moses, 'Stretch out your hand over Egypt so that the locusts swarm over the land and devour everything the hail has left.'",
      "T": "Yahweh said to Moses, 'Stretch your hand over Egypt — let the locusts come up and eat every plant the hail left standing.'"
    },
    "13": {
      "L": "And Moses stretched forth his rod over the land of Egypt, and the LORD brought an east wind upon the land all that day, and all that night; and when it was morning, the east wind brought the locusts.",
      "M": "So Moses stretched out his staff over Egypt, and the LORD made an east wind blow across the land all that day and all that night. By morning the east wind had brought the locusts.",
      "T": "Moses raised his staff over Egypt. Yahweh drove an east wind across the land all day and through the night — and by morning the east wind had brought the locusts."
    },
    "14": {
      "L": "And the locusts went up over all the land of Egypt, and rested in all the coasts of Egypt: very grievous were they; before them there were no such locusts as they, neither after them shall there be such.",
      "M": "The locusts invaded all of Egypt and settled throughout the country in great numbers — the worst locust plague there had ever been or would ever be.",
      "T": "The locusts swept across all Egypt and settled throughout the land in massive numbers. Never before had there been such a locust invasion, and never would be again."
    },
    "15": {
      "L": "For they covered the face of the whole earth, so that the land was darkened; and they did eat every herb of the land, and all the fruit of the trees which the hail had left: and there remained not any green thing in the trees, or in the herbs of the field, through all the land of Egypt.",
      "M": "They covered the ground until it was black, and they ate all the plants and all the fruit the hail had left. Nothing green remained on any tree or plant throughout all of Egypt.",
      "T": "They darkened the earth — then devoured it. Every plant, every fruit the hail had spared. Nothing green was left on tree or ground anywhere across Egypt."
    },
    "16": {
      "L": "Then Pharaoh called for Moses and Aaron in haste; and he said, I have sinned against the LORD your God, and against you.",
      "M": "Pharaoh quickly summoned Moses and Aaron and said, 'I have sinned against the LORD your God and against you.'",
      "T": "Pharaoh rushed to summon Moses and Aaron. 'I have sinned,' he said, 'against Yahweh your God and against you.'"
    },
    "17": {
      "L": "Now therefore forgive, I pray thee, my sin only this once, and intreat the LORD your God, that he may take away from me this death only.",
      "M": "Now please forgive my sin just this once, and pray to the LORD your God to remove this deadly plague from me.",
      "T": "'Forgive my sin — just this once — and pray to Yahweh your God to take this death away from me.'"
    },
    "18": {
      "L": "And he went out from Pharaoh, and intreated the LORD.",
      "M": "Moses left Pharaoh and prayed to the LORD.",
      "T": "Moses went out from Pharaoh and prayed to Yahweh."
    },
    "19": {
      "L": "And the LORD turned a mighty strong west wind, which took away the locusts, and cast them into the Red sea; there remained not one locust in all the coasts of Egypt.",
      "M": "The LORD changed the wind to a very strong west wind, which picked up the locusts and drove them into the Red Sea. Not a single locust remained anywhere in Egypt.",
      "T": "Yahweh shifted the wind — a powerful west wind swept up every locust and drove them into the Sea of Reeds. Not one remained in all of Egypt."
    },
    "20": {
      "L": "But the LORD hardened Pharaoh's heart, so that he would not let the children of Israel go.",
      "M": "But the LORD hardened Pharaoh's heart, and he would not let the Israelites go.",
      "T": "But Yahweh hardened Pharaoh's heart, and he would not release the children of Israel."
    },
    "21": {
      "L": "And the LORD said unto Moses, Stretch out thine hand toward heaven, that there may be darkness over the land of Egypt, even darkness which may be felt.",
      "M": "Then the LORD said to Moses, 'Stretch out your hand toward the sky so that darkness will spread over Egypt — darkness that can be felt.'",
      "T": "Yahweh said to Moses, 'Extend your hand toward the sky — a darkness will come over Egypt so thick it can be touched.'"
    },
    "22": {
      "L": "And Moses stretched forth his hand toward heaven; and there was a thick darkness in all the land of Egypt three days.",
      "M": "So Moses stretched out his hand toward the sky, and total darkness covered all Egypt for three days.",
      "T": "Moses raised his hand toward the sky — and a thick, tangible darkness covered all Egypt for three days."
    },
    "23": {
      "L": "They saw not one another, neither rose any from his place for three days: but all the children of Israel had light in their dwellings.",
      "M": "No one could see anyone else, and no one left his place for three days. But all the Israelites had light where they lived.",
      "T": "No one could see another person. No one could move from where they sat. For three days Egypt was a blind nation — but every Israelite home had light."
    },
    "24": {
      "L": "And Pharaoh called unto Moses, and said, Go ye, serve the LORD; only let your flocks and your herds be stayed: your little ones also shall go with you.",
      "M": "Pharaoh summoned Moses and said, 'Go, worship the LORD. Even your children may go with you — only leave your flocks and herds behind.'",
      "T": "Pharaoh called Moses to him. 'Go, worship Yahweh — your children can go too. Just leave your herds and flocks behind.'"
    },
    "25": {
      "L": "And Moses said, Thou must give us also sacrifices and burnt offerings, that we may sacrifice unto the LORD our God.",
      "M": "But Moses said, 'You must provide us with sacrifices and burnt offerings to present to the LORD our God.'",
      "T": "Moses refused: 'You must give us animals for sacrifice and burnt offering to bring to Yahweh our God.'"
    },
    "26": {
      "L": "Our cattle also shall go with us; there shall not an hoof be left behind; for thereof must we take to serve the LORD our God; and we know not with what we must serve the LORD, until we come thither.",
      "M": "Our livestock must go with us — not a hoof is to be left behind. We have to select from them for worshiping the LORD our God, and we will not know what we need until we get there.",
      "T": "'Not a single hoof stays behind — every animal goes with us. We do not yet know exactly what Yahweh will require of us until we arrive and he tells us.'"
    },
    "27": {
      "L": "But the LORD hardened Pharaoh's heart, and he would not let them go.",
      "M": "But the LORD hardened Pharaoh's heart, and he was unwilling to let them go.",
      "T": "But Yahweh hardened Pharaoh's heart, and he refused."
    },
    "28": {
      "L": "And Pharaoh said unto him, Get thee from me, take heed to thyself, see my face no more; for in that day thou seest my face thou shalt die.",
      "M": "Pharaoh said to Moses, 'Get out of my sight! Make sure you never appear before me again. The day you see my face, you will die!'",
      "T": "Pharaoh said to Moses, 'Get out of my presence. Never let me see your face again. The day you appear before me, you die.'"
    },
    "29": {
      "L": "And Moses said, Thou hast spoken well, I will see thy face again no more.",
      "M": "Moses replied, 'Just as you say — I will never appear before you again.'",
      "T": "Moses answered, 'You have spoken well. I will never see your face again.'"
    }
  },
  "11": {
    "1": {
      "L": "And the LORD said unto Moses, Yet will I bring one plague more upon Pharaoh, and upon Egypt; afterwards he will let you go hence: when he shall let you go, he shall surely thrust you out hence altogether.",
      "M": "Now the LORD had said to Moses, 'I will bring one more plague on Pharaoh and on Egypt. After that, he will let you go from here — when he lets you go, he will drive you out completely.'",
      "T": "Yahweh had said to Moses, 'One more plague I will bring on Pharaoh and on Egypt. After that, he will let you go — and when he does, he will drive you out entirely.'"
    },
    "2": {
      "L": "Speak now in the ears of the people, and let every man borrow of his neighbour, and every woman of her neighbour, jewels of silver, and jewels of gold.",
      "M": "Tell the people that men and women alike are to ask their neighbors for articles of silver and gold.",
      "T": "Tell the Israelites — every man and every woman — to ask their Egyptian neighbors for silver and gold jewelry."
    },
    "3": {
      "L": "And the LORD gave the people favour in the sight of the Egyptians. Moreover the man Moses was very great in the land of Egypt, in the sight of Pharaoh's servants, and in the sight of the people.",
      "M": "The LORD made the Egyptians favorably disposed toward the Israelites. Moses himself was highly regarded in Egypt, in the sight of Pharaoh's officials and in the eyes of the people.",
      "T": "Yahweh gave the Israelites such favor in Egyptian eyes that their neighbors were glad to give. By this point Moses himself was held in high respect throughout Egypt — by Pharaoh's officials and by the common people alike."
    },
    "4": {
      "L": "And Moses said, Thus saith the LORD, About midnight will I go out into the midst of Egypt.",
      "M": "So Moses said, 'This is what the LORD says: About midnight I will go throughout Egypt.'",
      "T": "Moses declared to Pharaoh, 'Yahweh's word is this: At midnight I will pass through the midst of Egypt.'"
    },
    "5": {
      "L": "And all the firstborn in the land of Egypt shall die, from the firstborn of Pharaoh that sitteth upon his throne, even unto the firstborn of the servant maid that is behind the mill; and all the firstborn of beasts.",
      "M": "Every firstborn son in Egypt will die, from the firstborn of Pharaoh who sits on his throne to the firstborn of the slave woman at her handmill, and also every firstborn animal.",
      "T": "Every firstborn in Egypt will die — from Pharaoh's heir on the throne to the slave woman's firstborn child at her millstone, and every firstborn animal."
    },
    "6": {
      "L": "And there shall be a great cry throughout all the land of Egypt, such as there was none like it, nor shall be like it any more.",
      "M": "There will be loud wailing throughout Egypt — worse than there has ever been or ever will be.",
      "T": "A cry of anguish will break out across Egypt unlike any the land has ever heard or will hear again."
    },
    "7": {
      "L": "But against any of the children of Israel shall not a dog move his tongue, against man or beast: that ye may know how that the LORD doth put a difference between the Egyptians and Israel.",
      "M": "But among the Israelites, not even a dog will bark at any person or animal. Then you will know that the LORD makes a distinction between Egypt and Israel.",
      "T": "But among all Israel, not even a dog will growl — no person, no animal harmed. This is how you will know that Yahweh draws a sharp line between Egypt and Israel."
    },
    "8": {
      "L": "And all these thy servants shall come down unto me, and bow down themselves unto me, saying, Get thee out, and all the people that follow thee: and after that I will go out. And he went out from Pharaoh in a great anger.",
      "M": "All these officials of yours will come and bow down to me, saying, \"Go, you and all the people who follow you!\" Only then will I leave.' After that, Moses went out from Pharaoh in great anger.",
      "T": "All your officials will come bowing before me, begging: 'Go! Leave! Take everyone who follows you!' Only then will I go.' Moses walked out from Pharaoh's presence burning with anger."
    },
    "9": {
      "L": "And the LORD said unto Moses, Pharaoh shall not hearken unto you; that my wonders may be multiplied in the land of Egypt.",
      "M": "The LORD had said to Moses, 'Pharaoh will not listen to you, so that my wonders may be multiplied in Egypt.'",
      "T": "Yahweh had already told Moses, 'Pharaoh will not listen to you — I am multiplying my wonders throughout Egypt.'"
    },
    "10": {
      "L": "And Moses and Aaron did all these wonders before Pharaoh: and the LORD hardened Pharaoh's heart, so that he would not let the children of Israel go out of his land.",
      "M": "Moses and Aaron performed all these wonders before Pharaoh, but the LORD hardened Pharaoh's heart, and he would not let the Israelites go from his land.",
      "T": "Moses and Aaron performed all these signs before Pharaoh — but Yahweh hardened Pharaoh's heart, and he would not release the children of Israel from his land."
    }
  },
  "12": {
    "1": {
      "L": "And the LORD spake unto Moses and Aaron in the land of Egypt, saying,",
      "M": "The LORD said to Moses and Aaron in Egypt:",
      "T": "In the land of Egypt, Yahweh spoke to Moses and Aaron:"
    },
    "2": {
      "L": "This month shall be unto you the beginning of months: it shall be the first month of the year to you.",
      "M": "This month is to be for you the first month, the first month of your year.",
      "T": "This month is the beginning of months for you — the first month of your year. Your calendar is being reset by this event."
    },
    "3": {
      "L": "Speak ye unto all the congregation of Israel, saying, In the tenth day of this month they shall take to them every man a lamb, according to the house of their fathers, a lamb for an house.",
      "M": "Tell the whole community of Israel that on the tenth day of this month each man is to take a lamb for his family, one for each household.",
      "T": "Announce this to all of Israel: on the tenth day of this month, every household is to take a lamb — one per family unit."
    },
    "4": {
      "L": "And if the household be too little for the lamb, let him and his neighbour next unto his house take it according to the number of the souls; every man according to his eating shall make your count for the lamb.",
      "M": "If a household is too small for a whole lamb, they must share one with their nearest neighbor, taking into account the number of people there are. Determine the amount of lamb needed according to what each person will eat.",
      "T": "If a household is too small to eat a whole lamb, they are to join with their nearest neighbor — calculate how many people there are and how much each person will eat, then divide the lamb accordingly."
    },
    "5": {
      "L": "Your lamb shall be without blemish, a male of the first year: ye shall take it out from the sheep, or from the goats.",
      "M": "The animals you choose must be year-old males without defect, and you may take them from the sheep or the goats.",
      "T": "The animal must be without blemish — a one-year-old male from the sheep or goats."
    },
    "6": {
      "L": "And ye shall keep it up until the fourteenth day of the same month: and the whole assembly of the congregation of Israel shall kill it in the evening.",
      "M": "Take care of it until the fourteenth day of the month, when all the members of the community of Israel must slaughter it at twilight.",
      "T": "Keep it until the fourteenth day of this month. At twilight the entire assembled community of Israel will slaughter their lambs."
    },
    "7": {
      "L": "And they shall take of the blood, and strike it on the two side posts and on the upper door post of the houses, wherein they shall eat it.",
      "M": "Then they are to take some of the blood and put it on the sides and tops of the doorframes of the houses where they eat the lambs.",
      "T": "Take some of the blood and mark the two doorposts and the lintel of every house where the lamb will be eaten."
    },
    "8": {
      "L": "And they shall eat the flesh in that night, roast with fire, and unleavened bread; and with bitter herbs they shall eat it.",
      "M": "That same night they are to eat the meat roasted over fire, along with bitter herbs and bread made without yeast.",
      "T": "That night they eat the meat — roasted over fire, not otherwise — with unleavened bread and bitter herbs."
    },
    "9": {
      "L": "Eat not of it raw, nor sodden at all with water, but roast with fire; his head with his legs, and with the purtenance thereof.",
      "M": "Do not eat the meat raw or boiled in water, but roast it over a fire — with its head, legs, and internal organs.",
      "T": "Not raw, not boiled in water — roasted whole over fire, head, legs, and inner parts included."
    },
    "10": {
      "L": "And ye shall let nothing of it remain until the morning; and that which remaineth of it until the morning ye shall burn with fire.",
      "M": "Do not leave any of it until morning; if some is left over, burn it.",
      "T": "Do not leave any until morning — burn whatever remains."
    },
    "11": {
      "L": "And thus shall ye eat it; with your loins girded, your shoes on your feet, and your staff in your hand; and ye shall eat it in haste: it is the LORD's passover.",
      "M": "This is how you are to eat it: with your cloak tucked into your belt, your sandals on your feet, and your staff in your hand. Eat it in haste; it is the LORD's Passover.",
      "T": "Eat it dressed for travel — belt fastened, sandals on, staff in hand. Eat quickly. This is Yahweh's Passover."
    },
    "12": {
      "L": "For I will pass through the land of Egypt this night, and will smite all the firstborn in the land of Egypt, both man and beast; and against all the gods of Egypt I will execute judgment: I am the LORD.",
      "M": "On that night I will pass through Egypt and strike down every firstborn — both people and animals — and I will bring judgment on all the gods of Egypt. I am the LORD.",
      "T": "That night I will pass through Egypt. I will strike every firstborn — person and animal — and execute judgment against every god of Egypt. I am Yahweh."
    },
    "13": {
      "L": "And the blood shall be to you for a token upon the houses where ye are: and when I see the blood, I will pass over you, and the plague shall not be upon you to destroy you, when I smite the land of Egypt.",
      "M": "The blood will be a sign for you on the houses where you are; and when I see the blood, I will pass over you. No destructive plague will touch you when I strike Egypt.",
      "T": "The blood on your doorposts will be a sign marking you as mine. When I see the blood, I will pass over you — passing over in the sense of sheltering you — and the destroying plague will not touch you when I strike Egypt."
    },
    "14": {
      "L": "And this day shall be unto you for a memorial; and ye shall keep it a feast to the LORD throughout your generations; ye shall keep it a feast by an ordinance for ever.",
      "M": "This is a day you are to commemorate; for the generations to come you shall celebrate it as a festival to the LORD — a lasting ordinance.",
      "T": "This day is to be a memorial for you. Keep it as a feast to Yahweh in every generation — a permanent ordinance for all time."
    },
    "15": {
      "L": "Seven days shall ye eat unleavened bread; even the first day ye shall put away leaven out of your houses: for whosoever eateth leavened bread from the first day until the seventh day, that soul shall be cut off from Israel.",
      "M": "For seven days you are to eat bread made without yeast. On the first day remove the yeast from your houses, for whoever eats anything with yeast in it from the first day through the seventh must be cut off from Israel.",
      "T": "Seven days you eat only unleavened bread. On the first day you purge all leaven from your homes. Whoever eats anything leavened from day one through day seven is to be cut off from the community of Israel."
    },
    "16": {
      "L": "And in the first day there shall be an holy convocation, and in the seventh day there shall be an holy convocation to you; no manner of work shall be done in them, save that which every man must eat, that only may be done of you.",
      "M": "On the first day hold a sacred assembly, and another one on the seventh day. Do no work at all on these days, except to prepare food for everyone to eat — that is all you may do.",
      "T": "The first day is a sacred gathering, and so is the seventh. Do no ordinary work on either day — the only exception is preparing food for the people."
    },
    "17": {
      "L": "And ye shall observe the feast of unleavened bread; for in this selfsame day have I brought your armies out of the land of Egypt: therefore shall ye observe this day in your generations by an ordinance for ever.",
      "M": "Celebrate the Festival of Unleavened Bread, because it was on this very day that I brought your divisions out of Egypt. Celebrate this day as a lasting ordinance for the generations to come.",
      "T": "Keep this Feast of Unleavened Bread — for it was on this precise day that I marched my armies out of Egypt. Let this day be kept in every generation as a permanent ordinance."
    },
    "18": {
      "L": "In the first month, on the fourteenth day of the month at even, ye shall eat unleavened bread, until the one and twentieth day of the month at even.",
      "M": "In the first month you are to eat bread made without yeast, from the evening of the fourteenth day until the evening of the twenty-first day.",
      "T": "In the first month: from evening on the fourteenth until evening on the twenty-first, you eat only unleavened bread."
    },
    "19": {
      "L": "Seven days shall there be no leaven found in your houses: for whosoever eateth that which is leavened, even that soul shall be cut off from the congregation of Israel, whether he be a stranger, or born in the land.",
      "M": "For seven days no yeast is to be found in your houses. And anyone — whether foreigner or native-born — who eats anything with yeast in it must be cut off from the community of Israel.",
      "T": "For seven days, no leaven is to be found anywhere in your homes. Foreigner or native-born — whoever eats leaven is cut off from Israel's community."
    },
    "20": {
      "L": "Ye shall eat nothing leavened; in all your habitations shall ye eat unleavened bread.",
      "M": "Eat nothing made with yeast. Wherever you live, you must eat unleavened bread.",
      "T": "Eat nothing leavened. In every place you live, unleavened bread only."
    },
    "21": {
      "L": "Then Moses called for all the elders of Israel, and said unto them, Draw out and take you a lamb according to your families, and kill the passover.",
      "M": "Then Moses summoned all the elders of Israel and said to them, 'Go at once and select the animals for your families and slaughter the Passover lamb.'",
      "T": "Moses called together all the elders of Israel. 'Go now,' he said, 'choose your Passover lambs according to your families, and slaughter them.'"
    },
    "22": {
      "L": "And ye shall take a bunch of hyssop, and dip it in the blood that is in the bason, and strike the lintel and the two side posts with the blood that is in the bason; and none of you shall go out at the door of his house until the morning.",
      "M": "Take a bunch of hyssop, dip it into the blood in the basin, and put some of the blood on the top and on both sides of the doorframe. None of you shall go out the door of your house until morning.",
      "T": "Take a bundle of hyssop, dip it in the blood in the basin, and brush that blood onto the lintel and both doorposts. Not one of you is to step outside until morning."
    },
    "23": {
      "L": "For the LORD will pass through to smite the Egyptians; and when he seeth the blood upon the lintel, and on the two side posts, the LORD will pass over the door, and will not suffer the destroyer to come in unto your houses to smite you.",
      "M": "When the LORD goes through the land to strike down the Egyptians, he will see the blood on the top and sides of the doorframe and will pass over that doorway, and he will not permit the destroyer to enter your houses and strike you down.",
      "T": "Yahweh will pass through to strike Egypt. When he sees the blood on the lintel and doorposts, he will pass over that door, sheltering it — he will not allow the destroyer to enter your home and bring death."
    },
    "24": {
      "L": "And ye shall observe this thing for an ordinance to thee and to thy sons for ever.",
      "M": "Obey these instructions as a lasting ordinance for you and your descendants.",
      "T": "Keep this observance — you and your children after you — as a permanent ordinance."
    },
    "25": {
      "L": "And it shall come to pass, when ye be come to the land which the LORD will give you, according as he hath promised, that ye shall keep this service.",
      "M": "When you enter the land that the LORD will give you as he promised, observe this ceremony.",
      "T": "When Yahweh brings you into the land he has promised to give you, keep this service there."
    },
    "26": {
      "L": "And it shall come to pass, when your children shall say unto you, What mean ye by this service?",
      "M": "And when your children ask you, 'What does this ceremony mean to you?'",
      "T": "When your children ask you, 'What does this rite mean?'"
    },
    "27": {
      "L": "That ye shall say, It is the sacrifice of the LORD's passover, who passed over the houses of the children of Israel in Egypt, when he smote the Egyptians, and delivered our houses. And the people bowed the head and worshipped.",
      "M": "then tell them, 'It is the Passover sacrifice to the LORD, who passed over the houses of the Israelites in Egypt and spared our homes when he struck down the Egyptians.' Then the people bowed down and worshiped.",
      "T": "tell them: 'This is Yahweh's Passover offering — he passed over the houses of Israel in Egypt. When he struck Egypt, our homes were sheltered.' When the people heard this, they bowed their heads and worshiped."
    },
    "28": {
      "L": "And the children of Israel went away, and did as the LORD had commanded Moses and Aaron, so did they.",
      "M": "And the Israelites went away and did just as the LORD had commanded Moses and Aaron.",
      "T": "The Israelites went away and carried out exactly what Yahweh had commanded Moses and Aaron."
    },
    "29": {
      "L": "And it came to pass, that at midnight the LORD smote all the firstborn in the land of Egypt, from the firstborn of Pharaoh that sat on his throne unto the firstborn of the captive that was in the dungeon; and all the firstborn of cattle.",
      "M": "At midnight the LORD struck down all the firstborn in Egypt, from the firstborn of Pharaoh who sat on the throne to the firstborn of the prisoner in the dungeon, and all the firstborn of the livestock as well.",
      "T": "At midnight Yahweh struck. Every firstborn in Egypt died — from Pharaoh's heir on the throne to the firstborn of the prisoner in the pit, and every firstborn animal."
    },
    "30": {
      "L": "And Pharaoh rose up in the night, he, and all his servants, and all the Egyptians; and there was a great cry in Egypt; for there was not a house where there was not one dead.",
      "M": "Pharaoh and all his officials and all the Egyptians got up during the night, and there was loud wailing in Egypt, for there was not a house without someone dead.",
      "T": "Pharaoh rose in the night — he, all his court, all Egypt — and a great cry went up. There was not a house in Egypt without death in it."
    },
    "31": {
      "L": "And he called for Moses and Aaron by night, and said, Rise up, and get you forth from among my people, both ye and the children of Israel; and go, serve the LORD, as ye have said.",
      "M": "During the night Pharaoh summoned Moses and Aaron and said, 'Up! Leave my people — you and the Israelites! Go, worship the LORD as you have requested.'",
      "T": "That night Pharaoh sent for Moses and Aaron. 'Get up!' he said. 'Get out from among my people — you and all the Israelites! Go, worship Yahweh as you demanded.'"
    },
    "32": {
      "L": "Also take your flocks and your herds, as ye have said, and be gone; and bless me also.",
      "M": "Take your flocks and herds, as you said, and go. And bless me too.",
      "T": "'Take your flocks and herds as you said, and go — and bless me too.'"
    },
    "33": {
      "L": "And the Egyptians were urgent upon the people, that they might send them out of the land in haste; for they said, We be all dead men.",
      "M": "The Egyptians urged the people to hurry and leave the country. 'For otherwise,' they said, 'we will all die!'",
      "T": "The Egyptians pressed Israel to leave at once. 'We are all dying,' they said. 'If you stay, we are all dead.'"
    },
    "34": {
      "L": "And the people took their dough before it was leavened, their kneadingtroughs being bound up in their clothes upon their shoulders.",
      "M": "So the people took their dough before the yeast was added, and carried it on their shoulders in kneading bowls wrapped in clothing.",
      "T": "The people grabbed their dough before it could rise, wrapped their kneading bowls in cloaks, and carried them on their shoulders — there was no time to wait."
    },
    "35": {
      "L": "And the children of Israel did according to the word of Moses; and they borrowed of the Egyptians jewels of silver, and jewels of gold, and raiment.",
      "M": "The Israelites did as Moses instructed and asked the Egyptians for articles of silver and gold and for clothing.",
      "T": "The Israelites did what Moses had told them — they asked their Egyptian neighbors for silver and gold jewelry and for clothing."
    },
    "36": {
      "L": "And the LORD gave the people favour in the sight of the Egyptians, so that they lent unto them such things as they required. And they spoiled the Egyptians.",
      "M": "The LORD had made the Egyptians favorably disposed toward the people, and they gave them what they asked for; so they stripped Egypt of its wealth.",
      "T": "Yahweh had given Israel such favor in Egypt's eyes that the Egyptians handed over whatever was asked. Israel plundered Egypt on the way out."
    },
    "37": {
      "L": "And the children of Israel journeyed from Rameses to Succoth, about six hundred thousand on foot that were men, beside children.",
      "M": "The Israelites journeyed from Rameses to Sukkoth. There were about 600,000 men on foot, besides women and children.",
      "T": "The Israelites moved out from Rameses to Succoth — some 600,000 men on foot, not counting women and children."
    },
    "38": {
      "L": "And a mixed multitude went up also with them; and flocks, and herds, even very much cattle.",
      "M": "Many other people went up with them, as well as large droves of livestock, both flocks and herds.",
      "T": "A diverse crowd of non-Israelites joined them — along with enormous herds of livestock, flocks and cattle alike."
    },
    "39": {
      "L": "And they baked unleavened cakes of the dough which they brought forth out of Egypt, for it was not leavened; because they were thrust out of Egypt, and could not tarry, neither had they prepared for themselves any victual.",
      "M": "With the dough they had brought from Egypt, they baked loaves of unleavened bread. The dough was without yeast because they had been driven out of Egypt and did not have time to prepare food for themselves.",
      "T": "From the dough they had carried out, they baked flat unleavened bread. There had been no time for yeast — they were driven out of Egypt with no opportunity to prepare provisions."
    },
    "40": {
      "L": "Now the sojourning of the children of Israel, who dwelt in Egypt, was four hundred and thirty years.",
      "M": "The length of time the Israelites lived in Egypt was 430 years.",
      "T": "The Israelites had lived in Egypt for 430 years."
    },
    "41": {
      "L": "And it came to pass at the end of the four hundred and thirty years, even the selfsame day it came to pass, that all the hosts of the LORD went out from the land of Egypt.",
      "M": "At the end of the 430 years, to the very day, all the LORD's divisions left Egypt.",
      "T": "On the very day those 430 years were complete, every division of Yahweh's army marched out of Egypt."
    },
    "42": {
      "L": "It is a night to be much observed unto the LORD for bringing them out from the land of Egypt: this is that night of the LORD to be observed of all the children of Israel in their generations.",
      "M": "Because the LORD kept vigil that night to bring them out of Egypt, on this night all the Israelites are to keep vigil to honor the LORD for the generations to come.",
      "T": "This is a night Yahweh kept watch — a vigil to bring them out of Egypt. And so this same night is kept as a vigil by all the children of Israel in every generation."
    },
    "43": {
      "L": "And the LORD said unto Moses and Aaron, This is the ordinance of the passover: There shall no stranger eat thereof.",
      "M": "The LORD said to Moses and Aaron, 'These are the regulations for the Passover: No foreigner may eat it.'",
      "T": "Yahweh said to Moses and Aaron: 'These are the Passover rules. No outsider may eat it.'"
    },
    "44": {
      "L": "But every man's servant that is bought for money, when thou hast circumcised him, then shall he eat thereof.",
      "M": "Any slave you have bought may eat it after you have circumcised him.",
      "T": "A slave bought with money may eat it after circumcision."
    },
    "45": {
      "L": "A foreigner and an hired servant shall not eat thereof.",
      "M": "But a temporary resident or a hired worker may not eat it.",
      "T": "A temporary resident or hired worker — no."
    },
    "46": {
      "L": "In one house shall it be eaten; thou shalt not carry forth ought of the flesh abroad out of the house; neither shall ye break a bone thereof.",
      "M": "It must be eaten inside the house; take none of the meat outside the house. Do not break any of the bones.",
      "T": "The whole meal is eaten inside one house — no meat goes outside, and not one bone is broken."
    },
    "47": {
      "L": "All the congregation of Israel shall keep it.",
      "M": "The whole community of Israel must celebrate it.",
      "T": "The entire community of Israel keeps this observance."
    },
    "48": {
      "L": "And when a stranger shall sojourn with thee, and will keep the passover to the LORD, let all his males be circumcised, and then let him come near and keep it; and he shall be as one that is born in the land: for no uncircumcised person shall eat thereof.",
      "M": "A foreigner residing among you who wants to celebrate the LORD's Passover must have all the males in his household circumcised; then he may take part, just like one born in the land. No uncircumcised male may eat it.",
      "T": "If a foreigner living among you wishes to keep Passover to Yahweh, all his males must first be circumcised. Then he may join in fully, as if native-born. No one uncircumcised may eat it."
    },
    "49": {
      "L": "One law shall be to him that is homeborn, and unto the stranger that sojourneth among you.",
      "M": "The same law applies to the native-born and to the foreigner residing among you.",
      "T": "One law — the same for the native-born and for the foreigner living among you."
    },
    "50": {
      "L": "Thus did all the children of Israel; as the LORD commanded Moses and Aaron, so did they.",
      "M": "All the Israelites did just as the LORD had commanded Moses and Aaron.",
      "T": "All the children of Israel did as Yahweh commanded Moses and Aaron — without exception."
    },
    "51": {
      "L": "And it came to pass the selfsame day, that the LORD did bring the children of Israel out of the land of Egypt by their armies.",
      "M": "And on that very day the LORD brought the Israelites out of Egypt by their divisions.",
      "T": "On that very day Yahweh led the children of Israel out of Egypt — rank by rank, division by division."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'exodus')
        merge_tier(existing, EXODUS, tier_key)
        save(tier_dir, 'exodus', existing)
    print('Exodus 7–12 written.')

if __name__ == '__main__':
    main()
