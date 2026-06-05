"""
mkt-original layer — 1 Corinthians all 16 chapters
Output: data/commentary/mkt-original/1corinthians.json

1 Corinthians is Paul's most sustained Greek rhetorical performance.
Key philological zones: sophia/logos wisdom-theology (ch1-4),
sarx/pneuma dualism (ch2-3), agape as a technical term (ch13),
and the anachronistic creedal formula of ch15.
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

ORIGINAL = {
  "1": {
    "18": "<p><strong>ho logos ho tou staurou</strong> (<em>ho logos ho tou staurou</em>, 'the word of the cross'): Paul's phrase is deliberate — not 'the theology of the cross' or 'the doctrine of the atonement' but the <em>logos</em> itself, the very message. <strong>moria</strong> (<em>mōria</em>, foolishness): Greco-Roman rhetoric valued wisdom (<em>sophia</em>) displayed through elegant argumentation (<em>logos</em>). Execution on a cross (<em>stauros</em>) was the most shameful death possible — reserved for slaves, pirates, and enemies of the state (Cicero Pro Rabirio 5.16: 'let the very word cross be far from the body, eyes, and ears of Roman citizens'). That this is the <em>power</em> (<em>dynamis</em>) of God for those being saved is Paul's inversion of all Greco-Roman honor-shame discourse.</p>",

    "24": "<p><strong>Christon Theou dynamin kai Theou sophian</strong> (<em>Christon Theou dynamin kai Theou sophian</em>): 'Christ the power of God and the wisdom of God.' Paul here makes Christ the personification of both divine attributes — power and wisdom are not merely Christ's qualities but identified with his person. This comes after the Corinthian division over rhetorical wisdom (1:12: some follow Apollo's eloquence, some Peter, some Paul). Paul's response: the divided parties are competing over what is no competition — Christ alone is Wisdom, and that wisdom is cruciform.</p>",

    "30": "<p><strong>sophias kai dikaiosynes kai hagiasmos kai apolytrosis</strong>: 'wisdom, righteousness, sanctification, and redemption.' The four nouns in asyndeton give Christ four forensic/cultic roles. <em>Dikaiosyne</em> (righteousness) covers the forensic standing; <em>hagiasmos</em> (sanctification/holiness) the cultic status; <em>apolytrosis</em> (redemption/release) the commercial-legal deliverance from bondage. That these are all said to be 'from God' (<em>apo theou</em>) makes clear they are received, not achieved. Paul is attacking the Corinthians' pride in human wisdom by showing that what they need — status, holiness, freedom — comes only from Christ.</p>"
  },
  "2": {
    "2": "<p><strong>ou gar ekrina ti eidenai en hymin ei me Iesoun Christon kai touton estauromemon</strong>: 'For I decided to know nothing among you except Jesus Christ and him crucified.' <em>Ekrina</em> is deliberate resolve, not ignorance. Paul came to the most philosophically sophisticated city in Greece and chose (<em>krinō</em>) to deploy only one argument: the cross. <em>Estauromenos</em> (crucified) is the perfect passive participle — not 'who was crucified' (past and done) but 'who is the crucified one' (ongoing identity). Paul's Christology is permanently cross-shaped.</p>",

    "13": "<p><strong>pneumatikois pneumatika synkrinontes</strong> (<em>pneumatikois pneumatika synkrinotes</em>): 'interpreting spiritual things to spiritual people' (or 'comparing spiritual things with spiritual things'). The phrase is syntactically ambiguous: <em>synkrinō</em> can mean 'combine' (matching Spirit-words with Spirit-people) or 'interpret' (explaining spiritual realities). Either way, Paul's point is that the Spirit's deep things (v. 10: <em>ta bathe tou theou</em>) are disclosed only within the Spirit's own interpretive community — those who have the mind of Christ (v. 16).</p>"
  },
  "3": {
    "16": "<p><strong>naos theou este kai to pneuma tou theou oikei en hymin</strong> (<em>naos theou este kai to pneuma tou theou oikei en hymin</em>): 'you are the temple of God and the Spirit of God dwells in you.' <em>Naos</em> is the inner sanctuary (the Most Holy Place and Holy Place), not merely the outer court (<em>hieron</em>). Paul uses the corporate 'you' (plural in Greek) — the community together is the <em>naos</em>, the place of divine habitation. This radically relocates the dwelling of God: not in the Jerusalem temple but in the community gathered around Christ. The destruction of this community-temple by division and immorality (v. 17) is therefore as serious as desecrating the Jerusalem sanctuary.</p>"
  },
  "6": {
    "19": "<p><strong>to soma hymon naos tou en hymin hagiou pneumatos estin</strong> (<em>to sōma hymōn naos tou en hymin hagiou pneumatos estin</em>): 'your body is a temple of the Holy Spirit within you.' Here the body (<em>sōma</em>) is singular — each believer's individual body is a sanctuary of the Spirit. This shifts 3:16's corporate sanctuary-language to the individual person. The implication for sexual ethics (vv. 15-18: not prostitution) is that bodily sin is sanctuary-desecration — the fornication charge is framed not as moral failure but as spatial-theological violation of the Spirit's dwelling place. <em>Agorazō</em> (to purchase, v. 20) is commercial-legal redemption language: you were bought at a price, therefore you are not your own property to dispose of as you wish.</p>"
  },
  "8": {
    "6": "<p><strong>heis theos ho pater ex hou ta panta kai hemeis eis auton kai heis kyrios Iesous Christos di hou ta panta kai hemeis di autou</strong>: Paul's two-clause Christological declaration is a deliberate restructuring of the Shema (Deut 6:4: YHWH our God, YHWH is one). Paul does not replace the Shema but expands it: the 'one God' (Father) and the 'one Lord' (Jesus Christ) together constitute the Shema's unity. The prepositions mark distinct roles: <em>ex hou</em> (from whom) for the Father as source; <em>di hou</em> (through whom) for the Son as agent/mediator. This is one of Paul's most explicit pre-Nicene Trinitarian formulas, set within a polemical argument about idols — the God who is one now includes Jesus Christ.</p>"
  },
  "11": {
    "24": "<p><strong>touto mou estin to soma to hyper hymon klomenon</strong> (<em>touto mou estin to sōma to hyper hymōn</em>, 'this is my body which is for you'): Paul's institution narrative (vv. 23-25) is the earliest written account of the Lord's Supper, predating the Gospels. <em>Parelabon ... paredoka</em> (I received ... I delivered) uses the technical Jewish tradition-transmission vocabulary (<em>qibbel... masar</em>): Paul claims this as received tradition, not his own creation. <strong>eis ten emen anamnesin</strong> (<em>eis tēn emēn anamnēsin</em>, 'in remembrance of me'): <em>anamnēsis</em> in LXX sacrifice contexts (Lev 24:7; Num 10:10) denotes a memorial that makes the past effective in the present — not merely cognitive recall but cultic re-presentation. The Eucharist re-presents Christ's self-offering.</p>"
  },
  "13": {
    "1": "<p><strong>ean tais glossais ton anthropon lalo kai ton angelon agapen de me echo</strong>: Paul begins the agape-chapter by making love the necessary condition for the validity of every spiritual gift. The 'tongues of angels' (<em>angelon glōssai</em>) was a Second Temple Jewish concept (cf. T. Job 48-50, where Job's daughters speak in angelic tongues) — Paul assumes this as a real category of speech. Without love (<em>agapē</em>), it is <em>chalkos echon</em> (a resounding gong) — the Corinthian competition over gifts produces sound without substance.</p>",

    "13": "<p><strong>nuni de menei pistis elpis agape ta tria tauta</strong>: 'but now these three remain: faith, hope, love.' <em>Nuni de</em> (but now) is Paul's characteristic eschatological-temporal marker: in the present age, before the complete (<em>to teleion</em>) arrives. The three are the characteristic present-age virtues (cf. 1 Thess 1:3; Rom 5:1-5; Col 1:4-5). <em>Meizōn de toutōn he agapē</em> (the greatest of these is love): not greater because it outlasts faith and hope (though it does — in the age to come there will be sight, not faith; possession, not hope), but greater because love is the nature of God himself (1 John 4:8) and therefore the eschatological reality into which faith and hope resolve.</p>"
  },
  "15": {
    "3": "<p><strong>paredoka gar hymin en protois ho kai parelabon</strong> (<em>paredōka gar hymin en prōtois ho kai parelabon</em>): the creedal formula of vv. 3-5 is the earliest extended theological statement in the NT, predating Paul's letters by roughly a decade after the crucifixion (30-35 CE). The four elements follow a strict parallelism: Christ died / was buried / was raised / appeared. <strong>kata tas graphas</strong> (twice): both the death and the resurrection are 'according to the Scriptures' — Scripture is the interpretive framework that gives the events their meaning; the cross is not a tragic accident but a divinely-ordained fulfillment of the entire OT witness.</p>",

    "20": "<p><strong>nuni de Christos egetertai ek nekron aparche ton kekoimemenon</strong> (<em>nuni de Christos egēgertai ek nekrōn aparchē tōn kekoimēmenōn</em>): <em>Aparche</em> (firstfruits) is the festival term for the first portion offered to God that consecrates and guarantees the whole (Lev 23:10-11; Num 18:12). By calling Christ the firstfruits of those who sleep, Paul makes his resurrection the <em>beginning</em> of the general resurrection, not an isolated miraculous event. The resurrection of believers is therefore not a secondary hope but structurally necessary: if Christ is firstfruits, the harvest will follow. <em>Kekoimēmenōn</em> (those who sleep) is the NT euphemism for death that Paul's resurrection-theology recontextualizes: sleep implies waking.</p>",

    "55": "<p><strong>pou sou thanate to nikos pou sou thanate to kentron</strong> (<em>pou sou, thanate, to nikos; pou sou, thanate, to kentron</em>): Paul adapts Hos 13:14 and Isa 25:8 into a victory-taunt over death. <em>Kentron</em> (sting/goad) was used for the venomous sting of a scorpion or the goading hook of a livestock driver — death's power to wound and compel. Paul names sin as death's sting (v. 56: <em>to de kentron tou thanatou he hamartia</em>) — death derives its terror from the law's capacity to count sin against us. Christ's death absorbs both the sting (sin's debt) and the goad (law's condemnation), leaving death powerless. The taunt is eschatologically realized, not merely future.</p>"
  }
}

def main():
    existing = load_comm('mkt-original', '1corinthians')
    merge_comm(existing, ORIGINAL)
    save_comm('mkt-original', '1corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 Corinthians mkt-original: {len(existing)} chapters, {total} verses.')

if __name__ == '__main__':
    main()
