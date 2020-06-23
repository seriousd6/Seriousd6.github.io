//chance and array searching methods
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
};

function rollDice(number) {
    result = (Math.floor(Math.random() * number))
    return result;
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

function modify(number) {
    return Math.floor(number * (.85 + Math.random() * .4))
};

function variableEvent(array, number) {
    let chance = rollDice(100)
    if (chance < 75) {
        return ""
    } else if (number === "undefined") {
        return searchArray(array) + " "
    } else {
        return searchArray(array[number]) + ' '
    }


};

function variableEffect(array, array2, array3) {
    let chance = rollDice(100)
    if (chance < 90) {
        return '.'
    } else if (chance < 95) {
        return '. ' + searchArray(array3)
    } else if (chance < 98) {
        return ". Observing this artwork has caused " + searchArray(array2[0])
    } else {
        return ". If you " + searchArray(array) + ', then ' + searchArray(array2[1])
    }
};

function printFrom(array, number) {
    let list = shuffle(array).slice(0, number)
    console.log(list)
}

/* ONLY DELETE BELOW HERE ------------------------------------------*/