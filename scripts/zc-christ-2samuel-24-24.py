"""
MKT Christ Commentary — 2 Samuel chapter 24
Run: python3 scripts/zc-christ-2samuel-24-24.py

Ch24: Struck conscience and godly grief — John 16:8 / 2 Cor 7:10;
      Angel's sword stayed at threshing floor — Rom 3:25 / Heb 7:25 propitiation type;
      Threshing floor as judgment site — Matt 3:12 / John 2:13-17;
      Sacrifice that stops the plague — Heb 9:14 / Num 16:48 atonement type

Typological links:
- 24:10 → 2 Cor 7:10; John 16:8; Matt 5:3 — struck conscience / godly grief
- 24:16 → Rom 3:25; Heb 7:25; Heb 13:12 — angel of wrath stayed = propitiation type
- 24:18 → Matt 3:12; John 2:13-17 — threshing floor as judgment/separation site
- 24:25 → Heb 9:14; Num 16:48; Rom 5:9 — sacrifice arrests plague / blood averts wrath
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
  "24": {
    "10": "<p>The immediate conviction that follows David&rsquo;s census — <em>wayyak lēḇ dāwiḏ ʾōtô ʾaḥărê ḵēn sāpar ʾet hāʿām</em>, &lsquo;David&rsquo;s heart struck him after he had numbered the people&rsquo; — is the OT narrative form of what 2 Cor 7:10 identifies as &lsquo;godly grief&rsquo; (<em>hē kata theon lypē</em>): the inner conviction that produces repentance rather than mere regret. The striking of the heart is not psychological remorse alone but the work of the divine witness on the conscience — what Heb 4:12 describes as the word of God &lsquo;discerning the thoughts and intentions of the heart.&rsquo; John 16:8 names this as the Spirit&rsquo;s specific office: &lsquo;when he comes, he will convict the world concerning sin and righteousness and judgment.&rsquo; David&rsquo;s struck heart is the pre-Pentecost form of the same operation: the inner disclosure of divine displeasure that the NT identifies as the Holy Spirit&rsquo;s convicting work. The pattern — sin, heart-struck conviction, confession (<em>ḥāṭāʾtî</em>, &lsquo;I have sinned greatly&rsquo;), and the seeking of mercy — is the structural template of Ps 51 (whose postscript connects it to Nathan&rsquo;s confrontation, 12:13), and of Matt 5:3: &lsquo;blessed are the poor in spirit, for theirs is the kingdom of heaven.&rsquo; The Christological significance is that Christ&rsquo;s atoning work presupposes this convicting work: the sacrifice for sin accomplishes nothing for those whose heart has not been struck. The struck heart is the NT&rsquo;s &lsquo;poor in spirit&rsquo; — the prerequisite of the kingdom and the precondition of mercy received.</p>",
    "16": "<p>The scene at Araunah&rsquo;s threshing floor — the angel of destruction with drawn sword (<em>wᵉḥarḇô šᵉlûpāh bᵉyāḏô nᵉṭûyāh ʿal yᵉrûšālaim</em>), stayed by YHWH&rsquo;s command at the precise site where David will erect the altar — is the typological anticipation of the propitiatory function of the site itself. The threshing floor that becomes the temple mount is first the site where YHWH&rsquo;s angel of wrath is arrested by divine mercy. Rom 3:25 names the anti-type: God &lsquo;put [Christ] forward as a propitiation (<em>hilastērion</em>) by his blood&rsquo; — the mercy seat where divine wrath is satisfied and arrested. Heb 7:25 identifies the ongoing intercessory form of this arrest: Christ &lsquo;always lives to make intercession&rsquo; for those who draw near to God through him. The angel&rsquo;s sword stayed at Araunah&rsquo;s threshing floor maps the spatial theology of atonement: this is the location where judgment is halted and where sacrifice is offered. 2 Chr 3:1 will identify it as the site of the temple — the permanent institutional locus of the sacrificial system whose final form is the cross. Heb 13:12: &lsquo;Jesus also suffered outside the gate in order to sanctify the people through his own blood&rsquo; — the wrath arrested at the threshing floor in 2 Samuel is exhausted at Golgotha, just outside the city that the temple on that threshing floor had dominated for a thousand years.</p>",
    "18": "<p>The divine command to David — <em>ʿălēh hāqēm laYHWH mizḇēaḥ bᵉgōren ʾărawnāh hayᵉḇûsî</em>, &lsquo;go up, erect an altar to YHWH on the threshing floor of Araunah the Jebusite&rsquo; — designates as the sacred site a <em>gōren</em> (threshing floor), the locus of grain-from-chaff separation and judgment. The threshing floor as a type of eschatological judgment governs Matt 3:12: &lsquo;his winnowing fork is in his hand, and he will clear his threshing floor and gather his wheat into the barn, but the chaff he will burn with unquenchable fire.&rsquo; The temple, built on this threshing floor (2 Chr 3:1), inherits the judgment function of the site: it is the place where YHWH meets Israel in both mercy (the sacrificial system) and judgment (Jer 7:14: &lsquo;I will do to this house what I did to Shiloh&rsquo;; Ezek 9–11: the divine glory departing before destruction). Jesus&rsquo;s temple-cleansing (John 2:13-17; Matt 21:12-13) is the messianic threshing-floor action — the Son arriving at the site founded by his ancestor to execute the judgment of separation that the site has always anticipated. The trajectory from 2 Samuel to the NT: plague arrested at threshing floor → altar established → temple built on threshing floor → Messiah cleanses the temple in threshing-floor judgment → temple destroyed and superseded by the Messiah&rsquo;s own body (John 2:19-21).</p>",
    "25": "<p>David&rsquo;s burnt offerings and peace offerings on Araunah&rsquo;s threshing floor arrest the plague: <em>wayyeʿātar YHWH lāʾāreṣ wattēʿāṣar hammaggēpāh mēʿal yiśrāʾēl</em> — &lsquo;YHWH responded to the plea for the land, and the plague was averted from Israel.&rsquo; The blood of the offering turns away the wrath that was destroying the people. This is the sacrificial template that the entire tabernacle/temple system will institutionalize, and whose anti-type Heb 9:14 names: &lsquo;how much more will the blood of Christ, who through the eternal Spirit offered himself without blemish to God, purify our conscience from dead works to serve the living God.&rsquo; The plague of death spreading through Israel because of David&rsquo;s sin is the concentrated form of what sin always produces — death spreading through the community by transgression (Rom 5:12: &lsquo;sin came into the world through one man, and death through sin, and so death spread to all men&rsquo;). The intercessor who stands in the gap between the living and the dead is prefigured in Num 16:48, where Aaron runs with his censer into the midst of the dying congregation and the plague is stopped at the place where he stands. The anti-type: Christ stands in the gap between the living and the dead, his death the atonement that arrests the plague at its source. Rom 5:9: &lsquo;since we have now been justified by his blood, how much more shall we be saved from God&rsquo;s wrath through him.&rsquo;</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '2samuel')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '2samuel', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'2samuel mkt-christ: wrote {count} verses across ch 24')

if __name__ == '__main__':
    main()
