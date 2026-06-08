"""
MKT Christ Commentary — Isaiah chapter 24
Run: python3 scripts/zc-christ-isaiah-24.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- v. 5: broken everlasting covenant — shadow: new covenant in Christ restores it
- v. 13: olive-gleaning remnant — shadow: faithful remnant gathered in Christ
- v. 21: punishment of host of heaven and kings — shadow: 1 Cor 15:24-25; Rev 20
- v. 22: pit and prison — shadow: Rev 20:1-3 Satan bound
- v. 23: YHWH reigns, sun/moon confounded — shadow: Rev 21:23 new Jerusalem light
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
"24": {
"1": "<p>A revelation of God: YHWH empties (<em>b̄ôqēq</em>) and lays waste (<em>ûb̄ôl ĕqāh</em>) the earth — the verbs are intensive Polel forms conveying thorough, complete action. The cosmic scope of this judgment (the whole earth, not one nation) establishes this as the final-judgment register. Revelation 6-19 draws on this imagery throughout the seal and trumpet and bowl judgments. The theology: sin's ultimate trajectory is the unraveling of creation, which only Christ's new creation (Rev 21:5: <em>behold, I am making all things new</em>) can reverse.</p>",
"2": "<p>A revelation of God: all social distinctions are annulled — priest and people, servant and master, seller and buyer, borrower and lender — judgment is perfectly impartial. This is the NT principle: there is no partiality with God (Rom 2:11; Acts 10:34). At the judgment seat of Christ all will stand equally as individuals accountable to the same standard (2 Cor 5:10; Rev 20:12).</p>",
"3": "<p>A revelation of God: the earth will be utterly emptied and utterly plundered — <em>hib̄bôq tibb̄ôq hā'āreṣ wĕhib̄bôz tibb̄ôz</em> — the doubled infinitive absolutes are emphatic. YHWH has spoken this word, and it is irrevocable. This establishes the certainty of the judgment that Christ will execute at his return — the same divine word that announced creation now announces its undoing and renewal.</p>",
"4": "<p>A revelation of God: the earth mourns (<em>'āb̄ĕlāh</em>) and withers (<em>nāb̄ĕlāh</em>), the world languishes and withers, the high ones of the people languish. Creation's mourning anticipates the NT framework of Romans 8:19-22: the creation groans under the weight of human sin, waiting for the liberation that comes through the revelation of the children of God — liberation secured by Christ's redemption.</p>",
"5": "<p>A shadow: the earth defiled under its inhabitants — they have transgressed the laws, violated the statutes, broken the everlasting covenant (<em>b̄ārak û b̄ĕrît 'ôlām</em>). The broken everlasting covenant is the ground of the curse. Christ establishes the new covenant in his blood (Luke 22:20; Heb 13:20: the <em>everlasting covenant</em> established by the blood of the eternal shepherd) — the same <em>b̄ĕrît 'ôlām</em> that Isaiah 24:5 describes as broken is the one Christ restores in an unbreakable form.</p>",
"6": "<p>A revelation of God: the curse (<em>'ālāh</em>) devours the earth; few men are left. The divine curse is the outworking of covenant violation (cf. Deut 27-28 — the curses of covenant-breaking). Christ becomes a curse for us (Gal 3:13 — <em>cursed is everyone who hangs on a tree</em>), absorbing the covenant curse so that those who are in him receive the covenant blessing instead.</p>",
"7": "<p>A revelation of God: the new wine mourns (<em>'āb̄al tîrôš</em>), the vine languishes, all the merry-hearted sigh. The joy of harvest — central to covenant life (Deut 16:13-15; cf. Ps 4:7) — fails under judgment. Christ transforms this mourning: John 2:1-11 (water into wine at Cana) signals that messianic abundance reverses this loss; John 15:11 promises that his joy remains in his disciples.</p>",
"8": "<p>A revelation of God: the tambourines cease, the noise of the jubilant stops, the mirth of the lyre ceases. The complete silencing of celebration is the sign of total divine judgment (cf. Rev 18:22: the voice of harpists and musicians heard no more in Babylon). The absence of music signals the absence of shalom. Christ restores the song: Rev 5:9 (a new song sung before the Lamb).</p>",
"9": "<p>A revelation of God: they no longer drink wine with singing; strong drink is bitter to those who drink it. The celebratory drink turned bitter is a reversal of covenant blessing. The NT picks up this inversion at the cross: Jesus was offered wine mixed with gall (Matt 27:34) — the bitter drink at the moment of maximum judgment, after which he promises the new wine of the kingdom (Matt 26:29).</p>",
"10": "<p>A revelation of God: the city of chaos (<em>qiryat-tōhû</em>) is broken down — the word <em>tōhû</em> is the same as Genesis 1:2 (formless void). The city built on human pride reverts to pre-creation chaos. Christ is the one through whom all things were made (John 1:3) and by whom all things hold together (Col 1:17); apart from him, the Babel-cities collapse back into chaos.</p>",
"11": "<p>A revelation of God: in the streets they cry out for wine, all joy has gone dark, the gladness of the earth is banished. The complete reversal of covenant blessing points forward to the consummation: Christ promises that in the kingdom the disciples will drink wine new with him (Matt 26:29) — the restoration of what judgment takes away.</p>",
"12": "<p>A revelation of God: desolation is left in the city and the gate is battered to ruins. The city's destruction is comprehensive — it is the anti-type of the new Jerusalem (Rev 21:2) whose gates are never shut (Rev 21:25). The desolated city of Isaiah 24 gives way to the city of God as the ultimate telos.</p>",
"13": "<p>A shadow: among the peoples it will be as at the gleaning of an olive tree (<em>k̠ĕnōqēp̄ zayit</em>) — a few left after the harvest. The remnant who survive judgment are those who lift their voices in praise (v. 14). Christ gathers this remnant: Luke 12:32 (<em>fear not, little flock</em>); Revelation 7:9 (a great multitude from every nation — the remnant that turns out to be vast). The gleaning remnant becomes a multitude no one can number.</p>",
"14": "<p>A shadow: they lift up their voices and sing for joy, shouting from the west over the majesty of YHWH. The remnant's praise from the ends of the earth (east, v. 15; coastlands, v. 15; ends of the earth, v. 16) anticipates the universal worship of Revelation 7:9-12 — every nation, tribe, people, and language standing before the throne and before the Lamb, crying <em>Salvation belongs to our God and to the Lamb.</em></p>",
"15": "<p>A shadow: glorify YHWH in the east, and in the coastlands the name of YHWH God of Israel. The universal geographic scope of praise — east, west (v. 14), coastlands — is the eschatological worship that Christ's redemption makes possible. Acts 1:8 (<em>to the ends of the earth</em>) frames the missionary movement as the vehicle through which this east-west praise is gathered.</p>",
"16": "<p>A revelation of God: from the ends of the earth songs are heard — <em>glory to the Righteous One</em> (<em>ṣĕb̄î lĕṣaddîq</em>). But the prophet breaks off in anguish: <em>I pine away, I pine away. Woe is me!</em> — the treacherous still deal treacherously. The tension between the eschatological praise and the present reality of ongoing wickedness is the tension of the NT's <em>already and not yet</em> — the songs of the kingdom are real, but the full resolution awaits the return of the Righteous One himself (cf. Jas 5:8: the coming of the Lord is near).</p>",
"17": "<p>A revelation of God: terror, pit, and snare for the inhabitants of the earth — <em>paḥad wāpaḥat wāpāḥ 'ālèkā</em> — the wordplay (terror/pit/snare with overlapping sounds) emphasizes inescapability. The NT frames final judgment with the same inescapability: Hebrews 2:3 (<em>how shall we escape if we neglect such a great salvation?</em>); Revelation 6:15-17 (kings and generals hide but cannot escape the wrath of the Lamb).</p>",
"18": "<p>A revelation of God: flight from one danger encounters another — the one who flees the sound of terror falls into the pit; the one who climbs out of the pit is caught in the snare. The windows of heaven are opened and the foundations of the earth shake — the flood imagery of Genesis 7:11 is invoked for the final judgment. Christ's cross is the one place of escape (Rom 5:9 — saved through him from the wrath to come).</p>",
"19": "<p>A revelation of God: the earth is broken, split, shaken violently (<em>rō'āh hit rō'ĕ'āh hā'āreṣ</em> — intensive Hithpolel). The cosmic earthquake of final judgment appears throughout the prophets (Amos 8:8; Zech 14:4-5) and the NT (Matt 27:51 — earthquake at the crucifixion as anticipation; Rev 16:18 — greatest earthquake in history at the final bowl). The creation trembles at its Judge.</p>",
"20": "<p>A revelation of God: the earth staggers like a drunkard (<em>nûa' tānûa' hā'āreṣ k̠aššikkôr</em>), sways like a hut. Its transgression lies heavy upon it — the weight of accumulated sin destabilizes creation itself. This verse does not directly anticipate Christ but establishes the necessity of the new creation: a creation staggering under sin cannot be reformed; it must be replaced (Rev 21:1 — the first earth passed away).</p>",
"21": "<p>A shadow: YHWH punishes the host of heaven in heaven and the kings of the earth on earth. The judgment of cosmic powers (<em>ṣĕb̄ā' hammārôm</em> — host on high) alongside earthly rulers anticipates Paul's vision of Christ's triumph over all principalities and powers (1 Cor 15:24-25: he must reign until he has put all enemies under his feet; Eph 6:12 — rulers, authorities, powers of this dark world). Christ's cross is the decisive defeat of these powers (Col 2:15).</p>",
"22": "<p>A shadow: they will be gathered as prisoners in a pit, shut up in a prison, and after many days they will be punished. Revelation 20:1-3 uses this framework directly: the angel seizes the dragon, binds him, and throws him into the Abyss for a thousand years — <em>after many days will be punished</em> corresponds to the release and final judgment of Revelation 20:7-10. The sequence of binding, imprisonment, and final punishment is the precise structure of both Isaiah 24:22 and the Revelation's millennial vision.</p>",
"23": "<p>A shadow: the moon will be confounded and the sun ashamed when YHWH of hosts reigns on Mount Zion — the natural luminaries are superseded by the divine presence. Revelation 21:23 applies this directly to the new Jerusalem: <em>the city does not need the sun or the moon to shine on it, for the glory of God gives it light, and the Lamb is its lamp</em>. Isaiah 60:19-20 develops the same theme. The reign of YHWH on Zion is fulfilled in the reign of Christ (Rev 22:3: the throne of God and of the Lamb will be in the city). The glory that makes moon and sun irrelevant is the glory of the incarnate, crucified, and risen Lord.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 24 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
