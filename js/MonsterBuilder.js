/*###################Chance and array manipulation methods#########################*/
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
function rollArray(array) {
    let shuffled = shuffle(array)
    let index = Math.floor(Math.random() * shuffled.length)
    return `(Roll: ${index}/${shuffled.length}) ${shuffled[index]}`;
};
function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
};
function variableEffect(array, array2, array3,array4) {
    let chance = rollDice(100)
    if (chance > 80) {
        return 'No Special Effect'
    } else if (chance > 60) {
        return searchArray(array3)
    } else if (chance > 40) {
        return "Observing this artwork has caused " + searchArray(array2[0])
    } else if (chance > 20){
        return "If you " + searchArray(array) + ', then ' + searchArray(array2[1])
    } else {
        return `This artwork is cursed. ${searchArray(array4)}`
    }
};
function variableEvent(givenArray, number) {
    let chance = rollDice(100)
    if (chance < 75) {
        return ""
    } else if (number === undefined) {
        return searchArray(givenArray) + " "
    } else {
        return searchArray(givenArray[number]) + ' '
    }
};
function printFrom(array, number, id) {
    let list = shuffle(array).slice(0, number)
    list.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
function modify(number) {
    return Math.floor(number * (.95 + Math.random() * .4))
};
function shuffleSlice(array, number) {
    return shuffle(array).slice(0, number)

};
function loopCountPrintList(array, id) {
    let x = array

    function count(array) {
        a = array
        a.sort();
        var current = null;
        var cnt = 0;
        let final = []
        for (var i = 0; i < a.length; i++) {
            if (a[i] != current) {
                if (cnt > 0) {
                    final.push(cnt + "-" + current);
                }
                current = a[i];
                cnt = 1;
            } else {
                cnt++;
            }
        }
        if (cnt > 0) {
            final.push(cnt + "-" + current);
        }
        return final
    }
    final = count(x);
    final.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
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
function reload() {
    location.reload()
};

/*==================================================================================*/
/*-----------------------------Page Scripts Below-----------------------------------*/
/*==================================================================================*/


let size = [('tiny',4),('small',6),('medium',8),('large',10),('huge',12),('gargantuan',20)]
let type = ['Aberration','Beast','Celestial','Construct','Dragon','Elementals','Fey','Fiend','Giant','Humaniod','Monstrosity','Ooze','Plant','Undead']
let alignment = ['Chaotic','Neutral','Lawful']
let alignment2 = ['Good', 'Neutral','Evil']

let hitDice = []

let speed = []//0-60
let movementTypes = ['Walking','Flying','Burrowing','Climbing','Swimming']

let languages = []
let vulnerabilities = []
let resistance = []
let immunity = []
let senses = ['Blindsight','Darkvision','Tremorsense','Turesight','']  

const challengeRatingParameters = {
    '0'     : { 'PB' : 2, 'AC' : 13, 'HPmin' : 1, 'HPmax' : 6, 'AtBon' : 3, 'DmgPerRoundmin': 0, 'DmgPerRoundmax': 1, 'SaveDC': 13, 'XP' : 10},   
    '1/8'   : { 'PB' : 2, 'AC' : 13, 'HPmin' : 7, 'HPmax' : 35, 'AtBon' : 3, 'DmgPerRoundmin': 2, 'DmgPerRoundmax': 3, 'SaveDC': 13, 'XP' : 25}, 
    '1/4'   : { 'PB' : 2, 'AC' : 13, 'HPmin' : 36, 'HPmax' : 49, 'AtBon' : 3, 'DmgPerRoundmin': 4, 'DmgPerRoundmax': 5, 'SaveDC': 13, 'XP' : 50},
    '1/2'   : { 'PB' : 2, 'AC' : 13, 'HPmin' : 50, 'HPmax' : 70, 'AtBon' : 3, 'DmgPerRoundmin': 6, 'DmgPerRoundmax': 8, 'SaveDC': 13, 'XP' : 100},
    '1'     : { 'PB' : 2, 'AC' : 13, 'HPmin' : 71, 'HPmax' : 85, 'AtBon' : 3, 'DmgPerRoundmin': 9, 'DmgPerRoundmax': 14, 'SaveDC': 13, 'XP' : 200},
    '2'     : { 'PB' : 2, 'AC' : 13, 'HPmin' : 86, 'HPmax' : 100, 'AtBon' : 3, 'DmgPerRoundmin': 15, 'DmgPerRoundmax': 20, 'SaveDC': 13, 'XP' : 450},
    '3'     : { 'PB' : 2, 'AC' : 13, 'HPmin' : 101, 'HPmax' : 115, 'AtBon' : 4, 'DmgPerRoundmin': 21, 'DmgPerRoundmax': 26, 'SaveDC': 13, 'XP' : 700},
    '4'     : { 'PB' : 2, 'AC' : 14, 'HPmin' : 116, 'HPmax' : 130, 'AtBon' : 5, 'DmgPerRoundmin': 27, 'DmgPerRoundmax': 32, 'SaveDC': 14, 'XP' : 1100},
    '5'     : { 'PB' : 3, 'AC' : 15, 'HPmin' : 131, 'HPmax' : 145, 'AtBon' : 6, 'DmgPerRoundmin': 33, 'DmgPerRoundmax': 38, 'SaveDC': 15, 'XP' : 1800},
    '6'     : { 'PB' : 3, 'AC' : 15, 'HPmin' : 145, 'HPmax' : 160, 'AtBon' : 6, 'DmgPerRoundmin': 39, 'DmgPerRoundmax': 44, 'SaveDC': 15, 'XP' : 2300},
    '7'     : { 'PB' : 3, 'AC' : 15, 'HPmin' : 161, 'HPmax' : 175, 'AtBon' : 6, 'DmgPerRoundmin': 45, 'DmgPerRoundmax': 50, 'SaveDC': 15, 'XP' : 2900},
    '8'     : { 'PB' : 3, 'AC' : 16, 'HPmin' : 176, 'HPmax' : 190, 'AtBon' : 7, 'DmgPerRoundmin': 51, 'DmgPerRoundmax': 56, 'SaveDC': 16, 'XP' : 3900},
    '9'     : { 'PB' : 4, 'AC' : 16, 'HPmin' : 191, 'HPmax' : 205, 'AtBon' : 7, 'DmgPerRoundmin': 57, 'DmgPerRoundmax': 62, 'SaveDC': 16, 'XP' : 5000},
    '10'    : { 'PB' : 4, 'AC' : 17, 'HPmin' : 206, 'HPmax' : 220, 'AtBon' : 7, 'DmgPerRoundmin': 63, 'DmgPerRoundmax': 68, 'SaveDC': 16, 'XP' : 5900},
    '11'    : { 'PB' : 4, 'AC' : 17, 'HPmin' : 221, 'HPmax' : 235, 'AtBon' : 8, 'DmgPerRoundmin': 69, 'DmgPerRoundmax': 74, 'SaveDC': 17, 'XP' : 7200},
    '12'    : { 'PB' : 4, 'AC' : 17, 'HPmin' : 236, 'HPmax' : 250, 'AtBon' : 8, 'DmgPerRoundmin': 75, 'DmgPerRoundmax': 80, 'SaveDC': 17, 'XP' : 8400},
    '13'    : { 'PB' : 5, 'AC' : 18, 'HPmin' : 251, 'HPmax' : 265, 'AtBon' : 8, 'DmgPerRoundmin': 81, 'DmgPerRoundmax': 86, 'SaveDC': 18, 'XP' : 10000},
    '14'    : { 'PB' : 5, 'AC' : 18, 'HPmin' : 266, 'HPmax' : 280, 'AtBon' : 8, 'DmgPerRoundmin': 87, 'DmgPerRoundmax': 92, 'SaveDC': 18, 'XP' : 11500},
    '15'    : { 'PB' : 5, 'AC' : 18, 'HPmin' : 281, 'HPmax' : 295, 'AtBon' : 8, 'DmgPerRoundmin': 93, 'DmgPerRoundmax': 98, 'SaveDC': 18, 'XP' : 13000},
    '16'    : { 'PB' : 5, 'AC' : 18, 'HPmin' : 296, 'HPmax' : 310, 'AtBon' : 9, 'DmgPerRoundmin': 99, 'DmgPerRoundmax': 104, 'SaveDC': 18, 'XP' : 15000},
    '17'    : { 'PB' : 6, 'AC' : 19, 'HPmin' : 311, 'HPmax' : 325, 'AtBon' : 10, 'DmgPerRoundmin': 105, 'DmgPerRoundmax': 110, 'SaveDC': 19, 'XP' : 18000},
    '18'    : { 'PB' : 6, 'AC' : 19, 'HPmin' : 326, 'HPmax' : 340, 'AtBon' : 10, 'DmgPerRoundmin': 111, 'DmgPerRoundmax': 116, 'SaveDC': 19, 'XP' : 20000},
    '19'    : { 'PB' : 6, 'AC' : 19, 'HPmin' : 341, 'HPmax' : 355, 'AtBon' : 10, 'DmgPerRoundmin': 117, 'DmgPerRoundmax': 122, 'SaveDC': 19, 'XP' : 22000},
    '20'    : { 'PB' : 6, 'AC' : 19, 'HPmin' : 356, 'HPmax' : 400, 'AtBon' : 10, 'DmgPerRoundmin': 123, 'DmgPerRoundmax': 140, 'SaveDC': 19, 'XP' : 25000},
    '21'    : { 'PB' : 7, 'AC' : 19, 'HPmin' : 401, 'HPmax' : 445, 'AtBon' : 11, 'DmgPerRoundmin': 141, 'DmgPerRoundmax': 158, 'SaveDC': 20, 'XP' : 33000},
    '22'    : { 'PB' : 7, 'AC' : 19, 'HPmin' : 446, 'HPmax' : 490, 'AtBon' : 11, 'DmgPerRoundmin': 159, 'DmgPerRoundmax': 176, 'SaveDC': 20, 'XP' : 41000},
    '23'    : { 'PB' : 7, 'AC' : 19, 'HPmin' : 491, 'HPmax' : 535, 'AtBon' : 11, 'DmgPerRoundmin': 177, 'DmgPerRoundmax': 194, 'SaveDC': 20, 'XP' : 50000},
    '24'    : { 'PB' : 7, 'AC' : 19, 'HPmin' : 536, 'HPmax' : 580, 'AtBon' : 12, 'DmgPerRoundmin': 195, 'DmgPerRoundmax': 212, 'SaveDC': 21, 'XP' : 62000},
    '25'    : { 'PB' : 8, 'AC' : 19, 'HPmin' : 581, 'HPmax' : 625, 'AtBon' : 12, 'DmgPerRoundmin': 213, 'DmgPerRoundmax': 230, 'SaveDC': 21, 'XP' : 75000},
    '26'    : { 'PB' : 8, 'AC' : 19, 'HPmin' : 626, 'HPmax' : 670, 'AtBon' : 12, 'DmgPerRoundmin': 231, 'DmgPerRoundmax': 248, 'SaveDC': 21, 'XP' : 90000},
    '27'    : { 'PB' : 8, 'AC' : 19, 'HPmin' : 671, 'HPmax' : 715, 'AtBon' : 13, 'DmgPerRoundmin': 249, 'DmgPerRoundmax': 266, 'SaveDC': 22, 'XP' : 105000},
    '28'    : { 'PB' : 8, 'AC' : 19, 'HPmin' : 716, 'HPmax' : 760, 'AtBon' : 13, 'DmgPerRoundmin': 267, 'DmgPerRoundmax': 284, 'SaveDC': 22, 'XP' : 120000},
    '29'    : { 'PB' : 9, 'AC' : 19, 'HPmin' : 761, 'HPmax' : 805, 'AtBon' : 13, 'DmgPerRoundmin': 285, 'DmgPerRoundmax': 302, 'SaveDC': 22, 'XP' : 135000},
    '30'    : { 'PB' : 9, 'AC' : 19, 'HPmin' : 806, 'HPmax' : 850, 'AtBon' : 14, 'DmgPerRoundmin': 303, 'DmgPerRoundmax': 320, 'SaveDC': 23, 'XP' : 155000},
}
const challengeRatingRewrite = {
    "CR" : [0,"1/8","1/4","1/2",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
    "PB" : [2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9],
    "AC" : [13,13,13,13,13,13,13,14,15,15,15,16,16,17,17,17,18,18,18,18,19,19,19,19,19,19,19,19,19,19,19,19,19,19],
    "HPmin" : [1,7,36,50,71,86,101,116,131,145,161,176,191,206,221,236,251,266,281,296,311,326,341,356,401,446,491,536,581,626,671,716,761,806],
    "HPmax" : [6,35,49,70,85,100,115,130,145,160,175,190,205,220,235,250,265,280,295,310,325,340,355,400,445,490,535,580,625,670,715,760,805,850],
    "AtBon" : [3,3,3,3,3,3,4,5,6,6,6,7,7,7,8,8,8,8,8,9,10,10,10,10,11,11,11,12,12,12,13,13,13,14],
    "DPRmin" : [0,2,4,6,9,15,21,27,33,39,45,51,57,63,69,75,81,87,93,99,105,111,117,123,141,159,177,195,213,231,249,267,285,303],
    "DPRmax" : [1,3,5,8,14,20,26,32,38,44,50,56,62,68,74,80,86,92,98,104,110,116,122,140,158,176,194,212,230,248,266,284,302,320],
    "SaveDC" : [13,13,13,13,13,13,13,14,15,15,15,16,16,16,17,17,18,18,18,18,19,19,19,19,20,20,20,21,21,21,21,22,22,22,22,23],
    "XP": [10,25,50,100,200,450,700,1100,1800,2300,2900,3900,5000,5900,7200,8400,10000,10000,11500,13000,15000,18000,20000,22000,25000,33000,41000,50000,62000,75000,90000,105000,120000,135000,155000]
}


function skillCalculation(){

}