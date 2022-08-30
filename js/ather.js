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



function quest() {
    let themeArray = ['Exploration', 'Comedy', `${searchArray(['Investigation', 'Mystery'])}`, 'Combat','Urban','Simulation (video game-like)',`${searchArray(['Kingmaker', 'Management'])}`, `${searchArray(['Action', 'Adventure'])}`, 'Horror', 'Espionage','Romance','Revenge',`${searchArray(['Collecting', 'Ranching'])}`]
    let goalArray = ['Money', 'Combat Power', 'Political/ influential Power','Rescue', 'Escape','Explore a new area','Retrieve','Thwart a plan', `Protect a ${searchArray(['place', 'NPC or PC', 'Artifact'])}`, `Win a ${searchArray(['small', 'large'])}-scale conflict`,'Settle a debt','clear a name']
    let rewardArray = ['Gold','Magic item','Lore/ knowledge','Cool but mostly useless items','Plot relevant item',`${searchArray(['NPC Contact', 'Ally', 'New Friend'])}`,`${searchArray(['New pet', 'New follower'])}`, `${searchArray(['New skill', 'New language'])}`, 'interesting trinket', `${searchArray(['Boon', 'Blessing','Charm'])}`, ,`Mundane ${searchArray(['Weapon', 'Armor', 'misc.'])} with a cool backstory`, 'Repairable broken item','New mode of transport', `${searchArray(['Property', 'Land and Title'])}`, 'Faction favor', 'Backstory connection', 'Trophy', `${searchArray(['Crafting materials', 'Crafting Recipes'])}`, 'Feats']
    let factionArray =['Home','Echos','Undead','Nature','Dragons','Gure','Gnolls','Fey','Radiant','Dieties']


    let actionTropes = ['Being a B.A.','Big trope hunting','Chase scene','Combat','Dueling','Escape','Fight scene','I have your index','Index to the rescue','Just in time','VIOLENCE']
    let crimeTropes = ['confidence (scams, frauds, tricks)','organized crime','Gambling',' sex trade','Smuggling','Thievery','Drugs','Vandalism','Victimhood','Abuse','kidnapping, hostages, abduction',' murder','terrorism','threatening','banishment','censorship','law enforcement','courtroom','execution','forensics','perp sweating','prison']
    let dramaTropes = ['Betrayal','confession','conflict','emotion','infidelity','price of power','rejection','revenge','serious','subverted innocence','had a hard life','victimhoom','violence']
    let espionageTropes = ['betrayal','Disguise','being watched','infauxmation','ninja','classified','stealth','truth and lies']
    let fairyTaleTropes = ['Abduction is love','Abusive parents','Aliens','an arm and a leg',`Androcles' lion`,'an ice person','animate inanimate objects','anthropomorphic personification','attention deficit... ooh, shiny!','back from the dead','bad boss','bears are bad news','beauty equals goodness','be careful what you wish for','the big bad wolf','big fancy castle','blue blood',' bothering by the book','bride and switch','cain and able','changeling tale','clingy macguffin','curse + escape clause','damsel in distress','dances and balls','david versus goliath','dead all along','deader than dead','deal with the devil','deceased parents are the best','distressed dude','doe snot like shoes',`don't go into the woods`,'double-in law marriage','dragon hoard','dragons prefer princesses','dude, wheres my respect?','due to the dead','earn your happy ending','enchanted forest','engagement challenge','evil matriarch','evil old folks','evil sorcere','evil tower of ominousness','exact eavesdropping','the fair folk','the fairest of them all','fairy devilmother','fairy godmother','fairy tale episode','fairy tale free-for-all','fake ultimate hero','fallen-on-hard-times job','faimly-unfriendly death','family-unfriendly violence','faux death','feminine women can cook','food chains','the fool','forbidden fruit','forced transformation','fractured fairy tale','gender flip','genie in a bottle','giant food','gingerbread house','girl in the tower','girl who fits the slipper','prince chamring','god save us form the queen','the good king','good princess, evil queen','greed','green-eyed monster','grimminfication','hair of gold, heart of gold','happily ever after','haunted castle','headless horseman','hedge of throns','heir club for men','hitchiker heroes','honorary uncle','hot witch','i know your true name','if i cant have you','impossible task','impossible theft','intangible theft','invisible to adults','involuntary shapeshifter','just liek robin hood','the kingdom','knight in shining armor','laser-guided karma','last request','law of inverse fertility','leaf boat','liminal time','little red fighting hood','love at first sight','mad scientists beautiful daughter','massive numbered siblings','malicious slander','macguffing guardian','meaningful name','merciful minion','mock millionaire','moving the goalposts','nameless narrative','noble fugitive','obfuscating stupidity','obnoxious-in-laws','offered the crown','offing the offpsring','off with his head!','old beggar test',
    'once upon a time','original position fallacy','our fairies are different','our witches are different','overprotective dad','pinnochio syndrome','please shoot the messenger','prince charming','princess for a day','princess protagonist','the promise',' proud beauty','the quest','rags to royalty','ragtag bunch of misfits','rash promise','re-headed stepchild','rescue romance','rip-van-winkle','royal brat','royal blood','rule of three','rule of seven','the runt at the end','the sandman','save the princess','schmuck banquet','scullery maid','secret identity','secret test of character','self-fulfilliong prophecy','shapeshifter shwodown','shapeshifting lover','she cleans up nicely','sibling triangle','soul jar','standard hero reward','swans a swimming','sweet and sour grapes','talking animal','threshold guardians','trail of bread crumbs','treacherous spirit chase',`true love's kiss`,'turtle island','Uriah Gambit','Wealthy ever after','what ever happened to the mouse?','When the clock strieks 12','wicked stepmother','wicked witch','Wonder child','year outside, hour inside','you have waited long enough','youngest child wins']
    
    let faction = searchArray(factionArray)
    let othertropes = `Action: ${searchArray(actionTropes)}, Crime: ${searchArray(crimeTropes)}, Drama: ${searchArray(dramaTropes)}, Espionage: ${searchArray(espionageTropes)}.`
    let output = `Theme: ${searchArray(themeArray)}; Goal: ${searchArray(goalArray)}; Reward: ${searchArray(rewardArray)}; Faction: ${faction}; Fantasy Tropes: ${searchArray(fairyTaleTropes) +', '+ searchArray(fairyTaleTropes) +', '+searchArray(fairyTaleTropes) +', '+searchArray(fairyTaleTropes) +', '+searchArray(fairyTaleTropes)}} ${othertropes}`
    document.getElementById("Quest").innerHTML = output 
}



function dungeonCreator() {
    let cityEvent  = ['Riot', 'Siege', 'Cult Gains Influence','Factions are Figthing', 'Wizard tower explodes', 'Royal Precession','Seasonal Celebration','Alarms are ringing','Alchemist paying for reagent retrieval','Exotic goods shipment arrives','Major heist is underway','Wizard college holding annual trials','Execution at dawn','Bounties posted everywhere','Serial killer stalking the streets','City watch is aggressively searching','Revolutionary sentiment spreading','Tournament is being announced','Travelling carnival','People are dissapearing'] 
    let dungeonEvents = ['NPC driven mad','Blocked passage','Terrifying soudns ahead','hostages begging for help','Enemy surprise','unexpected Ally','Suspicious NPC asking for help','Magical lures','bloody steps gettign fresher','slime runs down the wall','vulnerable enemy','time and space anomalies','disgusting smells','door slamming','doors slowly closing ahead','lights ahead','chanting in the distance','shadows begin to stir','enemy taunts form shadows','lumberign steps approach']
    let inhabitants = ['humans','beasts','humaniods','dragon','monster','undead','demonms','giant beast','swarm','cult','bandits','necromancer','assasins','giants','devils','golems','celestials','deity','abandoned']
    let objective = ['capture','collect','purge','raid','ritual','destroy','guard','revive','discover','hide','worship','grow','deliver','ransom','repair','forge','purify','corrupt','sacrifice','summon','kill','rescue','escape','stop','clear','find','return','defend','investigate','chase','infiltrate','survive','escort','map','recover','negotiate']
    let rooms = ['pit','chambers','great hall','maze','stairs','armory','dining','shrine','mine shaft','prison','courtyard','crypt','forge','cavern','fountain','laboratory','vault','workshop','stables','throne room']
    let setting = ['castle','cave','dungeon','grotto','hive','lair','mansion','maz','mine','monastery','necropolis','prison','ruins','sanctum','sewer','temple','tomb','tower','vault','woods']
    let theme = ['Ancient','blasphemous','bleak','bruning','corrupted','crystaline','cursed','elemental','flooded','fortified','hallowed','haunted','infested','overgrown','putrid','ruined','sacred','shadowy','tranquil','wild']
    let trapTrigger = ['switch','wire','magic barrier','pressure','light','sound','opening','touch','movement','time','swallow','proximity','breaking','lever','release','weight','closing','breath','temperature','lock']
    let trapEffect = ['charm','curse','alarm','spikes','Acid','Ice','fire','pit','beast','skeletons','net','crumbling','cage','flood','gas','spell','trap door','darts','pendulum','chute']
    let treasures = ['weapon','armor','coins','book','magic item','scroll','ring','cursed item','potion','artifact','spell tome','clue','gemstone','cloak','shield','mask','journal','map','key','nothing']
    let wildEvents = ['abandoned camp','swarm of animals ahead','bandits offer a deal','wounded desperate beast','earthquake','hazardous water crossing','being stalked','armed guards demand tithe','druidic ritual taking place','notorous bounty subject in the area','massive storm blowing in','travelling emrchant offers soemthing','mysterious fog confuses navigation','wildfire closing in','flash flood','mysterious fungi spreadin rapidly','mystical pool luring into the waters','darkness sooner than expected','wildlife is abnormal, mutated','nomadic NPC asks for help']

    let modifyingimagery = ['tavern','map','skull','throwing knives','spiderwebs','flame circle','maze','exit path','sticky floor','trap hole','eldritch tentacles','wine glass','boulder trap','mimic','trap','tripwire','net', 'ghost','shark','vault','moon over mountains','wolf moon','waterfall']
    let modifyingIdeas = ['vines','water','weapons','well', 'runes','lever','secret door','spiderwebs','flood','forge','fog','gas','acid','barrels','armory','cell','chasm','corpse','chest','fire','ice','lava','lock','mold','altar','barricade','aura','blood','book','collapse','cage','chamber','light','gate','stairwell','shrine','passage','pit','plant','rubble', 'supplies','trap','tracks','treasure']


}

function enemyCreator(){
    let asset = ['army','church','clan','cult','deity','government','weapon','wealth','popularity','spies','magic item','hidden identity']
    let method = ['stealth','violence','politics','magic','deceit','minions','chaos','bribery','misdirection','blackmail','fanatacism','manipulation']
    let cultFocus = ['ritual','bodies','drugs','prophecy','demon','old god','location','relic','book','chaos']
    let cultGoal = ['sacrifice','spread','acquire','destroy','summon','curse','consume','corrupt','manipulate','eradicate']
    function dragon() {
        let dragonAge = ['wyrmling','young','juvenile','adult','old','ancient','wyrm','great wyrm']
        let exoticDragon = ['Shadow','gem','faerie','light','force','prismatic','homebrew']
        let dragoncolor = ['black','blue','green','red','white','brass','bronze','copper','silver','gold',`exotic: ${searchArray(exoticDragon)}`] 
        return `Dragon (age: ${searchArray(dragonAge)}, color: ${searchArray(dragoncolor)})`
    }
    let dragonAge = ['wyrmling','young','juvenile','adult','old','ancient','wyrm','great wyrm']
    let exoticDragon = ['Shadow','gem','faerie','light','force','prismatic','homebrew']
    let dragoncolor = ['black','blue','green','red','white','brass','bronze','copper','silver','gold',`exotic: ${searchArray(exoticDragon)}`] 
    let lair = ['cave','tower','throne room','temple','sewers','ship','castle','mountain','mine','catacombs','crypt','church','mansion','spire','shrine','chasm','necropolis','vault','ruins','sanctum']
    let intelligentMonsters = ['werewolf','lich','homunculus','deva','ettin','hag','troll','vampire','manticore','ghost','imp','wight','aboleth','pegasus',dragon(),'djinni','mephit','nightmare','devil','succubus','giant','ogre','drow','incubus','merfolk','centaur','doppleganger','harpy','medusa','minotaur','treant','vampire','wraith',]
    let monsters = ['skeletons','zombie horde','hydra','golem','ettin','wyvern','gargoyle','gelatinous cube','basilisk','giant spider','bear','wolf','elemental','invisible stalker','blink dog','hell hound','behir','chimera','cockatrice','phase spider','owlbear','worg','mimic','shambling mound','shrieker','ooze','swarm','zombie']
    let intelligentMotivation = ['betrayal','conspiracy','desperation','destiny','discovery','faith','fear','genocide','greater good','greed','grief','knowledge','love','power','pride','rebellion','redemption','renown','revenge','rivalry','reproduction','space']
    let beastialMotivation = ['desperation','fear','rivalry','reproduction','space']
    let personality = ['hermit','fanatical','arrogant','jealous','obsessive','mischievous','warm','ambitions','intelligent','stoic','fiery','paranoid','observant','empathetic','unforgiving','egotistic','careless','narcissistic','volatile','pious']

    let villains = ['dark lord','charlatain','dictator','summoner','illusionist','elementalist','priest','necromancer','traitor','thief','ghost','wizard','hidden figure','beast','conquerer','noble','asasin','bandit','crime lord',dragon(),'heir','elemental','giant','knight','doppleganger','politician','advisor','prophet','scholar','demon','royal','alchemist','conman','witch','heretic','cultist','guild leader','undead','giant','deity']
    let villainTraits = ['resistance','weakness','immunity','health leech','reanimation','flying','multi-attack','grows stronger','poison','mind control','armor','exploding','healing','spellcasting','ranged attack','telekinesis','stealth','teleporitng','undead']
    let villainWeakness = ['tunnel vision','fear','dependant','lack of trust','magic','arrogance','addiction','past deeds','element','love','faith','curse','greed','health','bargain','resources','boastful','trust','morality','stubborn'] 
    let modifyingimagery =['blood goblet','magic tree','foor bite','brain','coins','castle forfeit flag','hourglass','flag','werewolf','spirder','nose','dagger','smiling burning man','devil pitchfork','shield with icon','potion','cogs','battering ram','angry mob','royalty on the throne','telepathy','behind bars','circular saw','gravestone','dungeon window','keyring']
    let modifyingIdeas =['erratic','restrained','organized','tough','fey','flight','grappler','hellish','drone','eerie','elemental','empowered','infamous','nervous','meek','zealous','aggressive','ambusher','amorphous','avoidance','berzerk','brave','bound','brute','corrosive','cunning','darkvision','displacer','deceptive','devious','envious','martyr','deranged','sadist','fixated','anger','amphibious','ambush','brave','corrupted','brash','cautious','ethereal','evasion','fanatical','feral','remorseless','intolerant','oppressive','fierce']

}

function worldCreator(){

    let assetMethod = []

    let modifyingimagery =[]
    let modifyingIdeas =[]

}

function characterCreator(){

    let assetMethod = []

    let modifyingimagery =[]
    let modifyingIdeas =[]

}

function miscCreator(){

    let adventureGear = ['compass','waterskin','spyglass','flint & stee','rope & hook','caltrops','oil','lantern','vial','backpack','candle','torch','rations','hourglass','disguise kit','writing kit',`thieve's tools`,'repair kit',`alchemist's kit`,'map']
    let armor =['clothing','padded','leather','studded leather','hide','chain','scale','half-plate','ring mail','chain mail','split','plate','shield','cloak','boots','gloves','helm','ring','amulet','robe']
    let conditons = ['blinded','charmed','confused','deafened','dying','exhausted','frightened','grappled','incapacitated','invisible','paralyzed','petrified','prone','restrained','silenced','sickened','slowed','stunned','surprised','unconscious',]

    let criticalHit = ['knock prone','terrify','amputate','disarm','bnus attack','flurry','armor break','rend','stun','triple damage','bonus move','inspire allies','hit multiple','advantage','drops item','broken bone','winded','blind','unconscious','decapitation']
    let criticalMiss = ['tripped','drop weapon','hit ally','hit self','blinded','winded','frightened','confused','stunned','stuck','unwanted focus','expose weakness','break weapon','drop item','disadvantage','anger allies','slowed','broken bone','unconscious']
    let curse = ['hostility','death clock','blinded','deaf','necrotic','madness','clumsy','bloodlust','fear','memory loss','feeble','life-drain',`deity's wrath`,'slowed','vertigo','aging',`can't lie`,'bleeding','mute','drunk','pursued','vampirism','lycanthropy','insomnia','hallucinations','disease','luck','exhaustion','disdained','memory','filth','suspicion','dread','possessed','envy','addiciton','hunger','noisy','false sense','ghostly']
    let discovery = ['blight','portal','hideout','sign','presence','lair','map','signs of battle','tracks','ruins','grave','supplies','bones','witness','message','trap','hidden path','source','writings','warnings']
    let items = ['amulet','arrows','axe','belt','boots','bow','book','bracelet','breastplate','brooch','candle','cloak','coin','compass','crown','cup','egg','feather','flute','glove','gem','hammer','har','helm','horn','lute','machiantions','mask','mirror','necklace','net','pack','potion','ring','rope','scepter','shield','skull','sword','wand']
    let magicalMishaps = ['dark vision','sapped energy','memory loss','too much power','lingering trauma','magic fizzles','possessed','physical mark','see dark power','deep sleep','summon fey',' reversed effect','damaged space','terrify witness','destroy item','sickness','summon demon','ominous whisper','']  



    let modifyingimagery =['sword in stone','wooden spike fence','pierced by spear','pawn','magical rings around a person','drinking horn','arrow through the head','power fist','broken arrow','blood recycle','poison bottle','horshoe','mushroom','genie lamp','skull and crossbones','dead trees','bone dagger','bloody sword','broken hatchet','torch','crowning a ruler','butterfly','gem','person frozen in ice','molten metal bucket','stone block','bell ringing','person running with bag of loot','cave entrance','morningstar','wand or staff with gem on top','winged boots','eyeball','four fingered claw','webs','box switch','crystals','arrow in the achilles','sword + lightning','portal gfate','book with skull']
    let modifyingIdeas =['shocking','shining','lucky','charged','banished','unfinished','fake','stolen','mysterious','feral','nightmare','dirty','worthelss','silent','arcane','ornate','damaged','glowing','holy','iron','ancient','cosmic','dwarven','demonic','wild','golden','steel','rotting','evil','tribal','blinding','savage','runic','concealed','flaming','vampiric','bloodthirsty','psychic','chaotic','slimy','heretical','fey','acid','bloody','desolate','awakened','black','incredible','gilded','artisinal','healing','copper','blazing','cunning','blessed','slithering','celestial','scaled','heavy','pristine','jeweled','singing','shadow','light','dark','indestructable','elvish','hidden','rusty','great','frozen','chilling','buried','redeeming','fake','mutated','silver','bleeding','diabolic','inspiring','natural','terrifying','ghostly']

}

function questCreator(){

    let assetMethod = []

    let modifyingimagery =[]
    let modifyingIdeas =[]

}





