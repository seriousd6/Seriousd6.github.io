"""
MKT Christ Commentary — Isaiah chapter 47
Run: python3 scripts/zc-christ-isaiah-47.py

Isaiah 47 is the taunt-song against Babylon personified as a proud queen
who will be humiliated. Structurally this is the opposite of the Servant
Songs in chs 42-53: the Servant empties himself and is exalted; Babylon
exalts herself and is emptied.

Key Christological texts:
- 47:4: "Our Redeemer — YHWH of hosts" → Luke 1:68; Rev 5:9 (Christ as gōʾēl)
- 47:7-8: Babylon's "I am, I alone" self-deification → John 8:58 (Christ's true I AM)
- 47:8: "I shall not sit as a widow" → Rev 18:7 (direct quotation)
- 47:9: "in one day" sudden judgment → Rev 18:8 (same phrase)
- 47:13: astrologers who cannot save → Matt 2:1-12 (Magi led to Christ by stars)
- 47:15: "no one to save you" → contrast with Rom 8:38-39 (nothing separates from Christ)
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
  "47": {
    "1": '<p>"Come down and sit in the dust, O virgin daughter of Babylon; sit on the ground without a throne." The humiliation of the enthroned queen — forced from her throne to the dust. Rev 18:7-8 quotes and expands this scene directly: Babylon "glorified herself and lived in luxury" but in one day comes mourning, famine, and fire. The contrast with Christ is the structural heart of Second Isaiah: Babylon descends from throne to dust because of pride; Christ descends from throne to manger and cross (Phil 2:6-8: "though he was in the form of God, he did not count equality with God a thing to be grasped, but emptied himself"), and is consequently exalted above all (Phil 2:9-11). The dust-throne reversal is the anti-pattern of Christological kenosis-and-exaltation.</p>',
    "2": '<p>"Take the millstones and grind flour; remove your veil, strip off your robe, uncover your legs, pass through the rivers." The forced labor and stripping of Babylon\'s queen — what Babylon imposed on Israel\'s captives is now imposed on her. Matt 18:33-34: the unmerciful servant who was forgiven but showed no mercy is handed over to the torturers — the principle of reciprocal judgment. Rev 17:16: "the ten horns that you saw, they and the beast will hate the prostitute. They will make her desolate and naked, and devour her flesh and burn her up with fire." The stripping is the eschatological reversal administered by the very powers Babylon used: the woman stripped to shame is the anti-type of those whom Christ clothes in white garments of righteousness (Rev 3:18; 7:9).</p>',
    "3": '<p>"Your nakedness shall be uncovered, and your disgrace shall be seen. I will take vengeance, and I will spare no one." The divine declaration of vengeance — YHWH himself will expose Babylon\'s shame. Rom 12:19: "Beloved, never avenge yourselves, but leave it to the wrath of God, for it is written, \'Vengeance is mine, I will repay, says the Lord.\'" Rev 6:10: the martyrs under the altar cry "how long before you will judge and avenge our blood?" The divine vengeance that God reserves to himself is executed through Christ at the parousia (2 Thess 1:8: "inflicting vengeance on those who do not know God"). The statement "I will spare no one" is the counterpoint to "he who did not spare his own Son but gave him up for us all" (Rom 8:32) — divine wrath either falls on the Son or on the unrepentant.</p>',
    "4": '<p>"Our Redeemer — YHWH of hosts is his name — is the Holy One of Israel." The doxological aside in the middle of the taunt song announces the identity of Babylon\'s adversary. The term <em>gōʾēl</em> (kinsman-redeemer) denotes the family member who pays the debt, redeems the enslaved, and avenges the murdered. Luke 1:68: Zechariah\'s Benedictus: "he has visited and redeemed his people." Gal 3:13: "Christ redeemed us from the curse of the law by becoming a curse for us." Rev 5:9: "by your blood you ransomed people for God from every tribe and language and people and nation." The Redeemer who stands against Babylon is Christ — YHWH of hosts in human flesh — who paid the price Babylon cannot.</p>',
    "5": '<p>"Sit in silence, and go into darkness, O daughter of the Chaldeans; for you shall no more be called the mistress of kingdoms." The kingdom that called itself eternal is silenced. Rev 18:2: "Babylon the great has fallen, has fallen." Rev 11:15: "the kingdom of the world has become the kingdom of our Lord and of his Christ, and he shall reign forever and ever." Dan 7:14 (the Son of Man): "his dominion is an everlasting dominion, which shall not pass away, and his kingdom one that shall not be destroyed." The silence and darkness into which Babylon sinks is the permanent end of the counterfeit kingdom — replaced by the eternal reign of Christ who is "Lord of lords and King of kings" (Rev 17:14).</p>',
    "6": '<p>"I was angry with my people; I profaned my heritage; I gave them into your hand; you showed them no mercy; on the aged you made your yoke exceedingly heavy." YHWH gave his people into Babylon\'s hand as an instrument of judgment — but Babylon exceeded her mandate by showing no mercy to the vulnerable. Matt 18:32-35: the unmerciful servant parable — "I forgave you all that debt because you pleaded with me. And should not you have had mercy on your fellow servant, as I had mercy on you?" Jas 2:13: "judgment is without mercy to one who has shown no mercy." The instrument of judgment that shows no mercy to the aged is judged without mercy. Christ, who bore the full weight of judgment, is the one who establishes a new community that shows mercy precisely because mercy has been shown to them (Matt 5:7).</p>',
    "7": '<p>"You said, \'I shall be mistress forever,\' so that you did not lay these things to heart or remember their end." The refusal to think about one\'s end (<em>ʾaḥărîtāh</em>) — the last things — is the spiritual blindness Christ repeatedly warns against. Luke 12:19-20: the rich fool who builds barns and says "eat, drink, be merry" does not "lay to heart" his end (God says "Fool! This night your soul is required of you"). Heb 2:1: "we must pay much closer attention to what we have heard, lest we drift away from it." Rev 18:7: "she says in her heart, \'I sit as a queen, I am no widow, and mourning I shall never see\'" — the direct NT echo of Isaiah 47:7 in the eschatological vision. The eternal mastership claimed by Babylon is the self-deification that Christ alone legitimately possesses.</p>',
    "8": '<p>"Now therefore hear this, you lover of pleasures, who sit securely, who say in your heart, \'I am, and there is no one besides me; I shall not sit as a widow or know the loss of children.\'" The divine-name formula "I am, and there is no one besides me" (<em>ʾănî wĕʾap̄sî ʿôḏ</em>) appears in Isaiah as YHWH\'s exclusive self-declaration (45:5-6,18,21-22; 46:9). Here Babylon steals it. John 8:58: "before Abraham was, I am (<em>egō eimi</em>)" — Christ\'s claim to the name, which the crowd treats as blasphemy (8:59). The entire chapter is structured around the contrast: the one who legitimately says "I AM" (Christ/YHWH) vs. the one who blasphemously usurps it (Babylon/every worldly power). Rev 18:7 quotes v.8b directly as Babylon\'s fatal self-deception.</p>',
    "9": '<p>"Both these things shall come upon you suddenly, in one day: the loss of children and widowhood shall come upon you in full measure, in spite of your many sorceries and the great power of your enchantments." The suddenness of Babylon\'s fall — "in one day." Rev 18:8: "For this reason her plagues will come in a single day, death and mourning and famine, and she will be burned up with fire; for mighty is the Lord God who has judged her." Luke 17:29-30: "on the day when Lot went out from Sodom, fire and sulfur rained from heaven and destroyed them all — so will it be on the day when the Son of Man is revealed." The "one day" of Babylon\'s judgment is the template for the eschatological day of Christ\'s coming — sudden, total, irresistible despite all protective powers.</p>',
    "10": '<p>"You felt secure in your wickedness; you said, \'No one sees me.\'" The delusion of invisible wickedness — "no one sees me." Heb 4:13: "no creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account." John 2:25: Jesus "knew what was in man" — he saw Nicodemus\'s real question (3:2), the woman at the well\'s actual history (4:17-18), and the Pharisees\' murderous thoughts (8:40). Prov 15:3: "the eyes of YHWH are in every place, keeping watch on the evil and the good." The illusion of concealed wickedness that Babylon maintains is shattered by the one who is the Word that penetrates to the division of soul and spirit (Heb 4:12). "I am, and there is no one besides me" appears again (v.10b) — the second instance of the stolen divine name.</p>',
    "11": '<p>"But evil shall come upon you, which you will not know how to charm away; disaster shall fall upon you, for which you will not be able to atone (<em>kappĕrāh</em>); and ruin shall come upon you suddenly, of which you know nothing." The disaster that cannot be atoned for — <em>kappĕrāh</em>, the atonement/ransom word. No ritual, no payment, no magic can avert it. Heb 10:26-28: "if we go on sinning deliberately after receiving the knowledge of the truth, there no longer remains a sacrifice for sins, but a fearful expectation of judgment." The contrast: Christ\'s atonement (<em>kippēr</em>) covers the sin of his people (Rom 3:25: <em>hilastērion</em>, the propitiation/mercy-seat); Babylon has no atonement available because she has rejected the Redeemer (v.4). The "disaster for which you cannot atone" is only avoided by those for whom Christ has provided the atonement.</p>',
    "12": '<p>"Stand fast in your enchantments and your many sorceries, with which you have labored from your youth; perhaps you may be able to succeed; perhaps you may inspire terror." The ironic divine permission — "try all your powers." Rev 9:20-21: after the plagues of the trumpets, "the rest of mankind, who were not killed by these plagues, did not repent of the works of their hands nor give up worshiping demons and idols... nor did they repent of their murders or their sorceries." Acts 8:9-13: Simon Magus, who "amazed the nation of Samaria, saying that he himself was somebody great," is himself amazed when Philip performs signs in Christ\'s name — the sorcery tradition silenced before the power of the gospel. The enchantments that cannot save Babylon are the "empty philosophy" (Col 2:8) that Christ disarmed at the cross (Col 2:15).</p>',
    "13": '<p>"You are wearied with your many counsels; let them stand forth and save you, those who divide the heavens, who gaze at the stars, who at the new moons make known what shall come upon you." The astrologers and star-dividers — the counselors who read the heavens but cannot save. Matt 2:1-12: the Magi (astrologers from the East) follow a star — but the star leads not to Babylon\'s counsel but to Christ. The heavens that Babylon\'s specialists "divide" are the heavens that declare the glory of God (Ps 19:1) and that pointed the Gentile wise men to the child who is "the light of the world" (John 8:12). Col 2:8: "elemental spirits of the world" (<em>stoicheia tou kosmou</em>) — the cosmic powers that Babylon\'s astrologers consulted are the same powers that Christ triumphed over at the cross (Col 2:15). The star-gazers are weary; the star leads to rest (Matt 2:9-10).</p>',
    "14": '<p>"Behold, they are like stubble; the fire consumes them; they cannot deliver themselves from the power of the flame. No coal for warming oneself is this, no fire to sit before!" The fire that consumes the counselors — not a useful fire for warmth, only the fire of judgment. Matt 3:12: "the chaff he will burn with unquenchable fire." Heb 12:29: "our God is a consuming fire." The distinction between the fire that warms and the fire that destroys is the distinction between the Spirit\'s fire (Matt 3:11: "he will baptize you with the Holy Spirit and fire") that refines, and the eschatological fire that consumes the stubble. Rev 20:15: "if anyone\'s name was not found written in the book of life, he was thrown into the lake of fire." The counselors consumed by fire are the contrast to those warmed by the Spirit\'s fire in Acts 2 (tongues of fire, Acts 2:3).</p>',
    "15": '<p>"Such to you are those you have labored with, who have done business with you from your youth; they wander about, each in his own direction; there is no one to save you." The abandonment at the moment of judgment — all trading partners scatter, no one saves. Rev 18:9-19: the kings, the merchants, the seafarers all "stand far off" and weep for Babylon but cannot help — the desertion is exact. The final words "there is no one to save you" (<em>ʾên môšîaʿ lāk</em>) are the negative of the promise of the Servant/Messiah whose very name "Jesus" (Yēšûaʿ) means "YHWH saves." Isa 43:11: "I, I am YHWH, and besides me there is no savior." Rom 8:38-39: "neither angels nor rulers, nor things present nor things to come, nor powers... will be able to separate us from the love of God in Christ Jesus our Lord." What no one can do for Babylon — save her — the Redeemer (v.4) accomplishes for those who are his.</p>',
  },
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    # INTENT: Verify all 15 Isaiah 47 mkt-christ verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 47 verse count changes, update expected total
    # VERIFY: Console shows OK with 15 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-christ' / 'isaiah.json').read_text())
    missing = [v for v in il.get('47', {}) if v not in out.get('47', {})]
    if missing:
        print(f'  MISSING: {missing}')
    else:
        print(f'  OK: all Isaiah 47 mkt-christ verses present ({len(il.get("47", {}))} verses)')

if __name__ == '__main__':
    main()
