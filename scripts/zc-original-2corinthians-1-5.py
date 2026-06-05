"""
mkt-original layer — 2 Corinthians all 13 chapters
Output: data/commentary/mkt-original/2corinthians.json

2 Corinthians is Paul's most rhetorically complex letter —
a sustained self-defense using the Corinthian 'super-apostles' as foils.
Key philological zones: the new covenant (ch3), reconciliation (ch5),
the 'thorn in the flesh' (ch12), and Paul's fool's speech (ch11).
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
    "20": "<p><strong>hosai gar epanggeliai theou en auto to nai</strong> (<em>hosai gar epangeliai theou, en autō to Nai</em>): 'For all the promises of God find their Yes in him.' The singular <em>Nai</em> (Yes) is Christ's own covenant-faithfulness (<em>pistis Christou</em> in its broadest register): the entirety of OT promise — Abrahamic, Mosaic, Davidic, prophetic — is ratified in one person. Paul uses the Greek <em>Nai</em> and its Aramaic cognate <em>Amen</em> as bookends: to the Yes in Christ, believers add the Amen through him to the glory of God. The liturgical shape (Christ-Yes → congregation-Amen) points to the eucharistic and corporate dimensions of this affirmation.</p>"
  },
  "2": {
    "14": "<p><strong>to de theo charis to pantote thriambeuonti hemas en to Christo</strong> (<em>tō de theō charis tō pantote thriambeuonti hēmas en tō Christō</em>): 'Thanks be to God, who in Christ always leads us in triumphal procession.' <em>Thriambeuō</em> refers to the Roman <em>triumphus</em> — the ceremonial procession of a victorious general through Rome, with captives displayed in chains behind him. The metaphor is deliberately ambiguous: does Paul picture himself as the general leading others, or as a captive in Christ's triumphal procession? Most commentators favor the latter (captive as a trophy of grace) which fits Paul's paradoxical weakness-theology throughout 2 Corinthians. The 'aroma of Christ' (<em>osme Christou</em>, v. 15) echoes the incense burned during a Roman triumph.</p>"
  },
  "3": {
    "6": "<p><strong>ho de gramma apoktennei to de pneuma zoopoiei</strong> (<em>ho de gramma apoktennei, to de pneuma zōopoiei</em>): 'the letter kills, but the Spirit gives life.' <em>Gramma</em> (letter/writing) refers not to the literal-vs-spiritual sense of Scripture but to the Mosaic covenant in its external, inscribed form — the same covenant Paul calls a 'ministry of death' (<em>diakonia tou thanatou</em>, v. 7) not because Torah is evil (cf. Rom 7:12: the law is holy, righteous, and good) but because it cannot provide the Spirit that enables fulfillment. The contrast is old covenant (<em>palaia diatheke</em>, v. 14) vs new covenant (<em>kaine diatheke</em>, v. 6), not text vs allegory.</p>",

    "18": "<p><strong>ten auten eikona metamorphoumetha apo doxes eis doxan</strong> (<em>tēn autēn eikona metamorphoumetha apo doxēs eis doxan</em>): 'we are being transformed into the same image from one degree of glory to another.' <em>Metamorphoō</em> (transform/transfigure) is the same word used for the Transfiguration (Matt 17:2; Mark 9:2) and Rom 12:2 (do not be conformed to this world, but be transformed by the renewing of your mind). The transformation is: (1) into the image of Christ (<em>eikon</em>); (2) progressive (from glory to glory); (3) mediated by the Spirit (<em>apo Kyriou Pneumatos</em>). The eschatological glorification (Rom 8:30) is already underway in the present — theosis-language without the ontological merger of later traditions.</p>"
  },
  "4": {
    "7": "<p><strong>echomen de ton thesauron touton en ostrakinois skeuesin</strong> (<em>echomen de ton thēsauron touton en ostrakinois skeuesin</em>): 'we have this treasure in clay jars.' <em>Ostrakinos</em> (earthen/clay) is the material of the most common, cheapest, most breakable pottery — cheap oil lamps, storage vessels, disposable containers. The treasure (the gospel of the glory of God in Christ) is disproportionately housed in the most fragile containers possible. The purpose clause: 'to show that the surpassing power belongs to God and not to us.' Paul's paradox of ministerial weakness inverts all Greco-Roman honor-shame expectations about what a legitimate messenger of the gods should look like.</p>"
  },
  "5": {
    "17": "<p><strong>ei tis en Christo kaine ktisis ta archaia parelthen idou gegonen kaina</strong> (<em>ei tis en Christō, kainē ktisis; ta archaia parēlthen, idou gegonen kaina</em>): 'if anyone is in Christ, new creation (<em>kainē ktisis</em>); the old things have passed away, behold new things have come.' <em>Kainē ktisis</em> lacks a verb — it is an exclamation, not a predicate sentence: 'new creation!' The eschatological new creation of Isa 65:17-25 has erupted into the present in the person who is 'in Christ'. The aorist <em>parēlthen</em> (passed away) and perfect <em>gegonen</em> (have come and remain) frame the conversion as a realized eschatological event: the old age has definitively ended; the new age is permanently present.</p>",

    "21": "<p><strong>ton me gnonta hamartian hyper hemon hamartian epoiesen</strong> (<em>ton mē gnonta hamartian hyper hēmōn hamartian epoiēsen</em>): 'him who knew no sin he made to be sin on our behalf.' The verse is the most compressed statement of substitutionary atonement in Paul. <em>Hamartian epoiesen</em> — 'made sin': not a sinner, not a sin offering (though that interpretation has ancient support; LXX uses <em>hamartia</em> for sin-offering in Lev 4-6), but 'sin' itself in its concentrated reality. The exchange: he became what we are (sin-bearers), so that in him we might become what he is (the righteousness of God). The prepositional phrase <em>hyper hemon</em> (on behalf of us) carries the weight of substitution throughout Paul's atonement-theology (cf. Gal 3:13; Rom 8:32).</p>"
  },
  "11": {
    "5": "<p><strong>ton hyperlian apostolon</strong> (<em>tōn hyperlian apostolōn</em>, 'the super-apostles'): Paul's ironic designation for the itinerant missionaries who had infiltrated the Corinthian church claiming superior status (visions, letters of recommendation, impressive personal appearance, powerful rhetoric). The term <em>hyperlian</em> ('exceedingly great') is Paul's sneer-construction: these self-commending <em>apostoloi</em> compete on the Greco-Roman honorific terms Paul refuses to use. His 'fool's speech' (11:16-12:10) deliberately mimics their boasting — then inverts it by boasting only in weakness, suffering, and the thorn in the flesh.</p>"
  },
  "12": {
    "9": "<p><strong>arkei soi he charis mou he gar dynamis en astheneia teleitai</strong> (<em>arkeî soi hē charis mou, hē gar dynamis en astheneia teleitai</em>): 'My grace is sufficient for you, for my power is made perfect in weakness.' This is the only recorded direct speech of the risen Christ to Paul outside the Damascus road and Acts (cf. 18:9-10 for a similar vision-word). <em>Teleitai</em> (is brought to completion/perfection) — the power reaches its <em>telos</em> when weakness provides no competition. <strong>skolops te sarki</strong> (<em>skólops tē sarki</em>, 'thorn in the flesh'): <em>skolops</em> means a stake or pointed object — more severe than 'thorn'; the 'messenger of Satan' (<em>angelos satana</em>) frames it as a demonically-mediated affliction that God uses for Paul's sanctification.</p>"
  }
}

def main():
    existing = load_comm('mkt-original', '2corinthians')
    merge_comm(existing, ORIGINAL)
    save_comm('mkt-original', '2corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'2 Corinthians mkt-original: {len(existing)} chapters, {total} verses.')

if __name__ == '__main__':
    main()
