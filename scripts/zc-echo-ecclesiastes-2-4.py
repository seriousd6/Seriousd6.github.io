"""
Echo Commentary — Ecclesiastes chapters 2–4
Run: python3 scripts/zc-echo-ecclesiastes-2-4.py

Ch2: Pleasure experiment → 1 Tim 4:4 (creaturely goods from God); v17 groaning
     under vanity → Rom 7:24; v26 sinner gathering for the pleasing one → Matt 25:29
Ch3: A time for everything → Gal 4:4 (fullness of time); v11 eternity in heart →
     Heb 11:1; v14 divine works endure → Rev 15:3; v17 judgment-time fixed → Acts 17:31
Ch4: Oppressed with no comforter → Rev 6:9-10; v9-12 two-better-than-one / three-cord
     → Heb 10:24-25; Matt 18:20; John 17:21
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

ECCLESIASTES_ECHOES = {
  "2": {
    "17": [
      {"type": "allusion", "target": "Rom 7:24",
       "note": "The Preacher&rsquo;s &ldquo;I hated life, because what is done under the sun seemed evil to me&rdquo; — disgust with the <em>hevel</em>-world — reaches its deepest expression in Paul&rsquo;s &ldquo;Wretched man that I am! Who will deliver me from this body of death?&rdquo; (Rom 7:24). Both express the insider&rsquo;s recognition that existence within the fallen order produces a bondage from which no internal resource can provide escape. The answer Qohelet cannot give (Paul immediately supplies): &ldquo;Thanks be to God through Jesus Christ our Lord&rdquo; (Rom 7:25) — the deliverer who enters the hated life and redeems it."}
    ],
    "24": [
      {"type": "allusion", "target": "1 Tim 4:4",
       "note": "The Preacher&rsquo;s conclusion that eating, drinking, and finding enjoyment in toil is &ldquo;from God&rsquo;s hand&rdquo; (vv24-25) is the wisdom tradition&rsquo;s creaturely-goods theology that Paul develops in 1 Tim 4:4-5: &ldquo;everything created by God is good, and nothing is to be rejected if it is received with thanksgiving, for it is made holy by the word of God and prayer.&rdquo; Both texts insist that the material gifts of created existence are legitimate divine gifts, not escapes from spirituality. Qohelet anchors joy in the Creator; Paul anchors it in the Creator known through Christ."}
    ],
    "26": [
      {"type": "allusion", "target": "Matt 25:29",
       "note": "God gives wisdom, knowledge, and joy to the one who pleases him, but to the sinner the task of gathering and collecting &ldquo;only to give to one who pleases God&rdquo; — the ironic reversal that the sinner&rsquo;s labor ultimately serves the righteous. Jesus&rsquo; parable of the talents ends with the identical principle: &ldquo;to everyone who has, more will be given... but from the one who has not, even what he has will be taken away&rdquo; (Matt 25:29). Qohelet observes this pattern in the wisdom order; Christ anchors it in the eschatological kingdom where the king reallocates all that was gathered apart from him."}
    ]
  },
  "3": {
    "1": [
      {"type": "allusion", "target": "Gal 4:4",
       "note": "The opening &ldquo;for everything there is a season, and a time for every purpose under heaven&rdquo; establishes the theological frame for Galatians 4:4&rsquo;s climactic declaration: &ldquo;but when the fullness of time had come, God sent forth his Son.&rdquo; The <em>pleroma tou chronou</em> (fullness of time) is the appointed kairos within the time-structure Qohelet describes. Every entry in the 3:1-8 catalogue — birth, death, planting, uprooting, mourning, dancing — is the created-order rhythm within which the incarnation is the appointed moment: God&rsquo;s <em>ʿēt</em> entering time to redeem it from within."}
    ],
    "11": [
      {"type": "allusion", "target": "Heb 11:1",
       "note": "&ldquo;He has made everything beautiful in its time. Also, he has put eternity (<em>hāʿōlām</em>) in the human heart, yet in such a way that no one can find out what God has done from beginning to end.&rdquo; The eternity-in-the-heart that cannot fully comprehend divine works is the creational basis for faith as Hebrews defines it: &ldquo;faith is the assurance of things hoped for, the conviction of things not seen&rdquo; (Heb 11:1). The <em>hāʿōlām</em> placed in the human heart creates the structural longing for what lies beyond the <em>hevel</em>-present; faith is the response that names and trusts the one who has placed that eternity there and promises its fulfillment in Christ."},
      {"type": "theme", "target": "Rev 21:5",
       "note": "&ldquo;He has made everything beautiful in its time&rdquo; — the temporal beauty within the creation-order — is the prologue to the eschatological declaration of Rev 21:5: &ldquo;Behold, I am making all things new.&rdquo; What Qohelet observes as time-bound beauty — beautiful in its time but subject to decay — becomes the eternal beauty of the new creation. The &ldquo;beautiful in its time&rdquo; of Eccl 3:11 points forward to the &ldquo;all things new&rdquo; of Rev 21:5, where the time-limitation is finally removed."}
    ],
    "14": [
      {"type": "allusion", "target": "Rev 15:3",
       "note": "&ldquo;Whatever God does endures forever; nothing can be added to it and nothing taken away from it&rdquo; — the divine works&rsquo; permanence is Qohelet&rsquo;s counter-point to the <em>hevel</em> of all creaturely works. Revelation 15:3-4 is the doxological fulfillment: &ldquo;Great and amazing are your deeds, O Lord God the Almighty! Just and true are your ways, O King of the nations!&rdquo; The permanence of divine works that Qohelet asserts as a wisdom observation becomes in Revelation the substance of the new-creation song — the eternal endurance of what God does in Christ."}
    ],
    "17": [
      {"type": "allusion", "target": "Acts 17:31",
       "note": "&ldquo;God will judge the righteous and the wicked, for there is a time for every matter and for every work&rdquo; — the appointed time of divine judgment. Paul at Athens makes the same declaration with its christological specification: &ldquo;he has fixed a day on which he will judge the world in righteousness by a man whom he has appointed; and of this he has given assurance to all by raising him from the dead&rdquo; (Acts 17:31). The <em>ʿēt</em> (appointed time) for judgment that Qohelet affirms in principle, Paul identifies as fixed in Christ&rsquo;s resurrection — the appointed judge has been revealed."}
    ]
  },
  "4": {
    "1": [
      {"type": "allusion", "target": "Rev 6:9",
       "note": "The Preacher&rsquo;s seeing &ldquo;the tears of the oppressed — they had no one to comfort them&rdquo; and the power on the side of the oppressors is the human condition that the Book of Revelation presents in its apocalyptic register. Revelation 6:9-10 shows the souls under the altar crying: &ldquo;O Sovereign Lord, holy and true, how long before you will judge and avenge our blood on those who dwell on the earth?&rdquo; The comforter whom the oppressed lack in Ecclesiastes is the one who will answer the cry under the altar: the coming Judge and King who vindicates."}
    ],
    "9": [
      {"type": "allusion", "target": "Heb 10:24",
       "note": "&ldquo;Two are better than one, because they get a better return for their labor.&rdquo; The relational wisdom of Eccl 4:9-12 — the better return, the mutual help when one falls, the warmth, the defense — is the creational basis for Hebrews&rsquo; call to community: &ldquo;let us consider how to stir up one another to love and good works, not neglecting to meet together, as is the habit of some, but encouraging one another, and all the more as you see the Day drawing near&rdquo; (Heb 10:24-25). The wisdom-observation that companionship multiplies resources becomes, in the eschatological context of Hebrews, the urgent basis for the covenant community&rsquo;s mutual encouragement."},
      {"type": "allusion", "target": "Matt 18:20",
       "note": "&ldquo;Two are better than one&rdquo; — the principle that presence multiplies effect — is given its christological form by Jesus: &ldquo;where two or three are gathered in my name, there am I among them&rdquo; (Matt 18:20). Christ is the third party in every gathering of two, the presence that transforms the better-than-one of creaturely community into the gathering-in-his-name of the covenant assembly. The cord of three strands (v12) finds its third strand in Christ&rsquo;s promised presence with his gathered people."}
    ]
  }
}

def main():
    existing = load_echo('ecclesiastes')
    merge_echo(existing, ECCLESIASTES_ECHOES)
    save_echo('ecclesiastes', existing)
    entries = sum(len(e) for ch in ECCLESIASTES_ECHOES.values() for e in ch.values())
    print(f'Ecclesiastes ch2-4 echoes: {len(ECCLESIASTES_ECHOES)} chapters, {entries} entries written.')

if __name__ == '__main__':
    main()
