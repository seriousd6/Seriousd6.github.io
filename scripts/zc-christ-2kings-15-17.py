"""
MKT Christ Commentary — 2 Kings chapters 15–17
Run: python3 scripts/zc-christ-2kings-15-17.py

Ch15: Uzziah's leprosy — king struck for priestly usurpation / Heb 7:1-3; Mark 1:41
Ch16: Ahaz's faithlessness produces the Immanuel sign — Isa 7:14 / Matt 1:23
Ch17: The prophetic warning summarized — every prophet sent / Matt 23:37; Acts 7:52

Key typological connections:
- 15:5: Uzziah struck with leprosy for entering the sanctuary → Heb 7:1-3 (king-priest legitimacy)
- 16:7: Ahaz sends to Assyria rather than trusting YHWH → Isa 7:14 / Matt 1:23 (Immanuel sign)
- 17:13: YHWH warned by every prophet → Matt 23:37; Acts 7:52 (the final prophet's lament)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

CHRIST = {
  "15": {
    "5": "<p>Uzziah&rsquo;s leprosy — inflicted when he entered the temple to burn incense on the altar of incense, a prerogative belonging to the Aaronide priests alone (2 Chr 26:16-20) — is the OT&rsquo;s most dramatic account of a king struck for crossing the boundary between royal and priestly offices. The Chronicler specifies the precise act: <em>wayyābo&rsquo; ʿuzziyyāhû ʾel bêt YHWH liqṭēr ʿal mizbah haqqᵉṭōret</em>, &lsquo;Uzziah went into the house of YHWH to burn incense on the altar of incense&rsquo; — the initiative of a king who sought to unite in himself what the Mosaic constitution separated. The leprosy is the sign of his exclusion: he was thrust out of the sanctuary and remained leprous to his death, dwelling in a separate house while his son Jotham governed. The theological pattern is the inverse of what Heb 7:1-3 describes in Melchizedek and applies to Christ: <em>aphōmoiōmenos de tō hyiō tou theou, menei hiereus eis to diēnekes</em> — &lsquo;resembling the Son of God, he remains a priest forever.&rsquo; Melchizedek holds both royal and priestly dignity legitimately — king of Salem, priest of God Most High — because the two offices were never separated in his person. Uzziah&rsquo;s attempted unauthorized fusion (and its punishment) marks the limit of the Davidic kingship within the Mosaic constitution: no Davidic king could be priest under the Levitical law. Jesus exceeds both offices through a different order altogether — &lsquo;not according to the law of a fleshly commandment but according to the power of an indestructible life&rsquo; (Heb 7:16). Jesus&rsquo;s touching of lepers (Mark 1:41-42) — the one who makes the unclean clean — also reverses the Uzziah pattern: where Uzziah&rsquo;s sanctuary-entry made the king leprous, Jesus&rsquo;s touch makes the leprous clean.</p>"
  },
  "16": {
    "7": "<p>Ahaz&rsquo;s message to Tiglath-pileser of Assyria — <em>ʿaḇdᵉḵā ûḇinᵉḵā ʾānî</em>, &lsquo;I am your servant and your son&rsquo; — is the OT&rsquo;s most explicit instance of a Davidic king using covenant sonship language to a foreign king rather than to YHWH. The language <em>ʿeḇeḏ</em> (servant) and <em>bēn</em> (son) is the vocabulary of the Davidic covenant itself: 2 Sam 7:14 (&lsquo;I will be his father and he shall be my son&rsquo;) and Ps 2:7 (&lsquo;You are my son; today I have begotten you&rsquo;) define the king&rsquo;s relationship to YHWH. Ahaz deploys this language toward the Assyrian king precisely because he refuses to trust YHWH for deliverance from the Syro-Ephraimite coalition. Isaiah&rsquo;s confrontation with Ahaz at this moment (Isa 7:1-17) ends with the Immanuel sign given because Ahaz refused to ask for one: <em>hinnēh hāʿalmāh hārāh wᵉyōleḏet bēn wᵉqārāʾt šᵉmô ʿimmānûʾēl</em> — &lsquo;behold, the virgin/young woman shall conceive and bear a son, and shall call his name Immanuel.&rsquo; Matt 1:23 cites this verse as fulfilled in Jesus&rsquo;s birth: <em>idou hē parthenos en gastri hexei kai texetai hyion, kai kalesousin to onoma autou Emmanouel</em>. The chain is theologically precise: Ahaz&rsquo;s refusal to trust YHWH and his deployment of covenant-sonship language to a human king produces the sign of the true Son whose name means &lsquo;God with us.&rsquo; At the baptism, the Father declares <em>houtos estin ho huios mou ho agapētos</em> — &lsquo;this is my beloved Son&rsquo; (Matt 3:17) — the pronouncement Ahaz refused to receive. Christ is the answer to Ahaz: the Son who is YHWH&rsquo;s servant (Isa 42:1) and YHWH&rsquo;s Son (Ps 2:7) in the fullness that the Davidic covenant always pointed toward.</p>"
  },
  "17": {
    "13": "<p>The Deuteronomistic historian&rsquo;s summary of the entire prophetic mission to Israel and Judah — <em>wayyāʿaḏ YHWH bᵉyiśrāʾēl ûḇîhûḏāh bᵉyaḏ kol nᵉḇîʾê kol ḥōzeh lēʾmōr šûḇû miḏḏarḵêḵem hārāʿôt</em>, &lsquo;yet YHWH warned Israel and Judah by every prophet and every seer, saying: Turn from your evil ways and keep my commandments and my statutes&rsquo; — is the OT&rsquo;s most comprehensive statement of the prophetic mission as warning-before-judgment. The entire prophetic corpus is here summarized as a sustained act of YHWH&rsquo;s patience: every prophet sent, every seer commissioned, all bearing the same summons to return. The nation refused. Jesus&rsquo;s lament over Jerusalem in Matt 23:37 inhabits this same framework: <em>Ierousalēm Ierousalēm hē apokteinousa tous prophētas kai lithobologousa tous apestalmenos pros autēn, posakis ēthelēsa episynagagein ta tekna sou</em> — &lsquo;O Jerusalem, Jerusalem, the city that kills the prophets and stones those who are sent to it! How often would I have gathered your children together as a hen gathers her brood under her wings, and you were not willing.&rsquo; The structure is identical: YHWH sent every prophet; Israel refused every prophet; judgment followed. Jesus as the final and definitive sender-and-sent (John 20:21: &lsquo;as the Father has sent me, even so I am sending you&rsquo;) is the culmination of the prophetic mission that 17:13 summarizes. Stephen in Acts 7:52 makes the typological sequence explicit: <em>tina tōn prophētōn ouk ediōxan hoi pateres hymōn</em> — &lsquo;which of the prophets did your fathers not persecute?&rsquo; — and concludes with the betrayal and murder of &lsquo;the Righteous One.&rsquo; The 17:13 summary is the OT&rsquo;s own retrospective on why the Servant who was sent had to be rejected.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '2kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '2kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'2kings mkt-christ: wrote {count} verses across ch 15-17')

if __name__ == '__main__':
    main()
