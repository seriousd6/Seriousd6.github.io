"""
MKT Christ — 1 John chapter 5
Output: data/commentary/mkt-christ/1john.json (adds ch5)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
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

DATA = {
  "5": {
    "5": '<p>A direct revelation: who is it that overcomes the world except the one who believes that Jesus is the Son of God? The Son of God title is here the specific Christological content of faith that makes victory possible. Not general theism or ethical monotheism, but the specific claim that the crucified and risen Jesus is the divine Son — this is what connects the believer to the victory Christ already won over the world. The rhetorical question (who overcomes? the one who believes this) makes faith in Christ the sole and sufficient ground of the community\'s overcoming posture in a hostile world.</p>',
    "6": '<p>A direct revelation: this is he who came through water and blood — Jesus Christ; not in the water only but in the water and the blood. The anti-Docetic Christological precision here is exact: the subject is Jesus Christ (the full name, human and divine), and his coming is through both water (the Jordan baptism, the beginning of his public ministry) and blood (the crucifixion, its completion). The one who came through water is the same one who came through blood — the incarnate Son did not shed his divine nature before the cross, which would have made the cross merely a human death. The blood is the blood of the Son of God (1:7), which is why it cleanses completely.</p>',
    "11": '<p>A direct revelation: God gave eternal life, and this life is in his Son. The Christological claim is locative: eternal life is not a divine attribute distributed generally but a reality located specifically in the Son. The community possesses life because it possesses the Son — union with Christ is the mechanism of life. Whoever has the Son has life; whoever does not have the Son does not have life (v.12). This is the sharpest possible Christological exclusivism grounded not in tribal identity but in the ontological reality that life itself is in Christ and in no other.</p>',
    "20": '<p>A direct revelation: the Son of God has come and has given us understanding to know him who is true; and we are in him who is true, in his Son Jesus Christ. This is the true God and eternal life. The letter closes with the most explicit Christological predication of the NT epistles: "this is the true God and eternal life" — with the most natural antecedent of "this" being Jesus Christ just named. The community is "in him who is true, in his Son Jesus Christ" — in (union with) the Father through being in (union with) the Son. The true God is not accessed apart from Jesus Christ but is found precisely and fully in him. The letter that opened with "the eternal life that was with the Father and was revealed to us" closes by naming what was revealed: this is the true God, eternal life himself.'
  }
}

def main():
    existing = load_comm('mkt-christ', '1john')
    merge_comm(existing, DATA)
    save_comm('mkt-christ', '1john', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 John mkt-christ: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
