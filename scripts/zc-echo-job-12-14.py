"""
Echo Layer — Job chapters 12–14
Run: python3 scripts/zc-echo-job-12-14.py

Key echo connections in this range:
- 12:9: only use of YHWH in Job's speeches → Rom 1:20 (creation bears witness)
- 12:10: life of every creature in God's hand → Acts 17:28 (in him we live)
- 12:13: wisdom and strength with God → Col 2:3 (treasures of wisdom in Christ)
- 12:17: he turns counselors to fools → 1 Cor 1:20 (foolishness of the wise)
- 12:22: brings deep things to light → 1 Cor 4:5; Dan 2:22
- 13:3: I want to argue my case before God → Heb 10:19-22 (boldness to enter)
- 13:15: though he kills me, yet I will hope → Hab 3:17-18; Rom 8:38-39
- 13:24: why do you hide your face? → Ps 22:24; Matt 27:46 (God's face turns at cross)
- 14:1-2: man comes up like a flower and wilts → 1 Pet 1:24; Jas 1:10
- 14:4: who can bring pure from impure? → John 3:6; Rom 3:23
- 14:7-9: hope for a tree cut down to sprout → John 12:24; 1 Cor 15:36-37
- 14:12: man lies down and does not rise UNTIL... → 1 Cor 15:20-22; 1 Thess 4:16
- 14:13-15: "if a man dies, will he live again?" — proto-resurrection → John 5:28-29
- 14:17: transgression sealed up → contrast Col 2:14 (record of debt nailed to cross)
- 14:19: you wash away the hope of man → contrast Heb 6:19 (hope as anchor)
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

JOB_ECHO_12_14 = {
  "12": {
    "9": [
      {"type": "allusion", "target": "Rom 1:20", "note": "&#8220;Who among all these does not know that the hand of the LORD has done this?&#8221; — this is the only occurrence of the divine name YHWH in all of Job&#8217;s speeches; it emerges in a natural-theology argument: the animals, birds, earth, and fish all testify to God&#8217;s sovereign action; Romans 1:20 articulates the same principle: &#8220;For since the creation of the world God&#8217;s invisible qualities — his eternal power and divine nature — have been clearly seen, being understood from what has been made&#8221;; Job&#8217;s appeal to creation as witness to the Creator is proto-Pauline natural theology deployed against friends who claim to have a monopoly on divine knowledge"}
    ],
    "10": [
      {"type": "allusion", "target": "Acts 17:28", "note": "&#8220;In his hand is the life of every living creature and the breath of all human flesh&#8221; — Job&#8217;s declaration that all life is held in God&#8217;s hand is the OT basis for Paul&#8217;s Areopagus sermon: &#8220;for in him we live and move and have our being&#8221; (Acts 17:28); both texts assert absolute creaturely dependence on God for the continuation of life itself — the <em>nepheš</em> (life/breath) of all creatures is not self-sustaining but held as a continuous gift; this is the ground both Job&#8217;s suffering and Christ&#8217;s incarnation stand on: God holds life, and therefore can both take it and give it back"}
    ],
    "13": [
      {"type": "allusion", "target": "Col 2:3", "note": "&#8220;With God are wisdom and strength; he has counsel and understanding&#8221; — Job&#8217;s description of God as the exclusive possessor of <em>ḥokmāh ûgᵉḇûrāh</em> (wisdom and might) is the background for Paul&#8217;s declaration in Colossians 2:3 that in Christ &#8220;are hidden all the treasures of wisdom and knowledge&#8221;; what Job attributes to God in the abstract, the NT locates specifically in the person of Christ — the wisdom that transcends all human counsel is not a divine attribute at a distance but a person who has entered human history"},
      {"type": "allusion", "target": "1 Cor 1:24", "note": "&#8220;With God are wisdom and strength&#8221; — the pairing of divine wisdom and power that Job describes becomes Paul&#8217;s description of Christ in 1 Corinthians 1:24: &#8220;Christ the power of God and the wisdom of God&#8221; (<em>Christon theou dynamin kai theou sophian</em>); the wisdom that Eliphaz and his friends claim to possess, and that Job insists belongs only to God, is identical with the crucified Christ — &#8220;who became for us wisdom from God&#8221; (1:30)"}
    ],
    "17": [
      {"type": "allusion", "target": "1 Cor 1:20", "note": "&#8220;He leads counselors away stripped of dignity and turns judges into fools&#8221; — Job&#8217;s doxology of divine sovereignty over human wisdom — stripping advisors, overturning the trusted — is the OT precedent for Paul&#8217;s question in 1 Corinthians 1:20: &#8220;Where is the wise person? Where is the teacher of the law? Where is the philosopher of this age? Has not God made foolish the wisdom of the world?&#8221;; both texts assert the same pattern: divine action renders human wisdom-claims absurd, and the &#8220;foolishness&#8221; of the gospel (the crucified Christ) is wiser than all human counsel"}
    ],
    "22": [
      {"type": "allusion", "target": "1 Cor 4:5", "note": "&#8220;He brings to light the deep things hidden in darkness and brings the shadow of death into the open&#8221; — Job&#8217;s description of God as the revealer of hidden things anticipates Paul&#8217;s eschatological statement in 1 Corinthians 4:5: &#8220;he will bring to light what is hidden in darkness and will expose the motives of the heart&#8221;; both texts use the same illumination-of-hidden-things pattern for divine disclosure, though Job deploys it about the present world&#8217;s hidden governance, while Paul applies it to the judgment that is coming"},
      {"type": "allusion", "target": "Dan 2:22", "note": "&#8220;He brings to light the deep things hidden in darkness&#8221; — Daniel 2:22 uses the same language in a doxology: &#8220;He reveals deep and hidden things; he knows what lies in darkness, and light dwells with him&#8221;; both Job and Daniel praise God for his access to what is concealed — the <em>ʿᵃmîqāṯāʾ ûmistᵃrāṯāʾ</em> of Dan 2:22 and the <em>nistārôṯ</em> of Job 12:22; in both cases, the hidden things belong to suffering contexts where God&#8217;s knowledge of the concealed is the only ground of hope"}
    ],
    "25": [
      {"type": "allusion", "target": "John 1:5", "note": "&#8220;They grope in the dark without light, and he makes them stagger like drunkards&#8221; — Job&#8217;s description of God removing understanding from rulers so they wander blindly in darkness is the reverse image of John 1:5: &#8220;The light shines in the darkness, and the darkness has not overcome it&#8221;; the darkness Job describes — powerful people stumbling without divine illumination — is the condition that the incarnation addresses; the world&#8217;s leaders groping in darkness is the OT picture of human existence that Christ as <em>phōs tou kosmou</em> (light of the world) enters to address"}
    ]
  },
  "13": {
    "3": [
      {"type": "allusion", "target": "Heb 10:19", "note": "&#8220;I want to speak directly to the Almighty; I long to argue my case before God&#8221; — Job&#8217;s longing to approach God directly, bypassing inadequate human mediators, is the OT form of what Hebrews 10:19-22 declares available through Christ: &#8220;we have confidence to enter the Most Holy Place by the blood of Jesus... let us draw near to God with a sincere heart and with the full assurance that faith brings&#8221;; what Job desperately desires — unmediated access to the divine presence — is exactly what Christ&#8217;s high priesthood provides; the barrier that made Job&#8217;s direct approach terrifying is the barrier Christ&#8217;s death removes"}
    ],
    "7": [
      {"type": "allusion", "target": "John 14:6", "note": "&#8220;Will you speak falsehood on God&#8217;s behalf? Will you tell lies for his sake?&#8221; — Job accuses his friends of theological deception: they construct a false account of God&#8217;s ways to defend God&#8217;s honor; John 14:6 presents the contrast — &#8220;I am the way and the truth and the life&#8221; — in the one who is himself the truth, no advocacy requires distortion; where the friends manufacture theological justifications for God, Christ embodies the truth that makes distortion unnecessary; the friends&#8217; &#8220;pious lies&#8221; are the negative image of Christ&#8217;s truthful mediation"}
    ],
    "15": [
      {"type": "allusion", "target": "Hab 3:17", "note": "&#8220;Though he kills me, yet I will hope in him&#8221; — Job&#8217;s declaration of hope against all evidence of God&#8217;s hostility is the most direct OT parallel to Habakkuk 3:17-18: &#8220;Though the fig tree does not blossom and there are no grapes on the vines...yet I will rejoice in the LORD, I will be joyful in God my Savior&#8221;; both texts formulate hope as a defiant act of the will in the face of circumstances that contradict it — hope not grounded in present evidence but in the character of God that transcends current experience"},
      {"type": "allusion", "target": "Rom 8:38", "note": "&#8220;Though he kills me, yet I will hope in him&#8221; — the absolute and unconditional nature of Job&#8217;s hope even through death is the OT anticipation of Paul&#8217;s climactic declaration in Romans 8:38-39: &#8220;I am convinced that neither death nor life... nor anything else in all creation will be able to separate us from the love of God that is in Christ Jesus our Lord&#8221;; Job&#8217;s hope that not even death can sever his relationship with God is what the resurrection of Christ grounds as certainty rather than mere aspiration"}
    ],
    "16": [
      {"type": "allusion", "target": "Heb 12:14", "note": "&#8220;This itself will be my deliverance — no godless man can stand in his presence&#8221; — Job&#8217;s confidence that only the genuinely righteous can stand before God is the OT form of Hebrews 12:14: &#8220;without holiness no one will see the Lord&#8221;; Job&#8217;s claim to be able to stand before God is not arrogance but a declaration of integrity; the NT grounds this confidence not in Job&#8217;s own record but in Christ&#8217;s righteousness imputed to those who trust him — the ones who &#8220;stand before God&#8221; in Revelation 7:9 are those who have &#8220;washed their robes and made them white in the blood of the Lamb&#8221;"}
    ],
    "24": [
      {"type": "allusion", "target": "Matt 27:46", "note": "&#8220;Why do you hide your face from me and treat me as your enemy?&#8221; — Job&#8217;s experience of God as adversary rather than defender, his face hidden from the innocent sufferer, is the OT pattern that reaches its apex in the cry of dereliction: &#8220;My God, my God, why have you forsaken me?&#8221; (Matt 27:46 citing Ps 22:1); the divine face-hiding that Job experiences as inexplicable becomes, at the cross, theologically necessary — God turns his face from Christ precisely because Christ has taken on the full weight of human guilt; what Job suffers without explanation, Christ suffers as the explanation"},
      {"type": "allusion", "target": "Ps 22:24", "note": "&#8220;Why do you hide your face from me?&#8221; — the hidden face of God in suffering is answered in Psalm 22:24: &#8220;he has not despised or scorned the suffering of the afflicted one; he has not hidden his face from him but has listened to his cry for help&#8221;; the same psalm that Jesus cites from the cross (v.1) ends with the assurance that God ultimately does not abandon the righteous sufferer; Job&#8217;s present experience of divine hiddenness does not represent the final truth about their relationship"}
    ]
  },
  "14": {
    "1": [
      {"type": "allusion", "target": "1 Pet 1:24", "note": "&#8220;Man born of woman is short-lived and full of turmoil. He comes up like a flower and then wilts; he passes like a shadow and does not endure.&#8221; — the flower-and-shadow metaphor for human transience is the OT source that Isaiah 40:6-8 develops and that 1 Peter 1:24 quotes directly: &#8220;All flesh is like grass, and all its glory like the flowers of the field; the grass withers and the flower falls, but the word of the Lord remains forever&#8221;; Job&#8217;s grief-saturated meditation on mortality is the experiential context that gives the prophetic and apostolic comfort its weight — the word that endures is the answer to the flesh that fails"}
    ],
    "4": [
      {"type": "allusion", "target": "John 3:6", "note": "&#8220;Who can bring something pure from something impure? No one can.&#8221; — Job&#8217;s rhetorical question about the impossibility of moral purity from a corrupted source is the OT form of Jesus&#8217; statement in John 3:6: &#8220;Flesh gives birth to flesh, but the Spirit gives birth to spirit&#8221;; the impossibility Job names — <em>ṭāhôr meṭāmēʾ</em> (pure from impure) — is the same impossibility that makes new birth from above necessary; the conclusion both texts draw is that only divine action can produce what human nature cannot"},
      {"type": "allusion", "target": "Rom 3:23", "note": "&#8220;Who can bring something pure from something impure? No one can.&#8221; — Job&#8217;s observation about universal human impurity is the wisdom tradition&#8217;s form of Paul&#8217;s categorical statement in Romans 3:23: &#8220;for all have sinned and fall short of the glory of God&#8221;; the anthropological pessimism that Job voices from within his suffering becomes the basis for Paul&#8217;s universal soteriology — because none are pure, none can save themselves, and the grace that reaches all must come from outside the human condition"}
    ],
    "7": [
      {"type": "allusion", "target": "John 12:24", "note": "&#8220;For there is hope for a tree: if it is cut down, it will sprout again, and its new growth will not stop... yet at the smell of water it will bud and put out branches like a new plant.&#8221; — Job uses the cut-down tree that sprouts again as a hopeful image to contrast with human death (vv.10-12), wishing the same were true of man; Jesus fulfills this wish with an exact parallel: &#8220;unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit&#8221; (John 12:24); Job&#8217;s tree-stump hope becomes, through the resurrection, the principle of death-and-new-life that undergirds all Christian hope"},
      {"type": "allusion", "target": "1 Cor 15:37", "note": "&#8220;Though its root grows old in the earth and its stump dies in the soil — yet at the smell of water it will bud&#8221; — the buried root that gives rise to new growth is Paul&#8217;s resurrection analogy in 1 Corinthians 15:37: &#8220;what you sow does not come to life unless it dies... You do not plant the body that will be, but just a seed&#8221;; Job&#8217;s agricultural image of death-and-new-growth anticipates the resurrection logic that Paul applies to the human body — buried as mortal seed, raised as immortal glory"}
    ],
    "12": [
      {"type": "allusion", "target": "1 Cor 15:20", "note": "&#8220;So man lies down and does not rise; until the heavens are no more, they will not wake or be roused from their sleep.&#8221; — Job&#8217;s &#8220;until the heavens are no more&#8221; is a conditional of hopelessness from within his pre-resurrection perspective; 1 Corinthians 15:20 announces the turn of that condition: &#8220;But Christ has indeed been raised from the dead, the firstfruits of those who have fallen asleep&#8221;; the &#8220;will not rise&#8221; of Job 14:12 is answered by the empty tomb — the one who lay down in death became the &#8220;firstfruits&#8221; whose rising guarantees the general resurrection that Job could only hope for"},
      {"type": "allusion", "target": "1 Thess 4:16", "note": "&#8220;They will not wake or be roused from their sleep&#8221; — Job&#8217;s description of the dead as &#8220;asleep&#8221; (<em>lōʾ yāqûṣû</em> — they will not be roused) uses the sleep metaphor for death that Paul employs throughout his resurrection teaching; 1 Thessalonians 4:16: &#8220;the dead in Christ will rise first&#8221; — the &#8220;sleep&#8221; that Job sees as final, Paul presents as temporary; the waking that Job says will not come &#8220;until the heavens are no more&#8221; is precisely what Christ&#8217;s return accomplishes"}
    ],
    "13": [
      {"type": "allusion", "target": "John 5:28", "note": "&#8220;O that you would hide me in Sheol, shelter me until your anger passes, set a fixed time for me, and then remember me!&#8221; — Job&#8217;s conditional longing — hide me in death until your wrath is over, then call me out — is the most explicit proto-resurrection hope in the wisdom literature; John 5:28-29 declares its fulfilment: &#8220;an hour is coming when all who are in the tombs will hear his voice and come out&#8221;; the &#8220;calling out&#8221; that Job both hopes for and doubts (v.14: &#8220;if a man dies, will he live again?&#8221;) is announced by Jesus as a certainty — and already enacted in the raising of Lazarus (John 11:43)"}
    ],
    "14": [
      {"type": "allusion", "target": "1 Cor 15:19", "note": "&#8220;If a man dies, will he live again? Through all my days of hard service I will wait until my release comes.&#8221; — Job&#8217;s question is the oldest and most direct form of the resurrection question that Paul addresses in 1 Corinthians 15: &#8220;if only for this life we have hope in Christ, we are of all people most to be pitied&#8221; (15:19); the hard service Job endures while waiting for his &#8220;release&#8221; (<em>ḥᵃlîpāh</em> — change/relief) is exactly the condition Paul says faith makes bearable only if resurrection is real; the whole of 1 Corinthians 15 is the answer to Job 14:14"}
    ],
    "15": [
      {"type": "allusion", "target": "John 11:25", "note": "&#8220;You will call out to me, and I will answer; you will long for the work of your hands.&#8221; — Job&#8217;s hope that God will call and he will answer — that death is not the final word — is the hope Jesus declares himself to be: &#8220;I am the resurrection and the life. The one who believes in me will live, even though they die&#8221; (John 11:25); the calling-out that Job dreams of, Jesus demonstrates with Lazarus (&#8220;Lazarus, come out!&#8221;, John 11:43); the longing of God for &#8220;the work of his hands&#8221; — his creatures — is answered in the incarnation and satisfied in the resurrection"}
    ],
    "17": [
      {"type": "allusion", "target": "Col 2:14", "note": "&#8220;My transgression is sealed in a bag, and you have stitched up my guilt.&#8221; — Job&#8217;s image of sin as a sealed, accumulated record kept against him is the legal metaphor that Colossians 2:14 inverts: &#8220;having canceled the charge of our legal indebtedness, which stood against us and condemned us; he has taken it away, nailing it to the cross&#8221;; the sealed bag of transgression that Job fears has been formally opened, discharged, and nailed to the instrument of death by the one who took the record of debt upon himself"}
    ],
    "19": [
      {"type": "allusion", "target": "Heb 6:19", "note": "&#8220;You wash away the hope of man&#8221; — Job&#8217;s lament reaches its lowest point: even hope is being eroded, worn away like stone by water (vv.18-19); Hebrews 6:19 provides the direct answer: &#8220;We have this hope as an anchor for the soul, firm and secure. It enters the inner sanctuary behind the curtain, where our forerunner, Jesus, has entered on our behalf&#8221;; the hope that Job&#8217;s suffering washes away is the hope that Christ&#8217;s entrance into the Holy of Holies anchors permanently — not subject to erosion because it is not grounded in Job&#8217;s circumstances but in Christ&#8217;s heavenly intercession"}
    ]
  }
}

def main():
    existing = load_echo('job')
    merge_echo(existing, JOB_ECHO_12_14)
    save_echo('job', existing)
    print('Job 12-14 echo layer written.')

if __name__ == '__main__':
    main()
