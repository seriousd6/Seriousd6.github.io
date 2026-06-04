"""
MKT 2 Corinthians chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2corinthians-4-6.py

Translation decisions:
- G2962 (κύριος): "Lord" across all tiers — consistent with all Pauline scripts, including 1 Cor.
- G4151 (πνεῦμα): "Spirit" (capitalized) throughout chs 4–6; all occurrences in these chapters
  refer to the Holy Spirit (4:13 "spirit of faith" follows the gloss, lowercased; 6:6 "Holy Spirit"
  explicit). 4:13 rendered "spirit of faith" lowercase to match the pattern from 1 Cor scripts where
  human-spirit uses are lowercased.
- G4561 (σάρξ): "flesh" in L. At 4:11 "mortal flesh" preserved across all tiers (the Greek is literal
  θνητὴ σάρξ). At 5:16 κατὰ σάρκα = "according to the flesh" (L), "from a worldly point of view" (M),
  "from the outside-in, by merely human standards" (T) — the same contextual handling as the 1 Cor scripts.
- G1343 (δικαιοσύνη): "righteousness" in L/M throughout; at 5:21 T adds "clothed in his own righteousness"
  to surface the forensic-imputation sense without over-explaining in L/M. At 6:14 kept as "righteousness"
  vs "lawlessness" across all tiers.
- G2643 (καταλλαγή) / G2644 (καταλλάσσω): "reconciliation" / "reconcile" consistently across all tiers in
  5:18-20 — the single best English equivalent for this covenant-restoration term.
- G728 (ἀρραβών) at 5:5: "pledge" (L) / "deposit, guaranteeing what is to come" (M) / "first installment—
  the down payment" (T). The Greek term was a commercial word for earnest money; the T surfaces this register.
- G4243 (πρεσβεύω) at 5:20: "ambassadors" in all tiers — the official diplomatic register Paul consciously
  invokes. Not softened to "representatives" in L.
- G5547 (Χριστός): "Christ" across all tiers — Corinthian audience is primarily Greek; the term functions
  as a proper name in Paul's Corinthian correspondence, consistent with 1 Cor scripts.
- 5:17 (καινή κτίσις): "new creation" — the eschatological category, not merely personal transformation.
  L preserves the anarthrous noun: "there is a new creation." T draws out the cosmic scope.
- 5:21: "him who knew no sin he made to be sin" — retained over the alternative "sin offering" reading.
  While the LXX uses ἁμαρτία for חַטָּאת (sin offering), Paul's point here is the substitution of status
  (sinless takes on the category of sin), not the mechanics of offering. The plain reading is followed in
  all tiers; T surfaces the exchange/imputation dimension.
- 6:14-18 composite OT quotation (Lev 26:11-12 / Ezek 37:27 / Isa 52:11 / 2 Sam 7:14 / Isa 43:6):
  Paul weaves these without precise citation; translations follow Paul's adapted Greek rather than any
  single OT version. The catena is treated as a unified rhetorical block.
- G955 (Βελιάρ/Βελίαλ) at 6:15: "Belial" across all tiers — the adversary/worthlessness figure from
  Hebrew Bible; more precise than "the devil" (which would be G1228 διάβολος) and preserves the OT register.
- Aspect note: 5:17 aorist (παρῆλθεν, γέγονεν) = completed change of state; "has passed away / has come"
  in L/M; T uses present-tense shock to mirror the behold-imperative (ἰδού).
- 4:13 OT echo (Ps 116:10 LXX): "I believed, therefore I spoke" — rendered as a citation in all tiers.
- Divine name: no יהוה (H3068) in these chapters. "Lord" (G2962 κύριος) renders the NT use.
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
  "4": {
    "1": {
      "L": "Therefore, having this ministry, just as we received mercy, we do not lose heart—",
      "M": "Therefore, since we have this ministry through God's mercy, we do not give up.",
      "T": "We have been entrusted with this ministry—and that only because of God's mercy toward us. So we do not lose heart."
    },
    "2": {
      "L": "But we have renounced the hidden things of shame; not walking in craftiness nor adulterating the word of God; but by the manifestation of truth we commend ourselves to every man's conscience before God.",
      "M": "Rather, we have renounced secret and shameful ways; we do not use deception, nor do we distort the word of God. On the contrary, by setting forth the truth plainly we commend ourselves to everyone's conscience in the sight of God.",
      "T": "We have put away every secret disgrace and every underhanded scheme. We never tamper with God's word to make it say what people want to hear. Instead, by declaring the truth openly and honestly, we let every person's conscience be the judge—under God's own gaze."
    },
    "3": {
      "L": "And if our gospel is indeed veiled, it is veiled among those who are perishing—",
      "M": "And even if our gospel is veiled, it is veiled to those who are perishing.",
      "T": "If our message is hidden at all, it is hidden only to those who are on the road to destruction."
    },
    "4": {
      "L": "in whom the god of this age has blinded the minds of the unbelieving, so that the light of the gospel of the glory of Christ, who is the image of God, might not dawn upon them.",
      "M": "The god of this age has blinded the minds of unbelievers, so that they cannot see the light of the gospel that displays the glory of Christ, who is the image of God.",
      "T": "The ruler of this present age has blinded the minds of those who refuse to believe, keeping them from seeing the blazing light of the good news—the glory of Christ, who is himself the image of God."
    },
    "5": {
      "L": "For we do not preach ourselves, but Christ Jesus as Lord, and ourselves as your servants for Jesus' sake.",
      "M": "For what we preach is not ourselves, but Jesus Christ as Lord, and ourselves as your servants for Jesus' sake.",
      "T": "We do not proclaim ourselves. We proclaim Jesus Christ as Lord—and ourselves as nothing more than your servants for Jesus' sake."
    },
    "6": {
      "L": "For God, who said, 'Out of darkness light shall shine,' is the one who has shone in our hearts to give the light of the knowledge of the glory of God in the face of Jesus Christ.",
      "M": "For God, who said, 'Let light shine out of darkness,' made his light shine in our hearts to give us the light of the knowledge of God's glory displayed in the face of Christ.",
      "T": "The same God who commanded light to blaze out of the primordial darkness has flooded our hearts with light—the light that reveals the knowledge of God's glory as it shines in the face of Jesus Christ."
    },
    "7": {
      "L": "But we have this treasure in earthen vessels, so that the surpassing greatness of the power may be of God and not from us.",
      "M": "But we have this treasure in jars of clay to show that this all-surpassing power is from God and not from us.",
      "T": "Yet we carry this priceless treasure in ordinary clay jars—so that the extraordinary power at work in us is unmistakably God's and not our own."
    },
    "8": {
      "L": "in everything pressed but not crushed, perplexed but not despairing,",
      "M": "We are hard pressed on every side, but not crushed; perplexed, but not in despair;",
      "T": "We are pressed from every direction—but not crushed. We are bewildered—but never in complete despair."
    },
    "9": {
      "L": "persecuted but not forsaken, cast down but not destroyed;",
      "M": "persecuted, but not abandoned; struck down, but not destroyed.",
      "T": "We are hunted—but never abandoned. We are knocked to the ground—but never finished off."
    },
    "10": {
      "L": "always carrying in the body the dying of Jesus, so that the life also of Jesus may be manifested in our body.",
      "M": "We always carry around in our body the death of Jesus, so that the life of Jesus may also be revealed in our body.",
      "T": "At every moment we carry in our bodies the dying of Jesus—so that the life of Jesus may also be seen at work in our mortal bodies."
    },
    "11": {
      "L": "For we who live are always being delivered over to death for Jesus' sake, so that the life of Jesus also may be manifested in our mortal flesh.",
      "M": "For we who are alive are always being given over to death for Jesus' sake, so that his life may also be revealed in our mortal body.",
      "T": "We who are still alive are being handed over to death again and again—for Jesus' sake—so that his life might break through into this dying flesh."
    },
    "12": {
      "L": "So then death works in us, but life in you.",
      "M": "So then, death is at work in us, but life is at work in you.",
      "T": "Death is doing its work in us—but life is flowing to you."
    },
    "13": {
      "L": "But having the same spirit of faith, according to what is written, 'I believed, and so I spoke,' we also believe, and so we also speak,",
      "M": "It is written: 'I believed; therefore I have spoken.' Since we have that same spirit of faith, we also believe and therefore speak,",
      "T": "Scripture says, 'I believed, and so I spoke.' We have that same spirit of faith—we believe, and so we speak."
    },
    "14": {
      "L": "knowing that he who raised the Lord Jesus will raise us also with Jesus and will present us with you.",
      "M": "because we know that the one who raised the Lord Jesus from the dead will also raise us with Jesus and present us with you to himself.",
      "T": "We know this: the God who raised the Lord Jesus from the dead will also raise us up with Jesus—and will bring all of us, you included, into his presence."
    },
    "15": {
      "L": "For all things are for your sake, so that the grace which is spreading through more people may cause the giving of thanks to overflow to the glory of God.",
      "M": "All this is for your benefit, so that the grace that is reaching more and more people may cause thanksgiving to overflow to the glory of God.",
      "T": "Everything that happens to us is for your sake—so that as grace spreads to more and more people, the flood of thanksgiving may rise and overflow, all to the glory of God."
    },
    "16": {
      "L": "Therefore we do not lose heart. Though our outer man is decaying, yet our inner man is being renewed day by day.",
      "M": "Therefore we do not lose heart. Though outwardly we are wasting away, yet inwardly we are being renewed day by day.",
      "T": "So we do not give up. Even though our bodies are wearing out, the inner person is being made new every single day."
    },
    "17": {
      "L": "For this momentary, light affliction is producing for us an eternal weight of glory beyond all comparison,",
      "M": "For our light and momentary troubles are achieving for us an eternal glory that far outweighs them all.",
      "T": "Our present troubles are slight and short-lived compared to the immeasurable, unending weight of glory being produced in us through them."
    },
    "18": {
      "L": "while we look not at the things seen but at the things not seen; for the things seen are temporal, but the things not seen are eternal.",
      "M": "So we fix our eyes not on what is seen, but on what is unseen, since what is seen is temporary, but what is unseen is eternal.",
      "T": "We keep our gaze on what cannot be seen rather than on what can—because the visible world is passing away, while what is invisible lasts forever."
    }
  },
  "5": {
    "1": {
      "L": "For we know that if our earthly tent-house is destroyed, we have a building from God, a house not made with hands, eternal in the heavens.",
      "M": "For we know that if the earthly tent we live in is destroyed, we have a building from God, an eternal house in heaven, not built by human hands.",
      "T": "We know this: if the tent we now live in—our earthly body—is torn down, we have a permanent home waiting from God, a dwelling place in the heavens, built without human hands, built to last forever."
    },
    "2": {
      "L": "For indeed in this we groan, longing to be clothed with our dwelling from heaven,",
      "M": "Meanwhile we groan, longing to be clothed instead with our heavenly dwelling,",
      "T": "In this tent we groan—aching to put on our heavenly home like a garment over us,"
    },
    "3": {
      "L": "inasmuch as having put it on we shall not be found naked.",
      "M": "because when we are clothed, we will not be found naked.",
      "T": "for when that happens we will be fully clothed, not stripped bare."
    },
    "4": {
      "L": "For indeed we who are in this tent groan, being burdened—not because we wish to be unclothed but clothed, so that what is mortal may be swallowed up by life.",
      "M": "For while we are in this tent, we groan and are burdened, because we do not wish to be unclothed but to be clothed instead with our heavenly dwelling, so that what is mortal may be swallowed up by life.",
      "T": "We are burdened inside this tent—we groan under the weight—not because we want to shed our bodies, but because we want to be further clothed, so that what is mortal and dying in us might be absorbed into life itself."
    },
    "5": {
      "L": "Now the one who has prepared us for this very thing is God, who has given us the Spirit as a pledge.",
      "M": "Now the one who has fashioned us for this very purpose is God, who has given us the Spirit as a deposit, guaranteeing what is to come.",
      "T": "And God is the one who has been shaping us all along for this very destiny. As proof of his intention, he has given us his Spirit as a first installment—the down payment on everything that is coming."
    },
    "6": {
      "L": "Therefore, being always of good courage, and knowing that while we are at home in the body we are absent from the Lord—",
      "M": "Therefore we are always confident and know that as long as we are at home in the body we are away from the Lord.",
      "T": "So we are always full of courage. We know that while we make our home in this body, we are away from our true home—away from the Lord."
    },
    "7": {
      "L": "for we walk by faith, not by sight.",
      "M": "For we live by faith, not by sight.",
      "T": "This is the only way we travel: by trusting what we cannot see, not by what our eyes can observe."
    },
    "8": {
      "L": "we are of good courage and prefer rather to be absent from the body and to be at home with the Lord.",
      "M": "We are confident, I say, and would prefer to be away from the body and at home with the Lord.",
      "T": "Yes, we are full of courage—and we would far rather leave this body and be home with the Lord."
    },
    "9": {
      "L": "Therefore we also make it our ambition, whether at home or absent, to be pleasing to him.",
      "M": "So we make it our goal to please him, whether we are at home in the body or away from it.",
      "T": "Whether we are in the body or out of it, we share one ambition: to please him."
    },
    "10": {
      "L": "For we must all appear before the judgment seat of Christ, so that each one may receive the things done through the body, according to what he has done, whether good or bad.",
      "M": "For we must all appear before the judgment seat of Christ, so that each of us may receive what is due us for the things done while in the body, whether good or bad.",
      "T": "For we will all stand before Christ's judgment seat—every one of us. Each person will give an account for what they did with their life in this body, good or bad."
    },
    "11": {
      "L": "Therefore, knowing the fear of the Lord, we persuade men; but we are made manifest to God. And I hope we are also made manifest to your consciences.",
      "M": "Since, then, we know what it is to fear the Lord, we try to persuade others. What we are is plain to God, and I hope it is also plain to your conscience.",
      "T": "Knowing what it is to stand in awe before the Lord, we work to persuade others. God already sees us for what we are—and I hope your own conscience also recognizes the truth about us."
    },
    "12": {
      "L": "We are not commending ourselves to you again, but giving you occasion to boast on our behalf, so that you may have something to say to those who boast in outward appearance and not in heart.",
      "M": "We are not trying to commend ourselves to you again, but are giving you an opportunity to take pride in us, so that you can answer those who take pride in what is seen rather than in what is in the heart.",
      "T": "We are not promoting ourselves again. We are giving you reason to be proud of us—so that you will have something to say when people boast about surface appearances rather than what is in the heart."
    },
    "13": {
      "L": "For if we are beside ourselves, it is for God; if we are of sound mind, it is for you.",
      "M": "If we are out of our mind, it is for the sake of God; if we are in our right mind, it is for you.",
      "T": "If we seem out of our minds, it is before God that we are so—and it is for his sake. If we are sober and collected, it is for yours."
    },
    "14": {
      "L": "For the love of Christ controls us, since we have concluded this: that one died for all, therefore all died;",
      "M": "For Christ's love compels us, because we are convinced that one died for all, and therefore all died.",
      "T": "Christ's love has seized hold of us—for we have reached this conclusion: one man died for all, which means that in him all died."
    },
    "15": {
      "L": "and he died for all, so that those who live might live no longer for themselves but for him who died for them and was raised.",
      "M": "And he died for all, that those who live should no longer live for themselves but for him who died for them and was raised again.",
      "T": "He died for all of them—so that those who are now alive would stop living for themselves and start living for the one who died and rose again for them."
    },
    "16": {
      "L": "Therefore from now on we know no one according to the flesh; even though we once knew Christ according to the flesh, we know him so no longer.",
      "M": "So from now on we regard no one from a worldly point of view. Though we once regarded Christ in this way, we do so no longer.",
      "T": "From this point on, then, we no longer evaluate anyone from the outside-in, by merely human standards. We once thought about Christ that way—but we have left that way of seeing behind."
    },
    "17": {
      "L": "Therefore, if anyone is in Christ, there is a new creation; the old has passed away—behold, the new has come.",
      "M": "Therefore, if anyone is in Christ, the new creation has come: the old has gone, the new is here!",
      "T": "Anyone who is in Christ has entered the new creation. The old order of things is gone. Look—everything has become new!"
    },
    "18": {
      "L": "All these things are from God, who through Christ reconciled us to himself and gave us the ministry of reconciliation:",
      "M": "All this is from God, who reconciled us to himself through Christ and gave us the ministry of reconciliation:",
      "T": "All this comes from God. He is the one who, through Christ, brought us back into relationship with himself—and then handed us the task of bringing others into that same reconciliation."
    },
    "19": {
      "L": "that God was in Christ reconciling the world to himself, not counting their trespasses against them, and has committed to us the word of reconciliation.",
      "M": "that God was reconciling the world to himself in Christ, not counting people's sins against them. And he has committed to us the message of reconciliation.",
      "T": "Here is what that reconciliation means: in Christ, God was making peace with the whole world—not holding anyone's sins against them. And he has entrusted us with the proclamation of that peace."
    },
    "20": {
      "L": "We are therefore ambassadors for Christ, God making his appeal through us. We implore you on behalf of Christ, be reconciled to God.",
      "M": "We are therefore Christ's ambassadors, as though God were making his appeal through us. We implore you on Christ's behalf: Be reconciled to God.",
      "T": "We are official envoys on Christ's behalf—and when we speak, God himself is making the appeal through us. We urge you, as Christ's representatives: accept the reconciliation God is offering."
    },
    "21": {
      "L": "Him who knew no sin he made to be sin on our behalf, so that we might become the righteousness of God in him.",
      "M": "God made him who had no sin to be sin for us, so that in him we might become the righteousness of God.",
      "T": "The sinless one he made to carry our sin—so that in him we might stand before God clothed in his own righteousness."
    }
  },
  "6": {
    "1": {
      "L": "Working together with him, we also urge you not to receive the grace of God in vain—",
      "M": "As God's co-workers we urge you not to receive God's grace in vain.",
      "T": "As those who work alongside God, we beg you: do not let the grace he has given you go to waste."
    },
    "2": {
      "L": "For he says, 'In a favorable time I listened to you, and in a day of salvation I helped you.' Behold, now is the favorable time; behold, now is the day of salvation.",
      "M": "For he says, 'In the time of my favor I heard you, and in the day of salvation I helped you.' I tell you, now is the time of God's favor, now is the day of salvation.",
      "T": "For God says in Scripture: 'At the right moment I answered you; on the day of salvation I came to your aid.' That right moment is now. Today is the day of salvation."
    },
    "3": {
      "L": "We give no offense in anything, so that the ministry may not be blamed.",
      "M": "We put no stumbling block in anyone's path, so that our ministry will not be discredited.",
      "T": "We do nothing that would put an obstacle in anyone's way—we will not allow the ministry to be brought into disrepute."
    },
    "4": {
      "L": "but as servants of God we commend ourselves in every way: by great endurance, in afflictions, in hardships, in distresses,",
      "M": "Rather, as servants of God we commend ourselves in every way: in great endurance; in troubles, hardships and distresses;",
      "T": "Instead, we show ourselves true servants of God in every circumstance—by patient endurance through troubles, hardships, and desperate situations;"
    },
    "5": {
      "L": "in beatings, in imprisonments, in riots, in labors, in sleepless nights, in fastings;",
      "M": "in beatings, imprisonments and riots; in hard work, sleepless nights and hunger;",
      "T": "through beatings, imprisonments, and riots; through exhausting labor, sleepless nights, and going without food;"
    },
    "6": {
      "L": "in purity, in knowledge, in patience, in kindness, in the Holy Spirit, in genuine love;",
      "M": "in purity, understanding, patience and kindness; in the Holy Spirit and in sincere love;",
      "T": "by purity of life, clear understanding, patient endurance, and genuine kindness; by the power of the Holy Spirit and by authentic love;"
    },
    "7": {
      "L": "in the word of truth, in the power of God, with the weapons of righteousness for the right hand and the left;",
      "M": "in truthful speech and in the power of God; with weapons of righteousness in the right hand and in the left;",
      "T": "with the word of truth and the power of God as our weapons; with righteousness as our armor in both hands—for both attack and defense;"
    },
    "8": {
      "L": "through honor and dishonor, through evil report and good report; as deceivers yet true,",
      "M": "through glory and dishonor, bad report and good report; genuine, yet regarded as impostors;",
      "T": "through honor and disgrace, through slander and praise—written off as frauds, yet completely honest;"
    },
    "9": {
      "L": "as unknown yet well known, as dying and behold we live, as punished yet not killed,",
      "M": "known and yet regarded as unknown; dying, and yet we live on; beaten, and yet not killed;",
      "T": "dismissed as nobodies yet known to everyone; on the edge of death, yet still alive; beaten within an inch of our lives, yet never actually killed;"
    },
    "10": {
      "L": "as sorrowful yet always rejoicing, as poor yet making many rich, as having nothing yet possessing all things.",
      "M": "sorrowful, yet always rejoicing; poor, yet making many rich; having nothing, and yet possessing everything.",
      "T": "broken-hearted, yet always full of joy; penniless, yet enriching many; owning nothing, yet possessing everything."
    },
    "11": {
      "L": "Our mouth is open to you, Corinthians; our heart is wide open.",
      "M": "We have spoken freely to you, Corinthians, and opened wide our hearts to you.",
      "T": "Corinthians, we have spoken plainly with you—our hearts have been thrown wide open to you."
    },
    "12": {
      "L": "You are not restrained in us, but you are restrained in your own affections.",
      "M": "We are not withholding our affection from you, but you are withholding yours from us.",
      "T": "We have not closed our hearts to you—you are the ones who have closed yours to us."
    },
    "13": {
      "L": "Now in return—I speak as to children—you also be open wide.",
      "M": "As a fair exchange—I speak as to my children—open wide your hearts also.",
      "T": "As a fair return—and I am speaking to you as my own children—open your hearts wide to us as well."
    },
    "14": {
      "L": "Do not be unequally yoked with unbelievers; for what partnership has righteousness with lawlessness? Or what fellowship has light with darkness?",
      "M": "Do not be yoked together with unbelievers. For what do righteousness and wickedness have in common? Or what fellowship can light have with darkness?",
      "T": "Do not link your life to unbelievers as though you were equal partners. What bond can there be between righteousness and wickedness? What common ground between light and darkness?"
    },
    "15": {
      "L": "What accord has Christ with Belial? Or what portion has a believer with an unbeliever?",
      "M": "What harmony is there between Christ and Belial? Or what does a believer have in common with an unbeliever?",
      "T": "What harmony can there be between Christ and Belial, the enemy of all good? What shared life exists between someone who trusts God and someone who does not?"
    },
    "16": {
      "L": "What agreement has the temple of God with idols? For we are the temple of the living God; as God said, 'I will dwell in them and walk among them, and I will be their God, and they shall be my people.'",
      "M": "What agreement is there between the temple of God and idols? For we are the temple of the living God. As God has said: 'I will live with them and walk among them, and I will be their God, and they will be my people.'",
      "T": "What agreement can exist between the temple of God and the shrine of an idol? We ourselves are the temple of the living God—and God has said: 'I will make my home among them. I will walk with them. I will be their God, and they will be my people.'"
    },
    "17": {
      "L": "'Therefore go out from their midst and be separate, says the Lord, and touch no unclean thing; then I will welcome you,'",
      "M": "Therefore, 'Come out from them and be separate, says the Lord. Touch no unclean thing, and I will receive you.'",
      "T": "'Come out from among them,' says the Lord. 'Keep yourself separate. Do not touch what is defiled—and I will take you to myself.'"
    },
    "18": {
      "L": "'And I will be a father to you, and you shall be sons and daughters to me, says the Lord Almighty.'",
      "M": "'And I will be a Father to you, and you will be my sons and daughters, says the Lord Almighty.'",
      "T": "'I will be your Father,' says the Lord Almighty—'and you will be my sons and daughters.'"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2corinthians')
        merge_tier(existing, CORINTHIANS_2, tier_key)
        save(tier_dir, '2corinthians', existing)
    print('2 Corinthians 4–6 written.')

if __name__ == '__main__':
    main()
