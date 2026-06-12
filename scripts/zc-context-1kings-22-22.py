"""
MKT Context Commentary — 1 Kings chapter 22
Run: python3 scripts/zc-context-1kings-22-22.py

Ch22: Micaiah's divine council vision — sôḏ YHWH; šālôm-prophecy as professional class;
      the lying spirit — rûaḥ šeqer and ANE prophetic manipulation context;
      Ahab's disguise at Ramoth-Gilead — Thutmose III / ANE parallels; arrow/breastplate gap

ANE/historical context:
- sôḏ YHWH (22:19-22): divine council in ANE — Ugaritic 'assembly of El'; Ps 82
- šālôm prophets (22:6): professional court prophets vs. YHWH's prophet
- rûaḥ šeqer (22:22): lying spirit in YHWH's council — Deut 18 contrast; 2 Thess 2
- Ahab's disguise (22:30): ANE royal disguise at battle — Thutmose III at Megiddo
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
  "22": {
    "19": "<p>Micaiah&rsquo;s vision of YHWH enthroned with &lsquo;all the host of heaven standing beside him on his right and on his left&rsquo; — <em>wāʾerʾeh ʾet YHWH yōšēḇ ʿal kissᵉʾô wᵉḵol ṣᵉḇāʾ haššāmayim ʿōmēḏ ʿālāyw mîmînô ûmiśśᵉmōʾlô</em> — is the OT&rsquo;s most detailed narrative scene in the <em>sôḏ YHWH</em> (divine council). The divine council is attested across the ancient Near East: the Ugaritic texts describe the <em>pḥr ʿilm</em> (assembly of El, or assembly of the gods), presided over by El and attended by the seventy divine sons of El, who debate and deliberate on cosmic matters. The Akkadian <em>puḫrum</em> (assembly) is a governing assembly of the great gods in Mesopotamian mythology. In the OT, the divine council appears in Job 1-2 (the <em>bᵉnê hāʾelōhîm</em> presenting before YHWH), Ps 82 (YHWH stands in the <em>ʿăḏat ʾēl</em> judging the divine beings), Ps 89:7 (<em>biqhal qᵉḏōšîm</em>), and Jer 23:18 (<em>mî ʿāmaḏ bᵉsôḏ YHWH</em> — &lsquo;who has stood in YHWH&rsquo;s council?&rsquo;). What distinguishes the Israelite council vision is YHWH&rsquo;s absolute sovereignty within it: the council deliberates, but YHWH&rsquo;s purpose cannot be frustrated. Micaiah&rsquo;s vision serves the narrative theologically: it relocates the question of Ahab&rsquo;s death from the political sphere (will Jehoshaphat ally?) to the cosmic sphere (what has YHWH decreed?). The outcome was decided in the divine council before Ahab ever consulted a prophet.</p>",
    "22": "<p>The <em>rûaḥ šeqer</em> (lying spirit) episode — a spirit volunteers before the divine council to be &lsquo;a lying spirit in the mouth of all his [Ahab&rsquo;s] prophets&rsquo; (<em>wāʾehyeh rûaḥ šeqer bᵉpî kol nᵉḇîʾāyw</em>) — presents the sharpest theological problem in the divine council scene: YHWH permits a spirit of deception to drive the court prophets&rsquo; false šālôm-oracles. The ANE context illuminates the passage: professional court prophets throughout the ancient Near East were cultic functionaries whose role was to provide oracular legitimation for royal military projects. The Mari letters (18th century BCE) document court prophecy in systematic detail: <em>āpilum</em> and <em>muḫḫûm</em> prophets deliver oracles to the king, often favorable to military ventures. The 400 court prophets consulting Ahab (v6) are this professional class — their šālôm-oracles are structurally predictable. Deut 18:20-22 establishes the test that the Micaiah narrative applies: the prophet who speaks presumptuously in YHWH&rsquo;s name without YHWH&rsquo;s word is a false prophet; the event (Ahab&rsquo;s death) will vindicate Micaiah and condemn the 400. The theological framing — YHWH ordaining the delusion of the court prophets as the instrument of Ahab&rsquo;s judicial death — is the ANE divine-warrior pattern turned inward: the same God who sent hardening on Pharaoh (Exod 10:1) now sends hardening on Israel&rsquo;s own idolatrous king, through the prophets who tell him what he wants to hear.</p>",
    "30": "<p>Ahab&rsquo;s decision to enter the battle at Ramoth-Gilead in disguise (<em>wāhîsṭar melek yiśrāʾēl wayyāḇōʾ bammilḥāmāh</em>) while asking Jehoshaphat to wear his royal robes is a documented ANE military tactic. The Annals of Thutmose III at Megiddo (c.1457 BCE) describe the Egyptian pharaoh donning his battle armor and personally leading the charge at Megiddo in a display of royal heroism — the opposite strategy but part of the same cultural expectation that the king&rsquo;s presence on the battlefield was militarily decisive. The Hittite texts and Assyrian royal annals document royal disguise as a protective measure in contexts where the king&rsquo;s identification by the enemy meant targeted death. Ahab&rsquo;s logic is internally coherent: if Micaiah&rsquo;s oracle is directed at &lsquo;the king of Israel,&rsquo; removing the royal markers should nullify the prediction. The narrative irony is pointed: an Aramean archer draws his bow &lsquo;at random (<em>bᵉtōm</em>)&rsquo; — literally &lsquo;in completeness/innocence,&rsquo; without special aim — and strikes the disguised Ahab at the exact gap between breastplate and armor scale (v34). The disguise defeats human identification but not divine decree: the arrow that was aimed at no one found the one man whose death had been decreed in the divine council of v19-23.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1kings mkt-context: wrote {count} verses across ch 22')

if __name__ == '__main__':
    main()
