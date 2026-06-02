"""
MKT Exodus chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-exodus-19-24.py

Covers the Sinai covenant unit: Israel's arrival and the theophany (ch. 19), the Decalogue
(ch. 20), the Book of the Covenant laws (chs. 21–23), and the covenant ratification (ch. 24).

Translation decisions:
- H3068 (יהוה): "the LORD" throughout — matches Genesis convention
- H430 (אֱלֹהִים): "God" throughout — matches Genesis convention
- H5459 (סְגֻלָּה) at 19:5: L="special possession", M="treasured possession",
  T="most precious treasure" — the term denotes a monarch's personal portable treasury,
  the thing kept closest; KJV "peculiar treasure" is archaic and misleading
- H4467+H3548 at 19:6: L/M="kingdom of priests", T="nation of royal priests" —
  Israel is to mediate between God and the nations; echoes 1 Pet 2:9
- H6918 (קָדוֹשׁ) at 19:6: "holy" = set apart for divine purpose, not merely morally pure
- H7523 (רָצַח) at 20:13: "murder" in all three tiers, NOT "kill" — this is the
  Hebrew word for unlawful premeditated killing; the KJV rendering "kill" is too broad
- H2530 (חָמַד) at 20:17: "covet" / T="crave" — to desire what belongs to another
- H2617 (חֶסֶד) at 20:6: L="steadfast love", M="faithful love", T="covenant loyalty"
- H4941 (מִשְׁפָּט) at 21:1: L="judgments", M="ordinances", T="rulings" — the body
  of case law in chs. 21–23 is the Book of the Covenant
- H1616 (גֵּר) at 22:21; 23:9: L="stranger", M="foreigner", T="immigrant" —
  covenant hospitality ethic grounded in Israel's own Egyptian experience
- H1285 (בְּרִית) at 24:7-8: "covenant" — the blood rite seals the Sinai covenant;
  the phrase "blood of the covenant" is deliberately echoed by Jesus at the Last Supper
- H3519 (כָּבוֹד) at 24:16-17: "glory" — the weighty, luminous, visible divine presence
- H6588 (פֶּשַׁע) at 23:21: "rebellion/transgressions" — deliberate covenant defection,
  not mere moral stumbling
- Lex talionis (21:24-25): "eye for eye" sets a ceiling on vengeance, not a floor;
  rendered literally in L; T preserves the proportionality principle
- Divine passive in penalty clauses: "shall be surely put to death" — human courts
  execute, but God is the ultimate judge; the doubling ("surely") is emphatic infinitive
- Verbal aspect: Hebrew imperfect negated in the Decalogue = permanent prohibition
  "you shall not / you will not"
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
  "19": {
    "1": {
      "L": "In the third month of the going out of the children of Israel from the land of Egypt, on that same day, they came into the wilderness of Sinai.",
      "M": "In the third month after the Israelites had left Egypt—on the very first day of that month—they arrived in the wilderness of Sinai.",
      "T": "Three months to the day after Israel left Egypt, they arrived in the wilderness of Sinai."
    },
    "2": {
      "L": "For they had departed from Rephidim and came into the desert of Sinai and camped in the wilderness; and Israel camped there before the mountain.",
      "M": "They had traveled from Rephidim and arrived in the Sinai Desert. After setting up camp in the wilderness, Israel camped there at the foot of the mountain.",
      "T": "They had set out from Rephidim, crossed into the Sinai wilderness, and made camp there at the base of the mountain."
    },
    "3": {
      "L": "And Moses went up to God, and the LORD called to him from the mountain, saying, 'Thus you shall say to the house of Jacob, and tell to the children of Israel:'",
      "M": "Then Moses went up to God, and the LORD called to him from the mountain and said, 'This is what you are to say to the house of Jacob and to tell the Israelites:'",
      "T": "Moses climbed the mountain toward God, and the LORD called down to him: 'Here is what you must tell the house of Jacob — declare it to the people of Israel:'"
    },
    "4": {
      "L": "'You have seen what I did to the Egyptians, and how I carried you on eagles' wings and brought you to myself.'",
      "M": "'You yourselves have seen what I did to Egypt, and how I carried you on eagles' wings and brought you to myself.'",
      "T": "'You saw what I did to Egypt — how I lifted you like an eagle bearing its young on outstretched wings and brought you home to me.'"
    },
    "5": {
      "L": "'And now, if you will indeed obey my voice and keep my covenant, then you shall be my special possession from among all peoples, for all the earth is mine;'",
      "M": "'Now if you will truly obey my voice and keep my covenant, you will be my treasured possession out of all the nations, for the whole earth is mine;'",
      "T": "'Now then — if you will listen to my voice and keep my covenant, you will be my most precious treasure from among all the peoples of the earth. The whole earth is mine,'"
    },
    "6": {
      "L": "'and you shall be to me a kingdom of priests and a holy nation.' These are the words that you shall speak to the children of Israel.",
      "M": "'and you will be for me a kingdom of priests and a holy nation.' These are the words you are to speak to the Israelites.",
      "T": "'but you — you will be a nation of royal priests, a people set apart as sacred to me.' This is the message you are to deliver to Israel."
    },
    "7": {
      "L": "And Moses came and called for the elders of the people and set before their faces all these words which the LORD commanded him.",
      "M": "So Moses went back and summoned the elders of the people and set before them all the words the LORD had commanded him to say.",
      "T": "Moses returned to the camp, gathered the elders of the people, and laid before them everything the LORD had said."
    },
    "8": {
      "L": "And all the people answered together and said, 'All that the LORD has spoken we will do.' And Moses returned the words of the people to the LORD.",
      "M": "All the people responded together: 'We will do everything the LORD has said.' So Moses brought their answer back to the LORD.",
      "T": "The whole assembly responded as one: 'We will do everything the LORD has said.' Moses took their answer back to God."
    },
    "9": {
      "L": "And the LORD said to Moses, 'Behold, I am coming to you in a thick cloud, that the people may hear when I speak with you, and may also believe you forever.' And Moses told the words of the people to the LORD.",
      "M": "The LORD said to Moses, 'I am going to come to you in a thick cloud so that the people will hear me speaking with you and will always put their trust in you.' And Moses told the LORD what the people had said.",
      "T": "The LORD told Moses, 'I will come to you wrapped in thick cloud so the people can hear me speaking with you — and from then on they will always trust you.' Moses reported the people's reply to the LORD."
    },
    "10": {
      "L": "And the LORD said to Moses, 'Go to the people and sanctify them today and tomorrow, and let them wash their garments,'",
      "M": "The LORD said to Moses, 'Go to the people and consecrate them today and tomorrow. Have them wash their clothes,'",
      "T": "'Go back to the people,' the LORD told Moses. 'Consecrate them today and tomorrow; have them wash their clothes'"
    },
    "11": {
      "L": "'and be ready against the third day, for on the third day the LORD will come down upon Mount Sinai in the sight of all the people.'",
      "M": "'and have them ready for the third day. On that day the LORD will come down on Mount Sinai in the sight of all the people.'",
      "T": "'and let them be ready for the third day — for on that day the LORD will descend on Mount Sinai in full view of all the people.'"
    },
    "12": {
      "L": "And you shall set bounds for the people all around, saying, 'Take heed to yourselves that you do not go up into the mount or touch the border of it; whoever touches the mount shall surely be put to death.'",
      "M": "Set boundaries for the people around the mountain and tell them, 'Be careful not to go up the mountain or touch its base. Anyone who touches the mountain must be put to death.'",
      "T": "'Mark out a boundary around the mountain and warn the people: do not set foot on it or even touch its edge. Anyone who touches this mountain will be put to death.'"
    },
    "13": {
      "L": "'No hand shall touch him, but he shall surely be stoned or shot through; whether beast or man, it shall not live. When the ram's horn sounds long, they shall come up to the mountain.'",
      "M": "'No one is to lay a hand on him — he must be stoned or shot with arrows. Whether animal or person, he shall not live. Only when the ram's horn sounds a long blast may the people come up to the mountain.'",
      "T": "'No one may touch the offender directly — stone them or shoot them with arrows. No living thing, human or animal, may survive the trespass. Only when the ram's horn blasts long may the people ascend.'"
    },
    "14": {
      "L": "And Moses went down from the mount unto the people and sanctified the people; and they washed their garments.",
      "M": "Moses went down from the mountain to the people and consecrated them, and they washed their clothes.",
      "T": "Moses came down from the mountain and consecrated the people. They washed their clothes"
    },
    "15": {
      "L": "And he said unto the people, 'Be ready against the third day; do not come near a woman.'",
      "M": "and he told them, 'Prepare yourselves for the third day. Abstain from sexual relations.'",
      "T": "and told them, 'Be ready for the third day — and refrain from sexual relations until then.'"
    },
    "16": {
      "L": "And it came to pass on the third day in the morning that there were thunders and lightnings and a thick cloud upon the mount, and the voice of the trumpet exceeding loud; so that all the people that were in the camp trembled.",
      "M": "On the morning of the third day there was thunder and lightning, a thick cloud over the mountain, and a very loud blast of the trumpet. All the people in the camp trembled.",
      "T": "On the morning of the third day the mountain erupted: thunder and lightning, a dense cloud wrapped around the peak, and the blast of the ram's horn louder than anything they had ever heard. The whole camp shook with terror."
    },
    "17": {
      "L": "And Moses brought forth the people out of the camp to meet God, and they stood at the nether part of the mount.",
      "M": "Moses led the people out of the camp to meet with God, and they stood at the foot of the mountain.",
      "T": "Moses led the people out of the camp to stand before God, and they assembled at the base of the mountain."
    },
    "18": {
      "L": "And mount Sinai was altogether on a smoke, because the LORD descended upon it in fire; and the smoke thereof ascended as the smoke of a furnace, and the whole mount quaked greatly.",
      "M": "Mount Sinai was covered with smoke, because the LORD descended on it in fire. The smoke billowed up like smoke from a furnace, and the whole mountain trembled violently.",
      "T": "The whole of Mount Sinai was shrouded in smoke, for the LORD had descended on it in fire. Smoke poured upward like the smoke of a blast furnace, and the mountain shuddered to its roots."
    },
    "19": {
      "L": "And when the voice of the trumpet sounded long, and waxed louder and louder, Moses spake, and God answered him by a voice.",
      "M": "The sound of the trumpet grew louder and louder. Then Moses spoke and the voice of God answered him.",
      "T": "The trumpet blast grew longer and more intense. Moses spoke — and the voice of God thundered back in reply."
    },
    "20": {
      "L": "And the LORD came down upon mount Sinai, on the top of the mount; and the LORD called Moses up to the top of the mount; and Moses went up.",
      "M": "The LORD descended to the top of Mount Sinai and called Moses to the top of the mountain. Moses went up.",
      "T": "The LORD came down to the summit of Mount Sinai and summoned Moses to the top. Moses climbed up."
    },
    "21": {
      "L": "And the LORD said unto Moses, 'Go down, charge the people, lest they break through unto the LORD to gaze, and many of them perish.'",
      "M": "The LORD told Moses, 'Go down and warn the people not to force their way through to see the LORD, or many of them will die.'",
      "T": "'Go back down,' the LORD said, 'and warn the people. They must not push past the boundary to glimpse me — they will die.'"
    },
    "22": {
      "L": "And also let the priests that come near to the LORD sanctify themselves, lest the LORD break forth upon them.",
      "M": "Even the priests, who are allowed to approach the LORD, must consecrate themselves, or the LORD will break out against them.",
      "T": "Even the priests who regularly approach the LORD must consecrate themselves — otherwise the LORD will burst out against them."
    },
    "23": {
      "L": "And Moses said unto the LORD, 'The people cannot come up to mount Sinai, for thou chargedst us, saying, \"Set bounds about the mount and sanctify it.\"'",
      "M": "Moses said to the LORD, 'The people cannot come up to Mount Sinai. You yourself warned us: \"Set boundaries around the mountain and consecrate it.\"'",
      "T": "Moses answered the LORD, 'But the people cannot come up to Sinai — you yourself ordered the boundaries and the consecration of the mountain.'"
    },
    "24": {
      "L": "And the LORD said unto him, 'Away, get thee down, and thou shalt come up, thou and Aaron with thee; but let not the priests and the people break through to come up unto the LORD, lest he break forth upon them.'",
      "M": "The LORD replied, 'Go down, and come back up — you and Aaron. But do not allow the priests or the people to break through to come up to the LORD, or he will break out against them.'",
      "T": "'Go back down,' said the LORD, 'and bring Aaron with you when you return. But keep the priests and the people from breaking through — do not let them come up to me, or I will burst out against them.'"
    },
    "25": {
      "L": "So Moses went down unto the people and spake unto them.",
      "M": "So Moses went down and told the people.",
      "T": "Moses descended and delivered the warning to the people."
    }
  },
  "20": {
    "1": {
      "L": "And God spake all these words, saying:",
      "M": "And God spoke all these words:",
      "T": "Then God spoke all these words:"
    },
    "2": {
      "L": "'I am the LORD your God, who brought you out from the land of Egypt, from the house of bondage.'",
      "M": "'I am the LORD your God, who brought you out of Egypt, out of the land of slavery.'",
      "T": "'I am the LORD your God — the one who brought you out of Egypt, out of the slave house.'"
    },
    "3": {
      "L": "'You shall have no other gods before me.'",
      "M": "'You shall have no other gods besides me.'",
      "T": "'You will have no other gods alongside me.'"
    },
    "4": {
      "L": "'You shall not make for yourself a carved image, nor any likeness of what is in heaven above or what is on the earth beneath or what is in the waters under the earth.'",
      "M": "'You shall not make for yourself an idol in the form of anything in heaven above or on the earth below or in the waters beneath the earth.'",
      "T": "'You will make no idol for yourselves — no carved image in the shape of anything above in the sky, below on the earth, or in the waters under the earth.'"
    },
    "5": {
      "L": "'You shall not bow down to them nor serve them; for I the LORD your God am a jealous God, visiting the iniquity of the fathers upon the children to the third and fourth generation of those that hate me,'",
      "M": "'You shall not bow down to them or worship them; for I, the LORD your God, am a jealous God, punishing the children for the sin of the fathers to the third and fourth generation of those who hate me,'",
      "T": "'Do not bow to them or serve them. I, the LORD your God, am a jealous God — I hold the children accountable for their fathers' rejection of me, down to the third and fourth generation.'"
    },
    "6": {
      "L": "'but showing steadfast love to thousands of those who love me and keep my commandments.'",
      "M": "'but showing faithful love to thousands who love me and keep my commandments.'",
      "T": "'Yet I lavish covenant loyalty on thousands who love me and live by my commands.'"
    },
    "7": {
      "L": "'You shall not take the name of the LORD your God in vain; for the LORD will not hold guiltless him that taketh his name in vain.'",
      "M": "'You shall not misuse the name of the LORD your God, for the LORD will not hold anyone guiltless who misuses his name.'",
      "T": "'Do not invoke the name of the LORD your God for empty or deceitful purposes — the LORD will not acquit anyone who treats his name as worthless.'"
    },
    "8": {
      "L": "'Remember the Sabbath day, to keep it holy.'",
      "M": "'Remember the Sabbath day by keeping it holy.'",
      "T": "'Keep the Sabbath day holy — guard its sacred character.'"
    },
    "9": {
      "L": "'Six days you shall labor and do all your work,'",
      "M": "'For six days you shall labor and do all your work,'",
      "T": "'Six days you will work and do all your tasks,'"
    },
    "10": {
      "L": "'but the seventh day is a Sabbath to the LORD your God; in it you shall not do any work, you, nor your son, nor your daughter, your manservant, nor your maidservant, nor your cattle, nor your stranger that is within your gates;'",
      "M": "'but the seventh day is a Sabbath to the LORD your God. On it you shall not do any work — neither you, nor your son or daughter, nor your male or female servant, nor your animals, nor any foreigner residing in your towns.'",
      "T": "'but the seventh day belongs to the LORD your God as Sabbath rest. On that day no one does any work — not you, not your children, not your servants, not your animals, not even the immigrant staying in your community.'"
    },
    "11": {
      "L": "'For in six days the LORD made heaven and earth, the sea, and all that is in them, and rested on the seventh day; therefore the LORD blessed the Sabbath day and hallowed it.'",
      "M": "'For in six days the LORD made the heavens and the earth, the sea, and everything in them, but he rested on the seventh day. Therefore the LORD blessed the Sabbath day and made it holy.'",
      "T": "'The reason: in six days the LORD made the sky and the earth, the sea and everything in them — and on the seventh day he rested. So the LORD blessed the Sabbath and set it apart as holy.'"
    },
    "12": {
      "L": "'Honor your father and your mother, that your days may be long upon the land which the LORD your God gives you.'",
      "M": "'Honor your father and your mother, so that you may live long in the land the LORD your God is giving you.'",
      "T": "'Give weight and honor to your father and your mother — this is how you will have long life in the land the LORD your God is giving you.'"
    },
    "13": {
      "L": "'You shall not murder.'",
      "M": "'You shall not murder.'",
      "T": "'You will not murder.'"
    },
    "14": {
      "L": "'You shall not commit adultery.'",
      "M": "'You shall not commit adultery.'",
      "T": "'You will not commit adultery.'"
    },
    "15": {
      "L": "'You shall not steal.'",
      "M": "'You shall not steal.'",
      "T": "'You will not steal.'"
    },
    "16": {
      "L": "'You shall not bear false witness against your neighbor.'",
      "M": "'You shall not give false testimony against your neighbor.'",
      "T": "'You will not testify falsely against your neighbor.'"
    },
    "17": {
      "L": "'You shall not covet your neighbor's house; you shall not covet your neighbor's wife, nor his manservant, nor his maidservant, nor his ox, nor his donkey, nor any thing that is your neighbor's.'",
      "M": "'You shall not covet your neighbor's house. You shall not covet your neighbor's wife, his male or female servant, his ox or donkey, or anything that belongs to your neighbor.'",
      "T": "'Do not crave your neighbor's house. Do not crave your neighbor's spouse, servants, animals, or anything else that belongs to your neighbor.'"
    },
    "18": {
      "L": "And all the people saw the thunderings and the lightnings and the noise of the trumpet and the mountain smoking; and when the people saw it, they trembled and stood afar off.",
      "M": "When all the people saw the thunder and lightning and heard the trumpet and saw the mountain in smoke, they trembled with fear. They stayed at a distance",
      "T": "The people saw it all — the lightning, the thunderclaps, the blaring trumpet, the mountain wreathed in smoke — and they shook with terror. They kept their distance"
    },
    "19": {
      "L": "And they said unto Moses, 'Speak thou with us, and we will hear; but let not God speak with us, lest we die.'",
      "M": "and said to Moses, 'Speak to us yourself and we will listen. But do not have God speak to us or we will die.'",
      "T": "and begged Moses, 'You speak to us — we can bear that. But do not let God speak to us directly, or we will die.'"
    },
    "20": {
      "L": "And Moses said unto the people, 'Fear not; for God is come to prove you, and that his fear may be before your faces, that ye sin not.'",
      "M": "Moses said to the people, 'Do not be afraid. God has come to test you, so that the fear of God will be with you to keep you from sinning.'",
      "T": "Moses told them, 'Do not be afraid. God has come to test you — to plant reverence for him so deep in you that you will not sin.'"
    },
    "21": {
      "L": "And the people stood afar off, and Moses drew near unto the thick darkness where God was.",
      "M": "The people remained at a distance, while Moses approached the thick darkness where God was.",
      "T": "The people stayed at the edge of the distance. Moses alone walked forward into the thick darkness where God was."
    },
    "22": {
      "L": "And the LORD said unto Moses, 'Thus thou shalt say unto the children of Israel, Ye have seen that I have talked with you from heaven.'",
      "M": "The LORD said to Moses, 'Tell the Israelites this: You have seen for yourselves that I have spoken to you from heaven.'",
      "T": "The LORD told Moses, 'Tell the people of Israel: you have witnessed this with your own eyes — I spoke to you from heaven.'"
    },
    "23": {
      "L": "'You shall not make alongside me gods of silver, nor shall you make for yourselves gods of gold.'",
      "M": "'Do not make alongside me gods of silver or gods of gold for yourselves.'",
      "T": "'Do not set up gods of silver or gold to stand beside me — I will have no rivals.'"
    },
    "24": {
      "L": "'An altar of earth you shall make unto me and sacrifice thereon your burnt offerings and your peace offerings, your sheep and your oxen; in all places where I record my name I will come unto thee and I will bless thee.'",
      "M": "'Make for me an altar of earth and sacrifice on it your burnt offerings and fellowship offerings, your sheep and cattle. Wherever I cause my name to be honored, I will come to you and bless you.'",
      "T": "'Build me an altar of earth and offer on it your whole burnt offerings and fellowship offerings — your sheep and cattle. Wherever I choose to make my name honored, I will come and bless you.'"
    },
    "25": {
      "L": "'And if thou wilt make me an altar of stone, thou shalt not build it of hewn stone; for if thou lift up thy tool upon it, thou hast polluted it.'",
      "M": "'If you make an altar of stone for me, do not build it with dressed stones; for if you use a chisel on it, you desecrate it.'",
      "T": "'If you build me a stone altar, use unhewn stones — the moment your iron tool touches it, you desecrate it.'"
    },
    "26": {
      "L": "'Neither shalt thou go up by steps unto mine altar, that thy nakedness be not discovered thereon.'",
      "M": "'Do not approach my altar by steps, so that your nakedness will not be exposed on it.'",
      "T": "'Do not approach my altar by steps — your dignity before me must be preserved.'"
    }
  },
  "21": {
    "1": {
      "L": "Now these are the judgments which thou shalt set before them:",
      "M": "These are the ordinances you are to set before them:",
      "T": "These are the rulings you shall lay before the people:"
    },
    "2": {
      "L": "If thou buy a Hebrew servant, six years he shall serve; and in the seventh he shall go out free for nothing.",
      "M": "If you buy a Hebrew slave, he is to serve you for six years. But in the seventh year, he shall go free without paying anything.",
      "T": "When you acquire a Hebrew bondservant, he serves six years — in the seventh he goes free, owing nothing."
    },
    "3": {
      "L": "If he came in by himself, he shall go out by himself; if he were married, then his wife shall go out with him.",
      "M": "If he came as a single man, he shall leave as a single man; if he had a wife when he came, she shall leave with him.",
      "T": "If he came in unmarried, he leaves unmarried; if he had a wife when he came, she leaves with him."
    },
    "4": {
      "L": "If his master have given him a wife, and she have born him sons or daughters; the wife and her children shall be her master's, and he shall go out by himself.",
      "M": "If his master gave him a wife who bears him sons or daughters, the woman and her children belong to her master. The man must leave alone.",
      "T": "But if the master provided him a wife and she bore children, the wife and children remain the master's property — the man leaves alone."
    },
    "5": {
      "L": "And if the servant shall plainly say, 'I love my master, my wife, and my children; I will not go out free;'",
      "M": "But if the servant declares, 'I love my master and my wife and children and do not want to go free,'",
      "T": "But if the servant says plainly, 'I love my master and my wife and my children — I choose not to go free,'"
    },
    "6": {
      "L": "then his master shall bring him unto the judges; he shall also bring him to the door, or unto the door post; and his master shall bore his ear through with an awl; and he shall serve him for ever.",
      "M": "then his master must take him before the judges and bring him to the door or doorpost. There his master shall pierce his ear with an awl, and he will be his servant for life.",
      "T": "his master brings him before the judges and then to the door or doorpost, where he pierces the servant's ear with an awl. That man is a willing servant for life."
    },
    "7": {
      "L": "And if a man sell his daughter to be a maidservant, she shall not go out as the menservants do.",
      "M": "When a man sells his daughter as a servant, she is not to go free in the same way as male servants.",
      "T": "If a man sells his daughter as a household servant, she is not subject to the same release terms as male servants."
    },
    "8": {
      "L": "If she please not her master, who hath betrothed her to himself, then shall he let her be redeemed; to sell her unto a strange nation he shall have no power, seeing he hath dealt deceitfully with her.",
      "M": "If she does not please the master who has selected her for himself, he must allow her to be redeemed. He has no right to sell her to foreigners, because he has broken faith with her.",
      "T": "If she displeases the master who had designated her for himself, he must allow her family to buy her back. He may not sell her to foreigners — that would be a betrayal of the agreement."
    },
    "9": {
      "L": "And if he have betrothed her unto his son, he shall deal with her after the manner of daughters.",
      "M": "If he selects her for his son, he shall treat her as he would a daughter.",
      "T": "If he designates her for his son instead, he must treat her with the rights of a daughter."
    },
    "10": {
      "L": "If he take him another wife; her food, her raiment, and her duty of marriage, shall he not diminish.",
      "M": "If he marries another woman, he must not reduce the first woman's food, clothing, or marital rights.",
      "T": "If he takes an additional wife, he must not deprive the first of food, clothing, or conjugal rights."
    },
    "11": {
      "L": "And if he do not these three unto her, then shall she go out free without money.",
      "M": "If he fails to provide these three things for her, she shall go free without paying anything.",
      "T": "If he withholds any of these three things from her, she goes free — no buyback required."
    },
    "12": {
      "L": "He that smiteth a man so that he die shall be surely put to death.",
      "M": "Anyone who strikes someone and kills them must be put to death.",
      "T": "Whoever strikes a person dead must be put to death."
    },
    "13": {
      "L": "And if a man lie not in wait, but God deliver him into his hand; then I will appoint thee a place whither he shall flee.",
      "M": "However, if the killing was not intentional, but God allowed it to happen, that person is to flee to a place I will designate.",
      "T": "But if he did not plan the killing — if God allowed it to happen — I will set aside a place of refuge to which the killer may flee."
    },
    "14": {
      "L": "But if a man come presumptuously upon his neighbor to slay him with guile; thou shalt take him from mine altar, that he may die.",
      "M": "But if someone schemes and kills another person deliberately, take him away from my altar and put him to death.",
      "T": "But the premeditated killer — the one who planned and waited — you shall drag him away even from my altar and execute him."
    },
    "15": {
      "L": "And he that smiteth his father, or his mother, shall be surely put to death.",
      "M": "Anyone who strikes their father or mother must be put to death.",
      "T": "Strike your father or mother — you are to be put to death."
    },
    "16": {
      "L": "And he that stealeth a man, and selleth him, or if he be found in his hand, he shall surely be put to death.",
      "M": "Anyone who kidnaps someone and sells them — or who is caught in possession of them — must be put to death.",
      "T": "Kidnapping a person for sale is a capital crime. So is being caught with a person known to be kidnapped."
    },
    "17": {
      "L": "And he that curseth his father, or his mother, shall surely be put to death.",
      "M": "Anyone who curses their father or mother must be put to death.",
      "T": "Curse your father or your mother — you are to be put to death."
    },
    "18": {
      "L": "And if men strive together, and one smite another with a stone, or with his fist, and he die not, but keepeth his bed;",
      "M": "If people quarrel and one person hits another with a stone or with their fist and the injured person does not die but is confined to bed,",
      "T": "If two men fight and one injures the other with a stone or his fist — not fatally, but the injured man must take to his bed —"
    },
    "19": {
      "L": "If he rise again, and walk abroad upon his staff, then shall he that smote him be quit; only he shall pay for the loss of his time, and shall cause him to be thoroughly healed.",
      "M": "the one who struck the blow will not be held responsible if the injured person gets up and walks around outside with a staff. However, he must compensate the person for the time lost and see that he is completely healed.",
      "T": "but recovers and walks about with his staff — the one who struck him is not liable for death. He must compensate for lost time and pay all medical expenses."
    },
    "20": {
      "L": "And if a man smite his servant, or his maid, with a rod, and he die under his hand; he shall be surely punished.",
      "M": "Anyone who beats their male or female slave with a rod and the slave dies as a direct result shall be punished.",
      "T": "If a man beats his slave — male or female — with a rod and the slave dies from the blows, he must be punished."
    },
    "21": {
      "L": "Notwithstanding, if he continue a day or two, he shall not be punished; for he is his money.",
      "M": "But if the slave recovers after a day or two, no punishment is to be given, since the slave is the master's property.",
      "T": "However, if the slave lingers for a day or two before dying, the owner is not punished — the financial loss itself is a consequence."
    },
    "22": {
      "L": "If men strive, and hurt a woman with child, so that her fruit depart from her, and yet no mischief follow; he shall be surely fined, according as the woman's husband will lay upon him; and he shall pay as the judges determine.",
      "M": "If people are fighting and hit a pregnant woman so that she gives birth prematurely but there is no serious injury, the offender must be fined whatever the woman's husband demands and the court allows.",
      "T": "If brawling men cause a pregnant woman to go into early labor — and no lasting harm results — the offender pays whatever fine the woman's husband demands, subject to the court's ruling."
    },
    "23": {
      "L": "And if any mischief follow, then thou shalt give life for life,",
      "M": "But if there is serious injury, you are to take life for life,",
      "T": "But if there is lasting harm, the penalty matches the injury: life for life,"
    },
    "24": {
      "L": "eye for eye, tooth for tooth, hand for hand, foot for foot,",
      "M": "eye for eye, tooth for tooth, hand for hand, foot for foot,",
      "T": "eye for eye, tooth for tooth, hand for hand, foot for foot —"
    },
    "25": {
      "L": "burning for burning, wound for wound, stripe for stripe.",
      "M": "burn for burn, wound for wound, bruise for bruise.",
      "T": "burn answered with burn, wound with wound, bruise with bruise."
    },
    "26": {
      "L": "And if a man smite the eye of his servant, or the eye of his maid, that it perish; he shall let him go free for his eye's sake.",
      "M": "If a man hits his male or female slave in the eye and destroys it, he must let the slave go free as compensation for the eye.",
      "T": "If a master strikes his slave's eye and blinds it, he must set that slave free — the eye costs the master his servant."
    },
    "27": {
      "L": "And if he smite out his manservant's tooth, or his maidservant's tooth; he shall let him go free for his tooth's sake.",
      "M": "And if he knocks out the tooth of his male or female slave, he must let the slave go free as compensation for the tooth.",
      "T": "If a master knocks out his slave's tooth, that slave goes free — the tooth earns freedom."
    },
    "28": {
      "L": "If an ox gore a man or a woman that they die, then the ox shall be surely stoned, and his flesh shall not be eaten; but the owner of the ox shall be quit.",
      "M": "If a bull gores a man or woman to death, the bull must be stoned to death, and its meat must not be eaten. But the owner of the bull will not be held responsible.",
      "T": "If an ox gores a man or woman to death, the ox is stoned and its meat may not be eaten — but the owner bears no liability."
    },
    "29": {
      "L": "But if the ox were wont to push with his horn in time past, and it hath been testified to his owner, and he hath not kept him in, but that he hath killed a man or a woman; the ox shall be stoned, and his owner also shall be put to death.",
      "M": "But if the bull was known to gore in the past, and the owner was warned yet did not keep it penned in, and it kills someone — the bull must be stoned and the owner put to death.",
      "T": "But if the ox had a history of goring, the owner knew it, and still failed to restrain it — and it kills someone — both the ox is stoned and the owner is put to death."
    },
    "30": {
      "L": "If there be laid on him a sum of money, then he shall give for the ransom of his life whatsoever is laid upon him.",
      "M": "However, if payment is demanded as a ransom for his life, he may pay whatever is required to save himself.",
      "T": "If the court accepts a ransom in place of death, the owner pays whatever sum is set to redeem his life."
    },
    "31": {
      "L": "Whether he have gored a son, or have gored a daughter, according to this judgment shall it be done unto him.",
      "M": "This same rule applies if the bull gores a son or daughter.",
      "T": "The same law applies whether the victim was a son or a daughter."
    },
    "32": {
      "L": "If the ox shall push a manservant or a maidservant; he shall give unto their master thirty shekels of silver, and the ox shall be stoned.",
      "M": "If the bull gores a male or female slave, the owner must pay thirty shekels of silver to the slave's master, and the bull must be stoned.",
      "T": "If the ox gores a slave, the owner pays thirty shekels of silver to the slave's master, and the ox is stoned."
    },
    "33": {
      "L": "And if a man shall open a pit, or if a man shall dig a pit, and not cover it, and an ox or an ass fall therein;",
      "M": "If anyone uncovers a pit or digs one and fails to cover it, and an ox or donkey falls into it,",
      "T": "If a man uncovers or digs a pit and fails to cover it, and an ox or donkey falls in —"
    },
    "34": {
      "L": "The owner of the pit shall make it good, and give money unto the owner of them; and the dead beast shall be his.",
      "M": "the one who opened the pit must pay the owner for the loss and take the dead animal for himself.",
      "T": "the pit's owner must make good the loss — pay the animal's owner and keep the carcass."
    },
    "35": {
      "L": "And if one man's ox hurt another's that he die; then they shall sell the live ox, and divide the money of it; and the dead ox also they shall divide.",
      "M": "If anyone's bull injures another person's bull and it dies, the owners are to sell the live bull and divide both the proceeds and the dead animal equally.",
      "T": "If one man's ox injures another man's ox and it dies, they sell the living ox and split the money — and they split the dead ox as well."
    },
    "36": {
      "L": "Or if it be known that the ox hath used to push in time past, and his owner hath not kept him in; he shall surely pay ox for ox; and the dead shall be his own.",
      "M": "But if it was known that the bull was in the habit of goring, and the owner failed to keep it penned up, he must replace the animal with a live one and keep the carcass.",
      "T": "But if the ox was a known gorer and the owner never restrained it, he must replace the animal with a live one and keep the dead one."
    }
  },
  "22": {
    "1": {
      "L": "If a man shall steal an ox, or a sheep, and kill it, or sell it; he shall restore five oxen for an ox, and four sheep for a sheep.",
      "M": "If a man steals an ox or a sheep and slaughters it or sells it, he must pay back five head of cattle for the ox and four sheep for the sheep.",
      "T": "Steal and slaughter or sell an ox — repay five oxen. Steal and slaughter or sell a sheep — repay four sheep."
    },
    "2": {
      "L": "If a thief be found breaking up, and be smitten that he die, there shall no blood be shed for him.",
      "M": "If a thief is caught breaking in at night and is struck and killed, the defender is not guilty of bloodshed.",
      "T": "If a thief breaks in at night and is killed in the act, there is no blood guilt on the homeowner."
    },
    "3": {
      "L": "If the sun be risen upon him, there shall be blood shed for him; for he should make full restitution; if he have nothing, then he shall be sold for his theft.",
      "M": "But if it happens after sunrise, the defender is guilty of bloodshed. The thief must make full restitution. If he has nothing, he must be sold to pay for what he stole.",
      "T": "But if the break-in occurs in daylight and the thief is killed, the killer is guilty. The thief must make full restitution; if he cannot, he is sold to cover his debt."
    },
    "4": {
      "L": "If the theft be certainly found in his hand alive, whether it be ox, or ass, or sheep; he shall restore double.",
      "M": "If the stolen animal is found alive in his possession — whether an ox, donkey, or sheep — he must pay back double.",
      "T": "If the stolen animal is found alive in his hands — ox, donkey, or sheep — he must repay double."
    },
    "5": {
      "L": "If a man shall cause a field or vineyard to be eaten, and shall put in his beast, and shall feed in another man's field; of the best of his own field, and of the best of his own vineyard, shall he make restitution.",
      "M": "If anyone grazes their livestock in a field or vineyard and lets the animals stray and graze in someone else's field, restitution must be made from the best of their own field or vineyard.",
      "T": "If a man's animal strays and eats another's crops, the owner must make it right from the best of his own field or vineyard."
    },
    "6": {
      "L": "If fire break out, and catch in thorns, so that the stacks of corn, or the standing corn, or the field, be consumed therewith; he that kindled the fire shall surely make restitution.",
      "M": "If a fire breaks out and spreads into thornbushes so that it burns up shocks of grain or standing grain or the whole field, the one who started the fire must make full restitution.",
      "T": "If fire gets out of control and burns another man's grain stacks, standing crops, or fields, the one who set the fire must make full restitution."
    },
    "7": {
      "L": "If a man shall deliver unto his neighbor money or stuff to keep, and it be stolen out of the man's house; if the thief be found, let him pay double.",
      "M": "If anyone gives a neighbor money or goods for safekeeping and they are stolen from the neighbor's house, the thief, if caught, must pay back double.",
      "T": "If a man entrusts money or valuables to a neighbor for safekeeping and they are stolen from that neighbor's house — if the thief is caught, he repays double."
    },
    "8": {
      "L": "If the thief be not found, then the master of the house shall be brought unto the judges, to see whether he have put his hand unto his neighbor's goods.",
      "M": "But if the thief is not found, the owner of the house must appear before God to declare that he has not taken the other person's property.",
      "T": "But if the thief is never caught, the neighbor must appear before God and swear he did not take the items himself."
    },
    "9": {
      "L": "For all manner of trespass, whether it be for ox, for ass, for sheep, for raiment, or for any manner of lost thing, which another challengeth to be his, the cause of both parties shall come before the judges; and whom the judges shall condemn, he shall pay double unto his neighbor.",
      "M": "In any case of disputed ownership — whether involving an ox, a donkey, a sheep, a garment, or any other lost property — both parties are to bring their cases before God. The one whom God declares guilty must pay back double to the other.",
      "T": "For every disputed claim — ox, donkey, sheep, clothing, or any lost item — both sides bring the case before God. The one God finds guilty pays the other double."
    },
    "10": {
      "L": "If a man deliver unto his neighbor an ass, or an ox, or a sheep, or any beast, to keep; and it die, or be hurt, or driven away, no man seeing it:",
      "M": "If anyone gives a neighbor a donkey, ox, sheep, or any animal to look after, and it dies, is injured, or is driven off without witnesses,",
      "T": "If a man leaves his neighbor in charge of a donkey, ox, sheep, or any animal, and the animal dies, is injured, or disappears without any witness —"
    },
    "11": {
      "L": "Then shall an oath of the LORD be between them both, that he hath not put his hand unto his neighbor's goods; and the owner of it shall accept thereof, and he shall not make it good.",
      "M": "the issue between them shall be settled by an oath before the LORD that the neighbor did not take the other person's property. The owner must accept this, and no restitution is required.",
      "T": "the matter is settled by an oath before the LORD: the caretaker swears he did not take the animal. The owner must accept the oath, and no restitution is required."
    },
    "12": {
      "L": "And if it be stolen from him, he shall make restitution unto the owner thereof.",
      "M": "But if the animal was stolen from the neighbor, he must make restitution to the owner.",
      "T": "But if the animal was stolen on his watch, he must make good the loss."
    },
    "13": {
      "L": "If it be torn in pieces, then let him bring it for witness, and he shall not make good that which was torn.",
      "M": "If it was torn by a wild animal, the neighbor must bring the remains as evidence; he is not required to make restitution for the torn animal.",
      "T": "If a wild animal killed it, the caretaker brings the carcass as proof — he owes no restitution for what a predator took."
    },
    "14": {
      "L": "And if a man borrow ought of his neighbor, and it be hurt, or die, the owner thereof being not with it, he shall surely make it good.",
      "M": "If anyone borrows an animal from a neighbor and it is injured or dies while the owner is not present, the borrower must make full restitution.",
      "T": "If a man borrows an animal and it is injured or dies when the owner is not present, the borrower must make full restitution."
    },
    "15": {
      "L": "But if the owner thereof be with it, he shall not make it good; if it be an hired thing, it came for his hire.",
      "M": "But if the owner was present, the borrower need not make restitution. If it was a hired animal, the loss is covered by the rental fee.",
      "T": "But if the owner was there, no restitution is required. If it was a hired animal, the hiring fee covers the risk."
    },
    "16": {
      "L": "And if a man entice a maid that is not betrothed, and lie with her, he shall surely endow her and take her to wife.",
      "M": "If a man seduces a virgin who is not pledged to be married and sleeps with her, he must pay the bride-price, and she shall be his wife.",
      "T": "If a man seduces an unbetrothed virgin and sleeps with her, he must pay the bride-price and take her as his wife."
    },
    "17": {
      "L": "If her father utterly refuse to give her unto him, he shall pay money according to the dowry of virgins.",
      "M": "If her father absolutely refuses to give her to him, he must still pay the bride-price for virgins.",
      "T": "If her father refuses, the man must still pay the standard bride-price for a virgin."
    },
    "18": {
      "L": "Thou shalt not suffer a witch to live.",
      "M": "Do not allow a sorceress to live.",
      "T": "You shall not let a sorceress live."
    },
    "19": {
      "L": "Whosoever lieth with a beast shall surely be put to death.",
      "M": "Anyone who has sexual relations with an animal must be put to death.",
      "T": "Whoever lies with an animal must be put to death."
    },
    "20": {
      "L": "He that sacrificeth unto any god, save unto the LORD only, he shall be utterly destroyed.",
      "M": "Anyone who sacrifices to any god other than the LORD must be destroyed.",
      "T": "Whoever offers sacrifice to any god but the LORD alone must be devoted to destruction."
    },
    "21": {
      "L": "Thou shalt neither vex a stranger, nor oppress him; for ye were strangers in the land of Egypt.",
      "M": "Do not mistreat or oppress a foreigner, for you were foreigners in Egypt.",
      "T": "Do not wrong or oppress the immigrant among you — remember, you were immigrants in Egypt."
    },
    "22": {
      "L": "Ye shall not afflict any widow, or fatherless child.",
      "M": "Do not take advantage of a widow or an orphan.",
      "T": "Do not oppress any widow or orphaned child."
    },
    "23": {
      "L": "If thou afflict them in any wise, and they cry at all unto me, I will surely hear their cry;",
      "M": "If you do and they cry out to me, I will certainly hear their cry.",
      "T": "If you do oppress them and they cry out to me, I will hear — I will hear every cry."
    },
    "24": {
      "L": "And my wrath shall wax hot, and I will kill you with the sword; and your wives shall be widows, and your children fatherless.",
      "M": "My anger will be aroused, and I will kill you with the sword; your wives will become widows and your children fatherless.",
      "T": "My anger will blaze — I will put you to the sword, and your wives will become the very widows you refused to protect, your children the orphans you would not pity."
    },
    "25": {
      "L": "If thou lend money to any of my people that is poor by thee, thou shalt not be to him as an usurer, neither shalt thou lay upon him usury.",
      "M": "If you lend money to one of my people among you who is needy, do not be like a moneylender to him; charge him no interest.",
      "T": "When you lend money to one of my people who is poor, do not play the moneylender — charge no interest."
    },
    "26": {
      "L": "If thou at all take thy neighbor's raiment to pledge, thou shalt deliver it unto him by that the sun goeth down;",
      "M": "If you take your neighbor's cloak as a pledge, return it to him by sunset,",
      "T": "If you ever take a man's cloak as a pledge, return it before sundown —"
    },
    "27": {
      "L": "for that is his covering only, it is his raiment for his skin; wherein shall he sleep? and it shall come to pass, when he crieth unto me, that I will hear; for I am gracious.",
      "M": "because that cloak is the only covering he has for his body. What else will he sleep in? When he cries out to me, I will hear, for I am compassionate.",
      "T": "for that cloak may be all he has to sleep in. When he cries out to me, I will hear — because I am a God of compassion."
    },
    "28": {
      "L": "Thou shalt not revile the gods, nor curse the ruler of thy people.",
      "M": "Do not blaspheme God or curse the ruler of your people.",
      "T": "Do not speak evil of God, and do not curse the ruler of your people."
    },
    "29": {
      "L": "Thou shalt not delay to offer the first of thy ripe fruits, and of thy liquors; the firstborn of thy sons shalt thou give unto me.",
      "M": "Do not hold back offerings from your harvest or your vintage. Give me the firstborn of your sons.",
      "T": "Do not hold back your grain and wine offerings. Give me the firstborn of your sons."
    },
    "30": {
      "L": "Likewise shalt thou do with thine oxen, and with thy sheep; seven days it shall be with his dam; on the eighth day thou shalt give it me.",
      "M": "Do the same with your cattle and your sheep. Let them stay with their mothers for seven days, but give them to me on the eighth day.",
      "T": "Do the same with your cattle and sheep — they stay with their mothers seven days; on the eighth day they belong to me."
    },
    "31": {
      "L": "And ye shall be holy men unto me; neither shall ye eat any flesh that is torn of beasts in the field; ye shall cast it to the dogs.",
      "M": "You are to be my holy people. So do not eat the meat of an animal torn by wild beasts; throw it to the dogs.",
      "T": "You are a people set apart for me — holy. Do not eat flesh torn by predators in the field; throw it to the dogs."
    }
  },
  "23": {
    "1": {
      "L": "Thou shalt not raise a false report; put not thine hand with the wicked to be an unrighteous witness.",
      "M": "Do not spread false reports. Do not help a guilty person by being a dishonest witness.",
      "T": "Do not pass along false rumors. Do not side with the guilty by becoming a corrupt witness."
    },
    "2": {
      "L": "Thou shalt not follow a multitude to do evil; neither shalt thou speak in a cause to decline after many to wrest judgment.",
      "M": "Do not follow the crowd in doing wrong. When you give testimony in a lawsuit, do not pervert justice by siding with the crowd.",
      "T": "Do not go along with the crowd when it moves toward evil. When you testify in court, do not twist justice by deferring to popular opinion."
    },
    "3": {
      "L": "Neither shalt thou countenance a poor man in his cause.",
      "M": "Do not show favoritism to a poor person in a lawsuit.",
      "T": "Do not show favoritism to the poor in a legal dispute either."
    },
    "4": {
      "L": "If thou meet thine enemy's ox or his ass going astray, thou shalt surely bring it back to him again.",
      "M": "If you come across your enemy's ox or donkey wandering off, be sure to return it.",
      "T": "If you find your enemy's ox or donkey wandering, bring it back to him."
    },
    "5": {
      "L": "If thou see the ass of him that hateth thee lying under his burden, and wouldest forbear to help him, thou shalt surely help with him.",
      "M": "If you see the donkey of someone who hates you fallen down under its load, do not leave it there; be sure you help them with it.",
      "T": "If the donkey of a man who hates you has collapsed under its load, do not walk past — stop and help him lift it."
    },
    "6": {
      "L": "Thou shalt not wrest the judgment of thy poor in his cause.",
      "M": "Do not deny justice to your poor people in their lawsuits.",
      "T": "Do not twist justice when a poor man brings his case."
    },
    "7": {
      "L": "Keep thee far from a false matter; and the innocent and righteous slay thou not; for I will not justify the wicked.",
      "M": "Have nothing to do with a false charge and do not put an innocent or honest person to death, for I will not acquit the guilty.",
      "T": "Stay far from false charges. Do not have a hand in putting an innocent or righteous person to death — I will not acquit the wicked."
    },
    "8": {
      "L": "And thou shalt take no gift; for the gift blindeth the wise, and perverteth the words of the righteous.",
      "M": "Do not accept a bribe, for a bribe blinds those who see and twists the words of the innocent.",
      "T": "Take no bribe. Bribes blind the clear-eyed and corrupt the speech of the honest."
    },
    "9": {
      "L": "Also thou shalt not oppress a stranger; for ye know the heart of a stranger, seeing ye were strangers in the land of Egypt.",
      "M": "Do not oppress a foreigner; you yourselves know how it feels to be foreigners, because you were foreigners in Egypt.",
      "T": "Do not oppress the immigrant among you. You know what it is to be a stranger — you were strangers in Egypt."
    },
    "10": {
      "L": "And six years thou shalt sow thy land, and shalt gather in the fruits thereof;",
      "M": "For six years you are to sow your fields and harvest the crops,",
      "T": "Six years you sow your land and gather its produce,"
    },
    "11": {
      "L": "but the seventh year thou shalt let it rest and lie still; that the poor of thy people may eat; and what they leave the beasts of the field shall eat. In like manner thou shalt deal with thy vineyard, and with thy oliveyard.",
      "M": "but during the seventh year let the land lie unplowed and unused. Then the poor among your people may get food from it, and the wild animals may eat what they leave. Do the same with your vineyard and your olive grove.",
      "T": "but in the seventh year let the land rest — leave it unworked. The poor may take what grows on its own; what they leave, the wild animals may eat. Do the same with your vineyards and olive groves."
    },
    "12": {
      "L": "Six days thou shalt do thy work, and on the seventh day thou shalt rest; that thine ox and thine ass may rest, and the son of thy handmaid, and the stranger, may be refreshed.",
      "M": "Do your work in six days. On the seventh day rest, so that your ox and donkey can rest, and the slave born in your household and the foreigner can be refreshed.",
      "T": "Work for six days. On the seventh, rest — so your ox and donkey can rest, and the household slave and the immigrant among you can draw breath."
    },
    "13": {
      "L": "And in all things that I have said unto you be circumspect; and make no mention of the name of other gods, neither let it be heard out of thy mouth.",
      "M": "Be careful to do everything I have said to you. Do not invoke the names of other gods; do not let them be heard on your lips.",
      "T": "Observe everything I have commanded you. Do not even speak the names of other gods — let them not be heard from your lips."
    },
    "14": {
      "L": "Three times thou shalt keep a feast unto me in the year.",
      "M": "Three times a year you are to celebrate a festival in my honor.",
      "T": "Three times a year you shall hold a festival for me."
    },
    "15": {
      "L": "Thou shalt keep the feast of unleavened bread; thou shalt eat unleavened bread seven days, as I commanded thee, in the time appointed of the month Abib; for in it thou camest out from Egypt; and none shall appear before me empty.",
      "M": "Celebrate the Festival of Unleavened Bread; for seven days eat bread made without yeast, as I commanded you. Do this at the appointed time in the month of Abib, for that is when you came out of Egypt. No one is to appear before me empty-handed.",
      "T": "Observe the Feast of Unleavened Bread — seven days of unleavened bread, as I commanded, at the appointed time in the month of Abib, when you came out of Egypt. When you appear before me, come with an offering."
    },
    "16": {
      "L": "And the feast of harvest, the firstfruits of thy labors, which thou hast sown in the field; and the feast of ingathering, which is in the end of the year, when thou hast gathered in thy labors out of the field.",
      "M": "Celebrate the Festival of Harvest with the firstfruits of the crops you sow in your field. And celebrate the Festival of Ingathering at the end of the year, when you gather in your crops from the field.",
      "T": "Celebrate the Feast of Harvest when you bring the first yield of your fieldwork. Celebrate the Feast of Ingathering at year's end, when you have brought in everything from your fields."
    },
    "17": {
      "L": "Three times in the year all thy males shall appear before the Lord GOD.",
      "M": "Three times a year all your men are to appear before the Lord, the LORD.",
      "T": "Three times a year every male among you shall present himself before the LORD."
    },
    "18": {
      "L": "Thou shalt not offer the blood of my sacrifice with leavened bread; neither shall the fat of my sacrifice remain until the morning.",
      "M": "Do not offer the blood of a sacrifice to me along with anything containing yeast. The fat of my festival offerings must not be kept until morning.",
      "T": "Do not offer the blood of my sacrifice alongside leavened bread. Do not let the fat from my festival remain until morning."
    },
    "19": {
      "L": "The first of the firstfruits of thy land thou shalt bring into the house of the LORD thy God. Thou shalt not seethe a kid in his mother's milk.",
      "M": "Bring the best of the firstfruits of your soil to the house of the LORD your God. Do not cook a young goat in its mother's milk.",
      "T": "Bring the very best of your firstfruits to the house of the LORD your God. Do not boil a kid in its mother's milk."
    },
    "20": {
      "L": "Behold, I send an Angel before thee, to keep thee in the way, and to bring thee into the place which I have prepared.",
      "M": "See, I am sending an angel ahead of you to guard you along the way and to bring you to the place I have prepared.",
      "T": "Watch: I am sending my angel ahead of you to guard you on the journey and bring you to the place I have prepared."
    },
    "21": {
      "L": "Beware of him, and obey his voice, provoke him not; for he will not pardon your transgressions; for my name is in him.",
      "M": "Pay attention to him and listen to what he says. Do not rebel against him; he will not forgive your rebellion, since my name is in him.",
      "T": "Listen to him carefully and do what he says. Do not defy him — he will not overlook your rebellion, for my own authority is within him."
    },
    "22": {
      "L": "But if thou shalt indeed obey his voice, and do all that I speak; then I will be an enemy unto thine enemies, and an adversary unto thine adversaries.",
      "M": "If you listen carefully to what he says and do all that I say, I will be an enemy to your enemies and will oppose those who oppose you.",
      "T": "But if you truly listen to him and do everything I say, I myself will be the enemy of your enemies, the adversary of those who stand against you."
    },
    "23": {
      "L": "For mine Angel shall go before thee, and bring thee in unto the Amorites, and the Hittites, and the Perizzites, and the Canaanites, the Hivites, and the Jebusites; and I will cut them off.",
      "M": "My angel will go ahead of you and bring you into the land of the Amorites, Hittites, Perizzites, Canaanites, Hivites and Jebusites, and I will wipe them out.",
      "T": "My angel will lead you into the land of the Amorites, Hittites, Perizzites, Canaanites, Hivites, and Jebusites — and I will destroy them."
    },
    "24": {
      "L": "Thou shalt not bow down to their gods, nor serve them, nor do after their works; but thou shalt utterly overthrow them, and quite break down their images.",
      "M": "Do not bow down before their gods or worship them or follow their practices. You must demolish them and break their sacred stones to pieces.",
      "T": "Do not bow to their gods, do not serve them, do not imitate their practices. Tear their altars down and shatter their sacred pillars."
    },
    "25": {
      "L": "And ye shall serve the LORD your God, and he shall bless thy bread, and thy water; and I will take sickness away from the midst of thee.",
      "M": "Worship the LORD your God, and his blessing will be on your food and water. I will take away sickness from among you,",
      "T": "Serve the LORD your God — he will bless your food and water and drive sickness far from your midst."
    },
    "26": {
      "L": "There shall nothing cast their young, nor be barren, in thy land; the number of thy days I will fulfil.",
      "M": "and none will miscarry or be barren in your land. I will give you a full span of life.",
      "T": "No woman among you will miscarry or remain barren. I will fill out the full measure of your days."
    },
    "27": {
      "L": "I will send my fear before thee, and will destroy all the people to whom thou shalt come, and I will make all thine enemies turn their backs unto thee.",
      "M": "I will send my terror ahead of you and throw into confusion every nation you encounter. I will make all your enemies turn and run.",
      "T": "I will send my dread ahead of you, throwing every nation you approach into confusion. I will make your enemies turn their backs and flee."
    },
    "28": {
      "L": "And I will send hornets before thee, which shall drive out the Hivite, the Canaanite, and the Hittite, from before thee.",
      "M": "I will send the hornet ahead of you to drive the Hivites, Canaanites and Hittites out of your way.",
      "T": "I will send a swarm of hornets ahead of you to drive out the Hivites, Canaanites, and Hittites before you."
    },
    "29": {
      "L": "I will not drive them out from before thee in one year; lest the land become desolate, and the beast of the field multiply against thee.",
      "M": "But I will not drive them out in a single year, because the land would become desolate and the wild animals too numerous for you.",
      "T": "I will not clear them out in a single year — the land would become wilderness and wild animals would multiply against you."
    },
    "30": {
      "L": "By little and little I will drive them out from before thee, until thou be increased, and inherit the land.",
      "M": "Little by little I will drive them out before you, until you have grown enough to take possession of the land.",
      "T": "Gradually I will drive them out before you, as your numbers grow and you are able to settle the land."
    },
    "31": {
      "L": "And I will set thy bounds from the Red sea even unto the sea of the Philistines, and from the desert unto the river; for I will deliver the inhabitants of the land into your hand; and thou shalt drive them out before thee.",
      "M": "I will establish your borders from the Red Sea to the Mediterranean Sea, and from the desert to the Euphrates River. I will hand over to you the people who live in the land, and you will drive them out before you.",
      "T": "I will set your territory from the Red Sea to the sea of the Philistines, and from the desert to the Euphrates. I will deliver the people of the land into your hands, and you will drive them out before you."
    },
    "32": {
      "L": "Thou shalt make no covenant with them, nor with their gods.",
      "M": "Do not make any covenant with them or with their gods.",
      "T": "You shall make no treaty with them and no alliance with their gods."
    },
    "33": {
      "L": "They shall not dwell in thy land, lest they make thee sin against me; for if thou serve their gods, it will surely be a snare unto thee.",
      "M": "Do not let them live in your land, or they will cause you to sin against me. If you serve their gods, it will certainly be a trap for you.",
      "T": "Do not let them settle among you — they will draw you into sin against me. If you worship their gods, that worship will become a trap that catches you."
    }
  },
  "24": {
    "1": {
      "L": "And he said unto Moses, 'Come up unto the LORD, thou, and Aaron, Nadab, and Abihu, and seventy of the elders of Israel; and worship ye afar off.'",
      "M": "Then the LORD said to Moses, 'Come up to the LORD, you and Aaron, Nadab and Abihu, and seventy of the elders of Israel. You are to worship at a distance,'",
      "T": "Then the LORD said to Moses, 'Come up to me — you and Aaron, Nadab and Abihu, and seventy of Israel's elders. You will worship at a distance.'"
    },
    "2": {
      "L": "'And Moses alone shall come near the LORD; but they shall not come nigh; neither shall the people go up with him.'",
      "M": "'but Moses alone is to approach the LORD; the others must not come near. And the people may not come up with him.'",
      "T": "'Moses alone approaches the LORD. The others must not come near, and the people must not ascend the mountain with him.'"
    },
    "3": {
      "L": "And Moses came and told the people all the words of the LORD, and all the judgments; and all the people answered with one voice, and said, 'All the words which the LORD hath said will we do.'",
      "M": "When Moses went and told the people all the LORD's words and laws, they responded with one voice: 'Everything the LORD has said we will do.'",
      "T": "Moses went back and told the people everything the LORD had said — all the words and all the rulings. The whole assembly answered as one: 'We will do everything the LORD has said.'"
    },
    "4": {
      "L": "And Moses wrote all the words of the LORD, and rose up early in the morning, and builded an altar under the hill, and twelve pillars, according to the twelve tribes of Israel.",
      "M": "Moses then wrote down everything the LORD had said. He got up early the next morning and built an altar at the foot of the mountain and set up twelve stone pillars representing the twelve tribes of Israel.",
      "T": "Moses wrote down all the LORD's words. Early the next morning he built an altar at the foot of the mountain and erected twelve pillars — one for each of the twelve tribes of Israel."
    },
    "5": {
      "L": "And he sent young men of the children of Israel, which offered burnt offerings, and sacrificed peace offerings of oxen unto the LORD.",
      "M": "Then he sent young Israelite men, and they offered burnt offerings and sacrificed young bulls as fellowship offerings to the LORD.",
      "T": "He sent young Israelite men to offer whole burnt offerings and to sacrifice bulls as fellowship offerings to the LORD."
    },
    "6": {
      "L": "And Moses took half of the blood, and put it in basons; and half of the blood he sprinkled on the altar.",
      "M": "Moses took half of the blood and put it in bowls, and the other half he splashed against the altar.",
      "T": "Moses collected half the blood in bowls and dashed the other half against the altar."
    },
    "7": {
      "L": "And he took the book of the covenant, and read in the audience of the people; and they said, 'All that the LORD hath said will we do, and be obedient.'",
      "M": "Then he took the Book of the Covenant and read it to the people. They responded, 'We will do everything the LORD has said; we will obey.'",
      "T": "Then he took the Book of the Covenant and read it aloud to all the people. They said, 'We will do everything the LORD has said, and we will obey.'"
    },
    "8": {
      "L": "And Moses took the blood, and sprinkled it on the people, and said, 'Behold the blood of the covenant, which the LORD hath made with you concerning all these words.'",
      "M": "Moses then took the blood, sprinkled it on the people and said, 'This is the blood of the covenant that the LORD has made with you in accordance with all these words.'",
      "T": "Moses took the blood and sprinkled it on the people, declaring: 'Behold — the blood of the covenant. The LORD has sealed his bond with you in all these words.'"
    },
    "9": {
      "L": "Then went up Moses, and Aaron, Nadab, and Abihu, and seventy of the elders of Israel;",
      "M": "Moses and Aaron, Nadab and Abihu, and the seventy elders of Israel went up",
      "T": "Then Moses, Aaron, Nadab, Abihu, and seventy elders of Israel climbed the mountain."
    },
    "10": {
      "L": "And they saw the God of Israel; and there was under his feet as it were a paved work of a sapphire stone, and as it were the body of heaven in his clearness.",
      "M": "and they saw the God of Israel. Under his feet was something like a pavement made of lapis lazuli, as bright and clear as the sky itself.",
      "T": "and they saw the God of Israel. Under his feet was what seemed like a floor of hammered sapphire — brilliant as the sky itself at noon."
    },
    "11": {
      "L": "And upon the nobles of the children of Israel he laid not his hand; also they saw God, and did eat and drink.",
      "M": "But God did not raise his hand against these leaders of the Israelites; they saw God, and they ate and drank.",
      "T": "God did not strike the leaders of Israel. They gazed on God — and then they ate and drank."
    },
    "12": {
      "L": "And the LORD said unto Moses, 'Come up to me into the mount, and be there; and I will give thee tables of stone, and a law, and commandments which I have written; that thou mayest teach them.'",
      "M": "The LORD said to Moses, 'Come up to me on the mountain and stay here, and I will give you the tablets of stone with the law and commandments I have written for their instruction.'",
      "T": "The LORD said to Moses, 'Come up to me on the mountain and wait there. I will give you the stone tablets with the law and commands I have inscribed — for teaching the people.'"
    },
    "13": {
      "L": "And Moses rose up, and his minister Joshua; and Moses went up into the mount of God.",
      "M": "Then Moses set out with Joshua his aide, and Moses went up on the mountain of God.",
      "T": "Moses set out with his attendant Joshua, and Moses ascended the mountain of God."
    },
    "14": {
      "L": "And he said unto the elders, 'Tarry ye here for us, until we come again unto you; and, behold, Aaron and Hur are with you; if any man have any matters to do, let him come unto them.'",
      "M": "He told the elders, 'Wait here for us until we come back to you. Aaron and Hur are with you, and anyone involved in a dispute can go to them.'",
      "T": "Moses told the elders, 'Wait here for us until we return. Aaron and Hur are with you — if anyone has a dispute to settle, bring it to them.'"
    },
    "15": {
      "L": "And Moses went up into the mount, and a cloud covered the mount.",
      "M": "When Moses went up on the mountain, the cloud covered it,",
      "T": "Moses went up, and cloud enveloped the mountain."
    },
    "16": {
      "L": "And the glory of the LORD abode upon mount Sinai, and the cloud covered it six days; and the seventh day he called unto Moses out of the midst of the cloud.",
      "M": "and the glory of the LORD settled on Mount Sinai. For six days the cloud covered the mountain, and on the seventh day the LORD called to Moses from within the cloud.",
      "T": "The glory of the LORD rested on Mount Sinai. The cloud covered it for six days — then on the seventh day the LORD called Moses from within the cloud."
    },
    "17": {
      "L": "And the sight of the glory of the LORD was like devouring fire on the top of the mount in the eyes of the children of Israel.",
      "M": "To the Israelites the glory of the LORD looked like a consuming fire on top of the mountain.",
      "T": "To the eyes of Israel watching below, the glory of the LORD blazed like devouring fire on the mountaintop."
    },
    "18": {
      "L": "And Moses went into the midst of the cloud, and gat him up into the mount; and Moses was in the mount forty days and forty nights.",
      "M": "Then Moses entered the cloud as he went on up the mountain. And he stayed on the mountain forty days and forty nights.",
      "T": "Moses walked into the cloud and climbed higher on the mountain. He remained on the mountain forty days and forty nights."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'exodus')
        merge_tier(existing, EXODUS, tier_key)
        save(tier_dir, 'exodus', existing)
    print('Exodus 19–24 written.')

if __name__ == '__main__':
    main()
