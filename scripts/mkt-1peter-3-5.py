"""
MKT 1 Peter chapters 3–5 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1peter-3-5.py

Conventions carried forward from mkt-1peter-1-2.py:
- G2962 (κύριος): "Lord" throughout all tiers.
- G4102 (πίστις): "faith" — believers' trusting reliance, not Christ's own faithfulness.
- G26 (ἀγάπη): "love" — willed, covenantal. G5360 (φιλαδελφία) = brotherly love (distinct).
- G1343 (δικαιοσύνη): "righteousness" in L/M; "right standing / right conduct" in T.
- G4561 (σάρξ): "flesh" in L; M uses context ("body" when purely physical, "flesh" when
    creatureliness/moral dimension is present); T unpacks.
- G3927/G3941 (sojourner/stranger): "sojourners" / "strangers" in L, "exiles" / "foreigners" in M;
    T surfaces the diaspora identity fully.
- G1588 (ἐκλεκτός): "elect" in L, "chosen" in M, "those God has chosen" in T.

Translation decisions specific to chapters 3–5:
- G4151 (πνεῦμα) — three distinct occurrences with different renderings:
    3:18 ζῳοποιηθεὶς δὲ πνεύματι: "made alive in the Spirit" (capitalized) — dative best read
      as instrumental (the Holy Spirit raised Christ, cf. Rom 8:11), not locative "in the realm
      of spirit." Capitalized, consistent with chs 1–2 convention for Holy Spirit.
    4:6 ζῷεν δὲ κατὰ θεὸν πνεύματι: "live in the spirit" (lowercase) — locative dative, the
      sphere/domain of existence before God as opposed to merely fleshly/human existence. The
      contrast is ontological (flesh vs. spirit as realms of being), not pneumatological.
    4:14 τὸ τοῦ θεοῦ πνεῦμα: "the Spirit of glory and of God" (capitalized) — the Holy Spirit
      explicitly named; rests on the suffering community as the Spirit rested on the Servant
      (Isa 11:2). T marks the Isaiah echo.
- G499 (ἀντίτυπος, 3:21): L "counterpart figure"; M "which corresponds to this"; T renders the
    typological pattern explicitly: the flood-water prefigured baptismal water. Not allegory
    but real historical correspondence in salvation history.
- G1906 (ἐπερώτημα, 3:21): "pledge/appeal" — a formal request or solemn commitment made toward
    God, not merely a polite asking. L: "appeal"; M: "pledge"; T: "a solemn vow made from a
    clear conscience toward God."
- "Spirits in prison" (3:19–20): these are the Watchers who rebelled before the flood — the
    fallen heavenly beings of Gen 6:1–4, imprisoned per 1 Enoch 6–16 and Jubilees. The same
    tradition is invoked in 2 Pet 2:4 and Jude 6. Christ's κήρυσσεν is a herald's victory
    proclamation, not an offer of post-mortem salvation. T renders accordingly.
- G3056 (λόγος, 3:15 "reason/account"): here λόγον = formal "account / reasoned defense" in the
    semi-legal sense — being called to explain oneself before a questioner. Not Greek
    philosophical Logos. L/M: "a reason"; T: "an account."
- G166 (αἰώνιος, 5:10): "eternal" in L/M. T: "the life of the coming age" — the qualitative
    dimension of God's future glory, not merely infinite duration.
- 5:5 quotation of Prov 3:34 (LXX): "God opposes the proud but gives grace to the humble."
    The same citation appears in Jas 4:6 — Peter and James draw on the same Wisdom tradition.
    T notes the source.
- "Babylon" (5:13): the conventional symbolic name for Rome in early Christian literature
    (cf. Rev 17:5; 18:2; Sib. Or. 5:143). Peter writes from Rome; the church there sends
    greetings to the diaspora communities of Asia Minor. T makes this identification explicit.
- 5:8 "roaring lion": vivid imagery preserved undiminished in all tiers. The metaphor must not
    be domesticated.
- OT intertextuality in chs 3–5:
    3:10–12: Extended quotation of Ps 34:12–16 (LXX 33:13–17). T marks source.
    3:14: Echo of Isa 8:12–13 ("do not fear what they fear / sanctify the Lord as holy"). T marks.
    4:8: Alludes to Prov 10:12 ("love covers all offenses"). T marks source.
    4:14: Echoes Isa 11:2 (Spirit resting on the Servant/Messiah). T marks.
    4:18: Quotation of Prov 11:31 (LXX). T marks source.
    5:5: Quotation of Prov 3:34 (LXX). T marks source.
- Aspect notes:
    3:9 ἀποδιδόντες (present participle) = ongoing practice — "not repaying / do not repay."
    3:18 παθόντος / aorist forms = single completed act of death — "suffered once."
    3:22 πορευθεὶς (aorist participle) = completed journey — "having gone into heaven."
    4:1 παθόντος (aorist) = completed suffering — "since Christ suffered."
    5:10 παθόντας (aorist) = brief completed ordeal — "after you have suffered a little while."
- Honour-shame dynamics: 3:16 "put to shame" / 4:16 "not ashamed" / 5:4 "crown of glory" —
    the entire section operates in the honour-shame register of first-century Roman society.
    T makes these dynamics explicit where the Greek requires it.
- Divine passive: 3:22 "having been subjected to him" (ὑποταγέντων, aorist passive) = God is the
    unnamed agent of subjecting all powers to the risen Christ.
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
  "3": {
    "1": {
      "L": "Likewise, wives, be subject to your own husbands, so that even if some disobey the word, they may be won without a word through the conduct of their wives,",
      "M": "Wives, in the same way submit yourselves to your own husbands so that, if any of them do not believe the word, they may be won over without words by the behavior of their wives,",
      "T": "Wives — take up the same posture of willing service. Even if your husband refuses to believe the message, you may win him over not by arguing but simply by the way you live."
    },
    "2": {
      "L": "when they behold your pure conduct in fear.",
      "M": "when they see the purity and reverence of your lives.",
      "T": "He will see your pure and reverent life — and it will reach him where words never could."
    },
    "3": {
      "L": "Let your adorning not be the outward kind — braiding of hair and putting on gold jewelry, or wearing of garments —",
      "M": "Your beauty should not come from outward adornment, such as elaborate hairstyles and the wearing of gold jewelry or fine clothes.",
      "T": "Do not invest everything in outward appearance — braided hair, gold jewelry, fine clothing."
    },
    "4": {
      "L": "but let it be the hidden person of the heart with the imperishable quality of a gentle and quiet spirit, which is of great worth before God.",
      "M": "Rather, it should be that of your inner self, the unfading beauty of a gentle and quiet spirit, which is of great worth in God's sight.",
      "T": "The real beauty God sees is the hidden person of the heart — a gentle, quiet spirit that does not fade. That is what God counts as precious."
    },
    "5": {
      "L": "For in this way also the holy women of old who hoped in God used to adorn themselves, being subject to their own husbands,",
      "M": "For this is the way the holy women of the past who put their hope in God used to adorn themselves. They submitted themselves to their own husbands,",
      "T": "The holy women of Israel's history — those who placed their hope in God — adorned themselves exactly this way, by living in willing submission to their husbands."
    },
    "6": {
      "L": "as Sarah obeyed Abraham, calling him lord; of whom you are children, if you do good and are not afraid of any terror.",
      "M": "like Sarah, who obeyed Abraham and called him her lord. You are her daughters if you do what is right and do not give way to fear.",
      "T": "Sarah is the pattern — she obeyed Abraham and called him lord. You are her daughters when you do good and refuse to let fear control you."
    },
    "7": {
      "L": "Husbands, likewise, dwell with your wives according to knowledge, showing honor to the woman as the weaker vessel, being heirs together of the grace of life, so that your prayers may not be hindered.",
      "M": "Husbands, in the same way be considerate as you live with your wives, and treat them with respect as the weaker partner and as heirs with you of the gracious gift of life, so that nothing will hinder your prayers.",
      "T": "Husbands — live with your wife with real understanding. She is physically more vulnerable; she is equally an heir of the life God gives by grace. Honor her accordingly. Fail to do this, and your prayers will be cut off."
    },
    "8": {
      "L": "Finally, all be of one mind, sympathetic, loving as brothers, tenderhearted, humble-minded;",
      "M": "Finally, all of you, be like-minded, be sympathetic, love one another, be compassionate and humble.",
      "T": "To sum up: be united in how you think, enter into one another's pain, love your fellow believers, carry each other's burdens, and walk in genuine humility."
    },
    "9": {
      "L": "not rendering evil for evil or reviling for reviling, but on the contrary blessing, knowing that to this you were called, that you might inherit a blessing.",
      "M": "Do not repay evil with evil or insult with insult. On the contrary, repay evil with blessing, because to this you were called so that you may inherit a blessing.",
      "T": "Never return evil for evil or a cutting word for a cutting word. Instead, speak blessing — this is the very purpose for which you were called, and it will bring blessing back to you."
    },
    "10": {
      "L": "For 'He who desires to love life and to see good days, let him keep his tongue from evil and his lips from speaking deceit;'",
      "M": "For, 'Whoever would love life and see good days must keep their tongue from evil and their lips from deceitful speech.'",
      "T": "Psalm 34 says it plainly: 'Do you want to love life and fill your days with good things? Keep your tongue away from evil and your lips away from every lie.'"
    },
    "11": {
      "L": "'let him turn away from evil and do good; let him seek peace and pursue it.'",
      "M": "'They must turn from evil and do good; they must seek peace and pursue it.'",
      "T": "'Turn your back on evil and do good. Hunt for peace — chase it down.'"
    },
    "12": {
      "L": "'For the eyes of the Lord are upon the righteous, and his ears are open to their prayer; but the face of the Lord is against those who do evil.'",
      "M": "'For the eyes of the Lord are on the righteous and his ears are attentive to their prayer, but the face of the Lord is against those who do evil.'",
      "T": "'The Lord has his eyes fixed on the righteous and his ears open to their prayers — but he sets his face against all who do evil.' (Ps 34:12–16)"
    },
    "13": {
      "L": "And who is there to harm you if you become zealous for what is good?",
      "M": "Who is going to harm you if you are eager to do good?",
      "T": "If you are genuinely committed to doing good, who is really going to hurt you for it?"
    },
    "14": {
      "L": "But even if you should suffer for the sake of righteousness, you are blessed. And do not fear their fear, nor be troubled,",
      "M": "But even if you should suffer for what is right, you are blessed. 'Do not fear what they fear; do not be frightened.'",
      "T": "Even if doing right brings suffering on you — you are blessed for it. Do not let their intimidation control you; do not be shaken. (Echo of Isa 8:12–13)"
    },
    "15": {
      "L": "but sanctify Christ as Lord in your hearts, always being ready to make a defense to everyone who asks you for a reason concerning the hope that is in you, yet with gentleness and fear,",
      "M": "But in your hearts revere Christ as Lord. Always be prepared to give an answer to everyone who asks you to give the reason for the hope that you have. But do this with gentleness and respect,",
      "T": "Instead, set Christ apart as Lord in the deepest part of you. Be ready at any moment to stand before anyone who demands an account of the hope you carry — and give that account with gentleness and proper reverence."
    },
    "16": {
      "L": "having a good conscience, so that in the thing in which you are slandered, those who revile your good conduct in Christ may be put to shame.",
      "M": "keeping a clear conscience, so that those who speak maliciously against your good behavior in Christ may be ashamed of their slander.",
      "T": "Keep your conscience clean. When they slander you, the good life you have lived in Christ will shame them and leave them with nothing credible to say."
    },
    "17": {
      "L": "For it is better to suffer for doing good, if God should so will, than for doing evil.",
      "M": "For it is better, if it is God's will, to suffer for doing good than for doing evil.",
      "T": "It is always better — when God permits suffering — to suffer for doing right than for doing wrong."
    },
    "18": {
      "L": "Because Christ also suffered once for sins, the righteous for the unrighteous, that he might bring us to God, being put to death in the flesh but made alive in the Spirit,",
      "M": "For Christ also suffered once for sins, the righteous for the unrighteous, to bring you to God. He was put to death in the body but made alive in the Spirit,",
      "T": "Christ himself died for sins once — the righteous one taking the place of the unrighteous — to bring you into God's presence. His body was killed; the Spirit raised him to life."
    },
    "19": {
      "L": "in which also he went and proclaimed to the spirits in prison,",
      "M": "After being made alive, he went and made proclamation to the imprisoned spirits —",
      "T": "In that same power he went and announced his victory to the spirits kept in confinement —"
    },
    "20": {
      "L": "those who were formerly disobedient, when the patience of God was waiting in the days of Noah while an ark was being prepared, in which a few, that is eight souls, were saved through water.",
      "M": "to those who were disobedient long ago when God waited patiently in the days of Noah while the ark was being built. In it only a few people, eight in all, were saved through water,",
      "T": "the rebellious Watchers of Gen 6:1–4, imprisoned before Noah's flood per the tradition of 1 Enoch — those who defied God when he held back judgment while the ark was being built. Eight human souls came through the floodwaters alive."
    },
    "21": {
      "L": "and which as a counterpart figure now saves you also — baptism, not the removal of filth from the flesh, but the appeal of a good conscience toward God — through the resurrection of Jesus Christ,",
      "M": "and this water symbolizes baptism that now saves you also — not the removal of dirt from the body but the pledge of a clear conscience toward God. It saves you by the resurrection of Jesus Christ,",
      "T": "That flood is the pattern; baptism is what it was pointing forward to — and it now saves you. Not because water washes off external grime, but because it is a solemn vow made from a clear conscience before God. It saves because Christ rose from the dead."
    },
    "22": {
      "L": "who is at the right hand of God, having gone into heaven, with angels and authorities and powers having been subjected to him.",
      "M": "who has gone into heaven and is at God's right hand — with angels, authorities and powers in submission to him.",
      "T": "He has gone into heaven and sits at the right hand of God — angels, rulers, and cosmic powers all placed in submission beneath him (divine passive: God subjected them all)."
    }
  },
  "4": {
    "1": {
      "L": "Therefore, since Christ suffered in the flesh, arm yourselves also with the same mind — because he who has suffered in the flesh has ceased from sin —",
      "M": "Therefore, since Christ suffered in his body, arm yourselves also with the same attitude, because whoever suffers in the body is done with sin.",
      "T": "Since Christ endured suffering in the flesh, arm yourself with the same resolve — the one who has suffered in the body has broken free from sin's controlling grip."
    },
    "2": {
      "L": "so as to live no longer by human desires but by the will of God for the remaining time in the flesh.",
      "M": "As a result, they do not live the rest of their earthly lives for evil human desires, but rather for the will of God.",
      "T": "That means the time still left in your body is no longer spent chasing human cravings — it is given over entirely to doing what God wants."
    },
    "3": {
      "L": "For the time that is past suffices for doing the will of the Gentiles — having lived in licentiousness, lusts, drunkenness, carousing, drinking bouts, and lawless idolatry.",
      "M": "For you have spent enough time in the past doing what pagans choose to do — living in debauchery, lust, drunkenness, orgies, carousing and detestable idolatry.",
      "T": "You have already spent too many years living the way those outside the covenant live — in sensuality, craving, drunkenness, wild parties, and every form of idol worship."
    },
    "4": {
      "L": "In this they are surprised that you do not run with them into the same overflow of debauchery, speaking evil of you;",
      "M": "They are surprised that you do not join them in their reckless, wild living, and they heap abuse on you.",
      "T": "They cannot understand why you will no longer plunge with them into the same torrent of excess — and they turn that confusion into slander against you."
    },
    "5": {
      "L": "who will give account to him who is ready to judge the living and the dead.",
      "M": "But they will have to give account to him who is ready to judge the living and the dead.",
      "T": "They will answer for it — before the one who stands ready to judge every person alive and every person who has ever died."
    },
    "6": {
      "L": "For this reason the gospel was preached even to the dead, that though judged in the flesh according to men, they might live in the spirit according to God.",
      "M": "For this is the reason the gospel was preached even to those who are now dead, so that they might be judged according to human standards in regard to the body, but live according to God in regard to the spirit.",
      "T": "This is why the good news was proclaimed even to those who have since died — so that, though the body faced death by human reckoning, the spirit might live in the way that belongs to God."
    },
    "7": {
      "L": "But the end of all things is at hand; therefore be sober-minded and watchful for prayers.",
      "M": "The end of all things is near. Therefore be alert and of sober mind so that you may pray.",
      "T": "Everything is drawing toward its close. So keep a clear head and a sober spirit — your prayer life depends on it."
    },
    "8": {
      "L": "Above all, having fervent love among yourselves, because love covers a multitude of sins.",
      "M": "Above all, love each other deeply, because love covers over a multitude of sins.",
      "T": "More than anything else: love one another urgently and without holding back — for love draws a veil over a multitude of offenses. (Cf. Prov 10:12)"
    },
    "9": {
      "L": "Being hospitable to one another without grumbling.",
      "M": "Offer hospitality to one another without grumbling.",
      "T": "Open your homes to one another — and do it without a word of grudging."
    },
    "10": {
      "L": "As each one received a gift, minister it to one another as good stewards of God's varied grace.",
      "M": "Each of you should use whatever gift you have received to serve others, as faithful stewards of God's grace in its various forms.",
      "T": "Whatever gift you have been given, put it to work for the others — that is what good stewardship of God's many-sided grace looks like."
    },
    "11": {
      "L": "If anyone speaks, let it be as oracles of God; if anyone ministers, let it be from the strength which God supplies, so that in all things God may be glorified through Jesus Christ, to whom belongs glory and dominion forever and ever. Amen.",
      "M": "If anyone speaks, they should do so as one who speaks the very words of God. If anyone serves, they should do so with the strength God provides, so that in all things God may be praised through Jesus Christ. To him be the glory and the power for ever and ever. Amen.",
      "T": "If you speak, speak as someone entrusted with God's own words. If you serve, serve with strength God himself supplies — so that everything gives glory to God through Jesus Christ. All glory and all power belong to him, now and forever. Amen."
    },
    "12": {
      "L": "Beloved, do not be surprised at the fiery trial among you, which is coming upon you for your testing, as though something strange were happening to you.",
      "M": "Dear friends, do not be surprised at the fiery ordeal that has come on you to test you, as though something strange were happening to you.",
      "T": "My dear friends, do not be caught off guard when the fire of trial breaks out among you. It has come to test you — and it is not some strange exception to the normal Christian life."
    },
    "13": {
      "L": "But insofar as you share in the sufferings of Christ, rejoice, so that at the revelation of his glory you may also rejoice with exultation.",
      "M": "But rejoice inasmuch as you participate in the sufferings of Christ, so that you may be overjoyed when his glory is revealed.",
      "T": "Instead, rejoice — because you are sharing in the very sufferings of Christ. When his glory is unveiled, your joy will be overwhelming."
    },
    "14": {
      "L": "If you are reproached in the name of Christ, you are blessed, because the Spirit of glory and of God rests upon you.",
      "M": "If you are insulted because of the name of Christ, you are blessed, for the Spirit of glory and of God rests on you.",
      "T": "If you are mocked for carrying the name of Christ — you are blessed. The Spirit of glory, which is God's own Spirit, has settled on you, just as the Spirit rested on the Messiah (Isa 11:2)."
    },
    "15": {
      "L": "But let none of you suffer as a murderer or a thief or an evildoer or as a meddler in other people's affairs.",
      "M": "If you suffer, it should not be as a murderer or thief or any other kind of criminal, or even as a meddler.",
      "T": "Just make sure you are not suffering because of something you actually did wrong — murder, theft, any crime at all, or even just sticking your nose into other people's business."
    },
    "16": {
      "L": "But if as a Christian, let him not be ashamed, but let him glorify God in this name.",
      "M": "However, if you suffer as a Christian, do not be ashamed, but praise God that you bear that name.",
      "T": "But if you suffer for being a Christian — do not let shame touch you. That name is an honor. Let it become a reason to glorify God."
    },
    "17": {
      "L": "For it is time for judgment to begin from the household of God; and if it begins from us first, what will be the end of those who disobey the gospel of God?",
      "M": "For it is time for judgment to begin with God's household; and if it begins with us, what will the outcome be for those who do not obey the gospel of God?",
      "T": "The time of judgment has arrived — and it begins with God's own household. If it starts with us, what outcome awaits those who have turned their backs on God's good news?"
    },
    "18": {
      "L": "And if the righteous are scarcely saved, where will the ungodly and sinner appear?",
      "M": "'And, \"If it is hard for the righteous to be saved, what will become of the ungodly and the sinner?\"'",
      "T": "Proverbs 11:31 says: 'If even the righteous barely make it through, where does that leave the godless and the sinner?'"
    },
    "19": {
      "L": "Therefore let those who suffer according to the will of God commit their souls to a faithful Creator while doing good.",
      "M": "So then, those who suffer according to God's will should commit themselves to their faithful Creator and continue to do good.",
      "T": "So let everyone whom God has placed in a path of suffering entrust their whole life to the God who made them — the one who can be trusted with everything — and keep doing good."
    }
  },
  "5": {
    "1": {
      "L": "Therefore I exhort the elders among you, as a fellow elder and a witness of the sufferings of Christ, and also a partaker of the glory that is about to be revealed:",
      "M": "To the elders among you, I appeal as a fellow elder and a witness of Christ's sufferings who also will share in the glory to be revealed:",
      "T": "To the leaders among you I speak — as one who is a leader alongside you, who witnessed the sufferings of Christ with his own eyes, and who will share in the glory that is coming:"
    },
    "2": {
      "L": "shepherd the flock of God that is among you, exercising oversight not by compulsion but willingly, as God would have it; not for shameful gain but eagerly;",
      "M": "Be shepherds of God's flock that is under your care, watching over them — not because you must, but because you are willing, as God wants you to be; not pursuing dishonest gain, but eager to serve;",
      "T": "Tend God's flock in your charge — not because you feel obligated, but because you genuinely want to, the way God intends. Not for the money, but because you love the work."
    },
    "3": {
      "L": "not domineering over those in your charge, but becoming examples to the flock.",
      "M": "not lording it over those entrusted to you, but being examples to the flock.",
      "T": "Do not throw your weight around over those in your care — be examples they can see and follow."
    },
    "4": {
      "L": "And when the Chief Shepherd is revealed, you will receive the unfading crown of glory.",
      "M": "And when the Chief Shepherd appears, you will receive the crown of glory that will never fade away.",
      "T": "When the Chief Shepherd himself appears, you will be given the crown of glory — not a laurel wreath that yellows and dies, but the kind that lasts forever."
    },
    "5": {
      "L": "Likewise, younger ones, be subject to the elders. And all of you clothe yourselves with humility toward one another, because 'God opposes the proud but gives grace to the humble.'",
      "M": "In the same way, you who are younger, submit yourselves to your elders. All of you, clothe yourselves with humility toward one another, because, 'God opposes the proud but shows favor to the humble.'",
      "T": "Those who are younger — take up a posture of willing service toward your elders. And let every single one of you wear humility like a garment in how you treat each other. For Proverbs 3:34 says: 'God goes to war against the arrogant, but opens his hand to the humble.'"
    },
    "6": {
      "L": "Humble yourselves, therefore, under the mighty hand of God, so that he may exalt you at the proper time,",
      "M": "Humble yourselves, therefore, under God's mighty hand, that he may lift you up in due time.",
      "T": "Bow yourselves down under the powerful hand of God — he will raise you up when the right moment comes."
    },
    "7": {
      "L": "casting all your anxiety upon him, because he cares for you.",
      "M": "Cast all your anxiety on him because he cares for you.",
      "T": "Unload every worry onto him — because he is not indifferent to what happens to you."
    },
    "8": {
      "L": "Be sober, be watchful. Your adversary the devil walks about as a roaring lion seeking someone he may devour.",
      "M": "Be sober-minded and alert. Your enemy the devil prowls around like a roaring lion looking for someone to devour.",
      "T": "Stay sober. Stay alert. Your enemy the devil is circling like a roaring lion, hungry, looking for someone to tear apart."
    },
    "9": {
      "L": "Resist him, being firm in the faith, knowing that the same sufferings are being accomplished in your brotherhood in the world.",
      "M": "Resist him, standing firm in the faith, because you know that the family of believers throughout the world is undergoing the same kind of sufferings.",
      "T": "Stand against him — unmovable in your faith. And know this: your brothers and sisters all over the world are enduring the same struggle."
    },
    "10": {
      "L": "And the God of all grace, who called you to his eternal glory in Christ Jesus, after you have suffered a little while, will himself restore, confirm, strengthen, and establish you.",
      "M": "And the God of all grace, who called you to his eternal glory in Christ, after you have suffered a little while, will himself restore you and make you strong, firm and steadfast.",
      "T": "The God who holds all grace — the one who called you into the life of the coming age through Christ — will, after this brief season of suffering, put you back together himself: make you solid, make you strong, set you on immovable ground."
    },
    "11": {
      "L": "To him be the dominion forever and ever. Amen.",
      "M": "To him be the power for ever and ever. Amen.",
      "T": "All power belongs to him — forever and ever. Amen."
    },
    "12": {
      "L": "Through Silvanus, whom I regard as a faithful brother, I have written to you briefly, exhorting and declaring that this is the true grace of God. Stand firm in it.",
      "M": "With the help of Silas, whom I regard as a faithful brother, I have written to you briefly, encouraging you and testifying that this is the true grace of God. Stand fast in it.",
      "T": "I have written this brief letter through Silvanus, a brother I trust completely — urging you and bearing witness: what you are standing in is the genuine grace of God. Do not step out of it."
    },
    "13": {
      "L": "She who is at Babylon, chosen together with you, sends you greetings, and so does Mark my son.",
      "M": "She who is in Babylon, chosen together with you, sends you her greetings, and so does my son Mark.",
      "T": "The community gathered here in Babylon — Rome, where the power of empire is centered, as both Peter and the book of Revelation call it — sends their greetings. So does Mark, my son in the faith."
    },
    "14": {
      "L": "Greet one another with a kiss of love. Peace to all of you who are in Christ.",
      "M": "Greet one another with a kiss of love. Peace to all of you who are in Christ.",
      "T": "Embrace one another with genuine affection. Peace to all of you who are in Christ."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1peter')
        merge_tier(existing, PETER1, tier_key)
        save(tier_dir, '1peter', existing)
    print('1 Peter 3–5 written.')

if __name__ == '__main__':
    main()
