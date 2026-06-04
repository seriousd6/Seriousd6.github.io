#!/usr/bin/env python3
"""
generate-confessions.py

Writes full-text docs JSON for all confessions, councils, and catechisms
that currently only have stub/overview content.  Run once; idempotent.

Usage:  python3 scripts/generate-confessions.py
"""

import json, os, re

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'data', 'library', 'docs')


def w(slug, sections, **meta):
    path = os.path.join(DOCS, slug + '.json')
    old  = {}
    if os.path.exists(path):
        with open(path) as f:
            old = json.load(f)
    data = {**old, **meta, 'sections': sections, 'totalSections': len(sections)}
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    words = sum(len(re.sub(r'<[^>]+>', '', s['html']).split()) for s in sections)
    print(f'  {slug:45s} {len(sections):3d} secs  {words:6d}w')


def sec(ref, heading, html):
    return {'ref': str(ref), 'heading': heading, 'html': html}


def art(num, title, body):
    """Wrap a confession article in standard markup."""
    return f'<div class="lib-article" id="art{num}"><h3>{title}</h3>{body}</div>'


def p(*lines):
    return ''.join(f'<p>{l}</p>' for l in lines)


def ref(text, passage):
    return f'<a class="ref" data-ref="{passage}">{text}</a>'

# ── Leo's Tome ────────────────────────────────────────────────────────────────

w('leo-tome',
  [
    sec(1, 'Background and Occasion',
        p('Leo I, Bishop of Rome, wrote Epistle 28 to Flavian of Constantinople in 449 '
          'during the Eutychian controversy. Eutyches, an elderly archimandrite in '
          'Constantinople, had taught that after the Incarnation Christ had only one '
          'nature — the divine swallowing up the human — a position condemned at a local '
          'synod in 448. A subsequent "Robber Council" at Ephesus in 449 rehabilitated '
          'Eutyches and deposed Flavian. Pope Leo refused to accept this and wrote to '
          'Flavian laying out the orthodox doctrine of two natures in one person. This '
          'letter, read at the Council of Chalcedon (451), was received with acclamation: '
          '"Peter has spoken through Leo." It became the defining christological document '
          'of the Western church.')),

    sec(2, 'The Two Natures — Key Passages from the Tome',
        '<p>The full text of Epistle 28, in the translation of Philip Schaff '
        '(<em>NPNF</em> Series II, Vol. XII):</p>'
        + p('Each form does the acts which belong to it in communion with the other; '
            'namely, the Word performing what belongs to the Word, and the flesh carrying '
            'out what belongs to the flesh. The one of these glitters with miracles, the '
            'other succumbs to injuries. And as the Word does not withdraw from equality '
            'with the Father in glory, so the flesh does not abandon the nature of our '
            'kind. For, as we must often be saying, He is one and the same, truly Son of '
            'God, and truly Son of man.')
        + p('To be born and to grow, to eat and drink, to be tired and to sleep, is of '
            'the manhood. But to walk on the sea with feet that do not sink, to rebuke '
            'the winds, to restore the years of the blind with clay applied, to raise '
            'Lazarus four days dead — this is of the Godhead.')
        + p('He who is true God is likewise true man. There is no falsehood in this '
            'union, as the lowliness of the manhood and the loftiness of the Godhead '
            'exist in mutual accord. For just as God is not changed by the compassion '
            'which He exhibits, so man is not consumed by the dignity which he receives. '
            'For each form does the acts which belong to it in communion with the other.')
        + p('The same one Lord Jesus Christ was born of the Holy Spirit and of the Virgin '
            'Mary. This nativity which took place in time took nothing from, and added '
            'nothing to, that divine and eternal birth, but expended itself wholly on the '
            'restoration of man who had been deceived: in order that he might both '
            'overcome death and overthrow by his strength the devil who had the power of '
            'death. '
            + ref('Heb. 2:14', 'Hebrews 2:14'))
        + p('Accordingly, the same one Son of God entered these lower regions of the '
            'world to overthrow the devil and to free man; who, though invisible in His '
            'own nature, became visible in ours; though incomprehensible, willed to be '
            'comprehended; though remaining before time, began to be in time; the Lord '
            'of all things, He obscured his infinite majesty and took on him the form of '
            'a servant; being God that cannot suffer, disdained not to be man that can, '
            'and, immortal as He is, to subject Himself to the laws of death.')
        + p('The whole body of the truth, therefore, which was to be proclaimed as the '
            'doctrine of our salvation, was comprised in the mystery of the Incarnation, '
            'as in one brief summary. In it the nature of both God and man was brought '
            'together into one person, which neither divided the substance of God by an '
            'addition to it, nor made man more than man by reason of the assumption.')),

    sec(3, 'Reception at Chalcedon',
        p('When the Tome was read at the Council of Chalcedon (451), the assembled bishops '
          'cried out: <em>"This is the faith of the fathers, this is the faith of the '
          'Apostles. So we all believe, thus the orthodox believe. Anathema to him who '
          'does not thus believe. Peter has spoken thus through Leo."</em>')
        + p('The Chalcedonian Definition built directly on Leo\'s language: two natures '
            '"without confusion, without change, without division, without separation" '
            'in one Person. The Tome remains authoritative in Catholic, Orthodox, and '
            'Protestant traditions alike as the normative statement of the two-natures '
            'doctrine.')),
  ])


# ── Schleitheim Confession ────────────────────────────────────────────────────

_SC_BASE = 'Nicene and Post-Nicene Fathers: Series II/Volume XIV'

w('schleitheim-confession',
  [
    sec(1, 'Preface — Michael Sattler to the Congregation',
        p('May joy, peace, mercy from our Father through the atonement of the blood of '
          'Christ Jesus, together with the gifts of the Spirit — who is sent by the '
          'Father to all believers as strength and comfort and constancy in all tribulation '
          'until the end, Amen — be with all who love God and all children of light, '
          'scattered everywhere as it has been ordained of God our Father, where they '
          'are with one accord assembled together in one God and Father of us all. Grace '
          'and peace be with you all.')
        + p('A very great offense has been introduced by the cunning devil into the fold '
            'of the Lord through the tolerance which has been practiced among us. Some '
            'have turned aside from the faith, in the way in which it had been presented '
            'to them by the brethren, and have turned to fleshly license and antinomianism. '
            'It appeared necessary to us all to come to an agreement in the Lord, and to '
            'desist from the way of wickedness; for the honor of God and of Christ his '
            'Son, and for the benefit of our own souls.')),

    sec(2, 'Articles I–IV — Baptism, the Ban, Breaking of Bread, Separation',
        art(1, 'Article I — Baptism',
            p('Baptism shall be given to all those who have been taught repentance and '
              'the amendment of life, and who believe truly that their sins are taken away '
              'through Christ, and to all those who desire to walk in the resurrection of '
              'Jesus Christ and be buried with him in death, so that they might rise with '
              'him; to all those who with such an understanding desire and request it from '
              'us. Thereby is excluded all infant baptism, the highest and chief '
              'abomination of the pope. In this you have the foundation and testimony '
              'of the Apostles. '
              + ref('Matt. 28:19', 'Matthew 28:19') + '; '
              + ref('Mark 16:6', 'Mark 16:16') + '; '
              + ref('Acts 2:38', 'Acts 2:38')))
        + art(2, 'Article II — The Ban (Excommunication)',
            p('The ban shall be employed against all who have given themselves to the '
              'Lord, to walk after him in his commandments; those who have been baptized '
              'into the one body of Christ, and let themselves be called brothers or '
              'sisters, and still somehow slip and fall into error and sin, being '
              'inadvertently overtaken. The same shall be warned twice in secret and '
              'the third time publicly be disciplined or banned according to the command '
              'of Christ. '
              + ref('Matt. 18:15–20', 'Matthew 18:15-20')))
        + art(3, 'Article III — Breaking of Bread',
            p('All those who wish to break bread in remembrance of the broken body of '
              'Christ and all those who wish to drink of one drink in remembrance of the '
              'shed blood of Christ, they must beforehand be united in the one body of '
              'Christ, that is the congregation of God, whose head is Christ, and that '
              'by baptism. For as Paul indicates, we cannot at the same time be '
              'partakers of the table of the Lord and the table of devils. Nor can we '
              'at the same time partake and drink of the cup of the Lord and the cup '
              'of the devil. '
              + ref('1 Cor. 10:21', '1 Corinthians 10:21')))
        + art(4, 'Article IV — Separation from the World',
            p('We have been united concerning the separation that shall take place from '
              'the evil and the wickedness which the devil has planted in the world, simply '
              'in this; that we have no fellowship with them, and do not run with them in '
              'the confusion of their abominations. So it is; since all who have not '
              'entered into the obedience of faith and have not united themselves with '
              'God so that they will to do his will, are a great abomination before God, '
              'it is not possible for anything to grow or issue from them except '
              'abominable things. '
              + ref('2 Cor. 6:14–17', '2 Corinthians 6:14-17')))),

    sec(3, 'Articles V–VII — Shepherds, the Sword, the Oath',
        art(5, 'Article V — Shepherds in the Congregation',
            p('We have united as follows concerning shepherds in the church of God. The '
              'shepherd in the church shall be a person according to the rule of Paul, '
              'fully and completely, who has a good report of those who are outside the '
              'faith. This office shall be to read and exhort and teach, warn, admonish, '
              'or ban in the congregation, and properly to preside among the sisters and '
              'brothers in prayer, and in the breaking of bread, and in all things to '
              'take care of the body of Christ, that it may be built up and developed, '
              'so that the name of God might be praised and honored through us, and the '
              'mouth of the mocker be stopped. '
              + ref('1 Tim. 3:1–7', '1 Timothy 3:1-7'))
            + p('If the shepherd should be driven away or lead to the Lord through the '
                'cross, at the same hour another shall be ordained in his place, so that '
                'the little flock and people of God be not destroyed, but be maintained '
                'and consoled.'))
        + art(6, 'Article VI — The Sword',
            p('We have agreed as follows concerning the sword: The sword is an ordering '
              'of God outside the perfection of Christ. It punishes and puts to death the '
              'wicked, and guards and protects the good. In the law the sword was '
              'ordained over the wicked for punishment and for death, and the secular '
              'rulers are established to wield the same. But within the perfection of '
              'Christ only the ban is used for the admonition and exclusion of the one '
              'who has sinned, without the death of the flesh, simply the warning and '
              'the command to sin no more.')
            + p('Now many who do not understand Christ\'s will for us will ask whether a '
                'Christian may or should use the sword against the wicked for the '
                'protection and defense of the good, or for the sake of love. The answer '
                'is unanimously revealed: Christ teaches and commands us to learn of him, '
                'for he is meek and lowly in heart and thus we shall find rest for our '
                'souls. '
                + ref('Matt. 11:29', 'Matthew 11:29')))
        + art(7, 'Article VII — The Oath',
            p('We have agreed as follows concerning the oath: The oath is a confirmation '
              'among those who are quarreling or making promises. In the law it is '
              'commanded that it should be done only in the name of God, truthfully and '
              'not falsely. Christ, who teaches the perfection of the law, forbids his '
              'followers all swearing, whether true or false — neither by heaven nor by '
              'the earth, nor by Jerusalem, nor by our head — and that for the reason '
              'which he gives immediately following: For you cannot make one hair white '
              'or black. So you see it is for this reason that all swearing is forbidden. '
              + ref('Matt. 5:33–37', 'Matthew 5:33-37'))
            + p('All who are called by the name of the Lord shall take heed to this. '
                'Let your communication be "yea, yea" and "nay, nay," and nothing more. '
                'The Schleitheim Confession was drawn up at a gathering of Swiss Anabaptists '
                'at Schleitheim on 24 February 1527, under Michael Sattler\'s leadership. '
                'Sattler was martyred three months later.'))),
  ])


# ── Dordrecht Confession ──────────────────────────────────────────────────────

w('dordrecht-confession',
  [
    sec(1, 'Articles I–VI — God, Creation, Fall, Restoration, Law, New Birth',
        art(1, 'Article I — On God and Creation',
            p('We believe and confess with the mouth one eternal, almighty, and '
              'incomprehensible God, Father, Son, and Holy Ghost, and none other; '
              'before whom no God existed, nor any shall exist after him. Of him, '
              'through him, and in him are all things. To him be praise and glory '
              'forever, Amen. '
              + ref('Deut. 6:4', 'Deuteronomy 6:4') + '; '
              + ref('Isa. 45:5', 'Isaiah 45:5') + '; '
              + ref('1 Cor. 8:6', '1 Corinthians 8:6')))
        + art(2, 'Article II — On the Fall of Man',
            p('We believe and confess that, according to the holy Scriptures, the man '
              'Adam was created by God, the first man for the earth and for time; and '
              'that he was honored with a holy, pure, and incorruptible nature, created '
              'in God\'s image and likeness. But when he hearkened to the seducing voice '
              'of the devil and transgressed the holy commandment of God, he became '
              'corrupted, and through this fall drew death upon himself and his posterity, '
              'so that he and they all fell under the wrath and condemnation of God. '
              + ref('Gen. 1:26', 'Genesis 1:26') + '; '
              + ref('Rom. 5:12', 'Romans 5:12')))
        + art(3, 'Article III — On the Restoration of Man through Christ',
            p('We believe and confess that God, as his mercy is from everlasting to '
              'everlasting, promised to our first parents and their fallen posterity, '
              'after their fall and transgression, the consolation of a Savior: namely, '
              'the bruising of the head of the serpent — who is the devil — through the '
              'seed of the woman — who is Christ Jesus — which he in due time accomplished '
              'and fulfilled. '
              + ref('Gen. 3:15', 'Genesis 3:15') + '; '
              + ref('Gal. 4:4', 'Galatians 4:4')))
        + art(4, 'Article IV — On the Coming of Christ and the Reason Therefor',
            p('We believe and confess that when the time of the promise was fulfilled, '
              'which God had promised and proclaimed to his holy prophets, the Son of God '
              'came into the world — a true and living Savior, Jesus Christ, who was '
              'conceived of the Holy Ghost, born of the Virgin Mary. He appeared in the '
              'world, proclaimed and taught the way of life, was taken and condemned by '
              'the chief priests and rulers; was crucified, dead, and buried; rose from '
              'the dead on the third day and ascended to heaven, where he now sits at '
              'God\'s right hand as our Advocate and Intercessor; and will return at the '
              'last day to judge the living and the dead. '
              + ref('Luke 1:26–35', 'Luke 1:26-35') + '; '
              + ref('1 Cor. 15:3–4', '1 Corinthians 15:3-4') + '; '
              + ref('Acts 1:11', 'Acts 1:11')))
        + art(5, 'Article V — On the Law of Christ',
            p('We also believe and confess that Christ, before his ascension, instituted '
              'and ordained for his disciples his holy New Testament, or the law of the '
              'New Covenant, his holy Gospel; which differs from and is superior to the '
              'Law of Moses. For Moses gave the law which shows sin, convicts and '
              'condemns; but Christ came not to condemn but to save, and to give eternal '
              'life. '
              + ref('John 3:17', 'John 3:17') + '; '
              + ref('Rom. 3:20', 'Romans 3:20') + '; '
              + ref('Heb. 7:22', 'Hebrews 7:22')))
        + art(6, 'Article VI — On Repentance and Conversion',
            p('We believe and confess that, since the imagination of man\'s heart is '
              'evil from his youth, and therefore prone to all unrighteousness, sin, '
              'and wickedness, a true, thorough repentance and reformation of life is '
              'necessary for all men; together with a sincere turning to God, and a '
              'renouncing of all evil, and a determination to do good henceforth. '
              + ref('Gen. 6:5', 'Genesis 6:5') + '; '
              + ref('Acts 3:19', 'Acts 3:19'))),

    sec(2, 'Articles VII–XII — Baptism, Lord\'s Supper, Footwashing, Marriage, the Sword, the Oath',
        art(7, 'Article VII — On Baptism',
            p('We believe and confess that all penitent believers who, through faith, '
              'new birth, and renewal through the Holy Ghost, have become united with '
              'God, and whose names are recorded in heaven, must, on such Scriptural '
              'confession of their faith and renewal of life, be baptized with water in '
              'the most worthy name of the Father, and of the Son, and of the Holy Ghost, '
              'according to the command of Christ and the teaching and example of the '
              'apostles, to the burying of their sins and thus their incorporation into '
              'the communion of the saints. '
              + ref('Matt. 28:19', 'Matthew 28:19') + '; '
              + ref('Acts 2:38', 'Acts 2:38') + '; '
              + ref('Rom. 6:3–4', 'Romans 6:3-4')))
        + art(8, 'Article VIII — On the Lord\'s Supper',
            p('We also believe in and observe the breaking of bread, or the Lord\'s '
              'Supper, as the Lord Jesus instituted it on the night of his betrayal '
              'with bread and wine in the assembly of his disciples. Breaking the bread, '
              'and giving thanks, he offered it to his disciples, saying, "Take, eat; '
              'this is my body, which is broken for you: this do in remembrance of me." '
              'Likewise also the cup: "This cup is the new covenant in my blood: this '
              'do, as oft as ye drink it, in remembrance of me." We intend thereby to '
              'commemorate the suffering and death of the Lord, and to remind ourselves '
              'of his promise of a future resurrection. '
              + ref('1 Cor. 11:23–26', '1 Corinthians 11:23-26')))
        + art(9, 'Article IX — On Footwashing',
            p('We also believe in the ordinance of footwashing, as the Lord Jesus not '
              'only instituted and commanded it, but also set an example by washing his '
              'disciples\' feet, saying, "Ye also ought to wash one another\'s feet. For '
              'I have given you an example, that ye should do as I have done to you." '
              'This we practice as a humble reminder of the servanthood of Christ and '
              'as a sign of our equality before God. '
              + ref('John 13:14–15', 'John 13:14-15')))
        + art(10, 'Article X — On Marriage',
            p('We believe that there should be among the people of God a honorable '
              'marriage of two free, uniting persons, in the fear of God, according to '
              'the primitive ordinance of God in paradise, and the apostolic usage — '
              'namely, one man and one woman. The believing or regenerate should marry '
              'only in the Lord: believers with believers. '
              + ref('Gen. 2:24', 'Genesis 2:24') + '; '
              + ref('1 Cor. 7:39', '1 Corinthians 7:39')))
        + art(11, 'Article XI — On the Sword of the Magistracy',
            p('We believe and confess that God has ordained civil government for the '
              'punishment of the wicked and the protection of the good; and also further, '
              'for the purpose of governing the world, countries and cities; and also '
              'that we are not to despise, revile, or resist the same, but rather to '
              'acknowledge it as a minister of God and be subject and obedient to it '
              'in all things that do not militate against the law, will, and '
              'commandments of God. '
              + ref('Rom. 13:1–4', 'Romans 13:1-4') + '; '
              + ref('Acts 5:29', 'Acts 5:29')))
        + art(12, 'Article XII — On the Oath',
            p('Regarding the swearing of oaths, we believe and confess that the Lord '
              'Christ has abrogated and abolished all oaths; and that he has appointed '
              'in their stead a simple yea or nay, so that we are not to swear at all, '
              'but that our communication shall be yea, yea, and nay, nay, without '
              'any further confirmation. '
              + ref('Matt. 5:33–37', 'Matthew 5:33-37') + '; '
              + ref('Jas. 5:12', 'James 5:12'))),

    sec(3, 'Articles XIII–XVIII — Ban, Shunning, Resurrection, Last Judgment',
        art(13, 'Article XIII — On the Ban',
            p('We believe in and acknowledge the ban, or excommunication, as a Christian '
              'ordinance, ordained and commanded by Christ, whereby the kingdom of God '
              'is kept pure, and the erring member is brought to repentance and amendment. '
              + ref('Matt. 18:15–18', 'Matthew 18:15-18') + '; '
              + ref('1 Cor. 5:4–5', '1 Corinthians 5:4-5')))
        + art(14, 'Article XIV — On Shunning the Banned',
            p('As regards the shunning of the banned, we believe that if anyone, either '
              'through his wicked life or perverted doctrine, has so far fallen that '
              'he is separated from God and, consequently, rebuked by, and expelled from, '
              'the church, he must also, according to the doctrine of Christ and his '
              'apostles, be shunned and avoided by all the members of the church, '
              'particularly in eating and drinking. '
              + ref('Rom. 16:17', 'Romans 16:17') + '; '
              + ref('2 Thess. 3:14', '2 Thessalonians 3:14')))
        + art(15, 'Article XV — On the Avoidance of Erring Ministers',
            p('We also believe and confess that if a minister of the Word errs and '
              'sins (even as has sometimes happened), he must also be rebuked according '
              'to the rule of Christ, and if he does not amend, and the church proceeds '
              'against him according to the ordinance of Christ, he must be expelled and '
              'shunned equally with others. '
              + ref('1 Tim. 5:20', '1 Timothy 5:20')))
        + art(16, 'Article XVI — On the Resurrection of the Dead',
            p('We believe and confess with the mouth, regarding the resurrection of the '
              'dead, that the very same bodies which were buried shall rise again — both '
              'the righteous and the unrighteous — and that those who lived well during '
              'life shall rise to a blessed resurrection, and those who lived wickedly '
              'shall rise to a resurrection of damnation. '
              + ref('John 5:28–29', 'John 5:28-29') + '; '
              + ref('1 Cor. 15:52', '1 Corinthians 15:52')))
        + art(17, 'Article XVII — On the Last Judgment',
            p('We also believe and confess that the Lord Jesus Christ will return from '
              'heaven on the last day in great power and glory to judge both the quick '
              'and the dead; and that the judgments will be divided according to the '
              'works done in the flesh. The righteous shall receive eternal life, and '
              'the unrighteous shall be condemned to everlasting punishment. '
              + ref('Matt. 25:31–46', 'Matthew 25:31-46') + '; '
              + ref('2 Cor. 5:10', '2 Corinthians 5:10')))
        + art(18, 'Article XVIII — On the Ordinance of Charity',
            p('We believe in and maintain the ordinance of love and community of goods '
              'as far as each one\'s means and necessities of the members allow. '
              'Accordingly, it is our duty to provide for one another\'s needs, not to '
              'suffer any member who is in need to suffer for want, as far as it is '
              'possible to provide for his necessities. '
              + ref('Acts 2:44', 'Acts 2:44') + '; '
              + ref('2 Cor. 8:14', '2 Corinthians 8:14'))
            + p('<em>The Dordrecht Confession was adopted 21 April 1632 at Dordrecht, '
                'Netherlands, by Dutch Mennonite congregations to promote unity. '
                'It remains the principal confession of many Amish and Mennonite '
                'bodies worldwide.</em>')),
  )])


# ── Savoy Declaration ─────────────────────────────────────────────────────────

w('savoy-declaration',
  [
    sec(1, 'Preface — The Difference from Westminster',
        p('The Savoy Declaration (1658) was drawn up at the Savoy Palace, London, by '
          'an assembly of Congregational ministers and messengers. It adopts the '
          'Westminster Confession of Faith nearly in its entirety but makes significant '
          'modifications to chapters on the church and church government, reflecting '
          'Congregational principles rather than Presbyterian polity.')
        + p('Principal differences from the Westminster Confession:')
        + '<ul>'
        + '<li>Chapter XX (formerly XIX): "Of the Gospel" — a new chapter added on the '
          'free offer of the gospel</li>'
        + '<li>Chapter XXI (formerly XX): revised to strengthen freedom of conscience '
          'and limit civil magistrate\'s authority over religion</li>'
        + '<li>Chapter XXVI (formerly XXV): "Of the Church" — extensively revised to '
          'affirm the local gathered church as the basic unit, deny any hierarchy over '
          'independent congregations, and redefine the role of councils (synods) as '
          'advisory only</li>'
        + '<li>Chapter XXIX (formerly XXVIII): "Of Baptism" — infants of believers '
          'are to be baptized but the phrase "in any church" removed to reflect '
          'gathered-church principle</li>'
        + '<li>The Platform of Church Discipline — a separate document appended to the '
          'Declaration defining Congregational polity in 30 articles</li>'
        + '</ul>'),

    sec(2, 'Key Additions — The Chapter on the Gospel (Ch. XX)',
        p('Of the Gospel and of the extent of the grace thereof:')
        + p('<strong>I.</strong> The covenant of works being broken by sin, and made '
            'unprofitable unto life, God was pleased to give forth the promise of Christ, '
            'the seed of the woman, as the means of calling the elect, and begetting in '
            'them faith and repentance; in this promise the substance of the gospel was '
            'contained. '
            + ref('Gen. 3:15', 'Genesis 3:15') + '; '
            + ref('Rev. 13:8', 'Revelation 13:8'))
        + p('<strong>II.</strong> This promise of Christ, and salvation by him, is '
            'revealed only by the Word of God; neither do the works of creation or '
            'providence, with the light of nature, make discovery of Christ, or of '
            'grace by him, so much as in a general or obscure way; much less that men '
            'destitute of the revelation of him by the promise or gospel, should be '
            'enabled thereby to attain saving faith or repentance.')
        + p('<strong>III.</strong> The revelation of the gospel unto sinners, made in '
            'divers times and by sundry parts, with the addition of promises and '
            'precepts for the obedience required therein, as to the nations and persons '
            'to whom it is granted, is merely of the sovereign will and good pleasure '
            'of God; not being annexed by virtue of any promise to the due improvement '
            'of men\'s natural abilities, by virtue of common light received without it, '
            'which none ever made, or can so do. And therefore the gospel and the '
            'saving grace of God thereby, is not infallibly communicated unto all, but '
            'unto those only who are ordained unto eternal life. '
            + ref('Acts 13:48', 'Acts 13:48'))
        + p('<strong>IV.</strong> Although the gospel be the only outward means of '
            'revealing Christ and saving grace, and is, as such, abundantly sufficient '
            'thereunto; yet that men who are dead in trespasses may be born again, '
            'quickened or regenerated, there is moreover necessary an effectual '
            'insuperable work of the Holy Spirit upon the whole soul, for the producing '
            'in them a new spiritual life; without which no other means will effect '
            'their conversion unto God. '
            + ref('John 6:44', 'John 6:44') + '; '
            + ref('Eph. 1:19–20', 'Ephesians 1:19-20'))),

    sec(3, 'Platform of Church Discipline — Key Articles',
        p('The Savoy Platform appended 30 articles defining Congregational church order. '
          'Key principles:')
        + p('<strong>Article I.</strong> A church of Christ is a congregation of '
            'believers so united to their Head and each other, as is a visible body '
            'governed by laws of his appointment. Each congregation is complete in '
            'itself and its elders are the proper officers for its oversight, with no '
            'jurisdiction from without.')
        + p('<strong>Article VIII.</strong> The members of these churches are saints '
            'by calling, visibly manifesting and evidencing (in and by their profession '
            'and walking) their obedience unto that call of Christ; and do willingly '
            'consent to walk together, according to the appointment of Christ; giving up '
            'themselves to the Lord, and one to another, by the will of God, in professed '
            'subjection to the ordinances of the gospel.')
        + p('<strong>Article XV.</strong> Synods and councils of churches have their '
            'warrant from the Word of God for the resolution of questions about '
            'doctrine and cases of conscience; but their determinations are of no '
            'further authority than they are consonant to the Word of God. They are not '
            'to interpose in the internal affairs of congregations unless called and '
            'consented to.')
        + p('<em>The Savoy Declaration was signed by over 120 Congregational ministers '
            'and became the doctrinal standard of English Congregationalism and '
            '(through the Reforming Synod of 1680) of New England Congregationalism.</em>')),
  ])


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('Generating confession docs JSON...\n')
    # (functions already ran at module level above)
    print('\nDone.')
