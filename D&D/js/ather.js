/*###################Chance and array manipulation methods#########################*/
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
function rollDice(number) {
    result = (Math.floor(Math.random() * number))
    return result;
};
function rollArray(array) {
    let shuffled = shuffle(array)
    let index = Math.floor(Math.random() * shuffled.length)
    return `(Roll: ${index}/${shuffled.length}) ${shuffled[index]}`;
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
        let li = document.createElement("li");
        let text = document.createTextNode(item);
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
function loopPrintList(array, id) {
    array.forEach(function(item) {
        let li = document.createElement("li");
        let text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
function toWords(s) {
    let th = ['', 'thousand', 'million', 'billion', 'trillion'];
    let dg = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    let tn = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
    let tw = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];


    s = s.toString();
    s = s.replace(/[\, ]/g, '');
    if (s != parseFloat(s)) return 'not a number';
    let x = s.indexOf('.');
    if (x == -1)
        x = s.length;
    if (x > 15)
        return 'too big';
    let n = s.split('');
    let str = '';
    let sk = 0;
    for (let i = 0; i < x; i++) {
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
        let y = s.length;
        str += 'point ';
        for (let i = x + 1; i < y; i++)
            str += dg[n[i]] + ' ';
    }
    return str.replace(/\s+/g, ' ');
};
function printArray(array) {
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
    }
};
function reload() {
    location.reload()
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

/*==================================================================================*/
/*-----------------------------Page Scripts Below-----------------------------------*/
/*==================================================================================*/


function quest() {
    document.getElementById("Quest").innerHTML = ''
    let themeArray = ['Exploration', 'Comedy', `${searchArray(['Investigation', 'Mystery'])}`, 'Combat','Urban','Simulation (video game-like)',`${searchArray(['Kingmaker', 'Management'])}`, `${searchArray(['Action', 'Adventure'])}`, 'Horror', 'Espionage','Romance','Revenge',`${searchArray(['Collecting', 'Ranching'])}`]
    let goalArray = ['Money', 'Combat Power', 'Political/ influential Power','Rescue', 'Escape','Explore a new area','Retrieve','Thwart a plan', `Protect a ${searchArray(['place', 'NPC or PC', 'Artifact'])}`, `Win a ${searchArray(['small', 'large'])}-scale conflict`,'Settle a debt','clear a name']
    let rewardArray = ['Gold','Magic item','Lore/ knowledge','Cool but mostly useless items','Plot relevant item',`${searchArray(['NPC Contact', 'Ally', 'New Friend'])}`,`${searchArray(['New pet', 'New follower'])}`, `${searchArray(['New skill', 'New language'])}`, 'interesting trinket', `${searchArray(['Boon', 'Blessing','Charm'])}`, ,`Mundane ${searchArray(['Weapon', 'Armor', 'misc.'])} with a cool backstory`, 'Repairable broken item','New mode of transport', `${searchArray(['Property', 'Land and Title'])}`, 'Faction favor', 'Backstory connection', 'Trophy', `${searchArray(['Crafting materials', 'Crafting Recipes'])}`, 'Feats']
    let factionArray =['Home','Echos','Undead','Nature','Dragons','Gure','Gnolls','Fey','Radiant','Dieties']

    let actionTropes = ['Being a B.A.','Big trope hunting','Chase scene','Combat','Dueling','Escape','Fight scene','I have your index','Index to the rescue','Just in time','VIOLENCE']
    let crimeTropes = ['confidence (scams, frauds, tricks)','organized crime','Gambling',' sex trade','Smuggling','Thievery','Drugs','Vandalism','Victimhood','Abuse','kidnapping, hostages, abduction',' murder','terrorism','threatening','banishment','censorship','law enforcement','courtroom','execution','forensics','perp sweating','prison']
    let dramaTropes = ['Betrayal','confession','conflict','emotion','infidelity','price of power','rejection','revenge','serious','subverted innocence','had a hard life','victimhoom','violence']
    let espionageTropes = ['betrayal','Disguise','being watched','infauxmation','ninja','classified','stealth','truth and lies']
    let fairyTaleTropes = ['Abduction is love','Abusive parents','Aliens','an arm and a leg',`Androcles' lion`,'an ice person','animate inanimate objects','anthropomorphic personification','attention deficit... ooh, shiny!','back from the dead','bad boss','bears are bad news','beauty equals goodness','be careful what you wish for','the big bad wolf','big fancy castle','blue blood',' bothering by the book','bride and switch','cain and able','changeling tale','clingy macguffin','curse + escape clause','damsel in distress','dances and balls','david versus goliath','dead all along','deader than dead','deal with the devil','deceased parents are the best','distressed dude','doe snot like shoes',`don't go into the woods`,'double-in law marriage','dragon hoard','dragons prefer princesses','dude, wheres my respect?','due to the dead','earn your happy ending','enchanted forest','engagement challenge','evil matriarch','evil old folks','evil sorcere','evil tower of ominousness','exact eavesdropping','the fair folk','the fairest of them all','fairy devilmother','fairy godmother','fairy tale episode','fairy tale free-for-all','fake ultimate hero','fallen-on-hard-times job','faimly-unfriendly death','family-unfriendly violence','faux death','feminine women can cook','food chains','the fool','forbidden fruit','forced transformation','fractured fairy tale','gender flip','genie in a bottle','giant food','gingerbread house','girl in the tower','girl who fits the slipper','prince chamring','god save us from the queen','the good king','good princess, evil queen','greed','green-eyed monster','grimminfication','hair of gold, heart of gold','happily ever after','haunted castle','headless horseman','hedge of throns','heir club for men','hitchiker heroes','honorary uncle','hot witch','i know your true name','if i cant have you','impossible task','impossible theft','intangible theft','invisible to adults','involuntary shapeshifter','just liek robin hood','the kingdom','knight in shining armor','laser-guided karma','last request','law of inverse fertility','leaf boat','liminal time','little red fighting hood','love at first sight','mad scientists beautiful daughter','massive numbered siblings','malicious slander','macguffing guardian','meaningful name','merciful minion','mock millionaire','moving the goalposts','nameless narrative','noble fugitive','obfuscating stupidity','obnoxious-in-laws','offered the crown','offing the offpsring','off with his head!','old beggar test',
    'once upon a time','original position fallacy','our fairies are different','our witches are different','overprotective dad','pinnochio syndrome','please shoot the messenger','prince charming','princess for a day','princess protagonist','the promise',' proud beauty','the quest','rags to royalty','ragtag bunch of misfits','rash promise','re-headed stepchild','rescue romance','rip-van-winkle','royal brat','royal blood','rule of three','rule of seven','the runt at the end','the sandman','save the princess','schmuck banquet','scullery maid','secret identity','secret test of character','self-fulfilliong prophecy','shapeshifter shwodown','shapeshifting lover','she cleans up nicely','sibling triangle','soul jar','standard hero reward','swans a swimming','sweet and sour grapes','talking animal','threshold guardians','trail of bread crumbs','treacherous spirit chase',`true love's kiss`,'turtle island','Uriah Gambit','Wealthy ever after','what ever happened to the mouse?','When the clock strieks 12','wicked stepmother','wicked witch','Wonder child','year outside, hour inside','you have waited long enough','youngest child wins']
    
    let output = []
    function questBuilder(){
        output.push(`Faction: ${searchArray(factionArray)}`)
        output.push(`Goal: ${searchArray(goalArray)}`)
        output.push(`Reward: ${searchArray(rewardArray)}`)
        output.push(`Theme: ${searchArray(themeArray)}`)
        output.push(`Major trope: ${searchArray(fairyTaleTropes)}`)
        output.push(`Minor trope: ${searchArray(fairyTaleTropes)}`)
        output.push(`Subgenre: ${searchArray([`Action - ${searchArray(actionTropes)}`,`Crime - ${searchArray(crimeTropes)}`,`Drama - ${searchArray(dramaTropes)}`, `Espionage - ${searchArray(espionageTropes)}`  ])}`)
    }
    
    questBuilder()
    loopPrintList(output,"Quest")
};

function buildRace(n) {
    //0 is plural, 1 is singular
    let common = [
        ['Humans', 'Dwarves', 'High-Elves', 'Wood-Elves', 'Gnomes', 'Half-Elves', 'Halflings', 'Dragonborn', 'Drow'],
        ['Human',' Dwarf', 'High-Elf', 'Wood-Elf', 'Gnome', 'Half-Elf', 'Halfling','Dragonborn', 'Drow']
    ]
    let uncommon= [
        ['Half-Orcs', 'Tabaxi', 'Kobolds', 'Warforged','Simic Hybrids','Goliaths', 'Orcs', 'Leonin', 'Owlins','Yuan-Ti', 'Tortles',],
        ['Half-Orc', 'Tabaxi', 'Kobold', 'Warforged','Simic Hybrid', 'Goliath', 'Orc', 'Leonin', 'Owlin', 'Yuan-Ti','Tortle',] 
    ]
    let rare = [
        [ 'Aarakocras', 'Bugbears', 'Firbolgs', 'Goblins', 'Hobgoblins', 'Kenkus', 'Shifters', 'Tritons', 'Lizardfolk', 'Vedalken', 'Verdan', 'Locathah', 'Grungs', 'Centaurs', 'Loxodons', 'Minotaurs','Deep Gnomes', 'Duregars', 'Harengon', 'Sea Elves','Changelings', 'Eladrins'],
        [ 'Aarakocra','Bugbear', 'Firbolg', 'Goblin', 'Hobgoblin', 'Kenku','Shifter',  'Triton', 'Lizardfolk', 'Vedalken', 'Verdan', 'Locathah', 'Grung', 'Centaur', 'Loxodon', 'Minotaur', 'Deep Gnome','Duregar','Harengon', 'Sea Elf','Changeling', 'Eladrin']
    ]
    let vRare = [
        ['Tieflings','Genasi', 'Aasimar', 'Satyrs', 'Fairies',  'Shadar-Kai', 'Feral Tieflings','Kalashtar',],
        ['Tiefling', 'Genasi', 'Aasimar', 'Satyr', 'Fairy', 'Shadar-Kai', 'Feral Tiefling','Kalashtar', ]
    ]
    let eRare = [
        [ 'Astral Elves', 'Giffs', 'Hadozee', 'Plasmoids', 'Gith', 'Githyankis', 'Githzerais' ],
        [ 'Astral Elf', 'Giff', 'Hadozee', 'Plasmoid', 'Gith','Githyanki', 'Githzerai' ]
    ]
    function findRace(n) {
        let chance = rollDice(100)
        if (chance > 98) {
            return searchArray(eRare[n]);
        } else if (chance > 95) {
            return searchArray(vRare[n]);
        } else if (chance > 80) {
            return searchArray(rare[n]);
        } else if (chance > 50) {
            return searchArray(uncommon[n]);
        } else {
            return searchArray(common[n]);
        }
        //document.getElementById("Race").innerHTML = characterRace
    };
    return findRace(n)
};

function fiftyTwoCardDungeon(input){
    document.getElementById("Dungeon").innerHTML = ''
    document.getElementById("DungeonKey").innerHTML = '' 
    
            let simpleRiddle = [
        "It has a golden head. It has a golden tail. It has no body. Answer: A gold coin.", "It wears a leather coat to keep its skins in working order. Escorts you to other realms, without a magic portal. Answer: Book.", "It dampens as it dries. Answer: Towel.", "What has two hands on its face but no arms? Answer: A clock", "What kind of coat is always wet when you put it on? Answer: A coat of paint.", "Many have heard me, yet nobody has seen me. I won’t speak back unless spoken to. What am I? Answer: An echo.", "What five long word become shorter when you add two letters? Answer: Short", "What is not alive but grows, does not breaths but needs air. Answer: Fire", "Better old than young; the healthier it is, the smaller it will be. Answer: A Wound.", "This fire is smothered best not by water or sand but by words. Answer: Desire.", "Two friends stand and travel together, one nearly useless without the other. Answer: Boots", "Feed me and I will live, give me a drink and I will die. Answer: Fire.", "A curved stick and a straight twig means red sap and a snapped trunk. Answer: Death by arrow.", "No warning of Timber could have stopped the dropping petals. Answer: Death by axe.", "A fitting cravat for a poorly chosen suit. Answer: Death by hanging.", "I build castles, yet tear down mountains, make some men blind, and others see. What am I? Answer: Sand.", "As I was going to St Ives I met a man with 7 wives. Each wife had 7 kids. Each kid had 7 cats. Each cat had 7 kittens. How many were going to St Ives? Answer: 1.", "What do banana, grammar and assess all have in common? Answer: if you take the first letter and put it on the end of the word, reading it backwards they spell the same word.", "Twelve men walking by, twelve pears hanging high. Each took a pear and left eleven hanging there. How did it happen? Answer: Each is someone’s name.", 
        "River bridge crossing, look out for the guards. Can you spell that without any ‘R’s? Answer: T-H-A-T.", "What is it that you keep when you need it not, but throw out when you do need it? Answer: An anchor.", "The foolish man wastes me, The average man spends me, And wise man invests me, Yet all men succumb to me. What am I? Answer: Time.", "What is something that dawns on you even when it shouldn’t? Answer: The obvious.", "When you come to the end of all you know, I am there. Who am I? HINTS: I start out wonderful, but then begin worse. Answer: The letter W.", "What has four legs in the morning, two legs in the afternoon and three legs in the evening? Answer: A Man. when he was a child he crawled on all four, when he was older, he walked on two legs and when he was old aged, he used a cane.", "I’m made out of five letters, And I’m made out of seven letters; I have keys but I don’t have locks, I’m concerned with time, but not with clocks. Answer: A Piano.", "Forty white horses on a red hill. They champ, they stamp, and then stand still. Answer: Teeth.", "I can fly like a bird not in the sky, which can always swim and can always dry. I say goodbye at night and morning hi. I’m part of you what am I. I follow and lead as you pass, dress yourself in black my darkness lasts. I flee the light but without the sun, Your view of me would be gone. Answer: A shadow.", "I am what men love more than life, fear more than death or mortal strife, what dead men have and rich require. I’m what contented men desire. Answer: Nothing.", "Two men drink poisoned Iced Tea. One man drinks his fast and lives. The other man drinks his slow and dies. How is this possible? Answer: The poison is in the ice not the tea. The ice melts in the slower drinker’s tea.", "Towns without houses, forests without trees, mountains without boulders and waterless seas. Answer: A Map.", "Two bodies in one, the longer I stand, the faster I run. Answer: Hourglass.", "Men desire me in public, but fear me in private. Answer: Truth.", "What is so fragile, even speaking its name will break it? Answer: Silence.", "What must you first give to me in order to keep it? Answer: Your word.", "Though I’m tender, I’m not to be eaten, Nor — though, mint fresh — your breath to sweeten. Answer: Money. Legal tender; minted coins.", "You never see it, but it’s almost always there, and most people quickly notice when it’s absent. Answer: Oxygen/Breathable Air.", 
        "An untiring servant it is, carrying loads across muddy earth. But one thing that cannot be forced, is a return to the place of its birth. Answer: River.", "Blessed are the first. Slow are the second. Playful are the third. Bold are the fourth. Brave are the fifth. Answer: Answer: Blade.", "Brought to the table. Cut and served. Never eaten. Answer: Cards.", "It can pierce the best armor, And make swords crumble with a rub. Yet for all its power, It can’t harm a club. Answer: Rust.", "It is a journey whose path depends, on an other’s vision of where it ends. Answer: Book.", "Men seize it from its home, tear apart its flesh, drink the sweet blood, then cast its skin aside. Answer: Orange.", "Names give power, Magic to control. But what is broken, by naming it? Answer: Silence.", "Passed from father to son, And shared between brothers. Its importance is unquestioned, Though it is used more by others. Answer: Name.", "Today he is there to trip you up, And he will torture you tomorrow. Yet he is also there to ease the pain, When you are lost in grief and sorrow. Answer: Alcohol.", "In the form of fork or sheet, I hit the ground. And if you wait a heartbeat, You can hear my roaring sound. Answer: Lightning.", "I have no tears but I perspire, I stretch but cannot respire, I can jump, walk, run and dance, Though I have no mind. I’ll take a stance. What am I? Answer: A leg.", "The beast of the plains, it goes through the ground, constantly on the search for its next meal. While it hates the taste of dwarves and elves, it loves the taste of halfling. Answer: Bulette.", "This thing can stay completely hidden in even the broadest of daylight. In halls and rooms that monster waits to ambush its next victim. Watch out from below, because it is the floor that this thing waits. Answer: Rug of smothering.", "In the world below, almost everything below has a heart as dark as their surroundings. This thing is the one exception, giving a light glow in the world of the Underdark. Answer: Flumph.", 
        "You keep it, but it never ages. Once shared it is gone forever. Answer: Secret.", "I can bring down the mightiest of men. Nobody can defy me. I am the enemy of flight. Yet you can’t even sense my presence. What am I? Answer: Gravity", "The more you walk on me the more we get along, and while other may still use me, with you is where I belong. What am I? Answer: Shoes", "I give mirth and merriment and they say I smell quite old but I can turn a timid man into one that is quite bold. What am I? Answer: Wine", "I am green with envy when I am placed below the sky. I do not breathe the air you breathe but I never wonder why. If you go and shelter me, I simply shrink and die. The answer to this riddle is simply who am I? Answer: A plant", "I guard precious treasures and yet my body never moves, but I open like a book when something of yours is used. When finally I’m gutted always feel quite blue. I always feel so useless without the gold that I consume. What am I? Answer: A Treasure Chest", "My body’s thin and slender and I grow shorter every day. You can use my single purpose, and I’ll be sure to lead the way. When I am placed upon a pastry then my life is soon to fade. What am I? Answer: A candle", "I am what’s desired above of all fame and wealth. Without me it’s assured that you’ll begin to lose your health. I’m not a fluid dancer, but you can put me on a shelf. What am I? Answer: Food", "I give people purpose, I am the gardener pulling weeds. In fact I keep a watchful eye over everybody’s deeds. I am the cobbler making shoes I am the blacksmith shoeing steeds. What am I? Answer: A job", "Born by fire, stone, or rain I feel most comfortable at home on the planes. When I am out of my element, I feel much disarray. What am I? Answer: An elemental", "I am gifted to you only when I am unwanted. I have the power to kill kings or the lowliest paupers. My strength is unquestioned and I move far and wide, yet my power can falter from potions imbibed. What am I? Answer: Sickness or Disease", "The more you take out the bigger I get. What am I? Answer: A hole", 
        "I am green for some time, but blue thereafter. If it is dark, I am likely to eat you. What am I? Answer: Grue", "Up and down they go and travel, but never do they move an inch. Answer: Stairs", "8 _ _ _ 1 _ _ _ 2 0′ Answer: 549763 (Put all the numbers in alphabetical order)", "Halo of water, tongue of wood, skin of stone and long I’ve stood. My fingers short reach to the sky, inside my heart men live and die. What am I? Answer: Castle", "Flying on invisible wings. I am massive in size. Then if my master commands, I am as small as he wishes. All men wish to own me, but when I touch them, They cannot touch me. I cry when I am with my brothers. Darkness follows wherever I go. I’m a friend, I’m an enemy. I am freedom. What am I? Answer: A Cloud", "A face I do have, but see I do not. When they see my hands, they oft ponder in thought Answer: A watch", "The more you take, the more you leave behind. What am I? Answer: Footsteps", "What kind of room can you never enter? Answer: A Mushroom.", "What is long, brown, and sticky? Answer: A stick.", "What has a head and a tail, can flip but has no legs? Answer: A coin.", "What is black when you buy it, red when you use it, and white when you throw it away? Answer: Coal.", "What belongs to you, but other people use it more than you do? Answer: Your name.", "Tall I am young, Short I am old, While with life I glow, Wind is my foe. What am I? Answer: A candle.", "I can build castles, I can stop a flood, I can show the time flow, I can make people blind, I can make others see. What am I? Answer: Sand", "If I’m in front I don’t matter, If I’m in back I make everything be more, I am something yet I am nothing. What am I? Answer: Zero", 
        "I shine brightest in the dark. I am there but cannot be seen. To have me costs you nothing. To be without me costs you everything. Answer: Hope.", "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost everybody. Answer: Pencil lead.", "What goes round the house and in the house but never touches the house? Answer: The sun.", "What comes once in a minute, twice in a moment, but never in a thousand years? Answer: The letter M.", "He who has it doesn’t tell it. He who takes it doesn’t know it. He who knows it doesn’t want it. What is it? Answer: Counterfeit money.", "What goes round and round the wood but never goes into the wood? Answer: The bark of a tree.", "I have a little house in which I live all alone. It has no doors or windows, and if I want to go out I must break through the wall. Answer: A chick in an egg.", "There are four siblings in this world, all born together. The first runs and never wearies. The second eats and is never full. The third drinks and is always thirsty. The fourth sings a song forever. Answer: Water, fire, earth, wind.", "A cloud was my mother, the wind is my father, my son is the cool stream, and my daughter is the fruit of the land. A rainbow is my bed, the earth my final resting place, what am I? Answer: Rain.", 
        "Poke your fingers in my eyes and I will open wide my jaws. Linen cloth, quills or paper, all will split before my might. What am I? Answer: Shears/Scissors", "What goes with a carriage, comes with a carriage, is of no use to a carriage and yet the carriage cannot go without it? Answer: Noise.", "What stands on one leg with its heart in its head? Answer: A cabbage.", "It’s been around for millions of years, but it’s no more than a month old. What is it? Answer: The moon.", "I met a man with a load of wood which was neither straight nor crooked. What kind of wood was it? Answer: Sawdust.", "What binds two people yet touches only one? Answer: A wedding ring.", "I am the beginning of sorrow and the end of sickness. There’s no happiness without me nor is there sadness. I am always in risk, yet never in danger. You will find me in the sun, but I am never out of darkness. Answer: The letter S.", "What holds water yet is full of holes? Answer: A sponge.", "Lives without a body, hears without ears, speaks without a mouth, to which the air alone gives birth. Answer: An echo.", "What goes into the water red and comes out black? Answer: A red-hot poker.", "When one does not know what it is, then it is something. When one knows what it is, then it is nothing. Answer: A riddle.", "It is the beginning of eternity, the end of time and space, the beginning of the end and the end of every space. What is it? Answer: The letter E", "What tastes better than it smells? Answer: A tongue.",
            ];

    //1. Declare Card, Suit, and meaning array
            let dungeon = []
            let description = []
            let ent = ''

    //2. Declare more variables for initial setup
            let cardArrayA10 =  [1,2,3,4,5,6,7,8,9,10]
            let cardarray1113 = [11,12,13]
            let suitArray = ['C','H','S','D']
            const build = {
                            1:{
                                rooms:1,
                                DirN: -1
                                },
                            2: {
                                rooms:1,
                                DirN: 1
                            },
                            3: {
                                rooms:1,
                                DirN: 0
                            },
                            4:{
                                rooms:2,
                                DirN: searchArray([1,-1])
                            },
                            5:{
                                rooms:2,
                                DirN: searchArray([1,-1])
                            },
                            6:{
                                rooms:2,
                                DirN: searchArray([1,0])
                            },
                            7:{
                                rooms:2,
                                DirN: searchArray([1,0])
                            },
                            8:{
                                rooms:2,
                                DirN: searchArray([0,-1])
                            },
                            9:{
                                rooms:2,
                                DirN:searchArray([0,-1])
                            },
                            10:{
                                rooms:3,
                                DirN: searchArray([1,0,-1])
                            },
                            }
            const suit = {
                            'C': {
                                1:'Reanimating Foes: Bones or other similar structures litter the floor and an alter sits at the other end. After the heroes enter the room they begin animating and attack the party. Each one should be very easily killed but will keep reanimating until the altar is destroyed.',
                                2:`Mindless Terror: This could be a gelatinous ooze, a spreading toxic plant, or something similar. A mindless enemy that can't be reasoned with, and just attacking it is dangerous. The one advantage the heroes have is it is slow, they can easily outmaneuver it or just run away.`,
                                3:'A Hunting Pack of Animals: This group works well as a team, both to set each other up for attacks and to defend each other from the heroes. Alone though, they are no real threat so clever heroes should try to split them up and fight them one-on-one.',
                                4:`Chained Giant: This powerful creature is restrained, injured or otherwise in a weakened state. It would usually be a very difficult opponent but if the heroes can exploit it's weakness and don't let their guard down, they should make short work of it.`,
                                5:'Inspiring Leader and a Bunch of Goons: Whether through charisma or magic, the leader is able to empower people to fight harder. Take them out however and the minions will start to crumble and surrender.',
                                6:'Concealed Enemies: These creatures have blended in with the scenery to ambush adventurers. Perhaps they are stone gargoyles, water elementals in a puddle, or sentient torture devices. Regardless they should take unobservant heroes by surprise and even be able to conceal themselves again during the fight.',
                                7:`Sword and Sorcery: This could be a fragile but powerful fire mage with their dedicated bodyguard. Maybe an assassin who can hide in darkness and a warlock who controls shadows. Try and come up with a fun combination of a martial fighter and a spellcaster where one's abilities compliments the other's.`,
                                8:'Environmental Hazards: The heroes find a single powerful enemy with some control over the environment. This could be through spells, spiritual connection or technology but the enemy gains extra actions per turn they can spend to alter the environment around them. Heroes will start to learn what to expect during the fight and how to react to it but until then will be fighting at a disadvantage.',
                                9:'Life Drainer: This creature uses foul magics or unholy biology to steal life force from the heroes whenever it deals damage. Do the heroes try to brute force their way through this uphill battle or do they come up with a more ingenious plan?',
                                10:'Firing Squad: This would be fairly simple combat against a small squad of fighters, except a team of rangers shoot down at the heroes from a safe position. Shooting back is made difficult by their heavy cover but leaving them unopposed could be a disaster.',
                                11:{
                                    B:'Brute:This boss hits very hard and can take a lot of damage in return. If the heroes fight fairly then they would quickly become overwhelmed so they will need to fight cleverly instead. The boss could be easily distracted, lured into some kind of trap or whatever else the heroes can think of.',
                                    F:'Arcane Reservoir: Magical energy flows through this place. Players can tap into this to empower their spells or basic attacks, but doing do risks random backlash. Enemies they find will probably tap into this but be incredibly unstable as a result.'
                                },
                                12:{
                                    B:`Titan: This boss is particularly huge, possibly even the size of a large building. Fighting them effectively might require heroes climbing up the boss' body or making use of multiple levels or balconies in the room.`,
                                    F:'Shifting Dimensions: Each room of the dungeon takes place in a different plane. The monsters and traps should change with it but will likely be eldritch and incomprehensible. The boss will shift planes and change completely during the fight.'
                                },
                                13:{
                                    B:'Martial Adept: The boss is an expert of their fighting style, easily able to outpace the heroes with showy feats of skill or see through a ruse. To stand a chance, the heroes will need to change the rules and fight the boss in a way they dont excel at.',
                                    F:`Malevolent Sentience: The dungeon is alive. This could be through technology, some kind of hive mind, or maybe it's just a giant mimic. Regardless, it is aware of the players and definitely wants them gone. It might even be able to communicate in some way.`
                                },
                                },
                            'H': {
                                1:'Secret Shopkeep: A goblin or similar creature has set up a small business selling scavenged goods from failed adventurers. Their wares are mostly useless but they do have the odd magic item at suspiciously low prices.',
                                2:`Abandoned Shrine: A lost shrine to a forgotten God lies in ruins, with signs of previous offerings scattered around it. Heroes can take some time to worship at it or even leave an offering to try and gain the god's favour. Depending on the nature of the god however, that may not be something they want.`,
                                3:`A Dark Bargain: A shady figure, maybe a vampire or warlock, appears out of the shadows and offers the heroes a deal. In exchange for a small amount of the hero's life force, they will give them a powerful boon. Try and make this something that will be particularly useful against the boss.`,
                                4:'Damaged Automaton: This creature could be mechanical, magical or just regular organic, but it is badly damaged and needs assistance. If the heroes are able to repair it then it offers to help them however it can.',
                                5:`A Test of Wits: A shady stranger poses the heroes a riddle (${searchArray(simpleRiddle)}), question or another test of intelligence. Giving the correct answer will likely reward money, gear or power but getting it wrong could be very dangerous indeed.`,
                                6:`Alchemist's Greenhouse: A vast, abandoned nursery of alchemical ingredients are growing unchecked with a small lab that was clearly once used for making potions. A hero who knows what they're doing could make a good profit by grabbing some cuttings, or even use the gear to make some potions.`,
                                7:'A Mighty Deed: A storyteller has taken residence in this room, hoping to hear exciting tales from passing adventurers. An impressive enough story will earn a small reward as payment. A truly outstanding tale could cause the storyteller to leave the dungeon immediately to share it with the world.',
                                8:'Wishing Well: A small pool of opaque water a foot or so deep sits in the centre of the room with an ominous inscription. Making a request and throwing in money or gear causes them to immediately sink out of sight and be lost. The more valuable the item the more likely the request will be granted accurately.',
                                9:`Tempting Fate: An unassuming deck of tarot cards sits on a small table. Drawing one card while in this room (draw from just the major arcana if you have a deck or roll a dice if you don't) will give you a glimpse of your near future, and appropriate temporary effect. Does the deck read the future or twist it? We may never know.`,
                                10:'Saferoom: This was the last thing you expected to find, a room in the dungeon that is completely free of danger. Whether due to a magical field or simply locks on the doors, heroes can rest in this room for as long as they need without anyone needing to keep watch.',
                                11:{
                                    B:'Illusionist: At the start of combat, the boss summons three copies of themselves. Once any of them have taken a third of their health secretly roll to see if it was the real one. Copies die after taking a third of the bosses max health or when the original dies.',
                                    F:`Forbidden Ritual: The boss is being summoned by a group of cultists. The boss starts less powerful and is joined by five cultists. At the end of each round add one 'tick' to the summon for each cultist still alive. At ten ticks the boss is fully summoned and much more powerful than normal.`
                                },
                                12:{
                                    B:'Elementalist: This spellcaster has mastered four schools of magic, possibly the four elements.Pick four sets of spells for this boss each themed around an element. Each round they can cast twice the normal amount but must pick from two different sets.',
                                    F:`Banishing Tools: The boss should be set up as close to the entrance as possible as long as they don't block any area. They are far more powerful than normal but in the first room of each suit is an item that weakens them slightly. With all four the fight is much easier.`
                                },
                                13:{
                                    B:'Summoner: This boss can summon hordes of minions and prefers to stand behind them. These minions should be fairly weak, a barrier to the boss but not the main threat in the fight.',
                                    F:`Deathly Presence: The boss has corrupted the dungeon by simply being there. Occasionally on regular floors, and more frequently when fighting the boss, heroes will have to seek out 'havens' or take damage as a foul miasma threatens to overwhelm them.`
                                },    
                                },
                            'S': {
                                1:'Rolling Boulders and Falling Floors: Speed and precision will be paramount here. Give players the option to take risky shortcuts and dangerous jumps if they start to get in trouble. If a player starts finding it too easy then offer some tempting loot they would need to slow down for.',
                                2:'Rising Threat: Something dangerous is rising up through the floor and the only way out is up. Strength and athletics are key, but let particularly strong or successful heroes slow down to help out those that are falling behind.',
                                3:`A Button Each: To open the door, several buttons behind different tests of skills need to be pressed at once. By some fortunate coincidence though, there are as many traps as there are heroes and the skill tests perfectly line up with their own skills. Give each Hero a chance to shine or, for some reason, a test that doesn't suit them.`,
                                4:'Mysterious Levers and Swinging Blades: The locked door is at the opposite end of a corridor to nine confusingly labelled levers. If you like you can make an actual puzzle to work out which one to pull or you could just ask for a skill check. For each incorrect lever pulled, swinging blades fall from the walls making the journey to the door much harder and more dangerous.',
                                5:'Big Chasm: It’s not very subtle, but it does the job. The door is on the other side of a massive ravine. A range of options here including climbing along the ceiling, fashioning some kind of bridge or just falling back to magic.',
                                6:`The Sentinel: This room is filled with pillars, plinths and an invulnerable golem. Fighting it won't achieve much more than slowing it down or distracting it, and a stealthier approach is liable to fail with a single bad roll. Heroes than use teamwork to combine the two will have the best chance of success here.`,
                                7:'Pressure Plates and Poison Arrows: Only one path over the patterned floor is safe, steeping an inch out of line will cause poison darts to fly from the walls. Figuring out the pattern would make the walk easier, but this will likely come down to walking very carefully.',
                                8:`Slippery Floors: The floor in this room is so slick it is hard to change direction and harder still to stop moving. This wouldn't be an issue if it wasn't for the spiky pillars, pits and walls which careless heroes could launch themselves into at a high speed.`,
                                9:`Magical Wards: A series of magical runes protect the doorway or corridor. If the heroes don't notice then they will be the target of a destructive spell. If they do find it then they will need to figure out a way to trigger it while standing a safe distance away. Try and theme the spells on the final boss. If the boss is a spellcaster then this could be a good chance to foreshadow one of their abilities.`,
                                10:'Deadly Plants: The room is overgrown with poisonous, acidic or otherwise harmful flora. Have these plants naturally grown like this or have they been engineered by an overzealous botanist? A particularly hardy hero may be able to just hack their way through it, but one with survival skills may know some tricks to avoiding harm.',
                                11:{
                                    B:`Stationary: For whatever reason, this boss is unable to move, but that doesn't stop them from being deadly. They should have a dangerous ranged attack and a melee attack that affects multiple heroes, perhaps it can use both each round to be extra deadly.`,
                                    F:'Wizards Tower: This tower was once, or still is, the home of a mighty wizard. Dangerous books line numerous bookshelves, sentient furniture aim to hinder the heroes and magical artifacts lie scattered on abandoned worktables. All encounters are almost certainly a little magical and probably sufficiently whimsical.'
                                },
                                12:{
                                    B:'Nimble: The boss is annoyingly hard to pin down. Expect them to be fairly unimpeded by the heroes, possibly even able to fly or climb walls. A melee boss will run between targets to find the weak link while a ranged boss able to dart between vantage points or away from danger to line up the perfect shot.',
                                    F:'Crumbling Ruins: This complex could once have been a mighty underground city or a place of worship. Now it is in such disrepair that simply getting around is a challenge. Have traps or hazards show up in most of the rooms to represent the difficult terrain but also feel free to scatter minor relics to represent ancient treasures.'
                                },
                                13:{
                                    B:'Unstoppable: This boss is unstoppable when they get moving and fond of shoving heroes around. As well as any regular attacks, they will usually try and push heroes into hazards or away from allies.',
                                    F:'Defended Fort: More than just a mere dungeon, the boss is using this building as a hideout and it is full of minions. Just entering the building may become a big part of the challenge. Combat rooms will likely be full of elites and even non-combat rooms might have the odd guard patrol.'
                                },    
                                },
                            'D': {
                                1:`Enchanted Gadgets: A small cache of magical trinkets is hidden in the stone wall . Not anything particularly powerful like a 'proper' magic item but a few small gadgets that a clever hero could use to their advantage.`,
                                2:'Abandoned Camp: There are signs that someone was living here, though they must have left in a hurry. A few basic tools and weapons and some supplies lie forgotten.These are unlikely to be of value, but they are exactly the sort of items a traveling adventurer needs.',
                                3:`Forgotten Forge: Most of the weapons have rusted away but there are a few basic melee weapons that are still usable. If the heroes inspect closer, they'll find a slightly hidden strongbox in the corner of the room. Inside is a perfectly preserved magical ${searchArray(['melee','ranged'])} weapon.`,
                                4:`Suspicious Armour Stands: In a line of ornamental armour displays, one stands out as being much more intact and possibly magical. Miraculously though, it doesn't come alive and start killing the heroes. Instead it is a suit of magical armour one of the heroes can wear.`,
                                5:'Almost Too Easy...: An almost completely dark room, the only light focused upon a displayed magic ranged weapon. Removing it causes an ominous grinding sound and a consequence later in the dungeon.',
                                6:`Tinker's Workshop: An tinker's workshop in a state of chaos. A selection of tools and blueprints are scattered around but the heroes' gaze is drawn to a single item sitting on a desk in front of a dead body. This item could be basically anything but in addition to its normal effects, the tinkerer accidentally transferred their sentience into it.`,
                                7:'Magic Library: An old, rotting library filled with ancient but damaged tomes. Even damaged, a hero or client with an interest in history would love to read what they can decipher. More interestingly though, there is a hidden compartment in the wall with a small selection of spell scrolls.',
                                8:`Enchanted Stream: A constant stream has eroded a small crack in the dungeon wall from which it continuously flows. This wouldn't be noteworthy except the liquid changes colour and glows slightly. When bottled it holds its colour and becomes a random potion.`,
                                9:'Cave Critter: You hear a small scuttling sound and eventually find a small dungeon animal running around. Somehow though, it is wearing a magic item of clothing clearly not designed for it. Heroes can try and catch it, but the aforementioned magic item will make this harder.',
                                10:`Extreme Luxury: You're not sure how they got here, but there are several locked strongboxes filled with valuables. This could be extravagant clothing, fine jewellery, ornate trinkets or whatever else you can imagine. To keep it interesting though, consider personalising the loot to be stuff the heroes might want to keep rather than immediately sell on.`,
                                11:{
                                    B:'Double Act: This duo works well as a team both to set each other up for attacks and to defend each other from the heroes. Alone though they are no real threat so clever heroes should try to split them up and fight them one-on-one.',
                                    F:'Volcano: The dungeon is in an active volcano and is largely made of platforms or bridges over pools of lava. Adventurers and enemies can fall, or be pushed, into the hot magma but the boss will be immune or even use it to their advantage.'
                                },
                                12:{
                                    B:'Replication: When the boss is defeated, the heroes are given just enough time to celebrate before the dead body splits into two weaker versions which restart combat. These halves will split one more time before they eventually stay dead.',
                                    F:'Tidal Caves: This dungeon is on the coast so claustrophobic rooms and corridors might be prone to flooding or even permanently underwater. For all the players are going to struggle, enemies will likely be unaffected and the boss will have some control over the water.'
                                },
                                13:{
                                    B:'Evil Party: The boss is actually a group of fighters, with matching size and skill set to the heroes (just more evil). When the bosses are all alive they can aid each other and each deal bonus damage. When each one dies this bonus is reduced.',
                                    F:'Endless Caverns: The dungeon is part of a giant cave complex with high ceilings and deep chasms. Expect flying enemies, rickety bridges and creatures lurking in the depths. The boss should combine all three.'
                                },    
                                }, 
                            }    
            let direction = 0 //0 = N, 1= E, 2 = S 3 = W
            let currentSize = 0
            let currentX = 0
            let currentY = 0
            let currentZ = 0

    //3. Declare the if/then rules based on the returned random card, including storing direction logic
            function modifyCoords(dir,op1,op2,op3){
                let addedRoom = []
                if (dir === 0){
                    if (op1 ===1){
                        currentX -= 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                    if (op2 ===1){
                        currentY += 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                    if (op3 ===1){
                        currentX += 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                } else if (dir === 1) {
                    if (op1 ===1){
                        currentY += 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                    if (op2 ===1){
                        currentX += 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                    if (op3 ===1){
                        currentY -= 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                } else if (dir === 2) {
                    if (op1 ===1){
                        currentX += 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                    if (op2 ===1){
                        currentY -= 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                    if (op3 ===1){
                        currentX -= 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                } else {
                    if (op1 ===1){
                        currentY -= 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                    if (op2 ===1){
                        currentX -= 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                    if (op3 ===1){
                        currentY += 1
                        let a = [currentX,currentY,currentZ]
                        if (checkConflict(a,dungeon) === 1) {
                            do {
                                currentZ += searchArray([-1,1])
                                a = [currentX,currentY,currentZ]
                            } while (checkConflict(a,dungeon)=== 1) 
                                addedRoom.push(a)
                        } else {
                            addedRoom.push(a)
                        }
                    }
                }
                return addedRoom
            };
            function checkDir(direction, change){
                if (direction + change > 3) {
                    direction = 0
                } else if (direction + change < 0) {
                    direction = 3
                } else {
                    direction += change
                }
            };
            function builder(card){
                if (card === 1) {
                    let newRooms = modifyCoords(direction,1,0,0)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=1
                    return newRooms
                } else if (card === 2){
                    let newRooms = modifyCoords(direction,0,0,1)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=1
                    return newRooms
                } else if (card === 3){
                    let newRooms = modifyCoords(direction,0,1,0)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=1
                    return newRooms
                } else if (card === 4){
                    let newRooms = modifyCoords(direction,1,0,1)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=2
                    return newRooms
                } else if (card === 5){
                    let newRooms = modifyCoords(direction,1,0,1)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=2
                    return newRooms
                } else if (card === 6){
                    let newRooms = modifyCoords(direction,1,1,0)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=2
                    return newRooms
                } else if (card === 7){
                    let newRooms = modifyCoords(direction,1,1,0)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=2
                    return newRooms
                } else if (card === 8){
                    let newRooms = modifyCoords(direction,0,1,1)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=2
                    return newRooms
                } else if (card === 9){
                    let newRooms = modifyCoords(direction,0,1,1)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=2
                    return newRooms
                } else if (card === 10){
                    let newRooms = modifyCoords(direction,1,1,1)
                    let change = build[card].DirN
                    checkDir(direction, change)
                    currentSize +=3
                    return newRooms
                }
            };

    //4. Complete the room array with the desired number of rooms  
            function buildDungeon(num){
                while (currentSize <= num) {
                    let card = searchArray(cardArrayA10)
                    let output = builder(card)
                    dungeon = dungeon.concat(output)
                }       
            };

    //5. find the furthest room in the array - draw a boss card and a modifier card
            function bossDesc(array){
                let boss2 = [suit[searchArray(suitArray)][searchArray(cardarray1113)].B,suit[searchArray(suitArray)][searchArray(cardarray1113)].F]
                array.push(`BOSS: ${boss2[0]} || ${boss2[1]}`)
            };

            //5.1 Order the array by Z value         
            function compareFn(a, b) {
                if (a[3] > b[3]) {
                    return 1
                }
                if ((a[3] < b[3])) {
                    return -1
                }
                return 0
            };
            
    //6. Iterate over the array and fill it with other cards based on the rules 
            function addEncounters(num,array){
                let a = []
                let c = []
                while (a.length < num - 1){
                    a.push(suit[searchArray(suitArray)][searchArray(cardArrayA10)])
                }
                c.push(ent)
                let b = a.concat(array)
                    do {
                        let z = searchArray(b)
                        if (checkConflict(z,c) === 0){
                            c.push(z)
                        }
                    } while (c.length <= num-1)
                return c
            };

    //7. Design the array so that it prints easily, likely storing each room as a number
            //TODO - create 2d or 3d render

    //8. store room descriptions in a key to be printed as well


    //9. theme the dungeon and dress the rooms


            let tortureFurnishings = [
                "bastinadoes", "bell(huge)", "bench", 'boots(iron)', 'branding irons', 'brazier', 'cage', 'chains', 'chair with straps', 'clamps', 'cressets', 'fetters', 'fire pit', 'grill', 'hooks', 'iron maiden', 'knives', 'manacles', 'oubliette', 'oil(barrel of)', 'pillory', 'pincers', 'pliers', 'pot(huge)', 'rack', 'ropes', 'stocks', 'stool', 'strappado', 'straw', 'table', 'tongs', 'thumb screws', 'torches', 'rack', 'vice', 'well', 'wheel', 'whips',
            ];
            let containerContents = [
                'ash', 'bark', 'bone', 'chunks', 'cinders', 'crystals', 'dust', 'fibers', 'gelatin', 'globes', 'grains', 'greasy', 'husks', 'leaves', 'liquid', 'lump(s)', 'oily', 'paste', 'pellets', 'powder', 'semi-liquid', 'skin/hide', 'splinters', 'stalks', 'strands', 'strips', 'viscous',
            ];
            let arcaneFurnishings = [
                'alembic', 'balance & weights', 'beaker', 'bellows', 'bladder', 'bottle', 'book', 'bowl', 'box', 'brazier', 'cage', 'cauldron', 'candle', 'candlestick', 'carafe', 'chalk', 'crucible', 'cruet', 'crystal ball', 'decanter', 'desk', 'dish', 'flask', 'funnel', 'furnace', 'herbs', 'horn', 'hourglass', 'jar', 'jug', 'kettle', 'ladle', 'lamp', 'lens(concave, convex, etc...)', 'magic circle', 'mortar & pestle', 'pan', 'parchment', 'pentacle', 'pentagram', 'phial', 'pipette', 'pot', 'prism', 'quill', 'retort', 'rod, mixing / stirring', 'scroll', 'scroll tube', 'sheet', 'skin', 'skull', 'spatula', 'spoon, measuring', 'stand', 'stool', 'stuffed animal', 'tank(container)', 'tongs', 'tripod', 'tube(container)', 'tube(piping)', 'tweezers', 'vial', 'waterclock', 'wire', 'workbench',
            ];
            let miscItems = [
                'awl', 'bandages', 'basin', 'basket', 'beater', 'book', 'bottle', 'bowl', 'box(small)', 'brush', 'candle', 'candle snuffer', 'candlestick', 'cane(walking stick)', 'case', 'casket(small)', 'chopper', 'coffer', 'cologne', 'comb', 'cup', 'decanter', 'dipper', 'dish', 'earspoon', 'ewer', 'flagon', 'flask', 'food', 'fork', 'grater', 'grinder', 'hourglass', 'jack(container)', 'jar', 'jug', 'kettle', 'knife', 'knucklebones', 'ladle', 'lamp/lantern', 'masher', 'mirror', 'mug', 'needle(s)', 'oil, cooking(or fuel)', 'oil fuel', 'oil, scented', 'pan', 'parchment', 'pitcher', 'pipe, musical', 'pipe, smoking', 'plate', 'platter', 'pot', 'pouch', 'puff', 'quill', 'razor', 'rope', 'salve', 'saucer', 'scraper', 'scroll', 'shaker', 'sifter', 'soap', 'spigot', 'spoon', 'stopper', 'statuette / figurine', 'strainer', 'tankard', 'tongs', 'thread', 'tinderbox(with flint & steel)', 'towel', 'tray', 'trivet', 'tureen', 'twine', 'unguent', 'vase', 'vial', 'wallet', 'washcloth', 'whetstone', 'wig', 'wool', 'yarn',
            ];
            let clothes = [
                'apron', 'belt', 'blouse', 'boots', 'buskins', 'cap', 'cape', 'cloak', 'coat', 'coif', 'doublet', 'dress', 'frock / pinafore', 'gauntlets', 'girdle', 'gloves', 'gown', 'hat', 'hood', 'hose', 'jerkin', 'kerchief', 'leggings', 'linen(drawers)', 'linen(undershirt)', 'mantle', 'pantaloons', 'petticoat', 'pouch / purse', 'robe', 'sandals', 'scarf', 'shawl', 'slippers', 'smock', 'stockings', 'surcoat', 'toga', 'trousers', 'tunic', 'veil', 'vest', 'wallet', 'wrapper',
            ];
            let religiousArticles = [
                "altar", "bell(s)", "brazier(s)", "candleabra", "candles", "candlesticks", "chime(s)", "cloth(altar),", "columns/pillars", "curtain/tapestry", "drum", "font (consecrated water container)", "gong", "holy/unholy symbol(s)", "holy/unholy writings", "idol(s)", "incense burner(s)", "kneeling bench", "lamp(s)", "lectern", "mosaics", "offertory container", "paintings/frescoes", "pews", "pipes(musical)", "prayer rug", "pulpit", "rail", "robes", "sanctuary", "screen", "shrine", "side chair(s)", "stand", "statues(s)", "throne", "vestry", "vestments", "votive light", "whistle",
            ];
            let airCurrents = [
                "a slight breeze", "a slight damp breeze", "a gusting breeze", "a cold current", "a slight downdraft", "a strong downdraft", "still", "still and very chilly", "still and warm","still and hot", "a slight updraft", "a strong updraft", "a strong wind", "a strong gusting wind", "a strong moaning wind",
            ];
            let generalFeatures = [
                "arrow, broken", "ashes", "bones", "bottle, broken", "chain, corroded", "club, splintered", "cobwebs", "coin, copper(bent)", "cracks, ceiling", "cracks, floor", "cracks, wall", "dagger hilt", "dampness, ceiling", "dampness, wall", "dripping", "dried blood", "dung - small creature", "dust", "flask, cracked", "food scraps", "fungi, common", "guano", "hair / fur bits", "hammer head, cracked", "helmet, badly dented", "iron bar, bent, rusted", "javelin head, blunt", "leather boot", "leaves(dry) & twigs", "mold(common)", "pick handle", "pole, broken", "pottery shards", "rags", "rope, rotten", "rubble & dirt", "sack, torn", "slimy coating, ceiling", "slimy coating, floor", "slimy coating, wall", "spike, rusted", "sticks", "stones, small", "straw", "sword blade, broken", "teeth/fangs, scattered", "torch stub", "wall scratchings", "water, small puddle", "water, large puddle", "water, trickle", "wax blob(candle stub)", "wood pieces, rotting",
            ];
            let odors = [
                "acrid smell", "chlorine smell", "dank, moldy smell", "earthy smell", "manure smell", "metallic smell", "ozone smell", "putrid smell", "rotting vegetation smell", "salty, wet smell", "smoky smell", "stale, fetid smell", "sulphurous smell", "urine smell",
            ];
            let soundsAndNoises = [
                "bang, slam", "bellow(ing)", "bong", "buzzing", "chanting", "chiming", "chirping", "clanking", "clashing", "clicking", "coughing", "creaking", "drumming",  "footsteps(ahead)", "footsteps(approaching)", "footsteps(behind)", "footsteps(receding)", "footsteps(side)", "giggling(faint)", "gong", "grating", "groaning", "grunting", "hissing", "hooting", "horn/trumpet sounding", "howling", "humming", "jingling", "knocking", "laughter", "moaning", "murmuring", "music", "rattling", "ringing", "roar(ing)", "rustling", "scratching/scrabbling", "scream(ing)", "scuttling", "shuffling", 'slithering', 'snapping', "sneezing", "sobbing", "splashing", "splintering", "squeaking", "squealing", "tapping", "thud", "thumping", "tinkling", "twanging", "whining", "whispering", "whistling",
            ];
            let airQuality = [
                "clear", "foggy", "steamy", "foggy near floor", "steamy near floor", "hazy", "dusty", "misted",
            ];
            let generalFurnishings = [
                "armchair", 'armoire', 'arrows', 'bag', 'barrel', 'bed', 'bench', 'blanket', 'box(large)', 'brazier & charcoal', 'bucket', 'buffet', 'bunks', 'butt(large barrel)', 'cabinet', 'candelabrum', 'carpet(large)', 'cask', 'chandelier', 'charcoal', 'chair', 'chair, padded', 'chair, padded, arm', 'chest, large', 'chest, medium', 'chest of drawers', 'closet(wardrobe)', 'coal', 'couch', 'crate', 'cupboard', 'cushion', 'desk', 'fireplace & wood', 'fireplace with mantle', 'fountain', 'fresco', 'grindstone', 'hamper', 'hogshead', 'idol(large)', 'keg', 'loom', 'mat', 'mattress', 'pail', 'painting', 'pallet', 'pedestal', 'pegs', 'pillow', 'pipe(large cask)', 'quilt', 'rug(small / medium)', 'rushes', 'sack', 'sconce, wall', 'screen', 'sheet', 'shelf', 'shrine', 'sideboard', 'sofa', 'staff, normal', 'stand', 'statue', 'stool, high', 'stool, normal', 'table, large', 'table, long', 'table, low', 'table, round', 'table, small', 'table, trestle', 'tapestry', 'throne', 'trunk', 'tub', 'tun', 'urn', 'wall basin and font (consecrated water container)', 'wood billets', 'workbench',
            ];

            let graffiti = [
                "‘Here Lies Big Benson – Didn’t Bring His Ten Foot Pole And Paid The Price’", "‘For a good time teleport to sequence [SIGIL SEQUENCE]’", "‘Sneek Atak Heer’ with an arrow pointing behind a rock.", "‘Kobold Pride’ in draconic.", "‘Your Mother Is A Succubus’", "‘Here lies Tom – ‘There’s no way that door can be a mimic’.’", "‘Here may be found the last words of Joseph of Aramathia. He who is valiant and pure of spirit may find the holy grail in the Castle of Aaauuuggghhh… ‘", "‘Dwarves Suck’ written 8 feet up a wall.", "‘Don’t bother trying to grave rob. The corpses don’t like visitors. Come to think of it, they don’t like anything living at all’.", "On the ceiling, ‘Beware of Trappers’", "On the floor, ‘Beware of Piercers’", "‘Archmage Drachnar and his Meat-Shields were here’", "On the side of the passage, ‘Only the penitent man shall pass …’", "A map of the dungeon that at first glance seems correct, but either upon closer inspection or actually trying to use it flaws are revealed, secret doors marked where there isn’t one, hallways/staircases connecting the wrong rooms, etc.", "‘I’ll make yer skeleton exit yer meat’, in Orcish.", 
                "‘Do not open.’ on a door (door opens to a small, empty closet). ‘Can you not read?’ on closet wall.", "‘Don’t Dead, Open inside’ written in the same manner as on the show. While there’s probably undead on the other side, the more or less garentees the room hasnt been looted.", "‘You don’t matter! Give up!’ Placed on a pair of small signs outside of the dungeon. Left by a well intentioned, if a bit stupid, bard.", "‘Sorry about your wall!’ Place this one near either some blood from a prior battle or a hole in the wall for added effect.", "‘Screw you!’ placed behind a false door with a booby trap rigged to the door. Maybe a explosive/grenade/fire trap or a rockfall trap.", "‘Sharg’s wife is most beautiful,’ in orcish script, next to a crude picture of a fang-mawed dog.", "A crude drawing of a kobold ‘in congress’ with a dragon. It isn’t clear from the context and art quality whether this is a good or bad thing for the kobold.", "68 tally marks scratched with incredible neatness. The last one looks very fresh and is shorter than the others…", 
                "‘2 to the left, 3 to the right and straight below’ in the language of a subservient race to the main dungeon dwelling race.", "‘[Cheif’s right hand lackeys name] is [impotent/illiterate/part-human/vegetarian/a bookworm/short-sighted/other dire embarrasing trait for one of their species or job] ‘ this is a horrible rumour around the dungeon which (s)he has worked hard to stamp out and is now largely forgotton or at least unspoken. It is also 100% true. Make sure you introduce them by name when the PCs meet them!", "‘Trouble reading this? Try Lothar’s Lights for all your torch and lantern needs. Just a short ride from this dungeon.’", "‘That last bit of graffiti was written by a [setting appropriate expletive]ing liar’. On a successful spot check, evidence of dried blood can be seen on the floor below the graffiti.", "Originally a crude carving of a penis, someone painted over it to turn it into a kitten. If the paint is removed, the original carved design remains.", "‘Block the path RUN’", "‘Take off that hat.’", "‘It sees NO EYES’", 
                "‘You have to burn the rope.’", "‘It hurts.’", "‘OVER THINKING IT’", "‘REDRUM’", "‘NILBOG’", "‘See you next Wednesday.’", "‘There is no such thing as Majestic-12.’", "‘How’s my dungeoneering?’", "‘Welcome to Hell. We accept payment in paper or plastic.’", "‘I must not tell lies.’", "‘Wash your boots, don’t leave any footprints behind.’", "‘I am so grateful to be alive. I am in a world of crap, yes, but I am alive. And I am not afraid.’", "‘She’s lying to you.’", "‘Did I ever tell you the definition of insanity?’", "‘Let me in. I’m scared.’", "In tiny lettering: ‘If you can read this, it’s already too late.’", "‘The Minotaur is not what he seems.’", "‘Secret door here.’", "‘Joreth – I’ve gone back for her. Meet me at the Frog and Jester in Pennyworth Lane.’", "‘Look behind you. Now!’", "‘I am the last of us. Do not think ill of me but I cannot go on alone. Do not choose the black door if you wish to see sunlight again. Good luck.’", "‘Ph’nglui mglw’nafh Cthulhu R’lyeh wgah’nagl fhtagn’", "‘No hope for those who proceed forward’", "‘Watch for the pit trap’", "In scribbled writing: ‘Don’t eat the mushrooms’", "Turn ‘wright’ at the fork’", "In blood: ‘Zed’s dead’", 
                "‘100 gold to anyone who finds my sword – [insert name and location of npc]’", "‘Brother, She’s not here- she is apparently in another dungeon.’", "‘You’re lucky someone already read these Explosive Runes.’", "‘Here lies Gilbert – ‘The mushrooms clearly aren’t poisonous, that rat just ate some and it was fine. Look, I’ll show you.’", "‘The skeletons are not dead’ hastily written halfway down a hallway of skeletons.", "‘The Great Necromage Vilicous and his coterie of foolishly moral companions were here’", "‘Treat the dungeon with courtesy, and it will do the same’", "‘Worm Path – Look both ways before crossing’ chalked on the floor on both sides of a large, circular tunnel intersecting a hall.", "‘Mind the gaps’ written in large letters before an otherwise empty stretch of hallway.", "‘If you are reading this, do NOT look behind you until you exit the room’ scrawled in shaky letters on the back wall of a dead end room.", "‘Please step on me’ carved onto the surface of random rocks and tiles on the dungeon floor. The words are seen multiple times throughout the dungeon’s exploration, and seem to disappear when no one is looking. The words constantly reappear no matter what, but if stepped on, helpful and relevant graffiti is found before the next encounter, puzzle, or junction of pathways.", "‘Grall Stonebringer was here.’", 
                "A picture of a gelatinous cube eating a person.", "A cartoonish picture of a dwarf running away from a rust monster.", "Written in very tiny letters: ‘If you can read this, you can’t see the goblin sneaking up behind you.’", "There is a short and narrow room; the long-rotted remains of a door hang off hinges at the entrance. Scrawled along one wall, in an ancient language the party must translate is ‘[Name of some long-dead king] gobbles donkey goobers’. The opposite wall is also marked, with ‘[Name of long-dead queen] does the nasty.’ If the party succeeds on a perception check they realize they’re standing in a toilet stall.", "A scribbled map of the dungeon, with a big X in one room and directions to a treasure. But it’s a trick; when the party stands at that spot they trigger a trap.", "‘Abandon hope all ye who enter here.’", "‘Artival. Waited 3 days for you. Ran out of supplies. Moving on to the next level (or whatever floor is the one below.’", "‘There’s a safe room in the center. Left food and supplies.’ (an obvious trap)", 
                "‘On this day, Brumr Goldbeard killed ninety-three kobolds.’", "‘Who built this place?’", "‘Vampires don’t care about daylight when live indoors.’", "‘Stick to the center halls. They’re safer.’", "‘Tika isn’t dead. She’s with us.’", "‘WHERE IS THE EXIT’", "‘None are so blind that they cannot see the darkness of this place. Look not upon the face of the weeping one, Tread not on the bones of mad men.’", "‘We are the real monsters.’", "‘This corner secured by the Mighty Woodchucks.’", "‘This was all already written. You are being controlled. They know what you’re doing. We’re all just pawns in their little game. They decide who lives and who dies. None of us are safe. None of us have free will. Don’t let them win.’", "‘Jessedo R.I.P.’", "‘If you find my body, tell Matin I loved him.’", "‘God bless the Zentarim.’", "‘Here rests two good men — Nissus and Camom. Respect their souls.’", "‘Let it be known that I, Luip Salazom, screwed every barmaid in Neverwinter.’", "Drawings of butts, each one from a different race.", "A symbol in thieves cant that means it is safe to rest, with ‘r rouge died so I cant right this in yur theves speak, but go screw yurself with a rusted spyke jerk.’ painted over it.", "‘There is a secret door somewhere on this passageway- I hope you have better luck finding it.’", "Large scrawled lettering that says ‘Droop woz heer’", "Crimson red letters that are still oddly sticky, ‘Don’t ask about the price’", "An oddly phallic image that seems to have been painted on in bold white paint.", "Bloody scrawled writing say ‘The secret chamber has been opened.’",
            ];
            let trap = [
                "A pit trap opens up beneath a character. At the bottom of the bit they are falling into is a button that drops a stone block on top of them, covering the hole and smashing the character.", "A lever with a sign that says “Pull to open” next to a locked door with an extremely poorly hid trap door right under the entrance. Pulling the lever surprisingly opens the door. If you touch the door without pulling the lever, the trap door opens.", "A series of regal-looking interconnected hallways are dimly lit with magical torches suspended in sconces. The entrance that the intruders come through suddenly closes itself off, and the intruders sit in silence for a few seconds. Looking down one of the other hallways reveals a slowly encroaching patch of darkness that snuffs out the torches as it makes its way forward, which relight themselves when intruders approach them while the darkness is not nearby. The intruders must search the various corridors while simultaneously avoiding the patch of darkness, which envelops and leaves no trace of anything that enters it. Any attempts to do combat with the darkness prove ineffectual, as anything that enters vanishes, never to be seen again. The darkness is semi-sentient, and the intruders can interact with it by trying to hide from it or get it to follow them. The key to escaping the hallways lies with the magic torches in the two impressively decorated sconces that the darkness can’t seem to pass by. By removing one of the special torches and carrying it with them, an intruder can hold off the darkness or even push it back. However, confronting it for too long will begin to dim the torch until it eventually snuffs out, forcing the holder to escape the darkness in order for the torch to relight. When the special torches approach the darkness from both sides of a hallway, it condenses and eventually fades, leaving a shadowy door to the outside where the last of it vanished.", 
                "A roughly cut gemstone hovers ominously over a crude alter in a cavernlike room while a malicious spirit floats up around the ceiling and out of sight. New entities entering the room causes the crystal turn to face the intruders, revealing that it is actually an eye of some sort, containing a pupil that darts rapidly between the intruders and the spirit. The spirit immediately begins cajoling the crystal eye into destroying the intruders, talking to it as though it were a child in need of guidance. After a few seconds of apparent listening, the eye completely focuses on the spirit and pillars of rock begin to rapidly erupt from the room’s surfaces at points near the intruders. The pillars, while initially inaccurate, begin homing in on the intruders more and more the longer they stay still, and do 5d10 bludgeoning damage on a hit. The key to escaping the room is the crystal eye in the center of the room, which is being told by the spirit to kill the intruders. By being more persuasive than the spirit, intruders can convince the eye to stop its onslaught and eventually target the spirit instead, which will disperse after being hit multiple times with pillars of rock. The eye is very childlike in its considerations and will lose focus if the intruders fail to convince it or begin to act too impatient. Simplistic approaches work well, and the eye responds positively to constructive encouragement when it targets the intruders (That was some very good aiming, I could feel the wind rush by me! Next time though, try to aim towards the mean spirit instead, OK?). Once the spirit is destroyed, a gentle suggestion that the eye create an exit will convince it to pull a slab of rock away from a wall and reveal a passage to outside the room.", 
                "Walking through an area with “Dormant hives of bees,” there is a queen bee figurine with a stinger shaped like a key in a glass jar at the opening of a room. The jar acts as a seal to keep the pheromones of the queen away from the rest of her hive. Once removed from the jar to unlock a mysterious key hole, the once dormant hives awaken to attack whomsoever holds “their queen.”", "A nearly invisible gelatinous cube encloses an entire section of a hallway/corridor. Requires strong perception check to even see. Will immediately begin digesting any adventurers who walk into it, tinging the clear jelly a slight pink color.", "A hallway with what appear to be dart traps, or falling spike traps, or fire. There are several different hallways in a succession of 3 (so imagine three hallways one after the other with different traps, with a small room between each that could hold 4-6 people. Each hallway starts with 2 statues. The first hallway deactivates the traps by grasping one of the hands and turning it down. Once the next hallway both statues have hands that turn, and one activates the traps just cleared while the other deactivates the ones ahead (but both can’t happen so if the try to deactivate the traps ahead it will still be active). And finally the last hallway will deactivate the traps but the floor is pressure sensitive. Illustrate this by having the party see the hand start to turn back when a member starts to walk across. Essentially the first two hallways punish groups that don’t follow right behind the rogue and send him forward to handle traps, while the last hallway punishes players who just follow right behind the rogue, and are afraid to make any distance.", 
                "A map is found on a skeleton wrapped around an old skeleton key. The map shows traps, but all the information is either half right or all wrong. The key is able to open any door in the dungeon, but attracts any undead within 10 miles. Take a hint, maybe the dead guy with the map and key died for a reason.", "When trying to open a door they have to pass a DC x wisdom saving throw to open it. Otherwise they feel compelled to ‘open’ the next nearest thing. Causing them to attack the closest person for y rounds.", "A secret door that leads into a closet-sized chamber whose walls and door are very thick. Detect magic will reveal a faint aura where the walls meet the ceiling. If any character steps entirely inside and the door is not blocked, the door will shut and meld into the stone of the wall. There is a barrier of inch-thick adamantium within the stone of the walls/floor/ceiling: this must be dealt with in addition to two feet of stone. The character inside the chamber will begin to suffocate after one hour and takes one level of exhaustion after each additional hour.", "Walking down a hallway, the party passes through a large set of wooden reinforced doors. Beyond these doors is another hallway about 50ft long. In this hallway, there are 10 large sets of full steel armor with varying weapons from daggers, long swords, flails, whips, mauls, glaives etc (all of which are very well made). They’re lined up along the walls of the hallway 5 on each side. If any of the armor or weapons are touched. Every single set of armor will come alive equipping the weapons they had, attacking the closest target immediately. The doors will also be slammed shut, slamming into anything in it’s way. The doors will only unlock if the sets of armor have been killed.", 
                "You enter a dungeon with an open pit in the middle of the floor, runes that you can’t decipher are around the hole. As you approach you can hear the cries of a small child, and when you look into the pit you can see a human child covered in dirty rags. You’re able to get the child out, but they say they can’t cross the runes and you’ll have to lift them up and over them. When you do, the child (vampire) tries to feed from you, dealing piercing damage.", "You come to the end of a hallway with three doors, each with a word in Common written on them. The first door has Community, the second door has Feast, and the third door has Companion. If you open the first door a swarm of cranium rats will descend upon you, alerting you to a mindflayers’ presence. If you open the second door three Spawn of Kyuss embrace you. If you open the third door, two Shadow Mastiffs lunge at you.", "A trap that is very kobold related, but could work for other creatures is this… Walking along a cliff either in a mountain/volcano or on it, a party member hits a pressure pad beneath some rubble, or dirt (depends on the environment). A harpoon shoots out and gets the member in the leg. A kobold who was waiting kicks a weight attached to a chain out and it drags the member down the side of the cliff to about 20ft above the next level (assuming they don’t pass a strength check at disadvantage). The ambush comes and there are kobolds on the lower level trying to reach the member while the party is ambushed and distracted. They will have to decide who is saving their friend and who is fighting, while the member is dangling and until he gets himself right side up is at a disadvantage to all attacks. The weight unless removed from the chain is going to disadvantage his climb (and the pain from a hook in his leg will make the climb a bit more difficult too). For ideas on how the chain looks, think of a fishing hook with a weight on it.", 
                "Two animate armors standing across from each other in a small room inviting the characters to play racquetball with a sphere of annihilation which the armor can catch.", "A door that opens into a short hall, behind the door is a poorly hidden log tied to the ceiling, but opening the door didn’t cause it to swing, must be a dud. Touching the door on the other side causes the stone slab that was the floor to slide into the wall, causing the player to fall into a pit of brambles, and the false log trap detaches and falls on top of them. Can be solved by throwing a rock at the door on the other side, the log will fall and create a safe bridge across the brambles.", "A cannon with a spear inside, readilly aimed, capable of changing its target. It has been set to trigger on any new magic being cast (If it was cast before entering its range then it won’t trigger it).", "A pitfall trap drops the poor adventurer into a gelatinous cube. Said block of evil Jelly also has animated swords in it that will blend the adventurer. Alternatively, there’s a normal floor trap, but disabling it drops the cube full of swords onto the adventurer from the ceiling.", "A room with a large spiky chandelier covering pretty much the entire ceiling and nothing on the floor or walls. Once the trap is triggered, gravity inverts in the room, dropping the occupants up into the spike trap chandelier. Afterwards, gravity returns to normal and drops them back down the room into the ground, followed shortly thereafter by the Impaldelier.", "A large square room, a small maze-like pathway in between pressure plates is on the the floor and leads to the other size. If a pressure plate is stepped on, a giant cube slime falls from above filling the whole room. Players must take 1d4 acid damage every turn of the slime until they escape.", "In a narrow hallway, you have a part of the floor that folds down when to much weight is put on and springs back to its normal position once the weight has been dropped. This obviously leads to a pit, but in the pit is nothing. It simply drops you 50ft leaving you in like a 20ft square room that’s 50ft high.", "A long, narrow corridor that slants downward slightly. A large reservoir of quicksilver lies to your south. Outrun the stream to avoid getting impaled.",
                "A stairway that has a closing metal door at the top and bottom. The top door is a false door and behind it lies a natural flow of lava. When the top 3 stairs detect any pressure, the top door has panels that open and let in the lava. The bottom door is locked, and panels in the floor at the bottom of the stairs open only after the entire hallway has filled with lava and the top door panels close again.", "A well with a rope or chain that hangs to the bottom. There is a grate about 100′ down that goes nowhere. The walls of the well have small holes all along its length, possibly from climbing pitons. Once a certain amount of weight is applied to the rope (equivalent to two or three party members) a gelatinous cube is poured from its cell behind the stones in the wall, and seeps through the walls into the well above the players. The gelatinous cube paralyzes creatures when they touch it and fail a save. The cube happily slides down the well and consumes its prey until all organic material is digested, then it seeps through the grate at the bottom and it collected and replaced in its cell behind the stonework.", "A treasure chest in a 10′ square pit. The entire pit is clean and smooth stone, making it difficult to climb. If weight is added to the floor of the pit (set to the weight of one or more humanoid adventurers) the pit and 1 foot of the pit walls is shot upward to the ceiling cutting off all means of escape. The walls then close in and collapse all humanoids unless they pile on top of the chest, which is not crushed. The treasure chest is a mimic but is magically paralyzed until the walls fully collapse inward, at which point he mimic is released from its spell and the trap resets in 1d4 days.", "A shield guardian with a stored spell of invisibility blocks a hallway or doorway and goes invisible before adventurers can see it. The Guardian body blocks the path and ambushes the first adventurer to bump into it.", "A pitfall into a pond of ooze. As the adventures move around the pond seems to start moving of it’s own accord and slowly drags anything on it’s surface into it’s depths.", 
                "A pitfall into with a pool of flammable oil. The victims can climb out of the pool into a long corridor leading back to where they where. Along the way are magical swinging candles, mini flamethrowers, and minor fire elementals.", "A seemingly normal abandoned bathroom. There is a tripwire coming out of one of the stalls, that tightly seals the only door. Then, contaminated water starts coming out of the toilets. The adventurers must break the door to escape, and if they touch the water, they get sick.", "A bedroom with enough beds for the party to sleep on. There are pressure plates under the mattresses, that open small holes in the walls. Slowly but surely, a neurotoxin starts coming out of the holes, and seamlessly fills the room, while the adventurers sleep.", "A rickety wooden bridge over a big dark pit, with snakes on the bottom. There is a hole on one of the side walls (requiring a passive perception check to notice). The bridge itself is relatively safe, but there is a thin tripwire halfway through it, that activates the hole, making it spill out a line of fire over the end of the bridge.", "A wall with three stone doors. There is a paper on it, saying that two of the doors lead to a treasure, while another kills whoever is passing through. Going through those doors is not necessary for the adventure. If a player decides to try their luck, roll a d6 to see what happens.", "A treasure room, filled with open and empty chests. There is only one closed container. If the adventurers loot it, the trap is deactivated. If they try to leave without touching it, a loud sound is heard, waking up all of the mimics.", "The adventurers must go through a door. There is a paper on it, with the words: “Be polite”, and a happy face. The door leads to an abandoned workshop, filled with statues and gargoyles. They have to shake the hands of every gargoyle before leaving the room, otherwise they will attack the party.", 
                "This is a standard pit-trap with a twist. At the bottom of the pit, and for ten feet up the walls, everything is coated in pitch. Pitch may be sticky, but in quantity it also acts like any other oil-based liquid – a lubricant. Climbing up a rope becomes extremely unlikely for whoever fell down the hole. But that’s not the worst bit. A couple of rounds after the pit trap is activated, the Kobolds, warned by a bell attached to the pit trap’s trigger, will show up with lit torches. And one of them will start combat by throwing a torch into the pit – igniting the pitch!", "Oil floats on water: You all know the scene. In the middle of the vast dungeon is a lake. At one edge of the lake is a boat. The heroes have to pile into the boat and row across the lake to the next section of the dungeon. Well, this particular lake is guarded by kobolds with spyglasses. And a few barrels full of lamp oil. And a torch. Be sure to wait until the party is most of the way across the lake before the kobolds start pouring lamp oil on the water.", "Kobolds are light, and armor is heavy: A well prepared Kobold always has an escape route. And his escape route is generally one only a Kobold can use. While most Kobolds choose to make tight passages that only a Tiny creature can squeeze into (thanks to their ability to fit into unlikely places), some rely on the fact that their pursuers are generally heavier, and in larger numbers, than themselves. Choose a corridor, and undermine it (dig a tunnel under the floor, but with too little material acting as floor/ceiling). Leave it just enough strength to handle the weight of a Kobold or two. Fill the corridor below with something nasty, and have it lead somewhere nasty. As a finishing touch, make sure there’s a collapsing ceiling in the upper tunnel as well to ensure that the heroes can’t climb back out after you.", 
                "Gold melts at a surprisingly low temperature: Did you know that you can melt gold in a candle flame? It would probably take about an hour to do so from room temperature, but you can. More importantly, if you keep your gold coins at a hot enough temperature, they’ll melt very quickly if exposed to a very potent heat source – like say they might melt within seconds if they were doused in lamp oil and lit. This is an interesting thing to note if your chosen method of storing gold coins is in a wire-mesh cage attached to the ceiling. Especially if such a cage is kept at very high temperature, and is trapped with various kinds of flame traps (flame traps that trigger onto the gold). Unfortunately, while the temperature might be relatively high compared to the meltin point of most metal, it’s still more than enough to cook any flesh it comes in contact with (and STICK to that flesh, as molten metal tends to, causing the WORST sort of burns). And of course, the easiest way to get at the gold itself is from directly below it. Be sure to note to the party how hot it is in the room with the gold while they’re standing under it. If they’re clever enough to figure out the trap beforehand, hopefully they’re also clever enough to notice the hidden drains in the floor before all that molten gold runs (very, very quickly) down those drains.", "At the end of a hallway is a fake door. When the doorknob is turned, a latch is released, and the spring mounted door flies out at whoever opened the door. Since the door takes up most of the hallway, there is no chance to dodge it at all. The person who attempted to open the door takes 2d6 points of damage, and anyone standing within 5 feet of the door will take 1d6 points of damage.", "Anyone weighing more than 150 lbs. will cause a lid to a pit to open. The pit is 25 feet deep.", 
                "The character steps into the trap and the gem eyes from a roomful of statues shoots rays at him. The PC is zapped and appears to be disintegrated. A skeleton appears in his place. It’s important that the PC’s don’t get a chance to detect this trap or they’ll quickly find a solution (Search DC30). The character is teleported to a sealed tomb filled with the skeletons of various victims. A black pudding, CR equal to the party, attempts to engulf the teleported PC and turn him into a skeleton with its acid. When the trap goes off, one of these skeletons is instantly teleported to where the PC was standing, making it appear like he was disintegrated. Make a Search DC 25 to notice the skeleton (pile of bones) is not the same makeup as the PC (DC 20 if the size category of the PC is one larger or smaller than medium). After six teleportations, the “living” victims (or their remains) are teleported back to the trap area. Defeat the trap by moving statues into the area so they can be teleported, eventually sending out “victims.”", "A room of freezing ice orbs that stick to the skin and slow the characters down significantly. Add monsters/other challenges to taste.", "A long passage of murky, depthless water. Two boats are tied up at the entrance- one that looks rickety and has a little water in the bottom, and one that is new looking, gilded on the edges and looks really watertight. Turns out the “new” boat is actually an illusion, and it disappears in a puff of smoke about halfway through.", "A long maze of gooey yellow sponge passages just large enough for one person to crawl through. The maze starts to shrink and harden if players take too long to get through.", "A long hallway of absolute darkness. If the adventurers try to bring light to it the darkness itself lashes out at the party.", 
                "They enter a room, and there are five doors. They are labeled 1, 2, 4, 5, 6. There is no door #3.", "A long, dimly-lit hallway. Candles light the way, and occasionally there are wisps of wind. Occasionally have a player step on a block that depresses a little, and tell them a puff of air just shot out of the block on the wall to their immediate left or right.", "A seemingly wooden door that says “Knock”. Knock on the door to enter. ALTERNATIVELY: a seemingly wooden door, badly worn; it seems as if it could just be destroyed. Players can see the other side, in fact. Catch? Nobody but the weakest among any group that approaches it, can open it. It cannot be destroyed by anything.", "A badly written sign in [the language of whatever people made the dungeon] that says “beware”; the area is somewhat stinky. It leads to a small hallway with another likewise-made/written sign that says “turn back”. It’s getting smellier now, and much more damp. If the party continues, they find themselves at the bottom of the underground craphouse. Bonus: if they made it this far, and if they get clever and can’t smell anything and want to risk being a social pariah for the next several days, they can climb the spout to the room(s) connected, above.", "Magic runes that activate when a character steps into and area, casting floor of ice. To move characters must roll dexterity or fall probe and take damage.", 
                "While travelling along a path towards a popular location or city, the PCs hear a voice so soothing and enchanting that they are compelled to move towards it. On failing a DC 15 Wisdom check, they walk towards the voice which leads to a hag nest. The voice emanates from one of the hags. On a successful check, PCs can still hear the voice but are able to clear their minds long enough to break free from the hold of the song. Lots of footprints are seen going in that direction.", "A flameskull is slightly buried underneath some dirt. The soil around it has been disturbed. As a player (or two) steps closer, they fall through the soil into the gelatinous cube below, and the flameskull rises striaight into the air.", "While travelling to a popular location or city on a path that is obscured (such as forest or cave), the party hears cries of help from a woman. These cries emanate from a hidden kenku group that ambush the party when they approach the voice.", "A stone bridge over a section of an otherwise normal river, the “water” under which is actually a grouping of gelatinous cubes in wait to surround any passers, running water hiding their already transparent bodies.", "A literal CATapult, triggered by a wire. If activated, a Cat is flung at the PC who triggered the trap. This cat will get an attack of opportunity with its claws while being flung, and will enter combat with the party afterwards.", "A ceiling trapdoor opens letting out a swarm of poisonous snakes as well as a giant poisonous snake.", "Three chests sit in a room. A sign on the wall reads “DANGER! MIMIC!” There is no mimic, but there is a rug of smothering under each chest.", "An animated armor using a flying sword. After the armor is defeated, the sword begins to fight.",
            ];
            let encounter = [
                "Under a loose bit of cobblestone on the ground, you see what appears to be a small tunnel. If you reach inside or stick around too long, a living crawling hand jumps out of the hole and attacks. This living hand has been hoarding rings and jewelry in this tunnel.", "The group finds a long forgotten coin hoard. All is not as it seems, some of the coins are tiny-sized mimics (maybe individuals, maybe swarms), that adhere to and attack those that try to gather the treasure.", "A crumbling wall with a small tunnel bore through its base hides the resting room for a peaceful Goblin who knows the dungeon well and will give directions or hints in trade for an interesting item.", "A series of really, staggeringly obvious traps. There’s a tripwire that’s made of thick hemp rope, a wooden pressure plate set in the middle of a cobblestone path, a dark path with a torch set right at the beginning (the torch is crudely attached to a lever on the wall).", "The ceiling is completely covered with horrid insects – dark, silent and unseen except for the occasional masonry dust they knock loose.", "Around a corner, you hear clucking. There’s a chicken in the dungeon? You’re three levels down. Shrug: maybe it’s just random. But every three rooms or so, there’s another one, just a chicken walking around and pecking at the dirt. Then you get to a region where there aren’t any chickens. That’s when stuff gets real. Because the chickens are a food source.", 
                "A dead end – The tunnel the party is walking down has them run headlong into a Giant!! Well, the upper torso of the giant. He’s not hostile and is pinned in place by the surrounding walls as he was chasing dinner down a hole and has wiggled himself into this tunnel, blocking any forward movement. If the party attacks him, he will yell and cry, ‘Stop it, please!’ and be overly pathetic, but with his arms pinned at his sides, they will likely kill him in time (suggest higher hit points than normal so the party has to take their time). If they chat with him, he knows a bit about the surrounding rooms as he’s seen creatures moving through the halls and possibly former adventurers. His name is Gordum, and he’s really hungry as he hasn’t eaten in a very long time. Normally, adventurers take pity on him and feed him while they make their way through the dungeon, but the real reason he stays stuck here is a ring of sustenance that he found years ago and pull on ’cause it was shiny.’ If he’s friendly, he offers to watch over the party while they sleep and promises to warn them if anyone else comes down the hallway.", 
                "A rune trap curses you so that you can’t refuse a request. (Requires the word please to count as a request).", "A dragon’s cave? – This room is 60 feet (18 Meters) across, and nearly as high, with small pools of water that collect in natural erosions to the west side where an underground stream has formed a small waterfall. The water is chilled and safe, even if it tastes earthy and heavy with minerals. As the group moves into the cave, they likely notice coins littering the edges of the room in small piles and an outcropping halfway up on the east wall… with a snoring, smoking dragon’s head. If the party is quiet, they can sneak through, but any attacks or loud noise wake and do not harm the dragon. It lets out a massive burst of fire over the heads of the group and yells curses as it waves around. Once it finishes, it demands tribute from the group or it will eat them!! In reality, the head and neck are a permanent illusion that was placed in the area to scare off adventurers by a mage who was practicing some new defenses for his study, and a fairy dragon has worked out how to control the illusion and get it to move when he wants. He uses magic to project his voice and sound like a great dragon, and can use a rune placed as part of the illusion to fire a cone of fire 3 times a day that does damage as an ancient dragon. The Fairy Dragon living in a small opening that’s only accessible at the top of the dome ceiling with a meter (2.5 foot) opening that one would need to fly to or us other means. Any tribute that’s left is floated to his home when the adventurers move on and kept there, or discarded around the ground to add to his greatness. (If characters can get to his cave, he should have 2-3 magical items of some note). The little guy has really done well duping people over the years.", 
                "A dire warning – Moving through this hall, the characters torchlight will cast light through a red ruby the size of an eye that’s been carved to catch and cast the light around the room. If there’s no light, the ruby isn’t found. The light through the ruby displaces words in 5-6 directions saying ‘The Stone of Anolox.’ A group also notices a warning on the wall, one painted with blood and another carved with what must be someone’s finger nails saying – ‘Do not, by any means, touch that gem!’ Anyone who picks up the gem, well, except Anolox, is immediately disintegrated and their ash fills the tunnel.", "A door painted onto a wall with two door knobs sticking out, one labeled ‘fame’ the other ‘fortune’. Touching fame will turn you as blue as a smurf, only reversible by a wish. Fortune will cause 10,000 cp to fall from the ceiling at great speed causing heavy damage.", "Bad Directions – A series of alcoves with a skeleton set to perch in each of them. Each is placed alternating up the hallway at 20 ft (6.5 Meter) segments. The first points down the hallway, the next at the floor, and the next straight up, and so on. Every time the party moves past the skeletons, they point a different direction, and it changes every time.", "Morbid Statuary – A massive room filled with people frozen in time, and in stone. Like creepy stalagmites, hundreds of humanoid statues point up from the ground. One looks like a prince leaning in to kiss a sleeping princess, another is a goblin throwing its hands in the air in panic, and another a cautious knight stalking in his armor. The place looks like a repository for the victims of a gorgon, hopefully long gone.", 
                "Help us Heroes! – The group comes across an small village that spreads out in a crevace in the wall and stretches for hundreds of feet, but where the ceiling is never more than 4 feet high. This is a village of Myconids that have lived here peacefully ‘since the time of our first spores’ and numbers in the thousands. They beg the party to help them as there is a murdered in the midst. Every day, more and more of their people go missing, and they can’t find the culprit. If they are helped, they will give the party pearls that they collect from nearby shellfish and have saved for years. (The murderer is a kobold with a ring of invisibility and a strange mask to keep from falling to the creatures spores. He REALLY loves cooked mushrooms and has been harvesting the myconids for dinner since finding the village).", "Welcome Matt – The group comes to a door rigged with a number of traps. A line at the top that pulls something above the door if it’s opened, a pressure plate that’s released from the bottom if the door is opened, poison darts that fire from the wall behind it, the works! All the traps are fairly easy to spot and disarm, and there are 6 total. An exceeding high perception check is needed to hear that there’s a small click after each trap is set off or disarmed. Once all six have been triggered, the real trap occurs. The walls 30 feet to either side of the door slam into the ceiling (these are 10ft cubes). At the same time, the floor drops out under the door at a steep angle to a smooth shoot, and the walls start moving in. While it looked like there was something behind the door, it leads no where but a series of mirrors that look like a nearly endless hallway, and with the walls closing in, the only way is down. Those characters that do slide down are eventually deposited into a large cage where a robed figure covered in bandages whips around and screams, ‘Happy Birthday Matt!’ He’s then disappointed that you and yours are not Matt. After muttering to himself for a while, he eventually apologizes for the ‘trap’ and releases the group, showing them to a set of stairs that head back to the tunnel. They don’t run into this encounter again.",
                "Poor soul- you find a skeleton chained to the wall. When you approach, you realize it is an undead. He is scared when you approach and explains that he was trapped here and was brought back from death to continue his torment. Who put him there is up to the dm. Also whether or not he is lying is up to you.", "The room nullifies any sounds made, players must communicate entirely through gestures OOC.", "The door opens up into a mirror dimension flipped horizontally, any and all actions taken are performed by the doubles on the other side, including stepping through the doorway. If a PC attempts to talk they are interrupted by themselves.", "The party walks down a hallway which and comes across an opening on one side leading into a large open room. Stepping on a trap in the middle of the open room causes the door to shut and the ceiling to begin to collapse – but only as long as one member of the party is still in the first hallway. That party member can disarm the trap, opening the door and raising the ceiling by finding a recess on the wall in the hallway with a switch in it. If they fail a roll on the first attempt they only manage to stick their hand through a hole into the room and have to search for a second recess.", "A large pit, filled at the bottom with spikes and scorpions. A sign is just visible on one side of the pit. A successful perception check, or a party member being dangled by their feet, can detect that the sign is upside down and says ‘LEARN THE WORDS’.", "The skeletal remains of a man can also bee seen at the bottom of the pit, still wearing black pants, suspenders, a shirt with horizontal black and white stripes, white gloves, and with a black beret perched atop its bleached skull.",
                "A gnome sorcerer with short term memory has been trying to find this dungeons hoard for the last 10 years, but keeps forgetting which way he came from.", "A large banquet hall, with pewter utensils, earthenware plates, and fine food. The walls are draped in common but warm furs, and the table is lit with some nice candelabras (2gp each). There are 2x(Party Size) seats at the table, and at the head is a stout, ruddy faced bearded earl who warmly beckons to the party. ‘Welcome,’ he he says, voice booming, ‘our other guests are almost here. Please, sit down.’ Seat the most interesting mix of NPCs, Villains, and historical figures at the table. The banquet quests are compelled to not make any hostile action in the room. The non-party guests are returned to whatever place and time they were in before the meal.", "A merchant adventurer (CR party level+1, true neutral alignment) has set up a table, chairs, and all manner of interesting equipment to sell to whomever happens to wander by.", "A wandering mycologist is looking for the weirdest mushrooms that you can find for their latest thesis/monograph. Not only will he pay (not much) for any mushrooms you can help him find, but you’ll get a mention in his paper! Think of the exposure! All the biggest mycologists in the region will be talking about this.", "In a this room, there is a dividing wall with a doorway. On this dividing wall are a series of colorful masks. Around the dividing wall appears to be a large wooden table with 10 chairs, 8 of them already filled with large creatures (a mix of monsters and/or adventurers in any combination) playing Texas hold’em poker for coin and valuables. No one is talking. Any players at the table who notice you will stop, stare, and point silently to the masks. Any two party members who wear the masks can join the game.", 
                "The party walks in on a group of hostile hobgoblins in the middle of them practicing their synchronized dance routine. After one round of surprised embarrassment, they will attack unless the players either start playing music or challenge them to a dance off.", "This room contains a hole with a wooden bucket on a string suspended over a large, clear pool of water. The bucket hangs down through a circular hole in the ceiling, leading up to a well. As the player’s approach, a coin falls down the hole, and a distant voice calls: ‘Magical well, I seek thy wisdom!’.", "This room is round, with a concave floor. Three large, metal spinning tops whirl magically around and around, bashing into each other seemingly at random. On a balcony wrapping around the room are three goblin shamans, engaging in their favorite pastime, BattleTop. Each controls the tops with a small, delicate handheld contraption. The tops will cease spinning if the contraption is broken, or if they leave the room for more than 1d4 days.", "This area of the dungeon appears to be under construction. Goblin work crews and ogre haulers are lead by hobgoblin foremen, building out new rooms and defenses according to blueprints lying unprotected on a table off to the side momentarily forgotten.", 
                "Three nothics sit, pouring over old tomes and scrolls, lit by blue crystals scattered on a pedestal. On the wall, a giant, engraved flaming eye is engraved. Staring at the carving of the eye for any significant length of time (DM’s discretion, but at least a few minutes) grants advantage on wisdom checks until the player’s next long rest. The player feels compelled to be unable to rest for the next two days, and is exhausted on the third day.", "Carved on the wall in code are the letters…H-A-S-T-U-R. If deciphered and spoken aloud, then whosoever speaks the name of this horrid Elder God, HIM WHO IS NOT TO BE NAMED must make a saving throw against magic or a Byhakhee will be gated in and attack (or the PC may go insane?).", "You walk into the next chamber and find a stone statue of a man reaching for a gold ring on a pedestal. The ring, when worn for at least 1 day, gives you +1 to all saving throws for each day it has been worn for up to a week, but if you take it off you suffer the inverse of that bonus for as long as you had it on. You can’t sell the ring. Putting the ring on the man’s finger will restore him from stone, at which point he reveals this ring was the result of a transmutation spell going horribly wrong. He gives you a level appropriate large sum of gold for releasing him and goes off on his merry way.", 
                "The ceiling of the dungeon tunnel has partially collapsed down, making it very difficult to get past. Characters would have to strip off any medium or heavier armor and backpacks to crawl past it. Investigating it more reveals some furniture at the top of the rubble near the ceiling, indicating a room above, but investigating it will probably complete the collapse and prevent further exploration down the tunnel.", "A several story deep library attended to by a seemingly human librarian that doesn’t know his library is deep in an underground dungeon. The stacks are littered with skeletons of all shapes and sizes but it doesn’t seem to bother the attendant. Now that you mention it, it has been a few years since he’s had anyone visit. That is, of course, anyone besides the necromancer that comes by every so often. – defeating the necromancer and his skeletons allows you access to the library. It contains a bunch of spell books for the wizards in your party, some defensive magical items, a moderate stash of gold, and a heap of baubles and nearly insignificant magical items.", "An undead, but coherrent, merchant runs a small item shop in the depths of the dungeon. The shopkeep is a little mad, but seems content to run a shop with average or slightly below average prices on basic goods (maybe a few rarities at DM’s discretion.) The Merchant seems disinterested in the world beyond the room their shop is located in, and if pressed seems to think they’re getting new supplies in once a week. Will react accordingly if the PCs attempt to cheat or steal from them.", "An archway has been heavily barricaded and the area around it has sign postings in the language of the dungeon’s inhabitants with stern warning to stay away. Skittering can be heard from within. Inside is a wing of the dungeon containing a burrow having broken through the wall and an infestation of subterranean creatures of the DM’s choice. (Possibly of a high CR to make this optional wing and its loot a real challenge to the PCs)",
                "A patch of wall indiscernible from the rest of the dungeon except for the incredibly soft quality of the stone. A small alcove containing a slightly inhuman skeleton is on the other side.", "A room that has no gravity.", "A crack in the floor that constantly streams out a thin wisp of smoke. It smells of honey.", "A docile monster that is permanently invisible.", "A room with a large central pool in which an elemental lives, protecting a powerful artifact.", "The ghost of an adventurer that became lost in the dungeon years ago.", "Foolish forebears- Ghosts of an adventuring party that died there long ago. They re-enact the the moments leading up to their deaths with no notice of the players. They can help lead them through the dungeon, and even offer information the players don’t know. Eventually though they will lead the party into a trap or deadly encounter", "Nuka skeletons- A room with the charred skeletons of dead adventurers. The walls are burnt black with the only thing juxtaposing it being the perfect white silhouettes of their final moments. When the player’s backs are turned the silhouettes move, and begin attacking the players. The skeletons get up, and their burnt black bones come alive with fiery cracks not dissimilar to embers left in the bottom of a bonfire.", "Murder mystery spectacular-A doorway that leads into a well set dining room has an instant kill trap thst extracts people’s souls from their bodies. They now have to act as ghosts in a murder mystery dinner party, and can get back in their bodies once they have helped solve the mystery. They are unable to communicate with anyone directly, but they can ‘haunt’ things to send messages.", 
                "Arachnid ally-A spider living in an old shoe offers information to adventurers for a modest fee. She can offer shortcuts, intel, and hidden passages", "Pilfering party-Another adventuring party has been stealthily following the party, and plan to jump them in the treasure room.", "No blinking!- As soon as the players step into this room the door locks behind them. The room is mostly normal with the exception that one wall has the words ‘no blinking!’ Written out in huge letters. If the players blink they see where the key is hidden, but only for a split second.", "A room filled with artifacts such as gems, ancient pots, weapons. Some are on pedestals but most are scattered on the floor as if someone has ransacked it but left everything inside. A small, golden statue of a dragon lies smashed by an empty pedestal, and at the end is a locked door with no keyhole. A large mirror leans against the wall on the left of the path. Reflected in it is the room, but with everything carefully arranged and the dragon statue unbroken on the pedestal. If the players attempt to steal anything, the pathway they came through liquidates and melts, across, trapping anyone inside the room and crushing anyone in the hall, until it is placed back where it was found. If the room is arranged like in the mirror, including mending the dragon statue, the door at the end slides open.", "A hole in the wall, about the height of human shoulders. There is something shiny on the deep end of the hole, however to reach that, you would have to reach inside, and it’s deep enough to swallow your arm up he shoulder. If you reach inside, something bites you, causing 1d4 piercing damage. If you reach inside again, nothing bites you and you are free to take the shiny thing. It’s a single goldpiece.", 
                "An old gnome is sat on a barrel smoking a pipe in a corridor of the dungeon, where the path splits into two. He gives the players a pleasant smile, and starts chatting about the draught. If they ask about how he came to be there at gives a vague answer about knocking the area well and directs them down left corridor, promising it’s worth their while. If they do they find a backpack filled with old treasure worth 30gp and the skeleton of a gnome lying beside it. If they go back, the old gnome is gone without a trace.", "A large disk floats rotating, a few inches from the circular walls of the room. Through the cracks you can see a deep chasm. At even spaces around the walls there are open and empty tombs, each with a seal floating above it. If the players all venture into the disk it will activate and spin violently, using its centrifugal force to push the players into the tombs or the entrance or exit.", "The ghost of the now crumbling manor is not pleased that some adventures are taking his stuff, but instead of attacking, he tries to find some middle ground with the group so he can be left in peace.", "In front of the party is a large stone door, possibly of gnomish construction that is covered in thin grooves that seem to make out a labyrinthine maze. In the middle is large ruby red gem that, when touched, shrinks the party and puts them somewhere random inside of it. In order to re-enlarge themselves and exit the labyrinth (thus opening the door) they must find their way back to the gem that now looms menacingly overhead while dodging mechanical spiders and tiny traps.", "A tiny telepathic spider offers to show them to a secret shortcut to the end of the dungeon. When followed a phase spider ambushes the party and thanks its child for bringing home dinner", 
                "A room with magical darkness cast upon it hides important clues, but the only thing that can dispel the darkness is a living chandelier over the player’s heads. The only problem is that the chandelier can feel pain and doesn’t want to be lit on fire. The party can try to convince the chandelier to let them light it or light it forcefully. If the latter then it screams bloody murder attracting any nearby enemies.", "In a completely filled treasure room a single sentient gold coin waits to liberate it’s brothers and sisters. As soon as the player’s backs are turned the gold coin begins animating 2d20 gold pieces a turn and they all make a break for it.", "In a large empty circular room in the middle of a tower is a flower surrounded by a ring of fur. If the flower is pulled the room shifts downward a few feet if the fur is ripped out it goes up a few feet. As soon as one is taken. It regrows as fast as it was pulled until it reaches the top or bottom level.", "At a junction of hallways, the players notice one hallway has a slight breeze accompanied by a slow, rhythmic wheezing. The air is slightly warm and has an acrid smell. If they seek out the source, it leads to an abandoned forge with an enormous billows. An enchantment keeps the forge warm, like a magical pilot light. The late forgemaster’s bones sit hunched at a workbench with various mechanical drawings. There are various trinkets around the room, some magical, some mundane. If the players take any of the items, they are attacked by a previously dormant construct that was sitting under a cloth in the corner of the room.", 
                "The players begin to smell a faint scent of baking bread. Is it delirium, or does someone live down here? Bonus! The smell of baking bread is soon joined by the smell of roasting meat. If the players seek out the source of the smell, they find a crack in the wall that leads to an ancient banquet hall, inexplicably laid out with a feast.", "The party finds a door, barred and barricaded. If cleared, the door appears to have been hastily welded shut by pouring molten metal around the edges, and requires a strength check to open. (or some industrious chiseling) When opened, the doorway opens into a void, scattered with stars. The party may step through, and they walk on an invisible surface even with the floor of the dungeon. Who knows what could be found in this strange realm?", "A room lined with standing alcoves. The alcoves are inhabited by a body encased in (magical) crystal. A knowledge history check can date the bodies to various eras of history. Near a collection of empty alcoves is a body bearing an item of only recent styling, invention, or popularity.", "A barren room with a standing mirror at one end. The mirror is cracked, it appears someone took an axe or sword to it some time ago, but the magical runes around it’s edge still flicker faintly with power.", "A room that appears to be a shrine of some kind. It contains a 10 ft wide, 3 ft deep circular pool in it’s center. In the pool, there is a duck. The duck resists all attempts to discern it’s nature, for all intents and purposes, it appears as an ordinary duck. The duck is docile and is content to do regular duck things. If, at any point, a member of the party says ‘I wish…’ within 5 feet of the duck, it quacks, grants the wish, and disappears in a suitably appropriate and silly display.", 
                "The dungeon is very cramped, smaller than usual hallways, doors just tall enough to fit through, etc. At the bottom of the dungeon is a large, cavernous chamber containing an enormous monster. Upon inspection, the chamber appears to be a sort of colosseum. The monster may be dead, undead, or alive, and may be immediately aggressive, or just want a friend. It has no understanding of how it got there.", "You come across an adventurer/adventurer party that has been magically bounded to a room so they can’t leave the area.", "There seems to be a weird hole in the wall that is pitch black. It doesn’t seem to have good magic or evil magic, in matter of fact, there is no magic coming from it. If an object is thrown into it, it shoots straight back dealing 1 damage. If a PC tries to get close, it automatically seals and reopens when no one is within 5 feet.", "When you enter the dungeon, after clearing the first few rooms of traps, you realize that the homeless had already cleared out the area and is now using it as a place to live and sleep in, they say it’s better than sleeping in the streets.", "The room is raining?", "You come across a nice looking devil statue in the middle of a room, after a DC 20 (Investigation) check, it turns out there is a button in its mouth, when pressed, the mouth closes shut dealing 2d4 piercing damage and you can see blood dissolving as it leaves your skin. After 10 seconds it reopens and the statue turns into an imp, this imp now serves under the PC that put their hand in the mouth.", "A reverse pit trap; a reverse gravity rune with the pit above instead of below.", 
                "The hallway the party is currently in starts to fill with water at about a knee deep height. Waves begin to form on the opposite end of the hall and rush towards the party. Each character in the water must make a DC 13 Dex saving throw or be knocked prone and pushed back 10 feet.", "A dwarven fighter, The last survivor of her party, is trying desperately to dig her way out of the dungeon with her war pick. Unfortunately, just as you reach her she breaches the dungeon’s sewers and unleashes a giant crocodile and a swarm of rats.", "An enemy Hobgoblin wizard the party is fighting casts shatter and collapses one of the nearby crumbling dungeon walls, revealing the basement of a very confused and panicked Halfling couple.", "Pipes high up on the walls in this chamber are dripping some kind of emerald-green liquid into a wall-mounted fountain. The fountain is nearly full. A successful miscellaneous intelligence check tells you that it’s just liquid paint. Highly toxic paint, but just paint. The fountain drains into an adjacent room, which is completely knee-deep in the liquid.", "The room contains a number of flensed livestock hanging on hooks, as if you’ve entered a butchery. Alongside creatures appropriate for the area, there are some animals from far away, such as penguins if in a dungeon surrounded by desert. If the party waits long enough, something invisible takes one animal corpse off the hooks and drags it into an adjacent room, where it begins butchering it.", "You come across a group of kobold engineers repairing some traps that jammed or are otherwise damaged.",
                "This room contains an 8ftx12ft pool of opaque white liquid, framed by four columns with taut chains leading up to a recess directly above the pool. If any creature is fully submerged into the pool (which is 10ft deep), a large metal mold begins descending from the ceiling recess. It will stop shortly before contacting the liquid if whatever creature entered the pool didn’t get out in time, but will plunge fully into the pool when everything leaves. When the mold returns out of the pool in four(?) minutes, a solid white mannequin in the shape of the submerged creature is atop it. The mannequin animates when there are no witnesses directly observing it, and will stalk the creature it’s modeled after. Perhaps the dungeon denizens are aware of the room’s properties, and have managed to take control of the mannequins to make reinforcements.", "A bright lamp hanging on the wall in an otherwise dim hallway, next to a wooden door with thick hinges. The door is locked, but it has a small counter at about elbow height, and a panel above that will open up if anyone tries to open the door or knocks on it. A flickering, jittering undead asks ‘I’m afraid the library is currently closed to visitors, but may I help you find a book?’ It will bring one book of choice for each person within the next few minutes who asks for one, but will not give multiple books to the same person. Books can be requested by very specific parameters (author, edition, hardcover or softcover, title), or by saying something as vague as ‘I’d like a book on cows’, though vagueness is probably less rewarding. The books are deposited on the door counter. Once every person it sees has received a book, or after a few minutes, the undead, door, and lamp vanish, leaving behind an ordinary patch of wall.", 
                "A broken down wall of the dungeon leads to a decently sized cave where five cow like animals with purple spots and luminescent horns are grinding their teeth against the stone walls to get the lichen growing inside this crumbling tunnel. If approached slowly they will ignore the PCs, but if the PCs get too close the biggest one will turn towards you and snort while the others run back into the tunnels. If the PCs continue to approach it will attempt to gore one of the PCs with its poisonous horns and will then gallop after its compatriots.", "A ghost and a corpse. The ghost is desperately trying to get back into its body so it can rescue its beloved, only it doesn’t realize that hundreds of years have passed and its beloved has likely died, if only from old age.", "A sentient chest, not a mimic and not enchanted. Somehow, in some way, the chest has become self aware. It cannot speak or see or hear or taste or feel, but it can ‘sense’ its surroundings somehow. With great effort it can open and close its lid, and with even greater effort it can move slightly across the floor. How the party learns to communicate with it is up to them.", "There is a helmet in the corner of this room/chamber. In the next room, there is an identical helmet. This continues for every single room afterwards. Any rooms visited before the first time the party noticed these helmets also have an identical helmet. If someone dons the helmet, they see all of the rooms of the dungeon at once, taking 2d12 psychic damage with a WIS save to halve the damage. This psychic damage occurs every time someone dons the helmet, but if they stick through with it rather than removing it, it can be used to get a brief glimpse of whatever an identical helmet would see in another room once every ten turns by passing a perception check. While someone wears a helmet, the other helmets seemingly vanish. Any damage or modifications inflicted to one helmet is performed on all the others.", 
                "The party comes across a glittering egg about the size of an adult halfling in kaleidoscopic colors. If they break it open, there are… more eggs inside, about the size of a normal chicken egg but made of the same material and in the same colors. Each of these can be cooked like an egg, or the party could wait for one to hatch by keeping it heated; a nature check tells you these are basilisk eggs, but luckily newly hatched basilisks don’t have their petrification abilities. A nature check, even if successful, fails to explain why the eggs were inside a larger egg.", "There is a pile of gold coins, about 4500gp total. Whenever the DM so chooses (but within a day), they sublimate into thin air- it was all Prankster’s gold. If players return to the same spot, they’ll see empty vials that probably contained the liquid where the pile originally was, complete with labels detailing what the liquid does.", "As the party rounds a corner or passes through a chokepoint, a small glinting ball bounces on the ground towards them before exploding into a massive cloud of whitish smoke. The party’s been ambushed by some kind of clever, intelligent pack of hunters, hopefully appropriate to their level. The exits to the room are so small that attempts to blow the smoke away can only siphon away so much at a time.", "The party walks into a room to be met only by a button and next to it are scribbles seeming to make out “DO NOT TOUCH.” As the final party member enters the room, the door slams shut and the 4 walls of the room flip, revealing walls lined with spikes that slowly encroach on the party. The walls are indestructible and unstoppable, and every time the button in the center of the room is pressed, the walls recede back to their starting position only to crawl towards the party once more. The only way out if the situation is to heed the advice of the sign. Right as the walls are pressing the party members together, about to impale them all, the walls will reset, for good, and the door will reappear, letting the party escape. The trap can only be reset by having every member of the party leave and then reenter. A funny, harmless trap that will either starve a mistrusting group to death or make them panic.", 
                "The walls of this room are lined with intricate carvings that appear to be dwarven in nature. They depict grand battles between dwarves and orcs that lead to a large set of stone double doors at the opposite end of the room. The doors depict a dwarf holding up a hammer that sparks with lightning. In the center of the room are 3 small pedestals and one larger pedestal in the middle. Each small pedestal has a stone tablet on it. Each tablet has a different word written on it: Others, Yourself, and Justice. To get the stone doors on the opposite side of the room to open, the party must put the tablets on the large center pedestal, placing Yourself on the bottom, Others atop it, and Justice at the very top. Once this is completed, the letters JOY will light up and the stone double doors swing open.", "Dave – An 78-year old human commoner who has no idea who was captured for slavery by the owner(s) of the dungeon – has a curse on him that activates after 1d4 days, and casts Fireball on him. The curse was applied by his ex, a vengeful witch who he had abandoned after learning of her true nature.", "A ghost bard of no fame who never got the chance to perform at the big show. He has come back from the great beyond to find that he can no long play his trumpet.", "A room which disguises itself as the childhood room of the first to enter. When enough people enter, the room locks. There is a significant difference that the one who first entered can spot with a DC 14 Intelligence saving throw to escape. Each time they fail, a nightmarish creature based on one of their childhood fears appears and the party must fight it.", "An eternal campfire burns in this room. The adventurers shadows appear on the dungeon wall, which turn into Shadows from the Monster Manual. The taller the adventurer, the more powerful the Shadow will be. The fire can only be put out by dousing it with holy water or some other curse removal.", 
                "Party enters a smallish, circular room, with a simple wooden door. There is a wooden door on the far side of the room, locked. The room has nothing but a simple wooden table, upon which is a single vase, containing a large, dark purple flower. If the party investigates, the flower is nightshade, and the vase is of unknown origin. Everything here is ordinary, other than the table, which is a mimic. Let it lie still until after the party investigates the flower/vase (if at all), just for the extra surprise factor.", "The party finds a scared Gazer whimpering in a corner of a room. It will cry and whimper if the party approaches. If the party can earn its trust, it will hang around and give playful licks. What will happen when the party finds the Beholder searching for his pet?", "You come across a large furnace in a dead end of the cave. It’s a fancy, built-in brick oven. If you open its cast iron door you hear faint moans and echoes. Inside it is pitch black, even with darkvision you cannot see the bottom. If you drop a lit torch you see hundreds upon hundreds of zombies and other shambling undead monsters converging on the light until it is extinguished.", "A goblin named Sam smorkle who is just looking for rusty things. If given a rusty thing he’ll help you until the next rusty things is found, where he’ll quickly work himself up into a frenzy and accuse you of wanting the rusty item. Roll initiative.", "A labyrinth eventually leads to a center room. The room appears to be a study with a table in the middle featuring an exact scale model of the labyrinth, including miniatures of the PCs themselves. Another miniature can be seen, of some hideous monstrosity, and its heading for the center room…", "The party finds a tiny portal to the Far Realm. An impossibly huge eye is looking at them… then after a few seconds the portal snaps shut leaving behind an strange small polyhedral made of a hard unknown material that somehow inspires awe and fear.", "The party finds an gold vein that has been roughly ‘mined out’. If they follow it, they find a hive of rust monsters eating the ore. If disturbed the RMs with spill out into the dungeon and eventually the surface (maybe destroying a nearby village).",
            ];

            function dressings(n){
                let dungeon = {
                    "Location": ["beneath a building in a city", "built into the catacombs or sewers beneath a city", "beneath a farmhouse", "beneath a graveyard", "beneath a ruined castle", "beneath a ruined city", "beneath a temple", "in a chasm", "in a cliff face", "in a desert", "in a forest", "in a glacier", "in a gorge", "in a jungle", "in a mountain pass", "in a swamp", "beneath or on top of a mesa", "in sea caves", "in several connected mesas", "on a mountain peak", " on a promontory", "on an island", "underwater", `${searchArray(["in the branches of a tree","around a geyser", "behind a waterfall","buried in an avalanche","buried in a sandstorm", "buried in volcanic ash","Sunk in a swamp", "floating on the sea", "in a meteorite","on a demiplane or pocket dimension", "in an area devastated by a magical catastrophe", "on a cloud", "in the Feywild", "in the Shadowfell", "on an island in an underground sea","In a volcano","on the back of a gargantuan living creature","sealed in a magical dome of force","inside a mordenkainen's magnificent mansion"])}`],
                    "Creator": {
                        "Basic": ["Beholder", `a group of ${buildRace(0)}`, "group of giants", "group of Hobgoblins", "group of Kuo-Toa", "Lich", "group of Mind Flayers", "group of Yuan-Ti", `group of ${searchArray(['Devils','Demons','Celestials'])}`, "natural or magical phenomena"],
                        "Human": {
                            "Alignment": ["Lawful good", "Neutral good", "Chaotic good", "Lawful neutral", "Neutral", "Chaotic neutral", "Lawful evil", "Neutral evil", "Chaotic evil"],
                            "Class": ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
                        }
                    },
                    "Purpose": {
                        "death trap": ["antechamber or waiting room for spectators", "guardroom fortified against intruders", `vault for holding important treasures, accessible only by locked or secret door (${searchArray(["trapped","trapped","trapped","not trapped"])})`, "room containing a puzzle that must be solved to bypass a trap or monster", "trap designed to kill or capture creatures", "observation room, allowing guards or spectators to observe creatures moving through the dungeon"],
                        "lair": ["armory stocked with weapons and armor", "audience chamber used to recieve guests", "banquet room used for important celebrations", "barracks where the lairs defenders are quartered", "bedroom for use by leaders", "chapel where the lair's inhabitants worship", "cistern or well for drinking water", "guardroom for defense of the lair", "kennel for pets and guard beasts", "kitchen for food storage and preparation", "pen or prison where captives are held", "storage, mostly nonperishable goods", "throne room where the lairs leaders hold court", "torture chamber", "training and exercise room", "trophy room or museum", "latrine or bath", "workshop for the contruction of weapons, armor, tools, and other goods"],
                        "maze": ["conjuring room, used to summon creatures that guard the maze", "guardroom for sentinel that patrol the maze", "lair for guard beasts that partol the maze", "pen or prison accessible only by secret door, used to hold captives condemned to the maze", "shrine dedicated to a god or other entity", "storage for food, as well as tools used by the maze's guardians to keep the complex in working order", "trap to confound or kill those sent into the maze", "well that provides drinking water", "workshop where doors, torch sconces, and other furnishings are repaired and maintained"],
                        "mine": ["barracks for miners", "bedroom for a supervisor or manager", "chapel dedicated to a patron diety of miners, earth, or protection", "cistern providing drinking water for miners", "guardroom", "kitchen used to feed workers", "laboratory used to conduct test on strange minerals extracted from the mine", `lode where metal ore is mined (${searchArray(["depleted","depleted","depleted","some ore left"])})`, "office used by the mine supervisor", "smithy for repairing damaged tools", "storage for tools and other equipment", "storage room or vault used to store ore for transport to the surface"],
                        "planar gate": ["decorated foyer antechamber", "armory used by the portal's guardians", "audience chamber for recieving visitors", "barracks used by the portal's guards", "bedroom for use by the high tanking members of the order that guards the portal", "chapel dedicated to a diety or dieties related to the protal and its defender", "cistern providing fresh water", "classroom for use of initiates learning about the portal's secrets", "conjuring room for summoning creatures used to investigate or defend the portal", "crypt where the remains of those that died guarding the portal are kept", "dining room", "divination room used to investigate the portal and events tied to it", "dormitory for visitors and guards", "entry room or vestibule", "gallery used for displaying trophies and objects related to the portal and those that guard it", "guardroom to protect or watch over the portal", "kitchen", "laboratory for conducting experiments related to the portal and the creatures that emerge from it", "library holding books abour the protal's history", "pen or prison for holding captives or creatures that emerge from the portal", `planar junction, where the gate to another plane ${searchArray(["once stood", "once stood","once stood", "is currently active"])}`, "storage", "strong room or vault, for guarding valuable treasures connected to the portal or funds used to pay the planar gate's guardians", "study", "torture chamber, for questioning creatures that pass through the portal or to clandestinely use it", "latrine or bath", "workshop for constructing the tools and gear needed to study the portal"],
                        "strongold": ["antechamber where visitors seeking access to the stronghold wait", "armory holding high-quality gear, including light siege weapons such as ballistas", "audience chamber used by the master of the stronghold to recieve visitors", "aviary or zoo for keeping exotic creatures", "banquet room for hosting celebrations and guests", "barracks used by elite guards", "bath outfitted with a marble floor and other luxurious accroutrements", "bedroom for use by the stronghold's master and other important guests", "chapel dedicated to a diety associated with the stronghold's master", "cistern providing drinking water", "dining room for intimate gatherings or informal meals", "dressing room featuring a number of wardrobes", "gallery for the display of expensive works of art and trophies", "game room used to entertain visitors", "guardroom", "kennel where monsters or trained animals that protect the stronghold are kept", "kitchen designed to prepare exotic foods for large numbers of guests", "library with an extensive collection of rare books", "lounge used to entertain guests", "pantry, including cellar for wine or spirits", "sitting room for family and intimate guests", "stable", "storage for mundane goods and supplies", `strong room or vault for protecting important treasures ${searchArray(["hidden behind a secret door","hidden behind a secret door","hidden behind a secret door","and the door is not hidden"])}`, "study, including a writing desk", "throneroom elaborately decorated", "waiting room where lesser guests are held before recieving an audience", "latrine or bath", "crypt blonging to the stronghold's master or someone else of importance"],
                        "temple/shrine": ["armory filled with weapons and armor, battle banners, and pennants", "audience chamber where priests of the temple recieve commoners and low-ranking visitors", "banquet room used for celebrations and holy days", "barracks for the temple's military arm or its hired guards", "cells where the faithful can sit in quiet contemplation", "central temple built to accomodate rituas", "chapel dedicated to a lesser diety associated with the temple's major diety", "classroom used to train initiates and priests", "conjuring room, specially sanctified and used to summon extraplanar creatures", "crypt for a high priest or similar figure, hidden and heavily guarded by creatures and traps", "divination room, inscribed with runes and stocked with soothsaying elements", "dining room (small), for the temple's high priests", "dining room (large) for the temple's servants and lesser priests", "dormitory for lesser priests or students", "guardroom", "kennel for animals or monsters associated with the temple's diety", "kitchen (might bear a disturbing resemblance to a torture chamber in an evil temple", "library, well stocked with religious treatises", "prison for captured enemies (in good or neutral temples) or those designated for sacrifices (in evil temples)", "robing room containing ceremonial outfits and items", "stable for riding horses and mounts belonging to the temple, or for visiting messengers and caravans", "storage holding mundane supplies", "strong room or vault holding important relics and ceremonial items, heavily trapped", "torture chamber, used in inquisitions (in lawful good and neutral temples) or for the sheer joy of causing pain (evil temples)", "latrine or bath", "well for drinking water, defendable in the case of attack or siege", "workshop for repairing or creating weapons, religious item, and tools"],
                        "tomb": ["antechamber for those that have come to pay respect to the dead or prepare themselves for burial rituals", "chapel dedicated to dieties that watch over the dead and protect their restng places", "a crypt for less important burials", "divination room, used in rituals to contact the dead for guidance", "false crypt(trapped) used to kill or capture thieves", "gallery to display the deeds of the deceased through trophies, statues, paintings, and so forth", "grand crypt for a noble, high priest, or other important indivudal", "guardroom, usually guarded by undead, constructs, or other creatures that do not need to eat or sleep", "robing room for preists to prepare for burial rituals", "storage, stocked with tools for maintaining the tomb and preparing the dead for burial", "tomb where the wealthiest and more important folk are interred, protected by secret doors and traps", "workshop for embalming the dead"],
                        "treasure vault": ["antechamber for visiting dignitaries", "armory containing mundane and magic gear used by the treasure vault's guards", "barracks for the guards", "cistern providing fresh water", "guardroom for defending against intruders", "kennel for trained beasts used to guard the treasure vault", "kitchen for feeding gaurds", "watch room that allows guards to observe those who approach the dungeon", "prison for holding captured intruders", "strong room or vault, for guarding the treasure hidden in the dungeon, accessible only by a locked secret door", "torture chamber for extracting information from captured intruders", "trap or other trick designed to kill or capture creatures that enter the dungeon", ],
                    },
                    "History": ["has been long since abandoned", "has been abandoned due to a plague", "has been conquered by invaders", "is avoided due to attacking raiders", "the pioneers of the area were destroyed by a discovery made within", "infighting destroyed the first residents", "is the site of a magical catastrophe, killing the first ones here", "has been battered and deemed unusable due to natural disasters", "this location has been cursed by the gods and shunned", `is currently under intelligent control`, "is overrun by planar creatures", "is the site of a great miracle", ],
                    "Layout": {
                        "Door": {
                            "Type": ["wooden", "wooden, barred or locked", "stone", "stone, barred or locked", "iron", "iron, barred or locked", "portcullis", "portcullis, locked in place", "secret door", "secred door, barred or locked", ],
                            "Beyond": ["a passage extending 10 ft., then T intersection extending 10ft. to the right and left", "passage 20 ft. straight ahead", "false door with trap", ],
                        },
                        "Chamber Types": ["antechamber", "armory", "audience chamber", "Aviary", "Banquet room", "barracks", "bath or latrine", "bedrooms", "bestiary", "cell", "chantry", "chapel", "cistern", "classroom", "closet", "conjuring room", "court", "crypt", "dining room", "divination room", "dormitory", "Dressing room", " entry room or vestibule", "Gallery", "Game room", "guardroom", "Hall", "great hall", "Hallway", "Kennel", "Kitchen", "laboratory", "Library", "Lounge", "meditation chamber", "Observatory", "office", "Pantry", "pen or prison", "reception room", "refectory", "robing room", "salon", "shrine", "sitting room", "smithy", "stable", "storage room", "strong room or vault", "study", "temple", "throne room", "torture chamber", "training or exercise room", "trophy room or museum", "waiting room", "nursery or schoolroom", "well", "workshop"],
                        "State": ["rubble, ceiling partially collapsed", "holes, floor partially collapsed", "Ashes, contents mostly burned", "used as a campsite", "pool of water, chambers original contents are water damaged", "furniture wrecked but still present", `Converted to a(n) ${searchArray(["antechamber", "armory", "audience chamber", "Aviary", "Banquet room", "barracks", "bath or latrine", "bedrooms", "bestiary", "cell", "chantry", "chapel", "cistern", "classroom", "closet", "conjuring room", "court", "crypt", "dining room", "divination room", "dormitory", "Dressing room", " entry room or vestibule", "Gallery", "Game room", "guardroom", "Hall", "great hall", "Hallway", "Kennel", "Kitchen", "laboratory", "Library", "Lounge", "meditation chamber", "Observatory", "office", "Pantry", "pen or prison", "reception room", "refectory", "robing room", "salon", "shrine", "sitting room", "smithy", "stable", "storage room", "strong room or vault", "study", "temple", "throne room", "torture chamber", "training or exercise room", "trophy room or museum", "waiting room", "nursery or schoolroom", "well", "workshop"])}`, "Stripped bare", "Pristine and in original state"]
                    },
                }
                let rooms = []
                let pickedPurpose = searchArray(Object.keys(dungeon.Purpose));
                let creatorPick = ''

                function creator(){
                    if (rollDice(100) < 50) {
                        return `a ${searchArray(dungeon.Creator.Basic)}`
                    } else {
                        return `a humanoid, specifically a ${searchArray(dungeon.Creator.Human.Alignment)} aligned ${buildRace(1)} ${searchArray(dungeon.Creator.Human.Class)}`;
                    };
                };
                function history(){
                    return `This ${searchArray(['dungeon','area of interest','ruins'])} is ${searchArray(dungeon.Location)}, it was created by ${creatorPick}. Historically it has been used as a ${pickedPurpose}. Also, it ${searchArray(dungeon.History)}.`
                };
                function entrance(){
                    return `The entrance of this dungeon lets into a(n) ${searchArray(dungeon.Layout["Chamber Types"])}, likely this area was a(n) ${searchArray(dungeon.Purpose[pickedPurpose])}.`
                };
                function newroom(x){
                    for (i = 0; i <= x; i++) {
                        let z = ''
                        if (rollDice(100) < 33) {
                            do {
                            z= `A(n) ${searchArray(dungeon.Layout["Chamber Types"])}. Hints of ${searchArray(['current','past','future'])} use as a ${searchArray(dungeon.Purpose[pickedPurpose])}. Current state: ${searchArray(dungeon.Layout.State)},`
                            } while (checkConflict(z,rooms) === 1) 
                            rooms.push(z)
                        } else if (rollDice(100) < 66) {
                            do {
                                z= searchArray(encounter)
                            } while (checkConflict(z,rooms) === 1) 
                            rooms.push(z)
                        } else {
                            do {
                                z= searchArray(trap)
                            } while (checkConflict(z,rooms) === 1) 
                            rooms.push(z)
                        }
                    };
                };
                function randomDesc(num){
                    let a = num
                    let desc = []
                    description.push('Other general dressings:')
                    description.push(`Air: ${searchArray(airQuality)} & ${searchArray(airCurrents)}`)
                    description.push(`Odor: ${searchArray(odors)}`)
                    description.push(`Sounds: ${searchArray(soundsAndNoises)}`)
                    for (i = 0; i <= a; i++) {
                        let b =''
                        do {
                            if (rollDice(100)<20){
                                b = ` General: ${searchArray(generalFeatures, miscItems)}; `
                            } else if (rollDice(100)<40) {
                                b = ` Grafitti: ${searchArray(graffiti)}; `
                            } else if (rollDice(100)<60) {
                                b = ` Furnishing: ${searchArray(generalFurnishings, tortureFurnishings, arcaneFurnishings)}; `
                            } else if (rollDice(100)<80) {
                                b = ` Random: ${searchArray(searchArray([clothes, religiousArticles, containerContents]))}; `
                            }
                        } while (checkConflict(b,desc) === 1)
                        desc.push(b)
                    }
                    return desc
                };

                creatorPick = creator()
                description.push(history())
                description.push(randomDesc(currentSize))

                ent = entrance()
                newroom(n-1)
                return rooms
            };

        //10. Create and priny a randomized dunegon based off the rules in 52 card dungeon with my own twist
            dungeon.push([currentX,currentY,currentZ]) 
            buildDungeon(input)
            dungeon[0].sort(compareFn)
            let descArray = dressings(currentSize)
            let descfinal = addEncounters(currentSize,descArray)
            bossDesc(descfinal)
            let Axe = combineArrays(dungeon, descfinal, currentSize+1)
        //document.getElementById("Dungeon").innerHTML = description
        //document.getElementById("DungeonKey").innerHTML = 
        loopPrintList(description, "Dungeon") 
        loopPrintList(Axe, "DungeonKey") 
};

function policy (n) {
    document.getElementById("Policy").innerHTML = ''
    let military = [
        `Resource management: +strategic Production in all cities, +strategic yield.`, `Third Alternative: ++gold and +culture from military and strategic developments.`, `Survey: double experience for recon units.`, `Disipline: +++combat strength when fighting bandits.`, `Agoge: +Production toward ranged and anti-calvary units.`, `Maritime industries: ++production towards naval units.`, `Maneuver = +production towards calvary units.`, `Conscription: -gold cost for unit maintenance.`, `Limitanei	- +loyalty for cities with garrisons.`, `Raid: Double yields for pillaging.`, `Veterancy: +production towards encampements and harbors.`, `Equestrian orders: +Yield for horses and iron .`, `Bastions: +city defense and ranged strength.`, `Limes: double production towards defensive buildings.`, `Feudal contract: +production towards melee, ranged, and anti-calvary units.`, `Retainers: +amenity for cities with a garrison.`, `Sack: +Yield from pillaging districts.`, `Professional army: -cost toward unit upgrades.`, `Retinues: -resource cost towards unit upgrades.`, `Craftsmen: double industrial zone adjacency bonuses.`, 
        `Chivalry: +production towards light and heavy calvary units.`, `Native conquest: +gold per earlier era unit conquest.`, `Wars of religion: +combat strength towards civs with different religion .`, `Logistics: +movement in friendly territory .`, `Drill Manuals: +yields for niter and coal.`, `Grande Armee: +production for melee ranged and anti-calvary units.`, `National identity: less combat strength loss from taking damage in battle.`, `Press Gangs: double production towards naval units.`, `Military research: +science for military buildings.`, `Force modernization: -gold cost for unit upgrades.`, `Total war: double Yield from coastal pillaging and raids and for plundering trade routes.`, `Propaganda: -war weariness over time.`, `Levee en masse: -gold cost for unit maintenance.`, `Lightning warfare: +production for calvary units.`, `Patriotic war: double production for all military support units.`, `Internation waters: Double production towards all naval units.`, `Military first: +production on all melee, anti calvary, and ranged units.`, `Integrated Space cell: +production towards military-beneficial sciences.`, `Second strike capability: -gold cost for large military weapon maintenance.`, `Strategic air force: +production toward all flying units.`, `After action reports: +experience from combat.`, `Their finest hour: +production towards air units, +strength in home territory.`, `Martial law: -war weariness, ++loyalty for cities with garrisons.`, `Defense of the motherland: NO war weariness from combat in home territory, doubel production for support units.`
    ];
    let economic = [
        `God king: +gold and +faith in capital.`, `Urban planning: +production in all cities.`, `Ilkum: +production to regional development.`, `Caravansaries: +gold from all trade routes.`, `Corvee: +production toward wonders.`, `Land surveyors	- reduce cost for expansion.`, `Colonization: +Production towards new cities.`, `Insulae: +housing in all cities with 2+districts.`, `Natural Philosophy: double efficiency to campus-adjacent tiles.`, `Scripture: double efficiency to holy site adjacent tiles.`, `Naval Infrastructure: double efficiency to harbor adjacent tiles.`, `Serfdom: +builder efficiency.`, `Meritocracy: +culter per specialty district.`, `Trade confederation: +culture and science from cross region trade routes.`, `Aesthetics: double efficiency to theater adjacent tiles.`, `Medina quarter: +housing to cities with 3+ specialty districts.`, `Town Charters: double efficiency to commercial hub adjacent districts.`, `Gothic architecture: +production to wonders.`, `Civil prestige: + amenity and housing to established govenors.`, `Simultaneum: double faith effectivness and even more if adjacent to 3 adjacency bones.`, 
        `Religious orders: +faith based combat.`, `Triangular trade: ++gold and +faith from all trade routes.`, `Rationalism: double science efficiencyfrom campus, +population.`, `Free market: double gold efficiency from commercial hub, +population.`, `Liberalism: +amenities to all cities with 2+ specialty districts.`, `Public works: +production toward regional development and builder efficiency.`, `Skyscrapers: +production towards wonders.`, `Grand opera: double culture efficiency from theater square, +population.`, `Public transport: +gold when farms are replaced with neighborhoods, +food, gold, and production from neighborhoods.`, `Expropiation: -cost for regional expansion.`, `Market economy:  +gold, culture, and science per interegional trade routes + strategic resources.`, `Economic union: double commercial hub and harbor district adjaceny bonuses.`, `New Deal: ++housing, +amenities ---gold to cities with 3+ specialty districts.`, `Five-year-plan: double campus and industrial zone adjacency bonuses.`, `Collectivization: ++food and + Production from domestic trade routes .`, `Heritage tourism: double tourism from great works and artifacts .`, `Sports media: double theater square adjacency bonuses, stadiums +amenity.`, `Satellite Broadcasts: quadruple tourism from great works of music .`, `Ecommerce: +++production and ++++gold from international trade routes, half from others.`
    ];
    let wildcard =[
        `Strategos: +great general develpoment.`, `Inspiraiton: +great scientist development.`, `Revelation: +great prophet development.`, `Literary tradition: +great writer development.`, `Navigation: +great admiral development.`, `Travelling Merchants: +great merchant development.`, `Invention: ++great engineer development, also + per workshop.`, `Frescoes: ++great artist development, also +per museum.`, `Symphonies: ++great musician development, also + per broadcast center.`, `Military organization: ++great general development and +movement, also + per Armory.`, `Laissez-Faire: ++great merchant development, also + per Bank, ++great admiral development, also +per shipyard.`, `Nobel prize: ++great scientist development.`, `Science Foundations: ++great scientist development, also + per university, ++great engineer development per power plant, also +per factory.`, `Aerospace contractors: +aluminum and +power.`,
        `Space tourism: reduce tourism towards other civilizations.`, `Hallyu: Improved bards.`, `Non-state actors: improved spies.`, `Integrated attack logistics: +movement starting in enemy territory, +Production towards detah robots.`, `Rabblerousing: +diplomatic favor, -cost of diplomatic actions.`, `Diplomatic capital: ++diplomatic favor.`, `Global coalition: +++combat strength in friendly territory.`, `Autocratic legacy: +Yield for all government buildings.`, `Republican legacy: +housing and amenities.`, `Oligarchic legacy: ++combat strength for all land melee, anti-calvary, and naval melee.`, `Mercantile legacy: +gold for cities with an established govenor.`, `Monarchic legacy: +housing per level of wall.`, `Theocratic legacy: ++religious strength and faith .`, `Communist legacy: +production based on size.`, `Democratic legacy: +production and housing per district, ++food and Production per suzerain trade route.`, `Fascist legacy: ++combat strength and -war weariness.`
    ];
    let diplomatic = [
        `Charismatic leader: +influence.`, `Diplomatic League: +envoys.`, `Paetorium: +loyalty.`, `Merchant Confederation: +gold from envoys.`, `Colonial offices: +citygrowth in initial region, +loyalty in different regions.`, `Machiavellianism: +spies efficiency.`, `Wisselbanken: +food, +production, +alliance points from trade routes to cities or city states.`, `Colonial Taxes: +gold and production for cities in new regions.`, `Raj: +gold, science, culture, faith for suzerain status, and trade routes to those city states.`, `Police state: -enemy spy effectiveness, -amenities, -loyalty.`,
        `Nuclear espionage: +spy effectiveness when stealing tech.`, `Arsenal of Democracy: ++food and production for both allied cities in a trade route.`, `Gunboat Diplomacy: Open borders with city states ++influence toward envoys.`, `Cryptography: -enemy spy effectiveness in your lands, +spy effectiveness in enemy lands.`, `Containment: +envoy effectiveness if a different government.`, `Music Censorship: -bard proliferation from other civs, -1 amenity in big cities.`, `International space agency: +science per city state suzerain status and allied civ.`, `Collective activism: +culture per city state suzerain and allied civ.`, `Communications office: +loyalty per city.`
    ];
    let darkAge =[
        `Monasticism: +++science for cities with a holy site, -culture in all cities.`, `Twilight valor: ++combat strength for all melee, cannot heal outside fo territory.`, `Inquisition: +++++religious strength, -science in all cities.`, `Isolationism: ++food and ++production, no regional expansion allowed.`, `Letters of Marque: doubel production for naval units, ++movement, double trade route plunder yield, half all regular trade route yield.`, `Robber Barons: +++++gold in cities with stock exchange, ++production for factories, --amenities.`, `Elite Forces: double experience for combat, ++gold cost for maintenance.`, `Collectivism: +food and ++housing per farm, double industrial zone adjacency bonuses, --great person development.`,
        `Rogue state: +++++production towards covilization weapons, no envoy development.`, `Flower power: double toruism for civs not at war, double cost for all land units.`, `Cyber Warfare: +++++combat strength for advanced units, civ grievances do not decay.`, `Automated workforce: ++production towards city projects, -amenity and ----loyalty in cities.`, `Disinformation campaign: +++diplomatic favor per broadcast center, -science and culture in all cities.`, `Decentralization: small cities gain ++loyalty, large cities --gold.`, `Samderzhaviye: +++++Production in the capital, no governors allowed.`, `Soft targets: +++++combat strength vs city attacks and defenses, --combat strength vs units.`, `Despotic paternalism: ++loyalty for cities with govenors, --science and culture for cities without governors. .`,
    ];
    let goldenAge = [
        `Monumentality: Faster regional expansion, +faith based expansion.`, `Exodus of the evangelists: Faster religious spread, more effective prosletizing, ++great prophet development.`, `Mandala state: ++culture for every wonder, --enemy city loyalty per wonder.`, `Free Inquiry: commercial hub and harbor gold provides science as well, campus provides gold equal to science.`, `Praetorian guard: ++unit healing per turn, ++production to military buildings.`, `Sakdina: +loyalty, +all great person development.`, `Reform the coinage: Traders cannot be plundered, ++gold per specialty district in the foreign city from trades.`,
        `Heartbeat of steam: +production toward wonders, science district adjacency bonus also adds production.`, `To Arms!: +++combat experience, ++Production towards military units.`, `Culture Industry: +culture per specialty district, ++production towards non-specialty districts, faith based growht and development.`, `Wish you were here: double tourism for national parks: +++tourism for world wonders.`, `Popular Front: double diplomatic favor from suzerain status, ++to all trade route yields.`, `Solidarity: ++gold, faith, and loyalty from govenors.`, `Sky and stars: +++ production towards flight-based buildings, +science and production in cities with flight based buildings.`, `Military-industrial complex: +aluminum, oil, and uranium yield, ++combat strength and +combat range.`
    ];
    function templatepicker(){
        let options = []
        do {
            let a = searchArray(military)
            if (checkConflict(a,options) === 0){
                options.push(`Military | ${a}`)
            }
            let b = searchArray(diplomatic)
            if (checkConflict(b,options) === 0){
                options.push(`Diplomatic | ${b}`)
            }
            let c = searchArray(economic)
            if (checkConflict(c,options) === 0){
                options.push(`Economic | ${c}`)
            }
            let d = searchArray(wildcard)
            if (checkConflict(d,options) === 0){
                options.push(`Wildcard | ${d}`)
            }
            let e = searchArray(darkAge)
            if (checkConflict(e,options) === 0){
                options.push(`Dark Age | ${e}`)
            }
            let f = searchArray(goldenAge)
            if (checkConflict(f,options) === 0){
                options.push(`Golden Age | ${f}`)
            }
        } while (options.length < 42)
        return options
    };
    function buildGovernment(n){
        let x = templatepicker()
        let z = []
        do {
            let y = searchArray(x)
            if (checkConflict(y,z) === 0){
                z.push(y)
            }
        } while (z.length < n )
        return z
    }

    let x = []
    let y = buildGovernment(n)
    do {
        x.push(`${(rollDice(4)+5) * (rollDice(4)+4) * (rollDice(4)+3) + (rollDice(500)) + ' years'}`)
    } while (x.length < y.length)
    
    let output = combineArrays(x,y,y.length)
    loopPrintList(output,"Policy")
};

function religion(n) {
    document.getElementById("Religion").innerHTML = ''
    let beliefs =[
        `+culture and faith from shrines`,
        `++faith for wonders`,
        `++food, faith, and housing for shrines and temples`,
        `Faith based campus and theater building`,
        `+housing for shrines and temples, ++gold from trade routes`,
        `faith-based warriors`,
        `+production from followers, holy sites +produciton and faith`,
        `+amenity in cities with 2 specialty districts`
    ];
    let worship = [
        `+++faith, 1 slot for religious art`,
        `+++faith, +1faith per era, cannot be pillaged or destroyed`,
        `+++faith, ++food, +housing`,
        `+++faith, ++production`,
        `+++faith, faster religious spread`,
        `+++faith, +housing, +diplomatic favor`,
        `+++faith, +amenity`,
        `+++++faith`,
        `+++faith, ++science`
    ];
    let founder = [
        `++gold per city`,
        `+science per city`,
        `+faith and +culture per holy site or theater square`,
        `+Yield from allied civs, +religious pressure`,
        `++faith per city`,
        `+envoy when city converts`,
        `++science, culture, gold, faith from each city with wonders`,
        `+science and gold per campus or commercial hub`,
        `+++gold per city`,
        `+culture per city`
    ];
    let enhancer = [
        `cultural growth near holy sites`,
        `+++++combat strength near foreign cities with this religion`,
        `+++combat strength near friendly cities with this religion`,
        `---cost for faith units`,
        `++++healing near holy cites`,
        `+++religious spread`,
        `Religious units ignore difficult terrain`,
        `Religous pressure is increased, even more when printing is researched`
    ]
    function religionPicker(){
        let options = []
        do {
            let a = searchArray(beliefs)
            if (checkConflict(a,options) === 0){
                options.push(`Beliefs | ${a}`)
            }
            let b = searchArray(worship)
            if (checkConflict(b,options) === 0){
                options.push(`Worship | ${b}`)
            }
            let c = searchArray(founder)
            if (checkConflict(c,options) === 0){
                options.push(`Founding Principle | ${c}`)
            }
            let d = searchArray(enhancer)
            if (checkConflict(d,options) === 0){
                options.push(`Enhancer | ${d}`)
            }
        } while (options.length <= 16)
        return options
    };
    function buildReligion(n){
        let x = religionPicker()
        let z = []
        do {
            let y = searchArray(x)
            if (checkConflict(y,z) === 0){
                z.push(y)
            }
        } while (z.length < n )
        return z
    }
    loopPrintList(buildReligion(n),"Religion")

};



