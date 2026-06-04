"""
MKT Job chapters 29–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-29-30.py

=== Structure ===

Chapters 29-30 are the hinge of Job's great final speech (chs 29-31). Chapter 29 is
his nostalgic idealization of the past — the days of God's blessing, social honor,
and deeds of justice. Chapter 30 is the brutal present — mockery by outcasts, God's
apparent enmity, physical suffering, and unanswered prayer. The contrast is designed
to be devastating: everything in ch 29 has an exact negative counterpart in ch 30.

=== Contested-term decisions ===

H433   (אֱלוֹהַּ, Eloah): "God" in all tiers (29:2, 29:4, 30:20-23) — consistent
       with prior Job scripts (chs 19-21). Eloah is the singular poetic form of Elohim,
       distinctive to the poetic books.

H7706  (שַׁדַּי, Shaddai): 29:5 — "Shaddai" (L) / "the Almighty" (M/T) — consistent
       across all prior Job scripts.

H5475  (סוֹד, sod): 29:4 — "friendship" (L/M) / "intimate presence" (T). Sod denotes
       the inner council of confidants, the circle of intimates (cf. Ps 25:14; Amos 3:7).
       KJV "secret" and ESV "friendship" are both defensible. The image is God's intimate
       counsel resting over Job's household like a covering presence. L/M use "friendship";
       T renders it as "intimate presence" to surface the covenantal-nearness dimension.

H5315  (נֶפֶשׁ, nefesh): 30:16, 30:25 — embodied self, not Greek immaterial soul.
       30:16 "my soul is poured out" = the whole person draining away from within.
       30:25 "was not my soul grieved" = visceral empathic suffering of the embodied self.
       "Soul" in L/M (traditional English convention); T makes the embodied dimension
       explicit: "the person I am" (30:16), "everything in me" (30:25).

H8577  (תַּנִּין, tannin): 30:29 — KJV renders "dragons" but the context (wilderness
       howling companions) points to jackals (cf. Mic 1:8, Isa 34:13 where the same
       term is paired with owls/ostriches in desolation scenes). Rendered "jackals"
       in all tiers. The accompanying "daughters of the ostrich" (H1323 H3284) = ostriches
       (or owls — the species is uncertain; "ostriches" follows ESV/NASB; rendered
       "wild birds" in T for sense-clarity).

H6664  (צֶדֶק, righteousness): 29:14 — "righteousness" in all tiers, as in prior
       chapters. This is Job's whole moral identity clothed on him.

H4941  (מִשְׁפָּט, mishpat): 29:14 — "justice" in all tiers; the legally structured,
       publicly applied standard — not merely personal "judgment." Both righteousness
       and justice together form the full garment of Job's public moral character.

H3820  (לֵב, lev): 29:13 — "heart" (all tiers). Here the widow's heart sings; lev is
       the center of volitional and emotional life, not merely sentiment.

H6963  (קוֹל, qol): 29:10 — "voice" rendered "noise/speech" depending on context.
       The nobles "held their peace" = their voice fell silent (kol + hashak).

=== Textual note on 30:24 ===

Verse 24 is notoriously difficult. The MT "Surely he will not stretch out his hand
against a heap of ruins, or in disaster cry for help from it?" (ESV) is often emended.
The more defensible reading — supported by LXX and context — is that Job is appealing
to a basic human instinct: even in ruins, a person reaches out; even in disaster, one
cries. This is exactly what Job is doing: making the cry that all suffering people make.
L/M render the text as a rhetorical appeal (reaching a hand out of ruins); T makes
the personal application explicit.

=== Aspect notes ===

Ch 29 uses predominantly waw-consecutive imperfects describing past events — the
narrative sequence of what used to be. These are rendered as simple past in L/M;
T uses the vivid-past or historic present to make the former glory live.

Ch 30 uses imperfects conveying ongoing present torment (vv 16-19, 27-30) alongside
perfects for completed reversals (vv 9-15). The contrast between "they used to honor
me" (perfect) and "they now torment me" (imperfect — still going) is significant.
T preserves this by using past tense for the social reversals and present progressive
for the ongoing suffering.

=== Poetic structure note ===

Both chapters are verse poetry. The T tier preserves line-cadence where the Hebrew
does (especially in ch 30's lament sections) and uses punctuation to mark
parallelistic structure rather than prose padding.
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
  "29": {
    "1": {
      "L": "Moreover Job continued his parable and said:",
      "M": "Job continued his discourse and said:",
      "T": "Job took up his speech once more:"
    },
    "2": {
      "L": "Oh that I were as in months past, as in the days when God preserved me!",
      "M": "Oh that I were as in the months gone by, in the days when God watched over me!",
      "T": "If only I could return — back to those months, back to the days when God kept watch over me and everything was good."
    },
    "3": {
      "L": "when his lamp shone upon my head, and by his light I walked through darkness;",
      "M": "when his lamp shone on my head and by his light I walked through darkness;",
      "T": "when his lamp burned above my head and I walked through every darkness without fear, because that light went before me;"
    },
    "4": {
      "L": "as I was in the days of my youth, when the friendship of God was over my tent;",
      "M": "as I was in the prime of life, when the friendship of God rested upon my tent;",
      "T": "the days of my prime — when God's intimate presence rested over everything I called home, a covering I did not have to ask for;"
    },
    "5": {
      "L": "when Shaddai was yet with me, and my children were around me;",
      "M": "when the Almighty was still with me, and my children were gathered around me;",
      "T": "when the Almighty walked beside me and my children were alive and gathered round my table;"
    },
    "6": {
      "L": "when I washed my steps with cream, and the rock poured out rivers of oil for me;",
      "M": "when I bathed my steps in cream and the rock poured out streams of oil for me;",
      "T": "when the land itself overflowed — every footstep on ground soaked in cream, every stone pouring oil in torrents. Abundance without effort; blessing without interruption."
    },
    "7": {
      "L": "when I went out to the gate of the city, when I took my seat in the square;",
      "M": "when I went out to the city gate and took my seat in the public square,",
      "T": "I would go to the city gate — the seat of justice, the place of elders — and take my place in the open square;"
    },
    "8": {
      "L": "the young men saw me and withdrew, and the aged rose and stood;",
      "M": "the young men saw me and stepped aside; the aged rose and stood to their feet.",
      "T": "the young men drew back at my approach; the elders rose from their seats. This was not ceremony — it was genuine deference, freely given."
    },
    "9": {
      "L": "the princes refrained from speaking and laid their hands on their mouths;",
      "M": "the princes stopped speaking and covered their mouths with their hands;",
      "T": "even the princes went silent. They put their hands to their mouths — whatever they had been saying seemed insufficient the moment I arrived."
    },
    "10": {
      "L": "the voice of the nobles was hushed, and their tongues cleaved to the roof of their mouths.",
      "M": "the voice of the nobles fell silent; their tongues stuck to the roof of their mouths.",
      "T": "The great men of the city — their voices stopped completely. Their tongues locked. My presence commanded that silence, and they gave it."
    },
    "11": {
      "L": "For the ear that heard me blessed me, and the eye that saw me bore witness for me;",
      "M": "For the ear that heard me called me blessed, and the eye that saw me testified for me;",
      "T": "Whoever heard me came away with a blessing on their lips. Whoever watched what I did — what they saw was evidence in my favor, not a case against me;"
    },
    "12": {
      "L": "because I delivered the poor who cried out, and the fatherless who had no one to help them.",
      "M": "for I rescued the poor when they cried for help, and the fatherless who had no one to help them.",
      "T": "because the poor cried and I answered. The fatherless had no one — and then they had me. That was the foundation of whatever honor I carried."
    },
    "13": {
      "L": "The blessing of him that was about to perish came upon me, and I caused the widow's heart to sing for joy.",
      "M": "The blessing of the one about to perish came to me, and I made the widow's heart sing for joy.",
      "T": "The dying man — the one who had no more strength to speak for himself — he blessed me before he went. The widow who had forgotten what joy felt like sang because of what I did for her. That was the accounting I lived by."
    },
    "14": {
      "L": "I clothed myself with righteousness and it clothed me; my justice was as a robe and a turban.",
      "M": "I put on righteousness and it clothed me; my justice was like a robe and a turban.",
      "T": "Righteousness was not a policy — it was clothing. I wore it; it wore me. My justice was both robe and turban — the full public identity, inside and out, visible from every angle."
    },
    "15": {
      "L": "I was eyes to the blind, and I was feet to the lame.",
      "M": "I was eyes for the blind and feet for the lame.",
      "T": "The blind had me for sight. The lame had me for motion. I was not merely sympathetic — I was functional to those who could not function."
    },
    "16": {
      "L": "I was a father to the poor, and the case of the one I did not know I searched out.",
      "M": "I was a father to the needy, and I investigated the case of the one I did not know.",
      "T": "The poor knew me as a father — not a patron with conditions attached, but a father who moved on their behalf. And even the complete stranger, whose case I had never heard — I went looking for it. I did not wait for them to reach me."
    },
    "17": {
      "L": "I broke the fangs of the wicked and wrested the prey from his teeth.",
      "M": "I broke the fangs of the wicked and forced the prey from his teeth.",
      "T": "When injustice was embedded — when the predator had the prey already between his teeth — I broke his hold. I pulled it back. That required force, and I used it without apology."
    },
    "18": {
      "L": "Then I said, 'I shall die in my own nest, and I will multiply my days like the sand.'",
      "M": "Then I said, 'I shall die in my own nest and multiply my days like the sand.'",
      "T": "And in all of that — the honor, the abundance, the deeds — I assumed it would last forever. 'I will die as I have lived,' I said to myself, 'at home in my nest, my days multiplying like grains of sand on the shore.' I was building toward a long and dignified death."
    },
    "19": {
      "L": "My root spread out to the waters, and the dew lay all night upon my branch;",
      "M": "My roots spread out to the waters, and the dew rested all night on my branches;",
      "T": "I imagined myself as a deep-rooted tree — roots reaching water that never runs dry, branches waking wet with dew every morning. Growth, nourishment, stability — always renewed, never failing."
    },
    "20": {
      "L": "my glory was ever fresh within me, and my bow was ever renewed in my hand.",
      "M": "my glory remained fresh within me, and my bow was always renewed in my hand.",
      "T": "My standing was not fading — it was being renewed. The bow in my hand — the strength to act, to protect, to strike when justice required — never grew slack. I expected it to stay that way."
    },
    "21": {
      "L": "Men listened to me and waited and kept silence for my counsel.",
      "M": "Men listened to me; they waited and held their silence for my counsel.",
      "T": "When I spoke, the room waited. Nobody interrupted. Nobody offered a competing word until I had finished. My counsel was what they had come to hear, and they knew it."
    },
    "22": {
      "L": "After my words they spoke no more; and my speech dropped gently upon them.",
      "M": "After my words they spoke no more; my speech fell upon them.",
      "T": "When I finished, nothing needed adding. The silence that followed was not awkward — it was the silence of people absorbing what they had just heard. My words fell on them like rain, slow and soaking."
    },
    "23": {
      "L": "They waited for me as for the rain, and they opened their mouths wide as for the spring rain.",
      "M": "They waited for me as for the rain and opened their mouths wide as for the spring rain.",
      "T": "They were thirsty for what I brought. The way a drought-cracked field opens to receive rain — that is how they received my words. I was the spring rains that ended the long dry wait."
    },
    "24": {
      "L": "If I smiled upon them, they could scarcely believe it; and the light of my face they did not let fall.",
      "M": "When I smiled at them they could hardly believe it; they did not let the light of my face fall.",
      "T": "A smile from me — they treasured it. They could barely believe it was meant for them. My approval was real currency; when I showed it, they held it close and did not waste a moment of it."
    },
    "25": {
      "L": "I chose the course for them and sat as chief; I dwelt as a king among his troops, as one who comforts the mourners.",
      "M": "I chose the course for them and sat as their head; I lived as a king among his troops, as one who comforts those who mourn.",
      "T": "I set the direction. I sat at the head. My place among them was what a king is among his soldiers — needed, relied upon, decisive. And when grief came to any of them, I sat with the mourners. Both command and compassion. That was what I was."
    }
  },
  "30": {
    "1": {
      "L": "But now those younger than I have me in derision, men whose fathers I would have refused to put with the dogs of my flock.",
      "M": "But now those younger than I hold me in contempt — men whose fathers I would have refused to place with the dogs of my flock.",
      "T": "And now. The reversal is total. Men younger than I am mock me openly. Their fathers — I would not have trusted those fathers to guard my sheepdogs, so low did they stand. And their sons mock me."
    },
    "2": {
      "L": "Yes, what is the strength of their hands to me, men in whom vigor has perished?",
      "M": "Indeed, what use is the strength of their hands to me — men whose vigor has already perished?",
      "T": "Even their help would be worth nothing — these are men who never had endurance even when they were young. Old age found nothing left to waste."
    },
    "3": {
      "L": "Through want and famine they were gaunt; they fled to the wilderness, desolate and waste.",
      "M": "Through want and famine they were barren; they fled into the desolate and waste wilderness.",
      "T": "Gnawed by hunger, hollowed by destitution — they had been driven to the wasteland, the howling emptiness beyond the edges of human life. Desolation was their home."
    },
    "4": {
      "L": "Who gathered saltbush among the shrubs, and the root of the broom plant was their food.",
      "M": "They gathered saltbush leaves from among the shrubs; the root of the broom plant was their food.",
      "T": "They ate what nothing else would touch — saltbush scraped from under thornbushes, broom roots pried from dry ground. This was their table. This was their feast."
    },
    "5": {
      "L": "They were driven out from among men; they were shouted after as after a thief.",
      "M": "They were driven out from human society; people shouted after them as after a thief.",
      "T": "Society had expelled them — not quietly. With shouts behind them, the way a crowd chases a thief through the street. Outcasts by public declaration. And these are my mockers."
    },
    "6": {
      "L": "They were made to dwell in the gullies of valleys, in holes of the earth, among the rocks.",
      "M": "They lived in gullies of the ravines, in holes of the earth, and among the rocks.",
      "T": "Cliffs and caves were their shelter. Not houses, not tents — the holes in the earth, the rocky outcroppings where nothing human lives by choice. That was where they lived. That is who mocks me."
    },
    "7": {
      "L": "Among the bushes they brayed; beneath the nettles they huddled together.",
      "M": "Among the bushes they cried out; beneath the nettles they gathered.",
      "T": "They made noise among the thornbushes — not speech, not song, but braying. And under the nettles they clustered together the way animals do for warmth. That was their community."
    },
    "8": {
      "L": "Children of senseless people, children of nameless men, they were beaten out of the land.",
      "M": "Children of fools, children of men without a name, they were flogged out of the land.",
      "T": "Sons of fools. Sons of men too disgraced to carry names worth carrying. Driven from the land with blows. These are the men who now make songs about me."
    },
    "9": {
      "L": "And now I have become their song; I am a byword to them.",
      "M": "And now I have become their song and their byword.",
      "T": "I am entertainment for these outcasts. The great man — the one who used to counsel princes, who used to be a father to the poor — I am the song they sing. Their stock example of downfall. Their byword."
    },
    "10": {
      "L": "They abhor me, they keep far from me, and do not hesitate to spit in my face.",
      "M": "They despise me and keep their distance; they do not hesitate to spit in my face.",
      "T": "Disgust — that is what I generate in them now. They back away and spit. In my face. Deliberate and public. Once I gave the widow reason to sing; now I give the gutter-born reason to spit."
    },
    "11": {
      "L": "Because he has loosed my cord and afflicted me, they have thrown off all restraint in my presence.",
      "M": "Because God has loosed my cord and afflicted me, they have cast aside all restraint in my presence.",
      "T": "God let the rein go — the restraint that once kept these people at bay from me. Once God stopped holding them back, every barrier that protected my dignity dissolved. They feel free to do anything."
    },
    "12": {
      "L": "On my right the rabble rises; they drive away my feet and build against me their roads of ruin.",
      "M": "On my right the mob rises up; they push aside my feet and build against me their roads of ruin.",
      "T": "They come at me from the right — the vulnerable flank. They shove my feet out from under me and build siege works to finish what God started. Their appetite for my destruction gives them organization."
    },
    "13": {
      "L": "They destroy my path; they advance my ruin; they have no one to help them — they need none.",
      "M": "They wreck my path; they advance my downfall; they need no one to help them.",
      "T": "Every possible way forward is ruined before I reach it. They press my destruction forward — not as a side effect of something else, but as a project they pursue. And they require no assistance. My weakness is sufficient."
    },
    "14": {
      "L": "They come in as through a wide breach; amid the crash they roll in.",
      "M": "They come in as through a wide breach; they rush in amid the ruin.",
      "T": "They pour in the way water pours through a broken wall — the moment the structure gives way, the flood follows. In the ruins of what was my life, they come. The collapse is their invitation."
    },
    "15": {
      "L": "Terrors are turned upon me; my dignity is swept away like the wind, and my welfare passes like a cloud.",
      "M": "Terrors are unleashed against me; my dignity is driven away like the wind, and my prosperity passes away like a cloud.",
      "T": "Terror after terror aimed at me. The honor I had — blown away, weightless as chaff in the wind. My well-being evaporated the way clouds dissolve: fast, complete, leaving no trace behind."
    },
    "16": {
      "L": "And now my soul is poured out within me; days of affliction grip me.",
      "M": "And now my soul is poured out within me; days of affliction have seized me.",
      "T": "The person I am — emptied out, poured from within like water from an overturned vessel. And the days of this affliction grip me like hands that will not let go."
    },
    "17": {
      "L": "At night my bones are pierced with pain, and the gnawing pain within me does not rest.",
      "M": "At night my bones are racked with pain, and the pain that gnaws at me never rests.",
      "T": "Night brings no relief. The bones ache as if something bores through them. The pain has its own relentless rhythm — it does not sleep when I try to. Darkness does not soften this."
    },
    "18": {
      "L": "With great force my garment is seized; it binds me like the collar of my coat.",
      "M": "With great force my clothing is seized by my disease; it binds me at the neck like the collar of my coat.",
      "T": "The disease has reshaped me so thoroughly that my own garment seizes and binds — it wraps around me at the collar like a noose. My body has become something strange even to its own clothes."
    },
    "19": {
      "L": "He has cast me into the mud, and I have become like dust and ashes.",
      "M": "He has thrown me into the mud; I have become like dust and ashes.",
      "T": "God threw me here. Into the mud. And what I have become — dust and ashes — is the image of total abasement, the most thoroughly undone a human being can be. He put me here."
    },
    "20": {
      "L": "I cry out to you and you do not answer; I stand up and you only look at me.",
      "M": "I cry to you but you do not answer; I stand, and you only stare at me.",
      "T": "I speak into the void and nothing comes back. I stand before God — upright, presenting myself — and he watches. Just watches. No word, no turn, no response. The most devastating silence I have ever experienced."
    },
    "21": {
      "L": "You have turned cruel to me; with the strength of your hand you press hard against me.",
      "M": "You have become cruel to me; with the power of your hand you oppose me.",
      "T": "What I have to say to God now — you have become my adversary. Not a distant God who simply ignores me, but an active one. Your strong hand is not lifted for me; it is pressed down against me."
    },
    "22": {
      "L": "You lift me up to the wind; you make me ride upon it, and you toss me in the storm.",
      "M": "You lift me up on the wind; you cause me to ride it and dissolve my substance.",
      "T": "You pick me up and hurl me into the wind — weightless, uncontrolled, at the mercy of what you set loose. You send me riding on something I cannot steer, and everything that was me — all substance, all stability — you dissolve it. Like a man taken apart."
    },
    "23": {
      "L": "For I know that you will bring me to death, and to the house appointed for all the living.",
      "M": "For I know you will bring me to death, to the house appointed for all the living.",
      "T": "I know where this ends. Death. The one house with an open door for everyone who has ever breathed. I am not surprised — I am saying it plainly: this is where you are taking me."
    },
    "24": {
      "L": "Yet does not one in a heap of ruins reach out his hand? Does a man not cry for help in his calamity?",
      "M": "Yet does not one in a heap of ruins reach out his hand? Does one not cry out in his disaster?",
      "T": "Even so — when a person is collapsing, buried under the rubble of their own ruin, the instinct is still to reach out a hand. Still to cry. This is that cry. This is that hand stretched into the dark."
    },
    "25": {
      "L": "Did I not weep for him whose day was hard? Was not my soul grieved for the poor?",
      "M": "Did I not weep for those in trouble? Was not my soul grieved for the poor?",
      "T": "I wept for the troubled — real tears, not gesture. Everything in me was wrung out with grief for the poor. And now I am the one who needs what I used to give, and it is not coming."
    },
    "26": {
      "L": "But when I looked for good, evil came; when I waited for the light, darkness came instead.",
      "M": "But when I looked for good, evil came; and when I waited for light, darkness came instead.",
      "T": "Every expectation reversed. I looked for good: evil arrived. I waited for light: the darkness came first. This is not coincidence — it is the shape of my disaster, exact and relentless."
    },
    "27": {
      "L": "My inner parts seethe and will not rest; days of affliction have come before me.",
      "M": "My inner parts churn and do not rest; days of affliction have overtaken me.",
      "T": "The churning inside me does not stop — the gut's physical revolt against what the mind cannot process. And the days of affliction outran me: they arrived before I was ready, before I had any defense prepared."
    },
    "28": {
      "L": "I go about in gloom without sunlight; I stand up in the assembly and cry out.",
      "M": "I walk in mourning without the sun; I stand up in the assembly and cry out.",
      "T": "I move through the world in mourning — not the ritual kind but the kind that precedes me everywhere I go. I stand in the public square — the very place where I once commanded silence — and cry out. The reversal is complete."
    },
    "29": {
      "L": "I have become a brother to jackals and a companion to ostriches.",
      "M": "I have become a brother to jackals and a companion to wild birds.",
      "T": "The creatures of desolation are my kindred now. Jackals and the wild birds of wasteland — the things that inhabit ruined places — these are my companions. I live where they live."
    },
    "30": {
      "L": "My skin turns black and peels from me, and my bones burn with fever.",
      "M": "My skin has turned black and peels away; my bones burn with fever.",
      "T": "The body reveals what the spirit suffers: blackened skin sloughing away, bones burning from within. This is not image — it is condition. Job's body is the visible sign of everything this chapter has said."
    },
    "31": {
      "L": "My harp has turned to mourning, and my flute to the voice of those who weep.",
      "M": "My harp has been turned to mourning and my flute to the sound of weeping.",
      "T": "Everything that once played for joy now plays for grief. The harp plays dirges. The flute has learned the sound of weeping. Chapter 29 opened with the memory of blessing; chapter 30 closes with the music of grief. The song has changed entirely."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 29–30 written.')

if __name__ == '__main__':
    main()
