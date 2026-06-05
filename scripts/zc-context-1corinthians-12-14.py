"""
mkt-context layer — 1 Corinthians all 16 chapters
Output: data/commentary/mkt-context/1corinthians.json

Corinth was a cosmopolitan Roman colony (refounded 44 BCE by Julius Caesar)
at the strategic land-bridge between mainland Greece and the Peloponnese.
Paul founded the church ca. 50-51 CE (see the Gallio anchor, Acts 18:12).
He writes 1 Corinthians ca. 53-54 CE from Ephesus.
The letter responds to a Corinthian letter (7:1: peri de hon egrapsate)
and oral reports from Chloe's people (1:11).
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

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

CONTEXT = {
  "1": {
    "12": "<p>Corinth was one of the most commercially and socially stratified cities in Greece — a Roman colony dominated by social climbing (<em>cursus honorum</em>), patron-client relationships, and competitive display of status. The factions around Apollos, Cephas, Paul (and a 'Christ' party, possibly anti-leader) reflect the patron-client pattern of the ancient city: clients attached themselves publicly to powerful figures. Apollos is specifically described as 'eloquent' (<em>logios</em>, Acts 18:24) and trained in Alexandria — the preeminent philosophical and rhetorical city. The Corinthian preference for Apollos over Paul reflects the Greco-Roman premium on <em>paideia</em> (rhetorical education) and philosophical sophistication.</p>",

    "26": "<p>'Not many of you were wise according to worldly standards, not many were powerful, not many were of noble birth' — Paul's sociological observation about the Corinthian congregation aligns with archaeological and literary evidence about early Christianity. The preponderance of craftsmen, freedpersons, and modest household-level patrons (Stephanas, Gaius — who could host the whole church, 16:15; Rom 16:23) in the Pauline churches suggests a largely sub-elite membership, with some wealthy exceptions. Theissen's 'social-level theory' of the Corinthian congregation has been refined but not overturned: the community spanned a wider social range than most ancient voluntary associations, creating the tensions Paul addresses (especially in ch.11's Lord's Supper debate).</p>"
  },
  "5": {
    "1": "<p>The case of the man who has his father's wife (<em>gynaika tou patros</em>): Roman law (Lex Iulia de adulteriis, 18 BCE) prohibited sexual relations between a stepson and his stepmother; the Mishnah listed such relationships as severe sexual prohibitions (m. Yevamot 1:1). Paul's shock ('not even among pagans') indicates the offense violated both Jewish law and Greco-Roman legal convention. The Corinthians' boasting about this case (<em>pephysiomenoi</em>, you are arrogant, v.2) may reflect a 'progressive' wing that interpreted Christian freedom (<em>eleutheria</em>) as transcendence of bodily ethics — a proto-Gnostic pneumatism that Paul vigorously opposes.</p>"
  },
  "6": {
    "12": "<p>'All things are lawful for me' (<em>panta moi exestin</em>) appears twice in ch.6 (vv. 12, 13) and twice in ch.10 (vv. 23, 24) — likely a Corinthian slogan that Paul quotes then qualifies. The slogan may originate from a misappropriation of Paul's own teaching on freedom from the law (Gal 5:1-6). The Corinthian pneumatics may have distinguished the body (morally irrelevant, destined for destruction) from the spirit (the locus of salvation) — allowing bodily indulgence as spiritually inconsequential. Paul's refutation uses the body-resurrection theology of ch.15 as its foundation: because the body will be raised, what you do with it matters eschatologically.</p>"
  },
  "7": {
    "1": "<p>Chapter 7 opens Paul's responses to the Corinthian letter (<em>peri de hon egrapsate</em>, 'now concerning what you wrote'). The Corinthian letter apparently advocated celibacy and questioned the legitimacy of marriage — possibly under the influence of a proto-ascetic position that abstaining from sex was spiritually superior. Paul's careful response: marriage is good, celibacy is good; the unmarried state allows undivided devotion to the Lord (v. 32-35), but celibacy is a gift (<em>charisma</em>) not universally given (v. 7). This is not a low view of marriage but a principled defense of celibacy as a legitimate charism alongside marriage — both are gifts for different callings.</p>"
  },
  "8": {
    "1": "<p>Food sacrificed to idols (<em>eidolotyton</em>) was a pervasive practical problem in Roman Corinth: virtually all public meat was associated with temple sacrifice (the macellum / market sold temple-overflow), and banquets at temples (11 dining rooms excavated at the Corinthian Asclepion) were major social-network events. Refusing all idol-food risked social and commercial marginalization. Paul navigates between two Corinthian groups: the 'strong' (who know idols are nothing and eat freely) and the 'weak' (whose conscience is wounded by eating). His solution (ch.8-10) is neither pure permissivism nor pure restrictionism but a love-shaped freedom: knowledge (<em>gnosis</em>) without love (<em>agapē</em>) destroys the weak sibling.</p>"
  },
  "11": {
    "17": "<p>The Lord's Supper dispute (11:17-34) reveals a community fractured along social-class lines. In the Greco-Roman patronal meal pattern, the <em>deipnon</em> (dinner) involved social differentiation: the host and high-status guests ate first in the <em>triclinium</em> (dining room), while lower-status clients and dependents ate later in the <em>atrium</em> with inferior food. The Corinthian pattern appears to be: wealthier members ate early and privately (v. 21: 'one person goes hungry'), leaving the poor waiting (v. 33). Paul's rebuke is both theological (you shame the body of Christ) and social (you despise those who have nothing, v. 22).</p>"
  },
  "12": {
    "12": "<p>Paul's body-of-Christ metaphor in ch.12 has antecedents in Greco-Roman political philosophy: Livy (Ab Urbe Condita 2.32) records Menenius Agrippa's famous fable of the body's parts rebelling against the belly, used as political rhetoric in Roman social conflict. Paul takes a common political body-metaphor but inverts its social logic: not 'everyone must do their part for the commonwealth' (which typically reinforced elite leadership) but 'the weaker parts are indispensable' (v. 22) and 'God has given greater honor to the inferior part' (v. 24). The social inversion of the cross (1:18-25) shapes the social anthropology of the body.</p>"
  },
  "15": {
    "12": "<p>The Corinthians who denied the resurrection ('some of you say there is no resurrection of the dead', v. 12) were likely not denying Jesus's resurrection but denying a future bodily resurrection of believers. Greek philosophical anthropology (Platonic dualism) regarded the body as the prison of the soul — salvation was the soul's release from the body, not the body's transformation. The Corinthian 'enthusiasts' may have believed they had already been fully saved and spiritually resurrected (cf. 2 Tim 2:18). Paul's refutation shows that the resurrection of believers and the resurrection of Christ are structurally inseparable: deny one and you deny both.</p>",

    "29": "<p>Baptism for the dead (<em>hoi baptizomenoi hyper ton nekron</em>, v. 29): the most exegetically contested verse in 1 Corinthians, with over 200 proposed interpretations. Most significant proposals: (1) vicarious baptism by living persons for dead relatives (attested later in Marcionite practice; Chrysostom knew of this); (2) baptism over/in reference to the dead (i.e., in hope of sharing their resurrection); (3) baptism at the graves of martyrs. Paul does not endorse the practice, only uses it as an ad hominem argument: whatever you are doing, it presupposes bodily resurrection.</p>"
  }
}

def main():
    existing = load_comm('mkt-context', '1corinthians')
    merge_comm(existing, CONTEXT)
    save_comm('mkt-context', '1corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 Corinthians mkt-context: {len(existing)} chapters, {total} verses.')

if __name__ == '__main__':
    main()
