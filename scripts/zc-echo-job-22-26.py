"""
Echo Layer — Job chapters 22–26
Run: python3 scripts/zc-echo-job-22-26.py

Key echo connections in this range:
- 22:6-9: Eliphaz's false charges of social sin → Matt 25:42-43 (hungry/naked/widow)
- 22:21: "make peace with him now and be reconciled" → 2 Cor 5:20 (be reconciled to God)
- 22:27: "pray to him and he will answer" → John 15:7; Jas 5:16
- 23:3: "if only I could reach the place where he dwells" → John 14:3; Heb 4:16
- 23:10: "when he has tried me, I will come out as gold" → 1 Pet 1:7; Jas 1:3
- 23:12: words of his mouth valued more than bread → Matt 4:4 (Deut 8:3)
- 24:13: "those who rebel against the light" → John 3:19-20
- 25:4: "how can any mortal be declared righteous before God?" → Rom 3:20; Gal 4:4
- 25:6: "a human being, who is a worm" → Ps 22:6; Phil 2:7 (Christ took lowest form)
- 26:6: Sheol and Abaddon bare before God → Rev 1:18; Rev 9:11
- 26:7: "hangs the earth on nothing" → Heb 1:3 (upholding all things by his word)
- 26:12: "crushed the sea dragon" → Rev 12:9; Col 2:15
- 26:14: "edges of his ways... how faint a whisper" → 1 Cor 13:12; Rom 11:33
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

JOB_ECHO_22_26 = {
  "22": {
    "6": [
      {"type": "allusion", "target": "Matt 25:42", "note": "Eliphaz levels a series of social-sin accusations against Job: seizing collateral unjustly, withholding water from the weary traveler, withholding bread from the starving, exploiting the powerful&#8217;s land-grab, turning widows away empty-handed, breaking the orphan&#8217;s strength (vv.6-9) — none of which Job has actually done, as the reader knows from chapters 1-2 and Job&#8217;s own testimony in chapter 31; the list of sins Eliphaz invents maps exactly onto the corporal works of mercy that Jesus commends in Matthew 25:42-43: &#8220;I was hungry and you gave me no food... thirsty and you gave me nothing to drink... naked and you did not clothe me&#8221;; Eliphaz&#8217;s false charges describe the sins of omission that Matthew 25 condemns — which makes Job a type of the one who was unjustly accused of violating covenant obligations he had in fact fulfilled"}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 57:15", "note": "&#8220;Is not God in the heights of heaven? See how high the stars tower above you.&#8221; — Eliphaz invokes divine transcendence as evidence of Job&#8217;s culpability; Isaiah 57:15 holds the same truth in tension with its opposite: &#8220;For this is what the high and exalted One says — he who lives forever, whose name is holy: &#8216;I live in a high and holy place, but also with the one who is contrite and lowly in spirit&#8217;&#8221;; divine height does not entail divine distance from the lowly; the incarnation is the definitive answer to Eliphaz&#8217;s implicit deism — the transcendent God descends precisely to the sufferer Eliphaz dismisses"}
    ],
    "21": [
      {"type": "allusion", "target": "2 Cor 5:20", "note": "&#8220;Make peace with him now and be reconciled; in that way good will find you.&#8221; — Eliphaz&#8217;s counsel to Job is theologically correct even though his diagnosis of Job&#8217;s condition is wrong; the NT articulation of the same call comes from Paul in 2 Corinthians 5:20: &#8220;We implore you on behalf of Christ, be reconciled to God&#8221;; the difference is that Eliphaz grounds reconciliation in Job&#8217;s moral reform (&#8220;banish iniquity from your household&#8221;, v.23), while Paul grounds it in the atonement of Christ — &#8220;God made him who had no sin to be sin for us, so that in him we might become the righteousness of God&#8221; (5:21)"}
    ],
    "26": [
      {"type": "allusion", "target": "Ps 37:4", "note": "&#8220;Then you will take your delight in the Almighty, and lift your face toward God.&#8221; — Eliphaz&#8217;s promise of restored delight in God echoes Psalm 37:4: &#8220;take delight in the LORD, and he will give you the desires of your heart&#8221;; both texts present <em>ʿōneg</em> (delight/pleasure in God) as the experiential outcome of right relationship; the NT grounds this delight not in moral achievement but in union with Christ — &#8220;rejoice in the Lord always&#8221; (Phil 4:4) is the NT form of the same call, now available through the reconciliation Eliphaz only hints at"}
    ],
    "27": [
      {"type": "allusion", "target": "John 15:7", "note": "&#8220;You will pray to him and he will answer; you will fulfill what you have vowed.&#8221; — Eliphaz&#8217;s conditional promise (if you return, your prayers will be answered) is given by Jesus as an unconditional gift to those abiding in him: &#8220;If you abide in me, and my words abide in you, ask whatever you wish, and it will be done for you&#8221; (John 15:7); the condition that Eliphaz imposes — moral reform — Christ replaces with union — &#8220;abide in me&#8221;; the prayer-answer relationship Eliphaz holds out as a goal is what Jesus gives as a present reality to those in him"}
    ]
  },
  "23": {
    "3": [
      {"type": "allusion", "target": "John 14:3", "note": "&#8220;If only I knew where to find him — if only I could reach the place where he dwells!&#8221; — Job&#8217;s longing to locate God and present his case is the OT form of the universal human desire for access to the divine presence; Jesus answers Job&#8217;s &#8220;if only&#8221; with a declaration: &#8220;I will come again and will take you to myself, that where I am you may be also&#8221; (John 14:3); and moments later: &#8220;I am the way, and the truth, and the life. No one comes to the Father except through me&#8221; (John 14:6) — the &#8220;place where God dwells&#8221; that Job cannot find is opened by the one who is himself the way"},
      {"type": "allusion", "target": "Heb 4:16", "note": "&#8220;If only I could reach the place where he dwells!&#8221; — the inaccessibility of God that Job laments is the same barrier that Hebrews 4:16 declares removed: &#8220;let us then with confidence draw near to the throne of grace, that we may receive mercy and find grace to help in time of need&#8221;; the confidence to approach God that Job desperately desires but cannot achieve is exactly the gift that Christ&#8217;s high priesthood provides — the barrier is down; the way is open"}
    ],
    "10": [
      {"type": "allusion", "target": "1 Pet 1:7", "note": "&#8220;But he knows the path I walk; when he has tried me, I will come out as gold.&#8221; — Job&#8217;s confidence that divine testing will ultimately refine rather than destroy him is the OT source of 1 Peter 1:7: &#8220;these have come so that the proven genuineness of your faith — of greater worth than gold, which perishes even though refined by fire — may result in praise, glory and honor when Jesus Christ is revealed&#8221;; both texts use the metallurgical image of gold-refining for suffering that tests and purifies; Job&#8217;s hope that his tested faith will emerge as gold becomes the NT&#8217;s framework for interpreting Christian suffering"}
    ],
    "12": [
      {"type": "allusion", "target": "Matt 4:4", "note": "&#8220;I have valued the words of his mouth more than my daily bread (<em>miḥuqqî</em>).&#8221; — Job&#8217;s declaration that divine speech exceeds bread in value is the OT precedent for Jesus&#8217; response to the devil in Matthew 4:4, quoting Deuteronomy 8:3: &#8220;man shall not live by bread alone, but by every word that comes from the mouth of God&#8221;; both texts assert the same priority: the nourishment provided by God&#8217;s word surpasses the nourishment of physical food; Job voices this conviction from within his suffering — without food, without health, he still values divine speech above the bodily sustenance he has lost"}
    ],
    "13": [
      {"type": "allusion", "target": "Heb 6:17", "note": "&#8220;But he is resolute in his purpose (<em>bᵉʾeḥāḏ ûmî yᵉšîḇennû</em>), and who can change him? What he wills, that he carries out.&#8221; — Job&#8217;s acknowledgment of divine immutability of purpose, though voiced in dread, articulates what Hebrews 6:17 celebrates: &#8220;God, desiring even more to show to the heirs of the promise the unchangeable nature of his purpose, intervened with an oath&#8221;; the same divine resoluteness that fills Job with dread (v.15) is the ground of the Christian&#8217;s hope — the immutable God who cannot change his purpose has bound himself by oath to the heirs of salvation"}
    ]
  },
  "24": {
    "7": [
      {"type": "allusion", "target": "Matt 25:36", "note": "&#8220;They spend the night naked, with no garment to cover them against the cold.&#8221; — Job&#8217;s survey of the exploited poor (chapter 24) catalogs the exact conditions that Jesus identifies with himself in the final judgment: &#8220;I was naked and you clothed me&#8221; (Matt 25:36); the naked poor who shelter against rocks (v.8), the hungry who carry others&#8217; harvest while starving (v.10), the fatherless snatched from their mothers (v.9) — Job&#8217;s theodicy complaint about God&#8217;s apparent indifference to this suffering is answered in Christ&#8217;s identification with &#8220;the least of these&#8221; (Matt 25:40)"}
    ],
    "12": [
      {"type": "allusion", "target": "Rev 6:10", "note": "&#8220;From the city the dying groan; the mortally wounded cry out — yet God lays no charge of wrongdoing.&#8221; — Job&#8217;s theodicy complaint that God seems silent in the face of urban suffering and violent death anticipates the cry of the martyrs under the altar in Revelation 6:10: &#8220;How long, O Lord, holy and true, until you judge the inhabitants of the earth and avenge our blood?&#8221;; both texts voice the same experience — the suffering righteous cry out and the divine judgment seems delayed; the answer given in Revelation (a little longer) and ultimately in Christ&#8217;s return is the answer to Job&#8217;s complaint"}
    ],
    "13": [
      {"type": "allusion", "target": "John 3:20", "note": "&#8220;These are among those who rebel against the light; they do not know its ways and will not walk its paths.&#8221; — Job&#8217;s description of the wicked as constitutive rebels against light is the OT form of John 3:19-20: &#8220;this is the judgment: the light has come into the world, and people loved the darkness rather than the light because their works were evil. For everyone who does wicked things hates the light and does not come to the light, lest his works should be exposed&#8221;; the moral aversion to light that Job describes as a behavioral pattern becomes, in the incarnation, the response to a person — the Light of the World who is rejected by those who prefer darkness"}
    ]
  },
  "25": {
    "4": [
      {"type": "allusion", "target": "Rom 3:20", "note": "&#8220;How can any mortal be declared righteous (<em>yiṣdaq</em>) before God? How can anyone born of a woman be clean?&#8221; — Bildad&#8217;s rhetorical question, the third and final speech of the Friends, states the conclusion all three have been driving toward: human beings are structurally incapable of meeting divine standards; Romans 3:20 is Paul&#8217;s NT statement of the identical principle: &#8220;no human being will be justified in his sight by works of the law&#8221;; both texts presuppose that the question they raise has no human answer — which is why the NT&#8217;s answer is the righteousness that comes through faith in Christ (Rom 3:21-22)"},
      {"type": "allusion", "target": "Gal 4:4", "note": "&#8220;How can anyone born of a woman be clean?&#8221; — Bildad&#8217;s question identifies the problem precisely: birth from a woman means participation in human impurity; Galatians 4:4 announces the startling solution: &#8220;God sent forth his Son, born of woman, born under the law, to redeem those who were under the law&#8221;; the incarnation does not bypass the condition Bildad describes — it enters it fully; Christ is born of woman (under the very condition that disqualifies), in order to provide the cleansing that birth from woman cannot generate"}
    ],
    "6": [
      {"type": "allusion", "target": "Ps 22:6", "note": "&#8220;How much less a mortal, who is a maggot, and a human being, who is a worm!&#8221; — Bildad&#8217;s climactic deprecation of humanity uses the worm (<em>tôlāʿāh</em>) image that Psalm 22:6 places on the lips of the righteous sufferer: &#8220;I am a worm and not a man, scorned by everyone, despised by the people&#8221;; the Psalm&#8217;s worm is Christ&#8217;s own self-identification in Gethsemane-and-cross — the Son of God taking the lowest human valuation upon himself; Bildad uses the worm to crush Job&#8217;s dignity; Psalm 22 uses it to identify the Messiah&#8217;s humiliation; Christ fulfills both by becoming the worm-man who rises as the firstborn from the dead"},
      {"type": "allusion", "target": "Phil 2:7", "note": "&#8220;A human being, who is a worm&#8221; — Bildad&#8217;s contemptuous diminishment of humanity is what Christ voluntarily enters; Philippians 2:7 describes the kenosis: &#8220;he made himself nothing by taking the very nature of a servant, being made in human likeness&#8221;; the one who is equal with God takes on the condition that Bildad describes as maximally contemptible — mortality, lowliness, dependence — not to confirm the contempt but to redeem the condition from within"}
    ]
  },
  "26": {
    "6": [
      {"type": "allusion", "target": "Rev 1:18", "note": "&#8220;Sheol is laid bare before him, and Abaddon has no covering.&#8221; — Job&#8217;s doxology asserts that even the realm of the dead is transparent to God — no darkness shields it; Revelation 1:18 presents the christological fulfilment: &#8220;I am the living one. I died, and behold I am alive forevermore, and I have the keys of Death and Hades.&#8221; The transparency of Sheol before God becomes, in the resurrection, the authority of Christ over Sheol — not merely that he can see it, but that he entered it and holds its keys"},
      {"type": "allusion", "target": "Rev 9:11", "note": "&#8220;Abaddon (<em>ʾᵃḇaddôn</em>) has no covering&#8221; — Job&#8217;s use of <em>ʾᵃḇaddôn</em> (destruction/the abyss) as a name for the underworld is the OT source of Revelation 9:11: &#8220;They have as king over them the angel of the bottomless pit. His name in Hebrew is Abaddon&#8221;; the realm that Job says is bare before God becomes in Revelation the domain of a defeated adversary whose king has been overthrown by the Lamb (Rev 5:5-6)"}
    ],
    "7": [
      {"type": "allusion", "target": "Heb 1:3", "note": "&#8220;He stretches out the north over the void and hangs the earth on nothing (<em>ʿal-bᵉlî-māh</em>).&#8221; — Job&#8217;s cosmological doxology — the earth suspended over emptiness by divine power alone — is the OT expression of what Hebrews 1:3 attributes to Christ: &#8220;upholding the universe by the word of his power&#8221;; the hanging of the earth on nothing that Job celebrates as a work of the Creator is the continuous act of the Son through whom &#8220;all things hold together&#8221; (Col 1:17); the doxology Job directs to YHWH is the doxology the NT directs to Christ"}
    ],
    "11": [
      {"type": "allusion", "target": "Heb 12:26", "note": "&#8220;The pillars of heaven tremble and are stunned at his rebuke.&#8221; — the trembling of cosmic structures before divine rebuke anticipates the eschatological shaking of Hebrews 12:26: &#8220;yet once more I will shake not only the earth but also the heavens&#8221; (citing Hag 2:6); both texts present the trembling of the created order as the appropriate response to divine majesty; in Hebrews, this cosmic shaking is connected to the &#8220;kingdom that cannot be shaken&#8221; — the unshakeable realm that the shaken heavens and earth reveal by contrast"}
    ],
    "12": [
      {"type": "allusion", "target": "Mark 4:39", "note": "&#8220;By his power he calmed the sea (<em>yārag hayyām</em>); by his understanding he crushed the sea dragon.&#8221; — Job&#8217;s doxology of God as the one who stills the chaotic sea is the OT basis for recognizing Christ&#8217;s authority when he rebukes the Sea of Galilee: &#8220;Peace! Be still!&#8221; (Mark 4:39); the calming that Job attributes to YHWH, Jesus enacts — implicitly claiming the same authority; the disciples&#8217; response (&#8220;Who then is this, that even the wind and the sea obey him?&#8221; Mark 4:41) is the question that Job&#8217;s doxology has already answered: it is YHWH"},
      {"type": "allusion", "target": "Col 2:15", "note": "&#8220;By his understanding he crushed the sea dragon (<em>tannîn</em>).&#8221; — the defeated sea-dragon of cosmogonic conflict appears in Job 26:12 as the one whom YHWH crushed at creation; Colossians 2:15 presents the definitive historical enactment of the same victory: &#8220;having disarmed the rulers and authorities, he put them to open shame, by triumphing over them in him [the cross]&#8221;; the crushing of the <em>tannîn</em> that Job celebrates as a cosmic deed is accomplished through the cross and resurrection — the dragon&#8217;s defeat is finalized in Christ&#8217;s triumph"}
    ],
    "13": [
      {"type": "allusion", "target": "Gen 1:2", "note": "&#8220;His Spirit made the heavens beautiful; his hand transfixed the twisting serpent (<em>nāḥāš bārîaḥ</em>).&#8221; — the Spirit&#8217;s beautifying of the heavens echoes Genesis 1:2 (&#8220;the Spirit of God was hovering over the waters&#8221;) — the same Spirit who ordered creation out of chaos; the <em>nāḥāš bārîaḥ</em> (fleeing/twisting serpent) transfixed by God&#8217;s hand appears in Isaiah 27:1 as the eschatological dragon slain by YHWH&#8217;s sword; Job&#8217;s cosmological poetry thus traces the arc from Spirit-over-waters (creation) to serpent-defeated (new creation)"}
    ],
    "14": [
      {"type": "allusion", "target": "1 Cor 13:12", "note": "&#8220;These things are but the edges of his ways; how faint a whisper we catch of him! The thunder of his full power — who can understand?&#8221; — Job concludes his doxology with an epistemological humility that Paul echoes in 1 Corinthians 13:12: &#8220;For now we see in a mirror dimly, but then face to face. Now I know in part; then I shall know fully, even as I have been fully known.&#8221; Job&#8217;s &#8220;faint whisper&#8221; of divine ways is what the present age offers; the full thunder of God&#8217;s power is the eschatological knowledge that awaits — and that the beatific vision will provide"},
      {"type": "allusion", "target": "Rom 11:33", "note": "&#8220;The thunder of his full power — who can understand?&#8221; — Job&#8217;s concluding doxological question is the same as Paul&#8217;s climactic exclamation in Romans 11:33: &#8220;Oh, the depth of the riches of the wisdom and knowledge of God! How unsearchable his judgments, and his ways beyond finding out!&#8221;; both texts arrive at the same posture — wonder before the incomprehensible — though Job arrives through suffering and protest while Paul arrives through theological reflection on the mystery of election; the same God is beyond both routes"}
    ]
  }
}

def main():
    existing = load_echo('job')
    merge_echo(existing, JOB_ECHO_22_26)
    save_echo('job', existing)
    print('Job 22-26 echo layer written.')

if __name__ == '__main__':
    main()
