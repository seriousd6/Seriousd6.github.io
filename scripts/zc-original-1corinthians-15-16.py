"""
mkt-original layer — 1 Corinthians chapters 15–16
Output: data/commentary/mkt-original/1corinthians.json
Run: python3 scripts/zc-original-1corinthians-15-16.py
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
    # INTENT: Merge new verse entries without overwriting already-present keys — safe to re-run.
    # CHANGE? If commentary JSON structure changes from {ch:{v:html}}, update this traversal.
    # VERIFY: Re-running the script should produce identical output.
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

NEW = {
  "15": {
    "1": "Paul makes known (gnōrizō) the gospel (euangelion) he preached — the present tense indicates an ongoing announcement, not a completed past event. He frames chapter 15 as a reminder of what they already received and on which they stand.",
    "2": "Through the gospel they are being saved (sōzesthe, present passive) — salvation is a process in motion, not merely a past event. The conditional unless you believed in vain (eikē) introduces the stakes: misbelief about resurrection nullifies the whole.",
    "4": "That he was buried and that he was raised on the third day in accordance with the scriptures (kata tas graphas) — the burial confirms the reality of death; the resurrection is scripture-fulfillment, though Paul does not name which texts. The passive ēgertai (was raised) emphasizes divine action throughout.",
    "5": "He appeared (ōphthē, aorist passive, he was seen) to Cephas, then to the Twelve — the verb ōphthē is the standard LXX verb for divine appearances (theophanies); Paul uses it consistently for all the resurrection appearances listed here.",
    "6": "He appeared to more than five hundred brothers at one time, most of whom are still alive, though some have fallen asleep — Paul signals that witnesses can be interviewed; this is not pious tradition but verifiable testimony.",
    "7": "He appeared to James, then to all the apostles — James the Lord's brother, who was not among the Twelve but became a pillar of the Jerusalem church (Gal 1:19; 2:9); his conversion is traceable to this appearance.",
    "8": "Last of all, as to one untimely born (ektrōmati, a miscarriage or aborted fetus), he appeared also to Paul — the word ektroma conveys abnormality and premature or violent birth; Paul uses it of his own out-of-sequence call, acknowledging that he was not a disciple during Jesus's ministry.",
    "9": "Paul is the least of the apostles, not worthy to be called an apostle, because he persecuted the church of God — the verb ediōxa (I persecuted) is imperfect, ongoing past action; Paul never lets himself forget the violence of his pre-conversion life.",
    "10": "By the grace of God I am what I am — one of Paul's most direct statements of identity. The charis (grace) of God was not in vain (kene); Paul labored more abundantly than all the apostles, yet insists it was not himself but the grace of God working with him.",
    "11": "Whether then it was I or they, so we preach and so you believed — the kerygma is identical across all the apostolic witnesses; the content, not the messenger, is the fixed point.",
    "12": "Now if Christ is proclaimed as raised from the dead, how can some among you say there is no resurrection of the dead? — the rhetorical question identifies the logical contradiction: the Corinthians affirm Christ's resurrection while denying the general resurrection, though the two stand or fall together.",
    "13": "If there is no resurrection of the dead, then Christ has not been raised — the argument moves by strict logical inference; the denial of the category (resurrection of the dead) eliminates the particular instance (Christ's resurrection).",
    "14": "And if Christ has not been raised, then our proclamation is empty (kenon) and your faith is empty (kenē) — both kenon (preaching) and kenē (faith) echo the word Paul used in v.10 (the grace that was not in vain/kene); if the resurrection is false, everything becomes kenon.",
    "15": "We are found to be false witnesses about God because we testified about God that he raised Christ — the word pseudomartyres (false witnesses) is the same category as the Ninth Commandment violation; to preach a resurrection that did not happen makes the apostles liars about God.",
    "16": "For if the dead are not raised, not even Christ has been raised — the argument repeats for emphasis; the logical entailment must be stated twice to make clear that there is no escape hatch.",
    "17": "And if Christ has not been raised, your faith is futile (mataia) and you are still in your sins — mataia (empty, futile) is a stronger word than kene; it means utterly without result. Without resurrection, the atonement is incomplete.",
    "18": "Then also those who have fallen asleep in Christ have perished (apōlonto) — the aorist of apollymi (to destroy, to perish); this is not a gentle word. If there is no resurrection, the Christian dead are simply gone.",
    "19": "If we have hoped in Christ only for this life, we are of all people most to be pitied (eleenoteroi) — the superlative adjective; apostolic suffering (v.30-32) makes no sense without resurrection. Hope that ends at death makes Christians the most pathetic of all people.",
    "21": "For as by a man came death, by a man has also come the resurrection of the dead — the Adam/Christ parallelism that Paul develops more fully in Romans 5:12-21 is here introduced through the category of manhood: a human brought death; a human has also brought resurrection.",
    "22": "For as in Adam all die, so also in Christ shall all be made alive — the two spheres: en tō Adam (in Adam) and en tō Christō (in Christ); membership in these two figures determines one's eschatological destiny. The all in each case is governed by the respective union.",
    "23": "But each in his own order (tagmati) — tagma is a military term for a battalion or rank; Paul imagines the resurrection as a military procession. Christ the firstfruits (aparche), then at his coming (parousia) those who belong to Christ.",
    "24": "Then comes the end, when he delivers the kingdom to God the Father after destroying every rule and every authority and power — the sequence: resurrection, then the eschatological defeat of hostile powers, then the handing over of the kingdom. The verb katargein (destroy, render inoperative) will recur in v.26.",
    "25": "For he must reign until he has put all his enemies under his feet — citing Psalm 110:1, the most-quoted OT text in the NT. The dei (must) indicates divine necessity rooted in the Psalm's promise; Christ's reign is purposively aimed at the defeat of every hostile power.",
    "26": "The last enemy to be destroyed (katargeitai) is death — death is personified as a power, the final adversary; the verb katargeitai (present passive, is being destroyed, will be destroyed) is the same word used for all the hostile powers in v.24.",
    "27": "For God has put all things in subjection under his feet — citing Psalm 8:6; the human figure of Psalm 8 (what is man?) receives dominion over all creation. Paul reads this as eschatologically fulfilled in Christ. But when it says all things are put in subjection, it is plain that he is excepted who put all things in subjection under him.",
    "28": "When all things are subjected to him, then the Son himself will also be subjected to him who put all things in subjection under him, so that God may be all in all — the telos (end) of the entire redemptive sequence: the Son's subjection to the Father is not subordination of being but the completion of the mission; God becomes ta panta en pasin (all things in all).",
    "29": "Otherwise what do people mean by being baptized for (or on behalf of) the dead? — baptism hyper tōn nekrōn is a notorious crux; Paul does not endorse or explain the practice but uses it as an argument ad hominem: if there is no resurrection, why are some of you doing this?",
    "30": "Why are we in danger every hour? — Paul's first-person argument from experience; his constant peril makes no sense if there is no resurrection.",
    "31": "I die every day — Paul's self-description of daily apostolic risk; the hyperbolic claim that he dies daily is grounded in the constant threat of martyrdom.",
    "32": "If from human motives I fought with beasts at Ephesus, what do I gain? If the dead are not raised, let us eat and drink for tomorrow we die — citing Isaiah 22:13; the Epicurean pleasure-principle becomes the only rational response if resurrection is false. Paul may refer to a real or metaphorical beast-fight at Ephesus.",
    "33": "Do not be deceived: bad company ruins good morals — Paul cites a well-known line from Menander's comedy Thais (phtheirousin ethe chresta homiliai kakai); the Corinthians' association with those who deny resurrection is corrupting their character.",
    "34": "Wake up from your drunken stupor (eknepsate) as you ought and do not go on sinning — the verb eknephō (sober up, become sane again) implies intoxication of thought; some at Corinth have no knowledge (agnosian) of God, which Paul says to their shame.",
    "35": "But someone will ask, how are the dead raised? With what kind of body do they come? — Paul shifts to the second question, which he treats as foolish (aphrōn): not the fact of resurrection but its mode.",
    "36": "You foolish person (aphrōn) — what you sow does not come to life unless it dies — the agricultural analogy: the seed must die before it can become a plant. The continuity between seed and plant is real but the form is transformed.",
    "37": "And what you sow is not the body that is to be, but a bare kernel, perhaps of wheat or some other grain — the seed is the material continuity; the body that emerges is the transformed form. Paul does not specify the relation precisely but insists there is both continuity and transformation.",
    "38": "But God gives it a body as he has chosen, and to each kind of seed its own body — the diversity of bodies is God's design; there is no single form of embodied existence.",
    "39": "Not all flesh is the same flesh — sarx (flesh): human, animal, bird, fish each have different sarx. The word sarx does not mean body in general; it specifies material constitution.",
    "40": "There are heavenly bodies and earthly bodies, but the glory of the heavenly is of one kind and the glory of the earthly is of another — sōmata epourania (heavenly bodies, i.e. stars) and sōmata epigeia (earthly bodies, i.e. living creatures). Each kind of body has its own doxa (glory, radiance).",
    "41": "There is one glory of the sun, and another glory of the moon, and another glory of the stars; for star differs from star in glory — the differentiation of glory within a single category (stars) supports the idea that the resurrection body will be glorious yet differentiated from the present body.",
    "42": "So is it with the resurrection of the dead — the analogy is applied. What is sown in perishability (phthora), raised in imperishability (aphtharsia); the four contrasts in vv. 42-44 are all passive participles: it is sown... it is raised...",
    "43": "Sown in dishonor (atimia), raised in glory (doxa); sown in weakness (astheneia), raised in power (dynamis) — the four pairs map the transformation: mortal weakness and dishonor are transformed into glory and power.",
    "44": "Sown a natural body (sōma psychikon), raised a spiritual body (sōma pneumatikon) — psychikon does not mean soulless or non-spiritual in a modern sense; it means animated by the psyche (natural life-principle). Pneumatikon means animated by the pneuma (Spirit of God); the resurrection body is fully animated by divine Spirit.",
    "45": "So it is written: the first man Adam became a living soul (psychen zōsan) — citing Genesis 2:7 (LXX); the last Adam became a life-giving spirit (pneuma zōopoioun). The contrast is between receiving life (psychen zōsan) and giving life (zōopoioun); the risen Christ is the source and agent of resurrection life.",
    "46": "But it is not the spiritual that is first but the natural and then the spiritual — the sequence matters: the psychikon precedes the pneumatikon in human experience. The order of the ages follows: present age (psychikon), then the age to come (pneumatikon).",
    "47": "The first man is from the earth, made of dust (choikos); the second man is from heaven — choikos (earthy, made of earth-stuff) echoes Genesis 2:7 (dust/aphar); the second man is from heaven (ex ouranou), indicating Christ's origin and the nature of the resurrection body.",
    "48": "As was the man of dust, so also are those who are of the dust; and as is the man of heaven, so also are those who are of heaven — the two humanities: earthy humanity descended from Adam, heavenly humanity participating in Christ's risen nature.",
    "49": "Just as we have borne the image of the man of dust, we shall also bear the image of the man of heaven — eikōn (image) carries the weight of Genesis 1:26-27; those who now bear Adam's image will bear Christ's image. Some manuscripts read the hortatory subjunctive (let us also bear) rather than the future indicative.",
    "50": "Flesh and blood (sarx kai haima) cannot inherit the kingdom of God, nor does the perishable inherit the imperishable — the rhetorical climax; the present bodily constitution is incapable of inheriting the coming order. Transformation, not mere resuscitation, is required.",
    "51": "Behold, I tell you a mystery (mystērion) — Paul introduces a previously unrevealed truth. We will not all sleep (die), but we will all be changed (allagesometha) — the mystery is the fate of those alive at the parousia: they will be transformed rather than dying and rising.",
    "52": "In a moment, in the twinkling of an eye (en atomō, en rhipē ophthalmou), at the last trumpet — atomos (indivisible moment) and rhipe ophthalmou (flash of an eye) are Greek expressions for the fastest conceivable instant. The last trumpet signals eschatological completion.",
    "53": "For this perishable body must put on the imperishable, and this mortal body must put on immortality — ependysasthai (put on, clothe oneself with) as one puts on a garment; the imagery is of clothing the mortal with the divine attribute of athanasia (immortality).",
    "54": "When the perishable puts on the imperishable, and the mortal puts on immortality, then shall come to pass the saying that is written: Death is swallowed up in victory — citing Isaiah 25:8 (LXX: death swallowed up in victory / katepothē ho thanatos eis nikos). The verb katapinō (swallow up, devour) reverses the image of death as a devourer.",
    "56": "The sting of death is sin, and the power of sin is the law — a parenthetical theological statement that answers why death had such power: sin gives death its sting (kentron, the point of a weapon or sting of an insect), and the law gives sin its power by defining and amplifying transgression (Rom 5:20; 7:7-11).",
    "57": "But thanks be to God (tō de theō charis) who gives us the victory through our Lord Jesus Christ — the doxological eruption that follows the citation of Isaiah 25:8; the victory is gift (charis, grace), not achievement.",
    "58": "Therefore, my beloved brothers, be steadfast (hedraioi), immovable (ametakinetoi), always abounding in the work of the Lord, knowing that in the Lord your labor is not in vain (kenon) — kenon (empty/vain) from v.14 returns: the labor that would have been empty if resurrection were false is now full of meaning because the resurrection is true.",
  },
  "16": {
    "1": "Now concerning the collection for the saints (hē logia eis tous hagious) — logia is a technical term for a charitable monetary collection; this is the Jerusalem relief fund Paul organized throughout the Gentile churches (Rom 15:25-27; 2 Cor 8-9; Gal 2:10). He gives the same directive he gave the churches of Galatia.",
    "2": "On the first day of every week each of you is to put something aside — the first day (Sunday, resurrection day) becomes the regular occasion for communal financial planning; the weekly rhythm ties giving to the resurrection calendar.",
    "3": "When I arrive, I will send those whom you accredit by letter to carry your gift to Jerusalem — Paul does not handle the money himself; he appoints delegates to carry it, guarding against any accusation of financial impropriety.",
    "4": "If it seems advisable that I should go also, they will accompany me — Paul leaves the decision open; his journey to Jerusalem with the collection becomes the fateful trip described in Acts 21.",
    "5": "I will visit you after passing through Macedonia — Paul's intended travel route: from Ephesus through Macedonia then to Corinth. The letter was written from Ephesus (v.8).",
    "6": "I intend to stay with you or even spend the winter so that you may help me on my journey wherever I go — the language of being sent on by the congregation (propemphthō, to be provided with provisions for travel) was standard in early Christian hospitality.",
    "7": "I do not want to see you now just in passing; I hope to spend some time with you if the Lord permits — the qualification the Lord permits (ean ho kyrios epitrepsē) reflects Paul's consistent acknowledgment that apostolic plans are subject to divine direction (Acts 18:21; Jas 4:15).",
    "8": "But I will stay in Ephesus until Pentecost — Ephesus is the base of operations; Pentecost marks the festival calendar that Paul still observed.",
    "9": "A wide door for effective work has opened to me, and there are many adversaries — thyra megalē (great door) is a metaphor for missionary opportunity; the adversaries (antikeimenos, those opposing) confirm that the opportunity is contested.",
    "10": "If Timothy comes, see that he is with you without fear — Paul sends Timothy as his representative but is uncertain when he will arrive; the community is instructed to put him at ease, since he is doing the work of the Lord as I am.",
    "11": "Let no one despise him (exouthenēsē) — the same verb used of despising the weak in the body (12:22) and of judging Paul's presence as weak (2 Cor 10:10); Timothy is apparently young and unimposing and at risk of being dismissed.",
    "12": "As for our brother Apollos, I strongly urged him to visit you with the other brothers, but it was not at all his will to come now — Apollos (the Alexandrian teacher of Acts 18:24-28, around whom one Corinthian faction formed, 1:12) declines Paul's request; Paul presents this without criticism, respecting Apollos's own judgment.",
    "13": "Be watchful (grēgoreite), stand firm in the faith (stēkete), act like men (andrizesthe), be strong (krataioūsthe) — four military-style imperatives in rapid succession. The first three are standard battlefield commands; krataioūsthe (be strong) echoes Psalm 31:24 and Deuteronomy 31:6-7.",
    "14": "Let all that you do be done in love (en agapē) — after the four assertive imperatives, the fifth overarching command reframes all the others; force without agape is militarism, not Christian community.",
    "15": "The household of Stephanas was the first converts in Achaia (aparche tēs Achaias) — aparche (firstfruits) again, as in 15:20, 23; the first believers in a region are the firstfruits of that harvest.",
    "16": "Be subject to such as these and to everyone who works and toils with them — hypotassō (be subject) applied not to ordained office-holders but to those who labor (kopiaō) in the community's service; authority flows from faithful service.",
    "17": "I rejoice at the coming of Stephanas and Fortunatus and Achaicus, because they have made up for your absence — these three are apparently the bearers of the Corinthian letter to Paul (7:1) and have supplied what Paul missed in not having the Corinthians present.",
    "18": "They refreshed my spirit and yours — anapauō (refresh, give rest) is the word Jesus used in the invitation to rest in him (Matt 11:28); those who serve the apostle reflect Christ's own refreshing presence.",
    "19": "The churches of Asia send you greetings — plural: there were multiple congregations in the province of Asia by this point. Aquila and Prisca with the church in their house send you hearty greetings in the Lord — the husband-wife team who traveled with Paul (Acts 18:2, 18, 26) host a house-church.",
    "20": "All the brothers greet you. Greet one another with a holy kiss — the holy kiss (philēma hagion) appears in all of Paul's letter-closings where greetings are mentioned (Rom 16:16; 2 Cor 13:12; 1 Thess 5:26); it was the customary form of greeting elevated into a liturgical act of Christian communion.",
    "21": "I, Paul, write this greeting with my own hand — Paul typically dictated his letters and added a closing greeting in his own hand as authentication (Col 4:18; 2 Thess 3:17; Gal 6:11); the signature verified the letter's genuineness.",
    "22": "If anyone has no love for the Lord, let him be accursed (anathema) — the opposite of love for the Lord is subject to the covenant curse (anathema, Greek equivalent of the Hebrew herem). Maranatha — the Aramaic prayer preserved in Greek letters: marana tha (our Lord, come!) or maran atha (our Lord has come). Either way it is the earliest Aramaic liturgical expression in the NT, reflecting the prayer-language of the earliest Aramaic-speaking church.",
    "23": "The grace of the Lord Jesus be with you — the standard Pauline letter-closing benediction; charis (grace) is the last theological word before the personal farewell.",
    "24": "My love be with you all in Christ Jesus — an unusual personal closing; Paul rarely adds a statement of his own love. The letter that began with divisions and rebukes ends with Paul's personal affection extending to all, in Christ Jesus.",
  }
}

if __name__ == '__main__':
    existing = load_comm('mkt-original', '1corinthians')
    merge_comm(existing, NEW)
    save_comm('mkt-original', '1corinthians', existing)
    for ch in ['15', '16']:
        print(f'  ch {ch}: {len(existing.get(ch, {}))} verses')
