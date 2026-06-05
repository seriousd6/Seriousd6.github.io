"""
MKT Original — Mark all 16 chapters
Output: data/commentary/mkt-original/mark.json

Mark is written in vivid, action-packed koine Greek with a lower register than
Luke or Matthew. Key features: euthys (immediately/straightway) — occurs 41 times;
imperfect tenses for vivid narrative; historic present verbs; aramaic transliterations
(talitha koum, ephphatha, eloi eloi, abba); Messianic Secret (epitimao/silence commands).
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

DATA = {
  "1": {
    "1": '<p><strong>arche tou euangeliou Iesou Christou huiou theou</strong> — the beginning of the gospel of Jesus Christ Son of God — Mark\'s opening is not a genealogy or birth narrative but a simple proclamation-header: the subject of what follows is the euangelion (good news, the Roman herald\'s announcement of a great event — usually a military victory or an emperor\'s birth). <em>Arche</em> (beginning) echoes Gen 1:1 and John 1:1; Mark presents the ministry of Jesus as the beginning of the new creation\'s decisive chapter. The genitive <em>Iesou Christou</em> is objective (the gospel about Jesus Christ) and possibly subjective (the gospel Jesus proclaimed); both are true.</p>',
    "15": '<p><strong>peplerothe ho kairos</strong> — the time is fulfilled — <em>kairos</em> (appointed time, season) vs. <em>chronos</em> (linear time); the <em>kairos</em> is the divinely appointed moment within time when the decisive event occurs. <strong>euthys</strong> (immediately) is Mark\'s signature adverb, appearing 41 times. It gives Mark\'s narrative the pace of urgent eschatological action: the kingdom\'s arrival is not gradual but sudden and demanding. <strong>metanoeite kai pisteuete en to euangelio</strong> — repent and believe in the good news — the two responses named: <em>metanoeite</em> (change direction) + <em>pisteuete</em> (trust, commit); together they define the covenant entry into the kingdom.</p>',
    "44": '<p><strong>ora medeni meden eipes</strong> — see that you say nothing to anyone — the first of Mark\'s Messianic Secret commands (cf. 1:25, 3:12, 5:43, 7:36, 8:30, 9:9). The Messianic Secret is Mark\'s distinctive theological pattern: Jesus repeatedly silences those who recognize him. This is not deception but the correct ordering of revelation — the full meaning of his identity can only be understood through the cross, which has not yet occurred. To announce the Messiah before the cross would be to proclaim a false Messiah (a triumphalist king rather than the Suffering Servant).</p>'
  },
  "2": {
    "10": '<p><strong>exousian echei ho huios tou anthropou aphienai hamartias epi tes ges</strong> — the Son of Man has authority on earth to forgive sins — the first Danielic Son of Man claim in Mark (cf. Dan 7:13-14); the universal dominion given to the Son of Man in Daniel is now being exercised in the specific act of pronouncing forgiveness in a Capernaum house. <em>Epi tes ges</em> (on earth) is emphatic: this divine prerogative is being exercised in the present earthly ministry, not deferred to the final judgment. The visible healing is the credential of the invisible forgiveness.</p>',
    "19": '<p><strong>mhe dynastai hoi huioi tou nymphonos en ho ho nymphios estin autois nesteuen</strong> — the wedding guests cannot fast while the bridegroom is with them — <em>huioi tou nymphonos</em> (sons of the wedding chamber) is a Semitic idiom for wedding guests; the idiom places Jesus in the role of the messianic bridegroom (cf. Isa 54:5-6, Hos 2:19). The presence of the bridegroom defines the appropriate response: feasting, not fasting. The eschatological joy is already present in Jesus\'s person; mourning practices are inappropriate in the kingdom\'s inaugural moment.</p>'
  },
  "3": {
    "28": '<p><strong>amēn lego hymin hoti panta aphethesetai tois huiois ton anthropon ta hamartemata kai hai blasphemiai</strong> — all sins will be forgiven the sons of men and whatever blasphemies they utter — the universality of forgiveness is stated first; then the single exception is given. <strong>blasphemia eis to pneuma to hagion</strong> — blasphemy against the Holy Spirit — the attribution of the Spirit\'s works (exorcism by the Spirit of God) to the demonic; the sin that cannot be forgiven because it involves the willful inversion of the Spirit\'s identification of Christ, thereby placing oneself permanently outside the Spirit\'s reach who grants repentance.</p>'
  },
  "4": {
    "11": '<p><strong>hymin to mysterion dedotai tes basileias tou theou</strong> — to you the mystery of the kingdom of God has been given — <em>mysterion</em> (mystery) in Jewish apocalyptic usage is the hidden divine plan that is disclosed only to the elect (Dan 2:18, 27-30; 1QpHab 7). The disclosure is a gift (<em>dedotai</em>, divine passive) not an achievement. <strong>ekeinois de tois exo en parabolais ta panta ginetai</strong> — but for those outside everything is in parables — the binary (inside/outside) reflects the community\'s self-understanding as those who have received the revelation that the world has not; the parables function simultaneously as revelation (for insiders) and concealment (for outsiders who refuse).</p>',
    "26": '<p><strong>hos anthropos bale ton sporon epi tes ges kai katheude kai egeire nykta kai hemeran kai ho sporos blastan kai mekynetai</strong> — the kingdom of God is as if a man scatters seed on the ground and sleeps and rises night and day and the seed sprouts and grows he knows not how — the unique feature of this Markan-only parable is the farmer\'s passivity: the growth occurs <em>automatē</em> (v.28, of itself, automatically, the origin of our word automatic). The kingdom\'s growth is not a human program but a divine process; human beings plant and wait but do not control the growth.</p>'
  },
  "5": {
    "7": '<p><strong>ti emoi kai soi Iesou huie tou theou tou hypsistou</strong> — what have I to do with you, Jesus, Son of God Most High? — the demonic recognition of Jesus\'s identity is ironic: the demons know what the disciples struggle to grasp. <em>Ti emoi kai soi</em> is a Semitic idiom (mah li valak) denoting confrontation and distancing: what is there between us? <strong>tou hypsistou</strong> — of the Most High — the divine title used predominantly in Gentile contexts (cf. Gen 14:18-20, Dan 4:24, Acts 16:17); the Gentile-territory encounter uses the universal divine name.</p>',
    "41": '<p><strong>talitha koum</strong> — Talitha koum — Mark uniquely preserves the Aramaic words of Jesus (1:41, 5:41, 7:34, 14:36), which gives the narrative the quality of eyewitness immediacy and grounds the tradition in the actual words of Jesus rather than theological paraphrase. <em>Talitha</em> = little girl (Aramaic); <em>koum</em> = arise, stand up. The interpreter\'s translation follows (<em>to korasion, soi lego, egeire</em> = little girl, I say to you, arise), emphasizing Jesus\'s sovereign command-authority over death.</p>'
  },
  "6": {
    "34": '<p><strong>eide pollyn ochlon kai esplanchnisthe ep autous</strong> — he saw a great crowd and had compassion on them — <em>splanchnizomai</em> (to be moved in the innards, to feel gut-level compassion) is the strongest Greek emotion-word available; it is always used in the Synoptics for Jesus\'s response to human suffering. The reason given (<em>hoti esan hos probata me echonta poimena</em> = because they were like sheep without a shepherd) is the Ezekiel 34 diagnosis — the abandoned flock. Jesus\'s compassion is the divine shepherd\'s response to the prophetically diagnosed abandonment.</p>'
  },
  "7": {
    "34": '<p><strong>ephphatha</strong> — Ephphatha — another Aramaic preservation (cf. 5:41); the word itself becomes performative: Jesus says be opened and the ears open. <em>Mogilalos</em> (v.32, speaking with difficulty or mute) is the LXX word in Isa 35:6 (the tongue of the mute will sing for joy) — Mark uses the Isaiah-term for the man healed, signaling that the Isaianic healing-sign is being enacted. The detail of Jesus\'s sighing (<em>estenaxen</em>) before the healing is a characteristic Markan note of Jesus\'s genuine human emotion and the weight he carries in the healing-mission.</p>'
  },
  "8": {
    "29": '<p><strong>hymeis de tina me legete einai</strong> — but who do you say that I am? — the crucial Christological question placed at the Gospel\'s structural midpoint (ch.8 is the pivot between Galilee-ministry and Jerusalem-passion in Mark). <strong>su ei ho Christos</strong> — you are the Christ — Peter\'s confession without the fuller Matthew expansion (Son of the living God). Immediately after the confession, the Messianic Secret is commanded (v.30) and the passion prediction follows (v.31), connecting Messiahship directly to suffering and rejection. In Mark, you cannot confess the Messiah without immediately being told about the cross.</p>',
    "34": '<p><strong>ei tis thelei opiso mou akolouthein, aparnessastho heauton kai arato ton stauron autou kai akoloutheitō moi</strong> — if anyone wishes to come after me, let him deny himself and take up his cross and follow me — the three imperatives are sequential: (1) <em>aparnessastho heauton</em> (deny himself = disown the self\'s claims on its own life); (2) <em>arato ton stauron autou</em> (take up his cross = adopt the posture of the condemned man carrying his instrument of execution); (3) <em>akoloutheitō moi</em> (follow me = continue in discipleship to the one walking to his death). Cross-bearing in Mark\'s context is not metaphor but literal: the disciples are called to the same path of suffering their master walks.</p>'
  },
  "9": {
    "24": '<p><strong>pisteuō; boethei mou te apistia</strong> — I believe; help my unbelief — one of the most theologically honest statements in the Gospels; the father\'s response is not a claim to complete faith but a simultaneous affirmation of what faith he has and an acknowledgment of its inadequacy. The prayer is self-aware about its own condition: the faith that asks for help with unbelief is already a form of faith (it turns to Christ rather than away from him). The raw honesty is characteristic of Mark\'s straightforward Christological realism.</p>'
  },
  "10": {
    "18": '<p><strong>ti me legeis agathon</strong> — why do you call me good? — the question is not a denial of Jesus\'s goodness but a probe into the rich young man\'s understanding. <em>Oudeis agathos ei me heis ho theos</em> — no one is good except God alone — if the man means only the common social compliment, the title is misapplied; if he means the absolute goodness that belongs to God alone, then his address to Jesus is more accurate than he knows. The question forces the recognition that the one being addressed either is not good (in which case the title is wrong) or is God (in which case the title barely captures the reality).</p>',
    "45": '<p><strong>ho huios tou anthropou ouk elthen diakonethenai alla diakonesai kai dounai ten psychen autou lytron anti pollon</strong> — the Son of Man came not to be served but to serve and to give his life as a ransom for many — the <em>anti</em> (in exchange for, instead of) is substitutionary: his life is the price paid in the place of the many. <em>Pollon</em> (many) in Semitic usage is inclusive (the many = all, cf. Isa 53:12); it does not limit the scope but emphasizes the number of beneficiaries. The Servant of Isa 53 who gives himself for the many is the Christological background: Jesus names this as his mission-purpose.</p>'
  },
  "11": {
    "17": '<p><strong>ho oikos mou oikos proseuchesetai pasin tois ethnesin</strong> — my house shall be called a house of prayer for all the nations — Mark uniquely preserves the Isaianic for all nations (Isa 56:7) that Matthew and Luke abbreviate. The universal scope is Mark\'s emphasis: the temple was designed not for ethnic-Israel exclusivity but for all-peoples access to the one God. The money-changers have occupied the only court designated for Gentile prayer. The temple\'s failure to be the house of prayer for all nations is the specific charge. Jesus\'s action is the restoration of Gentile access, a theme consistent with Mark\'s Gentile-friendly orientation.</p>'
  },
  "12": {
    "29": '<p><strong>akoue Israel, kyrios ho theos hemon kyrios heis estin</strong> — Hear, O Israel: the Lord our God, the Lord is one — Mark\'s version of the greatest commandment uniquely includes the Shema itself (Deut 6:4) as the foundation for the love-command. The scribe affirms Jesus\'s answer and adds that this love is more than all burnt offerings and sacrifices (v.33, citing Hos 6:6 / 1 Sam 15:22), and Jesus responds that the scribe is not far from the kingdom of God. This is Mark\'s only positive scribal encounter — the exception that proves the rule of official opposition.</p>'
  },
  "13": {
    "26": '<p><strong>kai tote opsontai ton huion tou anthropou erchomenon en nephelais</strong> — and then they will see the Son of Man coming in clouds — the Danielic vision (Dan 7:13) is cited in full; the coming-in-clouds is not spatial movement downward but the divine-presence-vehicle that indicates the Son of Man\'s authority-vindication. In Daniel\'s vision the Son of Man comes to the Ancient of Days (upward, receiving authority); in Mark\'s use the coming is toward the earth (downward, exercising the authority received). Both directions of travel are aspects of the same enthronement event.</p>'
  },
  "14": {
    "36": '<p><strong>abba ho pater, panta dynata soi</strong> — Abba, Father, all things are possible for you — Mark preserves the Aramaic <em>Abba</em> (the intimate word for father used within the family, though not exclusively infantile as sometimes claimed; cf. Rom 8:15, Gal 4:6 where it is the Spirit\'s cry in believers). The address combines intimacy (<em>Abba</em>) with theological acknowledgment (all things are possible for you), making the submission that follows (<em>all the same, not what I will but what you will</em>) the freely chosen embrace of a possible alternative — the Father could have chosen otherwise but Jesus submits to the path chosen.</p>',
    "62": '<p><strong>ego eimi kai opsesthe ton huion tou anthropou ek dexion kathemenon tes dynameōs kai erchomenon meta ton nephelos tou ouranou</strong> — I am; and you will see the Son of Man seated at the right hand of Power and coming with the clouds of heaven — Mark\'s high priest question receives the most direct answer in any Gospel (<em>ego eimi</em> vs. Matthew\'s <em>you have said so</em> and Luke\'s more guarded response). The ego eimi (I am) carries the divine-name resonance. The combination of Ps 110:1 (seated at the right hand) and Dan 7:13 (coming with the clouds) is Jesus\'s Christological self-claim at the moment of maximum vulnerability — arrested, abandoned, tried — which makes it simultaneously the most audacious claim and the most theologically complete self-revelation in Mark.</p>'
  },
  "15": {
    "34": '<p><strong>eloi eloi lema sabachthani</strong> — My God, my God, why have you forsaken me — Mark uses a slightly different Aramaic form from Matthew; both transliterate Ps 22:1. The double divine address (<em>my God, my God</em>) is the Psalm\'s opening cry — urgent, trusting, and anguished simultaneously. Mark\'s stark account of the crucifixion (no earthquake, no opened tombs as in Matthew, no thief-repentance as in Luke) makes the cry of dereliction the climactic statement: the Son of God dies abandoned by God, bearing what sinners deserve, before the vindication that Ps 22\'s own ending provides (vv.24-31: YHWH has not despised the affliction of the afflicted one).</p>',
    "39": '<p><strong>alethos houtos ho anthropos huios en theou</strong> — truly this man was Son of God — the centurion\'s confession is the human climax of Mark\'s Christology: the one who was declared Son of God by the Father at the baptism (1:11) is recognized as Son of God by a Roman soldier at the death. The inclusio is complete. Mark has no birth narrative because he begins with the Son\'s public identification (baptism-declaration) and ends with the soldier\'s confession — the entire Gospel is bounded by the Son of God identity, revealed through the Servant\'s death rather than despite it.</p>'
  },
  "16": {
    "6": '<p><strong>egerthe, ouk estin ode</strong> — he has been raised; he is not here — the passive <em>egerthe</em> (he was raised, divine passive) identifies the resurrection as God\'s act, not a resuscitation or self-resurrection. The empty tomb is the negative evidence; the positive evidence is the proclamation (<em>proagei hymas eis ten Galilaian</em> = he is going before you to Galilee). Mark\'s original ending (assuming 16:8 is the original ending) is characteristically abrupt: the women fled and said nothing to anyone, for they were afraid. The reader is left with the open question that the entire Gospel posed — who do you say that he is? The silence of the women is the silence into which the reader must speak.</p>'
  }
}

def main():
    existing = load_comm('mkt-original', 'mark')
    merge_comm(existing, DATA)
    save_comm('mkt-original', 'mark', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Mark mkt-original: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
