"""
MKT Christ Commentary — Hebrews chapters 1–5
Run: python3 scripts/zc-christ-hebrews-1-5.py

Key decisions:
- 1:1-4 prologue: "A direct revelation:" — the Son as God's final word is itself the Christological claim
- 1:5 Ps 2:7 + 2 Sam 7:14: "A fulfillment:" — the Son's exaltation fulfills what both texts promised
- 1:14 angels as servants: "A revelation of God:" — the angelic system reveals the Son's supremacy
- 2:6-9 Ps 8: "A fulfillment:" — Jesus as the fulfillment of the human-destiny-in-Ps-8
- 2:17 high priest: "A type:" — Aaronic high priesthood is the institutional type
- 3:1-6 Moses comparison: "A type:" — Moses as the shadow whose house-building is surpassed
- 4:14-16 sympathy of high priest: "A direct revelation:" — the incarnate Son's tested compassion
- 5:5-6 divine appointment: "A fulfillment:" — Ps 2:7 and Ps 110:4 applied to Christ's priesthood
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

HEBREWS = {
  "1": {
    "1": '<p>A direct revelation: in these last days God has spoken in his Son. The prologue of Hebrews presents the incarnation as God\'s decisive, climactic, definitive self-disclosure — not one more prophetic word added to a series but the final word in a new mode. All prior revelation was real but partial; the Son is not more of the same but qualitatively different. This is a direct revelation of the Triune God: the Father speaks, the Son is the speech, the Spirit has spoken through the prophets (Heb 9:8; 10:15). The entire subsequent argument of Hebrews unfolds what it means that God has spoken in a Son — the Son\'s identity (ch1), humanity (ch2), faithfulness (ch3), rest-giving (ch4), and priesthood (chs5-10) are all the content of this final speaking.</p>',
    "2": '<p>A direct revelation: the Son, through whom God made the worlds and who upholds all things, is the heir of all things. The creation-agency and cosmic-sustaining role disclosed in the Son identifies him as the one who was present at the beginning and who holds the creation together at every moment. This is not a revelation of something other than God but of God himself in his Son: the creator who entered creation, the upholder who became creature, the heir who has already received what was always his by divine appointment.</p>',
    "3": '<p>A direct revelation: the Son is the radiance of God\'s glory and the exact imprint of his nature. The Christological claim of the prologue reaches its height here: to see the Son is to see the Father\'s glory; to know the Son\'s character is to know the Father\'s substance. The purification of sins accomplished by the Son and the session at the right hand are the historical-eschatological events in which this identity is enacted — the creator who became human, made purification, and was enthroned, all in one sweep of history.</p>',
    "5": '<p>A fulfillment: God\'s words to the Son — "You are my Son; today I have begotten you" (Ps 2:7) and "I will be his Father, and he shall be my Son" (2 Sam 7:14) — are fulfilled in the exaltation of the crucified and risen Jesus. The Psalm 2 royal coronation finds its ultimate referent not in any Davidic king but in the Son who is raised from the dead and exalted to the right hand. The 2 Samuel 7 Davidic covenant promise finds its definitive fulfillment not in Solomon but in the Son of God who is over God\'s house forever. The double citation establishes the resurrection-exaltation as the moment when what was always true of the Son was openly declared and enacted in human history.</p>',
    "13": '<p>A fulfillment: "Sit at my right hand until I make your enemies a footstool for your feet" (Ps 110:1) — the exalted Christ fulfills the Davidic Lord\'s session. No angel has ever received this invitation; the Son alone is the referent of this Psalm\'s second-person address. The session is the evidence that the atonement is complete (no work remains to be done; he sat down), that the kingdom is inaugurated (the Son reigns from the right hand of the Majesty), and that the enemies\' subjugation is certain (until = active waiting for the eschatological completion of what the resurrection began).</p>'
  },
  "2": {
    "3": '<p>A direct revelation: the salvation announced by the Lord himself, attested by eyewitnesses, confirmed by signs and gifts of the Holy Spirit — this is the Trinitarian structure of the gospel\'s authentication. The Lord Jesus announced it; those who heard him testified; God confirmed it through the Spirit\'s distribution of gifts according to his will. The neglect of so great a salvation is therefore a neglect of the Triune God\'s own testimony about his Son.</p>',
    "9": '<p>A fulfillment: "we see him who for a little while was made lower than the angels, namely Jesus, crowned with glory and honor because of the suffering of death." The Psalm 8 vision of the human figure crowned with glory is fulfilled in the specific history of Jesus — the humiliation (crucifixion) and the exaltation (resurrection-crown). The general human destiny described in Ps 8 (dominion over creation) is actualized in the particular human being Jesus who, by tasting death for everyone, secures for all who are in him the Psalm 8 glory that was their created destiny. Creation\'s goal (human dominion) is achieved through the crucified and risen Son.</p>',
    "14": '<p>A direct revelation: through death he destroyed the one who has the power of death, that is, the devil, and delivered all those who through fear of death were subject to lifelong slavery. The Incarnation was purposive — not accidental but aimed at destroying the devil\'s death-dominion through participation in death itself. This is the paradox of the atonement: the one who is Life enters death to unmake it from within. The resurrection is not just the Son\'s personal vindication but the destruction of the enslaving power that death held over all humanity.</p>',
    "17": '<p>A type: the Aaronic high priest — chosen from among humans, offering for sins, able to sympathize because he himself is weak — is the OT institutional type whose characteristics are fulfilled and surpassed in Christ. The type reveals what the antitype will be: a priest who is genuinely human (made like his brothers in every respect), who propitiates for sins (makes atonement), and who can sympathize (merciful and faithful). But Christ exceeds the type in key dimensions: he is without sin (no self-offering needed), and his offering is himself (not animals). The type preserves the structure; the antitype perfects it.</p>'
  },
  "3": {
    "1": '<p>A direct revelation: Jesus is the apostle and high priest of our confession. Two offices — the one sent from God (apostle: the divine messenger) and the one who stands before God for humans (high priest: the human representative) — are united in a single person. This double-office Christology is the key to Hebrews\' entire argument: only the one who is both from God and for humanity can be the mediator of the new covenant. The community\'s confession centers on this person.</p>',
    "5": '<p>A type: Moses was faithful as a servant in God\'s house, testifying to the things that were to be spoken later — to the things that Christ would speak and be. Moses is not merely a historical predecessor but a typological pointer: his faithful service in the house was the anticipatory testimony to the one who would be over the house as Son and Builder. Moses\'s entire Levitical-covenantal institution was the form of the testimony; Christ is its content.</p>',
    "6": '<p>A direct revelation: Christ is faithful over God\'s house as Son, and we are his house if we hold fast. The ecclesiology is Christological: the church is defined as the Son\'s household, the community over which the Son reigns and for which he has made purification. The conditional ("if we hold fast") is not an undermining of certainty but the description of what belonging to the Son\'s house looks like — bold confidence in hope rather than drift and unbelief.</p>'
  },
  "4": {
    "3": '<p>A type: God\'s resting on the seventh day (Gen 2:2) is the primordial type of the divine rest into which believers are invited to enter. The creation Sabbath is not merely the weekly day of rest but the pattern of the eschatological participation in God\'s own completed-work rest. Faith enters into what God completed at creation; the wilderness generation\'s failure was their refusal to enter what had been available since the foundation of the world. Christ opens the way into the rest that the creation Sabbath established as the pattern and goal.</p>',
    "14": '<p>A direct revelation: we have a great high priest who has passed through the heavens, Jesus the Son of God. The twofold identity — "Jesus" (his human name, bearer of the human condition) and "Son of God" (his divine identity) — defines the mediator who has already crossed the threshold of the heavenly sanctuary on the community\'s behalf. His passing through the heavens is not his departure from the community but his entry into the heavenly holy of holies where he intercedes for them.</p>',
    "15": '<p>A direct revelation: we have a high priest who is not unable to sympathize with our weaknesses, having been tested in every respect as we are, yet without sin. The sympathy of the Son is not generic divine knowledge of human experience but the specific, lived acquaintance with weakness and temptation that the incarnation gives him. The "yet without sin" is not a distance but a completion — the test was real, and the faithfulness was real; having endured every test, he can help those being tested from within the experience of having gone through them.'
  },
  "5": {
    "5": '<p>A fulfillment: God glorified Christ by saying "You are my Son; today I have begotten you" (Ps 2:7) — the divine appointment of the Son to high-priestly office fulfills what the royal-sonship psalm anticipated. The crucified-and-risen Jesus is recognized by God as the Son at the moment of his exaltation; the Psalm\'s "today" is the day of the resurrection-exaltation, the inaugural day of the new priestly order.</p>',
    "6": '<p>A fulfillment: "You are a priest forever, according to the order of Melchizedek" (Ps 110:4) — the priest-forever promised by divine oath is fulfilled in Jesus whose indestructible resurrection life grounds an eternal priesthood. The Psalm\'s promise of a non-Levitical, oath-backed, eternal priesthood points forward to the one whose death and resurrection constitute the qualitatively different basis of priestly access. Melchizedek was the shadow; Christ is the substance — the king of righteousness and peace who is priest forever by divine oath.</p>',
    "8": '<p>A direct revelation: although he was a Son, he learned obedience through what he suffered, and being made perfect he became the source of eternal salvation. The incarnate Son\'s pathway of suffering-to-completion is not the story of a merely human figure becoming more than he was, but the revelation of how the divine Son accomplished from within human experience what redemption required. The obedience he learned is the obedience he now is — having walked the path of faithful submission to the Father through suffering, he is the source of the same salvation for all who obey him.</p>',
    "10": '<p>A fulfillment: designated by God as high priest according to the order of Melchizedek — the Ps 110:4 oracle\'s fulfillment frames the entire high-priestly Christology that Hebrews 5:1-10 introduces and chs. 7-10 elaborate. The Melchizedekian designation is not a new institution but the fulfillment of what the Genesis 14 figure and the Psalm 110 promise had held out as the type and anticipation of the definitive high priest.'
  }
}

def main():
    existing = load_comm('mkt-christ', 'hebrews')
    merge_comm(existing, HEBREWS)
    save_comm('mkt-christ', 'hebrews', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Hebrews mkt-christ: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
