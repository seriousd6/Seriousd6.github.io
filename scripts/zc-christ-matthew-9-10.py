"""
MKT Christ — Matthew all chapters (Christological trajectory)
Output: data/commentary/mkt-christ/matthew.json

Directness key: Matthew is a direct revelation book — Jesus is named Son of God,
Son of Man, Messiah, Emmanuel throughout. Key shadow/type/allusion moments:
shadow = OT narrative prefiguring Christ; type = OT figure intentionally
mirroring Christ; fulfillment = explicit OT text realized.
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
  "1": {
    "1": '<p>A fulfillment: the book of the genealogy of Jesus Christ, son of David, son of Abraham. Matthew opens by naming Jesus as the convergence point of two great OT promise-lines: the Abrahamic covenant (blessing to all nations through his seed, Gen 12:3, 22:18) and the Davidic covenant (an everlasting dynasty on David\'s throne, 2 Sam 7:12-16). Every generation of the genealogy is a step in the providential preparation for the one in whom both covenants find their fulfillment. The three-part structure (Abraham to David, David to exile, exile to Christ) declares that Israel\'s entire history was a long advent.</p>',
    "23": '<p>A fulfillment: behold the virgin shall conceive and bear a son, and they shall call his name Immanuel — God with us. The fulfillment of Isa 7:14 in the virgin birth is Matthew\'s programmatic Christological declaration: the incarnation of the Son is the coming of God himself to dwell with his people. Every OT passage about YHWH\'s presence with Israel (the pillar of cloud, the tabernacle glory, the temple Shekinah) pointed toward this: the permanent, personal, embodied presence of God in Jesus. The Gospel\'s closing promise (I am with you always, 28:20) is the Immanuel-theme completing its arc.</p>'
  },
  "2": {
    "15": '<p>A fulfillment: out of Egypt I called my son. The Exodus of Israel (Hos 11:1) is not merely a historical precedent but a type of the Son\'s own Egypt-return. Jesus relives the Exodus pattern: he goes to Egypt in danger, returns when the threat passes, passes through water (baptism = Red Sea crossing), is tested in the wilderness (40 days = 40 years), and gives the new Torah on the mountain (Sermon on the Mount). Matthew presents Jesus not merely as an individual fulfilling a verse but as the corporate representative of Israel, recapitulating and perfecting Israel\'s story.</p>'
  },
  "3": {
    "17": '<p>A direct revelation: this is my beloved Son with whom I am well pleased. The Father\'s declaration at the baptism publicly identifies Jesus as the one in whom Ps 2 (royal investiture) and Isa 42:1 (Servant appointment) converge. He is simultaneously the messianic king who will rule all nations and the Suffering Servant who will bear their sins. These two identities — which Israel\'s tradition held apart — are now declared to be one person. The whole mission of Jesus flows from this dual identity: he rules by serving and saves by dying.</p>'
  },
  "4": {
    "4": '<p>A direct revelation: man shall not live by bread alone but by every word that comes from the mouth of God. Jesus\'s quotation of Deut 8:3 in the wilderness is not merely a proof-text used in debate — it is the lived demonstration of what it means to be the true Israel. Where Israel in the wilderness grumbled for bread and failed the test of trusting God\'s word, Jesus embraces hunger and trusts the Father\'s provision. He is the faithful Israelite Israel could not be — and therefore the representative in whom Israel\'s failure is overcome and God\'s purpose for his people is fulfilled.</p>',
    "17": '<p>A direct revelation: repent, for the kingdom of the heavens has drawn near. Jesus\'s opening proclamation is the announcement that the long-awaited reign of God — anticipated in Daniel\'s stone-kingdom, Isaiah\'s eschatological banquet, and the Psalms of enthronement — has broken into history in his own person and ministry. The kingdom is not an institution but a reality: wherever the king is present, the kingdom is present. Every exorcism, healing, and teaching is the kingdom coming — the future of God arriving early in the person of the Son.</p>'
  },
  "5": {
    "17": '<p>A direct revelation: I have not come to abolish the Law and the Prophets but to fulfill them. Christ\'s relationship to Scripture is unique: he is not a scribe who interprets it, not a prophet who applies it, but the one toward whom all of it was pointing and in whom all of it reaches its intended fullness. The antitheses that follow (You have heard it said... but I say to you) do not set Jesus against Moses but demonstrate Jesus\'s sovereign authority to reveal the Torah\'s deepest intention — the intention the Author always had, which only the Author himself can fully declare.</p>',
    "48": '<p>A direct revelation: be perfect as your heavenly Father is perfect. The standard of the kingdom\'s ethics is not a moral code but a person — the character of the Father, which is also the character of the Son. Jesus does not merely command an impossible ethical ideal; he embodies it. The Sermon on the Mount describes not only what his disciples must become but what he already is: poor in spirit, meek, merciful, pure in heart, a peacemaker who endures persecution for righteousness. He is both the teacher and the subject of every beatitude.</p>'
  },
  "7": {
    "24": '<p>A direct revelation: everyone who hears these words of mine and does them will be like a wise man who built his house on the rock. Jesus presents himself as the Rock — the authoritative foundation for a life that withstands final judgment. The shift from Moses\'s covenant (obey and live) to Jesus\'s covenant (hear my words and do them) is implicit but decisive: the words Jesus speaks carry the same covenant-binding authority as Torah, because he is the Torah-author become flesh, speaking the fulfillment of what the text was always pointing toward.</p>'
  },
  "8": {
    "17": '<p>A fulfillment: he took our infirmities and bore our diseases. Matthew\'s citation of Isa 53:4 at the healing ministry — not at the cross — reveals that the Servant\'s vicarious bearing is already operative in the healing miracles. Christ carries what he heals: he takes it from the sufferer and bears it himself. The cross is not the only moment of substitution but its culmination; every healing is an anticipation of the cross in which the Servant absorbs what afflicts humanity. The miracles of Matthew 8-9 are the Servant Song enacted in the villages of Galilee.</p>'
  },
  "9": {
    "6": '<p>A direct revelation: the Son of Man has authority on earth to forgive sins. The Christological claim implicit in the healing of the paralytic is staggering: Jesus does not point to God\'s forgiveness and declare it announced — he forgives in his own name. The scribes\' objection (who can forgive sins but God alone?) is the correct theological instinct; Jesus\'s answer is not to deny the premise but to claim the prerogative: the Son of Man exercises divine authority on earth. The healing that follows is the visible confirmation of the invisible forgiveness, proving the claim.</p>'
  },
  "11": {
    "5": '<p>A fulfillment: the blind receive their sight and the lame walk, lepers are cleansed and the deaf hear, and the dead are raised up, and the poor have good news preached to them. Jesus\'s answer to John identifies himself as the one in whom Isaiah\'s eschatological catalog is being fulfilled. The signs of Isa 35 and 61 are not mere social goods that any compassionate person could provide — they are the specific marks of the age when God himself comes to save (Isa 35:4, Isa 61:1). By performing these signs, Jesus claims to be not merely the Messiah\'s herald but the divine Savior Isaiah announced.</p>',
    "28": '<p>A direct revelation: come to me all who labor and are heavy laden, and I will give you rest. Jesus speaks as personified Wisdom (Sir 24:19-20, 51:23-27 provide the background) and as YHWH who gives rest to his people (Ps 95:11). The invitation is not to a teaching-program but to a relationship with a person: come to me. The yoke of Christ is the yoke of covenant-relationship with him; the rest is the eschatological Sabbath that creation pointed toward and that Christ gives in advance to all who come.</p>'
  },
  "13": {
    "11": '<p>A direct revelation: to you it has been given to know the mysteries of the kingdom of the heavens. Christ is the revealer of the kingdom\'s mysteries — the one in whom the hidden purposes of God are disclosed. What OT prophets and kings longed to see (v.17) is now openly displayed in Jesus\'s ministry: the kingdom of heaven is present in him. The disciples receive not merely information about the kingdom but eyes to see it — a gift of revelation that is inseparable from their relationship with the one who is himself the kingdom\'s content.</p>'
  },
  "16": {
    "16": '<p>A direct revelation: you are the Christ, the Son of the living God. Peter\'s confession — received by revelation from the Father (v.17) — names the two central Christological realities of Matthew\'s Gospel: Messiahship (the anointed king who fulfills the Davidic promise) and divine sonship (the unique relationship to the Father that makes him more than David\'s human descendant). These two are inseparable: the Messiah is the Son, and the Son is the Messiah. Matthew\'s entire narrative is the demonstration that both titles belong to Jesus of Nazareth.</p>'
  },
  "17": {
    "5": '<p>A direct revelation: this is my beloved Son with whom I am well pleased; listen to him. The Transfiguration is the unveiling of Christ\'s eternal glory that the incarnation normally conceals. Moses (the Law) and Elijah (the Prophets) appear as witnesses and then depart; Jesus alone remains. The Father\'s command listen to him (echoing Deut 18:15) declares that the entire OT revelation reaches its consummation in the Son — not that Moses and Elijah are superseded as false but that they were preparatory and are now fulfilled. The disciples are to hear the Torah and the Prophets as they hear Jesus, because he is what they were pointing toward.</p>'
  },
  "20": {
    "28": '<p>A direct revelation: the Son of Man came not to be served but to serve and to give his life as a ransom for many. The ransom-saying is Jesus\'s most concentrated self-interpretation of his death before the passion narrative begins. He gives his psyche (self, life, person) as the lytron (ransom price) anti (in exchange for, substituting for) the many. The Isaianic Servant background (Isa 53:10-12) fills the content: the Servant who makes his soul an offering for sin thereby justifies many. Christ\'s death is not an accident or martyrdom but a purposive self-offering with the specific intent of ransoming others from what they cannot ransom themselves from.</p>'
  },
  "21": {
    "42": '<p>A fulfillment: the stone that the builders rejected has become the cornerstone. Jesus applies Ps 118:22-23 to himself: he is the stone rejected by Israel\'s builders (the chief priests and elders, v.23) that God has made the cornerstone of the new temple — the community of those who receive the kingdom (v.43). The stone-metaphor has a long OT trajectory (Isa 28:16, Zech 3:9) culminating in this: the rejected one is the foundational stone without which the entire structure of God\'s redemptive purposes would collapse. The crucifixion-and-resurrection is the act of rejection-and-vindication that fulfills the Psalm.</p>'
  },
  "22": {
    "44": '<p>A fulfillment: the LORD said to my Lord, sit at my right hand until I make your enemies a footstool for your feet. Jesus\'s use of Ps 110:1 reveals that the Messiah\'s identity exceeds Davidic sonship — he is David\'s Lord, which means he is the divine Son who pre-exists his own Davidic lineage. The Son of Man coming on the clouds (24:30) is seated at God\'s right hand (Ps 110:1) while his enemies are being subdued — the enthronement is present and active, not merely future. Every exercise of Christ\'s authority in Matthew (healing, teaching, forgiving, commissioning) is the exercise of this right-hand authority from the beginning of his ministry.</p>'
  },
  "26": {
    "28": '<p>A fulfillment: this is my blood of the covenant which is poured out for many for the forgiveness of sins. The cup-word at the Last Supper is the most concentrated intersection of Christological and covenantal themes in Matthew: the blood is covenant-blood (Exod 24:8), it is poured out for many (Isa 53:12), it accomplishes forgiveness (Jer 31:34), it is Jesus\'s own blood (divine-human person). The Passover context adds the liberation-from-Egypt dimension: as the lamb\'s blood protected Israel on the night of exodus, so Christ\'s blood accomplishes the definitive exodus from sin and death. The institution of the Lord\'s Supper is the establishment of the new Passover memorial.</p>'
  },
  "27": {
    "46": '<p>A direct revelation: my God, my God, why have you forsaken me? The cry of dereliction is the most difficult Christological moment in the Gospels — the eternal Son experiencing genuine God-forsakenness as the penalty of sin he is bearing for others. This is not merely the quoting of a Psalm for devotional comfort (though the Psalm ends in vindication); it is the actual experience of what Paul calls being made sin for us (2 Cor 5:21) and being cursed for us (Gal 3:13). The darkness, the abandoned cry, and the torn curtain together form the Christological declaration: God was in Christ, in the place of the God-forsaken, reconciling the world to himself.</p>',
    "51": '<p>A fulfillment: the curtain of the temple was torn in two from top to bottom. The rending of the veil that separated the holy of holies from the holy place is the Christological climax of Matthew\'s temple-theology: the barrier between God and humanity that the entire Levitical system presupposed and maintained is destroyed by Christ\'s death. Access to the divine presence, which required the high priest alone once a year with blood, is now open to all — the way into the most holy place has been opened permanently through Christ\'s body (Heb 10:20). Matthew adds the opened tombs and the resurrection of the saints (vv.52-53) as the first-fruits of the general resurrection inaugurated by Christ\'s death.</p>'
  },
  "28": {
    "18": '<p>A direct revelation: all authority in heaven and on earth has been given to me. The post-resurrection commissioning is the Danielic enthronement realized: the Son of Man to whom all authority was given (Dan 7:14) now speaks in his own name. The crucified Jesus is the risen and enthroned Lord — his death was not the end of his authority but the means by which the authority was exercised and the path by which it was received. The Great Commission is grounded in this universal authority: he sends because he has been given the power to send, and his presence accompanies the sent ones because his authority extends to every place they go.',
    "20": '<p>A direct revelation: I am with you always, to the end of the age. The Gospel that opened with Immanuel — God with us — closes with the personal promise of the same presence: I am with you. The Shekinah-theology of the OT (YHWH dwelling with his people in the tabernacle, the temple, the cloud of fire) reaches its final form in the risen Christ\'s personal, perpetual, universal accompaniment of his community. The age of the Spirit is not a lesser presence but the continuation of the Immanuel-presence through the risen body of the ascended Son, who is both seated at the right hand and present with his people through the Spirit he pours out.'
  }
}

def main():
    existing = load_comm('mkt-christ', 'matthew')
    merge_comm(existing, DATA)
    save_comm('mkt-christ', 'matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew mkt-christ: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
