"""
MKT 1 Peter chapters 1–2 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1peter-1-2.py

Translation decisions:
- G4151 (πνεῦμα): "Spirit" capitalised throughout chs 1–2 — all occurrences clearly reference the
  Holy Spirit (1:2 sanctification of the Spirit; 1:11 Spirit of Christ in the prophets; 1:12 Holy Spirit
  sent from heaven; 1:22 obedience through the Spirit). No lowercase ambiguity in this range.
- G4561 (σάρξ): "flesh" in 1:24 (direct quotation of Isa 40:6 — "all flesh is as grass"); "fleshly"
  as adjective in 2:11 (fleshly lusts). Not rendered "sinful nature" — the Isaiah quote is about
  creatureliness, not moral failure.
- G4102 (πίστις): "faith" throughout — the recipients' trusting reliance, not Christ's own faithfulness.
  1 Peter uses πίστις in the sense of the believers' response (1:5, 1:7, 1:9) and their testing.
- G1343 (δικαιοσύνη): "righteousness" in 2:24 (live to righteousness); "justly" / "righteously" in 2:23
  (the one who judges righteously/justly — dikaíōs, adverb form). Consistent with Romans convention.
- G26 (ἀγάπη): "love" — willed, covenantal, wholehearted love in 1:22 (love one another earnestly);
  contrasted implicitly with G5360 (φιλαδελφία = brotherly love / love of brothers) in the same verse.
- G3056 (λόγος): "word" in 1:23 (born again through the word of God); G4487 (ῥῆμα) = "word" in 1:25
  (the word of the Lord endures — quoting Isa 40:8). Both rendered "word" but contextually distinct;
  T tier notes the ῥῆμα in 1:25 as the spoken/proclaimed word.
- G2962 (κύριος): "Lord" throughout — consistent with all prior NT scripts.
- G3927 (πάρεπιδήμοις) / G3941 (παροίκους): L renders "sojourners" / "strangers"; M renders
  "exiles" / "foreigners"; T surfaces the diaspora identity fully ("dispersed exiles", "foreign nationals").
- G1588 (ἐκλεκτοῖς / ἐκλεκτοί): "elect" in L, "chosen" in M, "God's chosen people / those he has
  chosen" in T — election language must remain explicit; not softened to "special."
- G4268 (πρόγνωσιν): "foreknowledge" in L/M (technical theological term); T uses "eternal plan/purpose"
  to surface that this is not mere foresight but purposive divine initiative.
- G38 (ἁγιασμός): "sanctification" in L (preserve the technical term); "sanctifying work" in M;
  "making holy" or "act of setting apart" in T.
- G4473 (ῥαντισμόν, sprinkling of blood): L "sprinkling of blood" — directly echoes Moses' covenant
  ceremony (Ex 24:8) and the Levitical priestly inauguration. T surfaces this Exodus covenant echo.
- G313 (ἀναγεννάω, born again): "born again" / "new birth" throughout — regeneration language.
  First occurrence is 1:3 (aorist — completed act of new birth); second is 1:23 (perfect participle —
  past act with lasting present result: "having been born again").
- G166 (αἰώνιος): not in chs 1–2. (Appears in 1 Pet 5 only.)
- OT intertextuality:
  - 1:24–25: Direct quotation of Isa 40:6–8 (all flesh like grass). Quoted in full in all tiers;
    T marks the source.
  - 2:6: Quotation of Isa 28:16 (cornerstone in Zion). T marks source.
  - 2:7: Allusion to Ps 118:22 (rejected stone becomes cornerstone). T marks source.
  - 2:8: Allusion to Isa 8:14 (stone of stumbling). T marks source.
  - 2:9: Sustained echo of Ex 19:5–6 (chosen race, royal priesthood, holy nation, treasured possession)
    and Isa 43:20–21. T makes Ex 19 explicit.
  - 2:10: Echoes Hos 1:6, 1:9, 2:23 (not-my-people / now-my-people reversal). T marks source.
  - 2:22: Isa 53:9 ("no sin / no deceit in his mouth"). T marks source.
  - 2:24: Isa 53:4–5 ("bore our sins / by his wounds"). T marks source.
  - 2:25: Isa 53:6 ("sheep going astray"). T marks source.
- Aspect notes:
  - 1:3 ἀναγεννήσας (aorist) = single past act of giving new birth — rendered as completed event.
  - 1:5 φρουρουμένους (present participle) = ongoing guarding — "being guarded / are being shielded."
  - 1:22 ἡγνικότες (perfect) = past purification with present standing — "having purified."
  - 2:5 οἰκοδομεῖσθε (present passive) = ongoing construction — "are being built up."
  - 2:23 παρεδίδου (imperfect) = ongoing, habitual entrusting — "kept entrusting / continued to entrust."
- Divine passive: 2:8 "they were appointed" (ἐτέθησαν, aorist passive) — divine appointment implied;
  noted in T tier.
- Honour-shame culture: 2:6 "not put to shame" / 2:7 "precious" (τιμή = honour, worth) / 2:17 "honour
  all people" — the honour/shame axis runs through the entire passage. T makes these dynamics explicit.
- 2:18 οἰκέτης (household slave/domestic servant): L "servant," M "slave," T "those in domestic
  service" — Peter addresses the patron-client social structure without anachronistic modernising.
- 2:13 κτίσει (ordinance / institution / creature): "institution" (L), "authority" (M), "human authority"
  (T) — not the natural/creation meaning; the political-social sense is clear in context.
"""

import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

PETER1 = {
  "1": {
    "1": {
      "L": "Peter, an apostle of Jesus Christ, to the sojourners of the Dispersion scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia,",
      "M": "Peter, an apostle of Jesus Christ, To the exiles scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia—",
      "T": "From Peter, an apostle of Jesus Christ, to God's dispersed people living as exiles throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia—"
    },
    "2": {
      "L": "elect according to the foreknowledge of God the Father, in the sanctification of the Spirit, for obedience to Jesus Christ and sprinkling of his blood: May grace and peace be multiplied to you.",
      "M": "who have been chosen according to the foreknowledge of God the Father, through the sanctifying work of the Spirit, to be obedient to Jesus Christ and sprinkled with his blood: Grace and peace be yours in abundance.",
      "T": "You are God's elect—chosen according to his eternal purpose, set apart by the Spirit's work, called to obey Jesus Christ and be cleansed by his blood in the covenant he established. May grace and peace overflow in your lives."
    },
    "3": {
      "L": "Blessed be the God and Father of our Lord Jesus Christ! According to his great mercy, he has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead,",
      "M": "Praise be to the God and Father of our Lord Jesus Christ! In his great mercy he has given us new birth into a living hope through the resurrection of Jesus Christ from the dead,",
      "T": "All praise to the God and Father of our Lord Jesus Christ! Out of his tremendous mercy he has given us new birth into a hope that is vibrantly alive—secured by the resurrection of Jesus Christ from the dead."
    },
    "4": {
      "L": "to an inheritance that is imperishable, undefiled, and unfading, kept in heaven for you,",
      "M": "and into an inheritance that can never perish, spoil, or fade. This inheritance is kept in heaven for you,",
      "T": "This new birth gives us an inheritance waiting in heaven—one that cannot be destroyed, corrupted, or fade away—kept safe there for us,"
    },
    "5": {
      "L": "who are being guarded through faith by the power of God for a salvation ready to be revealed in the last time.",
      "M": "who through faith are being shielded by God's power until the coming of the salvation that is ready to be revealed in the last time.",
      "T": "while God's own power is continuously guarding us through our faith—until the final salvation is unveiled at the close of this age."
    },
    "6": {
      "L": "In this you rejoice, though now for a little while, if necessary, you have been grieved by various trials,",
      "M": "In all this you greatly rejoice, though now for a little while you may have had to suffer grief in all kinds of trials.",
      "T": "This is why you can rejoice—even while you are right now going through various painful trials for a brief season."
    },
    "7": {
      "L": "so that the tested genuineness of your faith—more precious than gold that perishes though it is tested by fire—may be found to result in praise and glory and honor at the revelation of Jesus Christ.",
      "M": "These have come so that the proven genuineness of your faith—of greater worth than gold, which perishes even though refined by fire—may result in praise, glory and honor when Jesus Christ is revealed.",
      "T": "These trials are testing your faith—and that tested faith is far more precious than gold, which fire can refine but which will still perish. When Jesus Christ appears, your proven faith will bring you praise, glory, and honor."
    },
    "8": {
      "L": "Though you have not seen him, you love him. Though you do not now see him, you believe in him and rejoice with joy that is inexpressible and filled with glory,",
      "M": "Though you have not seen him, you love him; and even though you do not see him now, you believe in him and are filled with an inexpressible and glorious joy,",
      "T": "You love him even though you have never seen him. You believe in him without seeing him, and even now you are filled with an indescribable, glory-saturated joy—"
    },
    "9": {
      "L": "obtaining the outcome of your faith, the salvation of your souls.",
      "M": "for you are receiving the end result of your faith, the salvation of your souls.",
      "T": "because you are already receiving what faith is designed to obtain: the salvation of your souls."
    },
    "10": {
      "L": "Concerning this salvation, the prophets who prophesied about the grace that was to be yours searched and inquired carefully,",
      "M": "Concerning this salvation, the prophets, who spoke of the grace that was to come to you, searched intently and with the greatest care,",
      "T": "The prophets who foretold this grace destined for you pored over their own writings with intense curiosity—"
    },
    "11": {
      "L": "inquiring what person or time the Spirit of Christ in them was indicating when he predicted the sufferings of Christ and the subsequent glories.",
      "M": "trying to find out the time and circumstances to which the Spirit of Christ in them was pointing when he predicted the sufferings of the Messiah and the glories that would follow.",
      "T": "they were trying to determine when and under what circumstances these things would happen—for the Spirit of Christ within them was pointing ahead to Christ's sufferings and the glories that would follow in their wake."
    },
    "12": {
      "L": "It was revealed to them that they were serving not themselves but you, in the things that have now been announced to you through those who preached the good news to you by the Holy Spirit sent from heaven, things into which angels long to look.",
      "M": "It was revealed to them that they were not serving themselves but you, when they spoke of the things that have now been told you by those who have preached the gospel to you by the Holy Spirit sent from heaven. Even angels long to look into these things.",
      "T": "God revealed to those prophets that they were writing not for their own generation but for yours—the very things now proclaimed to you by those who brought the good news, carried along by the Holy Spirit sent from heaven. Even angels lean in, longing to understand these mysteries."
    },
    "13": {
      "L": "Therefore, preparing your minds for action, and being sober-minded, set your hope fully on the grace that will be brought to you at the revelation of Jesus Christ.",
      "M": "Therefore, with minds that are alert and fully sober, set your hope on the grace to be brought to you when Jesus Christ is revealed at his coming.",
      "T": "So tighten your mental grip—clear-headed and fully alert—and pour all your hope into the grace that will be yours when Jesus Christ is revealed."
    },
    "14": {
      "L": "As obedient children, do not be conformed to the desires that you formerly had in your ignorance,",
      "M": "As obedient children, do not conform to the evil desires you had when you lived in ignorance.",
      "T": "Live as obedient children—don't let your lives still be shaped by the desires that ruled you in your pre-faith days of ignorance."
    },
    "15": {
      "L": "but as he who called you is holy, you also be holy in all your conduct,",
      "M": "But just as he who called you is holy, so be holy in all you do;",
      "T": "Instead, model your whole way of life on the holiness of the one who called you—"
    },
    "16": {
      "L": "since it is written, 'You shall be holy, for I am holy.'",
      "M": "for it is written: 'Be holy, because I am holy.'",
      "T": "for Scripture says: 'Be holy, because I am holy.' (Leviticus 11:44)"
    },
    "17": {
      "L": "And if you call on him as Father who judges impartially according to each one's deeds, conduct yourselves with fear during the time of your exile,",
      "M": "Since you call on a Father who judges each person's work impartially, live out your time as foreigners here in reverent fear.",
      "T": "You call on God as your Father—the same God who judges every person's conduct with absolute impartiality. So live your entire time as exiles on this earth with a reverent, healthy fear of him."
    },
    "18": {
      "L": "knowing that you were ransomed from the futile ways inherited from your forefathers, not with perishable things such as silver or gold,",
      "M": "For you know that it was not with perishable things such as silver or gold that you were redeemed from the empty way of life handed down to you from your ancestors,",
      "T": "Remember what you have been freed from: the hollow, futile way of life you inherited from your ancestors. That freedom cost something no silver or gold could pay—"
    },
    "19": {
      "L": "but with the precious blood of Christ, like that of a lamb without blemish or spot.",
      "M": "but with the precious blood of Christ, a lamb without blemish or defect.",
      "T": "it was paid with the precious blood of Christ—the blood of a perfect, spotless sacrificial lamb."
    },
    "20": {
      "L": "He was foreknown before the foundation of the world but was made manifest in the last times for the sake of you",
      "M": "He was chosen before the creation of the world, but was revealed in these last times for your sake.",
      "T": "Christ was chosen for this role before the world was ever made, but was revealed at this final moment in history—for your sake."
    },
    "21": {
      "L": "who through him are believers in God, who raised him from the dead and gave him glory, so that your faith and hope are in God.",
      "M": "Through him you believe in God, who raised him from the dead and glorified him, and so your faith and hope are in God.",
      "T": "Through Christ you have come to trust in God—the God who raised him from the dead and exalted him—making him the very ground on which your faith and hope stand."
    },
    "22": {
      "L": "Having purified your souls in obeying the truth for sincere brotherly love, love one another earnestly from a pure heart,",
      "M": "Now that you have purified yourselves by obeying the truth so that you have sincere love for each other, love one another deeply, from the heart.",
      "T": "You have cleansed your souls by obeying the truth, and this has produced genuine love for your fellow believers. Now go further—love one another with wholehearted intensity from a pure heart."
    },
    "23": {
      "L": "since you have been born again, not of perishable seed but of imperishable, through the living and abiding word of God;",
      "M": "For you have been born again, not of perishable seed, but of imperishable, through the living and enduring word of God.",
      "T": "This new nature you have was not born from any passing human seed—it came from something imperishable: the living, enduring word of God."
    },
    "24": {
      "L": "for 'All flesh is like grass, and all its glory like the flower of grass. The grass withers, and the flower falls,'",
      "M": "For, 'All people are like grass, and all their glory is like the flowers of the field; the grass withers and the flowers fall,'",
      "T": "'All human life is like grass, and all its beauty like a wildflower—the grass shrivels and the flower drops,' (Isaiah 40:6–7)"
    },
    "25": {
      "L": "'but the word of the Lord endures forever.' And this word is the good news that was preached to you.",
      "M": "'but the word of the Lord endures forever.' And this is the word that was preached to you.",
      "T": "'but the word of the Lord stands forever.' (Isaiah 40:8) This enduring, living word is precisely what was proclaimed to you as the gospel."
    }
  },
  "2": {
    "1": {
      "L": "So put aside all malice and all deceit and hypocrisy and envy and all slander.",
      "M": "Therefore, rid yourselves of all malice and all deceit, hypocrisy, envy, and slander of every kind.",
      "T": "Strip away everything incompatible with your new birth: malice, deception, hypocrisy, envy, and every form of slander."
    },
    "2": {
      "L": "Like newborn infants, long for the pure spiritual milk, that by it you may grow up into salvation—",
      "M": "Like newborn babies, crave pure spiritual milk, so that by it you may grow up in your salvation,",
      "T": "Like newborn babies craving their mother's milk, crave the pure nourishment of God's word—it is how you grow toward full salvation."
    },
    "3": {
      "L": "if indeed you have tasted that the Lord is good.",
      "M": "now that you have tasted that the Lord is good.",
      "T": "After all, you have already tasted how good the Lord is."
    },
    "4": {
      "L": "As you come to him, a living stone rejected by men but in the sight of God chosen and precious,",
      "M": "As you come to him, the living Stone—rejected by humans but chosen by God and precious to him—",
      "T": "Come to him—the living Stone, discarded by human hands but chosen by God and of infinite worth to him—"
    },
    "5": {
      "L": "you yourselves, like living stones, are being built up as a spiritual house, to be a holy priesthood, to offer spiritual sacrifices acceptable to God through Jesus Christ.",
      "M": "you also, like living stones, are being built into a spiritual house to be a holy priesthood, offering spiritual sacrifices acceptable to God through Jesus Christ.",
      "T": "and you too, as living stones, are being constructed into a spiritual temple—a holy priestly community whose spiritual sacrifices God gladly receives through Jesus Christ."
    },
    "6": {
      "L": "For it stands in Scripture: 'Behold, I am laying in Zion a stone, a cornerstone chosen and precious, and whoever believes in him will not be put to shame.'",
      "M": "For in Scripture it says: 'See, I lay a stone in Zion, a chosen and precious cornerstone, and the one who trusts in him will never be put to shame.'",
      "T": "For Scripture declares: 'Look—I am placing in Zion a cornerstone, chosen and priceless. The person who trusts in him will never be put to shame.' (Isaiah 28:16)"
    },
    "7": {
      "L": "So the honor is for you who believe, but for those who do not believe, 'The stone that the builders rejected has become the cornerstone,'",
      "M": "Now to you who believe, this stone is precious. But to those who do not believe, 'The stone the builders rejected has become the cornerstone,'",
      "T": "For those who believe, this cornerstone is their greatest honor and treasure. But for those who refuse to believe—'the stone the builders threw away has become the cornerstone' (Psalm 118:22)—"
    },
    "8": {
      "L": "and 'a stone of stumbling and a rock of offense.' They stumble because they disobey the word, as they were destined to do.",
      "M": "and, 'A stone that causes people to stumble and a rock that makes them fall.' They stumble because they disobey the message—which is also what they were destined for.",
      "T": "he is also a stone that trips people up, a rock that makes them fall. (Isaiah 8:14) They stumble because they refuse to obey the word—and this, too, was appointed by God."
    },
    "9": {
      "L": "But you are a chosen race, a royal priesthood, a holy nation, a people for his own possession, that you may proclaim the excellencies of him who called you out of darkness into his marvelous light.",
      "M": "But you are a chosen people, a royal priesthood, a holy nation, God's special possession, that you may declare the praises of him who called you out of darkness into his wonderful light.",
      "T": "But you—you are a chosen people, a royal priesthood, a holy nation, God's very own treasured possession. (Exodus 19:5–6) You exist to broadcast the mighty deeds of the one who pulled you out of darkness and into his astonishing light."
    },
    "10": {
      "L": "Once you were not a people, but now you are God's people; once you had not received mercy, but now you have received mercy.",
      "M": "Once you were not a people, but now you are the people of God; once you had not received mercy, but now you have received mercy.",
      "T": "Once you had no identity as a people; now you are God's own people. Once there was no mercy for you; now you live entirely within his mercy. (Hosea 1:6, 9; 2:23)"
    },
    "11": {
      "L": "Beloved, I urge you as sojourners and exiles to abstain from the desires of the flesh that wage war against your soul.",
      "M": "Dear friends, I urge you, as foreigners and exiles, to abstain from sinful desires, which wage war against your soul.",
      "T": "Dear friends, you are foreign nationals and transient residents in this world—so stay well away from fleshly cravings, which are actively fighting against your soul."
    },
    "12": {
      "L": "Keep your conduct among the Gentiles honorable, so that when they speak against you as evildoers, they may see your good deeds and glorify God on the day of visitation.",
      "M": "Live such good lives among the pagans that, though they accuse you of doing wrong, they may see your good deeds and glorify God on the day he visits us.",
      "T": "Live such exemplary lives among unbelievers that even those who slander you now will see your good works and end up glorifying God on the day of his coming."
    },
    "13": {
      "L": "Be subject for the Lord's sake to every human institution, whether to the emperor as supreme,",
      "M": "Submit yourselves for the Lord's sake to every human authority: whether to the emperor, as the supreme authority,",
      "T": "For the Lord's sake, honor every human authority structure—including the emperor as the supreme one—"
    },
    "14": {
      "L": "or to governors as sent by him to punish those who do evil and to praise those who do good.",
      "M": "or to governors, who are sent by him to punish those who do wrong and to commend those who do right.",
      "T": "or governors, who are his instruments for punishing wrongdoers and affirming those who do right."
    },
    "15": {
      "L": "For this is the will of God, that by doing good you should put to silence the ignorance of foolish people.",
      "M": "For it is God's will that by doing good you should silence the ignorant talk of foolish people.",
      "T": "God's will is this: that your good conduct silences the uninformed criticism of those who don't know better."
    },
    "16": {
      "L": "Live as people who are free, not using your freedom as a cover-up for evil, but living as servants of God.",
      "M": "Live as free people, but do not use your freedom as a cover-up for evil; live as God's slaves.",
      "T": "Live as genuinely free people—but don't use freedom as a smokescreen for evil. True freedom means belonging to God."
    },
    "17": {
      "L": "Honor everyone. Love the brotherhood. Fear God. Honor the emperor.",
      "M": "Show proper respect to everyone, love the family of believers, fear God, honor the emperor.",
      "T": "Give everyone their due respect. Love your fellow believers wholeheartedly. Stand in reverent awe of God. Honor the emperor."
    },
    "18": {
      "L": "Servants, be subject to your masters with all respect, not only to the good and gentle but also to the unjust.",
      "M": "Slaves, in reverent fear of God submit yourselves to your masters, not only to those who are good and considerate, but also to those who are harsh.",
      "T": "Those in domestic service—submit to your masters with complete respect, not only to the kind and reasonable ones, but even to the harsh and unreasonable."
    },
    "19": {
      "L": "For this is a gracious thing, when, mindful of God, someone endures sorrows while suffering unjustly.",
      "M": "For it is commendable if someone bears up under the pain of unjust suffering because they are conscious of God.",
      "T": "There is something genuinely praiseworthy about enduring unjust suffering when you do it with an awareness of God's presence."
    },
    "20": {
      "L": "For what credit is it if, when you sin and are beaten for it, you endure? But if when you do good and suffer for it you endure, this is a gracious thing in the sight of God.",
      "M": "But how is it to your credit if you receive a beating for doing wrong and endure it? But if you suffer for doing good and you endure it, this is commendable before God.",
      "T": "What credit is there in patiently enduring punishment you deserve? But when you do what is right and suffer for it anyway—and keep going—that is something God himself considers praiseworthy."
    },
    "21": {
      "L": "For to this you have been called, because Christ also suffered for you, leaving you an example, so that you might follow in his steps.",
      "M": "To this you were called, because Christ suffered for you, leaving you an example, that you should follow in his steps.",
      "T": "This is precisely the life you were called to—because Christ himself suffered on your behalf, leaving you a pattern to trace with your own steps."
    },
    "22": {
      "L": "He committed no sin, neither was deceit found in his mouth.",
      "M": "'He committed no sin, and no deceit was found in his mouth.'",
      "T": "He never sinned—not once. No deceptive word ever passed his lips. (Isaiah 53:9)"
    },
    "23": {
      "L": "When he was reviled, he did not revile in return; when he suffered, he did not threaten, but continued entrusting himself to him who judges justly.",
      "M": "When they hurled their insults at him, he did not retaliate; when he suffered, he made no threats. Instead, he kept entrusting himself to him who judges justly.",
      "T": "When insulted, he did not retaliate. When he suffered, he made no threats. He simply kept entrusting himself into the hands of the one who judges with perfect fairness."
    },
    "24": {
      "L": "He himself bore our sins in his body on the tree, that we might die to sin and live to righteousness. By his wounds you have been healed.",
      "M": "'He himself bore our sins' in his body on the cross, so that we might die to sins and live for righteousness; 'by his wounds you have been healed.'",
      "T": "He took our sins onto himself—carrying them in his own body up to the cross—so that we would die to sin's power and live fully for righteousness. His wounds have become our healing. (Isaiah 53:4–5)"
    },
    "25": {
      "L": "For you were straying like sheep, but have now returned to the Shepherd and Overseer of your souls.",
      "M": "For 'you were like sheep going astray,' but now you have returned to the Shepherd and Overseer of your souls.",
      "T": "You were wandering like lost sheep—but now you have come home to the Shepherd who watches over and guards your souls. (Isaiah 53:6)"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1peter')
        merge_tier(existing, PETER1, tier_key)
        save(tier_dir, '1peter', existing)
    print('1 Peter 1–2 written.')

if __name__ == '__main__':
    main()
