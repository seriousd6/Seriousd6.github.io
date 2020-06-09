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
}

//page scripts
let traderPersonality = [
    "I greet absolutely everyone with a warm hug. ", "I have a much better head for numbers than people. ", "I'm often more willing to barter in favors than coin. ", "I don't trust adventurers, not even a little bit. ", "It's all business with me, no need to be personable. ", "Repeat customers are my best friends. ", "I'll haggle all day, until your ears fall off. ", "I'm convinced my natural showmanship is what earns me customers. ",
]
let traderIdeal = [
    "Commerce. Free exchange is the world's greatest equalizer. (Lawful) ", "Monopoly. Undercutting my rivals and price gouging are the only ways to get ahead. (Evil) ", "Salesmanship. I'll sell absolutely anything. My horse, my mother, everything has a price. (Chaotic) ", "Charity. I try to give discounts or handouts to those that are truly in need. (Good) ", "Finality. No refunds. Ever. (Any) ", "Enjoyment. Buying and selling wares is all a big game to me, one that I love playing. (Any) ",
]
let traderBond = [
    "I have a sick relative that my business supports. ", "I owe a lot of money to organized crime, and they're threatening to collect. Violently. ", "I'm counting down the days to a peaceful retirement with my spouse or loved ones. ", "I hope to earn enough money to be able to pursue my true love, who is well above my station. ", "I'm on the run from the law, and plan to leave town before they finally recognize me. ", "A large portion of my money is spent atoning for my shameful past. ",
]
let traderFlaw = [
    "Most of my money is spent every night in the tavern. ", "I have no real faith in the quality of my merchandise, whether or not it is actually good. ", "If someone undercuts my prices, I'll cut their throat. ", "I counterfeit currency on the side, and slip it in with the change I give customers. ", "I never, ever, ever know when to quit, and I refuse to lose a sale. ", "It's hard for me to respect someone who doesn't know everything about what I'm selling. ",
]

let merchantType = [
    `Alcohol and refreshment`,
    `Animals(mounts and pets)`,
    `Books and maps(mundane)`,
    `Flowers and seeds`,
    `Food and animal parts`,
    `Furniture and interior decor`,
    `High fashion`,
    `Jewelry and gems`,
    `Knick-knacks`,
    `Leatherworking`,
    `Mechanical contraptions`,
    `Medium and heavy armor(and shields)`,
    `Potions, poisons, and herbs`,
    `Religious idols and blessings`,
    `Songs and instruments`,
    `Spell tomes and scrolls`,
    `Thieving supplies`,
    `Tools`,
    `Vehicles and transportation`,
    `Weapons`,
    `Legendary merchant(roll once on the Legendary Merchants table)`,
]

let legendaryMerchant = [
    `Astral traveler`,
    `Enchantments`,
    `Fey bargins`,
    `Magic items`,
    `Magical creatures`,
    `Necromancy`,
    `Needful things`,
    `Time-lost`,
]

function drinks() {
    let alcoholAndRefreshment = [
        //poor/atr
        `Ale, inferior (2cp/mug) stock: ${(1+rollDice(4))*100} mugs | Flavor will not leave mouth until next short rest`,
        `Ale, non-alcoholic (2cp/mug) stock: ${(1+rollDice(4))*100} mugs`,
        `Water (1cp/cup) stock: ${(1+rollDice(4))*100} cups | Clean and pure`,
        `Ale (4sp/mug) stock: ${(1+rollDice(4))*100} mugs | PHB 158`,
        `Flask or tankard (2cp) stock: ${(1+rollDice(4))*15} | PHB 150 Made of either pewter or treated wood`,
        `Tea, green (5cp/cup) stock: ${(1+rollDice(4))*10} cups`,
        //med
        `Brewer's supplies (20gp) stock: ${(1+rollDice(4))} | PHB 154`,
        `Cider (8cp/mug) stock: ${(1+rollDice(4))*100} mugs | Either apple. pear, pineapple, peach, or berry`,
        `Juice, fruit (3cp/cup) stock: ${(1+rollDice(4))*5} cups | Of any variety`,
        `Milk (1sp/bottle) stock: ${(1+rollDice(4))*5} bottles | Goat, cow, or other`,
        `Moonshine (3sp/bottle) stock: ${(1+rollDice(4))*5} bottles | Disadv. on saves to avoid intoxication`,
        `Tea, black (6cp/cup) stock: ${(1+rollDice(4))*10} cups`,
        `Yeast (4cp/lb.) stock: ${(1+rollDice(4))*2} lbs.`,
        //good
        `Brandy (5gp/bottle) stock: ${(1+rollDice(4))*2} bottles`,
        `Coffee (1sp/cup) stock: ${(1+rollDice(4))*10} cups`,
        `Hot chocolate (1sp/cup) stock: ${(1+rollDice(4))*10} cups`,
        `Mead (1sp/mug) stock: ${(1+rollDice(4))*100} mugs`,
        `Rum  (8gp/bottle) stock: ${(1+rollDice(4))*2} bottles`,
        `Tequila (8gp/bottle) stock: ${(1+rollDice(4))*2} bottles`,
        `Vodka (8gp/bottle) stock: ${(1+rollDice(4))*3} bottles`,
        `Whiskey (5sp/bottle) stock: ${(1+rollDice(4))*4} bottles`,
        `Wine, common (5sp/bottle) stock: ${(1+rollDice(4))*5} bottles | PHB 158`,
        `Wine, fine (10gp/bottle) stock: ${(1+rollDice(4))*4} bottles |PHB 158`,
        //ex
        `Ale, dwarven (25gp/mug) stock: ${(1+rollDice(4))*10} mugs | Drink a mug: facial hair grows perceptibly`,
        `Coffee, dwarven (15gp/cup) stock: ${(1+rollDice(4))*2} cups | Drink a cup: immune to sleep for 8 hours`,
        `Decanter of endless water (500gp) stock: Only 1, ever | DMG 161`,
        `Tea, portentous (20gp/cup) stock: ${(1+rollDice(4))*2} cups`,
        `Wine, elven (25gp/cup) stock: ${(1+rollDice(4))*2} cups`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Alcohol and Refreshment"
    alcoholAndRefreshment.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function animals() {
    let animalMerchant = [
        `Parrot, dead (1cp) stock: Only 1, ever | Deceased`,
        `Bat (2cp) stock: ${rollDice(4)} | MM 378`,
        `Cat (2sp) stock: ${rollDice(4)} | MM 320`,
        `Chicken (2cp) stock: ${rollDice(4)*2} | PHB 157 May instead be a rooster`,
        `Feed, animal (5cp/day) stock: ${rollDice(4)*30} days | PHB 157`,
        `Frog (1cp) stock: ${rollDice(4)} | MM 322 May instead be a toad`,
        `Goat (2gp) stock: ${rollDice(4)*2} | MM 330 May instead be a sheep`,
        `Lizard (1cp) stock: ${rollDice(4)} | MM 332`,
        `Pig (3sp) stock: ${rollDice(4)*2} | PHB 157`,
        `Rat (1cp) stock: ${rollDice(4)} | MM 335`,
        `Misc. CR 0 beasts (2cp-1gp) stock: ${rollDice(4)} | May be untamed`,
        `Badger (5sp) stock: ${rollDice(4)} | MM 378 Untamed`,
        `Cow (10gp) stock: ${rollDice(4)*2} | PHB 157 May instead be a bull, steer, or a cow variant`,
        `Draft horse (50gp) stock: ${rollDice(4)} | MM 327`,
        `Mule (8gp) stock: ${rollDice(4)} | MM 333 May instead be a donkey`,
        `Ox (15gp) stock: ${rollDice(4)} | PHB 757`,
        `Pony (30gp) stock: ${rollDice(4)} | MM 335`,
        `Raven (10gp) stock: ${rollDice(4)} | MM 335`,
        `Weasel (5sp) stock: ${rollDice(4)} | MM 340`,
        `Misc. CR 1/5 beasts (1gp-10gp) stock: ${rollDice(4)} | May be untamed`,
        `Misc. CR 1/4 beasts (5gp-25gp) stock: ${rollDice(4)} | May be untamed`,
        `Camel (50gp) stock: ${rollDice(4)} | MM 320`,
        `Eagle (20gp) stock: ${rollDice(4)-1} | MM 322`,
        `Hawk (15gp) stock: ${rollDice(4)-1} | MM 330`,
        `Lion (200gp) stock: ${rollDice(4)-1} | MM 337 Untamed`,
        `Mastiff (25gp) stock: ${rollDice(4)} | MM 332 Full-grown or pups`,
        `Monkey (25gp) stock: ${rollDice(4)-1}`,
        `Owl (20gp) stock: ${rollDice(4)} | MM 333`,
        `Riding horse (75gp) stock: ${rollDice(4)} | MM 336`,
        `Parrot, live (20gp) stock: ${rollDice(4)}`,
        `Panther (150gp) stock: ${rollDice(4)-2} | MM 333 Untamed`,
        `Tiger (200gp) stock: ${rollDice(4)-1} | MM 339 Untamed`,
        `Warhorse (400gp) stock: ${rollDice(4)} | MM 340`,
        `Wolf (50gp) stock: ${rollDice(4)} | MM 341`,
        `Misc. CR 1/2 beasts (20gp-50gp) stock: ${rollDice(4)} | May be untamed`,
        `Brown bear (300gp) stock: ${rollDice(4)} | MM 379 Untamed; full-grown or cubs`,
        `Elephant (600gp) stock: ${rollDice(4)-1} | MM 322`,
        `Mammoth (1,200 gp) stock: ${rollDice(4)-1} | MM 332`,
        `Rhinoceros (500 gp) stock: ${rollDice(4)-1} | MM 336 Untamed`,
        `Ring of animal influence (5.000 gp) stock: Only 1, ever | DMG 189`,
        `Misc. CR 1 beasts (50gp-300gp) stock: ${rollDice(4)-1} | May be untamed`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Animals (Mounts and Pets)"
    animalMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function books() {
    let booksAndMapsMerchant = [
        `Treasure map, fake (1 sp) stock: Only 1, ever | A DC 10 Investigation check discovers it is fake`,
        `Ink (10gp/ounce) stock: ${rollDice(4)*10} ounces | PHB 150`,
        `Ink pen (2cp) stock: ${rollDice(4)*2} | PHB 150`,
        `Paper (2sp/sheet) stock: ${rollDice(4)*20} sheets | PHB 150`,
        `Parchment (1sp/sheet) stock: ${rollDice(4)*2}0 sheets | PHB 150`,
        `Book, blank (25gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Book, tawdry (25gp) stock: ${rollDice(4)*2} | PHB 150 Example title: "My Midnight Tiefling"`,
        `Case, map or scroll (1gp) stock: ${rollDice(4)*5} | PHB 150`,
        `Guidebook, area (50gp) stock: ${rollDice(4)} | Pertains to a nearby specific city or location`,
        `Map, accurate (25gp) stock: ${rollDice(4)} | Portrays an important  area within 7 days' travel`,
        `Newspaper (2sp) stock: ${rollDice(4)*3} | Printed with the weekly news from a nearby city`,
        `Atlas, known world (500gp) stock: ${rollDice(4)-2} | Very accurate, but not overly detailed`,
        `Book, classic (100gp) stock: ${rollDice(4)} | Example title: "Adventures of Sherlock Gnomes"`,
        `Book, novel (50gp) stock: ${rollDice(4)} | Example title: "The Drow in the High Castle"`,
        `Calligrapher's supplies (10gp) stock: ${rollDice(4)} | PHB 154`,
        `Cartographer's tools (15gp) stock: ${rollDice(4)} | PHB 154`,
        `Guidebook, monster (125gp) stock: ${rollDice(4)} | Pertains to a specific monster type found nearby`,
        `Book, forgotten (500gp) stock: Only 1, ever | Example title: "The Call of Y'chak"`,
        `Map, planar (1,000gp) stock: Only 1, ever | Accurately depicts a significant planar location`,
        `Treasure map, real (1,000gp) stock: Only 1, ever | Depicts an area within 7 days' travel`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Books and Maps"
    booksAndMapsMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function flowers() {
    let flowersMerchant = [
        `Mixed flowers, dead (1cp/dozen) stock: ${rollDice(4)*2} dozen | Wilted and slightly browned`,
        `Mistletoe (1gp/sprig) stock: ${rollDice(4)*5} sprigs | PHB 150 Counts as a druidic focus`,
        `Mixed flowers (1cp/dozen) stock: ${rollDice(4)*5} dozen | A low-quality bouquet of common flowers`,
        `Seeds, crop (1cp/handful) stock: ${rollDice(4)*20} handfuls | Grows 10 lbs. of a staple, like rice or wheat`,
        `Seeds, wildflower (4cp/handful) stock: ${rollDice(4)*10} handfuls | Grows up to 60 wildflowers`,
        `Wildflowers (2cp/dozen) stock: ${rollDice(4)*5} dozen | A fresh bouquet of naturally local flowers`,
        `Flowers, fine (4cp/dozen) stock: ${rollDice(4)*5} dozen | Roses, lavendar, tulips, or similar`,
        `Herbalism kit (5gp) stock: ${rollDice(4)} PHB 154`,
        `Seeds, fine flower (8cp/handful) stock: ${rollDice(4)*10} handfuls | Grows a group of up to 120 fine flowers`,
        `Seeds, tree (5cp/handful) stock: ${rollDice(4)*10} handfuls | Grows up to 25 trees; oak, birch, pine, or similar`,
        `Glowblossom (1sp/dozen) stock: ${rollDice(4)*3} dozen | Emits dim light in a 10 foot radius`,
        `Phoenixbloom (1gp/dozen) stock: ${rollDice(4)*3} dozen | Burns as a torch, can set objects on fire`,
        `Seeds, fruit tree (3sp/handful) stock: ${rollDice(4)*10} handfuls | Grows up to 25 fruit trees; apple, pear, or similar`,
        `Seeds, glowblossom (2sp/handful) stock: ${rollDice(4)*2} handfuls | Grows up to 60 glowblossom flowers`,
        `Seeds, phoenix-bloom (2gp/handful) stock: ${rollDice(4)*2} handfuls | Grows up to 60 phoenixbloom flowers`,
        `Seeds, whistleweed (2sp/handful) stock: ${rollDice(4)*5} handfuls | Grows up to 60 whistleweed stalks`,
        `Whistleweed (1sp/dozen) stock: ${rollDice(4)*4} dozen | Whistles loudly when brushed against`,
        `Dragon lilly (5gp/dozen) stock: ${rollDice(4)} dozen | Contact instantly purifies up to 10 gal. of water`,
        `Quaal's feather token, tree (5,000 gp) stock: Only 1, ever | DMG 188`,
        `Seeds, dragon lilly (10gp/handful) stock: ${rollDice(4)} handfuls | Grows up to 60 dragon lillies in a shallow pond`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Flowers and Seeds"
    flowersMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function food() {
    let foodMerchant = [
        `Dung (1cp/lb.) stock: ${rollDice(4)*25} lbs.`,
        `Lard (2cp/lb) stock: ${rollDice(4)*2}5 lbs.`,
        `Meal, squalid (3cp/day) stock: ${rollDice(4)*20} days | PHB 158 Ripe, rancid, and the wrong kind of chewy`,
        `Teeth (1cp/each) stock: ${rollDice(4)*30} | Either animal or (possibly) human`,
        `Bread (2cp/loaf) stock: ${rollDice(4)*10} loaves | PHB 158`,
        `Butter (3cp/stick) stock: ${rollDice(4)*10} sticks`,
        `Cheese (1sp/hunk) stock: ${rollDice(4)*2}0 hunks | PHB 158`,
        `Eggs (1sp/dozen) stock: ${rollDice(4)*5} dozen | Chicken, duck, or similar`,
        `Flour (2cp/lb.) stock: ${rollDice(4)*10} lbs. | PHB 157`,
        `Fruit (1cp/each) stock: ${rollDice(4)*20} | Apples, plums, or similar; can also be vegetables`,
        `Meal, poor (6cp/day) stock: ${rollDice(4)*20} days | PHB 158 Gruel and greasy bits, smells like regret`,
        `Milk (1sp/bottle) stock: ${rollDice(4)*5} bottles`,
        `Wheat (1cp/lb.) stock: ${rollDice(4)*25} lbs. | PHB 157`,
        `Bones (5gp/set) stock: ${rollDice(4)} sets | Good for soup and maybe even necromancy`,
        `Hunting trap (5gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Meal, modest (3sp/day) stock: ${rollDice(4)*20} days | PHB 158 A hearty broth with real vegetables`,
        `Meat (3sp/chunk) stock: ${rollDice(4)*5} chunks | PHB 158 Beef, pork, chicken, venison or similar`,
        `Mess kit (2sp) stock: ${rollDice(4)*2} | PHB 150`,
        `Pot, iron (2gp) stock: ${rollDice(4)} | PHB 150`,
        `Rations (5sp/day) stock: ${rollDice(4)*5} days | PHB 150`,
        `Salt (5cp/lb.) stock: ${rollDice(4)*10} lbs. | PHB 157`,
        `Soap (2cp) stock: ${rollDice(4)*5} | PHB 150`,
        `Cake (5gp) stock: ${rollDice(4)} | Sumptuous and moist; feeds 8`,
        `Cook's utensils (1gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Fishing tackle (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Ginger (1gp/lb.) stock: ${rollDice(4)*10} lbs. | PHB 157`,
        `Hat, chef (3gp) stock: Only 1, ever`,
        `Meal, comfortable (5sp/day) stock: ${rollDice(4)*20} days | PHB 158 Lightly spiced meat served with a side dish`,
        `Meal, wealthy (8sp/day) stock: ${rollDice(4)*20} days | PHB 158 Well-prepared prime cut of meat, and dessert`,
        `Pie (1gp) stock: ${rollDice(4)*2} | Sweet or savory, feeds 1-2`,
        `Saffron (15gp/lb.) stock: ${rollDice(4)} lbs. | PHB 157`,
        `Spices (2gp/lb.) stock: ${rollDice(4)*5} lbs.|  PHB 157 Pepper, cinnamon, or similar`,
        `Bones, dragon (50gp/lb.) stock: ${rollDice(4)*5} lbs.`,
        `Horn, unicorn (1,000gp) stock: ${rollDice(4)-1}`,
        `Ioun stone, sustenance (5,000gp) stock: Only 1, ever | DMG 176`,
        `Meal, aristocratic (2gp/day) stock: ${rollDice(4)*20} days | PHB 158 A most succulet cut of magical beast`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Food and Animal Parts"
    foodMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function decor() {
    let artMerchant = [
        `Barrel (2gp) stock: ${rollDice(4)*5} | PHB 150`,
        `Basket (4sp) stock: ${rollDice(4)*5} | PHB 150`,
        `Bookcase (2gp) stock: ${rollDice(4)*3} | 5 feet x 1 foot, 4 feet tall, holds approx 60 books`,
        `Chest, medium (5gp) stock: ${rollDice(4)*2} | PHB 150 6 feet x 2 feet, 1 foot tall, holds approx 300 lbs.`,
        `Doghouse, large (3gp) stock: ${rollDice(4)-2} | Capable of holding a dog or other large creature`,
        `Furnace, coal (8gp) stock: ${rollDice(4)} | Can burn 1 lb. of coal per day`,
        `Table, wood (3gp) stock: ${rollDice(4)*2} | 4 feet x 8 feet, 2.5 feet tall`,
        `Chest, large (10gp) stock: ${rollDice(4)*2} | 6 feet x 3 feet, 2 feet tall, holds approx 900 lbs.`,
        `Jug or pitcher (2cp) stock: ${rollDice(4)*4} | PHB 150`,
        `Painting, medium (10gp) stock: Made to order | Example Depicts a gnome & her pet giant bee`,
        `Rug, large (12gp) stock: ${rollDice(4)} | 10 feet x 50 feet, really ties a room together`,
        `Wardrobe, wood (10gp) stock: ${rollDice(4)} | 4 feet x 1.5 feet, 6 feet tall, holds approx 900 lbs.`,
        `Altar (20gp) stock: Made to order | Contains holy symbols and space for rituals`,
        `Armchair (12gp) stock: ${rollDice(4)} | Leather, well-stuffed, highly comfortable`,
        `Banner or flag (30gp) stock: Made to order | 3 feet x 10 feet, comes with custom design`,
        `Bathtub, ornate (25gp) stock: ${rollDice(4)} | Example. Worked steel with dragon-headed taps`,
        `Bed, four-poster (75gp) stock: ${rollDice(4)} | 8 feet x 6 feet, filled with owlbear down`,
        `Desk, ornate (15gp) stock: ${rollDice(4)-2} | Example Intricate vines carved in smooth wood`,
        `Fountain (750gp) stock: Made to order | 6 feet x 6 feet, 4 feet tall, marble or similar`,
        `Lamp, magic (100gp) stock: ${rollDice(4)} | Turns off and on, triggered by a single clap`,
        `Mosaic, large (600gp) stock: Made to order | Example Water elementals crashing on a coast`,
        `Painting, huge (550gp) stock: Made to order | Example The artist's depiction of the Dawn War`,
        `Painting, large (50gp) stock: Made to order | Example A courtly dragonborn and her consort`,
        `Statue, metal (1,000gp) stock: Made to order | Example A brass statue of the goddess Avandra`,
        `Chandelier, huge (1,500gp) stock: Made to order | Example Astral crystal interlaced with mithral`,
        `Mirror of life trapping (50,000gp) stock: Only 1, ever | DMG 181`,
        `Statue, precious (2,000gp) stock: Made to order | Example An enormous adamantine dragon`,
        `Tapestry (1,500gp) stock: Made to order | Example Adventurers thwarting an ancient evil`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Furniture and Interior Decor"
    artMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function fashion() {
    let fashionMerchant = [
        `Sack, wearable (1cp) stock: ${rollDice(4)*5} | PHB 150 Almost waterproof`,
        `Cap, leather (5sp) stock: ${rollDice(4)*2} | A sturdy, if ugly, way to keep your head dry`,
        `Cap, bonnet (5sp) stock: ${rollDice(4)*2} | A working woman's hat`,
        `Cap, stocking (4sp) stock: ${rollDice(4)*2} | A long, conical cap for a cold winter's night`,
        `Clothes, common (5sp) stock: ${rollDice(4)*5} | PHB 150 Worn and patched, made of rough materials`,
        `Clothes, traveler's (2gp) stock: ${rollDice(4)*5} | PHB 150 Durable and well-made, but not exactly fancy`,
        `Robes (1gp) stock: ${rollDice(4)*2} | PHB 150 Simple, smooth, and clean, with many pockets`,
        `Clothes, costume (5gp) stock: ${rollDice(4)*2} | PHB 150 A finely made costume for a jester or actor`,
        `Cobbler's tools (5gp) stock: ${rollDice(4)} | PHB 154`,
        `Hat, bowler (2gp) stock: ${rollDice(4)*2} | A rounded hat with a short brim`,
        `Hood (5sp) stock: ${rollDice(4)*2}`,
        `Perfume vial (5gp) stock: ${rollDice(4)*2} vials | PHB 150 A faint floral aroma for the discerning nose`,
        `Weaver's tools (1gp) stock: ${rollDice(4)} | PHB 154`,
        `Wig (2gp) stock: ${rollDice(4)*2} | Beautiful or austere, good at hiding baldness`,
        `Bow or bowtie (12gp) stock: ${rollDice(4)*3} | Soft silken cloth, plain or with festive pattern`,
        `Clothes, aristocratic (50gp) stock: ${rollDice(4)*5} | The bleeding edge of modern fashion`,
        `Clothes, fine (15gp) stock: ${rollDice(4)*5} | PHB 150 Refined noble clothes, very fashionable`,
        `Cowl (2gp) stock: ${rollDice(4)*2} | A face-wrap favored by vigilantes and assassins`,
        `Goggles (10gp) stock: ${rollDice(4)} | Leather and glass, perfect for keeping eyes safe`,
        `Hat, adventurer's (15gp) stock: ${rollDice(4)} | A wide-brimmed leather hat favored by explorers`,
        `Hat, beret (3gp) stock: ${rollDice(4)*2} | A simple circular hat, a staple of artists`,
        `Hat. fez (5gp) stock: ${rollDice(4)*2} | Worn by distinguished individuals in arid lands`,
        `Hat, sea captain (20gp) stock: ${rollDice(4)} | A nautical cap that demands a crew's respect`,
        `Hat, ushanka (3gp) stock: ${rollDice(4)*2} | A soft, warm hat, ideal for freezing conditions`,
        `Hat, wizard (25gp) stock: ${rollDice(4)} | The conical, wide-brimmed hat of a true wizard`,
        `Mask (5gp) stock: ${rollDice(4)*2} | Secretive or festive, good for crimes and parties`,
        `Shaded glasses (350gp) stock: ${rollDice(4)} | Negates disadvantage from Sunlight Sensitivity`,
        `Boots of the winterlands (500gp) stock: Only 1, ever | DMG 156`,
        `Clothes, superior (150gp) stock: Only 1, ever | Enchanted, always the finest clothes in the room`,
        `Hat, superior (100 gp) stock: Only 1, ever | Enchanted, always the finest hat in the room`,
        `Robe of scintillating colors (50,000gp) stock: Only 1, ever`,
        `Slippers of spider climbing (500gp) stock: Only 1, ever | DMG 192`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "High Fashion"
    fashionMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function jeweler() {
    let jeweler = [
        `Geode, fake (2sp) stock: ${rollDice(4)*2} | No crystals within this rock. Only more rock.`,
        `Copper (5sp/lb.) stock: ${rollDice(4)*2} lbs. | PHB 157`,
        `Earring, simple (5gp) stock: ${rollDice(4)*5} | Small stud or ring of semi-precious metal`,
        `Gems, common (10gp/ea.) stock: ${rollDice(4)*4} | DMG 134 Examples: agate, lapis lazuli, malachite, tiger eye`,
        `Iron (1sp/lb.) stock: ${rollDice(4)*5} lbs. | PHB 157`,
        `Locket, brass (4sp) stock: ${rollDice(4)*3}`,
        `Pick, miners (4gp) stock: ${rollDice(4)} | PHB 150`,
        `Magnifying glass (100gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Ring, simple (5gp) stock: ${rollDice(4)*4} | A small circle of polished semi-precious metal`,
        `Medium Gems, uncommon (50gp/ea.) stock: ${rollDice(4)*5} | DMG 134 Examples: citrine, jasper, moonstone, quartz`,
        `Jeweler's tools (25gp) stock: ${rollDice(4)} | PHB 154`,
        `Necklace (150gp) stock: ${rollDice(4)*3} | Braided metal, including pendant with a gem`,
        `Signet ring (5gp) stock: ${rollDice(4)} | PHB 150`,
        `Silver (5gp/lb.) stock: ${rollDice(4)} lbs. | PHB 157`,
        `Brooch of shielding (500gp) stock: Only 1, ever | DMG 156`,
        `Crown (750gp) stock: ${rollDice(4)} | Precious metal circlet inset with gemstones`,
        `Earring, elegant (200gp) stock: ${rollDice(4)*2} | Ostentatiously gemmed stud or metal ring`,
        `Gems, exceptional (100gp/ea.) stock: ${rollDice(4)*4} | DMG 134 Examples: amber, amethyst, gamet, jade, pearl`,
        `Gem of brightness (500gp) stock: Only 1, ever | DMG 171`,
        `Gems, rare (500gp/ea.) stock: ${rollDice(4)*3} | DMG 134 Examples: alexandrite, peridot, topaz`,
        `Gems, very rare (1,000gp/ea.)stock: ${rollDice(4)*2} | DMG 134 Examples: emerald, opal, sapphire, ruby`,
        `Gold (50gp/lb.) stock: ${rollDice(4)} lbs. | PHB 157`,
        `Medallion of thoughts (500gp) stock: Only 1, ever | DMG 181`,
        `Ring, elegant (250gp) stock: ${rollDice(4)*2} | Tooled metal band inset with precious gems`,
        `Excellent Elemental gem (500gp) stock: Only 1, ever | DMG 167`,
        `Gems, legendary (5,000gp/ea.) stock: ${rollDice(4)} | DMG 134 Examples: black sapphire, diamond, jacinth`,
        `Platinum (500gp/lb.) stock: ${rollDice(4)} lbs. | PHB 157`,
        `Ring of protection (5,000 gp) stock: Only 1, ever | DMG 191`,
        `Ring of telekinesis (50,000 gp) stock: Only 1, ever | DMG 193`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Jewelry and Gems"
    jeweler.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function misc() {
    let KnickKnackMerchant = [
        `Pole, 10-foot (5cp) stock: ${rollDice(4)*4} | PHB 150`,
        `Blanket (5sp) stock: ${rollDice(4)*3} | PHB 150`,
        `Block and tackle (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Bucket (5cp) stock: ${rollDice(4)*4} | PHB 150`,
        `Candle (1cp) stock: ${rollDice(4)*10} | PHB 150`,
        `Chalk (1cp/piece) stock: ${rollDice(4)*5} pieces | PHB 150 Comes in a variety of colors`,
        `Dice set (1sp) stock: ${rollDice(4)*3} | PHB 154`,
        `Flask or tankard (2cp) stock: ${rollDice(4)*5} | PHB 150 Made of either pewter or treated wood`,
        `Playing card set (5sp) stock: ${rollDice(4)*3} | PHB 154`,
        `Signal whistle (5cp) stock: ${rollDice(4)*2} | PHB 150`,
        `Tinderbox (5sp) stock: ${rollDice(4)*3} | PHB 150`,
        `Amulet (5gp) stock: ${rollDice(4)} | PHB 150 Counts as a holy symbol`,
        `Ball bearings (1gp/1,000) stock: ${rollDice(4)*2,000} | PHB 150`,
        `Cart (15gp) stock: ${rollDice(4)} | PHB 157`,
        `Chain (5gp/10 feet) stock: ${rollDice(4)*20} feet | PHB 150`,
        `Climber's kit (25gp) stock: ${rollDice(4)} | PHB 150`,
        `Hourglass (25gp) stock: ${rollDice(4)} | PHB 150`,
        `Lamp (5sp) stock: ${rollDice(4)} | PHB 150`,
        `Lantern, bullseye (10gp) stock: ${rollDice(4)} | PHB 150`,
        `Lantern, hooded (5gp) stock: ${rollDice(4)} | PHB 150`,
        `Rope, hempen (1gp/50feet) stock: ${rollDice(4)*50} feet | PHB 150`,
        `Rowboat (50gp) stock: ${rollDice(4)-2} | PHB 157`,
        `Scale, merchant's (5gp) stock: ${rollDice(4)} | PHB 150`,
        `Tarokka deck (10gp) stock: ${rollDice(4)} | CoS 243`,
        `Alcherny jug (500gp) stock: Only 1, ever | DMG 150`,
        `Artisan's tools (varies) stock: ${rollDice(4)+2} sets | PHB 154 Prices are as listed in the PHB`,
        `Bell (1gp) stock: ${rollDice(4)+2} | PHB 150`,
        `Caltrops (1gp/20) stock: ${rollDice(4)*40} | PHB 150`,
        `Dragonchess set (1gp) stock: ${rollDice(4)} | PHB 154`,
        `Grappling hook (2gp) stock: ${rollDice(4)} | PHB 150`,
        `Lantern of revealing (500gp) stock: Only 1, ever | DMG 179`,
        `Three-Dragon Ante set (1gp) stock: ${rollDice(4)} | PHB 154`,
        `Spyglass (1,000gp) stock: ${rollDice(4)} | PHB 150`,
        `Sovereign glue (50,000gp) stock: Only 1, ever | DMG 200`,
        `Universal solvent (50,000gp) stock: Only 1, ever | DMG 209`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Knick Knacks"
    KnickKnackMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function leather() {
    let leatherWorker = [
        `Leather, cured (5gp/sq.yd) stock: ${rollDice(4)*4} sq.yds.`,
        `Bit and bridle (2gp) stock: ${rollDice(4)*2} | PHB 157`,
        `Cap, leather (5sp) stock: ${rollDice(4)*2} | A sturdy way to keep your head dry`,
        `Meat (3sp/chunk) stock: ${rollDice(4)*5} chunks | PHB 158`,
        `Padded armor (5gp) stock: ${rollDice(4)*2} | PHB 145`,
        `Pouch (5sp) stock: ${rollDice(4)*4} | PHB 150`,
        `Saddle, pack (5gp) stock: ${rollDice(4)} | PHB 157`,
        `Waterskin (2sp) stock: ${rollDice(4)*3} | PHB 150`,
        `Backpack (2gp) stock: ${rollDice(4)*3} | PHB 150`,
        `Clothes, traveler's (2gp) stock: ${rollDice(4)} | PHB 150 Durable and well-made, stands punishment`,
        `Hunting trap (5gp) stock: ${rollDice(4)} | PHB 150`,
        `Leather armor (10gp) stock: ${rollDice(4)*2} | PHB 145`,
        `Leatherworker's tools (25gp) stock: ${rollDice(4)} | PHB 154`,
        `Oil (1sp/flask) stock: ${rollDice(4)*2} flasks | PHB 150`,
        `Quiver (1gp) stock: ${rollDice(4)} | PHB 150`,
        `Saddle, riding (10gp) stock: ${rollDice(4)} | PHB 157`,
        `Bagpipes (30gp) stock: ${rollDice(4)} | PHB 154`,
        `Bag of holding (500gp) stock: Only ${rollDice(4)}, ever | DMG 153`,
        `Boots of elvenkind (500gp) stock: Only 1, ever | DMG 155`,
        `Boots of the winterlands (500gp) stock: Only 1, ever | DMG 156`,
        `Drum (6gp) stock: ${rollDice(4)} | PHB 154`,
        `Hat, adventurer's (15gp) stock: ${rollDice(4)} | A wide-brimmed leather hat favored by explorers`,
        `Hide armor (10gp) stock: ${rollDice(4)} | PHB 145`,
        `Saddlebags (4gp) stock: ${rollDice(4)*2} | PHB 157`,
        `Saddle, exotic (60gp) stock: ${rollDice(4)} | PHB 157`,
        `Saddle, military (20gp) stock: ${rollDice(4)} | PHB 157`,
        `Studded leather armor (45gp) stock: ${rollDice(4)} | PHB 145`,
        `Belt of dwarvenkind (5,000 gp) stock: Only 1, ever | DMG 155`,
        `Dragon scale mail, red (50,000 gp) stock: Only 1, ever | DMG 165`,
        `Glamoured studded leather (5,000 gp) stock: Only 1, ever | DMG 172`,
        `Saddle of the cavalier (500gp) stock: Only 1, ever | DMG 199`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Leather Worker"
    leatherWorker.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function mech() {
    let mechanicalMerchant = [
        `Hoop and stick (2cp) stock: ${rollDice(4)*3} | A pass-time from a simpler time`,
        `Abacus (2gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Ball bearings (1gp/1,000) stock: ${rollDice(4)*2000} | PHB 150`,
        `Block and tackle (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Cogs (1sp/handful) stock: ${rollDice(4)*5} handfuls`,
        `Oil (1sp/flask) stock: ${rollDice(4)*5} flasks | PHB 150`,
        `Barrel organ (30gp) stock: ${rollDice(4)} | Musical instrument; turn the crank to play`,
        `Bomb (150gp) stock: ${rollDice(4)*4} | DMG 267 May not exist in settings w/o gunpowder`,
        `Clockwork dog (5gp) stock: ${rollDice(4)} | When wound up, walks forward, barks, and flips`,
        `Clockwork dragonchess set (20gp) stock: ${rollDice(4)} | Automatically plays dragonchess against you`,
        `Gunpowder, horn (35gp) stock: ${rollDice(4)*4} | DMG 267 May not exist in settings w/o gunpowder`,
        `Hunting trap (5gp) stock: ${rollDice(4)*3} | PHB 150`,
        `Lock (10gp) stock: ${rollDice(4)*5} | PHB 150`,
        `Clockwork dragon (25gp) stock: ${rollDice(4)} | May breathe fire that can set objects alight`,
        `Clockwork mount (250gp) stock: ${rollDice(4)} | MM 336 Has the same statistics as a riding horse`,
        `Clockwork songbird (12gp) stock: ${rollDice(4)} | Sings 1 of 3 songs on command; flightless`,
        `Dynamite (200gp/stick) stock: ${rollDice(4)*4} sticks | DMG 267 May not exist in settings w/o gunpowder`,
        `Goggles of night (500gp) stock: Only 1, ever | DMG 172`,
        `Gunpowder, keg (250gp) stock: ${rollDice(4)} | DMG 267 May not exist in settings w/o gunpowder`,
        `Pocketwatch (10gp) stock: ${rollDice(4)*2} | When wound, reliably tells the time of day`,
        `Tinker's tools (50gp) stock: ${rollDice(4)+2} | PHB 154`,
        `Clockwork rocket sled (2,500gp) stock: ${rollDice(4)+1} | Moves 60 feet / round in one direction for 1 min`,
        `Iron bands of Bilarro (5,000gp) stock: Only 1, ever | DMG 177`,
        `Manual of golems, iron (25,000gp) stock: Only 1, ever | DMG 180`,
        `Wand of lightning bolts (5,000gp) stock: Only 1, ever | DMG 211`,
        `Winged boots (500gp) stock: Only 1, ever | DMG 274`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Mechanical Contraptions"
    mechanicalMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function armor() {
    let heavyarmor = [
        `Barrel, wearable (2gp) stock: ${rollDice(4)*2} | PHB 150 Includes straps; does not include bottom`,
        `Bucket (5cp) stock: ${rollDice(4)*2} | PHB 150 Anything is armor if you're foolhardy enough`,
        `Chain mail (75gp) stock: ${rollDice(4)*3} | PHB 145`,
        `Chain shirt (50gp) stock: ${rollDice(4)*4} | PHB 145`,
        `Copper (5sp/lb) stock: ${rollDice(4)*2} lbs. | PHB 157`,
        `Iron (1sp/lb) stock: ${rollDice(4)*5} lbs. | PHB 157`,
        `Ring mail (30gp) stock: ${rollDice(4)*4} | PHB 145`,
        `Scale mail (50gp) stock: ${rollDice(4)*3} | PHB 145`,
        `Shield (10gp) stock: ${rollDice(4)*3} | PHB 145`,
        `Anvil (75gp) stock: ${rollDice(4)}`,
        `Barding (*varies) stock: ${rollDice(4)*3} | PHB 157 Prices are as listed in the PHB`,
        `Breastplate (400gp) stock: ${rollDice(4)} | PHB 145`,
        `Helm, horned (25gp) stock: ${rollDice(4)} | While imposing, it is hard to get through doors`,
        `Smith's tools (20gp) stock: ${rollDice(4)} | PHB 154`,
        `Splint (200gp) stock: ${rollDice(4)+4} | PHB 145`,
        `Adamantine armor, any (500gp) stock: Only ${rollDice(4)}, ever | DMG 150 Must also pay the cost of the base armor`,
        `Armor, +1 (5,000gp)  stock: Only ${rollDice(4)}, ever | DMG 152 Must also pay the cost of the base armor`,
        `Half plate (750gp) stock: ${rollDice(4)+3} | PHB 145`,
        `Helm, winged (50gp) stock: ${rollDice(4)} | Gallant and flamboyant`,
        `Mithral armor, any (500gp) stock: Only ${rollDice(4)}, ever | DMG 182 Must also pay the cost of the base armor`,
        `Plate +1 (500gp) stock: ${rollDice(5)-2} | PHB 145`
        `Shield, +1 (500gp) stock: Only 1, ever | DMG 200`,
        `Silver (5gp/lb) stock: ${rollDice(4)*2} lbs. | PHB 157`,
        `Arrow-catching shield (5,000gp) stock: Only 1, ever | DMG 152`,
        `Armor, +2 (50,000gp) stock: Only 1, ever | DMG 152 Must also pay the cost of the base armor`,
        `Dwarven plate (50,000gp) stock: Only 1, ever | DMG 167`,
        `Elven chain (5,000gp) stock: Only 1, ever | DMG 168`,
        `Helm of teleportation (5,000 gp) stock: Only 1, ever | DMG 774`,
        `Shield, +2 (5,000gp) stock: Only ${rollDice(5)-2}, ever | DMG 200`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Medium/ Heavy Armor"
    heavyarmor.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function alch() {
    let alchemyAndPotions = [
        `Water (1cp/cup) stock: ${rollDice(4)*100} cups | An effective base for most potions`,
        `Herbalism kit (5gp) stock: ${rollDice(4)} | PHB 154`,
        `Herbs, common (5sp/lb) stock: ${rollDice(4)*10} lbs. | Ex: Mint, sage;often used in common potions`,
        `Herbs, uncommon (5gp/lb) stock: ${rollDice(4)*5} lbs. | Ex: Horsetail, comfrey; for uncommon potions`,
        `Poison, basic (100gp/vial) stock: ${rollDice(4)*2} vials | PHB 150 Injury;can inflict 1d4 poison damage`,
        `Potion of climbing (50gp) stock: ${rollDice(4)*2} | DMG 187 Grants a climbing speed for 1 hour`,
        `Potion of healing (50gp) stock: ${rollDice(4)*3} | PHB 150 Regains 2d4+2 hit points`,
        `Alchemist's supplies (50gp) stock: ${rollDice(4)} PHB 154`,
        `Assassin's blood (150gp/dose )stock: ${rollDice(4)+2} doses | DMG 257 Injested; can inflict 1d12 poison damage`,
        `Oil of slipperiness (250gp) stock: ${rollDice(4)-2} | DMG 184 Grants either freedom of movement or grease`,
        `Philter of love (250gp)stock: ${rollDice(4)+2} | DMG 184 Charms the drinker for up to an hour`,
        `Poisoner's kit (50gp) stock: ${rollDice(4)} | PHB 154`,
        `Potion of fire breath (250gp) stock: ${rollDice(4)+2} | DMG 187 Allows you to exhale fire.dealing 4 d6 damage`,
        `Potion of greater healing (250gp) stock: ${rollDice(4)*2} | DMG 187 Regains 4 d4 I .4 hit points`,
        `Potion of water breathing (250gp) stock: ${rollDice(4)*2} | DMG 188 Allows you to breathe water for up to an hour`,
        `Truth serum (150gp/dose) stock: ${rollDice(4)+2} doses | DMG 258 Injested;target cannot knowingly speak a lie`,
        `Drow poison (200gp/dose) stock: ${rollDice(4)} doses | DMG 258 Injury;can render target unconscious`,
        `Elixir of health (2,500 gp) stock: ${rollDice(4)+2} | DMG 168 Curse disease, blind, deaf, paralyze, and poison`,
        `Herbs, rare (50gp/lb)stock: ${rollDice(4)*4} lbs. | Ex: Devilroot, embertear; for rare potions Herbs, very rare 500 gp / lb .${rollDice(4)*2} lbs.Ex: Starspine, voidweave: for very rare potions`,
        `Potion of clairvoyance (2,500gp) stock: ${rollDice(4)+2} | DMG 187 Grants the effect of the clairvoyance spell`,
        `Potion of diminution (2,500gp) stock: ${rollDice(4)+2} | DMG 187 Drink to be shrunk as if by enlarge / reduce`,
        `Potion of heroism (2,500gp) stock: ${rollDice(4)} | DMG 188 Grants bless and 10 temporary hit points`,
        `Potion of mind reading (2,500gp) stock: ${rollDice(4)} | DMG 188 Grants the effects of the detect thoughts spell`,
        `Potion of superior healing (2,500gp) stock: ${rollDice(4)+2} | DMG 188 Regains 8d4+8 hit points`,
        `Serpent venom (200gp/dose) stock: ${rollDice(4)} doses | DMG 258 Injury;can inflict 3 d6 poison damage`,
        `Burnt othur fumes (500gp/dose) stock: ${rollDice(4)} doses | DMG 258 Inhailed;can inflict persistent poison damage`,
        `Malice (250gp/dose) stock: ${rollDice(4)} doses | DMG 258 Inhaled, can blind affected creatures`,
        `Oil of sharpness (25,000gp) stock: ${rollDice(4)} | DMG 184 Grants an item + 3 to attack and damage`,
        `Potion of invisibility (25,000gp)stock: ${rollDice(4)} | DMG 188 Grants invisibility for up to an hour`,
        `Potion of invulnerability (2,500gp) stock: ${rollDice(4)} | DMG 188 Grants resistance to all damage`,
        `Potion of longevity (25,000gp) stock: ${rollDice(4)-1} | DMG 188 Reduces your age by 1 d6 + 6 years, usually`,
        `Potion of supreme healing (25,000gp) stock: ${rollDice(4)} | DMG 187 Regains 10d4+20 hit points`,
        `Potion of vitality (25,000gp) stock: ${rollDice(4)} | DMG 188 Cures exhaustion, disease, and poison`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Potions, Poisons, Herbs"
    alchemyAndPotions.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function religious() {
    let religiousMerchant = [
        `Candle (1cp) stock: ${rollDice(4)*10} | PHB 150 Comes in a variety of colors`,
        `Book, holy (5gp) stock: ${rollDice(4)*10} | PHB 150 From one of a variety of faiths`,
        `Chalk (1cp/piece) stock: ${rollDice(4)*10} pieces | PHB 150 Comes in a variety of colors`,
        `Dagger, ritual (2gp) stock: ${rollDice(4)*2} | PHB 148 Has an oddly curved design`,
        `Holy symbol (*varies) stock: ${rollDice(4)*20} | PHB 150 Prices are as listed in the PHB`,
        `Incense (1sp/block) stock: ${rollDice(4)*20} blocks | Thick, musky, and pungent`,
        `Spell: Cure wounds (10gp) stock: 3 spells / day | PHB 230 Cast at 1st level; heals 1d8 + 3 hit points`,
        `Spell: Identify (20gp) stock: 3 spells / day stock: ${rollDice(4)*10} | PHB 252 PHB 150 Tells you the properties of a magic item`,
        `Druidic focus (varies) stock: ${rollDice(4)} | Prices are as listed in the PHB`,
        `Healer's kit (5gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Holy water (25gp/flask) stock: ${rollDice(4)*5} flasks | PHB 150`,
        `Quarterstaff (2sp) stock: ${rollDice(4)*2} | PHB 148`,
        `Robes (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Spell: Lesser restoration (40gp) stock: 3 spells / day | PHB 255 Cures blind, deaf, paralyze, or poison`,
        `Spell: Prayer of healing (40gp) stock: 3 spells / day | PHB 267 Cast at 2nd level; heals 2d8 + 3 hit points`,
        `Thurible (55gp) stock: ${rollDice(4)+2} | A gilded censer for burning incense`,
        `Keoghtom's ointment (250gp) stock: ${rollDice(4)+2} | PHB 179`,
        `Spell: Divination (210gp) stock: 3 spells / day | PHB 234 Grants guidance on a course of action`,
        `Spell: Remove curse (90gp) stock: 3 spells / day | PHB 271 Lifts curse or attunement to cursed item`,
        `Spell: Speak with dead (90gp) stock: 3 spells / day | PHB 277 Allows you to speak to one non-undead corpse`,
        `Staff of the Python (500gp) stock: Only 1, ever | DMG 204`,
        `Candle of invocation (50,000gp) stock: Only 1, ever | DMG 157`,
        `Spell: Greater restoration (450gp) stock: 3 spells / day | PHB 246 Reduces exhaustion, removes charm, petrify, curse, or ability/hp reduction`,
        `Spell: Raise dead (1,250gp) stock: 3 spells / day | PHB 270 Returns a dead corpse to life`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Religious Idols and Blessings"
    religiousMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function instruments() {
    let bardInstruments = [
        `Written song, terrible (1cp) stock: ${rollDice(4)} copies | Example: "Freeform Jazz Odyssey No. 12"`,
        `Bell (1gp) stock: ${rollDice(4)*3} | PHB 150`,
        `Drum (6gp) stock: ${rollDice(4)*4} | PHB 154`,
        `Horn (3gp) stock: ${rollDice(4)*3} | PHB 154`,
        `Shawm (2gp) stock: ${rollDice(4)*4} | PHB 154`,
        `Written song, derivative (5cp) stock: ${rollDice(4)} copies | Example: "The Dwarf Lass's Beard"`,
        `Bagpipes (30gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Chalumeau (15gp) stock: ${rollDice(4)*3} | Straight, wooden musical instrument, with reed`,
        `Cymbals (20gp/set) stock: ${rollDice(4)*3} sets`,
        `Flute (2gp) stock: ${rollDice(4)*4} | PHB 154`,
        `Lyre (30gp) stock: ${rollDice(4)*4} | PHB 154`,
        `Pan flute (12gp) stock: ${rollDice(4)*4} | PHB 154`,
        `Strings (2sp/5 strings) stock: ${rollDice(4)*5} strings | Good for restringing an instrument`,
        `Timbrel (13gp) stock: ${rollDice(4)*2} | A circular wood instrument with brass discs`,
        `Written song, catchy (5sp) stock: ${rollDice(4)} | Example: "A Tieing Went Down to Cormyr"`,
        `Adufe (10gp)stock: ${rollDice(4)*2} | A square, drum-like instrument that rattles`,
        `Dulcimer (25gp)stock: ${rollDice(4)*3} | PHB 154`,
        `Glockenspiel (35gp) stock: ${rollDice(4)*2} | Instrument of metal bars, struck with mallets`,
        `Instrument of the bards, Doss lute (500gp)stock: Only 1, ever | DMG 176`,
        `Lute (35gp) stock: ${rollDice(4)*3} | PHB 154`,
        `Pipes of haunting (500gp) stock: Only 1, ever | DMG 185`,
        `Pipes of the sewers (500gp) stock: Only 1, ever | DMG 185`,
        `Rebab (32gp) stock: ${rollDice(4)*2} | Long-knecked wooden string instrument`,
        `Viol (30gp) stock: ${rollDice(4)*3} | PHB 154`,
        `Written song, classic (5gp) stock: ${rollDice(4)} copies | Example: "Ghost Azers in the Sky"`,
        `Written song, inspired (50gp)stock: ${rollDice(4)} copies | Example: "4'33"`,
        `Chime of opening (2,500gp) stock: Only 1, ever | DMG 158`,
        `Gnomish saxophone (250gp) stock: ${rollDice(4)} | A brass musical instrument, covered in keys`,
        `Instrument of the bards, Canaith mandolin (5,000gp) stock: Only 1, ever`,
        `instrument of the bards, CI i lyre (5,000gp) stock: Only 1, ever | DMG 176`,
        `Written song, epic (500gp) stock: Only 1 copy, ever | Example: "FaerOnian Rhapsody"`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Songs and Instruments"
    bardInstruments.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function scrolls() {
    let spellsAndScrolls = [
        `Spell scroll, fake (25sp) stock: ${rollDice(4)} | A DC 10 Investigation check reveals it is fake`,
        `Calligrapher's supplies (10gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Case, scroll (1gp) stock: ${rollDice(4)*5} | PHB 150`,
        `Ink (10gp/ounce) stock: ${rollDice(4)*10} ounces | PHB 150`,
        `Ink pen (2cp) stock: ${rollDice(4)*5} | PHB 150`,
        `Parchment (1sp/sheet) stock: ${rollDice(4)*20} sheets | PHB 150`,
        `Spellbook, blank (50gp) stock: ${rollDice(4)*5} | PHB 150`,
        `Ritual book, 1st level (100gp) stock: ${rollDice(4)} | Contains a 1st - level ritual spell; can be copied`,
        `Ritual book 2nd level (100gp)stock: ${rollDice(4)} | Contains a 2nd - level ritual spell; can be copied`,
        `Ritual book, 3rd level (500gp) stock: ${rollDice(4)} | Contains a 3rd - level ritual spell; can be copied`,
        `Scroll, cantrip (50gp) stock: ${rollDice(4)*5} | DMG 200`,
        `Scroll, 1st level (50gp) stock: ${rollDice(4)*4} | DMG 200`,
        `Scroll, 2nd level (250gp) stock: ${rollDice(4)*4} | DMG 200`,
        `Scroll, 3rd level (250gp) stock: ${rollDice(4)*3} | DMG 200`,
        `Spell: Identify (20gp) stock: 3 spells / day | PHB 252 Tells you the properties of a magic item`,
        `Ritual book 4th level (5,000gp) stock: ${rollDice(4)} | Contains a 4th - level ritual spell;can be copied`,
        `Ritual book, 5th level (5,000gp) stock: ${rollDice(4)} | Contains a 5th - level ritual spell;can be copied`,
        `Ritual book, 6th level (50,000gp) stock: ${rollDice(4)-2} | Contains a 6th - level ritual spell;can be copied`,
        `Scroll, 4th level (2,500gp) stock: ${rollDice(4)*3} | DMG 200`,
        `Scroll, 5th level (2,500 gp) stock: ${rollDice(4)*2} | DMG 200`,
        `Scroll, 6th level (25,000 gp) stock: ${rollDice(4)*2} | DMG 200`,
        `Scroll of protection (2,500 gp) stock: ${rollDice(4)*3} | DMG 199 This scroll can be used by anyone, and protects any against a specific creature type`,
        `Spellbook, backup (5,000 gp) stock: ${rollDice(4)} | Touched to a spellbook: instantly copies it once`,
        `Manual of golems, clay (25,000 gp) stock: Only 1, ever | DMG 180`,
        `Scroll, 7th level (25,000gp) stock: ${rollDice(4)} | DMG 200`,
        `Scroll, 8th level (25,000gp) stock: ${rollDice(4)-2} | DMG 200`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Spell Tomes and Scrolls"
    spellsAndScrolls.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function fence() {
    let thievingMerchant = [
        `Book, "How to Steal" (25gp) stock: Only 1, ever | PHB 150 The outside is locked, and the inside is blank`,
        `Climber's kit (25gp) stock: ${rollDice(4)+2} | PHB 150`,
        `Grappling hook (2gp) stock: ${rollDice(4)+2} | PHB 150`,
        `Ladder, 10-foot (1sp) stock: ${rollDice(4)} | PHB 150`,
        `Rope, hempen (1gp/50ft.) stock: ${rollDice(4)*50} feet | PHB 150`,
        `Sack (1cp) stock: ${rollDice(4)*5} | PHB 150`,
        `Torch (1cp) stock: ${rollDice(4)*5} | PHB 150`,
        `Ammunition (*varies) stock: ${rollDice(4)*50} pieces | PHB 150 Prices are as listed in the PHB`,
        `Crowbar (2gp) stock: ${rollDice(4)*3} | PHB 150`,
        `Caltrops (1gp/20) stock: ${rollDice(4)*40} | PHB 150`,
        `Dagger (2gp) stock: ${rollDice(4)*4} | PHB 149`,
        `Disguise kit (25gp) stock: ${rollDice(4)*2} | PHB 754`,
        `Poison, basic (100gp/vial) stock: ${rollDice(4)*2} vials | PHB 150 Injury; can inflict 1d4 poison damage`,
        `Poisoner's kit (50gp) stock: ${rollDice(4)} | PHB 154`,
        `Shortbow (25gp) stock: ${rollDice(4)*2} | PHB 149`,
        `Signal whistle (5cp) stock: ${rollDice(4)*2} | PHB 150`,
        `Thieves' tools (25gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Crossbow, hand (75gp) stock: ${rollDice(4)*3} | PHB 149`,
        `Dice set (1sp) stock: ${rollDice(4)*2} | PHB 154 Also available weighted, for triple price`,
        `Drow poison (200gp/dose) stock: ${rollDice(4)+1} doses | DMG 258 Injury; can render target unconscious`,
        `Eversmoking bottle (500gp) stock: Only 1, ever | DMG 168`,
        `Forgery kit (15gp) stock: ${rollDice(4)} | PHB 154`,
        `Hat of disguise (500gp) stock: Only 1, ever | DMG 173`,
        `Playing card set (5sp) stock: ${rollDice(4)*3} | PHB 154 Also available marked, for double price`,
        `Rapier (25gp) stock: ${rollDice(4)} | PHB 150`,
        `Shortsword (10gp) stock: ${rollDice(4)} | PHB 150`,
        `Serpent venom (200gp/dose) stock: ${rollDice(4)} doses | DMG 258 Injury; can inflict 3d6 poison damage`,
        `Spyglass (1,000gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Cloak of elvenkind (500gp) stock: Only 1, ever | DMG 158`,
        `Dagger of venom (5,000gp) stock: Only 1, ever | DMG 167`,
        `Gloves of thievery (500gp) stock: Only 1, ever | DMG 172`,
        `Wyvern poison (1,200gp/dose) stock: ${rollDice(4)-1} doses | DMG 258 Injury; can inflict 7d6 poison damage`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Thieving Supplies"
    thievingMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function tools() {
    let toolsMerchant = [
        `Bucket (5cp) stock: ${rollDice(4)*2} | PHB 150`,
        `Shovel (2gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Block and tackle (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Dagger (2gp) stock: ${rollDice(4)} | PHB 149`,
        `Hammer (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Ladder, 10-foot (1sp) stock: ${rollDice(4)*2} | PHB 150`,
        `Lamp (1cp) stock: ${rollDice(4)*2} | PHB 150`,
        `Pick, miner's (2gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Pole, 10-foot (5cp) stock: ${rollDice(4)*2} | PHB 150`,
        `Spikes, iron (1gp/10) stock: ${rollDice(4)*40} | PHB 150`,
        `Torch (5sp) stock: ${rollDice(4)*4} | PHB 150`,
        `Wood (1cp/plank) stock: ${rollDice(4)*5} planks | Planks measure 2 in. x 4 in. x 5 ft. each`,
        `Abacus (2gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Carpenter's tools (8gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Cook's utensils (1gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Fishing tackle (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Hammer, sledge (2gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Handaxe (5gp) stock: ${rollDice(4)*2} | PHB 149`,
        `Lantern, bullseye (10gp) stock: ${rollDice(4)} | PHB 150`,
        `Lantern, hooded (5gp) stock: ${rollDice(4)} | PHB 150`,
        `Mason's tools (10gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Mirror, steel (5gp) stock: ${rollDice(4)} | PHB 150`,
        `Potter's tools (10gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Tinderbox (5sp) stock: ${rollDice(4)*2} | PHB 150`,
        `Weaver's tools (1gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Woodcarver's tools (1gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Alchemist's supplies (50gp) stock: ${rollDice(4)} | PHB 154`,
        `Cobbler's tools (5gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Crowbar (2gp) stock: ${rollDice(4)} | PHB 150`,
        `Glassblower's tools (30gp) stock: ${rollDice(4)} | PHB 154`,
        `Herbalism kit (5gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Magnifying glass (100gp) stock: ${rollDice(4)+1} | PHB 150`,
        `Navigator's tools (25gp) stock: ${rollDice(4)} | PHB 154`,
        `Painter's supplies (10gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Smith's tools (20gp) stock: ${rollDice(4)*2} | PHB 154`,
        `Tinker's tools (50gp) stock: ${rollDice(4)} | PHB 154`,
        `Gnomish army knife (100gp) stock: ${rollDice(4)} | Unfolds into up to 5 artisan's tools (you pick)`,
        `Gnomish tinderbox (50gp) stock: ${rollDice(4)} | Can instantly set alight small flammable objects`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Tools"
    toolsMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function vehicles() {
    let vehicleMerchant = [
        `Nag horse (5cp) stock: ${rollDice(4)} | Has 8 Strength and a movement speed of 20 ft.`,
        `Bit and bridle (2gp) stock: ${rollDice(4)*2} | PHB 157`,
        `Cart (15gp) stock: ${rollDice(4)} | PHB 157`,
        `Coach cab, ride (*varies) | PHB 159 Within a city: 1 cp; between towns: 3 cp / mile`,
        `Feed, animal (5cp/day) stock: ${rollDice(4)*30} days | PHB 157`,
        `Messenger service (2cp/mile) | PHB 159`,
        `Mule (8gp) stock: ${rollDice(4)*2} | MM 333 May instead be a donkey Ox 15 gp ${rollDice(4)*2} PHB 157`,
        `Pony (30gp) stock: ${rollDice(4)*2} | MM 335`,
        `Saddle, pack (5gp) stock: ${rollDice(4)} | PHB 157`,
        `Sled (20gp) stock: ${rollDice(4)} | PHB 157`,
        `Backpack (2gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Bedroll (1gp) ${rollDice(4)*2} | PHB 150`,
        `Carpenter's tools (8gp) stock: ${rollDice(4)} | PHB 154`,
        `Cartographer's tools (15gp) stock: ${rollDice(4)} | PHB 154`,
        `Draft horse (50gp) stock: ${rollDice(4)} | MM 321`,
        `Rowboat (50gp) stock: ${rollDice(4)} | PHB 157 Only sold if adjacent to a body of water`,
        `Saddle, riding (10gp) stock: ${rollDice(4)} | PHB 157`,
        `Saddlebags (4gp) stock: ${rollDice(4)} | PHB 157`,
        `Ship's passage, ride (1sp/mile) | PHB 159 Only sold if adjacent to a body of water`,
        `Wagon (35gp) stock: ${rollDice(4)} | PHB 157`,
        `Woodcarver's tools (1gp) stock: ${rollDice(4)} | PHB 154`,
        `Camel (50gp) stock: ${rollDice(4)} | MM 320`,
        `Folding boat (5,000gp) stock: Only 1, ever | DMG 170`,
        `Keelboat (3,000gp) stock: ${rollDice(4)} | PHB 157 Only sold if adjacent to a body of water`,
        `Navigator's tools (25gp) stock: ${rollDice(4)} | PHB 154 Only sold if adjacent to a body of water`,
        `Riding horse (75gp) stock: ${rollDice(4)} | MM 336`,
        `Saddle, military (20gp) stock: ${rollDice(4)} | PHB 157`,
        `Carpet of flying (50,000gp) stock: Only 1, ever | DMG 157 Size of the carpet is determined by the DM`,
        `Carriage (100gp) stock: ${rollDice(4)} | PHB 157`,
        `Chariot (250gp) stock: ${rollDice(4)} | PHB 157`,
        `Longship (10,000gp) stock: ${rollDice(4)-1} | PHB 157 Only sold if adjacent to a body of water`,
        `Sailing ship (10,000gp) stock: ${rollDice(4)-2} | PHB 157 Only sold if adjacent to a body of water`,
        `Warhorse (400gp) stock: ${rollDice(4)} | MM 340`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Vehicles and Transportation"
    vehicleMerchant.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}

function weapons() {
    let weaponTrader = [
        `Hammer (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Pole, 10 foot (5cp) ${rollDice(4)*2} | PHB 150`,
        `Ammunition (varies) stock: ${rollDice(4)*40} | PHB 150 Prices are as listed in the PHB`,
        `Simple melee weapons (varies) stock: ${rollDice(4)*15} | PHB 149 Prices are as listed in the PHB`,
        `Simple ranged weapons (varies) stock: ${rollDice(4)*15} | PHB 149 Prices are as listed in the PHB`,
        `Whetstone (1cp) stock: ${rollDice(4)*10} | PHB 150`,
        `Martial melee weapons (varies) stock: ${rollDice(4)*10} | PHB 149 Prices are as listed in the PHB`,
        `Quiver (1gp) stock: ${rollDice(4)*2} | PHB 150`,
        `Smith's tools (20gp) stock: ${rollDice(4)} | PHB 154`,
        `Ammunition, +1 (500gp/20) stock: ${rollDice(4)*20} | DMG 150 Must also pay the cost of the base ammunition`,
        `Javelin of lightning (500gp) stock: Only 1, ever | DMG 178`,
        `Martial ranged weapons (varies) stock: ${rollDice(4)*10} | PHB 149 Prices are as listed in the PHB`,
        `Quiver of Ehlonna (500gp) stock: Only 1, ever | DMG 189`,
        `Ram, portable (4gp)stock: ${rollDice(4)} | PHB 150`,
        `Sheath (8gp) stock: ${rollDice(4)*2} | Ornate leather holster for a dagger or sword`,
        `Shield (10gp) stock: ${rollDice(4)*2} | PHB 145`,
        `Weapon, +1 (500gp) stock: Only ${rollDice(4)}, ever | DMG 273 Must also pay the cost of the base weapon`,
        `Weapon of warning, any (500gp) stock: Only 1, ever | DMG 213 Must also pay the cost of the base weapon`,
        `Ammunition, +2 (5,000gp/20) stock: ${rollDice(4)*10} | DMG 150 Must also pay the cost of the base ammunition`,
        `Flame tongue, any (5,000gp) stock: Only 1, ever | DMG 170 Must also pay the cost of the base weapon`,
        `Frost brand, any (50,000gp) stock: Only 1, ever | DMG 177 Must also pay the cost of the base weapon`,
        `Oathbow (50,000gp) stock: Only 1, ever | DMG 183`,
        `Sword of sharpness, any (50,000gp) stock: Only 1, ever | DMG 206 Must also pay the cost of the base weapon`,
        `Vicious weapon, any (5,000gp) stock: Only 1, ever | DMG 209 Must also pay the cost of the base weapon`,
        `Weapon, +2 (5,000gp) stock: Only ${rollDice(4)}, ever | DMG 213 Must also pay the cost of the base weapon`,
    ]
    document.getElementById("Inventory").innerHTML = ""
    document.getElementById("Title").innerHTML = ""
    document.getElementById("Title").innerHTML = "Weapons"
    weaponTrader.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Inventory").appendChild(li);
    });
}


//LEGENDARY MERCHANTS
let astralTrader = [
    `Astral diamond (10,000gp/ea.) stock: Unlimited | May be used as a valid form of currency`,
    `Bag of holding (500gp) stock: Only ${rollDice(4)}, ever | DMG 153`,
    `Elemental compass (500gp) stock: Only 1, ever | Points to nearest portal to an elemental plane`,
    `Everbountiful soup kettle (500gp) stock: ${rollDice(4)} | Once per day: turns 2 gal. of water into enough soup to feed 6 people`,
    `Hourglass (25gp) stock: ${rollDice(4)*2} | PHB 150`,
    `Jar of preserving (500gp) stock: ${rollDice(4)} | Anything in jar does not age or require food / air`,
    `Mirror, steel (5gp) stock: ${rollDice(4)} | PHB 150`,
    `Obsidian mortar and pestle (250gp) stock: ${rollDice(4)} | Can grind any non-magical item to powder in 1d4 rounds`,
    `Oil of etherealness (2,500gp) stock: ${rollDice(4)} | DMG 183 Confers the effects of the etherealness spell`,
    `Potion of gaseous form (2,500gp) stock: ${rollDice(4)} | DMG 187 Confers the effects of the gaseous form spell`,
    `Potion of water breathing (250gp) stock: ${rollDice(4)} | DMG 188 Allows you to breathe water for up to an hour`,
    `Spell: Teleport (490gp) stock: 3 spells / day | PHB 281 Teleports to a location on the same plane`,
    `Spell: Teleportation circle (350gp) stock: 3 spells / day | PHB 287 Paying 20 times the cost allows you to create a permanent teleportation circle at your location`,
    `Amulet of the planes (50,000gp) stock: Only 1, ever | DMG 150`,
    `Cube of force (5,000gp) stock: Only 1, ever | DMG 159`,
    `Disintegration chamber (5,000gp) stock: Only 1, ever | Anything fully within this 1 ft.x 1 ft.x 1 ft.box is affected by a casting of the spell disintegrate`,
    `Gem of seeing (5,000gp) stock: Only 1, ever | DMG 172`,
    `Portable hole (5,000gp) stock: Only ${rollDice(4)}, ever | DMG 185`,
    `Spell: Control weather (640gp) stock: 3 spells / day | PHB 228 Changes the weather to conditions you dictate`,
    `Spell - Planar ally (360gp) stock: 3 spells / day | PHB 265 Summoned creature is free to act as it pleases`,
    `Spell: Plane shift (515gp) stock: 3 spells / day | PHB 266 Teleports to a location on a different plane`,
    `Cubic gate (500,000gp) stock: Only 1, ever | DMG 160`,
    `Iron flask (500,000gp) stock: Only 1, ever | DMG 178 Your DM decides what is within the iron flask`,
    `Spell: Astral projection (3,000gp) stock: 3 spells / day | PHB 215 Add 2, 200 gp to the cost for each creature this spell affects after the first, besides the caster`,
    `Spell: Gate (1,300gp) stock: 3 spells / day | PHB 244 Opens a stable portal to another plane`,
    `Well of many worlds (500,000gp) stock: Only 1, ever | DMG 213`,
]

let enchantmentTrader = [
    [
        `Quality Items Price Quantity`,
        `Random minor enchantment (100gp) stock: 3 enchants / day`,
        `Random major enchantment (500gp) stock: 3 enchants / day`,
        `Chosen minor enchantment (300gp) stock: 3 enchants / day`,
        `Chosen major enchantment (1,500gp) stock: 3 enchants / day`,
        `Random legendary enchantment (5,000gp) stock: 3 enchants / day`,
        `Excellent Chosen legendary enchantment (15,000gp) stock: 3 enchants / day`,
    ],
    [
        `Minor Enchantments`
        `Beacon - Bonus action: Item sheds bright light in 10 - foot radius, dim light for additional 10 feet. May extinguish with another bonus action.`,
        `Compass - Action: Learn which way is north.`,
        `Gleaming - This item never gets dirty.`,
        `Guardian - Grants a +2 bonus to initiative.`,
        `Language - This item grants know - ledge of a specific language chosen by the DM.`,
        `Sentinel - Item glows when within 120 feet of a specific type of creature chosen by the DM.`,
        `Unbreakable - This item can only be broken by special means.`,
        `Waterborne - Item can float in liquid, grants Advantage on checks to swim.`,
        `Major Enchantments`
        `Transforming - Action: Item changes into another item of the same type. A sword may turn into a different sword, or a pair of boots may turn into shoes.`,
        `Spider - Touched. Grants a climb speed equal to your movement speed.`,
        `Unseen - Item is permanently invisible.`,
        `Fleet - Grants a + 10 foot bonus to movement speed.`,
        `Flight - Action: Gain a flight speed equal to your movement speed until the end of your turn.`,
        `Glibness - Action: Gain advantage on all Charisma checks made within the next minute. Refreshes with long rest.`,
        `Night Eye - Grants darkvision out to 60 feet, or increases it by 60 feet.`,
        `Warding - Reaction: Gain advantage on a saving throw. Short rest refresh.`,
        `Legendary Enchantments`
        `Fearful - Bonus action: Adjacent creature must make a DC 15 Wisdom saving throw or be frightened of you until the end of your next turn. Short rest refresh.`,
        `Teleport - Bonus action: Teleport up to 15 feet in any direction.`,
        `Silent - Grants a + 10 bonus to Stealth.Lucky.Can add 1 d10 to any check, save, or attack. Short rest refresh.`,
        `Wall Walker - Bonus action: Can pass through solid objects until end of turn, which ejects you.Short rest refresh.`,
        `Vitality - Grants immunity to disease, poisons, and poison damage.`,
        `True Seeing - Grants truesight out to 60 feet, or increases it by 60 feet.`,
        `Fortitude - Increases your hit point max - imum by 15.`,
    ],
]

let feyMerchant = [
    [
        `Bag of tricks, rust (1 geas) stock: Only 1, ever | DMG 154`,
        `Boots of elvenkind (1 geas) stock: Only 1, ever | DMG 155`,
        `Bracers of archery (1 geas) stock: Only 1, ever | DMG 156`,
        `Cloak of elvenkind (1 geas) stock: Only 1, ever | DMG 158`,
        `Gloves of thievery (1 geas) stock: Only 1, ever | DMG 172`,
        `Quiver of Ehlonna (1 geas) stock: Only 1, ever | DMG 189`,
        `Sentinel shield (1 geas) stock: Only 1, ever | DMG 199`,
        `Cloak of displacement (2 geases) stock: Only 1, ever | DMG 158`,
        `Glamored studded leather (2 geases) stock: Only 1, ever | DMG 172`,
        `Ring of animal influence (2 geases) stock: Only 1, ever | DMG 189`,
        `Rod of the pact keeper + 2 (2 geases) stock: Only 1, ever | DMG 197`,
        `Warlock pact (3 geases) stock: Unlimited | PHB 105`,
        `Instrument of the bards, Anstruth harp (2 geases) stock: Only 1, ever | DMG 176`,
        `Oathbow (2 geases) stock: Only 1, ever | DMG 183`,
        `Ring of invisibility (3 geases) stock: Only 1, ever | DMG 191`,
        `Scimitar of speed (2 geases) stock: Only 1, ever | DMG 199`,
        `Vorpal sword, any (3 geases) stock: Only 1, ever | DMG 209`,
    ],
    [
        `d20 Geas`
        `Give your first - born child to the merchant.`,
        `Trade the merchant a simple lock of your hair.`,
        `Slay a particular fey, bring the merchant their head.`,
        `Bring the merchant a specific child, not your own.`,
        `Play a harmless trick on a specific powerful ruler.`,
        `Tell the merchant your single darkest secret.`,
        `Fake your own death, and assume a new identity.`,
        `Betray your friends in a specific way.`,
        `Give the merchant ${rollDice(4)} of your happiest memories.`,
        `Drink a mysterious potion the merchant offers you.`,
        `Steal a specific powerful item for the merchant.`,
        `You can speak only in rhyme for the next seven days.`,
        `Give the merchant a syllable of your name.`,
        `Lose proficiency in one instrument or artisan 's tools.`,
        `Never touch iron, or take 10 d10 radiant damage.`,
        `Trade an aspect of your beauty to the merchant.`,
        `Live as a fey hunting - dog for seven days.`,
        `Lose a specific, unmentioned, item on your person.`,
        `Become permanently charmed by the merchant.`,
        `If you use a specific word, a nearby object breaks.`,
    ],
]

let magicItemsMerchant = [
    `Bag of tricks, grey (500gp) stock: Only 1, ever | DMG 154`,
    `Dust of dryness (250gp) stock: Only ${rollDice(4)}, ever | DMG 166`,
    `Figurine of wondrous power, silver raven (500gp) stock: Only 1, ever | DMG 170`,
    `Immovable rod (500gp) stock: Only 1, ever | DMG 175`,
    `Ring of mind shielding (500gp) stock: Only 1, ever | DMG 191`,
    `Robe of useful items (500gp) stock: Only 1, ever | DMG 195`,
    `Rope of climbing (500gp) stock: Only 1, ever | DMG 197`,
    `Sending stones (500gp) stock: Only 1 set, ever | DMG 199`,
    `Wind fan (500gp) stock: Only 1, ever | DMG 213`,
    `Additional items (varies) | DMG 146 Up to 5 items found on Magic Item Table F`,
    `Bag of beans (5,000gp) stock: Only 1, ever | DMG 152`,
    `Broom offlying (500gp) stock: Only 1, ever | DMG 156`,
    `Crystal ball (50,000gp) stock: Only 1, ever | DMG 159`,
    `Deck of illusions (500gp) stock: Only 1 set, ever | DMG 167`,
    `Figurine of wondrous power, ivory goats (5,000gp) stock: Only 1 set, ever | DMG 169`,
    `Figurine of wondrous power, onyx dog (5,000gp) stock: Only 1, ever | DMG 170`,
    `Portable hole (5,000gp) stock: Only ${rollDice(4)} ever | DMG 185`,
    `Ring of feather falling (500gp) stock: Only 1, ever | DMG 193`,
    `Ring of free action (5,000gp) stock: Only 1, ever | DMG 191`,
    `Ring of the ram (5,000gp) stock: Only 1, ever | DMG 197`,
    `Staff of charming (5,000gp) stock: Only 1, ever | DMG 201`,
    `Wand of magic missiles (5,000gp) stock: Only 1, ever | DMG 211`,
    `Wand of wonder (5,000gp) stock: Only 1, ever | DMG 212`,
    `Additional items (varies) | DMG 147 Up to 5 items found on Magic Item Table G`,
    `Animated shield (50,000gp) stock: Only 1, ever | DMG 151`,
    `Cloak of arachnida (50,000gp) stock: Only 1, ever | DMG 158`,
    `Dancing sword, any (50,000gp) stock: Only 1, ever | DMG 161`,
    `Nolzur's marvelous pigments (50,000gp) stock: Only 1, ever | DMG 183`,
    `Staff of fire (50,000gp) stock: Only 1, ever | DMG 201`,
    `Wand of the war mage +3 (50,000gp) stock: Only 1, ever | DMG 212`,
    `Additional items (varies) | DMG 148 Up to 5 items found on Magic Item Table H`,
]

let magicCreaturesMerchant = [
    `Bit and bridle (2gp) stock: ${rollDice(4)*2} | PHB 157`,
    `Dire wolf (450gp) stock: ${rollDice(4)} | MM 321`,
    `Elk (60gp) stock: ${rollDice(4)} | MM 322`,
    `Feed, animal (5cp/day) stock: ${rollDice(4)*30} days | PHB 157`,
    `Flying snake (2gp) stock: ${rollDice(4)} | MM 322`,
    `Giant fire beetle (2gp) stock: ${rollDice(4)*2} | MM 325`,
    `Giant goat (300gp) stock: ${rollDice(4)} | MM 326`,
    `Giant lizard (350gp) stock: ${rollDice(4)} | MM 326`,
    `Giant wolf spider (400gp) stock: ${rollDice(4)} | MM 330`,
    `Saddle, exotic (60gp) stock: ${rollDice(4)+2} | PHB 157`,
    `Awakened shrub (25gp) stock: ${rollDice(4)} | MM 317`,
    `Blink dog (250gp) stock: ${rollDice(4)} | MM 318`,
    `Cockatrice (650gp) stock: ${rollDice(4)} | MM 42 Untamed`,
    `Dragon egg (750gp) stock: ${rollDice(4)-2} | Hatches with proper care after 90 days`,
    `Gelatinous cube (300gp) stock: ${rollDice(4)} | MM 242 Untamed`,
    `Giant bat (250gp) stock: ${rollDice(4)} | MM 323`,
    `Giant eagle (500gp) stock: ${rollDice(4)} | MM 324`,
    `Giant sea horse (500gp) stock: ${rollDice(4)} | MM 328 Only sold if adjacent to a body of water`,
    `Griffon (750gp) stock: ${rollDice(4)} | MM 174`,
    `Owlbear (750gp) stock: ${rollDice(4)} | MM 249 Untamed`,
    `Pegasus (750gp) stock: ${rollDice(4)} | MM 250`,
    `Pseudodragon (175gp) stock: ${rollDice(4)} | MM 254`,
    `Worg (300gp) stock: ${rollDice(4)} | MM 341`,
    `Basilisk (1,000gp) stock: ${rollDice(4)} | MM 24 Untamed`,
    `Bulette (1,500gp) stock: ${rollDice(4)} | MM 34 Untamed`,
    `Carrion crawler (800gp) stock: ${rollDice(4)} | MM 37 Untamed`,
    `Death dog (800gp) stock: ${rollDice(4)} | MM 321 Untamed`,
    `Displacer beast (1,250gp) stock: ${rollDice(4)} | MM 81 Untamed`,
    `Dragon wyrmling (2,500gp) stock: ${rollDice(4)-2} | MM 88-118 Untamed; may be of any color`,
    `Gorgon (1,500gp) stock: ${rollDice(4)-1} | MM 171 Untamed`,
    `Manticore (1,000gp) stock: ${rollDice(4)-1} | MM 213 Untamed`,
    `Mimic (800gp) stock: ${rollDice(4)} | MM 220 Untamed`,
    `Otyugh (1,250gp) stock: ${rollDice(4)} | MM 248 Untamed`,
    `Rust monster (800gp) stock: ${rollDice(4)} | MM 262 Untamed`,
    `Unicorn (1,750gp) stock: ${rollDice(4)-1} | MM 294 Untamed, except to those pure of heart`,
]

let necromanticMerchant = [
    `Acid (25gp/vial) stock: ${rollDice(4)*5} vials | PHB 150`,
    `Arcane focus (varies) stock: ${rollDice(4)} | PHB 150 Prices are as listed in the PHB`,
    `Dust of dryness (250gp) stock: Only ${rollDice(4)}, ever | DMG 166`,
    `Candle (1cp) stock: ${rollDice(4)*10} | PHB 150 Comes in black, grey, white, or red`,
    `Chain (5gp/10ft) stock: ${rollDice(4)*20} feet PHB 150`,
    `Chalk (1cp/piece) stock: ${rollDice(4)*10} pieces | PHB 150 Comes in black, grey, white, or red`,
    `Component pouch (25gp) stock: ${rollDice(4)} | PHB 150`,
    `Corpse, dead (4gp) stock: ${rollDice(4)*4} | An intact corpse perfect for necromancy`,
    `Dagger, ritual (2gp) stock: ${rollDice(4)*2} | PHB 148 Has an oddly curved design`,
    `Flesh (1sp/lb.) stock: ${rollDice(4)*20} lbs. | Best not to ask...`,
    `Holy symbol (varies) stock: ${rollDice(4)} | PHB 150 Prices are as listed in the PHB`,
    `Hourglass (25gp) stock: ${rollDice(4)*2} | PHB 150`,
    `Incense (1sp/block) stock: ${rollDice(4)*20} blocks | Thick, musky, and pungent`,
    `Lock (10gp) stock: ${rollDice(4)} | PHB 150`,
    `Manacles (2gp) stock: ${rollDice(4)*2} | PHB 150`,
    `Poison, basic (100gp/vial) stock: ${rollDice(4)} vials | PHB 150 Injury; can inflict 1d4 poison damage`,
    `Shovel (2gp) stock: ${rollDice(4)*2} | PHB 150`,
    `Spell: Animate dead (90gp) stock: 3 spells / day | PHB 212 3rd level; dead follow your commands for a day`,
    `Spell: Gentle repose (40gp) stock: 3 spells / day | PHB 245 Stops decay in a corpse, prevents undeath`,
    `Spell: Raise dead (1,250gp) stock: 3 spells / day | PHB 270 Returns a dead corpse to life`,
    `Spell: Speak with dead (90gp) stock: 3 spells / day | PHB 277 Allows you to speak to one non-undead corpse`,
    `Spellbook, blank (50gp) stock: ${rollDice(4)} | PHB 150`,
    `Weaver's tools (1gp) stock: ${rollDice(4)} | PHB 154`,
    `Amulet of health (5,000gp) stock: Only 1, ever | DMG 150`,
    `Cloak of the bat (5,000gp) stock: Only 1, ever | DMG 159`,
    `Bottomless bag of bones (500gp) stock: Only 1, ever | Contains an unlimited number of corpses only for use as raised minions in necromancy spells`,
    `Mask, plague doctor (50gp) stock: ${rollDice(4)} | Durable leather, with a long beak`,
    `Mask, skull (45gp) stock: ${rollDice(4)} | Made of actual bone`,
    `Pipes of haunting (500gp) stock: Only 1, ever | DMG 185`,
    `Spell: Create undead (1,260gp) stock: 3 spells / day | PHB 229 6th level; dead follow your commands for a day`,
    `Spell: Resurrection (2,490gp) stock: 3 spells / day | PHB 272 More potent way of restoring the dead to life`,
    `Wand of fear (5,000gp) stock: Only 1, ever | DMG 210`,
    `Manual of golems, (50,000gp) flesh stock: Only 1, ever | DMG 180`,
    `Potion of longevity (25,000gp) stock: Only ${rollDice(4)}, ever | DMG 188 Reduces your age by 1d6 + 6 years, usually`,
    `Spell: Clone (2,840gp) stock: 3 spells / day | PHB 222 Safeguards against death after 120 days`,
]

let devilishMerchant = [
    [
        `Bag of holding (500gp) stock: Only ${rollDice(4)}, ever | DMG 153`,
        `Bag of tricks, tan (500gp) stock: Only 1, ever | DMG 154`,
        `Daern's instant fortress (5,000gp) stock: Only 1, ever | DMG 160`,
        `Iron bands of Bilarro (5,000gp) stock: Only 1, ever | DMG 177`,
        `Mace of terror (5,000gp) stock: Only 1, ever | DMG 180`,
        `Rod of rulership (5,000gp) stock: Only 1, ever | DMG 197`,
        `Sword of life stealing (5,000gp) stock: Only 1, ever | DMG 206`,
        `Wand of fireballs (5,000gp) stock: Only 1, ever | DMG 210`,
        `Any desired item (varies) stock: ${rollDice(4)} add. items | Item quality no greater than rare`,
        `Belt of giant strength, fire (50,000gp) stock: Only 1, ever | DMG 155`,
        `Demon armor (50,000gp) stock: Only 1, ever | DMG 167`,
        `Figurine of wondrous power, obsidian steed (50,000gp) stock: Only 1, ever | DMG 170`,
        `Ioun stone, intellect (50,000gp) stock: Only 1, ever | DMG 176`,
        `Any desired item (varies) stock: ${rollDice(4)} add. items | Item quality no greater than very rare`,
        `Warlock pact (50,000gp) stock: Unlimited | PHB 105 Grants 1st level of warlock class, Fiend patron`,
        `Instrument of the bards, ollamh harp (500,000gp) stock: Only 1, ever | DMG 176`,
        `Iron flask (500,000gp) stock: Only 1, ever | DMG 178 Your DM decides what is within the iron flask`,
        `Talisman of ultimate evil (500,000gp) stock: Only 1, ever | DMG 207`,
        `Any desired item (varies) stock: ${rollDice(4)} add. items | Whatever the purchaser desires, of any quality`,
    ],
    [
        `1 Favor for Half Off (one item)`
        `Dump a suspicious vial in a nearby well.`,
        `Eat whole a buzzing, wriggling, live horsefly.`,
        `Smear a pentagram of blood at a specific holy site.`,
        `Say a specific fiend's name into the mirror, thrice.`,
        `Loosen the wheels on a nearby wagon.`,
        `Kill a noble's pet, leave it where it will be found.`,
        `Convince a child a prize awaits in the wilderness.`,
        `Publicly set alight a specific holy book.`,
        `Remove the head and hands of a specific statue.`,
        `Steal a local relic, leave it in a feed trough.`,
        `Toss a bag of mice into the local mill.`,
        `Instigate a bloody fight between complete strangers.`,
        `Coat the inn's woodpile in lamp oil.`,
        `Set a specific bridge on fire.`,
        `Leave a slaughtered black goat in the town square.`,
        `Dig up a specific corpse, hide its parts around town.`,
        `Publicly accuse a priest of practicing dark magic.`,
        `Steal food from a specific poor family, throw it away.`,
        `Spread rumors of a married couple's infidelity.`,
        `Roll twice again, disregarding 20. Favor involves both.`,
    ],
]

let timelostMerchant = [
    `Calculator (60gp) stock: ${rollDice(4)} | Tech (2); performs mathematical functions`,
    `Electric torch (50gp) stock: ${rollDice(4)} | Tech (1)`,
    `Entertainment pad (150gp) stock: ${rollDice(4)} | Tech (3)`,
    `Energy cell (15gp/each) stock: ${rollDice(4)*4}| DMG 268`,
    `Sending stones (500gp) stock: Only 1 set, ever | DMG 199 Made of a strange, smooth, colored substance`,
    `Wristwatch (55gp) stock: Only 1, ever | Reliably tells the time of day, runs on motion`,
    `Bead of force (5,000gp/6)stock: Only 6, ever | DMG 154`,
    `Boots of levitation (5,000gp) stock: Only 1 set, ever | DMG 155`,
    `Cube of force (5,000 gp)stock: Only 1, ever | DMG 151`,
    `Goggles of night (5,000gp) stock: Only 1, ever | DMG 172`,
    `Grenade, fragmentation (300gp/each) stock: ${rollDice(4)*2} | DMG 268 Tech (2)`,
    `Grenade, smoke (250gp/each) stock: ${rollDice(4)*2} | DMG 268 Tech (2)`,
    `Jetpack (3,500gp) stock: Only 1, ever | Tech (4)`,
    `Laser pistol (3,000gp) stock: Only 1, ever | DMG 268 Tech (4)`,
    `Laser rifle (4,500gp) stock: Only 1, ever | DMG 268 Tech (4)`,
    `Antimatter rifle (6,500gp) stock: Only 1, ever | DMG 268 Tech (4)`,
    `Apparatus of Kwalish (500,000gp) stock: Only 1, ever | DMG 159`,
    `Cloak of invisibility (500,000gp) stock: Only 1, ever | DMG 158`,
    `Grenade launcher (5,500gp) stock: Only 1, ever | DMG 268 Tech (4)`,
    `Screwdriver, acoustic (1,250gp) stock: Only 1, ever | Tech (3); Grants adv. on thieves' tools checks`,
    `Tome of clear thought (50,000gp) stock: Only 1, ever | DMG 208 Title: "Introduction to Quantum Physics"`,
    `Tome of understanding (50,000gp)stock: Only 1, ever | DMG 209 Title: "Farmer's Almanac"`,
]