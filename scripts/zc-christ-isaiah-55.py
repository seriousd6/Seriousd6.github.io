"""
MKT Christ Commentary — Isaiah 55 (13 verses — Come to the Waters)
Run: python3 scripts/zc-christ-isaiah-55.py
Key decisions:
- v1: "Come, everyone who thirsts" — DIRECT connection: John 7:37-38 (the
  last day of the feast, Jesus cried out: "If anyone is thirsty, let him
  come to me and drink"); Rev 22:17 ("let whoever is thirsty come")
- v3: "I will make with you an everlasting covenant, the sure mercies of
  David" — Acts 13:34 (Paul DIRECTLY quotes LXX of this verse, applying
  David's blessings to Christ's resurrection as the everlasting covenant
  fulfillment; the only NT quotation of this verse)
- v5: "Behold, you shall call a nation you do not know" — the Gentile
  mission; the nations running to Christ; fulfilled in Acts and Paul's
  missionary journeys
- vv8-9: "My thoughts are not your thoughts" — the divine transcendence
  that makes the cross counter-intuitive wisdom (1 Cor 1:18-25)
- vv10-11: "My word that goes out from my mouth shall not return empty"
  — John 1:1-14 (the Word became flesh and accomplished the Father's
  purpose); Heb 4:12 (the living and active word)
- vv12-13: The exodus of joy / cypress instead of thornbush — the final
  homecoming; the eschatological reversal; type of the new creation
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
    #   isaiah.json')); print('Isa 55 v1:',d.get('55',{}).get('1','MISSING')[:80])"
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, text in verses.items():
            existing[ch].setdefault(v, text)


ISAIAH = {
    "55": {
        "1": "<p>\"Come, everyone who thirsts, come to the waters; and he who has no money, come, buy and eat! Come, buy wine and milk without money and without price\" — the great grace-market: thirst without cost, wine and milk without payment. The economy of grace inverts market logic entirely: the more valuable the commodity (water, wine, milk — the necessities and delights of life), the less it costs the recipient. John 7:37-38: \"On the last day of the festival, the great day, while Jesus was standing there, he cried out, 'Let anyone who is thirsty come to me, and let the one who believes in me drink. As the scripture has said, \"Out of the believer's heart shall flow rivers of living water.\"'\" Revelation 22:17: \"The Spirit and the bride say, 'Come.' And let everyone who hears say, 'Come.' And let everyone who is thirsty come. Let anyone who wishes take the water of life as a gift.\" Jesus's Feast of Tabernacles cry and Revelation's closing invitation are the Isaiah 55:1 offer universalized — the cosmic marketplace where the water of life is given without price because the price has already been paid at the cross (1 Pet 1:18-19).</p>",
        "2": "<p>\"Why do you spend your money for that which is not bread, and your labor for that which does not satisfy? Listen diligently to me, and eat what is good, and delight yourselves in rich food\" — the futility of spending on non-sustaining commodities contrasted with free real food. The economic-spiritual paradox: money spent on substitutes, while the genuine article is free. Matthew 6:19-33: \"Do not store up for yourselves treasures on earth... seek first his kingdom and his righteousness, and all these things will be given to you as well.\" John 6:27: \"Do not work for food that spoils, but for food that endures to eternal life, which the Son of Man will give you.\" John 6:35: \"I am the bread of life. Whoever comes to me will never go hungry.\" The non-satisfying labor of Isaiah 55:2 is the labor that produces \"food that spoils\" — Jesus identifies himself as the real food that satisfies the hunger which every substitute fails to address. The free invitation of v1 becomes the satisfying feast of v2 for those who come to Christ.</p>",
        "3": "<p>\"Incline your ear, and come to me; hear, that your soul may live; and I will make with you an everlasting covenant, my steadfast, sure love for David\" — the everlasting covenant (<em>bĕrît ʿôlām</em>) with David's sure mercies (<em>ḥasdê Dāwid hanneʾĕmānîm</em>). Acts 13:34: \"The fact that God raised him from the dead, never to decay, is stated in these words: 'I will give you the holy and sure blessings promised to David.'\" Paul's quotation of Isaiah 55:3 (LXX) is the only NT citation, applied to Christ's resurrection as the fulfillment of the Davidic covenant. The \"steadfast sure love for David\" = the indestructible covenant faithfulness that the resurrection proves — death could not hold the one to whom David's mercies belong. Hebrews 13:20: \"the God of peace, who through the blood of the eternal covenant brought back from the dead our Lord Jesus, that great Shepherd of the sheep.\" The everlasting covenant of Isaiah 55:3 is the eternal covenant sealed in Christ's blood.</p>",
        "4": "<p>\"Behold, I made him a witness to the peoples, a leader and commander for the peoples\" — the Davidic king as witness-leader-commander to the nations. The royal titles go beyond Israel to include the peoples (<em>lĕʾummîm</em>). Revelation 1:5: \"and from Jesus Christ, the faithful witness, the firstborn from the dead, and the ruler of the kings of the earth.\" Revelation 19:16: \"On his robe and on his thigh he has this name written: King of Kings and Lord of Lords.\" The threefold description of the Davidic king in Isaiah 55:4 (witness, leader, commander) maps onto the Revelation 1:5 description of Christ: \"faithful witness\" (= witness), \"firstborn from the dead\" (= the everlasting covenant confirmed by resurrection), \"ruler of the kings of the earth\" (= leader/commander to the peoples). The fulfillment is total and explicit in Revelation's identification of Christ with the titles of Isaiah 55:4.</p>",
        "5": "<p>\"Behold, you shall call a nation that you do not know, and a nation that did not know you shall run to you, because of the LORD your God, and of the Holy One of Israel, for he has glorified you\" — the Gentile mission: unknown nations running to the glorified Servant-King. The running is initiated by YHWH's glorification of the king. Romans 15:9-12: Paul's catena of OT texts for the Gentile mission, including \"Praise the Lord, all you Gentiles.\" Acts 28:28: \"Therefore I want you to know that God's salvation has been sent to the Gentiles, and they will listen!\" John 12:20-23: \"Now there were some Greeks among those who went up to worship at the festival. They came to Philip with a request. 'Sir,' they said, 'we would like to see Jesus.' Jesus replied, 'The hour has come for the Son of Man to be glorified.'\" The Greeks coming to see Jesus triggers his announcement of glorification — Isaiah 55:5's nations running to the glorified one enacted in John 12. The glorification is the cross-and-resurrection (John 12:24: the grain of wheat falling into the ground).</p>",
        "6": "<p>\"Seek the LORD while he may be found; call upon him while he is near\" — the urgent invitation with temporal limits: there is a window; seek while the seeking can succeed. The eschatological urgency is the flip side of the free invitation of v1. 2 Corinthians 6:2: \"For he says, 'In the time of my favor I heard you, and in the day of salvation I helped you.' I tell you, now is the time of God's favor, now is the day of salvation.\" Hebrews 3:13-15: \"But encourage one another daily, as long as it is called 'Today,' so that none of you may be hardened by sin's deceitfulness... Today, if you hear his voice, do not harden your hearts.\" The \"while he may be found\" of Isaiah 55:6 is the \"Today\" of Hebrews — the time-limited seeking that requires present response. The proclamation of Christ creates the window (the age of grace, the day of salvation); the return of Christ closes it (Matt 25:10-12: \"the door was shut\").</p>",
        "7": "<p>\"Let the wicked forsake his way, and the unrighteous man his thoughts; let him return to the LORD, that he may have compassion on him, and to our God, for he will abundantly pardon\" — the repentance-invitation with the promise of abundant pardon (<em>yarbeh lisĕlôaḥ</em>, the pardon-multiplication). The returning of v7 echoes Israel's return-narrative (Deut 30:2; Jer 3:22). Luke 15:17-20: \"'I will set out and go back to my father and say to him: Father, I have sinned against heaven and against you'... But while he was still a long way off, his father saw him and was filled with compassion for him.\" 1 John 1:9: \"If we confess our sins, he is faithful and just and will forgive us our sins and purify us from all unrighteousness.\" The \"abundant pardon\" of Isaiah 55:7 is the father-running-to-meet-the-returning-son of Luke 15 — and the forgiveness available because Christ absorbed the punishment is what makes the pardon both abundant and just (1 John 1:9 grounds forgiveness in Christ's faithfulness and justice).</p>",
        "8": "<p>\"For my thoughts are not your thoughts, neither are your ways my ways, declares the LORD\" — the opening of the divine transcendence argument (vv8-9): the foundational epistemological gap between divine and human reason. 1 Corinthians 1:18-21: \"For the message of the cross is foolishness to those who are perishing, but to us who are being saved it is the power of God... For the foolishness of God is wiser than human wisdom, and the weakness of God is stronger than human strength.\" Romans 11:33-34: \"Oh, the depth of the riches of the wisdom and knowledge of God! How unsearchable his judgments, and his paths beyond tracing out! Who has known the mind of the Lord?\" The \"thoughts not your thoughts\" of Isaiah 55:8 is the hermeneutic that explains the cross: no one reasoned their way to a crucified Messiah as the center of salvation history. The cross is the supreme instance of divine thoughts that are not human thoughts — wisdom concealed in apparent foolishness (1 Cor 2:7-8).</p>",
        "9": "<p>\"For as the heavens are higher than the earth, so are my ways higher than your ways and my thoughts than your thoughts\" — the cosmic scale of the gap: heaven-to-earth distance measures the divine-human thought-gap. The transcendence is vertical and absolute. Romans 9:20: \"But who are you, a human being, to talk back to God? 'Shall what is formed say to the one who formed it, \"Why did you make me like this?\"'\" Isaiah 45:9 (the potter-clay analogy) underlies Paul's argument. The height-of-heavens gap of Isaiah 55:9 is the gap that makes election mysterious (Romans 9-11) and the cross counter-intuitive (1 Cor 1). Ephesians 3:18-19: \"may have power, together with all the Lord's holy people, to grasp how wide and long and high and deep is the love of Christ, and to know this love that surpasses knowledge.\" The love that surpasses knowledge (Eph 3:19) is the Isaiah 55:9 ways that are higher than our ways — and its full expression is the cross.</p>",
        "10": "<p>\"For as the rain and the snow come down from heaven and do not return there but water the earth, making it bring forth and sprout, giving seed to the sower and bread to the eater\" — the rain-analogy for the divine word: rain descends purposefully and does not return until it has accomplished its purpose (vegetation, seed, bread). The analogy establishes the effectiveness of the word. John 1:14: \"The Word became flesh and made his dwelling among us.\" Hebrews 4:12: \"For the word of God is alive and active. Sharper than any double-edged sword, it penetrates even to dividing soul and spirit, joints and marrow; it judges the thoughts and attitudes of the heart.\" The rain/snow that comes from heaven and produces fruit is the type of the Word who descended from heaven (John 6:38: \"For I have come down from heaven not to do my will but to do the will of him who sent me\") and never returned empty — the resurrection is the return with abundant fruit (John 12:24: the grain of wheat that dies and bears much fruit).</p>",
        "11": "<p>\"So shall my word be that goes out from my mouth; it shall not return to me empty, but it shall accomplish that which I purpose, and shall succeed in the thing for which I sent it\" — the word's certain effectiveness: the divine speech-act that always accomplishes its intention. John 1:1-14: \"In the beginning was the Word... the Word became flesh.\" John 6:63: \"The Spirit gives life; the flesh counts for nothing. The words I have spoken to you — they are full of the Spirit and life.\" Isaiah 55:11 is the ground of missional confidence: the word preached cannot fail. Romans 10:14-17: \"How, then, can they call on the one they have not believed in? And how can they believe in the one of whom they have not heard?... faith comes from hearing the message, and the message is heard through the word about Christ.\" The word that \"shall not return empty\" is the proclaimed gospel — but behind the proclaimed word is the incarnate Word (John 1:14) who accomplished the Father's purpose perfectly and returned to the Father (John 17:4: \"I have brought you glory on earth by finishing the work you gave me to do\").</p>",
        "12": "<p>\"For you shall go out in joy and be led forth in peace; the mountains and the hills before you shall break forth into singing, and all the trees of the field shall clap their hands\" — the creation-chorus of the new exodus: mountains singing, trees applauding. The non-human creation participates in the homecoming. Romans 8:19-22: \"For the creation waits in eager expectation for the children of God to be revealed... the creation itself will be liberated from its bondage to decay and brought into the freedom and glory of the children of God... the whole creation has been groaning as in the pains of childbirth right up to the present time.\" Revelation 5:13: \"Then I heard every creature in heaven and on earth and under the earth and on the sea, and all that is in them, singing: 'To him who sits on the throne and to the Lamb be praise and honor and glory and power, for ever and ever!'\" The singing mountains and clapping trees of Isaiah 55:12 are the creation-wide praise of Revelation 5:13 — triggered by the Lamb's victory that sets creation free. The new creation in Christ (2 Cor 5:17) is the down payment on the cosmic liberation that culminates in every creature singing.</p>",
        "13": "<p>\"Instead of the thorn shall come up the cypress; instead of the brier shall come up the myrtle; and it shall make a name for the LORD, an everlasting sign that shall not be cut off\" — the thorn-to-cypress reversal: the curse-plants (thorns, briers — Genesis 3:18) replaced by noble trees (cypress, myrtle). The reversal of the curse. Galatians 3:13: \"Christ redeemed us from the curse of the law by becoming a curse for us, for it is written: 'Cursed is everyone who is hung on a pole.'\" The crown of thorns on Christ's head (John 19:2) is the thorns of Genesis 3 taken into himself — and the cypress-and-myrtle replacement is the new creation in which the curse is reversed. Revelation 22:3: \"No longer will there be any curse.\" The thorn-to-cypress of Isaiah 55:13 is the curse-to-blessing of the new creation, accomplished by Christ who wore the thorns and rose as the everlasting sign that shall not be cut off (the risen Christ who \"dies no more\", Rom 6:9).</p>"
    }
}


def main():
    existing = load_comm("mkt-christ", "isaiah")
    before = sum(len(v) for v in existing.values())
    merge_comm(existing, ISAIAH)
    after = sum(len(v) for v in existing.values())
    save_comm("mkt-christ", "isaiah", existing)
    print(f"{len(existing)} chapters, {after} verse entries total (+{after - before} new)")
    for v, kw in [("1", "thirsty"), ("3", "covenant"), ("11", "empty"), ("13", "thorn")]:
        entry = existing.get("55", {}).get(v, "MISSING")
        print(f"  Isa 55:{v} — {'OK' if kw.lower() in entry.lower() else 'CHECK'}")
    ch = existing.get("55", {})
    missing = [str(i) for i in range(1, 14) if str(i) not in ch]
    print(f"  Missing verses: {missing if missing else 'none'}")


if __name__ == "__main__":
    main()
