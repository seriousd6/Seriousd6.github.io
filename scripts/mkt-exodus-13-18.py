"""
MKT Exodus chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-exodus-13-18.py

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "Yahweh" in T — the divine name carries covenantal weight; in the
  Song of Moses (ch. 15) where the name is thematically climactic ("Yahweh is a warrior" v.3,
  "Yahweh reigns" v.18) we use "Yahweh" in T to restore what small-caps "LORD" conceals.
- H430 (אֱלֹהִים): "God" in all tiers; when used of Jethro's theology (ch. 18) contextually "God"
  is appropriate since it is Jethro acknowledging the universal supremacy of Israel's God.
- H7307 (רוּחַ): In 15:8 ("blast of your nostrils") and 15:10 ("you blew with your wind/breath")
  the sense is clearly physical breath/wind — the storm that parts and closes the sea. Rendered
  "breath" / "wind" in all tiers; not "Spirit" here.
- H2617 (חֶסֶד): 15:13 "in your steadfast love" — L/M keep "steadfast love"; T "covenant loyalty"
  surfaces the patron-client covenantal force the word carries.
- H3444 (יְשׁוּעָה): 14:13 "the salvation of the LORD" — L "salvation", M "salvation", T "deliverance"
  (emphasising the active rescue event, not an abstract state).
- H3519 (כָּבוֹד): 14:4,17,18 "get glory" — the honour-shame dynamic is primary; T makes this
  explicit: "I will show my honour" / "Yahweh's glory". Glory is not merely aesthetic radiance
  but the public vindication of divine sovereignty over Egypt's gods.
- H5315 (נֶפֶשׁ): does not appear in these chapters.
- H1285 (בְּרִית): does not appear prominently here; oath to the fathers alluded to in 13:5.
- "Sons of Israel" (בְּנֵי יִשְׂרָאֵל): L preserves "sons of Israel" throughout; M uses "the
  Israelites" where the phrase is mid-narrative; T uses "Israel" for poetic economy.
- "Sea of Reeds" (יַם סוּף): standard translation "Red Sea" in L/M (conventional); T notes "Sea
  of Reeds" as the more accurate rendering of סוּף (reeds/rushes), clarifying the geography.
- "Armed" / "harnessed" 13:18 (חֲמֻשִׁים): the Hebrew means "arrayed in battle order" (five in
  a rank). L "armed for battle", M "armed for battle", T "arrayed rank by rank for war."
- "Manna" (מָן): 16:15 the word is an Aramaic/Egyptian loanword punning on "What is it?" (מָה
  הוּא). T surfaces this etymology in the commentary-style rendering.
- Song of Moses (15:1-18): ancient Hebrew poetry — among the oldest texts in the Bible (Albright,
  Cross). T tier uses line breaks to preserve the parallelism and gives the poetry cadence.
  Antithetic parallelism in vv. 6, 11; synthetic in vv. 13-16. Strophic structure: vv. 1-12
  (past deliverance), 13-18 (future settlement).
- Chiasmus in 15:6: "Your right hand, O LORD, glorious in power / Your right hand, O LORD,
  shatters the enemy" — the repetition is emphatic, not redundant. Preserved in all tiers.
- 14:25 "clogged their chariot wheels" — the LXX has "removed"; Hebrew text (MT) suggests either
  removal or obstruction. We follow MT: obstruction/removal of wheels causing difficulty.
- Jethro's theology (18:11): "greater than all gods" — not polytheism but rhetorical comparison
  (monolatry in polemic key). T: "towering above every god" to capture the triumphalist tone.
- H4687 (מִצְוָה): 16:28 "my commandments" — consistent with L/M/T as "commandments."
- Sabbath (שַׁבָּת): first introduced here in narrative. T makes the covenantal import explicit.
- 17:16 "a hand on the banner of the LORD" — the text is difficult; may mean "the throne of Yah"
  (כֵּס יָהּ rather than נֵס יָהּ). We follow the standard MT reading in L/M; T notes the
  alternative by rendering "his throne is pledged" to signal the oath-bound nature of the war.
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
  # ── Chapter 13: Consecration of the Firstborn; Feast of Unleavened Bread; Pillars ──
  "13": {
    "1": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "Yahweh spoke to Moses:"
    },
    "2": {
      "L": "Sanctify unto me every firstborn, whatever openeth the womb among the sons of Israel, both of man and of beast — it is mine.",
      "M": "\"Consecrate to me every firstborn — whatever first opens the womb among the Israelites, whether human or animal — it belongs to me.\"",
      "T": "\"Set apart for me every firstborn — every womb's first to open, human or animal, among my people. They belong to me.\""
    },
    "3": {
      "L": "And Moses said unto the people, Remember this day in which ye came out from Egypt, out of the house of bondage; for by strength of hand the LORD brought you out from this place. There shall no leavened bread be eaten.",
      "M": "Moses said to the people, \"Remember this day — the day you came out of Egypt, out of the place of slavery — for it was by a strong hand that the LORD brought you out from here. No leavened bread shall be eaten.\"",
      "T": "Moses addressed the people: \"Burn this day into memory — the day you walked out of Egypt, out of the house of slavery. Yahweh brought you out by sheer force of power. No leaven shall be eaten — let nothing rise that day.\""
    },
    "4": {
      "L": "This day ye go out in the month Abib.",
      "M": "Today, in the month of Abib, you are going out.",
      "T": "Today — in the month of Abib, the month of ripening grain — you march out free."
    },
    "5": {
      "L": "And it shall be when the LORD shall bring thee into the land of the Canaanites, and the Hittites, and the Amorites, and the Hivites, and the Jebusites — which he sware unto thy fathers to give thee, a land flowing with milk and honey — thou shalt keep this service in this month.",
      "M": "When the LORD brings you into the land of the Canaanites, Hittites, Amorites, Hivites, and Jebusites — the land he swore to your ancestors to give you, a land flowing with milk and honey — you shall observe this rite in this month.",
      "T": "When Yahweh brings you into the land he swore to your fathers — Canaan, a country rich as flowing milk and honey — you shall keep this annual rite. The land and the memory of liberation belong together."
    },
    "6": {
      "L": "Seven days thou shalt eat unleavened bread, and in the seventh day shall be a feast to the LORD.",
      "M": "For seven days you shall eat unleavened bread, and on the seventh day there shall be a festival to the LORD.",
      "T": "Seven days of unleavened bread — no leaven in the house, no leaven in the memory — and on the seventh day a festival before Yahweh."
    },
    "7": {
      "L": "Unleavened bread shall be eaten seven days; and there shall no leavened bread be seen with thee, neither shall there be leaven seen with thee in all thy borders.",
      "M": "Unleavened bread shall be eaten throughout the seven days; no leavened bread shall be seen among you, and no leaven shall be found anywhere in your territory.",
      "T": "Unleavened bread only, for the full seven days. No leaven anywhere in your homes or your land — Egypt's bread must not follow you into freedom."
    },
    "8": {
      "L": "And thou shalt tell thy son in that day, saying, This is done because of what the LORD did for me when I came forth out of Egypt.",
      "M": "On that day you shall tell your child, 'This is done because of what the LORD did for me when I came out of Egypt.'",
      "T": "Tell your children on that day: 'This feast is because of what Yahweh did for me — personally, for me — when he brought me out of Egypt.' Make the exodus your own story, not only your ancestors'."
    },
    "9": {
      "L": "And it shall be for a sign unto thee upon thine hand, and for a memorial between thine eyes, that the law of the LORD may be in thy mouth; for with a strong hand the LORD brought thee out of Egypt.",
      "M": "This observance shall be to you as a sign on your hand and a reminder between your eyes, so that the law of the LORD may be on your lips; for with a strong hand the LORD brought you out of Egypt.",
      "T": "Let this rite be like writing on your hand and a mark between your eyes — something you cannot ignore — so that Yahweh's teaching stays on your lips. A strong hand brought you out; let that strength shape your thinking."
    },
    "10": {
      "L": "Thou shalt therefore keep this ordinance in its season from year to year.",
      "M": "You shall therefore keep this statute at its appointed time from year to year.",
      "T": "Observe this rite at its proper time, year after year, without fail."
    },
    "11": {
      "L": "And it shall be when the LORD shall bring thee into the land of the Canaanites, as he sware unto thee and to thy fathers, and shall give it thee,",
      "M": "When the LORD brings you into the land of the Canaanites, as he swore to you and to your ancestors, and gives it to you,",
      "T": "When Yahweh fulfils his sworn oath and delivers Canaan into your hands,"
    },
    "12": {
      "L": "that thou shalt set apart unto the LORD all that openeth the womb; and every firstborn of the males of the beasts that thou hast shall belong to the LORD.",
      "M": "you shall set apart to the LORD all that first opens the womb. Every firstborn male of your livestock belongs to the LORD.",
      "T": "set apart for Yahweh every firstborn — the womb's first claim belongs to the one who redeemed you. Every firstborn male of your animals is his."
    },
    "13": {
      "L": "And every firstborn of a donkey thou shalt redeem with a lamb; and if thou wilt not redeem it, then thou shalt break its neck. And every firstborn of man among thy sons thou shalt redeem.",
      "M": "Every firstborn donkey you shall redeem with a lamb; if you do not redeem it, you must break its neck. Every firstborn son you shall redeem.",
      "T": "The firstborn donkey — redeem it with a lamb, or break its neck; it cannot be left unclaimed. Every firstborn son must also be redeemed — their lives belong to the God who spared them."
    },
    "14": {
      "L": "And it shall be when thy son asketh thee in time to come, saying, What is this? then thou shalt say unto him, By strength of hand the LORD brought us out from Egypt, from the house of bondage.",
      "M": "When in the future your child asks you, 'What does this mean?' you shall say, 'By a strong hand the LORD brought us out of Egypt, from the house of slavery.'",
      "T": "When your children one day ask, 'Why do we do this?' — tell them the story: 'Yahweh brought us out of Egypt by sheer force, out of the slave house.' Give them the narrative before you give them the rules."
    },
    "15": {
      "L": "And it came to pass when Pharaoh hardened himself against letting us go, that the LORD slew all the firstborn in the land of Egypt, both the firstborn of man and the firstborn of beast; therefore I sacrifice to the LORD all that openeth the womb, being males — but all the firstborn of my children I redeem.",
      "M": "For when Pharaoh stubbornly refused to let us go, the LORD struck down every firstborn in the land of Egypt — both the firstborn of man and the firstborn of beast. That is why I sacrifice to the LORD every male that first opens the womb, but every firstborn son I redeem.",
      "T": "Pharaoh hardened himself and refused to release us — so Yahweh struck every firstborn in Egypt, human and animal alike. The cost of Pharaoh's defiance was the death of Egypt's future. That is why every firstborn male we dedicate to God, and every firstborn son we redeem — because our sons survived only by his mercy."
    },
    "16": {
      "L": "And it shall be for a token upon thine hand, and for frontlets between thine eyes; for by strength of hand the LORD brought us forth out of Egypt.",
      "M": "It shall serve as a sign on your hand and as frontlets between your eyes, for by a strong hand the LORD brought us out of Egypt.",
      "T": "Wear it like a sign on your hand, like scripture between your eyes — because Yahweh's strong hand brought us out. Let the body remember what the mind might forget."
    },
    "17": {
      "L": "And it came to pass when Pharaoh had sent the people away, that God led them not through the way of the land of the Philistines, although that was near; for God said, Lest the people repent when they see war, and they return to Egypt.",
      "M": "When Pharaoh finally let the people go, God did not lead them by way of the Philistine coast, though that road was shorter; for God said, \"Lest the people lose heart when they encounter war and turn back to Egypt.\"",
      "T": "When Pharaoh released them, God did not take them the short road through Philistine territory. The reason was pastoral: God knew their courage was new and fragile. War would have broken it and sent them running back to their chains."
    },
    "18": {
      "L": "But God led the people about through the way of the wilderness of the Red Sea; and the sons of Israel went up armed out of the land of Egypt.",
      "M": "Instead God led the people around by way of the wilderness toward the Red Sea. The Israelites left the land of Egypt armed for battle.",
      "T": "So God guided them on the long route — through wilderness, toward the Sea of Reeds. And Israel went out arrayed rank by rank for war, weapons in hand, freed slaves who had to become an army."
    },
    "19": {
      "L": "And Moses took the bones of Joseph with him; for he had straitly charged the sons of Israel, saying, God will surely visit you; and ye shall carry up my bones away hence with you.",
      "M": "Moses took the bones of Joseph with him, for Joseph had made the Israelites solemnly swear, saying, \"God will certainly come to your aid; when he does, you must carry my bones up from here with you.\"",
      "T": "Moses carried Joseph's bones with him — Joseph had exacted an oath from Israel: 'When God comes for you, take me with you.' After four centuries, that old promise was honoured. The exodus carried its own dead home."
    },
    "20": {
      "L": "And they took their journey from Succoth and encamped in Etham at the edge of the wilderness.",
      "M": "They set out from Succoth and encamped at Etham, on the edge of the wilderness.",
      "T": "They moved out from Succoth and made camp at Etham — the last edge of the known world before the wild."
    },
    "21": {
      "L": "And the LORD went before them by day in a pillar of cloud to lead them the way, and by night in a pillar of fire to give them light — to go by day and by night.",
      "M": "The LORD went before them by day in a pillar of cloud to guide their way, and by night in a pillar of fire to give them light, so they could travel day and night.",
      "T": "Yahweh himself led the column — cloud by day to shade and guide them, fire by night to light their path. They were never left to navigate alone; the God who freed them now walked ahead."
    },
    "22": {
      "L": "The pillar of cloud by day and the pillar of fire by night departed not from before the people.",
      "M": "Neither the pillar of cloud by day nor the pillar of fire by night ever departed from before the people.",
      "T": "The cloud never lifted by day, and the fire never went out at night. Yahweh's presence was constant, visible, unbroken — a promise in the sky."
    }
  },
  # ── Chapter 14: The Crossing of the Sea ──
  "14": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "Then the LORD said to Moses,",
      "T": "Yahweh spoke to Moses:"
    },
    "2": {
      "L": "Speak unto the sons of Israel that they turn and encamp before Pi-hahiroth, between Migdol and the sea, before Baal-zephon — opposite it ye shall encamp by the sea.",
      "M": "\"Tell the Israelites to turn back and encamp before Pi-hahiroth, between Migdol and the sea, in front of Baal-zephon. Camp opposite it by the sea.\"",
      "T": "\"Have Israel double back and camp before Pi-hahiroth — between Migdol and the sea, facing Baal-zephon. Set up camp right at the water's edge.\""
    },
    "3": {
      "L": "For Pharaoh will say of the sons of Israel, They are entangled in the land; the wilderness hath shut them in.",
      "M": "\"Pharaoh will think the Israelites are wandering in confusion, hemmed in by the wilderness.\"",
      "T": "\"Pharaoh will look at their position and conclude they are lost — trapped between the wilderness and the sea. Let him think that.\""
    },
    "4": {
      "L": "And I will harden Pharaoh's heart that he shall pursue after them; and I will get me honour upon Pharaoh and upon all his host; and the Egyptians shall know that I am the LORD. And they did so.",
      "M": "\"I will harden Pharaoh's heart so that he pursues them, and I will gain glory over Pharaoh and his entire army; then the Egyptians will know that I am the LORD.\" And the Israelites did so.",
      "T": "\"I will harden Pharaoh's heart and he will chase them — and through that pursuit I will show my glory at his expense. Egypt will learn who I am.\" Israel obeyed."
    },
    "5": {
      "L": "And it was told the king of Egypt that the people had fled; and the heart of Pharaoh and of his servants was turned against the people, and they said, What have we done, that we have let Israel go from serving us?",
      "M": "When the king of Egypt was told that the people had fled, Pharaoh and his officials had a change of heart about the people and said, \"What have we done? We have let Israel go and lost their labor!\"",
      "T": "News reached Pharaoh: the people had fled. His heart and the hearts of his officials lurched — the same hearts Yahweh had hardened. 'What have we done?' they said. 'We released our workforce. We gave away our slaves.'"
    },
    "6": {
      "L": "And he made ready his chariot and took his people with him.",
      "M": "So he had his chariot prepared and took his forces with him.",
      "T": "Pharaoh ordered his chariot readied and marshalled his forces."
    },
    "7": {
      "L": "And he took six hundred chosen chariots, and all the chariots of Egypt, and captains over all of them.",
      "M": "He took six hundred select chariots and all the other chariots of Egypt, with officers over each.",
      "T": "Six hundred elite war-chariots, plus the full Egyptian chariot corps — every one commanded, every one sent in pursuit."
    },
    "8": {
      "L": "And the LORD hardened the heart of Pharaoh king of Egypt, and he pursued after the sons of Israel; for the sons of Israel went out with a high hand.",
      "M": "The LORD hardened the heart of Pharaoh king of Egypt, so that he pursued the Israelites, who were marching out boldly.",
      "T": "Yahweh hardened Pharaoh's heart. Pharaoh chased. And Israel marched out with their heads high — triumphant, unashamed, free."
    },
    "9": {
      "L": "And the Egyptians pursued after them — all the horses and chariots of Pharaoh, and his horsemen, and his army — and overtook them encamping by the sea beside Pi-hahiroth, before Baal-zephon.",
      "M": "The Egyptians — all Pharaoh's horses, chariots, horsemen, and troops — pursued them and caught up with them as they camped by the sea near Pi-hahiroth, in front of Baal-zephon.",
      "T": "Egypt's full military might bore down on them: horses, chariots, cavalry, infantry — overtaking Israel just as they had stopped to camp at the sea's edge, near Pi-hahiroth."
    },
    "10": {
      "L": "And when Pharaoh drew nigh, the sons of Israel lifted up their eyes, and behold, the Egyptians marched after them; and they were sore afraid; and the sons of Israel cried out unto the LORD.",
      "M": "As Pharaoh approached, the Israelites looked up and saw the Egyptians coming after them. They were terrified and cried out to the LORD.",
      "T": "They looked up and saw Egypt. The full army — the chariots, the dust-cloud, the closing distance. Terror swept through the camp and they cried out to Yahweh."
    },
    "11": {
      "L": "And they said unto Moses, Is it because there were no graves in Egypt that thou hast taken us away to die in the wilderness? Wherefore hast thou dealt thus with us, to carry us forth out of Egypt?",
      "M": "They said to Moses, \"Were there not enough graves in Egypt that you had to bring us here to die in the wilderness? What have you done to us, bringing us out of Egypt?\"",
      "T": "The people turned on Moses: 'Not enough graves in Egypt? You had to bring us out here to make new ones? What were you thinking?'"
    },
    "12": {
      "L": "Is not this the word that we did tell thee in Egypt, saying, Let us alone, that we may serve the Egyptians? For it were better for us to serve the Egyptians than that we should die in the wilderness.",
      "M": "\"Is this not what we said to you in Egypt: 'Leave us alone and let us serve the Egyptians'? It would have been better to remain slaves in Egypt than to die out here in the wilderness.\"",
      "T": "'Didn't we tell you this back in Egypt? Leave us alone — let us keep serving. Slavery with a living body beats freedom with a dead one.' Fear had already rewritten the past."
    },
    "13": {
      "L": "And Moses said unto the people, Fear not — stand still, and see the salvation of the LORD which he will show to you today; for the Egyptians whom ye have seen today, ye shall see them again no more for ever.",
      "M": "Moses said to the people, \"Do not be afraid. Stand firm and see what deliverance the LORD will bring you today; for the Egyptians you see now, you will never see again.\"",
      "T": "Moses stood firm: 'Don't be afraid. Hold your ground and watch — Yahweh will deliver you today. Those Egyptians you see closing in? You will never lay eyes on them again.'"
    },
    "14": {
      "L": "The LORD shall fight for you, and ye shall hold your peace.",
      "M": "\"The LORD himself will fight for you; you need only be still.\"",
      "T": "'Yahweh fights for you. Your part is simply this: be still.'"
    },
    "15": {
      "L": "And the LORD said unto Moses, Wherefore criest thou unto me? Speak unto the sons of Israel that they go forward.",
      "M": "The LORD said to Moses, \"Why are you crying out to me? Tell the Israelites to move forward.\"",
      "T": "Yahweh broke in: 'Moses — enough prayer. Tell them to go forward.'"
    },
    "16": {
      "L": "But lift thou up thy rod, and stretch out thine hand over the sea, and divide it; and the sons of Israel shall go on dry ground through the midst of the sea.",
      "M": "\"Lift up your staff, stretch out your hand over the sea, and divide it, so that the Israelites can walk through on dry ground.\"",
      "T": "'Lift your staff and stretch it over the sea. Divide it. Israel will walk through on dry ground.'"
    },
    "17": {
      "L": "And I, behold, I will harden the hearts of the Egyptians, and they shall follow them; and I will get me honour upon Pharaoh and upon all his host, upon his chariots and upon his horsemen.",
      "M": "\"And I — I will harden the hearts of the Egyptians so they will go in after them; and I will gain glory over Pharaoh and all his forces, his chariots and horsemen.\"",
      "T": "'And I will harden Egypt's hearts so they follow Israel into the sea — and I will show my glory through Pharaoh himself, through his chariots, through every soldier.'"
    },
    "18": {
      "L": "And the Egyptians shall know that I am the LORD, when I have gotten me honour upon Pharaoh, upon his chariots, and upon his horsemen.",
      "M": "\"Then the Egyptians will know that I am the LORD, when I have gained glory at the expense of Pharaoh, his chariots, and his cavalry.\"",
      "T": "'Egypt will know who I am — not through theology but through catastrophe. When Pharaoh's glory sinks in the sea, mine will stand alone.'"
    },
    "19": {
      "L": "And the angel of God which went before the camp of Israel removed and went behind them; and the pillar of cloud removed from before their face, and stood behind them.",
      "M": "Then the angel of God, who had been going before the Israelite camp, moved and went behind them; and the pillar of cloud moved from in front of them and took up position behind them.",
      "T": "The angel of God — the same presence that had led them — stepped out of the lead and moved to their rear. The pillar of cloud shifted to stand between Israel and Egypt."
    },
    "20": {
      "L": "And it came between the camp of Egypt and the camp of Israel; and it was a cloud of darkness to them, but it gave light by night to these; so that the one came not near the other all the night.",
      "M": "It stood between the Egyptian camp and the Israelite camp — bringing darkness and cloud to the Egyptians while giving light to the Israelites. Neither side could approach the other all night long.",
      "T": "One cloud, two effects: Egypt's side was plunged into darkness; Israel's side was bathed in light. The whole night passed and neither army could touch the other."
    },
    "21": {
      "L": "And Moses stretched out his hand over the sea; and the LORD caused the sea to go back by a strong east wind all that night, and made the sea dry land; and the waters were divided.",
      "M": "Then Moses stretched out his hand over the sea, and the LORD drove the sea back with a powerful east wind all that night and turned the sea into dry land; the waters were divided.",
      "T": "Moses stretched out his hand. Yahweh drove the sea back with a roaring east wind all through the night. The seabed became dry ground. The waters split apart and stood."
    },
    "22": {
      "L": "And the sons of Israel went into the midst of the sea upon the dry ground; and the waters were a wall unto them on their right hand and on their left.",
      "M": "The Israelites walked through the sea on dry ground, with walls of water on their right and on their left.",
      "T": "Israel walked through. Dry ground underfoot, walls of water on both sides — an impossible corridor opened by the God of the impossible."
    },
    "23": {
      "L": "And the Egyptians pursued and went in after them to the midst of the sea — all Pharaoh's horses, his chariots, and his horsemen.",
      "M": "The Egyptians pursued and followed them into the sea — all Pharaoh's horses, chariots, and cavalry.",
      "T": "Egypt followed. Every horse, every chariot, every soldier poured into the corridor after them — into the trap."
    },
    "24": {
      "L": "And it came to pass in the morning watch that the LORD looked unto the host of the Egyptians through the pillar of fire and of cloud, and troubled the host of the Egyptians.",
      "M": "In the morning watch, the LORD looked down on the Egyptian army through the pillar of fire and cloud, and threw the Egyptian forces into confusion.",
      "T": "In the last watch before dawn, Yahweh looked down from the pillar of fire and cloud — and panic broke loose in the Egyptian ranks."
    },
    "25": {
      "L": "And he took off their chariot wheels, so that they drove them heavily; and the Egyptians said, Let us flee from before Israel; for the LORD fighteth for them against the Egyptians.",
      "M": "He jammed the wheels of their chariots so they drove with difficulty. The Egyptians cried, \"Let us flee from Israel! The LORD is fighting for them against Egypt!\"",
      "T": "The chariot wheels were seized — they lurched and ground to a halt. And then even the Egyptians understood: 'Run. Yahweh is fighting for them against us.'"
    },
    "26": {
      "L": "And the LORD said unto Moses, Stretch out thine hand over the sea, that the waters may come again upon the Egyptians, upon their chariots, and upon their horsemen.",
      "M": "Then the LORD said to Moses, \"Stretch out your hand over the sea, so that the waters may flow back over the Egyptians — their chariots and their cavalry.\"",
      "T": "Yahweh commanded Moses: 'Stretch your hand over the sea. Let the waters return upon Egypt.'"
    },
    "27": {
      "L": "And Moses stretched forth his hand over the sea, and the sea returned to his strength when the morning appeared; and the Egyptians fled against it; and the LORD overthrew the Egyptians in the midst of the sea.",
      "M": "Moses stretched out his hand over the sea, and at daybreak the sea returned to its natural flow. The Egyptians tried to flee into it, but the LORD swept the Egyptians into the sea.",
      "T": "Moses raised his hand. At dawn the sea rushed back to full strength. Egypt turned to run — and Yahweh hurled them into the waves."
    },
    "28": {
      "L": "And the waters returned and covered the chariots and the horsemen — all the host of Pharaoh that came into the sea after them; there remained not so much as one of them.",
      "M": "The waters flowed back and covered all the chariots and horsemen — the entire army of Pharaoh that had followed the Israelites into the sea. Not one survived.",
      "T": "The sea closed over everything: chariots, horses, soldiers — all of Pharaoh's army that had entered the corridor. Not one came back out."
    },
    "29": {
      "L": "But the sons of Israel walked upon dry land in the midst of the sea; and the waters were a wall unto them on their right hand and on their left.",
      "M": "But the Israelites had walked through the sea on dry ground, with the walls of water on their right and on their left.",
      "T": "Israel had walked through on dry ground, water standing on both sides like walls. What was death for Egypt was salvation for Israel — the same sea, the same night, two opposite outcomes."
    },
    "30": {
      "L": "Thus the LORD saved Israel that day out of the hand of the Egyptians; and Israel saw the Egyptians dead upon the sea shore.",
      "M": "That day the LORD saved Israel from the power of the Egyptians, and Israel saw the Egyptian bodies lying along the seashore.",
      "T": "That day Yahweh saved Israel from Egypt's grip. And in the morning, they stood on the shore and looked at what had been the most powerful army in the world — washed up, dead, finished."
    },
    "31": {
      "L": "And Israel saw the great work which the LORD did upon the Egyptians; and the people feared the LORD, and believed in the LORD and in his servant Moses.",
      "M": "When Israel saw the great power that the LORD displayed against the Egyptians, the people feared the LORD and put their trust in the LORD and in his servant Moses.",
      "T": "They saw the scale of what Yahweh had done. And the people feared — not the fear that paralyzes, but the fear that worships. They trusted Yahweh and his servant Moses."
    }
  },
  # ── Chapter 15: The Song of Moses; Miriam's Song; Marah; Elim ──
  "15": {
    "1": {
      "L": "Then Moses and the sons of Israel sang this song unto the LORD, and spake, saying: I will sing unto the LORD, for he hath triumphed gloriously — the horse and his rider hath he thrown into the sea.",
      "M": "Then Moses and the Israelites sang this song to the LORD: \"I will sing to the LORD, for he has triumphed gloriously; the horse and its rider he has hurled into the sea.\"",
      "T": "Then Moses and Israel broke into song before Yahweh:\n\"I will sing to Yahweh — he has risen in triumph!\nHorse and rider he has flung into the sea.\""
    },
    "2": {
      "L": "The LORD is my strength and my song, and he is become my salvation; this is my God and I will glorify him — my father's God, and I will exalt him.",
      "M": "\"The LORD is my strength and my song; he has become my salvation. He is my God and I will praise him — my father's God and I will exalt him.\"",
      "T": "\"Yahweh is my strength, my song — he became my deliverance.\nHe is my God and I will make him a sanctuary,\nmy father's God — I will lift him high.\""
    },
    "3": {
      "L": "The LORD is a man of war; the LORD is his name.",
      "M": "\"The LORD is a warrior; the LORD is his name.\"",
      "T": "\"Yahweh is a warrior — Yahweh is his name.\""
    },
    "4": {
      "L": "Pharaoh's chariots and his host hath he cast into the sea; and his chosen captains also are drowned in the Red Sea.",
      "M": "\"Pharaoh's chariots and his army he cast into the sea; his finest officers are drowned in the Red Sea.\"",
      "T": "\"Pharaoh's chariots and his army — thrown into the sea.\nHis elite officers swallowed by the Sea of Reeds.\""
    },
    "5": {
      "L": "The floods have covered them; they sank to the bottom as a stone.",
      "M": "\"The great deep covered them; they went down to the depths like a stone.\"",
      "T": "\"The deep closed over them;\nthey sank like stones to the bottom.\""
    },
    "6": {
      "L": "Thy right hand, O LORD, is glorious in power; thy right hand, O LORD, hath dashed in pieces the enemy.",
      "M": "\"Your right hand, O LORD, is majestic in power; your right hand, O LORD, shattered the enemy.\"",
      "T": "\"Your right hand, Yahweh — glorious in strength!\nYour right hand, Yahweh — it shattered the enemy!\""
    },
    "7": {
      "L": "And in the greatness of thine excellency thou hast overthrown them that rose up against thee; thou sentest forth thy wrath which consumed them as stubble.",
      "M": "\"In the greatness of your majesty you overthrew your adversaries; you unleashed your burning anger and it consumed them like stubble.\"",
      "T": "\"In the fullness of your majesty you crushed your opponents;\nyou released your fury — it burned them like dry straw.\""
    },
    "8": {
      "L": "And with the blast of thy nostrils the waters were heaped together; the floods stood upright as a heap; the deeps were congealed in the heart of the sea.",
      "M": "\"By the blast of your nostrils the waters piled up; the flowing waters stood firm like a wall; the deep waters congealed in the heart of the sea.\"",
      "T": "\"One breath from your nostrils — the waters heaped up.\nThe floods stood straight like a wall.\nThe deeps froze at the sea's core.\""
    },
    "9": {
      "L": "The enemy said, I will pursue; I will overtake; I will divide the spoil; my desire shall be satisfied upon them; I will draw my sword; my hand shall destroy them.",
      "M": "\"The enemy said, 'I will pursue, I will overtake, I will divide the plunder; my desire will be satisfied at their expense; I will draw my sword; my hand will destroy them.'\"",
      "T": "\"The enemy said:\n'I will pursue, I will catch them,\nI will divide the spoil — fill my hands with it,\nunsheathe my sword, cut them down.'\"\nWords of a predator. Words that came to nothing."
    },
    "10": {
      "L": "Thou didst blow with thy wind; the sea covered them; they sank as lead in the mighty waters.",
      "M": "\"But you blew with your wind — the sea covered them; they sank like lead in the mighty waters.\"",
      "T": "\"You breathed — and the sea covered them.\nThey sank like lead in those vast, indifferent depths.\""
    },
    "11": {
      "L": "Who is like unto thee, O LORD, among the gods? Who is like thee, glorious in holiness, fearful in praises, doing wonders?",
      "M": "\"Who is like you, O LORD, among the gods? Who is like you — majestic in holiness, awesome in praises, working wonders?\"",
      "T": "\"Who compares to you, Yahweh, among any so-called god?\nWho matches you — holy in majesty, terrible in glory, worker of wonders?\nNo one. Nothing.\""
    },
    "12": {
      "L": "Thou stretchedst out thy right hand; the earth swallowed them.",
      "M": "\"You stretched out your right hand; the earth swallowed them.\"",
      "T": "\"You reached out your hand — the earth swallowed them whole.\""
    },
    "13": {
      "L": "Thou in thy steadfast love hast led the people that thou hast redeemed; thou hast guided them in thy strength unto thy holy habitation.",
      "M": "\"In your steadfast love you have led the people you redeemed; you have guided them in your strength to your holy dwelling.\"",
      "T": "\"In your covenant loyalty you have led the people you ransomed;\nin your strength you have guided them toward your holy mountain.\""
    },
    "14": {
      "L": "The peoples have heard; they tremble; pangs have seized the inhabitants of Philistia.",
      "M": "\"The peoples heard and trembled; anguish seized the inhabitants of Philistia.\"",
      "T": "\"The nations have heard — they shudder.\nPhilistia writhes in sudden dread.\""
    },
    "15": {
      "L": "Then the chiefs of Edom were dismayed; the mighty men of Moab — trembling seized them; all the inhabitants of Canaan were melted away.",
      "M": "\"Then the chiefs of Edom were terrified; the leaders of Moab were seized with trembling; all the inhabitants of Canaan melted in fear.\"",
      "T": "\"The chiefs of Edom crumple with dread;\nthe warriors of Moab — their knees shake.\nAll of Canaan dissolves into panic.\""
    },
    "16": {
      "L": "Terror and dread shall fall upon them; by the greatness of thine arm they shall be still as a stone — till thy people pass over, O LORD, till the people pass over which thou hast purchased.",
      "M": "\"Terror and dread fall on them; by the power of your arm they are still as stone — until your people cross over, O LORD, until the people you have purchased pass by.\"",
      "T": "\"Terror and dread fall upon them;\nyour arm's vast power turns them to stone —\nuntil your people cross over, Yahweh,\nuntil the people you redeemed with blood and wonder pass through.\""
    },
    "17": {
      "L": "Thou shalt bring them in and plant them in the mountain of thine inheritance — the place, O LORD, which thou hast made for thee to dwell in; the sanctuary, O Lord, which thy hands have established.",
      "M": "\"You will bring them in and plant them on your own mountain — the place, O LORD, that you made as your dwelling, the sanctuary, O Lord, that your hands have established.\"",
      "T": "\"You will bring them in and plant them on your mountain,\nthe place you made your own home, Yahweh —\nthe sanctuary your hands built and will not abandon.\""
    },
    "18": {
      "L": "The LORD shall reign for ever and ever.",
      "M": "\"The LORD will reign forever and ever.\"",
      "T": "\"Yahweh reigns — forever and ever.\""
    },
    "19": {
      "L": "For the horse of Pharaoh went in with his chariots and with his horsemen into the sea, and the LORD brought again the waters of the sea upon them; but the sons of Israel walked on dry land in the midst of the sea.",
      "M": "For when Pharaoh's horses, chariots, and horsemen went into the sea, the LORD brought the waters back over them; but the Israelites had walked through the sea on dry ground.",
      "T": "Pharaoh's horses, his chariots, his cavalry — they entered the sea. Yahweh brought the sea back over them. But Israel had walked through on dry ground. The song is grounded in history; the poetry did not exaggerate."
    },
    "20": {
      "L": "And Miriam the prophetess, the sister of Aaron, took a timbrel in her hand; and all the women went out after her with timbrels and with dances.",
      "M": "Then Miriam the prophetess, Aaron's sister, took a tambourine in her hand, and all the women followed her with tambourines and dancing.",
      "T": "Then Miriam the prophetess — Aaron's sister, and a leader in her own right — took up a tambourine. All the women followed her out into the dance."
    },
    "21": {
      "L": "And Miriam answered them: Sing ye to the LORD, for he hath triumphed gloriously — the horse and his rider hath he thrown into the sea.",
      "M": "And Miriam sang to them: \"Sing to the LORD, for he has triumphed gloriously — the horse and its rider he has hurled into the sea.\"",
      "T": "Miriam led the response:\n\"Sing to Yahweh — he has risen in triumph!\nHorse and rider he has flung into the sea!\""
    },
    "22": {
      "L": "So Moses brought Israel from the Red Sea, and they went out into the wilderness of Shur; and they went three days in the wilderness and found no water.",
      "M": "Then Moses led Israel away from the Red Sea, and they went into the wilderness of Shur. They traveled for three days in the wilderness and found no water.",
      "T": "Moses led Israel away from the sea into the wilderness of Shur. Three days they walked. No water. The song had barely dried on their lips."
    },
    "23": {
      "L": "And when they came to Marah, they could not drink of the waters of Marah, for they were bitter; therefore the name of it was called Marah.",
      "M": "When they came to Marah, they could not drink the water there because it was bitter — that is why the place was called Marah.",
      "T": "At Marah the water was undrinkable — bitter as salt. So the place was named for it: Marah. Bitterness."
    },
    "24": {
      "L": "And the people murmured against Moses, saying, What shall we drink?",
      "M": "The people grumbled against Moses, saying, \"What are we to drink?\"",
      "T": "The people turned on Moses: 'What are we supposed to drink?'"
    },
    "25": {
      "L": "And he cried unto the LORD; and the LORD shewed him a tree; and he cast it into the waters, and the waters were made sweet. There he made for them a statute and an ordinance, and there he proved them.",
      "M": "Moses cried out to the LORD, and the LORD showed him a piece of wood; he threw it into the water, and the water became sweet. There the LORD gave them a statute and a rule, and there he tested them,",
      "T": "Moses cried out. Yahweh showed him a tree — he threw it in, and the bitter water turned sweet. It was also the place where Yahweh set a legal standard and began to test them: could they trust him when conditions were hard?"
    },
    "26": {
      "L": "Saying, If thou wilt diligently hearken to the voice of the LORD thy God, and wilt do that which is right in his sight, and wilt give ear to his commandments and keep all his statutes, I will put none of these diseases upon thee which I have brought upon the Egyptians; for I am the LORD that healeth thee.",
      "M": "saying, \"If you will carefully listen to the voice of the LORD your God and do what is right in his eyes, giving heed to his commandments and keeping all his statutes, I will not bring on you any of the diseases I brought on the Egyptians; for I am the LORD who heals you.\"",
      "T": "'If you will truly listen to Yahweh your God — do what is right, heed his commands, keep his statutes — then I will not send on you the plagues I sent on Egypt. I am Yahweh your healer.' The offer at Marah: obedience in exchange for the health Egypt lost."
    },
    "27": {
      "L": "And they came to Elim, where were twelve wells of water and threescore and ten palm trees; and they encamped there by the waters.",
      "M": "Then they came to Elim, where there were twelve springs and seventy palm trees; and they camped there by the water.",
      "T": "Then they reached Elim — twelve springs, seventy palms, water enough for everyone. They camped beside it and rested."
    }
  },
  # ── Chapter 16: Manna and Quail ──
  "16": {
    "1": {
      "L": "And they took their journey from Elim, and all the congregation of the sons of Israel came unto the wilderness of Sin, which is between Elim and Sinai, on the fifteenth day of the second month after their departing out of the land of Egypt.",
      "M": "The whole Israelite community set out from Elim and came to the wilderness of Sin, which lies between Elim and Sinai, on the fifteenth day of the second month after they had left Egypt.",
      "T": "The whole congregation moved out from Elim into the wilderness of Sin — halfway between Elim and Sinai — on the fifteenth day of the second month. Exactly one month since they had left Egypt."
    },
    "2": {
      "L": "And the whole congregation of the sons of Israel murmured against Moses and Aaron in the wilderness.",
      "M": "In the wilderness the whole Israelite community grumbled against Moses and Aaron.",
      "T": "In the wilderness the whole congregation turned against Moses and Aaron. Hunger drives short memories."
    },
    "3": {
      "L": "And the sons of Israel said unto them, Would that we had died by the hand of the LORD in the land of Egypt, when we sat by the pots of flesh and ate bread to the full; for ye have brought us forth into this wilderness to kill this whole assembly with hunger.",
      "M": "The Israelites said to them, \"If only we had died by the LORD's hand in Egypt! There we sat by the pots of meat and ate all the food we wanted; but you have brought us out into this wilderness to starve this whole community to death.\"",
      "T": "'We should have died in Egypt — at least there we had meat, bread, enough. You brought us out here to starve the whole community.' They had exchanged slavery with food for freedom with hunger, and freedom was losing."
    },
    "4": {
      "L": "Then said the LORD unto Moses, Behold, I will rain bread from heaven for you; and the people shall go out and gather a day's portion every day, that I may prove them whether they will walk in my law or no.",
      "M": "Then the LORD said to Moses, \"I am going to rain bread from heaven for you. The people shall go out and gather enough for that day — each day's portion that day — so that I can test whether they will follow my instructions or not.\"",
      "T": "Yahweh said to Moses: 'I will rain bread from the sky. Each day they gather what they need for that day — no more, no less. It is a test: can they trust daily provision? Can they stop hoarding and rest in my sufficiency?'"
    },
    "5": {
      "L": "And it shall come to pass on the sixth day that they shall prepare that which they bring in; and it shall be twice as much as they gather daily.",
      "M": "\"On the sixth day, when they prepare what they bring in, it will be twice as much as they gather on the other days.\"",
      "T": "'On the sixth day they will prepare double — because the seventh is for rest, not gathering.'"
    },
    "6": {
      "L": "And Moses and Aaron said unto all the sons of Israel, At even, then ye shall know that the LORD hath brought you out from the land of Egypt.",
      "M": "So Moses and Aaron told all the Israelites, \"By evening you will know that it was the LORD who brought you out of Egypt,\"",
      "T": "Moses and Aaron addressed the whole company: 'This evening you will see that it was Yahweh who brought you out of Egypt.'"
    },
    "7": {
      "L": "And in the morning, then ye shall see the glory of the LORD; for that he heareth your murmurings against the LORD; and what are we, that ye murmur against us?",
      "M": "\"and in the morning you will see the glory of the LORD, because he has heard your grumbling against him. Who are we, that you should grumble against us?\"",
      "T": "'In the morning you will see Yahweh's glory — because he has heard you grumbling against him. We are nothing. Your complaint is not with us; it is with God.'"
    },
    "8": {
      "L": "And Moses said, This shall be when the LORD shall give you in the evening flesh to eat and in the morning bread to the full; for that the LORD heareth your murmurings which ye murmur against him; and what are we? your murmurings are not against us, but against the LORD.",
      "M": "Moses said, \"You will know this when the LORD gives you meat to eat in the evening and all the bread you want in the morning, because the LORD has heard your grumbling against him. We are nothing — your grumbling is not against us but against the LORD.\"",
      "T": "'Yahweh will give you meat at dusk and bread at dawn — because he heard your complaint. And let me be clear: your quarrel is not with Moses and Aaron. It is with Yahweh himself.'"
    },
    "9": {
      "L": "And Moses said unto Aaron, Say unto all the congregation of the sons of Israel, Come near before the LORD; for he hath heard your murmurings.",
      "M": "Then Moses told Aaron, \"Say to the entire Israelite community: 'Come before the LORD, for he has heard your grumbling.'\"",
      "T": "Moses said to Aaron: 'Call the assembly before Yahweh — he has heard them.'"
    },
    "10": {
      "L": "And it came to pass as Aaron spake unto the whole congregation of the sons of Israel, that they looked toward the wilderness, and behold, the glory of the LORD appeared in the cloud.",
      "M": "While Aaron was speaking to the whole Israelite community, they turned toward the wilderness and saw the glory of the LORD appearing in the cloud.",
      "T": "As Aaron spoke, they turned and looked out toward the wilderness — and the glory of Yahweh blazed in the cloud."
    },
    "11": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "Yahweh spoke to Moses:"
    },
    "12": {
      "L": "I have heard the murmurings of the sons of Israel; speak unto them, saying, At even ye shall eat flesh, and in the morning ye shall be filled with bread; and ye shall know that I am the LORD your God.",
      "M": "\"I have heard the grumbling of the Israelites. Tell them: 'At evening you will eat meat, and in the morning you will have all the bread you want. Then you will know that I am the LORD your God.'\"",
      "T": "'I have heard the grumbling. Tell them: at dusk — meat. At dawn — bread enough. And through this they will come to know: I am Yahweh their God.'"
    },
    "13": {
      "L": "And it came to pass at even that the quail came up and covered the camp; and in the morning the dew lay round about the camp.",
      "M": "That evening quail came and covered the camp; and in the morning there was a layer of dew around the camp.",
      "T": "That evening quail descended and blanketed the camp. By morning, dew lay all around — and when it lifted, something was left on the ground."
    },
    "14": {
      "L": "And when the dew that lay was gone up, behold, upon the face of the wilderness there lay a thin flaky thing, thin as hoar frost on the ground.",
      "M": "When the dew had evaporated, there on the surface of the wilderness were thin, flaky flakes, as fine as frost on the ground.",
      "T": "When the dew evaporated, a thin flaky substance lay over the ground — fine as frost, delicate as scales. Something no one had seen before."
    },
    "15": {
      "L": "And when the sons of Israel saw it, they said one to another, What is it? For they knew not what it was. And Moses said unto them, This is the bread which the LORD hath given you to eat.",
      "M": "When the Israelites saw it, they asked each other, \"What is it?\" — for they did not know what it was. Moses said to them, \"This is the bread the LORD has given you to eat.\"",
      "T": "'What is it?' — they asked each other. The Hebrew word stuck: man hu, 'what is it?' — and the name manna was born from the question. Moses answered: 'This is the bread Yahweh has given you.'"
    },
    "16": {
      "L": "This is the thing which the LORD hath commanded: Gather ye of it every man according to his eating — an omer for every man, according to the number of your persons; take ye every man for them which are in his tents.",
      "M": "\"This is what the LORD has commanded: 'Each of you is to gather as much as you need — an omer per person, according to the number of people you have; each person is to gather for those in their own tent.'\"",
      "T": "'Yahweh's instruction: gather an omer per person — one day's portion per head, for everyone in your tent. No more, no less.'"
    },
    "17": {
      "L": "And the sons of Israel did so; and gathered some more, some less.",
      "M": "The Israelites did so — some gathered more, some less.",
      "T": "They gathered — some more, some less, each according to their energy and their fear."
    },
    "18": {
      "L": "And when they did mete it with an omer, he that gathered much had nothing over, and he that gathered little had no lack; they gathered every man according to his eating.",
      "M": "But when they measured it by the omer, those who gathered more had nothing left over, and those who gathered less had no shortage; each had gathered exactly what they needed.",
      "T": "When they measured it out, something extraordinary happened: whoever had gathered much found only an omer; whoever had gathered little had a full omer. The provision was self-equalising. No one had too much; no one had too little."
    },
    "19": {
      "L": "And Moses said, Let no man leave of it till the morning.",
      "M": "Then Moses said to them, \"No one is to keep any of it until morning.\"",
      "T": "'Leave none of it till morning,' Moses said."
    },
    "20": {
      "L": "Notwithstanding they hearkened not unto Moses; but some of them left of it until the morning, and it bred worms and stank; and Moses was wroth with them.",
      "M": "However, some of them paid no attention to Moses; they kept part of it until morning — and it became full of maggots and smelled foul. Moses was angry with them.",
      "T": "Some didn't listen. They kept a supply overnight — and by morning it was writhing with maggots and reeked. Moses was furious. The provision was not meant to be hoarded; it was meant to be trusted."
    },
    "21": {
      "L": "And they gathered it every morning, every man according to his eating; and when the sun waxed hot, it melted.",
      "M": "Each morning everyone gathered as much as they needed; when the sun grew hot, it melted away.",
      "T": "Each morning they gathered it — each person what they needed. When the sun climbed, it melted. Each day a fresh start, a fresh provision, a fresh act of trust."
    },
    "22": {
      "L": "And it came to pass that on the sixth day they gathered twice as much bread — two omers for one man; and all the rulers of the congregation came and told Moses.",
      "M": "On the sixth day they gathered twice as much — two omers per person — and all the community leaders came and reported this to Moses.",
      "T": "On the sixth day the gathering doubled naturally — two omers a head. The community leaders came to Moses, puzzled."
    },
    "23": {
      "L": "And he said unto them, This is that which the LORD hath said: Tomorrow is a rest, a holy sabbath unto the LORD; bake that which ye will bake today, and seethe that ye will seethe; and that which remaineth over lay up for you to be kept until the morning.",
      "M": "He said to them, \"This is what the LORD said: 'Tomorrow is a Sabbath rest — a holy Sabbath to the LORD. Bake what you want to bake and boil what you want to boil; save whatever is left and keep it until morning.'\"",
      "T": "'Yahweh said: Tomorrow is Sabbath — a holy rest. Cook what you want today. What remains, set aside. It will keep. The Sabbath is sacred; it needs no bread-gathering to validate it.'"
    },
    "24": {
      "L": "And they laid it up till the morning, as Moses bade; and it did not stink, neither was there any worm therein.",
      "M": "So they saved it until morning, as Moses instructed, and it did not spoil or become infested with maggots.",
      "T": "They set the double portion aside. In the morning it was unchanged — no rot, no worms. The Sabbath provision played by different rules."
    },
    "25": {
      "L": "And Moses said, Eat that today; for today is a sabbath unto the LORD; today ye shall not find it in the field.",
      "M": "\"Eat it today,\" Moses said, \"for today is a Sabbath to the LORD. You will not find any of it on the ground today.\"",
      "T": "'Eat it today,' Moses told them. 'Today is Sabbath — Yahweh's rest. There is nothing in the field today. The ground itself is resting.'"
    },
    "26": {
      "L": "Six days ye shall gather it; but on the seventh day which is the sabbath, in it there shall be none.",
      "M": "\"Six days you are to gather it; but on the seventh day, the Sabbath, there will be none.\"",
      "T": "'Six days — gather. The seventh day is Sabbath. There will be nothing to find. The pattern is built into the provision.'"
    },
    "27": {
      "L": "And it came to pass that there went out some of the people on the seventh day for to gather, and they found none.",
      "M": "Nevertheless, some of the people went out on the seventh day to gather — but found nothing.",
      "T": "Some went out on the seventh day anyway. They found nothing. Distrust costs you the rest."
    },
    "28": {
      "L": "And the LORD said unto Moses, How long refuse ye to keep my commandments and my laws?",
      "M": "Then the LORD said to Moses, \"How long will you refuse to keep my commands and my instructions?\"",
      "T": "Yahweh said to Moses: 'How long will they refuse to trust me and keep my instructions?'"
    },
    "29": {
      "L": "See, for that the LORD hath given you the sabbath; therefore he giveth you on the sixth day the bread of two days; abide ye every man in his place; let no man go out of his place on the seventh day.",
      "M": "\"See — the LORD has given you the Sabbath; that is why he provides bread for two days on the sixth day. Everyone is to stay where they are on the seventh day; no one is to go out.\"",
      "T": "'Understand: Yahweh has given you the Sabbath. That is why the sixth-day provision is doubled. Stay home on the seventh day. The Sabbath is a gift. Stop treating it as an inconvenience.'"
    },
    "30": {
      "L": "So the people rested on the seventh day.",
      "M": "And the people rested on the seventh day.",
      "T": "And the people rested."
    },
    "31": {
      "L": "And the house of Israel called the name thereof Manna; and it was like coriander seed, white; and the taste of it was like wafers made with honey.",
      "M": "The Israelites called the food manna. It was white like coriander seed and tasted like wafers made with honey.",
      "T": "Israel named it manna — 'What is it?' — a daily reminder that the provision came before the understanding. It was white, flaky, fine like coriander seed, sweet as honey wafers."
    },
    "32": {
      "L": "And Moses said, This is the thing which the LORD hath commanded: Fill an omer of it to be kept for your generations; that they may see the bread wherewith I have fed you in the wilderness, when I brought you forth from the land of Egypt.",
      "M": "Moses said, \"This is what the LORD has commanded: 'Keep an omer of manna for your future generations, so they can see the bread I gave you to eat in the wilderness when I brought you out of Egypt.'\"",
      "T": "'Yahweh commands: keep an omer of it for all your generations — so that your descendants can see with their own eyes the bread their ancestors ate in the wilderness when Yahweh brought them out of Egypt.'"
    },
    "33": {
      "L": "And Moses said unto Aaron, Take a pot and put an omer full of manna therein, and lay it up before the LORD to be kept for your generations.",
      "M": "So Moses told Aaron, \"Take a jar and put an omer of manna in it. Then place it before the LORD to be kept for the generations to come.\"",
      "T": "Moses told Aaron: 'Take a jar, fill it with an omer of manna, and set it before Yahweh as a memorial for all future generations.'"
    },
    "34": {
      "L": "As the LORD commanded Moses, so Aaron laid it up before the Testimony to be kept.",
      "M": "As the LORD had commanded Moses, Aaron placed the jar before the Testimony to be preserved.",
      "T": "Aaron did as Yahweh had commanded — he placed the jar before the Testimony, where it would remain as a witness."
    },
    "35": {
      "L": "And the sons of Israel did eat manna forty years, until they came to a land inhabited; they did eat manna until they came unto the borders of the land of Canaan.",
      "M": "The Israelites ate manna for forty years, until they reached a settled land; they ate manna until they came to the border of Canaan.",
      "T": "Forty years. Manna every morning for forty years, until they reached land that could grow grain. The provision outlasted every doubt, every failure, every rebellion — until they came to the edge of Canaan."
    },
    "36": {
      "L": "Now an omer is the tenth part of an ephah.",
      "M": "(An omer is one-tenth of an ephah.)",
      "T": "An omer is one-tenth of an ephah — a day's portion, small enough to remind you daily that you depend on God."
    }
  },
  # ── Chapter 17: Water from the Rock; Battle with Amalek ──
  "17": {
    "1": {
      "L": "And all the congregation of the sons of Israel journeyed from the wilderness of Sin, by their stages, according to the commandment of the LORD; and they encamped in Rephidim, and there was no water for the people to drink.",
      "M": "The whole Israelite community set out from the wilderness of Sin by stages, as the LORD directed; they camped at Rephidim, where there was no water for the people to drink.",
      "T": "The whole congregation moved on from the wilderness of Sin in stages — Yahweh directed each step. They camped at Rephidim. There was no water."
    },
    "2": {
      "L": "Wherefore the people did chide with Moses, and said, Give us water that we may drink. And Moses said unto them, Why do ye chide with me? Wherefore do ye tempt the LORD?",
      "M": "So the people quarreled with Moses and said, \"Give us water to drink.\" Moses replied, \"Why do you quarrel with me? Why do you put the LORD to the test?\"",
      "T": "The people quarrelled with Moses: 'Give us water.' Moses fired back: 'Why are you fighting with me? Why are you testing Yahweh?'"
    },
    "3": {
      "L": "And the people thirsted there for water; and the people murmured against Moses and said, Wherefore is this that thou hast brought us up out of Egypt — to kill us and our children and our cattle with thirst?",
      "M": "But the people were thirsty for water there and grumbled against Moses. They said, \"Why did you ever bring us out of Egypt to make us and our children and our livestock die of thirst?\"",
      "T": "But thirst overwhelmed reason. They turned on Moses again: 'Why did you bring us out of Egypt? To kill us — our children, our animals — with thirst?'"
    },
    "4": {
      "L": "And Moses cried unto the LORD, saying, What shall I do unto this people? They be almost ready to stone me.",
      "M": "Then Moses cried out to the LORD, \"What am I to do with this people? They are almost ready to stone me!\"",
      "T": "Moses cried out to Yahweh: 'What do I do with these people? They are one step from stoning me.'"
    },
    "5": {
      "L": "And the LORD said unto Moses, Go on before the people, and take with thee of the elders of Israel; and thy rod wherewith thou smotest the river, take in thine hand, and go.",
      "M": "The LORD answered Moses, \"Walk out in front of the people. Take with you some of the elders of Israel and carry in your hand the staff with which you struck the Nile, and go.\"",
      "T": "Yahweh answered: 'Walk out ahead of them. Bring elders as witnesses. Carry the staff that split the Nile. Go.'"
    },
    "6": {
      "L": "Behold, I will stand before thee there upon the rock in Horeb; and thou shalt smite the rock, and there shall come water out of it, that the people may drink. And Moses did so in the sight of the elders of Israel.",
      "M": "\"I will stand there before you on the rock at Horeb; strike the rock, and water will come out of it for the people to drink.\" Moses did this in the sight of the elders of Israel.",
      "T": "'I will stand on the rock at Horeb. Strike it. Water will flow.' Moses obeyed before the elders — witnesses to the moment. The rock that needed striking was not abandoned; God stood on it."
    },
    "7": {
      "L": "And he called the name of the place Massah and Meribah, because of the chiding of the sons of Israel, and because they tempted the LORD, saying, Is the LORD among us or not?",
      "M": "He named the place Massah and Meribah — Testing and Quarreling — because the Israelites quarreled and because they tested the LORD by saying, \"Is the LORD among us or not?\"",
      "T": "He named it Massah — Testing — and Meribah — Quarrelling. Because Israel had asked the question that lay beneath all their grumbling: 'Is Yahweh actually here?' The question itself was a failure of faith. But the water flowed anyway."
    },
    "8": {
      "L": "Then came Amalek and fought with Israel in Rephidim.",
      "M": "The Amalekites came and attacked Israel at Rephidim.",
      "T": "Then Amalek struck — an attack on Israel at Rephidim. The first military conflict of the wilderness years."
    },
    "9": {
      "L": "And Moses said unto Joshua, Choose us out men and go out; fight with Amalek. Tomorrow I will stand on the top of the hill with the rod of God in mine hand.",
      "M": "Moses said to Joshua, \"Choose some men and go out and fight against the Amalekites. Tomorrow I will stand on the hilltop with the staff of God in my hand.\"",
      "T": "Moses turned to Joshua: 'Select your fighters and engage Amalek. Tomorrow I will stand on the hill with the staff of God.' Leadership in battle took two forms here: Joshua in the field and Moses on the height."
    },
    "10": {
      "L": "So Joshua did as Moses had said to him and fought with Amalek; and Moses, Aaron, and Hur went up to the top of the hill.",
      "M": "Joshua fought the Amalekites as Moses had ordered. Moses, Aaron, and Hur went up to the top of the hill.",
      "T": "Joshua took the field. Moses, Aaron, and Hur climbed to the summit."
    },
    "11": {
      "L": "And it came to pass when Moses held up his hand that Israel prevailed; and when he let down his hand Amalek prevailed.",
      "M": "As long as Moses held up his hand, Israel had the upper hand; whenever he lowered his hand, Amalek gained the advantage.",
      "T": "When Moses raised his hands, Israel advanced. When his arms dropped, Amalek pushed forward. The battle below was linked to the posture above. Prayer and warfare were not separate."
    },
    "12": {
      "L": "But Moses' hands were heavy; and they took a stone and put it under him and he sat thereon; and Aaron and Hur stayed up his hands, the one on the one side and the other on the other side; and his hands were steady until the going down of the sun.",
      "M": "When Moses' hands grew heavy, Aaron and Hur took a stone and put it under him so he could sit. They held his hands up — one on each side — and his hands remained steady until sunset.",
      "T": "Moses' arms grew heavy. Aaron and Hur set a stone for him to sit on and each took one arm and held it up. Two men held up the man who held up Israel. His arms stayed steady until the sun went down."
    },
    "13": {
      "L": "And Joshua discomfited Amalek and his people with the edge of the sword.",
      "M": "So Joshua overwhelmed the Amalekite army with the sword.",
      "T": "Joshua routed Amalek with the sword."
    },
    "14": {
      "L": "And the LORD said unto Moses, Write this for a memorial in a book and rehearse it in the ears of Joshua; for I will utterly put out the remembrance of Amalek from under heaven.",
      "M": "Then the LORD said to Moses, \"Write this on a scroll as a reminder and make sure Joshua hears it: I will completely blot out the memory of Amalek from under heaven.\"",
      "T": "Yahweh commanded: 'Write this down and read it to Joshua: I will utterly erase the memory of Amalek from under heaven.' The judgment was decreed before the next battle began."
    },
    "15": {
      "L": "And Moses built an altar and called the name of it Jehovah-nissi.",
      "M": "Moses built an altar and named it \"The LORD is my banner.\"",
      "T": "Moses built an altar and named it: Yahweh-Nissi — Yahweh is my banner. Victory did not belong to Joshua's sword; it belonged to the one who sustained Moses' arms."
    },
    "16": {
      "L": "And he said, Because the LORD hath sworn: the LORD will have war with Amalek from generation to generation.",
      "M": "He said, \"A hand upon the throne of the LORD! The LORD will be at war with Amalek from generation to generation.\"",
      "T": "He said: 'His throne is pledged to this — Yahweh will be at war with Amalek age after age.' Not merely a battle but a long covenantal conflict. The altar was a declaration, not a celebration."
    }
  },
  # ── Chapter 18: Jethro's Visit and Counsel ──
  "18": {
    "1": {
      "L": "And Jethro the priest of Midian, father in law of Moses, heard of all that God had done for Moses and for Israel his people — that the LORD had brought Israel out of Egypt.",
      "M": "Now Jethro, the priest of Midian and father-in-law of Moses, heard about everything God had done for Moses and for Israel his people — and how the LORD had brought Israel out of Egypt.",
      "T": "Jethro, priest of Midian and Moses' father-in-law, heard the whole story — what God had done for Moses and for Israel, how Yahweh had brought them out of Egypt. The news of the exodus had reached Midian."
    },
    "2": {
      "L": "Then Jethro, Moses' father in law, took Zipporah, Moses' wife, after he had sent her back,",
      "M": "After Moses had sent his wife Zipporah back, his father-in-law Jethro had received her.",
      "T": "Moses had sent Zipporah home earlier — away from the dangerous confrontation with Pharaoh. Now Jethro brought her back to him."
    },
    "3": {
      "L": "and her two sons — of whom the name of the one was Gershom, for Moses said, I have been a sojourner in a foreign land,",
      "M": "along with her two sons. One was named Gershom, for Moses had said, \"I have been a foreigner in a foreign land,\"",
      "T": "and her two sons. The first was named Gershom — 'a stranger there' — because Moses had said when the boy was born: 'I have been an alien in a foreign land.'"
    },
    "4": {
      "L": "and the name of the other was Eliezer, for he said, The God of my father was my help, and delivered me from the sword of Pharaoh.",
      "M": "and the other was Eliezer, for Moses had said, \"My father's God was my help; he rescued me from Pharaoh's sword.\"",
      "T": "The second was Eliezer — 'my God is help' — because Moses had said at his birth: 'My father's God was my help and delivered me from Pharaoh's sword.' Both names were theology. Both names were autobiography."
    },
    "5": {
      "L": "And Jethro, Moses' father in law, came with his sons and his wife unto Moses into the wilderness where he was encamped at the mountain of God.",
      "M": "Jethro, Moses' father-in-law, came with Moses' sons and wife to him in the wilderness where he was camped at the mountain of God.",
      "T": "Jethro arrived at the mountain of God — the same mountain where Yahweh had first spoken to Moses from the burning bush — bringing Zipporah and the boys."
    },
    "6": {
      "L": "And he said unto Moses, I thy father in law Jethro am come unto thee, and thy wife and her two sons with her.",
      "M": "He sent word to Moses: \"I, your father-in-law Jethro, am coming to you with your wife and her two sons.\"",
      "T": "He sent a message ahead: 'I — Jethro, your father-in-law — am coming. Your wife and sons are with me.'"
    },
    "7": {
      "L": "And Moses went out to meet his father in law, and did obeisance and kissed him; and they asked each man of his fellow's welfare; and they came into the tent.",
      "M": "So Moses went out to meet his father-in-law and bowed down and kissed him; they greeted each other and then went into the tent.",
      "T": "Moses went out to meet him — bowed, embraced, kissed him. They exchanged questions about each other's welfare, then went inside. No ceremony; just reunion."
    },
    "8": {
      "L": "And Moses told his father in law all that the LORD had done unto Pharaoh and to the Egyptians for Israel's sake, and all the travail that had come upon them by the way, and how the LORD delivered them.",
      "M": "Moses told his father-in-law everything the LORD had done to Pharaoh and the Egyptians for Israel's sake, and all the hardship they had encountered along the way, and how the LORD had delivered them.",
      "T": "Moses told the whole story — what Yahweh had done to Pharaoh, to Egypt, for Israel's sake; the hardships along the way; the deliverances that had punctuated the journey. He held nothing back."
    },
    "9": {
      "L": "And Jethro rejoiced for all the goodness which the LORD had done to Israel, whom he had delivered out of the hand of the Egyptians.",
      "M": "Jethro was delighted to hear about all the good things the LORD had done for Israel in rescuing them from the Egyptians.",
      "T": "Jethro was filled with joy at the goodness Yahweh had shown Israel — how he had rescued them from Egypt's grip. The outsider rejoiced in Israel's liberation."
    },
    "10": {
      "L": "And Jethro said, Blessed be the LORD, who hath delivered you out of the hand of the Egyptians, and out of the hand of Pharaoh — who hath delivered the people from under the hand of the Egyptians.",
      "M": "He said, \"Praise be to the LORD, who rescued you from the Egyptians and from Pharaoh, and who delivered the people from under Egyptian oppression.\"",
      "T": "Jethro said: 'Blessed be Yahweh, who rescued you from Egypt and from Pharaoh — who delivered his people from under Egypt's crushing hand.' A Midianite priest worshipping Israel's God."
    },
    "11": {
      "L": "Now I know that the LORD is greater than all gods; for in the very thing wherein they dealt proudly he was above them.",
      "M": "\"Now I know that the LORD is greater than all other gods, for he showed this very thing when the Egyptians dealt arrogantly with Israel.\"",
      "T": "'Now I know — I know — that Yahweh towers above every god. In the very thing Egypt used to oppress, Yahweh used to judge. Their pride was their undoing; his honour was vindicated.' Jethro had come to a conclusion. It was a conversion."
    },
    "12": {
      "L": "And Jethro, Moses' father in law, took a burnt offering and sacrifices for God; and Aaron came and all the elders of Israel to eat bread with Moses' father in law before God.",
      "M": "Then Jethro, Moses' father-in-law, brought a burnt offering and other sacrifices to God; and Aaron and all the elders of Israel came to eat a meal with Moses' father-in-law in the presence of God.",
      "T": "Jethro brought burnt offerings and sacrifices to God. Aaron and all the elders of Israel came and shared a covenant meal with Moses' father-in-law in the presence of God. An outsider's table became holy ground."
    },
    "13": {
      "L": "And it came to pass on the morrow that Moses sat to judge the people; and the people stood by Moses from the morning unto the evening.",
      "M": "The next day Moses took his seat to serve as judge for the people; and the people stood around him from morning until evening.",
      "T": "The next morning Moses sat to judge the people — and they queued from dawn to dusk. The line never ended."
    },
    "14": {
      "L": "And when Moses' father in law saw all that he did to the people, he said, What is this thing that thou doest to the people? Why sittest thou thyself alone, and all the people stand by thee from morning unto even?",
      "M": "When his father-in-law saw all that Moses was doing for the people, he said, \"What is this you are doing for the people? Why do you alone sit as judge, while all these people stand around you from morning until evening?\"",
      "T": "Jethro watched all day. Then he asked: 'What are you doing? Why are you alone in the seat while all these people wait from sunrise to sunset?'"
    },
    "15": {
      "L": "And Moses said unto his father in law, Because the people come unto me to enquire of God.",
      "M": "Moses answered his father-in-law, \"Because the people come to me to seek God's will.\"",
      "T": "Moses explained: 'They come to me to inquire of God.'"
    },
    "16": {
      "L": "When they have a matter, they come unto me; and I judge between one and another, and I make them know the statutes of God and his laws.",
      "M": "\"Whenever they have a dispute, it is brought to me; I decide between the parties and inform them of God's decrees and instructions.\"",
      "T": "'When there is a dispute they bring it to me. I decide between them and teach them God's statutes and laws.' A right answer. But not a sustainable one."
    },
    "17": {
      "L": "And Moses' father in law said unto him, The thing that thou doest is not good.",
      "M": "Moses' father-in-law replied, \"What you are doing is not good.\"",
      "T": "Jethro didn't soften it: 'What you are doing is not good.'"
    },
    "18": {
      "L": "Thou wilt surely wear away, both thou, and this people that is with thee; for this thing is too heavy for thee; thou art not able to perform it thyself alone.",
      "M": "\"You will only wear yourself out — and these people too. The work is too heavy for you; you cannot handle it alone.\"",
      "T": "'You will exhaust yourself — and the people too. This is too heavy for one man. You cannot carry it alone.'"
    },
    "19": {
      "L": "Hearken now unto my voice; I will give thee counsel, and God shall be with thee: Be thou for the people to Godward, that thou mayest bring the causes unto God.",
      "M": "\"Listen now to me and I will give you some advice, and may God be with you. You must be the people's representative before God and bring their disputes to him.\"",
      "T": "'Listen to me — I offer counsel, and may God confirm it. You should remain the people's representative before God — the one who brings the great cases to him.'"
    },
    "20": {
      "L": "And thou shalt teach them the statutes and the laws, and shalt shew them the way wherein they must walk and the work that they must do.",
      "M": "\"Teach them his decrees and instructions; show them the way to live and the duties they are to fulfill.\"",
      "T": "'Teach them the statutes and laws. Show them the path to walk and what their work looks like. Give them the principles so they can apply them.'"
    },
    "21": {
      "L": "Moreover thou shalt provide out of all the people able men — such as fear God, men of truth, hating unjust gain — and place such over them to be rulers of thousands, of hundreds, of fifties, and of tens.",
      "M": "\"But select capable men from all the people — men who fear God, trustworthy men who hate dishonest gain — and appoint them as officials over thousands, hundreds, fifties, and tens.\"",
      "T": "'But this: find capable men — men who fear God, who are truthful, who despise bribes — and appoint them as leaders of thousands, hundreds, fifties, and tens. Distribute authority. What you cannot carry alone, share.'"
    },
    "22": {
      "L": "And let them judge the people at all times; and it shall be that every great matter they shall bring unto thee, but every small matter they shall judge themselves; so shall it be easier for thee, and they shall bear the burden with thee.",
      "M": "\"Have them serve as judges for the people at all times, but have them bring every major case to you — the minor cases they can decide themselves. That way your load will be lighter because they will share it with you.\"",
      "T": "'Let them judge the routine cases. Only the large and difficult ones come to you. The burden will be shared and you will last. And so will they.'"
    },
    "23": {
      "L": "If thou shalt do this thing, and God command thee so, then thou shalt be able to endure, and all this people shall also go to their place in peace.",
      "M": "\"If you do this and God so commands, you will be able to stand the strain, and all these people will go home satisfied.\"",
      "T": "'If you do this — and if God confirms it — you will endure. And all these people will go home in peace instead of waiting in exhaustion.'"
    },
    "24": {
      "L": "So Moses hearkened to the voice of his father in law and did all that he had said.",
      "M": "Moses listened to his father-in-law and did everything he said.",
      "T": "Moses listened. He implemented everything Jethro had said. Wisdom does not require a prophet; it can come from a Midianite father-in-law."
    },
    "25": {
      "L": "And Moses chose able men out of all Israel and made them heads over the people — rulers of thousands, of hundreds, of fifties, and of tens.",
      "M": "He chose capable men from all Israel and made them leaders of the people — officials over thousands, hundreds, fifties, and tens.",
      "T": "Moses chose capable men from across Israel and appointed them leaders: over thousands, hundreds, fifties, tens. A structure was built."
    },
    "26": {
      "L": "And they judged the people at all times; the hard causes they brought unto Moses, but every small matter they judged themselves.",
      "M": "They served as judges for the people at all times. The difficult cases they brought to Moses, but the simple ones they decided themselves.",
      "T": "They handled the everyday disputes. The hard cases came to Moses. The system worked because the responsibility was distributed."
    },
    "27": {
      "L": "And Moses let his father in law depart; and he went his way into his own land.",
      "M": "Then Moses sent his father-in-law on his way, and Jethro returned to his own country.",
      "T": "Moses said goodbye to Jethro, and his father-in-law went home to Midian. He had brought Moses' family back, shared a sacrifice, given counsel that would shape Israel's governance for generations, and departed. A brief visit; a lasting legacy."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'exodus')
        merge_tier(existing, EXODUS, tier_key)
        save(tier_dir, 'exodus', existing)
    print('Exodus 13–18 written.')

if __name__ == '__main__':
    main()
