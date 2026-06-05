"""
Echo layer — Matthew chapters 5–6 (Sermon on the Mount, part 1)
Output: data/echoes/matthew.json (adds ch5-6)

The Sermon on the Mount is a comprehensive new-Torah address with deep Sinai/Moses echoes,
Psalms beatitude patterns, Deuteronomic covenant structure, Isaiah prophetic-ethical tradition,
and OT citation/fulfillment throughout the six antitheses.
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
  "5": {
    "1": [
      {"type": "type", "target": "Exod 19:3", "note": "Moses went up to God on the mountain — Jesus ascending the mountain to teach the kingdom-Torah mirrors Moses ascending Sinai to receive the law; the new Moses typology established from the outset"}
    ],
    "3": [
      {"type": "allusion", "target": "Isa 61:1-2", "note": "Blessed are the poor in spirit — the anointed one brings good news to the poor (anawim) in Isaiah 61; the beatitude draws on the same Isaianic category of the spiritually humble who receive God's favor"},
      {"type": "allusion", "target": "Ps 37:11", "note": "The meek shall inherit the earth — Ps 37:11 provides the exact language of the third beatitude; Jesus lifts the Psalmic promise into the kingdom declaration"}
    ],
    "4": [
      {"type": "allusion", "target": "Isa 61:2-3", "note": "Blessed are those who mourn, for they shall be comforted — the Isaianic comfort of mourners (to comfort all who mourn) is the prophetic ground of this beatitude"}
    ],
    "6": [
      {"type": "allusion", "target": "Isa 55:1-2", "note": "Blessed are those who hunger and thirst for righteousness — the Isaianic invitation to the hungry and thirsty (come and eat, come and buy without cost) is the OT background for covenant satisfaction"}
    ],
    "8": [
      {"type": "allusion", "target": "Ps 24:3-4", "note": "Who shall ascend the hill of the LORD? He who has clean hands and a pure heart — the entry-psalm's requirement of inner purity (pure heart) maps directly onto the beatitude; pure-hearted are those qualified to see God"}
    ],
    "12": [
      {"type": "allusion", "target": "1 Kgs 18:4", "note": "So they persecuted the prophets before you — Elijah's flight from Jezebel and the 100 hidden prophets; the tradition of prophetic persecution that runs through Israel's history now extends to the disciples"}
    ],
    "14": [
      {"type": "allusion", "target": "Isa 42:6", "note": "You are the light of the world — the Servant is a light to the nations (Isa 42:6; 49:6); Jesus applies the Servant vocation collectively to the disciple community"},
      {"type": "allusion", "target": "Isa 60:3", "note": "Nations shall come to your light — the eschatological light of Zion that draws the nations; the community functions as the visible hill-city of the kingdom"}
    ],
    "17": [
      {"type": "allusion", "target": "Deut 4:2", "note": "I have not come to abolish but to fulfill — do not add to or take from the word I command (Deut 4:2); Jesus distinguishes his authoritative fulfillment-relation to Torah from abolition or mere addition"},
      {"type": "allusion", "target": "Ps 119:89", "note": "Not one jot or tittle shall pass from the law — the eternal establishment of God's word in heaven (Ps 119:89); Jesus affirms the immovable permanence of Torah even as he fulfills it"}
    ],
    "21": [
      {"type": "quote", "target": "Exod 20:13", "note": "You shall not murder — the sixth commandment of the Decalogue; the first antithesis begins with the murder prohibition and radicalizes it to anger and contempt"}
    ],
    "27": [
      {"type": "quote", "target": "Exod 20:14", "note": "You shall not commit adultery — the seventh commandment; Jesus's second antithesis radicalizes the adultery prohibition to lustful looking as inner adultery"}
    ],
    "31": [
      {"type": "quote", "target": "Deut 24:1-4", "note": "Whoever divorces his wife let him give her a certificate of divorce — the Mosaic divorce provision (get = certificate); Jesus tightens the Deuteronomic permission, recognizing only sexual immorality as grounds"}
    ],
    "33": [
      {"type": "allusion", "target": "Lev 19:12", "note": "You shall not swear falsely — the Levitical oath prohibition (swearing falsely by the divine name); Jesus abolishes the oath system entirely in favor of simple truthfulness"},
      {"type": "allusion", "target": "Num 30:2", "note": "Perform to the Lord what you have sworn — the Mosaic law on vow-fulfillment; the antithesis targets the system of oath-swearing that the law presupposed"}
    ],
    "38": [
      {"type": "quote", "target": "Exod 21:24", "note": "An eye for an eye and a tooth for a tooth — the lex talionis of Exod 21:24, Lev 24:20, Deut 19:21; originally a limit on disproportionate vengeance, Jesus replaces it with non-resistance"}
    ],
    "43": [
      {"type": "quote", "target": "Lev 19:18", "note": "You shall love your neighbor — the love-neighbor command of Lev 19:18; Jesus takes it beyond the community boundary (and adds: and hate your enemy, the popular extension he is correcting)"},
      {"type": "allusion", "target": "Prov 25:21-22", "note": "If your enemy is hungry give him bread — the proverbial tradition of good toward enemies; Jesus radicalizes toward universal enemy-love"}
    ],
    "45": [
      {"type": "allusion", "target": "Ps 19:4-6", "note": "He makes his sun rise on the evil and on the good — God's indiscriminate providential care (the sun going forth like a bridegroom) as the pattern for the community's indiscriminate love"}
    ],
    "48": [
      {"type": "allusion", "target": "Lev 19:2", "note": "You shall be holy as I the LORD your God am holy — the Holiness Code's imitatio Dei command; Jesus rephrases it as perfection (teleios), applying the divine-character standard to the new-covenant community"}
    ]
  },
  "6": {
    "6": [
      {"type": "allusion", "target": "Isa 26:20", "note": "Enter your room and shut your door — Isaiah's instruction to hide in the chamber during divine judgment; the inner room (tameion) prayer-space as the place of intimate, unseen communion with God"}
    ],
    "9": [
      {"type": "allusion", "target": "Ezek 36:23", "note": "Hallowed be your name — I will sanctify my great name; the LORD's name-sanctification was the prophetic vision of the eschatological vindication; the Lord's Prayer prays for the fulfillment of this prophetic hope"},
      {"type": "allusion", "target": "Dan 7:14", "note": "Your kingdom come — the Danielic kingdom given to the Son of Man; the prayer for kingdom-arrival echoes the vision of universal dominion"}
    ],
    "10": [
      {"type": "allusion", "target": "Ps 143:10", "note": "Your will be done on earth as in heaven — Teach me to do your will (Ps 143:10); the prayer aligns the earthly community with the already-perfect heavenly obedience"}
    ],
    "11": [
      {"type": "allusion", "target": "Prov 30:8", "note": "Give us this day our daily bread — feed me with the food that is needful for me (Prov 30:8); the wisdom tradition on dependence on God for daily provision"},
      {"type": "allusion", "target": "Exod 16:4", "note": "Daily bread — the manna wilderness provision (a day's portion each day); the Lord's Prayer embeds the Exodus-manna pattern into daily petition"}
    ],
    "12": [
      {"type": "allusion", "target": "Ps 32:1", "note": "Forgive us our debts as we forgive our debtors — the Psalmic declaration of the blessedness of forgiveness; debt/sin terminology from Aramaic (hoba = debt = sin)"}
    ],
    "13": [
      {"type": "allusion", "target": "Ps 141:4", "note": "Lead us not into temptation but deliver us from evil — do not let my heart incline to any evil thing (Ps 141:4); the petition for divine protection from moral deviation and the evil one"}
    ],
    "19": [
      {"type": "allusion", "target": "Prov 23:4-5", "note": "Do not lay up treasures on earth where moth and rust destroy — the wisdom warning against wealth that sprouts wings and flies away; Jesus intensifies the proverbial tradition into a kingdom-ethic"}
    ],
    "22": [
      {"type": "allusion", "target": "Prov 4:23", "note": "The lamp of the body is the eye — keep your heart with all vigilance, for from it flow the springs of life (Prov 4:23); the eye as the heart's orientation-indicator determines whether the body is filled with light or darkness"}
    ],
    "24": [
      {"type": "allusion", "target": "Deut 6:13-14", "note": "You cannot serve God and money — the Shema logic of exclusive covenant loyalty to YHWH alone; no other master alongside the LORD; Jesus applies the God-or-Baal exclusivity to God-or-Mammon"},
      {"type": "allusion", "target": "1 Kgs 18:21", "note": "How long will you go limping between two opinions? — Elijah's challenge at Carmel; the same either/or exclusivity Jesus applies to the kingdom vs. wealth allegiance"}
    ],
    "25": [
      {"type": "allusion", "target": "Ps 55:22", "note": "Do not be anxious about your life — cast your burden on the LORD and he will sustain you; the Psalmic anti-anxiety grounded in divine provision"},
      {"type": "allusion", "target": "1 Kgs 17:4-6", "note": "Consider the ravens — God fed Elijah through ravens at Cherith; the bird-provision miracle as the background for God's care for the anxious"}
    ],
    "33": [
      {"type": "allusion", "target": "Ps 37:4", "note": "Seek first the kingdom of God and his righteousness — delight yourself in the LORD and he will give you the desires of your heart; seeking God first as the path to receiving all else"}
    ]
  }
}

def main():
    existing = load_echo('matthew')
    merge_echo(existing, ECHOES)
    save_echo('matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
