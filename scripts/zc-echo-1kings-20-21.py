"""
Echo Layer — 1 Kings chapters 20–21
Run: python3 scripts/zc-echo-1kings-20-21.py

Key echo connections:
- 20:13 — 'By this you shall know that I am YHWH' → Ezek 6:7 and throughout Ezekiel
- 20:28 — 'YHWH is God of the hills but not the valleys' → Matt 28:18 (universal lordship)
- 20:35-43 — Prophet's self-condemning parable → Nathan/David pattern (2 Sam 12); Matt 21:40-41
- 20:42 — ḥerem violation → 1 Sam 15:9 (Saul/Agag parallel); disobedience forfeiting the covenant
- 21:3 — Naboth: 'YHWH forbid that I should give you the inheritance of my fathers' → Lev 25:23
- 21:10-13 — Two false witnesses, Naboth stoned → Mark 14:57-58 (false witnesses at Jesus' trial)
- 21:17-19 — Elijah confronts Ahab → 2 Sam 12:7 Nathan pattern; exact-recompense prophecy fulfilled in 22:38
- 21:20 — 'You have sold yourself to do evil' → Rom 7:14 (sold under sin)
- 21:25-26 — Jezebel inciting Ahab → Rev 2:20 (Jezebel in Thyatira seducing God's servants)
- 21:27-29 — Ahab's repentance and YHWH's relenting → Jon 3:10; 2 Pet 3:9
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

KINGS_ECHOES = {
  "20": {
    "13": [
      {
        "type": "theme",
        "target": "Ezek 6:7",
        "note": "A prophet approaches Ahab with the word: &ldquo;Thus says the LORD: Have you seen all this great multitude? Behold, I will give it into your hand this day, and you shall know that I am the LORD.&rdquo; The recognition formula <em>wəyādaʿtā kî ʾănî yhwh</em> (&ldquo;you shall know that I am YHWH&rdquo;) appears here as a war oracle in the northern kingdom, but this exact phrase drives the entire prophetic program of Ezekiel, where it occurs over sixty times. The formula reaches its NT fulfillment in the universal declaration that will accompany Christ&rsquo;s return, when &ldquo;every knee will bow and every tongue confess&rdquo; (Phil 2:10-11) — the knowledge of YHWH that Israel repeatedly refused to gain through covenant will be imposed universally in the last day."
      }
    ],
    "28": [
      {
        "type": "theme",
        "target": "Matt 28:18",
        "note": "The Arameans theorize that YHWH &ldquo;is a god of the hills, and not a god of the valleys&rdquo; — they lost the hill-country battle because of divine geography, not divine supremacy. So YHWH sends another prophet: &ldquo;Because the Syrians have said YHWH is a god of the hills but not of the valleys, I will give all this great multitude into your hand, and you shall know that I am YHWH.&rdquo; The battle that follows is to correct a pagan theology of limited deity. Jesus&rsquo; Great Commission opens with the demolition of the same error: &ldquo;All authority in heaven and on earth has been given to me&rdquo; (Matt 28:18) — not some; not in particular domains. The pagan instinct to confine divine sovereignty to a sphere is always refuted by the God of both hills and valleys."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "2 Sam 12:7",
        "note": "By command of YHWH a prophet disguises himself as a wounded soldier and tells Ahab a story: he let a prisoner escape who had been committed to his care, and Ahab pronounces the sentence — &ldquo;So shall your judgment be.&rdquo; The prophet then removes his disguise and announces that the prisoner was Ben-hadad, whom Ahab was supposed to destroy. The technique is identical to Nathan&rsquo;s parable of the stolen ewe lamb (2 Sam 12:1-7): the king is drawn into pronouncing judgment on his own conduct without realizing it. Jesus uses the same technique in the parable of the vineyard tenants (Matt 21:33-41), where his hearers pronounce judgment on the evil tenants before recognizing themselves in the story. The prophetic parable that lures the powerful into self-condemnation is a recurring instrument of divine judgment."
      }
    ],
    "42": [
      {
        "type": "allusion",
        "target": "1 Sam 15:9",
        "note": "&ldquo;Because you let go out of your hand the man whom I had devoted to destruction (<em>ʾîš ḥormî</em>), therefore your life shall be for his life.&rdquo; Ahab&rsquo;s sparing of Ben-hadad is the exact sin Saul committed with Agag — both were commanded to execute the <em>ḥerem</em> (the ban, devotion to destruction) and both spared the enemy king from political calculation. Both pronouncements become dynasty-ending judgments (1 Sam 15:23; cf. 1 Kgs 21:21-22). The pattern establishes that the failure to enact YHWH&rsquo;s judgment on those he designates, from whatever motive, is itself covenantal rebellion. The <em>ḥerem</em> principle — that certain enemies of YHWH&rsquo;s people are given over to total destruction as a form of holy war — will be taken up eschatologically in Revelation&rsquo;s language of divine wrath poured out without mercy on those devoted to destruction."
      }
    ]
  },
  "21": {
    "3": [
      {
        "type": "allusion",
        "target": "Lev 25:23",
        "note": "Naboth refuses Ahab with an oath: &ldquo;YHWH forbid that I should give you the inheritance of my fathers (<em>naḥălat ʾăbôtāy</em>).&rdquo; This is not stubbornness but covenantal theology: Leviticus 25:23 declares that the land cannot be permanently sold because &ldquo;the land is mine; for you are strangers and sojourners with me.&rdquo; Family land is held in trust from YHWH as part of the tribal inheritance, and its alienation would violate the jubilee principle. Naboth&rsquo;s refusal is an act of faithfulness to Torah; it is precisely his righteousness that makes him a target. The NT picks up this theology in the language of inheritance (<em>klēronomia</em>) — the redeemed share in an inheritance that cannot be seized or sold (1 Pet 1:4)."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Mark 14:57",
        "note": "Jezebel instructs: &ldquo;Set two worthless men (<em>bənê bəliyaʿal</em>) opposite him and let them bring a charge against him, saying, &ldquo;You have cursed God and the king.&rdquo;&rdquo; The two-witness requirement of Deuteronomy 17:6 is formally observed while being deliberately subverted — the witnesses are hired false witnesses. Naboth is judicially murdered under the appearance of legal process. The same pattern appears at Jesus&rsquo; trial before the Sanhedrin: &ldquo;Many bore false witness against him, but their testimony did not agree&rdquo; (Mark 14:57-59; Matt 26:59-61). The righteous man condemned by a conspiracy of false testimony under a show of legal procedure is a recurrent pattern in Israel&rsquo;s history that reaches its climax in the trial of Christ."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "2 Sam 12:7",
        "note": "After Naboth&rsquo;s murder and Ahab&rsquo;s seizure of the vineyard, YHWH sends Elijah with a direct confrontation: &ldquo;Arise, go down to meet Ahab king of Israel... and say to him, &lsquo;Have you killed and also taken possession?&rsquo;&rdquo; The terse double accusation — murder followed by seizure — exposes the logic of royal impunity. Elijah&rsquo;s mission mirrors Nathan&rsquo;s confrontation of David (2 Sam 12:1-15): both prophets are sent directly after a king uses political power to take what he desires at the cost of a subject&rsquo;s life. The pattern of the prophet confronting the king who abuses his power is the OT version of speaking truth to power — a role fulfilled finally by John the Baptist confronting Herod (Matt 14:4) and ultimately by Christ whose entire ministry was a confrontation of corrupt authority."
      }
    ],
    "19": [
      {
        "type": "theme",
        "target": "1 Kgs 22:38",
        "note": "&ldquo;In the place where dogs licked up the blood of Naboth shall dogs lick your own blood.&rdquo; This is Elijah&rsquo;s oracle of exact recompense — same place, same instrument, same outcome. The oracle is fulfilled in 1 Kings 22:38: &ldquo;they washed the chariot by the pool of Samaria, and the dogs licked up his blood.&rdquo; The fulfillment structure — prophetic word followed by its exact historical realization — is a marker of genuine prophecy throughout the OT (Deut 18:21-22). It establishes that YHWH&rsquo;s word shapes history rather than simply predicting it, a claim the NT extends to every prophecy fulfilled in Christ."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Rom 7:14",
        "note": "Elijah announces to Ahab: &ldquo;You have sold yourself (<em>hitmakartā</em>) to do evil in the sight of YHWH.&rdquo; The idiom of self-selling (<em>mākar</em> in the reflexive) describes voluntary slavery — Ahab is not merely tempted into sin but has made himself sin&rsquo;s slave through a series of willing choices. Paul uses the same idiom in Romans 7:14: &ldquo;I am of the flesh, sold under sin (<em>pepramenos hypo tēn hamartian</em>).&rdquo; The Hebrew and Greek idioms are exact equivalents: one who has sold himself cannot free himself. The solution to being sold under sin is the same in both Testaments — redemption requires a price paid by another (Gal 3:13; 1 Cor 6:20)."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Rev 2:20",
        "note": "The narrator&rsquo;s summary: &ldquo;There was none who sold himself to do what was evil in the sight of YHWH like Ahab, whom Jezebel his wife incited (<em>hēsîtāh</em>).&rdquo; Jezebel becomes the paradigm of the woman who uses royal-religious authority to seduce the people of God into idolatry and sexual immorality. Revelation 2:20 takes this as a type directly: &ldquo;I have this against you, that you tolerate that woman Jezebel, who calls herself a prophetess and is teaching and seducing my servants to practice sexual immorality and to eat food sacrificed to idols.&rdquo; The &ldquo;Jezebel&rdquo; of Thyatira is named by the figure she embodies — the prophetic tradition identifies her incitement of Ahab as the pattern for any false teacher who corrupts God&rsquo;s people from within."
      }
    ],
    "27": [
      {
        "type": "theme",
        "target": "Jon 3:10",
        "note": "After Elijah&rsquo;s devastating oracle, Ahab tears his clothes, fasts, and goes about quietly — a genuine act of mourning and humiliation. YHWH&rsquo;s response is immediate: &ldquo;Have you seen how Ahab has humbled himself before me? Because he has humbled himself before me, I will not bring the disaster in his days.&rdquo; The pattern — repentance immediately moves divine judgment — is the same as Nineveh in Jonah 3: a wicked king repents in response to a prophetic word of doom, and YHWH relents from the threatened catastrophe. 2 Peter 3:9 states the principle: &ldquo;The Lord is not slow to fulfill his promise as some count slowness, but is patient toward you, not wishing that any should perish, but that all should reach repentance.&rdquo; Even Ahab&rsquo;s brief act of humility delays the inevitable — the divine patience extends even to those whose record is as dark as his."
      },
      {
        "type": "theme",
        "target": "2 Pet 3:9",
        "note": "YHWH&rsquo;s relenting in response to Ahab&rsquo;s repentance demonstrates the divine character that 2 Peter 3:9 states explicitly: God is &ldquo;not wishing that any should perish, but that all should reach repentance.&rdquo; The relenting is not a theological problem (as if divine justice is compromised) but a revelation of the same character that sent Jonah to Nineveh, that waited for Israel through centuries of apostasy, and that sent Christ — the patience of YHWH toward sinners is not weakness but the outworking of his desire to save."
      }
    ]
  }
}

def main():
    existing = load_echo('1kings')
    merge_echo(existing, KINGS_ECHOES)
    save_echo('1kings', existing)
    print('1 Kings 20-21 echoes written.')

if __name__ == '__main__':
    main()
