"""
MKT Original Commentary — Ezra chapters 8–10
Run: python3 scripts/zc-original-ezra-8-10.py

Ch8: ʿānāh / lᵉhitʿannôt — humble/afflict-oneself; fasting vocabulary (8:21)
     yad ʾĕlōhênû — the hand-of-God formula; 9 occurrences in Ezra-Nehemiah (8:22)
     qōḏeš — consecrated vessel-bearers; vessel-holiness transferred to bearers (8:28)
     darkᵉmônîm / ʾadrarkônîm — darics; Persian gold coins; numismatic precision (8:27)
Ch9: bāḏal — to separate; Nip'al of bāḏal — not-separated-themselves; Lev 20:24-26 (9:1)
     ʿāwōn — iniquity; the guilt-accumulation image (9:6)
     yātēḏ — peg/nail in a holy place; unusual metaphor; Isa 22:23-25 connection (9:8)
     māʿal — treachery/unfaithfulness; the covenant-breach term (9:4)
Ch10: bāḏal Nip'al — to separate; the dissolution formula (10:11)
      yiqqāhēl — shall be forfeited; ḥerem-application to property (10:8)
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

DATA = {
  "8": {
    "21": "<p><span class='term'>lᵉhitʿannôt liphānê ʾĕlōhênû</span> — 'to humble ourselves before our God' (8:21). The root <span class='term'>ʿānāh</span> (to be low, afflicted) in the Hithpael reflexive designates the deliberate self-abasement of fasting: the worshipper voluntarily enters the physical condition of affliction as a posture of covenant dependence. The same root governs the affliction of the Day of Atonement (<em>tᵉʿannû ʾet-napšōtêkem</em>, Lev 16:29) — the mandatory national fast. Ezra's fast is voluntary rather than mandated but draws on the same theological vocabulary: the body's lowering signals the spirit's orientation. The request for 'a straight way' (<em>derek yᵉšārāh</em>) is itself a covenant idiom: the straight/level path as the route under divine direction (Isa 40:3-4; Ps 27:11).</p>",
    "22": "<p><span class='term'>yad-ʾĕlōhênû ʿal-kol-mᵉḇaqqᵉšāyw lᵉṭôḇāh</span> — 'the hand of our God is on all who seek him for good' (8:22). The <span class='term'>yad YHWH/ʾĕlōhîm</span> formula appears nine times in Ezra-Nehemiah as the shorthand for divine providential power and direction — 'the good hand of my God was upon me' is Nehemiah's repeated refrain (Neh 2:8, 18; cf. Ezra 7:6, 9, 28; 8:18, 22, 31). The formula has its roots in the Exodus narrative (YHWH's hand against Egypt, Exod 9:3) but is here domesticated into a personal-providential sense. The <span class='term'>mᵉḇaqqēš</span> participle (seeker) echoes Ezra's own verb in the Artaxerxes letter (7:10) and connects seeking-God to receiving the divine hand. The public declaration to the king — 'his power and wrath are against all who forsake him' — makes the formulation bilateral: hand-for-seekers, power-against-forsakers, the two sides of the covenant's conditional structure.</p>",
    "27": "<p><span class='term'>darkᵉmônîm / ʾadrarkônîm</span> — 'darics of gold' (8:27). The numismatic precision of the vessel list is notable: <span class='term'>darkᵉmôn</span> is the Hebrew transliteration of the Greek <em>dareikos</em> (from Persian <em>darayanush</em> = Darius), the standard gold coin of the Achaemenid Empire. These coins bore the image of the Persian king in running-archer posture. The Chronicler/Ezra's use of the technical coinage term (<em>ʾadrarkônîm</em> in 1 Chr 29:7 and Ezra 8:27) reflects the late Persian-period vocabulary in which Hebrew has absorbed the monetary terminology of the empire. The precise denomination and quantity of the donated gold vessels — 20 gold basins worth 1,000 darics = ~8.4 kg of gold — signals the accountability culture of Achaemenid temple administration.</p>",
    "28": "<p><span class='term'>qōḏeš ʾattem laYHWH</span> — 'you are holy to the LORD' (8:28). Ezra's declaration to the priests who will carry the vessels connects carrier-holiness to vessel-holiness: the consecrated containers require consecrated bearers. The <span class='term'>qōḏeš</span> designation places both the priests and the vessels in the same semantic domain as the temple itself — they are set apart from ordinary use. The holiness-transfer concept (<em>the sacred charges them with the quality of what they carry</em>) underlies the warning: 'Watch and keep them.' A failure in transport would be a violation of holiness, not merely a logistical failure. The Levitical tradition (Num 4:5-20) specifies exactly this principle for tabernacle transport — the carriers' holiness protects both themselves and the holy objects.</p>"
  },
  "9": {
    "1": "<p><span class='term'>lōʾ-hiḇḏalû</span> — 'they have not separated themselves' (9:1). The Nip'al of <span class='term'>bāḏal</span> (to divide, separate) is the technical term for the covenant-boundary separations YHWH established: between clean and unclean animals (Lev 11:47), between Israel and the nations (Lev 20:24-26: 'I have separated you from the peoples'), between the holy and the common (Lev 10:10). The Ezra narrative frames the intermarriage crisis as a bāḏal-failure: the separation that constituted covenant identity has not been maintained. The same verb governs the solution (10:11, 16: 'separate yourselves'; <em>hiḇḏalû</em>) — the covenant restoration precisely reverses the covenant violation using the identical technical term.</p>",
    "4": "<p><span class='term'>māʿal māʿal</span> — 'acted treacherously' (9:4). The root <span class='term'>mā'al</span> designates a specific kind of covenant breach — unfaithfulness to a sacred obligation or person. It is the word used for Achan's violation of the ḥerem (Josh 7:1), for unfaithfulness to a spouse (Num 5:12), and as the Chronicler's terminal diagnostic for fallen kings (2 Chr 36:14: 'all the officers of the priests and the people were exceedingly unfaithful, following all the abominations of the nations'). Its use here for the intermarriage violation identifies the act not merely as social mixing but as a betrayal of the covenant relationship — Israel's marriage to YHWH being undermined by the people's marriage to those devoted to other gods.</p>",
    "6": "<p><span class='term'>ʿāwōnōtênû rābû lᵉmaʿlāh mērōʾš</span> — 'our iniquities have risen higher than our heads' (9:6). The spatial image of <span class='term'>ʿāwōn</span> (iniquity/guilt) rising above the head is unusual — the guilt is so accumulated that it towers over the one who should be above it. <span class='term'>ʿāwōn</span> carries the double sense of the act of guilt and the consequent punishment-obligation (both 'iniquity' and 'its consequences'). The mounting-to-the-heavens image (<em>wᵉʾašmatênû gāḏᵉlāh ʿad laššāmayim</em>) recalls the tower-of-Babel vertical pride (Gen 11:4) reversed: there it was ambition reaching heaven; here it is guilt reaching heaven. The <em>ʾašmāh</em> (guilt, offense) in the parallel clause belongs to the priestly-legal vocabulary of cultic offense (Lev 5:15-26).</p>",
    "8": "<p><span class='term'>yātēḏ bimqôm qoḏšô</span> — 'a peg in his holy place' (9:8). The <span class='term'>yātēḏ</span> (tent-peg, nail) metaphor for divine favor is lexically distinctive. Its closest OT parallel is Isa 22:23-25 (the Eliakim oracle): YHWH will drive Eliakim 'like a peg in a secure place' (<em>yātēḏ bᵉmāqôm neʾĕmān</em>), a peg on which all the household's honor can hang — until the peg is cut down. Ezra's use of the same image for the remnant's precarious but real establishment in Judah ('to give us a peg in his holy place') draws on Isa 22's idea: a small, secure anchor point amid the expanse of judgment. The diminishing modifiers — 'a peg,' 'a little space,' 'a little reviving' — emphasize that what YHWH has given is minimal but real: covenant life clinging to its anchor in the sanctuary.</p>",
    "9": "<p><span class='term'>gāḏēr biyᵉhûḏāh ûḇîrûšālaim</span> — 'a wall in Judah and Jerusalem' (9:9). The <span class='term'>gāḏēr</span> (wall, fence, enclosure) is the word used for garden walls and vineyard enclosures (Num 22:24; Ps 80:12; Isa 5:5) rather than city fortifications (<em>ḥômāh</em>). The choice of <em>gāḏēr</em> — the enclosure of a cultivated garden — rather than the military <em>ḥômāh</em> is theologically significant: divine protection is presented as the gardener's enclosure of a vineyard (cf. Isa 5:1-7, where YHWH's care for Israel is figured as the vineyard's <em>gāḏēr</em>), not as a fortress wall. The covenant's protective function is cultivation, not merely fortification.</p>"
  },
  "10": {
    "8": "<p><span class='term'>yiqqāhēl kol-rᵉkûšô</span> — 'all his property shall be forfeited' (10:8). The verb <span class='term'>ḥāram</span> underlies the legal formula here (NIV 'forfeited'; lit. 'devoted to destruction/ban'). The <span class='term'>ḥerem</span> principle — the consecration of property to YHWH by exclusion from ordinary use — is being applied to covenant defaulters: failure to appear at the assembly within three days would result in the forfeiture of property and exclusion from the congregation of exiles. The application of the ḥerem logic to property in a covenant-discipline context is unusual — it transfers the war-spoils vocabulary of Deuteronomy into a post-exilic communal governance register. The 'congregation of the exiles' (<em>qᵉhal haggôlāh</em>) is itself a coinage — the exilic community as the new covenant assembly.</p>",
    "11": "<p><span class='term'>hiḇḏalû mikᵉʿammê hāʾāreṣ</span> — 'separate yourselves from the peoples of the land' (10:11). The Nip'al imperative of <span class='term'>bāḏal</span> mirrors the diagnosis of 9:1 (<em>lōʾ-hiḇḏalû</em>) in its solution: the covenant violation was not-separating; the covenant restoration is separating. The <em>bāḏal</em> vocabulary connects the entire Ezra 9-10 unit into a chiastic pair. The phrase <span class='term'>ʿammê hāʾāreṣ</span> (peoples of the land) is the Ezra-Nehemiah technical term for the non-exilic, mixed-population indigenous peoples — not identical with the Pentateuchal 'Canaanites' but invoking the same covenantal boundary. The dissolution of the foreign marriages (<em>nāšîm nᵉḵrîyyôt</em>, foreign women) is the practical enactment of bāḏal — the vocabulary of separation made domestic and personal.</p>"
  }
}

def main():
    c = load_comm('mkt-original', 'ezra')
    merge_comm(c, DATA)
    save_comm('mkt-original', 'ezra', c)
    count = sum(len(v) for v in DATA.values())
    print(f'ezra mkt-original: wrote {count} verses across ch 8-10')

if __name__ == '__main__':
    main()
