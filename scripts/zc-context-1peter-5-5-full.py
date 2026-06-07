"""
mkt-context layer — 1 Peter chapter 5 (all 14 verses)
Output: data/commentary/mkt-context/1peter.json
Run: python3 scripts/zc-context-1peter-5-5-full.py

Setting: The letter closes with instructions to elders, the younger generation, the whole
community (humility under God's hand, resistance of the devil), a doxology, a travelogue
note identifying Silas as amanuensis and Mark as co-laborer, and the 'Babylon' (Rome)
greeting from the co-elect community there. The closural conventions follow standard
Pauline epistolary practice.
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
    # INTENT: Merge new verse entries without overwriting already-present keys — safe to re-run.
    # CHANGE? If commentary JSON structure changes from {ch:{v:html}}, update this traversal.
    # VERIFY: Re-running the script should produce identical output.
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

NEW_DATA = {
  "5": {
    "1": "<p>'To the elders among you, I appeal as a fellow elder (<em>sympresbyteros</em>) and a witness of Christ's sufferings who also will share in the glory to be revealed' — Peter's self-designation as <em>sympresbyteros</em> (co-elder) rather than apostle (<em>apostolos</em>) is a deliberate rhetorical choice: appealing as a peer carries more relational weight than commanding as a superior. The title 'witness of Christ's sufferings' (<em>martys tōn tou Christou pathēmatōn</em>) identifies Peter as an eyewitness of the passion narrative — a distinctive credential. In Asia Minor, elders were the recognized community leaders: the Jewish synagogue institution of <em>zaqenim</em> (elders) was adapted into the Christian community structure, with elders exercising oversight, teaching, and pastoral authority.</p>",
    "2": "<p>'Be shepherds of God's flock that is under your care, watching over them — not because you must, but because you are willing, as God wants you to be; not pursuing dishonest gain, but eager to serve' — the shepherd (<em>poimainō</em>) and overseer (<em>episkopountes</em>) roles combine to form the pastoral-episcopal function. Peter's triple positive-negative contrast (willing not compelled; eager to serve not greedy; examples not lords) addresses three actual failure modes of community leadership in the ancient world: compelled compliance (leaders pressed into service reluctantly), financial exploitation (the patron-client system gave leaders leverage over clients' resources), and hierarchical domination. The 'God's flock' designation frames the elders' authority as stewardship — they manage what belongs to God, not to themselves.</p>",
    "3": "<p>'Not lording it over those entrusted to you, but being examples to the flock' — <em>katakyrieuntes</em> (lording it over) is the same compound that Jesus uses in Mark 10:42-43 (the rulers of the Gentiles lord it over them... not so with you). The contrast between Gentile hierarchical domination and servant-leadership defines the community's leadership model. The 'examples' (<em>typoi</em>) — the leaders who model the life they call others to — is the Pauline and Petrine pedagogy: leadership through embodiment rather than command (cf. Phil 3:17: join in imitating me, brothers; 1 Cor 11:1: imitate me as I imitate Christ).</p>",
    "4": "<p>'And when the Chief Shepherd (<em>archipoimenos</em>) appears, you will receive the crown of glory that will never fade away' — <em>archipoimenos</em> (Chief Shepherd, head shepherd) is a NT hapax and evokes the LXX shepherding imagery for God (Ps 23:1; Isa 40:11; Ezek 34:11-16). The appearance (<em>phanerōthentos</em>) of the Chief Shepherd is the parousia — the return of Christ. The 'crown of glory that will never fade' (<em>ton amarantinon tēs doxēs stephanon</em>) uses the same root as <em>amaranton</em> (unfading) applied to the inheritance in 1:4. The <em>stephanos</em> (wreath-crown) was the athletic and civic crown awarded at festivals; Peter's eschatological crown surpasses all such civic honors.</p>",
    "5": "<p>'In the same way, you who are younger, submit yourselves to your elders. All of you, clothe yourselves with humility toward one another, because 'God opposes the proud but shows favor to the humble'' — the 'in the same way' (<em>homoiōs</em>) connects the younger members' submission to the elder-leadership pattern above and the household-code pattern of chapters 2-3. The 'clothing yourselves with humility' (<em>tēn tapeinophrosynēn egkombōsasthe</em>) uses a verb from <em>egkombōma</em>, the apron or work-garment tied on by a slave — the very garment Jesus tied on himself when he washed the disciples' feet (John 13:4-5: he tied a towel around his waist). The Prov 3:34 quotation closes the argument: the cosmic order requires humility because God himself opposes pride.</p>",
    "6": "<p>'Humble yourselves, therefore, under God's mighty hand, that he may lift you up in due time' — the 'mighty hand of God' (<em>krataiān cheira tou theou</em>) is the Exodus formula: God's powerful hand that brought Israel out of Egypt (Exod 13:3, 9, 14, 16; Deut 3:24; 9:26). Peter applies the Exodus redemption-power to the present situation of the scattered communities: the same mighty hand that defeated Pharaoh is the hand under which they are to humble themselves. The 'due time' (<em>en kairō</em>) is the eschatological moment of reversal — the same 'appointed time' of divine action that characterizes apocalyptic expectation.</p>",
    "7": "<p>'Cast all your anxiety on him because he cares for you' — the imperative 'cast' (<em>epiripsantes</em>, aorist participle of <em>epiriptō</em>) echoes Ps 55:22 LXX (cast your burden on the LORD, and he will sustain you). The 'because he cares for you' (<em>hoti autō melei peri hymōn</em>) is the theological grounding: God's care is not incidental but constitutive of the relationship. The same verb (<em>melō</em>) appears in the disciples' fear-cry to Jesus in the storm: 'Don't you care that we are perishing?' (Mark 4:38). Peter's assurance addresses the same fear — and answers it by pointing to the God who does care, whose care was demonstrated in the resurrection.</p>",
    "8": "<p>'Be sober-minded and alert. Your enemy the devil prowls around like a roaring lion looking for someone to devour' — the 'roaring lion' (<em>leōn ōryomenos</em>) seeking prey was familiar imagery in the Psalms (Ps 22:13: roaring lions that tear their prey; Ps 7:2: or he will tear me like a lion). The devil as the adversary (<em>antidikos</em>, a legal-forensic term for the opponent in a lawsuit) who seeks to devour is the Joban Satan (<em>ha-satan</em>, the adversary/accuser) brought into the eschatological frame. The sober-mindedness (<em>nēpsate</em>) and alertness (<em>grēgorēsate</em>) are the same twin commands of eschatological preparedness that Jesus issued in Gethsemane (Mark 14:38: watch and pray that you may not enter into temptation).</p>",
    "9": "<p>'Resist him, standing firm in the faith, because you know that the family of believers throughout the world is undergoing the same kind of sufferings' — the resistance of the devil through standing firm in the faith mirrors James 4:7 (resist the devil and he will flee from you) and Eph 6:13 (stand firm and resist). The solidarity note — 'the same kind of sufferings' that the worldwide community of believers (<em>adelphis hymon en kosmō</em>, your brotherhood in the world) experiences — is a pastoral-geographic encouragement. The scattered communities in Asia Minor are not uniquely persecuted; their suffering connects them to the suffering church across the empire.</p>",
    "10": "<p>'And the God of all grace, who called you to his eternal glory in Christ, after you have suffered a little while, will himself restore you and make you strong, firm, and steadfast' — the fourfold promise (restore, make strong, firm, steadfast) is the eschatological outcome of the suffering endured. The 'God of all grace' (<em>ho theos pasēs charitos</em>) is a distinctive title that frames everything God provides — including the suffering — within the category of grace. The 'called you to his eternal glory' (<em>kalesas eis tēn aiōnion autou doxan</em>) frames the calling as telos-oriented: the purpose of the call is eschatological participation in God's own glory, which the present suffering does not negate but temporarily delays.</p>",
    "11": "<p>'To him be the power for ever and ever. Amen' — the brief doxology (<em>autō to kratos eis tous aiōnas tōn aiōnōn. amēn</em>) uses <em>kratos</em> (might, ruling power) rather than the more common <em>doxa</em> (glory) — the same term used in the Lord's Prayer doxology in later manuscripts (Matt 6:13: for thine is the kingdom and the power and the glory). The doxological close after v. 10's promise is standard Pauline and Petrine epistolary form, offering praise to the God who has been described as the one who calls, restores, and establishes. The 'Amen' is the congregational ratification of the doxology when read aloud in the house-church assembly.</p>",
    "12": "<p>'With the help of Silas, whom I regard as a faithful brother, I have written to you briefly, encouraging you and testifying that this is the true grace of God. Stand fast in it' — Silas (<em>Silouanos</em>) is almost certainly the Silvanus of the Pauline letters (1 Thess 1:1; 2 Thess 1:1; 2 Cor 1:19) and the Silas of Acts (15:22-18:5), who served as an emissary of the Jerusalem council and a Pauline mission companion. His role as amanuensis (secretary) or letter-carrier is indicated; ancient authors commonly used secretaries who had some compositional latitude, which explains the Pauline-style Greek of a letter ostensibly from an Aramaic-speaking Galilean fisherman. The summary 'this is the true grace of God' is Peter's seal on the letter's theological core.</p>",
    "13": "<p>'She who is in Babylon, chosen together with you, sends you her greetings, and so does my son Mark' — 'Babylon' is the standard Jewish and early Christian cryptonym for Rome: 4 Ezra 3:1-2, 28-31; 2 Baruch 10:1-3; Rev 14:8; 16:19; 17:5; 18:2 all use Babylon for Rome. The Roman community ('she who is in Babylon') co-sends greetings, indicating a network of communication between the Roman mother-church and the Asia Minor diaspora communities. 'My son Mark' (<em>Markos ho hyios mou</em>) is John Mark of Acts 12:12; 13:13; 15:37-39 — reconciled with Paul by the time of 2 Tim 4:11 ('Get Mark and bring him... he is helpful to me') and now described as Peter's own spiritual son, likely reflecting a close Petrine-Mark connection that the early church tradition recognized in Mark's Gospel.</p>",
    "14": "<p>'Greet one another with a kiss of love. Peace to all of you who are in Christ' — the 'kiss of love' (<em>en philēmati agapēs</em>) was the early Christian practice of the holy kiss at the assembly — also attested in Paul (Rom 16:16; 1 Cor 16:20; 2 Cor 13:12; 1 Thess 5:26). The practice had roots in both Jewish greeting customs and Greco-Roman social convention; in the Christian context it expressed the familial bond of the new community (brothers and sisters in Christ). The closing 'peace to all of you who are in Christ' (<em>eirēnē hymin tois en Christō</em>) echoes the greeting of v. 2's 'grace and peace' and functions as both a pastoral benediction and a liturgical close to the letter read in the assembly."
  }
}

if __name__ == '__main__':
    existing = load_comm('mkt-context', '1peter')
    merge_comm(existing, NEW_DATA)
    save_comm('mkt-context', '1peter', existing)
    import json as _json
    il = _json.load(open(ROOT / 'data' / 'interlinear' / '1peter.json'))
    all_ok = True
    for ch in ['5']:
        missing = set(il.get(ch, {}).keys()) - set(existing.get(ch, {}).keys())
        if missing:
            print(f'  ch {ch} STILL MISSING: {sorted(missing, key=int)}')
            all_ok = False
        else:
            print(f'  ch {ch}: complete ({len(existing.get(ch, {}))} verses)')
    if all_ok:
        print('All verses present')
