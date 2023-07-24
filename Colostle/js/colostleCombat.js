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
function loopPrintList(array, id) {
    array.forEach(function(item) {
        let li = document.createElement("li");
        let text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
function printArray(array) {
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
    }
};
function checkConflict(coord,array){
    let bad = 0
    for (i = 0; i <= array.length; i++) {
        if (JSON.stringify(coord) === JSON.stringify(array[i])) {
            bad = 1
            return bad
        } 
    }
    return bad
};
function combineArrays(array1,array2,sizecount){
    let c = []
    let i = 0
    do { 
        let addition = [`(${array1[i]}) | ${ array2[i]}`]
        c[i]= addition
        i++
    } while (c.length < sizecount)
    return c
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


//General Combat
        //Rooks
    let magic = ['none','electric','rumble','ice']
    let bodyType = ['offensive','defensive']
    let rewardWeapon = ['ranged','melee']
    let reward= ['Helm','Arm','Rookling',`${searchArray(rewardWeapon)} weapon`]

//People
    let intention = ['to kill you.','to steal from you.','to flee from you.','to hide something from you.']
    let weapon = ['ranged','melee']

//Draw
    let cardHistory = []
    function draw(id) {
        let cardArray =  [2,3,4,5,6,7,8,9,10,'j','q','k','a']
        let suitArray = ['c','h','s','d']
        const cards= {
            ac:"./images/cards/ac.png",
            ad:"./images/cards/ad.png",
            ah:"./images/cards/ah.png",
            as:"./images/cards/as.png",
            kc:"./images/cards/kc.png",
            kd:"./images/cards/kd.png",
            kh:"./images/cards/kh.png",
            ks:"./images/cards/ks.png",
            qc:"./images/cards/qc.png",
            qd:"./images/cards/qd.png",
            qh:"./images/cards/qh.png",
            qs:"./images/cards/qs.png",
            jc:"./images/cards/jc.png",
            jd:"./images/cards/jd.png",
            jh:"./images/cards/jh.png",
            js:"./images/cards/js.png",
            '1c':"./images/cards/1c.png",
            '2c':"./images/cards/2c.png",
            '3c':"./images/cards/3c.png",
            '4c':"./images/cards/4c.png",
            '5c':"./images/cards/5c.png",
            '6c':"./images/cards/6c.png",
            '7c':"./images/cards/7c.png",
            '8c':"./images/cards/8c.png",
            '9c':"./images/cards/9c.png",
            '10c':"./images/cards/10c.png",
            '1d':"./images/cards/1d.png",
            '2d':"./images/cards/2d.png",
            '3d':"./images/cards/3d.png",
            '4d':"./images/cards/4d.png",
            '5d':"./images/cards/5d.png",
            '6d':"./images/cards/6d.png",
            '7d':"./images/cards/7d.png",
            '8d':"./images/cards/8d.png",
            '9d':"./images/cards/9d.png",
            '10d':"./images/cards/10d.png",
            '1h':"./images/cards/1h.png",
            '2h':"./images/cards/2h.png",
            '3h':"./images/cards/3h.png",
            '4h':"./images/cards/4h.png",
            '5h':"./images/cards/5h.png",
            '6h':"./images/cards/6h.png",
            '7h':"./images/cards/7h.png",
            '8h':"./images/cards/8h.png",
            '9h':"./images/cards/9h.png",
            '10h':"./images/cards/10h.png",
            '1s':"./images/cards/1s.png",
            '2s':"./images/cards/2s.png",
            '3s':"./images/cards/3s.png",
            '4s':"./images/cards/4s.png",
            '5s':"./images/cards/5s.png",
            '6s':"./images/cards/6s.png",
            '7s':"./images/cards/7s.png",
            '8s':"./images/cards/8s.png",
            '9s':"./images/cards/9s.png",
            '10s':"./images/cards/10s.png"
        }
        function pickCardAndSuit(){
            let x = searchArray(cardArray) + searchArray(suitArray)
            if (checkConflict(x,cardHistory)===1){
                do {
                    x = searchArray(cardArray) + searchArray(suitArray)
                } while (checkConflict(x,cardHistory)===1) 
                cardHistory.push(x)
                return x
            } else {
                cardHistory.push(x)
                return x
            }

        }

        let cardChoice = pickCardAndSuit()
        var img = new Image();
        img.src = cards[cardChoice]
        let elem = img
        img.onload = function () {
            if (id === 'playerDrawCon') {
                document.getElementById("playerDrawCon").appendChild(elem)
                console.log(cardHistory.length)
            } else {
                document.getElementById("enemyDrawCon").appendChild(elem)
                console.log(cardHistory.length)
            }
        }
        if (cardHistory.length ===52) {
            console.log("shuffle")
            cardHistory.length = 0
        }
        
    }

//shuffle and clear board
function shuffleDeck() {
    cardHistory.length = 0
    console.log(cardHistory)
}
function clearBoard() {
    document.getElementById("playerDrawCon").innerHTML=''
    document.getElementById("enemyDrawCon").innerHTML=''
}


    









