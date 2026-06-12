"""
MKT Original Commentary — 1 Kings chapters 18–19
Run: python3 scripts/zc-original-1kings-18-19.py

Ch18: sᵉʿippîm — 'limp between two opinions'; the double-minded pāsaḥ;
      theophanic fire consuming the Carmel sacrifice — acceptance pattern
Ch19: wayyišʾal ʾet napšô lāmût — asking his soul to die; broom-tree exhaustion;
      šiḇʿat ʾălāpîm — seven thousand; the hidden remnant / Rom 11:4-5

Key Hebrew terms:
- sᵉʿippîm (18:21): forks/branches — the two-forked tree; the double mind
- pāsaḥ (18:21): to limp/leap — same root as Passover (pesaḥ)
- wayyišʾal ʾet napšô lāmût (19:4): asked his soul to die — prophetic exhaustion
- šiḇʿat ʾălāpîm (19:18): seven thousand — the hidden elect remnant
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
  "18": {
    "21": "<p>Elijah&rsquo;s challenge to the assembled Israel — <em>ʿad mātay ʾattem pōsᵉḥîm ʿal šᵉtê hassᵉʿippîm</em>, &lsquo;how long will you limp between two opinions (<em>sᵉʿippîm</em>)?&rsquo; — uses the precise vocabulary of structural division. The noun <em>sᵉʿippîm</em> is from <em>sāʿap</em> (to divide, fork) and means the branching forks of a tree: the image is of a person whose weight is distributed between two diverging branches, unable to commit to either. The verb <em>pāsaḥ</em> (to limp, to leap) is from the same root as <em>pesaḥ</em> (Passover): the verb means both to skip/leap and to limp — the double-forked stance produces an unstable gait. Ps 119:113 uses the cognate: <em>sᵉʿăpîm śānēʾtî</em> — &lsquo;I hate the double-minded,&rsquo; contrasting the undivided heart of the lover of Torah with the divided heart of the uncommitted. Jas 1:8 deploys the Greek equivalent: <em>dipsychos</em> (double-souled) — &lsquo;a double-minded man is unstable in all his ways.&rsquo; Jas 4:8: &lsquo;purify your hearts, you double-minded (<em>dipsychoi</em>).&rsquo; The OT text on which James draws is Elijah&rsquo;s Carmel challenge. Matt 6:24: &lsquo;no one can serve two masters,&rsquo; and Rev 3:15-16 (&lsquo;neither hot nor cold&rsquo;) are the NT&rsquo;s applications of the same structural point: the covenant demands undivided loyalty, and division between YHWH and any other absolute is the fundamental form of unfaithfulness.</p>",
    "38": "<p>The divine fire on Carmel — <em>wayyippōl ʾēš YHWH wattōʾkal ʾet hāʿōlāh wᵉʾet hāʿēṣîm wᵉʾet hāʾăḇānîm wᵉʾet hāʿāpār wᵉʾet hammayim ʾăšer bātᵉʿālāh lāḥăkāh</em>, &lsquo;the fire of YHWH fell and consumed the burnt offering and the wood and the stones and the dust and licked up the water in the trench&rsquo; — is the theophanic fire of acceptance in its most dramatic form. The pattern is consistent across the OT&rsquo;s inaugural sacrificial moments: Lev 9:24 marks the inauguration of the Levitical system (<em>wattēṣēʾ ʾēš millipᵉnê YHWH wattōʾkal ʿal hammizbēaḥ</em>, &lsquo;fire came out from before YHWH and consumed on the altar&rsquo;); 2 Chr 7:1 marks Solomon&rsquo;s temple dedication (<em>wāʾēš yārᵉḏāh min haššāmayim wattōʾkal hāʿōlāh wᵉhazzᵉḇāḥîm</em>, &lsquo;fire came down from heaven and consumed the burnt offerings and sacrifices&rsquo;). The divine fire consuming the sacrifice signals YHWH&rsquo;s acceptance and presence. Heb 12:29 carries the principle into the NT: <em>kai gar ho theos hēmōn pyr katanaliskon</em>, &lsquo;for our God is a consuming fire.&rsquo; The Carmel fire is the crisis proof of what Heb 9:26 names as the final event in the same sequence: Christ &lsquo;put away sin by the sacrifice of himself&rsquo; — the one, final, all-consuming sacrifice that makes all subsequent altar-fire unnecessary because it exhausted what the consuming fire always demanded.</p>"
  },
  "19": {
    "4": "<p>Elijah&rsquo;s collapse under the broom tree (<em>ʾetem</em>, Retama raetam, the white-flowering desert shrub that provides shade in the Negev) — <em>wayyišʾal ʾet napšô lāmût</em>, &lsquo;he asked for his soul/life (<em>napšô</em>) to die&rsquo; — is the OT&rsquo;s most direct account of prophetic burnout: the total exhaustion that follows crisis-action, the desire for death at the moment of apparent victory. The <em>napšô</em> (his life, his self, his appetite for existence) is what he asks to die — a request for total cessation. YHWH&rsquo;s response is not rebuke, not a prophetic commission, not a theological correction — it is provision: the angel touches him twice (<em>wayyigʿō bô</em>) and says <em>qûm ʾᵉḵôl</em>, &lsquo;arise and eat.&rsquo; The angel bakes a cake on hot coals and brings a jar of water. Physical sustenance precedes any word of recommission or reorientation (which comes only after Horeb, vv14-18). The pattern of gracious provision before recommissioning appears in John 21:9-12, where the risen Jesus has a charcoal fire (<em>anthrakia</em>) with fish and bread ready for the failed and discouraged disciples before any word of commission is spoken. The <em>qûm ʾᵉḵôl</em> at the broom tree is the OT form of the pastoral principle: the servant is fed and strengthened before he is sent; the shepherd provides for the exhausted before demanding further service.</p>",
    "18": "<p>YHWH&rsquo;s corrective to Elijah&rsquo;s complaint of total isolation — <em>wᵉhišʾartî bᵉyiśrāʾēl šiḇʿat ʾălāpîm kol habbirkayim ʾăšer lōʾ kārᵉʿû labbāʿal</em>, &lsquo;I have reserved for myself in Israel seven thousand, all the knees that have not bowed to Baal&rsquo; — introduces the <em>šᵉʾār</em> (remnant) as a theological category. The verb <em>hišʾartî</em> (hiph&rsquo;il of <em>šāʾar</em>, &lsquo;I have left/reserved&rsquo;) is the technical term for the remnant&rsquo;s existence: YHWH himself has preserved them, not their own resilience or visibility. The number seven thousand is symbolic (seven = completeness; thousands = covenant-fullness), not a census figure. The seven thousand are hidden from Elijah&rsquo;s perception but known to YHWH — their existence is a matter of divine knowledge and divine preservation, not human observation. Paul in Rom 11:4-5 quotes this verse as the OT proof for the grace-remnant of his own time: &lsquo;what is God&rsquo;s reply to him? &ldquo;I have kept for myself seven thousand men who have not bowed the knee to Baal.&rdquo; So too at the present time there is a remnant (<em>leimma</em>), chosen by grace (<em>kat&rsquo; eklogēn charitos</em>).&rsquo; The theological structure: the hiddenness of the remnant is not a sign of YHWH&rsquo;s defeat but of his sovereign preservation of what belongs to him — the same structure that underlies the elect-within-Israel argument of Rom 9-11 and the church&rsquo;s existence as a hidden remnant in every age of apparent apostasy.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1kings')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1kings', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1kings mkt-original: wrote {count} verses across ch 18-19')

if __name__ == '__main__':
    main()
