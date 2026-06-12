"""
MKT Original Commentary — 2 Kings chapters 18–20
Run: python3 scripts/zc-original-2kings-18-20.py

Ch18: bāṭaḥ / miḇṭāḥ — Hezekiah's trust; the Rabshakeh's taunt on misplaced trust;
      hebraically ironic use of miḇṭāḥ against the people of trust
Ch19: Hezekiah's prayer — spreading the letter before YHWH; ferāšōn / God-hearing;
      Isaiah's oracle — the 'hook in the nose' oracle (19:28); the remnant
Ch20: ḥizzəqiyyāhû / hizqiyyāhû — Hezekiah's name = 'YHWH has strengthened';
      šûḇ — turning / the sun's shadow going backward; Hezekiah's folly with Babylon

Key Hebrew terms:
- bāṭaḥ (18:5): to trust — Hezekiah's trust in YHWH = the OT's trust-ideal
- ʿal mî bāṭaḥtā (18:20): 'on what do you trust?' — the Rabshakeh's rhetoric
- qaddôš yiśrāʾēl (19:22): Holy One of Israel — Isaiah's central divine title
- hōlēḵ ʾaḥōrannît (20:11): the shadow going backward — sign of Hezekiah's healing
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

ORIGINAL = {
  "18": {
    "5": "<p>The Deuteronomistic verdict on Hezekiah — <em>bYHWH ʾelōhê yiśrāʾēl bāṭaḥ wᵉʾaḥărāyw lōʾ hāyāh kāmōhû bᵉḵōl malkê yᵉhûḏāh wᵉʾăšer hāyû lᵉpānāyw</em>, &lsquo;he trusted in YHWH the God of Israel, so that there was none like him among all the kings of Judah after him, nor among those who were before him&rsquo; — is the highest trust-affirmation in the entire Kings narrative. The verb <em>bāṭaḥ</em> (to trust, to have confidence, to lean upon) and its noun <em>miḇṭāḥ</em> (trust, security, that in which one trusts) are the vocabulary of the Psalter&rsquo;s security-language: Ps 22:5 (&lsquo;in you they trusted and were not put to shame&rsquo;); Ps 62:8 (&lsquo;trust in him at all times, O people&rsquo;); Ps 118:8-9 (&lsquo;it is better to take refuge in YHWH than to trust in man... in princes&rsquo;). The Rabshakeh&rsquo;s taunt (v19-20: <em>ʿal mî bāṭaḥtā</em>, &lsquo;on what do you trust?&rsquo;) systematically attacks every possible object of trust — Egypt, YHWH, Hezekiah&rsquo;s own reforms — as illusory. The confrontation is a theology-of-trust narrative: when all human resources fail, what does <em>bāṭaḥ</em> look like? Hezekiah&rsquo;s response (19:1: tearing his clothes, entering the temple; 19:14-19: spreading the Assyrian letter before YHWH) embodies the answer: trust means bringing the threat into YHWH&rsquo;s presence and leaving it there. Prov 3:5-6 formalizes the Hezekiah paradigm: <em>bᵉṭaḥ ʾel YHWH bᵉḵol libbᵉḵā</em>, &lsquo;trust in YHWH with all your heart.&rsquo;</p>",
    "20": "<p>The Rabshakeh&rsquo;s rhetorical opening — <em>ʾāmar melek ʾaššûr mah habbittāḥôn hazzeh ʾăšer bāṭāḥtā</em>, &lsquo;the king of Assyria says: On what is this confidence/trust (<em>bittāḥôn</em>) on which you rely?&rsquo; — is a philosophical challenge on the nature of trust itself. The noun <em>bittāḥôn</em> (trust, confidence; from <em>bāṭaḥ</em>) is the object of the question: not &lsquo;why do you resist Assyria?&rsquo; but &lsquo;what is the <em>content</em> of your trust?&rsquo; The Rabshakeh&rsquo;s demolition method is systematic: Egypt is a broken reed (v21: <em>ʿal hammišʿenet haqqāneh hārāṣûṣ hazzeh ʿal miṣrāyim</em>); YHWH is not reliable because Hezekiah himself removed the high places (v22); Israel&rsquo;s military resources are inadequate (v23-24). The Rabshakeh has correctly identified the three things a besieged city might trust: foreign alliance, national deity, military strength. His argument fails only because it cannot account for the category he dismisses: YHWH as the one who actually controls Assyrian military campaigns. Paul&rsquo;s <em>pepoithēsis</em> (confidence, trust; the LXX equivalent of <em>bittāḥôn</em>) in Phil 3:3-4 works through the same category: &lsquo;though I myself have reason for confidence in the flesh... whatever gain I had, I counted as loss for the sake of Christ.&rsquo; The Rabshakeh&rsquo;s question — <em>on what do you trust?</em> — is the question that confronts every confidence-claim in the face of overwhelming power.</p>"
  },
  "19": {
    "22": "<p>Isaiah&rsquo;s oracle against Sennacherib — <em>ʾet mî ḥēraptā ûḇizzāltā wᵉʿal mî hărîmōtā qôl wattissāʾ mārôm ʿêneyḵā ʿal qᵉḏôš yiśrāʾēl</em>, &lsquo;Whom have you mocked and reviled? Against whom have you raised your voice and lifted your eyes to the heights? Against the Holy One of Israel!&rsquo; — centers the oracle on the divine title <em>qᵉḏôš yiśrāʾēl</em> (Holy One of Israel). This is Isaiah&rsquo;s characteristic title for YHWH, appearing 25 times in the book of Isaiah (compared to 6 times in all the rest of the OT). The title fuses holiness (<em>qōḏeš</em>) — the absolute otherness and transcendence of YHWH, the unapproachable divine quality that fills the seraphim&rsquo;s hymn in Isa 6:3 (<em>qāḏôš qāḏôš qāḏôš</em>) — with covenant particularity (&lsquo;of Israel&rsquo;). Sennacherib has raised his voice against the one who cannot be approached without dying (Isa 6:5: &lsquo;woe is me! I am undone&rsquo;); his doom is not military defeat but the offense of approaching the unapproachably holy without the mediation that YHWH alone provides. Rev 4:8 takes the seraphic triple-holy into the heavenly court where the four living creatures hymn the eternal God; the NT resolution of holiness is not distance but mediation — the blood of Christ enabling approach to the holy (Heb 10:19: <em>parrēsian eis tēn eisodon tōn hagiōn</em>, &lsquo;confidence to enter the holy places&rsquo;).</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2kings')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2kings', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2kings mkt-original: wrote {count} verses across ch 18-20')

if __name__ == '__main__':
    main()
