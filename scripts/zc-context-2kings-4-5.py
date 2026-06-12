"""
MKT Context Commentary — 2 Kings chapters 4–5
Run: python3 scripts/zc-context-2kings-4-5.py

Ch4: Elisha and the Shunammite woman — the wealthy woman as patron; the closed room
     hospitality; the parallels with Elijah/Zarephath widow pattern; upper room / Lk 22
Ch5: Naaman's healing — Aramean military disease; leprosy in ANE (ṣāraʿat);
     Jordan as covenant-boundary water; the Gehazi punishment as Naaman's displaced
     judgment; Naaman's portion of Israelite soil — ANE territorial deity assumptions

ANE/historical context:
- 4:10: the prophet's upper room (ʿaliyyat qîr) — stone-room hospitality for the holy man
- 5:1: naʿman = 'pleasant/gracious' — Aramean sar ṣāḇāʾ healed by Israelite prophet
- 5:10: Jordan as covenant water — 7 immersions / cleansing rite
- 5:17: two mule-loads of Israelite soil — portable deity theology / ANE territorial limits
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
  "4": {
    "10": "<p>The Shunammite&rsquo;s hospitality to Elisha — constructing a dedicated <em>ʿaliyyat qîr</em> (a walled upper room with a bed, table, chair, and lamp) — reflects both the ANE hospitality tradition for wandering holy men and the particular Israelite institution of the <em>ʾîš ʾelōhîm</em> (man of God) as a recognized social-religious figure supported by wealthy patrons. The <em>ʿaliyyāh</em> (upper room/chamber) was a distinct room typically built on the roof or as a second story, providing the most private and prestigious space in the house; the furnishing details (bed, table, chair, lamp) indicate a permanent guest room for regular use, not temporary hospitality. Comparable ANE parallels: the Ugaritic text KTU 1.17 depicts the hero Danel receiving a divine oracle after offering hospitality to the divine messengers, establishing the reciprocal pattern of hospitality-to-divine-agent yielding divine provision. The Elijah/Zarephath widow parallel (1 Kgs 17:19-23: Elijah brought to the widow&rsquo;s upper room, raises her son there) establishes the <em>ʿaliyyāh</em> as the space for the greatest miracle: the son raised in the upper room of the man of God. Both &lsquo;upper room&rsquo; episodes anticipate the NT&rsquo;s upper room (Mark 14:15: <em>anagaion</em>) where the Last Supper is held, and Acts 1:13 where the disciples await the Spirit — the upper room as the space of covenant renewal and resurrection presence.</p>"
  },
  "5": {
    "10": "<p>Elisha&rsquo;s instruction to Naaman — <em>hālôḵ wᵉrāḥaṣtā šeḇaʿ pᵉʿāmîm bayyardēn</em>, &lsquo;go and wash yourself seven times in the Jordan&rsquo; — is medically, ritually, and geographically specific. The <em>ṣāraʿat</em> (conventionally translated &lsquo;leprosy&rsquo; but covering a range of skin conditions in the Levitical purity system, Lev 13-14) was the purity condition that required a seven-step ritual cleansing in the Levitical law (Lev 14:1-9: the cleansed person washes clothes seven days). The number seven in the Elisha instruction echoes Levitical ritual completeness. The Jordan&rsquo;s choice is geographically pointed: Naaman wants the rivers of Damascus, which are &lsquo;better&rsquo; by any measure of water quality (v12: Abana and Pharpar). The Jordan is the covenant-boundary water of Israelite religious geography — the water Joshua crossed (Josh 3), the water John will baptize in, the water at which Elijah and Elisha parted the waters (2 Kgs 2:8, 14). The healing occurs in the covenant-water of YHWH&rsquo;s people, not in the superior rivers of Damascus — signaling that cleanness is defined by YHWH&rsquo;s covenant, not by natural quality. The seven-fold immersion in covenant-water is the ritual precursor for the NT&rsquo;s baptismal theology: entry into cleanness through the water of covenant-belonging (Rom 6:4).</p>",
    "17": "<p>Naaman&rsquo;s request for &lsquo;two mule-loads of earth (<em>ʾădāmāh</em>)&rsquo; to take back to Aram is a window into standard ANE territorial-deity theology. Throughout the ancient Near East, deities were understood as geographically bound: the gods of a nation were associated with its land, temples, and territory; a worshipper of a particular god who relocated to foreign soil required either the worship of the new territory&rsquo;s gods or some way of bringing the deity&rsquo;s territory with them. The Assyrian inscriptions and Egyptian wisdom texts document the assumption that divine power was territorially limited. Naaman&rsquo;s request is coherent within this framework: to worship YHWH in Damascus requires Israelite soil as the physical substrate of YHWH&rsquo;s presence. Elisha&rsquo;s response — <em>lēḵ lᵉšālôm</em>, &lsquo;go in peace&rsquo; — neither endorses the theology nor corrects it explicitly; the narrator leaves the theological irony implicit. The prior verse (v15: &lsquo;now I know that there is no God in all the earth but in Israel&rsquo;) is a more advanced theology than the two-mule-loads request that follows, suggesting Naaman&rsquo;s understanding is transitional. Isa 40:12-31 provides the theological correction: YHWH is not territorially limited but measures the waters in the hollow of his hand; he is the creator of the ends of the earth. John 4:21-24 (Jesus to the Samaritan woman: &lsquo;the hour is coming when neither on this mountain nor in Jerusalem will you worship the Father&rsquo;) is the final dissolution of the territorial-worship assumption that the two-mule-loads request embodies.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2kings mkt-context: wrote {count} verses across ch 4-5')

if __name__ == '__main__':
    main()
