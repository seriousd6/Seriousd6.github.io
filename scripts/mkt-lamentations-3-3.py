"""
MKT Lamentations chapter 3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-lamentations-3-3.py

Translation decisions:

- H1397 (גֶּבֶר / geber): "man" in L/M. Geber denotes a strong man, a warrior — not the
  generic ʾādām. The poet identifies himself as one whose strength should be a given; its
  collapse is therefore doubly devastating. T surfaces this force in v.1.

- H3068 (יהוה): "LORD" in L/M (small caps convention). "Yahweh" in T where the covenant
  name's personal weight is the point: vv. 18, 21-26, 40, 55, 58-59, 61, 64, 66.
  Follows the LAM-1a decision: T uses "Yahweh" at intensity peaks of direct address and
  in the chesed passage (vv. 22-26) where the covenant name is essential to the argument.

- H136 (אֲדֹנָי / Adonai): "the Lord" (title) in all tiers — vv. 31, 36, 37, 58.
  Distinct from H3068; denotes sovereignty. Maintained from LAM-1a.

- H2617 (חֶסֶד / ḥesed): The pivotal word of v.22 and v.32. No single English word suffices.
  L: "steadfast love" (two-word compound preserving the covenantal weight).
  M: "steadfast love" (same — widely recognized in modern translation).
  T: "covenant faithfulness" in v.22 (covenant-loyalty dimension foregrounded);
  "steadfast love" in v.32 (compassionate dimension foregrounded). Both senses are real.

- H7356 (רַחֲמִים / raḥamim): "compassions" in L (plural of intensity preserved);
  "mercies" in M (standard English idiom); "tender mercies" in T to capture the Hebrew's
  bodily resonance — raḥamim is cognate with reḥem (womb); it is deep, visceral care.

- H530 (אֱמוּנָה / ʾemûnāh): "faithfulness" in all tiers. V.23: "great is your faithfulness"
  — the declaration stands as the counterweight to the despair of vv. 17-18. In T this
  is rendered with exclamation to preserve the rhetorical force.

- H6960 (קָוָה / qāwāh): "wait/hope" — vv. 24, 25, 26. In L: "will hope in him" / "wait";
  in M: "hope in him" / "wait for him" / "wait quietly." In T the nuance of active, patient
  expectation (not passive resignation) is surfaced.

- H5315 (נֶפֶשׁ / nephesh): "soul" in L (embodied self). In M/T: "soul" where it means the
  whole self; "life" where the physical survival dimension dominates (e.g., v.58 "redeemed
  my life"). No Greek immaterial soul imported.

- H5769 (עוֹלָם / ʿôlam): "forever/ever" — v.6 "those long dead" = lit. "those of ancient
  times"; v.31 "will not cast off forever." In T, both senses are honored: v.6 the ancient
  dead, v.31 the temporariness of rejection.

- Acrostic structure: Lamentations 3 is a triple acrostic — each of the 22 Hebrew letters
  governs three consecutive verses (aleph = vv. 1-3, beth = vv. 4-6, etc.), yielding 66
  verses total. This is not reproduced in English. The T tier honors poetic cadence and
  forward momentum but makes no attempt to replicate the alphabetic constraint.

- Speaker shifts: vv. 1-20 are individual lament (first person singular — the geber);
  vv. 21-39 are individual meditation/confession (I/my); vv. 40-47 shift to communal
  ("we/us/our") as the individual voice broadens to include the whole community;
  vv. 48-66 return to the individual voice for final petition. These shifts are preserved
  in all three tiers.

- Theological turning point (v.21): The Hebrew syntax of v.21 is significant: "This I call
  to my heart / therefore I will hope." The act of remembering is itself the turning point.
  T marks this transition with full force.

- Vv. 34-36 unit: These three verses form a single syntactic argument: "to crush prisoners...
  to deny justice... to subvert a man's cause — the Lord does not approve." They describe
  injustices that God does not sanction; the list ends with the Lord's negative verdict.
  L/M preserve the syntactic parallelism; T makes the argumentative structure explicit.

- Textual note on v.22: The Hebrew is disputed. The MT has "חֲדָשִׁים לַבְּקָרִים" (new
  every morning) in v.23, and v.22 asserts that it is because of Yahweh's chesed that
  "we have not been consumed" (negative: "tāmamnū" with negative). This is the standard
  reading. Some render v.22 as a statement of wonder: "Is it of the LORD's mercies that
  we are not consumed?" — treated as a rhetorical affirmation. All tiers follow the
  affirmative declarative reading (the most natural Hebrew reading).
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

LAMENTATIONS = {
  "3": {
    "1": {
      "L": "I am the man who has seen affliction by the rod of his wrath.",
      "M": "I am the man who has seen affliction under the rod of God's wrath.",
      "T": "I am the strong man — the warrior — and even I have been brought low by the rod of his fury."
    },
    "2": {
      "L": "He has led me and made me walk in darkness and not in light.",
      "M": "He has driven me and brought me into darkness, not light.",
      "T": "He led me — but into darkness, not daylight. Every step he guided brought me deeper into shadow."
    },
    "3": {
      "L": "Surely against me he turns his hand again and again all the day long.",
      "M": "He has turned his hand against me time after time, all day long.",
      "T": "Again and again, without pause, all day long — his hand turned against me."
    },
    "4": {
      "L": "He has made my flesh and my skin waste away; he has broken my bones.",
      "M": "He has worn away my flesh and skin; he has broken my bones.",
      "T": "My body wastes — skin, flesh, bone. He consumed me from the outside in and broke what remained."
    },
    "5": {
      "L": "He has built against me and surrounded me with poison and hardship.",
      "M": "He has besieged and encircled me with gall and tribulation.",
      "T": "He walled me in — surrounded me on every side with poison and suffering, so there was no way out and nothing sweet to breathe."
    },
    "6": {
      "L": "He has made me sit in darkness like those long dead.",
      "M": "He has made me dwell in darkness like those long dead.",
      "T": "He placed me in the kind of darkness that belongs only to the dead — the ancient, forgotten dead."
    },
    "7": {
      "L": "He has hedged me in so that I cannot get out; he has made my chains heavy.",
      "M": "He has walled me in so I cannot escape; he has made my chains heavy.",
      "T": "He built a wall around me so tight that no escape was possible. Then he made my chains heavier still."
    },
    "8": {
      "L": "Also when I cry out and call for help, he shuts out my prayer.",
      "M": "Even when I cry out and shout, he shuts out my prayer.",
      "T": "I cried. I shouted. He closed the door on my prayer. Not a word got through."
    },
    "9": {
      "L": "He has blocked my ways with hewn stones; he has made my paths crooked.",
      "M": "He has blocked my paths with cut stone; he has made my ways crooked.",
      "T": "He barricaded every road with huge hewn stones and twisted every path into a dead end. There was no way forward, no way straight."
    },
    "10": {
      "L": "He was to me like a bear lying in wait, like a lion in secret places.",
      "M": "He was like a bear lying in ambush, like a lion in hiding.",
      "T": "He was not a shepherd — he was a bear crouching in ambush, a lion lurking in the shadows, waiting."
    },
    "11": {
      "L": "He turned aside my ways and tore me to pieces; he has made me desolate.",
      "M": "He turned me off my path and tore me apart; he has left me desolate.",
      "T": "He diverted me from every path and then tore me apart. He left me in ruins — utterly desolate."
    },
    "12": {
      "L": "He bent his bow and set me as a mark for the arrow.",
      "M": "He bent his bow and set me as a target for his arrows.",
      "T": "He drew his bow. He set me up as the target. I was the thing he aimed at."
    },
    "13": {
      "L": "He drove into my kidneys the arrows of his quiver.",
      "M": "He shot the arrows of his quiver into my inmost being.",
      "T": "His arrows found my deepest part — driving into my innermost being, where a man's core is."
    },
    "14": {
      "L": "I have become a laughingstock to all my people, their taunt all the day long.",
      "M": "I have become a laughingstock to all my people, the object of their mockery all day long.",
      "T": "The people who were mine now mock me all day without stopping. I am their joke, their taunt-song."
    },
    "15": {
      "L": "He has filled me with bitterness; he has made me drunk with wormwood.",
      "M": "He has filled me with bitterness; he has satiated me with wormwood.",
      "T": "He poured bitterness into me until I could hold no more. He fed me wormwood until I was drunk on it."
    },
    "16": {
      "L": "He has also broken my teeth with gravel stones; he has covered me with ashes.",
      "M": "He ground my teeth with gravel and made me cower in ashes.",
      "T": "He pressed gravel into my mouth until my teeth broke. He buried me in ashes."
    },
    "17": {
      "L": "And you have removed my soul far from peace; I have forgotten what prosperity is.",
      "M": "My soul has been stripped of peace; I have forgotten what happiness is.",
      "T": "Peace has been ripped from me so completely that I have forgotten it was ever real. The very idea of well-being has grown foreign to me."
    },
    "18": {
      "L": "And I said, 'My strength has perished, and my hope from the LORD.'",
      "M": "And I said, 'My endurance has perished, and my hope from the LORD.'",
      "T": "And I said it out loud: 'Whatever strength I had is gone. Whatever hope I placed in Yahweh — that too is gone.'"
    },
    "19": {
      "L": "Remembering my affliction and my misery, the wormwood and the gall.",
      "M": "Remembering my affliction and my wandering, the wormwood and the gall.",
      "T": "I keep returning to it — the affliction, the homelessness, the bitter taste of wormwood and gall."
    },
    "20": {
      "L": "My soul has them still in remembrance and is bowed down within me.",
      "M": "My soul continually remembers it and sinks down within me.",
      "T": "My whole self keeps circling back to the memory, weighed down by it, unable to rise."
    },
    "21": {
      "L": "This I call to my heart, and therefore I have hope.",
      "M": "Yet this I call to mind, and therefore I have hope:",
      "T": "But then — this one thing I force myself to remember. And it is enough to give me hope."
    },
    "22": {
      "L": "The steadfast love of the LORD never ceases; his compassions never come to an end.",
      "M": "It is because of the LORD's steadfast love that we are not consumed, for his mercies never fail.",
      "T": "We are still alive — and the only reason is Yahweh's covenant faithfulness. His steadfast love does not stop. His mercies do not run out."
    },
    "23": {
      "L": "They are new every morning; great is your faithfulness.",
      "M": "They are new every morning. Great is your faithfulness!",
      "T": "Morning by morning they arrive, fresh. Great — immeasurably great — is your faithfulness."
    },
    "24": {
      "L": "The LORD is my portion, says my soul; therefore I will hope in him.",
      "M": "The LORD is my portion, says my soul; therefore I will hope in him.",
      "T": "The LORD himself is my inheritance — what else do I need? Therefore, my soul, keep hoping in him."
    },
    "25": {
      "L": "The LORD is good to those who wait for him, to the soul that seeks him.",
      "M": "The LORD is good to those who wait for him, to the soul that seeks him.",
      "T": "The LORD is good — genuinely, truly good — to those who wait on him, to those who keep seeking him out."
    },
    "26": {
      "L": "It is good that one should wait quietly and hope for the salvation of the LORD.",
      "M": "It is good for a person to wait quietly for the salvation of the LORD.",
      "T": "There is goodness in waiting quietly — in sitting still and trusting that the rescue only the LORD can bring will come."
    },
    "27": {
      "L": "It is good for a man that he bear the yoke in his youth.",
      "M": "It is good for a man to bear the yoke in his youth.",
      "T": "It is genuinely good for a man to shoulder a hard burden while he is young — better learned early than late."
    },
    "28": {
      "L": "Let him sit alone and keep silence when he has laid it upon him.",
      "M": "Let him sit alone and in silence when God has placed it on him.",
      "T": "Let him sit down in silence — alone, without protest — when God is the one who has assigned the burden."
    },
    "29": {
      "L": "Let him put his mouth in the dust — there may yet be hope.",
      "M": "Let him put his mouth in the dust — there may still be hope.",
      "T": "Let him press his face to the ground. Let him be humbled to the dust. Even there, hope may not be finished."
    },
    "30": {
      "L": "Let him give his cheek to the one who strikes him; let him be filled with reproach.",
      "M": "Let him offer his cheek to the one who strikes him and be filled with insults.",
      "T": "Let him turn his cheek toward the blow. Let him absorb the shame. This is the posture of a man who has entrusted his vindication to God."
    },
    "31": {
      "L": "For the Lord will not cast off forever.",
      "M": "For the Lord will not reject forever.",
      "T": "The Lord's rejection is not permanent. He does not abandon his people for ever."
    },
    "32": {
      "L": "But though he cause grief, he will have compassion according to the abundance of his steadfast love.",
      "M": "Though he causes grief, he will have compassion in accordance with the abundance of his steadfast love.",
      "T": "Even when he inflicts pain, his compassion waits on the other side — measured by the fullness of his covenant love, and that love is immense."
    },
    "33": {
      "L": "For he does not afflict from his heart nor grieve the children of men willingly.",
      "M": "For he does not willingly afflict or grieve the children of men.",
      "T": "God does not enjoy this. He does not take pleasure in human suffering. When he disciplines, it is not what he desires — it is what love requires."
    },
    "34": {
      "L": "To crush under foot all the prisoners of the earth,",
      "M": "To crush beneath his feet all the prisoners of the earth,",
      "T": "To trample prisoners into the earth —"
    },
    "35": {
      "L": "to turn aside the right of a man before the face of the Most High,",
      "M": "to deny a man his rights before the Most High —",
      "T": "to deny justice to a person before the Most High's own face —"
    },
    "36": {
      "L": "to subvert a man in his cause — the Lord does not approve these things.",
      "M": "to deprive a man of justice in his own case — the Lord does not approve of these things.",
      "T": "to corrupt a man's legal cause — these are things the Lord sees and does not sanction."
    },
    "37": {
      "L": "Who is it that speaks and it comes to pass, unless the Lord has commanded it?",
      "M": "Who has spoken and it came to pass, unless the Lord has commanded it?",
      "T": "Whose word can bring anything into being without the Lord's command? No one's."
    },
    "38": {
      "L": "Is it not from the mouth of the Most High that both good and bad proceed?",
      "M": "Is it not from the mouth of the Most High that both good and evil come?",
      "T": "Is it not from the Most High himself that both prosperity and calamity flow? There is no other source."
    },
    "39": {
      "L": "Why does a living man complain, a man about the punishment of his sins?",
      "M": "Why should a living man complain — about the punishment of his own sins?",
      "T": "Then why complain? You are still alive. A living man, being punished for his own sins — what basis does he have for grievance?"
    },
    "40": {
      "L": "Let us search and try our ways and return to the LORD.",
      "M": "Let us examine and test our ways and turn back to the LORD.",
      "T": "Let us stop and look inward — examine every road we have walked, every path we have chosen. Then let us turn back to the LORD."
    },
    "41": {
      "L": "Let us lift up our hearts together with our hands to God in the heavens.",
      "M": "Let us lift up our hearts and hands together to God in heaven.",
      "T": "Let us raise both heart and hands toward God in heaven — not just the gesture, but the whole self reaching up."
    },
    "42": {
      "L": "We have transgressed and rebelled; you have not forgiven.",
      "M": "We have transgressed and rebelled, and you have not forgiven.",
      "T": "We admit it: we rebelled. We broke covenant. And you have not forgiven — not yet. The sentence stands."
    },
    "43": {
      "L": "You have covered yourself with anger and pursued us; you have killed and not pitied.",
      "M": "You wrapped yourself in anger and pursued us; you killed without pity.",
      "T": "You wrapped yourself in fury and came after us. You killed, and showed no mercy in the killing."
    },
    "44": {
      "L": "You have covered yourself with a cloud so that no prayer can pass through.",
      "M": "You have veiled yourself in a cloud so that no prayer can pass through.",
      "T": "You pulled a cloud between yourself and us, so dense that our prayers could not find their way through to you."
    },
    "45": {
      "L": "You have made us scum and refuse among the peoples.",
      "M": "You have made us refuse and scum among the peoples.",
      "T": "You made us the lowest of the low — the refuse, the offscouring, what nations discard and despise."
    },
    "46": {
      "L": "All our enemies have opened their mouths against us.",
      "M": "All our enemies have opened wide their mouths against us.",
      "T": "Every enemy opens their mouth wide over us — ready to swallow, ready to consume."
    },
    "47": {
      "L": "Fear and a snare have come upon us, desolation and destruction.",
      "M": "Panic and pitfall have come upon us, devastation and destruction.",
      "T": "Terror comes first, then the trap; then devastation, then total ruin — all of it falling on us at once."
    },
    "48": {
      "L": "Rivers of water run down from my eyes for the destruction of the daughter of my people.",
      "M": "My eyes stream with rivers of tears because of the destruction of my people.",
      "T": "I cannot stop crying. My tears fall in rivers over the ruin of my people, the daughters of Zion."
    },
    "49": {
      "L": "My eye flows and does not cease, without any pause,",
      "M": "My eyes will keep flowing without ceasing, without rest,",
      "T": "The tears do not stop. There is no pause, no respite — only the endless flowing of grief,"
    },
    "50": {
      "L": "until the LORD looks down and sees from heaven.",
      "M": "until the LORD looks down from heaven and sees.",
      "T": "until the LORD himself looks down from heaven and takes notice."
    },
    "51": {
      "L": "My eye causes me grief because of all the daughters of my city.",
      "M": "My eyes bring pain to my heart because of all the daughters of my city.",
      "T": "What my eyes see pierces my heart — the fate of all Jerusalem's daughters written on every face."
    },
    "52": {
      "L": "My enemies chased me like a bird, without cause.",
      "M": "Those who are my enemies without cause hunted me like a bird.",
      "T": "They hunted me — enemies who had no real grievance against me — chasing me down like a trapped bird."
    },
    "53": {
      "L": "They cut off my life in the pit and cast a stone upon me.",
      "M": "They cut short my life in the pit and threw stones upon me.",
      "T": "They threw me into the pit alive and sealed it with stones. They meant for me to die there, in the dark, buried."
    },
    "54": {
      "L": "Waters flowed over my head; I said, 'I am cut off.'",
      "M": "Water closed over my head; I said, 'I am finished.'",
      "T": "The water rose over my head. I said it: 'I am finished. I am gone.'"
    },
    "55": {
      "L": "I called on your name, O LORD, out of the depths of the pit.",
      "M": "I called on your name, LORD, from the deepest pit.",
      "T": "From the lowest depth — from inside the pit where I thought I would die — I called out your name, Yahweh."
    },
    "56": {
      "L": "You heard my voice; do not hide your ear from my breathing, from my cry.",
      "M": "You heard my voice. Do not turn away your ear from my cry, from my breathing.",
      "T": "You heard me. Do not look away now. Do not shut out my cry — even my desperate, ragged breathing is a prayer to you."
    },
    "57": {
      "L": "You drew near on the day I called on you; you said, 'Do not fear.'",
      "M": "You drew near when I called on you; you said, 'Fear not.'",
      "T": "The very day I called, you came. You came close. And you spoke: 'Do not be afraid.'"
    },
    "58": {
      "L": "O Lord, you have pleaded the causes of my soul; you have redeemed my life.",
      "M": "Lord, you have taken up my case; you have redeemed my life.",
      "T": "Lord, you became my advocate. You took my case. You bought back my life when I could not buy it myself."
    },
    "59": {
      "L": "O LORD, you have seen my wrong; judge my cause.",
      "M": "LORD, you have seen the wrong done to me. Uphold my cause.",
      "T": "Yahweh, you have seen the injustice done against me. Now render judgment. Be my judge."
    },
    "60": {
      "L": "You have seen all their vengeance and all their schemes against me.",
      "M": "You have seen all their vengeance, all their plots against me.",
      "T": "You have seen their every act of revenge, every scheme they hatched against me. Nothing is hidden from you."
    },
    "61": {
      "L": "You have heard their reproach, O LORD, and all their schemes against me,",
      "M": "You have heard their taunts, LORD, all their scheming against me,",
      "T": "Yahweh, you have heard every taunt they threw at me, every conspiracy they formed. You have been present for all of it —"
    },
    "62": {
      "L": "the lips of those who rose against me and their schemes against me all the day.",
      "M": "the lips of my attackers and their scheming against me all day long.",
      "T": "all day long, their lips moving against me, their minds working up new plans to destroy me."
    },
    "63": {
      "L": "Behold their sitting down and their rising up; I am their mocking song.",
      "M": "Look at them — whether they sit or stand, I am the subject of their mockery.",
      "T": "Watch them. Whether sitting or rising, whether at rest or in motion — my suffering is their entertainment. I am their song, their joke."
    },
    "64": {
      "L": "You will render to them a recompense, O LORD, according to the work of their hands.",
      "M": "You will repay them, LORD, according to what their hands have done.",
      "T": "Repay them, Yahweh. Let their hands' work come back on them. Measure their recompense by exactly what they have done."
    },
    "65": {
      "L": "You will give them anguish of heart; your curse will be upon them.",
      "M": "Give them anguish of heart and your curse upon them.",
      "T": "Let the anguish they caused me settle in their own hearts. Let your curse — not mine — be what overtakes them."
    },
    "66": {
      "L": "You will pursue them in anger and destroy them from under your heavens, O LORD.",
      "M": "Pursue them in anger and destroy them from under your heavens, LORD.",
      "T": "Pursue them, Yahweh. Pursue them in fury and wipe them from the face of the earth — every one who stands under these heavens."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'lamentations')
        merge_tier(existing, LAMENTATIONS, tier_key)
        save(tier_dir, 'lamentations', existing)
    print('Lamentations 3 written.')

if __name__ == '__main__':
    main()
