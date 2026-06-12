"""
MKT Christ Commentary — 2 Kings chapters 18–20
Run: python3 scripts/zc-christ-2kings-18-20.py

Ch18: Hezekiah's trust superlative — the best Davidic king until / Heb 3:2; Matt 12:42
Ch19: Hezekiah spreads letter before YHWH / prayer of cosmic sovereignty / John 17
Ch20: Third-day temple ascent after mortal illness / 1 Cor 15:4; Hos 6:2

Key typological connections:
- 18:5: Hezekiah trust superlative → Heb 3:2-6; Matt 12:42 (greater than Solomon)
- 19:15: prayer — you alone are YHWH / Lord of all kingdoms → John 17:1-3; Matt 26:39
- 20:5: on the third day go up to the house of YHWH → 1 Cor 15:4; Hos 6:2
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
  "18": {
    "5": "<p>The narrator&rsquo;s superlative for Hezekiah — <em>bāṭaḥ bē YHWH ʾelōhê yiśrāʾēl wᵉʾaḥărāyw lōʾ hāyāh kāmōhû bᵉḵōl malkê yᵉhûḏāh wᵉʾăšer hāyû lᵉpānāyw</em>, &lsquo;he trusted in YHWH the God of Israel, and after him there was none like him among all the kings of Judah, nor among those who were before him&rsquo; — is the OT&rsquo;s highest commendation given to any Davidic king. The superlative runs in both directions: no king before him (not even David, to whom the qualifier about Bathsheba always attaches) and no king after him. Yet Hezekiah&rsquo;s faithfulness, however superlative within the Davidic line, is still bounded: he is faithful while Sennacherib threatens, then shows Babylon his treasures and receives Isaiah&rsquo;s judgment (20:12-18); he dies and is succeeded by Manasseh, the worst of all kings. The superlative that the narrator applies to Hezekiah within the Davidic sequence points beyond itself to the one of whom it could be said without qualification. Heb 3:2-6 establishes Jesus as &lsquo;faithful to him who appointed him&rsquo; — <em>pistos tō poiēsanti auton</em> — and then distinguishes Moses (faithful as a servant in God&rsquo;s house) from Christ (faithful as a Son over God&rsquo;s house). Hezekiah represents the OT&rsquo;s best achievement within the servant-king category; Jesus is the Son who fulfills the category itself. Matt 12:42 (&lsquo;something greater than Solomon is here&rsquo;) generalizes the principle: the wisdom and faithfulness the Davidic kings partially embodied is present in its fullness in Jesus.</p>"
  },
  "19": {
    "15": "<p>Hezekiah&rsquo;s prayer — opening with <em>YHWH ʾelōhê yiśrāʾēl yōšēḇ hakkᵉrûḇîm ʾattāh hûʾ hāʾelōhîm lᵉḇaḏḏᵉḵā lᵉḵōl mamléḵôt hāʾāreṣ ʾattāh ʿāśîtā ʾet haššāmayim wᵉʾet hāʾāreṣ</em>, &lsquo;O YHWH, God of Israel, who is enthroned above the cherubim, you are the God, you alone, of all the kingdoms of the earth; you have made heaven and earth&rsquo; — is the OT&rsquo;s fullest royal prayer of cosmic sovereignty, addressed from within the sanctuary to the one whose throne exceeds the sanctuary. The prayer moves from sovereignty (v15) to the specific crisis (v16-18) to petition grounded in YHWH&rsquo;s reputation among the nations (v19: &lsquo;so that all the kingdoms of the earth may know that you alone are YHWH&rsquo;). The structure of the prayer — addressing the Father as the one with authority over all things, presenting the specific need, asking for deliverance with a universal purpose — is the template of Jesus&rsquo;s high-priestly prayer in John 17: <em>Pater, elēlythen hē hōra; doxason sou ton hyion, hina ho hyios doxasē se, kathōs edōkas autō exousian pasēs sarkos</em> — &lsquo;Father, the hour has come; glorify your Son that the Son may glorify you, since you have given him authority over all flesh&rsquo; (17:1-2). Hezekiah prays that the nations may know YHWH; Jesus prays that the world may know that the Father sent him (John 17:21, 23). Hezekiah spreads Sennacherib&rsquo;s letter before YHWH (v14) — the literal enactment of bringing the enemy&rsquo;s threat into the sanctuary — as Jesus in Gethsemane (Matt 26:39) brings the cup of judgment before the Father: &lsquo;not as I will, but as you will.&rsquo; The king&rsquo;s prayer that YHWH act for the sake of his name in all the earth finds its fulfillment in the Son whose name is above every name (Phil 2:9-10).</p>"
  },
  "20": {
    "5": "<p>The sign given to Hezekiah after YHWH grants him fifteen additional years — <em>ûḇayyôm haššᵉlîšî taʿăleh bêt YHWH</em>, &lsquo;and on the third day you shall go up to the house of YHWH&rsquo; — embeds within it the third-day pattern that Paul identifies in 1 Cor 15:4 as the scriptural framework for Christ&rsquo;s resurrection: <em>kai hoti ēgerthē tē hēmera tē tritē kata tas graphas</em> — &lsquo;and that he was raised on the third day in accordance with the Scriptures.&rsquo; The &lsquo;Scriptures&rsquo; Paul cites do not name a single text; they describe a pattern present across multiple OT narratives. Hezekiah&rsquo;s recovery from mortal illness and his third-day ascent to the house of YHWH is one of the OT&rsquo;s clearest instances of this pattern: a man under sentence of death (v1: &lsquo;you shall die; you shall not recover&rsquo;), granted life by divine reversal, vindicated publicly on the third day in the sanctuary. Hos 6:2 names the same structure: <em>yᵉḥayyēnû miyyōmāyim bayyôm haššᵉlîšî yᵉqîmēnû wᵉniḥyeh lᵉpānāyw</em> — &lsquo;after two days he will revive us; on the third day he will raise us up, that we may live before him.&rsquo; The conjunction of &lsquo;third day&rsquo; and &lsquo;before YHWH / house of YHWH&rsquo; in both Hos 6:2 and 2 Kgs 20:5 establishes the pattern: the restored life that comes after judgment is life oriented toward YHWH&rsquo;s presence. Jesus&rsquo;s resurrection on the third day and his ascent to the Father (John 20:17: &lsquo;I am ascending to my Father and your Father&rsquo;) fulfills both the death-reversal and the sanctuary-ascent that Hezekiah&rsquo;s healing anticipates.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '2kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '2kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'2kings mkt-christ: wrote {count} verses across ch 18-20')

if __name__ == '__main__':
    main()
