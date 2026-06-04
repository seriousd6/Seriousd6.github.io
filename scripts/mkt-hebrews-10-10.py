"""
MKT Hebrews chapter 10 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hebrews-10-10.py

This is the first Hebrews chapter committed to draft. Conventions established here
should be carried forward by all subsequent Hebrews scripts.

Structure of the chapter:
  vv. 1–18  — The climax of the sacrificial argument (chs 7–10): one offering, complete atonement.
  vv. 19–25 — Three "let us" exhortations: draw near, hold fast, stir one another up.
  vv. 26–31 — Solemn warning against deliberate apostasy.
  vv. 32–39 — Call to persevering faith; Hab 2:3–4 closing quotation.

Translation decisions:

- G2962 (κύριος): "Lord" — consistent with all NT scripts; used for both the Father
  (v.16 new covenant quotation, v.30 Deut 32 quotation) and Jesus (v.12 sat at right hand
  of God is implied).

- G4151 (πνεῦμα): "Spirit" capitalised throughout — v.15 "the Holy Spirit" and v.29
  "the Spirit of grace" are clearly divine references; no lower-case 'spirit' appears in ch.10.

- G5048 (τελειόω): "perfect" (L) / "bring to completion" (M) / eschatological
  wholeness of standing before God (T). The word does not mean moral perfection alone;
  it denotes reaching the telos — full access to God's presence. Repeated at v.1
  (cannot perfect) and v.14 (has perfected).

- G266 (ἁμαρτία): "sin / sins" throughout — standard rendering.

- G2378 (θυσία): "sacrifice" — the animal/ritual act; distinct from G4376 (προσφορά)
  "offering" which covers Christ's self-offering in vv.10,14,18 and the Psalm 40
  quotation. Keeping both terms in play preserves the argument's own vocabulary.

- G4893 (συνείδησις): "conscience" — the inner awareness of moral status before God;
  v.2 "consciousness of sins" / v.22 "evil conscience." L/M both use "conscience"; T
  renders it as "guilt-awareness" or "inner awareness of guilt" where that sharpens sense.

- G1242 (διαθήκη): "covenant" — the new covenant of Jer 31 is the climax of vv.16–17,
  and "blood of the covenant" in v.29 echoes Exod 24 (Sinai). L/M/T all use "covenant."

- G3954 (παρρησία): v.19 "confidence" (M) / "free and open access" (T — the word
  denotes speaking freely, hence unimpeded approach to God); v.35 "confidence" (M/T).
  L uses "boldness" (closer to word meaning). This is a key ecclesial term in Hebrews.

- G4561 (σάρξ) v.20: "flesh" — Christ's body as the true curtain (καταπέτασμα); the
  clause "that is, through his flesh" identifies his torn flesh with the torn Temple curtain.
  L/M preserve "flesh"; T renders "body" with the curtain interpretation made explicit.

- G37 (ἁγιάζω): "sanctify / sanctified / consecrated" — set apart for God. v.10 we are
  sanctified (completed); v.14 those being sanctified (ongoing process, present ptc.);
  v.29 "he was sanctified" — the apostate is the referent (he was formerly set apart by
  covenant blood), not Christ; this reading intensifies the apostasy.

- G26 (ἀγάπη) v.24: "love" — covenantal, willed, self-giving love; distinguished from
  mere affection. The "stirring up" (G3948, παροξυσμός) is a strong word — a provocation,
  a sharp spur; T uses "provoke" or "spur" rather than the softer "encourage."

- G5590 (ψυχή): "soul" — v.38 "my soul" is God's inner being (anthropomorphism from LXX
  Hab); v.39 "souls" are the human persons preserved through faith.

- G4102 (πίστις) v.38–39: "faith" — personal trust and fidelity; in the Hab 2:4 quotation
  the LXX adds "my" (μου) to δίκαιος: "my righteous one" — the LORD's covenant partner.
  T tier surfaces this covenantal ownership.

- OT quotations:
  - vv.5–7: Psalm 40:6–8 LXX — uses LXX "a body you prepared for me" (not MT
    "ears you dug for me"). This is intentional; the author selects the LXX reading to
    advance the incarnation/body argument. Rendered as speech of Christ.
  - vv.16–17: Jeremiah 31:33–34 (same quotation as Hebrews 8:10–12, here abbreviated).
  - v.30: Deuteronomy 32:35–36 ("Vengeance is mine" + "The LORD will judge his people").
  - vv.37–38: Isaiah 26:20 LXX + Habakkuk 2:3–4 LXX combined; v.38 "my righteous one."

- Aspect notes:
  - v.10 "we have been sanctified" — perfect passive (completed, lasting result).
  - v.14 "he has perfected" — perfect active; "those being sanctified" — present ptc. ongoing.
  - v.26 "if we sin wilfully" — present ptc. (ongoing, habitual sin after receiving truth).
  - v.32 "you endured" — aorist, completed struggle.
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

HEBREWS = {
  "10": {
    "1": {
      "L": "For the law, having a shadow of the coming good things, not the very image of the things themselves, is never able year by year with the same sacrifices which they offer continually to make perfect those who draw near.",
      "M": "For the law contains only a shadow of the good things that are coming, not the true form of those realities, and can never, by the same sacrifices offered year after year without ceasing, bring to completion those who draw near.",
      "T": "The law was never more than a rough sketch—a foreshadow of the good things God was bringing—not the living reality itself. No matter how faithfully those annual sacrifices were repeated, they could not bring worshippers into the fullness of standing before God that he intended."
    },
    "2": {
      "L": "Otherwise would they not have ceased to be offered, because the worshippers, once having been cleansed, would have had no further consciousness of sins?",
      "M": "For if they could, would they not have stopped being offered? Because the worshippers, once truly cleansed, would no longer have been conscious of their sins.",
      "T": "If those sacrifices actually worked, they would have stopped. A worshipper who had been genuinely cleansed would carry no further inner awareness of guilt—but clearly that awareness remained, year after year."
    },
    "3": {
      "L": "But in those sacrifices there is a remembrance of sins year by year.",
      "M": "Instead, in those sacrifices there is an annual reminder of sins.",
      "T": "What the repeated sacrifices actually accomplished was the opposite of removal: each annual round rehearsed guilt rather than erasing it."
    },
    "4": {
      "L": "For it is impossible for the blood of bulls and goats to take away sins.",
      "M": "For it is impossible for the blood of bulls and goats to take away sins.",
      "T": "The problem was structural. Animal blood was simply unable to deal with human sin—it was the wrong currency for that transaction entirely."
    },
    "5": {
      "L": "Therefore coming into the world he says, 'Sacrifice and offering you did not desire, but a body you prepared for me;'",
      "M": "Therefore, when Christ comes into the world, he says, 'Sacrifice and offering you did not desire, but a body you have prepared for me;'",
      "T": "This is why, at the very moment of his entry into the world, Christ speaks with the words of Psalm 40—and the words are astonishing: 'You never truly wanted animal sacrifice, God. What you prepared for me was a body.'"
    },
    "6": {
      "L": "'in burnt offerings and sin offerings you took no pleasure.'",
      "M": "'In burnt offerings and offerings for sin you took no pleasure.'",
      "T": "'The entire range of burnt offerings and sin offerings—none of it was ever what you were really after.'"
    },
    "7": {
      "L": "'Then I said, \"Behold, I have come—in the roll of the book it has been written about me—to do your will, O God.\"'",
      "M": "'Then I said, \"See, I have come to do your will, O God, as it is written about me in the scroll of the book.\"'",
      "T": "'So here I am, Lord. The whole of Scripture pointed to this moment. I have come to do your will.'"
    },
    "8": {
      "L": "When above he says, 'Sacrifices and offerings and burnt offerings and sin offerings you neither desired nor took pleasure in'—which are offered according to the law—",
      "M": "When he said above, 'You have not desired nor taken pleasure in sacrifices and offerings and burnt offerings and sin offerings'—which are offered in accordance with the law—",
      "T": "Notice what that quotation names: every category of offering the law prescribed—grain offerings, animal sacrifices, burnt offerings, sin offerings—and God declares he neither wanted nor was pleased by any of them."
    },
    "9": {
      "L": "then he said, 'Behold, I have come to do your will.' He does away with the first in order to establish the second.",
      "M": "then he added, 'Behold, I have come to do your will.' He removes the first covenant order in order to establish the second.",
      "T": "Then comes the decisive line: 'I have come to do your will.' With that, Christ sweeps the old sacrificial order off the stage and sets the new—obedient self-offering—in its place."
    },
    "10": {
      "L": "By which will we have been sanctified through the offering of the body of Jesus Christ once for all.",
      "M": "By this will we have been sanctified through the offering of the body of Jesus Christ once for all.",
      "T": "It is precisely this will of God—obeyed by Christ in offering his own body—that has set us apart for God permanently. This happened once. It is complete. It will not be repeated."
    },
    "11": {
      "L": "And every priest stands day by day ministering and offering the same sacrifices repeatedly, which are never able to take away sins.",
      "M": "And every priest stands day after day in service, offering the same sacrifices over and over, which can never take away sins.",
      "T": "The contrast with the old priesthood is stark: priests stood every day at their post, repeating the same offering endlessly—because it never fully worked. The posture and the repetition both signal failure."
    },
    "12": {
      "L": "but this one, having offered one sacrifice for sins for all time, sat down at the right hand of God,",
      "M": "But this priest, having offered one sacrifice for sins for all time, sat down at the right hand of God,",
      "T": "Christ is utterly different. One sacrifice for sins—sufficient for eternity—and then he sat down at God's right hand. The seated posture is itself a declaration: the work is finished."
    },
    "13": {
      "L": "waiting from then until his enemies are placed as a footstool for his feet.",
      "M": "waiting from that time until his enemies are made a footstool for his feet.",
      "T": "From that throne he waits—not anxiously, but with royal certainty—for the day every hostile power is placed beneath his feet. The outcome is not in doubt; it is simply still unfolding."
    },
    "14": {
      "L": "For by one offering he has perfected for all time those who are being sanctified.",
      "M": "For by a single offering he has brought to completion for all time those who are being made holy.",
      "T": "One offering. And by it, all who are in the ongoing process of being made holy have been brought permanently to their destined fullness before God—not partially, not provisionally, but completely."
    },
    "15": {
      "L": "And the Holy Spirit also testifies to us; for after saying,",
      "M": "The Holy Spirit also bears witness to us concerning this; for after saying,",
      "T": "The Spirit himself adds his voice to confirm it. Through Jeremiah he had already said:"
    },
    "16": {
      "L": "'This is the covenant that I will establish with them after those days, says the Lord: I will put my laws upon their hearts, and upon their minds I will inscribe them,'",
      "M": "'This is the covenant I will make with them after those days, says the Lord: I will put my laws on their hearts and write them on their minds,'",
      "T": "'When those days come,' says the Lord, 'I will write my laws not on stone tablets but directly into their hearts and minds—no longer external commands, but an inward reality.'"
    },
    "17": {
      "L": "then, 'Their sins and their lawless deeds I will remember no more.'",
      "M": "then he adds, 'I will remember their sins and their lawless deeds no more.'",
      "T": "And then the decisive promise: God will not merely overlook those sins—he will cease to remember them. They will have no existence in his mind."
    },
    "18": {
      "L": "Now where there is forgiveness of these, there is no longer any offering for sin.",
      "M": "Where there is forgiveness of these sins, there is no longer any offering for sin.",
      "T": "The logic is airtight: if sins are truly and permanently forgiven, what further sacrifice could possibly be needed? Complete forgiveness ends the entire age of sacrifice."
    },
    "19": {
      "L": "Therefore, brothers, having boldness to enter the holy places by the blood of Jesus,",
      "M": "Therefore, brothers and sisters, since we have confidence to enter the holy places by the blood of Jesus,",
      "T": "Brothers and sisters—the argument now becomes an invitation. Because of Christ's blood we have free and unimpeded access into God's own presence, the holiest place that exists."
    },
    "20": {
      "L": "by the new and living way that he opened for us through the curtain, that is, his flesh,",
      "M": "by the new and living way that he opened for us through the curtain, that is, through his flesh,",
      "T": "The route in is new—it never existed before. It is living—Christ himself is the way. And the curtain that was torn open to give us entry? That curtain is his own body, his flesh given on the cross."
    },
    "21": {
      "L": "and having a great priest over the house of God,",
      "M": "and since we have a great high priest over the house of God,",
      "T": "We also have a great high priest who presides over God's whole household—one who not only knows the way in but is the way in."
    },
    "22": {
      "L": "let us draw near with a true heart in full assurance of faith, having our hearts sprinkled clean from an evil conscience and our bodies washed with pure water.",
      "M": "let us draw near with a sincere heart and in full assurance of faith, with our hearts sprinkled clean from an evil conscience and our bodies washed with pure water.",
      "T": "So come. Come with genuine hearts, without the paralysing inner awareness of unresolved guilt. Our consciences have been cleansed by the blood of Christ's covenant; our bodies have been washed in baptism. There is nothing left to bar our way."
    },
    "23": {
      "L": "Let us hold fast the confession of our hope without wavering, for faithful is he who promised.",
      "M": "Let us hold firmly to the confession of our hope without wavering, for he who promised is faithful.",
      "T": "Hold the rope of hope and don't let go. The public confession we have made—Christ crucified, risen, coming—stand there unmoved. God who made those promises does not waver, so neither should we."
    },
    "24": {
      "L": "And let us consider one another for the stirring up of love and good works,",
      "M": "And let us consider how to spur one another on to love and good works,",
      "T": "And think purposefully about one another—about how to provoke each other toward love and toward concrete acts of goodness. This requires attention and creativity, not passivity."
    },
    "25": {
      "L": "not forsaking the assembling of ourselves together, as is the habit of some, but encouraging one another, and all the more as you see the Day approaching.",
      "M": "not neglecting to meet together, as is the habit of some, but encouraging one another, and all the more as you see the Day drawing near.",
      "T": "Don't stop gathering—some have already fallen into that drift, and it leads nowhere good. Meeting together is how we hold each other up, and the urgency of gathering only increases as the Day of the Lord draws closer."
    },
    "26": {
      "L": "For if we go on sinning wilfully after receiving the knowledge of the truth, there no longer remains any sacrifice for sins,",
      "M": "For if we go on sinning deliberately after receiving the knowledge of the truth, there no longer remains a sacrifice for sins,",
      "T": "A sobering reality must be named: if someone who has received the full light of the gospel deliberately, persistently continues in sin, they have stepped outside the only frame within which forgiveness operates. There is no alternative sacrifice."
    },
    "27": {
      "L": "but a certain terrifying expectation of judgment and a fury of fire about to devour the adversaries.",
      "M": "but a terrifying expectation of judgment and a raging fire that will consume the adversaries of God.",
      "T": "What remains for such a person is not mercy but something dreadful: the certain anticipation of judgment and the fire reserved for those who stand as enemies of God."
    },
    "28": {
      "L": "Anyone who has set aside the law of Moses dies without mercy on the testimony of two or three witnesses.",
      "M": "Anyone who rejected the law of Moses died without mercy on the evidence of two or three witnesses.",
      "T": "Think about what the old covenant demanded: to disown Moses' law brought death—no clemency, no appeal, no exception. The standard was severe."
    },
    "29": {
      "L": "By how much more severe punishment do you think the one will be judged worthy who trampled underfoot the Son of God and regarded as a common thing the blood of the covenant by which he was sanctified, and insulted the Spirit of grace?",
      "M": "How much worse punishment, do you think, will be deserved by the one who has trampled underfoot the Son of God, has treated as something common the blood of the covenant by which he was sanctified, and has insulted the Spirit of grace?",
      "T": "Now multiply that severity by what is at stake. To trample the Son of God underfoot. To treat as worthless and defiled the blood of the new covenant—the very blood that had once set that person apart for God. To insult the Spirit who carries grace into the world. The punishment owed for this exceeds anything Moses' law could impose."
    },
    "30": {
      "L": "For we know the one who said, 'Vengeance belongs to me, I will repay,' and again, 'The Lord will judge his people.'",
      "M": "For we know him who said, 'Vengeance is mine; I will repay,' and again, 'The Lord will judge his people.'",
      "T": "We are not speaking of an abstraction. We know who made these declarations—the God who said, 'I myself will deal with wrongs; I will repay.' He also said, 'I will judge my own people.' The warning therefore falls on those who are inside the covenant, not strangers to it."
    },
    "31": {
      "L": "It is a terrifying thing to fall into the hands of the living God.",
      "M": "It is a terrifying thing to fall into the hands of the living God.",
      "T": "There is nothing tame about this. To fall into the hands of the living God—not the hands of mercy extended in invitation, but the hands of a living Judge who is not indifferent—is a prospect that should make anyone tremble."
    },
    "32": {
      "L": "But call to remembrance the former days in which, after being enlightened, you endured a great struggle of sufferings,",
      "M": "But recall the earlier days when, after you were enlightened, you endured a hard and painful struggle,",
      "T": "Now shift the gaze. Look back. Remember what you were in those first days after the light broke in—you did not buckle. You absorbed a great and costly struggle."
    },
    "33": {
      "L": "partly being publicly exposed to reproaches and afflictions, and partly becoming sharers with those being so treated.",
      "M": "sometimes being publicly exposed to reproach and affliction, and sometimes standing alongside those who were treated this way.",
      "T": "You were publicly shamed and made to suffer. And when others were targeted, you stood with them rather than quietly stepping back to protect yourselves."
    },
    "34": {
      "L": "For you had compassion on those in chains and accepted with joy the plundering of your possessions, knowing that you yourselves have a better and an abiding possession.",
      "M": "For you showed compassion to those in prison and joyfully accepted the plundering of your property, since you knew that you yourselves had a better possession, one that lasts.",
      "T": "You visited prisoners—at real risk to yourselves. When your own property was seized, you received it with joy, because you had already calculated: what cannot be taken from you is worth far more than what can."
    },
    "35": {
      "L": "Therefore do not throw away your confidence, which has a great reward.",
      "M": "Therefore do not throw away your confidence, which carries a great reward.",
      "T": "So don't abandon now what you paid so much to build. That free, unashamed confidence before God—hold it. Attached to it is a reward greater than anything you have surrendered."
    },
    "36": {
      "L": "For you have need of endurance, so that having done the will of God you may receive the promise.",
      "M": "For you need endurance, so that when you have done the will of God you may receive what was promised.",
      "T": "What you need at this moment is not a new argument but the capacity to keep going. Do what God calls you to do—keep doing it—and the promised outcome will arrive."
    },
    "37": {
      "L": "'For yet a little while, and the coming one will come and will not delay;'",
      "M": "'For yet a little while, and the coming one will come and will not delay.'",
      "T": "Scripture says: 'A little while—only a little—and the One who is coming will come. He will not keep you waiting.' The wait is not endless."
    },
    "38": {
      "L": "'But my righteous one shall live by faith, and if he shrinks back, my soul has no pleasure in him.'",
      "M": "'But my righteous one will live by faith, and if he shrinks back, my soul takes no pleasure in him.'",
      "T": "'The one I call my righteous one lives by trusting me—not by sight, not by comfort, not by the relief of pulling back. But if he retreats into fear, I take no pleasure in him.' The 'my' is the LORD's possessive: this is a covenant partner, and faithfulness is what the relationship requires."
    },
    "39": {
      "L": "But we are not of those who draw back to destruction, but of those of faith for the preservation of the soul.",
      "M": "But we do not belong to those who shrink back and are destroyed, but to those who have faith and so preserve their souls.",
      "T": "And we—we are not in that retreating category. We are not pulling back toward ruin. We are the ones whose faith carries their very lives forward into safety."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hebrews')
        merge_tier(existing, HEBREWS, tier_key)
        save(tier_dir, 'hebrews', existing)
    print('Hebrews 10 written.')

if __name__ == '__main__':
    main()
