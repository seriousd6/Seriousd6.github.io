"""
mkt-christ layer — 2 Corinthians chapters 1–5
Output: data/commentary/mkt-christ/2corinthians.json
Run: python3 scripts/zc-christ-2corinthians-1-5.py

Christological spine: Christ as Yes to all promises (1:20), the apostle's
comfort as participation in Christ's sufferings, new covenant minister (3:6),
image of God who transforms beholders (3:18), treasure in clay (4:6-7),
the great exchange (5:21), new creation in Christ (5:17).
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
  "1": {
    "1": "<p>Paul's apostleship is by the will of God — the crucified and risen Christ who commissioned him on the Damascus road. This letter's entire christological argument rests on Paul's identity as a servant of the suffering Christ; his authority is inseparable from his pattern of weakness and endurance.</p>",
    "2": "<p>Grace and peace from God our Father and the Lord Jesus Christ — the Pauline greeting binds the peace Christ purchased at the cross (Rom 5:1; Col 1:20) to every opening of this intensely pastoral letter. The dual source (Father and Son) is Paul's binitarian shorthand for the God revealed in Christ.</p>",
    "3": "<p>The God of all comfort is named the Father of our Lord Jesus Christ — Jesus is the definitive disclosure of the merciful Father (John 14:9). The God who comforts is the God who sent the Comforter (John 14:16); apostolic consolation is the Spirit of the risen Christ mediated through suffering servants.</p>",
    "4": "<p>Comfort flows through shared suffering: God comforts Paul so Paul can comfort the Corinthians. The cruciform economy of grace — Christ's suffering becomes our salvation; our suffering in Christ becomes others' strength — is already operating in the letter's opening verses.</p>",
    "5": "<p>The participatory structure of the apostolic life: as Christ's own pathemata (sufferings) overflow into the apostle's experience (Col 1:24: filling up what is lacking in Christ's afflictions for the sake of his body), so Christ's comfort overflows in equal measure. The paschal pattern governs the whole.</p>",
    "6": "<p>The directional movement of suffering — affliction received, comfort given — mirrors the pro nobis structure of the cross. As Christ's death was for us, apostolic suffering is for the congregation; the cruciform pattern extends through the body into every member's experience.</p>",
    "7": "<p>The eschatological certainty is christological: those who share in Christ's sufferings will share in his glory (Rom 8:17). The Corinthians' participation in Paul's suffering is their participation in the paschal mystery — cross first, then resurrection.</p>",
    "8": "<p>Paul's transparency about the Asian affliction is itself a christological act. The Lord who concealed nothing from his disciples (John 15:15) shapes an apostle who hides nothing from his congregation; suffering shared is suffering redeemed.</p>",
    "9": "<p>The death-sentence imposed on Paul drove him to the God who raises the dead — the resurrection is not merely theological conviction but practical resource. The God who raised Jesus from the dead is the apostle's actual ground of confidence in extremity.</p>",
    "10": "<p>The triple tense of deliverance (delivered/delivers/will deliver) mirrors the Easter proclamation: he has risen, he lives, he will come. Every apostolic rescue is a micro-resurrection, a partial realization of the resurrection that awaits.</p>",
    "11": "<p>The community of the risen Christ prays together because the risen Lord himself intercedes (Rom 8:34; Heb 7:25). Apostolic deliverance comes through the corporate intercession of Christ's body; prayer is the mechanism of resurrection-power distribution.</p>",
    "12": "<p>Apostolic transparency mirrors the character of the incarnate Christ who concealed nothing (John 18:20-21). Paul's integrity is the embodiment of the cruciform mind that seeks nothing for itself — the ethical implication of the cross applied to apostolic conduct.</p>",
    "13": "<p>Plain speech as a christological commitment: the Word became flesh and dwelt plainly among us (John 1:14). The apostle who preaches the unambiguous Christ speaks without concealment. Christ is the end of all opacity.</p>",
    "14": "<p>The day of the Lord Jesus frames all present evaluations. At the parousia, the risen Judge will reveal what is genuine; the mutual boasting of apostle and congregation on that day will be the eschatological vindication of the cruciform ministry.</p>",
    "15": "<p>Even Paul's travel plans are shaped by pastoral benefit for the congregation, not personal advantage. The cruciform mind (Phil 2:4: let each of you look not only to his own interests but also to the interests of others) governs the apostle's movements.</p>",
    "16": "<p>The double visit expressed double grace: the God who gives abundantly (2 Cor 9:8) gives through an apostle who comes and comes again. Apostolic visitation is an extension of Christ's own coming to his people.</p>",
    "17": "<p>The charge of fickleness would contradict the nature of the gospel Paul preaches. A yes-and-no apostle could not credibly proclaim the unchanging Christ who is the same yesterday, today, and forever (Heb 13:8).</p>",
    "18": "<p>The divine faithfulness (pistos ho theos) is the model for and guarantee of apostolic trustworthiness. God's character in Christ — the faithful God who keeps covenant — is the ground from which Paul argues his own consistency.</p>",
    "19": "<p>Jesus Christ, proclaimed among the Corinthians, was not Yes and No but in him it is always Yes — the risen Lord is the eternal Yes of God to all his purposes. The apostle who preaches this Yes cannot himself be double-minded; the message shapes and demands consistency in the messenger.</p>",
    "21": "<p>The anointing (chrisas, from chrio) connects believers to Christ the Anointed One. Every believer shares the Messiah's consecration; the body participates in the Head's anointing. This is the christological basis of the priesthood of all believers.</p>",
    "22": "<p>The Spirit as arrabōn (down-payment) points to the full inheritance Christ secured. The seal of the Spirit is the Father's signature on what the Son purchased; the guarantee is the first installment of the resurrection life that will culminate in the redemption of the body.</p>",
    "23": "<p>The apostle appeals to the divine Judge — the same God who vindicated Christ in the resurrection — as witness to his motives. Paul is transparent before the one who raised Jesus; his conduct is lived coram Deo (before God).</p>",
    "24": "<p>The cruciform model of authority: Jesus came not to be served but to serve and give his life (Mark 10:45). The apostle who preaches the servant-Lord cannot lord it over the congregation; he works with them for their joy.</p>",
  },
  "2": {
    "1": "<p>The painful visit and the apostle's decision not to repeat it reflect cruciform pastoral wisdom — not self-protection but care for the congregation's formation. The goal is the Corinthians' joy, which is ultimately joy in Christ.</p>",
    "2": "<p>Apostolic joy is inseparable from the congregation's joy — a body-of-Christ reality. The head suffers with every member (1 Cor 12:26); the apostle's gladness and grief are bound up with those he serves.</p>",
    "3": "<p>The tearful letter was an act of cruciform love, not administrative authority. The Lord who wept over Jerusalem (Luke 19:41) shapes an apostle who writes in tears for the congregation's sake rather than sparing himself the pain.</p>",
    "4": "<p>The apostle's tears echo the weeping Savior (John 11:35; Heb 5:7: with loud cries and tears). Cruciform ministry carries the emotional weight of the Christ who suffered; the apostle's anguish of heart is a participation in the compassionate heart of Christ.</p>",
    "5": "<p>The offense against the apostle wounds the whole body of Christ at Corinth. The one who causes pain has not merely insulted Paul but harmed the community that is Christ's presence in that city.</p>",
    "6": "<p>The community discipline has served its healing purpose and must stop before it destroys the one Christ died to save. Like the physician who removes the treatment when healing begins, the congregation follows Christ's own restorative purpose in discipline (Heb 12:5-11).</p>",
    "7": "<p>The risk of over-punishment is that it destroys the very person for whom Christ shed his blood. The imperative to forgive and comfort the offender is grounded in the value that God places on every human being: Christ died for this one too.</p>",
    "8": "<p>The official act of love-reaffirmation ratifies the community's care for the restored member. As God ratified the new covenant in Christ's blood, the congregation ratifies its love in concrete communal action.</p>",
    "9": "<p>Apostolic obedience is finally obedience to Christ himself (v.10: in the presence of Christ). The Corinthians' response to Paul's letter tests their response to the Lord who sent him — the apostle and the Lord are not separable in this delegation structure (John 13:20).</p>",
    "10": "<p>The apostolic forgiveness pronounced in the presence of Christ mirrors the risen Christ's own authority (John 20:23: if you forgive the sins of anyone, they are forgiven). Paul is the instrument; the risen Christ is the agent through whom the forgiveness is real.</p>",
    "11": "<p>Satan's strategy is division, accusation, and unforgiveness. The cross defeated the accuser (Rev 12:10-11); the community that forgives lives out the victory of Calvary against the schemes of the one Christ has already overcome.</p>",
    "12": "<p>The open door for the gospel is the risen Christ's initiative (Rev 3:7-8: the one who holds the key of David opens what no one shuts). Every missionary opportunity is the risen Lord's gift; apostolic mission is the extension of Christ's own sending.</p>",
    "13": "<p>Even in apostolic anxiety, the pastoral network of trust (Titus as Paul's emissary) reflects the body of Christ functioning in mutual care. The community of the resurrection is also the community of mutual dependence and concern.</p>",
    "14": "<p>God leads Paul in the triumphus of the risen Christ — the victory belongs to God; the apostle participates as a captive-turned-soldier in the procession of the Victor who has conquered sin, death, and the powers. The resurrection is the triumph; apostolic mission is its ongoing public display throughout the world.</p>",
    "15": "<p>The apostle's life, patterned on the crucified and risen Christ, is itself a fragrant offering to God (Eph 5:2: Christ loved us and gave himself up for us, a fragrant offering and sacrifice to God). As Christ's self-offering was the supreme aroma of worship, so the apostolic life participates in that offering.</p>",
    "16": "<p>The cross divides: to those perishing it is folly, to those being saved it is the power of God (1 Cor 1:18). The proclamation of Christ crucified produces diametrically opposite responses — not because the message changes but because hearers are differently oriented toward God.</p>",
    "17": "<p>Speaking in Christ (en Christo) means speaking within the covenant relationship Christ has established, with the full weight of that commission. The sincere apostle has been commissioned by the God who revealed himself definitively in Christ; his words are not his own but carry the authority of the one who sent him.</p>",
  },
  "3": {
    "1": "<p>The entire system of self-commendation is challenged by the christological reality: Christ commended himself not through letters but through the cross — the ultimate demonstration of love (Rom 5:8). The apostle who shares that pattern needs no other credential.</p>",
    "2": "<p>The Corinthian congregation is the letter written on Paul's heart — the embodied proof of the gospel's power. The community shaped by the Spirit of the risen Christ is more reliable testimony than any papyrus letter of recommendation.</p>",
    "3": "<p>Christ is the author of this living letter; Paul is the courier. The Spirit who raised Jesus from the dead (Rom 8:11) is the ink that writes resurrection life on human hearts. The contrast of stone tablets and heart-tablets is Ezekiel 36:26-27 fulfilled: a heart of flesh, my Spirit within you — the new covenant's anthropological transformation accomplished in Christ.</p>",
    "4": "<p>All apostolic confidence is christologically mediated — through Christ (dia Christou) toward God. Paul has no standing before God apart from Christ; through the Son he approaches the Father (Eph 2:18: through him we both have access in one Spirit to the Father).</p>",
    "5": "<p>The sufficiency (hikanotes) is entirely derivative: apart from me you can do nothing (John 15:5). The apostle's fruitfulness is a participation in Christ's own life and power through the Spirit — nothing originates in Paul himself.</p>",
    "6": "<p>The new covenant inaugurated at the Last Supper (1 Cor 11:25: this cup is the new covenant in my blood) is the foundation of apostolic ministry. The letter kills: the law reveals and condemns sin. The Spirit gives life: the resurrection transforms condemned sinners into new-creation beings.</p>",
    "7": "<p>The Mosaic glory was real and delegated — derived from a theophany that itself pointed forward to the greater glory of the incarnation. The Torah's glory is not denied but relativized by the surpassing glory of Christ, the fullness of divine disclosure.</p>",
    "8": "<p>The Spirit poured out at Pentecost (Acts 2:33) is the eschatological gift of the new age, the presence of the risen Christ in and among his people. The ministry that mediates this Spirit-life surpasses the ministry that could only reveal sin's condemnation.</p>",
    "9": "<p>The righteousness of God has been revealed in the gospel (Rom 1:17; 3:21-22) — in the crucified and risen Christ who is our righteousness (1 Cor 1:30). The new covenant ministry mediates divine righteousness imputed through faith; the old could only condemn.</p>",
    "10": "<p>The incarnation is the surpassing glory: the Word became flesh and we beheld his glory (John 1:14). The Torah's glory, real and true, points toward and is eclipsed by the glory of the Son who is the radiance of the Father's glory (Heb 1:3).</p>",
    "11": "<p>The permanent (menon) is the new covenant established in the unending priesthood of the risen Christ (Heb 7:24-25: because he continues forever, he holds his priesthood permanently). What is fading is replaced not by nothingness but by the eternal permanence of Christ's priestly mediation.</p>",
    "12": "<p>The boldness (parresia) of the new covenant minister reflects the access to God secured by Christ (Heb 4:16: with confidence draw near to the throne of grace). The veil of Sinai has been removed by the cross; the way into the holiest is permanently open.</p>",
    "13": "<p>Moses's veil prefigures the temple veil torn at the crucifixion (Mark 15:38). Moses covered temporary, fading glory; Christ's death removed the barrier separating humanity from God's presence — permanently and definitively.</p>",
    "14": "<p>The christological hermeneutical key: only in Christ is the veil over the OT removed. The risen Christ who opened the scriptures to the disciples on the road (Luke 24:27, 45) is the one who enables right reading of Moses. All that Moses wrote was about him (John 5:46).</p>",
    "15": "<p>The veil lies not on the text but on the heart that reads it without the risen Christ. The same scriptures that are veiled to the unbelieving heart are unveiled to the one who has turned to the Lord — the difference is not in the text but in the reader's relationship to Christ.</p>",
    "16": "<p>The turning (epistrepho) to the Lord is conversion to the risen Christ who is Lord. The same Lord who opened the scriptures on Easter evening (Luke 24:45: he opened their minds to understand the scriptures) removes the veil from every heart that turns to him in faith.</p>",
    "17": "<p>The freedom purchased by Christ (Gal 5:1: for freedom Christ has set us free) is the Spirit's gift and the new covenant's characteristic. The Spirit of the risen Lord liberates from condemnation (Rom 8:1-2), from the fear of death, and from the power of self.</p>",
  },
  "4": {
    "1": "<p>The apostle's perseverance is grounded not in personal resilience but in the mercy (eleos) that constitutes the ministry. Christ the merciful high priest (Heb 2:17) is both the source and the model: he endured the cross for the joy set before him (Heb 12:2), so the apostle does not lose heart.</p>",
    "2": "<p>Apostolic transparency mirrors the incarnation's plainness: Christ did not commend himself through clever rhetoric but through self-giving love (1 Cor 2:1-5). Renouncing underhanded ways is the apostle's participation in the character of the one who concealed nothing.</p>",
    "3": "<p>The veil remains over those who reject the crucified Christ. The stumbling block of the cross (1 Cor 1:23) is the veil; those who will not bow before the crucified King cannot see the glory that shines in his face.</p>",
    "4": "<p>Christ is the eikōn tou theou (image of God — Col 1:15), the one in whom the invisible God becomes fully visible (John 14:9). Satan's blinding strategy aims at preventing the unveiling of this image; the incarnation and resurrection are God's definitive unveiling of himself in the face of his Son.</p>",
    "5": "<p>The proclamation of Christ as kyrios (Lord) is the Easter confession (Phil 2:11: Jesus Christ is Lord, to the glory of God the Father). The apostle's entire task is derivative: he witnesses to the risen Lord, not to himself. Self-proclamation would be a fundamental misunderstanding of the mission.</p>",
    "7": "<p>The treasure is Christ himself dwelling in the apostle (Col 1:27: Christ in you, the hope of glory). The clay jar conceals and reveals simultaneously: the weakness of the vessel contrasts with the power of its content, showing unmistakably that the resurrection power is divine, not human.</p>",
    "8": "<p>Each antithesis in vv.8-9 is a death-and-resurrection moment: pressed but not crushed, perplexed but not despairing. The limit that is never crossed is the limit the risen Christ holds — the same Christ who bore death itself without being consumed by it.</p>",
    "9": "<p>The apostle is never forsaken because Christ bore that forsakenness at Golgotha (Matt 27:46: My God, my God, why have you forsaken me?). The striking down that does not destroy is the apostle's participation in the Easter pattern: crucified but raised, down but not out.</p>",
    "10": "<p>The two movements of the paschal mystery are enacted simultaneously in the apostle's body: the dying of Jesus (nekrosis — real physical suffering) and the life of Jesus (resurrection power manifested through that dying). The cross and the empty tomb are both on display in apostolic ministry.</p>",
    "11": "<p>Death first, then life — the paschal sequence is the apostolic pattern. The mortal flesh (thnete sarx) is the precise location where resurrection power operates, guaranteeing that the glory belongs entirely to God and not to the vessel.</p>",
    "12": "<p>The apostle's death-in-body generates life in the congregation — the cruciform dynamic of Christian ministry. As Christ's death generates life for the world, apostolic suffering generates life for the church. This is not coincidental but structurally necessary to the cross-shaped mission.</p>",
    "13": "<p>Psalm 116:10 (LXX: I believed, therefore I spoke) is read as the apostle's own confession and as an echo of Christ's own trust through the cross. The psalmist gave thanks for deliverance from death; Paul identifies with that trust-in-death and with the resurrection that followed.</p>",
    "14": "<p>The resurrection of Jesus is the guarantee of the apostle's resurrection — the same power that raised Christ from the dead will raise those who are in him (Rom 8:11). The final gathering before God is the eschatological completion of the body-of-Christ unity that already exists.</p>",
    "15": "<p>The extension of grace is the fruit of the cruciform pattern. As Christ's death was for all (5:14-15), so the apostle's suffering is for the congregation; the multiplication of grace through suffering produces an ever-expanding chorus of thanksgiving, gloria in excelsis.</p>",
    "16": "<p>The outer wasting is the dying of Jesus carried in the body; the inner renewal is the Spirit's resurrection work (Rom 8:10-11: if Christ is in you, though the body is dead, the Spirit gives life). The daily renewal is the Spirit progressively enacting the resurrection life that will be fully revealed at the last day.</p>",
    "17": "<p>The affliction is light not by denial but by comparison with the eschatological glory — the Christ-conforming transformation of the resurrection body (Phil 3:21: he will transform our lowly body to be like his glorious body; 1 Cor 15:43: raised in glory). Present suffering is the path toward that sharing in Christ's own resurrection glory.</p>",
    "18": "<p>The unseen things are the risen and ascended Christ, the coming kingdom, and the resurrection life. Faith is the conviction of things not seen (Heb 11:1); the apostle's endurance is sustained by the vision of what Christ's resurrection has already secured and what his parousia will fully reveal.</p>",
  },
  "5": {
    "1": "<p>The house not made with hands (oikodomēn acheiropoieton) echoes Christ's promise to build a temple not made with hands (Mark 14:58; John 2:19-21: the temple he spoke of was his body). The resurrection body is the ultimate temple — the dwelling place of the Spirit without the limitations of mortality, the fulfillment of what every OT sanctuary pointed toward.</p>",
    "2": "<p>The groaning for the heavenly dwelling joins the groaning of creation (Rom 8:22) and the inward groaning of the Spirit (Rom 8:23: as we await the redemption of our bodies). The resurrection body is the completion of Christ's redemptive work in its full physical dimension.</p>",
    "3": "<p>The clothing metaphor for the resurrection body echoes 1 Corinthians 15:53-54: this mortal must put on immortality. Christ's resurrection body is the prototype; those in him will be clothed with the same imperishable life, not left in the nakedness of disembodied existence.</p>",
    "4": "<p>Death swallowed up in victory (1 Cor 15:54 citing Isa 25:8) is the resurrection's definitive triumph — not escape from the body but its transformation into immortality. The swallowing of mortality by life is the Easter victory applied to the totality of human existence.</p>",
    "5": "<p>The Spirit as arrabōn (down-payment) points to the full resurrection inheritance. The Spirit who raised Jesus from the dead (Rom 8:11) is the first installment of the resurrection life that will be fully realized when Christ returns and transforms the mortal body to be like his own glorious body (Phil 3:21).</p>",
    "6": "<p>The Christian's true home is with the risen and ascended Lord (Phil 1:23: my desire is to depart and be with Christ, for that is far better). The life of faith is a life of holy homesickness for the presence of Christ — at home in the body but away from the one who is the soul's true home.</p>",
    "7": "<p>The sight of Christ's resurrection has not yet been granted in its fullness; the apostle walks toward what he does not yet fully see. Faith is the appropriate mode of existence in the time between resurrection and parousia — trusting the one whose resurrection is real even when not yet visible.</p>",
    "8": "<p>The desire to be with Christ mirrors the risen Lord's own prayer: Father, I desire that they also, whom you have given me, may be with me where I am (John 17:24). Death for the believer is departure into the presence of the one who conquered death — not defeat but homecoming.</p>",
    "9": "<p>The ambition to please Christ (euarestos autō einai) frames all apostolic activity. Jesus himself lived to please the Father (John 8:29: I always do the things that are pleasing to him); the apostle inherits and embodies this orientation, making it the single aim of both present life and approaching death.</p>",
    "10": "<p>The risen Christ who has been given all judgment by the Father (John 5:22) will adjudicate every life at the bema. For those in Christ there is no condemnation (Rom 8:1), but there is full revelation — every deed, every motive, every act of service or neglect disclosed and evaluated by the one who knows all things.</p>",
    "11": "<p>Paul's persuasion is motivated by the awesome reality of standing before the risen Christ — not commercial interest or social ambition. The fear of the Lord (Prov 9:10) is the beginning of the apostle's wisdom about how life is to be lived and how the gospel is to be proclaimed.</p>",
    "12": "<p>The boast that matters is before God who sees the heart (1 Sam 16:7). Christ himself was outwardly despised and rejected (Isa 53:2-3) but was inwardly and ultimately vindicated by the resurrection. The apostle who follows the crucified Christ shares this pattern of outward weakness and inward reality.</p>",
    "13": "<p>Ecstatic experiences belong to the vertical relationship with God; sober self-presentation belongs to the congregation's formation. The cruciform mind holds both: wholly given to God, wholly given to others — the two great commandments embodied in apostolic life.</p>",
    "14": "<p>The love of Christ (his self-giving agape demonstrated at the cross — Rom 5:8: God demonstrates his own love for us in that while we were sinners Christ died for us) is the controlling force. Because we have concluded this: one has died for all — the hyper-pantōn atonement is Paul's compressed creed, the christological foundation of everything that follows in vv.14-21.</p>",
    "15": "<p>The purpose of the atonement is transformation of life-orientation: from self-living to Christ-living. The resurrection (and was raised) is inseparable from the death in the salvific formula; the risen Christ calls the redeemed to live for him — not as burden but as the natural expression of having been bought with his life.</p>",
    "16": "<p>The resurrection inaugurates a new epistemology: no human being can be rightly evaluated apart from their relation to the risen Christ. The pre-conversion Pharisee who assessed Jesus as a failed messianic pretender has been overturned by the resurrection; all old assessments collapse before the Easter event.</p>",
    "17": "<p>The resurrection of Christ is the beginning of the new creation (Rev 21:5: behold, I am making all things new; Col 1:18: the firstborn from the dead). Those who are in Christ are participants in the new creation that began at Easter — already possessing the new-creation life through the Spirit, awaiting its full manifestation at the parousia.</p>",
    "18": "<p>The new creation and the reconciliation are both pure gift (panta ek tou theou — all things from God). The triune God initiated, effected, and now extends the reconciliation through the apostolic ministry. The ministry of reconciliation continues the mission of the reconciled.</p>",
    "19": "<p>The not-counting (mē logizomenos) of trespasses is the negative side of the great exchange (v.21): Christ is counted as sin so believers are not counted as sinners. The cosmic scope (kosmos) of the reconciliation reflects the resurrection's universal claim — Christ is Lord of all, and the reconciliation is offered to all.</p>",
    "20": "<p>The apostle participates in Christ's own mission as the Father's supreme ambassador (Heb 1:1-2: God has spoken to us by his Son). The plea — be reconciled to God — is Christ's own appeal through the apostle's voice. The urgency of the appeal reflects the seriousness of the estrangement that Christ's death has bridged.</p>",
    "21": "<p>The great exchange is the christological ground of all Paul's soteriology: the sinless one (the lamb without blemish — 1 Pet 1:19; who knew no sin experientially — Heb 4:15) was made to be sin — identified with the sin-offering (hatta't), bearing the curse (Gal 3:13). The purpose (hina): we become the righteousness of God in him — not merely declared righteous but incorporated into the covenant faithfulness of God himself. The substitution is total and symmetrical; this is the center of the cross's meaning for Paul.</p>",
  }
}

if __name__ == '__main__':
    existing = load_comm('mkt-christ', '2corinthians')
    merge_comm(existing, NEW)
    save_comm('mkt-christ', '2corinthians', existing)
    for ch in ['1', '2', '3', '4', '5']:
        print(f'  ch {ch}: {len(existing.get(ch, {}))} verses')
