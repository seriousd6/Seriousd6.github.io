"""
MKT Christ Commentary — Judges chapters 14–17
Run: python3 scripts/zc-christ-judges-14-17.py

Every verse receives an entry connecting it to the trajectory toward Christ.

Ch14: Samson's marriage — divine sovereignty through human failure; the lion/honey
      riddle as type of death-and-life; Spirit-rushing as messianic empowerment
Ch15: Jawbone victory; En-hakkore spring; the pattern of lament-and-provision
Ch16: Delilah betrayal; hair/Nazirite; Spirit's departure; death-that-defeats;
      Samson's prayer and final act as a type of Christ's death defeating more in
      dying than living
Ch17: Micah's shrine — religious formalism without covenant; the priest-for-hire;
      "everyone did what was right in his own eyes" as the condition requiring a king

Typological keys:
- Samson as a Nazirite set apart from birth: parallels John the Baptist (Luke 1:15)
  and Christ (set apart before time, Eph 1:4; the ultimate Nazirite consecration)
- Lion/honey riddle (14:14): the death that produces sweetness — 1 Cor 15:54-55
  ('Death is swallowed up in victory'); Heb 2:14 — through death destroying death
- Spirit three times rushing on Samson: the three-fold Spirit-empowerment
  points to the permanent Spirit-anointing on Christ (Isa 61:1; John 3:34)
- Samson's "he did not know YHWH had left" (16:20): Ps 22:1; Matt 27:46 — the
  dereliction of the cross as the moment of maximum abandonment before victory
- More killed in his death than life (16:30): the cross saves more than the
  earthly ministry; "unless a grain of wheat falls and dies" (John 12:24)
- Micah's shrine (ch17): formalism vs covenant; sets up the need for the king
  who will establish true worship (1 Sam 7; Ps 24; John 4:23)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

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

CHRIST = {
  "14": {
    "1": "<p>Samson's story begins with an unauthorized desire that YHWH sovereignly uses: 'his father and mother did not know that it was from YHWH' (v4). This is the pattern of divine sovereignty working through human failure — what Joseph names in Gen 50:20: 'You intended evil against me; God intended it for good.' In Christ, the ultimate example of this principle reaches its apex: those who crucified him 'acted in ignorance' (Acts 3:17), yet 'this Jesus, delivered up according to the definite plan and foreknowledge of God, you crucified and killed by the hands of lawless men' (Acts 2:23). The cross is simultaneously human evil and divine good — the same God who worked through Samson's sinful desire works through the sinful desire of those who condemned his Son.</p>",
    "4": "<p>'It was from YHWH, for he was seeking an occasion against the Philistines.' Divine sovereignty over human sin — the most theologically dense verse in the Samson narrative. YHWH does not author Samson's sinful desire but works through it to create the confrontation his deliverance purpose requires. This is the grammar of providence at the cross: 'for truly in this city there were gathered together against your holy servant Jesus, whom you anointed, both Herod and Pontius Pilate, along with the Gentiles and the peoples of Israel, to do whatever your hand and your plan had predestined to take place' (Acts 4:27-28). The 'occasion' YHWH seeks through Samson's marriage is a type of the 'occasion' he sought through the betrayal of Judas, the jealousy of the priests, and the cowardice of Pilate.</p>",
    "6": "<p>'The Spirit of YHWH rushed upon him' — the first of three Spirit-empowerments in the Samson narrative (14:6; 14:19; 15:14). Each prepares for a specific act of deliverance. The permanent, immeasurable Spirit-anointing of Christ (John 3:34 — 'for he gives the Spirit without measure') is the fulfillment: not crisis-response empowerment but abiding consecration. The lion-tearing — bare-handed, no weapon — is Samson at his most messianic: pure divine strength operating through human flesh. Paul: 'not I, but the grace of God that is with me' (1 Cor 15:10). The Spirit-empowered defeat of a predatory beast anticipates Christ's defeat of the lion-like adversary: 'Your adversary the devil prowls around like a roaring lion, seeking someone to devour' (1 Pet 5:8) — Christ 'destroyed the one who has the power of death' (Heb 2:14).</p>",
    "14": "<p>'Out of the eater came something to eat, and out of the strong came something sweet.' The Samson riddle is perhaps the most compressed type of the resurrection in the OT: death (the lion, the eater, the strong) produces life (honey, food, sweetness). Paul's resurrection hymn draws from the same imagery: 'Death is swallowed up in victory. O death, where is your victory? O death, where is your sting?' (1 Cor 15:54-55 — citing Isa 25:8 and Hos 13:14). The strength of death has been inverted into the sweetness of resurrection life. Christ's death — the ultimate 'eater' that consumed the sins of the world — becomes the source of the sweetest good: eternal life. 'Unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit' (John 12:24).</p>",
    "19": "<p>'The Spirit of YHWH rushed upon him, and he went down to Ashkelon and struck thirty men of them.' The second Spirit-empowerment in a context that looks like personal vengeance rather than covenant deliverance. Yet even here YHWH is working — these are the first Philistines struck in the campaign that will culminate in ch16. Christ's statement about his own mission maps this pattern: 'I did not come to bring peace, but a sword' (Matt 10:34) — what appears as personal confrontation (the temple cleansing, the clash with Pharisees) is the divine warrior's campaign against the powers that enslave humanity. The Spirit-rushed judge who strikes the enemy in the context of personal crisis is a rough type of the Spirit-anointed Messiah whose personal sufferings become the mechanism of universal deliverance.</p>"
  },
  "15": {
    "14": "<p>'The Spirit of YHWH rushed upon him, and the ropes on his arms became like flax burned with fire.' The third and final Spirit-empowerment of Samson's early career — this time releasing him from bonds so he can fight. The binding-and-releasing pattern is consistent: Israel binds their own deliverer (vv12-13), but the Spirit breaks every chain. This is the grammar of the resurrection: 'God raised him up, loosing the pangs of death, because it was not possible for him to be held by it' (Acts 2:24). The ropes that bound Samson dissolve like burning flax; the grave that held Christ could not hold him. The Spirit of YHWH that empowers the judge-deliverer is the same Spirit who raised Christ from the dead (Rom 8:11).</p>",
    "18": "<p>Samson's prayer after the great victory — 'You have given this great salvation (<em>yəšûʿāh gəḏôlāh</em>) by the hand of your servant, and now shall I die of thirst?' — is one of the most human moments in the book: the great deliverer is undone by ordinary thirst. This is the pattern of the incarnation: the one who gives living water (John 4:14) says 'I thirst' from the cross (John 19:28). The strongest man in Israel cannot sustain himself after the battle; the Son of God in human flesh experiences the full vulnerability of creaturely life. The prayer is heard and answered (v19) — as was Jesus's Gethsemane prayer, answered not by the removal of the cup but by the resurrection on the other side of it.</p>",
    "19": "<p>'God split open the hollow place that is in Lehi, and water came out from it.' The wilderness-water provision pattern (Moses striking the rock, Exod 17:6; Num 20:11) repeats here: God provides water for his deliverer after battle. Paul interprets the wilderness rock as Christ: 'they drank from the spiritual Rock that followed them, and the Rock was Christ' (1 Cor 10:4). The spring at En-hakkore ('Spring of the One Who Called') preserves Samson's prayer in geography — a place-name that testifies to answered prayer. In Christ, the ultimate 'called out' one (Isa 42:6 — 'I have called you in righteousness') becomes the source of living water for all who cry to God: 'If anyone thirsts, let him come to me and drink' (John 7:37).</p>"
  },
  "16": {
    "17": "<p>'A razor has never come upon my head, for I have been a Nazirite to God from my mother's womb.' Samson's final disclosure of the secret of his strength identifies it as Nazirite consecration — a set-apart life from birth. The parallel to Christ is the ultimate consecration: 'Blessed be the Lord God of Israel, for he has visited and redeemed his people... As he spoke by the mouth of his holy prophets from of old... to show mercy to our fathers and to remember his holy covenant' (Luke 1:68-72). Christ is the one holy and consecrated from eternity (Eph 1:4 — 'chosen in him before the foundation of the world'). Where Samson's consecration is violated and the source of strength removed, Christ's holiness is unbreakable — he who 'knew no sin' (2 Cor 5:21) could not be defiled and could not be held by death.</p>",
    "20": "<p>'He did not know that YHWH had left him.' The most tragic sentence in Judges — and a type of the most anguished cry in the NT: 'My God, my God, why have you forsaken me?' (Matt 27:46, citing Ps 22:1). Where Samson's abandonment is the consequence of covenant violation (his Nazirite vow broken), Christ's dereliction is the consequence of substitutionary atonement — he who knew no sin becomes sin (2 Cor 5:21), experiencing the full weight of divine abandonment that sinners deserve. Samson did not know YHWH had left; Christ cries it from the cross, fully conscious of the abandonment he is undergoing on behalf of others. The type is partial — the antitype is total and willing.</p>",
    "28": "<p>Samson's final prayer — 'Remember me, O Lord YHWH, and please strengthen me just this once, O God, that I may be avenged' — is a lament prayer from the depths: blind, enslaved, mocked. The element of 'remembering' (<em>zākar</em>) is the covenant memory-language: when YHWH 'remembers,' he acts on prior commitment (Gen 8:1 — God remembered Noah; Exod 2:24 — God remembered his covenant with Abraham). The thief on the cross echoes this exact form: 'Jesus, remember me when you come into your kingdom' (Luke 23:42). Both are at the point of death, disgraced, asking only to be remembered by the covenant God. Both prayers are heard.</p>",
    "30": "<p>'He killed more at his death than he had killed during his life.' The final Samson verdict is the pattern of Christ's cross in miniature: 'unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit' (John 12:24). The living Samson killed Philistines one by one; the dying Samson kills 3,000 in a moment. The living Jesus gathered twelve disciples; the dying Jesus draws all people to himself (John 12:32 — 'And I, when I am lifted up from the earth, will draw all people to myself'). The cross produces more fruit than the entire earthly ministry — Pentecost (3,000 in a day, Acts 2:41) follows Calvary. The Samson pattern is the seed of the gospel principle: death is more fruitful than life when it is a death of consecrated self-giving.</p>"
  },
  "17": {
    "5": "<p>Micah's private shrine — ephod, teraphim, carved image, molten image, private priest — is the institutional form of the book's theological failure: Israel constructs its own access to God rather than using what God has provided. Jesus condemns the same impulse: 'You worship what you do not know' (John 4:22) — sincerity without covenant truth produces false worship. The NT's answer to Micah's shrine is the true worship that comes through Christ: 'True worshipers will worship the Father in spirit and truth, for the Father is seeking such people to worship him' (John 4:23). Every unauthorized approach to God from Cain's offering to Micah's shrine to Simon Magus's attempt to buy the Spirit points to the same problem — human beings trying to construct their own access rather than entering through the door that God has provided: 'I am the door' (John 10:9).</p>",
    "6": "<p>'In those days there was no king in Israel. Everyone did what was right in his own eyes.' The book's theological verdict — repeated four times (17:6; 18:1; 19:1; 21:25) — is simultaneously the diagnosis of the human condition apart from God's kingship and the forward-pointing arrow toward the Messiah-King. Paul expresses the same diagnosis in Rom 3:10-12: 'None is righteous, no, not one; no one seeks for God... no one does good.' The 'no king in Israel' refrain is the OT's way of saying what Paul says in Gal 4:4 — 'when the fullness of time had come, God sent forth his Son.' The chaos and moral collapse of the judge period is the darkness before the dawn; the refrain cries out for the king who will be born in Bethlehem.</p>",
    "13": "<p>Micah's confidence — 'Now I know that YHWH will prosper me, since I have a Levite as priest' — is the theology of procedural religion: get the right ritual personnel, and prosperity follows. This is the error Christ systematically dismantles: 'This people honors me with their lips, but their heart is far from me; in vain do they worship me, teaching as doctrines the commandments of men' (Matt 15:8-9, citing Isa 29:13). The hired Levite at a stolen-idol shrine is the extreme case of what happens when form replaces substance, procedure replaces heart, and religious technique replaces covenant relationship. In Christ, the Levitical priesthood itself is superseded: 'We have such a high priest, one who is seated at the right hand of the throne of the Majesty in heaven' (Heb 8:1) — the Levite-for-hire gives way to the eternal priest after the order of Melchizedek.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', 'judges')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', 'judges', c)
    print(f'judges mkt-christ: wrote {sum(len(v) for v in CHRIST.values())} verses across ch 14-17')

if __name__ == '__main__':
    main()
