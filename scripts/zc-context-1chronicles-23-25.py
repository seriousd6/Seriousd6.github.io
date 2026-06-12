"""
MKT Context Commentary — 1 Chronicles chapters 23–25
Run: python3 scripts/zc-context-1chronicles-23-25.py

Ch23: Levitical service age lowered from 30 to 20 — tabernacle portage function obsolete (23:27)
Ch24: Twenty-four priestly divisions by lot — mishmarot calendar confirmed by Qumran 4Q320-4Q329 (24:10)
Ch25: Temple musicians nāḇāʾ (prophesying) — ANE cultic music as divine communication (25:1)
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
  "23": {
    "27": "<p>David&rsquo;s revision of the Levitical service age is an institutional reform with explicit theological rationale. Numbers 4:3 set the original age at thirty years (&lsquo;from thirty years old and above, even to fifty years old&rsquo;) for those who carried the tabernacle; Numbers 8:24-25 set initial service at twenty-five, with heavy portage duties beginning at thirty. The Chronicler records David&rsquo;s lowering of the service threshold to twenty (23:24, 27) and explicitly grounds this in a changed function: &lsquo;because the Levites are no longer required to carry the tabernacle or any of the vessels used in its service&rsquo; (23:26). The portage requirement — the primary reason for the age-thirty minimum — had become obsolete once the Ark had a fixed sanctuary. The Chronicler presents David&rsquo;s reform not as a departure from Mosaic law but as a contextual application: the law&rsquo;s provisions were calibrated to wilderness conditions; settled sanctuary conditions call for different staffing requirements. This principle of institutional adaptation to changed function parallels the Mishnah&rsquo;s later discussions of which Mosaic agricultural laws apply outside the land of Israel, and the Dead Sea Scrolls&rsquo; Temple Scroll (11QT), which extensively reworks Mosaic regulations to fit its idealized settled-temple situation. The Chronicler thus presents David as a reforming administrator whose changes are theologically grounded, not arbitrary &mdash; a portrait the Chronicler consistently maintains: David reorganizes the cult with divine sanction, not personal authority.</p>"
  },
  "24": {
    "10": "<p>The assignment of the &lsquo;eighth lot to Abijah&rsquo; (<em>laʾăḇîyāh haššᵉmînî</em>) is one of the most consequential details in the priestly division list, precisely because Luke 1:5 names Zechariah, the father of John the Baptist, as belonging to &lsquo;the division of Abijah&rsquo; (<em>ἐφημερίας Ἀβιά</em>). But the immediate historical context of 1 Chr 24 is the establishment of the twenty-four priestly courses — the <em>mishmarot</em> (watches/divisions) — by lot: Eleazar&rsquo;s line produced sixteen courses, Ithamar&rsquo;s eight, allocated by sacred lot-casting in the presence of Zadok and Ahimelech (24:3-6). This twenty-four division system became the organizing structure of Second Temple Jewish priesthood and calendar. The Dead Sea Scrolls provide the most detailed external evidence for the ongoing use of this system: the <em>mishmarot</em> documents from Cave 4 (4Q320, 4Q321, 4Q321a, 4Q322-4Q329) preserve calendrical texts tracking which priestly division was on duty for each Sabbath and new moon across six-year cycles. These documents, dating to the 1st century BCE, confirm that the Chronicler&rsquo;s division framework remained operative and administratively central in Second Temple practice. The lot-casting procedure itself — assigning order by sacred chance — reflects the Urim/Thummim tradition (Prov 16:33: &lsquo;The lot is cast into the lap, but its every decision is from YHWH&rsquo;), treating random selection as a mechanism for divine ordering rather than human preference.</p>"
  },
  "25": {
    "1": "<p>The Chronicler&rsquo;s description of the temple musicians as those who &lsquo;prophesied (<em>hannibāʾîm</em>) with lyres, harps, and cymbals&rsquo; — using the Hiphil participle of <em>nāḇāʾ</em>, the standard verb for prophetic speech — is a deliberate theological classification: temple music is a form of inspired communication, not merely aesthetic performance. The same verb root produces <em>nāḇîʾ</em> (prophet). The three guilds — Asaph, Heman, and Jeduthun — each receive this designation: Asaph prophesied &lsquo;under the direction of the king&rsquo; (25:2); the sons of Jeduthun prophesied &lsquo;with the lyre in thanksgiving and praise&rsquo; (25:3); Heman is called &lsquo;the king&rsquo;s seer in the words of God&rsquo; (<em>ḥōzeh hammelek bᵉdiḇrê hāʾelōhîm</em>, 25:5). ANE parallels for cultic music as prophetic/oracular activity are extensive: at Ugarit, the <em>šr</em>im (singers) held official cultic status alongside priests; the Mesopotamian <em>kalû</em>-priest (lamentation singer) and <em>nāru</em> (musician-singer) used music specifically as a means of communicating grief and petition to the deity, functioning in a quasi-prophetic role during temple rituals; Egyptian temple musicians, the <em>ḥsyt</em> (&lsquo;praised/praising ones&rsquo;), held hereditary priestly rank. What distinguishes the Chronicler&rsquo;s presentation is the explicit use of prophetic vocabulary: the singers are not merely skilled performers but inspired speakers — their music is divine speech in musical form. This understanding underlies the NT treatment of the Psalms as prophetic (Acts 2:30-31, treating Ps 16 as David &lsquo;being a prophet&rsquo;) and the use of psalmic texts as oracular predictive material throughout the NT.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1chronicles')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1chronicles', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1chronicles mkt-context: wrote {count} verses across ch 23-25')

if __name__ == '__main__':
    main()
