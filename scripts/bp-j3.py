#!/usr/bin/env python3
import json, os

OUT_DIR = '../data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def merge_article(slug, data):
    path = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(path):
        return False
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return True

ARTICLES = {
  'jezreel-portion-of': {
    'id': 'jezreel-portion-of', 'term': 'Jezreel, Portion of', 'category': 'places',
    'intro': '<p>The portion of Jezreel refers to the plot of land at Jezreel associated with Naboth\'s vineyard, which King Ahab coveted and Queen Jezebel seized through false accusation and judicial murder. The prophet Elijah declared that on this same ground the blood of Jezebel and her sons would be shed, a prophecy fulfilled when Jehu drove his chariot to the portion of Jezreel and had Jezebel\'s body thrown down from the tower.</p><p>The site became a byword for the consequences of royal injustice and divine retribution, and its memory is woven into the narrative of Ahab\'s dynasty as a place where human cruelty met the judgment of God.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['2 Kings 9:10', '2 Kings 9:21', '2 Kings 9:36', '1 Kings 21:13']
  },
  'jezreel-tower-of': {
    'id': 'jezreel-tower-of', 'term': 'Jezreel, Tower of', 'category': 'places',
    'intro': '<p>The tower of Jezreel was a watchtower or lookout post situated within or near the royal city of Jezreel in the northern kingdom of Israel. It is mentioned in connection with the lookout who watched for Jehu\'s approach during the revolution that overthrew the house of Ahab, spotting the rapid driving of his chariot from a distance before his arrival at the city gates.</p><p>Watchtowers of this kind were standard features of Israelite fortified towns, serving both military and civil functions as observation points over the surrounding plain.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['2 Kings 9:17']
  },
  'jezreel-valley-of': {
    'id': 'jezreel-valley-of', 'term': 'Jezreel, Valley of', 'category': 'places',
    'intro': '<p>The Valley of Jezreel is the great triangular plain stretching across northern Israel between the hill country of Galilee to the north and the ridge of Mount Carmel and Samaria to the south, bounded on the east by the Jordan Valley. Also known as the Plain of Esdraelon, it served as the primary highway between the Mediterranean coast and Transjordan and was the site of numerous decisive battles in biblical history, including Gideon\'s rout of the Midianites and the death of Saul at the hands of the Philistines.</p><p>Its fertility made it central to Israelite agriculture, and its strategic position guaranteed it a role in the major conflicts of every era. Hosea\'s prophecy that God would break the bow of Israel in the Valley of Jezreel gave the name an eschatological dimension later echoed in the imagery of Armageddon.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Joshua 17:16', 'Judges 6:33', 'Hosea 1:5', '1 Samuel 31:1']
  },
  'joab': {
    'id': 'joab', 'term': 'Joab', 'category': 'people',
    'intro': '<p>Joab (meaning: <em>paternity; voluntary</em>), son of Zeruiah and nephew of David, served as the commander-in-chief of David\'s armies throughout most of his reign. Militarily brilliant and fiercely loyal to David\'s throne, he led Israel\'s forces in campaigns against the Ammonites, Syrians, Edomites, and the rebel forces of Absalom. Yet Joab was also capable of ruthless self-interest: he murdered Abner treacherously to avenge his brother Asahel, killed Absalom against David\'s explicit orders, and later assassinated Amasa.</p><p>His support of Adonijah over Solomon sealed his fate; Solomon had him executed at the altar of the tabernacle following David\'s deathbed instruction. Joab stands in Scripture as a man of extraordinary ability whose violence and ambition ultimately undid him.</p>',
    'sections': [], 'hitchcock_meaning': 'paternity; voluntary', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['2 Samuel 2:13', '2 Samuel 10:7', '2 Samuel 11:1', '1 Kings 11:15']
  },
  'joah': {
    'id': 'joah', 'term': 'Joah', 'category': 'people',
    'intro': '<p>Joah (meaning: <em>fraternity; brother of the Lord</em>) is the name of several men in the Old Testament. The most prominent was the son of Obed-edom, a gatekeeper appointed to the tabernacle in David\'s time. Another Joah was among the Levites in Hezekiah\'s time who helped purify the temple, and a third served as royal recorder under King Hezekiah and was part of the delegation that met the Assyrian field commander Rabshakeh at the conduit of the upper pool.</p><p>The name\'s occurrence across multiple periods reflects its common usage in Levitical and royal administrative circles in ancient Judah.</p>',
    'sections': [], 'hitchcock_meaning': 'fraternity; brother of the Lord', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['1 Chronicles 26:4', '1 Chronicles 6:21', '2 Kings 18:18', '2 Kings 18:26']
  },
  'joahaz': {
    'id': 'joahaz', 'term': 'Joahaz', 'category': 'people',
    'intro': '<p>Joahaz (meaning: <em>apprehending; possessing; seeing</em>) was the son of Joah and served as a recorder or secretary under King Josiah, assisting in the oversight of those who repaired the temple during Josiah\'s reform. The name is a shortened variant of Jehoahaz. He is mentioned only in the account of Josiah\'s temple restoration efforts recorded in 2 Chronicles.</p>',
    'sections': [], 'hitchcock_meaning': 'apprehending; possessing; seeing', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['2 Chronicles 34:8']
  },
  'joanna': {
    'id': 'joanna', 'term': 'Joanna', 'category': 'people',
    'intro': '<p>Joanna (meaning: <em>grace or gift of the Lord</em>) was the wife of Chuza, the steward of Herod Antipas, and one of the women healed by Jesus who afterward traveled with him and the Twelve, supporting the ministry from her own resources. She is named among the women who went to the tomb on the morning of the resurrection and brought back word to the apostles that the tomb was empty.</p><p>Her presence in both Galilee and Jerusalem suggests she was a woman of means and consistent devotion, and her connection to Herod\'s household offers a rare window into how Jesus\'s ministry reached even the courts of Jewish client rulers.</p>',
    'sections': [], 'hitchcock_meaning': 'grace or gift of the Lord', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Luke 8:3', 'Luke 24:10', 'Luke 3:27']
  },
  'joash': {
    'id': 'joash', 'term': 'Joash', 'category': 'people',
    'intro': '<p>Joash (meaning: <em>who despairs or burns</em>) is the name of several biblical figures, the most notable being Joash king of Judah, who was hidden in the temple as an infant to save him from Queen Athaliah\'s slaughter of the royal family, then crowned at age seven under the protection of the high priest Jehoiada. His reign saw significant temple repair funded by a systematic collection from the people. Another Joash was the father of Gideon, an Abiezrite of Manasseh, who defended his son after Gideon destroyed the altar of Baal.</p><p>A third Joash was king of Israel, grandson of Jehu, who won three victories over the Syrians as Elisha prophesied on his deathbed.</p>',
    'sections': [], 'hitchcock_meaning': 'who despairs or burns', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Judges 6:11', '2 Kings 12:1', '2 Kings 13:10']
  },
  'job': {
    'id': 'job', 'term': 'Job', 'category': 'people',
    'intro': '<p>Job (meaning: <em>he that weeps or cries</em>) was a man of Uz, described in Scripture as blameless and upright, fearing God and turning away from evil. He is counted among the greatest of the men of the east, possessing vast flocks and a large family, and his name appears alongside Noah and Daniel as a paradigm of righteousness in Ezekiel\'s prophecy. After suffering the catastrophic loss of wealth, children, and health through divinely permitted affliction, Job maintained his integrity while debating the justice of God with three friends.</p><p>The book bearing his name wrestles with the problem of innocent suffering and ends with divine vindication of Job over his friends, the restoration of his fortunes, and the apostolic witness that the Lord is compassionate and merciful to those who endure.</p>',
    'sections': [], 'hitchcock_meaning': 'he that weeps or cries', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Ezekiel 14:14', 'Ezekiel 14:20', 'James 5:11']
  },
  'job-book-of': {
    'id': 'job-book-of', 'term': 'Job, Book of', 'category': 'concepts',
    'intro': '<p>The Book of Job is a poetic and dramatic exploration of innocent suffering, theodicy, and the nature of God\'s governance of the world. Often regarded as among the oldest compositions in Scripture, it consists of a prose prologue and epilogue framing an extended poetic dialogue between Job and his three friends Eliphaz, Bildad, and Zophar, followed by the speeches of the young Elihu and the majestic divine speeches from the whirlwind.</p><p>The book resists easy resolution to the problem of suffering, vindicating Job\'s honest lament while rebuking the friends\' mechanical theology of retribution. Paul quotes from the book in 1 Corinthians, and the New Testament epistle of James holds Job up as a model of patient endurance, pointing to the Lord\'s compassion as the final word of the story.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Ezekiel 14:14', 'James 5:11', '1 Corinthians 3:19']
  },
  'jobab': {
    'id': 'jobab', 'term': 'Jobab', 'category': 'people',
    'intro': '<p>Jobab (meaning: <em>sorrowful, hated</em>) is the name of several persons in the Old Testament. The most prominent was a son of Joktan listed among the early descendants of Shem. Another Jobab was an early king of Edom, son of Zerah of Bozrah, who reigned before any king ruled over Israel. A third Jobab was a Canaanite king of Madon who joined the northern coalition against Joshua and was defeated at the waters of Merom.</p>',
    'sections': [], 'hitchcock_meaning': 'sorrowful, hated', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 10:29', 'Genesis 36:33', 'Joshua 11:1']
  },
  'jochebed': {
    'id': 'jochebed', 'term': 'Jochebed', 'category': 'people',
    'intro': '<p>Jochebed (meaning: <em>glorious; honorable</em>) was the daughter of Levi, wife of Amram, and mother of Moses, Aaron, and Miriam. When Pharaoh decreed the death of all Hebrew male infants, she hid her son Moses for three months and then, unable to conceal him longer, placed him in a waterproofed basket among the reeds of the Nile, where he was discovered and adopted by Pharaoh\'s daughter. Her faith in this act of desperate protection is commended in the New Testament.</p><p>Jochebed is notable as the only woman in the Old Testament explicitly said to be the daughter of Levi, making her the ancestress of Israel\'s priestly and prophetic leadership.</p>',
    'sections': [], 'hitchcock_meaning': 'glorious; honorable', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Numbers 26:59', 'Exodus 6:20']
  },
  'joel': {
    'id': 'joel', 'term': 'Joel', 'category': 'people',
    'intro': '<p>Joel (meaning: <em>he that wills or commands</em>) is the name of a number of men in the Old Testament, the most significant being Joel son of Pethuel, a prophet of Judah whose book is included among the Minor Prophets. Among secular persons named Joel, Samuel\'s firstborn son Joel was appointed judge at Beersheba but is condemned in Scripture for taking bribes, a failure that contributed to Israel\'s demand for a king.</p><p>Other bearers of the name include a Reubenite chief, a Levite of the line of Gershom, and one of David\'s mighty men. The widespread use of the name reflects its meaning — a compound of two names for God — and its appeal in Israel\'s worshipping community.</p>',
    'sections': [], 'hitchcock_meaning': 'he that wills or commands', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Samuel 8:2', '1 Chronicles 5:4', '1 Chronicles 15:7']
  },
  'joel-book-of': {
    'id': 'joel-book-of', 'term': 'Joel, Book of', 'category': 'concepts',
    'intro': '<p>The Book of Joel is a prophetic work attributed to Joel son of Pethuel, addressed to the people of Judah in response to a devastating locust plague. The prophet interprets the disaster as a foretaste of the Day of the Lord and calls the nation to solemn repentance. The second half of the book moves from judgment to promise, culminating in the great prophecy of the Spirit\'s outpouring on all flesh — sons and daughters, servants and handmaids — which Peter identifies as fulfilled on the day of Pentecost.</p><p>Joel is one of the most frequently cited Old Testament prophets in the New Testament, his eschatological imagery shaping both apostolic proclamation and Revelation\'s visions of cosmic judgment and restoration.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Acts 2:16', 'Joel 2:28', 'Joel 2:32']
  },
  'joelah': {
    'id': 'joelah', 'term': 'Joelah', 'category': 'people',
    'intro': '<p>Joelah (meaning: <em>lifting up; profiting; taking away slander</em>) was one of the Benjamite warriors who joined David at Ziklag while David was still restricted in his movements because of Saul. He was a son of Jeroham of Gedor and is listed among the ambidextrous bowmen and slingers who came to David\'s support before his accession to the throne.</p>',
    'sections': [], 'hitchcock_meaning': 'lifting up; profiting; taking away slander', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['1 Chronicles 12:7']
  },
  'joezer': {
    'id': 'joezer', 'term': 'Joezer', 'category': 'people',
    'intro': '<p>Joezer (meaning: <em>he that aids</em>) was a Korhite who came to David at Ziklag, joining the growing band of mighty men who supported David during the period of his conflict with Saul. He is listed among the warriors of the tribe of Benjamin who were skilled with bow and could shoot arrows or sling stones with either hand.</p>',
    'sections': [], 'hitchcock_meaning': 'he that aids', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['1 Chronicles 12:6']
  },
  'johanan': {
    'id': 'johanan', 'term': 'Johanan', 'category': 'people',
    'intro': '<p>Johanan (meaning: <em>who is liberal or merciful</em>) is the name of a number of men in Scripture, the most prominent being the military commander who warned Gedaliah of a plot against his life after the fall of Jerusalem, a warning that went unheeded. After Gedaliah\'s assassination, Johanan led the remnant community in seeking Jeremiah\'s counsel, then defied the prophet\'s word and led the people to Egypt. Another Johanan was the firstborn son of King Josiah, and yet another was the son of Eliashib in the time of Ezra.</p>',
    'sections': [], 'hitchcock_meaning': 'who is liberal or merciful', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Jeremiah 40:8', 'Jeremiah 40:13', '2 Kings 25:23']
  },
  'john': {
    'id': 'john', 'term': 'John', 'category': 'people',
    'intro': '<p>John (meaning: <em>the grace or mercy of the Lord</em>), son of Zebedee and Salome, was one of the Twelve Apostles and, with his brother James, received from Jesus the surname Boanerges — sons of thunder. He was present at the transfiguration and in Gethsemane, and at the crucifixion took Mary the mother of Jesus into his own home at Jesus\'s request. John is traditionally identified as the beloved disciple of the Fourth Gospel and the author of the Johannine epistles and the book of Revelation.</p><p>With Peter and James he formed the inner circle of the apostles, and his ministry in Ephesus and long life made him the last surviving eyewitness of Jesus\'s ministry. Several other men named John appear in the New Testament, including John Mark the evangelist and John the father of Peter.</p>',
    'sections': [], 'hitchcock_meaning': 'the grace or mercy of the Lord', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Matthew 4:21', 'Matthew 10:2', 'Mark 1:19', 'Mark 3:17']
  },
  'john-the-baptist': {
    'id': 'john-the-baptist', 'term': 'John the Baptist', 'category': 'people',
    'intro': '<p>John the Baptist was the son of Zechariah the priest and Elizabeth, a kinswoman of Mary, born six months before Jesus to parents of advanced age following an angelic announcement. He grew in the wilderness until his public appearance at the Jordan, preaching a baptism of repentance and announcing the imminent arrival of the Messiah. Jesus identified him as the Elijah-figure prophesied by Malachi, the greatest of those born of women and the forerunner sent to prepare the Lord\'s way.</p><p>After baptizing Jesus and witnessing the Spirit\'s descent and the Father\'s voice, John was imprisoned by Herod Antipas for condemning his unlawful marriage and eventually beheaded at Herodias\'s instigation. His ministry is described as the turning point between the Law and the Prophets and the new era of the kingdom.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Luke 1:5', 'Matthew 3:3', 'Isaiah 40:3', 'Malachi 3:1']
  },
  'john-first-epistle-of': {
    'id': 'john-first-epistle-of', 'term': 'John, First Epistle of', 'category': 'concepts',
    'intro': '<p>The First Epistle of John is a letter written by the apostle John, traditionally dated to the latter decades of the first century and associated with his ministry at Ephesus. Written to counter an early docetic or proto-Gnostic teaching that denied the full humanity of Christ, the letter insists that the Word who was from the beginning was heard, seen, and handled — a testimony grounded in eyewitness encounter. The epistle is structured around tests of authentic Christian life: confession of the incarnation, love of the brethren, and obedience to the commandments.</p><p>Its central declaration that God is light and God is love, and its exposition of assurance of salvation, have made it one of the most devotionally significant writings in the New Testament canon.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['1 John 1:1', '1 John 4:8', '1 John 5:13']
  },
  'john-gospel-of': {
    'id': 'john-gospel-of', 'term': 'John, Gospel of', 'category': 'concepts',
    'intro': '<p>The Gospel of John, the fourth canonical Gospel, differs markedly in structure and emphasis from the Synoptics, beginning with a prologue identifying Jesus as the eternal Logos who was with God in the beginning and through whom all things were made. The Gospel is organized around seven signs — miraculous works that reveal Jesus\'s glory — and seven great "I am" discourses that identify Jesus with the divine name. Its stated purpose is that readers might believe Jesus is the Christ, the Son of God, and that through believing they might have life in his name.</p><p>Traditionally attributed to the apostle John, son of Zebedee, and composed toward the end of the first century, the Gospel\'s theological depth and Christological precision have made it foundational for the church\'s understanding of the incarnation and eternal life.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['John 20:31', 'John 1:1', 'John 1:14']
  },
  'john-second-epistle-of': {
    'id': 'john-second-epistle-of', 'term': 'John, Second Epistle of', 'category': 'concepts',
    'intro': '<p>The Second Epistle of John is the shortest book in the New Testament, a brief letter from "the elder" addressed to an "elect lady and her children," most likely a local church or a prominent Christian woman and her household. The letter warns against offering hospitality to traveling teachers who deny that Jesus Christ has come in the flesh, striking the same anti-docetic note found in 1 John. It emphasizes walking in truth and love and urges vigilance against those who go beyond the teaching of Christ.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['2 John 1:1', '2 John 1:7', '2 John 1:10']
  },
  'john-third-epistle-of': {
    'id': 'john-third-epistle-of', 'term': 'John, Third Epistle of', 'category': 'concepts',
    'intro': '<p>The Third Epistle of John is a personal letter from "the elder" to a man named Gaius, commending him for his faithful hospitality to traveling missionaries and contrasting his conduct with that of Diotrephes, who refused to welcome the brethren and expelled from the church those who did. A third figure, Demetrius, is commended as having a good testimony from all. The letter provides a rare glimpse into the practical mechanics of early Christian itinerant mission and the authority disputes within local congregations.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['3 John 1:1', 'Romans 16:23', 'Acts 19:29']
  },
  'joiada': {
    'id': 'joiada', 'term': 'Joiada', 'category': 'people',
    'intro': '<p>Joiada was a high priest of Israel in the post-exilic period, son of Eliashib and grandson of the first high priest after the return from Babylon. He is listed in the genealogy of priests recorded in Nehemiah. One of his sons married the daughter of Sanballat the Horonite, and Nehemiah expelled him from Jerusalem for this breach of the law of mixed marriages. Joiada stands in the line of high-priestly succession spanning the restoration period.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Nehemiah 3:6', 'Nehemiah 12:10', 'Nehemiah 13:28']
  },
  'joiakim': {
    'id': 'joiakim', 'term': 'Joiakim', 'category': 'people',
    'intro': '<p>Joiakim was a high priest of Israel during the restoration period, son of Jeshua the first post-exilic high priest and father of Eliashib. He held the high priesthood during the time of Nehemiah\'s predecessor and is associated with the heads of the priestly families who served in his day. His name appears in the records of the Levitical courses and the priestly genealogy preserved in Nehemiah\'s memoirs.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Nehemiah 12:10', 'Nehemiah 12:12', 'Nehemiah 12:26']
  },
  'joiarib': {
    'id': 'joiarib', 'term': 'Joiarib', 'category': 'people',
    'intro': '<p>Joiarib (meaning: <em>chiding, or multiplying, of the Lord</em>) is the name of several persons in the post-exilic books. One was a leading man at Casiphia whom Ezra sent to find Levites for the return journey to Jerusalem. Another was a Judahite ancestor of Maaseiah who settled in Jerusalem after the exile. A third was the head of the first priestly division in the reorganization of priestly families recorded in Nehemiah, ancestor of the Maccabean priestly dynasty.</p>',
    'sections': [], 'hitchcock_meaning': 'chiding, or multiplying, of the Lord', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Ezra 8:16', 'Nehemiah 11:5', 'Nehemiah 11:10']
  },
  'jokdeam': {
    'id': 'jokdeam', 'term': 'Jokdeam', 'category': 'places',
    'intro': '<p>Jokdeam (meaning: <em>crookedness, or burning, of the people</em>) was a town in the hill country of Judah, listed in the tribal allotments of Joshua alongside Maon and Carmel. Its precise location is uncertain, but it lay in the southern highlands of the territory assigned to Judah. The town is mentioned only in the boundary and city lists of Joshua and does not appear in later biblical narratives.</p>',
    'sections': [], 'hitchcock_meaning': 'crookedness, or burning, of the people', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Joshua 15:56']
  },
  'jokim': {
    'id': 'jokim', 'term': 'Jokim', 'category': 'people',
    'intro': '<p>Jokim (meaning: <em>that made the sun stand still</em>) was a descendant of Judah through the line of Shelah, listed in the genealogical records of 1 Chronicles among the clan of Judah. He appears only in this genealogical passage and is otherwise unknown in the biblical narrative. His name suggests a connection to the tradition of divine intervention associated with Joshua\'s long day.</p>',
    'sections': [], 'hitchcock_meaning': 'that made the sun stand still', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['1 Chronicles 4:22']
  },
  'jokmeam': {
    'id': 'jokmeam', 'term': 'Jokmeam', 'category': 'places',
    'intro': '<p>Jokmeam (meaning: <em>confirmation, or revenge, of the people</em>) was a Levitical city assigned to the Kohathite clan from the tribe of Ephraim. It is also mentioned in a list of Solomon\'s administrative districts as a town in the fourth district. The site is associated with a location in the Jordan Valley and may be the same as Kibzaim mentioned in an earlier list of Levitical cities, though scholars debate the identification.</p>',
    'sections': [], 'hitchcock_meaning': 'confirmation, or revenge, of the people', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['1 Chronicles 6:68', '1 Kings 4:12']
  },
  'jokneam': {
    'id': 'jokneam', 'term': 'Jokneam', 'category': 'places',
    'intro': '<p>Jokneam (meaning: <em>possessing, or building up, of the people</em>) was a Canaanite royal city in the territory of Zebulun whose king was defeated by Joshua. It was subsequently assigned as a Levitical city to the Merarite clan from Zebulun\'s territory. The city commanded an important pass through the Carmel ridge where the Kishon River enters the Jezreel Valley, giving it strategic significance in controlling traffic between the coast and the interior of Canaan.</p>',
    'sections': [], 'hitchcock_meaning': 'possessing, or building up, of the people', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Joshua 19:11', 'Joshua 21:34']
  },
  'jokshan': {
    'id': 'jokshan', 'term': 'Jokshan', 'category': 'people',
    'intro': '<p>Jokshan (meaning: <em>an offense; hardness; a knocking</em>) was the second son of Abraham by Keturah, his wife after Sarah\'s death. He was the father of Sheba and Dedan, ancestors of Arabian tribes. The descendants of Jokshan represent part of the broader family of Abraham\'s sons by Keturah who were sent eastward and became the progenitors of various Semitic peoples in Arabia and Transjordan.</p>',
    'sections': [], 'hitchcock_meaning': 'an offense; hardness; a knocking', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 25:2', 'Genesis 25:3', '1 Chronicles 1:32']
  },
  'joktan': {
    'id': 'joktan', 'term': 'Joktan', 'category': 'people',
    'intro': '<p>Joktan (meaning: <em>small dispute; contention; disgust</em>) was the second son of Eber in the genealogy of Shem, and the brother of Peleg, in whose days the earth was divided. Joktan is the progenitor of thirteen Arabian peoples listed in the Table of Nations in Genesis 10, including Hazarmaveth, Jerah, and Havilah. He is generally identified as the ancestor of the southern Arabian peoples, making the Joktanide tribes one of the major branches of Semitic civilization in the ancient world.</p>',
    'sections': [], 'hitchcock_meaning': 'small dispute; contention; disgust', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 10:25', '1 Chronicles 1:19']
  },
  'joktheel': {
    'id': 'joktheel', 'term': 'Joktheel', 'category': 'places',
    'intro': '<p>Joktheel is the name of two places in the Old Testament. One was a town in the lowland of Judah, listed in the cities of the Shephelah in Joshua\'s tribal allotments. The other, more significant use is as the name given by King Amaziah of Judah to the Edomite city of Sela after he captured it in battle, killing ten thousand Edomites. This Sela, also known as Petra, was the great cliff-city of Edom in the mountains of Seir.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Joshua 15:38', '2 Kings 14:7', '2 Chronicles 25:12']
  },
  'jonadab': {
    'id': 'jonadab', 'term': 'Jonadab', 'category': 'people',
    'intro': '<p>Jonadab (meaning: <em>who gives liberally</em>) is the name of two notable biblical figures. The first was a nephew of David, described as a very crafty man, who advised Amnon on how to lure his half-sister Tamar and is thus morally implicated in the rape that precipitated Absalom\'s vengeance. The second and more honored Jonadab was the son of Rechab, who met Jehu during his purge of Baal worship and endorsed his reform, and whose clan maintained a vow of ascetic simplicity that Jeremiah later used as an object lesson of faithful obedience.</p>',
    'sections': [], 'hitchcock_meaning': 'who gives liberally', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['2 Kings 10:15', 'Jeremiah 35:6', '2 Samuel 13:3']
  },
  'jonah': {
    'id': 'jonah', 'term': 'Jonah', 'category': 'people',
    'intro': '<p>Jonah (meaning: <em>a dove; he that oppresses; destroyer</em>), son of Amittai of Gath-hepher in Zebulun, was a prophet who predicted the restoration of Israel\'s borders under Jeroboam II. He is best known for the divine commission to preach repentance to Nineveh, which he attempted to flee by sea, was swallowed by a great fish for three days and nights, and after deliverance fulfilled his mission — to his own dismay when the city repented and God relented from judgment.</p><p>Jesus cited Jonah\'s three days in the fish as a sign of his own death and resurrection, making Jonah a typological figure of central importance to the New Testament\'s understanding of redemption and the mission to the nations.</p>',
    'sections': [], 'hitchcock_meaning': 'a dove; he that oppresses; destroyer', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['2 Kings 14:25', 'Matthew 12:39', 'Matthew 12:40']
  },
  'jonah-book-of': {
    'id': 'jonah-book-of', 'term': 'Jonah, Book of', 'category': 'concepts',
    'intro': '<p>The Book of Jonah is unique among the Minor Prophets in being primarily a narrative about the prophet rather than a collection of his oracles. It recounts Jonah\'s flight from his divine commission, his rescue by a great fish, his eventual preaching to Nineveh, and his subsequent complaint when God spared the city. The book\'s climax is a divine question about the breadth of God\'s compassion for all peoples, including Israel\'s enemies.</p><p>Jesus appealed to the sign of Jonah as a prefiguration of his own burial and resurrection and cited the Ninevites\'  repentance as a rebuke to his contemporaries\' unbelief, giving the book enduring christological significance in the New Testament.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Matthew 12:39', 'Matthew 12:40', 'Luke 11:29']
  },
  'jonas': {
    'id': 'jonas', 'term': 'Jonas', 'category': 'people',
    'intro': '<p>Jonas is the Greek and New Testament form of the Hebrew name Jonah. In the New Testament it appears in two distinct contexts: first, as the name Jesus uses for the prophet Jonah when citing the sign of Jonah as a foreshadowing of his resurrection; and second, as the name of Simon Peter\'s father — "Simon Bar-Jonas" (son of Jonas) — used by Jesus at the great confession at Caesarea Philippi and again at the post-resurrection restoration of Peter by the Sea of Galilee.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Matthew 12:39', 'Matthew 12:41', 'John 21:15']
  },
  'jonath-elem-rechokim': {
    'id': 'jonath-elem-rechokim', 'term': 'Jonath-elem-rechokim', 'category': 'concepts',
    'intro': '<p>Jonath-elem-rechokim is a musical or liturgical notation in the heading of Psalm 56, understood to mean "the silent dove of far-off places" or "dove of the distant terebinths." It is generally interpreted as the name of a tune or melody to which the psalm was to be sung, a common practice of indicating performance style in the psalter superscriptions. The psalm itself is attributed to David during his detention among the Philistines in Gath, giving the imagery of a distant and silent dove a poignant biographical context.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Psalms 56:1']
  },
  'jonathan': {
    'id': 'jonathan', 'term': 'Jonathan', 'category': 'people',
    'intro': '<p>Jonathan (meaning: <em>given of God</em>), eldest son of King Saul, is celebrated in Scripture for his covenant friendship with David, his military courage, and his loyalty that transcended political loyalty to his own dynasty. He initiated Israel\'s deliverance from Philistine occupation with a bold two-man assault on the garrison at Michmash, and he twice intervened to protect David from Saul\'s murderous jealousy at the cost of his own inheritance. His lament by David — "your love to me was wonderful, surpassing the love of women" — is among the most memorable elegies in the Bible.</p><p>Jonathan was killed alongside his father and brothers at the battle of Mount Gilboa. Several other men named Jonathan appear in Scripture, including a Levite priest of the tribe of Dan and various minor figures in Chronicles, Ezra, and Nehemiah.</p>',
    'sections': [], 'hitchcock_meaning': 'given of God', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Samuel 13:2', '2 Samuel 1:23', '1 Samuel 18:1']
  },
  'joppa': {
    'id': 'joppa', 'term': 'Joppa', 'category': 'places',
    'intro': '<p>Joppa (meaning: <em>beauty; comeliness</em>), the modern city of Jaffa on the Mediterranean coast of Israel, was the principal seaport serving Jerusalem, located about thirty-five miles northwest of the capital. The cedars of Lebanon floated down to Joppa for the building of both Solomon\'s temple and the second temple after the return from exile. Jonah departed from Joppa when fleeing his commission to Nineveh.</p><p>In the New Testament, the disciple Tabitha (Dorcas) lived in Joppa and was raised from the dead by Peter, who subsequently lodged there with Simon the tanner. It was at Joppa that Peter received the vision of the sheet descending from heaven, preparing him for the mission to the household of Cornelius at Caesarea.</p>',
    'sections': [], 'hitchcock_meaning': 'beauty; comeliness', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Jonah 1:3', 'Acts 9:36', 'Ezra 3:7', '2 Chronicles 2:16']
  },
  'joram': {
    'id': 'joram', 'term': 'Joram', 'category': 'people',
    'intro': '<p>Joram (meaning: <em>to cast; elevated</em>) is the name of two contemporary kings — one of Israel and one of Judah — who reigned during the same period and were related by marriage. Joram king of Israel, son of Ahab, continued his parents\' Baal worship though less ardently, and was wounded in battle against Hazael of Syria at Ramoth-gilead. Joram (also called Jehoram) king of Judah was the son of Jehoshaphat and married Ahab\'s daughter Athaliah, whose influence drew him into Baal worship; he was plagued with disease and died without honor.</p><p>Both Jorams fell in the period of Jehu\'s coup: the Israelite king was shot by Jehu\'s arrow at Naboth\'s field, while the Judahite king\'s wife Athaliah subsequently seized the throne of Jerusalem.</p>',
    'sections': [], 'hitchcock_meaning': 'to cast; elevated', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['2 Kings 8:16', '2 Kings 8:25', '2 Kings 8:28']
  },
  'jordan': {
    'id': 'jordan', 'term': 'Jordan', 'category': 'places',
    'intro': '<p>The Jordan (meaning: <em>the river of judgment</em>) is the chief river of Palestine, flowing south from the slopes of Mount Hermon through the Sea of Galilee and down through the Jordan Rift Valley to the Dead Sea, a distance of about two hundred miles along its winding course. The river forms the eastern boundary of Canaan proper and was miraculously parted to allow Israel\'s crossing under Joshua, as it had been when Elijah and Elisha crossed on dry ground.</p><p>In the New Testament the Jordan is the site of John the Baptist\'s ministry and of Jesus\'s baptism, at which the Spirit descended as a dove and the Father\'s voice declared Jesus his beloved Son. This event gave the river permanent significance in Christian baptismal theology as the antitype of Israel\'s crossing into the promised land.</p>',
    'sections': [], 'hitchcock_meaning': 'the river of judgment', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Matthew 3:5', 'Genesis 13:10', 'Joshua 3:17', 'Psalms 114:3']
  },
  'joseph': {
    'id': 'joseph', 'term': 'Joseph', 'category': 'people',
    'intro': '<p>Joseph (meaning: <em>increase; addition</em>), the eleventh son of Jacob and firstborn of Rachel, is the subject of the longest continuous narrative about a single individual in Genesis. Sold into slavery by his brothers, he rose to become second in command of Egypt through divine gift of dream interpretation, and his position enabled him to preserve his family during the great famine. His forgiveness of his brothers — "you meant evil against me, but God meant it for good" — is among the most profound statements of providential theology in the Old Testament.</p><p>In the New Testament, Joseph of Nazareth, the husband of Mary and legal father of Jesus, was a carpenter of Davidic descent through whom Jesus\'s royal lineage was legally reckoned. Several other Josephs appear in the Gospels, including Joseph of Arimathea, the wealthy council member who provided his tomb for Jesus\'s burial.</p>',
    'sections': [], 'hitchcock_meaning': 'increase; addition', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 30:23', 'Genesis 37:3', 'Genesis 37:36', 'Genesis 50:20']
  },
  'joshua': {
    'id': 'joshua', 'term': 'Joshua', 'category': 'people',
    'intro': '<p>Joshua (meaning: <em>a savior; a deliverer</em>), son of Nun of the tribe of Ephraim, was Moses\'s military commander and personal attendant, one of the two faithful spies who urged Israel to trust God and enter Canaan, and Moses\'s divinely appointed successor as leader of Israel. Under his leadership Israel crossed the Jordan, captured Jericho and Ai, defeated the Canaanite coalitions in both the south and north, and divided the land among the twelve tribes. The Hebrew form of his name — Yehoshua — is identical to Jesus, a connection the New Testament writers employed to present Jesus as the true Joshua who brings God\'s people into their inheritance.</p><p>Other men named Joshua appear in the Old Testament, including the high priest Joshua who returned from Babylon and presided over the restoration of the altar and temple in the time of Zerubbabel.</p>',
    'sections': [], 'hitchcock_meaning': 'a savior; a deliverer', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Numbers 13:16', 'Acts 7:45', 'Hebrews 4:8', 'Exodus 17:8']
  },
  'joshua-the-book-of': {
    'id': 'joshua-the-book-of', 'term': 'Joshua, The Book of', 'category': 'concepts',
    'intro': '<p>The Book of Joshua records Israel\'s conquest and settlement of Canaan under Joshua\'s leadership, presenting the fulfillment of God\'s promises to Abraham that his descendants would inherit the land. The book divides into three main sections: the campaigns of conquest, the division of the land among the tribes, and Joshua\'s farewell addresses and covenant renewal at Shechem. It is closely connected to Deuteronomy in both theology and style, presenting the conquest as the outworking of Mosaic covenant faithfulness.</p><p>The book\'s opening miracle at the Jordan and the account of the sun standing still at Gibeon frame the conquest as a sustained act of divine warfare, while the inclusion of Rahab and the Gibeonites demonstrates that the promised land\'s boundaries encompass repentant Gentiles who shelter under Israel\'s God.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Joshua 10:12', 'Joshua 1:1', 'Joshua 24:1']
  },
  'josiah': {
    'id': 'josiah', 'term': 'Josiah', 'category': 'people',
    'intro': '<p>Josiah (meaning: <em>the Lord burns; the fire of the Lord</em>) was king of Judah from approximately 640 to 609 B.C., ascending the throne at age eight following his father Amon\'s assassination. He instituted the most sweeping religious reform in Judah\'s history, purging the temple and land of Baal altars, Asherah poles, and high places, destroying the ancient high place at Bethel, and reinstating the Passover on a scale unprecedented since the days of the judges. The discovery of the Book of the Law during temple repairs prompted both personal repentance and national covenant renewal.</p><p>Jeremiah prophesied during his reign, and the prophetess Huldah confirmed that divine judgment on Judah was deferred because of Josiah\'s penitence. He was killed at Megiddo while attempting to intercept Pharaoh Necho\'s army, and his death was mourned by Jeremiah and the entire nation.</p>',
    'sections': [], 'hitchcock_meaning': 'the Lord burns; the fire of the Lord', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['2 Kings 22:1', '2 Chronicles 34:1', '2 Kings 23:1', 'Jeremiah 25:3']
  },
  'jot': {
    'id': 'jot', 'term': 'Jot', 'category': 'concepts',
    'intro': '<p>Jot is the English rendering of iota, the smallest letter of the Greek alphabet, used in the Authorized Version of Matthew 5:18 where Jesus declares that not one jot or tittle will pass from the law until all is fulfilled. The underlying Hebrew concept is the <em>yod</em>, the smallest letter of the Hebrew alphabet, which Jesus uses to affirm the permanent authority and complete fulfillment of the Mosaic law. The pairing of jot with tittle — a small decorative stroke on Hebrew letters — emphasizes that even the minutest scribal detail of Scripture carries divine weight.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Matthew 5:18']
  },
  'jotham': {
    'id': 'jotham', 'term': 'Jotham', 'category': 'people',
    'intro': '<p>Jotham (meaning: <em>the perfection of the Lord</em>) is the name of two men in the Old Testament. The more prominent is Jotham son of Uzziah (Azariah), who served first as co-regent when his father was struck with leprosy and then reigned as sole king of Judah for sixteen years. He is commended for personal righteousness, building work on Jerusalem\'s wall and the Upper Gate of the temple, and military success against the Ammonites — though the high places were not removed during his reign. The other Jotham was the youngest son of Gideon who escaped Abimelech\'s slaughter, delivered the famous fable of the trees choosing a king, and pronounced a curse on the men of Shechem for their treachery.</p>',
    'sections': [], 'hitchcock_meaning': 'the perfection of the Lord', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Judges 9:5', '2 Chronicles 26:21', '2 Kings 15:5']
  },
  'journey': {
    'id': 'journey', 'term': 'Journey', 'category': 'concepts',
    'intro': '<p>In biblical usage, journey most often refers to a measured unit of travel, particularly the "sabbath day\'s journey," which Acts 1:12 records as the distance from the Mount of Olives to Jerusalem. Jewish tradition fixed this at approximately two thousand cubits (about half a mile or nine hundred meters), based on the maximum distance Israelites were permitted to travel outside their camp on the Sabbath according to Numbers 35:5. The limitation reflects the Sabbath law\'s intent to restrict labor and movement while permitting attendance at the tabernacle or synagogue.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Acts 1:12', 'Numbers 11:31', 'Exodus 16:29']
  },
  'jozabad': {
    'id': 'jozabad', 'term': 'Jozabad', 'category': 'people',
    'intro': '<p>Jozabad is the name of at least ten different individuals in the Old Testament, reflecting the name\'s popularity in the post-Davidic period. Among the most notable: two Manassite chiefs who deserted to David before the battle of Jezreel, a Levite who assisted in distributing the holy offerings during Hezekiah\'s reform, a chief of the Levites who helped oversee the rebuilding of the temple in Nehemiah\'s time, and several priests and laymen who had taken foreign wives and dissolved the marriages during Ezra\'s reform.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['1 Chronicles 12:4', '1 Chronicles 12:20']
  },
  'jozachar': {
    'id': 'jozachar', 'term': 'Jozachar', 'category': 'people',
    'intro': '<p>Jozachar (meaning: <em>remembering; of the male sex</em>) was a servant of King Joash of Judah who conspired with Jehozabad to assassinate the king at Beth-millo. The account in 2 Kings names him Jozachar son of Shimeath, while 2 Chronicles calls him Zabad son of Shimeath. After the murder Jozachar was executed by King Amaziah, who succeeded Joash, though the conspirators\' children were spared in accordance with the law of Deuteronomy that forbids punishing children for their fathers\' sins.</p>',
    'sections': [], 'hitchcock_meaning': 'remembering; of the male sex', 'source_ids': ['easton', 'smith'],
    'key_refs': ['2 Kings 12:21', '2 Chronicles 24:26']
  },
  'jubal': {
    'id': 'jubal', 'term': 'Jubal', 'category': 'people',
    'intro': '<p>Jubal (meaning: <em>he that runs; a trumpet</em>) was the son of Lamech and Adah in the antediluvian genealogy of Cain, and is identified in Genesis as "the father of all those who play the lyre and pipe" — that is, the originator of musical arts among humanity. His name may be connected to the Hebrew <em>yobel</em>, which denotes the jubilee trumpet, suggesting an etymological link between Jubal and the musical traditions of Israel\'s later worship. He was a brother of Jabal, the ancestor of tent-dwellers and herders, and a half-brother of Tubal-cain, the forger of metal tools.</p>',
    'sections': [], 'hitchcock_meaning': 'he that runs; a trumpet', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 4:21']
  },
  'jubilee': {
    'id': 'jubilee', 'term': 'Jubilee', 'category': 'concepts',
    'intro': '<p>The Jubilee was the fiftieth year in Israel\'s liturgical calendar, inaugurated by the sounding of the ram\'s horn (yobel) on the Day of Atonement and observed every seven cycles of seven years. Its defining provisions, laid out in Leviticus 25, required the release of all Hebrew slaves to their families, the return of all ancestral land to its original tribal families, and the cessation of agricultural labor. The system was designed to prevent the permanent accumulation of land and wealth by a small class and to protect the economic viability of each Israelite household across generations.</p><p>Whether the Jubilee was ever fully observed is uncertain; Isaiah appears to echo its language in the great proclamation of liberty in chapter 61, which Jesus applied to himself at the synagogue in Nazareth, interpreting his own ministry as the ultimate Jubilee of God\'s kingdom.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Leviticus 25:11', 'Leviticus 25:12', 'Isaiah 61:1', 'Luke 4:18']
  },
  'juda': {
    'id': 'juda', 'term': 'Juda', 'category': 'people',
    'intro': '<p>Juda is the Greek form of the Hebrew name Judah as it appears in New Testament genealogies. In Luke\'s genealogy of Jesus it designates an ancestor of Joseph. In Hebrews 7:14 the form "Juda" (or Judah) is used to identify the tribe from which Jesus descended, noting that Moses spoke nothing about priests from that tribe, underscoring the novelty of Christ\'s high priesthood according to the order of Melchizedek. The name also appears in Revelation as the tribe of Judah from which the Lion is identified.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Luke 3:33', 'Hebrews 7:14', 'Revelation 5:5']
  },
  'judah': {
    'id': 'judah', 'term': 'Judah', 'category': 'people',
    'intro': '<p>Judah (meaning: <em>the praise of the Lord; confession</em>) was the fourth son of Jacob by Leah, and the patriarch from whom the tribe of Judah descended. He persuaded his brothers to sell Joseph rather than kill him, offered himself as a surety for Benjamin before the unknown Joseph in Egypt, and received from his father Jacob the messianic blessing: "the scepter shall not depart from Judah, nor the ruler\'s staff from between his feet, until tribute comes to him." This oracle established Judah as the royal tribe from which David and, ultimately, Jesus the Messiah descended.</p><p>The name Judah became the designation for the southern kingdom after the division of the monarchy, and later for the province of Judea under Persian, Greek, and Roman administration. The Jewish people take their name from this patriarch.</p>',
    'sections': [], 'hitchcock_meaning': 'the praise of the Lord; confession', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 29:35', 'Genesis 37:26', 'Genesis 44:14', 'Genesis 49:10']
  },
  'judah-upon-jordan': {
    'id': 'judah-upon-jordan', 'term': 'Judah upon Jordan', 'category': 'places',
    'intro': '<p>Judah upon Jordan is a phrase found in the boundary description of the tribe of Naphtali in Joshua 19:34, where the territory touches "Judah at the Jordan." The reference likely designates a specific ford or district on the eastern bank of the Jordan that marked the boundary point between the tribal territories in the region of the Jordan River\'s upper course near the Sea of Galilee. The precise identification of the location has been debated by biblical geographers, and it may reflect a now-lost tribal settlement or landmark.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Joshua 19:34']
  },
  'judah-kingdom-of': {
    'id': 'judah-kingdom-of', 'term': 'Judah, Kingdom of', 'category': 'places',
    'intro': '<p>The Kingdom of Judah was the southern Israelite state formed after the division of the united monarchy following Solomon\'s death, consisting of the tribes of Judah and Benjamin and centered on Jerusalem. It was ruled by the Davidic dynasty continuously for nearly three and a half centuries, from Rehoboam (c. 930 B.C.) until the Babylonian destruction of Jerusalem under Zedekiah (586 B.C.). Its kings ranged from reformers like Jehoshaphat, Hezekiah, and Josiah to deeply apostate rulers like Manasseh.</p><p>The prophets Isaiah, Jeremiah, Micah, and others addressed their oracles primarily to Judah, and its survival long after the fall of the northern kingdom of Israel was attributed by those prophets to God\'s faithfulness to the Davidic covenant and his purpose for the temple and the city he had chosen.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['2 Kings 25:8', '1 Kings 12:20', '2 Chronicles 36:1']
  },
  'judah-tribe-of': {
    'id': 'judah-tribe-of', 'term': 'Judah, Tribe of', 'category': 'people',
    'intro': '<p>The Tribe of Judah was the largest and most prominent of the twelve tribes of Israel, numbering 74,600 men of military age at the first Sinai census and marching at the head of Israel\'s camp in the wilderness. Its territory after the conquest extended across the southern highlands of Canaan, including Hebron, Bethlehem, and the Shephelah, and bordered the Dead Sea to the east and the Negev desert to the south. Caleb the faithful spy was from Judah, and the tribe was granted the privilege of leading the military campaigns after Joshua\'s death.</p><p>David\'s rise from the tribe of Judah fulfilled Jacob\'s deathbed prophecy, and the tribe\'s primacy was permanently established with the Davidic covenant. The New Testament identifies Jesus as the Lion of the tribe of Judah.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Numbers 1:26', 'Numbers 2:3', 'Genesis 49:10', 'Revelation 5:5']
  },
  'judas': {
    'id': 'judas', 'term': 'Judas', 'category': 'people',
    'intro': '<p>Judas (meaning: <em>the praise of the Lord; confession</em> — the Greek form of Judah) is the name of several New Testament figures. The most notorious is Judas Iscariot, one of the Twelve Apostles, who betrayed Jesus to the chief priests for thirty pieces of silver and afterward hanged himself in remorse. His betrayal is presented in the Gospels as both a human act of greed and treachery and the fulfillment of prophetic Scripture.</p><p>A second apostle named Judas — called "not Iscariot" by John and identified as Thaddaeus in the Synoptics — asked Jesus at the Last Supper why he would manifest himself to the disciples and not to the world. Another Judas was a brother of Jesus listed in the Gospels, possibly the author of the Epistle of Jude. Judas of Galilee led a revolt against the Roman census in A.D. 6.</p>',
    'sections': [], 'hitchcock_meaning': 'Jude, same as Judah', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Matthew 1:2', 'John 6:71', 'John 13:2', 'Acts 1:16']
  },
  'jude': {
    'id': 'jude', 'term': 'Jude', 'category': 'people',
    'intro': '<p>Jude (the English form of Judas) identifies himself at the opening of the epistle bearing his name as "a servant of Jesus Christ and brother of James," which most interpreters take to mean he was a brother of Jesus, as James was also a brother of the Lord. Like his brother James, Jude apparently did not believe in Jesus during his earthly ministry but became a follower after the resurrection. He is listed among the brothers of Jesus named in the Synoptic Gospels and may be the "Judas not Iscariot" who questioned Jesus at the Last Supper, though this identification is uncertain.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Jude 1:1', 'Matthew 13:55', 'John 14:22']
  },
  'jude-epistle-of': {
    'id': 'jude-epistle-of', 'term': 'Jude, Epistle of', 'category': 'concepts',
    'intro': '<p>The Epistle of Jude is a brief but intense letter written by Jude, a brother of James and likely of Jesus, addressed to Christians facing the infiltration of antinomian teachers who were using grace as a license for immorality and denying Jesus Christ as Lord. Jude marshals a series of Old Testament examples — the wilderness generation, the fallen angels, Sodom and Gomorrah — alongside references to the pseudepigraphical books of Enoch and the Assumption of Moses to warn against apostasy and urge his readers to contend for the faith.</p><p>The epistle shares significant material with 2 Peter 2 and is noted for its Jewish apocalyptic idiom and its closing doxology, one of the most majestic in the New Testament.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Jude 1:1', 'Jude 1:3', 'Matthew 10:3']
  },
  'judea': {
    'id': 'judea', 'term': 'Judea', 'category': 'places',
    'intro': '<p>Judea is the Greco-Roman name for the region of southern Palestine corresponding to the ancient tribal territory of Judah and Benjamin. After the Babylonian exile, the returning community centered in Jerusalem gave the name Judah (rendered in Greek as Ioudaia and in Latin as Judaea) to the province governed first under the Persians, then under Alexander\'s successors, the Maccabees, and finally under Roman administration. Its boundaries varied across periods but consistently centered on Jerusalem, Bethlehem, Hebron, and Jericho.</p><p>In the New Testament Judea is frequently contrasted with Galilee and Samaria as one of the three main regions of the Holy Land, and it is the setting for Jesus\'s birth, his trial and crucifixion, and the earliest Christian community at Jerusalem.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Matthew 2:1', 'Haggai 1:1', 'Luke 1:65', 'Acts 1:8']
  },
  'judge': {
    'id': 'judge', 'term': 'Judge', 'category': 'concepts',
    'intro': '<p>In the Old Testament, judges served as local leaders appointed to arbitrate disputes and administer justice according to Mosaic law, with Moses himself as the originating figure who delegated judicial authority to capable men able to handle the volume of cases among the Israelites. In the period between Joshua and the monarchy, the term "judge" referred to a series of charismatic military deliverers raised up by God to rescue Israel from foreign oppression — figures like Othniel, Deborah, Gideon, and Samson — whose authority was derived from the Spirit rather than hereditary succession.</p><p>The prophets consistently called Israel\'s judges to justice for the poor and vulnerable, and the New Testament presents God himself as the ultimate judge of all the earth, with final judgment entrusted to Jesus Christ.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Judges 2:18', 'Exodus 2:14', 'Judges 10:1']
  },
  'judges-book-of': {
    'id': 'judges-book-of', 'term': 'Judges, Book of', 'category': 'concepts',
    'intro': '<p>The Book of Judges records the history of Israel from the death of Joshua to the eve of the monarchy, covering the era of the charismatic deliverers sent by God to rescue Israel from the cycles of apostasy, foreign oppression, repentance, and deliverance that structure the book\'s theology. Its famous refrain — "In those days there was no king in Israel; everyone did what was right in his own eyes" — frames the period as one of moral and political chaos arising from covenant unfaithfulness.</p><p>The book includes the stories of twelve judges, the greatest being Gideon, Deborah, Jephthah, and Samson, as well as the troubling appendices recounting the Danite migration and the Benjamite civil war. It serves as a theological prelude to the books of Samuel and the establishment of the Davidic monarchy.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Judges 2:16', '1 Samuel 7:2', 'Judges 21:25']
  },
  'judgment-hall': {
    'id': 'judgment-hall', 'term': 'Judgment hall', 'category': 'places',
    'intro': '<p>The judgment hall — the Greek <em>praetorium</em> — was the official residence and administrative headquarters of a Roman governor, used for judicial proceedings and executive functions. In the Gospels the term designates the palace or headquarters of Pontius Pilate in Jerusalem where Jesus was brought after his arrest and tried before sentence of crucifixion was pronounced. The praetorium may have been the Antonia Fortress adjacent to the temple or Herod\'s palace on the western hill of Jerusalem, a question debated by archaeologists.</p><p>Paul uses the same Greek term in Philippians to indicate that his imprisonment had become known throughout the whole praetorian guard, likely referring to the imperial household troops in Rome.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['John 18:28', 'Matthew 27:27', 'Mark 15:16']
  },
  'judgment-seat': {
    'id': 'judgment-seat', 'term': 'Judgment seat', 'category': 'concepts',
    'intro': '<p>The judgment seat — the Greek <em>bema</em> — was an elevated platform or tribunal from which a magistrate delivered official rulings, awarded prizes, or pronounced verdicts. In the Gospels and Acts it designates the official tribunal of Pilate at the Pavement (Gabbatha) and later the judgment seats of Gallio at Corinth and Festus at Caesarea. The New Testament authors adopt the term for eschatological purposes: Paul writes in Romans and 2 Corinthians that all believers will stand before the judgment seat (bema) of Christ or of God to give account of their deeds, though the context in 2 Corinthians emphasizes reward rather than condemnation for the justified.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Matthew 27:19', 'Romans 14:10', '2 Corinthians 5:10']
  },
  'judgment-the-final': {
    'id': 'judgment-the-final', 'term': 'Judgment, The final', 'category': 'events',
    'intro': '<p>The final judgment is the climactic eschatological event in biblical theology in which God calls all humanity to account before his tribunal at the end of history. In both testaments the Day of the Lord is presented as a day of reckoning when the deeds of every person are weighed and the destinies of the righteous and the wicked are determined. Jesus\'s discourse in Matthew 25 portrays the Son of Man as judge separating the nations as a shepherd separates sheep from goats, with the criterion being how the nations treated "the least of these my brothers."</p><p>Paul writes that all must appear before the judgment seat of Christ, that God will judge the secrets of men through Jesus Christ, and that judgment will begin with the household of God. The book of Revelation depicts the great white throne judgment before which the dead are raised and judged according to their works recorded in the books.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Matthew 25:31', 'Romans 14:10', '2 Corinthians 5:10', '2 Thessalonians 1:7']
  },
  'judgments-of-god': {
    'id': 'judgments-of-god', 'term': 'Judgments of God', 'category': 'concepts',
    'intro': '<p>The judgments of God in Scripture refer both to his acts of justice executed in history — punishments and calamities visited upon individuals, nations, or Israel for sin — and to his statutes and ordinances given to Israel as the law of the covenant. The psalms celebrate both dimensions: the righteous rules and decrees that Israel was privileged to receive, and the terrifying acts by which God vindicated the righteous and punished the wicked. The plagues of Egypt, the destruction of Sodom, and the Babylonian exile are among the most prominent examples of God\'s historical judgments against sin.</p><p>Paul argues in Romans that God\'s judgments are unsearchable and his ways inscrutable, even as he demonstrates in the same letter that all humanity is under divine judgment and stands in need of the righteousness that comes through faith in Christ.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Psalms 36:6', 'Exodus 21:1', 'Psalms 119:7', 'Romans 11:33']
  },
  'judith': {
    'id': 'judith', 'term': 'Judith', 'category': 'people',
    'intro': '<p>Judith (meaning: <em>the praise of the Lord</em>, a feminine form of Judah) was a daughter of Beeri the Hittite and wife of Esau, listed among his Canaanite wives in Genesis 26:34. Her marriage to Esau is noted as a source of grief to Isaac and Rebekah, illustrating the contrast between Esau\'s disregard for the patriarchal covenant community and Jacob\'s eventual marriage within the extended family. She is not to be confused with the heroic widow Judith of the deuterocanonical book, which is not considered canonical in Protestant tradition.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Judah', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Genesis 26:34']
  },
  'julia': {
    'id': 'julia', 'term': 'Julia', 'category': 'people',
    'intro': '<p>Julia (meaning: <em>downy; soft and tender hair</em>) was a Christian woman in Rome greeted by Paul at the close of his letter to the Romans, mentioned alongside Philologus. She may have been the wife or sister of Philologus. The name Julia was extremely common in the Roman world, being associated with the imperial Julian clan, and its presence in a list of Roman Christians reflects the cosmopolitan character of the early church at Rome, which included people of both slave and free status.</p>',
    'sections': [], 'hitchcock_meaning': 'downy; soft and tender hair', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Romans 16:15']
  },
  'julius': {
    'id': 'julius', 'term': 'Julius', 'category': 'people',
    'intro': '<p>Julius (meaning: <em>same as Julia</em>) was a Roman centurion of the Augustan cohort assigned to escort Paul from Caesarea to Rome for his imperial trial. The account in Acts 27 portrays Julius favorably, treating Paul with courtesy and allowing him to visit friends at Sidon. When the ship was wrecked at Malta, Julius intervened to prevent the soldiers from killing the prisoners, sparing Paul\'s life. His sympathetic handling of the apostle throughout the voyage reflects a broader Lukan interest in showing that Roman officials often recognized Paul\'s innocence.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Julia', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Acts 27:1', 'Acts 27:3', 'Acts 27:43']
  },
  'junia': {
    'id': 'junia', 'term': 'Junia', 'category': 'people',
    'intro': '<p>Junia (meaning: <em>youth</em>) is a woman, or possibly a man named Junias, greeted by Paul in Romans 16:7 alongside Andronicus as a fellow Jew, a kinsman, and a fellow prisoner who was "well known among the apostles." The phrase "among the apostles" may mean that Andronicus and Junia were notable within the apostolic circle, or that the apostles held them in high regard. If Junia is a woman, the reference has been significant in discussions of women\'s roles in the earliest church, as the name was commonplace in the Roman world and exclusively feminine in attested usage.</p>',
    'sections': [], 'hitchcock_meaning': 'youth', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Romans 16:7']
  },
  'juniper': {
    'id': 'juniper', 'term': 'Juniper', 'category': 'concepts',
    'intro': '<p>The juniper of the Authorized Version most likely refers to the <em>Retama raetam</em>, the white broom plant of the desert regions of Palestine and Sinai, rather than the true juniper tree. This desert shrub, which can grow six to twelve feet high, provides some shade and was used as fuel. Elijah sat under a juniper in the wilderness of Beersheba when, exhausted and despairing, he prayed to die, and the angel of the Lord twice awoke him with food and water for the journey ahead. The roots of the retam also served as fuel, mentioned in Job, and its charcoal produced arrows in Psalm 120.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['1 Kings 19:4', '1 Kings 19:5', 'Psalms 120:4', 'Job 30:4']
  },
  'jupiter': {
    'id': 'jupiter', 'term': 'Jupiter', 'category': 'concepts',
    'intro': '<p>Jupiter (meaning: <em>the father that helpeth</em>) was the chief deity of the Roman pantheon, king of the gods and ruler of the heavens, identified by the Greeks with Zeus. He appears in two New Testament contexts. At Lystra, when Paul healed a lame man, the crowd identified Paul and Barnabas as Hermes and Zeus (Jupiter) descended from heaven, and the priest of Zeus brought oxen and garlands to offer sacrifice, an act the apostles vigorously refused. In Acts 19, the image of Artemis at Ephesus is said to have "fallen from Zeus" (Jupiter), indicating a sky-stone or meteorite enshrined as the goddess\'s cult image.</p>',
    'sections': [], 'hitchcock_meaning': 'the father that helpeth', 'source_ids': ['easton', 'smith', 'isbe'],
    'key_refs': ['Acts 14:12', 'Acts 14:13', 'Acts 19:35']
  },
  'justice': {
    'id': 'justice', 'term': 'Justice', 'category': 'concepts',
    'intro': '<p>Justice in biblical theology refers to God\'s essential attribute of moral rectitude and his active governance of the world in accordance with righteousness. The Hebrew concepts of <em>mishpat</em> (judgment, right decision) and <em>tsedaqah</em> (righteousness, conformity to a standard) together constitute the biblical understanding of justice, and both are used of God as the foundation of his throne. Divine justice expresses itself in the condemnation of sin, the vindication of the righteous, the protection of the poor and powerless, and ultimately in the cross, where God\'s justice and mercy meet in the atoning death of Christ.</p><p>The prophets consistently called Israel\'s rulers and people to embody justice in their social and legal practice, and the New Testament insists that justification — being declared righteous before God — is itself an act of divine justice accomplished through the faithfulness of Jesus Christ.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'isbe'],
    'key_refs': ['Psalms 89:14', 'Amos 5:24', 'Romans 3:26', 'Isaiah 61:8']
  },
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP j3: Jezreel, Portion of → Justice: wrote {written}, skipped {skipped} existing.")

main()
