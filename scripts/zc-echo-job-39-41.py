"""
Echo Layer — Job chapters 39–41
Run: python3 scripts/zc-echo-job-39-41.py

Key echo connections in this range:
- 39:1-4: God cares for wild births → Matt 10:29; Luke 12:24 (not one sparrow falls)
- 39:19-25: The war horse → Rev 19:11 (Christ on white horse); trumpet-battle → 1 Cor 15:52
- 39:27-30: Eagle on rocky heights, spot prey → Matt 24:28; Rev 4:7 (eagle face)
- 40:2: "Will a critic argue with the Almighty?" → Rom 9:20 (who are you to answer back?)
- 40:4: "I put my hand over my mouth" → Isa 6:5; Luke 5:8 (undone before holiness)
- 40:8: "condemn me so you can be righteous" → Rom 3:4; Phil 3:9 (righteousness from God)
- 40:12: "humble the proud" → Jas 4:6; Luke 1:51-52 (Magnificat)
- 41:1: "Can you pull Leviathan up with a hook?" → Isa 27:1; Rev 20:2 (dragon bound)
- 41:10-11: "who is able to stand before me?" → Rom 11:34-35; Ps 50:12
- 41:33-34: "king over all the proud" → Rev 13:4 (beast); contrast Rev 19:16 (Christ overcomes)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

JOB_ECHO_39_41 = {
  "39": {
    "1": [
      {"type": "allusion", "target": "Matt 10:29", "note": "&#8220;Do you know when the mountain goats give birth? Can you watch over the birth of the does?&#8221; — God&#8217;s speech to Job opens by pointing to the reproductive care of the wildest creatures as evidence of divine involvement in what humans never see; Matthew 10:29 expresses the same providential logic: &#8220;Are not two sparrows sold for a penny? Yet not one of them will fall to the ground outside your Father&#8217;s care.&#8221; The rhetorical question God asks Job (&#8220;do you know...?&#8221;) implies that God does know — the births Job cannot witness, God attends; the same care that superintends wild mountain births superintends human suffering that seems unseen"},
      {"type": "allusion", "target": "Luke 12:24", "note": "God&#8217;s detailed knowledge of wild animals&#8217; birth cycles — the months they carry young, the moment of delivery — is the OT basis for Jesus&#8217; argument in Luke 12:24: &#8220;Consider the ravens: they do not sow or reap, they have no storeroom or barn; yet God feeds them. How much more valuable you are than birds!&#8221;; the divine providential attention to wild creatures that the whirlwind speech uses to humble Job is repurposed by Jesus to comfort his disciples — the same evidence of God&#8217;s care that reduces Job to silence assures the disciples of their Father&#8217;s attention"}
    ],
    "5": [
      {"type": "allusion", "target": "Gal 5:1", "note": "&#8220;Who set the wild donkey free? Who opened the bonds of the onager?&#8221; — the wild donkey&#8217;s freedom, given by God as its native condition (<em>miḥôr-šilaḥtî</em> — &#8220;into the desert I freed it&#8221;), is a creature-specific type of the freedom that belongs to God&#8217;s gifts; Galatians 5:1: &#8220;It is for freedom that Christ has set us free. Stand firm, then, and do not let yourselves be burdened again by a yoke of slavery.&#8221; The wild donkey&#8217;s bond-breaking freedom is the creaturely emblem of what Christ accomplishes at the human level — not freedom from proper constraint but freedom from the yoke that was imposed by another"}
    ],
    "19": [
      {"type": "allusion", "target": "Rev 19:11", "note": "&#8220;Did you give the horse its might? Did you clothe its neck with a flowing mane?&#8221; — God&#8217;s portrait of the war horse — fearless, trumpet-excited, battle-hungry — is the OT image behind Revelation 19:11: &#8220;I saw heaven standing open and there before me was a white horse, whose rider is called Faithful and True. With justice he judges and makes war.&#8221; The horse that God describes in Job 39 as clothed by him with might is the horse that the victorious Christ rides at his return; the mane God gave (<em>raʿᵃmāh</em>) anticipates the armies following Christ &#8220;dressed in fine linen, white and clean, on white horses&#8221; (Rev 19:14)"}
    ],
    "25": [
      {"type": "allusion", "target": "1 Cor 15:52", "note": "&#8220;At each trumpet blast it cries out &#8216;Aha!&#8217; It scents the battle from far away — the roar of commanders and the war cry.&#8221; — the war horse&#8217;s excitement at the trumpet that cannot be restrained is the OT sensory image of the resurrection trumpet that 1 Corinthians 15:52 announces: &#8220;in a flash, in the twinkling of an eye, at the last trumpet. For the trumpet will sound, the dead will be raised imperishable, and we will be changed.&#8221; The charge at the trumpet that Job&#8217;s war horse cannot resist is the type of the irresistible summons that will call the dead to life at Christ&#8217;s return"}
    ],
    "27": [
      {"type": "allusion", "target": "Rev 4:7", "note": "&#8220;Does the eagle soar at your command and build its nest on the heights?... Its young ones drink blood; where the slain are, there the eagle is.&#8221; — the eagle with its long-range vision, nesting on inaccessible heights, drawn to the place of death, is the living creature whose face is that of an eagle in Revelation 4:7 (the four living creatures around the throne); and it is the eagle whose saying is quoted in Matthew 24:28 and Luke 17:37 — &#8220;wherever the corpse is, there the eagles will gather&#8221; — as the image of inescapable judgment gathering at the site of death; the eagle Job describes is the same creature that frames both the throne-room doxology and the eschatological warning"}
    ]
  },
  "40": {
    "2": [
      {"type": "allusion", "target": "Rom 9:20", "note": "&#8220;Will a critic argue with the Almighty? Let the one who accuses God answer him.&#8221; — God&#8217;s first challenge to Job after the whirlwind is the question that Paul echoes in Romans 9:20: &#8220;But who are you, O man, to answer back to God? Will what is molded say to its molder, &#8216;Why have you made me like this?&#8217;&#8221; (citing Isa 29:16); both texts use the radical asymmetry between Creator and creature to address the problem of theodicy — the creature&#8217;s moral challenge to the Creator&#8217;s justice; Paul&#8217;s point is not that God is unanswerable tyrant but that the framework for the question is always the creature&#8217;s, not the Creator&#8217;s"}
    ],
    "4": [
      {"type": "allusion", "target": "Isa 6:5", "note": "&#8220;I am of little account; what shall I say to you? I put my hand over my mouth.&#8221; — Job&#8217;s response to the divine theophany echoes the pattern of prophetic vision-encounters: Isaiah 6:5 (&#8220;Woe is me! I am ruined! For I am a man of unclean lips, and I live among a people of unclean lips, and my eyes have seen the King, the LORD Almighty&#8221;) and Peter in Luke 5:8 (&#8220;Go away from me, Lord; I am a sinful man!&#8221;); the hand over the mouth is the physical gesture of stunned inadequacy before divine presence — not merely an emotional reaction but a recognition that the complaint-posture Job has maintained is now impossible"},
      {"type": "allusion", "target": "Luke 5:8", "note": "&#8220;I put my hand over my mouth... I will not answer again&#8221; — Job&#8217;s silencing before the theophany is the wisdom-book parallel to Peter&#8217;s collapse before the miraculous catch: &#8220;depart from me, for I am a sinful man, O Lord&#8221; (Luke 5:8); both are the instinctive response of a human being who encounters the holy at close range — not guilt alone but the recognition that all prior claims to adequacy were spoken from a distance; the theophany resolves the argument not by answering Job&#8217;s questions but by transforming the one who asked them"}
    ],
    "8": [
      {"type": "allusion", "target": "Rom 3:4", "note": "&#8220;Would you discredit my justice? Would you condemn me so that you can be righteous?&#8221; — God&#8217;s challenge identifies the logical structure of the Friends&#8217; theodicy and Job&#8217;s counter-protests: both positions, pursued to their extreme, require either condemning God or condemning Job; Romans 3:4 states the same unavoidable conclusion: &#8220;let God be true though every man a liar, as it is written: &#8216;That you may be justified in your words, and prevail when you are judged&#8217;&#8221; (citing Ps 51:4); the righteousness of God is not secured by finding human beings guilty — it is intrinsic to who God is; Job&#8217;s accusation and the Friends&#8217; accusation are different error-forms of the same category mistake"}
    ],
    "12": [
      {"type": "allusion", "target": "Jas 4:6", "note": "&#8220;Look at every proud person and humble him; trample the wicked where they stand.&#8221; — God&#8217;s challenge to Job (can you do what I do with the proud?) articulates the divine attribute that James cites as grounds for human humility: &#8220;God opposes the proud but gives grace to the humble&#8221; (Jas 4:6, citing Prov 3:34); what God invites Job to try — the humbling of every proud person — is what only God can accomplish; the NT grounds this same principle in Christ&#8217;s own humiliation (Phil 2:5-8) as the pattern for those who want to share in the divine humbling of pride"},
      {"type": "allusion", "target": "Luke 1:51", "note": "&#8220;Look at every proud person and humble him&#8221; — God&#8217;s description of his own action against pride is the content of Mary&#8217;s Magnificat: &#8220;He has performed mighty deeds with his arm; he has scattered those who are proud in their inmost thoughts. He has brought down rulers from their thrones but has lifted up the humble&#8221; (Luke 1:51-52); the divine reversal of the proud that God describes to Job as his exclusive prerogative is what the Magnificat declares has been enacted in the incarnation — the child in Mary&#8217;s womb is the one who will accomplish what neither Job nor anyone else could"}
    ],
    "14": [
      {"type": "allusion", "target": "Phil 3:9", "note": "&#8220;Then I myself will acknowledge that your own right hand can give you victory.&#8221; — the conditional is rhetorically impossible: no human right hand can achieve the divine justice God describes in vv.11-13; the impossibility is the point; Philippians 3:9 is Paul&#8217;s answer to having spent his life trying to build the righteousness his right hand could achieve: &#8220;not having a righteousness of my own that comes from the law, but that which comes through faith in Christ — the righteousness that comes from God on the basis of faith&#8221;; Job&#8217;s encounter with the whirlwind produces the same recognition Paul articulates — no human right hand achieves salvation; it comes from God"}
    ],
    "15": [
      {"type": "allusion", "target": "Col 1:16", "note": "&#8220;Look at Behemoth, which I made just as I made you.&#8221; — the Creator&#8217;s claim on Behemoth — &#8220;which I made&#8221; — is the same claim that Colossians 1:16 extends to all created reality through Christ: &#8220;for in him all things were created: things in heaven and on earth, visible and invisible... all things have been created through him and for him&#8221;; the &#8220;I made&#8221; of the whirlwind speech is the Father&#8217;s claim; the NT attributes the same creative act to the Son — the Behemoth and the human being both exist through and for Christ"}
    ]
  },
  "41": {
    "1": [
      {"type": "allusion", "target": "Isa 27:1", "note": "&#8220;Can you pull Leviathan up with a hook, or hold down his tongue with a rope?&#8221; — God&#8217;s rhetorical challenge establishes Leviathan&#8217;s incomprehensibility and inaccessibility to human beings; Isaiah 27:1 announces what YHWH himself will do: &#8220;In that day, the LORD will punish with his sword — his fierce, great and powerful sword — Leviathan the gliding serpent, Leviathan the coiling serpent; he will slay the monster of the sea.&#8221; The Leviathan that no human can hook, YHWH himself will slay — what was impossible for Job becomes the promised eschatological act of divine judgment"},
      {"type": "allusion", "target": "Rev 20:2", "note": "&#8220;Can you pull Leviathan up with a hook?&#8221; — the Leviathan that no one can catch or bind becomes, in Revelation 20:2, the dragon that the angel binds: &#8220;He seized the dragon, that ancient serpent, who is the devil, or Satan, and bound him for a thousand years.&#8221; The binding that was impossible for any human — Leviathan with rope and hook — is accomplished by divine agency through the cross and resurrection; Christ&#8217;s defeat of the dragon is the eschatological answer to God&#8217;s whirlwind challenge"}
    ],
    "10": [
      {"type": "allusion", "target": "Rom 11:34", "note": "&#8220;No one is fierce enough to rouse him; who then is able to stand before me? Who has given me anything that I should owe him in return?&#8221; — the argument moves from Leviathan&#8217;s terrifying power to God&#8217;s absolute sovereignty: if no one can stand before Leviathan, then obviously no one can stand before God; Romans 11:34-35 echoes the same logic in its doxological conclusion: &#8220;Who has known the mind of the Lord? Or who has been his counselor? Who has first given to God, that God should repay him?&#8221; (citing Isa 40:13-14); both texts end the same way: God owes nothing to anyone; salvation is therefore entirely grace"}
    ],
    "11": [
      {"type": "allusion", "target": "Ps 50:12", "note": "&#8220;Everything under all the heavens belongs to me.&#8221; — God&#8217;s declaration of universal ownership is the exact claim of Psalm 50:12: &#8220;the world is mine, and all it contains&#8221;; both texts assert absolute divine proprietorship as the ground that makes all human giving to God categorically impossible — Job cannot bribe or obligate God, because there is nothing Job possesses that was not already God&#8217;s; the logic is the same as Paul&#8217;s in Romans 11:35 (who has given to God first?) — salvation cannot be earned because payment is impossible for the creature who owns nothing"}
    ],
    "33": [
      {"type": "allusion", "target": "Rev 13:4", "note": "&#8220;There is nothing on earth to compare with him; he is a creature fashioned without fear. He surveys everything that exalts itself; he is king over all the proud.&#8221; — Leviathan&#8217;s kingship over the proud, his incomparability, his surveying gaze over all that exalts itself, creates the OT template for what Revelation 13 describes of the beast: &#8220;Who is like the beast? Who can make war against it?&#8221; (Rev 13:4) — the language of Leviathan&#8217;s incomparability is repurposed for the beast that the fallen world worships; but both texts are answered by Revelation 19:11-16 and 20:2-10, where the Lamb who was slain proves greater than both Leviathan and beast"},
      {"type": "allusion", "target": "Ps 74:14", "note": "&#8220;He is king over all the proud&#8221; — the Leviathan who at creation&#8217;s end is king over pride is the same Leviathan that Psalm 74:14 declares already defeated: &#8220;it was you who crushed the heads of Leviathan and gave it as food to the creatures of the desert.&#8221; The psalmist appeals to YHWH&#8217;s past victory over Leviathan as grounds for present help; Job 41 shows why that past victory is the only grounds for hope — no human power could have done it; the cross is the definitive enactment of that crushing (Col 2:15; Heb 2:14)"}
    ]
  }
}

def main():
    existing = load_echo('job')
    merge_echo(existing, JOB_ECHO_39_41)
    save_echo('job', existing)
    print('Job 39-41 echo layer written.')

if __name__ == '__main__':
    main()
