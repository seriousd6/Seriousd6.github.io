"""
MKT 2 Corinthians chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2corinthians-1-3.py

Translation decisions:
- G2962 (κύριος): "Lord" across all tiers — consistent with all Pauline scripts.
- G5547 (Χριστός): "Christ" in all tiers — Corinthian audience is Greek; "Christ" is functioning
  as a proper name throughout the Pauline corpus.
- G3874 (παράκλησις): "comfort" in L/M; "comfort" or "consolation" in T depending on register.
  The word appears 10× in ch. 1:3–7 alone; Paul's θλῖψις/παράκλησις pairing is the structural
  backbone of the introduction.
- G2347 (θλῖψις): "tribulation" in L; "trouble/distress/affliction" in M; "suffering/trial" in T.
  Semantic range covers affliction, pressure, oppression — rendered contextually across the chapter.
- G3804 (παθήματα): "sufferings" in all tiers — the sufferings-of-Christ motif in 1:5–7.
- G4991 (σωτηρία): "salvation" in L/M/T — the full salvation sense, not merely "deliverance" at 1:6.
- G5485 (χάρις): "grace" in L/M/T except at 1:15 where the context is clearly "benefit/favor"
  (a visit-gift from Paul) — rendered "grace" in L (word-for-word), "benefit" in M/T.
- G4102 (πίστις): "faith" in L/M (1:24); "trust" in T — the Reformation debate on subjective faith
  vs. objective faithfulness does not apply in this context; πίστις here = the Corinthians' own
  believing stance.
- G4151 (πνεῦμα): "Spirit" (capitalized) whenever clearly the Holy Spirit (1:22; 3:3, 6, 8, 17, 18).
  Lowercase "spirit" at 2:13 (Paul's human spirit, "no rest in my spirit").
- G3056 (λόγος): "word" in all tiers at 2:17 — God's word as proclaimed message.
- G1577 (ἐκκλησία): "church" in all tiers — consistent with all other Pauline scripts.
- G1242 (διαθήκη): "covenant" in all tiers (3:6, 14) — NOT "testament." The new covenant/old
  covenant contrast is the explicit topic of ch. 3; "covenant" is exegetically required.
- G1121 (γράμμα): "letter/written code" in L; "written code/letter" in M; "written code" in T
  at 3:6. The contrast is between the external written law (which kills) and the Spirit (who gives life).
  "Letter" alone can be misread as an epistle; "written code" in M/T makes the contrast explicit.
- G1391 (δόξα): "glory" in all tiers throughout ch. 3 — central term; no deviation.
- G1248 (διακονία): "ministry/ministration" — L uses "ministration" (more literal); M/T use "ministry."
- G3954 (παρρησία): "plainness of speech" in L; "boldness" in M; "freedom and openness" in T (3:12).
- G1657 (ἐλευθερία): "liberty" in L; "freedom" in M/T (3:17).
- G2358 (θριαμβεύω): "causeth to triumph" in L; "leads in triumphal procession" in M/T (2:14).
  The Greek image is the Roman triumph, where conquered captives are paraded behind the general.
  Paul is the captive-trophy of Christ, not the triumphant general — M/T surfaces this nuance.
- G2175 (εὐωδία): "sweet savour" in L; "pleasing aroma" in M; "fragrance" in T — the incense
  language of 2:14–16 echoes OT sacrificial worship. The aroma-of-Christ metaphor is preserved
  consistently.
- G1343 (δικαιοσύνη): "righteousness" in L; "righteousness" in M; "righteousness" / "declares
  righteous" in T at 3:9 — the forensic ministry-of-righteousness contrasted with ministry-of-condemnation.
- G572 (ἁπλότης): "simplicity" in L; "integrity" in M; "transparent honesty" in T (1:12) —
  the word means singleness, openness, absence of double-dealing.
- G2734 (κατοπτρίζω): "beholding as in a glass" in L; "contemplate" in M; "gazing on… as in a mirror"
  in T (3:18) — the mirror image: we behold the Lord's glory and are transformed into it.
- 3:3 OT echo: "not on tablets of stone but on tablets of human hearts" — explicit echo of
  Jeremiah 31:33 and Ezekiel 36:26 (new covenant promise). T surfaces this but without parenthetical.
- 2:14 triumphal procession: Paul images God as the Roman general leading Christ-followers as
  captive-trophies. The fragrance of incense hung over both the victorious procession and pagan
  sacrifices — the double edge in 2:15–16 (life/death) is intentional.
- Aspect: 1:9 aorist "we had the sentence of death" = completed act; 3:18 present passive
  "are being transformed" = ongoing process rendered as English present continuous.
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

CORINTHIANS_2 = {
  "1": {
    "1": {
      "L": "Paul, an apostle of Christ Jesus by the will of God, and Timothy our brother, to the church of God at Corinth, with all the saints in all Achaia:",
      "M": "Paul, an apostle of Christ Jesus by the will of God, and Timothy our brother, to the church of God in Corinth, together with all the saints throughout Achaia.",
      "T": "From Paul, apostle of Christ Jesus by God's own appointment, and from our brother Timothy. To the congregation of God at Corinth — and to all God's people throughout Achaia."
    },
    "2": {
      "L": "Grace to you and peace from God our Father and the Lord Jesus Christ.",
      "M": "Grace and peace to you from God our Father and the Lord Jesus Christ.",
      "T": "May God our Father and the Lord Jesus Christ give you grace and peace."
    },
    "3": {
      "L": "Blessed be the God and Father of our Lord Jesus Christ, the Father of mercies and God of all comfort,",
      "M": "Praise be to the God and Father of our Lord Jesus Christ, the Father of compassion and the God of all comfort,",
      "T": "All praise to the God and Father of our Lord Jesus Christ. He is the Father of compassion and the source of every comfort —"
    },
    "4": {
      "L": "who comforteth us in all our tribulation, that we may be able to comfort them which are in any tribulation, through the comfort wherewith we ourselves are comforted of God.",
      "M": "who comforts us in all our troubles, so that we can comfort those in any trouble with the comfort we ourselves receive from God.",
      "T": "who comforts us in every suffering we face, so that we in turn can bring to others the same comfort God has poured into us."
    },
    "5": {
      "L": "For as the sufferings of Christ abound in us, so our consolation also aboundeth through Christ.",
      "M": "For just as the sufferings of Christ overflow into our lives, so also through Christ our comfort overflows.",
      "T": "We share abundantly in Christ's sufferings — and in exactly that measure, God's comfort flows to us through Christ."
    },
    "6": {
      "L": "And whether we be afflicted, it is for your comfort and salvation; or whether we be comforted, it is for your comfort, which is effectual in the enduring of the same sufferings which we also suffer.",
      "M": "If we are distressed, it is for your comfort and salvation; if we are comforted, it is for your comfort, which produces in you patient endurance of the same sufferings we ourselves suffer.",
      "T": "When we endure suffering, it is for your comfort and salvation. When we receive comfort, it is for your comfort too — comfort that equips you to endure patiently the same trials we face."
    },
    "7": {
      "L": "And our hope of you is stedfast, knowing that as ye are partakers of the sufferings, so shall ye be also of the consolation.",
      "M": "And our hope for you is firm, because we know that just as you share in our sufferings, so also you share in our comfort.",
      "T": "Our hope for you stands firm: because you share our sufferings, you will equally share our comfort."
    },
    "8": {
      "L": "For we would not, brethren, have you ignorant of our trouble which came to us in Asia, that we were pressed out of measure, above strength, insomuch that we despaired even of life:",
      "M": "We do not want you to be unaware, brothers and sisters, of the hardship we experienced in the province of Asia. We were under great pressure, far beyond our ability to endure, so that we despaired of life itself.",
      "T": "We want you to know about the crushing ordeal we went through in Asia. We were overwhelmed beyond all bearing — the pressure so severe that we gave up hope of surviving."
    },
    "9": {
      "L": "But we had the sentence of death in ourselves, that we should not trust in ourselves, but in God which raiseth the dead:",
      "M": "Indeed, in our own hearts we felt the sentence of death. But this happened that we might not rely on ourselves but on God, who raises the dead.",
      "T": "We felt the death sentence in our own hearts — and that was precisely the point. God was stripping us of all self-reliance, teaching us to trust in him alone: the God who raises the dead."
    },
    "10": {
      "L": "Who delivered us from so great a death, and doth deliver: in whom we trust that he will yet deliver us;",
      "M": "He has delivered us from such a deadly peril, and he will deliver us again. On him we have fixed our hope that he will continue to deliver us.",
      "T": "He rescued us from that mortal danger, and he delivers us still. We have placed our hope in him, and he will go on rescuing us."
    },
    "11": {
      "L": "Ye also helping together by prayer for us, that for the gift bestowed upon us by means of many persons, thanks may be given by many on our behalf.",
      "M": "as you help us by your prayers. Then many will give thanks on our behalf for the gracious favor granted us in answer to the prayers of many.",
      "T": "You play your part by praying for us. Then when God grants us the gift, many people will offer him thanks — all because so many prayed."
    },
    "12": {
      "L": "For our rejoicing is this, the testimony of our conscience, that in simplicity and godly sincerity, not with fleshly wisdom, but by the grace of God, we have had our conversation in the world, and more abundantly to you-ward.",
      "M": "Now this is our boast: our conscience testifies that we have conducted ourselves in the world, and especially in our relations with you, with integrity and godly sincerity — not with worldly wisdom but by the grace of God.",
      "T": "Here is what we are proud of: our conscience bears witness that we have lived in the world — and especially in our dealings with you — with transparent honesty that comes from God. We have not relied on human cleverness; we have relied on God's grace."
    },
    "13": {
      "L": "For we write none other things unto you, than what ye read or acknowledge; and I trust ye shall acknowledge even to the end;",
      "M": "For we are not writing you anything you cannot read or understand. And I hope that,",
      "T": "Everything we have written to you is straightforward — nothing hidden, nothing between the lines. And I hope that,"
    },
    "14": {
      "L": "As also ye have acknowledged us in part, that we are your rejoicing, even as ye also are ours in the day of the Lord Jesus.",
      "M": "just as you have understood us in part, you will come to understand fully that you can boast of us just as we will boast of you in the day of the Lord Jesus.",
      "T": "just as you have partly come to understand us, you will one day understand us fully — that on the day of the Lord Jesus we can take pride in you, and you in us."
    },
    "15": {
      "L": "And in this confidence I was minded to come unto you before, that ye might have a second benefit;",
      "M": "Because I was confident of this, I planned to visit you first so that you could benefit twice.",
      "T": "It was this confidence that made me plan to visit you first — I wanted you to receive a double gift of grace."
    },
    "16": {
      "L": "And to pass by you into Macedonia, and to come again out of Macedonia unto you, and of you to be brought on my way toward Judaea.",
      "M": "I planned to visit you on my way to Macedonia and again on my return from Macedonia, so that you could send me on my way to Judea.",
      "T": "My plan was to stop with you on the way to Macedonia, come back through you on the return, and then have you send me on to Judea — two visits instead of one."
    },
    "17": {
      "L": "When I therefore was thus minded, did I use lightness? or the things that I purpose, do I purpose according to the flesh, that with me there should be yea yea, and nay nay?",
      "M": "Was I fickle when I made this plan? Or do I make plans in a worldly manner so that in the same breath I say both 'Yes, yes' and 'No, no'?",
      "T": "Does this change of plan make me a waverer — someone who can't be trusted to mean what he says? Do I operate by purely human calculation, saying yes and no in the same breath?"
    },
    "18": {
      "L": "But as God is faithful, our word toward you was not yea and nay.",
      "M": "But as surely as God is faithful, our message to you is not 'Yes' and 'No.'",
      "T": "I call God himself to witness: what we have spoken to you has never been a mixture of yes and no."
    },
    "19": {
      "L": "For the Son of God, Jesus Christ, who was preached among you by us, even by me and Silvanus and Timotheus, was not yea and nay, but in him was yea.",
      "M": "For the Son of God, Jesus Christ, who was proclaimed among you by me and Silvanus and Timothy, was not 'Yes and No.' In him it has always been 'Yes.'",
      "T": "The Son of God, Jesus Christ — whom Silvanus, Timothy, and I proclaimed to you — was never a mixture of yes and no. In him, there is only Yes."
    },
    "20": {
      "L": "For all the promises of God in him are yea, and in him Amen, unto the glory of God by us.",
      "M": "For no matter how many promises God has made, they are 'Yes' in Christ. And so through him the 'Amen' is spoken by us to the glory of God.",
      "T": "Every promise God ever made finds its fulfillment in Christ — every last one is Yes. And so it is through Christ that we say Amen to God, to his glory."
    },
    "21": {
      "L": "Now he which stablisheth us with you in Christ, and hath anointed us, is God;",
      "M": "Now it is God who makes both us and you stand firm in Christ. He anointed us,",
      "T": "It is God himself who has made us firm together with you in Christ. He anointed us —"
    },
    "22": {
      "L": "Who hath also sealed us, and given the earnest of the Spirit in our hearts.",
      "M": "set his seal of ownership on us, and put his Spirit in our hearts as a deposit, guaranteeing what is to come.",
      "T": "stamped his ownership on us and planted his Spirit in our hearts as the down payment on all he has promised."
    },
    "23": {
      "L": "Moreover I call God for a record upon my soul, that to spare you I came not as yet unto Corinth.",
      "M": "I call God as my witness — and may he judge me if I am lying — that it was in order to spare you that I did not return to Corinth.",
      "T": "God is my witness — I put my very soul on the line: the reason I have not yet come back to Corinth is to spare you grief."
    },
    "24": {
      "L": "Not for that we have dominion over your faith, but are helpers of your joy: for by faith ye stand.",
      "M": "Not that we lord it over your faith, but we work with you for your joy, because it is by faith you stand firm.",
      "T": "This is not about us ruling your faith — that is not our authority. We are partners in your joy. After all, you already stand firm in your faith."
    }
  },
  "2": {
    "1": {
      "L": "But I determined this with myself, that I would not come again to you in heaviness.",
      "M": "So I made up my mind that I would not make another painful visit to you.",
      "T": "I made a firm decision: I was not going to pay you another grief-laden visit."
    },
    "2": {
      "L": "For if I make you sorry, who is he then that maketh me glad, but the same which is made sorry by me?",
      "M": "For if I grieve you, who is left to make me glad but you whom I have grieved?",
      "T": "Think about it: if I make you sad, who will cheer me up? Only the very people I have made sad."
    },
    "3": {
      "L": "And I wrote this same thing unto you, lest, when I came, I should have sorrow from them of whom I ought to rejoice; having confidence in you all, that my joy is the joy of you all.",
      "M": "So I wrote that letter so that when I came I would not be distressed by those who should have made me glad. I was confident about all of you — that you would all share my joy.",
      "T": "That is why I wrote instead of visiting: I did not want to arrive and be grieved by the very people who ought to fill me with joy. I was — and still am — convinced that when I rejoice, you all rejoice with me."
    },
    "4": {
      "L": "For out of much affliction and anguish of heart I wrote unto you with many tears; not that ye should be grieved, but that ye might know the love which I have more abundantly unto you.",
      "M": "For I wrote to you out of great distress and anguish of heart, with many tears — not to grieve you, but to let you know how deeply I love you.",
      "T": "When I wrote that letter, I was in great anguish of heart — tears came with every word. My aim was not to hurt you; I wrote so that you would understand the depth of love I have for you."
    },
    "5": {
      "L": "But if any have caused grief, he hath not grieved me, but in part: that I may not overcharge you all.",
      "M": "If anyone has caused grief, he has not so much grieved me as he has grieved all of you — to some extent, not to exaggerate.",
      "T": "The person who caused the hurt did not really hurt me alone — in some degree he hurt all of you. I say 'in some degree' so as not to lay it on too thick."
    },
    "6": {
      "L": "Sufficient to such a man is this punishment, which was inflicted of many.",
      "M": "The punishment inflicted on him by the majority is sufficient.",
      "T": "The censure the community imposed on that person is punishment enough."
    },
    "7": {
      "L": "So that contrariwise ye ought rather to forgive him, and comfort him, lest perhaps such a one should be swallowed up with overmuch sorrow.",
      "M": "Now instead, you ought to forgive and comfort him, so that he will not be overwhelmed by excessive sorrow.",
      "T": "It is time to reverse course: forgive him, welcome him back, encourage him — or excessive grief may swallow him whole."
    },
    "8": {
      "L": "Wherefore I beseech you that ye would confirm your love toward him.",
      "M": "I urge you, therefore, to reaffirm your love for him.",
      "T": "I am urging you: make it unmistakably clear to him that you love him."
    },
    "9": {
      "L": "For to this end also did I write, that I might know the proof of you, whether ye be obedient in all things.",
      "M": "Another reason I wrote was to see if you would stand the test and be obedient in everything.",
      "T": "This was also part of my purpose in writing: I wanted to see whether you would rise to the test — whether you are truly obedient in everything."
    },
    "10": {
      "L": "To whom ye forgive any thing, I forgive also: for if I forgave any thing, to whom I forgave it, for your sakes forgave I it in the person of Christ;",
      "M": "Anyone you forgive, I also forgive. And what I have forgiven — if there was anything to forgive — I have forgiven for your sake, in the presence of Christ.",
      "T": "Whatever you forgive, I forgive too. And where I have forgiven anything, I did it for your sake, in the sight of Christ himself."
    },
    "11": {
      "L": "Lest Satan should get an advantage of us: for we are not ignorant of his devices.",
      "M": "so that Satan might not outwit us. For we are not unaware of his schemes.",
      "T": "We must not give Satan an opening — we know how he operates."
    },
    "12": {
      "L": "Furthermore, when I came to Troas to preach Christ's gospel, and a door was opened unto me of the Lord,",
      "M": "Now when I went to Troas to preach the gospel of Christ and found that the Lord had opened a door for me,",
      "T": "When I arrived in Troas to preach the gospel of Christ, the Lord had set wide open a door of opportunity —"
    },
    "13": {
      "L": "I had no rest in my spirit, because I found not Titus my brother: but taking my leave of them, I went from thence into Macedonia.",
      "M": "I still had no peace of mind, because I did not find my brother Titus there. So I said goodbye to them and went on to Macedonia.",
      "T": "but I had no peace of mind, because Titus my brother was not there. So I took my leave and pressed on to Macedonia."
    },
    "14": {
      "L": "Now thanks be unto God, which always causeth us to triumph in Christ, and maketh manifest the savour of his knowledge by us in every place.",
      "M": "But thanks be to God, who always leads us in Christ's triumphal procession and uses us to spread the aroma of the knowledge of him everywhere.",
      "T": "Praise to God! He continually leads us forward as trophies in Christ's victory procession, and through us he spreads everywhere the fragrance of the knowledge of Christ — like incense filling every room."
    },
    "15": {
      "L": "For we are unto God a sweet savour of Christ, in them that are saved, and in them that perish:",
      "M": "For we are to God the pleasing aroma of Christ among those who are being saved and those who are perishing.",
      "T": "We are to God the very fragrance of Christ — whether those who encounter us are on the path to life or the path to death."
    },
    "16": {
      "L": "To the one we are the savour of death unto death; and to the other the savour of life unto life. And who is sufficient for these things?",
      "M": "To the one we are an aroma that brings death; to the other, an aroma that brings life. And who is equal to such a task?",
      "T": "For those who are perishing, we carry the smell of death leading to death; for those being saved, the smell of life leading to life. And who on earth is adequate for such a mission?"
    },
    "17": {
      "L": "For we are not as many, which corrupt the word of God: but as of sincerity, but as of God, in the sight of God speak we in Christ.",
      "M": "Unlike so many, we do not peddle the word of God for profit. On the contrary, in Christ we speak before God with sincerity, as those sent from God.",
      "T": "We are not like the many who hawk God's word for personal gain. We are people of integrity, commissioned by God, speaking in Christ's name with God himself as our witness."
    }
  },
  "3": {
    "1": {
      "L": "Do we begin again to commend ourselves? or need we, as some others, epistles of commendation to you, or letters of commendation from you?",
      "M": "Are we beginning to commend ourselves again? Or do we need, like some people, letters of recommendation to you or from you?",
      "T": "Are we starting all over to put ourselves forward? Do we need — as some apparently do — commendation letters to bring to you, or letters from you to carry elsewhere?"
    },
    "2": {
      "L": "Ye are our epistle written in our hearts, known and read of all men:",
      "M": "You yourselves are our letter, written on our hearts, known and read by everyone.",
      "T": "You are our letter — inscribed on our hearts, visible to everyone, open for all the world to read."
    },
    "3": {
      "L": "Forasmuch as ye are manifestly declared to be the epistle of Christ ministered by us, written not with ink, but with the Spirit of the living God; not in tables of stone, but in fleshy tables of the heart.",
      "M": "You show that you are a letter from Christ, the result of our ministry, written not with ink but with the Spirit of the living God, not on tablets of stone but on tablets of human hearts.",
      "T": "You are a letter written by Christ himself — delivered through our hands, penned not with ink but by the Spirit of the living God, inscribed not on stone tablets but on the living tablets of the human heart."
    },
    "4": {
      "L": "And such trust have we through Christ to God-ward:",
      "M": "Such is the confidence we have through Christ before God.",
      "T": "This is the confidence we have — and it flows entirely through Christ, toward God."
    },
    "5": {
      "L": "Not that we are sufficient of ourselves to think any thing as of ourselves; but our sufficiency is of God;",
      "M": "Not that we are competent in ourselves to claim anything for ourselves, but our competence comes from God.",
      "T": "It is not that we are in any way adequate on our own — we cannot even have a useful thought that originates in ourselves. Our adequacy is entirely God's gift."
    },
    "6": {
      "L": "Who also hath made us able ministers of the new testament; not of the letter, but of the spirit: for the letter killeth, but the spirit giveth life.",
      "M": "He has made us competent as ministers of a new covenant — not of the written code but of the Spirit; for the written code kills, but the Spirit gives life.",
      "T": "He has fitted us to serve the new covenant — not the written code, but the Spirit. For the written code executes; the Spirit makes alive."
    },
    "7": {
      "L": "But if the ministration of death, written and engraven in stones, was glorious, so that the children of Israel could not stedfastly behold the face of Moses for the glory of his countenance; which glory was to be done away:",
      "M": "Now if the ministry that brought death, which was engraved in letters on stone, came with glory, so that the Israelites could not look steadily at the face of Moses because of its glory, transient though it was,",
      "T": "Consider: the ministry inscribed on stone — the very ministry that brought death — was launched in such blazing glory that the Israelites could not look Moses in the face. And that glory was already fading."
    },
    "8": {
      "L": "How shall not the ministration of the spirit be rather glorious?",
      "M": "will not the ministry of the Spirit be even more glorious?",
      "T": "How much more glorious, then, must be the ministry of the Spirit!"
    },
    "9": {
      "L": "For if the ministration of condemnation be glory, much more doth the ministration of righteousness exceed in glory.",
      "M": "If the ministry that brought condemnation was glorious, how much more glorious is the ministry that brings righteousness!",
      "T": "If the ministry that condemned people was launched in glory, the ministry that declares people righteous surpasses it in glory beyond measure."
    },
    "10": {
      "L": "For even that which was made glorious had no glory in this respect, by reason of the glory that excelleth.",
      "M": "For what was glorious has no glory now in comparison with the surpassing glory.",
      "T": "In fact, what was once glorious has lost all appearance of glory — completely eclipsed by a glory so overwhelming that it reduces the former to nothing."
    },
    "11": {
      "L": "For if that which is done away was glorious, much more that which remaineth is glorious.",
      "M": "And if what was transient came with glory, how much greater is the glory of what is permanent!",
      "T": "If what was temporary came wrapped in glory, the permanent surpasses it in glory beyond all comparison."
    },
    "12": {
      "L": "Seeing then that we have such hope, we use great plainness of speech:",
      "M": "Therefore, since we have such a hope, we are very bold.",
      "T": "Because we hold this hope, we speak with great freedom and openness."
    },
    "13": {
      "L": "And not as Moses, which put a vail over his face, that the children of Israel could not stedfastly look to the end of that which is abolished:",
      "M": "We are not like Moses, who would put a veil over his face to prevent the Israelites from seeing the end of what was passing away.",
      "T": "We are nothing like Moses, who hid his face behind a veil so that Israel could not watch the fading glory reach its end."
    },
    "14": {
      "L": "But their minds were blinded: for until this day remaineth the same vail untaken away in the reading of the old testament; which vail is done away in Christ.",
      "M": "But their minds were made dull, for to this day the same veil remains when the old covenant is read. It has not been removed, because only in Christ is it taken away.",
      "T": "But their minds were hardened — calcified. To this very day, when they read the old covenant, that veil lies there unlifted. Only in Christ does it fall away."
    },
    "15": {
      "L": "But even unto this day, when Moses is read, the vail is upon their heart.",
      "M": "Even to this day when Moses is read, a veil covers their hearts.",
      "T": "Even now, every time Moses is read aloud, a veil lies over their hearts."
    },
    "16": {
      "L": "Nevertheless when it shall turn to the Lord, the vail shall be taken away.",
      "M": "But whenever anyone turns to the Lord, the veil is taken away.",
      "T": "But the moment someone turns to the Lord, the veil lifts."
    },
    "17": {
      "L": "Now the Lord is that Spirit: and where the Spirit of the Lord is, there is liberty.",
      "M": "Now the Lord is the Spirit, and where the Spirit of the Lord is, there is freedom.",
      "T": "The Lord — the one you turn to — is the Spirit. And wherever the Spirit of the Lord is present, there is freedom."
    },
    "18": {
      "L": "But we all, with open face beholding as in a glass the glory of the Lord, are changed into the same image from glory to glory, even as by the Spirit of the Lord.",
      "M": "And we all, who with unveiled faces contemplate the Lord's glory, are being transformed into his image with ever-increasing glory, which comes from the Lord, who is the Spirit.",
      "T": "And all of us — with unveiled faces — are gazing on the Lord's glory as in a mirror, and we are being transformed from one degree of glory to the next into that same image. This is the work of the Lord, who is the Spirit."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2corinthians')
        merge_tier(existing, CORINTHIANS_2, tier_key)
        save(tier_dir, '2corinthians', existing)
    print('2 Corinthians 1–3 written.')

if __name__ == '__main__':
    main()
