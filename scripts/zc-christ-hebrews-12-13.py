"""
MKT Christ Commentary — Hebrews chapters 12–13
Run: python3 scripts/zc-christ-hebrews-12-13.py

Key decisions:
- 12:2 pioneer and perfecter: "A direct revelation:" — Jesus as the one who ran and won the race before us
- 12:10 share in his holiness: "A direct revelation:" — the goal of discipline as divine-character participation
- 12:22-24 heavenly assembly: "A direct revelation:" — the present eschatological community
- 12:24 better blood: "A direct revelation:" — Christ's blood vs. Abel's
- 12:26-27 unshakeable kingdom: "A fulfillment:" — Hag 2:6 fulfilled in the Christ-event
- 13:8 same yesterday, today, forever: "A direct revelation:" — Christ's eternal constancy
- 13:12 outside the gate: "A direct revelation:" — the purposive suffering of the holy sacrifice
- 13:20-21 God of peace/great shepherd: "A direct revelation:" — the resurrection benediction
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
  "12": {
    "1": '<p>A direct revelation: surrounded by so great a cloud of witnesses, let us run with endurance the race that is set before us. The community\'s race is not run in isolation but within the communion of all the faith-witnesses who have gone before — Abel, Noah, Abraham, Moses, and all the rest. Their completed testimony surrounds and encourages the current runners. The race metaphor identifies the Christian life as a contest with a defined goal, a defined course (set before us — already established by Christ\'s own completion of it), and a defined means of success (endurance: bearing the weight of suffering to the finish rather than quitting).</p>',
    "2": '<p>A direct revelation: looking to Jesus, the pioneer and perfecter of our faith, who for the joy set before him endured the cross, despising the shame, and is seated at the right hand of the throne of God. The Christian race is not run by following an abstract ideal but by fixing the gaze on a person who has already run it and completed it. Jesus is pioneer (he went first, opening the path) and perfecter (he brought faith to its completion and goal) — both the trailblazer and the finisher. His joy-despite-cross, honor-despite-shame, and current session are the revelation of what the race looks like for its participants: suffering through to glory.</p>',
    "10": '<p>A direct revelation: God disciplines us for our good, that we may share his holiness. The goal of the entire discipline-theology of ch12 is participation in the divine character — specifically in holiness. This is not merely conformity to ethical rules but ontological transformation: the disciplined community is being made to share what God is. The incarnate Son who lived the path of suffering-to-glory is the pattern; the community is being formed into his image by the same Father who formed him through the disciplines of obedience (5:8).</p>',
    "22": '<p>A direct revelation: you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem, and to innumerable angels in festal gathering, and to the assembly of the firstborn who are enrolled in heaven. The community\'s present status — not future hope but present arrival — is described in terms of the heavenly assembly they have already joined through Christ\'s ministry. The "you have come" (<em>proselelythate</em>, perfect tense) is the access already granted through Christ\'s priestly entry into the heavenly sanctuary. The community worships not in a room but in the heavenly Jerusalem, not alongside a few but in the company of myriads.</p>',
    "24": '<p>A direct revelation: Jesus, the mediator of a new covenant, and the sprinkled blood that speaks a better word than the blood of Abel. The two comparisons of ch12 converge here: the Sinai covenant vs. the new covenant (mediated by Jesus, not Moses), and Abel\'s blood (crying for vengeance) vs. Jesus\'s blood (speaking forgiveness). The "better word" that Christ\'s blood speaks is the gospel itself: not "avenge me!" but "forgive them!" The blood of the new covenant mediator is the foundation of the heavenly community\'s access and the answer to all the cries for justice that have accumulated since Abel.</p>',
    "28": '<p>A fulfillment: we are receiving a kingdom that cannot be shaken — the fulfillment of Haggai\'s promised shaking (Hag 2:6). The once-more shaking of heaven and earth that Haggai promised has been accomplished in the Christ-event (the cross-resurrection-ascension as the apocalyptic transformation of the cosmos), leaving the unshakeable kingdom as the permanent inheritance of those in Christ. The community that suffered the shaking of persecution receives instead of the shaking the unshakeable kingdom — because they belong to the one whose resurrection is the first-fruits of the unshakeable new creation.'
  },
  "13": {
    "8": '<p>A direct revelation: Jesus Christ is the same yesterday and today and forever. The eternal constancy of Christ is the Christological ground for the community\'s theological stability: the same Christ who died (yesterday) is alive and interceding (today) and will return (forever). The false teachers\' novelties are ruled out not merely by tradition but by the unchangeableness of Christ himself — he does not update his gospel or revise his person. The community that is anchored to this eternal Christ is immune to the drift that new religious fashions produce.</p>',
    "12": '<p>A direct revelation: Jesus also suffered outside the gate in order to sanctify the people through his own blood. The purposive suffering outside the gate is the revelation of the cross\'s nature: it was not accidental or merely judicial but the fulfillment of the spatial theology of the sin-offering (burned outside the camp) applied to the definitive sacrifice. To sanctify through his own blood is the full Christological claim: his blood is the means, the sanctification of the people is the goal, and his suffering outside the gate is the historical event that accomplishes both.</p>',
    "20": '<p>A direct revelation: the God of peace who brought again from the dead our Lord Jesus, the great shepherd of the sheep, by the blood of the eternal covenant — the closing benediction is a Christological compendium. God of peace: the covenant relationship restored by the atonement. Brought again from the dead: the resurrection as God\'s act. Our Lord Jesus: the human name and divine title. The great shepherd: the Ezekielian Davidic shepherd who gathers and leads God\'s flock. Blood of the eternal covenant: the atoning self-offering that inaugurates the covenant that will never be superseded. All that Hebrews has argued about the high priest, the covenant, the sacrifice, and the resurrection converges in this single ascription of praise.</p>',
    "21": '<p>A direct revelation: may the God of peace equip you with everything good that you may do his will, working in us that which is pleasing in his sight, through Jesus Christ, to whom be glory forever and ever. The closing prayer applies the entire Christological argument to the practical ethical life of the community. The equipping for good works, the doing of God\'s will, and the production of what pleases God are all "through Jesus Christ" — his high-priestly mediation grounds not only the community\'s access to God but also their ongoing moral formation. The doxology to Christ (to whom be glory forever) is the appropriate conclusion of the letter\'s sustained argument for his superiority and finality.'
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
