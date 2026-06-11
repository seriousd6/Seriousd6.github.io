import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]: existing[ch][v] = entries

ECHOES = {
  "11": {
    "4": [
      {"type": "allusion", "target": "1 Cor 10:6", "note": "Paul uses the wilderness craving as a direct type-warning: 'these things took place as examples for us, that we might not desire evil as they did.' The mixed multitude's craving (v4) = the Corinthians' idolatry and fleshly appetite. The wilderness generation is the negative type; the church is warned not to repeat it."},
      {"type": "allusion", "target": "1 Cor 10:3", "note": "Paul calls the manna 'spiritual food' (v3) in the same context — the contrast between craving Egypt's food and eating the spiritual food from God mirrors the contrast between fleshly appetite and the Lord's Supper."}
    ],
    "9": [
      {"type": "quotation", "target": "John 6:31", "note": "The crowd quotes Ps 78:24 / Num 11:7-9 to Jesus: 'He gave them bread from heaven to eat.' Jesus responds: 'My Father gives you the true bread from heaven.' The manna description in Num 11:7-9 (white, taste of fresh oil, ground and boiled) is the backdrop for John 6's entire bread-of-life discourse."}
    ],
    "17": [
      {"type": "allusion", "target": "Acts 2:17", "note": "The Spirit resting on 70 elders (v17) is the OT partial fulfillment of Joel 2's promise, which Peter cites at Pentecost: 'I will pour out my Spirit on all flesh.' The 70-elder event was limited (selected leaders only); Pentecost extended the Spirit's resting to 'all flesh.' Moses's wish in v29 ('would that all were prophets') is answered at Pentecost."}
    ],
    "25": [
      {"type": "allusion", "target": "1 Cor 14:1", "note": "The elders prophesied when the Spirit rested on them. Paul's exhortation to 'desire spiritual gifts, especially that you may prophesy' (1 Cor 14:1) draws on the Spirit-and-prophecy connection established in Numbers 11. The 70 elders' Spirit-given prophecy is the OT foundation for NT pneumatic gift-expectation."}
    ],
    "29": [
      {"type": "allusion", "target": "Acts 2:17", "note": "Moses: 'Would that all YHWH's people were prophets, and that YHWH would put his Spirit on them!' This wish is the direct OT preparation for Joel 2:28-29 ('your sons and daughters shall prophesy'), which Peter quotes at Pentecost (Acts 2:17-18) as fulfilled. Moses's unfulfilled wish becomes the Pentecost proclamation: the Spirit is now poured on all flesh."}
    ],
    "34": [
      {"type": "allusion", "target": "1 Cor 10:6", "note": "The plague at Kibroth-hattaavah ('graves of craving') when people were struck down while eating: 'now these things took place as examples for us, that we might not desire evil as they did' (1 Cor 10:6). The grave-site named for their craving is Paul's exhibit A for fleshly desire leading to judgment."}
    ]
  },
  "12": {
    "3": [
      {"type": "allusion", "target": "Matt 11:29", "note": "Moses is described as 'very humble, more than all people who were on the face of the earth.' Jesus describes himself with the same quality: 'I am gentle and humble [tapeinos] in heart.' Moses's unparalleled humility is the OT's pre-eminent type of the humility of Christ — who 'humbled himself by becoming obedient to the point of death' (Phil 2:8)."}
    ],
    "7": [
      {"type": "allusion", "target": "Heb 3:5", "note": "YHWH's commendation of Moses — 'my servant Moses is faithful in all my house' — is quoted in Hebrews 3:5 to establish the Moses-Christ typological contrast: 'Moses was faithful in all God's house as a servant... but Christ is faithful over God's house as a son.' Num 12:7-8's distinction between Moses (servant, face-to-face speech) and other prophets (vision/dream) underpins Hebrews' argument for Christ's superiority."}
    ],
    "8": [
      {"type": "allusion", "target": "John 1:18", "note": "YHWH speaking to Moses 'mouth to mouth, clearly, and not in riddles, and he beholds the form of YHWH' — the most direct divine communication any human received. Yet John 1:18: 'No one has ever seen God; the only God, who is at the Father's side, he has made him known.' The face-to-face of Moses is surpassed by the Son who dwells in the Father's bosom. Moses saw the form; Christ is the form."}
    ],
    "13": [
      {"type": "allusion", "target": "Heb 7:25", "note": "Moses cries out: 'O God, please heal her — please!' — interceding for Miriam who had opposed him. This is a type of Christ's intercession for those who oppose him: 'he always lives to make intercession for them' (Heb 7:25). Moses's intercessory prayer for his accuser is the OT form of Jesus's prayer from the cross: 'Father, forgive them' (Luke 23:34)."}
    ],
    "15": [
      {"type": "allusion", "target": "Heb 13:12", "note": "Miriam is shut outside the camp for seven days while the congregation waits. Heb 13:12-13: 'Jesus also suffered outside the gate... let us go to him outside the camp and bear the reproach he endured.' The 'outside the camp' pattern — whether the leper, the sin-offering animal (Lev 4:12), or Miriam — consistently marks the place of reproach and exclusion where Christ suffered."}
    ]
  },
  "13": {
    "16": [
      {"type": "allusion", "target": "Heb 4:8", "note": "Moses renames Hoshea ('salvation') to Yehoshua ('YHWH saves'). The name Yehoshua (Joshua) is the Hebrew form of the Greek Iesous (Jesus). Heb 4:8: 'For if Joshua [same name as Jesus in Greek] had given them rest, God would not have spoken of another day later on.' The renaming here marks the moment the name 'YHWH saves' entered the narrative as the leader who would bring Israel into rest — pointing beyond Joshua to Jesus who gives the true Sabbath rest (Heb 4:9-11)."}
    ],
    "23": [
      {"type": "allusion", "target": "John 15:1", "note": "The spies cut a cluster of grapes so large it required two men to carry on a pole — the signature fruit of the promised land from the valley of Eshcol ('cluster'). Jesus: 'I am the true vine... my Father is the vinedresser' (John 15:1). The enormous cluster from Eshcol is the type of the abundant fruit of the true Vine; the promised land's fruit is the type of the life produced in Christ."}
    ],
    "30": [
      {"type": "allusion", "target": "Heb 11:6", "note": "Caleb silences the people: 'Let us go up at once and occupy it, for we are well able to overcome it.' Caleb's faith — seeing the same evidence as the 10 faithless spies but reaching the opposite conclusion — is the type of Heb 11:6: 'without faith it is impossible to please God, for whoever would draw near to God must believe that he exists and that he rewards those who seek him.' Joshua and Caleb are the faith-heroes of the spy narrative (Heb 3:17-19 cites the unbelief of the majority as the reason they fell)."}
    ],
    "32": [
      {"type": "allusion", "target": "Heb 3:18", "note": "The ten faithless spies: 'the land, through which we have gone to spy it out, is a land that devours its inhabitants.' Their unbelief — expressing impossibility at what God had promised — is the antitype of Heb 3:18-19: 'to whom did he swear that they would not enter his rest, but to those who were disobedient? So we see that they were unable to enter because of unbelief.' The faithless spies become Hebrews' primary example of the disobedience-unbelief link that forfeits rest."}
    ]
  }
}

def main():
    e = load_echo('numbers')
    merge_echo(e, ECHOES)
    save_echo('numbers', e)
    print('Numbers 11-13 echoes written.')

if __name__ == '__main__':
    main()
