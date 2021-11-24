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
}

function randomHostAndHook() {
    //HOST AND PLOT COUPON ---------------------------------------------------------- 

    function returnHost() {
        let hostArray = [
            'A large family of gnomes. They are quite welcoming to guests, and serve dishes upon dishes of rich, steaming food at their meals, often accompanied by the father and the older sons singing.', 'A young tiefling loner who’s willing to share his small, spartan flat. A starving-artist type (well, not quite starving, he does pretty well) who specializes in portraits. He doesn’t bother the guests if they don’t bother him. Keeps his work depicting who he remembers as his mother (an Erinyes) in a safe in his room.', 
            'A soft-spoken Half-orc librarian and his wife, an Elvish herbalist. She isn’t as welcoming as him, but is alright with guests as long as they stay out of the workshop. They both do some of the cooking, so the meals are…unique.', "A Kobold matriarch. While her children have all moved out, their children are dropped off at Grandma’s house quite frequently, and she teaches them all she knows. She also runs a small shrine to Bahamut in the cellar.", "A hot-headed, wealthy heiress and her more rational lady-in-waiting.", "The prince of a corroding noble line, of late taken to dressing in black, composing gloomy poems, and brooding on the battlements of his manor.", "A dwarvish professor with a magnificent walrus mustache, as well as his warm, old-fashioned wife (a dressmaker) and their daughter, who’s visiting for a month or so from her apprenticeship.", "The quiet Mother of a hostel run by the temple of the god of the poor. The tragedy and despair of many of her visitors has rubbed off on her a little. The food is outstanding.", "A not-quite-right young man with ambitions to become a psychologist. Asks far too many personal questions, then goes off on rants about what he thinks shaped his guests to the people they are today. Total quack psychologist, doesn’t know what he’s saying at all.", "An Eladrin who’s spending a few centuries ‘indulging in kindness’. There’s a too-good-to-be-true air to the stay. Breakfast in bed, indoor training arena, a small dungeon built underneath the manor and stocked with inexpensive monsters, a wizard’s study, everything they could possibly want. And the host is always smiling.",
            "A jovial Goliath with an Australian accent who spends most of his time wrestling with various dangerous forms of wildlife. Owns a large merchant company, spends most of his time doing push-ups or lifting weights or wrestling yetis.", "A shriveled, wrinkled, hobbling old Bullywug whose sentences are out of order, and seems to speak in riddles. He wears a slightly threadbare robe and carries a walking stick.", "A stern Halfing dance instructor. She’s quite sprightly, humming waltz tunes as she works. She corrects people’s postures out of force of habit.", "An old Dragonborn mercenary who frequently lapses into a thousand-yard-stare. While not tormented by nightmares, he’s a good-humored guy with quite a few tips on adventuring.", "A water genasi weaver whose skill isn’t quite unmatched, but it’s up there. Naturally, the curtains and carpets of his house are expertly made and quite flamboyant.", "A cackling, bitter old woman. Actually a Green Hag, and her curse is the reason the couple next door (whom she finds insufferable) have been trying for a child for years without success. Serves stew or porridge for every meal from a huge, battered-looking black cauldron.", "A hard-as-nails half-elf rancher. Owns stables upon stables of pure-bred racing horses. Despises city-slickers.", 
            "An old Minotaur noble. He wears huge suits, custom-made for him, and has a staff of Animated Objects who sing, dance, and make dinner.", "A slightly suspicious young woman. Knows far too much about weapons, disappears for long periods of time, and locks the basement door very heavily. She’s an assassin for a local gang of racketeers, and will skip town if she’s found out.", "An Animated Armor that speaks like the Discworld golems (That Is, She Talks Like This) and moves very jerkily. She (well, it’s built for a female humanoid) used to work for an evil artificer before a band of adventurers gave her full free will. Knows a thing or sixty-four about dungeoneering, and considers herself indebted to all adventurers.", "A goblin horse-jockey who loves nothing more than the thrill of a race. Talks a mile a minute, usually boasting about his races, and his house is full of trophies that he polishes devoutly.", "A human card-sharp who won his entire house in a game of Triple Ogres. He’s married to the shrewd but not very welcoming owner of a local tavern. She brings home the latest gossip each night.", "A kobold artificer who’s trying to turn his species’ natural affinity for mechanisms to the good. Owns all sorts of fascinating contraptions, like an automatic pencil-sharpener or a tiny construct that writes down any good ideas he has mid-conversation.", "A merry old smuggler, although he’s put his pirating days behind him aside from the odd chorus of Dead Man’s Chest. His house is adorned with model ships and sketches of exotic shores. Drinks strong home-brewed grog.", 
            "The town doctor. There’s something odd about her of late. She stays up past midnight, tends to skip meals, and always seems to be tearing up some piece of paper and tossing it in the trash. (She’s smitten with the blacksmith’s apprentice, but can’t bring herself to tell him.)", "A rough-and-ready frontier-dwelling female Dwarf, who lives in a quaint cottage. She’s older than most of the village, and knows all the skills of the hinterlands: medicine, hunting, cooking, the lot.", "An old man who can’t seem to look you in the eye. He has one craft, and one craft only: he’s a knife maker. Assassins from every syndicate, court or gang come to him for their daggers. Even the odd Drow comes in the dead of the night to buy an honest-to-Lolth Master Work dagger.", "A scheming duke who tries to see if the party thinks his power-plays would work without hinting too obviously at his massive ambitions.", "A satyr couple who are, well, typical satyrs. They love wine, music, food, the usual revel stuff. Enjoy having guests, of course, but can’t stand ‘sticks in the mud’, ‘killjoys’ or ‘introverts’.", "A female Drow who left the Underdark because she’s claustrophobic. Polite, in a regal sort of way. Her house doesn’t have hallways so much as long, broad halls, with bookcases or coffee tables or armchairs.", 
            "A newer vampire who is having a little bit of an identity crisis. He gets the ‘nocturnal’ part, yes, he gets that, but isn’t the whole ‘domination’ thing a little unethical? and similar conversation. Keeps forgetting that garlic tastes disgusting to him now.", "The best Dwarvish pastry-chef that has ever walked the earth. And she knows it. Quite boastful.", "The keeper of a local shrine to the fire god. He’ll just sit by the fireplace, staring into it for hours on end. Has a very large and overly friendly golden retriever.", "The local ‘crazy cat lady’. An Air Genasi whose hair is always blowing in a gentle breeze. This confuses her cats to no end. She has forty-three of them, and one Mimic who enjoys it’s current lifestyle and has decided to stay shaped like a cat.", "A Tabaxi game-warden. His wolfhound isn’t part wolf, it’s part Displacer Beast, which means people often think he has two dogs. Pleasant but fairly quiet.", "A grizzled old human war veteran. Wears an eyepatch. Has a suit of plate-armor stained with horrific, otherworldly humors in his front hall. Retired after ridding his ancestral estate of some kind of great beast he refuses to describe.", "A gnomish scientist who studies modrons. He’s utterly fascinated by them, and can go on for hours with horrifically dull facts and factoids about them. His house is littered with mounted modrons, dissected modrons, everything modron-related you could imagine.", 
            "A time-wizard who messes with his personal time for kicks. Making himself twelve years old, being in four places at once. He thinks it’s a riot. His house is full of books of temporal magic, or at least it was, twelve minutes before you try to open one of them. Opening one book makes them all vanish to the past. It’s his security system.", "A noble Knight Lord who lives in a small castle and commands an order of chivalrous Knights. A former adventurer.", "A wise Grand Wizard who lives in a magic tower and commands a guild of powerful Wizards. A former adventurer.", "A clever Spymaster who lives in a heavily-secured manor and commands a guild of Spies. A former adventurer.", "A pious High Priest of Light who lives in a modest house attached to a glorious Temple. A former adventurer.", "A homely man with balding white hair, a small beard and eyeglasses. Meets with friends often, talking for hours in the cellar. Are they…acting? Playing some sort of dice-game? It’s not quite clear. Says he hails from the realm of Greyhawk.", 
            "An elvish professor of languages who, despite having fought in several wars, is a honorable, straight-laced, old-fashioned gentleman. He’s writing a rather long book. Apparently it’s about halflings and some kind of Ring?", "A razor-witted Dwarvish comedian who does standup at local taverns, dishing out the side-clutchers and knee-slappers galore. Willing to share a few jokes with the party, too. His ‘why did the cockatrice cross the road?’ always gets ’em.", "A Bugbear leg-breaker for the local mob is trying way too hard to be polite and gracious. His apartment’s nice, of course, but he seems to think that the entire party are some sort of sting operation.", "A former Underdark delver, this calm but dispassionate female Tiefling is married to a far more bubbly and cheery Wood Elf. They bicker regularly about what ‘acceptable decorations’ are, stuffed Troglodyte heads or singing roses.", "A brawny whiskey-maker who meets over a nice, old keg with rogues and grave-robbers every night, it seems. His house is above his tavern.", 
            "An Eladrin woodcarver who has recently taken up trying to enchant things. She’s terribly confident it’ll work out eventually, but for now you’ll have to put up with wooden busts that hurl abuse or curse words and cutlery that work together to spell out rather rude slang.", "A Halfling balloonist with a terrible case of wanderlust. Half of his things haven’t been unpacked yet, half of them are already ready to go.", "A master wizard who crafts Golems. Has some shady deals with dungeon overlords, but is still a good man. Might cut the Evil Overlords off from his business if approached; he’s a man of principles, just needs a push of sorts to get him to stand his ground for them.", "An Aasimar teamster who’s moving into the song business. He’s got quite the voice, and a few songs already written: All Shook Up, 500 Miles, and he’s working on a few more.", 
            "A slightly edgy Tiefling who wants to be both friendly and intimidating. Budding metalhead. His apartment is nearly plastered with band posters and song lyrics.", "A genteel, aristocratic Red Dragon who lives in an enormous castle.", "A curious young man enamored by the sea. Despite his youth, his hair is receding. He never seems to blink, either. His house is full of weird idols and jewelry of ancient civilizations.", "A charlatan ‘wizard’ who’s really just a chemist. Tries to keep her lab hidden. Nearly has a breakdown if she’s confronted about her fraud.", "A Goliath strongman of the local circus. His quarters are rather large, because he’s rather large. They’re right next to the acrobats’ and the lion tamer’s.", 
            "A vain elvish wizard who spends most of her time in front of her magic mirror, and the rest of it complaining about upload schedules and dislike mobs and ad revenue.", "A dwarvish butcher. His wife is an author. Both of his daughters are in preschool. He himself is vegetarian, but does eat fish. Spends his evenings playing pool in the cellar with his friends, or going on walks with his daughters.", "A professional court-jester of the local duke or lord. Not as cheery off the job; gripes to anyone who’ll listen about his poor wages and difficult job. His house is a small cottage within the bailey of the castle.", "A tight-lipped priest who seems to have a shrine to every god in his tiny house. The hallways are crammed with altars and icons, and the whole place smells like incense 24/7.", "An unintentionally insufferable Aasimar ballerina. Lets the guests have the run of the kitchen; she’s too busy practicing for her next performance in the studio downstairs.", "A young bachelor Mountain Dwarf, who’s bitter about getting turned down by the local army or militia. He’s drinking a little more than is good for him.", 
            "A gnomish jeweler, his wife and three children. They have a pretty large townhouse. The husband is a little busy with an important order: a new crown for an anonymous nobleman.", "A halfling priest of various gods of knowledge and nature. He’s a part-time biologist, running a few experiments in the lab in his basement. He’d love to meet a Druid or Ranger with more hands-on experience than himself.", "A Fey who lives in a checkers-themed tower. May kick the guests out if they mention chess or use chess analogies. Most of the food is circular (pie, pancakes, etc.), the tablecloths and bedsheets all have checkered patterns. Writes long letters to a bitter rival.", "A Fey who lives in a chess-themed tower. Gets rather testy if people mention checkers. The staff are construct automatons that only move like particular chess pieces. Complains about a completely irrational rival who sends him storms of nonsense letters every day.", "A professional human trick-shot-archer. She goes on tour with the circus now and then. Her favorite one is nailing a playing card out of someone’s hand from one hundred paces.", 
            "A stout Dwarf who’s a master cook. He puts his heart and soul into every slab of beef, taking hours just to prepare them for barbecuing. Doesn’t spend much time with the guests.", "A human former doctor (she’s still got the beak-mask hung up on the wall in an airtight case, and she warns the party that it’s quite contaminated) who retired after fighting some sort of otherworldly entity beneath her ancestral estate. Recently took up horse-riding.", "A human comedian whose jokes tend to be at his own expense. Unmarried but pretty well-off, for a comedian. He tends to leave in the evening and come back close to midnight after his show.", "An eladrin priest of Tymora. Closer to his fey ancestry than most Eladrin. He’s scheming with a local gang to spring some of their hooligans from prison- after all, the whims of chance are unpredictable, or so he’ll say if the party threatens to inform the authorities. Then he will try and bribe them.", "A calm Oriental-looking man who works as a janitor during the day. His apartment isn’t exactly barren, but it’s certainly unextravagant. He’s teaching a local child the various martial arts he mastered in his time as a Monk.", "A simple Halfling herb-farmer. She has a small plot of land behind her house, where she grows things like spices and vegetables. Patient, because as she says, you can’t hurry peppers. Spends most of her time reading novels.", 
            "A dragonborn tale-weaver. No, not an author, she’s quite firm. A tale-weaver, the kind that don’t get written down so much as passed along. Though she doesn’t exactly have it in writing, she’s very familiar with the wording and themes that make a riveting tale.", "A solemn, gods-fearing Dwarvish carpenter. They call him the Pious Benchmaker, which baffles him. His wife is of somewhat better cheer, but tolerates no nonsense in her house. The furniture is first-rate. You could hit it with a battle-hammer and it wouldn’t dent.", "An Aasimar mattress-maker. Laments his own misfortune: his mattresses are so good, he either sleeps on them and can’t get himself out of bed, or he sleeps on a couch or armchair and doesn’t sleep well. It’s a DC X Strength save to get off his guest-beds (the best ones, for he’s quite hospitable), where X is 10 plus the number of days since the sleeper has been in a normal bed instead of a bedroll or cot.", "A slightly unhinged half-orc scholar. He’s studying all sorts of bizarre phenomena at once, and keeps a wall covered in notes, sketches, and pieces of twine connecting them. The statistical anomalies of coin flips, the way the planet is tilted, all those sorts of things. Frequently becomes so engrossed in his studies he forgets to eat.", 
            "A ratcatcher who is quite ferocious in his task. He’s got mousetraps all over the place, and hundreds of rat skulls nailed to his wall. Grim, adamant, and talks at length about what utter vermin rodents are.", "A friendly, jocular doppelganger illusionist and it’s tame mimic pets. The house appears to have a large staff of servants and much finely-made furniture…", "A gnomish Expert Clown. He doesn’t just study mere tossing and tumbling, mind you. He studies the psychology of clowning. What makes a pie to the face so funny? Or what is the thrill-inducing factor of juggling eggs? He can tell you. He can tell you for several hours.", "A human stone-carver and his teenage son. The son’s a little worried about his father, as the latter seems to be losing interest in the craft. Their house is full of half-finished works.", "A high elf mask-maker. It’s a delicate craft, she’ll tell you. Fey come to call every so often, picking up their masks but also staying to chat with her a bit. So do some actors. And one or two assassins.", 
            "A scruffy human gravedigger. He isn’t exactly a philosopher, but tends to make incisive remarks about mortality and time. Doesn’t like elves, because they don’t give him business.", "An old man with a bald head and gleaming eyes. If asked, he only gives his profession as ‘chemist’, and spends a lot of time in his lab. He’s less harmless than he seems; he’s the master poison-brewer for a local assassin’s guild. If he’s found out, he calls in his allies on whoever discovered his true identity.", "A young couple of a Tiefling and an Aasimar. Their ancestors didn’t like the marriage much, and it couldn’t exactly get officiated by a priest (but the local marriage law did allow for a Fey to do the job). They’re getting along fine.", "A pious couple who are gravely concerned about their young daughter. She claims to see ‘shadowy people’ in the cellar, and apparently brought the family dog back to life. They’re both nearly nervous wrecks, and priests of every Good god have been coming and going all week to try and exorcise the child.", "A white-haired old man and his shrill wife, both the village healers, although the Mr. recently got fired by the prince whose father he used to work for.", "A playwright who is outraged at his rivals trying to spread the rumor that his work was ghostwritten for him. Insists on reading off sonnets and scenes to the guests to prove that he’s genuine.", "A grizzled, scarred town guard. He’s only in during the day, usually asleep, and spends the nights walking the streets and smoking very particular cheap cigars. Moody but not hostile.", 
            "A ‘professional quest-giver’ who pampers the heroes with everything he can. He’s in kahoots with a local dungeon-lord, and gets a share of the armor, weapons and loot of the heroes killed in the dungeon he directs them towards. He’ll take to the hills if he’s found out.", "A young priestess of a god of the wilds. Her house is on the very outskirts of town, and has a terrible case of rats, which she doesn’t mind as long as they don’t bother the guests. Rats that do bother the guests get speared. She doesn’t take nonsense, but has some sense of humor.", "A Kenku minstrel who rents a room above the tavern he performs in. It’s covered in posters from his ‘glory-days’- although a keen eye (DC 15 Investigation) will note that they’re actually other bards’ posters, with the minstrel’s name altered into them.", "An apprentice baker and his wife, a schoolteacher. Their house was a cheap deal, and is a little run-down but still serviceable. Gets a little drafty, though.", "A Kobold who claims to be an architect and interior designer. Actually, she’s a dungeon planner who designs catacombs, lairs and castles galore. Highly sought-after by evil overlords, and frantically tries to direct them away while the guests are there. If she’s found out, she’ll flee to the safety of one of her closer creations.", "A Swordsmith who has been at it for years. He keeps a display case of splintered, shattered or blunted swords recovered from various dungeons and battlefields, each with the tale of a fallen hero attached to it.", "A halfling gourmand with an affinity for candies. He’s a longstanding foe of witches who use his creations, or mockeries thereof, to lure children into their cook-pots.", "A Dwarvish family of four- father, mother, son, daughter -who are rather new in town. Hospitable, but the house is still full of moving crates. The father is a lumberjack, the mother is a stay-at-home parent.", "The High Priest of a local shrine of the god of travelers and messengers. He’s an unmatched source of information, references and road maps, and will greet anybody with a smile so long as they return the favor.", "An old Elvish couple. The husband spends most of his time golfing or whittling, the wife is busy giving advice to her newly-married daughter. They live in a nice old house, although there’s a ghost in the attic. Don’t worry, it’s very polite during the day, and it can’t leave the attic."
        ]
        return searchArray(hostArray)
    };

    function findPlot() {
        let hostPlotArray = [
            [ //ZERO THE PERSON'S ROLE
                'a barkeep.', 'a warrior', 'a merchant', 'an agent', 'a criminal', 'a performer', 'a nobel.', 'a bureaucrat', 'a member of the clergy', 'an artist', 'a craftsman', 'a magic user'
            ],
            [ //ONE THEIR LOCATION
                'in an unknown location - they are hard to pin down, always on the move', `in a ${searchArray(['nearby', 'far away']) + " " + searchArray(['village', 'city', 'castle', 'stronghold'])}`, 'that passes through here occasionally, might want to ask around', "that frequents the area, keep and eye out and you're bound to bump into them", 'that lives right nearby', 'that lives just a few villages away', `quite a distance from here in a remote location, you'll need your map marked`, "who is basically unreachable. Let their people know, they'll find you"
            ],
            [ //TWO THEIR FEELINGS TOWARDS YOU
                "I hate [PC],and I wont give [[PC]/the party] the time of day, unless they pay up front (5gp/minute)", "Why would I help [PC], unless of course [PC] is offering something in return?", "I am willing to help [PC], but they'd need to persuade me", "Will do anything [PC] asks, no explanations or renumerations needed", "I hate [PC's] guts", "I never really liked [PC]", "We did try to kill each other that one time…", "I do not remember [PC] in the slightest", "I tolerate [PC], they'll get no special treatment", "I could lend a hand maybe I guess, but what's their name again?", "We are amicable but not necessarily amenable", "Sure, for the right (high) price in gold", "Yes, but first they'd need to help me do a thing that’s… a little dark", "Yes, but they'd need to help me get this thing first", "Yes, but they'd need to help me resolve a personal issue first", "Yes, but they'd need to cover some expenses", "Yes, but they'd have to join my guild", "Wish I could help, but it’s impossible now because magical restrictions", "Wish I could help, but it’s impossible now because social issues", "Yes, but they'd need to help me resolve a personal issue after", "I would do anything for [PC], but I won’t do that", "Any time, but they'd owe me one", "I would do anything for [PC]"
            ],
            [ //THREE RELATIONSHIP
                'are your rival', 'are an acquantance', 'are an old friend', 'are your old teacher', 'are a fellow student', 'are a family friend', 'are a childhood friend', 'are a family member', 'are an admirer of your work', 'are your secret admirer (stalker?)', 'are a work associate of yours'
            ],
            [ //FOUR ASSISTANCE
                "has done something similar long ago", "has done it once under duress", "has experience getting the right things for it", "has practiced this before, and can totally help", "is very smart, and can puzzle out stuff like this all the time", "knows the right people to ask about it", "knows where to find out more about it", "knows some ancient lore about it", "has some related magic for it", "has  authority to get help for it"
            ],
            [ //FIVE POSSIBLE TWIST
                'NPC really doesn’t like someone else in the party', 'NPC really likes someone in party too much', 'NPC Might tell your enemies', 'NPC Is actually not helpful', 'An adversary learns about you and your location and acts upon it', 'A local mob threatens the NPC to not help [PC]/ Party', "Another NPC you know needs your help, urgently", "You are mistaken for someone else, who's in big trouble", "The NPC severly insults and taunts one of your party members.", "The NPC gets a crush on [PC] or on one of the party"
            ],
        ]

        function findAssistance() {
            return "If you tell your host about a current challenge you'll learn about someone who " + searchArray(hostPlotArray[4]) + "."
        };

        function findRoleAndLocation() {
            return " They are currently " + searchArray(hostPlotArray[0]) + " " + searchArray(hostPlotArray[1]) +"."
        };

        function findRelationship() {
            return " Rumor has it that they " + searchArray(hostPlotArray[3]) + "."
        };

        function findFeelings() {
            return ` Also, you'll probably be hearing something like ` + '"' + searchArray(hostPlotArray[2]) + '" if you end up trying to contact them for help.'
        };

        function findSetback() {
            return searchArray(hostPlotArray[5]) + '.'
        }

        let setbacknumber = Math.floor(Math.random() * 100);
        if (setbacknumber > 85) {
            return findAssistance() + findRoleAndLocation() + findRelationship() + findFeelings() + ' Unfortunately, ' + findSetback(); +"."
        } else {
            return findAssistance() + findRoleAndLocation() + findRelationship() + findFeelings() 
        }
    };

    document.getElementById("Host").innerHTML = returnHost() + " " + findPlot();
    //console.log(returnHost() + findPlot())    
}


