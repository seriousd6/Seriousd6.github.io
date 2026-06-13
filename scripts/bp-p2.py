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
  'perazim-mount': {
    'id': 'perazim-mount', 'term': 'Perazim, Mount', 'category': 'places',
    'intro': '<p>Mount Perazim was the site where David defeated the Philistines in battle, and David named it Baal-perazim ("Lord of the breakthroughs") because God broke through his enemies "like a breaking forth of waters." Isaiah later invokes the same name in his prophecy of judgment: "the Lord will rise up as at Mount Perazim... to do his deed, strange is his deed!" — applying the imagery of sudden divine intervention against Israel\'s own complacency and the Assyrian threat. The location is not precisely identified but was near the Valley of Rephaim southwest of Jerusalem.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['2 Samuel 5:20', 'Isaiah 28:21', '1 Chronicles 14:11']
  },
  'peres': {
    'id': 'peres', 'term': 'Peres', 'category': 'concepts',
    'intro': '<p>Peres is the singular form of the Aramaic word <em>parsin</em> meaning "divided" or "broken," appearing in Daniel 5:28 as part of the mysterious handwriting on the wall at Belshazzar\'s feast: MENE, MENE, TEKEL, PERES (UPHARSIN). Daniel interpreted it as "Your kingdom is divided and given to the Medes and Persians" — a wordplay on the Aramaic root meaning both "divided" and the name "Persia." The prophecy was fulfilled that very night when Belshazzar was slain and Darius the Mede received the kingdom.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Daniel 5:28', 'Daniel 5:25']
  },
  'perez': {
    'id': 'perez', 'term': 'Perez', 'category': 'people',
    'intro': '<p>Perez (meaning: <em>divided; rupture</em>) was the son of Judah and Tamar, born at the same time as his twin brother Zerah in an unusual birth in which Zerah\'s hand appeared first but Perez broke through first, causing the midwife to say "What a breach you have made for yourself!" The breach-name stuck. Perez became the more prominent line: his descendants the Perezites were the largest clan in Judah, David descended from him through Hezron and Ram, and Matthew\'s genealogy of Jesus runs through Perez. Ruth 4:18 opens the genealogy connecting Perez to David.</p>',
    'sections': [], 'hitchcock_meaning': 'divided; rupture', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 38:29', 'Ruth 4:18', 'Matthew 1:3', '1 Chronicles 27:3']
  },
  'perez-uzzah': {
    'id': 'perez-uzzah', 'term': 'Perez-uzzah', 'category': 'places',
    'intro': '<p>Perez-uzzah ("breach of Uzzah") was the name David gave to the threshing floor of Nacon (or Chidon) where Uzzah died after reaching out to steady the ark of God when the oxen stumbled. God\'s anger burned against Uzzah, and he died there beside the ark. David, frightened and angry at the breach the Lord had made against Uzzah, halted the procession and the ark remained with Obed-edom for three months before David brought it successfully to Jerusalem. The site became a memorial of the holiness of God and the danger of handling sacred things without reverence.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['2 Samuel 6:6', '2 Samuel 6:8', '1 Chronicles 13:11']
  },
  'perfection': {
    'id': 'perfection', 'term': 'Perfection', 'category': 'concepts',
    'intro': '<p>Perfection in Scripture carries a range of meanings related to completion, wholeness, and moral maturity rather than sinless absolute perfection. The Hebrew <em>tamim</em> (blameless, whole) and Greek <em>teleios</em> (complete, mature, fully developed) both emphasize completeness of purpose and character. God commands Abraham to "walk before me and be blameless" and Jesus commands his hearers to "be perfect, as your heavenly Father is perfect." Paul distinguishes between the already-perfect position of believers in Christ and the ongoing maturation of practical holiness toward which they press. The Hebrews epistle presents Christ as the one who has been made perfect through suffering and who perfectly accomplishes what the Levitical system could not.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Matthew 5:48', 'Genesis 17:1', 'Hebrews 7:19', 'Philippians 3:12']
  },
  'perfumes': {
    'id': 'perfumes', 'term': 'Perfumes', 'category': 'concepts',
    'intro': '<p>Perfumes and aromatic substances were central to ancient Israelite worship and daily life. The holy incense burned before the Lord in the tabernacle was a carefully prescribed compound of stacte, onycha, galbanum, and frankincense, forbidden for private use. Spices and perfumes also played roles in anointing oil, burial preparation, and bridal adornment. The Song of Solomon celebrates perfume as part of the beloved\'s allure. In the New Testament, Mary of Bethany\'s anointing of Jesus with costly nard and Nicodemus\'s mixture of myrrh and aloes for burial represent the highest expressions of devotion through aromatic substances.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Exodus 30:35', 'Song of Solomon 3:6', 'John 12:3', 'John 19:39']
  },
  'perga': {
    'id': 'perga', 'term': 'Perga', 'category': 'places',
    'intro': '<p>Perga (meaning: <em>very earthy</em>) was the capital city of Pamphylia on the southern coast of Asia Minor, located a few miles inland from the Mediterranean near the Cestrus River. Paul and Barnabas passed through Perga twice during the first missionary journey — first on their way inland to Pisidian Antioch, and again on the return trip when Paul preached there. John Mark left the party at Perga on the outward journey, a departure that caused the later disagreement between Paul and Barnabas. Perga was a significant city with a famous temple of Artemis and a well-preserved Hellenistic-Roman urban layout still visible archaeologically.</p>',
    'sections': [], 'hitchcock_meaning': 'very earthy', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Acts 13:13', 'Acts 13:14', 'Acts 14:25']
  },
  'pergamos': {
    'id': 'pergamos', 'term': 'Pergamos', 'category': 'places',
    'intro': '<p>Pergamos (or Pergamum, meaning: <em>height; elevation</em>) was a major city in the Roman province of Asia in western Asia Minor (modern Bergama, Turkey), the capital of the Attalid kingdom before becoming a leading Roman provincial center. It possessed the second largest library in the ancient world (second only to Alexandria), a famous altar of Zeus, temples to Rome and Augustus, and the shrine of Asclepius the healing god. The letter to Pergamos in Revelation 2:12–17 commends the church for holding fast to Christ\'s name even "where Satan\'s throne is" — a reference perhaps to the imperial cult or the great altar of Zeus — while rebuking those who hold the teaching of Balaam and the Nicolaitans.</p>',
    'sections': [], 'hitchcock_meaning': 'height; elevation', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Revelation 1:11', 'Revelation 2:12', 'Revelation 2:17']
  },
  'perida': {
    'id': 'perida', 'term': 'Perida', 'category': 'people',
    'intro': '<p>Perida (meaning: <em>separation; division</em>) was the ancestor of a family of Solomon\'s servants who returned from Babylon with Zerubbabel after the exile, listed in Nehemiah 7:57. The parallel list in Ezra 2:55 calls the ancestor Peruda, indicating these are variant spellings of the same name. The "servants of Solomon" appear to have been a class of temple workers, possibly of non-Israelite origin, who performed manual labor in service of the sanctuary alongside the Levites and Nethinim.</p>',
    'sections': [], 'hitchcock_meaning': 'separation; division', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Nehemiah 7:57', 'Ezra 2:55']
  },
  'perizzites': {
    'id': 'perizzites', 'term': 'Perizzites', 'category': 'people',
    'intro': '<p>The Perizzites (meaning: <em>dwelling in villages</em>) were one of the pre-Israelite peoples of Canaan, listed alongside the Canaanites, Hittites, Amorites, Hivites, and Jebusites in the divine promise of the land to Abraham. They appear frequently in the conquest lists as one of the peoples Israel was commanded to drive out, and they were known to dwell in the hill country and forested regions alongside the Rephaim. Like other Canaanite peoples, the Perizzites were not fully exterminated, and their continued presence contributed to the religious syncretism that plagued Israel through the period of the judges and monarchy.</p>',
    'sections': [], 'hitchcock_meaning': 'dwelling in villages', 'source_ids': ['easton'],
    'key_refs': ['Genesis 15:20', 'Exodus 3:8', 'Joshua 17:15']
  },
  'persecution': {
    'id': 'persecution', 'term': 'Persecution', 'category': 'concepts',
    'intro': '<p>Persecution — the active hostile opposition of authorities or communities toward believers because of their faith — is a consistent theme in both Testaments. The prophets were persecuted by kings and priests; Jesus was killed by the Jewish and Roman authorities; and the early church experienced systematic opposition from both Jewish leadership and the Roman imperial system. Jesus explicitly promised his disciples that they would face persecution and called those who endure it blessed, promising the kingdom of heaven as their reward.</p><p>Paul catalogues his own sufferings as evidence of authentic apostolic ministry and teaches that "all who desire to live a godly life in Christ Jesus will be persecuted." The New Testament authors consistently frame persecution as participation in Christ\'s own suffering and a mark of genuine discipleship rather than evidence of divine disfavor.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Matthew 5:10', '2 Timothy 3:12', 'Acts 8:1', 'Romans 8:35']
  },
  'perseverance-of-the-saints': {
    'id': 'perseverance-of-the-saints', 'term': 'Perseverance of the Saints', 'category': 'concepts',
    'intro': '<p>The perseverance of the saints is the theological doctrine that those whom God has genuinely regenerated and justified will continue in faith and ultimately reach eternal salvation — not because of their own strength but because of God\'s preserving grace. It is grounded in texts such as John 10:28–29 (no one shall snatch them from my hand), Romans 8:29–30 (those foreknown are glorified), and Philippians 1:6 (he who began a good work will complete it). The doctrine does not deny the reality of apostasy or backsliding but holds that true saving faith will, through the Spirit\'s work, ultimately endure.</p><p>Sometimes termed "eternal security" or "once saved, always saved," the doctrine is affirmed in Reformed and many Baptist traditions while disputed by Arminian and Wesleyan theologies that emphasize the possibility of final apostasy.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['John 10:28', 'Romans 11:29', 'Philippians 1:6', 'John 6:39']
  },
  'persia': {
    'id': 'persia', 'term': 'Persia', 'category': 'places',
    'intro': '<p>Persia was the great empire that succeeded Babylon as the dominant power of the ancient Near East, founded by Cyrus the Great in 550 B.C. through the unification of the Medes and Persians. At its height under Darius I and Xerxes I it stretched from the Aegean Sea to the Indus River. Persia\'s role in biblical history is primarily the context of the post-exilic books: Cyrus issued the decree in 538 B.C. that allowed Jewish exiles to return to Judah and rebuild the temple — a decree that Isaiah had prophesied by name over a century earlier. The books of Ezra, Nehemiah, Esther, Daniel, Haggai, and Zechariah are all set partly or entirely in the Persian period.</p>',
    'sections': [], 'hitchcock_meaning': 'that cuts or divides; a nail; a gryphon; a horseman', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Ezra 1:1', 'Ezra 1:2', 'Daniel 6:28', 'Isaiah 44:28']
  },
  'persis': {
    'id': 'persis', 'term': 'Persis', 'category': 'people',
    'intro': '<p>Persis (meaning: <em>same as Persia — a Persian woman</em>) was a woman in the Roman church greeted by Paul at the close of Romans 16:12 as "the beloved Persis, who has worked hard in the Lord." She is distinguished from Tryphena and Tryphosa (whom Paul exhorts to work hard) by the past tense applied to her labors, which some interpreters take as indicating her advanced age. Her name, meaning Persian woman, suggests she or her ancestors came from the eastern parts of the empire, reflecting the diverse ethnic composition of the early Roman church.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Persia', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Romans 16:12']
  },
  'peruda': {
    'id': 'peruda', 'term': 'Peruda', 'category': 'people',
    'intro': '<p>Peruda (meaning: <em>same as Perida — separation; division</em>) was the ancestor of a family of Solomon\'s servants who returned from Babylon with Zerubbabel after the exile, listed in Ezra 2:55. The parallel list in Nehemiah 7:57 calls the ancestor Perida, indicating these are variant spellings of the same name. The designation "servants of Solomon" likely refers to temple workers of non-Israelite origin assigned to auxiliary service in the sanctuary, a class established by Solomon alongside the Nethinim.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Perida', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Ezra 2:55', 'Nehemiah 7:57']
  },
  'peter': {
    'id': 'peter', 'term': 'Peter', 'category': 'people',
    'intro': '<p>Peter (meaning: <em>a rock or stone</em>) — also known as Simon son of Jonah, or Cephas (the Aramaic equivalent of Peter) — was a fisherman from Bethsaida who, with his brother Andrew, became one of the first disciples called by Jesus. He was the spokesman for the Twelve, the first to confess Jesus as "the Christ, the Son of the living God," and the first apostle to see the risen Lord. His three denials of Jesus on the night of the arrest were followed by a restoration by the Sea of Galilee in which Jesus three times commissioned him to feed and tend his sheep.</p><p>On the day of Pentecost Peter preached the first apostolic sermon and led the Jerusalem church in its earliest years. He later played a pivotal role at the Council of Jerusalem, and his ministry to Jewish communities extended to Corinth and eventually Rome, where tradition places his martyrdom under Nero.</p>',
    'sections': [], 'hitchcock_meaning': 'a rock or stone', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Matthew 16:17', 'John 1:42', 'Acts 2:14', 'Galatians 2:7']
  },
  'peter-first-epistle-of': {
    'id': 'peter-first-epistle-of', 'term': 'Peter, First Epistle of', 'category': 'concepts',
    'intro': '<p>The First Epistle of Peter is a letter from the apostle Peter to "elect exiles scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia" — Gentile and Jewish Christians in Asia Minor facing social marginalization and the threat of persecution. Its central themes are the believers\' identity as a chosen people and holy nation, the suffering of Christ as both example and ground of salvation, the importance of honorable conduct before unbelievers, and eschatological hope in the inheritance kept in heaven. Peter grounds ethical exhortation consistently in the redemptive work of Christ and the revelation of the last times.</p><p>Written perhaps from Rome ("Babylon") around the time of Nero\'s persecution in the mid-60s A.D., 1 Peter is among the most practically theological letters in the New Testament, uniting doctrine and life around the suffering and glory of Jesus.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Peter 1:1', '1 Peter 1:3', '1 Peter 2:9', '1 Peter 4:12']
  },
  'peter-second-epistle-of': {
    'id': 'peter-second-epistle-of', 'term': 'Peter, Second Epistle of', 'category': 'concepts',
    'intro': '<p>The Second Epistle of Peter is a farewell letter from the apostle, written in anticipation of his death, warning against the same false teachers addressed in Jude — libertines who deny the Lord and mock the promise of his return. The letter opens with the apostolic eyewitness testimony of the transfiguration as the foundation for the reliability of prophetic Scripture, which Peter grounds in the divine rather than human will as its source. Its most distinctive section is the apocalyptic passage of chapter 3, which declares that the Lord is not slow about his promise but patient, and that the present heavens and earth are stored for fire.</p><p>The letter\'s authorship is the most debated of any New Testament book, with many scholars attributing it to a Petrine school rather than Peter directly; the church\'s eventual acceptance of it as canonical reflects a judgment about its apostolic content.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['2 Peter 1:1', '2 Peter 1:16', '2 Peter 3:9', '2 Peter 1:21']
  },
  'pethahiah': {
    'id': 'pethahiah', 'term': 'Pethahiah', 'category': 'people',
    'intro': '<p>Pethahiah (meaning: <em>the Lord opening; gate of the Lord</em>) is the name of three men in the post-exilic period. The first was the head of the nineteenth priestly course in David\'s temple organization. The second was a Levite who confessed mixed marriages during Ezra\'s reform and stood on the stairs during the great public confession of Nehemiah 9. The third was a Judahite appointed as the king\'s agent in matters concerning the people, stationed at the Persian court — a liaison between the Jewish community and the imperial administration.</p>',
    'sections': [], 'hitchcock_meaning': 'the Lord opening; gate of the Lord', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 24:16', 'Nehemiah 9:5', 'Nehemiah 11:24']
  },
  'pethor': {
    'id': 'pethor', 'term': 'Pethor', 'category': 'places',
    'intro': '<p>Pethor was the hometown of Balaam son of Beor, described in Numbers 22:5 as "which is near the River" — a reference to the Euphrates — and in Deuteronomy 23:4 as in Mesopotamia. Ancient Assyrian records mention a city Pitru on the western bank of the Euphrates near Carchemish in northern Syria, which most scholars identify with biblical Pethor. Balak of Moab sent messengers from Moab to Pethor to summon Balaam to curse Israel — a journey of several hundred miles reflecting Balaam\'s reputation as a powerful diviner of international standing.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Numbers 22:5', 'Deuteronomy 23:4']
  },
  'pethuel': {
    'id': 'pethuel', 'term': 'Pethuel', 'category': 'people',
    'intro': '<p>Pethuel (meaning: <em>mouth of God; persuasion of God</em>) was the father of the prophet Joel. He is mentioned only in Joel 1:1 in the superscription "The word of the Lord that came to Joel, the son of Pethuel." Nothing further is known about him, and his name appears nowhere else in Scripture. The identification of Joel\'s father by name follows the convention of prophetic books that name the prophet\'s father as a form of identifying the prophet\'s lineage and potentially his prophetic authority.</p>',
    'sections': [], 'hitchcock_meaning': 'mouth of God; persuasion of God', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joel 1:1']
  },
  'petra': {
    'id': 'petra', 'term': 'Petra', 'category': 'places',
    'intro': '<p>Petra ("rock" in Greek) was the remarkable cliff city of the Nabataean Arabs carved into the red sandstone mountains of Edom, southeast of the Dead Sea. It is identified with the biblical Sela ("rock" in Hebrew), the ancient capital of Edom, captured by Amaziah king of Judah who renamed it Joktheel. Isaiah 16:1 refers to Sela in the context of Moabite refugees seeking safety. The Nabataean kingdom centered at Petra flourished from approximately the 4th century B.C. through its Roman incorporation in A.D. 106, and the city\'s treasury, monasteries, and temples carved directly from rose-red rock make it one of the most spectacular archaeological sites in the world.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Isaiah 16:1', '2 Kings 14:7', '2 Chronicles 25:12']
  },
  'peulthai': {
    'id': 'peulthai', 'term': 'Peulthai', 'category': 'people',
    'intro': '<p>Peulthai (meaning: <em>my works</em>) was the eighth son of Obed-edom, a Levite gatekeeper appointed by David to serve at the ark and later at the tabernacle and temple. The family of Obed-edom was renowned for its blessing — the ark had brought prosperity to his household during its three months there — and his sons were similarly blessed with great ability. Peulthai is listed among the sixty-two descendants of Obed-edom who served as gatekeepers and temple officials.</p>',
    'sections': [], 'hitchcock_meaning': 'my works', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Chronicles 26:5']
  },
  'phalec': {
    'id': 'phalec', 'term': 'Phalec', 'category': 'people',
    'intro': '<p>Phalec is the Greek form of Peleg, appearing in Luke 3:35 in the genealogy of Jesus. Peleg was the son of Eber and great-grandson of Shem, "for in his days the earth was divided" — a cryptic reference in Genesis 10:25 that has been interpreted as referring to the division of languages at Babel, the geological separation of continents, or the division of peoples into their national territories. His name literally means "division" or "canal," and he is the ancestor of Abraham through the Shemite line.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Peleg', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Luke 3:35', 'Genesis 10:25', 'Genesis 11:16']
  },
  'phallu': {
    'id': 'phallu', 'term': 'Phallu', 'category': 'people',
    'intro': '<p>Phallu (also Pallu, meaning: <em>admirable; hidden</em>) was the second son of Reuben, Jacob\'s firstborn, and the ancestor of the Palluite family of the tribe of Reuben. He is listed among the seventy persons of Jacob\'s household who came to Egypt (Genesis 46:9) and in the Reubenite clan census of Numbers 26:5. His son Eliab was the father of Dathan and Abiram, who participated in Korah\'s rebellion against Moses and Aaron and were swallowed by the earth as divine judgment.</p>',
    'sections': [], 'hitchcock_meaning': 'admirable; hidden', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 46:9', 'Numbers 26:5', 'Numbers 26:8']
  },
  'phalti': {
    'id': 'phalti', 'term': 'Phalti', 'category': 'people',
    'intro': '<p>Phalti (also Phaltiel or Paltiel, meaning: <em>deliverance; flight</em>) was the son of Laish from Gallim to whom Saul gave Michal, David\'s wife, after David had fled from Saul. When David later reclaimed Michal as part of his political reconciliation with the house of Saul, Phalti followed her weeping as she was taken away, until Abner commanded him to turn back. This brief but poignant detail reveals a man who had formed a genuine emotional bond with Michal during their years together.</p>',
    'sections': [], 'hitchcock_meaning': 'deliverance; flight', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Samuel 25:44', '2 Samuel 3:15', '2 Samuel 3:16']
  },
  'phanuel': {
    'id': 'phanuel', 'term': 'Phanuel', 'category': 'people',
    'intro': '<p>Phanuel (meaning: <em>face or vision of God</em>) was the father of the prophetess Anna who encountered the infant Jesus in the temple at the presentation. He is of the tribe of Asher — one of the northern tribes that had largely disappeared after the Assyrian conquest — and his mention is one of the few clear New Testament references to someone from one of the "lost tribes" maintaining an identity in Jewish life. Anna, his widowed daughter of great age, gave thanks to God and spoke of the child Jesus to all who were waiting for the redemption of Jerusalem.</p>',
    'sections': [], 'hitchcock_meaning': 'face or vision of God', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Luke 2:36']
  },
  'pharaoh': {
    'id': 'pharaoh', 'term': 'Pharaoh', 'category': 'people',
    'intro': '<p>Pharaoh (meaning: <em>that disperses; that spoils</em>) is the title given to the kings of ancient Egypt, derived from the Egyptian <em>per-aa</em> meaning "great house" — the royal palace itself, used by extension for its occupant. Several pharaohs appear in Scripture without their personal names: the pharaoh of Abraham\'s time who took Sarah; the pharaoh of Joseph\'s time who elevated him to second in command; the pharaoh of the Exodus who hardened his heart against Moses through ten plagues until the death of his firstborn broke his resistance; and several later pharaohs who engaged with Israel\'s kings in alliance or conflict.</p><p>The Exodus pharaoh is the most theologically significant, presented as the embodiment of human resistance to divine sovereignty whose hardening serves to display God\'s power and glory to the nations.</p>',
    'sections': [], 'hitchcock_meaning': 'that disperses; that spoils', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 12:15', 'Genesis 41:1', 'Exodus 5:2', 'Romans 9:17']
  },
  'pharaohs-daughters': {
    'id': 'pharaohs-daughters', 'term': "Pharaoh's Daughters", 'category': 'people',
    'intro': '<p>Three daughters of Pharaoh are mentioned in Scripture. The most prominent is the daughter of Pharaoh who rescued the infant Moses from the Nile, named him, and raised him in the Egyptian court — an act of compassion that the New Testament treats as the providential means of Moses\'s education for his future mission. Moses\'s choice to identify with Israel rather than remain as "son of Pharaoh\'s daughter" is held up in Hebrews 11:24 as an act of faith. Solomon also married a daughter of Pharaoh as part of his political alliances, housing her in a specially built palace in Jerusalem. A third Pharaoh\'s daughter, Bithiah (or Bithia), is mentioned in 1 Chronicles 4:18 as wife of the Judahite Mered.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Exodus 2:10', 'Hebrews 11:24', '1 Kings 3:1', '1 Chronicles 4:18']
  },
  'pharez': {
    'id': 'pharez', 'term': 'Pharez', 'category': 'people',
    'intro': '<p>Pharez (the older English form of Perez, meaning: <em>division; rupture</em>) was the son of Judah and Tamar, born in unusual circumstances when Tamar disguised herself as a prostitute after her rights under the levirate law were denied. His twin Zerah put out his hand first but Pharez broke through, giving him the birth-name "breach." Pharez became the ancestor of the royal Judahite line through Hezron, Ram, Amminadab, Nahshon, and Salmon — the lineage that runs through Boaz, Obed, Jesse, and David to Jesus in Matthew\'s genealogy.</p>',
    'sections': [], 'hitchcock_meaning': 'division; rupture', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 38:29', 'Ruth 4:18', 'Matthew 1:3']
  },
  'pharisees': {
    'id': 'pharisees', 'term': 'Pharisees', 'category': 'people',
    'intro': '<p>The Pharisees (meaning: <em>set apart</em>) were a major religious movement in Second Temple Judaism, originating in the Maccabean period as a lay movement devoted to rigorous observance of the Mosaic law and its oral tradition. They believed in the resurrection of the dead, angels, and the spirits — in contrast to the Sadducees — and sought to extend priestly purity codes to all of daily life. In the Gospels the Pharisees are the most frequent opponents of Jesus, confronting him over sabbath observance, ritual purity, fasting, and his association with sinners.</p><p>Jesus\'s Sermon on the Mount and his "woes" in Matthew 23 represent extended engagements with Pharisaic teaching. Despite the conflict, some Pharisees showed sympathy toward Jesus (Nicodemus, Joseph of Arimathea), and Paul proudly identified himself as a Pharisee. The Pharisees were the forebears of rabbinic Judaism after the temple\'s destruction in A.D. 70.</p>',
    'sections': [], 'hitchcock_meaning': 'set apart', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Matthew 23:15', 'Acts 26:5', 'Philippians 3:5', 'John 7:48']
  },
  'pharpar': {
    'id': 'pharpar', 'term': 'Pharpar', 'category': 'places',
    'intro': '<p>Pharpar (meaning: <em>that produces fruit</em>) was one of the two rivers of Damascus — along with Abana — which Naaman the Syrian army commander preferred over the Jordan River when Elisha told him to dip seven times in the Jordan to be cleansed of his leprosy. "Are not Abana and Pharpar, the rivers of Damascus, better than all the waters of Israel?" he protested. The Pharpar is generally identified with the Nahr el-Awaj, a river flowing from the slopes of Hermon south of Damascus into the eastern desert, supplying the southern part of the Damascus plain.</p>',
    'sections': [], 'hitchcock_meaning': 'that produces fruit', 'source_ids': ['easton', 'smith'],
    'key_refs': ['2 Kings 5:12']
  },
  'phebe': {
    'id': 'phebe', 'term': 'Phebe', 'category': 'people',
    'intro': '<p>Phebe (also Phoebe, meaning: <em>shining; pure</em>) was a woman of the church at Cenchreae (the eastern port of Corinth) who is described by Paul in Romans 16:1–2 as a deaconess (or servant) of the church and a patroness of many, including Paul himself. She was likely the carrier of Paul\'s letter to the Romans, which would have made her its first public reader to the Roman congregation. Her designation as <em>diakonos</em> (the same word used for male deacons) and as <em>prostatis</em> (patron, benefactor) indicates a woman of some social standing who exercised recognized ministry and financial support of the church.</p>',
    'sections': [], 'hitchcock_meaning': 'shining; pure', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Romans 16:1', 'Romans 16:2']
  },
  'phenice': {
    'id': 'phenice', 'term': 'Phenice', 'category': 'places',
    'intro': '<p>Phenice (or Phoenix) was a harbor on the southern coast of Crete facing southwest and northwest, mentioned in Acts 27:12 as the port where the crew of Paul\'s ship hoped to winter rather than at the inadequate harbor of Fair Havens. The majority decision to sail for Phenice against Paul\'s advice led directly to the catastrophic storm and eventual shipwreck at Malta. The harbor is generally identified with the modern Loutro on the southwestern Cretan coast, whose sheltered bay fits the description of facing "toward the southwest and northwest." The same word (Phoenicia) is used elsewhere for the coastal region of Syria and Lebanon.</p>',
    'sections': [], 'hitchcock_meaning': 'red; purple', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Acts 27:12']
  },
  'phenicia': {
    'id': 'phenicia', 'term': 'Phenicia', 'category': 'places',
    'intro': '<p>Phoenicia (or Phenicia, meaning: <em>red; purple</em>) was the coastal strip of Syria and Lebanon north of Mount Carmel, home to the great Semitic maritime cities of Tyre, Sidon, and Byblos. The Phoenicians were master shipbuilders, traders, and craftsmen whose purple dye and cedar exports gave them wealth and influence throughout the ancient Mediterranean world. Solomon allied with Hiram of Tyre to obtain cedar for the temple and skilled craftsmen including Hiram the bronzeworker. In the New Testament Jesus traveled into the region of Tyre and Sidon and healed the Syrophoenician woman\'s daughter, and the early church established a congregation in Phoenicia during the dispersal after Stephen\'s death.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Acts 21:2', 'Acts 11:19', 'Mark 7:26', '1 Kings 5:1']
  },
  'phicol': {
    'id': 'phicol', 'term': 'Phicol', 'category': 'people',
    'intro': '<p>Phicol was the commander of the army of Abimelech, king of the Philistines at Gerar. He appears twice in the patriarchal narratives: first accompanying Abimelech when the king made a covenant with Abraham at Beersheba following the dispute over the well, and again when a later Abimelech (or the same king at a later time) made a similar covenant with Isaac at the same location. His presence at both covenantal negotiations suggests he was a senior military officer whose witness guaranteed the treaty\'s binding force.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Genesis 21:22', 'Genesis 26:26']
  },
  'philadelphia': {
    'id': 'philadelphia', 'term': 'Philadelphia', 'category': 'places',
    'intro': '<p>Philadelphia (meaning: <em>love of a brother</em>) was a city in the Roman province of Asia in western Asia Minor (modern Alasehir, Turkey), founded by the Attalid king Attalus II Philadelphus and named for his fraternal loyalty. Situated near significant fault lines, it suffered devastating earthquakes, including the great earthquake of A.D. 17. The letter to Philadelphia in Revelation 3:7–13 is one of the two letters (along with Smyrna) that contain only commendation and no rebuke — promising the church that Christ has set before it an open door that no one can shut and will keep it from the hour of trial coming upon the whole world.</p>',
    'sections': [], 'hitchcock_meaning': 'love of a brother', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Revelation 3:7', 'Revelation 3:8', 'Revelation 1:11']
  },
  'philemon': {
    'id': 'philemon', 'term': 'Philemon', 'category': 'people',
    'intro': '<p>Philemon (meaning: <em>who kisses</em>) was a wealthy Christian at Colossae to whom Paul addressed the shortest of his canonical letters. He was a convert of Paul\'s (possibly from Paul\'s Ephesian ministry), a host of the church that met in his house, and a slave owner whose runaway slave Onesimus had come to Paul in Rome, been converted, and was being sent back with the letter. Paul appeals to Philemon to receive Onesimus "no longer as a slave, but better than a slave, as a dear brother" — one of the New Testament\'s most significant statements about the transformation of social relationships within the household of faith.</p>',
    'sections': [], 'hitchcock_meaning': 'who kisses', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Philemon 1:1', 'Philemon 1:15', 'Philemon 1:16', 'Colossians 4:9']
  },
  'philemon-epistle-to': {
    'id': 'philemon-epistle-to', 'term': 'Philemon, Epistle to', 'category': 'concepts',
    'intro': '<p>The Epistle to Philemon is a brief personal letter from Paul to a Christian slaveholder in Colossae on behalf of his runaway slave Onesimus, who had become a Christian during Paul\'s Roman imprisonment. The letter is a masterpiece of tactful advocacy: Paul appeals to Philemon on the basis of their friendship and gospel partnership, declining to command but persuading from love, and hints strongly that he hopes Onesimus will be sent back to serve him in ministry. Paul\'s appeal to receive Onesimus as a brother rather than a slave, combined with his offer to pay any debt personally, has been seen as an implicit challenge to the institution of slavery operating through transformation of personal relationships rather than direct social legislation.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Philemon 1:1', 'Philemon 1:16', 'Philemon 1:18']
  },
  'philetus': {
    'id': 'philetus', 'term': 'Philetus', 'category': 'people',
    'intro': '<p>Philetus (meaning: <em>amiable; beloved</em>) was a false teacher in the Ephesian church, named alongside Hymenaeus in 2 Timothy 2:17–18 as one whose teaching had spread like gangrene. The specific error attributed to them was teaching that the resurrection had already occurred — a realized eschatology that denied the future bodily resurrection Paul taught. This teaching was "upsetting the faith of some." Hymenaeus is also condemned in 1 Timothy 1:20, where Paul says he handed him over to Satan to be taught not to blaspheme, suggesting he had previously been disciplined.</p>',
    'sections': [], 'hitchcock_meaning': 'amiable; beloved', 'source_ids': ['easton', 'smith'],
    'key_refs': ['2 Timothy 2:17', '2 Timothy 2:18']
  },
  'philip': {
    'id': 'philip', 'term': 'Philip', 'category': 'people',
    'intro': '<p>Philip (meaning: <em>warlike; a lover of horses</em>) is the name of several New Testament figures, most prominently two among the apostles and evangelists. Philip the Apostle was from Bethsaida, called by Jesus directly after Andrew and Peter, and is noted for his questions at the feeding of the five thousand and the Upper Room — "Lord, show us the Father and it is enough for us." Philip the Evangelist was one of the seven deacons chosen to serve widows in Jerusalem, who later evangelized Samaria with great effect, encountered the Ethiopian eunuch on the road to Gaza and baptized him, and hosted Paul on his journey to Jerusalem.</p><p>Herod Philip I (tetrarch of Ituraea) and Herod Philip II (brother of Herod Antipas and first husband of Herodias) are also named Philip in the Gospels.</p>',
    'sections': [], 'hitchcock_meaning': 'warlike; a lover of horses', 'source_ids': ['easton', 'smith'],
    'key_refs': ['John 1:44', 'Matthew 10:3', 'Acts 8:5', 'John 14:8']
  },
  'philippi': {
    'id': 'philippi', 'term': 'Philippi', 'category': 'places',
    'intro': '<p>Philippi (meaning: <em>city of Philip</em>) was a leading city of Macedonia in northeastern Greece, named after Philip II of Macedon who developed it for its gold mines, situated on a strategic plateau commanding the route between Asia and Europe. The city held significant Roman colonial status following its role in the battle (42 B.C.) in which Octavian and Antony defeated Brutus and Cassius. Paul established the first European Christian community at Philippi following his vision of the Macedonian man, and the church\'s founding members included Lydia of Thyatira, a slave girl delivered from a spirit of divination, and the jailer converted after an earthquake.</p><p>The Philippian church was among Paul\'s closest supporters, sending aid to him in prison and during his other missionary travels.</p>',
    'sections': [], 'hitchcock_meaning': 'same as Philip, in the plural', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Acts 16:12', 'Acts 16:9', '1 Thessalonians 2:2', 'Philippians 4:15']
  },
  'philippians-epistle-to': {
    'id': 'philippians-epistle-to', 'term': 'Philippians, Epistle to the', 'category': 'concepts',
    'intro': '<p>The Epistle to the Philippians is a letter of warm personal friendship from Paul to the church he founded at Philippi, written during one of his imprisonments (most likely Rome, though Ephesus and Caesarea are also proposed). Its pervading tone is joy — the word "rejoice" appears in various forms sixteen times — despite the prison context and the possibility of Paul\'s death. Its central theological passage is the famous Christ-hymn of Philippians 2:5–11, describing Christ\'s self-emptying, incarnation, and humiliation to death on a cross, followed by divine exaltation as the basis for Christian humility and unity.</p><p>The letter also contains Paul\'s autobiographical statement renouncing all legal righteousness for the righteousness that comes through faith in Christ, and the famous declaration "I can do all things through Christ who strengthens me."</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Philippians 1:7', 'Philippians 2:5', 'Philippians 4:4', 'Philippians 3:8']
  },
  'philistia': {
    'id': 'philistia', 'term': 'Philistia', 'category': 'places',
    'intro': '<p>Philistia was the coastal plain of southwestern Canaan occupied by the Philistines, stretching from Joppa southward to Gaza and bounded by the Mediterranean on the west and the Shephelah foothills on the east. Its five principal cities — Gaza, Ashdod, Ashkelon, Gath, and Ekron — each had its own ruler (seren). The psalmists use Philistia as a symbol of former enemies now subordinated to Israel\'s God: "Over Philistia I shout in triumph" (Psalms 60:8; 108:9). The plain\'s rich agricultural land and strategic coastal position made it a zone of perpetual contest between Israel and its neighbors from the judges period through the monarchy.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Psalms 60:8', 'Psalms 87:4', 'Genesis 21:32', 'Joel 3:4']
  },
  'philistines': {
    'id': 'philistines', 'term': 'Philistines', 'category': 'people',
    'intro': '<p>The Philistines were a seafaring people, probably of Aegean origin (the "Sea Peoples" of Egyptian records), who settled along the southwestern coast of Canaan around 1200 B.C. and established a confederation of five cities. They are connected in the Table of Nations to Casluhim, son of Mizraim son of Ham. The Philistines possessed iron technology and military organization that initially gave them a significant advantage over Israel, a dominance represented most dramatically by the narrative of Goliath and the broader Philistine oppression of Israel during Saul\'s reign.</p><p>David\'s victories broke Philistine power, though conflicts continued through the monarchy. The prophets condemned Philistia alongside other neighbors of Israel. By the New Testament era the Philistines had lost their distinct identity, their coastal region becoming part of Greco-Roman Palestine.</p>',
    'sections': [], 'hitchcock_meaning': 'those who dwell in villages', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 10:14', '1 Samuel 17:4', 'Amos 9:7', 'Judges 14:1']
  },
  'phinehas': {
    'id': 'phinehas', 'term': 'Phinehas', 'category': 'people',
    'intro': '<p>Phinehas (meaning: <em>bold aspect; face of trust or protection</em>) was the son of Eleazar and grandson of Aaron, whose act of zealous violence against Zimri and Cozbi during Israel\'s Baal-Peor apostasy turned away God\'s plague, resulting in the divine covenant of a perpetual priesthood for his line. Psalm 106:30 commemorates this act as "counted to him as righteousness for all generations." He later led the delegation that investigated the altar built by the eastern tribes and averted civil war by his discerning response.</p><p>A second Phinehas was the wicked son of the priest Eli who, with his brother Hophni, treated the offerings with contempt and slept with the women serving at the tabernacle. He was killed in battle on the day the ark was captured by the Philistines — the news causing Eli to fall and die and Phinehas\'s wife to name their son Ichabod ("the glory has departed").</p>',
    'sections': [], 'hitchcock_meaning': 'bold aspect; face of trust or protection', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Numbers 25:7', 'Psalms 106:30', 'Joshua 22:30', '1 Samuel 4:11']
  },
  'phlegon': {
    'id': 'phlegon', 'term': 'Phlegon', 'category': 'people',
    'intro': '<p>Phlegon (meaning: <em>zealous; burning</em>) was a Christian at Rome greeted by Paul in Romans 16:14 alongside Hermes, Patrobas, Hermas, and other unnamed brothers. Nothing further is recorded about him in Scripture. Like others in the closing greetings of Romans, Phlegon likely belonged to one of the household communities that made up the early Roman church. The name is of Greek origin and was commonly borne by freedmen and slaves in the Roman imperial period.</p>',
    'sections': [], 'hitchcock_meaning': 'zealous; burning', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Romans 16:14']
  },
  'phoenicia': {
    'id': 'phoenicia', 'term': 'Phoenicia', 'category': 'places',
    'intro': '<p>Phoenicia (see also Phenicia) was the ancient name for the coastal cities of modern Lebanon and northern Israel — principally Tyre, Sidon, and Byblos — inhabited by Semitic peoples who became the greatest maritime traders of the ancient world. Their alphabet, adopted and adapted by the Greeks, became the foundation of most Western writing systems. In the New Testament, Phoenicia is explicitly mentioned in Acts 21:2 as a region Paul passed through by sea, and Christians fleeing persecution after Stephen\'s death established communities there as far back as Acts 11:19.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Acts 21:2', 'Acts 11:19', 'Mark 7:31']
  },
  'phrygia': {
    'id': 'phrygia', 'term': 'Phrygia', 'category': 'places',
    'intro': '<p>Phrygia (meaning: <em>dry; barren</em>) was a large, loosely defined inland region of central Asia Minor occupying the central plateau of modern Turkey. Its boundaries shifted over time but typically covered the area between Lydia to the west and Cappadocia to the east. Phrygian cities important in early Christianity included Pisidian Antioch, Iconium, Laodicea, Hierapolis, and Colossae. Jews from Phrygia were present at Pentecost in Jerusalem (Acts 2:10), and Paul passed through the region on his second and third missionary journeys. The churches of the Lycus Valley — Colossae, Laodicea, Hierapolis — were effectively Phrygian congregations.</p>',
    'sections': [], 'hitchcock_meaning': 'dry; barren', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Acts 2:10', 'Acts 13:14', 'Acts 16:6', 'Acts 18:23']
  },
  'phut': {
    'id': 'phut', 'term': 'Phut', 'category': 'people',
    'intro': '<p>Phut (or Put) was the third son of Ham in the Table of Nations (Genesis 10:6) and the progenitor of the Libyan peoples of North Africa. The name is used in the prophets for Libya or a North African people allied with or subject to Egypt: Jeremiah 46:9, Ezekiel 27:10, 30:5, and 38:5 mention Put alongside Egypt, Ethiopia, and other African nations in oracles of judgment. The Revised Version and most modern translations render the name as Put or Libya in prophetic passages, distinguishing the people from the Libyan nation proper while maintaining the connection to the North African region.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Genesis 10:6', 'Jeremiah 46:9', 'Ezekiel 30:5']
  },
  'phygellus': {
    'id': 'phygellus', 'term': 'Phygellus', 'category': 'people',
    'intro': '<p>Phygellus (meaning: <em>fugitive</em>) was a Christian in the province of Asia who turned away from Paul, named alongside Hermogenes as one of those who abandoned the apostle in his time of need. Paul writes to Timothy that "all who are in Asia turned away from me, among whom are Phygellus and Hermogenes" (2 Timothy 1:15) — a statement likely referring to a specific failure to support Paul during his second Roman imprisonment rather than a general apostasy. Their departure is contrasted sharply with the faithful loyalty of Onesiphorus, who sought Paul out in Rome and was not ashamed of his chains.</p>',
    'sections': [], 'hitchcock_meaning': 'fugitive', 'source_ids': ['easton', 'smith'],
    'key_refs': ['2 Timothy 1:15']
  },
  'phylacteries': {
    'id': 'phylacteries', 'term': 'Phylacteries', 'category': 'concepts',
    'intro': '<p>Phylacteries (the Greek term for the Hebrew <em>tefillin</em>, meaning: <em>things to be especially observed</em>) were small leather boxes containing four passages of Scripture (Exodus 13:1–10, 13:11–16; Deuteronomy 6:4–9; 11:13–21) bound with leather straps to the forehead and left arm during morning prayers, based on the Mosaic command to bind the words of God as a sign on the hand and frontlets between the eyes. The practice reflected a literal interpretation of Deuteronomy 6:8. Jesus criticized the Pharisees for making their phylacteries broad and their tassels long to be seen by others — using religious observance for social display rather than genuine devotion.</p>',
    'sections': [], 'hitchcock_meaning': 'things to be especially observed', 'source_ids': ['easton'],
    'key_refs': ['Matthew 23:5', 'Deuteronomy 6:8', 'Exodus 13:9']
  },
  'physician': {
    'id': 'physician', 'term': 'Physician', 'category': 'concepts',
    'intro': '<p>Physicians in the ancient world practiced medicine through a combination of empirical observation, herbal remedies, and religious ritual. Israelite medicine was influenced by Egyptian practice, and the law code provided for recognizing and managing skin diseases, ritual uncleanness, and bodily discharges. The criticism of King Asa that "he did not seek the Lord, but sought help from physicians" (2 Chronicles 16:12) reflects a tension between seeking divine healing and medical means. Jesus references physicians in his saying "those who are well have no need of a physician, but those who are sick do" and in the aphorism "Physician, heal yourself." Paul\'s companion Luke is identified as "the beloved physician" in Colossians 4:14.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['2 Chronicles 16:12', 'Luke 4:23', 'Mark 2:17', 'Colossians 4:14']
  },
  'pi-beseth': {
    'id': 'pi-beseth', 'term': 'Pi-beseth', 'category': 'places',
    'intro': '<p>Pi-beseth (meaning: <em>abode of the goddess Bastet</em>) was an Egyptian city in the eastern delta region corresponding to the ancient Bubastis (modern Tell Basta), a major cult center of the cat-headed goddess Bastet. Ezekiel 30:17 includes Pi-beseth in his oracle against Egypt, predicting that its young men will fall by the sword and the city will go into captivity. Archaeological excavations have confirmed Bubastis as an important New Kingdom and Late Period city, and the discovery there of extensive cat mummies confirms its religious character.</p>',
    'sections': [], 'hitchcock_meaning': 'abode of the goddess Bahest or Bast', 'source_ids': ['easton'],
    'key_refs': ['Ezekiel 30:17']
  },
  'pi-hahiroth': {
    'id': 'pi-hahiroth', 'term': 'Pi-hahiroth', 'category': 'places',
    'intro': '<p>Pi-hahiroth (meaning: <em>the mouth; the pass of Hiroth</em>) was Israel\'s last campsite before the crossing of the Red Sea (or Sea of Reeds), located "between Migdol and the sea, in front of Baal-zephon." Here the Israelites, apparently trapped between the sea and the approaching Egyptian army, witnessed God\'s miraculous opening of the sea. The site is associated with the eastern edge of the Egyptian delta, though its precise location remains debated. It appears in both the Exodus narrative and in Numbers 33:7–8\'s retrospective itinerary as a landmark of the great deliverance.</p>',
    'sections': [], 'hitchcock_meaning': 'the mouth; the pass of Hiroth', 'source_ids': ['easton'],
    'key_refs': ['Exodus 14:2', 'Exodus 14:9', 'Numbers 33:7']
  },
  'pieces': {
    'id': 'pieces', 'term': 'Pieces', 'category': 'concepts',
    'intro': '<p>"Pieces of silver" in Scripture refers to varying denominations and weights of silver currency used in different periods. In the patriarchal period, Jacob purchased land at Shechem for a hundred <em>kesitah</em> (pieces). Joseph was sold for twenty pieces of silver, and Judas received thirty pieces of silver for betraying Jesus — the price of a slave in Mosaic law (Exodus 21:32) and the fulfillment of Zechariah 11:12–13. The pieces of silver in the New Testament are typically <em>shekels</em> or <em>staters</em>. Jesus\'s parable of the lost coin involves ten silver <em>drachmai</em>, each a day\'s wage.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Zechariah 11:12', 'Matthew 27:3', 'Genesis 33:19', 'Luke 15:8']
  },
  'piety': {
    'id': 'piety', 'term': 'Piety', 'category': 'concepts',
    'intro': '<p>Piety in the New Testament sense encompasses both reverence toward God and fulfillment of familial and social duties flowing from that reverence. The Greek <em>eusebeia</em> (godliness, reverence, piety) appears throughout the Pastoral Epistles as a key virtue of the Christian life — training in godliness is of value for all things, holding promise for the present life and the life to come. In 1 Timothy 5:4 piety specifically denotes the duty of children and grandchildren to support their widowed relatives — translated "show piety at home" — reflecting the connection between devotion to God and duty to family that the biblical concept consistently maintains. Paul warns in 2 Timothy 3:5 of those who have a form of godliness but deny its power.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Timothy 4:8', '1 Timothy 5:4', '2 Timothy 3:5', 'Titus 1:1']
  },
  'pigeon': {
    'id': 'pigeon', 'term': 'Pigeon', 'category': 'concepts',
    'intro': '<p>Pigeons (and doves) served as the specified sacrifice for those too poor to bring a lamb or goat. The Mosaic law accepted a pair of doves or young pigeons as a valid burnt offering (Leviticus 1:14), sin offering for a new mother (Leviticus 12:6), and purification sacrifice in other contexts. Abraham\'s covenant sacrifice in Genesis 15 included a turtledove and pigeon. Joseph and Mary presented two turtledoves or young pigeons at Jesus\'s presentation in the temple — the poverty offering — and Jesus drove out those selling doves at the temple entrance during the cleansing. The dove at Jesus\'s baptism echoes both the creation dove and Israel\'s sacrificial practice.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 15:9', 'Leviticus 1:14', 'Luke 2:24', 'John 2:14']
  },
  'pilate-pontius': {
    'id': 'pilate-pontius', 'term': 'Pilate, Pontius', 'category': 'people',
    'intro': '<p>Pontius Pilate was the Roman prefect (procurator) of Judea from approximately A.D. 26 to 36, the governor before whom Jesus was tried, condemned, and sentenced to crucifixion. All four Gospels describe the trial in detail: Pilate found no guilt in Jesus, repeatedly attempted to release him, was warned by his wife\'s dream, performed the symbolic hand-washing, and ultimately caved to the crowd\'s demands under threat of being reported to Caesar. His question "What is truth?" has become one of the most-quoted utterances in the passion narrative.</p><p>Pilate is mentioned in the Apostles\' and Nicene Creeds ("suffered under Pontius Pilate") as the historical anchor of the crucifixion. He was eventually recalled to Rome following a violent incident against the Samaritans and disappeared from the historical record.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Luke 23:4', 'John 18:38', 'Matthew 27:19', 'Acts 4:27']
  },
  'pillar': {
    'id': 'pillar', 'term': 'Pillar', 'category': 'concepts',
    'intro': '<p>Pillars in Scripture serve multiple functions — architectural, commemorative, and religious. Stone pillars (<em>matstsebah</em>) were set up as memorials by the patriarchs: Jacob at Bethel, at Rachel\'s tomb, and at the covenant with Laban; the Mosaic law later forbade the erection of pillars as cultic objects because of their association with Canaanite Baal worship. Samson pulled down the pillars of the Philistine temple on himself and his enemies. In Revelation the overcomer is promised to be a pillar in the temple of God. The pillar of cloud and fire that led Israel in the wilderness was the most prominent divine pillar — a visible manifestation of God\'s guiding and protective presence.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 28:18', 'Genesis 35:20', 'Judges 16:26', 'Revelation 3:12']
  },
  'pine-tree': {
    'id': 'pine-tree', 'term': 'Pine Tree', 'category': 'concepts',
    'intro': '<p>The pine tree of the Authorized Version translates several Hebrew words whose precise botanical identification remains disputed. In Isaiah 41:19 and 60:13 the KJV reads "pine tree" for the Hebrew <em>tidhar</em>, which some modern versions render as "pine," "elm," or "plane tree." Nehemiah 8:15 also includes a tree rendered "pine" in some versions in the list of branches to be used for building booths at the Feast of Tabernacles. The Aleppo pine (<em>Pinus halepensis</em>) does grow in Lebanon and the highlands of Carmel and Galilee, making the identification plausible for the Lebanese and northern contexts, though certainty remains elusive.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Isaiah 41:19', 'Isaiah 60:13', 'Nehemiah 8:15']
  },
  'pinnacle': {
    'id': 'pinnacle', 'term': 'Pinnacle', 'category': 'concepts',
    'intro': '<p>The pinnacle of the temple was the point in Satan\'s second temptation of Jesus, where Satan transported Jesus to the highest point of the Jerusalem temple complex and challenged him to throw himself down, citing Psalm 91\'s promise of angelic protection. The Greek word <em>pterygion</em> (literally "a little wing" or "a projection") likely refers to the southeastern corner of the temple mount, which according to Josephus was built up to an enormous height over the Kidron Valley. Jesus\'s refusal to put God to the test by an unnecessary and dramatic test of miraculous protection is the climax of the second temptation sequence.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Matthew 4:5', 'Luke 4:9']
  },
  'pipe': {
    'id': 'pipe', 'term': 'Pipe', 'category': 'concepts',
    'intro': '<p>The pipe or flute was one of the simplest and most widespread musical instruments of the ancient Near East, made from reed, bone, or wood and used in both sacred and secular contexts. In Israel pipes accompanied the anointing of kings (1 Kings 1:40), the processions of prophetic bands (1 Samuel 10:5), and the pilgrimages to Jerusalem\'s feasts (Isaiah 30:29). Jesus refers to the pipe in his parable of the children in the marketplace who played flute and expected their companions to dance. In the New Testament the flute (aulos) was used by mourners — Matthew 9:23 mentions flute-players at Jairus\'s house. Revelation 18:22 includes flute-players among the sounds of Babylon that will be heard no more.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['1 Samuel 10:5', '1 Kings 1:40', 'Isaiah 30:29', 'Matthew 9:23']
  },
  'piram': {
    'id': 'piram', 'term': 'Piram', 'category': 'people',
    'intro': '<p>Piram (meaning: <em>a wild ass of them</em>) was the king of Jarmuth in Canaan, one of the five Amorite kings who joined the coalition against Gibeon following the city\'s treaty with Israel. After the Gibeonites appealed to Joshua, he marched through the night from Gilgal and routed the coalition at Gibeon. Piram and his four confederate kings — the kings of Jerusalem, Hebron, Lachish, and Eglon — fled and hid in a cave at Makkedah, where they were trapped by Joshua until the Israelite forces returned, then brought out and publicly executed as a sign of God\'s total victory over Canaan\'s kings.</p>',
    'sections': [], 'hitchcock_meaning': 'a wild ass of them', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Joshua 10:3', 'Joshua 10:16', 'Joshua 10:26']
  },
  'pirathon': {
    'id': 'pirathon', 'term': 'Pirathon', 'category': 'places',
    'intro': '<p>Pirathon (meaning: <em>his dissipation or deprivation; his rupture</em>) was a town in the hill country of the Amalekites in the territory of Ephraim, mentioned as the home of two men in Israel\'s history: Abdon son of Hillel, who judged Israel for eight years and was buried there; and Benaiah the Pirathonite, one of David\'s thirty mighty warriors and later his chief bodyguard under Solomon. The site is identified with Far\'atah, about six miles west-southwest of Shechem in the Ephraimite highlands.</p>',
    'sections': [], 'hitchcock_meaning': 'his dissipation or deprivation; his rupture', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Judges 12:15', '2 Samuel 23:30', '1 Chronicles 11:31']
  },
  'pirathonite': {
    'id': 'pirathonite', 'term': 'Pirathonite', 'category': 'people',
    'intro': '<p>Pirathonite is the gentilical designation for persons from Pirathon in Ephraim, used of two men in Scripture: Abdon son of Hillel the Pirathonite, the tenth judge of Israel who judged for eight years and was buried in Pirathon in the land of Ephraim; and Benaiah the Pirathonite, a soldier in David\'s army listed among the twelve monthly division commanders and among the thirty mighty men. The latter\'s leadership of the division for the eleventh month (1 Chronicles 27:14) indicates his military prominence in David\'s administrative organization.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Judges 12:13', 'Judges 12:15', '2 Samuel 23:30']
  },
  'pisgah': {
    'id': 'pisgah', 'term': 'Pisgah', 'category': 'places',
    'intro': '<p>Pisgah (meaning: <em>hill; eminence; fortress</em>) was a ridge or peak in the Abarim mountain range east of the Jordan, across from Jericho in the territory of Moab, from whose summit Moses was granted his final panoramic view of the promised land before his death. "Go up to the top of Pisgah and look westward and northward and southward and eastward, and look at it with your eyes, for you shall not go over this Jordan" (Deuteronomy 3:27). Numbers 23:14 places Balaam at the field of Zophim on the top of Pisgah for one of his oracles. Pisgah is often identified with, or as a spur of, Nebo, the specific summit where Moses died.</p>',
    'sections': [], 'hitchcock_meaning': 'hill; eminence; fortress', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Deuteronomy 3:27', 'Numbers 23:14', 'Numbers 21:20', 'Deuteronomy 34:1']
  },
  'pisidia': {
    'id': 'pisidia', 'term': 'Pisidia', 'category': 'places',
    'intro': '<p>Pisidia (meaning: <em>pitch; pitchy</em>) was a mountainous region in southern Asia Minor, north of Pamphylia and east of Lycia, known for its rugged terrain and fierce independent population. The city "Antioch in Pisidia" (or Pisidian Antioch, actually located in Phrygia on its border with Pisidia) was an important Roman colonia visited twice by Paul and Barnabas on the first missionary journey. Paul\'s synagogue sermon there, preserved in Acts 13:14–41, is the most complete example of his early preaching and traces Israel\'s history from the exodus through David to Christ.</p>',
    'sections': [], 'hitchcock_meaning': 'pitch; pitchy', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Acts 13:14', 'Acts 14:21', 'Acts 14:24']
  },
  'pison': {
    'id': 'pison', 'term': 'Pison', 'category': 'places',
    'intro': '<p>Pison (meaning: <em>changing; extension of the mouth</em>) was one of the four rivers said in Genesis 2:11–12 to flow from the headwaters of the Garden of Eden, described as flowing "around the whole land of Havilah, where there is gold." The identification of the Pison with any known modern river is uncertain: proposals have included the Indus, the Ganges, the Nile, a Persian Gulf river system, and rivers of Arabia. The difficulty is compounded by the parallel identification of the Gihon with a river that flows around Cush, since none of the standard identifications produce a geographically coherent map of all four rivers from a single source.</p>',
    'sections': [], 'hitchcock_meaning': 'changing; extension of the mouth', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 2:11', 'Genesis 2:12']
  },
  'pit': {
    'id': 'pit', 'term': 'Pit', 'category': 'concepts',
    'intro': '<p>The pit in Scripture serves both as a literal feature of ancient Palestinian life and as a rich theological metaphor. Literally, pits or cisterns were common features of Israelite towns and farms, used for water storage; their uncovered state was a recognized hazard (Exodus 21:33–34). The pit as a place of confinement was used against Jeremiah (thrown into a muddy cistern) and Joseph (thrown into a dry pit by his brothers). Theologically the pit becomes a figure for Sheol or the underworld — the place of death and alienation from God. The psalmists cry to God from "the pit," and Revelation\'s "bottomless pit" (abyss) is a place of demonic imprisonment.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 37:24', 'Exodus 21:33', 'Psalms 40:2', 'Revelation 20:1']
  },
  'pitch': {
    'id': 'pitch', 'term': 'Pitch', 'category': 'concepts',
    'intro': '<p>Pitch (bitumen or asphalt) was a naturally occurring substance found in the ancient Near East, particularly in the region of the Dead Sea and in Mesopotamia, used as a waterproofing and adhesive material. Noah was instructed to coat the ark with pitch inside and out. The baby Moses\'s basket was waterproofed with pitch and tar. The valley of Siddim, where Sodom and Gomorrah were located, had numerous bitumen pits, and the fleeing kings fell into them during the battle with the four eastern kings. Isaiah uses burning pitch as an image of God\'s judgment on Edom (Isaiah 34:9–10).</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 6:14', 'Exodus 2:3', 'Genesis 14:10', 'Isaiah 34:9']
  },
  'pitcher': {
    'id': 'pitcher', 'term': 'Pitcher', 'category': 'concepts',
    'intro': '<p>The pitcher was a clay jar with handles used primarily for drawing and carrying water from wells and springs, a daily domestic task performed by women in the ancient Near East. Rebekah\'s readiness to water the camels of Abraham\'s servant demonstrated the generous character that identified her as Isaac\'s wife. Gideon\'s three hundred men carried empty pitchers concealing torches as part of the nighttime ambush of the Midianite camp. In the New Testament Jesus directs the disciples to follow a man carrying a jar of water to find the upper room for the Passover. The potter\'s vessel of clay becomes a biblical metaphor for human fragility and divine sovereignty.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Genesis 24:15', 'Judges 7:16', 'Judges 7:19', 'Mark 14:13']
  },
  'pithom': {
    'id': 'pithom', 'term': 'Pithom', 'category': 'places',
    'intro': '<p>Pithom (meaning: <em>their mouthful; a dilatation of the mouth</em>) was one of the two "store cities" built by Israelite slave labor in Egypt before the Exodus, along with Rameses. Exodus 1:11 records that the Egyptians "set taskmasters over them to afflict them with heavy burdens. They built for Pharaoh store cities, Pithom and Rameses." Pithom is identified by many scholars with Tell el-Maskhuta or Tell er-Retaba in the eastern delta region of Egypt, where archaeological excavations have found storage chambers and evidence of construction activity during the New Kingdom period. The city\'s establishment as a storage depot for military supplies reflects Egypt\'s expansion into the Sinai and Canaan during this era.</p>',
    'sections': [], 'hitchcock_meaning': 'their mouthful; a dilatation of the mouth', 'source_ids': ['easton', 'smith'],
    'key_refs': ['Exodus 1:11', 'Exodus 12:37']
  },
  'plague': {
    'id': 'plague', 'term': 'Plague', 'category': 'concepts',
    'intro': '<p>Plagues in Scripture are sudden, widespread afflictions sent by God as judgments on sin, the most famous being the ten plagues of Egypt by which God demonstrated his sovereignty over Pharaoh, the Egyptian gods, and the forces of nature before the Exodus. The plagues progressed in intensity from the Nile turning to blood through frogs, lice, flies, livestock disease, boils, hail, locusts, darkness, and the death of the firstborn. Numbers records several plagues sent against Israel in the wilderness for rebellion, including a deadly plague at Kibroth-hattaavah and a plague stopped by Phinehas\'s action at Peor. In the New Testament plagues appear prominently in Revelation\'s seven bowls and seven trumpets as eschatological judgments on a rebellious world.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Numbers 11:33', 'Numbers 16:46', 'Exodus 7:14', 'Revelation 15:1']
  },
  'plain': {
    'id': 'plain', 'term': 'Plain', 'category': 'concepts',
    'intro': '<p>Plains in Scripture include several distinct geographical features: the Jordan Valley plain visible from Lot\'s vantage point, which he chose for its fertility; the plain of Mamre associated with Abraham\'s encampment near Hebron; the plains of Moab where Israel camped before crossing into Canaan; and the plain of Esdraelon (Jezreel Valley). The Hebrew terms include <em>kikkar</em> (disk, circle — used of the Jordan plain), <em>biqah</em> (valley floor or broad valley), <em>mishor</em> (level ground, plateau), and <em>arabah</em> (the desert valley of the Jordan and Dead Sea region). Each term reflects a different topographical reality, and careful reading of biblical geography requires attention to which type of "plain" is intended.</p>',
    'sections': [], 'hitchcock_meaning': '', 'source_ids': ['easton'],
    'key_refs': ['Genesis 13:10', 'Genesis 14:17', 'Numbers 36:13', 'Deuteronomy 34:8']
  },
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP p2: Perazim, Mount → Plain: wrote {written}, skipped {skipped} existing.")

main()
