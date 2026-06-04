"""
MKT Job chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-4-6.py

Context: Chapters 4–5 = Eliphaz's first speech (cycles begin); chapter 6 = Job's reply.
Job is Hebrew wisdom poetry — parallelism is load-bearing; T tier preserves/enhances it.

Translation decisions:
- H7706 (שַׁדַּי / Shaddai): "the Almighty" in L/M; "Shaddai" or "the Almighty" in T — the divine
  epithet El Shaddai is distinctive in Job and should not be flattened to generic "God"
- H433 (אֱלוֹהַּ / Eloah): "God" — the poetic singular used throughout Job; distinct from H430 (Elohim)
- H7307 (רוּחַ / ruach): context-driven — "a spirit" (4:15, apparitional vision), "spirit" (6:4,
  inner life of Job). Never capitalized in these chapters; no divine Spirit reference here.
- H2617 (חֶסֶד / hesed): 6:14 is contested. Hebrew syntax: "To the despairing, hesed from his
  friend — and he forsakes the fear of the Almighty." Subject of "forsakes" is ambiguous:
  the one who withholds hesed (most natural reading), not the despairing person. Rendered:
  withholding steadfast love from a desperate friend = forsaking the fear of the Almighty.
- H5315 (נֶפֶשׁ / nephesh): "appetite" in 6:7 (context: refusing food/taste), "life" in 6:11
  (embodied self, not immaterial soul)
- H6918 (קָדוֹשׁ / qadosh): "the Holy One" in 6:10 — capitalized as divine title, consistent
  with usage elsewhere
- H3374 (יִרְאָה / yirah): "fear" throughout = reverential awe / covenantal orientation,
  not mere fright
- Poetic structure: T tier uses line breaks (\\n) for formal parallelism in 4:3-4, 4:8-11,
  4:17-19, 5:6-7, 5:17-18, 6:2-4, 6:14-21, 6:25-26 and elsewhere where the poetry is dense
- H1285 (בְּרִית / berit): "covenant" in 5:23 — formal pact/league reading maintained
- Aspect notes: Job's verbs in ch.6 use the perfect heavily = completed, established states of
  suffering, not ongoing; Eliphaz in 4–5 mixes perfect (testimony) and imperfect (promise)
- OT echo: 5:13 quoted verbatim in 1 Cor 3:19; T tier notes the force of this
- Textual note: 5:5 is notoriously difficult (hapax lexemes for thorns/snare); translation
  follows ESV/NASB majority reading
- 6:14 alternative reading (KJV/NKJV): "pity should be shown to a friend even if he forsakes
  the fear of the Almighty" — rejected here as the less natural Hebrew syntax
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


JOB = {
  "4": {
    "1": {
      "L": "Then answered Eliphaz the Temanite, and said,",
      "M": "Then Eliphaz the Temanite replied:",
      "T": "Eliphaz the Temanite spoke:"
    },
    "2": {
      "L": "If one ventures a word with you, will you be impatient? Yet who can withhold himself from speaking?",
      "M": "If someone ventures a word with you, will it trouble you? Yet who can hold back from speaking?",
      "T": "Dare I speak, knowing it may sting?\nYet who can keep silent when words press to be said?"
    },
    "3": {
      "L": "Behold, you have instructed many, and the weak hands you have strengthened.",
      "M": "Look — you have instructed many people, and you have strengthened weak hands.",
      "T": "How many others you have taught.\nHow many faint hands you have steadied."
    },
    "4": {
      "L": "The stumbling one your words have upheld, and the faltering knees you have made firm.",
      "M": "Your words have upheld the one who was stumbling, and you have steadied feeble knees.",
      "T": "The man about to fall — your words held him up.\nThe trembling knees — you made them firm."
    },
    "5": {
      "L": "But now it comes upon you, and you are impatient; it touches you, and you are dismayed.",
      "M": "But now that it has come upon you, you are impatient; it has touched you, and you are terrified.",
      "T": "But now the trouble has come upon you, and your courage fails.\nIt has reached you — and you fall apart."
    },
    "6": {
      "L": "Is not your fear your confidence, and the integrity of your ways your hope?",
      "M": "Is not your reverence for God your confidence, and the integrity of your ways your hope?",
      "T": "You built your life on fearing God — does that not give you ground to stand on?\nIs not the integrity of your ways the very thing you hoped in?"
    },
    "7": {
      "L": "Remember, I pray: who that was innocent has perished? Or where have the upright been cut off?",
      "M": "Think: has any innocent person ever perished? Have the upright ever been destroyed?",
      "T": "Call to mind one truly innocent man who perished.\nFind me one upright life that was simply cut down."
    },
    "8": {
      "L": "As I have seen, those who plow iniquity and those who sow wickedness reap it.",
      "M": "As I have observed, those who plow trouble and sow wickedness reap the same.",
      "T": "What I have always seen holds:\nthe ones who farm trouble harvest it;\nthose who seed wickedness reap a full crop of it."
    },
    "9": {
      "L": "By the breath of God they perish, and by the blast of his nostrils they are consumed.",
      "M": "By the breath of God they perish, and by the blast of his nostrils they are consumed.",
      "T": "A single breath from God undoes them.\nOne flare of his nostrils, and they are gone."
    },
    "10": {
      "L": "The roar of the lion, the voice of the fierce lion — the teeth of the young lions are broken.",
      "M": "The roar of the lion, the voice of the fierce lion — the teeth of the young lions are shattered.",
      "T": "The mighty lion still roars;\nthe fierce lion still lifts its voice —\nbut even the cubs' teeth are already broken."
    },
    "11": {
      "L": "The strong lion perishes for lack of prey, and the whelps of the lioness are scattered abroad.",
      "M": "The mature lion perishes for lack of prey, and the cubs of the lioness scatter.",
      "T": "Even the mightiest predator starves when prey runs out.\nIts cubs scatter, left to fend for themselves."
    },
    "12": {
      "L": "Now a word was secretly brought to me, and my ear received a whisper of it.",
      "M": "A word came to me in secret, and my ear caught a faint whisper of it.",
      "T": "A word came to me by stealth.\nMy ear barely caught the whisper."
    },
    "13": {
      "L": "In thoughts from visions of the night, when deep sleep falls on men,",
      "M": "In disturbing thoughts from visions of the night, when deep sleep descends on people,",
      "T": "It came in the fragmented imagery of a night vision,\nas deep sleep was settling over everyone —"
    },
    "14": {
      "L": "fear came upon me and trembling, which made all my bones shake.",
      "M": "fear came over me and trembling, making all my bones shake.",
      "T": "— fear seized me, and trembling;\nevery bone in my body shook."
    },
    "15": {
      "L": "A spirit passed before my face; the hair of my flesh stood on end.",
      "M": "A spirit passed before my face; the hair on my body bristled.",
      "T": "Something passed before my face — a spirit —\nand the hair on my skin stood up."
    },
    "16": {
      "L": "It stood still, but I could not discern its form. A shape was before my eyes; silence, then I heard a voice:",
      "M": "It stopped still, but I could not make out its form. A shape was before my eyes; silence — and then a voice:",
      "T": "It stopped.\nI could not make it out. Something was there before my eyes.\nThen: silence.\nThen a voice:"
    },
    "17": {
      "L": "'Can a mortal man be more righteous than God? Can a man be purer than his Maker?'",
      "M": "'Can a mortal be more righteous than God? Can a person be purer than their Maker?'",
      "T": "'Can any mortal stand in the right before God?\nCan the creature claim purity the Creator does not grant?'"
    },
    "18": {
      "L": "'Behold, in his servants he places no trust, and his angels he charges with folly.'",
      "M": "'God places no trust even in his servants; he charges his very angels with error.'",
      "T": "'Even his own heavenly servants he cannot fully trust;\neven among his angels he finds fault.'"
    },
    "19": {
      "L": "'How much more those who dwell in clay houses, whose foundation is in the dust, who are crushed before the moth!'",
      "M": "'How much more those who live in houses of clay, whose foundation is the dust, who are crushed more easily than a moth!'",
      "T": "'And if the angels fail the test —\nwhat of those who live in clay houses,\nwhose foundation is dust,\nwho can be crushed like a moth?'"
    },
    "20": {
      "L": "'From morning to evening they are shattered; without regard, they perish forever.'",
      "M": "'Between morning and evening they are destroyed; without anyone noticing, they vanish forever.'",
      "T": "'In less than a day they can be shattered —\nand no one marks their passing;\nthey are simply gone.'"
    },
    "21": {
      "L": "'Is not their tent cord plucked from within them? They die — and without wisdom.'",
      "M": "'Is not their tent stake pulled up from within them? They die, and that without gaining wisdom.'",
      "T": "'Their tent stake is yanked out before they are ready.\nThey die having learned nothing.'"
    }
  },
  "5": {
    "1": {
      "L": "Call now; is there one who will answer you? And to which of the holy ones will you turn?",
      "M": "Call out now — is there anyone who will answer you? To which of the holy ones will you appeal?",
      "T": "Go ahead, call out — who do you think will answer?\nWhich of the holy ones will take up your cause?"
    },
    "2": {
      "L": "For vexation kills the foolish man, and envy slays the simple.",
      "M": "Vexation kills the foolish, and jealousy destroys the naive.",
      "T": "Anger destroys the fool;\nresentment kills the gullible."
    },
    "3": {
      "L": "I have seen the foolish taking root, and suddenly I cursed his dwelling.",
      "M": "I have seen the fool put down roots, only to see his household suddenly cursed.",
      "T": "I have watched the fool seem well-settled —\nthen without warning, his household came to ruin."
    },
    "4": {
      "L": "His children are far from safety; they are crushed in the gate, and there is none to deliver.",
      "M": "His children are kept from safety; they are crushed at the city gate, with no one to rescue them.",
      "T": "His children find no refuge;\nthey are ground down at the gates of justice\nwith no one to help them."
    },
    "5": {
      "L": "The hungry devour his harvest, taking it from among the thorns, and the snare swallows his wealth.",
      "M": "The hungry eat up his harvest, snatching it from among the thorns; they swallow up everything he owned.",
      "T": "Famine cleans out the fool's harvest;\nstrangers grab his crops out of the briars;\nthe thirsty swallow up everything he saved."
    },
    "6": {
      "L": "For affliction does not come forth from the dust, nor does trouble spring from the ground,",
      "M": "Affliction does not rise from the dust, nor does trouble spring from the ground —",
      "T": "Trouble does not grow wild in the dirt;\nsuffering does not sprout from bare soil —"
    },
    "7": {
      "L": "but man is born to trouble as the sparks fly upward.",
      "M": "but people are born to trouble as naturally as sparks fly upward.",
      "T": "— no, it is simply what it is to be human:\nwe are born into trouble\nthe way sparks rise, inevitably, toward the sky."
    },
    "8": {
      "L": "But I would seek God, and to God would I commit my cause,",
      "M": "As for me, I would seek God, and to God I would commit my cause —",
      "T": "But if I were in your place, I would take my complaint straight to God.\nI would lay the whole matter before him —"
    },
    "9": {
      "L": "who does great things and unsearchable, marvellous things without number:",
      "M": "who does great and unsearchable things, marvellous things beyond counting —",
      "T": "the God who does things great and beyond searching out,\nwonders too numerous to count —"
    },
    "10": {
      "L": "who gives rain upon the earth and sends waters upon the fields;",
      "M": "who sends rain upon the earth and water upon the open fields;",
      "T": "who waters the earth\nand floods the open fields with rain;"
    },
    "11": {
      "L": "who sets on high those that be low, that those who mourn may be exalted to safety;",
      "M": "who lifts up the lowly on high, and raises those in mourning to safety;",
      "T": "who exalts the humiliated\nand gives the grieving a place of security;"
    },
    "12": {
      "L": "who frustrates the devices of the crafty, so that their hands cannot succeed;",
      "M": "who thwarts the schemes of the cunning, so that their hands achieve nothing of what they plan;",
      "T": "who catches the schemers in their own cunning\nso that nothing they plot comes to anything;"
    },
    "13": {
      "L": "he catches the wise in their own craftiness, and the counsel of the wily is carried headlong.",
      "M": "he traps the wise in their own shrewdness, and the schemes of the crafty are swept away.",
      "T": "the clever walk into traps of their own making —\nthis is the very word Paul will quote:\nGod catches the wise in their craftiness."
    },
    "14": {
      "L": "They meet with darkness in the daytime and grope at noon as in the night.",
      "M": "They encounter darkness in broad daylight and grope at midday as though it were night.",
      "T": "The powerful stumble in broad daylight\nand feel their way at noon as if it were midnight."
    },
    "15": {
      "L": "But he saves the needy from the sword of their mouth and from the hand of the mighty.",
      "M": "But he saves the poor from the cutting words of their enemies and from the grip of the powerful.",
      "T": "Yet God rescues the helpless —\nrescues them from the cutting words of the powerful\nand from the grip of the strong."
    },
    "16": {
      "L": "So the poor have hope, and injustice shuts her mouth.",
      "M": "So the poor find hope, and injustice is silenced.",
      "T": "So the destitute are given a future,\nand wickedness is left with nothing to say."
    },
    "17": {
      "L": "Behold, happy is the man whom God corrects; therefore do not despise the discipline of the Almighty.",
      "M": "See, blessed is the person whom God reproves; do not despise the discipline of the Almighty.",
      "T": "Here is a truth worth holding:\nthe one God rebukes is the one God has not abandoned.\nDo not pull away from the Almighty's correction —"
    },
    "18": {
      "L": "For he wounds, but he also binds up; he strikes, but his hands heal.",
      "M": "For he wounds and then bandages; he strikes down and his own hands heal.",
      "T": "— for he is both the one who wounds and the one who binds the wound;\nthe one who strikes and the one whose hands restore."
    },
    "19": {
      "L": "In six troubles he will deliver you, and in seven no evil shall touch you.",
      "M": "From six troubles he will deliver you; in seven, no evil will reach you.",
      "T": "Six times — seven times — he will pull you through.\nNo evil will be able to reach you."
    },
    "20": {
      "L": "In famine he will redeem you from death, and in war from the power of the sword.",
      "M": "In famine he will redeem you from death, and in war from the lethal edge of the sword.",
      "T": "When famine comes, he will buy you back from death.\nWhen battle comes, he will save you from the sword."
    },
    "21": {
      "L": "You will be hidden from the scourge of the tongue, and you will not fear when destruction comes.",
      "M": "You will be sheltered from the lash of the tongue, and will not dread when disaster comes.",
      "T": "The vicious words of enemies will not find you;\nwhen ruin comes sweeping through, it will pass you by."
    },
    "22": {
      "L": "At destruction and famine you shall laugh, and you shall not fear the wild beasts of the earth.",
      "M": "You will laugh at destruction and famine, and will not dread the wild animals of the land.",
      "T": "You will laugh at catastrophe and drought;\nthe wild creatures of the earth will hold no terror for you."
    },
    "23": {
      "L": "For you shall be in covenant with the stones of the field, and the beasts of the field shall be at peace with you.",
      "M": "You will have a pact with the stones of the field, and the wild animals will be at peace with you.",
      "T": "The very stones of the field will do you no harm,\nand the creatures of the wild will lie down peacefully in your presence."
    },
    "24": {
      "L": "You shall know that your tent is at peace, and you shall visit your fold and lack nothing.",
      "M": "You will know that your home is secure, and when you check your flocks, nothing will be missing.",
      "T": "Your home will be a place of shalom.\nWhen you walk your pastures, everything will be in order."
    },
    "25": {
      "L": "You shall know also that your offspring shall be many, and your descendants as the grass of the earth.",
      "M": "You will know that your children will be numerous, and your descendants like the grass of the earth.",
      "T": "You will watch your children flourish,\nyour descendants spreading like grass across the land."
    },
    "26": {
      "L": "You shall come to your grave in full vigor, as a shock of grain comes up in its season.",
      "M": "You will come to your grave in ripe old age, like a sheaf of grain harvested in its proper season.",
      "T": "When your time comes, you will go to your grave full and satisfied —\nthe way a sheaf of grain is brought in when it is perfectly ripe."
    },
    "27": {
      "L": "Behold, this we have searched out; it is true. Hear it and know it for yourself.",
      "M": "Look, we have examined this carefully; it is true. Hear it and take it to heart.",
      "T": "We have weighed all of this; it holds.\nListen — and let it sink in."
    }
  },
  "6": {
    "1": {
      "L": "Then Job answered and said:",
      "M": "Then Job replied:",
      "T": "Job answered:"
    },
    "2": {
      "L": "Oh that my vexation were weighed, and all my calamity laid in the balances!",
      "M": "If only my grief could be weighed, and all my calamity placed on the scales!",
      "T": "If only my anguish could be placed on a scale —\nmy grief and my disaster weighed out in full —"
    },
    "3": {
      "L": "For then it would be heavier than the sand of the seas; therefore my words have been reckless.",
      "M": "It would be heavier than the sand of the sea; no wonder my words have been rash.",
      "T": "— it would outweigh the sand of every shore.\nThat is why my words have spilled out so wildly."
    },
    "4": {
      "L": "For the arrows of the Almighty are in me; my spirit drinks their poison; the terrors of God are arrayed against me.",
      "M": "The Almighty's arrows are lodged in me; my spirit is drinking their venom; the terrors of God are lined up against me.",
      "T": "The Almighty's arrows are in me and stuck there;\nmy whole spirit is drinking down their poison.\nGod's terrors are drawn up in battle order against me."
    },
    "5": {
      "L": "Does the wild donkey bray when it has grass, or does the ox low when it has its fodder?",
      "M": "Does a wild donkey bray when it has grass? Does an ox bellow when it has its fodder?",
      "T": "Does a donkey bray in a green field?\nDoes an ox bellow at a full manger?\nI am not complaining without cause."
    },
    "6": {
      "L": "Can tasteless food be eaten without salt, or is there any flavor in the white of an egg?",
      "M": "Can bland food be eaten without salt? Is there any taste in the white of an egg?",
      "T": "Unsalted food is no food at all.\nThe slime of an egg is flavorless.\nThat is what my life has become."
    },
    "7": {
      "L": "My appetite refuses to touch them; they are as sickness to me.",
      "M": "My appetite refuses to touch such things; they are like loathsome food to me.",
      "T": "I cannot bring myself to swallow it.\nEverything my life is now turns my stomach."
    },
    "8": {
      "L": "Oh that I might have my request, and that God would grant my desire:",
      "M": "If only I could have what I ask for, that God would grant my longing —",
      "T": "I have one request, one thing I long for,\nthat God would grant me:"
    },
    "9": {
      "L": "that it would please God to crush me, that he would let loose his hand and cut me off!",
      "M": "that God would be willing to crush me, to let loose his hand and cut me off!",
      "T": "that he would simply crush me.\nLet him unleash his hand\nand make an end of me."
    },
    "10": {
      "L": "This would be my comfort; I would even exult in unsparing pain, for I have not denied the words of the Holy One.",
      "M": "This would be my consolation — to exult even in pain without mercy — because I have not concealed the words of the Holy One.",
      "T": "That would be my one comfort:\nto know I held firm,\nthat I endured even that and did not flinch from what the Holy One said."
    },
    "11": {
      "L": "What is my strength, that I should wait? And what is my end, that I should prolong my life?",
      "M": "What is my strength, that I should hold on? What do I have to look forward to, that I should endure?",
      "T": "What strength is left in me that I should go on waiting?\nWhat future do I have that makes endurance worth it?"
    },
    "12": {
      "L": "Is my strength the strength of stones? Is my flesh of bronze?",
      "M": "Is my strength like the strength of stone? Is my flesh made of bronze?",
      "T": "I am not made of stone.\nMy flesh is not bronze.\nI have limits."
    },
    "13": {
      "L": "Is it not that there is no help in me, and that sound wisdom is driven from me?",
      "M": "Is there no help left in me? Has all sound judgment been driven away?",
      "T": "I have no resources left inside me.\nEvery clear thought has been beaten out."
    },
    "14": {
      "L": "To the despairing, steadfast love from his friend — else he forsakes the fear of the Almighty.",
      "M": "The despairing person deserves steadfast love from a friend; to withhold it is to forsake the fear of the Almighty.",
      "T": "When someone is in despair,\nwhat they need from a friend is faithful, covenant love.\nTo deny that is to deny the fear of God."
    },
    "15": {
      "L": "My brothers have dealt treacherously like a desert stream, like channels of streams that pass away,",
      "M": "My brothers are as treacherous as a seasonal brook, like watercourses that flow away —",
      "T": "My friends have let me down the way a desert wadi fails —\nthose seasonal streambeds that run full and then vanish —"
    },
    "16": {
      "L": "which are black from the ice, in which the snow is hidden;",
      "M": "which run dark with melting ice, swollen where snow lies hidden;",
      "T": "rushing with ice-melt and snowmelt in winter,"
    },
    "17": {
      "L": "when the heat comes, they are gone; when it is hot, they dry up from their place.",
      "M": "but when the heat comes they disappear; when summer arrives, they dry up from their channel.",
      "T": "but when the heat of summer strikes,\nthey dry up and are gone without a trace."
    },
    "18": {
      "L": "The paths of their course wind away; they go up into emptiness and are lost.",
      "M": "The courses they ran turn aside; they rise into wasteland and vanish.",
      "T": "Their channels twist and wind off into nothing;\nthey run up into barren ground and disappear."
    },
    "19": {
      "L": "The caravans of Tema looked; the companies of Sheba waited and hoped.",
      "M": "The caravans of Tema looked for water; the travelers of Sheba hoped for it.",
      "T": "Caravans from Tema scan the horizon for those wadis;\nSheba's travelers fix their hope on them —"
    },
    "20": {
      "L": "They are confounded because they had hoped; they come there and are ashamed.",
      "M": "They are put to shame because they trusted them; they arrive and find themselves disappointed.",
      "T": "— only to arrive at empty, cracked earth,\nhumiliated by their own hope."
    },
    "21": {
      "L": "For now you have become nothing; you see my terror and are afraid.",
      "M": "You have now become just like them — you see my disaster and shrink back in fear.",
      "T": "And so it is with you, my friends.\nYou are those empty wadis.\nYou took one look at my suffering and shrank away."
    },
    "22": {
      "L": "Have I said, 'Give to me,' or, 'Offer a bribe for me from your wealth'?",
      "M": "Have I asked you for a gift? Have I asked you to pay a bribe on my behalf out of your own money?",
      "T": "Did I ask you for money?\nDid I beg you to pull strings for me at your own expense?"
    },
    "23": {
      "L": "Or, 'Deliver me from the hand of the enemy'? Or, 'Redeem me from the hand of the ruthless'?",
      "M": "Or, 'Save me from my enemy's hand,' or, 'Rescue me from the grip of the ruthless'?",
      "T": "Did I ask you to rescue me,\nto use your influence to get me free?\nI asked nothing of you."
    },
    "24": {
      "L": "Teach me, and I will be silent; and make me to understand wherein I have erred.",
      "M": "Teach me, and I will be quiet; show me in what way I have gone wrong.",
      "T": "All I ask is this: teach me.\nExplain where I have gone wrong,\nand I will fall silent."
    },
    "25": {
      "L": "How forceful are upright words! But what does your reproving prove?",
      "M": "How compelling honest words are! But what does your argumentation actually prove?",
      "T": "Honest words have real force — I acknowledge that.\nBut what, exactly, are you proving about me?"
    },
    "26": {
      "L": "Do you think to reprove words, when the speech of a desperate man is but wind?",
      "M": "Do you intend to reprove words, as if the speech of a despairing man were just wind?",
      "T": "You are trying to score debating points\nagainst someone whose words are the cry of despair —\nas if you could correct desperation the way you correct an argument."
    },
    "27": {
      "L": "You would even cast lots over the fatherless and barter over your friend.",
      "M": "You would cast lots over an orphan and sell out your friend.",
      "T": "You are the kind of people who would auction off an orphan\nand trade on the misery of a friend."
    },
    "28": {
      "L": "But now, be pleased to look at me, for I will not lie to your face.",
      "M": "Now then, be willing to look me in the face, for I will not lie to you.",
      "T": "Look at me.\nActually look.\nI will not lie to your face."
    },
    "29": {
      "L": "Return, I pray; let no injustice be done; yea, return again — my righteousness is still intact.",
      "M": "Come back now; let there be no injustice here. Come back again — my integrity is at stake.",
      "T": "Reconsider.\nNo injustice, please — reconsider.\nMy honor is on the line in this."
    },
    "30": {
      "L": "Is there injustice on my tongue? Cannot my palate discern what is wrong?",
      "M": "Is there any wrongdoing on my tongue? Can my own sense of taste not tell what is harmful?",
      "T": "My tongue knows the taste of injustice.\nIt knows the difference.\nThere is none here."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 4–6 written.')

if __name__ == '__main__':
    main()
