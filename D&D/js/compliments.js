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

/*==================================================================================*/
/*-----------------------------Page Scripts Below-----------------------------------*/
/*==================================================================================*/


function compliment(){
    document.getElementById("compliment").innerHTML = ""
let cornyComparison = [
    "Rakshasa's socks", "Crawling Claw's clap", "Owlbear's hoot", "Dryad's sprig", "Unicorn's horn", "Treant's trunk", "Dragon's hoard","Cockatrice's charm", "Gorgon's gaze", "Basilisk's beauty", "Pixie's laughter", "Harpy's harmony", "Beholder's brilliance", "Kraken's embrace", "Chimera's grace", "Manticore's roar", "Gnoll's grin", "Phoenix's rebirth", "Sphinx's riddle", "Goblin's mischief", "Satyr's dance", "Centaur's gallop", "Mermaid's song", "Djinn's wish", "Medusa's gaze", "Gelatinous Cube's transparency", "Gargoyle's sturdiness", "Cyclops' vision", "Hippogriff's flight", "Leprechaun's luck", "Minotaur's strength", "Pegasus' wings", "Siren's allure", "Vampire's charm", "Werewolf's agility", "Zombie's endurance", "Wraith's haunting presence", "Yeti's resilience", "Mummy's mystery", "Golem's fortitude", "Changeling's transformation", "Fairy's enchantment", "Griffon's majesty", "Hydra's regrowth", "Invisible Stalker's stealth", "Nymph's beauty", "Ogre's might", "Roc's size", "Troll's regeneration", "Wendigo's hunger", "Giant's strength", "Banshee's haunting wail", "Cerberus' vigilance", "Gnashrak's roar", "Screechwing's speed", "Stoneheart's endurance"
]
let mid = [
    "a creative", "a gorgeous", "a beautiful", "an intelligent", "a friendly", "a kind", "an awesome", "an impressive", "a great", "an important", "an admirable", "a dependable", "a talented", "a hardworking", "an imaginative", "a generous", "an excellent", "an inspiring","an extraordinary", "a magnificent", "a splendid", "a remarkable", "a fantastic", "a delightful", "a marvelous", "an exceptional", "a phenomenal", "a legendary", "a fabulous", "a heroic", "a charming", "an alluring", "a captivating", "a stellar", "a glorious", "a majestic", "a wondrous", "a magical", "an enchanting", "a brilliant", "an innovative", "a visionary", "a gifted", "a resourceful", "a wise", "a noble", "an influential", "a respected", "a heroic", "a valiant", "a courageous", "a gallant", "a chivalrous", "a dignified"
]
let finisher = [
    "person", "DM", "friend", "creator", "inspirer","storyteller", "adventurer", "role-player", "wizard", "game master", "player character", "dice roller", "rulebook reader", "lore master", "campaign builder", "improviser", "battle strategist", "problem solver", "team player", "risk taker", "character actor", "creative mind", "quest giver", "quest completer", "team coordinator", "rule enforcer", "encounter designer", "world builder", "puzzle master", "trap setter", "minis painter", "lore enthusiast", "encounter planner", "dungeon designer", "character sheet organizer", "battle narrator", "innovative thinker", "imaginative soul", "mystery unraveler", "monster creator", "alliance forger", "story arc architect", "artwork collector", "NPC impersonator", "lore keeper", "battle describer", "strategic planner", "lore researcher", "tactical thinker", "champion of imagination"
]
let template = [
    `It's cool to be in the presence of such ${searchArray(mid)} ${searchArray(finisher)}!`, 
    `You are as cool as rolling two natural twenties in a row!`, 
    `People are glad and lucky to know ${searchArray(mid)} ${searchArray(finisher)} like you!`, 
    `I love your creativity!`, `I think you are the ${searchArray(cornyComparison)}`,
    `I am honored such ${searchArray(mid)} ${searchArray(finisher)} would visit my site!`
]
document.getElementById("compliment").innerHTML = `P.S. ${searchArray(template)}`;
//console.log(searchArray(template))
}

