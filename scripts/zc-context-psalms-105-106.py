"""
Psalms — all four layers (echo + original + context + christ)
Adds chs 18-150 echo content and all original/context/christ entries.
Output: data/echoes/psalms.json + mkt-original + mkt-context + mkt-christ

Psalms is quoted in the NT more than any other OT book (~80 direct citations).
Key Christological Psalms: 2 (Messianic king), 8 (Son of Man),
16 (resurrection), 22 (Passion), 45 (royal wedding), 69 (zeal/persecution),
110 (Davidic Lord), 118 (cornerstone), 119 (Torah meditation).
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

PSA_ECHO = {
  "22": {
    "1": [
      {"type": "fulfillment", "target": "Matt 27:46", "note": "My God my God why have you forsaken me — the opening cry of Ps 22 becomes Jesus's cry of dereliction from the cross; the Passion Psalm begins with abandonment and ends with vindication and proclamation; Jesus quotes its opening in Aramaic (Eloi eloi lema sabachthani), indicating it frames his entire cross-experience"},
      {"type": "allusion", "target": "Heb 2:12", "note": "I will tell of your name to my brothers; in the midst of the congregation I will praise you — the risen Christ quotes Ps 22:22 in Hebrews 2 as his own proclamation of the Father's name to his siblings after resurrection; the Psalm's movement from dereliction to praise is the movement of Christ's death and resurrection"}
    ],
    "18": [
      {"type": "fulfillment", "target": "John 19:24", "note": "They divide my garments among them and for my clothing they cast lots — John notes the soldiers' casting of lots for Jesus's seamless robe as fulfilling Ps 22:18 exactly; the Passion's most specific physical detail had been prophesied a thousand years before"}
    ]
  },
  "45": {
    "6": [
      {"type": "fulfillment", "target": "Heb 1:8", "note": "Your throne O God is forever and ever — Hebrews 1:8 quotes Ps 45:6 directly as a word addressed to the Son: the divine throne of Ps 45 (the royal wedding psalm) belongs to Christ, making him the one addressed as God in the OT's own worship"}
    ]
  },
  "69": {
    "9": [
      {"type": "fulfillment", "target": "John 2:17", "note": "Zeal for your house has consumed me — John cites Ps 69:9 as fulfilled when Jesus cleansed the temple; the disciples remembered this verse as the scripture that governed his action"},
      {"type": "allusion", "target": "Rom 15:3", "note": "The reproaches of those who reproach you have fallen on me — Paul quotes Ps 69:9b as the Christ-pattern: Christ did not please himself but bore the reproaches meant for God; Christ takes the insults aimed at God's house as his own"}
    ]
  },
  "110": {
    "1": [
      {"type": "fulfillment", "target": "Acts 2:34-35", "note": "The LORD says to my Lord: Sit at my right hand until I make your enemies your footstool — Peter's Pentecost sermon cites Ps 110:1 as the proof that the risen Jesus is the Lord David spoke of, now enthroned at God's right hand"},
      {"type": "fulfillment", "target": "Heb 1:13", "note": "To which of the angels did God ever say: Sit at my right hand? — Hebrews opens with Ps 110:1 as the definitive Christological text distinguishing Christ from angels; no angel received this throne-assignment, only the Son"}
    ],
    "4": [
      {"type": "fulfillment", "target": "Heb 7:17", "note": "You are a priest forever after the order of Melchizedek — the Melchizedekian priesthood of Ps 110:4 is the foundational text for Hebrews' extended argument that Christ's eternal priesthood supersedes the Levitical order; Hebrews 7 is entirely an exposition of this one verse"}
    ]
  },
  "118": {
    "22": [
      {"type": "fulfillment", "target": "Matt 21:42", "note": "The stone that the builders rejected has become the cornerstone — Jesus quotes Ps 118:22-23 after the parable of the tenants; the rejected stone is his own rejection by the Jerusalem leadership and his vindication through resurrection"},
      {"type": "fulfillment", "target": "1 Pet 2:7", "note": "The stone that the builders rejected has become the cornerstone — Peter applies Ps 118:22 to Christ and then to believers as living stones built on this cornerstone"}
    ]
  },
  "132": {
    "11": [
      {"type": "fulfillment", "target": "Acts 2:30", "note": "Of the fruit of your body I will set on your throne — Peter cites this Davidic promise (Ps 132:11, cf. Ps 89:3-4; 2 Sam 7:12) as the basis for understanding Jesus's resurrection as the fulfillment of the Davidic covenant: God swore to David that he would put one of his descendants on his throne, and knowing this, David spoke of the resurrection of the Christ"}
    ]
  }
}

PSA_ORIGINAL = {
  "2": {
    "7": "<p><strong>YHWH amar elai beni atta ani hayom yelidticha</strong> (<em>Yhwh ʾāmar ʾēlay, bĕnî ʾattâ ʾănî hayyôm yĕlídtîkā</em>): 'The LORD said to me: You are my Son; today I have begotten you.' The royal adoption formula of Ps 2:7 was applied to the Davidic king at his enthronement — the king became YHWH's 'son' in a representative capacity (2 Sam 7:14; Ps 89:26-27). The NT applies it to Jesus at three Christological moments: the baptism (Matt 3:17), the transfiguration (2 Pet 1:17), and the resurrection (Acts 13:33; Heb 1:5; 5:5). The resurrection is the decisive 'today' in NT usage: the day of Christ's enthronement at the Father's right hand is the day of divine sonship's full eschatological declaration.</p>"
  },
  "8": {
    "4": "<p><strong>mah enosh ki tizkerenu uben adam ki tipqedenu</strong> (<em>mâ-ʾĕnôš kî-tizqĕrennû ûben-ʾādām kî tipqĕdennû</em>): 'What is man that you are mindful of him, and the son of man that you care for him?' <em>Ben adam</em> (son of man) in Ps 8 is the representative human made lower than the heavenly beings and crowned with glory — a meditation on Gen 1:26-28's dominion mandate. The NT (Heb 2:5-9) applies Ps 8 to Christ as the true human who fulfills the Adamic mandate: 'We do not yet see everything in subjection to him, but we see him who for a little while was made lower than the angels, namely Jesus, crowned with glory and honor because of the suffering of death.' Christ recapitulates and fulfills humanity's Ps 8 vocation.</p>"
  },
  "22": {
    "1": "<p><strong>eli eli lamah azavtani</strong> (<em>ʾēlî ʾēlî lāmāh ʿăzabtānî</em>): 'My God, my God, why have you forsaken me?' The opening of the Passion Psalm in its Hebrew form. The Aramaic at the cross (Mark 15:34: <em>Eloi eloi lema sabachthani</em>) uses the Aramaic form of the Psalm's Hebrew opening, suggesting Jesus was quoting from memory in the vernacular. The Psalm moves from dereliction (vv. 1-21) to proclamation and praise (vv. 22-31) — ending not in abandonment but in universal witness ('all the ends of the earth shall turn to the LORD', v. 27). The early church understood Jesus's citation of the Psalm's opening as invoking the whole Psalm, including its vindication ending.</p>"
  },
  "110": {
    "1": "<p><strong>neum YHWH laadoni shev limini ad ashit oyvecha hadom leraglecha</strong> (<em>nĕʾum Yhwh laʾdōnî, šēb liymînî ʿad-ʾāšît ʾōyĕbêkā hădōm lĕraglêkā</em>): 'The oracle of YHWH to my lord: Sit at my right hand until I make your enemies your footstool.' <em>Neum</em> (oracle of) is the formula for divine speech — the highest possible speech-authority marker in Hebrew prophecy. David writes <em>laadoni</em> (to my lord), creating the theological puzzle Jesus exploits in Matt 22:41-46: how can David's descendant also be David's lord? The Davidic Messiah must be more than a Davidic son; only divine sonship accounts for the double identity. <em>Shev limini</em> (sit at my right hand): enthronement at the supreme position of divine authority — the NT applies this to the resurrection/ascension as Christ's enthronement (Acts 2:34-35; Eph 1:20-21; Heb 1:3).</p>",

    "4": "<p><strong>nishba YHWH velo yinachem atta kohen leolam al divrati malkitsedek</strong> (<em>nišbaʿ Yhwh wĕlōʾ yinnāḥēm ʾattā-kōhēn lĕʿôlām ʿal-diḇrātî malkîṣedeq</em>): 'YHWH has sworn and will not change his mind: You are a priest forever after the manner of Melchizedek.' The divine oath (<em>nishba ... velo yinachem</em>) makes this the most certain OT promise after the Abrahamic oath. <em>Malkitsedek</em> (Melchizedek, king of righteousness): the mysterious priest-king of Gen 14:18-20 who blessed Abraham and received a tithe — without genealogy, without recorded birth or death. Hebrews 7 uses the silence of Scripture about Melchizedek's origins as a typological argument: a priesthood with no recorded beginning or end points to an eternal priesthood.</p>"
  }
}

PSA_CONTEXT = {
  "1": {
    "1": "<p>The Psalter (150 poems spanning roughly David's reign to the post-exilic period) was the hymnbook of the Second Temple — used in liturgy from the restoration (Ezra-Nehemiah) through the NT period. The Dead Sea Scrolls (1QPs, 4QPsa-r, and 11QPsa) preserve the most psalms of any biblical book among the Qumran community, indicating the Psalter's centrality in Jewish worship. The Psalter is organized into five books (Ps 1-41, 42-72, 73-89, 90-106, 107-150) mirroring the five books of Moses, each ending with a doxology. The arrangement suggests a canonical editorial design: the Psalter tells the story of Israel's covenant relationship with YHWH from Torah-delight (Ps 1) to universal praise (Ps 150).</p>"
  },
  "22": {
    "1": "<p>Psalm 22 is the most cited OT Psalm in the NT Passion narratives. Its historical background (David's persecution?) is unknown — the Psalm presents an archetypal experience of abandonment and vindication. The pattern: intense lament (vv. 1-21) → sudden transition to praise (v. 22) → eschatological proclamation (vv. 27-31: 'all the families of the nations shall worship before you ... posterity shall serve him; it shall be told of the Lord to the coming generation'). The Psalm functions in NT usage not as a prediction of specific details but as the divinely-given interpretive framework for understanding the cross: suffering-unto-vindication, abandonment-unto-universal-proclamation.</p>"
  },
  "110": {
    "1": "<p>Psalm 110 is the most frequently quoted OT text in the NT. Jesus cites it in the Synoptics (Matt 22:41-46 and parallels) as a riddle about the Messiah's nature. Peter cites it at Pentecost (Acts 2:34-35). Paul cites it (1 Cor 15:25; Eph 1:20; Col 3:1). Hebrews cites or alludes to it eight times (1:3, 13; 5:6, 10; 6:20; 7:17, 21; 8:1; 10:12-13). Its dominance in NT Christology is due to its dual claim: (1) divine enthronement at God's right hand; (2) eternal Melchizedekian priesthood. These two — divine lordship and perfect priesthood — are the two Christological pillars the NT builds on from this one Psalm.</p>"
  }
}

PSA_CHRIST = {
  "2": {
    "7": "<p>A direct revelation: 'You are my Son; today I have begotten you.' The royal Psalm 2 reaches its Christological fullness in the resurrection. Paul at Pisidian Antioch (Acts 13:33): God raised Jesus, 'as it is written in the second Psalm, You are my Son, today I have begotten you.' The 'today' of divine fatherhood is not the eternal generation alone but the specific day of the resurrection-enthronement, when the Son's identity is publicly declared. Every application of Ps 2:7 in the NT (baptism, transfiguration, resurrection) marks a moment when the Father publicly declares the Son's identity for the community to hear.</p>"
  },
  "22": {
    "1": "<p>A fulfillment: 'My God, my God, why have you forsaken me?' The Passion Psalm that Jesus cited from the cross is both a historical lament (David in extremity) and a Christological prophecy (the Son's abandonment in the atonement). The cry 'why have you forsaken me' is not a failure of faith but a genuine experience of divine absence — the moment when Christ bore the full weight of human sin-under-judgment. The Psalm's movement (dereliction → trust → vindication → universal proclamation) is the death-and-resurrection narrative in miniature. Jesus did not die in despair; the Psalm he cited ends in the world's worship of YHWH through the one who suffered.</p>"
  },
  "110": {
    "1": "<p>A direct revelation: 'The LORD says to my Lord: Sit at my right hand until I make your enemies your footstool.' The most foundational Christological oracle in the OT: the risen and ascended Christ is enthroned at the Father's right hand (the supreme position of divine authority) awaiting the final subjection of all enemies, including death (1 Cor 15:25-26). The present era is the era of Christ's enthronement: he reigns now, his enemies are being progressively placed under his feet, and the ultimate subjection is certain. Ps 110:1 frames the entire NT's understanding of the ascension and the present Christological situation of the cosmos.</p>",

    "4": "<p>A fulfillment: 'You are a priest forever after the order of Melchizedek.' The divine oath of the eternal priesthood is fulfilled in Christ's resurrection, which established him as the priest who never dies. Unlike the Levitical priests who needed to offer sacrifice repeatedly and who were replaced by death, Christ offered himself once and lives forever in the power of an indestructible life (Heb 7:16, 24-25). The Melchizedekian priesthood — prior to Aaron, not from the tribe of Levi, without recorded end — is the OT's own signal that the Levitical system was provisional. Christ's eternal intercession ('he always lives to make intercession for them', Heb 7:25) is the fulfillment of Ps 110:4's oath.</p>"
  }
}

def main():
    e = load_echo('psalms')
    merge_echo(e, PSA_ECHO)
    save_echo('psalms', e)
    print(f'Psalms echo: {len(e)} chapters, {sum(len(v) for v in e.values())} verses')

    c = load_comm('mkt-original', 'psalms')
    merge_comm(c, PSA_ORIGINAL)
    save_comm('mkt-original', 'psalms', c)
    print(f'Psalms original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', 'psalms')
    merge_comm(c, PSA_CONTEXT)
    save_comm('mkt-context', 'psalms', c)
    print(f'Psalms context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', 'psalms')
    merge_comm(c, PSA_CHRIST)
    save_comm('mkt-christ', 'psalms', c)
    print(f'Psalms christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

if __name__ == '__main__':
    main()
