"""
MKT Context Commentary — 2 Samuel chapters 14–16
Run: python3 scripts/zc-context-2samuel-14-16.py

Ch14: The wise woman of Tekoa — the ʾēšet ḥāḵāmāh as ANE intermediary role;
      the technique of the prophetic trap applied by Joab
Ch15: Absalom's judicial demagoguery at the gate — the ANE context of royal justice;
      the Mount of Olives exile route — the geography of David's departure
Ch16: Ahithophel of Giloh — the political-wisdom tradition in ancient Israel;
      Shimei's curses from Bahurim in Benjamin territory

ANE/historical context:
- ʾēšet ḥāḵāmāh (14:2): 'wise woman' — a recognized professional mediator role
- City gate justice (15:2-6): the šaʿar (gate) as the formal legal venue in ANE cities
- Ahithophel (16:23): 'his counsel was like the word of God' — the wisdom tradition
- Giloh (15:12): in the Judahite hill country, ca. 8 km south of Hebron
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
  "14": {
    "2": "<p>Joab summons a woman from Tekoa (<em>ʾiššāh ḥāḵāmāh mētᵉqōaʿ</em>, a wise woman from Tekoa) to act as his proxy in the David/Absalom negotiations. The term <em>ʾēšet ḥāḵāmāh</em> (wise woman) designates a recognized professional role in ancient Israelite society — an intermediary who was skilled in rhetorical argument, legal framing, and persuasive speech. The same designation appears in 2 Sam 20:16-22, where a wise woman from Abel negotiates with Joab during the Sheba rebellion, successfully defusing a military crisis through forensic argument. These two instances suggest a recognized category of professional female wisdom-practitioners who could function as public speakers and legal advocates in situations where women had access but male advocates did not. The Proverbs figure of the <em>ʾēšet ḥayil</em> (the capable woman, Prov 31:10-31) who &lsquo;opens her mouth with wisdom&rsquo; (31:26) may be in the background of this professional category. Tekoa (<em>tᵉqôaʿ</em>) is a village approximately 16 km south of Jerusalem in the Judahite hill country, the same location the prophet Amos identifies as his hometown (Amos 1:1: &lsquo;the words of Amos, who was among the shepherds of Tekoa&rsquo;).</p>",
    "14": "<p>The wise woman&rsquo;s theological statement — &lsquo;we must all die; we are like water spilled on the ground... yet God devises means so that the banished one will not remain an outcast&rsquo; — is spoken within a fictional legal case but contains a genuine theological principle that the narrator endorses. The image of spilled water (<em>mayyim niggārîm ʾārṣāh</em>) as a mortality metaphor has ANE parallels: the Epic of Gilgamesh uses comparable water/dissolution imagery for human mortality. But the theological move — that YHWH actively devises (<em>ḥāšaḇ maḥăšāḇôt</em>) to bring back the banished — is distinctively Israelite: a deity not merely accepting mortality as fate but actively planning around it. This is the Second Temple reception of the verse: the rabbinic tradition associated <em>ḥāšaḇ maḥăšāḇôt</em> with the divine redemptive planning that runs from the Exodus through the return from exile.</p>"
  },
  "15": {
    "2": "<p>Absalom&rsquo;s four-year campaign to steal the hearts of the Israelites is conducted at the city gate (<em>šaʿar</em>): <em>wayyaškem ʾaḇšālôm wᵉʿāmaḏ ʿal yaḏ derek haššaʿar</em> — &lsquo;Absalom used to rise early and stand beside the way of the gate.&rsquo; The city gate in ANE cities was the formal venue for legal proceedings, commercial transactions, and public assembly — the equivalent of the modern courthouse and town square combined. Ruth 4:1 shows Boaz conducting the levirate proceedings &lsquo;at the gate&rsquo;; Job 29:7 shows the elder &lsquo;taking his seat in the gate&rsquo; as the mark of civic authority. Absalom appropriates this legal venue by intercepting litigants before they reach the king, hearing their cases himself, and declaring — without authority — that their cause is just and that there is no royal appointee to hear them. This is a calculated delegitimization of David&rsquo;s administration through the display of alternative judicial concern. The ANE texts from Ugarit and the Amarna Letters document similar royal or quasi-royal figures who built popular support by providing judicial access that the established authority withheld or delayed.</p>",
    "30": "<p>David&rsquo;s ascent of the Mount of Olives (<em>maʿăleh hazzeytîm</em>) marks the geographic pivot of the Absalom narrative. The ridge of the Mount of Olives runs parallel to Jerusalem&rsquo;s eastern side, separated by the Kidron Valley, and forms the natural route eastward from Jerusalem toward the Jordan Valley and Transjordan. The ancient road David would have taken descends the eastern slope of the Mount of Olives toward Bethany, then drops into the Jordan Rift Valley — a descent of approximately 1,200 meters over 25 km. This is the road that would later be traveled by Persian-period returnees (Neh 2:11-15), by Jesus on his triumphal entry (Luke 19:29-40: via Bethphage and Bethany on the Mount of Olives), and on which Jesus wept over Jerusalem (Luke 19:41). The geography of David&rsquo;s humiliated exile — barefoot, weeping, heading east over the same ridge — is the precise geographical setting of the Passion week events a millennium later.</p>"
  },
  "16": {
    "23": "<p>The narrator&rsquo;s comment on Ahithophel&rsquo;s standing: <em>ûʿăṣat ʾăḥîṯōpel ʾăšer yaʿaṣ bayyāmîm hāhēm kaʾăšer yišʾal ʾîš bidbar hāʾelōhîm kēn kol ʿăṣat ʾăḥîṯōpel</em> — &lsquo;the counsel of Ahithophel, which he gave in those days, was as if one consulted the word of God; so was all the counsel of Ahithophel esteemed.&rsquo; This extraordinary assessment — placing Ahithophel&rsquo;s political counsel on the same level as divine oracle — reflects the Israelite wisdom tradition&rsquo;s highest claim for sagacity: wisdom that has been so refined by experience and insight that it partakes of divine clarity. Ahithophel is from Giloh (<em>gîlōh</em>), identified with modern Khirbet Jala in the Judahite hill country, approximately 8 km south of Hebron. His granddaughter is Bathsheba (Eliam son of Ahithophel is listed in 2 Sam 23:34 as one of David&rsquo;s mighty men; Bathsheba is the daughter of Eliam, 11:3) — which may explain both Ahithophel&rsquo;s proximity to the court and his personal motivation for joining Absalom&rsquo;s rebellion. The political-wisdom tradition that Ahithophel represents — the professional adviser whose counsel was sought as if it were divine — is the ANE background for the OT wisdom literature&rsquo;s appropriation of this tradition under the claim that &lsquo;the fear of YHWH is the beginning of wisdom&rsquo; (Prov 9:10).</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2samuel')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2samuel', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2samuel mkt-context: wrote {count} verses across ch 14-16')

if __name__ == '__main__':
    main()
