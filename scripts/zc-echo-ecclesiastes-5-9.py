"""
Echo Commentary — Ecclesiastes chapters 5–9
Run: python3 scripts/zc-echo-ecclesiastes-5-9.py

No parallels file exists for Ecclesiastes.

Ch 5: The disciplined speech before God, vow-keeping, and the gift of simple
    enjoyment connect forward to the Lord's Prayer, vow-regulation in Matt 5,
    and the contentment theology of 1 Tim 6.
Ch 6: The limitation of wealth without the capacity to enjoy it and the
    insatiable appetite connect to the Bread of Life discourse (John 6) and
    the parable of the rich fool (Luke 12).
Ch 7: The counter-intuitive wisdom about mourning, death, and the universal
    sinfulness (v20, v29) connects to the Beatitudes and the Pauline diagnosis
    of universal sin (Rom 3:10-12).
Ch 8: The universal power of death and the delayed-judgment problem connect to
    Christ's conquest of death (Heb 2:14-15; Rev 1:18) and Paul's patience-
    and-wrath theology (Rom 2:4-5).
Ch 9: The universal fate of death, the hope of the living, and the forgotten
    poor wise man who saved the city provide the richest christological echoes
    in this section.
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

ECCLESIASTES_ECHOES = {
  "5": {
    "1": [
      {"type": "allusion", "target": "1 Sam 15:22",
       "note": "The Qohelet's counsel that drawing near to listen is better than the sacrifice of fools stands in the prophetic tradition that obedience surpasses ritual: 'to obey is better than sacrifice, and to listen than the fat of rams' (1 Sam 15:22). The same principle governs Isa 1:13-17 and Mic 6:6-8. Hebrews 10:22 draws the conclusion: the true approach to God's house is through Christ's blood, with sincere heart and full assurance of faith."},
      {"type": "allusion", "target": "Heb 10:22",
       "note": "The warning to guard one's steps when approaching the house of God anticipates the Hebrews invitation: 'let us draw near with a true heart in full assurance of faith.' Both texts treat proximity to God as something requiring preparation and intentionality — but where Ecclesiastes can only counsel caution, Hebrews provides the basis for bold approach: the blood of Christ that cleanses the conscience from dead works to serve the living God."}
    ],
    "2": [
      {"type": "allusion", "target": "Matt 6:7",
       "note": "Qohelet's counsel against hasty, wordy speech before God — 'let your words be few' because 'God is in heaven and you are on earth' — is the exact principle Jesus applies in the Lord's Prayer instruction: 'when you pray, do not heap up empty phrases as the Gentiles do, for they think that they will be heard for their many words. Do not be like them, for your Father knows what you need before you ask' (Matt 6:7-8). Both texts ground verbal restraint in the same asymmetry: God's transcendence makes human verbal performance unnecessary."}
    ],
    "4": [
      {"type": "allusion", "target": "Matt 5:33",
       "note": "Qohelet's vow-keeping instruction — 'pay what you have vowed' — participates in the tradition that Jesus radicalizes in the Sermon on the Mount: 'do not swear at all&hellip; let what you say be simply Yes or No' (Matt 5:33-37). Where Ecclesiastes regulates vow-keeping after the vow is made, Jesus relocates the problem to the making of vows itself: the integrity that Qohelet commends as a duty Christ commends as a default mode of speech."}
    ],
    "10": [
      {"type": "allusion", "target": "1 Tim 6:6",
       "note": "Qohelet's observation that whoever loves money is never satisfied with money — this too is vapor — is the experiential foundation for Paul's teaching: 'there is great gain in godliness with contentment, for we brought nothing into the world and we cannot take anything out of the world&hellip; the love of money is a root of all kinds of evils' (1 Tim 6:6-10). Qohelet observes the futility of money-love from below; Paul provides the positive alternative (contentment as godliness) and the warning from above."}
    ],
    "15": [
      {"type": "allusion", "target": "1 Tim 6:7",
       "note": "The image of coming naked from the womb and departing just as naked — carrying nothing from one's labor — is cited almost verbatim in 1 Timothy 6:7: 'we brought nothing into the world, and we cannot take anything out of the world.' Paul uses this Qohelet observation to ground the virtue of contentment: since nothing can be carried out, the acquisition of more is structurally futile, and the wise person attaches to what does accompany them — godliness and contentment — rather than wealth."}
    ],
    "18": [
      {"type": "theme", "target": "Col 3:17",
       "note": "Qohelet's commendation of eating, drinking, and finding enjoyment in labor as the fitting portion God gives identifies the created-goods enjoyment as a gift that comes from God and is received with him in view. Paul's christological translation: 'whatever you do, in word or deed, do everything in the name of the Lord Jesus, giving thanks to God the Father through him' (Col 3:17). The enjoyment Qohelet commends becomes the thanksgiving that Col 3 prescribes — both recognize the same structure of receiving created goods as God's gift."}
    ]
  },
  "6": {
    "2": [
      {"type": "allusion", "target": "Luke 12:20",
       "note": "Qohelet's portrait of the man who has wealth, riches, and honor but whom God does not enable to enjoy them — and a stranger devours it all — is the wisdom-tradition version of the parable of the rich fool: 'God said to him, Fool! This night your soul is required of you, and the things you have prepared, whose will they be?' (Luke 12:20). Both texts identify the same configuration: abundance of goods, absence of the capacity to possess them, and sudden dissolution. Jesus makes explicit what Qohelet leaves implicit: God is the one who withdraws the capacity."}
    ],
    "7": [
      {"type": "allusion", "target": "John 6:35",
       "note": "All a person's labor goes toward filling the mouth yet the appetite is never satisfied — the structural insatiability of physical hunger as an image of the deeper human emptiness. Jesus addresses precisely this in the Bread of Life discourse: 'I am the bread of life; whoever comes to me shall not hunger, and whoever believes in me shall never thirst' (John 6:35). Qohelet names the problem (appetite that labor cannot satisfy); Jesus names the answer (the bread that satisfies permanently). The connection is structural: only what comes from above can fill what labor below cannot."}
    ],
    "12": [
      {"type": "theme", "target": "John 14:2",
       "note": "Qohelet's closing question — 'who can tell anyone what will happen under the sun after they are gone?' — names the limit of human knowledge about the future. The NT answer is not a philosophical improvement but a personal one: Jesus reveals what is prepared 'after' — 'in my Father's house are many rooms&hellip; I am going to prepare a place for you' (John 14:2). The person who cannot be told what comes after is given by Christ not information about the future but a person who has gone before them."}
    ]
  },
  "7": {
    "2": [
      {"type": "allusion", "target": "Matt 5:4",
       "note": "Qohelet's observation that it is better to go to a house of mourning than feasting, because the living should take death to heart, aligns structurally with the Beatitude: 'blessed are those who mourn, for they shall be comforted' (Matt 5:4). The counter-intuitive wisdom that confronting grief is more formative than celebrating pleasure is the wisdom tradition's anticipation of the kingdom's grief-to-comfort dynamic. Jesus adds the eschatological comfort that Qohelet cannot supply: the mourning that takes death seriously will ultimately receive the consolation of resurrection."}
    ],
    "13": [
      {"type": "allusion", "target": "Rom 9:20",
       "note": "Qohelet's rhetorical question — 'who can straighten what God has made crooked?' — expresses the limits of human capacity to alter God's sovereign arrangements. Paul uses the same argument in Romans 9:20 against the person who quarrels with God's purposes: 'who are you, O man, to answer back to God? Will what is molded say to its molder, why have you made me like this?' Both texts place the creature before the Creator's irreversible decisions. The NT adds that the crooked — humanity's sin — is ultimately addressed not by human straightening but by Christ's death, which achieves what no human agency could."}
    ],
    "20": [
      {"type": "quote", "target": "Rom 3:10",
       "note": "Qohelet's observation that 'there is no righteous person on earth who always does good and never sins' is the experiential-wisdom foundation for Paul's catena in Romans 3:10-12, where he quotes Psalm 14:1-3 (&ldquo;there is no one righteous, not even one&rdquo;) to demonstrate universal sinfulness. Paul and Qohelet share the same diagnosis — the universal moral failure of the human — but Paul proceeds to the solution that Qohelet cannot reach: the righteousness of God through faith in Jesus Christ (Rom 3:21-22)."}
    ],
    "29": [
      {"type": "allusion", "target": "Gen 3:1",
       "note": "Qohelet's conclusion that 'God made human beings upright, but they have gone in search of many devices' is a compressed summary of the Fall: the original uprightness (<em>yashar</em>) and the autonomous seeking (<em>biqqeshu chishbonot rabbim</em>) maps directly onto Genesis 3, where the human pair — made in the image of God — sought the devices of independent moral knowledge. The serpent's enticement and Eve's and Adam's seeking are the first instance of the device-seeking that Qohelet catalogs across the entire human project. Romans 5:12 gives this the theological form Paul needs: 'sin came into the world through one man.'"}
    ]
  },
  "8": {
    "8": [
      {"type": "type", "target": "Heb 2:14",
       "note": "Qohelet's observation that no one has power over the life-breath to restrain it, and no one has power over the day of death — 'there is no release from that battle' — names the absolute limit of human power. This is the problem that Hebrews 2:14-15 identifies as addressed by the Incarnation: 'through death he might destroy the one who has the power of death, that is, the devil, and deliver all those who through fear of death were subject to lifelong slavery.' Christ enters the battle from which there is 'no release' and releases those trapped in it — achieving what Qohelet says no human can do."},
      {"type": "type", "target": "Rev 1:18",
       "note": "The claim that no one has power over the day of death finds its resolution in the risen Christ's declaration: 'I died, and behold I am alive forevermore, and I have the keys of Death and Hades' (Rev 1:18). The 'keys' are the authority over the locked gates that Qohelet says no one can open. Christ does not merely survive death but acquires dominion over it — the power that Qohelet says belongs to no human being is shown by Revelation to belong to the risen Son."}
    ],
    "11": [
      {"type": "allusion", "target": "Rom 2:4",
       "note": "Qohelet's observation that when the sentence for a wrong is not carried out quickly the human heart is emboldened to do evil is the experiential ground for Paul's warning about presuming on divine patience: 'do you presume on the riches of his kindness and forbearance and patience, not knowing that God's kindness is meant to lead you to repentance? But because of your hard and impenitent heart you are storing up wrath for yourself on the day of wrath' (Rom 2:4-5). Both texts identify the same misreading of delayed judgment as license; Paul makes explicit that the delay is patience, not permissiveness."}
    ],
    "17": [
      {"type": "allusion", "target": "1 Cor 2:10",
       "note": "Qohelet's conclusion that no one — not even the wise — can discover all that God has done under the sun names the epistemic limit of human wisdom before divine hiddenness. Paul addresses the same hiddenness from the other side: 'God has revealed to us through the Spirit&hellip; the Spirit searches everything, even the depths of God' (1 Cor 2:10). The wisdom that cannot be discovered by searching (Qohelet's conclusion) is the wisdom that God discloses by the Spirit to those who receive the mind of Christ. The revelation does not negate the hiddenness Qohelet describes; it provides access from within the hiddenness through the Spirit's gift."}
    ]
  },
  "9": {
    "1": [
      {"type": "allusion", "target": "John 10:29",
       "note": "Qohelet's claim that 'the righteous and the wise and all they do are in God's hands' — even though no one knows whether love or hatred awaits them — provides the frame that Jesus fills christologically: 'no one is able to snatch them out of the Father's hand' (John 10:29). Qohelet affirms divine custody of the righteous but cannot resolve the uncertainty about outcome; Jesus declares that custody means preservation — the sheep held in the Father's hand are held toward eternal life, not toward an uncertain end."}
    ],
    "2": [
      {"type": "theme", "target": "Heb 9:27",
       "note": "The same fate coming to all — righteous and wicked, clean and unclean, those who sacrifice and those who do not — is the experiential observation behind Hebrews 9:27: 'it is appointed for people to die once, and after that comes judgment.' Both texts affirm the universal appointment of death; Hebrews adds the judgment that follows and the solution Christ provides: his one sacrifice for sins addresses the universal appointment by providing the atonement that the universal judgment requires."}
    ],
    "5": [
      {"type": "allusion", "target": "1 Cor 15:18",
       "note": "The claim that the dead know nothing, have no further reward, and are forgotten defines the horizon that Paul identifies as the problem that the resurrection resolves: 'if there is no resurrection of the dead&hellip; then those also who have fallen asleep in Christ have perished' (1 Cor 15:13, 18). Qohelet describes what resurrection would need to overcome: the forgetting, the knowing-nothing, the ended reward. Paul argues that Christ's resurrection transforms Qohelet's description from permanent condition to temporary state — death is not the end but the penultimate moment before the final resurrection."}
    ],
    "10": [
      {"type": "allusion", "target": "Col 3:23",
       "note": "The exhortation 'whatever your hand finds to do, do it with all your strength' — grounded in the urgency that there is no work in the grave — is taken up in Paul's christological reframing of labor: 'whatever you do, work heartily, as for the Lord and not for men, knowing that from the Lord you will receive the inheritance as your reward' (Col 3:23-24). Qohelet's urgency is grounded in death's approach; Paul's urgency is grounded in Christ's lordship. Both produce wholehearted present engagement, but Paul adds the permanence of reward that Qohelet denies."}
    ],
    "15": [
      {"type": "type", "target": "Luke 4:24",
       "note": "The poor wise man who saved the city by his wisdom and was not remembered afterward is a striking type of Christ's own reception. The structural parallel is exact: he came in poverty and wisdom, he delivered the community from the besieging power, and he was forgotten. Jesus' pronouncement that 'no prophet is acceptable in his hometown' (Luke 4:24) speaks to the same pattern. The forgotten deliverer of Ecclesiastes 9 anticipates the despised and rejected Servant (Isa 53:3) who saved by his wisdom what no military power could and was not remembered by those he saved — until the resurrection reversed the forgetting."},
      {"type": "allusion", "target": "1 Cor 1:25",
       "note": "The poor wise man who saved the city by wisdom and was despised illustrates the principle Paul articulates in 1 Corinthians 1:25: 'the foolishness of God is wiser than men, and the weakness of God is stronger than men.' The world's failure to value the poor man's wisdom that saved it is the Ecclesiastes version of the world's failure to recognize the crucified Christ as wisdom — 'Christ crucified, a stumbling block to Jews and folly to Gentiles, but to those who are called&hellip; the power of God and the wisdom of God' (1 Cor 1:23-24)."}
    ],
    "17": [
      {"type": "allusion", "target": "1 Cor 1:21",
       "note": "Qohelet's observation that words of the wise spoken quietly carry more weight than the shouting of rulers among fools is the experiential foundation for Paul's insight that God 'was pleased through the folly of preaching to save those who believe' (1 Cor 1:21). The quiet wisdom that carries more weight than the shouting of power is the pattern of Christ's teaching — not conquest by rhetorical force but the still, small persuasion that captures those with ears to hear. The quiet word of the wise is the wisdom-form of the foolishness of preaching."}
    ]
  }
}

def main():
    existing = load_echo('ecclesiastes')
    merge_echo(existing, ECCLESIASTES_ECHOES)
    save_echo('ecclesiastes', existing)
    total = sum(len(vv) for vv in ECCLESIASTES_ECHOES.values())
    entries = sum(len(e) for ch in ECCLESIASTES_ECHOES.values() for e in ch.values())
    print(f'Ecclesiastes 5-9 echoes: {total} verses, {entries} entries written.')

if __name__ == '__main__':
    main()
