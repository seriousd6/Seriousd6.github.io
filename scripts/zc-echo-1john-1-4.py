"""
Echo layer — 1 John chapters 1–4
Output: data/echoes/1john.json

1 John is densely allusive to John's Gospel and Genesis 1, to Leviticus/Deuteronomy
covenant-love language, to Psalms on righteousness, and to Isaiah on light.
The Johannine proprium: abiding (meno), love-command, light/darkness, born of God.
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

ECHOES = {
  "1": {
    "1": [
      {"type": "allusion", "target": "John 1:1", "note": "In the beginning was the Word — same opening formula (ap arches) grounding the incarnation in eternal pre-existence"},
      {"type": "allusion", "target": "Gen 1:1", "note": "The beginning (arche) echoes Genesis 1:1 — creation and new-creation share the same starting point"},
      {"type": "allusion", "target": "John 19:35", "note": "What we have seen and touched — eyewitness language mirrors the Beloved Disciple's testimony"}
    ],
    "2": [
      {"type": "fulfillment", "target": "Isa 9:2", "note": "The life was revealed — the manifestation of eternal life fulfills the Isaianic promise of great light appearing to those in darkness"},
      {"type": "allusion", "target": "John 1:14", "note": "The word became flesh and dwelt among us — parallel revelation-language for the incarnation"}
    ],
    "5": [
      {"type": "theme", "target": "Gen 1:3-4", "note": "God is light — creation's first act (light from darkness) reveals the character of the Creator; John applies this ontologically to God"},
      {"type": "allusion", "target": "Ps 27:1", "note": "The LORD is my light — Psalmic identification of God as light source, here universalized as God's very nature"},
      {"type": "allusion", "target": "John 8:12", "note": "I am the light of the world — the theological claim about God here grounds Jesus's self-identification there"}
    ],
    "7": [
      {"type": "fulfillment", "target": "Lev 17:11", "note": "The blood of Jesus his Son cleanses us from all sin — the Levitical principle (blood makes atonement for the soul) fulfilled in the definitive sacrifice"},
      {"type": "shadow", "target": "Zech 13:1", "note": "A fountain opened for the house of David for sin and uncleanness — the promised cleansing fountain now identified as Christ's blood"}
    ],
    "9": [
      {"type": "theme", "target": "Ps 32:5", "note": "If we confess our sins he is faithful and just to forgive — the Psalmic pattern of confession leading to divine forgiveness"},
      {"type": "allusion", "target": "Ps 51:1-2", "note": "Cleanse me from my sin — the penitential tradition of direct divine cleansing underpins the promise here"},
      {"type": "allusion", "target": "Mic 7:18", "note": "Who is a God like you, who pardons sin and forgives transgression? — Micah's doxology over divine forgiveness is the OT warrant John draws on when he calls God 'faithful and just to forgive'; the same covenant God who pardoned Israel now purifies through Christ's atoning work."}
    ]
  },
  "2": {
    "1": [
      {"type": "fulfillment", "target": "Isa 53:12", "note": "Jesus Christ the righteous as our advocate (parakletos) — intercession for transgressors fulfilled in the heavenly high-priestly advocacy of Christ"},
      {"type": "allusion", "target": "Job 16:19-21", "note": "My witness is in heaven, my advocate on high — the plea for a heavenly advocate realized in Christ"}
    ],
    "2": [
      {"type": "fulfillment", "target": "Lev 16:15-16", "note": "He is the propitiation (hilasmos) for our sins — the Day of Atonement propitiation for the whole community fulfilled in Christ's self-offering"},
      {"type": "type", "target": "Lev 16:30", "note": "Atonement shall be made for you to cleanse you — the annual type fulfilled once-for-all in Christ's atoning work"}
    ],
    "5": [
      {"type": "allusion", "target": "Deut 6:5", "note": "Keeping his word, in him love is truly perfected — the Shema love-command (love God with all) is the covenant basis for the love-commandment here"},
      {"type": "allusion", "target": "John 14:23", "note": "If anyone loves me he will keep my word — the love-obedience link is identical to John's Gospel"}
    ],
    "7": [
      {"type": "allusion", "target": "Lev 19:18", "note": "The old commandment you had from the beginning — the love-neighbor command of Leviticus is the ancient basis of the commandment John calls old"},
      {"type": "allusion", "target": "Deut 6:5", "note": "The old commandment = love command from Sinai, received in the beginning of Israel's covenant life"}
    ],
    "8": [
      {"type": "fulfillment", "target": "John 1:5", "note": "The darkness is passing away and the true light is already shining — the new commandment is new because Christ inaugurated the new-creation dawn"},
      {"type": "allusion", "target": "Isa 60:1-3", "note": "Arise, shine, for your light has come — the eschatological light-dawning over Zion is being realized in the community's ethical transformation"}
    ],
    "12": [
      {"type": "allusion", "target": "Ps 25:11", "note": "Sins are forgiven for his name's sake — Psalmic forgiveness on account of the divine name, echoed in the community's assured forgiveness"}
    ],
    "13": [
      {"type": "allusion", "target": "Gen 1:1", "note": "The description 'him who is from the beginning' applied to the Father (and by implication to the pre-existent Son) echoes Genesis 1:1's ἐν ἀρχῇ; knowing the one who precedes creation is the mark of mature faith in the Johannine framework."}
    ],
    "14": [
      {"type": "allusion", "target": "Ps 119:11", "note": "The word of God abides in you — the Psalmist hides God's word in his heart; here abiding of the word is the mark of spiritual maturity"},
      {"type": "theme", "target": "Deut 11:18", "note": "Lay up these words in your heart — covenant instruction abiding in the community as the basis for obedient strength"}
    ],
    "15": [
      {"type": "theme", "target": "Deut 13:4", "note": "Do not love the world — the covenant call to exclusive allegiance to YHWH (not following other gods) is now reframed as not loving the world-system"},
      {"type": "allusion", "target": "Jas 4:4", "note": "Friendship with the world is enmity with God — parallel letter-tradition applying the same exclusive loyalty principle"}
    ],
    "17": [
      {"type": "allusion", "target": "Isa 51:6", "note": "The world is passing away — the heavens vanishing like smoke; the eschatological passing of the present order"},
      {"type": "fulfillment", "target": "Dan 7:14", "note": "Whoever does the will of God abides forever — the everlasting dominion given to the Son of Man is shared by those united to him"}
    ],
    "18": [
      {"type": "allusion", "target": "Dan 7:25", "note": "It is the last hour — Danielic end-time urgency; the final period before the Son of Man's vindication"},
      {"type": "theme", "target": "2 Thess 2:3-4", "note": "Antichrist coming — Paul's man of lawlessness tradition parallel to John's antichrist warning"}
    ],
    "22": [
      {"type": "allusion", "target": "Ps 2:2", "note": "Denying that Jesus is the Christ inverts Psalm 2's proclamation of YHWH's anointed king; the antichrist figure stands in the position of the psalm's conspiring nations who set themselves against the Lord and his anointed."}
    ],
    "25": [
      {"type": "allusion", "target": "Isa 25:8", "note": "The promised eternal life (ζωὴ αἰώνιος) echoes Isaiah's eschatological banquet where death is swallowed up forever; John presents the promise as already given by the one who is from the beginning, anchoring eschatological life in covenant faithfulness."}
    ],
    "20": [
      {"type": "fulfillment", "target": "Joel 2:28-29", "note": "You have been anointed by the Holy One — the Spirit-anointing of the community fulfills Joel's promise that all God's people would receive the Spirit"},
      {"type": "allusion", "target": "Isa 11:2", "note": "The Spirit of the LORD resting on the anointed — messianic anointing now shared with the whole community"}
    ],
    "23": [
      {"type": "allusion", "target": "John 5:23", "note": "Whoever denies the Son does not have the Father — identical theological claim: honor of the Son and honor of the Father are inseparable"},
      {"type": "allusion", "target": "John 14:6", "note": "No one comes to the Father except through me — the Son as exclusive mediatorial access to the Father"}
    ],
    "27": [
      {"type": "fulfillment", "target": "Jer 31:33-34", "note": "The anointing teaches you about everything — the new covenant promise that all will know the LORD without external teaching, fulfilled in Spirit-anointing"},
      {"type": "allusion", "target": "Isa 54:13", "note": "All your children shall be taught by the LORD — the promise of divine teaching given to the whole covenant community"}
    ]
  },
  "3": {
    "1": [
      {"type": "fulfillment", "target": "Hos 1:10", "note": "Called children of God — the sons of the living God; the adoption-promise to Israel universalized to all who receive Christ"},
      {"type": "allusion", "target": "John 1:12", "note": "To all who received him he gave the right to become children of God — the foundational Johannine claim repeated"}
    ],
    "2": [
      {"type": "allusion", "target": "Ps 17:15", "note": "We shall see him as he is — I shall behold your face in righteousness; the Psalmic hope of beatific vision realized in the eschatological transformation"},
      {"type": "theme", "target": "Job 19:26-27", "note": "In my flesh I shall see God — Job's vision-hope extended to the full transformation at Christ's appearing"}
    ],
    "3": [
      {"type": "allusion", "target": "Lev 11:44", "note": "All who have this hope in him purify themselves, as he is pure — the Levitical holiness command ('be holy, for I am holy') is the OT ancestor of John's purity-hope logic; the difference is that the standard is now the Son's own purity, not ritual prescription."}
    ],
    "4": [
      {"type": "theme", "target": "Deut 17:11-12", "note": "Sin is lawlessness (anomia) — transgressing divinely given Torah is the OT definition of the sin-as-lawlessness John adopts"}
    ],
    "5": [
      {"type": "fulfillment", "target": "Isa 53:9", "note": "Isaiah's declaration that the Servant 'had done no violence, nor was any deceit in his mouth' is fulfilled in 'in him is no sin'; the Servant's perfect sinlessness that qualified him to bear others' guilt is exactly what John asserts — and it is the basis for Christ's sin-taking ability."}
    ],
    "8": [
      {"type": "fulfillment", "target": "Gen 3:15", "note": "The devil has been sinning from the beginning — Satan is the ancient enemy of Gen 3; the Son of God appeared to destroy his works, fulfilling the protoevangelium"},
      {"type": "allusion", "target": "John 12:31", "note": "Now is the ruler of this world cast out — the defeat of the devil in the cross-event is what 1 John applies to the community"}
    ],
    "9": [
      {"type": "allusion", "target": "Jer 31:33", "note": "The new-covenant promise that God will write his law on their hearts — internal transformation, not external compliance — underlies John's claim that 'God's seed remains' in the born-of-God person; the σπέρμα is the indwelling divine life the new covenant inaugurated."},
      {"type": "allusion", "target": "Ezek 36:27", "note": "Ezekiel's promise 'I will put my Spirit in you and move you to follow my decrees' is the OT ground for the moral impossibility John describes: the Spirit's permanent indwelling constitutes the inability to persist in the pattern of sin."}
    ],
    "12": [
      {"type": "allusion", "target": "Gen 4:8", "note": "Cain murdered his brother — the first murder as the paradigmatic act of the one who is from the evil one; John's instruction not to be like Cain frames community hatred as a re-enactment of this inaugural crime."}
    ],
    "15": [
      {"type": "allusion", "target": "Gen 9:6", "note": "The severity of designating every brother-hater a murderer draws on the Noahic image-of-God principle — human life bears the divine image and murder is the ultimate violation of it; John extends the logic of that commandment to its interior dimension, as Christ had done in Matthew 5."}
    ],
    "14": [
      {"type": "allusion", "target": "John 5:24", "note": "We have passed from death to life — the Johannine life-passage that occurs in hearing and believing, here applied to the love-test"},
      {"type": "allusion", "target": "Deut 30:15-19", "note": "I set before you life and death — the covenant choice-framework: love is the path of life, hatred is the path of death"}
    ],
    "16": [
      {"type": "fulfillment", "target": "John 15:13", "note": "By this we know love, that he laid down his life for us — Christ's self-giving as the definition of love; community love is the derivative"}
    ],
    "17": [
      {"type": "allusion", "target": "Deut 15:7-11", "note": "Closes his heart against his brother in need — the year of release law: not hardening the heart against the poor is covenant obligation"},
      {"type": "allusion", "target": "Prov 19:17", "note": "Whoever is generous to the poor lends to the LORD — the wisdom tradition on material generosity as love-in-action"}
    ]
  },
  "4": {
    "1": [
      {"type": "allusion", "target": "Deut 13:1-3", "note": "Test the spirits — Deuteronomy warned that even signs-performing prophets must be tested; the criterion is doctrinal fidelity to YHWH"},
      {"type": "allusion", "target": "1 Thess 5:21", "note": "Test everything, hold fast what is good — parallel apostolic instruction to the community on discerning prophecy"}
    ],
    "2": [
      {"type": "allusion", "target": "John 1:14", "note": "Jesus Christ has come in the flesh — the incarnation-confession mirrors the Word-became-flesh proclamation; denial = Docetism"},
      {"type": "allusion", "target": "2 John 7", "note": "Those who do not confess Jesus coming in the flesh — Johannine epistolary tradition's consistent anti-Docetic criterion"}
    ],
    "6": [
      {"type": "allusion", "target": "Isa 59:14", "note": "The 'spirit of falsehood' that refuses to hear God's messengers echoes Isaiah's diagnosis of a society where truth has stumbled and faithfulness cannot enter; John identifies within the community the same polarity between those oriented toward God and those toward the world-system."}
    ],
    "7": [
      {"type": "theme", "target": "Deut 6:5", "note": "Let us love one another, for love is from God — the Shema love-command; love as divine property now shared with the born-of-God community"},
      {"type": "allusion", "target": "Gen 1:26-27", "note": "Made in the image of God — the theological basis for love: God is love, humans are image-bearers, therefore human love participates in divine love"}
    ],
    "8": [
      {"type": "theme", "target": "Exod 34:6-7", "note": "God is love — the great divine self-disclosure at Sinai (abounding in steadfast love) is here distilled to its essential claim about God's character"}
    ],
    "9": [
      {"type": "fulfillment", "target": "John 3:16", "note": "God sent his only Son into the world that we might live through him — almost verbatim, grounding the love-claim in the Son-sending event"},
      {"type": "allusion", "target": "Gen 22:2", "note": "Only Son — the binding of Isaac uses the same term (yahid = only/beloved); the Aqedah as the shadow of the Father's gift of the Son"}
    ],
    "10": [
      {"type": "fulfillment", "target": "Lev 16:16", "note": "He sent his Son to be the propitiation for our sins — the Day of Atonement propitiation (kapporeth) fulfilled in Christ's atoning self-offering"},
      {"type": "type", "target": "Num 21:8-9", "note": "The bronze serpent lifted up for those who look to it — Johannine type (John 3:14-15) for the Son sent to be looked to for life/atonement"}
    ],
    "12": [
      {"type": "allusion", "target": "John 1:18", "note": "No one has ever seen God — identical claim; the unseen God is revealed through the Son and through the community that abides in love"},
      {"type": "allusion", "target": "Exod 33:20", "note": "You cannot see my face, for man shall not see me and live — the divine hiddenness that makes the incarnation the only adequate revelation"}
    ],
    "14": [
      {"type": "fulfillment", "target": "John 4:42", "note": "The Father has sent his Son to be the Savior of the world — the Samaritan confession; the universal scope of the Son-sending"},
      {"type": "allusion", "target": "Isa 43:11", "note": "I am the LORD, and besides me there is no savior — YHWH as sole savior; Jesus as the Savior of the world is the NT fulfillment of this exclusive claim"}
    ],
    "16": [
      {"type": "theme", "target": "Exod 34:6", "note": "God is love and whoever abides in love abides in God — the divine name-proclamation (steadfast love as defining character) grounds the mutual-abiding theology"},
      {"type": "allusion", "target": "John 15:4-7", "note": "Abide in me — the vine-and-branches abiding language is the Fourth Gospel's equivalent of this mutual indwelling"}
    ],
    "18": [
      {"type": "allusion", "target": "Ps 27:1", "note": "Perfect love casts out fear — the Psalmist who fears nothing because YHWH is his light; the love-perfect community participates in this freedom from dread"}
    ],
    "19": [
      {"type": "fulfillment", "target": "Deut 7:8", "note": "We love because he first loved us — YHWH loved Israel first and redeemed them before they loved; the prevenient love of God is the basis of responsive love"}
    ],
    "20": [
      {"type": "allusion", "target": "Matt 5:44-45", "note": "Cannot love God whom he has not seen if he hates his brother — the visible neighbor as the test of love for the invisible God parallels the Sermon on the Mount ethic"}
    ]
  }
}

def main():
    existing = load_echo('1john')
    merge_echo(existing, ECHOES)
    save_echo('1john', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 John echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
