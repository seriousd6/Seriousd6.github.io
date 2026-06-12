"""
MKT Context Commentary — 1 Chronicles chapters 26–28
Run: python3 scripts/zc-context-1chronicles-26-28.py

Ch26: Gatekeeper system — ANE temple-guard parallels; treasury officials (26:12)
Ch27: David's census refusal under-20s — Abrahamic stars-promise contrast with ch21 census (27:23)
Ch28: The tabnît blueprint — Exodus 25 pattern + ANE divine architectural revelation parallels (28:11)
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
  "26": {
    "12": "<p>The organization of gatekeepers (<em>šôʿărîm</em>) into divisions stationed at the four cardinal gates of the temple complex (26:13-18 specifies Shalleketh gate on the west causeway, the storehouse gate, the portico) reflects a pattern of temple security administration attested widely in the ANE. Egyptian New Kingdom temple complexes maintained permanent gate-guard contingents recorded in administrative papyri — the Wilbour Papyrus (c. 1143 BCE) references temple-affiliated land assignments for gate-personnel. Mesopotamian temples employed <em>atû</em>-gatekeepers whose duties included ritual purity control as well as physical security; Ur III administrative texts from Nippur record grain rations for gatekeeper contingents at the Ekur temple. At Ugarit, the <em>ṯʿrm</em> (gatekeepers) appear in administrative lists alongside temple craftsmen. The Jerusalem gatekeeper system&rsquo;s organizational sophistication — lots for the south gate, four-per-day at the causeway, six at the storehouses (26:17-18) — reflects a complex administrative structure typical of major ANE temple establishments. The Chronicler&rsquo;s detail that the gatekeepers were also responsible for the treasuries (26:20-28) reflects the ANE practice of integrating access-control and asset-management: gate-personnel controlled not only physical ingress but the flow of dedicated offerings and war-spoil deposits. The post-exilic Levitical community that read Chronicles would have recognized their own institutions in this Davidic precedent — Neh 12:25 mentions Nehemiah-era gatekeepers at the same stations.</p>"
  },
  "27": {
    "23": "<p>The notation that David &lsquo;did not take the number of those from twenty years old and below, because YHWH had said he would increase Israel like the stars of the heavens&rsquo; (<em>kᵉḵôḵᵉḇê haššāmayim</em>) is a pointed contrast with the sinful census of ch 21 (= 2 Sam 24), where David counted the fighting men and brought divine punishment. The Chronicler here notes that David&rsquo;s organizational census of ch 27 deliberately excluded the under-twenties — the group who, by Mosaic law (Num 1:3), were below military census age — and grounds this exclusion in the Abrahamic covenant&rsquo;s multiplication promise (Gen 15:5; 22:17; 26:4). The stars-of-heaven metaphor for Israel&rsquo;s innumerability appears first in the Abrahamic promissory texts and functions as a theological limit on human enumeration: to count all of Israel would presume to measure what God has promised to exceed human counting. The contrast with ch 21 is structural: that census (of fighting men, 1,100,000 + 470,000) triggered plague and required atonement; this census (monthly military rotations, with deliberate exclusion of a segment on covenantal grounds) is an act of proper administrative order. The Chronicler also notes in 27:24 that Joab began but never completed the ch 21 census &lsquo;and it was not entered into the account of the chronicles of King David&rsquo; — the aborted sinful census is explicitly excluded from official record, whereas ch 27&rsquo;s administrative roster is canonical record. The episode illustrates the Chronicler&rsquo;s consistent principle: enumeration that acknowledges divine boundaries is legitimate; enumeration that implicitly claims exhaustive sovereignty belongs to YHWH alone is dangerous.</p>"
  },
  "28": {
    "11": "<p>David&rsquo;s transmission of the architectural plans to Solomon — the <em>tabnît</em> (pattern/blueprint) for the porch, the houses, the inner rooms, the upper chambers, the inner sanctuary, and the place of the ark-cover (28:11-12) — is presented as divinely revealed architecture. 28:19 makes this explicit: &lsquo;All this in writing by the hand of YHWH upon me; all the works of this pattern (<em>tabnît</em>) he made me understand.&rsquo; The word <em>tabnît</em> is the same used in Exod 25:9,40, where Moses is commanded to build the tabernacle &lsquo;according to all that I am showing you, the pattern (<em>tabnît</em>) of the tabernacle and the pattern of all its furnishings.&rsquo; The Chronicler deliberately echoes the Sinai architectural-revelation pattern: as Moses received the tabernacle blueprint on the mountain, David received the temple blueprint by divine inspiration. This places David in a Moses-like role as mediator of divine architectural revelation. The ANE background for divine architectural transmission is the Gudea Cylinder (ca. 2100 BCE), where Ningirsu delivers a temple plan to Gudea in a dream, including the goddess Nisaba holding a lapis-lazuli tablet with the star-map of the house, and a divine builder holding the ground-plan. Neo-Assyrian kings similarly claimed divine direction in temple restoration: Esarhaddon&rsquo;s cylinder inscriptions record that the god Marduk &lsquo;showed me&rsquo; the plan for the Esagila restoration. What distinguishes the Chronicler&rsquo;s account is the written form: &lsquo;in writing by the hand of YHWH upon me&rsquo; — the blueprint comes as written divine communication, not merely a vision, elevating the architectural plan to near-scriptural authority. This has implications for how the temple was understood in post-exilic Judaism: its proportions were not arbitrary but divinely specified, and David&rsquo;s written receipt of the plan provided the authorization-chain that legitimated the Second Temple&rsquo;s claim to continuity with the Solomonic structure.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1chronicles')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1chronicles', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1chronicles mkt-context: wrote {count} verses across ch 26-28')

if __name__ == '__main__':
    main()
