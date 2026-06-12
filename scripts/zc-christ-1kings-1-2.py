"""
MKT Christ Commentary — 1 Kings chapters 1–2
Run: python3 scripts/zc-christ-1kings-1-2.py

Ch1: Solomon's messianic anointing at Gihon — horn of oil / Acts 10:38 / Ps 45:7;
     Davidic promise fulfilled in Solomon's living enthronement — Acts 2:30
Ch2: David's death and tomb — Acts 2:29-31 (Peter's Pentecost exegesis);
     Zadok as sole high priest — Abiathar removed / Heb 7 priestly replacement

Key typological connections:
- 1:39: horn-of-oil anointing → Acts 10:38; Heb 1:9 (anointed with oil of gladness)
- 1:48: living father sees son enthroned → Acts 2:30 (David as prophet of the resurrection)
- 2:10: David slept/buried → Acts 2:29-31 (Peter: tomb still present; resurrection required)
- 2:35: Zadok sole priest → Heb 7:12, 28 (change of priesthood = change of law)
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
  "1": {
    "39": "<p>Zadok the priest takes the horn of oil from the tent (<em>mēhāʾōhel</em>) and anoints Solomon king — <em>wayyimšaḥ ʾet šᵉlōmōh wayyitqᵉʿû baššôpār wayyōʾmᵉrû kol hāʿām yᵉḥî hammelek šᵉlōmōh</em>, &lsquo;and all the people shouted, &ldquo;Long live King Solomon!&rdquo;&rsquo; — the formal royal anointing that establishes Solomon as YHWH&rsquo;s <em>māšîaḥ</em> (anointed one). The horn of oil from the tabernacle-tent connects the anointing to the full Levitical consecration tradition, and the anointed king enters the category that the prophets will eventually extend to the coming deliverer. Peter in Acts 10:38 names the fulfillment: &lsquo;God anointed Jesus of Nazareth with the Holy Spirit and with power&rsquo; — the <em>echrisen auton ho theos pneumati hagiō</em> echoes the Hebrew anointing pattern, the Spirit-anointing replacing the horn of oil. Ps 45:7 (&lsquo;God, your God, has anointed you with the oil of gladness beyond your companions&rsquo;) is cited in Heb 1:9 as spoken directly to the Son: the royal anointing of the Davidic line reaches its definitive expression in the Son whom God anoints with the oil of gladness — the Spirit-anointing that descends at his baptism (Luke 3:22), fulfilling Isa 61:1 (&lsquo;the Spirit of the Lord is upon me, because he has anointed me&rsquo;). The anointing at Gihon is the founding moment of the messianic anointing tradition that culminates in the one whose title is simply &lsquo;The Anointed.&rsquo;</p>",
    "48": "<p>David&rsquo;s blessing on hearing of Solomon&rsquo;s anointing — <em>bārûḵ YHWH ʾelōhê yiśrāʾēl ʾăšer nātan hayyôm yōšēḇ ʿal kissᵉʾî wᵉʿênay rōʾôt</em>, &lsquo;blessed be YHWH the God of Israel who has granted today one to sit on my throne, my own eyes seeing it&rsquo; — functions as the living king&rsquo;s prophetic acknowledgment that the succession promise has been kept. Peter in Acts 2:30 identifies David as a prophet who knew &lsquo;that God had sworn with an oath to him that he would set one of his descendants on his throne&rsquo; (<em>ek karpou tēs osphyos autou kathisai epi ton thronon autou</em>). The prophetic structure is identical: David speaks about a son who will occupy his throne. But Acts 2:30 inserts the resurrection as the mechanism — it is not Solomon but the resurrected Son of David who fulfills the eternal dynasty promise (2 Sam 7:12-13, 16). David saw Solomon and blessed YHWH; Peter argues that David, as a prophet, &lsquo;foresaw and spoke about the resurrection of the Christ&rsquo; (Acts 2:31). Solomon&rsquo;s enthronement is the type-fulfillment that establishes the pattern; the antitype is the resurrection-enthronement of Jesus at the right hand of God (Acts 2:33) — the permanent occupation of David&rsquo;s throne that Solomon&rsquo;s mortal reign could only temporarily prefigure.</p>"
  },
  "2": {
    "10": "<p>The notice of David&rsquo;s death — <em>wayyiškaḇ dāwîḏ ʿim ʾăḇōtāyw wayyiqqāḇēr bᵉʿîr dāwîḏ</em>, &lsquo;David slept with his fathers and was buried in the city of David&rsquo; — becomes the textual anchor for Peter&rsquo;s Pentecost argument in Acts 2:29-31. Peter explicitly states: &lsquo;Brothers, I may say to you with confidence about the patriarch David that he both died and was buried, and his tomb is with us to this day (<em>to mnēma autou estin en hēmin achri tēs hēmeras tautēs</em>).&rsquo; The tomb&rsquo;s verifiable presence demolishes any interpretation that Ps 16:10 (&lsquo;you will not abandon my soul to Hades or let your Holy One see corruption&rsquo;) was fulfilled in David himself — David did see corruption; his tomb is there. Therefore Ps 16 must speak of a different David-shaped figure — the descendant on whose behalf David wrote prophetically. Acts 13:36 sharpens the argument: &lsquo;David, after he had served the purpose of God in his own generation, fell asleep and was laid with his fathers and saw corruption; but he whom God raised up did not see corruption.&rsquo; The death-and-burial notice of 1 Kgs 2:10 is the historical datum that Peter and Paul treat as the falsifying condition on any non-resurrection reading of the Davidic psalms: David&rsquo;s tomb proves that the resurrection of Christ is not secondary Pauline theology but the claim upon which the entire Davidic covenant finds its only non-disappointing fulfillment.</p>",
    "35": "<p>Solomon&rsquo;s removal of Abiathar from the high-priestly office and installation of Zadok as sole priest — <em>wayyāśem hammelek ʾet ṣāḏôq kōhēn taḥat ʾeḇyāṯār</em>, &lsquo;the king put Zadok the priest in place of Abiathar&rsquo; — fulfills the judgment oracle against Eli&rsquo;s house (1 Sam 2:31-36) and establishes a sole priestly line for Solomon&rsquo;s reign. This priestly replacement is the OT type for the argument of Heb 7: &lsquo;if perfection had been attainable through the Levitical priesthood... what further need would there have been for another priest to arise after the order of Melchizedek?&rsquo; (Heb 7:11). Heb 7:12 states the principle: &lsquo;for when there is a change in the priesthood, there is necessarily a change in the law as well.&rsquo; The Zadokite replacement of the Elide/Abiatharite line demonstrates that the Levitical order was already revisable within the OT itself — the removal of one priestly line for another is not a foreign imposition but a pattern embedded in the system. Abiathar is sent alive to his estate at Anathoth (v26), excluded but not executed. Heb 7:28 names the consummation: &lsquo;the law appoints men in their weakness as high priests, but the word of the oath, which came later than the law, appoints a Son who has been made perfect forever.&rsquo; The Abiathar-to-Zadok succession is the OT form of the principle that the Levitical priesthood was never the terminus — always a type awaiting the priest after the order of Melchizedek whose appointment is by divine oath and whose office is eternal.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1kings mkt-christ: wrote {count} verses across ch 1-2')

if __name__ == '__main__':
    main()
