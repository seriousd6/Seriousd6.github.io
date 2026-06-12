"""
MKT Christ Commentary — Job chapter 42
Run: python3 scripts/zc-christ-job-42-42.py
Key connections:
- Job 42:5  -> John 1:14 / 2 Cor 4:6 / 1 John 1:1-3 (hearing vs. seeing; the Incarnation as direct
               vision of God; "we have seen his glory"; knowledge of glory in face of Christ)
- Job 42:7  -> Acts 2:36 (God's verdict vindicates Job/Christ; resurrection as divine verdict)
- Job 42:8  -> Heb 7:25 / Luke 23:34 (Job intercedes for accusers; Christ intercedes for enemies)
- Job 42:10 -> shub shevut exile-return idiom; the gospel as ultimate return from exile
- Job 42:15 -> Gal 3:28-29 (daughters inherit alongside sons; equal inheritance in Christ)
- Job 42:17 -> John 14:2 / Rev 21 (died satisfied; death transformed into full life by resurrection)
"""

import json, pathlib
ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

new_data = {
    "42": {
        "1": "<p>Job answers the LORD &#8212; not the friends, not the absent mediator he longed for, but God himself. The entire book has been moving toward this moment of direct address. Christ makes this direct address to the Father possible for all: &#8220;through him we... have access in one Spirit to the Father&#8221; (Eph&#160;2:18).</p>",
        "2": "<p>&#8220;I know now that you can do all things and that no plan of yours can be stopped.&#8221; Job&#8217;s confession of divine omnipotence follows the encounter in the whirlwind. This is the knowledge of God that only direct encounter produces. Christ&#8217;s resurrection is the ultimate demonstration of this omnipotence: &#8220;with God all things are possible&#8221; (Matt&#160;19:26), including raising the dead.</p>",
        "3": "<p>&#8220;Who is this who speaks without knowledge? Therefore I have spoken of things I did not understand &#8212; things too wonderful for me that I did not know.&#8221; Job withdraws his &#8220;without knowledge&#8221; complaint as he quotes God&#8217;s question back. Paul describes the same experience of encounter with mystery: &#8220;for now we know in part&#8221; (1&#160;Cor&#160;13:12) &#8212; and Christ is the one in whom &#8220;all the treasures of wisdom and knowledge&#8221; are hidden (Col&#160;2:3), the deposit of the wonderful things Job couldn&#8217;t understand.</p>",
        "4": "<p>&#8220;You said: Listen, and I will speak; I will question you, and you shall answer me.&#8221; Job recites the terms of the divine encounter. Christ poses the decisive questions: &#8220;Who do you say I am?&#8221; (Matt&#160;16:15); &#8220;Do you believe this?&#8221; (John&#160;11:26); &#8220;Do you love me?&#8221; (John&#160;21:17). The God who questions and requires response is the pattern fully disclosed in Jesus&#8217;s pedagogy.</p>",
        "5": "<p>&#8220;I had heard about you by report, but now my own eyes have seen you.&#8221; The epistemological revolution of the theophany: from second-hand report to direct vision. The Incarnation is the definitive answer to Job&#8217;s wish: John&#160;1:14 &#8220;the Word became flesh and dwelt among us, and we have seen his glory.&#8221; 2&#160;Cor&#160;4:6: &#8220;God... has shone in our hearts to give the light of the knowledge of the glory of God in the face of Jesus Christ.&#8221; 1&#160;John&#160;1:1&#8211;3: &#8220;that which we have heard, which we have seen with our eyes, which we looked upon and have touched with our hands, concerning the word of life.&#8221; The hearing-versus-seeing transition that Job experiences in the whirlwind becomes permanently available through the Incarnation.</p>",
        "6": "<p>&#8220;Therefore I take back my words and repent in dust and ashes.&#8221; The posture of the creature before the holy Creator after genuine encounter. But the NT transformation is crucial: through Christ&#8217;s mediation, the encounter with God does not leave us in the dust but raises us. 1&#160;John&#160;3:2: &#8220;when he appears we shall be like him, because we shall see him as he is.&#8221; The dust-and-ashes response is real; but in Christ it is the prelude to resurrection, not the end of the story. Note that v6 is the book&#8217;s most debated verse &#8212; &#8220;repent&#8221; (<i>&#702;em&#702;&#257;s</i>) may mean withdrawing a legal posture, not moral guilt &#8212; which aligns with resurrection: Job withdraws the lawsuit, not admits sin.</p>",
        "7": "<p>&#8220;My anger burns against you and your two friends, because you have not spoken the truth about me, as my servant Job has.&#8221; God&#8217;s verdict vindicates Job and overturns the friends&#8217; theology. The resurrection of Christ is God&#8217;s definitive verdict: Acts&#160;2:36 &#8220;God has made him both Lord and Christ, this Jesus whom you crucified&#8221; &#8212; the resurrection is the Father&#8217;s vindication of the one who was condemned by human judgment. What the friends did to Job, the world did to Christ; and God vindicated both.</p>",
        "8": "<p>&#8220;My servant Job will pray for you, and I will accept his prayer on your behalf.&#8221; Job intercedes for his accusers &#8212; those who had condemned him without cause. This is the exact pattern of Christ: Luke&#160;23:34 &#8220;Father, forgive them, for they know not what they do.&#8221; Heb&#160;7:25: &#8220;he always lives to make intercession&#8221; for those who come through him &#8212; including his former adversaries. The interceding servant whose prayer is accepted is the type; Christ the great High Priest is the antitype.</p>",
        "9": "<p>The friends did what the LORD told them; and the LORD accepted Job&#8217;s prayer. The intercession succeeds: the accusers receive forgiveness through the prayer of the one they wronged. Rom&#160;5:10&#8211;11: &#8220;while we were enemies we were reconciled to God by the death of his Son&#8212; much more, now that we are reconciled, shall we be saved by his life.&#8221; The logic of ch.&#160;42:8&#8211;9 is the logic of the gospel: forgiveness through the intercession of the righteous one on behalf of the guilty.</p>",
        "10": "<p>&#8220;The LORD restored Job&#8217;s fortunes after he prayed for his friends; the LORD doubled everything Job had previously.&#8221; The <i>&#353;&#251;b &#353;ᵉb&#251;t</i> idiom &#8212; &#8220;turned the captivity&#8221; or &#8220;restored the fortunes&#8221; &#8212; is the exile-return language of Deut&#160;30:3; Jer&#160;29:14; Ezek&#160;39:25; Ps&#160;126:4. The gospel is the ultimate <i>&#353;&#251;b &#353;ᵉb&#251;t</i>: the return from the exile of sin and death, conditioned on the intercession of Christ. That the restoration comes after the intercession for the accusers teaches that the way to restoration runs through forgiveness of enemies.</p>",
        "11": "<p>All his brothers, sisters, and friends came, comforted him, and each gave him silver and a gold ring. The restored community gathered around the restored man. Heb&#160;2:11&#8211;12: &#8220;he is not ashamed to call them brothers... I will proclaim your name to my brothers.&#8221; Christ gathers the restored community around himself &#8212; and the comfort they bring is the <i>paraklēsis</i> that only God can give through the Spirit (2&#160;Cor&#160;1:3&#8211;4).</p>",
        "12": "<p>The LORD blessed the latter part of Job&#8217;s life more than the former &#8212; doubled livestock, a thousandfold. The double-blessing pattern. Eph&#160;3:20: God &#8220;is able to do far more abundantly than all that we ask or think, according to the power at work within us.&#8221; The blessings of the new creation exceed the blessings of the original creation &#8212; just as Christ&#8217;s resurrection body exceeds the original human body.</p>",
        "13": "<p>He also had seven sons and three daughters. The same number of children as before (1:2) &#8212; not doubled. This theological point is debated: the children lost are not replaced but the same number are given, implying that the original ten are not simply annulled. The resurrection logic applies: the dead are not replaced but raised &#8212; 1&#160;Cor&#160;15:42&#8211;44 &#8220;what is sown is perishable; what is raised is imperishable.&#8221;</p>",
        "14": "<p>He named his daughters Jemimah (dove/day), Keziah (cinnamon), Keren-happuch (horn of eye-shadow). Named daughters, in a culture where sons carried the name. The gospel names and dignifies those whom cultural convention overlooks: Luke&#160;8:2 (women named among Jesus&#8217;s disciples); John&#160;20:16 (Mary named at the resurrection, the first witness). Christ&#8217;s resurrection community includes those whose naming was unexpected.</p>",
        "15": "<p>&#8220;In all the land no women were as beautiful as Job&#8217;s daughters, and their father gave them property alongside their brothers.&#8221; The daughters inherit alongside the sons &#8212; a profound reversal of the ancient inheritance norm. Gal&#160;3:28&#8211;29: &#8220;there is neither Jew nor Greek, slave nor free, male nor female, for you are all one in Christ Jesus. And if you are Christ&#8217;s, then you are Abraham&#8217;s offspring, heirs according to promise.&#8221; The equal inheritance of the daughters is the OT shadow of the gospel&#8217;s equal inheritance in Christ.</p>",
        "16": "<p>After all this, Job lived a hundred and forty years and saw his children and grandchildren to the fourth generation. The double patriarchal lifespan (70 × 2 = 140) &#8212; restoration exceeding expectation. The promise of long life extends in Christ to eternal life: John&#160;11:26 &#8220;whoever lives and believes in me shall never die.&#8221; The generational blessing Job enjoyed points to the covenant blessing secured for all who are in Christ (Gal&#160;3:29).</p>",
        "17": "<p>&#8220;So Job died, old and satisfied with life (<i>&#347;&#257;b&#275;a&#702; y&#257;m&#238;m</i>).&#8221; The patriarchal death formula &#8212; &#8220;satisfied/full of days&#8221; &#8212; used of Abraham (Gen&#160;25:8), Isaac (Gen&#160;35:29), and David (1&#160;Chr&#160;29:28). The book ends with death &#8212; but a death that has passed through the fire of suffering, the silence of God, the encounter in the whirlwind, vindication, intercession, and restoration. In Christ, this kind of death is transformed entirely: &#8220;in my Father&#8217;s house are many rooms&#8221; (John&#160;14:2); &#8220;death is swallowed up in victory&#8221; (1&#160;Cor&#160;15:54). Job dies satisfied; Christ is raised; and those in Christ will see what Job could only dimly hope for: God himself, face to face (Rev&#160;22:4).</p>"
    }
}

existing = load_comm('mkt-christ', 'job')
merge_comm(existing, new_data)
save_comm('mkt-christ', 'job', existing)

for ch in sorted(new_data.keys(), key=int):
    vv = new_data[ch]
    have = sum(1 for v in vv if v in existing.get(ch, {}))
    print(f'  ch{ch}: {have}/{len(vv)} verses present')
