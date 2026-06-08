"""
MKT Original Commentary — Isaiah chapter 59
Run: python3 scripts/zc-original-isaiah-59.py

Isaiah 59 is the great diagnostic of sin's barrier between YHWH and his people,
culminating in YHWH's unilateral intervention as divine warrior when no human
mediator is found. The chapter is one of Paul's most-used OT passages.

Key translation decisions:
- 59:2 mabdîlîm: "separating/making a division" — the metaphor of sin as a wall
  that divides rather than as guilt that requires payment.
- 59:7-8: Paul quotes these verses in Rom 3:15-17 as part of his universal
  indictment (the "catena" of OT sin texts in Rom 3:10-18).
- 59:16-17: YHWH dons armor — ṣĕdāqâ (righteousness) as breastplate,
  yĕšûʿâ (salvation) as helmet. Paul reconfigures this armor for the believer
  in Eph 6:14-17: the armor of God that the divine warrior wore is given to those
  who are in Christ.
- 59:20: Rom 11:26 quotes "the Deliverer will come from Zion" to argue that
  Israel's partial hardening is temporary; the eschatological Deliverer is Christ.
- 59:21: The new covenant of the Spirit and the Word — the Spirit placed on the
  Servant/community, and the word placed in their mouths, will never depart.
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
  "59": {
    "1": '<p><strong>hēn lōʾ-qāṣĕrâ yad-Yhwh mîhôšîaʿ</strong> — "the hand of YHWH is not too short to save" — the opening refutation of a false diagnosis. The same rhetorical question about YHWH\'s "shortened hand" appears in 50:2 as a challenge to Israel; here it is answered before it is asked. <strong>wĕlōʾ-kābĕḏâ ʾoznô miššĕmôaʿ</strong> — "nor is his ear heavy from hearing" — deafness and weakness are both denied. The problem is not YHWH\'s incapacity but the people\'s moral condition (v.2).</p>',
    "2": '<p><strong>kî ʾim-ʿăwōnōtêkem hāyû mabdîlîm bênêkem ûbên ʾĕlōhêkem</strong> — "but your iniquities have separated (<em>bāḏal</em>, H914, to divide, to make a distinction) you from your God" — the theology of sin as relational separation rather than merely legal violation. The iniquities have become a wall between parties who should be together. <strong>wĕḥaṭṭōʾôtêkem histîrû pānîm mikkkem</strong> — "and your sins have hidden his face from you" — the hiding of YHWH\'s face (<em>histîr pānîm</em>) is the withdrawal of his covenantal presence, the most serious covenant judgment (cf. Ps 13:1; 27:9; Isa 8:17).</p>',
    "3": '<p><strong>kî kappêkem niggĕʾălû baddām</strong> — "for your hands are defiled with blood" (<em>gāʾal</em>, H1351, to defile/desecrate — a cultic term for making unclean). <strong>wĕʾeṣbĕʿōtêkem beʿāwōn śipĕtôtêkem dibbĕrû-šeqer</strong> — "and your fingers with iniquity; your lips have spoken lies." The anatomy of sin — hands, fingers, lips, tongue — covers the full range of sinful actions from violent deed to deceptive speech. The inventory of body parts implicated in sin is similar to Paul\'s catena in Rom 3:13-17.</p>',
    "4": '<p><strong>ʾên-qōrēʾ ḇĕṣedeq wĕʾên nišpāṭ beʾĕmûnâ</strong> — "no one calls out in righteousness, and no one pleads in faithfulness" — the legal domain (calling out for justice, pleading before courts) is corrupted. <strong>bāṭôaḥ ʿal-tōhû wĕdabbēr-šāwĕʾ hārô ʿāmāl wĕhôlîḏ ʾāwen</strong> — "trusting in chaos and speaking lies; they conceive mischief and give birth to iniquity" — the reproduction metaphor (<em>hārâ</em>, to conceive; <em>yālad</em>, to give birth) frames sin as generative, producing offspring that continue beyond the original act.</p>',
    "5": '<p><strong>bêṣê ṣipʿônî biqēʿû</strong> — "they hatch the eggs of a viper" (<em>ṣipʿônî</em>, H6848, a venomous serpent — adder or cobra). <strong>wĕqûrê ʿakkābîš yĕʾōrōgû</strong> — "and weave the spider\'s web." The viper-egg and spider-web pair the production of lethal poison with the crafting of deceptive traps. The hatchlings of the viper become serpents (v.5b), and the spider\'s web is useless as covering (v.6). Both images describe sin that appears productive but produces only danger and futility.</p>',
    "6": '<p><strong>qûrêhem lōʾ-yihyû lĕbegeḏ wĕlōʾ yitkassû bĕmaʿăśêhem</strong> — "their webs will not serve as clothing; they cannot cover themselves with what they have made" — the futility of sinful manufacture. The spider\'s web looks like fabric but provides neither covering nor warmth. <strong>maʿăśêhem maʿăśê-ʾāwen ûpōʿal ḥāmās bĕkappêhem</strong> — "their works are works of iniquity, and deeds of violence are in their hands" — the climax of the body-inventory that began in v.3.</p>',
    "7": '<p><strong>raglêhem lārāʿ yārûṣû</strong> — "their feet run to evil" — the swiftness of sin. Paul quotes vv.7-8 in Rom 3:15-17 as part of his catena of OT sin-texts proving universal human guilt: "Their feet are swift to shed blood; in their paths are ruin and misery; and the way of peace they have not known." <strong>ûmahărû lišpōk dam-nāqî</strong> — "and they hurry to shed innocent blood" (<em>dam nāqî</em>, innocent blood — a category of sin that defiles the land, Num 35:33; Deut 19:10).</p>',
    "8": '<p><strong>derekh šālôm lōʾ yāḏĕʿû</strong> — "the way of peace (<em>šālôm</em>) they do not know" — the absence of peace-knowledge is a comprehensive moral description: they neither know how to make peace nor recognize it. <strong>wĕʾên mišpāṭ bĕmaʿgĕlôtām</strong> — "there is no justice in their tracks." <strong>nĕtîḇōtêhem ʿiqqĕšû lāhem</strong> — "their paths they have made crooked for themselves" (<em>ʿāqaš</em>, H6140, to make crooked/perverse). Paul uses this verse in Rom 3:17 to close the catena, making peace-ignorance the capstone of the universal human condition before Christ.</p>',
    "9": '<p><strong>lāken rāḥaq mimmennû mišpāṭ wĕlōʾ taśśîgēnû ṣĕdāqâ</strong> — "therefore justice is far from us, and righteousness does not reach us" — the community shifts to first-person confession. The distance of justice is not cosmic but self-created: they have driven it away through the behaviors of vv.3-8. <strong>nĕqawweh lāʾôr wĕhinnēh-ḥōšek</strong> — "we wait for light but behold, darkness" — the inversion of expectation: salvation anticipated but darkness experienced.</p>',
    "10": '<p><strong>nĕgašĕšâ kĕʿiwrîm qîr ûkĕʾên ʿênayim nĕgašēšâ</strong> — "we grope for the wall like the blind; we grope like those who have no eyes" — the blindness metaphor extends the darkness of v.9 to incapacity for navigation. <strong>kāšalnû ḇāṣŏhorāyim kānešep</strong> — "we stumble at noon as in the twilight" — the paradox of midday darkness (cf. Deut 28:29: the covenant curse of groping at noon). <strong>bammĕšammānîm kayyĕmētîm</strong> — "among those in their prime, we are like dead men."</p>',
    "11": '<p><strong>nĕhĕmeh kaddōbîm kullānû</strong> — "we all growl like bears" (<em>hāmâ</em>, H1993, to growl/roar/groan). <strong>wĕkayyônîm hāgōh nĕhgeh</strong> — "and moan plaintively like doves" — the contrast of bear-growl and dove-coo captures the double register of the community\'s anguish: fierce desperation and plaintive mourning together. <strong>nĕqawweh lammišpāṭ wĕʾayin lîšûʿâ rāḥăqâ mimmennû</strong> — "we wait for justice but there is none; for salvation, but it is far from us" — the waiting (<em>qāwâ</em>, cf. 25:9; 40:31) produces only distance, not arrival.</p>',
    "12": '<p><strong>kî rabbû pĕšāʿênû negd-eykā wĕḥaṭṭōʾôtênû ʿānnâ bānû</strong> — "for our transgressions are multiplied before you, and our sins testify against us" (<em>ʿānâ</em>, H6030, to testify, to answer back — the sins become witnesses in the divine court). <strong>pĕšāʿênû ʾittānû waʿăwōnōtênû yĕdaʿănûm</strong> — "our transgressions are with us, and we know our iniquities" — the confession deepens: the sins are present (not past), known (not hidden), and multiple.</p>',
    "13": '<p><strong>pāšôaʿ ûkahēš bYhwh ûnāsôg mēʾaḥar ʾĕlōhênû</strong> — "transgressing and denying YHWH, and turning away from following our God" — the three-fold pattern: transgression (active violation), denial (of YHWH\'s claims), and retreat (withdrawal from his following). <strong>dabbēr-ʿōšeq wĕsārâ hārô wĕhāgô millib dĕḇārê-šāqer</strong> — "speaking oppression and revolt, conceiving and uttering from the heart lying words." The origin of the lying words is the heart (<em>lēḇ</em>) — the seat of moral orientation in Hebrew anthropology.</p>',
    "14": '<p><strong>wĕhussag ʾāḥôr mišpāṭ</strong> — "justice is turned back" (<em>nāsag</em>, H5253, to be driven back, to retreat) — the reversal of the proper order: what should advance (justice) retreats; what should come near (righteousness) stands far away. <strong>ûṣĕdāqâ mērāḥôq taʿămod</strong> — "and righteousness stands far off." <strong>kî-kāšĕlâ bāreḥôḇ ʾĕmet</strong> — "for truth has stumbled in the public square (<em>rĕḥôb</em>)" — the public legal space (the city gate) has become a place where truth falls. <strong>wĕnĕkōḥâ lōʾ-tûkal lābôʾ</strong> — "and integrity cannot enter."</p>',
    "15": '<p><strong>wattĕhî hāʾĕmet neʿĕderet</strong> — "truth has disappeared/is absent" (<em>ʿādar</em>, H5737, to be absent, to be lacking — the same root as the shepherd who calls his sheep and one is missing). <strong>wĕsār mērāʿ mištōlēl</strong> — "and the one who turns from evil makes himself a prey (<em>šālal</em>)" — the moral inversion: righteousness is predatory behavior. <strong>wayyar Yhwh wayyeraʿ bĕʿênāyw kî ʾên mišpāṭ</strong> — "YHWH saw it, and it displeased him that there was no justice" — the divine observation (<em>rāʾâ</em>) and moral response (<em>rāʿaʿ bĕʿênāyw</em>, evil in his eyes) introduce the divine intervention of vv.16-17.</p>',
    "16": '<p><strong>wayyar kî-ʾên ʾîš wayyištômem kî ʾên maphgîaʿ</strong> — "he saw that there was no man, and was appalled (<em>šāmam</em>, H8074, to be desolate, horrified) that there was no one to intercede (<em>pāgaʿ</em>, H6293, to intercede, to meet/touch — the intercessor makes contact between two parties)" — the divine horror at the total vacuum of human mediation. No prophet, no priest, no judge, no king can mediate between YHWH and the people. <strong>wayyôšaʿ lô zĕrōʿô ûṣiḏqātô hîʾ sĕmākātthu</strong> — "his own arm brought him salvation, and his righteousness supported him" — YHWH becomes his own mediator.</p>',
    "17": '<p><strong>wayyilbaš ṣĕdāqâ kašširyôn</strong> — "he put on righteousness as a breastplate" (<em>širyôn</em>, H8302, coat of mail/breastplate). <strong>wĕkôbaʿ yĕšûʿâ bĕrōʾšô</strong> — "and a helmet of salvation on his head" (<em>kôbaʿ</em>, H3553, helmet). Paul in Eph 6:14,17 distributes this armor to the believer: "having put on the breastplate of righteousness... take the helmet of salvation." What YHWH wore as the divine warrior is now given to those who are in Christ to wear. <strong>wayyilbaš bigdê nāqām tilibūšet</strong> — "he put on garments of vengeance for clothing" — and wrapped himself in zeal (<em>qinʾâ</em>) as a mantle.</p>',
    "18": '<p><strong>kĕʿal gĕmûlôt kĕʿal yĕšallēm</strong> — "according to their deeds, so he will repay" — the retributive formula. The recompense is distributed to three groups: <em>ṣārāyw</em> (his adversaries), <em>ʾōyĕḇāyw</em> (his enemies), and the coastlands (<em>ʾiyyîm</em>) — i.e., the full width of opposition, from close enemies to the distant nations. The divine warrior\'s campaign addresses the complete spectrum of those who oppose YHWH\'s covenant purposes.</p>',
    "19": '<p><strong>wĕyîrĕʾû mimmāʿăraḇ ʾet-šēm Yhwh ûmimmiẑraḥ-šemeš ʾet-kĕḇōḏô</strong> — "they will fear the name of YHWH from the west, and his glory from the rising of the sun" — the universal fear (reverence/worship) that results from the divine warrior\'s actions. East and west together represent the totality of geographic space. <strong>kî-yābōʾ kanāhār ṣār rûaḥ Yhwh nōssĕsâ bô</strong> — "for the enemy will come like a rushing stream; the Spirit of YHWH will drive him away" — a difficult verse: either the enemy comes like a flood and YHWH\'s Spirit drives him away, or YHWH himself comes as a flood-tide driven by his Spirit.</p>',
    "20": '<p><strong>ûḇāʾ lĕṣiyyôn gōʾēl</strong> — "a Redeemer (<em>gōʾēl</em>, H1350, the kinsman-redeemer) will come to Zion" — the arrival formula. Paul quotes this in Rom 11:26 ("and in this way all Israel will be saved, as it is written, \'The Deliverer will come from Zion\'") to argue that Israel\'s partial hardening (11:25) is temporary — the eschatological Deliverer (Christ at his return) will complete what the current mission to the gentiles is preparing. <strong>ûlĕšābê pešaʿ bĕyaʿăqōb</strong> — "and to those who turn from transgression in Jacob" — the <em>gōʾēl</em>\'s arrival is conditioned by repentance, or more precisely, his arrival produces repentance.</p>',
    "21": '<p><strong>wĕʾănî zōʾt bĕrîtî ʾôtām ʾāmar Yhwh</strong> — "as for me, this is my covenant with them, says YHWH" — the covenant formula introducing the new covenant elements. <strong>rûḥî ʾăšer ʿāleykā ûdĕḇāray ʾăšer-śamtî bĕpîkā</strong> — "my Spirit that is upon you and my words that I have placed in your mouth" — the two covenant instruments: Spirit and Word. <strong>lōʾ-yāmûšû mipîkā ûmippî zarʿăkā ûmippî zeraʿ zarʿăkā</strong> — "shall not depart from your mouth, nor from the mouth of your offspring, nor from the mouth of your offspring\'s offspring" — the triple-generation promise makes the covenant\'s persistence explicit: Spirit-and-Word covenant is permanent across generations. This new covenant of Spirit and Word is what Jer 31:33 and Ezek 36:27 also describe.</p>',
  },
}

def main():
    existing = load_comm('mkt-original', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-original', 'isaiah', existing)
    # INTENT: Verify all 21 Isaiah 59 mkt-original verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 59 verse count changes, update expected total
    # VERIFY: Console shows OK with 21 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-original' / 'isaiah.json').read_text())
    missing = [v for v in il.get('59', {}) if v not in out.get('59', {})]
    if missing:
        print(f'  MISSING: {missing}')
    else:
        print(f'  OK: all Isaiah 59 mkt-original verses present ({len(il.get("59", {}))} verses)')

if __name__ == '__main__':
    main()
