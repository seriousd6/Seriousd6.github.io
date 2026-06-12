"""
MKT Original Commentary — 2 Samuel chapter 24
Run: python3 scripts/zc-original-2samuel-24-24.py

Ch24: The census and its aftermath — the two-level causality problem (YHWH/Satan);
      David's choice of punishment: 'let me fall into the hand of YHWH';
      the threshing floor of Araunah as the Moriah convergence point;
      David's refusal of the free gift: 'I will not offer what costs me nothing'

Key Hebrew terms:
- wayyasep ʾap YHWH (24:1): YHWH's anger as the hidden cause — cf. 1 Chr 21:1 (Satan)
- wayyinnāḥem YHWH (24:16): YHWH relents — same nāḥam as Gen 6:6, 1 Sam 15:11
- lōʾ ʾaʿăleh ḥinnām (24:24): 'I will not offer for nothing' — the costly-sacrifice principle
- har hammôriyyāh (2 Chr 3:1): Araunah's threshing floor = Moriah = temple mount
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
  "24": {
    "1": "<p>The census narrative opens with the most theologically contested verse in 2 Samuel: <em>wayyōsep ʾap YHWH laḥărōt bᵉyiśrāʾēl wayyāset ʾet dāwiḏ bāhem lēmōr lēḵ mᵉneh ʾet yiśrāʾēl wᵉʾet yᵉhûḏāh</em> — &lsquo;the anger of YHWH was kindled again against Israel, and he incited David against them, saying, &ldquo;Go, number Israel and Judah.&rdquo;&rsquo; The parallel account in 1 Chr 21:1 substitutes &lsquo;Satan&rsquo; for YHWH as the inciting agent: <em>wayyāqom śāṭān ʿal yiśrāʾēl wayyāset ʾet dāwiḏ</em> — &lsquo;Satan stood against Israel and incited David.&rsquo; The two accounts describe the same event from the two levels of OT causality that Job 1-2 makes structurally explicit: YHWH is the primary agent whose sovereign purpose operates through secondary agents including the adversary. The census narrative thus has the same double-agency structure as the Joseph story (Gen 50:20), the hardening of Pharaoh (Exod 4:21 + 7:13), and ultimately the crucifixion (Acts 2:23: &lsquo;this Jesus, delivered up according to the definite plan and foreknowledge of God... you crucified and killed by the hands of lawless men&rsquo;). The two-level causality is not a theological confusion but the OT&rsquo;s most honest account of how divine sovereignty and creaturely agency operate simultaneously without collapsing into each other.</p>",
    "14": "<p>David&rsquo;s choice between the three punishments: <em>ṣar lî māʾōḏ nipolāh nāʾ bᵉyaḏ YHWH kî rabbîm raḥămāyw ûḇᵉyaḏ ʾāḏām ʾal ʾeppōlāh</em> — &lsquo;I am in great distress. Let me fall into the hand of YHWH, for his mercy (<em>raḥămîm</em>) is great; but let me not fall into the hand of man.&rsquo; David&rsquo;s theological preference for divine discipline over human punishment is grounded in the comparative mercy argument: YHWH&rsquo;s <em>raḥămîm</em> (mercies, from <em>reḥem</em>, womb — the Hebrew term for the most intimate form of compassionate attachment) is greater than any human alternative. The word <em>raḥămîm</em> is the plural of intensity — mercies upon mercies. This appeal to YHWH&rsquo;s <em>raḥămîm</em> is the same ground on which Lam 3:22 rests (&lsquo;it is of YHWH&rsquo;s ḥasādîm that we are not consumed; his raḥămîm never come to an end&rsquo;) and on which Paul declares &lsquo;God of all comfort&rsquo; (2 Cor 1:3 — the Greek <em>oiktirmōn</em> translating <em>raḥămîm</em>). David&rsquo;s prayer-logic — preferring the punishment of the merciful God over the punishment of merciless men — is the theological ground of the NT&rsquo;s call to fear God rather than man (Matt 10:28).</p>",
    "18": "<p>The site of David&rsquo;s altar-purchase converges three great redemptive-historical moments on a single geographic point. Araunah&rsquo;s threshing floor (<em>gōren ʾărawnāh</em>) on the ridge above Jerusalem is identified in 2 Chr 3:1 as <em>har hammôriyyāh</em> — the Mount Moriah where Solomon builds the temple. This is the same Moriah where Abraham bound Isaac for sacrifice (Gen 22:2: &lsquo;go to the land of Moriah and offer him there as a burnt offering&rsquo;). The triple convergence — (1) Abraham&rsquo;s near-sacrifice on Moriah where YHWH provides a substitute; (2) David&rsquo;s altar-building where the plague is arrested; (3) Solomon&rsquo;s temple where YHWH&rsquo;s presence dwells — makes this the most theologically dense sacred site in the OT, and its anti-type is Golgotha, the hill just outside Jerusalem where the ultimate substitute is offered. The trajectory: Moriah (substitutionary provision), Moriah-as-temple (ongoing atonement), Golgotha (final atonement) — three moments on a single theological line, geographically proximate.</p>",
    "24": "<p>David&rsquo;s refusal of Araunah&rsquo;s free gift: <em>lōʾ wᵉlōʾ ʾeqnaʾ mēʿimmᵉḵā bᵉmāḥîr wᵉlōʾ ʾaʿăleh laYHWH ʾelōhay ʿōlôt ḥinnām</em> — &lsquo;No, I insist on buying it from you for a price; I will not offer burnt offerings to YHWH my God that cost me nothing (<em>ḥinnām</em>).&rsquo; The word <em>ḥinnām</em> (free, for nothing, without cost) is used in Job 1:9 (&lsquo;does Job fear God for nothing?&rsquo;) and in Mal 1:10 (YHWH&rsquo;s rebuke of those who perform the motions of worship without genuine commitment). David&rsquo;s statement defines authentic worship: the sacrifice that costs nothing is not sacrifice. The NT amplifies this: Paul&rsquo;s living sacrifice (Rom 12:1: &lsquo;present your bodies as a living sacrifice, holy and acceptable to God, which is your spiritual worship&rsquo;) and Jesus&rsquo;s parables of the treasure and the pearl (Matt 13:44-46: &lsquo;in his joy he goes and sells all that he has and buys that field&rsquo;) — authentic worship and authentic discipleship both cost everything. The free gift refused models the opposite of cheap grace: the worshipper who will not bring to God what costs him nothing has understood something that many who perform free worship have not.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2samuel')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2samuel', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2samuel mkt-original: wrote {count} verses across ch 24')

if __name__ == '__main__':
    main()
