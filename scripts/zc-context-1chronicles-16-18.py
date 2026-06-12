"""
MKT Context Commentary — 1 Chronicles chapters 16–18
Run: python3 scripts/zc-context-1chronicles-16-18.py

Ch16: Composite psalm from Ps 105 + Ps 96 + Ps 106 — anthological composition technique (16:8-36)
      Dual sanctuary: Ark in Jerusalem / tabernacle at Gibeon (16:39-40)
Ch17: Nathan's oracle refusing David — ANE temple-building divine authorization parallels (17:3)
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

CONTEXT = {
  "16": {
    "8": "<p>The psalm the Chronicler places in David&rsquo;s mouth at the Ark&rsquo;s installation in Jerusalem (16:8-36) is a composite text assembled from three canonical psalms: vv8-22 = Ps 105:1-15, vv23-33 = Ps 96:1-13, vv34-36 = Ps 106:1 + 47-48. The Chronicler creates a new liturgical poem by weaving together existing psalmic material — a technique scholars call &lsquo;anthological composition&rsquo; or &lsquo;innerbiblical exegesis.&rsquo; This practice — using earlier sacred texts as raw material for new compositions — is attested across ancient Near Eastern and Second Temple Jewish literature: the Dead Sea Scrolls contain the 11QPsalms scroll (11QPsa), which rearranges and interpolates biblical psalms with additional compositions; the Hodayot (1QH, Thanksgiving Hymns) weave together biblical language into new forms; and the Temple Scroll (11QT) creates a new legal-liturgical text by fusing and reworking Deuteronomy and Leviticus. The Chronicler&rsquo;s composite psalm is the OT&rsquo;s clearest instance of this method: specific psalms are selected and combined, with the composite serving the narrative purpose of an inaugural liturgy for the Ark&rsquo;s permanent home. The same impulse — creating new sacred text through the reuse of authorized sacred text — drives both the Chronicler&rsquo;s liturgical compilation and the NT&rsquo;s citation-chain compositions (e.g., Rom 3:10-18, which chains seven OT citations; Heb 1:5-13, citing six OT texts in succession).</p>",
    "39": "<p>The Chronicler&rsquo;s notation that Zadok the priest and his fellow priests continued to minister before the tabernacle at Gibeon (16:39-40) while Asaph ministered before the Ark in Jerusalem establishes a historically unusual dual-sanctuary situation: two legitimate cult sites operating simultaneously, with different personnel and different sacred objects. Gibeon&rsquo;s priority as a high place is confirmed by 1 Kgs 3:4, where Solomon went to Gibeon to sacrifice &lsquo;for that was the great high place,&rsquo; and where YHWH appeared to him in the dream. The Chronicler, writing after the temple was built and the dual-sanctuary period long past, preserves this detail to explain a problem: why was Solomon at Gibeon (not Jerusalem) for his inaugural sacrifice? The answer the Chronicler implies is that Gibeon was the Mosaic-tabernacle site, which retained legitimacy during the interregnum between Ark-installation (David) and temple-dedication (Solomon). The archaeological evidence for Gibeon&rsquo;s cultic role beyond the Pritchard excavations is limited, but the Chronicler&rsquo;s explicit account of Gibeon as the location of the Mosaic tabernacle during David&rsquo;s reign is the primary textual evidence for this dual-sanctuary hypothesis, which has no ANE direct parallel but reflects the broader principle that pre-temple Israel maintained multiple legitimate cult sites before centralization.</p>"
  },
  "17": {
    "3": "<p>YHWH&rsquo;s word through Nathan refusing David&rsquo;s temple plan — &lsquo;It was not you who built me a house to dwell in... I have not dwelt in a house since the day I brought up Israel to this day, but I have gone from tent to tent and from dwelling to dwelling&rsquo; (17:5-6) — places the proposed temple in a theological context: YHWH&rsquo;s presence has been mobile, not fixed. In the ANE, temple-building required explicit divine authorization, often received through dreams, omens, or oracular inquiry. The most elaborate example is the &lsquo;Cylinder of Gudea&rsquo; (Gudea of Lagash, ca. 2100 BCE), which describes in detail the Sumerian ruler&rsquo;s reception of divine temple-building authorization in a dream, including the architectural blueprint delivered by the god Ningirsu. Neo-Assyrian and Neo-Babylonian kings similarly claimed divine mandate for temple-restoration projects: Nabonidus of Babylon records detailed accounts of divine instructions to restore the temple of the moon-god Sin at Harran. YHWH&rsquo;s refusal through Nathan is thus the inverse of the expected ANE pattern: the king proposes the temple; the god declines and redirects (the building will be done by a son, not the king). The Chronicler&rsquo;s emphasis on this refusal is also an implicit apologetic: David&rsquo;s non-building of the temple was not a failure of piety but a divine decision that actually honored David (&lsquo;I have been with you wherever you went&rsquo;, v8). The divine-authorization pattern that Gudea and the Assyrian kings received through vision, David receives through oracle — and what he receives is a dynasty rather than a building.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1chronicles')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1chronicles', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1chronicles mkt-context: wrote {count} verses across ch 16-18')

if __name__ == '__main__':
    main()
