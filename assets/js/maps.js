/* maps.js — Biblical Maps page (Leaflet.js + CartoDB Voyager tiles) */
'use strict';

import { escHtml, READER_URL } from './core.js';
import { wireRefLinks } from './wire.js';

/* ── Tile layer ──────────────────────────────────────────────────────────── */
var TILE_URL  = 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';
var TILE_ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>';

/* ── Map catalogue ───────────────────────────────────────────────────────── */
var MAPS = [
  {
    id:     'holy-land',
    label:  'Holy Land (NT)',
    icon:   '🗺',
    title:  'Palestine in the Time of Jesus',
    sub:    'Galilee, Samaria, Judea, and beyond — c. AD 27–30',
    center: [32.0, 35.3],
    zoom:   8,
    legend: [
      { type: 'dot',  color: '#b00010', label: 'Capital / significant city' },
      { type: 'dot',  color: '#444',    label: 'Town / village' }
    ],
    render: _renderHolyLand
  },
  {
    id:     'paul-journeys',
    label:  "Paul's Journeys",
    icon:   '⛵',
    title:  "Paul's Missionary Journeys",
    sub:    'Three journeys + the voyage to Rome — c. AD 46–60',
    center: [38.5, 24.0],
    zoom:   5,
    legend: [
      { type: 'line', color: '#c44d29', label: '1st journey (AD 46–48)' },
      { type: 'line', color: '#1a5fa8', label: '2nd journey (AD 49–51)' },
      { type: 'line', color: '#3d7a4a', label: '3rd journey (AD 52–57)' },
      { type: 'line', color: '#7b5ea7', label: 'Voyage to Rome (AD 59–60)', dashed: true }
    ],
    render: _renderPaulJourneys
  },
  {
    id:     'exodus',
    label:  'The Exodus',
    icon:   '🏜',
    title:  'The Exodus Route',
    sub:    "Israel's journey from Egypt to Canaan — c. 1446–1406 BC",
    center: [29.8, 33.5],
    zoom:   6,
    legend: [
      { type: 'line', color: '#c44d29', label: 'Exodus route' },
      { type: 'line', color: '#c44d29', label: '40-year wandering', dashed: true }
    ],
    render: _renderExodus
  },
  {
    id:     'divided-kingdom',
    label:  'Divided Kingdom',
    icon:   '👑',
    title:  'Israel & Judah — The Divided Kingdom',
    sub:    'Northern Israel and Southern Judah — 931–586 BC',
    center: [32.0, 35.3],
    zoom:   8,
    legend: [
      { type: 'swatch', color: 'rgba(100,160,220,0.35)', label: 'Israel (Northern Kingdom)' },
      { type: 'swatch', color: 'rgba(210,170,80,0.35)',  label: 'Judah (Southern Kingdom)' },
      { type: 'dot',    color: '#1a5fa8', label: 'Northern capital (Samaria)' },
      { type: 'dot',    color: '#9b2335', label: 'Southern capital (Jerusalem)' }
    ],
    render: _renderDividedKingdom
  },
  {
    id:     'ancient-near-east',
    label:  'Ancient Near East',
    icon:   '🌍',
    title:  'The Ancient Near East',
    sub:    'Egypt, Canaan, Assyria, Babylon, and Persia — the OT world',
    center: [31.0, 40.0],
    zoom:   4,
    legend: [
      { type: 'dot', color: '#b00010', label: 'Major empire capital' },
      { type: 'dot', color: '#444',    label: 'City' }
    ],
    render: _renderAncientNearEast
  },
  /* ── New thematic maps ── */
  {
    id:     'patriarchal-journeys',
    label:  'Patriarchal Journeys',
    icon:   '🐪',
    title:  'Journeys of the Patriarchs',
    sub:    'Abraham, Jacob, and Joseph — c. 2100–1800 BC',
    center: [32.5, 38.0],
    zoom:   5,
    legend: [
      { type: 'line', color: '#c44d29', label: "Abraham's journey" },
      { type: 'line', color: '#1a5fa8', label: "Jacob's journey" },
      { type: 'line', color: '#3d7a4a', label: "Joseph sold to Egypt", dashed: true }
    ],
    render: _renderPatriarchalJourneys
  },
  {
    id:     'conquest',
    label:  'Conquest of Canaan',
    icon:   '⚔',
    title:  'The Conquest of Canaan',
    sub:    "Joshua's southern and northern campaigns — c. 1406–1390 BC",
    center: [31.8, 35.3],
    zoom:   8,
    legend: [
      { type: 'line', color: '#c44d29', label: 'Southern campaign' },
      { type: 'line', color: '#1a5fa8', label: 'Northern campaign' },
      { type: 'dot',  color: '#b00010', label: 'Battle site' },
      { type: 'dot',  color: '#444',    label: 'City / landmark' }
    ],
    render: _renderConquest
  },
  {
    id:     'twelve-tribes',
    label:  'Twelve Tribes',
    icon:   '🏕',
    title:  'The Twelve Tribes of Israel',
    sub:    'Tribal allotments after the conquest — c. 1400–1050 BC',
    center: [32.0, 35.5],
    zoom:   7,
    legend: [
      { type: 'swatch', color: 'rgba(179,60,60,0.4)',   label: 'Judah / Simeon' },
      { type: 'swatch', color: 'rgba(34,85,170,0.4)',   label: 'Ephraim / Manasseh' },
      { type: 'swatch', color: 'rgba(46,140,124,0.4)',  label: 'Galilee tribes (Zebulun, Naphtali, Asher, Issachar)' },
      { type: 'swatch', color: 'rgba(139,92,26,0.4)',   label: 'Transjordan (Gad, Reuben, Manasseh-E)' }
    ],
    render: _renderTwelveTribes
  },
  {
    id:     'judges',
    label:  'Time of the Judges',
    icon:   '🛡',
    title:  'Israel in the Time of the Judges',
    sub:    'Key battles and deliverances — c. 1380–1050 BC',
    center: [32.0, 35.3],
    zoom:   8,
    legend: [
      { type: 'dot', color: '#b00010', label: 'Battle site' },
      { type: 'dot', color: '#7b5ea7', label: 'Judge hometown / key location' },
      { type: 'dot', color: '#444',    label: 'Philistine city' }
    ],
    render: _renderJudges
  },
  {
    id:     'david-kingdom',
    label:  "David's Kingdom",
    icon:   '⭐',
    title:  "David's Kingdom and Military Campaigns",
    sub:    'The united monarchy at its greatest extent — c. 1010–970 BC',
    center: [31.5, 36.0],
    zoom:   6,
    legend: [
      { type: 'swatch', color: 'rgba(180,140,40,0.2)', label: "David's kingdom (core + vassal states)" },
      { type: 'line',   color: '#b00010', label: 'Military campaigns' },
      { type: 'dot',    color: '#b00010', label: 'Capital / key city' }
    ],
    render: _renderDavidKingdom
  },
  {
    id:     'invasions',
    label:  'Assyrian & Babylonian Invasions',
    icon:   '🔥',
    title:  'Assyrian and Babylonian Invasions',
    sub:    'The fall of Samaria (722 BC) and Jerusalem (586 BC)',
    center: [33.0, 39.0],
    zoom:   5,
    legend: [
      { type: 'line', color: '#8b1a1a', label: 'Assyrian invasion — Samaria falls (722 BC)' },
      { type: 'line', color: '#c44d29', label: "Sennacherib's siege — Jerusalem spared (701 BC)" },
      { type: 'line', color: '#1a3a6b', label: 'Babylonian invasions — Jerusalem falls (586 BC)', dashed: true }
    ],
    render: _renderInvasions
  }
];

/* ── State ───────────────────────────────────────────────────────────────── */
var _leaflet  = null;   // active Leaflet map instance
var _overlays = [];     // active layer references for cleanup

/* ── Init ────────────────────────────────────────────────────────────────── */
export function initMapsPage() {
  if (!document.getElementById('maps-container')) return;
  if (!window.L) {
    document.getElementById('maps-map').textContent = 'Map library failed to load. Please check your internet connection.';
    return;
  }
  _buildNav();
  _wireDetailClose();
  _selectMap(MAPS[0]);
}

function _buildNav() {
  var nav = document.getElementById('maps-nav');
  if (!nav) return;
  MAPS.forEach(function (m) {
    var btn = document.createElement('button');
    btn.className  = 'maps-nav-btn';
    btn.dataset.id = m.id;
    btn.innerHTML  = '<span class="maps-nav-icon">' + m.icon + '</span>' + escHtml(m.label);
    btn.addEventListener('click', function () { _selectMap(m); });
    nav.appendChild(btn);
  });
}

function _selectMap(map) {
  /* update nav active state */
  document.querySelectorAll('.maps-nav-btn').forEach(function (b) {
    b.classList.toggle('maps-nav-btn--active', b.dataset.id === map.id);
  });

  /* update title / sub */
  var titleEl = document.getElementById('maps-map-title');
  var subEl   = document.getElementById('maps-map-sub');
  if (titleEl) titleEl.textContent = map.title;
  if (subEl)   subEl.textContent   = map.sub;

  _hideCityDetail();
  _buildLegend(map.legend);

  /* destroy existing map, then (re)init */
  _clearOverlays();
  if (_leaflet) {
    _leaflet.remove();
    _leaflet = null;
  }

  var container = document.getElementById('maps-map');
  _leaflet = L.map(container, { zoomControl: true, attributionControl: true })
               .setView(map.center, map.zoom);

  L.tileLayer(TILE_URL, {
    maxZoom:     19,
    attribution: TILE_ATTR
  }).addTo(_leaflet);

  map.render(_leaflet);
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

/* ── Legend ──────────────────────────────────────────────────────────────── */
function _buildLegend(items) {
  var legend = document.getElementById('maps-legend');
  if (!legend) return;
  if (!items || !items.length) { legend.hidden = true; return; }
  legend.hidden   = false;
  legend.innerHTML = '<p class="maps-legend-title">Legend</p>';
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
    legend.appendChild(row);
  });
}

/* ── City detail panel ───────────────────────────────────────────────────── */
function _showCityDetail(city) {
  var panel  = document.getElementById('maps-city-detail');
  var nameEl = document.getElementById('maps-city-name');
  var descEl = document.getElementById('maps-city-desc');
  var refsEl = document.getElementById('maps-city-refs');
  if (!panel) return;
  if (nameEl) nameEl.textContent = city.name;
  if (descEl) descEl.textContent = city.desc || '';
  if (refsEl) {
    refsEl.innerHTML = '';
    (city.refs || []).forEach(function (ref) {
      var chip = document.createElement('a');
      /* ref class + data-ref so wireRefLinks picks it up for hover previews */
      chip.className = 'ref maps-city-ref-chip';
      chip.setAttribute('data-ref', ref);
      chip.href        = READER_URL + '?ref=' + encodeURIComponent(ref);
      chip.textContent = ref;
      refsEl.appendChild(chip);
    });
    /* wire the new chips so they get the site-wide hover tooltip + modal */
    wireRefLinks(refsEl);
  }
  panel.hidden = false;
  panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function _hideCityDetail() {
  var panel = document.getElementById('maps-city-detail');
  if (panel) panel.hidden = true;
}

function _wireDetailClose() {
  document.addEventListener('click', function (e) {
    if (e.target && e.target.id === 'maps-city-close') _hideCityDetail();
  });
}

/* ═══════════════════════════════════════════════════════════════════════════
   MAP DEFINITIONS
   ═══════════════════════════════════════════════════════════════════════════ */

/* ── 1. Holy Land — Palestine in the time of Jesus ───────────────────────── */
function _renderHolyLand(map) {
  var cities = [
    { name: 'Jerusalem',         lat: 31.7767, lon: 35.2345, capital: true,
      desc: 'The city of the great King. Site of the Temple, the Last Supper, Crucifixion, Resurrection, and Pentecost.',
      refs: ['Psalm 48:1', 'Luke 19:41', 'Acts 2:1', 'Revelation 21:2'] },
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
      refs: ['John 11:1', 'John 11:35', 'Luke 24:50'] },
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
  /* Routes — lat/lon waypoints */
  var journey1 = [
    [36.20, 36.16],  /* Antioch (Syria) */
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
    [36.20, 36.16]   /* Antioch (return) */
  ];

  var journey2 = [
    [36.20, 36.16],  /* Antioch */
    [37.35, 33.40],  /* Derbe */
    [37.58, 32.34],  /* Lystra */
    [39.77, 26.12],  /* Troas */
    [40.49, 25.52],  /* Samothrace */
    [40.84, 24.71],  /* Neapolis */
    [41.01, 24.28],  /* Philippi */
    [40.64, 22.94],  /* Thessalonica */
    [40.36, 22.55],  /* Berea */
    [37.98, 23.73],  /* Athens */
    [37.91, 22.88],  /* Corinth */
    [37.94, 27.34],  /* Ephesus */
    [32.50, 34.90],  /* Caesarea Maritima */
    [31.78, 35.23],  /* Jerusalem */
    [36.20, 36.16]   /* Antioch */
  ];

  var journey3 = [
    [36.20, 36.16],  /* Antioch */
    [38.50, 31.00],  /* Galatia / Phrygia region */
    [37.94, 27.34],  /* Ephesus */
    [40.64, 22.94],  /* Thessalonica */
    [37.91, 22.88],  /* Corinth */
    [40.64, 22.94],  /* Macedonia again */
    [39.77, 26.12],  /* Troas */
    [37.52, 27.25],  /* Miletus */
    [36.54, 36.16],  /* Tyre */
    [32.50, 34.90],  /* Caesarea Maritima */
    [31.78, 35.23]   /* Jerusalem */
  ];

  var romeVoyage = [
    [31.78, 35.23],  /* Jerusalem */
    [32.50, 34.90],  /* Caesarea */
    [36.30, 30.55],  /* Myra */
    [36.89, 27.29],  /* Rhodes (approx sea route) */
    [34.92, 25.30],  /* Crete (Fair Havens) */
    [35.94, 14.38],  /* Malta */
    [37.08, 15.27],  /* Syracuse, Sicily */
    [40.83, 14.25],  /* Puteoli */
    [41.90, 12.50]   /* Rome */
  ];

  _addLayer(_routeLine(journey1,  '#c44d29', false));
  _addLayer(_routeLine(journey2,  '#1a5fa8', false));
  _addLayer(_routeLine(journey3,  '#3d7a4a', false));
  _addLayer(_routeLine(romeVoyage,'#7b5ea7', true));

  var cities = [
    { name: 'Antioch (Syria)', lat: 36.20, lon: 36.16, capital: true,
      desc: 'The first great Gentile church; the sending base for all three missionary journeys. Believers were first called "Christians" here.',
      refs: ['Acts 11:26', 'Acts 13:1', 'Acts 14:27'] },
    { name: 'Ephesus',        lat: 37.94, lon: 27.34, capital: true,
      desc: "Paul spent three years here — his longest stay. From Ephesus the word of God spread throughout the province of Asia. He wrote 1 Corinthians here.",
      refs: ['Acts 19:10', 'Acts 20:31', 'Ephesians 1:1', 'Revelation 2:1'] },
    { name: 'Corinth',        lat: 37.91, lon: 22.88, capital: true,
      desc: "Paul spent 18 months in this cosmopolitan port city. His longest-sustained letters address its troubled church. He wrote Romans from here.",
      refs: ['Acts 18:1', '1 Corinthians 1:1', 'Romans 16:23'] },
    { name: 'Athens',         lat: 37.98, lon: 23.73,
      desc: "Paul preached on the Areopagus, declaring to philosophers the identity of the unknown God and proclaiming the resurrection — the scandal of the gospel.",
      refs: ['Acts 17:22', 'Acts 17:31'] },
    { name: 'Thessalonica',   lat: 40.64, lon: 22.94,
      desc: "Paul planted a church here in three Sabbaths before being driven out. He wrote 1 & 2 Thessalonians to encourage this persecuted congregation.",
      refs: ['Acts 17:1', '1 Thessalonians 1:6'] },
    { name: 'Philippi',       lat: 41.01, lon: 24.28,
      desc: "The first church planted in Europe, on Paul's second journey. Lydia, a seller of purple, was its first convert. Paul wrote the most joyful of his letters here.",
      refs: ['Acts 16:12', 'Philippians 1:1', 'Acts 16:14'] },
    { name: 'Rome',           lat: 41.90, lon: 12.50, capital: true,
      desc: "Paul arrived under house arrest and spent two years preaching the kingdom of God to all who came — including members of Caesar's household. He was martyred here.",
      refs: ['Acts 28:30', 'Philippians 4:22', 'Romans 1:1'] },
    { name: 'Troas',          lat: 39.77, lon: 26.12,
      desc: "Paul received the Macedonian vision here — 'Come over to Macedonia and help us.' The gospel crossed into Europe from this Asian port.",
      refs: ['Acts 16:9', 'Acts 20:6'] },
    { name: 'Caesarea',       lat: 32.50, lon: 34.90,
      desc: "Paul was imprisoned here for two years under Felix and Festus before appealing to Caesar, which led to his voyage to Rome.",
      refs: ['Acts 23:33', 'Acts 25:12'] },
    { name: 'Jerusalem',      lat: 31.78, lon: 35.23, capital: true,
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
      refs: ['Exodus 14:21', 'Exodus 14:28', 'Exodus 15:1'] },
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
      refs: ['Exodus 19:1', 'Exodus 20:1', 'Exodus 40:34', 'Galatians 4:25'] },
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
    { name: 'Jerusalem',         lat: 31.777, lon: 35.234, capital: true,
      desc: "Capital of the southern kingdom of Judah, the city of David and the site of the Temple. Survived Assyria's siege (701 BC) but fell to Babylon in 586 BC.",
      refs: ['2 Samuel 5:7', '1 Kings 14:21', '2 Kings 25:9'] },
    { name: 'Dan',               lat: 33.248, lon: 35.651,
      desc: "Jeroboam placed a golden calf here to stop Israel from going to Jerusalem to worship — 'These are your gods, O Israel, who brought you up out of Egypt.'",
      refs: ['1 Kings 12:28', '1 Kings 12:29'] },
    { name: 'Bethel',            lat: 31.927, lon: 35.224,
      desc: "The second golden calf shrine of Jeroboam. Condemned by Amos as 'Beth Aven' (house of wickedness). The old site of Jacob's vision became a center of apostate worship.",
      refs: ['1 Kings 12:29', 'Amos 4:4', 'Amos 5:5'] },
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
    { name: 'Jerusalem',        lat: 31.777, lon: 35.234, capital: true,
      desc: "Center of Israel's covenant worship. The Temple stood here from Solomon (966 BC) to Nebuchadnezzar's destruction (586 BC).",
      refs: ['Psalm 48:2', '2 Samuel 5:7', '1 Kings 8:13'] },
    { name: 'Damascus',         lat: 33.514, lon: 36.276, capital: true,
      desc: "Capital of the Aramean kingdom. A perpetual rival and ally of Israel. Paul was converted on the road here; Elisha sent Naaman here to be healed.",
      refs: ['2 Samuel 8:6', 'Amos 1:3', 'Acts 9:2', '2 Kings 5:1'] },
    { name: 'Sidon',            lat: 33.564, lon: 35.371,
      desc: "Leading Phoenician city, older than Tyre. Jezebel was a Sidonian princess. Elijah fled to Zarephath, near Sidon, and was sustained by a widow.",
      refs: ['1 Kings 17:9', 'Matthew 15:21', '1 Kings 16:31'] },
    { name: 'Tyre',             lat: 33.271, lon: 35.196,
      desc: "Premier Phoenician port. Hiram of Tyre provided cedar and craftsmen for Solomon's Temple. Ezekiel's longest oracle against a foreign nation targets Tyre.",
      refs: ['1 Kings 5:1', 'Ezekiel 28:1', 'Amos 1:9'] },
    { name: 'Nineveh',         lat: 36.359, lon: 43.160, capital: true,
      desc: "Capital of the Assyrian empire at its height. God sent Jonah here with a message of repentance — they repented. Nahum prophesied its destruction in 612 BC.",
      refs: ['Jonah 3:3', 'Nahum 1:1', 'Zephaniah 2:13'] },
    { name: 'Babylon',          lat: 32.536, lon: 44.421, capital: true,
      desc: "Capital of Nebuchadnezzar's empire. Jerusalem fell to him in 586 BC; the exiles were brought here. Daniel served in its court. Revelation uses it as a symbol of all godless empire.",
      refs: ['Daniel 1:1', 'Psalm 137:1', 'Isaiah 13:19', 'Revelation 17:5'] },
    { name: 'Ur of the Chaldeans', lat: 30.963, lon: 46.104,
      desc: "Abraham's homeland in southern Mesopotamia — a sophisticated urban center. God called him out of this world to go to an unknown land, trusting only the promise.",
      refs: ['Genesis 11:31', 'Acts 7:2', 'Hebrews 11:8'] },
    { name: 'Susa',             lat: 32.189, lon: 48.255, capital: true,
      desc: "Winter capital of the Persian empire. Esther and Mordecai lived here under Xerxes. Nehemiah served here as cupbearer before returning to rebuild Jerusalem.",
      refs: ['Esther 1:2', 'Nehemiah 1:1', 'Daniel 8:2'] },
    { name: 'Haran',            lat: 36.863, lon: 39.020,
      desc: "Abraham's family stopped here after leaving Ur; Terah died here. Jacob fled here from Esau and served Laban for twenty years. A major Assyrian trade center.",
      refs: ['Genesis 11:31', 'Genesis 28:10', 'Acts 7:4'] },
    { name: 'Carchemish',       lat: 36.844, lon: 38.006,
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
    [36.863, 39.020],  /* Haran — family stops; Terah dies */
    [32.199, 35.283],  /* Shechem — first altar in Canaan (Gen 12:6) */
    [31.927, 35.224],  /* Bethel — second altar */
    [30.780, 31.820],  /* Egypt — famine journey */
    [31.533, 35.096],  /* Hebron — chief residence; Machpelah burial cave */
    [31.777, 35.234],  /* Moriah — binding of Isaac (2 Chr 3:1) */
    [31.252, 34.792]   /* Beersheba — covenant with Abimelech */
  ];

  /* Jacob: Beersheba → Bethel → Haran → Mahanaim / Peniel → Shechem → Egypt */
  var jacobRoute = [
    [31.252, 34.792],  /* Beersheba — flees Esau */
    [31.927, 35.224],  /* Bethel — Jacob's ladder; God reaffirms covenant */
    [36.863, 39.020],  /* Haran — serves Laban twenty years */
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
      refs: ['Genesis 11:31', 'Acts 7:2', 'Hebrews 11:8'] },
    { name: 'Haran (Paddan-Aram)', lat: 36.863, lon: 39.020,
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
    { name: 'Moriah (Jerusalem)', lat: 31.777, lon: 35.234,
      desc: "God commanded Abraham to sacrifice Isaac on 'one of the mountains of Moriah.' As the knife was raised, the Angel of the LORD provided a ram caught in a thicket — a vivid type of Christ's substitution. 2 Chronicles 3:1 identifies Moriah as the site of Solomon's Temple.",
      refs: ['Genesis 22:2', 'Genesis 22:13', '2 Chronicles 3:1', 'John 1:29'] },
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
      refs: ['Joshua 6:20', 'Joshua 6:25', 'Hebrews 11:30'] },
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

  var tribes = [
    /* ── West of Jordan ── */
    { name: 'Judah', fillColor: '#b33c3c', fillOpacity: 0.28, color: '#b33c3c',
      coords: [
        [31.88, 35.10], [31.88, 35.40], [31.65, 35.55],
        [31.30, 35.40], [31.00, 35.10], [30.75, 34.80],
        [30.75, 34.40], [31.10, 34.50], [31.55, 34.70],
        [31.80, 34.90], [31.88, 35.10]
      ],
      desc: 'Largest tribe; includes Jerusalem, Bethlehem, and Hebron. "The scepter shall not depart from Judah … until Shiloh comes" (Gen 49:10). From Judah came David, and ultimately Jesus the Messiah, the Lion of the tribe of Judah.',
      refs: ['Joshua 15:1', 'Genesis 49:10', 'Revelation 5:5'] },

    { name: 'Simeon', fillColor: '#c9921a', fillOpacity: 0.28, color: '#c9921a',
      coords: [
        [31.30, 34.50], [31.40, 35.00], [31.10, 35.00],
        [30.75, 34.80], [30.75, 34.40], [31.10, 34.30], [31.30, 34.50]
      ],
      desc: "Allotted within Judah's territory in the far south around Beersheba. Jacob prophesied they would be 'scattered in Israel' (Gen 49:7). As Judah grew powerful, Simeon was absorbed into it — they had no independent destiny.",
      refs: ['Joshua 19:1', 'Genesis 49:7', '1 Chronicles 4:24'] },

    { name: 'Benjamin', fillColor: '#4a8c3f', fillOpacity: 0.28, color: '#4a8c3f',
      coords: [
        [32.00, 35.10], [32.00, 35.40],
        [31.88, 35.40], [31.88, 35.10], [32.00, 35.10]
      ],
      desc: 'Small but strategically placed between Ephraim and Judah. Jerusalem sat on its border. Saul, the first king of Israel, was a Benjaminite — as was Paul the apostle.',
      refs: ['Joshua 18:11', 'Judges 20:4', 'Romans 11:1'] },

    { name: 'Dan (original)', fillColor: '#cc5522', fillOpacity: 0.28, color: '#cc5522',
      coords: [
        [32.05, 34.80], [32.10, 35.10],
        [31.90, 35.10], [31.80, 34.90], [32.05, 34.80]
      ],
      desc: "Originally allotted a coastal strip west of Benjamin and Ephraim. Dan was unable to conquer their territory — 'the Amorites pressed the Danites back into the hill country.' Most of the tribe migrated north to Laish (renamed Dan).",
      refs: ['Joshua 19:40', 'Judges 1:34', 'Judges 13:2'] },

    { name: 'Ephraim', fillColor: '#2255aa', fillOpacity: 0.28, color: '#2255aa',
      coords: [
        [32.20, 35.50], [32.20, 35.10], [32.10, 34.90],
        [31.90, 34.90], [32.00, 35.10], [32.00, 35.40], [32.20, 35.50]
      ],
      desc: "Joseph's younger son received Jacob's greater blessing (Gen 48:19). The Tabernacle rested at Shiloh in Ephraim for ~300 years. After the kingdom split, Ephraim dominated the northern tribes.",
      refs: ['Joshua 16:5', 'Genesis 48:20', 'Hosea 5:3'] },

    { name: 'Manasseh (West)', fillColor: '#5c3d9e', fillOpacity: 0.28, color: '#5c3d9e',
      coords: [
        [32.60, 35.55], [32.60, 35.00], [32.40, 34.90],
        [32.20, 34.90], [32.20, 35.10], [32.20, 35.50], [32.60, 35.55]
      ],
      desc: "Half of Manasseh — Joseph's firstborn — received land north of Ephraim. The daughters of Zelophehad successfully petitioned Moses for an inheritance (Num 27:7) — God affirmed their case, establishing a legal precedent.",
      refs: ['Joshua 17:1', 'Numbers 27:7', 'Joshua 17:3'] },

    { name: 'Issachar', fillColor: '#2e8c7c', fillOpacity: 0.28, color: '#2e8c7c',
      coords: [
        [32.70, 35.55], [32.60, 35.55], [32.40, 35.50],
        [32.40, 35.75], [32.70, 35.80], [32.70, 35.55]
      ],
      desc: "Settled in the fertile Jezreel Valley. Jacob's blessing: 'a strong donkey crouching between the sheepfolds' — implying agricultural contentment. They provided warriors for David who 'understood the times' (1 Chr 12:32).",
      refs: ['Joshua 19:17', 'Genesis 49:14', '1 Chronicles 12:32'] },

    { name: 'Zebulun', fillColor: '#3d7a5c', fillOpacity: 0.28, color: '#3d7a5c',
      coords: [
        [33.00, 35.50], [32.90, 35.10], [32.60, 35.10],
        [32.60, 35.55], [32.80, 35.60], [33.00, 35.50]
      ],
      desc: "Lower Galilee tribe. Isaiah prophesied: 'The land of Zebulun … the people dwelling in darkness have seen a great light' (Isa 9:1) — fulfilled when Jesus based his ministry in Capernaum in Zebulun territory.",
      refs: ['Joshua 19:10', 'Isaiah 9:1', 'Matthew 4:15'] },

    { name: 'Asher', fillColor: '#c05c7a', fillOpacity: 0.28, color: '#c05c7a',
      coords: [
        [33.25, 35.10], [33.10, 34.90], [32.90, 34.80],
        [32.80, 34.85], [32.90, 35.10], [33.00, 35.10], [33.25, 35.10]
      ],
      desc: "Coastal tribe bordering Phoenicia in the north. Jacob: 'Asher's food shall be rich; he shall yield royal delicacies' — olive groves and coastal fertility. The prophetess Anna, who greeted the infant Jesus in the Temple, was from Asher (Luke 2:36).",
      refs: ['Joshua 19:24', 'Genesis 49:20', 'Luke 2:36'] },

    { name: 'Naphtali', fillColor: '#1a6699', fillOpacity: 0.28, color: '#1a6699',
      coords: [
        [33.35, 35.60], [33.20, 35.20], [33.10, 35.10],
        [33.00, 35.50], [33.10, 35.80], [33.25, 35.85], [33.35, 35.60]
      ],
      desc: "Upper Galilee tribe. Barak was from Kedesh-Naphtali. Capernaum — Jesus's ministry headquarters — lay in Naphtali, fulfilling Isaiah's 'great light' prophecy to the despised northern region.",
      refs: ['Joshua 19:32', 'Genesis 49:21', 'Matthew 4:13'] },

    { name: 'Dan (northern)', fillColor: '#aa3311', fillOpacity: 0.26, color: '#aa3311',
      coords: [
        [33.28, 35.55], [33.22, 35.85],
        [33.42, 35.92], [33.52, 35.68], [33.28, 35.55]
      ],
      desc: "After failing to hold their western territory, most of Dan migrated north and conquered the peaceful city of Laish, renaming it Dan. Jeroboam erected one of his two golden calves here.",
      refs: ['Judges 18:27', '1 Kings 12:29', 'Joshua 19:47'] },

    /* ── East of Jordan (Transjordan) ── */
    { name: 'Reuben', fillColor: '#8b5c1a', fillOpacity: 0.28, color: '#8b5c1a',
      coords: [
        [31.80, 35.55], [31.80, 36.20], [31.30, 36.00],
        [31.10, 35.65], [31.40, 35.55], [31.80, 35.55]
      ],
      desc: "Jacob's firstborn, who forfeited his birthright through sin. The tribe settled east of the Dead Sea on the Moabite plateau. Moses challenged them: 'Shall your brothers go to war while you sit here?' (Num 32:6). Jacob's word: 'unstable as water, you shall not excel.'",
      refs: ['Joshua 13:15', 'Numbers 32:1', 'Genesis 49:4'] },

    { name: 'Gad', fillColor: '#6b4c2a', fillOpacity: 0.28, color: '#6b4c2a',
      coords: [
        [31.80, 35.55], [32.40, 35.75],
        [32.40, 36.30], [31.80, 36.20], [31.80, 35.55]
      ],
      desc: "Settled in Gilead (central Transjordan). Jacob: 'Raiders shall raid Gad, but he shall raid at their heels.' Jephthah the judge was a Gadite. The tribe pledged to cross the Jordan and fight with their brothers until the entire land was conquered.",
      refs: ['Joshua 13:24', 'Genesis 49:19', 'Judges 11:1'] },

    { name: 'Manasseh (East)', fillColor: '#7c5c9e', fillOpacity: 0.28, color: '#7c5c9e',
      coords: [
        [32.40, 35.75], [32.90, 35.65], [33.10, 35.80],
        [33.10, 36.50], [32.80, 36.60], [32.40, 36.30], [32.40, 35.75]
      ],
      desc: "Half of Manasseh settled in Bashan (north Transjordan) after defeating Og, one of the last Rephaim giants. The region was renowned for its powerful cattle — 'cows of Bashan' became prophetic shorthand for complacent luxury (Amos 4:1).",
      refs: ['Joshua 13:29', 'Deuteronomy 3:1', 'Numbers 32:39', 'Amos 4:1'] }
  ];

  /* Render each tribal territory as a filled polygon; click for tribe info */
  tribes.forEach(function (t) {
    var poly = L.polygon(t.coords, {
      color:       t.color,
      weight:      1.5,
      fillColor:   t.fillColor,
      fillOpacity: t.fillOpacity,
      opacity:     0.85
    });
    poly.bindTooltip(t.name, { sticky: true, direction: 'center' });
    /* Reuse the city-detail panel for tribe info */
    poly.on('click', function () {
      _showCityDetail({ name: t.name, desc: t.desc, refs: t.refs });
    });
    _addLayer(poly);
  });

  /* Reference cities marked on the tribal map */
  var cities = [
    { name: 'Jerusalem', lat: 31.777, lon: 35.234, capital: true,
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
      refs: ['1 Samuel 1:3', '1 Samuel 4:3', 'Psalm 78:60', 'Jeremiah 7:12'] },

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
    [32.50, 34.90],   /* northern coast */
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
    [31.777, 35.234],  /* Jerusalem */
    [31.750, 35.150],  /* Valley of Rephaim (SW of Jerusalem) */
    [31.729, 34.853],  /* Gath region — Philistine heartland */
    [31.600, 34.700]   /* coastal plain */
  ];

  var moabCampaign = [
    [31.777, 35.234],  /* Jerusalem */
    [31.600, 35.600],  /* Judean desert east */
    [31.500, 36.000]   /* Moab highlands (2 Sam 8:2) */
  ];

  var ammonCampaign = [
    [31.777, 35.234],  /* Jerusalem */
    [32.100, 35.700],  /* Jordan crossing northward */
    [31.955, 35.945]   /* Rabbah (Ammon — modern Amman) */
  ];

  var aramCampaign = [
    [31.777, 35.234],  /* Jerusalem */
    [32.500, 35.500],  /* northward through Galilee */
    [33.514, 36.276]   /* Damascus — garrisons placed (2 Sam 8:6) */
  ];

  var edomCampaign = [
    [31.777, 35.234],  /* Jerusalem */
    [31.100, 35.300],  /* Valley of Salt — 18,000 Edomites defeated */
    [30.500, 35.000]   /* Edom highlands — garrisons placed throughout */
  ];

  _addLayer(_routeLine(philistineCampaign, '#b00010', false));
  _addLayer(_routeLine(moabCampaign,       '#b00010', false));
  _addLayer(_routeLine(ammonCampaign,      '#b00010', false));
  _addLayer(_routeLine(aramCampaign,       '#b00010', false));
  _addLayer(_routeLine(edomCampaign,       '#b00010', false));

  var cities = [
    { name: 'Jerusalem', lat: 31.777, lon: 35.234, capital: true,
      desc: "David captured the Jebusite stronghold of Zion and made it his capital. He brought the ark here with dancing and great rejoicing. His heart burned to build a permanent Temple — but God gave him a greater gift: the Davidic covenant. 'I will raise up your offspring … and establish the throne of his kingdom forever' (2 Sam 7:12–13).",
      refs: ['2 Samuel 5:7', '2 Samuel 6:12', '2 Samuel 7:12', '2 Samuel 7:16'] },
    { name: 'Hebron (David crowned)', lat: 31.533, lon: 35.096,
      desc: "David reigned over Judah alone here for seven and a half years while the house of Saul held the north. After Ish-bosheth's assassination, the elders of all Israel came to Hebron and anointed David king over all Israel. The nation was finally unified.",
      refs: ['2 Samuel 2:4', '2 Samuel 5:5', '2 Samuel 5:3'] },
    { name: 'Damascus (Aram conquered)', lat: 33.514, lon: 36.276,
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
  /* ── Assyrian conquest of northern Israel, 722 BC (Sargon II) ── */
  var assyrianRoute = [
    [36.359, 43.160],  /* Nineveh — Assyrian capital */
    [36.844, 38.006],  /* Carchemish — Euphrates crossing point */
    [35.133, 36.750],  /* Hamath — gateway into Canaan / Syria */
    [33.514, 36.276],  /* Damascus — fell to Tiglath-Pileser III in 732 BC */
    [32.278, 35.198]   /* Samaria — fell after three-year siege, 722 BC */
  ];

  /* ── Sennacherib's western campaign, 701 BC ── */
  var sennacheribRoute = [
    [36.359, 43.160],  /* Nineveh */
    [36.844, 38.006],  /* Carchemish */
    [34.000, 36.300],  /* Hamath / Riblah — staging area */
    [31.560, 34.847],  /* Lachish — major siege (depicted in palace reliefs) */
    [31.777, 35.234]   /* Jerusalem — besieged but miraculously spared (2 Kgs 19) */
  ];

  /* ── Babylonian campaigns, 605–586 BC (Nebuchadnezzar) ── */
  var babylonianRoute = [
    [32.536, 44.421],  /* Babylon */
    [35.000, 43.500],  /* northwest march along the Euphrates */
    [36.844, 38.006],  /* Carchemish — decisive battle 605 BC; Egypt routed */
    [35.133, 36.750],  /* Hamath / Syria */
    [33.514, 36.276],  /* Damascus */
    [31.777, 35.234]   /* Jerusalem — 605 BC: Daniel; 597 BC: Jehoiachin; 586 BC: city destroyed */
  ];

  _addLayer(_routeLine(assyrianRoute,    '#8b1a1a', false));
  _addLayer(_routeLine(sennacheribRoute, '#c44d29', false));
  _addLayer(_routeLine(babylonianRoute,  '#1a3a6b', true));

  var cities = [
    { name: 'Nineveh', lat: 36.359, lon: 43.160, capital: true,
      desc: "Capital of the Assyrian empire. Under Sargon II it conquered Samaria (722 BC). Under Sennacherib it besieged Jerusalem (701 BC) but was repelled by the Angel of the LORD. Jonah preached here; the city repented. Nahum later prophesied its destruction — in 612 BC Nineveh fell to the Babylonians and Medes exactly as foretold.",
      refs: ['2 Kings 17:6', '2 Kings 19:36', 'Nahum 1:1', 'Jonah 3:3'] },
    { name: 'Carchemish', lat: 36.844, lon: 38.006,
      desc: "The great Euphrates crossing. In 605 BC Nebuchadnezzar crushed Pharaoh Neco here — the battle that handed the ancient Near East to Babylon. Jeremiah 46:2 marks it as the beginning of the end for Judah. Daniel's first deportation followed within that year.",
      refs: ['Jeremiah 46:2', '2 Chronicles 35:20', 'Daniel 1:1'] },
    { name: 'Damascus', lat: 33.514, lon: 36.276, capital: true,
      desc: "Capital of Aram. Fell to Tiglath-Pileser III of Assyria in 732 BC; King Rezin was executed. Isaiah had prophesied: 'Damascus will cease to be a city and will become a heap of ruins' (Isa 17:1) — fulfilled within his generation.",
      refs: ['2 Kings 16:9', 'Isaiah 17:1', 'Isaiah 8:4'] },
    { name: 'Samaria', lat: 32.278, lon: 35.198, capital: true,
      desc: "Capital of the northern kingdom. After a three-year siege, Sargon II captured Samaria in 722 BC and deported 27,290 Israelites to Assyria, replacing them with foreign settlers. The ten tribes were scattered — fulfilling generations of warnings from Amos, Hosea, and Micah.",
      refs: ['2 Kings 17:5', '2 Kings 17:6', '2 Kings 17:23', 'Hosea 13:16'] },
    { name: 'Lachish', lat: 31.560, lon: 34.847, capital: true,
      desc: "Sennacherib personally directed the siege from his camp here, the conquest immortalized in massive palace reliefs in Nineveh. Archaeology has uncovered a clear destruction layer from 701 BC. Sennacherib boasted of trapping Hezekiah 'like a bird in a cage' — conspicuously admitting he never took Jerusalem.",
      refs: ['2 Kings 18:14', '2 Kings 19:8', 'Isaiah 36:2', 'Micah 1:13'] },
    { name: 'Jerusalem', lat: 31.777, lon: 35.234, capital: true,
      desc: "In 701 BC Sennacherib surrounded Jerusalem. Hezekiah spread his letter before the LORD and prayed; Isaiah prophesied; the Angel of the LORD killed 185,000 Assyrians in a night — Jerusalem was spared. But in 586 BC, after a century of prophetic warning, Nebuchadnezzar broke the walls, burned the Temple, and marched the survivors to Babylon. 'How lonely sits the city that was full of people!' (Lam 1:1).",
      refs: ['2 Kings 19:35', '2 Kings 25:9', 'Lamentations 1:1', 'Jeremiah 52:13'] },
    { name: 'Babylon', lat: 32.536, lon: 44.421, capital: true,
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
