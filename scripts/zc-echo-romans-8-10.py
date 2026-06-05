"""
MKT Echo Layer — Romans chapters 8–10
Run: python3 scripts/zc-echo-romans-8-10.py

Source data used:
- data/translation/draft/mediating/romans.json (MKT text for ch8-10)
- data/parallels/romans.json (absorbed: 8:36 Ps 44:22; 9:7 Gen 21:12; 9:9 Gen 18:10;
  9:12 Gen 25:23; 9:15 Exod 33:19; 9:17 Exod 9:16; 9:25 Hos 2:23; 9:26 Hos 1:10;
  9:27-28 Isa 10:22-23; 9:29 Isa 1:9; 9:33 Isa 28:16 + Isa 8:14;
  10:5 Lev 18:5; 10:6-8 Deut 30:12-14; 10:11 Isa 28:16; 10:13 Joel 2:32;
  10:15 Isa 52:7; 10:16 Isa 53:1; 10:18 Ps 19:4; 10:19 Deut 32:21;
  10:20-21 Isa 65:1-2)

Key decisions in this range:
- 8:3 "in the likeness of sinful flesh, as a sin offering" — the phrase "peri hamartias"
  is the LXX technical term for sin offering (Lev 4-5); classified as type because the
  structural correspondence (substitutionary, God-provided) is the point, not a verbal quotation
- 8:32 "did not spare his own Son" — LXX Gen 22:16 uses the same verb (epheisato)
  for Abraham not sparing Isaac; classified as type (the Aqedah is the structural type)
- 9:13 "Jacob I loved, Esau I hated" — Malachi 1:2-3 quote; classified as quote
- 9:20-21 potter/clay — both Isa 29:16 / 45:9 and Jer 18:1-6 stand behind this;
  classified as allusion to both since no verbatim quotation
- 10:6-8 Deut 30:12-14 — Paul's midrashic rereading applies the "near word" to Christ's
  descent/ascent and the gospel proclamation; classified as quote with note explaining
  the Christological rereading
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

ROMANS_ECHOES = {
  "8": {
    "1": [
      {"type": "allusion", "target": "Isa 43:25", "note": "God declares 'I, even I, am he who blots out your transgressions, for my own sake' — the divine removal of guilt for which Paul now announces the full actualization in Christ: no condemnation for those in him."},
      {"type": "allusion", "target": "Ps 103:12", "note": "As far as east from west, so God removes transgressions from his people — the psalmist's declaration of comprehensive forgiveness is the OT form of Paul's 'no condemnation,' now grounded in the completed work of Christ."}
    ],
    "2": [
      {"type": "allusion", "target": "Ezek 36:27", "note": "God's promise to put his Spirit in his people 'and move them to follow my decrees' — Paul's 'law of the Spirit who gives life' is the actualization of Ezekiel's new-covenant Spirit who enables the obedience the old law could not produce."},
      {"type": "allusion", "target": "Jer 31:33", "note": "The new covenant law written on the heart, not on stone tablets — the Spirit's liberating law in 8:2 is the subjective side of the new covenant that Jeremiah's 'written on the heart' anticipated."}
    ],
    "3": [
      {"type": "type", "target": "Lev 4:3", "note": "The Levitical sin offering (peri hamartias in the LXX) — Paul's phrase 'God sending his own Son in the likeness of sinful flesh, as a sin offering' uses the LXX technical term for the sin-offering category, presenting Christ's incarnation-and-death as the fulfillment of the entire Levitical system of sin offerings."},
      {"type": "allusion", "target": "Isa 53:10", "note": "The LORD made the Servant's life 'a guilt offering' (asham) — Isaiah's Servant who bears the guilt offering function is the prophetic trajectory that Paul's 'God condemning sin in the flesh' actualizes in Christ."}
    ],
    "4": [
      {"type": "allusion", "target": "Ezek 36:27", "note": "God's Spirit moving his people to follow his decrees — Paul's 'the righteous requirement of the law might be fully met in us, who walk by the Spirit' is the enacted form of Ezekiel's promised Spirit-enabled obedience; the Spirit does what the law commanded but could not produce in sinful flesh."}
    ],
    "5": [
      {"type": "theme", "target": "Prov 14:12", "note": "There is a way that appears right to a person, but in the end it leads to death — the Proverbs contrast between the way that looks good to the flesh and the way that leads to life is the wisdom background for Paul's Spirit-versus-flesh contrast in vv5-8."}
    ],
    "6": [
      {"type": "allusion", "target": "Deut 30:15-20", "note": "Moses sets before Israel life and death, blessing and curse — Paul's 'the mind governed by the flesh is death, but the mind governed by the Spirit is life and peace' maps onto the Deuteronomic two-ways framework, now reconfigured around the Spirit versus the flesh rather than covenant obedience versus covenant disobedience."}
    ],
    "7": [
      {"type": "allusion", "target": "Ps 2:2-3", "note": "The nations conspiring against the LORD and his anointed, refusing to submit — Paul's 'the mind governed by the flesh is hostile to God; it does not submit to God's law' generalizes the psalm's picture of rebellious rulers to the universal condition of unrenewed human nature."}
    ],
    "8": [
      {"type": "theme", "target": "Isa 1:13-14", "note": "God declaring that the offerings of the rebellious cannot please him — Paul's 'those who are in the realm of the flesh cannot please God' stands in the prophetic tradition that exterior religious performance by an unreformed heart cannot satisfy the holy God."}
    ],
    "9": [
      {"type": "allusion", "target": "Ezek 37:14", "note": "God promising to put his Spirit in his people so they may live — Paul's 'you are not in the realm of the flesh but are in the realm of the Spirit, if indeed the Spirit of God lives in you' is the realized form of Ezekiel's promise of divine Spirit-indwelling as the marker of the renewed covenant people."}
    ],
    "10": [
      {"type": "allusion", "target": "Gen 2:17", "note": "The body mortal because of sin — Paul's 'your body is subject to death because of sin' recalls the Adamic curse (death entered through Adam's sin, Rom 5:12), now contrasted with the Spirit as life because of righteousness."}
    ],
    "11": [
      {"type": "type", "target": "Ezek 37:12-14", "note": "God promising to open graves and put his Spirit in the people so they may live — the resurrection vision of Ezekiel 37 is the OT type that Paul's 'he who raised Christ from the dead will also give life to your mortal bodies through his Spirit' fulfills and surpasses: not national restoration but bodily resurrection of individuals through the same Spirit."}
    ],
    "12": [
      {"type": "theme", "target": "Deut 8:5", "note": "The Lord disciplines his people as a father disciplines a son — Paul's language of obligation-not-to-the-flesh stands in the context of a covenantal relationship that demands loyalty, the kind of familial obligation that the father-son language of Deuteronomy grounds."}
    ],
    "13": [
      {"type": "allusion", "target": "Deut 30:15", "note": "Moses sets before Israel life and death; choose life — Paul's 'if by the Spirit you put to death the misdeeds of the body, you will live' restates the Deuteronomic two-ways in Spirit-and-flesh terms: putting to death the flesh is the Spirit-empowered form of choosing life."}
    ],
    "14": [
      {"type": "allusion", "target": "Exod 4:22", "note": "God declares Israel his firstborn son, called out of Egypt — Paul's 'those who are led by the Spirit of God are the children of God' applies the Exodus sonship to the entire community of the Spirit, now constituted by the Spirit rather than by ethnic descent from Abraham."}
    ],
    "15": [
      {"type": "allusion", "target": "Hos 11:1-4", "note": "God calling his son out of Egypt and teaching him to walk, like a parent lifting a child — the father-son relationship Paul describes through the Spirit of adoption echoes the Hosean portrait of God's tender parental relationship with Israel, now enacted on a deeper level through the Spirit."},
      {"type": "theme", "target": "Exod 4:22", "note": "Israel named God's firstborn son — Paul's 'Spirit of adoption to sonship' by which the community cries 'Abba, Father' transfers the OT adoption language of Israel-as-son to all who are led by the Spirit, including Gentiles."}
    ],
    "16": [
      {"type": "theme", "target": "Deut 14:1-2", "note": "You are the children of the LORD your God — the Spirit bearing witness with our spirit that we are God's children is the interior confirmation of what the Deuteronomic tradition declared externally about Israel's status as God's children through covenant."}
    ],
    "17": [
      {"type": "allusion", "target": "Ps 2:8", "note": "God offering the Son the nations as an inheritance — Paul's 'heirs of God and co-heirs with Christ' picks up the royal inheritance language of Ps 2:8, now shared with all who belong to the Son through the Spirit."},
      {"type": "allusion", "target": "Deut 33:4", "note": "The law as the inheritance of the assembly of Jacob — Paul reframes inheritance away from Torah as inherited possession toward co-inheritance with Christ, the true heir of the Abrahamic and Davidic promises."}
    ],
    "18": [
      {"type": "theme", "target": "Isa 40:5", "note": "The glory of the LORD to be revealed, seen by all flesh together — Paul's contrast between present sufferings and the coming glory echoes Isaiah's eschatological promise of universal divine disclosure; the suffering precedes the revelation of glory, which is the prophetic pattern (Isa 53 → Isa 52:13-15)."}
    ],
    "19": [
      {"type": "allusion", "target": "Isa 11:6-9", "note": "The creation at peace in the messianic age — creation's eager expectation for the children of God to be revealed activates Isaiah's vision of the created order restored when the shoot from Jesse brings justice; the groaning of vv19-22 is the negative of the Isaianic promise awaiting fulfillment."}
    ],
    "20": [
      {"type": "allusion", "target": "Gen 3:17-19", "note": "The ground cursed because of Adam — Paul's 'creation was subjected to frustration' translates the Genesis curse theologically: creation's bondage to futility is the consequence of Adam's rebellion, subjected not by the creation's own will but by God's judicial decree that the domain of the sinner shares the sinner's fate."},
      {"type": "allusion", "target": "Eccl 1:2", "note": "Vanity of vanities, all is vanity — the Hebrew hebel (breath, emptiness, frustration) that Ecclesiastes uses for the futility of the created order under death and time is the OT vocabulary Paul deploys for 'mataiotes' (frustration/futility) in describing creation's subjection."}
    ],
    "21": [
      {"type": "allusion", "target": "Isa 65:17", "note": "God's promise to create new heavens and a new earth — creation's liberation from bondage to decay into 'the freedom and glory of the children of God' is the corporate and cosmic form of the new creation Paul expects, anticipated in Isaiah's eschatological vision."}
    ],
    "22": [
      {"type": "allusion", "target": "Isa 26:17-18", "note": "A woman with child in pain when near delivery — Isaiah's birth-pain as the metaphor for Israel's suffering that precedes divine deliverance is the OT frame for Paul's 'the whole creation has been groaning as in the pains of childbirth'; the suffering is purposive and productive, not terminal."}
    ],
    "23": [
      {"type": "type", "target": "Exod 23:19", "note": "The firstfruits offering — the firstfruits consecrated the whole harvest in anticipation; Paul's 'firstfruits of the Spirit' uses the Levitical-priestly category to describe the Spirit as the initial installment that sanctifies and guarantees the full harvest of resurrection and adoption."}
    ],
    "24": [
      {"type": "theme", "target": "Lam 3:24-26", "note": "The Lord is my portion; I will wait for him; it is good to wait quietly for salvation — the Lamentations posture of patient hope in unseen divine salvation is the OT form of Paul's 'who hopes for what they already have' — genuine hope is directed toward the not-yet."}
    ],
    "25": [
      {"type": "allusion", "target": "Ps 25:5", "note": "Wait for you all day long — the psalmic virtue of patient waiting for God (qavah) is the OT category Paul draws on; the eschatological hope that waits patiently for what is unseen is not resignation but the faith-posture commended throughout the Psalter."}
    ],
    "26": [
      {"type": "theme", "target": "Ps 38:9", "note": "All my longing is before you; my sighing is not hidden from you — Paul's 'we do not know what we ought to pray for, but the Spirit himself intercedes for us through wordless groans' stands in the tradition of the psalmist's inarticulate longing that God nonetheless hears; the Spirit's groaning is the deepest form of this prayer."}
    ],
    "27": [
      {"type": "allusion", "target": "Ps 139:1-4", "note": "You know my thoughts before I speak — Paul's 'he who searches our hearts knows the mind of the Spirit' draws on the Psalter's witness to God's heart-searching knowledge; the Spirit praying in accordance with God's will is heard because God knows both the Spirit's intention and the believer's need simultaneously."},
      {"type": "allusion", "target": "1 Chr 28:9", "note": "The Lord searches every heart and understands every motive behind the thoughts — the divine heart-searching that Paul invokes as the ground of the Spirit's intercessory efficacy is an established OT principle about God's comprehensive knowledge of inward states."}
    ],
    "28": [
      {"type": "allusion", "target": "Gen 50:20", "note": "What others intended for harm, God intended for good — Joseph's reflection on his sufferings is the paradigmatic OT instance of God working all things together for good for those he has called; Paul universalizes Joseph's principle into a Christological axiom."},
      {"type": "allusion", "target": "Isa 46:10-11", "note": "God declaring the end from the beginning and accomplishing his purpose — the divine sovereignty over all events that Paul claims in 'God works all things for good' is the Creator's prerogative that Isaiah 46 asserts against the empty gods who cannot predict or control events."}
    ],
    "29": [
      {"type": "allusion", "target": "Gen 1:26-27", "note": "God making humanity in his image — Paul's 'conformed to the image of his Son' restates the creation-goal (the image of God) in Christological terms: the Son is the true image (Col 1:15), and the predestination to conformity to him is the eschatological restoration of what Genesis 1 declared about humanity's origin."},
      {"type": "allusion", "target": "Ps 89:27", "note": "God making David his firstborn, the most exalted of the kings of the earth — Paul's 'that he might be the firstborn among many brothers and sisters' picks up the Davidic firstborn language, now applied to the risen Christ who heads the family of those predestined to share his image."}
    ],
    "30": [
      {"type": "allusion", "target": "Isa 41:9-10", "note": "God calling Israel from the ends of the earth: 'I called you... I chose you and have not rejected you' — Paul's golden chain (predestined → called → justified → glorified) inhabits the Isaianic language of divine calling as an act of electing love, now applied to the new covenant community."}
    ],
    "31": [
      {"type": "allusion", "target": "Ps 118:6-7", "note": "The Lord is with me; I will not be afraid. What can man do to me? — Paul's rhetorical 'if God is for us, who can be against us?' echoes the psalmist's confession of divine sufficiency against all human opposition; the resurrection makes the claim absolute rather than merely situational."}
    ],
    "32": [
      {"type": "type", "target": "Gen 22:16", "note": "Abraham did not withhold (epheisato, LXX) his son Isaac — Paul's 'he who did not spare (ouk epheisato) his own Son' is a deliberate echo of the Aqedah using the identical LXX verb; the God who stopped Abraham from sacrificing his son did not stop himself from giving his own. The Aqedah is the type; the cross is the reality that made the type bearable by God."}
    ],
    "33": [
      {"type": "allusion", "target": "Isa 50:8-9", "note": "The Servant says 'He who vindicates me is near; who will contend with me? Who is my accuser?' — Paul's 'who will bring any charge against those whom God has chosen? It is God who justifies' is the Servant's vindication-language applied to all who are in Christ; the Servant's confidence before accusers becomes the church's confidence."}
    ],
    "34": [
      {"type": "allusion", "target": "Ps 110:1", "note": "The Lord invites the Davidic king to sit at his right hand until enemies are made a footstool — Paul's 'Christ Jesus who died — more than that, who was raised to life — is at the right hand of God and is also interceding for us' is the NT reading of Ps 110:1 combined with Isa 53:12 (interceding for transgressors); the two OT texts together describe the risen and enthroned Messiah-Servant."}
    ],
    "35": [
      {"type": "allusion", "target": "Ps 44:22", "note": "The psalm of complaint about being sheep for slaughter while trusting God — Paul's list of 'trouble, hardship, persecution, famine...' maps onto the psalmist's catalogue of affliction; the quotation in v36 will confirm the connection."}
    ],
    "36": [
      {"type": "quote", "target": "Ps 44:22", "note": "Paul cites Psalm 44:22 ('For your sake we face death all day long; we are considered as sheep to be slaughtered') to identify the community's suffering with the covenant suffering of the psalmist — but the difference is crucial: in Ps 44 the sufferers seem abandoned; in Romans 8 the sufferers are 'more than conquerors through him who loved us.'"}
    ],
    "37": [
      {"type": "allusion", "target": "Ps 44:4-8", "note": "Through God we push back our enemies — the same psalm Paul cited in v36 contains the confidence of God-given victory; Paul takes the suffering half of Ps 44 (v22) and fulfills the victory half (vv4-8) through Christ, the one through whom we are more than conquerors."}
    ],
    "38": [
      {"type": "theme", "target": "Ps 139:7-10", "note": "There is nowhere to flee from God's presence — Paul's list of cosmic powers unable to separate believers from God's love inverts the psalmist's point: nothing in heaven or earth or depth can take the believer beyond God's reach, precisely because God's love is more extensive than the creation."}
    ],
    "39": [
      {"type": "allusion", "target": "Isa 38:18", "note": "Sheol and death cannot praise God — Paul's confidence that not even death can separate from God's love is the positive inversion of the OT restriction (death placed the worshiper beyond the praise-community); Christ's resurrection has removed this final barrier."}
    ]
  },
  "9": {
    "1": [
      {"type": "allusion", "target": "Gen 42:18", "note": "Joseph's oath formula — the formal oath-with-witness structure Paul uses ('I speak the truth in Christ; my conscience confirms it in the Holy Spirit') follows OT patterns of solemn attestation that invoke God as witness, appropriate to the gravity of the claim that Paul wishes he were cursed for Israel's sake."}
    ],
    "2": [
      {"type": "theme", "target": "Ps 119:136", "note": "Streams of tears because people do not keep your law — Paul's 'great sorrow and unceasing anguish' over Israel's unbelief stands in the tradition of the prophet-psalmist who weeps over Israel's condition; the grief here is Jeremianic in quality (cf. Jer 9:1 — 'Oh that my head were a spring of water')."}
    ],
    "3": [
      {"type": "allusion", "target": "Exod 32:32", "note": "Moses asks God to blot him out of the book if God will not forgive Israel — Paul's wish to be 'cursed and cut off from Christ for the sake of my brothers' is in direct succession to Moses's intercessory self-offering; the Mosaic intercession is the OT type for this Christological commitment to Israel's redemption."}
    ],
    "4": [
      {"type": "theme", "target": "Exod 4:22", "note": "Israel named God's firstborn son — the 'adoption to sonship' (huiothesia) Paul lists as Israel's privilege is the OT sonship grounded in the Exodus covenant and the Davidic covenant (Ps 89:26-27); Paul acknowledges these as real privileges even as he wrestles with their partial non-realization."},
      {"type": "allusion", "target": "Exod 40:34-35", "note": "The glory of the LORD filling the tabernacle — 'theirs the divine glory' recalls the Shekinah glory that was Israel's unique covenant possession; the later loss of the divine glory (Ezek 10-11) makes its return a messianic expectation (Ezek 43:1-5) that Paul sees as fulfilled in Christ (2 Cor 3:18; 4:6)."}
    ],
    "5": [
      {"type": "allusion", "target": "Isa 9:6", "note": "The child born whose name is 'Mighty God, Everlasting Father' — Paul's statement that 'from them is traced the human ancestry of the Messiah, who is God over all' stands in the Isaianic tradition of the divine-human Messiah; the Davidic descendant who is simultaneously 'God over all' fulfills the Emmanuel trajectory (Isa 7:14; 9:6)."}
    ],
    "6": [
      {"type": "theme", "target": "Num 23:19", "note": "God is not a man that he should lie; has he spoken and not fulfilled? — Paul's 'it is not as though God's word had failed' addresses the same concern: can God's promises to Israel be trusted? Numbers 23:19 insists God's words are irrevocable; Paul will show that apparent failure is in fact a more complex fulfillment."}
    ],
    "7": [
      {"type": "allusion", "target": "Gen 21:12", "note": "God tells Abraham that 'it is through Isaac that your offspring will be reckoned' — Paul cites this to establish that physical descent from Abraham was never the criterion of covenant membership; God's election of Isaac over Ishmael already shows that promise and not biology defines the true Israel."}
    ],
    "8": [
      {"type": "allusion", "target": "Gal 4:23", "note": "The principle that Ishmael was born of the flesh and Isaac born of the Spirit — Paul's summary that 'it is not the children by physical descent who are God's children, but it is the children of the promise who are regarded as Abraham's offspring' applies the Genesis Isaac-versus-Ishmael distinction as the hermeneutical key to understanding Israel within Israel."}
    ],
    "9": [
      {"type": "quote", "target": "Gen 18:10", "note": "God's promise at Mamre — 'At the appointed time I will return, and Sarah will have a son' — is cited as the archetypal word of promise (logos tes epangelias) that cannot be annulled by biology or human will; the promise-word that created Isaac is the paradigm for the election-by-promise Paul argues defines the true people of God."}
    ],
    "10": [
      {"type": "allusion", "target": "Gen 25:21-23", "note": "God opening Rebekah's womb and the two nations struggling in her womb — Paul invokes the Jacob-Esau twins' election to demonstrate that divine sovereign purpose precedes any human performance; the struggle in the womb is the OT's most compressed statement of election-before-works."}
    ],
    "11": [
      {"type": "theme", "target": "Isa 46:10", "note": "God declaring the end from the beginning — Paul's emphasis that God's purpose of election stands 'not by works but by him who calls' is grounded in the OT's consistent claim that God's plans are determined before the events occur; Isaiah 46:10 is the theological basis for the predetermination Paul describes."}
    ],
    "12": [
      {"type": "quote", "target": "Gen 25:23", "note": "The oracle to Rebekah — 'The older will serve the younger' — is cited as God's election word spoken before the twins' birth to establish that the criterion was divine call, not human primogeniture or merit; Paul reads the reversal of birth order as the OT disclosure of elective grace."}
    ],
    "13": [
      {"type": "quote", "target": "Mal 1:2-3", "note": "Malachi's 'Jacob I loved, but Esau I hated' is cited to confirm the election-principle at the national level: God's choice of Jacob/Israel over Esau/Edom was not arbitrary but expressed the divine love-commitment that constitutes a covenant people; the 'hatred' is the relative rejection of the non-elect line, not personal vindictiveness."}
    ],
    "14": [
      {"type": "theme", "target": "Deut 32:4", "note": "The Rock whose works are perfect, all his ways just — Paul's rhetorical 'Is God unjust?' is answered by the Deuteronomic affirmation of divine justice as the bedrock of Israel's theology; Paul's argument in vv15-18 will show that sovereign election is not injustice but the expression of mercy."}
    ],
    "15": [
      {"type": "quote", "target": "Exod 33:19", "note": "God's answer to Moses after the golden calf — 'I will have mercy on whom I have mercy, and I will have compassion on whom I have compassion' — is cited as the scriptural principle that mercy is sovereignly dispensed at God's initiative, not earned by merit; the context (post-golden-calf mercy) makes the point even stronger: mercy is given where judgment would be most expected."}
    ],
    "16": [
      {"type": "allusion", "target": "Prov 16:1", "note": "The plans of the heart belong to humans, but the answer of the tongue is from the LORD — Paul's 'it does not, therefore, depend on human desire or effort, but on God's mercy' stands in the wisdom tradition's consistent teaching that human planning cannot override divine purpose; sovereign mercy is the ultimate determining factor."}
    ],
    "17": [
      {"type": "quote", "target": "Exod 9:16", "note": "God's word to Pharaoh — 'I raised you up for this very purpose, that I might display my power in you and that my name might be proclaimed in all the earth' — is cited to show that God's sovereign purpose operates even through the hardened unbeliever; Pharaoh's resistance was the occasion for the display of divine power that spread God's fame to the nations (cf. Josh 2:10; 1 Sam 4:8)."}
    ],
    "18": [
      {"type": "theme", "target": "Exod 4:21", "note": "God hardening Pharaoh's heart — the Exodus narrative's repeated hardening motif (sometimes God hardens, sometimes Pharaoh hardens his own heart) is the OT precedent for Paul's 'God hardens whom he wants to harden'; divine hardening is judicial, the confirmation of a prior human self-hardening rather than its cause."}
    ],
    "19": [
      {"type": "allusion", "target": "Hab 1:13", "note": "The prophet's complaint about the LORD using the unjust to punish the more righteous — the objection Paul voices ('why does God still blame us? Who resists his will?') is the same theodicy problem that Habakkuk raises; Paul's answer in vv20-21 will be the potter/clay response rather than a full theodicy."}
    ],
    "20": [
      {"type": "allusion", "target": "Isa 29:16", "note": "You turn things upside down, as if the potter were thought to be like the clay — Isaiah's rebuke of those who question God's purposes uses the potter/clay image; Paul's 'who are you, a human being, to talk back to God?' inhabits the same prophetic protest against human presumption toward the Creator."},
      {"type": "allusion", "target": "Isa 45:9-10", "note": "Woe to those who quarrel with their Maker — does the clay say to the potter 'What are you making?' — Isaiah 45's potter/clay image is the closer verbal parallel; Paul's 'shall what is formed say to the one who formed it...' echoes this directly, presenting divine sovereignty over creation as the ground for sovereign election."}
    ],
    "21": [
      {"type": "type", "target": "Jer 18:1-6", "note": "Jeremiah at the potter's house — the potter remaking a marred vessel as he sees fit, and God's right to do the same with Israel — is the prophetic instance of the potter's authority that Paul appeals to; the point in Jeremiah is God's sovereign freedom in covenant dealings, not fatalism."}
    ],
    "22": [
      {"type": "allusion", "target": "Exod 9:16", "note": "Pharaoh as the paradigm of the vessel prepared for wrath — Paul's 'objects of his wrath — prepared for destruction' develops the Pharaoh typology of v17 into a principle: God's bearing with those destined for judgment serves to display his patience and make his power known."},
      {"type": "allusion", "target": "Ezek 18:23", "note": "God takes no pleasure in the death of the wicked — Paul's 'what if God, choosing to show his wrath, bore with great patience' suggests a restrained divine judgment; Ezekiel's affirmation that God does not desire destruction provides the OT counterbalance that prevents reading Paul's vessel-of-wrath language as divine sadism."}
    ],
    "23": [
      {"type": "theme", "target": "Isa 45:9-11", "note": "The riches of God's glory revealed to those he chose — the conjunction of divine glory and mercy that Paul describes in the vessels of mercy is anticipated in Isaiah's portrait of God's sovereign creative purpose (to display his own glory) fulfilled in the redemption of his people."}
    ],
    "24": [
      {"type": "allusion", "target": "Amos 9:11-12", "note": "The restoration of David's fallen tent 'so that they may possess the remnant of Edom and all the nations' — Paul's 'called, not only from the Jews but also from the Gentiles' fulfills the Amos promise that the reconstituted Davidic kingdom would incorporate the Gentile nations, cited in Acts 15:16-17 as the Jamesian interpretation of the same fulfillment."}
    ],
    "25": [
      {"type": "quote", "target": "Hos 2:23", "note": "Paul applies Hosea's promise — I will call them my people who are not my people — to the Gentiles: a remarkably bold rereading, since Hosea's original context is the restoration of faithless northern Israel, but Paul reads the not-my-people language as applying equally to those never in the covenant, since covenant faithlessness and covenant exclusion both result in the same condition."}
    ],
    "26": [
      {"type": "quote", "target": "Hos 1:10", "note": "Hosea's promise that in the very place where they were told they are not my people, there they will be called children of the living God — the conversion of Lo-Ammi to sons-of-the-living-God is the OT promise Paul reads as fulfilled in the Gentile mission; the reversal of Hosea's Lo-Ammi judgment is the pattern for Gentile inclusion in the new covenant."}
    ],
    "27": [
      {"type": "quote", "target": "Isa 10:22-23", "note": "Isaiah's 'though Israel's numbers be like the sand of the sea, only a remnant will be saved' — Paul applies this to explain that the mass of ethnic Israel's non-reception of the gospel is itself a fulfillment of Isaiah's remnant prophecy; the remnant is not a failure of the covenant but its selective realization within a faithless majority."}
    ],
    "28": [
      {"type": "quote", "target": "Isa 10:23", "note": "The Lord will carry out his sentence on the earth with speed and finality — the divine judgment embedded in the remnant oracle confirms that God's word has not failed; it has been executed precisely as Isaiah predicted, in the separation of the remnant from the rest."}
    ],
    "29": [
      {"type": "quote", "target": "Isa 1:9", "note": "Isaiah's 'unless the Lord Almighty had left us descendants (sperma, seed), we would have become like Sodom and Gomorrah' — the preservation of a seed within a people deserving total destruction is the OT pattern for the believing remnant within Israel; Paul uses this to show that Israel's current partial receptivity matches Isaiah's own description of the covenant people's precarious survival."}
    ],
    "30": [
      {"type": "theme", "target": "Isa 51:1", "note": "Those who pursue righteousness and who seek the LORD — Paul's paradox that Gentiles who did not pursue righteousness obtained it while Israel who pursued it did not traces the surprising reversal that Isaiah already anticipated: the mission to the Gentiles would produce fruit where Israel's own religious effort had stalled."}
    ],
    "31": [
      {"type": "allusion", "target": "Deut 6:25", "note": "Moses declaring that Israel's righteousness would consist in keeping all this law — Paul's description of Israel 'pursuing the law as the way of righteousness' without obtaining it is the failure of the Deuteronomic program; the law could define righteousness but not produce it in sinful flesh."}
    ],
    "32": [
      {"type": "allusion", "target": "Isa 28:16", "note": "The cornerstone laid in Zion as the test of Israel's response — Paul's 'they pursued it not by faith but as if it were by works; they stumbled over the stumbling stone' introduces the Isa 28:16 / Isa 8:14 complex (quoted in v33) as the explanation of Israel's stumbling: the stone-laying in Zion (the Messiah) was the test that exposed the basis of their pursuit."}
    ],
    "33": [
      {"type": "quote", "target": "Isa 28:16", "note": "The foundational stone laid in Zion — Paul combines Isa 28:16 ('a precious cornerstone for a sure foundation') and Isa 8:14 ('a stone that causes people to stumble and a rock that makes them fall') into a single testimonia about Christ; the stone is simultaneously the foundation for faith and the stumbling-block for those who pursue righteousness by works."},
      {"type": "quote", "target": "Isa 8:14", "note": "A stone that causes stumbling and a rock that makes people fall — Isaiah's warning about the LORD of hosts as a stumbling stone to both houses of Israel is applied to Christ; the one who is the foundation for all who trust becomes the obstacle for those who persist in works-righteousness rather than faith."}
    ]
  },
  "10": {
    "1": [
      {"type": "allusion", "target": "Isa 53:12", "note": "The Servant interceding for transgressors — Paul's 'my heart's desire and prayer to God for the Israelites is that they may be saved' places Paul in the position of the Servant who intercedes for those he loves even when they do not receive him."}
    ],
    "2": [
      {"type": "allusion", "target": "Num 25:11-13", "note": "Phinehas whose zeal for God was not accompanied by understanding — Paul's 'zeal not based on knowledge' echoes the prophetic critique of misguided religious intensity; Israel's zeal for the law is real but misdirected, like the OT examples of sincere but ill-directed devotion."}
    ],
    "3": [
      {"type": "allusion", "target": "Isa 64:6", "note": "All our righteous acts are like filthy rags — Israel's attempt to 'establish their own' righteousness rather than submitting to God's righteousness stands in the tradition of Isaiah's confession about self-generated holiness that cannot satisfy the divine standard; Paul now specifies that God's righteousness has arrived in Christ."}
    ],
    "4": [
      {"type": "allusion", "target": "Jer 31:31-33", "note": "The new covenant replacing the old — Paul's 'Christ is the culmination (telos) of the law so that there may be righteousness for everyone who believes' articulates the telos toward which the Mosaic administration was always pointing; Jeremiah's new covenant (Torah internalized by the Spirit) is the trajectory Christ fulfills and surpasses."}
    ],
    "5": [
      {"type": "quote", "target": "Lev 18:5", "note": "Moses's principle that 'the person who does these things will live by them' — Paul cites this as the logic of the law-righteousness system: it demands doing and promises life on that basis; the reason Christ fulfills the law (v4) is that no one has done it perfectly except Christ himself, who did these things and lived."}
    ],
    "6": [
      {"type": "quote", "target": "Deut 30:12", "note": "Moses's 'who will ascend to heaven to get it and proclaim it to us?' — Paul rereads Deuteronomy 30:12 Christologically: the 'ascending to heaven' is glossed as bringing Christ down (questioning the necessity of the incarnation) and 'descending into the deep' as bringing Christ up from the dead (questioning the necessity of the resurrection); the near word of Deut 30 is the gospel, already accomplished."}
    ],
    "7": [
      {"type": "quote", "target": "Deut 30:13", "note": "Moses's 'who will cross the sea to get it?' — Paul glosses the descent into the sea as descent into the abyss (Hades) and return (the resurrection); the radical accessibility of the word in Deuteronomy 30 — no heroic journey required — becomes Paul's argument that no additional redemptive labor is needed beyond what Christ has already accomplished."}
    ],
    "8": [
      {"type": "quote", "target": "Deut 30:14", "note": "The word is near you, in your mouth and in your heart — Paul identifies this near word as 'the message of faith we are proclaiming'; Moses's claim that the covenant word is radically accessible is fulfilled in the gospel proclamation, which requires only hearing and believing rather than heroic ascent or descent."}
    ],
    "9": [
      {"type": "allusion", "target": "Ps 110:1", "note": "The LORD's declaration 'Sit at my right hand until I make your enemies a footstool' — Paul's 'declare with your mouth Jesus is Lord' is the confession that the one enthroned at God's right hand (Ps 110:1) is Jesus; the confession of Jesus as 'Lord' (kyrios) applies the OT divine name and enthronement to the risen Christ."}
    ],
    "10": [
      {"type": "allusion", "target": "Deut 6:5-6", "note": "Love the LORD with all your heart — Paul's 'with your heart that you believe and are justified, with your mouth that you profess and are saved' reframes the Shema's heart-and-mouth devotion to Yahweh around the saving confession of Christ; the whole-person commitment of Deuteronomy 6 now has its ultimate object in the Lord Jesus."}
    ],
    "11": [
      {"type": "quote", "target": "Isa 28:16", "note": "The one who trusts in the stone laid in Zion 'will never be put to shame' — Paul cites this (already quoted in 9:33) to confirm the universality of faith-righteousness: 'Anyone who believes' (with the universal LXX addition) will be vindicated; the Isaianic promise of non-shame for those who trust in the Messiah-stone is the OT ground of the gospel's inclusive offer."}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 45:22", "note": "God's call to the ends of the earth — 'Turn to me and be saved, all you ends of the earth, for I am God, and there is no other' — Paul's 'the same Lord is Lord of all and richly blesses all who call on him' is the actualization of Isaiah 45:22's universal invitation through the confession of Christ as Lord."}
    ],
    "13": [
      {"type": "quote", "target": "Joel 2:32", "note": "Joel's 'everyone who calls on the name of the LORD will be saved' is applied by Paul to Christ, continuing the practice of Acts 2:21 and 21:38; the divine name (YHWH) on whose invocation Joel promises salvation is now identified with the name of the Lord Jesus, extending the covenant promise to all who call."}
    ],
    "14": [
      {"type": "theme", "target": "Ps 96:2-3", "note": "Proclaim his salvation, declare his glory among the nations — the chain of calling → believing → hearing → preaching → sending that Paul constructs in vv14-15 inhabits the Psalter's vision of the divine name proclaimed to all nations; the missionary sequence Paul describes is the form the psalmist's call to proclamation takes in the new covenant era."}
    ],
    "15": [
      {"type": "quote", "target": "Isa 52:7", "note": "How beautiful on the mountains are the feet of those who bring good news, proclaiming peace and announcing salvation — Paul cites this as scriptural warrant for the necessity of sending preachers; the Isaianic herald announcing Zion's redemption after Babylon is the OT form of the apostolic missionary whose sending Paul argues is divinely necessary."}
    ],
    "16": [
      {"type": "quote", "target": "Isa 53:1", "note": "Isaiah's 'Lord, who has believed our message?' — Paul cites this as the prophetic anticipation of faith's rarity; the same Servant-song from which the gospel's core comes (Isa 53) already predicted that the report (acoe) would not be widely believed, so Israel's unbelief is not an embarrassing surprise but a fulfillment of Isaiah's expectation."}
    ],
    "17": [
      {"type": "allusion", "target": "Isa 55:10-11", "note": "God's word going out and not returning empty but accomplishing what he desires — Paul's 'faith comes from hearing the message, and the message is heard through the word about Christ' assumes the Isaianic theology of the word as the living, active agent of divine purpose; it is not the hearer's response that generates faith but the word itself, which accomplishes God's redemptive intention."}
    ],
    "18": [
      {"type": "quote", "target": "Ps 19:4", "note": "Their voice goes out into all the earth; their words to the ends of the world — Paul applies Psalm 19:4 (about the wordless proclamation of creation) to the proclamation of the gospel; the psalmist's claim that all the earth has heard creation's witness becomes Paul's rhetorical argument that Israel cannot claim not to have heard."}
    ],
    "19": [
      {"type": "quote", "target": "Deut 32:21", "note": "God's word through Moses — 'I will make you envious by those who are not a nation; I will make you angry by a nation that has no understanding' — Paul reads the Song of Moses as God's advance announcement of the Gentile mission; God predicted he would provoke Israel through a non-people, which is what the Gentile reception of the gospel is accomplishing."}
    ],
    "20": [
      {"type": "quote", "target": "Isa 65:1", "note": "Isaiah speaking of the Gentiles — 'I was found by those who did not seek me; I revealed myself to those who did not ask for me' — Paul interprets this as God speaking of the Gentiles (contra the original Isaianic context which some take as referring to Israel); the paradox of divine self-disclosure to those who were not looking for God is fulfilled in the Gentile mission."}
    ],
    "21": [
      {"type": "quote", "target": "Isa 65:2", "note": "God's long-suffering toward Israel — 'All day long I have held out my hands to a disobedient and obstinate people' — applied to Israel; the same Isaiah chapter contrasts God's welcome of Gentile seekers (v1) with his persistent outreach to unresponsive Israel (v2). Paul reads both as describing the present situation: Israel's unbelief is not new but is the continuation of the disobedience Isaiah already described."}
    ]
  }
}

def main():
    existing = load_echo('romans')
    merge_echo(existing, ROMANS_ECHOES)
    save_echo('romans', existing)
    print('Romans 8–10 echoes written.')

if __name__ == '__main__':
    main()
