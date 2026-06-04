#!/usr/bin/env python3
"""One-off script: patch series/volume fields into data/library/index.json."""
import json, os

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX   = os.path.join(ROOT, 'data', 'library', 'index.json')

# (series_id, series_title, volume_number, volume_label)
SERIES = {
  # Calvin
  'calvin-institutes':       ('calvin-institutes', 'Institutes of the Christian Religion', 0, 'Overview'),
  'calvin-institutes-book1': ('calvin-institutes', 'Institutes of the Christian Religion', 1, 'Book I (Wikisource)'),
  'calvin-institutes-vol1':  ('calvin-institutes', 'Institutes of the Christian Religion', 2, 'Vol. I — Books I–II'),
  'calvin-institutes-vol2':  ('calvin-institutes', 'Institutes of the Christian Religion', 3, 'Vol. II — Books III–IV'),
  # Augustine
  'augustine':                      ('augustine', 'Works of Augustine', 0, 'Overview'),
  'augustine-confessions':          ('augustine', 'Works of Augustine', 1, 'Confessions'),
  'augustine-city-of-god':          ('augustine', 'Works of Augustine', 2, 'City of God'),
  'augustine-on-trinity':           ('augustine', 'Works of Augustine', 3, 'On the Trinity'),
  'augustine-on-christian-doctrine':('augustine', 'Works of Augustine', 4, 'On Christian Doctrine'),
  'augustine-enchiridion':          ('augustine', 'Works of Augustine', 5, 'Enchiridion'),
  # Ignatius
  'ignatius':                ('ignatius', 'Letters of Ignatius of Antioch', 0, 'Overview'),
  'ignatius-ephesians':      ('ignatius', 'Letters of Ignatius of Antioch', 1, 'To the Ephesians'),
  'ignatius-magnesians':     ('ignatius', 'Letters of Ignatius of Antioch', 2, 'To the Magnesians'),
  'ignatius-trallians':      ('ignatius', 'Letters of Ignatius of Antioch', 3, 'To the Trallians'),
  'ignatius-romans':         ('ignatius', 'Letters of Ignatius of Antioch', 4, 'To the Romans'),
  'ignatius-philadelphians': ('ignatius', 'Letters of Ignatius of Antioch', 5, 'To the Philadelphians'),
  'ignatius-smyrnaeans':     ('ignatius', 'Letters of Ignatius of Antioch', 6, 'To the Smyrnaeans'),
  'ignatius-polycarp':       ('ignatius', 'Letters of Ignatius of Antioch', 7, 'To Polycarp'),
  # Justin Martyr
  'justin-martyr':          ('justin-martyr', 'Works of Justin Martyr', 0, 'Overview'),
  'justin-first-apology':   ('justin-martyr', 'Works of Justin Martyr', 1, 'First Apology'),
  'justin-second-apology':  ('justin-martyr', 'Works of Justin Martyr', 2, 'Second Apology'),
  'justin-dialogue-trypho': ('justin-martyr', 'Works of Justin Martyr', 3, 'Dialogue with Trypho'),
  # Tertullian
  'tertullian':               ('tertullian', 'Works of Tertullian', 0, 'Overview'),
  'tertullian-apology':       ('tertullian', 'Works of Tertullian', 1, 'Apology'),
  'tertullian-prescription':  ('tertullian', 'Works of Tertullian', 2, 'Prescription Against Heretics'),
  # Athanasius
  'athanasius':                ('athanasius', 'Works of Athanasius', 0, 'Overview'),
  'athanasius-on-incarnation': ('athanasius', 'Works of Athanasius', 1, 'On the Incarnation'),
  'athanasius-life-of-antony': ('athanasius', 'Works of Athanasius', 2, 'Life of Antony'),
  # Gregory of Nazianzus
  'gregory-nazianzus':            ('gregory-nazianzus', 'Works of Gregory of Nazianzus', 0, 'Overview'),
  'gregory-theological-orations': ('gregory-nazianzus', 'Works of Gregory of Nazianzus', 1, 'Five Theological Orations'),
  'gregory-nazianzus-orations':   ('gregory-nazianzus', 'Works of Gregory of Nazianzus', 2, 'Complete Orations'),
  # Irenaeus
  'irenaeus':               ('irenaeus', 'Works of Irenaeus', 0, 'Overview'),
  'irenaeus-against-heresies':('irenaeus', 'Works of Irenaeus', 1, 'Against Heresies'),
  # Chrysostom
  'chrysostom':               ('chrysostom', 'Works of Chrysostom', 0, 'Overview'),
  'chrysostom-on-priesthood': ('chrysostom', 'Works of Chrysostom', 1, 'On the Priesthood'),
  # Andrew Murray
  'murray-humility':                ('andrew-murray', 'Works of Andrew Murray', 1, 'Humility'),
  'murray-deeper-christian-life':   ('andrew-murray', 'Works of Andrew Murray', 2, 'The Deeper Christian Life'),
  'murray-ministry-of-intercession':('andrew-murray', 'Works of Andrew Murray', 3, 'Ministry of Intercession'),
  'murray-lord-teach-us-to-pray':   ('andrew-murray', 'Works of Andrew Murray', 4, 'Lord, Teach Us to Pray'),
  # John Bunyan
  'pilgrims-progress':     ('john-bunyan', 'Works of John Bunyan', 1, "Pilgrim's Progress"),
  'bunyan-holy-war':       ('john-bunyan', 'Works of John Bunyan', 2, 'The Holy War'),
  'bunyan-grace-abounding':('john-bunyan', 'Works of John Bunyan', 3, 'Grace Abounding'),
  # Anselm
  'anselm-proslogion':    ('anselm', 'Works of Anselm of Canterbury', 1, 'Proslogion'),
  'anselm-cur-deus-homo': ('anselm', 'Works of Anselm of Canterbury', 2, 'Cur Deus Homo'),
  # Chesterton
  'chesterton-orthodoxy':       ('chesterton', 'Works of G.K. Chesterton', 1, 'Orthodoxy'),
  'chesterton-everlasting-man': ('chesterton', 'Works of G.K. Chesterton', 2, 'The Everlasting Man'),
  # Leo
  'leo-tome':    ('leo', 'Works of Leo the Great', 1, 'Tome of Leo'),
  'leo-sermons': ('leo', 'Works of Leo the Great', 2, 'Sermons'),
  # Cyprian
  'cyprian-on-unity':     ('cyprian', 'Works of Cyprian of Carthage', 1, 'On the Unity of the Church'),
  'cyprian-on-the-lapsed':('cyprian', 'Works of Cyprian of Carthage', 2, 'On the Lapsed'),
}

with open(IDX) as f:
    index = json.load(f)

patched = 0
for entry in index:
    if entry['id'] in SERIES:
        sid, stitle, vol, vlabel = SERIES[entry['id']]
        entry['series']        = sid
        entry['series_title']  = stitle
        entry['volume']        = vol
        entry['volume_label']  = vlabel
        patched += 1

with open(IDX, 'w') as f:
    json.dump(index, f, indent=2, ensure_ascii=False)
    f.write('\n')

print(f'Patched {patched} entries.')
