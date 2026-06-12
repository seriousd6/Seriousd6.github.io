"""
MKT Original Commentary — 2 Kings chapters 9–11
Run: python3 scripts/zc-original-2kings-9-11.py

Ch9: qannōʾ qinnēʾtî — Jehu's zeal-claim; šālôm vocabulary in judgment context
Ch10: wᵉyēhû lōʾ šāmar lāleket bᵉtôrat YHWH — zeal without Torah-fidelity
Ch11: ʿam hāʾāreṣ — the people of the land as a political actor

Key Hebrew terms:
- qannōʾ qinnēʾtî (10:16): I have been zealous / the zeal-root qnʾ
- šālôm (9:11, 17-19, 22, 31): šālôm inquiries as the ironic refrain of judgment
- ʿam hāʾāreṣ (11:14, 18-20): the people of the land — political force in the restoration
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
  "9": {
    "22": "<p>When Joram asks Jehu <em>hašālôm yēhûʾ</em> (&lsquo;is it šālôm, Jehu?&rsquo;), Jehu&rsquo;s response — <em>mah haššālôm ʿaḏ zᵉnûnê ʾîzeḇel ʾimmᵉḵā</em>, &lsquo;what šālôm (peace) can there be, so long as the harlotries of your mother Jezebel and her sorceries are so many?&rsquo; — is the chapter&rsquo;s fourth use of the <em>šālôm</em>-inquiry pattern (vv11, 17, 18, 19, 22). The repeated <em>šālôm</em> questions structure the chapter as a sequence of false-peace inquiries: the watchman asks, the king asks, the messengers ask — all using the covenant-greeting word — and in each case Jehu&rsquo;s response is either a deflection or (here) an explicit denial. The ironic deployment of <em>šālôm</em> throughout the judgment narrative is prophetic rhetoric: the covenant-peace word (<em>šālôm</em> = wholeness, covenant-wellbeing) is exposed as an impossible category for the Ahab dynasty. Jer 6:14 and 8:11 make explicit what the Jehu narrative implies: &lsquo;they have healed the wound of my people lightly, saying, &ldquo;Peace, peace,&rdquo; when there is no peace.&rsquo; The false šālôm of the court prophets and the ironic šālôm-inquiries of 2 Kgs 9 are structurally identical: a peace-word used where YHWH has declared judgment. John 14:27 names the true šālôm&rsquo;s source: &lsquo;peace I leave with you; my peace I give to you. Not as the world gives do I give to you.&rsquo; The šālôm the world cannot give (and the Ahab dynasty does not have) is the eschatological gift of the risen Christ.</p>"
  },
  "10": {
    "16": "<p>Jehu&rsquo;s invitation to Jehonadab — <em>lᵉḵā ʾittî ûrᵉʾēh bᵉqinʾātî lYHWH</em>, &lsquo;come with me and see my zeal for YHWH&rsquo; — uses the root <em>qnʾ</em> (to be zealous, to be jealous; noun <em>qinʾāh</em>: zeal, jealousy) that runs throughout the OT&rsquo;s most intense covenant-fidelity language. Phinehas in Num 25:11 is credited with <em>qinʾātî bᵉtôḵām</em> (&lsquo;being zealous with my jealousy among them&rsquo;) — turning aside YHWH&rsquo;s wrath by a violent act of covenant enforcement; Elijah&rsquo;s self-description in 1 Kgs 19:10, 14 (&lsquo;<em>qannōʾ qinnēʾtî lYHWH</em>&rsquo;) uses the same intensive infinitive absolute. The Deuteronomistic verdict on Jehu (v29, v31) acknowledges his zeal while noting its incompleteness: he eliminated the Baal worship but &lsquo;did not turn aside from the sins of Jeroboam.&rsquo; Zeal for YHWH against Baal coexisted with continuation of calf-worship. Paul in Gal 1:14 uses <em>zēlōtēs</em> (zealot) for his pre-conversion persecution of the church: &lsquo;I was advancing in Judaism beyond many of my own age, being extremely zealous for the traditions of my fathers.&rsquo; Phil 3:6 lists &lsquo;as to zeal, a persecutor of the church.&rsquo; The Jehu pattern — genuine zeal for YHWH that nonetheless missed the full covenant requirement — is the OT structure that Paul&rsquo;s conversion exposes in retrospect: <em>zēlos theou</em> (zeal for God) without <em>epignōsis</em> (knowledge/recognition of Christ) is the Romans 10:2 diagnosis of Israel&rsquo;s situation.</p>"
  },
  "11": {
    "14": "<p>The <em>ʿam hāʾāreṣ</em> (people of the land) who stand at the coronation of the young Joash — <em>wᵉhinnēh hammelek ʿōmēḏ ʿal hāʿammûḏ kammišpāṭ wᵉhaśśārîm wᵉhaḥăṣōṣᵉrôt ʿal hammelek wᵉkol ʿam hāʾāreṣ śāmēaḥ wᵉtōqēaʿ baḥăṣōṣᵉrôt</em> — are the political force that restores the Davidic dynasty after Athaliah&rsquo;s six-year usurpation. The <em>ʿam hāʾāreṣ</em> in Kings is not a sociological term for the rural poor (a post-exilic usage) but a constitutional term for the full covenant community of Judah acting as a political collective: they enthrone kings (2 Kgs 21:24; 23:30), execute traitors (11:20), and serve as the legitimate political expression of the covenant people distinct from the court and the military. The term anticipates what the NT calls <em>laos</em> (people of God): the assembled covenant community whose acclamation and participation constitutes the legitimate acknowledgment of the covenant king. The coronation scene — the hidden king revealed, the usurper slain, the people rejoicing at the restoration of the legitimate son of David — is the structural type of the resurrection-enthronement narrative: the Son of David hidden (in the tomb), the usurper&rsquo;s power broken, the <em>laos</em> of the new covenant acclaiming the risen king (Acts 2:36: <em>asphaleōs oun ginōsketō pas oikos Israēl hoti kai kyrion kai Christon auton ho theos epoiēsen</em>).</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2kings')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2kings', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2kings mkt-original: wrote {count} verses across ch 9-11')

if __name__ == '__main__':
    main()
