"""
MKT Christ Commentary — 1 Kings chapters 20–21
Run: python3 scripts/zc-christ-1kings-20-21.py

Ch20: Ahab's condemned mercy toward Ben-hadad — the king who released the man YHWH devoted;
      the disguised prophet condemning by parable — Nathan/David echo / 2 Sam 12
Ch21: Naboth's vineyard — judicial murder for inheritance;
      Jezebel's false-witness execution type / Matt 26:59-61;
      Elijah's Ahab-death oracle — the blood-field judgment / Acts 1:18-20

Key typological connections:
- 20:42: Ahab releases the man YHWH devoted → Barabbas-release (the condemned released, the
         innocent condemned) / Matt 27:15-26 as anti-type
- 21:13: false witnesses condemn Naboth → Matt 26:60-61 (false witnesses at Jesus's trial)
- 21:19: blood in Naboth's place → Acts 1:18-19 (Judas's blood-field); Heb 12:24
- 21:29: Ahab humbles himself / YHWH relents → Heb 4:16; the principle of responsive mercy
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
  "20": {
    "42": "<p>The prophet&rsquo;s oracle to Ahab after his release of Ben-hadad — <em>yaʿan šillaḥtā ʾet ʾîš ḥermî miyyāḏ wᵉhāyᵉtāh napšᵉḵā taḥat napšô</em>, &lsquo;because you have let go out of your hand the man whom I had devoted to destruction, therefore your life shall be for his life&rsquo; — establishes the principle of substitutionary exchange in a context of judicial failure: the man who should die is released; the one who released him bears the death penalty. The typological shadow of Barabbas is pronounced: Pilate releases a man whom (in Pilate&rsquo;s own judgment) deserved punishment, while the innocent one is condemned. Matt 27:20-26 narrates the anti-typological exchange: the crowd chooses Barabbas (&lsquo;let go the man of violence&rsquo;) and condemns Jesus (&lsquo;let him be crucified&rsquo;). Ahab condemned himself by releasing the condemned man; Pilate condemns himself by the same act — &lsquo;I am innocent of this man&rsquo;s blood&rsquo; (Matt 27:24) is the ironic echo of Ahab&rsquo;s condemned mercy. The inversion is total in Christ: in the passion, the released man is genuinely guilty and the condemned man is genuinely innocent; the substitutionary exchange that Ahab botched is here accomplished exactly and finally — the guilty released, the innocent condemned, life given for life.</p>"
  },
  "21": {
    "13": "<p>Naboth&rsquo;s execution through false witnesses — <em>wayyāšîḇû šᵉnê hāʾănāšîm bᵉnê ḇᵉliyyaʿal wayyēšᵉḇû negeḏô wayyᵉʿiḏūhû... wayyōṣîʾūhû miḥûṣ lāʿîr wayyisqᵉlūhû bāʾăḇānîm wayyāmōṯ</em>, &lsquo;two worthless men accused him before the people... they took him outside the city and stoned him to death&rsquo; — follows the formal pattern of the two-witness requirement (Deut 17:6) deployed to execute an innocent man. The false-witness pattern is the structural model for Jesus&rsquo;s trial: Matt 26:59-61 records that &lsquo;the chief priests and the whole council were seeking false testimony against Jesus... Finally two came forward and said, &ldquo;This man said, &lsquo;I am able to destroy the temple of God and to rebuild it in three days.&rsquo;&rdquo;&rsquo; The formal structure is identical: two witnesses (satisfying the legal minimum), a false accusation, a death sentence on an innocent man, execution &lsquo;outside the city&rsquo; (Heb 13:12: &lsquo;Jesus also suffered outside the gate&rsquo; — as Naboth died outside the city). Naboth refuses to curse God and the king (v13: the accusation is that he blessed, i.e., cursed, them) and dies innocent; Jesus is accused on a twisted version of a true word and dies innocent. The judicial murder of the vineyard-owner&rsquo;s innocent heir is the parable Jesus himself tells in Matt 21:33-41 — the tenants kill the son, the owner comes and destroys them.</p>",
    "19": "<p>Elijah&rsquo;s oracle over Naboth&rsquo;s vineyard — <em>ḵōh ʾāmar YHWH bimqôm ʾăšer lāqᵉqû hakkᵉlāḇîm ʾet dam nāḇôt yālōqᵉqû hakkᵉlāḇîm ʾet dāmᵉḵā gam ʾāttāh</em>, &lsquo;in the place where dogs licked up the blood of Naboth shall dogs lick your own blood&rsquo; — introduces the blood-field principle: the place of innocent blood becomes the place of the murderer&rsquo;s blood. Acts 1:18-19 applies this to Judas: he &lsquo;bought a field with the reward of his wickedness, and falling headlong he burst open in the middle and all his bowels gushed out... so that field was called in their own language Akeldama, that is, Field of Blood.&rsquo; The blood-field principle — the place of treachery becomes the monument of the traitor&rsquo;s end — traces from Naboth&rsquo;s vineyard through the Achan narrative (Josh 7) to Judas&rsquo;s field. Heb 12:24 resolves the blood-oracle in Christ: the blood that Jesus shed &lsquo;speaks a better word than the blood of Abel&rsquo; — Abel&rsquo;s blood cried for vengeance (Gen 4:10); Naboth&rsquo;s blood triggered the blood-field curse; Christ&rsquo;s blood speaks mercy and redemption. The blood-place that was Naboth&rsquo;s field and Judas&rsquo;s field is answered by the blood-place that is Golgotha — where the innocent&rsquo;s blood, rather than cursing, forgives.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1kings mkt-christ: wrote {count} verses across ch 20-21')

if __name__ == '__main__':
    main()
