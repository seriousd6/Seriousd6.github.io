"""
Joshua — all four layers.
Key NT uses: Rahab's faith/scarlet cord (2), crossing Jordan (3-4),
fall of Jericho (6), Joshua as type of Jesus (same name), rest-promise (1, 21-22).
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

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ECHO = {
  "1": {
    "5": [
      {"type": "allusion", "target": "Heb 13:5", "note": "I will not leave you or forsake you — YHWH's promise to Joshua (Josh 1:5) is quoted in Heb 13:5 as the basis for Christian contentment: he has said I will never leave you nor forsake you; what was said to Joshua as a conquest promise is applied to all believers as a life-promise"}
    ]
  },
  "2": {
    "18": [
      {"type": "allusion", "target": "Heb 11:31", "note": "The scarlet cord in the window — Rahab the prostitute's faith (she hid the spies and trusted in YHWH's deliverance) is remembered in the Hall of Faith; her scarlet cord sign has been read as a type of the blood of Christ marking the household for salvation"},
      {"type": "allusion", "target": "Jas 2:25", "note": "Was not Rahab the prostitute also justified by works when she received the messengers and sent them out by another way? — James cites Rahab alongside Abraham as proof that faith works; her active concealment of the spies demonstrates living faith, not mere assent"}
    ]
  },
  "3": {
    "17": [
      {"type": "allusion", "target": "Matt 3:13", "note": "The people passed over on dry ground through the Jordan — the Jordan crossing (waters parted as at the Red Sea) is the typological background for Jesus's baptism in the Jordan: he enters the water of judgment and comes out the other side, inaugurating the new exodus; baptism as the new covenant Jordan-crossing"}
    ]
  },
  "5": {
    "13": [
      {"type": "allusion", "target": "Rev 19:11-15", "note": "The commander of YHWH's army with his drawn sword — the divine warrior who appears to Joshua is the pre-incarnate Christ, the same figure who leads the armies of heaven in Revelation 19; the Joshua narrative is set in motion by the personal presence of the divine commander"}
    ]
  },
  "21": {
    "45": [
      {"type": "allusion", "target": "Heb 4:8-9", "note": "Not one word of all the good promises that YHWH had made to the house of Israel had failed — Joshua's testimony of YHWH's complete faithfulness to his land-promises; yet Hebrews argues that if Joshua had given them rest, God would not have spoken of another day later on (Ps 95:7-8): the Canaan rest is real but not final, pointing to the eschatological sabbath-rest that remains for the people of God"}
    ]
  }
}

ORIGINAL = {
  "1": {
    "1": "<p>Joshua's Hebrew name (<em>Yehoshua</em>) means 'YHWH saves' — the same name as Jesus (Greek <em>Iēsous</em>, from the LXX transliteration of <em>Yehoshua</em>). The name-identity is not coincidental: Hebrews 4:8 uses the identity of names to make a theological argument ('if Joshua [<em>Iēsous</em>] had given them rest ...'). Joshua is Israel's deliverer who leads the people into the promised land after Moses; Jesus is the deliverer who leads his people into the ultimate rest that Canaan only shadowed. The structural parallel is complete: Moses (law) could not bring Israel into rest; Joshua/Jesus (the one YHWH saves) is the one who completes the journey.</p>"
  },
  "2": {
    "18": "<p><strong>et tikvat chut hashani hazeh tiksheri bevad haChalon</strong>: 'this scarlet thread [<em>tikvat chut hashani</em>] you shall tie in the window.' <em>Tikvah</em> can mean both 'cord/thread' and 'hope' — some patristic interpreters (Justin Martyr, Origen) noted that the word for Rahab's hope (<em>tikvah</em>) is the same as the word for her scarlet cord; her hope and the scarlet cord are linguistically the same thing. Whether or not this wordplay is original, the typological point is clear: the scarlet cord marks the household for salvation as the Passover blood marked the doorposts; those inside are safe, those outside are not. Rahab's inclusion in Matthew's genealogy (Matt 1:5) is a Gentile woman's faith being woven into the Messiah's line.</p>"
  }
}

CONTEXT = {
  "1": {
    "1": "<p>Joshua narrates the conquest of Canaan under Joshua's leadership (ca. 1406-1380 BCE on the early date, ca. 1230-1200 on the late date). It was written to show the fulfillment of YHWH's land-promises to the patriarchs (Gen 15:18-21) and to demonstrate the covenant consequences of obedience and disobedience. The book presents an idealized conquest (all the land was taken, 11:23; 21:45) alongside a realistic acknowledgment of remaining enclaves (13:1-7; 15:63; 16:10) — both perspectives are true at different levels. The conquest's morality (the <em>cherem</em>, the total destruction commanded) has been a central challenge in biblical ethics; the NT never repeats the command and applies it only to the final eschatological judgment, not to earthly conflict.</p>"
  }
}

CHRIST = {
  "1": {
    "3": "<p>A type: 'Every place that the sole of your foot will tread upon I have given you.' Joshua leads the second generation of Israel into their inheritance — the land promise made to Abraham (Gen 15:18-21), repeated to Isaac and Jacob, promised through Moses, now fulfilled through Joshua. Jesus is the greater Joshua: his name is the same, his mission is analogous (leading his people into the promised inheritance), and the rest he gives exceeds what Canaan could provide. Hebrews 4:1-11 carefully argues that the Canaan-rest was provisional: 'if Joshua had given them rest, God would not have spoken later of another day' (4:8); the true rest is the sabbath-rest that remains for the people of God, entered by faith in Christ (4:11).</p>"
  },
  "2": {
    "18": "<p>A type: 'Tie this scarlet cord in the window and bring your father and mother, your brothers and all your father's household into your house.' Rahab's scarlet cord has been typologically read as the blood of Christ marking the household for salvation — and the parallel is structurally exact: an outsider (a Gentile, a prostitute) is incorporated into God's covenant people by faith expressed through a sign (scarlet cord / blood); everyone inside the marked household is saved; everyone outside is not. Matthew's genealogy (Matt 1:5) incorporates Rahab explicitly into the Messiah's lineage — the Gentile woman of faith is literally in the line of Christ. Rahab is one of the Bible's clearest illustrations that faith, not ethnicity, is the covenant criterion.</p>"
  },
  "21": {
    "45": "<p>A direct revelation: 'Not one word of all the good promises that the LORD had made to the house of Israel had failed; all came to pass.' Joshua's testimony to YHWH's promise-keeping is the OT's most comprehensive affirmation of divine faithfulness to the covenant. Paul applies the same principle to the gospel: 'For all the promises of God find their Yes in him. That is why it is through him that we utter our Amen to God for his glory' (2 Cor 1:20). Christ is the fulfillment of every OT promise — not just some, but all. The land-promises of Joshua are included: their ultimate referent is the new creation inheritance (Rom 4:13: the promise that he would be heir of the world; Heb 11:16: they desire a better country, a heavenly one).</p>"
  }
}

def main():
    e = load_echo('joshua')
    merge_echo(e, ECHO)
    save_echo('joshua', e)

    c = load_comm('mkt-original', 'joshua')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', 'joshua', c)

    c = load_comm('mkt-context', 'joshua')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', 'joshua', c)

    c = load_comm('mkt-christ', 'joshua')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', 'joshua', c)

    print('joshua: all 4 layers written')

if __name__ == '__main__':
    main()
