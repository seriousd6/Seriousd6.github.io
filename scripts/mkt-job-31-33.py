"""
MKT Job chapters 31–33 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-31-33.py

=== Overview of this unit ===

Ch 31 — Job's Oath of Innocence (40 verses): The climax of Job's self-defense.
         A systematic negative confession — Job swears by God that he has not committed
         a catalogue of sins (sexual ethics, vv.1–12; social ethics, vv.13–23; religious
         ethics, vv.24–28; personal character, vv.29–34), then stamps it with his legal
         signature (vv.35–37), and closes with a land oath (vv.38–40a).
         Colophon: "The words of Job are ended" — the book's pivot point.

Ch 32 — Elihu's Introduction (22 verses): A new character enters. Elihu son of Barachel
         the Buzite has been silent because the three friends were older. When they fail
         to answer Job, his anger kindles. He defends his right to speak (Spirit > age),
         disowns the friends' arguments, and announces he is about to burst with words.
         His entry shifts the book's tone: from a failed three-voice dialectic to a single
         voice who claims better access to the truth — though he is right about some things
         and overconfident about others.

Ch 33 — Elihu Addresses Job (33 verses): Elihu quotes Job's own words back to him, then
         corrects Job's charge that God has gone hostile. His counter-thesis: God speaks
         through dreams and through suffering — channels Job has missed. He describes the
         full arc of divine pedagogy: dream → warning → illness → edge of death → mediator
         → ransom → restoration. This is the closest the book gets to a theodicy that
         takes suffering seriously as divine communication rather than punishment.

=== Contested-term decisions (carried forward from mkt-job-25-28.py) ===

H410  (אֵל, El): "God" in all tiers.
H433  (אֱלוֹהַּ, Eloah): "God" in all tiers (Job's preferred singular poetic form).
H7706 (שַׁדַּי, Shaddai): "the Almighty" in all tiers — retained across all Job scripts.
H3068 (יהוה): not present in these chapters (Job's poetic core avoids the name).
H136  (אֲדֹנָי, Adonai): not present in these chapters.

H1285 (בְּרִית, berit, 31:1): "covenant" in all tiers. The word is juridical and heavy —
      a formal oath-bound agreement. Not "promise" or "resolution." Job has made a legal
      compact with his own eyes. This is not mere self-discipline; it is covenant fidelity
      applied inward.

H7307 (רוּחַ, ruach):
      32:8  — "the spirit" / "breath of the Almighty" — divine animating breath giving
              understanding to humans; "Spirit" (capital S) in all tiers. The Almighty's
              breath is the direct source of understanding, contrasted with inherited wisdom.
      32:18 — "the spirit within me" — the same divine breath compelling Elihu; capital S.
      33:4  — "the Spirit of God" — capital S throughout; God's agency in making Elihu.

H5315 (נֶפֶשׁ, nefesh):
      31:30 — "his soul" in L; "his life" in M/T — the life God could withdraw.
      33:18 — "his soul" in L; "him" in M; "the person" in T — the embodied self pulled
              from the pit.
      33:22 — "his soul" in L; "his life" in M/T — near the destroyers.
      33:28 — "his soul" in L; "his life" in M/T.
      33:30 — same pattern.

H11   (אֲבַדּוֹן, Abaddon, 31:12): "Abaddon" in all tiers — the abyss of destruction;
      carried forward as a proper name. Not "destruction" alone.

H7585 (שְׁאוֹל, Sheol): Not explicitly used in these chapters; the parallel term in 33:22
      is H7845 (שַׁחַת, shachat, "pit") — rendered "pit" in all tiers throughout.

H121  (אָדָם, Adam, 31:33): Treated as a proper name — "like Adam" — rather than the
      generic "mankind." The comparison is to Adam hiding his transgression in the garden
      (Gen 3:8–10). This reading is widely supported (LXX, Peshitta, many modern commentators)
      and fits the text better than "as men do" (KJV tradition). Documented in T tier.

H7563 (רָשָׁע, rasha, 31:3): "wicked" / "workers of iniquity" in all tiers.

H2611 (חָנֵף, chaneph): not present in these chapters (it appeared in 27:8 as "godless").

H6030 (עָנָה, anah): "answer/respond" — standard rendering throughout.

H4941 (מִשְׁפָּט, mishpat, 31:11, 31:13): "judgment/case" — the legal register of the
      oath sections.

=== Aspect and tense notes ===

Ch.31: The oath structure uses conditional perfects (the "if" clauses) followed by
       jussive/optative forms for the consequences Job calls down on himself. In Hebrew
       the oath is saying "if any of these things are true, let the corresponding disaster
       fall on me." T should honour the cumulative, relentless weight of the oath — forty
       verses of stacked conditions, each clause adding another stone to the edifice.
       The colophon (v.40b) is the only prose sentence in the chapter and should feel
       conclusive and final.

Ch.32: vv.1–5 are prose narrative (past tense, third person). vv.6–22 switch to Elihu's
       direct speech in verse. The repeated self-references ("I said," "I waited," "I will
       speak") reflect the self-consciousness of a young man who knows he is out of protocol.
       T should register both his genuine insight (the Spirit argument, v.8) and his
       self-preoccupation (he mentions himself far more than any other speaker in Job).

Ch.33: Elihu quotes Job's own words in vv.9–11, which makes it important that those verses
       echo Job's earlier language. The dream-speech (vv.15–18) and the ransom theology
       (vv.23–28) are the theological heart of the chapter. T should give them weight without
       flattening them. The mediator figure in v.23 is one of the most theologically loaded
       verses in Job; it anticipates the mediator theme of Hebrews and Job 19:25–27. T notes
       the weight.

=== OT echo notes ===

31:33 — "like Adam": echoes Genesis 3:8–10. Adam's hiding is the archetype of covering
         sin. Job's oath that he has not done this is an implicit claim to have surpassed
         the Adamic failure.
31:38–40 — The land crying out recalls Cain's blood crying from the ground (Gen 4:10)
            and the prophetic tradition of land desecrated by injustice (Isa 5:8–10;
            Mic 2:1–2). T surfaces this.
33:23–24 — The mediator/ransom motif anticipates Job 19:25–27 (the redeemer/vindicator)
            and forms an early witness to the theology developed in Hebrews 9:12, 15.
            T notes this as anticipation without overclaiming.
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
  # ============================================================
  # Chapter 31 — Job's Oath of Innocence
  # ============================================================
  "31": {
    "1": {
      "L": "A covenant I made with mine eyes; and how then should I gaze upon a virgin?",
      "M": "I made a covenant with my eyes; how then could I look upon a young woman?",
      "T": "Job begins his great oath not with murder or theft but with the eye — the gate of desire. He has made a formal, legally binding agreement with his own sight: it will not fix itself on a young woman with desire. The covenant language is deliberate and heavy. This is not a casual resolution. It is an oath with the self as both party and witness."
    },
    "2": {
      "L": "For what is the portion of God from above, and the heritage of the Almighty from on high?",
      "M": "For what is the portion God assigns from above, the heritage the Almighty deals from on high?",
      "T": "The question beneath the oath: what does God allot to those who violate such covenants? What comes down from the heights? Job already knows the answer. He is not asking from ignorance; he is asking to show that he knows the stakes."
    },
    "3": {
      "L": "Is not destruction for the unjust and calamity for the workers of iniquity?",
      "M": "Is there not ruin for the unrighteous and disaster for those who work iniquity?",
      "T": "Yes. The theology is clear: destruction for the crooked, calamity for those who do evil. Job is not claiming ignorance of consequences. He is claiming innocence of the acts that would trigger them. He knows what the punishment is, and he is staking his life on the claim that he has not earned it."
    },
    "4": {
      "L": "Does not he see my ways and count all my steps?",
      "M": "Does he not see my ways and number all my steps?",
      "T": "And God sees everything. Job is not making this oath in secret. Every step he has taken is on record with the one who counts them. That is exactly why the oath is serious — and why it can be made honestly."
    },
    "5": {
      "L": "If I have walked in vanity, or my foot hath hastened unto deceit —",
      "M": "If I have walked in falsehood, or my foot has rushed toward deceit —",
      "T": "First condition: if his life has been built on emptiness — on appearances rather than truth, on the shadow of virtue rather than the substance —"
    },
    "6": {
      "L": "Let me be weighed in a just balance, that God may know mine integrity.",
      "M": "Let me be weighed in an honest balance, so that God may know my integrity.",
      "T": "Then: put him on the scales. Fair scales. Honest weights. Let God read the measurement. He will find what is there — integrity — not what the friends have projected onto him."
    },
    "7": {
      "L": "If my step hath turned aside from the way, or mine heart hath walked after mine eyes, or any blot hath cleaved to my hands —",
      "M": "If my step has turned from the right path, or my heart has followed my eyes, or any stain has clung to my hands —",
      "T": "Second condition: if his feet left the proper path, if his heart trailed after what his eyes wanted instead of what is right, if there is a single stain on his hands from anything that passed through them —"
    },
    "8": {
      "L": "Then let me sow and another eat, and let my offspring be rooted out.",
      "M": "Then let me plant and another harvest, and let my offspring be uprooted.",
      "T": "— then let him lose the fruit of his own work. Plant and another reaps. Family torn from the ground. Job is piling consequences on himself. He is not hedging."
    },
    "9": {
      "L": "If mine heart hath been enticed by a woman, or if I have lain in wait at my neighbour's door —",
      "M": "If my heart has been drawn away by a woman, or I have lurked at my neighbour's door —",
      "T": "Third condition: if desire for another man's wife has taken hold of his heart, if he has crouched near her door waiting —"
    },
    "10": {
      "L": "Then let my wife grind for another and let others bow down over her.",
      "M": "Then let my wife grind for another man, and let others lie with her.",
      "T": "— then let his own wife be given to another man's service and his bed. Job applies to himself the exact punishment that would fit the crime. The symmetry is brutal and deliberate."
    },
    "11": {
      "L": "For that would be a heinous crime, and an iniquity to be judged.",
      "M": "For that would be a shameful outrage and an iniquity deserving judgment.",
      "T": "Adultery is not a private failure that stays between the parties. It is a public crime — the kind that goes before judges, that collapses households, that the law was made to address. Job knows this and says it without softening."
    },
    "12": {
      "L": "For it is a fire that consumeth unto Abaddon and would root out all mine increase.",
      "M": "For it is a fire that burns all the way to Abaddon and would consume all my harvest.",
      "T": "The fire of adultery does not stop at the surface. It burns all the way to Abaddon — to the uttermost abyss of destruction — and roots out everything that grew from his work. Not just a household ruined. Everything."
    },
    "13": {
      "L": "If I have despised the cause of my manservant or of my maidservant when they contended with me —",
      "M": "If I have dismissed the complaint of my servant or my maidservant when they had a dispute with me —",
      "T": "The servants: if Job had turned away their grievance because he was the master and the law of power said he could. If their case had been worth less to him because of who they were —"
    },
    "14": {
      "L": "What then shall I do when God riseth up? And when he visiteth, what shall I answer him?",
      "M": "What could I do when God rises up? When he holds inquiry, what shall I answer him?",
      "T": "The reasoning Job gives himself: a servant who has a complaint against me is a human being standing before God as I am. God's court does not rank by social position. If I dismissed their case, God rises in his court and I have no answer."
    },
    "15": {
      "L": "Did not he that made me in the womb make him? And did not one fashion us in the womb?",
      "M": "Did not the one who made me in the womb make him too? Did not one God form us both in the womb?",
      "T": "The same hand that formed Job in the womb formed the servant. One maker. He does not distinguish by social rank in the work of making. The master's status is a social fact; the image of God is a deeper fact."
    },
    "16": {
      "L": "If I have withheld the poor from their desire, or have caused the eyes of the widow to fail —",
      "M": "If I have refused the poor what they needed, or caused the widow's eyes to fail from waiting —",
      "T": "And the vulnerable: if Job denied the poor what they asked for, if he made the widow wait until her hope wore out, if her eyes searched the horizon for help that never came because he did not send it —"
    },
    "17": {
      "L": "Or have eaten my morsel alone, and the fatherless hath not eaten thereof —",
      "M": "Or if I ate my food alone and the fatherless ate nothing —",
      "T": "Or consumed a meal in private while a fatherless child went without — if he ate well and kept the door closed —"
    },
    "18": {
      "L": "For from my youth he grew up with me as with a father, and from my mother's womb I guided the widow.",
      "M": "For from my youth the fatherless grew up with me as with a father, and from birth I cared for the widow.",
      "T": "The reason he can make this oath: he has been doing this his entire life. The orphan grew up under his household as under a father's roof. And from birth — he takes it that far back — he has been a guide to the widow. This is not philanthropy. It is the practice of a lifetime."
    },
    "19": {
      "L": "If I have seen any perish for lack of clothing or the poor without covering —",
      "M": "If I have seen anyone dying from lack of clothing, or any poor person without covering —",
      "T": "If he ever saw someone going under from cold and turned away —"
    },
    "20": {
      "L": "If his loins have not blessed me, and if he was not warmed with the fleece of my sheep —",
      "M": "If he has not blessed me from his very body, and if the wool of my sheep has not kept him warm —",
      "T": "— when the poor man's own body has responded to Job's gift with gratitude, when Job's own wool reached him and kept him alive. This is not charity at a distance. The warmth is physical and the blessing is personal."
    },
    "21": {
      "L": "If I have lifted up my hand against the fatherless when I saw my help in the gate —",
      "M": "If I have raised my hand against the fatherless when I had allies at the city gate —",
      "T": "Or if Job ever used his social power — his supporters in the gate, his influence in the legal assembly — to harm a child who had no defenders. The gate was where cases were heard and where the powerful operated. He had the power. Did he misuse it?"
    },
    "22": {
      "L": "Then let mine arm fall from the shoulder blade and mine arm be broken at the elbow.",
      "M": "Then let my arm fall from its socket and my arm be broken from the elbow.",
      "T": "Then let the arm that did it go. The limb that raised against a fatherless child — let it fall. The punishment is proportionate and precise. He is not speaking in generalities; he is naming the body part that would have committed the crime."
    },
    "23": {
      "L": "For the destruction of God is a terror to me, and by reason of his highness I could not endure.",
      "M": "For the destruction God sends is a terror to me; before his majesty I cannot hold my ground.",
      "T": "The fear behind the oath. Job is genuinely afraid of God — not in the formal, professional sense, but in the personal sense of a man who knows he stands before the one whose highness cannot be measured. That fear is what makes the oath real."
    },
    "24": {
      "L": "If I have made gold my hope or said to fine gold, Thou art my confidence —",
      "M": "If I have made gold my hope or called pure gold my security —",
      "T": "Moving from social ethics to religious: if Job's trust was located in wealth. If he treated gold as his foundation — his god, his refuge, the place where his security lived —"
    },
    "25": {
      "L": "If I rejoiced because my wealth was great and because mine hand had gotten much —",
      "M": "If I rejoiced that my wealth was great or that my hand had gained much —",
      "T": "Or if the accumulation itself was the joy. If what satisfied him was watching the pile grow, if the getting was the meaning —"
    },
    "26": {
      "L": "If I beheld the sun when it shone or the moon walking in brightness —",
      "M": "If I gazed at the sun in its brilliance or the moon as it moved in splendor —",
      "T": "Or the sun. Or the moon — the great celestial objects that the ancient world venerated. If Job looked at them and felt the pull of worship —"
    },
    "27": {
      "L": "And my heart was secretly enticed and my mouth hath kissed my hand —",
      "M": "And my heart was secretly seduced, and my hand was kissed toward them —",
      "T": "The gesture of worship: the hand kissed and extended toward the divine object. If his heart was drawn toward it privately, quietly, away from scrutiny — the kind of religious drift that happens in secret among those with enough social standing to practice it discreetly —"
    },
    "28": {
      "L": "This also were an iniquity to be judged, for I should have denied the God who is above.",
      "M": "This too would be an iniquity deserving judgment, for I would have denied the God above.",
      "T": "That act of worship would not be a preference; it would be a denial. To worship the sun or moon is to replace the God who made them. That is apostasy, and in the covenant framework it carries the weight of death."
    },
    "29": {
      "L": "If I rejoiced at the destruction of him who hated me or exulted when evil found him —",
      "M": "If I rejoiced when my enemy was ruined, or exulted when disaster found him —",
      "T": "The enemies: if Job took private pleasure in an enemy's downfall. The human reflex — that quiet satisfaction when someone who wronged you suffers — Job is swearing against it. Not just the action, but the feeling."
    },
    "30": {
      "L": "Neither have I allowed my mouth to sin by asking a curse upon his soul —",
      "M": "I have not let my mouth sin by calling down a curse on his life —",
      "T": "He has not even invoked divine wrath against those who hated him. The mouth — the instrument of blessing and cursing — has not been turned against his enemies. That restraint is itself a kind of moral achievement, because the mouth wants to."
    },
    "31": {
      "L": "If the men of my household said not, Who is there that hath not been satisfied with his meat? —",
      "M": "If the men of my household have not said, 'Who has not been filled with his food?' —",
      "T": "Even the household's testimony is brought in. What do the people inside Job's walls say? Not 'we have not been fed' but the opposite: who among them has not been satisfied at his table? The household itself is a witness."
    },
    "32": {
      "L": "The stranger did not lodge in the street; I opened my doors to the traveller.",
      "M": "No stranger had to sleep in the street; I opened my doors to the traveller.",
      "T": "And the stranger on the road. No one slept in the open because Job's doors were closed. The ancient virtue of hospitality at its fullest: not managing the list of approved guests, but making the road safe for anyone who passed."
    },
    "33": {
      "L": "If I have covered my transgressions as Adam, by hiding mine iniquity in my bosom —",
      "M": "If I have hidden my transgressions like Adam, concealing my iniquity in my heart —",
      "T": "The reference is to Adam hiding himself in the garden after his transgression — the archetype of concealed guilt. Job swears he has not done this. He has brought his life out into the open, submitted it to examination. He is making the opposite move from Adam."
    },
    "34": {
      "L": "Because I feared the great multitude and the contempt of families terrified me, so that I kept silence and did not go out of the door —",
      "M": "Because I feared the crowd and the contempt of families terrified me, and so I kept silent and did not go out the door —",
      "T": "The social pressure that silences the innocent: the crowd's judgment, the contempt of neighbors, the weight of what everyone thinks. Job is saying he never gave in to it. He did not stay quiet to preserve his standing. He never hid behind closed doors to avoid the public verdict."
    },
    "35": {
      "L": "Oh that one would hear me! Behold, my mark — let the Almighty answer me; and that mine adversary had written a book!",
      "M": "O that someone would hear me! Here is my signature — let the Almighty answer me! O that my accuser had written out his charges!",
      "T": "This is the pivot of the entire oath. Job has finished his negative confession — forty verses of stacked conditions, the complete presentation of his life before the divine court. Now he stamps it. 'Here is my signature. This is my legal brief. Let the Almighty respond to it.' And he wants the charges in writing — he wants to know exactly what he is accused of. This is Job at his most legally defiant and his most personally desperate at the same instant."
    },
    "36": {
      "L": "Surely I would carry it upon my shoulder and bind it as a crown upon my head.",
      "M": "Surely I would carry it on my shoulder and wear it as a crown on my head.",
      "T": "If God wrote the charges and delivered them, Job says he would wear them — not as a condemned man being led to trial, but as a man who has been taken seriously enough to be formally charged. The indictment itself would be the crown: proof that he had stood his ground."
    },
    "37": {
      "L": "I would declare unto him the number of my steps; as a prince I would approach him.",
      "M": "I would give him an account of all my steps; I would approach him like a prince.",
      "T": "He would not slink in as a guilty man. He would walk toward God as a prince approaches a king — with dignity, with a complete account, with nothing hidden. Every step, every decision, every day. Let it be examined."
    },
    "38": {
      "L": "If my land crieth out against me and its furrows weep together —",
      "M": "If my land has cried out against me and its furrows have wept —",
      "T": "Even the land is called as a witness. The earth has memory. It responds to what is done on it, and the prophets know that blood soaks in and cries out (Gen 4:10). Has Job's land complained about its master?"
    },
    "39": {
      "L": "If I have eaten its fruits without payment or have caused the owners thereof to lose their life —",
      "M": "If I have eaten its produce without paying, or stripped the life from its owners —",
      "T": "If he took the harvest without paying, or drove out those who owned the land — the precise crime the prophets condemn, the accumulation of land by force or fraud (Isa 5:8; Mic 2:2). Job says: not this."
    },
    "40": {
      "L": "Let thistles grow instead of wheat and weeds instead of barley. The words of Job are ended.",
      "M": "Then let thistles grow instead of wheat and weeds instead of barley. The words of Job are ended.",
      "T": "The final curse on himself: if any of it is true, let the ground turn against him. Wheat becomes thistles, barley becomes weeds — the curse of Genesis 3 falls on the soil that fed a dishonest man.\n\nThe words of Job are ended. After the great oath, after the complete presentation of his life before the divine court, Job falls silent. He has nothing more to say to his friends. He has said everything. He waits."
    }
  },

  # ============================================================
  # Chapter 32 — Elihu's Introduction
  # ============================================================
  "32": {
    "1": {
      "L": "So these three men ceased to answer Job because he was righteous in his own eyes.",
      "M": "So these three men stopped answering Job, because he was righteous in his own eyes.",
      "T": "The friends stop. Job has outlasted every argument they had. He remained righteous in his own judgment and they could not shake it. They have nothing left to say."
    },
    "2": {
      "L": "Then was the anger of Elihu the son of Barachel the Buzite, of the family of Ram, kindled; against Job his anger was kindled because he justified himself rather than God.",
      "M": "Then the anger of Elihu son of Barachel the Buzite, of the clan of Ram, burned — against Job, because he declared himself righteous rather than God.",
      "T": "Into the silence steps Elihu — young, full of anger, full of himself. His genealogy is given in detail, perhaps because he has no authority from age and must establish it by lineage. His anger burns against Job on one count: Job has been making himself righteous at God's expense."
    },
    "3": {
      "L": "Also against his three friends was his anger kindled because they had found no answer and yet had condemned Job.",
      "M": "He was also angry with his three friends because they had found no answer and yet had condemned Job.",
      "T": "And against the three friends on a different count: they ran out of arguments and then condemned Job anyway — which is a special kind of injustice. They could not refute him, so they implied his guilt by going silent. Elihu sees through that."
    },
    "4": {
      "L": "Now Elihu had waited to speak with Job because they were older than he.",
      "M": "Elihu had waited to speak with Job because the others were older than he was.",
      "T": "He has been there the whole time. Silent — not because he agreed, but because the protocol of age demanded it. The older men spoke first. He has been listening and restraining himself through all of it."
    },
    "5": {
      "L": "When Elihu saw that there was no answer in the mouth of these three men, his anger was kindled.",
      "M": "When Elihu saw that the three men had no answer, his anger was aroused.",
      "T": "Watching them fall silent — seeing the great case just end without resolution, without justice for Job or for God — was too much. The restraint broke."
    },
    "6": {
      "L": "And Elihu the son of Barachel the Buzite answered and said: I am young and ye are aged; therefore I was afraid and durst not declare to you mine opinion.",
      "M": "Then Elihu son of Barachel the Buzite answered: I am young and you are old; that is why I was afraid and held back from telling you what I think.",
      "T": "Elihu begins. He acknowledges the protocol he is about to break: young man, old men, and the expectation is that the young listen. He was afraid. He held back. There is something genuine in this admission, even if what follows becomes increasingly confident."
    },
    "7": {
      "L": "I said: Days should speak, and multitude of years should teach wisdom.",
      "M": "I thought, 'Let the aged speak; let many years teach wisdom.'",
      "T": "He thought what everyone thinks: years accumulate into wisdom. Age speaks, experience teaches. The received understanding of how knowledge is transmitted — from elder to younger, from many seasons to few."
    },
    "8": {
      "L": "But there is a spirit in man, and the breath of the Almighty giveth them understanding.",
      "M": "But it is the Spirit in a person — the breath of the Almighty — that gives them understanding.",
      "T": "But this is incomplete. The Spirit in human beings — the Almighty's own breath — is what gives understanding. And Spirit is not distributed by seniority. The breath of God does not check credentials before it illuminates a mind."
    },
    "9": {
      "L": "The great are not always wise; neither do the aged understand judgment.",
      "M": "It is not the great who are always wise, nor the aged who always understand what is right.",
      "T": "The principle that follows: greatness and age do not automatically produce wisdom. The three elders in front of him have failed to understand the case. Youth does not disqualify; seniority does not guarantee."
    },
    "10": {
      "L": "Therefore I said: Hearken to me; I also will declare mine opinion.",
      "M": "Therefore I say: Listen to me; I too will express what I think.",
      "T": "So Elihu speaks. Not only because the Spirit compels him, but because the alternative — the great case of Job vs. God left unresolved in silence — is worse than the protocol he is breaking."
    },
    "11": {
      "L": "Behold, I waited for your words; I gave ear to your reasons whilst ye searched out what to say.",
      "M": "I waited for your words; I listened carefully to your arguments while you searched for what to say.",
      "T": "He catalogues his waiting. He gave them full attention — not dismissively, carefully — while they worked through their arguments, their silences, their searches for what to say next."
    },
    "12": {
      "L": "Yea, I attended unto you and behold, there was none of you that convinced Job or that answered his words.",
      "M": "I listened carefully to all of you, and not one of you has refuted Job or answered what he said.",
      "T": "And the verdict: no one refuted him. No one answered Job's words. He is still standing after everything the three friends fired at him. Between them they could not place a single argument that held."
    },
    "13": {
      "L": "Lest ye say: We have found wisdom — God shall vanquish him, not man.",
      "M": "Do not say, 'We have found wisdom; let God deal with him, not us.'",
      "T": "He heads off their exit. 'God will handle it' is not a conclusion; it is a retreat. You cannot declare the case finished and hand it to heaven simply because you ran out of arguments. That is not finding wisdom. That is losing the argument and refusing to say so."
    },
    "14": {
      "L": "Now he hath not directed words against me, and I will not answer him with your speeches.",
      "M": "He has not directed his argument against me, and I will not reply to him with your kind of arguments.",
      "T": "Elihu has an advantage: Job has not been arguing against him. He enters the exchange clean, without the history the three friends carry, without their accumulated failures. He will not use their weapons. He has something different."
    },
    "15": {
      "L": "They were amazed; they answered no more; words left them.",
      "M": "They are astonished; they say nothing more; words have left them.",
      "T": "The three friends: standing there, astonished. Perhaps by Job. Perhaps by Elihu arriving in the silence. Perhaps simply by the situation, which has exceeded every category they brought to it."
    },
    "16": {
      "L": "When I waited and they did not speak, but stood still and answered no more —",
      "M": "I waited, but they did not speak; they stood there and answered no more.",
      "T": "He waited for them. They were done. They stood in the open space between arguments, having emptied themselves, with nothing left to place in the gap."
    },
    "17": {
      "L": "I said: I will also answer my part; I also will declare mine opinion.",
      "M": "Then I said, 'I too will give my answer; I too will state what I think.'",
      "T": "And so he answers. It is his turn now. He has been thinking about this for a long time."
    },
    "18": {
      "L": "For I am full of words; the Spirit within me constraineth me.",
      "M": "For I am full of words; the Spirit within me urges me on.",
      "T": "He cannot stay silent any longer. The words have filled him — the Spirit in him pushing from inside like something that needs to get out. He is not performing urgency. He is reporting it."
    },
    "19": {
      "L": "Behold, my belly is as wine with no vent; it is ready to burst like new wineskins.",
      "M": "My belly is like wine with no outlet — like new wineskins about to burst.",
      "T": "New wine in a sealed skin: the fermentation active, the pressure building, the skin at the point of rupture. That is what it feels like inside him. He is not exaggerating for effect. This is the physical experience of someone with something urgent to say and nowhere yet to say it."
    },
    "20": {
      "L": "I will speak that I may find relief; I will open my lips and answer.",
      "M": "I will speak and find relief; I will open my lips and answer.",
      "T": "Speaking will be release — for him, not only for his audience. He is not pretending this is pure service. It is also personal necessity. He needs to say this."
    },
    "21": {
      "L": "Let me not, I pray, accept any man's person, nor give flattering titles unto any man.",
      "M": "I will show partiality to no one, nor will I flatter anyone.",
      "T": "His commitment: no favoritism, no flattery. He will not manage the audience by giving people the status they want. He is not going to tell Job what Job wants to hear, or tell the friends what the friends want to hear."
    },
    "22": {
      "L": "For I know not how to give flattering titles; in so doing my Maker would soon take me away.",
      "M": "For I do not know how to flatter; if I did, my Maker would soon remove me.",
      "T": "He cannot flatter — and beyond capability, it would cost him his life. If he shaped his words to please rather than to be true, God would take him away. The accountability is real and he takes it seriously. This is one of the more credible things Elihu says about himself."
    }
  },

  # ============================================================
  # Chapter 33 — Elihu Addresses Job
  # ============================================================
  "33": {
    "1": {
      "L": "Wherefore, Job, I pray thee, hear my speeches and hearken to all my words.",
      "M": "But now, Job, hear my words and listen to everything I have to say.",
      "T": "Elihu turns directly to Job. The others addressed him too, but with the accumulated weight of failed arguments. Elihu comes in as a peer — someone who believes he has something genuinely new to offer."
    },
    "2": {
      "L": "Behold now, I have opened my mouth; my tongue hath spoken in my mouth.",
      "M": "See now, I have opened my mouth; my tongue speaks within my mouth.",
      "T": "He draws attention to the act of speaking. In the context of Job's long, waiting silence — and the friends' exhausted quiet — the opening of a new mouth feels significant. Words are happening. Listen."
    },
    "3": {
      "L": "My words come from the uprightness of my heart, and my lips speak knowledge clearly.",
      "M": "My words come from an upright heart; my lips speak what I know sincerely.",
      "T": "Not wisdom inherited from tradition, not authority borrowed from age — but what his heart has found to be straight. And he will speak it without riddle, without the oblique accusations the three friends preferred. Directly."
    },
    "4": {
      "L": "The Spirit of God hath made me, and the breath of the Almighty hath given me life.",
      "M": "The Spirit of God has made me, and the breath of the Almighty gives me life.",
      "T": "Elihu establishes common ground: the same Spirit and the same Almighty-breath that Job speaks of is what gave Elihu life too. He is not positioning himself above Job. He is standing beside him, both of them creatures of the same maker."
    },
    "5": {
      "L": "If thou canst answer me, set thy words in order before me, stand up.",
      "M": "If you can answer me, set your words in order before me and take your stand.",
      "T": "An invitation with an edge. If Job has an answer to what Elihu is about to say, let him prepare it now. Stand up. Arrange the case. Elihu is not afraid of a response. He is inviting one."
    },
    "6": {
      "L": "Behold, I am in God's place as thou didst wish; I also was formed from clay.",
      "M": "See, I stand before God on your behalf as you wished; I too was formed from clay.",
      "T": "Job wanted a mediator — someone who could stand between him and God without being God himself, someone who would not crush him simply by proximity. Elihu says: I am that person. Not God, but made of the same clay as Job. A human representative."
    },
    "7": {
      "L": "Behold, my terror shall not make thee afraid, nor shall my hand be heavy upon thee.",
      "M": "My dread will not terrify you, nor will my pressure be heavy upon you.",
      "T": "He is not what Job feared God would be: overwhelming, crushing, too great to approach. He will not press Job down by sheer force of authority. He will simply speak."
    },
    "8": {
      "L": "Surely thou hast spoken in mine hearing, and I have heard the voice of thy words:",
      "M": "You have spoken in my hearing, and I have heard the words you said:",
      "T": "I was there. I listened. Everything Job said in his long defense — Elihu was in earshot through all of it. He is not working from hearsay."
    },
    "9": {
      "L": "I am clean, without transgression; I am innocent and there is no iniquity in me.",
      "M": "You said: 'I am clean, without transgression; I am innocent and there is no iniquity in me.'",
      "T": "Here is what Job said — Elihu quotes him back. 'I am clean. No transgression. No iniquity.' These are Job's own words from his great oath. Elihu has been paying close attention."
    },
    "10": {
      "L": "Behold, he findeth occasions against me; he counteth me as his enemy.",
      "M": "But you also said: 'He finds grievances against me; he regards me as his enemy.'",
      "T": "And also this: God is looking for pretexts to accuse Job, treating him like an adversary. Elihu is assembling Job's case as Job actually made it — accurately — before he begins to answer it."
    },
    "11": {
      "L": "He putteth my feet in the stocks; he marketh all my paths.",
      "M": "He puts my feet in stocks; he watches all my paths.",
      "T": "'He has imprisoned my feet, tracked every move.' Elihu repeats Job's own language back to him. The charge is on the record. Now he will respond to it."
    },
    "12": {
      "L": "Behold, in this thou art not just; I will answer thee: God is greater than man.",
      "M": "But in this I tell you plainly that you are wrong: God is greater than any human being.",
      "T": "And here is Elihu's answer: Job, in this you have overstepped. Not necessarily in your claim of innocence — Elihu does not directly contest that — but in your charge that God has become your enemy and owes you an explanation. God is greater than man. The category error is to treat God as a peer in a legal dispute."
    },
    "13": {
      "L": "Why dost thou strive against him? For he giveth not account of any of his matters.",
      "M": "Why do you argue against him? For he does not give account for any of his actions.",
      "T": "God is not obligated to explain himself to the creatures he made. The sovereign is not accountable to the subject in the framework Job is invoking. Job keeps demanding a hearing, but the entire premise of the demand is wrong: God does not answer to the court Job has tried to convene."
    },
    "14": {
      "L": "For God speaketh once, yea twice, yet man perceiveth it not.",
      "M": "For God speaks in one way and then another, though people do not notice.",
      "T": "The answer to Job's complaint that God has gone silent: God has been speaking. One way, then another. The problem is not divine silence; it is human inattention. Job has been so focused on demanding a specific kind of answer that he has missed the actual communication that was happening."
    },
    "15": {
      "L": "In a dream, in a vision of the night, when deep sleep falleth upon men, in slumberings upon the bed —",
      "M": "In a dream, in a nighttime vision, when deep sleep falls on people as they slumber on their beds —",
      "T": "The first channel: the dream. The night vision. The deep sleep that takes a person out of ordinary waking consciousness — that suspended state where the noise of the day cannot compete for attention."
    },
    "16": {
      "L": "Then he openeth the ears of men and sealeth their instruction —",
      "M": "He opens people's ears and confirms what he is teaching them —",
      "T": "God opens the ear in that state. Seals the instruction — marks it, delivers it in a way that cannot be mistaken for the ordinary chatter of a dreaming mind. Real communication through the channel of sleep."
    },
    "17": {
      "L": "That he may withdraw man from his purpose and conceal pride from man —",
      "M": "To turn them from their intended course and shield them from pride —",
      "T": "The purpose: to redirect, not to condemn. To pull the person back from a path that leads to destruction, and to conceal from them the pride that is already steering them off the edge. God speaks through dreams because he is trying to save people, not catch them."
    },
    "18": {
      "L": "He keepeth back his soul from the pit and his life from perishing by the sword.",
      "M": "He keeps him from the pit and his life from crossing into death.",
      "T": "The goal: keep the person alive. Keep them from the pit — not as an abstraction but as the specific disaster that pride or wrong direction would produce. God warns through the dream because he does not want them to die."
    },
    "19": {
      "L": "He is chastened also with pain upon his bed and with the strife of many of his bones —",
      "M": "He is also chastened with pain upon his bed, and with unending conflict in his bones —",
      "T": "The second channel: suffering. The pain that comes and does not leave. The bone-deep ache that is continuous and has no obvious source. This too is speech — a different register of the same divine communication."
    },
    "20": {
      "L": "So that his life abhorreth bread and his soul dainty meat.",
      "M": "So that he cannot eat bread and his appetite revolts against any food.",
      "T": "The body turns against itself. Food — the most basic comfort, the most ordinary good of living — becomes repulsive. Appetite disappears, pleasure disappears, the ordinary texture of being alive drains away. Job knows this from the inside."
    },
    "21": {
      "L": "His flesh is consumed so that it cannot be seen, and his bones that were not seen stick out.",
      "M": "His flesh wastes away until it is gone, and his bones that were hidden now protrude.",
      "T": "The body disappears — flesh consumed, bones that were hidden under muscle now visible, pushing through. Elihu is describing Job's condition back to him with clinical precision. This is not general theology. This is an account of what Job is living through."
    },
    "22": {
      "L": "Yea, his soul draweth near unto the pit and his life to the destroyers.",
      "M": "His life draws near the pit and his soul to the agents of death.",
      "T": "The edge is close. The pit is pulling. The destroyers — the agents of death that move at the boundary of human existence — are near. The person is almost gone."
    },
    "23": {
      "L": "If there be a messenger with him, an interpreter, one among a thousand, to declare to man his uprightness —",
      "M": "But if there is a messenger for him, a mediator — one in a thousand — who declares to the person what is right for them —",
      "T": "At that edge, at the threshold of death, something might happen. An interpreter appears: one person in a thousand who can stand between the dying person and God and speak what the right direction is. One mediator. One voice of grace in the moment of extremity. This is the figure that the whole book of Job has been longing for — and that the New Testament will name."
    },
    "24": {
      "L": "Then he is gracious unto him and saith: Deliver him from going down to the pit; I have found a ransom.",
      "M": "Then God is gracious to him and says: Spare him from going down to the pit; I have found a ransom.",
      "T": "And God responds to the mediator's intercession: 'Spare him. Don't let him fall. I have found a ransom.' The ransom — the price that lifts the sentence — comes from God's own finding. He provides what he also requires. The grace is complete in itself."
    },
    "25": {
      "L": "His flesh shall be fresher than a child's; he shall return to the days of his youth.",
      "M": "His flesh becomes fresher than a child's; he is restored to the days of his youth.",
      "T": "After the ransom: restoration. The body that was wasting returns. The old man gets young again — not metaphorically but in the sense of strength and vitality genuinely recovered. The reversal is as total as the fall was."
    },
    "26": {
      "L": "He shall pray unto God and he will be favourable unto him, and he shall see his face with joy; and he will restore to man his righteousness.",
      "M": "He prays to God and God accepts him; he sees his face with a shout of joy, and God restores his righteousness.",
      "T": "And prayer becomes real again — answered prayer, not cries into silence. He can see God's face, which suffering had obscured. Joy — the spontaneous, unforced kind. And his righteousness is restored: not declared from outside, but given back as if it had been in safekeeping all along."
    },
    "27": {
      "L": "He looketh upon men, and if any say: I have sinned and perverted what was right, and it profited me not —",
      "M": "He looks on people, and if any say: 'I sinned and bent what was right, and it brought me nothing good' —",
      "T": "The response that completes the restoration: honest acknowledgment. 'I sinned. I bent what should have been straight. And it got me nothing.' Not flattery, not performance — a plain, accurate statement about oneself. That is what opens the way back."
    },
    "28": {
      "L": "He will deliver his soul from going into the pit and his life shall see the light.",
      "M": "God will deliver his life from the pit, and his life will see the light.",
      "T": "The deliverance happens. The pit does not get him after all. The light — which had gone out in the darkness of suffering — returns. He sees it."
    },
    "29": {
      "L": "Lo, all these things God worketh oftentimes with man —",
      "M": "See, God does all these things — again and again — with a person —",
      "T": "And this is the pattern — not a one-time event. God works this way with human beings repeatedly: dream, suffering, mediator, ransom, restoration. The cycle can run more than once. God is patient with those who are not paying attention."
    },
    "30": {
      "L": "To bring back his soul from the pit, to be enlightened with the light of the living.",
      "M": "To bring his life back from the pit, that he might be lit by the light of the living.",
      "T": "The purpose behind every iteration of the cycle: pull the person back from the edge. Let them live. Give them the light of the living — not a diminished half-life of mere survival, but the genuine brightness of a life properly inhabited."
    },
    "31": {
      "L": "Mark well, O Job, hearken unto me; hold thy peace and I will speak.",
      "M": "Pay close attention, Job; listen to me; be silent and I will speak.",
      "T": "Elihu pauses and re-invites Job's attention. He is not done, and he wants Job to track with him — not simply to be talked at, but to follow the argument."
    },
    "32": {
      "L": "If thou hast any thing to say, answer me; speak, for I desire to justify thee.",
      "M": "If you have anything to say, answer me; speak up, for I want to see you vindicated.",
      "T": "Remarkably: Elihu says he wants Job justified. Unlike the three friends, whose entire project was to get Job to confess guilt he did not have, Elihu wants Job to have an answer that vindicates him. He is not trying to win. He is trying to find the truth."
    },
    "33": {
      "L": "If not, hearken unto me; hold thy peace and I will teach thee wisdom.",
      "M": "If not, listen to me; be silent, and I will teach you wisdom.",
      "T": "And if Job has nothing to say in response — if the case Elihu has made holds — then listen further. Elihu has more. Wisdom, which is what the whole book of Job is about, what the whole search of chapter 28 could not locate — that is what he is offering. The question is whether he can deliver it."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 31–33 written.')

if __name__ == '__main__':
    main()
