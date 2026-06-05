"""
MKT Echo — John chapter 8
Run: python3 scripts/zc-echo-john-8-8.py

Source data used:
- data/interlinear/john.json (Strongs codes; confirmed egō eimi at vv.12, 24, 28, 58)
- data/translation/draft/mediating/john.json (MKT text for all 59 verses)
- data/parallels/john.json (empty — nothing to absorb)
- data/echoes/john.json (existing entries for chs 1–6; ch 8 not yet written)

Key decisions in this range:
- vv.1–11 (Pericope Adulterae): Textually absent from earliest manuscripts (P66, P75,
  Sinaiticus, Vaticanus) and widely considered a later insertion. Echoes are written for
  the received text without suppressing this fact in notes where the textual uncertainty
  is hermeneutically significant.
- vv.24, 28, 58 (absolute ἐγώ εἰμι): Classified as `allusion` to Isa 43:10–13 and
  Exod 3:14. The verbal form (Greek egō eimi / LXX egō eimi) intentionally echoes the
  divine name formula; v.58 is classified `allusion` rather than `fulfillment` because
  Jesus makes an ontological claim, not a citation of a predictive text.
- v.5 / v.7: The two-witness law invoked (Deut 17:7 executioner requirement, Deut 19:15
  dual-witness rule). v.17 contains Jesus' explicit citation of "your Law" (Deut 19:15)
  — classified `quote`.
- v.6 (writing on the ground): Jer 17:13 is the most defensible OT parallel — note hedges
  appropriately given that the connection is widely discussed but not verbally certain.
- v.35 (slave vs. son): Gen 21:10 (Hagar/Ishmael expulsion) is the structural background
  to the slave/son contrast; Paul makes this explicit in Gal 4:30 but John's text evokes
  the same distinction without citing it.
- v.56 (Abraham saw my day): Gen 22:14 (yhwh yir'eh / the LORD will be seen/provide) is
  the primary reference; Gen 15:12–18 (covenant vision) is the secondary candidate.
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

JOHN_ECHOES = {
  "8": {

    # ── Pericope Adulterae (vv. 1–11) ────────────────────────────────────

    "1": [
      {"type": "allusion", "target": "2 Sam 15:30",
       "note": "David fled to the Mount of Olives weeping when betrayed — a king ascending in grief and exposure. The Evangelist's placement of Jesus at the same location on the night before the confrontation in the temple courts carries Davidic resonance: the rightful king withdraws, then returns to face his opponents."},
      {"type": "allusion", "target": "Zech 14:4",
       "note": "Zechariah locates the Lord's eschatological victory on the Mount of Olives: 'On that day his feet will stand on the Mount of Olives.' Jesus' regular presence there (Luke 21:37) draws on this geography as the site of messianic arrival and judgment."}
    ],

    "2": [
      {"type": "theme", "target": "Isa 2:3",
       "note": "Isaiah envisions a day when the nations stream to the mountain of the Lord to be taught his ways: 'For out of Zion shall go forth the law, and the word of the LORD from Jerusalem.' Jesus teaching in the temple courts with all the people gathered around him is the beginning of that fulfillment — Torah going forth from Zion's sanctuary."}
    ],

    "3": [
      {"type": "shadow", "target": "Hos 3:1",
       "note": "The Mosaic law treats adultery as a covenant violation — Israel's repeated apostasy is itself figured by Hosea as adultery against the Lord. The woman brought before Jesus represents the broader pattern of covenant unfaithfulness that the prophets diagnosed; Jesus' response of forgiveness without condoning sin mirrors the divine posture in the prophets."}
    ],

    "5": [
      {"type": "quote", "target": "Lev 20:10",
       "note": "The Pharisees cite the Mosaic law directly: 'Moses commanded us to stone such women.' Lev 20:10 and Deut 22:22–24 both prescribe death for adultery. The citation is accurate; the trap lies in forcing Jesus to adjudicate between Roman law (which denied Jews capital authority) and Mosaic law."},
      {"type": "allusion", "target": "Deut 22:22",
       "note": "Deuteronomy specifies that both parties caught in adultery are to be put to death — yet only the woman is brought forward. The one-sided accusation already violates the law's own requirement, a contradiction Jesus need not name to make present."}
    ],

    "6": [
      {"type": "allusion", "target": "Jer 17:13",
       "note": "Jeremiah declares that those who turn from the Lord will be 'written in the dust' — their names recorded in the earth rather than among the living. Jesus writing on the ground with his finger may evoke this image: the accusers themselves, not the accused, are the ones whose names belong in the dust. The verbal connection is possible though not verbally certain; many scholars note it while acknowledging its uncertainty."},
      {"type": "allusion", "target": "Exod 31:18",
       "note": "The law was written by the finger of God on stone tablets. Jesus writes with his finger on the ground — a reversal: not permanent stone but transient earth, not condemnation but an act that disperses the accusers. The gesture echoes divine writing without asserting it as a fulfillment claim."}
    ],

    "7": [
      {"type": "allusion", "target": "Deut 17:7",
       "note": "The Mosaic law required that the witnesses throw the first stone in an execution: 'The hands of the witnesses must be the first in putting that person to death.' Jesus does not abolish the law's procedure but applies its qualification directly: the legally required first thrower must be sinless. The accusers' silent departure is their tacit confession of disqualification."}
    ],

    "11": [
      {"type": "theme", "target": "Isa 43:25",
       "note": "The divine declaration in Isaiah — 'I, even I, am he who blots out your transgressions, for my own sake, and remembers your sins no more' — provides the theological ground for Jesus' 'neither do I condemn you.' Forgiveness is not the suspension of justice but the prerogative of the one who is both judge and redeemer."},
      {"type": "theme", "target": "Ezek 18:21",
       "note": "Ezekiel's watchman theology insists that if the wicked turn from their sins, none of their offenses will be held against them. 'Go now and leave your life of sin' is the prophetic call to repentance that precedes restoration — the pattern Ezekiel articulates and Jesus enacts in person."}
    ],

    # ── "I am the light of the world" (v. 12) ────────────────────────────

    "12": [
      {"type": "fulfillment", "target": "Isa 42:6",
       "note": "The Servant Song appoints the Servant 'as a light for the Gentiles' — to open eyes that are blind, to free captives from darkness. Jesus claims this role directly and personally: 'I am the light of the world.' John presents the claim as the Servant's self-identification, not merely an analogy."},
      {"type": "fulfillment", "target": "Isa 49:6",
       "note": "'I will also make you a light for the Gentiles, that my salvation may reach to the ends of the earth.' The scope of 'the world' in Jesus' claim echoes this universal Servant commission; the light is not national but cosmic in reach."},
      {"type": "allusion", "target": "Isa 9:2",
       "note": "'The people walking in darkness have seen a great light; on those living in the land of deep darkness a light has dawned.' Isaiah's eschatological light, promised to a people under shadow, arrives in person. John has already identified Jesus as the light shining in darkness (John 1:5); here Jesus makes the claim explicitly."},
      {"type": "theme", "target": "Ps 27:1",
       "note": "'The LORD is my light and my salvation — whom shall I fear?' The Psalm connects light with salvation and casts out fear. Jesus' declaration that his followers will 'have the light of life' expands the Psalm's personal confession into a universal offer."}
    ],

    # ── Two-witness law (vv. 13–18) ───────────────────────────────────────

    "13": [
      {"type": "theme", "target": "Num 35:30",
       "note": "Numbers requires multiple witnesses in capital cases: 'No one is to be put to death on the testimony of only one witness.' The Pharisees invoke the same principle against Jesus' self-testimony. The irony of the passage is that the one whose testimony they discount is the only fully reliable witness in the scene."}
    ],

    "15": [
      {"type": "theme", "target": "Isa 11:3",
       "note": "Isaiah's messianic king 'will not judge by what he sees with his eyes, or decide by what he hears with his ears; but with righteousness he will judge.' Jesus contrasts 'judging by human standards' (kata tēn sarka) with judgment by the Father's standard — the very distinction Isaiah draws between flawed human evaluation and the Spirit-equipped righteous judgment of the Davidic ruler."}
    ],

    "16": [
      {"type": "allusion", "target": "Isa 50:8",
       "note": "The Servant declares: 'He who vindicates me is near. Who then will bring charges against me?' Jesus standing with the Father who sent him mirrors the Servant's confidence: the judge is not the human court but the divine sender. Condemnation by the religious authorities cannot override the vindication of the one who commissioned the mission."}
    ],

    "17": [
      {"type": "quote", "target": "Deut 19:15",
       "note": "Jesus explicitly cites 'your own Law': Deut 19:15 establishes that 'a matter must be established by the testimony of two or three witnesses.' By framing his two-witness claim (himself + the Father) within the Law's own evidentiary standard, Jesus does not bypass Torah but fulfills its procedural requirement at the highest possible register."}
    ],

    # ── "I go where you cannot come" (vv. 21–24) ─────────────────────────

    "21": [
      {"type": "allusion", "target": "Ezek 3:18",
       "note": "Ezekiel's watchman oracle: 'When I say to a wicked person, you will surely die, and you do not warn them... that wicked person will die for their sin.' The formula 'you will die in your sin' is drawn from Ezekiel's covenant-accountability language — the consequence of rejecting the appointed messenger's word."},
      {"type": "allusion", "target": "Ezek 33:8",
       "note": "The same Ezekielian formula recurs: 'if you do not speak out to dissuade them from their ways, that wicked person will die for their sin.' Jesus as the appointed prophet-messenger pronounces the covenantal consequence; the echo makes his warning recognizable within Israel's prophetic tradition, not unprecedented."}
    ],

    "24": [
      {"type": "allusion", "target": "Isa 43:10",
       "note": "The absolute ἐγώ εἰμι ('I am he') matches the LXX translation of the divine self-identification formula repeated in Deutero-Isaiah: 'so that you may know and believe me and understand that I am he' (egō eimi). The same formulation appears in Isa 43:13, 25; 45:18; 46:4; 48:12 — a signature of Yahweh's exclusive self-declaration. Jesus' use of the formula without a predicate is a deliberate appropriation of this idiom."},
      {"type": "allusion", "target": "Deut 32:39",
       "note": "'See now that I, even I, am he' (Deut 32:39, LXX: idete idete hoti egō eimi) — the Song of Moses uses the identical formula as Yahweh asserts exclusive sovereignty over life and death. The absence of a predicate in Jesus' 'I am he' echoes this Mosaic divine self-declaration directly."}
    ],

    # ── "When you have lifted up the Son of Man" (v. 28) ─────────────────

    "28": [
      {"type": "allusion", "target": "Isa 52:13",
       "note": "The Servant will 'be raised and lifted up and highly exalted.' John's distinctive word for crucifixion — hypsōthēnai ('to be lifted up,' also in John 3:14; 12:32) — fuses exaltation and death in a way that echoes Isaiah's exalted Servant. Being lifted up on the cross is simultaneously being lifted up in glory."},
      {"type": "allusion", "target": "Isa 43:10",
       "note": "'When you have lifted up the Son of Man, then you will know that I am he' — the disclosure formula mirrors Isa 43:10 ('so that you may know... that I am he'). The crucifixion becomes the revelatory event through which the divine identity becomes undeniable, the very function Isaiah assigned to Israel's witness-role among the nations."}
    ],

    # ── Truth and freedom (vv. 31–36) ────────────────────────────────────

    "32": [
      {"type": "theme", "target": "Ps 119:45",
       "note": "The psalmist declares 'I will walk about in freedom, for I have sought out your precepts.' The connection between knowing God's truth and living in freedom runs through the wisdom tradition; Jesus claims to be the living embodiment of that truth — knowing him replaces the role of the precepts as the path to freedom."},
      {"type": "allusion", "target": "Isa 61:1",
       "note": "The anointed one of Isa 61:1 proclaims 'freedom for the captives and release from darkness for the prisoners.' Jesus' promise that the truth will set his followers free stands in the trajectory of this jubilee proclamation; John 8:36 ('if the Son sets you free, you will be free indeed') makes the agent explicit."}
    ],

    "33": [
      {"type": "allusion", "target": "Isa 41:8",
       "note": "'You, Israel, my servant, Jacob, whom I have chosen, you descendants of Abraham my friend' — Abrahamic descent is the identity Israel claims throughout the OT. The crowd's appeal ('we are Abraham's descendants') is not incorrect but misapplied: descent does not automatically confer the freedom that belongs to the covenant relationship, a distinction the prophets also made (Jer 7:4; Isa 48:1–2)."}
    ],

    "34": [
      {"type": "theme", "target": "Isa 42:7",
       "note": "The Servant's commission includes 'freeing captives from prison and releasing from the dungeon those who sit in darkness.' Jesus' diagnosis — 'everyone who sins is a slave to sin' — names the captivity the Servant is sent to break. Sin as bondage, not merely infraction, is the presupposition behind the Servant's liberation work."}
    ],

    "35": [
      {"type": "allusion", "target": "Gen 21:10",
       "note": "Sarah's dismissal of Hagar and Ishmael — 'Get rid of that slave woman and her son, for that woman's son will never share in the inheritance with my son Isaac' — establishes the OT contrast Jesus invokes: a slave has no permanent standing in the household; the son inherits. Paul develops the same contrast typologically in Gal 4:30, confirming that the Gen 21 story was read in early Christianity as the background for the slave/son distinction."}
    ],

    "36": [
      {"type": "allusion", "target": "Isa 61:1",
       "note": "The anointed figure of Isa 61:1 proclaims 'the year of the LORD's favor' — the jubilee language of release and restoration. 'If the Son sets you free, you will be free indeed' names the agent of that jubilee as the Son, whose freedom is permanent (ontological) rather than cyclical (jubilee) or conditional (law-observance)."}
    ],

    # ── Abraham discourse (vv. 37–47) ─────────────────────────────────────

    "37": [
      {"type": "allusion", "target": "Jer 11:19",
       "note": "Jeremiah records a plot against his own life from those who rejected his word: 'Let us destroy the tree and its fruit; let us cut him off from the land of the living, that his name be remembered no more.' The pattern — murderous rejection of the prophet sent by God — is what Jesus identifies in the crowd's desire to kill him despite his Abrahamic lineage claim."}
    ],

    "39": [
      {"type": "allusion", "target": "Gen 18:19",
       "note": "God commissions Abraham specifically because 'he will direct his children and his household after him to keep the way of the LORD by doing what is right and just.' The standard for being Abraham's children is not genealogy but covenantal conduct. Jesus applies Abraham's own commissioning criteria: doing what Abraham did — receiving the one God sent."}
    ],

    "41": [
      {"type": "allusion", "target": "Isa 63:16",
       "note": "Isaiah's prayer pleads: 'You are our Father, though Abraham does not know us or Israel acknowledge us; you, LORD, are our Father.' The crowd's claim — 'the only Father we have is God himself' — uses Isaiah's prayer language, but the prophet used it in confession of failure, not assertion of status. The crowd inverts the prayer's penitent logic into a proud self-justification."}
    ],

    "42": [
      {"type": "theme", "target": "Mal 1:6",
       "note": "'A son honors his father, and a servant his master. If I am a father, where is the honor due me?' Malachi's rebuke — addressed to a people who claim God as Father while dishonoring him through faithless worship — is the pattern Jesus applies. Those who claim divine fatherhood while rejecting the Son God sent have reproduced Malachi's contradiction."}
    ],

    "43": [
      {"type": "fulfillment", "target": "Isa 6:9",
       "note": "Isaiah's commissioning oracle — 'Be ever hearing, but never understanding; be ever seeing, but never perceiving' — describes the covenantal hardening that results from repeated rejection of the prophetic word. Jesus' observation that the crowd is 'unable to hear' his word fits this pattern: it is not merely intellectual failure but the judicial consequence of persistent rejection."}
    ],

    "44": [
      {"type": "allusion", "target": "Gen 3:4",
       "note": "The serpent's first recorded speech is a lie: 'You will not certainly die' — a direct contradiction of God's word. Jesus identifies the devil as 'the father of lies' whose native language is falsehood; this identity is established in the garden narrative where deception is the instrument of humanity's first death."},
      {"type": "allusion", "target": "Gen 4:8",
       "note": "Cain's murder of Abel is the first human murder, committed under the influence of the one Jesus names as 'a murderer from the beginning' (1 John 3:12 makes the Cain connection explicit). The 'beginning' of murder in human history is Gen 4; the 'beginning' of the murderous impulse lies in the deceiver who preceded it."}
    ],

    "46": [
      {"type": "allusion", "target": "Isa 53:9",
       "note": "'He had done no violence, nor was any deceit in his mouth' — Isaiah's portrait of the Servant's sinlessness is the OT counterpart to Jesus' challenge: 'Can any of you prove me guilty of sin?' The Servant's blamelessness, which enables him to bear others' guilt, is the same sinlessness Jesus claims as the ground for the crowd's obligation to believe him."}
    ],

    "47": [
      {"type": "allusion", "target": "Deut 18:15",
       "note": "Moses promises a prophet like himself: 'you must listen to him.' The Mosaic succession establishes that belonging to God means hearing the prophet God sends. Jesus' statement — 'whoever belongs to God hears what God says' — is the same principle: refusal to hear him is evidence of belonging to a different father."},
      {"type": "allusion", "target": "Jer 7:13",
       "note": "The temple sermon: 'I spoke to you again and again, but you did not listen; I called you, but you did not answer.' Israel's history of not hearing is the pattern Jesus identifies as still operative; the crowd's inability to hear is the continuation of a covenantal failure the prophets repeatedly named."}
    ],

    "48": [
      {"type": "allusion", "target": "2 Kgs 17:29",
       "note": "After Assyria resettled Samaria, the colonists 'made their own gods in the several towns where they settled' while also fearing the LORD — a syncretistic religion the Jews regarded as spiritually polluted. Calling Jesus 'a Samaritan' was a sectarian slur implying mixed, apostate devotion; the juxtaposition with 'demon-possessed' signals the accusers' view that Jesus stands outside true Israelite covenantal religion."}
    ],

    "50": [
      {"type": "theme", "target": "Isa 42:8",
       "note": "'I am the LORD; that is my name! I will not yield my glory to another.' Jesus' refusal to seek his own glory — 'there is one who seeks it, and he is the judge' — is the inverse of Isaiah's divine declaration. God does not yield his glory; Jesus does not claim what he has not been given. The judge who seeks glory is the Father, and his verdict is the only one that counts."}
    ],

    # ── "Before Abraham was, I am" (vv. 51–59) ───────────────────────────

    "51": [
      {"type": "allusion", "target": "Gen 2:17",
       "note": "Death entered human experience as the consequence of disobeying God's word: 'when you eat from it you will certainly die.' Jesus promises the inverse: those who obey his word 'will never see death.' The reversal is structural — disobedience to the first divine word brought death; obedience to the Word made flesh brings life."},
      {"type": "theme", "target": "Ps 89:48",
       "note": "'Who can live and not see death, or who can escape the power of the realm of death?' The Psalm frames physical death as the universal human limit. Jesus' promise transgresses this limit, which is why the crowd hears it as either madness or the claim of someone greater than the patriarchs."}
    ],

    "56": [
      {"type": "type", "target": "Gen 22:14",
       "note": "After the Akedah, Abraham named the place 'the LORD Will Provide' (yhwh yir'eh) — and the narrator adds: 'And to this day it is said, On the mountain of the LORD it will be provided.' The verb can also mean 'seen' or 'appear.' Abraham saw the day of divine provision on that mountain; what he saw typologically was the sacrifice of the true Son, whose substitutionary death Gen 22 shadows with structural precision."},
      {"type": "allusion", "target": "Gen 15:12",
       "note": "During the covenant ceremony of Gen 15, a deep sleep fell on Abraham and a terrifying darkness; then the LORD passed through the pieces in fire — Abraham witnessed a prophetic vision of future suffering and redemption. The moment Abraham 'saw' the future may include this night vision, which revealed the covenant path through death to inheritance."}
    ],

    "58": [
      {"type": "allusion", "target": "Exod 3:14",
       "note": "God's self-disclosure to Moses — 'I AM WHO I AM... I AM has sent me to you' (LXX: egō eimi ho ōn / egō eimi) — is the foundational divine name declaration in the OT. Jesus' 'before Abraham was born, I am' reproduces the absolute egō eimi construction without a predicate, the precise form of the divine name. The crowd's response (taking up stones for blasphemy, v.59) confirms they understood the claim."},
      {"type": "allusion", "target": "Isa 43:13",
       "note": "'Even from ancient days I am he' (LXX: apo tēs archēs egō eimi) — Deutero-Isaiah's repeated divine self-identification formula places divine existence before all human history. Jesus' claim 'before Abraham was born, I am' maps onto this formulation: the 'I am he' who existed before the patriarch is the same speaker."},
      {"type": "allusion", "target": "Ps 90:2",
       "note": "'Before the mountains were born or you brought forth the whole world, from everlasting to everlasting you are God.' The Psalm frames God's existence as categorically prior to all creaturely time. Jesus' claim to pre-Abrahamic existence claims this same category — not merely long life (which the crowd's 'not yet fifty years old' already dismisses) but eternal being."}
    ],

    "59": [
      {"type": "allusion", "target": "Lev 24:16",
       "note": "The law mandated stoning for blasphemy: 'anyone who blasphemes the name of the LORD is to be put to death. The entire assembly must stone them.' The crowd's immediate move to pick up stones signals that they interpreted Jesus' absolute 'I am' as a blasphemous claim to the divine name — the charge that will recur at his trial (Mark 14:61–64). Their legal instinct is not wrong; what they deny is its truth."}
    ]

  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 8 echoes written.')

if __name__ == '__main__':
    main()
