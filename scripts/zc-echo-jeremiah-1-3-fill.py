"""
Echo fill — Jeremiah chapters 2–3
Run: python3 scripts/zc-echo-jeremiah-1-3-fill.py

Ch 1:5 already written by Phase 2 combined script; merge_echo will skip it.

Key echo decisions:
- 2:13 (living water / cracked cisterns) = John 4 and John 7 direct Christological appropriation
- 2:21 (choice vine gone wild) = John 15:1-6 (true vine replaces faithless Israel)
- 3:15 (shepherds after my heart) = John 10:11 (the Good Shepherd as ultimate fulfillment)
- 3:16 (no more ark needed) = Heb 9:4; Rev 21:22 (Christ/new Jerusalem supersedes the ark)
- 3:22 (return and I will heal) = Luke 15:20; John 6:37 (the welcome of the prodigal)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
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

JER_ECHO_2_3 = {
  "2": {
    "2": [
      {"type": "allusion", "target": "Eph 5:25-27", "note": "I remember the devotion of your youth, the love of your bridal days — YHWH recalls Israel's honeymoon fidelity in the wilderness; Paul frames the Christ-church relationship with the same husband-wife analogy: Christ loves the church as a husband loves his bride, presenting her holy and without blemish; the bridal covenant metaphor of Jer 2:2 becomes the lens through which Paul reads the cross"},
      {"type": "allusion", "target": "Rev 2:4", "note": "I have this against you: you have abandoned the love you had at first — the risen Christ to Ephesus echoes YHWH's lament over Israel's lost bridal devotion; the apostolic church recapitulates the pattern Jeremiah describes: first love given, then forsaken, then called to return"}
    ],
    "3": [
      {"type": "allusion", "target": "1 Cor 15:20", "note": "Israel was holy to the LORD, the firstfruits of his harvest — the firstfruits language applied to Israel as a consecrated offering to YHWH; Paul applies firstfruits language to Christ (the firstfruits of those who have fallen asleep) and to the first converts; Jas 1:18 applies it to believers. The consecrated-firstfruits status that Israel held is now held by Christ and, in him, the church"},
      {"type": "allusion", "target": "Jas 1:18", "note": "Of his own will he brought us forth by the word of truth, that we should be a kind of firstfruits of his creatures — James applies the firstfruits designation (originally Israel's, as in Jer 2:3) to the new covenant community; the church inherits Israel's covenantal status as YHWH's consecrated offering"}
    ],
    "11": [
      {"type": "allusion", "target": "Rom 1:23", "note": "My people have exchanged their glory for what does not profit — Israel traded YHWH, their glory, for worthless idols; Paul diagnoses the same exchange at the root of universal human sin: they exchanged the glory of the immortal God for images; the Jeremianic indictment of Israel becomes Paul's analysis of the entire Adamic race"},
      {"type": "allusion", "target": "Rom 3:23", "note": "All have sinned and fall short of the glory of God — the glory that Israel abandoned (Jer 2:11) is the glory that all humanity falls short of; Paul universalizes Jeremiah's particular accusation against Israel into a diagnosis of the human condition that Christ came to remedy"}
    ],
    "13": [
      {"type": "fulfillment", "target": "John 4:10-14", "note": "They have abandoned me, the spring of living water, and dug their own cisterns — cracked cisterns that hold no water; Jesus applies the living water image to himself at the Samaritan well: whoever drinks the water I give will never thirst; the spring of living water that Israel forsook (YHWH) is now identified as Jesus himself, who gives the water that becomes a spring welling up to eternal life"},
      {"type": "fulfillment", "target": "John 7:37-38", "note": "On the last day of the feast Jesus stood up and cried out: if anyone thirsts let him come to me and drink — the spring of living water (Jer 2:13) that Israel abandoned is now openly offered in Christ; YHWH's self-description as living water is Jesus's own self-proclamation"},
      {"type": "allusion", "target": "Rev 22:1", "note": "The river of the water of life, bright as crystal, flowing from the throne of God and of the Lamb — the spring of living water YHWH described himself as in Jer 2:13 flows in the new creation from the throne of the Lamb; what Israel refused now overflows eternally"}
    ],
    "21": [
      {"type": "fulfillment", "target": "John 15:1-5", "note": "I planted you as a choice vine, of pure and wholesome seed — how then have you turned into the wild shoots of a foreign vine? YHWH's vineyard metaphor for Israel reaches its Christological resolution in Jesus's claim: I am the true vine, and my Father is the gardener; where Israel failed as YHWH's vine, Christ is the vine that bears fruit; those who abide in him bear the fruit that Israel failed to bear"},
      {"type": "allusion", "target": "Rom 11:17-24", "note": "The wild olive branches grafted in where natural branches were broken off — Paul's grafting metaphor for Gentile inclusion parallels the vine imagery of Jer 2:21; what YHWH planted as a choice vine became wild, and the Gentiles who were wild are grafted into the cultivated stock; the vine/branches imagery expresses the same covenantal reversal"}
    ],
    "30": [
      {"type": "allusion", "target": "Matt 23:37", "note": "Your own sword has consumed your prophets like a ravaging lion — YHWH's lament that Israel killed his prophets; Jesus's lament over Jerusalem explicitly echoes this: O Jerusalem, Jerusalem, you who kill the prophets and stone those sent to you; the prophet-killing pattern Jeremiah mourns reaches its culmination in the rejection and crucifixion of Jesus himself"}
    ]
  },
  "3": {
    "1": [
      {"type": "allusion", "target": "Matt 19:8-9", "note": "If a man divorces his wife and she goes and marries another, can he take her back? — the Deuteronomic divorce law (Deut 24:1-4) declares such return defiling; yet YHWH proposes to take Israel back in spite of this law; Jesus's discussion of divorce (Matt 19:8-9) engages the same passage Moses wrote; the scandal of YHWH's grace over the letter of the law is the grace that the cross enacts"}
    ],
    "14": [
      {"type": "allusion", "target": "Luke 15:18-20", "note": "Return, faithless children, declares the LORD, for I am your husband — the divine call to return to the covenant; the prodigal son's return in Luke 15:18-20 ('I will arise and go to my father') enacts the teshuvah Jeremiah's YHWH summons; the father who runs to meet the returning son is the same YHWH who pleads for faithless Israel to come home"},
      {"type": "allusion", "target": "John 6:37", "note": "All that the Father gives me will come to me, and whoever comes to me I will never cast out — the divine assurance that those who return will be received; the Jeremianic call to return (3:14: return, faithless children) is backed by the same divine welcome Jesus promises to all who come to him"}
    ],
    "15": [
      {"type": "fulfillment", "target": "John 10:11", "note": "I will give you shepherds after my own heart, who will lead you with knowledge and wisdom — YHWH's promise of true shepherds to replace the faithless leaders; Jesus is the ultimate fulfillment: I am the good shepherd; the good shepherd who leads with knowledge and wisdom is YHWH's own shepherd-heart in human form"},
      {"type": "allusion", "target": "Eph 4:11", "note": "He gave the apostles, the prophets, the evangelists, the shepherds and teachers — Christ gives shepherd-leaders to the church, fulfilling the promised shepherds after God's own heart (Jer 3:15); the gift of shepherds is ultimately Christ's gift through his ascension"}
    ],
    "16": [
      {"type": "allusion", "target": "Heb 9:4", "note": "In those days no one will say anymore: the ark of the covenant of the LORD — its day is past; in the new age, the ark will no longer be the focus of covenant presence; Hebrews traces the supersession of the ark's sacred furniture by Christ's own person and priestly ministry; the diminishment of the ark that Jeremiah prophesies is fulfilled in the new covenant"},
      {"type": "fulfillment", "target": "Rev 21:22", "note": "I saw no temple in the city, for its temple is the Lord God Almighty and the Lamb — the ark resided in the temple's inner sanctum; the new Jerusalem has neither ark nor temple because the Lamb is himself the presence-of-God that the ark symbolized; Jeremiah's prediction that the ark would not be missed is finally true when God himself dwells with his people"}
    ],
    "17": [
      {"type": "allusion", "target": "Rev 21:24-26", "note": "At that time Jerusalem will be called the throne of the LORD, and all nations will gather to it — the eschatological pilgrimage of nations to Jerusalem; the nations will walk by its light and bring their glory into the new Jerusalem (Rev 21:24-26); Jer 3:17's vision of a multi-national Jerusalem-centered worship is the OT form of the new Jerusalem's international assembly"}
    ],
    "22": [
      {"type": "allusion", "target": "Luke 15:20", "note": "Return, faithless children, and I will heal your faithlessness — the divine offer of healing for covenant infidelity; the father who runs to meet the prodigal while still far off (Luke 15:20) embodies YHWH's healing-return promise of Jer 3:22; the prodigal's declaration 'here we are, we come to you' (v. 22b) is the human response that Jesus's parable enacts"},
      {"type": "allusion", "target": "Rev 22:17", "note": "The Spirit and the Bride say: Come. And let the one who is thirsty come — the final NT echo of the divine summons to return; the Jeremianic call to return (3:22: return and I will heal) resounds through the closing pages of the canon; the Spirit still summons, the Bride still calls, and all who are thirsty are welcome"}
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHO_2_3)
    save_echo('jeremiah', existing)
    print('Jeremiah 2-3 echoes written.')

if __name__ == '__main__':
    main()
