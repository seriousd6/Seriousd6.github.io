"""
MKT Nehemiah chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-nehemiah-4-6.py

Translation decisions:
- H3068 (יהוה): "LORD" in L and M; "the LORD" in T. Consistent with Ezra scripts.
- H136 (אֲדֹנָי): "the Lord" (mixed case, Adonai) in all tiers. Appears at 4:14.
- H430 (אֱלֹהִים): "God" throughout. Personal address form "O my God" / "my God" preserved.
- H2617 (חֶסֶד): Does not appear in chs 4–6. No rendering needed here.
- H5315 (נֶפֶשׁ): "life" in 6:11 (to save his life — embodied self, not immaterial soul).
- H1419 + H3372 (great and awesome/terrible): "great and awesome" in L/M; "great and
  terrifying" avoided — "awe-inspiring" also considered; "awesome" retained as
  covenantal/fearsome rather than colloquial.
- H8451 (תּוֹרָה): Does not appear in chs 4–6.
- Mockers (chs 4–6): Sanballat, Tobiah the Ammonite, Geshem the Arab, and the Ashdodites
  form an ethnic coalition of opponents — their identities are preserved without softening.
- Honor-shame framing (4:2, 4:4, 6:6, 6:11): Deliberate contempt / shame-reversal logic
  surfaced in T tier. The public open letter (6:5) is an ancient pressure tactic.
- "The work is great" (4:19): Technical military-logistics observation, not generic praise.
- 5:7 "I took counsel with myself" (H3820 = heart): Inner deliberation before public action.
- 5:13 lap-shaking (H5287): A formal covenant-curse gesture, not mere dramatic flair. T
  makes this explicit.
- 6:10 Shemaiah "confined" (H6113): May indicate ritual impurity making his temple counsel
  doubly suspect — a confinee proposing sanctuary entry.
- 6:11 "Should such a man as I flee?": Double argument — honor (a leader does not bolt)
  and theology (Nehemiah is not a priest; entering the sanctuary would be sacrilege). T
  preserves both.
- 6:14 Noadiah the prophetess: Only named female prophet in post-exilic narrative; her
  inclusion suggests the opposition's psychological operation extended across gender lines.
- 6:15 "fifty-two days": The completion time is a theological data point; T names it.
- 4:23 final clause: The Hebrew is textually difficult. Rendered "each kept his weapon at
  the ready" following ESV-style reading, which is better attested than KJV "for washing."
- Verse count: Ch 4 = 23, Ch 5 = 19, Ch 6 = 19; total 61. Matches NEH-1b work queue entry.
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

NEHEMIAH = {
  "4": {
    "1": {
      "L": "But it came to pass, when Sanballat heard that we were building the wall, that he was angry and greatly provoked, and he mocked the Jews.",
      "M": "When Sanballat heard that we were rebuilding the wall, he became furious and deeply offended, and he ridiculed the Jews.",
      "T": "When Sanballat learned of the rebuilding, he did not respond privately—his fury became a public performance. He gathered an audience and openly mocked the Jews, turning their labor into a spectacle of contempt."
    },
    "2": {
      "L": "And he spoke before his brothers and the army of Samaria and said, 'What are these feeble Jews doing? Will they restore things for themselves? Will they sacrifice? Will they finish in a day? Will they revive the stones from the heaps of rubbish—even the burned ones?'",
      "M": "In front of his associates and the army of Samaria he said, 'What do these feeble Jews think they are doing? Can they actually restore this? Will they make a sacrifice and get it done in a single day? Can they bring life back to burned stones from rubble heaps?'",
      "T": "Before the military of Samaria and his own circle, Sanballat catalogued their contempt: these are exhausted, dishonored people—can they work a miracle? Finish in a day? Breathe life into charred rubble? Every question was rhetorical, each one layering more shame on the project."
    },
    "3": {
      "L": "Now Tobiah the Ammonite was beside him, and he said, 'Even what they build—if a fox goes up on it, he will break down their stone wall.'",
      "M": "Tobiah the Ammonite, who was standing nearby, added, 'Whatever they build, if a fox trots across it, it will collapse their stone wall.'",
      "T": "Tobiah the Ammonite piled on: 'Even if they do build something, a fox walking across it will bring the whole thing down.' The contempt was coordinated—a public shaming performance meant to demoralize the workers before they began."
    },
    "4": {
      "L": "Hear, O our God, for we are despised. Turn back their reproach on their own heads and give them up as plunder in a land of captivity.",
      "M": "Hear us, O our God, for we are held in contempt. Turn their reproach back on their own heads and hand them over as plunder in a land of exile.",
      "T": "Nehemiah's response to the mockery was not a counter-argument—it was a prayer. He brought the shame directly to God: 'We are publicly humiliated. Return it on their own heads. Let the exile they threaten us with become their own fate.'"
    },
    "5": {
      "L": "And do not cover their iniquity, and do not let their sin be blotted out from before you, for they have provoked you to anger before those who are building.",
      "M": "Do not cover their guilt or let their sin be wiped from your sight, for they have provoked you to anger in the presence of the builders.",
      "T": "The prayer sharpens into an imprecation: 'Do not forgive this. They have insulted your workers doing your work—that makes it an offense against you, not just against us. Remember it.'"
    },
    "6": {
      "L": "So we built the wall, and the whole wall was joined together to half its height, for the people had a mind to work.",
      "M": "So we built the wall, and the entire wall was joined together to half its height, because the people had the will to work.",
      "T": "In spite of the scorn, work continued. The whole circuit of the wall rose to half height—because the people had set their hearts on it. Public humiliation had not broken their resolve."
    },
    "7": {
      "L": "But when Sanballat and Tobiah and the Arabians and the Ammonites and the Ashdodites heard that the repairing of the walls of Jerusalem was advancing and that the breaches were beginning to be stopped up, they were very angry.",
      "M": "But when Sanballat, Tobiah, the Arabs, the Ammonites, and the Ashdodites heard that the walls of Jerusalem were being restored and the gaps were being closed, they were furious.",
      "T": "Progress on the wall expanded the opposition's coalition. Five regional groups—Sanballat's Samaria, Tobiah's Ammonites, the Arab confederacy, the Ashdodites—all heard the same news: the breaches were closing. Their collective fury intensified."
    },
    "8": {
      "L": "And they all conspired together to come and fight against Jerusalem and to cause confusion in it.",
      "M": "They all plotted together to march on Jerusalem and create confusion there.",
      "T": "Their tactical response was a united front: a coordinated military strike against Jerusalem, with the secondary goal of sowing enough internal confusion to collapse the project from within."
    },
    "9": {
      "L": "But we prayed to our God and set a guard against them day and night because of them.",
      "M": "We prayed to our God and posted a guard against them day and night.",
      "T": "The community's response was both spiritual and practical—the pattern Nehemiah would repeat throughout the crisis. Prayer was not a substitute for strategy; a round-the-clock guard was not a substitute for prayer. Both, together."
    },
    "10": {
      "L": "And Judah said, 'The strength of the burden-bearers is failing. There is too much rubble. We are not able to build the wall.'",
      "M": "Meanwhile, the people of Judah were saying, 'The strength of the laborers is giving out, and there is so much rubble that we cannot rebuild the wall.'",
      "T": "The external threat was compounded by internal collapse. The workers' strength was breaking down under the rubble load—and the demoralization was spreading. Judah said aloud what everyone was beginning to feel: 'We can't do this.'"
    },
    "11": {
      "L": "And our adversaries said, 'They will not know or see until we come among them and kill them and cause the work to cease.'",
      "M": "Our enemies were saying, 'They will not see us coming until we are in their midst—we will kill them and stop the work.'",
      "T": "The enemy's plan was surprise: strike before the builders knew what was happening. Kill them at their posts. End the project with a single raid. The intelligence on this reached Nehemiah."
    },
    "12": {
      "L": "At that time the Jews who were dwelling beside them came and said to us ten times from all the places where they were living, 'You must return to us from every direction.'",
      "M": "And the Jews who lived near our enemies came repeatedly—ten times—from all the places they lived, to warn us that attacks were coming from every side.",
      "T": "Jewish communities living dangerously close to the enemy lines sent runners with the same warning ten times over: the attack was coming, and it would come from multiple directions simultaneously."
    },
    "13": {
      "L": "So I stationed the people in the lower parts of the space behind the wall and on the heights, arranged by their clans, with their swords, their spears, and their bows.",
      "M": "I stationed the people in the lower sections behind the wall and on the exposed heights, grouped by families, each armed with swords, spears, and bows.",
      "T": "Nehemiah responded with a tactical deployment: he positioned clan units at the most vulnerable sections—the low ground where attackers could approach most easily, and the exposed heights where visibility was needed. Every unit was armed."
    },
    "14": {
      "L": "And I looked, and rose up, and said to the nobles and to the officials and to the rest of the people, 'Do not be afraid of them. Remember the Lord, who is great and awesome, and fight for your brothers, your sons, your daughters, your wives, and your homes.'",
      "M": "After surveying the situation, I stood up and addressed the nobles, officials, and all the people: 'Do not be afraid of them. Remember the Lord, who is great and awe-inspiring, and fight for your brothers, sons, daughters, wives, and homes.'",
      "T": "Nehemiah addressed the full community—leadership and workers alike. His speech had two movements: look up (remember the great and awesome Lord), then look around (fight for every person you love). The divine warrior and the human defender belong together."
    },
    "15": {
      "L": "When our enemies heard that it was known to us, and that God had brought their plan to nothing, we all returned to the wall, each to his own work.",
      "M": "When our enemies learned that their scheme had been found out and that God had brought it to nothing, we all went back to the wall, each to his own task.",
      "T": "God's providence was also tactical: the enemies' plan depended on surprise, and surprise was now gone. Without it they had no advantage. We returned to the wall—every person, every assignment—because the threat had been neutralized not by our own cleverness but by God's."
    },
    "16": {
      "L": "And it came to pass from that day on that half of my servants did the work and half held the spears, the shields, the bows, and the coats of mail. And the officers stood behind all the house of Judah",
      "M": "From that day on, half my men did construction work while the other half stood guard, armed with spears, shields, bows, and body armor. The officers positioned themselves behind the entire force of Judah",
      "T": "The community reorganized for sustained dual-purpose operation: half the workforce building, half standing guard in full military kit. The officers took rear positions behind the Judah contingent—a command structure able to respond in any direction."
    },
    "17": {
      "L": "who were building on the wall. And those carrying burdens loaded themselves in such a way that each worked on the task with one hand and held his weapon with the other.",
      "M": "who were working on the wall. Those carrying loads did so in a way that allowed each man to work with one hand while keeping his weapon ready in the other.",
      "T": "The builders solved the problem of armed construction: one hand on the work, one hand on the weapon. It was slower, but it meant the wall was never undefended at any point."
    },
    "18": {
      "L": "And each of the builders had his sword strapped at his side while he built. And the one who sounded the trumpet was beside me.",
      "M": "Every builder wore his sword belted at his side as he worked. The trumpeter stayed beside me.",
      "T": "Every builder carried a sword—not stored nearby, but belted on the body, ready while the hands worked. Nehemiah kept the signal-bearer at his side: the trumpet was the nerve center of the whole defensive system."
    },
    "19": {
      "L": "And I said to the nobles and to the officials and to the rest of the people, 'The work is great and spread out, and we are separated on the wall, far from one another.'",
      "M": "I told the nobles, officials, and all the people: 'The work is extensive and the wall is long. We are spread far apart from each other.'",
      "T": "Nehemiah named the tactical vulnerability plainly: the wall's length meant the workforce was scattered. No section could see another. A localized attack would overwhelm one team before others could respond—unless there was a communications protocol."
    },
    "20": {
      "L": "In the place where you hear the sound of the trumpet, gather to us there. Our God will fight for us.",
      "M": "Wherever you hear the trumpet sound, rush there. Our God will fight for us.",
      "T": "The protocol was simple: sound of trumpet means point of attack—run there. And beneath the tactical instruction lay the theological ground: 'Our God will fight for us.' Human rapid response and divine intervention were not alternatives but partners."
    },
    "21": {
      "L": "So we labored at the work, and half of them held spears from the rising of the morning until the stars appeared.",
      "M": "So we worked at the task, with half the men holding spears from the break of dawn until the stars came out.",
      "T": "The rhythm of it: dawn to stars, every day. Builders and guards, side by side, through the full span of daylight. The day ended only when darkness made work impossible."
    },
    "22": {
      "L": "At that time I also said to the people, 'Let every man and his servant lodge inside Jerusalem, that they may be a guard for us by night and may labor by day.'",
      "M": "I also instructed the people at that time: 'Each man with his household workers should stay the night inside Jerusalem—serving as a guard by night and a worker by day.'",
      "T": "Nehemiah closed the final gap in the security plan: nobody leaves the city at night. Workers who had been commuting back to villages would now sleep inside the walls. Night security required bodies inside the perimeter."
    },
    "23": {
      "L": "So neither I nor my brothers nor my servants nor the men of the guard who followed me—none of us took off our clothes; each man kept his weapon at the ready.",
      "M": "Neither I nor my brothers nor my servants nor the guards who accompanied me removed our clothing; each man kept his weapon within reach.",
      "T": "They slept dressed and armed. Nehemiah included himself—no separation between the leader's comfort and the workers' conditions. The threat was constant enough that this became the normal way to live. The boundary between construction project and military campaign had dissolved."
    }
  },
  "5": {
    "1": {
      "L": "Now there arose a great cry of the people and of their wives against their Jewish brothers.",
      "M": "At that time a great outcry arose from the people and their wives against their fellow Jews.",
      "T": "While the external enemy pressed from without, an internal crisis erupted. The common people—men and women together—raised a public grievance against their own wealthy Jewish neighbors. The wall-building had exposed a fracture inside the community."
    },
    "2": {
      "L": "For there were those who said, 'We, our sons, and our daughters are many. Let us get grain that we may eat and stay alive.'",
      "M": "Some were saying, 'Our families are large—sons and daughters. We need grain just to eat and survive.'",
      "T": "The grievances sorted into categories. The first and most basic: survival. 'We have children. We have nothing to feed them. We need grain or people will die.'"
    },
    "3": {
      "L": "There were also those who said, 'We are mortgaging our fields, our vineyards, and our houses to get grain because of the famine.'",
      "M": "Others said, 'We have pledged our fields, vineyards, and homes to get grain during the famine.'",
      "T": "Second category: asset liquidation under duress. The famine had driven families to pledge their productive land and their homes as collateral for food. Once the famine lifted, the debts remained."
    },
    "4": {
      "L": "And there were those who said, 'We have borrowed money for the king's tax on our fields and our vineyards.'",
      "M": "Still others said, 'We have had to borrow money to pay the king's tax on our fields and vineyards.'",
      "T": "Third category: imperial tax debt. The Persian crown's levy on agricultural land had to be paid in coin. Families with grain but no silver had to borrow—at interest—just to meet the tax on their own property."
    },
    "5": {
      "L": "Now our flesh is as the flesh of our brothers, our children are as their children. Yet we are forcing our sons and our daughters into slavery, and some of our daughters have already been enslaved, and it is not in our power, for other men have our fields and our vineyards.",
      "M": "We are the same flesh as our brothers, and our children are like theirs. But we are having to reduce our sons and daughters to slavery—some of our daughters are already enslaved—and we are helpless, because our fields and vineyards are now in others' hands.",
      "T": "The deepest injury: 'We are you. Same blood, same covenant, same God. But our children are becoming slaves while yours are free. Some of our daughters are already gone—sold into debt-service—and we have no assets left to redeem them.' The language of identical flesh was a covenant appeal, not sentimentality."
    },
    "6": {
      "L": "I was very angry when I heard their outcry and these words.",
      "M": "I was deeply angry when I heard their cry and their complaint.",
      "T": "Nehemiah heard it all—and the text does not soften his reaction. He was very angry. This was not administrative irritation; it was the righteous anger of a leader confronting covenant violation within the covenant community."
    },
    "7": {
      "L": "And I took counsel with myself, and I brought charges against the nobles and the officials. I said to them, 'You are each exacting interest from your own brother.' And I called a great assembly against them",
      "M": "After deliberating inwardly, I brought a formal charge against the nobles and officials. I said to them, 'You are each lending at interest to your own people.' Then I convened a large public assembly to confront them",
      "T": "He paused before acting—inner deliberation before public confrontation. Then he moved decisively: the charge against the nobles and rulers was specific and legal (Torah prohibited lending at interest to fellow Israelites), and he convened a public assembly to ensure accountability before the whole community."
    },
    "8": {
      "L": "and said to them, 'We, as far as we were able, have redeemed our Jewish brothers who had been sold to the nations. But now you are selling your own brothers, that they may be sold to us!' They were silent and could not find a word to say.",
      "M": "and said, 'We have done everything we could to buy back our Jewish brothers who were sold to foreign nations—and now you are selling your own brothers back into that same bondage! They end up being sold back to us!' They had nothing to say.",
      "T": "The argument was devastating: 'We just spent our own resources buying Jewish slaves back from Gentile hands—and you are selling them again. You are undoing redemption work with one hand while we do it with the other.' The nobles fell completely silent. There was no defense."
    },
    "9": {
      "L": "So I said, 'The thing that you are doing is not good. Ought you not to walk in the fear of our God to prevent the reproach of the nations who are our enemies?'",
      "M": "I continued, 'What you are doing is wrong. Should you not walk in the fear of our God, so that our enemies among the nations have no grounds to reproach us?'",
      "T": "'What you are doing is dishonorable—and the dishonor reaches further than this community. Our enemies are watching. Injustice practiced within our own walls while we claim to serve God gives every surrounding nation an argument against us. Walk in the fear of God.' The internal covenant obligation and the external witness were inseparable."
    },
    "10": {
      "L": "Likewise I and my brothers and my servants have been lending them money and grain. Let us abandon this exacting of interest.",
      "M": "Moreover, I and my brothers and my servants have also been lending them money and grain. Let us stop charging interest altogether.",
      "T": "Nehemiah included himself in the indictment: 'I have been part of this system too—lending money and grain.' His call to end the practice was not an outsider's demand but a self-implicating reform. That credibility was essential to what followed."
    },
    "11": {
      "L": "Return to them this very day their fields, their vineyards, their olive orchards, and their houses, and the hundredth part of the money, the grain, the wine, and the oil that you have been exacting from them.",
      "M": "Restore to them today their fields, vineyards, olive groves, and houses, and the one-percent interest you have been taking on money, grain, wine, and oil.",
      "T": "The demand was immediate and comprehensive: not eventually—today. Return the land, the houses, the collateral seized for defaulted loans, and every interest payment extracted. The economic structures that had produced the debt-slavery were to be dismantled as of this moment."
    },
    "12": {
      "L": "Then they said, 'We will restore them and require nothing from them. We will do as you say.' And I called the priests and made them swear to do according to this promise.",
      "M": "They replied, 'We will give everything back and demand nothing more. We will do exactly as you say.' Then I called the priests and had them take a formal oath to keep this promise.",
      "T": "The nobles agreed publicly. Nehemiah did not let the moment pass with verbal agreement—he summoned priests immediately and had the nobles swear a solemn oath before God. Words could be forgotten; an oath before the priesthood carried the weight of the covenant."
    },
    "13": {
      "L": "I also shook out the fold of my garment and said, 'So may God shake out every man from his house and from his labor who does not keep this promise. So may he be shaken out and emptied.' And all the assembly said, 'Amen,' and praised the LORD. And the people did as they had promised.",
      "M": "I also shook out the fold of my robe and said, 'May God shake out and empty every man like this—from his house and from his labor—who does not keep this promise.' The whole assembly said, 'Amen,' and praised the LORD. And the people kept their word.",
      "T": "Nehemiah sealed the oath with a symbolic curse-gesture: he shook out the fold of his robe—a formal ancient act meaning 'may everything be stripped from the one who breaks this.' The community responded with 'Amen'—assent to the curse—and then broke into praise. The LORD was to be both witness and enforcer. The people followed through."
    },
    "14": {
      "L": "Moreover, from the day that I was appointed to be their governor in the land of Judah, from the twentieth year to the thirty-second year of Artaxerxes the king, twelve years, neither I nor my brothers ate the food allotted to the governor.",
      "M": "Furthermore, throughout my entire term as governor of Judah—twelve years, from the twentieth to the thirty-second year of King Artaxerxes—neither I nor my brothers drew on the governor's food allowance.",
      "T": "Nehemiah then made his own record transparent: twelve years as governor, and he had never once charged the people for his household's upkeep. The governor's food allotment—his legal entitlement—he had declined entirely. His reform of others rested on his own prior practice."
    },
    "15": {
      "L": "The former governors who were before me laid heavy burdens on the people and took from them for food and wine, besides forty shekels of silver. Even their servants exercised dominion over the people. But I did not do so because of the fear of God.",
      "M": "The governors before me had burdened the people heavily, taking food and wine from them in addition to forty shekels of silver. Even their aides lorded it over the people. But I did not behave this way, out of reverence for God.",
      "T": "The standard practice of Persian-era governors was to run the office as a revenue stream: mandatory food levies, wine requisitions, forty shekels of silver in fees—and their staff adding further impositions. Nehemiah refused the entire model. Not out of political calculation, but because he feared God more than he valued the perquisites of power."
    },
    "16": {
      "L": "Also I devoted myself to the work on this wall, and I acquired no land. And all my servants were gathered there for the work.",
      "M": "I also gave myself fully to the work on this wall and did not purchase any land. All my servants were put to work on the project.",
      "T": "He had also declined to leverage his position for personal enrichment: no land was acquired while he held power. Every member of his household was deployed to the wall—not to his private interests. The governor's office was an instrument of service, not accumulation."
    },
    "17": {
      "L": "Furthermore, there were at my table a hundred and fifty men—Jews and officials—besides those who came to us from the nations around us.",
      "M": "Moreover, I regularly fed 150 Jewish officials at my table, in addition to visitors from the surrounding nations.",
      "T": "His table bore a public function: 150 officials and community leaders ate there regularly, plus delegations from neighboring peoples. In an honor-culture context, this was diplomacy and community building, not personal entertainment—and every meal came out of his own resources."
    },
    "18": {
      "L": "Now what was prepared for me daily was one ox and six choice sheep, and fowl were also prepared for me. And once every ten days all kinds of wine in abundance. Yet for all this I did not demand the food allotment of the governor, because the service on this people was heavy.",
      "M": "Each day my table required one ox, six prime sheep, birds, and generous supplies of wine every ten days. Despite all this expense, I never drew on the governor's food budget, because the burden on these people was already too great.",
      "T": "The provision was substantial—the cost of feeding 150 men daily. He itemized it to make the sacrifice visible. And he absorbed every coin of it himself. His reasoning: the people were already bent under the weight of famine, taxation, and labor. He would add nothing more to that load."
    },
    "19": {
      "L": "Remember me, O my God, for good, according to all that I have done for this people.",
      "M": "Remember me with favor, O my God, for everything I have done for this people.",
      "T": "The chapter closes with a prayer that is both humble and unguarded: 'God—you saw it all. Remember it.' Nehemiah makes no argument, lodges no complaint. He simply places his service before God's eyes and trusts the record to him."
    }
  },
  "6": {
    "1": {
      "L": "Now it came to pass, when Sanballat and Tobiah and Geshem the Arab and the rest of our enemies heard that I had built the wall and that there was no breach left in it—although at that time I had not yet set up the doors in the gates—",
      "M": "When Sanballat, Tobiah, Geshem the Arab, and the rest of our enemies heard that the wall was rebuilt and no gaps remained—though the gate doors had not yet been installed—",
      "T": "The wall was structurally complete: continuous, unbroken, standing. Only the gate doors remained unset—and news of this near-completion reached the coalition of enemies immediately."
    },
    "2": {
      "L": "Sanballat and Geshem sent to me saying, 'Come and let us meet together at Hakkephirim in the plain of Ono.' But they intended to do me harm.",
      "M": "Sanballat and Geshem sent a message: 'Come, let us meet in one of the villages in the plain of Ono.' But their intent was to harm me.",
      "T": "The invitation sounded diplomatic—a meeting to discuss the situation in neutral territory. Nehemiah saw through it immediately: the remote plain of Ono was not a conference venue, it was a killing ground. The entire proposal was a trap."
    },
    "3": {
      "L": "And I sent messengers to them saying, 'I am doing a great work, so that I cannot come down. Why should the work cease while I leave it and come down to you?'",
      "M": "I sent back this reply: 'I am engaged in an important work and cannot come down. Why should the work stop while I leave it to come to you?'",
      "T": "His refusal was principled and public: 'The work I am doing matters too much to abandon.' He did not claim a prior engagement or a diplomatic excuse. The work itself was the reason—and framing it that way put the invitation's frivolousness on display."
    },
    "4": {
      "L": "And they sent to me four times after this manner, and I answered them in the same manner.",
      "M": "Four times they sent the same kind of message, and each time I gave them the same answer.",
      "T": "They tried four more times. The repetition was itself a pressure tactic—escalating urgency, testing whether persistence would erode his resolve. His answer did not change."
    },
    "5": {
      "L": "Then Sanballat sent his servant to me in the same manner a fifth time, with an open letter in his hand.",
      "M": "A fifth time, Sanballat sent his aide to me, this time carrying an unsealed letter.",
      "T": "On the fifth attempt the tactic escalated: an open letter—unsealed, readable by every courier's hand, every bystander along the route. This was a public document, designed to be circulated and read widely before it ever reached Nehemiah."
    },
    "6": {
      "L": "In it was written: 'It is reported among the nations, and Geshem also says it, that you and the Jews intend to rebel. That is why you are building the wall. And according to these reports you are about to become their king.",
      "M": "It read: 'Reports are circulating among the surrounding nations—Geshem confirms this—that you and the Jews are planning a revolt. That is the reason for the wall. And these same reports say you intend to make yourself their king.",
      "T": "The letter was a manufactured intelligence report: widespread rumors, with Geshem's name as a credibility anchor, claiming that Nehemiah's entire project was cover for a rebellion. The accusation was treason against Persia—the most dangerous charge that could be brought before Artaxerxes."
    },
    "7": {
      "L": "'And you have also appointed prophets to proclaim concerning you in Jerusalem, saying, \"There is a king in Judah!\" And now this will be reported to the king. Come now therefore, and let us take counsel together.'",
      "M": "'You have even arranged for prophets to announce in Jerusalem, \"There is a king in Judah!\" This will reach the king's ears. So come—let us work something out together.'",
      "T": "'You have lined up prophets to make your kingship official before Jerusalem hears it through other channels—and this will reach Artaxerxes.' The implied offer: come meet us and we will manage how this story reaches the king. The implied threat: refuse, and the letter goes north with our interpretation."
    },
    "8": {
      "L": "Then I sent to him saying, 'Nothing of the sort you have described has happened. You have invented all of this out of your own heart.'",
      "M": "I sent back this reply: 'None of what you describe has actually happened. You have fabricated the whole story from your own imagination.'",
      "T": "Nehemiah did not negotiate the terms of the accusation or offer a counternarrative. He denied the premise entirely: 'You made this up.' There was no ambiguous middle ground to manage—the letter was fiction, and he said so plainly."
    },
    "9": {
      "L": "For they all wanted to make us afraid, thinking, 'Their hands will drop from the work, and it will not be done.' But now, O God, strengthen my hands.",
      "M": "They were all trying to frighten us, thinking our hands would go limp and the work would stop. So I prayed: 'Now, O God, give me strength.'",
      "T": "The entire operation—the false intelligence, the open letter, the diplomatic invitations—had one goal: make the builders lose their nerve. Nehemiah named it as fear tactics, then turned to prayer. 'Strengthen my hands, God.' The builder's hand and the praying hand are the same hand."
    },
    "10": {
      "L": "Now I went to the house of Shemaiah the son of Delaiah, son of Mehetabel, who was confined to his home. And he said, 'Let us meet together in the house of God, inside the temple. Let us close the doors of the temple, for they are coming to kill you—they are coming to kill you at night.'",
      "M": "I went to the house of Shemaiah son of Delaiah, son of Mehetabel, who was homebound. He said, 'Let us meet in the house of God—inside the temple—and close the doors there, because they are coming to kill you. They will come at night to kill you.'",
      "T": "An insider came to Nehemiah: Shemaiah, a man confined to his home—possibly by ritual impurity or forced restriction. His counsel sounded like emergency protection from a sympathetic ally: flee to the temple, bar the doors, hide until the danger passes. It was precisely the kind of advice a frightened man might accept."
    },
    "11": {
      "L": "But I said, 'Should a man like me flee? And who is there that, being as I am, would go into the temple to save his life? I will not go in.'",
      "M": "I replied, 'Should a man in my position run away? And who, being in my position, would enter the temple just to save his life? I will not go in.'",
      "T": "Nehemiah's refusal had two edges. First, honor: a governor does not bolt in fear—that is cowardice, and cowardice in a leader destroys the community's will. Second, theology: he was not a priest; entering the sanctuary unlawfully would be sacrilege, not safety. His dignity and his reverence for God's law held together in one answer: 'I will not go in.'"
    },
    "12": {
      "L": "And I perceived that God had not sent him, but that he had spoken this prophecy against me because Tobiah and Sanballat had hired him.",
      "M": "I understood then that God had not sent him—he had given this prophecy against me because Tobiah and Sanballat had paid him.",
      "T": "Nehemiah's discernment was precise: the counsel did not come from God—it came from his enemies' payroll. Shemaiah was a hired prophet. The oracle was a product, not a message."
    },
    "13": {
      "L": "For this purpose he was hired, that I should be afraid and act in this way and sin, so that they could give me a bad name in order to taunt me.",
      "M": "He had been hired to frighten me into acting this way—to make me sin, so they could damage my reputation with a harmful report.",
      "T": "The trap's sophistication: if Nehemiah fled into the sanctuary in fear, he committed priestly trespass—a sin that would generate a damaging scandal. His enemies would have documentary evidence of his disgrace, delivered to the Persian court by the same hands that wrote the open letter."
    },
    "14": {
      "L": "Remember Tobiah and Sanballat, O my God, according to these their works, and also the prophetess Noadiah and the rest of the prophets who wanted to make me afraid.",
      "M": "My God, remember what Tobiah and Sanballat have done—and also the prophetess Noadiah and the other prophets who were trying to intimidate me.",
      "T": "Nehemiah's response to the hired-prophet operation was a prayer of entrusting judgment: God would remember what Tobiah and Sanballat had done. The mention of the prophetess Noadiah is notable—a named woman in a position of prophetic authority, deployed by the opposition. The psychological operation had reached into every sector of Judean society."
    },
    "15": {
      "L": "So the wall was finished on the twenty-fifth day of the month of Elul, in fifty-two days.",
      "M": "The wall was completed on the twenty-fifth day of Elul, in fifty-two days.",
      "T": "On the twenty-fifth of Elul the wall stood complete—fifty-two days from Nehemiah's first night inspection of the rubble. Against a backdrop of mockery, coordinated opposition, famine, internal debt crisis, false prophecy, and assassination plots, fifty-two days is not a construction achievement. It is a theological statement."
    },
    "16": {
      "L": "And it came to pass, when all our enemies heard of it, and all the nations around us saw it, they fell greatly in their own esteem, for they perceived that this work had been accomplished by the help of our God.",
      "M": "When all our enemies heard of it and all the surrounding nations saw it, their confidence collapsed, for they recognized that this work had been accomplished with the help of our God.",
      "T": "Every enemy, every watching nation, drew the same conclusion: the wall's completion was not explicable by human resources alone. Nehemiah's demoralized, exhausted, internally divided community had finished a defensive circuit in under two months, under active opposition. The nations lost their own confidence—and knew why."
    },
    "17": {
      "L": "Moreover, in those days the nobles of Judah were sending many letters to Tobiah, and Tobiah's letters were coming to them.",
      "M": "Meanwhile, during this period, the nobles of Judah were sending many letters to Tobiah, and Tobiah's letters were coming back to them.",
      "T": "The victory was real—but the internal security failure persisted. Judah's own nobility was in active, ongoing correspondence with Tobiah. The wall had been built; the divided community inside it had not."
    },
    "18": {
      "L": "For many in Judah were bound by oath to him, because he was the son-in-law of Shecaniah son of Arah, and his son Jehohanan had taken the daughter of Meshullam son of Berechiah as his wife.",
      "M": "Many in Judah were sworn to him by oath: he was the son-in-law of Shecaniah son of Arah, and his son Jehohanan had married the daughter of Meshullam son of Berechiah.",
      "T": "The alliance was structural, not accidental. Tobiah had married into a respected Judahite family, and his son had done the same—binding two prominent houses to him through marriage covenants. His network of in-laws reached deep into the community's leadership, and their loyalties were genuinely divided."
    },
    "19": {
      "L": "Also they would report his good deeds before me and carry my words back to him. And Tobiah sent letters to make me afraid.",
      "M": "They would speak of his good deeds to me and report my responses back to him. And Tobiah kept sending letters to intimidate me.",
      "T": "These insiders functioned as a two-way intelligence channel: lobbying Nehemiah on Tobiah's behalf while feeding Nehemiah's words directly back to the enemy. Tobiah's letters continued arriving throughout—still designed to wear Nehemiah down, still generating fear. The chapter ends not with resolution but with the ongoing reality of an adversary embedded in the community itself."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'nehemiah')
        merge_tier(existing, NEHEMIAH, tier_key)
        save(tier_dir, 'nehemiah', existing)
    print('Nehemiah 4–6 written.')

if __name__ == '__main__':
    main()
