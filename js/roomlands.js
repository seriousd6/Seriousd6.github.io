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

let cardArrayA10 =  [1,2,3,4,5,6,7,8,9,10]
let cardarray1113 = [11,12,13]
let suitArray = ['C','H','S','D']

//General
    //Character Creation
        //Calling
            let calling = [`There is an army sweeping through the lands around your village. You have heard tales of
            their unstoppable nature; burning villages in their wake, their men clad in monstrous, spiked
            black armour.
            One night they arrive at your village; it is chaos, people screaming, running for their lives,
            the roofs of your people’s huts and tents ablaze, lighting up the night sky. But most terrifying
            of all... Rooks, following their general’s commands, their eyes burning with a purple flame.
            No-one has ever commanded a living Rook before - how is this possible?
            You survive. Maybe you’re left for dead, maybe you hide. Maybe they took someone you
            love, maybe you just want revenge... either way, you will need to get to the bottom of the
            mystery of the Black Army and the Rooks of Purple Flame.`,
            
            `You have a vision as you sleep one night; far across the lands, in a room that looks nothing
            like the room your village resides in, is a tower. The tower looks like it might have been a Rook
            once; thin and impossibly tall with its slender arms by its sides.
            In your vision you see a weapon in a room at the very top of the tower, waiting, calling
            for you. Your village has been besieged by Rooks lately, your hunters are stretched thin.
            Maybe, if you could reach this mythical place, you might be able to save your village?
            
            It flew overhead, casting a shadow black as night in the middle of the day - the Dragon
            Rook, the only Rook known to fly. You hear whispers and rumours of a party heading out to
            hunt it... they say if you can defeat it, you will gain the ability to fly... you can’t let them get
            to it first.`,
            
            `Most villages and peoples living in the Colostle have a passive opinion about the Rooks;
            they are simple wildlife and rarely seen, nothing to be too worried about. But not your
            village. Your village has hated all Rooks ever since one ploughed right through the centre
            of your homes, killing loved ones and disappearing into the night.
            Which is why your secret friendship with a very unusual Rook would not go down well with
            the villagers if they ever were to discover it. You meet your friend in a nearby forest as often
            as you can. It doesn’t talk, but it doesn’t attack; it’s not like other Rooks but you don’t know
            why.
            One day when you pay it a visit, it is gone from its usual place, and there are signs of a
            scuffle and a trail leading off into the distance. You have to go find it.`,
            
            `As a child, your mother used to tell you stories of warriors with diamond
            skin, morphing weapons of magma and obsidian blades that
            never dulled. Their powers came from the Fabled Rookstones; ancient one-of-a-kind stones,
            hundreds of them, made of a different rock, crystal or gem and each holding a unique
            magical power.
            It wasn’t true of course; there are only 3 kinds of Rookstones, Ice, Shock and Rumble, and
            all Rooks have one of these. Everybody knows that.
            But now, as an adult, you know a little more, you’re a little wiser to the world. And you know
            that stories like that don’t exist without a grain of truth. What if the legendary Rookstones
            actually exist?`,
            
            `A map and a key passed down in your family. The map covers a huge area; you can see
            multiple rooms - and you’ve never even seen the edges of your Room! 5 locations are
            marked on it with different coloured glyphs. The locations look like ancient Rook bodies,
            long since fallen, rotting like ancient temples.
            The key is ornate and strange, with a Rook symbol carved into its head. It looks like it would
            fit into a Rook. Maybe those 5 ancient Rook bodies are locked, and only you have the key.
            But what could possibly be hidden within?`,
            
            `You are a member of an order of Knights. Knights have one job: They are highly trained
            and conditioned to take on Rooks and are some of the greatest Rook fighters in all of the
            Colostle. Your superior in your Order has called you into his office, and he has a mission for
            you...`
        ]
            
        //Nature
            let nature = [
                'Happy-go-lucky, extremely optimistic, fun',
                'Impatient, quick-to-anger, grumpy',
                'Brave, by-the-book, serious, no sense of humour',
                'Introspective, quiet, mysterious, person of few words',
                'Larger than life, tells exaggerated stories, roars with laughter',
                'Sly, strategic and always planning',
                'Salt-of-the-earth, common folk, finds it easy to talk with anyone'
            ]
        //Class
        const characterClass = {
            'Armed':{
                'exploration':3,
                'combat':4,
                'description':`The Armed quite literally have an arm from a Rook connected to them via a complex ritual, attuning its intention to them. The Armed are proficient in melee combat and are highly capableadventurers. They are warriors. An Armed adventurer could have any type of arm; a blade, a hand, a cannon, a strange machine the user doesn’t yet understand. If the arm has a hand or the ability to hold items, it can be used to carry an additional weapon if you have one.`,
                'extended description': `The process of bonding with a Rook Arm is known as ‘The Grafting’. Depending on the person’s constitution, the size and weight of the Rook arm, and those who are carrying out the ritual, this process can vary from simple and painless to lengthy and painful. Because of this, Arm users tend to be battle-hardened and tough, chosen to wield an Arm because they are strong enough. Despite the immense toughness of the Armed, wielding an Arm can still take a great toll on them. Sometimes it can hurt because of its weight, or when it lifts something heavy, it tugs against the user’s body. Other times there is a mental weight, a stress in the mind when coercing it to follow command. Arm users can have any number of arms attached to them, limited only by the physical and mental weight they can bear and the size and complexity of the arms they have.
                    Arms come in all shapes and sizes. Some are like human arms with joints and multi-fingered hands; these tend to be the easiest to wield as they challenge the mind in the same way that a human arm does. But some arms are strange or very different; like coiling segmented plates that flow like a snake, or spidery multi-jointed arrangements that split and separate. Some arms can be big and bulky enough to lift the user off the ground or carry incredibly heavy weights. Others allow users to do fine detailed work that they could never normally do with their human hands. 
                    Some Arm users claim to see messages or hallucinations, believed to be the memories of the Rook the arm came from. A complex meditation ritual involving exotic herbs and roots can allow an Arm user to see these memories more clearly and try to understand the Rooks and their purposes better. The images are always hazy and vague but there is a very real sense of a semblance of sentience even though it is generally thought that they are just machines and only Rooklings have sentience.`,
                'trait prompts': ['Are you a hunter who felled their first Rook and wish to wear the arm as a trophy?', 'Does your village or clan fit Rook arms to their children to equip them for the harsh life of living in the Colostle?', 'Did you lose a limb of your own in a battle when young and have the Rook limb fitted as a replacement?', 'Is the Rook arm a family heirloom passed down your family line when the previous owner falls in battle? Are you the latest to claim it, or is there something you must do first before you are worthy?', 'Is your Arm a question of status? Do others in your tribe have larger, more ornate Arms, and is it important to your character to compete or not?', 'Are you the first in your family/clan/village to wield an Arm?']
            },

            'Followed':{
                'exploration':5,
                'combat':3,
                'description':`he Followed have a small Rook companion, like a pet or familiar that follows them and their commands. These ‘Rooklings’ are found in the cores of larger Rooks - as yet it is not known why. They display a base level of sentience akin to that of a dog or a cat and can form deep and personal bonds with their human companions. The Followed are excellent rangers, pathfinders and navigators.`,
                'extended description':`The Followed are usually very capable explorers, proficient in tracking, survival and navigation, and combined with their Rookling companions (who often have a sense of direction and knowledge about the world) they are more equipped than most to navigate the lands of the Colostle. 
                    Rooklings can vary in size from very small (the size of a kitten) to the size of a person. A Rookling will have the body and magic characteristics of the large Rook it was harvested from. To create your first Rookling, head to the ‘Creating your Opponent - Rooks’ section in the combat rules to either choose the body and magic characteristics, or draw cards to create them randomly. No two Rooklings look alike, just like the Rooks they come from, and many of them can be very strange shapes. The only consistent characteristic across them all is that they are made of stone, and seem to feature castle elements but on a much smaller scale; such as doors, windows, crenellations, tiny balconies, drawbridges, and sometimes even tiny gardens in miniature courtyards jutting out of the sides of their bodies.
                    Fighting with Rooklings involves fighting in a partnership with your companion. Your character will have a weapon in their hands, but when you do an UNARMED or MAGIC attack this might be a moment where you command your Rookling to fight, or use its magic! Maybe it has ice powers, or the ability to roll into a ball and smash into its opponents. Maybe it can climb inside an enemy Rook and do damage from within, or maybe it can throw you high into the air to bring a weapon attack down on an enemy; the only limit is your imagination!
                    When fighting with your Rookling companion, think about what it is about your partnership that makes you skilled Rook hunters. Maybe you even have some special moves that you can do together due to a convenient combination of specialities!`,
                'trait prompts': ['Does your village or clan hate the Rooks, and did you have to keep your bond with a Rookling secret?',
                'Is your Rookling the core of a Rook that killed someone close to your character?',
                'Is your bond with your Rookling a reluctant one; does it follow, but you wish it didn’t? ',
                'Does your Rookling have something special about it? A strange crest or a hand that looks like a key?',
                'Think about your Rooklings shape, abilities and how it would fight in combat. With these things considered it will make it easier to come up with strategies in battle!']
            },

            'Helmed':{
                'exploration':2,
                'combat':5,
                'description':`The Helmed harvest a piece of strange machinery from the very core of a Rook and, using rituals and a real working understanding of the crystal patterns and stones, they are able to create a Helm that can be worn and operated, granting them the magical abilities of the Rook it was harvested from.`,
                'extended description':`The Helmed are the closest to wizards or alchemists in the world of Colostle. Understanding the magical properties of Rooks and how to harness them is partly a pursuit of arcane knowledge and also one of logic and crystal-engineering, like magical circuitry.  
                    Any human-made devices that use Rookstones, like lanterns or refrigeration chambers, are made by the Helmed, or someone who would be a great candidate for a Helm.
                    This knack for Rook alchemy is rare and even if it manifests in someone, there is then the added challenge of defeating a Rook to obtain the part or parts usable to create a Helm.
                    However, once done, unlike the Arm which requires attunement and a great toll on the body, the use of a Helm is purely operative, there is no attunement required. It is, however, complex and a deep understanding is required.
                    The Helmeds skills are the most sought after in society. Manipulating and understanding the magical ‘technology’ of the Rooks allows people luxuries beyond the reach of human technology. This can mean one of two things for the Helmed, they are either venerated, or enslaved, depending on the nature of the person who comes across them.
                    Others still consider the Helmed to be Rook sympathizers or ‘witches’. They are thought to be brainwashed with a Rooks thoughts infecting and affecting their own, as such they are often driven out of smaller settlements and distrusted in larger ones. Some religious zealots consider the use of the Rookstone magic to be heresy; consorting with the monsters that threaten everyday life for people. These people consider the Helmed to be the very worst heretics.`,
                'trait prompts': [
                    'Has your character always had an understanding of Rooks since they were young? And if so, how did they first discover that?',
                    'Does your character respect the Rooks, or simply see them as a source for scrap to tinker with?',
                    'Is your character more comfortable in their workshop, dissecting and assembling, and is therefore reluctant to head out on a grand quest or journey?',
                    'Is your character surrounded by brave warrior Armed or strategic ranger Followed, and feeling a need to prove their worth in their village or clan?',
                    'Is your character driven to understand the mechanisms and technology of the Rooks and the Colostle as a whole?']
            },

            'Mounted':{
                'exploration':5,
                'combat':2,
                'description':`The Mounted ride an adapted mechanism taken from Rook parts, as a vehicle or mount to allow them easier traversal across the land and sea of the Colostle. Typically this involves taking a part of the Rook responsible for it’s locomotion and disconnecting it from the main body, and turning it into something that can be operated with crude controls, mechanisms and levers. The Mounted’s mounts can vary from horse-like creatures to boats and even bikes.`,
                'extended description':`Like the Helmed, the Mounted are gifted Rooksmiths, with a basic understanding of their functionality. But unlike the Helmed who have an understanding of the magical circuitry and therefore magical abilities of a Rook, the Mounted have a mechanical one.
                The Mounted are nomads and scavengers, constantly on the hunt for felled or ancient decaying Rooks and harvesting parts for their own mount. Partly to upgrade, and partly to just keep it going, as mounts require constant maintenance, like off-road vehicles. A Mounted’s mount is their heart and their life. Like looking after a bike or a beloved car, it is everything, it is their freedom. 
                When you defeat a Rook or come across a husk out in the wilds, your character can take parts to upgrade or add to the functionality of your mount. This functions as a story opportunity for your character. Perhaps you took damage in your last battle and you take pieces from a fallen Rook to repair it. Maybe where once there were wheels, you attach legs in their place.
                Individual parts of Rooks seem to function on their own. If you remove a spinning wheel from the core of a Rook it will continue to spin on it’s own. If you take a leg mechanism; it will still have power despite being disconnected. This means any part that isn’t completely smashed to splinters can be made useful to a Mounted.
                Mounted are capable of battling Rooks and do so using the Mount’s built in Weapons (for example a cannon or a battering ram). In COMBAT, if you draw a WEAPON attack you can use your Mount’s weapon or one that your character carries in their hands.
                The Mounted have a low starting COMBAT score but as you explore more you will find ways to increase that score. Don’t see this as a limitation. Instead, it is a storytelling opportunity to have your character go on an adventure of growth.`,
                'trait prompts': [
                    'Do you come from a village of Mounted, with buildings and encampments made of mechanical parts of Rooks? Being Mounted is in your blood?',
                    'Come up with what your mount looks like and what Weapon it has on board to help defend you on your adventures.',
                    'Perhaps your nomadic tribe is running out of Rook parts, your lands no longer as fertile for living and fallen Rooks as before. Maybe you must travel further afield to find new lands, rich in broken mechanical parts to scavenge. ',
                    'Maybe your father is famous in the tribe for his mechanical adeptness and warrior’s spirit. You live in his shadow, keen to prove you have what it takes to carry on the family name.',
                    'One day when scavenging a Rook husk you come across a part unlike any seen before. It could change how your mount functions dramatically. What would the others think if they saw it though, would they try to take it from you?']
            },


            }
        //Weapon
    //TBA Jobs
    

//Exploration

//combat

