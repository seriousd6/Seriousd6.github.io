"""
MKT Original Commentary — Isaiah chapter 56
Run: python3 scripts/zc-original-isaiah-56.py

Isaiah 56 opens "Third Isaiah" (chs 56-66) with a radical inclusion oracle:
foreigners and eunuchs who keep covenant are fully included in YHWH's community.
The chapter pivots from the Servant Songs (chs 40-55) to the application of their
implications for the shape of the restored community.

Key translation decisions:
- 56:3 sārîs: "eunuch" — not "official" (as sometimes softened); the text addresses
  the specific group excluded in Deut 23:1 and promises them restoration.
- 56:5 yāḏ wāšēm: "hand and a name" — a hendiadys for memorial and legacy; the
  combination is a permanent monument greater than biological lineage.
- 56:7 bêt tĕpillâ lĕkol-hāʿammîm: "a house of prayer for all peoples" — Jesus
  quotes this phrase in the temple cleansing (Mark 11:17; Matt 21:13; Luke 19:46),
  making the eschatological fulfillment the criterion by which the temple's corruption
  is judged.
- 56:10 ṣōpāyw ʿiwwĕrîm: "his watchmen are blind" — the watchman/shepherd figure
  who fails becomes a foil for the Good Shepherd of Isaiah 40:11 and John 10.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    """Merge new_data into existing without overwriting present entries."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ISAIAH = {
  "56": {
    "1": '<p><strong>šimrû mišpāṭ waʿăśû ṣĕdāqâ</strong> — "keep justice and do righteousness" — the ethical imperative that opens the chapter and frames the entire inclusion oracle: the welcome of foreigners and eunuchs is grounded in covenant obedience, not merely theological sentiment. <strong>kî qĕrôbâ yĕšûʿātî lābôʾ wĕṣidqātî lĕhiggālôt</strong> — "for my salvation (<em>yĕšûʿâ</em>) is near to come, and my righteousness (<em>ṣĕdāqâ</em>) to be revealed" — the eschatological imminence is the motivation for present ethical action. The pairing of <em>yĕšûʿâ</em> (salvation) and <em>ṣĕdāqâ</em> (righteousness) — both expressing YHWH\'s character and act — is characteristic of Isaiah\'s theology of the coming restoration.</p>',
    "2": '<p><strong>ʾašrê ʾĕnôš yaʿăśeh zōʾt</strong> — "blessed is the man who does this" — the beatitude structure (cf. Ps 1:1; 41:1; Matt 5:3-11) grounds the blessing in action, not status. <strong>ûben-ʾādām yĕḥăzeq bāh</strong> — "and the son of man who holds fast to it" (<em>ḥāzaq</em>, to be strong, to grasp firmly). <strong>šōmēr šabbāt mēḥallĕlô wĕšōmēr yādô mēʿăśôt kol-rāʿ</strong> — "keeping the Sabbath without profaning it, and keeping his hand from doing any evil" — the Sabbath-keeping (<em>šāmar šabbāt</em>) is the specific marker of covenant participation for the expanded community of vv.3-8. The Sabbath is the weekly enacted covenant sign.</p>',
    "3": '<p><strong>wĕʾal-yōʾmar ben-hannēkār hannilweh ʾel-Yhwh lēʾmōr habdēl yabdîlēnî Yhwh mēʿal ʿammô</strong> — "let not the foreigner (<em>ben-hannēkār</em>, son of the foreign land) who has joined himself to YHWH say, \'YHWH will surely separate me from his people.\'" The fear being addressed is the legal exclusion of Deut 23:3-8 (Ammonites, Moabites, and others excluded from the assembly). <strong>wĕʾal-yōʾmar hassārîs hēn ʾănî ʿēṣ yābēš</strong> — "and let not the eunuch say, \'Behold, I am a dry tree.\'" The eunuch (<em>sārîs</em>, H5631) is excluded by Deut 23:1; the "dry tree" metaphor expresses his condition of having no descendants and therefore no memorial.</p>',
    "4": '<p><strong>kî-kōh ʾāmar Yhwh lassārîsîm ʾăšer yišmĕrû ʾet-šabbĕtôtay</strong> — "for thus says YHWH to the eunuchs who keep my Sabbaths" — the response to the eunuch\'s fear is direct divine address. <strong>ûbāḥărû baʾăšer ḥāpāṣtî ûmaḥăzîqîm bibĕrîtî</strong> — "who choose what pleases me and hold fast my covenant" — the three criteria (Sabbath-keeping, choosing what pleases YHWH, holding fast the covenant) define the community membership in terms of character and allegiance rather than birth status. The inclusion is based on obedience, not on reversing the physical condition.</p>',
    "5": '<p><strong>wĕnātattî lāhem bĕbêtî ûbĕḥômōtay yāḏ wāšēm</strong> — "I will give them in my house and within my walls a monument and a name (<em>yāḏ wāšēm</em>)" — <em>yāḏ</em> (hand/memorial stele) and <em>šēm</em> (name) together form the idea of a permanent public monument — more enduring than biological descendants. <strong>ṭôḇ mibbānîm ûmibbānôt</strong> — "better than sons and daughters" — the reversal is complete: what the eunuch lacked (children as memorial) is exceeded by what YHWH gives. <strong>šēm ʿôlām ʾettēn-lô ʾăšer lōʾ yikkārēt</strong> — "an everlasting name I will give him that shall not be cut off" — the permanent name (<em>šēm ʿôlām</em>) is the ultimate reversal of the eunuch\'s fear of namelessness.</p>',
    "6": '<p><strong>ûbĕnê hannēkār hannilwîm ʿal-Yhwh lĕšārĕtô</strong> — "and the foreigners who join themselves to YHWH, to serve him" — <em>lāwâ</em> (to join oneself to, to attach to) is the same root as "Levi" — the joining of foreigners to YHWH mirrors the tribal name that meant "attached." <strong>ûlĕʾahăbâ ʾet-šēm Yhwh lihyôt lô laʿăḇādîm</strong> — "to love the name of YHWH, and to be his servants." <strong>kol-šōmēr šabbāt mēḥallĕlô ûmaḥăzîqîm bibĕrîtî</strong> — "everyone who keeps the Sabbath without profaning it and holds fast my covenant" — the Sabbath is again the covenant marker for this extended community.</p>',
    "7": '<p><strong>wahăḇîʾôtîm ʾel-har qoḏšî wĕśimmahttîm bĕbêt tĕpillātî</strong> — "I will bring them to my holy mountain and make them joyful in my house of prayer" — the phrase <em>bêt tĕpillātî</em> (my house of prayer) is the crux. <strong>ʿôlōtêhem wĕzibḥêhem lĕrāṣôn ʿal-mizbĕḥî</strong> — "their burnt offerings and sacrifices will be accepted on my altar." <strong>kî bêtî bêt-tĕpillâ yiqqārēʾ lĕkol-hāʿammîm</strong> — "for my house shall be called a house of prayer for all peoples (<em>kol-hāʿammîm</em>)" — the universalist climax. Jesus quotes this phrase in Mark 11:17; Matt 21:13; Luke 19:46 when cleansing the temple, indicting the traders who have turned the house of all-peoples prayer into a commercial operation, and specifically a den of robbers (<em>mĕʿarat pārīṣîm</em>) drawn from Jer 7:11.</p>',
    "8": '<p><strong>nĕʾum ʾădōnāy Yhwh mĕqabbēṣ nidḥê yiśrāʾēl</strong> — "oracle of the Lord YHWH, who gathers the outcasts (<em>nidḥê</em>, scattered/banished ones) of Israel" — the ingathering is already underway for Israel. <strong>ʿôd ʾăqabbēṣ ʿālāyw lĕniqbāṣāyw</strong> — "I will gather still more to him besides those already gathered" — the gathering extends beyond Israel to the foreigners and eunuchs of vv.3-7. The word <em>ʿôd</em> (still/again) signals that the community expansion is not finished; YHWH will continue adding to his people.</p>',
    "9": '<p><strong>kol-ḥayyat haśśādeh ʾĕtāyû lĕʾākōl kol-ḥayyat bayyāʿar</strong> — "all you beasts of the field, come to eat; all you beasts in the forest." The sudden shift from the inclusion oracle (vv.1-8) to a summons to wild animals is jarring. The animals are summoned to consume something — what? The context (vv.10-12) identifies the corrupt leaders as the target: the watchmen who fail, the shepherds who only think about their own appetite, are abandoned to become the prey of wild beasts.</p>',
    "10": '<p><strong>ṣōpāyw ʿiwwĕrîm kullām</strong> — "his watchmen (<em>ṣōpeh</em>, H6822, lookout/sentinel) are all blind" — the failure of Israel\'s spiritual leadership. <strong>lōʾ yāḏĕʿû kullām</strong> — "they have no knowledge at all." <strong>kullām kĕlāḇîm ʾillĕmîm lōʾ yûklû linbōaḥ</strong> — "they are all dumb dogs that cannot bark" — the watchdog who cannot bark is the most specific failure: the guard animal\'s one function is warning, and it fails to give warning. The blind watchman and the silent watchdog are images of pastoral and prophetic failure. <strong>hōzîm šōkĕḇîm ʾōhăḇê lānûm</strong> — "dreaming, lying down, loving to slumber."</p>',
    "11": '<p><strong>wĕhakkĕlāḇîm ʿazzê-nepeš lōʾ yāḏĕʿû śobʿâ</strong> — "the dogs have a mighty appetite (<em>ʿazzê-nepeš</em>, strong of soul/appetite) and are never satisfied" — the insatiable desire is the defining character of the failed leadership. <strong>wĕhēmmâ rōʿîm lōʾ yāḏĕʿû hāḇîn</strong> — "and they are shepherds who have no understanding." The word <em>rōʿeh</em> (shepherd, leader/pastor) connects to the Good Shepherd imagery of 40:11: the shepherd who gathers lambs contrasted with these shepherds who think only of their own appetite. <strong>kullām lĕdarkām pānû ʾîš lĕbiṣʿô miqṣēhû</strong> — "they have all turned to their own way, each one to his own gain (<em>beṣāʿ</em>, unjust gain, plunder)."</p>',
    "12": '<p><strong>lĕkû ʾeqqĕḥâ-yāyin wĕnisĕbĕʾâ šēkār</strong> — "Come, let me get wine and let us drink strong drink" — the self-invitation of the corrupt leaders to continued indulgence. <strong>wĕhāyâ kāzeh māḥār yôm gādôl yōtēr mĕʾōd</strong> — "and tomorrow will be like this day, even much more so" — the presumptuous confidence in continuation (cf. Luke 12:19-20\'s rich fool: "Soul, you have ample goods laid up for many years"). The chapter ends with this damning characterization of Israel\'s leadership: blind watchmen, insatiable dogs, presumptuous drinkers — the antithesis of the obedient, covenant-keeping foreigners and eunuchs of vv.1-8 who receive YHWH\'s welcome.</p>',
  },
}

def main():
    existing = load_comm('mkt-original', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-original', 'isaiah', existing)
    # INTENT: Verify all 12 Isaiah 56 mkt-original verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 56 changes, update expected total
    # VERIFY: Console shows OK with 12 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-original' / 'isaiah.json').read_text())
    missing = [v for v in il.get('56', {}) if v not in out.get('56', {})]
    if missing:
        print(f'  MISSING: {missing}')
    else:
        print(f'  OK: all Isaiah 56 mkt-original verses present ({len(il.get("56", {}))} verses)')

if __name__ == '__main__':
    main()
