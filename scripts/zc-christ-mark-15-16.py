"""
MKT Christ — Mark all 16 chapters
Output: data/commentary/mkt-christ/mark.json

Mark\'s Christology is Son of God (1:1) framed by the baptism (1:11) and
the centurion (15:39). The Messianic Secret creates a pattern:
Jesus\'s identity is progressively revealed through suffering, not power.
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
    "1": '<p>A direct revelation: the beginning of the gospel of Jesus Christ, Son of God. Mark\'s opening declaration is the entire Gospel in one sentence: the subject of all that follows is Jesus (personal name, human historical identity), Christ (the Messiah, the anointed one of Israel\'s hope), and Son of God (the divine identity that gives the Messiah infinite worth). The gospel (euangelion) is not a teaching but a person — the announcement that this person has come, has acted, has died, has risen. Everything in Mark\'s 16 chapters is the unpacking of this opening declaration.</p>',
    "11": '<p>A direct revelation: you are my beloved Son; with you I am well pleased. The Father\'s declaration at the baptism identifies Jesus publicly as the royal Son (Ps 2:7) and the Servant-figure (Isa 42:1) simultaneously. Mark\'s Christology holds these two together without harmonizing them: the royal Son is the Suffering Servant; the one destined for universal dominion is the one who will give his life as a ransom for many. Every subsequent event in Mark unfolds the content of this dual identity — the exorcisms and healings demonstrate the Son\'s authority; the cross demonstrates the Servant\'s self-giving.</p>',
    "15": '<p>A direct revelation: the kingdom of God has come near — repent and believe in the good news. Christ is not merely the herald of the kingdom but its embodiment: wherever Jesus is, the kingdom is present. His exorcisms are kingdom-conflict (plundering the strong man\'s house, 3:27); his healings are the kingdom\'s compassion reversing the curse; his teaching is the kingdom\'s wisdom clarifying God\'s intention. The announcement that the time is fulfilled names Jesus\'s arrival as the fulfillment of the Danielic kairos — the appointed eschatological moment has come in his person.</p>'
  },
  "2": {
    "10": '<p>A direct revelation: the Son of Man has authority on earth to forgive sins. The Christological claim here is the most audacious of the Galilean ministry: Jesus exercises the divine prerogative of forgiveness not as a priestly representative applying a mechanism but in his own name, on his own authority, on earth. The Danielic Son of Man who received universal authority from the Ancient of Days is present in Capernaum, forgiving a paralytic, demonstrating that the eschatological reign has broken into the present through his person. The healing that follows makes the invisible forgiveness visible — the one who can do the harder thing (forgive) has demonstrated it by doing the visible thing (heal).</p>'
  },
  "3": {
    "27": '<p>A direct revelation: no one can enter a strong man\'s house and plunder his goods unless he first binds the strong man. The exorcisms are not individual humanitarian interventions but the systematic dismantling of the enemy\'s empire. Christ enters the strong man\'s house (the present age under demonic dominion) as the stronger one (the divine Son, anointed by the Spirit), binds the strong man (defeats Satan through the cross/resurrection), and plunders his goods (liberates those enslaved to demonic power). Every exorcism is an installment of this larger liberation — the kingdom\'s invasion of occupied territory.</p>'
  },
  "4": {
    "39": '<p>A direct revelation: he awoke and rebuked the wind and said to the sea, Peace! Be still. The calming of the storm is the exercise of the divine sovereignty over the waters that the OT declares belongs to YHWH alone (Ps 107:29, Job 9:8). Jesus exercises this sovereignty in his own person, not by prayer or petition to God, but by command: his word silences the storm. The disciples\' terrified question (who is this that even the wind and sea obey him?) is the question that Ps 107 answers — YHWH, who stills the storm. Mark presents Jesus as the one doing what the Psalm says only YHWH does.</p>'
  },
  "5": {
    "41": '<p>A direct revelation: Talitha koum — little girl, I say to you, arise. The resurrection of Jairus\'s daughter is the first explicit raising-from-death in Mark, performed with a simple Aramaic command. The contrast with later resurrection narratives (the elaborate prayer of Elijah in 1 Kgs 17:21, the stretching of Elisha over the boy in 2 Kgs 4:34-35) is stark: Jesus does not pray, does not invoke God, does not perform a ritual — he speaks to the dead girl as to a sleeping child. The command-authority over death revealed here is the authority that will be exercised in his own resurrection and in the final resurrection.</p>'
  },
  "8": {
    "29": '<p>A direct revelation: Peter answered him, You are the Christ. The Petrine confession at Caesarea Philippi is the structural center of Mark\'s Gospel. The immediate sequence that follows is theologically decisive: the Messianic Secret (silence commanded), the passion prediction (the Christ will suffer and die), and the call to cross-bearing. Mark\'s Christological argument is that the Messiah is only correctly understood as the Suffering Servant — to confess the Christ without the cross is to confess a misunderstood Christ. Peter\'s rebuke (v.32) and Jesus\'s sharp response (get behind me, Satan) demonstrate that Messiahship divorced from suffering is a Satanic distortion, not a divine truth.</p>',
    "34": '<p>A direct revelation: if anyone wishes to come after me, let him deny himself and take up his cross and follow me. The cross is not a Markan metaphor for general difficulty but a specific path: the path Christ himself walked. Discipleship in Mark is defined by cross-bearing — sharing the master\'s path of self-denial, rejection, suffering, and death in the confidence of resurrection. The cross-bearing community is the community shaped by the Christology: the Son of God who died reveals what it means to follow the Son of God who died. Mark\'s suffering community (addressed in the Roman persecution context) is being told that their cross-bearing is not a contradiction of the gospel but its confirmation.</p>'
  },
  "10": {
    "45": '<p>A direct revelation: the Son of Man came not to be served but to serve and to give his life as a ransom for many. Mark\'s version of the ransom saying is the definitive self-interpretation of the cross in this Gospel. The movement is from the Danielic Son of Man (who receives universal service, Dan 7:14) to the Isaianic Servant (who gives his life for the many, Isa 53:12) — Jesus holds both identities and describes their synthesis: the one who deserves all service gives himself for others\' ransom. The cross is not the defeat of the Son of Man but the specific form in which the Son of Man\'s authority is exercised.</p>'
  },
  "11": {
    "17": '<p>A direct revelation: is it not written, My house shall be called a house of prayer for all the nations? Jesus\'s temple action is a Christological claim: he acts with the authority of the temple\'s owner and designer (the divine author of Isa 56:7), overturning what has violated its purpose and restoring its universal-prayer function. The cursing of the fig tree (11:12-14) and the withering confirmed (11:20-21) frame the temple action, suggesting that the temple institution itself is under the same judgment as the fruitless tree. Christ is both fulfilling the temple\'s purpose and announcing its coming replacement by the community gathered around himself.</p>'
  },
  "14": {
    "22": '<p>A direct revelation: take; this is my body. The Last Supper words are the most concentrated Christological claim in Mark: Jesus identifies the bread with his body and the cup with the blood of the covenant poured out for many. He interprets his own impending death through the Passover and Sinai covenant frameworks — his body is the Passover lamb whose blood protects from judgment, and his blood is the covenant blood of Sinai that ratifies the relationship between God and people. The Lord\'s Supper instituted here is the permanent memorial of the one historical event on which the new covenant community is founded.</p>',
    "62": '<p>A direct revelation: I am; and you will see the Son of Man seated at the right hand of Power and coming with the clouds of heaven. Jesus\'s response before the high priest is the most explicit Christological self-disclosure in Mark. At the moment of maximum vulnerability (arrested, tried, abandoned), Jesus speaks the most comprehensive claim: he is the I AM (the divine self-identification), the enthroned Son of Man at God\'s right hand (Ps 110:1), and the coming one with divine glory (Dan 7:13). The humiliation does not diminish the claim; it is the form in which the claim reaches its fullest expression — the Son of God who dies is the Son of God who reigns.</p>'
  },
  "15": {
    "34": '<p>A direct revelation: my God, my God, why have you forsaken me? The cry of dereliction is a Christological statement about substitutionary atonement: the Son of God genuinely experiences God-forsakenness as the penalty of sin he bears for others. This is not theatrical or only apparent — the spiritual weight of bearing what separates humanity from God is real, and Jesus bears it in his own person. The darkness (v.33), the cry, and the death together constitute the atonement: at Golgotha, God in Christ is in the place of the God-forsaken, absorbing the wrath that sin deserves, so that those who trust him never need to experience that forsakenness themselves.</p>',
    "39": '<p>A direct revelation: truly this man was Son of God. The centurion\'s confession at the cross is Mark\'s Christological climax. The Gospel that opened with the declaration Jesus Christ, Son of God (1:1) and that the demons recognized throughout (1:24, 3:11, 5:7) now receives its human confession — from a Roman soldier, not a Jewish disciple, at the moment of death, not of triumph. Mark argues that the cross is not the refutation of the divine sonship but its revelation: it is precisely the manner of his death (v.39 — how he died) that leads the centurion to the confession. The Son of God is most clearly seen at the cross.</p>'
  },
  "16": {
    "6": '<p>A direct revelation: he has been raised; he is not here. The resurrection announcement by the young man (angel) in the empty tomb is the counterpart to the Father\'s declaration at the baptism: the one identified as the beloved Son (1:11) is the one raised from the dead (16:6). Mark does not narrate resurrection appearances (in the original ending) but declares the resurrection and points forward to Galilee — the community is to follow the risen Lord as they followed the living Lord through Mark\'s Gospel. The resurrection vindicates everything Jesus claimed and fulfills every passion prediction; it is the Father\'s endorsement of the Son\'s entire Messianic-Servant mission.'
  }
}

def main():
    existing = load_comm('mkt-christ', 'mark')
    merge_comm(existing, DATA)
    save_comm('mkt-christ', 'mark', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Mark mkt-christ: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
