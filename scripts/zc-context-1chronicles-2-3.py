"""
MKT Context Commentary — 1 Chronicles chapters 2–3
Run: python3 scripts/zc-context-1chronicles-2-3.py

Ch2: Perez/Zerah sons of Tamar in the Judahite genealogy — Gen 38's levirate context;
     the royal line descending through the "scandalous" union
Ch3: Zerubbabel's historical placement — Persian-period Davidic governor (Hag 1:1);
     post-exilic genealogy extending 6 generations → dating the Chronicler ca. 400-350 BCE
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
  "2": {
    "4": "<p>The Chronicler&rsquo;s inclusion of Perez and Zerah as sons of Tamar and Judah (Gen 38) in the Judahite genealogy is significant because it embeds the royal line&rsquo;s most irregular origin in the genealogy without comment. Perez (pereṣ = &lsquo;breach&rsquo;) is the ancestor of the Davidic line (2:5 → 2:9-17 → David); the line runs through an act of levirate deception. Gen 38&rsquo;s social-legal context involves the levirate custom (<em>yibbum</em>) by which a surviving brother was obligated to marry a deceased brother&rsquo;s widow to raise up offspring for him (Deut 25:5-10). Judah&rsquo;s failure to give his son Shelah to Tamar (Gen 38:11, 14) and Tamar&rsquo;s initiative to secure her levirate rights through disguised intercourse with Judah are the background. The Chronicler does not retell this — he simply records the names. Ancient genealogies regularly included irregular origins: the Sumerian King List includes kings whose origins involved divine-human relations; the Egyptian royal genealogies occasionally suppress irregular successions. The Chronicler&rsquo;s matter-of-fact inclusion of Tamar&rsquo;s sons reflects the genealogy&rsquo;s purpose: to establish covenant-lineage continuity, not to edit the moral complexity of the ancestors. Matt 1:3 follows the same practice, naming Tamar among the four women in Jesus&rsquo;s genealogy, all of whom have irregular situations.</p>",
    "10": "<p>The genealogical sequence from Ram to Jesse (2:10-12) — Ram, Amminadab, Nahshon, Salmon, Boaz, Obed, Jesse — is the same sequence preserved in Ruth 4:18-22 and reproduced in Matt 1:3-6. The convergence of these three genealogical lists (Chronicles, Ruth, Matthew) on the same ten-generation sequence from Perez to David indicates the stability of this particular lineage tradition in post-exilic Jewish memory. The appearance of Nahshon son of Amminadab is significant: Nahshon was the leader of the tribe of Judah during the wilderness period (Num 1:7; 2:3; 7:12) and is connected to the first tribal offering at the tabernacle&rsquo;s dedication (Num 7:12-17). The genealogy thus links the Davidic line to the wilderness-era tribal leadership and to Aaron (Amminadab&rsquo;s daughter Elisheba married Aaron, Exod 6:23) — providing both royal and priestly genealogical connections for the Davidic lineage. This breadth of connection — Davidic king and Aaronide priest simultaneously connected through Amminadab — is the kind of genealogical significance the post-exilic community, which lacked a king but retained a high priest, would have found theologically resonant.</p>"
  },
  "3": {
    "19": "<p>Zerubbabel, son of Pedaiah (or Shealtiel in Hag 1:1; Ezra 3:2 — a minor genealogical discrepancy, possibly explained by levirate succession), is the most significant post-exilic Davidic figure in the Chronicler&rsquo;s genealogy. Historically, Zerubbabel served as the Persian-appointed governor of Yehud (the province of Judah) under Darius I (ca. 522-486 BCE), as attested in the books of Haggai (Hag 1:1: &lsquo;Zerubbabel son of Shealtiel, governor of Judah&rsquo;) and Zechariah (Zech 4:6-10: YHWH&rsquo;s word to Zerubbabel, &lsquo;not by might, nor by power, but by my Spirit&rsquo;). Haggai addresses Zerubbabel as YHWH&rsquo;s <em>ḥôtām</em> (signet ring, Hag 2:23) — a reversal of the curse on Coniah/Jehoiachin (Jer 22:24, where Coniah is torn off as a signet ring). The Chronicler&rsquo;s extension of the Davidic genealogy six generations beyond Zerubbabel (into figures otherwise unknown: Hananiah, Shelomith, Hashubah, Ohel, Berechiah, Hasadiah, Jushab-hesed in vv19-20; then further in vv21-24) provides a chronological anchor: six generations at 25 years per generation places the Chronicler&rsquo;s composition ca. 400-350 BCE, in the late Persian period. The genealogy demonstrates that the Davidic line survived exile and continued into the Chronicler&rsquo;s own era — a live covenant claim, not merely a historical record.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1chronicles')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1chronicles', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1chronicles mkt-context: wrote {count} verses across ch 2-3')

if __name__ == '__main__':
    main()
