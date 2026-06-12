"""
MKT Christ Commentary — 2 Kings chapters 6–8
Run: python3 scripts/zc-christ-2kings-6-8.py

Ch6: Elisha's opened eyes — the servant sees the invisible army / 2 Cor 4:18;
     Elisha feeds captive Arameans — enemy-feeding as covenant-reversal type / Rom 12:20
Ch7: Four lepers as gospel-heralds — the outsider announcing salvation / Isa 52:7
Ch8: Hazael's evil foreknown / Elisha weeps — the prophet who grieves judgment / Luke 19:41

Key typological connections:
- 6:17: eyes opened to see heavenly army → 2 Cor 4:18; Heb 11:1 (faith = unseen reality)
- 6:22: Elisha feeds captive Aramean army → Rom 12:20 (feed your enemies; coals of fire)
- 7:9: four lepers announce the good news → Isa 52:7; Rom 10:15 (beautiful feet)
- 8:11: Elisha weeps over coming judgment → Luke 19:41-44 (Jesus weeps over Jerusalem)
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
  "6": {
    "17": "<p>Elisha&rsquo;s prayer — <em>YHWH pᵉqaḥ nāʾ ʾet ʿênāyw wᵉyirʾeh</em>, &lsquo;YHWH, please open his eyes that he may see&rsquo; — and the servant&rsquo;s vision of the mountain filled with horses and chariots of fire is the OT&rsquo;s clearest narrative demonstration of the reality of the invisible. The servant&rsquo;s natural eyes see the Aramean army; his opened eyes see YHWH&rsquo;s army. The greater reality is invisible; what appears threatening is actually surrounded by what cannot be seen. 2 Cor 4:18 names the NT principle: <em>mē skopountōn hēmōn ta blepomena alla ta mē blepomena; ta gar blepomena proskaira, ta de mē blepomena aiōnia</em> — &lsquo;we look not to the things that are seen but to the things that are unseen. For the things that are seen are transient, but the things that are unseen are eternal.&rsquo; Heb 11:1 defines faith precisely in terms of this structural dynamic: <em>estin de pistis elpizomenōn hypostasis, pragmatōn elegchos ou blepomenōn</em> — &lsquo;faith is the assurance of things hoped for, the conviction of things not seen.&rsquo; The servant&rsquo;s opened eyes are the narrative form of what faith operates in: the greater reality that surrounds the threatening visible, and that prayer accesses. The apostolic prayer-pattern of Eph 1:18 (&lsquo;having the eyes of your hearts enlightened&rsquo;) is the NT form of the same petition: open his eyes that he may see.</p>",
    "22": "<p>Elisha&rsquo;s instruction to feed the captive Aramean army rather than kill them — <em>śim lāhem leḥem ûmayim</em>, &lsquo;set bread and water before them&rsquo; — is one of the OT&rsquo;s most striking enactments of the enemy-love principle. The king of Israel asks whether to kill; Elisha says: feed. The result (v23): &lsquo;the Aramean raiders no more came into the land of Israel.&rsquo; The enemy fed becomes the peaceful neighbor. Paul in Rom 12:20 cites Prov 25:21-22: <em>ean peinaō ho echthros sou, psōmize auton; ean dipsa, potizon auton</em> — &lsquo;if your enemy is hungry, feed him; if he is thirsty, give him something to drink; for by so doing you will heap burning coals on his head.&rsquo; The Elisha-feeding narrative is the OT&rsquo;s enacted form of this principle: the enemy army given bread and water departs in peace. Jesus in Matt 5:44 (&lsquo;love your enemies and pray for those who persecute you&rsquo;) names the disposition; Elisha at Dothan provides the OT narrative illustration. The feeding of enemies at the prophet&rsquo;s table also anticipates the kingdom-table of Luke 14:12-14, where Jesus instructs precisely not to invite friends but to invite those who cannot repay — the Elisha-table becomes a type of the eschatological banquet that reverses all expected social hierarchies.</p>"
  },
  "7": {
    "9": "<p>The four lepers&rsquo; recognition of their obligation — <em>yôm bᵉśôrāh hûʾ</em>, &lsquo;this day is a day of good news&rsquo; — is the OT&rsquo;s clearest narrative application of the gospel-obligation. The lepers have news that will save the starving city; withholding it out of self-interest would be a punishable offense. The word <em>bᵉśôrāh</em> (good news, gospel) is the Hebrew root behind the LXX&rsquo;s <em>euangelion</em>. Isa 52:7 (&lsquo;how beautiful upon the mountains are the feet of him who brings good news [<em>mᵉḇaśśēr</em>], who publishes peace, who brings good news of happiness&rsquo;) applies this vocabulary to the herald of eschatological restoration; Paul in Rom 10:15 cites Isa 52:7 directly as the warrant for apostolic proclamation: <em>pōs de kēryx sōsin ean mē apostalosōsin; kathōs gegraptai, hōs hōraioi hoi podes tōn euangelizomenōn agatha</em>. The four lepers are the OT&rsquo;s unexpected heralds — socially excluded, marginally positioned, but carriers of the word that saves. The pattern recurs in the resurrection: the first heralds of the empty tomb are women (Luke 24:9-10), socially undervalued as witnesses; the apostolic proclamation begins with the socially unlikely, as did the lepers&rsquo; announcement at the city gate. The lepers&rsquo; &lsquo;this is a day of good news and we are keeping silent&rsquo; is the OT&rsquo;s starkest statement of the obligation that attaches to received grace.</p>"
  },
  "8": {
    "11": "<p>Elisha&rsquo;s weeping as he gazes at Hazael — seeing what Hazael will do to Israel — combines prophetic knowledge of coming judgment with the prophet&rsquo;s grief over it. The man of God who announces judgment is not unmoved by it; the commission to speak the word of YHWH does not insulate the prophet from the weight of what that word contains. Luke 19:41-44 narrates Jesus weeping over Jerusalem: <em>kai hōs ēggisen, idōn tēn polin eklausen ep&rsquo; autēn</em>, &lsquo;and when he drew near and saw the city, he wept over it, saying, &ldquo;Would that you, even you, had known on this day the things that make for peace!&rdquo;&rsquo; — and proceeds to announce the city&rsquo;s destruction. The weeping prophet who announces judgment is the OT type that Jesus inhabits and fulfills in its deepest form: the one who <em>is</em> the judgment of God (John 5:22: &lsquo;the Father judges no one but has given all judgment to the Son&rsquo;) is also the one who weeps over the judgment falling on those who reject it. Elisha weeps because he foresees what Hazael will do; Jesus weeps because he foresees what Rome will do — and in both cases the weeping is the prophet&rsquo;s authentic grief, not performance. Jer 8:21-9:1 (&lsquo;for the wound of the daughter of my people is my heart wounded; is there no balm in Gilead?&rsquo;) is the same prophetic structure, connecting Elisha, Jeremiah, and Jesus in a single pattern of judgment-announcing grief.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '2kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '2kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'2kings mkt-christ: wrote {count} verses across ch 6-8')

if __name__ == '__main__':
    main()
