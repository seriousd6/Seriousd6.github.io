"""
MKT 1 Samuel chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1samuel-19-24.py

Covers: Saul's repeated attempts on David's life; Jonathan's protection; David's flight to
Naioth and the Spirit falling on Saul's messengers (ch. 19); Jonathan and David's covenant,
the arrow signal, their farewell (ch. 20); David at Nob — Ahimelech gives showbread and
Goliath's sword; David feigns madness before Achish (ch. 21); Adullam, the parents to Moab,
Gad's word, the massacre at Nob, Abiathar escapes (ch. 22); David saves Keilah, the ephod
oracles, Jonathan's final visit, the Ziphite betrayal, the Rock of Escape (ch. 23); David
spares Saul in the cave — the robe, the anointed one, the cave confrontation (ch. 24).

Translation decisions:
- H3068 (יהוה): "LORD" (L/M); "the LORD" in T — consistent with all prior 1 Samuel scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H4428 (מֶלֶךְ): "king" all tiers.
- H4899 (מָשִׁיחַ, mashiach): "the LORD's anointed" (L/M); "the LORD's anointed one" (T) —
  critical to ch. 24; David's refusal to strike Saul is explicitly theological: Saul bears
  the consecration of divine appointment, and David refuses to be the one who undoes it,
  even when he has the opportunity and the provocation.
- H2617 (חֶסֶד, chesed): "kindness" (L); "steadfast love" (M); "covenant faithfulness" (T)
  — appears in 20:8,14,15 in the context of the Jonathan-David covenant; the word is
  covenant-relational, not sentimental; T surfaces the treaty-love register.
- H5315 (נֶפֶשׁ, nephesh): "soul" (L); "life" (M/T) — "as your soul lives" (20:3) is an
  oath formula; "my soul" and "his own soul" in the Jonathan love-description (20:17) is
  the totality of Jonathan's person, not an immaterial soul.
- H8655 (תְּרָפִים, teraphim): "household image/idol" — the idol Michal uses in 19:13,16;
  L/M use "image" (the closest English cognate); T names it "household idol" to clarify
  that this is a cultic object in David's house, a narrative detail the narrator does not
  editorialize about but which signals Michal's background.
- H3899+H6440 (לֶחֶם הַפָּנִים, bread of the Presence / showbread): "shewbread" (L);
  "bread of the Presence" (M/T) — the technical liturgical term for the twelve loaves
  kept perpetually before the LORD; Jesus cites this episode in Mark 2:26.
- H7307 (רוּחַ): "Spirit of God" (capitalized, ch. 19:20,23) — same divine-empowerment
  context as chs. 10-11; the repeated falling of the Spirit on Saul's messengers and then
  on Saul himself is ironic: the Spirit that once made Saul a king now humiliates him by
  making him prophesy helplessly before Samuel.
- H1285 (בְּרִית, covenant): "covenant" (L/M); "sworn covenant" or "covenant bond" (T)
  — the Jonathan-David covenant in ch. 20 is a formal treaty with oath and sign; T
  consistently treats it as a political-theological bond, not merely emotional friendship.
- H4899+David's restraint (ch. 24): David's three-part argument — the proverb (v.13),
  the self-deprecation (v.14), the appeal to divine judgment (v.15) — is carefully
  constructed rhetoric addressed to the watching men as much as to Saul. T surfaces
  the deliberate structure.
- The proverb "Out of the wicked comes wickedness" (24:13): this is David's way of saying
  "I will not commit the act that would define me as wicked — I leave justice to God."
  T surfaces this logic explicitly.
- H238 (אָזַן): "reveal / disclose to the ear" (L/M: "disclosed / told"); the Hebrew
  idiom "speak into the ear" (19:2; 20:12,13) denotes intimate private communication.
  T surfaces the intimacy in select uses.
- Ahimelech's lie on David's behalf (ch. 21): the narrator presents this without
  editorial comment; David deceives Ahimelech about his mission to protect the mission
  and the priest. Ahimelech is innocent. Doeg's presence (v.7) is ominous — the narrator
  plants the seed of the coming massacre. T flags the dramatic irony.
- The massacre at Nob (ch. 22): the killing of 85 priests and an entire priestly city —
  men, women, children, infants, animals — is presented with stark economy. The narrator
  does not moralize; the atrocity is allowed to speak. T does not soften it.
- Jonathan's final visit (23:16): "strengthened his hand in God" (חִזֵּק אֶת-יָדוֹ
  בֵּאלֹהִים) — a technical expression for giving someone courage rooted in theological
  assurance. Jonathan does not come to strategize; he comes to help David anchor his
  faith. T treats this as the deepest act of the friendship.
- "Dead dog" and "flea" (24:14): extreme self-abasement in honor-shame culture; David
  uses the language of social nullity to highlight the absurdity of the king of Israel
  hunting him. T surfaces the rhetorical strategy.
- Aspect/tense: waw-consecutive imperfects throughout rendered as English past narrative.
  No future tenses unless the Hebrew uses genuine future forms.
- H5315 ("between me and death," 20:3): "there is but a step between me and death" —
  the Hebrew is "כִּי פֶּסַע בֵּינִי וּבֵין הַמָּוֶת" — a measured step's distance;
  L preserves "a step"; M/T keep the image.
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
  "19": {
    "1": {
      "L": "And Saul spoke to Jonathan his son and to all his servants, that they should kill David. But Jonathan, son of Saul, delighted greatly in David.",
      "M": "Saul told his son Jonathan and all his servants that they should kill David. But Jonathan, Saul's son, was deeply fond of David.",
      "T": "Saul issued orders to his son Jonathan and to all his household staff: David was to be killed. But Jonathan loved David deeply and could not be part of it."
    },
    "2": {
      "L": "And Jonathan told David, saying, Saul my father seeks to kill you; now therefore take heed to yourself in the morning, and abide in a secret place and hide yourself.",
      "M": "Jonathan warned David: 'My father Saul is looking for a way to kill you. Be on guard tomorrow morning—find a hidden place and stay out of sight.'",
      "T": "Jonathan went straight to David and laid it out plainly: 'My father is planning to kill you. Tomorrow morning you must be careful—go somewhere hidden and stay there.'"
    },
    "3": {
      "L": "And I will go out and stand beside my father in the field where you are, and I will speak with my father about you; and what I see I will tell you.",
      "M": "'I will go out and stand near my father in the field where you are, and I will speak to my father about you. Whatever I learn, I will tell you.'",
      "T": "'I'll go out and take my place beside my father in the field—where you can hear—and I'll plead your case to him directly. Whatever I find out, I'll bring back to you.'"
    },
    "4": {
      "L": "And Jonathan spoke well of David to Saul his father, and said to him, Let not the king sin against his servant David; for he has not sinned against you, and because his works have been very good toward you.",
      "M": "Jonathan spoke on David's behalf to his father Saul and said to him, 'The king must not wrong his servant David—he has done nothing against you, and his service to you has been outstanding.'",
      "T": "Jonathan made his appeal to Saul directly: 'Do not sin against your servant David. He has done you no wrong. Everything he has done on your behalf has been excellent.'"
    },
    "5": {
      "L": "For he put his life in his hand and struck down the Philistine, and the LORD worked a great salvation for all Israel; you saw it and rejoiced. Why then will you sin against innocent blood by killing David without cause?",
      "M": "'He risked his life and struck down the Philistine, and the LORD won a great victory for all Israel. You saw it yourself and were glad. So why would you sin against innocent blood by killing David for no reason?'",
      "T": "'He put his life on the line to kill the Philistine champion, and the LORD gave Israel a great deliverance through him. You rejoiced at that victory. So why would you now shed innocent blood? David has given you no cause—killing him would be a sin against you, against him, and against the LORD.'"
    },
    "6": {
      "L": "And Saul hearkened to the voice of Jonathan; and Saul swore, As the LORD lives, he shall not be put to death.",
      "M": "Saul listened to Jonathan and swore an oath: 'As the LORD lives, David shall not be put to death.'",
      "T": "Saul was moved. He listened to Jonathan and swore a solemn oath: 'As the LORD lives, David will not die.' For a moment, the murderous intent was checked."
    },
    "7": {
      "L": "And Jonathan called David, and Jonathan told him all those things; and Jonathan brought David to Saul, and he was in his presence as before.",
      "M": "Jonathan called David and told him everything; then Jonathan brought David to Saul, and David served before him as before.",
      "T": "Jonathan brought David back into the full report of everything that had passed, and then brought him to Saul. For a while it was as if nothing had changed—David was back in the king's court, serving before him as before."
    },
    "8": {
      "L": "And there was war again, and David went out and fought with the Philistines and struck them with a great blow, and they fled before him.",
      "M": "War broke out again, and David went out and fought the Philistines, striking them so hard that they fled before him.",
      "T": "War with the Philistines resumed. David went out, fought, and won a decisive engagement—the Philistines broke and fled. His value to Saul was undeniable."
    },
    "9": {
      "L": "And a harmful spirit from the LORD came upon Saul as he sat in his house with his javelin in his hand; and David was playing the lyre.",
      "M": "Then a harmful spirit from the LORD came upon Saul as he sat in his house with his spear in hand, while David was playing the lyre.",
      "T": "But then it struck again—the harmful spirit from the LORD, the inner turbulence that had seized Saul before. He sat in his house, spear in hand, as David played to calm him."
    },
    "10": {
      "L": "And Saul sought to pin David to the wall with the javelin; but he slipped away from before Saul, so that he struck the javelin into the wall; and David fled and escaped that night.",
      "M": "Saul drove the spear at David, trying to pin him to the wall. But David dodged, and the spear stuck in the wall. David fled and got away that night.",
      "T": "Saul's arm moved without warning—the spear flew at David to pin him to the wall. David stepped aside; the spear buried itself in the wall. David ran for his life into the night."
    },
    "11": {
      "L": "Saul also sent messengers to David's house to watch him, that he might kill him in the morning; but Michal, David's wife, told him, saying, If you do not save your life tonight, tomorrow you will be killed.",
      "M": "Saul sent agents to David's house to watch him through the night and kill him in the morning. But David's wife Michal warned him: 'If you don't get out tonight, you will be dead by morning.'",
      "T": "Saul's network moved quickly: agents were posted around David's house to watch through the night and execute him at first light. But Michal—David's own wife, Saul's own daughter—pulled David aside. 'If you don't run tonight,' she said, 'you will not be alive by morning.'"
    },
    "12": {
      "L": "So Michal let David down through the window, and he went and fled and escaped.",
      "M": "Michal lowered David through a window, and he ran and fled and escaped.",
      "T": "Michal helped him through the window in the dark, and David dropped down and ran—and escaped."
    },
    "13": {
      "L": "And Michal took the household image and laid it on the bed and put a pillow of goat hair at its head and covered it with a garment.",
      "M": "Michal took a household idol, placed it in the bed, put a cushion of goat hair at the head, and covered it with a garment.",
      "T": "Michal bought him more time. She placed the household idol in the bed, arranged a cushion of goat hair where the head would be, and draped a garment over the whole shape."
    },
    "14": {
      "L": "When Saul sent messengers to take David, she said, He is sick.",
      "M": "When Saul's messengers came to take David, she said, 'He is ill.'",
      "T": "When Saul's agents arrived to seize David, Michal met them calmly: 'He's sick in bed—he can't be moved.'"
    },
    "15": {
      "L": "Then Saul sent the messengers again to see David, saying, Bring him up to me in the bed, that I may kill him.",
      "M": "Saul sent the messengers back with orders: 'Bring him to me in his bed—I'll kill him there.'",
      "T": "Saul's patience was gone. He sent them back with explicit instructions: 'Bring him to me in the bed if you have to—I will kill him myself.'"
    },
    "16": {
      "L": "And when the messengers came in, behold, the household image was in the bed, with the pillow of goat hair at its head.",
      "M": "When the messengers went in, they found the idol in the bed with a cushion of goat hair where the head should be.",
      "T": "The messengers went in and pulled back the covers—and found an idol, not David. Michal's deception had worked."
    },
    "17": {
      "L": "Saul said to Michal, Why have you deceived me thus and let my enemy go, so that he has escaped? And Michal answered Saul, He said to me, Let me go; why should I kill you?",
      "M": "Saul demanded of Michal, 'Why have you deceived me like this and helped my enemy escape?' Michal replied, 'He threatened me—he said, \"Let me go, or I will kill you.\"'",
      "T": "Saul confronted his daughter: 'Why did you deceive me? You let my enemy escape!' Michal deflected the blame onto David: 'He threatened me—he said if I didn't let him go, he would kill me.' She had no choice. Or so she claimed."
    },
    "18": {
      "L": "Now David fled and escaped, and came to Samuel at Ramah and told him all that Saul had done to him. And he and Samuel went and stayed at Naioth.",
      "M": "David fled and escaped, came to Samuel at Ramah, and told him everything Saul had done to him. And he and Samuel went and stayed at Naioth.",
      "T": "David made for Ramah and Samuel. He needed the prophet—the one who had anointed him—and he told Samuel the whole story of Saul's murderous pursuit. The two of them withdrew together to Naioth."
    },
    "19": {
      "L": "And it was told Saul, saying, Behold, David is at Naioth in Ramah.",
      "M": "Word reached Saul: 'David is at Naioth in Ramah.'",
      "T": "Saul's network reported the location: David was at Naioth in Ramah, in the prophet's compound."
    },
    "20": {
      "L": "Then Saul sent messengers to take David; and when they saw the company of the prophets prophesying, with Samuel standing as head over them, the Spirit of God came upon the messengers of Saul, and they also prophesied.",
      "M": "Saul sent agents to seize David. When they arrived and saw the company of prophets prophesying with Samuel standing at their head, the Spirit of God came upon Saul's agents and they too began to prophesy.",
      "T": "Saul dispatched his men. They arrived at Naioth and found a band of prophets in full prophetic activity—Samuel presiding over them. And then something happened that no one ordered: the Spirit of God fell on Saul's own agents, and they began to prophesy with the rest."
    },
    "21": {
      "L": "When it was told Saul, he sent other messengers, and they also prophesied. And Saul sent again, the third time, and they also prophesied.",
      "M": "When Saul was told this, he sent another group of agents—and they too prophesied. He sent a third group, and they too prophesied.",
      "T": "Word came back to Saul: his first squad had broken out in prophecy. He sent a second. The same thing happened. He sent a third. Again the Spirit overwhelmed them before they could lay hands on David."
    },
    "22": {
      "L": "Then he himself went to Ramah and came to the great well at Sechu; and he asked, saying, Where are Samuel and David? And one said, Behold, they are at Naioth in Ramah.",
      "M": "Then Saul himself went to Ramah. He came to the great cistern at Sechu and asked, 'Where are Samuel and David?' Someone said, 'They are at Naioth in Ramah.'",
      "T": "Finally Saul went himself. He arrived at the great cistern at Sechu outside Ramah and asked where Samuel and David were. He was pointed to Naioth."
    },
    "23": {
      "L": "And he went there to Naioth in Ramah. And the Spirit of God came upon him also, and he went prophesying as he went, until he came to Naioth in Ramah.",
      "M": "He set out for Naioth in Ramah—and the Spirit of God came upon him as he walked, and he prophesied all the way until he arrived at Naioth.",
      "T": "Saul headed for Naioth—and the Spirit of God overtook him before he arrived. He prophesied as he walked, the whole distance. The king who had come to kill his former servant arrived unable to do anything but prophesy."
    },
    "24": {
      "L": "And he too stripped off his garments, and he too prophesied before Samuel and lay naked all that day and all that night. Therefore they say, Is Saul also among the prophets?",
      "M": "He stripped off his garments and prophesied before Samuel as well, and lay naked all that day and all that night. That is why people say, 'Is Saul also among the prophets?'",
      "T": "Saul stripped off his royal garments and lay there before Samuel, prophesying all through the day and into the night—helpless, naked, exposed. The man who had come to kill was rendered utterly harmless by the same Spirit that had once made him king. The proverb said it all: 'Is Saul also among the prophets?'"
    }
  },
  "20": {
    "1": {
      "L": "Then David fled from Naioth in Ramah and came and said before Jonathan, What have I done? What is my guilt? And what is my sin before your father, that he seeks my life?",
      "M": "David fled from Naioth in Ramah, came to Jonathan, and asked, 'What have I done? What is my wrongdoing? What sin have I committed against your father, that he is trying to kill me?'",
      "T": "David came straight from Naioth to Jonathan—shaken, urgent, needing to understand. 'What have I done wrong? What offense have I committed against your father? Why does he want me dead?'"
    },
    "2": {
      "L": "And he said to him, Far be it! You shall not die. Behold, my father does nothing either great or small without disclosing it to me. And why would my father hide this from me? It is not so.",
      "M": "Jonathan replied, 'Far from it—you will not die! My father never acts, great or small, without telling me. Why would he hide something like this from me? He hasn't.'",
      "T": "Jonathan reassured him: 'That's not possible. You are not going to die. My father doesn't make a move—nothing big, nothing small—without telling me first. If he intended to kill you, I would know.' But Jonathan did not yet know the depth of his father's madness."
    },
    "3": {
      "L": "But David swore more, and said, Your father knows well that I have found favor in your eyes, and he has thought, Let not Jonathan know this, lest he be grieved; yet truly as the LORD lives, and as your soul lives, there is but a step between me and death.",
      "M": "But David insisted with an oath: 'Your father knows that I have found favor with you—and that is precisely why he has decided not to tell you, so you would not be grieved. But I swear by the LORD and by your own life: there is only a step between me and death.'",
      "T": "'Jonathan, think it through. Your father knows how you feel about me—and that is exactly why he has hidden this from you. He doesn't want you to grieve, or to warn me. I am telling you, and I swear by the LORD and by your very life: one step is all that separates me from death right now.'"
    },
    "4": {
      "L": "Then Jonathan said to David, Whatever your soul desires, I will do for you.",
      "M": "Jonathan said to David, 'Whatever you want me to do, I will do it.'",
      "T": "Jonathan's answer was complete loyalty: 'Whatever you need me to do—I will do it.'"
    },
    "5": {
      "L": "And David said to Jonathan, Behold, tomorrow is the new moon, and I should not fail to sit with the king at table; but let me go, that I may hide myself in the field until the evening of the third day.",
      "M": "David said to Jonathan, 'Tomorrow is the new moon festival, and I should be sitting with the king at the feast—but let me go, so I can hide in the field until the third evening.'",
      "T": "'Here is the situation: tomorrow is the new moon feast—I would normally be at the king's table. But let me disappear into the countryside and stay hidden until the third evening. That will tell us something.'"
    },
    "6": {
      "L": "If your father misses me at all, then say, David earnestly asked leave of me to run to Bethlehem his city, for there is a yearly sacrifice there for all the clan.",
      "M": "'If your father notices I'm absent, tell him: \"David asked urgently for my permission to go to Bethlehem—there is an annual family sacrifice there.\"'",
      "T": "'If your father asks about me, tell him this: \"David begged me to let him go home to Bethlehem for the clan's annual sacrifice. He felt he had to be there.\" That's the cover story.'"
    },
    "7": {
      "L": "If he says, Good! it will be well with your servant; but if he is very angry, then know that harm is determined by him.",
      "M": "'If he says \"That's fine,\" then all is well with me. But if he flares up in anger, you'll know he has decided to harm me.'",
      "T": "'If he shrugs it off, I'm safe. But if he erupts—then you will know. It won't be ambiguous. His anger will tell you everything.'"
    },
    "8": {
      "L": "Therefore deal kindly with your servant, for you have brought your servant into a covenant of the LORD with you; but if there is guilt in me, you yourself kill me, for why should you bring me to your father?",
      "M": "'So show your covenant loyalty to your servant—you yourself brought me into a covenant before the LORD with you. If I have done anything wrong, kill me yourself. Why should you hand me over to your father?'",
      "T": "'I'm asking you to honor the covenant we made before the LORD, you and I together. If I have wronged you or your father in any real way, execute me yourself—you are within your rights. But don't deliver me to him.'"
    },
    "9": {
      "L": "Jonathan said, Far be it from you! For if I knew certainly that harm was determined by my father to come upon you, would I not tell you?",
      "M": "Jonathan replied, 'Far from that! If I knew for certain that my father had decided to harm you, I would absolutely tell you.'",
      "T": "'Don't even think that,' Jonathan said. 'If I found out my father was set on destroying you, I would come and tell you myself. I promise you that.'"
    },
    "10": {
      "L": "Then David said to Jonathan, Who will tell me if your father answers you roughly?",
      "M": "David said to Jonathan, 'Who will let me know if your father answers you harshly?'",
      "T": "'But how will I know?' David pressed. 'How will you get the message to me if your father responds with fury?'"
    },
    "11": {
      "L": "And Jonathan said to David, Come, and let us go out into the field. And they both went out into the field.",
      "M": "Jonathan said to David, 'Come, let's go out to the field.' And they went out together.",
      "T": "'Come,' Jonathan said. 'Out to the field—I have a plan.' And they went out together, away from walls and ears."
    },
    "12": {
      "L": "And Jonathan said to David, O LORD, the God of Israel, when I have sounded out my father about this time tomorrow, or the third day, and behold it is good toward David, and I do not then send to you and reveal it to you,",
      "M": "Jonathan said to David, 'By the LORD, the God of Israel—when I sound out my father tomorrow or the day after, and if the situation looks favorable to David, and I do not immediately send word to let you know,'",
      "T": "Jonathan laid out the signal and the oath: 'I call the LORD, God of Israel, to witness. When I have probed my father's intentions—tomorrow, or the day after at the latest—if things look safe for you and I fail to send and tell you,'"
    },
    "13": {
      "L": "may the LORD do so to Jonathan and more also. But if my father intends harm to you, I will reveal it to you and send you away, that you may go in safety; and may the LORD be with you as he was with my father.",
      "M": "'—then may the LORD punish me, and severely. But if my father means to harm you, I will warn you and send you away safely. May the LORD be with you as he was with my father.'",
      "T": "'—then let the LORD punish me severely. But if my father is set on harming you, I will tell you so you can flee safely. And may the LORD be with you the way he was once with my father—as a constant companion and defender.'"
    },
    "14": {
      "L": "And if I am still alive, show me the steadfast love of the LORD, that I may not die;",
      "M": "'And if I am still alive, show me the steadfast love of the LORD—don't let me die—'",
      "T": "'And if I am still alive when the LORD has established you—show me the covenant faithfulness of the LORD. Don't let me be abandoned.'"
    },
    "15": {
      "L": "and do not cut off your kindness from my house forever; not even when the LORD cuts off every one of the enemies of David from the face of the earth.",
      "M": "'—and never cut off your steadfast love from my house, even when the LORD has cut off all of David's enemies from the face of the earth.'",
      "T": "'And when your enemies—every last one—have been removed by the LORD, don't cut off your faithfulness from my household. Remember us.' Jonathan was already speaking of David's kingship as a foregone conclusion."
    },
    "16": {
      "L": "And Jonathan made a covenant with the house of David, saying, May the LORD require it at the hand of David's enemies.",
      "M": "So Jonathan made a covenant with the house of David, saying, 'May the LORD hold David's enemies to account.'",
      "T": "Jonathan formally sealed a covenant with David's house. He called the LORD to enforce it: any enemy of David who broke this bond would answer to God."
    },
    "17": {
      "L": "And Jonathan made David swear again by his love for him, for he loved him as he loved his own soul.",
      "M": "Jonathan made David swear it again—because of his love for David, for he loved him as his own self.",
      "T": "Jonathan pressed David to swear the covenant again. He loved David that deeply—not politically, not strategically—with the same love a man has for his own life, for his own person."
    },
    "18": {
      "L": "Then Jonathan said to him, Tomorrow is the new moon; and you will be missed, because your seat will be empty.",
      "M": "Jonathan said to him, 'Tomorrow is the new moon feast, and your absence will be noticed—your seat will be empty.'",
      "T": "Jonathan rehearsed the plan: 'Tomorrow is the new moon. The king will look for you. Your place at the table will be empty.'"
    },
    "19": {
      "L": "On the third day go down quickly to the place where you hid yourself on the day of the matter, and remain beside the stone Ezel.",
      "M": "'On the third day go quickly to the place where you hid when this trouble started, and stay beside the stone called Ezel.'",
      "T": "'On the third day, go quickly to where you hid before—beside the stone Ezel. Stay there and watch.'"
    },
    "20": {
      "L": "And I will shoot three arrows to the side of it, as though I shot at a mark.",
      "M": "'I will shoot three arrows to the side of it, as if I were shooting at a target.'",
      "T": "'I'll shoot three arrows in that direction, as if I'm practicing at a mark. The arrows will carry the message.'"
    },
    "21": {
      "L": "And behold, I will send the boy, saying, Go, find the arrows. If I say to the boy, Look, the arrows are on this side of you—take them—then come, for there is peace for you and no danger, as the LORD lives.",
      "M": "'I will send the boy, saying, \"Find the arrows.\" If I call to him, \"Look, the arrows are on this side of you—pick them up,\" then come out; there is safety for you, no threat. As the LORD lives, it is clear.'",
      "T": "'I'll send my boy to retrieve them. If I shout to him, \"The arrows are on this side—pick them up,\" then come out. The signal means: it's safe, you can return. I swear it by the LORD's life.'"
    },
    "22": {
      "L": "But if I say to the youth, Behold, the arrows are beyond you—then go, for the LORD has sent you away.",
      "M": "'But if I say to the boy, \"The arrows are farther out,\" then go—for the LORD has sent you away.'",
      "T": "'But if I shout that the arrows are farther on—beyond you—then run. That signal means the LORD himself is releasing you, sending you away from here.'"
    },
    "23": {
      "L": "And as for the matter of which you and I have spoken, behold, the LORD is between you and me forever.",
      "M": "'And as for everything we have agreed on between us—the LORD is witness between you and me forever.'",
      "T": "'And as for the covenant we have just made—the LORD himself stands between us as witness. This bond holds forever, whatever comes.'"
    },
    "24": {
      "L": "So David hid in the field; and when the new moon came, the king sat down to eat food.",
      "M": "David hid in the field. When the new moon came, the king sat down to eat.",
      "T": "David went into hiding in the countryside. The new moon feast came, and the king took his place at the table."
    },
    "25": {
      "L": "The king sat on his seat, as at other times, on the seat by the wall; Jonathan arose, and Abner sat by Saul's side, but David's place was empty.",
      "M": "The king sat in his usual seat against the wall, Jonathan sat opposite, and Abner sat beside Saul—but David's place was vacant.",
      "T": "Saul took his customary seat by the wall. Jonathan and Abner were in their usual positions. David's place sat empty, conspicuous in its absence."
    },
    "26": {
      "L": "Yet Saul said nothing that day, for he thought, Something has happened to him; he is not clean—surely he is not clean.",
      "M": "Saul said nothing that day, thinking, 'Something has happened to him—he must be ceremonially unclean; yes, he must be unclean.'",
      "T": "Saul noticed but said nothing. He assumed a ritual explanation: David must be ceremonially unclean—an absence on those grounds was normal and needed no comment."
    },
    "27": {
      "L": "But on the next day, the second day of the month, David's place was empty. And Saul said to Jonathan his son, Why has the son of Jesse not come to the meal, either yesterday or today?",
      "M": "But on the following day, the second day of the month, David's place was still empty. Saul said to his son Jonathan, 'Why hasn't the son of Jesse come to the meal—not yesterday, and not today either?'",
      "T": "The second day came, and David's seat was still empty. Saul's patience was exhausted. He turned on Jonathan: 'Why hasn't Jesse's son come to the feast? Two days now—where is he?'"
    },
    "28": {
      "L": "Jonathan answered Saul, David earnestly asked leave of me to go to Bethlehem.",
      "M": "Jonathan replied to Saul, 'David asked my permission urgently to go to Bethlehem.'",
      "T": "Jonathan delivered the agreed story: 'David asked me urgently for permission to go home to Bethlehem.'"
    },
    "29": {
      "L": "He said, Please let me go, for our clan has a sacrifice in the city, and my brother has commanded me to be there; and now, if I have found favor in your eyes, let me get away, I pray, and see my brothers. Therefore he has not come to the king's table.",
      "M": "'He said, \"Please let me go—our family has a sacrifice in the city and my brother insisted I be there. If I have found any favor in your eyes, let me slip away to see my brothers.\" That is why he is not at the king's table.'",
      "T": "'He said his family had a sacrifice in the city—his brother had specifically commanded him to be there. He asked me if he had my favor—and I let him go. That is why he is not here.'"
    },
    "30": {
      "L": "Then Saul's anger burned against Jonathan, and he said to him, You son of a perverse, rebellious woman! Do I not know that you have chosen the son of Jesse to your own shame and to the shame of your mother's nakedness?",
      "M": "Saul's anger flared at Jonathan, and he shouted at him, 'You son of a twisted, rebellious woman! Do I not know that you have sided with Jesse's son to your own disgrace and to your mother's disgrace?'",
      "T": "Saul erupted. His rage was not just at David—it turned on his own son. The insult he hurled was savage: 'You son of a perverse and rebellious woman!' He attacked Jonathan's loyalty, his legitimacy, his mother. In that culture, to shame the mother was to shame the son to the core."
    },
    "31": {
      "L": "For as long as the son of Jesse lives on earth, neither you nor your kingdom shall be established. Therefore now send and bring him to me, for he shall surely die.",
      "M": "'For as long as Jesse's son lives on this earth, neither you nor your kingdom will stand. Now send for him and bring him to me—he must die.'",
      "T": "'As long as Jesse's son is alive, you will never have a kingdom. He will take everything from you. Now stop protecting him and bring him to me—he has to die.' Saul could see what Jonathan would not: David's rise was Jonathan's displacement."
    },
    "32": {
      "L": "Then Jonathan answered Saul his father and said to him, Why should he be put to death? What has he done?",
      "M": "Jonathan answered his father Saul: 'Why should he die? What has he done?'",
      "T": "Jonathan stood his ground. Even under his father's fury he pressed back: 'Why does he deserve to die? What crime has he committed?'"
    },
    "33": {
      "L": "And Saul hurled the javelin at him to strike him; so Jonathan knew that his father was determined to put David to death.",
      "M": "Saul hurled his spear at Jonathan to strike him. That was how Jonathan knew his father was fully determined to kill David.",
      "T": "Saul's answer was a javelin. He threw it at his own son. That answered every question Jonathan had asked. His father was beyond reasoning with."
    },
    "34": {
      "L": "So Jonathan rose from the table in fierce anger and ate no food the second day of the month, for he was grieved for David, because his father had disgraced him.",
      "M": "Jonathan rose from the table furious and ate nothing that second day of the month, grieving for David because his father had shamed him.",
      "T": "Jonathan left the table. He couldn't eat. His grief was layered: for David, who was in danger; for his father, who had thrown a spear at his own son; for himself, caught between a loyalty he could not abandon and a father who had chosen murderous shame."
    },
    "35": {
      "L": "In the morning Jonathan went out into the field to the appointment with David, and with him a little boy.",
      "M": "In the morning Jonathan went out to the field to the appointed place with David, and a young servant went with him.",
      "T": "At dawn Jonathan went out to the field and the appointed place, a young boy at his side."
    },
    "36": {
      "L": "And he said to his boy, Run and find the arrows that I shoot. As the boy ran, he shot an arrow beyond him.",
      "M": "He said to the boy, 'Run and find the arrows I shoot.' As the boy ran, Jonathan shot an arrow that flew past him.",
      "T": "He told the boy to go ahead and retrieve whatever he shot. The boy ran out, and Jonathan shot—sending the arrow well past the boy, into the field beyond."
    },
    "37": {
      "L": "And when the boy came to the place of the arrow that Jonathan had shot, Jonathan called after the boy and said, Is not the arrow beyond you?",
      "M": "When the boy reached the place where the arrow had landed, Jonathan called out, 'The arrow is farther out, isn't it?'",
      "T": "When the boy reached the arrow, Jonathan called out loud: 'The arrow went farther on—didn't it?' The signal was given."
    },
    "38": {
      "L": "And Jonathan called after the boy, Hurry! Be quick! Do not stay! And Jonathan's boy gathered up the arrows and came to his master.",
      "M": "Jonathan called to him, 'Hurry! Don't stop!' The boy gathered the arrows and came back to his master.",
      "T": "He called urgently, 'Quickly! Don't linger!' The boy gathered the arrows and ran back. Nothing seemed amiss to the child."
    },
    "39": {
      "L": "But the boy knew nothing; only Jonathan and David knew the matter.",
      "M": "The boy knew nothing of the meaning; only Jonathan and David understood the signal.",
      "T": "The boy knew nothing—he had retrieved arrows, nothing more. Only Jonathan and David understood what had passed between them."
    },
    "40": {
      "L": "Then Jonathan gave his weapons to his boy and said to him, Go and carry them to the city.",
      "M": "Jonathan handed his weapons to the boy and said, 'Go take these back to the city.'",
      "T": "Jonathan handed off his gear to the boy and sent him back to town."
    },
    "41": {
      "L": "And as soon as the boy was gone, David rose from beside the mound and fell on his face to the ground and bowed three times; and they kissed one another and wept with one another, until David made it exceed.",
      "M": "As soon as the boy was gone, David came out from beside the mound, fell on his face to the ground and bowed three times. Then they kissed each other and wept together, David weeping the most.",
      "T": "The moment the boy was out of sight David came out from his hiding place, fell to the ground before Jonathan three times in full prostration, and they came together. They wept. They held each other. David wept most of all—perhaps because he already knew this was the last time."
    },
    "42": {
      "L": "And Jonathan said to David, Go in peace, forasmuch as we have sworn, both of us, in the name of the LORD, saying, The LORD shall be between you and me, and between my offspring and your offspring, forever. Then he arose and departed, and Jonathan went into the city.",
      "M": "Jonathan said to David, 'Go in peace—we have both sworn in the LORD's name: the LORD shall be between you and me, and between my offspring and yours, forever.' David arose and left, and Jonathan went back into the city.",
      "T": "'Go in peace,' Jonathan said. 'We have sworn this to each other by the LORD: he stands between you and me, and between our families, forever.' David rose and departed into exile. Jonathan turned and walked back to the city. Each went toward a very different future."
    }
  },
  "21": {
    "1": {
      "L": "Then David came to Nob, to Ahimelech the priest; and Ahimelech came trembling to meet David and said to him, Why are you alone, and no one is with you?",
      "M": "David came to Nob, to Ahimelech the priest. Ahimelech came out to meet him trembling and said, 'Why are you alone? Where is everyone?'",
      "T": "David made his way to Nob, to the priest Ahimelech. Ahimelech's trembling as he came out to meet David is telling—something about David's solitude and urgency alarmed the priest at once. 'Why are you alone?' he asked. 'Where are your men?'"
    },
    "2": {
      "L": "And David said to Ahimelech the priest, The king has charged me with a matter and said to me, Let no one know anything of the matter about which I send you, and with which I have charged you. And I have made an appointment with the young men for such and such a place.",
      "M": "David told the priest, 'The king has sent me on a confidential mission. He instructed me not to tell anyone what he has assigned me to do or where he has sent me. As for my men—I have arranged to meet them at a certain location.'",
      "T": "David lied. 'The king sent me on a secret mission,' he told Ahimelech. 'He gave strict orders—no one is to know the details. My men are waiting for me at a prearranged point.' It was a fabrication from the first word. David was a fugitive, not a royal envoy. Ahimelech had no way to know."
    },
    "3": {
      "L": "Now therefore what do you have at hand? Give me five loaves of bread, or whatever is available.",
      "M": "'Now, what do you have available? Give me five loaves of bread, or whatever there is.'",
      "T": "'So give me what you have—five loaves of bread, or whatever you can spare.' He needed provisions and he needed them quickly."
    },
    "4": {
      "L": "And the priest answered David and said, There is no common bread at hand, but there is holy bread—if only the young men have kept themselves from women.",
      "M": "The priest replied, 'I have no ordinary bread—only the sacred bread. But that I can give you, if your men have kept away from women.'",
      "T": "Ahimelech had a problem: only the sacred bread was on hand—the bread of the Presence. He could offer it, but only if those who ate it were ritually clean. 'Are your men holy? Have they kept from women?'"
    },
    "5": {
      "L": "And David answered the priest, Truly, women have been kept from us as always when I go on an expedition; and the vessels of the young men are holy even when it is a common journey. How much more today will their vessels be holy?",
      "M": "David answered, 'Indeed, women have been kept from us as always on campaign. Even on ordinary missions the men keep themselves holy. Certainly today they are clean.'",
      "T": "David pressed the case: 'We always maintain ritual purity on military duty. Even on routine missions the men are clean. Today especially—they are certainly ready to eat holy bread.' The priest accepted the answer."
    },
    "6": {
      "L": "So the priest gave him the holy bread, for there was no bread there but the bread of the Presence, which is removed from before the LORD, to be replaced by hot bread on the day it is taken away.",
      "M": "So the priest gave him the sacred bread—the only bread available was the bread of the Presence, which is taken from before the LORD and replaced with fresh loaves on the day it is removed.",
      "T": "Ahimelech gave David the bread of the Presence—the loaves that had been set before the LORD in the sanctuary. These were taken out on their rotation day and replaced with fresh-baked loaves; Ahimelech gave David those outgoing loaves. It was technically lawful; it was also extraordinary—holy bread for a fugitive."
    },
    "7": {
      "L": "Now a certain man of the servants of Saul was there that day, detained before the LORD; his name was Doeg the Edomite, the chief of Saul's herdsmen.",
      "M": "A man of Saul's servants happened to be there that day, held before the LORD—Doeg the Edomite, the head of Saul's herdsmen.",
      "T": "One ominous detail: Doeg the Edomite was there. He was Saul's chief herdsman, detained at the sanctuary for some religious obligation. He saw everything. The narrator plants this fact like a seed of coming horror."
    },
    "8": {
      "L": "And David said to Ahimelech, And is there not here at hand a spear or a sword? For I have brought neither my sword nor my weapons with me, because the king's business required haste.",
      "M": "David asked Ahimelech, 'Is there a spear or sword here? I didn't bring my weapons—the king's errand required me to leave quickly.'",
      "T": "'One more thing,' David said. 'Do you have a sword or a spear? I left mine behind—the mission required speed.' Another part of the fiction. He had been running for his life."
    },
    "9": {
      "L": "And the priest said, The sword of Goliath the Philistine, whom you struck down in the Valley of Elah—behold, it is here wrapped in a cloth behind the ephod; if you will take that, take it, for there is none here but that. And David said, There is none like that; give it to me.",
      "M": "The priest replied, 'The sword of Goliath the Philistine—the one you struck down in the Valley of Elah—is here, wrapped in cloth behind the ephod. If you want it, take it; there's nothing else.' David said, 'There's nothing like it; give it to me.'",
      "T": "Ahimelech had exactly one weapon: the sword of Goliath. The great champion David had killed was now memorialized here in the sanctuary behind the ephod, his own weapon wrapped in cloth. The priest offered it. David took it without hesitation: 'There is none like it.' The weapon of his greatest victory would see him through his deepest crisis."
    },
    "10": {
      "L": "And David rose and fled that day from before Saul, and went to Achish the king of Gath.",
      "M": "David rose and fled that day from before Saul and went to Achish the king of Gath.",
      "T": "David left Nob and headed into Philistia—to Achish, king of Gath. Desperation, or strategy, or both: he was running toward the last place Saul would expect."
    },
    "11": {
      "L": "And the servants of Achish said to him, Is not this David the king of the land? Did they not sing of him to one another in dances, saying, Saul has struck down his thousands, and David his ten thousands?",
      "M": "Achish's servants said to him, 'Isn't this David, the king of the land? Isn't this the one they sing about in their dances: \"Saul has struck down his thousands, and David his ten thousands\"?'",
      "T": "Achish's courtiers recognized him immediately: 'Isn't this David? The king of the land? The one Israel celebrates in song—Saul with his thousands, David with his ten thousands?' They knew exactly who was standing in their court. And they knew what it meant."
    },
    "12": {
      "L": "And David took these words to heart and was very much afraid of Achish the king of Gath.",
      "M": "David took this seriously and was very afraid of Achish the king of Gath.",
      "T": "David heard what they were saying and felt the danger. He was not among friends. He was in the court of an enemy king who had every reason to use him as a political asset—or simply kill him."
    },
    "13": {
      "L": "So he changed his behavior before them and pretended to be insane in their hands, and scrabbled on the doors of the gate and let his spittle fall down upon his beard.",
      "M": "So he altered his behavior before them, acting as if he were insane—scratching at the doors of the gate and letting saliva dribble down his beard.",
      "T": "David improvised. He began acting deranged—scratching at the city gates, letting spit run down his beard, making himself as undignified and harmless as possible. The greatest warrior in Israel played the madman to survive."
    },
    "14": {
      "L": "Then Achish said to his servants, Look, you see the man is mad; why have you brought him to me?",
      "M": "Achish said to his servants, 'Look at this man—he's obviously mad! Why did you bring him to me?'",
      "T": "Achish was annoyed: 'The man is clearly mad. Why did you bring him to me?'"
    },
    "15": {
      "L": "Am I short of madmen, that you have brought this fellow to behave as a madman in my presence? Shall this fellow come into my house?",
      "M": "'Do I need madmen, that you've brought this one to carry on in front of me? Is this man supposed to come into my palace?'",
      "T": "'Do I have a shortage of lunatics, that you import them from Israel? Get him out of here. He is not coming into my house.' David's plan worked. The deception saved his life."
    }
  },
  "22": {
    "1": {
      "L": "David therefore departed from there and escaped to the cave of Adullam; and when his brothers and all his father's house heard it, they went down there to him.",
      "M": "David left there and escaped to the cave of Adullam. When his brothers and all his father's household heard, they went down there to him.",
      "T": "David found his way to the cave of Adullam—a stronghold in the borderlands of Judah. When his family got word of where he was, they came: his brothers, his father's whole household. Even Jesse came. The family closed ranks around the son who had become an outlaw."
    },
    "2": {
      "L": "And everyone who was in distress, and everyone who was in debt, and everyone who was bitter in soul, gathered to him; and he became captain over them; and there were with him about four hundred men.",
      "M": "All who were under pressure, all in debt, and all who were bitter came to him, and he became their leader. About four hundred men were with him.",
      "T": "And then the dispossessed came: men in crisis, men crushed by debt, men whose lives had soured beyond recovery. They found their way to David's cave and gathered around him—about four hundred of them. He became their leader. The future king was assembling his army, whether he knew it or not, from the rejects and the desperate of Israel."
    },
    "3": {
      "L": "And David went from there to Mizpeh of Moab; and he said to the king of Moab, Please let my father and my mother come out and stay with you, until I know what God will do for me.",
      "M": "From there David went to Mizpeh of Moab and asked the king of Moab, 'Please let my father and mother stay with you until I know what God will do for me.'",
      "T": "David's first act was to protect his parents. He went to the king of Moab—a natural connection, given that David's great-grandmother Ruth was Moabite—and asked for asylum for Jesse and his wife. 'I don't know yet how this will end. Let them stay with you until I do.'"
    },
    "4": {
      "L": "And he left them with the king of Moab, and they stayed with him all the time that David was in the stronghold.",
      "M": "He left them in the king of Moab's care, and they stayed there all the while David was in the stronghold.",
      "T": "The king of Moab agreed, and David's parents lived there safely for the duration of his time in hiding. He had put them beyond Saul's reach."
    },
    "5": {
      "L": "And the prophet Gad said to David, Do not remain in the stronghold; depart, and go into the land of Judah. So David departed and went into the forest of Hereth.",
      "M": "The prophet Gad told David, 'Don't stay in the stronghold—go into the land of Judah.' So David left and went to the forest of Hereth.",
      "T": "The prophet Gad brought a word: leave the stronghold, go back into Judah. David obeyed without question. He moved to the forest of Hereth in Judah—still hiding, but where God had directed him."
    },
    "6": {
      "L": "When Saul heard that David and the men who were with him had been discovered, Saul was sitting at Gibeah, under the tamarisk tree on the height, with his spear in his hand and all his servants standing about him.",
      "M": "Saul heard that David and his men had been located. He was sitting at Gibeah under the tamarisk tree on the hill, his spear in hand, with all his servants standing around him.",
      "T": "Word reached Saul: David had been spotted, and he had men with him. Saul was holding court on the hill at Gibeah, seated under the tamarisk tree with his spear—always the spear—his servants arrayed around him. It was a portrait of paranoia and power."
    },
    "7": {
      "L": "And Saul said to his servants who stood about him, Hear now, you Benjaminites! Will the son of Jesse give every one of you fields and vineyards, will he make you all commanders of thousands and commanders of hundreds,",
      "M": "Saul said to his servants, 'Listen, all you Benjaminites! Will Jesse's son give every one of you fields and vineyards? Will he make you commanders over thousands and hundreds?'",
      "T": "Saul addressed his inner circle with wounded, suspicious fury: 'You are Benjaminites—my own tribe. Will Jesse's son reward you the way I have? Will he give you land? Promote you? You are betting on the wrong king.'"
    },
    "8": {
      "L": "that all of you have conspired against me? No one reveals to me when my son makes a covenant with the son of Jesse. And none of you is sorry for me or reveals to me that my son has stirred up my servant against me, to lie in wait, as at this day.",
      "M": "'Has every one of you conspired against me? No one told me when my own son made a pact with Jesse's son. None of you grieves for me. None of you told me that my son has incited my own servant to ambush me—as he is doing today.'",
      "T": "'You are all in on it, aren't you? My own son made a covenant with David and not one of you told me. Not one of you feels anything for me. No one said: your son is working against you, he has turned your servant into your enemy. I am surrounded by treachery.' Saul's paranoia was consuming him—turning every loyalty into betrayal."
    },
    "9": {
      "L": "Then Doeg the Edomite, who was stationed over the servants of Saul, answered and said, I saw the son of Jesse coming to Nob, to Ahimelech the son of Ahitub.",
      "M": "Doeg the Edomite, who was standing with Saul's servants, replied, 'I saw Jesse's son come to Nob—to Ahimelech son of Ahitub.'",
      "T": "Doeg the Edomite stepped forward. He had been waiting for this moment. 'I saw Jesse's son at Nob. He went to Ahimelech the priest—Ahitub's son.'"
    },
    "10": {
      "L": "And he inquired of the LORD for him and gave him provisions and gave him the sword of Goliath the Philistine.",
      "M": "'Ahimelech inquired of the LORD for him, gave him food, and handed over the sword of Goliath the Philistine.'",
      "T": "'Ahimelech prayed to the LORD for him. He gave him bread. He gave him Goliath's sword.' Every word was true, and every word was aimed to kill."
    },
    "11": {
      "L": "Then the king sent to summon Ahimelech the priest, the son of Ahitub, and all his father's house, the priests who were at Nob; and all of them came to the king.",
      "M": "The king sent for Ahimelech the priest, Ahitub's son, along with all his father's household—all the priests at Nob. They all came to the king.",
      "T": "Saul summoned the entire priestly establishment of Nob: Ahimelech and his whole priestly family. They came, obedient, unsuspecting, into the king's presence."
    },
    "12": {
      "L": "And Saul said, Hear now, son of Ahitub. And he answered, Here I am, my lord.",
      "M": "Saul said, 'Hear me, son of Ahitub.' He replied, 'I am here, my lord.'",
      "T": "Saul addressed him formally: 'Son of Ahitub—listen.' 'I am here, my lord,' Ahimelech replied, still believing himself safe."
    },
    "13": {
      "L": "Saul said to him, Why have you conspired against me, you and the son of Jesse, in that you have given him bread and a sword and have inquired of God for him, so that he has risen against me, to lie in wait, as at this day?",
      "M": "'Why have you conspired against me—you and Jesse's son? You gave him bread and a sword, you inquired of God for him, so that he could rise against me and ambush me, as he is doing now.'",
      "T": "The accusation was a full conspiracy charge: 'You and David are working together against me. You gave him provisions, you gave him a weapon, you prayed the LORD's guidance for him—all so he could rise against me and hunt me down.' None of it was true of Ahimelech, who had known nothing of David's real situation."
    },
    "14": {
      "L": "Then Ahimelech answered the king and said, And who among all your servants is so faithful as David, who is the king's son-in-law and captain over your bodyguard and honored in your house?",
      "M": "Ahimelech replied, 'Who among all your servants is as loyal as David? He is your son-in-law, captain of your bodyguard, and one of the most honored people in your household.'",
      "T": "Ahimelech answered with the steady confidence of a man who had done nothing wrong: 'Who is more faithful to you than David? He is your son-in-law. He commands your personal guard. He is the most honored man in your court.' He still believed David was the loyal servant he appeared to be."
    },
    "15": {
      "L": "Was it today that I began to inquire of God for him? Far be it from me! Let not the king impute anything to his servant or to all the house of my father, for your servant knew nothing of all this, less or more.",
      "M": "'Is this the first time I have inquired of God for him? Of course not! Let the king not charge me or any of my father's house—your servant knew absolutely nothing about any of this, great or small.'",
      "T": "'And is this the first time I have prayed the LORD's guidance for him? I have done it many times before—always at the court's request. Do not lay this guilt on me or on my father's house. I knew nothing of whatever is between you and David. Nothing at all.' He was innocent. It made no difference."
    },
    "16": {
      "L": "And the king said, You shall surely die, Ahimelech, you and all your father's house.",
      "M": "The king said, 'You will certainly die, Ahimelech—you and your entire father's household.'",
      "T": "Saul's verdict was absolute: 'You will die. All of you—you and every member of your father's household.' No trial. No deliberation. The sentence fell on innocent men."
    },
    "17": {
      "L": "And the king said to the runners who stood about him, Turn and kill the priests of the LORD, because their hand also is with David, and because they knew when he fled and did not reveal it to me. But the servants of the king would not put out their hand to strike the priests of the LORD.",
      "M": "The king ordered his guards who stood beside him, 'Turn and kill the priests of the LORD—they are in league with David; they knew he fled and didn't tell me.' But the king's servants refused to lift their hand against the priests of the LORD.",
      "T": "Saul turned to his guards: 'Kill the priests—every one of them. They knew David was a fugitive and they said nothing to me.' But the guards would not do it. Whatever they thought of Saul, they would not strike down the LORD's anointed servants. Some line of sacred restraint held them."
    },
    "18": {
      "L": "Then the king said to Doeg, You turn and strike the priests. And Doeg the Edomite turned and he himself struck the priests, and he killed on that day eighty-five men who wore the linen ephod.",
      "M": "The king said to Doeg, 'You—turn and strike the priests.' Doeg the Edomite turned and attacked the priests himself, killing eighty-five men who wore the linen ephod that day.",
      "T": "Saul turned to the one man who would do it. 'Doeg—you do it.' The Edomite who had no covenantal qualms about striking the LORD's servants stepped forward and killed eighty-five priests—every man who wore the linen ephod, the sign of priestly service. Eighty-five."
    },
    "19": {
      "L": "And Nob, the city of the priests, he put to the sword: both man and woman, child and infant, ox, donkey and sheep—with the edge of the sword.",
      "M": "And Nob, the city of priests, he put to the sword: men, women, children, infants, oxen, donkeys, and sheep—all with the sword.",
      "T": "And then Doeg went to the city itself—Nob, the priestly city—and destroyed it entirely. Men, women, children, nursing infants. Livestock. Everything that breathed. What Saul had been commanded to do to Amalek and failed, he now did to the LORD's own priestly city. The narrator records the atrocity without a single word of editorial comment. The list of victims is the commentary."
    },
    "20": {
      "L": "But one of the sons of Ahimelech the son of Ahitub, named Abiathar, escaped and fled after David.",
      "M": "But one son of Ahimelech son of Ahitub escaped—Abiathar—and fled to David.",
      "T": "One man escaped. Abiathar, a son of Ahimelech—the last survivor of the priestly line of Nob—fled and found his way to David."
    },
    "21": {
      "L": "And Abiathar told David that Saul had killed the priests of the LORD.",
      "M": "Abiathar told David that Saul had killed the priests of the LORD.",
      "T": "He brought David the news: Saul had killed the LORD's priests. All of them."
    },
    "22": {
      "L": "And David said to Abiathar, I knew on that day, when Doeg the Edomite was there, that he would surely tell Saul. I have brought about the death of all the persons of your father's house.",
      "M": "David said to Abiathar, 'I knew that day, when Doeg the Edomite was there, that he would certainly report it to Saul. I am responsible for the death of every person in your father's house.'",
      "T": "David did not deflect the guilt. 'I knew it,' he said. 'The moment I saw Doeg there at Nob, I knew he would go to Saul. I said nothing. I left. And because of that, your father's whole house is dead. That is on me.' It was not the whole truth—Saul made the choice, Doeg swung the sword—but David bore the weight of the chain of events he had set in motion."
    },
    "23": {
      "L": "Remain with me; do not be afraid, for he who seeks my life seeks your life; for you are safe with me.",
      "M": "'Stay with me—don't be afraid. The one who wants my life wants yours too. You are under my protection.'",
      "T": "'Stay with me. Don't be afraid. We share the same enemy now—he wants both of us dead. You will be safe with me.' David took Abiathar in. And Abiathar brought the ephod with him—the instrument of divine inquiry that would serve David in all that followed."
    }
  },
  "23": {
    "1": {
      "L": "Then they told David, Behold, the Philistines are fighting against Keilah and are robbing the threshing floors.",
      "M": "David was told, 'The Philistines are attacking Keilah and raiding the threshing floors.'",
      "T": "News reached David in the wilderness: the Philistines were hitting Keilah during the harvest—pillaging the threshing floors at the season when the grain was most exposed. A border town was being plundered."
    },
    "2": {
      "L": "Therefore David inquired of the LORD, saying, Shall I go and attack these Philistines? And the LORD said to David, Go and attack the Philistines and save Keilah.",
      "M": "David inquired of the LORD: 'Should I go and attack these Philistines?' The LORD replied, 'Go, attack the Philistines, and save Keilah.'",
      "T": "David did not move without asking. He brought the question to the LORD through the ephod: 'Do I go fight the Philistines?' The LORD answered directly: 'Go. Rescue Keilah.'"
    },
    "3": {
      "L": "But David's men said to him, Behold, we are afraid here in Judah; how much more then if we go to Keilah against the armies of the Philistines?",
      "M": "But David's men objected: 'We're already afraid here in Judah—how much more if we go to Keilah against the Philistines?'",
      "T": "His men pushed back: 'We're already on the run in Judah—hiding from Saul. And you want us to go fight the Philistines too?' Their fear was understandable. They were four hundred fugitives, not an army."
    },
    "4": {
      "L": "Then David inquired of the LORD again. And the LORD answered him and said, Arise, go down to Keilah, for I will give the Philistines into your hand.",
      "M": "David inquired of the LORD again. The LORD replied, 'Go down to Keilah—I will give the Philistines into your hand.'",
      "T": "David went back to the LORD a second time. The answer was the same, and now it came with a promise: 'Arise, go down—I will hand the Philistines over to you.' That was enough."
    },
    "5": {
      "L": "And David and his men went to Keilah and fought with the Philistines and drove away their livestock and struck them with a great blow. So David saved the inhabitants of Keilah.",
      "M": "David and his men went to Keilah, fought the Philistines, drove off their livestock, and struck them hard. David rescued the people of Keilah.",
      "T": "David led his men to Keilah. They attacked the Philistines, captured their livestock—the spoils that would feed his men—and inflicted a decisive defeat. The people of Keilah were rescued. A fugitive king had done what the legitimate one would not."
    },
    "6": {
      "L": "When Abiathar the son of Ahimelech had fled to David at Keilah, he came down with an ephod in his hand.",
      "M": "When Abiathar son of Ahimelech fled to David at Keilah, he brought the ephod with him.",
      "T": "A note from the narrator: when Abiathar escaped to David, he had brought the priestly ephod—the instrument of divine inquiry. That is how David could consult the LORD at Keilah. The surviving priest gave the outlaw king access to God's direct word."
    },
    "7": {
      "L": "Now it was told Saul that David had come to Keilah. And Saul said, God has given him into my hand, for he has shut himself in by entering a town that has gates and bars.",
      "M": "Saul was told that David had gone to Keilah. He said, 'God has handed him over to me—he has trapped himself by entering a walled city.'",
      "T": "News reached Saul: David was at Keilah—inside a walled city with gates and bars. Saul interpreted this as divine favor: 'God has given him to me. He has nowhere to run.' It was wishful thinking, and God would prove it wrong."
    },
    "8": {
      "L": "And Saul mustered all the people for war, to go down to Keilah and besiege David and his men.",
      "M": "Saul mobilized all his forces to march on Keilah and besiege David and his men.",
      "T": "Saul mobilized his entire army to march on Keilah and trap David inside."
    },
    "9": {
      "L": "When David learned that Saul was plotting evil against him, he said to Abiathar the priest, Bring the ephod here.",
      "M": "When David learned that Saul was scheming to harm him, he told Abiathar the priest, 'Bring the ephod.'",
      "T": "David's intelligence network told him Saul was marching. Before making any move, he called for the ephod. The first thing he did was pray."
    },
    "10": {
      "L": "Then David said, O LORD, the God of Israel, your servant has surely heard that Saul seeks to come to Keilah, to destroy the city on my account.",
      "M": "David prayed, 'O LORD, God of Israel, your servant has heard that Saul intends to come to Keilah and destroy the city because of me.'",
      "T": "He laid the situation before the LORD: 'O LORD, God of Israel—I know Saul is coming here. He will destroy this city because of me. Tell me what is true.'"
    },
    "11": {
      "L": "Will the men of Keilah surrender me into his hand? Will Saul come down, as your servant has heard? O LORD, the God of Israel, please tell your servant. And the LORD said, He will come down.",
      "M": "'Will the men of Keilah hand me over to him? Will Saul really come, as I have heard? O LORD, God of Israel, tell your servant.' The LORD replied, 'He will come.'",
      "T": "Two questions: 'Will Saul come?' and 'Will Keilah betray me?' He asked them in order. First answer: 'He will come.'"
    },
    "12": {
      "L": "Then David said, Will the men of Keilah surrender me and my men into the hand of Saul? And the LORD said, They will surrender you.",
      "M": "David asked, 'Will the men of Keilah hand me and my men over to Saul?' The LORD said, 'They will hand you over.'",
      "T": "Second answer: 'They will surrender you.' The people David had just rescued would give him to Saul to save themselves. He had not earned their lasting loyalty, only their momentary relief. David heard the LORD's word and acted on it."
    },
    "13": {
      "L": "Then David and his men, who were about six hundred, arose and departed from Keilah, and went wherever they could go. And when Saul was told that David had escaped from Keilah, he abandoned the expedition.",
      "M": "David and his men—now about six hundred—arose and left Keilah, moving from place to place as they could. When Saul heard that David had slipped out of Keilah, he called off the campaign.",
      "T": "David left immediately, taking his six hundred men with him. They dispersed into the wilderness, moving constantly, offering no fixed target. Saul heard the news and called off the siege. There was no point."
    },
    "14": {
      "L": "And David remained in the wilderness in the strongholds and stayed in the hill country of the wilderness of Ziph. And Saul sought him every day, but God did not give him into his hand.",
      "M": "David stayed in the wilderness, in the strongholds of the wilderness of Ziph's hill country. Saul hunted him every day, but God did not give David into his hand.",
      "T": "David lived in the wilderness—the strongholds of the Ziph highlands, moving constantly through the terrain that protected him. Saul kept hunting, day after day. But the LORD kept David out of his reach."
    },
    "15": {
      "L": "David saw that Saul had come out to seek his life. David was in the wilderness of Ziph at Horesh.",
      "M": "David learned that Saul had come out to seek his life, while David was at Horesh in the wilderness of Ziph.",
      "T": "David saw it clearly: Saul had left his capital and taken the field personally to hunt him down. David was at Horesh in the Ziph wilderness, hiding."
    },
    "16": {
      "L": "And Jonathan, Saul's son, arose and went to David at Horesh and strengthened his hand in God.",
      "M": "Jonathan, Saul's son, went to David at Horesh and strengthened his resolve in God.",
      "T": "And then Jonathan came. He went out from Gibeah—his father's court, where he was presumably safe—and found David at Horesh. He came not with a plan, not with an army, but to fortify David's trust in God. That is what the phrase means: he strengthened David's hand in God."
    },
    "17": {
      "L": "And he said to him, Do not fear, for the hand of Saul my father shall not find you. You shall be king over Israel, and I shall be next to you; and Saul my father also knows this.",
      "M": "'Don't be afraid,' he said. 'My father's hand will not reach you. You will be king over Israel, and I will be second to you—my father knows this himself.'",
      "T": "'Don't be afraid,' Jonathan said. 'My father will not get to you. You will be king over Israel, and I will stand at your side as your second. Even my father knows this is true.' Jonathan had relinquished the throne without bitterness—perhaps without any choice—but in that moment, in the wilderness, he sealed it with words of faith."
    },
    "18": {
      "L": "And the two of them made a covenant before the LORD; and David remained at Horesh, and Jonathan went to his house.",
      "M": "The two of them made a covenant before the LORD. David remained at Horesh and Jonathan returned home.",
      "T": "They sealed the covenant again before the LORD. Then Jonathan went back—back to Gibeah, back to his father's house, back to a king who would eventually die in battle. David stayed in the wilderness. This was the last time they would meet."
    },
    "19": {
      "L": "Then the Ziphites went up to Saul at Gibeah, saying, Is not David hiding among us in the strongholds at Horesh, on the hill of Hachilah, which is on the south of Jeshimon?",
      "M": "The Ziphites went up to Saul at Gibeah and said, 'David is hiding among us in the strongholds at Horesh, on the hill of Hachilah south of Jeshimon.'",
      "T": "Almost immediately, the Ziphites went up to Saul at Gibeah. They volunteered the information freely: 'David is hiding in our territory—at Horesh, on Hachilah Hill, south of Jeshimon.' Tribal self-interest, or fear of Saul's wrath if they sheltered the outlaw—either way, they handed David over."
    },
    "20": {
      "L": "Now therefore, O king, come down according to all your heart's desire to come down; and our part shall be to surrender him into the king's hand.",
      "M": "'So come down whenever you like, O king—it's your call. We'll hand him over to you.'",
      "T": "'Come whenever you wish, O king. We will do our part—we will hand him over.' They offered themselves as informants and captors."
    },
    "21": {
      "L": "And Saul said, May you be blessed by the LORD, for you have had compassion on me.",
      "M": "Saul replied, 'May the LORD bless you for having mercy on me.'",
      "T": "Saul blessed them. 'The LORD bless you—you have had compassion on me.' The paranoid king had genuine grief, real anguish. His pain was not manufactured, even if his response to that pain was monstrous."
    },
    "22": {
      "L": "Go and make yet more sure; know and see the place where his foot is, and who has seen him there, for it is told me that he deals very cunningly.",
      "M": "'Go and double-check. Find out exactly where he is and who has seen him there—I'm told he is very cunning.'",
      "T": "'Go back and confirm everything. Find the exact spot, the exact witnesses. I am told he is exceptionally clever.' Saul did not want to move until he had David pinned."
    },
    "23": {
      "L": "See therefore, and take note of all the lurking places where he hides himself, and come back to me with certainty; and I will go with you. And if he is in the land, I will search him out among all the thousands of Judah.",
      "M": "'Find out all his hiding places and come back to me with solid information. Then I will go with you. And if he is anywhere in the land, I will find him—even if I have to search through every clan in Judah.'",
      "T": "'Map his hiding places. Come back with solid intelligence. Then I will come myself. If David is anywhere in the land, I will find him, even if I have to go through every household in Judah.' Saul was utterly committed to the hunt."
    },
    "24": {
      "L": "And they arose and went to Ziph ahead of Saul. But David and his men were in the wilderness of Maon, in the Arabah on the south of Jeshimon.",
      "M": "They went ahead of Saul to Ziph. But David and his men were in the wilderness of Maon, in the Arabah south of Jeshimon.",
      "T": "The Ziphites went back ahead of Saul to prepare. But David had already moved: he and his men were in the wilderness of Maon, in the arid lowlands south of Jeshimon. The hunter and the hunted were closing in on each other."
    },
    "25": {
      "L": "And Saul and his men went to seek him. When David was told, he went down to the rock and stayed in the wilderness of Maon; and when Saul heard, he pursued after David in the wilderness of Maon.",
      "M": "Saul and his men set out to find David. When David was informed, he went down to the cliff and stayed in the wilderness of Maon. Hearing this, Saul pursued him into that wilderness.",
      "T": "Saul marched out with his men. David got word and moved deeper into Maon—hiding near a rock formation. Saul tracked him there and came in pursuit."
    },
    "26": {
      "L": "Saul went on one side of the mountain, and David and his men on the other side of the mountain; and David made haste to get away from Saul, for Saul and his men were closing in on David and his men to capture them.",
      "M": "Saul was going along one side of the mountain while David and his men were on the other side, with David hurrying to escape. Saul and his men were closing the circle around David to capture him.",
      "T": "Saul moved along one face of the hill; David and his men scrambled along the other. The gap was closing. Saul's force was folding around David like a trap—seconds, perhaps, from sealing it."
    },
    "27": {
      "L": "But a messenger came to Saul, saying, Hurry and come, for the Philistines have made a raid against the land.",
      "M": "But a messenger arrived with urgent news for Saul: 'Come quickly—the Philistines have raided the land.'",
      "T": "Then a messenger broke through with news: 'Urgent—the Philistines are raiding. Come now.' Saul had to abandon the chase. In the last moment before the trap closed, David's enemies had saved him."
    },
    "28": {
      "L": "So Saul turned back from pursuing David and went against the Philistines. Therefore that place was called the Rock of Escape.",
      "M": "Saul broke off pursuit of David and went to face the Philistines. That is why the place was called the Rock of Escape.",
      "T": "Saul wheeled away from the hunt and marched to meet the Philistines. The place where David almost died was named Sela-hammahlekoth—the Rock of Escape, or the Rock of Divisions. It was a name the people remembered."
    },
    "29": {
      "L": "And David went up from there and stayed in the strongholds of En-gedi.",
      "M": "David went up from there and settled in the strongholds of En-gedi.",
      "T": "David moved again—this time to the caves above En-gedi, on the western shore of the Dead Sea. Dramatic terrain, isolated, defensible. He would be safe there—for a while."
    }
  },
  "24": {
    "1": {
      "L": "And it came to pass when Saul had returned from following the Philistines, that they told him, saying, Behold, David is in the wilderness of En-gedi.",
      "M": "When Saul returned from pursuing the Philistines, he was told, 'David is in the wilderness of En-gedi.'",
      "T": "The moment Saul dealt with the Philistines, the hunt resumed. The report came in: David was at En-gedi. Saul did not rest."
    },
    "2": {
      "L": "Then Saul took three thousand chosen men from all Israel and went to seek David and his men in front of the Rocks of the Wild Goats.",
      "M": "Saul took three thousand of Israel's best troops and went to find David and his men near the Rocks of the Wild Goats.",
      "T": "Saul mobilized three thousand picked fighters—Israel's best—and led them to the limestone crags above En-gedi, where ibex pick their way through the cliffs. It was no small operation."
    },
    "3": {
      "L": "He came to the sheepfolds by the way, where there was a cave, and Saul went in to cover his feet; and David and his men were sitting in the back parts of the cave.",
      "M": "He came to the sheepfolds along the road where a cave was, and Saul went in to relieve himself. David and his men were sitting in the innermost recesses of the cave.",
      "T": "Along the way, Saul stopped at a sheepfold. There was a cave there, and Saul went in alone to relieve himself—unguarded for a moment, unaware. David and his entire company were in the depths of that very cave, hidden in the darkness."
    },
    "4": {
      "L": "And the men of David said to him, Behold the day of which the LORD said to you, I will give your enemy into your hand, and you shall do to him as shall seem good in your eyes. Then David arose and cut off the skirt of Saul's robe secretly.",
      "M": "David's men whispered to him, 'This is the day the LORD promised—he has given your enemy into your hand. Do whatever seems right to you.' David arose and quietly cut off the corner of Saul's robe.",
      "T": "David's men seized the moment in a whisper: 'This is the day. The LORD said he would give your enemy into your hand—and here he is, alone, in your cave.' David stood up. But he did not draw his sword. He moved through the darkness and cut off a corner of Saul's robe—silent, unseen. Then he went back to his men."
    },
    "5": {
      "L": "And it came to pass afterward that David's heart smote him, because he had cut off the skirt of Saul's robe.",
      "M": "Afterward, David's heart struck him because he had cut off the corner of Saul's robe.",
      "T": "And then David's conscience hit him. Even cutting the robe felt like a violation. Saul was the LORD's anointed—to handle his garment without his knowledge was too close to desecrating that sacred office. David felt it as guilt."
    },
    "6": {
      "L": "And he said to his men, The LORD forbid that I should do this thing to my lord, the LORD's anointed, to put out my hand against him, seeing he is the LORD's anointed.",
      "M": "He said to his men, 'The LORD forbid that I should do such a thing to my lord—the LORD's anointed—or put out my hand against him, since he is the LORD's anointed.'",
      "T": "He turned to his men: 'The LORD forbid that I should lay hands on my lord. He is the LORD's anointed. Whatever he has become, whatever he has done to me—that office is sacred. I will not be the one to strike the man the LORD anointed as king.' This was not cowardice. It was theology."
    },
    "7": {
      "L": "So David restrained his men with these words and did not permit them to rise against Saul. And Saul arose and went out of the cave and went on his way.",
      "M": "With these words David held his men back and did not let them attack Saul. Saul got up, left the cave, and went on his way.",
      "T": "David's words settled his men. No one moved. Saul finished what he had come in for, stood up, and walked back out into the sunlight—never knowing how close he had come to dying in the dark. David watched him go."
    },
    "8": {
      "L": "Afterward David also arose and went out of the cave and called after Saul, saying, My lord the king. And when Saul looked behind him, David stooped with his face to the earth and bowed down.",
      "M": "Then David got up, went out of the cave, and called after Saul: 'My lord the king!' Saul looked back, and David bowed to the ground with his face down.",
      "T": "Then David stepped out into the light behind Saul. He called out: 'My lord the king!' Saul turned—and David prostrated himself face to the ground. The gesture was clear: he was presenting himself, unarmed, in submission. He was taking a calculated risk."
    },
    "9": {
      "L": "And David said to Saul, Why do you listen to the words of men who say, Behold, David seeks your harm?",
      "M": "David said to Saul, 'Why do you give ear to people who say, \"David intends to harm you\"?'",
      "T": "From the ground, David made his case: 'Why do you listen to the people who whisper that I mean you harm? Look at this moment. Look at the evidence.'"
    },
    "10": {
      "L": "Behold, this day your eyes have seen how the LORD gave you today into my hand in the cave; and some said to kill you, but my eye spared you; and I said, I will not put out my hand against my lord, for he is the LORD's anointed.",
      "M": "'This very day you have seen with your own eyes that the LORD delivered you into my hands in the cave. Some urged me to kill you, but I spared you. I said, \"I will not raise my hand against my lord—he is the LORD's anointed.\"'",
      "T": "'Today the LORD gave you to me. In that cave, alone, at my mercy—you were in my hand. My men told me to kill you. I refused. I said: he is the LORD's anointed, I will not touch him. You can verify this. Your own eyes saw that I came out behind you rather than against you.'"
    },
    "11": {
      "L": "Moreover, my father, see, yea, see the skirt of your robe in my hand; for in that I cut off the skirt of your robe and did not kill you, know and see that there is no evil or rebellion in my hand, and I have not sinned against you, though you hunt my life to take it.",
      "M": "'Look, my father—here is the corner of your robe in my hand. I cut it off but I did not kill you. See and understand: there is no evil or treachery in me. I have not wronged you, even though you are hunting me down to take my life.'",
      "T": "'Look, father.' He held up the corner of the robe—evidence that could not be argued away. 'I was close enough to cut your garment and I did not kill you. That is proof. Whatever anyone has told you, my hands are clean. I have not wronged you. I am not your enemy. And yet you hunt me like this.'"
    },
    "12": {
      "L": "May the LORD judge between me and you, and may the LORD avenge me of you; but my hand shall not be against you.",
      "M": "'May the LORD judge between us—may the LORD avenge me against you—but my hand will never touch you.'",
      "T": "'I am not going to settle this myself. I place it before the LORD—let him judge between us; let him vindicate me if I am right. But I will not raise my hand against you. That is my commitment.'"
    },
    "13": {
      "L": "As the proverb of the ancients says, Out of the wicked comes wickedness; but my hand shall not be against you.",
      "M": "'As the old proverb says: \"Out of the wicked comes wickedness.\" But my hand shall not be against you.'",
      "T": "'There is an old proverb: wickedness comes from the wicked. I invoke it as my argument. If I were wicked, I would have acted wickedly in that cave. I did not. My hand will not be against you—because I am not wicked toward you, whatever you believe.'"
    },
    "14": {
      "L": "After whom has the king of Israel come out? After whom do you pursue? After a dead dog! After a single flea!",
      "M": "'After whom has the king of Israel come out? Who are you chasing? A dead dog! A single flea!'",
      "T": "'Think about what you are doing. The king of Israel—the commander of a three-thousand-man force—is hunting a single fugitive. A dead dog. One flea. That is how small and contemptible you treat me. Is this worth your time? Your dignity? Your kingdom?' The self-abasement was rhetorical: David was forcing Saul to hear the absurdity of the situation."
    },
    "15": {
      "L": "May the LORD therefore be judge and decide between me and you; and may he see and plead my cause and deliver me from your hand.",
      "M": "'May the LORD be judge and decide between me and you. May he see my case, plead for me, and deliver me from your power.'",
      "T": "'The LORD is my judge. He sees this. He will decide between us, defend my cause, and deliver me from your hand.' David closed his case. He had said everything. Now it was Saul's turn."
    },
    "16": {
      "L": "And it came to pass when David had finished speaking these words to Saul, Saul said, Is this your voice, my son David? And Saul lifted up his voice and wept.",
      "M": "When David finished speaking, Saul said, 'Is that your voice, my son David?' And Saul wept aloud.",
      "T": "When David had finished, Saul spoke—and his voice was shaken: 'Is that you, David? My son?' And Saul broke down and wept. Whatever else Saul was, in that moment his love for David was real."
    },
    "17": {
      "L": "He said to David, You are more righteous than I; for you have done good to me, whereas I have done evil to you.",
      "M": "He said, 'You are more righteous than I am—you have done good to me, but I have done evil to you.'",
      "T": "'You are the better man,' Saul said. 'You have treated me rightly. I have treated you wrongly.' He knew it. He had always known it."
    },
    "18": {
      "L": "And you have declared this day how you have dealt well with me, in that the LORD delivered me into your hand and you did not kill me.",
      "M": "'You have shown today what kind of man you are—when the LORD handed me to you, you let me go.'",
      "T": "'You proved yourself today. The LORD gave me to you—completely—and you spared me. You have demonstrated exactly the kind of man you are.' Saul's acknowledgment was total. And it changed nothing."
    },
    "19": {
      "L": "For if a man finds his enemy, will he send him away on a good road? So may the LORD reward you with good for what you have done to me this day.",
      "M": "'If a man finds his enemy, does he let him go safely on his way? May the LORD repay you with good for what you have done to me today.'",
      "T": "'No man who finds his enemy lets him walk away unharmed. You did. May the LORD repay you for this in kind—good for good.' He was acknowledging a debt he could not repay and a virtue he could not match."
    },
    "20": {
      "L": "And now, behold, I know well that you shall surely be king, and that the kingdom of Israel shall be established in your hand.",
      "M": "'Now I know clearly that you will certainly be king, and that the kingdom of Israel will be secured in your hands.'",
      "T": "'And I know it. I have always known it. You will be king. The kingdom will be established in your hand.' Saul confessed what he had spent years trying to prevent."
    },
    "21": {
      "L": "Swear now to me by the LORD that you will not cut off my offspring after me, and that you will not destroy my name from my father's house.",
      "M": "'Swear to me by the LORD that you will not wipe out my family line after me, and that you will not blot out my name from my father's house.'",
      "T": "'I ask one thing. Swear to me by the LORD: when you are king, do not destroy my descendants. Do not erase my name from my father's house.' It was what every ancient Near Eastern dynastic successor did—eliminate the rival line. Saul was begging David not to be that kind of king."
    },
    "22": {
      "L": "And David swore to Saul. Then Saul went to his house, and David and his men went up to the stronghold.",
      "M": "David swore this to Saul. Then Saul went home, and David and his men returned to the stronghold.",
      "T": "David swore the oath. It was an oath he would keep—years later, when he brought Mephibosheth, Jonathan's surviving son, to his own table. Saul went home. David and his men climbed back to the stronghold. The moment of reconciliation was over. Nothing structural had changed."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '1samuel', existing)
    print('1 Samuel 19–24 written.')

if __name__ == '__main__':
    main()
