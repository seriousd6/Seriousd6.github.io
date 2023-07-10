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
            'description':
                `The Armed quite literally have an arm from a Rook connected to them via a complex ritual, attuning its intention to them. The Armed are proficient in melee combat and are highly capableadventurers. They are warriors. An Armed adventurer could have any type of arm; a blade, a hand, a cannon, a strange machine the user doesn’t yet understand. If the arm has a hand or the ability to hold items, it can be used to carry an additional weapon if you have one.`,
            'extended description': 
                `The process of bonding with a Rook Arm is known as ‘The Grafting’. Depending on the person’s constitution, the size and weight of the Rook arm, and those who are carrying out the ritual, this process can vary from simple and painless to lengthy and painful. Because of this, Arm users tend to be battle-hardened and tough, chosen to wield an Arm because they are strong enough. Despite the immense toughness of the Armed, wielding an Arm can still take a great toll on them. Sometimes it can hurt because of its weight, or when it lifts something heavy, it tugs against the user’s body. Other times there is a mental weight, a stress in the mind when coercing it to follow command. Arm users can have any number of arms attached to them, limited only by the physical and mental weight they can bear and the size and complexity of the arms they have. Arms come in all shapes and sizes. Some are like human arms with joints and multi-fingered hands; these tend to be the easiest to wield as they challenge the mind in the same way that a human arm does. But some arms are strange or very different; like coiling segmented plates that flow like a snake, or spidery multi-jointed arrangements that split and separate. Some arms can be big and bulky enough to lift the user off the ground or carry incredibly heavy weights. Others allow users to do fine detailed work that they could never normally do with their human hands. Some Arm users claim to see messages or hallucinations, believed to be the memories of the Rook the arm came from. A complex meditation ritual involving exotic herbs and roots can allow an Arm user to see these memories more clearly and try to understand the Rooks and their purposes better. The images are always hazy and vague but there is a very real sense of a semblance of sentience even though it is generally thought that they are just machines and only Rooklings have sentience.`,
            'trait prompts': ['Are you a hunter who felled their first Rook and wish to wear the arm as a trophy?', 'Does your village or clan fit Rook arms to their children to equip them for the harsh life of living in the Colostle?', 'Did you lose a limb of your own in a battle when young and have the Rook limb fitted as a replacement?', 'Is the Rook arm a family heirloom passed down your family line when the previous owner falls in battle? Are you the latest to claim it, or is there something you must do first before you are worthy?', 'Is your Arm a question of status? Do others in your tribe have larger, more ornate Arms, and is it important to your character to compete or not?', 'Are you the first in your family/clan/village to wield an Arm?']
        },

        'Followed':{
            'exploration':5,
            'combat':3,
            'description':
                `The Followed have a small Rook companion, like a pet or familiar that follows them and their commands. These ‘Rooklings’ are found in the cores of larger Rooks - as yet it is not known why. They display a base level of sentience akin to that of a dog or a cat and can form deep and personal bonds with their human companions. The Followed are excellent rangers, pathfinders and navigators.`,
            'extended description':
                `The Followed are usually very capable explorers, proficient in tracking, survival and navigation, and combined with their Rookling companions (who often have a sense of direction and knowledge about the world) they are more equipped than most to navigate the lands of the Colostle. Rooklings can vary in size from very small (the size of a kitten) to the size of a person. A Rookling will have the body and magic characteristics of the large Rook it was harvested from. To create your first Rookling, head to the ‘Creating your Opponent - Rooks’ section in the combat rules to either choose the body and magic characteristics, or draw cards to create them randomly. No two Rooklings look alike, just like the Rooks they come from, and many of them can be very strange shapes. The only consistent characteristic across them all is that they are made of stone, and seem to feature castle elements but on a much smaller scale; such as doors, windows, crenellations, tiny balconies, drawbridges, and sometimes even tiny gardens in miniature courtyards jutting out of the sides of their bodies. Fighting with Rooklings involves fighting in a partnership with your companion. Your character will have a weapon in their hands, but when you do an UNARMED or MAGIC attack this might be a moment where you command your Rookling to fight, or use its magic! Maybe it has ice powers, or the ability to roll into a ball and smash into its opponents. Maybe it can climb inside an enemy Rook and do damage from within, or maybe it can throw you high into the air to bring a weapon attack down on an enemy; the only limit is your imagination! When fighting with your Rookling companion, think about what it is about your partnership that makes you skilled Rook hunters. Maybe you even have some special moves that you can do together due to a convenient combination of specialities!`,
            'trait prompts': ['Does your village or clan hate the Rooks, and did you have to keep your bond with a Rookling secret?',
            'Is your Rookling the core of a Rook that killed someone close to your character?',
            'Is your bond with your Rookling a reluctant one; does it follow, but you wish it didn’t? ',
            'Does your Rookling have something special about it? A strange crest or a hand that looks like a key?',
            'Think about your Rooklings shape, abilities and how it would fight in combat. With these things considered it will make it easier to come up with strategies in battle!']
        },

        'Helmed':{
            'exploration':2,
            'combat':5,
            'description':
                `The Helmed harvest a piece of strange machinery from the very core of a Rook and, using rituals and a real working understanding of the crystal patterns and stones, they are able to create a Helm that can be worn and operated, granting them the magical abilities of the Rook it was harvested from.`,
            'extended description':
                `The Helmed are the closest to wizards or alchemists in the world of Colostle. Understanding the magical properties of Rooks and how to harness them is partly a pursuit of arcane knowledge and also one of logic and crystal-engineering, like magical circuitry. Any human-made devices that use Rookstones, like lanterns or refrigeration chambers, are made by the Helmed, or someone who would be a great candidate for a Helm. This knack for Rook alchemy is rare and even if it manifests in someone, there is then the added challenge of defeating a Rook to obtain the part or parts usable to create a Helm. However, once done, unlike the Arm which requires attunement and a great toll on the body, the use of a Helm is purely operative, there is no attunement required. It is, however, complex and a deep understanding is required. The Helmeds skills are the most sought after in society. Manipulating and understanding the magical ‘technology’ of the Rooks allows people luxuries beyond the reach of human technology. This can mean one of two things for the Helmed, they are either venerated, or enslaved, depending on the nature of the person who comes across them. Others still consider the Helmed to be Rook sympathizers or ‘witches’. They are thought to be brainwashed with a Rooks thoughts infecting and affecting their own, as such they are often driven out of smaller settlements and distrusted in larger ones. Some religious zealots consider the use of the Rookstone magic to be heresy; consorting with the monsters that threaten everyday life for people. These people consider the Helmed to be the very worst heretics.`,
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
            'description':
                `The Mounted ride an adapted mechanism taken from Rook parts, as a vehicle or mount to allow them easier traversal across the land and sea of the Colostle. Typically this involves taking a part of the Rook responsible for it’s locomotion and disconnecting it from the main body, and turning it into something that can be operated with crude controls, mechanisms and levers. The Mounted’s mounts can vary from horse-like creatures to boats and even bikes.`,
            'extended description':
                `Like the Helmed, the Mounted are gifted Rooksmiths, with a basic understanding of their functionality. But unlike the Helmed who have an understanding of the magical circuitry and therefore magical abilities of a Rook, the Mounted have a mechanical one. The Mounted are nomads and scavengers, constantly on the hunt for felled or ancient decaying Rooks and harvesting parts for their own mount. Partly to upgrade, and partly to just keep it going, as mounts require constant maintenance, like off-road vehicles. A Mounted’s mount is their heart and their life. Like looking after a bike or a beloved car, it is everything, it is their freedom. When you defeat a Rook or come across a husk out in the wilds, your character can take parts to upgrade or add to the functionality of your mount. This functions as a story opportunity for your character. Perhaps you took damage in your last battle and you take pieces from a fallen Rook to repair it. Maybe where once there were wheels, you attach legs in their place. Individual parts of Rooks seem to function on their own. If you remove a spinning wheel from the core of a Rook it will continue to spin on it’s own. If you take a leg mechanism; it will still have power despite being disconnected. This means any part that isn’t completely smashed to splinters can be made useful to a Mounted. Mounted are capable of battling Rooks and do so using the Mount’s built in Weapons (for example a cannon or a battering ram). In COMBAT, if you draw a WEAPON attack you can use your Mount’s weapon or one that your character carries in their hands. The Mounted have a low starting COMBAT score but as you explore more you will find ways to increase that score. Don’t see this as a limitation. Instead, it is a storytelling opportunity to have your character go on an adventure of growth.`,
            'trait prompts': [
                'Do you come from a village of Mounted, with buildings and encampments made of mechanical parts of Rooks? Being Mounted is in your blood?',
                'Come up with what your mount looks like and what Weapon it has on board to help defend you on your adventures.',
                'Perhaps your nomadic tribe is running out of Rook parts, your lands no longer as fertile for living and fallen Rooks as before. Maybe you must travel further afield to find new lands, rich in broken mechanical parts to scavenge. ',
                'Maybe your father is famous in the tribe for his mechanical adeptness and warrior’s spirit. You live in his shadow, keen to prove you have what it takes to carry on the family name.',
                'One day when scavenging a Rook husk you come across a part unlike any seen before. It could change how your mount functions dramatically. What would the others think if they saw it though, would they try to take it from you?']
        },

    }
    let specialClass ={
        'Within': {
            'exploration':5,
            'combat':6,
            'description':
                `Those that take on the incredibly powerful Astrolithic Rooks and win are experienced, mythic warriors. And their reward is an opportunity to become Within. For with a little careful manipulation it is possible to climb into a defeated Astrolithic Rook and pilot it; like a huge stone suit of armour. However, not only are Astrolithic Rooks incredibly powerful with grand new weaponry never seen in the Rooms below... but they can fly.`,
            'extended description':
                `Easily the most powerful class; ‘Within’ is a status that is earned and is never the start of your character’s journey. Especially considering that the only way to attain a Rooksuit is by making it to the rooftops and slaying an Astrolithic Rook. All ‘Within’ start life as a different class - and when piloting their Rooksuit it acts as a temporary upgrade until they elect to leave it for some reason. While ‘Within’, a player has a few options available to them: Firstly they can fly. They can use this ability to fast travel across the battlements, or reenter the Rooms below and fly across those lands. On top of that the combat stats for a Within are immensely high, making you nearly unstoppable against other Rooks. Being Within means you are not subject to Astrolithic Rook attacks whilst within the Rooksuit. The instant you leave the suit, the Astrolithics may notice you again. You have attacks: (LASER ATTACK The Rook seems to charge some kind of glass or crystal emitter and then suddenly a blast of white heat flashes from the end and hurtles towards your character in a straight line | FLYING ATTACK The Rook swoops out of range of your attacks only to swing around in the air and lash out at you as it flies back. | GRAB ATTACK A stone hand unfolds from a hidden location and grabs you, at the same time, the Rook hurtles into the sky carrying you upward. A fall from this height could really hurt! | ROCKET ATTACK The Rook disconnects a part of itself, perhaps one of its arms or a small turret and it blasts towards you with the same propulsion as the Rook has itself for flight. Your character braces as the stone missile streaks toward you...) piloting an Astrolithic Rook. 
                When writing your Within character think carefully about what this means for your character’s story. It could be considered an end, your warrior/adventurer reaching the zenith of legend; the highest power of all. Or perhaps this power changes your character somewhat; for good or for bad. Or you could continue your journey; now as a near invincible hero and your story could introduce moments of peril by being separated from your Rooksuit or having it stolen from you. The Within is intended as the peak of your potential rewards; a gift to a player so that there is something at the end of the adventure to aspire to. But just imagine how the other characters you have met might react to seeing you in a Rooksuit - or what it might mean for advancing the story of your character’s Calling.`
        }
            
    }

    //TBA Jobs
 
/*****GENERAL*****/
    //Supplements:
    function pickClass(){
        return searchArray(Object.keys(characterClass))
    }
    let items = [
        'one valuable treasure','a cache of supplies','a critical piece of information','a cache of materials to create a potion to heal one wound','a mysterious key',`a ${searchArray(['salvagable','working'])} vehicle`,'a tame animal','a potion','an interesting machine part','a revealing map','a new weapon',`an intricate ${searchArray(['artifact','idol'])}`,'two valuable treasures'
    ]
    let situations = [
        'you meet a friend.','a storm rolls in.','something falls from the `ceiling`.','you fall.','a loud noise can be   heard.','a strange feeling comes over you.','the sun sets or rises.','a fire breaks out.','somethign breaks.','your way is blocked.','you are surrounded.','hunger sets in.','you create or repair something.'
    ]
    let generalEvents = [
        /*Organic (Hearts/Diamonds)*/
        [
            `${searchArray(['An armed','An unarmed'])} stranger in unusual robes with a castle symbol on them. Perhaps ${searchArray(['he','she'])} has clues about the nature of the Colostle, but these strangers are often unwilling to even be found, let alone be spoken to. You’ve heard tell of them before - a cult maybe? People don’t talk about them kindly; strangers with strange practices... but they definitely know something. If you fight them, create a human opponent in your COMBAT phase.`,
            `An Animal to hunt for food. This animal is ${searchArray(['easy prey','dangerous'])} The animals in the wilds are strange and unfamiliar; weird combinations of animals you might know, a boar with scales, or a fowl with 2 sets of wings. Adventuring is hungry work, you should make time to eat.`,
            `CALLING - You come across ${searchArray(['a friendly','an unfriendly'])} ${searchArray(['man','woman','boy','girl'])}  who is key to your CALLING. Maybe they have a clue about what you’re looking for, or they block your way to learning more...`,
            `${searchArray(['A trustworthy','An untrustworthy'])} ${searchArray(['man','woman','boy','girl'])} you meet asks you to find something for them. Maybe they have lost something, or they are too afraid to get it. They will reward you with a ${searchArray(items)} if you do this for them. Use the other cards drawn in this EXPLORATION phase to inform where you might need to go. If you fight them, create a human opponent in your COMBAT phase.`,
            `A dead body of a ${searchArray(['man','woman','boy','girl'])}. Who are they? What are they wearing? ${searchArray([`Things seem safe, and if the body is searched you find a ${searchArray(items)}`,`Something seems off, and if you stick around too long, ${searchArray(situations)}`])}`,
            `Another adventurer like yourself, they seem ${searchArray(['friendly','unfriendly'])}, and are garbed in Rook Armour and seem to be a ${pickClass()}. But what do they want? Are they here to help you take down a Rook? If so what do they want in return? Or are their intentions darker? If you fight them, create a human opponent in your COMBAT phase.`,
            `A screech from the sky, the beat of heavy wings... gargoyles. You thought they were just stories you were told as a child. Apparently not! It grabs you by the shoulders and starts to carry you upward. ${searchArray(['It takes you to a whole new area.','It takes you up to its nest in the rafters of the ceiling. There is no fighting a Gargoyle...'])}`,
            `You come across a small settlement, maybe a farming village, the buildings are all wooden and skins, like most small settlements. ${searchArray([`${searchArray(items)} can be found here.`, `While you are here, ${searchArray(situations)}`])}`,
            `A massive skeleton. ‘It looks humanoid. But it can’t be, can it?’ ${searchArray('Getting closer you can see that it is safe',`${searchArray([`You go unnoticed despite finding out it is a bandit camp.`,'You get close enough to see it is bandit camp, just when you realize that, you are captured.'])} It’s a camp of people. At least, they look like people; they walk on 2 legs and carry tools in 2 arms, but they’re not.... human. Who are they? What do they want?`)}`,
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`
        ],
        /*Inorganic*/
        [
            `A large treasure. Maybe a chest or a valuable golden object, perched atop an altar, ${searchArray(['it seems completely untouched','there is evidence of attempted raids'])}. Whatever it is, it fills you with hope for your adventure. Add 1 point to either your EXPLORATION or COMBAT scores and come up with a unique item for your inventory.`,
            `A door. No ordinary door - a door between Rooms in the Colostle; it’s impossible, huge beyond imagining, disappearing upward into the sky. If you hadn’t seen it from a distance, you’d have thought it was just another wall. ${searchArray(['The door is ruined, you may be able to slip through a gap',`it is ${searchArray(['intact but unlocked, so you might have to find a mechanism to open it', 'intact and locked, so you might have to find a mechanism to unlock it, and then open it.'])}`])}`,
            `${searchArray(['An intact','A ruined'])} staircase leading to another floor in the Colostle. Massive - and a quest in itself to climb - it vanishes into mist and clouds. Each step is the height of a small house - who could have possibly built this? If this is not the first staircase you have come across, you can consult the BATTLEMENTS module to take you to the Colostle Rooftops. If it is the first staircase you have found, it takes you to another floor of the Colostle.`,
            `Ruins, ${searchArray(['somewhat intact','mostly rubble'])}, of a people you’ve never heard of. The unfamiliar inscriptions and architecture suggest these people lived a very long time ago. While you are here, ${searchArray(situations)}`,
            `A great, strange mechanism that seems to operate something in the Colostle. Pipes, gearwheels and levers; it seems oversized but you think you can operate it. ${searchArray(['It seems functional','It seems damaged,  maybe you need to find something to repair it?'])}`,
            `A trap! ${searchArray(['You avoid it!','You are caught in it!'])} Maybe a hunters trap, or a pit, or some old machinery. What do you do now?`,
            `A cave entrance. A darkness beckons beyond. Could it lead to deeper parts of the Colostle itself? ${searchArray(['It is flat and easily navigable.','It looks deep and hard to climb into.'])}`,
            `The sea. A huge expanse of water stretches out before you ${searchArray([', serene and welcoming',', stormy and tempestuous'])}. You stand on a rocky coast, or a beach, looking out. The water stretches to the horizon but beyond it you can see the tell-tale columns and ceiling supports of the Colostle; it’s all still within a room. If you don’t want to use the expansion module, consider this a coastal region of cliffs and beaches. Otherwise, consult the OCEANS module to explore the SEA!`,
            `CALLING - You come across a place that is key to your CALLING. ${searchArray(['You find a building with a clue in it!','You find one of the locations you were looking for on your quest!'])}`,
            `You come across ${searchArray(['a thriving city; here you see motorised vehicles and mechanisms seemingly on every corner, and best of all, shops, culture, and hunters; a place of commerce, trade and meeting!','an abandoned city. It was either destroyed or the people left, all that remains is the overgrown bones of a once large community and the rook corpses used to defend it.'])}`,
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`
        ]
    ]

    //Exploration    
    function generalExploration(){
        if (rollDice(100) > 50){
            return searchArray(generalEvents[0])
        } else {
            return searchArray(generalEvents[1])
        }
    }

/*****OCEAN*****/
    //Supplements
    let weather = [
        `SUNSHINE - Add one to your EXPLORATION or COMBAT score.`,
        `STRONG WINDS - a good wind takes your boat where you want to go, quickly.`,
        `FOG - Visibility is reduced to 2 feet in front of you. It is unnervingly quiet.`,
        `HEAVY RAIN - No shelter, it pelts against your skin. You’ll just have to sail on.`,
        `CALM - no winds, baking heat. You will be stuck in the middle of the sea with no way to move for 24 hours.`,
        `CROSSWIND - You are blown off course and are lost at sea for 24 hours.`,
        `SNOW - Small flakes settle on your boat, this is going to get cold...`,
        `WATERSPOUT - A column of water twirling with wind, it's heading toward you!`,
        `STORM - Your boat is tossed by huge waves and heavy winds.`,
        `LIGHTNING - Forks of lightning light up the sky, the sea churns with malice.`,
        `ICE - The ocean freezes instantly around your boat. You are stuck for 24 hours.`,
        `TSUNAMI - A huge wave looms above your boat. Can you ride it out or will it smash your boat to pieces?`,
        `MAELSTROM - your boat is damaged and you wake up stranded on a new island. Return to base book Encounter tables for your next EXPLORATION Phase.`
    ]
    //Exploration
    let oceanEvents = [
            /*Organic (Hearts/Diamonds)*/
            [
                `A single castle tower sticks up out of the water, waves splashing around where it connects with the sea.${searchArray(['It seems uninhabited.','You hear voices from deep within.'])} There is a doorway that is accessible from the height of the sea, and when you look down into the interior you are stunned to see that it goes deep down into an underwater complex, completely airtight from the sea around it. WEATHER: ${searchArray(weather)}.`,
                `Another seagoing adventurer in their own vessel. ${searchArray(['They seem friendly.','They seem unfriendly.'])} WEATHER: ${searchArray(weather)}`,
                `Shipwreck. You pull up alongside the ${searchArray([`mostly intact vessel and find ${searchArray(items)} and ${searchArray(items)}`,`the completeley wrecked vessel and find ${searchArray(items)} floating among the debris`])}`,
                `An island with the tell-tale crenellations of a castle around its perimeter. Could it be that you are seeing just the very top of a huge Rook below the waves? ${searchArray(['The rook is dead.',`the rook's traps are still active!`])}`,
                `A huge seagoing creature is swimming just below the surface. Maybe its leading you somewhere, maybe you could hunt it for food? ${searchArray(['It swims past your vessel with no issue.','It hits your vessel as it passes!'])} WEATHER: ${searchArray(weather)}`,
                `Sea cave, large enough for your vessel to enter. It’s huge, cavernous within, like an underground river leading from one cavern to the next. ${searchArray([`It is inhabited and the ${searchArray(['friendly','unfriendly'])} creatures you meet are not human`, `It is uninhabited and you find ${searchArray(items)}`])}`,
                `A pirate ship! The pirates lasso your ship and bring you aboard. This is not a time to fight - you must sneak out and escape the pirate ship! Tell your story of how you navigate the halls and decks of the pirate ship and ${searchArray([`how you find the treasure`,`how you find the weapon`])} that you take back with you.`,
                `Shallow waters and underwater ruins. If the weather is good, you could drop anchor and swim down to investigate...${searchArray(['Finding rook parts','finding treasure'])} should you be able to venture into the deeps.`,
                `A small island. ${generalExploration()}. That is all there is to find here, return to the SEA to continue. WEATHER: ${searchArray(weather)}`,
                `A coastline. If you decide to disembark here then return to the base rulebook for ongoing EXPLORATION phases. WEATHER: ${searchArray(weather)}`,
                `You found an island with ${searchArray(items)}!`,
                `You found A Medium Rook!`,
                `You found A Massive Rook!`
            ],
    ]
    function oceanExploration(){
        return searchArray(oceanEvents)
    }

/*****CITY*****/
    //Supplements
    let rooklings = [
        `A spidery one with 6 legs`,
        `A ball-shaped one that rolls`,
        `A telescopic one that extends and retracts`,
        `One with a large glowing eye`,
        `A speedy wheeled one`,
        `A friendly and loving one`,
        `One with powerful spring-like legs`,
        `It walks on 4 legs like a dog`,
        `One that splits into 3 parts`,
        `A mean looking one bristling with blades`,
        `One that magically floats in the air beside you`,
        `One with a mysterious door in its front`,
        `One that emits garbled speech from time to time.`
    ]
    let cityBasics ={
        'staples': {
            'Hunters Guild':
                `You can decide
                to accept quests and head out to complete the requirements, or you can turn it down and ask for another. This is as simple as going through the process again and seeing what you get a second time. Consider using the quests you DON’T take on as more aspects to your story. Other things are happening out in the world and maybe they can tie in to your character’s overall adventure.`,
            'Tavern' : 
                `Colostle operates on a bartering system of commerce, you can trade any item you have found on your travels for a night’s stay at the Tavern. This stay will grant your player +1 to either your COMBAT or EXPLORATION scores. You can only do this ONCE per visit to the city. You will have to spend at least one EXPLORATION phase outside of the city before being able to use the Tavern again. The Tavern is also a great place to meet people and talk to strangers, and hear rumours and ask about any jobs that are needed. Once per visit to the Tavern you can ask a stranger for a quest and use the Quest Generation system from the Hunter’s Guild section to create one. Then when complete you will need to return to the Tavern for your reward.`,
            'Merchant':
                `The Merchant is an interesting character found in their shop in the city streets. For a variety of different prices (see each item) all manner of strange devices, weapons and supplies can be purchased. Some of them are single use - others are pieces of equipment you can equip:
                GLIDER - Neat unfolding glider structure stored on your character’s back that allows you to glide from heights. PRICE: 3 Treasures
                WEATHERSTONE - A mysterious stone that summons (${searchArray(weather)}). it will always generate. Can be used once per EXPLORATION phase. PRICE - Any 5 items
                TURTLE SHELL ARMOUR - Stone Rook Armour in the shape of a turtle shell. Will block one wound of damage each COMBAT phase. PRICE - 5 Treasures
                TRIPWIRE LAUNCHER - A crossbow-like device that launches 2 pins with a chain between them. When aimed correctly this can trip up a Rook. PRICE - 4 items
                ROOK GAUNTLETS - Huge stone Rook hands that fit over your hands and allow you to punch with the power of a Rook. PRICE - Any 1 item
                EXTENDING POLE - Telescopic pole made from Rook parts. Allows you to vault upward and also attack from a distance PRICE - Any 3 items
                ELECTRIC SWORD - A Rook great sword imbued with Electric magic. PRICE - 1 Treasure`,
            'Housing District':
                `The Housing District is where the populace of the city live and is a great place for your story to develop if you need to meet a contact, stay with family or friends, or get some information. The district mostly consists of Rook husks piled on top of one another to create something akin to an apartment block. Makeshift ladders and crude stairways clamber over lower houses to reach upper ones and here-and-there old Rook arms form bridges and washing lines. Between the houses; wandering the various walkways and corridors are vendors selling food door-to-door, mysterious cultists going about their shady business trying to recruit new members, and the residents themselves, gossiping or visiting friends. It is a vibrant place and where your character will need to go if they are looking for someone. All manner of people live in the Housing Districts of cities; entertainers, brewers, retired heroes, seamstresses, tailors, huge families, hermits squirrelled away from the outside world, and soldiers for the army of the city. The Housing District is a great place for anything to happen in your story that involves meeting new or old characters and advancing your adventure with information and rumour!`
            },
        'amenities' : {
            'Palace Grounds' :
                `This city has a palace, and a ruler as well. This is likely a place of sumptuous architecture built out of only the most ornate Rook husks, at a high point in the city  looking over everyone else. It is doubtful that a wanderer such as yourself would simply be allowed in but perhaps your story has given your character a reason to speak to the ruler? An offering would certainly help - maybe you have picked up a treasure on your adventure?`,
            'Lapidarist' :
                `A Rookstone specialist; someone who can work these ancient magical stones and magically upgrade your equipment, for a price of course. FOR 1 TREASURE - they can add an additional magical ability (Ice, Rumble or Electric) to your helm. FOR 2 TREASURES - they can add a magical ability to an Arm, Rookling or Mount. FOR 3 TREASURES - they will share with you a Rookstone from their private collection. One that isn’t Ice, Rumble or Electric; but a new one-of-a-kind magical power. You can come up with what this power is and how your character can use it.`,
            'Rooksmith' :
                `Toiling away in their Mount Garages; Rooksmiths work on the mechanical parts of Rooks and convert them into vehicles or mounts to be ridden upon. FOR 3 TREASURES - they will build a custom mount for your character. It could be seaworthy, or landworthy and will feature some form of WEAPON based attack ability which you can choose (such as cannon, crossbow, battering ram etc.) See MOUNTED class info for fighting with MOUNT weapons.`,
            'Cartographer': 
                `A wise and bookish individual dedicated to the difficult art of mapping the lands around the city. Cartographers rely on information from Rook Hunters as they cannot go out and collect it themselves. THEY WILL PAY 2 TREASURES for a map of a new area. Take a quest from the Hunter’s Guild. Draw a map of your adventure marking anything discovered from your EXPLORATION phases whilst on the quest. Return it to the Cartographer for your reward.`,
            'Weapon Smith':
                `A tough person covered in oil and rumble powder working in a hot and smoky forge. They take Rook weapons and adapt and upgrade them for hunters. FOR 1 TREASURE - they can upgrade your current weapon. Add 1 to your COMBAT score. FOR 2 TREASURES - they can give you a whole new weapon. This is yours to come up with; perhaps a great hammer or a long Rookspear? Add 1 to your COMBAT score.`,
            'Arms Dealer': 
                `They stand behind their counter; a great number of small arms coming out of their back like a stone spider. The Arms dealer can find a new arm for you and help you with the ritual of attunement. FOR 2 TREASURES - they can provide you with a whole new arm. This can be whatever you imagine - perhaps it is coiled like a snake, or huge and thick like a tree trunk; able to lift a boulder with ease?`,
            'Rookling Crèche':
                `Rookling Crèches appear in most cities in the Colostle as a great place for Hunters to pickup their first Rookling companion for a quest. Or for those who live within the city to secure some cheap labour for their business or family home. As a player you can trade any Rooklings you have adopted on your journey here for a chance at a different type using the table below. Or you can buy a Rookling for 2 TREASURES. Either way you must let the cards decide which you receive - its always a gamble with Rooklings!`,
            'Gourmet District':
                `The centre of food production in the city; a bustling place of restaurants, food markets and spice bazaars. Here, hunters who have caught wild beasts out in the lands surrounding the city can find a great price for their prize - and also get a great meal while they’re bargaining. THEY WILL PAY 1 TREASURE for a wild beast caught by a hunter. FOR 1 TREASURE - enjoy a meal from one of the many restaurants and add 1 to your EXPLORATION score.`,
            'House for sale':
                `Living in a city does not come cheap. For 20 TREASURES you can buy a house in a city that has this option available. This is advisable to do if the city you have discovered has a lot of useful amenities. Owning a house grants you plenty of story options for your character but it also grants your character 2 major boons:
                HEALING - once per stay in the city you can heal your character fully back up to their starting EXPLORATION and COMBAT scores. Narratively this involves your character staying in the city for a WEEK.
                FAST TRAVEL - As a resident you gain access to the city’s Caravan service which allows your character the ability to fast travel back from any Hunter’s Guild quests. This means your character won’t have to spend the EXPLORATION phases to journey back after a quest and instead can travel for a single day in the caravan. You cannot use the Caravan to head out to a quest though - only to return home.`  
            }
    }
    let merchant = [
        `GLIDER - Neat unfolding glider structure stored on your character’s back that allows you to glide from heights. PRICE: 3 Treasures`,
        `WEATHERSTONE - A mysterious stone that summons (${searchArray(weather)}). it will always generate. Can be used once per EXPLORATION phase. PRICE - Any 5 items`,
        `TURTLE SHELL ARMOUR - Stone Rook Armour in the shape of a turtle shell. Will block one wound of damage each COMBAT phase. PRICE - 5 Treasures`,
        `TRIPWIRE LAUNCHER - A crossbow-like device that launches 2 pins with a chain between them. When aimed correctly this can trip up a Rook. PRICE - 4 items`,
        `ROOK GAUNTLETS - Huge stone Rook hands that fit over your hands and allow you to punch with the power of a Rook. PRICE - Any 1 item`,
        `EXTENDING POLE - Telescopic pole made from Rook parts. Allows you to vault upward and also attack from a distance PRICE - Any 3 items`,
        `ELECTRIC SWORD - A Rook great sword imbued with Electric magic. PRICE - 1 Treasure`
    ]
    let huntersGuild = [
        [/*Location*/
            `in a deep dark forest`,
            `on an island in the middle of a lake`,
            `high in some rocky mountains`,
            `in a Rook graveyard`,
            `deep in a strange cave`,
            `in the misty gloomy swamplands`,
            `at the doorway to another room`,
            `in the abandoned ruins of an ancient people`,
            `on the huge staircase leading up into the clouds`        
        ],
        [/*Twist*/
            `The Rook is picking on travellers and attacking their mounts and then eating them.`,
            `The Rook is flying somehow, circling a tower and dropping boulders on anyone who gets close.`,
            `Inside a huge ancient Rook husk, a medium sized Rook is holed up sending hordes of Rooklings out to steal resources and bring them back.`,
            `A massive spider-like Rook is terrorising local towns and villages.`,
            `A wheeled Rook is churning up farmland of a local village.`,
            `A Rook has made its nest in a village and has forced all the residents out.`,
            `A Rook has planted itself in a river and blocks the flow of water.`,
            `A Rook underground is causing earthquakes with its rumble magic.`,
            `At the top of a volcano a massive Rook is awakening and threatens to make the volcano erupt.`,
            `A mischievous spectral Rookling haunts a town.`,
            `A town built on the back of a huge once-dormant Rook. But the Rook has awoken and is slowly on the move...`,
            `People have reported a voice coming from within a massive dormant Rook...`,
            `A whole village is dreaming of the same Rook, but none of them have seen it... yet.`
        ],
    ]

    function buildCity(){
        let size = 4 + rollDice(9)
        let cityContents = [`Hunter's guild`,'Tavern','Merchant','Housing district'] 
        for (i=size-4;i>0;i--){
            cityContents.push(searchArray(Object.keys(cityBasics.amenities)))
        }
        loopPrintList(cityContents, CityOutput)
        
    }
    function guildQuest(){
        let distance = 1 + rollDice(4) 
        let reward = 2 + rollDice(1)
        return `${searchArray(huntersGuild[1])} It can be found ${searchArray(huntersGuild[0])}, ${distance} phases away. We will give you ${reward} treasures if you solve this problem.`
    }
    function rookling(){
        return searchArray(rooklings)
    }




/*****BATTLEMENTS*****/
   /*****OCEAN*****/
    //Supplements
    let exposureEvents = [
        `TREASURE FALL - A stone capsule falls from the sky, triggered by your movement. Nothing attacks you, but the capsule contains a TREASURE within it. to your inventory - you may be able to trade it later on in your adventure.`,
        `ASTROLITHIC ROOK CHASE - An Astrolithic Rook falls, but something about it seems wrong; it falls onto a distant rooftop, gets up, and turns in your direction. You see its eyes flash - it’s hunting you! Describe how you run away and hide from it (using other prompts from this EXPLORATION phase), or turn to fight! (See below to create your opponent)`,
        `EERIE SILENCE - Nothing happens. Maybe you got away with it this time.`,
        `ASTROLITHIC WRECKFALL - draw another card to see if you are hit by debris from the falling wreck of a downed Astrolithic Rook. If it is RED you are hit and take one WOUND. If it is BLACK you are safe.`,
        `METEOR SHOWER - Tonnes of burning debris falls from the sky, perhaps once a Rook, but now just fiery balls of death. You’re caught out with nowhere to take cover, take one WOUND.`,
        `ASTROLITHIC ROOK APPEARS - See below to create your opponent and then fight!`
        
        
    ]
    //Exploration
    let battlementEvents = [
            /*Organic (Hearts/Diamonds)*/
            [
                `A single castle tower sticks up out of the water, waves splashing around where it connects with the sea.${searchArray(['It seems uninhabited.','You hear voices from deep within.'])} There is a doorway that is accessible from the height of the sea, and when you look down into the interior you are stunned to see that it goes deep down into an underwater complex, completely airtight from the sea around it. WEATHER: ${searchArray(weather)}.`,
                `Another seagoing adventurer in their own vessel. ${searchArray(['They seem friendly.','They seem unfriendly.'])} WEATHER: ${searchArray(weather)}`,
                `Shipwreck. You pull up alongside the ${searchArray([`mostly intact vessel and find ${searchArray(items)} and ${searchArray(items)}`,`the completeley wrecked vessel and find ${searchArray(items)} floating among the debris`])}`,
                `An island with the tell-tale crenellations of a castle around its perimeter. Could it be that you are seeing just the very top of a huge Rook below the waves? ${searchArray(['The rook is dead.',`the rook's traps are still active!`])}`,
                `A huge seagoing creature is swimming just below the surface. Maybe its leading you somewhere, maybe you could hunt it for food? ${searchArray(['It swims past your vessel with no issue.','It hits your vessel as it passes!'])} WEATHER: ${searchArray(weather)}`,
                `Sea cave, large enough for your vessel to enter. It’s huge, cavernous within, like an underground river leading from one cavern to the next. ${searchArray([`It is inhabited and the ${searchArray(['friendly','unfriendly'])} creatures you meet are not human`, `It is uninhabited and you find ${searchArray(items)}`])}`,
                `A pirate ship! The pirates lasso your ship and bring you aboard. This is not a time to fight - you must sneak out and escape the pirate ship! Tell your story of how you navigate the halls and decks of the pirate ship and ${searchArray([`how you find the treasure`,`how you find the weapon`])} that you take back with you.`,
                `Shallow waters and underwater ruins. If the weather is good, you could drop anchor and swim down to investigate...${searchArray(['Finding rook parts','finding treasure'])} should you be able to venture into the deeps.`,
                `A small island. ${generalExploration()}. That is all there is to find here, return to the SEA to continue. WEATHER: ${searchArray(weather)}`,,
                `A coastline. If you decide to disembark here then return to the base rulebook for ongoing EXPLORATION phases. WEATHER: ${searchArray(weather)}`,
                `You found an island with ${searchArray(items)}!`,
                `You found A Medium Rook!`,
                `You found A Massive Rook!`
            ],
    ]
 

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


    function draw(id) {
        let cardArray =  [2,3,4,5,6,7,8,9,10,'j','q','k','a']
        let suitArray = ['c','h','s','d']
        const cards= {
            ac:"../art/cards/ac.png",
            ad:"../art/cards/ad.png",
            ah:"../art/cards/ah.png",
            as:"../art/cards/as.png",
            kc:"../art/cards/kc.png",
            kd:"../art/cards/kd.png",
            kh:"../art/cards/kh.png",
            ks:"../art/cards/ks.png",
            qc:"../art/cards/qc.png",
            qd:"../art/cards/qd.png",
            qh:"../art/cards/qh.png",
            qs:"../art/cards/qs.png",
            jc:"../art/cards/jc.png",
            jd:"../art/cards/jc.png",
            jh:"../art/cards/jc.png",
            js:"../art/cards/jc.png",
            '1c':"../art/cards/1c.png",
            '2c':"../art/cards/2c.png",
            '3c':"../art/cards/3c.png",
            '4c':"../art/cards/4c.png",
            '5c':"../art/cards/5c.png",
            '6c':"../art/cards/6c.png",
            '7c':"../art/cards/7c.png",
            '8c':"../art/cards/8c.png",
            '9c':"../art/cards/9c.png",
            '10c':"../art/cards/10c.png",
            '1d':"../art/cards/1d.png",
            '2d':"../art/cards/2d.png",
            '3d':"../art/cards/3d.png",
            '4d':"../art/cards/4d.png",
            '5d':"../art/cards/5d.png",
            '6d':"../art/cards/6d.png",
            '7d':"../art/cards/7d.png",
            '8d':"../art/cards/8d.png",
            '9d':"../art/cards/9d.png",
            '10d':"../art/cards/10d.png",
            '1h':"../art/cards/1h.png",
            '2h':"../art/cards/2h.png",
            '3h':"../art/cards/3h.png",
            '4h':"../art/cards/4h.png",
            '5h':"../art/cards/5h.png",
            '6h':"../art/cards/6h.png",
            '7h':"../art/cards/7h.png",
            '8h':"../art/cards/8h.png",
            '9h':"../art/cards/9h.png",
            '10h':"../art/cards/10h.png",
            '1s':"../art/cards/1s.png",
            '2s':"../art/cards/2s.png",
            '3s':"../art/cards/3s.png",
            '4s':"../art/cards/4s.png",
            '5s':"../art/cards/5s.png",
            '6s':"../art/cards/6s.png",
            '7s':"../art/cards/7s.png",
            '8s':"../art/cards/8s.png",
            '9s':"../art/cards/9s.png",
            '10s':"../art/cards/10s.png"
        }
        function pickCardAndSuit(){
            return searchArray(cardArray) + searchArray(suitArray)
        }

        let cardChoice = pickCardAndSuit()
        var img = new Image();
        img.src = cards[cardChoice]
        let elem = img
        img.onload = function () {
            if (id === 'playerDrawCon') {
                document.getElementById("playerDrawCon").appendChild(elem)
            } else {
                document.getElementById("enemyDrawCon").appendChild(elem)
            }
        }
        
    }
        //City

    









