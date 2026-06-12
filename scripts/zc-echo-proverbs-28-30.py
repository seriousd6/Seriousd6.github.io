"""
MKT Echo Layer — Proverbs chapters 28–30
Run: python3 scripts/zc-echo-proverbs-28-30.py

Ch28: Confess/forsake sins → find mercy (28:13) — 1 John 1:9;
      trust in LORD vs greed (28:25) — Matt 6:33
Ch29: King judges poor faithfully → eternal throne (29:14) — Luke 1:32-33;
      no prophetic vision (29:18) — John 1:14;
      pride humbled / humble honored (29:23) — Luke 14:11;
      fear of man vs trust in LORD (29:25) — Matt 10:28
Ch30: Agur's question about the divine name and his Son (30:4) — John 3:13; Col 1:16;
      every word of God proves true (30:5) — John 17:17;
      daily bread petition (30:8-9) — Matt 6:11
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

ECHOES = {
  "28": {
    "13": [
      {"type": "allusion", "target": "1 John 1:9", "note": "Whoever conceals his sins will not prosper, but whoever confesses and forsakes them will find mercy — the two-movement pattern of genuine repentance (confession + forsaking) that Proverbs identifies as the path to mercy. John's formulation is the NT form: 'if we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness' (1 John 1:9). The mercy promised is now grounded in Christ's atoning work rather than in personal moral reform alone."},
      {"type": "theme", "target": "Luke 15:20", "note": "The prodigal who 'comes to himself' and returns to confess to his father is the parabolic enactment of this proverb: the concealment and self-justification that followed the departure are reversed in the confession ('Father, I have sinned'). The father's response — running, embracing, restoring — is the mercy Proverbs promises, now rendered in narrative by Christ."}
    ],
    "14": [
      {"type": "theme", "target": "Heb 4:1", "note": "Happy is the one who fears the LORD continually, but whoever hardens his heart will fall into calamity — the 'hardening' (qasheh lev) that Proverbs associates with calamity is the exact theme Hebrews develops: 'Today, if you hear his voice, do not harden your hearts' (Heb 4:7, citing Ps 95:7). The persistent fear of the LORD and the persistent soft heart are, in both texts, the conditions of continued blessing."}
    ],
    "25": [
      {"type": "allusion", "target": "Matt 6:33", "note": "A greedy person stirs up strife, but whoever trusts in the LORD will prosper — the contrast between greedy grasping and trusting God's provision is the Sermon on the Mount's central economic teaching: 'seek first the kingdom of God and his righteousness, and all these things will be added to you' (Matt 6:33). Trust in the LORD is the alternative to the anxiety-driven accumulation that the proverb identifies as conflict-producing."}
    ],
    "27": [
      {"type": "allusion", "target": "Luke 14:13-14", "note": "Whoever gives to the poor will not lack, but whoever hides his eyes from them will receive many curses — the promise to the giver and the warning to the one who averts his eyes. Christ's corresponding teaching: 'when you give a feast, invite the poor, the crippled, the lame, the blind, and you will be blessed, because they cannot repay you. For you will be repaid at the resurrection of the just' (Luke 14:13-14). The repayment Proverbs implies is made explicit and eschatological by Christ."}
    ]
  },
  "29": {
    "7": [
      {"type": "theme", "target": "Matt 25:45", "note": "The righteous man considers the cause of the poor; the wicked man does not care to understand it — the distinction between those who attend to the poor's cause and those who do not is the criterion of the sheep-and-goats judgment (Matt 25:31-46). The wicked king's failure in Proverbs 29:7 is the 'I did not care to understand it' that becomes 'I never knew you' in Matthew 25."}
    ],
    "14": [
      {"type": "type", "target": "Luke 1:32-33", "note": "A king who judges the poor with faithfulness — his throne will be established forever — the royal ideal of perpetual reign grounded in justice for the poor. The Magnificat places Christ on exactly this trajectory: 'he will be great and will be called the Son of the Most High. And the Lord God will give to him the throne of his father David, and he will reign over the house of Jacob forever' (Luke 1:32-33). Christ is the king whose throne is established forever because he is the one who most completely judges with faithfulness toward the poor (Luke 4:18)."},
      {"type": "allusion", "target": "Ps 72:4", "note": "Psalm 72:4 articulates the same royal ideal: 'May he defend the cause of the poor of the people, give deliverance to the children of the needy.' The psalm's messianic king is the template both Proverbs and Luke draw on; Christ is the fulfillment."}
    ],
    "18": [
      {"type": "allusion", "target": "John 1:14", "note": "Where there is no prophetic vision (chazon), the people are unrestrained — vision here is the prophetic word that orders communal life. The incarnation is the definitive restoration of prophetic vision: 'the Word became flesh and dwelt among us, and we have seen his glory' (John 1:14). The seeing that John announces ('we have seen') is the recovery of the chazon-vision that Proverbs identifies as necessary for ordered life — now embodied in a person rather than transmitted in oracles."},
      {"type": "theme", "target": "Heb 1:1-2", "note": "The fragmentation of prophetic speech ('at many times and in many ways') described in Hebrews 1:1 is the condition Proverbs 29:18 laments; the 'in these last days he has spoken to us by his Son' (Heb 1:2) is the restoration. Christ is the unified prophetic vision that prevents the unrestrained scattering of the people."}
    ],
    "23": [
      {"type": "allusion", "target": "Luke 14:11", "note": "A man's pride will bring him low, but the one who is humble in spirit will obtain honor — one of Proverbs' most repeated themes (cf. Prov 16:18, 18:12). Christ cites this as a governing principle of the kingdom: 'everyone who exalts himself will be humbled, and everyone who humbles himself will be exalted' (Luke 14:11, 18:14). The proverb is the observation; Christ's declaration is the eschatological guarantee."},
      {"type": "allusion", "target": "Phil 2:8-9", "note": "The humiliation-to-exaltation pattern of Proverbs 29:23 is the structural logic of the Philippians hymn: Christ 'humbled himself by becoming obedient to the point of death... therefore God has highly exalted him' (Phil 2:8-9). The one who was brought lowest is the one most highly honored — the proverb's principle embodied at maximum scale."}
    ],
    "25": [
      {"type": "allusion", "target": "Matt 10:28", "note": "The fear of man lays a snare, but whoever trusts in the LORD is kept safe — Christ's commission addresses exactly this fear: 'do not fear those who kill the body but cannot kill the soul. Rather fear him who can destroy both soul and body in hell' (Matt 10:28). The snare of human fear is dissolved by proper fear of God — the reorientation of fear that both texts prescribe, now grounded by Christ in the Father's protective care ('not one of them falls to the ground apart from your Father,' Matt 10:29)."},
      {"type": "theme", "target": "1 Pet 3:14", "note": "Peter's instruction to those facing persecution — 'do not fear what they fear, and do not be troubled, but in your hearts honor Christ the Lord as holy' (1 Pet 3:14-15) — is the NT's pastoral application of this proverb. The snare of human fear is countered by the specific orientation of the heart toward Christ."}
    ]
  },
  "30": {
    "4": [
      {"type": "allusion", "target": "John 3:13", "note": "Who has ascended to heaven and come back down? Who has gathered the wind in his fists? Who has wrapped up the waters in a garment? What is his name, and what is his son's name? Surely you know! — Agur's rhetorical questions about the transcendent God, culminating in the question about the divine Son's name, form one of the OT's most remarkable anticipatory passages. Christ answers Agur's question directly: 'No one has ascended into heaven except he who descended from heaven, the Son of Man' (John 3:13). The name Agur could not supply, Jesus provides."},
      {"type": "allusion", "target": "Col 1:16", "note": "Who has gathered the wind in his fists? Who has wrapped up the waters in a garment? — the questions about mastery of wind and waters point to the creator of all things. Colossians identifies Christ as the one through whom and for whom all things were created, and in whom 'all things hold together' (Col 1:16-17). The name-question Agur poses is answered: it is Jesus Christ."},
      {"type": "allusion", "target": "John 1:18", "note": "What is his son's name? — the question about the Son who shares the divine name anticipates the NT's revelation: 'the only begotten God, who is at the Father's side, he has made him known' (John 1:18). Agur's rhetorical 'surely you know' — implying no one does — is the OT's confession of this very hiddenness that the incarnation resolves."}
    ],
    "5": [
      {"type": "allusion", "target": "John 17:17", "note": "Every word of God proves true; he is a shield to those who take refuge in him — the reliability of the divine word is the premise of Christ's prayer: 'Sanctify them in the truth; your word is truth' (John 17:17). The shielding function Proverbs assigns to every true word of God is concentrated in Christ, who is himself the Word (John 1:1)."},
      {"type": "theme", "target": "Heb 4:12", "note": "Every word of God proves true — the reliability of the divine word is the premise of Hebrews: 'the word of God is living and active, sharper than any two-edged sword... discerning the thoughts and intentions of the heart' (Heb 4:12). The refinement Proverbs describes (every word tried, like silver refined) is the active, penetrating quality Hebrews attributes to the word."}
    ],
    "8": [
      {"type": "allusion", "target": "Matt 6:11", "note": "Give me neither poverty nor riches — feed me with just what I need — the prayer for the measured daily portion is the nearest OT parallel to the Lord's Prayer's 'give us this day our daily bread' (Matt 6:11). Agur's request captures the theological logic of the petition: not accumulation, not anxiety — the portion appointed for today, from the hand of the Father who knows what we need."}
    ],
    "9": [
      {"type": "theme", "target": "Luke 12:15", "note": "Lest I be full and deny you, saying 'Who is the LORD?' — the spiritual danger of abundance: prosperity breeding forgetfulness of God. Christ's warning: 'one's life does not consist in the abundance of his possessions' (Luke 12:15), followed by the parable of the rich fool whose abundance consumed his attention until he forgot the God before whom he would stand that very night (Luke 12:20)."}
    ]
  }
}

def main():
    e = load_echo('proverbs')
    merge_echo(e, ECHOES)
    save_echo('proverbs', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'proverbs echo: wrote entries for {count} verses in ch 28-30')

if __name__ == '__main__':
    main()
