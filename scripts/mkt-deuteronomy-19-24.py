"""
MKT Deuteronomy chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-deuteronomy-19-24.py

Covers: cities of refuge and the manslaughter/murder distinction (ch. 19); witnesses and
false-testimony law (ch. 19); landmark law (ch. 19); holy-war procedure including priestly
oration and the exemptions from service (ch. 20); the heifer ritual for unexplained murder
(ch. 21); laws on captive women, firstborn rights, and the rebellious son (ch. 21);
hanging on a tree (ch. 21); lost-property and mixed-species laws (ch. 22); marriage and
sexual-purity laws (ch. 22); assembly exclusions and camp holiness (ch. 23); runaway slaves,
cult prostitution, lending at interest, vows, and gleaning-from-neighbor laws (ch. 23);
divorce certificate and remarriage prohibition (ch. 24); exemptions for the newly married,
pledge laws, kidnapping, wages, individual accountability, and gleaning for the vulnerable
(ch. 24).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M (small-caps convention); "the LORD" in T — matches Numbers
  and Exodus scripts
- H430 (אֱלֹהִים): "God" in all tiers
- H7523 (רָצַח): "murderer/murder" for intentional killing (ch. 19) — distinct from
  H5221 (נָכָה, "kills/strikes") used for the accidental death in 19:4–5; this lexical
  distinction drives the whole refugee law
- H1350 (גָּאַל): "blood avenger" all tiers — the kinsman entitled to execute; L/M use the
  technical phrase, T unpacks it as "the kinsman-avenger"
- H4733 (מִקְלָט) appears implicitly via "cities of refuge" formula; rendered "city of refuge"
  all tiers
- H2764 (חֵרֶם): "devote to destruction" / "place under the ban" — L uses "devote to
  complete destruction," M uses "utterly destroy," T surfaces the meaning: "consecrate to
  annihilation"
- H5315 (נֶפֶשׁ): "life" (not "soul") in 24:6 pledge law — "taking a life in pledge" captures
  the embodied sense; similarly "a life" in the lex talionis (19:21)
- H2617 (חֶסֶד): does not appear in this range; no decision needed
- H1285 (בְּרִית): does not appear in this range; no decision needed
- H1121+H112 (בֶּן סוֹרֵר): "stubborn and rebellious son" — standard rendering; L preserves
  the hendiadys, T surfaces the honour-shame breach
- H3919 (לֵל) / "hung on a tree" (21:22–23): rendered literally "hang him on a tree" L;
  "hung on a tree" M; T notes the Pauline echo (Gal 3:13 applies this to Christ's cross)
  without anachronistically asserting it — phrasing: "hanged on a tree, and so accursed
  before God"
- H8441 (תּוֹעֵבָה): "abomination" all tiers — the strong cultic revulsion word
- H6945/H6948 (קָדֵשׁ/קְדֵשָׁה): "male/female cult prostitute" — not merely a secular
  "prostitute"; L uses "shrine prostitute," M/T use "cult prostitute"
- H5392 (נֶשֶׁךְ): "interest / usury" — "interest" in all tiers; L includes both H5392 and
  H8636 (תַּרְבִּית) where both appear, noting the semantic overlap
- H5797+H1060 (רֵאשִׁית אוֹנוֹ): "the firstfruits of his strength" — standard; T notes
  the honor claim attached to firstborn status
- H1200 (בְּעֵרַת): "purge / burn out" — "purge the evil from your midst" all tiers;
  matches the refrain formula throughout chs. 19–22
- Lex talionis (19:21): rendered word-for-word in L; reordered for flow in M; T notes this
  is not a license for private revenge but a public tariff capping disproportionate
  retaliation — proportionality, not cruelty
- Ch. 21:22–23: Paul quotes this in Gal 3:13. T tier notes the trajectory without
  anachronism, phrasing: "for to hang on a tree is to stand under God's curse."
- Ch. 22:6–7 (mother bird): a microcosm of the environmental/creational ethic embedded in
  the law; T tier surfaces this
- Ch. 23:15–16 (escaped slave): stands in dramatic contrast to most ancient Near Eastern
  codes which mandated return; T tier marks this
- Ch. 24:16 (individual responsibility): a watershed principle in ancient law; T tier notes
  its scope
- Poetic/rhetorical refrains ("so you shall purge the evil from your midst," "that it may
  go well with you"): preserved verbatim in L/M, given expressive cadence in T
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

DEUTERONOMY = {
  "19": {
    "1": {
      "L": "When the LORD your God cuts off the nations whose land the LORD your God is giving you, and you dispossess them and dwell in their cities and in their houses —",
      "M": "When the LORD your God cuts off the nations whose land he is giving you to possess, and you drive them out and settle in their cities and houses —",
      "T": "When the LORD clears away the nations from the land he is handing to you, and you move into their cities and homes —"
    },
    "2": {
      "L": "you shall set apart three cities for yourself in the midst of your land which the LORD your God is giving you to possess.",
      "M": "you shall designate three cities in the midst of your land that the LORD your God is giving you to possess.",
      "T": "you are to mark out three cities in the heart of the land the LORD is giving you — cities of refuge, set apart for this purpose."
    },
    "3": {
      "L": "You shall prepare the road and divide into three parts the territory of your land which the LORD your God is giving you as an inheritance, so that every manslayer may flee there.",
      "M": "Prepare the roads and divide your territory into three districts, so that any manslayer can flee to one of these cities.",
      "T": "Build and maintain clear roads to these cities, and divide your land into three regions accordingly, so that any person who has accidentally killed someone can reach safety quickly."
    },
    "4": {
      "L": "This is the case of the manslayer who may flee there and live: whoever kills his neighbor unintentionally, not having hated him previously —",
      "M": "This is the provision for the manslayer who may flee there and live: anyone who kills his neighbor unintentionally, without having harbored any previous hatred against him —",
      "T": "Here is who may use these cities: the person who kills a neighbor by pure accident, with no malice beforehand —"
    },
    "5": {
      "L": "as when a man goes with his neighbor into the forest to cut wood, and his hand swings the ax to cut down the tree, and the iron slips from the helve and strikes his neighbor so that he dies — he shall flee to one of these cities and live.",
      "M": "as when someone goes into the forest with a neighbor to cut wood, swings the ax to fell a tree, and the iron head slips from the handle and strikes the neighbor so that he dies — that person shall flee to one of these cities and live.",
      "T": "Suppose a man goes with his neighbor into the forest to cut timber. He swings his ax at a tree, the iron head flies off the handle, and his neighbor is struck dead. That man — with no intention of harm — must be able to flee to a city of refuge and live."
    },
    "6": {
      "L": "lest the blood avenger pursue the manslayer in the heat of his anger and overtake him, because the way is long, and strike him mortally — though he was not deserving of death, since he had not hated him in previous time.",
      "M": "Otherwise the blood avenger may pursue him in fierce anger, overtake him on a long road, and strike him down — though he was not deserving of death, since he had not hated him beforehand.",
      "T": "Without that refuge, the kinsman-avenger could pursue in the heat of grief and fury, catch up with the man along the road, and cut him down — though that man deserved no death, for there was no hatred in his heart."
    },
    "7": {
      "L": "Therefore I command you: You shall set apart three cities.",
      "M": "Therefore I command you: You shall designate three cities for this purpose.",
      "T": "This is why I give this command: set apart three cities — mercy must be built into the legal structure of the land."
    },
    "8": {
      "L": "And if the LORD your God enlarges your territory, as he swore to your fathers, and gives you all the land that he promised to give to your fathers —",
      "M": "If the LORD your God enlarges your territory, as he swore to your ancestors, and gives you all the land he promised them —",
      "T": "If the LORD expands your borders — fulfilling every oath he swore to your ancestors and granting you the full extent of the promised land —"
    },
    "9": {
      "L": "provided you keep all this commandment that I command you today, by loving the LORD your God and by walking in his ways always — then you shall add three more cities to these three,",
      "M": "and if you keep all this commandment I am giving you today, loving the LORD your God and walking always in his ways — then you shall add three more cities beyond these three,",
      "T": "and if you remain faithful to all that I command today, loving the LORD your God and walking in his ways without turning aside — then add three more refuge cities to the original three."
    },
    "10": {
      "L": "so that innocent blood may not be shed in your land that the LORD your God is giving you for an inheritance, and so blood guilt be upon you.",
      "M": "so that innocent blood is not shed in your land that the LORD your God is giving you for an inheritance, and so that bloodguilt does not come upon you.",
      "T": "The goal is this: that no innocent person's blood be spilled on the land the LORD is giving you, and that the land not be stained with guilt that falls back on you."
    },
    "11": {
      "L": "But if anyone hates his neighbor and lies in wait for him and rises against him and strikes him mortally so that he dies, and flees into one of these cities,",
      "M": "But if someone hates his neighbor, ambushes him, strikes him down so that he dies, and then flees to one of these cities,",
      "T": "But if a man nurses hatred for his neighbor, lies in wait, attacks and kills him, and then runs to one of these refuge cities —"
    },
    "12": {
      "L": "the elders of his city shall send and fetch him from there, and hand him over to the blood avenger, that he may die.",
      "M": "the elders of his city shall send for him, bring him back from there, and hand him over to the blood avenger to be put to death.",
      "T": "the elders of his own city must send for him, drag him back, and hand him over to the kinsman-avenger. A refuge city is not a sanctuary for a murderer."
    },
    "13": {
      "L": "Your eye shall not pity him, but you shall purge the guilt of innocent blood from Israel, so that it may go well with you.",
      "M": "Show him no pity. Purge the guilt of innocent blood from Israel, so that things may go well for you.",
      "T": "No mercy for him. Purge the land of the innocent blood that cries out — only then will things go well for Israel."
    },
    "14": {
      "L": "You shall not move your neighbor's landmark, which the men of old have set, in the inheritance that you will hold in the land that the LORD your God is giving you to possess.",
      "M": "Do not move your neighbor's boundary marker, set by your predecessors in your inheritance, in the land the LORD your God is giving you to possess.",
      "T": "Do not shift your neighbor's boundary stone — those ancient markers, planted by the men who came before you, define a neighbor's God-given portion. To move one is to steal what the LORD allocated."
    },
    "15": {
      "L": "A single witness shall not rise up against a person for any crime or any wrong in connection with any offense that he has committed. Only on the evidence of two witnesses or of three witnesses shall a matter be established.",
      "M": "A single witness is not enough to convict anyone of any crime or wrongdoing — whatever the offense. A matter is established only on the testimony of two or three witnesses.",
      "T": "No man can be convicted on one person's word alone, regardless of the offense. The truth of any charge must be confirmed by two or three witnesses — this protects every person from a single accuser's vendetta."
    },
    "16": {
      "L": "If a malicious witness rises against a person to testify wrongdoing against him,",
      "M": "If a malicious witness comes forward and accuses someone of a crime,",
      "T": "If a false accuser comes forward and levels a charge against another person —"
    },
    "17": {
      "L": "then both parties to the dispute shall stand before the LORD, before the priests and the judges who are in office in those days.",
      "M": "both parties in the dispute shall stand before the LORD, before the priests and the judges who are serving at that time.",
      "T": "both the accuser and the accused must appear before the LORD — before the priests and judges then in office. The dispute is not merely between two people; it is heard before God."
    },
    "18": {
      "L": "The judges shall investigate thoroughly, and if the witness is a false witness and has testified falsely against his brother,",
      "M": "The judges shall investigate the matter carefully, and if the witness has testified falsely against his brother,",
      "T": "The judges will examine the case with all diligence, and if they find that the witness lied — that the accusation was fabricated against an innocent person —"
    },
    "19": {
      "L": "then you shall do to him as he had intended to do to his brother. So you shall purge the evil from your midst.",
      "M": "you shall do to him what he intended to do to his brother. Purge the evil from your midst.",
      "T": "you shall turn his own scheme back on him — whatever he meant to inflict on the innocent man, he now receives. Purge the evil from your midst."
    },
    "20": {
      "L": "And those who remain shall hear and fear, and shall never again commit any such evil among you.",
      "M": "The rest of the people will hear about it and be afraid, and they will never again do such an evil thing among you.",
      "T": "When the rest of the people hear what happened, fear will take hold — and malicious false accusation will cease. Justice made public teaches the whole community."
    },
    "21": {
      "L": "Your eye shall not pity: life for life, eye for eye, tooth for tooth, hand for hand, foot for foot.",
      "M": "Show no pity: life for life, eye for eye, tooth for tooth, hand for hand, foot for foot.",
      "T": "Let there be no misplaced compassion. The punishment must match the crime exactly — life for life, eye for eye, tooth for tooth, hand for hand, foot for foot. This lex talionis is not a license for private revenge; it is a public tariff that caps retaliation, ensuring proportionality."
    }
  },
  "20": {
    "1": {
      "L": "When you go out to war against your enemies and see horses and chariots and an army larger than yours, you shall not be afraid of them, for the LORD your God is with you, who brought you up from the land of Egypt.",
      "M": "When you march out to battle against your enemies and see horses, chariots, and a force larger than yours, do not be afraid of them — the LORD your God who brought you out of Egypt is with you.",
      "T": "When you march into battle and face an army that outnumbers you — cavalry, war chariots, overwhelming force — do not let fear take hold. The LORD your God, who led you out of Egypt, marches with you."
    },
    "2": {
      "L": "And as you draw near to the battle, the priest shall come forward and speak to the people,",
      "M": "As the army approaches the battle line, the priest shall step forward and address the troops,",
      "T": "Before the fighting begins, the priest steps to the front and speaks — this is no mere ritual; divine assurance must precede human courage."
    },
    "3": {
      "L": "and shall say to them, 'Hear, O Israel! Today you are drawing near for battle against your enemies. Let not your heart be faint. Do not be afraid, or panic, or tremble before them,",
      "M": "saying, 'Hear, O Israel! Today you are about to engage your enemies in battle. Do not be faint-hearted. Do not be afraid or alarmed or terrified by them,",
      "T": "'Listen, Israel! Today you stand at the edge of battle. Do not let your heart falter. Do not be afraid, do not panic, do not dissolve in terror before them —"
    },
    "4": {
      "L": "for the LORD your God is he who goes with you to fight for you against your enemies, to give you victory.'",
      "M": "for the LORD your God goes with you to fight on your behalf against your enemies and to give you victory.'",
      "T": "for the LORD your God goes before you into the fight — he battles your enemies and hands you the victory.'"
    },
    "5": {
      "L": "Then the officers shall speak to the people, saying, 'Who is the man who has built a new house and has not dedicated it? Let him go back to his house, lest he die in the battle and another man dedicate it.",
      "M": "The officers shall then address the troops: 'Has any man built a new house and not yet dedicated it? Let him go home, so he does not die in battle and someone else dedicates it.",
      "T": "Then the officers address the assembled force: 'Has anyone built a new house but not yet held the dedication? Go home — do not die in battle only to have another man perform the ceremony you earned.'"
    },
    "6": {
      "L": "And who is the man who has planted a vineyard and has not yet enjoyed its fruit? Let him go back to his house, lest he die in the battle and another man enjoy it.",
      "M": "Has any man planted a vineyard and not yet eaten of its fruit? Let him go home, so he does not die in battle and someone else enjoys it.",
      "T": "'Has anyone planted a vineyard but never tasted the first harvest? Go home — the vine you planted should not become another man's reward.'"
    },
    "7": {
      "L": "And who is the man who has betrothed a wife and has not taken her? Let him go back to his house, lest he die in battle and another man take her.'",
      "M": "Has any man become engaged to a woman and not yet married her? Let him go home, so he does not die in battle and another man marry her.'",
      "T": "'Has anyone pledged himself to a woman but not yet brought her home as his wife? Go home — you should not fall in battle and leave her for another man to claim.'"
    },
    "8": {
      "L": "And the officers shall speak further to the people, and shall say, 'Who is the man who is fearful and faint-hearted? Let him go back to his house, lest the heart of his brothers melt as his heart.'",
      "M": "The officers shall continue: 'Is any man here afraid or faint-hearted? Let him go home so that he does not cause his comrades to lose heart as well.'",
      "T": "'And is anyone here simply afraid — heart already failing before the fight begins? Go home. One man's fear is contagious; we cannot afford to have it spread through the ranks.'"
    },
    "9": {
      "L": "And when the officers have finished speaking to the people, commanders of armies shall be appointed at the head of the people.",
      "M": "When the officers finish addressing the troops, they shall appoint military commanders to lead them.",
      "T": "When the officers have finished their address and sent home all who qualified for exemption, they then appoint commanders — the army that remains is ready and willing."
    },
    "10": {
      "L": "When you draw near to a city to fight against it, you shall first offer it terms of peace.",
      "M": "When you advance on a city to attack it, first offer it peace.",
      "T": "Before any siege or assault, send an offer of peace. War is not the first resort."
    },
    "11": {
      "L": "And if it responds to you peaceably and opens to you, all the people who are found in it shall be subject to forced labor for you and shall serve you.",
      "M": "If it accepts your offer and opens its gates, all the people found there shall serve you under compulsory labor.",
      "T": "If the city accepts and opens its gates, its people become your subjects and laborers — spared, but subject."
    },
    "12": {
      "L": "But if it will not make peace with you and makes war against you, then you shall besiege it.",
      "M": "But if it refuses peace and chooses to fight, then you shall lay siege to it.",
      "T": "But if the city refuses peace and takes up arms against you, you may besiege it."
    },
    "13": {
      "L": "And when the LORD your God gives it into your hand, you shall strike every male in it with the edge of the sword.",
      "M": "When the LORD your God delivers it into your hand, put every male to the sword.",
      "T": "When the LORD gives it into your hand — and he will — put every male to the sword."
    },
    "14": {
      "L": "But the women and the little ones, the livestock, and everything in the city — all its spoil — you shall take as plunder for yourself. And you shall eat the spoil of your enemies, which the LORD your God has given you.",
      "M": "But the women, children, livestock, and all the goods of the city you may take as plunder for yourselves — eat what your enemies possessed, for the LORD your God has given it to you.",
      "T": "The women, children, livestock, and all property you may take as rightful spoil — the LORD your God has given it to you as the fruit of the victory."
    },
    "15": {
      "L": "Thus you shall do to all the cities that are very far from you, which are not among the cities of these nations.",
      "M": "This is how you shall treat all the distant cities, those not belonging to these nearby nations.",
      "T": "This is the rule for distant cities — cities outside the promised land itself."
    },
    "16": {
      "L": "But in the cities of these peoples that the LORD your God is giving you for an inheritance, you shall not let anything that breathes survive.",
      "M": "In the cities of these peoples that the LORD your God is giving you as your inheritance, you must not leave anything alive that breathes.",
      "T": "But in the cities of the nations the LORD is giving you as your inheritance, nothing that breathes may be left alive."
    },
    "17": {
      "L": "You shall devote them to complete destruction — the Hittites and the Amorites, the Canaanites and the Perizzites, the Hivites and the Jebusites — as the LORD your God has commanded,",
      "M": "Utterly destroy them — the Hittites, Amorites, Canaanites, Perizzites, Hivites, and Jebusites — as the LORD your God has commanded,",
      "T": "Consecrate them to total destruction — Hittites, Amorites, Canaanites, Perizzites, Hivites, Jebusites — exactly as the LORD your God has commanded."
    },
    "18": {
      "L": "so that they may not teach you to do according to all their abominable practices that they have done for their gods, and so cause you to sin against the LORD your God.",
      "M": "so that they cannot teach you to imitate all the abominations they practiced in the worship of their gods and lead you into sin against the LORD your God.",
      "T": "The reason is clear: if they remain, they will teach Israel their ways — and the worship of their gods is the deepest kind of corruption, the sin that destroys a people from within."
    },
    "19": {
      "L": "When you besiege a city for many days, making war against it to capture it, you shall not destroy its trees by wielding an ax against them. You may eat from them, but you shall not cut them down — for is the tree of the field a man, that it should come under siege from you?",
      "M": "During a prolonged siege, do not destroy the surrounding trees by taking an ax to them. You may eat their fruit, but do not cut them down. Are the trees of the field human combatants, that you should besiege them?",
      "T": "Even during a long siege, do not destroy the fruit trees with your axes. Eat from them — they are your provision, not your enemy. The tree has not taken up arms against you; it simply stands in the field, indifferent to the conflict below."
    },
    "20": {
      "L": "Only the trees that you know are not trees for food you may destroy and cut down, that you may build siege works against the city that is making war with you, until it falls.",
      "M": "You may cut down trees that do not produce food and use the timber to build siege works against the city fighting you, until it surrenders.",
      "T": "Non-fruit-bearing trees may be felled for timber and used in siege construction — but the living, fruit-bearing trees are to be spared. The created order is not collateral damage in human warfare."
    }
  },
  "21": {
    "1": {
      "L": "If a slain person is found lying in the open field in the land that the LORD your God is giving you to possess, and it is not known who struck him down,",
      "M": "If a murdered person is found lying in the open country in the land the LORD your God is giving you, and it is unknown who killed him,",
      "T": "A body is found in the field — killed, but by whom no one knows. The land itself is now under threat, for innocent blood has been shed on it."
    },
    "2": {
      "L": "then your elders and your judges shall come out and measure to the surrounding cities, to the city that is nearest to the slain person.",
      "M": "your elders and judges shall go out and measure the distance to the towns surrounding the site, to determine which town is nearest the victim.",
      "T": "The elders and judges go out together and measure — every nearby town is implicated until the nearest one is identified and assumes responsibility."
    },
    "3": {
      "L": "And the elders of the city that is nearest to the slain person shall take a heifer that has never been worked and has never pulled in a yoke.",
      "M": "The elders of the nearest town shall take a young cow that has never been put to work or yoked.",
      "T": "The elders of that nearest town must take a young heifer that has never been worked — an unblemished animal, untouched by the labor of ordinary life, set apart for this solemn act."
    },
    "4": {
      "L": "And the elders of that city shall bring the heifer down to a valley with a perennial stream, one that is neither plowed nor sown, and shall break the heifer's neck there in the valley.",
      "M": "They shall bring the heifer down to a rocky ravine with a running stream — ground that has never been plowed or sown — and break the heifer's neck there.",
      "T": "They lead the heifer to a wild, uncultivated valley with a running stream — untamed ground, never given over to human agriculture — and break its neck there. Blood is answered by death, even when the killer is unnamed."
    },
    "5": {
      "L": "Then the priests, the sons of Levi, shall come near, for the LORD your God has chosen them to minister to him and to bless in the name of the LORD, and by their word every dispute and every assault shall be settled.",
      "M": "Then the Levitical priests shall come forward, for the LORD your God has chosen them to serve him and to pronounce blessings in his name, and every dispute and injury is to be settled by their ruling.",
      "T": "The Levitical priests step forward — they alone stand at the intersection of God and the people, authorized to invoke his name in blessing, and to adjudicate every matter of disputed guilt."
    },
    "6": {
      "L": "And all the elders of that city nearest to the slain person shall wash their hands over the heifer whose neck was broken in the valley.",
      "M": "All the elders of the town nearest the murdered man shall wash their hands over the heifer whose neck was broken in the ravine.",
      "T": "Then all the elders of that town wash their hands over the slaughtered heifer — a public, ritual declaration of innocence, an act the whole community witnesses."
    },
    "7": {
      "L": "And they shall declare, 'Our hands did not shed this blood, and our eyes did not see it done.",
      "M": "They shall declare, 'Our hands did not shed this blood, nor did we witness it.',",
      "T": "'Our hands shed no blood,' they declare. 'Our eyes saw nothing.' The community publicly dissociates itself from the crime."
    },
    "8": {
      "L": "Forgive your people Israel, O LORD, whom you have redeemed, and do not set the guilt of innocent blood in the midst of your people Israel.' And the bloodguilt shall be forgiven them.",
      "M": "Forgive your people Israel, whom you redeemed, O LORD, and do not hold the guilt of innocent blood against your people.' And they will be absolved of bloodguilt.",
      "T": "'Forgive your people, O LORD — the people you redeemed — and do not let this innocent blood become a charge against us.' When the rite is complete, the guilt is lifted. The land breathes again."
    },
    "9": {
      "L": "So you shall purge the guilt of innocent blood from your midst, when you do what is right in the sight of the LORD.",
      "M": "In this way you shall purge innocent bloodguilt from your midst by doing what is right in the sight of the LORD.",
      "T": "This is how you keep the land clean — not by finding the killer, which may be impossible, but by performing the rite that shows the community took innocent blood seriously."
    },
    "10": {
      "L": "When you go out to battle against your enemies, and the LORD your God gives them into your hand and you take them captive,",
      "M": "When you go to war against your enemies and the LORD your God gives you victory over them and you take prisoners,",
      "T": "After a battle, when the LORD has given victory and prisoners have been taken —"
    },
    "11": {
      "L": "and you see among the captives a beautiful woman, and you desire her and want to take her as your wife,",
      "M": "and you notice among the captives a beautiful woman and are attracted to her and want to marry her,",
      "T": "and you see among the captive women one who is beautiful, and desire stirs in you —"
    },
    "12": {
      "L": "then you shall bring her home to your house, and she shall shave her head and trim her nails.",
      "M": "bring her home to your house. She shall shave her head and trim her nails.",
      "T": "you must bring her home first. She shaves her head and cuts her nails — outward signs of leaving her old life behind, entering a period of transition."
    },
    "13": {
      "L": "And she shall take off the garment of her captivity and shall remain in your house and mourn her father and her mother a full month. After that you may go in to her and be her husband, and she shall be your wife.",
      "M": "She shall remove the clothing she wore in captivity, stay in your house, and mourn her father and mother for a full month. After that you may marry her, and she shall be your wife.",
      "T": "She puts aside the garments of her captivity and spends a full month in your house mourning the loss of her family and her former world. Only after that month of grief is honored may you take her as your wife. Her humanity is not to be trampled in your haste."
    },
    "14": {
      "L": "But if you no longer delight in her, you shall let her go where she wishes. You shall not sell her for money, nor shall you treat her as a slave, since you have violated her.",
      "M": "If you are no longer pleased with her, you must release her to go wherever she chooses. You may not sell her for money or treat her as a slave, because you have violated her.",
      "T": "But if the marriage sours and you no longer want her, let her go free — wherever she chooses. You may not sell her or treat her like property. The act of taking her as your wife meant something; you humbled her, and she must be released with her dignity intact."
    },
    "15": {
      "L": "If a man has two wives, the one loved and the other unloved, and both have borne him children, and if the firstborn son belongs to the unloved wife —",
      "M": "If a man has two wives — one loved and one unloved — and both have borne him sons, and the unloved wife's son is the firstborn,",
      "T": "When a man has two wives — one favored, one not — and both have given him sons, and it happens that the firstborn belongs to the unloved wife —"
    },
    "16": {
      "L": "then on the day when he assigns his possessions as an inheritance to his sons, he may not treat the son of the loved as the firstborn in preference to the son of the unloved who is the firstborn.",
      "M": "when he divides his estate among his sons, he may not give the firstborn's rights to the son of the loved wife instead of to the actual firstborn, the son of the unloved.",
      "T": "the day he settles the inheritance, he may not play favorites — he cannot elevate the son of the wife he loves above the son of the wife he neglects, even if that is his private wish."
    },
    "17": {
      "L": "But he shall acknowledge the firstborn, the son of the unloved, by giving him a double portion of all that he has, for he is the firstfruits of his strength. The right of the firstborn is his.",
      "M": "He must acknowledge the unloved wife's son as the firstborn by giving him a double share of all his property, for that son is the firstfruits of his father's strength. The birthright belongs to him.",
      "T": "He must give the unloved wife's son a double portion of the estate — for that son is the firstfruits of his father's strength, the beginning of his posterity. Birthright is not a gift the father confers by sentiment; it is a legal claim the son was born with."
    },
    "18": {
      "L": "If a man has a stubborn and rebellious son who will not obey the voice of his father or the voice of his mother, and, though they discipline him, will not listen to them,",
      "M": "If a man has a stubborn and rebellious son who refuses to obey either parent, and who remains defiant even after they discipline him,",
      "T": "When a son is stubbornly, persistently rebellious — ignoring both his father and his mother, unbroken by every form of discipline —"
    },
    "19": {
      "L": "then his father and his mother shall take hold of him and bring him out to the elders of his city at the gate of his place,",
      "M": "his father and mother shall take hold of him and bring him before the elders of his town at the city gate,",
      "T": "his parents must take hold of him and bring him to the elders at the city gate. The family's private authority has been exhausted; the community must now act."
    },
    "20": {
      "L": "and they shall say to the elders of his city, 'This son of ours is stubborn and rebellious; he will not obey our voice; he is a glutton and a drunkard.'",
      "M": "They shall say to the elders, 'This son of ours is stubborn and rebellious — he refuses to obey us. He is a glutton and a drunkard.'",
      "T": "'This son of ours,' they say, 'is beyond our reach. He is stubborn, rebellious, out of control — given to gluttony and drunkenness.' The charge is public; the shame falls on him before the whole town."
    },
    "21": {
      "L": "Then all the men of his city shall stone him to death with stones. So you shall purge the evil from your midst, and all Israel shall hear and fear.",
      "M": "Then all the men of his town shall stone him to death. So you shall purge the evil from your midst, and all Israel will hear about it and be afraid.",
      "T": "All the men of the town stone him to death. This is a severe law — its purpose is not cruelty but purging: a son who has cut himself free of all social bonds is a threat to the fabric of the community. All Israel hears, and the fear that follows is itself a warning."
    },
    "22": {
      "L": "And if a man has committed a sin worthy of death and is put to death, and you hang him on a tree,",
      "M": "If a man is executed for a capital offense and you hang his body on a tree,",
      "T": "When a man is executed for a crime that merits death and his corpse is displayed on a tree —"
    },
    "23": {
      "L": "his body shall not remain overnight on the tree, but you shall bury him the same day, for a hanged man is cursed by God. You shall not defile your land that the LORD your God is giving you for an inheritance.",
      "M": "do not leave his body on the tree overnight. Bury him that same day, for anyone hanged on a tree is under God's curse. Do not defile your land that the LORD your God is giving you as an inheritance.",
      "T": "his body must not stay there overnight — bury him before sunset. For to hang on a tree is to stand under God's own curse. Leave the body up and the land is defiled; bury it the same day and the curse is not spread onto the ground. (Paul will later cite this verse in Galatians 3 to proclaim that Christ, hanging on the cross, absorbed this curse in the place of those the law condemned.)"
    }
  },
  "22": {
    "1": {
      "L": "You shall not see your brother's ox or his sheep going astray and ignore them. You shall surely return them to your brother.",
      "M": "If you see your fellow Israelite's ox or sheep straying, do not ignore it — you must return it to its owner.",
      "T": "If you see a neighbor's animal wandering loose, do not look the other way. Bring it back. Indifference to a neighbor's loss is a form of theft."
    },
    "2": {
      "L": "And if your brother is not near you, or if you do not know him, you shall bring it into your house, and it shall stay with you until your brother seeks it. Then you shall restore it to him.",
      "M": "If the owner does not live nearby, or you do not know who he is, take the animal home and care for it until its owner comes looking for it. Then return it.",
      "T": "If the owner is unknown or far away, take the animal in and care for it at your own expense. When the owner comes searching, hand it back. The obligation does not disappear just because the owner is a stranger."
    },
    "3": {
      "L": "And you shall do the same with his donkey, and the same with his garment, and the same with any lost thing of your brother's that you find. You may not hide yourself.",
      "M": "Do the same with his donkey, his garment, or any lost property of your neighbor's that you find. You cannot pretend not to see it.",
      "T": "Donkey, garment, any lost object — the obligation is the same. You cannot legally claim not to have noticed. Active neighborliness is required."
    },
    "4": {
      "L": "You shall not see your brother's donkey or his ox fallen down by the way and ignore them. You shall surely help him to lift them up again.",
      "M": "If you see your neighbor's donkey or ox collapsed on the road, do not ignore it — help him lift it up.",
      "T": "If a neighbor's animal has collapsed under its load, you stop and help — not just offer sympathy. The neighbor's burden is your concern."
    },
    "5": {
      "L": "A woman shall not wear a man's garment, nor shall a man put on a woman's cloak, for all who do these things are an abomination to the LORD your God.",
      "M": "A woman must not wear men's clothing, nor a man women's clothing — everyone who does such things is an abomination to the LORD your God.",
      "T": "The boundaries between male and female — expressed even in dress — belong to the created order. To deliberately erase them is an abomination: a refusal of the distinctions God built into human identity."
    },
    "6": {
      "L": "If you come upon a bird's nest in any tree or on the ground, with young ones or eggs and the mother sitting on the young or on the eggs, you shall not take the mother with the young.",
      "M": "If you happen to find a bird's nest in a tree or on the ground, with chicks or eggs and the mother sitting on them, do not take the mother along with the young.",
      "T": "If you stumble on a bird's nest — mother settled over chicks or eggs — do not take the mother. This small law carries a large principle: the fertility of the created order is not yours to exhaust at will."
    },
    "7": {
      "L": "You shall let the mother go, but the young you may take for yourself, so that it may go well with you, and that you may live long.",
      "M": "Let the mother fly away and take only the young. Then things will go well for you, and you will have a long life.",
      "T": "Release the mother — she can reproduce again; the chain of life continues. Take only the young. Obedience to even this small creational law carries the promise of longevity and flourishing."
    },
    "8": {
      "L": "When you build a new house, you shall make a parapet for your roof, so that you do not bring the guilt of blood upon your house if anyone falls from it.",
      "M": "When you build a new house, install a railing around the roof, so that you do not incur bloodguilt if someone falls from it.",
      "T": "Build a railing on your roof — people walk there, and you are responsible for their safety on your property. Neglect this and a preventable death falls on your conscience."
    },
    "9": {
      "L": "You shall not sow your vineyard with two kinds of seed, lest the whole yield be forfeited to the sanctuary — both the crop you have sown and the produce of the vineyard.",
      "M": "Do not plant two kinds of seed in your vineyard; if you do, everything grown there — the full crop and the vineyard produce — becomes forfeit.",
      "T": "Do not mix your seed in the vineyard. The principle of kinds-kept-distinct runs through the created order; violating it makes the entire yield forfeit — you lose everything by blurring the boundary."
    },
    "10": {
      "L": "You shall not plow with an ox and a donkey together.",
      "M": "Do not plow with an ox and a donkey yoked together.",
      "T": "Do not yoke an ox and a donkey together for plowing — they are unequal in strength and gait, and the weaker animal suffers. The law protects the animal from a burden it was not built to bear."
    },
    "11": {
      "L": "You shall not wear cloth made of wool and linen mixed together.",
      "M": "Do not wear clothing woven from a mixture of wool and linen.",
      "T": "Do not wear sha'atnez — fabric that mingles wool and linen in the weave. The laws of mixture extend even to what you put on your body."
    },
    "12": {
      "L": "You shall make tassels on the four corners of the garment with which you cover yourself.",
      "M": "Make tassels on the four corners of your outer garment.",
      "T": "The tassels on the corners of your garment are a constant physical reminder — every movement signals that you belong to the LORD and live under his commands."
    },
    "13": {
      "L": "If any man takes a wife and goes in to her and then hates her",
      "M": "If a man marries a woman, sleeps with her, and then turns against her",
      "T": "If a man marries, consorts with his wife, then turns on her —"
    },
    "14": {
      "L": "and brings charges against her and gives her a bad name, saying, 'I took this woman, and when I came near her, I did not find in her evidence of virginity' —",
      "M": "and publicly slanders her, saying, 'I married this woman, but when I lay with her I found no proof of her virginity' —",
      "T": "and publicly destroys her reputation, claiming she was not a virgin when he married her —"
    },
    "15": {
      "L": "then the father of the young woman and her mother shall take and bring out the evidence of her virginity to the elders of the city at the gate.",
      "M": "then the young woman's father and mother shall bring the evidence of her virginity before the elders at the city gate.",
      "T": "her parents bring forward the physical evidence of her virginity and lay it before the elders at the gate — the accusation will be tested publicly."
    },
    "16": {
      "L": "And the father of the young woman shall say to the elders, 'I gave my daughter to this man to marry, and he hates her;",
      "M": "The girl's father shall say to the elders, 'I gave my daughter to this man in marriage, but he has turned against her;",
      "T": "'I gave this man my daughter,' her father says to the elders. 'He married her — and now he hates her.'"
    },
    "17": {
      "L": "and now he has brought charges against her, saying, \"I did not find in your daughter evidence of virginity.\" But here is the evidence of my daughter's virginity.' And they shall spread the cloth before the elders of the city.",
      "M": "he has accused her of misconduct, saying, \"Your daughter was not a virgin.\" But here is the proof of her virginity.' They shall then spread the cloth before the elders.",
      "T": "'He fabricated a slander: \"Your daughter was not a virgin.\" But the evidence is here.' They spread the cloth before the elders. The accusation is answered. The community judges."
    },
    "18": {
      "L": "Then the elders of that city shall take the man and discipline him,",
      "M": "The elders of that town shall then take the man and punish him.",
      "T": "If the evidence confirms the wife's innocence, the elders seize the husband and punish him —"
    },
    "19": {
      "L": "and they shall fine him a hundred shekels of silver and give them to the father of the young woman, because he has brought a bad name upon a virgin of Israel. And she shall be his wife. He may not divorce her all his days.",
      "M": "They shall fine him a hundred shekels of silver, which shall be given to the young woman's father, because he defamed a virgin of Israel. She remains his wife; he may never divorce her.",
      "T": "He pays a hundred shekels of silver to her father — double the typical bride-price — because he tried to use the law as a weapon against an innocent woman. She remains his wife, and he forfeits the right to divorce her for the rest of his life. The law turns his scheme against him."
    },
    "20": {
      "L": "But if the thing is true, that evidence of virginity was not found in the young woman,",
      "M": "But if the charge is true and no evidence of virginity is found for the young woman,",
      "T": "But if the charge is upheld — if the evidence is absent and the accusation proves true —"
    },
    "21": {
      "L": "then they shall bring the young woman to the door of her father's house, and the men of her city shall stone her to death with stones, because she has done an outrageous thing in Israel by whoring in her father's house. So you shall purge the evil from your midst.",
      "M": "they shall bring her to the entrance of her father's house, and the men of her town shall stone her to death. She has committed a shameful act in Israel by being promiscuous in her father's house. Purge the evil from your midst.",
      "T": "she is brought to her father's door and the men of the town stone her to death. She acted shamefully — engaging in sexual immorality while living under her father's authority and presenting herself as chaste. Purge the evil from your midst."
    },
    "22": {
      "L": "If a man is found lying with the wife of another man, both of them shall die — the man who lay with the woman, and the woman. So you shall purge the evil from Israel.",
      "M": "If a man is caught having sex with another man's wife, both the man and the woman shall die. Purge the evil from Israel.",
      "T": "Adultery is a crime against the marriage covenant, the spouse, and the community. Both parties die — equal accountability, no double standard. Purge the evil from Israel."
    },
    "23": {
      "L": "If there is a young woman who is a virgin betrothed to a husband, and a man finds her in the city and lies with her,",
      "M": "If a virgin who is engaged to be married is found in the city and a man lies with her,",
      "T": "When a betrothed virgin is found in town and a man lies with her —"
    },
    "24": {
      "L": "then you shall bring them both out to the gate of that city and stone them to death with stones — the young woman because she did not cry out in the city, and the man because he violated his neighbor's wife. So you shall purge the evil from your midst.",
      "M": "bring both of them to the gate of the town and stone them to death — the woman because she did not cry for help inside the city, and the man because he violated his neighbor's betrothed wife. Purge the evil from your midst.",
      "T": "both are brought to the city gate and stoned — the man because he violated what was his neighbor's; the woman because she made no outcry in a place where she could have been heard. The town is complicit in silence; in the town, silence is consent. Purge the evil."
    },
    "25": {
      "L": "But if in the open country a man meets a young woman who is betrothed and the man seizes her and lies with her, then only the man who lay with her shall die.",
      "M": "But if the man meets the betrothed woman in the open country, and forcibly lies with her, only the man shall die.",
      "T": "But if the assault happens in the countryside — where no one could hear a cry — only the man dies. The location matters: it determines what was possible, and the law is just enough to take that into account."
    },
    "26": {
      "L": "But you shall do nothing to the young woman; she has committed no sin worthy of death. For this case is like that of a man who attacks his neighbor and murders him —",
      "M": "Do nothing to the young woman — she has done nothing deserving death. This case is like that of a man who attacks and kills his neighbor —",
      "T": "The woman bears no guilt. This is not a seduction; this is assault. It is as straightforward as one man attacking and murdering another —"
    },
    "27": {
      "L": "because he found her in the open country, and though the betrothed young woman cried out, there was no one to save her.",
      "M": "the man came upon her in the open country, and even if the betrothed woman cried out, there was no one to rescue her.",
      "T": "he found her where no one could hear. She may well have cried out — there was simply no one there to save her. The law does not punish the powerless for their powerlessness."
    },
    "28": {
      "L": "If a man finds a young woman who is a virgin, who is not betrothed, and seizes her and lies with her, and they are found,",
      "M": "If a man finds an unbetrothed virgin, forces himself on her, and they are discovered,",
      "T": "If a man assaults an unbetrothed virgin and it comes to light —"
    },
    "29": {
      "L": "then the man who lay with her shall give to the father of the young woman fifty shekels of silver, and she shall be his wife, because he has violated her. He may not divorce her all his days.",
      "M": "the man must pay her father fifty shekels of silver and marry her. Because he violated her, he may never divorce her.",
      "T": "he must pay fifty shekels to her father and take her as his wife — and he can never divorce her. He has forced a permanent obligation on himself. She is provided for; he is bound. The law makes him responsible for what he chose to destroy."
    },
    "30": {
      "L": "A man shall not take his father's wife, nor shall he uncover his father's skirt.",
      "M": "A man must not marry his father's wife or violate his father's marital rights.",
      "T": "A father's wife is off-limits to his son — to take her is to violate the father's honor and the integrity of his household. The skirt is a symbol of covenantal possession; to uncover it is to claim what is not yours."
    }
  },
  "23": {
    "1": {
      "L": "No one who is emasculated by crushing or cutting shall enter the assembly of the LORD.",
      "M": "No one who has been emasculated — whether by crushing or by cutting — may enter the assembly of the LORD.",
      "T": "A man who has been physically emasculated may not enter the congregation of the LORD. The assembly is constituted by wholeness; certain conditions mark a boundary between that sacred gathering and the world outside."
    },
    "2": {
      "L": "No one of illegitimate birth shall enter the assembly of the LORD; not even to the tenth generation shall any of his descendants enter the assembly of the LORD.",
      "M": "No one born of a forbidden union may enter the assembly of the LORD — not even down to the tenth generation.",
      "T": "One born of a union that violated the covenant boundaries of Israel may not enter the assembly — nor may his descendants, to the tenth generation. These exclusions are not expressions of cruelty; they mark the boundaries that defined Israel as a distinct people before God."
    },
    "3": {
      "L": "No Ammonite or Moabite shall enter the assembly of the LORD. Even to the tenth generation, none of them shall enter the assembly of the LORD forever,",
      "M": "No Ammonite or Moabite may enter the assembly of the LORD — not even to the tenth generation; never, for all time —",
      "T": "Ammonites and Moabites are permanently excluded from Israel's assembly — down to the tenth generation, which is to say: forever —"
    },
    "4": {
      "L": "because they did not meet you with bread and water on the way when you came out of Egypt, and because they hired against you Balaam the son of Beor from Pethor of Mesopotamia, to curse you.",
      "M": "because they refused to provide you with food and water when you came out of Egypt, and because they hired Balaam son of Beor from Pethor in Mesopotamia to curse you.",
      "T": "because they refused the basic hospitality due to travelers when Israel came through the wilderness, and because they paid Balaam of Pethor to curse Israel. Both acts were calculated hostility toward God's covenant people."
    },
    "5": {
      "L": "But the LORD your God would not listen to Balaam. Instead the LORD your God turned the curse into a blessing for you, because the LORD your God loved you.",
      "M": "But the LORD your God refused to listen to Balaam and turned the curse into a blessing for you, because the LORD your God loves you.",
      "T": "Balaam's mouth opened to curse — and blessing came out instead, because the LORD would not let a hired word override his love for Israel. Every syllable Balaam spoke was redirected. This is the LORD's authority over the words of his enemies."
    },
    "6": {
      "L": "You shall not seek their peace or their prosperity all your days forever.",
      "M": "Never seek their friendship or wellbeing as long as you live.",
      "T": "Israel is not to seek treaties, alliances, or neighborly goodwill with Ammon or Moab. The hostility they showed was not accidental — it was an act against the covenant, and it is remembered permanently."
    },
    "7": {
      "L": "You shall not abhor an Edomite, for he is your brother. You shall not abhor an Egyptian, because you were a sojourner in his land.",
      "M": "Do not despise an Edomite — he is your brother. Do not despise an Egyptian — you lived as a foreigner in his land.",
      "T": "But do not hate the Edomite — Esau's children are Jacob's blood kin. And do not hate the Egyptian — even though Egypt enslaved you, you once lived as guests in their land. Israel's memory of suffering does not license hatred of every people who once wronged them."
    },
    "8": {
      "L": "Children born to them in the third generation may enter the assembly of the LORD.",
      "M": "Their descendants in the third generation may enter the assembly of the LORD.",
      "T": "Their grandchildren — raised within Israel, shaped by its life — may join the assembly. The exclusion is not eternal for Edom and Egypt as it is for Ammon and Moab. Grace outlasts grievance."
    },
    "9": {
      "L": "When you are encamped against your enemies, you shall keep yourself from every evil thing.",
      "M": "When you are camped against an enemy, keep yourself from every form of evil.",
      "T": "The camp is a holy space — the LORD is present in it. Everything in it must reflect that holiness, even in the midst of war."
    },
    "10": {
      "L": "If any man among you becomes unclean because of a nocturnal emission, he shall go outside the camp. He shall not come inside the camp.",
      "M": "If any man becomes ceremonially unclean from a nocturnal emission, he must leave the camp and stay outside.",
      "T": "A man rendered ritually unclean by a nocturnal emission must remove himself from the camp. The presence of the LORD demands purity — not because the body is shameful, but because the holy is set apart from the ordinary."
    },
    "11": {
      "L": "But when evening comes, he shall wash himself in water, and when the sun has set, he may come inside the camp.",
      "M": "At evening he shall wash with water, and after sunset he may return to the camp.",
      "T": "At sunset, after bathing, he may return. The exclusion is temporary, the restoration is full."
    },
    "12": {
      "L": "You shall have a place outside the camp to which you go out.",
      "M": "Designate an area outside the camp where you can go to relieve yourself.",
      "T": "Even basic sanitation is ordered around the holiness of the camp — nothing defiling belongs inside the perimeter where the LORD walks."
    },
    "13": {
      "L": "And you shall have a trowel with your tools, and when you sit down outside you shall dig a hole with it and turn back and cover up your excrement.",
      "M": "Carry a small trowel as part of your gear; when you sit down outside, dig a hole and cover your waste when you are done.",
      "T": "Every soldier carries a digging tool. What is unclean is buried, covered, returned to the earth. The camp remains clean — not merely for hygiene, but because the LORD is present."
    },
    "14": {
      "L": "Because the LORD your God walks in the midst of your camp to deliver you and to give up your enemies before you, therefore your camp must be holy, so that he may not see anything indecent among you and turn away from you.",
      "M": "For the LORD your God moves throughout your camp to protect you and to hand your enemies over to you. Your camp must be holy, so that he does not see anything offensive and withdraw from you.",
      "T": "Here is the reason behind all these rules: the LORD himself walks through your camp — to protect, to deliver, to give you victory. His presence is your greatest military asset. But he will not stay where he sees filth and disorder. Keep the camp holy, or risk losing the one advantage that actually wins wars."
    },
    "15": {
      "L": "You shall not hand over to his master a slave who has escaped from his master to you.",
      "M": "Do not return a runaway slave to his master if he has sought refuge with you.",
      "T": "If an enslaved person escapes and reaches you — do not send him back. This law stood against the standard of nearly every surrounding culture, which mandated return. Israel's law grants the escaped slave sanctuary."
    },
    "16": {
      "L": "He shall dwell with you in your midst, in the place that he chooses in one of your towns, wherever it suits him. You shall not oppress him.",
      "M": "Let him live with you in whatever town he chooses, wherever suits him best. Do not mistreat him.",
      "T": "Let him settle where he wishes — he chooses his own place, his own town, his own future. The same people commanded not to oppress the foreigner are here commanded not to oppress the escaped slave. Freedom, once extended, must be real."
    },
    "17": {
      "L": "There shall be no female cult prostitute among the daughters of Israel, and there shall be no male cult prostitute among the sons of Israel.",
      "M": "No Israelite woman shall become a cult prostitute, and no Israelite man shall become a cult prostitute.",
      "T": "No Israelite — male or female — may serve as a cult prostitute. This was a feature of Canaanite worship, where sexual activity was woven into the worship of fertility deities. It is categorically off-limits for Israel."
    },
    "18": {
      "L": "You shall not bring the fee of a female prostitute or the wages of a male prostitute into the house of the LORD your God in payment for any vow, for both of these are an abomination to the LORD your God.",
      "M": "Do not bring the earnings of a prostitute or the wages of a male prostitute into the house of the LORD your God as an offering for any vow — both are an abomination to the LORD.",
      "T": "Money earned through cult prostitution cannot be laundered into an act of worship. You cannot make an abomination holy by donating its profits. Both the act and the money that comes from it are detestable to the LORD."
    },
    "19": {
      "L": "You shall not charge your brother interest — interest on money, interest on food, interest on anything that is lent for interest.",
      "M": "Do not charge a fellow Israelite interest on money, food, or anything else lent at interest.",
      "T": "Do not charge interest to a fellow Israelite on any loan — whether money, food, or anything else. The covenant community is not a market where profit is extracted from those in need."
    },
    "20": {
      "L": "You may charge a foreigner interest, but you may not charge your brother interest, so that the LORD your God may bless you in all that you undertake in the land that you are entering to take possession of it.",
      "M": "You may charge a foreigner interest, but not your fellow Israelite — so that the LORD your God may bless everything you put your hand to in the land you are about to possess.",
      "T": "A foreigner outside the covenant community is a different matter; commercial lending at interest is permissible there. But within Israel, interest-bearing loans exploit the vulnerable — and the LORD's blessing flows to communities that refuse to do so."
    },
    "21": {
      "L": "When you vow a vow to the LORD your God, you shall not delay fulfilling it, for the LORD your God will surely require it of you, and you will be guilty of sin.",
      "M": "When you make a vow to the LORD your God, do not delay in fulfilling it — the LORD will hold you to it, and delay makes you guilty.",
      "T": "A vow made to the LORD is not a conditional intention — it is a binding oath. God keeps his word; he expects the same from those who invoke his name. Delay is not neutral; it is a form of dishonesty before God."
    },
    "22": {
      "L": "But if you refrain from vowing, you will not be guilty of sin.",
      "M": "But if you choose not to make a vow at all, you incur no guilt.",
      "T": "Silence is no sin. The law does not demand vows — it only demands that vows made be kept. Better not to promise than to promise and fail."
    },
    "23": {
      "L": "You shall be careful to do what has passed your lips, for you have freely vowed to the LORD your God what you have promised with your mouth.",
      "M": "Be careful to do what you have promised, for you have made a freewill vow to the LORD your God with your own mouth.",
      "T": "Your words before God have weight. What you have freely spoken, you must freely perform. The integrity of your speech is the integrity of your character."
    },
    "24": {
      "L": "When you go into your neighbor's vineyard, you may eat your fill of grapes, as many as you want, but you shall not put any in your bag.",
      "M": "When you enter your neighbor's vineyard, you may eat your fill of grapes — as many as you like — but you may not take any away in a container.",
      "T": "A traveler may eat grapes from a neighbor's vineyard — hospitality is built into the law. But filling a bag to take away crosses the line from receiving hospitality to taking property. Eat here, take nothing home."
    },
    "25": {
      "L": "When you go into your neighbor's standing grain, you may pluck ears with your hand, but you shall not put a sickle to your neighbor's standing grain.",
      "M": "When you walk through a neighbor's standing grain, you may pluck heads of grain by hand, but do not put a sickle to the grain.",
      "T": "The same principle applies to grain fields: hunger may be satisfied by hand, one ear at a time — but bring a sickle and you are harvesting someone else's crop. The law draws a line between meeting need and making profit."
    }
  },
  "24": {
    "1": {
      "L": "When a man takes a wife and marries her, if then she finds no favor in his eyes because he has found something indecent in her, and he writes her a certificate of divorce and puts it in her hand and sends her out of his house, and she departs out of his house,",
      "M": "If a man marries a woman and she finds no favor with him because he discovers some indecency in her, he shall write her a certificate of divorce, hand it to her, and send her out of his house.",
      "T": "If a man marries a woman, finds some ground of objection, and decides to end the marriage, he must give her a written certificate of divorce — a formal, legal document that places the dissolution on record and gives her the freedom to remarry. This law does not endorse easy divorce; it regulates it and protects her."
    },
    "2": {
      "L": "and when she departs out of his house she may go and become another man's wife,",
      "M": "Once she has left his house, she is free to marry another man.",
      "T": "With the certificate in hand, she is legally free. She may marry again."
    },
    "3": {
      "L": "and if the latter husband hates her and writes her a certificate of divorce and puts it in her hand and sends her out of his house, or if the latter husband dies who took her to be his wife,",
      "M": "But if her second husband also turns against her and divorces her, or if the second husband dies,",
      "T": "And if the second marriage also ends — either by divorce or the husband's death —"
    },
    "4": {
      "L": "then her former husband, who sent her away, may not take her again to be his wife after she has been defiled. For that is an abomination before the LORD. And you shall not bring sin upon the land that the LORD your God is giving you for an inheritance.",
      "M": "her first husband may not take her back as his wife after she has been with another man — that is detestable before the LORD. Do not bring sin upon the land the LORD your God is giving you as your inheritance.",
      "T": "her first husband cannot remarry her. The marriage was formally dissolved; she entered another union; she has passed beyond what the first marriage could claim. To take her back now is an abomination — it reduces her to a commodity that can be traded and reclaimed at will. The land would be defiled by it."
    },
    "5": {
      "L": "When a man is newly married, he shall not go out with the army or be liable for any other public duty. He shall be free at home one year to bring joy to his wife whom he has taken.",
      "M": "When a man has recently married, he shall not serve in the army or be required for any public service. He shall be free at home for one year to bring happiness to the wife he has married.",
      "T": "A newly married man is exempt from military service and civic obligations for a full year. The point is not to give him a holiday — it is to let a marriage take root. A new household is a new covenant; it deserves time to form. The law builds this in."
    },
    "6": {
      "L": "No one shall take a mill or an upper millstone in pledge, for that would be taking a life in pledge.",
      "M": "Do not take a mill or a millstone as collateral for a loan — that would be seizing someone's livelihood as a pledge.",
      "T": "The mill grinds the flour that feeds the household. To take it as collateral is to take the family's daily bread — to take a life in pledge. The law forbids it: a creditor's rights end where basic survival begins."
    },
    "7": {
      "L": "If a man is found stealing a person from among his brothers, the sons of Israel, and treating him as a slave or selling him, that thief shall die. So you shall purge the evil from your midst.",
      "M": "If someone is caught kidnapping a fellow Israelite — treating him as a slave or selling him — that thief shall be put to death. Purge the evil from your midst.",
      "T": "Kidnapping and selling a fellow Israelite is a capital crime. To reduce a covenant brother to merchandise — to traffic in human beings — is the worst kind of theft, one that strikes at a person's very self. Death for the trafficker, freedom for the community. Purge the evil."
    },
    "8": {
      "L": "Take care, in cases of leprous disease, to be very careful to do according to all that the Levitical priests instruct you. As I commanded them, so you shall be careful to do.",
      "M": "In cases of skin disease, be very careful to follow exactly what the Levitical priests direct you. Carry out faithfully what I commanded them.",
      "T": "When it comes to skin disease, do not improvise. The priests have received specific instruction about diagnosis, quarantine, and restoration — follow it. The health of the community depends on proper procedure, and only the priests are authorized to adjudicate it."
    },
    "9": {
      "L": "Remember what the LORD your God did to Miriam on the way as you came out of Egypt.",
      "M": "Remember what the LORD your God did to Miriam on the journey out of Egypt.",
      "T": "Remember Miriam — she challenged Moses, and the LORD struck her with leprosy. Even the prophetess, even Moses's own sister, was not exempt from the consequences of rebellion and the protocols of disease. No one is above the law of the community's purity."
    },
    "10": {
      "L": "When you make your neighbor a loan of any sort, you shall not go into his house to collect his pledge.",
      "M": "When you make a loan to your neighbor, do not go into his home to take his pledge.",
      "T": "When you lend to a neighbor, do not step inside his house to seize the collateral yourself. His home is the last space of dignity he controls — respect it."
    },
    "11": {
      "L": "You shall stand outside, and the man to whom you make the loan shall bring the pledge out to you.",
      "M": "Stand outside and let him bring you his pledge.",
      "T": "Stand at the door. Let him choose what to offer. The borrower retains that much agency — the creditor does not ransack his home."
    },
    "12": {
      "L": "And if he is a poor man, you shall not sleep with his pledge.",
      "M": "If he is poor, do not keep his pledge overnight.",
      "T": "If the man is poor, the cloak he gave you as collateral may be all he has to sleep in. Do not keep it through the night."
    },
    "13": {
      "L": "You shall restore to him the pledge as the sun sets, so that he may sleep in his cloak and bless you. And it shall be righteousness for you before the LORD your God.",
      "M": "Return his cloak at sunset so he can sleep warmly. He will bless you, and it will count as righteousness before the LORD your God.",
      "T": "Return it at sunset. He sleeps warm; he blesses you; and that act of mercy is credited to you as righteousness before the LORD. The law is specific here because mercy must be specific — general compassion that forgets the cold night is no compassion at all."
    },
    "14": {
      "L": "You shall not oppress a hired worker who is poor and needy, whether he is one of your brothers or one of the sojourners who are in your land within your towns.",
      "M": "Do not mistreat a poor and needy hired worker — whether he is a fellow Israelite or a foreigner living in one of your towns.",
      "T": "A day laborer — whether Israelite or immigrant — is among the most vulnerable people in the community: no permanent employment, no reserves, no leverage. Do not exploit that vulnerability."
    },
    "15": {
      "L": "You shall give him his wages on the same day, before the sun goes down — for he is poor and sets his heart on it. Lest he cry against you to the LORD, and you bear sin.",
      "M": "Pay his wages the same day, before sunset — he is poor and counting on it. If you withhold them and he cries out to the LORD, you will be guilty of sin.",
      "T": "Pay him the day he works, before the sun goes down. He has nothing to fall back on; that wage is what he needs tonight. Withhold it and his cry reaches the LORD — and that cry brings guilt on you. The law does not wait for court proceedings; it moves at the speed of a laborer's need."
    },
    "16": {
      "L": "Fathers shall not be put to death for the sins of their children, nor children be put to death for the sins of their fathers. Each person shall be put to death for his own sin.",
      "M": "Parents shall not be put to death for the sins of their children, and children shall not be put to death for the sins of their parents. Each person shall be executed only for his own sin.",
      "T": "Each person answers for his own sin — not for his father's, not for his children's. This verse enshrines individual moral accountability in law: guilt is personal, not inherited. It was a watershed moment in ancient jurisprudence, standing against blood-feud logic and collective punishment."
    },
    "17": {
      "L": "You shall not pervert the justice due to the sojourner or to the fatherless, or take a widow's garment in pledge.",
      "M": "Do not deprive the foreigner or the fatherless of justice, or take a widow's garment as collateral.",
      "T": "Three categories of the powerless — the foreigner, the orphan, the widow — must receive full justice without distortion. And a widow's cloak is not to be taken as collateral; she has already lost enough."
    },
    "18": {
      "L": "But you shall remember that you were a slave in Egypt and the LORD your God redeemed you from there. Therefore I command you to do this.",
      "M": "Remember that you were a slave in Egypt and the LORD your God redeemed you. That is why I give you this command.",
      "T": "You know what it is to be powerless. You know what it is to be exploited. You know what it is to have no advocate. The LORD rescued you from that place. Now live in a way that shows you remember — become the advocate you once needed."
    },
    "19": {
      "L": "When you reap your harvest in your field and forget a sheaf in the field, you shall not go back to get it. It shall be for the sojourner, the fatherless, and the widow, that the LORD your God may bless you in all the work of your hands.",
      "M": "When you harvest your field and leave a sheaf behind, do not go back for it — leave it for the foreigner, the fatherless, and the widow. The LORD your God will bless you for it in everything you do.",
      "T": "If you leave a sheaf in the field at harvest time, leave it. It is not yours to reclaim — it belongs to the foreigner, the orphan, the widow who gleans after you. The law formalizes generosity, building it into the agricultural calendar so that the poor eat whether or not the owner feels charitable that day."
    },
    "20": {
      "L": "When you beat your olive trees, you shall not go over them again. It shall be for the sojourner, the fatherless, and the widow.",
      "M": "When you have beaten the olives off your trees, do not go back for what is left — it belongs to the foreigner, the fatherless, and the widow.",
      "T": "When you beat the olive trees, one pass is all you take. What remains on the branches after you go — that is the share of those who have no trees of their own."
    },
    "21": {
      "L": "When you gather the grapes of your vineyard, you shall not strip it afterward. It shall be for the sojourner, the fatherless, and the widow.",
      "M": "When you harvest your vineyard, do not go back for every last bunch — leave the remainder for the foreigner, the fatherless, and the widow.",
      "T": "One harvest through the vineyard, then leave. What hangs behind on the vines is already spoken for — it belongs to the vulnerable. The harvest is not measured by what you can strip; it is measured by what you freely leave."
    },
    "22": {
      "L": "You shall remember that you were a slave in the land of Egypt. Therefore I command you to do this.",
      "M": "Remember that you were a slave in Egypt. That is why I am giving you this command.",
      "T": "And again: remember Egypt. Memory of suffering is the engine of mercy. The law does not appeal to abstract duty; it appeals to lived experience. You were the vulnerable one. Now make sure someone else finds the gleaning waiting for them when they come behind you."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'deuteronomy')
        merge_tier(existing, DEUTERONOMY, tier_key)
        save(tier_dir, 'deuteronomy', existing)
    print('Deuteronomy 19–24 written.')

if __name__ == '__main__':
    main()
