"""
MKT Christ Commentary — Isaiah 64 (12 verses — Oh That You Would Rend the Heavens)
Run: python3 scripts/zc-christ-isaiah-64.py
Key decisions:
- v1: "Oh that you would rend the heavens and come down" — the prayer that the
  incarnation answers: the Father tears open the heavens at the baptism of Jesus
  (Mark 1:10 — the heavens "torn apart"), granting the very petition Isaiah 64:1
  voices; the theophany-wish fulfilled in incarnation
- v4: "No eye has seen... what God has prepared for those who wait" — DIRECT
  citation in 1 Cor 2:9 (Paul attributes this to Scripture; the LXX version
  of Isaiah 64:4 is the source text); the eschatological hope that eye cannot
  see is what the Spirit reveals in Christ
- v6: "We have all become like one who is unclean, and all our righteous deeds
  are like a polluted garment" — the definitive OT statement of human moral
  bankruptcy; Rom 3:10-12; Phil 3:9 (righteousness not my own but from God
  through faith in Christ)
- v8-9: Potter and clay — Rom 9:20-21 (Paul's use of the potter-clay image to
  argue for divine sovereignty in election); the clay that argues with the potter
  is the posture that the cross silences
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent


def load_comm(layer, book):
    p = ROOT / "data" / "commentary" / layer / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}


def save_comm(layer, book, data):
    p = ROOT / "data" / "commentary" / layer / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def merge_comm(existing, new_data):
    # INTENT: Write only absent keys so re-running is safe after manual edits.
    # CHANGE? If isaiah.json schema changes, update merge_comm and ISAIAH dict below.
    # VERIFY: python3 -c "import json; d=json.load(open('data/commentary/mkt-christ/
    #   isaiah.json')); print('Isa 64 v4:',d.get('64',{}).get('4','MISSING')[:80])"
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, text in verses.items():
            existing[ch].setdefault(v, text)


ISAIAH = {
    "64": {
        "1": "<p>\"Oh that you would rend the heavens and come down, that the mountains might quake at your presence\" — the anguished theophany-petition: the community pleads for YHWH to tear open the boundary between heaven and earth. The rending of the heavens is the spatial miracle that divine absence requires. Mark 1:10: \"And when he came up out of the water, immediately he saw the heavens being torn apart (<em>schizomenous</em>) and the Spirit descending on him like a dove.\" Matthew 27:51: \"And behold, the curtain of the temple was torn in two, from top to bottom.\" The two tearings of Mark and Matthew answer Isaiah 64:1 — at the baptism, the heavens are rent (the petition granted) and the Father declares the beloved Son; at the cross, the temple curtain is rent (the access granted). The incarnation is the tearing-open of the cosmic boundary that Isaiah 64:1 petitioned — God rending heaven to come down in the person of Jesus.</p>",
        "2": "<p>\"As when fire kindles brushwood and the fire causes water to boil — to make your name known to your adversaries, and that the nations might tremble at your presence!\" — the purpose of the theophany: divine-name recognition among adversaries, trembling among nations. The fire and water imagery of terrifying divine power. Hebrews 12:29: \"for our God is a consuming fire.\" Revelation 1:14-15: \"The hairs of his head were white, like white wool, like snow. His eyes were like a flame of fire, his feet were like burnished bronze, refined in a furnace.\" The risen Christ of Revelation 1 is the answered theophany of Isaiah 64:2 — the divine presence that causes trembling among adversaries. Acts 2:37: \"When the people heard this, they were cut to the heart.\" The Pentecost sermon causes the trembling that Isaiah petitioned — nations hearing the mighty works of God in their own languages (Acts 2:11), which is a fulfillment of the divine-name-made-known petition.</p>",
        "3": "<p>\"When you did awesome things that we did not expect, you came down, the mountains quaked at your presence. From of old no one has heard or perceived by the ear, no eye has seen a God besides you, who acts for those who wait for him\" — the remembered theophanies (Sinai above all) as ground for the present petition. The God who did the unexpected in the past can do it again. The phrase \"no eye has seen a God besides you\" anticipates the v4 statement that Paul will cite directly. Luke 1:49: \"for he who is mighty has done great things for me, and holy is his name.\" Mary's Magnificat recalls the \"awesome things that we did not expect\" — the incarnation was precisely the unexpected thing (the virgin birth, the Bethlehem manger, the census). 1 Corinthians 1:27: \"But God chose what is foolish in the world to shame the wise; God chose what is weak in the world to shame the strong.\" The unexpected divine action of Isaiah 64:3 is the pattern of all divine action, culminating in the cross.</p>",
        "4": "<p>\"From of old no one has heard or perceived by the ear, no eye has seen a God besides you, who acts for those who wait for him\" — the uniqueness-declaration: no God besides YHWH acts on behalf of those who wait for him (<em>lĕmĕḥakkeh lô</em>). 1 Corinthians 2:9: \"But, as it is written, 'What no eye has seen, nor ear heard, nor the heart of man imagined, what God has prepared for those who love him.'\" Paul cites Isaiah 64:4 (in LXX form) as the source for the Spirit-revealed wisdom of the gospel — the things God has prepared are the eschatological realities unveiled by the Spirit of Christ. The hidden things of Isaiah 64:4 are the mystery of Christ revealed in the gospel (1 Cor 2:10: \"these things God has revealed to us through the Spirit\"). Ephesians 3:4-5: \"the mystery of Christ, which was not made known to the sons of men in other generations as it has now been revealed to his holy apostles and prophets by the Spirit.\" The \"no eye has seen\" of Isaiah 64:4 is the not-yet of prophecy; the Spirit's revelation in Christ is its yes.</p>",
        "5": "<p>\"You meet him who joyfully works righteousness, those who remember you in your ways. Behold, you were angry, and we sinned; in our sins we have been a long time, and shall we be saved?\" — the communal self-indictment: the transition from praise of divine action (vv3-4) to confession. YHWH meets the righteous worker — but \"we sinned.\" The honesty of the prayer: chronic sinfulness, long-continued. Romans 3:23: \"for all have sinned and fall short of the glory of God.\" Romans 5:8: \"but God shows his love for us in that while we were still sinners, Christ died for us.\" The \"shall we be saved?\" of Isaiah 64:5 is the existential question that the gospel answers: yes — not because we have worked righteousness but because Christ, the one who \"joyfully works righteousness\" perfectly (Heb 4:15: without sin), meets us in our sin and absorbs the anger we incurred.</p>",
        "6": "<p>\"We have all become like one who is unclean, and all our righteous deeds are like a polluted garment. We all fade like a leaf, and our iniquities, like the wind, take us away\" — the total moral bankruptcy: not just sinners but the community's righteousnesses (its best efforts) are like a \"polluted garment\" (<em>bĕged ʿiddîm</em>). Romans 3:10-12: \"None is righteous, no, not one; no one understands; no one seeks for God. All have turned aside; together they have become worthless; no one does good, not even one.\" Philippians 3:8-9: \"I count everything as loss because of the surpassing worth of knowing Christ Jesus my Lord... that I may gain Christ and be found in him, not having a righteousness of my own that comes from the law, but that which comes through faith in Christ, the righteousness from God that depends on faith.\" Paul's self-application of Isaiah 64:6 logic: his Pharisaic righteousness (his best efforts) is counted as dung so that Christ's righteousness replaces it. The polluted garments of Isaiah 64:6 are replaced by the white robes of Revelation 7:14 — \"washed... in the blood of the Lamb.\"</p>",
        "7": "<p>\"There is no one who calls upon your name, who rouses himself to take hold of you; for you have hidden your face from us, and have made us melt in the hand of our iniquities\" — the spiritual paralysis: no one calls, no one stirs himself to pray, because YHWH has hidden his face and iniquity has produced a spiritual immobility. Romans 3:11: \"no one seeks for God.\" Romans 8:26: \"Likewise the Spirit helps us in our weakness. For we do not know what to pray for as we ought, but the Spirit himself intercedes for us with groanings too deep for words.\" The \"no one calls\" of Isaiah 64:7 is the condition of humanity without the Spirit — and the Spirit's intercession of Romans 8:26 is the divine answer to the failure to call. Christ makes intercession at the right hand of the Father (Heb 7:25: \"he always lives to make intercession for them\") — the one who calls on our behalf when we cannot call for ourselves.</p>",
        "8": "<p>\"But now, O LORD, you are our Father; we are the clay, and you are our potter; we are all the work of your hand\" — the pivot to petition on the basis of the Father-creator relationship: \"but now\" (<em>wĕʿattāh</em>) — the same hinge word as Isaiah 43:1. Despite the moral bankruptcy of vv5-7, the community appeals to the relationship that creation and covenant establish: Father, potter. Romans 9:20-21: \"But who are you, O man, to answer back to God? Will what is molded say to its molder, 'Why have you made me like this?' Has the potter no right over the clay, to make out of the same lump one vessel for honorable use and another for dishonorable use?\" Paul uses the potter-clay image of Isaiah 64:8 in his argument for divine sovereignty in election — the same imagery, applied not to petition but to the silencing of human objection. The cross is the decisive potter-act: God reshapes broken human clay into the image of the risen Son (Rom 8:29: \"conformed to the image of his Son\").</p>",
        "9": "<p>\"Be not so terribly angry, O LORD, and remember not iniquity forever. Behold, please look, we are all your people\" — the intercession: \"all your people\" is the ground of appeal. The covenant community presses its covenant membership as the reason for divine restraint. Romans 11:1-2: \"I ask, then, has God rejected his people? By no means! For I myself am an Israelite, a descendant of Abraham, a member of the tribe of Benjamin. God has not rejected his people whom he foreknew.\" Hebrews 7:25: \"Consequently, he is able to save to the uttermost those who draw near to God through him, since he always lives to make intercession for them.\" The \"remember not iniquity forever\" petition of Isaiah 64:9 is the petition that Christ grants through his blood — Hebrews 8:12 (quoting Jer 31:34): \"I will remember their sins no more.\" The new covenant is the answer to Isaiah 64:9's request: YHWH has covenanted to no longer remember the iniquity of the forgiven.</p>",
        "10": "<p>\"Your holy cities have become a wilderness; Zion has become a wilderness, Jerusalem a desolation\" — the devastation of the exile described: the holy places reduced to wilderness. The most sacred geography has become desert. Luke 21:20-22: \"But when you see Jerusalem surrounded by armies, then know that its desolation has come near. Then let those who are in Judea flee to the mountains... For these are days of vengeance, to fulfill all that is written.\" Revelation 21:2: \"And I saw the holy city, new Jerusalem, coming down out of heaven from God, prepared as a bride adorned for her husband.\" The Jerusalem made desolate in Isaiah 64:10 is the Jerusalem made desolate in AD 70 (fulfilling Luke 21) — and both prepare the way for the new Jerusalem coming down from heaven (Revelation 21), which is the city that the desolated earthly city was always pointing toward. Christ weeps over Jerusalem's desolation (Luke 19:41) and then promises its eschatological renewal (Rev 21).</p>",
        "11": "<p>\"Our holy and beautiful house, where our fathers praised you, has been burned by fire, and all our pleasant places have become ruins\" — the temple destroyed: the specific focus narrows from holy cities (v10) to the temple itself. The place of praise is ash. The keenness of the loss — \"holy and beautiful\" (<em>qōdĕšēnû ûṯipaʾartēnû</em>) — captures the community's grief. John 2:19-21: \"Jesus answered them, 'Destroy this temple, and in three days I will raise it up.'... But he was speaking about the temple of his body.\" 1 Corinthians 3:16-17: \"Do you not know that you are God's temple and that God's Spirit dwells in you?... God's temple is holy, and you are that temple.\" The burned beautiful house of Isaiah 64:11 anticipates the temple that Christ's body is — which is destroyed (crucified) and raised in three days, becoming the foundation of the new temple that is the community of believers indwelt by the Spirit. Revelation 21:22: \"And I saw no temple in the city, for its temple is the Lord God the Almighty and the Lamb.\" The earthly temple's destruction is the precondition for the eternal temple.</p>",
        "12": "<p>\"Will you restrain yourself at these things, O LORD? Will you keep silent, and afflict us so terribly?\" — the closing petition: will YHWH remain passive? The silence of God in affliction is the community's sharpest pain. The question hangs unanswered — which makes Isaiah 65's response (God who was always ready to be found) all the more dramatic. Psalm 22:1-2: \"My God, my God, why have you forsaken me? Why are you so far from saving me, so far from my cries of anguish? My God, I cry out by day, but you do not answer, by night, but I find no rest.\" Matthew 27:46: Jesus quotes Psalm 22:1 from the cross. The divine silence of Isaiah 64:12 reaches its deepest point at the cross — when the Son himself cries out \"why have you forsaken me?\" and receives silence in return. But the silence is not the end: Psalm 22:24: \"For he has not despised or scorned the suffering of the afflicted one; he has not hidden his face from him but has listened to his cry for help.\" Isaiah 65:1: \"I was ready to be sought by those who did not ask for me.\" The silence breaks at the resurrection.</p>"
    }
}


def main():
    existing = load_comm("mkt-christ", "isaiah")
    before = sum(len(v) for v in existing.values())
    merge_comm(existing, ISAIAH)
    after = sum(len(v) for v in existing.values())
    save_comm("mkt-christ", "isaiah", existing)
    print(f"{len(existing)} chapters, {after} verse entries total (+{after - before} new)")
    for v, kw in [("1", "rend"), ("4", "eye has seen"), ("6", "unclean"), ("8", "potter")]:
        entry = existing.get("64", {}).get(v, "MISSING")
        print(f"  Isa 64:{v} — {'OK' if kw.lower() in entry.lower() else 'CHECK'}")
    ch = existing.get("64", {})
    missing = [str(i) for i in range(1, 13) if str(i) not in ch]
    print(f"  Missing verses: {missing if missing else 'none'}")


if __name__ == "__main__":
    main()
