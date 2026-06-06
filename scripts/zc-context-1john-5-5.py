"""
MKT Context Commentary — 1 John chapter 5
Run: python3 scripts/zc-context-1john-5-5.py

Source data used:
- data/interlinear/1john.json
- data/translation/draft/mediating/1john.json
- data/commentary/mkt-context/1john.json (existing entries incl. chs 1-4)

Historical setting: same as chs 1-4 (Johannine community, Ephesus, ca. 85-95 CE).
Ch 5 introduces the three-witness structure (Spirit, water, blood) in response to
Cerinthian Christology, addresses prayer and the sin-unto-death question, and closes
with the community's three "we know" affirmations (vv. 18-20).

Key decisions:
- "water and blood" (v.6): anti-Cerinthian — the historical crucifixion (blood),
  not just the baptism (water alone), defines the Christ-event
- Three witnesses (vv.7-8): Deut 19:15 juridical background; Spirit = inward witness,
  water + blood = historical events
- "sin unto death" (v.16): likely apostasy (deliberate rejection of the incarnate
  Christ), not an individual moral lapse; no parallel in OT sin-categories
- "One born of God keeps them safe" (v.18): referent = Christ, not the believer
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

JOHNI_CH5 = {
  "5": {
    "1": '<p>The belief-criterion ("everyone who believes that Jesus is the Christ is born of God") is the anti-Cerinthian confession in its most compressed form: the human name Jesus is identical with the divine title Christ. Cerinthus (Irenaeus Haer. 1.26.1) separated the earthly Jesus from the heavenly Christ-spirit, which descended at baptism and departed before the crucifixion. John insists the two are one person: believing that Jesus is the Christ is the criterion of new birth, and those who separate them — as the secessionists do — demonstrate by that very separation that they have not been born of God. The love-logic of the verse (loving the parent entails loving the children) grounds the community\'s mutual love in their shared divine parentage.</p>',
    "2": '<p>The mutual-verification structure of the Johannine ethics surfaces here in its reverse form: ordinarily, love of the visible brother verifies love of the invisible God (4:20-21); here, love of God and obedience to his commands verify love of the children of God. The coherence is not circular but systemic — love of God, love of neighbor, and obedience to commands are a unified pattern whose presence is mutually confirming and whose absence in any part exposes the whole as deficient. This directly addresses the secessionists whose ethical indifference (toward the community members they left) contradicts their claim to love God.</p>',
    "3": '<p>The anti-heavy-burden claim echoes Jesus\' "my yoke is easy and my burden is light" (Matt 11:30). In the context of Second Temple Judaism, there was debate about which commandments were "light" (<em>qalot</em>) and which "heavy" (<em>chamuroth</em>) (Mishnah Avot 2:1), and the Pharisaic tradition had developed an extensive interpretive fence around the Torah. The Johannine claim is not that the commands are few or simple, but that they are not burdensome because they flow from love rather than external obligation: the one born of God (v. 4) keeps the commands naturally, as the expression of a transformed nature, not as external legal imposition.</p>',
    "4": '<p>Victory language (<em>nike</em>/<em>nikao</em>) had currency in both Jewish apocalyptic (the war between God\'s forces and the forces of darkness: Qumran War Scroll 1QM) and in the Roman imperial world (Nike as the goddess of victory, pervasive on coins and monuments throughout the empire). John\'s community, socially marginalized in Roman Ephesus, participates in a victory already accomplished. The aorist participle "the one that has overcome the world" (<em>nikesasa ton kosmon</em>) is past tense: the decisive victory has already occurred in Christ\'s cross and resurrection, and faith is the means by which the community appropriates and lives from that accomplished victory.</p>',
    "5": '<p>The confession "Jesus is the Son of God" again anchors overcoming faith to the specific Christological identity of the one who came by water and blood (v. 6). The Cerinthian position — affirming a heavenly Christ while relativizing the human Jesus — could not produce the faith that overcomes the world, because the world-overcoming faith is trust in the one who entered the world fully and suffered its worst (the crucifixion). The rhetorical question "who is it?" emphasizes that no alternative Christology produces genuine overcoming: only the faith in the fully incarnate Son of God has the content capable of sustaining the community\'s endurance against the world\'s opposition.</p>',
    "7": '<p>The juridical framework (witnesses testifying to establish a truth claim) is deeply Jewish: Deuteronomy 19:15 required two or three witnesses to establish any matter in court. Early Christianity applied this requirement to the confirmation of truth claims (Matt 18:16; 2 Cor 13:1; John 8:17-18 — Jesus citing the two-witness law to validate his self-testimony). John provides three witnesses — Spirit, water, and blood — collectively establishing the testimony about Jesus as adequately attested. The implied setting is a kind of divine court in which the secessionists have brought an alternative Christology and the apostolic community presents its three-fold testimony in rebuttal.</p>',
    "8": '<p>The three agree in one: Spirit, water, and blood as converging witnesses. The Spirit\'s witness is internal to the community — the Paraclete-role of John 14:26, 15:26, and the anointing of 1 John 2:27, which teaches the community inwardly and authenticates the apostolic proclamation. Water and blood are the historical events of the Christ: baptism (the Spirit\'s descent and the Father\'s public testimony, Mark 1:11) and crucifixion (the blood that constitutes the atonement and the new covenant). Against Cerinthus, who affirmed the water (the Spirit\'s descent at baptism) but not the blood (the crucifixion as Christ\'s act), John insists on both historical events as constitutive of the Christ-event.</p>',
    "9": '<p>The a-fortiori argument: if two or three human witnesses legally establish a fact (Deut 19:15), how much more does God\'s testimony establish it? Roman law relied heavily on witness testimony (<em>testis</em>) for establishing facts; the Mishnah (Sanhedrin 5:1-4) regulated testimony extensively. The divine testimony is "greater" not merely because of its source (divine vs. human) but because it is triple and convergent (Spirit, water, blood). The secessionists\' counter-claim — their alternative Christology — is one human construction against a three-fold divine testimony. The epistemological advantage lies entirely with the apostolic community.</p>',
    "10": '<p>The internal reception of the testimony ("in themselves") is the subjective side of the objective testimony: the Spirit within the community member personally witnesses to the truth of Jesus\' identity, so that believing the Son means having the testimony confirmed inwardly. Rejecting this testimony — as the secessionists do by their alternative Christology — is characterized as "calling God a liar" (echoing 1:10). This is not hyperbole but a specific accusation: the secessionists\' Christological revision implicitly contradicts the divine testimony about the Son, placing them in the position of judging God\'s own self-testimony as inadequate or misleading.</p>',
    "11": '<p>The content of the divine testimony is identified precisely: God has given us eternal life, and this life is in his Son. The locating of life specifically in the Son directly counters any Gnostic or Cerinthian arrangement in which eternal life is accessed through gnosis, mystical experience, or a divine principle apart from the historical Jesus. Life is inseparable from the person — you cannot have the life without having him. This is the Johannine equivalent of Acts 4:12 ("salvation is found in no one else") applied to the specific controversy: the secessionists\' Christ-without-the-full-Jesus is a Christ who cannot communicate the life God has given in the Son.</p>',
    "12": '<p>The exclusive either/or (Son = life; no Son = no life) directly addresses the community situation: the secessionists who have departed from the Johannine community\'s Christological confession no longer "have the Son" in John\'s sense — they have redefined him in a way that severs the divine Christ from the human Jesus. Their alternative Christology, however sophisticated, cannot communicate the life that is in the Son, because the life is not in a doctrine about Christ or a spiritual Christ-principle but in the person who came by water and blood. The starkness of the either/or is proportional to the stakes of the controversy.</p>',
    "13": '<p>The stated purpose of the letter is assurance for those who have believed and remained: "so that you may know that you have eternal life." The Johannine community has been destabilized by the secessionists\' claims — those who departed may have seemed to have superior spiritual knowledge, making those who remained wonder if they had missed something important. John\'s pastoral strategy is not to introduce new arguments but to confirm what the community already has: they believe in the authentic name of the Son of God, which is the criterion for having eternal life. The "knowing" (<em>eidete</em>) is settled, assured knowledge, not anxious uncertainty.</p>',
    "15": '<p>The confidence that God hears prayer according to his will (v. 14) grounds the further confidence that what has been asked is already received. This anticipatory assurance of answered prayer has Jewish precedent: the Rabbinic concept of prayer as already answered when offered in faith (b. Berakhot 34b). In the Hellenistic world, petitionary prayer to the gods (<em>euchai</em>) was understood as a request that might or might not be granted depending on the deity\'s favor; John\'s framework is different — prayer within God\'s will is already effective because it aligns with the divine purpose. The specific application in v. 16 (praying for a sinning brother) demonstrates that the assurance is communally applied.</p>',
    "17": '<p>The clarification that all wrongdoing is sin — against any proto-Gnostic position that spiritual persons are above moral categories — is paired with the recognition that not all sin leads to death. The distinction may draw on the OT distinction between intentional and unintentional sins: Numbers 15:27-31 contrasted sins committed inadvertently (for which atonement was available) with sins committed with a "high hand" (deliberate defiance of God, for which there was no prescribed atonement). In the community context, the "sin unto death" likely refers to the apostasy of the secessionists: the deliberate, knowing abandonment of the confession of the incarnate Christ, for which no intercessory prayer is commanded.</p>',
    "18": '<p>The "One who was born of God" (<em>ho gennetheis ek tou theou</em>) who keeps the community member safe is best read as Christ — the uniquely born-of-God Son who protects those born of God. The grammar distinguishes the two: one who has been born of God (the community member) does not continue to sin, and the one born of God (Christ, the unique Son) keeps them safe. This is a pastoral reassurance for a community under attack from false teaching: the Son himself is the guardian of those who belong to him, not merely through their own moral vigilance, but through his active protection against the evil one\'s inroads.</p>',
    "19": '<p>The cosmic dualism (children of God vs. the whole world under the evil one) echoes the Qumran Two Spirits doctrine (1QS 3-4) and the broader Jewish apocalyptic framework in which two powers contend for humanity\'s allegiance. In the immediate context, the "world" under the evil one is the socio-intellectual environment — the culture of Ephesus, the imperial cult, the Hellenistic philosophical atmosphere — that the secessionists have aligned themselves with (4:5: "they are from the world"). The community\'s different orientation (children of God) is not merely a moral preference but a cosmic relocation: they have been born out of the world\'s domain and into the domain of the one who keeps them (v. 18).</p>'
  }
}

def main():
    existing = load_comm('mkt-context', '1john')
    merge_comm(existing, JOHNI_CH5)
    save_comm('mkt-context', '1john', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 John mkt-context ch 5: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
