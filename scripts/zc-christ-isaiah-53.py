"""
MKT Christ Commentary — Isaiah chapter 53
Run: python3 scripts/zc-christ-isaiah-53.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Note: verses 5 and 11 are already present; merge_comm will skip them.

Key decisions in this range:
- v. 1: unbelief at the Servant — direct: John 12:38; Rom 10:16
- v. 4: bore our griefs — direct: Matt 8:17; 1 Pet 2:24
- v. 7: silent lamb — direct: Acts 8:32-35; John 1:29
- v. 9: grave with wicked/rich — direct: Matt 27:38,57-60; 1 Pet 2:22
- v. 10: will of YHWH to crush — direct: Acts 4:28; resurrection ('he shall prolong his days')
- v. 12: numbered with transgressors, intercession — direct: Luke 22:37; Heb 7:25
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
    # INTENT: Non-destructive merge — existing entries are never overwritten, safe to re-run
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]: existing[ch][v] = html

ISAIAH = {
"53": {
"1": "<p>A direct prophecy. <em>Mî hě'emîn lišmû'ātēnû ûzĕrôa' YHWH 'al-mî niglātāh</em> — who has believed what he has heard from us? And to whom has the arm of YHWH been revealed? John 12:38 cites this verse as fulfilled in the aftermath of Jesus' signs: <em>so that the word spoken by the prophet Isaiah might be fulfilled: 'Lord, who has believed what he heard from us?'</em> Romans 10:16 cites it again: <em>they have not all obeyed the gospel, for Isaiah says, 'Lord, who has believed what he has heard from us?'</em> The Servant's reception begins with the question of belief — establishing that the scandal of the Messiah is the stumbling block the gospel announces.</p>",
"2": "<p>A direct prophecy. <em>No form or majesty that we should look at him, and no beauty that we should desire him</em> — the Servant is not recognizable as a king, having no regal appearance. The hiddenness of the Messiah's glory is the Incarnation's signature: John 1:10-11 (the world did not know him; his own people did not receive him); Luke 2:7 (born in a stable, no room at the inn). The root from dry ground (<em>kĕšōreš mē'ereṣ ṣiyyāh</em>) is the emergence of new life from what appeared dead — the Davidic dynasty cut to a stump (Isa 11:1), from which the Servant-shoot emerges against all expectation.</p>",
"3": "<p>A direct prophecy. <em>Nib̠zeh waḥădal 'îšîm 'îš maḵ'ōb̠ôt</em> — despised and rejected by men, a man of sorrows (<em>maḵ'ōb̠ôt</em> — literally pains, griefs) and acquainted with grief. The passion narrative is the direct fulfillment: Luke 23:11 (Herod with his soldiers treated him with contempt and mocked him); John 1:11 (he came to his own, and his own people did not receive him); Mark 9:12 (how is it written of the Son of Man that he should suffer many things and be treated with contempt?). <em>As one from whom men hide their faces</em> — the disciples' flight (Matt 26:56) and Peter's denial (Matt 26:69-75) enact the hiding of faces from the suffering Servant.</p>",
"4": "<p>A direct prophecy. <em>'ākēn ḥolāyēnû hû' nāśā' ûmaḵ'ōb̠ênû sĕb̠ālām</em> — surely he has borne (<em>nāśā'</em>) our griefs and carried our sorrows. Matthew 8:17 quotes this as fulfilled in Jesus' healing ministry: <em>he took our illnesses and bore our diseases</em> — applying the Servant's bearing not only to the cross but to the entire ministry of healing. 1 Peter 2:24 applies it to the atonement: <em>he himself bore our sins in his body on the tree, that we might die to sin and live to righteousness</em>. The verb <em>nāśā'</em> (to bear, to carry) is the sacrificial term for taking on what belongs to another — the same verb that describes the scapegoat carrying the people's sins (Lev 16:22).</p>",
"5": "<p>A direct prophecy. <em>Wĕhû' mĕḥōlāl mippĕšā'ênû mĕdukka' mē'ăwōnōtênû</em> — he was pierced (<em>mĕḥōlāl</em>) for our transgressions; he was crushed for our iniquities. The substitutionary logic — pierced <em>for</em> our transgressions — is the center of the atonement: Romans 4:25 (delivered up for our trespasses); 2 Corinthians 5:21 (he made him who knew no sin to be sin for us); Galatians 3:13 (Christ redeemed us from the curse of the law by becoming a curse for us). John 19:34,37 applies the piercing directly (they pierced his side; they shall look on him whom they have pierced). The chastisement (<em>mûsar</em>) that brought us peace and the wounds by which we are healed are the NT's theology of the cross in 20 Hebrew words.</p>",
"6": "<p>A direct prophecy. <em>Kullānû kĕṣō'n tā'înû 'îš lĕdarkô pānînû waYHWH hip̄gîa' b̠ô 'ēt 'ăwōn kullānû</em> — all we like sheep have gone astray; we have turned every one to his own way; and YHWH has caused the iniquity of us all to fall on him. The total scope of sin (<em>kullānû... kullānû</em> — all of us... all of us) and the total scope of the bearing: every individual's sin laid on the Servant. 1 Peter 2:25 cites this directly: <em>you were straying like sheep, but have now returned to the Shepherd and Overseer of your souls</em>. John 10:11-15 (the Good Shepherd lays down his life for the sheep, knowing his sheep and known by them) is the narrative form of Isaiah 53:6 — the Shepherd who becomes the sacrificial lamb for the straying sheep.</p>",
"7": "<p>A direct prophecy. <em>Niggaś wĕhû' na'ăneh wĕlō' yip̄taḥ-pîw kĕśeh labbataḥ yûb̠al</em> — he was oppressed and he was afflicted, yet he opened not his mouth; like a lamb led to slaughter, like a sheep silent before its shearers. Acts 8:32-35 records Philip using this exact verse to explain the gospel to the Ethiopian eunuch — the most explicit OT-to-gospel connection in Acts. The silent lamb is Jesus before the high priest (Matt 26:63: Jesus remained silent) and before Pilate (Matt 27:14: he gave him no answer, not even to a single charge). John 1:29 (behold the Lamb of God who takes away the sin of the world) and 1 Peter 1:19 (the precious blood of Christ like that of a lamb without blemish or spot) are the theological appropriation of the silent lamb of Isaiah 53:7.</p>",
"8": "<p>A direct prophecy. <em>Mē'ōṣer ûmimmiśpāṭ luqqāḥ ûb̠ĕdôrô mî yĕśôḥēaḥ kî niggĕzar mē'ereṣ ḥayyîm mippešā' 'ammî nĕga' lāmô</em> — by oppression and judgment he was taken away; who considered that he was cut off out of the land of the living, stricken for the transgression of my people? The legal process culminating in death (<em>oppression and judgment... taken away</em>) is the trial and crucifixion: Pontius Pilate's judgment, the unjust verdict, the execution. <em>Cut off out of the land of the living</em> is death. Romans 4:25 (he was delivered up for our trespasses) and Acts 3:13-15 (you denied the Holy and Righteous One... and killed the Author of life, whom God raised) apply this verse to the cross and the resurrection that reverses it.</p>",
"9": "<p>A direct prophecy. <em>Wayyittēn 'et-rĕšā'îm qib̠rô wĕ'et-'āšîr b̠ĕmōtāyw</em> — they made his grave with the wicked and with a rich man in his death. The double burial detail — among the wicked (crucified between two criminals, Luke 23:32-33) and with a rich man (Joseph of Arimathea's tomb, Matt 27:57-60) — is fulfilled with precision. <em>Although he had done no violence, and there was no deceit in his mouth</em> — 1 Peter 2:22 quotes this of Christ directly: <em>he committed no sin, neither was deceit found in his mouth</em>. The innocence of the Servant established by the prophet becomes the foundation of his substitutionary efficacy: the innocent dies for the guilty.</p>",
"10": "<p>A direct prophecy. <em>waYHWH ḥāp̄ēṣ dakke'ô heḥĕlî 'im-tāśîm 'āšām nap̄šô yir'eh zera' ya'ărîk̠ yāmîm</em> — yet it was the will (<em>ḥāp̄ēṣ</em>) of YHWH to crush him; he has put him to grief. When his soul makes a guilt offering (<em>'āšām</em>), he shall see his offspring; he shall prolong his days. Acts 4:28 (what your hand and your plan had predestined to take place — the crucifixion — is the fulfillment of YHWH's sovereign will). The <em>'āšām</em> (guilt/reparation offering, Lev 5-6) applied to the Servant is the atoning sacrifice that satisfies divine justice. <em>He shall prolong his days</em> after making the offering for guilt is the resurrection: the one who was cut off (v. 8) lives again, seeing his offspring — the community of faith — as the fruit of his death. Hebrews 9:14 (Christ offered himself without blemish to God) and John 12:24 (the grain of wheat that falls and dies bears much fruit) apply both the sacrifice and the offspring-seeing.</p>",
"11": "<p>A direct prophecy. <em>mê'ămal nap̄šô yir'eh yiśbā' bĕda'tô yaṣdîq ṣaddîq 'ab̠dî lārabbîm wă'ăwōnōtām hû' yisb̄ōl</em> — out of the anguish of his soul he shall see and be satisfied; by his knowledge shall the righteous one, my servant, make many to be accounted righteous, and he shall bear their iniquities. The forensic justification (<em>yaṣdîq</em> — to declare/make righteous) of the many through the Servant is the OT ground of Paul's doctrine of justification: Romans 5:19 (by the one man's obedience the many will be made righteous); 2 Corinthians 5:21 (so that in him we might become the righteousness of God). The Servant's satisfaction (<em>yiśbā'</em>) after anguish is the resurrection-joy: John 17:4 (I glorified you on earth, having accomplished the work you gave me to do); Hebrews 12:2 (who for the joy set before him endured the cross).</p>",
"12": "<p>A direct prophecy. <em>lākēn 'ăḥalleq-lô b̠ārabbîm wĕ'et-'ăṣûmîm yĕḥallēq šālāl taḥat 'ăšer hě'ĕrāh lammāwet nap̄šô wĕ'et-pōšĕ'îm nimnāh wĕhû' ḥēṭ'-rabbîm nāśā' wĕlappōšĕ'îm yap̄gîa'</em> — therefore I will divide him a portion with the many... because he poured out his soul to death and was numbered with the transgressors; yet he bore the sin of many, and makes intercession for the transgressors. Jesus cites this verse at the Last Supper: Luke 22:37 (<em>for I tell you that this scripture must be fulfilled in me: 'and he was numbered with the transgressors'</em>) — identifying himself as the Servant before the arrest that makes it literal (crucified between criminals, Luke 23:32-33). <em>He makes intercession for the transgressors</em> is Hebrews 7:25 (<em>he always lives to make intercession for them</em>) and Luke 23:34 (<em>Father, forgive them, for they know not what they do</em>). The dividing of spoil (<em>yĕḥallēq šālāl</em>) with the strong is the resurrection triumph's fruits distributed to those who are his (Eph 4:8: when he ascended he gave gifts to his church).</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 53 mkt-christ: {v} verses in script (merge skips existing 2).')

if __name__ == '__main__':
    main()
