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

function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
};


// convert numbers to word form
function toWords(s) {
    var th = ['', 'thousand', 'million', 'billion', 'trillion'];
    var dg = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
    var tn = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'];
    var tw = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'];


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

function printFrom(array, number, id) {
    let list = shuffle(array).slice(0, number)
    list.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};


function cat(){
    let size = [
        "all skin and bones", "a little scrawny", "pretty average in size", "a little long and lanky", "fat", "chonky",
    ]
    let color= [
        "solid white", "solid black", "solid grey", "grey and black spotted tabby", "orange and black spotted tabby", "grey and black striped tabby", "orange and white striped tabby", "orange and white striped tabby", "grey and black blotched tabby", "black and white bicolor", "white and orange bicolor", "calico",
    ]
    let eyes = [
        "yellow eyes", "golden brown eyes", "copper brown eyes", "dull green eyes", "bright green eyes", "brilliant gold eyes", "copper eyes", "bright blue eyes", "pale blue eyes", "bluish grey eyes", "one blue eye and one golden brown eye", "one blue eye and one copper brown eye",
    ]
    let bredTo = [
        "to hunt mice in granaries", "to hunt mice in urban dwellings", "to hunt rats aboard ships", "to hunt rats and mice in barns", "to hunt birds on rooftops", "to hunt snakes and lizards", "to sit on laps", "for no particular reason; it's ancestors were semi-feral village cats", "for no particular reason; it's ancestors were semi-feral city cats", "for no reason at all; it's ancestors were wild animals",
    ]
    let favFood = [
        "warm milk", "mice", "baby mice", "songbirds", "pigeon", "chicken", "sardines", "tuna", "salmon", "bacon",
    ]
    let markings =[
        "white or black toes on one foot", "extremely long whiskers", "a white or black tipped tail", "no tail", "a broken tail", "a scarred ear", "a patch of missing fur", "a pink nose", "a black nose", "a pink and black nose",
    ]
    let habits = [
        "a habit of hiding whenever it first meets someone", "a habit of begging for food", "a mistrustful demeanor, even toward people it knows well", "a playful demeanor, always chasing its tail", "a curious demeanor, always sneaking up and pouncing on things", "a noisy yowl when it is sad", "a cute little meow when it is content", "a habit of purring and rubbing against your leg", "a habit of hissing at any who approach it", "a friendly demeanor, provided you have food",
    ]
    let talent = [
        "scratching", "hissing", "purring", "climbing trees", "climbing walls", "catching mice", "catching fish", "catching birds", "avoiding you", "ignoring you",
    ]
    document.getElementById("Cat").innerHTML =  `You see a ${searchArray(size)} ${searchArray(color)}, with ${searchArray(eyes)} and ${searchArray(markings)}. The cat was bred to ${searchArray(bredTo)}, enjoys ${searchArray(favFood)}, typically has ${searchArray(habits)} and is especially talented at ${searchArray(talent)}.`
    console.log(output)
}

