"""
MKT Christ Commentary — 1 Kings chapters 12–14
Run: python3 scripts/zc-christ-1kings-12-14.py

Ch12: Kingdom divided as YHWH's judicial act — the torn garment / Ahijah prophecy;
      Jeroboam's golden calves as idolatry paradigm — Exod 32 echo
Ch13: Man of God from Judah and the lion — sign of the altar / 2 Kgs 23 fulfillment
Ch14: Ahijah's oracle of total dynasty judgment — no undivided heart; Asa contrast

Key typological connections:
- 12:15: kingdom-division as YHWH's judicial act → Matt 21:43 (kingdom taken and given)
- 12:28: golden calves / 'your gods who brought you up' → 1 Cor 10:7; Rom 1:23
- 13:2: altar-sign naming Josiah → 2 Kgs 23:15-16 (fulfilled 300 years later); Acts 4:28
- 14:8: Jeroboam did not follow YHWH as David → contrast with David as covenant type
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
  "12": {
    "15": "<p>The narrator&rsquo;s explanation for Rehoboam&rsquo;s refusal to listen to the elders — <em>kî hāyᵉtāh sib bāh mēʿim YHWH lᵉmaʿan hāqîm ʾet dᵉḇārô ʾăšer dibber YHWH bᵉyaḏ ʾăḥiyyāh haššîlōnî</em>, &lsquo;for it was a turn of affairs brought about by YHWH that he might fulfill his word&rsquo; — applies the Deuteronomic theological principle: the political fracture of the unified monarchy is not a historical accident but the fulfillment of Ahijah&rsquo;s torn-garment oracle (11:29-39). YHWH works through human foolishness (Rehoboam&rsquo;s harsh response) to accomplish his decreed judgment. Matt 21:43 applies this same kingdom-transfer logic in its final form: <em>dia touto legō hymin hoti arthēsetai aph&rsquo; hymōn hē basileia tou theou kai dothēsetai ethnei poiounti tous karpous autēs</em> — &lsquo;therefore I tell you, the kingdom of God will be taken from you and given to a people producing its fruits.&rsquo; The movement from the unified Solomonic kingdom to the divided kingdoms to the exile and to the reconstitution in Christ follows this pattern of judicial removal and new-covenant gift. The kingdom torn from Solomon&rsquo;s dynasty is ultimately reconstituted in David&rsquo;s greater Son — not as a territorial-political entity but as the kingdom of God present among a people defined by covenant faithfulness (Luke 17:21).</p>",
    "28": "<p>Jeroboam&rsquo;s golden calves at Bethel and Dan — <em>hinnēh ʾelōheyḵā yiśrāʾēl ʾăšer heʿelûḵā mēʾereṣ miṣrāyim</em>, &lsquo;behold your gods, O Israel, who brought you up out of the land of Egypt&rsquo; — is a direct citation of Aaron&rsquo;s golden calf proclamation at Sinai (Exod 32:4, 8: <em>ʾēlleh ʾelōheyḵā yiśrāʾēl ʾăšer heʿelûḵā mēʾereṣ miṣrāyim</em>). The identical wording marks Jeroboam&rsquo;s cult as a deliberate re-enactment of the foundational apostasy — and signals to the Deuteronomistic narrator that the northern kingdom was inaugurated on the same idolatrous principle that nearly destroyed Israel at Sinai. Paul in 1 Cor 10:7 cites the Sinai calf episode directly as the paradigm of idolatrous eating: <em>mēde eidōlolatrai ginesthe, kathōs tines autōn kathōs gegraptai, &ldquo;ekathisen ho laos phagein kai pein kai anestēsan paizein&rdquo;</em> — and applies it as a warning to the Corinthians about participation in idol feasts. Rom 1:23 (&lsquo;they exchanged the glory of the immortal God for images resembling mortal man and birds and animals and creeping things&rsquo;) describes the universal idolatrous exchange that Jeroboam&rsquo;s calves enact at the national level. Christ is the resolution to the calf-pattern: he is the true image of the invisible God (Col 1:15), the one in whom the &lsquo;glory of God&rsquo; (2 Cor 4:6) that Israel exchanged for images is finally and rightly seen and worshipped.</p>"
  },
  "13": {
    "2": "<p>The unnamed man of God from Judah pronounces a sign against Jeroboam&rsquo;s altar at Bethel by naming the agent of its future destruction: <em>hinnēh ḇēn nôlāḏ lᵉḇêt dāwîḏ yōšiyyāhû šᵉmô</em>, &lsquo;behold, a son shall be born to the house of David, Josiah by name, and he shall sacrifice on you the priests of the high places who make offerings on you.&rsquo; The prophecy is fulfilled in precise verbal echo three centuries later in 2 Kgs 23:15-16: Josiah defiles the altar at Bethel, burns bones on it, and &lsquo;this was the word of YHWH that the man of God had proclaimed.&rsquo; The specificity of the named prophecy — naming the individual who will fulfill it, 300 years before his birth — is the OT&rsquo;s sharpest example of predictive precision in a non-messianic context, and establishes the pattern of fulfilled-by-name prophecy. Acts 4:28 applies the same pattern to the crucifixion: the rulers and crowds acted &lsquo;to do whatever your hand and your plan had predestined to take place.&rsquo; The named-agent prophecy of 1 Kgs 13:2 is the OT&rsquo;s structural precedent for understanding how historical agents fulfill divinely predetermined events — a framework Peter and Paul apply directly to the passion narrative as its fulfillment.</p>"
  },
  "14": {
    "8": "<p>Ahijah&rsquo;s oracle to Jeroboam contrasts him with David: YHWH gave the kingdom to Jeroboam but Jeroboam did not keep YHWH&rsquo;s commands — <em>wᵉlōʾ hāyîtā kᵉʿaḇdî dāwîḏ ʾăšer šāmar miṣwōtay wᵉʾăšer hālak ʾaḥăray bᵉkol lᵉḇāḇô</em>, &lsquo;you have not been like my servant David who kept my commandments and followed me with all his heart.&rsquo; David as the <em>covenant baseline</em> is the Deuteronomistic standard against which every king is measured — and every king falls short, except Hezekiah and Josiah. The &lsquo;whole heart&rsquo; (<em>kol lēḇāḇ</em>) criterion that David alone met in the narrative becomes in the NT the criterion that only one person has ever fully satisfied. Heb 3:2 applies this to Jesus: <em>piston onta tō poiēsanti auton</em>, &lsquo;faithful to him who appointed him&rsquo; — and the comparison is explicitly with Moses (not David), but the principle is identical: the one who was faithful with his whole heart in YHWH&rsquo;s house. Jesus&rsquo;s own declaration — <em>ho poiōn ta thelēmata tou patros mou</em> (John 6:38, &lsquo;I have come down from heaven, not to do my own will but the will of him who sent me&rsquo;) — is the definitive &lsquo;whole heart&rsquo; that Jeroboam, David, and every king typologically reached toward and fell short of. Christ is the king who actually fulfills the David-standard.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1kings mkt-christ: wrote {count} verses across ch 12-14')

if __name__ == '__main__':
    main()
