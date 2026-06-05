"""
MKT Christ Commentary — Hebrews chapters 6–9
Run: python3 scripts/zc-christ-hebrews-6-9.py

Key decisions:
- 6:13-18 Abraham's oath: "A shadow:" — divine self-swearing as the type of Christ's priestly oath
- 7:1-3 Melchizedek: "A shadow:" — the Genesis figure's typological features
- 7:24-25 eternal priest: "A direct revelation:" — Christ's living intercession
- 7:27 once for all: "A direct revelation:" — the singular sacrifice vs. the daily repetition
- 8:1-2 seated at right hand: "A direct revelation:" — the post-atonement high-priestly session
- 8:8-13 Jer 31 new covenant: "A fulfillment:" — explicit new covenant fulfillment in Christ
- 9:11-14 Christ's blood: "A direct revelation:" — the self-offering as the true atonement
- 9:24 heaven itself: "A direct revelation:" — Christ appearing in God's presence for us
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
  "6": {
    "13": '<p>A shadow: when God swore by himself to Abraham (Gen 22:16-17), the divine self-oath was the maximum possible guarantee of the promise — the pattern pointing forward to the greater oath by which the Son was installed as eternal high priest (Ps 110:4: "The Lord has sworn and will not change his mind"). Abraham\'s blessing-oath is the shadow; the priestly oath of Ps 110:4 is the fuller expression; both together establish the certainty of what God has promised. Christ is both the content of the Abraham-promise (the seed in whom all nations are blessed, Gal 3:16) and the high priest installed by the oath that makes the new covenant irrevocable.</p>',
    "19": '<p>A direct revelation: we have a sure and steadfast anchor of the soul, a hope that enters into the inner place behind the curtain, where Jesus has gone as a forerunner on our behalf. The forerunner (<em>prodromos</em>) who has entered the heavenly sanctuary is the risen and ascended Christ, now present in God\'s presence as the community\'s representative. The anchor-hope is not wishful thinking but the certainty grounded in his actual presence there — the hope is anchored to a reality already established in heaven, not to a future possibility.'
  },
  "7": {
    "1": '<p>A shadow: Melchizedek — the king-priest without recorded genealogy, without beginning or end in the biblical narrative — prefigures the Son of God who is priest forever not by hereditary right but by the power of indestructible life. The Genesis 14 figure\'s shadowy, genealogy-free existence in the text is designed to foreshadow the one who genuinely has no end of life. Every detail of the Genesis Melchizedek narrative that Hebrews notes (name, title, textual silence about ancestry and death) is a feature of the shadow that corresponds to an antitype feature of the Son.</p>',
    "22": '<p>A direct revelation: Jesus has become the guarantor of a better covenant. The surety-Christology is remarkable: the Son does not merely announce the covenant but puts himself up as security for it — if the covenant\'s benefits are not delivered, he is liable. His death is precisely the discharge of this surety-obligation: he bore the covenant\'s curse (Gal 3:13) to secure its blessing for those who could not secure it themselves. The better covenant rests on the better guarantor whose indestructible life ensures the guarantee is permanent.</p>',
    "25": '<p>A direct revelation: Christ is able to save to the uttermost those who draw near to God through him, since he always lives to make intercession for them. The resurrection-life of the Son is not passive but active — the living high priest continuously intercedes at the Father\'s right hand. This is not a repetition of his sacrifice (which was once for all) but the ongoing application of his completed atonement: he presents himself, the one who was offered, as the basis of the community\'s continuing access. The "always lives" grounds the "to the uttermost" — the completeness of the salvation is proportionate to the permanence of the intercessor.</p>',
    "27": '<p>A direct revelation: unlike the Levitical high priests, Jesus has no need to offer sacrifices daily — first for his own sins and then for those of the people. He did this once for all when he offered himself. The singularity and self-offering are the two distinguishing marks of Christ\'s sacrifice over the entire Levitical system. Once — not annually, not repeatedly. Himself — not an animal substitute. The once-for-all self-offering is both the climax of the sacrificial theology and its abolition: it succeeds so completely that no further sacrifice is needed.'
  },
  "8": {
    "1": '<p>A direct revelation: we have such a high priest, one who is seated at the right hand of the throne of the Majesty in heaven, a minister in the holy places, in the true tent that the Lord set up, not man. The seated posture (contrast with the ever-standing Levitical priests, 10:11) declares the completed work; the right-hand position declares the divine acceptance; the heavenly ministry declares the continuing access he secures. This is the summary of the entire priestly argument: a real high priest, with a real sanctuary, doing a real ministry — but heavenly rather than earthly, completed rather than ongoing, in the true tent rather than its copy.</p>',
    "6": '<p>A direct revelation: Christ has obtained a ministry that is as much more excellent than the old as the covenant he mediates is better, since it is enacted on better promises. The better ministry and better covenant are grounded in better promises — not merely better in terms of explicitness but better in terms of the reality they deliver: the internal law (not external command), the universal God-knowledge (not mediated instruction), the complete forgiveness (not annual atonement that remembers sins). All three improvements are grounded in Christ\'s completed sacrifice and Spirit-giving.</p>',
    "8": '<p>A fulfillment: "Behold, the days are coming, declares the Lord, when I will make a new covenant with the house of Israel and the house of Judah" — the days that Jeremiah anticipated have come in Jesus. The new covenant that Jeremiah promised (internal law, complete forgiveness, universal God-knowledge) is the covenant that Jesus inaugurated with his blood (Luke 22:20: "this cup is the new covenant in my blood") and that his Spirit enacts in the community. The Jeremiah 31:31-34 citation is not merely predictive but structurally: it proves that the Mosaic covenant was designed to be temporary and that Christ\'s coming was God\'s planned fulfillment, not an improvisation.</p>'
  },
  "9": {
    "7": '<p>A shadow: the high priest going alone into the Most Holy Place once a year, not without blood which he offers for himself and for the unintentional sins of the people — the restriction, the solitude, the blood requirement, and the annual repetition are all typological features pointing to their antitypes in Christ\'s ministry. The restriction (one person per year) → fulfilled in the unique high priest whose once-for-all entry opens the way for all. The blood requirement → fulfilled in his own blood. The annual repetition → abolished by the once-for-all offering.</p>',
    "11": '<p>A direct revelation: Christ appeared as a high priest of the good things that have come, then through the greater and more perfect tent not made with hands, not of this creation — he entered once for all into the holy places, not by means of the blood of goats and calves but by means of his own blood, thus securing an eternal redemption. The four contrasts (greater tent vs. handmade tent; own blood vs. animal blood; once for all vs. annually; eternal redemption vs. temporary purification) define what the incarnation, cross, resurrection, and ascension accomplished. The "appeared" (<em>paragenomenos</em>) marks the historical event of the Incarnation as the beginning of the true high-priestly ministry that culminated in the heavenly entry.</p>',
    "24": '<p>A direct revelation: Christ has entered, not into holy places made with hands, but into heaven itself, now to appear in the presence of God on our behalf. The "now" is the present reality of the ascended Christ\'s ministry — he is presently in God\'s presence, presently appearing before the Father for the community. The community does not approach an empty throne but the presence of their high priest who is simultaneously at the right hand of God and interceding on their behalf. His appearing for them grounds the community\'s confidence to approach through him.</p>',
    "28": '<p>A direct revelation: Christ, having been offered once to bear the sins of many, will appear a second time, not to deal with sin but to save those who are eagerly waiting for him. The two appearances structure the entire Christological narrative: the first appearance was the self-offering for sin (the cross and heavenly entry); the second appearance will be the consummation-salvation of those who are waiting. Between the two appearances is the present time of high-priestly intercession (vv24-25) and the community\'s faith-endurance. The parousia is not a new atonement but the completion of the salvation that the first appearing secured.'
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
