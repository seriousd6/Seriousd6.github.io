/* maps.js — Biblical Maps page (Leaflet.js + CartoDB Voyager tiles) */
'use strict';

import { _resolve, escHtml, READER_URL } from './core.js';
import { wireRefLinks } from './wire.js';
import { loadPlaces, getPlace } from './places.js';

/* ── Tile layer ──────────────────────────────────────────────────────────── */
var TILE_URL  = 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';
var TILE_ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>';

/* ── Canonical region geometry (single source shared with the timelapse) ────── */
// INTENT: data/maps/regions.json is the canonical, era-scoped source for region/empire/tribe
//   outlines. maps.js loads it once in initMapsPage and scene render() functions pull geometry
//   via _regionCoords(id, era). Inline coords remain at each call site as a safety fallback so
//   a missing/failed regions.json never blanks a map (we can't visually verify here).
// CHANGE? Region ids must match data/maps/regions.json `id` fields; era strings must match a
//   period's `era`. If a scene needs a region not yet in regions.json, add it there (don't
//   reintroduce a permanent inline-only shape) — the fallback arg is only a safety net.
// VERIFY: Load /maps/#twelve-tribes → tribe outlines match regions.json (tribe-* settlement
//   period). Block regions.json in DevTools → maps still render via inline fallbacks.
var _REGIONS_URL = _resolve('../../data/maps/regions.json');
var _REGIONS     = null;   // { id → region } once loaded; null until then / on failure

/* ── Canonical city coordinates ──────────────────────────────────────────── */
// INTENT: Single source of truth for recurring city lat/lon so future edits
//   don't drift across render functions. All array form [lat, lon].
// CHANGE? If you adjust a coordinate, it updates every map that uses COORDS.<name>.
//   Also update timelapse.json manually — it stores coords independently.
// VERIFY: Load each map; all city markers should land on the correct locations.
var COORDS = {
  jerusalem:  [31.777,  35.234],
  damascus:   [33.514,  36.276],
  babylon:    [32.536,  44.421],
  antioch:    [36.20,   36.16],   /* Antioch on the Orontes / Syrian Antioch */
  rome:       [41.90,   12.50],
  ephesus:    [37.94,   27.34],
  nineveh:    [36.359,  43.160],
  caesarea:   [32.50,   34.90],   /* Caesarea Maritima */
  carchemish: [36.844,  38.006],
  haran:      [36.863,  39.020],
  athens:     [37.98,   23.73],
  corinth:    [37.91,   22.88],
  troas:      [39.77,   26.12],
  miletus:    [37.52,   27.25],
  alexandria: [31.20,   29.92]
};

/* ── Map catalogue ───────────────────────────────────────────────────────── */
/* Overview strings use \n\n for paragraph breaks — rendered by _overviewHtml  */
var MAPS = [
  {
    id:       'holy-land',
    label:    'Holy Land (NT)',
    icon:     '🗺',
    title:    'Palestine in the Time of Jesus',
    sub:      'Galilee, Samaria, Judea, and beyond — c. AD 27–30',
    overview: 'Palestine in the first century was divided into Galilee, Samaria, and Judea — all under Roman rule through a combination of client kings (the Herods) and Roman prefects (like Pilate). The region was small enough to cross on foot in days, yet it became the stage for the central event in all of history: the incarnation, ministry, death, and resurrection of the Lord Jesus Christ.\n\nJesus grew up in Nazareth and launched his public ministry at his baptism in the Jordan (Matthew 3:13). His Galilean ministry — based in Capernaum (Matthew 4:13) — produced the Sermon on the Mount, the calling of the Twelve, and the great miracles of healing and nature. The long journey toward Jerusalem (Luke 9:51) culminates in the Triumphal Entry, the Last Supper, the agony in Gethsemane, and the Crucifixion outside the city walls at Golgotha (John 19:17).\n\nThe Resurrection and Ascension near Bethany (Luke 24:50–51) transformed a band of frightened disciples into bold witnesses. Pentecost in Jerusalem (Acts 2:1–4) marks the birth of the church — the new covenant community gathered from every nation by the Spirit poured out from the throne of the risen Christ, fulfilling Jesus\'s promise: "You will receive power when the Holy Spirit has come upon you, and you will be my witnesses" (Acts 1:8).',
    center:   [32.0, 35.3],
    zoom:     8,
    legend: [
      { type: 'dot',  color: '#b00010', label: 'Capital / significant city' },
      { type: 'dot',  color: '#444',    label: 'Town / village' }
    ],
    render: _renderHolyLand
  },
  {
    id:       'paul-journeys',
    label:    "Paul's Journeys",
    icon:     '⛵',
    title:    "Paul's Missionary Journeys",
    sub:      'Three journeys + the voyage to Rome — c. AD 46–60',
    overview: "Paul's three missionary journeys (c. AD 46–57) and his voyage to Rome (AD 59–60) span the eastern Mediterranean world — from Syrian Antioch through Asia Minor, Macedonia, and Greece to the imperial capital. He traveled on Roman roads and by sea, planting churches in strategic cities from which the gospel spread to surrounding regions.\n\nThe first journey (Acts 13–14) planted churches in Cyprus and Galatia. The second (Acts 15–18) crossed into Europe — Philippi, Thessalonica, Athens, Corinth. The third (Acts 18–21) centered on a three-year ministry in Ephesus: 'all who lived in Asia heard the word of the Lord, both Jews and Greeks' (Acts 19:10). Paul's final voyage to Rome (Acts 27–28) ended in shipwreck at Malta before his arrival under house arrest — where he preached 'with all boldness and without hindrance' (Acts 28:31).\n\nPaul's journeys are the fulfillment of Jesus's commission in Acts 1:8. The letters he wrote to these churches — Galatians, 1–2 Thessalonians, 1–2 Corinthians, Romans, Ephesians, Philippians, Colossians — form the heart of the New Testament epistles. His own summary: 'From Jerusalem and all the way around to Illyricum I have fulfilled the ministry of the gospel of Christ' (Romans 15:19).",
    center:   [38.5, 24.0],
    zoom:     5,
    legend: [
      { type: 'line', color: '#c44d29', label: '1st journey (AD 46–48)' },
      { type: 'line', color: '#1a5fa8', label: '2nd journey (AD 49–51)' },
      { type: 'line', color: '#3d7a4a', label: '3rd journey (AD 52–57)' },
      { type: 'line', color: '#7b5ea7', label: 'Voyage to Rome (AD 59–60)', dashed: true }
    ],
    render: _renderPaulJourneys
  },
  {
    id:       'exodus',
    label:    'The Exodus',
    icon:     '🏜',
    title:    'The Exodus Route',
    sub:      "Israel's journey from Egypt to Canaan — c. 1446–1406 BC",
    overview: 'The Exodus stands as the defining act of Israel\'s national redemption — God delivering his enslaved people from 430 years of bondage in Egypt through ten plagues, the Passover, and the crossing of the Red Sea (Exodus 1–15). The route shown follows the traditional southern Sinai itinerary placing Mount Sinai at Jebel Musa; northern and Midianite alternatives are debated by scholars.\n\nKey events by location: Rameses/Goshen — the Passover night and departure (Exodus 12:37); Red Sea — the sea divided, Pharaoh\'s army drowned, the Song of Moses (Exodus 14–15); Marah — bitter water made sweet (Exodus 15:23); Rephidim — water from the rock, Amalek defeated by Moses\'s raised hands (Exodus 17); Mount Sinai — the Ten Commandments, the covenant ratified, the Tabernacle built and filled with glory (Exodus 19–40); Kadesh-barnea — the twelve spies sent, unbelief condemns Israel to forty years of wandering (Numbers 13–14); Plains of Moab — Deuteronomy preached, Moses\'s death, Joshua commissioned (Deuteronomy 31–34).\n\nThe Exodus is the interpretive lens for the entire Bible\'s understanding of salvation. The Passover lamb points to Christ, "our Passover lamb" (1 Corinthians 5:7). The Red Sea crossing is a "baptism into Moses" — a type of dying and rising with Christ out of slavery into freedom (1 Corinthians 10:1–2). The manna points to Jesus, the true bread from heaven (John 6:31–35). Hebrews 3–4 holds the wilderness generation up as a solemn warning: do not harden your hearts in unbelief as they did.',
    center:   [29.8, 33.5],
    zoom:     6,
    legend: [
      { type: 'line', color: '#c44d29', label: 'Exodus route' },
      { type: 'line', color: '#c44d29', label: '40-year wandering', dashed: true }
    ],
    render: _renderExodus
  },
  {
    id:       'divided-kingdom',
    label:    'Divided Kingdom',
    icon:     '👑',
    title:    'Israel & Judah — The Divided Kingdom',
    sub:      'Northern Israel and Southern Judah — 931–586 BC',
    overview: "When Rehoboam, Solomon's son, refused to lighten the burden of heavy taxation, Jeroboam son of Nebat led ten northern tribes in revolt — fulfilling God's word through the prophet Ahijah (1 Kings 11:29–39). From 931 BC, Israel was split: the northern kingdom of Israel (capital: Samaria, 19 kings, all evil) and the southern kingdom of Judah (capital: Jerusalem, 20 kings, a few righteous).\n\nNorthern Israel was corrupted from the start by Jeroboam's two golden calves at Bethel and Dan. The prophets Elijah, Elisha, Amos, and Hosea all ministered in the north against deepening apostasy. Sargon II of Assyria took Samaria in 722 BC and deported 27,290 Israelites (2 Kings 17:6). Judah survived Sennacherib's massive siege under Hezekiah through miraculous deliverance (2 Kings 19:35), but fell to Nebuchadnezzar in 586 BC when he destroyed the Temple and marched the survivors to Babylon (2 Kings 25:9).\n\nThe divided kingdom exposes the failure of human kingship under the Mosaic covenant. Not even the best kings — Hezekiah, Josiah — could secure lasting obedience. This failure drives the prophetic cry for a new covenant (Jeremiah 31:31–34) and a new David (Ezekiel 37:24–25) — the one true King who would succeed where all others failed, ruling by the Spirit rather than by law.",
    center:   [32.0, 35.3],
    zoom:     8,
    legend: [
      { type: 'swatch', color: 'rgba(100,160,220,0.35)', label: 'Israel (Northern Kingdom)' },
      { type: 'swatch', color: 'rgba(210,170,80,0.35)',  label: 'Judah (Southern Kingdom)' },
      { type: 'dot',    color: '#1a5fa8', label: 'Northern capital (Samaria)' },
      { type: 'dot',    color: '#9b2335', label: 'Southern capital (Jerusalem)' }
    ],
    render: _renderDividedKingdom
  },
  {
    id:       'ancient-near-east',
    label:    'Ancient Near East',
    icon:     '🌍',
    title:    'The Ancient Near East',
    sub:      'Egypt, Canaan, Assyria, Babylon, and Persia — the OT world',
    overview: 'The world of the Old Testament was shaped by the great empires of the ancient Near East — Egypt to the southwest, Assyria and Babylon in Mesopotamia, and Persia to the east. Israel occupied a narrow land corridor between sea and desert, through which every major power had to march — perpetually contested territory that drove Israel to dependence on God rather than geopolitical alliance.\n\nThe empires in view span roughly 2,000 years: Egypt enslaved Israel (Exodus 1) and defeated Josiah at Megiddo (2 Kings 23:29). Assyria destroyed the northern kingdom (722 BC, 2 Kings 17). Babylon destroyed Jerusalem and the Temple (586 BC, 2 Kings 25). Persia ended the exile through Cyrus\'s decree (538 BC, Ezra 1:1–4). The cities of Ur, Haran, Nineveh, Babylon, and Susa all appear in the biblical narrative as God exercises sovereign rule over nations that do not know him.\n\nThe biblical claim underlying this entire map is audacious: the God of small Israel is the Lord of all empires. Egypt\'s Pharaoh is his instrument (Romans 9:17). Assyria is "the rod of his anger" (Isaiah 10:5). Babylon is his servant (Jeremiah 25:9). Cyrus is his "anointed" (Isaiah 45:1). Every empire rises and falls on his word — a claim that seemed impossible from inside a besieged city, yet was vindicated again and again across the centuries.',
    center:   [31.0, 40.0],
    zoom:     4,
    legend: [
      { type: 'dot', color: '#b00010', label: 'Major empire capital' },
      { type: 'dot', color: '#444',    label: 'City' }
    ],
    render: _renderAncientNearEast
  },
  /* ── New thematic maps ── */
  {
    id:       'patriarchal-journeys',
    label:    'Patriarchal Journeys',
    icon:     '🐪',
    title:    'Journeys of the Patriarchs',
    sub:      'Abraham, Jacob, and Joseph — c. 2100–1800 BC',
    overview: "The patriarchal era begins with God's call to Abraham from Ur of the Chaldeans (c. 2091 BC) and ends with Jacob's family of 70 settling in Egypt under Joseph's protection (c. 1876 BC). These were 'strangers and exiles on the earth' (Hebrews 11:13), holding nothing but a promise: land, innumerable descendants, and blessing for all nations through their offspring (Genesis 12:1–3).\n\nAbraham's journey: Ur → Haran (Terah dies) → Shechem (first altar, Genesis 12:6) → Bethel → Egypt (famine) → Hebron. The key events: the covenant confirmed at night with the smoking firepot (Genesis 15:17); the binding of Isaac on Moriah (Genesis 22); the cave of Machpelah purchased as the first title to the promised land (Genesis 23:19). Jacob's journey: Beersheba → Bethel (the ladder, Genesis 28:12) → Haran (twenty years with Laban) → Mahanaim (angels, Genesis 32:2) → Peniel (wrestles with God, receives the name Israel, Genesis 32:28) → Shechem → Hebron. Joseph: sold at Dothan (Genesis 37:28), carried to Egypt, imprisoned, elevated to second-in-command; the whole family of 70 reunites in Egypt (Genesis 46:6).\n\nHebrews 11 reads these journeys as a gallery of faith: each patriarch 'died in faith, not having received the things promised, but having seen them and greeted them from afar' (Hebrews 11:13). The promise they held — land, offspring, blessing for all nations — is the gospel preached in advance (Galatians 3:8), finding its fulfillment in Jesus Christ, the offspring of Abraham in whom all nations are blessed.",
    center:   [32.5, 38.0],
    zoom:     5,
    legend: [
      { type: 'line', color: '#c44d29', label: "Abraham's journey" },
      { type: 'line', color: '#1a5fa8', label: "Jacob's journey" },
      { type: 'line', color: '#3d7a4a', label: "Joseph sold to Egypt", dashed: true }
    ],
    render: _renderPatriarchalJourneys
  },
  {
    id:       'conquest',
    label:    'Conquest of Canaan',
    icon:     '⚔',
    title:    'The Conquest of Canaan',
    sub:      "Joshua's southern and northern campaigns — c. 1406–1390 BC",
    overview: 'The conquest of Canaan (c. 1406–1390 BC) was the fulfillment of God\'s promise to Abraham four centuries earlier: "To your offspring I will give this land" (Genesis 12:7). Under Joshua son of Nun, Israel crossed the Jordan on dry ground — a second Exodus miracle (Joshua 3–4) — and launched three campaign phases from their base at Gilgal.\n\nKey battles: Jericho — walls fell after seven days of circling by faith (Joshua 6); Ai — initially defeated due to Achan\'s hidden sin, then taken by a masterful ambush (Joshua 7–8); Gibeon — the five-king coalition routed; the sun stood still for a full day (Joshua 10:12–14); Lachish — taken in one day (Joshua 10:32); Hebron — claimed by the 85-year-old Caleb who drove out the Anakim giants, fulfilling Moses\'s promise made forty-five years earlier (Joshua 14:13); Hazor — "head of all those kingdoms," burned (Joshua 11:10); Waters of Merom — the vast northern coalition destroyed. After the campaigns, the land was divided by lot among the twelve tribes at Shiloh (Joshua 18:1).\n\nThe conquest raises hard questions about the ban (ḥērem — total destruction) that the text answers only in part: Canaan\'s judgment had been stored up for 400 years (Genesis 15:16). More importantly, the conquest is a gift of grace: the land is taken not by military superiority but by faith — faith expressed in tactics that would fail without God (circling walls, splitting forces at Ai). And Rahab the Gentile prostitute, saved by a scarlet cord (Joshua 2:21), signals that the conquest is ultimately about grace, not ethnicity.',
    center:   [31.8, 35.3],
    zoom:     8,
    legend: [
      { type: 'line', color: '#c44d29', label: 'Southern campaign' },
      { type: 'line', color: '#1a5fa8', label: 'Northern campaign' },
      { type: 'dot',  color: '#b00010', label: 'Battle site' },
      { type: 'dot',  color: '#444',    label: 'City / landmark' }
    ],
    render: _renderConquest
  },
  {
    id:       'twelve-tribes',
    label:    'Twelve Tribes',
    icon:     '🏕',
    title:    'The Twelve Tribes of Israel',
    sub:      'Tribal allotments after the conquest — c. 1400–1050 BC',
    overview: "After the conquest, Joshua assembled the whole congregation at Shiloh and distributed the promised land by lot among the twelve tribes (Joshua 18:1–10). The Tabernacle was set up at Shiloh in Ephraim and remained there as the worship center for approximately 300 years. The Levites received no territorial allotment — 48 Levitical cities were scattered throughout all the tribes — because 'the LORD God of Israel is their inheritance' (Joshua 13:33).\n\nWest of the Jordan: Judah and Simeon in the south; Benjamin between Judah and Ephraim (Jerusalem sat on their shared border); Dan originally assigned the coastal strip west of Benjamin (but most migrated north to Laish/Dan due to pressure from Amorites, Judges 1:34); Ephraim and West Manasseh in the central highlands; Issachar and Zebulun in the Jezreel Valley; Asher along the Phoenician coast; Naphtali in Upper Galilee. East of the Jordan (Transjordan): Reuben on the Moabite plateau, Gad in Gilead, and East Manasseh in Bashan — all three bound by oath to cross over and fight with their brothers until the land was taken (Joshua 1:14–15).\n\nThe tribal map is the geography of covenant inheritance — each tribe's portion was a tangible installment on the promise made to Abraham. But the map also shows the fractures to come: Dan's failure to hold its western territory prefigures Israel's spiritual drift. Simeon's absorption into Judah fulfilled Jacob's dying prophecy (Genesis 49:7). And Judah's central, large allotment — containing Jerusalem and Bethlehem — fulfills Jacob's word: 'The scepter shall not depart from Judah' (Genesis 49:10).",
    center:   [32.0, 35.5],
    zoom:     7,
    legend: [
      { type: 'swatch', color: 'rgba(179,60,60,0.4)',   label: 'Judah / Simeon' },
      { type: 'swatch', color: 'rgba(34,85,170,0.4)',   label: 'Ephraim / Manasseh' },
      { type: 'swatch', color: 'rgba(46,140,124,0.4)',  label: 'Galilee tribes (Zebulun, Naphtali, Asher, Issachar)' },
      { type: 'swatch', color: 'rgba(139,92,26,0.4)',   label: 'Transjordan (Gad, Reuben, Manasseh-E)' }
    ],
    render: _renderTwelveTribes
  },
  {
    id:       'judges',
    label:    'Time of the Judges',
    icon:     '🛡',
    title:    'Israel in the Time of the Judges',
    sub:      'Key battles and deliverances — c. 1380–1050 BC',
    overview: "The period of the Judges (c. 1380–1050 BC) is among the most sobering in Scripture. Following the death of Joshua, Israel repeatedly fell into a cycle: they abandoned the LORD → God allowed an oppressing nation to punish them → they cried out → God raised a judge (šōpēṭ — deliverer/ruler) → rest → judge died → the cycle began again, each time worse. The book concludes with a haunting refrain: 'In those days there was no king in Israel. Everyone did what was right in his own eyes' (Judges 21:25).\n\nThe major judges and their conflicts: Othniel — delivered from Cushan-Rishathaim of Mesopotamia (Judges 3:9); Deborah and Barak — defeated Sisera's 900 iron chariots at the Kishon River; Jael drove a tent peg through Sisera's skull (Judges 4–5); Gideon — 300 men with torches and clay jars routed the Midianites in the Jezreel Valley; 'A sword for the LORD and for Gideon!' (Judges 7:20); Jephthah — defeated the Ammonites but bound himself by a rash vow (Judges 11); Samson — a Nazirite from birth with supernatural strength, a thirty-year conflict with the Philistines ending in the temple of Dagon at Gaza (Judges 13–16). The era ends with the capture of the Ark at Aphek — God allowing even the symbol of his presence to be taken, to prove that covenant relationship cannot be presumed upon (1 Samuel 4:11).\n\nThe book of Judges is not primarily a moral gallery of heroes to emulate. It is a diagnosis of the human heart without the transforming grace of God. Each judge is more flawed than the last. The book progressively argues that Israel needs not just a better deliverer but a fundamentally different kind of king — one righteous from the inside, who rules by the Spirit. That longing is partially answered in David, and finally answered in Jesus Christ, the true and perfect Judge and King.",
    center:   [32.0, 35.3],
    zoom:     8,
    legend: [
      { type: 'dot', color: '#b00010', label: 'Battle site' },
      { type: 'dot', color: '#7b5ea7', label: 'Judge hometown / key location' },
      { type: 'dot', color: '#444',    label: 'Philistine city' }
    ],
    render: _renderJudges
  },
  {
    id:       'david-kingdom',
    label:    "David's Kingdom",
    icon:     '⭐',
    title:    "David's Kingdom and Military Campaigns",
    sub:      'The united monarchy at its greatest extent — c. 1010–970 BC',
    overview: "David's reign (c. 1010–970 BC) is the high-water mark of Israel's national history. After seven and a half years as king of Judah in Hebron (2 Samuel 2:11), all Israel anointed David king at age 37 (2 Samuel 5:3). He captured Jerusalem from the Jebusites and made it his capital — a politically brilliant choice, belonging to no single tribe. He brought the ark to Jerusalem with dancing and great joy (2 Samuel 6), then received the greatest divine promise in the Old Testament: the Davidic covenant (2 Samuel 7).\n\nDavid's military campaigns extended his rule from Egypt's border to the Euphrates: the Philistines subjugated (2 Samuel 5:17–25, 8:1); Moab made tributary (2 Samuel 8:2); Aram-Zobah and Damascus defeated and garrisoned (2 Samuel 8:5–6); Edom crushed in the Valley of Salt, 18,000 killed (2 Samuel 8:13); Ammon besieged at Rabbah — the occasion of the great fall with Bathsheba and the murder of Uriah (2 Samuel 11). 'The LORD gave David victory wherever he went' (2 Samuel 8:14) — yet the king who conquered every nation nearly lost his own soul.\n\nThe Davidic covenant (2 Samuel 7:12–16) is the summit of the Old Testament: God promises that David's offspring will build a house for his name, and that God will establish that throne forever — 'I will be to him a father, and he shall be to me a son.' The prophets orient every messianic hope around this covenant (Isaiah 9:7; Ezekiel 37:24; Amos 9:11). Matthew begins his Gospel with 'Jesus Christ, the son of David' — and the throne that David established becomes, in Christ, a throne that will never end.",
    center:   [31.5, 36.0],
    zoom:     6,
    legend: [
      { type: 'swatch', color: 'rgba(180,140,40,0.2)', label: "David's kingdom (core + vassal states)" },
      { type: 'line',   color: '#b00010', label: 'Military campaigns' },
      { type: 'dot',    color: '#b00010', label: 'Capital / key city' }
    ],
    render: _renderDavidKingdom
  },
  {
    id:       'invasions',
    label:    'Assyrian & Babylonian Invasions',
    icon:     '🔥',
    title:    'Assyrian and Babylonian Invasions',
    sub:      'The fall of Samaria (722 BC) and Jerusalem (586 BC)',
    overview: 'The great empires swept through the land of Israel as instruments of divine covenant judgment. Moses had warned six centuries earlier: if Israel broke the covenant, God would send foreign nations against them, culminating in exile (Deuteronomy 28:36–68; Leviticus 26:27–39). What looked like military defeat was actually theological statement — the God of Israel was himself executing the curses his people had earned.\n\nAssyrian campaigns: Tiglath-Pileser III deported northern and eastern tribes in 733 BC (2 Kings 15:29). Shalmaneser V besieged Samaria; Sargon II completed the conquest in 722 BC, deporting 27,290 Israelites (2 Kings 17:6). Sennacherib marched through Judah in 701 BC, besieging Lachish and surrounding Jerusalem — but the Angel of the LORD struck 185,000 Assyrian soldiers in a single night (2 Kings 19:35). Babylonian campaigns: Nebuchadnezzar crushed Egypt at Carchemish in 605 BC (Jeremiah 46:2), then in three waves — 605 BC (Daniel), 597 BC (Jehoiachin), 586 BC — destroyed the Temple and city, marching the survivors to Babylon (2 Kings 25).\n\nYet the exile was not the end of the story — it was the midpoint. From the ruins God spoke through Jeremiah: "I will make a new covenant… I will write it on their hearts" (Jeremiah 31:31–33). From Babylon, Ezekiel saw dry bones live again (Ezekiel 37). Isaiah proclaimed a Servant who would suffer for the sins of his people and see light after his anguish (Isaiah 52–53). The deportation that looked like utter defeat was the prologue to the deepest promises ever spoken.',
    center:   [33.0, 39.0],
    zoom:     5,
    legend: [
      { type: 'line', color: '#8b1a1a', label: 'Assyrian invasion — Samaria falls (722 BC)' },
      { type: 'line', color: '#c44d29', label: "Sennacherib's siege — Jerusalem spared (701 BC)" },
      { type: 'line', color: '#1a3a6b', label: 'Babylonian invasions — Jerusalem falls (586 BC)', dashed: true }
    ],
    render: _renderInvasions
  },
  {
    id:       'intertestamental',
    label:    'Intertestamental',
    icon:     '🏛',
    title:    'Between the Testaments',
    sub:      'Alexander, the Maccabees, and Rome — 400–4 BC',
    overview: 'Between the last word of Malachi and the first word of Matthew\'s Gospel lie four centuries of prophetic silence — no new Scripture, no prophet. Yet these were not empty years: they were the years in which God prepared the world for the fullness of time (Galatians 4:4).\n\nAlexander the Great\'s conquest of the Persian Empire (334–323 BC) reshaped the world. Within twelve years, one language — Greek — became the common tongue from Egypt to India. In Alexandria the Hebrew Scriptures were translated into Greek (the Septuagint, c. 250–150 BC), placing them in the hands of every literate person in the Mediterranean world. Roman roads and the Pax Romana would later give the gospel free passage across that same world. What looked like imperial conquest was providential preparation.\n\nFor Judea, the Hellenistic era brought intense spiritual pressure. Under the Seleucid king Antiochus IV Epiphanes (175–164 BC), Hellenization was enforced by decree — circumcision banned, Torah burned, the Temple altar given to Zeus. In 167 BC Antiochus sacrificed swine on the altar in Jerusalem — the "abomination of desolation" (Daniel 11:31) that Jesus would later cite as a type of future sacrilege (Matthew 24:15). The Maccabean family — Mattathias and his five sons — rose in revolt from Modein; Judas Maccabeus recaptured Jerusalem in 164 BC, cleansed the Temple, and rededicated it. This is the origin of Hanukkah, the "Feast of Dedication" at which Jesus walked in Solomon\'s Colonnade (John 10:22).\n\nThe Hasmonean dynasty that followed ruled for a century, but gradual corruption and civil war opened the door for Rome. In 63 BC the Roman general Pompey besieged Jerusalem, entered the Holy of Holies, and peered inside — then walked out, astonished to find no idol, no statue, no visible deity. He left the Temple intact but made Judea a Roman client. He appointed an Idumean family as local rulers: the Herods. Herod the Great (37–4 BC) ruled by terror and political genius, rebuilding the Temple in unprecedented splendor — the very Temple in which Jesus would teach. Into this world, in the fullness of time, God sent forth his Son.',
    center:   [32.5, 35.5],
    zoom:     5,
    legend: [
      { type: 'line',   color: '#4a7fcb', label: "Alexander's conquest (334–323 BC)" },
      { type: 'line',   color: '#b33c3c', label: 'Maccabean revolt (167–164 BC)' },
      { type: 'line',   color: '#8b1a1a', label: "Pompey's campaign — Rome enters (63 BC)", dashed: true },
      { type: 'swatch', color: 'rgba(155,112,0,0.28)',  label: 'Ptolemaic sphere (c. 323–198 BC)' },
      { type: 'swatch', color: 'rgba(123,94,167,0.22)', label: 'Seleucid Empire (c. 312–64 BC)' },
      { type: 'swatch', color: 'rgba(179,60,60,0.28)',  label: 'Hasmonean Kingdom (c. 165–63 BC)' }
    ],
    render: _renderIntertestamental
  },
  /* ── New maps ── */
  {
    id:       'solomon-kingdom',
    label:    "Solomon's Kingdom",
    icon:     '🏛',
    title:    "Solomon's Kingdom & Trade Routes",
    sub:      'The united monarchy at its height — temple, trade, and empire — c. 970–931 BC',
    overview: "Solomon's reign (c. 970–931 BC) saw Israel reach its greatest territorial extent and economic prosperity. He ruled 'over all the kings from the Euphrates to the border of Egypt' (1 Kings 4:21), collecting tribute from surrounding nations. His administrative districts supplied the royal household; his fleet at Ezion-geber (1 Kings 9:26) opened Red Sea trade to Ophir; his alliance with Hiram of Tyre brought cedar, gold, and craftsmen from Phoenicia.\n\nSolomon's greatest achievement was the Temple in Jerusalem (1 Kings 5–8), built in seven years from the finest materials and filled at its dedication with the glory cloud (1 Kings 8:10–11). He also rebuilt Megiddo, Hazor, and Gezer as fortified chariot cities (1 Kings 9:15–17). The Queen of Sheba journeyed from Arabia to test his wisdom (1 Kings 10:1–13) — and was overwhelmed: 'The half was not told me.' Her visit is a preview of the eschatological vision of Gentile nations streaming to Israel's king (Isaiah 60:1–6).\n\nSolomon's kingdom carried the seeds of its own destruction. His 700 wives and 300 concubines from surrounding nations 'turned his heart after other gods' (1 Kings 11:4), violating the explicit prohibition of Deuteronomy 17:17. The crushing forced labor that built his projects (1 Kings 5:13) fractured the kingdom at his death. Jesus cited Solomon's glory as a foil: 'Even Solomon in all his glory was not arrayed like one of these' lilies (Matthew 6:29). The one greater than Solomon (Matthew 12:42) builds his kingdom not of cut stone and trade routes but of living stones and the Spirit.",
    center:   [30.5, 36.5],
    zoom:     5,
    legend: [
      { type: 'line', color: '#c44d29', label: 'Red Sea trade route (Ezion-geber)' },
      { type: 'line', color: '#1a5fa8', label: 'Phoenician alliance (Tyre)' },
      { type: 'line', color: '#3d7a4a', label: 'Egypt trade route (horses & chariots)' },
      { type: 'line', color: '#9b7000', label: 'Caravan route (Tadmor)', dashed: true },
      { type: 'dot',  color: '#b00010', label: 'Capital / fortified city' }
    ],
    render: _renderSolomonKingdom
  },
  {
    id:       'return-exile',
    label:    'Return from Exile',
    icon:     '🕊',
    title:    'The Return from Exile',
    sub:      'Cyrus, Zerubbabel, Ezra, and Nehemiah — c. 538–400 BC',
    overview: "In 539 BC Cyrus the Great of Persia conquered Babylon and issued a decree allowing Jewish exiles to return home and rebuild the Temple (Ezra 1:1–4). Isaiah had named Cyrus by name 150 years before his birth and called him God's 'anointed' — the surprising instrument of the new exodus (Isaiah 44:28–45:1). The return happened in three main waves over nearly a century.\n\nZerubbabel led approximately 49,897 exiles back in 538 BC (Ezra 2:64–65), laid the Temple foundation amid weeping and shouting (Ezra 3:12), and — after years of opposition from Samaria — completed the second Temple in 516 BC (Ezra 6:15). Ezra the scribe returned in 458 BC with a second group, carrying the law of God; he confronted the community's intermarriage with surrounding peoples (Ezra 7–10). Nehemiah, cupbearer to Artaxerxes in Susa, heard Jerusalem's walls lay in ruins and obtained permission to rebuild (Nehemiah 1–2). He completed the entire wall in 52 days (Nehemiah 6:15) — then Ezra read the law publicly, the people wept, and the covenant was renewed (Nehemiah 8–10).\n\nThe return was a real but partial fulfillment of the prophetic promises. The restored community was small, poor, and a Persian vassal. The glory cloud did not return to the second Temple (Haggai 2:3). The Davidic throne was not restored. Malachi — the last prophet before 400 years of silence — called the people to covenant faithfulness and promised that the Lord himself would come suddenly to his Temple (Malachi 3:1). Full restoration awaited the coming of the one who is 'greater than the temple' (Matthew 12:6) and who would build the true new Jerusalem.",
    center:   [33.5, 41.5],
    zoom:     5,
    legend: [
      { type: 'line', color: '#3d7a4a', label: 'Return route (Babylon → Jerusalem)' },
      { type: 'line', color: '#3d7a4a', label: 'Ezra\'s route from Susa', dashed: true },
      { type: 'dot',  color: '#b00010', label: 'Capital / key city' }
    ],
    render: _renderReturnExile
  },
  {
    id:          'seven-churches',
    label:       'Seven Churches',
    icon:        '✉',
    title:       'The Seven Churches of Revelation',
    sub:         'Letters to the churches of Asia Minor — c. AD 95',
    defaultBook: 'Revelation',
    overview: "The seven churches of Revelation (Revelation 2–3) were real congregations in the Roman province of Asia (western Turkey), situated on a circular postal route from Ephesus northward to Pergamum, then south and east to Thyatira, Sardis, Philadelphia, and Laodicea. John was exiled on the island of Patmos (Revelation 1:9) when he received these letters from the risen Christ — each addressed to the 'angel' of the church, each carrying a personal word of diagnosis and call.\n\nEach letter follows a pattern: a title for Christ drawn from the opening vision; a word of commendation (except Sardis and Laodicea, who receive none); a rebuke; a call to repentance; and a promise to 'the one who overcomes.' The seven profiles: Ephesus (2:1–7) — doctrinally vigilant but loveless; Smyrna (2:8–11) — persecuted but faithful, receiving no rebuke; Pergamum (2:12–17) — tolerating worldly compromise; Thyatira (2:18–29) — false teaching allowed; Sardis (3:1–6) — a reputation for life but dead; Philadelphia (3:7–13) — faithful under weakness, given an open door; Laodicea (3:14–22) — self-sufficient and lukewarm, Christ standing outside knocking.\n\nThese seven letters are simultaneously first-century pastoral correspondence and enduring addresses to the church in every age. Every congregation in every era recognizes itself somewhere in these seven profiles — loveless orthodoxy, faithful suffering under persecution, worldly compromise, spiritual deadness, self-sufficient lukewarmness. The call is always the same: 'He who has an ear, let him hear what the Spirit says to the churches' (Revelation 2:7). The promise is always the same: the overcomer shares in the eschatological glory of the new creation.",
    center:   [38.5, 27.8],
    zoom:     7,
    legend: [
      { type: 'line', color: '#7b5ea7', label: 'Postal circuit (Patmos → seven churches)' },
      { type: 'dot',  color: '#7b5ea7', label: 'Church city' },
      { type: 'dot',  color: '#444',    label: 'Patmos (John\'s exile)' }
    ],
    render: _renderSevenChurches
  },
  {
    id:       'jerusalem',
    label:    'Jerusalem',
    icon:     '✝',
    title:    'Jerusalem — The Holy City',
    sub:      "Melchizedek's Salem to the New Jerusalem — c. 2000 BC – AD 100",
    overview: "Jerusalem stands at the geographic and redemptive center of all of Scripture. It first appears as Salem, where the priest-king Melchizedek brought bread and wine to Abraham and received his tithe — a mysterious figure who prefigures the eternal priesthood of Christ (Genesis 14:18; Hebrews 7:1). On the hill of Moriah — the same site — God commanded Abraham to sacrifice Isaac, provided a ram in his place, and spoke the word that echoed through the ages: 'The LORD will provide' (Genesis 22:14). A thousand years later, David captured the Jebusite stronghold of Zion and made it his capital, bringing the ark of the covenant here with dancing and rejoicing (2 Samuel 5:7; 6:15). On the threshing floor of Araunah he built an altar and saw the plague stopped — the site God designated for the Temple (2 Samuel 24:25; 2 Chronicles 3:1).\n\nSolomon built the Temple in seven years, and at its dedication the glory cloud filled the house so that the priests could not stand to minister (1 Kings 8:10–11) — God himself dwelling among his people. For four centuries this Temple was the heart of Israel's worship. The city survived Sennacherib's siege when the Angel of the LORD struck 185,000 Assyrian soldiers in a single night (2 Kings 19:35), only to fall to Nebuchadnezzar in 586 BC when the covenant curses of Deuteronomy 28 were finally executed. Solomon's Temple was burned; the people were marched to Babylon. The returning exiles rebuilt a humbler Second Temple, dedicated in 516 BC with weeping and rejoicing together (Ezra 3:12–13). Judas Maccabeus rededicated it in 164 BC after Antiochus's desecration. Herod the Great, beginning c. 20 BC, expanded and beautified it to staggering proportions — one of the architectural wonders of the ancient world.\n\nIt is to this city that all four Gospels march. Jesus entered from Bethany on a donkey, fulfilling Zechariah 9:9, while crowds spread palm branches: 'Hosanna to the Son of David!' (Matthew 21:9). He wept over the city that would not receive him (Luke 19:41–44). He taught in the Temple courts, drove out the money changers, and declared himself greater than the Temple. On Thursday evening he instituted the Lord's Supper in an upper room on Mount Zion. He crossed the Kidron Valley and entered Gethsemane, where he prayed with sweat falling like drops of blood until the moment of his arrest. He was tried before Caiaphas in the house on the hill, condemned by Pilate in the Praetorium, and crucified at Golgotha outside the city wall. On the first day of the week the tomb was empty. Forty days of resurrection appearances were followed by the Ascension from the Mount of Olives — 'in a cloud, out of their sight' (Acts 1:9). Ten days later, Pentecost: the Spirit fell in the very city where it all happened, and three thousand were baptized (Acts 2:1–41).\n\nJesus foretold the Temple's destruction with architectural precision: 'Not one stone here will be left on another' (Matthew 24:2). In AD 70 the Roman general Titus fulfilled it exactly — the Temple burned, the walls torn down, over a million dead in the siege. Yet the New Testament looks beyond the earthly city to the heavenly: the New Jerusalem descending from God out of heaven, a city with no temple in it, 'for its temple is the Lord God the Almighty and the Lamb' (Revelation 21:22). He who said 'I am the light of the world' while standing in the Temple treasury is himself the city's eternal light — 'and its lamp is the Lamb' (Revelation 21:23).",
    center:   [31.7767, 35.2345],
    zoom:     14,
    legend: [
      { type: 'dot',    color: '#b00010', label: 'Key NT site' },
      { type: 'dot',    color: '#444',    label: 'OT / historical site' },
      { type: 'swatch', color: 'rgba(180,140,40,0.18)', label: 'Temple Mount platform' },
      { type: 'swatch', color: 'rgba(80,120,200,0.12)', label: 'First-century city walls (approx.)' }
    ],
    render: _renderJerusalem
  }
];

/* ── Timelapse t-values for each map (links panel to time-lapse page) ───── */
var MAP_TL_TIMES = {
  'ancient-near-east':      60,
  'patriarchal-journeys':   60,
  'exodus':                320,
  'conquest':              370,
  'twelve-tribes':         400,
  'judges':                450,
  'david-kingdom':         530,
  'solomon-kingdom':       558,
  'divided-kingdom':       640,
  'invasions':             700,
  'return-exile':          790,
  'intertestamental':      870,
  'holy-land':            1000,
  'paul-journeys':        1055,
  'seven-churches':       1075,
  'jerusalem':            1000
};

/* ── State ───────────────────────────────────────────────────────────────── */
var _leaflet        = null;   // active Leaflet map instance
var _overlays       = [];     // active layer references for cleanup
var _currentMapDef  = null;   // active map config (for reset-view button)
var _legendControl  = null;   // Leaflet control hosting the map legend
var _defaultBook    = null;   // optional default book name for partial refs (e.g. "Revelation")
var _markerIndex    = [];     // { city, marker } for every _cityMarker in the current map
var _currentSiteIdx = -1;     // position in _markerIndex for prev/next navigation
var _activeTab      = 'overview'; // 'overview' | 'sites'

/* ── Era groups (drives nav section headers) ─────────────────────────────── */
var GROUPS = [
  { label: 'The Holy City',         ids: ['jerusalem'] },
  { label: 'The Ancient World',     ids: ['ancient-near-east', 'patriarchal-journeys'] },
  { label: 'Egypt & the Exodus',    ids: ['exodus'] },
  { label: 'Conquest & Settlement', ids: ['conquest', 'twelve-tribes', 'judges'] },
  { label: 'The Monarchy',          ids: ['david-kingdom', 'solomon-kingdom', 'divided-kingdom', 'invasions'] },
  { label: 'Exile & Return',        ids: ['return-exile'] },
  { label: 'Intertestamental',      ids: ['intertestamental'] },
  { label: 'New Testament',         ids: ['holy-land', 'paul-journeys', 'seven-churches'] }
];

/* ── Init ────────────────────────────────────────────────────────────────── */
// INTENT: Entry point for the maps page — builds the map-selector nav from
//   MAPS/GROUPS arrays, wires all controls (tabs, city detail panel, reset
//   button, search), then selects the initial map from location.hash or MAPS[0].
// CHANGE? If you add a MAPS entry, also update GROUPS so it appears in the nav;
//   if you rename a map id, update the location.hash matching at lines 361–365.
//   wireRefLinks(container) is called on city detail panels — if wire.js
//   signature changes, that call silently mis-wires refs.
// VERIFY: Load /maps/ with no hash → first map renders; load /maps/#paul-journeys
//   → Paul's Journeys map loads directly; click a city → detail panel opens.
export function initMapsPage() {
  if (!document.getElementById('maps-container')) return;
  if (!window.L) {
    document.getElementById('maps-map').textContent = 'Map library failed to load. Please check your internet connection.';
    return;
  }
  // Load canonical region geometry first so the first render() can use it; on failure we
  // proceed with _REGIONS=null and every _region() call falls back to its inline coords.
  fetch(_REGIONS_URL)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (doc) {
      if (doc && doc.regions) {
        _REGIONS = {};
        doc.regions.forEach(function (rg) { _REGIONS[rg.id] = rg; });
      }
    })
    .catch(function () { /* fallbacks handle it */ })
    .then(function () { _startMapsPage(); });
}

// ── Desk linking: show a linked reader's chapter places ────────────────────
// desk-frame.js re-dispatches the Desk's bsw-desk-show-places postMessage as
// this window event. Markers land on whichever era map is showing; a chapter
// change replaces the layer.
var _followLayer = null;
function _wireDeskFollow() {
  window.addEventListener('bsw:desk-show-places', function (e) {
    if (!_leaflet || !window.L || !e.detail || !e.detail.ids) return;
    // P17: snap to the era map that fits the linked reader's book (John →
    // NT Palestine) before drawing its chapter places, so multi-era places
    // render in the right historical context.
    if (e.detail.mapId && (!_currentMapDef || _currentMapDef.id !== e.detail.mapId)) {
      var target = MAPS.filter(function (m) { return m.id === e.detail.mapId; })[0];
      if (target) _selectMap(target);
    }
    loadPlaces().then(function () {
      if (!_leaflet) return;
      if (_followLayer) { try { _leaflet.removeLayer(_followLayer); } catch (err) {} _followLayer = null; }
      var group = L.layerGroup();
      var pts = [];
      e.detail.ids.forEach(function (id) {
        var p = getPlace(id);
        if (!p || typeof p.lat !== 'number') return;
        pts.push([p.lat, p.lon]);
        L.circleMarker([p.lat, p.lon], {
          radius: p.region ? 14 : 8, color: '#c0392b', weight: 3,
          fillColor: '#c0392b', fillOpacity: p.region ? 0.08 : 0.2
        }).bindTooltip(escHtml(p.name)).addTo(group);
      });
      if (!pts.length) return;
      group.addTo(_leaflet);
      _followLayer = group;
      if (pts.length === 1) _leaflet.flyTo(pts[0], 9);
      else _leaflet.fitBounds(pts, { padding: [40, 40], maxZoom: 9 });
    });
  });
}

function _startMapsPage() {
  _buildNav();
  _wireDeskFollow();
  _wireDetailClose();
  _wireResetButton();
  _wireTabs();
  _wireSiteNav();
  _wireSiteSearch();
  var hash = location.hash.slice(1);
  var initial = MAPS[0];
  for (var i = 0; i < MAPS.length; i++) {
    if (MAPS[i].id === hash) { initial = MAPS[i]; break; }
  }
  _selectMap(initial);
  _applyFocusParam();
}

// INTENT: Let other pages deep-link the Maps page straight to a coordinate — a Biblepedia place
//   article's "Open in full map" link is /maps/?focus=lat,lon[,zoom]. We fly there and drop a
//   highlight ring so the user lands on the place they came from.
// CHANGE? The link is built in assets/js/biblepedia.js (_renderLocationPanel); keep the param
//   name/order ("focus=lat,lon,zoom") identical there. Runs after _selectMap so _leaflet exists.
// VERIFY: open /maps/?focus=31.7767,35.2345,12 → map flies to Jerusalem with a red ring marker.
function _applyFocusParam() {
  var m = /[?&]focus=([^&#]+)/.exec(location.search);
  if (!m || !_leaflet) return;
  var p = decodeURIComponent(m[1]).split(',').map(parseFloat);
  if (p.length < 2 || isNaN(p[0]) || isNaN(p[1])) return;
  var zoom = (p.length > 2 && !isNaN(p[2])) ? p[2] : 11;
  _leaflet.flyTo([p[0], p[1]], zoom);
  L.circleMarker([p[0], p[1]], { radius: 11, color: '#c0392b', weight: 3, fillOpacity: 0.15 })
    .addTo(_leaflet);
}

function _buildNav() {
  var nav = document.getElementById('maps-nav');
  if (!nav) return;
  var byId = {};
  MAPS.forEach(function (m) { byId[m.id] = m; });
  GROUPS.forEach(function (g) {
    var lbl = document.createElement('div');
    lbl.className   = 'maps-nav-group-label';
    lbl.textContent = g.label;
    nav.appendChild(lbl);
    g.ids.forEach(function (id) {
      var m = byId[id];
      if (!m) return;
      var btn = document.createElement('button');
      btn.className  = 'maps-nav-btn';
      btn.dataset.id = m.id;
      btn.innerHTML  = '<span class="maps-nav-icon">' + m.icon + '</span>' + escHtml(m.label);
      btn.addEventListener('click', function () { _selectMap(m); });
      nav.appendChild(btn);
    });
  });

  // P16: narrow widths (phones, slim desk panels) swap the button column for
  // a dropdown — CSS shows exactly one of the two. Kept in sync by _selectMap.
  var sel = document.createElement('select');
  sel.id = 'maps-nav-select';
  sel.className = 'maps-nav-select';
  sel.setAttribute('aria-label', 'Choose a map');
  GROUPS.forEach(function (g) {
    var og = document.createElement('optgroup');
    og.label = g.label;
    g.ids.forEach(function (id) {
      var m = byId[id];
      if (!m) return;
      var opt = document.createElement('option');
      opt.value = m.id;
      opt.textContent = m.icon + ' ' + m.label;
      og.appendChild(opt);
    });
    sel.appendChild(og);
  });
  sel.addEventListener('change', function () {
    var m = byId[sel.value];
    if (m) _selectMap(m);
  });
  nav.parentNode.insertBefore(sel, nav);
}

function _selectMap(map) {
  _currentMapDef = map;
  _defaultBook   = map.defaultBook || null;

  /* update nav active state */
  document.querySelectorAll('.maps-nav-btn').forEach(function (b) {
    var isActive = b.dataset.id === map.id;
    b.classList.toggle('maps-nav-btn--active', isActive);
    b.setAttribute('aria-current', String(isActive));
  });
  var navSel = document.getElementById('maps-nav-select');
  if (navSel && navSel.value !== map.id) navSel.value = map.id;

  /* update title / sub */
  var titleEl  = document.getElementById('maps-map-title');
  var subEl    = document.getElementById('maps-map-sub');
  var tlChipEl = document.getElementById('maps-tl-chip');
  if (titleEl) titleEl.textContent = map.title;
  if (subEl)   subEl.textContent   = map.sub;
  if (tlChipEl) {
    var tlT = MAP_TL_TIMES[map.id];
    if (tlT != null) {
      tlChipEl.href    = 'timelapse/#t=' + tlT;
      tlChipEl.textContent = '⏱ Time-Lapse';
      tlChipEl.hidden  = false;
    } else {
      tlChipEl.hidden  = true;
    }
  }

  /* populate the always-visible overview panel with clickable scripture refs */
  var overviewEl = document.getElementById('maps-overview');
  if (overviewEl) {
    overviewEl.innerHTML = map.overview
      ? _overviewHtml(map.overview)
      : '<p style="color:var(--color-muted,.888);font-style:italic">No overview available.</p>';
    wireRefLinks(overviewEl);
  }

  /* update URL hash for deep-linking without adding a history entry */
  if (history.replaceState) history.replaceState(null, '', '#' + map.id);

  _hideCityDetail();
  _buildLegend(map.legend);

  /* keep Leaflet alive across switches to avoid blank-tile flash */
  _clearOverlays();
  var container = document.getElementById('maps-map');
  if (!_leaflet) {
    _leaflet = L.map(container, { zoomControl: true, attributionControl: true });
    L.tileLayer(TILE_URL, { maxZoom: 19, attribution: TILE_ATTR }).addTo(_leaflet);
    /* Create the legend overlay control once and keep it across map switches */
    _legendControl = _createLegendControl();
    _legendControl.addTo(_leaflet);
    /* Ensure Leaflet reads the flex-resolved container height, not a cached value */
    _leaflet.invalidateSize();
  }
  _leaflet.setView(map.center, map.zoom);
  map.render(_leaflet);
  /* _markerIndex is now fully populated by _cityMarker calls inside render */
  _setTab('overview');
  _buildSiteList();
}

/* ── Layer management ────────────────────────────────────────────────────── */
function _addLayer(layer) {
  layer.addTo(_leaflet);
  _overlays.push(layer);
  return layer;
}

function _clearOverlays() {
  _overlays.forEach(function (l) { if (_leaflet) _leaflet.removeLayer(l); });
  _overlays = [];
  _markerIndex = [];   /* fresh index for next render pass */
}

/* ── Marker factories ────────────────────────────────────────────────────── */
function _cityMarker(city) {
  var color    = city.capital ? '#b00010' : '#333';
  var size     = city.capital ? 14 : 10;
  var weight   = city.capital ? 2.5 : 2;
  var m = L.circleMarker([city.lat, city.lon], {
    radius:      size / 2,
    fillColor:   color,
    color:       '#fff',
    weight:      weight,
    fillOpacity: 0.92
  });
  m.bindTooltip(city.name, { permanent: false, direction: 'top', offset: [0, -6] });
  m.on('click', function () { _showCityDetail(city); });
  _markerIndex.push({ city: city, marker: m });   /* register in site index */
  return m;
}

function _routeLine(coords, color, dashed) {
  var opts = {
    color:     color,
    weight:    2.5,
    opacity:   0.85,
    lineJoin:  'round',
    lineCap:   'round'
  };
  if (dashed) opts.dashArray = '8 5';
  return L.polyline(coords, opts);
}

/* ── Legend (Leaflet overlay control) ────────────────────────────────────── */
function _createLegendControl() {
  var LegendControl = L.Control.extend({
    onAdd: function () {
      var div = L.DomUtil.create('div', 'maps-legend-control');
      /* Prevent scroll/click on the legend from being captured by the map */
      L.DomEvent.disableClickPropagation(div);
      L.DomEvent.disableScrollPropagation(div);
      return div;
    }
  });
  return new LegendControl({ position: 'topright' });
}

function _buildLegend(items) {
  /* Always keep the old sidebar legend hidden — the Leaflet control is canonical */
  var sidebarLegend = document.getElementById('maps-legend');
  if (sidebarLegend) sidebarLegend.hidden = true;

  if (!_legendControl) return;
  var container = _legendControl.getContainer();
  if (!container) return;

  container.innerHTML = '';
  if (!items || !items.length) {
    container.hidden = true;
    return;
  }
  container.hidden = false;

  var title = document.createElement('p');
  title.className   = 'maps-legend-title';
  title.textContent = 'Legend';
  container.appendChild(title);

  items.forEach(function (item) {
    var row = document.createElement('div');
    row.className = 'maps-legend-item';
    if (item.type === 'swatch') {
      row.innerHTML =
        '<span class="maps-legend-swatch" style="background:' + item.color + ';border-color:rgba(0,0,0,.2)"></span>' +
        escHtml(item.label);
    } else if (item.type === 'line') {
      var border = item.dashed ? 'border-top: 3px dashed ' + item.color : '';
      row.innerHTML =
        '<span class="maps-legend-line" style="background:' + (item.dashed ? 'transparent' : item.color) + ';' + border + '"></span>' +
        escHtml(item.label);
    } else if (item.type === 'dot') {
      row.innerHTML =
        '<svg width="14" height="14" style="flex-shrink:0"><circle cx="7" cy="7" r="5" fill="' +
        item.color + '" stroke="#fff" stroke-width="1.5"/></svg>' + escHtml(item.label);
    }
    container.appendChild(row);
  });

  // D: regions are schematic teaching approximations — note it whenever the legend
  // includes a filled-area (swatch) entry, i.e. the map is showing region boundaries.
  if (items.some(function (it) { return it.type === 'swatch'; })) {
    var note = document.createElement('div');
    note.className = 'maps-legend-note';
    note.textContent = 'Region boundaries are approximate.';
    container.appendChild(note);
  }
}

/* ── Region / border polygon helper ─────────────────────────────────────── */
/* Adds a lightly filled, dashed polygon to show a historical region or empire.
   Placed UNDER city markers (added first, so markers render on top).
   label: optional short name rendered as a permanent div-icon at the centroid.
   color: CSS colour string.  fillOpacity default 0.08.                       */
// INTENT: Chaikin corner-cutting rounds a polygon's hard corners into an organic outline,
//   so the schematic region boxes don't read as rectangles. Two passes (factor 0.25/0.75)
//   keep the shape close to the authored extent while removing the boxy look. Operates on a
//   closed ring; a trailing duplicate-of-first point is dropped so the seam doesn't kink.
// CHANGE? More iterations = rounder + more vertices (2x each pass). If a region is authored
//   with already-detailed coastline vertices, rounding still helps; lower to 1 if it over-softens.
// VERIFY: On the Roman-provinces map the Galilee/Judea/etc. overlays render as rounded blobs,
//   not axis-aligned rectangles.
function _smoothRing(coords, iters) {
  var pts = coords.slice();
  if (pts.length > 1) {
    var f = pts[0], l = pts[pts.length - 1];
    if (f[0] === l[0] && f[1] === l[1]) pts.pop();   /* drop duplicate closing point */
  }
  if (pts.length < 3) return coords;
  iters = iters == null ? 2 : iters;
  for (var k = 0; k < iters; k++) {
    var out = [];
    for (var i = 0; i < pts.length; i++) {
      var a = pts[i], b = pts[(i + 1) % pts.length];
      out.push([a[0] * 0.75 + b[0] * 0.25, a[1] * 0.75 + b[1] * 0.25]);
      out.push([a[0] * 0.25 + b[0] * 0.75, a[1] * 0.25 + b[1] * 0.75]);
    }
    pts = out;
  }
  return pts;
}

// INTENT: Resolve a region's polygon from the canonical regions.json by id, choosing the
//   period whose [fromYear,toYear] window contains `era` (a year, negative=BC) when given,
//   else the era string match, else the first period. Returns null when unavailable so the
//   caller can fall back to its inline coords.
// CHANGE? Period selection: pass a number (year) for time-accurate scenes, or a period.era
//   string. If regions.json schema changes (periods[].coords), update here.
// VERIFY: _regionCoords('tribe-judah') returns a ≥9-point ring on the twelve-tribes map.
function _regionCoords(id, era) {
  if (!_REGIONS) return null;
  var r = _REGIONS[id];
  if (!r || !r.periods || !r.periods.length) return null;
  var p = null;
  if (typeof era === 'number') {
    p = r.periods.filter(function (x) {
      return (x.fromYear == null || era >= x.fromYear) && (x.toYear == null || era <= x.toYear);
    })[0];
  } else if (typeof era === 'string') {
    p = r.periods.filter(function (x) { return x.era === era; })[0];
  }
  p = p || r.periods[0];
  return p && p.coords ? p.coords : null;
}

// _region: draw a region by canonical id (regions.json) with an inline fallback. Prefers the
// shared geometry; `fallback` keeps the map working if regions.json is missing that id.
function _region(id, era, fallback, label, color, fillOpacity, info) {
  var coords = _regionCoords(id, era) || fallback;
  if (!coords) return;
  _addRegion(coords, label, color, fillOpacity, info);
}

// info (optional): a {name/desc/refs/significance} object → makes the region clickable,
// surfacing its detail in the shared city-detail panel (reuses the twelve-tribes pattern).
function _addRegion(coords, label, color, fillOpacity, info) {
  var poly = L.polygon(_smoothRing(coords, 2), {
    color:       color,
    weight:      1,
    fillColor:   color,
    fillOpacity: fillOpacity != null ? fillOpacity : 0.09,
    dashArray:   '5 4',
    interactive: !!info   /* clickable only when it carries detail; else don't steal clicks */
  });
  if (info) {
    poly.bindTooltip(label || info.name || '', { sticky: true, direction: 'center' });
    poly.on('click', function () { _showCityDetail(info); });
  }
  _addLayer(poly);
  if (label) {
    var center = poly.getBounds().getCenter();
    var icon = L.divIcon({
      className: 'maps-region-label',
      html:      '<span>' + escHtml(label) + '</span>',
      iconSize:  [1, 1],   /* avoid Leaflet adding default size */
      iconAnchor:[0, 0]
    });
    _addLayer(L.marker(center, { icon: icon, interactive: false, keyboard: false }));
  }
}

/* ── Overview HTML renderer ──────────────────────────────────────────────── */
function _overviewHtml(text) {
  /* Extract ref spans BEFORE escaping so that HTML-special chars in surrounding
     prose (apostrophes, em-dashes, &c.) do not break the parenthesised-ref regex.
     Each placeholder is replaced back with a safe anchor after the escape pass. */
  function _parseRefs(para) {
    var anchors = [];
    /* Step 1 — pull out every (…) group that looks like one or more Bible refs */
    var withPlaceholders = para.trim().replace(/\(([^)]+)\)/g, function (_, inner) {
      var parts = inner.split(/;\s*/);
      var any = false;
      var chips = parts.map(function (part) {
        part = part.trim();
        /* A full ref starts with a capital (optionally preceded by a leading digit).
           A partial ref like "2:1" or "3:14–22" starts with a digit + colon — only
           linkable when the current map provides a defaultBook. */
        var isFullRef    = /^(?:\d\s+)?[A-Z]/.test(part) && /\d/.test(part);
        var isPartialRef = _defaultBook && /^\d+:\d+/.test(part.trim());
        if (isFullRef || isPartialRef) {
          any = true;
          var resolvedPart = isPartialRef ? (_defaultBook + ' ' + part.trim()) : part;
          var apiRef = resolvedPart.replace(/[–—]/g, '-');
          /* target="_blank" is the fallback when wireRefLinks can't parse the ref */
          return '\x00REF' + anchors.push(
            '<a class="ref maps-overview-ref" data-ref="' + apiRef +
            '" href="' + READER_URL + '?ref=' + encodeURIComponent(apiRef) +
            '" target="_blank" rel="noopener">' + escHtml(part) + '</a>'
          ) + '\x00';
        }
        return '\x00PLAIN' + anchors.push(escHtml(part)) + '\x00';
      });
      return any ? '(' + chips.join('; ') + ')' : '(' + inner + ')';
    });
    /* Step 2 — escape the rest of the prose (safe now that refs are placeholdered) */
    var escaped = escHtml(withPlaceholders);
    /* Step 3 — restore the anchors (they were already built with escHtml parts) */
    return escaped.replace(/\x00(?:REF|PLAIN)(\d+)\x00/g, function (_, i) {
      return anchors[parseInt(i, 10) - 1];
    });
  }
  return text.split(/\n\n+/).map(function (p) {
    return '<p>' + _parseRefs(p) + '</p>';
  }).join('');
}

/* ── City detail panel ───────────────────────────────────────────────────── */

function _showCityDetail(city) {
  var panel  = document.getElementById('maps-city-detail');
  var nameEl = document.getElementById('maps-city-name');
  var descEl = document.getElementById('maps-city-desc');
  var sigEl  = document.getElementById('maps-city-significance');
  var refsEl = document.getElementById('maps-city-refs');
  if (!panel) return;

  if (nameEl) nameEl.textContent = city.name;
  if (descEl) descEl.textContent = city.desc || '';
  if (sigEl) {
    if (city.significance) {
      sigEl.textContent = city.significance;
      sigEl.hidden = false;
    } else {
      sigEl.hidden = true;
    }
  }
  if (refsEl) {
    refsEl.innerHTML = '';
    (city.refs || []).forEach(function (rawRef) {
      /* Expand partial refs like "2:1" or "3:14-22" to "BookName 2:1" using
         the map's defaultBook, so wireRefLinks can parse them correctly. */
      var fullRef = rawRef;
      if (_defaultBook && /^\d+:\d+/.test(rawRef.trim())) {
        fullRef = _defaultBook + ' ' + rawRef.trim();
      }
      var chip = document.createElement('a');
      chip.className = 'ref maps-city-ref-chip';
      chip.setAttribute('data-ref', fullRef);
      /* href + target="_blank" is the navigation fallback; wireRefLinks will
         prefer to open the site modal, but if parseRef fails the link still works */
      chip.href        = READER_URL + '?ref=' + encodeURIComponent(fullRef);
      chip.target      = '_blank';
      chip.rel         = 'noopener';
      chip.textContent = rawRef;  /* display original short form, full ref in data-ref */
      refsEl.appendChild(chip);
    });
    /* Wire hover-preview tooltip + modal; leaves target="_blank" intact as fallback */
    wireRefLinks(refsEl);
  }

  /* Find city in _markerIndex for prev/next navigation */
  _currentSiteIdx = -1;
  for (var j = 0; j < _markerIndex.length; j++) {
    if (_markerIndex[j].city === city) { _currentSiteIdx = j; break; }
  }
  var navEl = document.getElementById('maps-city-nav');
  var posEl = document.getElementById('maps-city-nav-pos');
  if (navEl) navEl.hidden = (_currentSiteIdx < 0 || _markerIndex.length < 2);
  if (posEl && _currentSiteIdx >= 0) {
    posEl.textContent = (_currentSiteIdx + 1) + ' / ' + _markerIndex.length;
  }

  /* Remove any previous city-map chip, then add one for Jerusalem */
  var prevChip = panel.querySelector('.maps-city-map-chip');
  if (prevChip) prevChip.remove();
  if (city.name === 'Jerusalem') {
    var mapChip = document.createElement('a');
    mapChip.className   = 'maps-city-map-chip';
    mapChip.href        = '#jerusalem';
    mapChip.textContent = 'View city map';
    mapChip.addEventListener('click', function (e) {
      e.preventDefault();
      for (var i = 0; i < MAPS.length; i++) {
        if (MAPS[i].id === 'jerusalem') { _selectMap(MAPS[i]); break; }
      }
    });
    /* Insert after the refs div (or after significance if refs absent) */
    var refsEl2 = document.getElementById('maps-city-refs');
    if (refsEl2) refsEl2.insertAdjacentElement('afterend', mapChip);
  }

  /* Study notes — localStorage per map+city */
  var prevNotes = panel.querySelector('.maps-city-notes-wrap');
  if (prevNotes) prevNotes.remove();
  if (_currentMapDef) {
    var noteKey  = 'bsw_map_note_' + _currentMapDef.id + '_' + city.name;
    var noteVal  = localStorage.getItem(noteKey) || '';
    var noteWrap = document.createElement('div');
    noteWrap.className = 'maps-city-notes-wrap';
    var noteToggle = document.createElement('button');
    noteToggle.className   = 'maps-city-notes-btn';
    noteToggle.textContent = noteVal ? 'Note' : 'Add note';
    var noteArea = document.createElement('textarea');
    noteArea.className   = 'maps-city-notes-textarea';
    noteArea.placeholder = 'Your study notes…';
    noteArea.value       = noteVal;
    noteArea.hidden      = !noteVal;   /* auto-expand if a note already exists */
    noteToggle.addEventListener('click', function () {
      noteArea.hidden = !noteArea.hidden;
      if (!noteArea.hidden) noteArea.focus();
    });
    noteArea.addEventListener('input', function () {
      noteToggle.textContent = noteArea.value.trim() ? 'Note' : 'Add note';
    });
    noteArea.addEventListener('blur', function () {
      var v = noteArea.value.trim();
      if (v) {
        localStorage.setItem(noteKey, v);
        _refreshMarkerNote(city, true);
      } else {
        localStorage.removeItem(noteKey);
        _refreshMarkerNote(city, false);
      }
    });
    noteWrap.appendChild(noteToggle);
    noteWrap.appendChild(noteArea);
    /* Append after the last dynamic element in the detail panel */
    panel.appendChild(noteWrap);
  }

  panel.hidden = false;
}

function _hideCityDetail() {
  var panel = document.getElementById('maps-city-detail');
  if (panel) panel.hidden = true;
}

/* Adds/removes a note-dot on the Leaflet marker when note is saved/deleted */
function _refreshMarkerNote(city, hasNote) {
  for (var i = 0; i < _markerIndex.length; i++) {
    if (_markerIndex[i].city === city) {
      var el = _markerIndex[i].marker.getElement();
      if (el) el.classList.toggle('maps-marker-has-note', hasNote);
      break;
    }
  }
}

/* On initial render, decorate markers for cities that already have notes */
function _applyExistingNotes() {
  if (!_currentMapDef) return;
  _markerIndex.forEach(function (entry) {
    var key    = 'bsw_map_note_' + _currentMapDef.id + '_' + entry.city.name;
    var hasNote = !!localStorage.getItem(key);
    var el = entry.marker.getElement();
    if (el) el.classList.toggle('maps-marker-has-note', hasNote);
  });
}

function _wireDetailClose() {
  document.addEventListener('click', function (e) {
    if (e.target && e.target.id === 'maps-city-close') _hideCityDetail();
  });
}

function _wireResetButton() {
  var btn = document.getElementById('maps-reset-view');
  if (!btn) return;
  btn.addEventListener('click', function () {
    if (_leaflet && _currentMapDef) {
      _leaflet.setView(_currentMapDef.center, _currentMapDef.zoom);
    }
  });
}

/* ── Tab switching (Overview ↔ Sites) ────────────────────────────────────── */
function _wireTabs() {
  var btnOverview = document.getElementById('maps-tab-overview');
  var btnSites    = document.getElementById('maps-tab-sites');
  var btnRefs     = document.getElementById('maps-tab-refs');
  if (btnOverview) btnOverview.addEventListener('click', function () { _setTab('overview'); });
  if (btnSites)    btnSites.addEventListener('click',    function () { _setTab('sites'); });
  if (btnRefs)     btnRefs.addEventListener('click',     function () { _setTab('refs'); });
}

function _setTab(tab) {
  _activeTab = tab;
  var overviewEl  = document.getElementById('maps-overview');
  var siteIndexEl = document.getElementById('maps-site-index');
  var refsIndexEl = document.getElementById('maps-refs-index');
  var btnOverview = document.getElementById('maps-tab-overview');
  var btnSites    = document.getElementById('maps-tab-sites');
  var btnRefs     = document.getElementById('maps-tab-refs');
  if (overviewEl)  overviewEl.hidden  = (tab !== 'overview');
  if (siteIndexEl) siteIndexEl.hidden = (tab !== 'sites');
  if (refsIndexEl) refsIndexEl.hidden = (tab !== 'refs');
  if (btnOverview) { btnOverview.classList.toggle('maps-tab--active', tab === 'overview'); btnOverview.setAttribute('aria-selected', String(tab === 'overview')); }
  if (btnSites)    { btnSites.classList.toggle('maps-tab--active',    tab === 'sites');    btnSites.setAttribute('aria-selected',    String(tab === 'sites')); }
  if (btnRefs)     { btnRefs.classList.toggle('maps-tab--active',     tab === 'refs');     btnRefs.setAttribute('aria-selected',     String(tab === 'refs')); }
}

/* ── Site index list (populated after each map render) ───────────────────── */
function _buildSiteList() {
  var listEl  = document.getElementById('maps-site-list');
  var tabEl   = document.getElementById('maps-tab-sites');
  var searchEl = document.getElementById('maps-site-search');
  if (listEl) listEl.innerHTML = '';
  if (searchEl) searchEl.value = '';
  if (tabEl) tabEl.textContent = 'Sites (' + _markerIndex.length + ')';
  /* Decorate markers that already have saved notes for this map */
  _applyExistingNotes();
  /* Build the Refs tab content from the same _markerIndex */
  _buildRefsIndex();
  if (!listEl) return;
  _markerIndex.forEach(function (entry, idx) {
    var item = document.createElement('div');
    item.className = 'maps-site-item';
    item.innerHTML =
      '<div class="maps-site-item-name">' + escHtml(entry.city.name) +
        (entry.city.capital ? ' <span class="maps-site-item-star">★</span>' : '') +
      '</div>' +
      '<div class="maps-site-item-desc">' +
        escHtml((entry.city.desc || '').slice(0, 130)) +
      '</div>';
    item.addEventListener('click', function () {
      _currentSiteIdx = idx;
      if (_leaflet) {
        _leaflet.flyTo(entry.marker.getLatLng(), Math.max(_leaflet.getZoom(), 11),
                       { animate: true, duration: 0.55 });
      }
      _showCityDetail(entry.city);
    });
    listEl.appendChild(item);
  });
}

/* ── Scripture refs index (Refs tab) ─────────────────────────────────────── */
/* Canonical Bible book order for sorting */
var _BOOK_ORDER = [
  'Genesis','Exodus','Leviticus','Numbers','Deuteronomy',
  'Joshua','Judges','Ruth','1 Samuel','2 Samuel',
  '1 Kings','2 Kings','1 Chronicles','2 Chronicles',
  'Ezra','Nehemiah','Esther','Job','Psalms','Proverbs',
  'Ecclesiastes','Song of Solomon','Isaiah','Jeremiah',
  'Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos',
  'Obadiah','Jonah','Micah','Nahum','Habakkuk','Zephaniah',
  'Haggai','Zechariah','Malachi',
  'Matthew','Mark','Luke','John','Acts',
  'Romans','1 Corinthians','2 Corinthians','Galatians',
  'Ephesians','Philippians','Colossians',
  '1 Thessalonians','2 Thessalonians',
  '1 Timothy','2 Timothy','Titus','Philemon',
  'Hebrews','James','1 Peter','2 Peter',
  '1 John','2 John','3 John','Jude','Revelation'
];

function _refBook(ref) {
  /* Extract book name from a ref string like "1 Kings 8:10" or "Matthew 24:2" */
  var m = ref.match(/^(\d\s+)?[A-Z][a-zA-Z ]+(?=\s+\d)/);
  return m ? m[0].trim() : ref;
}

function _refSortKey(ref) {
  var book  = _refBook(ref);
  var bookIdx = _BOOK_ORDER.indexOf(book);
  if (bookIdx < 0) bookIdx = 999;
  /* Extract chapter:verse for secondary sort */
  var cv = ref.replace(book, '').trim(); /* e.g. "8:10" */
  var parts = cv.split(':');
  var ch = parseInt(parts[0]) || 0;
  var vs = parseInt(parts[1]) || 0;
  return bookIdx * 1000000 + ch * 1000 + vs;
}

function _buildRefsIndex() {
  var el = document.getElementById('maps-refs-index');
  if (!el) return;
  el.innerHTML = '';

  /* Collect all refs from all cities, deduplicate */
  var seen = {};
  var allRefs = [];
  _markerIndex.forEach(function (entry) {
    (entry.city.refs || []).forEach(function (ref) {
      if (!seen[ref]) { seen[ref] = true; allRefs.push(ref); }
    });
  });

  if (!allRefs.length) {
    el.innerHTML = '<p class="maps-refs-empty">No scripture references in this map.</p>';
    return;
  }

  /* Sort by canonical Bible order */
  allRefs.sort(function (a, b) { return _refSortKey(a) - _refSortKey(b); });

  /* Group by book for readability */
  var byBook = [];
  var lastBook = null;
  allRefs.forEach(function (ref) {
    var book = _refBook(ref);
    if (book !== lastBook) {
      byBook.push({ book: book, refs: [] });
      lastBook = book;
    }
    byBook[byBook.length - 1].refs.push(ref);
  });

  var countEl = document.createElement('p');
  countEl.className   = 'maps-refs-count';
  countEl.textContent = allRefs.length + ' reference' + (allRefs.length !== 1 ? 's' : '') +
                        ' across ' + byBook.length + ' book' + (byBook.length !== 1 ? 's' : '');
  el.appendChild(countEl);

  byBook.forEach(function (group) {
    var bookEl = document.createElement('div');
    bookEl.className = 'maps-refs-book';
    var labelEl = document.createElement('div');
    labelEl.className   = 'maps-refs-book-label';
    labelEl.textContent = group.book;
    bookEl.appendChild(labelEl);
    var chipsEl = document.createElement('div');
    chipsEl.className = 'maps-refs-chips';
    group.refs.forEach(function (ref) {
      var chip = document.createElement('a');
      chip.className = 'ref maps-refs-chip';
      chip.setAttribute('data-ref', ref);
      chip.textContent = ref;
      chipsEl.appendChild(chip);
    });
    wireRefLinks(chipsEl);
    bookEl.appendChild(chipsEl);
    el.appendChild(bookEl);
  });
}

/* ── Site search filter (wired once on init) ─────────────────────────────── */
function _wireSiteSearch() {
  var input = document.getElementById('maps-site-search');
  if (!input) return;
  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase();
    var listEl = document.getElementById('maps-site-list');
    if (!listEl) return;
    listEl.querySelectorAll('.maps-site-item').forEach(function (el) {
      el.style.display = (q && !el.textContent.toLowerCase().includes(q)) ? 'none' : '';
    });
  });
}

/* ── Prev / Next site navigation ─────────────────────────────────────────── */
function _wireSiteNav() {
  var prevBtn = document.getElementById('maps-city-prev');
  var nextBtn = document.getElementById('maps-city-next');
  if (prevBtn) prevBtn.addEventListener('click', function () { _stepSite(-1); });
  if (nextBtn) nextBtn.addEventListener('click', function () { _stepSite(1); });
}

function _stepSite(dir) {
  if (!_markerIndex.length) return;
  var base = _currentSiteIdx >= 0 ? _currentSiteIdx : (dir > 0 ? -1 : _markerIndex.length);
  var next = ((base + dir) % _markerIndex.length + _markerIndex.length) % _markerIndex.length;
  var entry = _markerIndex[next];
  if (_leaflet) {
    _leaflet.flyTo(entry.marker.getLatLng(), Math.max(_leaflet.getZoom(), 11),
                   { animate: true, duration: 0.55 });
  }
  _showCityDetail(entry.city);
}

/* ═══════════════════════════════════════════════════════════════════════════
   MAP DEFINITIONS
   ═══════════════════════════════════════════════════════════════════════════ */

/* ── 1. Holy Land — Palestine in the time of Jesus ───────────────────────── */
function _renderHolyLand(map) {
  /* Roman Empire — the overarching power controlling all of Palestine c. AD 27–30 */
  _region('empire-rome', 30, [[30.00,33.50],[30.00,37.50],[34.00,37.50],[34.00,33.50]], 'Roman Empire', '#8b0000', 0.04);

  /* Roman administrative provinces / regions c. AD 27–30 */
  _addRegion([[33.30,34.70],[33.30,35.70],[32.55,35.70],[32.55,34.70]], 'Galilee',   '#4a8c3f', 0.09);
  _addRegion([[32.55,34.70],[32.55,35.70],[31.88,35.70],[31.88,34.70]], 'Samaria',   '#9b7000', 0.08);
  _addRegion([[31.88,34.50],[31.88,35.60],[31.00,35.60],[31.00,34.50]], 'Judea',     '#b33c3c', 0.08);
  _addRegion([[31.50,35.60],[31.50,36.40],[32.55,36.40],[32.55,35.60]], 'Perea',     '#5c3d9e', 0.08);
  _addRegion([[32.55,35.60],[32.55,36.60],[33.30,36.60],[33.30,35.60]], 'Decapolis', '#2255aa', 0.07);

  var cities = [
    { name: 'Jerusalem',         lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: 'The city of the great King. Site of the Temple, the Last Supper, Crucifixion, Resurrection, and Pentecost.',
      refs: ['Psalm 48:1', 'Luke 19:41', 'Acts 2:1', 'Revelation 21:2'],
      significance: 'The earthly Jerusalem is a shadow of the New Jerusalem — the city "whose builder and maker is God," the bride of Christ descending from heaven (Hebrews 11:10; Revelation 21:2).' },
    { name: 'Bethlehem',         lat: 31.7054, lon: 35.2024,
      desc: "Birthplace of Jesus, fulfilling Micah's prophecy. Also the city of David, and the home of Ruth and Boaz.",
      refs: ['Micah 5:2', 'Luke 2:4', 'Ruth 1:22'] },
    { name: 'Nazareth',          lat: 32.6996, lon: 35.3035,
      desc: "Jesus grew up here and spent about thirty years in this obscure Galilean town. He read Isaiah 61 in the synagogue and was rejected.",
      refs: ['Luke 4:16', 'Luke 2:51', 'Matthew 2:23'] },
    { name: 'Capernaum',         lat: 32.8823, lon: 35.5753,
      desc: "Jesus's base of ministry in Galilee. Home of Peter and Andrew; site of healings, the calling of Matthew, and the Bread of Life discourse.",
      refs: ['Matthew 4:13', 'Mark 1:21', 'John 6:35'] },
    { name: 'Jericho',           lat: 31.8535, lon: 35.4616,
      desc: "The oldest city in the world. Its walls fell at Israel's shout. Jesus healed blind Bartimaeus here and called Zacchaeus down from a sycamore tree.",
      refs: ['Joshua 6:20', 'Luke 18:35', 'Luke 19:1'] },
    { name: 'Bethany',           lat: 31.7742, lon: 35.2590,
      desc: "Home of Mary, Martha, and Lazarus. Jesus wept here and raised Lazarus four days after his death. The Ascension happened near here.",
      refs: ['John 11:1', 'John 11:35', 'Luke 24:50'],
      significance: 'The raising of Lazarus is the seventh and climactic sign in John — a public preview of the resurrection Jesus himself would accomplish four days later in the same area.' },
    { name: 'Caesarea Philippi', lat: 33.2481, lon: 35.6943,
      desc: "At the foot of Mount Hermon near pagan shrines, Jesus asked his disciples: 'Who do you say I am?' Peter's great confession followed.",
      refs: ['Matthew 16:13', 'Matthew 16:16'] },
    { name: 'Caesarea Maritima', lat: 32.5025, lon: 34.8958,
      desc: "Herod's great port city on the Mediterranean. Peter preached to Cornelius here — the first Gentile converts. Paul was imprisoned here for two years.",
      refs: ['Acts 10:1', 'Acts 23:33', 'Acts 25:6'] },
    { name: 'Samaria (Sebaste)', lat: 32.2781, lon: 35.1981,
      desc: "Capital of the northern kingdom, built by Omri. Fell to Assyria in 722 BC. Later, Jesus passed through the region and met the woman at Jacob's well.",
      refs: ['1 Kings 16:24', '2 Kings 17:6', 'John 4:5'] },
    { name: 'Joppa (Jaffa)',     lat: 32.0560, lon: 34.7544,
      desc: "Ancient port city. Jonah boarded a ship here to flee Tarshish. Peter raised Dorcas here and received the vision of clean and unclean animals.",
      refs: ['Jonah 1:3', 'Acts 9:36', 'Acts 10:9'] },
    { name: 'Cana of Galilee',   lat: 32.7455, lon: 35.3493,
      desc: "Site of Jesus's first miracle — turning water into wine at a wedding banquet, revealing his glory and prompting his disciples' belief.",
      refs: ['John 2:1', 'John 2:11'] },
    { name: 'Tiberias',          lat: 32.7922, lon: 35.5312,
      desc: "City built by Herod Antipas on the western shore of the Sea of Galilee, named for Emperor Tiberius. A sea crossing took Jesus near here.",
      refs: ['John 6:23', 'John 21:1'] },
    { name: 'Emmaus',            lat: 31.8388, lon: 35.0611,
      desc: "Two disciples met the risen Jesus on this road. He opened the Scriptures to them, and they recognized him in the breaking of bread.",
      refs: ['Luke 24:13', 'Luke 24:30'] },
    { name: 'Qumran',            lat: 31.7426, lon: 35.4573,
      desc: "Community on the Dead Sea shore where the Dead Sea Scrolls were hidden in caves — preserving the oldest known OT manuscripts, confirming the biblical text.",
      refs: ['Isaiah 40:3'] },
    { name: 'Hebron',            lat: 31.5327, lon: 35.0957,
      desc: "Abraham bought the cave of Machpelah here to bury Sarah — the first real estate in the promised land. David was first crowned king of Judah here.",
      refs: ['Genesis 23:19', '2 Samuel 2:4'] },
    { name: 'Beersheba',         lat: 31.2518, lon: 34.7915,
      desc: "The southernmost marker of the promised land. 'From Dan to Beersheba.' Abraham dug a well here; Elijah fled here and encountered God under a broom tree.",
      refs: ['Genesis 21:31', '1 Kings 19:3', 'Amos 8:14'] },
    { name: 'Gaza',              lat: 31.5017, lon: 34.4674,
      desc: "Philistine stronghold. Samson was blinded and imprisoned here, then brought down the temple in his death. Philip met the Ethiopian eunuch on the road here.",
      refs: ['Judges 16:21', 'Judges 16:30', 'Acts 8:26'] },
    { name: 'Sychar',            lat: 32.2098, lon: 35.2712,
      desc: "Near Jacob's well in Samaria. Jesus sat here, weary from the journey, and offered a Samaritan woman living water — she became the first evangelist to her city.",
      refs: ['John 4:5', 'John 4:14', 'John 4:39'] },
    { name: 'Dan',               lat: 33.2484, lon: 35.6514,
      desc: "Northernmost city of Israel. Jeroboam erected a golden calf here. The phrase 'from Dan to Beersheba' designated the full extent of the promised land.",
      refs: ['1 Kings 12:29', 'Judges 20:1'] }
  ];
  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 2. Paul's Missionary Journeys ──────────────────────────────────────── */
function _renderPaulJourneys(map) {
  /* Roman Empire — the single political world Paul travels through */
  _addRegion([
    [34.00,11.50],[34.00,42.00],[43.00,42.00],[43.00,11.50],[34.00,11.50]
  ], 'Roman Empire', '#8b0000', 0.04);

  /* Roman provinces — subdivisions of imperial territory c. AD 46–60 */
  _addRegion([[36.00,36.00],[36.00,42.00],[38.50,42.00],[38.50,36.00]], 'Syria & Cilicia', '#9b7000', 0.07);
  _addRegion([[36.00,25.00],[36.00,36.00],[40.50,36.00],[40.50,25.00]], 'Asia & Galatia',  '#2255aa', 0.07);
  _addRegion([[40.50,22.00],[40.50,26.50],[43.00,26.50],[43.00,22.00]], 'Macedonia',        '#b33c3c', 0.07);
  _addRegion([[37.00,21.50],[37.00,23.50],[40.50,23.50],[40.50,21.50]], 'Achaia',           '#4a8c3f', 0.07);
  _addRegion([[34.50,33.00],[34.50,37.00],[36.00,37.00],[36.00,33.00]], 'Syria & Judea',    '#5c3d9e', 0.07);

  /* Routes — lat/lon waypoints */
  var journey1 = [
    COORDS.antioch,  /* Antioch (Syria) */
    [35.12, 33.92],  /* Salamis, Cyprus */
    [34.78, 32.42],  /* Paphos, Cyprus */
    [36.85, 30.70],  /* Perga */
    [37.93, 30.86],  /* Antioch of Pisidia */
    [37.87, 32.48],  /* Iconium (Konya) */
    [37.58, 32.34],  /* Lystra */
    [37.35, 33.40],  /* Derbe */
    [37.58, 32.34],  /* Lystra (return) */
    [37.87, 32.48],  /* Iconium */
    [37.93, 30.86],  /* Antioch of Pisidia */
    [36.85, 30.70],  /* Perga */
    [36.58, 31.00],  /* Attalia */
    COORDS.antioch   /* Antioch (return) */
  ];

  var journey2 = [
    COORDS.antioch,  /* Antioch */
    [37.35, 33.40],  /* Derbe */
    [37.58, 32.34],  /* Lystra */
    COORDS.troas,  /* Troas */
    [40.49, 25.52],  /* Samothrace */
    [40.84, 24.71],  /* Neapolis */
    [41.01, 24.28],  /* Philippi */
    [40.64, 22.94],  /* Thessalonica */
    [40.36, 22.55],  /* Berea */
    COORDS.athens,  /* Athens */
    COORDS.corinth,  /* Corinth */
    COORDS.ephesus,  /* Ephesus */
    COORDS.caesarea,  /* Caesarea Maritima */
    COORDS.jerusalem,  /* Jerusalem */
    COORDS.antioch   /* Antioch */
  ];

  var journey3 = [
    COORDS.antioch,  /* Antioch */
    [38.50, 31.00],  /* Galatia / Phrygia region */
    COORDS.ephesus,  /* Ephesus */
    [40.64, 22.94],  /* Thessalonica */
    COORDS.corinth,  /* Corinth */
    [40.64, 22.94],  /* Macedonia again */
    COORDS.troas,  /* Troas */
    COORDS.miletus,  /* Miletus */
    [36.54, 36.16],  /* Tyre */
    COORDS.caesarea,  /* Caesarea Maritima */
    COORDS.jerusalem   /* Jerusalem */
  ];

  var romeVoyage = [
    COORDS.jerusalem,  /* Jerusalem */
    COORDS.caesarea,  /* Caesarea */
    [36.30, 30.55],  /* Myra */
    [36.89, 27.29],  /* Rhodes (approx sea route) */
    [34.92, 25.30],  /* Crete (Fair Havens) */
    [35.94, 14.38],  /* Malta */
    [37.08, 15.27],  /* Syracuse, Sicily */
    [40.83, 14.25],  /* Puteoli */
    COORDS.rome   /* Rome */
  ];

  _addLayer(_routeLine(journey1,  '#c44d29', false));
  _addLayer(_routeLine(journey2,  '#1a5fa8', false));
  _addLayer(_routeLine(journey3,  '#3d7a4a', false));
  _addLayer(_routeLine(romeVoyage,'#7b5ea7', true));

  var cities = [
    { name: 'Antioch (Syria)', lat: COORDS.antioch[0], lon: COORDS.antioch[1], capital: true,
      desc: 'The first great Gentile church; the sending base for all three missionary journeys. Believers were first called "Christians" here.',
      refs: ['Acts 11:26', 'Acts 13:1', 'Acts 14:27'],
      significance: 'Antioch establishes the missionary pattern that the church has followed ever since: a healthy local church sends workers, the gospel advances, new churches are planted, and the senders receive a report of what God has done.' },
    { name: 'Ephesus',        lat: COORDS.ephesus[0], lon: COORDS.ephesus[1], capital: true,
      desc: "Paul spent three years here — his longest stay. From Ephesus the word of God spread throughout the province of Asia. He wrote 1 Corinthians here.",
      refs: ['Acts 19:10', 'Acts 20:31', 'Ephesians 1:1', 'Revelation 2:1'],
      significance: 'In Revelation 2:1–7 the risen Christ commends Ephesus for doctrinal faithfulness but rebukes it for abandoning its first love — a warning that orthodox belief without love for Christ is a gutted faith.' },
    { name: 'Corinth',        lat: COORDS.corinth[0], lon: COORDS.corinth[1], capital: true,
      desc: "Paul spent 18 months in this cosmopolitan port city. His longest-sustained letters address its troubled church. He wrote Romans from here.",
      refs: ['Acts 18:1', '1 Corinthians 1:1', 'Romans 16:23'] },
    { name: 'Athens',         lat: COORDS.athens[0], lon: COORDS.athens[1],
      desc: "Paul preached on the Areopagus, declaring to philosophers the identity of the unknown God and proclaiming the resurrection — the scandal of the gospel.",
      refs: ['Acts 17:22', 'Acts 17:31'] },
    { name: 'Thessalonica',   lat: 40.64, lon: 22.94,
      desc: "Paul planted a church here in three Sabbaths before being driven out. He wrote 1 & 2 Thessalonians to encourage this persecuted congregation.",
      refs: ['Acts 17:1', '1 Thessalonians 1:6'] },
    { name: 'Philippi',       lat: 41.01, lon: 24.28,
      desc: "The first church planted in Europe, on Paul's second journey. Lydia, a seller of purple, was its first convert. Paul wrote the most joyful of his letters here.",
      refs: ['Acts 16:12', 'Philippians 1:1', 'Acts 16:14'] },
    { name: 'Rome',           lat: COORDS.rome[0], lon: COORDS.rome[1], capital: true,
      desc: "Paul arrived under house arrest and spent two years preaching the kingdom of God to all who came — including members of Caesar's household. He was martyred here.",
      refs: ['Acts 28:30', 'Philippians 4:22', 'Romans 1:1'] },
    { name: 'Troas',          lat: COORDS.troas[0], lon: COORDS.troas[1],
      desc: "Paul received the Macedonian vision here — 'Come over to Macedonia and help us.' The gospel crossed into Europe from this Asian port.",
      refs: ['Acts 16:9', 'Acts 20:6'] },
    { name: 'Caesarea',       lat: COORDS.caesarea[0], lon: COORDS.caesarea[1],
      desc: "Paul was imprisoned here for two years under Felix and Festus before appealing to Caesar, which led to his voyage to Rome.",
      refs: ['Acts 23:33', 'Acts 25:12'] },
    { name: 'Jerusalem',      lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: "Paul returned to Jerusalem after each journey, bringing financial gifts from the Gentile churches. His final visit led to his arrest.",
      refs: ['Acts 21:17', 'Acts 15:2', 'Romans 15:26'] },
    { name: 'Lystra',         lat: 37.58, lon: 32.34,
      desc: "Paul healed a lame man here, was mistaken for Hermes, then stoned and left for dead. Timothy, his closest companion, was from Lystra.",
      refs: ['Acts 14:8', 'Acts 14:19', '2 Timothy 1:5'] },
    { name: 'Paphos',         lat: 34.78, lon: 32.42,
      desc: "Capital of Cyprus. Paul blinded the sorcerer Bar-Jesus here; the proconsul Sergius Paulus believed — the first recorded Gentile convert of the first journey.",
      refs: ['Acts 13:6', 'Acts 13:12'] },
    { name: 'Salamis',        lat: 35.12, lon: 33.92,
      desc: "First port of call on the first missionary journey, where Paul and Barnabas preached in the synagogues of their home island, Cyprus.",
      refs: ['Acts 13:5'] },
    { name: 'Malta',          lat: 35.90, lon: 14.50,
      desc: "Paul was shipwrecked here on the voyage to Rome. He survived a viper bite without harm and healed many on the island over three months.",
      refs: ['Acts 28:1', 'Acts 28:3'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 3. The Exodus Route ─────────────────────────────────────────────────── */
function _renderExodus(map) {
  var route = [
    [30.78, 31.82],  /* Rameses / Goshen (Nile Delta) */
    [30.56, 32.07],  /* Succoth */
    [30.30, 32.35],  /* Etham */
    [29.90, 32.60],  /* Red Sea crossing (Gulf of Suez) */
    [29.30, 32.85],  /* Marah */
    [28.90, 33.10],  /* Elim */
    [28.65, 33.74],  /* Rephidim */
    [28.54, 33.98]   /* Mount Sinai (Jebel Musa, traditional) */
  ];

  var wandering = [
    [28.54, 33.98],  /* Sinai */
    [29.00, 34.60],  /* Wilderness of Paran */
    [30.62, 34.43],  /* Kadesh-barnea */
    [29.80, 34.70],  /* Wilderness wandering arc */
    [28.54, 33.98],  /* Return to Sinai region */
    [29.60, 35.05],  /* Ezion-geber (Aqaba) */
    [30.30, 35.20],  /* Along Transjordan plateau */
    [31.50, 35.70],  /* Plains of Moab */
    [31.85, 35.46]   /* Jericho (Jordan crossing) */
  ];

  _addLayer(_routeLine(route,     '#c44d29', false));
  _addLayer(_routeLine(wandering, '#c44d29', true));

  var cities = [
    { name: 'Rameses (Goshen)',  lat: 30.78, lon: 31.82, capital: true,
      desc: "The city built by Israelite forced labor in Egypt's Nile Delta. Israel set out from here on the night of the first Passover.",
      refs: ['Exodus 1:11', 'Exodus 12:37', 'Genesis 45:10'] },
    { name: 'Red Sea Crossing',  lat: 29.90, lon: 32.60, capital: false,
      desc: "God parted the sea; Israel walked through on dry ground. Pharaoh's army pursuing them was swallowed by the returning waters. The Song of Moses followed.",
      refs: ['Exodus 14:21', 'Exodus 14:28', 'Exodus 15:1'],
      significance: 'Paul calls the sea-crossing a "baptism into Moses" — all passed through water under the cloud, as a type of dying and rising with Christ out of slavery into freedom (1 Corinthians 10:1–2).' },
    { name: 'Marah',             lat: 29.30, lon: 32.85,
      desc: "The first test after the Red Sea: bitter water made sweet when Moses cast a tree into it. God promised: 'I am the LORD who heals you.'",
      refs: ['Exodus 15:23', 'Exodus 15:26'] },
    { name: 'Elim',              lat: 28.90, lon: 33.10,
      desc: "An oasis with twelve springs and seventy palm trees — God's abundant provision after the trial of Marah. A picture of refreshment after testing.",
      refs: ['Exodus 15:27'] },
    { name: 'Rephidim',          lat: 28.65, lon: 33.74,
      desc: "Water flowed from the rock when Moses struck it at God's command. Then the Amalekites attacked — Joshua fought while Moses held up his hands.",
      refs: ['Exodus 17:1', 'Exodus 17:11', '1 Corinthians 10:4'] },
    { name: 'Mount Sinai',       lat: 28.54, lon: 33.98, capital: true,
      desc: "The mountain of God. Israel camped here for nearly a year. The Ten Commandments were given; the covenant was ratified; the Tabernacle was built. The law is given here to a redeemed people.",
      refs: ['Exodus 19:1', 'Exodus 20:1', 'Exodus 40:34', 'Galatians 4:25'],
      significance: 'Paul contrasts Sinai — the covenant of bondage through law — with the Jerusalem above, the covenant of grace through promise: Sinai demands; the gospel gives a new heart (Galatians 4:24–26; Jeremiah 31:33).' },
    { name: 'Kadesh-barnea',     lat: 30.62, lon: 34.43,
      desc: "The gateway to the promised land. The twelve spies returned here with their report. Israel's unbelief condemned them to forty years of wandering in the wilderness.",
      refs: ['Numbers 13:26', 'Numbers 14:33', 'Deuteronomy 2:14'] },
    { name: 'Ezion-geber',       lat: 29.55, lon: 34.95,
      desc: "A stopping point at the northern tip of the Gulf of Aqaba during the wilderness wandering, and later the site of Solomon's fleet.",
      refs: ['Numbers 33:35', '1 Kings 9:26'] },
    { name: 'Mount Nebo',        lat: 31.76, lon: 35.73,
      desc: "Moses climbed here and saw the entire promised land stretched before him — then died, 120 years old, his eyes undimmed. God himself buried him.",
      refs: ['Deuteronomy 34:1', 'Deuteronomy 34:5'] },
    { name: 'Jericho (Jordan)',  lat: 31.85, lon: 35.46,
      desc: "Israel crossed the Jordan on dry ground here — a second Exodus miracle. The conquest of Canaan began with the miraculous fall of Jericho's walls.",
      refs: ['Joshua 3:17', 'Joshua 6:20'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 4. The Divided Kingdom ──────────────────────────────────────────────── */
function _renderDividedKingdom(map) {
  /* Rising Assyrian power in the north — the eventual destroyer of both kingdoms */
  _addRegion([[34.50,36.00],[34.50,46.00],[38.00,46.00],[38.00,36.00]], 'Assyrian Empire (rising power)', '#8b1a1a', 0.05);
  /* Egypt — the other great power dominating the south */
  _region('empire-egypt-core', -700, [[23.00,26.00],[23.00,36.00],[30.50,36.00],[30.50,26.00]], 'Egypt', '#9b7000', 0.06);

  /* Neighbouring nations / regions of the Divided Kingdom period */
  _region('empire-phoenicia', -700, [[33.20,34.60],[33.20,35.55],[34.60,35.55],[34.60,34.60]], 'Phoenicia',    '#1a5fa8', 0.08);
  _region('empire-philistia', -700, [[31.50,34.40],[31.50,34.90],[31.88,34.90],[31.88,34.40]], 'Philistia',    '#7b5ea7', 0.09);
  _region('empire-aram-damascus', -800, [[33.20,35.55],[33.20,37.00],[34.60,37.00],[34.60,35.55]], 'Aram-Damascus','#c44d29', 0.08);
  _addRegion([[31.00,35.55],[31.00,36.40],[31.88,36.40],[31.88,35.55]], 'Moab',         '#9b7000', 0.09);
  _addRegion([[29.80,35.00],[29.80,36.40],[31.00,36.40],[31.00,35.00]], 'Edom',         '#8b1a1a', 0.08);
  _addRegion([[31.88,35.55],[31.88,36.40],[32.55,36.40],[32.55,35.55]], 'Ammon',        '#3d7a4a', 0.08);

  /* Approximate polygon for northern Israel */
  var israelPolygon = [
    [33.25, 35.20],
    [33.20, 36.00],
    [32.55, 36.45],
    [32.00, 35.72],
    [31.88, 35.40],
    [32.10, 35.10],
    [32.55, 34.92],
    [33.10, 34.95],
    [33.25, 35.20]
  ];

  /* Approximate polygon for southern Judah */
  var judahPolygon = [
    [31.88, 35.40],
    [32.00, 35.72],
    [31.55, 35.55],
    [31.20, 35.22],
    [31.00, 35.05],
    [30.62, 34.43],
    [31.22, 34.83],
    [31.88, 35.40]
  ];

  _addLayer(L.polygon(israelPolygon, {
    color:       '#1a5fa8',
    weight:      1.5,
    fillColor:   '#64a0dc',
    fillOpacity: 0.28,
    dashArray:   '5 3'
  }));

  _addLayer(L.polygon(judahPolygon, {
    color:       '#9b7000',
    weight:      1.5,
    fillColor:   '#d2aa50',
    fillOpacity: 0.28,
    dashArray:   '5 3'
  }));

  var cities = [
    { name: 'Samaria',           lat: 32.278, lon: 35.198, capital: true,
      desc: "Capital of the northern kingdom of Israel, built by Omri. Site of Ahab and Jezebel's idolatry. Fell to Assyrian king Sargon II in 722 BC — Israel's 200-year kingdom ends.",
      refs: ['1 Kings 16:24', '2 Kings 17:6', 'Amos 3:12'] },
    { name: 'Jerusalem',         lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: "Capital of the southern kingdom of Judah, the city of David and the site of the Temple. Survived Assyria's siege (701 BC) but fell to Babylon in 586 BC.",
      refs: ['2 Samuel 5:7', '1 Kings 14:21', '2 Kings 25:9'] },
    { name: 'Dan',               lat: 33.248, lon: 35.651,
      desc: "Jeroboam placed a golden calf here to stop Israel from going to Jerusalem to worship — 'These are your gods, O Israel, who brought you up out of Egypt.'",
      refs: ['1 Kings 12:28', '1 Kings 12:29'] },
    { name: 'Bethel',            lat: 31.927, lon: 35.224,
      desc: "The second golden calf shrine of Jeroboam. Condemned by Amos as 'Beth Aven' (house of wickedness). The old site of Jacob's vision became a center of apostate worship.",
      refs: ['1 Kings 12:29', 'Amos 4:4', 'Amos 5:5'],
      significance: 'Jacob named it "house of God" after seeing the ladder between earth and heaven. Jesus declared himself the true Bethel — "the ladder" by which heaven and earth are now joined (John 1:51).' },
    { name: 'Shechem',           lat: 32.199, lon: 35.283,
      desc: "Jeroboam made this his first capital and the site of the fateful assembly where he led the northern tribes in revolt against Rehoboam.",
      refs: ['1 Kings 12:1', '1 Kings 12:16', 'Genesis 34:1'] },
    { name: 'Megiddo',           lat: 32.588, lon: 35.185,
      desc: "Fortified city guarding the Jezreel Valley pass. Site of many decisive battles in OT history. Its name gives us 'Armageddon' (Har Megiddo — mountain of Megiddo).",
      refs: ['Judges 5:19', '2 Kings 23:29', 'Revelation 16:16'] },
    { name: 'Jezreel',           lat: 32.457, lon: 35.306,
      desc: "Ahab's palace and Naboth's vineyard — the scene of Jezebel's murder of Naboth and Elijah's judgment prophecy. Jehu executed the dynasty of Omri here.",
      refs: ['1 Kings 21:1', '2 Kings 9:30'] },
    { name: 'Tirzah',            lat: 32.337, lon: 35.348,
      desc: "First capital of the northern kingdom before Samaria was built by Omri in 885 BC. Praised for its beauty in the Song of Solomon.",
      refs: ['1 Kings 15:33', 'Song of Solomon 6:4'] },
    { name: 'Beersheba',         lat: 31.252, lon: 34.792,
      desc: "Southern boundary of Judah. The prophets condemned Israel for making it a pilgrimage site rather than worshiping God rightly in Jerusalem.",
      refs: ['Amos 5:5', '2 Samuel 24:7'] },
    { name: 'Lachish',           lat: 31.560, lon: 34.847,
      desc: "Second-most-important city of Judah. Sennacherib's massive siege of Lachish is depicted in detailed relief sculptures found in his palace at Nineveh.",
      refs: ['2 Kings 18:14', '2 Chronicles 32:9', 'Micah 1:13'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 5. The Ancient Near East ────────────────────────────────────────────── */
function _renderAncientNearEast(map) {
  var cities = [
    { name: 'Memphis',          lat: 29.849, lon: 31.250, capital: true,
      desc: "Ancient capital of Lower Egypt. Center of Egyptian power during the Patriarchal period and the Exodus. Isaiah prophesied its desolation.",
      refs: ['Isaiah 19:13', 'Jeremiah 46:14', 'Hosea 9:6'] },
    { name: 'Thebes (No-Amon)', lat: 25.687, lon: 32.640, capital: true,
      desc: "Capital of Upper Egypt, known as No-Amon in the OT. A great center of worship of Amun-Ra. Nahum invoked its sack as a warning to Nineveh.",
      refs: ['Nahum 3:8', 'Jeremiah 46:25'] },
    { name: 'Goshen',           lat: 30.780, lon: 31.820,
      desc: "The fertile Nile Delta region where Israel lived for 430 years, from Joseph's invitation to the night of the Exodus.",
      refs: ['Genesis 45:10', 'Exodus 8:22', 'Exodus 12:37'] },
    { name: 'Jerusalem',        lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: "Center of Israel's covenant worship. The Temple stood here from Solomon (966 BC) to Nebuchadnezzar's destruction (586 BC).",
      refs: ['Psalm 48:2', '2 Samuel 5:7', '1 Kings 8:13'] },
    { name: 'Damascus',         lat: COORDS.damascus[0], lon: COORDS.damascus[1], capital: true,
      desc: "Capital of the Aramean kingdom. A perpetual rival and ally of Israel. Paul was converted on the road here; Elisha sent Naaman here to be healed.",
      refs: ['2 Samuel 8:6', 'Amos 1:3', 'Acts 9:2', '2 Kings 5:1'] },
    { name: 'Sidon',            lat: 33.564, lon: 35.371,
      desc: "Leading Phoenician city, older than Tyre. Jezebel was a Sidonian princess. Elijah fled to Zarephath, near Sidon, and was sustained by a widow.",
      refs: ['1 Kings 17:9', 'Matthew 15:21', '1 Kings 16:31'] },
    { name: 'Tyre',             lat: 33.271, lon: 35.196,
      desc: "Premier Phoenician port. Hiram of Tyre provided cedar and craftsmen for Solomon's Temple. Ezekiel's longest oracle against a foreign nation targets Tyre.",
      refs: ['1 Kings 5:1', 'Ezekiel 28:1', 'Amos 1:9'] },
    { name: 'Nineveh',         lat: COORDS.nineveh[0], lon: COORDS.nineveh[1], capital: true,
      desc: "Capital of the Assyrian empire at its height. God sent Jonah here with a message of repentance — they repented. Nahum prophesied its destruction in 612 BC.",
      refs: ['Jonah 3:3', 'Nahum 1:1', 'Zephaniah 2:13'] },
    { name: 'Babylon',          lat: COORDS.babylon[0], lon: COORDS.babylon[1], capital: true,
      desc: "Capital of Nebuchadnezzar's empire. Jerusalem fell to him in 586 BC; the exiles were brought here. Daniel served in its court. Revelation uses it as a symbol of all godless empire.",
      refs: ['Daniel 1:1', 'Psalm 137:1', 'Isaiah 13:19', 'Revelation 17:5'],
      significance: 'Babylon becomes Scripture\'s symbol for all organized human rebellion against God — from the Tower of Babel to "Babylon the Great" of Revelation 17–18, the world-system that persecutes the saints until the Lamb overcomes.' },
    { name: 'Ur of the Chaldeans', lat: 30.963, lon: 46.104,
      desc: "Abraham's homeland in southern Mesopotamia — a sophisticated urban center. God called him out of this world to go to an unknown land, trusting only the promise.",
      refs: ['Genesis 11:31', 'Acts 7:2', 'Hebrews 11:8'],
      significance: "God's call to Abraham from Ur is the beginning of the gospel — the promise of blessing for all nations that Paul identifies as the gospel preached in advance, fulfilled in Christ (Galatians 3:8)." },
    { name: 'Susa',             lat: 32.189, lon: 48.255, capital: true,
      desc: "Winter capital of the Persian empire. Esther and Mordecai lived here under Xerxes. Nehemiah served here as cupbearer before returning to rebuild Jerusalem.",
      refs: ['Esther 1:2', 'Nehemiah 1:1', 'Daniel 8:2'] },
    { name: 'Haran',            lat: COORDS.haran[0], lon: COORDS.haran[1],
      desc: "Abraham's family stopped here after leaving Ur; Terah died here. Jacob fled here from Esau and served Laban for twenty years. A major Assyrian trade center.",
      refs: ['Genesis 11:31', 'Genesis 28:10', 'Acts 7:4'] },
    { name: 'Carchemish',       lat: COORDS.carchemish[0], lon: COORDS.carchemish[1],
      desc: "At this great bend of the Euphrates, Nebuchadnezzar defeated the Egyptian army in 605 BC — the decisive battle that began the Babylonian era and the first deportation from Judah.",
      refs: ['2 Chronicles 35:20', 'Jeremiah 46:2', 'Daniel 1:1'] },
    { name: 'Persepolis',       lat: 29.935, lon: 52.891, capital: true,
      desc: "Ceremonial capital of the Achaemenid Persian empire. Built by Darius and Xerxes (Ahasuerus of Esther). Cyrus, Darius, and Artaxerxes — the kings of the return from exile — ruled from Persia.",
      refs: ['Ezra 1:1', 'Ezra 6:1', 'Ezra 7:1'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 6. Journeys of the Patriarchs ──────────────────────────────────────── */
function _renderPatriarchalJourneys(map) {
  /* Abraham: Ur → Haran → Shechem → Bethel → Egypt → Hebron → Moriah → Beersheba */
  var abrahamRoute = [
    [30.963, 46.104],  /* Ur of the Chaldeans */
    COORDS.haran,  /* Haran — family stops; Terah dies */
    [32.199, 35.283],  /* Shechem — first altar in Canaan (Gen 12:6) */
    [31.927, 35.224],  /* Bethel — second altar */
    [30.780, 31.820],  /* Egypt — famine journey */
    [31.533, 35.096],  /* Hebron — chief residence; Machpelah burial cave */
    COORDS.jerusalem,  /* Moriah — binding of Isaac (2 Chr 3:1) */
    [31.252, 34.792]   /* Beersheba — covenant with Abimelech */
  ];

  /* Jacob: Beersheba → Bethel → Haran → Mahanaim / Peniel → Shechem → Egypt */
  var jacobRoute = [
    [31.252, 34.792],  /* Beersheba — flees Esau */
    [31.927, 35.224],  /* Bethel — Jacob's ladder; God reaffirms covenant */
    COORDS.haran,  /* Haran — serves Laban twenty years */
    [32.190, 35.750],  /* Mahanaim — angels meet Jacob returning */
    [32.170, 35.600],  /* Peniel — wrestles with God; receives name Israel */
    [32.199, 35.283],  /* Shechem — settles briefly */
    [31.927, 35.224],  /* Bethel — God reconfirms covenant (Gen 35) */
    [31.533, 35.096],  /* Hebron — Isaac's home; Jacob based here */
    [30.780, 31.820]   /* Egypt — reunites with Joseph */
  ];

  /* Joseph: sold at Dothan → carried by traders down to Egypt */
  var josephRoute = [
    [32.420, 35.220],  /* Dothan — sold by brothers for twenty pieces of silver */
    [31.500, 35.000],  /* caravan route south through Canaan */
    [31.000, 34.800],  /* near Gaza / entry to Egypt */
    [30.780, 31.820]   /* Egypt — Potiphar's house, prison, Pharaoh's court */
  ];

  _addLayer(_routeLine(abrahamRoute, '#c44d29', false));
  _addLayer(_routeLine(jacobRoute,   '#1a5fa8', false));
  _addLayer(_routeLine(josephRoute,  '#3d7a4a', true));

  var cities = [
    { name: 'Ur of the Chaldeans', lat: 30.963, lon: 46.104, capital: true,
      desc: "Abraham's homeland — a sophisticated Sumerian city-state on the lower Euphrates. God called him out with no destination disclosed, only a promise. He obeyed without knowing where he was going (Heb 11:8).",
      refs: ['Genesis 11:31', 'Acts 7:2', 'Hebrews 11:8'],
      significance: 'Abraham "went out, not knowing where he was going" — the model of saving faith: forward movement on the word of God alone, with no visible guarantee. The church still walks the same road (Hebrews 11:8–10).' },
    { name: 'Haran (Paddan-Aram)', lat: COORDS.haran[0], lon: COORDS.haran[1],
      desc: "The family stopped here after leaving Ur; Terah died at 205. Abraham departed at 75. Jacob later fled here to escape Esau, served Laban twenty years, and built his family — the twelve sons who became the tribes of Israel.",
      refs: ['Genesis 11:31', 'Genesis 12:4', 'Genesis 28:10', 'Genesis 29:20'] },
    { name: 'Shechem', lat: 32.199, lon: 35.283,
      desc: "Abraham's first stop in Canaan. God appeared: 'To your offspring I will give this land.' He built his first altar here. Jacob later purchased land here and dug a well; Jesus spoke with a Samaritan woman at that very well.",
      refs: ['Genesis 12:6', 'Genesis 33:18', 'John 4:5'] },
    { name: 'Bethel', lat: 31.927, lon: 35.224,
      desc: "Abraham built his second altar here. Jacob sleeping here saw a ladder reaching to heaven with angels ascending and descending — God stood at the top and promised the land. Jacob named it 'Beth-El' (house of God) and vowed to return.",
      refs: ['Genesis 12:8', 'Genesis 28:12', 'Genesis 35:1'] },
    { name: 'Egypt (Goshen)', lat: 30.780, lon: 31.820,
      desc: "Abraham fled a famine here. Joseph was sold into slavery in Egypt, rose to second-in-command, and invited his family during the great famine. Jacob's family of 70 entered; 430 years later they left as a nation of millions under Moses.",
      refs: ['Genesis 12:10', 'Genesis 41:41', 'Genesis 46:6', 'Exodus 12:40'] },
    { name: 'Hebron', lat: 31.533, lon: 35.096, capital: true,
      desc: "Abraham's main home in Canaan. He purchased the cave of Machpelah here to bury Sarah — Israel's first legal title to the promised land. All three patriarchs and their wives (except Rachel) are buried here.",
      refs: ['Genesis 13:18', 'Genesis 23:19', 'Genesis 49:31'] },
    { name: 'Moriah (Jerusalem)', lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1],
      desc: "God commanded Abraham to sacrifice Isaac on 'one of the mountains of Moriah.' As the knife was raised, the Angel of the LORD provided a ram caught in a thicket — a vivid type of Christ's substitution. 2 Chronicles 3:1 identifies Moriah as the site of Solomon's Temple.",
      refs: ['Genesis 22:2', 'Genesis 22:13', '2 Chronicles 3:1', 'John 1:29'],
      significance: '"God will provide for himself the lamb" (Genesis 22:8) — a word Abraham spoke in faith that God fulfilled two thousand years later on the same mountain, when he did not spare his own Son but gave him up for us all.' },
    { name: 'Beersheba', lat: 31.252, lon: 34.792,
      desc: "Abraham dug a well here and covenanted with Abimelech, naming the place 'well of the oath.' Isaac settled here after the binding. Jacob saw God in a vision here before descending to Egypt. It marked the southernmost boundary of the promised land.",
      refs: ['Genesis 21:31', 'Genesis 26:23', 'Genesis 46:1'] },
    { name: 'Dothan', lat: 32.420, lon: 35.220,
      desc: "Joseph found his brothers here pasturing flocks. They stripped him of his coat, cast him into an empty cistern, then sold him to an Ishmaelite caravan for twenty pieces of silver. What they intended for evil, God intended for good.",
      refs: ['Genesis 37:17', 'Genesis 37:28', 'Genesis 50:20'] },
    { name: 'Peniel', lat: 32.170, lon: 35.600,
      desc: "On the night before facing Esau and his 400 men, Jacob wrestled alone with a divine Man until daybreak. His hip was put out of socket, but he refused to let go: 'I will not let you go unless you bless me.' He received the name Israel — 'one who strives with God' — and walked away limping.",
      refs: ['Genesis 32:24', 'Genesis 32:28', 'Hosea 12:4'] },
    { name: 'Mahanaim', lat: 32.190, lon: 35.750,
      desc: "Angels of God met Jacob here as he returned from Haran; he named the place 'two camps.' Later David fled to Mahanaim — the city that sheltered the king in his darkest hour during Absalom's revolt.",
      refs: ['Genesis 32:2', '2 Samuel 17:24'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 7. Conquest of Canaan ───────────────────────────────────────────────── */
function _renderConquest(map) {
  /* Land of Canaan — the overarching pre-conquest territory Israel was promised */
  _region('empire-canaan-states', -1400, [[30.50,34.20],[30.50,36.00],[33.30,36.00],[33.30,34.20]], 'Land of Canaan', '#9b7000', 0.05);

  /* Canaanite city-state regions and neighbours before the conquest */
  _addRegion([[31.50,34.40],[31.50,34.90],[32.55,34.90],[32.55,34.40]], 'Philistine plain',  '#7b5ea7', 0.08);
  _addRegion([[31.88,35.40],[31.88,36.00],[32.55,36.00],[32.55,35.40]], 'Jordan Valley',     '#2255aa', 0.07);
  _addRegion([[32.55,35.00],[32.55,36.00],[33.20,36.00],[33.20,35.00]], "Hazor's domain",    '#b33c3c', 0.07);
  _addRegion([[31.00,35.00],[31.00,35.55],[31.88,35.55],[31.88,35.00]], 'Jebusite highlands','#9b7000', 0.08);

  /* Southern campaign: base at Gilgal → sweeping south through Canaanite cities */
  var southernCampaign = [
    [31.875, 35.440],  /* Gilgal — base camp east of Jericho */
    [31.854, 35.462],  /* Jericho — walls fell on the seventh day */
    [31.920, 35.280],  /* Ai — ambush after Achan's sin is dealt with */
    [31.836, 35.171],  /* Gibeon — sun stands still; five-king coalition routed */
    [31.650, 34.950],  /* Makkedah — five kings killed in the cave */
    [31.560, 34.847],  /* Lachish — taken in one day */
    [31.533, 35.096],  /* Hebron — Anakite city; given to Caleb */
    [31.390, 34.960]   /* Debir — final southern objective */
  ];

  /* Northern campaign: from Gilgal north to ambush coalition at Waters of Merom */
  var northernCampaign = [
    [31.875, 35.440],  /* Gilgal — departure */
    [32.057, 35.287],  /* Shiloh / central highlands */
    [32.588, 35.185],  /* Jezreel Valley crossing */
    [33.000, 35.550],  /* Waters of Merom — sudden attack on northern coalition */
    [33.017, 35.568]   /* Hazor — burned; 'head of all those kingdoms' */
  ];

  _addLayer(_routeLine(southernCampaign, '#c44d29', false));
  _addLayer(_routeLine(northernCampaign, '#1a5fa8', false));

  var sites = [
    { name: 'Gilgal (base camp)', lat: 31.875, lon: 35.440, capital: true,
      desc: "Israel's base after crossing the Jordan on dry ground. Twelve memorial stones were set up here. The reproach of Egypt was 'rolled away' through circumcision; the first Passover in Canaan was celebrated. Joshua returned after every campaign.",
      refs: ['Joshua 4:19', 'Joshua 5:9', 'Joshua 5:10'] },
    { name: 'Jericho', lat: 31.854, lon: 35.462, capital: true,
      desc: "The first city taken. Israel marched around it once daily for six days, seven times on the seventh, then shouted — and the walls collapsed flat. Only Rahab's household was spared. The city was placed under the ban; Achan hid some plunder and brought defeat at Ai.",
      refs: ['Joshua 6:20', 'Joshua 6:25', 'Hebrews 11:30'],
      significance: 'Rahab hung a scarlet cord in her window — the agreed sign of salvation when Israel came. This thread of red, marking the saved household while judgment fell on the rest, is one of the richest pictures of the blood of Christ in the entire Old Testament.' },
    { name: 'Ai', lat: 31.920, lon: 35.280,
      desc: "After the disaster of the first assault (due to Achan's sin), Joshua executed a masterful ambush: half his force feigned retreat to draw the garrison out while the other half entered from behind and burned the city. 12,000 died.",
      refs: ['Joshua 7:4', 'Joshua 8:1', 'Joshua 8:28'] },
    { name: 'Gibeon', lat: 31.836, lon: 35.171,
      desc: "The Gibeonites secured a peace treaty by deception. Joshua honored it. When five kings besieged Gibeon, Joshua marched all night from Gilgal — and the sun stood still for a full day until the battle was complete. 'There has been no day like it before or since' (Josh 10:14).",
      refs: ['Joshua 9:15', 'Joshua 10:12', 'Joshua 10:13'] },
    { name: 'Lachish', lat: 31.560, lon: 34.847,
      desc: "Taken in one day — the king of Gezer who came to its aid was also destroyed. A major Canaanite fortress. Archaeological excavation reveals a massive destruction layer consistent with the Conquest period.",
      refs: ['Joshua 10:31', 'Joshua 10:32'] },
    { name: 'Hebron', lat: 31.533, lon: 35.096,
      desc: "Caleb, now 85, claimed Hebron as his personal inheritance — fulfilling Moses's promise made when Caleb alone, with Joshua, gave a faithful report of the land forty-five years earlier. He drove out the three Anakim sons.",
      refs: ['Joshua 14:13', 'Joshua 15:13', 'Numbers 13:30'] },
    { name: 'Hazor', lat: 33.017, lon: 35.568, capital: true,
      desc: "Largest Canaanite city-state, 'formerly the head of all those kingdoms.' Joshua burned it — the only northern city explicitly burned. Excavations by Yigael Yadin confirmed a massive 13th-century BC destruction layer, with a Solomonic rebuilding above.",
      refs: ['Joshua 11:10', 'Joshua 11:13', 'Judges 4:2'] },
    { name: 'Waters of Merom', lat: 33.000, lon: 35.550,
      desc: "The northern coalition — kings from Hazor to Mount Hermon — assembled here with horses and chariots 'as numerous as the sand.' Joshua attacked suddenly; Israel hamstrung the horses and burned the chariots. Victory came by trusting God's word: 'Do not be afraid' (Josh 11:6).",
      refs: ['Joshua 11:5', 'Joshua 11:6', 'Joshua 11:7'] },
    { name: 'Shiloh', lat: 32.057, lon: 35.287,
      desc: "After the major campaigns, the whole congregation assembled at Shiloh in Ephraim. The Tabernacle was set up here; the land was formally divided among the tribes. Shiloh remained Israel's worship center for ~300 years.",
      refs: ['Joshua 18:1', 'Joshua 19:51', 'Psalm 78:60'] }
  ];

  sites.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 8. Twelve Tribes of Israel ─────────────────────────────────────────── */
function _renderTwelveTribes(map) {
  /* Approximate tribal boundaries from Joshua 13–21.
     Exact borders are debated; polygons show general allotment regions.
     Click any territory or reference city for info.                    */

  /*
   * Tribal boundary coordinates — redesigned to eliminate overlaps.
   * Key shared-edge lat/lon spine (west of Jordan):
   *   Lat 31.88  — Judah / Benjamin / Dan-orig south boundary
   *   Lat 32.00  — Benjamin north / Ephraim south
   *   Lat 32.55  — Ephraim north / W.Manasseh south / Issachar south
   *   Lat 32.75  — W.Manasseh north / Issachar north / Galilee south
   *   Lat 33.00  — Lower Galilee (Zebulun) north / Upper Galilee south
   *   Lat 33.30  — Upper Galilee (Naphtali/Asher) north / Dan-north south
   *   Lon 34.65  — Mediterranean coast
   *   Lon 34.90  — Dan-orig east / Ephraim west / W.Manasseh west coast-end
   *   Lon 35.10  — Central ridge (Benjamin west, Zebulun west, W.Manasseh east)
   *   Lon 35.55  — Jordan River west bank / Issachar east / Naphtali east
   *   Lon 35.65  — Jordan east bank (Transjordan tribes west edge)
   */
  var tribes = [
    /* ── West of Jordan ── */

    /* JUDAH — large southern tribe from Jerusalem to the Negev */
    { name: 'Judah', fillColor: '#b33c3c', fillOpacity: 0.28, color: '#b33c3c',
      coords: [
        [31.88, 34.90], /* NW — shared with Dan SW                    */
        [31.88, 35.10], /* N  — shared with Benjamin SW                */
        [31.88, 35.40], /* NE — shared with Benjamin SE                */
        [31.55, 35.55], /* E  — Dead Sea western shore (shared Reuben) */
        [31.10, 35.42], /* SE — south of Dead Sea                      */
        [30.75, 34.80], /* S  — Negev                                  */
        [30.75, 34.00], /* SW — Brook of Egypt                         */
        [31.55, 34.65], /* W  — southern coast                         */
        [31.88, 34.90]  /* close                                       */
      ],
      desc: 'Largest tribe; includes Jerusalem, Bethlehem, and Hebron. "The scepter shall not depart from Judah … until Shiloh comes" (Gen 49:10). From Judah came David, and ultimately Jesus the Messiah, the Lion of the tribe of Judah.',
      refs: ['Joshua 15:1', 'Genesis 49:10', 'Revelation 5:5'],
      significance: 'The scepter that "shall not depart from Judah until Shiloh comes" (Genesis 49:10) finds its fulfillment in Jesus — the Lion of the tribe of Judah who alone is worthy to open the scroll of history (Revelation 5:5).' },

    /* SIMEON — allotted within Judah; intentional nested overlap */
    { name: 'Simeon', fillColor: '#c9921a', fillOpacity: 0.28, color: '#c9921a',
      coords: [
        [31.30, 34.90], [31.15, 35.10], [30.90, 35.10],
        [30.75, 34.80], [30.75, 34.40], [31.10, 34.35],
        [31.30, 34.90]
      ],
      desc: "Allotted within Judah's territory in the far south around Beersheba. Jacob prophesied they would be 'scattered in Israel' (Gen 49:7). As Judah grew powerful, Simeon was absorbed into it — they had no independent destiny.",
      refs: ['Joshua 19:1', 'Genesis 49:7', '1 Chronicles 4:24'] },

    /* BENJAMIN — narrow strip between Judah and Ephraim; Jerusalem on its southern edge */
    { name: 'Benjamin', fillColor: '#4a8c3f', fillOpacity: 0.28, color: '#4a8c3f',
      coords: [
        [32.00, 35.10], /* NW — shared with Ephraim SW                */
        [32.00, 35.40], /* NE — shared with Ephraim SE                */
        [31.88, 35.40], /* SE — shared with Judah NE                  */
        [31.88, 35.10], /* SW — shared with Judah N                   */
        [32.00, 35.10]  /* close                                      */
      ],
      desc: 'Small but strategically placed between Ephraim and Judah. Jerusalem sat on its border. Saul, the first king of Israel, was a Benjaminite — as was Paul the apostle.',
      refs: ['Joshua 18:11', 'Judges 20:4', 'Romans 11:1'] },

    /* DAN (original) — coastal/Shephelah strip west of Benjamin+Ephraim */
    { name: 'Dan (original)', fillColor: '#cc5522', fillOpacity: 0.28, color: '#cc5522',
      coords: [
        [32.55, 34.90], /* NE — shared with W.Manasseh SW / Ephraim NW */
        [32.00, 34.90], /* E  — shared with Ephraim W / Benjamin NW     */
        [31.88, 34.90], /* SE — shared with Judah NW                    */
        [31.88, 34.65], /* S  — coast, shared with Judah W              */
        [32.55, 34.65], /* N  — coast, shared with W.Manasseh W         */
        [32.55, 34.90]  /* close                                        */
      ],
      desc: "Originally allotted a coastal strip west of Benjamin and Ephraim. Dan was unable to conquer their territory — 'the Amorites pressed the Danites back into the hill country.' Most of the tribe migrated north to Laish (renamed Dan).",
      refs: ['Joshua 19:40', 'Judges 1:34', 'Judges 13:2'] },

    /* EPHRAIM — central highlands north of Benjamin */
    { name: 'Ephraim', fillColor: '#2255aa', fillOpacity: 0.28, color: '#2255aa',
      coords: [
        [32.55, 35.55], /* NE — shared with W.Manasseh SE / Issachar SW */
        [32.55, 34.90], /* NW — shared with Dan NE / W.Manasseh SW      */
        [32.00, 34.90], /* SW — shared with Dan E / Benjamin NW         */
        [32.00, 35.40], /* SE — shared with Benjamin NE                 */
        [32.55, 35.55]  /* close                                        */
      ],
      desc: "Joseph's younger son received Jacob's greater blessing (Gen 48:19). The Tabernacle rested at Shiloh in Ephraim for ~300 years. After the kingdom split, Ephraim dominated the northern tribes.",
      refs: ['Joshua 16:5', 'Genesis 48:20', 'Hosea 5:3'] },

    /* WEST MANASSEH — north of Ephraim+Dan, west of Jezreel */
    { name: 'Manasseh (West)', fillColor: '#5c3d9e', fillOpacity: 0.28, color: '#5c3d9e',
      coords: [
        [32.75, 34.65], /* NW — coast, shared with Asher SW            */
        [32.75, 35.10], /* NE — shared with Zebulun SW / Issachar NW   */
        [32.55, 35.10], /* SE — shared with Ephraim N / Issachar W     */
        [32.55, 34.90], /* S  — shared with Ephraim NW / Dan NE        */
        [32.55, 34.65], /* SW — coast, shared with Dan N               */
        [32.75, 34.65]  /* close                                       */
      ],
      desc: "Half of Manasseh — Joseph's firstborn — received land north of Ephraim including the Carmel ridge and coastal plain. The daughters of Zelophehad successfully petitioned Moses for an inheritance (Num 27:7) — God affirmed their case, establishing a legal precedent.",
      refs: ['Joshua 17:1', 'Numbers 27:7', 'Joshua 17:3'] },

    /* ISSACHAR — fertile Jezreel Valley east of Manasseh, south of Galilee */
    { name: 'Issachar', fillColor: '#2e8c7c', fillOpacity: 0.28, color: '#2e8c7c',
      coords: [
        [32.75, 35.10], /* NW — shared with W.Manasseh NE / Zebulun SW  */
        [32.75, 35.55], /* NE — shared with Zebulun SE / Naphtali SW    */
        [32.55, 35.55], /* SE — shared with Ephraim NE                  */
        [32.55, 35.10], /* SW — shared with Ephraim N / W.Manasseh SE   */
        [32.75, 35.10]  /* close                                        */
      ],
      desc: "Settled in the fertile Jezreel Valley. Jacob's blessing: 'a strong donkey crouching between the sheepfolds' — implying agricultural contentment. They provided warriors for David who 'understood the times' (1 Chr 12:32).",
      refs: ['Joshua 19:17', 'Genesis 49:14', '1 Chronicles 12:32'] },

    /* ZEBULUN — Lower Galilee, between Asher and Naphtali */
    { name: 'Zebulun', fillColor: '#3d7a5c', fillOpacity: 0.28, color: '#3d7a5c',
      coords: [
        [33.00, 35.10], /* NE — shared with Naphtali NW / Asher NE     */
        [33.00, 35.00], /* NW — shared with Asher NE (same lon)        */
        [32.75, 35.00], /* SW — shared with Asher SE / W.Manasseh NE   */
        [32.75, 35.55], /* SE — shared with Issachar NE / Naphtali SW  */
        [33.00, 35.10]  /* close                                       */
      ],
      desc: "Lower Galilee tribe. Isaiah prophesied: 'The land of Zebulun … the people dwelling in darkness have seen a great light' (Isa 9:1) — fulfilled when Jesus based his ministry in Capernaum in Zebulun territory.",
      refs: ['Joshua 19:10', 'Isaiah 9:1', 'Matthew 4:15'] },

    /* ASHER — coastal Galilee strip from Carmel to Phoenicia */
    { name: 'Asher', fillColor: '#c05c7a', fillOpacity: 0.28, color: '#c05c7a',
      coords: [
        [33.30, 34.65], /* NW — Phoenician border                      */
        [33.30, 35.00], /* NE — shared with Naphtali NW / Dan-N SW     */
        [33.00, 35.00], /* SE — shared with Zebulun NW / Naphtali SW   */
        [32.75, 35.00], /* S  — shared with Zebulun SW / W.Manasseh NE */
        [32.75, 34.65], /* SW — coast, shared with W.Manasseh NW       */
        [33.30, 34.65]  /* close                                       */
      ],
      desc: "Coastal tribe bordering Phoenicia in the north. Jacob: 'Asher's food shall be rich; he shall yield royal delicacies' — olive groves and coastal fertility. The prophetess Anna, who greeted the infant Jesus in the Temple, was from Asher (Luke 2:36).",
      refs: ['Joshua 19:24', 'Genesis 49:20', 'Luke 2:36'] },

    /* NAPHTALI — Upper Galilee and Sea of Galilee basin */
    { name: 'Naphtali', fillColor: '#1a6699', fillOpacity: 0.28, color: '#1a6699',
      coords: [
        [33.30, 35.00], /* NW — shared with Asher NE                   */
        [33.30, 35.65], /* NE — shared with Dan-north SW               */
        [32.75, 35.55], /* SE — shared with Issachar NE / Zebulun SE   */
        [33.00, 35.10], /* SW — shared with Zebulun NE / Asher SE      */
        [33.00, 35.00], /* W  — shared with Asher SE                   */
        [33.30, 35.00]  /* close                                       */
      ],
      desc: "Upper Galilee tribe surrounding the Sea of Galilee. Barak was from Kedesh-Naphtali. Capernaum — Jesus's ministry headquarters — lay in Naphtali, fulfilling Isaiah's 'great light' prophecy to the despised northern region.",
      refs: ['Joshua 19:32', 'Genesis 49:21', 'Matthew 4:13'] },

    /* DAN (northern) — migrated north to Laish/Dan near Mount Hermon */
    { name: 'Dan (northern)', fillColor: '#aa3311', fillOpacity: 0.26, color: '#aa3311',
      coords: [
        [33.55, 35.65], /* NE                                          */
        [33.55, 35.00], /* NW                                          */
        [33.30, 35.00], /* SW — shared with Asher NE / Naphtali NW    */
        [33.30, 35.65], /* SE — shared with Naphtali NE               */
        [33.55, 35.65]  /* close                                       */
      ],
      desc: "After failing to hold their western territory, most of Dan migrated north and conquered the peaceful city of Laish, renaming it Dan. Jeroboam erected one of his two golden calves here.",
      refs: ['Judges 18:27', '1 Kings 12:29', 'Joshua 19:47'] },

    /* ── East of Jordan (Transjordan) ── */

    /* REUBEN — Moabite plateau east of Dead Sea */
    { name: 'Reuben', fillColor: '#8b5c1a', fillOpacity: 0.28, color: '#8b5c1a',
      coords: [
        [31.88, 35.65], /* NW — shared with Gad SW                    */
        [31.88, 36.25], /* NE — shared with Gad NE                    */
        [31.10, 36.00], /* SE                                          */
        [31.00, 35.65], /* SW                                          */
        [31.88, 35.65]  /* close                                       */
      ],
      desc: "Jacob's firstborn, who forfeited his birthright through sin. The tribe settled east of the Dead Sea on the Moabite plateau. Moses challenged them: 'Shall your brothers go to war while you sit here?' (Num 32:6). Jacob's word: 'unstable as water, you shall not excel.'",
      refs: ['Joshua 13:15', 'Numbers 32:1', 'Genesis 49:4'] },

    /* GAD — Gilead (central Transjordan) */
    { name: 'Gad', fillColor: '#6b4c2a', fillOpacity: 0.28, color: '#6b4c2a',
      coords: [
        [32.40, 35.65], /* NW — shared with E.Manasseh SW             */
        [32.40, 36.35], /* NE — shared with E.Manasseh SE             */
        [31.88, 36.25], /* SE — shared with Reuben NE                 */
        [31.88, 35.65], /* SW — shared with Reuben NW                 */
        [32.40, 35.65]  /* close                                       */
      ],
      desc: "Settled in Gilead (central Transjordan). Jacob: 'Raiders shall raid Gad, but he shall raid at their heels.' Jephthah the judge was a Gadite. The tribe pledged to cross the Jordan and fight with their brothers until the entire land was conquered.",
      refs: ['Joshua 13:24', 'Genesis 49:19', 'Judges 11:1'] },

    /* EAST MANASSEH — Bashan (northern Transjordan) */
    { name: 'Manasseh (East)', fillColor: '#7c5c9e', fillOpacity: 0.28, color: '#7c5c9e',
      coords: [
        [33.30, 35.65], /* NW — shared with Dan-north SE              */
        [33.30, 36.60], /* NE                                          */
        [32.40, 36.35], /* SE — shared with Gad NE                   */
        [32.40, 35.65], /* SW — shared with Gad NW                   */
        [33.30, 35.65]  /* close                                      */
      ],
      desc: "Half of Manasseh settled in Bashan (north Transjordan) after defeating Og, one of the last Rephaim giants. The region was renowned for its powerful cattle — 'cows of Bashan' became prophetic shorthand for complacent luxury (Amos 4:1).",
      refs: ['Joshua 13:29', 'Deuteronomy 3:1', 'Numbers 32:39', 'Amos 4:1'] }
  ];

  /* Render each tribal territory as a filled polygon; click for tribe info */
  tribes.forEach(function (t) {
    var poly = L.polygon(_smoothRing(t.coords, 2), {
      color:       t.color,
      weight:      1.5,
      fillColor:   t.fillColor,
      fillOpacity: t.fillOpacity,
      opacity:     0.85
    });
    poly.bindTooltip(t.name, { sticky: true, direction: 'center' });
    /* Reuse the city-detail panel for tribe info */
    poly.on('click', function () {
      _showCityDetail(t); /* pass full object so significance is included */
    });
    _addLayer(poly);

    /* Permanent centroid label — same pattern as _addRegion labels */
    var center = poly.getBounds().getCenter();
    var labelIcon = L.divIcon({
      className: 'maps-tribe-label',
      html:      '<span style="color:' + escHtml(t.color) + '">' + escHtml(t.name) + '</span>',
      iconSize:  [1, 1],
      iconAnchor:[0, 0]
    });
    _addLayer(L.marker(center, { icon: labelIcon, interactive: false, keyboard: false }));
  });

  /* Reference cities marked on the tribal map */
  var cities = [
    { name: 'Jerusalem', lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: 'On the border of Benjamin and Judah. David captured it from the Jebusites and made it his capital; Solomon built the Temple here.',
      refs: ['Joshua 15:63', '2 Samuel 5:7'] },
    { name: 'Shiloh', lat: 32.057, lon: 35.287, capital: true,
      desc: "The Tabernacle rested in Ephraim at Shiloh for ~300 years. The land was divided among the twelve tribes here in Joshua 18–19.",
      refs: ['Joshua 18:1', '1 Samuel 4:3'] },
    { name: 'Shechem', lat: 32.199, lon: 35.283,
      desc: "Levitical city and city of refuge in Ephraim. Joshua's great farewell address — 'Choose this day whom you will serve' — was delivered here.",
      refs: ['Joshua 20:7', 'Joshua 24:1'] },
    { name: 'Hebron', lat: 31.533, lon: 35.096,
      desc: "Caleb's inheritance; a Levitical city of refuge. The patriarchs and matriarchs are buried here.",
      refs: ['Joshua 14:13', 'Joshua 21:11'] },
    { name: 'Dan (N)', lat: 33.248, lon: 35.651,
      desc: "Northernmost city after Dan's migration here. 'From Dan to Beersheba' — the full length of the promised land.",
      refs: ['Judges 18:29', '1 Kings 12:29'] },
    { name: 'Beersheba', lat: 31.252, lon: 34.792,
      desc: "Southernmost marker of the promised land — 'from Dan to Beersheba' denoted all Israel.",
      refs: ['Judges 20:1', 'Genesis 21:31'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 9. Time of the Judges ───────────────────────────────────────────────── */
function _renderJudges(map) {
  /* Israel (tribal confederacy) — no king, no central power */
  _addRegion([[30.75,34.65],[30.75,35.55],[33.30,35.55],[33.30,34.65]], 'Israelite tribal territories', '#3d7a4a', 0.05);

  /* Surrounding peoples who oppressed and threatened Israel during the Judges period */
  _region('empire-philistia', -1000, [[31.50,34.40],[31.50,34.90],[31.88,34.90],[31.88,34.40]], 'Philistia',    '#7b5ea7', 0.10);
  _addRegion([[31.00,34.60],[31.00,35.00],[31.50,35.00],[31.50,34.60]], 'Shephelah',    '#9b7000', 0.07);
  _addRegion([[31.88,35.55],[31.88,36.20],[32.55,36.20],[32.55,35.55]], 'Ammon/Gilead', '#3d7a4a', 0.07);
  _addRegion([[31.00,35.55],[31.00,36.20],[31.88,36.20],[31.88,35.55]], 'Moab',         '#c44d29', 0.07);

  /* Key battles, judge homelands, and Philistine cities — c. 1380–1050 BC */

  var sites = [
    /* ── Deborah and Barak — northern battle ── */
    { name: 'Kishon River (Deborah / Barak vs. Sisera)', lat: 32.57, lon: 35.10, capital: true,
      desc: "Deborah the prophetess-judge summoned Barak to lead Israel against Sisera's 900 iron chariots. The LORD threw the Canaanites into confusion; the Kishon River swept away the chariot force. Sisera fled on foot — and Jael drove a tent peg through his skull as he slept in her tent.",
      refs: ['Judges 4:7', 'Judges 5:21', 'Judges 4:21'] },

    { name: "Kedesh-Naphtali (Barak's home)", lat: 33.020, lon: 35.569,
      desc: "Home of Barak son of Abinoam. Deborah sent for him here: 'Has not the LORD commanded you?' He refused to go without Deborah — so the honor of the decisive kill went to Jael, a woman.",
      refs: ['Judges 4:6', 'Judges 4:8', 'Hebrews 11:32'] },

    /* ── Gideon — Midianite oppression ── */
    { name: 'Jezreel Valley (Gideon vs. Midianites)', lat: 32.55, lon: 35.30, capital: true,
      desc: "The Midianites spread across the valley 'like locusts for number.' Gideon's 300 — chosen by lapping water like dogs — surrounded the camp at night with torches in jars and trumpets. They smashed the jars, raised their torches, and shouted: 'A sword for the LORD and for Gideon!' The army panicked and destroyed itself.",
      refs: ['Judges 7:7', 'Judges 7:20', 'Judges 7:12'] },

    { name: "Ophrah (Gideon's hometown)", lat: 32.400, lon: 35.420,
      desc: "The Angel of the LORD appeared to Gideon while he threshed wheat in a winepress — hiding from the Midianites. God called the terrified farmer a 'mighty man of valor' and commissioned him. Gideon asked for signs; God patiently gave them.",
      refs: ['Judges 6:11', 'Judges 6:15', 'Judges 8:32'] },

    /* ── Jephthah — Ammonite oppression ── */
    { name: 'Mizpah of Gilead (Jephthah)', lat: 32.000, lon: 35.800,
      desc: "Jephthah, an outcast son of a harlot expelled by his brothers, was recalled to lead Gilead against the Ammonites. The Spirit of the LORD came on him. He made a rash vow before battle. He won — but his vow fell tragically on his only daughter.",
      refs: ['Judges 11:11', 'Judges 11:29', 'Judges 11:34'] },

    { name: 'Rabbah (Ammonite capital)', lat: 31.955, lon: 35.945,
      desc: "Capital of Ammon (modern Amman, Jordan). Jephthah's victory brought twenty Ammonite cities under Israelite control. Centuries later, David besieged Rabbah here — the occasion of his sin with Bathsheba.",
      refs: ['Judges 11:32', '2 Samuel 12:26'] },

    /* ── Samson — Philistine conflict ── */
    { name: "Zorah (Samson's hometown)", lat: 31.782, lon: 34.990,
      desc: "The Angel of the LORD announced Samson's birth to his barren mother. He was consecrated a Nazirite from the womb. The Spirit of the LORD began to stir in him between Zorah and Eshtaol — setting up the thirty-year conflict with the Philistines.",
      refs: ['Judges 13:2', 'Judges 13:24', 'Judges 13:25'] },

    { name: 'Timnah (Samson vs. Philistines)', lat: 31.760, lon: 34.937,
      desc: "Samson saw a Philistine woman here and demanded her as a wife. On the way he killed a lion bare-handed. Later he used honey from its carcass as a riddle at the wedding. The Philistines threatened his wife for the answer — he lost the bet and killed thirty men for their garments.",
      refs: ['Judges 14:1', 'Judges 14:5', 'Judges 14:12'] },

    { name: 'Valley of Sorek (Delilah)', lat: 31.720, lon: 34.970,
      desc: "Samson loved Delilah in this valley. The five Philistine lords each offered her 1,100 pieces of silver to discover the secret of his strength. Three times he lied; the fourth time he confessed. She shaved his head as he slept — and the LORD departed from him.",
      refs: ['Judges 16:4', 'Judges 16:17', 'Judges 16:20'] },

    { name: 'Gaza (Samson imprisoned)', lat: 31.502, lon: 34.467,
      desc: "Samson was blinded, bound in bronze chains, and made to grind grain in prison — the judge reduced to an animal. At a Philistine festival, his hair had grown. He braced himself between the two central pillars, prayed, and pushed them apart — collapsing the building on 3,000 Philistines. 'He killed more at his death than in his life.'",
      refs: ['Judges 16:21', 'Judges 16:28', 'Judges 16:30'] },

    /* ── Eli, the Ark, and Samuel ── */
    { name: 'Shiloh (Tabernacle / Eli / Samuel)', lat: 32.057, lon: 35.287, capital: true,
      desc: "The Tabernacle stood here for ~300 years. Eli was high priest; Hannah prayed here and received Samuel through desperate prayer. Samuel ministered before the LORD as a boy and received his first prophetic call here. Then Israel, treating the ark as a lucky charm, carried it to battle — God allowed it to be captured as judgment on Eli's house.",
      refs: ['1 Samuel 1:3', '1 Samuel 4:3', 'Psalm 78:60', 'Jeremiah 7:12'],
      significance: 'God allowed Shiloh\'s destruction to prove that his presence cannot be presumed upon. Jeremiah cited it as a warning to Jerusalem: "I will make this house like Shiloh" — no building guarantees God\'s protection when the people are corrupt (Jeremiah 7:14).' },

    { name: 'Aphek / Ebenezer (Ark captured)', lat: 32.096, lon: 34.912,
      desc: "Israel was routed by the Philistines here — 30,000 dead. Hophni and Phinehas were killed. The ark was captured. When the news reached Eli, he fell backward from his seat and broke his neck. His dying daughter-in-law named her son Ichabod — 'the glory has departed from Israel.'",
      refs: ['1 Samuel 4:1', '1 Samuel 4:10', '1 Samuel 4:17'] },

    /* ── Philistine city-states ── */
    { name: 'Ashdod', lat: 31.810, lon: 34.649,
      desc: "Philistine city where the captured ark was placed in Dagon's temple. The next morning Dagon was face-down before the ark. On the second morning Dagon's head and hands lay cut off on the threshold. The LORD struck the people with tumors until they sent the ark away.",
      refs: ['1 Samuel 5:1', '1 Samuel 5:3', '1 Samuel 5:4'] },

    { name: 'Gath', lat: 31.729, lon: 34.853,
      desc: "Hometown of Goliath and the Anakim giants. The ark passed through Gath causing disease. David feigned madness before King Achish here to escape. Ittai the Gittite — paradoxically — was David's most loyal soldier.",
      refs: ['1 Samuel 5:8', '1 Samuel 17:4', '1 Samuel 21:13', '2 Samuel 15:19'] },

    { name: 'Ekron', lat: 31.867, lon: 34.845,
      desc: "When the ark arrived in Ekron, the people cried: 'They have brought the ark to kill us!' The five Philistine lords assembled and sent it back to Israel on a new cart drawn by milch cows. Baal-Zebub, god of Ekron, was consulted by king Ahaziah of Israel — Elijah rebuked the messengers on the road.",
      refs: ['1 Samuel 5:10', '1 Samuel 6:12', '2 Kings 1:2'] }
  ];

  sites.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 10. David's Kingdom and Military Campaigns ──────────────────────────── */
function _renderDavidKingdom(map) {
  /* Egypt — the great southern empire David maintained relations with */
  _region('empire-egypt-core', -1000, [[23.00,28.00],[23.00,36.00],[30.00,36.00],[30.00,28.00]], 'Egypt', '#9b7000', 0.06);
  /* Neighbours outside David's direct control */
  _addRegion([[33.20,34.60],[33.20,35.55],[34.60,35.55],[34.60,34.60]], 'Phoenicia (allied)', '#1a5fa8', 0.07);
  _addRegion([[31.00,34.30],[31.00,34.80],[31.88,34.80],[31.88,34.30]], 'Philistia (subdued)','#7b5ea7', 0.08);

  /* Approximate extent of David's domain including conquered and vassal states.
     The precise borders of his influence are uncertain; based on 2 Sam 8.   */
  var kingdomPolygon = [
    [33.35, 35.80],   /* Dan — northern border */
    [33.20, 36.50],   /* Aram-Damascus (vassal; 2 Sam 8:6) */
    [34.00, 37.50],   /* Aram-Zobah (vassal) */
    [32.00, 37.00],   /* Ammon / Rabbah (subdued) */
    [31.50, 36.20],   /* Moab (two-thirds executed; garrisons placed) */
    [29.80, 35.00],   /* Edom / Aqaba (18,000 killed; garrisons throughout) */
    [30.75, 34.40],   /* southern Negev */
    [31.60, 34.50],   /* Philistine border — subdued but not absorbed */
    COORDS.caesarea,   /* northern coast */
    [33.10, 34.95],   /* Phoenician border (Tyre/Sidon were allies, not vassals) */
    [33.35, 35.80]    /* close */
  ];

  _addLayer(L.polygon(kingdomPolygon, {
    color:       '#9b7000',
    weight:      1.5,
    fillColor:   '#b8902a',
    fillOpacity: 0.15,
    dashArray:   '6 4'
  }));

  /* Military campaign routes radiating from Jerusalem */
  var philistineCampaign = [
    COORDS.jerusalem,  /* Jerusalem */
    [31.750, 35.150],  /* Valley of Rephaim (SW of Jerusalem) */
    [31.729, 34.853],  /* Gath region — Philistine heartland */
    [31.600, 34.700]   /* coastal plain */
  ];

  var moabCampaign = [
    COORDS.jerusalem,  /* Jerusalem */
    [31.600, 35.600],  /* Judean desert east */
    [31.500, 36.000]   /* Moab highlands (2 Sam 8:2) */
  ];

  var ammonCampaign = [
    COORDS.jerusalem,  /* Jerusalem */
    [32.100, 35.700],  /* Jordan crossing northward */
    [31.955, 35.945]   /* Rabbah (Ammon — modern Amman) */
  ];

  var aramCampaign = [
    COORDS.jerusalem,  /* Jerusalem */
    [32.500, 35.500],  /* northward through Galilee */
    COORDS.damascus   /* Damascus — garrisons placed (2 Sam 8:6) */
  ];

  var edomCampaign = [
    COORDS.jerusalem,  /* Jerusalem */
    [31.100, 35.300],  /* Valley of Salt — 18,000 Edomites defeated */
    [30.500, 35.000]   /* Edom highlands — garrisons placed throughout */
  ];

  _addLayer(_routeLine(philistineCampaign, '#b00010', false));
  _addLayer(_routeLine(moabCampaign,       '#b00010', false));
  _addLayer(_routeLine(ammonCampaign,      '#b00010', false));
  _addLayer(_routeLine(aramCampaign,       '#b00010', false));
  _addLayer(_routeLine(edomCampaign,       '#b00010', false));

  var cities = [
    { name: 'Jerusalem', lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: "David captured the Jebusite stronghold of Zion and made it his capital. He brought the ark here with dancing and great rejoicing. His heart burned to build a permanent Temple — but God gave him a greater gift: the Davidic covenant. 'I will raise up your offspring … and establish the throne of his kingdom forever' (2 Sam 7:12–13).",
      refs: ['2 Samuel 5:7', '2 Samuel 6:12', '2 Samuel 7:12', '2 Samuel 7:16'],
      significance: 'When David danced before the ark entering Jerusalem, he was acting as a type of the greater Son of David who would enter the same city to cries of "Hosanna!" — and then pass through death to the throne of the universe.' },
    { name: 'Hebron (David crowned)', lat: 31.533, lon: 35.096,
      desc: "David reigned over Judah alone here for seven and a half years while the house of Saul held the north. After Ish-bosheth's assassination, the elders of all Israel came to Hebron and anointed David king over all Israel. The nation was finally unified.",
      refs: ['2 Samuel 2:4', '2 Samuel 5:5', '2 Samuel 5:3'] },
    { name: 'Damascus (Aram conquered)', lat: COORDS.damascus[0], lon: COORDS.damascus[1],
      desc: "David defeated Hadadezer of Aram-Zobah and the Arameans of Damascus who came to his aid. He placed garrisons throughout Syria and collected tribute. 'The LORD gave David victory wherever he went' (2 Sam 8:14). The captured silver and gold were dedicated to the LORD.",
      refs: ['2 Samuel 8:5', '2 Samuel 8:6', '2 Samuel 8:11'] },
    { name: 'Rabbah (Ammon)', lat: 31.955, lon: 35.945,
      desc: "Joab besieged Rabbah (modern Amman) while David remained in Jerusalem — the occasion of the great fall: David, Bathsheba, and the murder of Uriah. After Nathan's confrontation and David's repentance (Ps 51), Joab captured the citadel and summoned David to take the crown.",
      refs: ['2 Samuel 11:1', '2 Samuel 12:26', '2 Samuel 12:30', 'Psalm 51:1'] },
    { name: 'Valley of Rephaim', lat: 31.750, lon: 35.155,
      desc: "The Philistines spread here southwest of Jerusalem twice. Both times David inquired of the LORD before attacking — not presuming on yesterday's answer. The second battle was won by a divinely timed flanking maneuver: 'attack when you hear the sound of marching in the treetops of the balsam trees.'",
      refs: ['2 Samuel 5:18', '2 Samuel 5:22', '2 Samuel 5:24'] },
    { name: 'Valley of Salt (Edom)', lat: 31.100, lon: 35.300,
      desc: "Joab and Abishai killed 18,000 Edomites in the Valley of Salt south of the Dead Sea. David placed garrisons throughout Edom. This fulfilled Isaac's prophecy that Jacob's nation would one day throw off Esau's yoke.",
      refs: ['2 Samuel 8:13', '1 Chronicles 18:12', 'Genesis 27:40'] },
    { name: 'Bethlehem', lat: 31.705, lon: 35.202,
      desc: "David's hometown. Samuel came here secretly and anointed the youngest of Jesse's sons — the boy no one considered — while rejecting the impressive older brothers. 'The LORD sees not as man sees; man looks on the outward appearance, but the LORD looks on the heart' (1 Sam 16:7).",
      refs: ['1 Samuel 16:1', '1 Samuel 16:7', 'Ruth 4:17'] },
    { name: 'Ziklag', lat: 31.390, lon: 34.700,
      desc: "Achish of Gath gave Ziklag to David during his years as a fugitive from Saul. The Amalekites burned it and seized the women and children; David pursued and recovered everything. He learned of Saul and Jonathan's death here — and composed his great lament: 'How the mighty have fallen.'",
      refs: ['1 Samuel 27:6', '1 Samuel 30:1', '2 Samuel 1:17'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 11. Assyrian & Babylonian Invasions ─────────────────────────────────── */
function _renderInvasions(map) {
  /* Empire heartland zones showing the source of each invasion */
  _region('empire-assyria-core', -700, [[35.00,37.00],[35.00,48.00],[38.00,48.00],[38.00,37.00]], 'Assyrian Empire',  '#8b1a1a', 0.07);
  _region('empire-babylon-core', -590, [[30.00,38.00],[30.00,50.00],[35.00,50.00],[35.00,38.00]], 'Babylonian Empire','#1a3a6b', 0.07);
  _region('empire-egypt-core', -600, [[22.00,26.00],[22.00,36.00],[30.00,36.00],[30.00,26.00]], 'Egypt',            '#9b7000', 0.07);
  _addRegion([[31.00,34.40],[31.00,36.00],[33.30,36.00],[33.30,34.40]], 'Israel / Judah',   '#3d7a4a', 0.06);

  /* ── Assyrian conquest of northern Israel, 722 BC (Sargon II) ── */
  var assyrianRoute = [
    COORDS.nineveh,  /* Nineveh — Assyrian capital */
    COORDS.carchemish,  /* Carchemish — Euphrates crossing point */
    [35.133, 36.750],  /* Hamath — gateway into Canaan / Syria */
    COORDS.damascus,  /* Damascus — fell to Tiglath-Pileser III in 732 BC */
    [32.278, 35.198]   /* Samaria — fell after three-year siege, 722 BC */
  ];

  /* ── Sennacherib's western campaign, 701 BC ── */
  var sennacheribRoute = [
    COORDS.nineveh,  /* Nineveh */
    COORDS.carchemish,  /* Carchemish */
    [34.000, 36.300],  /* Hamath / Riblah — staging area */
    [31.560, 34.847],  /* Lachish — major siege (depicted in palace reliefs) */
    COORDS.jerusalem   /* Jerusalem — besieged but miraculously spared (2 Kgs 19) */
  ];

  /* ── Babylonian campaigns, 605–586 BC (Nebuchadnezzar) ── */
  var babylonianRoute = [
    COORDS.babylon,  /* Babylon */
    [35.000, 43.500],  /* northwest march along the Euphrates */
    COORDS.carchemish,  /* Carchemish — decisive battle 605 BC; Egypt routed */
    [35.133, 36.750],  /* Hamath / Syria */
    COORDS.damascus,  /* Damascus */
    COORDS.jerusalem   /* Jerusalem — 605 BC: Daniel; 597 BC: Jehoiachin; 586 BC: city destroyed */
  ];

  _addLayer(_routeLine(assyrianRoute,    '#8b1a1a', false));
  _addLayer(_routeLine(sennacheribRoute, '#c44d29', false));
  _addLayer(_routeLine(babylonianRoute,  '#1a3a6b', true));

  var cities = [
    { name: 'Nineveh', lat: COORDS.nineveh[0], lon: COORDS.nineveh[1], capital: true,
      desc: "Capital of the Assyrian empire. Under Sargon II it conquered Samaria (722 BC). Under Sennacherib it besieged Jerusalem (701 BC) but was repelled by the Angel of the LORD. Jonah preached here; the city repented. Nahum later prophesied its destruction — in 612 BC Nineveh fell to the Babylonians and Medes exactly as foretold.",
      refs: ['2 Kings 17:6', '2 Kings 19:36', 'Nahum 1:1', 'Jonah 3:3'] },
    { name: 'Carchemish', lat: COORDS.carchemish[0], lon: COORDS.carchemish[1],
      desc: "The great Euphrates crossing. In 605 BC Nebuchadnezzar crushed Pharaoh Neco here — the battle that handed the ancient Near East to Babylon. Jeremiah 46:2 marks it as the beginning of the end for Judah. Daniel's first deportation followed within that year.",
      refs: ['Jeremiah 46:2', '2 Chronicles 35:20', 'Daniel 1:1'] },
    { name: 'Damascus', lat: COORDS.damascus[0], lon: COORDS.damascus[1], capital: true,
      desc: "Capital of Aram. Fell to Tiglath-Pileser III of Assyria in 732 BC; King Rezin was executed. Isaiah had prophesied: 'Damascus will cease to be a city and will become a heap of ruins' (Isa 17:1) — fulfilled within his generation.",
      refs: ['2 Kings 16:9', 'Isaiah 17:1', 'Isaiah 8:4'] },
    { name: 'Samaria', lat: 32.278, lon: 35.198, capital: true,
      desc: "Capital of the northern kingdom. After a three-year siege, Sargon II captured Samaria in 722 BC and deported 27,290 Israelites to Assyria, replacing them with foreign settlers. The ten tribes were scattered — fulfilling generations of warnings from Amos, Hosea, and Micah.",
      refs: ['2 Kings 17:5', '2 Kings 17:6', '2 Kings 17:23', 'Hosea 13:16'] },
    { name: 'Lachish', lat: 31.560, lon: 34.847, capital: true,
      desc: "Sennacherib personally directed the siege from his camp here, the conquest immortalized in massive palace reliefs in Nineveh. Archaeology has uncovered a clear destruction layer from 701 BC. Sennacherib boasted of trapping Hezekiah 'like a bird in a cage' — conspicuously admitting he never took Jerusalem.",
      refs: ['2 Kings 18:14', '2 Kings 19:8', 'Isaiah 36:2', 'Micah 1:13'] },
    { name: 'Jerusalem', lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: "In 701 BC Sennacherib surrounded Jerusalem. Hezekiah spread his letter before the LORD and prayed; Isaiah prophesied; the Angel of the LORD killed 185,000 Assyrians in a night — Jerusalem was spared. But in 586 BC, after a century of prophetic warning, Nebuchadnezzar broke the walls, burned the Temple, and marched the survivors to Babylon. 'How lonely sits the city that was full of people!' (Lam 1:1).",
      refs: ['2 Kings 19:35', '2 Kings 25:9', 'Lamentations 1:1', 'Jeremiah 52:13'],
      significance: 'The exile fulfilled the covenant curses of Deuteronomy 28 — but also launched the prophets\' greatest visions: the new exodus, new covenant, and the coming Servant who would accomplish what Israel never could (Isaiah 52–53; Jeremiah 31:31–34).' },
    { name: 'Babylon', lat: COORDS.babylon[0], lon: COORDS.babylon[1], capital: true,
      desc: "By its rivers the exiles wept and hung their harps on the willows. Daniel served faithfully in Nebuchadnezzar's court; Ezekiel prophesied among the exiles at the Chebar canal. In 539 BC the handwriting on the wall ended the empire in a single night; Cyrus of Persia conquered Babylon and decreed the return of the exiles.",
      refs: ['Psalm 137:1', 'Daniel 5:30', 'Ezra 1:1', 'Revelation 17:5'] },
    { name: 'Riblah', lat: 34.500, lon: 36.600,
      desc: "Nebuchadnezzar's field headquarters during the Judean campaigns. Zedekiah, the last king of Judah, was captured fleeing and brought here in chains. His sons were slaughtered before his eyes — the last sight he ever saw — then his eyes were gouged out and he was marched to Babylon.",
      refs: ['2 Kings 25:6', 'Jeremiah 52:9', 'Jeremiah 39:5'] },
    { name: 'Megiddo (Josiah killed)', lat: 32.588, lon: 35.185,
      desc: "In 609 BC the reformer-king Josiah intercepted Pharaoh Neco marching to aid dying Assyria against Babylon. Despite Neco's warning, Josiah engaged in battle and was struck by archers. He died — the last good king of Judah was gone. All the nation mourned. The rapid decline to exile accelerated.",
      refs: ['2 Kings 23:29', '2 Chronicles 35:22', 'Zechariah 12:11'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 12. Solomon's Kingdom & Trade Routes ────────────────────────────────── */
function _renderSolomonKingdom(map) {
  /* Approximate kingdom extent: 1 Kgs 4:21,24 — Tiphsah to Gaza, from the Euphrates to Egypt */
  var kingdomPolygon = [
    [36.00, 38.50],   /* Tiphsah on the Euphrates — northern limit (1 Kgs 4:24) */
    [34.00, 36.60],   /* Hamath gateway into Syria */
    [33.27, 35.20],   /* Phoenician border (Tyre — ally, not vassal) */
    COORDS.caesarea,   /* northern Mediterranean coast */
    [31.40, 34.20],   /* Philistine coast (subdued under David) */
    [30.75, 34.00],   /* Brook of Egypt — SW border (1 Kgs 8:65) */
    [29.55, 34.95],   /* Ezion-geber on the Red Sea */
    [30.50, 36.00],   /* Edom (under Solomonic control) */
    [31.00, 36.50],   /* Moab */
    [31.96, 35.95],   /* Ammon / Rabbah */
    [33.50, 36.80],   /* Aram-Damascus (vassal) */
    [34.55, 38.28],   /* Tadmor — desert caravan fortress (2 Chr 8:4) */
    [36.00, 38.50]    /* close */
  ];

  _addLayer(L.polygon(kingdomPolygon, {
    color:       '#9b7000',
    weight:      1.5,
    fillColor:   '#d4a800',
    fillOpacity: 0.12,
    dashArray:   '6 4'
  }));

  /* Red Sea trade route: Jerusalem → Ezion-geber → Ophir (3-year voyage) */
  var redSeaRoute = [
    COORDS.jerusalem,  /* Jerusalem */
    [29.55,  34.95],   /* Ezion-geber / Elath — fleet harbor (1 Kgs 9:26) */
    [25.00,  38.00],   /* Red Sea, southbound */
    [21.50,  43.50]    /* Ophir / Arabia Felix (gold, ivory, peacocks; 1 Kgs 10:11) */
  ];

  /* Phoenician alliance: Jerusalem → Megiddo → Tyre (cedar, craftsmen, gold) */
  var phoenicianRoute = [
    COORDS.jerusalem,  /* Jerusalem */
    [32.588, 35.185],  /* Megiddo — Solomonic chariot city */
    [33.271, 35.196]   /* Tyre — Hiram's alliance (1 Kgs 5:1) */
  ];

  /* Egypt trade route: horses & chariots imported (1 Kgs 10:28) */
  var egyptRoute = [
    COORDS.jerusalem,  /* Jerusalem */
    [31.858, 34.919],  /* Gezer — Pharaoh's dowry gift (1 Kgs 9:16) */
    [30.750, 34.000],  /* Brook of Egypt / Egyptian border */
    [30.060, 31.250]   /* Memphis / Egypt — horses and chariots */
  ];

  /* Caravan route through the Syrian desert to Tadmor */
  var tadmorRoute = [
    COORDS.jerusalem,  /* Jerusalem */
    COORDS.damascus,  /* Damascus */
    [34.548, 38.283]   /* Tadmor (Palmyra) — desert fortress and caravan hub */
  ];

  _addLayer(_routeLine(redSeaRoute,     '#c44d29', false));
  _addLayer(_routeLine(phoenicianRoute, '#1a5fa8', false));
  _addLayer(_routeLine(egyptRoute,      '#3d7a4a', false));
  _addLayer(_routeLine(tadmorRoute,     '#9b7000', true));

  var cities = [
    { name: 'Jerusalem', lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: "Center of Solomon's empire. The Temple — built in seven years from Lebanese cedar and Ophir gold — was filled with the glory cloud at its dedication (1 Kings 8:10–11). His palace complex took thirteen years. Foreign dignitaries, including the Queen of Sheba, came from across the known world.",
      refs: ['1 Kings 6:37', '1 Kings 8:10', '1 Kings 10:1', '1 Kings 10:23'],
      significance: "Jesus declared himself 'greater than Solomon' (Matthew 12:42) — not in wisdom or wealth but in the kingdom he builds: not of cedar and gold but of living stones, reconciled to God through his own blood, whose glory will never depart." },
    { name: 'Ezion-geber', lat: 29.55, lon: 34.95, capital: true,
      desc: "Solomon's fleet harbor on the Gulf of Aqaba (Red Sea), built with Hiram's Phoenician sailors. Every three years the ships returned from Ophir with 420 talents of gold, silver, almugwood, ivory, apes, and peacocks — trade goods that underwrote the Temple's grandeur.",
      refs: ['1 Kings 9:26', '1 Kings 10:11', '1 Kings 10:22'] },
    { name: 'Megiddo', lat: 32.588, lon: 35.185, capital: true,
      desc: "One of Solomon's three great chariot cities (with Hazor and Gezer). Archaeology confirms a 10th-century BC Solomonic six-chambered gateway identical at all three sites — a striking confirmation of 1 Kings 9:15. It controlled the crucial Jezreel Valley pass.",
      refs: ['1 Kings 9:15', '1 Kings 10:26', '1 Kings 4:12'] },
    { name: 'Hazor', lat: 33.017, lon: 35.568,
      desc: "Rebuilt by Solomon as a major fortified city in the north. Yigael Yadin's excavations uncovered a Solomonic six-chambered gate identical to those at Megiddo and Gezer, fulfilling 1 Kings 9:15 with archaeological precision.",
      refs: ['1 Kings 9:15', 'Joshua 11:10'] },
    { name: 'Gezer', lat: 31.858, lon: 34.919,
      desc: "Pharaoh captured and burned Gezer, then gave it as a wedding dowry to his daughter — Solomon's wife. Solomon rebuilt it as a chariot city. The 'Gezer Calendar,' found here, is one of the oldest Hebrew inscriptions known, dated to the 10th century BC.",
      refs: ['1 Kings 9:15', '1 Kings 9:16', '1 Kings 9:17'] },
    { name: 'Tyre', lat: 33.271, lon: 35.196,
      desc: "Hiram king of Tyre supplied cedar and cypress from Lebanon, master craftsmen, and his sailors for Solomon's fleet. In return Solomon gave him twenty Galilean cities — which Hiram named Cabul ('worthless'), suggesting dissatisfaction with the arrangement.",
      refs: ['1 Kings 5:1', '1 Kings 9:11', '1 Kings 9:13'] },
    { name: 'Tadmor (Palmyra)', lat: 34.548, lon: 38.283,
      desc: "Solomon built Tadmor in the Syrian desert (2 Chronicles 8:4) as a fortress and watering station controlling the caravan route between Damascus and the Euphrates. Later called Palmyra, it became one of antiquity's greatest trading cities.",
      refs: ['2 Chronicles 8:4', '1 Kings 9:19'] },
    { name: 'Ophir (trade destination)', lat: 21.50, lon: 43.50,
      desc: "The ancient world's premier source of gold — located somewhere in southern Arabia, East Africa, or the Horn of Africa (exact location debated). Solomon's fleet from Ezion-geber made the three-year round voyage, returning with 420 talents of gold per voyage, plus ivory, precious stones, almugwood, and exotic animals.",
      refs: ['1 Kings 9:28', '1 Kings 10:11', '1 Kings 22:48'] },
    { name: 'Shechem', lat: 32.199, lon: 35.283,
      desc: "Where Solomon's son Rehoboam came to be crowned. The northern tribes demanded relief from the burden of forced labor. When Rehoboam rejected the counsel of wise elders and threatened to make the yoke heavier, ten tribes revolted. The kingdom Solomon spent forty years building fractured in a day.",
      refs: ['1 Kings 12:1', '1 Kings 12:4', '1 Kings 12:16'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 13. The Return from Exile ───────────────────────────────────────────── */
function _renderReturnExile(map) {
  /* Persian empire extent c. 538–400 BC — the political backdrop for the return */
  _addRegion([
    [23.00,25.00],[23.00,60.00],[39.00,60.00],[39.00,42.00],[37.00,36.00],[31.00,25.00],[23.00,25.00]
  ], 'Achaemenid Persian Empire', '#9b7000', 0.06);
  _addRegion([[31.00,34.40],[31.00,36.00],[33.30,36.00],[33.30,34.40]], 'Judea / Yehud province', '#3d7a4a', 0.09);
  _addRegion([[32.00,35.55],[32.00,36.50],[33.00,36.50],[33.00,35.55]], 'Samaria province', '#b33c3c', 0.07);

  /* Return route: Babylon → northwest along the Fertile Crescent → Damascus → Jerusalem.
     A direct desert crossing was impractical; all traffic followed the river valley north
     then turned west and south — the same route armies and merchants had used for centuries. */
  var returnRoute = [
    COORDS.babylon,  /* Babylon — exile community */
    [34.000, 43.500],  /* northwest up the Euphrates valley */
    COORDS.carchemish,  /* Carchemish — major Euphrates crossing */
    [36.200, 37.200],  /* Aleppo region */
    [34.000, 36.300],  /* Riblah / Hamath */
    COORDS.damascus,  /* Damascus */
    COORDS.jerusalem   /* Jerusalem */
  ];

  /* Ezra's route: Susa → Babylon → assembled at Ahava canal → same Fertile Crescent path */
  var ezraRoute = [
    [32.189, 48.255],  /* Susa — Ezra's and Nehemiah's posting */
    COORDS.babylon,  /* Babylon — joined the group at the Ahava canal (Ezra 8:15) */
    [34.000, 43.500],
    COORDS.carchemish,
    [36.200, 37.200],
    [34.000, 36.300],
    COORDS.damascus,
    COORDS.jerusalem   /* Jerusalem — 'the hand of our God was on us' (Ezra 8:31) */
  ];

  _addLayer(_routeLine(returnRoute, '#3d7a4a', false));
  _addLayer(_routeLine(ezraRoute,   '#3d7a4a', true));

  var cities = [
    { name: 'Babylon', lat: COORDS.babylon[0], lon: COORDS.babylon[1], capital: true,
      desc: "By its rivers the exiles wept and hung their harps on the willows (Psalm 137:1). Zerubbabel assembled the first return group here in 538 BC; Ezra used the Ahava canal as the staging point for his 458 BC group. In 539 BC Cyrus conquered Babylon in a single night and issued the decree of return.",
      refs: ['Psalm 137:1', 'Ezra 1:11', 'Ezra 8:15', 'Daniel 5:30'],
      significance: "God used the empire that destroyed Jerusalem to free it — Cyrus 'the anointed' (Isaiah 45:1) named 150 years before his birth. The exile that looked like God's absence was the prologue to his deepest promises." },
    { name: 'Susa', lat: 32.189, lon: 48.255, capital: true,
      desc: "Persian winter capital where Esther saved the Jewish people under Xerxes and Nehemiah served as cupbearer to Artaxerxes. Nehemiah heard that Jerusalem's walls lay in ruins and obtained royal letters and timber for their rebuilding. He wept, fasted, and prayed for days before speaking to the king.",
      refs: ['Esther 1:2', 'Nehemiah 1:1', 'Nehemiah 2:1', 'Daniel 8:2'] },
    { name: 'Persepolis', lat: 29.935, lon: 52.891, capital: true,
      desc: "Ceremonial capital of the Achaemenid Persian empire, built by Darius and Xerxes. The three great kings of the return — Cyrus (538 BC), Darius (520 BC), and Artaxerxes (458 and 445 BC) — all issued decrees advancing the restoration. Ezra 6:1–5 records Cyrus's original decree found in the Median archives.",
      refs: ['Ezra 1:1', 'Ezra 6:1', 'Ezra 7:1'] },
    { name: 'Nippur', lat: 32.127, lon: 45.237,
      desc: "A major Babylonian city south of Babylon where many Jewish exiles settled. Business tablets from the Murashu firm (5th century BC) preserve dozens of Hebrew names — evidence that many exiles became prosperous landowners and merchants. When Cyrus's decree came, the majority chose to remain. Those who returned were a faithful remnant.",
      refs: ['Jeremiah 29:5', 'Ezra 2:64', 'Ezekiel 1:1'] },
    { name: 'Jerusalem', lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: "The goal of three great returns. Zerubbabel laid the Temple foundation (538 BC); after Samaritan opposition, it was completed in 516 BC. Ezra returned in 458 BC to restore the law. Nehemiah rebuilt the walls in 52 days in 445 BC; Ezra then read the law publicly and the people wept with joy and renewed the covenant.",
      refs: ['Ezra 3:11', 'Ezra 6:15', 'Nehemiah 6:15', 'Nehemiah 8:8'],
      significance: "The return was real but partial — no Shekinah glory cloud, no Davidic throne, no end to vassal status. Malachi's final word: 'The Lord whom you seek will suddenly come to his temple' (Malachi 3:1). Full restoration awaited One greater than Zerubbabel, Ezra, or Nehemiah." },
    { name: 'Samaria', lat: 32.278, lon: 35.198,
      desc: "The Samaritan community — descendants of Assyrian settlers intermarried with remaining Israelites — opposed both the Temple and wall rebuilding. They wrote to Persian kings to halt the work (Ezra 4:4–5) and Sanballat mocked and threatened Nehemiah. Nehemiah refused their offers and pushed past their resistance.",
      refs: ['Ezra 4:1', 'Ezra 4:4', 'Nehemiah 4:1', 'Nehemiah 6:1'] },
    { name: 'Damascus', lat: COORDS.damascus[0], lon: COORDS.damascus[1],
      desc: "A key waypoint on the Fertile Crescent return route — the ancient road that all traffic followed north from Babylon, then west through Syria and south into Canaan. The returning exiles would have passed through this gateway on Zerubbabel's, Ezra's, and Nehemiah's journeys.",
      refs: ['Ezra 7:9', 'Ezra 8:31'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 14. Between the Testaments ─────────────────────────────────────────── */
function _renderIntertestamental(map) {
  /* Ptolemaic sphere — Egypt and southern Palestine c. 323–198 BC */
  _addRegion([[22.00,24.00],[22.00,37.50],[34.50,37.50],[34.50,24.00]], 'Ptolemaic Sphere', '#9b7000', 0.07);
  /* Seleucid Empire — Syria, Mesopotamia c. 312–64 BC */
  _region('empire-seleucid', -200, [[34.50,34.00],[34.50,50.00],[42.00,50.00],[42.00,34.00]], 'Seleucid Empire',  '#7b5ea7', 0.07);
  /* Hasmonean kingdom at greatest extent c. 100 BC — roughly all of Palestine */
  _addRegion([[30.50,34.20],[30.50,36.50],[33.30,36.50],[33.30,34.20]], 'Hasmonean Kingdom', '#b33c3c', 0.10);
  /* Nabataean kingdom — controls trade routes south and east of Judea */
  _addRegion([[27.50,34.50],[27.50,38.50],[31.00,38.50],[31.00,34.50]], 'Nabataean Kingdom', '#c44d29', 0.08);

  /* Alexander's conquest march through the Levant, 334–323 BC */
  var alexanderRoute = [
    [36.80, 36.17],  /* Issus — decisive battle, Darius III routed, 333 BC */
    [33.271, 35.196], /* Tyre — 7-month siege, city taken, 332 BC */
    [31.502, 34.467], /* Gaza — 2-month siege, falls, 332 BC */
    COORDS.jerusalem, /* Jerusalem — peacefully surrenders */
    COORDS.alexandria, /* Alexandria — founded 331 BC */
    COORDS.damascus, /* Damascus — passes through heading east */
    [36.25,  43.40],  /* Gaugamela — Persia crushed, 331 BC */
    COORDS.babylon  /* Babylon — Alexander dies here, 323 BC */
  ];

  /* Maccabean revolt: Modein → guerrilla campaign → Jerusalem, 167–164 BC */
  var maccabeanRoute = [
    [31.92,  34.98],  /* Modein — Mattathias strikes the first blow, 167 BC */
    [31.97,  35.15],  /* Gophna hills — guerrilla base in the wilderness */
    [31.836, 35.171], /* Beth-Horon — Judas defeats Seleucid force */
    COORDS.jerusalem  /* Jerusalem — Temple recaptured, rededicated, 164 BC */
  ];

  /* Pompey's campaign south through Syria into Judea, 63 BC */
  var pompeyRoute = [
    COORDS.damascus, /* Damascus — Rome establishes Syria as province */
    [32.199, 35.283], /* Shechem — marches south along the ridge */
    COORDS.jerusalem  /* Jerusalem — besieged, Temple Mount entered; independence ends */
  ];

  _addLayer(_routeLine(alexanderRoute, '#4a7fcb', false));
  _addLayer(_routeLine(maccabeanRoute, '#b33c3c', false));
  _addLayer(_routeLine(pompeyRoute,    '#8b1a1a', true));

  var cities = [
    { name: 'Jerusalem', lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1], capital: true,
      desc: "The contested center of the intertestamental period. Antiochus IV Epiphanes desecrated the Temple in 167 BC — erecting an altar to Zeus and sacrificing swine on it (the 'abomination of desolation,' Daniel 11:31). Judas Maccabeus recaptured and rededicated it in 164 BC — the event celebrated as Hanukkah. Pompey entered the Holy of Holies in 63 BC, astonished to find it empty. Herod the Great rebuilt the Temple to vast splendor beginning c. 20 BC.",
      refs: ['Daniel 11:31', 'Matthew 24:15', 'John 10:22', '1 Maccabees 4:36'],
      significance: "Jesus walked in Solomon's Colonnade during Hanukkah (John 10:22) — the very feast commemorating the Temple's reconsecration by the Maccabees. The intertestamental Temple was the backdrop of his entire ministry and the setting of his teaching that he himself is the true temple (John 2:19–21)." },
    { name: 'Alexandria', lat: COORDS.alexandria[0], lon: COORDS.alexandria[1], capital: true,
      desc: "Founded by Alexander in 331 BC, Alexandria became the greatest city of the Hellenistic world. Its Jewish diaspora community — perhaps 100,000 — translated the Hebrew Scriptures into Greek (the Septuagint, c. 250–150 BC). This Greek Old Testament became the Bible quoted by Jesus, Paul, and the apostles throughout the New Testament.",
      refs: ['Acts 6:9', 'Acts 18:24'],
      significance: "The Septuagint (LXX) translated in Alexandria was God's instrument for placing the Hebrew Scriptures in the hands of every literate person in the Roman world. When the apostles proclaimed 'as it is written,' the world could read it. The Greek language and the LXX are two of the most visible providential preparations for the gospel." },
    { name: 'Antioch (Syria)', lat: COORDS.antioch[0], lon: COORDS.antioch[1], capital: true,
      desc: "Capital of the Seleucid Empire and seat of Antiochus IV Epiphanes, who issued the decrees enforcing Hellenization throughout Judea — banning circumcision, Sabbath, and Torah. From here the orders came to desecrate the Temple. A century and a half later, Antioch became the birthplace of the Gentile church and the launching base for Paul's three missionary journeys.",
      refs: ['1 Maccabees 1:44', 'Acts 11:26', 'Acts 13:1'] },
    { name: 'Modein', lat: 31.92, lon: 34.98,
      desc: "Hometown of Mattathias the priest and his five sons — including Judas Maccabeus ('the Hammer'). When a royal officer arrived to enforce Greek sacrifices, Mattathias killed him and destroyed the altar. 'Let everyone who is zealous for the law and supports the covenant come out with me!' (1 Maccabees 2:27). The revolt that preserved Torah-observant Judaism through the darkest Hellenistic pressure began here in 167 BC.",
      refs: ['1 Maccabees 2:1', '1 Maccabees 2:27', 'Hebrews 11:35'],
      significance: "Hebrews 11:35–38 appears to allude to the Maccabean martyrs — 'those who were tortured, refusing to accept release … of whom the world was not worthy.' The faithfulness of these little-known heroes preserved the covenant community from which the Messiah would come." },
    { name: 'Tyre', lat: 33.271, lon: 35.196,
      desc: "Alexander besieged this island fortress for seven months in 332 BC, building a causeway from the mainland (fulfilling Ezekiel's prophecy that its stones would be cast into the sea, Ezekiel 26:12). Its fall broke Phoenician naval power and opened the Levantine coast to Greek culture — Greek cities, Greek gods, Greek language — transforming the world Jesus would be born into.",
      refs: ['Ezekiel 26:12', 'Acts 21:3'] },
    { name: 'Gaza', lat: 31.502, lon: 34.467,
      desc: "Fell to Alexander after a fierce two-month siege in 332 BC. The southern gateway between Egypt and Canaan, Gaza was contested throughout the Hellenistic and Maccabean periods. Centuries later, Philip the evangelist encountered an Ethiopian official on the road from Jerusalem to Gaza — the first African convert (Acts 8:26).",
      refs: ['Acts 8:26', 'Amos 1:6'] },
    { name: 'Damascus', lat: COORDS.damascus[0], lon: COORDS.damascus[1], capital: true,
      desc: "Taken by Alexander without battle in 332 BC and later a Seleucid stronghold. Pompey passed through on his way south in 63 BC to settle the Jewish civil war between Hyrcanus II and Aristobulus II. In the early 1st century AD Damascus was under Nabataean influence — the city from which Paul escaped in a basket after his conversion (2 Corinthians 11:32).",
      refs: ['Acts 9:24', '2 Corinthians 11:32'] },
    { name: 'Petra', lat: 30.328, lon: 35.444, capital: true,
      desc: "Capital of the Nabataean Arab kingdom — master traders who controlled the caravan routes carrying incense, myrrh, and spices from Arabia and the Red Sea to the Mediterranean. The Nabataeans grew powerful precisely during the Maccabean and Hasmonean period. Paul's time in 'Arabia' after his conversion (Galatians 1:17) likely placed him in or near the Nabataean sphere.",
      refs: ['Galatians 1:17', '2 Corinthians 11:32'] },
    { name: 'Joppa', lat: 32.056, lon: 34.754,
      desc: "The Maccabees seized Joppa as a naval base for their campaigns, giving Judea its first sea access since Solomon. Simon Maccabeus fortified it. Later the apostle Peter raised Dorcas here and received the vision that dissolved the food laws and opened the Gentile mission (Acts 10:9–16) — in the house of Simon the tanner, on the harbor that the Maccabees had first taken for Israel.",
      refs: ['1 Maccabees 13:11', 'Acts 9:36', 'Acts 10:9'] },
    { name: 'Issus', lat: 36.80, lon: 36.17,
      desc: "The battle of Issus (333 BC) was Alexander's decisive encounter with Darius III of Persia. Outnumbered and fighting on a narrow coastal plain, Alexander's Macedonian phalanx and cavalry crushed the Persian forces. Darius fled, abandoning his family to Alexander's mercy. The battle opened the entire Levant to Greek conquest within a year.",
      refs: ['Daniel 8:5', 'Daniel 8:7'] },
    { name: 'Babylon', lat: COORDS.babylon[0], lon: COORDS.babylon[1], capital: true,
      desc: "Alexander entered Babylon as a liberator after crushing Persia, and died here in 323 BC at age 32. His sudden death without a clear heir fragmented his empire among his generals (the Diadochi), producing the Ptolemaic and Seleucid kingdoms that would compete for control of Palestine for 150 years — exactly as Daniel's vision of the four kingdoms had foretold (Daniel 8:8; 11:3–4).",
      refs: ['Daniel 8:8', 'Daniel 11:3', 'Daniel 11:4'] }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 15. The Seven Churches of Revelation ───────────────────────────────── */
function _renderSevenChurches(map) {
  /* Roman Empire — the imperial framework in which all seven churches existed */
  _addRegion([
    [35.00,24.00],[35.00,32.00],[42.00,32.00],[42.00,24.00],[35.00,24.00]
  ], 'Roman Empire', '#8b0000', 0.04);
  /* Roman Province of Asia — the specific administrative province of the seven letters */
  _addRegion([
    [36.70,26.00],[36.70,30.50],[40.50,30.50],[40.50,26.00],[36.70,26.00]
  ], 'Province of Asia', '#7b5ea7', 0.08);

  /* Postal circuit from Patmos clockwise through the seven churches of Asia Minor.
     The route follows the actual Roman road network connecting the cities. */
  var circuit = [
    [37.302, 26.548],  /* Patmos — John's place of exile */
    COORDS.ephesus,    /* Ephesus — 1st church */
    [38.420, 27.140],  /* Smyrna — 2nd church */
    [39.121, 27.184],  /* Pergamum — 3rd church */
    [38.920, 27.844],  /* Thyatira — 4th church */
    [38.491, 28.042],  /* Sardis — 5th church */
    [38.343, 28.519],  /* Philadelphia — 6th church */
    [37.826, 29.113]   /* Laodicea — 7th church */
  ];

  _addLayer(_routeLine(circuit, '#7b5ea7', false));

  var cities = [
    { name: 'Patmos', lat: 37.302, lon: 26.548,
      desc: "A small volcanic island in the Aegean, 37 miles southwest of Miletus. John was exiled here 'on account of the word of God and the testimony of Jesus' (Revelation 1:9) — most likely under the Emperor Domitian (c. AD 95). On the Lord's Day he was caught up in the Spirit and received the entire Revelation from the risen Christ.",
      refs: ['Revelation 1:9', 'Revelation 1:10', 'Revelation 1:19'],
      significance: "Rome's tool of silencing became the place where Christ spoke most fully. The island meant to end John's voice became the origin of the church's most read book of hope." },
    { name: 'Ephesus', lat: COORDS.ephesus[0], lon: COORDS.ephesus[1], capital: true,
      desc: "Largest port in the province of Asia, home of the Temple of Artemis (one of the Seven Wonders). Paul spent three years here (Acts 19); John settled here in old age. The risen Christ commends their doctrinal vigilance but rebukes them: 'You have abandoned the love you had at first.' Remove your lamp unless you repent.",
      refs: ['Revelation 2:1', 'Acts 19:10', 'Ephesians 1:1'],
      significance: "'Remember therefore from where you have fallen; repent, and do the works you did at first' (Revelation 2:5). Orthodoxy without love for Christ is an empty shell — the lamp is removed when the heart is gone." },
    { name: 'Smyrna', lat: 38.420, lon: 27.140, capital: true,
      desc: "A prosperous port city with a large Jewish population hostile to the church. The risen Christ — himself dead and alive again — addresses a persecuted church facing poverty and imprisonment with no rebuke, only encouragement: 'Do not fear what you are about to suffer … Be faithful unto death, and I will give you the crown of life.'",
      refs: ['Revelation 2:8', 'Revelation 2:10'],
      significance: "Polycarp, bishop of Smyrna, was martyred here c. AD 155. When ordered to curse Christ he replied: 'Eighty-six years I have served him and he has done me no wrong. How can I blaspheme my King who saved me?' He received the crown." },
    { name: 'Pergamum', lat: 39.121, lon: 27.184, capital: true,
      desc: "The seat of Roman provincial authority and a major center of emperor worship — 'where Satan's throne is.' The church is praised for holding fast even where Antipas was martyred. But they tolerated the teaching of Balaam and the Nicolaitans: compromise with pagan feast tables and immorality. Christ says repent, or 'I will come to you soon and war against them with the sword of my mouth.'",
      refs: ['Revelation 2:12', 'Revelation 2:13', 'Revelation 2:14'] },
    { name: 'Thyatira', lat: 38.920, lon: 27.844,
      desc: "A prosperous trade-guild city. The church is praised for love, faith, service, and endurance — and for growing in these. But they tolerated 'Jezebel,' a false prophetess teaching sexual immorality and food sacrificed to idols — likely through the trade-guild festivals that required pagan meals for economic participation.",
      refs: ['Revelation 2:18', 'Revelation 2:20', 'Acts 16:14'] },
    { name: 'Sardis', lat: 38.491, lon: 28.042,
      desc: "A once-great city whose acropolis was deemed impregnable — yet twice in history captured by surprise when sentries fell asleep at the one unguarded point. The risen Christ applies this history directly: 'You have a reputation for being alive, but you are dead. Wake up!' Only a few had not soiled their garments.",
      refs: ['Revelation 3:1', 'Revelation 3:2', 'Revelation 3:4'],
      significance: "'I will come like a thief, and you will not know at what hour I will come against you' — the allusion to Sardis's famous unguarded moments drives the warning home: spiritual complacency exposes the same vulnerability." },
    { name: 'Philadelphia', lat: 38.343, lon: 28.519,
      desc: "A smaller city that had suffered earthquake damage and Jewish hostility. The risen Christ places no rebuke here. He has set before them 'an open door no one can shut.' Because they kept his word with little strength, he promises to keep them from the coming hour of trial and to write on them permanently the name of his God, his city, and his new name.",
      refs: ['Revelation 3:7', 'Revelation 3:8', 'Revelation 3:10'],
      significance: "'I will write on him the name of my city, the new Jerusalem, which comes down from my God out of heaven' — the weakest church receives the most comprehensive promise of belonging in the eternal city." },
    { name: 'Laodicea', lat: 37.826, lon: 29.113, capital: true,
      desc: "The wealthiest of the seven cities — a banking center, fine black wool producer, and home of a famous eye-salve school. The church reflects its city's self-sufficiency: 'I need nothing.' But Christ sees it as 'wretched, pitiable, poor, blind, and naked.' He stands outside knocking. The rebuke is tender: 'Those whom I love, I reprove and discipline. Be zealous and repent.'",
      refs: ['Revelation 3:14', 'Revelation 3:17', 'Revelation 3:20'],
      significance: "'I counsel you to buy from me gold refined by fire, white garments… and salve to anoint your eyes' — Christ reverses Laodicea's three civic claims to fame: its gold, its black wool, its eye-salve. True wealth, clothing, and sight come only from him." }
  ];

  cities.forEach(function (c) { _addLayer(_cityMarker(c)); });
}

/* ── 16. Jerusalem — The Holy City ──────────────────────────────────────── */
function _renderJerusalem(map) {
  /* Approximate first-century city walls — AD 30 extent, including City of David south */
  _addRegion([
    [31.784, 35.226], /* NW — Jaffa Gate / Herod's Palace area */
    [31.784, 35.238], /* N  — Damascus Gate */
    [31.782, 35.241], /* NE — Bezetha (new quarter beyond Damascus Gate) */
    [31.776, 35.241], /* E  — eastern edge of Temple Mount platform */
    [31.770, 35.240], /* SE — south of Temple Mount, toward City of David */
    [31.768, 35.237], /* S  — Pool of Siloam / City of David southern end */
    [31.768, 35.229], /* SW — Hinnom Valley bend */
    [31.771, 35.226], /* W  — west wall south of Citadel */
    [31.784, 35.226]  /* close */
  ], null, '#4a7fcb', 0.07);

  /* Temple Mount platform — the vast raised esplanade on which the Temple stood */
  _addLayer(L.polygon([
    [31.780, 35.234], [31.780, 35.241],
    [31.776, 35.241], [31.776, 35.234],
    [31.780, 35.234]
  ], {
    color: '#9b7000', weight: 1.5,
    fillColor: '#b8902a', fillOpacity: 0.18,
    interactive: false
  }));

  var sites = [
    { name: 'Temple Mount', lat: 31.7781, lon: 35.2354, capital: true,
      desc: "The 35-acre platform Herod the Great expanded beginning c. 20 BC — one of the greatest construction projects in the ancient world. The Temple itself stood at its center, gleaming with white limestone and gold. Jesus taught daily in Solomon's Colonnade on its eastern edge, drove out the money changers, and declared it a house of prayer. The Romans burned and demolished the Temple in AD 70, just as Jesus foretold — not one stone left on another.",
      refs: ['1 Kings 8:10', 'Matthew 21:13', 'Matthew 24:2', 'John 10:23'],
      significance: "Jesus declared himself greater than the Temple (Matthew 12:6) and identified his own body as the true temple (John 2:19–21). When he died, the Temple veil tore from top to bottom — the barrier between God and humanity removed not by a priest's hand but by the death of the High Priest himself (Matthew 27:51)." },
    { name: 'Western Wall', lat: COORDS.jerusalem[0], lon: COORDS.jerusalem[1],
      desc: "The western retaining wall of Herod's Temple platform — the only surviving structure from the Second Temple. The visible stones weigh hundreds of tonnes; Josephus describes the wall rising over 30 metres above street level. In Jesus's time the full esplanade above it was thronged with pilgrims during the feasts. The disciples marvelled at its stones (Mark 13:1); Jesus replied that every one would be thrown down.",
      refs: ['Mark 13:1', 'Mark 13:2', 'Luke 21:5'] },
    { name: 'Golgotha — Church of the Holy Sepulchre', lat: 31.7784, lon: 35.2296, capital: true,
      desc: "The traditional site of the Crucifixion and Resurrection, venerated since the 4th century and identified by Eusebius and Constantine's mother Helena. The site was outside the first-century city wall (John 19:20) — consistent with the location of a quarry and garden in this area, confirmed by archaeology. The church encloses both the rock of Golgotha and the burial tomb.",
      refs: ['John 19:17', 'John 19:20', 'John 19:41', 'Matthew 27:33'],
      significance: "Here — on whatever square metre of ground it fell — the Son of God was crucified, died, and was buried. And here, on the third day, the tomb was empty: 'He is not here; he has risen' (Matthew 28:6). The Resurrection is the hinge of history: if Christ is risen, everything is transformed; if not, nothing matters (1 Corinthians 15:17–19)." },
    { name: 'Garden Tomb', lat: 31.7843, lon: 35.2300,
      desc: "A site north of Damascus Gate favored by many Protestant Christians since General Gordon identified it in 1883. It features a rock-cut garden tomb near a skull-shaped escarpment (Golgotha = 'place of the skull'). The tomb itself is genuine Iron Age / Second Temple period rock-cut burial — the right type and period for Joseph of Arimathea's tomb. Whether the precise location or not, standing here makes the Gospel narrative viscerally imaginable.",
      refs: ['John 19:41', 'John 20:1', 'Matthew 27:60'] },
    { name: 'Garden of Gethsemane', lat: 31.7794, lon: 35.2398,
      desc: "An olive garden on the lower western slope of the Mount of Olives, across the Kidron Valley from the city. After the Last Supper, Jesus came here with his disciples and prayed with such agony that his sweat became like drops of blood. He was arrested here by a crowd with swords and clubs, led by Judas. His disciples fled into the dark.",
      refs: ['Matthew 26:36', 'Luke 22:44', 'John 18:1', 'Matthew 26:56'],
      significance: "In Gethsemane, the second Adam did what the first Adam refused: he submitted his will entirely to the Father — 'Not my will, but yours, be done' (Luke 22:42). Where Adam grasped at autonomy and lost paradise, Jesus surrendered his will and regained it for us." },
    { name: 'Mount of Olives', lat: 31.7779, lon: 35.2453,
      desc: "The ridge east of Jerusalem from which Jesus surveyed the city and wept over it (Luke 19:41). He delivered the Olivet Discourse here, foretelling the Temple's destruction and his own return (Matthew 24–25). The Triumphal Entry descended from Bethphage on its eastern slope. From this ridge, in full view of his disciples, Jesus was taken up in a cloud at the Ascension (Acts 1:9). Zechariah 14:4 foretells his feet standing here at his return.",
      refs: ['Luke 19:41', 'Matthew 24:3', 'Acts 1:9', 'Zechariah 14:4'] },
    { name: 'Pool of Siloam', lat: 31.7698, lon: 35.2375,
      desc: "The pool at the southern end of Hezekiah's tunnel — a 533-metre channel cut through solid rock c. 701 BC to secure Jerusalem's water supply against Sennacherib's siege (2 Kings 20:20). Jesus sent the man born blind to wash here, and he came back seeing (John 9:7). Excavated in 2004, the pool's first-century date was confirmed. The Siloam Inscription recording the tunnel-cutters meeting underground was found in 1880 — one of the earliest Hebrew inscriptions known.",
      refs: ['John 9:7', '2 Kings 20:20', 'Isaiah 22:9'],
      significance: "The pool's name 'Siloam' means Sent — and Jesus, the one who was sent (John 9:4), gave sight to the blind at this very pool (Isaiah 35:5). The sign in John 9 is a sustained allegory: the Pharisees can see physically but are blind; the once-blind man sees, confesses, and worships." },
    { name: 'Pool of Bethesda', lat: 31.7816, lon: 35.2359,
      desc: "A large double pool north of the Temple Mount near the Sheep Gate, with five colonnaded porches. Here Jesus healed a man who had been paralyzed for 38 years — on the Sabbath, which drew Pharisaic opposition. Excavations confirmed the pool's existence and first-century date, vindicating John's detailed description (often dismissed as theological symbol rather than historical geography).",
      refs: ['John 5:2', 'John 5:5', 'John 5:8'] },
    { name: 'Antonia Fortress (Praetorium)', lat: 31.7801, lon: 35.2349,
      desc: "Herod's massive fortress at the NW corner of the Temple Mount, garrisoning Roman troops who could reach any Temple disturbance in moments. The probable location where Jesus stood before Pilate, was flogged, crowned with thorns, and condemned. Pilate said 'Here is the man!' (John 19:5) — Ecce Homo — at what may have been this location. The soldiers' barracks floor, marked with game-boards, may still be visible below the Convent of Sisters of Zion.",
      refs: ['John 18:28', 'John 19:5', 'Matthew 27:27', 'Acts 21:34'] },
    { name: 'Upper Room / Cenacle', lat: 31.7703, lon: 35.2294,
      desc: "Tradition from the second century places the Last Supper on the southwest hill (Mount Zion). 'I have earnestly desired to eat this Passover with you before I suffer' (Luke 22:15). Jesus took bread, gave thanks, broke it: 'This is my body, given for you. Do this in remembrance of me.' He took the cup: 'This cup that is poured out for you is the new covenant in my blood.' The same upper room may have hosted the 120 disciples at Pentecost (Acts 1:13; 2:1).",
      refs: ['Luke 22:15', 'Luke 22:19', 'Acts 1:13', 'Acts 2:1'],
      significance: "Every celebration of the Lord's Supper since AD 30 has been a repetition of what Jesus did in this room — and every one proclaims his death until he comes (1 Corinthians 11:26). The meal instituted in Jerusalem will be consummated at the Marriage Supper of the Lamb (Revelation 19:9)." },
    { name: 'House of Caiaphas', lat: 31.7710, lon: 35.2278,
      desc: "Tradition places the high priest Caiaphas's house on the eastern slope of Mount Zion. Here the Sanhedrin assembled in the night; Jesus was questioned, struck, and mocked. In the courtyard below, Peter stood by a charcoal fire and denied knowing Jesus three times — and the rooster crowed (Luke 22:61). The church of St. Peter in Gallicantu (Peter of the Crowing Cock) marks the traditional site. A rock-cut prison pit beneath it is plausibly identified as the cell where Jesus waited through the night.",
      refs: ['Matthew 26:57', 'Luke 22:55', 'Luke 22:62', 'John 18:15'],
      significance: "Peter's denial here, and his restoration beside a second charcoal fire after the Resurrection (John 21:9), bracket the Passion story. Three denials answered by three 'Do you love me?' — one for each. The one who failed worst became the first preacher of the Resurrection at Pentecost, fifty days later, in the same city." },
    { name: 'City of David', lat: 31.7719, lon: 35.2366,
      desc: "The original Jebusite stronghold on the narrow ridge south of the Temple Mount, captured by David around 1004 BC. Smaller than imagination suggests — about 50 metres wide — but elevated above the Kidron and fortified by natural ravines. David brought the ark here; Solomon built his palace before the Temple. Hezekiah's tunnel runs beneath this hill. Ongoing excavations since the 1970s have revealed the Iron Age city in remarkable detail.",
      refs: ['2 Samuel 5:7', '2 Samuel 6:12', '1 Kings 3:1', '2 Kings 20:20'] },
    { name: "Herod's Palace / Citadel", lat: 31.7742, lon: 35.2273,
      desc: "Herod's vast palace in the northwest upper city, defended by three towers — Hippicus, Phasael, and Mariamne. This is the alternative candidate for the Praetorium where Pilate rendered judgment, if Pilate used the royal palace rather than the Antonia Fortress. When Jesus was sent to Herod Antipas (who was also staying in Jerusalem for the Passover), the location was likely a Hasmonean palace nearby. The base of Phasael Tower still stands as the 'Tower of David.'",
      refs: ['Luke 23:7', 'John 18:28', 'Acts 23:35'] }
  ];

  sites.forEach(function (c) { _addLayer(_cityMarker(c)); });
}
