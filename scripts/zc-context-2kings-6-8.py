"""
MKT Context Commentary — 2 Kings chapters 6–8
Run: python3 scripts/zc-context-2kings-6-8.py

Ch6: Elisha's opened eyes — chariots of fire / ANE divine-warrior imagery;
     siege of Samaria — the extreme famine (donkey's head, dung, cannibalism) / Lev 26:29
Ch7: The four lepers at the gate — the outsider-herald of salvation pattern
Ch8: Hazael's coup predicted by Elisha — the prophet who weeps over coming judgment

ANE/historical context:
- 6:17: chariots of fire and horses — ANE divine-warrior chariot tradition
- 6:25: donkey's head for 80 shekels — siege-economics and the covenant curse
- 7:3-8: four lepers as heralds — the unexpected vector of good news
- 8:8-13: Elisha weeping over Hazael — the prophet who sees and grieves coming evil
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
  "6": {
    "17": "<p>Elisha&rsquo;s prayer that his servant&rsquo;s eyes be opened to see the mountain full of horses and chariots of fire (<em>sûsîm wᵉreḵeḇ ʾēš sāḇîḇ lᵉʾelîšāʿ</em>) deploys the ANE&rsquo;s most powerful divine-warrior imagery. The celestial chariotry motif is widespread in ancient Near Eastern divine-warrior texts: Egyptian hymns to Amun-Re depict the god riding his solar chariot across the heavens; Akkadian mythology includes divine chariots in celestial combat. In Israelite tradition the <em>reḵeḇ ʾelōhîm</em> (chariots of God) appears in Ps 68:17 (twenty thousand chariots, thousands upon thousands) and the divine-warrior tradition. Elijah&rsquo;s departure was in a chariot of fire (2 Kgs 2:11-12), and Elisha called him &lsquo;the chariots of Israel and its horsemen&rsquo; at the departure (<em>reḵeḇ yiśrāʾēl ûpārāšāyw</em>, 2 Kgs 2:12; 13:14 — the same cry used for Elisha at his death). The theological claim is precise: the true military strength of Israel is not its standing army but YHWH&rsquo;s invisible celestial forces — more numerous and more powerful than the Aramean host. The Elisha narrative provides the narrative grounding for Ps 46:11 (&lsquo;the Lord of hosts is with us; the God of Jacob is our fortress&rsquo;): what Elisha&rsquo;s servant sees in vision is the ongoing reality behind the psalm&rsquo;s confidence.</p>",
    "25": "<p>The besieged Samaria&rsquo;s famine conditions — a donkey&rsquo;s head sold for eighty shekels of silver and dove&rsquo;s dung (or possibly carob pods) for five shekels — are siege economics at their extreme. The catastrophic siege-famine is the enacted form of the covenant curse of Lev 26:29 (&lsquo;you shall eat the flesh of your sons&rsquo;) and Deut 28:53-57, both of which predict cannibalism as the extreme expression of covenant judgment under siege: &lsquo;you will eat the fruit of your womb, the flesh of your sons and daughters, whom YHWH your God has given you.&rsquo; The cannibalism reported to the king in vv26-29 (one woman eating her son in accordance with a pact with another woman who has hidden hers) is the literal fulfillment of Deut 28:53-57 and Lev 26:29. The Deuteronomic structure is the author&rsquo;s interpretive frame: the siege of Samaria is not simply military misfortune but covenant curse enacted. Lam 4:10 applies the same image to the Babylonian siege of Jerusalem: &lsquo;the hands of compassionate women have boiled their own children; they became their food during the destruction of my people.&rsquo; The besieged city eating its children is the OT&rsquo;s most extreme covenant-curse image.</p>"
  },
  "7": {
    "3": "<p>The four lepers at the city gate who discover the abandoned Aramean camp — <em>wᵉʾarbaʿāh ʾănāšîm hāyû mᵉṣōrāʿîm petaḥ haššāʿar</em>, &lsquo;now there were four men who were lepers at the entrance to the gate&rsquo; — are a paradigm of the theologically unexpected herald. Within Israelite social and ritual structure, lepers (<em>mᵉṣōrāʿîm</em>) were excluded from the community (Lev 13:46: &lsquo;he shall live alone; his dwelling shall be outside the camp&rsquo;) — stationed at the gate is the classic position of the excluded: inside the city is starvation; outside the city are the Arameans. The lepers&rsquo; logic in v4 (&lsquo;if we say, let us enter the city, the famine is in the city and we will die there; and if we sit here, we die also&rsquo;) is the logic of desperate boundary-crossing that characterizes the OT&rsquo;s outsider-herald pattern. They discover the abandoned Aramean camp, eat, take silver and gold and garments — and then recognize their obligation (v9): &lsquo;we are not doing right. This day is a day of good news (<em>yôm bᵉśôrāh hûʾ</em>).&rsquo; The precise vocabulary of Isa 52:7 (<em>mah nāwû ʿal hehārîm raglê mᵉḇaśśēr</em>) is anticipated: the lepers become the bearers of the <em>bᵉśôrāh</em> (good news) that saves the starving city — the exact social profile that Paul and the Gospels apply to the apostolic mission: the socially excluded become the heralds of salvation to those who are trapped inside.</p>"
  },
  "8": {
    "11": "<p>Elisha&rsquo;s response to Hazael&rsquo;s mission — <em>wayyaśśēm ʾet pānāyw wayyāśem ʿaḏ bōš wayyēḇḵ ʾîš hāʾelōhîm</em>, &lsquo;he fixed his gaze and stared until he was embarrassed, and the man of God wept&rsquo; — is one of the OT&rsquo;s most affecting descriptions of prophetic grief. Elisha weeps because he sees what Hazael will do to Israel (v12: set fire to fortresses, kill young men, dash children, rip open pregnant women) — judgment that the prophet has been commissioned to announce (1 Kgs 19:15: YHWH had instructed Elijah to anoint Hazael as king over Aram as the instrument of judgment). The prophet weeps over the judgment his own commission has set in motion. The combination of prophetic commission and prophetic grief is structurally parallel to Jesus&rsquo;s weeping over Jerusalem (Luke 19:41-44): Jesus announces the destruction of Jerusalem while weeping at the city — the one who announces judgment does not celebrate it. Jer 8:21-9:1 (&lsquo;for the wound of the daughter of my people is my heart wounded; I mourn, and dismay has taken hold on me. Is there no balm in Gilead?&rsquo;) is the same structure: the prophet of judgment mourning the judgment he announces.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2kings mkt-context: wrote {count} verses across ch 6-8')

if __name__ == '__main__':
    main()
