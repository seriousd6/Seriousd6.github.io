"""
MKT Christ Commentary — Isaiah chapter 52
Run: python3 scripts/zc-christ-isaiah-52.py

Isaiah 52 prepares for the Fourth Servant Song (52:13-53:12):
1. vv.1-6: Call to Zion to awake and put on her garments — the new exodus
2. vv.7-12: Herald of good news, YHWH returning to Zion, the new departure
3. v.13: Opening of the Fourth Servant Song (already present in output)
4. vv.14-15: The Servant's marred appearance and worldwide effect

Note: verse 13 already exists in output — merge_comm skips it safely.

Key Christological texts:
- 52:3: "redeemed without money" → 1 Pet 1:18-19 (ransom not with silver/gold)
- 52:7: "how beautiful are the feet" → Rom 10:15 (gospel proclamation)
- 52:10: "all ends of the earth shall see" → Luke 2:30-32; John 12:32
- 52:11: "come out from her" → 2 Cor 6:17; Rev 18:4
- 52:13: already present (exaltation of Servant)
- 52:14: marred appearance → John 19:1-5; Phil 2:7
- 52:15: sprinkling many nations → Rom 15:21 (Paul's mission citation)
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
  "52": {
    "1": '<p>"Awake, awake, put on your strength, O Zion; put on your beautiful garments, O Jerusalem, the holy city." The double "Awake, awake" mirrors 51:9 (the arm of YHWH awakening) — now the community is called to respond. Rev 21:2: "the holy city, new Jerusalem, coming down out of heaven from God, prepared as a bride adorned for her husband." Eph 5:27: "the church... in splendor, without spot or wrinkle or any such thing, that she might be holy and without blemish." The "beautiful garments" are the righteousness Christ provides: Rev 19:8 (the fine linen, bright and pure, is "the righteous deeds of the saints"); Isa 61:10 ("he has clothed me with the garments of salvation"). The call to awake is both eschatological and present: Rom 13:11 ("it is time for you to wake from sleep") applies the same awakening call to the church awaiting Christ\'s return.</p>',
    "2": '<p>"Shake yourself from the dust and arise, O captive Jerusalem; loose the bonds from your neck, O captive daughter of Zion." The prisoner told to remove her own bonds — the paradox of liberation that requires the liberated to participate. John 11:44: Lazarus comes out of the tomb still bound, and Jesus says "Unbind him, and let him go" — the act of loosing is given to the community to perform what Christ has accomplished. Gal 5:1: "For freedom Christ has set us free; stand firm therefore, and do not submit again to a yoke of slavery." The neck-bonds are the yoke of the law and sin; rising from dust is the resurrection posture of those who belong to the risen Lord. The command to "shake off the dust" (Matt 10:14) is Jesus\'s instruction to the disciples as they go out — the liberation Zion is offered becomes the posture of the gospel mission.</p>',
    "3": '<p>"For thus says YHWH: \'You were sold for nothing, and you shall be redeemed without money.\'" The costlessness of the sale and the costlessness of the redemption — but what costs nothing to the recipient cost everything to the Redeemer. 1 Pet 1:18-19: "you were ransomed from the futile ways inherited from your forefathers, not with perishable things such as silver or gold, but with the precious blood of Christ." Rev 22:17: "let the one who desires take the water of life without price." The "without money" (<em>lōʾ bĕḵesef</em>) redemption anticipates Isa 55:1 ("without money and without price") — the free offer of salvation that is free to receive but infinitely costly to provide. The apparent economy — sold for nothing, bought for nothing — conceals the price of the Son.</p>',
    "4": '<p>"For thus says the Lord YHWH: My people went down at the first into Egypt to sojourn there, and the Assyrian oppressed them for nothing." The review of Israel\'s exile history — Egypt and Assyria as types of captivity. Matt 2:13-15: the flight to Egypt and return fulfill Hos 11:1 ("out of Egypt I called my son") — Christ recapitulates Israel\'s Egypt sojourn in his infancy. The "for nothing" (<em>ʾēpōʾ mâ-lî-p̄ōh</em> — "what have I here?") oppression without cause is the oppression that Christ, the innocent one, endured supremely. The typological pattern: Egypt-bondage → Exodus-liberation is the meta-narrative that Christ\'s passion-resurrection enacts at cosmic scale (Luke 9:31: "his departure" — the Greek is <em>exodon</em>, exodus).</p>',
    "5": '<p>"Now therefore what have I here, declares YHWH, seeing that my people are taken away for nothing? Their rulers wail, declares YHWH, and continually all the day my name is despised." Paul quotes this verse in Rom 2:24: "The name of God is blasphemed among the Gentiles because of you" — applying the oracle to the moral failure of Jews in Rome whose conduct dishonors YHWH. The "name despised" because of the people\'s captivity becomes in the NT the name despised because of the community\'s hypocrisy. But the name is ultimately glorified through Christ: Phil 2:9-11 ("the name that is above every name, so that at the name of Jesus every knee should bow"). The desecration of the name in exile is answered by the exaltation of the name in resurrection.</p>',
    "6": '<p>"Therefore my people shall know my name. Therefore in that day they shall know that it is I who speak; here I am." The self-revelation of YHWH in the eschaton — "here I am" (<em>hinnēnî</em>). John 17:6: "I have manifested your name to the people whom you gave me out of the world." John 17:26: "I made known to them your name, and I will continue to make it known." John 8:24,28: "unless you believe that I am he, you will die in your sins... when you have lifted up the Son of Man, then you will know that I am he." The "I AM" declarations of Christ are the fulfillment of 52:6 — the people will "know his name" through the one who says "I am the way, the truth, and the life" (John 14:6). "Here I am" is both the prophetic messenger\'s response and the divine self-disclosure that Christ embodies.</p>',
    "7": '<p>"How beautiful upon the mountains are the feet of him who brings good news, who publishes peace, who brings good news of happiness, who publishes salvation, who says to Zion, \'Your God reigns.\'" The most celebrated gospel verse in the OT. Rom 10:15 quotes it as the basis for the preaching mission: "How are they to preach unless they are sent? As it is written, \'How beautiful are the feet of those who preach the good news!\'" The content of the good news is threefold: <em>šālôm</em> (peace), <em>ṭôb</em> (happiness/good), <em>yĕšûʿâ</em> (salvation — the same root as "Jesus"). The announcement "Your God reigns" (YHWH mālāk) = "the kingdom of God has come near" (Mark 1:15). The herald who runs to declare the king\'s victory is Christ — and those who follow him become heralds of the same message (the Great Commission, Matt 28:19-20).</p>',
    "8": '<p>"The voice of your watchmen — they lift up their voice; together they sing for joy; for eye to eye they see the return of YHWH to Zion." The watchmen seeing YHWH return to Zion — the eschatological vision of divine return. Luke 2:25-32: Simeon, who had waited for "the consolation of Israel," takes the child Jesus and says "my eyes have seen your salvation." John 1:14: "we have seen his glory, glory as of the only Son from the Father." Acts 1:10-11: two angels announce to the watching disciples that "this Jesus, who was taken up from you into heaven, will come in the same way as you saw him go." The watchmen of Isaiah 52:8 are simultaneously the prophets who saw Christ\'s coming, those who witnessed his incarnation, and the church that watches for his return.</p>',
    "9": '<p>"Break forth together into singing, you waste places of Jerusalem, for YHWH has comforted his people; he has redeemed Jerusalem." The desolate places breaking into song. Rev 21:1-5: "Behold, I am making all things new" — the waste places become the new Jerusalem. Isa 35:1-2: "the wilderness and the dry land shall be glad; the desert shall rejoice and blossom." Luke 19:40: "if these were silent, the very stones would cry out" — Jesus\'s response when the Pharisees demand silence from the disciples who are declaring him king; creation itself would join the singing of 52:9. The comfort and redemption of Jerusalem announced here is the subject of the entire second half of Isaiah (chs 40-66), fulfilled in Christ\'s "it is finished" (John 19:30).</p>',
    "10": '<p>"YHWH has bared his holy arm before the eyes of all the nations, and all the ends of the earth shall see the salvation of our God." The bared arm of YHWH — the divine warrior revealing his power. Luke 2:30-32: Simeon: "my eyes have seen your salvation that you have prepared in the presence of all peoples, a light for revelation to the Gentiles." John 12:32: "when I am lifted up from the earth, I will draw all people to myself." 1 Cor 1:24: "Christ crucified... the power of God" (<em>dynamin Theou</em>) — the cross is the bared arm of YHWH. The universal scope ("all the ends of the earth") is the Great Commission geography (Matt 28:19: "all nations") and the Pentecost reversal of Babel (Acts 2:5: "devout men from every nation under heaven"). The arm bared at the cross is the arm that gathers the nations.</p>',
    "11": '<p>"Depart, depart, go out from there; touch no unclean thing; go out from the midst of her; purify yourselves, you who bear the vessels of YHWH." The call to holy separation. 2 Cor 6:17 quotes this directly: "Therefore go out from their midst, and be separate from them, says the Lord." Rev 18:4: "Come out of her, my people, lest you take part in her sins." The "vessels of YHWH" — the temple vessels that the Babylonian priests were not to profane during the return — become in the NT the believers themselves: 2 Tim 2:21 ("a vessel for honorable use, set apart as holy, useful to the master of the house"). The call to depart from uncleanness is the holiness ethic of the new community, grounded in the purity Christ has provided.</p>',
    "12": '<p>"For you shall not go out in haste, and you shall not go in flight, for YHWH will go before you, and the God of Israel will be your rear guard." The new exodus that differs from the first: no haste, no panic (contrast Ex 12:11: "eat it in haste"). The un-panicked departure of those who trust in YHWH\'s protection before and behind. Phil 4:6-7: "do not be anxious about anything... and the peace of God... will guard your hearts and your minds in Christ Jesus." Matt 28:20: "I am with you always, to the end of the age" — the promise of divine presence going before and behind. Heb 13:5: "I will never leave you nor forsake you." The rear-guard YHWH is Christ who sent the Paraclete (John 14:16-17) as his presence after the ascension — the church moves through history neither in haste nor in fear because Christ guards both the advance and the retreat.</p>',
    "14": '<p>"As many were astonished at you — his appearance was so marred, beyond human semblance, and his form beyond that of the children of mankind." The Servant\'s disfigurement that shocks observers. John 19:1-5: after the scourging, Pilate presents the beaten Jesus to the crowd — "Behold the man!" (<em>Ecce homo</em>) — and the "man" is barely recognizable. Phil 2:7-8: "emptied himself, taking the form of a servant... he humbled himself by becoming obedient to the point of death." Isa 53:2-3 extends the description: "he had no form or majesty... he was despised and rejected." The astonishment (<em>šāmēm</em>) of v.14 is the stupefied horror of those who encounter the spectacle of divine suffering in human flesh — it is the astonishment of the cross, which Paul describes as "folly to those who are perishing" but "the power of God" to those being saved (1 Cor 1:18).</p>',
    "15": '<p>"So shall he sprinkle many nations; kings shall shut their mouths because of him; for that which has not been told them they shall see, and that which they have not heard they shall understand." The Servant who sprinkles the nations — the priestly act (<em>yazzeh</em>) applied to the Gentiles at cosmic scale. 1 Pet 1:2: believers are "chosen... for obedience to Jesus Christ and for sprinkling with his blood." Heb 9:13-14: the blood of Christ purifies the conscience. Rom 15:20-21 quotes v.15 directly as the mandate for Paul\'s mission to the unevangelized Gentiles: "I make it my ambition to preach the gospel, not where Christ has already been named... as it is written, \'Those who have never been told of him will see, and those who have never heard will understand.\'" The kings who shut their mouths is the NT pattern of earthly authority silenced before Christ: Matt 22:46 ("no one was able to answer him a word"), 27:12-14 (Jesus silent before Pilate; Pilate himself silenced by the crowd). The unanswerable Christ sprinkles all nations with his blood.</p>',
  },
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    # INTENT: Verify all 15 Isaiah 52 mkt-christ verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 52 verse count changes, update expected total
    # VERIFY: Console shows OK with 15 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-christ' / 'isaiah.json').read_text())
    missing = [v for v in il.get('52', {}) if v not in out.get('52', {})]
    if missing:
        print(f'  MISSING ch 52: {missing}')
    else:
        print(f'  OK: all Isaiah 52 mkt-christ verses present ({len(il.get("52", {}))} verses)')

if __name__ == '__main__':
    main()
