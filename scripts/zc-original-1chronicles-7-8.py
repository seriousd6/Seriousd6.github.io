"""
MKT Original Commentary — 1 Chronicles chapters 7–8
Run: python3 scripts/zc-original-1chronicles-7-8.py

Ch7: Beriah folk-etymology — bᵉ-rāʿāh = "in/because of disaster" (7:23)
Ch8: Eshbaal/Merib-baal — the Chronicler's original theophoric names vs.
     Samuel's bōšet (shame) substitutions (8:33-34)
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
  "7": {
    "23": "<p>The naming of Ephraim&rsquo;s son Beriah carries a folk etymology: <em>wayyiqrāʾ ʾet šᵉmô bᵉrîʿāh kî bᵉrāʿāh hāyᵉtāh bᵉḇêtô</em>, &lsquo;and he called his name Beriah because disaster had come to pass (bᵉrāʿāh hāyᵉtāh) in his house.&rsquo; The etymology is a paronomastic play: the name <em>bᵉrîʿāh</em> is heard as <em>bᵉ-rāʿāh</em>, &lsquo;in/with calamity&rsquo; (from the root <em>rāʿaʿ</em>). The occasion is the death of Ephraim&rsquo;s sons at the hands of the men of Gath (v21) — a genealogical fragment not attested elsewhere. The naming-in-grief practice appears throughout the patriarchal narratives: Rachel names her last son Ben-oni (&lsquo;son of my sorrow&rsquo;) before Jacob renames him Benjamin (Gen 35:18); Phinehas&rsquo;s wife names her son Ichabod (&lsquo;no glory&rsquo;) at the loss of the ark (1 Sam 4:21). The Chronicler&rsquo;s inclusion of the Beriah fragment is unusual in a genealogical list — it interrupts the sequence with a narrative moment — suggesting the Chronicler is drawing on an independent tradition about Ephraim&rsquo;s household loss. Beriah&rsquo;s name encodes the family history: his very existence is memorialized as born out of tragedy.</p>"
  },
  "8": {
    "33": "<p>The Chronicler names Saul&rsquo;s sons as Jonathan, Malchishua, Abinadab, and <em>ʾeš baʿal</em> (Eshbaal, &lsquo;man of Baal&rsquo;); Jonathan&rsquo;s son is named <em>mᵉrîḇ baʿal</em> (Merib-baal, &lsquo;Baal contends/pleads&rsquo;). These are the original theophoric names. The parallel passages in Samuel use <em>ʾîšbōšet</em> (Ishbosheth, &lsquo;man of shame&rsquo;) and <em>mᵉpîḇōšet</em> (Mephibosheth, &lsquo;from the mouth of shame&rsquo;) — systematic substitutions of <em>bōšet</em> (shame, disgrace) for <em>baʿal</em>. This scribal practice of replacing Baal-element theophoric names with <em>bōšet</em> is attested across Samuel and reflects the later theological aversion to preserving Baal-names even in personal names from the Saul-David period. The Chronicler preserves the older forms: the theophoric <em>baʿal</em> in these pre-monarchic and early monarchic personal names did not necessarily indicate Baal-worship — <em>baʿal</em> as a common noun means &lsquo;lord&rsquo; or &lsquo;master&rsquo; and was sometimes used of YHWH (Hos 2:16: <em>tiqrᵉʾî ʾîšî wᵉlōʾ tiqrᵉʾî lî ʿôḏ baʿlî</em>, &lsquo;you will call me &ldquo;My Husband&rdquo; and no longer call me &ldquo;My Baal&rdquo;&rsquo; — YHWH himself once called <em>baʿal</em>). The Samuel substitutions are a later editorial censorship; the Chronicler&rsquo;s retention of Eshbaal and Merib-baal reflects either access to earlier sources or a different editorial policy. The LXX often mediates between both traditions.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1chronicles')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1chronicles', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1chronicles mkt-original: wrote {count} verses across ch 7-8')

if __name__ == '__main__':
    main()
