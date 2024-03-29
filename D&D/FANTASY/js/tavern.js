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
function printFrom(array, number, id) {
let list = shuffle(array).slice(0, number)
list.forEach(function(item) {
var li = document.createElement("li");
var text = document.createTextNode(item);
li.appendChild(text);
document.getElementById(id).appendChild(li);
});
};
function orderedPrint(array, number, id) {
let list = array.slice(0, number)
list.forEach(function(item) {
var li = document.createElement("li");
var text = document.createTextNode(item);
li.appendChild(text);
document.getElementById(id).appendChild(li);
});
};
function loopCountStoreList(array) {
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
return count(x);
};
function modify(number) {
return Math.floor(number * (.85 + Math.random() * .4))
};
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
function reload() {
location.reload()
};
function loopPrintList(array, id) {
    final = array
    final.forEach(function(item) {
        let li = document.createElement("li");
        let text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};

/*==================================================================================*/
/*-----------------------------Page Scripts Below-----------------------------------*/
/*==================================================================================*/

function tavernPremise() {
let taverns = [
"The Salty Seafarer - Found moored up at ports around the lands, this floating tavern is always busy, but only for a week or so before it sails off to it's next destination. Who knows when you'll bump into it again! Famed for the owner's stories and fables they have collected on their travels from the tavern's many patrons, as well as world famous bards who often travel along with it. Of course we can't forget to mention the exotic drinks and food they have picked up on the way!", 
"Nobody's Inn - Entering this tavern, you find that there doesn't seem to be an owner, although there are many patrons, pouring their own drinks and leaving coins in collection trays.", 
"The Boney Bar - The Boney bar is, if anything, creepier than it sounds. Not only are there skeletons serving you, nearly everything is made out of bones. The tables and chairs, a massive chandelier hanging in the centre of the room... even the mugs are skulls with the holes plugged up! Luckily, the food and drink is exquisite!", 
"The Dapper Dragon - A fancy restaurant that uses tiny dragons and other creatures to help cook food. Basically Ratatouille but with monsters! If I were you, unless you like your food black, I wouldn't ask for my steak to be 'Well done.'", 
"Hunter's Rest - Situated in the head of a huge dragon, this extravagant tavern is a place for hunters to show off their kills and share stories of their hunts. They also hold competitions here, as well as hosting a market and trade shows for meats, furs and other materials extracted from their kills. Adorning the walls of the three floors are the heads of all sorts of beasts, ranging from stags and boar to more exotic creatures like Owlbears and Displacer Beasts. There is a leaderboard filled with the top 20 hunter's names and how many points they have for the season.", 
"The Weather House - The weather inside this place is always different to what it is outside, offering respite if it is particularly hot or cold. Unfortunately the owners were not very specific with the wizard that they got to enchant their tavern, causing it to rain, snow or even hail inside when the weather outside is warm, which isn't great for business, although they do keep a few umbrellas by the front door, so you can stay mostly dry if you decide to stay here.", 
"Tinsy Winsy Tavern - Sandwiched between two large buildings is a small door leading to a tiny room with one stool in front of a short bar, leaving just enough room behind it for a halfling barkeep.", 
"The Drunken Dummy - Every night the owner is on stage with his wooden ventriloquist dummy. This thing looks creepy as hell, but they are telling some great jokes and the crowd is eating it all up! The act seems to show they have a complicated relationship, with the dummy regularly shouting down the owner and slapping him. It's a fantastic routine... or so it seems.", 
"The King's Armistice - This tavern has been untouched by many wars over the years. Said to have been blessed by a mighty wizards final words as he sacrificed himself to end a long and gory war, it is a place to go for some respite during warring times. Upon entering all equipment disappears, including clothing. No magic seems to work either. Of course upon exiting, many people instantly break any truce they previously had, making the surrounding area of this tavern a bit of a wreck.", 
"The Tinker Inn - As you push the door you hear a mechanical whirring. Looking up you see a clockwork soldier with a big hammer run out of a house and strike a bell, alerting the owner to a new visitor. Dotted around the tavern are all sorts of interesting toys and contraptions. Some are just for aesthetics, like a small hot air balloon flying around the room, but others are actually useful. Little trains run along tracks around the room delivering food and drinks and music is playing from a strange box at the back of the room.",
"The Nibbly Fish - Opening the door you realise that nearly the whole floor is lowered and covered in a pool of water about a foot deep. A sign on the door says, 'No shoes!' You take your boots off and step inside, noticing there are tiny colourful goldfish swimming around and nibbling the dead skin off your feet. There's nothing like a free foot pedicure whilst you enjoy a good drink!", 
"The Cat's Whiskers - Ran by a lovely Tabaxi family, this inn is full of cats of all different breeds. You'll find them napping on beams, weaving in and out of the patrons legs and mewing whilst they wait to be fed. It's a great place to visit if you like milk on tap! (But awful if you're allergic to cats)", 
"The Costumer's Always Right - There is a bouncer at the door dressed up like a bugbear. He says, 'Hey, no coming in without a costume.' Once dressed up sufficiently you are let inside. You see people dressed up as famous heroes from stories and also as monsters, some of which are real and some are made up. They are all chatting and laughing, pretending to fight and posing for portraits.", 
"Gravity Falls Tavern - Situated at the base of a waterfall that is actually flowing up the cliff instead of down it, the Gravity Falls Tavern is a sight to behold. It's upside down. Drunk people are exiting, stumbling around as they navigate the stone steps. Entering, you see a chandelier standing upright, 'hanging' from a chain set in the floor. The most amazing thing is that you see people walking and sitting on every single face of this room. Each side of the room seems to have it's own gravity field, including the bar, which is at 90 degrees to what you currently see as the floor. You realise that those people probably weren't drunk, just disorientated from dealing with all the changes in gravity!", 
"The Roasting Duck - Every night is roast night here at The Roasting Duck! We're not just talking about the food either. Come on in for you and your friends to get a good ol' roasting from our in-house roasters and you can even get up on stage and give it a go. The best roaster every night wins 30gp! Do you have what it takes?",
"Firebeard Tavern - At the end of every night the magnificently bearded owner stands up on a table in the middle of the tavern to the cheers of the patrons and sets his beard on fire, keeping it going for as long as he can. During this time drinks are free so the patrons swig as much as they can before he has to pat it out. His record is 4 minutes!", 
"The Tower - Unlike any tavern you've seen before, this place is about 6 times taller than it is round! Apparently this place used to be connected to a massive castle, but it got destroyed in a great war. With a spiral staircase round the edge and a pole in the middle to slide down, this tavern is certainly a novelty. You notice all the staff members have incredibly strong calf muscles from walking up the steps so much. At the top of the tower is an open top terrace, offering an amazing view out across the surrounding valleys.", 
"The Grape Escape - An underground winery that stretches for longer than any tavern you've seen before. Like a wine cellar, this place has thousands of bottles in racks and shelves that make up the walls. What sets this apart from other wine cellars is that it is also a maze! Without a guide you are sure to get lost in its winding walls. ", 
"The Peace & Quiet - A haven for writers and readers alike, this is the quietest tavern/library you've ever seen. Although to be fair, it is the only tavern/library you've ever seen. With three floors of books, comfy seats and desks, this is a great place to relax, or even come for a quick nap... as long as you don't snore. If you're looking for a good book, this is the place to go. There are books on every wall, shelves upon shelves of ordered books and not to mention the staircases with books under every single step! You will be spoilt for choice! However, if you aren't keen on this scene you aren't going to have too much fun. There are alcoholic bevereges, but they are all cocktails themed around book names... (Tequila Mockingbird, Lord of the Gins, etc.) and there is a limit of one per customer to avoid anyone getting too loud.",
"The Knife & Pork - With its very own in-house abattoir, feel free to select your favourite from a wide selection of pigs to chow down on this evening. It's the perfect place to be swined and dined! This place is really fancy and looks great from the outside. Everyone is dressed to the nines and are pretty posh. As soon as you enter you hear the squealing of pigs out the back. Likely to be a pretty harrowing experience for you and your party...", 
"The Amen Arms - The Amen Arms is a multi-use building, being a church and also a bar. The only problem is that they only sell communion wine on tap. Unfortunately this has left the members of the clergy with pretty severe drinking problems, which does liven up Sunday prayers, but isn't so great when the priest is loudly weeping at funerals and weddings.", 
"Rick Ade Bar - This bar has some of the trippiest drinks you've ever seen! Fizzing potions and steaming cauldrons are on every table and everything is so cheap! As you've had your fill and you go to leave you realise the door has been barricaded and there is no way out. You're told that all the drinks need to go before anyone can leave. Looking around you see there are creatures like Bugbears and Gnolls as well as people of all different races (and classes) around the bar, some not looking overly thrilled that they have to spend the night in this place. You see a fight break out between two clerics, shouting 'Die demon scum! Go back to whence you came!' That's when you feel it start to kick in... What on earth is in these drinks?", 
"The Stray Fey Inn - This beautiful inn originated from the Feywild. Due to an accident many years ago, this inn and all of its patrons got transported to your plane. Apparently this was a pretty rough area before the inn turned up and they attracted some higher class visitors. No one is quite sure what happened with the inn that was here before, but it is common legend that it was taken to the Feywild with its less-than-savoury patrons so they could try and redeem themselves in a different land.", 
"The Playhouse - This grand theater has been converted into a dining establishment with live acts. Once a month the Queen visits and judges a talent competition, with the winner taking a spot in the Royal Talent Guild. Members of this guild go to live in the castle grounds, entertaining guests and earning a great salary before being kicked back out into the real world once the Queen has had enough of you. Past members all seem desperate to get back, but most of them fail.",
"The Boar Inn - This tavern seems really standard. Just a really old sweet couple who are like 90 years old. Offer tea and coffee and cakes rather than booze. There are those white lacy doilies on the tables and it's just proper classic old person vibe. However, you do notice a dull repetitive thudding through the floorboards. With some investigation you find a bright neon, seizure-inducing underground club. Everyone is covered in glow in the dark patterns. Drink and drugs are in high supply. If you decide to stay you're soon joined by the old couple who properly rave it up. They ask that you do not tell anyone else of their secret club because the nobles wouldn't approve it. In return you get half price food and drink, either upstairs or downstairs.", 
"Twilight Tussle Inn - Every night at sunset a huge brawl breaks out over the tavern. Once there are x people left, everyone that lost must buy them a drink at some point during the evening. (Replace 'x' with the party size -1 person.) Naturally, the owners have long since stopped buying new glasses, tending to just use stone mugs because they are so much harder to break. They have also had to bolt down all of the tables and chairs to stop them being used as weapons every night. other than that is is pretty much no holds barred, although there will be a severe penalty if you actually kill someone during the tussle.", 
"The Brushstroke Bed & Breakfast - (BSB&B for short) is an idyllic and luscious establishment with a very special hook. Each rooms door is replaced by a large enchanted painting that creates different scenes to sleep in. Ranging from snugly tropical treehouses and luxurious campsites in the woods to frozen igloos and rocking boats on the sea. This place is sure to have a room for anyone to enjoy... if they have the coin to afford it.", 
"Fire and Ice Alehouse - This tavern features dueling bars on opposite sides of the room. One side icy and blue tones the other billowing flames and red tones. The two sides come together across the ceiling every hour to make 'fire water' that falls from a swirling cloud in the middle of the room. Fire Water is a delicious drink that also provides its drinker resistance to fire and ice for 24 hours.",
"The Toil & Trouble - Ran by a Neutral Witch, this place is filled with bad guys nearly 24/7. She doesn't seem to notice or care about anyone's alignments or what they get up to, unless there is any violence. If anyone causes a scene she descends on them, leaves them within an inch of their lives and bans them for life. If anyone tries to return, even in disguise, she knows and instantly kills them. She has no time for people that want to cause problems in her domain.", 
"The Rickety Witch - There aren't actually any witches in this bar, but the servers float around on brooms and are dressed up as them. The food is all themed around ingredients in potions. Rat tails, eyes of creatures, etc. Surprisingly tasty!", 
"The Dark Horse - This tavern is in complete darkness and any attempt to create a light either by magical or non-magical methods will fail. The staff all wear special goggles that allow them to see whilst serving tables and dealing with customers. It is billed as a unique experience to tantalise your senses, but in reality the owner is a once beautiful sorceress that has been horrifically disfigured by a curse and she hates being seen. She may employ the party to help lift the curse and in return offer them the tavern, which they can design however they wish.", 
"The Bam & Booze - The best way to describe this place is... confusing. The first thing you need to do is figure out how to get in! The door doesn't seem to open in the normal way. Do you try and go through a window? Down the chimney? Maybe there's a key hidden somewhere? It gets even more confusing once you get inside. All of the drinks are FREE! (As long as you can solve the puzzles the owner puts before you. Some may be in a different room of the tavern, whereas others could be simple riddles. Now you've had your fill and are ready to leave, how do you get out? Uh oh. It's a huge escape room! (I feel like this one will be really fun to flesh out for a DM!)", 
"Oasis - Stumbling through the desert you happen upon a large tent with camels tied up outside. Inside is a luxury bar with expensive drinks and attractive women. People are sitting around in beanbags, smoking who knows what from hookahs. Smells of delicious exotic foods are wafting through the air. It's very inviting. I'll let you DMs decide how real this place is! It could either be a mirage and not exist at all, a crappy little tent with horrible drinks under a major illusion or exactly as described. How evil are you feeling?", 
"The Meteorite Meat Shack - Located at the bottom of a huge impact crater from a meteorite, this self sustaining tavern is attached to a huge farm. Apparently the soil in the bottom of the crater is particularly fertile, leading to stronger crops and livestock! If your players do some investigating they will find out that the meteorite is still around, with a barn built around it in the dead centre of the crater. Of course it is the source of the mysteriously good crops and livestock. All it needs is a human blood sacrifice once a week...", 
"Cheep & Cheerful - A tavern filled with colourful birds of all different species flying around and perching on beams above you. You can buy seeds to feed the birds if you are so inclined. (They are also less likely to try and eat your dinner if you feed them!). No Cats or Tabaxi allowed.", 
"Hear Here! - Live music, 24/7, featuring all your favourite artists and bands; Coldflay, Goblin Manuel Miranda, Armour Class/Difficulty Class, Owlbear City, Bulette Zeppelin and more! (5gp entry)", 
"Muscles & Cockles - The only restaurant where you can pump iron and pump beer, from a tap. The beer, not the iron. The stronger you are, the heavier your discount. Upon entering you must perform a feat of strength, such as hitting a button with a mallet to try and ding the bell at the top or lifting something heavy, like barrels of beer or a rotund gentleman.", 
"The Holey Grail - Named after a grail that has been pierced hundreds of times, be it from arrows, explosions or a multitude of other things. Every night the tavern owners hold a contest to see who can create the most holes when it is tossed in the air. After 12 hours the grail has mysteriously repaired itself. (You could make this a magical item or simply have the owners replace it with a new one every day)", 
"Love Me Knot - This tavern is placed right there on the beach. But, oh no, the tides coming in! Never fear, the Love Me Knot floats and is tied down to heavy anchors beneath the sea floor to stop it from drifting away. Of course it still seems to move around the beach every other week to find a nice spot in the sun.", 
"Grogchamp - Winner of finest Grog 3 years straight, you'd be hard pressed to find a finer drink. However, the brewer is letting all the fame get to his head and is getting rather arrogant, challenging all around to try and create a better beverage. Are your party up to the task?", 
"The Leeky Crockpot - Everything is... leeky. Like, based on leeks. Leeks on your food, leeks used as stirrers in your drinks. There are even leeks on the beds! Where are all these leeks coming from? Now you smell like leeks. You scrub and you scrub, but still, the leeky reek remains. If your adventurers get a bed here for the night they take a charisma hit to all except those who love leeks, in which case they get a bonus.", 
"The Troll Booth - Simply pay your fee to cross the bridge and there surely won't be any trouble. They'll even throw in a hot cup of tea or coffee to make it worth your while. The trolls found that they were getting a lot higher return when they moved over to the service industry instead of the... ambush industry?", 
"Rise and Shine - You arrive at the tavern after a hard day's dungeon diving, just to find it is shut. Looking at the opening hours you see it is open from 6AM-7AM. Who on earth is drinking at 6 in the morning?? If they go during open hours they find it is absolutely heaving with customers, drunkards stumbling out after being in there for just a few minutes. Whilst inside you notice time is so much slower too. It will feel like hours pass whilst inside, even if you're only in there for 10 minutes of real time. (Maximum 12 hours in the 1 hour it's open, so 10 minutes real time would be 2 hours drinking time, for example)", 
"Above Par - Err, drinking and mini-golf? Yes please! A hole-in-one on the final hole wins you a free drink at the bar. Just be careful though, the more you drink, the harder it is to aim! (You may also refer to this place as 'The Golf Club')", 
"Beat it - As you enter you must play a tune on a drum kit. If you play it well everyone cheers, but if it's bad they will boo and jeer. If you refuse to play or roll a nat 1, you can't enter. If you roll a nat 20 you get a free beer or some other prize.", 
"Climber's Paradise - The only thing between you and a cold glass of ale is this 100-foot climbing wall.", 
"Paradice - Yes, Paradice. This club is so exclusive, you can only get in if you hit a DC20 Charisma check.", 
"Rambler's Gamble - Among the hills and slopes of this region rests an inn. An inn owned by a being addicted to gambling. Any travelers passing by may be tempted to enter for a refreshing drink and a hot meal, but they will find no prices on the menu. Maybe they would like to wager something for it instead?", 
"Gob Site - A wooden construct, stuck together with mud and held up with thin ropes, this absolute dive of a bar isn't somewhere you would choose to go, even in a pinch. A Goblin ran establishment, serving Goblins and ONLY Goblins... Unless you have something to make it worth their while.",
]
document.getElementById("Premise").innerHTML = searchArray(taverns);
};
function tavernName() {
    document.getElementById("Name").innerHTML = ""
    function tavernNamer() {
        let posts = [
            "Inn", "Tavern", "Bed and Breakfast", "Lodge", "Roadhouse", "Saloon", "Lounge", "Watering Hole", "Pub", "Taphouse", "Tavern & Inn", "Groghouse", "Ale Garden", "Canteen", "Rest House","Brewery", "Alehouse", "Meadery", "Tankard Tower", "Stout Stop", "Bottle & Barrel",
            ]
        let adjective = [
            "Airborne", "Smelly", "Slouching", "Giddy", "Brazen", "Bawdy", "Hobbled", "Wrinkled", "Grim", "Silent", "Broken", "Happy", "Sunken", "Quiet ", "Trodden", "Headless", "Burning", "Squawking", "Toothy", "Hungry", "Mighty", "Frisky", "Staggering", "Gutted", "Peckish", "Thirsty", "Artful", "Rare", "Steamy", "Drunk", "Glorious", "Crooked", "Blushing", "Insolent", "Enthusiastic", "Joyful", "Surprising", "Scorned", "Shameful", "Romantic", "Wise", "Sweet", "Surly", `Smoky`, `Tempered`, `Sanguine`, `Frosty`, `Elusive`, `Serene`, `Mirthful`, `Iridescent`, `Quaint`, `Vibrant`, `Mysterious`, `Ancient`, `Timeless`, `Playful`, `Twisted`, `Regal`, `Majestic`, `Fiery`, `Moonlit`, `Hallowed`, "Soothing", "Reverent", "Coarse", "Artificial", "Clumsy", "Clever", "Deaf", "Blind", "Paralyzed", "Prone", "Restrained", "Unconscious", "Invisible", "Petrified", "Poisoned", "Charmed", "Frightened", "Grappled", "Acrobatic", "Dextrous", "Intelligent", "Strong", "Athletic", "Deceitful", "Charismatic", "Insightful", "Intimidating", "Observant", "Natural", "Perceptive", "Performing", "Persuasive", "Stealthy", "Soft", "Dirty", "Dangerous", "Deadly", "Hidden", "Useful", "Dashing", "Alert", "Brave", "Large", "Tiny", "Wicked", "Tricky", "Mysterious", "Kind", "Handsome", "Fresh", "Frantic", "Foolish", "Adorable", "Clueless", "Cruel", "Elegant", "Friendly", "Laughing", "Lost", "Sleepless", "Salty", "Gnashing", "Winking", "Smiling", "Waving", "Ugly", "Old", "New", `Same ol'`, "Wealthy", "Bad", "Sleeping", "Bright", "Shiny", "Hairy", "Magic", "Burning", "Drunken", "Tipsy", "Quiet", "Devout", "Chivalrous", "Ancient", "Lucky", "Busy", "Fragile", "Cloudy", "Smooth", "Creepy", "Curious", "Grotesque", `Golden`, `Crimson`, `Jovial`, `Whispering`, `Slumbering`, `Luminous`, `Silent`, `Brooding`, `Gleaming`, `Rustic`, `Howling`, `Lonely`, `Roaring`, `Glimmering`, `Sable`, `Bewitched`, `Enchanted`, `Dreaming`, `Pensive`, `Spirited`, "Prickly", "Poor", "Putrid", "Puzzled", "Obnoxious", "Fierce", "Fancy", "Faithful", "Magnificent", "Enchanting", "Eager", "Easy", "Innocent", "Determined", "Horrible", "Wide-Eyed", "Victorious", "Uptight", "Unusual", "Troubled", "Thankful", "Terrible", "Tame", "Talented", "Strange", "Spotless", "Shy", "Repulsive", "Quaint", "Cursed", "Blessed", "Copper", "Gold", "Electrum", "Platinum", "Silver", "Ruby", "Sapphire", "Emerald", "Jade", "Opal", "Garnet", "Diamond", "Coral", "Moonstone", "Pearl", "Amber", "Ivory", "Obsidian" 
        ]
        let verb = [
            "Attack", "Run", "Rest", "Dive", "Strike", "Break", "Fall", "Point", "Recall", "Stand", "Walk", "Watch", "Wait", "Reply", "Request", "Delight", "Challenge", "Dream", "Guide", "Hunt", "Embrace", "Knot", "Jump", "Place", "Order", "Race", "Tap", "Yawn", "Wink", "Wash", "Signal", "Turn", "Bow", "Leap", "March", "Design", "Slight", "Display", "Fight", "Draft", "Code", "Exchange", "Drink", "Curse", "Battle", "Command", "Lie", "Boast", "Itch", "Kiss", "Guess", "Flight", "Doubt", "Demand", "Attempt", "Arrangement", "Climb", "Call", "Laugh", "Stack","Whisper", "Song", "Roar", "Dance", "Murmur", "Toast", "Seek", "Revel", "Sway", "Shout", "Rise", "Glisten", "Burn", "Cry", "Glance", "Plot", "Scheme", "Ponder", "Reflect", "Glow", "Shine", "Lurch", "Nest", "Roost", "Sail", "Row", "Forge", "Craft", "Howl", "Echo", "Tread", "Slide", "Ramble", "Spin", "Rally", "Stride", "Stalk", "Charge", "Glare", "Peek", "Blink", "Flare", "Huddle", "Cuddle", "Stretch", "Wave", "Cheer", "Charm", "Beckon", "Shimmer", "Gaze", "Lament",
        ]
        let verbing = [
            `Dancing`, `Singing`, `Lurking`, `Prancing`, `Laughing`, `Crying`, `Roaring`, `Glowing`, `Tapping`, `Sighing`, `Beckoning`, `Drifting`, `Fluttering`, `Sneezing`, `Grumbling`, `Snoring`, `Hooting`, `Skipping`, `Racing`, `Leaping`, `Humming`, `Whistling`, `Swaying`, `Dashing`, `Shivering`, `Hissing`, `Yearning`, `Flickering`, `Rumbling`, `Spinning`, `Vanishing`, `Giggling`, `Pouncing`, `Shining`, `Twirling`, `Groaning`, `Whispering`, `Slithering`, `Quivering`, `Echoing`
        ]
        let person = [
            "Guy", "Gal", "Abbot", "Refugee", "Acolyte", "Archmage", "Assassin", "Bandit", "Berserker", "Commoner", "Cultist", "Fanatic", "Gladiator", "Mage", "Preist", "Scout", "Spy", "Thug", "Veteran", "Dutchess", "Paladin", "Farmer", "Seaman", "Knight", "Scholar", "Seadog", "Jester", "Noble", "King", "Count", "Duke", "Emperor", "Thief", "Sailor", "Farmer", "Soldier", "Mercenary", "Priest", "Mage", "Scholar", "Beggar", "Bard", "Guard", "Drunk", "Wench", "Knight", "Merchant", "Smuggler", "Fool", "Druid", "Witch", "Traveler", "Fisherman", "Lady", "Harlot", "Bounty Hunter", "Gardener", "Gambler", "Prince", "Princess", "Brother", "Father", "Sister", "Mother", "Pirate", "Journeyman", "Chieftain", "Lord", "Miller", "Archer", "Crossbowman", "Lumberjack", "Miner", "Hunter", "Villager", "Settler", "Butcher", "Oracle", "Pilgrim", "Courier", "Hero", "Necromancer", "Sorcerer", "Wizard", "Barbarian", "Ranger", "Fighter", "Monk", "Warlock", "Summoner", "Arcanist", "Blood Hunter", "Cleric", "Rogue", "Artificer", "Outlander", "Exile", "Shepherd", "Nomad", "Explorer", "Hermit", "Mystic", "Prophet", "Tailor", "Blacksmith", "Brewer", "Alchemist", "Scribe", "Librarian", "Healer", "Tinkerer", "Chandler", "Fletcher", "Mason", "Cobbler", "Potter", "Weaver", "Baker", "Coachman", "Enchanter", "Shipwright", "Carpenter", "Falconer", "Dancer", "Troubadour", "Silversmith", "Goldsmith", "Conjurer", "Illusionist", "Evoker", "Diviner", "Geomancer", "Shaman", "Tribesman", "Champion", "Elder", "Herald", "Beasttamer", "Beastmaster", "Tutor", "Innkeeper", "Stonemason", "Leatherworker", "Armorer", "Weaponsmith", "Matron", "Patron", "Steward", "Maiden", "Reaper", "Seer", "Charmer", "Mourner", "Vagabond", "Emissary", "Apostle", "Diplomat", "Ambassador",
        ];
        let place = [
            "Swamp", "Mire", "End", "Bridge", "Gate", "Road", "Solace", "Haven", "Rest", "Paradise", "Fort", "House", "Home", "Venture", "Joint", "Hut", "Repose", "Keep", "Garden", "Room", "Sanctum", "Retreat", "Asylum", "Hideaway", "Refuge", "Shelter", "Haunt", "Shack", "Den", "Clearing", "Dungeon", "Castle", "Cottage", "Dungeon", "Field", "Camp", "Lean-To", "Mountain", "Cave", "Town", "City", "Lake", "Pond", "Lair", "Chamber", "Hovel", "Stall", "Grove", "Cove", "Harbor", "Port", "Quay", "Falls", "Hollow", "Meadow", "Ford", "Crossing", "Forest", "Woods", "Heath", "Crag", "Peak", "Valley", "Dale", "Ridge", "Bank", "Coast", "Shoal", "Brook", "Stream", "River", "Bend", "Isle", "Canyon", "Desert", "Oasis", "Beach", "Hill", "Fen", "Marsh", "Thicket", "Glade", "Pasture", "Prairie", "Tundra", "Waste", "Terrace", "Plateau", "Glen", "Springs", "Bay", "Lagoon", "Reef", "Grotto", "Barrows", "Ruins", "Tower", "Fortress", "Monastery", "Temple", "Shrine", "Altar", "Bazaar", "Market", "Square", "Arena", "Alcove", "Lodge", "Palace", "Mansion", "Villa", "Manor", "Farm", "Orchard", "Vineyard", "Brewery", "Mill", "Smithy", "Stables", "Wharf", "Dock", "Outpost",
        ];
        let thing = [
            "Whistle", "Anchor", "Bench", "Bramble", "Nail", "Scale", "Bugle", "Keystone", "Blight", "Hook", "Tree", "Flower", "Drum", "Buckle", "Chair", "Table", "Spoon", "Fork", "Axe", "Sword", "Shield", "Armor", "Bag", "Door", "Stash", "Bed", "Bunk", "Bedroll", "Barrel", "Keg", "Crate", "Box", "Pot", "Vial", "Arrow", "Broom", "Shovel", "Pillow", "Hearth", "Candle", "Lantern", "Mug", "Cup", "Tankard", "Bottle", "Plate", "Plow", "Pot", "Pan", "Lamp", "Wagon", "Spoke", "Rug", "Hammer", "Anvil", "Forge", "Goblet", "Chest", "Wardrobe", "Cellar", "Beer", "Ale", "Mead", "Wine", "Vodka", "Feather", "Oar", "Brandy", "Cask", "Harp", "Lute", "Necklace", "Bracelet", "Comb", "Mantle", "Crown", "Ring", "Oil", "Potion", "Gem", "Scroll", "Wand", "Bead", "Horseshoe", "Pike", "Bow", "Slippers", "Trident", "Brooch", "Amulet", "Pipe", "Figurine", "Deck", "Circlet", "Fan", "Boots", "Quiver", "Helm", "Gloves", "Belt", "Cape", "Dagger", "Shackles", "Horn", "Staff", "Book", "Wings", "Bands", "Crystal Ball", "Carpet", "Cask", "Manual", "Tome", "Flask", "Treasure", "Map", "Artifact", "Trap", "Dart", "Javelin", "Spear", "Halberd", "Hoard", "Key", "Stone", "Talisman", "Scimitar", "Apparatus", "Bracers", "Bowl", "Chime", "Decanter", "Card", "Mail", "Elixer", "Boat", "Ship", "Hat", "Clothes", "Headband", "Haversack", "Mirror", "Mace", "Philter", "Periapt", "Robe", "Rope", "Saddle", "Glue", "Well", "Trinket", "Statue", "Hankercheif", "Locket", "Bone", "Skull", "Sickle"
        ];
        let monster = [
            "Aarakocra", "Aboleth", "Angel", "Animated Object", "Animated Weapon", "Ankheg", "Azer", "Banshee", "Basilisk", "Behir", "Beholder", "Blight", "Bugbear", "Bulette", "Bullywug", "Cambion", "Carrion Crawler", "Centaur", "Chimera", "Chuul", "Cloaker", "Cockatrice", "Couatl", "Crawling Claw", "Cyclops", "Darkmantle", "Death Knight", "Demilich", "Demon", "Devil", "Dinosaur", "Displacer Beast", "Doppleganger", "Dracolich", "Shadow Dragon", "Dragon", "Dragon Turtle", "Drider", "Dryad", "Duergar", "Elemental", "Empyrean", "Ettercap", "Ettin", "Faerie Dragon", "Flameskull", "Flumph", "Fomorian", "Fungi", "Galeb Duhr", "Gargoyle", "Genie", "Ghost", "Giant", "Gibbering Mouther", "Gith", "Gnoll", "Goblin", "Golem", "Gorgon", "Grell", "Grick", "Griffon", "Grimlock", "Hag", "Half Dragon", "Harpy", "Hell Hound", "Helmed Horror", "Hippogriph", "Hobgoblin", "Homunculus", "Hook Horror", "Hydra", "Intellect Devourer", "Invisible Stalker", "Jakalwere", "Kenku", "Kobold", "Kraken", "Kuo-Toa", "Lamia", "Lich", "Lizardfolk", "Lycanthrope", "Magmin", "Manticore", "Medusa", "Mephits", "Merfolk", "Merrow", "Mimic", "Mind Flayer", "Minotaur", "Modron", "Mummie", "Myconid", "Naga", "Nightmare", "Nothic", "Ogre", "Oni", "Ooze", "Orc", "Otyugh", "Owlbear", "Pegasus", "Peryton", "Piercer", "Pixie", "Psuedodragon", "Purple Worm", "Quaggoth", "Rakshasa", "Remorhazes", "Revenant", "Roc", "Roper", 
            "Rust Monster", "Sahuagin", "Salamander", "Satyr", "Scarecrow", "Shadow", "Shambling Mound", "Shield Guardian", "Skeleton", "Slaadi", "Specter", "Sphinx", "Sprite", "Stirge", "Succubus", "Incubus", "Terrasque", "Thri-kreen", "Treant", "Troglodyte", "Troll", "Umber Hulk", "Unicorn", "Vampire", "Water Weird", "Wight', `Will-o'-Wisp`, 'Wraith", "Wyvern", "Xorn", "Yeti", "Yuan-ti", "Yugoloth", "Zombie", "Ape", "Awakened Tree", "Awakened Shrub", "Axe Beak", "Baboon", "Badger", "Bat", "Black Bear", "Blink Dog", "Blood Hawk", "Boar", "Brown Bear", "Camel", "Cat", "Constrictor Snake", "Crab", "Crocodile", "Death Dog", "Deer", "Dire Wolf", "Draft Horse", "Eagle", "Elephant", "Elk", "Flying Snake", "Frog", "Giant Ape", "Giant Badger", "Giant Bat", "Giant Boar", "Giant Centipede", "Giant Constrictor Snake", "Giant Crab", "Giant Crocodile", "Giant Eagle", "Giant Elk", "Giant Fire Beetle", "Giant Frog", "Giant Goat", "Giant Hyena", "Giant Lizard", "Giant Octopus", "Giant Owl", "Giant Poisonous Snake", "Giant Rat", "Giant Scorpion", "Giant Sea Horse", "Giant Shark", "Giant Spider", "Giant Toad", "Giant Vulture", "Giant Wasp", "Giant Weasel", "Giant Wolf Spider", "Goat", "Hawk", "Hunter Shark", "Hyena", "Jackal", "Killer Whale", "Lion", "Lizard", "Mammoth", "Mastiff", "Mule", "Octopus", "Owl", "Panther", "Phase Spider", "Poisonous Snake", "Polar Bear", "Pony", "Quipper", "Rat", "Raven", "Reef Shark", "Rhinoceros", "Riding Horse", "Saber-Toothed Tiger", "Scorpion", "Sea Horse", "Spider", "Bat Swarm", "Insect Swarm", "Poisonous Snake Swarm", "Quipper Swarm", "Rat Swarm", "Raven Swarm", "Tiger", "Vulture", "Warhorse", "Weasel", "Winter Wolf", "Wolf", "Worg"
        ];

        let template = [
            `The ${searchArray(person)}'s ${searchArray(thing)}`,
            `The ${searchArray(person)}'s ${searchArray(place)}`,
            `The ${searchArray(person)}'s ${searchArray(monster)}`,
            `The ${searchArray(person)}'s ${searchArray(verb)}`,
            `The ${searchArray(person)}'s ${searchArray(verbing)}`,
            `The ${searchArray(person)} at the ${searchArray(place)}`,
            `The ${searchArray(person)} and the ${searchArray(thing)}`,
            `The ${searchArray(person)} and ${searchArray(monster)}`,
            `The ${searchArray(person)} and the ${searchArray(monster)}`,
            `The ${searchArray(person)} and ${searchArray(person)}`,
            `The ${searchArray(person)} and the ${searchArray(person)}`,
            `The ${searchArray(person)}'s ${searchArray(adjective)} ${searchArray(verb)}`,
            `The ${searchArray(person)}'s ${searchArray(adjective)} ${searchArray(verbing)}`,
            `The ${searchArray(person)}'s ${searchArray(adjective)} ${searchArray(thing)}`,
            `The ${searchArray(person)}'s ${searchArray(adjective)} ${searchArray(monster)}`,

            `The ${searchArray(monster)}'s ${searchArray(thing)}`,
            `The ${searchArray(monster)}'s ${searchArray(place)}`,
            `The ${searchArray(monster)}'s ${searchArray(verb)}`,
            `The ${searchArray(monster)}'s ${searchArray(verbing)}`,
            `The ${searchArray(monster)}'s ${searchArray(adjective)} ${searchArray(verb)}`,
            `The ${searchArray(monster)}'s ${searchArray(adjective)} ${searchArray(verbing)}`,
            `The ${searchArray(monster)}'s ${searchArray(adjective)} ${searchArray(thing)}`,
            `The ${searchArray(monster)} in the ${searchArray(place)}`,
            `The ${searchArray(monster)} and the ${searchArray(monster)}`,
            `The ${searchArray(monster)} and the ${searchArray(thing)}`,

            `The ${searchArray(adjective)} ${searchArray(thing)}`,
            `The ${searchArray(adjective)} ${searchArray(place)}`,
            `The ${searchArray(adjective)} ${searchArray(monster)}`,
            `The ${searchArray(adjective)} ${searchArray(person)}`,
            `The ${searchArray(adjective)} ${searchArray(verb)}`,
            `The ${searchArray(adjective)} ${searchArray(verbing)}`,

            `The ${searchArray(thing)} ${searchArray(place)}`,
            `The ${searchArray(thing)}'s ${searchArray(verb)}`,
            `The ${searchArray(thing)}'s ${searchArray(verbing)}`,
            `The ${searchArray(thing)}'s ${searchArray(adjective)} ${searchArray(verb)}`,
            `The ${searchArray(thing)}'s ${searchArray(adjective)} ${searchArray(verbing)}`,
            `The ${searchArray(thing)} and ${searchArray(thing)}`,
            `The ${searchArray(thing)} and the ${searchArray(monster)}`,

            `The ${searchArray(place)}'s ${searchArray(thing)}`,
            `The ${searchArray(place)}'s ${searchArray(verb)}`,
            `The ${searchArray(place)}'s ${searchArray(verbing)}`,
            `The ${searchArray(place)}'s ${searchArray(adjective)} ${searchArray(verb)}`,
            `The ${searchArray(place)}'s ${searchArray(adjective)} ${searchArray(verbing)}`,
            `The ${searchArray(place)} at the ${searchArray(place)}`,

            `The ${searchArray(verbing)} ${searchArray(thing)}`,
            `The ${searchArray(verbing)} ${searchArray(place)}`,
            `The ${searchArray(verbing)} ${searchArray(monster)}`,
            `The ${searchArray(verbing)} ${searchArray(person)}`,
            `The ${searchArray(verbing)} ${searchArray(verb)}`,
            `The ${searchArray(verbing)} and ${searchArray(verb)}`,

            `The ${searchArray(place)}`,

            `The ${toWords(3+rollDice(97))}${searchArray(monster)}s`,
            `The ${toWords(3+rollDice(97))}${searchArray(thing)}s`,
            `The ${toWords(3+rollDice(97))}${searchArray(place)}s`,
            `The ${toWords(3+rollDice(97))}${searchArray(person)}s`,
            `The ${toWords(3+rollDice(97))}${searchArray(verb)}s`,
            `The ${toWords(3+rollDice(7))}${searchArray(monster)}s`,
            `The ${toWords(3+rollDice(7))}${searchArray(thing)}s`,
            `The ${toWords(3+rollDice(7))}${searchArray(place)}s`,
            `The ${toWords(3+rollDice(7))}${searchArray(person)}s`,
            `The ${toWords(3+rollDice(7))}${searchArray(verb)}s`
        ]
        let chance = rollDice(100)
        if (chance < 33) {
        return searchArray(template) + " " + searchArray(posts)
        } else {
        return searchArray(template)
        }
    }
    let a = [tavernNamer(),tavernNamer(),tavernNamer(),tavernNamer(),tavernNamer(),]
    loopPrintList(a,"Name")
};
function findF1() {
function getFlavorOne() {
let tavernFlavor1 = [
"A 10-year old girl is running the tavern. Everybody is afraid of her.", 
"collection of fine plates hangs from the wall.", 
"A finely carved but dusty statue lies in a dark corner.", 
"A game of horseshoes in on going.", 
"A group is quietly sitting, listening to a man telling a story.", 
"A group surrounds two large men arm wrestling, they appear to have been there for quite a while, sweat is dripping from them.", 
"A large amount of cats covers nearly every surface, they are very skilled at dodging blows.", 
"A mediocre bard is performing to an ambivalent crowd.", 
"A patron is sleeping on the floor, cuddling an empty tankard.", 
"There is a playpen for small children near the bar.", 
"There is a large and high stage, both clean and deserted.", 
"There is a small library in the corner.", 
"There is a small shrine at the end of the bar.", 
"There is a small wrestling ring at the center, currently unused but fresh blood is visible.", 
"In a dark corner lies a broken table and chairs, when looking closer you can see still wet blood.", 
"A three way drinking contest is in progress, a fourth participant is under the table, snoring.", 
"A very good looking waiter is getting a lot of attention from female patrons.", 
"A very nice and affectionate dog is just begging for some attention.", 
"A very pretty waitress is singing loudly while she works, she is a terrible singer but no one dares say so.", 
"A waiter with a peg leg is struggling to walk while balancing glasses.", 
"A waitress with a peg leg walks with impressive grace.", 
"An intricate slide and pulley system allow beer to be delivered to every table without leaving the bar.", 
"As you walk in a food fight breaks out.", 
"At random times a carved duck will make a sound. However, it will not quack but instead mostly moo or make other barnyard animal noises.", 
"Behind the bar is a wired skeleton,", 
"If asked about it the owner, says it's [PC's] father.", 
"Behind the bar is an extensive collection of rare drinks.", 
"The fireplace is massive and burns so hot that most give it a wide breadth.", 
"A large birthday party is ongoing, a candle laden cake is being lit.", 
"There is already a party of adventurers, they are celebrating the accomplishment of a quest.", 
"The inn is completely spotless.", 
"In a dark corner there is a group playing a game of dice, they are trying to be subtle and failing.", 
"There is a single long communal table.", 
"Hunting trophies are displayed prominently all the walls.", 
"Loud and continuous swearing can be heard from the kitchen.", 
"Many weapons are hanging on the walls.", 
"Numerous paintings of the owners with large fish hang behind the bar.", 
"On the roof is a large telescope.", 
"On the top shelf there is a series of jars with various body parts.", 
"A one armed waiter has a prosthetic that allows them to carry dozens of glasses at once.", 
"One of the wall is a quite elaborate fresco.", 
"One of the walls is a giant, living, tree.", 
"Pelts of various animals line the walls and cover the floor.", 
"Huge heavily weaponized warforged innkeeper that has higher stats than everyone in the entire campaign.", 
"All the furniture is made of stone.", 
"The bar is circular and at the center of the room.", 
"The bar is made of marble.", 
"The drinks come in wooden boots.", 
"The inn has a omnipresent shrimp theme.", 
"The inn has a watch tower attached.", 
"The inn has its own moat, about half a meter wide, complete with miniature drawbridge.", 
"The inn has two large tapestries, rotten but still quite impressive.", 
"The inn is made from a large boat.", 
"A two legged fish being is sitting at the bar. It has a clear bowl covering its head that is 9 / 10 ths full of water. It has a drink in front of it and you think to yourself...how is he going to drink that damn drink?", 
"The inn is mostly underground.", 
"The inn is lit by candles that give off a green light.", 
"The inn is patroned by a knightly order.", 
"The inn is patroned by hardened criminals.", 
"The inn is patroned by several nobles.", 
"The inn is patroned by the local law enforcement.", 
"The inn is quite small but has four floors.", 
"The inn used to be a church, the bar contains the altar.", 
"The inn used to be a fort, the windows are arrow slits.", 
"The inn uses glasses hand made by the owner.", 
"The owner is distinctly foreign.", 
"The owner practices juggling when they have a free moment, they are still pretty bad.", 
"The owner whistles when cleaning glasses, it is quite lovely.", 
"The owners are a pair of identical twins, they are completely indistinguishable.", 
"The whole bar is as ramshackle as can be, it looks like what was once a number of smaller clustered houses that have had rooftops and walls bridged between them into one large sprawling single floored inn with several rooms.", 
"The tables are all tree stumps coming through the floor.", 
"The tables are on a level a couple of feet lower than the bar.", 
"There is a taxidermied head of a really rare creature on the bar.", 
"The whole front room smells, the odor is indescribable, but not unpleasant.", 
"The windows are stained glass.", 
"There are dozens of lush potted plants.", 
"There’s a rotting corpse sitting next to he door looking at its watch. When asked about it, the innkeeper will say' he’ s waiting for someone' and tell you to mind your business when asked further.", 
"There are two rival bars in the same inn, they both work for the inn but get a share of their revenue.", 
"There is a couple kissing at the bar, they seem quite passionate and very inexperienced.", 
"There is a fireplace in all four corners of the front room.", 
"There is a large stone and crystal collection behind the bar.", 
"There is a large window in the ceiling.", 
"There is a large, well crafted grandfather cloak behind the bar.", 
"There is a man playing three shells and a pea in the corner.",
"There is a parrot at the bar, it whistles continuously.", 
"There is a rusting suit of armor right as you open the door, the arms are raised, wielding a sword.", 
"There is a small stream going through the front room.", 
"Several animal skulls lay on the bar, each one has a burning candle inside.", 
"There is a two headed dog, he well loved by everyone.", 
"There is a two tailed cat.", 
"There is a water well at the center of the front room.", 
"All drinks are served in wooden tankards that, upon closer inspection, are carved with the likenesses of a-great heroes of a long-forgotten age b-great villains of a long-forgotten age c-an enormous serpent, coiled around the mug and swallowing its own tail d-countless beetles which, after looking away, never seem to be where they were when you looked at them last e-a menagerie of animals that don't look out of the norm, but if asked, no one seems to know exactly what they are.", 
"There is an expensive looking chandelier hanging from the surprisingly high ceiling.", 
"There is a bachelorette party in progress.", 
"Almost every flat surface has one or more figurines or trinkets that the owner loves to collect. They'll often allow patrons to barter for their meal with a new trinket.", 
"A large pit filled with sand takes up a good portion of floor space. Several patrons are leaning on the railing and taking bets. Roll 1 d6 for fighters 1.Humanoids 2.Dogs 3.Chickens 4.Large lizards 5.Monstrous humanoids 6.Undead vs a mortal.", 
"A man is on one knee in front of a woman, he holds out an open box with a ring in it, the inn is completely silent.", 
"A woman is currently giving birth, everyone else seems to be either panicking or undisturbed.", 
"Everyone in the inn is standing up and are separated in two groups facing each other, they seem to be having an argument.", 
"The bar runs across the center of the front room, splinting it into two, while one side is loud and rowdy the other is calm and dignified.", 
"An unknown public figure is staying at the inn, all their servant are in the front room.", 
"The owner of the inn has a orphan Owlbear who roams around eating food people spill.", 
"The walls are all painted pink, everyone refuses to talk about it.",
]
return searchArray(tavernFlavor1)
}
document.getElementById("F1").innerHTML = getFlavorOne();
};
function findF2() {
function getFlavorTwo() {
let tavernFlavor2 = [
"This tavern has a map of the world painted on the wall around the fireplace. Visiting travelers leave notes stuck in the cracks near various places with a bit of information about that area.", 
"A taxidermy Beholder hangs from the ceiling in the center of this tavern. It’s not a real Beholder. It was made out of leather and paint, but it’s up high enough that no one can get a close look.", 
"The Bartender and serving girls all wear bright green and gold floral sashes over their left shoulders, draped across and tied at the right hip. A few patrons wearing similar sashes drink for free.", 
"Dozens of floating orbs of light, the size of goose eggs, drift lazily around the tavern, giving off plenty of illumination-to avoid dark corners and sinister plotting.", 
"Benches mounted to the walls assure that every patron has a protected back. There are no stools or seats at the bar. No one will be getting backstabbed at this establishment.", 
"Knee high platforms crisscross the tavern floor so that the Halfling servers can easily fill mugs and clear tables. It does make for a tripping hazard for tall folk, so watch yer step. Anyone involved in a bar brawl will have disadvantage on attack rolls.", 
"This tavern reeks of pickled fish. The owner cures them himself and sells them to travelers in sealed clay pots. The pots do little to mask the odor.", 
"An elaborate tapestry hangs behind the bar. Rumor has it that there are secret symbols and writings embroidered into the pattern. Some say it's a treasure map. Others say it's magical incantations for powerful spells. And others claim it hides the password for a secret society. The barkeep says she just thought it was pretty.", 
"A life sized statue behind the bar of a human man covering his eyes is supposedly the original owner of the tavern. Legend has it he fell in love with a Medusa and she accidentally turned him to stone. Many spellcasters over the years have tried to reverse the condition, yet failed.", 
"The owner is a Firbolg. Tables are ten feet high. The chairs have ladders attached so shorter patrons can reach their drinks. The smallest mug holds a gallon of ale. A bowl of soup can feed a family of six humans.", 
"The proprietor of the tavern is a shifty old dwarf, always looking over his shoulder and scanning the room. Occasionally he is spotted speaking to the bar itself as he wipes down the counter top. Whenever the fire in the hearth is dying, he runs his hand over the mantle, whispers to it in a comforting manner before the entire building shudders, creaks, strains, before letting out a groaning exhale and the fire is revitalized. Some believe the tavern itself is living.", 
"A weird contraption occupies an arcade that appears to be a slanted table, enchanted with fairy—and perhaps mechanical— lights. A spring propells a ball that is hastened and bounces around interacting with a tableux of pixies, live pixies, darting around doing pointless tasks under a glass surface. The tavernkeep calls it a 'pinball machine'. The current highscore is held by a person with the acronym BBEG.", 
"An enchanted lute provides a musical accompaniment to the tavern. It has a respectable repertoire, but one string is out of tune, making concentration checks difficult. The tavern owner despises bards, having his paramour swept off by one. So anyone offering to retune the lute might be met with violence.", 
"A dog. A friendly one. The unusual thing is that everyone sees the dog differently. A highlander Barbarian sees the dog as a longhaired red highland setter, but a Wood-Elf might see the dog as a black wolfhound, and a mountain Dwarf might see it as a small rat-terrier. This difference is unlikely to be noticed at the time, and only comes up during conversation later, after leaving the tavern.", 
"There are 5 doors around the bar each opens up to a different city and destroying an outside building does nothing but move the portal to a different building in said city. The doors might be locked or otherwise require permission (a fee perchance?) to use.", 
"A saloon style tavern with a modest stage up front where all the patrons can see. On Friday nights the astral diva sings her prophecies.", 
"The bar is associated with a local mages guild, and has magical brews on tap. Upon downing a pint, roll on wild magic table.", 
"The bar is knownfor its strong drinks, occasionally a drunken reveller will come in demanding 'hammerbrew', which will invariably knock them out for 1d4 hours (on a DC 25 con check) Hammerbrew is incredibly expensive and the barmaid demands to be paid in advance, including tip!", 
"The tavern has had enough of twitchy adventurers. All wood fittings have been burned to a blackened tone, and a large sign suggests any magic usage will lead to a ban from all establishments in the area. People are often thrown out for appearing to use magic, even if they aren’t. The tavern is that gun-shy.", 
"The bar is staffed with retired 'adventurers'. All are significantly mauled, scarred and most missing fingers, eyes, or limbs. Similarly battered adventurers will drink for free, in return for a tale to the general audience.", 
"The wall is covered with hundreds of mounted heads-some unsurprising, such as a troll or a small dragon-others more so, such as a blinking, it blinked, I swear, didn’t you see it? Half-Orc or...is that a baby?", 
"While normal appearing from the outside, inside the bar and tables are all moulded from one tree, which is rooted in the bar and has carefully been bent and flattened over hundreds of years to serve as a bar and tables. The tree is still alive and growing, with a leaf sprouting here and there.", 
"The entire tavern is curiously dusty, despite being well attended, some areas look like they have a decade of dust upon them. If dust is swept off an empty table, all regulars will groan, and a large number of days written in chalk on the bar will be wiped off.", 
"The mugs are enchanted to refill themselves when you snap your fingers. You still get charged for the refills though.", 
"The tavern is a renovated monastery. The grounds were hallowed such that the entire area is magically silent. Patrons come from near and far for the extraordinary peace and quiet it offers. Ordering food and drink can be a bit of a hassle though, having to pantomime eating or drinking, and being brought whatever is being served that day.", 
"A halfing sitting on a table playing a medium violin like cello. The Halfling is the owner, and not a very talented musician.", 
"The bar is situated on a pier, and has a lower level where patrons can fish and let their feet sit in the water, where small fish nibble on the skin harmlessly. The cook will fry up anything you catch for free!", 
"A lonely, windswept tavern on the coast is situated a little closer to the sea than the rest of the village. Behind the bar there 's a thin-toothed comb made out of a shell, and the bartender tends to become gloomy if asked about it.", 
"A tavern made by a master dwarven stonemason, each table and stool is a fully piece of stonework, which slides glassily across the floor on clever grooves hidden in the floor. Given a few minutes, you can arrange every table in the place into one long feast table, with the tables making a sort of zig-zag line.", 
"Strict No Adventurers policy-time for some Charisma checks.", 
"A friendly mastiff hound wanders around the tavern begging at tables for snuggles and scritches. Any adventurer that feeds it a piece of meat will find that the dog will make its way outside toward a treasure chest hidden in the dirt outside.", 
"A tavern tucked away in one of the hottest regions of Avernus. It’s name is the Icebox, and it is owned by a devil who has bound an ice elemental into eternal servitude. This tavern has a fireplace containing a magical blue flame that radiates cold, rather than heat. This same blue flame is also behind the bar, beneath an iron grate upon which several mugs sit. This keeps them frosty cold, and makes this tavern an area favorite. Devils like to visit here for a change of scenery.", 
"A coastal tavern built from a kraken’s skull. It’ s name is The Little Fish. This tavern is frequented by wild storytellers, who tell the truth about 25 % of the time.", 
"A 2-story tavern with a strange reputation, where patrons must pay a steep fee up front before entering. Once inside, players will see a strange black liquid dripping from several holes in the ceiling, which is being collected in large barrels beneath them. Patrons dip their mugs into these barrels and drink the liquid, which is delicious and quite intoxicating. Rumor has it that this liquid is the blood of a demon who is imprisoned upstairs. No one is allowed upstairs to find out.", 
"A tavern called 'The View' built right next to a beautiful but very loud waterfall. The tavern owner thought it was a smart business move to build next to the waterfall, but you can barely hear anything inside over the roar of the waterfall only meters away from the front door.", 
"All patrons must check their weapons at the door of this tavern, much like a coat check. You are given a numbered ticket and the weapon is stored away in a back room behind a curtain. Unbeknownst to the players, this tavern is notorious for 'accidentally' replacing high quality or magical weapons that have been checked with inferior duplicates.", 
"All the food and drink have a slightly off taste. Not to the point of inedibility, but enough to notice something's off about it. When asked the bartender just smiles and says everything's spiced with a 'special ingredient' here. An investigation will reveal the barkeep raises snails and uses their slime as a staple ingredient in all of the food. He uses the slime from his favorite snails for his regulars.", 
"The ceiling of the tavern is very high up, and rather than walk around the tables servers descend from above in a complicated harness system. Sometimes, when nobody's looking, a hook will descend and pull up especially drunk patrons.", 
"The owner/bartender was a merchant for many years and can't reset a good haggle. A large chalkboard behind the bar displays a list of the lowest prices customers have managed to get out of him this evening, complete with a chalk portrait of the current #1 cheapskate.", 
"Each table is attached to a little boat that floats down a man-made underground water course. Patrons are offered the choice between the tunnel of love or the waterfall course at the entrance.", 
"A strange tavern that appears only in the most remote places. Wanderers May enter and find other adventurers from far off places just as confused as they are. There is no tavern keeper but hot food and drink is ready on the tables and the kitchen is open for those who cook. The upstairs rooms have comfy beds with silk sheets and fur blankets.The strangers are allowed one night to rest and feast with one another as they tell tales of their adventures and the bizarre places they’ve found the tavern. Come morning the party will awaken in a clearing where the tavern once stood. The strangers are gone and they are all awaken clean and refreshed.", 
"One of the servers looks a bit like a monkey, their arms dragging on the floor. On closer inspection... She is a monkey. You might not always get exactly what you ordered, but if you dare complain this monkey will show their teeth, and you really don't want to fight her.", 
"This tavern is completely made out of ice. Even the glasses are carved from ice. The food is pretty cold too. If a fight breaks out, for every move action, make a dex saving throw or slip (become prone).", 
"When you come in, you're in luck: there's exactly enough seats left for your party! Turns out this tavern scales with the number of patrons in it, and is always exactly big enough to have that bustling, slightly cramped tavern feel. The servers and cooks are real however, so if too many people come in at once, you might have to wait for your meal for a bit!", 
"This rather expensive, high-end tavern serves dozens of traditional clay oven dishes. All of these are hand - made by the clay warforged bartender, straight from the oven embedded in their chest.", 
"Beverage faucets are fashioned to resemble a wooden snake spitting the liquid out.", 
"Area of the bar uses oddly shaped sitting areas and tables to allow for centaurs or other non - humanoid races to be there.", 
"Main area of the bar is designed like a circle so that there are no corners of the bar for edgy people to brood in.", 
"Tavern secretly hides 10 coin-sized wooden emblems across it every morning. If you find one, you can exchange it for a bottom-shelf drink of your choice. Tavern's decorated enough that there are many spots for these to be hidden in. Players can find these with perception/search checks, with them being more likely to find them the earlier in the morning it is (as less of them have already been found).", 
"The menu(or barkeep/barmaid) insist on pairing everything on the menu with a spiced meat. You want ale? There's a meat for it. Wine? There's a meat for it. You just want to order some gruel and be left alone? Too bad! There's a meat for that!", 
"Soft music fills the room, just over the din of the occupants. Each patron, however, hears a different tune/instrument to fit their mood/preference.", 
"The wait staff are all benevolent changelings that shift a slight detail every time they leave direct sight. For example: they first meet a blonde, mustachioed barkeep. When he returns with drinks, he's clean shaven. He dips below the bar to fill from the tap and emerges with darker hair.", 
"This tavern is run by gnomes who have goliaths as slaves. The goliaths are completely cowed by their masters and their little tiny whips.", 
"Upon entering you must sign up to take part in a barroom brawl.People who arrive late have to take less desirable positions in the fight, such as 'first one to get thrown through the window.'", 
"If anyone orders anything other than the bartender’s personal brand of brew, all other patrons are allowed to throw darts at them.", 
"A cross shaped tavern with the bar in the middle, the PCs people always want to emerge from shadowy corners, this one has 8.", 
"Your food/drinks are brought to you via tortoise-literally the opposite of Fast Food", 
"Cats freely roam the Tavern looking for treats and cuddles.", 
"No chairs, we eat on the floor with low tables, prone, on your belly, propped up with your elbows.", 
"The tavern is segregated by race, you get a discount if you sit in your designated area, charged double if you don’t.", 
"The Tavern is floating on a lake in the middle of town?", 
"There is some strange skeleton mounted to the wall above the fireplace. Nobody knows what kind of creature it belongs to or where it came from, but it's been there for so long that patrons just accept and celebrate its existence.", 
"A massive, politically neutral tavern and inn that is enchanted to prevent any and all acts of violence within its walls. It allows patrons to rest free from conflict or worry, no matter what their political, religious, or racial affiliation. It may also serve as the perfect hideout for someone with enemies, provided that they remain in the tavern.", 
"One too many exotic-wood wall panels line her tavern's walls -- they slinky the halls, flipping from beam to beam so that they all tangentially fit. You have to wait until the door you walked through lines up with a wall panel before you can leave--the 24 clocks for the 24 doors to the 24 regions are listed by name on the wall next to the tricetails specials.", 
"You are sucked (resist: as Mighty or better) into the bar the moment you push on it.", 
"Rumour has it, you are to be either stupid drunk or else heavily caffeinated while you exit through the door because otherwise crossing its threshold causes a pounding headache that plays echoes of the pounding tavern walls throughout the rest of the day intensifying and diminishing with light levels (as: Light-Sensitive).", 
"A dwarves mechanic runs the bar and has a set of three automatons in the corner that when he presses a stone button under the bar they spring to life and start lifelessly playing a beautiful song. The bartender usually leaves it off and has a somber look whenever the tavern fills up and he puts them on.", 
"An ancient, but magical crossbow over the bar that has patrons split on whether or not it works or not (spoiler alert-it does), and rumors of the tavern owner's dangerous past. Bonus points if he is an elderly unassuming gentleman.", 
"The Any Port tavern has been enchanted so that, on the inside, it seems like there's a storm raging outside no matter the weather.", 
"Fake of a unique and well known artifact from the world. Half the visitors think it’s the real thing, while the other half are certain it’s not...", 
"The bar is managed by a wizard and their apprentices. Unseen servants carry orders between tables while apprentices man the kegs of magically enhanced brew. Many of the doors and passageways of the tavern may be used as portals if the proper keys and rituals are performed.", 
"This tavern is known for the fire walking competition it hosts. A bed of coals is rests in the center of the tavern and is carefully tended by its staff. Those who win the competition typically get free drinks and meal for the night.", 
"The tavern has a archery/axe throwing range in back that is often used by customers to settle bets, disputes, or just have a good time.", 
"A long dice table making up a section of the bar - maybe the entire bar is a dice table, and you roll to determine the price of your drink.", 
"All staff are Dragonborn, tavern could be called scales and ales", 
"The barkeep is a dwarf on stilts, but the stilts are being hidden by the bar itself, giving the bartender the appearance of a dwarf with disproportionately long legs.", 
"The cursed candle is a bar that operates completely in the dark, as it was built for those with sunlight sensitivity. The owner is a gnome who sells goggles of dark vision at a fair price.", 
"In this tavern, anyone can steal your drink without punishment.", 
"A tavern which is entirely ran by tiny servants (From the spell in xanathars guide) the owner of the tavern is sorcerer who doesn’t really know how his/her powers work but if he/she drips his/her blood onto an object it turns into a tiny servant.", 
"Other patrons are playing their own ttrpg, but if inspected the party realizes that they are playing a very similar adventure to their own. Too similar to be a coincidence.", 
"Tavern oven use a dragon that breaths fire to heat up the food, which gives a special magical flair to the food (whether the dragon is willing or is chained and forced to do this is up for the GM to decide)", 
"Shady alchemist behind the tavern will sell sleeping potions and other concoctions for people to buy and spike drinks with. Tavern owners are aware of this man, but aren't doing anything about him due to him sharing some of his profits with them.", 
"Dart which is a +2 magic item and made more durable by the enchantment is hidden among the other darts for the tavern's dart game. No one else knows about it or how it got there, but it can be found with Detect Magic and stolen.", 
"Drinking glasses are prismatic and more durable. It's actually a side-business the tavern has going for it, you can buy them for 1 gold per glass and will be charged for breaking them (could have qualities other than being prismatic, point is that they're special and could make for a good souvenir)", 
"The bar is themed as a [monstrous race] bar. The staff all dress up and enact stereotypes, poorly.", 
"The tavern is located in one of the poorer parts of the town but uncharacteristically lavish chandeliers, well-kept and polished countertops, and high-quality alcohol and entertainment make it a popular hideout for the city’s nobility (perhaps they fund the establishment).",
"There is a weapon or pair of weapons hung over the hearth or bar. They relate to the name of the bar (e.g.a Winchester rifle for the Winchester pub in Shaun of the Dead).", 
"The tavern is on a cliff side with a part of the tavern sticking out over the water. For a small fee, the bartender can open a trap and make you fall in the water (the falling space has been cleared of anything that could harm the patrons, or is it?). It is considered to be a popular form of entertainment amongst the regulars. The trap can also be used to clear drunken patrons and there is staff to help you out of the water.", 
"The **Carry Oak E' pub is run by a failed Bard who opens the stage to anyone who wants to sing popular songs regardless of their talent or voice quality.", 
"The Mead Mystique requires all guests to wear masks. It is a somewhat shady, but otherwise classy place. Much of the clientele is the city elite looking for excitement, but the prices allow a working class crowd for them to blend in with.", 
"The tavern stands at sea level on poles over the ocean. The floor gives way to many pools, and the set-up facilitates that creates of land and sea may grab a drink & bite together. Humans, Elves, Grippli, Merfolk, Sahuagin. The bowser is Yurian.", 
"The tavern is a mimic. The door is the mouth. The mimic might still be alive (and tame?) or just the corpse. Better yet, Rumor has it, the mimic is just sleeping...", 
"The tavern teleports to a set town in a series of locations each Thursday at noon. Each town has a cleared plot of land reserved for it's arrival. It is always very popular as it is used to transport unique supplies from each town in the cellar. The tavern owner is very rich, very friendly, and neutral good.", 
"The Elemental Plane of Alcohol is a tavern run by a mad mage and is located in a demiplane.Every drink gives a wildmagic effect.", 
"The Tavern is in a cave and is run by a lich and his henchmen. Its regular customers are humanoid monsters like Ogres, Bugbear, and Hobgoblins.",
]
return searchArray(tavernFlavor2)
}
document.getElementById("F2").innerHTML = getFlavorTwo();
};
function findInsult() {
function insultGenerator() {
function searchArray(array) {
return array[Math.floor(Math.random() * array.length)];
}
let primeLine = [
"That outfit does little to disguise your unfortunate bone structure", 
"Your pedigree lacks distinction", 
"None shall mourn your passing", 
"Your skills are weak", 
"I question the moral character of your mother", 
"You'd be worth more if you were ground up and used for food", 
"Your net worth is far below average", 
"Your hygeine leaves much to be desired", 
"Your lover craves my ministrations fortnightly", 
"You reek of failure", 
"You have no friends and your family hates you,", 
"I doubt that you even lift", 
"Egad, I can smell you from here", 
"You are an embarrassment to your species", 
"You are entirely without value", 
"The immensity of your deficiency consistenty bewilders me", 
"I'm almost impressed at how hard you're trying", 
"You are completely alone and insignificant in the vast, cold expanse of the Multiverse", 
"Your countenance and your posterior are nigh indistinguishable", 
"You 've got posture worse than an arthritic gnoll", 
"You are unloved", 
"The gods have forsaken you,", 
"You disgust me", 
"You fight like a dairy farmer", 
"You couldn't fight your way out of a rotten burlap sack", 
"Clearly your people have not yet discovered the toothbrush", 
"You need a wash", 
"I can't believe someone let you out dressed like that", 
"Your face is physically painful to look upon", 
"A black dragon's breath smells better than yours", 
"You have naught charisma", 
"You'll lose yet again", 
"This will be just one in a long line of your failures", 
"I can see why eveyone in your life has given up on you,", 
"Your parents did a miserable job raising you,", 
"It seems you weren't hugged enough as a child", 
"What tiny hands you have", 
"There's an engraving of your face in the Codex of Knowledge next to the entry for 'incompetence'", 
"It looks like you've been beaten savagely with the ugly stick", 
"Better go change your diaper", 
"You've the vocabulary of a nine-year-old simpleton", 
"Your reproductive fortitude is widely known to be lacking", 
"You clearly skipped leg day", 
"Run along home and", 
"let the grown-ups work this out", 
"Surely that's not the best you can do", 
"Apparently someone trained you wrong as a joke", 
"I desire we be better strangers", 
"Your lover is notoriously unfaithful", 
"Nobody's impressed with you,", 
"Your lover complains of your lack of endurance", 
"Incompetence rolls off of you in waves", 
"You're not as smart as you think you are", 
"You're neither stable, nor a genius", 
"I almost feel sorry for you,", 
"I think I hear your parents calling you,", 
"Get thee to a nunnery", 
"Children laugh at you behind your back", 
"Your face makes babies cry", 
"There's nothing strong about you but your stench", 
"Your favorite bard sucks", 
"I'm surprised you've not yet choked to death on your own stupidity", 
"I see you've been packing on the pounds for next winter", 
"It's not OK to be the way you are", 
"There's a lot wrong with you,", 
"Bless your heart", 
"You should re-think your priorities", 
"You'd best go home and put on your big-girl pants", 
"I fart in your general direction", 
"You wipe donkey butts", 
"Your very existence is a desecration", 
"Fie on thee", 
"You make me sick", 
"I thought I recognized your foul stench", 
"You are a waste of breath", 
"You are a poor imitation of a person", 
"Try harder", 
"Yippee ki yay", 
"I'm not impressed", 
"It looks like you need a nap", 
"Your behavior is predictably infantile", 
"Your character is imminently impeachable", 
"Your attire is unquestionably inappropriate", 
"I'm shocked by your egregious incompetence", 
"Eat a bowl of daggers", 
"Say hello to your mother for me", 
"Your mother attends a university", 
"You lack couth", 
"You don't have what it takes", 
"Everything is wrong with you,", 
"You haven't sufficient skills to pay your bills", 
"Your desperation is palpable", 
"Shut your mouth hole", 
"I take offense to your presence", 
"Your existence shall not be tolerated", 
"The world needs less of you,", 
"I'd avoid mirrors if I were you,", 
"I laugh derisively in your weasly face", 
"You're 4 stones of stupid in a 2 stone bag", 
"Your father smelled of elderberries", 
"I would cry too if I were you,", 
"You're a loony", 
"All eyes and no sight", 
"All hail anionted sovereign of sighs and groans,", 
"Not so much brain as earwax",
]
let adjective = [
"clingy", 
"cruel", 
"careless", 
"vain", 
"pompous", 
"belligerant", 
"big-headed", 
"self-centered", 
"nasty", 
"thoughtless", 
"aloof", 
"stubborn", 
"tactless", 
"pig-headed", 
"fussy", 
"jealous", 
"obstinate", 
"narrow-minded", 
"sneaky", 
"unrelaible", 
"indiscreet", 
"impatient", 
"dishonest", 
"inflexible", 
"deceiftul", 
"idle", 
"foolish", 
"weak-willed", 
"cowardly", 
"gullible", 
"disgraceful", 
"jarring", 
"errant", 
"ruttish", 
"unmuzzled", 
"tottering", 
"rank", 
"puny", 
"infectious", 
"gleeking", 
"goaish", 
"frothy", 
"tickle-brained", 
"weather-bitten", 
"toad-spotted", 
"swag-bellied", 
"sheep-biting", 
"shard-borne", 
"rump-fed", 
"rude-growing", 
"rough-hewn", 
"reeling-ripe", 
"pox-marked", 
"pottle-deep", 
"plume-plucked", 
"onion-eyed", 
"motley-minded", 
"milk-livered", 
"knotty-pated", 
"ill-nurtured", 
"ill-breeding", 
"idle-headed", 
"hell-hated", 
"hedge-born", 
"hasty-witted", 
"half-faced", 
"guts-griping", 
"full-gorged", 
"fool-born", 
"folly-fallen", 
"fly-bitten", 
"flea-bitten", 
"flap-mouthed", 
"fen-sucked", 
"fat-kidneyed", 
"earth-vexing", 
"doghearted", 
"dizzy-eyed", 
"dismal-dreaming", 
"clay-brained", 
"foully-formed", 
"foul-smelling", 
"churlish", 
"dim-witted", 
"arse-faced", 
"unsavory", 
"execrable", 
"spoony", 
"unlovable", 
"cowardly", 
"flea-ridden", 
"scab-encrusted", 
"puss-filled", 
"bilious", 
"highly fed and lowly taught", 
"ill-tempered", 
"mewling", 
"gibbering", 
"bloated", 
"drooling", 
"mealy-mouthed", 
"chicanerous", 
"greasy", 
"sleazy", 
"sweaty", 
"porcine", 
"foolish", 
"stupid", 
"ugly", 
"illiterate", 
"asinine", 
"apelike", 
"artless", 
"arse-sniffing", 
"addle-pated", 
"boorish", 
"mangy", 
"canker-blossomed", 
"castrated", 
"dandruff-covered", 
"cancerous", 
"cantankerous", 
"untrustworthy", 
"pestilent", 
"diseased", 
"rotting", 
"lecherous", 
"crass", 
"ill-mannered", 
"unrefined", 
"basic", 
"whiny", 
"unpleasant", 
"foul", 
"half-witted", 
"silly", 
"braying", 
"sniveling", 
"beastly", 
"oafish", 
"malignant", 
"suffering", 
"bedridden", 
"buck-toothed", 
"shifty little", 
"moaning", 
"bloviating", 
"insipid", 
"slothful", 
"drunken", 
"salacious", 
"recalcitrant", 
"insubordinate", 
"deplorable", 
"regrettable", 
"pernicious", 
"odious", 
"scandalous", 
"barb-tongued", 
"two-faced", 
"cloven-hooved", 
"equivocating", 
"slippery", 
"bleating", 
"bulbous", 
"pilfering", 
"feral", 
"thrice-cursed", 
"unimpressive", 
"middling", 
"rotten", 
"contemptuous", 
"nattering", 
"annoying", 
"superfluous", 
"contrarian", 
"tedious", 
"meddlesome", 
"syphilitic", 
"over-blown", 
"prattling", 
"dung-covered", 
"simpering", 
"light-of-brain", 
"ignorant", 
"plague"
]
let finishThem = [
"apple-john", 
"baggage", 
"barnacle", 
"bladder", 
"boar-pig", 
"bum-bailey", 
"canker-blossom", 
"clack-dish", 
"clotpole", 
"codpiece", 
"dewberry", 
"dingleberry", 
"flap-dragon", 
"flax-wench", 
"flirt-gill", 
"foot-licker", 
"giglet", 
"lout", 
"hedge-pig", 
"scut", 
"miscreant", 
"MediaQueryListEventmoldwarp", 
"nut-hook", 
"sphincter", 
"boil", 
"plague sore", 
"strumpet", 
"dung-heap", 
"braggart", 
"swine", 
"bag of rats", 
"ignoramus", 
"sack of lard", 
"bucket of sewage", 
"butt-pimple", 
"bastard", 
"waste of space", 
"garbage fire", 
"dotard", 
"ne'er-do-well", 
"miscreant", 
"ruffian", 
"pants-stain", 
"vermin", 
"drunkard", 
"fishwife", 
"blowhard", 
"peasant", 
"meat-sack", 
"idiot", 
"simpleton", 
"gelding", 
"jackanape", 
"scoundrel", 
"miser", 
"philestine", 
"monster", 
"dog", 
"mutt", 
"mongrel", 
"outcast", 
"dunderhead", 
"filth", 
"dirtbag", 
"sad-sack", 
"loser", 
"failure", 
"eunuch", 
"cultist", 
"camp-follower", 
"ingrate", 
"sow", 
"cow", 
"rotter", 
"cuckold", 
"contagion", 
"fishmonger", 
"harlot", 
"curmudgeon", 
"weakling", 
"whiner", 
"mistake", 
"dimwit", 
"bore", 
"boar", 
"boor", 
"clown", 
"beast", 
"oaf", 
"louse", 
"beast", 
"beggar", 
"peon", 
"recidivist", 
"reactionary", 
"ragamuffin", 
"servant", 
"whipping-boy", 
"rapscallion", 
"minion", 
"lackey", 
"toady", 
"trollop", 
"ninny", 
"coward", 
"fiend", 
"runt", 
"half-wit", 
"goatherd", 
"prevaricator", 
"philanderer", 
"debutante", 
"dilettante", 
"bag of failure", 
"goat", 
"toddler", 
"worm", 
"slime", 
"brigand", 
"plague-rat", 
"villain", 
"jerk", 
"pan-handler", 
"turd", 
"curr", 
"dandy", 
"egg"
]
return (searchArray(primeLine) + ' you ' + searchArray(adjective) + ' ' + searchArray(finishThem) + '.');
}
let lawfulInsult = [
"Of course I talk like an idiot. How else could you understand me?", 
"Your Mama’s so fat she died. I’m sorry for your loss!", 
"The volume of the knowledge which you do not possess makes the ocean look like a puddle.", 
"May the chocolate chips in your cookies turn out to be raisins.", 
"May every sock you wear be slightly rotated just enough to be mildly uncomfortable.", 
"I’d like to leave you with one thought on your mind, but I don’t think it would fit.", 
"You look like someone who knows how to handle themselves in bed.", 
"Someone done blowed out your kindling.", 
"I see that you’ve set aside this special time to humiliate yourself in public.", 
"You started at the bottom… and it’s been downhill ever since.", 
"Brains aren’t everything. In fact in your case they’re nothing.", 
"No, no, I’m not insulting you I’m describing you.", 
"If what you don’t know can’t hurt you, you’re invulnerable.", 
"Ordinarily people live and learn. You just keep on living.", 
"You are as strong as an ox and almost as intelligent.", 
"If you were twice as smart, you’d still be stupid.", 
"Shock me. Say something intelligent.", 
"I don’t think you are a fool. But then what’s MY opinion against thousands of others?", 
"Isn’t it rather dangerous to use one’s entire vocabulary in a single sentence?", 
"I’d give you a nasty look but you’ve already got one.", 
"You’ll never be half the man your mother is.", 
"If you’re going to be two-faced, at least make one of them pretty.", 
"I’ve seen people like you before, but I had to pay admission.", 
"I would ask how old you are, but I doubt you can count that high.", 
"Just because you have one doesn’t mean you need to act like one.", 
"Half your outfit looks fabulous!", 
"I love how you don’t care what people think of you.", 
"You are impossible to underestimate.", 
"I can’t believe you’d come out in public with a face like that. Have some decency and wear a mask.", 
"Let me say this in a language you can understand, grunts annoyingly.", 
"You are a person of rare intelligence.", 
"[In a mildly racist French accent] Your mother was a hamster, and your father smelled of elderberries!", 
"You fight like a dairy farmer!", 
"You should learn from the dwarves and at least be drunk before you act insufferable.", 
"What is your name? Oh wait I forgot you don’t remember it.", 
"You’re ugly on a metaphysical level.", 
"Your nose looks bigger than your ego.", 
"I bet you didn’t even realize this was an insult!", 
"Wow, your hair is fine! … Wait, no, I mean thinning! Your hair is thinning!", 
"You would probably have a nice smile if it weren’t for your face!", 
"That outfit looks expensive. Shame it’s not helping…", 
"Nice hair!", 
"I’m so excited to forget you.", 
"Why do you have to be so tall? If you had been pint sized at least we could have overlooked you easier.", 
"Now was one of your parents an orc or are your teeth just that bad?", 
"Now I realize you’re probably an orphan but you cant have lived this long and learnt absolutely nothing in regards to manners.", 
"I would kill you but I don’t think the gates of heaven are wide enough for you to fit through.", 
"'Oh, let’s fight the level X adventurers, they’ll die easily' Don’t you think if we were bad at this we would be dead by now. You’re idiots for even trying to fight us!", 
"Now there’s a face only an aboleth could love.", 
"That’s your big plan? I’ve heard more intelligent growls from an Owlbear.", 
"Are you made out of gold? You’re dense, soft, and I’d love to stick a pick axe in you.", 
"Wow! You did way better than I thought you would do. That’s great!", 
"You’re a really great adventuring party…just not for this quest.", 
"Well, wow…that idea is just something…we’ll have to remember that for a discussion on another day.", 
"I’m not saying you’re ugly, I’m just saying the beholder refused to look at you.", 
"Was that your own idea or did someone write it down for you?", 
"You know, I pity your mother. 9 months of effort to bring you into the world, and it’ll only take me a few moments to remove you from it.", 
"Don’t bother praying to your gods, cleric. You’re about to meet them.", 
"You’re not even worth the mud on my shoes.", 
"Beauty is in the eye of the beholder. Unfortunately, my eyes are all too human in your presence.", 
"Did you rehearse that monologue? Oh what am I saying, you probably read it off of that napkin you call a spellbook", 
"Have you considered a career as a dung sweeper? You’ve already got the smell down pat.", 
"I don’t know what kind of mental gymnastics you did to reach that conclusion, but they certainly could outmatch a trained performer.", 
"Are you deaf, blind or just utterly stupid?", 
"I’d try to get you back on track, but you’d probably actually get on the train tracks and get killed in the process.", 
"I heard that you went in to a restaurant and ate everything in the restaurant and they had to close the restaurant.", 
"Sorry, just give me a minute. I’m trying to think of ways to mock you, but in your case they’d be flattery.", 
"You butter your bread like an old man.", 
"You have the brain of someone who has encountered a Mind Flayer!", 
"You look like you’d eat two cakes for lunch.", 
"You have the sparse beard of a young pageboy.", 
"Agh! What is that horrible smell…oh I see you’ve bathed that layer of mud off today that must be it.", 
"Your wit has never been matched. Exceeded, often, but never matched.", 
"Did it hurt when you fell from the celestial plane, missed the material, and landed in the nine hells?", 
"Could you tell me what god you worship? I see no other reason save for divine luck that your dumb arse has lasted this long.", 
"So you’re the one that an Ogre brings along on a date so that he looks better by comparison. I’ve been looking for you on account of a friend.", 
"May I suggest you learn magic? I don’t see any other way you could cover up those horrendous blemishes.", 
"You’re mother, I’m sure, is a wonderful person. It’s a darn right shame you did t take after her.", 
"They say the gods make no mistakes, but you are proof otherwise.", 
"I am always happy to have you around. Your aroma is a vivid reminder why I no longer enter Owl Bear caves.", 
"Let me guess, you have a great personality.", 
"Wow. You really look your age.", 
"You are aware that people simply tolerate you?", 
"I can explain it to you but I can’t understand it for you.", 
"You’d struggle to pour water out of a boot with instructions on the bottom.", 
"If I agreed with you, we’d both be wrong.", 
"When was the last time you saw someone smile because you entered a room?", 
"I’m not angry. I’m just very disappointed.", 
"Your new haircut looks so much better than the last one.", 
"The foulest place of mine arse is fairer than thy face.", 
"You certainly do live up to your reputation.", 
"That kind of petty meanness doesn’t become you. Show us you can do better.", 
"I envy everyone you have never met.", 
"I’d try to insult you but I’d never do as well as nature did.", 
"I hope your day is filled with people like you.", 
"You’re not the sharpest knife in the drawer, but you’d make a spoon jealous.", 
"Your unibrow would make a Cyclops envious. Or horny.", 
"Looking at you makes me wish I needed glasses, and happened to forget them today.", 
"Normally I don’t insult people as intelligent as you, but I’ll make an exception in your case.", 
"May something bad befall you, like an onion falling on your head.",
]
let chance = rollDice(100)
if (chance < 50) {
document.getElementById("Insult").innerHTML = 'An argument erupts: "' + insultGenerator() + '"';
} else {
document.getElementById("Insult").innerHTML = 'An argument erupts: "' + searchArray(lawfulInsult) + '"';
}
};
function findEndConvo() {
function findRumor(){
let completeRumors =[
"'Ey, did you hear about poor old Tom Gobbard, the fisherman? Apparently he was out fishin’ a fortnight ago, and he reeled in something that…wasn’t a fish He’s over there in the corner, still gibbering uncontrollably, if ye’ want to ask him about it.", 
"I have it on good authority that a mysterious ship pulled into harbor just five days ago. Apparently, there’s not a living soul onboard. The captain and crew have simply vanished. The town watch investigated, and the entire ship was empty…except for a rather large box in the cargo hold. The ship is still sitting in the harbor. No one’s been brave enough to open the box.", 
"Did you hear that Captain Norkus died just last week? It’s true! Word is that he tripped on his own deck and snapped his neck. His family paid a LOT of money to have him resurrected, and they’re trying to keep it a secret. It’s just…ever since he was raised from the dead he’s been…different. It’s hard to put your finger on it, but he's definitely been givin' ME the creeps.", 
"Sit back, lad, I’ve got a story for you. Back in my youth, I sailed on a trader’s ship. We got blown off course, and made land on a green island, lush with vines and fruit trees. We thought we’d load up on fruit for the journey, but it wasn’t long before the island…started moving. We rushed back to the ship and I’ve never found the isle since.", 
"You want to speak of strange isles? Well, when I was a lad my crew and I found a rocky isle many miles north. It was a tiny isle, lonely and bare, save for a solitary, black tower. We considered exploring the tower, but thought better of it when the sun went down and the tower began to…sing. We loved our lives, so we boarded the ship and fled!", 
"The ghost ship is real, I’ve seen it! Head northwest of here, and, if the moon is full, you’ll see a glowing, purple pirate ship with ragged sails, floating just a mile’s distance away. No matter how close you sail, the ghost ship stays just out of reach…", 
"You want to hear something funny? There’s a tiny town on the east coast where everyone has the same name! I mean it, EVERYONE. The butcher, the baker, the candlestick maker, everyone in town goes by the name ‘Goxus.’ Come to think of it, they all speak with the same sort of…distracted tone of voice, too. Kind of odd, now that I think of it. Anyway, they’ve never cheated me so I suppose I’ll keep doin’ business with ‘em.", 
"Yes, this is Wicker the Parrot. I found him perched outside my window this morning. Can’t understand why his tail feathers have gone white, though…and where’s his master? This parrot used to talk nonstop, but now he only repeats one phrase… “Stay away from the Weeping Pool.” What do y’think that means?", 
"There’s a fishing village to the west where they don’t seem to like strangers, much. I was lost and needed an inn, so I convinced them to let me stay the evening. I wish I’d have just moved on. One evening, late at night, I awoke to the sound of soft chanting outside my window. I pulled back the curtain and saw everyone in town down by the shore, holding an infant high in the air. As I watched, three ugly, blue-skinned women climbed out of the sea and onto the land. I closed the curtain and went back to bed. Wouldn’t recommend staying there!", 
"If you’re sailing off to the west, keep an eye out. I’ve been hearing reports that there’s a big black storm brewing off the western coast. Strange thing, though, is that the storm has been building for several days, and the black clouds won’t blow away. Even stranger…some folks have been sayin’ that if you look at the black storm clouds just right, they look like faces…",
"The Giants were never killed in the giant war, they secretly retreated into their airship and escaped (they actually went up into the clouds like Jack and the beanstalk)", 
"The king's advisor is a disguised lizardfolk", 
"Lead helmets stop the government from hearing your thoughts (they also make you go crazy from lead poisoning)", 
"The public execution of an enemy kingdom's spy was faked with a body double. The real guy is hiding out pretending to be a peasant in one of the outlying towns.", 
"The birds are spies for the government (not robots though that's crazy)", 
"the beholder is rumored to have dreamt up the kingdom itself", 
"The Primordials were never content with being resigned to their own planet, and the increasing amount of dragonborns (only there by sudden portals) points to the fact theyre trying to break back in", 
"The heir to the throne is actually the son of the general, switched at birth with the true heir, who is living as a peasant, unaware of their lineage.", 
"The rapid disappearance of many types of animals in the surrounding area is the work of a mad wizard, intent on fusing them together Frankenstein style. It’s only a matter of time until they will go after humans.", 
"The government puts something in the city's water in order to surpress magical abilities in its citizens.", 
"The bandit raids on towns and villages are orchestrated by smithing guilds in order to increase demand in weapons and armor.", 
"The strange magical beasts and monsters in the area are actually what's left of sapient humanoids that were experimented upon by mad mages.", 
"The local artifact and curio shop is suspiciously cheap and easy to steal from to encourage the spread of demonicly corrupting artifacts.", 
"A being with glowing red eyes has been seen in the woods many times over the past month.", 
"The entire kingdom is actually being run by the sentient throne the king sits on", 
"The kingdom's elite are using the cargo Griffins to spread chemical trails across the sky.", 
"The local Crime Lord is actually the king's daughter who is trying to make life generally difficult for her father who has promised her hand in marriage against her desire, and eventually she's planning on having him murdered in order to take over. She keeps her identity completely secret and lives a double life with the denizens of the underworld.", 
"The real king was actually killed years ago by his corrupt advisors; he's been replaced by a doppelganger under the control of said advisors ever since.", 
"The Gods are a lie. They don't exist. They are really a powerful cabal of spellcasters who rule the world secretly", 
"Dragons aren't particularly long lived. They only appear so because they grow in power by killing others of their kind. That is why there are so few of them", 
"Dwarves are the actual builders of this world. They created everything literally from the ground up. Elves are actually 'fallen dwarves' who live so much longer because they have cut themselves off from the earth and stone and no longer return to it when they die.", 
"Everyone knows there used to be a village there, it was on the trading route. But there is no village there anymore. Nor any sign that one used to be there!", 
"The attacks on the livestock are not actually from a direwolf as the king has proclaimed, but they are being used as sacrifices by an evil cult OR your typical lycnathropy trope.", 
"Someone believes that the king was born abroad and isn't legitimate and wants witnesses or certificates of his birth", 
"Someone believes that Elven Pressleaf, the famous elven bard, didn’t actually die from too many nature shrooms, but retired and is in hiding", 
"Someone believes that teleportation magic is a hoax, and that people haven’t been to the The Lunar Castle, home of Lunadiel", 
"Carol O'Na, is believed to be the reincarnation of the horseman Pestilence. It seems everywhere she goes people get sick", 
"Karen Wokefeld once hired an abjuration wizard to protect their house during a small bandit raid. She is claiming his abjuration magic actually cursed her family, and would like him dead", 
"No one goes near the abandoned mansion at the edge of town because it’s haunted. But rumour is that’s just a ghost story to keep people away while something more sinister happens behind the walls..", 
"A local business man is intent on building a legacy of locally-owned farms. He employs only slaves.", 
"The rise in sea-levels over the past few decades are not a result of the slowly increasing global temperature but rather an increase in gargantuan water-dwelling creatures, whose sheer collective volume is actually displacing the water, making it appear to have risen.", 
"A local drunk and part time stable-hand claims the recent spate of illness and deaths across the kingdom are the result of tiny invisible creatures attacking us from the inside, and not because the king slept with the wife of a powerful and vindictive mage. Nobody believes him, and his drinking habit grows by the day. His family are concerned and are considering staging an intervention.", 
"All the random natural events impeding construction of an outpost are being caused by a group of druids trying to stop the project.", 
"The king is hiring spies to spy on people who didnt pay lots of stuff", 
"A person wanted forthe stuff of the kingdom is a little kid", 
"There was a shop that had over 40 people going there a week but it was replaced with one of the least selling shops today", 
"The kings king's assassination while he was in his coach was not by a rogue from the the storage tower of the wizards collegium, but was actually done by the kings own guard from a grassy hill on the route through the city.", 
"The leaders of the 2 warring nations are in cahoots. The gain profit and influence by perpetuating the war. They have provided propaganda to be taught in schools, they put out flier propaganda on both sides, they use religion.", 
"The kings throne is actually a mimic that has been enchanted to only allow those of the royal bloodline to sit on it.", 
"The Queen was never assassinated, it was actually the King. She has been using polymorph and potions to disguise herself as the King.", 
"The horses used by the guards are actually Kelpie that have been contracted to work for the Kingdom and are feed the prisoners that are 'executed'.", 
"The reason the Holts Farm never suffers from blights and pests is because they sacrifice an orphan to the creature that lives in their well.", 
"A rebel group is opposing the prominent church with the overwhelming evidence of their old god.", 
"When you use teleportation magic, it's not you being teleported. The real you dies, gets disintegrated, and then they make a clone of you in your place.", 
"Changelings and Doppelgangers have infiltrated our society, they could be anyone at any time!", 
"The King has been replaced with an illusion - The real king is being held prisoner in the dungeons.", 
"The thieves guild is actually a secret branch of the government - When someone gets caught, they don't get prosecuted, they get retired from the public eye and repurposed.", 
"Aarakocra aren't real.", 
"Secret organizations proliferate anti-tiefling propaganda to keep them subjugated.", 
"Orcs used to be intelligent, until government programs turned them into killing machines.", 
"The church of <insert god here> is a front for the cult of <insert other entity here>.", 
"Metallic dragons don't exist. Chromatic dragons paint themselves metallic to attract prey.", 
"The 'Common' language is a means of cultural suppression by humans for races who speak other languages - by unifying the races under the human tongue, they assured that they were at the center of trade. It didn't even used to be called common, that change was made in the year 733 for PR purposes.", 
"There are alligators the size of whales in the city sewers. One recently destroyed an outhouse!", 
"The earth is hollow; beneath the Underdark, there is a beautiful and mysterious land of freshwater seas and mushroom forests with inverted gravity.", 
"Roundearthers are convinced that the world is not a disc and stories of sailors falling over the edge are merely government propaganda.", 
"The 'Golden Age of Magic' that took place hundreds of years ago actually never took place. The world is much younger than history books show, and everything that happened before a certain point in time was a large-scale illusion placed upon everyone in the kingdom as a cover-up for something else that happenedinfernal", 
"A clan of changelings have secretly replaced significant individuals of power in order to steer the kingdom to its doom as revenge for somethinginfernal", 
"The kingdom is surrounded by tall walls that hide everything beyond. No one is allowed out because of the Great War between nations. In reality, there is no Great War. Beyond the walls are unending stretches of desert, ocean, and destroyed land due to some catastrophic event that's hidden from the general populace. But the truth is somewhere out thereinfernal", 
"Low magic campaign: Powerful magic exists, but the knowledge is hidden in the hands of the powerful, while the general populace is told that magic inherently has a cap in strengthinfernal", 
"A current plague is actually spread by mages using 'Sending' which is why the non-magic using commoners get illking", 
"According to some credible sources, health potions are made of pulverized gnomes.", 
"The various planes of reality are all part of a giant turtle’s dream. If a sufficiently powerful wizard or sorcerer were to find a way, they could wake the turtle.", 
"A bandit company that was vanquished/scatter years ago never really died, their members just integrated into society and they're enacting a covert, long-term mission to sow chaos in the kingdom. Rumor is, 'My neighbor is a sleeper agent of the long-disbanded thieve's guild!'", 
"If you go into the Giant's Beard Inn, Soggy Frog Inn, or Quail's Tavern and ask about Rohir Borgenaut, they kick you out. That name means nothing to anyone else in the city. Why?", 
"Those slaves that the mercenaries sold to the citizenry a few months back are actually just zombies wearing rings of disguise self! People are paying money to bring zombies into their home!", 
"I saw the court wizard flash a demonic handsign once, as he stood behind the Baron during an address to the people. Who was he trying to signal in the town? What does the signal mean?", 
"A farmer tells the party that his neighbor was NOT, in fact, killed by orcs three years ago. Orcs go house to house, killing and plundering. My neighbor was violently killed in his own home, and nothing was stolen! no other houses hit! I suspect it was the farmer's guild, they've been squeezing us really hard. I thought they were supposed to help us?!", 
"The humans in an elf-human city have invented a new device that the elves suspect was purposefully invented to hurt them: the printing press. Using this device, they began mass unlawful arrest of all elves caught in the human quarter, and are producing arrest records much faster than the elf council can keep up with - resulting in a great many innocent elves staying in jail unlawfully for days, weeks, and even months.", 
"Farmer Randall made a huge fuss a week ago - claims he saw a green dragon eating his sheep. He demanded a retinue of guards come and do a detail. When the guards arrived the following dawn, farmer Randall denies ever making any such claim, and refuses the guards entry to his farm. A few days later, his wife 'left town in the middle of the night' and no one has seen her since. What the hell is going on at farmer Randall's?", 
"Many demons and other humanoid monsters are just people wearing suits",
]
function rumorMill(){
let subject= [
"a child", 
"a fat merchant", 
"a temple priest", 
"a sailor", 
"a soldier", 
"a magician", 
"a noble", 
"a rogue", 
"a crazy monk", 
"a drunken farmer", 
"the king", 
"the queen", 
"the local miller", 
"the local blacksmith", 
"a retired adventurer", 
"a famous assassin", 
"an influential guildmaster", 
"the mayor", 
"an up-and-coming young knight", 
"the high priest of bhaal", 
"a powerful drow matron", 
"a wicked wizard", 
"the knight-lord of a local order of paladins", 
"strahd von zarovich", 
"a militant emperor in the west", 
"a dragon-tamer in the mountains", 
"the local dragon", 
"an orc warlord", 
"one of the party members", 
"an ancient pharaoh", 
"a popular gladiator", 
"a teamster who is a local legend for reckless driving", 
"the crown prince", 
"a master alchemist", 
"a high-ranking hobgoblin commander", 
"an elven sage", 
"the duchess", 
"the duke", 
"the local priest", 
"an eccentric inventor", 
"the town lunatic", 
"a notorious pirate captain", 
"a travelling monk", 
"a famous mystic", 
"the housekeeper of a local hostel", 
"a viking king", 
"the great chief of ogres", 
"a famous trap-maker", 
"an influential politician", 
"the town beggar", 
"the princess", 
"a newly-appointed lady knight of the region", 
"a newly-appointed lord knight of the region", 
"the caesar of minotaurs", 
"the local weaponsmith", 
"the bbeg", 
"the mysterious man with a long, silver beard and a ragged black cloak", 
"the mysterious woman with long, silver hair and an old-fashioned scarlet cloak", 
"the local tobacco merchant", 
"the kingpin of a crime ring", 
"the head of a tarrasque-worshiping cult", 
"a vicious manticore baron", 
"a highly sought-after tailor", 
"a highly sough-after baker", 
"a highly sought-after physician", 
"every gravedigger in the entire region", 
"the king's two-year-old son", 
"a kuo-toa diplomat", 
"the bloodlord of vampires", 
"a necromancer", 
"the court magician", 
"a boatman on the local river", 
"a mason building the king's new palace", 
"a great athlete", 
"the head of a not-so-secret society", 
"the local innkeeper", 
"a zombie who was voted in as townmaster", 
"an elvish king", 
"the lord of a druidic circle", 
"the new 8-year-old king", 
"a famous painter", 
"one of the pcs' mentor", 
"a famous evangelist", 
"a gorgon beauty guru", 
"the yuan-ti god-king", 
"a powerful unseelie fey", 
"a goblin warlord", 
"the editor of a local newspaper", 
"the game warden", 
"the king's butler", 
"a renowned golem-building wizard", 
"a great general", 
"a local veteran and war hero", 
"a folk-music writer", 
"the street-lamp lighter", 
"the street sweeper", 
"the chimney-sweep", 
"the harsh boss of a local factory", 
"a far-sailing explorer, back in town after an expedition", 
"a local archaeologist", 
"the witchfinder general", 
"the protector angel of the nearest large city", 
"a powerful seelie fey", 
"the iron emperor of dwarves", 
"the erlking of a local band of monster-hunters", 
"a fashion icon", 
"the grand duke of the society for the preservation of gnomish vocabulistics and grammar", 
"a famous daredevil", 
"the leader of a mostly harmless local cult", 
"the leader of an extremely harmful local cult",
]
let mid2 = [
"hunting ogres", 
"digging pit traps", 
"minting gold pieces", 
"falling out of windows", 
"human sacrifice", 
"setting things on fire", 
"raiding small settlements", 
"eating pastries shaped like sacred icons", 
"swimming around in pools of oil", 
"riding horses", 
"painting pictures", 
"sabotaging other people's carriages", 
"hurling radishes at beggars", 
"stepping on people's toes", 
"doing nothing", 
"shutting up", 
"feeling confident", 
"running over small and fluffy animals", 
"tipping over dominoes", 
"going on shopping sprees", 
"punching sacks of potatoes", 
"building elaborate but useless siege engines", 
"having rap-battles with pixies", 
"doing the conga", 
"convincing other people to do the conga", 
"building extremely comfortable couches", 
"building up an immunity to every kind of poison they can find", 
"studying vaccination", 
"learning how to fly", 
"burying dead bodies", 
"juggling swords", 
"juggling", 
"being a clown", 
"buying elaborate tricorn hats", 
"ringing people's doorbells and running away", 
"writing terrible books", 
"reading scandalous magazines", 
"praising themselves", 
"cow-tipping", 
"throwing china plates across rooms", 
"plating things with solid gold", 
"getting involved in tangled love-triangles", 
"awarding themselves trophies for things they never did", 
"giving long and elaborate speeches", 
"getting drunk", 
"getting high", 
"throwing knives at pictures of their enemies", 
"mixing fake blood in excessive quantities", 
"fighting treants", 
"inventing new kinds of forks", 
"grave robbing", 
"burning down mansions", 
"writing speeches full of innuendos for pastors", 
"recycling old furniture", 
"playing war-games", 
"playing card games", 
"playing dice games", 
"making loaded dice", 
"starting bar fights", 
"making theatrical declarations of war against nonexistent countries", 
"completely ignoring real-world geography", 
"crashing the economy", 
"hurling cinder-blocks at passerby", 
"teaching trolls calligraphy", 
"insulting dragons", 
"writing dramatic last wills for themselves regarding fictitious deaths", 
"murdering people to start a murder-investigation romantic drama", 
"brooding on rooftops", 
"doing tuck-and-rolls into wedding ceremonies", 
"hiding treasures in local dungeons", 
"doing the charleston at funerals", 
"starting moshpits at children's cello recitals", 
"headbanging to the church choir", 
"rolling themselves down hills", 
"giving excessive amounts of charity", 
"joining every secret society they can find", 
"doing somersaults when excited", 
"shooting people with crossbows", 
"designing a new national flag for their country every day, and sending it to the nobility for approval", 
"taming mimics", 
"hitting people over the head with bar stools", 
"wearing cool cloaks", 
"spontaneously combusting", 
"drag-racing in carriages", 
"trying to ride displacer beasts", 
"trying to ride owlbears", 
"jumping out at people from behind corners and shouting 'boo!'", 
"rigging old castles to explode", 
"making silly faces at high-ranking clergy", 
"smoking far too many cigarettes than is advisable", 
"writing fake magazine articles describing wars between closely allied countries", 
"deep-frying books", 
"writing dictionaries of all 89 dialects of abyssal", 
"pulling pranks", 
"breeding new horses", 
"conducting unethical scientific experiments", 
"building exact replicas of small villages, then demanding that all the villagers from that village move to the replica", 
"giving themselves ludicrous new titles", 
"carrying far too many canes", 
"carrying out exorcisms",
]
let root = [
`is disgusted by ${searchArray(mid2)}`, `hates ${searchArray(mid2)}`, `weeps tears of joy for ${searchArray(mid2)}`, `breaks down laughing at the thought of ${searchArray(mid2)}`, `is worryingly obsessed with ${searchArray(mid2)}`, `spent all their money on ${searchArray(mid2)}`, `has asked the church to forbid ${searchArray(mid2)}`, `has asked the church to demand ${searchArray(mid2)}`, `has formed a society based around ${searchArray(mid2)}`, `has led an expedition to ${searchArray(mid2)}`, `once enjoyed ${searchArray(mid2)}`, `has recently picked up ${searchArray(mid2)}`, `demands someone to explain to them what all the fuss is with ${searchArray(mid2)}`, `has forbid the mere mention of ${searchArray(mid2)}`, `commissioned several murals of ${searchArray(mid2)}`, `sentenced convicts to ${searchArray(mid2)}.`, `named their new yacht ${searchArray(mid2)}.`, `disowned their child for the child's becoming addicted to ${searchArray(mid2)}`, `is hopelessly addicted to ${searchArray(mid2)}`, `has challenged any takers to a contest of ${searchArray(mid2)}`, `has started a scandal by ${searchArray(mid2)}`, 
`has completely ignored the issues of ${searchArray(mid2)}`, `got drunk and admitted to ${searchArray(mid2)}`, `firmly denies that they have ever ${searchArray(mid2)}`, `is hosting a costume ball themed around ${searchArray(mid2)}`, `suffers nightmares about ${searchArray(mid2)}`, `wants advice on how to go about ${searchArray(mid2)}`, `tossed someone out of a window for daring to malign ${searchArray(mid2)}`, `hired bards to sing the praises of ${searchArray(mid2)}`, `is trying to quit ${searchArray(mid2)}`, `divorced their spouse to spend more time ${searchArray(mid2)}`, `wandered into the desert with the intent of ${searchArray(mid2)}`, `demanded that any honest man would never stoop to ${searchArray(mid2)}`, `stole a carriage to go ${searchArray(mid2)}`, `has paid people to stop ${searchArray(mid2)}`, `has demanded, against ancient tradition, that they be allowed to ${searchArray(mid2)}`, `carved a statue of themselves ${searchArray(mid2)}`, `has never even tried ${searchArray(mid2)}`, `is ignoring the obvious solution to their current problem,  ${searchArray(mid2)}.`, `gives up all hope for the world when they think about ${searchArray(mid2)}`, `turns into a panda whenever they try ${searchArray(mid2)}`, `has been cursed by a witch to ceaselessly wander through the forest,  ${searchArray(mid2)}`, `loves their spouse, but more so, ${searchArray(mid2)}`, `used magic to make 100 people go ${searchArray(mid2)}`, `got drunk and went ${searchArray(mid2)}`, `spent all their inheritance on ${searchArray(mid2)}`, 
`might start a war over ${searchArray(mid2)}`, `tattooed themselves with scenes of ${searchArray(mid2)}`, `ceaselessly talks about ${searchArray(mid2)}`, `ran 40 miles so as not to be late for ${searchArray(mid2)}`, `wears their finest clothes to ${searchArray(mid2)}`, `believes in the gods but more so in ${searchArray(mid2)}`, `doesn't even understand ${searchArray(mid2)}`, `pays good money for people to compete at  ${searchArray(mid2)} for their amusement.`, `found an ancient urn, worth thousands, depicting ${searchArray(mid2)}`, `insists that it is a genteel pursuit to ${searchArray(mid2)}`, `is causing trouble for everyone by ${searchArray(mid2)}`, `sees it as unseemly to ${searchArray(mid2)}`, `frequently enjoys ${searchArray(mid2)}`, `is enraged by ${searchArray(mid2)}`, `is saddened by ${searchArray(mid2)}`, `got sick while ${searchArray(mid2)}`, `broke their foot while ${searchArray(mid2)}`, `died while ${searchArray(mid2)}`, `proposed to their true love whilst ${searchArray(mid2)}`, `is terrified by the prospect of ${searchArray(mid2)}`, `believes it is a grievous sin to ${searchArray(mid2)}`, `nearly started a revolution while a nobleman was ${searchArray(mid2)}`, `clapped a man in irons for trying to ${searchArray(mid2)}`, `is only ever gladdened by ${searchArray(mid2)}`, `fully intends to kill their rival, making it look like an accident that occurred while they were ${searchArray(mid2)}`, `has changed their main pursuit to ${searchArray(mid2)}.`, `denies claims that they ever ${searchArray(mid2)}, despite solid evidence.`, `has a long history in their family of ${searchArray(mid2)}`, 
`was nearly assassinated while ${searchArray(mid2)}`, `explodes with fury when others ask if they intend to ${searchArray(mid2)}`, `is enchanted to slowly levitate into the sky should they ever try ${searchArray(mid2)}`, `has ordered a local noble to stop ${searchArray(mid2)}`, `is haunted by the ghosts of those who died such that they could ${searchArray(mid2)}`, `has cured themselves of a terrible illness by simply ${searchArray(mid2)}`, `arose from the grave when they heard their relatives were ${searchArray(mid2)} instead of attending their funeral.`, `wrote long and vivid books on the subject of ${searchArray(mid2)}`, `will not so much as get out of bed until they ${searchArray(mid2)}`, `rises bright and early to ${searchArray(mid2)}`, `trained several hawks for the purposes of ${searchArray(mid2)}`, `breaks into song and dance randomly to distract people from their habit of ${searchArray(mid2)}`, `says they would rather die than ${searchArray(mid2)}`, `dreams of ${searchArray(mid2)}`, `has no appetite on days when they haven't ${searchArray(mid2)}`, `hired adventurers to ${searchArray(mid2)}`, `hired a wizard to help them with ${searchArray(mid2)}`, `built an entire facility dedicated to ${searchArray(mid2)}`, `used slaves and prisoners for ${searchArray(mid2)}`, `threw themselves into a lake after a long day of ${searchArray(mid2)}`, `hosted a banquet in celebration of their successful quest of ${searchArray(mid2)}`, `frequently boasts about how good they are at ${searchArray(mid2)}`, `demands that nobody but themselves be allowed to ${searchArray(mid2)}`, `prays to the gods for success in ${searchArray(mid2)}`, `recommends that pregnant women try ${searchArray(mid2)}`, `firmly believes that ${searchArray(mid2)} is extremely classy and romantic.`,
]
let action = [
"got drunk", 
"got washed out to sea", 
"got stuck on a runaway horse", 
"found an old well", 
"disappeared for 3 days", 
"found an old tomb", 
"met a weird stranger", 
"found a magic item", 
"was sleepwalking", 
"walked off into the forest",
]
let discovery = [
"a new disease", 
"a powerful artifact", 
"a cursed item", 
"a sleeping monster", 
"a treasure map", 
"a hero/villain thought dead, returned to life", 
"a book of secrets", 
"a key to a vast fortune", 
"a supressed truth about the ruling kingdom", 
"a door to another plane",
]
let result = [
"people are disappearing!", 
"people are sick!", 
"the king has decreed strange new laws!", 
"the temple has issued strange new tenets!", 
"the sun might not come back up!", 
"the moon might fracture!", 
"the world might be invaded!", 
"people are having bad dreams every night!", 
"people are unable to sleep!", 
"people are afraid to come outside!",
]
let variableRoot = `${searchArray(action)} and discovered ${searchArray(discovery)}, and now ${searchArray(result)}`

let source = [
"the local newspaper", 
"the village idiot", 
"the gods themselves", 
"a giant demon", 
"a local magistrate", 
"the captain of the guard", 
"a drunk in a bar", 
"an eerily sober man in a bar", 
"the local miser", 
"my grandmother's ghost", 
"an insane prophet", 
"a mercenary captain", 
"a mermaid", 
"a man who turned out to be a doppleganger", 
"three gnomes in a trench coat", 
"two halflings in a trench coat", 
"eighty-six pixies in a trench coat", 
"an animated, sentient trench coat", 
"a beholder", 
"a man cursed to only speak the truth", 
"a local jester", 
"a mafia hitman", 
"a goblin who was on fire", 
"a cloud giant", 
"a group of azers", 
"a man who fell through the roof", 
"a viking warrior", 
"a man who rolled through like tumbleweed", 
"a mind flayer", 
"mordenkainen himself", 
"volo himself", 
"a bounty hunter", 
"an old soldier", 
"an old policeman", 
"a former army commander", 
"a crusader", 
"an occultist", 
"a grave robber", 
"a mailman", 
"an animated reflection of myself in a mirror", 
"a man who wore two dark cloaks", 
"a one-legged, one-armed, one-eyed man", 
"a werewolf", 
"a stone golem", 
"a tap-dancer", 
"a saxophone player", 
"the high priest of kelemvor", 
"an entire travelling circus", 
"the town crier", 
"a retired pirate", 
"a retired bandit", 
"a slightly insane author", 
"a salty old sailor", 
"a great-grandmother from a large local clan", 
"the greatest clown in the world", 
"a suit of animated armor that had trapped a man inside it", 
"a man selling salt", 
"a trickster spirit", 
"an imp", 
"a regiment of hobgoblins", 
"a tribe of orcs", 
"an ettin, who also said it wasn't true", 
"a wraith", 
"a lich lord", 
"a lost traveler", 
"the mayor's niece", 
"a fisherman", 
"a silent and mysterious stranger who recently moved into town", 
"a professional spy", 
"a stockbroker", 
"a tabaxi minstrel", 
"a goliath monk", 
"a band of singing dwarves who sung it to me", 
"an elvish comedian", 
"a halfling with a mohawk", 
"my evil twin", 
"a lost planeswalker", 
"a slightly evil magician", 
"a poison dealer", 
"a mob legbreaker", 
"someone covered head to toe in scarves and coats", 
"my spouse", 
"my son", 
"a tortle with a purple-painted shell", 
"three knights, one in white armor, one in black, one in grey", 
"a kobold with a violent temper who screamed at me about it", 
"a dragonborn who was looking for their parents", 
"a beautiful forest nymph", 
"an old woman who turned out to be a hag", 
"an old man who turned out to be a vampire", 
"a man who refused to stop doing jumping jacks", 
"a young woman who started a dance party after telling me", 
"a skeleton", 
"a morbid man with tired-looking eyes and rumpled suit", 
"a talking parrot", 
"a wandering preacher", 
"a young half-elf who was on a pilgrimage", 
"a knight in golden armor", 
"gary gygax", 
"a talking cat",
]
let generatedRumor = `Did you hear that ${searchArray(subject)} ${searchArray([searchArray(root),variableRoot])}. I could be wrong but I heard that from ${searchArray(source)}`;
return searchArray([generatedRumor, searchArray(completeRumors)])
} 
let legendArray = [
"Infernal Research. The research of a Lich when he was just a powerful wizard that holds the secret to trans-planar communication.", 
"Ocean’s Bounty. The lost treasure of a great pirate hidden in a cursed shipwreck on the floor of the ocean.", 
"Ancient Laboratory. The portal to the demi plane that holds the laboratory of the greatest alchemist of all time.", 
"Seeds of the Tree of Life. They are mystical artifacts with unknown powers not meant for mortal men.", 
"Divine Razor. A holy blade wielded by a paladin of a forgotten god said to be entombed in the God’s last temple.", 
"Keeper of the Celestial Grave. The last servant of a dead god roams in the mountains and knows of the his master’s final resting place.", 
"Fey incense. This incense smells of lavender and pine. It is said that if you burn the incense at a shrine in the wildest part of the woods, you will summon a kindly dryad.", 
"Chalice of the Spider Queen. This ornate chalice flows over with an inky poison, magically refilling whenever it is emptied. The chalice lies in an underground citadel guarded by dark elves. Many have died to procure it.", 
"Uncanny star chart. At a first glance, this chart of the night sky appears unremarkable. However, closer inspection will show that the chart depicts constellations that do not exist. He who can decipher the mysterious star map can navigate to a place where the veil between our world and the far realm is thin.", 
"Oracle’s die. This icosahedral die is hewn from obsidian. It is located in the tomb of a long-dead seer who met with a terrible end. To wield the Oracle’s die means triumph over the machinations of fate.", 
"Temple of Delights. High in the mountains and surrounded by golden mist, the Temple of Delights is a monument to a god of pleasure. Worshippers at the temple serve sumptuous banquets, wear fine silks, and indulge their senses according to each passing whim. Many seek to make a pilgrimage there, and few return.", 
"Duchess’s mirror. This silver handheld mirror has no magical properties or so the Duchess swears. The duchess’s jilted lover stole her favorite mirror, and she is willing to pay a hefty sum to whoever can retrieve it.", 
"Crown of the Oligarch. A platinum crown decorated with shining emeralds, said to be the crown that the leaders of the rebellion used to sway the population to their side against the first empire. After centuries of wars the crown was lost to time", 
"Merchant’s Map. The personal map of man who left his home and returned with a great bounty of wealth of origin unknown.", 
"Garden of Carminas. a medusa queen blessed by the gods had the ability to turn people into gold statues rather than stone, her island lair is covered in hundreds of statues.", 
"Grundzik's Lost Mine. Grundzik Goldpick led an expedition to set up a mine in the far mountains. Word came back of the abundance of wealth he had discovered before suddenly no word came back at all.", 
"Forge of the Heavens. Legends say that there is a mythical forge that was used to create the weapons of the Gods, any weapon made there is imbued with incredible holy power.", 
"Tears of Korharath. A set of gemstones of immense power said to be the crystallized tears of Korharath in his last moments. He was the lover of the goddess of magic and the first magic user to exist. He was burned on a pyre for his unnatural powers.", 
"Wreck of the Flayer’s Fleet. Strange evil artifacts begin showing up at private auctions in nearby cities. Tomb robbers have discovered a 2000 year old wreck of a Mind Flayer Spelljammer scout ship in the wilderness, and are scavenging dangerous technologies from it. One of the technologies is a beacon which, when accidentally activated, calls the main body of the Mind Flayer Fleet to reunite with the descendants of the Mind Flayer survivors in the material plane.", 
"A powerful wizard achieved immortality and was written about in the histories. Recent scholars now believe his residence was high atop a local mountain, now under a new name. If he is immortal could this wizard still be here?", 
"Vessels of Imarn - a wizard or artificer who found out how to plunge souls into constructs. Eventually wanting to become immortal he did this to himself. In his mechanical ever-shifting maze lies his laboratory, and along with it a thousand-years of treasures.", 
"Lunar Sword. Long ago a hero used a silver blade that changed in shape and power with the waxing and waning of the moon to slay a terrible werewolf. It is said that the blade was laid to rest in the Gardens of the Moon.", 
"Pirate Kings’ Diary. The diary of the pirate king who hoarded and pillaged for years. It has the location of all his secret stashes of treasure around the world.", 
"The Seraph’s Wings. A pair of real angel wings that are said to heal anybody who touches them of any disease.", 
"Kovvonanns tomb. the temple where a powerful barbarian that had the ability to rage like no other. His axes are rumored to still rest in his cold dead hands.", 
"Belly of the beast. A golden city home to an order of powerful wizards, said to hold a great many powerful magical artifacts and secrets. Was swallowed by an enormous beast.", 
"Shard of Awakening. Legend tells of a crystallised piece of pure divine magic left over from creation itself. This bright green crystal is a catalyst for life and is said to have caused ordinary animals to not only gain sentience similar to humans, but also to grow to incredible sizes and display powerful magic of their own. If it could do that to a mere beast, what could it do to a person...", 
"Paeso's Lost Tale. The legendary storyteller Paeso was said to have written one last story before he died. Its said to have been buried with him, and was actually based on an old legend about a lost treasure.", 
"Skyforge. A remnant of the Golden Age of Magic, and birthplace of many artifacts still used by heroes to this day! The island it was built on used to float through the skies of the world, but fell into the ocean during the spell plague. Many sailors claim to have spotted it over the years, but its current location is unknown.", 
"Aurintaura. The fabled 'Land of Gold' is said to lie to the far south through a sea constantly plagued by turbulent storms. Those who have made the journey and returned have all become rich beyond their wildest dreams, but many ships loaded with gold ore never made it back and still lie across the sea bed. The largest of these is the Aurintaura (The Golden Bull) Said to contain enough of the precious metal to line every road in the world!", 
"Mask of Ancestry. This ancient wooden mask is adorned with tribal markings from a long forgotten civilization. Rather then being the treasure, this item is easy to obtain, being in the possession of a collector all to eager to lend it out to adventurers under contract. The treasure comes from the masks power to see into the past of any object or location. The current owner used it on a single gold piece and saw a chamber full of gold coins that stretched as far as the eye could see. He wants you to find this chamber for him and share the spoils of the greatest treasure hoard the world will ever know.", 
"Archmage Statue. A remnant of the floating cities before the spell plague. Legends say this statue talks and can teach the secrets of magic... if it survived in one piece that is.", 
"Phantom bazaar. Once a year, carts and stalls mysteriously crop up along a street in the capital city. The stalls are translucent and shed an eerie glow. At this market, ghostly vendors sell their wares — cursed rings, possessed dolls, the weapons of long-dead warriors, etc. Here you might happen upon a powerful magic item or a dreadful curse.", 
"Sought-after blossom. This plant, known for its striking red flower, is the only surviving organism of its kind. A druid circle wants to bring the plant back from the brink of extinction, but there’s just one problem — a dragon is hoarding it.", 
"Island of glass. This island lies in the middle of a vast ocean, far from mainland shores. The sand on this island is imbued with a unique property — in the hands of a skilled glassblower, its resultant glass is unbreakable.", 
"Hidden noble. A nobleman has been kidnapped and taken to an enemy city. This city is inhabited entirely by shapeshifters, and when would-be rescuers come to save the nobleman, everyone in the city assumes the noble’s form.", 
"Pirate’s left hand. An infamous pirate offers booty to whoever can find his missing hand. It’s out there somewhere!", 
"Lucky coin. This unassuming copper coin always lands on heads and grants unwavering luck to whoever possesses it. The coin lies among countless other copper coins in a vault in a massive, well-guarded treasury.",
"Swamp Lurker: a six foot tall elven woman with skin lesions and leprosy ulcers. The Swamp Lurker has been spotted in swamps all over the world and is always carrying a lantern. Legends say that she was once a cleric that was desperately trying to cure her city of a deadly disease. Those who make pacts with her have the strange quirk of attracting flies. She has been known to assist travelers as well as kill them.", 
"Corrin: an artificer that had achieved lichdom through human transmodifications. Corrin is now more machine than man.", 
"Chained King: a large creature with black feathers and demon horns. The Chained King was punished by the gods for using forbidden magic. The Chained King now remains locked away by three chains, each will be broken if certain requirements are met. As of now one of the chains was broken when a woman gave birth to a beast.", 
"Fafnir: a 15 million year old red wyrm that has survived off of his unending list for gold. Fafnir uses his greed as motivation to remain forever living.", 
"Volk: a primordial living at the bottom of a volcano. Legends say when Volk arises from the volcano the entire continent will be lit aflame.", 
"Sobrick: a crocodile human hybrid often worshipped by lizardfolk who is said to spring from the bottom of the ocean depths to eat the sky when he escapes a maze of coral he is trapped in.", 
"Galia: The mother of all dryads, Galia is found in a forest in the feywild and is said to be 100-300 feet tall. Galia is responsible for creating seasonal change. If Galia dies she simply is reborn from her old corpse. Galia is lawful in nature and will only appear to those who she wishes to see.", 
"Watcher: an invisible entity with eternal life grated to them by the gods of death. It’s impossible to know how old the watcher is or where they are at any moment but what is certain is they are always gathering information. Warlocks have made pacts with The Watcher but even they have never talked to or seen them.", 
"Monolith: a monk that has been meditating for 2000 years. The Monoliths real name is Feng and he has not aged since he had been in meditation. The Monolith while being unconscious still has subconscious defenses. Many assassins have tried to kill The Monolith only to have their mind bombarded with psychic energy.", 
"William Greyhammer: a dwarven paladin that upon death was offered the opportunity to be the guardian of Celestia. William spends his days at the gates of Celesia making sure the people who enter are allowed there.", 
"Drakeslayer: a greatsword that was forged by a great cleric. Drakeslayer can speak telepathically and has a hatred for dragonkind. Drakeslayer is a +3 weapon and deals an additional 2d6 to all dragons.", 
"Behemoth: a 6 legged bear-like creature with chitinous plates and fur, a hairless head and sharp needle like teeth. Roaming the heart of the oldest forest in the land, its roar is audible from the villages near the edge. They say it sounds like the screams of thousands of creatures dying, and the war drums of a legion", 
"Goliath: a tiger-like creature with one pair of legs and a pair of muscular arms. It’s fur is thick and drips a dark viscous syrup. A head that looks almost reptilian in nature and thick sharp teeth like the heads of spears. It’s roar sounds like a screeching violin. On its stomach is a deep scar, scholars say the Goliath got this scar from a fight it survived with The Behemoth", 
"Spawn of Orcus: This entity is the result of an ancient summoning ritual gone wrong in the Underdark. 30ft in diameter, the Spawn of Orcus is an amalgamation of over a hundred humanoid corpses and skulls, fused together in a disgusting mutated formation of perpetually rotting flesh and bone. For centuries it has writhed in agony in a gigantic cavern known as the Sepulchre Sanguinis, where the original ritual once took place. Its agonizing wails can be heard for miles, and its only wish is it to spread pain and suffering to those who cross its path.", 
"Warforged Dragons: a peculiar species that was uncovered only recently. Warforged dragons are the rarest type of dragon and come in all forms of metals like copper, steel, iron, and even aluminum. The largest and most intelligent of the warforged dragons known is Gorashi. Gorashi breaths fire and poison, they have been known to make deals with mortals for knowledge they have gained in their lifetime.", 
"Barothgar: an orcish sorcerer that steals the remaining life force of the creature he kills. Barothgar has killed so many creatures that his estimated lifespan is 1.3 trillion years. Barothgar is a name feared by all orckin. Some old and sick orcs venture into his mountainous domain so that Barothgar can give them a warriors death.", 
"Phenrodna: A failed attempt at creating a being with the power of sorcery artificially, Phenrodna is sealed inside a large gemstone through the use of the Imprisonment spell, and has been for many hundreds of years. Originally a normal human, it has lost that humanity, the wild magic coursing through its veins mutating it into a mercurial form that is ever shifting, while also driving it insane, and making it exceptionally powerful. It can be released from imprisonment by three kings simultaneously touching the crystal.", 
"Karthonon: a lich that lives in the feywild and is worshiped by the fairies living near him. Karthonon uses his worshippers as subjects for his alchemichal experiments. Karthonon is as of now not very well known however many of the feywilds best divination wizards forsee of a dark being using his power to destroy the summer court. Whether the being succeeds is uncertain. The dark being these wizards see is Karthonon.", 
"Weeping King: A ghostly apparition that resides in a lonely, decaying long hall in the wetlands. Tears seem to eternally flood from his eyes and his hellish wail drives men to their knees. When he holds aloft his chipped, rusted sword a host of long dead warriors manifest around him", 
"Kumbaka: a dragonborn bard that was one of the first dragonborn ever born into existence. Kumbaka spent his life learning as many instruments and languages as possible. One day using his charm and cunning Kumbaka made a bet to a god of magic that if they couldn't kill him before he was done with his preformance tomorrow was over then he would be unable to age and won't die until they are finished counting to infinity. The god of magic agrred to this bet with confidence but on the night of the performance Kumbaka was nowhere to be found. Kumbaka had actually preformed in a different plane of existence which bought him enough time to finish his preformance before he could be found. Kumbaka knows that the god is almost done counting to infinity amd is planning one last show three years from now. In his life Kumbaka had learned to play 13 instruments and can speak 6 different languages. Kumbaka is proud of his accomplishments and is ready to die.", 
"Hermit of the Glade: No one knows how old he is, but he has always been there, and will always be there. His house is well maintained, though of low quality. For some reason no one ever bothers him, and few even bother to visit. He is always polite, helpful and could even be called friendly by those who have tried to visit. Perhaps he is some old man blessed/cursed with immortality, or perhaps there’s more to his story.", 
"Beast: A boar that has lived in the underdark for 1000 years. He was ordinary boar that grew too large. Throughout the ages hunters have tried to slay The Beast, but none have triumphed. The Beast has only grown, both in size and hatred. His thick hide bristles with the spears and blades of the hunters and warriors it has bested.", 
"Früdwark The Elder Giant: no one is sure if Früdwark is a storm giant or a separate breed of giant entirely. Früdwark is by far the largest and oldest giant known to giant kind. Früdwark has no concern for other giants, dragons, or mortals and simply wants to be left alone. Früdwark has a distaste for dragons especially because dragons seem to be the creatures that are always trying to pester him the most. Früdwark has been known to make deals with mortals so that they can stop bothering him and so that they can kill dragons who bother him.", 
"Filtara: the oldest dracolich still alive. Filtara was the creature that had taught mortals to achieve lichdom at the cost of their servitude. Filtara was betrayed by her servants and was banished to an endless void somewhere in the shadowfell. When Filtara escapes her prison she will plan to make all humanoids extinct for what they have done to her.", 
"Ythandr: a pit fiend that owns the endless library which is a huge landmark in the nine layers of hell. The endless library is considered the library with the most books and information within its walls. Those who make too much noise in the library are swiftly dealt with by Ythandr. First time offenders are warned and left with a painful burn mark, second time offenders are taken to an area of the library simply labeled 'pain room'. It's a mystery what happens in the pain room but each offender spends 20 years in it and always leave with the parts of their brain pretaining to memory removed and given back to them in a jar. Ythandr is one of the very few devils that were born before the nine hells existed.",
"Trader: a quiet, strange being who pulls a cart full of strange magical items for no known reason. They wears a cloak that is always oily for some reason, a mask that completely hides their face, and large leather gauntlets that go up to their elbow. They only accepts other magic items of equal value for trade, and their stock is completely random, one day they may have only a +1 dagger, the next they may have multiple +5 vorpal swords. They are immune to all magical effects, including any forms of divination. If a PC asks a god or being with similar power about them, the god/other being will have no clue who they are talking about. They are friendly to the party, but will refuse to leave their cart or reveal any skin no matter what.", 
"Poison Tree: The Primal Aspect of Knowledge, both good and ill. Uncovering new information is to be celebrated, even when it brings about ruin. Some scholars believe the tree is purely a metaphor, written about to conceptualize complex ideas in a primitive age; some believe it to be real, and strike out on lifelong journeys to find it and eat of its fruit.", 
"Eros: Referred to as 'The Mother of Monsters' in common parlance, this entity shares its name with the later goddess of love, though Eros is far more primal. It is love and lust in all of its forms, and its offspring and faithful are hybrids of monsters and humanoid species. Violent and terrible, the Forbidden Plateu of the Cult of Eros is home to rare species of beast and plant life. The very air there is said to corrupt mortals beyond recognition, twisting them into amalgams of man and monster.", 
"Iron Pillar: Deep in the earth, it sings an endless song to all who dig toward it, though they do not understand it. Those who find it, fall to their knees in worship and expire in mortal terror.", 
"Pig: a very strong woman with the head of a boar. The Pig can be found anywhere and everywhere as long as there is dim light. The Pig is a lawful neutral being that punishes those who try to defile the laws of nature. The Pig is said to be a failed experiment on how to prevent hunger but why the entity has lived for such a long time is beyond explanation. Those who have been killed by the hands of The Pig are found with no face and black ooze bubbling from a hole in their chest.", 
"Yawning Willow: A sentient tree that speaks via the wind blowing through its leaves. The Yawning Willow is so old that it invented the language of druidic and has taught some of the first druids the ways of nature.", 
"Rinoir: he uses the body of a human once sworn in pact to Rinoir, now an avatar to him, as a demonic machine that has twelve mechanical arms protruding from the human’s old, withered, and blackened corpse. Rinoir is desperate to find a new host as his current one is getting more and more fragile as each year goes by.", 
"Duke of Stone: a 20 foot tall being made of various stones and metals. The Duke of Stone is near impossible to describe due to their alien nature but some defining features are its many eyes and sharp, jagged body (if that even is a body at all). The Duke of Stone is a creature who takes joy in learning of its prey before petrifying them and engulfing their stone body into its horrendous figure. The Duke is always joking about how it 'eats' and 'sleeps' like a fleshbag, thinking of any creature smaller than him as a toy.", 
"Qpljhyt: an entity made of a pink fleshy substance that forms into a circle. The name of this creature cannot be pronounced by any creature except for gods and powerful aberrant mind sorcerers. Qpljhyt has been around since the creation of the material plane and will only give information to those who he wishes to give information to. Qpljhyt cannot attack but can use a special reaction to force a creature to make a DC 28 intelligence saving throw, on a failed save the creature is reduced to 0 hit points and on a successful save the creature take 30+20d12 force damage. Any creature reduced to 0 hit points by Qpljhyt are erased from time and space. Qpljhyt has a hit point total of 4000.", 
"Talveer: A roughly humanoid figure made of grey living ropes bound together, wearing rough clothing that seems to be made from parts of various clothes and other materials sown together. They wander the wilderness, if encountered by heroes or others with potential, they will offer a strange quest. The rewards will be good, but the consequences of failure morbidly bizarre. Accept the quests at your own peril, follow every letter and you will be rewarded, a single mistake will be worse than death.", 
"Night Owl: an immortal being who owns a demiplane where the sun never rises and the party never stops. Those who get trapped on his plane cease to age with the downside of never being able to escape the endless party.", 
"Birds: Ancient beings of Shadowfell that seep into the material plane through their disciples. Nobody knows where The Birds came from or what their true intentions are, as each of their followers are given a different set of powers and directives, but they are powerful. Those who know of their existence speak of visions of thousands of voices speaking at once, being in the center of a tornado of black wings, and an overwhelming sense of dread.", 
"Thornhart: A very old, forgotten god of life and nature, may be offspring of (insert your god of nature). His appearance resembles a massive hart with white fur tinged with green as if moss has been growing over him, with antlers made of interwoven vines covered in blooming flowers of all colors. A rainbow rack, it's called. Once long ago he was worshipped as a god of protection, rewarding those living close with nature. Now all he protects is his own Grove, mostly forgotten by all except the oldest of druids. He is standoffish to an irrational degree towards all but the most reverent of druids.", 
"Stormpale: A very old, forgotten god of war and death, may be offspring of (insert your god of war). His appearance is a massive falcon (about the size of a young red dragon) whose feathers are so black they seem to drink the light. He appears as though he's a shadow in the sky, or rather, a shadow projected onto the sky. The only part of him that is not inky blackness are his red eyes, which don't so much glow as they seem to reflect light back in a red haze. Seeing him in the sky has long been considered a very ill omen, portending war, famine, or death of some sort. However, at this point, being forgotten for so long, he is simply lonely, and is content to have a conversation with anyone.", 
"Arachae Cythalia: roughly translated from deep speech meaning queen of spiders, Arachae Cythalia is a spider with an old hags face and human feet on each of its ten spider legs. Arachae Cythalia has been building a web from the deep realm to the material plane and she will soon achieve her goals. Arachae Cythalia believes she deserves to be the goddess of spiders and intents to kill the current god of spiders. Arachae Cythalia gives birth to a freakish human spider hybrid race that has not been seen by anyone in the material plane. The ettercap species is considered a perversion of spiderkin to Arachae Cythalia and plans to cause a mass extinction to all ettercaps.", 
"Dreamstalker Child: an undead entity that manifests primarily in dreams, travelling from one dreamer to the next. It appears as a young child with an indistinct face that cannot be remembered, wearing a tattered grey linen tunic. If the dreamer reacts with fear or hostility towards the child, it will begin stalking them during waking hours. Small knife cuts will appear on the stalked person's body. If they walk near a dark doorway, they will feel a small hand grab them and try to pull them inside.", 
"Golden Thrush: a small, plump bird with large, inquisitive eyes. Its plumage is brilliant gold, with brown spots and a white underbelly. Its song is a sparkling high-pitched trill, audible for miles. It is actually a remnant of the consciousness of an ancient forest spirit. If it witnesses someone damaging the forest or attacking the native creatures therein, it defends its domain by diving at the trespasser at incredible speeds, plunging through their body like a bullet. If fed mistletoe berries, it will grant a boon and safe passage through its forest.", 
"Warden of Agathys: a large muscular devil with blue skin and horns made of ice as well as a pigs nose. The Warden of Agathys hold the flail of punishment which is a +3 flail that magically causes painful spasms. The Wardens job is to punish sinners who were vile enough to make it into such a deep layer. After doing the same job for three millennia The Warden has perfected the art of torture to a science.", 
"Duchess of Wasps: a giant wasp with a head set ablaze with purple fire. The Duchess of Wasps can speak telepathically to creatures and loves to feast on mortal flesh. The Duchess of Wasps very rarely allows for deals to be struck with mortals but when she feels generous she allows for them to get power in return for food that her children may eat. The Duchess of Wasps will lay eggs in her victims and wait for them to hatch. Her lair is filled with wasps and corpses of humanoids, goblins, trolls, dragons, beholders, etc. Legends say that The Duchess of Wasps was once a druid that has transformed into a creature as disgusting as her heart, others say she was the first wasp to ever fly, whatever her story is nobody can deny how old and how powerful she is with near impossibly potent venoms, acids, and Psionics capability.", 
"Epok, Tilin, and Merq: The Planestriders: A trio of Alhoons that travel between planes successfully hiding for decades at a time. Every thirty years, they return to the Material plane to repeat their ritualistic sacrifices to extend their lives. They target weary travelers on quiet secondary roads. The story of these planestriders is thousands of years old.", 
"Scourge: a giant reptilian beast from a time long before man existed. It resembles a Tyrannosaurus with wings and horns. It can use a sonic roar as a breath weapon and break down fortified walls. It is said any city he visits is depopulated and left in ruins.", 
"Gnorman, The Gnomish Sythesist Summoner: He's an incredibly old gnome who at this point cant survive outside of his eidolon and is incredibly powerful. He spends most of his time making discount magic gear and supplies for the needy. The eidolon takes the form of a large mass of black tentacles.", 
"People's God: A sentient, if simple mind created on accident via the arcane architects when a great ritual tripled the size of their city overnight. The People's God, or 'Ol Watchful, as it's called colloquially, is omniscient within the walls of the city and can be asked questions via prayer, though the answers are vague at best, nonsensical at worst. It's whispered that a band of vigilantes and a handful of neighborhood watches have learned to access it's knowledge in a more precise manner, and will go to extreme lengths to keep that knowledge out of the hands of the law. Many have claimed to see Ol’ Watchful but appearances vary from story to story and usually come from unreliable sources.", 
"Heart of The Undead: a mass of black flesh and rotten plant matter located in the shadowfell. The Heart will convulse occasionally and create a wave of necrotic energy from its convulsion. Any non undead who are within a 200,000 foot radius of The Heart while it convulses will take 4d12 necrotic damage. Those who die from the necrotic wave are resurrected as zombies. It is uncertain of the connection between The Heart and undead as a whole but it seems like undead try to protect The Heart.", 
"Shatterquake: An ancient continent-sized Earth Elemental. It is said its steps could cause the very continental plates to shift. It slumbers now, and a family of Halflings have began unknowingly cultivating life from its back. One day, it may awaken.", 
"Yiith?: Long ago. when a cerebrilith devoured the mind of a minor god, its temple home was sealed away, the whole pocket dimension locked for eons and eons in fear of the demon leaking out divine secrets or power into the rest of the world. When the makeshift tomb was finally unsealed, all that was found besides bones and dust was a single sea snail, dull and healthy. It MIGHT be the cerebrilith Yiith, morphed into this inconspicuous form as a disguise or a side-effect of absorbing the god's magic. Either way, the explorers that raided the ancient home knew of its history, and have taken great care to ensure that this possibly-volatile creature stays under lock and key.", 
"Saurothid: What remains of an extremely powerful fiendish entity that was heavily wounded long ago. It is mindlessly spawing lesser monsters in its crippled state, and despite having powers that exceed even the most powerful wizards, it wants to die and will not actively resist against the party trying to kill it. Though it’s endless army of lesser devils and its aura of heat and darkness will still make killing Saurothid a difficult task.", 
"Fuishtar: known by some as The Great Scorcher, Fuishtar is a gargantuan fire elemental that can speak directly to the god of war. Fuishtar is a servant to the god of war and is used as a messenger by the god of war. There is a legend of a battlefield where both sides prayed for the removal of a tarrasque so that they may fight. Their prayers were answered and Fuishtar stayed the monstrosity, the cost of his services is that all tarrasque from them onward had immunity to fire.", 
"Illumin: They are not known to engage with humans openly. But now and then, those who went spelunking or miners trapped in caves found themselves either led out by a mysterious light being. Or sometimes, led deeper in. The stories told around them are often suggestive that when someone becomes trapped in the dark, they measure a person by whether or not they bring light to others. Then choose to appear and lead them to whatever the Illumin wish them to see. Perhaps it is safety or their end. But whether or not the beings truly gauge such things or if they are each with their own whims and choices is not known to mortals. The Illumin themselves are creatures of the dark, deep, and below places. They are often compared to feyfolk or changelings but some scholars have theorized they share things in common with bioluminscent cave mushrooms or spores. They disappear in areas of light, and can shape themselves as they wish. Another more accepted theory is that they are the result of hallucinations and that they do not truly exist.", 
"Jack O’The Roadside: A tall, pale human man in patched suit who casts no shadow. He is seen by travellers on the side of the road at night, playing a golden harp and inviting them to dance. Should they dance his beautiful melody he will begin to up in tempo until it’s the fastest song in all the lands. It is said that those who can keep up with Jack are granted good luck for 7 years but those who fail encounter naught but misfortunes.", 
"Altabach: A large snake, in the upper range of an anaconda, with off-white scales and black eyes, fangs, and tailtip. Letters and words crawl over his skin like living text. He hoards secrets, and will answer two questions in return for the tongue of one's lover and the liver of a faithful hound.", 
"Stro The Patient: An immense egg that, at first glance, appears to be made of stone. It is sunk partway into the ground, and lichen grows over its surface. No one is certain for how long it has lain there, but there is no doubt it is alive: it's surface is warm to the touch, and a slow pulse, almost like a heartbeat can be felt by those standing near to it. Those living in its proximity may find themselves falling under its psychic influence and performing strange tasks. The ultimate goal of the unborn creature, as long as if and when the egg hatch, remain unknown.", 
"Mother Hornwort: Ancient even by hag standards, Mother Hornwort's hunched figure emanates an aura of power. She rides a giant stork as a mount, and has been known to feed it those she dislikes. She is avoided by sensible folk, but other hags sometimes seek her out for her knowledge, services, or to offer supplication in hopes of earning her favour.", 
"Giants Shadow: a peryton that has survived thousands of years feeding on hearts and slowly growing. The creature is now larger than a wyvern and its shadow resembles a giant instead of a human.", 
"Soul of Winter: a glowing blue light in the shape of a woman that appears on the coldest night in winter. Many have theories on who she is and why she comes but they all vary from culture to culture. One culture believes she collects the souls of the dead to be judged, another says she is a frost hag that revels in making the coldest nights even colder, some say she’s an illusion brought by frigid weather on the eyes of naive travelers, no one will really know for certain.", 
"Umaraka: a gargantuan sea serpent that guards the entrance into the abyss. Umaraka is worshipped as a god of darkness and the sea by many cultists. Umaraka can speak to its followers through dreams, usually asking for more living creatures to be sacrificed in its name.", 
"Forgotten King: a once great king that fell upon a curse that would slowly turn him into a god of madness. The gods knew that while they could stop his horrid new form from arising they couldn’t help but watch as the abomination unfolded before their eyes out of morbid curiosity. The forgotten king has been cursed for 500,00 years now and looks like a deformed werewolf, having one hand being larger than the other, a horn protruding from his eye socket, sickly white colored fur, and pure white eyes. The Forgotten King has never transcended into godhood for the other gods refused to allow it. He now waits in his castles ruins waiting for his daughter (who’s been dead for many many centuries) to come back from her coronation as princess (an event that happened when he was still happy). Hearing him ramble on about how proud he is and how he will celebrate with tea can bring any man to tears.", 
"Sabaramha, The Dark Empyrean - The daughter of Tharizdun, Sabaramha is a six armed empyrean exceptionally talented in swords and life magic. Instead of the normal healing abilities that life magic would normally imply, Sabaramha's skills lie in the manufacture of diseases that can wipe out civilizations or the forced evolution of violent magical beasts.", 
"Oreglai, Shadow of Death - Oreglai appears as a giant rotting crow with a 2 mile long wingspan. All plants caught in its shadow wither and die, while creatures are afflicted with a horrible despair that can cause suicidal thoughts. Oreglai is infested with billions of insects that often reach gigantic sizes.", 
"Krullajer, The Fear Tyrant - This golden great wyrm turned shadow dragon feeds of fear itself. Fearing Krullajer himself will empower him and grant him immortality. Whereas, simple fear in general will also strengthen him, yet to a smaller degree. To seal away Krullajer, the gods built a magical artifact to make everyone and everything forget him. This artifact becomes more fragile as general worry, doubt, and fear spread across the world.", 
"Asherl-Khan, The Guilt of Gods - Khan, the former god of glory, was slain and reanimated as this undead husk of a god. Khan's artifact, The Mantle of Glory was also transformed into The Mantle of Guilt which now exhales an impossibly black fog that reanimates the fallen and converts undead into following Asherl-Khan's will. The other gods were too ashamed to face their former friend and thus had Sigil's Lady of Pain seal him away in one of her mazes.", 
"Voltius the Eternal: the oldest known vampire of the world. His large age and the gigantic quantities of blood he consummed granted him god-like abilities relate to his condition. He can smell any warm-blooded creature in a 3km radius, control blood with telekinetic power, making him able to slow down heart-rates, extracting precise quantity of blood, giving blood related diseases, etc..., shapeshift into anything, turn invisible, and is immune to any anti-vampires techniques. You can see his reflection in mirrors, holy water feels like water to him, he can go anywhere no matter if he was invited or not, sunlight doesn't do anything to him...The list goes on.", 
"Renegade God: A Nameless God who, in ancient times, sided against his fellows Gods. His name was erased from history, an he was chained deep beneath the earth.", 
"King of Flames: A powerful Titan residing in a blinding palace on the back of a giant Phoenix, by which he travels the world.", 
"Three-Faced Tree: An enormous and ancient oak with three humanoid faces protruding from it. They will answer any question: one of the faces always tells the truth, one tells what the traveler would want to hear, and the last one always lies.", 
"Xurv: a death tyrant located somewhere in the abyss. Xurv has no grand scheme or plan to conquer, he simply enjoys inflicting pain. Xurv will float above the abyss scouring one layer at a time trying to find demons. When Curv finds one he shoots a laser at it obliterating any trace of its existence.", 
"Pam: a frail old human woman who just never seems to die. She has outlived her children, grand children, great grandchildren and so on for so many generations, but the pain of loss just doesn't seem to dissipate. This has left her a bitter old woman. She holds intimate knowledge of ancient societies because, well, she lived there and she often yearns for the 'good old days' when only sorcerers could make fire and magic couldn't be learned by any idiot who could open a book. She has attempted and failed at ending her own life and having it ended for her by provocation, but recently she has altered her strategy in life and is using her knowledge to indugle in a little necromancy. If she won't die, then neither will her great-great-great-great-great-great-grand children. If she succeeds, she will be united with her huge extended, risen again, family.", 
"Forge: The Forge is a sentient entity...a golem of sorts. The Forge acts more as a portal when a hero commits their first great deed (I.e. slaying a dragon or protecting a kingdom) the Forge will appear out of nowhere, often emerging from nearby water sources of from the shadows. its 12-foot tall stature consumes the hero and they wake up within the Forge. They have the honor of watching the forge create their very own custom magical weapon.", 
"Old Rambler: A bark-encrusted quadrupedal humanoid with a skull that channels it's slow breaths through pipe-like protusions. It’s breath acts as a thick fog and any living thing that breathes in the fog takes constant acid damage, but is revived with increased vitality an hour after leaving it's presence. The Old Rambler wanders slowly through the swamps of which it is considered a patron.", 
"Walker: Nobody's sure of this being's real name, or even what they look like; the Walker has appeared as male, female, elven, human, dragonborn, and many other races besides. Regardless of their form, the Walker is always found walking down a road or path, surrounded by golden motes of light. They have never been seen leaving or arriving anywhere. If the Walker is spoken to politely, they will reply and offer to grant the person 'a light to watch their path'. When the person accepts, one of the lights that surround the Walker will start orbiting them instead, and will keep doing so until they die (when it flies off in a straight line, presumably back to the Walker.) If questioned about the direction of their journey or why they have lived so long, they will reply, 'Does the walker choose the path, or the path the walker?'", 
"Myriad Faced One: a colossal entity that has tens of faces and hundreds of arms. He lived for trillions of years and is located at the intersection of all the planes of the multiverse. His goal is to fusion all planes to create a single perfectly balanced plane.", 
"Ugami: the first ever skeleton, sometimes called the ever-living warrior. Ugami had made a pact with a warlock to remain living forever so he can fight for eternity. The wizard agreed and now Ugami lives in an ancient dungeon waiting for his next foe. Centuries underground has left Ugami completely insane.", 
"Melezabeth: A severed undead head of an ancient giant, kept unliving only by its unsatiable gluttony. It has no bowels and everything it devours comes right through it, chewed and dropped from between all tangled sinews and veins that hang from its stump of a neck, all resembling grotesque tentacles and pseudopods. Melezabeth is mostly immobile, sitting atop of the ancient bottomless well, losing all its meals to the void beneath it. It can crawl, albeit very slowly. It can't be satiated, even with the help of its many cultists, which sacrifice countless victims to Melezabeth's all-devouring maw. Its minions suckle black goo from its disguisting arteries, like lambs of an undead goat, which gives them supernatural strength to do Melezabeth's bidding. They say the head has hypnotic abilities and when fought, it will often cannibalize its minions to instantly regenerate portions of health, catching prey with veiny tentacles and shooting nauseating goo from its swollen body.", 
"Cottage: Deep in the Far Realm, protected by an unbreakable bubble of force, lies a small, picturesque, thatched country cottage, floating on an floating island of land with a small pasture for two or three sheep, a small wooden shed, and a vegetable garden. Two elderly humans can occasionally be seen, puttering about the garden, milking the sheep, or caring for the cottage in some way. Ancient tomes and beings with such knowledge describe them simply as The Husband and The Wife, but that is largely the entirety of knowledge about them. They, or similar beings, have lived in The Cottage unchanged for millennia. The bubble in which they exist is utterly unbreachable, even by divine power or spells that effect the nature of reality itself, such as Wish. Any attempts to reach the inside of the bubble result in the breacher being hurled from the area with insane speed and force. Anyone attempting to contact the couple through the bubble will be greeted with friendly nods and waves, but no other attempts at communication.", 
"Abstract: The result of a failed attempt at Lichdom. The wizard was left a torn and deformed being; immortal but cut off from magic. They cannot cast spells of their own. Instead their aura perverts the magic of those around them. Twisting and tainting the effects of spells and magic items or weapons.", 
"Chirpy: A delightfully round songbird. Nobody can fully identify its species but know it to be a magical being of some kind. Chirpy is a primordial creature and despite having powerful magical potential still has the mind of a bird. They cannot be killed permanently by anything short of a god and when out of sight are capable of traveling from one point to another in an instant. Chirpy finds people interesting and will follow anyone who shows it affection.", 
"Liliveth: An ancient Oracle of a long forgotton deity who lives on an island in the middle of the ocean. She represents the turning between day and has two presences: She who walks the light, and she who walks the dark. She resides in two temples built into opposite halves of a mountain. The light temple is filled with light and magic based puzzles. The night temple is filled with dangers and fights taking place in magical darkness. At the end of each, she is sitting upon a throne. Small and frail but radiating with power. In the light, she will answer any three questions you ask, three answers, two truths, and one falsehood. In the dark, she will answer one question per individual, but the answer always rings true, and the asker may not like the answer. After a group leaves her temples, they will not open their doors again for anyone for 1,000 cycles of sun and moon.", 
"Savior: a 7 foot tall angelic being with large white eagle wings, unnaturally pale skin, and no face. The Savior is rarely seen and seldom heard of. When a hero is doomed The Savior will come down and protect them from the fatal blow. Some say The Savior is a solar of the goddess of fortune but it is impossible to say for certain. Sightings of The Savior go back farther than elven history.", 
"Keeper of The Body: a large grey mass that gives off immense amounts of heat and exists just beyond the edge of the universe. Very few have spoken to it but those who have had to pass an intense trail of strength to unlock a stone door with celestial writings saying 'I Feel All'. Those who have spoken to The Body gain a feat called Fragment of the body which grants the creature +2 constitution and advantage on constitution saves. The Body tells all it meets that it must reunite with its kin.", 
"Keeper of The Mind: a large blue crystal with other crystals attached to it resembling a pattern that gives off a strange sense of pressure and exists just beyond the edge of the universe. Very few have spoken to it but those who have had to pass a difficult trail of mental fortitude to unlock a stone door with celestial writings saying 'I Know All'. Those who have spoken to The Mind gain a feat called Fragment of the mind which grants the creature +2 intelligence and advantage on intelligence saves. The Mind tells all it meets that it must reunite with its kin.",
"The Living Mountain – What happens when really powerful magic items are placed into a tomb and truly forgotten? A cache of powerful magic items began seeping magic into the earth around it, causing the very stone to come alive. This mountain takes the form of a massive humanoid shape. The only way to stop it is to traverse the dungeon in it’s body and remove the magic items.", 
"Y’uum, The Evergrowing – This massive creature is a mile-long collection of spores and mold that travels slowly across the landscape. Food and plantlife instantly wilt and go bad when Y’uum is near. If Y’uum comes into contact with a living creature, it will slowly burrow into it’s skin, eating it from the inside out.", 
"Nimir, Demon Lord of the Ruinous Oblivion – A massive, nearly invisible figure draped in long, disgusting cloth. Nimir oversees the creation of wraiths. When it is time to create a wraith, Nimir descends to the ethereal plane and infuses a soul with a massive rush of negative energy. If one looks directly upon Nimir, it will almost look like you are looking at a mirage.", 
"Shuggdus – The gargantuan, monstrous-looking, water-based creature. They have powerful hearing, especially underwater. The Shuggdus move along on tentacles instead of legs. They are completely blind and rely on touch and sound to get around.", 
"Yazothle – A formless blob that consumes everything in it’s path. It gains the knowledge of anything it eats. The souls of the eaten are sometimes seen trying to escape the creature’s ooze-like body, but to no avail. They are trapped for all eternity. Whatever this creature consumes increases it’s size.", 
"The Dreaming Maw – A castle-sized crystal floats above the ground, every so often pulsing red. Its lower half goves way to a mess of tentacles, some hundreds of meters long, that twist and writhe ceaselessly. It moves slowly, inexorably, for reasons unknown, and as it does the lands near it warp; first gaining a slimy texture, then sprouting tentacles, eyes, mouths, arms, then becoming those things until there is no trace of nature in them, only squirming fields of flesh. From these places sometimes life emerges, but not as life known to Men. Floating orbs of flesh and eyes, nearly normal creatures with grotesquely large features, fragments of stone from which sprout tentacles, and many other forms which cannot escape and fall back into the warped earth before presumably being destroyed.", 
"The Bickering Hydra – This creature started off as seven princess sisters who constantly fought and bickered among themselves, while their kingdom fell apart around them before armies of monsters. Because of their cursed bloodline, their ugly heads are now positioned on seven serpentine necks of a giant hydra-like monster, so they must share the same body and cannot escape each other’s presence. Their domain is the ruins of their kingdom, full with twisted, chimeric monsters.", 
"Gar-Khoza – Strangely enough, this gargantuan beast is quite passive, usually not paying the living much attention and only ‘feeding’ on corpses and dead plant matter. It resembles a giant amalgam of body parts from various creatures formed into a vaguely humanoid shape. Its state of decay, or lack there of, makes it seem much younger than it actually is. It’s an entity of rot, exhaling and surrounded by a necrotic mist. The occasional animal will make their home inside it, usually a swarm of insects or a vulture perched on its back. It shambles around aimlessly, leaving a trail of harmless, albeit alien, fungi and bugs in its wake. It’s known to defend itself violently if the need arises.", 
"Gzgeth, The Wandering Maw – This bulbous abomination closely resembles a starfish, but house sized (but technically never stops growing). Long arms that extend out radially, as well as thousands of tube feet that propel it forward (see starfish movement). On the top side of its body where all the arms originate is a massive radial maw that its arms are always dropping things into. Its maw contains layers upon layers of teeth all the way into the gullet. The maw emits such a stench of decomposing matter that the word ‘stench’ makes it sound pleasant.", 
"Seklitlosri, The Black Tear – A massive winged toad with tentacles on her head to bring prey into her razor teeth maw. She has amassed a group of followers who collect her tears in urns. Any living creature that drinks from water polluted with the substance mutates into a toadish creature like them.", 
"Borovoi – A towering creature of long thin limbs, it hides among the trees, taking the appearance of the forest it inhabits. Preferring the flesh of the apex predator, the Borovoi attracts woodland creatures to serve as bait. The bait is kept docile and unaware, luring the hunter close enough to become the prey.", 
"Aspect of Fenris – The shadow of a giant dire wolf of the Apocalypse. The howl of the aspect blots out the sun and shakes the earth.", 
"The Clone Worm – A cosmically large worm hundreds of millions of kilometres across, consisting of the warped and deformed bodies of countless assimilated civilisations. The worm senses and is attracted to the formation of empty husk bodies, like those formed by the Clone spell, and when it draws close enough to be seen twisting and turning in the sky, any creatures created through cloning or through creating genetic copies come out wrong, deformed, warped, often beyond recognition at all, sometimes huge and bloated and other times spindly and wicked. Interestingly, this also affects creatures who have used teleportation magic, as well as any who have been reincarnated or resurrected.", 
"The Vrenbliock – A gargantuan monster consisting of nothing but murderous eyes, hundreds of long spiny arms, and a large mouth. It disguises its grotesque body as a cloud. It uses its hiding place in the sky and its long arms to reach down and pick up unsuspecting prey. The only problem with its disguise is that it’s closer to the ground than most clouds.", 
"Crealeth – A hulking monstrosity that waits in the darkest depths. A fleshy transport for the vile creations of the aboleth, the Crealeth is a large whale like creature covered with pustule abrasions that constantly leak a black tar. The creature is host to an exposed maw of needle like teeth as large as the fiercest warrior and a row of blind eyes wrapping around its large dome-like head. The Crealeth is a means to an end, an unstopped leviathan carrying in its stomach the oozing and decaying armies of the aboleth.", 
"Tagrabui, the Rotten Being of the Marsh – A gargantuan half-decomposed bear with sloth-like front legs, blind eyes and moss growing on its back. Drool drips from its ever open maw: it ultimately hungers for the Sun, which it’s destined to devour when the time is right. Being in its presence causes the sensation of drowning and objects around it act as if they were underwater. Certain swampland tribes, who do not know any better, worship it as a god of death and rebirth.", 
"Cavestep, The Hill Titan – Thought to be creatures of legend, a Hill Titan rests only a few hours from the player’s hometown. In appearance, they resemble a hill giant, but are much bigger. The back of a Hill Titan is covered in a small mountain range. When they awaken, they rise from the earth, taking everything that was built on top of it with it.", 
"Graveteeth – This graveyard golem is the result of a necromancy spell gone horribly wrong. Instead of ressurecting a single corpse, this necromancer unknowingly gained a massive boost of power from his patron and ended up ressurecting the entire graveyard. Made of rotted limbs and tombstones, this shambling creature can be smelled long before it can be seen.", 
"Drak’Munshoo, Eater of Stars – This ancient lunar dragon resides on the dark side of the moon in your fantasy world. When the moon is full, it’s iridescent scales light up and it shoots across the sky, feeding on small stars. What is commonly mistaken for a shooting star is actually the lunar dragon flying across the night sky, belly full of stars.",
"The Herder – This massive worm takes residence in the temperate mountains and spends just as much time above ground as below. It’s primarily herbivorous, swallowing small forests for it’s meals. The herder has an odd fascination for the goats of it’s mountains, watching them as a past time. If any harm comes to its goats, the worm will do everything within its power to destroy the attacker.", 
"Turukto – Told to be a gift from the gods of nature, these crane like creatures stand almost 120 feet tall. They mainly act passive against any creature that approaches it, and if dared one may climb onto its wooden body. On its legs sprouts orange fruits of bittersweet honey that goes well with the view from the top of their body.", 
"Jericho – An enormous cannon that fires highly destructive bolts of demonic lightning. Around it grows the living flesh of a tormented siege beast who relies on the cannon to act as its spine and controls it directly with its brain. This ‘creature’ resides in the Nine Hells, eagerly waiting to be used for war.", 
"Roga’th the Unmoving – Legend says it is a massive statue that appears to be praying to a god in a field. It is instead luring travelers and creatures to investigate where it will then smash it’s hand down, killing most creatures caught under it instantly. It is unknown how this statue has appeared in almost every continent. Perhaps it is magic, or maybe perhaps there is more than one. One thing that is certain, however, is that it always seems to appear near holy sites…", 
"Skylla – A gargantuan creature that lives near coastal towns. She resembles a Hydra in form. Skylla has six heads, and will devour crewman with each of them of any ship that comes too close. She eagerly waits beneath the waves for oncoming sea vessels.", 
"Nüthmetaya – A gargantuan snake, the size of 20 men around and easily 200 feet long. Many a myth has been based on this beast. Despite the many tales, it is strangely passive, preferring instead to feed on tiny organisms in the waters it swims through. Though it lives underwater for most of its life, it does surface once every 70 years or so for one week to refill its massive lungs. It possesses immense psychic abilities, and uses these to communicate, or to defend itself in the rare occasion something actually threatens it.", 
"Totoma, the Golden Calamity – Before you stands a dragon unlike any you’ve encountered before. Standing 30 feet tall and at least 50 feet long, Totoma has a mixture of draconic and feline features. His face is an elongated feline face with swept back cats ears and long whiskers, with intelligent amber eyes. A pair of white bone antlers rise from the back of his skull. His elongated body is covered in golden scales that seem to shimmer black, giving the appearance of shifting leopard spots. Around his neck these scales are much larger and longer, giving the appearance of a mane of golden blades. Each of his four legs end in massive paws with wicked hooked claws.", 
"Akuma, Beast Of The Dark – A giant bear that sleeps within the forest and protects it from harm. Those that dare to enter his domain and harm it must pray that he doesn’t find them. For the ones he manages to kill, he feeds them to his forest friends.", 
"The Skeletal Titan – The Skeletal Remains of long dead immortals, be they titans, fiends, or even celestials who fell in battle in the wars of the distant past, their corpses may have been left behind and now all that remain are their skeletons, enduring like adamantine. Only the most powerful of necromancers can reanimate these remains, which act as powerful siege weapons and even weapons of mass destruction should the mage be able to channel more of the titans old self. Lesser mages sometimes try to enlarge the remains of already large skeletons, but they never match up with the real thing.", 
"K’lyfrd the Red – A giant hound, red and large, that wanders the land and befriending folk. Ultimately more of an NPC, as it is not particularly hostile.", 
"Kwoptarr – A massive frog that lives in a swamp in a massive hollow tree who loves to learn. If you befriend him, his spit is a powerful poison that he will bestow upon people who can tell him a riddle he hasn’t heard before.", 
"Charybdis – Charybdis looks like a hideous bladder and twice per day gulps up the water of the sea, creating massive maelstroms that utterly devastate any ships that come too close. According to old sea tales Charybdis is the organ of an ancient God of the Sea that has long since been slain.", 
"The Cadaver Colossus – The Cadaver Colossus is a truly gruesome creation. It is a giant flesh golem created with the bodies of hundreds of corpses. To animate such a massive body of dead flesh, a group of 7 necromancers are needed to conduct the awakening ritual.", 
"Vegoreth – This creature is a massive bison that roams the great planes and prairies. He normally travels with other bison, who look to him for protection. He is often mistaken for a large hill.", 
"The Nameless Tunneler – Drow, Svirfneblin, and Duergar mythologies all reference a creature which their cultures first encountered when exploring the deep parts of the Underdark. Something truly massive lives down there, even below the entrances to the Abyss and other portals. Explorers’ logs discuss gigantic walls of slowly undulating gray-green flesh filling tunnels hundreds of feet across, slowly corroding the tunnels with acidic slime, yet expanding to fill the space as well. No head or tail have ever been found, so it’s not known if it’s one creature or many, but known locations are hundreds of miles apart. Hideous parasites like enormous flat ticks are occassionally found and attack all observers viciously.", 
"The Mithril Defender – A construct created using a ludicrous amount of mithril and multiple uses of the wish spell, the Mithril Defender is possibly the most devastating weapon ever created, save for one flaw. The construct’s two heads are completely independent of one another, leading to it being prone to being easily disoriented.", 
"The Ruinbringer: Legends say it comes from the outer planes, and others say it’s a twisted form of fiend. Whatever it is, one thing is certain: anything that crosses the path of this dragon-like monstrosity is in danger of total annihilation.", 
"Black Cloud of Death – These dreadful creatures are incredibly powerful, sentient monsoon-like beings that survive by acts of death and ruin. They appear as thunderclouds, and can be encountered in any warm desert and can move contrary to the course dictated by the wind if it suits them. Their rolling depths do little to conceal the occasional flares of red lightning; the winds that precede them echo with thunder. Their winds carry particles of soot and ash, darkening the ground and the air as they approach.", 
"Arachnarok – Of the many spiders that infest the world, the gargantuan Arachnarok is the largest of them all. It is a silent predator bigger than a townhouse. In the depths of the forest, the eight-legged monstrosity stalks and entraps entire herds of wildlife, as well as larger prey such as giants. After capturing larger creatures with its rope-like web and flesh-dissolving venom, the spider would begin to drink up the liquefied innards of its paralysed, but still living victim.", 
"Iceberooze – A gargantuan Ooze that is mistaken for huge icebergs detached from the ice continent. Those poor ships that collided with the ice that surrounds it were absorbed without a trace by this creature. Once, a powerful group of adventurers managed to end one of these Ooze, which grow to these dimensions due to the amount of waste and food they find in the sea, but these adventurers suffered many casualties. If they cut it, it would simply divide. The only way they found they could stop it was to hit it with powerful fire magic.", 
"Jörmungandr – Also known as the world serpent. His scales extend to the far reaches of each continent as he slumbers within the ocean. Much of his body is often mistaken for mountain ranges. And when he rustles in his sleep the continent quakes. Try not to wake him up.", 
"Eater of Worlds – A giant, brown worm, with eyes running down its whole body. It splits into smaller worms when cut. Feeds off of sin and Corruption. Always at odds with the Brain of Cthulhu.", 
"The Brain of Cthulhu – A giant, pink brain, with a mass of tentacle attached to it. Reveals a mouth with jagged teeth, with a heart in the center, after taking enough damage. Controls a Crimson infection. Always at odds with the Eater of Worlds.", 
"Kalkurruka, The Scream fron the Stars – Most would describe it as a worm that came from the night sky, roiling about with no obvious sign of how it flies. It is entirely covered in mirror-like bladed scales, from the tip of its tail all the way to it’s circular mouth that lead to endless rows of teeth of the same material. No visible eyes, ears, nose, or any limbs. Its scales vibrate a harsh clanging, chittering sound wherever it goes, like a million screams floating by. It will occasionally descend to the ground to devour any plant or animal life in it’s path, growing larger and shedding scales to regrow new ones. Anyone who find and cuts themselves onto those scales may be inflicted with a curse that leads to a slow transformation into a sort of hybrid with mirror scales and only a circular mouth for a head. Kalkurruka and its hybrids seem to be searching for something on this plane, though no one os certain what.", 
"Black Pudding Lake – This gigantic mass of black ooze slowly creeps along, dissolving and absorbing anything in it’s path. This dark ‘lake’ easily regains any lost material by ‘eating’ everything it dissolves. When it creeps through a city, any buildings in its path are toppled as their foundations are completely eaten away, causing mass destruction.", 
"Animated Temple – Your party enters a temple that seems unguarded. You quickly and quite easily reach the center where a magic artifact awaits. You take it and begin to feel tremors. The entire temple is shaking around you. You’re running to the exit and are violently thrown around the walls and onto the floor as you make your way out. You see the light but you notice the outside world seems to be moving? You exit the temple and turn around and see that the temple itself is alive, and it wants its heart.", 
"The Yawning Chasm – A large canyon that is, in essence, a giant mouth. Its opposite walls meet each other over the course of a hundred years so it can absorb or ‘swallow’ the rocks and dirt that have fallen in and been forgotten, thus preventing the creature from ever eroding away. Digging into the its walls can reveal treasures and trash left to the canyon over millenniums. Though the Yawning Chasm is unlikely to bother most living creatures, 100 years is only a quick bite on a geological timescale and quite dangerous for most non-living things. Once the canyon has been sealed, it stays such a way for a year, leaving only a baron, thin stretch of dirt where its lips once were. When it finally begins to open again, it loudly echoes a day-long, droning sound for which it gets its name, after which it will be another hundred years before it is fully open again.", 
"Reefback Leviathan – Colossal whale like creatures that are often mistaken for moving islands in the oceans they traverse. Their backs are entirely covered with coral reefs and embedded shipwrecks that have collided with it. They are a prey species for a much larger leviathan creature.", 
"Jorrenfilg – A massive cloud of dark fog, miles across. Somewhere in the cloud is Jorrenfilg, once a beloved queen, now a complete terror. She’s about 20 feet tall, her body gaunt and her skin bronze, both in color and material. Along each of her arms are a dozen silver serpents, able to extend and armed with searing fangs, and her hands replaced with unicorn horns which she uses to help support her frail legs. The fog constantly bellowing out from her lower face, though it clears somewhat in a small area around her, her lower jaw is split apart and now more like two tusks, the upper part of her face is unchanged and that of a beautiful woman, with tears streaming from her eyes and becoming deadly bolts of electricity zipping throughout the fog.", 
"The Meta-Inevitable – If the plane of Mechanus somehow were to fall in to disarray by it’s own hand from conflicting imperatives or Inevitables, this towering construct will be called into action. Build from clockwork parts, it’s titanic form shakes the earth as it walks the planes with an unstoppable determination to set its lesser versions straight. Half modron, half titan, the Meta-Inevitable will always override its orders from Primus if they conflict with its prime directive from the Creator.", 
"Ardenvot – Nobody knows what it is, where it came from, or anything else about Ardenvot. Ardenvot wanders the world, usually slowly, killing anything it comes across. It has no destination or objective as far as anyone can tell, but it does often travel in strange patterns, zig-zagging, moving in a circle then spiralling down to the center, going back and forth across random areas, and many more, sonetimes repeating the patterns or ceasing them to start another or travel randomly. The base of its body is a series of hexagonal prisms, 500 feet long, each face 30 feet wide, made of an incredibly tough dull grey metal, forming a larger hexagon. On the inward facing edges of the prisms are white lines, from which spear-like tendrils attack anything in the middle with lightening speed. The prisms are connected to eachother by black spheres with a diameter of 60 feet, from these spheres it can form appendages as it wishes, though fragile and weak they’re able to form legs to hold it up and walk around, and pull or fling whatever life it comes across into the middle.", 
"Kylix, the Cloud Spider – This colossal silver arachnid hangs from a web of altocumulus clouds past the edge of the world, constantly spinning wispy clouds from the water vapor in the air and feeding them to the wind.", 
"Quercus, The Living Ecosystem – This gigantic oak-based treant, whose branches are full of life, rests sleepily in the middle of a dense forest. Birds, squirrels, bugs, and bees all nest on or in him and all will defend him with their lives.",
"Garrus, The Stone Watcher – a giant earth elemental who melded his body into a mountain with only his face showing. He watches over the valley. Most people think his face is merely a rock formation.", 
"Sidderous, the Malevolent Moon – Once a demon lord, Sidderous was tossed into orbit and crushed by space rocks by the Gods, forming a small moon. This moon still contains the demons essence and he can blight the world or cause bad luck on the world below.", 
"Hoydecko – A stoic, wraith like creature that stands unmoving over the great valley. Hoydecko’s masked face is parallel to the mountains on the horizon. It’s body is almost transparent and things pass through it unharmed. You could be forgiven for mistaking Hoydecko for an illusion, but it’s gentle breathing can be heard and felt echoing behind the mask. Hoydecko has stood longer than the oldest tribes in the valley. He is a feature of many myths and prophecies. What is is there for? Is it sleeping? Standing guard?", 
"Queen Oryst – The first dwarf. Over thousands of years, she has grown to immense size. Her beard is like a grey forest and her spear is as tall as a mountain. She is wise and peaceful, but has no time for elves and reacts violently to drow. She might be immensely old and patient but she is still a dwarf, grim and doom-driven.", 
"Teref-zanab, The Many Wormed – A writhing mass of worms that lives below the land, its million appendages gathering information and food for the large, central body that is unknowable under the writhing mass of its body. Those that approach feel themselves draw ever closer to the central mass before they are torn asunder by a million writhing worms.", 
"Kroll, The Many-Scaled One – A giant chimera, with the head of a snake, the body of a lizard, and the tail of a fish. Kroll is the byproduct of some ancient goddess who got frisky with some monsters eons ago. It does not have too much sentience, but does remember the thousands of years it has lived so far. Kroll does not like to be disturbed in its solitary life at the coast, but more than that, Kroll does not like to be hungry. And it is always hungry.", 
"The Wandering Island – Sometimes seen out at sea, appears to be an undiscovered island. However, stories of it’s location are constantly changing. Some people claim to have stepped foot on it only for the island to submerge into the sea, forcing them to swim back to their boat. Others claim to have seen it emerge out of the water. Most people claim that it’s is a reverse mirage, land where there shouldn’t be. Further investigation may reveal that it is a Gigantic Turtle that wanders the ocean.", 
"Kletterhaus – A somewhat sentient wizard’s mansion on six lengthy limbs of living wood that can be used to walk and climb. When its master is away, it feeds by lowering it’s basement chamber onto trees, opening wide its cellar doors, and then biting off their tops. It runs away from fire, but defends itself against persistent pursuers. The legs regrow, albeit slowly.", 
"Unz Bak – The name comes from an old orcish dialect, and rather poetically means ‘large ball’. These coast-dwelling beasts are somewhere between reptile and mammal, covered in thick, flexible plates. They can be found squatting above or in ocean shallows, heads rooting around for any food submerged beneath the sandy floor. When a herd has exhausted a stretch of coast, they move to solid land, bite their tails, and roll towards the next stretch. Unz bak are prized for their armor plates and man-sized eggs, which are often deposited close to shores they intend to revisit, but keeping track of them is also important to coastal fishing towns due to the fish swarms that follow in the wake of an unz bak feeding. Unz bak are fairly docile, but can be rather crudely ‘trained’ for battle, a practice that orc warbands have used before for devastating pillages.", 
"Cloud Drifter – Cloud Drifters are translucent sacks of organs bound inside an oily, bubble-like membrane. Gossamer filaments drift behind them on the winds, catching stray meteoric material and food particles. The one fully opaque part of a cloud drifter is its beak, a metallic, serrated cone between eight to twelve feet long, which can thrust downward to rip the flesh off of any creature that has somehow ascended to the cloud drifter’s altitude, thousands of feet above the clouds. Cloud drifters react poorly to higher air pressure; every bit of their corpses except for the beak tends to disintegrate before reaching the ground, making it hard to prove their existence.", 
"Trappercaps – Trappercaps are chitinous monstrosities, with twelve gnarled legs supporting a fleshy structure not unlike a mushroom cap, thirty feet in diameter. It has no discernible eyes or head, but the top of its cap is studded with mouth-like orifices. Each orifice contains a hook-tipped tentacle, which trappercaps exude when hunting for prey. They appear to sense primarily through smell, touch, and vibration. Trappercaps lie dormant for weeks, legs burrowed into the ground, letting foliage, debris, soil and snow cover their tentacles until something steps on one, at which point the offended tentacle plows upwards, hooks the unfortunate prey, and retreats back into its corresponding mouth. When overwhelmed with multiple prey items, the trappercap bursts from the ground and begins an indiscriminate, frenzied feast, before relocating at high speed.", 
"Daruur Adag – This massive creature, often mistaken for several landmotes, drifts through the sky. In actuality, it is a sky octopus clinging to a collection of landmotes, carcasses of sky whales and the ruins of some lost great civilization. It is normally docile, but occasionally releases a stream of flammable gas to adjust it’s bouancy.", 
"Heke – A massive roc that is three times the size of the average roc. It has been terrorizing the countryside for close to 400 years now. Nothing can seem to match it’s strength and speed. It feeds off large herding animals.", 
"Killith – A giant six legged, two tailed crocodile that stalks the Oka Maobo swamps. Tribes in the area dump a portion of their food into the swamp every night to appease the great Killith.", 
"Galia – The mother of all dryads, Galia is found in a forest in the feywild and is said to be 100-300 feet tall. Galia is responsible for creating seasonal change. If Galia dies she simply is reborn from her old corpse. Galia is lawful in nature and will only appear to those who she wishes to see.", 
"Hemorgolix – An incredibly large sentient clot of blood. The blood flows and beats as if Hemorgolix was a giant heart. No one truly knows where Hemorgolix resides but it’s worshipers one day hope to summon it into the material plane.", 
"Hammerclaw – This vast crustacean will hunt anything from wales to ships. Resembeling a massive crab with two sets of claws, Hammerclaw sometimes attack coastal settlements as well, especially if he is feeling territorial.", 
"Oarthen, The Old – Oarthen is the very first elephant, placed on this planet by the Gods as a protector of humankind. It is his job to watch over the human race, and to destroy anything that would cause harm to it.", 
"Cliffracer – Cliffracer is a bird-like creature that has a wingspan of almost thirty feet and a long verticle sail along it’s spine. Cliffracer lives in large caves along an ocean cliff, and patiently waits for ships to pass by.", 
"Dragondie the Dragonfly – Not much in this world is scarier than a dragonfly big enough to feed on dragons. Earning the name Dragondie by an adventurer who claims he saw it take down a dragon, Dragondie resides in the forest and is thought to be a primordial bug.", 
"Giennu the World Owl – This fey creature often befriends Sylvan creatures, and despising anything else. Giennu sits at 15 feet high and only appears at night. If travelers are walking the roads at night, it is almost certain that Giennu will swoop them up, never to be seen again.",
"Garg-ANT-uan Ants – These massive ants live in cliff formations in the desert. They are the size of horses, and their tunnels are said to reach the center of the earth. Dwarves love them for the tunneling abilities, but fear the sort of things that they might awaken in the earth below.", 
"Hellfang the Rat – This disgusting creature resides in the sewers underneath a major city in your campaign. This massive rat, usually accompanied by hundreds of other regular rats, scours the sewer tunnels looking for fresh meat. People have claimed to see Hellfang reach up and grab people from the sewer drains, in broad daylight, and drag them down into the sewer.", 
"Corpseface – Corpseface is a gargantuan bioluminescent bat that lives in deep caves, coming out only at night to feed. The body of Corpseface glows a bright neon green due to the millions of microorganisms that flow in it’s bloodstream. Corpseface gets its name by the gruesome appearance of it’s face after it feeds.", 
"Kalut, the Devourer – This titanic insect-like fiend is a master of Rot and Decay. Anything organic that this creature touches will soon rot and wither away. It takes the form of a massive locust, but walks around on two feet (when not using it’s wings). It tries to spend it’s time desicrating holy temples and shrines.", 
"Rusted One – While the Rusted One does not have a definitive form, it is a conglomerate of rusted armor that gets left behind in dungeons after their wearer suffers a horrible fate. The creature can smell rust, and immediately drags it’s loud, clanging body through a dungeon to retrieve the fallen armor. After 400 years, the Rusted One has a cult following of dwarves that wish to dig this massive creature out of the mountain, and release it upon the earth.", 
"Colossal Apes – These immense apes are incredibly dangerous and predatorial. Found on large jungle islands, these apes drive away or kill anything that gets bigger than it, in fear that something might be bigger than them. There aren’t many left on the planet, and fewer live to tell the tale of seeing one in person.", 
"Roots, the Shambling Mound – Left to grow for centuries, this Shambling Mound is said to have roots that travel for hundreds of miles. Massive trees have grown into the back of Roots, which is a testament to the amount of time that it has laid dorment. Over the past few nights, people in the local village have felt the ground begin to shake. It is time for Roots to awaken.", 
"Elder Tempest – These creatures are some of the most powerful of Elementals. In this case, the Elder Tempest takes the form of wind. Created by dark clouds, wind, rain, and thunder, the Elder Tempest looks like a massive feathered serpent. The Elder Tempest controls massive storms that have been known to bring cities crumbling down with ease.", 
"Abis, Demon Lord of the Deep – Abis lies dormant in the impossibly deep trenches of the ocean, waiting for his worshippers to bring him the body of a kraken. Only after he finishes feasting on the kraken will his hunger return, and then, the waters of the world will run red with blood. Abis takes the form of a massive nautalus.", 
"Agonath-Ra, the Chained Doom – This creature was an evil wizard who transformed himself into a colossal, tarrasque-like monstrosity, lying waste to whole towns. Now he is almost completely paralyzed, buried under a hill. The denizens of his domain built their city upon this hill, most of them unaware of the beast underneath. Some of them discovered the truth though, and use tunnels to reach Agonath-Ra’s body. They harvest his flesh and blood and use them for magical purposes, becoming more powerful – and monstrous – by the process. Agonath-Ra is helpless to stop this torture (though he regenerates quickly any damage), and the occasional earthquake is the most he can do. But he still dreams the day he will break free of his earthly prison.", 
"Shriek of the Caverns – This obnoxious creature hides in crags and small caves. Its shriek can be heard from miles away, and those who linger too long near it will begin to feel their bones crumble from the pressure created by it. Up close, it resembles an extremely round and fat beetle, however, where its face would be is an impossibly large maw.", 
"Gorefang, the Gargoyle Lord – This creature is the dread lord of a great gothic city full of gargoyles and other statues, all of which come alive at night. Gorefang sits upon a massive cathedral, waiting for travelers to come to his crumbling city so that he may feed again.", 
"Pale Strider – From the foggy mist extends a long, gigantic and lithe limb attached to a large clawed foot. The flesh is human like, but is a sickly white and translucent showing the network of veins below. The creature’s body is obscured by an ever present ethereal fog that is chilling. It moves silently for its size and is rarely hostile unless provoked. It’s fog does necrotic damage and wherever it travels, a plague seems to follow.", 
"Terror of the Sands – This creature resembles a massive scorpion out in the middle of the Taz’ring desert. Brought to life by a sinister cult that could not contain it, this creature wanders the sands looking for it’s next meal. It can run insanely quick for a creature of it’s size.", 
"Kobold Stack – This ‘creature’ is just ten kobolds standing on each other’s shoulders. In the kobold’s mind, bigger is better, so why not be as big as you possibly can? While, yes, it IS startling to come across, they are very easily knocked over.", 
"Gravegrub – A massive grub that constantly feeds on corpses beneath graveyards. Local funeral homes offers special adamantine caskets so your loved one won’t be eaten by Gravegrub.", 
"Smiley’ the Serpent Lord – This creature resembles a massive snake with a human face, stuck in a permenant smile. ‘Smiley’ has been seen wandering closer and closer to a swamp village in the region. Reports have said they they see a massive human head smiling at them from below the murky water, just watching them.", 
"Loo’shin, the Giant Squid – The giant squid is one of the most feared creatures a ship can face on the open sea. Loo’shin is no exception. She loves to collect shipwrecks and bring them back to her lair.", 
"Crystal Colossus – A towering golem-like creature whose main crystal color determines its temperament. If you witness a red Crystal Colossus, run as fast as you can.", 
"Seaweed Giant – These giants lurk in the deeper bays around the shore. Getting up to 30 ft, these large creatures feed on huge clumps of seaweed that form in the bays. They are thought of as protectors of coastal villages, as long as the villagers bring it enough seaweed to eat daily.", 
"Huge Arcane Jellyfish – These jellyfish are crafted from pure magic. A few have even grown to the size of small towns. Because they are made of magic, these creatures float aimlessly in the sky. Their long tentacles sometimes hit the ground, causing a massive explosion of electrical energy.", 
"Pephellius, The Talking Forest – Long ago, a druid awakened a popular tree. That tree spread through its roots sending up new shoots, now the whole forest is sentient.", 
"Adamantine Tortoise – Also known as Adamantine-Shells, these gargantuan turtles are found deep in the Underdark, gorging themselves on minerals and ores. As it eats, the minerals are absorbed into the turtle’s shell, making it even stronger over time. These creatures are very protective of their caves, and will charge at any light source it finds underground.", 
"Rust Dragon – These dragons have an insatiable hunger for weapons and armor, making them a very diificult foe to fight. They are gargantuan creatures, and their rust colored wings block out the sun when they fly. Rust Dragons feed upon small mountains, trying to get to the delicious ore inside.", 
"Sheyeoxks – This extra dimensional being, the size of a solar system, creates wormholes to tunnel through the universe one dimension at a time. Its true form, being of hundreds of dimensions, is impossible to conceive. It’s so big it has its own gravitational pull.", 
"Giant Bees – Originating from deep in the Fey Wild, these bees were created by an ancient order of druids that sought to protect their domain. Unfortunately for the druids, these creatures are bumbling and lazy, just like a normal bee. Every once in a while, a riff in the Fey will open up and one of these bumbling oafs will make it’s way into your realm. While they are funny to look at, if provoked, they can become very dangerous.", 
"Bismark – One of the first complex creatures to evolve on this plane, Bismark started out as a nautilus type creature feeding in primordial seas as an alpha predator. He has fed and grown, fed and grown, using his size to overpower anything he came across. After eons of racing evolutionary branches (some he fathered) and winning, he was discovered by one of the first deities who changed him into their planar battleship, spearheading the invasion of worlds.",
"Volmusian Ember Hair - A breed derived from fire elemental stock, bred by druids as attack animals. Fiery red hair, maned, with a sturdy frame and short snout. 1d3 Fire damage/round if within 5ft and the dog dislikes you.", 
"Mutt of Tindalos - Possessed of the blood of creatures which exist outside of space-time; this canine does not move, it simply stutters & teleports up to 40ft in a round instead. They are off-putting creatures, emaciated and long-limbed with greenish-grey fur.", 
"Hemohound - Descended from the hounds owned by vampires. Sable-furred, with crimson eyes and bodies built for pursuit. Hemohounds feed on blood, and biting living creatures heals them. Each successful bite restores 1 HP to the dog.", 
"Cerberusid - Smuggled out from Hades itself, these stocky, well-muscled and snub nosed dogs have multiple heads for observing the comings and goings of the dead. Advantage on anything to do with multi-tasking or perception. Roll 1d6 - 1-3: 2 heads, 4-6: 3 heads.", 
"Dorician Pale Dog - Developed by fakirs for the purposes of curing diseases, these wane and mangy beasts are capable of taking diseases into themselves by licking the afflicted and transferring them to another through the means of coughing or sneezing fits.", 
"Dolchean Mole-hound - A strange breed of canine developed by dwarves to help them guard their subterranean farms. Mole-hounds have short white fur, huge reflective eyes, and massive paws. These dogs can burrow and dig at half the speed at which they can run.", 
"Sivardian Chaser - These huge, grey-furred, and wolf like dogs were bred by Hobgoblins to keep pace with and flush out their traditional Centaur rivals. Chasers move 20ft faster a round than a typical canine.", 
"Phantom Cur - Cultivated from canines repeatedly revived through necromantic means, these eerie hounds outwardly seem like normal members of their species, but they often go minutes without breathing or days without blinking. Their own proximity to death allows them to sense and affect incorporeal beings.", 
"Spell Terrier - Developed by generations of spell-casters to be the ideal Familiar, spell terriers are small enough to be carried on one's person and are possessed of luxurious hair suitable for petting. Spell Terriers can identify and retrieve spell components and magical items.", 
"Witcher Spaniel - A dog bred by mage-hunters to help them identify their targets. These spaniels are tall and long-bodied, with short dark coats and pointed features. Witchers can sense the presence of magic, and will growl when a spell is used in their presence.", 
"Ceirwannian Hunting Hound - Graceful and sleek of profile, these shaggy-haired hunting dogs are a traditional companion of elvish rangers, and are used to help their owners harry prey. Ceirwannians gain advantage on all rolls relating to stealth or ambush.", 
"Splay-toed Goblin Dog - Long of limb and short-furred with large digit pads, these dogs are used by Goblins as both draft and riding animals. Their feet allow them to easily bound and scurry up the broken terrain and caves in which their masters make their homes. Splay-toes ignore the effects of difficult terrain and climb half as their movement speed.", 
"Chardonian Water Spaniel - Savior of pirates and sailors the world over, Chardonian are mid-sized short-haired dogs which come in a variety of blues. Fiercely loyal, these dogs are trained to retrieve folk thrown overboard during sea voyages. Chardonian have been interbred with water elementals, and they may breathe underwater and swim as quickly as they run.", 
"Drowish Oozehound - Bizarre and terrifying creatures designed by the dark elves as guardians for their slave pens. These beasts tend towards bright and playful personalities, their fur replaced by semi-translucent globules of tar like ichor. A bite (or nuzzle) from an Oozehound necessitates a strength check to escape.", 
"Saoghal Cultivated Dog - A servant dog bred by the nobility to be a gentleman's best friend, these beautiful beasts move with the poise and elegance of an aristocrat. Their long fur is kinked into tight spools which must be brushed daily to keep from knotting. Saoghals are incredibly intelligent, watching those that treat with their owners carefully, barking or growling when they suspect that lies are being told.", 
"Doppeldachshund - Originally the product of a now obscure and likely mad arch-mage, this breed of dog is now chiefly treasured by cheap side shows and thieves. Doppeldachshund are able to briefly alter their form into that of other animals of their own approximate size. They can maintain an alternate form for only ten minutes before shifting back.", 
"Corantinian War Dog - Chosen from the fiercest and largest stock by generations of crusaders to foster a gargantuan canine which rivals a small pony in size. Corantinians have thick coats of white fur which braid themselves into thick protective cords as the dog matures. Corantinians have an extra Hit Die than a typical canine.", 
"Troll-blooded Laika - This particular land race was developed by goblinoid tribes to aid them in their hunts and raids. Interbred with regenerating creatures, these dogs are utterly fearless and unflinchingly loyal. They are a mid-sized breed and of average build, but they are terribly ugly, covered in patches of uneven and wart-ridden fur. Troll-blooded Laika regenerate 1/HP a turn. Laika eat double the amount of a typical dog.", 
"Poison Dart Dog - Inspired by the similarly named amphibian, a group of shaman deep within the jungles of Auyyuah have bred a line of canines capable of producing and expelling poisons. These dogs can at will exude a class 'M' poison. They are hairless and sleek creatures, with slick patches where the poison naturally pools.", 
"Platinum Retreiver - An offshoot of common hunting dogs, these somewhat dopey and friendly beasts can detect the presence of precious metals up to 60' away.",
]
let legends = `You hear someone telling part of the legend of (the) ${searchArray(legendArray)}`;
function omen() {
let completeOmens = [
"A PC makes eye contact with a mysterious beggar, who gasps and runs away. If followed, they disappear.", 
"A raven caws angrily at the party before flying away. More are seen periodically, perching and watching.", 
"A woman in the street drops an urn, which shatters. There's a moment of silence in the street.", 
"A baby won't stop crying in a nearby basket. If the players investigate, there is no child. The crying is gone.", 
"The campfire goes out in the middle of the night. There is no wind. It is difficult to restart as darkness closes in.", 
"The flames of nearby candles flicker out completely, but a moment later they return.", 
"The moon is larger and brighter than usual. It seems to dominate the sky, and cast harsh, pale shadows.", 
"A wooden road sign is snapped in half at a crossroads. It lies broken in the dirt.", 
"The clouds are gray and full of rain. And yet it does not rain. Though thunder rumbles, not a drop lands.", 
"A PC wakes up in the morning with a cut across their palm that wasn't there before.", 
"Animals go wild. Horses buck and have wide, scared eyes. Dogs bark fiercely and pull at their leashes.", 
"There's a large crack in a PC's drinking glass, and yet it doesn't break unless forced.", 
"A bird flies into the wall of a building and drops dead outside the door.", 
"A PC is contacted by the Sending spell, but they only hear heavy breathing and crying.", 
"The players hear distant, sourceless harp music. When pointed out or mentioned, it stops.", 
"An old man has a heart attack in the street. He stares directly at one of the PCs as he dies.", 
"A passed out drunk wakes suddenly and screams, clawing at his eyes. He runs and disappears.", 
"A strong wind that was blowing all day suddenly stops. The world is still for a few moments before life continues.", 
"A child chases an errant ball, only to trip and twist their ankle. The ball is not found.", 
"The temple doors are tossed open by a violent wind until a concerned acolyte rushes to close them.",
];
let setting = [
"You find yourself on a ship at night with rain pelting your face.", 
"You find yourself in a seemingly peaceful grove full of flowers.", 
"You find yourself at the top of a wizard's tower, looking over the ledge.", 
"You find yourself sitting at a the bar of a familiar inn.", 
"You find yourself face down in the sand with no structure in sight.", 
"You find yourself falling from the sky and crashing into a body of water.", 
"You find yourself on a battlefield lined with dead soldiers and common folk alike.", 
"You find yourself in a cemetery covering all sides of a city-sized sphere floating in the darkness.", 
"You find yourself as small as an insect, lost in the grass of a field.", 
"You find yourself looking down upon your own body, laying where you slept this night.", 
"You find yourself feasting with loved ones in a grand mansion.", 
"You find yourself bound to a strangers back as they walk through a swamp.", 
"You find yourself rising from slumber in the same spot you fell asleep, but you see your body still sleeping; you are a spirit.", 
"You find yourself losing an arm wrestling contest to a king, and the court laughs and points.", 
"You find yourself swimming in an endless ocean.", 
"You find yourself telling a joke to a monarch, and nobody laughs.", 
"You find yourself furiously running from something chasing you.", 
"You find yourself aboard a ship far out to sea.", 
"You find yourself at the gates of eternity; a choir of divine beings float around you as far as you can see.", 
"You find yourself in the dilapidated temple of a religion you despise. However, a feeling of failure weighs heavy on your mind.",
];
let being = [
"A three-headed being looks down upon you from the sky, one face scowling, one crying, and one smiling.", 
"Your deity manifests in front of you after crashing down from the heavens; they are worn from battle.", 
"A serpent slithers toward you, it's body growing longer as it moves as to never leaves an area it once occupied.", 
"A sickly frog uses its broken limbs to move toward you.", 
"A figure made solely of familiar faces stares at you.", 
"The person you care for most walks up behind you and places their hands gently around your neck.", 
"Bones rise and form the skeleton of an unrecognizable creature.", 
"Your skin tears from your muscle, forming a swirl of a face in front of you.", 
"A swarm of maggots overtake your surroundings becoming a being standing 20 feet tall.", 
"A mass of red clouds shroud the sky. A tear allows you to see something approaching from far beyond the stars.", 
"Four versions of you appear, each one from an important moment in your life.", 
"An oval eye nearly as tall as you stares at you, following you wherever you go.",
];
let action= [
"The being looks left quickly, and scrambles around before disappearing, but you can faintly make out", 
"It creates a plume of fire; you feel the heat against your face. A vision of what to come:", 
"A pool forms at your feet, swirling with otherworldly power, which glistens with the image of", 
"It calls out your name but its voice fades from existence. Then you see", 
"It tears open, revealing a single word in a language you do not understand along with the image of", 
"You destroy it, but it wails and dies revealing", 
"A wave of teeth and bones wash everything away, and in its wake, you see", 
"It kneels before you, arms stretched out as if waiting to receive something.", 
"Its mouth opens, a haunting chorus of laughter erupting forth; its cackles turn to streams of light which manifest as", 
"It splits the ground open before you, exposing the depths of the world.",
];
let dreamOmen = [
"your hometown, burning, absolutely orange with smoke and flame.", 
"those you love turning the back on you, shame is clear in their eyes.", 
"a devilish form laughing before being consumed in brimstone.", 
"your eyes pull themselves from your body, moving toward a collection of colors you cannot look away from.", 
"all material items you treasure are taken, destroyed, or dissolve.", 
"a foreign vessel with a crew that have no solid form sinking at an incredible rate.", 
"cracks forming along the sea bed, draining the waters, and then a horde of monstrous limbs climbing out.", 
"a terrible screech and then complete and utter silence.",
];
let feeling = [
"You feel a great sense of dread about how real it all felt, but shake it off quickly.", 
"You feel a bit perplexed on why this being came to you of all people.", 
"You feel like this is something you need to tell your party members, but can barely find the words to describe the experience.", 
"You feel like this matter will weigh on you for the days to come.", 
"You feel the matter would be a complete waste of time to investigate.", 
"You feel unsettled at the events that unfolded before you.",
];
let wakeUp = [
"You awaken in a cold sweat.", 
"When you awake, you find yourself sleepwalking about 20 feet from where you fell asleep.", 
"When you awaken, you still see the last image of your dream when you shut your eyes until you flush them with water.", 
"You jump up, screaming for a moment, but you are able to silence yourself before waking your allies.",
];
let generatedOmen = `${searchArray(setting)} ${searchArray(being)} ${searchArray(action)} ${searchArray(dreamOmen)} ${searchArray(feeling)} ${searchArray(wakeUp)}`;
return searchArray([searchArray(completeOmens), generatedOmen]);
};
function nightmare(){
let completeNightmares = [
"You find yourself stranded in a desert, only sand from horizon to horizon. You keep walking but the dunes don't seem to come any closer. You feel extremely thirsty and slowly but steadily, your energy starts to fade. Hours seem to pass and when youre getting desperate, the sand in front of you starts to shift, a giant scorpion emerges and starts chasing you. ", 
"You stand before all those who have been affected by your rampant killings throughout your adventure. A wife who committed suicide after you killed her husband, a bandit. A son, clinging to his mother and asking when his father will be home. A woman, weeping for the loss of her daughter. A man brought to tears by the loss of his husband. They weep and ask why you've brought them such pain. You cannot see yourself and it is unclear whether they are actually referring to you or to the cursed item which is giving the dream. ", 
"You're having a normal dream and everything is 100% fine, then all of a sudden, certain items start to grow, then shrink, then grow, then shrink. You have no control of what it is or if it grows or shrinks and your forced to be 100% concentrated on this object. You're completely aware you're dreaming but can't stop. Whilst this is happening, a loud, deep bass drum is going off every couple seconds, it almost sounds like a war drum. You can hear it but you can't comprehend what is going on or where it's coming from. ", 
"You dream about (the next encounter). ", 
"You are fighting a shadow rival, and the nightmare is different dependent on where you are sleeping: In the mountains, your rival attacks with a sword of ice and rock; In the forest, your rival strikes from shadows and bushes all around; In the desert, your rival attacks with a scorpion's tail; In a town, every passing villager is your rival; By the sea, your rival pins you underwater, gasping for air; Just before you awaken soaked in sweat, your shadow rival's face lightens to reveal your own reflection. ", 
"You're in a dimly lit room, you see a butterfly or moth struggling to fly and flapping against the wall. Walking over to investigate, you reach out to gently touch the grey creature, only for it to fall into dust as soon as you touch it. ", 
"You dream that you are chased by countless slow walking zombies and you can't defend yourself even if you want to. Also the floor is very slippery, like you are on a frozen lake, no matter how hard you try, you can't run properly. ", 
"You dream that the letter you were searching for a long time is in your hands now, but you can't read it, but everybody expects you to read it. You want to take your time but it gets worse and the letter begins to burn in your hands. You have a little time to read this important information, good luck trying. ", 
"You dream that you are a constant state of falling. Everytime you think that you are going to hit the floor, a gigantic monster appears and swallows you to another dimension and you keep falling in there too. ", 
"You find yourself in a battle for whatever cause you champion, whether it be the safety of a loved one or the annihilation of your most despised enemies. The battle is a crucial one, one you’ve prepared for for months; however, every strike you make falls short, your body feels sluggish whenever you move to attack - as if you’re wearing full plate underwater or you’re one of those squishy wizard-folk - all your spells fizzle and drown as you find yourself unable to speak. You watch helplessly as you fail to protect your loved ones from horrible fates, your empire crumbles around you, and your every last pleasant dream lies in shambles at your feet. ", 
"You dream that you've lost all of the skill and experience you've gained over your travels. If you were a melee user, you feel your muscles wither away and your attacks are as weak as a child, a magic user, your spells backfire or are weak and useless, an archer would watch his arrows fly wildly off-target, etc. You can get creative with the description here, if a PC is proud of a certain skill you could describe in brutal detail how awful they've become. ", 
"You dream that your body is overtaken by a malicious presence, and you watch as a helpless captor while it slays your companions using your body ", 
"You dream that you've died, and your companions forget about you completely. Meanwhile, you linger on as a spirit and watch your party go on without you and meet great success, seemingly much better without you dragging them down. ", 
"In your dream you suffer a grave wound, and instead of saving you, your party decides to put you out of your misery, you spring awake just as you feel the cold steel of the blade meet your neck. ", 
"You go out for a night on the town with your friends. All is well and you are having a great time. Eventually the inevitable time comes when you must rest. Finally alone, the faint music and noise of the tavern behind you, you feel relaxed and at ease. Strangely relaxed, even as a hand morphs out of the wall in front of you. It gives a slow wave, so you feel like it is friendly and even wave back. Strange, when did it get a friend? Why do they keep trying to touch you? You decide to leave and try to turn away but there are more hands beside you now and they grab you. No matter how hard you try, you cannot break free, more and more of them grab at you, pulling you towards the wall. You manage to get out loudly as they somehow pull you into it, but you are cut off as a hand covers your mouth and pulls you through the wall. You see your friends rush into the room and bite the hand and try to shout to them, but they cannot hear or see you from this side of the wall. You watch them search for you fruitlessly until you are pulled screaming further into darkness. ", 
"You dream that you wake up normally, however as soon as you speak for the first time, you are interrupted mid sentence by biting your own tongue. You try to curse the pain away only to spit blood and teeth from your mouth. Frantically you scramble to grab them with one hand while trying to stop the flow of blood from your mouth with the other. You can feel more of your teeth falling from your gums into the sea of blood filling your mouth. Strangely, the person you were talking to does not seem shocked by this and continues on normally. You try to shout to them for help, hell, for anything, even a bowl to catch the pieces of you falling off, but only succeed in spraying them with a mouthful of blood and your remaining teeth. They still seem unphased, even as you raise your hands to your mouth in surprise to feel it, only to have your lower jaw slough off. Panicking you reach for them, only to find that your limbs crumple at the joints as you try to move them. Your entire body slowly crumpled as bits break or fall off until you are nothing more than a blob of mangled human parts in disarray, staring up at your friend as breathing becomes harder and harder to do. You wake up just after you black out. ", 
"You are awakened by strange noises outside. Some sort of loud commotion. You decide to get ready and investigate. As you head out, you are stopped by someone close to you. They start trying to tell you something. By the way their hands move, it must be important, but only an inhuman screeching comes out of their mouth when they talk. Their lips don't even move. You try to get them to repeat themselves and they seem to get frustrated and grab a notepad. You feel a slight relief for a moment before they turn the pad to you so you can see what they have wrote and it is just jagged scribbles. Others try to help them explain what's going on to you and progressively everyone gets more and more frustrated but you still can't understand them. You wake up screaming as one of your party members jumps on in a rage after an extended effort trying to get the point across to you. ", 
"You find yourself seemingly restrained, looking down you see your a baby swaddled in a course blanket. An unseen figure picks you up and begins to carry you, walking at a slow hobbled giant. Eventually you are laid down on a forest floor and the unseen figure walks away. A rat scampers over to you and climbs on your chest, you feel yourself smiling at it, soon there are more, 3, 6, a dozen, two dozen! They climb over biting into your flesh until you succumb to death from a 1000 bites. ", 
"You’re racing away from a darkness that threatens to swallow you. Something about this darkness and it’s inky blackness seems to be erasing everything it touches and the daylight begins to dwindle. You claw a slide down the edge of a wet leafy steep and slip into the pond far below. You expect cool water to wash over you but it’s oddly warm. You breech the surface and are horrified to discover you’re swimming in a pool of vomit. It’s in your mouth and nose, choking you as you start to drown, gagging over and over. Finally you realize that you are laying down, and the gagging is real, that you are actually beginning to choke on your own vomit. The character continues gagging afterwards for 15 minutes. ", 
"You're walking along a path when a heavy silence falls, like a great weight is placed on you. You look up to a forest in flames as large monstrous heads on necks higher than trees glare down upon you. ", 
"You slowly wipe the tears from your eyes before opening them. All around you the crowd shouts. 'You are a terrible person.' 'You should never have existed.' 'Scum of the earth.' Wiping more tears from your eyes you slowly turn your head upwards. Before you, silhouetted by the gray cloudy sky, stands a tree with a rope hanging from it. A hooded figure places a platform beneath it. A person is pushed towards it. You wish you could forget them but you can't. It's your partner of over 300 of your most beautiful, wonderful, joyful moons. The crowd's shouting gets louder. 'Murderer.' 'Terrorist.' 'Villain.' You continue to watch, knowing they are innocent with all of your heart, mind, and soul. The shouting gets louder. Your world is consumed, leaving only the shouting, the rope, and the love of your life. The shouting reaches its peak as the rope is tied around their neck. You can't take it any more. Rushing forward towards the tree, crying out in agony all the way. You push aside a guard and feel cold, hard steel piece through your back. A lung ruptures, but before you die you hear one last thing, 'You could have lived. It only had to be me.' Darkness fills your vision as the rope goes taut. ", 
"The weight of a cask of ale presses down upon your back as you return to your home village from the city. Birds sing as they fly through the sky's bright, cloudless blue. You set down the cask for a rest and begin to play a joyful tune on your ukulele. Gray clouds begin rise over the horizon but they don't look quite normal. After some thought you realize that it is smoke coming up from the only place you've ever known. The birds go silent as you leave the cask behind and start running. The cries of your people blend with screams of the invaders before echoing across the landscape. Praying to all of the gods, you continue only to run face to face with a strange person clad in dark armor and wielding a shining sword. Past them you can see your parents on the ground crying over the body of your sibling. Your childhood friend sees you and shouts to run while you can. The attacker grabs you and kicks you to the ground. Another one approaches and begins to mock you. You wish you could do something to stop this. You would willing surrender your life to end the suffering of your people. But that chance never comes, a sword pierces through your heart and you fall to the ground. The last sounds you hear are the cries of your parents and the angry shouts of your friend. Your vision fills with red before fading to black. ", 
"The bustling crowds push past you as you walk to your favorite bar. Once you arrive at your normal seat an unfamiliar dwarf comes up to you and sits down. 'I have an opportunity for you.' Intrigued you start paying very close attention. The dwarf pulls out a rune covered deck of cards, 'How many do you want.' After some questioning they explain that the cards are items of great power. You agree to take third cards and pull out the first one. On the first card a bright, golden, almost glowing orb appears. Years of experience flood through your mind while a belt wraps itself around you causing strength to surge through your body. Extremely satisfied with the outcome you pull out one more. On this card a the image of a golden key glows before a powerful magic (Important Item) appears in your grasp. You can sense the sword or whatever] would strip away the soul of anyone unfortunate enough to get hit by you. The third card has a cloaked figure on it and no apparent effect occurs. You try to thank the dwarf but find they have already left. After celebrating by getting thoroughly drunk you return to your home and pass out almost as soon as you enter. You awake to find your spouse standing over you and bring down your new sword or bring down a sword whilst wearing your new whatever] on your throat. The air escapes your lungs and you hear nothing from them before your vision fades to dark. ", 
"A small sidewalk cafe in the open market. The character is seated and finds the body feels so heavy As to be unable to rise. Waiters and then passersby stop one after the other in front of the player placing plates full of offal in front of them. Disgust colors their faces as they take the plate away empty. The character doesn't remember eating but feels fuller and fuller. The crowds begin cutting of their own body parts to set before the player only to react in fear and loathing as empty plates are taken away. If the player ever tries to actually eat what is front of them they look down and see their own half eaten body and blood on their hands. ", 
"Climbing up the circular interior stairway of a tower castle the sense of something BAD following increases. The faster the character tries to get away the tighter and tighter the hall becomes until the press is suffocating. If the player turns around they find the stairs crumbling behind them into a void where they would fall forever. ", 
"A giant approaches and you reach for you weapon only to find an empty sheath. The creature laugh as it points out you forgot your pants as well. The rest of the party starts to chuckle also until one then the other notices that (whomever of the party the character likes most) has been slain with the lost weapon. ", 
"You are a Shepard, tending to your flock of sheep. You feel relaxed as you count them jumping over a fence, one by one. But pretty soon the sheep coming over the fence becomes a flood as they swarm around you. Soon you are completely surround, tormented by their inhuman moans as they stare at you with their alien eyes. ", 
"you dream that you are drowning in ghostly hands that pull you into the ground while the item floats before you ", 
"you dream a friend gives you a gift in a box and when you open it, the item lies inside and when you look back at your friend they are swiftly withering into a corpse ", 
"you dream of walking through a large empty house at night and tormented voices call to you behind closed doors but never anyone behind them ", 
"you dream you're standing at the banks of an icy lake at night and you can hear the item call your name over and over, knowing it lies at the bottom of the lake while silent figures around from the bank point at you, their eyes milky white ", 
"you dream that you visit a royal figurehead but when you are left alone with them, they begin to choke on blood in their mouth and the guards enter, convinced that you are the murderer ", 
"You're in an outhouse, when something big starts slamming on the door, trying to break it down. The slamming slowly gets louder, and you try to get up to escape, but you find yourself chained to the seat. The banging suddenly stops. The door creaks open and you hear a rasping breath, a cold chill engulfs you. You hear the breath get louder and louder, until it feels like it's almost in your ear. Then suddenly, the thing screams in your ear and you wake up in a cold sweat, screaming. ", 
"A little child stands before you. They reach out a hand towards you as if for help. An ax appears nested in their skull. A spear appears through their heart. They screams as blade after blade impale them; crying out for you to end it; end their misery. A small obsidian glass dagger appears in your hand. But you can’t do it. You wake up with a start, sweating, with the dagger clutched in your fist. ", 
"You are writing a letter or playing an instrument at a feverish pace, but your fingers start to quickly grow weak and you lose sensation in them. The skin and muscles on your fingers slowly starts to rot off the bone, but you cant stop moving them until the bare bone that remains falls off and you are left with only a bleeding stump for a hand. ", 
"You have a ship to catch. It leaves in just a few minutes and it is absolutely imperative you get on it. But for every few steps you take, the road shifts so that it goes at right angles to the path to the ship, and it lengthens. You keep going faster and faster, but cannot catch up. Periodically, you come upon people who ask you questions, and you have to give the right answer to move on, or something terrible will happen. ", 
"Your party is is the entrance to the $BBEG'S_LAIR$. Your comrade says 'On three. 1...2...' You glance down. You are naked, directly under the continual light globe in the ceiling, forgot to prepare any spells this morning and are not proficient in the bizarre exotic weapon in your hand. Your friends look at you expectantly to lead the charge. ... '3!!!!!' ", 
"You go about your day as usual, when you suddenly feel your teeth loosening as you touch them with your tongue. They start to fall out one by one, and you can't do anything against it.", 
"You find yourself sitting at a table in a dark room along with others, trapped in an hypnotic state and mumbling sentences while referring to yourself in third-person. ", 
"The dream is wonderful. All of your friends and family are there. Even the ones who have passed away. You feel elated and joyful. Everyone lives forever in the light. Then, slowly you realise that this can’t be real. People do die. Most of these people are dead. You will die too. ", 
"You are traveling a road by your self. The road begins to wrap around and suddenly you realize you're traveling in a circle you can't escape from. No where to go but forward you encounter someone traveling ahead of you on the same direction . As you catch up to him/her you they began to seem familiar. As you get close enough, you see it is yourself, only horribly disfigured. A gaping wound in your chest. And your face horribly scarred. This future version of you gasping for air says 'don't trust them' and falls over. ", 
"you are fighting with your closest friends against a horrible monster (beholder or something similar) when you are suddenly compelled to turn against those who have saved you countless times and whom you have grown to love and trust. you slowly kill them before killing yourself out of grief. ", 
"You are running from a horrifying monster the likes of which you've never seen before. He moves at a slower pace than you but he never seems to tire while you feel yourself fading quickly. Up ahead you see a house. Safety! Surely, if you get inside and lock the door you can buy time to find a hiding place. Your speed picks up, energy renewed at the thought of safety. Finally making it you slam open the door and dart inside. You survey your surroundings when suddenly you feel a hot breath on your neck. In that instant one terrible thought makes itself horribly clear. 'I forgot to lock the door.' ", 
"You dream you are staring into a mirror, your reflection smiles evilly at you before turning its back to you and walking away. The world surrounding you starts turning to glass and crystal, as your body turns to glass you awake. ", 
"A giant crystallized skull floats in space surrounded by stars, as the skull rotates to face you you catch a glimpse of light shining from inside the skull through one of its eye sockets. ", 
"You are sitting with your friends at a table in a tavern, having a meal when suddenly you find yourself bringing up a secret you hide from them. Then closest or more vulnerable friend]'s head rolls off. The severed head says 'no wonder you hid this, you monster.' You look down, your meal has turned to blood. You look back up. All your friends have lost their heads now, and they lay slumped over the table. ", 
"You are trapped in a giant butler's sink in dirty water and the plug has been removed and the water is beginning to swirl pulling you round and down sweeping you past giant utensils just too distant or too fast to catch. ", 
"You are nothing more than an imaginary puppet dancing to the tune of laughing godlike beings who decide your fate with a casual toss of dice. ", 
"Your party have forgotten you exist, and are trying to kill you or they torture you instead ", 
"You dream of getting stitches from a huge living orange with an artificer's crank-powered sewing machine... ", 
"You start by entering a room. There's a chest. It's a mimic. You run and open a door. It's a mimic. You bring out your sword. It's a mimic. The room is a mimic. Your chestplate is a mimic. Your helmet is a mimic. YOU are a mimic. ", 
"You’re wandering alone in a forest. It’s dark and cold, but there’s no snow, just a bitter frost that clings to everything. You can feel the numbness in your fingertips slowly spread up your hands and arms. You vaguely understand that you won’t last long - that you WILL die if you don’t find shelter from the cold. Up ahead you see a light. Maybe an inn? Just a small cottage? At this point anything will do. You try to walk towards it, but you can’t control your shivering and you collapse on the forest floor. You can’t move your fingers, but you can claw your way forward, inch by inch. Finally, you’re at the edge of the clearing, but you’ve used the last of your strength. The cold binds your screams in your throat, and your body shakes uncontrollably. Eventually even that ceases, and all you can do is watch the people through the windows as the frost covers your eyes. As you struggle to hang on to your last breath, knowing that once you breathe out no more air will enter your lungs, you wake and realize your chest hurts from holding your breath. ", 
"You sit next to a campfire. The party members surround you. You all tell stories, recite poems and jokes, and drink to your hearts content. Eerily, you hear a soft whisper in your ear, and you feel a sharp blade crawl across your neck. You watch in horror as your closest friends observe you bleeding to death and do nothing to help you. ", 
"In a bustling city you watch you party members getting slowly eaten by giant (Terrifying Creature). None of the citizens around you seem to hear you or do anything about it. ", 
"You find yourself laying down in a heap of snow in a frozen forest, barely alive, your friends are around you... (they are either all laying down, all standing, all dead, etc) ", 
"You find yourself at home, in the night outside your house. A terrifying attacker chases you inside, only to find your family/friends who are too busy to even take notice. You fall victim to the attacker as they sit idly by, ignoring your screams. ", 
"You find yourself among a crowded urban area, a market perhaps. However, you quickly realize everything, from folk to beast to nature itself, is running backwards in time. You try to interact with someone, to no avail. Suddenly you notice a hooded figure across the street staring at you. As you try to discern it's shape, you see a humanoid creature with an upside down face, screeching as it points in your direction ", 
"You and your companions are having a meal. Only thing is, there's no food, only charcoal on the plates. You turn it away, but everybody is staring at you seriously. You feel a hit on the back of your skull and dizzily watches without reacting your friends tying you to the chair and force-feeding you. It tastes like ash and you feel your throat bleeding as you swallow. 'You gotta eat, $Name$' 'Gotta keep your fire lit'. ", 
"You stand at the end of a large stone and wood bridge, the land around you dead and barren, the sky dark aglow with an eerie orange light. The wind howling as you scan around, you notice the bridge and the surrounding area as place from your childhood. Though then it was vibrant and lush with life thriving all around. As sadness and despair begin to settle into your gut you hear a ferocious wicked growl. From the shadows a large beast with razor sharp teeth, gnarled spines growing out of it's back, and blood thirty eyes starts moving towards. You try and runaway but move slowly as the horror approaches, half way across the bridge you stand consumed in shadow. The beast is upon you and ready to... ", 
"You are walking on the docks at night with your? child, you look to your left and a massive serpent made of black bones slowly rises from the dark water. You freeze but your? child keeps moving, playfully running forward. You wake up as the serpent lunges at your child?. ", 
"It's winter, you're a wolf running with your pack. They find something to eat in the snow and you join them. After a few bites you look down, you've been eating the half frozen remains of your loved one. ", 
"A charming friendly creature offers you blueberry cake. You eat the cake, and begin to expand and turn blue. Then your adventuring comrade yells 'Gonna Pop!' and everyone ducks for cover! ", 
"You wake up in your camp and hear the soft crunching of branches. As you look, you hear a growl behind you. As you turn to face it, a (Terrifying Creature) leaps at you. You feel warm breath on your face as it begins to take a bite! ", 
"You're hunting for an offender, and as you are about to shoot, they hide behind the last tavernkeep you saw. You shot them instead and the offender's shadow looms over you. Smothering you! ", 
"You're on a sandy beach and realize $Skittering_Creatures$ are crawling all over you. They engulf you completely. ", 
"You find yourself at a gathering of those you admire. Great heroes, beautiful lovers, and influential figures. They're all looking at you with admiration. You open your mouth to speak, but you feel your teeth begin to fall out. As each one clinks to the stone floor, you can feel the disgust roll over you, the taste of blood in your mouth making you sick as you wake up gagging. ", 
"You see (npc or character they're most attached to) approaching, as you go to embrace them you notice a look of surprise then pain cross their face, as you look down you see your hand, scarlet, as the blood drips down your elbow the drops in the pool of blood bring you back to awareness, they whisper one word 'Why?' as the tears run down their face mixing with the blood the last thing you hear is the dripping of the blood flowing down your arm. You awaken to the sound of the rains last drops collecting in a pool nearby. ", 
"You move to awaken $party_member$ for their turn on watch, but as you move you notice an odd weakness in your legs, as you look down you notice for the first time the flesh on your hands slowly melting and sloughing off revealing the pitted/ rotted bone beneath, as you go to scream out in horror/pain,your legs give out from beneath you, the impact knocking the breath from your lungs. As you lay there feeling your body slowly dissolve, unable to draw breath you see a pair of malevolent feline eyes staring at you from the lowest branch in the tree you were resting against, the cat begins to take shape and as it leaps at you it bursts apart as a swarm of spiders engulfing you, you awaken to your own screams, realizing it was just a dream, but a prickling along your spine and the echoes of a malicious laugh leave you wondering, was it really only a dream? ", 
"It's hot. Humid. You're holding an unfamiliar crossbow-like weapon. You lie motionless in a row of bushes along the edge of a flooded grain field. Dragonfly-shaped airships circle overhead with a powerful thumping sound, and begin to debark men clad in green. With a stuttering roar, some kind of automated wand sprays red magic missiles into the green-clad men from somewhere on your left. Their crossbow-like weapons glow with flickering star-shaped flame as they respond. You wake with a start, wondering what that even was. ", 
"You are being pursued by an immense fat demon made of glass. You can only run, because if you try to hide, it bursts through even the stoutest stone wall with a cry of 'OH YEAH!' Brilliant red ichor sloshes visibly within its skin at every step. ", 
"The party is ambushed by goblins. Just as you are about to enter the fray, you feel a breeze. One of your party members asks if you're forgetting something. You look down and see that you are nude. The party laughs. The goblins laugh. You wake up cold, the blanket having slid off the bed. ", 
"An airship envelops you in golden light and you float up from the ground. A group of hairless gray Deep Gnomes straps you to a table and performs a thorough examination. Uncomfortably thorough. They shine a glittering light in your eyes and you jerk awake. It's an hour before dawn and you can't recall making camp last night, even though the tents are set up. ", 
"You are standing above the sky, leaning against a wall of glass, looking down on the familiar coastline of your homeland, made strange by this new perspective. A menacing shape, clearly made of metal, slides soundlessly into view and begins to project beams of light at the points you know hold towns. ", 
"You're in complete agony. You move the hand away from your mouth to see it is covered in blood. The blood continues to drip on the sides of your mouth. You run to the nearby commoners walking among the streets begging for help except nothing you say makes sense. The words appear to be gurgled by the amount of blood. They look at you strangely and push you away as you bleed on their clothing. Looking into a mirror placed in front of a store, you use your hands to spread your mouth open and realize that your tongue has been extracted. The amount of blood begins to overtake you and you begin to choke. It is at that moment you wake up with a burning sensation in the back of your throat. You were choking on saliva in your sleep. ", 
"The bed you are sleeping in is really a mimic and is trying to eat you! ", 
"Your loved one is secretly a doppelganger and your real loved one is held captive far away. ", 
"Your favorite possession has been stolen and been replaced by a fake replica. ", 
"You're stuck in a white room with an eerie-looking statue. You don't know why, but something's telling you that you really need to leave or something horrible will happen. ", 
"You're stuck in some kind of time-loop, reliving the same day over and over again. Nobody will believe you, even as you predict every detail you've spent the last month or so seeing over and over. ", 
"A surreal rendition of the next planned encounter. It takes a sharp deviation from the original when a shadowy creature picks the party off one by one and the dreamer is helpless to stop it. ", 
"You are stranded in a painted desert, and the sun is perpetually setting. The dry, dusty ground becomes a riverbed which flash floods and drags you under. ", 
"You are a bird, flying over someone dying. You alight next to them and they reach for you. ", 
"You are dying. A bird alights next to you. Then more. You are whisked up in a flock of small birds who peck and scratch. You know there will soon be no trace of you left, but you cannot.. or must not move. ", 
"A collection of live butterflies and winged insects sits in front of you, glittering like jewels. Your (Stern_Parental_Figure) stands over your left shoulder instructing you in the method of euthanizing, and then mounting the insects for display and study. They tell you that you are not done despite all the bugs having been mounted. You realize they mean to have you mounted last, and expects you to do everything but the final pin. ", 
"Your teeth are loose. You pull one out by accident, but a second grows into it's place. You pull a second, and a third... ", 
"You see yourself in the mirror. You smile, and have too many teeth, and then your reflection drags you into the mirror and begins devouring you. ", 
"You go to show your friends some cool thing you can suddenly do, and find they are dead.. rotting hunks of flesh, but still moving. They bite and scratch, clawing at you, trying to drag you down. ", 
"You are lost and naked. Something is pursuing you, and the further you run the larger and more frightening it becomes, eventually looming on the horizon. ", 
"Wandering the labynthian corridors of a place you once knew well, seeking a murderer hiding amongst your friends. It starts to snow and inside the building there are snowdrifts everywhere. It is quite cold, and you are nearly naked. Your friends don't beleive you that there is a murderer and that it is snowing. You are also late, the murderer has killed one of your friends, and know that if you do not find the killer soon, then more of your friends will die. ", 
"A dream where you wandering through a cave populated with mannequins. All of whom are wearing the faces of your friends and family. At the back is a mannequin whose back is turned to you. You find yourself terrified at looking upon its face. But you don't know why... ", 
"You dream of your family members that are still alive are brutally murdered by someone or something. ", 
"Your beloved family pet turns on you, and you are forced in defense to choke it. It does not relent its attack as you do, and you're forced to continue choking until it dies. Its head swells and throbs with its heartbeat as you continue the hold, and it dies as the animal's scalp and face explode from the pressure of the blood you choked it with. Your pet falls dead from your hands, a brutal mess, and all the good memories you had with it flash before you and seem to crumble. ", 
"Your dream that you have severed ties with (best_friend); yet contact continues, and they seem to be nearly everywhere in your life. They betrayed you, yet everywhere you go and everything you involve with they seems to be there. Frustrated, you approach them near a stream and berate them that it was they who wronged you and still goes where they know you will be. You begin to argue in earnest, screaming and furious, and as your vision blurs and tunnels, you find you have wrestled them to the bank of the stream, and to try to silence his screams, push his head in the water. Before you know it they are dead in your hands! ", 
"You are in a noble's salon, moving among salaciously dressed courtesans. Every drink you sip tastes like sand, and every caress fills you with horror. When you sit at the table they all set to, devouring the meat, but the sickly sweet smell of it makes you think of corrupted flesh, and the thought of eating it turns your guts. ", 
"You dream that you're in a dark room, and random body parts of all different races are appearing and disappearing sporadically. They begin striking you, chasing you, or assaulting you. Some have claws, others warts or a contagious disease...  ", 
"You dream you're watching the stars when you feel a sense of losing your footing like you're going to fall into the night sky, nearly falling upward. As your feet leave the ground, the stars dim as a winged form stares at you, then you plummet into the cold ocean. ", 
"You dream that you're home reading by candlelight when you look up to see your (PET) contorting; it's head and limbs sprouting second and third heads and limbs. Lightning flashes by the window and a dark monstrous shadow looms across the horizon line. ", 
"You dream you wake in your bed at home to the sound of the sound water flowing just out of ear shot. As you follow the sound you feel the wriggling of tentacles in your left hand and look down to see a writhing mess of small squid. ",
"You dream that you are buried alive in the ground and waken to the cramped darkness, screaming & yelling as you scratch your nails bloody against the coffin lid. The ground outside is filled with burrowing and holes begin to smash open as black tentacles begin to writhe through slowly filling the coffin with their cold, slimy touches as they begin to suffocate you. ", 
"You dream of floating in a strange, airless void, with a scintillating blue field of stars on one side and a great black void on the other. As you look around, the void begins to grow, enveloping the rest of the sky, and as the last lights wink out you feel your body start to be ripped apart.", 
"You dream of floating in a deep, dark ocean, with the only thing in sight a thin tapeworm like creature seemingly floating just below you. It's only as it rises up to devour you that you realize the worm is as wide as a world.", 
"You dream of awakening in a small cottage. You begin to fall upwards, suffering terrifying vertigo, as everything above you darkens and fades out of existence.", 
"You're sitting outdoors, with your loved ones around you. The sun is shining and you're having a picnic. Your favorite person says something that makes you laugh. Your laugh is interrupted when you cough. You look down at your hand, and one of your teeth has fallen out. You feel your other teeth grow and wiggle their way out of your gums and fall in your hand. You begin coughing uncontrollably, spraying the ground with teeth. The coughing turns to retching, and you start vomiting teeth. Not just human teeth, but dog teeth, shark teeth, teeth that fit in no sane mouth. They cut your mouth as they come up, and soon you are covered in blood and alien teeth... You continue vomiting teeth until you wake up.", 
"As the player sits in a semi lit up room, oddly shaped shadow appear from the completely dark corners and slowly creep towards them. When the shadows reach the player, they become physical entities. The shadow from the front-left becomes a two headed cyclops with two sets of insect-like arms with clawed appendages at the end. The one from the front right becomes slime-covered fat creature with a scaly tail lining down its back from the back of it neck and 4 eye stalks on its chubby head. It’s mouth is like that of a goblin shark. The one from the back left becomes a giant fly with two large horns on the sides of its head instead of eyes and a scorpion tail on its back. The one on the back right is a gibbering mouther with hundreds of legs on its underside. These four entities tear the player apart until they wake up.", 
"You put on your coat and get ready to leave your house. The hat stand is strangely empty. You feel empty; utterly empty. You walk to the $Place_Of_Employment$. Everyone you pass has a hat and is silently screaming.; You pass the silently screaming secretary in their neat fascinator. You reach your desk.There's your hat. A standard homburg. The desk where it sits is cracked and etched as if acid had been oozing from the hat. Your emptiness is being replaced by fear. Dread. Horror. You reach for the hat anyway...", 
"You awaken on a wooden slab when some cool, heavy liquid cascades onto you. It's hard to move or see, burning your eyes when you open them, but you can vaguely make out a gargantuan humanoid looming above you and skewers your chest and chops of your arm.", 
"Liquid begins to drown you. You attempt to scream, the salty sweet liquid fills your mouth and drowns out your calls. Strange creatures remove your limbs and then pick up your severed arm and toss it in their mouth, full feeling remaining as it masticates and swallows. As it drops in its stomach you are fully aware of the sensation of your arm's broken bones now being dissolved by the hot acid.", 
"You're running through a rain forest chasing some brightly colored bird. It's ducking and weaving through the lower canopy, just able to stay 20 feet ahead of you until suddenly it stops. As it turns its head the bird smiles a toothy, orcish grin that wraps around its entire head, motions at you with its beak and laughs like a hyena. Uncountably more sources of laughter flutter in behind and around you as the sky darkens with more and larger wings.", 
"Your $Parents$ are tucking you into your cradle, speaking in tongues with their eyes closed. When they lean in to kiss you their eyes open, and you see that under the lids are black holes, ringed with teeth.", 
"You wake up standing on a white pebbly beach before a great black ocean. As you stand with your feet in the surf you feel the tugging of the obsidian water at your legs, far higher than the surf should reach...Looking down, you see barnacles and suckers grabbing up to your knees, dragging you into the briny depths. Fighting kicking and screaming, you see an old man sitting on a big rock on the shore staring at you with gaping empty holes where his eyes once were. As your mouth fills with the inky black water and your vision starts to blur, the old man grins and begins singing an ancient sea shanty that, despite being pulled under the water, you can hear as if you were standing next to him.", 
"Everyone you ever knew or loved stands in a circle before you and behind you, and stabs you with a weapon, painfully.", 
"You and a band of soldiers face an army at a bank, trying to cross the lake. You pelt them with arrows, and they fire back. Suddenly it goes silent, and arrow flies out striking the man next to you. Attempting to bring him to your commander, soldiers stream from the bushes behind you, clubbing and slashing everything. You do not know whose who, desperately trying to protect anyone you recognize. One falls upon you, clubbing you with a rock as your arms go weak, unable to fight back.",
]
//You find yourself in    
let place = [
"in a graveyard, a blood-red moon hangs above", 
"in the bedroom from your childhood. There is no door to exit the room", 
"in the room you fell asleep in", 
"in absolute darkness. In the silence you can hear your own heart beat", 
"in an open field. Next to you is a dead oak tree with an empty noose swinging in the breeze", 
"in a dark forest. In the corner of your eye you can see something is following you", 
"in a dark cave. A low, rhythmic chanting echoes around you", 
"in a prison cell. The walls are scratched and your fingernails are bloodied", 
"in a long hallway with a door at the end. The door doesn't get closer as you approach", 
"knee deep swamp water. You can feel something touching your leg under the surface",
]
//In the [Place] you see
let figure = [
`a ${searchArray(['boy','girl'])}`, `a young ${searchArray(['man','woman'])}`, `an elderly ${searchArray(['man','woman'])}`, "yourself", 
"a large dog", 
"your parents", 
"a shadowy figure", 
"a small toy doll, standing upright", 
"a large wolf, standing on it's hind legs", 
"a large cat",    
]
let savedFigure = searchArray(figure)
//The [Figure]
let descriptor = [
"has it's eyes and mouth sewn shut", 
"is decaying. It's flesh and hair are falling to the ground", 
"is wheezing loudly. You can feel your throat drying and it gets harder to breath", 
"blood slowly trickles from the corners of it's mouth, then eyes, and finally it appears to be sweating blood", 
"its chest bursts open and maggots and worms tumble out, writhing on the floor", 
"has it's throat slit. You see the wound open and close slightly with it's breathing", 
"has mismatching limbs. It looks to be sewn together using mismatching pieces", 
"has the lower body of an arachnid", 
"has fingernails that continue to grow. They look sharp", 
"is starting to crumble away as if it were made of ash",    
]
//The [Figure]
let action = [
"sprints at you", 
"begins walking slowly toward you", 
"throws it's head back and starts cackling wildly", 
"tries to speak, but spiders begin pouring out it's mouth", 
"catches fire at it's feet and it quickly spreads up it's body", 
"vanishes and reappears inches from your face", 
"grows double it's size and begins chasing you", 
"grows horrible, black, leathery wings and begins flying towards you", 
"begins systematically breaking its fingers while staring you in the eye", 
"starts ripping the flesh from it's face",    
]
//You wake up in a cold sweat
let falseWake = [
`inches from your face is the ${savedFigure}`, "in the darkness you can see the outline of the same entity as before", 
"the same entity as before is sprinting towards you, roll initiative. [Player wakes as soon as the figure reaches them. All spells fail and attacks miss against it", 
"the door to the room opens slowly and the same entity as before walks in", 
"the party member closest to them is replaced with the same entity as before", 
"standing over you is the same entity as before", 
"as you are about to go to sleep you blink and the same entity as before is in front of you", 
"the same entity as before is walking toward you slowly. You cannot move", 
"the same entity as before is dragging away a party member. It looks up and makes eye contact with you", 
"inside of a new nightmare. Take it from the top", 
"Have the false wake resolve and the player wakes up. Or do they?",    
]
let generatedNightmare = `You find yourself ${searchArray(place)}. You see ${savedFigure}, and you notice ${searchArray(descriptor)}. All of a sudden it ${searchArray(action)}. You jolt awake... ${searchArray(falseWake)}`
return searchArray([generatedNightmare, searchArray(completeNightmares)])
}
let output = searchArray([`You hear someone spreading a rumor: ${searchArray([rumorMill(),searchArray(completeRumors)])}`, `You hear someone recounting a legend: ${legends}`, `You hear someone explaining an omen: ${omen()}`, `You hear someone sharing their nightmare: ${nightmare()}`])
return output
}
function overHear() {
let chance = rollDice(100)
let tavernOverHear = [
"And then the wolves came...", 
"And that’s why it’s hard for me to buy pants.", 
"What do you mean it’s infected ?", 
"How far do you think I can throw this hammer?", 
"I swear to gods it was just two goblins in a trench coat", 
"...and that's the second time I got crabs.", 
"And I said to him, that's no displacer beast, that's my wife!", 
"That's not beer they're drinking.", 
"...so I told myself, Mario, take it easy!", 
"No Jane I'm not going to your stupid baby's baptism to Tiamat", 
"I mean, legally, it’s a religion but they are just worshipping a lump of green stone! Got more followers than the Temple of Bahamut now and the priest is mighty unhappy to be losing devotees to a damn rock...", 
"There's good money to be made in barley smuggling and that's the truth.", 
"So I says to her, that's BARLEY legal!", 
"So there I was, I had 1 foot on the latrine, I had 2 pieces of pie left, the dog was having a seizure.", 
"So I’m sitting there, covered in grog and the tentacles can’t even touch me...", 
"...it was THIS big! And that was just between the eyes!", 
"You really think she’s into it...?", 
"...so my fist got the sucker in his liver and that little weasel went scurryin'! But enough about your husband, how are you doing?", 
"No, no, no, the pigeon is the least of your problems..", 
"Oh god, its the goose. run.", 
"Hey, who moved my cheese?", 
"Just hire some band of adventurers to do it, they will accept anything as long as you tell them it’s a quest.", 
"How awful... did he at least die painlessly?... to shreds you say...", 
"Jones's dog went missing, you wouldn't happen to know anything about that, would you, Elkard?", 
"You still got that book on how to get demons out of pigeon?", 
"These owl tassels cost HOW much?", 
"You know, it's about time they put a Tavern in that Orphanage.", 
"Some holy woman - she’s slept with half the nuns!!!", 
"I'm going to the bear pits tomorrow. Wanna come with?", 
"And they were roommates...", 
"...and that's how I got trampled over by a herd of owlbears", 
"THAT'S the reason you keep honey on you?! For that!?", 
"...that's how they convinced me that I needed a pet crow.", 
"So I was on my third pint at that point...", 
"I don't know Marv, I work my butt off to provide for her and what do I get? My own boot leather fried in a skillet and served with a side of spit.", 
"Now why the hell wouldja do that?!", 
"...thinks 4 swords are too many? That's ridiculous...", 
"I'd ask for medium-rare but everyone knows what they make this steak out of is better burnt.", 
"But I DID see it! He ate the whole bag of nails!", 
"The cleric said it should clear up if I keep putting the poultice on it. Smells like piss, it does", 
"I know they say beauty's in the eye of the beholder but I don't know if I can stay with a woman with that many eyestalks", 
"...and by this point, I still hadn't found my pants!", 
"Dude, I don't care if she's an elf. She's still way too young for you.", 
"…Dropped that ax on his foot. Took off three toes but he stood there screeching about his new boot…", 
"...so I push this oddly thin orc and... I shit you not... he fell apart into three goblins and ran in different directions..", 
"What do you mean I remind you of MY mother!?!?", 
"I'm told it's the latest fashion but honestly does that make them worth the stench?", 
"Three steak and kidney pies was not a good idea...", 
"...so two casks of ale, a buttered piece of bread, and a wet sock are all you need.", 
"She ate how many breadsticks?", 
"No Dad I'm not a crazed marauder, I'm an adventurer. Well, the difference being, one's a job and the other's mental sickness.", 
"...and I said unicorns don't even wear pants.", 
"Where did you find a blue antler at 3 in the morning?", 
"Had a dog once.Turns out it was just a creepy old Druid.", 
"And that's how I learned that flammable and inflammable mean the same thing... and it's also why I can't grow eyebrows.", 
"Who is she, anyway!? Some... tart from the village!? Humph! 'Younger than me' is she!?", 
"No, no! It's true! At least that's what I was told... Drink a troll's blood at midnight and you'll get younger right on the spot!", 
"I swear to the gods that boy's got some ogre in him. I saw him eat fifty eggs in an hour.", 
"...and get this. He says he can't see me again because he's actually a polymorphed dragon and he had to go back to his lair.", 
"...and for a small fee of 10 gold you can start your own potion selling business and be rich just like me!", 
"I just don't trust those magic-using types. I heard they can stick their magic into your head and make you do whatever they want!", 
"If he comes back this way I'll stick a spear right in his gut. I ain't got no qualms about it neither.", 
"If it weren't for my horse I never would've gotten into college.", 
".....those aren't children.",
"Let me guess... someone stole your sweet roll.", 
"What do you call a group of owlbears, a sleuth or a parliament?", 
"So help me Pelor, if Max makes one more 'I barely know her' joke, I'm gonna shove him face-first into the dirtiest latrine in the Hag and Hog!", 
"The ale at the pub is too foamy because they don't pour it right! My mam always said,'Don't be a jerk, tilt the glass!','...was a good friend of mine.Never understood a word he said but I helped him drink his wine..", 
"... and they didn't know what to feed the damn thing, so they figured to just feed it nails and call it a day. By the way, you wouldn't happen to know someone in need of a dead ostrich, would you?", 
"....and that is why you don’t eat the blue ones.", 
"...and I haven’ t swum since.", 
"...he’s in my face yelling about flamingos...", 
"...weeks to get the smell of corpse out.", 
"So, imagine a 50 ft tall mushroom...", 
"...the guy was holding it upside down!", 
"And that's how I learned that flammable and inflammable mean the same thing... and it's also why I can't grow eyebrows.", 
"You know, there are eyes on the moon", 
"...and he used the strawberries as a distraction and jumped through the window. And the mayor didn't even see him!", 
"Lucky for us, the wizard lit the pinecones on fire, and we hurled them at the dire wolves that had chased us up the trees!", 
"Can we not talk about that incident in the graveyard?", 
"You did what with a fire elemental?", 
"Nobody talk about those damn chickens okay?", 
"... and, of course, the invisibility spell had to pick that specific moment to wear off, and me without even a towel to cover myself with. And that's the story of how I ended up getting my head kicked in by the women's rugby team.", 
"You really thought it would be a good idea to hire a bard for your daughter's 18th birthday? Especially one with his reputation?", 
"...why do so many of your spells involve tentacles?!", 
"Hey, you. Wanna buy a sundial?",
"... and then I said 'Wrecked'em? Damn near killed'em!' Get it? ... ah, you guys wouldn't know a joke if it bit ya.", 
"... I guess, in a way, kobolds are kinda like Dragonborn halflings. Not that I'd ever say that within earshot of a Dragonborn, however.", 
"Seeing as they have to run after criminals, is it really wise to hire someone with a knee injury as a guard?", 
"And I'm-a telling you, the world, she is not-a flat-a. She's a round, she's a firm-a, she's a fully-packed-a! She's-a round, LIKE-A MY HEAD!!!", 
"...we’ re halfway through when I open a door and: frogs. Everywhere.", 
"...’oh no, Mr. Bigshot Wizard is gonna curse me! Ha! ’ZAP! And that’s why I’m married to a cow.", 
"Wait, they regenerate ?", 
"...it was so cute too, he even had a bucket on his head for a helmet. I still walloped him after I fished him out of the well though.", 
"...Curr, I am ['PCs name' the 'PCs Class'] of great renown. Surely you have heard of me! You simply must give me, ['PCs name' the 'PCs Class'] of great renown, free drinks!", 
"Say you put it atop your house, would you become a god?", 
"...but I had to put that life behind me. Too much glamour and fame in candlemaking, and I just wanted to settle down. The ladies it brought, though...my goodness, the ladies.",
`... so I says to the guy—I says “that’s not your nephew! That’s a flail snail with a mace infection!” `, `and that’s when I said “beholder? I hardly know her!” `, `so then I told her “madam it couldn’t have been my dog, he was eaten by an aboleth yesterday! `, `“So then I looked this beholder right in the eye, and I —“ “which one?” Piped the old codger in the corner of the room `, `...and there it was. The most magnificent mermaid I’ve ever seen. And as I move in for a passionate kiss, I wake up. It was only a wet dream. `, `"And that's the second time I got giant crabs" `, `"So I says 'that's no displacer beast, that's my wife!" `, `And after all that, the goblin says to the lady “Wow, you sure you don’t want me to eat him?” `, `Then, just as the sun was beginning to rise, the mage looked over and saw it wasn’t his spell book he’d been protecting, it was a cookbook!” `, `So the ogre just took one look at him and says “I don’t think that part should have spots...” so he let him go! `, `But then, right as the kobold was going to leave the bar, the bartender says “wow, I guess that’s what tipped...the scale!” (Followed by laughter) `, `"...and so she told me she wanted me to make a pact with her in exchange for eldritch power. I had to tell her I wasn't ready for that kind of commitment." `, `Woman with a hook for a hand: "And that's why I'll never have tea with the baker's wife ever again!" `, `"Next thing I know, the bard has a broken lute string, the monk is ten feet in the air and the druid is stuck as a frog" (use this one when the party gets caught sneaking so they don't hear the end of the story). `, `"So if you just invest 50 copper and I invest 100 of my own, I know a guy who can turn that into 5 gold in two months." `, `"What would you know about pulling teeth? You're not a barber!" `, `And so I tells her “look, lady, the difference between your half-orc baby and a goblin teenager is pretty low, just be glad it was a flesh wound!” `, `"So I says 'that's no displacer beast, that's my wife!'" `, `And at the end of the night, she realizes he had been using Mage Hand to seem bigger, he wasn’t actually that big at all! `, `So the adventurers ask the creed wizard “why?” And the wizard simply responded “I wanted to make egg salad...” `, `then I said, "If you didn't want to turn to stone, you shouldn't have married Medusa! (Bonus: and that was the second time I got crabs) `,
`Then I said back to her "are you Medusa? Cuz I'm hard as a rock! `, `“... so I sold him the bag of holding, but switched it at the last moment for the one filled with flumph farts!!” `, `“....and that’s how I got me hook leg and peg arm.” as told by a pirate.  `, `“No, really!! He was just two halfling wrestlers in a trench coat! Honest!” `, `“...and then she screamed "Wait, that’s not ale - that’s camel piss!!!!” `, `“...and that’s how I found out that dwarf lasses have TWO beards!!!” `, `And so the Eunuch said, "That's not my sister.. that's my wife!" `, `"...so the xorn says... wait, no, let me start again, it wasn't a xorn it was a half-orc. So this half-orc decides to join the army, wait what are you doing with that axe -" `, `"...and then Asmodeus says 'With fiends like these, who needs enemas?'" `, `"...no, you see it's funny because the bard was sleeping with a mimic." "That's how all your jokes end." "Because it's always funny!" `, `"...polishing her orbs with a cloaker!" `, `After I finished cleaning off the blood from the steps I was banned from entering any of her temples again. I still donate and spread the good word though- a cleric banned from entering their own gods temples `, `And that’s how I found out how to properly cook aboleth. It’s quite nutritious.- the strange three eyed cook `, `"And I tossed that dwarf good, if you know what I mean!" `, 
`"That bard was here last night and I can't stop itching..." `, `"...and that was the last time I ever hooked up with a beholder" `, `“But then the rich dude takes one look at the dog, goes ‘mine isn’t THAT shaggy’, and shuts the door.” `, `“... and then I said, ‘That’s no hag, that’s my mother-in-law!’ “ `, `“... that’s when I walked into the gelatinous cube.” `, `“... I don’t care about the barmaid, is the cheese alright?!” A fat halfling chuckles. `, `“... What can I say, I was a horny bard. Now, I’m just a bard...” A tiefling with two broken horns `, `..and then she screamed "they weren't Kobolds, they were children" and I says to her "it's all the same in here" pats stomach `, `...and then he asked me, "Can you do anything other than eldritch blast?" and nobody's heard from him since... `, `Then I said back to her "are you Medusa? Cuz I'm hard as a rock! `, `"So the merrow says 'those aren't oars, they're my sisters!" `, `“...so the interrogator says, ‘What’s with all the fish?’ and I say, ‘I thought you said fillet!” `, `"...Good thing gnolls can't get rabies, right?" `, `"...There was zero reason for you to joke about kidnapping the princess in front of the bard, you know." `, `"...For the last time, nobody wants to hear about how you escaped the shapeshifter who was stalking you." `, `"...Really? You can do THAT to an orc?" `, `"...Only a rookie adventurer would mistake a kobold for a lizardfolk. For one thing, they smell completely different!" `, `"...Moreover, imagine what would have happened if I HADN'T clocked the daylights out of that horse" "But wait.. didn't you say it was already dead?" "Yes!!" `, `"...You know (guard / NPC name), I know you're all over this whole 'natural' thing since you went spelunking with that druid girl, but as your pal? TAKE A BATH!" `, `"...And that's why I can never go back to (Location)."..."Why..?"..."Huh?"..."You didn't say why, you just said 'and that's why I can never go back to (location)."..."Why don't you ever let me be dramatic for 5 seconds, (NPC name) ?!" `, `"...In short, NEVER do that while on top of a Minotaur."`, `"...And right before I put him on bread and water, he says: "Please, I have a family!"..."Yeah?" "Nah, that was it, that's all he said really." "....." `,
]
let drunkBoast = [
"'I once hit a medusa so hard in the face its eyes saw each other.'", 
"'I once shouted the fire off of a burning orphanage.'", 
"'I once killed 7 men in one stroke.'", 
"'I once killed 7 flies in one stroke.'", 
"'I once lived for a year in a barren desert solely off of juice which I squeezed from rocks.'", 
"'I once killed a red dragon with fire.'", 
"'I stole a kiss from a nymph in a hidden grotto, cold as the moon she was, but twice as lovely.'", 
"'I once beat an ogre in an arm wrestle.'", 
"'I punched an incoming arrow once. It went right through the eye of the archer.'", 
"'Once had a dryad wanna inhabit my wood if’n ya know what I mean.'", 
"'One time, I beat the mayor in an egg spoon race.'", 
"'I once outdrank a clan of dwarves in a drinking contest.'", 
"'I once caught a fish that was TTTTHHHHIIIIISSSSS BIG.'", 
"'I got a free go at the land’s most expensive brothel by pretending to be the king.'", 
"'One time I seduced a god. That’s why they weren’t answering your prayers.'", 
"'I once blew out a fire elemental with a belch.'", 
"'I once drank an entire water elemental.'", 
"'My shadow is actually a Shadow. It does what I want because it’s scared of me.'", 
"'Once I was bit by a wererat and it turned into me.'", 
"'I once led an army of kobolds.'", 
"'I’ve been to the 7th layer of the Abyss.'", 
"'I once told a riddle so ingenious a Sphinx couldn’t solve it. It killed itself out of shame.'", 
"'I’m so good at handstands I can do them with two hands tied behind my back!'", 
"'I once drowned a merfolk.'", 
"'Grew a beard so rough it beat a mindflayer in a tentacle wrestling contest.'", 
"'Found Vecna’s liver and it’s not done me any wrong since I got it in.'", 
"'I once drank myself free from a bowl of watery death.'", 
"'I once ambushed a mimic with my disguise.'", 
"'I once threw a minotaur so far, he landed in a different kingdom.'", 
"'I once cut off all of a hydra’s heads at once.'", 
"'I once seduced a succubus.'", 
"'I once tricked a mimic with a fake adventurer.'", 
"'I once beat an ettin in a staring contest.'", 
"'Just last week, I ate 100 hard boiled eggs in an hour.'", 
"'I once domesticated a displacer beast. Nasty things are impossible to keep track of, so I had to get rid of it.'", 
"'I once defeated a clan of trolls while in the middle of a pie eating contest and still won.'", 
"'I flexed so hard once that the vampire sucking my blood popped.'", 
"'I once used all three wishes from a ring to get a nice mutton and lettuce sandwich where the mutton is extra lean.'", 
"'I can dodge a Spear of Backbiting.'", 
"'I once beat a Medusa in a staring contest!'", 
"'Drizzt Do’Urden personally gifted me a panther cub to be my familiar.'", 
"'I am the Raven Queen.'", 
"'I once drank a decanter of endless water dry.'", 
"'I once hit an owlbear SOOO hard, it turned into a bearowl.'", 
"'I beat Asmodeus at dragon chess once.'", 
"'I killed a man, with THIS THUMB.'", 
"'Lightweight! I once drank a dragon under the table, I’ll have you know!'", 
"'I once wrestled a dragon out of the sky.'", 
"'I once beat a Beholder in a game of I Spy.'", 
"'I’ve had, like, 50 heart attacks, and I’m still standing!'", 
"'I convinced a God to make a star for me, no you can’t see it from here.'", 
"'I calmed a raging barbarian.'", 
"'I once got a standing ovation from (a famous bard).'", 
"'I convinced (a famous cleric or paladin) to follow me.'", 
"'I put a suit of armor on a monk.'", 
"'I spotted (a famous rogue) sneaking around the city.'", 
"'I beat (a famous ranger or druid) at hide and seek in the woods.'", 
"'I beat (a famous wizard or scholar) in a trivia competition.'", 
"'I cracked a set of adamantine armor.'", 
"'I drank everything out of an Alchemy Jug.'", 
"'I exterminated a camp of ogres while wearing armor of vulnerability.'", 
"'I found an arrow of me slaying, stabbed myself with it, and didn’t pass out from the pain.'", 
"'I pulled myself out from inside a bag of devouring.'", 
"'I beat out someone wearing boots of speed in a foot race.'", 
"'I held a door closed through a Chime of Opening.'", 
"'I saw someone wearing a cloak of invisibility.'", 
"'I walked through the barrier from a Cube of Force.'", 
"'I’ve killed enough dragons to create a a set of Dragon Scale Mail for each dragon type.'", 
"'I hid from someone using a Gem of Seeing.'", 
"'I bench-pressed an Immovable Rod.'", 
"'I beat a Storm Giant in a wrestling match.'", 
"'I won a barfight against someone who had just drank a Potion of Invulnerability.'", 
"'I drank my weight in Potions of Poison.'", 
"'I found a Robe of Useful Items and the only patch on it was me.'", 
"'I opened something glued shut with Sovereign Glue.'", 
"'I walked through a Sphere of Annihilation.'", 
"'I found a luckstone carved in the image of me.'", 
"'Someone used Detect Magic, and all it found was me.'", 
"'I once converted a Mind Flayer to veganism.'", 
"'I was almost the king’ s brother/sister-in-law.'", 
"'I just downed the spiciest burrito you ever did see. Until a couple seconds ago my mouth was still smoldering.'", 
"'I once peed of a cliff and hit a bird three meters away from me.'", 
"'You know that mine in the nearby mountains? I dug it. With a single punch.'", 
"'I once kicked a shark so hard it exploded.'", 
"'I once hit a Mind Flayer so hard its tentacles went in its mouth.'", 
"'I went to a village in the far lands and drove the inhabitants insane.'", 
"'I’m a celestial travel guide looking for a green starship.'", 
"'I’ve danced with a devil in the pale moonlight.'", 
"'I put the man in manticore.'", 
"'I can cast spells with no hands.'", 
"'With my serenade, I once enthralled a siren.'", 
"'I’ve visited the cloud district often, have you? Oh what am I saying.'", 
"'A dwarf has no chance in our drinking my liver.'", 
"'I once stopped a hurricane by shooting at it with a bow.'", 
"'Dragons learned how to breathe fire from me.'", 
"'Your looking at the man who has made three volcanoes erupt prematurely.'", 
"'I once casted a tenth level spell.'", 
"'I once beat a demon so bad he begged an occultist sent him back.'", 
"'I once painted a portrait so lifelike the buyer started using it as a mirror.'", 
"'I’ve hiked so many mountains I know all the mountain goats by name.'",
]
let braggart = [
"Most Likely To Retire Early", 
"Most Likely To Catch On Fire", 
"Most Likely To Sell Their Soul", 
"Most Likely To Become Immortal", 
"Most Likely To Work For A Beholder", 
"Most Likely To Marry A Doppelgänger", 
"Most Stealthy", 
"Most Likely To Arm Wrestle An Orc", 
"Most Likely To Be Eaten By A Mimic", 
"Most Likely To Start A Cult", 
"Most Likely To Join A Cult", 
"Most Likely To Be Arrested", 
"Most Likely To Arrest Someone", 
"Most Likely To Meet The King", 
"Most Likely To Be Publicly Executed", 
"Most Likely To Ascend To Godhood", 
"Most Likely To Slay A Dragon", 
"Most Likely To Marry A Dragon", 
"Most Likely To Be Resurrected", 
"Most Likely To Defeat A Lich", 
"Best Sword Fighter", 
"Best Spellcaster", 
"Most Agile", 
"Most Likely To Die To Falling Rocks", 
"Most Likely To Be Granted A Wish", 
"Most Likely To Be Charmed", 
"Most Likely To Resort To Cannibalism", 
"Most Likely To Lead An Army", 
"Most Likely To Become A Teacher", 
"Most Likely To Commit A War Crime On Accident", 
"Most Likely To Commit A War Crime On Purpose", 
"Most Likely To Get A Bounty On Their Head", 
"Most Likely To Rescue A Princess", 
"Most Likely To Kidnap A Princess", 
"Most Likely To Get Lost At Sea", 
"Most Likely To Start A Duel", 
"Most Likely To Die In A Duel", 
"Most Likely To Pass Out Drunk In An Alley", 
"Most Likely To Get Lost", 
"Most Likely To Injure Themselves", 
"Most Likely To Own A Tavern", 
"Most Likely To Destroy A Tavern", 
"Most Likely To Be Worshipped By Tribals", 
"Most Likely To Discover Long-lost Knowledge", 
"Most Likely To Go Insane", 
"Most Likely To Get Trapped In Another Dimension", 
"Most Likely To Move To Another Dimension", 
"Most Likely To Be Forgotten", 
"Most Likely To Sacrifice A Virgin", 
"Most Likely To Be Sacrificed", 
"Mest Climber", 
"Best Swimmer", 
"Best Archer", 
"Most Charming", 
"Most Dangerous", 
"Most Likely To Get Framed", 
"Most Likely To Be Permanently Disfigured", 
"Most Likely To Practice Necromancy", 
"Most Likely To Die To A Trap", 
"Most Likely To Be Manipulated", 
"Best Ocean Navigator", 
"Best Subterranean Navigator", 
"Most Likely To Summon A Demon", 
"Most Likely To Win A Dance-off", 
"Most Likely To Lose A Dance-off", 
"Most Likely To Murder An Innocent", 
"Most Likely To Rob A Shop", 
"Most Likely To Sink A Ship", 
"Most Likely To Use Disguises Regularly", 
"Most Likely To Gain A Nickname", 
"Most Likely To Be Buried In A Proper Grave", 
"Most Likely To Fight In An Arena", 
"Most Likely To Die Shortly After Succeeding", 
"Most Likely To Forget Their Own Name", 
"Most Likely To Disappear Without A Trace", 
"Most Likely To Destroy An Entire Village", 
"Most Likely To Do Something Catastrophically Wrong", 
"Most Likely To Do Something Catastrophically Right", 
"Most Likely To Have An Evil Twin", 
"Most Likely To Sacrifice Themselves To Save Another", 
"Most Likely To Date A Different Species", 
"Most Likely To Lose An Artifact Of Great Power", 
"Most Likely To Explode Without Warning", 
"Most Likely To Frame Themselves To Hide A Different Crime", 
"Most Likely To Be Enslaved", 
"Most Likely To Enslave Something", 
"Most Likely To Prevent The Apocalypse", 
"Most Likely To Start The Apocalypse", 
"Most Likely To End The Apocalypse", 
"Most Likely To Polymorph Permanently", 
"Most Likely To Start A War", 
"Most Likely To End A War", 
"Most Likely To Tame Everything They Encounter", 
"Most Likely To Commit A Hate Crime", 
"Most Likely To Be The Target Of A Hate Crime", 
"Most Likely To Found A Village", 
"Most Likely To Be The Subject Of An Epic", 
"Most Likely To Write An Epic", 
"Most Likely To Develop An Unhealthy Obsession", 
"Most Likely To Eat Anything They Kill",
]
let toasts = [
`Heres to the Dwarfs for their great Brews!`, `Heres to friends both old or new.`, `Here to the gods. Let's hope they are watching over us.`, `Drink up. We have foes to slay`, `Here to whatever god you worship because we all are probably going to meet them soon.`, `May death come swiftly to our enemies!`, `Asmodeus! We'll be seeing you soon!`, `The Resistance endures!`, `A toast my friends, to the war's end.`, `May we all live longer than our foes.`, `Good fortune to all... except for [insert enemy race here], because bugger the whole lot of them.`, `Though you may never find the answers to your problems in the bottom of a glass, good drinking buddies can make the bad times more tolerable. So here's to you, my good friends.`, `Good life to you, and a short one to your foes.`, `A toast to the hardest working members of our party: our livers! Gods help us if they up and quit.`, `Bottom's up and top's down.`, `May we all never wake to a goblin's ugly face!`, `May the strong find peace, and may the weak be the ones to challenge us!`, `Here's to (the Rogue), for finding the coin to buy these drinks! Here's to (the Cleric), for healing our wounds and curing our hangovers! And here's to (the Paladin), for not lecturing us on vice!`, `Fortune and Glory, kids!`, `May their corpses be heavy with gold.`, `May at least one of live through this to tell the bard how heroic I was.`, `May your mother never find out.`, `May our life be long and prosper, and our death be far and peaceful.`, `*Awkward silence, expressive glance* Cheers!`, `May our path be that hard, we'll learn all we need to beat it.`, `I dare you to get what you want... And now, I suppose, the thing we want is drinking! So, cheers!`, `To the perfect match!`, `May future us won't regret about our decisions.`, `My heart is as full as my glass, when I drink to you, old friend!`, `To the king, and country, houses, and food, for the green living forest, filled with wood, To love, and passion, desires, and... rum... And the last, but not least... For your massive Mo... -- oh, shut up, *bardname*, I said it's enough two glasses ago! What's next, jokes about your strange appeal to dragons?!`, 
`May our world be full of adventures, We would quest, if shiny gold rang, May taverns contain suspicious strangers, and dungeons -- dragons to bang! .... *deadly silence* -- *uck, I told you! Go upstairs, or I will throw you there!`, `To you lot, I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve. But, I drink with every last one of you.`, `*Holding two drinks up in the air* To my comrade dear, Wish you could still be with us. Until then I will drink for both of us.`, `To the rogue who tried to poison my drink, buy better poison and hope you choke on your gruel.`, `To brewer of the drinks we are drinking, Gods' speed you majestic bastards!`, `Here's to tonight. We may not all remember it but, someone is bound to remember for us.`, `To our livers, they are going to have to do double time tonight but, they used to it by now.`, `*if the drinks were watered down* To the nearby lake, keeping this afloat since it opened.`, `*if the drinks are fantastic* To the (Tavern/Bar/Inn's name), Your bartenders and wenches need a raise.`, `To the (city guard/town guard/militia's name), keeping roads clear, the (county/city/town) safe, and brewers and merchants able to get here.`, `Here's to the Bard and his scab of a brain. Here's to the Dragon and all it has slain. The gate is knocked in and the town is aflame. And it's ours for the taking, and you get the fame.`, `Here's to the Bard and his knob of a head. Here's to the Orkney, the smoke, and the dead. The gate is knocked in and the town is aflame. And it's ours for the taking, and you get the fame.`, `Here's to the Bard and a pullin' me plum. Here's to the Beast and the rest of you scum. The gate is knocked in and the town is aflame. And it's ours for the taking, though you get the fame.`, `A toast to a very special person, Charlie Mopps, the man who invented beer!`,
`Here's to... here's to... uh... screw it. Here's to getting drunk!`, `Here's to [proprietor of the tavern or inn the party's in] and [name of the tavernmaid who served them] for tolerating our drunk asses for so long.`, `May your courage never falter`, `May your strength never falter`, `To companionship, warm beds, and hot meals`, `To fame and fortune`, `To good fortune`, `To good friends`, `To good health`, `To lady luck`, `To lasting peace`, `To new friends`, `To returning home safely`, `To the cook for an excellent meal`, `To the host for their hospitality`, `To the successful completion of the mission`, `To those who have fallen before you`, `May death come swiftly to our enemies!`, `Asmodeus! We'll be seeing you soon!`, `The Resistance endures!`, `A toast my friends, to the war's end.`, `May we all live longer than our foes.`, `Good fortune to all... except for [insert enemy race here], because bugger the whole lot of them.`, `Though you may never find the answers to your problems in the bottom of a glass, good drinking buddies can make the bad times more tolerable. So here's to you, my good friends.`, `Good life to you, and a short one to your foes.`, `A toast to the hardest working members of our party: our livers! Gods help us if they up and quit.`, `Bottom's up and top's down!`, `May we all never wake to a goblin's ugly face!`, `May the strong find peace, and may the weak be the ones to challenge us!`, `Here's to (the Rogue), for finding the coin to buy these drinks! Here's to (the Cleric), for healing our wounds and curing our hangovers! And here's to (the Paladin), for not lecturing us on vice!`, `Fortune and Glory, kids!`, `May their corpses be heavy with gold.`, `May at least one of live through this to tell the bard how heroic I was.`, `May your mother never find out.`,
]
if (chance < 25) {
return 'You hear the end of a conversation: "' + searchArray(tavernOverHear) + '"';
} else if (chance < 50) {
return "You hear a drunken boast: " + searchArray(drunkBoast);
} else if (chance < 75) {
return 'You hear: Well I was voted "' + searchArray(braggart) + '"... What about you?!';
} else {
return 'You hear a toast: "' + searchArray(toasts) + '"';
}
}
let output = searchArray([findRumor(), overHear()])
document.getElementById("EndConvo").innerHTML = output
};
function bardFind() {
function findBard() {
let tavernBards = [
"Jacobs- a fallen aasimarian college of swords bard that was banished from his home after taking vengeance on a former lawful evil warlock now turned cleric. Jacobs now travels with the Cobalt Ravens, an assassins guild of four members masquerading as street performers. Jacobs worships Olidammara and plays a flute that conceals a hidden short sword.", 
"Phillip Swiftfoot- a halfling college of lore violinist that left his village to seek stories and adventure. Phillip has such an optimistic outlook on life that it’s almost infectious.", 
"Snowy Night- a tabaxi college of glamour linguist that was brought up as a noble and was thought of as a half demigoddess because of her birth atop a holy mountain and her divine beauty. Snowy Night ran away from her home because of the overbearing rules she had to follow. She now works as a part time adventurer and tavern owner.", 
"Bao Liu- a blue dragonborn bardic dancer that had lost her family after a dragon had burnt their palace down. Bao is now a dragon hunter using her knowledge of the arts and Phoenix sorcerer lineage to eradicate as many chromatic dragons as possible.", 
"Clare Krath- an Aarakocra college of glamour acrobat that spends her time getting better at acrobatics every day learning from the greatest acrobats still alive.", 
"Oliver Brightmoon- a halfling college of glamour pianist that claims to be from the Feywild. Nobody is sure of Oliver’s tall tales but he believes them and to him that’s all that matters.", 
"Blue- a firbolg college of life orator that was raised in the swamplands and wanders the world in search of literature and people to share his knowledge with.", 
"Jed Silverhammer- a gnome college of lore fire spinner. A cheerful soul who began traveling at the young age of 12 to share uplifting stories and performances to people across the world.", 
"Darvius- a silver dragonborn college of valor bard and worshipper of Bahamut that was sent by the church to investigate rumors of an evil presence in a cave far east from his temple. He has traveled for a year now killing undead and searching for the next great evil to arise.", 
"Father Kiria- an elf college of lore bard and cult leader. Father Kiria has a small following seeking to summon an ancient aberration that will destroy half of the world. Father Kiria is a master manipulator and well traveled scholar.", 
"Jeffrey Fletchershot- a gnome college of valor bard that prides himself on his bow. Jeffrey considers archery as just as legitimate an artform as music and refuses to entertain the notion that any elf can beat him in archery. Jeffrey helped in the making of the first firearms and will occasionally use those as well.", 
"Merik and Ardur- An unlikely pairing of Lizardfolk (Merik) and Kenku (Ardur) this pair of bards have spent years in the marshes studying and incorporating the animal sounds (like frogs croaking, dragonflies buzzing and various bird calls) into their masterpiece 'Sounds of the Swamp'. Now they seek to bring this rustic music to the urbanites of the human cities. Their hope is to raise awareness and appreciation of the natural setting.", 
"Hans Glinckenstein- A gnomish bard/ mage whose favored form of expression is pantomime. His routine, which he calls 'Invisible Wall of Force' is remarkable only in that he uses Levitate and Feather Fall during the routine.", 
"Torrag the Elder- Torrag scoffs at being called a mere storyteller. His job is to keep the tribes myths, legends, and culture alive by preserving and passing on its oral history. Torrag May look old and fragile but he is still a well trained fighter.", 
"Dismal Merrick- some bards are exemplars of musical mastery. Not Merrick. His music is so awful people need to get away from it. Hearing it can ruin a man’s mood. People hire him to play for their enemies. It works, his bardic magic and abilities come from how BAD he is. Instead of inspiring others he discourages them. Instead of inspiring hope he causes dread. Instead of bringing wonder he brings disgust.", 
"Karthog the Brutal- this orc learned a rare trick, bringing out the music in his opponents. In battle every hit is a drum beat. Every scream a verse gone wrong. Karthog knows how to hit to turn their opponent into an instrument. Karthog has a technique he likes to call the human piano. Those who have seen the human piano are never the same.", 
"Gerrard- Gerrard was lucky to have a ring of sustenance. He never expected an angry wizard would trap him in a soundproof invisible box. Gerard has become a skilled mime out of necessity not choice.", 
"Jon Malick’s skeleton crew- Malick (he prefers to go by his last name) is a bard/necromancer whose instruments are unique. He has animated skeletons use their bones as drums, castanets, rib cage xylophones (due to carefully placed metal pieces). Sometimes he even has them dance.", 
"Bumf- an orc who has mastered the use of the war drum and war horn. Bumfs job given to him by the tribe is to blow the war horn at the start of the attack to scare away puny villagers and to bang his war drum in feasting rituals. Bumf gets angry when someone criticizes his musical stylings.", 
"Jessie- a yuan ti pureblood street magician. Jessie is a narcissist that believes she is the most genius person to ever walk the earth. Seeing people clap and rave about how someone could do tricks that are really no more complex than tying ones shoes makes Jessie laugh at how mentally inferior the public is to her incredible genius.", 
"Darren Loudbeard- A dwarf piper, known for his loud bagpipe. The sound he creates from his magical pipebag is alarming at first but as your ears adjust to the piercing sounds you cant help but jump in line with the crowd and dance a jig stomping your feet to the thunderous claps of feet all around you. As the song ends people push and shove to be next in line to drop ole' Darren a coin and tip their hat. Darren's beard has large grey braids that almost reach his feet, filled with ceramic tokens that look like bagpipes and war hammers.", 
"Dacrovil- A kobold bard who only performs in draconic, most of his lyrics are terrible but people think he is amazing because they simply enjoy the melody of his lute playing.", 
"Sven- a human bard with an electric guitar great axe. Sven is a viking that loves to learn of warriors long past. Sven uses lots of white and black face paint. Before Sven goes into battle he cuts an x into his chest for good luck.", 
"Faith- a tiefling bard that worships the god of music. Faith shares scripture and divine revelations through song.", 
"Samantha- a Medusa college of glamour bard that loves music and art. Samantha lives in a cave covered in beautiful paintings and is filled with the sound of viol playing. Samantha is a very nice person but has accidentally turned people to stone many times before.", 
"Chet- a Goliath bard pyromancer that uses his magic to dazzle and wonder crowds with fireworks. Chet was kicked out of his band of goliaths for being too weak. Overtime Chet has built a name for himself as the most fashionable bachelor in Tor.", 
"Sorrow- a tiefling college of whispers bard that had his heart broken on her wedding day. Sorrow plays somber melodies so everyone else can feel the sadness she feels. Sorrow becomes enraged at the sight of a wedding.", 
"Saldran- an author of numerous horror novels that has gone insane over the fear of elder gods he has written. Saldran is seen either writing more novels or preforming rituals for the gods in his stories.", 
"Bardbeak- A Kenku bard who has studied from the best, that is to say that he can imitate some of the greatest bards in the lands music with his uncanny ability of mimicry. A living jukebox.", 
"Gripple Derriwitz- The gnomish comedian. His quips are quick witted and his tongue is as sharp as a whip. Better watch out if your on the receiving end of his “Vicious Mockery.”", 
"Gary Sharptongue- a 500 year old dwarven bard that speaks very eloquently and has a love for languages. Gary can speak eight different languages fluently. Gary writes campaign speeches for politicians for a living.", 
"Gordon Thornton- a bard unicyclist and juggler that dreams of riding a unicycle across an entire continent. Gordon was once a city guard before he resigned to follow his passion of juggling.", 
"Bobo- a college of satire yuan ti bard that had learned to feel emotions through the laughter of children. Bobo became a clown and uses his bardic magic to spread joy across the lands.", 
"Carrie- a human bard that has an undying passion for popsickle stick sculptures. This passion is so strong she can shift the weave around her with it. Carrie loves using animate object to give her creations life.", 
"Tsumata- a college of swords bard and prestigious chef. Tsumata prides himself on his infamous Tsumata sushi recipe. Tsumata has been practicing his sushi recipes for 35 years.", 
"The Blackmore Sisters- two elven sisters only seen dancing in heavy rain storms. Air seems to crackle around these two young women as they sing songs in praise of the god of storms.", 
"Kote- the bartender of this tavern has red hair, red as flame. He sings of the adventures of a famous hero with such attention to detail that you could almost believe he'd been there.", 
"Six Tree- this friendly Tabaxi bard seems to coincidentally show up at every turn, and he always remembers the party and asks how their quest fares. In truth, he is a spy for a dark evil lurking just beyond the horizon.", 
"Darla Dawn, the Automaton- it's unclear if Darla is truly a technological marvel of clockwork and spring as the man carting her around claims, or simply flesh and blood cleverly disguised, but one thing is certain, her harp music could move the surliest thug to tears.", 
"Varadella- an elven vampire that was an excellent lute player in life and death. Varadella has grown bored with life and is looking for more victims to kill. Varadellas favorite hobby is making and playing instruments she creates from the flesh and bones of her victims.", 
"Truflord- a young college of lore bard that is paid to travel around with a group of paladins amd sing of their greatness. Truflord hates his work and the people he works with but they pay too good to leave. Truflord has written a few love songs for his wife when he returns home.", 
"Billy- A simpleton farmer who left in a philosophical pursuit of the meaning of life. Quick to befriend everyone and has a story pertaining to any situation. Jimmy always has a story of a relative who suffered a similar plight.", 
"The One and Only Jimmy Wilde- A former gladiator entertainer who is constantly given the role of being on the losing side. Seeing as it was a dead-end career, they left in search of making a name for themself. Jimmy takes everything at face value.", 
"Imelda- an elven bard born in the feywild and taught by satyrs to play the pan flute. Imelda loves nature and will die to protect it. Imeldas pan flute playing is beautiful and she is usually seen with many animals small and large listening to her melodies.", 
"Will Miller- a human college of valor bard and expert marksman. Will was given his first firearm by his father just before he passed away. Ever since Will has trained to be the best sharpshooter ever known. Will is trying to find a person named Jeffrey Fletchershot so he can challenge him to a duel.", 
"Connor Silverfoot- a halfling bartender and self proclaimed mixologist, Connor has served many an adventurer a drink. Connor plays the guitar but according to him his true artform is making booze. Those who say Conmors drinks taste awful are usually pronounced dead within a week after setting foot in his bar. The deaths are bewildering to locals and all of the officials refuse to speak on the matter. Connor says that he has nothing to do with their deaths and that they probably just made the wrong person mad.", 
"Cotton- a parrot that was once a human before he was cursed by a warlock after Cotton had slept with his wife. Cotton hangs around bars for free food and is trying to steal enough coin to pay for a cleroc to rid the curse from him.", 
"Jukebot- a warforged that has no memory of who they are. Jukebot has the word general scratched into his side and appears to be missing a few parts. Jukebot was given a job as a singer in a tavern and makes very good money there. Jukebot has the uncanny ability to mimic any sounds they hear which allows them to play songs from other people. Jukebot takes requests for three silver.", 
"Hansel- a yodeling tortle that loves climbing and swimming. Handles yodeling can be heard for miles even underwater.", 
"Yagrasias Zagiacarath- a triton college of glamour bard that was exiled from his home because of using illegal drugs. Yagra is a poet that loves using mind altering substances. Yagra is learning herbalism and alchemy while traveling from city to city performing rhythm and poetry.",
]
let chance = rollDice(100);
if (chance < 15) {
return 'You notice there is no bard currently performing!'
} else if (chance < 35) {
return 'You notice a new up and coming bard is performing.'
} else {
return 'You survey the scene and notice that a well known bard is performing: ' + searchArray(tavernBards) + '\n'
}
}
document.getElementById("Bard").innerHTML = findBard();
};
function instrumentFind() {
let bardInstrument = [

`A lute that was carved from an enchanted tree. When played, the illusion of sheet music and music notes can be seen flowing around the player.`, `A set of reed pipes made by a Satyr. Their sweet and mysterious sound grants disadvantage on saving throws to resist being charmed by the musician.`, `A vuvuzela that, when blown, sobers every person up within a 20 foot radius.`, `A tuba that spits out water, the pressure is determined by the quality of the music.`, `A comically long recorder that’s long enough to be used as a functioning quarter staff.`, `The Hydrophary – A species of aquatic plant that is vaguely octopus-shaped and can be played like a bagpipe. It wiggles its tentacles with delight when played.`, `Any type of string instrument that, when the command word is spoken, turns into a type of axe. The size of the instrument decides what type of ax it is: violin is a handaxe, guitar and lute are battle-axe, and bass is a greataxe. Speak the command word again to revert back to instrument.`, `The Phomenflumphen: You’re not sure what this is. It appears to be equal parts accordion, bagpipe and drum. The Gnome playing it seems to know what they’re doing though. Without training, all checks with this bizarre instrument are made at disadvantage.`, `A conductor’s baton that allows you to shift the pitch of someone talking to make it sound musical.`, 
`Cetacean Song – An ocarina seemingly crafted from snowflake obsidian that produces some decently low notes, and is shaped somewhat like an aquatic animal of some sort (inspired by this)`, `Conductor’s Instrumental – At first glance, it just looks like a typical conductor’s baton. However, depending on the direction and speed it is moved, it will softly hum a note.`, `Hidden Headbanger – It doesn’t look like too much, just a simple polished wooden 6-string guitar. When a bard plays it, however, it sounds as if it were an overdriven electric guitar. Has a disclaimer on the bottom written in small text: ‘FOR THOSE ABOUT TO ROCK’`, `Zamchroma – A zampogna with tubes made of a special glass that ‘catch and toss’ light that passes through them, giving them the appearance of being made of solidified and slowly shifting rainbows. It produces notes that echo very slightly, and overall sound heavenly or ethereal in nature.`, `A saxophone with special compartments for storing rations. A snacksophone.`, `The Dread Lute – Found deep in a dungeon on the corpse of a powerful bard. The wood is rotting and the strings are long gone, but 'playing' it still produces beautiful music, as if it were brand new.`, `The Flute of Love – The mage who sold this to you said it would make any listener fall in love. That doesn’t seem to be true, but any music you try to play comes out as the same love song, every single time.`, `Goblin Drums – A pair of small hand-played drums that can be worn around your neck with an old bit of rope. Whenever you use them to grant inspiration, any goblins in earshot also become inspired.`, 
`Chance the Rapier – This intelligent sword speaks with incredible creativity and rhyme. You can sing along with it to get the same benefits of a bardic instrument.`, `An enchanted accordion. Whoever plays it will slowly but steadily increases the tempo of whatever song they are playing.`, `A Stroh violin with the horn decorated with dwarven runes.`, `Namic’s Bladder – A set of Uilleann Pipes, black as ebony and with an incredibly clear sound. Said to have been created from the bones and bladder of a Black Dragon by Hersem Grelelian, who defeated the dragon on the way to her wedding and presented them to her husband.`, `A member of the violin family made out of iridescent ivory. It changes sizes and transforms into the different forms of the family depending on the phase of the moon, starting as a violin on the full moon and growing into a double bass by the new moon.`, `A very worn looking banjo with the peg head made out of a carved piece of driftwood. Grants the performer the benefits the rustic hospitality feature with anybody that listens to a successful enough (DC 14) performance using the banjo.`, `A foldable grand piano that also doubles up as a boat.`, `The mouthpiece of a flute. When held to the mouth, the rest of the flute is revealed. It’s ghostly blue and produces sweet but strangely sad notes.`, `A small flute carved from bone. When played, it sounds like a massive pipe organ, and even the liveliest of tunes has an unnerving, ominous tone.`, `Shoes of Tap: Tap dancing shoes that when you click the heels, as bonus an action, allows one to tap dance on any surface. Movement speed decreases by 10, because you are dancing, but ignore difficult terrain, can dance on water, and can dance on walls when tapping magic is in use.`, `The Pipe Pipe: A smoking pipe that doubles as a playing pipe. If you smoke and play at the same time you can magically control the shape of the smoke.`, 
`Brass Plate: This large brass instrument wraps around you and acts as plate armor. When you roll a 1 on sneak the instrument starts playing mocking music as you move.`, `A set of wooden spoons, ebony black with a glossy finish and silver inlay. After attunement, when the phrase ‘Spoonblades, to my aid!’ is called within a 15-foot area, the spoons transform into two spoon-shaped shortswords (Treat as a +1 weapon).`, `A set of four elderwood carved string instruments: The Shining Violin, The Viola Melodious, The Morning Cello, and The Bass Sonorous. The four instruments have a deep amethyst luster, and golden inscriptions in an elvish script. The inscriptions tell of a tryst between the God of Forest, and the Mountain Goddess. The quartet hasn’t been played together in 500 years.`, `The Bass Bass. It’s a large contrabass that looks like a fish. If you press a button on the neck of the bass, the fish head will tell a bad joke.`, `The Brass Bass Bass. A Double Bass, also fish shaped. Playing the bass gives you the ability to breathe underwater when playing the bass, and advantage while doing so.`, `The Brass Sass Bass Bass. An octobass carved for a giant, also piscine. When played with enough skill and force, able to deal structural damage to walls, doors, and other nearby objects. Will randomly interject with cutting remarks aimed at any nearby hostile creatures in their native tongue.`, 
`A jaw harp carved from a peacock’s bone. Can cast feather fall once per day. The performer has a faint image of a peacock’s tail appear behind them when playing.`, `Pearl – An undersized lute that slowly (yet constantly) drips water while it is being played. The water is fresh and potable, but only drips while the music continues.`, `The Golden Fiddle of Georg Ja. Legends say that he played this fiddle at the wedding of the ancient Queen Kershaw, banishing a demonic presence that had plagued her for a decade.`, `The Silver Fiddle of Georg Ja. Legends say that Georg played this fiddle as Kershaw’s kingdom burned, swearing revenge on the armies that had destroyed his lover’s domain.`, `The Brass Fiddle of Georg Ja. Legends say that Georg never really liked this fiddle.`, `Fae Flute: an intricate flute whose music is understood as language by Fae creatures. While playing this flute you have Sylvan as a language.`, `Dread Drums of Doom: Deep booming drums that make creatures uneasy. Enemy creatures have disadvantage on save vs. frightened condition. Creatures who are immune to fear/frightened condition are unaffected.`, 
`First Mate’s Harmonica: An old harmonica engraved with a compass card and a variety of fish. When played on land it summons a fresh breeze smelling of salt and seaweed, putting everyone in a melancholic mood missing the sea. Playing the harmonica on a boat or ship of any size however grants the mercy of the sea. As long as the bard is playing the creatures of the deep show now interest in attacking the ship, an aft wind drives the ship forward and rogue waves lose most of their power before hitting the ship. When the music ends the effect slowly wears off and things return to normal over the next 30 minutes.`, `An ancient set of pipes made from the hollowed out finger bones of a dead bard, with his soul still bound to them. When music is played from the instrument, listeners can faintly make out a gentle vocal accompaniment that perfectly fits whatever is being played.`, `A wooden, roughly carved hunting horn that still has patches of bark remaining on its surface. The deep, haunting sound it makes is dark, foreboding, and above all else, wild, with its notes echoing far longer than they should. Once per week, the player of the pipes may use their action to mark a creature. At the start of the player’s next turn, a pack of 2d4 spectral wolves coalesce into being near them and begin to hound the marked creature. The wolves pursue and attack the marked creature relentlessly, being completely immune to mental manipulation of any kind, and otherwise have the same stats as regular wolves. If a spectral wolf dies, it dissipates into the air for 24 hours, after which it reassembles itself within 100 feet of the target and continues its hunt. This effect persists until the marked creature dies or a week has passed, at which point the wolves give a final howl before evaporating and returning to the hunting horn, eagerly awaiting their next prey.`, `An intelligent banjo of common, almost aggressively average craft. Insecure about its own worth and fantasizing of respect and honor, it refuses to sound like a banjo and instead sounds like a grand piano through sheer force of will.`, 
`A magical harp that causes whatever false legend sung while playing it to become true.`, `A set of panpipes made from a tree struck by lightning. Playing the pipes allows the piper to subtly and slowly alter the weather to either induce or reduce thunderstorms.`, `The Dijj- a long, hollowed out greatclub, the Dijj makes a deep and oddly pleasant sound if blown into. If used as a greatclub, the strikes make powerful echoes, adding an extra 1d6 thunder damage to each hit.`,
`The Paltry Psaltery- A diminutive dulcimer-like instrument, in the hands of a talented bard, this instrument can bring bad luck and meager gains for enemies. As an action once per rest, a bard can play the Paltry Psaltery and force all enemies he sees to make a Charisma save (DC 10+ the Bard’s performance modifier) or be subjected to the effects of the Bane spell. The effect lasts for as long as the bard plays, plus 1d6 rounds.`, `Old Man’s Shawm- This otherwise nondescript brown shawm has three wrinkled old faces carved into the bell. If a command word is spoken and then the instrument is played, one of the faces will open its mouth, creating a strange overtone. Anyone hearing the resultant music for one full round must make a constitution saving throw or gain one level of exhaustion.`, `A small drum with a symbol etched on the skin. Closer inspection reveals that the symbol is in fact a tattoo denoting membership to a now-defunct bandit group. (Things did not end well!)`, `An ocarina made out of a large beetle exoskeleton. The sound is not dissimilar to a cricket’s chirp.`, `A 2-meter long string instrument with a thin slate body and metal strings (4 of them). Easy to play and far more durable than it looks. It has no name and nobody knows where it is from.`, `It looks like an axe but it’s completely blunt, hollow and riddled with holes. When swung it makes whistling sounds of different pitch – depending on the speed and direction of the swing.`, `A didgeridoo. Spiraling around it’s length is an epic saga of a great war from history, but key details are false including the victors.`, `A shamisen that has leaves growing out of the tuning pegs. If removed, they grow back very quickly.`, `An aged fiddle made of bits and junk, the finish is patchy and the pegs might even be bits of hardened cork, but an upbeat tune played on this fiddle never fails to get people wiggling fingers and doing a jig. If the listeners resist, they make a Charisma saving throw and dance uncontrollably for 1 minute on a failed save.`, `A white Japanese-style flute delicately inlaid with strange runes of blue-black metal. Close examination will reveal that the flute is carved from a human femur. It always sounds beautiful, but breathtakingly mournful.`, `An old and damaged wooden flute, held together with bandages. Inexplicably, there is a small plant growing out of one of the finger holes. It produces surprisingly beautiful music considering its condition.`,
`Bamboongos: A set of bongos made outta bamboo, that when played, summons 1d4 musicians that will give advantage to any bard song or inspiration. For every musician above the first one that is summoned, the inspiration/song gains a +2 bonus, for a total of +6.`, `A lute with the body made out a giant tortoise shell. Grants +1 to AC when not being played and is strapped to the bard’s back.`, `A french horn decorated with black bronze dwarven runes that can only play melodies in minor key.`, `A fiddle made out of pure white wood and engraved with elven runes that can only play melodies in the major key.`, `A harp with a body made out of an opaque golden glass that seem to glow as the instrument is played.`, `A bassoon with the bell joint carved into the shape of a dragon’s head that shoots smoke rings when played.`, `A cornett with an axe blade attached to the lower half that allows it to be used as a handaxe.`, `A shield with two metal sticks that can be taken out of the back. When hit, may either sound like a steel drum, a gong, or an odd snare drum, depending on which side of the stick the bard is hitting with, and where on the shield they strike.`, `The Whistles of The Deep – A set of stone chimes, expertly crafted by dwarven musicians in absolute darkness. The expert player can, while maintaining a proper rhythm, cast stone shape once per long rest.`, 
`A shoulder brace that can be inflated. When a pipe is inserted into the end, it can act as a small, high-pitched bagpipe.`, `A smaller lute that plays pluckier tones called a lute-kelele.`, `A banjo called the ‘Banjo of Truth’ that once per day allows the performer to play a bad country song to cast one charge of Zone of Truth.`, `A bedazzled flute called a Jewel that blows out different scented vapor.`, `Boots of the Dawn Chorus. A collection of bellows, whistles and trumpets adorn the soles of these shoes. Each dance the bard performs sounds like an ethereal birdsong. However, when the bard is fleeing from battle, it sounds a lot like a gaggle of honking geese.`, `A magically enchanted Glass Harmonica; when picked up it will float in front of the musician and start to spin as fast or slowly as the musician asks it to.`, `A shamisen that is always cold to the touch. When played, the leaves fall off every tree within a 100′ radius.`, `The squire’s hurdy-gurdy: the soul of the squire who last owned this instrument is bound to it. When it’s played, a ghostly voice sings praise of the nearest warrior deemed worthy (with varying degrees of accuracy).`, `A lyre that sounds inexplicably familiar to everyone that hears it. No matter what song is played, it always makes the listener feel nostalgic.`, 
`The Thunderhorn: A horn with a polished white-gold exterior. No matter how hard you blow into this horn, it is always comically loud.`, `A whistle that only people you choose can hear.`, `A tiny brass bell wrapped in silk cloth. When the cloth is removed, the slightest disturbance unleashes a deafening ring.`, `A 15ft Alphorn that when blown summons icy winds and frost. Oddly enough, it also causes a chance of summoning a St. Bernard with a small keg of brandy around its neck. (Roll a d20, if natural 20, dog is summoned.)`, `A mountain dulcimer made of black locust wood. The sound-holes are intricately carved in the shape of stars. It re-tunes itself on clear nights.`, `A lyre that suspiciously resembles the description of one belonging to a certain sun god. It seems to glow with radiance when played. Creatures associated with the moon visibly cringe when they see it, as if they do not like the thought of it’s existence.`, `A hurdy-gurdy made from darkwood, with enchanted strings that produce illusions while being played. The illusions are clearly illusions, and won’t trick anybody, but are entertaining nonetheless. The form of the illusions range from a tiny ship sailing across a wall, to sapling growing out of the floor. The illusions are always transparent to an extent, and appear almost holographic.`, `The Phoenix Egg – A beautifully constructed Red xun, said to be made from the egg of a Phoenix. It is said that, if it is played correctly, it will restore those who die around it to life (mimicking the effect of the revivify spell).`, `An Upright piano that is actually a highly mobile construct built with adjustable legs to be able to move in different terrain. If the piano is played badly or a less than favorable song is played then the constructs personality will take over and it will slam the lid shut, possibly on the musician’s fingers.`, 
`A string instrument created by and for Elven musicians. The strings are made of specialized bowstring. When they are plucked in the right way they can shoot an ethereal arrow, which deals sonic damage and leaves a ringing in the targets ears.`, `The Dragpipes: A set of bagpipes where the bag itself resembles a dragon’s skull. The horns are exaggerated to form the reeds while the player blows through the mouthpiece connected to the back of the neck. The sound of the Dragpipes mimics the roars of different dragons so the player can convince or cause frightening presence to people making them think there is one, or many dragons.`, `The Barbarian’s Cello: A cello carved from ironwood by dwarves. Its music, when played correctly, instills resolution, confidence, and defense in others.`, `Conch Shell of the Officer: Legend says that this trumpet-like instrument was used by the Captain of the Guards in one of the ancient merfolk kingdoms. Used to rally troops to protect its nation. Sometimes it will drip out water, even when it is completely dry. It is inscribed with the words ‘take me up’.`, `Fairy Bell: A tiny bell (not fairy-tiny, but regular human tiny) formed from silver and bronze. It has three icons on it. The longer it is rung in rhythm, the more cumulative the effect.`, `Harp of Hades: Necromantic magic flows off this instrument. Though it looks like any angelic harp, its music has been known to drive people to depression, sorrow, and madness. Any necromantic magic in the area increases in potency. Those unfortunate to hear its song are likely to see visions of horrifying events that they never knew about, such as the murder of a loved one that was disguised as a natural death or a repressed memory.`, `Marimba of the Wind: Under each tone bar is a secret compartment, perfect for a rogue to hide things. It also seems to bring impossible good luck to the player, though this cannot be proven.`, 
`The Triangle: If arcane words are invoked (which can be seen inscribed on the triangle if exposed to temperatures either hot or cold strong enough to kill a man), the center of the triangle becomes an invisible dimensional portal, like a bag of holding.`, `Organ of the Dreaming Land: When played, the nearest sleeping person will begin dreaming of the circumstances around the player. It cannot be played by anyone not of noble birth.`, `Drum, That Which Calls Thunder: A drum of unknown origin. It appears to be made from traditional methods, with clay and perhaps crocodile skin. But there is something more ancient about this drum that you can’t quite put your finger on. It turns any attack back toward the source (like turning back arrows to the people who shot them).`, `Perfect Stillness – This strange instrument appears to make no sound when played; however, all those listening become hyper-aware of all of the sounds around them.`, `The Master’s Desk – An exquisitely smooth guqin, carved of cherry wood and perfectly tuned every time it is uncovered. Believed to have belonged to Guit Prox, the ancient Minotaur sage of lore.`, `The Bann’s Fiddle – A light green Fiddle with a bow like a sapling, it is impossible to play the Bann’s Fiddle sadly. Every song has an upbeat, cheery tone. When sad songs are sung on the fiddle, there is a strange magic that turns them happy by the end, resulting in a strange retelling of many tragic sagas.`, `Red Chuk – A small red box with a wooden handle, the Red Chuk creates an impressive percussive sound when struck. Anyone playing has advantage on any persuasion or performance check to act in accordance with courtly formalities for the next hour.`,
]
document.getElementById("Instrument").innerHTML = searchArray(bardInstrument)
};
function currentlyPlaying() {
function songBuilder(){
let subject = [ `a young ${searchArray(["barmaid", 
"blacksmith's daughter", 
"farmer's daughter", 
"miner's daughter", 
"innkeeper's daughter", 
"harlot", 
"lady's maid", 
"scullery maid",])}`, `a(n) ${searchArray(["barmaid", 
"captain's wife", 
"farmwife", 
"fisherman's wife", 
"housemaid", 
"madame", 
"merchant's wife", 
"seamstress",])}`, `a(n) ${searchArray(["beautiful noble maiden", 
"young princess", 
"ugly princess", 
"young queen", 
"old queen", 
"wicked queen", 
"faerie queen", 
"old widow",])}`, `a(n) ${searchArray(["young novice priestess", 
"innocent virgin", 
"high priestess", 
"sister of mercy", 
"old prude", 
"oracle", 
"temptress", 
"zealot",])}`, `a(n) ${searchArray(["crone", 
"enchantress", 
"gypsy woman", 
"fortune teller", 
"potion-maker", 
"seer", 
"dark sorceress", 
"wicked witch",])}`, `a(n) ${searchArray(["alchemist", 
"conjurer", 
"illusionist", 
"magician", 
"necromancer", 
"pyromancer", 
"old wizard", 
"apprentice mage",])}`, `a(n) ${searchArray(["barbarian", 
"gladiator", 
"guard captain", 
"young knight", 
"proud knight", 
"old knight", 
"mystery knight", 
"sellsword",])}`, `a(n) ${searchArray(["bandit", 
"gambler", 
"jester", 
"outlaw", 
"pirate", 
"singer", 
"smuggler", 
"thief",])}`, `a(n) ${searchArray(["young acolyte", 
"exorcist", 
"healer", 
"stoic monk", 
"preacher", 
"old priest", 
"young scholar", 
"wise master",])}`, `a common ${searchArray(["blacksmith", 
"farmer", 
"fisherman", 
"herder", 
"innkeeper", 
"miner", 
"sailor", 
"tailor",])}`, `a(n) ${searchArray(["foolish king", 
"tyrant king", 
"wise king", 
"old lord", 
"young lord", 
"cruel prince", 
"handsome prince", 
"wealthy merchant",])}`, `a great ${searchArray(["bear", 
"boar", 
"bull", 
"dragon", 
"lion", 
"ox", 
"stag", 
"wolf",])}`, `a diminutive ${searchArray(["badger", 
"cat", 
"dog", 
"fox", 
"hedgehog", 
"rat", 
"snake", 
"spider",])}`, `a(n) ${searchArray(["crocodile", 
"frog", 
"fish", 
"mermaid", 
"octopus", 
"shark", 
"swan", 
"whale",])}`, `a(n) ${searchArray(["dove", 
"eagle", 
"mockingbird", 
"owl", 
"raven", 
"rooster", 
"sparrow", 
"vulture",])}`, `a(n) ${searchArray(["devil", 
"demon", 
"3", 
"giant", 
"ghost", 
"goblin", 
"griffon", 
"hag", 
"ogre",])}`, `a historical ${searchArray(["battle", 
"captivity", 
"death", 
"feast or fair", 
"illness", 
"storm", 
"tournament", 
"wedding",])}`, `a(n) ${searchArray(["cave", 
"desert", 
"forest", 
"lake", 
"mountain", 
"river", 
"sea", 
"swamp",])}`, `a(n) ${searchArray(["castle", 
"garden", 
"fountain", 
"inn", 
"market", 
"tavern", 
"temple", 
"tomb",])}`, `a(n) ${searchArray(["coin", 
"book", 
"goblet", 
"map", 
"shield", 
"ship", 
"sword", 
"wagon",])}`, ]
let popularity = [ `it was written by a legendary bard`, `it has a subversive double meaning`, `it was banned by a tyrannical ruler`, `it was banned by a priest or priestess`, `it has a humorous, bawdy style`, `it was a popular sovereign’s favorite`, `it was sung at a local hero’s funeral`, `it was sung at a magnificent wedding feast`, `its lyrics are completely outrageous`, `of no good reason; it’s just a catchy tune`, ]
let commonUse = [ `children’s birthdays`, `pubs and civic festivals`, `pubs and scholarly ceremonies`, `pubs and military camps`, `religious ceremonies and festivals`, `royal courts and tournaments`, `taverns and aboard ships`, `taverns and low brothels`, `taverns and mining camps`, `tournaments`, `wakes and funerals`, `weddings`, ]
let commonPerformance = [ `a solo without accompaniment`, `a solo with a single percussion instrument accompanying`, `a solo with a single stringed instrument accompanying`, `a solo with a variety of instruments accompanying`, `a duet with two male voices`, `a duet with a male and a female part`, `a duet with two female voices`, `a quartet of male voices without accompaniment`, `a chorus of singers with little to no instrumental accompaniment`, `a chorus of singers with a variety of instruments accompanying`, `a solo for the verses with everyone joining in for the chorus`, `rarely as possible; few people know the words, but everyone knows the melody`, ]
let tempo = [ ` ponderous`, ` slow and steady`, `n andante`, `n allegro`, ` lively`, ` lilting`, ` fast-paced`, ` frenetic`, ]
let melody = [ `dominated by punctuating rhythm`, `not so memorable as its harmonies`, `hauntingly beautiful`, `simple and easy to pick up`, `incredibly catchy`, `variable, depending on who's singing`, ]
let subject1 = searchArray(subject)
let subject2 = searchArray(subject)

let output = `A song about ${subject1 +" and "+subject2}, popular because ${searchArray(popularity)}. Sung at ${searchArray(commonUse)} as ${searchArray(commonPerformance)}, with a melody that is ${searchArray(melody)} and a${searchArray(tempo)} tempo.`
return output
}
var bardSongs = [
"'Snuffed The Magic Dragon’ – A song about slaying a dragon that has terrorized the countryside. This song has a part two called ‘Stuffing The Magic Dragon’ in which the party has the dragon stuffed and brought to their castle.", 
"‘The Deep One’s Sea Shanty’ – To anyone who can’t speak Aquan this sound sounds like an upbeat sea shanty sung in another language. To those who do speak Aquan it tells the story of ‘The One who causes the waves’ and how he fought the gods themselves to reclaim the sea as his own.", 
"‘Lycan Virgin’ – Famous wenching song punctuated by wolf howls. Werewolves struggle to resist joining in during these parts, as does anyone else who has had a few…", 
"‘Crossbow’ – A song about a Ranger who rides into town to collect a bounty, alive or dead, against the Barbarian Reckless Redd. ‘No one dared to ask his business, no one dared to make a slip, ‘cus the Ranger there among them had a crossbow at his hip.’", 
"‘The Wizard and the Wren’ – A children’s song about a wizard who built a wooden town taller than any in the land that was undone by a wren who needed twigs to build its nest.", 
"‘The Crown on the Head and the Crown on the Heart’ – An epic poem describing a king who was usurped and his journey of growth on his return to the throne.", 
"‘Ashkeeper’ – A slow and somber dwarven chant about the history of one of their oldest and deepest fortresses.", 
"‘Our Son Arsen’s Arsine Arson and Parson Carson’s Incarceration Assertion’ – This bar song is known for being a dangerous tongue twister, and requires a DC 20 perform or linguistics check to sing without a serious mouth injury. Failing the check results in being unable to sing or speak for 1d6 hours.", 
"‘My Shortest Love’ – a song about the love between an elf and a halfling (hence “shortest”).", 
"‘The Seven Dwarves’ – song about how seven dwarves help to rescue a human maiden poisoned by a female wizard.", 
"‘Blasphemy Song’ – a rhyming song where every verse is an insult to a god. It is usual sung at a speedy pace. Worshipers say any bard who sings the song will face divine retribution, but for most bards, this wasn’t their last song.", 
"‘The Seven Screw-ups That Saved the World’ – A song about an adventuring party in which the members kept dying but still managed to stop the apocalypse. Each verse is how they helped the party, and how they died is in the chorus: ‘There were Seven Screw-ups in the party in all, One sang with the banshee in the hall and then there were Six Screw-ups in the party in all’ Popularly altered to sing the praises of other unfortunate adventuring groups.", 
"‘Rocking Chair’ – A calm ballad about an old elven lady remembering the times when she was young and fierce.", 
"‘Cold Blows the Wind’ – The love ballad of a budding necromancer and the lover she lost to the sea.", 
"‘Letters in the Sky’ – A tragic tale about a prince exiled to the sun and a princess exiled to the moon, and how they can only express their love for each other by arranging the stars into messages. Usually, it ends with the performer gazing skyward on the final chorus.", 
"‘Pahoot’ – A children’s song (best played on the flute or piccolo) that parents roll their eyes at while their children giggle. It features verses about the exploits of Pahoot, the flatulent goblin, who somehow always gets the last laugh whenever he’s ostracized for his odor.", 
"‘Where You’ve Been’ – A song about a ranger who searches for his lost love, using his tracking skills, but he’s delayed by his memories of the locations he visits. At the end of the song, he finds his love waiting for him.", 
"‘Behind Blue Scales’ – song by a blue dragonborn who wants to break free from chromatic influence.", 
"‘What’s In A Bottle Of Elfish Wine’ – A popular song among taverns owners and their patrons. This fast paced song is widely known and adapted by everyone who sings it.", 
"‘The Night Groomer’ – a tragic story about a night time barber who was killed by a customer that transformed into a werewolf.", 
"‘The Lonely Golem’ – A song about a statue coming to life and starting a quest to find friends, forgetting that its job was to protect an ancient weapon built to destroy nations.",
"‘The Shortening of Meradian Finn’ – A Dwarven drinking song with thirty-eight official verses (and countless unofficial ones), the song recounts the punishment meted out against an Elven noble who stole from a Dwarven treasury. The chorus ends with a rousing slamming of glasses and a ‘in the end, he never did again!’ It is considered poor taste by many elves, which helps account in part for its popularity.", 
"‘The Bawdy Body of Biddy Badee’ – A raucous account of an old woman accidentally restored to youth and beauty. The song makes liberal use of alliteration and plays on words: ‘her newly charmed charms were enchanting enchantment; passing by barracks led to guardsman advancement…’", 
"‘The Cruel Changeling’ – A mournful ballad of a wandering bard falling for a woman at a fair, only to discover that she is wearing another’s face.", 
"‘And All for a Turnip’ – A song best sung as a round. It tells the story of a hungry halfling and his incredible exploits finding a snack.", 
"‘I Eldalië Nairii (sometimes translated as The People Mourn)’ – An Elven Dirge describing the loss of Cyrindes Flestivel, a beautiful and kind mage, to a spreading plague, along with many of her people. A melancholy ode to loss, some have taken it as a representation of the Elves’ sense of mourning for the loss of their brighter world.", 
"‘I Eldalië Snuiiiiii (The last word is used to sound like snoring or deep breathing)’ – A parody of the Elven Dirge ‘I Eldalië Nairii’, the song is of unknown source; it tells of an Elven bard singing the dirge, while the listeners fall asleep from boredom. A sure way to insult the singer of such a dirge, it is best sung with as much false pomposity as possible.", 
"‘But the Gnome Was Never Seen’ – A children’s song, used to remind Gnomish youths about the importance of caution and care.", 
"‘Adam the Easygoing’ – A relaxed song telling the tale of the titular Adam, a large, pudgy human paladin with an odd knack for befriending those he defeated in combat.", 
"‘I Write the Spells’ – A catchy if somewhat easily grating little song of unknown origin. If sung, it makes certain wizards go absolutely berserk.", 
"‘Nyarna Nwalcamun’ – The Saga of the Hero Grefedd and his journey to destroy the sentient cursed sword Nwalcamun. Traditionally, the climactic final battle scene is punctuated by the beat of a hammer on an anvil, representing Grefedd’s smashing of Nwalcamun while under attack by a drow army.", 
"‘The Green Eyes of Mallistari’ – The wooing song of a human woodsman for a half-elven maiden ‘met in a shady glade.’ The song is notable for a memorable bridge, often used when teaching the lute.", 
"‘Ga-Grosh For-Thaash’ – A song adapted from an Orcish marching anthem, useful for learning the rudiments of Orcish.", 
"‘The Oysters of Miss Marchelle’ – A sea shanty, recounting the joys of stopping in port at an establishment called ‘Harbor Belle.’ The song declares that ‘no sailor can resist the delight of the oysters of Miss Marchelle.’ The shanty, unlike many such songs, is not clearly innuendo, although it certainly may be (and many sailors sing it as such).", 
"‘Arnash Quadmatter’ – A song mocking the quintessential absent-minded wizard, referring to the foibles caused by having ‘his nose in a book, a book, a book…’", 
"‘The Missing Child’ – A mournful Elven song about a mother looking for her lost child, eventually going mad with grief and drowning herself, only to rise again as a banshee." < "‘Grandma Got Eaten By An Owlbear’ – A Popular song in winter months reminding people that they shouldent allow their elderly ex adventuring grandmother to attempt to wrestle monstrosities.", 
"‘You Can Just Call Me The Gnome’ – A fast-paced, silly song telling the increasing exploits of Hamish McTamish, a fictional gnome adventurer. Each time the chorus is sung, Hamish’s name is lengthened with more titles (the last chorus includes as many silly titles as the singer can think of and can sing in a single breath) followed by ‘but you can just call me the Gnome!’ Although believed to be human in origin, gnomes love the song, and an informal competition has sprung up as to the longest final chorus. The current record belongs to Sprigvill Gaudynack, who (via both her own talent and magical augmentation) kept the last chorus going for three and a half minutes.", 
"‘Callaud’s Pre-funeral Dance’ – A sprightly instrumental air for country dances. If played with a performance check DC 18 or higher, it functions like ‘Otto’s Irresistible Dance’ for anyone not in combat or threatened (i.e. it will make listening townsfolk break out into dance, but not if you are in the midst of robbing their homes).", 
"‘Long, Gone Galangal’ – A love story told through Gamelan music about an adventurous Chef seeking a rare root in the forest. Instead of finding it, they find the love of their life. The song is quite long, requires a large number of musicians to play properly, and has a happy ending.",
"‘Untranslateable Orcish Proverb’ – A morality tale operatically told through Carved Masks, Huge Percussion Instruments (Taiko style Drumming), Slapstick Pantomime, and Throat Singing techniques. A classic of High Orcish culture, now practically lost to time and the collapse of High-Orcish society. The choregraphy is quite energetic.", 
"‘Great-Grandmother Will Enjoy Eating Your Flesh An Orchestral Eladrin Morality Tale from the Far Fey Realms’ – A bold hero cheats and fails to respect the ancestral Mother-spirit. The mother spirit holds the hero to his deal and devours him for his crimes. The tale is told non-verbally, through colorful illusion and intepretive dance.", 
"‘My Lord, Come-a-Leaping’ – A bawdy Halfling tale about a Randy Prince who is turned into Frog when he comes on too strong to a powerful and beautiful Halfling Sorceress, and discovers he likes being a Frog more than a Ruler.", 
"‘The Farmer’s Corn’ – A bawdy tale about a comely farmer’s daughter who mishears something someone said, and spreads gossip around the village.", 
"‘The Three Spinners’ – A children’s Tale retold through a tongue twisting call and response song. It is about three unmarried magical Farm-women who challenge that they can out-spin (thread) better than anyone. They challenge a devil, who curses one with a swollen foot, one with an infected finger, and one with an infected lip. The woman with the infected lip’s line is supposed to be sung while holding one’s tongue. In the end, the women win, the devil is defeated, and each one wins more gold than they know what to do with.", 
"‘The Town with No Name’ – ‘I came across a pokey town. Not much going on and curtains all down. I came across a smokey tavern. Not much going on in that pokey town.’ A slow sad song about a old woman that lost her way and found a town not on any maps they brought and only too late discovered it to be a ghost town. (Actual ghost town not just one that was abandoned).", 
"‘Beware A Human Bard’ – A pseudo-cautionary song about the lascivious characteristics of human bards; the song begins with an Elvish mother warning her daughter, and proceeds through all the more common races into more and more ridiculous warnings (‘Mama Golem warns that he’ll say he likes your rocks, but what he’s really thinking of…’)", 
"‘The Fall of the Sun’ – A mournful Aarakocra ballad, said to have been written by the first to travel from the Elemental Plane of Air and see a sunset.", 
"‘The Cheese Song’ – ‘Cheese Cheese Cheese Cheese Cheese Cheese Cheese Cheese Cheese Cheese’ A song used by Kenku bards who create melodies out of the different voices and accents they have heard the word in the songs they sing.", 
"‘Glida’s Wedding’ – A traditional halfling travel song, describing the setup for a halfling wedding, ‘held in the shadow of the wagons on a Summer Sunday.’", 
"‘The Flute & Lute’ – A ‘dueling instruments’ style song featuring the eponymous instruments. While some bards have added words to the lute portion, it is usually simply instrumental.", 
"‘Bear Bride’ – A song about a human maid, enchanted by a fair traveler into leaving her home, who meets a sad end when she discovers the traveler is a dangerous druid. Likely originating in legends warning of associating with strangers.", 
"‘Rocks Fall’ – A cautionary song about travelers who did not heed the warnings of the gods and met a sudden and tragic end in an avalanche.", 
"‘Green Fields, Grey Fields (The Old Woman and Young Girl)’ – A song about an old woman walking with her great-granddaughter. The song is both nostalgic and melancholy.", 
"‘The Solemn Judge’ – A song about an irascible old magistrate, his beautiful daughter, and the blacksmith’s son who falls for her. The last verse tells of the judge marrying the happy couple.", 
"‘Fleshy Pinklings’ – An Orcish Festival song, championing the power of the Orcish races and declaring their superiority over the rest of the world, and their destiny as conquerors.", 
"‘Cloth in the Street’ – A protest song, originally written in Malthcumband, calling for weavers to rise up against an unjust leader. Banned in many evil-aligned areas, the song calls for the people to rise up and take back the city. Ironically, one of the governments to ban the song is the tyrannical Communal Autocracy of Malthcumband, formed by many of the same weavers the song was first written for.", 
"‘The Colors Of Death’ – A colorful tale of how an adventuring party was brutally murdered by all the chromatic dragons at once.", 
"‘Well Well Well’ – A song relating how several people did mischief and subsequently fell into a hole in the ground. The chorus starts with: ‘Well Well Well, look who fell here!’.", 
"‘To The Death’ – A marching song about a young soldier who plans on dying bravely to defend their homeland, and asks their leader to write a letter home for them to their one true love. It was quite popular long ago, but is now considered cloying and outdated.", 
"‘Ale for the Victorious’ – A popular drinking song sung by soldiers while off-duty.", 
"‘To My Lover’s Lover’s Love’ – A downer of a song, this tear-jerker is a letter dictated, postmortem, by a forlorn lover telling all the sordid and dirty deeds of their former lover, now in the arms of another.", 
"‘Sir Dalloway the Duelist’ – A song from a hundred years ago, poking fun at nobles and fragile honor. It was once considered unlawful to sing it in polite company, but it is now a popular folk ballad that is quite catchy.", 
"‘Rhetting the Flax’ – A work song about how many bales of flax a young and ambitious villager promises to grow, harvest, prepare, spin, weave, and sell, so they can have enough fabric and gold for a huge wedding, if only their lover would return their affection. The song is a thinly veiled sexual innuendo.", 
"‘The Horrible Haggis of Hampstead Heath’ – A rhyming cumulative song about a mimic that swallows an farmer’s old, rotten haggis, gains magical powers, and then goes on a rampage. It devours an entire town, where every occupant, their occupation, their children, and the name of their family pets are listed. At first no-one stops it because they are too self-centered. In the end, the town’s guards and even the mayor are devoured. The song has a happy ending as the unlikely hero lets themselves get devoured and then slices open the mimic from the inside, releasing everybody safe and sound. The best bards are able to keep the crowd going for an entire hour, and then recite in reverse order the entire population of the village.", 
"‘Ogre-Melon Crawl’ – A catchy ditty which is a comedic precautionary tale about walking and not riding a horse if you have been drinking Ogre-Melon wine.", 
"‘Two Hundred and Seventeen Heartbeats’ – a controversial Elven composition. The singer takes a breath, then measures their pulse in silence for the duration that the title implies, while the audience is meant to slowly embrace the many natural sounds taking place during that time as a song of their own. It has been hailed by some musicians as a deep, thoughtful reflection on natural sounds, but criticized by others as a bad joke.", 
"‘Dwavers Wumblerubs’ – A halfling nonsense song, meant to sound like, but not actually be, Dwarvish. Sung with mock solemnity.", 
"‘Slashworthy’ – A sea shanty about a cutlass that never went dull, until the captain of the ship used it to shave his back.", 
"‘The Old Dun Cow’ – The dedicated patrons of a tavern take refuge in the cellar while the building burns down around them, and take advantage of the taverner’s stores while waiting to be rescued.", 
"‘The Hollowed One’ – A tale about a man who gave his mind, will, and voice to be able to house a disgraced god to protect his people. Any who hear it are inclined to feel a deep lament for this person.", 
"‘The Snarl’ – A frightening song about gnoll attacks, with reference to the sounds they make beforehand. Sure to give a frisson to listeners.", 
"‘Duplicitous Dannalor’ – A song about a half-elf man who is having simultaneous affairs with an elven woman and a human woman.", 
"‘Dreaming of an Inn’ – A ballad of an adventurer in the wilderness, missing civilization and bemoaning the uncouth surroundings and travelling companions.", 
"‘Gandavous Thunke’ – Oh, Gandavous Thunke was a dangerous drunk with chaos instilled in his soul, And when faced with sellswords, or rampaging Orc Hordes, Or an angry cantankerous Troll, Old Gandy would growl and fix them with a scowl and unleash the magic inside, Calling forth lightning, or- equally frightening- A fireball, leaving them fried. Now, though it seems tragic, the use of the magic has had an effect on his hue; So if you’re foolhardy and meet him at a party, you can call him Old Gandy the Blue.", 
"‘This Moment of Magic’ – A love song about a wizard’s apprentice falling for his classmate as they cooperate in the creation of a summoning circle. ‘Though I open a gate to the Plane of Air, and float through unending skies, I would never find night that was dark as your hair, nor a view as blue as your eyes.’", 
"‘Robin Redbreast’ – A song about a bird hopping through the forest. Although unknown by many, including some of its singers, there is a second message contained in thieves’ cant within the song, describing the guard patterns of the Royal Summer Palace of Keann.", 
"‘The Future Journey’ – A Dwarven song about the afterlife ‘dug down below.’",
"‘Tenting on the Old Campground’ – a ballad of a soldier honoring and remembering those they’ve lost and wishing for an end of the war they are fighting.", 
"‘My Hedgehog Son’ – A catchy, nonsense, drinking song about a magical, talking hedgehog that gets adopted by a childless farmer, the hedgehog rides a rooster like a knight on a horse, and makes the farmer rich. The song is filled with tongue twisters. Bards occasionally challenge each other to invent and repeat new verses, each more difficult and hilarious than the last, while taking a drink after every flubbed line.", 
"‘The Silken Meadow’ – Who knew ancient Eladrin epic poetry turned thousand year old ballad could be so raunchy?", 
"‘Llolth’s Lullaby’ – An adventuring bard somewhere made it all the way down to the underdark, and heard one or two of the teaching songs sung by the Creche Matrons who give young Drow infants the education they need to survive the rigors of life; the song is in a deep dialect of undercommon that is almost never spoken anymore, but it is filled with all sorts of ‘Learning Magic’, mnemonics, and cultural references that makes it a sort of memetic hazard (you NEVER forget the words if sung by a powerful enough teacher), but the effect is less so when you don’t understand the language. That adventurous bard made it back to the surface, but not understanding the dialect of the deep, transposed the lullaby into a few other chords and added an improvisational lick of their own. That was a thousand years ago, and people have been humming and playing the tune up here ever since then, 50 generations later.", 
"‘Health Potion #9’ – A song about a long-suffering herbalist companion to a luckless knight and the scrapes the two of them get into. In the end, they end happily- the knight marries a guard captain who arrests him, while the herbalist falls for a local fortune teller.", 
"‘Ghouls in the Graveyard’ – A song about running through a graveyard seeking to avoid the attack of undead.", 
"‘A Red Ribbon’ – A murder-ballad. A lover is given a red ribbon, the lover cheats while wearing the ribbon. The lover is strangled with said ribbon. The song is sung from the perspective of the lover wearing the red ribbon and ends abruptly, mid verse.", 
"‘She’s Won the Crusade’ – A song about the exploits of a halfling bard, celebrating her exploits in the Great Crusade of Nevis with increasingly impossible descriptions of her victories.", 
"‘Last breath’ – A song about the recent death of a loved one, party member, and loss, the song goes through the 5 stages of grief as well.", 
"‘Hurry Up and Die’ – A song about a necromancer seeking a zombie companion, but surrounded only by living creatures.", 
"‘Run Through The Jungle’ – A saga of adventurers who managed to successfully get through the Haunted Temple of Khymann’roe and obtain the Crystal of Nor’Vesh without ever entering combat- simply by running away.", 
"‘No Rest For The Wicked’ – This song tells the tale of Caela of the Mammoth, a paladin of vengeance from a barbarian tribe, on her quest to hunt down the travelers who robbed and killed her father.", 
"‘The Stew’ – a Farcical portrayal of an foolish adventurer getting news that their loved one has decided that they are probably dead and has moved on. The distraught adventurer falls in love with the attractive savage, promising they’d ‘Jump in the Stew for You’. It has become a popular saying amongst foolish young lovers.", 
"‘There Is No Mountain’ – A chant developed in the monastery of Gar-Yin. The chant is used to focus the speaker away from the material realm, and declares the non-existence of the mountain, valley, and river visible from the monastery’s meditation area.", 
"‘The Scornful Beauty’ – A human traveler falls for a Dwarven gemsmith’s daughter, but she rebuffs his advances. The song calls on her to turn her head and consider his suit.", 
"‘Dihen-Nin (Forgive Me)’ – A mournful plea by an Elven soldier to his fallen comrades, begging their forgiveness for his survival ‘when your songs have been ended.’", 
"‘Captain Hennion’s Wife’ – A decidedly ribald army song about the wife of a commanding officer; it is common to adapt a verse to be about the wife (or daughter) of a current army leader. Singing this song can be a good way to end up in the stocks; nevertheless, it is very popular in camp.", 
"‘And Another Tree Falls’ – A mournful tale of a dryad, trying unsuccessfully to protect her grove from the incursion of a growing human city. This song is abnormally famous for starting bar fights, especially if there are urban and wild elements in the tavern.", 
"‘Clotted Soil’ – A recounting of the betrayal of King Bhoulthekk Bramfisted and his army by the Elven nation of Alv’dirae when the Dwarven army stood to defend Alv’dirae’s borders from attacks by the Ghowldresh Empire. One of the often-quoted verses from the saga includes the line ‘And may I trust a broken axe before an elf again.’", 
"‘The Old Fisherman’ – A shanty about a mysterious old Dwarven fisherman, encountered in the middle of the ocean on a little skiff. According to legend, if the fisherman is disturbed by a ship and not treated with respect, he kills every guilty soul on the ship with his gaff and leaves them hanging from the yardarms like a fish market.", 
"‘Simon McGurk’ – A shanty about a brilliant but lazy pirate. ‘Oh Simon McGurk, scared stiff of work, sailing all over the sea…’", 
"‘Greed’s Foul End’ – A movement from a morality play featuring a single musician and a vocalist. The piece is about the dangers of greed and the benefits of charity. Poignant, but difficult to pull off; often a touchstone work for performers of an ecclesiastical bent.",
];
document.getElementById("Song").innerHTML = searchArray([searchArray(bardSongs),songBuilder()])
};
function drinkFind() {
function findSpDrink() {
let drinkSpecialty = [
"The Flaming Dragon – A spicy beer that causes the user to breathe fire when they burp.", 
"The Banshee’s Breath – white, swirling liquor made from a special translucent wild berry. Tastes sweet, has an effect similar to mint gum in that it always feels cold.", 
"The Mountain’s Bounty – A fine liquor made using water from a glacial stream. Always refreshing, and always makes you feel cold no mater the weather.", 
"Mawxie – A drink all the locals cite as a local treasure. Tastes disgusting.", 
"Bog Grog – A mix of Rum, Orange Juice and fermented herbs that, when drunk, causes the user to gain advantage on saving throws against being poisoned for 30 minutes.", 
"Frost Mead – Honey and the tear of an Ice Giant make this shot. The crackling blue sparkle and the jet of icy breath you have for rest of the day is worth the expense.", 
"Weatherbee’s Whirler – Invented by the perhaps too inventive Filbus Weatherbee, this drink is testimony as to why it is a bad idea to point a gnome’s sharp mind towards the creation of a new brew. After spending many years living among the dwarves, Weatherbee made his way home with a drink even the stout folk couldn’ t handle. This monstrosity is laced with latent magic designed to lessen the chance of drinkers dying from its ungodly alcohol content, and reportedly tastes like 'A kick in the face from a horse.' After one shot of this drink, the drinker is shunted into a chaotic haze of blurry awareness, bolstered confidence, and overpowering drunkenness. In addition, the latent magic in the brew causes minor, uncontrolled magical effects to occur around the drinker at random times during the haze. The nature of these effects is up to either the DM or the player, so long as the effects are sufficiently insignificant. After 1d4 hours, the haze drops away and the drinker immediately and almost violently falls into a deep sleep so that they may recover.", 
"Dragonborn Bloodwine – When you drink it, you are able to use a breath attack once within the next 10 minutes.", 
"The Quieker – nasty rum that gives a high pitched voice for 1d4 hours.", 
"Faerie Fireball – a delicious cinnamon whiskey made with a touch of Fey magic. Causes uncontrollable hiccups for 1d4 hours. With each hiccup a small cloud of shimmering breath is released.", 
"Lily in a Well – a tall mug of ale, half full with an edible flower garnish.", 
"Hammer Beer – One glass will make you feel like you just hit yourself with a hammer. Minus 5 HP.", 
"Dragon’s Piss – A beer that tastes exactly like one would suspect by its name. For sure not a drink you need a second one of.", 
"Shamrock Shake – Instant dc15 con save. On fail the patron is incapacitated. No save required if patron has Irish(sounding) accent.", 
"The Sun’s Glory – A citrusy cider that makes your eyes glow like an Aasimar.", 
"Black Midnight – A drink created by necromancers to honor fallen necromancers, Bitter with a touch of rum. Those who drink it have nightmares of dying and spending an eternity rotting away inside a coffin. This helps enforce necromancers to contemplate their own moralities.", 
"The Phoenix– A peppery drink that burns on the way down, and then again on the way out. It is often used as a prank on drunk companions, who have a nasty surprise waiting for them the next time they go to relieve themselves.", 
"Hair of the Bloodhound – Once you have become intoxicated on this brew, you gain the usual drawbacks of drunkenness but gain advantage on survival checks.", 
"Seer’s Solution – A mildly viscous green liquid. The first two shots have no effect. The third gives you truesight up to 60 ft for 1d4 minutes. The fourth and subsequent shots give the drinker horrible audio/visual hallucinations for 1d4 + 2 hours. Counter resets at dawn.", 
"Spider’s Bite – Take 1d8 poison damage on a failed CON saving throw. Packs a mean punch.", 
"The Fortnight – Very strong alcohol. If you actually drink enough to get drunk, you stay hammered for days.", 
"Tinkerer’s Tincture – dark and smooth, and when you drink it all the clicking, whistling, and scraping noises are more apparent to your ear.", 
"2 Couples in a Shared Household – (much easier'if teabags exist) Two different types of hot tea, 2 of each, into one mug.", 
"Sucker Punching a Rabbit – A single teabag steeped in the biggest mug you have.", 
"Buried Treasure – A single, very sweet, rather expensive hard candy is stuck to the bottom of a mug of very hard liqour. Once you’ve drunk it all, you get a spoon to pull it off with.", 
"Ouch – Two full shots worth of lemon juice put into a glass of very high proof alcohol.", 
"What was I Saying? – An unassuming shot of very strong alcohol, with a cherry in it, usually taken in the middle of a conversation, which is promptly ended.", 
"Actual Torture – 2 Teaspoons of salt which are to be eaten all at once. Then washed down with a citrus based liquor. If anyone else offers any drinks, their hands are free game for attack.", 
"The Green Kobold – The first drink to ever be served in a piece of ham, with the skin. 1 shot of herbal liquor wrapped in ham. To be eater all at once. Probably fixed in place with at least 1 pin, make sure you pick it out before you eat it.",
"End of the Line – Very high quality, rather expensive alcohol. A coin is flipped. If heads, your drink is free. If tails, you are forced to drink until you either die or pass out. If you regain consciousness, you must continue drinking.", 
"Traffic Stop – Invented by a Diviner. Whenever a fight seems to be brewing, everyone orders a traffic stop. It’ s a mug of 3 separate liquors that stay separated in their mug, all very strong. The goal is to drink it all before the local police forces arrive.", 
"Dragon Milk – not really milk, or related to dragons. It’ s an expensive white drink, resembling milk(duh) that removes any alcohol in your body. As a result you exale fire in the form of a single burp, resembling a dragon.", 
"The Necromancer – a drink for those who fall unconcious from alcohol. It’ s a green glowing liquid. Also known as the ‘Corpse Reviver’- when poured into the unconcious persons mouth he / she gets up and walks in a way similair to a zombie.", 
"Beholder – a delicious drink decorated with an eye or multiple smaller ones. Feels like normal alcohol but gives the person a (false of course) feeling he/she has multiple eyes after drinking enough of it.", 
"Elysium – a nonalcoholic drink that smells and looks as bad as it tastes. Some compared it to trash, vomit or even excrement but only because they couldn’t find the adequate foul words. Most refuse to look at it, let alone allow it to come close to their nose. Only those with the strongest will manage to gulp it down. Once drunk, the person experiences true bliss, which seems to last for decades. In reality it’ s a few seconds.", 
"Nine Steps – commonly known as‘ The Niner’ or by it’ s full name‘ Nine Steps to Hell’. It is a liquid that when left to settle separates into 9 parts, the bottom one being pure black and the top a beautiful red with a gradient in between. After drinking it the person seems frozen for a few seconds, but to the person who gulpes it down it feels like days, weeks, maybe even months of 9 different experiences, all basically a form of torture. Often used as a torture method but sometimes drunk to prove ones mental strength, as those that can’ t endure it go insane. The niner is a rare drink because it’s extremely hard to make. An amateur making it, if the ingridients aren’t correct to the milligram, makes a drink that causes instant death.", 
"Honey Pine Dew – An imported halfling mead, served in small cups. Very pleasant taste, cheap in halfling towns, but expensive elsewhere.", 
"Cubed Spirit – This drink is served as a hollow ice cube with liquid spirit within. As the ice melts in your mouth the drink will come out. How exactly this novelty drink is produced, is a well kept secret.", 
"Milky Way Whisky – A light blue drink that tastes like very watered down, sweetened milk with a lot of alcohol. Besides giving a quick buzz, it also gives bone, and thus teeth, a blue fluorescent glow for 1d4 hours.", 
"The House Special – This drink doesn’ t have a particular name, but it’ s cheap. It doesn’ t really have an effect. In fact, you’re pretty sure the bartender is simply casting prestidigitation on dishwater to make it taste like like it has alcohol in it.", 
"True Dwarven Stout – A strong drink, not recommended if you cannot handle your alcohol. Traditionally served on the rocks, literally. There are pieces of stone lying on the bottom of your drink. Said to give the true mining flavor. This drink will make any dwarve feel very nostalgic.", 
"Petralias Wine – A very expensive wine that is served as a single droplet. It does nothing for thirst or getting drunk, bit the flavor is said to be very concentrated and the lack of drink quantity should make the experience richer. Typically ordered by very pretentious people.", 
"Golden Goat – Fermented goat milk and honey.", 
"Star Liquid – A really black drink resembling the night sky. If you drink it you experience a wonderful journey trough the stars for 1 min.", 
"Polymorphic Brew – Commonly used in drinking games, this brew will turn the user into an animal when they burp. They turn back about a minute later.", 
"Insom’s Ale – has same effects as a long rest, calming.", 
"Lilphina’s Lusty Lover Liquid Liquor – The bottle comes in two parts, with each part having a different hue of color depending on the flavor. When two persons consume the drink within 5 minutes of one another, their minds are swapped for 1 hour.", 
"Piña Colossus – a rare colossal pineapple hollowed out and filled with rum, coconut cream, and pineapple juice. Usually a shared drink. The pineapple shrinks in size when the liquid is drank or spilled. It will also continue to expand and grow to colossal proportions the more liquid that is added.", 
"The Coup de Grace – At the end of the night, the bartop is wiped down with a rag, the contents are rung into a shot glass.", 
"Drippzt – The drops in the bottoms of emptied kegs mixed together and dyed black.Anyone who can drink a pint of it without vomiting doesn’ t have to pay.", 
"Firebreath Ale – If someone drinks it and then breathes into a flame, a 3 rd level Fireball is cast centered on the flame.", 
"Belching rum – After trunking this make a con save.On a failed save the effect takes place immediately.On a success you choose when to have the effect take place(After ten minutes the effect takes place no matter what.) Effect: You belch thunderously.Everyone in a 100 foot radius is defened for one round.", 
"The Titans brew – A regular tasting ale served in an enormous cup, and after drinking it the receiver grows a few inches.", 
"Paladin’ s Bane – sweet enough to tempt the righteous and you hardly taste the alcohol, but it’ ll give you a decent hangover and diabetes to boot.", 
"Goodberry Gin – if you drink enough of it, it works as a mild healing potion which may or may not compensate for the damage done to your liver or you falling down the stairs while drunk. 1d6 hp healing, 1d4 drunk damage.", 
"Hagraven Brandy – though it has a taste as ugly as its namegiver, the appearance of everyone around you will exponentially improve with every sip you take. - 3 on Charisma saving throws for 1 d6 hours.", 
"Will-o-the-Whiskey – whisky with minor hallucinatory effects, starts with a tiny tingling light in the corner of your eyes, ends with a shining orb of light dancing a few yards away from you, moving away as you try to catch it.", 
"Mandrake Mocha – a hot creamy beverage with a narcotic effect. Dulls the pain, leads you into a deep slumber.", 
"Madman’s Mead – downing a mug causes a fleeting bout of insanity, roll a d100 for effects of Short - Term Madness.", 
"Ochre Stout – a cheap drink so thick you can taste chunks in it. Best to swallow and not be curious.", 
"The Drunken Dwarf – a pint of dwarven stout with a teabag in it.", 
"For(local deity)’ s Sake – a local sake or rice wine, popular with priests.", 
"Ciderella – a sweet apple cider, considered 'a girls drink'. Even the toughest bloke will begin giggling like a little girl after a few drinks.", 
"Jalapálinka – a fruit brandy spiced with hot peppers.Burns the throat, downing a pitcher leads to steam escaping ears and nostrils.", 
"Ginger Ale – Wait, this doesn’t taste like ginger at all… An ale that turns your hair ginger, effect lasts for 1 d6 days.", 
"The Maiden – a quadrupel beer, served in a bottle with a donkey and a pretty girl on the label. Sweet but strong.", 
"Bock Bear – a bock beer that gives you +1Str and extra body hair for 1d6 hours.", 
"Polypilsener – turns you into a canary for 1d4 minutes. Drinking half a mug will turn you halfway into a canary.", 
"Our Thoughts and Prayers – a brandy that works as a reverse Detect Thoughts spell-surrounding people learn your surface thoughts, although you’ re unaware of it. Range increases with 2 ft each glass, though your thoughts don’t exactly get more coherent.", 
"Smirgnome – a vodka that fills your brain with the weirdest ideas, although the morning after you’ll likely have no memory of inventing a sunlight-storing clockwork pigeon to hunt vampires with.", 
"Abbathor’s Gold – a clear golden mead that does nothing to quench your thirst–instead, you crave more of it. Roll a Charisma saving throw (DC 10) after each glass-if you fail, you keep drinking. After 8 glasses you pass out for 1d10 hours.", 
"Coala – a Dwarven invention, this black bubbly drink tastes like grinded coal with sugar, but also makes you feel reinvigorated and less tired.", 
"Cinder – a spiced cider served hot.You can control non - magical flame that fits within a 1ft cube for 1d10 minutes.", 
"The Umber Hulk – a pint of whisky, brandy and tequila in equal measures. Good luck.", 
"Bottomless pint – the bartender pours beer into a ceramic mug. When the patron pulls the glass up to their mouths, they realize that the mug really doesn’ t have a bottom.The mug is empty, and the beer has been pour through the mug into a hole in the bar with a pitcher underneath.", 
"Copperhead – the bartender pours a beer, mixes in a shot of whiskey, and then a couple drop of snake venom from a vial. Normally drinkers will feel numb in their extremities. If a drinker fails their savingthrow, they will be paralyzed from the neck down for 1D20 minutes.", 
"Brazenbrew – Served in a special mug laced with bronze, the drinker is more apt to make outrageous claims of ability, but also gains the relevant luck to succeed while still under the influence.", 
"Yam’ s Choice – A delightful mead, high class, has a fair chance of being extremely addictive. Withdrawal is applying two effects from the long - term madness chart, and one from the short-term chart.", 
"Witchwood Absinthe – A potent spirit the color of a moss-covered tombstone. It has mild hallucinogenic properties, and local folklore holds you can hear the voices of those you’ ve lost if you drink enough.Not too much, though. You might join them.", 
"Salty Dog Ale – A dark, rich brew that reminds you of the sea. Plopping in the shell of a sea snail for good luck is customary, and adds a fitting salinity to the drink.", 
"Hymvaren’ s Luck – A bright, golden-colored beer named after a local drunk who woke up on the beach after a night of carousing with a chest full of pirate’ s treasure. He claims to have no memory of that night.", 
"Bourbon of Dwarfkind – makes the user start to grow a beard. If they can normally, you see accelerated growth.If they can’t, a few hairs will sprout on their chin.", 
"Old Mill Rye – tastes alright, has a strange aftertaste in the back of your throat of an old sock. It’ s cheap and gets you drink [Insert local diety’ s name] brew– Has characteristics that reminds you of said god. Gold for sun worship for example. Hint of cinnamon for a hot and fiery one. A hint of licorice root perhaps.", 
"Ochre Jelly Ale – Ale with safe-to-drink ochre jelly mixed in it.", 
"A Regular Glass Of Water – That’ s it. It’ s just a normal glass with regular, boring water inside.", 
"Mimic Drink – Usually sold by tricksters to play pranks on people. Looks like a regular glass of water, but a tiny water elemental / water weird is disguised as normal water.", 
"Liquid Nitrogen – Drank by frost giants and other beings that can tolerate extreme cold.", 
"Mead of invulnerability – Once drunk user makes a DC 15 Wisdom check. On a fail believes they are immune to all damage and if damage is dealt to them believe they did not take the damage. Effects for ten minutes. User still take all damage as normal.", 
"Inverted rum – when you drink it, every one around you in a 15 foot cube becomes drunk. This dose not include yourself.", 
"Goblin Spit – whiskey and gin mixed with the barkeep’s home-made mints. It tastes surprisingly good despite its name. As is tavern tradition, a long-distance spitting competition occurs after every round.", 
"The Hook and Slider – a cooked goat(?) intestine tied and filled with a heavy beer. After finishing the beer chow on the intensive.", 
"Lucky Leprechaun – A sickly green drink that gives you advantage on Charisma checks for one hour.", 
"The Tiamat – 5 different shots, one for each color of the different heads. One is black and syrupy, one blue and gives tingly feeling, one is on fire, one is green and tastes a bit minty, the last is white and frosts the closest things. They are mixed together and separate in the cup making a very nice presentation.", 
"The Sweet Roll – flavors of cinnamon and sugar blend with the strong scent of rum. The drinker gains an additional 1d4 to any pickpocket attempts for the next hour.", 
"The Sailor’s Spirit – There once was a cap’ and a crew, Who made the most wonderful brew, From rations of lime, They would in their spare time, Make fine drinks no man could outdo.", 
"Good Hearth’s Brew – A hot spiced rum which is popular during long winter nightsfor the immediate feeling of warmth and calm that follows.", 
"Tarnation – A strong spiced cider served warm and traditionally drank as quickly as posible after a boisterous cheer or a lewd drinking song. Enchantmented with the effect of the consumer belching a small flame right after ingesting.", 
"Gnome Rum – Makes your voice high, squeaky, and annoying.", 
"Ethereal Ale – The more intoxicated you get, the more you fade into the ethereal plane. First you become slightly transparent, than objects start to phase through you from tame to time and if you manage to keep drinking you entirely enter the ethereal plane.",
]
let teaSpecialty = [
"Stranger's Heart - Made from leaves of the Succubus Kiss, a parasitic red vine with lip shaped leaves that wraps around young trees, this bitter tea makes you feel in love for a few minutes but with no one in particular. Can be addictive for some people.", 
"Mountain Fire - Made from Scorched Berries that grown at the base of some volcanoes. The berries are poisonous but once boiled and then dried they can be turned into a spicy drink that fills you with warmth and releases tensions in the body. Drinking more then one cup might make you sweat profusely.", 
"Morning Sun - Made traditionally from a mix of orange peels and Croissant Lotus petals by monks of the Zenchu River, this bittersweet infusion helps with morning grogginess and giving a productive an early start. Also helps to resist sleep spells.", 
"Gundyr's Ice Breaker - A bestseller during flu season, this algae based infusion has a strong salty taste but will clear your airways in minutes. Despite it's usefulness, only few people would risk collecting the Ice Grappler Algea that grow under the ice of frozen lakes. Gundyr is on of them.", 
"Sharp Moonlight - A tea made from the petals of a flower (from a cactus) that blooms only under the moonlight. The leaves must be harvested and processed before the morning, when the petals will, if left to their own, have all wilted. In small amount, Sharp Moonlight helps people sleep, but larger doses can produce hallucinogenic dreams. Many report feeling as if they were one with the moon themselves.", 
"Khârt (pronounced Curt with a hard c) - A dwarven tea made from the Khyr fungus, which only grows deep underground and physically resembles the black truffle. The tea possesses a bitter, spicy, and pungent aroma and is a potent stimulant, with its precise effects varying depending on method of preparation and the precise provenance of the khyr. The most commonly found type has the khyr being finely minced, dried, and pressed into bricks for easier storage and transport. This tea instills alertness and creativity with a slight sense of euphoria, making it a prized commodity amongst wizards, philosophers, and courtiers in many lands (albeit most prefer to add other things to mask the taste), and a major dwarven trade good.", 
"Forge-Fire - Whilst Khârt is a common beverage with not very much cultural significance to the dwarves, forge-fire is a brew steeped in ceremony, and it is only consumed by dwarven masters of a craft before undertaking a great endeavor, whether it be a warrior leading a charge against an enemy army, a runeworker making a gate impervious to ram or explosive, or a smith forging the armor of a king. The khyr used in forge-fire is of the highest quality, and the most prized for forge-fire is khyr found growing upon the graves of a dwarf's ancestors or prior masters of the art, as the dwarves believe those specific fungi are gifts from the ancestors and hold some of their skill. Forge-fire is prepared by the drinker in a ritual that takes around 6 hours, during which the dwarf meditates on their ancestors, their training and knowledge, and the magnitude of the task ahead. The tea itself is prepared rather strangely: the khyr is finely sliced and placed into a wide and shallow bowl (often an ornate heirloom) and over it is poured strong mushroom brandy. The mixture is set alight and the heat from the burning, along with the tincturing from the alcohol, produce the infusion. A final incantation is sung and the brew is drunk whilst it is still burning. The brew fills the user with single-minded focus and vigor, making their movements swift, sure, and tireless, with many under its effects being known to work without stopping for days or even weeks. However, the aftereffects are extremely unpleasant, almost as if their life energy itself has burned up, and often leave the dwarf bedridden for months, and those who have consumed it claim to have felt that they utterly lost themselves in the chorus of ancestors and the purity of the craft, . In all dwarven history, few have consumed the forge's flame thrice, and none have survived it.", 
"Corpses Caffeine - Made from the petals of a corpse flower. When crushed they can be turned into an orange paste that can be infused in hot water to make a bitter but smooth tea. This tea makes you more aware of dead organisms near you.", 
"Nature’s wake - Made from an old ritual flower used by Druid’s to talk to nature. The petals of this flower are a bright and luminous white but, when dropped in boiling water, the liquid turns black with patches of green. Stir for 10 minutes and drink in one sip is the recommended brewing and drinking time. If brewed and drank correctly, nature will keep you safe for 24 hours. Examples of this would be nature guiding you out of a forest, trees protecting you like a shield.", 
"Leafwalker's Sensation - Crushed and dried leaves and sprigs from a Dryad's very own branches. The taste isn't different from other green teas, but it's magical warmth will flood inside your throat and belly. If the ingredients were gifted from a dryad, this tea will nourish and soothe to your inner core -mind, body and soul- and awakens your connection to the Fey for a short while. Just don't drink any that was harvested from a dead or unwilling Dryad...", 
"Dragon’s Balm - Sometimes chewed, this spiky leaf is known to any wood-witch or hermit worth their salt - a common sight among roadside plants and overgrown gardens. When brewed the leaf gives off a strong smoky aroma - drinking it makes your breath smell slightly of woodsmoke and brimstone. The short term effects are as a mild stimulant - a particularly potent brew might help someone work tirelessly for several hours or walk twice as far in a day. Those under its effects seem artificially chipper and may talk more than they mean to. The aftereffects are marked; a mild and not unpleasant lethargy usually followed by a deep and untroubled sleep. Valued by travelers and those living in peaceful locales for its use in travel and ease in ensuring a full night’s rest, the wise avoid its use when danger looms or work must continue at great length - the sleep of Dragon's Balm is difficult to rouse from and the lethargy lasts until the body is allowed to completely rest. Repeated use runs the risk of dependence, and the tea will begin staining the teeth orange over time.", 
"Ghostflower Tea - Used by mediums and those who wish to commune with the dead - this tea must be prepared in a special ritual lasting an hour. The ritual involves selecting the proper leaves and bulbs from this unassuming but rare white-gold flower and painstakingly removing the tiny black pods that spread from the flower’s open bell. Each pod must be shucked and its contents ground, but when the tea is finally imbibed the user can interact with and speak to the dead. The imbiber will be wreathed in a soft glow for the duration, and appear translucent under moonlight. Given a strong enough dose, they will be able to pass through flimsier solid objects - this effect is rare and taking too much Ghostflower tea is dangerous. The dead become attracted to those who drink this tea; an unlucky medium may drink to speak to a lost loved one or question a murder victim or ancient lord only to find themselves the focus of every unquiet dead or revenant for miles around. Drinking poorly prepared tea or drinking two doses in a single changing of the moon (a month) can give the imbiber intense visual hallucinations and make them violently ill; they have been known to speak at length to visions of their dead loved ones or ancestors and carry out battles against imaginary foes. The skin of a victim of Ghostflower poisoning will be pale and flushed; the blood will not clot and they bleed freely. Those with weak constitutions may perish. Individuals who die while under the effects of ghost flower tea are more likely to become spirits themselves.", 
"Moon Tea - Brewed by witches, midwives, queens and bachelors - this tea is from an uncommon leafy plant of green-grey leaves. Bitter smelling but sweet on the tongue, having two cups of this at most an hour before coitus will prevent pregnancy. Some claim it heightens sensation and others that it ages the body, but when taken by any sex its efficacy is renowned. Babies born from unions where one or both parent take this tea are considered lucky by many, and the child of such a union is often marked by green flecks in their eyes. This plant is harvested so regularly that what was once a common sight in every garden and back patio has become a valuable commodity; this is because improper harvesting yields sufficient quantities for a dose while killing this fragile plant.", 
"Willwillown - a common long leaf tea that grows on hillsides and is hardy. Usually drunk as a before midday tea but has several flavored varieties by mixing it with florals like Rill or Munlack or Pepper Flower, or with citrus peels. Gnomes like it baked rather than air dried as it rounds out the body, but they also brew it strong and tanneny which others find unpleasant. Dwarves will sometimes chew Willwillown berries but humans find them bitter and unpalatable.", 
"Moradin's Loose Leaf - Made from the leaves of Ironwood and a proprietary blend of black tea leaves steeped in a forge's quenching bucket. Gives the drinker renewed vigor to continue hammering, bending and cutting long past many of the younger dwarves.", 
"Avlat - Made from leaves of a vine that grows wild in poor soil. Brews a peppery, copper-colored tea that is a bit of an acquired taste, but often is used to accentuate other bold flavors, such as those found in rich wines, sauces, and ales.", 
"Beorunna's Cure-All Named, oddly enough, for a legendary barbarian queen credited with its discovery, this bitter-tasting tea made from boiled stems located in the Savage Frontier has taken on an austere reputation among healers and herbalists. The first time a creature that consumes this tea regains hit points from any source in the following hour, they regain 2d4 additional hit points.", 
"Blackthorn - Brewed from the leaves of the blackthorn shrub, producing a savory tea with earthy woody notes, and a fruity, tangy aftertaste. This tea is known to calm an upset stomach, and is remarkably common in the Dragon Coast and Dragon Reach.", 
"Blueleaf - Harvested from the leaves of the bitterhedge plant, plentiful throughout the Realms and used to ward off common crop parasites. When brewed, creates an off-blue tea that is slightly sweet with an almost minty aftertaste. Many enjoy this tea recreationally, though used medicinally it suppresses nausea and dysentery for 8 hours after consumption.", 
"Chalthorn - Made from grey, furry weeds that plague farmers in Sembia and the Dalelands, this cloudy tea has a dry, chalky taste that is difficult to like. However, when a creature drinks this tea, it becomes unable to taste spice in food for one hour, rendering the most spicy of cuisine palatable.", 
"Coffee - A potent drink with a bold, robust yet bitter flavor, energizing to those that drink it. A creature cannot sleep or be put to sleep by any means for an hour after drinking coffee.", 
"Coffee, Dwarvish - A thick, sluggish liquid, almost syrupy in texture and black as midnight. It is doubtful if any actual coffee beans are involved. For 8 hours after drinking dwarvish coffee, a creature cannot sleep or be put to sleep by any means.", 
"Earth Dragon's Eye - A rich black tea from Shou Lung in Kara-Tur, slightly acerbic, with a complex earthy aroma. Drinking this tea refreshes you and loosens your muscles, increasing your land movement speed by 5 feet for the next hour.", 
"Elkammat - Brewed from groundnut husks found in Murghôm, Semphar, Mulhorand, Unther, and Chondath, this brown tea has a woody, bitter, and slightly nutty flavor. Typically served spiced with cinnamon, nutmeg, or more esoteric spices, this tea warms the heart and engenders positive feelings in those who drink it. The drink of choice for the entire eastern Inner Sea.", 
"Feverbalm - This tea is brewed from small multi-colored red, black, and yellow flowers found in the Savage Frontier. Drinking this tea calms the mind and numbs the throat and tongue, suppressing any madness effects the character suffers for one hour.", 
"Gaeth'ad - A tea brewed by the orcs of the Shadow Marches, tasting thick and brackish, with a flavor that stays on the tongue. A versatile if incredibly pungent drink, it can be  brewed as a mild stimulant, depressant, or hallucinogenic, depending on methods used when brewing.", 
"Jethur - Purplish and (usually) as savory as broth, this tea is made from dense clusters of fungi known as carpet mushrooms. The taste of this tea is known to shift as one drinks it, and it is renowned by merchants for its ability to induce sobriety and soothe digestion. A creature that drinks this tea suppresses the effects of any alcohol in their system for 2 hours.", 
"Long Jing - A rich and fragrant green tea, grown in Kara-Tur’s Zhejiang province. Tradition holds that this tea can help cleanse the body of toxins, granting a creature that drinks it resistance to poison damage for one hour after consumption.", 
"Mallow - This light blue floral tea is popular in Maztica, often finding use as a sleep aid. It carries a light semi-sweet taste. If a creature drinks this tea before sleeping, they sleep free of nightmares and cannot be affected by the dream spell or similar abilities.",
"Meiriath - A rich copper-colored beverage tasting of mango and citrus, popular with wealthy residents of Halruaa, Unther, and Mulhorand. Made from carefully-dried leaves of cave-sedge, a grass-like plant that grows in caves and other dark places.", 
"Mother's Leaf - A mellowing concoction, carrying with it strong grass and sage notes, a staple of healers in the Savage Frontier. If a creature that drinks this tea suffers from any diseases, they can make a Constitution saving throw with a DC of 13. On a success, one disease the creature suffers ends gradually after 24 hours. A creature can only attempt this saving throw once, requiring a long rest before attempting it again.", 
"Mourningberry - Traditionally found near graves and other deathly places, the leaves and flowers of this plant can be seeped into a tea, but its berries are mildly toxic. When brewed, the tea acts as a slight depressant, relaxing those that drink it and making them disinterested in conflict or confrontation. Often served ceremonially at funerals.", 
"Nararoot - A shaved-down tuber seeped into a tea, its natural licorice flavor is softened into a musky semi-sweet aroma. This tea functions as a form of birth control; a female humanoid that drinks this tea is rendered infertile for a period of 2 weeks. A similar tea for male humanoids is derived from cassil, though that tea costs 10 gp for every 1/20 lb.",
"Pale Jade - A light and airy white tea, cultivated in Kara-Tur, primarily within Shou Lung. A popular export, many merchants and tea connoisseurs hold this tea as an excellent introduction to proper tea drinking.", 
"Par-Salian's Blend - A smoky, citrus-rich blend of herbs that soothes the throat, passed down between the magi of Krynn. If a creature drinks this tea, it suppresses any conditions that cause a hacking cough for 24 hours.", 
"Sandberry - These yellow berries grow in the Western Heartlands, proliferating in otherwise barren and ravaged areas. Tea brewed from these berries is yellow in color and has a harsh, bitter, and acidic taste, but nevertheless is favored by travelers as an excellent source of hydration in arid lands.", 
"Talkuth - Made from groundleaf, a hardy plant that is one of the few things which can survive the bitter cold of the North. This tea is slate grey with a metallic tang, and is generally considered unpalatable to those not used to consuming it.", 
"Tal, blackroot - Brewed by the halflings of Khorvaire’s Talenta Plains, this beverage is served piping hot and carries a taste of bitter cinnamon. Served traditionally around mid-day, many add a healthy dollop of honey to round out the flavor.", 
"Tal, milian - This chilled purple tea is also brewed by halflings of the Talenta Plains, and has a complex flavor akin to licorice or anise.", 
"Three Ashes - A bitter tea served stone cold, brewed by the Dustmen of Sigil. Drinking it is said to clear the mind, and dampen emotions. If a creature that is charmed drinks this tea, that condition is suppressed for one hour.", 
"Vauge - Made from the voj-weed that grows wild near Khôltar, this mellow grassy tea has a slight salt aftertaste.", 
"Wild Ginger -Brewed from ginger root and a few choice additives, this tea comes in a wide variety of colors, depending on which type of ginger is used. Popular for its use in settling the stomach, and its warm, slightly spicy taste.", 
"Yellowleaf - Concocted from the undried, sword-shaped leaves of the idaya weed, this tea is remarkably common throughout the Shining South. It has a robust and dependable taste, and a pale yellow coloration. Though traditionally served hot, cold yellowleaf tea can be used to remove most stains from clothing and other textiles.",
]
let chance = Math.floor(Math.random() * 100);
if (chance < 40) {

return "Non-Alcoholic Drink: " + searchArray(teaSpecialty)
} else if (chance < 90) {
return "Specialty Alcohol: " + searchArray(drinkSpecialty)
} else {
return "The barkeep hails you and says 'This here’s a milk only tavern, including all milk derivatives.'";
}
}
findSpDrink();
document.getElementById("Drink").innerHTML = findSpDrink();
};
function foodFind() {
function findFood() {
let foodEvent = [
"One of the local hunters haulded in a big buck, so we’re having venison stew.", 
"Darkmantle soufflé, with hollandaise sauce and a fried egg on top.", 
"Griffin shanks, with secret sauce BBQ.", 
"Pseudodragon on a stick.", 
"Rack of owlbear ribs.", 
"Caramel fritters, with healing potion baked in.", 
"Blubber Baked Barnacles, local delicacy.", 
"Bobo’s JoJos (BoBo is a half-orc bartender and cook, JoJos are essentially seasoned and fried potato wedges).", 
"Stag Steak & Dire Lobster (Surf and Turf).", 
"Illithid Larva in Squid Ink, eat it before it eats you!", 
"Ice cream. Cooled by a business savvy winter wolf who is partners with the tavern’s ex adventurer owner.", 
"Catch ya own fish and chips.- there’s an interdimensional hole in the tavern’s floor that leads to the elemental plane of water. We cook anything you catch and provide the chips but you have to supply your own rod.", 
"Bread pudding with extra sharp dire goat cheese. Comes with a side of grilled onions and carrots.", 
"Squeaver chili served with a cool glass of Beholstein milk. 'The Squeaver is a many-tentacled furry beast with large buck teeth that spends its days constructing fabulous dams. The Beholstein is truly a special prize of dairy farms across the realm, as its back half is separated from the useful bits, so fertilizer can go directly where it needs to.'", 
"Spicy Jumbalaya with crispy eel skin strips on top.", 
"Celebratory Goat Stew with assorted fruits, nuts, and cheeses.", 
"Potatoes! Potatoes of all sizes. Grab a giant potato bowl for potato soup with a side of roasted potatoes.", 
"Goat and Quail Egg Omelette, served with lingonberrys.", 
"Marinated Artichokes seasoned with caper and chicory, and served on a bed of Wild Mushroom Rice.", 
"Sauteed Partridge in a black raspberry reduction sauce, comes with a side of Grilled Jalapeños.", 
"Roasted tarantula with hairs carefully singed off and fangs used as toothpicks.",
"Roasted hazelnuts and fresh apples with a strip of bear jerky and a wedge of ripe cheese.", 
"Kumquat Curd Pancakes, served with a Tankard of Yarrow Beer.", 
"Tom passed last week, and he had a weird will. So we’re having Tom Roast.", 
"You lot must’ve seen that giant pile of crates out front. SOMEBODY (yelling toward the back) accidentally order 10000 ears of corn instead of our usual 100. So, we’re running specials on corn, cornmeal, cornbread, creamcorn, and other corn dishes.", 
"Hell fire peppers: popular among teiflings as they can handle the intense spiciness of them. Warning: extremely spicy.", 
"Sweet, sweet hell: Roasted with onions and slathered with honey. Goes great with any meat.", 
"Dragon’s eggs: eggs cooked with thin slices of beef and a little bit of cayenne. Salt and pepper according to taste. Served in a bowl with dragons on it for pa-zaz!", 
"A traveling gnome has a new fruit called ‘Impression Berries’. Eating it changes your voice to sound like someone else in the room. The flavor is based on your feelings towards that person (ex: if you like them, the berries are sweet. Dislike, bitter. Attracted to, spicy).", 
"Four beautiful sisters were left one piece of their grandmother’s special beef stew recipe (who passed away a week ago). They all are too jealous to share their parts of the recipe so the party must decide with faux recipe is the best.", 
"A man is taking his son out hunting for his first time. They’re going to cook what they catch. They are accidently attack by an owlbear. The party must save them, then enjoy owlbear venison.", 
"Oyster eating contest! ('Those were mind flayer eggs? Uhh…I don’t feel so good.')",
"A portal to the elemental plane of fire has opened! In small backwater town. The local rednecks have been using it as a pit to cook beef.", 
"It’s the cook’s birthday and has the day off. All we can manage today is day old bread with a stew made from yesterday’s leftover roast.", 
"Chicken minced pies. They’re the [king/queen/emperor/governor/ruler]’s favorite.", 
"Meatloaf. Guess the meat and the meal is free!", 
"The town farms have been ransacked by kobolds, but can I get you some dirt soup?", 
"The party just killed a red dragon and freed a town from it’s tyranny. The cook wants to try his hand at dragon prairie oysters for the community.", 
"A kraken has been killed. The local tavern host a calamari eating contest, with the villager who eats the most getting accolades and free ale for a season.", 
"Thinly sliced fruit slices covered in hardened sugar and topped with honey. DC 10 Con Save or +1 initiative -1 to all checks regarding stillness", 
"A slightly burnt steak filled with a juice from the tavernkeep, it tastes great but a bloodcurdling yell came from the back when he was preparing it, a human yell.", 
"Pastry-wrapped Goat on a bed of Battered Fried Green Beans, served with doughnuts, lingonberrys, and scrambled quail eggs.", 
"Marinated Artichokes seasoned with caper and chicory with Sauteed Spinach, served with Frybread with pumpkin butter.", 
"Fried potatoes and lamb on a bed of fireroot leaves, covered in a spicy smolderberry sauce. Smolderberries are rarely used in food due to their ashy taste and uncommon growing conditions, but the tavern owner found a way to get ahold of them many years back, and has since taken the time to figure out how to make their smoky flavor shine.", 
"A juicy shark steak steeped in whisperwood sap, seasoned with the tavern owner’s signature spice. The shark had been a monster of a beast that nearly sunk the ship that caught it, and it’s robust flavor mixes surprisingly well with the overpoweringly sweet sap. The signature spice is literally just wood shavings from the kitchen counter.", 
"A local fishing boat has discovered that, in lieu of actually catching fish, eating seaweed is surprisingly nourishing and tastes… just okay.",
"Nettle Soup.", 
"Rabbit in a wine-currant sauce.", 
"Orange omelettes for harlots and ruffians.", 
"Cave Fisher Tail with Cave Fisher bloodwine. (Cave Fisher is a weird cave lobster with alcoholic blood.)", 
"Sweet and Sour Cockatrice with rock candy and rice in a stone bowl.", 
"Bulette fin soup.", 
"Roast velociraptor.", 
"Chimera Steak. It’s nature’s turducken!", 
"Deep fried rust monster.", 
"Water with ice.", 
"Merchants from a foreign land selling foreign foods have recently passed by. Spicy shrimp and rice. Make a con save against psychic damage from spiciness.", 
"Fish eggs. Who eats fish eggs? Why did the 'Black Salmon' crash nearby carrying loads of fish eggs? Why would anyone pay for nasty, slimy, fish eggs? Free.", 
"Mutton chops with 'mutton chops' facial hair seared into it.", 
"Leftover Kebab. Roll two specials. Put them on a stick.", 
"Drake steak.", 
"Deep fried Drake tail (I like the idea of roaming pacts of drakes to drive home the fantasy aspect compared to our world).", 
"Giant Centipede or other insect stew, serve in a shell bowl.", 
"It’s the cook’s night off. The meal of the day is beer. Lots of it.", 
"Wild boar sausages with berry gravy.", 
"It’s just chicken. I mean, what kind of strange kin y’think we are?", 
"A band of adventurers came running in begging us to take this heap of 'cursed meat' off their hands, even threw a few handfuls of gold into a sack to get us to take it… So we’re having Mystery Meat for the next night or two.", 
"Had a strange merchant come through with a machine he claimed would make us so much food it would 'Rain from the sky'. Meatballs, potato mash, and a strange beverage the traveler called 'Cola' will be served here at dirt prices for a while.", 
"The cauldron the size of the table is dropped in the table with no description. It is filled with 3 live octopus, which will be perfectly cooked, after the party kills it themselves, of course.", 
"Whiskey stew with rye bread.", 
"Pickled purple worm that has been marinating in honey wine and various regional spices.", 
"The town has received a mysterious shipment of rations that the mayor is insisting must be sold to the general public.", 
"Mushroom Stroganoff: On the menu it seems normal, but the dish has a purple tinge to it when it arrives at the table. Turns out, it’s actually a violet fungus that got into the pantry!", 
"Traditional English Breakfast; Sausage, Eggs, Tomatoes, and black pudding… While most of the meal is delicious, the blood used for the black pudding makes your mouth tingle with energy–did they use some sort of magical creature to make it?", 
"Our local brewer has been 'experimenting' recently. And by experimenting I mean trying to make alcohol out of every fruit they can get their hand on. If you’ve never tried watermelon wine, now’s your chance.", 
"500 year aged Owlbear cheese, served with Ancient Dwarven Wine. Bartender says that of you can eat an ounce of each and keep it down, you’ll get free bed, meal, and drink the rest of your life in the tavern.", 
"Toad-in-the-hole (real dish in uk – sausages in a large Yorkshire pudding) but there are regional differences in the kingdom. Some use sausages and some use real toads. People are fierce and proud of the camp they fall into. Which is prevalent in this village? Is it insulting to ask then not chose the dish?",
"A section of giant spider leg that’s been been battered and prepared with an accompanying sourweed soup to dip it in. When a frequent taverngoer came across a nest of giant spiders and eradicated it with fire, he offered the owner the corpses. The owner experimented and finally came to realize that, while the abdomen was far too gamy, not to mention poisonous, the legs had a taste and texture similar to crab.", 
"A platter of assorted fruits served drenched in Caldian oil. Caldian oil is exceptionally rare in those parts due to the fact that doesn’t grow on the continent, and the tavernowner only has some due to his recent assistance on a traveling merchant’s vessel. The uniquely tart taste and tingling sensation provided by the oil is coveted for its ability to give layers of flavor to even the blandest of fare. Do not touch your eyes after getting any on your fingers.", 
"It’s Trial and Error Night! Every once in a while, the tavernowner takes a shot at expanding their menu and makes a variety of dishes that aren’t normally an option. Roll on the list 3 more times. Over the course of the day, the tavernowner makes the food from each of those options. At the end of the day, the owner serves all of the food at the same time, both independently and in combinations with the other options to see whether any of the experimental fare is worth adding as a regular option.", 
"Boar meat cooked in a broth composed of various sour berries and spices.", 
"The tavern is offering a 'special sauce' that can be added to existing dishes. A successful intelligence check will reveal it to be a dead gray ooze.", 
"Oat porridge …again.",
"A small, man-made island in the middle of the ocean has a tavern that always serves a veal special. There are no cows anywhere near the island.", 
"Oysters Tiamat", 
"Sing-for-your-supper: order whatever you want and if you sing a song that charms the bartender (dc12) your meal is on the house. (Players are encouraged to sing)", 
"Minotaur patties", 
"The new half-orc chef is preparing what he calls 'Woodman steaks' (It’s Elf). It is similar to pork but lean and with a mysterious, herbal flavor. The chef may approach the right party to 'procure other rare meats'.", 
"Kobold scale chips with salsa.", 
"Beer. Just drink some of the beer, its going bad.", 
"A raptor is brought in from the south. Raptor is expensive. The people being poor, and the travelers being stingy, no one wants to buy it. So there’s a contest. If the entire raptor can be eaten in an hour and a half the meal, and all alcohol along with it, is free. Otherwise you pay full price.", 
"Giant crayfish tail sauteed in butter with Abyssal peppers and a side of thinly-sliced shrieker steaks.", 
"Stewed mule flanks with boiled carrots and parsnips.", 
"Boar bone soup: A brown coloured liquid with bits of meat that smells bad but tastes great.", 
"A small locally caught fish that was de-scalled and dipped in egg then coated in flour. Then dunked in boiling oil and cooked till a golden crispiness.", 
"Poached Trout and Walnut Bread with a Glass of Brandy to wash it down.", 
"Baked Bear and Mulberry Tart.", 
"Salted Catfish, caught locally.", 
"Boiled Sausage and Sharp Cheese. The cheese was made locally, and considered to be a delicacy.", 
"Fried fish. The fish turns out to be a wizard who is unable to polymorph back into his human self.",
]
let bakedGoods = [
"Sourdough rolls glistening with freshly applied butter and a garnish of parsley.", 
"Braids filled with minced and roasted fruits. Apple filled braids are particular popular in this season", 
"Pumpernickel rye baked into rounded loafs that are adorned with caraway seeds.", 
"French-style plain complete with a golden brown egg-wash.", 
"Dragon donuts are twists in the shape of a dragon’s horn with a thin sugar glaze and a surprisingly spicy kick.", 
"Chocolate zucchini cakes coated in powder sugar and crowned with strawberries.", 
"A pound cake coated in a sugary lemon drizzle.", 
"Meat pies, stuffed with various local game, give off wisps of steam and heavy aromas.", 
"Barkskin biscuits have a tough, almost woody, exterior that are often soaked in milk or tea to soften.", 
"Black ooze bread pudding is an acrid smelling, albeit surprisingly sweet, bread pudding that tastes of cinnamon licorice.", 
"Gelatinous cube flan, despite not being made from the creature, is a recipe of Calisham original that is traditionally made in square baking pan. The addition of gelatin helps the dish hold its signature shape.", 
"Dwarven ale bread is a very dense but flavorful bread made from ales and stouts (generally of dwarven make). Despite being baked, the potency of the drinks used in its making can still provide the eater a slight buzz when consumed. Often used as a desert in many northern kingdoms and tribes.", 
"Jötnbrød (YERT-n-breh), a massive boule of dark rye bread enriched with bone meal, resulting in a beefy, slightly crunchy bread. A large handful is equivalent to a trail ration, but produces horrid constipation.", 
"Sawyers flat, a horrid, matzo-like crisp-bread cut with maple (best), birch (ehhh), or pine (oh gods) sawdust. Often eaten by unskilled laborers, or during famine/drought.", 
"A frangipane style baked custard that uses a flour made from exotic, far away seeds.", 
"Raisin dotted pastries of choux rolled into spirals and heavily glazed. Topped with pistachios.",
"Tartines made with spicy sausage and blistered tomatoes.", 
"Assorted Bagels (asiago, whole wheat, multigrain, blueberry, cherry, goodberry, etc.) are stacked on a nearby platter.", 
"Buttered Crumpet, best served warm to ensure that the butter soaks into the soft and spongy crust.", 
"Cheese Cake, a simple creamy filling of egg, sugar, and cheese within a fluffy pastry crust. Some variants have a coating of fruit jam on its top for added flavor.", 
"Carrot Cake, a moist layered cake covered in a thick layer of freshly made cream cheese frosting.", 
"Fresh cornbread & butter served with a side of honey, maple syrup, and/or fruit jam/jelly.", 
"Fruit Dumplings (apple, blackberry, blueberry, elderberry, strawberry, etc) that have been boiled or fried and coated in a mixture of sugar and cinnamon.", 
"Fruit Pies (apple, blackberry, blueberry, elderberry, strawberry, etc) adorns with ornate patterns in to top crust.", 
"Meat Dumplings, dumplings filled with various meats. Some enterprising creators crimp them to resemble a fat large lizard or dragon.", 
"Muffins of various flavors—apple, apple banana, banana nut, blueberry, etc.—, are heaped in a basket on a nearby table. Some are topped with powdered brown sugar, powdered sugar, and/or sesame, poppy, or pumpkin seeds.", 
"Pumpkin pie, a creamy orange desert that is best served with a dollop of freshly whipped cream.", 
"Sweet Potato Pie is a staple of many households during holiday celebrations. Often topped with a powdering or hardened glaze of brown sugar.", 
"Fried funnel cake with sprinkled confectioners’ sugar.", 
"Bowlcaps are a type of round, dense bread rolls made to be crusty on one side but soft and steamed on the other. Typically eaten by laborers, the soft side is usually pressed down over the rim of a wooden bowl to act as a lid, containing and preserving the contents, until mealtime.", 
"Flower bread is made from various types of powdered flowers giving it light floral taste and aroma.", 
"Honey bread, bread but with honey.", 
"The Wrong Bread, or the ‘you weren’t supposed to buy THAT one.’, is a half-stale loaf of bread containing a plot hook baked into it. This item could be a small magical trinket with a larger meaning, such as a ring, a wand, a small piece of a very powerful spell-scroll, or something more mundane but equally powerful. For example, the item could be a signet-ring or seal of a noble or royal (maybe it’s a high-end fake, maybe it’s the real-deal that was recently stolen), or perhaps just a small bag of very valuable gems. No matter what it actually is, you have it now, and boy are there people who are going to try to make you regret it.", 
"Small chocolate bars that were prepared using healing potions. When you don’t have a druid and want goodberry.", 
"Goodberry Pie, made with the eponymous berries, grants 5hp when consumed, but must be eaten within a day.", 
"Gelatinous Pudding – a very, very sticky treat.", 
"Spider bread that was baked by drow. Don’t ask. Seriously.", 
"Miner’s pasties, are made with meat and potatoes in one end, jam in the other, and a thick crust ‘handle’ on one side that is designed to be grabbed with coal-black hands and thrown away after.", 
"Tiny dense black rye rolls that are studded with cloves.", 
"Fist-sized cups of hard bread, filled with cold pease pudding.", 
"Crates of ship’s biscuit, barely edible but capable of lasting years at sea.", 
"Small boxes of traveler’s biscuit – similar, but more palatable due to the addition of lard and salt, and with a shelf life of only a year.", 
"Monkey’s tail is a coil of thin pretzel-like bread that is boiled in soda ash, topped with salt and pepper, and then baked.", 
"Piles of pale-yellow buttery shortbread that are imprinted with various coats of arms.", 
"Roll and stew is a wooden bowl containing some thin stock (fish, goat, squirrel, etc) and a bread roll to dip in it.", 
"Small balls of fried bread that are soaked in pistachio-flavored syrup.", 
"Mutton-bread, a double-fist-sized roll of steamed bread, that is filled with minced mutton spiced with plenty of pepper. The mutton is cooked inside the bread, so its juices leak out when bitten into.", 
"Small rhubarb pies, made with thin crunchy hot-water pastry.", 
"Red rolls are bread made with pig’s blood instead of water, and stuffed with boiled pig stomach or intestine. Very nourishing, if a bit smelly.", 
"Golden pear bread, shiny and egg enriched, contains a generous filling of wine-stewed pears, cinnamon, and brown sugar.", 
"‘Peasant’s breakfast’, a barely-leavened flatbread that is split and stuffed with curried chickpeas and a chopped boiled egg.", 
"‘Penny treat’, a finger-sized roll of brown bread drizzled with blackstrap molasses or watered-down maple syrup.", 
"‘Tuppenny treat’, like a Penny treat, but topped with a sliver of dry cheese.", 
"Fragrant caraway seed buns display a golden brown top glistening with butter.", 
"Salt-roll are small round rolls of chewy brown bread, topped with a truly alarming amount of flaky sea salt.", 
"Nut breads, sweet or savory, baked with whatever nuts are locally grown.", 
"Puffed pastries cooked in meat drippings (think Yorkshire puddings).", 
"Mushroom breads, sometimes with unexpected medicinal or recreational properties.", 
"Tiny frosted cakes full of spices, nuts, or fruits.", 
"Towering bread creations formed in the shapes of fantastical beasts, castles, or scenes, usually for festivals or special occasions.",
"Bacon, sharp cheese, green onion, and hot pepper scones.", 
"Chicken Bread, it’s got the chicken baked in! So it’s great for those on the go. Developed by humans, of course.", 
"Almond croissants are flaky croissants sliced in half and filled with dark chocolate spread.", 
"Siren’s Tack, a dry and dense bread, that is as hard as a brick. When eaten alone, this hardtack is basically a rock that sits in your gut. They are surprisingly filling, but a bit hard to keep down. It’s traditional to boil them in broth (to soften and flavor it) and serve under fish and gravy in port towns.", 
"Plump-Helm Roast is a unique pie, filled to the brim with minced and liquefied Plump-Helmet mushrooms. The subterranean fungus is rather sweet (which allows it to be brewed into alcohol, among other things), which makes the pie a rather addictive mix of sweet and savory. Often served with Plump-Helmet Wine and fine dwarven cheeses.", 
"Lifeleaf Wafer are small disks of flour, water, salt and finely chopped lifeleaf that are baked till hard. Naturally restorative, unnaturally salty.", 
"Vagrant’s Cake, a recipe passed down from Druid to Druid; barley flour, berries, sugar, eggs, goat butter and water, mixed finely and baked until golden. The cakes are sweet and nutritious, perfect for short, day-long journeys.", 
"Illithid Brain Pies appears like a common pie, with an uncommon filling. Whether the brains are from or for the Illithid is up to the skill of the adventurer wanting to bake this dish.", 
"Seawater bread is a notable staple of coastal markets and bakeries.", 
"Dwarvish baguette are short and stout like its namesake.", 
"Gnomish sourdough made from 4000 year old yeast culture.",
"Phallic-shaped doces fálicos frosted sweet bread.", 
"Twice baked travelers bread provide of tough but crisp foodstuff that is perfect for trail rations.", 
"Amaranth biscuits yield a subtle nutty flavor that goes well with many spreads.", 
"Fruitcake! Can also double as a doorstop or makeshift weapon.", 
"Goodberry Biscuit are, a light, flaky, buttery biscuit infused with goodberry juice and drenched in a sweet sugary glaze. Eating two has either the healing or satiating effect at random. You can eat four but you are sickened for d4 rounds.", 
"Conchas are white, brown, or pink dusted sweet breads with a shell pattern on them", 
"Churros are long tubes of fried dough coated with cinnamon and sugar", 
"Cochito, a soft gingerbread in the shape of a pig", 
"Empanadas and pineapple, apple, or pumpkin turnovers provide a sweet, yet filling treat.", 
"A single, dusty, half-eaten cracker just laying on the floor.", 
"Turtle bread, a round loaf that is hard on the outside, and super soft on the inside.", 
"Copper cookies are small sweet cookies that cost 5cp each.", 
"Six Copper Pie (based on the Sing a Song of 6 Pence song/rhyme)", 
"4 and 20 Shrieker Mushrooms baked in a pie. The pie is baked in a dutch oven and set inside a fire-pit. When cut a few soft screams escape through the crust.", 
"Stone bread is perfect for adventurers as it will never go stale due to it already rock hard. It can double up as a rather effective improvised weapon.", 
"Black moss cupcake, a jet-black appearance belies an earthy almost charcoal-like flavor that transitions to matcha aftertaste.", 
"Owlbear Claws are delicious pastries made with honey and fig. They are a foot across with large ‘claws’ cut out on one side. Will feed a party of five. (Or one certain Dragonborn in my campaign).", 
"Arcane party muffins are chocolate and hazelnut muffins with magical blue sugar (that sparkles) sprinkled on top of them. When consumed you can change your eye color for a minute.", 
"Peanut butter cookies, a simple cookie adorned with fork marks and granulated sugar.", 
"Prism dough is a bread that is risen to look like a triangular based prism. It tastes sweeter at the top of the spire and sourer nearer the base. Can feed 2-4 people.", 
"The Little Volcano is a cone shaped jam donut that uses chili jam.", 
"Troll Rolls are warm basil rolls, jarred with melted honey butter and sugared flesh (non-human).",
"Swamp-weed Loaf, an uncommon and generally disliked type of baked good made from a dried aquatic kelp found in swamps. It’s unknown who first invented the swamp-weed loaf or for what reason, but what is known is that it’s absolutely dreadful.", 
"Fairy fingers are merengue treats, piped in a thinly oblong shape. Often coated in confectioner’s sugar but some recipes call for actual pixie or sprite dust.", 
"Fairy’s heart, a pastry twisted into the shape of a heart, with a (magically?) glistening jam centre.", 
"Angel food cake, a light and fluffy cake made using angel blood instead of eggs. Often glazed with a light lemon and sugar glaze. Tastes heavenly.", 
"Devils food cake, a dense and heavy cake made using the blood of devils that is fortified using ground bone devil horn. This cake has a sweet fiery cinnamon aftertaste that leaves the eater wanting for more.", 
"Rhubarb shortbread bars are a sweet confection made from shortbread coated in rhubarb custard and topped with brown sugar.", 
"Ankheg burrows, a thin but crispy chimney cake made by wrapping a thin strip of dough around a spool and coating the outside with oils and sugar before baking. Often filled with chocolate, nuts, or various fruits.",
]
let specialIngredient = [
"Shifting Calamari: The tentacles of a displacer beast sliced and fried in a light batter. Aim your fork carefully.", 
"Fajita Nocturna: Bat meat pan-seared with onions and eaten out of a dried and floured cloaker wing. Remember to remove the claws.", 
"Up-and-Down Stew: Traditionally made with blink dog and hellhound meat in broth, any mixture of Fey and Fiendish meat will achieve the dish’s signature roiling swirls.", 
"Steamed Umber Hulk: The arms and legs of an umber hulk steamed and served with veggies. May cause acute memory loss if undercooked.", 
"Underdark Paella: Cooked giant spider, umber hulk, and roper come together with fresh vegetables and sautéed shrieker to make a one-of-a-kind dish.", 
"King of the Sea’s Sashimi: A complex mix of herbs, spices, and sauce neutralizes the mind control toxin in the thinly sliced aboleth meat that makes up this dish.", 
"Gorgon Roast: The naturally hollow body of a freshly slain gorgon can be placed over a flame and used as a cooking vessel, creating a unique cooking style that brings a unique taste to the food.", 
"Hydra Eggs: With a similar property to their adult counterparts, the yolk of a hydra egg will appear to split 5 times when beaten. If fried, the yolk turns a deep amber color.", 
"Tadpole Cocktail: Mindflayer tadpoles beheaded, cooked with veggies, and served with cocktail sauce. Said to bring back old memories when eaten.", 
"Griffin Gyro Wrap: Griffin steak wrapped in the wings and spit-roasted vertically. Takes 2 days to cook, but serves 20.", 
"Dryad Tea: Adding leaves from a dryad can transform the flavor of any tea and impart a bit of the dryad’s mood at the time of picking onto the drinker.", 
"Bonfire Dire Boar: The only true way to cook the massive swine. Roast vertically inside a bowl-shaped bonfire until the outside is charred black. Make deep cuts as the juices tend to move inwards during cooking.", 
"Marauder’s Pie: Meat from at least 4 different sources ground up, cooked, mixed with veggies, and covered with a crust. A 'true' one contains meat from something sentient.", 
"Mushroom Casserole: Diced myconid, shrieker, and trillimac cooked with bluestalk pasta and a lichen sheet. High in protein, a favorite of low-ranking Drow.", 
"Skewered Manticore: Diced manticore roasted over fire on its own spines. Requires great care and patience, as the spines tend to shatter and ruin the meat. Success will yield a rich, spicy meal.", 
"Escarfléau: A flail snail cooked in the shell with a lot of butter and garlic, highlighting the meat’s natural spiciness. Served still in the shell, feeds four. Bon appetite!", 
"Draconic Jerky: The tongue of a dragon salted and dried, it’ll keep for 1000 years without losing flavor. Rarely made from a true dragon, usually the tongue of a wyvern or drake.", 
"Bullywug sur la flamme: The leg of a bullywug marinated for a week and grilled over an open fire. Tastes like chicken, smells like death. A favorite of Wood Elves.", 
"Hippocampus Surf’n’Turf: The legs and tail of a hippocampus cooked, lightly salted, and served together. Often prepared for aquatic dignitaries.", 
"Gelatinous Marmalade: Gelatinous cube jelly mixed with sugar water. Doesn’t taste like much, but can make just about anything safe to eat if enough is slathered on it.", 
"Woodland Bite: Viper venom watered down with apricot wine and spiced with pepper juice. Often used for drinking contests in more remote forest taverns.", 
"Lightning Gumbo: Diced behir meat, peppers, and onions in broth in a large heavy pot. After cooking for 30 minutes, dump the behir’s lightning gland in and close the lid. After the thud, the meal is ready.",
"Feast of Gruumsh: Prepared by orcs after a particularly successful hunt. The prize kill is buried with hot coals for 4 days, coated in sauce, and served whole. The hunter who slayed the beast begins the feast by stabbing out one of its eyes.", 
"Lost Honor: When a rust monster eats a dwarf’s weapon, it’s only fair the dwarf return the favor. The claws of a rust monster are tough, tasteless, and unfulfilling, but the dwarves don’t care.", 
"In the Eye of the Beholder: The severed eyestalks of a beholder can impart their effects onto food placed inside for weeks after death. Effects range from refrigeration to disintegration, all useful in their own ways.", 
"Troll Taters: Sliced potatoes oven-roasted in troll fat. After 30 minutes, the potatoes will come out fully cooked but looking raw due to the lingering regeneration effects of the troll fat.", 
"Gnoll Rolls: Pan-fried gnoll meat packed into small biscuits. Good trail food, athough it may scare of wildlife.", 
"Phoenix Roast: While difficult, it is possible to delay the burning and rebirth of a Phoenix. The result is a naturally sweet meat that cooks itself, going from raw to fully cooked in 15 minutes. After 1 hour, the rest of the bird will resurrect as normal.", 
"Sliced Troll Liver: The liver of a troll will continuing regenerating for several days after death. By placing a chunk of liver in an open topped container, roughly 50 slices of fresh liver can be freely acquired before the quality suddenly drops.", 
"Desert Sun Jerky: The tail of a giant scorpion hung on a rack to dry for 3 days. Every 12 hours, it must be flipped over. After 3 days, all of the venom has broken down, salting the meat in the process.",
"Troll Stirfry: Greased with pig fat and vegetables from fresh gardens. Spices from far off lands burn your tongue. Next time you land a flamming arrow upon a Trolls brow, take a slice of flesh along with its gold.", 
"Beholder Sushi: Beauty may be in the eye of the Beholder, but it’s taste is in the eye stalks! Really speaking, this can be made with most Beholder-kin (such as Spectators) and even enjoyed as sashimi. If you’re too squeamish about eating the ‘tentacles’ of your floating eyeball nightmares raw, simply coat in batter and crispy breadcrumbs for an excellent (if dangerous) kalimari.", 
"Gorgon Roast: While not technically edible itself, the rocky/metallic remains of a Gorgon Bull Male am excellent oven for the smart, open minded adventurer. Lighting a fire beneath an I damaged portion of the bill allows you to turn it into a giant cooling vessel. Always aim to remove the head cleanly for the best results. Once slain, it will become perfectly hollow, but always allow to air for one hour to allow any remnants of its vapours to escape. Then stuff the metal carcass with any other meat you can hunt and enjoy the satisfaction on multiple levels.", 
"Sahaguin Roe: Questionable, as the creature is seen as humanoid by most adventurers, the eggs of these fishlike creatures are much like salmon roe, popping with small explosions of flavour on the tongue.", 
"Dryad Tea: Should one find a friendly Dryad, always ask for some leaves or petals to add an excellent infusion of flavour. These flavours change depending on the Dryads mood when gifting the leaves. For the best results, flirt gently with the nature spirit. NEVER take the leaves or remains of a dead or corrupted Dryad unless planning on brewing laxatives or poisons.", 
"Seared Scorpion: Either boil or sear the meat in the shell, then consume similar to lobster or other shellfish. Heating the shell not only makes it easier to break, but also allows the meat to steam inside the shell, making for a much more tender meal.", 
"Slaughterfish Stew: One of the few fish that tastes better stewed. For the best results, skin the fish pieces and poach in milk instead.", 
"Pan-fried Cockatrice: Tastes so much better than chicken! A favourite of adventurers and food connoisseurs the world over, this versatile meat can be fried, breaded and barbecued for an excellent and filling meal with very little effort… except for killing the creature in the first place. It’s also rumoured to help the joints, especially after petrification.", 
"Phoenix Soup: Not made with actual Phoenix. This is made with a meat of your choice and a Phoenix feather. No fire necessary. Simple break the feather around the middle and drip 3 drops of the golden liquid into the soup you’ve prepared. For added flavour, shave the feather stem into your soup or save them for another night. You should now have a filling, spicy dish that will revitalise you and leave you feeling refreshed and ready to carry on, night or day!", 
"Manticore Skewers: Slightly dangerous. Never break the spines, and only ever use unbroken spines to begin with. Cut the manticore meat into bite sized pieces before skewering. Roast on an open fire. If the spine explodes, do not eat the meat. If prepared correctly, the spicy, fiery toxin will denature and become something akin to a sauce or marinade as it leaches out of the skewer and into the meat as it cooks. Not for the faint of heart.",
"Dragon: A notoriously difficult meat. Dragons are normally sentient creatures, but the lesser dragons (including wyverns and wyrms) are considered fair game. Excluding the alchemical ingredients, such as the eyes or heart (which must always be consumed raw if used in magical recipes or rituals), most of a dragon is meat, just like any animal. After the arduous task of scaling (best done with the beasts own claws or teeth), the meat must be cooked on an incredibly hot flame, regardless of species. It is believed to be physically impossible to overlook dragon. Also, the dragons tongue is entirely edible. Often considered an alchemical ingredient, it can be cooked or dried into jerky. It often holds a little innate magic, transferring the knowledge of languages the creature knew in life, if any. An interesting (and tasty) way to learn some new words.", 
"Gryphon sirloin: Often utterly ruined by the casual adventurer, the Gryphon should be butchered by a professional whenever possible. A well prepared, fresh Gryphon sirloin will often fetch as much money as the party will receive from felling the beast in the first place! Surprisingly tender and flavourful, the meat is a strange combination of white and red, fusing the best of both into some of the best meat known to men or elves.", 
"Fried Goblin Ears: Works with a variety of ears, so long as the adventurer isn’t picky or is desperate. Favourite snacks of the bandit tribes of the south, the fried ears of their foes are enjoyed by all ages after the rest of the corpse has been robbed, stripped and butchered… maybe skip this recipe…", 
"Whole Roast Dire Boar: Wild pigs have nothing on the elusive Dire Boar. Even Dire Wolf packs think twice before attempting to bring down one of these colossal swine! Often as big as a small elephant, the only way to enjoy this is to roast it whole. Make it a celebration. The whole hunting party should help gathering wood and building a large enough spit to cook the kill. Carve away meat once cooked like kebab meat and enjoy with the whole village!", 
"Roast potatoes in Troll Fat: No duck fat for these crispy adventurers favourites! Simply roast in a clay oven after cutting into quarters and covering liberally with Troll fat.", 
"Kraken caviar: Incredibly rare and extremely expensive, only the richest of kings and emperors will ever be able to dine on the freshly laid eggs of a Kraken. These things are released en masse and grow rapidly to try and combat the multitude of oceanic predators that feed on their young. These must be caught and consumed less than 5 days after being laid. After that, if exposed to water, these regular looking roe will rapidly expand to the size of a cannonball and continue to absorb nearby water until it holds a pocket of water roughly 5ft in diameter.", 
"Hydra Eggs: With a similar property to their adult counterparts, the yolk of a hydra egg will appear to split up to 5 times while being beaten. If fried, the yolk turns a deep amber colour.", 
"Owlbear Steak: Very ‘gamey’, but perfect for jerky. Plenty of meat on an Owlbear too.", 
"Roast Behir: The only way to enjoy the multi-legged dragon lookalike. After removing the electric glands and other organs, the meat of a Behir should be either smoked or roasted. Most adventurers miss out on the best flavour of this mountain dwelling creature. Properly cooked, Behir meat should have a taste reminiscent of the air after a lightning storm. Pairs well with cheese, oddly enough.", 
"Ants on a Log: Raisins and peanut butter slathered on beholder eyestalks (replaces celery stalks).", 
"Shell Shark Fin Soup: The fin decorating the bowl is just for show, the soup itself is a standard vegetable broth.", 
"Bullywug Leg: said to taste like chicken, if that chicken had been drowned in a swamp.", 
"Flail Escargot: A whole Flail Snail is roasted in the shell, and served with garlic and herbs. Its so large, that it is often ordered as a main course for 4 people.", 
"Mindflayer Calamari: The mindflayers tentacle gives just a bit more out of the ordinary taste to it, which has been discribed as ‘out of this world’.", 
"Illithid Probes: Mind flayer spawn harvested by the town’s local heroes. Their heads are cut off and the bodies lined up like shrimp. It is a good source of vitamins for the brain. 6: Owlbear Meat: A large slab of owlbear meat slathered in gravy made from the meat itself.", 
"Shambling Lettuce: Leafy greens harvested from a shambling mound. Just dont let it get away!", 
"Strahd Wine: Some stupid adventurer took that wine glass strahd always had after killing him. Turns out it’s bottomless. Yay?", 
"Terrasque Ice Cream: Powdered terrasque horn, once shaved off, it can be used for a variety of purposes due to its resistance to temperature change. One of them is ice cream!", 
"Bullete-Fin Soup: An exotic dish made from these dangerous creatures. Served in a buttery soup.", 
"Ilithari: mind layer tentacles sautéed in a sauce made from spiced ilithid cerebrospinal fluid. Warning, may cause hallucinations.", 
"Gelatinous Cube Marmalade: The snack that bites back! Be sure to remove any debris of slain adventurers.", 
"Poached Basilisk Eye: Eat it but don’t look it at. Mostly because gross.", 
"Gnoll Roll: A hearty biscuit stuffed with pan-fried gnoll meat. Eating too many may give you feral thoughts.", 
"Animated hors d’oeuvres: All of these finger foods are held together with tiny, toothpick-sized animated swords. They’re delicious, but can be deadly in a swarm.", 
"Lime Gelatinous Cube Salad – A dish made from the genetically modified and farmed Lime Gelatinous Cube. Consists of a whole Lime Gelatinous Cube stuffed with fruits and topped with whipped cream.", 
"Roc Foie Gras – Made from the fatty liver of an inhumanely force-fed Roc. One serving of Roc Foie Gras could feed an entire village, but it is quite expensive and typically only enjoyed by the upper class.", 
"Quasit Boil – Typically served at large get-togethers, hundreds of Quasits are boiled alive with corn on the cob, potatoes, sausage, and spices. This dished is traditionally served in a family style fashion by dumping in a large pile on a table and dumping additional spices directly on top.", 
"Fondgoo: An insane eccentric aspiring gourmet turned adventurer developed this after a horrific adventure in a ooze laboratory. Combining the jelly of a gelatinous cube with copious amounts of cheese and wine over high heat, you are able to neutralize most of the acidic elements to create an amazing dish. A mild anesthetizing effect tickles and numbs the mouth, preventing speech for a minute after consumption. Some consider this a boon and it is a frequent dish at many upper-class family reunions.", 
"Flesh Fondgoo: Captured by a human from beyond the stars with an unnatural hunger, the chef only had servitude as a survival option. Becoming comforter and preparer of meals, the new take on the fondgoo proved to be delectable with the right ingredients. Thin slices of half-orc proved to be the most popular with the star cannibal and his crew, wildly rich with only mild game flavor from the mixed heritage. The gourmet would never admit it to anyone, but his refined palate preferred the gnoll. The terror only ended after discovering what they thought was a holy grail, a Hungering Flesh that went from cornucopia to consumer in no short order.", 
"Roasted Phoenix: When you’re done, you toss the bones in the fire and *pop* the phoenix is back. Also, you can always cook it just right; if you keep going, then it loops rare through well done.", 
"Forever Stew: made with a bit of troll meat which is still regenerating. If managed carefully, one only needs to add vegetables and can continue making a meaty stew night after night, indefinitely. But if you don’t eat it fast enough or fail to tend it properly, you could end up with recognizable troll bits (hands, eyes, …) starting to show up, or worse.", 
"Basilisk Bisque: With a broth made from basilisk scales and filled with root vegetables and basilisk meat, this bisque is normally served in a warmed stone bowl.", 
"Almiraj & Rabbit Buchada: A dish marvellously made with part Almiraj and part Rabbit, both are force-fed until their stomach rips. The organs are then removed and the meat, carrots, cuscus and herbs are stuffed inside the Almiraj’s stomach.", 
"Flumph with Undersalmon: The tendrils of a dead flumph are removed, boiled on water along with the sanguine coloured fish commonly known as Undersalmon. It is served with Rice and Potatoes. This Dwarven dish has been since outlawed, with the discovery of the complexity of Flumph society. Although some still prepare it, as not only is it a delicious food, the psionic energy left on the meat brings joy to those who eat it.", 
"Neogi Neck: one of the few parts of the Neogi that are not poisonous, the Neogi’s neck has tender meat and takes months to spoil. As such, it’s often sought out by adventurers tired of eating the same old dried meat when on the road.", 
"Dry Stirge: this is a common folk food. In places with Stirge infestations, meat is often spoiled as these tiny creatures suck all of its blood and nutrients. Because of that, locals recur to it to replace their meat. The Stirge is prepared on a campfire, but because of the many types of blood that it sucks, it often leads to the eater contracting some sort of disease.", 
"Party meat: Nobody knows who had the terrifying idea of powdering sugar on Kruthik tissue, but certainly it was a madman. Or a genius, once you taste it and realise this abysmal combination is actually delicious. it’s almost impossible to attend to a dwarven party without seeing this dish, commonly known as party meat.", 
"Axe Beak beak: This is usually served with the bird’s head cut off and the lower part of its beak being decorated with its meat, as well as a plentitude of vegetables.", 
"Mind Flayer Calamari: Mind Flayer tentacles chopped and deep fried. Great with soy sauce and rice.", 
"Ankheg Claw Stir-Fry: Ankheg claws are very tough due to constant use in burrowing and therefore require long cook times, but soften beautifully over time. Use ginger, spring greens and your favourite stir fry sauce, goes very well with roughly chopped myconid.",
"Hydra Eye Jelly: A delicacy among the braver class of adventurers, Hydra eyes became so highly acclaimed in part due to the might of their owners, but also due to the fact that you will generally get a minimum of ten for every Hydra killed. Cook in simmering water until they begin to cloud, then chill in an ice bath and mash before mixing with pork gelatin and allowing to solidify while chilled.", 
"Froghemoth Calamari: Delicious and filling, Froghemoth Calamari is a dish enjoyed by all, cut into rings, removing the cartilaginous and muscular centre before washing well. To cook, broil until firm and serve with olive oil and vinegar or to simply fry until golden and serve with as many dipping sauces as you wish, don’t be afraid to experiment.", 
"Pate of Elder Brain: A very difficult meat to acquire and tricky to prepare properly, Pate of Elder Brain is worth the work if you live to taste it. carefully remove all external tentacles and connective tissue before butchering, being careful of the internal connective tissue as you go. Cut into small pieces and place in a pot of water, slowly raise the temperature to medium until firm and blanch once cooked before blending. Ensure brain is really dead before preparing to butcher.", 
"Fried Roc Wings: Once you have your Roc wings, butcher them into pieces around the size of a chicken’s wing and lay aside, mix together flour, spices, salt and pepper before carefully coating the Roc meat and frying, be sure that the Roc is cooked through, Roc wings are tough and must be cooked well.", 
"Otyugh Ribs: Who would have thought that a garbage eating Monster could be to tasty right?! Butcher the ribs down small enough to fit into your ceramic oven and cook overnight in your favourite pork sauce, before revelling in the delicious taste of possibly the most amazing ribs you will ever taste.", 
"Remorhaz Stew: Remorhaz is a wonderful meat for stews in that it retains heat forever! The Heat immune properties of the Remorhaz become fallible after their death, but they still require extremely high temperatures to be able to cook. Think smelting furnace, not oven. With such high temperatures required, Remorhaz needs to be cooked by eye due to the limited availability of such heat sources. Dice into evenly sized chunks and cook until very slightly crisp on the outside, tossing as you go before adding to a stew. Sufficiently heated Remorhaz meat will stay hot for hours, even up to a day or two, keeping any stew it is added to hot as long as you wish.", 
"Roasted Bulette Flank: Bulette flesh is damnably tough and needs to be slow cooked with extreme patience. Combine red wine vinegar, balsamic vinegar, soy sauce, brown sugar, mustard, rosemary, olive oil, and salt and pepper to taste to make a marinade. Cut the flank steaks off of the body and marinade them for at least a full day before roasting while continuously basting with the drippings. Once finished you will have a beautifully flavoursome and moist flank that while slightly gritty, is worth the effort of cooking it.",
"Cave Fisher Sushi: As some of you may know, Cave Fisher blood ignites if exposed to flame or excess heat, therefore the best way to prepare it is to cut the meat into sushi sized pieces and drain as much blood as possible from the flesh before igniting and letting the excess blood burn off, lightly flaming the sushi for perfect preparation. Serve on Sushi rice with soy sauce.", 
"Forest Garbage Sauce: Anything you can use. Violet fungus, myconids, moss, mushrooms. Provides a hearty, earthy base. A secret: the sap of a treant, woad warrior, or blight is bitter. But together, simmer them. Put over any dark meat and find a bottle of dark, cheap red wine.", 
"The blood of a vampire spawn is intoxicating. Mix with a bloody-mary (that tomato based morning juice drink). Add in some raw vegetables. Celery, olives, carrots, and the like. Bottoms up.", 
"Demon Wing Soup: It’s very spicy, and the wings are chewy, but there isn’t a whole lot for a humanoid to eat in hell, so it works.", 
"Candied Quipper: One of the cheapest quick snacks around. Quippers taste uncompromisingly bitter and have an awful crunch to them. They still aren’t very good once dipped in boiling tree sap, but at least they are covered in candy…", 
"Honeyed Siren’s Tongue: The tongue of a siren produces the most wonderful sound when chewed, bards will often accompany instrumental performances with the chewing of a Siren’s tongue in order to woo crowds even further. Mixing it with honey makes it slightly easier to chew, but cooking it causes it to lose these magical effects.", 
"Water Elemental Juice: The fluid harvested from a living water elemental has been known to retain effervescent properties after being harvested due to residual magic power left over in the collected sample. Water elemental juice can be mixed with anything from potions to fruit juice to make a refreshing bubbly beverage. It is suggested to not drink the substance without dilution.",
"Pixie Salad: A tossed salad of finely chopped pixies will always produce the flavors of the colors of the rainbow. Each bite may taste like a different color, the first might be purple, the second may taste like red and so on and so forth. The older the salad is since the death of the pixies the closer the taste is to brown.", 
"Trollbalaya: A jambalaya made from troll sausage, typically with a drizzle of boiled troll blood, topped with two Troll’s eyes. (Trolls are surprisingly delicious)", 
"Pulled Orc Sandwiches: Typically made from Orc shoulder or pectoral, the younger the orc the better. Requires 10 hours of cooking over old coals, best seasoned with an elven blend, two chopped onions, and copious salt and pepper.", 
"Burritoes: Giant’s toes are surprisingly rich in protein and healthy fats. Chop them, Sear them, cook two behir eggs in the left over grease, and create an excellent set of breakfast burritos. For a bit of added fun, they are best served on the toe nail.", 
"Rib-hirs: Behir’s are nasty buggers, but they’re good for one thing: ribs. The longest rib cage you will find, gather up your town, or the local goliath tribe, and you’ll make a killing off of these. Flay the scales and smoke at a low heat over hickory logs for 2 days, slowly rotating the ribs through. A nice baste of dwarven ale mixed with citrus, or a rub of an orcish spice blend will make this a meal to remember. Just keep in mind the smell will travel for miles, so you might attract a nearby Roc.", 
"Roc Stock & Balor: While not actually made with Balor flesh, this demonic delicacy is as the name implies a stew made from Roc stock and any sort of demonic flesh. Due to the hellish nature of the flesh, the stew does not need any outside heat to work itself to a hearty temperature. Good for those in survivalist situations, assuming you can ignore the faint brimstone smell.",
]
let chance = rollDice(100)
if (chance < 33) {
return "The special for the day: '" + searchArray(foodEvent) + "'."
} else if (chance < 90) {
return "The specials for the day: '" + searchArray(bakedGoods) + " Also, we have " + searchArray(specialIngredient)
} else {
return "We just have the regular ol' fare today "
}

}
document.getElementById("Food").innerHTML = findFood();
};
function gameFind() {
let size = [ "large group of people", "considerable crowd of people", "few tables pushed together with a small group of people", "pair of people", `rambunctious crowd surrounding ${toWords(2+rollDice(8))}people`, ];
let stakes = [ `players have the opportunity to bet once on each player's turn`, `players have several opportunities to bet on each player's turn`, `players have several opportunities to bet each round`, `players must bet before the round is played`, `players must bet before the game begins`, `spectators bet as often as players do`, `spectators typically place bets before the game begins`, `spectators often place bets while the game is in progress`, `cheating is extremely rare or impossible`, `cheating is difficult, and often occurs with the help of someone else in the room`, `cheating is common`, `cheating is encouraged`, ];
let renown = [ `high stakes gambling.`, `low stakes, social gambling.`, `its simple set of rules.`, `its complicated set of rules.`, `the ease with which anyone can learn to play.`, `its class of expert players and their elaborate strategies.`, `a celebrated instance of cheating that launched a war.`, `a celebrated instance of cheating that prevented a war.`, `a legendary match involving a king or queen.`, `a legendary match involving a witch or wizard.`, `a storied bet where the loser faced an aberration with many eyes.`, `a storied bet where the loser faced a dragon.`, `a storied bet where the loser faced a demon.`, `a storied bet where the loser faced a devil.`, `a storied bet where the loser faced an elemental.`, `a storied bet where the loser faced a kraken.`, `a storied bet where the loser faced a lich.`, `a storied bet where the loser faced a vampire.`, `a storied bet in which the winner took an airship from the loser.`, `a storied bet in which the winner took an ancient text from the loser.`, `a storied bet in which the winner took a castle from the loser.`, `a storied bet in which the winner took the keys to the city from the loser.`, `a storied bet in which the winner took a magic sword from the loser.`, `a storied bet in which the winner took a magic wand from the loser.`, `a storied bet in which the winner took a princess from the loser.`, `a storied bet in which the winner took a treasure hoard from the loser.`, ];
let popular = [ `sailors and pirates.`, `fishermen and dockworkers.`, `thieves and knaves.`, `knights and lords.`, `peasants.`, `dwarves.`, `miners and smiths.`, `goblins and hobgoblins.`, `elves.`, `noblewomen.`, `masons and stonecutters.`, `mages and priests.`, ];
let origin = [ "long ago in this region.", "long ago in a foreign land.", "long ago in an unknown location.", "in the recent past in this region.", "in the recent past in this very room.", "in the recent past in a foreign land.", "down along the docks of a bustling port city.", "in a quaint country inn.", "in rough-and-tumble urban tavern.", "along a trade route to an exotic land.", "in the court of a mighty king or queen.", "in the mind of a half-mad wizard." ];

function cardGame() {
let winner = [ "play all the cards in his or her hand.", "be holding the highest score at the end of the hand.", "be holding the score closest to a target score.", "hold all the cards in the deck.", "win the most tricks over the course of a round.", "be holding the lowest score at the end of the hand.", "bluff and bet their way to having the lowest scoring hand.", "bluff and bet there way to being the highest scoring hand."]
let best = [ "the dragon", "the lord", "the crown", "the queen", "the alchemist", "the knight", "the champion", "the eagle"]
let worst = [ "the worm", "the beggar", "the rat", "the fool", "the crone", "the devil", "the villain", "the pigeon" ]


let cards = [
`The rules are simple, on each turn the player plays a card from his or her hand face up or face down on the table. To win, they must ${searchArray(winner)} The best ${searchArray(['card','hand',])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}. `,
`The rules are simple, on each turn the player draws one or more cards from a personal deck. To win, they must ${searchArray(winner)} The best ${searchArray(['card','hand',])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}. `,
`The rules are simple, on each turn the player draws one card from a community deck. To win, they must ${searchArray(winner)} The best ${searchArray(['card','hand',])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}. `,
`The rules are simple, on each turn the player draws a card from a community deck if he or she has no other plays. To win, they must ${searchArray(winner)} The best ${searchArray(['card','hand',])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}. `,
`The rules are simple, on each turn the player places a card from his or her hand into the discard pile. To win, they must ${searchArray(winner)} The best ${searchArray(['card','hand',])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}. `,
`The rules are simple, on each turn the player lays down a pair, a three or four of a kind, or a straight on the table. To win, they must ${searchArray(winner)} The best ${searchArray(['card','hand',])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}. `,
`The rules are simple, on each turn the player lays down a card to build threes and fours of a kind or straights on the table. To win, they must ${searchArray(winner)} The best ${searchArray(['card','hand',])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}. `,
`The rules are simple, on each turn the player draws one or more cards from a personal deck. To win, they must ${searchArray(winner)} The best ${searchArray(['card','hand',])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}. `
]
return searchArray(cards);
};

function diceGame() {
let winner = [ "have rolled the highest score in play.", "roll the highest possible score.", "roll the lowest possible score.", "have rolled the lowest score in play.", "achieve a target score over the succession of many rolls.", "outscore his or her opponents over the succession of many rolls.", "bluff and bet their way to having the lowest remaining score.", "bluff and bet there way to being the highest remaining score." ]
let best = [ "the dragon", "the keep", "the warship", "the maiden", "the thunder", "the shark", "the tower", "the sorcerer" ]
let worst = [ "The snake", "The thief", "The dinghy", "The hag", "The ghost ship", "The tuna", "The pits", "The demon" ]
let dice = [
`The rules are simple, on each turn the player rolls once. To win, they must ${searchArray(winner)} The highest roll is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player rolls twice, keeping the better results. To win, they must ${searchArray(winner)} The highest roll is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player rolls once or twice, keeping the second result on a reroll. To win, they must ${searchArray(winner)} The highest roll is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player rolls at the same time as other players. To win, they must ${searchArray(winner)} The highest roll is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player rolls and hides the results from other players. To win, they must ${searchArray(winner)} The highest roll is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player rolls and hides the results from him- or herself and from other players. To win, they must ${searchArray(winner)} The highest roll is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player rolls and hides the results from him- or herself but not from the other players. To win, they must ${searchArray(winner)} The highest roll is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player rolls and waits for an arbiter to make a ruling. To win, they must ${searchArray(winner)} The highest roll is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`
]
return searchArray(dice)
};

function boardGame() {
let winner = [ "capture all of his or her opponents pieces.", "kill all of his or her opponents pieces.", "race his or her opponent's pieces through a labyrinth of obstacles.", "maneuver pieces to the far side of his or her opponent's territory.", "capture his or her opponent's headquarters.", "kill his or her opponent's commanding piece.", "score points while navigating pieces through a labyrinth.", "claim territorial positions with pieces before his or her opponent does.", ]
let best = [ "the dragon", "the warhorse", "the warlord", "the mastermind", "the queen", "the dark lord", "the treasure chest", "the sword", ]
let worst = [ "the minion", "the foot soldier", "the goblin", "the goon", "the guard", "the skeleton", "the trap", "the club", ]
let board = [
`The rules are simple, on each turn the player moves one of his or her pieces on the board. To win, they must ${searchArray(winner)} The ${searchArray(["most powerful piece", "strongest maneuver"])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player places a piece on the board. To win, they must ${searchArray(winner)} The ${searchArray(["most powerful piece", "strongest maneuver"])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player moves two or more of his or her pieces on the board. To win, they must ${searchArray(winner)} The ${searchArray(["most powerful piece", "strongest maneuver"])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player places two or more pieces on the board. To win, they must ${searchArray(winner)} The ${searchArray(["most powerful piece", "strongest maneuver"])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player removes one or more of his or her opponent's pieces by encircling it or flanking it. To win, they must ${searchArray(winner)} The ${searchArray(["most powerful piece", "strongest maneuver"])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player halts his or her opponent's progress by encircling or flanking one or more of the opponent's pieces. To win, they must ${searchArray(winner)} The ${searchArray(["most powerful piece", "strongest maneuver"])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player converts one or more of his or her opponent's pieces by encircling it or flanking it. To win, they must ${searchArray(winner)} The ${searchArray(["most powerful piece", "strongest maneuver"])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`,
`The rules are simple, on each turn the player moves his or her piece closer to a destination space on the board. To win, they must ${searchArray(winner)} The ${searchArray(["most powerful piece", "strongest maneuver"])} is called ${searchArray(best)}, and the worst is called ${searchArray(worst)}.`
]
return searchArray(board)
};
let games = [
[
`You notice that there is a ${searchArray(size)} playing a card game with a deck of over 100 cards. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${cardGame()}`,
`You notice that there is a ${searchArray(size)} playing a card game with a deck of 53 cards. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${cardGame()}`,
`You notice that there is a ${searchArray(size)} playing a card game with a deck of 52 cards. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${cardGame()}`,
`You notice that there is a ${searchArray(size)} playing a card game with a deck of 24 cards. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${cardGame()}`,
`You notice that there is a ${searchArray(size)} playing a card game with a deck of 22 cards. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${cardGame()}`,
`You notice that there is a ${searchArray(size)} playing a card game with a deck with a variable number of cards. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${cardGame()}`
],
[
`You notice that there is a ${searchArray(size)} playing a dice game using a pair of dice. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${diceGame()}`,
`You notice that there is a ${searchArray(size)} playing a dice game using several dice. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${diceGame()}`,
`You notice that there is a ${searchArray(size)} playing a dice game using several dice, pencils, and paper. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${diceGame()}`,
`You notice that there is a ${searchArray(size)} playing a dice game using one or two dice and a board with pieces. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${diceGame()}`
],
[
`You notice that there is a ${searchArray(size)} playing a board game with sets of matching pieces. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${boardGame()}`,
`You notice that there is a ${searchArray(size)} playing a board game with sets of individual pieces. In this game ${searchArray(stakes)} and it is known for ${searchArray(renown)} The game is widely known, but is most loved by ${searchArray(popular)} It was devised ${searchArray(origin)} ${boardGame()}`
],
];
let chance = rollDice(100)
if (chance < 33) {
return searchArray(games[0])
} else if (chance < 67) {
return searchArray(games[1])
} else {
return searchArray(games[2])
};
};
function events() {
function checkEvent() {
let badTavernEvent = [
"Local criminals hangout in this tavern. They try to sell drugs. One criminal pours red dust in the drinks of the guest while they are not watching.", 
"The tavern is known for gambling. One guy is on a big winstreak and pays drinks for everybody. Nobody knows yet that he plays with loaded dice.", 
"The ‘bartender’ is handing out free drinks and food. The owner is locked into the storage room.", 
"A crossbow bolt crashes through the window and strikes a merchant who came to the city from far away.", 
"A ventriloquist starts preforming. The puppet looks very old and is wearing clothes that were quite fashionable about a century ago. The performance satirizes current events and culture and has the whole tavern laughing, but if you are observant for about half an hour, whenever the ventriloquist suggests wrapping up the performance the puppet dismisses his concerns. The show goes on for three hours until the puppet is finally satisfied, at which point the ventriloquist is extremely tired and looks terrified.", 
"A puritan priest comes in and berates the patrons for their behavior, preaching a path of holiness and purity. The old innkeep tells him ‘Yer aff yer heid, ya wee bawface!’ and proceeds to flash her boobs at him. The priest flees in horror, muttering protective chants.", 
"A scruffy looking man slips something into a drink before returning to the woman at his table.", 
"It’s a two for one special night and the tavern is packed, making easy targets for thieves and pickpockets.", 
"A drunk half-orc starts taunting the innkeeper, who’s cut him off.", 
"The tavern has a black board on one of the walls, with the names of each person present, and current bets. It’s a deadpool, in which people bet on your death.", 
"A group of exquisitely dressed people walk into the tavern, judging people’s outfits, generally in a negative way.", 
"A fight breaks out, between two big strong men. The bartender sighs, and gives each a free drink, separating them.", 
"The customers are all looking over their shoulders, with small smiles on their faces, and seem ready to… do something. Suddenly, someone screams ‘FOOD FIGHT!’ and everyone starts throwing food at each other. In the end, the owner gets pissed, and makes everyone clean up the mess.", 
"A man in a dark trench coat is skulking in the back, selling contraband to anyone who asks.", 
"A man in a dark trench coat is skulking in the back, selling contraband to anyone who asks However, he is part of a sting, and the local guard snatches up the buyers on their way out of the tavern.", 
"Someone playing the knife-fingers stabbing game accidentally stabs their own hand, possibly cutting off a finger.", 
"The local militia captain busts down the door and grabs the innkeeper, placing him under arrest for an unknown reason.", 
"Two drunken wizards come to blows over a perceived slight. Parts of the tavern catch fire or are otherwise affected by magical effects.", 
"A shadowy figure enters and orders a drink. The only problem is, there seem to be a mass of tentacles where feet should be.", 
"The first batch of beer from the halfling brewery in the next town is very lively. A bit too lively. A tide of hoppy foam bursts from the barrel and up into the bar, showing no signs of slowing down.", 
"After a few drinks, you could swear all the patrons in the bar have the exact same face. You shake your head. Must be the wine.", 
"The barkeep here has a very literal approach to lock-ins. Sure, you can drink past closing time—as long as you didn’t want to leave again, ever.", 
"Part of the tavern is under construction after a battle or large fight. Builders are constantly moving planks of wood between tables and sometimes hitting patrons. Roll improvised weapon attacks vs players AC at various points in the visit.", 
"The inn is flooded with people. Survivers of a battle not far off. Some seem to only have superficial wounds while others are not as lucky. Over the sounds of heavy breathing and mouning the party hears a voice ring out ‘CLERIC!! We need a cleric!’", 
"A health inspector busts in and attempts to shut the bar down due to health code violations.", 
"After several drinks the party realizes that they’re the only non-monster creatures in the tavern.", 
"After several minutes inside the tavern the party can hear a thunder storm rolling into the area. The whether gets increasing worse the longer they stay inside, and after 45 minutes a tree crashes into the side of the tavern.", 
"A religious group comes inside to preach about the sin of consuming alcohol.", 
"The musicians plating inside the tavern draw in a large enough crowd that the that the bartenders have to start kicking people who are too drunk.", 
"After the party sits down for a drink or two, a group of guards come inside searching for several highway robbers. The robbers descriptions match those of the party members; so they’er handcuffed, dragged to prison, waiting for a trial.", 
"Two Warforged start fighting one another. Watch out for their partner the Gnome pickpocket. She’s the brains of the operation.", 
"A fire elemental moves into the hearth!", 
"This is a thieve’s guild’s secret hideout in plain sight. Tonight, the corpses of the dead they left beneath the floorboards arise!", 
"The tavernkeep is a vampire. One of his servants accidentally begins pouring a bottle of his finest blood.", 
"A group of overzealous paladins springs a sudden raid on the tavern, breaking casks and arresting people, slamming them into cage-carts they parked in the back.", 
"One of the patrons is a werewolf, and he begins to turn.", 
"An ancient legend is (figuratively) brought to life by a traveling team of a bard and an illusion wizard.", 
"The tavern begins a ‘you break it, we hire a bounty hunter to make you pay’ policy today. No one wants to be the first person to break the rule.", 
"That Elven barmaid, that’s been slapped on the butt one to many times, turns out to be a shapeshifter. And she’s just transformed into a raging ogre.", 
"A notorious criminal duo known as the Grimshade Brothers have arrived to the tavern to celebrate which is in the neighboring village of the city they just robbed. Their known for robbing banks and causing mayhem wherever they go.", 
"Two goblins are on stage doing a juggling act. The juggling act involves flaming torches, hand axes, and vials of strange green goo. No one seems concerned.", 
"A love potion is accidentally slipped into one of your party’s drinks instead of the beautiful lady at the next table….", 
"Book signing for the new release ‘Quest for Annihilation : How Adventuring is Destroying Our Moral Fabric’", 
"The drunk mage in the corner is passed out and talking in his sleep. Roll for wild magic effect.", 
"You stumble into the middle of a wake, complete with the body of the deceased on ice next to the bar. Bonus points if that’s the ice used in the drinks!", 
"The owner makes it very clear he don’t want no trouble in his bar. Will not serve adventurers if they don’t relinquish their weapons.",
]
let tavernQuest = [
"Some tables are flipped over. In the middle of the room is a young orc girl on the ground surrounded by a few people. Her water just broke. She is about to receive twins. Nobody knows what to do.", 
"Two separate people are drinking alone. Neither seems at all suspicious on their own, but together they happen to be watching every single patron, as well as every entrance/exit.", 
"You hear an explosion from across the tavern. The blast knocked out a male gnome for 1d6 minutes. Once the gnome wakes up he starts madly raving, saying things like ‘I was so close!’ and ‘that was my last chance.’ and ‘it’s too late now.’", 
"The tavern is hosting a weekly poker tournament. If the players win, they get gold and gossip possibly leading to a quest.", 
"Tavern acts as a clearinghouse for counterfeit currency. Next shipment arrives two days from today.", 
"The tavern is about to run out of ale. Your party is discretely asked to procure some more within 1d4 hours to avoid a riot.",
]
let goodTavernEvent = [
"Tonight is the 10th annual Dragonfire Drinking contest! The person who can stomach the most Dragonfire Ale (very, VERY hot) will win the grand prize!", 
"A group in the back corner of the tavern are arm wrestling.", 
"A travelling gnome from a far away land has made a deal with the tavern, and is selling exotic and strange drinks in a wooden stand they have set up in the corner of the room.", 
"It is the monthly wild magic surge brew drinking contest. If you can get the most down, you win. You may lose your hair and grow an extra arm but hey, the prize is 30 gp.", 
"The owner of the tavern is an old lady. She owns about 5d20 cats. She cant serve you drinks or food right now because she has to feed her cats first.", 
"There is a cow in the middle of the tavern. Everybody is wasted and nobody knows how the cow got there or who owns the cow.", 
"A half-elf sitting alone seems to be muttering to themselves but is actually decribing the comings and goings of the tavern to a sentient weapon on their lap.", 
"A soldier is dressed in plainclothes, watching a deal going on at another table. The disguise is not fooling anyone.", 
"It’s the annual ‘Food Frenzy’. For two silver pieces (one of which goes to the house, the other to the pot), participants compete to eat the most meatballs in 10 minutes. There are six heats, and a then final. The winner of the gets the pot.", 
"It’s the annual Ferret-legging Endurance competition. In the sport of ferret-legging, competitors tie their trousers at the ankles before placing two ferrets inside and securely fastening their belts to prevent the ferrets from escaping. Each competitor then stands in front of the judges for as long as he can. Competitors cannot be drunk or drugged, nor can the ferrets be sedated. In addition, competitors are not allowed to wear underwear beneath their trousers which must allow the ferrets free access from one leg to the other and the ferrets must have a full set of teeth that must not have been filed or otherwise blunted. The winner is the person who lasts the longest.", 
"In the annual Bonny Beard Competition, the most elaborately styled beard, as judged by the patrons, nets the winner a night of free drinks. The losers have to shave their beards off.", 
"The Annual Greased Piglet Game requires that a 15x15ft pen is set up in the tavern. Participants pay a small fee to compete to catch a lard greased piglet in the quickest time. The winner keeps the piglet.", 
"Off in the corner a group is gathering around an intense card game. At the table are a wise cracking dwarf, an elf who invented ‘poker face’, and a burly half orc about to loss all him gold.", 
"An old, friendly sea-hag offers a free sample of stew, with more to come if the taster guesses the secret ingredient. The stew gives a positive magical boon on a DC15 CON save and a negative effect on a failure.", 
"As the party walks in they hear a Bard who is recounting there recent adventures as if he was there for all of them. (This is good for a low renown party as it adds an air of mystery).", 
"An old man can be overheard telling a ragtag group of mixed races about a dungeon. After some discussion, and a handshake, he hands them a map.", 
"An old man challenges you to a game of wizard’s chess. The wooden pieces are enchanted, gesturing and shouting as they fight, though you can’t make out what they say. It is fascinating to watch. The man promises who can win from him will win the chess set, though if you lose, it will not be easy to stop playing. He offers no further explanation. (If you lose, you become a chess piece, trapped in the game).", 
"It’s ‘Bear Night’. There are mounted bear heads on the wall, bear furs on the chairs and your drinks are served in bear-decorated goblets. After a while you begin to notice the bar is packed exclusively with hairy middleaged men, who are all acting rather familiar with each other…", 
"There’s a haggis eating competition. Winner gets free drinks 'till sunrise.", 
"It’s a busy night and the bar is packed. Suddenly everyone turns around as several squealing greased pigs are released into the tavern. They have numbers painted on their backs. The staff begins chasing them to much hilarity of the patrons. After a while, they have caught the pigs numbered 1, 2 and 4 but there is no sign of number 3.",
"All the windows of the Inn slam open as the candle light dims, only to be undone a few moments later. Then a small girl stands and shouts her apologies for the disturbance.", 
"Knife throwing competition! D20+DEX: 1-10 miss the target. 10-14 outer ring. 14-18 middle ring. 18-19 inner ring. 20 bullseye. 3 throws each. PCs can play each other or NPCs for gold / rewards etc.", 
"There’s a discussion going on at the bar. One of the customers seems to be underage, and the bartender won’t get them a drink, unless he sees something that confirms they’re old enough to drink. The customer has a way to prove that, but made a bet with the other customers, giving 10 gp to each one that gets it right, and takes 10gp from each who gets it wrong.", 
"A portal opens in the middle of the tavern. A man wearing pajamas comes out of it, orders a drink, and leaves through the portal, that closes behind him. If the players ask anyone, they will just say he shows up sometimes.", 
"The tavern’s owner runs into the tavern, saying they won the lottery, and will get everyone free drinks.", 
"One of the patrons has gathered a sizable crowd with their exotic pet and its tricks.", 
"This tavern exists in multiple dimensions, it has at least 20 different doors which connect to the outside world, but as you guessed, different ones. The owner is a mad wizard with the longest and most unkempt beard youve ever seen. Over each of the entries, there is a sign to where it leads. One of the doors is barred and kept shut at all times, the sign reads: dont open, dead inside.", 
"Tonight’s the local Battle of the Bards, where the prize pool includes a set of fine platinum strings.", 
"The Tavern menu has a ‘Mystery Special’. When ordered it is a large stack of pancakes covered in various fruit that looks like a big smiling face. When eaten the player is reminded of their mother/father/paternal guardian.", 
"A female drow in common clothes and a big hat (to block the sun) walks into the tavern and an uncomfortable silence ensues. After it is clear that the drow doesn’t want any trouble the tavern slowly goes back to normal and the drow woman orders a drink and sits down with a wealthy half elf merchant.",
"A wrestling ring has been erected in the middle of the tavern. The current champion drinks nearby, and accepts all challengers.", 
"An old drow tells stories about his long life in the Underdark. He tells tales of other drow, kuo toa, mind flayers, flumphs, and even a purple worm he encountered.", 
"The local beastmaster has arranged an animal show. He starts off with a raven, a giant frog, and a blood hawk. He finishes with a bulette, an owlbear, and a displacer beast. Each animal loves him like a family member.", 
"Inside the Tavern the party finds about 60 people stuffed inside this small three room tavern all gathered around the bar. The tavern just recently hired a barmaid to work full time.", 
"The Half-Orc chef near a large fire pit offers the party a sample of the roasting boar he has over a spit.", 
"A Tabaxi hunter set up in the corner offers to sell the party wild pheasants and other game birds for the Tavern cook to make.", 
"Once a month the neighboring warlords meet in this tavern to discuss… literature.", 
"Tavern is holding bar tending classes once a week to train new staff as well as supply competent labor to the noble houses – top of the class gets to pick their assignment.", 
"A polymorphed silver dragon walks in, orders a drink with no ice, and then he just frosts up his drink whenever. He only has one drink, and when he finishes his drink, you can see him switching from creature to creature , but only minorly.", 
"It is a roast night. Have the players take turns roasting either each other’s characters, or the DM.",
"A talent agent is holding auditions for the midwinter festival play. Bonus points for singing and dancing!", 
"After 1d6 drinks gravity seems to hold no sway over the bar patrons. Everyone starts to float and the regular drinks keep drinking on the ceiling as if this is a normal occurrence.", 
"A member of your party is mistaken for a local celebrity. People are constantly asking for autographs etc for the whole night.", 
"It’s the owners birthday! Reduced drink prices and free cake!", 
"The barkeep leaves a single coin with a tiny dragon at your table, he says ‘be sure to spend him quick, he likes to travel’ the dragon is friendly but will not separate from the coin.",
]
let chance = rollDice(100);
if (chance < 15) {
return "While you are there..." + searchArray(badTavernEvent)
} else if (chance < 30) {
return "While you are there..." + searchArray(tavernQuest)
} else if (chance < 45) {
return "While you are there..." + searchArray(goodTavernEvent)
} else if (chance < 60) {
return gameFind()
} else {
return "Nothing of note is going on"
}
}
checkEvent();
document.getElementById("Event").innerHTML = checkEvent();
};
function quest() {
function clearBoard() {
document.getElementById("Quest").innerHTML = "";
document.getElementById("Promo").innerHTML = "";
}
clearBoard()
let questBoard = [
"Help wanted! Chicken turns neon green when placed in moonlight.", 
"Wanted alive! Traveling merchant peddling sets of cursed sewing needles.", 
"Old Jeb the farmer claims his sheepdog had puppies, but they all have split tails and he doesn 't know their sire. ", 
"Snowberry bushes only bloom before a blizzard. Collect five snowberry blooms", 
"for an alchemist before the storm hits.", 
"A small pack of wererats have taken up residence in the city sewers and keep causing trouble for the locals.", 
"The party is summoned by a king to be his friends for a day.", 
"A cranky old man in town complains that his pocket watch is stolen, and he has his suspicions on who the thief is. The townsfolk say that he’s a senile old man who probably lost it.", 
"A farmer asks for help. His crops are constantly getting trashed. He wants the group/player to keep watch over the night. It ends up being that the poor farmers’ trusty scarecrow has been brought to life by dark magic. It is optional to buy or make a new scarecrow.", 
"A seemingly exorbitant amount of gold is offered on the message board to get rid of a 'house spider'. It turns out that it's about a spider-like mimic in the shape of a house. ", 
"The local priesthood is paying gold for water collected from the Opal Caves to treat a spreading fever.", 
"An apothecary will pay for certain herbs growing in the Frog Marches.", 
"Wanted dead or alive: Alfreck Sunderbeam. Wanted for turning all my cows into purple balloon animals. Will pay big!", 
"Blockade needed for Thunder Rose Lake. Water has turned poisonous and local animals are very sick.", 
"Debt collection", 
"Fake the death of (name)", 
"Find a way to break cursed item.", 
"Find a way to (kill, imprison, ect.)(name).", 
"Find missing person.", 
"Guard/Escort (person or object)", 
"A hunt for an exotic animal for a local tavern (a dire boar in this case as the hunt is less of the problem as figuring out how to transport a 2000 lb dead animal back to town)", 
"Looking into the rumor of gnolls raiding the outlying farmlands", 
"An ad for someone trying to sell trained guard/riding dogs", 
"A woman is looking for her husband who disappeared a week ago (he actually left her and ran away)", 
"Hired hands needed for apple picking.",
"That old women with rats in her basement.", 
"Turtle census(count the turtles).", 
"Divers needed to swim to the bottom of the lake and retrieve overturned boat.", 
"Old estate needs to be cleared of furniture and cleaned for sale.", 
"Alchemist needs some ingredient and is too old to make the journey themselves.", 
"Need help with a barn raising.", 
"Need night watch to watch for cow tippers.", 
"Missing chickens at the nearby farm.", 
"Security for a caravan", 
"General store looking to buy uncommon goods above market value", 
"Lost dog post written by a child", 
"Crazy wizard looking for test subjects", 
"Help retrieving a sacred sword", 
"Stores with coupon/deals", 
"Tavern advertising the entertainment coming through town 'Get rich quick' scheme", 
"Petitions to change a law", 
"Ad for someone running for office", 
"Army recruitment posters", 
"Warnings about a con artist", 
"Announcement for a big fight this weekend", 
"A minstrel looking for adventurers to tell their stories", 
"Missing pet pig! He answers to Mr.Locksley. Reward on safe return! (child's scrawl of handwriting) Accompanied by a cutsie pig picture along with whatever else is on the board there are dead/devoured remains of animals on the outskirts of town. The sewer maintenance crew refuses to go down into the sewers, the town's hiring new men. A series of other notices that lead to the conclusion that there's a monster in town. Mr. Locksley is actually a pink troll with a curly cue tail and a oinker of a pig nose. His owner is a small, adorable little girl.", 
"Tinker looking for parts(for some wacky machine?); maybe the party have seen one of these parts in the past? ", 
"Spell components needed(possibly for something sinister) ", 
"Looking for extras to perform in a play/talent show for visiting gentry (may allow the party access to local fortresses?)", 
"Slave(s) for sale", 
"Diggers needed for archaeological find!", 
"Estate sale (good place to pick up weird items) ", 
"Wanted : husband/wife for aging son/daughter; huge dowry!!", 
"Test subjects wanted. Free Food, Free Gold!", 
"Undead Outbreak inn Homeless Shelter Seek Astrid (last name torn off) (gets the PC 's to investigate to find the NPC.) ", 
"Report (Local Bandit Squad) Activity to Town Guard! ", 
"Have you seen this Goblin (portrait of a goblin Mooning someone and picking it's nose ", 
"Lost Minotaur, Captured Alive! (Local gladiator ring lost it's Minotaur and the group ends up finding it in a China shop ba-dum-chh.)", 
"Weekly Gladiator Tournament FAME, GLORY, GOLD! * Arena not responsible for lose of life or limb.", 
"Bodyguard Requested for Local Nobility", 
"Sanitation comittee looking for exterminator. (Were-Rats in local sewers)", 
"Farmer Druid needs assistance clearing out over grown crop (Druid magic summoned a bunch of Plant elementals) ", 
"Enforced Curfew in Riverwalk Park District. ", 
"Ghouls in the graveyard! Payment per ghoul head.", 
"Wanted: Wizard for children's birthday party. If interested please contact Lady Latimer with your qualifications. Thank you. ", 
"Plants from cave needed for pet lizard's diet. Inquire at the lizard-shaped house for further details.(Herpetophobes need not apply)", 
"Lost Cat - Taken by aspiring wizard who is confused about the nature of familiars. Accidentally summons a demon who he can't control.", 
"Help Wanted - Shopkeeper's Assistant [previous assistant disappeared, assumed left without telling anyone. But he was killed by assassins.] ", 
"Bodyguards Needed for One Night -Local leader and/or rich guy gets a tip that done hitmen are coming for him. They 've got time to set up defenses, and after some time a group of armed men show up. It turns out the attackers are actually officials coming with orders from the nearby <king?> to shut down rich guy's criminal enterprise. ", 
"Wizard seeking scribe to document his dissertation. Must have a steady hand and brew a mighty pot of tea. ", 
"Local meadery seeks help controlling honey drone population. Those with venom allergy need not contact. ", 
"Bard needed for Sweet 200 party. Must be elven. No fey-wine allergies. Bonus pay if you know all the words to 'Giant Jungle Snake' by Necky Mirage.", 
"Local farmer requesting for help capturing his cows that went missing. Investigating party notices that a big chunk is missing from the fence and it seems that a large creature (who happens to love eating wood?) came and took a huge bite out of the fence. ", 
"Schoolteacher needed for orphanage. Must like half-orcs. Must have even temperament. Latest vaccinations recommended.", 
"Reward offered for discovery of the source of the Olthark River.", 
"Mapmaker will pay for protection on journey. - Inquire at Hargen's, your friendly local map emporium.", 
"Wanted: wildlife expert with knowledge of forest giant mating habits. See Zappo at Expeditions, Inc.", 
"Pseudodragon free to good home. Includes a used set of leather protective gear. Very friendly, makes a great familiar. Come see Abrasane the Red.", 
"Company of dwarves requires one or several competent fighters to escort an expedition. Must sign non-disclosure agreements prior to hire. Find Dalvin Granitebeard at the Last Signpost Inn.", 
"Seasonal work: upcoming tournament needs message runners, assistants, and crowd enforcers. Speak to Bailey Mostaff at the Keep.", 
"Looking for laboratory assistant. Must know the 12 major constellations by heart. Knowledge of the 48 lesser constellations preferred. Inquire at the Royal Astronomy Society.", 
"Construction workers needed. Hard labor, good pay. Special bonuses for magic users. Come to Cathedral Square and report to construction site office", 
"Got ghosts? We ain't afraid of them! Professional spectre inspectors at reasonable rates. Find Peter at the Firehouse Tavern.", 
"Urgent! Need professional dog handler for upcoming dogsled race. Original handler mysteriously sick. Pay: large cut of race winnings, if any. See Cornelius at the Snow Tails Guild. ", 
"Looking for someone to deliver a wagon full of harmless supplies to the Captiol. 500gp+expenses. (It's a wagon for a group of weapon smugglers delivering to a group of rebels)", 
"My grandfather has been stuck in his room for a few days. Here is the situation, I came to the city to take care of him after receiving his letter. He had came down with a terrible cold and needed someone to take care of him. And so I came to the city and took care of him the past two weeks but he has not gotten any better. But now he had locked himself in his room and I am worried if he is okay. He won't open the door or talk to me but I know he is in there because I hear him walking around from time to time. PLEASE HELP! I can't get through this locked door by myself. Meet me at our address here in the city's residential district. Post haste!", 
"There's a hole in the roof, and I need some help repairing it. It leaks something awful, can't stand anywhere without getting wet when it rains. I've had a look at it up close, but there's no way I could fix it myself. If I had a few lads stop by my bakery on Swing St. around closing, we could get it done in no time. I have a few tools, but an extra hammer wouldn't hurt either. I'll be more than happy to provide you with lodgings for the night afterwards, with a 1/2 loaf of bread for each worker. Hope I get some help soon, or I may have to close up shop permanently and move back out to the country.", 
"A band of Hobgoblins intercepted my woodsmen returning from lumber collection. They are very crafty and have been holed up in an old elven city in the woods 3 tenday's walk from town. I need some adventurers willing to go retrieve my goods! WARNING: My lumberjacks were investigating a magical forest, so the nature of the trees and lumber is unknown. Proceed with caution.", 
"Bandits have been intercepting food and supply shipments destined for the new logging settlement located approximately 3 days ' north-west of town, at the border of the forest. We are requesting able-bodied adventurers and mercenaries to act as escorts for the next and final shipment. It is essential to the operation that these supplies reach the settlement.", 
"Our animals have started acting perversely. At first they were competing more for feed, but now they've turned aggressive against the people. We can't collect eggs, milk the cattle or shear the sheep! I fear it won't be long before the people start to be effected.", 
"Test subjects to try a selection of recent experimental brews. Most effects will be harmless, some few may be dangerous. Fatalities are not expected. Maximum 3 phials per subject with instructions for use, anticipated effects, and guaranteed payment for recovery (if needed). Subjects will be expected to provide a detailed log of duration, side-effects, and potential dangers. Report to the Blackened Tower 2 miles East of town. ", 
"I require the assistance of a party to find the wizard who turned my wife into a sheep and convince him to turn her back.", 
"Lately, may of the children in town have been complaining of nightmares. After a few days (weeks for some) of tortured dreams, the parents of these poor children find that they are missing from their beds. A reward has been gathered by concerned parents in the community for anyone who can either find the children or provide information that leads to their recovery.", 
"Help! I was transporting some of my harvest down a rough path, and when I was around half way to the next town, I was attacked my a raid of goblins. I would like you adventurers to retrieve my wagon. For your reward, I will give you ten gold pieces each, as it is all I can afford. ",
"Need help completing a human sized game of chess. Pieces move on their own. Chess game must be won to win my house back from this stupid witch. ", 
"A huge band of goblins has taken over my barn. They are trampling my crops and eating all the hay. I’m afraid they will start eating my pigs next. ", 
"Urgent request! Local wizard has turned my sheep upside down. I cannot get them to stay right side up. They occasionally turn rainbow colors. Please help soon!", 
"Seeking daisy melons, a local delicacy of (Town name).I went to (Town name) last summer for vacation and I have been craving one ever sense. I will pay you a large sum of gold for a wagon load of daisy melons. ", 
"Lost: my favorite blankie.I’ ve had this blankie for as long as I remember. I have not been able to sleep in 3 days (since it went missing).", 
"Seeking help making cake and cookies for a local wedding. My staff did not show up for work. Urgent request! Will pay for your time and talent!", 
"Convince a loan shark to forgive a mans debt Helping a poor lad win a race so that he can win the heart of his crush.", 
"Babysit for a friendly fey power - couple whose magically - gifted children love playing games like 'the floor is made of lava,", 
"don't let the balloon touch the ground', and 'freeze tag.'", 
"Light all the sacred shrine lanterns along a deserted mountain trail.", 
"Investigate the site of a meteor crash in the deep woods. ", 
"Track down a cow that broke free from the herd and return it to the farmer (alive)", 
"Convince someones child not to become a soldier/adventurer.", 
"Convince someone's parents that they should allow their child to be a soldier or adventurer.", 
"Take a lesson from a BARD and make a performance. ", 
"Use your spells to aide in a Play or performance.", 
"Look into strange happenings around town. (It's just restless kids/ teens playing pranks)", 
"Take some food/supplies to the orphanage outside of town.", 
"Help gather food for the upcoming celebratory feast (fruit from the orchard, grain or vegetables from the fields, herbs and mushrooms from the forest, etc.Choose what makes most sense in your setting) Harvest honey from a certain beehive with the sweetest honey. The bees there are notoriously ornery.", 
"Gather rare medicinal herbs to help the local healer brew a salve for Little Timmy who's sick.", 
"The town's blacksmith has broken his arm. Figure out a way to keep the town supplied until he's back on his feet.", 
"An NPC's party is a total snooze fest. Liven it up. Let your players interpret that as they wish...", 
"Negotiate with the local kobold tribe over mining rights and dues.", 
"Spy on the populace for a local lord, to find the insurrectionists. ", 
"Convince a proud weapon smith to make plow shares, instead of his legendary blades. (The blades end up sentient and cursed after so many battles.)", 
"Infiltrate a thieves guild, to unmask the new 'Puppet Master.' ", 
"Rebuild a home destroyed by bandits ", 
"Help a local cleric move a sofa ", 
"Re - light a signal fire on top of a mountain ", 
"Participate in a talent show ", 
"Challenge the village bullies to a game of basketball ", 
"Deliver secret letters for two star crossed lovers from rival houses. ", 
"Solve the murder mystery.", 
"Find the elven queen and get magical soil and seeds to heal the recently cleaned blighted forest.", 
"Win a tournament of carnival games.", 
"Win a poker/card/dice tournament.", 
"Deliver a love letter.", 
"Take a group to the school prom.", 
"Fix up a bunch of broken items in the shopkeeper’s place. ", 
"Be a member of the jury for a very grey case ", 
"Set up trade agreements between competing guilds to help alleviate the amount of sabotage in the business.", 
"Train a group of guards in how to anticipate the often unpredictable actions of adventurers.", 
"Host a support group for 'I think my child might be turning evil'", 
"Resolve a miner’s strike for the local magistrate.", 
"Save a servant’s job by finding the missing silver and prove she didn’t pilfer it.", 
"Raise funds from the tight-fisted local aristocracy to build an orphanage for the children orphaned by the recent war, to which the local aristocracy was heavily called upon to financially support by the Baron/Duchess/Queen, etc.", 
"Perform a puppet show for the children of a fey court to keep them entertained and out of mischief while their parents/guardians attend court.", 
"Collect living magical beasts for the local Countess’s Mystical Menagerie.", 
"Take the Baroness’s teenage son on a 'heroic adventure' as he is enamored with adventurers and longs for an epic quest, but is socially awkward, bad with weapons, clumsy, and so far unable to learn even cantrips. They are forbidden from placing him in front of any real threat. Do they put on a completely faux adventure or attempt to build his confidence and teach him skills? ", 
"Prove the innocence of a man accused of theft of a noble's jewels ", 
"Find a way to repair a large windmill that helps drive the town ",
"Put on a play for a group of orphans after the local actor troupe quit ", 
"Interview witnesses of a possible murder Interview applicants for the job of henchman", 
"Get alchemical supplies for healing potions to a remote town dealing with a disease outbreak ", 
"Deal with a noble's son bullying and throwing his weight around", 
"Plan security for a festival. They have to be careful, too tight and it's no fun. Too loose, and it can get out of hand. Include different areas where things can go wrong (party boats, shooting range, stuff for kids in the morning).", 
"A local orphanage is going to be shut down. The only way to keep it open is to win the cash prize at the local talent show/battle of the bands.", 
"A series of combat fake - outs where a siege turns out to be a festival, but the party needs to convince them to clear a path from the front gate. Then some marauders attack but it turns out they're just larping, but they are still bothering travelers, etc.", 
"Help Catsy Cline the tabaxi farmer do chores around her farm with lots of unusual creatures.", 
"Help a group of mourners put on a funeral. You'll need to play music and cater food.", 
"Try to beat the Fairy Godfather at a casino game to win a magic item. A woman's flock of prize chickens were spooked away by last night's storm. They look to be a different breed than most other chickens in the area. Help her round them up safe and sound and she'll give you a warm meal and a small reward.", 
"A young boy asks for help to find his runaway family dog. He gives you a shabby old blanket covered in fur and tells you it was her favorite. Under the smudges of mud and dead leaves, you notice finely embroidered clothes that suggest that he comes from a wealthy family. ", 
"A performer who was supposed to make an appearance at the tavern the party is staying at hasn't shown up yet. Either find them or stall for time so the crowd doesn't get bored!", 
"A house party in the city has been getting lots of noise complaints. Break it up and send the drunk guests home. A little girl's direcat got stuck in a tree.", 
"A wizard's familiar is going on strike. Apparently it doesn't like dying so much.", 
"Find a very small lost item. ", 
"Be bodyguards for someone who just wants them for the prestige. They are incredibly irritating but under no threat of violence. ", 
"Retrieve a blink dog or semi intangible animal.", 
"Write a diplomatic letter for an inept ruler to prevent disaster. Help out local farmers before the first frost rolls in .", 
"Babysit a powerfully magical infant. ", 
"Rescue a cat from a giant magical tree (its near the top) ", 
"Find and bring back a child lost in a maze (the maze changes and uses illusions) ", 
"Fill in for some performers who are unavailable (sick, hurt, left). Could be a play, stunts, music, etc.(lots of role playing, write an outline of challenges they'll encounter during it)", 
"Help someone find a loophole in a contact with a demon/fey ", 
"Gather rare ingredients for a particular perfume, poison, or potion for an alchemist.", 
"Help the local blacksmith with their next armor piece. ", 
"Baby sit a bunch of old time adventures with dementia. Their class abilities are still intact, they're just senile.", 
"Someone seeks help in solving a magical puzzle box they inherited from a family member. ", 
"Plant some false information, either by rumour, or in letter form. Make sure the correct people learn this information. Bonuses for making them believe it comes from an enemy of theirs, not the player, and is supposed to be secret.", 
"Help a local chef win a cook off by gathering his necessary exotic ingredients (marketplace, dark market, going and getting them yourself from the wilderness) ", 
"Go with a dragon studies professor to study a dragon's habits. ", 
"A changling has a sword pulled on them by their friends after telling them they're a changling.", 
"Declog a sewer pipe in the sewers beneath the city. There is a homeless werebeaver living there that is unknowingly building a dam, causing the blockage, during full moons.", 
"Track down a cowardly sentient ooze with a magic item.", 
"Win a poetry competition in a cave of intelligent pacifist orcs ", 
"Help a lone forest dweller unblock the mountain path from storm debris ", 
"Help an astral dragon return to its home plane.", 
"Help with rebuilding an intricate shrine so the settlement it's built around can receive the blessing of its god(s) once more.", 
"Proper reconstruction probably requires it to be partly made of rare materials using exotic techniques.", 
"Help the festival planners in preventing an important festival competition/election/nomination from being rigged.", 
"Accompany a famous explorer(s) as they seek to catalog new sights with the aid of 'fresh yet experienced perspectives'.", 
"Rescue a merchant caravan trapped in a stormy mountain pass.", 
"Tutor a newborn demigodlike being in mortal matters, so that it can blend in with the mortal family it is raised with.", 
"Help the local government investigate and assess candidates for an office of high esteem, requiring specific traits e.g.unwavering loyalty, honesty, a  propensity for pragmatism, etc.", 
"Bring a renowned artist to somewhere they've never been so they can become inspired once more.", 
"One of the locals owns a hyperactive blink dog as a pet. Recently they hurt their leg so need someone to take it for a walk.", 
"Recover several missing sandbags and get them to the town before the coming storm.",
"Abandoned house not so abandoned?", 
"Monstrosity terrorizes small village, mercenaries required!", 
"Unidentified corpses found in alley, towns guard desperate for information", 
"Missing children cases still increasing", 
"Traveling circus coming to town, hiring clowns", 
"Inaugural 'Battle of the Bards' competition! Inquire at the Bards’ College. ", 
"Adventurous Chef seeks volunteers to try bold new dishes (Not liable for food poisoning). ", 
"Local Wizard has turned himself into a pickle, needs help turning back. ", 
"Guards needed to help watch over art stock that's going to be auctioned off ", 
"A locol start-up tavern/inn/saloon/pub/anything else needs to hire temporary bouncers ", 
"A warning to all townsfolk to stay inside for the night (his is all the info that you need to give on this quest at the notice board. If they're interested they can ask around. If not, stuff is gonna happen later that night) ", 
"Issues with a mage's experiments are causing local plant life to die. ", 
"Authorites are requesting an escort for the entourage that is going to speak with him. ", 
"A simple noise complaint anout the alchemist from the southern side of town. People are having trouble sleeping. ", 
"Missing [[insert Item Here]]. Return to [[Insert Person Here]]. Reward of [[Insert Gold Reward Here]]. ", 
"A local blacksmith has claimed to have cracked the code on making the perfect set of armor and is willing to give a full set to anyone who can bring the needed ore. ", 
"A local farmer wants some assistance with livestock that should be giving birth soon ", 
"Cabbages disappeared again! ", 
"Boy bitten by box ", 
"Crazy lady thinks our mayor sucked her blood ", 
"Winter surprisingly warm so far ", 
"Mysterious barking keep kids awake at night ", 
"Museum closed until further notice ", 
"Prizes for best costume at party next week! ", 
"Research assistant needed, for details talk to NPC ABC ", 
"WANTED: Photo of old man, no additional information ", 
"Wanted notice for member of party, with barely recognizable etching of the PC. Crime and reward at DM’s choice. ", 
"Request for information about a mysterious blue box that has been appearing and disappearing around town, as well as the strange skinny man with floppy hair, big chin and a fez, who seems to accompany the box. ", 
"Cursed item merchant in need of guards.", 
"Need coin? Help local wizard test spells today!", 
"Antique shop, may or may not have mimic infestation, need professional adventure with gentle methods to help", 
"RATS. local labyrinth in need of fire mage, meet me at the old stump at midnight if interested", 
"Need teeth, you have teeth, I have gold, we trade, me at pond.", 
"Tired of farming? Looking for excitement?! Join the brotherhood of the fallen God today! Meeting are every Monday and Thursday at noon. Refreshments will be provided, first time members are encouraged to bring their own black robe", 
"A slab of human skin is nailed to the notice board, the message written in blood 'local woman seeks strong man, recently divorced and looking to meet new people' ", 
"Town festival in 1 week. Sign up now for the pie eating competition! ", 
"Help needed finding lost chickens. ", 
"Solve my riddles for a major prize (sort of riddle scavenger hunt) ", 
"King’s pet gelatinous cube missing again. Please give any information about its whereabouts. ", 
"Otto’s Outstanding Oddities grand opening tomorrow! Come in a get one free minor potion with any purchase! ", 
"Wanted: a person with experience with shoe-making and troll-speak or bridge repair and militant arts. (trolls maintain a series of bridges for years after agreeing for shoes. They have not gotten their shoes yet.) ", 
"Looking for anyone with experience of the certain 'grave matters' who will to bring my love back to me. Need not worry about my safety. Will be compensated handsomely afterward. (They are looking for a necromancer. Not to raise their dead spouse but a dead mistress.) ", 
"Needed: a spare pair of hands, a strong back, and a compassionate heart to help a dying old man (The man is a warlock looking to ditch his old body for a new one.) ", 
"Man-eating Monster on Loose: Alderman has set award of 150 gold and 5 fine goats for the person who ends the monster's existence. ", 
"Hav Ye Chikon. Expecc Rawerd. Lav rawerd atta caf's moth wit numbar ove chikons. Chikies nat hart ore aten. Dunt be Cheep. (A semi-literate goblin, bandit, or child has posted a ransom notice to get stuff from peasants for their stolen chickens. 'Have your chicken. Expect a reward. Leave reward at the cave's mouth with number of chickens. Chickens are not hurt or eaten. Don't be cheap.') ", 
"Massive cock stealing chicks and turn the villages other cocks rock hard (Naturally its a cockatrice causeing havoc and Quest giver may or may not get the inuendo) ", 
"Wanted: Bandits (Looking to hire bandits) ", 
"Private Investigator seeks mystery, will pay handsomely to those willing to create complex mysteries ", 
"Lost dog: Please help find my dog, answers to Fido, likes bones, 6ft tall, large wings, enjoys in-depth conversation. ", 
"Seeking mortal foes: testing of deadly traps and henchmen prior to opening of new secret lair. Enquire within. (A hidden lever on the notice board opens a trap door to a dungeon, under construction) ", 
"Sewer monster sick, need help getting medicine, shlumogurath is a asset to this town and we should all pitch in, its the least we can do for him", 
"The ghosts are back, graveyard keeper looking for help", 
"Goblin party rescheduled to this friday, bring your own ale", 
"Famer looking for cheap labor, necromancer wanted", 
"Man attacked by something in sewer ", 
"Noble's jewelry reported stolen, handsome reward ", 
"Caravans looking for escort between towns as increasing numbers of (insert campaign relevent enemy) attack merchant travelers ", 
"Town can't find source of rotting smell ", 
"The town's well was poisoned ", 
"Something important (Mine, Logging Woods, Farm outside town) taken hostage by enemies ", 
"Noble wants a most extravagant breakfast, only one thing will do ", 
"Sage wants old texts from cursed crypt ", 
"Relic from local temple has gone missing ", 
"Bounty, Xavras Thunderhelm escaped the local jail, likely to have returned to bandit hideout ", 
"Axebeaks threating local livestock, need X pheramone/item to keep them away (Alchemist/healer) in need of ingredients ", 
"Animals behaving strangely. (awakened, charmed, polymorphed sentient being, possessed, trained by someone) ", 
"Animals disappearing ", 
"Bounty on (creature/person/group) ", 
"Caravan in need of guards ", 
"Courier needed ", 
"Ghost sighting ", 
"Help breaking curse ", 
"Impartial mediator needed ", 
"Missing person ", 
"Nightwatchman. mysterious thieves keep stealing from my (farm, store, warehouse) during the night ", 
"Rare creature sighted. Reward for live capture. ", 
"Strange noises coming from abandoned (castle, fort, house, manor, mill, temple) ", 
"Help wanted, removal of demon stuck in pigeon. Reward Pigeon or demon (whichever suits your fancy) (With no other context or information) ", 
"The entire village of (insert village name) and all its inhabitants have disappeared from this world without a trace. Now only unspoilt woodland lives there. Be cautious ", 
"Bovere, give my belt back already. I know you have it. ", 
"A flyer that seems to be written on stretched human skin, the writing looks as if it was achieved through scarification (where it is cut into the skin and let healed) 'ones wish is only a simple deal away' and it has a large swirling symbol underneath the title. If the pc tries to raise awareness of this it seems to magically dissappear however if they take the flyer they can use it to summon a demon willing to make a deal in exchange for a wish ", 
"Local Man fell into river, Builders needed!", 
"A note, covered in blood, simply stating for the person looking at it to 'Cover your ears'. (Unsurprisingly, This is a note pertaining to a false Hydra. ", 
"A relatively fresh piece of paper states 'Heroes Missing, assumed dead, after giant silver spider enters inn; witness testimonies needed.' With further research, the party would discover the creature responsible to be a Retriever. ", 
"One Sign catches particular attention, the text simply stating 'Not a Mimic!' The results may surprise you when you discover that it’s not a mimic... not a regular mimic, anyways.. ", 
"An interesting paper on the board notes of a Local Young Noble reportedly being 'Possessed by Evil Spirit after spree of etherial robberies collect loot for the Prince; royal family baffled'", 
"A silk message is visible on the board, titled as 'Mayor’s dog turns out to be Blink Dog, city council not amused'", 
"Officially put up by the city council, one gold-brimmed sign raises a rather strange business offer; 'Collecting Flail Snails for city zoo, 5 GP per Snail Collected.' You’re relatively sure it would be hard to contain these creatures without having them bash through windows, but the pay seems tempting enough... -", 
"Huge rat problem in my cellar (turns out to be a single giant rat) ", 
"IT BEGINS. (pinned to the notice board is a single thumb. Serial killers!) ", 
"I need help with annoying mosquitoes (turns out to be a normal babysitting job for 3 children) ", 
"Bake sale tomorrow night at Temple of Fire. Boon Auction to follow. Raising funds for new Summoning Chamber. ", 
"Wanna do some 'Work' for a 'Fella In Need' locally? ", 
"A local inventor is looking to pay someone to help him test his armor. The armor works great, but it is so heavy and uncomfortable that it is pretty useless. Movement is cut down to 1/4 speed. The true marvel is his mounted ballista that he uses to shoot at the PC wearing his armor. It is magazine fed from the top and can fire rapidly as he turns a crank. But, the inventor is set on the armor no matter how much the PCs try to convince him to market the ballista. Later, the PCs can find this inventor in the wild, trapped by an owlbear or two. He is like a turtle trapped on his back. At this point, if the PCs help him, he is open to marketing the ballista.", 
"Multiple dissapearences in the Town Stage. Witnesses claim 'they were dragged by leeches'. ", 
"Giant Rat infestation in the sewers. Rumors of a 'Rat King' are spreading. ", 
"Entire mansion goes missing. A giant hole now is on the place.", 
"A very fancy flyer for a traveling merchant who has set up their cart just outside of town.", 
"A posting for a missing family heirloom promising a great reward to whoever finds it. ", 
"Pie eating contest, 20g entry fee. Winner earns a magical 'Bag of PieS' that contains one random pie per day. The pie expires after 24 hours.",
"‘Wanted Dead or Alive – Bonecrusher, Orc Chieftain to the south! Warning: very heavily armed and dangerous. Has many henchmen. Reward: 1,000gp’", 
"‘Missing: a large turtle named Hubert who has escaped from the Caster’s School of Polymorphing. Please return if found!’", 
"Chicken Wrangler Needed! Some jerks smashed my coop and now 100 chickens are loose. 1GP/chicken to return them, no questions asked.’ (Poster is True Neutral witch in old haunted forest; all the chickens have been enlarged.)", 
"Need men to form a small honour garrison for the banquet I am holding in my manor. Important people are involved, so discretion is mandatory. 200GP per person, payed upfront. No questions asked. (All the guests are vampires.)", 
"The book store has a shipment of rare books coming in and needs people to help unload them. Will pay 100gold per person and not responsible for any injuries incurred on the job. (Caution: dangerous magic and pet books around.)", 
"Exterminator needed: I’ve got a mess of rats in my basement. Bring me 10 rat tails in return for payment. (Listed address has no basement and owner has no rat problem. The advert has a typo and should point to a house further down the way.)", 
"Exterminator needed: There’s a bunch of noise coming from the attic. Like chains or moaning or something. It’s probably those damn raccoons again. I would have my husband look into it, but the lazy oaf up and died on me. Payment dependant on work done. (Listed address has no attic, but does have a basement with a rat problem. Murdered husband is haunting the house, bring proton pack.)", 
"Strong Swimmer Needed! My simpleton apprentice left my ore cart unattended on the bridge and the blasted thing tumbled into the river! Hopefully the ore is still in there somewhere, I’ll pay gold to anyone who can get me my ore!", 
"Sick Grandmother: My grandmother is sick and needs a shipment of medicine. Our normal courier has gone missing, so we desperately need it delivered. Expedited fee available with a bonus upon delivery (Grandma makes a mean elven bread.)", 
"Squirrel Hunting: A squirrel has been seen in town stealing jewelry from citizens. We think there may be more than one squirrel involved — they always head west after the theft. They need to be captured or killed; a bonus available if stolen items are returned.", 
"Earrings Stolen: My wagon was robbed by bandits in the eastern forest. Among the items taken where heirloom earrings that were given to me by my mother. Please find them. Reward available.", 
"TEST SUBJECT NEEDED! We at the Barrington Bakery (insert your own name) are looking for subjects to test out our new magical breads. We infuse magic into the mixing process for a, hopefully, tasteful bread. You will need to taste each bread, and have our scholar review the side effects. You will be paid per day.", 
"Lost Arrow: While practicing with a bow, my son lost a trophy arrow (he was not supposed to use). He was practicing in the Northern plains and thinks the arrow went into the forbidden forest. Please retrieve this arrow. As an alchemist, I will pay in healing potions.", 
"Goblin encampment: A goblin encampment has appeared in the Southern part of town across the ravine. They’ve been there for days and don’t seem to be aggressive, but we can’t be so sure. Find out what they’re doing — if they’re a threat, please dispatch with them.", 
"Wandering Skeleton: Wandering Skeleton seen on the outskirts of town. It appears armed with a sword, shield and horned helmet. Dispatch this skeleton and we’ll offer you 10% off anything in town.", 
"100 List: Help! Local bard needs assistance creating a list of 100 dirty jobs no one wants to do. A small payment will be available as well as your name as a contributing author in the book I’m writing.", 
"Kobold Flour: Local baker seeks Kobold Flour for the upcoming Monster festival. This specialty item can only be found in Kobold encampments. Will pay 10gp per pound (maximum of 100 pounds).", 
"The (Insert bar or inn name here) is looking for a bard to entertain the crowds on Thursday Nights (mug for a copper night).", 
"Merchants looking for armed security to escort us to (Insert town or city name here).", 
"(Insert townsfolk name here), our beloved mushroom forager, has not returned from the forest. He was last seen four days ago. Need help finding him(her?)!", 
"Lost mail! Important documents might have been intercepted. The currier I’ve been expecting has not arrived. Please inquire at the City Hall.", 
"The town of (insert neighboring town) has challenged us to our annual match of Shinty (or similar sport). Let’s show them who’s best, and get that trophy back where it belongs!", 
"Lady Clarissa will read your future in the cards. I know you will show up. Where am I? Don’t worry, dear. Fate will guide you.", 
"The Imperial Army needs your skills! Join us to fight the good fight!", 
"Koboliam Ore Needed: A local blacksmith needs Koboliam Ore, which is only found in the Myriad caves to the North. Once a Kobold stronghold, this abandoned cave is full of traps and possibly other dangers — will pay top gold for each block of Ore.", 
"Burial Escort needed: Our recently deceased father needs to be buried in the family lot, six miles north through the badlands. A small party escort is required in case of trouble.", 
"Bandit Kidnappers! Our beloved daughter has been captured by Bandits! They have not made any demands, but we want her back. They were last seen Northwest of the old tower — a reward for our daughter (alive), plus a bonus for the head of each bandit.", 
"Family Bandits! My son and his two friends have left the village to become bandits. Find them and teach them the error of their ways. Reward if they return — must be alive.", 
"Kubo’s Strings: Local bard Kubo lost his musical strings during an encounter with a small dragon. The dragon has the magical strings attached to it’s teeth. Please retrieve the strings and you will be rewarded with a +1 AC enchantment to your armor!", 
"Flying Monkeys: During a recent storm, Flying Monkeys came and took our poor family dog. They live in the Julliad mountains. Please bring back our precious dog — our children are lost without them. We don’t have much in money, but as farmers we can reward you with rations for all your travels.", 
"Magnificent Seven: Our villagers overheard bandits who plan on raiding our town in one week’s town. We seek seven or more strong warriors who will help defend us.", 
"Troupe of traveling bards need a few strong individuals to help schlep and set up our equipment on our world tour. Can pay in booze and lodging.", 
"Detail-oriented individuals needed to go door-to-door to market my magical floor-sucker-cleaner. Commission based.", 
"Need young fit person to shovel snow from my walkway (if high summer. In winter substitute with ‘mow grass’ or something else appropriate. Employer is an elderly individual from a far-off land who has enchanted their property to be more like their home country.)", 
"Book keepers needed! Not really. Bandit-wizards have been trying to steal from my personal library of arcane books. Need tough, preferably illiterate, bodies to defend collection until I can secure safer storage.", 
"Tower Demolition Sought: The four story bell tower has been deemed by the city council as a stain on the communities reputation, as it was built with “ill-gotten” funds by the rencently disgraced and now former mayor, Cornul Glassen. The council is offering 500 gold to anyone who can reduce the bell tower, which was dedicated in his honor, to rubble without loss of life or other property in the town square. Plans must be approved by council before work can begin.", 
"Come join us for the first annual bucket festival! Bring a bucket and you favourite drinks to join in the festivities. Meet out back the delapited house on the edge of town at any time. You know the one, you’ve seen it in your dreams.", 
"Needed bartender. Looking to employ a bartender for my inn, The crooked arrow. Must be able to listen to political rants on the slower days. NO GOBLINS", 
"The well water has started tasting funny, someone should look into that.", 
"LOST Young boy named James, he has been missing for over a week and was last seen going of to play by the river. Reward if found.", 
"Local spell caster looking for lab “assistant.” Intelligence not required, but a high resistance to pain appreciated.", 
"Mole Dispatch – a group of unusually large moles wreck our fields! We are in dire need of a someone who is getting rid of those pests. Payment in gold or products from our farmers market.", 
"Sheep Numbers Dwindling – We don’t know who, or what, is killing our sheep, but we cant ignore it any longer. Over the last three months, we found several mother sheep and their newborns dead. We offer 10 gold coins for whoever finds out what has happened to our lifestock and ends this from happening again. (A were-sheep has been killing the other sheep, can be found out when the heard is observed, all sheep go away when this particular one comes close to them, or when the transformation happens during a clear moonlit night.)", 
"A notice to those on hard times that the mines are hiring, the tag line on the bottom says “We’ve cleared out the danger that once struck our mine and threatened the safety of the miners, we are confident that resuming our operations shall be fruitful and safe for all.” (Underneath that is a hand written note directly under the text, “So much for your confidence.”)", 
"Deal of a lifetime! I’m willing to trade a lovely tin pot, painted with cornflowers and lilies (and showing a few holes, true, but that’s a plus, for you can add a few more and look at that, you’ve got a colander) for a cart. The cart needn’t be big, can even be tiny, in fact, just so that two, or better four, people could fit in it, with ample room for bags and sacks, if possible. Could be old, long as it rides well and has new wheels, and strong axles, so actually probably nothing made longer than a year or two ago would do. Leave a message with Bohddie.", 
"Cleric needed – Daughter Ill and Dying (A local father is worried because his daughter’s health has been rapidly declining. He needs someone with knowledge of medicine to determine what kind of illness… or poison or curse… is affecting her.)", 
"Adventurers needed! Our Kobold in our previous adventuring party is currently missing and is in possession of an ancient and dangerous artifact. Problem is, he ate it. Please return the artifact in tact! The Kobold (Skrazz) can be returned dead, alive, or not at all for all we care. 1000 GP Reward.", 
"Multi-Linguist Needed: While going through my pappy’s attic I found this really old map that I’m pretty sure leads to something cool. The problem is, I can’t read it! Pretty sure it’s Celestial, Draconian or Elvish cuz the letters are all curly. If the map leads to some sweet treasure I’ll share it fairly with you!", 
"Taste-Tester Needed: Lord _____ needs a qualified taste-tester for upcoming banquet to fill recently vacated position. Benefits include All you can eat food and drink, provided medical care, lodging and pay-per-taste. Dwarvish candidates preferred. Inquire at ______ Manor.", 
"A Muse-ment Please: My brother, the head writer of our musical comedy duo is in a rut. He hasn’t been writing any good jokes for a while and I just can’t play backup to another lukewarm song like “there’s gnome place like home”. He needs something hilarious and inspiring to jump-start his creativity again. I’m taking him to the _____ tavern tonight for drinks, and if you manage to orchestrate some weird and hilarious scene I’ll pay you 10g. (by the way, don’t tell him I paid for this, just say I owe you money or something I don’t care) -Billie Doobie", 
"FOUND: Stange child’s doll. Blue gingham dress, yellow yarn hair with blue satin bow, made of painted wood. Eyes are large and very lifelike, seeming to follow you around the room. IF YOU RECOGNIZE THIS DOLL PLEASE COME AND TAKE IT I’LL GIVE YOU 5G. -23 Wyverann St E", 
"LOST SHORTS: please, this seems silly, but recently my favorite lucky shorts have gone missing! I’m sure someone stole them but I have no proof. I need them before the big poker tournament tomorrow and I will pay 100g to whoever finds them! They are purple with green polka-dots and the back pocket has a recently-patched up rip. Also my name is written on the waistband. -Marty Martingale, #4 Lake Park Ave. E", 
"WHO AM I?: I woke up in a gutter this morning outside of the Hill Street Inn and Tavern. I do not remember who I am, where I am from, what my name is, anything. I have a large sack of gold on my person and I am currently renting at the Hill Street Inn and Tavern for the foreseeable future. If you assist me in regaining my lost memories I would be more than happy to properly compensate you, for it seems that whoever I am, it is a man of means.", 
"Local Tavern needs (at least one more) bouncer for annual all-you-can-drink QuaffFest Celebration tomorrow. Usual bouncer called in sick and can’t make it. Will pay 5s/hr and after your shift that evening all your drinks are free!", 
"BARD EXTRAORDINARE: Art is the purest expression of the soul, and no-one expresses themselves more eloquently than Clover Salvatore, the hottest Bard to grace the realm. The Golem Guardian newspaper has called him, “A fresh voice, Clover Salvatore will wow your tavern with his genre-bending style, and witty lyrics. A star in the making”. Send a pigeon and book him in now!", 
"FIRST CLASS MALE: If you need a message that needs delivering, look no further than this First Class Male. With reasonable fees and lightning quick delivery, it’s not just the devilishly handsome good looks that make this the best way to tell someone you care. Speak to Dorian for more information.",
"Help wanted t’ return me property: Yesterday some o’ th’ young neighborhood scalawags stole me carved wooden leg while I were pissed in th’ gutter outside th’ Salty Strumpet. I can nah chase aft them t’ git it back ’cause me backup leg be mor’n ghastly. If’n ye can get back me leg I’ll pay ye 10 gold, it holds a lot o’ sentimental-type meanin’ t’ me.", 
"BIG AWARD MONEY!! Near forest there is cave. In cave small monster. Need help with monster. WILL AWARD BIG MONEY!! (A barghest’s trap, prepared by goblins to lure adventurers in and devour them alive)", 
"Someone stole my chicken that lays all sort of metal eggs. Help me find it.", 
"My Family is about to find out about my secret. Good liars and problem solvers in need.", 
"The bridge collapsed again and I lost my wagon. Will pay good gold if bridge repaired, and more if wagon retrieved. Contact Arkwright’s village store for reward. (Twist: Goblins have been booby trapping the bridge to steal the contents of wagons.)", 
"What up? We’re three cool guys who are looking for other cool guys who want to hang out in our party mansion. Nothing sexual. Dudes in good shape encouraged. If you’re fat, you should be able to find humor in the little things. Again, nothing sexual.", 
"Missing pet! My pet has been missing since three nights ago and has not returned home. If found return to , whoever finds him will be rewarded greatly! (Twist: the missing pet is actually a small dragon.)", 
"Need basilisk eggs for experiment! Big reward!", 
"Missing: One (1) semi-intelligent skeleton. 5 feet 10 inches. Last seen wearing blue cloak. He was sent to the market for some groceries five days ago, and hasn’t come home. His creator misses him very much. 50 GP & four (4) Stones of Farspeech upon return.", 
"Love of my life! Please, I need your help to make me look cool in front of the love of my life, so that I can win her heart! I could never hope to win her by normal means since I’m poor. I will give you all of my life savings in return. Bonus if you look scary! //DM note: The plan is to have the players perform as crooks flirting and trying to pick up the girl and in turn be chased away by the contract giver to make him look cool.", 
"Need to make silver quick? Why not platinum! Rent doesn’t pay itself ya’ know! Find Raul Sonderheim and ask him how you can become your own boss and never have to work a day in your life! (Can be a quest to thwart a predatory pyramid scheme OR be the starting branch in a murder investigation once Raul is found murdered, likely by one of the people he recruited.)", 
"WORK FROM HOME: Easy money that anyone can do! Finally live your dream lifestyle! Be your own boss! Make thousands in your first week! Retire early! Don’t be left out!", 
"Open minded and discrete healer wanted. Must interview.: Despite the suspicious wording, the job is treating people from discriminated-against ancestries or with embarrassing deformities that have been persecuted, passed over, or financially exploited by other healing organizations. The pay is low, but you make solid allegiances. Word of your kindness spreads among the hidden downtrodden and you may find welcome far away.", 
"Sales assistant wanted. Incredible pay!: It’s a multi-level marketing job. The job poster gives you a sales talk about their wonderful liniments and gizmos. They do work, but they are overpriced. You have to make a bulk purchase of the items and then try to resell them for a profit. You are unlikely to find the buyers needed to turn a profit and are stuck with too much stock.", 
"Horsebreaker needed! Inquire at the Post Office! The job is preparing young horses to accept the saddle and harness so they can be ridden or pull carts. They must also be taught basic commands and gaits. The job is successful if the handler can get the horses to calmly accept riders and obey simple orders.", 
"Do you think you know your gems? A grand test awaits at Nappe and Klippe’s Emporium. Only those who truly appreciate mines and minerals should apply! A local jeweler’s outfit acquired a large stock of specialty mineral samples and gems from a flash sale of unclaimed shipments. They need them identified but want someone, preferentially a dwarf, who isn’t going to undersell them. The first part of the job is a basic knowledge test and then they move onto the unusual samples. They pay in wholesale gems of the player’s choice.", 
"Music tutor: My son Stevie wants to be a bard, but the kid has absolutely no talent. I want to enjoy my time at home without the shrieking of his horrible electric lute destroying the peace. I’ll pay you 10g to give him some lessons, and if after a couple his “Music” becomes less painful, I’ll give you a 100g bonus. Contact John Harris at 75 Leyton Ave.", 
"Help! My mother-in-law is coming to town for a visit and I need someone professional to inflict me with some awful disease or other affliction so I have an excuse to stay in bed and not interact or be around her. Please no afflictions that cause perminant damage or death. Mildly life-threatening ok. Meet me at 10pm behind that bar that smells like old goat. You know the one. 50g upon disease delivery.", 
"Help recovering property! This is your local bard Razzle, and if you’ve seen me lately you know that I haven’t quite been myself. The truth is I lost my prize peacock feather hat in a wager at the Lusty Mermaid two days ago. The man who won it from me said I could pay him back for the value of the hat, but when I went to the inn he was staying at I found he skipped town without even paying his tab! (And I found out he cheated at that game of cards by the by) Please, I need a skilled ranger or another who is good at tracking to get back my hat! I’ll pay you 4,000 gold to go with me to get it, and I’m willing increase the price to 5,000 if our quarry proves elusive.", 
"URGENT: It is my little pookums birthday and the entertainment cancelled! Anyone may apply as replacements at the magistrates estate.", 
"NEEDED: Someone competent in the ways of word to berate, yell, and speak ill of me. Willing to pay. Discretion is key. Meet me during the night 2 alleys up from the pub in order to discuss terms.", 
"LOST: 3 peg legs, a hook, 5 eye patches, and a talking parrot. If found please return to “The Luckiest Crew” down at the pier.", 
"HELP WANTED: Poor old widow requests the assistance of any strong and able persons to rearrange some furnishings. (She is a witch in a small town of elderly folks that help her trick strong strangers in order to preserve their own lives.)", 
"MINIONS NEEDED – Local Lich Looking for Less than Lawful Lackeys. References not required, no paladins. Full training and benefits given.", 
"Fence need painted. Good pay. Contact Sythi at the Inn. Twist, the fence is 10 feet tall and almost a mile long.", 
"ISO: Skilled toymaker, it’s my daughter’s birthday and she wants a teddy. I can compensate for any materials you use. This was posted by an orc and her human husband, there’s an address near the bottom with a smiley face. The 6-year old half-orc wants a GIANT teddy.", 
"IN NEED OF DURABLE IDIOT, WILL BE WORKING WITH IMPOSSIBLE GEOMETRIES. IDIOCY NOT NEEDED BUT DESIRED. BRING FRIENDS. snacks provided! (This was wrote incredibly hastily by a desperate wizard, and his wife. The words “snacks provided” are in much cleaner handwriting toward the bottom, obviously added as it was being posted.)", 
"My brother an me want candy!!! (This note is barely legible and is tacked at the very bottom of the board.)", 
"Hey, we’re having a party and we need booze. Bring any and all you can carry. (Posted by some broskis at the wizard college. There’re about 200 in need of whatever alcohol they can get their hands on.)", 
"Having trouble stocking all these books! Will pay for some big and strong people to help me! (This was posted by a small old woman who owns the local library.)", 
"A set of seemingly innocuous symbols is carved into the side of a barrel underneath the board, all in Thieves’ Cant. The symbols are being used for a purpose they’re very much not meant for, and the message is patchy and uncertain. “Dangerous Area.” “Owner not home.” “Owner is Vigilant.” Meaning: One for the rogues! The local thieves’ guild has found that their missions in the area have ended… poorly. Their new recruits are raving about some kind of spirit, and the veterans insist that something just isn’t right.", 
"Need demolition help: A demolition company is looking for outside help to clear out and then tear down a vacant house. The reward can be money or allowing the players to scavenge what they find inside the house. (What the company doesn’t tell the adventurers is that no one will do the job because of the powerful stench coming from the house. Exploring the house reveals a locked(mechanically or magically) wooden door leading to the basement of the house. The basement contains 1d4 Dretchs accidentally summoned by the previous owner.)", 
"Mimic hunt! Mimics are running rampant throughout the town. Find and kill 2D6 mimics. 1-6 mimics gets 100gp, 7-11 gets 300gp, and 12 kills gets 500gp.", 
"Being followed by crawling claws. Kill 1D4 crawling claws. Reward of 40gp.",
"House is overrun with rats. Exterminate 4D10 rats and 2D4 dire rats. Reward of 450gp.", 
"Help find my lost pet cat! Reward of 3D10gp to anyone who finds him.", 
"The baker has put out a poster, looking for someone to deliver pastries to the mischievous yet kind faeiry dragon that watches over the town from its lair in the woods outside.", 
"Looking for riddle maker. You make riddles, we buy ’em! For more information contact your local Wizards Association.", 
"WANTED: Internship with seasoned adventurers. I’ve admired heroes all my life and want to try my hand at it! I’m hardworking, loyal, and a team player.", 
"Victimless Instigators of Loot Extraction is seeking henchmen for transportation of merchandise. Some risk is involved. Must be capable of intercepting and stopping pursuers. If interested, head to Church of St. Deegho and ask for Carmen.", 
"Help! My good friend Smolik Droweater has been trapped! My scrying reveals he is stuck in a 10-foot room. He has a chest of valuables with him, but needs help getting it and him out of the dungeon safely! Come to the Tower Tisential if you are willing to help! -the Wizard Quinn.", 
"Seasoned adventurers needed! Writer/Bard here, tell me the tales of your great adventures, I need some inspiration for my books/songs. Payment will be determined by how good your stories are.", 
"Just bought the old mill outside of town. But there’s something living in it (make something up). Will pay 50GP and free milling service for a year to anybody who clears out the infestation and makes it safe for our family to set up!", 
"Help settle a minor dispute between two noble Elven houses! House Alendrian is looking for adventurers to help draw the domain lines with the House Walopez border. If you are strong of arm and fleet of foot, inquire at the Dovestail Manor.",
"The lord of the city is rumored to have been killed and replaced with a doppleganger. A local guard thought he saw the lord change skin, but he can’t be sure. He approaches the party for help with the matter.", 
"A townswoman has been hearing strange rattling and moans coming from the abandoned house next door. She asks the party to investigate.", 
"The local blacksmith tasks you with bringing back (1d10) silver or from a nearby mine that roaming gnolls recently took residence in.", 
"Walking around the city, your party notice many of the citizens are missing one or two fingers.", 
"The market is buzzing amd filled with people arguing. It appears that all hens in the coty stopped laying eggs, and has driven the price of eggs sky high.", 
"A local farmer asks the party to either scare off or kill a pack of wolves that have been terrorizing his cattle periodically.", 
"Two opposing tailors each have half of the finest pair of pants ever created. You have been hired to repair the pants and reunite the halves.", 
"A local dancer complains of screaming at odd hours of the morning.", 
"The library has been infested with small mimics disguised as books. Exterminate them.", 
"Rumor has it that the local librarian is secretly a dangerous lich/vampire. Investigate.", 
"A bard has been found dead in an alleyway. Investigate.", 
"A young boy has a small pouch of copper stolen from him by teenage thugs.", 
"Through less-than-reputable channels, the party hears about a plan to hunt a small roving group of purple worms. The local crime syndicate wants the precious and hard to obtain organs and blood from the worms. The local city guard wants the location of the nest discovered and reported and nothing more.",
"A noble requests that the party deliver a small package. Around ten minutes after the package is delivered, someone approaches the party and asks where their package is, providing valid identification.", 
"A city watchman requests the party’s help in setting up a sting. If the party agrees, the operation begins, but when the target arrives, at least one member of the party recognizes the target and believes them to be innocent.", 
"The owner of an herbalist shop hires the party to descend into the city’s sewers and gather ingredients, including an organ belonging to a creature that should not rightly be living in the sewer.", 
"A wizard/scholar shows the party some maps detailing the locations of lightning strikes in the city in the past few years/months/days. There is a strangely perfect circle of lightning strikes around a small, inconspicuous area. An orphan is attempting to learn magic, and the spell he’s attempting is much too powerful for him.", 
"A local organisation ask for your help to find and eliminate cult influence from a variety of districts.", 
"The mayor asks you to help them with a zombie problem.", 
"A rash of political assassinations has sweapt the city council. The only other connecting thread is the same calio cat being seen at the scene.", 
"A massive sinkhole has collapsed the market square into the sewers. The local urchines claim seeing a shadowy tower and a glowing rainbow mist rise from the hole in the middle of the night.", 
"A grandly dressed man or woman of significant weight shouts at the adventurers to stop a young thief that ran off with a basket of hers.", 
"A local bard has been abducting local pets and harvesting their tendons for lute strings. A young orphan approaches the party and asks them to rescue his cat, as it is the closest thing he has to a family.", 
"The party is approached by a hunched man with an awful, hacking cough. His face is obscured somewhat by a hood, but he asks the group for some medicine or healing, preferably in his own home.", 
"A townsman claims to have seen starved, pale humans dragging others away, and the players see that exact man get dragged away moments later if they dismiss it.",
"An increasing amount of people are being found dead in their bed with bite marks in the neck. Rumours of vampires are going around, however the bite marks of the victims correspond to their own arrangement of teeth.", 
"It has remained mysteriously cloudy above the city for the last couple of weeks and dead birds keep dropping out of the sky at night.", 
"One day the players find that their favourite tavern is just straight up gone. It has been replaced with a normal living house or two. Nobody in town, not even the people who visited the tavern regularly, can remember the tavern.", 
"A small child asks you to help their father who has been injured in an alley, but when you arrive, nothing is there. The child sits crying and hugging nothing but air.", 
"All of the Clergymen in the town have fallen deathly ill. The town elder asked the party to investigate this phenomenon.", 
"A young child approaches the party and asks that they find his missing siblings. Their last known location was the decrepit chapel where the city outskirts meets the forest.", 
"A sweet old lady stops the party in the street and asks if they can go and buy things on her shopping list for her. She hands the party a bag of gold and the list. Upon closer inspection, the items seem to be ingredients for a deadly mass ritual.", 
"A mad alchemist set up shop next to your favorite tavern. The whole establishment reeks of foul eggs and other unpleasant things. The tavern owner asks you to help convincing the alchemist to stop his work or leave.", 
"A plague of rats has struck the poorest streets of the city. They seem unusually focused and vicious. Seek out and quash the infestation.", 
"A tavern has burned to the ground with thirteen people inside, and inside was found the bodies of ten dopplegangers.", 
"A local smuggling gang has recently begun battling against a tribe of Grung in the sewers- they have appealed to the city guard for help, and frogs have been seen in concerning numbers after recent rainfalls.", 
"Rumors abound that the local magistrate is a devil in disguise- but in fact, they are a polymorphed dragon.", 
"An ancient fey ruin has been discovered beneath the city, and green-eyed deer and wolves have begun running through the streets at night, howling and hunting down those who don’t get inside fast enough.", 
"A child has fallen ill and the local herbalist needs some very specific ingredients but can’t leave the child unattended, the herbalist requests your party to get them.", 
"A string of missing children have been happening in a sector with constant reports of a “dragon” in the sewers. The local guild council asks the party to investigate.", 
"A large tiger is running loose in the market. If the party kills it, the noblewoman it belongs to emerges from the crowd and demands immediate compensation.", 
"A bit of food sold to the party (cake, pie, soup, etc.) suddenly has a humanoid pinky finger found within it.", 
"A string of young noblemen have turned up missing, and the only connection is that they all visited the same brothel.", 
"A magnificent circus has arrived in town, but during the last night of the festivities the castle will be robbed.", 
"An old ship thought to be lost at sea for many years suddenly returns to port, seemingly no worse for wear. The crew and passengers are completely unscathed, and no one has any idea how long they’ve actually been gone.", 
"The poorest and youngest citizens start to drown on dry land and in open places, skin soaked and slimey. There is an aboleth somewhere infecting the oldest, deepest, well of the city with its slime.", 
"Somebody is “kidnapping” all the bronze statues in the city. Its either a military faction building a massive hidden cannon, a were-rust monster, or a mad mage perfecting an animate object spell.", 
"The Guild of Actors and Musicians has challenged both the Illusionest Guild and Bard College to a contest of pomp and pagency for the next festival. They need the party to sabotage the competition.", 
"The city guard has lost two female members undercover in the brothel district. Not missing but giving up law and order in favor of vice and hedonism There may be a succubi flipping all of the agents being sent.", 
"The local brewer’s latest batch of high end whiskey has been sabotaged/cursed by fae. The five barrels already sold need reclaimed quickly and quietly less the brewery’s reputation suffers.", 
"Half the city has become overgrown with dense vegetation overnight. The city watch is busy defending the rest of the city from wild animal incursions from the newly-formed woods, so the Captain of the Guard asks the party to investigate the root of the matter.", 
"An infection seems to spreading in the slums. City officials deny any proof of it and guards no longer keep watch close to the slums at night. You are beckoned into an alleyway by a hooded figure who implores you to find out the fate their loved one who went into the slums to heal the sick.", 
"A local sports team have gotten inexplicably unstoppable in a very short time. Rumours of something amiss range from dark bargains, to an amazing halfling herbalist (and everything in between). Collect clues, follow up leads, and get to the bottom of it!", 
"The water in one district has suddenly become highly flammable. The local government want to find out why, and want it stopped. Players find that a group of anti-establishment rabble employee a pyromancer to make this easy to hide accelerant, but something went wrong.", 
"The entire upper class are loosing their hair and want you to get to the bottom of it.", 
"It’s election time for the new city Mayor. To everyone’s surprise, the Kobolds that live in the city sewers have put forward a candidate for the job…", 
"A local cult of demon worshippers have recently been seen helping the community, feeding the homeless, and housing the poor. The city guard is SURE they’re up to no good, but can’t PROVE it.", 
"The village drunkard is stuck in a Groundhog day loop, and uses his knowledge to mess with the party for 24 hours, as it’s the most fun way to spend repeating eternity.", 
"A distressed-looking housewife implores the party to kill the giant rats living in her basement. Once down there, however, the party finds hallucinogenic mushroom spores that cause them to see their greatest fears. It’s otherwise a perfectly ordinary basement.", 
"A peddler with a cart selling odd wares, such as jugs that transform water into oil and pots that heat up without fire, has been seen wandering the streets at night. However, the items he sells often malfunction or explode.", 
"A talking rat has been hustling the three shell game in dark alleys, cheating locals of their gold. It’s rumoured it wears a hat.", 
"Every full moon, the cats of town gather inside a deserted house. What are they planning?", 
"A local merchant asks the party to deliver a note across the city. When they return for payment the merchant doesn’t remember the party. An investigation will show that his left ring finger is now missing.", 
"The party sees a local elderly woman attacked by a large half-orc man. He steals a small pouch filled with the leaves of an exotic plant. If the party returns the plant to the woman, she rewards them with a dozen cookies made from the plant they returned to her. After consuming the cookies the adventurers find out that the plant is this worlds equivalent to marijuana.", 
"An Ooze that was planted in the sewers to clean them and deal with the rat problem has grown ginormous and started to split into more Oozes.", 
"The party hears about a man getting murdered last night. The perpetrator is a spirit and there were plenty of witnesses, but only about half saw the spirit. Every night another victim is taken until the group can unravel the secret.", 
"A man is confronted by a mob for not being able to control his sorcery.", 
"The local Thief Guild is fighting a Feud with the local Gypsy family for the drugdealing control of a district. The governors know this and get money for looking the other side, a lot of money, but their feud might recall unwanted attention over the city and his pocket, he ask your help in the matter.", 
"A brewer of the second best ale in town believes the most popular brewer has made a pact with a demon to enhance her wares. If the party investigates, they find that all the brewers in town have unknowingly made deals with the same demon, which has plans to adulterate all their wares and take control of the townsfolks’ minds.", 
"Workmen are sledgehammering tombstones from the local cemetery for material to repair the cobblestone streets. The dead are not happy about this.", 
"A statue in the town square has disappeared overnight and footprints (apparently from the statue) are found leading to the Magicians’ quarter. It could be a prank or something more sinister.", 
"A drunkard begins to screaming at the party, claiming they robbed him. When searched by watchmen, the man’s purse turns up in their pockets.", 
"Bodies have begun appearing at the exits of the sewers with bite marks on them. Rumors of cannibal cults, lycanthropes, and other such things have begun flying around. You are hired to investigate the matter.", 
"A seemingly mad doomsayer is yelling in the streets that the sewers are a gateway to the Abyss. Every day this is ignored, d8 demons of a challenge rating of 1 or lower will crawl out of the sewers at night. Every week this is ignored, the challenge rating increases by 1.", 
"In the big garden of a powerful family, the party notices several woodland critters acting strange. Upon further inspection, they appear almost human in their mannerisms. If the party inquires about the family, they learn that they are rather known for being proficient in charming and polymorphing…", 
"A single member of the party notices a young boy in an alleyway with a third eye in his forehead. The boy telepathically tells the member to come find him in the graveyard.", 
"The party is stopped by a traveling salesman, that frantically insists on handing a spherical object wrapped in cloth to the party.", 
"Eleanor, an heiress to a wealthy baron’s estate, is found murdered in the old meatpacking district. Gretchen, her identical twin, plasters the city in posters offering a bountiful purse for the head of her sister’s killer. Meanwhile, a woman claiming to be Eleanor swears that it was her sister Gretchen that was killed, and is offering a matching reward to anyone who can uncover the truth.", 
"A beloved statue has disappeared from the center of town. An alderman asks the party to find it, but the more they investigate, the more people insist that the statue never existed.", 
"Animate slimes and oozes are seeping out of the sewers.", 
"A long line of ill townfolks are waiting impatiently outside the apothecary’s house, they been there all day and either the apothecary or her assistant are answering the door. The thing is that the apothecary kept some creatures caged to farm their poison and somehow, they were freed.", 
"The party encounters a burning building and must rescue several commoners trapped inside. Later, they discover that this is one in a string of arsons.", 
"The party must earn the respect of a local group of toughs by competing in a bracket-style fighting tournament. However, some competitors have been meeting with unfortunate accidents…", 
"Several locals have committed uncharacteristic, violent acts. Each claims to have been commanded to do so by a benevolent deity in their dreams.", 
"A talking cat follows the party, promising to take them to a magical place where wine flows like water and gold litters the ground.", 
"The building of a new road has earned the city the ire of the local druids.", 
"The local miners have gone on strike, demanding higher wages and better equipment. The Boss wants your to remind them who’s in charge.", 
"A portal to hell/the abyss opens in the town square, but nobody else seems to notice or care. Demons are now shopping in the market.", 
"When the local innkeeper is rebuilding his hearth, a removed section of a wall reveals a human skeleton embedded in the masonry, covered in strangle carvings.", 
"The group sees a Drow named Vicepenny with a red balloon trying to lure a child into the sewers from a sewer drain.", 
"A monkey steals and runs off with one of their hats. Will return for a piece of fruit.", 
"An employee in a lumberjack costume offers the party free samples of jerky from a nearby tavern counting as one daily ration.", 
"A group of mean geese begin chasing any dwarves or gnomes in the group. Geese are protected under the city rulers.", 
"A peaceful Hill Giant sells his intricate lace patterns. People wonder how he does it. Upon interrogation he reveals he does most of the work himself but his two Pixie roommates are always waiting for him to go to sleep. The lace over your face lets you get a good night’s rest no matter where you are.", 
"A hippy elf sells a single dragon scale necklace with your name on it for 1d6x10GP.", 
"The party gets a coupon for one free lesson “For You & A Friend” at the local Fighting Pit. They have to pay for their own uniforms.", 
"Ever since the ascension of the new baron/burgher, criminals have been taken into the keep and never seen again. The captain of the guard knows that the keep should have run out of room in the dungeons long ago, but he hasn’t been allowed inside to see them.", 
"A public execution is taking place in the town square, the town is split on whether the accused is actually guilty.", 
"A house/shop in the middle of town has vanished entirely, as if it were just erased from creation. A strange scent and magical residue permeates the premises.", 
"A very belligerent (and often drunk) old man is causing problems in town. The hangup: it is the burgher’s dearly beloved uncle who remains an extremely proficient fighter in his advanced age. The guard can’t apprehend him without serious injury to the man.",
"TAVERN JOBS", 
"Little girl having night mares, looking for adventures to gaurd her bedroom door at night from monsters. 10 gp  (Hag in the forest is visiting her slowly turning her into a hag.)", 
"What looks like a missing person quest, but turns out to be a little kid trying to find a date for their single parent", 
"Help! I lost my owl bear and Its oddly aggressive i need it back alive. please bring to Owl Bear Farms.", 
"'i lost my gold dragon scale frying pan.'", 
"Rescue my cat from the goblins in the forest", 
"I found a weird book with weird looking shapes on it and its glowing blue and spawning dead geese everywhere", 
"Courier service needed. delivery to the Forest Queen, needed by the Spring Equinox. don't open the package, don't let the wolves catch you. 6000 gp… with proof of delivery ", 
"Two cacti are throwing a coconut on a major highway. If the coconut is taken forcefully then the cacti get mad. But they will willingly play catch", 
"I want the shoes! They have them! Go take them! But only the left ones! No right shoes! Right shoes hurt my ears! Please read in insane voice", 
"investigate a pond. when players get thier they only find a goose. if it is disturbed and honks it summons a horde or cr appropriate monster. /goosehydra ", 
"ex wife of the high wizard in town needs adventures to surve child support papers to wizard.", 
"a wanted poster with a picture of one of the party members but under a different name. the person that is wanted may or may not be the party member.", 
"I, a local merchant, need help tracking a potion I sold to someone this past week (it may or may not be faulty and potentially fatal)idk who bought it", 
"A young girl says her cat has run away. Turns out she is actually been dead for (length of time) and the cat leads them to almost certain death.", 
"'Lost pet children' (it's the children of the family pet) written by a child.", 
"Something keeps coming onto my farm at night and stealing all my fox. leaving me with no fox to give. Help me find my Fox. ( fake job)", 
"'we buy silver' posters and when the players get to the store it's run by two lovely werewolves", 
"locate the disappearing glowing moss", 
"Got a new Blinkdog puppy, now hiring trainers!", 
"Help! My grandma is out of control and needs to be taught a lesson.", 
"I need three orc tusks. tusks must be from a full grown male, preferably warriors. for magical contract reasons they must be given willingly. ", 
"My Blink Dog doesn't blink? It just keeps staring at me", 
"Platemail Armor accidentally given intelligence, escaped, hiding in woods. Return to Artificer Jackson Cortland for (gold cost)", 
"Gonthar needs help finding Gonthar's pet Squirrel, Gonthar.", 
"I think my pet mimic ran away. Her preferred shape is a children's toy box. If you see her please bring her home safely, I'm sure she's terrified.", 
"'I can't find my banana! Find my banana!' Old man Jackson who forgot her ate banana and that he issued the quest", 
"Exorcism required to clear out cursed family tomb! ", 
"help me find out why I am always brused and sore in the morning", 
"forest grew in our town overnight. sometimes it whispers jumbled prophecy. trees also magic resistant. we're slowly being driven mad. when they get there itd be fun if the 'prophecy' was just a poor attempt at poetry by the forest", 
"last spotted at the gate of the nine hells.", 
"My farm animals are going missing (turns out to be violet fungus)", 
"I'm currently stuck in a well. if you would be so kind as to bring some food and drink to the well it would be much appreciated", 
"A must find my spectacles. Finds the person and the spectacles are on their head.", 
"My goats keep disappearing and I keep finding these pits filled with pink and blue goo. Please figure out what's going on. I need my goats.", 
"Help wanted, Charm resistance mandatory", 
"theif stole my co-worker please capture the theif and bring me back my co-worker. ( co-worker is a flesh golem.) ", 
"kobold mother of 47 requires a sturdy babysitter, reward for find. sitter will also be compensated.", 
"Help my 500 year old grandfather find a date", 
"I need a bundle of sticks from the eldest tree in the nearby forest.", 
"Help needed must sacrifice 47 chickens to the llama god", 
"Search for the magical fleece￼", 
"need a tear drop of a dragon", 
"Reward 500gp fake paladin ", 
"Help! Three lizardmen won't stop singing horribly at midnight and it keeps me up. Get rid of them or help them get on pitch", 
"need help removing a fire chicken from local farm. ", 
"Help! My lover has been kidnapped by Dragonborn cultists and needs to be saved! (Lover is powerful leader of cult)", 
"can someone please teach my how to tie my shoes laces please- it's been 30 years and I'm still clueless ", 
"exterminate rabid dogs that attack people on the road Rabid dogs are actually mutated and demonic and have been trained by a local cult", 
"lucky rock. Randy probably took it, he's a jerk. start there.", 
"lost my pet pseudodragon 1000 gp to who ever finds them.", 
"'help! need candy for godly duties! just dont tell my mother'-bims the fusha fey dragon with an a god complex and obsession with candy and sweets-", 
"Help! A bunch of Kobolds (and/or goblins) have taken up residence in one of the barns on my farm and are killing and eating my animals.", 
"Help wanted! Sir Knothole is getting old and wants to live out his glory days. will pay you to pretend to be bandit gang for him to defeat.", 
"Troublesome dragon near town. relocation service requested. absolutely no killing please. 6000gp after swearing on truth spell the dragon has moved… ", 
"crypt guards wanted! a string of grave robberies has occurred under the last several new moons. 100gp to any that can catch the culprit 'dead' handed", 
"A farmer outside town has been requesting help finding his missing chickens the only evidence of something we are going on is holes underneath chicken coop. ", 
"'Take a break. relax. don't stress out to much. come have a drink at Talia's pub!' With a free coupon for a drink.", 
"Lost Hand! Last see harassing a rat near Krooked Kraken. If found, please return to Lefty.", 
"mighty warriors needed. Serious inquiries only. my sister has been taken by a cult and I need her retrieved. 800gp alive. 3000gp dead", 
"Huge Gelatinous cube sliding down the hill. Not sure where it came from but seems to be heading for my tower. Please stop it before it gets here!", 
"Sewer system maintenance needed. Experienced ratters preferred. 5sp per giant rat tail, 1sp per dozen rats. corpses required for pay", 
"Keen investigators needed! children behaving too well, bewitchery suspected. any evidence paid for in gold and favors.", 
"Iron Golem gone mad at the blacksmith's. Trapped it in the basement but it's shaking my house down! Smash it and you're welcome to the scraps.", 
"A giant rat stole and ate my wedding ring! Find the damn vermin and return what is rightfully mine.", 
"Help! I'm a single father. My daughter just started pooping blood from her front butt. she is possessed by a blood demon. God fearing cleric wanted.", 
"A tavern owner requests that you steal the recipe of a stew that a rival tavern owner uses bc it originally belonged to his grandfather.", 
"'rabbit hunters needed' 'ruthless rabbits raid local farms causing carrot shortage'", 
"The local quilting guild needs 8 yeti pelts for a commission", 
"HELP! Mimics have invaded my library and disguised themselvesas books! Kill the Mimics, but don't destroy the books or the Library ", 
"Help needed! Local cheese gone missing. Reward negotiable. Cheese is the local gold guard drake or muletant cheese elemental (lava elemental)", 
"Local Tavern needs help exterminating Large Rats! Rats are feral, have scales, incredibly aggressive! (Rats may be drakes, barkeep unsure)", 
"A quickling has gotten it's hands on some boots of speed. It's been stealing everything that's not tied down. For the love of God no one can catch it.", 
"local kenku thief wanted for identity theft and multiple armed robberies, wanted dead or alive. Kenny's name is bang and they are a gunslinger", 
"Please kill the bear in the cave. Then make it a trap, the whole cave is full of primal bears.", 
"To marry my daughter. Ask the bartender about Grizzly Softpaws. ( daughter doesn't want to be married.)", 
"1 year contract - cast teleportation circle on a spot near this town everyday for a year so we get more people to do our quests", 
"I require the tongues of 42 chickens for science! Please deliver them in a fortnight", 
"a large shrub has sudden appeared in my property", 
"need actors to fill the role of soldiers to help impress hobgoblin for courtship.", 
"Retrieve a statue called The Blue Diamond Monkey from a temple in the jungle. Will be rewarded with rare items in return.", 
"'Lost Pet Wanted Dead or Alive Reward to be discussed.' Necromancer lost his bone golem; it's name is J. Roger and he likes alchohol.", 
"Retrieve a ￼wyvern egg ￼for a master chef", 
"tavern owner needs help with finding a woman to love big heart but im part dog. ", 
"need test subjects to gauge the effectivity of new potion", 
"a gelatinous cube has taken a residence in my barn and need it removed", 
"Need a mercenary to kill the mercenary that I hired to kill the first mercenary", 
"adventurers needed to fake a wedding/kidnapping so my father in law will stop insulting my fiance! possible dance battle. free food included.", 
"Please retrieve undergarments. Lost near the local goblin nest after some drunken carousing. May or may not be held within the goblin nest.", 
"i think my father is in a cult? Please help??? (The father is actually just in a BBQ club for fellow dads)", 
"Adventurers needed! My daughter has run away to marry a dragon. I would prefer that she doesnt marry a sugar daddy. Please get her home w/o bloodshed", 
"A farmer has put in a request to find his missing sheep. We also have reason to believe that this 'sheep' is not a sheep at all and actually a Druid. ", 
"House haunted?! Furniture keeps appearing and disappearing. Pet has gone missing. Food goes missing as well. Need help.", 
"Help. My pet pseudodragon escaped 10 years ago and I found it again. it's the size of an elephant and it REMEMBERED MY NAME. I RAISED A RED DRAGON AND I DON'T KNOW WHAT TO DO ABOUT IT.", 
"all the cheese has gone missing please find it", 
"Basement is full of fungus please kill it", 
"A glowing entity has been stealing my fish from my net. It glows a blue-green color, then disappears with my fish! (Glowing squid)", 
"'Experiment 2603 has gone missing. It may still be in the city. please capture, but don't kill it... also, use extreme caution. Thank you.' ", 
"Workshop infested with shadow demons (Smoke Mephits). 50gp on completion; No looting! -Foreman Luellan", 
"Hired security needed for our weekly dwarf fightclub. Be warned lower armor is recommended, drunk dwarfs tent to fight with no honor. 100gp each body ", 
"Local Farmer and son who are not the brightest can't seem to tell where their cows have been disappearing off to.", 
"help escort the amnesiatic necromancer back to their retirement home",
"Angry Imp stuck in my basement. Please remove. Don't break anything. (It's really a drunk goblin that's painted red and slippery cause paint is wet)", 
"Please Help. I want to go home. (The island is a Zaratan from Tome of Beasts)", 
"TONIGHT ONLY- at the docks. plot twist it's a siren obsessed with the little mermaid and only sings under the sea.", 
"GREETINGS! My cat has gone missing. She is especially hard to find, so be careful! I lost her while on a stroll on the northernmost hillside! Thx!", 
"a bounty letter for 100 gp for any information on who stole a potato from a local farmer", 
"Must be willing to handle a long... hard... 66 years of service.", 
"Dragon scales. Form a live or dead dragon.", 
"Possessed knife-wielding chicken is holding my family hostage. Any amount of gold, just get the thing out of my house!!", 
"500 GOLD .remove wild magic zone 300 GOLD .cursed monk killer strikes again 100 GOLD .living weapon searching for partner", 
"Two bards are playing outside my house all night. Please make them stop. Or at least teach them how to play.", 
"big 'ol gators in my backyard pond, they took my dog bring back the gators head for my revenge. Also bring me back my dog.", 
"Lost my brother in the woods while camping please bring him back. (turns out their brother is a talking skull that he dropped)", 
"I've been cursed. I've tried cleaning my house, but everything I clean gets dirtier.", 
"Please help my elf friend get a date! She lonely and needs help!", 
"'Please help, local troll stole my cat to eat'", 
"A fey that wants a lich lover", 
"Need the fifth eyestalk of a Beholder. Not the first, not the 6th, the FIFTH. And the next smartarse who brings me all of them is getting incinerated!", 
"quest to defeat dragon. but its really a lizardfolk with good intimidation.", 
"rescue pet cat from a tree. (Cat happens to be a displacer beast)", 
"A young girl has a messily written quest asking to help find her pet, she makes it seem like a cute puppy..its really a dire wolf.", 
"The salamancer is requesting for someone to hunt his arch enemy the newtromancer reward is 1gp", 
"'Need help collecting various items for new home *By replying to this notice you are in no way bound to a contractual agreement.' -Just a chill guy who needs help running errands. -Doesnt explain why all the items PCs collect are extermely occultic", 
"'Lost my penny's in the woods need strong adventuress to help me find them.... they are rare - reword is one of the penny's'", 
"collect deathkiss blood for spell components no killing. medicine checks to use special syringes.", 
"Farmer needs a 'perfectly normal ladder' retrieved from his orchard. no one dares get close to it. DC 15 Wisdom save to approach it.", 
"A request to find and kill a specific goose that lays in a cave outside the city. it is a very terrible goose.", 
"My baby beholder shrank my kids", 
"My neighbors will not stop trying to one-up each other with lawn decorations, and I cannot sleep because of the noise. make it look like an accident.", 
"HEWP WIF GOBINSES. a local group of kobolds are requesting help dealing with what they think are goblins, but are drow setting up to attack a town", 
"My crush is amazing, but I don't know how to approach her. Please pretend to attack her so I can swoop in and she'll fall in love and get married", 
"FREE SISTRR my name is neyn, my sister is mean and please take her away. shes probably delicious. (Nyen, an orc, is luring adventurers for gear)", 
"Roach infested basement. BIG ONES ", 
"RATS IN MY BASEMENT. npc has been hearing rats in their basement, only there is no basement. the second theory players come up with is true.", 
"Missing golden cat.......it's a sphinx", 
"it has come to the attention of the merchants guild that someone in town is actually 3 kobolds in a trenchcoat, these duplicitous crettens must be stopped any solid evidence should be brought to the chamber of commerce forth with.", 
"37-Golem lost. Help Golem home. Golem pay gold.", 
"my cabbage cart keeps getting destroyed by a teenage monk and his friends plese stop him", 
"'Gnimle wants adventures to get treasure. lots of treasure. come gnoblin cave. not goblin. no goblins here. Just treasure!'", 
"Cat herder needed. Posted by elderly business owner who brings a horde of cats to local houses to remove mice.", 
"help an old woman carry her jug full of coppers to the bank so she can cash them in.", 
"(from a former bard) to help get his lucky coat back from his ex which is a ___(insert sexy monster here)", 
"local necromancer lost his skeleton. skeleton is docile and listens to instructions. party must bring skeleton back in good condition pays okay", 
"Need 4-6+ brave men/women to scratch my domesticated hydra's many necks so it doesn't get cranky", 
"A serious one to fill out the board. Wolves have been stealing sheep and a lot of them, daily. They leave an obvious trail but nobody has return", 
"There's are 50 cats in the town and the poster is convinced that no one owns a car and he thinks there an uprising that's about to begin (he's right)", 
"Help getting cat out of a tree. Plot twist customer and cat are a Druid couple.", 
"Low level - Investigate a string of thefts. Of undergarments. ", 
"A old hag lost her walk house? (Inspired by baga yaga) or a old wizard lost his spellbook in a library filled with book mimics.", 
"Need help wrangling prized chickens. (Chickens = giant eagles w/o flying speed) chickens can't be harmed and spook easily and are aggressive.", 
"turned into potted plant, details below.", 
"Please help me find my son! He is a dragonborn child with strange scales! (The client is three kobolds in a cloak looking for their friend)", 
"raving chicken that kills other chickens and uses the bones as weapons", 
"COME OVER HERE AND BREAK MY ROCK (the rock is secretly a golem)", 
"Collect kobold ear wax for its amazing medicinal properties.", 
"Collect wild honey. Seams easy. But the honey is found in hives built in certain trees at least 100 feet off the ground by a species of giant bee.", 
"Horns women. Will pay for Mindflayer Partner(s).", 
"I will pay YOU to take this Cursed Dagger. it keeps telling me the date of my death. I buried it and it came back.", 
"a pair of skeleton Brothers keep trapping and feeding a town of humans very bad spaghetti. Although outside of that they seem very friendly and always let the humans out the next day", 
"I'm trying to grow a forest of my own trolls. Can you get me 10 troll pieces. The bigger the pieces the more your pay", 
"cursed Candy Castle popped up just outside of town. attention all passing adventures! Waves of monsters are plaguing us. it's really inconvenient", 
"'HELP! Me wife got stuck arms deep in our cow, who then ran off with her.'", 
"I need the head of a hag that lives in the forest. she has been coming onto my farm and slaughtering my livestock", 
"an alchemist needs 15 Red Dragon Scales for their potion experiment.", 
"My owl shifted into a lady! I need a magic user to change her back!", 
"A little girls rubber ducky is lost. A wealthy family is paying good money for it to be returned. It's easy to find but possessed by a demon.", 
"Babies of all species have been temporarily going missing at night, then returning where they were three days later unscathed…", 
"'Fight me.' -Kyle, human", 
"Hello Reader! my aunt is in need of a baby sitter for her 4 sons and 1 daughter, while she is out to a ball in the neighbor city (name) take care", 
"Kill monkeys. Like...30 monkeys. And retrieve all of their hearts and return them to me.", 
"my ex killed my cat. Mildly inconvince them as much as possible for 8 hrs.", 
"help! my potatoes field is haunted. nothing will grow! it has to be ghosts! (they havn't actually planted anything)", 
"Dear Adventurers I require 10 left shoes of various sizes. Just the left ones should there be a right shoe it decreases your pay. 50gp", 
"A Murderhobo Warforged Barbarian and Drow Owner is on a rampage killing the innocent. Stop the threat.", 
"DJ Lich is having rave and needs adventures to as guards to stop other adventures from ruining his party", 
"Earth elementals blocking trade road (they're tiny elementals that keep stacking rocks in the way when people aren't around)", 
"badger keeps harassing me and breaks my beehives. please help.", 
"hive of bees the size of volkswagens in a farmer's barn. they are pretty docile but they dont want to leave because of a grove of giant flowers", 
"WE REQUIRE... A SHRUBBERY! AND A SECOND! Planted next to the first, so there's a little path…", 
"Dwarven bartender needs brave volunteers to test his 'new brews and mixed drinks.' que Dwhatever for misc. drink and effects.", 
"I need help getting eggs (warning harder then sound their dragon egg DM picks color and how many but the party don't found out till they get there)", 
"Looking for handsome and beautiful adventurers to escort me to a fey party. I am located in the bog. Yes I am a Bog witch.", 
"accidently lost my glasses in a pocket dimension full of random junk", 
"Hi! I'm leaving town for a few days for business, and need help babysitting my pets. They are well trained, loving Owlbears. 3 adults and 2 children", 
"I'm looking for a large horse that's been wandering the forest! this horse is a kelpie willing to aid the group for a price, exotic flesh.", 
"a hastily drawn note that says 'help I have angered the squirrels' and nothing else", 
"Looking for a bard to learn from. Teach me your ways.", 
"local lord/lady requesting adventurers to gather a rare fruit from nearby mountain (guarded by monsters) (fairy tale tribute).", 
"transportation of Yeti's milk from the neighboring city.", 
"Request for manticore spines preferably with barbs still attached. Also if available will buy the venom sac if intact.", 
"sewer cleaning", 
"Request for information on bear fighting rings.", 
"Looking for possessed beaver named Kevin, may be a trapped Druid.", 
"help my beast breeding farm requires help when they go the farm to help the person running the farm is a gnome and the beasts are large/huge monsters", 
"3 kobolds in a trenchcoat robbing people in the park", 
"clean out the local outhouse reward is what ever they can find. ", 
"House haunted?! Furniture keeps appearing and disappearing. Pet has gone missing. Food goes missing as well. Need help.", 
"Lost donkey, answers to the name Candace. 2,000 gold reward. Dead or alive. (The donkey ate a rare magical item and then mysteriously disappeared)", 
"a bunch of pixies are turning a local farmers pumpkins too big for use and are using them as homes", 
"REWARD! Any who have information or know whereabouts of suspect to the Werebear Attack out by Ironleaf Outpost. Please inquire at the Guild!!",
]
let promo = [
"Magical Memory Deletion – Will delete unwanted or unhappy memories for a price.", 
"Magical Tattoo Shop – Get tattoos imbued with magic, either gives stat bonuses or allows the use of a once daily skill.", 
"Magical Fireworks Makers – creates fireworks that are much more impressive than normal fireworks, and twice as big.", 
"Magical Teleportation. Teleport where you need to go.", 
"TelEx. Teleport Express will deliver your items wherever you need overnight.", 
"Magical Animal Breeder – Breeds magical animal companions for mounts or pets.", 
"Dream Delvers – Allows someone to enter their dreams and create whatever they want inside.", 
"Magic Item Hunter – will find specific magic items and sell them to you for an increased cost, depending on the rarity of course.", 
"Medium – A necromancer that will become possessed temporarily by the spirit of a departed loved one for a fee.", 
"A wizard who casts fly on people who pay and want to fly.", 
"A wizard who uses Major Image to recreate a scenario or for a play.", 
"Merlo’s Moving Company – uses Mage Hand and Telekinesis to move your boxes.", 
"Restaurant that uses magic to create catered food for events.", 
"An ‘Adjuster’ – Will magically alter your appearance for a price. Can change height, teeth, skin color, eye color, etc.", 
"Soul Infuser – Infuses a soul (either one they sell, or one you happen to have laying around) into an item of your choice. I imagine it as either for instance infusing a kangaroo soul into your boots to allow you to jump better. If you pay enough you can summon the soul as an ethereal familiar.", 
"Druidic Express – A high level druid who has designated stations(trees) to teleport people around for an aged oak leaf ticket.", 
"Warlocks Vaults – A high level warlock who runs special vaults. Creates your own demiplane for whatever use you want, they won’t ask questions but ask for payment.", 
"High level cleric that casts commune on your behalf.", 
"Fire Brigade – mages that use magic to put out fires & rescue people trapped in fires.", 
"Lamplighter – mage that uses magic to light streetlamps in towns & cities.", 
"Mage Hunters – mages that specialize in tracking down & capturing mages that use their powers for criminal endeavors.", 
"Magical Tattoo Shop – provide magically linked tattoos that allow people to communicate telepathically.", 
"Magical Telegraph Office – Offices are located in cities & towns. Messages are sent & received by magic. If the recipient of the message isn’t present in the office, Then the message is delivered by courier.", 
"Sculptors – mages that use shape stone to create their works.", 
"Weather Mage – providing rain for farmers & guaranteed good weather for outside events.", 
"Wind Mage – speeds up sea travel by providing a constant wind.", 
"Swap delivery; when ordering an item, you receive a clay likeness of the item that will swap places with the completed good.", 
"Makeover Mage – will change your gender, even if you just came in to ask for directions.", 
"Laundry Service – A wizard with modified spells like Cone of Fold and Detergent Ray offers to have your clothing cleaner than the day you bought it.", 
"Summoned Stories – they specialize in the magical aspects of construction. Magically built buildings at the highest end (might take a year or more). Magical traps and secret rooms at the mid-range. Magic windows or toilets at the low end.", 
"Items lost – they specialize in untraceable getting rid of things. Depending on the thing this could just be casting disintegrate or could involve sending things to destructive planes like the center of the plane of fire. They say they won’t do people or bodies of sentients, but you have your doubts.", 
"Smells By Design – magical perfumes.", 
"Better Friends – they will cast awaken on your pets. No guarantees.", 
"Vital Images – creating magical paintings that are photo realistic and may move or include sound.", 
"Waukeen’s Walk In Clinic – all cleric spells available for a price. Including resurrection.", 
"Witches Broom – a house cleaning service that specializes in using prestidigitation to get the house crazy clean.", 
"Goat Coins. Originally invented as a toy for a sorceress’ daughter, Goat Coins contain one to three charges that allow the user to summon a mount for 24 hours. Goat coins are ideal for children’s parties, but packhorse, draft mule, giant charging chicken, and Heffalumps are also available. Prices subject to the size and value of the mount, as well as the number of charges in the coin. (Mounts cannot fight and will dispel if injured.)", 
"A temp service that hires out undead servants (don’t worry! Our servants signed consent forms way in advance before they died!) to perform menial labor.", 
"The War Zone – A shop that sells magical trading cards which are used for dueling. They are enchanted to create illusionary images that actually fight each other. There are also tournaments held in the shop, and the champion wins a rare magic artifact as a price: a golden eye that lets you read your opponent’s thoughts. (only works during a card battle)", 
"Earwax Removal using a very small Mage Hand.", 
"Flood Cleanup using Telekinesis and Mage Hand.",
"Dog Walking using Mage Hand.", 
"Magical beast walking/pet sitting.", 
"The Finder – will track down who or what you need. Is basically psychic, so supplying an item important to the target will help.", 
"Balthasar’s Bedazzling Beauty Boutique – A high mage who was once tormented for his appearance. In younger years he had a split lip, one eye with no iris and a semi developed nose. Being so shunned by his peers he focused manically on his studies and after many years of training became a spectacularly gifted transmutation wizard. Balthasar has since used his powers to transform himself into ever more perfect depictions of beauty and is the most sought-after guest for the high-end dinner parties in (whatever town you put him). He makes a fortune with spells such as seeming and modified versions of alter self (much like professional makeup artists), but his best-selling service is true polymorph. For the small price of a couple hundred gold (scale to your economy) he changes fat people into thin, does chin and nose jobs, gender swaps, anything you can pay for.", 
"Witty Comeback Assist – The next time the player is insulted, a perverse and demonic trickster will remotely whisper 1d4 cutting responses in the players ear. They might even be able to divine personal secrets of their victim to make the remarks that much more legendary.", 
"Magical Services locator – this ley line reader can tell you how to find many of the other services on this list by studying the vibrations of the magical ley lines. All their directions will be given using invisible ley lines as landmarks. They will give the customer a special ley line candle that burns blue when it is near a ley line. But the candle goes out a lot.", 
"Magic Smack – For a fee, this vendor will cast an untraceable magical smack in real time, on any target the customer has a piece of (hair, skin, finger, etc.). The smack does no damage, but in Common a rude disembodied voice says your choice of, ‘You’ve been smacked!’, ‘That’s what you get!’, or ‘Don’t make me come back!", 
"Supernatural Tracker – For a small sum, a local druid offers to track anyone of your choosing in the local forests. He employs creatures on land and air to stealthy track a target for up to 24 hours. A scribe will transpose the animal’s description and location of the events on paper for a small extra fee.", 
"An “effects” seller who casts enchantments on clothes to make them sparkle or appear on fire.", 
"Magical Tattoo Remover, transfer or wipe away a tattoo or similar marking from the body.", 
"Divine investment/broker services, diviners who observe and modify markets to get the best results for them and their clients. This business can get rather hairy when different firms or individuals seek opposing results.", 
"Last Will and Testament, necromancers who use their trade to provide closure to family estates (as long as the corpse is intact). Living wills are not accepted.", 
"Divine Winds Acupuncture and Massage, a parlor that focuses on healing and enhancing the body by channeling the ambient magics of the world through key points in the body.", 
"Clothing mender uses magic to repair and tailor clothes.", 
"Magical match maker, the girl you like doesn’t like you? Time to change her mind with some enchantment.", 
"Translation service using Comprehend Languages. They literally trade you the book for another one that you can actually read. For a small fee of course.", 
"Anti- Surveillance/ Security – Magical surveillance can be a nuisance. This Private Mercenary Group doesn’t fight for you but will design and install methods of keeping your home safe from Scrying, Divining magics, and intruders.", 
"A prostitute offers you a magical fun time, in reality they are using modify memory to make you think the best time of your life. Nothing of the sort really happens to you.", 
"Last Chances – For the exceedingly wealthy, 1000 gp is a drop in the bucket. Why not spend it keeping yourself safe? For the cost of the components and a small fee, we cast Contingency, keyed to whatever spell you want!", 
"Twendel’s Traveling Travel Agency – A wizard named Twendel travels around on foot to various towns bringing along with them a box full of vacations in a jar. After paying a small fee the client picks out a jar, each jar having its own terrain and what level of difficulty they would like their vacation to have. The wizard then shrinks down the clients, places them in the jar and after a predetermined set of time releases them from the jar either having enjoyed a relaxing vacation in a tropical paradise or battled their way through an orcish stronghold to claim useful artifacts. Based on the difficulty of the jar the price increases but the wizard also stocks the more difficult jars with better loot.", 
"Sending House – A large building, full is Stones of Sending that each go to different cities, acting as a relay, will send a message for a small fee.", 
"Lawson’s Legally Binding Legislation – Magical contracts whose contents must be enforced.", 
"Druidic Gardening Service – They use plant magic to give you lush foliage and natural topiary. No more patchy lawns.", 
"The Rite Choice – Mages in the business of performing funeral ceremonies for the wealthy, complete with interment and sealing of the tomb with your choice of curses for any who might come grave robbing. For a fee, they’ll also lift curses for family members who have decided they want to pawn grandma’s ring after all.", 
"Sleep helpers – A group of mages cast sleep to help insomniacs or people that need a nice rest.", 
"Emergency Food – a dedicated magic-using chef will use ‘Create Food and Water’ to instantly make food for you, although it’s pricey and there’s a limited supply! (Of spell slots)", 
"Hidden Magic Item Store – the owners have an illegal list of magic items bought from shady connections. Only through thieves’ cant can you identify the store and order a magic item. Otherwise, the store seems a normal store.", 
"VSM Arcade – a team of wizards have mastered the Programmed Illusion spell and have essentially turned their workshop into a ‘VR’ arcade for PC’s. They can fight hordes of monsters (or DM can get more creative with what they can do) and perform spells and abilities without cost or rest without being in any actual danger. Costs 10gp per hour.", 
"Body Mods – A mage will alter your appearance to take on the characteristics of different creatures. Fur, fangs, claws, gills, bird eyes, even wings if you have the coins.", 
"The Auction of Many Things – An Auction house that specializes in obtaining artifacts and magic items throughout the multiverse. The cost may be expensive, but the various artifacts are well worth the cost. You may feast your eyes on the Book of Asmodeus one day then the next day is an artifact that gives you insight into the draconic prophecy.", 
"Speak with Well-Read – using something similar to Telepathic Bond but with a potentially longer duration depending on how much you pay; these wizards will act as translators or on-call assistants for nearly any intellectual problem you have. They bill more if the customer exceeds a certain number of questions per minute.", 
"Boss Music – they’ll put a spell on you. Specifically, they’ll give you the ability to play one song or other musical arrangement of your choice (no action required) at will. The song emanates from your location and can also be turned off at will.", 
"Sloomba? Roomslime? The name is a work in progress, but the wizard presents a small slime. This magically created creature will move slowly around your house casting prestidigitation to keep things clean and maintained! And for the adventurers, I have a travel model! Basically, one installed in a custom backpack. This kind of magical labor-saving creature will revolutionize domestic life. Presto-slime?", 
"Imagined Intimacy – a perfectly legal way to have the very realistic illusion of any kind of fantasy you could desire – just speak to the slightly sweaty wizard behind the counter, fill out your Fantastic Fantasy Form(tm) and head to one of the rooms in the back. Your Intimacy Awaits.", 
"Alms Aplenty – A food bank run by a fairly exhausted cleric and their disciples. Constantly creating food and water for the poor and making sure it’s distributed fairly.", 
"On The Mend – For a small fee will cast mending on any object brought into the store.", 
"Frosty’s – A shave ice stall that manages to never run out of ice even on the hottest days of summer thanks to the proprietor knowing Frostbite.", 
"Zone of Trust – A marriage/ relationship counseling group that one can go to and be ensured that your partner will not be speaking any lies within a 15ft radius. (The can also Calm Emotions)", 
"Allie’s Appraisal – An antiques appraisal store that will be able to Identify the object, Detect Magic, and Comprehend Languages that may be written on your piece.", 
"Dr. Feelgood’s – Not a real doctor. He is, however, a washed up one-hit-wonder bard who can Cure Wounds for a small fee.", 
"Magical Cleaning Service – Enchanted tools and prestidigitation. Please do not leave apprentices alone in the room.", 
"Dr Drenzel’s Dentistry – A half-orc who doesn’t actually fix your teeth but creates beautiful decorative metal or gemstone caps and bands for all sorts of teeth or tusks.", 
"Manpower – Need a few extra hands for menial labor? We provide golems that can do a wide range of physical labor jobs.", 
"Tunneling & Mining – Mages with shape earth & shape stone.", 
"The Ice Mage – providing ice whenever & wherever you need it. Ice cubes, ice blocks, a frozen pond, or even ice sculptures.", 
"Body Doubles – An illusionist that can make it look like you’re in two places at once. they can also make someone look & sound like you, so you can be seen somewhere that you’re not. Great for party tricks, alibis, or confusing assassins.", 
"Soul Jars – keep the soul of whoever you like in a jar. No questions asked.", 
"Pet Translators – Druids and rangers casting speak with animal to let pet owners communicate with their pets", 
"Adventure Tours – Will teleport people to places like undersea ships they have made breathable and give interactive tours", 
"Magical Confections – All manner of candies and pastries with magical twists: will it turn you green? Will you be able to lift a tree out of the ground with your mind? You never know until you try one!", 
"Curse Delivery Service – Do you really hate someone? Send them an item imbued with a minor curse! Try some of our favorites including incessant screaming inside of their head, a curse to make every food taste like something the recipient hates, and many more.", 
"Culpert’s Construction Company- A magician speeds up construction efforts for large structures by using Move Earth to create the basement, leveling off the ground and smoothing the earth out.", 
"The Phantom Opera House – An Opera house owned and run by a collection of illusion-based wizards who create visual spectacles to go along with the performances.", 
"Perfect Paintings – A wizard creates what are essentially the world’s first photographs by magically superimposing the target’s image onto his own specially made material. they are in perfect clarity and he has a variety of fun pose and background options to choose from.", 
"Grenden the Enhancer – By night, this shady guy will sell you magical performance enhancers (jump, longstrider, etc.) to win races. By day he is a successful sports gambler.", 
"Snilloc’s Cold Storage – these ice wizards will keep your meat cold until you can sell it. Gentle repose is a specialty of theirs.", 
"Locksmiths – Need an arcane lock on your door? Need an alarm on your entrance hall? Need a glyph of warding on your safe? These wizards have got you covered.", 
"Roland’s Replicators – Will make an exact magical copy of any item brought in. Cannot replicate magical effects but will give off a similar magical aura.", 
"Melvor’s Magical Mead – Magic infused ‘mead’ that will get you drunk with only a thimble full. Contains all the effects of heavy drinking, but no alcohol",
]
let questPull = shuffle(questBoard);
let chance = rollDice(100)
let flyers = shuffle(promo);


if (chance < 25) {
printFrom(questPull, 4, "Quest")
} else if (chance < 50) {
printFrom(questPull, 3, "Quest")
} else if (chance < 75) {
printFrom(questPull, 2, "Quest")
} else if (chance < 100) {
printFrom(questPull, 1, "Quest")
};
let chanceTwo = rollDice(100)
if (chanceTwo < 25) {
printFrom(flyers, 1, "Promo")
} else if (chanceTwo < 50) {
printFrom(flyers, 2, "Promo")
} else if (chanceTwo < 75) {
printFrom(flyers, 3, "Promo")
} else if (chanceTwo < 100) {
printFrom(flyers, 4, "Promo")
};
};
function rivalParty() {
document.getElementById("Rival").innerHTML = ""

function calculateGold(level, fights) {
if (level === 1) {
return `(Average Value: ~${60*fights}gp) Coins: PP:${modify(0)*fights} GP:${modify(0)*fights} EP:${modify(5)*fights} SP:${modify(195)*fights} CP:${modify(390)*fights}`
} else if (level === 2) {
return `(Average Value: ~${60*fights}gp) Coins: PP:${modify(0)*fights} GP:${modify(3)*fights} EP:${modify(31)*fights} SP:${modify(312)*fights} CP:${modify(260)*fights}`
} else if (level === 3) {
return `(Average Value: ~${60*fights}gp) Coins: PP:${modify(0)*fights} GP:${modify(12)*fights} EP:${modify(35)*fights} SP:${modify(482)*fights} CP:${modify(158)*fights}`
} else if (level === 4) {
return `(Average Value: ~${60*fights}gp) Coins: PP:${modify(1)*fights} GP:${modify(16)*fights} EP:${modify(53)*fights} SP:${modify(567)*fights} CP:${modify(105)*fights}`
} else if (level === 5) {
return `(Average Value: ~${505*fights}gp) Coins: PP:${modify(2)*fights} GP:${modify(50)*fights} EP:${modify(248)*fights} SP:${modify(828)*fights} CP:${modify(14)*fights}`
} else if (level === 6) {
return `(Average Value: ~${505*fights}gp) Coins: PP:${modify(4)*fights} GP:${modify(60)*fights} EP:${modify(305)*fights} SP:${modify(828)*fights} CP:${modify(0)*fights}`
} else if (level === 7) {
return `(Average Value: ~${505*fights}gp) Coins: PP:${modify(5)*fights} GP:${modify(69)*fights} EP:${modify(386)*fights} SP:${modify(772)*fights} CP:${modify(0)*fights}`
} else if (level === 8) {
return `(Average Value: ~${505*fights}gp) Coins: PP:${modify(18)*fights} GP:${modify(71)*fights} EP:${modify(485)*fights} SP:${modify(706)*fights} CP:${modify(0)*fights}`
} else if (level === 9) {
return `(Average Value: ~${505*fights}gp) Coins: PP:${modify(7)*fights} GP:${modify(84)*fights} EP:${modify(755)*fights} SP:${modify(547)*fights} CP:${modify(0)*fights}`
} else if (level === 10) {
return `(Average Value: ~${505*fights}gp) Coins: PP:${modify(7)*fights} GP:${modify(66)*fights} EP:${modify(696)*fights} SP:${modify(718)*fights} CP:${modify(0)*fights}`
} else if (level === 11) {
return `(Average Value: ~${1951*fights}gp) Coins: PP:${modify(24)*fights} GP:${modify(968)*fights} EP:${modify(399)*fights} SP:${modify(142)*fights} CP:${modify(0)*fights}`
} else if (level === 12) {
return `(Average Value: ~${1951*fights}gp) Coins: PP:${modify(26)*fights} GP:${modify(1057)*fights} EP:${modify(466)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
} else if (level === 13) {
return `(Average Value: ~${1951*fights}gp) Coins: PP:${modify(29)*fights} GP:${modify(1262)*fights} EP:${modify(269)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
} else if (level === 14) {
return `(Average Value: ~${1951*fights}gp) Coins: PP:${modify(27)*fights} GP:${modify(1432)*fights} EP:${modify(218)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
} else if (level === 15) {
return `(Average Value: ~${1951*fights}gp) Coins: PP:${modify(39)*fights} GP:${modify(1457)*fights} EP:${modify(194)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
} else if (level === 16) {
return `(Average Value: ~${1951*fights}gp) Coins: PP:${modify(46)*fights} GP:${modify(1533)*fights} EP:${modify(166)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
} else if (level === 17) {
return `(Average Value: ~${1951*fights}gp) Coins: PP:${modify(779)*fights} GP:${modify(875)*fights} EP:${modify(175)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
} else if (level === 18) {
return `(Average Value: ~${12205*fights}gp) Coins: PP:${modify(834)*fights} GP:${modify(834)*fights} EP:${modify(185)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
} else if (level === 19) {
return `(Average Value: ~${12205*fights}gp) Coins: PP:${modify(870)*fights} GP:${modify(1075)*fights} EP:${modify(0)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
} else if (level === 20) {
return `(Average Value: ~${12205*fights}gp) Coins: PP:${modify(921)*fights} GP:${modify(1081)*fights} EP:${modify(0)*fights} SP:${modify(0)*fights} CP:${modify(0)*fights}`
}
};

function alternateRewards(level, fights) {
function loopCountPushGems(array, array2, value) {
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
array2.push(` Bag of gems (Value: ${value} gp): ${final}`)
}

function loopCountPushArt(array, array2, value) {
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
array2.push(`A Set of Art Pieces (Value: ${value} gp): ${final}`)
}
let cantrip = ["Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights", "Druidcraft", "Eldritch Blast", "Fire Bolt", "Friends", "Frostbite", "Green-Flame Blade", "Guidance", "Gust", "Infestation", "Light", "Lightning Lure", "Mage Hand", "Magic Stone", "Mending", "Message", "Minor Illusion", "Mold earth", "Poison Spray", "Prestidigitation", "Primal Savagery", "Produce Flame", "Ray of Frost", "Resistance", "Sacred Flame", "Shape Water", "Shillelagh", "Shocking Grasp", "Spare the Dying", "Sword Burst", "Thaumaturgy", "Thorn Whip", "Thunderclap", "Toll the Dead", "True Strike", "Vicious Mockery", "Word of Radiance"]
let first = ["Absorb Elements", "Alarm", "Animal Friendship", "Armor of Agathys", "Arms of Hadar", "Bane", "Beast Bond", "Bless", "Burning Hands", "Catapult", "Cause Fear", "Ceremony (Ritual)", "Chaos Bolt", "Charm Person", "Chromatic Orb", "Color Spray", "Command", "Compelled Duel", "Comprehend Languages (Ritual)", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good", "Detect Magic (Ritual)", "Detect Poison and Disease (Ritual)", "Disguise Self", "Dissonant Whispers", "Divine Favor", "Earth Tremor", "Ensnaring Strike", "Entangle", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Find Familiar (Ritual)", "Fog Cloud", "Goodberry", "Grease", "Guiding Bolt", "Hail of Thorns", "Healing Word", "Hellish Rebuke", "Heroism", "Hex", "Hunter’s Mark", "Ice Knife", "Identify", "Illusory Script", "Inflict Wounds", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Purify Food and Drink (Ritual)", "Ray of Sickness", "Sanctuary", "Searing Smite", "Shield", "Shield of Faith", "Silent Image", "Sleep", "Snare", "Speak with Animals (Ritual)", "Tasha’s Hideous Laughter", "Tenser’s Floating Disk (Ritual)", "Thunderous Smite", "Thunderwave", "Unseen Servant (Ritual)", "Witch Bolt", "Wrathful Smite", "Zephyr Strike"]
let second = ["Aganazzar’s Scorcher", "Aid", "Alter Self", "Animal Messenger (Ritual)", "Arcane Lock", "Augury", "Barkskin", "Beast Sense (Ritual)", "Blindness/Deafness", "Blur", "Branding Smite", "Calm Emotions", "Cloud of Daggers", "Continual Flame", "Cordon of Arrows", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Dragon's Breath", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/Reduce", "Enthrall", "Find Steed", "Find Traps", "Flame Blade", "Flaming Sphere", "Gentle Repose (Ritual)", "Gust of Wind", "Healing Spirit", "Heat Metal", "Hold Person", "Invisibility", "Knock", "Lesser Restoration", "Levitate", "Locate Animals or Plants (Ritual)", "Locate Object", "Magic Mouth", "Magic Weapon", "Maximilian’s Earthen Grasp", "Melf’s Acid Arrow", "Mind Spike", "Mirror Image", "Misty Step", "Moonbeam", "Nystul’s Magic Aura", "Pass Without Trace", "Phantasmal Force", "Prayer of Healing", "Protection from Poison", "Pyrotechnics", "Ray of Enfeeblement", "Rope Trick", "Scorching Ray", "See invisibility", "Shadow Blade", "Shatter", "Silence (Ritual)", "Skywrite (Ritual)", "Snilloc’s Snowball Swarm", "Spider Climb", "Spike Growth", "Spiritual Weapon", "Suggestion", "Warding Bond", "Warding Wind", "Web", "Zone of Truth"]
let third = ["Animate Dead", "Aura of Vitality", "Beacon of Hope", "Bestow Curse", "Blinding Smite", "Blink", "Call Lightning", "Catnap", "Clairvoyance", "Conjure Animals", "Conjure Barrage", "Counterspell", "Create Food and Water", "Crusader’s Mantle", "Daylight", "Dispel Magic", "Elemental Weapon", "Enemies abound", "Erupting Earth", "Fear", "Feign Death (Ritual)", "Fireball", "Flame Arrows", "Fly", "Gaseous Form", "Glyph of Warding", "Haste", "Hunger of Hadar", "Hypnotic Pattern", "Leomund’s Tiny Hut", "Life Transference", "Lightning Arrow", "Lightning Bolt", "Magic Circle", "Major Image", "Mass Healing Word", "Meld into Stone (Ritual)", "Melf’s Minute Meteors", "Nondetection", "Phantom Steed", "Plant Growth", "Protection from Energy", "Remove Curse", "Revivify", "Sending", "Sleet Storm", "Slow", "Speak with Dead", "Speak with Plants", "Spirit Guardians", "Stinking Cloud", "Summon Lesser Demons", "Thunder Step", "Tidal Wave", "Tiny Servant", "Tongues", "Vampiric Touch", "Wall of Sand", "Wall of Water", "Water Breathing (Ritual)", "Water Walk (Ritual)", "Wind Wall"]
let fourth = ["Arcane Eye", "Aura of Life", "Aura of Purity", "Banishment", "Blight", "Charm Monster", "Compulsion", "Confusion", "Conjure Minor Elementals", "Conjure Woodland Beings", "Control Water", "Death Ward", "Dimension Door", "Divination (Ritual)", "Dominate Beast", "Elemental Bane", "Evard’s Black Tentacles", "Fabricate", "Find Greater Steed", "Fire Shield", "Freedom of Movement", "Giant Insect", "Grasping Vine", "Greater Invisibility", "Guardian of Faith", "Guardian of Nature", "Hallucinatory Terrain", "Ice Storm", "Leomund’s Secret Chest", "Locate Creature", "Mordenkainen’s Faithful Hound", "Mordenkainen’s Private Sanctum", "Otiluke’s Resilient Sphere", "Phantasmal Killer", "Polymorph", "Shadow of Moil", "Sickening Radiance", "Staggering Smite", "Stone Shape", "Stoneskin", "Storm Sphere", "Summon Greater Demon", "Vitriolic Sphere", "Wall of Fire", "Watery Sphere"]
let fifth = ["Animate Objects", "Antilife Shell", "Awaken", "Banishing Smite", "Bigby’s Hand", "Circle of Power", "Cloudkill", "Commune", "Commune with Nature", "Cone of Cold", "Conjure Elemental", "Conjure Volley", "Contact Other Plane", "Contagion", "Control Winds", "Creation", "Danse Macabre", "Dawn", "Destructive Wave", "Dispel Evil and Good", "Dominate Person", "Dream", "Enervation", "Far Step", "Flame Strike", "Geas", "Greater Restoration", "Hallow", "Hold Monster", "Holy Weapon", "Immolation", "Infernal Calling", "Insect Plague", "Legend Lore", "Maelstrom", "Mass Cure Wounds", "Mislead", "Modify Memory", "Negative Energy Flood", "Passwall", "Planar Binding", "Raise Dead", "Rary’s Telepathic Bond (Ritual)", "Reincarnate", "Scrying", "Seeming", "Skill Empowerment", "Steel Wind Strike", "Swift Quiver", "Synaptic Static", "Telekinesis", "Teleportation Circle", "Transmute Rock", "Tree Stride", "Wall of Force", "Wall of Light", "Wall of Stone", "Wrath of Nature"]
let sixth = ["Arcane Gate", "Blade Barrier", "Bones of the Earth", "Chain Lightning", "Circle of Death", "Conjure Fey", "Contingency", "Create Homunculus", "Create Undead", "Disintegrate", "Drawmij’s Instant Summons", "Druid Grove", "Eyebite", "Find the Path", "Flesh to Stone", "Forbiddance (Ritual)", "Globe of Invulnerability", "Guards and Wards", "Harm", "Heal", "Heroes’ Feast", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Magic Jar", "Mass Suggestion", "Mental Prison", "Move Earth", "Otiluke’s Freezing Sphere", "Otto’s Irresistible Dance", "Planar Ally", "Primordial Ward", "Primordial Ward", "Programmed", "Scatter", "Soul Cage", "Sunbeam", "Tenser’s Transformation", "Transport via Plants", "True Seeing", "Wall of Ice", "Wall of Thorns", "Wind Walk", "Word of Recall"]
let seventh = ["Conjure Celestial", "Crown of Stars", "Delayed Blast Fireball", "Divine Word", "Etherealness", "Finger of Death", "Fire Storm", "Forcecage", "Mirage Arcane", "Mordenkainen’s Magnificent Mansion", "Mordenkainen’s Sword", "Plane Shift", "Power Word Pain", "Prismatic Spray", "Project Image", "Regenerate", "Resurrection", "Reverse Gravity", "Sequester", "Simulacrum", "Symbol", "Teleport", "Temple of the Gods", "Whirlwind"]
let eighth = ["Abi-Dalzim’s Horrid Wilting", "Animal Shapes", "Antimagic Field", "Antipathy/Sympathy", "Clone", "Control Weather", "Demiplane", "Dominate Monster", "Earthquake", "Feeblemind", "Glibness", "Holy Aura", "Illusory Dragon", "Incendiary Cloud", "Maddening Darkness", "Maze", "Mighty Fortress", "Mind Blank", "Power Word Stun", "Sunburst", "Telepathy", "Trap the Soul", "Tsunami"]
let ninth = ["Astral Projection", "Foresight", "Gate", "Imprisonment", "Invulnerability", "Mass Heal", "Mass Polymorph", "Meteor Swarm", "Power Word Heal", "Power Word Kill", "Prismatic Wall", "Psychic Scream", "Shapechange", "Storm of Vengeance", "Time Stop", "True Polymorph", "True Resurrection", "Weird", "Wish"]
let magicItemsA = [`Spell scroll (cantrip) ${searchArray(cantrip)}`, `Spell scroll (1st level) ${searchArray(first)}`, `Spell scroll (2nd level) ${searchArray(second)}`, `Spell scroll (3rd level) ${searchArray(third)}`, "Potion of healing", "Potion of climbing", "Potion of greater healing", "Bag of holding", "Driftglobe"]
let magicItemsB = [`Spell scroll (cantrip) ${searchArray(cantrip)}`, `Spell scroll (1st level) ${searchArray(first)}`, `Spell scroll (2nd level) ${searchArray(second)}`, `Spell scroll (3rd level) ${searchArray(third)}`, "Potion of greater healing", "Potion of fire breath", "Potion of resistance", "Ammunition, +1", "Potion of animal friendship", "Potion of hill giant strength", "Potion of growth", "Potion of water breathing", "Bag of holding", "Keoghtom's ointment", "Oil of slipperiness", "Dust of disappearance", "Dust of dryness", "Dust of sneezing and choking", "Elemental gem", "Philter of love", "Alchemy jug", "Cap of water breathing", "Cloak of the manta ray", "Driftglobe", "Goggles of night", "Helm of comprehending languages", "Immovable rod", "Lantern of revealing", "Mariner's armor", "Mithral armor", "Potion of poison", "Ring of swimming", "Robe of useful items", "Rope of climbing", "Saddle of the cavalier", "Wand of magic detection", "Wand of secrets"]
let magicItemsC = [`Spell scroll (cantrip) ${searchArray(cantrip)}`, `Spell scroll (1st level) ${searchArray(first)}`, `Spell scroll (2nd level) ${searchArray(second)}`, `Spell scroll (3rd level) ${searchArray(third)}`, "Potion of superior healing", "Ammunition, +2", "Potion of clairvoyance", "Potion of diminution", "Potion of gaseous form", "Potion of frost giant strength", "Potion of stone giant strength", "Potion of heroism", "Potion of invulnerability", "Potion of mind reading", "Elixir of health", "Oil of etherealness", "Potion of fire giant strength", "Quaal's feather token", "Scroll of protection", "Bag of beans", "Bead of force", "Chime of opening", "Decanter of endless water", "Eyes of minute seeing", "Folding boat", "Heward's handy haversack", "Horseshoes of speed", "Necklace of fireballs", "Periapt of health", "Sending Stones"]
let magicItemsD = [`Spell scroll (4thlevel) ${searchArray(fourth)}`, `Spell scroll (5thlevel) ${searchArray(fifth)}`, `Spell scroll (6thlevel) ${searchArray(sixth)}`, "Potion of supreme healing", "Potion of invisibility", "Potion of speed", "Ammunition, +3", "Oil of sharpness", "Potion of flying", "Potion of cloud giant strength", "Potion of longevity", "Potion of vitality", "Horseshoes of a zephyr", "Nolzur's marvelous pigments", "Bag of devouring", "Portable hole"]
let magicItemsE = [`Spell scroll (4thlevel) ${searchArray(fourth)}`, `Spell scroll (5thlevel) ${searchArray(fifth)}`, `Spell scroll (6thlevel) ${searchArray(sixth)}`, "Potion of storm giant strength", "Potion of supreme healing", "Universal solvent", "Arrow of slaying", "Sovereign glue"]
let magicItemsF = [`Spell scroll (4thlevel) ${searchArray(fourth)}`, `Spell scroll (5thlevel) ${searchArray(fifth)}`, `Spell scroll (6thlevel) ${searchArray(sixth)}`, "Weapon, +1", "Shield,+ 1", "Sentinel shield", "Amulet of proof against detection and location", "Boots of elvenkind", "Boots of striding and springing", "Bracers of archery", "Brooch of shielding", "Broom of flying", "Cloak of elvenkind", "Cloak of protection", "Gauntlets of ogre power", "Hat of disguise", "Javelin of lightning", "Pearl of power", "Rod of the pact keeper, + 1", "Slippers of spider climbing", "Staff of the adder", "Staff of the python", "Sword of vengeance", "Trident of fish command", "Wand of magic missiles", "Wand of the war mage, + 1", "Wand of web", "Weapon of warning", "Adamantine armor (chain mail)", "Adamantine armor (chain shirt)", "Adamantine armor (scale mail)", "Bag of tricks (gray)", "Bag of tricks (rust)", "Bag of tricks (tan)", "Boots of the winterlands", "Circlet of blasting", "Deck of illusions", "Eversmoking bottle", "Eyes of charming", "Eyes of the eagle", "Figurine of wondrous power (silver raven)", "Gem of brightness", "Gloves of missile snaring", "Gloves of swimming and climbing", "Gloves of thievery", "Headband of intellect", "Helm of telepathy", "Instrument of the bards (Doss lute)", "Instrument of the bards (Fochlucan bandore)", "Instrument of the bards (Mac-Fuimidh cittern)", "Medallion of thoughts", "Necklace of adaptation", "Periapt of wound closure", "Pipes of haunting", "Pipes of the sewers", "Ring of jumping", "Ring of mind shielding", "Ring of warmth", "Ring of water walking", "Quiver of Ehlonna", "Stone of good luck", "Wind fan", "Winged boots"]
let magicItemsG = [`Spell scroll (7thlevel) ${searchArray(seventh)}`, `Spell scroll (8thlevel) ${searchArray(eighth)}`, `Spell scroll (9th level) ${searchArray(ninth)}`, "Weapon, +2", `Figurine of wondrous power ${searchArray(["(bronze griffon)", "(ebony fly)", "(golden lions)", "(ivory goats)", "(marble elephant)", "(onyx dog)", "(serpentine owl)"])}`, "Adamantine armor (breastplate)", "Adamantine armor (splint)", "Amulet of health", "Armor of vulnerability", "Arrow-catching shield", "Belt of dwarvenkind", "Belt of hill giant strength", "Berserker axe", "Boots of levitation", "Boots of speed", "Bowl of commanding water elementals", "Bracers of defense", "Brazier of commanding fire elementals", "Cape of the mountebank", "Censer of controlling air elementals", "Armor, +1 chain mail", "Armor of resistance (chain mail)", "Armor of resistance (chain shirt)", "Armor,+ 1 chain shirt", "Cloak of displacement", "Cloak of the bat", "Cube of force", "Daern's instant fortress", "Dagger of venom", "Dimensional shackles", "Dragon slayer", "Elven chain", "Flame tongue", "Gem of seeing", "Giant slayer", "Clamoured studded leather", "Helm of teleportation", "Horn of blasting", "Horn of Valhalla (silver or brass)", "Instrument of the bards (Canaithmandolin)", "Instrument of the bards (Cii lyre)", "loun stone (awareness)", "loun stone (protection)", "loun stone (reserve)", "loun stone (sustenance)", "Iron bands of Bilarro", "Armor, + 1 leather", "Armor of resistance (leather)", "Mace of disruption", "Mace of smiting", "Mace of terror", "Mantle of spell resistance", "Necklace of prayer beads", "Periapt of proof against poison", "Ring of animal influence", "Ring of evasion", "Ring of feather falling", "Ring of free action", "Ring of protection", "Ring of resistance", "Ring of spell storing", "Ring of the ram", "Ring of X-ray vision", "Robe of eyes", "Rod of rulership", "Rod of the pact keeper, +2", "Rope of entanglement", "Armor, +1 scale mail", "Armor of resistance (scale mail)", "Shield, +2", "Shield of missile attraction", "Staff of charming", "Staff of healing", "Staff of swarming insects", "Staff of the woodlands", "Staff of withering", "Stone of controlling earthelementals", "Sun blade", "Sword of life stealing", "Sword of wounding", "Tentacle rod", "Vicious weapon", "Wand of binding", "Wand of enemy detection", "Wand of fear", "Wand of fireballs", "Wand of lightning bolts", "Wand of paralysis", "Wand of the war mage, +2", "Wand of wonder", "Wings of flying"]
let magicItemsH = [`Spell scroll (7thlevel) ${searchArray(seventh)}`, `Spell scroll (8thlevel) ${searchArray(eighth)}`, `Spell scroll (9th level) ${searchArray(ninth)}`, "Weapon, +3", "Amulet of the planes", "Carpet of flying", "Crystal ball (very rare version)", "Ring of regeneration", "Ring of shooting stars", "Ring of telekinesis", "Robe of scintillating colors", "Robe of stars", "Rod of absorption", "Rod of alertness", "Rod of security", "Rod of the pact keeper, +3", "Scimitar of speed", "Shield, +3", "Staff of fire", "Staff of frost", "Staff of power", "Staff of striking", "Staff of thunder and lightning", "Sword of sharpnes", "Wand of polymorph", "Wand of the war mage, + 3", "Adamantine armor (half plate)", "Adamantine armor (plate)", "Animated shield", "Belt of fire giant strength", "Belt of frost (or stone) giant strength", "Armor, + 1 breastplate", "Armor of resistance (breastplate)", "Candle of invocation", "Armor, +2 chain mail", "Armor, +2 chain shirt", "Cloak of arachnida", "Dancing sword", "Demon armor", "Dragon scale mail", "Dwarven plate", "Dwarven thrower", "Efreeti bottle", "Figurine of wondrous power (obsidian steed)", "Frost brand", "Helm of brilliance", "Horn of Valhalla (bronze)", "Instrument of the bards (Anstruthharp)", "loun stone (absorption)", "loun stone (agility)", "loun stone (fortitude)", "loun stone (insight)", "loun stone (intellect)", "loun stone (leadership)", "loun stone (strength)", "Armor, +2 leather", "Manual of bodily health", "Manual of gainful exercise", "Manual of golems", "Manual of quickness of action", "Mirror of life trapping", "Nine lives stealer", "Oathbow", "Armor, +2 scale mail", "Spellguard shield", "Armor, + 1 splint", "Armor of resistance (splint)", "Armor, + 1 studded leather", "Armor of resistance (studded leather)", "Tome of clear thought", "Tome of leadership and influence", "Tome of understanding"]
let magicItemsI = [`Spell scroll (7thlevel) ${searchArray(seventh)}`, `Spell scroll (8thlevel) ${searchArray(eighth)}`, `Spell scroll (9th level) ${searchArray(ninth)}`, "Defender", "Hammer of thunderbolts", "Luck Blade", "Sword of answering", "Holy avenger", "Ring of djinni summoning", "Ring of invisibility", "Ring of spell turning", "Rod of lordly might", "Vorpal sword", "Belt of cloud giant strength", "Armor, +2 breastplate", "Armor, +3 chain mail", "Armor, +3 chain shirt", "Cloak of invisibility", "Crystal ball (legendary version)", "Armor, + 1 half plate", "Iron flask", "Armor, +3 leather", "Armor, +1 plate", "Robe of the archmagi", "Rod of resurrection", "Armor, +1 scale mail", "Scarab of protection", "Armor, +2 splint", "Armor, +2 studded leather", "Well of many worlds", "Armor, +2 half plate", "Armor, +2 plate", "Armor, +3 studded leather", "Armor, +3 breastplate", "Armor, +3 splint", "Armor, +3 half plate", "Armor, +3 plate", "Apparatus of Kwalish", "Armor of invulnerability", "Belt of storm giant strength", "Cubic gate", "Deck of many things", "Efreeti chain", "Armor of resistance (half plate)", "Horn of Valhalla (iron)", "Instrument of the bards (OIIamh harp)", "loun stone (greater absorption)", "loun stone (mastery)", "loun stone (regeneration)", "Plate armor of etherealness", "Plate armor of resistance", "Ring of air elemental command", "Ring of earth elemental command", "Ring of fire elemental command", "Ring of three wishes", "Ring of water elemental command", "Sphere of annihilation", "Talisman of pure good", "Talisman of the sphere", "Talisman of ultimate evil", "Tome of the stilled tongue"]


if (level === 1) {
let loot = []


let x = Math.floor(1 + fights / 2)
for (i = 0; i < x; i++) {


loot.push(searchArray(magicItemsA))
}


return loopCountStoreList(loot)
} else if (level === 2) {
let loot = []


let x = Math.floor(1 + fights / 2)
for (i = 0; i < x; i++) {



loot.push(searchArray(magicItemsA))
}


return loopCountStoreList(loot)
} else if (level === 3) {
let loot = []


let x = Math.floor(1 + fights / 2)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsA))
}


return loopCountStoreList(loot)
} else if (level === 4) {
let loot = []


let x = Math.floor(1 + fights / 2)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsA))
}


return loopCountStoreList(loot)
} else if (level === 5) {
let loot = []


let x = Math.floor(1 + fights / 4)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsB))
}


return loopCountStoreList(loot)
} else if (level === 6) {
let loot = []


let x = Math.floor(1 + fights / 4)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsB))
loot.push(searchArray(magicItemsB))
}


return loopCountStoreList(loot)
} else if (level === 7) {
let loot = []


let x = Math.floor(1 + fights / 4)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsB))
}


return loopCountStoreList(loot)
} else if (level === 8) {
let loot = []


let x = Math.floor(1 + fights / 4)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsA))
loot.push(searchArray(magicItemsB))
loot.push(searchArray(magicItemsB))
}


return loopCountStoreList(loot)
} else if (level === 9) {
let loot = []


let x = Math.floor(1 + fights / 4)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsB))
loot.push(searchArray(magicItemsB))
loot.push(searchArray(magicItemsB))
}


return loopCountStoreList(loot)
} else if (level === 10) {
let loot = []


let x = Math.floor(1 + fights / 6)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsB))
loot.push(searchArray(magicItemsB))
loot.push(searchArray(magicItemsC))
}


return loopCountStoreList(loot)
} else if (level === 11) {
let loot = []


let x = Math.floor(1 + fights / 6)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsB))
loot.push(searchArray(magicItemsC))
loot.push(searchArray(magicItemsC))
}


return loopCountStoreList(loot)
} else if (level === 12) {
let loot = []


let x = Math.floor(1 + fights / 6)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsC))
loot.push(searchArray(magicItemsC))
loot.push(searchArray(magicItemsC))
}


return loopCountStoreList(loot)
} else if (level === 13) {
let loot = []


let x = Math.floor(1 + fights / 6)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsC))
loot.push(searchArray(magicItemsC))
loot.push(searchArray(magicItemsD))
}


return loopCountStoreList(loot)
} else if (level === 14) {
let loot = []


let x = Math.floor(1 + fights / 6)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsC))
loot.push(searchArray(magicItemsD))
loot.push(searchArray(magicItemsD))
}


return loopCountStoreList(loot)
} else if (level === 15) {
let loot = []


let x = Math.floor(1 + fights / 6)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsD))
loot.push(searchArray(magicItemsD))
loot.push(searchArray(magicItemsD))
}


return loopCountStoreList(loot)
} else if (level === 16) {
let loot = []


let x = Math.floor(1 + fights / 8)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsD))
loot.push(searchArray(magicItemsD))
loot.push(searchArray(magicItemsE))
}


return loopCountStoreList(loot)
} else if (level === 17) {
let loot = []


let x = Math.floor(1 + fights / 8)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsD))
loot.push(searchArray(magicItemsE))
loot.push(searchArray(magicItemsE))
}


return loopCountStoreList(loot)
} else if (level === 18) {
let loot = []


let x = Math.floor(1 + fights / 8)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsE))
loot.push(searchArray(magicItemsF))
loot.push(searchArray(magicItemsG))
}


return loopCountStoreList(loot)
} else if (level === 19) {
let loot = []


let x = Math.floor(1 + fights / 8)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsF))
loot.push(searchArray(magicItemsG))
loot.push(searchArray(magicItemsH))
}


return loopCountStoreList(loot)
} else if (level === 20) {
let loot = []


let x = Math.floor(1 + fights / 8)
for (i = 0; i < x; i++) {




loot.push(searchArray(magicItemsG))
loot.push(searchArray(magicItemsH))
loot.push(searchArray(magicItemsI))
}


return loopCountStoreList(loot)
}
};

let partySize = 3 + rollDice(3)
let partyLevel = 1 + rollDice(19)
let standing = [
"friendly towards the PC party", 
"hostile towards the PC party for a percieved slight", 
"stand-offish and secretive", 
"drunk", 
"currently looking for someone", 
"recovering/wounded from a battle that went poorly",
]
let travelPlans = [ "North", "North - East", "East", "South - East", "South", "South - West", "West", "North - West", ]

function partyPrint(Number) {
function pBuilder(Number) {
let party = []
for (let i = 0; i < Number; i++) {
party[i] = ` ${genderReturn()} ${raceReturn()} ${findClass()}`
};

function raceReturn() {
var races = [
[ //Common
'Human',
],
[ //Uncommon
'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling',
],
[ //Rare
'Dragonborn', 'Tiefling', 'Genasi', 'Aasimar', 'Half-Orc', 'Tabaxi',
],
[ //Very Rare
'Kalashtar', 'Shifter', 'Warforged', 'Simic Hybrid', 'Changeling', 'Goliath', 'Gith', 'Yuan-Ti', 'Tortle', 'Aarakocra', 'Orc',
],
[ //Ultimate Rare
'Bugbear', 'Firbolg', 'Goblin', 'Hobgoblin', 'Kenku', 'Kobold', 'Triton', 'Lizardfolk', 'Vedalken', 'Verdan', 'Locathah', 'Grung', 'Centaur', 'Loxodon', 'Minotaur',
],
]

let chance = rollDice(100)
if (chance > 98) {
let raceArray = races[4]
return searchArray(raceArray);
} else if (chance > 95) {
let raceArray = races[3]
return searchArray(raceArray);
} else if (chance > 80) {
let raceArray = races[2]
return searchArray(raceArray);
} else if (chance > 50) {
let raceArray = races[1]
return searchArray(raceArray);
} else {
let raceArray = races[0]
return searchArray(raceArray);
}
};

function findClass() {
//Class Array
let classes = [
[
'Bard', 'Cleric', 'Fighter', 'Ranger', 'Rogue',
],
[
'Barbarian', 'Druid', 'Monk', 'Paladin',
],
[
'Sorcerer', 'Warlock', 'Wizard', 'Artificer', 'Summoner',
],
[
'Bounty Hunter', 'Blood Hunter', 'Mystic',
],
]

function classReturn() {
var chance = rollDice(100);
if (chance > 98) {
return searchArray(classes[3]);
} else if (chance > 75) {
return searchArray(classes[2]);
} else if (chance > 45) {
return searchArray(classes[1]);
} else {
return searchArray(classes[0]);
};
}
return classReturn()
};

function genderReturn() {
let chance = rollDice(100)
if (chance < 50) {
return "(F)"
} else {
return "(M)"
}
};
return party
}
return pBuilder(Number)
}
let pcomp = partyPrint(partySize)

let flavor = `Another adventuring party ${searchArray(["is already in the tavern once the PC party arrives", 
"arrives to the tavern some time after the PC party"])}. They seem to be ${searchArray(standing)}. If engaged, the PC party may learn that the other party will be travelling ${searchArray(travelPlans)} to reach their next destination. The party is level ${partyLevel}.`
let comp = `The other party's composition is: ${pcomp}`
let gold = `The other party's funds are: ${calculateGold(partyLevel,partySize)}.`
let items = `The other party's magical items are ${searchArray(["concealed","out in the open"])}: ${alternateRewards(partyLevel,partySize*2)}`
let output = [flavor, comp, gold, items]
orderedPrint(output, output.length, "Rival")
};
function buildTavern() {
tavernName()
findF1()
findF2()
findEndConvo()
findInsult()
bardFind()
instrumentFind()
currentlyPlaying()
foodFind()
drinkFind()
events()
quest()
rivalParty()
};