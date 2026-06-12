"""
Echo Layer — Esther chapters 1–5
Run: python3 scripts/zc-echo-esther-1-5.py

Key echo connections in this range:
- 1:11-19: Vashti deposed for refusal — honour/replacement theme → Prov 31:10-12; Matt 5:5
- 2:7: Mordecai raises orphaned Esther → James 1:27 (pure religion = orphan care)
- 2:17: King chooses Esther above all → Deut 7:6 (YHWH choosing beloved people)
- 3:1: Haman the Agagite → 1 Sam 15:8 (Saul's failure to destroy Agag = root of this crisis)
- 3:2: Mordecai refuses to bow → Dan 3:12 (Shadrach/Meshach/Abednego refuse to bow)
- 3:6: Genocidal decree against all Jews → Ps 83:4; Rev 12:17 (dragon attacks seed of woman)
- 4:14: "for such a time as this" → Acts 17:26-27 (already present); Gal 4:4 (fullness of time)
- 4:16: "If I perish, I perish" + three-day fast → John 12:24; Luke 24:46 (resurrection pattern)
- 5:1: Esther approaches on the third day → 1 Cor 15:4; Matt 20:19 (third-day typology)
- 5:2: Esther finds hen (favour/grace) before the king → Gen 6:8; Heb 4:16 (throne of grace)
- 5:14: Haman builds gallows for Mordecai → Gal 6:7 (reap what you sow); Prov 26:27
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

ESTHER_ECHO_1_5 = {
  "1": {
    "1": [
      {"type": "allusion", "target": "Dan 4:1", "note": "&#8220;In the days of Ahasuerus, who reigned from India to Ethiopia over one hundred and twenty-seven provinces&#8221; — the universal scope of Persian dominion echoes Daniel&#8217;s world-empire theology; in both Daniel and Esther the fate of the covenant people is decided within pagan court politics, and in both the story insists that YHWH&#8217;s hidden sovereignty operates precisely within the machinery of empire that appears to control the world"}
    ],
    "2": [
      {"type": "allusion", "target": "Neh 1:1", "note": "&#8220;King Ahasuerus sat on his royal throne at the citadel of Susa&#8221; — Susa is the same setting as Nehemiah 1:1; together they form the two faces of Persian-period Jewish experience: the court insider (Esther/Mordecai) and the court servant who returns to rebuild (Nehemiah); both stories begin at Susa and move through the logic of Persian royal favour toward the preservation and restoration of Israel"}
    ],
    "11": [
      {"type": "allusion", "target": "Prov 31:10", "note": "Vashti is summoned to display her beauty before the king and his officials — the demand treats a wife as a possession rather than a person of worth; Proverbs 31:10-12 presents the alternative: a woman whose husband trusts her and whose worth is recognized intrinsically; Vashti&#8217;s refusal, whatever the narrator&#8217;s ambiguity about it, exposes the difference between honour bestowed for display and honour rooted in character"}
    ],
    "19": [
      {"type": "allusion", "target": "Matt 5:5", "note": "&#8220;Her royal position will be given to one who is better than she&#8221; — Ahasuerus&#8217;s advisors recommend replacement; providentially, the &#8220;better&#8221; replacement will be Esther, through whom Israel is saved; the displacement of Vashti sets in motion the story in which the meek inherit — not by assertion but by endurance and strategic courage; the pattern of the humble displacing the exalted runs from here to the Beatitudes"}
    ]
  },
  "2": {
    "7": [
      {"type": "allusion", "target": "Jas 1:27", "note": "Mordecai had raised Hadassah (Esther), for she had no father or mother — his guardianship of an orphaned cousin is the lived form of what James declares to be pure religion: &#8220;to visit orphans and widows in their affliction&#8221; (Jas 1:27); Mordecai&#8217;s daily care for Esther, continued even into her time in the harem (2:11), models the covenant loyalty that constitutes authentic devotion within a world where the temple is absent and explicit piety is suppressed"}
    ],
    "10": [
      {"type": "allusion", "target": "Gen 45:1", "note": "&#8220;Esther had not made known her people or her kindred, for Mordecai had instructed her not to make it known&#8221; — the concealment of identity in a foreign court is the pattern established by Joseph in Egypt (Gen 37-45); both Joseph and Esther operate under hiddenness until the moment of crisis when their identity must be revealed for the people to be saved; the revelation of identity (Esther 7:3; Gen 45:1) becomes the turning point of both stories"}
    ],
    "17": [
      {"type": "allusion", "target": "Deut 7:6", "note": "&#8220;The king loved Esther more than all the women, and she found grace and favour (<em>&#7717;&#275;n w&#257;&#7717;eseḏ</em>) in his sight more than all the virgins&#8221; — the pairing of <em>&#7717;&#275;n</em> (grace/favour) and <em>&#7717;eseḏ</em> (steadfast love) is the covenant vocabulary that Deuteronomy 7:6 uses for YHWH&#8217;s election of Israel: &#8220;you are a people holy to the LORD your God... a treasured possession&#8221;; the king&#8217;s inexplicable preference for Esther is the human image of divine election — favour given, not earned, to a hidden and unlikely recipient"}
    ],
    "21": [
      {"type": "allusion", "target": "Rom 13:4", "note": "Mordecai uncovers the assassination plot against Ahasuerus and reports it through Esther — his protection of the pagan king who holds power over his people is the OT form of Paul&#8217;s teaching that the governing authorities are God&#8217;s servants (Rom 13:4); Mordecai acts loyally within the imperial system even while maintaining a loyalty to his people that the system cannot command; his deed is recorded in the royal chronicles (2:23), the human register that God will use at the pivotal moment of chapter 6"}
    ]
  },
  "3": {
    "1": [
      {"type": "allusion", "target": "1 Sam 15:8", "note": "&#8220;Haman the son of Hammedatha the Agagite&#8221; — the Agagite designation is a direct pointer to 1 Samuel 15: Saul was commanded to destroy Agag and the Amalekites completely but spared Agag (1 Sam 15:8-9); Samuel killed Agag (15:33) but the failure to complete the <em>&#7717;&#275;rem</em> is retrospectively blamed for this crisis; in Esther, the descendant of Benjamin (Mordecai, 2:5 — same tribe as Saul) will face the descendant of Agag, and what Saul failed to finish, the story of Esther will complete"}
    ],
    "2": [
      {"type": "allusion", "target": "Dan 3:12", "note": "&#8220;Mordecai would not bow down or pay homage&#8221; — the refusal to bow to a human official as an act of religious loyalty is the same stance taken by Shadrach, Meshach, and Abednego when ordered to worship Nebuchadnezzar&#8217;s statue (Dan 3:12); both stories embed the same question: what is the one act of symbolic obeisance that a faithful Jew cannot perform without denying YHWH&#8217;s exclusive claim? Both refusals trigger a genocidal response that YHWH overturns; the pattern is the pattern of Daniel-Esther exile piety"},
      {"type": "allusion", "target": "Acts 5:29", "note": "Mordecai&#8217;s refusal to obey the king&#8217;s command regarding Haman is the OT form of the apostolic principle: &#8220;we must obey God rather than men&#8221; (Acts 5:29); both texts locate the moment of civil disobedience precisely at the point where human command contradicts the fundamental theological claim — YHWH&#8217;s sole lordship cannot coexist with ritual deference to a rival authority"}
    ],
    "6": [
      {"type": "allusion", "target": "Rev 12:17", "note": "&#8220;Haman sought to destroy all the Jews, the people of Mordecai, throughout the whole kingdom of Ahasuerus&#8221; — the genocidal intent against the entire covenant people is the OT type of the dragon&#8217;s campaign against &#8220;the rest of her offspring, those who keep the commandments of God&#8221; (Rev 12:17); in both texts, the annihilation of the seed of the woman is the goal; in both, the attempt fails through providential reversal; Haman is the <em>&#7717;ar-m&#283;ggid&#244;</em> of the Persian period"},
      {"type": "allusion", "target": "Ps 83:4", "note": "&#8220;[Haman sought] to destroy all the Jews&#8221; — Psalm 83:4 voices the same genocidal goal: &#8220;Come, let us wipe them out as a nation; let the name of Israel be remembered no more!&#8221;; the psalmist&#8217;s prayer against the coalition that seeks Israel&#8217;s annihilation is answered in the Esther narrative — the decree is reversed, the enemy is destroyed, and the name of Israel is preserved"}
    ],
    "10": [
      {"type": "allusion", "target": "Gen 41:42", "note": "&#8220;The king took his signet ring from his hand and gave it to Haman&#8221; — the signet ring delegating royal authority is the same gesture Pharaoh uses when giving Joseph authority over Egypt (Gen 41:42); the irony is structural: the ring that saves in Genesis becomes the ring that condemns in Esther; but the deeper irony is that both stories end with the ring&#8217;s authority redirected toward Israel&#8217;s salvation — Esther 8:2 shows Mordecai receiving the same ring after Haman&#8217;s downfall"}
    ],
    "13": [
      {"type": "allusion", "target": "John 10:10", "note": "The decree goes out to destroy, kill, and annihilate (<em>l&#277;hašm&#238;&#7693; lah&#7611;r&#333;&#7853; ûl&#277;ʾabb&#275;&#7693;</em>) all Jews — the triple verb cluster of destruction echoes the character of the enemy in John 10:10: &#8220;the thief comes only to steal and kill and destroy&#8221; (<em>kleptein kai thyein kai apollyein</em>); the concentrated language of annihilation marks both Haman and the thief of John 10 as embodiments of the same anti-life power that Christ came to overthrow: &#8220;I came that they may have life and have it abundantly&#8221;"}
    ]
  },
  "4": {
    "1": [
      {"type": "allusion", "target": "Joel 2:12", "note": "Mordecai tears his clothes, puts on sackcloth and ashes, and cries with a loud and bitter cry — the mourning practices in Esther 4:1-3 are the same emergency repentance gestures that Joel 2:12-13 calls for: &#8220;return to me with all your heart, with fasting, with weeping, and with mourning; and rend your hearts&#8221;; the paradox of Esther is that nowhere is YHWH named, yet the fast of 4:16, the sackcloth of 4:1-3, and the prayer implied throughout are the enacted form of exactly the covenant return Joel envisions"}
    ],
    "14": [
      {"type": "allusion", "target": "Gal 4:4", "note": "&#8220;Who knows whether you have not come to the kingdom for such a time as this?&#8221; — Mordecai&#8217;s rhetorical question frames Esther&#8217;s placement in the harem as providentially purposed for this crisis moment; Paul&#8217;s &#8220;fullness of time&#8221; (Gal 4:4) is the NT articulation of the same theological claim: that God&#8217;s agents are placed at specific historical junctures for specific redemptive purposes; both texts resist fatalism (&#8220;if you keep silent...&#8221;) while affirming that providence has already positioned its instrument"}
    ],
    "16": [
      {"type": "allusion", "target": "John 12:24", "note": "&#8220;If I perish, I perish&#8221; — Esther&#8217;s willingness to die for her people, preceded by the three-day fast that is the only explicit &#8220;religious&#8221; act in the book, is the OT form of the grain-of-wheat saying: &#8220;unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit&#8221; (John 12:24); Esther&#8217;s self-offering — going unsummoned to the king, risking death — becomes the instrument of Israel&#8217;s salvation"},
      {"type": "allusion", "target": "Luke 24:46", "note": "&#8220;Fast for me... for three days, night or day... then I will go to the king, though it is against the law, and if I perish, I perish&#8221; — the three-day fast preceding the approach to the king creates the structural pattern of death-and-life that Luke 24:46 identifies as the scriptural necessity: &#8220;that the Christ should suffer and on the third day rise from the dead&#8221;; Esther&#8217;s three days end not in death but in favour and rescue — an anticipatory pattern of the resurrection on the third day"}
    ]
  },
  "5": {
    "1": [
      {"type": "allusion", "target": "1 Cor 15:4", "note": "&#8220;On the third day Esther put on her royal robes and stood in the inner court of the palace&#8221; — the temporal marker &#8220;on the third day&#8221; following the three-day fast (4:16) creates one of the OT&#8217;s most explicit third-day patterns; 1 Corinthians 15:4 identifies the resurrection &#8220;on the third day in accordance with the Scriptures&#8221; — this is one of the scriptural patterns Paul has in mind; the one who had as it were died (&#8220;if I perish, I perish&#8221;) now stands clothed in royal garments before the throne, alive and vindicated"}
    ],
    "2": [
      {"type": "allusion", "target": "Heb 4:16", "note": "&#8220;When the king saw Queen Esther standing in the court, she found favour in his eyes. He held out the golden sceptre... and Esther approached and touched the tip of the sceptre&#8221; — this is the OT image behind Hebrews 4:16: &#8220;let us then with confidence draw near to the throne of grace, that we may receive mercy and find grace to help in time of need&#8221;; Esther approaching the king unsummoned, risking death, and receiving the extended sceptre of welcome is the exact typological scene that &#8220;throne of grace&#8221; evokes; in Christ, the sceptre is always extended"},
      {"type": "allusion", "target": "Gen 6:8", "note": "&#8220;She found favour (<em>&#7717;&#275;n</em>) in his eyes&#8221; — Esther&#8217;s finding of favour before the king uses the same formula as Noah finding favour with YHWH (Gen 6:8: &#8220;Noah found favour in the eyes of the LORD&#8221;); in both cases, the favour is undeserved, its recipient is surrounded by hostility or judgment, and it results in the preservation of a remnant; <em>&#7717;&#275;n</em> — grace/favour — is the unilateral gift that reverses the sentence of death"}
    ],
    "3": [
      {"type": "allusion", "target": "Mark 6:23", "note": "&#8220;What is your request? It shall be granted to you, even up to half the kingdom&#8221; — the extravagant royal offer echoes Herod&#8217;s promise to Herodias&#8217;s daughter (Mark 6:23); both scenes show a king making an open-ended pledge; but the contrast is the point: Herod&#8217;s promise leads to the death of the prophet, Ahasuerus&#8217;s leads to the salvation of a people; the same rhetorical form serves opposite ends, and the difference is the character of the intercessor who brings the request"}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 14:12", "note": "&#8220;Yet all this is worth nothing to me, as long as I see Mordecai the Jew sitting at the king&#8217;s gate&#8221; — Haman&#8217;s inability to enjoy his position, power, wealth, and royal favour because one man refuses to honour him is the portrait of pride that cannot bear to share space with a rival; Isaiah 14:12-15 traces the same psychology of <em>g&#275;ʾ&#257;h</em> (arrogance) that drives the king of Babylon to his ruin: &#8220;I will make myself like the Most High&#8221; — and falls; Haman&#8217;s obsession with Mordecai&#8217;s refusal is the pride that precedes the fall of chapters 6-7"}
    ],
    "14": [
      {"type": "allusion", "target": "Gal 6:7", "note": "Zeresh and Haman&#8217;s friends advise him to build a gallows fifty cubits high and hang Mordecai on it — the counsel that sounds like a solution is the preparation of his own destruction; Galatians 6:7: &#8220;whatever one sows, that will he also reap&#8221;; the gallows Haman builds for Mordecai becomes the gallows on which Haman himself is hanged (7:9-10); the sowing/reaping principle here is compressed into a single narrative act — the instrument of intended murder becomes the instrument of the murderer&#8217;s execution"},
      {"type": "allusion", "target": "Prov 26:27", "note": "&#8220;He had a gallows made, fifty cubits high&#8221; — Proverbs 26:27: &#8220;Whoever digs a pit will fall into it, and a stone will come back on him who starts it rolling&#8221;; the proverb that expresses the retributive logic of the world is enacted literally in Esther: the pit (gallows) prepared for the righteous is the pit into which the wicked fall; the fifty-cubit height, intended to ensure maximum visibility and shame for Mordecai, ensures maximum visibility and shame for Haman when the reversal comes"}
    ]
  }
}

def main():
    existing = load_echo('esther')
    merge_echo(existing, ESTHER_ECHO_1_5)
    save_echo('esther', existing)
    print('Esther 1-5 echo layer written.')

if __name__ == '__main__':
    main()
