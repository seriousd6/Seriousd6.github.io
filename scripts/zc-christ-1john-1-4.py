"""
MKT Christ — 1 John chapters 1–4 (Christological trajectory)
Output: data/commentary/mkt-christ/1john.json

Directness classifications for 1 John 1-4:
- 1:1-2 "A direct revelation:" — the eternal Word made experiential
- 1:7 "A direct revelation:" — Christ's blood as the cleansing agent
- 2:1 "A direct revelation:" — Christ as heavenly parakletos
- 2:2 "A direct revelation:" — Christ as hilasmos
- 2:22-23 "A direct revelation:" — Son-denial = Father-denial
- 3:5 "A direct revelation:" — the sinless Son appeared to take away sin
- 3:8 "A direct revelation:" — Son of God appeared to destroy devil's works (fulfills Gen 3:15)
- 4:2 "A direct revelation:" — the incarnation as the Christological criterion
- 4:9-10 "A direct revelation:" — the Son-sending as love's revelation and hilasmos
- 4:14 "A direct revelation:" — the Father sent the Son as Savior of the world
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
    "1": '<p>A direct revelation: that which was from the beginning, which we heard, which we saw, which we handled — the eternal Word of life disclosed in tangible, historical, apostolic experience. John declares not a theology derived from observation but a person encountered through the senses: Christ is the content of the testimony, not merely its subject. The movement from eternal being (from the beginning) to physical handling (our hands touched) is the complete arc of the incarnation compressed into the letter\'s opening relative clause. All Christological claim in the letter flows from this initial declaration of the Word-made-touchable.</p>',
    "7": '<p>A direct revelation: the blood of Jesus his Son cleanses us from all sin. The Christological precision is complete: Jesus (his human name, historical identity) is the Son (his divine relation, which gives the blood its infinite worth) and his blood cleanses. No shadow, type, or pointer here — the letter makes the direct claim that the historical event of the crucifixion is the ongoing cleansing agent for the community. The present tense (cleanses) points to the continuing efficacy of a once-completed act — Christ\'s blood is not merely past history but present purification.</p>'
  },
  "2": {
    "1": '<p>A direct revelation: Jesus Christ the righteous as our advocate (parakletos) before the Father. The intercession of Christ at the right hand of the Father is the NT\'s central heavenly-ministry claim — here stated in the pastoral context of community members who sin. The righteous one advocates for the unrighteous; his qualification is not his community membership but his character (<em>dikaios</em>) and his completed atonement (v.2). This is not typological but direct: no OT high priest is needed as the comparison point; Christ himself is named as the present, effective advocate.</p>',
    "2": '<p>A direct revelation: he is the propitiation for our sins, and not for ours only but for the whole world. The Christological office of hilasmos (propitiation) belongs to Christ directly — not prefigured by the mercy seat (though the typological connection enriches the meaning) but exercised by Christ as his own completed act. The scope (the whole world) is the universal offer that the community possesses as its own experience and proclaims to all others. No further mediation is needed: Christ is the complete and sufficient atoning sacrifice for all.</p>',
    "22": '<p>A direct revelation: whoever denies that Jesus is the Christ denies the Father also. The Christological criterion here is not ethical but confessional: the content of faith determines the reality of one\'s relationship to the Father. This is not rationalism (the right formula saves) but the recognition that the Father has identified himself definitively through the Son — to refuse the Son is to refuse the Father\'s own self-disclosure. The mutual-indwelling theology (Son and Father) means that acceptance or rejection of Christ is acceptance or rejection of the God who sent him.</p>'
  },
  "3": {
    "5": '<p>A direct revelation: you know that he was revealed to take away sins, and in him there is no sin. Two Christological claims in tandem: the purpose of the revelation (to take away sins — the substitutionary and cleansing mission) and the qualification of the one revealed (no sin in him — the sinless one who can bear what he did not owe). The sinlessness is not background information but active qualification: only the one with no sin of his own could effectively take away the sins of others. The aorist (he was revealed) points to the definitive historical appearing of the incarnate Son.</p>',
    "8": '<p>A direct revelation: the Son of God appeared (ephanerothe) to destroy the works of the devil — the fulfillment of Genesis 3:15. The protoevangelium promised enmity between the seed of the woman and the seed of the serpent, and the crushing of the serpent\'s head. John identifies the appearing of the Son of God as the moment this promise is fulfilled: the one appeared precisely for this destructive-redemptive purpose. The works of the devil (deception, accusation, death, bondage to sin) are being undone by the one who is greater than the evil one (4:4).</p>',
    "16": '<p>A direct revelation: by this we know love, that he laid down his life for us. The cross is the definition of love itself — not an illustration of a pre-existing concept of love but the originating event from which love is first properly understood. John inverts the expected direction: we do not apply a definition of love to Christ\'s death; we derive our definition of love from Christ\'s death. The community\'s love for one another is therefore derivative and participatory: we lay down our lives in imitation of and participation in the one who first laid down his life for us.</p>'
  },
  "4": {
    "2": '<p>A direct revelation: Jesus Christ has come in the flesh — every spirit that confesses this is from God. The incarnation is not merely one doctrine among others but the watershed Christological claim: the eternal Son\'s permanent assumption of humanity. The perfect participle (having-come-in-flesh) declares not merely that the incarnation happened but that its results remain — the risen Christ is still the enfleshed Christ, the glorified one still bearing the wounds (John 20:27). This confession is the boundary of genuine Christology and the test of any claimed spiritual experience.</p>',
    "9": '<p>A direct revelation: in this the love of God was revealed among us, that God sent his only Son into the world so that we might live through him. The revelation of love is not a general religious insight but a specific historical event: the sending of the monogenes Son (the one-and-only Son, echoing John 3:16). The telos of the sending (that we might live through him) establishes the Son\'s role as the mediatorial source of eschatological life — not an example of life to imitate but a source of life to receive. All the letter\'s ethics flow from this gift-logic: received life produces outgoing love.</p>',
    "10": '<p>A direct revelation: in this is love, not that we loved God but that he loved us and sent his Son to be the propitiation for our sins. The definition of love is again grounded in the Son-sending, specifically in its atoning dimension. The propitiation (hilasmos) names the specific mechanism by which the love was enacted: not sentimental feeling but wrath-satisfying sacrifice. The prevenience of God\'s love (not that we loved God but that he loved us) is the Christological datum: love found its form in the cross before anyone had yet responded to it.</p>',
    "14": '<p>A direct revelation: the Father has sent his Son to be the Savior of the world. The universal scope of salvation (Savior of the world, not merely of the community or of Israel) is grounded in the Father\'s specific sending of the Son. The title Savior (<em>soter</em>) carries both Jewish liberation-history resonance (YHWH as Israel\'s only savior, Isa 43:11) and Greco-Roman political resonance (emperors and benefactors called soter in Ephesus). John applies both registers to Christ: he fulfills the divine salvation-monopoly of the OT while surpassing the civic salvation-claims of imperial religion.</p>'
  }
}

def main():
    existing = load_comm('mkt-christ', '1john')
    merge_comm(existing, DATA)
    save_comm('mkt-christ', '1john', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 John mkt-christ: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
