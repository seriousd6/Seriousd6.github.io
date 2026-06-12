"""
MKT Christ Commentary — 1 Samuel chapters 17–18
Run: python3 scripts/zc-christ-1samuel-17-18.py

Ch17: David vs. Goliath — the single champion who fights on behalf of the people;
      the ḥerpāh removed; the battle belongs to YHWH; enemy defeated by own weapon
Ch18: Jonathan's soul-union with David — the covenant bond and royal self-divestiture;
      Saul's envy pattern; YHWH's presence with David but departed from Saul
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
  "17": {
    "26": "<p>David's question about the reward for killing Goliath contains the theologically precise word: <em>ûsār ḥerpāh mēʿal yiśrāʾēl</em> — 'and removes the reproach (<em>ḥerpāh</em>) from upon Israel.' The noun <em>ḥerpāh</em> (reproach, shame, disgrace) is the OT term for the social and covenantal humiliation that comes when YHWH's people are defeated before their enemies — it implies that YHWH himself has been shamed by his people's humiliation. The champion who removes <em>ḥerpāh</em> restores not only Israel's honor but YHWH's name among the nations. Psalm 22:6 places <em>ḥerpāh</em> at the center of the Passion: 'I am a worm and not a man, scorned (<em>ḥerpat</em>) by mankind and despised by the people' — the ultimate champion who removes Israel's reproach first bears the world's reproach himself. Hebrews 13:13 calls believers to 'go to him outside the camp and bear the reproach (<em>oneidismon</em>, the LXX term for <em>ḥerpāh</em>) he endured.' The Davidic pattern — champion accepts the task of reproach-removal by engaging the enemy alone — is fulfilled when the Son of Man takes the world's shame upon himself on the cross so that those he represents go free of it.</p>",
    "45": "<p>David's counter-challenge to Goliath frames the combat as a contest between weapons and name: <em>ʾānoḵî bāʾ ʾēlêḵā bəšēm YHWH ṣəḇāʾôt</em> — 'I am coming to you in the name of YHWH of armies.' Goliath comes with sword, spear, and javelin — the full apparatus of human military power. David comes with the divine name as his only weapon. This is not merely rhetorical: in OT thought, the divine name is the effective presence of YHWH — to invoke it in battle is to invoke YHWH as the actual combatant. The NT translates this directly into spiritual warfare: 2 Cor 10:4 ('the weapons of our warfare are not of the flesh but have divine power'); Eph 6:17 ('the sword of the Spirit, which is the word of God'); Phil 2:9-10 ('the name that is above every name, at the name of Jesus every knee shall bow'). The Davidic combat pattern — the name of YHWH against the weapons of the flesh — is fulfilled in Christ, who enters the cosmic confrontation with sin and death not by force of arms but by the power of the divine name he bears as the Son (John 17:11: 'keep them in your name, which you have given me').</p>",
    "51": "<p>The decisive act of Goliath's defeat: David has no sword, so he takes Goliath's own sword and cuts off the giant's head with it. The enemy is destroyed by his own weapon — the principle that Paul will articulate as the central logic of the atonement: 'through death he might destroy the one who has the power of death' (Heb 2:14). Death defeats death; the enemy's own weapon is turned against him. The same principle governs Paul's argument in 1 Cor 15:26 ('the last enemy to be destroyed is death') and Col 2:14-15 ('he disarmed the rulers and authorities and put them to open shame, triumphing over them in him'). Just as David descends into the valley defenseless except for the name of YHWH, defeats the champion in single combat, and uses the enemy's own sword to complete the victory — so Christ descends into human mortality, takes the full weight of death upon himself, and rises from it having destroyed the power of the one who wielded it. The decapitation of Goliath with his own sword is the most precise narrative type of the cross in the David story.</p>"
  },
  "18": {
    "1": "<p>Jonathan's soul-union with David: <em>wənepeš yôhônātān niqšərāh bənepeš dāwiḏ wayyeʾĕhāḇēhû yôhônātān kənapšô</em> — 'the soul (<em>nepeš</em>) of Jonathan was bound (<em>qāšar</em>) to the soul of David and Jonathan loved him as his own soul.' The verb <em>qāšar</em> (to bind, tie, knot — used for binding a scarlet thread in Josh 2:18, binding the phylacteries in Deut 6:8) indicates a permanent bond of covenant attachment. The mutual self-identification — loving another 'as his own soul' — is the template for the great commandment: love your neighbor as yourself (<em>kāmôḵā</em>, Lev 19:18). But the NT extends this into the mystical union of the believer with Christ: 1 Cor 6:17 ('he who is joined to the Lord becomes one spirit with him'); John 15:5 ('I am the vine; you are the branches'). Jonathan's soul-binding to David is the OT narrative embodiment of the union that Christ will describe as indwelling — the believer's <em>nepeš</em> bound to the anointed king's by covenant love, not legal obligation.</p>",
    "4": "<p>Jonathan's voluntary self-divestiture is one of the most theologically significant acts in the Samuel narrative: he removes his robe (<em>mᵉʿîl</em>), his armor, his sword, his bow, and his belt — the entire apparatus of his princeship — and gives them to David. This is not merely a gift of friendship but a formal act of covenant submission: Jonathan is the crown prince, Saul's heir, the one whose position David will eventually occupy. His giving of the royal garments to David is a voluntary surrender of claim — he recognizes and affirms David's election over his own birthright. This is the precise OT narrative type of Phil 2:6-7: 'though he was in the form of God, he did not count equality with God a thing to be grasped, but emptied himself, taking the form of a servant.' Jonathan empties himself of royal prerogative in favor of the anointed; the Son empties himself of divine glory in taking on human form. The typological flow also points in the other direction: as Jonathan voluntarily cedes the kingdom to David, so every believer who acknowledges Christ's lordship enacts a Jonathanesque divestiture — surrendering the claim to self-rule in favor of the true king.</p>",
    "12": "<p>The theological pivot of chapter 18: <em>wayhî YHWH ʿim dāwiḏ ûmēʿim šāʾûl sār</em> — 'YHWH was with David but had departed (<em>sār</em>, turned away/removed himself) from Saul.' The transfer of divine presence is the defining structural reality of the rest of the Samuel narrative: everything that follows — David's military successes, Saul's paranoid deterioration, the Spirit's absence from Saul and his resort to the witch of En-dor — flows from this theological reality. YHWH's presence is not automatic or permanent but covenantally conditioned. The NT theology of the Spirit's indwelling makes this conditional permanence explicit: 'anyone who does not have the Spirit of Christ does not belong to him' (Rom 8:9); 'do not grieve the Holy Spirit' (Eph 4:30). The Saul/David contrast maps the two conditions — the Spirit-abandoned king who deteriorates into fear, envy, and violence vs. the Spirit-accompanied shepherd-king whose presence brings blessing to everything around him. Christ reverses the Saul trajectory permanently: he promises the Spirit who 'will be with you forever' (John 14:16) — the divine presence that is not conditional on individual performance but secured by the new covenant.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1samuel')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1samuel', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1samuel mkt-christ: wrote {count} verses across ch 17-18')

if __name__ == '__main__':
    main()
