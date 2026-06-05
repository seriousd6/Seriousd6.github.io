"""
MKT Christ Commentary — John chapter 8
Run: python3 scripts/zc-christ-john-8-8.py

Source data used:
- data/interlinear/john.json
- data/translation/glossary-greek.json (ἐγώ εἰμι, ὑψωθῇ, ἐλεύθερος)
- data/translation/draft/mediating/john.json (MKT text for quoting)
- data/echoes/john.json (OT connections already established for ch 8)
- data/commentary/mkt-original/john.json (terminology: "the Evangelist")
- data/commentary/mkt-christ/john.json (chs 1–4 terminology carry-forward)

Key decisions in this range:
- "The Evangelist" used consistently (matching chs 1–4 register)
- Pericope Adulterae (8:1–11) is absent from the earliest Greek MSS (P66, P75,
  Sinaiticus, Vaticanus) but is traditional canonical content; treated at face value
  with Christological freight noted; textual status flagged in v1 entry
- v7 noted as the only occasion where Christ himself (by his own sinlessness criterion)
  could have thrown the stone — and chose not to: this is 3:17 enacted in person
- v12 "I am the light of the world" classified as direct fulfillment of Isa 42:6; 49:6;
  Isa 9:2 — the Servant self-identifies, not merely analogizes
- ego eimi in v24 and v28 classified as deliberate divine-name appropriation (Exod 3:14;
  Isa 43:10 series) — the crowd's understanding confirms this in v59
- v28 "lifted up" (hypsōthēnai) classified as type/fulfillment of Isa 52:13 — crucifixion
  as simultaneous execution and exaltation; connects to 3:14 (bronze serpent) and 12:32
- v36 classified as fulfillment of Isa 61:1 jubilee — the Son's freedom is permanent,
  not cyclical; carries forward the "truth sets free" logic of v32
- v46 sinlessness challenge ("can any of you prove me guilty of sin?") classified as
  fulfillment of Isa 53:9 — sinlessness constitutive of the Servant's vicarious role
- v56 "Abraham rejoiced to see my day" classified as type: the Akedah (Gen 22) is the
  vision Abraham received; what he saw typologically was the substitutionary death of
  the true Son
- v58 "before Abraham was born, I am" classified as the chapter's Christological apex:
  eternal divine existence claimed in the precise formula of Exod 3:14 / Isa 43:10;
  v59 stoning response confirms the crowd understood the claim as a divine-name assertion
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


JOHN = {
  "8": {
    "1": '<p>The Mount of Olives, where Christ withdraws overnight, carries Davidic resonance — David fled across that same ridge weeping when betrayed (2 Sam 15:30) — and eschatological weight: Zechariah 14:4 locates the Lord\'s decisive arrival there. Note: this passage (8:1–11) is absent from the earliest manuscripts (P66, P75, Sinaiticus, Vaticanus), though it circulates as traditional canonical material. Its Christological content is treated at face value.</p>',

    "2": '<p>The seated teacher in the temple courts fulfills the pattern of Isa 2:3 — instruction going forth from Zion\'s sanctuary to all who gather. The authoritative posture of the seated rabbi combined with the populace streaming to him anticipates the eschatological gathering the prophets described; Christ is in the place where Torah was taught, teaching what the Law pointed toward.</p>',

    "3": '<p>A revelation of God: the scribes and Pharisees place Christ in the role of judicial arbiter over a capital case. The Christological significance emerges from what follows — only the one who is himself without sin (v7; 46) has standing to judge the woman, and only the one who came not to condemn but to save (3:17) would exercise that standing as he does. The setup is a trap that reveals who Christ is by what he refuses to do.</p>',

    "4": '<p>A revelation of God: the accusers articulate the legal charge accurately but the trap imposes a false dilemma — uphold the law and condemn her, or show mercy and violate it. The Christological resolution neither abandons the law nor crushes the woman under it. Christ is the one who can hold law and grace together because he is both the lawgiver and the one who will bear the law\'s condemnation in her place.</p>',

    "5": '<p>The Mosaic command to stone adulterers (Lev 20:10; Deut 22:22) is the standard they cite. The Christological irony: Christ is the one through whom that law was given at Sinai, and also the one who came to fulfill rather than abolish it (Matt 5:17). The question "what do you say?" is the question the whole Gospel asks of him — and his answer will consistently exceed the framework in which it is put.</p>',

    "6": '<p>A revelation of God: Christ writes on the ground with his finger. The finger of God wrote the Law on stone tablets at Sinai (Exod 31:18); here the lawgiver writes in dirt — transient, not engraving — while the accusers, who brandish the stone law, are dispersed. The composure of Christ under pressure is itself the self-disclosure of the one who operates from a different order than the trap set for him.</p>',

    "7": '<p>A direct revelation: "let any one of you who is without sin be the first to throw a stone." The legal requirement of Deut 17:7 — witnesses throw the first stone — is met with a qualification only Christ himself satisfies. He is the only person present who, by his own criterion, could throw the stone. He chooses not to. This is 3:17 ("God did not send his Son to condemn the world") made concrete: the sinless judge declines to execute judgment on the sinner before him.</p>',

    "8": '<p>A revelation of God: the second act of writing on the ground, after the challenge of v7, creates the space for the accusers to reach their own verdict without Christ pronouncing it on them. The patience and restraint of the one who holds all judgment (5:22) — waiting while they process — is the divine composure that confounds the urgency of the trap.</p>',

    "9": '<p>A revelation of God: the accusers depart one by one, oldest first, until only Christ remains with the woman. The Christological structure is complete: those who claimed the authority to condemn cannot sustain it under scrutiny; the one who actually holds that authority (5:22, 27) remains. The irony is absolute — the judge who stays is the only one present who had the standing to condemn, and he will not.</p>',

    "10": '<p>A revelation of God: "where are they? Has no one condemned you?" The judge\'s inquiry establishes the legal situation — no witnesses remain to press the charge (Deut 17:6: no one is to be put to death on the testimony of only one witness). Christ speaks as the final arbiter whose verdict is the only one that matters. The question contains the answer; the scene has already absolved her by process of law.</p>',

    "11": '<p>A direct revelation: "neither do I condemn you — go and leave your life of sin." The one who could condemn chooses not to; the one who forgives commands a life turned from sin. This is 3:17 enacted as personal encounter: the Son came not to condemn the world but to save it. The divine forgiveness of Isa 43:25 ("I blot out your transgressions, for my own sake") is exercised by the Son in person — and paired with the prophetic call to repentance, neither suspending justice nor crushing the sinner under it.</p>',

    "12": '<p>A direct fulfillment: "I am the light of the world" names Christ as the Servant commissioned in Isa 42:6 ("a light for the Gentiles") and Isa 49:6 ("my salvation may reach to the ends of the earth"). The great light that Isaiah 9:2 promised to the people walking in darkness is not a future arrival — it is a present person. The Prologue has already identified Christ as the light shining in darkness (1:4–5, 9); here Christ claims the title directly, carrying the scope from Israel to "the world."</p><p>The promise "whoever follows me will never walk in darkness but will have the light of life" makes discipleship the condition of participation in what the Servant was sent to accomplish. The light is personal, not institutional — it belongs to following Christ, not to a place or rite.</p>',

    "13": '<p>A revelation of God: the Pharisees invoke the legal rule that self-testimony is invalid. The Christological response in the following verses — grounded in his knowledge of his own origin and destination — establishes that the ordinary epistemic rules do not govern the one who knows what no human witness can know. His testimony is not self-interested; it is the testimony of the one who has come from the Father and returns to him.</p>',

    "14": '<p>A revelation of God: "I know where I came from and where I am going." The heavenly origin and the destination that lies beyond the cross ground Christ\'s self-testimony in a knowledge no human court can possess. The ordinary two-witness rule governs human disputes where no single party has complete access to the truth; Christ speaks from a vantage that transcends that limit. He does not need corroborating witnesses for facts that only he knows from the inside.</p>',

    "15": '<p>A revelation of God: "you judge by human standards" (<em>kata tēn sarka</em>) — according to the flesh, by visible surface criteria. Christ does not judge by that standard. Isaiah\'s messianic king "will not judge by what he sees with his eyes, or decide by what he hears with his ears; but with righteousness he will judge" (Isa 11:3–4). The contrast between flesh-level evaluation and Spirit-equipped divine judgment is the difference between the accusers and the one they are judging.</p>',

    "16": '<p>A revelation of God: "I stand with the Father who sent me." Christ\'s judgment is valid because he is not a single human witness but the agent of the Father — the two standing together constitute the valid testimony the law requires. The Servant of Isa 50:8 declares "he who vindicates me is near"; the Son\'s vindication comes from the Father who sent him, whose presence alongside him means no verdict of human courts is final.</p>',

    "17": '<p>A revelation of God: Christ cites "your own Law" — Deut 19:15 (two witnesses) — and positions himself within it rather than above it. The Christological move is to meet the legal challenge from within the framework of Torah, demonstrating that the Law\'s own evidentiary standard is fulfilled at the highest possible register: himself and the Father. He does not bypass Torah; he inhabits it completely.</p>',

    "18": '<p>A direct revelation: "I am one who testifies for myself; my other witness is the Father who sent me." The two-witness requirement is satisfied by the Son and the Father — an unprecedented fulfillment of the Deut 19:15 standard. No human tribunal can subpoena the Father; no verdict that excludes his testimony is complete. The Christological claim is that human legal categories, applied to this case, lead to the conclusion the Pharisees are trying to avoid.</p>',

    "19": '<p>A revelation of God: "if you knew me, you would know my Father also." The epistemological claim runs through the Gospel: knowledge of God is only available through the Son (1:18; 14:9). The Pharisees\' question "where is your father?" reveals that they have not found the Father they claim to serve, because they have not recognized the Son through whom the Father is made known. Rejection of the Son is, simultaneously, ignorance of the Father.</p>',

    "20": '<p>A revelation of God: "his hour had not yet come." The passion timeline governs Christ\'s movements through the entire Gospel, and the Evangelist marks the moments when it almost runs out. No human power can arrest him before the appointed hour; no conspiracy can compress the schedule. The sovereignty of Christ over his own death — "I lay it down of my own accord" (10:18) — is what the "hour" language protects throughout.</p>',

    "21": '<p>A revelation of God: "you will die in your sin." The departure of Christ and the consequence of refusing him are joined: where he goes, they cannot follow — not because of a geographic barrier but because they have not received the one who is the way (14:6). The Ezekielian formula of dying in sin (Ezek 3:18; 33:8) — used of those who reject the appointed watchman\'s word — is applied to the rejection of Christ himself as the final prophet and more than a prophet.</p>',

    "22": '<p>A revelation of God: the leaders\' misunderstanding ("will he kill himself?") reflects the recurring Johannine pattern — Christ\'s statements about his death are heard only on the literal surface. They cannot imagine that he goes where they cannot follow because his death will be given freely at the appointed hour, not seized by them on their terms. The misunderstanding preserves the Christological irony: their understanding of death cannot accommodate the one who will lay down his life and take it up again (10:17–18).</p>',

    "23": '<p>A revelation of God: "I am from above; I am not of this world." The ontological claim grounds the epistemological gap the chapter has been exposing. The crowd judges by standards from below; Christ speaks from above. The contrast is not between good people and bad but between two orders of origin — and Christ\'s origin from above is what gives his words about heavenly things the authority of direct witness (3:12–13).</p>',

    "24": '<p>A direct revelation: "if you do not believe that <em>egō eimi</em>, you will die in your sins." The absolute ego eimi without a predicate is the divine name formula of Deutero-Isaiah — "so that you may know and believe me and understand that I am he" (Isa 43:10, LXX: <em>egō eimi</em>; also 43:13, 25; 45:18; 46:4; 48:12) — and of Deuteronomy\'s Song of Moses (Deut 32:39). Life or death hinge on this identity: whether the one speaking is who he claims to be. This is the Gospel\'s kerygmatic claim in its starkest form (20:31).</p>',

    "25": '<p>A revelation of God: "just what I have been telling you from the beginning." Christ\'s self-revelation has been consistent since the Prologue. He has not shifted his claims; the audience has not heard them. The consistency of his self-witness from 1:1 onward is itself a Christological claim — there is no version of Jesus that does not make these assertions, no earlier, simpler layer beneath the divine-name claims.</p>',

    "26": '<p>A revelation of God: "he who sent me is trustworthy." The warrant for Christ\'s speaking is the faithfulness of the Father — the covenant-loyal God whose <em>ʾemûnāh</em> underwrites every word his agent delivers. The Christological mission is grounded not in Christ\'s own credibility but in the God whose character is the ultimate guarantee. The world is told what the Father tells; the message is trustworthy because the sender is.</p>',

    "27": '<p>A revelation of God: "they did not understand that he was telling them about his Father." The Evangelist\'s parenthetical note exposes the depth of the incomprehension: they heard "the one who sent me" and could not identify who that was. The entire theological argument of chapter 8 — Father and Son, origin and destination, judgment and testimony — was spoken to people who had no framework for hearing it. The revelation was present; the capacity to receive it was absent.</p>',

    "28": '<p>A direct type fulfilled: "when you have lifted up the Son of Man, then you will know that I am he." The crucifixion is simultaneously execution and revelation — the moment when the divine name becomes undeniable. <em>Hypsōthēnai</em> (to be lifted up) carries both senses: physically raised on the cross and exalted in glory, as in Isa 52:13 ("my servant will be raised and lifted up and highly exalted"). The logic of the verse follows Isa 43:10 — "so that you may know that I am he" — making the cross the revelatory event that fulfills both the Servant\'s exaltation and the divine self-disclosure formula.</p>',

    "29": '<p>A revelation of God: "he has not left me alone, for I always do what pleases him." The perfect obedience of the Son to the Father — the disposition that will culminate in "not my will, but yours" at Gethsemane (Luke 22:42) and "it is finished" at the cross (19:30). This is the Servant of Isa 42:1 in whom the Father\'s soul delights, the one chosen and commissioned whose obedience runs from the beginning of his mission to its completion. The Father\'s abiding presence is the fruit of the Son\'s unbroken fidelity.</p>',

    "30": '<p>A revelation of God: "even as he spoke, many believed in him." The Evangelist marks the faith-response generated by the divine-name exchange and the crucifixion announcement. The word about who Christ is and what he will do produces belief even in a hostile audience. The pattern runs through the Gospel: the word about Christ is never without effect (cf. Isa 55:11 — the word does not return empty); some harden, some believe, but the word does not fail.</p>',

    "31": '<p>A revelation of God: true discipleship is defined as holding to Christ\'s teaching — abiding in his word. The covenant-loyalty test the prophets applied to Israel (Deut 5:29 — "that their hearts would be inclined to fear me and keep my commands") is here applied to response to Christ. Discipleship is not momentary assent but sustained residence in the word. The "really my disciples" (<em>alēthōs</em>) distinguishes genuine from sign-faith reception, a concern the Evangelist has maintained since 2:23–25.</p>',

    "32": '<p>A direct revelation: "the truth will set you free." The truth is not merely propositional — Christ will identify himself as the truth (14:6: "I am the way, the truth, and the life"). Knowing the truth is therefore knowing Christ; the freedom it produces is liberation from the slavery he is about to name (v34). The wisdom tradition\'s connection between knowing God\'s way and walking in freedom (Ps 119:45) finds its personal embodiment: the truth that liberates is a person, not a principle.</p>',

    "33": '<p>A revelation of God: the crowd\'s insistence — "we are Abraham\'s descendants and have never been slaves" — contradicts the entire Exodus narrative (their ancestors were enslaved in Egypt), the Babylonian exile, and their present condition under Rome. The deeper slavery Christ is about to name (v34) is the one no genealogy can address. Abrahamic descent does not confer the freedom of Abraham\'s children; it only establishes the lineage through which the promise would come — and that promise is standing before them, unrecognized.</p>',

    "34": '<p>A revelation of God: "everyone who sins is a slave to sin." The Christological implication is immediate: the only one in this conversation who is not a slave to sin is Christ himself (v46; Isa 53:9; 2 Cor 5:21). His freedom is not the freedom of the law-observer who has managed obedience, but the constitutive freedom of the sinless one. He can liberate others from sin-slavery because he alone stands outside it — and he stands outside it precisely in order to stand inside our condemnation in our place.</p>',

    "35": '<p>A revelation of God: "a slave has no permanent place in the family, but a son belongs to it forever." The allusion to Gen 21:10 (Sarah dismissing Hagar and Ishmael — the slave cannot share the inheritance with the son) establishes the ontological difference between the slave\'s condition and the son\'s. Christ as the Son belongs to the Father\'s household permanently; those he liberates (v36) are incorporated into that permanent sonship, not into a temporary or conditional arrangement.</p>',

    "36": '<p>A fulfillment: "if the Son sets you free, you will be free indeed." The jubilee proclamation of Isa 61:1 — the anointed one declaring "freedom for the captives" — arrives in the person of the Son. The freedom the jubilee offered cyclically every fifty years, and which the law\'s release mechanisms provided temporarily, is now offered permanently and ontologically. The Son\'s liberation is not a legal maneuver but a change of nature: from slave to son, which is what the new birth of 3:3–8 described from another angle.</p>',

    "37": '<p>A revelation of God: "you are looking for a way to kill me, because you have no room for my word." The murderous intent toward Christ is the defining symptom of the father-relationship he will name in v44. Jeremiah faced the same pattern — those who plotted against the prophet who brought God\'s word to them (Jer 11:19; 18:18). Christ identifies the rejection of his word as the root of the homicidal impulse; the desire to silence him is the desire to silence the word he carries from the Father.</p>',

    "38": '<p>A revelation of God: "I am telling you what I have seen in the Father\'s presence, and you are doing what you have heard from your father." The contrast sets up the paternity question the rest of the chapter will press. Christ speaks from direct vision of the Father; they act from the instruction of a different father (v44). The Christological claim is that his words are not opinions or interpretations but the direct transcript of what he has seen in the divine presence — the one who exists in the Father\'s bosom (1:18) speaks what he knows from there.</p>',

    "39": '<p>A revelation of God: "if you were Abraham\'s children, you would do what Abraham did." The criterion for Abrahamic descent is not genealogy but conduct — specifically, Abraham\'s disposition to receive the messengers God sent (Gen 18:2–8; Heb 11:8–19). God commissioned Abraham to direct his household "to keep the way of the LORD by doing what is right and just" (Gen 18:19). The crowd\'s desire to kill the one God sent is the exact inversion of what Abraham modeled. Conduct reveals father; conduct exposes them.</p>',

    "40": '<p>A revelation of God: "you are looking for a way to kill me, a man who has told you the truth that I heard from God." Christ presents himself simultaneously as the truthful messenger and the target of murder — the pattern of the rejected prophet, but deeper: the truth he tells is not his own but God\'s, which means rejecting him is rejecting God\'s own word about himself. The paradox is that a God-fearing people who claim to reject blasphemy are trying to murder the one through whom God speaks most directly.</p>',

    "41": '<p>A revelation of God: "the only Father we have is God himself." The crowd\'s escalating claim inverts the logic of the passage — they claim divine fatherhood while rejecting the Son whom the Father sent. The implicit accusation against Jesus (illegitimate birth, the slur behind "we are not illegitimate") is met by what follows: the real question of illegitimacy is not about birth certificates but about whether one\'s conduct is consistent with the Father one claims. The crowd\'s claim fails on its own terms.</p>',

    "42": '<p>A direct revelation: "if God were your Father, you would love me, for I have come here from God." The Christological test is stated with full clarity: love for the Son is the proof of the Father relationship. The Father loves the Son (3:35; 5:20; 17:24); those who belong to the Father are drawn into that love and therefore love what the Father loves. The crowd\'s hostility toward Christ is not a secondary failure but the primary indicator that their claimed Father-relationship is not what they assert it to be.</p>',

    "43": '<p>A fulfillment: "you are unable to hear what I say." The language of judicial inability to hear echoes Isaiah\'s commissioning — "be ever hearing but never understanding" (Isa 6:9) — which the NT consistently applies to those who reject the prophetic word (Mark 4:12; Acts 28:26–27). The crowd\'s failure to understand Christ\'s language is not intellectual failure that better explanation could fix; it is the covenantal consequence of the prior disposition of their will, the hardening that Israel\'s history of prophetic rejection has produced.</p>',

    "44": '<p>A revelation of God: "you belong to your father, the devil." The identification reveals who Christ is by antithesis: the devil is a murderer from the beginning (Gen 4; the death introduced through the serpent\'s lie in Gen 3:4) and the father of lies (Gen 3:4 — "you will not certainly die"). Christ is, in every particular, the opposite: the one who comes to give life abundantly (10:10), the way, the truth, and the life (14:6). He is truth; the devil is the father of lies. He is life; the devil is a murderer. The crowd\'s embrace of murder and rejection of truth locates their paternity.</p>',

    "45": '<p>A revelation of God: "yet because I tell the truth, you do not believe me." The paradox exposes the depth of the problem. Those who belong to the father of lies cannot receive the one who is truth; their alienation from truth is constitutive, not accidental. This is the Johannine equivalent of the Synoptic parable of the soils — the word about Christ that falls on certain hearts finds no purchase not because of deficiencies in the word but because of the character of the soil. Truth itself becomes the occasion of rejection by those whose father is the deceiver.</p>',

    "46": '<p>A direct fulfillment: "can any of you prove me guilty of sin?" The challenge claims sinlessness — the precise attribute the Servant of Isaiah 53:9 embodies: "he had done no violence, nor was any deceit in his mouth." Christ\'s sinlessness is not incidental to his identity but constitutive of his role: only the one who has no sin of his own can bear the sin of others (2 Cor 5:21; Heb 4:15; 1 Pet 2:22; 1 John 3:5). The challenge is unanswered in silence — no charge can be sustained. His sinlessness and the world\'s inability to disprove it is the legal ground on which the substitutionary atonement rests.</p>',

    "47": '<p>A revelation of God: "whoever belongs to God hears what God says." The Christological test runs consistently through the Gospel — response to Christ is the indicator of one\'s relationship to God (1:11–12; 10:27). The Mosaic promise of Deut 18:15 — "you must listen to him" — was the command to receive the prophet God sends; refusal to hear Christ is the definitive failure to listen to the prophet Moses promised. The diagnosis is total: they do not hear because they do not belong to God.</p>',

    "48": '<p>A revelation of God: calling Christ "a Samaritan and demon-possessed" is the ultimate delegitimization available to the crowd — placing him outside true Israelite religion and under demonic influence simultaneously. The Christological irony is dense: the Lord of Israel is dismissed as a Samaritan apostate (2 Kgs 17); the one through whom the Spirit was given without measure (3:34) is accused of demon possession. The accusations reveal the accusers\' bankruptcy — they have no argument left, only insult.</p>',

    "49": '<p>A revelation of God: "I honor my Father and you dishonor me." The Christological inversion of Mal 1:6 ("where is the honor due me?") — a rebuke addressed to Israel for honoring God with corrupted worship. The Son\'s honoring of the Father is perfect; the crowd\'s response to the Son is dishonor, which simultaneously dishonors the Father who sent him. The chain of honor and dishonor in the fourth Gospel runs from the Father through the Son to those who receive or reject him.</p>',

    "50": '<p>A revelation of God: "I am not seeking glory for myself; but there is one who seeks it, and he is the judge." The Father\'s seeking of the Son\'s glory and the Son\'s refusal to glorify himself is the pattern of their relationship throughout the Gospel (5:41; 7:18; 17:1). The Christological significance: the one who does not seek his own glory will be glorified by the Father — and that glorification is the verdict of the judge. The cross, which looks like shame, is the Father\'s moment of glorifying the Son (12:23; 13:31). The judge\'s verdict overturns the crowd\'s.</p>',

    "51": '<p>A direct revelation: "whoever obeys my word will never see death." The structural reversal of Gen 2:17 — disobedience to God\'s word brought death into the human story; obedience to Christ\'s word abolishes it. Christ does not merely postpone death or promise comfort at death; he claims authority over death itself. This is the same claim John 11 will dramatize over Lazarus\'s tomb: the one who makes this promise will demonstrate it in the most visible possible way, before his own death and resurrection make it definitive.</p>',

    "52": '<p>A revelation of God: the crowd\'s objection — "Abraham died, and so did the prophets; yet you say whoever obeys your word will never taste death" — confirms they are hearing only on the physical level. The Christological distinction they cannot access: Christ is not promising the prevention of physical death but the conquest of the death that matters — the separation from God that physical death seals for those outside him. Physical death remains for his followers (Lazarus will die again); the power of death over the beloved is what has been broken.</p>',

    "53": '<p>A revelation of God: "are you greater than our father Abraham?" The question anticipates a negative answer from someone making an outrageous comparison — and receives an implicit yes in everything that follows. The same structure governs 4:12 (Jacob\'s well) and will recur at every point where the Evangelist places Christ against the patriarchs. He is greater — not as an ego claim but as the consequence of what "before Abraham was born, I am" (v58) actually means.</p>',

    "54": '<p>A revelation of God: "my Father, whom you claim as your God, is the one who glorifies me." The Christological point is targeted: they appeal to the God who, by their own claim, is the God who glorifies Christ. Their system of appeals runs directly to the one whose verdict against them is declared by the one they reject. The God they invoke as their own is the one who will vindicate his Son against those who seek to kill him.</p>',

    "55": '<p>A revelation of God: "though you do not know him, I know him." The exclusive knowledge of the Son — announced in the Prologue (1:18: the one in the Father\'s bosom has made him known) — is stated here in personal terms. The crowd\'s claim to know God is measured against Christ\'s intimate, direct knowledge: he knows the Father as the Father knows him (10:15). Their God-knowledge passes through their Scriptures and traditions; his passes through the eternal communion of the Son with the Father.</p>',

    "56": '<p>A type: "your father Abraham rejoiced at the thought of seeing my day; he saw it and was glad." Abraham\'s vision of Christ\'s day is most precisely located in the Akedah — where the mountain of the Lord was named "the LORD Will Provide" and the narrator added: "on the mountain of the LORD it will be seen/provided" (Gen 22:14). What Abraham saw structurally was the sacrifice of the true Son in place of the human son — the divine provision of the substitutionary victim. The Evangelist claims that Abraham\'s faith was not merely trust in a promise but perception of the specific event toward which the promise pointed.</p>',

    "57": '<p>A revelation of God: the crowd can only hear "seen Abraham" in chronological terms — as a claim about long life. They cannot access the ontological register in which the sentence operates. Their objection "you are not yet fifty years old" already misses the point: Christ is not claiming to have been very old when Abraham was alive but to exist in a different category from time-bound creatures entirely. The misunderstanding creates the space for v58\'s clarification.</p>',

    "58": '<p>A direct revelation: "before Abraham was born, I am." The supreme Christological claim of the chapter — and one of the highest in the Gospel. The present tense "I am" (<em>egō eimi</em>) is set against the past tense "before Abraham was born," which is itself an understatement: the absolute "I am" without predicate is the formula of divine self-identification from Exod 3:14 ("I AM WHO I AM / I AM has sent me") and the repeated Deutero-Isaiah formula (Isa 43:10, 13, 25; 45:18; 46:4; 48:12) — Yahweh\'s exclusive self-declaration that he exists without beginning, eternally prior to all things. Christ does not say "I was before Abraham" (which would claim long pre-existence) but "I am" — the eternal present that belongs to the divine name alone. The stoning response of v59 confirms the crowd heard it precisely as a claim to the divine name.</p>',

    "59": '<p>A direct revelation confirmed by response: the crowd immediately picks up stones for blasphemy — the mandated punishment under Lev 24:16 for anyone who "blasphemes the name of the LORD." Their legal instinct is not wrong. They correctly identified that Jesus had claimed the divine name; what they deny is its truth. Their response is the same one the trial will reproduce (Mark 14:61–64): the claim to divine identity is the charge, and it is not refuted, only rejected. Christ withdraws — not because the hour has come but because it has not. The one who said "no one takes my life from me" (10:18) slips away at his own discretion, preserving the divine sovereignty over his death that has governed every scene since 7:30.</p>'
  }
}


def main():
    existing = load_comm('mkt-christ', 'john')
    merge_comm(existing, JOHN)
    save_comm('mkt-christ', 'john', existing)
    print('John 8 mkt-christ written.')

if __name__ == '__main__':
    main()
