"""
MKT Context Commentary — 2 Samuel chapters 12–13
Run: python3 scripts/zc-context-2samuel-12-13.py

Ch12: Nathan's prophetic parable technique — first recorded mashal as confrontational
      prophecy; the public dimension of royal sin; Yedidyah — grace after judgment
Ch13: The Succession Narrative's structural thesis — the three-wave dynastic punishment;
      Tamar's desolation and the legal-social context of rape in ancient Israel

ANE/historical context:
- The mashal (parable) as a prophetic confrontation device — rare in ANE literature;
  Nathan's parable anticipates the rabbinic mashal tradition and Jesus's parables
- nāʾaṣ (12:14): to despise/blaspheme — the ANE concept of the king's sin as
  national-divine offense; YHWH's name at stake in the king's conduct
- Yedidyah (12:25): 'beloved of YHWH' — the grace-name given through Nathan
- The Succession Narrative (2 Sam 9–20, 1 Kgs 1–2): widely recognized as one of
  the oldest prose narratives in world literature
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

CONTEXT = {
  "12": {
    "1": "<p>Nathan&rsquo;s parable to David is the earliest recorded example of the prophetic <em>māšāl</em> (parable/allegory) used as a confrontational device. The <em>māšāl</em> genre in the OT ranges from proverbs to extended allegories (Ezek 17; 24), but its use as a prophetic tool to bypass a king&rsquo;s defenses and produce self-condemnation is unique to this passage. Nathan&rsquo;s technique — inducing David to pronounce judgment on &ldquo;the rich man&rdquo; and then revealing the parable&rsquo;s referent — is a rhetorical trap of extraordinary sophistication. The rabbinic tradition would later formalize the mashal as a teaching device (the parable with its <em>nimshal</em>, the point of application); Jesus&rsquo;s parables draw on this tradition while reversing the direction: rather than trapping the hearer in their own judgment, they invite the hearer to see themselves in one of the characters and choose their response. The Succession Narrative (2 Sam 9–20; 1 Kgs 1–2) is widely regarded by scholars as one of the oldest and most sophisticated pieces of prose narrative in world literature. Leonhard Rost&rsquo;s 1926 identification of the Succession Narrative as a literary unit remains influential; its detached, ironic narrative stance — showing the hero&rsquo;s sin without comment — is without parallel in the ancient Near East.</p>",
    "10": "<p>Nathan&rsquo;s oracle of dynastic consequences: <em>wᵉʿattāh lōʾ tāsûr ḥereb mibêtᵉḵā ʿad ʿôlām</em> — &lsquo;now therefore the sword shall never depart from your house.&rsquo; The three-wave structure of the punishment — sword/violence (Amnon killing Absalom&rsquo;s sister; Absalom killing Amnon; the civil war), sexual exposure (Absalom&rsquo;s public violation of David&rsquo;s concubines), and political rebellion (Absalom&rsquo;s coup) — corresponds precisely to the structure of David&rsquo;s sin in vv4-5: violence (killing Uriah), sexual violation (taking Bathsheba), and betrayal of covenantal loyalty. The Hebrew concept of <em>middah kᵉneged middah</em> (measure for measure) — the principle that punishment mirrors the crime in structure if not in degree — is the theological logic the narrative embodies. Chapters 13-20 execute this oracle in exact sequence. The structural correspondence between sin and consequence is the DH&rsquo;s principal pedagogical method: the text does not moralize but shows, allowing the careful reader to perceive the <em>middah kᵉneged middah</em> pattern.</p>",
    "25": "<p>YHWH&rsquo;s naming of Solomon through Nathan: <em>wayyišlaḥ bᵉyaḏ nātān hannāḇîʾ wayyiqrāʾ ʾet šᵉmô yᵉḏîḏyāh biʿăḇûr YHWH</em> — &lsquo;he sent a message by Nathan the prophet, and he called his name Yedidyah (<em>yᵉḏîḏyāh</em> — beloved of YHWH), because of YHWH.&rsquo; The naming is an act of divine grace inserted between the public catastrophe of Bathsheba&rsquo;s first child&rsquo;s death and the Ammonite campaign: the child of the relationship that began in sin receives a name expressing divine delight. <em>Yᵉḏîḏyāh</em> (from <em>yāḏîḏ</em>, beloved, the same root as in Ps 45:1 &lsquo;my heart overflows with a pleasing theme, I address my verses to the king; my tongue is like the pen of a ready scribe&rsquo; — a royal psalm) is the alternate name YHWH gives Solomon, not the throne-name. That this particular child — born of Bathsheba, the Hittite&rsquo;s widow — is declared beloved of YHWH and becomes the temple-builder is the Succession Narrative&rsquo;s most explicit statement of grace-following-judgment: YHWH does not abandon his covenantal purpose even when it runs through human sin.</p>"
  },
  "13": {
    "1": "<p>The Succession Narrative opens its second movement with the three words that mark the royal household&rsquo;s internal decay: <em>ûlᵉʾaḇšālôm ben dāwiḏ ʾāḥôt yāpāh</em> — &lsquo;and Absalom the son of David had a beautiful sister.&rsquo; The narrative structure of ch13-20 executes Nathan&rsquo;s oracle (12:10-12) with precise structural correspondence: the sword (Amnon&rsquo;s violation → Absalom&rsquo;s killing of Amnon → the eventual civil war), sexual violation in daylight (Absalom&rsquo;s public appropriation of David&rsquo;s concubines, 16:22), and the rebellion that humiliates David publicly (Absalom&rsquo;s coup). The &lsquo;Succession Narrative&rsquo; designation used by modern scholars refers to chapters 9-20 and 1 Kgs 1-2, which together answer the question: who will sit on David&rsquo;s throne? The narrative is notable for its absence of prophetic interruption (unlike the earlier David stories): YHWH&rsquo;s hand is visible only through consequences, not through direct oracles. This literary restraint — showing rather than telling — is the narrative&rsquo;s theological sophistication.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2samuel')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2samuel', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2samuel mkt-context: wrote {count} verses across ch 12-13')

if __name__ == '__main__':
    main()
