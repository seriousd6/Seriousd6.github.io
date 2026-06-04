"""
MKT Job chapters 16–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-16-18.py

=== Contested-term decisions ===

H7307 (רוּחַ, ruach): context-driven, as in chs.13–15.
      16:3  — "windy words" / "empty words" — phrase: דִּבְרֵי רוּחַ, words of wind.
              Job echoes Eliphaz's "east wind" taunt from 15:2, now turning it back on
              the friends. L "windy words," M "empty words," T idiomatically.
      17:1  — "My spirit is spent" — ruach as Job's inner vital force, the animating
              breath. L/M "spirit," T "the life in me."

H5315 (נֶפֶשׁ, nefesh): embodied self throughout, not Greek soul.
      16:4  — "your soul" / "my soul's stead" — L retains the idiom; M/T render "if
              you were in my place."
      18:4  — "he who tears himself" (נַפְשׁוֹ) — reflexive use: "himself."

H410  (אֵל, El): "God" in all tiers. Appears throughout ch.16–18.
H433  (אֱלוֹהַּ, Eloah): "God" in all tiers (16:20, 21).
H7563 (רָשָׁע, rasha): "wicked" in L/M, "wicked" in T — used by Bildad (ch.18) to
      describe the fated doom he intends as a veiled threat against Job.
H2611 (חָנֵף, chaneph): "hypocrite" (L — KJV tradition retained); "godless" (M/T).
      Carried from chs.13–15.
H7585 (שְׁאוֹל, Sheol): "Sheol" in L/M/T — retained as a proper name across all tiers
      in this passage (17:13, 17:16) since T reads better preserving the place-name.

H1368 (גִּבּוֹר, gibbor): "warrior/mighty warrior" — 16:14 God charges upon Job "like
      a warrior." L "warrior," M "great warrior," T "warrior who has already won."

H7717 (שָׂהֵד, sahed, 16:19): an Aramaic loanword used only here in the Hebrew Bible,
      meaning "witness/advocate." Paired with H5707 (עֵד, ed, standard "witness") for
      emphasis. L "advocate," M "advocate," T renders the heavenly intercessor motif
      fully, anticipating Job 19:25 and NT mediation. This is the theological apex of
      the chapter.

H4009 (מִבְטָח, mivtach, 18:14): "confidence/security" — what is torn from the wicked
      man's tent.

H1060 (בְּכוֹר, bekor, 18:13): "firstborn of death" — unique to this verse; likely
      refers to the most lethal disease, death's premier offspring. Retained literally
      in all tiers; T elaborates the imagery.

מֶלֶךְ בַּלָּהוֹת ("king of terrors," 18:14): "king of terrors" in all tiers — too
      resonant to soften. Death personified as sovereign. T gives it full weight.

=== Aspect and tense notes ===

Ch.16 is Job's response to Eliphaz (from ch.15). The chapter falls in three movements:
  vv.1–6   — rebuttal: the friends are miserable comforters
  vv.7–17  — description of God's assault (military, hunting, and judicial imagery
              combined); imperfects throughout indicate ongoing torment
  vv.18–22 — the cry for a witness: two vocatives (O earth! / my witness in heaven)
              framing the most forward-looking theological moment in the poem so far.
The perfects in vv.18–19 mark decisive, completed appeals: Job has cried out to earth
and claimed a heavenly advocate. These are acts, not wishes.

Ch.17 uses imperfects and perfects in rapid alternation. Job's description of his
deterioration (vv.1–7) is in the completed aspect — these things have already happened.
The hope-statements (vv.9–10) are Job's contrary-to-fact assertions: the righteous man
holds on, even if I cannot. The final movement (vv.13–16) is Future / Conditional:
"if I wait, Sheol is my house." T captures the resignation without melodrama.

Ch.18 (Bildad): The fate-of-the-wicked poem (vv.5–21) uses imperfects consistently —
the doom of the wicked is a relentless, rolling present tense, never finished, always
in process. T renders this as an unrelenting present, which intensifies the threat
that Bildad is implicitly directing at Job.

=== OT echo notes ===

16:18 — "O earth, do not cover my blood" echoes the blood of Abel crying from the
         ground (Gen 4:10). Job is claiming the status of unjustly slain innocent. T
         surfaces this explicitly.

16:19–21 — the "witness in heaven" and "advocate on high" (H5707 + H7717) anticipate
         Job 19:25 ("my Redeemer lives") and NT intercession (Heb 7:25; 1 John 2:1).
         T notes this connection without anachronism — Job reaches toward something
         he cannot fully name.

17:6 — "a byword of the peoples" (H4914) — Job has become a mashal, a proverb, a
         cautionary tale. This is profound shame in honor-shame culture.

18:15 — brimstone scattered over the wicked man's dwelling echoes the destruction of
         Sodom and Gomorrah (Gen 19:24). T surfaces this.

18:14 — "king of terrors" — Death personified as a royal figure receiving the condemned.
         The image is unparalleled in the Hebrew Bible in its directness.

=== Structural notes ===

Ch.16: The witness motif (vv.18–21) is the emotional and theological center. Job moves
from the earth (v.18 — material witness, like Abel's blood) to heaven (v.19 — the
unseen advocate) and back to the friends' mockery (v.20) before ending with the
practical deadline: his years are running out (v.22). The movement is horizontal →
vertical → horizontal, framing the divine intercession between earthly realities.

Ch.17: Shorter, more fragmented — Job's speech is breaking down under weight of despair.
The byword-verse (v.6) is the hinge: from protesting his integrity (vv.3–5) to
accepting his social destruction (vv.6–7). Verses 13–16 are Job naming his situation
as plainly as he can: Sheol is his house. He makes his bed there.

Ch.18: Bildad's entire "fate of the wicked" poem is a thinly veiled accusation against
Job. The reader knows Job is innocent (ch.1–2); Bildad does not. T can surface this
irony — these vivid descriptions of doom were meant to describe Job, but they describe
the wrong man.
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
  "16": {
    "1": {
      "L": "And Job answered and said:",
      "M": "Then Job answered:",
      "T": "Job answered:"
    },
    "2": {
      "L": "I have heard many such things; comforters of trouble are you all.",
      "M": "I have heard all this before. You are miserable comforters, every one of you.",
      "T": "I have heard every one of these lines before. You came to bring comfort and you have brought only more trouble. All of you. Miserable comforters — that is what you are."
    },
    "3": {
      "L": "Shall windy words have an end? Or what emboldens you that you answer?",
      "M": "Will these empty words never stop? What gives you the confidence to keep answering me?",
      "T": "When does the stream of wind end? You pile words on words and not one of them carries any weight. And what is it that makes you so certain you have something to say? What emboldens you to keep answering?"
    },
    "4": {
      "L": "I also could speak as you do; if your soul were in my soul's place, I could heap up words against you and shake my head at you.",
      "M": "I could talk just like you if you were in my place — I could pile words against you and shake my head at you.",
      "T": "I could do exactly what you are doing. Switch our positions — put you where I am and me where you are — and watch how easily I could stack arguments against you and shake my head in practiced sympathy. It is easy to speak when you are the one who is well."
    },
    "5": {
      "L": "I would strengthen you with my mouth, and the consolation of my lips would assuage your pain.",
      "M": "I would strengthen you with my words, and the comfort of my lips would ease your grief.",
      "T": "But I would not do what you have done. Every word I used would be aimed at strengthening you. Whatever I said would be designed to ease the pain, not to prove a theological system at your expense."
    },
    "6": {
      "L": "Though I speak, my pain is not assuaged; and though I hold back, what departs from me?",
      "M": "If I speak, the pain is not relieved; and if I stay silent, how much of it leaves me?",
      "T": "Neither choice helps. Speak: the pain stays. Stay silent: the pain stays. Nothing I do changes the suffering by a single degree. I am trapped by it."
    },
    "7": {
      "L": "Surely now he has made me weary; he has desolated all my company.",
      "M": "But now he has utterly exhausted me; he has made desolate everyone around me.",
      "T": "He has ground me down past exhaustion. And not only me — everyone who was part of my life has been driven away, left desolate. The attack stripped me of my network as completely as it stripped me of my health."
    },
    "8": {
      "L": "You have shriveled me — which is a witness; and my leanness rises up to testify against me to my face.",
      "M": "You have wasted my flesh until it shows — that itself is a witness; my emaciation rises up and testifies against me to my face.",
      "T": "Look at what has been done to this body. My skin hangs. The wasting is visible evidence — and evidence that is being used against me. My own deteriorating flesh stands up and testifies: here is the guilty party. My body accuses me."
    },
    "9": {
      "L": "He has torn me in his anger and is hostile to me; he gnashes his teeth at me; my foe sharpens his eyes against me.",
      "M": "He has torn me apart in his wrath and pursued me; he gnashes his teeth at me; my enemy fixes his sharpened gaze upon me.",
      "T": "This is what it looks like from inside: a predator with bared teeth, tearing into me out of rage, tracking me with focused, narrowed eyes. Hostility. Grinding teeth. A gaze sharpened to a point."
    },
    "10": {
      "L": "They have gaped at me with their mouth; they have struck me on the cheek in reproach; they have massed together against me.",
      "M": "They open their mouths wide at me; they strike my cheek in contempt; they have gathered themselves together against me.",
      "T": "A mob of mockers with their mouths open wide — the gesture of maximum contempt. Blows to my cheek, not from anger but from pure disdain, which is worse. And all of them coordinated, unified, a single front of opposition."
    },
    "11": {
      "L": "God has handed me over to the ungodly and cast me into the hands of the wicked.",
      "M": "God has surrendered me to the evildoers and thrown me into the hands of the wicked.",
      "T": "God is not merely absent here. He is the one who opened the door. He handed me over — surrendered me, gave me up — to the evildoers. The wicked men did not find me on their own; they were given me."
    },
    "12": {
      "L": "I was at ease, and he shattered me; he seized me by the neck and dashed me to pieces; he set me up as his target.",
      "M": "I was living in ease, and he shattered me; he grabbed me by the neck and broke me apart; he stood me up as his target.",
      "T": "There was a before. I was at peace — prosperous, settled, undisturbed. Then he seized me by the neck and shook me to pieces. And then he stood me up in the open field as a target. The man he is destroying was not warned. He was not offered a reason. He was simply aimed at."
    },
    "13": {
      "L": "His archers encircle me; he pierces my kidneys without mercy and pours my gall upon the ground.",
      "M": "His archers surround me; he slashes into my kidneys without mercy and spills my gall on the ground.",
      "T": "Archers on every side, no gap to run through. He cuts into the deep interior — the kidneys, where emotion lives, where the center of a person is — and shows no mercy. He spills out what is innermost. Nothing is kept. Everything is poured out on the ground."
    },
    "14": {
      "L": "He breaks me through with breach upon breach; he runs upon me like a warrior.",
      "M": "He breaks through me, breach after breach; he charges at me like a great warrior.",
      "T": "Every wall I had is gone. He has broken through them all, breach after breach, each gap wider than the last. And then he runs through the wreckage like a warrior who has already won — not from necessity now, just from momentum."
    },
    "15": {
      "L": "I have sewn sackcloth upon my skin and laid my horn in the dust.",
      "M": "I have sewn sackcloth over my skin and pressed my dignity down into the dust.",
      "T": "I have sewn the mourning-cloth directly onto my skin — not draped, sewn — as if it is part of me now. And every sign of my former strength and standing: I have ground it into the dust myself. There is no dignity left worth protecting."
    },
    "16": {
      "L": "My face is reddened with weeping, and the shadow of death is on my eyelids —",
      "M": "My face is flushed raw from weeping, and the shadow of death rests on my eyelids —",
      "T": "Weeping has burned my face. And the shadow of death — that particular darkness — has settled on my eyelids like something that has decided to stay —"
    },
    "17": {
      "L": "— though no violence is in my hands, and my prayer is pure.",
      "M": "— yet no violence has been done by my hands, and my prayer has been pure.",
      "T": "— and for what? My hands are clean. Every prayer I have prayed has been honest before God. The suffering cannot be answered by any fault of mine."
    },
    "18": {
      "L": "O earth, cover not my blood, and let my cry have no resting place!",
      "M": "O earth, do not cover my blood; let my cry find no place to settle!",
      "T": "I call on the earth itself: do not swallow my blood. When Abel was murdered, his blood cried from the ground — let mine do the same. Do not absorb it, do not silence it. Let the cry stay airborne, restless, unanswered — because it has not yet been answered."
    },
    "19": {
      "L": "Even now my witness is in heaven, and my advocate is on high.",
      "M": "Even now my witness is in heaven, and my advocate is on high.",
      "T": "But there is this: even now, even in the midst of all this, something is on the other side. My witness is in heaven. There is an advocate standing for me in the highest place — someone who knows what I am and holds my case. I cannot see this advocate. I can barely name what I am reaching for. But I reach for it."
    },
    "20": {
      "L": "My friends mock me; but my eye weeps to God.",
      "M": "My friends scorn me, yet my eye pours out tears to God.",
      "T": "The men who came to comfort me are mocking me now. And I have nowhere left to turn but upward. My tears go to God — even the God who is doing this to me. I cannot stop seeking him. Even in accusation, I am still praying."
    },
    "21": {
      "L": "O that a man might plead with God as a man pleads for his neighbor —",
      "M": "If only a mortal man could plead with God the way a man pleads for his neighbor —",
      "T": "What I want is so simple: I want to be able to bring my case to God the way any ordinary person brings a dispute to a fellow human being. The access. The hearing. The possibility of being genuinely heard and genuinely answered —"
    },
    "22": {
      "L": "— for the years that number are coming, and I shall walk a path from which I will not return.",
      "M": "— for the few years left are slipping past, and I am walking a road from which there is no return.",
      "T": "— because the time is almost gone. What years remain are already moving past. I am already on the one-way road, the road that ends and does not loop back. The conversation has to happen now. There is no later."
    }
  },
  "17": {
    "1": {
      "L": "My spirit is destroyed; my days are extinguished; the grave is ready for me.",
      "M": "My spirit is spent; my days are put out; the grave is waiting for me.",
      "T": "The spirit in me is broken past repair. My days are guttered out. The only thing left prepared and waiting is the grave — and it is already ready."
    },
    "2": {
      "L": "Are there not mockers with me? And does not my eye dwell on their provocation?",
      "M": "Surely there are mockers all around me, and my eye rests on their hostile provocation.",
      "T": "I cannot look anywhere without seeing contempt. Mockers surround me. My eye takes it all in — the provocations, the sneer, the sustained hostility. I cannot not see it."
    },
    "3": {
      "L": "Lay down a pledge for me with yourself; who else will strike his hand for me?",
      "M": "Give me a pledge yourself; who else is there to strike hands with me?",
      "T": "I am appealing to you directly, God: be my guarantor. No one else will. There is not a person willing to seal a pledge on my behalf. You are the only one left who could stand as collateral — against yourself, on my behalf."
    },
    "4": {
      "L": "For you have hidden their hearts from understanding; therefore you will not exalt them.",
      "M": "For you have closed off their minds from true understanding; therefore you will not let them triumph.",
      "T": "The friends are not seeing clearly, and there is a reason: you have withheld understanding from them. Their blindness is not accidental. And because their wisdom is hollow — manufactured without real insight — they will not be the ones you vindicate in the end."
    },
    "5": {
      "L": "He who denounces his friends for gain — the eyes of his children shall fail.",
      "M": "He who betrays his friends for personal gain — his children's eyes will fail.",
      "T": "There is a principle operating here: inform against your friends for what you can get out of it, and the consequences reach your children. The betrayer's family pays. The pattern is reliable."
    },
    "6": {
      "L": "He has made me a byword among the peoples, and I am one before whose face men spit.",
      "M": "He has turned me into a proverb among the nations — I am one before whose face men spit.",
      "T": "God has made me a cautionary tale. My name is a proverb now — the byword for inexplicable disaster, the reference point people use when they want to name the worst that can happen to a person. And when they see me in the street, they do not lower their eyes out of respect. They spit."
    },
    "7": {
      "L": "My eye has grown dim with grief, and all my limbs are like shadows.",
      "M": "My eye has grown dim from sorrow, and all my limbs are like shadows.",
      "T": "Grief has clouded my sight. And my body is becoming insubstantial — I look at my arms, my hands, and they are like shadow on a wall. There is less and less of me here."
    },
    "8": {
      "L": "Upright men are appalled at this, and the innocent stirs himself against the godless.",
      "M": "Upright men are horrified by this; the innocent rises up against the godless.",
      "T": "The genuinely righteous observer — wherever such a person exists — is appalled watching this happen. And the innocent man does not stay passive in the face of it. He turns himself against the godless. Innocent suffering is supposed to provoke righteous resistance, not comfortable acceptance."
    },
    "9": {
      "L": "The righteous one holds to his way, and the one with clean hands grows ever stronger.",
      "M": "The righteous man keeps to his course, and the one with clean hands grows stronger and stronger.",
      "T": "Here is what I hold to, against everything surrounding me: the righteous man does not let go of his course. Clean hands are not weakened over time — they are strengthened. Integrity does not erode; it compounds."
    },
    "10": {
      "L": "But all of you, come now — I cannot find a wise man among you.",
      "M": "But come, all of you, try again — I still cannot find a wise man among you.",
      "T": "Come. All of you. Bring whatever you have left. I have been listening and looking for wisdom in what you say, and I have found none. Not one."
    },
    "11": {
      "L": "My days are past; my plans are broken off, even the deepest longings of my heart.",
      "M": "My days are over; my plans have been cut off — even the secret longings of my heart.",
      "T": "Time is up. Every plan I had — snapped. Every private hope, every deep intention of the heart that no one knew about — gone. Not faded; severed."
    },
    "12": {
      "L": "They turn night into day; they say, 'The light is near,' even in the face of darkness.",
      "M": "They make night into day; they say, 'The light is near,' even while darkness surrounds them.",
      "T": "The friends call the night day. They stand in the dark and insist the light is just around the corner. That is not hope — that is manufactured optimism, offered for someone else's benefit, not mine."
    },
    "13": {
      "L": "If I hope, Sheol is my house; I have made my bed in the darkness.",
      "M": "If I wait, Sheol is my home — I have made my bed in the darkness.",
      "T": "What am I waiting for? If I wait, there is only one destination. Sheol is my address. I have already made my bed there in the dark. The transition is underway."
    },
    "14": {
      "L": "I say to the pit, 'You are my father,' and to the worm, 'My mother and my sister.'",
      "M": "I call out to corruption, 'You are my father,' and to the worm, 'My mother and my sister.'",
      "T": "These are my family now. The rotting pit is my father. The worm is my mother and my sister. The relationships that define where a person belongs have been rewritten in the language of death and decay."
    },
    "15": {
      "L": "Where then is my hope? And who perceives any hope for me?",
      "M": "Where then is my hope? Who can see hope for me?",
      "T": "Where has it gone — the hope? I search for it and I cannot locate it. Can you see it? Can anyone? Point it out to me. I have lost the thread."
    },
    "16": {
      "L": "Shall it go down with me to the gates of Sheol? Together we shall descend into the dust.",
      "M": "Will it descend with me to the gates of Sheol? Together we shall go down into the dust.",
      "T": "My hope and I will go down together. Down to where hope ends — to the gates of Sheol, the boundary where life stops. Together into the dust. At least that: we will not be separated."
    }
  },
  "18": {
    "1": {
      "L": "And Bildad the Shuhite answered and said:",
      "M": "Then Bildad the Shuhite answered:",
      "T": "Bildad the Shuhite spoke:"
    },
    "2": {
      "L": "How long will you make an end of words? Consider, and then we will speak.",
      "M": "How long before you stop talking? Think first, and then we will have our say.",
      "T": "Are you going to let anyone else speak? You hunt for words and deploy them endlessly. Stop. Think. When you have actually thought, we will have a conversation worth having."
    },
    "3": {
      "L": "Why are we counted as cattle? Why are we vile in your sight?",
      "M": "Why do you regard us as animals? Why are we worthless in your eyes?",
      "T": "Is that what we are to you — livestock? You look at us and see creatures not worth reasoning with. We will not accept that contempt."
    },
    "4": {
      "L": "You who tear yourself in your anger — will the earth be abandoned for your sake? Or the rock removed from its place?",
      "M": "You who tear yourself apart in your rage — will the earth be forsaken on your account? Will the rock be moved from its place for you?",
      "T": "You are tearing yourself to pieces with your own anger. And you seem to expect the universe to rearrange itself around your suffering. The rock should move for you. The earth should be cleared for you alone. That is the scale of the arrogance beneath the grief."
    },
    "5": {
      "L": "Yes, the light of the wicked is put out, and the flame of his fire does not shine.",
      "M": "Yes, the light of the wicked is extinguished; the flame of his fire gives no light.",
      "T": "Here is the pattern — and Bildad is laying it out deliberately: the wicked man's light is snuffed. The fire that blazed so brilliantly is gone. They cannot produce lasting light, however bright they burned."
    },
    "6": {
      "L": "The light in his tent is darkened, and the lamp above him is put out.",
      "M": "The light in his tent grows dark, and the lamp over him is extinguished.",
      "T": "Every source of light in his household fails. The lamp that watched over him from above — it goes dark. There is nothing illuminating his home anymore."
    },
    "7": {
      "L": "His vigorous steps are cramped, and his own counsel throws him down.",
      "M": "His powerful stride is shortened, and his own schemes bring him down.",
      "T": "The confident stride he once had is cut short. And what ultimately destroys him is not an outside enemy — it is his own cleverness. His own plans become the trap that springs on him."
    },
    "8": {
      "L": "For he is cast into a net by his own feet, and he walks into a snare.",
      "M": "He is thrown into a net by his own feet, and he walks right onto a snare.",
      "T": "His own feet carry him there. He is not ambushed from outside — he wanders directly into the net. The trap he laid, or the trap laid for people like him, and his own walking does the rest."
    },
    "9": {
      "L": "A trap seizes him by the heel; a snare grips him.",
      "M": "A trap catches him by the heel; a snare holds him tight.",
      "T": "The trap takes him from behind, by the heel, as he walks — suddenly. And once the snare grabs hold, it does not release. There is no mechanism for escape built into it."
    },
    "10": {
      "L": "A rope is hidden in the ground for him, and a trap waits on his path.",
      "M": "A rope is buried in the ground for him, and a trap waits on his path.",
      "T": "The traps were set before he arrived. Buried in the earth, positioned on the road ahead. He walks into what was already prepared for him."
    },
    "11": {
      "L": "Terrors frighten him on every side and drive him at every step.",
      "M": "Terrors frighten him on every side and push him forward at every step.",
      "T": "He cannot find quiet. Terrors surround him in every direction — inside and outside, day and night — pushing him onward when he should stop, shattering his thoughts, denying him any peace."
    },
    "12": {
      "L": "His vigor is famished, and calamity stands ready at his side.",
      "M": "His strength is starved, and disaster stands ready at his side.",
      "T": "Even his strength is eaten away by what is coming. And disaster walks beside him — keeping pace, patient, prepared — ready for the moment."
    },
    "13": {
      "L": "The parts of his skin are devoured; the firstborn of death devours his limbs.",
      "M": "His skin is eaten away piece by piece; the firstborn of death devours his body.",
      "T": "Illness takes him systematically, piece by piece, the skin consumed. And the firstborn of death — the most lethal thing death produces, its most terrible offspring — moves through his body with purpose."
    },
    "14": {
      "L": "His security is torn from his tent, and he is marched to the king of terrors.",
      "M": "His confidence is ripped away from his home, and he is brought before the king of terrors.",
      "T": "Everything that made him feel safe is stripped away — torn from the very tent where he lived. And then he is marched forward, compelled, brought to the king of terrors himself. Death personified as a monarch, receiving his subject with full ceremony."
    },
    "15": {
      "L": "What is not his dwells in his tent; brimstone is scattered over his dwelling.",
      "M": "Something alien has moved into his tent; brimstone is scattered over his home.",
      "T": "Something that does not belong to him has moved into his house. His home has been taken over. And brimstone over the threshold — that particular smell of divine judgment, the sulfur of Sodom — burned into the ground where he lived."
    },
    "16": {
      "L": "Below, his roots dry up; above, his branches wither.",
      "M": "His roots dry up below; his branches wither above.",
      "T": "The destruction works from both directions at once. The roots go dry underneath — the hidden foundation fails. The branches wither above — what is visible fails. There is no part of the tree that is not dying."
    },
    "17": {
      "L": "His memory perishes from the earth, and he has no name in the streets.",
      "M": "His memory vanishes from the land; he has no name in the open places.",
      "T": "Nothing survives him. No one will remember his name in the countryside, in the public places, in the streets of any city. The memory of him dissolves. He existed — and the world keeps no record of it."
    },
    "18": {
      "L": "He is pushed from light into darkness and expelled from the world.",
      "M": "He is driven from light into darkness and banished from the world.",
      "T": "Shoved out of the light into darkness. Expelled. Not dead in the ordinary sense — negated. Treated as if he never fully belonged among the living, and now removed from their number."
    },
    "19": {
      "L": "He has no offspring or descendant among his people, and no survivor in the place where he sojourned.",
      "M": "He has no offspring or descendants among his people, and no survivor where he once lived.",
      "T": "No one to carry his line. No children, no grandchildren, no living branch left. And in the place where he built his life — not even a remnant of what he built, not one survivor of his household. He ends without continuation."
    },
    "20": {
      "L": "Those who come after him are appalled at his day, and those who went before him are seized with horror.",
      "M": "Those who come after him are horrified by his fate; those who went before him are seized with dread.",
      "T": "His destruction is a spectacle of horror visible across time. Future generations look back at his fate and are appalled. The older generations who knew him and watched it happen are seized with dread. He has become a monument to ruin — visible from every direction."
    },
    "21": {
      "L": "Surely such are the dwellings of the ungodly, and this is the place of one who does not know God.",
      "M": "Surely such are the homes of the wicked, and this is the dwelling of the one who does not know God.",
      "T": "Bildad's conclusion — and the target is unmistakable: this is the fate of the wicked. This is what happens to the man who does not know God. Look at where you are, Job. Look at what surrounds you. Draw the obvious conclusion. We already have."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 16–18 written.')

if __name__ == '__main__':
    main()
