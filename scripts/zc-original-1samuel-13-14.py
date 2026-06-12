"""
MKT Original Commentary — 1 Samuel chapters 13–14
Run: python3 scripts/zc-original-1samuel-13-14.py

Ch13: Saul's unlawful sacrifice at Gilgal — the first act that costs him the kingdom;
      Samuel's oracle: YHWH has sought a man after his own heart (13:14)
Ch14: Jonathan's faith raid at Michmash — acting without his father's knowledge;
      Saul's rash oath; Jonathan and the honey; the near-execution of Jonathan;
      the people's rescue of Jonathan; Saul's ongoing wars

Key Hebrew terms:
- nibbaltā (13:13): you have acted foolishly — from nābal (fool); Saul's own story
  connects to the nabal vocabulary of the book
- kilᵉḇābô (13:14): after his own heart — the unique descriptor of the coming Davidic king
- yônātān (14:6): his battle-cry of faith — nothing prevents YHWH from saving by many or few
- ḥardat ʾelōhîm (14:15): trembling of God — the supernatural panic at Michmash
- ʾālāh (14:24): the oath-curse Saul put on Israel — the rash vow that nearly costs Jonathan his life
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

ORIGINAL = {
  "13": {
    "8": "<p>Saul waits the seven days Samuel commanded (cf. 10:8) then acts alone: <em>wayyitʾappaq šāʾûl wayyaʿal hāʿōlāh</em> — 'Saul forced himself and offered the burnt offering.' The reflexive <em>hitpael</em> of <em>ʾāpas</em> — 'he forced himself' — is Saul's own explanation (v12). This is the Hebrew grammar of self-justification: Saul acts against his conscience, against the prophetic command, against the covenantal boundary, and the syntax marks this as a psychological act of self-overriding. The sacrifice itself is not sinful in kind — burnt offerings are the proper response to military crisis — but this one is offered by someone who has no authority to offer it: the king is not the priest. The boundary between royal and priestly office that Saul crosses is the same boundary that will later kill Uzziah when he enters the temple to burn incense (2 Chr 26:16-21).</p>",
    "12": "<p>Saul's self-defense: <em>wāʾōmar ʿattāh yērᵉdû pəlištîm ʾēlay hagilgālāh wûpənê YHWH lōʾ ḥillôtî</em> — &lsquo;I said, &ldquo;Now the Philistines will come down against me at Gilgal, and the face of YHWH I have not entreated,&rdquo; so I forced myself and offered the burnt offering.' The phrase <em>ḥillôtî ʾet pənê YHWH</em> (to entreat the face of YHWH) is the technical formula for seeking the divine oracle before battle (cf. Judg 1:1). Saul's problem is not that he failed to seek YHWH's face but that he sought it through an unauthorized action. The syntax of the excuse — 'I forced myself' — is the grammar of all rationalized disobedience: the imperative is real (seek YHWH before battle), the reasoning is plausible (Samuel is late), the act is catastrophic.</p>",
    "13": "<p>Samuel's verdict employs the vocabulary of divine rejection: <em>nibbāltā</em> — 'you have acted foolishly' — from the root <em>nābal</em>, the same root as Nabal the fool of ch25. Saul's foolish act is not primarily tactical but theological: <em>lōʾ šāmartā ʾet miṣwat YHWH ʾelōhêḵā ʾăšer ṣiwwāḵ</em> — 'you have not kept the commandment of YHWH your God which he commanded you.' The vocabulary is Deuteronomic: <em>šāmar miṣwāh</em> (to keep a commandment) is the covenant-loyalty formula that runs through Deut 4-11. Samuel's words make explicit that Saul's failure is not military or strategic but covenantal — the category of failure that will define the entire Saul narrative through ch15.</p>",
    "14": "<p>The most theologically dense verse in the Saul narrative: <em>biqēš YHWH lô ʾîš kilᵉḇābô</em> — 'YHWH has sought for himself a man according to his own heart.' The phrase <em>kilᵉḇābô</em> (after his heart/according to his heart) is unique in the OT as a description of the king YHWH seeks. <em>Lēḇāḇ</em> (heart) in Hebrew anthropology is the seat of will, understanding, and intention — the inner life that YHWH sees when he looks past appearance (16:7). The verb <em>biqēš</em> (to seek, search) suggests active divine initiative: YHWH has been looking, has found his candidate. Paul cites this verse in his Antioch synagogue sermon (Acts 13:22) as the theological basis for David's appointment — and by implication for Christ's: the king YHWH sought is the one whose heart is wholly aligned with YHWH's purposes, the antitype of both Saul and David, ultimately fulfilled in Christ who 'always does the things that are pleasing' to the Father (John 8:29).</p>"
  },
  "14": {
    "6": "<p>Jonathan's battle-speech to his armor-bearer is one of the OT's most compressed statements of active faith: <em>ûlᵉyôhônātān kî ʾên laYHWH māḵôr lᵉhôšîaʿ bᵉraḇ ʾô ḇimʿāṭ</em> — 'for nothing prevents YHWH from saving whether by many or by few.' The verb <em>māḵôr</em> (hindrance, restraint) is rare; the theological claim is radical: divine saving action is not constrained by military arithmetic. This anticipates Gideon's 300 (Judg 7), David's single stone against Goliath, and Paul's 'when I am weak, then I am strong' (2 Cor 12:10). Jonathan acts from the epistemological inversion that characterizes biblical faith: the normal ratio of forces is irrelevant when YHWH acts. His father Saul, by contrast, is paralyzed by numbers — waiting under a pomegranate tree while his kingdom evaporates (v2).</p>",
    "12": "<p>The armor-bearer's response — <em>ʿăśēh kol ʾăšer bilᵉḇāḇeḵā nəṭēh lāḵ hinnᵉnî ʿimmᵉḵā kilᵉḇāḇeḵā</em> — 'Do all that is in your heart; here I am with you according to your heart' — uses the <em>lēḇāḇ</em> vocabulary of 13:14: the man after the heart, the heart-aligned companion. The phrase <em>hinnᵉnî ʿimmᵉḵā</em> (here I am with you) echoes the divine commissioning formula (<em>ʾehyeh ʿimmāḵ</em>, 'I will be with you') given to Moses, Gideon, and the judges. Jonathan and his armor-bearer form a two-man unit operating in the <em>lēḇāḇ</em>-mode that defines the coming Davidic king — not Saul's paralyzed majority but Jonathan's faithful two.</p>",
    "15": "<p>The divine panic at Michmash is described as <em>ḥardat ʾelōhîm</em> — 'the trembling of God' — which even the ground participates in: <em>wattirʿaš hāʾāreṣ</em>, 'the earth shook.' The <em>ḥardat ʾelōhîm</em> is the supernatural terror that YHWH sends before his people to disable the enemy (cf. Exod 23:27 — 'I will send my terror before you'; Josh 2:9 — Rahab's report that the terror of Israel has fallen on the Canaanites). It is theophanic panic — the fear that precedes YHWH's presence in battle. The Michmash earthquake is also the beginning of a typological pattern: the earth shakes when YHWH acts decisively for his people (cf. Matt 27:51; 28:2 — the earthquake at the crucifixion and resurrection).</p>",
    "24": "<p>Saul's oath: <em>ʾārûr hāʾîš ʾăšer yōʾkal leḥem ʿad hāʿereb wənikqamtî mēʾōyᵉḇay</em> — 'Cursed is the man who eats bread until evening when I have avenged myself on my enemies.' The word <em>ʾārûr</em> (cursed) is covenant-curse vocabulary, drawing from the Deuteronomic blessings and curses (Deut 27-28). Saul invokes the covenant-curse mechanism to bind his own army, making food-restraint into a military-religious obligation. The result is the people's exhaustion (v31) and the near-death of Jonathan. The rash oath (<em>ʾālāh</em>) that nearly kills his own son is a pattern that Jephthah's daughter represents in the worst possible form (Judg 11) — covenant-curse language deployed without divine authorization, generating tragic consequence. Saul's oath is a smaller-scale Jephthah, with the people ultimately rescuing Jonathan where no one rescued Jephthah's daughter.</p>",
    "45": "<p>The people's covenant-rescue of Jonathan: <em>ḥālîlāh kî ʾim yāmût yôhônātān ʾăšer ʿāśāh hayyəšûʿāh haggəḏôlāh hazzōʾt bəyiśrāʾēl</em> — 'Far be it! Jonathan shall not die, for he has worked this great salvation (<em>yəšûʿāh gəḏôlāh</em>) in Israel.' The phrase <em>yəšûʿāh gəḏôlāh</em> (great salvation) is the same formula used by Samson after his jawbone victory (Judg 15:18) and the language from which <em>yēšûaʿ</em> (Jesus, 'salvation') derives its meaning. The people redeem Jonathan from Saul's death sentence — a son rescued from death by the intervention of the covenant community. The irony is double: the son who worked the salvation that neither Saul nor the army could accomplish is nearly killed by his own father's oath, and is only saved by the same people he delivered.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1samuel')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1samuel', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1samuel mkt-original: wrote {count} verses across ch 13-14')

if __name__ == '__main__':
    main()
