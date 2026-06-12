"""
Echo Commentary — 2 Samuel chapters 12–13
Run: python3 scripts/zc-echo-2samuel-12-13.py

Ch12: Nathan's parable — the penetrating word of God; David's confession and
      immediate forgiveness; the child's death and David's hope of reunion
Ch13: Amnon and Tamar — the hardened heart that refuses the voice; the desolation
      of the innocent in the corruption of the royal house

Key OT↔NT echo connections:
- 12:7 → Heb 4:12-13: the word of God that pierces and exposes
- 12:13 → 1 John 1:9 / Rom 4:7-8: confession and immediate divine forgiveness
- 12:23 → 1 Thess 4:13-14 / John 11:25: &lsquo;I shall go to him&rsquo; — resurrection hope
- 13:14 → Heb 3:15 / John 10:27: the hardened heart that refuses to hear the voice
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

ECHO = {
  "12": {
    "7": [
      {"type": "allusion", "target": "Heb 4:12-13", "note": "Nathan's sudden turn — 'You are the man!' (ʾattāh hāʾîš) — is the OT's most dramatic demonstration of the word of God as a double-edged sword that penetrates all disguise. David had heard the parable as a neutral judge and passed sentence on the rich man, not realizing the word was aimed at himself. Heb 4:12-13 describes exactly this dynamic: 'the word of God is living and active, sharper than any two-edged sword, piercing to the division of soul and spirit... discerning the thoughts and intentions of the heart. And no creature is hidden from his sight.' Nathan's ʾattāh hāʾîš is the pre-eminent OT instance of the word that strips away self-justification and reveals the sinner to himself."},
      {"type": "allusion", "target": "John 16:8", "note": "Nathan functions here as the type of the Spirit's convicting work described in John 16:8: 'he will convict the world concerning sin and righteousness and judgment.' The prophet who comes from outside the king's self-perception and speaks the one sentence that brings the entire edifice of self-deception crashing down — this is the pattern of the Spirit's conviction, which does not merely inform but pierces, bringing the hearer to the crisis of repentance."}
    ],
    "13": [
      {"type": "allusion", "target": "1 John 1:9", "note": "David's immediate confession — 'I have sinned against YHWH' (ḥāṭāʾtî laYHWH) — and Nathan's equally immediate absolution — 'YHWH has also put away your sin; you shall not die' — establish the OT pattern that 1 John 1:9 makes explicit: 'if we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.' The speed of the forgiveness — no waiting period, no penance cycle, no delayed verdict — reflects the character of YHWH as the God who forgives in response to the contrite confession. Psalm 32 (David's own meditation on this event) is the OT's fullest exposition: 'when I acknowledged my sin... you forgave the iniquity of my sin' (Ps 32:5)."},
      {"type": "allusion", "target": "Rom 4:6-8", "note": "Paul cites Psalm 32 in Romans 4:6-8 as the paradigmatic OT case of imputed righteousness: 'Blessed is the one against whom the Lord will not count his sin' (Ps 32:2, quoting David). The Nathan/David exchange in 2 Sam 12:13 is the narrative event that underlies David's psalm, which Paul then deploys as the OT proof that justification is by faith apart from works — the king who committed adultery and murder receives forgiveness not by reparation but by confession before YHWH, the divine word declaring him forgiven."}
    ],
    "23": [
      {"type": "allusion", "target": "1 Thess 4:13-14", "note": "David's statement after the child's death — 'I shall go to him, but he will not return to me' — is the OT's clearest personal expression of hope for future reunion with the departed. The direction of travel is asymmetric: the dead cannot return to the living, but the living will go to the dead through their own death. Paul's argument in 1 Thess 4:13-14 builds on exactly this OT structure: 'we do not want you to be uninformed about those who are asleep, that you may not grieve as others do who have no hope' — the hope is not that they will return but that 'God will bring with him those who have fallen asleep.' David's hope is the implicit OT anticipation that Paul makes explicit in the resurrection."},
      {"type": "allusion", "target": "John 11:25", "note": "David's 'I shall go to him' is the OT's implicit affirmation of life beyond death that Jesus makes explicit in John 11:25: 'I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live.' David's confidence in going to his son — not merely as a statement of mortality but as a statement of hope — is the pre-resurrection expression of the faith that Jesus confirms and grounds in his own person. Where David could only express the direction of hope, Jesus declares himself to be the foundation of that hope."}
    ]
  },
  "13": {
    "14": [
      {"type": "allusion", "target": "Heb 3:15", "note": "The narrator's description of Amnon — 'he would not listen to her voice' (lōʾ ʾābāh lišmōaʿ bəqōlāh) — is the paradigm of the hardened heart that refuses the counsel of righteousness. Hebrews 3:15, citing Psalm 95, applies the same pattern to the hearing of Christ's voice: 'Today, if you hear his voice, do not harden your hearts as in the rebellion.' Amnon's refusal of Tamar's voice is the narrative type of the hardening-against-the-voice that Hebrews warns against — the person who hears and refuses, not from ignorance but from desire stronger than conscience."},
      {"type": "allusion", "target": "John 10:27", "note": "Amnon's refusal to hear Tamar's voice — she speaks wisdom and offers a way of escape (v13) but he will not hear — is the negative image of John 10:27: 'my sheep hear my voice, and I know them, and they follow me.' The one who belongs to the shepherd hears and follows; the one who does not belong refuses the voice even when it speaks their good. Amnon's lōʾ ʾābāh lišmōaʿ bəqōlāh (he was not willing to listen to her voice) is the OT narrative portrait of the one who, in John's terms, does not belong to the flock."}
    ]
  }
}

def main():
    e = load_echo('2samuel')
    merge_echo(e, ECHO)
    save_echo('2samuel', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'2samuel echo: wrote {count} verses across ch 12-13')

if __name__ == '__main__':
    main()
