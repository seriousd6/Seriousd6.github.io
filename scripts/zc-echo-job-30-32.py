"""
Echo Layer — Job chapters 30–32
Run: python3 scripts/zc-echo-job-30-32.py

Key echo connections in this range:
- 30:9-10: Job mocked, spit upon → Ps 22:6-7; Isa 50:6 (suffering servant despised)
- 30:19: "dust and ashes" → Ps 22:15 (brought to the dust of death)
- 30:20: "I cry but you do not answer" → Ps 22:1-2; Matt 27:46 (cry of dereliction)
- 30:25: "Did I not weep for those in trouble?" → John 11:35; Heb 4:15 (Christ's tears)
- 31:1: covenant with eyes → Matt 5:28 (lust in the heart = adultery)
- 31:13-15: rights of servants, one God formed both → Gal 3:28; Col 4:1
- 31:16-18: care for poor, widow, fatherless → Jas 1:27; Luke 4:18
- 31:19-20: clothing the naked → Matt 25:36
- 31:24-25: gold as hope → Matt 6:24; 1 Tim 6:17
- 31:33: "hidden like Adam" → Gen 3:12; Rom 5:12 (sin through Adam)
- 31:35: "O that the Almighty would answer" → Heb 4:15-16; 9:24 (Christ our advocate)
- 32:8: "Spirit, breath of the Almighty gives understanding" → Gen 2:7; John 3:8; 2 Tim 3:16
- 32:9: "not the great who are always wise" → 1 Cor 1:27; Matt 11:25
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

JOB_ECHO_30_32 = {
  "30": {
    "9": [
      {"type": "allusion", "target": "Ps 22:6", "note": "Job becoming 'their song and their byword' — a subject of contemptuous mockery — runs parallel to Psalm 22:6-7's sufferer who is 'a reproach of men and despised by the people; all who see me mock me.' The Psalmist's cry of abandonment and public humiliation maps onto Job's lament here, and both texts are drawn into the Passion narrative: the mockery at the cross (Matt 27:39-44) echoes both."},
      {"type": "allusion", "target": "Ps 69:11", "note": "Psalm 69:11 — 'I made sackcloth my clothing and became a byword to them' — uses the identical <em>mašāl</em> (byword) vocabulary that Job uses here. Psalm 69 is the most-cited psalm in the Passion narratives; Job's humiliation is drawn into the same trajectory of righteous suffering that the NT applies to Christ."}
    ],
    "10": [
      {"type": "allusion", "target": "Isa 50:6", "note": "Job says those who once depended on him now 'despise me and keep their distance; they do not hesitate to spit in my face' — a precise verbal parallel to the Servant's experience in Isaiah 50:6: 'I offered my back to those who beat me, my cheeks to those who pulled out my beard; I did not hide my face from mocking and spitting.' The reversal of status — the benefactor now mocked and spat upon — is a structural feature that links Job's suffering to the Servant's, and through both to the Passion (Matt 26:67; 27:30)."}
    ],
    "19": [
      {"type": "allusion", "target": "Ps 22:15", "note": "God 'has thrown me into the mud; I have become like dust and ashes' — the dissolution to earth recalls Psalm 22:15's sufferer 'brought to the dust of death,' and both echo the creation curse of Genesis 3:19 ('you are dust and to dust you shall return'). The NT applies Psalm 22 to the crucifixion; Christ's death is the fullest embodiment of the dust-of-death trajectory that both passages describe."},
      {"type": "allusion", "target": "Gen 3:19", "note": "Job's reduction to 'dust and ashes' (the same phrase he uses in Job 42:6) echoes the divine verdict of Genesis 3:19 and the mortality of the dust-creature. Christ's submission to this dust-condition (Phil 2:7-8; John 19:30) is the basis on which resurrection reverses it."}
    ],
    "20": [
      {"type": "allusion", "target": "Ps 22:2", "note": "Job's 'I cry to you but you do not answer; I stand, and you only stare at me' is the experiential core of Psalm 22:2 — 'I cry by day, but you do not answer; by night, but find no rest.' Both texts describe unanswered prayer to a God who has not yet acted. Jesus quotes Psalm 22:1 from the cross (Matt 27:46; Mark 15:34), making Job's prior articulation of this experience of divine silence one of the deepest prefigurations of the cry of dereliction."}
    ],
    "25": [
      {"type": "allusion", "target": "John 11:35", "note": "Job asks, 'Did I not weep for those in trouble? Was not my soul grieved for the poor?' — lamenting that his compassion for others' suffering was not reciprocated. Jesus, who wept at Lazarus's tomb (John 11:35) and over Jerusalem (Luke 19:41), embodies the compassion Job claims and goes further: not merely grieving over the suffering of others but bearing it (Isa 53:4; Heb 4:15)."},
      {"type": "allusion", "target": "Heb 4:15", "note": "Job's record of empathy with the afflicted and grieving — 'my soul was grieved for the needy' — anticipates Hebrews 4:15's claim that Christ is a high priest 'who has been tempted in every way, just as we are' and can 'sympathize with our weaknesses.' Job demonstrates that compassionate suffering is not peripheral to righteous humanity but central to it."}
    ]
  },
  "31": {
    "1": [
      {"type": "allusion", "target": "Matt 5:28", "note": "Job 31:1 — 'I made a covenant with my eyes; how then could I look upon a young woman?' — is the OT anticipation of Jesus's teaching that 'anyone who looks at a woman with lustful intent has already committed adultery with her in his heart' (Matt 5:28). Job's covenant of the eyes grounds sexual morality in intention and the heart, not merely in external act — the same ethical internalization that marks the Sermon on the Mount."}
    ],
    "13": [
      {"type": "allusion", "target": "Col 4:1", "note": "Job's declaration that he attended fairly to the complaints of his servants (vv.13-15) because 'did not the one who made me in the womb make him too?' grounds servant-rights in shared creatureliness before God. Colossians 4:1 and Ephesians 6:9 make the same argument: 'Masters, treat your bondservants justly and fairly, knowing that you also have a Master in heaven.' Job articulates the theological basis — shared Creator — that Paul applies as the basis of Christian household ethics."},
      {"type": "allusion", "target": "Gal 3:28", "note": "The principle that Job grounds in creation — 'one God formed us both in the womb' — is the same basis on which Galatians 3:28 declares 'there is neither slave nor free... for you are all one in Christ Jesus.' The covenant of equal creatureliness Job claims is the principle that Paul says is realized fully in Christ."}
    ],
    "16": [
      {"type": "allusion", "target": "Jas 1:27", "note": "Job's catalogue of care for the vulnerable — not refusing the poor what they need, not causing the widow's eyes to fail (v.16), feeding the fatherless from his table (v.17), clothing the naked (v.19-20) — is the most detailed personal enactment of what James 1:27 calls 'pure religion': to care for orphans and widows in their distress. Job's ethical autobiography constitutes the OT benchmark against which NT social ethics is measured."},
      {"type": "allusion", "target": "Luke 4:18", "note": "Job's record of giving to the poor (v.16), feeding the hungry (v.17), and clothing the naked (v.19) maps directly onto the Isaianic mission statement Jesus claims in Luke 4:18 ('to bring good news to the poor... to set the oppressed free'). Job embodies the Jubilee ethics that the Law commanded; Christ fulfills what Job exemplifies."}
    ],
    "19": [
      {"type": "allusion", "target": "Matt 25:36", "note": "Job's claim that he clothed the naked — 'if I have seen anyone dying from lack of clothing, or any poor person without covering' and provided warmth from his sheep's wool (v.20) — is the OT grounding for Matthew 25:36's 'I was naked and you clothed me.' The judgment on this criterion in Matthew 25 draws on the ethical standard Job claims to have met and that the Law required; Job's personal testimony makes visible what the Sermon's demands look like concretely."}
    ],
    "24": [
      {"type": "allusion", "target": "Matt 6:24", "note": "Job's oath that he has not 'made gold my hope or called pure gold my security' (v.24) nor rejoiced when 'my wealth was great' (v.25) repudiates the materialism that Jesus identifies as the rival lord in Matthew 6:24 ('you cannot serve God and money'). Job's ethical self-examination names the interior disposition — trusting wealth — that Jesus prohibits; Job's negative oath is the OT equivalent of the positive counsel to store treasure in heaven (Matt 6:20)."},
      {"type": "allusion", "target": "1 Tim 6:17", "note": "Job's refusal to set his hope on gold anticipates Paul's instruction to 'those who are rich in this present age not to be haughty, nor to set their hopes on the uncertainty of riches, but on God' (1 Tim 6:17). The posture Job describes — assessing wealth but not resting hope in it — is exactly the disposition the NT calls for."}
    ],
    "26": [
      {"type": "allusion", "target": "Rom 1:23", "note": "Job's oath that he did not 'gaze at the sun in its brilliance or the moon as it moved in splendor' and allow his heart to be 'secretly seduced' to 'kiss his hand toward them' (vv.26-27) is the personal refusal of precisely the sin Romans 1:23 diagnoses: exchanging 'the glory of the immortal God for images' of created things. Job's negative oath against stellar worship demonstrates that the sin Paul identifies as universal idolatry was known, named, and refused by the righteous."}
    ],
    "29": [
      {"type": "allusion", "target": "Matt 5:44", "note": "Job's declaration that he did not 'rejoice when my enemy was ruined, or exult when disaster found him' (v.29) and 'did not let my mouth sin by calling down a curse on his life' (v.30) is the pre-Sermon-on-the-Mount practice of enemy-love. Jesus's 'love your enemies and pray for those who persecute you' (Matt 5:44) does not introduce a new ethical requirement but names explicitly what Job lived implicitly — and what Proverbs 24:17 had already taught."}
    ],
    "33": [
      {"type": "allusion", "target": "Gen 3:12", "note": "Job's oath 'if I have hidden my transgressions like Adam' is the book's most explicit naming of the Adamic dynamic of concealment that began at the Fall (Gen 3:12: Adam hides and deflects blame). Job's covenant of transparency — his willingness to have his life examined before God — contrasts with Adam's reflexive self-protection and anticipates the complete transparency of the one who 'had no sin' (2 Cor 5:21) and concealed nothing."},
      {"type": "allusion", "target": "Rom 5:12", "note": "The explicit 'like Adam' comparison invites the Pauline typology of Romans 5:12-21: sin entered through one man's transgression, and the human default since Eden is the Adamic pattern of concealment. Job's refusal of this pattern — 'I have not hidden my transgression like Adam' — is a partial escape from the Adamic condition that only the Last Adam (1 Cor 15:45) fully overcomes."}
    ],
    "35": [
      {"type": "allusion", "target": "Heb 4:16", "note": "Job's longing — 'O that someone would hear me! Here is my signature — let the Almighty answer me!' (v.35) — is the OT articulation of the need for direct access to God that the law could not provide. Hebrews 4:16 answers Job's wish: 'Let us then with confidence draw near to the throne of grace, that we may receive mercy and find grace.' Christ as the intercessor-advocate who hears and answers is the response to Job's unanswered longing for an answerer."},
      {"type": "allusion", "target": "Heb 9:24", "note": "Job desires that his 'accuser had written out his charge' — he wants the indictment in writing so he can answer it (v.35-36). Hebrews 9:24 presents Christ as the one who 'entered heaven itself, now to appear in the presence of God on our behalf' — the advocate before the divine court that Job longs for but cannot access under the old covenant. Job's courtroom metaphor is fulfilled in the heavenly high priesthood."}
    ],
    "38": [
      {"type": "allusion", "target": "Gen 4:10", "note": "Job's closing oath that 'if my land has cried out against me and its furrows have wept' (v.38) invokes land-as-witness language that echoes Genesis 4:10: 'your brother's blood cries out to me from the ground.' The land that absorbs innocent blood speaks against the perpetrator; Job's oath invites this testimony against himself if guilty. The land-witness motif recurs in the prophets and anticipates Romans 8:22 (creation groaning under the weight of human sin)."}
    ]
  },
  "32": {
    "8": [
      {"type": "allusion", "target": "Gen 2:7", "note": "Elihu's declaration that 'it is the Spirit (<em>rûaḥ</em>) in a person — the breath (<em>nišmat</em>) of the Almighty — that gives them understanding' draws on the creation language of Genesis 2:7, where God breathes the <em>nišmat ḥayyîm</em> (breath of life) into the dust-creature. Wisdom is not a human achievement but a divine bestowal — a claim that John 3:8 (the Spirit blows where it wills) and 1 Corinthians 2:10-12 develop: the Spirit alone searches and reveals the deep things of God."},
      {"type": "allusion", "target": "2 Tim 3:16", "note": "Elihu's claim that the Spirit of the Almighty gives understanding to human beings is the structural principle behind the NT doctrine of inspiration: 2 Timothy 3:16's <em>theopneustos</em> (God-breathed) and 2 Peter 1:21 ('men spoke from God as they were carried along by the Holy Spirit') build on this conviction that genuine wisdom has a divine breath-source. Elihu's statement anticipates that the same Spirit who animates and gives understanding is the Spirit of prophecy."}
    ],
    "9": [
      {"type": "allusion", "target": "1 Cor 1:27", "note": "Elihu's observation that 'it is not the great who are always wise, nor the aged who always understand what is right' echoes the wisdom-inversion that Paul celebrates in 1 Corinthians 1:27: 'God chose what is foolish in the world to shame the wise.' Both passages challenge the equation of social status or experience with divinely-granted understanding. This inversion is embodied in Jesus, who revealed his teaching 'to little children' rather than the wise (Matt 11:25)."},
      {"type": "allusion", "target": "Matt 11:25", "note": "Elihu's challenge to the assumption that age equals wisdom ('it is not the great who are always wise') anticipates Jesus's thanksgiving prayer that God 'has hidden these things from the wise and learned, and revealed them to little children' (Matt 11:25). The Spirit-dispensed understanding of Job 32:8 is independent of social credentials — a point the incarnation demonstrates fully."}
    ],
    "18": [
      {"type": "allusion", "target": "Luke 5:37", "note": "Elihu's image of being 'full of words' compelled to burst out — 'my belly is like wine with no outlet — like new wineskins about to burst' (vv.18-19) — uses the same wineskin-and-new-wine imagery that Jesus deploys in Luke 5:37-38 (and Mark 2:22; Matt 9:17). In Jesus's context the new wine is the kingdom's reality that cannot be contained in old-covenant structures; Elihu's image captures the Spirit-compelled necessity of proclamation that the NT associates with the new-covenant Spirit."}
    ],
    "21": [
      {"type": "allusion", "target": "Acts 10:34", "note": "Elihu's declaration 'I will show partiality to no one, nor will I flatter anyone' (vv.21-22), grounded in accountability to his Maker, anticipates Peter's declaration in Acts 10:34 that 'God shows no partiality' and the NT ethical injunction of impartiality (Jas 2:1-9; Rom 2:11). The OT grounding of impartiality in Creator-accountability is the same foundation the NT builds on."}
    ]
  }
}

def main():
    existing = load_echo('job')
    merge_echo(existing, JOB_ECHO_30_32)
    save_echo('job', existing)
    chs = sum(1 for ch in ['30','31','32'] if ch in JOB_ECHO_30_32)
    print(f'Job 30-32 echoes written ({chs} chapters)')

if __name__ == '__main__':
    main()
