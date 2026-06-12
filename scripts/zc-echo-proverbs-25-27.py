"""
Echo Commentary — Proverbs chapters 25–27
Run: python3 scripts/zc-echo-proverbs-25-27.py

Ch 25: Hezekiah collection — the concealed/revealed glory of God (v2) → 1 Cor 2:7-10;
    humility at the king's court (v6-7) → Luke 14:7-11; enemy-feeding / heap-coals
    (vv21-22, already absorbed from parallels as type:quote) — adding a complementary
    note on the new-covenant ethic transformation; self-control (v28) → Gal 5:22-23.
    Note: parallels entries for ch25:v21 and ch26:v11 already exist; merge_echo
    deduplicates by (type, target), so any new entries here must use different targets.
Ch 26: Fool discourse — dog returns to vomit (v11, already in parallels); the wise-
    in-own-eyes folly (v12) → Luke 18:9; quarreling-without-whisperer (v20) → Jas 3:5;
    the pit-digger who falls in (v27) → Gal 6:7-8.
Ch 27: Do not boast of tomorrow (v1) → Jas 4:13-16; iron sharpening iron (v17)
    → Heb 10:24-25; heart-mirror (v19) → 2 Cor 3:18; Sheol never satisfied (v20)
    → Rev 20:14; faithful wounds of a friend (v6) → John 15:13.
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

PROVERBS_ECHOES = {
  "25": {
    "2": [
      {"type": "allusion", "target": "1 Cor 2:7",
       "note": "The glory of God in concealment — 'it is the glory of God to conceal things' — is the OT background for Paul's 'secret and hidden wisdom of God, which God decreed before the ages for our glory.' The hiddenness that is God's glory is the very pattern that Paul applies to the cross: a mystery concealed in the depths of God and now revealed in Christ as the wisdom the rulers of this age could not discern."},
      {"type": "theme", "target": "Rom 11:33",
       "note": "Paul's doxology — 'how unsearchable are his judgments and how inscrutable his ways!' — stands in the tradition of Prov 25:2's concealment-glory. The things kings search out (v2b) and the things only God knows (v2a) define the epistemic boundary that Paul celebrates when he concludes his argument about divine election and mercy: God's concealment is not an obstacle but the very form of his majesty."}
    ],
    "6": [
      {"type": "type", "target": "Luke 14:8",
       "note": "The wisdom counsel not to exalt oneself in the king's presence and to take the lower position rather than be humbled publicly is the direct background for Jesus' parable of the wedding seat: 'when you are invited by someone to a wedding feast, do not sit down in a place of honor' (Luke 14:8). Jesus converts the courtly wisdom of Proverbs into a parable about the kingdom, applying the same logic of voluntary humility that leads to genuine exaltation."}
    ],
    "7": [
      {"type": "allusion", "target": "Luke 14:10",
       "note": "The better outcome of being told 'come up here' rather than being put lower in the presence of the noble reverses the expected social dynamic — and Jesus quotes this exact pattern: 'when you are invited, go and sit in the lowest place, so that when your host comes he may say to you, Friend, move up higher' (Luke 14:10). Proverbs 25:7 is the wisdom text that Jesus takes up and re-frames as a kingdom principle about eschatological reversal."}
    ],
    "11": [
      {"type": "allusion", "target": "Col 4:6",
       "note": "The gold-apple-in-silver-setting image for the fitly-spoken word is the wisdom tradition's highest praise for speech; Paul's 'let your speech always be gracious, seasoned with salt, so that you may know how you ought to answer each person' (Col 4:6) stands in the same tradition. The carefully timed, precisely calibrated word that Proverbs commends becomes in the NT the gracious speech formed by the indwelling of Christ's word (Col 3:16)."}
    ],
    "21": [
      {"type": "theme", "target": "Matt 5:44",
       "note": "The enemy-feeding / heap-burning-coals instruction (vv21-22) is absorbed into the NT as a specific quotation (Rom 12:20), but it also belongs to the Sermon on the Mount's love-of-enemy teaching: 'love your enemies and pray for those who persecute you' (Matt 5:44). Where Proverbs motivates the action by its shaming-effect on the enemy, Jesus grounds it in the Father's impartial care for all — a deeper motivational transformation of the same ethical command."}
    ],
    "28": [
      {"type": "allusion", "target": "Gal 5:23",
       "note": "The city broken into and left without walls as a metaphor for the man without self-control describes precisely the vulnerability that Paul addresses with self-control (<em>enkrateia</em>) as a fruit of the Spirit (Gal 5:23). The undefended city of Proverbs 25:28 is the life lived without the Spirit's self-control; the Spirit-formed fruit rebuilds the walls from within that no external law-keeping could maintain."}
    ]
  },
  "26": {
    "12": [
      {"type": "allusion", "target": "Luke 18:9",
       "note": "The woe pronounced on 'a man wise in his own eyes' — for whom there is more hope for a fool — is the wisdom tradition's verdict that Jesus dramatizes in the Pharisee-and-tax-collector parable: the one who was 'wise in his own eyes' (trusting in himself that he was righteous) left unjustified, while the fool who saw his own need was justified (Luke 18:14). Proverbs 26:12 is the wisdom aphorism; Luke 18 is its narrative illustration."},
      {"type": "allusion", "target": "Rom 12:16",
       "note": "Paul's 'do not be wise in your own sight' (Rom 12:16) is the NT echo of Prov 26:12's warning in a communal context — the body of Christ is the community where self-wisdom is replaced by mutual deference and humility. The woe of Proverbs becomes the apostolic command; both stem from the same diagnosis that self-knowledge without God is the root form of foolishness."}
    ],
    "20": [
      {"type": "allusion", "target": "Jas 3:5",
       "note": "The observation that 'where there is no whisperer, quarreling ceases' identifies the tongue as the fuel that keeps conflict alive — the exact point James develops with the ship's rudder and the forest fire: 'how great a forest is set ablaze by such a small fire! And the tongue is a fire' (Jas 3:5-6). The principle of Prov 26:20 (remove the fuel-source, fire goes out) is the same as James' destructive-tongue teaching applied to the church community."}
    ],
    "27": [
      {"type": "allusion", "target": "Gal 6:7",
       "note": "The trap-setter falling into his own pit and the stone-roller crushed under his own stone are concrete instances of the moral law Paul formulates in Gal 6:7: 'do not be deceived: God is not mocked, for whatever one sows, that will he also reap.' The principle of Proverbs — that harm intended for another returns to the sender — is for Paul not merely karmic justice but the expression of divine government: God will not be mocked by those who scheme against his purposes."}
    ]
  },
  "27": {
    "1": [
      {"type": "allusion", "target": "Jas 4:13",
       "note": "The prohibition against boasting about tomorrow — 'do not boast about tomorrow, for you do not know what a day may bring' — is directly echoed in James 4:13-16: 'come now, you who say, Today or tomorrow we will go into such and such a town&hellip;yet you do not know what tomorrow will bring.' James sharpens the Proverbs observation into a specific rebuke of commercial presumption and adds the christological frame: 'if the Lord wills, we will live and do this or that' (v15)."}
    ],
    "5": [
      {"type": "theme", "target": "John 16:8",
       "note": "The claim that 'open rebuke is better than hidden love' identifies the courageous confrontation that true love requires. Jesus' promise of the Paraclete who will 'convict the world concerning sin and righteousness and judgment' (John 16:8) is the supreme instance of the rebuke that genuine love performs: the Spirit's convicting work is the loving rebuke that opens the way to repentance and healing."}
    ],
    "6": [
      {"type": "allusion", "target": "John 15:13",
       "note": "The 'faithful are the wounds of a friend' — the painful truthfulness of genuine loyalty — finds its ultimate expression in Christ: 'greater love has no one than this, that someone lay down his life for his friends' (John 15:13). The friend-wound of Proverbs 27:6 is the costly honesty of love; Christ's cross-wound is the ultimate costly act of loyal love — wounds that deal the sting of death so that the friends receive life."}
    ],
    "17": [
      {"type": "allusion", "target": "Heb 10:24",
       "note": "Iron sharpening iron — the mutual formation that happens when one person encounters another — is the principle behind Heb 10:24-25's call to 'stir up one another to love and good works, not neglecting to meet together.' The assembly of believers is the community where iron-on-iron sharpening takes place: the mutual encouragement and provocation to love is the communal practice of Proverbs' sharpening wisdom, made urgent by the approaching Day."}
    ],
    "19": [
      {"type": "allusion", "target": "2 Cor 3:18",
       "note": "As water mirrors the face, so the human heart mirrors the person — and by extension, the community mirrors the One they behold. Paul's transformation theology in 2 Cor 3:18 uses the mirror metaphor: 'we all, with unveiled face, beholding the glory of the Lord, are being transformed into the same image.' The heart-mirrors-what-it-sees principle of Prov 27:19 becomes in Paul the mechanism of sanctification: beholding Christ transforms the beholder into Christ's likeness."}
    ],
    "20": [
      {"type": "type", "target": "Rev 20:14",
       "note": "Sheol and Abaddon, which are never satisfied and whose appetite is bottomless, are the OT characterization of death's insatiability — the type that Rev 20:14 permanently resolves: 'then Death and Hades were thrown into the lake of fire.' The never-satisfied Sheol of Proverbs 27:20 is the chaotic power that Christ defeats and permanently confines. Rev 1:18 makes the claim explicit: 'I have the keys of Death and Hades.'"},
      {"type": "theme", "target": "Eccl 1:8",
       "note": "The insatiability of Sheol/Abaddon and the insatiability of human eyes in Prov 27:20b form the same pair that Ecclesiastes 1:8 catalogs: 'the eye is not satisfied with seeing, nor the ear with hearing.' Both texts probe the structural restlessness of creaturely desire that Augustine famously captured: 'our heart is restless until it rests in you' — a restlessness that is resolved only when the eyes behold what does satisfy (Rev 22:4: 'they will see his face')."}
    ]
  }
}

def main():
    existing = load_echo('proverbs')
    merge_echo(existing, PROVERBS_ECHOES)
    save_echo('proverbs', existing)
    total = sum(len(vv) for vv in PROVERBS_ECHOES.values())
    entries = sum(len(e) for ch in PROVERBS_ECHOES.values() for e in ch.values())
    print(f'Proverbs 25-27 echoes: {total} verses, {entries} entries written.')

if __name__ == '__main__':
    main()
