//Chance and array manipulation methods
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
};

function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
};

// Page Scripts

function compliment(){
    document.getElementById("compliment").innerHTML = ""
let cornyComparison = [
    "Rakshasa's socks", "Crawling Claw's clap", "Owlbear's hoot", "Dryad's sprig", "Unicorn's horn", "Treant's trunk", "Dragon's hoard",
]
let mid = [
    "a creative", "a gorgeous", "a beautiful", "an intelligent", "a friendly", "a kind", "an awesome", "an impressive", "a great", "an important", "an admirable", "a dependable", "a talented", "a hardworking", "an imaginative", "a generous", "an excellent",
]
let finisher = [
    "person", "DM", "friend",
]
let template = [
    `It's cool to be in the presence of such ${searchArray(mid)} ${searchArray(finisher)}!`, `You are as cool as rolling two natural twenties in a row!`, `People are glad and lucky to know ${searchArray(mid)} ${searchArray(finisher)} like you!`, `I love your creativity!`, `I think you are the ${searchArray(cornyComparison)}`, `I am honored such ${searchArray(mid)} ${searchArray(finisher)} would visit my site!`
]
document.getElementById("compliment").innerHTML = `P.S. ${searchArray(template)}`;
//console.log(searchArray(template))
}

