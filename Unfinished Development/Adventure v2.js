//Chance and array manipulation methods
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
};

function rollDice(number) {
    result = (Math.floor(Math.random() * number))
    return result;
};

function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
};

function variableEvent(Arg) {
    let chance = rollDice(100)
    if (chance < 90) {
        return ""
    } else {
        return Arg
    }
};
// convert numbers to word form
function toWords(s) {
    var th = ['', 'thousand', 'million', 'billion', 'trillion'];
    var dg = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    var tn = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
    var tw = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];


    s = s.toString();
    s = s.replace(/[\, ]/g, '');
    if (s != parseFloat(s)) return 'not a number';
    var x = s.indexOf('.');
    if (x == -1)
        x = s.length;
    if (x > 15)
        return 'too big';
    var n = s.split('');
    var str = '';
    var sk = 0;
    for (var i = 0; i < x; i++) {
        if ((x - i) % 3 == 2) {
            if (n[i] == '1') {
                str += tn[Number(n[i + 1])] + ' ';
                i++;
                sk = 1;
            } else if (n[i] != 0) {
                str += tw[n[i] - 2] + ' ';
                sk = 1;
            }
        } else if (n[i] != 0) { // 0235
            str += dg[n[i]] + ' ';
            if ((x - i) % 3 == 0) str += 'hundred ';
            sk = 1;
        }
        if ((x - i) % 3 == 1) {
            if (sk)
                str += th[(x - i - 1) / 3] + ' ';
            sk = 0;
        }
    }

    if (x != s.length) {
        var y = s.length;
        str += 'point ';
        for (var i = x + 1; i < y; i++)
            str += dg[n[i]] + ' ';
    }
    return str.replace(/\s+/g, ' ');
};
//Reload Page
function reload() {
    location.reload()
};

function printArray(array) {
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
    }
}




let coreAssumptions = {
    "Divinity": [
        ["Distant", "involved", "Present", ],
        ["Loose Pantheon", "Tight Pantheon", "Mystery", "Monotheism", "Dualism", "Animism", "Idealogical", ]
    ],
    "Civilization": [],
    "Age": [],
    "History": [],
    "Magic": [],
    "Races": [],
    "Planes": ["Typical (Elemental, Fey, Shadowfell)", "None - these divisions are mental only, everything exists on this world"]

}
let government = {
    "Autocracy": "",
    "Bureaucracy": "",
    "Confederacy": "",
    "Democracy": "",
    "Dictatorship": "",
    "Feudalism": "",
    "Gerontocracy": "",
    "Hierarchy": "",
    "Magocracy": "",
    "Matriarchy": "",
    "Militocracy": "",
    "Monarchy": "",
    "Oligarchy": "",
    "Patriarchy": "",
    "Meritocracy": "",
    "Plutocracy": "",
    "Republic": "",
    "Satrapy": "",
    "Kleptocracy": "",
    "Theocracy": "",
}
let commerce = {
    "Currency": []
}
let factions = {
    "Roles": [],
    "Goals": [],
    "Magic": [],
}
let laws = {
    "Magic": [],
    "Weapons": [],
}
let startingArea = {
    "Base": [],
    "Region": [],
    "Adventure": [],
}



let wilderness = {
    "Monuments": [],
    "Ruins": [],
    "Settlements": [],
    "Strongholds": [],
    "Oddities": [],
}
let settlements = {
    "Race Relations": [],
    "Ruler Status": [],
    "Notable Traits": [],
    "Renown": [],
    "Calamity": [],
    "Buildings": {
        "Residence": [],
        "Tavern": [],
        "Religious": [],
        "Warehouse": [],
        "Shop": [],
        "Urban Encounter": [],
    }
}