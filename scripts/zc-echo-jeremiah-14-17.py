"""
Echo layer -- Jeremiah chapters 14-17
Run: python3 scripts/zc-echo-jeremiah-14-17.py

Key NT connections:
- 14:8:  "hope of Israel" / deliverer in trouble -- Acts 28:20; John 14:6
- 14:14: false prophets in YHWH's name -- Matt 7:22-23; Matt 24:11
- 16:14-15: new exodus replacing the old -- Luke 9:31; Acts 13:17-39
- 16:16: YHWH sending fishermen -- Matt 4:19 (fishers of men)
- 16:19: nations coming from ends of earth -- Isa 49:6; Matt 28:19; 1 Thess 1:9
- 17:1:  sin written on the heart vs. law on the heart -- 2 Cor 3:3; Heb 8:10
- 17:5-8: cursed/blessed contrast -- Gal 3:10-13; Rev 22:2
- 17:9:  heart more deceitful than anything -- Mark 7:21-23
- 17:10: YHWH searches hearts -- Rev 2:23 (Christ's self-identification)
- 17:13: spring of living water / names in the dust -- John 4:14; 7:37-38; 8:6-8
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f"  wrote {p.relative_to(ROOT)}")

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e["type"], e["target"]) for e in existing[ch][v]}
                for e in entries:
                    if (e["type"], e["target"]) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e["type"], e["target"]))

JEREMIAH_ECHOES = {
  "14": {
    "7": [
      {"type": "allusion", "target": "1 John 2:12", "note": "Act for the sake of your name though our sins testify against us -- the prayer for YHWH to act on behalf of his own name despite the people's guilt is answered in Christ's atonement: your sins have been forgiven on account of his name (1 John 2:12); also Rom 3:25-26 (God presented Christ as a sacrifice to demonstrate his justice... so as to be just and the one who justifies those who have faith in Jesus)"},
    ],
    "8": [
      {"type": "allusion", "target": "Acts 28:20", "note": "O hope of Israel, its deliverer in times of trouble -- the title hope of Israel that Jeremiah applies to YHWH as the rescuer in crisis is the exact phrase Paul uses at his Roman imprisonment (Acts 28:20: it is because of the hope of Israel that I am bound with this chain); the messianic deliverer who rescues in times of trouble is Christ, the personal embodiment of Israel's hope"},
    ],
    "14": [
      {"type": "allusion", "target": "Matt 7:22", "note": "The prophets are prophesying falsehoods in my name -- I did not send them, I did not command them, I did not speak to them -- Jesus applies the same criterion to false teachers who invoke his name: many will say to me on that day, Lord Lord, did we not prophesy in your name? And I will say to them, I never knew you (Matt 7:22-23); the unauthorized prophecy that Jeremiah condemns recurs as the NT's warning about those who claim Christ's name without genuine commission"},
      {"type": "allusion", "target": "Matt 24:11", "note": "Prophets prophesying in YHWH's name without being sent -- the unauthorized prophetic office Jeremiah warned against is the pattern for the many false prophets Jesus predicts will arise in the last days (Matt 24:11); the test of true prophecy (commission from YHWH vs. self-generated vision) is the OT ground for the NT's repeated warnings about false teachers"}
    ],
    "17": [
      {"type": "allusion", "target": "John 11:35", "note": "Let my eyes overflow with tears night and day without stopping, for the virgin daughter of my people has been shattered -- Jeremiah's weeping for Israel's destruction is the prophetic pattern enacted by Jesus: Jesus wept (John 11:35), and he wept over Jerusalem (Luke 19:41) precisely because he foresaw the fulfillment of what Jeremiah mourned; the prophet who wept over Israel's judgment is the type of the Son who weeps over the city before bearing its judgment"}
    ]
  },
  "15": {
    "1": [
      {"type": "allusion", "target": "Heb 7:25", "note": "Even if Moses and Samuel stood before me, my heart would not turn toward this people -- the limitation of even the greatest OT intercessors is answered by Christ whose intercession is unlimited and permanent: he always lives to make intercession for those who draw near to God through him (Heb 7:25); what Moses and Samuel could not accomplish at this point of Israel's sin, Christ accomplishes for all who come through him"},
    ],
    "2": [
      {"type": "allusion", "target": "Rev 13:10", "note": "Those destined for death, to death; those for the sword, to the sword; those for famine, to famine; those for captivity, to captivity -- Revelation applies this pattern to the end-time conflict: if anyone is to go into captivity, into captivity he will go; if anyone is to be killed with the sword, with the sword he will be killed (Rev 13:10); the Jeremianic inevitability of judgment becomes the eschatological pattern in Revelation"}
    ],
    "16": [
      {"type": "allusion", "target": "John 4:34", "note": "When I found your words I devoured them; your word was my joy and the delight of my heart -- the prophet who feeds on the divine word as his primary nourishment anticipates Jesus's saying: my food is to do the will of him who sent me and to finish his work (John 4:34); the nourishment Jeremiah found in YHWH's word corresponds to Christ who is himself the Word made flesh and who lives by every word that comes from the Father (Matt 4:4)"}
    ],
    "19": [
      {"type": "allusion", "target": "John 15:16", "note": "If you return to me I will restore you; you will stand before me -- the prophetic restoration to covenant standing that YHWH promises to Jeremiah after his complaint is the pattern of Christ's restoration of the disciples after their failure; you did not choose me but I chose you and appointed you to go and bear fruit (John 15:16); the restored prophet who utters the precious rather than the worthless is the type of the apostles restored after the resurrection"}
    ]
  },
  "16": {
    "9": [
      {"type": "allusion", "target": "Rev 18:23", "note": "I am about to silence in this place -- before your very eyes and in your days -- the voice of joy and gladness, the voice of the bridegroom and bride -- Revelation's lament over Babylon uses Jeremiah's exact phrase as the measure of judgment: the voice of the bridegroom and bride will never be heard in you again (Rev 18:23); the silence of covenant celebration that Jeremiah announced as judgment on Jerusalem becomes Revelation's measure of Babylon's final judgment"}
    ],
    "14": [
      {"type": "allusion", "target": "Luke 9:31", "note": "Days are coming when they will no longer say: as the LORD lives who brought Israel out of Egypt -- the promise that the new exodus will replace the old as the foundational saving event corresponds to Luke's description of the transfiguration conversation: they spoke of his departure (his exodus, in the Greek) which he was about to accomplish at Jerusalem (Luke 9:31); Christ's death-and-resurrection is the new exodus that supersedes the Sinai deliverance as the covenant's founding event"},
    ],
    "16": [
      {"type": "fulfillment", "target": "Matt 4:19", "note": "I am sending for many fishermen and they will fish them out -- YHWH's sending of fishermen to gather scattered Israel in judgment becomes the pattern Christ reverses and reapplies: follow me and I will make you fishers of men (Matt 4:19); what Jeremiah portrayed as the gathering-for-judgment (fishing Israel out of their hiding places) Christ transforms into the gathering-for-salvation -- the same fishing metaphor applied to redemptive rather than judicial gathering"},
    ],
    "19": [
      {"type": "allusion", "target": "1 Thess 1:9", "note": "The nations will come from the ends of the earth and say: our ancestors inherited only falsehood -- the eschatological turning of the nations from idols to YHWH is the global mission Christ commissions (Matt 28:19) and Paul describes as already happening: you turned to God from idols to serve the living and true God (1 Thess 1:9); what Jeremiah prophesied as the nations recognizing the falsehood of their idols is the universal evangelistic reality of the NT mission"}
    ]
  },
  "17": {
    "1": [
      {"type": "fulfillment", "target": "Heb 8:10", "note": "Judah's sin is engraved with an iron stylus on the tablet of their heart -- the sin written on the heart (Jer 17:1) is the negative image of the law written on the heart (Jer 31:33): both concern what is inscribed on the inner person. Hebrews quotes the new covenant promise (Heb 8:10: I will put my laws in their minds and write them on their hearts) as the direct contrast to this verse: what sin once engraved, the Spirit rewrites with the law of Christ; 2 Cor 3:3 (written not on tablets of stone but on tablets of human hearts by the Spirit of the living God)"}
    ],
    "5": [
      {"type": "allusion", "target": "Gal 3:10", "note": "Cursed is the one who trusts in human beings and relies on human strength, turning his heart from the LORD -- Paul cites a parallel curse-formula in Gal 3:10 (cursed is everyone who does not continue to do everything written in the book of the law); the Jeremianic curse on misplaced human trust is the OT framework for Paul's argument that those outside of Christ are under the curse of the law; both identify the same structural problem: trust directed away from YHWH toward what cannot save"},
    ],
    "7": [
      {"type": "allusion", "target": "Rev 22:2", "note": "Blessed is the one who trusts in the LORD -- he will be like a tree planted beside a stream, sending its roots out to the water -- the tree-by-water image of covenant blessing is the OT counterpart to the tree of life in Rev 22:2 (the tree of life with its twelve kinds of fruit, its leaves for the healing of the nations); the well-watered tree of Jeremiah's blessing becomes the eschatological tree of life whose leaves heal the nations in the new creation; also Ps 1:3"},
    ],
    "9": [
      {"type": "allusion", "target": "Mark 7:21", "note": "The heart is more deceitful than anything else and desperately sick -- who can understand it? -- Jesus's teaching on the corrupt heart (Mark 7:21-23: from within, out of the heart of a person, come evil thoughts, sexual immorality, theft, murder, adultery, greed, malice, deceit, lewdness, envy, slander, arrogance, and folly) is the NT exposition of Jeremiah's diagnostic; the corrupt heart that Jeremiah diagnosed is what Christ says the law cannot fix from outside but must be transformed from within (Ezek 36:26; John 3:3)"},
    ],
    "10": [
      {"type": "fulfillment", "target": "Rev 2:23", "note": "I the LORD examine the heart and test the inner mind, to give each person according to his conduct and actions -- in the letter to Thyatira, Christ identifies himself with precisely this divine function: I am he who searches hearts and minds (literally kidneys and hearts), and I will repay each of you according to your deeds (Rev 2:23); this is the most direct Christological appropriation of a YHWH-function in Revelation, identifying Christ's heart-searching judgment with the divine heart-searcher of Jeremiah 17:10"},
    ],
    "13": [
      {"type": "allusion", "target": "John 7:37", "note": "O LORD, the hope of Israel -- all who forsake you will be ashamed; those who turn away will have their names written in the dust, for they have forsaken the LORD, the spring of living water -- Christ applies the spring of living water image to himself at Tabernacles: if anyone is thirsty, let him come to me and drink (John 7:37-38); the spring of living water that Jeremiah identifies as YHWH himself is what Christ claims to be; also John 8:6-8 where Jesus writes in the dust (the only Gospel scene that echoes the dust-writing of Jer 17:13)"},
      {"type": "allusion", "target": "John 4:14", "note": "Those who forsake the LORD, the spring of living water -- Jesus offers the Samaritan woman the same spring: whoever drinks the water I give will never thirst again; the water I give will become a spring of water welling up to eternal life (John 4:14); the spring of living water that YHWH is in Jeremiah is the spring that Christ offers in John -- a direct Christological identification with the divine source"}
    ]
  }
}

def main():
    existing = load_echo("jeremiah")
    merge_echo(existing, JEREMIAH_ECHOES)
    save_echo("jeremiah", existing)
    print("Jeremiah 14-17 echoes written.")

if __name__ == "__main__":
    main()
