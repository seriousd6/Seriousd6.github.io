"""
MKT Original Commentary — 1 Kings chapters 3–5
Run: python3 scripts/zc-original-1kings-3-5.py

Ch3: lēḇ šōmēaʿ — Solomon's 'hearing heart' request; wisdom as gift not seizure;
     ḥoḵmat ʾelōhîm — wisdom of God operating through the king for justice
Ch4: rōḥaḇ lēḇ — 'breadth of heart'; encyclopedic wisdom in ANE context
Ch5: mᵉnûḥāh — sabbatical rest as precondition for temple-building (Heb 3-4)

Key Hebrew terms:
- lēḇ šōmēaʿ (3:9): hearing/listening heart — wisdom as receptive attunement
- ḥoḵmat ʾelōhîm (3:28): wisdom of God — genitive of origin and quality
- rōḥaḇ lēḇ (4:29): breadth/expansiveness of heart — comprehensive wisdom
- mᵉnûḥāh (5:4): rest — the Deuteronomic precondition for the permanent sanctuary
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
  "3": {
    "9": "<p>Solomon&rsquo;s request at Gibeon is for a <em>lēḇ šōmēaʿ</em> — literally &lsquo;a heart that hears/listens,&rsquo; conventionally translated &lsquo;an understanding mind&rsquo; or &lsquo;a discerning heart.&rsquo; The root <em>šāmaʿ</em> is the foundational verb of the Shema (Deut 6:4: <em>šᵉmaʿ yiśrāʾēl</em> — &lsquo;hear, O Israel&rsquo;): to have a <em>lēḇ šōmēaʿ</em> is to internalize the Shema as a disposition — a heart constitutively attuned to receive divine speech and direction. Solomon&rsquo;s request elaborates: <em>lᵉhāḇîn bên ṭôḇ lᵉrāʿ</em> — &lsquo;to discern between good and evil.&rsquo; This is the same discernment capacity associated with the tree of the knowledge of good and evil in Gen 2:9 — but the contrast is structurally significant: Adam and Eve grasped at the knowledge autonomously (<em>ḥāmdāh</em>, Gen 3:6: &lsquo;desirable to make one wise&rsquo;) and received it as curse; Solomon asks for it as a gift, for the benefit of others (v9b: <em>ʾet ʿammᵉḵā haggāḏôl hazzeh</em>, &lsquo;this your great people&rsquo;). The OT wisdom tradition&rsquo;s claim is that <em>ḥoḵmāh</em> is given, not grasped: Prov 2:6, &lsquo;YHWH gives wisdom (<em>nōtēn ḥoḵmāh</em>); from his mouth come knowledge and understanding.&rsquo; Jas 1:5: &lsquo;if any of you lacks wisdom, let him ask God, who gives generously to all without reproach, and it will be given him&rsquo; — the NT application of the Solomonic model: wisdom is the gift of a hearing heart turned toward God.</p>",
    "28": "<p>The people&rsquo;s response to Solomon&rsquo;s judgment — <em>wayyirᵉʾû mippᵉnê hammelek kî rāʾû kî ḥoḵmat ʾelōhîm bᵉqirbô laʿăśôt mišpāṭ</em>, &lsquo;they stood in awe of the king, because they saw that the wisdom of God was in him to do justice&rsquo; — uses <em>ḥoḵmat ʾelōhîm</em> as a genitive of origin and quality. The same construction as <em>ḥardath ʾelōhîm</em> (1 Sam 14:15: a terror of God) marks the superlative divine quality of what is described. The wisdom operating in Solomon is recognized as qualitatively divine because of what it produces: <em>mišpāṭ</em> (justice) that cuts to the hidden reality beneath the surface claim. The OT wisdom tradition traces all such wisdom to its divine source: Prov 8:22 personifies <em>ḥoḵmāh</em> as the first of YHWH&rsquo;s works, present at creation. 1 Cor 1:24 applies this to Christ: &lsquo;Christ the wisdom of God (<em>theou sophian</em>)&rsquo; — not wisdom from God but the embodied divine Wisdom. Col 2:3: &lsquo;in him are hidden all the treasures of wisdom and knowledge.&rsquo; The Solomonic <em>ḥoḵmat ʾelōhîm</em> operating through a human king to produce justice is the institutional precursor to the Logos who &lsquo;became flesh and dwelt among us&rsquo; (John 1:14) as embodied divine Wisdom administering ultimate justice.</p>"
  },
  "4": {
    "29": "<p>The description of Solomon&rsquo;s wisdom uses the phrase <em>rōḥaḇ lēḇ</em> — &lsquo;breadth of heart.&rsquo; <em>Rōḥaḇ</em> (breadth, expanse) applied to the <em>lēḇ</em> (heart/mind) denotes the comprehensive reach of mental and spiritual capacity across every domain. The enumeration that follows (v33: trees from cedar to hyssop; beasts, birds, reptiles, fish) places Solomon in the ANE encyclopedic wisdom tradition: comparable to Egyptian wisdom texts (Amenemopet, Ptah-hotep) and Mesopotamian wisdom literature, where listing natural phenomena was both a demonstration and a form of mastery. The comparison with &lsquo;all the wisdom of the people of the east and all the wisdom of Egypt&rsquo; (v30) locates Solomonic wisdom within, while surpassing, the intellectual traditions of the surrounding cultures. Matt 12:42 supplies the NT contrast application: &lsquo;the queen of the South came from the ends of the earth to hear the wisdom of Solomon, and behold, something greater than Solomon (<em>pleion Solomōnos</em>) is here.&rsquo; The comprehensive <em>rōḥaḇ lēḇ</em> — wisdom extending to every natural domain — is surpassed by the one in whom &lsquo;all the treasures of wisdom and knowledge are hidden&rsquo; (Col 2:3).</p>"
  },
  "5": {
    "4": "<p>Solomon&rsquo;s explanation for why David could not build the temple — that YHWH has now given rest (<em>mᵉnûḥāh</em>) on every side — invokes the Deuteronomic theology of <em>mᵉnûḥāh</em> as the precondition for the permanent sanctuary. Deut 12:9-11 makes centralized worship conditional on YHWH giving Israel rest (<em>hammᵉnûḥāh wᵉhannāḥălāh</em>, &lsquo;the rest and the inheritance&rsquo;): &lsquo;when he gives you rest from all your enemies around you... then to the place that YHWH your God will choose, to make his name dwell there, there you shall bring all that I command you.&rsquo; <em>Mᵉnûḥāh</em> is from the root <em>nûaḥ</em> (to rest, to settle), the same root as Noah&rsquo;s name (Gen 5:29: &lsquo;this one will give us rest&rsquo;), the Ark&rsquo;s settling on Ararat (Gen 8:4), and the Sabbath rest (Gen 2:2: <em>wayyānaḥ</em>). The temple is built in the condition of Sabbath-peace. Heb 3:7–4:11 reads <em>mᵉnûḥāh</em> as the theological category fulfilled by Christ: &lsquo;we who have believed enter that rest (<em>katapausin</em>)&rsquo; (Heb 4:3), and the argument is that the temple&rsquo;s built-in-rest was only a type — since Ps 95:11 (&lsquo;they shall not enter my rest&rsquo;) was spoken after the Sinai-rest and the Canaan-rest had already been achieved, a further <em>mᵉnûḥāh</em> remains. Heb 4:10: &lsquo;whoever has entered God&rsquo;s rest has also rested from his works as God did from his.&rsquo;</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1kings')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1kings', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1kings mkt-original: wrote {count} verses across ch 3-5')

if __name__ == '__main__':
    main()
