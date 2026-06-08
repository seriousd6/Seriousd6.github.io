"""
MKT Christ Commentary — Isaiah chapter 32
Run: python3 scripts/zc-christ-isaiah-32.py

Isaiah 32 divides into:
1. vv.1-8: The Righteous King oracle — the messianic king as shelter/refuge
2. vv.9-14: Oracle against the complacent women — judgment on the comfortable
3. vv.15-20: The Spirit-pouring transformation — wilderness to fruitful field,
   resulting in righteousness, peace, and security

Key Christological texts:
- 32:1-2: The king as hiding-place from storms → John 14:2-3; Rev 7:15
- 32:3-4: Eyes opened, ears hearing, tongue speaking → Matt 11:5; Isa 35:5-6
- 32:15: "until the Spirit is poured upon us from on high" → Acts 2:17-18;
  John 7:38-39 (rivers of living water = the Spirit)
- 32:17: "righteousness → peace" → Rom 5:1; Jas 3:18
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
  "32": {
    "1": '<p>"Behold, a king will reign in righteousness, and princes will rule in justice." The righteous king (<em>melek lĕṣedeq</em>) is the messianic portrait Isaiah develops across the book: 9:6-7 (Prince of Peace, reigning on David\'s throne), 11:1-5 (the Branch ruling with righteousness), 16:5 (the throne established in steadfast love). In the NT, Jesus enters Jerusalem as the king (Matt 21:5: "Behold, your king is coming to you" — citing Zech 9:9), is interrogated by Pilate as to whether he is the king of the Jews (John 18:37: "You say that I am a king. For this purpose I was born and for this purpose I have come into the world"), and will reign at his return (Rev 19:16: "King of kings and Lord of lords"). The "princes ruling in justice" are the apostles and elders who govern the new community under Christ\'s rule.</p>',
    "2": '<p>"Each will be like a hiding place from the wind, a shelter from the storm, like streams of water in a dry place, like the shade of a great rock in a weary land." The fourfold description of the righteous king as refuge — hiding place, shelter, streams, and shade — is applied Christologically across the NT. Rev 7:15: "he who sits on the throne will shelter them with his presence" (literally, "will spread his tent over them"). John 14:2-3: "In my Father\'s house are many rooms... I go to prepare a place for you." The "shade of a great rock in a weary land" connects to 1 Cor 10:4 (the rock in the wilderness was Christ). The streams of water in a dry place are the "rivers of living water" that Jesus promises in John 7:38 as the Spirit given to those who believe in him.</p>',
    "3": '<p>"Then the eyes of those who see will not be closed, and the ears of those who hear will give attention." The opened eyes and attentive ears under the righteous king directly reverse the hardening commission of 6:9-10. Matt 11:5 is Jesus\'s self-description fulfilling this reversal: "the blind receive their sight and the deaf hear." Isa 35:5-6 uses the same opened-eyes/opened-ears motif for the coming salvation — Jesus\'s healings of the blind (John 9) and the deaf (Mark 7:31-37) are the enacted demonstrations that the righteous king of Isaiah 32 has arrived. The kingdom opens what the hardening closes.</p>',
    "4": '<p>"The heart of the hasty will understand and know, and the tongue of the stammerers will hasten to speak distinctly." The transformation of the slow-of-understanding and the tongue-tied anticipates the Pentecost event (Acts 2:4: "they began to speak in other tongues as the Spirit gave them utterance") and the Great Commission\'s effect across languages and peoples. The "stammering tongue" (<em>lāšôn ʿilgîm</em>) connects to Isa 28:11 ("by people of strange lips and with a foreign tongue, YHWH will speak to this people") — the unintelligible becomes intelligible under the Spirit\'s giving. Rom 8:26 extends this: "the Spirit helps us in our weakness. For we do not know what to pray for as we ought, but the Spirit himself intercedes for us with groanings too deep for words."</p>',
    "5": '<p>"The fool will no more be called noble, nor the scoundrel said to be honorable." The eschatological reversal of false social honor is a consistent NT theme. Luke 16:15: "what is exalted among men is an abomination in the sight of God." Matt 23:27: "Woe to you, scribes and Pharisees, hypocrites! For you are like whitewashed tombs, which outwardly appear beautiful, but within are full of dead people\'s bones." 1 Cor 1:26-28: "not many of you were wise according to worldly standards, not many were powerful, not many were of noble birth... God chose what is foolish in the world to shame the wise." The reversal of fool/noble is enacted in the cross (the "foolishness" of God wiser than human wisdom, 1:25).</p>',
    "6": '<p>"For the fool speaks folly, and his heart is busy with iniquity, to practice ungodliness, to utter error concerning YHWH, to leave the craving of the hungry unsatisfied, and to deprive the thirsty of drink." The fool\'s heart busy with iniquity — specifically depriving the hungry and thirsty — is the anti-portrait of the righteous king who feeds and waters (v.2: streams in a dry place). Matt 25:41-45 presents the ultimate judgment on those who did not feed the hungry or give the thirsty a drink: "I was hungry and you gave me no food, I was thirsty and you gave me no drink." The fool of Isaiah 32:6 is the one who passes by the hungry in Matt 25 and the man beaten in the ditch (Luke 10:30-32).</p>',
    "7": '<p>"As for the scoundrel — his devices are evil; he plans wicked schemes to ruin the poor with lying words, even when the plea of the needy is right." The scoundrel who ruins the poor with lies is the anti-shepherd figure. John 10:10: "The thief comes only to steal and kill and destroy" — the thief who scatters and exploits the sheep. Matt 7:15-20: "Beware of false prophets, who come to you in sheep\'s clothing but inwardly are ravenous wolves." Rev 13:5-6: the beast who speaks arrogant words against God. The contrast between the scoundrel of Isaiah 32:7 and the righteous king of 32:1 is the contrast between the prince of this world and Christ.</p>',
    "8": '<p>"But he who is noble plans noble things, and on noble things he stands." The noble person (<em>nāḏîḇ</em>, generous/magnanimous) who plans and stands by generosity is the portrait of the servant-leader that Jesus embodies. Matt 5:3-12: the beatitudes describe the character of those in the kingdom — the poor in spirit, the meek, the merciful. Luke 8:15: the good soil that hears the word and holds it fast in "an honest and good heart" (<em>kardia kalē kai agathē</em>). The contrast with the fool (v.5-7) and the scoundrel (v.7) establishes the moral binary of Isaiah\'s wisdom theology, resolved in Christ who is the wisdom of God (1 Cor 1:30).</p>',
    "9": '<p>"Rise up, you women who are at ease, hear my voice; you complacent daughters, give ear to my speech." The prophetic address to the complacent women anticipates the parable of the ten virgins (Matt 25:1-13: five were foolish and unprepared; "watch therefore, for you know neither the day nor the hour") and the warnings against self-satisfied ease. Luke 12:19-20: the soul who says "eat, drink, be merry" is called a fool. Rev 3:17: the church at Laodicea "you say, I am rich, I have prospered, and I need nothing, not realizing that you are wretched, pitiable, poor, blind, and naked." The ease of Isaiah 32:9 is the spiritual complacency that all three texts warn against.</p>',
    "10": '<p>"In little more than a year you will shudder, you complacent women; for the grape harvest fails, the fruit harvest will not come." The sudden reversal of the comfortable harvest — "in a little more than a year" — is the pattern of sudden judgment. Luke 17:26-30: "Just as it was in the days of Noah... they were eating and drinking and buying and selling and planting and building, but on the day when Lot went out from Sodom, fire and sulfur rained from heaven." 1 Thess 5:3: "While people are saying, \'There is peace and security,\' then sudden destruction will come upon them as labor pains come upon a pregnant woman." The comfortable harvest that suddenly fails is the unguarded moment of Christ\'s coming (Matt 24:42-44).</p>',
    "11": '<p>"Tremble, you women who are at ease! Shudder, you complacent ones! Strip, and make yourselves bare, and tie sackcloth around your waist." The call to grief and mourning that shakes the comfortable is the posture of repentance. Jas 4:9: "Be wretched and mourn and weep. Let your laughter be turned to mourning and your joy to gloom. Humble yourselves before the Lord." Rev 18:7-8: the mourning for Babylon contrasted with her former luxury — "as she glorified herself and lived in luxury, so give her a like measure of torment and mourning." The sackcloth of Isaiah 32:11 is the voluntary grief of repentance as against the forced grief of judgment.</p>',
    "12": '<p>"Beat your breasts for the pleasant fields, for the fruitful vine." The mourning over lost agricultural fruitfulness is the lament over what pride and complacency destroyed. The beating of breasts — a gesture of grief — appears in Luke 23:48 at the crucifixion: "all the crowds... returned home beating their breasts." Luke 18:13: "the tax collector, standing far off, would not even lift up his eyes to heaven, but beat his breast, saying, \'God, be merciful to me, a sinner!\'" The voluntary breast-beating of repentance (Luke 18) is the appropriate response to the loss described in Isaiah 32 — grief that leads to the mercy Christ offers.</p>',
    "13": '<p>"For the soil of my people growing up in thorns and briers, yes, for all the joyful houses in the exultant city." The land reverting to thorns and briers — the judgment imagery of 5:6; 7:23-25 — connects directly to the curse of Gen 3:18 ("thorns and thistles it shall bring forth for you"). The crown of thorns at the crucifixion (Matt 27:29; John 19:2) is the symbolic condensation of the full curse: Christ wears the thorns of the judgment-land on his head. The "joyful houses" that fall silent anticipate the NT warnings about Jerusalem\'s coming desolation (Matt 23:38; Luke 19:43-44).</p>',
    "14": '<p>"For the palace is forsaken, the populous city deserted; the hill and the watchtower will become dens forever, a joy of wild donkeys, a pasture of flocks." The forsaken palace and deserted city is a type of the Jerusalem judgment that Jesus predicts (Luke 21:5-6: "As for these things that you see, the days will come when there will not be left here one stone upon another that will not be thrown down"). The desolation of what was formerly "the joy" of the city is the same pattern as Matt 23:38 ("your house is left to you desolate"). The watchtower that becomes a pasture for flocks anticipates the Good Shepherd who reclaims the abandoned land.</p>',
    "15": '<p>"Until the Spirit is poured upon us from on high, and the wilderness becomes a fruitful field, and the fruitful field is deemed a forest." The Spirit-pouring from on high is the Pentecost promise. Acts 2:17-18 applies Joel 2:28-32 to Pentecost, but the Isaianic background of Spirit-pouring upon the community (Isa 32:15; 44:3; Ezek 36:26-27) is the broader OT foundation. John 7:38-39: "\'Whoever believes in me, as the Scripture has said, rivers of living water will flow from his heart.\' Now this he said about the Spirit, whom those who believed in him were to receive, for as yet the Spirit had not been given, because Jesus was not yet glorified." The wilderness-to-fruitful-field transformation by the Spirit is the new creation that begins at Pentecost.</p>',
    "16": '<p>"Then justice will dwell in the wilderness, and righteousness abide in the fruitful field." The Spirit\'s transformation of the land produces justice and righteousness in the transformed landscape. Matt 6:33: "seek first the kingdom of God and his righteousness, and all these things will be added to you." Rom 14:17: "the kingdom of God is not a matter of eating and drinking but of righteousness and peace and joy in the Holy Spirit." The justice and righteousness that abide in the Spirit-transformed field are the character of the kingdom — not imposed by law but produced by the Spirit. Gal 5:22-23: the fruit of the Spirit is the new harvest of the fruitful field.</p>',
    "17": '<p>"And the effect of righteousness will be peace, and the result of righteousness, quietness and trust forever." The righteousness → peace sequence is Paul\'s atonement logic: "since we have been justified by faith, we have peace with God through our Lord Jesus Christ" (Rom 5:1). The righteousness achieved at the cross produces the peace — not the peace produced by human moral achievement but the peace given as the consequence of divine righteousness imputed to the believer. Jas 3:18: "a harvest of righteousness is sown in peace by those who make peace." Heb 12:11: "it yields the peaceful fruit of righteousness to those who have been trained by it." The "quietness and trust forever" is the eschatological security of those who are justified.</p>',
    "18": '<p>"My people will abide in a peaceful habitation, in secure dwellings, and in quiet resting places." The eschatological rest in peaceful dwellings is the fulfillment Christ brings. John 14:2-3: "In my Father\'s house are many rooms... I go to prepare a place for you." Heb 4:9-10: "there remains a Sabbath rest for the people of God, for whoever has entered God\'s rest has also rested from his works as God did from his." Rev 21:3: "Behold, the dwelling place of God is with man. He will dwell with them, and they will be his people, and God himself will be with them as their God." The peaceful habitation of Isaiah 32:18 is the final state of the new creation — God and his people dwelling together in the rest Christ has prepared.</p>',
    "19": '<p>"And it will hail when the forest falls down, and the city will be utterly laid low." The hailstorm judgment that precedes the ultimate peace anticipates the apocalyptic hail sequences of Revelation: 8:7 (first trumpet: hail and fire mixed with blood); 11:19 (the temple opened, hailstorm); 16:21 (the seventh bowl: great hailstones). The falling of the forest and city is the judgment that clears the way for the new creation. The pattern is always: judgment on the old order, then the establishment of the peaceful habitation (v.18). Christ comes first as the one who endures the storm (8:24: "he rebuked the wind and the sea"); at his return, the storm of judgment clears the way for the new dwelling.</p>',
    "20": '<p>"Happy are you who sow beside all waters, who let the feet of the ox and the donkey range free." The beatitude-form (<em>ʾašrêkem</em>, "happy/blessed are you") that closes the chapter echoes the beatitude tradition of Psalms and the Sermon on the Mount (Matt 5:3-12). "Sowing beside all waters" is the fruitful labor of the Spirit-filled new creation — Isa 55:10-11 (the rain that makes the earth fruitful, like the word that accomplishes its purpose); John 12:24 (the grain that falls into the ground and dies brings forth much fruit). The ox and donkey ranging free recall the animals of Christ\'s entry into Jerusalem (Matt 21:2-5: "untie the donkey and the colt") and the manger scene (Luke 2:7) — the humble animals of labor free in the new creation\'s rest.</p>',
  },
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    # INTENT: Verify all 20 Isaiah 32 mkt-christ verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 32 verse count changes, update expected total
    # VERIFY: Console shows OK with 20 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-christ' / 'isaiah.json').read_text())
    missing = [v for v in il.get('32', {}) if v not in out.get('32', {})]
    if missing:
        print(f'  MISSING: {missing}')
    else:
        print(f'  OK: all Isaiah 32 mkt-christ verses present ({len(il.get("32", {}))} verses)')

if __name__ == '__main__':
    main()
