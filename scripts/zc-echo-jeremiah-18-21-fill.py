"""
Echo fill — Jeremiah chapters 18–21
Run: python3 scripts/zc-echo-jeremiah-18-21-fill.py

Combined Phase 2 script exists but contains no echo entries for chs 18–21.

Key echo decisions:
- 18:6 (potter/clay) = Rom 9:20-21 direct citation
- 19:5-6 (Tophet/Ben-hinnom) = geographic origin of Gehenna in the Synoptics
- 20:9 (fire in my bones) = 1 Cor 9:16 (compelled to preach); Luke 24:32
- 20:10 (report him) = Matt 26:59 (false witnesses sought)
- 21:8 (way of life/death) = John 14:6; Matt 7:13-14
- 21:9 (surrender and live) = Matt 16:25 (lose life to find it)
"""

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

JER_ECHO_18_21 = {
  "18": {
    "6": [
      {"type": "allusion", "target": "Rom 9:20-21", "note": "Can I not deal with you as this potter deals with the clay, O house of Israel? — Paul quotes the potter-clay image from Jer 18:6 to ground divine sovereignty in election: who are you, O man, to answer back to God? Does not the potter have the right to make from the same lump one vessel for honored use and another for dishonorable use? The image justifies YHWH's free reshaping of Israel and the inclusion of Gentiles"}
    ],
    "7": [
      {"type": "allusion", "target": "Luke 15:7", "note": "If that nation turns from its evil I will relent concerning the disaster I intended for it — the conditional structure of divine judgment (repentance leads to relenting) is the theological ground for the parable of the prodigal son: there is more joy in heaven over one sinner who repents than over ninety-nine who need no repentance (Luke 15:7); the relenting God of Jer 18:7-8 is the running Father of Luke 15"}
    ],
    "18": [
      {"type": "allusion", "target": "Matt 26:4", "note": "Come, let us make plans against Jeremiah — the conspiracy of priests, sages, and prophets against the prophet who speaks YHWH's word; the pattern prefigures the chief priests and elders who plotted to seize Jesus by stealth and kill him (Matt 26:4); in both cases the religious establishment conspires to silence the prophetic voice that indicts them"}
    ],
    "20": [
      {"type": "allusion", "target": "Luke 23:34", "note": "Should good be paid back with evil? I stood before you and interceded for them, yet they have dug a pit for my life — Jeremiah&apos;s lament that his intercessory suffering is repaid with murderous conspiracy; Jesus on the cross intercedes for those crucifying him: Father, forgive them, for they do not know what they are doing; the pattern of the intercessor attacked by those he prays for reaches its climax at Calvary"}
    ]
  },
  "19": {
    "5": [
      {"type": "allusion", "target": "Mark 9:47-48", "note": "They built the high places of Baal to burn their sons in the fire in the valley of Ben-hinnom — child sacrifice at Tophet; the LXX transliteration geenna (Gehenna) derives directly from Ge-hinnom (valley of Hinnom); Jesus uses Gehenna twelve times as his primary image for eschatological judgment (Mark 9:47-48: where the worm does not die and the fire is not quenched); the geography of Israel&apos;s worst sin becomes the NT&apos;s vocabulary for divine judgment"},
      {"type": "allusion", "target": "Matt 5:22", "note": "The valley of Ben-hinnom where children were burned — the geographic origin of gehenna, which Jesus uses in the Sermon on the Mount (Matt 5:22: liable to the Gehenna of fire); the historical atrocity of Tophet names the eschatological reality Jesus describes"}
    ],
    "9": [
      {"type": "allusion", "target": "Luke 21:20-24", "note": "I will make them eat the flesh of their sons and daughters in the desperate siege — the covenant curse of siege-cannibalism (Deut 28:53-57) fulfilled in the Babylonian siege; Jesus&apos;s Olivet Discourse predicts its recurrence: when you see Jerusalem surrounded by armies know that its desolation has come; Luke 21:24 records its fulfillment in 70 CE"}
    ],
    "10": [
      {"type": "allusion", "target": "Luke 20:18", "note": "Break the flask in front of the men — the irreversible shattered-vessel judgment; Jesus combines Isa 8:14-15 and Ps 118:22 in the parable of the vineyard tenants: everyone who falls on that stone will be broken to pieces, and on whomever it falls it will crush him (Luke 20:18); both images convey irreversible divine judgment"}
    ]
  },
  "20": {
    "9": [
      {"type": "allusion", "target": "1 Cor 9:16", "note": "There is in my heart something like a burning fire shut up in my bones — the compulsion of the prophetic call; Paul describes the same constraint: woe to me if I do not preach the gospel (1 Cor 9:16); the inner compulsion that Jeremiah could not suppress is the apostolic vocation&apos;s defining feature — the word is not a choice but a necessity"},
      {"type": "allusion", "target": "Luke 24:32", "note": "A burning fire shut up in my bones — the disciples on the road to Emmaus: did not our hearts burn within us while he talked with us on the road and opened the Scriptures to us? The burning fire Jeremiah felt when YHWH&apos;s word overcame his resistance is the same fire the disciples felt when the risen Christ opened Scripture; the word&apos;s inner compulsion recurs in both testaments"}
    ],
    "10": [
      {"type": "allusion", "target": "Matt 26:59", "note": "I hear many people whispering: Report him — let us report him! All my trusted friends are watching for my stumbling — the institutional surveillance combined with intimate betrayal; the Sanhedrin&apos;s search for false testimony against Jesus (Matt 26:59: the chief priests and council sought false testimony that they might put him to death) follows the same pattern of conspiracy and betrayal Jeremiah experienced"},
      {"type": "allusion", "target": "Ps 41:9", "note": "All my trusted friends are watching for my stumbling — the intimate betrayal; Ps 41:9 (my close friend has lifted his heel against me) is cited by Jesus in John 13:18 as fulfilled in Judas; Jeremiah&apos;s lament is part of the righteous-sufferer pattern that culminates in the passion narrative"}
    ],
    "11": [
      {"type": "allusion", "target": "Rom 8:31", "note": "The LORD is with me like a mighty and terrible warrior; therefore my persecutors will stumble and not prevail — the confidence that divine presence makes opposition ultimately powerless; Paul&apos;s rhetorical question (if God is for us who can be against us?) is the NT form of Jeremiah&apos;s confession; the Lord-as-warrior presence is the foundation of both Jeremiah&apos;s and Paul&apos;s confidence under persecution"}
    ]
  },
  "21": {
    "5": [
      {"type": "allusion", "target": "Luke 19:43-44", "note": "I myself will fight against you with an outstretched hand and mighty arm — YHWH fighting against his own covenant city through Babylon; Jesus&apos;s lament over Jerusalem anticipates its 70 CE destruction: the days will come when your enemies encircle you (Luke 19:43-44), because you did not know the time of your visitation; the Roman siege recapitulates the Babylonian siege as YHWH&apos;s judgment"}
    ],
    "8": [
      {"type": "allusion", "target": "John 14:6", "note": "I am setting before you the way of life and the way of death — the two-ways formula recast in siege terms: surrender and live, resist and die; Jesus&apos;s claim (I am the way, the truth, and the life) is the Christological resolution of the two-ways motif: the way of life is now a person, not merely a moral choice"},
      {"type": "allusion", "target": "Matt 7:13-14", "note": "The way of life and the way of death — the Deuteronomic-Jeremianic two-ways tradition becomes the structural framework of Jesus&apos;s Sermon on the Mount: the narrow gate and hard way leads to life; the wide gate and easy way leads to destruction; Jesus formalizes the ancient prophetic two-ways teaching"}
    ],
    "9": [
      {"type": "allusion", "target": "Matt 16:25", "note": "Whoever goes out and surrenders to the Chaldeans who are besieging you will live — survival through surrender to the enemy (seen as treasonous by Jerusalem&apos;s defenders); the paradox recurs in Jesus&apos;s teaching: whoever wants to save his life will lose it, but whoever loses his life for my sake will find it (Matt 16:25); the Jeremianic call to surrender prefigures the cross-shaped logic of the gospel"}
    ],
    "12": [
      {"type": "allusion", "target": "Luke 4:18", "note": "Administer justice every morning; rescue from the hand of the oppressor those being robbed — the prophetic demand for justice as daily covenant practice directed at the house of David; Jesus&apos;s synagogue sermon (Luke 4:18: he has sent me to proclaim release to captives and to set at liberty the oppressed) stands in this tradition; the justice-demand of the Davidic house becomes the mission statement of David&apos;s greater Son"}
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHO_18_21)
    save_echo('jeremiah', existing)
    print('Jeremiah 18-21 echoes written.')

if __name__ == '__main__':
    main()
