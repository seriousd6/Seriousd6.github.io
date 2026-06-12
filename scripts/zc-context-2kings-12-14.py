"""
MKT Context Commentary — 2 Kings chapters 12–14
Run: python3 scripts/zc-context-2kings-12-14.py

Ch12: Joash's temple repair — the collection-chest innovation; Jehoiada's reforms;
      the Aramean payment-of-tribute to preserve Jerusalem
Ch13: Elisha's death and the posthumous resurrection — prophetic power as object of
      reverence in the ancient world; Amos 2:11-12 context
Ch14: Amaziah's challenge to Joash / the thistle-and-cedar parable — ANE fable form;
      Jeroboam II's territorial expansion — the width of Amos's indictment

ANE/historical context:
- 12:9: the chest at the temple gate — parallels in Mesopotamian temple collection practices
- 13:21: Elisha's bones resurrection — prophetic relics in ANE context
- 14:9: thistle-cedar parable — ANE fable genre (Jotham's trees, Judg 9:7-15)
- 14:25: Jonah from Gath-hepher — placing Jonah historically in the period of Jeroboam II
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
    "9": "<p>Jehoiada&rsquo;s innovation — boring a hole in the lid of a chest (<em>wayyiqqaḥ yᵉhôyāḏāʿ hakkōhēn ʾărôn ʾeḥāḏ wayyiqḇōʿ ḥōr bᵉḏaltô</em>) and placing it beside the altar on the right side at the entrance to the temple — is the OT&rsquo;s earliest described purpose-built collection mechanism. The chest collects designated funds specifically for temple repair: the priests are formally excluded from the repair funds (v8: they no longer take money from the people), and the money goes directly to the craftsmen. This institutional separation of priestly income from temple maintenance funds addresses the corruption evident in v7 (the priests have not repaired the temple). Comparable collection mechanisms appear in Mesopotamian temple records: the Ur III temple accounts (ca. 2100-2000 BCE) document grain and metal contributions to temple maintenance through specialized administrative systems. The sociological point: the collection-chest innovation is a form of institutional accountability — the money is counted by the king&rsquo;s secretary and high priest together (v10), preventing individual priestly appropriation. The NT&rsquo;s contrast between the chest&rsquo;s large and small contributions (Mark 12:41-44) is set against this institutional background: the treasury (<em>gazophylakion</em>) at the Jerusalem temple was the direct institutional descendant of the Joash-era chest.</p>"
  },
  "13": {
    "20": "<p>The notice that Moabite raiders used to invade every spring (<em>wᵉʾōrᵉḥôt môʾāḇ bāʾû bāʾāreṣ bōʾ šānāh</em>) frames the posthumous resurrection miracle: a burial party, encountering raiders, throws a corpse into Elisha&rsquo;s tomb; the man revives when he touches Elisha&rsquo;s bones. The ANE context for prophetic relics and their power is extensive: the Ugaritic ritual texts document the care of ancestral bones in funerary rites; Egyptian texts describe the power of mummified remains; Greek hero-cults at the classical period were built around the burial sites of legendary figures whose bones were believed to convey protective power. In Israelite practice, the bones of Joseph were carried out of Egypt at the exodus (Exod 13:19) and finally buried at Shechem (Josh 24:32) — the preservation and ultimate burial of the patriarch&rsquo;s bones was a covenant obligation. The Elisha-bones miracle is not a general statement about prophetic relics (the text does not encourage relic-devotion) but a narrative demonstration that the power of the Spirit of YHWH that worked through Elisha was not exhausted by Elisha&rsquo;s death — the same Spirit that will raise the dead (Ezek 37: dry bones; John 5:28-29) is already active in the prophetic tradition, exceeding the prophet&rsquo;s own lifetime.</p>"
  },
  "14": {
    "9": "<p>King Joash of Israel&rsquo;s response to Amaziah&rsquo;s challenge — a fable about the thistle of Lebanon sending to the cedar of Lebanon asking for his daughter in marriage, and the cedar ignoring it until a wild beast trampled the thistle — is a specimen of the ANE fable genre applied to political rhetoric. The <em>māšāl</em> (proverb, parable, fable) was a recognized diplomatic/rhetorical form throughout the ancient Near East: Jotham&rsquo;s fable of the trees seeking a king (Judg 9:7-15) is the OT&rsquo;s most developed earlier example, and Egyptian wisdom literature contains animal-fables used in political contexts (the demotic fable-papyri). The cedar/thistle contrast is an ANE botanical hierarchy: the cedar of Lebanon (<em>ʾerez lᵉḇānôn</em>) is the supreme tree of ANE literary tradition — mighty, magnificent, impossible to damage without great effort. The thistle (<em>ḥôaḥ</em>) is the thorn-weed of field and path, trampled without notice. Joash identifies himself as the cedar and Amaziah as the thistle — the parable is designed to deflate Amaziah&rsquo;s pride without open insult, giving him a face-saving opportunity to withdraw. The narrative confirms the parable&rsquo;s accuracy: Amaziah does not heed and is defeated (v12). The ANE fable tradition used by Joash is the same genre Jesus deploys in the parables, though the Gospels&rsquo; parables characteristically invert the hierarchies the ANE fable assumes.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2kings mkt-context: wrote {count} verses across ch 12-14')

if __name__ == '__main__':
    main()
