"""
MKT Original — Matthew chapters 7–14 (in one batch for efficiency)
Output: data/commentary/mkt-original/matthew.json (adds ch7-14)

Key terms:
ch7: ekbalo, peirazo, petros/petra
ch8: exousia, Iesou logoi, katharistheti, hekatontarchos
ch9: aphientai, skandalizomai, diakonia
ch10: apostolos, apoleia, martyrion, euangelion
ch11: anapausis, zeugos, chrestos, phortion
ch12: anomia, Beelzeboul, meizōn, blaspemia
ch13: mysterion, kruptos, synienai, synteleia
ch14: perisseuma, periepatesen, distezo
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
  "7": {
    "24": '<p><strong>oikodomesen</strong> — built — the aorist indicates completed action, the wise builder actually builds (vs. merely hearing). <strong>akouon mou tous logous toutous kai poion autous</strong> — hearing my words and doing them — the two-stage requirement mirrors the Shema (<em>shema</em> = hear and obey). <strong>petra</strong> — bedrock, solid rock — contrasted with <em>psammos</em> (sand); the Semitic image of the rock as foundation for covenant stability (Isa 28:16, the tested cornerstone in Zion). The house built on rock withstands floods and winds — the twin disasters of Palestinian flash floods and seasonal windstorms.</p>'
  },
  "8": {
    "9": '<p><strong>kai gar ego anthropos eimi hypo exousian</strong> — for I also am a man under authority — the centurion\'s argument is a fortiori: if he can command soldiers at a distance because he himself is under Roman military authority (a chain of command that gives his words power), how much more can Jesus command disease at a distance, being himself under the ultimate authority. <strong>exousia</strong> — authority, the right and power to act — appears 10 times in Matthew, always associated with Jesus\'s teaching, healing, and forgiving (7:29, 9:6, 11:27, 28:18).</p>',
    "17": '<p><strong>autos tas astheneias hemon elaben kai tas nosous ebastasen</strong> — he himself took our infirmities and bore our diseases — Matthew\'s citation of Isa 53:4 applies the Servant\'s vicarious bearing not to the cross but to the healing ministry. <em>Labo</em> (took) and <em>bastazo</em> (bore, carried) are the verbs of the Servant\'s substitutionary work. The healing miracles are not merely humanitarian acts but are themselves the Servant\'s carrying of human sickness — an extension of the same substitutionary principle that reaches its fullness in the passion.</p>'
  },
  "9": {
    "6": '<p><strong>exousian echei ho huios tou anthropou epi tes ges aphienai hamartias</strong> — the Son of Man has authority on earth to forgive sins — the two claims in sequence: (1) the Son of Man (Danielic title) exercises divine prerogatives, (2) <em>epi tes ges</em> (on earth) — this authority is exercised in history, not deferred to final judgment. The scribes\' objection is theologically correct (only God can forgive sins); Jesus\'s claim is equally precise: the Son of Man is acting with God\'s authority on earth.</p>',
    "13": '<p><strong>eleos thelo kai ou thysian</strong> — mercy I desire and not sacrifice — the Hosea citation (Hos 6:6); <em>eleos</em> (steadfast covenant-love, translating Hebrew <em>hesed</em>) is the Covenant-quality Jesus consistently prioritizes over external cultic performance. <strong>ouk elthon kalesai dikaious alla hamartoulous</strong> — I did not come to call righteous people but sinners — <em>kaleo</em> (to call) carries the election-language of divine summoning; the call of sinners is the unexpected reversal that defines Jesus\'s mission-profile.</p>'
  },
  "10": {
    "28": '<p><strong>me phobeisthe apo ton apokteinonton to soma</strong> — do not fear those who kill the body — the first <em>me phobos</em> is addressed to the fear of persecutors; the second <strong>phobeisthe de mallon</strong> (rather fear) addresses the appropriate fear of God. The contrast is not between two fears of the same kind but between the fear that produces obedience to God and the paralysis produced by fear of humans. <strong>ton de psychen me dynamenon apokteinai</strong> — those who cannot kill the soul — soul (<em>psyche</em>) as the seat of personal existence that physical death does not terminate.</p>'
  },
  "11": {
    "28": '<p><strong>deute pros me pantes hoi kopionte kai pephortimenoi</strong> — come to me all who labor and are heavy laden — <em>kopionto</em> (laboring to exhaustion) + <em>pephortimenoi</em> (perfect passive, permanently burdened) describes the condition; <em>deute pros me</em> (come to me) is Wisdom\'s invitation. <strong>anapausis</strong> — rest, refreshment — not idleness but the rest of the Sabbath: cessation from the burden of self-justifying religious effort. <strong>chrestos</strong> (v.30) — good, pleasant, kind — the same word used for good wine that has aged well (Luke 5:39) and for the kindness of God (Rom 2:4); the yoke of Christ has the quality of what has been made right.</p>'
  },
  "12": {
    "31": '<p><strong>blasphemia tou pneumatos</strong> — blasphemy against the Spirit — uniquely among Matthew\'s sin-categories, this sin is <strong>ouk aphethesetai</strong> (will not be forgiven) in this age or the coming age. The context defines the blasphemy: attributing the works of the Holy Spirit (exorcism performed by the Spirit of God, v.28) to Beelzeboul (the devil). The sin is the persistent, seeing refusal to recognize the Spirit\'s presence in Christ\'s ministry — a willful inversion of light and darkness that places oneself permanently outside the reach of the Spirit who grants repentance.</p>',
    "35": '<p><strong>ho agathos anthropos ek tou agathou thesaurou ekballei agatha</strong> — the good man out of his good treasure brings forth good things — <em>thesauros</em> (treasury, storehouse) as the inner reservoir from which speech flows; <em>ekballo</em> (to throw out, bring out) emphasizes that speech is not accidental but driven out of what is stored within. The heart-treasury precedes and determines the word: character produces speech, not vice versa.</p>'
  },
  "13": {
    "11": '<p><strong>hoti hymin dedotai gnona ta mysteria tes basileias ton ouranon</strong> — to you it has been given to know the mysteries of the kingdom of the heavens — <em>mysterion</em> (mystery, secret) in Jewish apocalyptic usage denoted the divine plan hidden in the age but now disclosed to the elect; Daniel uses the term for what only God and his messenger can reveal (Dan 2:47). The disciples receive the gift of understanding (<em>synesis</em>) that the parable-audience does not receive — not by their merit but by divine grace (<em>dedotai</em>, divine passive).</p>',
    "52": '<p><strong>grammateus matheteutheis te basileia ton ouranon</strong> — a scribe discipled to the kingdom of the heavens — the concluding self-description of the kingdom-teacher; Matthew presents Jesus as producing a new kind of scribe who draws from both old and new. <strong>kainos kai palaios</strong> — new and old — the order is deliberate (new first): the new covenant does not discard the old treasury but brings it forward into its fulfillment; the scribe who understands the kingdom reads the old Torah through the new light Christ provides.</p>'
  },
  "14": {
    "27": '<p><strong>tharsein</strong> — take courage, be of good cheer — an imperative of encouragement used in crisis moments; Jesus speaks it to the storm-panicked disciples and to the paralytic (9:2) and to the hemorrhaging woman (9:22). <strong>ego eimi</strong> — I am — the LXX divine self-disclosure formula (Exod 3:14, Isa 41:4, 43:10); spoken in the darkness on the sea to terrified disciples, the formula identifies Jesus with the divine presence that crossed the Red Sea. <strong>me phobeisthe</strong> — do not fear — the standard divine reassurance formula throughout the OT (Gen 15:1, Isa 41:10, 43:1).</p>'
  }
}

def main():
    existing = load_comm('mkt-original', 'matthew')
    merge_comm(existing, DATA)
    save_comm('mkt-original', 'matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew mkt-original: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
