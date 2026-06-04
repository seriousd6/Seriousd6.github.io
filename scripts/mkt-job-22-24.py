"""
MKT Job chapters 22–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-22-24.py

=== Contested-term decisions ===

H7706 (שַׁדַּי, Shaddai): "the Almighty" in all tiers throughout — consistent with all
      prior Job scripts. The Almighty is Eliphaz's preferred title for God (ch.22 uses
      it 5× as appeals to repentance). Carried from chs.16–18.

H410  (אֵל, El): "God" in all tiers. Appears in 22:2, 22:12, 22:13, 23:16.
H433  (אֱלוֹהַּ, Eloah): "God" in all tiers. 22:26, 24:12.

H3068 (יהוה): Does not appear in these three chapters per interlinear.

H5315 (נֶפֶשׁ, nefesh, 23:13): "what his soul desires" — L retains soul-language for
      source transparency; M "what he wills"; T "what he purposes." The divine nefesh
      here signals God's sovereign will, not a Greek psychê — it is the self that wills.
      Embodied, purposeful, not immaterial. Carried from chs.16–18.

H7307 (רוּחַ): Does not appear in these chapters.

H7563 (רָשָׁע, rasha): "the wicked" / "wicked" in all tiers — Bildad used it of the
      wicked in ch.18; now Job uses it of those who oppress the poor (24:6). Same word,
      different polemical direction. "Wicked" retained throughout.

H7585 (שְׁאוֹל, Sheol): "Sheol" in all tiers at 24:19 — retained as proper noun
      throughout Job. Consistent with chs.17, 21.

H6757 (צַלְמָוֶת, tsalmaveth): "the shadow of death" / "deep darkness" — the LXX reads
      "shadow of death." Both are defensible; this text (24:17) makes the darkness
      dangerous (the criminals are at home in it), which argues for retaining the more
      vivid "shadow of death" in L/M; T reads "death's own darkness."

=== Dramatic irony note (ch.22) ===

Eliphaz's third speech (ch.22) is the only place in the dialogue where a friend makes
explicit, specific accusations against Job: taking pledges without cause, withholding
water and bread, exploiting widows and orphans. The reader knows from chs.1–2 that
these accusations are entirely false. This irony saturates the T tier: Eliphaz's call
to repentance is theological sound advice aimed at the wrong man. The T tier surfaces
this without editorializing — the beauty and the wrongness are held together.

=== Aspect and tense notes ===

Ch.22: Eliphaz uses a mix of perfect (describing Job's alleged past sins, vv.6–9) and
imperfect (describing the consequences, vv.10–11). The perfects of accusation are
decisive: "you have done these things." The imperfects of consequence are ongoing:
"therefore snares are around you."

The call to repentance (vv.21–30) shifts to conditional + imperfect: "if you return...
you will be built up." The conditional frame acknowledges that the outcome depends on
Job's response. T preserves this conditionality without softening it.

Ch.23: Job's speech moves between longing (imperfect — ongoing desire), confidence
(perfect of declaration — "I have kept his way," v.11, stating completed faithfulness),
and fear (imperfect — ongoing condition). The pivot at v.10 ("I shall come forth as
gold") is a confident imperfect-of-certainty — not a wish but an expectation. T renders
it as Job's settled conviction, not a fragile hope.

Ch.24: The social injustice catalog (vv.2–12) uses imperfects throughout — these things
are always happening, not historical events. The "light-rebels" section (vv.13–17) also
uses imperfects: habitual wickedness. The fate-of-the-wicked passage (vv.18–24) uses
imperfects that can be read as either descriptive or confident-assertion ("they will be
exalted briefly and then fall"). Job closes with a perfect-as-challenge: "if not so,
who will prove me a liar?" — a completed claim awaiting response.

=== OT echo notes ===

22:6 — "stripped the naked of their clothing" — echoes Amos 2:8, Ezek 18:7: taking
         pledges from the poor is a covenant violation, not just social incivility.

22:9 — "widows / fatherless" — the two classes protected most explicitly in Torah
         (Exod 22:22–24; Deut 24:17–21). Eliphaz's accusations target the most
         theologically weighted victims in the Hebrew legal imagination.

23:10 — "I shall come forth as gold" — anticipates the refining-fire imagery of Zech
         13:9, Isa 48:10, Mal 3:3. Job's language reaches toward what the prophets will
         later make explicit: suffering as purification, not punishment.

24:19 — "so does Sheol those who have sinned" — the drought/snow-melt simile is a
         natural-world mashal (wisdom saying). Sheol as inevitable, impersonal force:
         see also Prov 27:20, Isa 5:14.

=== Structural notes ===

Ch.22 has three movements:
  vv.2–5   — theological argument: God gains nothing from Job's righteousness, so the
              suffering must arise from sin
  vv.6–20  — the indictment: specific accusations + announcement of consequence + the
              fate of the ancient wicked
  vv.21–30 — the call to restoration: conditional promises, each more beautiful than
              the last, culminating in intercession

Ch.23 has two movements:
  vv.2–9   — the search: Job longs for a hearing, cannot find God
  vv.10–17 — the confidence + fear: Job knows his own integrity; God knows it too;
              this is both reassuring and terrifying

Ch.24 has three movements:
  vv.1–12  — the theodicy question + catalog of social injustice
  vv.13–17 — the light-rebels: those who specifically choose darkness
  vv.18–25 — the fate of the wicked: Job's assertion that they will fall, ending with
              a direct challenge to anyone who disagrees
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
  "22": {
    "1": {
      "L": "Then Eliphaz the Temanite answered and said:",
      "M": "Then Eliphaz the Temanite answered:",
      "T": "Eliphaz the Temanite spoke:"
    },
    "2": {
      "L": "Can a man be profitable to God? Even the wise man profits only himself.",
      "M": "Can any human being be of use to God? Even the wise man's wisdom serves himself alone.",
      "T": "What can a human being offer God? The question answers itself: nothing. If you are wise, the wisdom profits you — not him. He needs nothing from us. This is Eliphaz's opening move, and it sets up everything that follows."
    },
    "3": {
      "L": "Is it any pleasure to the Almighty that you are righteous, or any gain that you make your ways blameless?",
      "M": "Does the Almighty take any pleasure in your being righteous? Does he gain anything from you walking without blame?",
      "T": "Your moral performance means nothing to God's well-being. He does not benefit from your righteousness, does not profit from your integrity. Eliphaz is saying: if God gained nothing from your goodness, he had no reason to reward it — which means the suffering is not a reversal of reward. It must be something else. It must be punishment."
    },
    "4": {
      "L": "Is it because of your piety that he reproves you and brings you into judgment?",
      "M": "Is it because of your reverence for him that he calls you to account and puts you on trial?",
      "T": "Would God go to all this trouble over you because he fears you? Because he respects your piety? Eliphaz thinks the idea is absurd, and he uses the absurdity to set up the real accusation: if reverence didn't bring God's wrath, something else did."
    },
    "5": {
      "L": "Is not your wickedness great? Your iniquities without end?",
      "M": "Your wickedness is immense — surely — and your iniquities without limit.",
      "T": "Here is the accusation, stated plainly: the suffering is this vast, so the sin must be this vast. Eliphaz does not have evidence. He has a theology, and Job has become the proof text."
    },
    "6": {
      "L": "For you have taken pledges from your brothers without cause and stripped the naked of their clothing.",
      "M": "You have seized collateral from your kinsmen for no reason, and stripped people of the very clothes on their backs.",
      "T": "Now the accusations become specific, and specific charges require evidence that Eliphaz does not have. He demanded collateral from his own kin with no debt to secure. He stripped people who had nothing left to strip. These are real sins — they appear in the prophets and the law as covenant violations. But they are not Job's. We know this. Eliphaz does not."
    },
    "7": {
      "L": "You have not given water to the weary to drink, and you have withheld bread from the hungry.",
      "M": "You have not given the weary traveler water to drink; you have withheld bread from the starving.",
      "T": "Water for the exhausted traveler, bread for the starving — in this culture these were not optional courtesies but moral absolutes. Withholding them was a violation of the most basic human obligation. Eliphaz says Job did exactly this. It is false. And it is precisely the kind of sin that Job has never committed."
    },
    "8": {
      "L": "The man of power had the earth, and the man of rank dwelt in it.",
      "M": "But the powerful man possessed the land, and the man of high standing settled in it.",
      "T": "Eliphaz's picture of the world Job supposedly inhabited: the rich and prominent took everything, and Job — wealthy, honored, influential — was one of them. In Eliphaz's reading, Job used his position not to protect the vulnerable but to take from them."
    },
    "9": {
      "L": "You have sent widows away empty, and the arms of the fatherless have been crushed.",
      "M": "You have turned widows away empty-handed; you have broken the strength of the orphan.",
      "T": "Two classes that Torah protected most explicitly: widows and orphans. Both appear in Israel's covenant law as specially guarded. Eliphaz accuses Job of targeting them specifically — sending the widow away with nothing, crushing whatever small power of defense the orphan had left. Still false. Still deliberate."
    },
    "10": {
      "L": "Therefore snares surround you, and sudden dread throws you into panic.",
      "M": "That is why traps are all around you now, and sudden terror has seized you.",
      "T": "This is the theological payoff: the suffering proves the sin. The snares, the sudden terror — these are God's answer to documented wrongdoing. The suffering explains the sin; the sin explains the suffering. Job has been enclosed in Eliphaz's closed system, and there is no exit from inside it."
    },
    "11": {
      "L": "Or darkness so thick that you cannot see, and a flood of water overwhelming you.",
      "M": "Darkness so dense you cannot see through it, and a flood of waters sweeping over you.",
      "T": "The darkness is total. No way to read what's ahead. And then the flood — not rain but full inundation, the kind that leaves no foothold, no place to stand. Eliphaz is still describing Job's suffering as punishment, but the imagery has gone elemental."
    },
    "12": {
      "L": "Is not God high in the heavens? Look how high the stars are exalted.",
      "M": "Is not God in the heights of heaven? See how high the stars tower above you.",
      "T": "God's height is supposed to be intimidating here — a reminder of the distance between the divine and the human. Eliphaz says: look up. The stars are unreachably far. God is higher still. The implication is clear: from that height, God sees everything, including what you have done down here."
    },
    "13": {
      "L": "And you say, 'What does God know? Can he judge through the dense cloud?'",
      "M": "And you say, 'What does God know? Can he see through the dense cloud to give judgment?'",
      "T": "Now Eliphaz puts words in Job's mouth — attributing to him the skeptic's position. You think the clouds block God's sight. You think the distance makes him ignorant. You are behaving, Eliphaz suggests, like someone who believes God cannot see what goes on down here in the dark."
    },
    "14": {
      "L": "Dense clouds cover him so that he does not see; he walks on the vault of heaven.",
      "M": "Dense clouds screen him so he cannot see; he walks only along the circuit of the sky.",
      "T": "Eliphaz finishes the view he has attributed to Job: God is too far above, wrapped in cloud, pacing the distant rim of heaven — occupied with cosmic affairs, blind to what happens below. This is not a position Job has ever taken. Eliphaz is condemning Job for a theology Job does not hold."
    },
    "15": {
      "L": "Will you keep to the ancient path that wicked men have walked —",
      "M": "Will you persist in the old road that wicked people once traveled —",
      "T": "The question is an accusation: you are following the road the wicked have always walked. There is nothing new about your situation — it is the ancient pattern. Great sinners, catastrophic consequences. Eliphaz has the lineage memorized."
    },
    "16": {
      "L": "— those who were snatched away before their time, their foundation swept away by a flood?",
      "M": "— those who were cut down before their time, whose foundation was swept away by a flood?",
      "T": "— the ones who did not even finish their years. Cut off early, their entire foundation dissolved like soil in a flash flood. The ground beneath their lives gave way all at once. This, Eliphaz implies, is where Job is headed."
    },
    "17": {
      "L": "They said to God, 'Turn away from us' — and 'What can the Almighty do to us?'",
      "M": "They were the ones who said to God, 'Leave us alone' — and 'What can the Almighty do to us?'",
      "T": "These were people who openly dismissed God — who looked at the Almighty and said: what use are you? Go away. We do not need you. Eliphaz is comparing Job to them, suggesting that Job's questioning of God's justice is really just this ancient defiance in a more sophisticated disguise."
    },
    "18": {
      "L": "Yet he had filled their houses with good things. But the counsel of the wicked is far from me.",
      "M": "Yet he had filled their houses with abundance — though the thinking of the wicked is far from my own.",
      "T": "Here the crack in Eliphaz's system opens: he has to acknowledge the paradox. God blessed the very men who dismissed him. Their houses were full. Eliphaz adds the disclaimer quickly — I am not like them — but the paradox he has just named is the exact problem Job has been pressing for twenty chapters. Eliphaz does not see the irony in his own argument."
    },
    "19": {
      "L": "The righteous see their ruin and rejoice; the innocent mock them:",
      "M": "The righteous see their destruction and celebrate; the innocent deride them:",
      "T": "In the traditional framework, the righteous get to witness the fall of the wicked and take satisfaction in it — the moral order has finally been vindicated. The innocent mock, not cruelly, but because the just outcome arrived at last. Eliphaz is placing Job on the side of the innocent, hoping the encouragement will land. It does not."
    },
    "20": {
      "L": "Surely our adversaries have been cut off, and what remained of them fire has consumed.",
      "M": "Surely our opponents are destroyed; what remained of them the fire has devoured.",
      "T": "The wicked are gone. Their substance is ash. This is the conclusion Eliphaz wants Job to draw: the system works, the wicked fall, the righteous survive. Look at the evidence. Therefore: repent, and you will survive."
    },
    "21": {
      "L": "Agree with him now, and be at peace; thereby good will come to you.",
      "M": "Make peace with him now and be reconciled; in that way good will find you.",
      "T": "The call to repentance arrives dressed as pragmatic advice: get on the right side of this. Stop fighting. The good you want is still possible — all it requires is surrender. Eliphaz does not know he is asking an innocent man to confess to sins he never committed."
    },
    "22": {
      "L": "Receive the law from his mouth; lay up his words in your heart.",
      "M": "Accept his instruction from his own mouth; store his words in your heart.",
      "T": "Take what God says. Do not argue with it. Receive it. Hold it in the deepest place you have. This is Eliphaz's vision of the restored relationship — submission, absorption, interior transformation. It is not bad advice in principle. It is simply aimed at the wrong person."
    },
    "23": {
      "L": "If you return to the Almighty, you will be built up; if you put iniquity far from your tents,",
      "M": "If you return to the Almighty, you will be restored; banish iniquity from your household,",
      "T": "The great Hebrew word for repentance: shuv — turn back. Return. If you make this turn, you will be rebuilt from the ruins. The prerequisite is clear: the iniquity must be removed from your tent, from the lived space of your life. For Job, this condition is impossible to meet — because there is no iniquity there."
    },
    "24": {
      "L": "then lay up your gold as dust, and the gold of Ophir among the stones of the wadis;",
      "M": "then treat your gold like ordinary dust, and your Ophir gold like stream-bed pebbles;",
      "T": "The prosperity promise comes wrapped in a strange instruction: stop treating gold as precious. When God is your treasure, gold becomes as ordinary as dust, as common as the rocks in a dry streambed. This is the paradox of restoration — wealth returns to those who stop grasping for it."
    },
    "25": {
      "L": "and the Almighty will be your gold and your gleaming silver.",
      "M": "and the Almighty himself will be your gold, your abundance of pure silver.",
      "T": "God replaces the gold. This is the heart of what Eliphaz is offering: not just that wealth returns, but that the relationship with God becomes itself the real treasure. The Almighty as the ultimate wealth. It is beautiful theology. And it is aimed at the wrong man."
    },
    "26": {
      "L": "For then you will delight yourself in the Almighty and lift your face to God.",
      "M": "Then you will take your delight in the Almighty, and lift your face toward God.",
      "T": "Joy in God becomes possible again. The face can be raised — no longer pressed to the ground in shame, no longer turned away in accusation. This is the freedom Eliphaz promises: upward, face toward God, delighting. Job wants exactly this. He cannot get it by the path Eliphaz is mapping."
    },
    "27": {
      "L": "You will pray to him and he will hear you; you will fulfill your vows.",
      "M": "You will pray to him and he will answer; you will fulfill what you have vowed.",
      "T": "Prayer restored. Access restored. The channel that has felt blocked — the channel Job has been shouting into — opened again. Vows made in devotion completed in gratitude. This is the picture of a man whose relationship with God is whole. Job longs for it. Eliphaz thinks all it costs is confession."
    },
    "28": {
      "L": "Whatever you decide will be established for you, and light will shine on your ways.",
      "M": "Whatever you determine will be settled; light will shine on all your paths.",
      "T": "The authority of the restored person: what you decree comes to pass. The light comes back. The darkness — the snares, the sudden terror, the flood — dissolves, and you walk in clarity again. Eliphaz's vision of restoration is genuinely beautiful. It will come true for Job. Just not for any of the reasons Eliphaz thinks."
    },
    "29": {
      "L": "When men are cast down you will say, 'There is lifting up'; and he will save the downcast in spirit.",
      "M": "When others are brought low, you will say, 'There is hope'; and he will save the one who bows his head.",
      "T": "The restored Job becomes the one who speaks hope into other people's low places. When someone else is in the pit, Job — who has been lower than any of them — will be the one who knows to say: there is still a lifting up. There is still a way out. He will know it from the inside."
    },
    "30": {
      "L": "He delivers even one who is not innocent; he will be delivered through the cleanness of your hands.",
      "M": "He will rescue even the person who is not innocent; he will be delivered through the purity of your hands.",
      "T": "The final verse is difficult and beautiful: even the not-innocent can be rescued — even someone who genuinely has sinned — through the intercession of righteous hands. Eliphaz may mean this as a generous concession: once your hands are clean, Job, others will be saved through you. Either way, the irony is acute: Job's hands already are clean. They have always been."
    }
  },
  "23": {
    "1": {
      "L": "Then Job answered and said:",
      "M": "Then Job answered:",
      "T": "Job answered:"
    },
    "2": {
      "L": "Even today my complaint is bitter; his hand is heavier than my groaning.",
      "M": "Even today my complaint is bitter; the burden laid on me is heavier than my crying out can express.",
      "T": "Notice: Job does not begin by defending himself. He begins with the weight of it. The complaint has not softened. The suffering itself — the pressure of it — is heavier than any words he can produce. His groaning does not come close to containing what he carries."
    },
    "3": {
      "L": "Oh that I knew where I might find him — that I might come to his dwelling place!",
      "M": "If only I knew where to find him — if only I could reach the place where he dwells!",
      "T": "This is the cry at the center of Job's book: where is God? Not 'does God exist?' — Job never doubts that. Where is he? If Job could find the address, he would go. He is not afraid of the encounter. He wants it desperately. The problem is that God has become unfindable."
    },
    "4": {
      "L": "I would set my cause in order before him and fill my mouth with arguments.",
      "M": "I would present my case before him in full order, and fill my mouth with the strongest arguments.",
      "T": "Job is not planning to plead for mercy. He is planning to argue. He has prepared his brief. He would lay out the case — carefully, completely, with every piece of evidence he possesses. His mouth full of arguments, not supplications. He comes as a man who knows his case is good."
    },
    "5": {
      "L": "I would know what he would answer me, and understand what he would say to me.",
      "M": "I would know what he would say in reply, and understand every word of his answer.",
      "T": "More than anything, Job wants to hear the other side. He is not afraid of God's response. He believes that if God answered, the answer would be — must be — something that makes sense of all this. Even if it is silence, the silence is an answer. Either way: speak. Answer. Say something."
    },
    "6": {
      "L": "Would he contend with me in the greatness of his power? No — he would give heed to me.",
      "M": "Would he use his vast power to overwhelm me in argument? No — he would hear me out.",
      "T": "Job's confidence here is remarkable: God would not simply overpower the argument with omnipotence. He would listen. He would attend to what Job has to say. Job is not afraid of an honest confrontation with God — because Job knows his own innocence, and he believes God knows it too, even if God is not saying so."
    },
    "7": {
      "L": "There an upright man could argue with him; and I would be delivered once and for all from my judge.",
      "M": "There a person of integrity could bring his case; and I would receive a final acquittal from my judge.",
      "T": "In this imagined hearing, the upright man — a category Job places himself in without apology — can make his case fully. And the verdict would come: released. Delivered from the role of defendant, which has been Job's position for chapters now. The judge who is also the one Job is accusing — once that judge heard the full case, Job would walk free."
    },
    "8": {
      "L": "But I go forward, and he is not there; and backward, but I cannot perceive him;",
      "M": "But I go east, and he is not there; I go west, and cannot find him;",
      "T": "The imagined hearing collapses against reality: God cannot be found. All directions exhausted. East — nothing. West — nothing. The search continues even though the search itself proves what Job cannot yet fully accept."
    },
    "9": {
      "L": "on the left where he works, but I cannot behold him; he turns to the right, but I cannot see him.",
      "M": "he works on the left, and I cannot see him; he conceals himself on the right, and I cannot spot him.",
      "T": "He is present — Job knows he is working, knows he is there — but he hides. Deliberately hides. He is not simply absent. He is present and concealed, which is a different and more painful thing than absence."
    },
    "10": {
      "L": "But he knows the way I take; when he has tested me, I shall come forth as gold.",
      "M": "But he knows the path I walk; when he has tried me, I will come out as gold.",
      "T": "Here is the pivot — one of the most beautiful moments in all of Job. Job cannot find God. But God can find Job. God knows the way Job is taking. And the trial: Job names it without flinching. He is in the furnace. But when it is finished — he will come out gold. Not damaged. Not destroyed. Purified. He is sure of this."
    },
    "11": {
      "L": "My foot has held fast to his steps; I have kept his way and not turned aside.",
      "M": "My foot has stayed on his track; I have held to his path without turning off.",
      "T": "This is not boasting. This is Job's evidence for the confidence of verse 10. He knows what he has done with his life. He has followed. He has not swerved. The integrity is not a claim made for effect — it is the ground he is standing on."
    },
    "12": {
      "L": "From the commandment of his lips I have not departed; I have treasured the words of his mouth more than my portion of food.",
      "M": "I have not departed from his commands; I have valued the words of his mouth more than my daily bread.",
      "T": "More than food. That is the measure. The commandments were not an obligation grudgingly kept — they were the food of his life, more sustaining than bread, more nourishing than anything physical. This is the portrait of a man who has genuinely loved God's instruction. The suffering cannot be explained by the life this verse describes."
    },
    "13": {
      "L": "But he is of one mind, and who can turn him? What his soul desires, that he does.",
      "M": "But he is resolute in his purpose, and who can change him? What he wills, that he carries out.",
      "T": "God does not negotiate. He has a will and that will does not shift. What he purposes happens — full stop. For Job, sitting in the wreckage, this divine inflexibility is both terrifying and strangely reassuring. God is not arbitrary. He has a purpose. Even this has a purpose. Job cannot see what it is, but the sovereignty of the one who ordains it at least means there is a reason."
    },
    "14": {
      "L": "For he will complete what is appointed for me; and many such things are with him.",
      "M": "He will carry out what he has ordained for me; and there is much more still with him.",
      "T": "God has more to do. The present suffering is not the whole of what God has planned — there is more. Whether the more is further suffering or eventual vindication, Job cannot see. But the God who appoints does not leave things incomplete. Whatever this is, it will be finished."
    },
    "15": {
      "L": "Therefore I am terrified at his presence; when I consider, I am shaken before him.",
      "M": "That is why I am shaken in his presence; when I think of him, dread fills me.",
      "T": "Here is the terror that sits alongside the trust. God is sovereign, inflexible, purposeful — and that makes him frightening. Not the way chaos is frightening, but the way certainty is frightening. Whatever God has decided for Job will happen. And Job does not yet know what he has decided."
    },
    "16": {
      "L": "God has made my heart faint, and the Almighty has dismayed me;",
      "M": "God has made my heart weak; the Almighty has shaken me with dread;",
      "T": "The courage required to maintain trust has cost him. His heart has been made soft — the word for clay losing its shape, or for courage failing. He is not a man of iron. The Almighty has frightened him, and the fright is ongoing."
    },
    "17": {
      "L": "yet I am not silenced by the darkness, nor by the thick gloom that covers my face.",
      "M": "yet I am not cut off by the darkness, nor by the deep darkness covering my face.",
      "T": "But he is still speaking. Still reaching. The darkness has not shut his mouth. Even with God hidden, even with terror working through him from within, even with deep darkness pressing against his face — he has not gone quiet. The chapter ends not with resolution but with Job still in the open, still insisting on being heard."
    }
  },
  "24": {
    "1": {
      "L": "Why are times not stored up by the Almighty, so that those who know him see his days of judgment?",
      "M": "Why does the Almighty not set appointed times, so that those who know him can witness his days of reckoning?",
      "T": "This is the question of theodicy itself: if God sees everything, why doesn't he schedule justice? Why are there no visible days of reckoning when God acts in observable history to right wrongs? Those who trust him should be able to point to such moments. Why can't they?"
    },
    "2": {
      "L": "There are those who remove boundary markers; they seize flocks by force and graze them.",
      "M": "Some people move the boundary stones; they steal flocks by force and pasture them.",
      "T": "Land theft — the most fundamental crime in an agrarian society. Boundary stones marked what was yours; to move them was to steal not just land but the future security of a family across generations. And the flocks taken openly, by force — not even pretending to hide it."
    },
    "3": {
      "L": "They drive off the donkey of the fatherless; they take the widow's ox as a pledge.",
      "M": "They drive away the orphan's donkey; they seize the widow's ox as collateral.",
      "T": "The orphan's donkey and the widow's ox — the only assets that stand between these people and destitution, their only means of working the land. The law explicitly protected these classes. The wicked ignore the law and strip protection from those who most need it."
    },
    "4": {
      "L": "They thrust the needy off the road; the poor of the earth all go into hiding together.",
      "M": "They shove the needy off the road; the poor of the land have all gone into hiding.",
      "T": "The roads belong to the powerful. The needy are pushed to the margins — forced to move through the wasteland, through the hidden places. Eventually they stop trying to use the public ways at all. They simply disappear, gathering together in their shared invisibility."
    },
    "5": {
      "L": "Behold, like wild donkeys in the desert they go to their labor, seeking prey in the wasteland as food for their children.",
      "M": "Look — like wild donkeys in the desert they go out to work, foraging in the wasteland for food for their children.",
      "T": "The poor, driven from the roads and the fields, now live like wild animals. The wilderness is their territory. They rise early to forage — the same rhythm as a predator hunting — because that is what survival in the margins requires. Children need to eat. The foraging is constant. This is what economic violence produces in the bodies of the people it touches."
    },
    "6": {
      "L": "In the field they reap fodder that is not their own; they glean in the vineyard of the wicked.",
      "M": "They harvest crops from fields that are not theirs; they glean leftover grapes in the wicked man's vineyard.",
      "T": "The gleaning law existed to protect the poor — fields could not be stripped bare; something had to be left for the destitute. But the poor now glean from the wicked man's vineyard, picking through scraps of what was once their own. The wicked eat off the labor of those they have dispossessed."
    },
    "7": {
      "L": "They spend the night naked without clothing, with no covering in the cold.",
      "M": "They spend the night naked, with no garment to cover them against the cold.",
      "T": "No shelter, no clothing, no warmth. The poor sleep exposed — in the cold that moves down from the mountains after dark, in the chill that finds every gap. The wicked man sleeps in his house. The man he has stripped sleeps under the open sky."
    },
    "8": {
      "L": "They are drenched by the mountain showers and cling to the rock for want of shelter.",
      "M": "They are soaked by the mountain rains and press against the rock for any protection.",
      "T": "Rain comes and they have nowhere to go. They press themselves against the rock face — the only thing between them and the weather. The embrace of the rock: desperate, cold, inadequate. This is what the theft of homes and land looks like from the inside."
    },
    "9": {
      "L": "They tear the fatherless child from the breast; they seize a pledge from the poor.",
      "M": "They snatch the fatherless infant from its mother's breast; they take collateral from the destitute.",
      "T": "The fatherless infant — the most defenseless creature imaginable — dragged from the breast. This is the violence at its extreme: not just seizing property, not just taking work animals, but reaching into the most intimate human act and ripping the child away. And from the poor: the last thing they had to offer, taken."
    },
    "10": {
      "L": "They go about naked without clothing; hungry, they carry the sheaves.",
      "M": "The poor go about without clothing; starving, they carry the harvest sheaves.",
      "T": "The workers who harvest the grain walk naked and hungry. They are producing food they will not eat. The sheaves pass through their arms into the storehouses of those who took their land, their clothing, their dignity. The labor is theirs. The benefit is not."
    },
    "11": {
      "L": "Between the walls they press out oil; they tread the winepresses, yet suffer thirst.",
      "M": "They press olives among the terrace walls; they tread the winepresses, yet they go thirsty.",
      "T": "Oil and wine pressed by people who cannot afford a swallow of either. Surrounded by abundance — within the walls of the winery — and thirsty. The proximity of what they cannot have is its own particular cruelty. They produce the wine. They go thirsty."
    },
    "12": {
      "L": "From the city men groan; the soul of the wounded cries out — yet God charges no one with wrong.",
      "M": "From the city the dying groan; the mortally wounded cry out — yet God lays no charge of wrongdoing.",
      "T": "The groan rises from inside the city itself — a constant low sound, the protest of the suffering that fills the streets. The dying cry out explicitly. And God does not flag this as a crime. No charge is laid. The cry goes up and, as far as anyone can see, nothing happens. This is the scandal Job is naming: not that God doesn't hear — but that he hears and, so far, does not act."
    },
    "13": {
      "L": "They are among those who rebel against the light; they do not know its ways, nor do they stay in its paths.",
      "M": "These are among those who rebel against the light; they do not know its ways and will not walk its paths.",
      "T": "Light in this poetry is moral clarity, the law, the divine order. The wicked do not just ignore it — they rebel against it. Active resistance to what is true. And they do not want to understand; they actively refuse to walk the path light marks. Darkness is not just their environment — it is their preference."
    },
    "14": {
      "L": "With the first light the murderer rises; he kills the poor and needy; in the night he acts as a thief.",
      "M": "The murderer rises before dawn and kills the poor and needy; in the night he becomes the thief.",
      "T": "A schedule of evil: the murderer goes out before sunrise — under the last darkness, when witnesses are absent. He targets the poor and needy specifically, because they have no protection and no recourse. When night falls, the same figure becomes the thief. The entire rotation of light and dark has been organized around harm."
    },
    "15": {
      "L": "The adulterer's eye watches for the twilight, saying, 'No eye will see me,' and he covers his face.",
      "M": "The adulterer's eye watches for the dusk, thinking, 'No one will spot me,' and he disguises his face.",
      "T": "Three criminals operating in three conditions of light: murderer at first light, thief at night, adulterer at twilight — the ambiguous hour. Each one using darkness as permission. The adulterer goes further and covers his face even in the dark. The shame knows it is shameful. The cover-up confirms what the act already is."
    },
    "16": {
      "L": "In the dark they dig through houses; by day they seal themselves in — they have no dealings with the light.",
      "M": "In the darkness they break through walls; by day they stay shut away — they want nothing to do with the light.",
      "T": "The burglars marked their targets in daylight and executed in darkness — day spent identifying, night spent breaking through. Then, inverting the normal rhythm of life, they seal themselves inside by day, sleeping while the honest world works. Their relationship to light and dark is a mirror image of everything right."
    },
    "17": {
      "L": "For the shadow of death is their morning; they are at home with the terrors of deep darkness.",
      "M": "The shadow of death is their morning; they are familiar with the horrors of death's darkness.",
      "T": "They have adapted to what kills other people. Death's own darkness — the kind thick enough to hide in — is not frightening to them; it is their native hour, their morning. The morning that restores the decent person is what shuts them in. The darkness that terrifies the innocent is where they thrive. They have become what they love."
    },
    "18": {
      "L": "Swift is he on the surface of the water; cursed is their portion in the land; he does not turn toward the vineyards.",
      "M": "He skims across the surface of the water like foam; his share of the land is under a curse; he does not go near the vineyards.",
      "T": "The wicked man passes across the surface of things like scum on water — quickly, leaving nothing behind, belonging nowhere. His portion is cursed, even if he cannot see it yet. He does not go near vineyards because the vineyard is associated with patient cultivation, with inheritance, with the long work of building something that lasts. None of that is his."
    },
    "19": {
      "L": "Drought and heat snatch away the snow waters; so does Sheol those who have sinned.",
      "M": "Just as drought and heat evaporate the melting snow, so Sheol takes those who have sinned.",
      "T": "The comparison is drawn from physics: snowmelt evaporates in drought and heat, and there is nothing left. That is how Sheol takes the wicked — not gradually, not slowly, but with the same natural inevitability. The sun does not negotiate with the snow. Sheol does not negotiate with the sinner."
    },
    "20": {
      "L": "The womb forgets him; the worm feeds on him with appetite; he will not be remembered; wickedness is snapped like a tree.",
      "M": "The womb that bore him forgets him; the worm devours him eagerly; he is no longer remembered; wickedness is broken off like a tree.",
      "T": "Complete erasure from every dimension of memory. The mother who carried him — even she forgets. The worm finds him satisfying, consumed with appetite. No community keeps his name. And wickedness itself — the principle he embodied — snapped off at the root, like a tree that falls without warning and is gone."
    },
    "21": {
      "L": "He preys on the barren woman who bears no child, and does no good to the widow.",
      "M": "He preys on the childless woman who cannot conceive, and shows no kindness to the widow.",
      "T": "The wicked man's particular cruelty targets the doubly vulnerable: the barren woman with no children to protect her, and the widow with no husband. In both cases the normal protections of relationship have been stripped away, and the wicked man steps into the gap not to help but to exploit."
    },
    "22": {
      "L": "He drags away the mighty with his strength; he rises up, and none can be sure of life.",
      "M": "By his power he brings even the strong man down; he rises up, and no one's life is secure.",
      "T": "The wicked man's violence is not limited to the helpless. Even the strong are not safe from him. Once his power grows large enough, even those who could ordinarily defend themselves cannot be certain of surviving. Power without restraint threatens the vulnerable first — and eventually, everyone."
    },
    "23": {
      "L": "Though he is given safety and he rests on it, yet his eyes are upon all their ways.",
      "M": "God allows him to rest in security, and he relies on that security — yet God's eyes are on every path he takes.",
      "T": "Here is the final word before Job's challenge: God sees. The wicked man is allowed to rest in apparent security — for now, for reasons we cannot fully understand. But God's eyes are on every step he takes. The inaction is not blindness. It is patience — or something that looks like patience from outside. The watching changes everything."
    },
    "24": {
      "L": "They are exalted for a little while, and then are gone; they are brought low and gathered in like all others; they are cut off like the tops of the grain.",
      "M": "They are lifted up for a moment and then they are gone; they sink down and are gathered in with everyone else; they are cut off like the head of a stalk of grain.",
      "T": "The exaltation of the wicked is real but brief. They rise — sometimes high — and then they come down. Not gradually: cut off the way grain is harvested, the whole thing severed at once and gathered in with everything else. Their end is not unique. It is not even dramatic. The grain is cut, the field is empty."
    },
    "25": {
      "L": "And if it is not so, who will prove me a liar and make my speech amount to nothing?",
      "M": "And if this is not true, who will prove me wrong and show that my words are worthless?",
      "T": "Job ends with a challenge. He has described the world as he sees it — the suffering of the righteous, the prosperity and eventual ruin of the wicked, the silence of God, the certainty that justice will come. If any of this is wrong, let someone say so. Bring evidence. He is not afraid of being corrected. He is afraid of being ignored. Ignore him if you can. Prove him wrong if you must. But do not pretend the question doesn't exist."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 22–24 written.')

if __name__ == '__main__':
    main()
