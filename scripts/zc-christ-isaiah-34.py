"""
MKT Christ Commentary — Isaiah chapter 34
Run: python3 scripts/zc-christ-isaiah-34.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- v. 4: sky rolled as scroll, stars fall — direct: Rev 6:13-14 (sixth seal); Matt 24:29
- v. 8: day of vengeance for Zion — shadow: Rev 19:2 (Christ avenges his servants)
- v. 10: smoke forever — shadow: Rev 14:11; 19:3 (eternal judgment smoke)
- v. 11-12: chaos/emptiness — shadow: Rev 18:2 (Babylon as haunt of unclean things)
- v. 16: scroll of YHWH, Spirit gathers — shadow: Book of Life / Rev 20:12
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
"34": {
"1": "<p>A revelation of God: all nations are summoned to hear, all peoples to listen — the earth and all that fills it, the world and all that comes from it. The universal scope of YHWH's address in Isaiah 34 is the same universal scope as the final judgment: Revelation 20:11-15 (a great white throne, and earth and sky fled from his presence; all the dead stood before the throne). The summons to all nations establishes that no nation is exempt from the divine reckoning — a principle that Christ as the universal Judge (Acts 17:31; John 5:22) fulfills.</p>",
"2": "<p>A revelation of God: YHWH's wrath is upon all the nations, his fury upon all their armies — they are devoted to destruction (<em>hĕḥĕrîmām</em>), given over to slaughter. The <em>herem</em> (devoted destruction) language from holy war is applied universally: all nations, not just Canaan's peoples. The eschatological fulfillment is Revelation 19:19-21 — the beast, the kings of the earth, and their armies gathered against Christ, and all of them slain by the sword from his mouth. The final <em>herem</em> of history is executed by the returning King.</p>",
"3": "<p>A revelation of God: their slain shall be cast out; their stench shall rise from their corpses; the mountains shall flow with their blood. The hyperbolic language of cosmic war — mountains flowing with blood — appears in Revelation 14:20: blood flowing from the winepress up to the height of a horse's bridle for sixteen hundred stadia. The scope of final judgment is beyond imagining; Isaiah 34:3 and Revelation 14:20 both reach for imagery that acknowledges its own inadequacy before the reality.</p>",
"4": "<p>A direct eschatological reference. The host of heaven dissolves (<em>wĕnāmak kol-ṣĕb̄ā' haššāmayim</em>), the skies roll up like a scroll (<em>kĕsefer niglāl</em>), and all their host falls like leaves from a vine. Revelation 6:13-14 cites this verse explicitly at the sixth seal: <em>the stars of the sky fell to the earth as a fig tree sheds its winter fruit; the sky vanished like a scroll being rolled up</em>. Jesus cites the same imagery in Matthew 24:29 (the sun darkened, moon without light, stars falling from heaven). The dissolution of the cosmic order in Isaiah 34:4 is the OT text that the NT reads as the cosmic sign accompanying Christ's return.</p>",
"5": "<p>A revelation of God: YHWH's sword is drunk in heaven; now it descends on Edom (<em>'al-'Edôm</em>) — the people he has devoted to judgment. Edom in the prophets (and especially in Obadiah, Isa 63:1-6) functions as the representative of all who oppose YHWH and his people. The sword drunk in heaven and descending is the imagery Revelation 19:15 applies to Christ: <em>from his mouth comes a sharp sword with which to strike down the nations</em>. The heavenly sword of Isaiah 34:5 is the sword of the mouth of the returning King.</p>",
"6": "<p>A revelation of God: YHWH's sword is filled with blood — fat and blood of lambs and goats and rams — the great sacrifice in Bozrah. The sacrifice metaphor frames the judgment of enemies as a cosmic offering — the inverse of Israel's sacrifices, where YHWH received the animal; here YHWH consumes the enemy as a sacrifice. Revelation 19:17-18 develops the same imagery: the angel calls all the birds to come to the great supper of God, to eat the flesh of kings and captains. The great feast of judgment is the anti-type of the Eucharist — the supper of death rather than the supper of life.</p>",
"7": "<p>A revelation of God: wild oxen and young bulls fall with the powerful — the land is soaked with blood, the soil saturated with fat. The completeness of the judgment — even the great beasts fall — establishes that no created power is exempt from divine justice. The NT frames this as the subjugation of all things under Christ: 1 Corinthians 15:24-28 (he must reign until he has put all enemies under his feet — the last enemy is death itself).</p>",
"8": "<p>A shadow: <em>kî yôm nāqām lĕYHWH šĕnat šillûmîm lĕrîb̠ Ṣiyyôn</em> — for YHWH has a day of vengeance (<em>nāqām</em>), a year of recompense for the cause of Zion. The divine vengeance is not arbitrary but forensic — it is <em>for the cause of Zion</em>, the vindication of YHWH's people. Revelation 19:2 applies this exactly: <em>his judgments are true and just; he has avenged (<em>exedikesen</em>) the blood of his servants</em>. Christ as the avenger of his martyred people (Rev 6:10 — <em>how long until you avenge our blood?</em> / Rev 19:2 — the answer) is the fulfillment of the day of YHWH's vengeance for Zion's cause.</p>",
"9": "<p>A revelation of God: Edom's streams turned to pitch, its soil to sulfur — the land a burning pitch. The transformation of a land into a perpetual burning (pitch and sulfur = continuous fire) is the imagery of Sodom and Gomorrah extended eschatologically. Jude 7 frames Sodom as a type of eternal fire for those who suffer the punishment of eternal fire. The burning of Edom is the historical-prophetic type of the eschatological fire prepared for the devil and his angels (Matt 25:41; Rev 20:10).</p>",
"10": "<p>A shadow: it shall not be quenched night or day; its smoke shall go up forever (<em>lĕ'ôlām ya'aleh 'āšānāh</em>). Revelation 14:11 quotes this: <em>the smoke of their torment goes up forever and ever, and they have no rest, day or night</em> — applied to those who worship the beast. Revelation 19:3 applies it to Babylon: <em>the smoke from her goes up forever and ever</em>. The eternal smoke of Isaiah 34:10 is the OT foundation for the NT's language of eternal judgment. Christ's warning about Gehenna (Mark 9:43-48: the fire that is not quenched, the worm that does not die) rests on this text and Isaiah 66:24.</p>",
"11": "<p>A shadow: the hawk, hedgehog, owl, and raven possess it — YHWH stretches over it the line of chaos (<em>qaw-tōhû</em>) and the plumb line of emptiness (<em>'ab̄nê-b̠ōhû</em>). The creation terms from Genesis 1:2 (<em>tōhû wāb̠ōhû</em> — formless and void) are applied as instruments of divine de-creation. What YHWH creates by imposing order on chaos, he un-creates by imposing chaos on order. Revelation 18:2 applies the same imagery to Babylon: <em>Babylon has become a dwelling place of demons, a haunt for every unclean spirit and every unclean bird</em>. The haunt of unclean birds marks de-creation.</p>",
"12": "<p>A revelation of God: its nobles call the kingdom nothing, all her princes shall be nothing. The dissolution of political order — the evacuation of meaning from all human hierarchies — is the eschatological reality that Christ's kingdom alone resists. Daniel 2:44 (the kingdom that shall never be destroyed) and Revelation 11:15 (the kingdom of the world has become the kingdom of our Lord and of his Christ) describe the positive counterpart: the divine kingdom that fills the space left when all human kingdoms are declared nothing.</p>",
"13": "<p>A shadow: thorns in its palaces, nettles and thistles in its strongholds — a haunt of jackals, an abode for ostriches. The reversal of human achievement — palace becomes wilderness, stronghold becomes desert — is the consistent eschatological judgment on pride-built cities. Babylon's fall in Revelation 18:19 (laid waste in a single hour) is the final fulfillment of this pattern. Christ's words about Jerusalem (Luke 21:6: not one stone left on another) apply the same logic to the city that rejected its messianic visitation.</p>",
"14": "<p>A revelation of God: desert creatures and wild goats meet in Edom; the night creature (<em>lîlît</em>) settles and finds rest there. The occupation of a ruined place by creatures of the night and wilderness — associated in ANE thought with chaos and the demonic — marks complete divine abandonment. The NT's language of unclean spirits returning to a swept house (Matt 12:43-45) uses the same logic: the place cleansed but not filled becomes the habitation of worse spirits. Edom's fate warns what happens when YHWH's presence departs.</p>",
"15": "<p>A revelation of God: the tree snake nests and lays eggs; the hawks gather, each with her mate. The wilderness creatures find their mates and multiply in the desolation — nature returns to fill the vacuum left by divine judgment on human civilization. The same theme of divine faithfulness to the natural order continuing even in judgment establishes the principle that YHWH does not abandon creation itself — only those who abuse it. Romans 8:21 frames creation's liberation from futility as the positive counterpart to Isaiah 34's de-creation narrative.</p>",
"16": "<p>A shadow: <em>diršû mê-'al sēp̄er YHWH wĕqirā'û</em> — seek from the scroll of YHWH and read. Not one of these shall be missing; none shall lack her mate. YHWH's Spirit has gathered them and his hand has portioned them. The <em>sēper YHWH</em> (scroll/book of YHWH) in which all things are written and from which all things are fulfilled anticipates the Book of Life in Revelation (13:8; 20:12-15): the scroll in which all names of those belonging to the Lamb are written. The Spirit's faithfulness in gathering all that the scroll decreed — not one missing — is the faithfulness that guarantees the complete fulfillment of every prophetic word about Christ (Luke 24:44: everything written about me in the Law, the Prophets, and the Psalms must be fulfilled).</p>",
"17": "<p>A revelation of God: YHWH has cast the lot for them, his hand has portioned it with the line — they shall possess it forever, from generation to generation they shall dwell in it. The permanence of divine judgment — the desolate land given as an eternal portion to the creatures of the wild — establishes that YHWH's sovereign decisions are irreversible. The same permanence applies to his positive decrees: the inheritance of the meek (Matt 5:5: they shall inherit the earth; cf. Ps 37:11), the eternal possession of those in Christ (1 Pet 1:4: an inheritance imperishable, undefiled, and unfading, kept in heaven for you). The eternal portion that Edom receives in desolation is the anti-type of the eternal inheritance the redeemed receive in Christ.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 34 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
