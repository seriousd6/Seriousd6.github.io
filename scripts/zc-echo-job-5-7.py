"""
Echo Layer — Job chapters 5–7
Run: python3 scripts/zc-echo-job-5-7.py

Key echo connections in this range:
- 5:7: born to trouble as sparks fly upward → Rom 5:12 (Adamic inheritance of suffering)
- 5:9: great and unsearchable things → Rom 11:33 (depth of God's wisdom)
- 5:11: lifts up the lowly → Luke 1:52 (Magnificat); Jas 4:10
- 5:13: catches the wise in their craftiness → 1 Cor 3:19 (already present)
- 5:17: blessed is the one God reproves → Heb 12:5-6 (the Lord disciplines those he loves)
- 5:18: wounds and then bandages → Hos 6:1; 1 Pet 2:24 (by his wounds you have been healed)
- 6:4: Almighty's arrows lodged in me → Ps 38:2; the lament of the afflicted innocent
- 6:14: despairing person deserves hesed from a friend → John 15:13 (greater love)
- 6:15-17: treacherous brooks that fail → Jer 15:18; John 4:14 (water that never fails)
- 7:1: hard service on earth like a hired worker → Mark 10:45 (Son of Man as servant)
- 7:7: my life is a breath → Jas 4:14 (you are a mist)
- 7:17-18: What is man that you should make so much of him? → Ps 8:4; Heb 2:6-9
- 7:21: Why not pardon my sin? → Matt 26:28; Heb 9:22 (forgiveness through blood)
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

JOB_ECHO_5_7 = {
  "5": {
    "7": [
      {"type": "allusion", "target": "Rom 5:12", "note": "&#8220;People are born to trouble as naturally as sparks fly upward&#8221; — Eliphaz&#8217;s observation about the universality of human suffering resonates with Paul&#8217;s theological account in Romans 5:12: &#8220;sin entered the world through one man, and death through sin, and in this way death spread to all people&#8221;; Eliphaz intends the maxim as a rebuke to Job (suffering is natural, not exceptional), but the deeper truth he accidentally voices is that human life under the fall is structurally oriented toward affliction — the very condition that Christ assumes and transforms in the incarnation"}
    ],
    "9": [
      {"type": "allusion", "target": "Rom 11:33", "note": "&#8220;Who does great and unsearchable things, marvellous things beyond counting&#8221; — Eliphaz&#8217;s doxology of divine inscrutability is the OT cognate of Paul&#8217;s climactic exclamation in Romans 11:33: &#8220;Oh, the depth of the riches of the wisdom and knowledge of God! How unsearchable his judgments, and his ways beyond tracing out!&#8221;; both texts invoke the category of divine &#8220;unsearchableness&#8221; (<em>ḥēqer</em>; Gk. <em>anexeraunētos</em>) as the proper response to encountering the limits of human wisdom about God&#8217;s ways — a category that Job will himself deploy against his friends"}
    ],
    "11": [
      {"type": "allusion", "target": "Luke 1:52", "note": "&#8220;Who lifts up the lowly on high, and raises those in mourning to safety&#8221; — Eliphaz&#8217;s description of YHWH&#8217;s reversal of social conditions is the OT pattern behind Mary&#8217;s Magnificat: &#8220;He has brought down rulers from their thrones but has lifted up the humble&#8221; (Luke 1:52); both texts frame God&#8217;s character as constitutively committed to reversal — the lowly exalted, the mourning raised — a pattern that reaches its ultimate expression in the resurrection of the crucified Son"}
    ],
    "15": [
      {"type": "allusion", "target": "Luke 4:18", "note": "&#8220;He saves the poor from the cutting words of their enemies and from the grip of the powerful&#8221; — the deliverance of the poor and powerless from oppressive speech and exploitation is the content of the jubilee proclamation that Jesus announces at Nazareth: &#8220;The Spirit of the Lord is on me, because he has anointed me to proclaim good news to the poor&#8221; (Luke 4:18); YHWH&#8217;s character as defender of the poor and silencer of injustice (5:16) is the ground on which Christ&#8217;s mission stands"}
    ],
    "17": [
      {"type": "allusion", "target": "Heb 12:5", "note": "&#8220;See, blessed is the person whom God reproves; do not despise the discipline (<em>mûsar</em>) of the Almighty&#8221; — Eliphaz quotes a wisdom tradition about divine discipline; Hebrews 12:5-6 cites the parallel in Proverbs 3:11-12 to interpret Christian suffering: &#8220;do not make light of the Lord&#8217;s discipline... because the Lord disciplines the one he loves&#8221;; the irony is that Eliphaz intends this as an accusation (Job is being disciplined because he sinned), while Hebrews applies it as comfort; the same text functions differently depending on whether the sufferer is genuinely guilty or innocent as Job is"}
    ],
    "18": [
      {"type": "allusion", "target": "Hos 6:1", "note": "&#8220;For he wounds and then bandages; he strikes down and his own hands heal&#8221; — this is the exact logic of Hosea 6:1: &#8220;Come, let us return to the LORD. He has torn us to pieces but he will heal us; he has injured us but he will bind up our wounds&#8221;; both texts describe a YHWH who is the source of both wound and healing, and both invite a response of trust and return; the pattern reaches its christological apex in 1 Peter 2:24: &#8220;by his wounds you have been healed&#8221; — the wound that Christ bears is the one that heals"},
      {"type": "allusion", "target": "1 Pet 2:24", "note": "&#8220;He wounds and then bandages... his own hands heal&#8221; — the divine pattern of wound-and-healing that Eliphaz describes abstractly is enacted concretely in the crucifixion: &#8220;He himself bore our sins in his body on the cross, so that we might die to sins and live for righteousness; by his wounds you have been healed&#8221; (1 Pet 2:24); 1 Peter 2:24 cites Isaiah 53:5 but the Job 5:18 pattern is the earlier wisdom articulation of the same theological principle — the healer suffers in order to heal"}
    ],
    "26": [
      {"type": "allusion", "target": "1 Cor 15:37", "note": "&#8220;You will come to your grave in ripe old age, like a sheaf of grain harvested in its proper season&#8221; — the agricultural image of the grain harvested at its proper time is the OT seed of Paul&#8217;s resurrection argument in 1 Corinthians 15:37-38: &#8220;what you sow does not come to life unless it dies... God gives it a body as he has determined, and to each kind of seed he gives its own body&#8221;; the grain harvested at the right season becomes, through the resurrection metaphor, the seed that must die before it comes to life in a transformed body"}
    ]
  },
  "6": {
    "4": [
      {"type": "allusion", "target": "Ps 38:2", "note": "&#8220;The Almighty&#8217;s arrows are lodged in me; my spirit is drinking their venom; the terrors of God are lined up against me&#8221; — Job&#8217;s image of divine arrows recalls Psalm 38:2: &#8220;your arrows have sunk into me, and your hand has come down on me&#8221;; both texts use the arrow image for the affliction that comes directly from God&#8217;s hand on the sufferer — not random suffering but aimed suffering; Psalm 38 is David&#8217;s lament in illness and abandonment, creating a pattern of royal suffering that points toward the Passion narrative"},
      {"type": "allusion", "target": "Ps 22:1", "note": "Job&#8217;s &#8220;terrors of God are lined up against me&#8221; opens the pattern of innocent suffering under God&#8217;s perceived assault that Psalm 22 voices most fully: &#8220;My God, my God, why have you forsaken me? Why are you so far from saving me?&#8221; (Ps 22:1); both Job and Psalm 22 stage the experience of the righteous sufferer who perceives God as hostile rather than absent — the precise experience that Christ enacts on the cross when he cries Ps 22:1 from the darkness of Golgotha"}
    ],
    "14": [
      {"type": "allusion", "target": "John 15:13", "note": "&#8220;The despairing person deserves steadfast love (<em>ḥeseḏ</em>) from a friend; to withhold it is to forsake the fear of the Almighty&#8221; — Job identifies <em>ḥeseḏ</em> as what friendship owes to the suffering; John 15:13 defines the ultimate expression of this love: &#8220;Greater love has no one than this: to lay down one&#8217;s life for one&#8217;s friends&#8221;; where Job&#8217;s friends withhold the covenant loyalty that suffering demands, Christ enacts it in its fullest form — not merely sympathizing with the suffering but entering into death on their behalf"}
    ],
    "15": [
      {"type": "allusion", "target": "Jer 15:18", "note": "&#8220;My brothers are as treacherous as a seasonal brook, like watercourses that flow away&#8221; — Job&#8217;s image of the wadi that promises water but vanishes in summer heat is also Jeremiah&#8217;s complaint about God himself in Jeremiah 15:18: &#8220;Why is my pain unending and my wound grievous and incurable? You are to me like a deceptive brook, like a spring that fails.&#8221; Both Job and Jeremiah use the same image — the <em>naḥal ʾākzāḇ</em> (treacherous brook) — to describe the experience of unfulfilled expectation in crisis; the suffering prophet and the suffering patriarch share the same rhetorical vocabulary for abandonment"}
    ],
    "17": [
      {"type": "allusion", "target": "John 4:14", "note": "The seasonal brookes that &#8220;disappear when the heat comes&#8221; — the image of water that satisfies temporarily but ultimately fails — is the foil that Jesus&#8217; offer in John 4:14 explicitly addresses: &#8220;but whoever drinks the water I give them will never thirst. Indeed, the water I give them will become in them a spring of water welling up to eternal life.&#8221; Job&#8217;s friends are the human form of the failing brook; Christ is the permanently flowing spring — the <em>ḥeseḏ</em> that Job&#8217;s friends withheld, given freely and inexhaustibly"}
    ],
    "27": [
      {"type": "allusion", "target": "John 19:24", "note": "&#8220;You would cast lots (<em>tappîlû ʿal-yāṯôm</em>) over an orphan and sell out your friend&#8221; — Job accuses his friends of treating him like an orphan to be disposed of, using the lot-casting image for callous allocation; the lot-casting that reduces the vulnerable person to a commodity appears in its starkest form at the crucifixion: &#8220;they divided my clothes among them and cast lots for my garment&#8221; (John 19:24 citing Ps 22:18); the reduction of the suffering innocent to a series of property transactions — Job&#8217;s estate was already stripped — anticipates the stripping and lotting of Christ"}
    ]
  },
  "7": {
    "1": [
      {"type": "allusion", "target": "Mark 10:45", "note": "&#8220;Does not man have hard service (<em>ṣāḇāʾ</em>) on earth, and are not his days like those of a hired worker?&#8221; — <em>ṣāḇāʾ</em> is the word for military service and the compulsory labour of the covenant people; Job&#8217;s description of human life as hard service under a demanding master is the experiential underside of what Christ voluntarily enters: &#8220;the Son of Man came not to be served but to serve, and to give his life as a ransom for many&#8221; (Mark 10:45); the <em>ṣāḇāʾ</em> that Job endures as an unwilling conscript, Christ takes on as a willing servant"}
    ],
    "7": [
      {"type": "allusion", "target": "Jas 4:14", "note": "&#8220;Remember that my life is but a breath (<em>rûaḥ</em>); my eyes will never again see happiness&#8221; — Job&#8217;s lament that life is a <em>rûaḥ</em> (breath/wind) is the OT source of James 4:14: &#8220;What is your life? You are a mist (<em>atmis</em>) that appears for a little while and then vanishes.&#8221; Both texts use the brevity of life as a theological pressure point — in James, as a warning against presumptuous planning; in Job, as a cry of grief; in both, the transience of human life calls for either humility or lament rather than self-sufficient confidence"}
    ],
    "9": [
      {"type": "allusion", "target": "Acts 1:11", "note": "&#8220;As a cloud vanishes and is gone, so the one who descends to Sheol does not come up&#8221; — Job asserts, from within his suffering, the finality of death: no return from Sheol; the &#8220;he will never return home&#8221; of verse 10 voices the pre-resurrection impossibility that the disciples experienced after the crucifixion; Acts 1:11 is the answer to Job 7:9 — &#8220;this same Jesus, who has been taken from you into heaven, will come back in the same way you have seen him go&#8221;; the one who descended into death (Acts 2:27 cites Ps 16:10) did not remain in Sheol; the exception that Job cannot imagine becomes the ground of Christian hope"}
    ],
    "11": [
      {"type": "allusion", "target": "Rom 8:26", "note": "&#8220;I will speak in the anguish of my spirit (<em>bᵉṣar rûḥî</em>) and complain in the bitterness of my soul&#8221; — Job&#8217;s decision to voice his suffering rather than suppress it is the OT form of what Paul&#8217;s pneumatology makes possible for the suffering believer: &#8220;the Spirit himself intercedes for us through wordless groans (<em>stenagmois alaletois</em>)&#8221; (Rom 8:26); Job&#8217;s anguished speech and the Spirit&#8217;s inexpressible groaning are on the same theological continuum — both assert that the suffering of the righteous reaches God as genuine prayer, not as faithless complaint"}
    ],
    "12": [
      {"type": "allusion", "target": "Matt 8:26", "note": "&#8220;Am I the sea, or a sea monster (<em>tannîn</em>), that you place a guard over me?&#8221; — Job protests that God treats him as a cosmic enemy requiring surveillance and restraint; the same sea and <em>tannîn</em> (chaos-dragon) imagery appears throughout the Psalms as what YHWH has already defeated (Ps 74:13-14; 89:9-10); Jesus&#8217; rebuking of the sea in Matthew 8:26 (&#8220;he rebuked the winds and the waves, and it was completely calm&#8221;) demonstrates his authority over precisely the chaotic force Job is accused of being; Christ is not the guard over the sea — he is the one who commands it"}
    ],
    "17": [
      {"type": "allusion", "target": "Ps 8:4", "note": "&#8220;What is man, that you should make so much of him, and that you fix your attention on him — testing him every morning, examining him every moment?&#8221; — Job&#8217;s complaint about divine scrutiny inverts Psalm 8:4: &#8220;what is mankind that you are mindful of him, human beings that you care for them?&#8221; (Ps 8:4); the same question — why does God pay such close attention to human beings? — carries opposite tones: in Psalm 8, wonder and gratitude; in Job 7, dread and exhaustion; the distance between the two uses of the same question maps the distance between creation&#8217;s ideal and the fall&#8217;s reality"},
      {"type": "allusion", "target": "Heb 2:6", "note": "&#8220;What is man, that you should make so much of him?&#8221; — Hebrews 2:6-9 quotes Psalm 8:4-6 and applies it christologically: &#8220;But we do see Jesus, who was made lower than the angels for a little while, now crowned with glory and honor because he suffered death&#8221; (Heb 2:9); the question Job voices in anguish — why does God attend so closely to a human being? — receives its ultimate answer in the incarnation: God fixes his attention on humanity because he has become human, taking the full weight of Job&#8217;s condition upon himself"}
    ],
    "21": [
      {"type": "allusion", "target": "Matt 26:28", "note": "&#8220;Why do you not pardon my offense and forgive my sin? For soon I shall lie down in the dust; you will search for me, but I will be gone.&#8221; — Job&#8217;s plea for forgiveness before death is the OT anticipation of the question the NT answers: why can God not simply pardon? Because the moral weight of sin requires a satisfaction that maintains justice while extending mercy; Matthew 26:28 is the answer: &#8220;this is my blood of the covenant, which is poured out for many for the forgiveness of sins&#8221; — the pardon Job asks for is made available through the One who lay in the dust (Ps 22:15) and rose, carrying the answer to Job&#8217;s plea in his own resurrection"},
      {"type": "allusion", "target": "Heb 9:22", "note": "&#8220;Why do you not pardon my offense?&#8221; — Job&#8217;s question assumes that forgiveness is an arbitrary divine choice; Hebrews 9:22 reveals the constraint: &#8220;without the shedding of blood there is no forgiveness.&#8221; The theological answer to Job&#8217;s plea is not that God is unwilling but that the mechanism for forgiveness — the priestly sacrifice that provides the blood for atonement — had not yet been provided; what Job begs for from within the old covenant economy is what Hebrews declares available through Christ&#8217;s once-for-all offering"}
    ]
  }
}

def main():
    existing = load_echo('job')
    merge_echo(existing, JOB_ECHO_5_7)
    save_echo('job', existing)
    print('Job 5-7 echo layer written.')

if __name__ == '__main__':
    main()
