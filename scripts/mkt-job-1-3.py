"""
MKT Job chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-1-3.py

Translation decisions:
- H7854 (שָׂטָן): "the Adversary" (L/M) / "the Accuser" (T) — Hebrew uses the definite article
  (ha-satan), making it a legal title meaning challenger/accuser, not yet a proper name.
  "Satan" imports later theological freight; "Adversary" preserves the courtroom/legal register.
- H3068 (יהוה): "LORD" (L/M) / "the LORD" (T) — small-caps convention per guide.
- H430 (אֱלֹהִים): "God" throughout — grammatically plural, contextually singular in Job's prose
  frame; no theological ambiguity requiring special handling in chs 1–3.
- H5315 (נֶפֶשׁ): "life" in 2:4,6 — context is physical survival; rendered as "life" not "soul"
  to avoid Platonic import. Job's embodied self is what Satan wagers.
- H7307 (רוּחַ): "wind" in 1:19 — clearly the wind from the desert (wilderness direction
  specified), not spirit. H7307 is polysemous; context rules here.
- H8535/H8538 (תָּם/תֻּמָּה): "blameless"/"integrity" — preserves the moral completeness
  sense (tam = whole/complete rather than merely morally spotless).
- H2600 (חִנָּם): "for nothing/without cause" — rendered both ways per context; 1:9 stresses
  the Adversary's challenge ("for nothing"), 2:3 stresses God's admission ("without cause").
- H3882 (לִוְיָתָן): "Leviathan" in 3:8 — mythological chaos-dragon; the proper name is kept;
  context: those who curse the day know how to arouse even this primordial creature.
- Chapter 3 is Hebrew poetry (Job's opening lament). T tier uses line breaks to honour
  parallelism. L/M remain prose sentences. Poetry begins at 3:3.
- Aspect: narrative prose in chs 1–2 uses waw-consecutive imperfect (past narrative).
  Job's lament in ch 3 uses jussive/imperfect for wishes ("let... perish," "let... be dark").
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
  "1": {
    "1": {
      "L": "There was a man in the land of Uz whose name was Job, and that man was blameless and upright, and one who feared God and turned away from evil.",
      "M": "There was a man in the land of Uz whose name was Job. This man was blameless and upright, one who feared God and turned away from evil.",
      "T": "In the land of Uz there lived a man named Job — a man without moral blemish, upright in all his ways, who feared God and kept himself far from evil."
    },
    "2": {
      "L": "And there were born to him seven sons and three daughters.",
      "M": "He had seven sons and three daughters.",
      "T": "Seven sons and three daughters had been born to him."
    },
    "3": {
      "L": "His possessions were seven thousand sheep and three thousand camels and five hundred yoke of oxen and five hundred she-donkeys, and a very great household, and that man was the greatest of all the people of the east.",
      "M": "His possessions included seven thousand sheep, three thousand camels, five hundred yoke of oxen, and five hundred female donkeys, together with a very large household of servants. He was the greatest man among all the people of the east.",
      "T": "His wealth was vast: seven thousand sheep, three thousand camels, five hundred yoke of oxen, five hundred she-donkeys, and a large retinue of servants. He was the most prominent man in all the East."
    },
    "4": {
      "L": "And his sons went and made a feast in the house of each one on his day, and they sent and called their three sisters to eat and to drink with them.",
      "M": "His sons would take turns holding feasts in their homes, each on his appointed day, and they would invite their three sisters to eat and drink with them.",
      "T": "Job's sons would rotate hosting feasts — each son on his own birthday — and they always invited their three sisters to celebrate with them."
    },
    "5": {
      "L": "And when the days of feasting had run their course, Job would send and consecrate them, and he would rise early in the morning and offer burnt offerings according to the number of them all. For Job said, 'Perhaps my sons have sinned and cursed God in their hearts.' Thus Job did continually.",
      "M": "When each round of feasting was over, Job would send for his children and consecrate them. He would rise early in the morning and offer a burnt offering for each of them all, for he said, 'Perhaps my sons have sinned and cursed God in their hearts.' This is what Job did regularly.",
      "T": "When the feast days ended, Job would gather his children for a solemn rite — rising at dawn, consecrating each one, and offering a burnt offering for every child. His reasoning: 'Perhaps one of my sons has sinned and silently cursed God in his heart.' This was Job's standing practice."
    },
    "6": {
      "L": "Now there was a day when the sons of God came to present themselves before the LORD, and the Adversary also came among them.",
      "M": "One day the heavenly beings came to present themselves before the LORD, and the Adversary came among them as well.",
      "T": "In the heavenly court, the divine assembly gathered to stand before the LORD. Among them, uninvited, came the Accuser."
    },
    "7": {
      "L": "And the LORD said to the Adversary, 'From where have you come?' The Adversary answered the LORD and said, 'From going to and fro in the earth and from walking up and down in it.'",
      "M": "The LORD said to the Adversary, 'Where have you come from?' The Adversary answered the LORD, 'From roaming through the earth and walking back and forth on it.'",
      "T": "The LORD addressed the Accuser: 'Where have you been?' He replied, 'Patrolling the earth — moving to and fro across it.'"
    },
    "8": {
      "L": "And the LORD said to the Adversary, 'Have you considered my servant Job? There is no one like him on earth — a blameless and upright man who fears God and turns away from evil.'",
      "M": "The LORD said to the Adversary, 'Have you taken notice of my servant Job? There is no one like him on earth — blameless and upright, fearing God and turning from evil.'",
      "T": "The LORD pointed to Job: 'Have you taken stock of my servant Job? He is without equal on earth — a man of complete integrity, upright in his ways, who fears me and refuses evil.'"
    },
    "9": {
      "L": "Then the Adversary answered the LORD and said, 'Does Job fear God for nothing?'",
      "M": "The Adversary answered the LORD, 'Does Job fear God for no reason?'",
      "T": "The Accuser's response was a challenge: 'Does Job serve God for nothing? There must be an angle.'"
    },
    "10": {
      "L": "Have you not made a hedge around him and around his house and around all that he has on every side? You have blessed the work of his hands, and his possessions have increased in the land.",
      "M": "'Have you not put a protective fence around him and his household and all he has on every side? You have blessed the work of his hands, and his wealth has multiplied throughout the land.'",
      "T": "'You have built a wall around him — around his family, his household, everything he owns. You bless whatever he touches, and his wealth keeps growing. Of course he serves you! What has it cost him?'"
    },
    "11": {
      "L": "But put forth your hand now and touch all that he has, and he will curse you to your face.",
      "M": "'But stretch out your hand and strike everything he has — he will surely curse you to your face.'",
      "T": "'Strip it all away — touch what he has — and he will curse you to your face. All that worship will vanish.'"
    },
    "12": {
      "L": "And the LORD said to the Adversary, 'Behold, all that he has is in your hand; only do not stretch out your hand against him.' So the Adversary went out from the presence of the LORD.",
      "M": "The LORD said to the Adversary, 'Very well, everything he has is in your power. Only do not lay a hand on the man himself.' So the Adversary departed from the LORD's presence.",
      "T": "The LORD accepted the challenge: 'Everything he owns is in your hands. Only leave the man himself untouched.' With that, the Accuser left the divine court."
    },
    "13": {
      "L": "Now there was a day when his sons and his daughters were eating and drinking wine in the house of their eldest brother.",
      "M": "One day his sons and daughters were eating and drinking wine at the oldest brother's house.",
      "T": "On a day like any other, Job's children were feasting and drinking at the oldest son's home."
    },
    "14": {
      "L": "And a messenger came to Job and said, 'The oxen were plowing and the donkeys were feeding beside them,'",
      "M": "A messenger came running to Job and said, 'The oxen were plowing and the donkeys were grazing nearby —'",
      "T": "A breathless messenger ran to Job: 'We were out in the fields — oxen plowing, donkeys grazing — when —'"
    },
    "15": {
      "L": "'— and the Sabeans fell upon them and seized them; they have struck down the servants with the edge of the sword, and I alone have escaped to tell you.'",
      "M": "'— the Sabeans raided us. They seized the livestock and cut down the servants with the sword. I alone escaped to tell you!'",
      "T": "'— Sabean raiders swept down. They took everything — oxen, donkeys — and killed every worker with the sword. I am the only one who escaped to bring you the news.'"
    },
    "16": {
      "L": "While he was yet speaking, there came also another and said, 'The fire of God fell from heaven and burned up the sheep and the servants and consumed them, and I alone have escaped to tell you.'",
      "M": "While that man was still speaking, another arrived: 'Fire from God fell from heaven and burned up the sheep and all the servants, consuming them. I alone escaped to tell you!'",
      "T": "The first messenger had not finished speaking when a second arrived, gasping: 'A fire fell from the sky — a divine fire — and incinerated the sheep and every shepherd. I am the only survivor.'"
    },
    "17": {
      "L": "While he was yet speaking, there came also another and said, 'The Chaldeans made out three bands and fell upon the camels and carried them away, and also struck down the servants with the edge of the sword; and I alone have escaped to tell you.'",
      "M": "While that man was still speaking, another arrived: 'Three Chaldean raiding parties swept in, took all the camels, and killed the servants with the sword. I alone escaped to tell you!'",
      "T": "Before the second had finished, a third messenger burst in: 'Three columns of Chaldean raiders overran the camel herds and killed all the handlers. I alone got away to tell you.'"
    },
    "18": {
      "L": "While he was yet speaking, there came also another and said, 'Your sons and your daughters were eating and drinking wine in their eldest brother's house,'",
      "M": "While that man was still speaking, another arrived: 'Your sons and daughters were eating and drinking at the oldest brother's house —'",
      "T": "The third had not finished when a fourth came, and his news was the worst: 'Your children were at their eldest brother's feast —'"
    },
    "19": {
      "L": "'— and behold, a great wind came from across the wilderness and struck the four corners of the house, and it fell upon the young men, and they are dead; and I alone have escaped to tell you.'",
      "M": "'— a great wind came out of the wilderness and struck the four corners of the house. It collapsed on the young people, and they are all dead. I alone escaped to tell you!'",
      "T": "'— a massive windstorm came roaring out of the desert and collapsed the house on top of them. All your children are dead. I alone survived to bring you this news.'"
    },
    "20": {
      "L": "Then Job arose and rent his mantle and shaved his head and fell upon the ground and worshipped.",
      "M": "At this, Job stood up, tore his outer garment, shaved his head, fell to the ground, and worshipped.",
      "T": "Job rose from his place. He tore his robe. He shaved his head. Then he threw himself face-down on the ground — and he worshipped."
    },
    "21": {
      "L": "And he said, 'Naked I came from my mother's womb, and naked shall I return there. The LORD gave, and the LORD has taken away; blessed be the name of the LORD.'",
      "M": "He said, 'Naked I came from my mother's womb, and naked I will return. The LORD gave, and the LORD has taken away; may the name of the LORD be praised.'",
      "T": "'I came into this world with nothing, and I will leave the same way. The LORD gives and the LORD takes away — may his name be honored through it all.'"
    },
    "22": {
      "L": "In all this Job sinned not, nor charged God with foolishness.",
      "M": "In all this, Job did not sin or accuse God of wrongdoing.",
      "T": "Through all of this, Job did not sin. He made no bitter charge against God."
    }
  },
  "2": {
    "1": {
      "L": "Again there was a day when the sons of God came to present themselves before the LORD, and the Adversary also came among them to present himself before the LORD.",
      "M": "Again the heavenly beings came to present themselves before the LORD, and the Adversary came among them as well to stand before the LORD.",
      "T": "The divine assembly convened before the LORD once more. And again the Accuser appeared in their midst."
    },
    "2": {
      "L": "And the LORD said to the Adversary, 'From where have you come?' The Adversary answered the LORD and said, 'From going to and fro in the earth and from walking up and down in it.'",
      "M": "The LORD said to the Adversary, 'Where have you come from?' The Adversary answered, 'From roaming through the earth and walking back and forth on it.'",
      "T": "The LORD asked the Accuser again: 'Where have you been?' The same answer came back: 'Patrolling the earth — moving to and fro across it.'"
    },
    "3": {
      "L": "And the LORD said to the Adversary, 'Have you considered my servant Job, that there is none like him in the earth — a blameless and upright man who fears God and turns away from evil? And he still holds fast to his integrity, although you incited me against him to destroy him without cause.'",
      "M": "The LORD said to the Adversary, 'Have you taken note of my servant Job? There is no one like him on earth — blameless and upright, fearing God and turning from evil. He still maintains his integrity, even though you incited me against him to ruin him without cause.'",
      "T": "'Have you looked at my servant Job? He stands without peer on this earth — a man of complete integrity who fears me and rejects evil. He is still holding fast, even after you turned me against him to destroy him for no reason.'"
    },
    "4": {
      "L": "And the Adversary answered the LORD and said, 'Skin for skin! All that a man has he will give for his life.'",
      "M": "The Adversary answered the LORD, 'Skin for skin! A man will give everything he has to save his own life.'",
      "T": "'Skin for skin!' the Accuser shot back. 'A man will sacrifice anything to keep his own life. Possessions are one thing — touch his body, and we will see a different Job.'"
    },
    "5": {
      "L": "But put forth your hand now and touch his bone and his flesh, and he will curse you to your face.",
      "M": "'But reach out now and strike his flesh and his bones — he will surely curse you to your face.'",
      "T": "'Touch his body — strike bone and flesh — and his piety will crack. He will curse you openly.'"
    },
    "6": {
      "L": "And the LORD said to the Adversary, 'Behold, he is in your hand; only preserve his life.'",
      "M": "The LORD said to the Adversary, 'Very well, he is in your hands. Only spare his life.'",
      "T": "The LORD gave his answer: 'He is in your hands. Do what you will — but do not kill him.'"
    },
    "7": {
      "L": "So the Adversary went out from the presence of the LORD and struck Job with loathsome boils from the sole of his foot to the crown of his head.",
      "M": "The Adversary left the LORD's presence and afflicted Job with painful, festering sores from the soles of his feet to the top of his head.",
      "T": "The Accuser left the divine court and immediately struck Job with agonizing, suppurating sores — every inch of him, from foot to scalp."
    },
    "8": {
      "L": "And he took himself a potsherd to scrape himself withal, and he sat down among the ashes.",
      "M": "Job took a piece of broken pottery to scrape his sores while he sat among the ashes.",
      "T": "Job took a broken shard of pottery to scrape at his wounds and sat down in the ash heap — the posture of complete desolation."
    },
    "9": {
      "L": "Then his wife said to him, 'Do you still hold fast your integrity? Curse God and die.'",
      "M": "His wife said to him, 'Are you still holding on to your integrity? Curse God and be done with it.'",
      "T": "His wife could not endure it: 'You are still clinging to your integrity? Curse God and die. End this.'"
    },
    "10": {
      "L": "But he said to her, 'You speak as one of the foolish women speaks. Shall we receive good from God and shall we not receive evil?' In all this Job sinned not with his lips.",
      "M": "But he replied, 'You are speaking like a foolish woman. Shall we accept good from God and refuse to accept adversity?' In all this, Job did not sin with his lips.",
      "T": "But Job answered her: 'You sound like a senseless woman. If we accept blessings from God's hand, can we not also accept suffering?' Through all of this, Job did not sin with his words."
    },
    "11": {
      "L": "Now when Job's three friends heard of all this evil that had come upon him — Eliphaz the Temanite, and Bildad the Shuhite, and Zophar the Naamathite — they came every one from his own place and met together to mourn with him and to comfort him.",
      "M": "When Job's three friends — Eliphaz the Temanite, Bildad the Shuhite, and Zophar the Naamathite — heard about all the adversity that had come upon him, they each came from their own region and arranged to meet together to express their sympathy and comfort him.",
      "T": "Three of Job's closest friends heard the reports of all the suffering that had fallen on him. Eliphaz the Temanite, Bildad the Shuhite, and Zophar the Naamathite — they made arrangements and traveled together from their homes to be with him in his grief."
    },
    "12": {
      "L": "And when they lifted up their eyes from afar and did not recognize him, they lifted up their voice and wept, and they rent every man his mantle and sprinkled dust upon their heads toward heaven.",
      "M": "When they looked up from a distance, they could not even recognize him. They wept aloud, each tearing his outer garment and throwing dust into the air over his head as a gesture of grief directed toward heaven.",
      "T": "From a distance they saw him — and did not recognize him. They burst into loud weeping. Each man tore his robe; they scooped up handfuls of dirt and flung it skyward in anguished grief."
    },
    "13": {
      "L": "And they sat down with him upon the ground seven days and seven nights, and none spoke a word to him, for they saw that his grief was very great.",
      "M": "They sat on the ground beside him for seven days and seven nights. No one spoke a single word to him, for they could see how overwhelming his suffering was.",
      "T": "For seven days and seven nights they sat with him on the ground in silence. No one spoke. They could see that his pain was beyond words."
    }
  },
  "3": {
    "1": {
      "L": "After this Job opened his mouth and cursed his day.",
      "M": "After this, Job opened his mouth and cursed the day he was born.",
      "T": "When the silence finally broke, it was Job who broke it — he opened his mouth and cursed the day of his birth."
    },
    "2": {
      "L": "And Job spoke and said:",
      "M": "Job spoke and said:",
      "T": "And this was his lament:"
    },
    "3": {
      "L": "Let the day perish on which I was born, and the night that said, 'A man is conceived.'",
      "M": "Let the day on which I was born perish, and the night that announced, 'A boy has been conceived.'",
      "T": "Let that day be erased — the day I was born.\nLet that night be expunged — the night when word came: 'A son is conceived.'"
    },
    "4": {
      "L": "Let that day be darkness! Let not God above inquire after it, and let no light shine upon it.",
      "M": "Let that day be turned to darkness. May God above not care for it, nor light shine upon it.",
      "T": "Let that day be swallowed by darkness.\nLet God withhold his gaze from it.\nLet no light ever find it again."
    },
    "5": {
      "L": "Let darkness and the shadow of death claim it; let a cloud dwell upon it; let the blackness of the day terrify it.",
      "M": "May darkness and deep shadow reclaim it; may a cloud settle over it; may the blackness of that day strike it with terror.",
      "T": "Let darkness and death-shadow seize it.\nLet a stormcloud settle on its face.\nLet the suffocating dark of eclipse make it tremble."
    },
    "6": {
      "L": "As for that night — let thick darkness seize it; let it not rejoice among the days of the year; let it not come into the number of the months.",
      "M": "As for that night — let pitch darkness take it; let it not be counted among the days of the year; let it not enter the reckoning of the months.",
      "T": "And that night — let thick darkness swallow it whole.\nBlot it from the calendar.\nCut it from the count of months — let it cease to exist."
    },
    "7": {
      "L": "Lo, let that night be desolate; let no joyful voice come into it.",
      "M": "Let that night be barren; let no sound of joy enter it.",
      "T": "Let that night stand alone and barren.\nLet no shout of joy ever be heard within it."
    },
    "8": {
      "L": "Let them curse it who curse the day — those who are ready to rouse up Leviathan.",
      "M": "Let those who are skilled at cursing days put a curse on it — those who know how to rouse Leviathan.",
      "T": "Let professional cursers curse that night —\nthose dark craftsmen ready to unleash Leviathan from the deep."
    },
    "9": {
      "L": "Let the stars of its dawn be dark; let it look for light but have none, and let it not see the dawning of the day.",
      "M": "May the stars of its predawn twilight grow dark; may it wait for light that never comes; may it never see the breaking of morning.",
      "T": "Let the stars of its twilight go dark.\nLet it wait for the light that never arrives.\nLet it never see the eyelids of morning open."
    },
    "10": {
      "L": "Because it did not shut the doors of my mother's womb, nor hide sorrow from my eyes.",
      "M": "Because it did not close the doors of my mother's womb to me, nor hide trouble from my eyes.",
      "T": "Because it did not shut the doors of the womb —\nbecause it let me through into all this sorrow."
    },
    "11": {
      "L": "Why did I not die from the womb? Why did I not give up the ghost when I came out of the belly?",
      "M": "Why did I not die at birth? Why did I not perish when I came from the womb?",
      "T": "Why did I not die at the moment of birth?\nWhy did I not breathe my last as I came out of the womb?"
    },
    "12": {
      "L": "Why did the knees receive me? Or why the breasts, that I should suck?",
      "M": "Why were there knees to receive me, and breasts for me to nurse?",
      "T": "Why were knees there to hold me?\nWhy were there breasts to nurse me into life?"
    },
    "13": {
      "L": "For now should I have lain still and been quiet; I should have slept; then had I been at rest,",
      "M": "For then I would have lain down and been at rest; I would have slept and been at peace —",
      "T": "For then I would be lying down in peace,\nasleep, and at rest at last —"
    },
    "14": {
      "L": "with kings and counsellors of the earth who built desolate places for themselves,",
      "M": "with kings and counselors of the earth who built themselves ruins,",
      "T": "at rest with the kings and statesmen of ancient times,\nwho built their monuments that now lie in rubble,"
    },
    "15": {
      "L": "or with princes who had gold, who filled their houses with silver.",
      "M": "or with princes who hoarded gold and filled their mansions with silver.",
      "T": "or with princes who glutted their palaces with gold and silver —\nall of them equally still in the dust."
    },
    "16": {
      "L": "Or as a hidden untimely birth I had not been, as infants that never saw light.",
      "M": "Or why was I not like a stillborn hidden away, like infants who never saw the light of day?",
      "T": "Or better still — why was I not a stillborn,\nlike those infants who never opened their eyes to light?"
    },
    "17": {
      "L": "There the wicked cease from troubling, and there the weary are at rest.",
      "M": "There the wicked cease from their turmoil, and there the exhausted find rest.",
      "T": "There the wicked stop their endless schemes;\nthere the weary finally lay down their burden."
    },
    "18": {
      "L": "There the prisoners rest together; they hear not the voice of the oppressor.",
      "M": "There the prisoners rest together; they no longer hear the taskmaster's shout.",
      "T": "There the prisoners lie down undisturbed,\nno longer hearing the taskmaster's bark."
    },
    "19": {
      "L": "The small and the great are there, and the servant is free from his master.",
      "M": "The lowly and the great are alike there, and the slave is free from his master.",
      "T": "Small and great are equal there.\nThe slave breathes free — his master cannot follow."
    },
    "20": {
      "L": "Why is light given to him that is in misery, and life to the bitter in soul?",
      "M": "Why is light given to the one who suffers, and life to those whose souls are bitter?",
      "T": "Why is light given to the miserable?\nWhy is life handed to those whose souls are bitter with grief?"
    },
    "21": {
      "L": "who long for death but it comes not, and who search for it more than for hidden treasures,",
      "M": "to those who long for death that does not come, who search for it more eagerly than for buried treasure,",
      "T": "Those who ache for death that will not come —\nwho dig for it the way miners dig for hidden gold —"
    },
    "22": {
      "L": "who rejoice exceedingly and are glad when they can find the grave?",
      "M": "who would be overjoyed and exult when they finally reach the grave?",
      "T": "who would leap with joy, who would shout in relief,\nif only they could find the grave."
    },
    "23": {
      "L": "Why is light given to a man whose way is hidden, and whom God has hedged in?",
      "M": "Why is life given to a man whose way is hidden, whom God has fenced in on every side?",
      "T": "Why give light to the man whose path God has barricaded,\nwhose way forward is hidden from him on every side?"
    },
    "24": {
      "L": "For my sighing comes before my food, and my roarings are poured out like the waters.",
      "M": "For my groaning comes even before my food, and my cries pour out like rushing water.",
      "T": "My sighs come before bread reaches my mouth.\nMy cries of anguish pour out like floodwater."
    },
    "25": {
      "L": "For the thing which I greatly feared has come upon me, and that which I was afraid of has come unto me.",
      "M": "What I dreaded most has befallen me; what I feared has come upon me.",
      "T": "The catastrophe I dreaded most has arrived.\nThe very thing I feared has come."
    },
    "26": {
      "L": "I was not at ease, neither had I rest, neither was I quiet, yet trouble came.",
      "M": "I had no ease, no rest, no peace — yet trouble still came.",
      "T": "No ease. No rest. No quiet peace.\nAnd still — trouble came."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 1–3 written.')

if __name__ == '__main__':
    main()
