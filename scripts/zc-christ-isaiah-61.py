"""
MKT Christ Commentary — Isaiah chapter 61
Run: python3 scripts/zc-christ-isaiah-61.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Note: verse 1 already present; merge_comm will skip it. All 11 included for completeness.

Key decisions in this range:
- v. 1: direct — Luke 4:18-19 (Jesus reads this in Nazareth: Today this is fulfilled)
- v. 2a: year of YHWH's favor — direct: Luke 4:21; 2 Cor 6:2
- v. 2b: day of vengeance (Jesus stops reading mid-verse) — first/second advent gap
- v. 3: oil of gladness — shadow: Heb 1:9; Rev 21:4
- v. 6: priests of YHWH — direct: 1 Pet 2:9; Rev 1:6; 5:10
- v. 8: everlasting covenant — direct: Heb 13:20
- v. 10: garments of salvation/righteousness — shadow: Gal 3:27; 2 Cor 5:21; Rev 19:8
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
    # INTENT: Non-destructive merge — existing entries are never overwritten, safe to re-run
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]: existing[ch][v] = html

ISAIAH = {
"61": {
"1": "<p>A direct prophecy. <em>Rûaḥ 'ădōnāy YHWH 'ālay ya'an māšaḥ YHWH 'ōtî lĕb̠aśśēr 'ănāwîm šĕlāḥanî laḥăb̠ōš lĕnišb̠ĕrê-lēb̠ liqrō' lišb̠ûyîm dĕrôr wĕla'ăsûrîm pĕqaḥ-qôaḥ</em> — the Spirit of YHWH is upon me, because YHWH has anointed me to bring good news to the poor; he has sent me to bind up the brokenhearted, to proclaim liberty to the captives and the opening of the prison to those who are bound. Luke 4:18-21: Jesus reads this text in the Nazareth synagogue and says, <em>today this scripture has been fulfilled in your hearing</em>. This is the most explicit self-identification of Jesus with Isaiah's Servant in the Gospels. The anointing (<em>māšaḥ</em>) that makes one a <em>māšîaḥ</em> (Messiah/Christ) is the Spirit-anointing at his baptism (Luke 3:22) that inaugurates the ministry of Isaiah 61:1.</p>",
"2": "<p>A direct prophecy with a noted gap. <em>Liqrō' šĕnat-rāṣôn laYHWH wĕyôm nāqām lē'lōhênû lĕnaḥēm kol-'ăb̄ĕlîm</em> — to proclaim the year of YHWH's favor, and the day of vengeance of our God; to comfort all who mourn. Luke 4:20 records that Jesus rolled up the scroll and sat down after reading <em>to proclaim the year of YHWH's favor</em> — stopping before <em>and the day of vengeance of our God</em>. This mid-sentence pause is theologically precise: the year of favor is the first advent (grace and healing); the day of vengeance is the second advent (judgment). 2 Corinthians 6:2 (<em>behold, now is the favorable time; behold, now is the day of salvation</em>) applies the year of favor to the gospel age. The day of vengeance awaits Christ's return (Rev 19:11-21).</p>",
"3": "<p>A shadow: to grant to those who mourn in Zion — a beautiful headdress (<em>pĕ'ēr</em>) instead of ashes, the oil of gladness (<em>šemen śāśôn</em>) instead of mourning, the garment of praise instead of a faint spirit. Hebrews 1:9 quotes Psalm 45:7 of Christ: <em>God has anointed you with the oil of gladness beyond your companions</em> — the anointed one who possesses the oil of gladness himself gives it to those who mourn. Revelation 21:4 is the eschatological fulfillment: God will wipe away every tear; there will be no more mourning or crying. The oaks of righteousness (<em>'êlê haṣṣedeq</em>) are those rooted in Christ (Col 2:7: rooted and built up in him), displaying the righteousness that is his gift.</p>",
"4": "<p>A shadow: they shall build up the ancient ruins; raise up the former devastations; repair the ruined cities. The rebuilding theme of Isaiah 58:12 continues here. The community formed by the Servant's ministry becomes a restoring community — the church as rebuilder of what sin has destroyed. Ephesians 2:19-22 (built on the foundation of the apostles and prophets, Christ being the cornerstone; the whole structure joined together grows into a holy temple in the Lord). The ancient ruins are the shattered human condition; the rebuilt city is the community of the new covenant gathered in Christ.</p>",
"5": "<p>A shadow: strangers shall tend your flocks; foreigners shall be your plowmen and vinedressers. The inclusion of foreigners in the service of Zion is the type of the Gentile mission: not the replacement of Israel by Gentiles but the incorporation of Gentiles into the covenant community. Romans 11:17 (Gentile branches grafted into the olive tree) and Ephesians 3:6 (the Gentiles are fellow heirs, members of the same body) describe the same dynamic. The foreigners who serve Zion are the Gentile believers whose inclusion fulfills Isaiah's vision of a united human family before YHWH.</p>",
"6": "<p>A direct prophecy. <em>Wĕ'attem kōhănê YHWH tiqāre'û mĕšārtê 'Ĕlōhênû yē'āmēr lākem</em> — but you shall be called the priests of YHWH; they shall speak of you as the ministers of our God. 1 Peter 2:9 applies this directly to the church: <em>you are a chosen race, a royal priesthood, a holy nation, a people for his own possession</em>. Revelation 1:6 (he has made us a kingdom, priests to his God and Father) and 5:10 (you have made them a kingdom and priests to our God) cite the same prophetic promise as fulfilled in Christ's work. The universal priesthood — all the redeemed as priests — is what Exodus 19:6 promised and Isaiah 61:6 reaffirms, fulfilled through Christ who is both high priest and the one who makes his people priests.</p>",
"7": "<p>A shadow: instead of your shame there shall be a double portion; instead of dishonor they shall rejoice in their lot; they shall have everlasting joy (<em>śimḥat 'ôlām</em>). The reversal of shame into double honor is the eschatological pattern that Christ enacts: the one who endured the shame of the cross (Heb 12:2: despising the shame) receives the honor of the exaltation at the Father's right hand. Those who share his shame share his honor: Romans 8:17 (we suffer with him in order that we may also be glorified with him). The everlasting joy of Isaiah 61:7 is the joy that no one can take away (John 16:22).</p>",
"8": "<p>A direct prophecy. <em>Kî 'ănî YHWH 'ōhēb̠ mišpāṭ śōnē' gāzēl bĕ'ôlāh ûnātattî pĕullah bě'emet lāhem ûb̠ĕrît 'ôlām 'ekrōt lāhem</em> — for I, YHWH, love justice; I hate robbery and wrong; I will faithfully give them their recompense, and I will make an everlasting covenant (<em>b̠ĕrît 'ôlām</em>) with them. Hebrews 13:20 identifies this everlasting covenant as the new covenant sealed in Christ's blood: <em>the God of peace who brought again from the dead our Lord Jesus, the great shepherd of the sheep, by the blood of the eternal covenant</em>. The same <em>b̠ĕrît 'ôlām</em> that Isaiah 24:5 describes as broken and Isaiah 55:3 promises to restore is established permanently through the blood of the Servant.</p>",
"9": "<p>A shadow: their offspring shall be known among the nations, and their descendants in the midst of the peoples; all who see them shall acknowledge them as an offspring YHWH has blessed. The visible blessing of the covenant community among the nations — recognized even by outsiders as YHWH's blessed people — is the NT picture of the church's witness: Matthew 5:16 (let your light shine before others, so that they may see your good works and give glory to your Father who is in heaven). The offspring known among the nations are those born again through the Servant's gospel (John 1:12-13; 1 Pet 1:23), whose transformed lives testify that they are an offspring YHWH has blessed.</p>",
"10": "<p>A shadow: <em>śôś 'āśîś baYHWH tāgēl nap̄šî bē'lōhay kî hilbîšanî b̠igdê-yēša' mĕ'îl ṣĕdāqāh</em> — I will greatly rejoice in YHWH; my soul shall exult in my God, for he has clothed me with the garments of salvation (<em>bigdê-yēša'</em>); he has covered me with the robe of righteousness (<em>mĕ'îl ṣĕdāqāh</em>), as a bridegroom decks himself, as a bride adorns herself. The clothing imagery is the NT's forensic justification in pictorial form: 2 Corinthians 5:21 (in him we might become the righteousness of God); Galatians 3:27 (you have clothed yourselves with Christ); Revelation 19:8 (the fine linen, bright and pure, represents the righteous deeds of the saints). The exultation of the one clothed in salvation is the joy of justification — what Paul describes in Romans 5:1-2 as peace with God and rejoicing in hope.</p>",
"11": "<p>A shadow: as the earth causes its sprouts to spring up, and a garden causes what is sown in it to sprout up, so the Lord YHWH will cause righteousness and praise to sprout up before all the nations. The agricultural metaphor of righteousness sprouting before all nations is the gospel's universal scope: Romans 1:17 (the righteousness of God is revealed from faith to faith); John 12:24 (unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit). The mustard seed and leaven parables (Matt 13:31-33) use the same natural-growth imagery for the kingdom: the Servant's work, once planted, produces a harvest that fills the earth with righteousness and praise to YHWH.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 61 mkt-christ: {v} verses in script (merge skips existing v.1).')

if __name__ == '__main__':
    main()
