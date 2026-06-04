"""
MKT 1 Samuel chapters 13–15 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1samuel-13-15.py

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — small-caps convention maintained per prior scripts.
- H430 (אֱלֹהִים): "God" throughout — all references unambiguously the God of Israel.
- H2617 (חֶסֶד): 15:6 — "kindness" (L), "loyalty" (M), "covenant faithfulness" (T). The Kenites
  showed chesed to Israel at the exodus; the term carries covenant-loyalty force, not mere civility.
- H5057 (נגיד): 13:14 — "captain" (L), "ruler" (M), "leader" (T) — same convention as prior scripts;
  the nagid word signals shepherding appointment distinct from the popularly demanded melek.
- H4428 (מלך): "king" throughout all tiers.
- H2763 (חָרַם / חֶרֶם): The ban/herem in ch. 15 — "utterly destroy" (L), "completely destroy" (M),
  "devote to destruction / place under the ban" (T). This is a technical term for sacred warfare
  consecration; Saul's selective application of it is the theological heart of ch. 15.
- H5162 (נחם): 15:11, 15:35 — "repent" (L), "regret" (M), "grieve" (T). Hebrew uses the same root
  for God's grief over Saul as for human repentance. In T the emotional register is surfaced. Note:
  v. 29 uses a different Hebrew root (H5331 / H5162 in negation) to say God does NOT repent — the
  tension is deliberate and theologically significant.
- H5331 (נֵצַח): 15:29 — "Strength of Israel" (L), "Eternal One of Israel" (M), "Enduring One of
  Israel" (T) — a divine title used only here in this form, grounding Samuel's declaration that the
  divine word about Saul is irrevocable.
- H7307 (רוּחַ): Not present in these chapters.
- Aspect notes: narrative waw-consecutive imperfects rendered as English past tense throughout.
  Jonathan's raid verbs (14:13) use perfective forms — sudden, completed acts in rapid sequence.
- Textual-critical notes:
  (1) 13:1 — The MT is corrupt: the Hebrew reads "a son of a year Saul in his reigning and two years
      he reigned." The numbers are clearly incomplete; scribal haplography dropped the originals.
      Rendered honestly in L/M; T surfaces the textual problem.
  (2) 14:18 — MT reads "the ark of God"; LXX reads "the ephod." The ephod makes better sense
      (the ark was at Kiriath-jearim; the ephod is the divination instrument); T notes this variant.
  (3) 14:41 — LXX preserves a much longer text here (likely lost by homoioteleuton in MT). The MT
      "give a perfect lot" probably abbreviates the Urim/Thummim inquiry. T notes this.
  (4) 14:47 — H7561 (rasha in Hiphil) normally means "act wickedly"; used here to mean "he
      prevailed" — likely a textual difficulty or unusual idiom. T notes the problem.
  (5) 15:32 — Agag's last words are ambiguous: "The bitterness of death is surely past" may be
      confident relief or terrified resignation. T preserves the ambiguity.
  (6) Divine sorrow in 15:11 vs. divine constancy in 15:29 — the tension is intentional in the
      Hebrew and carried forward in all three tiers.
- OT intertextuality: 15:22 ("to obey is better than sacrifice") is cited in Mark 12:33 and is one
  of the pivotal prophetic axioms reshaping Israel's understanding of cult and ethics.
- Honor-shame: 15:30 — Saul's repeated plea is driven as much by shame avoidance (honor before the
  elders) as by genuine repentance. T surfaces this cultural dynamic explicitly.
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

SAMUEL = {
  "13": {
    "1": {
      "L": "A year old was Saul when he became king, and two years he reigned over Israel.",
      "M": "Saul was [a year] old when he became king and reigned [two] years over Israel.",
      "T": "The record of Saul's reign opens with a corrupted text: the MT reads that he was 'a year old' at his accession and ruled two years—both numbers are almost certainly incomplete, the originals lost by scribal error."
    },
    "2": {
      "L": "And Saul chose for himself three thousand men of Israel; two thousand were with Saul in Michmash and in the hill country of Bethel, and a thousand were with Jonathan in Gibeah of Benjamin; and the rest of the people he sent each man to his tent.",
      "M": "Saul selected three thousand men from Israel: two thousand were with him at Michmash and in the hill country of Bethel, and a thousand were with Jonathan at Gibeah of Benjamin. The rest of the troops he dismissed to their homes.",
      "T": "Saul organized a standing force of three thousand: two thousand with him at Michmash and the Bethel highlands, one thousand with Jonathan at Gibeah. The rest he sent home, keeping only this select corps."
    },
    "3": {
      "L": "And Jonathan smote the garrison of the Philistines that was in Geba; and the Philistines heard of it. And Saul blew the trumpet throughout all the land, saying, 'Let the Hebrews hear!'",
      "M": "Jonathan struck the Philistine garrison at Geba, and the Philistines heard of it. Saul had the trumpet blown throughout the whole land with the announcement: 'Let the Hebrews take notice!'",
      "T": "Jonathan struck the first blow—he hit the Philistine garrison at Geba. When word reached the Philistines, Saul had the alarm sounded across the whole land: 'Let every Hebrew know what has been done!'"
    },
    "4": {
      "L": "And all Israel heard, saying, 'Saul has struck a garrison of the Philistines, and also Israel has made itself odious among the Philistines.' And the people were called together after Saul to Gilgal.",
      "M": "All Israel heard the report: 'Saul has struck a Philistine garrison, and Israel has become repugnant to the Philistines.' The people rallied to Saul at Gilgal.",
      "T": "The news spread across Israel: 'Saul has hit the Philistines—and now Israel has made itself unbearable to them.' The people streamed to Saul at Gilgal, sensing the storm about to break."
    },
    "5": {
      "L": "And the Philistines gathered themselves together to fight with Israel, thirty thousand chariots and six thousand horsemen, and people as the sand which is on the seashore in multitude; and they came up and encamped in Michmash, eastward of Beth-aven.",
      "M": "The Philistines mustered to fight Israel: thirty thousand chariots, six thousand cavalry, and foot soldiers as numerous as the sand on the seashore. They marched up and encamped at Michmash, east of Beth-aven.",
      "T": "The Philistine response was overwhelming: thirty thousand chariots, six thousand cavalry, and infantry beyond counting—like sand on the shore. They massed at Michmash east of Beth-aven, blocking the highland passes."
    },
    "6": {
      "L": "When the men of Israel saw that they were in a strait—for the people were hard pressed—the people hid themselves in caves and in thickets and in rocks and in tombs and in pits.",
      "M": "The men of Israel saw they were in desperate straits; under severe pressure, the troops hid in caves, thickets, rocks, cellars, and cisterns.",
      "T": "The Israelites took one look at the odds and panicked. The army dissolved into the landscape—men hiding in caves, thickets, rocky crags, tombs, and dry cisterns."
    },
    "7": {
      "L": "And some Hebrews crossed over the Jordan to the land of Gad and Gilead; and as for Saul, he was yet in Gilgal, and all the people who followed him were trembling.",
      "M": "Some Hebrews crossed the Jordan into the land of Gad and Gilead. Saul remained at Gilgal, and those who stayed with him were trembling.",
      "T": "Some Israelites fled across the Jordan into Gad and Gilead. Saul held his position at Gilgal, but even the men who stayed with him were shaking."
    },
    "8": {
      "L": "And he waited seven days, according to the set time that Samuel had appointed; but Samuel came not to Gilgal, and the people were scattering from him.",
      "M": "He waited seven days—the time Samuel had appointed—but Samuel did not come to Gilgal, and the people kept deserting him.",
      "T": "Seven days Saul waited—exactly the time Samuel had fixed. Samuel did not come. As the days wore on, the men began slipping away."
    },
    "9": {
      "L": "And Saul said, 'Bring the burnt offering to me, and the peace offerings.' And he offered the burnt offering.",
      "M": "Saul commanded, 'Bring me the burnt offering and the fellowship offerings.' And he offered the burnt offering himself.",
      "T": "Saul made the decision: 'Bring the burnt offering and the peace offerings.' He offered the burnt offering with his own hands."
    },
    "10": {
      "L": "And it came to pass that as soon as he had finished offering the burnt offering, behold, Samuel came; and Saul went out to meet him to greet him.",
      "M": "Just as he finished presenting the burnt offering, Samuel arrived. Saul went out to meet and greet him.",
      "T": "The moment Saul finished the offering, Samuel came into view. Saul went out to meet him with a greeting—but the encounter would not go as he imagined."
    },
    "11": {
      "L": "And Samuel said, 'What have you done?' And Saul said, 'Because I saw that the people were scattering from me, and that you came not within the days appointed, and that the Philistines had gathered themselves in Michmash—'",
      "M": "Samuel demanded, 'What have you done?' Saul replied, 'I saw the people deserting me; you did not come within the appointed time; and the Philistines had massed at Michmash—'",
      "T": "Samuel's first words were a demand: 'What have you done?' Saul answered with his reasoning: 'The men were abandoning me. You hadn't arrived at the set time. And the Philistines were assembling at Michmash—'"
    },
    "12": {
      "L": "And I said, 'Now the Philistines will come down upon me at Gilgal, and I have not sought the favor of the LORD.' So I compelled myself and offered the burnt offering.",
      "M": "'—so I thought: the Philistines will attack at Gilgal and I have not sought the LORD's favor. I felt forced to act and offered the burnt offering.'",
      "T": "'—and I thought: the Philistines will come down on us here at Gilgal and I haven't sought the LORD's help yet. So I forced myself and offered the burnt offering.' Saul's logic was impeccable; his obedience was not."
    },
    "13": {
      "L": "And Samuel said to Saul, 'You have acted foolishly. You have not kept the commandment of the LORD your God which he commanded you; for now would the LORD have established your kingdom over Israel for ever.'",
      "M": "Samuel said to Saul, 'You have acted foolishly. You did not keep the commandment of the LORD your God that he gave you—for if you had, the LORD would have established your dynasty over Israel forever.'",
      "T": "Samuel's verdict was unsparing: 'You have acted like a fool. You did not keep the LORD your God's command. Had you obeyed, the LORD would have secured your dynasty over Israel permanently. The throne would have been your family's without end.'"
    },
    "14": {
      "L": "But now your kingdom shall not continue; the LORD has sought for himself a man after his own heart, and the LORD has commanded him to be captain over his people, because you have not kept what the LORD commanded you.",
      "M": "But now your kingdom will not endure. The LORD has sought out a man after his own heart and appointed him as ruler over his people, because you have not kept what the LORD commanded you.",
      "T": "Your dynasty is over before it has begun. The LORD has already found the man he wants—a man whose heart is shaped like his own—and has designated him as Israel's leader. Your disobedience forfeited what might have been."
    },
    "15": {
      "L": "And Samuel arose and went up from Gilgal unto Gibeah of Benjamin. And Saul numbered the people that were present with him—about six hundred men.",
      "M": "Samuel arose and went from Gilgal up to Gibeah of Benjamin. Saul counted the men still with him—about six hundred.",
      "T": "Samuel turned and went up from Gilgal to Gibeah of Benjamin, leaving Saul standing with his depleted force. When Saul counted the men still with him, there were only about six hundred."
    },
    "16": {
      "L": "And Saul and Jonathan his son, and the people that were present with them, remained in Gibeah of Benjamin; but the Philistines encamped in Michmash.",
      "M": "Saul, his son Jonathan, and the troops remaining with them stayed at Gibeah of Benjamin, while the Philistines were encamped at Michmash.",
      "T": "Saul and Jonathan held Gibeah of Benjamin with their six hundred. Across the ridge, the Philistine host sprawled across Michmash."
    },
    "17": {
      "L": "And the spoilers came out from the camp of the Philistines in three companies; one company turned toward the way of Ophrah, to the land of Shual,",
      "M": "Raiding parties went out from the Philistine camp in three detachments: one went toward the road to Ophrah in the land of Shual,",
      "T": "The Philistines then sent three raiding columns out of the main camp: one struck toward Ophrah and the Shual district,"
    },
    "18": {
      "L": "and one company turned toward the way of Beth-horon, and one company turned toward the border that looks down upon the valley of Zeboim toward the wilderness.",
      "M": "one turned toward the road to Beth-horon, and one turned toward the border overlooking the valley of Zeboim in the direction of the wilderness.",
      "T": "a second swept toward Beth-horon, and a third veered to the ridge overlooking the valley of Zeboim toward the desert."
    },
    "19": {
      "L": "Now there was no smith found throughout all the land of Israel; for the Philistines had said, 'Lest the Hebrews make swords or spears.'",
      "M": "There was not a metalworker to be found anywhere in Israel, because the Philistines had said, 'Otherwise the Hebrews will make swords or spears.'",
      "T": "The Philistines had enforced a total iron monopoly: not a single blacksmith worked in all of Israel—they had forbidden it, fearing the Israelites would forge weapons."
    },
    "20": {
      "L": "But all the Israelites went down to the Philistines, every man to sharpen his plowshare and his mattock and his axe and his sickle.",
      "M": "So every Israelite had to go down to the Philistines to have his plowshare, mattock, axe, or sickle sharpened.",
      "T": "Every Israeli farmer was forced to go to Philistine smiths to get his tools sharpened—completely at their mercy."
    },
    "21": {
      "L": "The charge was a pim for the plowshares and for the mattocks, and a third of a shekel for sharpening the axes and for setting the ox-goads.",
      "M": "The price was two-thirds of a shekel for the plowshares and mattocks, and a third of a shekel for sharpening the axes and setting the goads.",
      "T": "The Philistines charged a pim—about two-thirds of a shekel—for the larger tools and a third shekel for axe-sharpening and resetting the ox-goads. Even maintenance was taxed."
    },
    "22": {
      "L": "So it came to pass in the day of battle that there was neither sword nor spear found in the hand of any of the people that were with Saul and Jonathan; but with Saul and with Jonathan his son was there found.",
      "M": "When the day of battle came, not one soldier in Saul and Jonathan's force had a sword or a spear—only Saul and Jonathan themselves were armed.",
      "T": "When the battle finally arrived, not one man in the Israelite army had a sword or spear. Only Saul and Jonathan were properly armed—the army was fighting with farm tools."
    },
    "23": {
      "L": "And the garrison of the Philistines went out to the pass of Michmash.",
      "M": "The Philistine garrison advanced to hold the pass of Michmash.",
      "T": "Meanwhile, the Philistine garrison moved to occupy the pass at Michmash—controlling the only route into the highlands."
    }
  },
  "14": {
    "1": {
      "L": "Now it came to pass upon a day that Jonathan the son of Saul said to the young man that bore his armor, 'Come, let us go over to the Philistines' garrison that is on the other side.' But he did not tell his father.",
      "M": "One day Jonathan said to his armor-bearer, 'Come, let us cross over to the Philistine garrison on the other side.' He did not tell his father.",
      "T": "On an impulse, Jonathan said to his armor-bearer, 'Come—let's cross over to the Philistine garrison on the other side.' He kept it from his father."
    },
    "2": {
      "L": "Now Saul was staying in the outskirts of Gibeah under the pomegranate tree that is in Migron; and the people who were with him were about six hundred men.",
      "M": "Saul was stationed at the edge of Gibeah under the pomegranate tree at Migron, with about six hundred men.",
      "T": "Saul, meanwhile, sat beneath the pomegranate tree at Migron on the outskirts of Gibeah—waiting with his six hundred, unaware of what his son was doing."
    },
    "3": {
      "L": "And Ahijah son of Ahitub, the brother of Ichabod son of Phinehas son of Eli, the priest of the LORD at Shiloh, was wearing an ephod. And the people did not know that Jonathan had gone.",
      "M": "Ahijah son of Ahitub—brother of Ichabod, son of Phinehas, son of Eli, the LORD's priest at Shiloh—was there wearing the ephod. No one in camp knew Jonathan had slipped away.",
      "T": "With Saul was Ahijah the priest—grandson of Eli, nephew of the ill-fated Ichabod, wearing the priestly ephod. No one in the camp knew Jonathan had gone."
    },
    "4": {
      "L": "And between the passes by which Jonathan sought to cross over to the Philistines' garrison, there was a sharp crag on one side and a sharp crag on the other side; the name of the one was Bozez and the name of the other Seneh.",
      "M": "Between the two passes that Jonathan planned to cross to reach the Philistine garrison stood two sharp rock crags—one called Bozez and the other Seneh.",
      "T": "Jonathan's chosen route to the Philistine garrison passed between two jagged outcrops—Bozez and Seneh. The terrain was as treacherous as the plan."
    },
    "5": {
      "L": "The one crag was situated to the north, over against Michmash, and the other to the south, over against Gibeah.",
      "M": "The northern crag faced Michmash; the southern crag faced Gibeah.",
      "T": "One crag faced north toward Michmash; the other faced south toward Gibeah—the two enemy camps on either side of this narrow cleft."
    },
    "6": {
      "L": "And Jonathan said to the young man that bore his armor, 'Come, let us cross over to the garrison of these uncircumcised; it may be that the LORD will work for us, for there is nothing to hinder the LORD from saving by many or by few.'",
      "M": "Jonathan told his armor-bearer, 'Come, let us go over to the garrison of these uncircumcised. Perhaps the LORD will act on our behalf—nothing prevents the LORD from saving by many or by few.'",
      "T": "Jonathan said to his armor-bearer: 'Come—let's go at that garrison of the uncircumcised. The LORD may well act on our behalf. Nothing stops him from delivering through two men as easily as through thousands.'"
    },
    "7": {
      "L": "And his armor-bearer said to him, 'Do all that is in your heart. Go ahead; behold, I am with you according to your heart.'",
      "M": "His armor-bearer replied, 'Do whatever is in your heart. I am with you—whatever you decide.'",
      "T": "His armor-bearer answered simply: 'Do whatever you have in mind. I'm with you all the way.'"
    },
    "8": {
      "L": "Then Jonathan said, 'Behold, we will cross over to the men, and we will reveal ourselves to them.'",
      "M": "Jonathan said, 'Good. We will cross over to them and let ourselves be seen.'",
      "T": "'Good,' said Jonathan. 'We'll cross over and step into the open where they can see us.'"
    },
    "9": {
      "L": "If they say to us, 'Wait until we come to you,' then we will stand still in our place and will not go up to them.",
      "M": "If they say 'Stay there until we come to you'—we stop and do not advance.",
      "T": "If they say 'Hold your position while we come down to you'—then we stop and don't go up."
    },
    "10": {
      "L": "But if they say, 'Come up to us,' then we will go up; for the LORD has delivered them into our hand. And this shall be a sign to us.",
      "M": "But if they say 'Come up to us'—we go up, because the LORD has handed them over to us. That will be our sign.",
      "T": "But if they call down 'Come up!'—we go. That's the LORD's signal that he has already given them to us."
    },
    "11": {
      "L": "And both of them revealed themselves to the garrison of the Philistines; and the Philistines said, 'Behold, the Hebrews come out of the holes where they have been hiding themselves!'",
      "M": "They stepped into the open in sight of the Philistine garrison, and the Philistines called out, 'Look—the Hebrews are crawling out of the holes where they'd been hiding!'",
      "T": "They stepped into the open, visible to the Philistine sentries. 'Look!' the guards shouted. 'The Hebrews are coming out of their holes!'"
    },
    "12": {
      "L": "And the men of the garrison called to Jonathan and his armor-bearer and said, 'Come up to us, and we will show you a thing.' And Jonathan said to his armor-bearer, 'Come up after me, for the LORD has delivered them into the hand of Israel.'",
      "M": "The garrison sentries called to Jonathan and his armor-bearer: 'Come on up—we'll show you something!' Jonathan told his armor-bearer, 'Follow me. The LORD has given them to Israel.'",
      "T": "'Come on up!' the Philistine guards called down. 'We have something to show you.' The sign had come. Jonathan turned to his armor-bearer: 'Follow me. The LORD has handed them over to Israel.'"
    },
    "13": {
      "L": "And Jonathan climbed up on his hands and his feet, with his armor-bearer after him; and they fell before Jonathan, and his armor-bearer slew them after him.",
      "M": "Jonathan scrambled up the rock face on his hands and feet, with his armor-bearer right behind him. The Philistines fell before Jonathan, and his armor-bearer finished them off.",
      "T": "Jonathan went up the cliff hand over foot, his armor-bearer right behind him. The sentries fell before Jonathan, and the armor-bearer dispatched each one as he came up."
    },
    "14": {
      "L": "And that first strike which Jonathan and his armor-bearer made was about twenty men within about a half-acre of land.",
      "M": "That first assault—Jonathan and his armor-bearer—took down about twenty men in a space of roughly half an acre.",
      "T": "Twenty Philistines went down in the first strike, within an area no larger than half an acre of plowed ground."
    },
    "15": {
      "L": "And there was trembling in the camp, in the field, and among all the people; the garrison and the raiders also trembled, and the earth shook; and it became a very great trembling.",
      "M": "Terror spread through the whole Philistine force—camp, field, garrison, and raiding parties alike. The ground shook. It was a panic that came from God.",
      "T": "Then divine panic swept through the entire Philistine force—camp, garrison, raiders, outlying troops. The ground itself trembled. This was no ordinary battle fear; it was the kind of terror the LORD sends."
    },
    "16": {
      "L": "And the watchmen of Saul in Gibeah of Benjamin looked; and behold, the multitude was melting away, going here and there.",
      "M": "Saul's sentries at Gibeah of Benjamin looked out and saw the Philistine mass disintegrating—men rushing about in confusion.",
      "T": "Saul's watchmen on the heights of Gibeah of Benjamin stared: the enormous Philistine host was dissolving—men scattering in every direction."
    },
    "17": {
      "L": "Then Saul said to the people who were with him, 'Number now and see who has gone from us.' And when they had counted, behold, Jonathan and his armor-bearer were not there.",
      "M": "Saul ordered, 'Call the roll—find out who is missing.' When they checked, Jonathan and his armor-bearer were gone.",
      "T": "Saul ordered a roll call: 'Find out who's not here.' The count came back: Jonathan and his armor-bearer—gone."
    },
    "18": {
      "L": "And Saul said to Ahijah, 'Bring the ark of God here.' For the ark of God was with the children of Israel at that time.",
      "M": "Saul told Ahijah, 'Bring the ark of God.' (The ark of God was with Israel at that time.)",
      "T": "Saul called to Ahijah: 'Bring the ark of God.' The MT reads 'ark'; the LXX reads 'ephod'—and since the ark was at Kiriath-jearim, not the battlefield, the ephod reading may be original. He was seeking a divine oracle."
    },
    "19": {
      "L": "And it came to pass, while Saul was speaking to the priest, that the tumult in the camp of the Philistines went on and increased; and Saul said to the priest, 'Withdraw your hand.'",
      "M": "While Saul was still consulting the priest, the uproar from the Philistine camp kept growing louder. Saul told the priest, 'Withdraw your hand—stop.'",
      "T": "Even as Saul consulted Ahijah, the noise from the Philistine camp kept escalating. Saul cut off the ritual: 'Withdraw your hand. We're going now.'"
    },
    "20": {
      "L": "And Saul and all the people who were with him assembled and came to the battle; and behold, every man's sword was against his fellow, and there was a very great confusion.",
      "M": "Saul and all his men rallied and entered the battle. They found every Philistine's sword turned against his own comrade—massive chaos.",
      "T": "Saul and all his men charged into the battle to find it already won by God: every Philistine fighting his own ally, the whole force in self-inflicted rout."
    },
    "21": {
      "L": "Moreover the Hebrews who had been with the Philistines previously, who had gone up with them into the camp from the country round about—even they also turned to be with the Israelites who were with Saul and Jonathan.",
      "M": "The Hebrews who had previously been serving with the Philistines and had gone into their camp from the surrounding territory also switched sides and joined the Israelites under Saul and Jonathan.",
      "T": "Even the Israelites who had been pressed into Philistine service now defected back—crossing over to join Saul and Jonathan's army as the tide turned."
    },
    "22": {
      "L": "Likewise all the men of Israel who had hidden themselves in the hill country of Ephraim—when they heard that the Philistines had fled, even they also followed hard after them in the battle.",
      "M": "Similarly, all the Israelites who had been hiding in the hill country of Ephraim came out when they heard the Philistines were fleeing, and joined the hot pursuit.",
      "T": "And the men hiding throughout the Ephraim hills—when word reached them that the Philistines were in full flight—poured out to join the chase."
    },
    "23": {
      "L": "So the LORD saved Israel that day, and the battle passed over as far as Beth-aven.",
      "M": "The LORD saved Israel that day, and the fighting swept as far as Beth-aven.",
      "T": "The LORD had saved Israel that day. The battle rolled on past Beth-aven—a victory larger than any human plan had envisioned."
    },
    "24": {
      "L": "And the men of Israel were hard pressed that day; for Saul had bound the people under an oath, saying, 'Cursed be the man who eats any food until evening, until I am avenged on my enemies.' So none of the people tasted any food.",
      "M": "The Israelite troops were in desperate straits that day because Saul had put the people under an oath: 'Cursed be any man who eats food before evening, until I have taken vengeance on my enemies.' So no one ate anything.",
      "T": "The Israelite soldiers were struggling—because Saul had imposed a rash oath before the battle: 'Cursed be anyone who eats before I take vengeance on my enemies—nothing until evening.' The men fought all day on empty stomachs."
    },
    "25": {
      "L": "And all the troops came to the forest; and there was honey on the ground.",
      "M": "The whole army entered the forest, where honey was dripping on the ground.",
      "T": "As the army pushed through the forest, they came upon honey flowing across the ground."
    },
    "26": {
      "L": "And when the troops came to the forest, behold, the honey was dripping; but no man put his hand to his mouth, for the people feared the oath.",
      "M": "When they entered the forest, the honey was flowing freely—but no one lifted his hand to his mouth because they all feared the oath.",
      "T": "There it was—honey everywhere. But not one man reached for it. They feared the oath too much."
    },
    "27": {
      "L": "But Jonathan had not heard when his father charged the people with the oath; so he stretched out the end of the rod that was in his hand and dipped it in the honeycomb, and put his hand to his mouth; and his eyes brightened.",
      "M": "Jonathan had not heard his father's oath to the troops. He stretched out the tip of his staff, dipped it in the honeycomb, and ate. His eyes lit up.",
      "T": "But Jonathan had been out raiding when his father made the oath—he never heard it. He dipped the tip of his staff into the honeycomb and ate. Immediately his eyes brightened."
    },
    "28": {
      "L": "Then one of the people answered and said, 'Your father strictly charged the people with an oath, saying, Cursed be the man who eats food this day. And the people were faint.'",
      "M": "One of the soldiers told him, 'Your father bound the whole army with a strict oath: Cursed be anyone who eats today. That is why the men are exhausted.'",
      "T": "One of the soldiers explained: 'Your father laid a strict oath on the whole army—Cursed be any man who eats today! And so the men are falling on their feet.'"
    },
    "29": {
      "L": "Then Jonathan said, 'My father has troubled the land. See how my eyes have brightened because I tasted a little of this honey.'",
      "M": "Jonathan said, 'My father has brought trouble on the land. See how much better I feel from just a taste of honey.'",
      "T": "Jonathan said it plainly: 'My father has brought disaster on the army. Look—I tasted only a little honey and already my strength is returning. Think what the men could have done today if they'd been allowed to eat.'"
    },
    "30": {
      "L": "How much more, if haply the people had eaten freely today of the spoil of their enemies which they found! For had there not been now a much greater slaughter among the Philistines?",
      "M": "'How much better if the troops had been free to eat from the plunder they found! The slaughter of the Philistines would have been far greater.'",
      "T": "'If only the men had eaten their fill from the captured stores—the Philistine defeat would have been total, not partial. A rash oath cost us a complete victory.'"
    },
    "31": {
      "L": "And they struck down the Philistines that day from Michmash to Aijalon; and the people were very faint.",
      "M": "They drove the Philistines from Michmash to Aijalon that day, and the troops were utterly exhausted.",
      "T": "The Israelites pursued and struck Philistines all the way from Michmash to Aijalon—a long, hard chase—and by the end the men were completely spent."
    },
    "32": {
      "L": "And the people flew upon the spoil and took sheep and oxen and calves and slaughtered them on the ground; and the people ate them with the blood.",
      "M": "The troops swooped on the plunder, seized sheep, cattle, and calves, and slaughtered them on the ground, eating the meat with the blood still in it.",
      "T": "The starving men threw themselves on the captured livestock—slaughtering animals where they stood and eating the meat still bloody, violating the prohibition against consuming blood."
    },
    "33": {
      "L": "Then they told Saul, saying, 'Behold, the people are sinning against the LORD by eating with the blood.' And he said, 'You have acted treacherously; roll a large stone to me this day.'",
      "M": "Saul was told: 'The troops are sinning against the LORD—they are eating meat with the blood.' He said, 'You have been faithless. Roll a large stone to me right now.'",
      "T": "Saul heard the report: 'The men are sinning against the LORD—eating meat with the blood.' He acted at once: 'That is faithlessness. Roll a large stone here—now.'"
    },
    "34": {
      "L": "And Saul said, 'Disperse yourselves among the people and say to them, Bring here every man his ox and every man his sheep, and slaughter them here and eat; and do not sin against the LORD by eating with the blood.' And all the people brought every man his ox with him that night and slaughtered them there.",
      "M": "Saul commanded: 'Spread out among the troops and tell them: Bring your ox, your sheep—slaughter them here and eat. But do not sin against the LORD by eating blood.' All the people brought their animals that night and slaughtered them there.",
      "T": "Saul ordered his officers through the camp: 'Every man—bring your animal here and slaughter it properly. Don't sin against the LORD by eating blood.' The people obeyed; every man brought his animal that night and the slaughter was done correctly."
    },
    "35": {
      "L": "And Saul built an altar to the LORD; it was the first altar that he built to the LORD.",
      "M": "Saul built an altar to the LORD—the first altar he ever built to the LORD.",
      "T": "Saul built an altar to the LORD there. It was his first—and the narrative notes it quietly, without praise."
    },
    "36": {
      "L": "And Saul said, 'Let us go down after the Philistines by night and plunder them until the morning light, and let us not leave a man of them.' And they said, 'Do whatever seems good to you.' Then the priest said, 'Let us draw near here to God.'",
      "M": "Saul proposed, 'Let us go down after the Philistines tonight and raid them until dawn—not a man escapes.' The troops agreed: 'Do whatever seems best.' But the priest said, 'Let us first inquire of God.'",
      "T": "Saul proposed a night pursuit: 'Hit the Philistines in the dark, keep going until dawn—leave no survivors.' The men were willing. But the priest stepped in: 'First let us ask God.'"
    },
    "37": {
      "L": "And Saul inquired of God, 'Shall I go down after the Philistines? Will you deliver them into the hand of Israel?' But he did not answer him that day.",
      "M": "Saul inquired of God: 'Shall I pursue the Philistines? Will you give them into Israel's hand?' But God did not answer him that day.",
      "T": "Saul put the question to God: 'Should we pursue? Will you deliver them to Israel?' Silence. God did not answer that day."
    },
    "38": {
      "L": "And Saul said, 'Come here, all you leaders of the people; and know and see in what this sin has been today.'",
      "M": "Saul said, 'Come here, all you leaders. Let us find out where the sin lies that blocked God's answer today.'",
      "T": "Saul summoned the army's leaders: 'Come and face this. Some sin has been committed today that silenced God. We need to find it.'"
    },
    "39": {
      "L": "'For as the LORD lives who saves Israel, though it be in Jonathan my son, he shall surely die.' But not a man of all the people answered him.",
      "M": "'As the LORD who delivers Israel lives—even if the guilt lies with Jonathan my own son, he will certainly die.' Not one of the people answered him.",
      "T": "'As the LORD lives—the one who saves Israel—even if it is my own son Jonathan who is guilty, he dies.' The men stood in silence. No one spoke."
    },
    "40": {
      "L": "Then he said to all Israel, 'You be on one side, and I and Jonathan my son will be on the other side.' And the people said to Saul, 'Do what seems good to you.'",
      "M": "He told all Israel, 'You stand on one side; Jonathan and I will stand on the other.' The people agreed: 'Do as seems best to you.'",
      "T": "Saul set up the lot: 'All Israel on one side; Jonathan and I on the other.' The people gave their consent."
    },
    "41": {
      "L": "Therefore Saul said to the LORD God of Israel, 'Give a perfect lot.' And Saul and Jonathan were taken, but the people escaped.",
      "M": "Saul prayed, 'LORD God of Israel, give a true decision.' The lot fell on Saul and Jonathan; the people were cleared.",
      "T": "Saul prayed: 'LORD God of Israel, give us a clear answer.' The lot closed on Saul and Jonathan—they were identified as the guilty side—while the people were cleared. [The LXX preserves a longer prayer explicitly naming Urim and Thummim, likely the original text.]"
    },
    "42": {
      "L": "And Saul said, 'Cast the lot between me and Jonathan my son.' And Jonathan was taken.",
      "M": "Saul said, 'Cast between me and Jonathan.' The lot fell on Jonathan.",
      "T": "The final cast: 'Between me and Jonathan.' It pointed to Jonathan."
    },
    "43": {
      "L": "Then Saul said to Jonathan, 'Tell me what you have done.' And Jonathan told him and said, 'I tasted a little honey with the end of the rod that was in my hand. Here I am—I must die.'",
      "M": "Saul said to Jonathan, 'Tell me what you have done.' Jonathan answered, 'I tasted a little honey with the tip of my staff. Here I am, ready to die.'",
      "T": "Saul faced his son: 'Tell me what you did.' Jonathan answered quietly: 'I tasted a little honey—just the tip of my staff dipped in. And now, apparently, I am to die.'"
    },
    "44": {
      "L": "And Saul said, 'God do so to me and more also; for you shall surely die, Jonathan.'",
      "M": "Saul said, 'May God punish me severely if you do not die, Jonathan.'",
      "T": "Saul held firm: 'May God strike me down and worse if you don't die, Jonathan.' The oath demanded satisfaction."
    },
    "45": {
      "L": "But the people said to Saul, 'Shall Jonathan die, who has worked this great salvation in Israel? Far be it! As the LORD lives, not a hair of his head shall fall to the ground, for he has worked with God this day.' So the people ransomed Jonathan, and he did not die.",
      "M": "The people rose up against Saul: 'Should Jonathan die—the one who brought this great deliverance to Israel? Never! As the LORD lives, not one hair of his head will fall to the ground, for he acted with God today.' So the people redeemed Jonathan, and he did not die.",
      "T": "The people rose as one man against the king: 'Should Jonathan die? He who gave us this great victory? Never! As the LORD lives, not a hair of his head will be touched—God has been with him today.' They ransomed Jonathan and he lived. The voice of the people overruled the voice of the king."
    },
    "46": {
      "L": "Then Saul went up from following the Philistines, and the Philistines went to their own place.",
      "M": "Saul called off the pursuit of the Philistines, and the Philistines returned to their own territory.",
      "T": "Saul broke off the pursuit. The Philistines went home. The chase that might have been decisive was abandoned."
    },
    "47": {
      "L": "So Saul took the kingdom over Israel and fought against all his enemies on every side—against Moab and against the Ammonites and against Edom and against the kings of Zobah and against the Philistines; and wherever he turned he prevailed.",
      "M": "Saul established his rule over Israel and fought enemies on every front—Moab, Ammon, Edom, the kings of Zobah, and the Philistines. Wherever he turned, he prevailed.",
      "T": "Saul's reign was defined by constant warfare on every border: Moab, Ammon, Edom, the kings of Zobah, the Philistines. Wherever he turned, he held his ground. [The Hebrew word here, rasha in Hiphil, is unusual; most interpreters read it as 'he prevailed' rather than 'he acted wickedly.']"
    },
    "48": {
      "L": "And he acted valiantly and smote the Amalekites, and delivered Israel from the hands of those who plundered them.",
      "M": "He gathered a force, struck the Amalekites, and rescued Israel from those who had been plundering them.",
      "T": "He raised a fighting force, struck the Amalekites, and freed Israel from the raiders who had preyed on them—a success that set the stage for the more demanding command that followed."
    },
    "49": {
      "L": "Now the sons of Saul were Jonathan, Ishui, and Malchishua; and the names of his two daughters were: the name of the firstborn was Merab and the name of the younger was Michal.",
      "M": "Saul's sons were Jonathan, Ishvi, and Malchishua. His daughters were Merab the elder and Michal the younger.",
      "T": "Saul's household: three sons—Jonathan, Ishvi, and Malchishua—and two daughters, Merab the elder and Michal the younger."
    },
    "50": {
      "L": "And the name of Saul's wife was Ahinoam the daughter of Ahimaaz; and the name of the captain of his army was Abner the son of Ner, Saul's uncle.",
      "M": "Saul's wife was Ahinoam daughter of Ahimaaz. His army commander was Abner son of Ner, Saul's uncle.",
      "T": "Saul's wife was Ahinoam, daughter of Ahimaaz. His military commander was Abner son of Ner—his own uncle, which made the command a family affair."
    },
    "51": {
      "L": "Kish was the father of Saul, and Ner the father of Abner was the son of Abiel.",
      "M": "Kish was Saul's father; Ner, Abner's father, was the son of Abiel.",
      "T": "Kish and Ner—Saul's and Abner's fathers—were brothers, both sons of Abiel. The two men who held Israel's kingship and generalship were cousins."
    },
    "52": {
      "L": "And there was hard war against the Philistines all the days of Saul; and whenever Saul saw any strong man or any valiant man, he attached him to himself.",
      "M": "War with the Philistines was fierce throughout Saul's reign, and whenever he saw a capable or courageous man, he recruited him into his service.",
      "T": "The Philistine threat never let up for the length of Saul's reign. His response was to build his army person by person—any man of strength or valor he spotted, he brought into his personal force."
    }
  },
  "15": {
    "1": {
      "L": "And Samuel said to Saul, 'The LORD sent me to anoint you king over his people Israel; now therefore listen to the voice of the words of the LORD.'",
      "M": "Samuel said to Saul, 'The LORD sent me to anoint you king over his people Israel. Now listen to what the LORD says.'",
      "T": "Samuel spoke to Saul with full weight of authority: 'The LORD himself sent me to anoint you king over Israel. That appointment means you are bound to obey him. Now listen carefully.'"
    },
    "2": {
      "L": "'Thus says the LORD of hosts: I have marked what Amalek did to Israel, how he set himself against him in the way when he came up from Egypt.'",
      "M": "'This is what the LORD of Hosts says: I remember what Amalek did to Israel—how he ambushed them on the road when they came up from Egypt.'",
      "T": "'This is the message of the LORD of Armies: I have not forgotten what Amalek did to Israel—the ambush on the road out of Egypt. The account has been open all this time, and now it is time to settle it.'"
    },
    "3": {
      "L": "'Now go and strike Amalek and utterly destroy all that they have and do not spare them; but kill both man and woman, child and infant, ox and sheep, camel and donkey.'",
      "M": "'Now go and attack Amalek and completely destroy everything they have. Spare no one—kill man and woman, child and nursing infant, ox and sheep, camel and donkey.'",
      "T": "'Now march out and strike Amalek. Devote everything they have to destruction—no survivors, no exceptions, no sparing. Man, woman, child, infant, ox, sheep, camel, donkey—everything under the ban.'"
    },
    "4": {
      "L": "So Saul summoned the people and numbered them at Telaim: two hundred thousand foot soldiers, and ten thousand men of Judah.",
      "M": "Saul mustered the troops at Telaim: two hundred thousand infantry and ten thousand men of Judah.",
      "T": "Saul mobilized Israel for the campaign and mustered at Telaim: two hundred thousand infantry from Israel and ten thousand from Judah—a massive force for total war."
    },
    "5": {
      "L": "And Saul came to the city of Amalek and lay in wait in the valley.",
      "M": "Saul advanced to the Amalekite stronghold and set an ambush in the valley.",
      "T": "Saul approached the Amalekite stronghold and positioned his forces in the valley below for the assault."
    },
    "6": {
      "L": "And Saul said to the Kenites, 'Go, depart, go down from among the Amalekites, lest I destroy you with them; for you showed kindness to all the children of Israel when they came up out of Egypt.' So the Kenites departed from among the Amalekites.",
      "M": "Saul warned the Kenites: 'Leave—get away from the Amalekites or I will destroy you with them. You showed loyalty to all Israel when they came up from Egypt.' The Kenites withdrew from the Amalekites.",
      "T": "Before the attack, Saul gave the Kenites a warning: 'Get away from the Amalekites—now. You showed covenant faithfulness to Israel on the way out of Egypt, and I will not destroy you with them.' The Kenites withdrew."
    },
    "7": {
      "L": "And Saul struck the Amalekites from Havilah as you approach Shur, which is east of Egypt.",
      "M": "Saul struck the Amalekites all the way from Havilah to the approach of Shur, which lies east of Egypt.",
      "T": "Saul swept through Amalekite territory from Havilah to Shur on Egypt's eastern border—covering the full extent of the land."
    },
    "8": {
      "L": "And he took Agag the king of the Amalekites alive, and utterly destroyed all the people with the edge of the sword.",
      "M": "He captured Agag king of Amalek alive and devoted all the rest of the people to destruction by the sword.",
      "T": "He captured Agag—the Amalekite king—alive. The rest of the people he put to the sword as commanded."
    },
    "9": {
      "L": "But Saul and the people spared Agag and the best of the sheep and of the oxen and of the fatlings and the lambs, and all that was good, and would not utterly destroy them; but everything despised and worthless they utterly destroyed.",
      "M": "But Saul and the people spared Agag, along with the best sheep and cattle, the fatlings and the lambs, and everything of value—they refused to destroy these. Only what was thin and inferior did they devote to destruction.",
      "T": "But Saul and the army broke the ban selectively. They kept Agag alive and held back the finest animals—the best sheep and cattle, the fatlings and lambs, everything worth keeping. Only the worthless and inferior did they destroy. It was obedience with conditions, which is not obedience."
    },
    "10": {
      "L": "Then the word of the LORD came to Samuel, saying,",
      "M": "Then the word of the LORD came to Samuel:",
      "T": "That night the word of the LORD came to Samuel:"
    },
    "11": {
      "L": "'I repent that I have made Saul king, for he has turned back from following me and has not performed my commandments.' And it grieved Samuel, and he cried to the LORD all night.",
      "M": "'I regret that I made Saul king, for he has turned away from me and has not carried out my commands.' Samuel was deeply troubled and cried out to the LORD all night.",
      "T": "'I grieve that I made Saul king. He has turned his back on me and refused my commands.' The word struck Samuel to the core. He spent the entire night crying out to the LORD."
    },
    "12": {
      "L": "And Samuel rose early to meet Saul in the morning; and it was told Samuel, saying, 'Saul came to Carmel and set up a monument for himself, and turned and passed on and went down to Gilgal.'",
      "M": "Samuel rose early to meet Saul, but received word: 'Saul has been to Carmel—he set up a monument for himself there—then turned and moved down to Gilgal.'",
      "T": "Samuel rose at dawn to meet Saul. The report came back: 'Saul went to Carmel first and erected a monument to himself there, then moved on down to Gilgal.' The detail of the monument was telling."
    },
    "13": {
      "L": "And Samuel came to Saul, and Saul said to him, 'Blessed are you by the LORD! I have performed the commandment of the LORD.'",
      "M": "When Samuel arrived, Saul greeted him: 'Blessed are you by the LORD! I have carried out the LORD's command.'",
      "T": "When Samuel arrived, Saul met him with confident words: 'Blessed are you by the LORD! I have fully carried out the LORD's command.' He believed it."
    },
    "14": {
      "L": "And Samuel said, 'What then is this bleating of sheep in my ears, and the lowing of oxen that I hear?'",
      "M": "Samuel replied, 'Then what is this bleating of sheep I hear? And this lowing of cattle?'",
      "T": "Samuel's response was a single devastating question: 'Then what is that sound? I hear sheep bleating. I hear cattle lowing. Explain that to me.'"
    },
    "15": {
      "L": "And Saul said, 'They have brought them from the Amalekites, for the people spared the best of the sheep and the oxen to sacrifice to the LORD your God; and the rest we have utterly destroyed.'",
      "M": "Saul said, 'The troops brought them from the Amalekites. They spared the best sheep and cattle to sacrifice to the LORD your God—and the rest we destroyed completely.'",
      "T": "Saul shifted the blame immediately: 'The men brought them. They saved the choicest sheep and cattle for a sacrifice to the LORD your God. Everything else we destroyed.' Three problems: the decision was Saul's, not the men's; the LORD had not asked for a sacrifice; and he said 'your God,' not 'my God.'"
    },
    "16": {
      "L": "Then Samuel said to Saul, 'Stop! Let me tell you what the LORD said to me last night.' And he said to him, 'Speak.'",
      "M": "Samuel said, 'Stop. Let me tell you what the LORD said to me last night.' 'Speak,' said Saul.",
      "T": "Samuel held up his hand: 'Enough. Let me tell you what the LORD said to me last night.' 'Say it,' Saul replied."
    },
    "17": {
      "L": "And Samuel said, 'Though you were little in your own eyes, were you not made the head of the tribes of Israel? The LORD anointed you king over Israel.'",
      "M": "Samuel said, 'When you were small in your own eyes, you were made head of the tribes of Israel. The LORD anointed you king over Israel.'",
      "T": "Samuel began the indictment with the beginning: 'There was a time when you saw yourself as nobody—and that was the very moment the LORD made you head of all Israel's tribes. He anointed you king. Remember where you stand.'"
    },
    "18": {
      "L": "'And the LORD sent you on a journey and said, Go and utterly destroy the sinners, the Amalekites, and fight against them until they are consumed.'",
      "M": "'The LORD sent you on a mission with an explicit command: Go and completely destroy the Amalekites, those sinners, and fight until you have wiped them out.'",
      "T": "'And the command he gave you was unambiguous: Go, destroy the Amalekites—those who have sinned against my people—and fight until there is nothing left of them. Those were his exact words.'"
    },
    "19": {
      "L": "'Why then did you not obey the voice of the LORD? Why did you swoop upon the spoil and do what is evil in the sight of the LORD?'",
      "M": "'Why then did you not obey the LORD? Why did you pounce on the plunder and do what was evil in his eyes?'",
      "T": "'So why? Why did you not obey the LORD's voice? Instead of finishing the job you launched yourself at the spoil—and that is evil in the LORD's sight.'"
    },
    "20": {
      "L": "And Saul said to Samuel, 'Yes, I have obeyed the voice of the LORD, and have gone the way the LORD sent me, and have brought Agag the king of Amalek, and have utterly destroyed the Amalekites.'",
      "M": "Saul replied, 'But I did obey the LORD! I went where he sent me. I brought back Agag king of Amalek, and I completely destroyed the Amalekites.'",
      "T": "Saul stood his ground: 'I did obey. I went where the LORD directed me. I captured Agag. I destroyed the Amalekites.' He genuinely believed his selective compliance qualified as full obedience."
    },
    "21": {
      "L": "'But the people took from the spoil sheep and oxen, the best of the devoted things, to sacrifice to the LORD your God in Gilgal.'",
      "M": "'But the people took sheep and cattle from the plunder—the choicest of what had been devoted to destruction—to sacrifice to the LORD your God at Gilgal.'",
      "T": "'But the soldiers—' again Saul deflects—'took from the devoted things the finest sheep and cattle, intending to sacrifice to the LORD your God at Gilgal.' He frames their disobedience as devotion; Samuel will name it correctly."
    },
    "22": {
      "L": "And Samuel said, 'Has the LORD as great delight in burnt offerings and sacrifices as in obeying the voice of the LORD? Behold, to obey is better than sacrifice, and to listen than the fat of rams.'",
      "M": "Samuel replied, 'Does the LORD take as much pleasure in burnt offerings and sacrifices as in obedience to his voice? To obey is better than sacrifice; to listen is better than the fat of rams.'",
      "T": "Samuel's verdict was devastating: 'Does the LORD prefer an offering over obedience? Does sacrifice please him more than compliance? No. Obedience is worth more than sacrifice. Attentiveness to him outweighs the fat of a thousand rams.'"
    },
    "23": {
      "L": "'For rebellion is as the sin of divination, and stubbornness is as iniquity and idolatry; because you have rejected the word of the LORD, he has also rejected you from being king.'",
      "M": "'Rebellion is like the sin of divination, and stubbornness is like wickedness and idolatry. Because you rejected the word of the LORD, he has rejected you as king.'",
      "T": "'Defiance against the LORD is no different from sorcery. Stubbornness is the same as serving idols. Because you treated the LORD's word as something to edit—he has ended your kingship. The rejection is his response to yours.'"
    },
    "24": {
      "L": "And Saul said to Samuel, 'I have sinned, for I have transgressed the commandment of the LORD and your words, because I feared the people and obeyed their voice.'",
      "M": "Saul said to Samuel, 'I have sinned. I transgressed the LORD's command and your words because I was afraid of the people and listened to them.'",
      "T": "Saul finally said the word: 'I have sinned.' But the confession immediately explained itself away: 'I feared the men. I let them prevail.' Saul's deepest failure was obedience to the crowd instead of obedience to God—an honor-shame collapse at the core of his kingship."
    },
    "25": {
      "L": "'Now therefore, I pray you, pardon my sin and return with me that I may worship the LORD.'",
      "M": "'Now please forgive my sin and come back with me so I can worship the LORD.'",
      "T": "Saul's plea mixed genuine longing with social calculation: 'Forgive my sin and come back with me—I want to worship the LORD.' He needed forgiveness; he also needed Samuel's public presence to hold his honor before the people."
    },
    "26": {
      "L": "And Samuel said to Saul, 'I will not return with you, for you have rejected the word of the LORD, and the LORD has rejected you from being king over Israel.'",
      "M": "Samuel replied, 'I will not go back with you, because you rejected the LORD's word—and the LORD has rejected you as king over Israel.'",
      "T": "Samuel's answer was final: 'I will not go back with you. You rejected the LORD's word—the LORD has rejected you as king over Israel. The two rejections mirror each other exactly.'"
    },
    "27": {
      "L": "And as Samuel turned to go away, Saul seized the hem of his robe, and it tore.",
      "M": "As Samuel turned to leave, Saul grabbed the edge of his robe, and it tore.",
      "T": "Samuel turned to walk away. Saul grabbed at the hem of his robe—and the cloth tore in his hand."
    },
    "28": {
      "L": "And Samuel said to him, 'The LORD has torn the kingdom of Israel from you today and has given it to a neighbor of yours, who is better than you.'",
      "M": "Samuel said, 'The LORD has torn the kingdom of Israel from you today and given it to one of your neighbors—someone better than you.'",
      "T": "Samuel turned the torn cloth into a prophetic sign: 'The LORD has just done that to your kingdom—torn it from you this day and given it to one who is better than you. Your neighbor already has it in promise.'"
    },
    "29": {
      "L": "And also the Strength of Israel will not lie or repent, for he is not a man, that he should repent.",
      "M": "Moreover, the Eternal One of Israel does not lie or change his mind, for he is not a man who changes his mind.",
      "T": "Samuel added the theological bedrock: 'The Enduring One of Israel does not deceive and does not reverse his word. He is not a human being who reconsiders.' What had been declared was irrevocable."
    },
    "30": {
      "L": "Then he said, 'I have sinned; yet honor me now before the elders of my people and before Israel, and return with me that I may worship the LORD your God.'",
      "M": "Saul said again, 'I have sinned; but please honor me before the elders of my people and before Israel. Come back with me so I can worship the LORD your God.'",
      "T": "Saul tried once more: 'I have sinned—yes. But don't shame me publicly. Honor me before the elders, before all Israel. Come with me and let me worship the LORD your God.' He confessed the sin; he could not yet absorb the loss of standing."
    },
    "31": {
      "L": "So Samuel turned back after Saul, and Saul worshipped the LORD.",
      "M": "So Samuel went back with Saul, and Saul worshipped the LORD.",
      "T": "Samuel relented and turned back. Saul worshipped the LORD. The act was real, but the moment was irreversible."
    },
    "32": {
      "L": "Then Samuel said, 'Bring Agag the king of the Amalekites to me.' And Agag came to him haltingly; and Agag said, 'Surely the bitterness of death is past.'",
      "M": "Samuel commanded, 'Bring Agag king of Amalek to me.' Agag came hesitantly; and Agag said, 'Surely the bitter agony of death has passed.'",
      "T": "Samuel ordered: 'Bring Agag the Amalekite king here.' Agag came—the text says 'haltingly' or perhaps 'with confidence'; the Hebrew is ambiguous. His last words were either relieved or terrified: 'Surely the bitterness of death has passed.' He was wrong."
    },
    "33": {
      "L": "And Samuel said, 'As your sword has made women childless, so shall your mother be childless among women.' And Samuel hewed Agag in pieces before the LORD in Gilgal.",
      "M": "Samuel said, 'As your sword has made women childless, so your mother shall be childless among women.' And Samuel cut Agag down before the LORD at Gilgal.",
      "T": "Samuel pronounced the sentence in the exact grammar of justice: 'As your sword has made house after house childless—mother after mother left without sons—so your own mother joins them today.' Then Samuel executed Agag before the LORD at Gilgal."
    },
    "34": {
      "L": "Then Samuel went to Ramah, and Saul went up to his house at Gibeah of Saul.",
      "M": "Samuel returned to Ramah, and Saul went home to Gibeah of Saul.",
      "T": "Samuel went back to Ramah. Saul went home to Gibeah. Each man to his own place—but the break between them was final."
    },
    "35": {
      "L": "And Samuel did not see Saul again until the day of his death; but Samuel mourned for Saul. And the LORD repented that he had made Saul king over Israel.",
      "M": "Samuel did not see Saul again until the day of his death; yet Samuel grieved for him. And the LORD regretted that he had made Saul king over Israel.",
      "T": "Samuel never saw Saul again for the rest of his life. Yet he grieved for Saul—a long, unresolved mourning. And the LORD himself grieved that he had made Saul king over Israel. Both prophet and God bore the cost of what Saul had thrown away."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '1samuel', existing)
    print('1 Samuel 13–15 written.')

if __name__ == '__main__':
    main()
