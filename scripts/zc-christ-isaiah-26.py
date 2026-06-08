"""
MKT Christ Commentary — Isaiah chapter 26
Run: python3 scripts/zc-christ-isaiah-26.py

Isaiah 26 is the "Song of the City of Salvation" — a hymn sung in the strong city
on the day of salvation (contrast with the fallen "lofty city" of v.5).

Key Christological texts:
- 26:3: "perfect peace" (shalom shalom) → Phil 4:7; John 14:27 (peace Christ gives)
- 26:4: "everlasting rock" (tsur olamim) → 1 Cor 10:4 ("the rock was Christ")
- 26:7: "level path of the righteous" → John 14:6 ("I am the way")
- 26:19: "Your dead shall live; their bodies shall rise" — the clearest resurrection
  promise in the OT; John 5:28-29; 1 Cor 15:20-23; Matt 27:52-53
- 26:20: "Enter your chambers" → John 14:2-3 (rooms prepared by Christ)
- 26:21: YHWH coming to judge → Jude 14-15; Rev 6:10 (parousia)
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
    """Merge new_data into existing without overwriting present entries."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ISAIAH = {
  "26": {
    "1": '<p>"We have a strong city; he sets up salvation as walls and bulwarks." The strong city (<em>ʿîr ʿāz</em>) with salvation (<em>yĕšûʿâ</em>) as its structural walls is the eschatological Zion. Heb 11:10: "he was looking forward to the city that has foundations, whose designer and builder is God"; Heb 12:22: "you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem." Rev 21:10-12 presents the New Jerusalem descending, with a great wall — here in Isaiah the wall is salvation itself, meaning the walls are the saving act of God in Christ. The city is not fortified by stone but by the redemption accomplished at the cross.</p>',
    "2": '<p>"Open the gates, that the righteous nation that keeps faith may enter in." Rev 21:25 fulfills this: "its gates will never be shut by day — and there will be no night there"; Rev 22:14: "Blessed are those who wash their robes, so that they may have the right to the tree of life and that they may enter the city by the gates." The one who is the door of entry is Christ: "I am the door; if anyone enters by me, he will be saved" (John 10:9). The "righteous nation that keeps faith" (<em>gôy ṣaddîq šōmēr ʾĕmunîm</em>) is the community of those justified by faith — the NT\'s "righteousness of God through faith in Jesus Christ for all who believe" (Rom 3:22).</p>',
    "3": '<p>"You keep him in perfect peace whose mind is stayed on you, because he trusts in you." The doubled <em>šālôm šālôm</em> (peace, peace — a superlative) is the peace that Christ gives. John 14:27: "Peace I leave with you; my peace I give to you. Not as the world gives do I give to you. Let not your hearts be troubled, neither let them be afraid." Phil 4:7: "the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus." The mind "stayed" on YHWH (<em>sāmûk</em>, leaning/resting upon) is the same posture as Paul\'s "in Christ" — the peace is not produced by the mind\'s effort but by its resting on the object of trust.</p>',
    "4": '<p>"Trust in YHWH forever, for in YHWH GOD is an everlasting rock." 1 Cor 10:4: "and the rock was Christ" — the spiritual rock that Israel drank from in the wilderness is identified as the pre-incarnate Christ. The <em>ṣûr ʿôlāmîm</em> (rock of ages/everlasting rock) is the foundation on which Christ builds his church (Matt 16:18) and on which those who hear his words build (Matt 7:24-25). Heb 13:8: "Jesus Christ is the same yesterday and today and forever" — the everlastingness of the rock is the unchanging faithfulness of Christ. "Rock of Ages, cleft for me" (Toplady) is the direct hymnodic application of this verse.</p>',
    "5": '<p>"For he has humbled the inhabitants of the height, the lofty city. He lays it low, lays it low to the ground, casts it to the dust." The humbling of the lofty city is fulfilled proleptically at the fall of Babylon (Rev 14:8; 18:2: "Fallen, fallen is Babylon the great!") and ultimately in the judgment of all earthly power systems. Phil 2:6-11 establishes Christ as the agent of this humbling: the one who "emptied himself, taking the form of a servant" (v.7) is the same one before whom "every knee should bow" (v.10). The pattern is kenosis-then-exaltation — the strong city of salvation (v.1) rises as the lofty city falls.</p>',
    "6": '<p>"The foot tramples it, the feet of the poor, the steps of the needy." The reversal of social order in the eschatological judgment is the Magnificat\'s content: "he has brought down the mighty from their thrones and exalted those of humble estate; he has filled the hungry with good things, and the rich he has sent away empty" (Luke 1:52-53). Matt 5:3: "Blessed are the poor in spirit, for theirs is the kingdom of heaven." The lowly who trample the fallen city are those who were previously the humiliated poor — their elevation is the Servant\'s own mission (Isa 61:1: "to bring good news to the poor").</p>',
    "7": '<p>"The path of the righteous is level; you make level the way of the righteous." The level path (<em>yĕšārîm</em>, upright/straight) connects to Isa 40:3 ("make straight in the desert a highway") and Luke 3:5 (the Baptist\'s ministry of leveling). But the ultimate fulfillment is Christ himself: "I am the way, and the truth, and the life" (John 14:6). The "way" is not merely a method but a person — the level path of the righteous is not an ethical standard but the one who is himself righteousness and who, by union with him, becomes our path.</p>',
    "8": '<p>"In the path of your judgments, O YHWH, we wait for you; your name and remembrance are the desire of our soul." The posture of waiting for YHWH (cf. 40:31) is the NT community\'s posture regarding Christ\'s return. Rev 22:20: "Come, Lord Jesus!" The Maranatha prayer of 1 Cor 16:22 ("Our Lord, come!") is the NT\'s "your name and remembrance are the desire of our soul." The Acts community "waited" for the promised Spirit (Acts 1:4) as the first installment of the full waiting for Christ — the Advent posture governs both the Spirit\'s coming and the Son\'s return.</p>',
    "9": '<p>"My soul yearns for you in the night; my spirit within me earnestly seeks you." The night-seeking of God anticipates Jesus in Gethsemane (Matt 26:36-46: praying alone in the night before the crucifixion, "my soul is very sorrowful, even to death"). The "earnest seeking" (<em>ʾăšaḥărĕkā</em>, to seek early/diligently) is the prayer-posture of the one who comes to his Father. Heb 5:7: "In the days of his flesh, Jesus offered up prayers and supplications, with loud cries and tears, to him who was able to save him from death, and he was heard because of his reverence." The night-yearning of Isaiah 26:9 is the Servant\'s own spirituality.</p>',
    "10": '<p>"If favor is shown to the wicked, he does not learn righteousness; in the land of uprightness he deals corruptly and does not see the majesty of YHWH." The hardening of the wicked by grace misused parallels Rom 2:4-5 ("do you presume on the riches of his kindness... not knowing that God\'s kindness is meant to lead you to repentance? But because of your hard and impenitent heart you are storing up wrath"). The failure to "see the majesty of YHWH" is the failure to see Christ: John 12:45, "whoever sees me sees him who sent me." The light of divine favor that the wicked do not use to see God becomes the ground of their condemnation.</p>',
    "11": '<p>"O YHWH, your hand is lifted up, but they do not see it. Let them see your zeal for your people, and be ashamed." The divine hand lifted in blessing and judgment that the wicked cannot perceive — at Christ\'s return, "then will appear in heaven the sign of the Son of Man, and then all the tribes of the earth will mourn" (Matt 24:30). The zeal for his people that will be made manifest is the same zeal that drove Jesus to cleanse the temple (John 2:17: "Zeal for your house will consume me"). 1 John 2:28: "so that when he appears we may have confidence and not shrink from him in shame at his coming."</p>',
    "12": '<p>"O YHWH, you will ordain peace for us, for you have indeed done for us all our works." The divine ordaining of peace and the acknowledgment that all works are from God is the theology of grace. Eph 2:8-10: "For by grace you have been saved through faith... not a result of works, so that no one may boast. For we are his workmanship, created in Christ Jesus for good works, which God prepared beforehand, that we should walk in them." The "peace ordained" is the peace established through the atonement (Rom 5:1: "we have peace with God through our Lord Jesus Christ") — not achieved but received.</p>',
    "13": '<p>"O YHWH our God, other lords besides you have ruled over us, but your name alone we bring to remembrance." The exclusive naming of YHWH over former lords is the Christological confession of Phil 2:11: "every tongue confess that Jesus Christ is Lord, to the glory of God the Father." Col 2:15: Christ "disarmed the rulers and authorities and put them to open shame, by triumphing over them in him" — the "other lords" that once ruled are the powers Christ has defeated at the cross. The Name (<em>šēm</em>) that alone is remembered is the name above every name (Phil 2:9).</p>',
    "14": '<p>"They are dead, they will not live; they are shades, they will not arise; to that end you have visited them with destruction and wiped out all remembrance of them." The dead-who-shall-not-rise (the former lords who ruled Israel) contrasts sharply with v.19 ("your dead shall live"). In NT terms, the powers and rulers who will not rise are the "rulers of this age, who are doomed to pass away" (1 Cor 2:6). Christ alone is "the first and the last, and the living one. I died, and behold I am alive forevermore" (Rev 1:17-18) — the one who died and rose stands over against those who died and will not rise.</p>',
    "15": '<p>"But you have increased the nation, O YHWH, you have increased the nation; you are glorified; you have expanded all the borders of the land." The multiplication of the nation anticipates the church\'s expansion to all peoples. Matt 28:18-20: "Go therefore and make disciples of all nations." Acts 1:8: "to the ends of the earth." The "borders of the land" are now the whole earth — Rom 4:13: "the promise that he would be heir of the world" was given to Abraham and his offspring. The physical borders of Canaan become the spiritual borders of the new creation: "the meek shall inherit the earth" (Matt 5:5, citing Ps 37:11).</p>',
    "16": '<p>"O YHWH, in distress they sought you; they poured out a whispered prayer when your discipline was upon them." The prayer in extremity — seeking God specifically under discipline (<em>mûsār</em>, chastisement). Heb 5:7: "In the days of his flesh, Jesus offered up prayers and supplications, with loud cries and tears, to him who was able to save him from death, and he was heard because of his reverence." The "whispered prayer" (<em>ṣĕqôn lāḥaš</em>, a barely audible murmur) is the prayer so pressed by suffering that it can only be whispered — Gethsemane and the cross are the ultimate fulfillment of this verse in the Servant who prays under the discipline that we deserved.</p>',
    "17": '<p>"Like a pregnant woman who writhes and cries out in her pangs when she is near to giving birth, so were we before you, O YHWH." The birth-pangs image of eschatological distress is directly used in John 16:20-21: "you will be sorrowful, but your sorrow will turn into joy. When a woman is giving birth, she has sorrow because her hour has come, but when she has delivered the baby, she no longer remembers the anguish." Matt 24:8: "all these are but the beginning of the birth pains" — the eschatological distress before Christ\'s return is labor that will end in the joy of resurrection and new creation (vv.18-19). Rom 8:22: "the whole creation has been groaning together in the pains of childbirth until now."</p>',
    "18": '<p>"We were pregnant; we writhed; but we have given birth to wind. We have accomplished no deliverance in the earth, and the inhabitants of the world have not fallen." The failed birth — human striving produces only wind. In Gal 2:16, Paul\'s whole argument against Torah-works-righteousness is the same point: "a person is not justified by works of the law but through faith in Jesus Christ." Human religious effort to produce deliverance generates "wind" — it is the <em>rûaḥ</em> of the Spirit, given freely by God (John 3:8: "the wind blows where it wishes"), that produces the new birth (John 3:5-6). The contrast between vv.18 and 19 is the contrast between human striving and divine resurrection.</p>',
    "19": '<p>"Your dead shall live; their bodies shall rise. You who dwell in the dust, awake and sing for joy! For your dew is a dew of light, and the earth will give birth to the dead." The most explicit resurrection promise in the OT. John 5:28-29: "An hour is coming when all who are in the tombs will hear his voice and come out, those who have done good to the resurrection of life, and those who have done evil to the resurrection of judgment." 1 Cor 15:20-23: "in fact Christ has been raised from the dead, the firstfruits of those who have fallen asleep... as in Adam all die, so also in Christ shall all be made alive." Matt 27:52-53: at Jesus\'s resurrection, "the tombs also were opened... many bodies of the saints who had fallen asleep were raised" — the preliminary fulfillment of Isaiah 26:19. The "dew of light" (<em>ṭal ʾôrōt</em>) is the resurrection-dew, the divine life-moisture that awakens the dead — in John\'s Gospel, Christ is the resurrection and the life (11:25) who speaks and the dead come forth (11:43-44).</p>',
    "20": '<p>"Come, my people, enter your chambers, and shut your doors behind you; hide yourselves for a little while until the fury has passed by." The divine hiding-place during judgment connects to the Passover night (Exod 12:22-23: "none of you shall go out of the door of his house until the morning"). John 14:2-3: "In my Father\'s house are many rooms (<em>monai</em>). I go to prepare a place for you... I will come again and will take you to myself." The "chambers" (<em>ḥăḏārîm</em>) are the dwelling places Christ prepares — the believer\'s shelter in the eschatological judgment is union with Christ, hidden with him in God (Col 3:3: "your life is hidden with Christ in God"). Rev 6:11: "They were told to rest a little longer" — the <em>kĕmōʿeṭ</em> (for a little while) of Isaiah 26:20.</p>',
    "21": '<p>"For behold, YHWH is coming out from his place to punish the inhabitants of the earth for their iniquity, and the earth will disclose the blood shed on it, and will no more cover its slain." The divine coming-out to judge is the parousia. Jude 14-15: "Behold, the Lord comes with ten thousands of his holy ones, to execute judgment on all and to convict all the ungodly." The earth disclosing its concealed blood is the revelation of all violence at the judgment: Rev 6:10 (the martyrs\' blood crying out), Rev 16:6 ("for they have shed the blood of saints and prophets"), Rev 18:24 ("in her was found the blood of prophets and of saints"). The cross itself is the foundational disclosure: the earth swallowed no blood at Calvary — the body was taken down, the blood poured, the injustice recorded — and at the parousia, no blood will remain covered.</p>',
  },
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    # INTENT: Verify all 21 Isaiah 26 mkt-christ verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 26 verse count changes, update expected total
    # VERIFY: Console shows complete with 21 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-christ' / 'isaiah.json').read_text())
    missing = [v for v in il.get('26', {}) if v not in out.get('26', {})]
    if missing:
        print(f'  MISSING: {missing}')
    else:
        print(f'  OK: all Isaiah 26 mkt-christ verses present ({len(il.get("26", {}))} verses)')

if __name__ == '__main__':
    main()
