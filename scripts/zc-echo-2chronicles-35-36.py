"""
Echo Layer — 2 Chronicles chapters 35–36
Run: python3 scripts/zc-echo-2chronicles-35-36.py

Key echo connections in this range:
- 35:1: Josiah's Passover on the 14th day → 1 Cor 5:7 (Christ our Passover)
- 35:13: fire-roasted Passover lamb → Exod 12:8-9; John 19:36
- 35:18: greatest Passover since Samuel → Luke 22:15-16
- 35:25: Jeremiah's lament at Megiddo → Zech 12:10-11 (mourning for the pierced one)
- 36:16: "no remedy" (ʿad lēʾên marpēʾ) → Mark 2:17; Luke 4:18
- 36:21: land's Sabbath rest 70 years → Heb 4:9; Lev 26:34
- 36:22-23: Cyrus decree — the close of the Hebrew canon → Matt 2:1-2; Rev 22:20
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

CHRON2_ECHO_35_36 = {
  "35": {
    "1": [
      {"type": "type", "target": "1 Cor 5:7", "note": "Josiah slaughters the Passover lamb on the fourteenth of the first month (the exact date of Exod 12:6) — the most precise Passover observance since the Mosaic institution; the entire Passover theology of 2 Chr 35 is the shadow of which Paul declares the substance: &#8220;Christ, our Passover lamb, has been sacrificed&#8221; (1 Cor 5:7); Josiah&#8217;s unprecedented Passover precision points to the one who would be crucified on the precise Passover date (John 19:14; 1 Cor 5:7) and whose death fulfilled every Passover element"},
      {"type": "allusion", "target": "John 19:36", "note": "The Passover lamb slaughtered on the 14th of Nisan — &#8220;they shall not break any of its bones&#8221; (Exod 12:46; Num 9:12) — is the regulation Josiah&#8217;s meticulous Passover upholds; John explicitly identifies this as fulfilled in Jesus&#8217; crucifixion: &#8220;these things took place that the Scripture might be fulfilled: not one of his bones will be broken&#8221; (John 19:36); Josiah&#8217;s great Passover is the penultimate celebration before the one that the Passover had always been pointing toward"}
    ],
    "13": [
      {"type": "type", "target": "Exod 12:8", "note": "The Passover animals are roasted with fire (yᵉbaššᵉlû bāʾēš) according to the Mosaic prescription — &#8220;roasted with fire&#8221; (Exod 12:8-9); the fire-roasted lamb is the most visceral type of the one who would be consumed by the fire of divine judgment on behalf of the people; as the Passover lamb bore the heat of fire, Christ bore the wrath that would have consumed the people (Isa 53:10; Gal 3:13): &#8220;the LORD has laid on him the iniquity of us all&#8221;"}
    ],
    "18": [
      {"type": "allusion", "target": "Luke 22:15", "note": "&#8220;No Passover like it had been kept in Israel since the days of Samuel the prophet&#8221; — the superlative Passover before the Exile finds its superseding fulfillment in Jesus&#8217; last Passover: &#8220;I have earnestly desired to eat this Passover with you before I suffer&#8221; (Luke 22:15-16); as Josiah&#8217;s Passover was unprecedented in its covenant faithfulness and national scope, Jesus&#8217; final Passover was unprecedented as the moment when the feast became simultaneously the sacrifice and the feast — host and lamb in one person"}
    ],
    "21": [
      {"type": "allusion", "target": "John 11:51", "note": "Pharaoh Neco sends word to Josiah: &#8220;God has commanded me to hurry. Cease opposing God, who is with me&#8221; — a pagan king speaks a true divine word that the righteous king ignores; the pattern of divine speech through unexpected human channels recurs in the NT: Caiaphas unwittingly prophesies &#8220;that Jesus would die for the nation&#8221; (John 11:51); the irony in both cases is that a political figure outside the covenant community speaks a divine word that carries more weight than recognized"}
    ],
    "25": [
      {"type": "allusion", "target": "Zech 12:10", "note": "Jeremiah composed laments for Josiah, and &#8220;all the singing men and women have spoken of Josiah in their laments to this day; they made these a rule in Israel&#8221; — the great mourning at Megiddo for the fallen righteous king becomes the OT type of Zech 12:10-11: &#8220;they will look on me, the one they have pierced, and they will mourn for him as one mourns for an only child&#8221; (v10), &#8220;the weeping in Jerusalem will be as great as the weeping of Hadad-rimmon in the plain of Megiddo&#8221; (v11); the lament for Josiah at Megiddo becomes the template for the eschatological mourning over the pierced Christ"}
    ]
  },
  "36": {
    "13": [
      {"type": "allusion", "target": "Heb 3:15", "note": "Zedekiah &#8220;stiffened his neck and hardened his heart against turning to the LORD, the God of Israel&#8221; — the vocabulary of hardening (qāšāh ʿorep; ʿimmeṣ lēḇāḇô) is the Chronicler&#8217;s climactic statement on the royal failure that necessitates exile; the author of Hebrews deploys the same warning against hardening from Ps 95:7-8: &#8220;Today, if you hear his voice, do not harden your hearts&#8221; (Heb 3:15; 4:7); Zedekiah&#8217;s hardened heart is the negative exemplar for the new covenant community not to repeat in the face of the greater word spoken in the Son (Heb 1:2)"}
    ],
    "16": [
      {"type": "allusion", "target": "Mark 2:17", "note": "The Chronicler&#8217;s verdict on the final generation: &#8220;they mocked the messengers of God, despised his words, and scoffed at his prophets, until the wrath of the LORD rose against his people, until there was no remedy (ʿad lēʾên marpēʾ)&#8221; — the diagnosis of utter incurability that the exile represents; Jesus declares himself the physician sent for those who are incurably sick: &#8220;Those who are well have no need of a physician, but those who are sick; I came not to call the righteous, but sinners&#8221; (Mark 2:17); &#8220;lēʾên marpēʾ&#8221; is the precise condition that requires the healer who is greater than any medicine Israel&#8217;s history has offered"},
      {"type": "allusion", "target": "Luke 4:18", "note": "&#8220;No remedy&#8221; (lēʾên marpēʾ) — the Chronicler&#8217;s summary of Israel&#8217;s terminal condition — is the condition that Jesus announces he has come to address: quoting Isa 61:1-2 in the Nazareth synagogue, &#8220;The Spirit of the Lord is upon me, because he has anointed me to proclaim good news to the poor... to proclaim liberty to the captives and recovery of sight to the blind, to set at liberty those who are oppressed&#8221; (Luke 4:18); the exile that ends 2 Chronicles with &#8220;no remedy&#8221; is the condition from which Jesus announces release"}
    ],
    "21": [
      {"type": "allusion", "target": "Lev 26:34", "note": "The land keeps its Sabbath rests during the seventy years of exile — fulfilling Lev 26:34-35 (&#8220;the land shall enjoy its Sabbaths&#8221;) and Jer 25:11; 29:10: the forced Sabbath for the land corresponds exactly to Israel&#8217;s failure to observe the Sabbath years; judgment restores the rhythm of rest that covenant faithlessness had disrupted"},
      {"type": "allusion", "target": "Heb 4:9", "note": "The land&#8217;s enforced seventy-year Sabbath rest (fulfilling Lev 26:34) is the temporal type of the &#8220;Sabbath rest that remains for the people of God&#8221; (Heb 4:9); as the land kept its Sabbaths when Israel could not, so the eschatological rest that Christ provides is the permanent Sabbath that Israel&#8217;s history only partially glimpsed; &#8220;whoever has entered God&#8217;s rest has also rested from his works as God did from his&#8221; (Heb 4:10) — the exile&#8217;s Sabbath land points to the final rest"}
    ],
    "22": [
      {"type": "type", "target": "Isa 45:1", "note": "Cyrus king of Persia is stirred by the Spirit of YHWH (hēʿîr YHWH ʾet-rûaḥ Kōreš) to issue a decree releasing Israel to return and rebuild the temple — a Gentile emperor as the instrument of divine restoration; Isaiah had named Cyrus by name 150 years before his birth (Isa 44:28; 45:1: &#8220;I call him by name&#8221;) and called him &#8220;my shepherd&#8221; and YHWH&#8217;s &#8220;anointed&#8221; (mᵉšîḥî) — the only non-Israelite in Scripture given the title of anointed; the pagan king who serves the divine restorative purpose points to the one who is the true Anointed, the true shepherd, through whom the ultimate restoration comes"}
    ],
    "23": [
      {"type": "allusion", "target": "Rev 22:20", "note": "The final words of Chronicles — and of the Hebrew Bible in its canonical order — are Cyrus&#8217;s decree: &#8220;Whoever is among you of all his people, may the LORD his God be with him. Let him go up&#8221; (yaʿal); the Hebrew Bible closes not with arrival but with an invitation and an imperative to ascend to Jerusalem; the NT echoes this closing note in Rev 22:17: &#8220;The Spirit and the Bride say, Come&#8221; and in Rev 22:20: &#8220;Come, Lord Jesus!&#8221; — the Hebrew canon&#8217;s final call (&#8220;let him go up&#8221;) becomes the NT&#8217;s Maranatha (&#8220;let him come down&#8221;): the meeting point is the New Jerusalem where God dwells with his people (Rev 21:3)"},
      {"type": "allusion", "target": "Matt 2:1", "note": "Cyrus the Gentile king declares &#8220;YHWH the God of heaven has given me all the kingdoms of the earth, and he has charged me to build him a house at Jerusalem&#8221; — a pagan empire acknowledging YHWH&#8217;s universal sovereignty as the basis of temple restoration; the Magi from the East (Matt 2:1-2) — Gentiles coming to acknowledge Israel&#8217;s king at the birth of Jesus — are the NT counterpart: the Gentile world recognizing the coming of the one who is himself the temple (John 2:21), the house of YHWH that Cyrus only pointed toward; the pattern of Gentiles serving the purposes of Israel&#8217;s restoration runs from Cyrus to the Magi to Paul&#8217;s mission to the nations"}
    ]
  }
}

def main():
    existing = load_echo('2chronicles')
    merge_echo(existing, CHRON2_ECHO_35_36)
    save_echo('2chronicles', existing)
    print('2 Chronicles 35-36 echo layer written.')

if __name__ == '__main__':
    main()
