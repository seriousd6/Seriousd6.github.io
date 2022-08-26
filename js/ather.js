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
    let output = `Theme: ${searchArray(themeArray)}; Goal: ${searchArray(goalArray)}; Reward: ${searchArray(rewardArray)}; Faction: ${faction}; Fantasy Tropes: ${shuffleSlice(fairyTaleTropes,4)} ${othertropes}`
    document.getElementById("Quest").innerHTML = output 
}






