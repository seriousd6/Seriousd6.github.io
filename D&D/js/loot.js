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


/*

**historal events
words for ruler
things to be drinking
Words for showing
facial expressions
art source array
cultural motifs array
types of fancy clothes
fancy clothes materials
what are the categories art would cover
mirrors to society
stories
history
values
beliefs
social norms
hopes
fears

*/

function pickDirection(){
    return searchArray([ 'north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest' ])
}
function treasureMap() {
    let start = [
        `big cracked boulder`, 
        `lightning-blasted oak tree`, 
        `rock shaped like a horse`, 
        `stone wall with a piece of volcanic glass`, 
        `exact center of the village/town/city`, 
        `statue of (famous person)`, 
        `shipwreck of the SS (name)`, 
        `bones of the black dragon`, 
        `cavern near the waterfall`, 
        `top of the volcano`, 
        `exact center of the lake`, 
        `abandoned Temple`, 
        `old Fort`, 
        `old standing circle`, 
        `road marker leading south`, 
        `exact center of the longest bridge`, 
        `hangman's scaffold`, 
        `${searchArray(['king','queen'])}'s throne room`, 
        `crossroads`, 
        `largest tomb in the cemetery`, 
        `enchanted glade with glowing mushrooms`, 
        `sunken ruins beneath the sea`, 
        `ancient tree with inscriptions`, 
        `buried ruins of an ancient civilization`, 
        `giant beehive hanging from a tree branch`, 
        `mysterious crop circle in a field`, 
        `ruined watchtower on a hilltop`, 
        `forgotten library filled with dusty books`, 
        `gloomy and abandoned mine shaft`, 
        `strange markings on a rocky cliffside`, 
        `mystical standing stones arranged in a circle`, 
        `frozen cave with sparkling ice crystals`, 
        `lost island hidden by illusion magic`, 
        `overgrown jungle temple with booby traps`, 
        `crystal-clear underground lake`, 
        `ancient labyrinth with shifting walls`, 
        `sacred waterfall believed to have healing powers`,
        `hidden entrance behind a waterfall`, 
        `scorched desert oasis with a secret passage`, 
        `glistening pearl at the heart of the coral reef`, 
        `bottom of the deepest ocean trench`, 
        `enchanted forest with singing trees`, 
        `dragon's skull embedded in the mountainside`, 
        `cursed tower surrounded by eternal storm clouds`, 
        `wreckage of an alien spaceship`, 
        `ancient celestial observatory`, 
        `garden of glowing crystals`, 
        `lost city in the clouds`, 
        `whispering sands of the desert`, 
        `fabled fountain of eternal youth`, 
        `forgotten dungeon with hidden traps`, 
        `portal to another realm within a cave`,
        `crashed meteorite site with otherworldly rocks`, 
        `secret passage beneath an ancient tree root`, 
        `ominous graveyard of sea serpents`, 
        `enchanted ice sculptures in an icy cave`, 
        `enchanted well that grants wishes`, 
        `maze of mirrors that distorts reality`, 
        `floating island with gravity-defying terrain`, 
        `timeless pocket dimension accessible through a portal`, 
        `abandoned wizard's tower with magical residue`, 
        `giant flower with petals that emit a soft glow`, 
        `eerie ruins of a cursed castle`, 
        `moonlit meadow where mythical creatures gather`,
        `quaint cottage hidden within a dense forest`, 
        `old windmill on the edge of the rolling hills`, 
        `rugged cliffside overlooking the crashing waves`, 
        `narrow entrance to a labyrinthine cave system`, 
        `peaceful meadow with wildflowers in full bloom`, 
        `forgotten ruins of an ancient amphitheater`, 
        `vine-covered archway leading to a secluded garden`, 
        `rustic bridge spanning a tranquil river`, 
        `isolated lighthouse standing tall on a rocky outcrop`, 
        `abandoned lighthouse with a crumbling spiral staircase`, 
        `mysterious island shrouded in perpetual mist`, 
        `colorful hot air balloons soaring in the sky`, 
        `serene waterfall cascading into a clear pool below`, 
        `ancient tree with a hollow trunk and hidden cavity`, 
        `ramshackle barn nestled in the fields`, 
        `remote cottage atop a hill with breathtaking views`, 
        `quiet cemetery with weathered tombstones`, 
        `humble blacksmith's workshop in a small village`, 
        `hidden cave entrance behind a cascading waterfall`
    ]
    let then = [
        `Go north for ${1 + rollDice(20)} mile(s)`, 
        `Go south for ${1 + rollDice(20)} mile(s)`, 
        `Go east for ${1 + rollDice(20)} mile(s)`, 
        `Go west for ${1 + rollDice(20)} mile(s)`, 
        `Go northeast for ${1 + rollDice(20)} mile(s)`, 
        `Go northwest for ${1 + rollDice(20)} mile(s)`, 
        `Go southeast for ${1 + rollDice(20)} mile(s)`, 
        `Go southwest for ${1 + rollDice(20)} mile(s)`,
        `Continue straight ahead for ${1 + rollDice(20)} mile(s)`, 
        `Follow the winding path for ${1 + rollDice(20)} mile(s)`, 
        `Climb to the top of the nearest hill and look for a landmark`, 
        `Descend into the valley and cross the river`, 
        `Head towards the setting sun for ${1 + rollDice(20)} mile(s)`, 
        `Follow the stars in the night sky for guidance`, 
        `Navigate through the dense forest for ${1 + rollDice(20)} mile(s)`, 
        `Cross the ancient stone bridge over the chasm`, 
        `Scale the rocky cliff to reach higher ground`, 
        `Venture into the dark cave and keep to the right path`, 
        `Take a shortcut through the abandoned mine tunnels`, 
        `Pass through the enchanted field of glowing flowers`, 
        `Follow the footprints left by a mysterious creature`, 
        `Solve the riddle carved on the ancient standing stone`, 
        `Ask the locals for directions to the next landmark`, 
        `Listen to the sound of distant waterfalls and head towards it`, 
        `Follow the river downstream to uncover its secrets`, 
        `Keep an eye out for a peculiar tree with twisted roots`, 
        `Ask the spirits of the forest for guidance`, 
        `Trust your instincts and follow your heart's desire`, 
        `Search for a hidden passage beneath the old ruins`, 
        `Look for a shimmering beacon of light in the night sky`, 
        `Pay attention to the stars and constellations for clues`, 
        `Follow the trail of sparkling crystals`,
        `Listen for the sound of distant drums and follow the rhythm`, 
        `Head towards the highest peak visible in the horizon`, 
        `Navigate through the ancient maze of hedges`, 
        `Follow the ancient road paved with cobblestones`, 
        `Descend into the underground catacombs and search for clues`, 
        `Cross the rope bridge suspended over the deep gorge`, 
        `Look for the remains of an old campfire to follow a traveler's path`, 
        `Enter the enchanted glade and follow the trail of glowing butterflies`, 
        `Climb the spiral staircase of the ruined tower to survey the surroundings`, 
        `Follow the river upstream`, 
        `Search for an abandoned boat by the lakeside and row across`, 
        `Head towards the distant smoke rising from a chimney`, 
        `Follow the alignment of three ancient stones`, 
        `Trace the steps of an old legend passed down through generations`, 
        `Follow the carved arrows on the trees left by a previous adventurer`, 
        `Venture through the echoing cavern`, 
        `Climb to the top of the waterfall to gain a better vantage point, look around`, 
        `Follow the trail of glowing crystals`, 
        `Navigate the treacherous marshland using the raised stepping stones`, 
        `Look for the constellation of the North Star to guide your way`, 
        `Head towards the sound of distant bells tolling in the breeze`, 
        `Search for a set of peculiar runes engraved on a large rock`, 
        `Follow the trail of peculiar animal tracks`, 
        `Venture through the ancient graveyard, following the moss-covered tombstones`, 
        `Head towards the eerie glow emanating from the ghostly marsh`, 
        `Follow the trail of floating lanterns`,
        `Navigate through the twisting canyons by following the river's path`,
        `Climb to the top of the ancient tree and observe the surroundings`,
        `Follow the path of the stars in the night sky`,
        `Head towards the distant sound of thunder and looming dark clouds`,
        `Follow the trail of glowing fireflies guiding you through the dark forest`,
        `Venture into the underground catacombs and follow the flickering torches`,
        `Follow the winding river as it snakes through the landscape`,
        `Navigate the treacherous mountain pass by following the goat tracks`,
        `Head towards the distant sound of laughter and celebration`,
        `Follow the ancient road paved with luminous stones`,
        `Venture into the depths of the haunted forest and face your fears`,
        `Follow the path of petals left behind by a mystical creature`,
        `Head towards the highest tower in the castle and search`,
        `Follow the trail of colorful ribbons`,
        `Venture into the enchanted marsh and follow the path of the wisps`,
        `Follow the winding path of floating lanterns`
       ]
    let until = [
        `mountain shaped like a tooth`, 
        `hill shaped like a saddle`, 
        `cliffs of red stone`, 
        `tiny caves in a white hill`, 
        `old fortress ruins`, 
        `dried up creekbed`, 
        `swift-running river`, 
        `waterfall`, 
        `abandoned village`, 
        `tree with a large hole in it`, 
        `toppled statue of (Deity)`, 
        `landslide of shale and gravel`, 
        `steep-sided valley with blue flowers`, 
        `beach strewn with black seashells`, 
        `broken remains of a watchtower`, 
        `road marker pointing east`, 
        `dilapidated hunter's shack`, 
        `crossroads`, 
        `hand-cut stairway into the hillside`, 
        `canyon with natural stairs leading down`,
        `strange rock formation resembling a dragon's head`, 
        `mysterious cave entrance with glowing markings`, 
        `ancient stone circle surrounded by ancient symbols`, 
        `crystal-clear underground pool hidden in a cavern`, 
        `grove of trees with silver leaves and golden bark`, 
        `large stone archway leading to an unknown realm`, 
        `ruins of an ancient library filled with forgotten knowledge`, 
        `giant stone door with inscriptions and a missing key`, 
        `sunken shipwreck with remnants of a valuable cargo`, 
        `whispering grove where the trees seem to speak`, 
        `eerie silence of a hidden burial ground`, 
        `sacred shrine with offerings left by pilgrims`, 
        `ancient stone monolith with celestial engravings`, 
        `underground labyrinth with a glowing crystal compass`, 
        `entrance to a labyrinth guarded by stone statues`, 
        `meandering path through a forest of colorful mushrooms`, 
        `towering tree with branches forming an intricate pattern`, 
        `series of glowing crystals leading deeper into the earth`, 
        `ghostly apparitions of a forgotten battlefield`, 
        `abandoned mine with the remnants of forgotten treasures`, 
        `hidden chamber filled with shimmering gemstones`, 
        `eerie fog-shrouded swamp with unknown creatures lurking`, 
        `hidden garden with plants that bloom only once in a century`, 
        `hidden valley where time seems to stand still`, 
        `underground chamber with an ancient map etched on the walls`, 
        `portal shimmering with energy, leading to unknown realms`,
        `ancient tree with carvings detailing a legendary tale`, 
        `forgotten altar atop a hill with offerings of the past`, 
        `peculiar formation of rocks resembling a celestial map`, 
        `serene grove filled with bioluminescent fireflies at night`, 
        `abandoned observatory with a telescope pointing skyward`, 
        `hidden hot spring with rejuvenating and healing properties`, 
        `ancient stone bridge spanning a wide and rushing river`, 
        `massive hollow tree housing an ecosystem of unique creatures`, 
        `cave filled with ancient hieroglyphs and mysterious symbols`, 
        `majestic waterfall cascading into a shimmering pool below`, 
        `ancient sundial marking the passage of time with precision`, 
        `statue garden with lifelike statues that seem to follow you`, 
        `sprawling labyrinth of interconnected underground tunnels`, 
        `petrified forest where trees appear frozen in time and stone`, 
        `ethereal glade with floating orbs of light guiding the way`, 
        `forgotten crypt filled with the whispers of lost souls`, 
        `hidden sanctuary protected by ancient warding spells`, 
        `underground river leading to an uncharted subterranean lake`, 
        `clearing where the stars align to form a celestial pattern`, 
        `ruined castle with crumbling walls and a dark past`, 
        `shimmering aurora dancing across the night sky, illuminating the path`
    ]
    let thenTwo = [
        `go north for ${1 + rollDice(30)} mile(s)`, 
        `go south for ${1 + rollDice(30)} mile(s)`, 
        `go east for ${1 + rollDice(30)} mile(s)`, 
        `go west for ${1 + rollDice(30)} mile(s)`, 
        `go northeast for ${1 + rollDice(30)} mile(s)`, 
        `go northwest for ${1 + rollDice(30)} mile(s)`, 
        `go southeast for ${1 + rollDice(30)} mile(s)`, 
        `go southwest for ${1 + rollDice(30)} mile(s)`,
        `follow the winding river for ${1 + rollDice(30)} mile(s)`,
        `walk along the coastal shore for ${1 + rollDice(30)} mile(s)`,
        `continue through the rolling hills for ${1 + rollDice(30)} mile(s)`,
        `climb to higher ground and head ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `descend into the valley and follow the stream for ${1 + rollDice(30)} mile(s)`,
        `venture into the dense forest and keep to the main trail for ${1 + rollDice(30)} mile(s)`,
        `follow the road marker pointing towards a nearby village for ${1 + rollDice(30)} mile(s)`,
        `cross the stone bridge and head ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `navigate through the rocky canyon to the other side for ${1 + rollDice(30)} mile(s)`,
        `make your way across the open plains heading ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `follow the footsteps of wildlife, they may lead you ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `walk through the sunlit meadow with wildflowers for ${1 + rollDice(30)} mile(s)`,
        `climb the gentle slope of a hill and head ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `descend into the shadowy ravine and head ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `follow the ancient cobblestone road leading ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `make your way through the swaying fields of tall grass heading ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `navigate the winding mountain pass going ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `follow the path of scattered stones marking the way ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `walk along the riverbank and head ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `climb up the ancient stone steps and head ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `descend into the cool shade of the forest and head ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `make your way through the vast fields of wheat heading ${pickDirection()} for ${1 + rollDice(30)} mile(s)`,
        `follow the trail of animal tracks leading ${pickDirection()} for ${1 + rollDice(30)} mile(s)`
        ]
    let untilTwo = [
        `rock shaped like a heart`, 
        `mountain shaped like a bird's head`, 
        `petrified forest`, 
        `salt lake`, 
        `dried up swampland`, 
        `broken bridge`, 
        `old abandoned mill`, 
        `the ruined tower of the famous mage`, 
        `the ancient cemetery`, 
        `the mossy limestone cliffs`, 
        `the old granite quarry`, 
        `the abandoned campgrounds`, 
        `the vandalized statue of the former ruler`, 
        `the crossroads`, 
        `the road marker pointing West`, 
        `minaret`, 
        `quicksand`, 
        `hills honeycombed with caves`, 
        `old King's Forest`,
        `the ancient stone archway covered in vines`, 
        `the sparkling river winding through the valley`, 
        `the dilapidated castle perched atop the hill`, 
        `the fields of sunflowers stretching as far as the eye can see`, 
        `the towering waterfalls cascading down the rocky cliffside`, 
        `the eerie mist-covered moors with unknown secrets`, 
        `the mysterious standing stones arranged in a perfect circle`, 
        `the hidden oasis with lush vegetation and clear blue water`, 
        `the ancient battleground where legends once clashed`, 
        `the enormous tree with roots that form a natural bridge`, 
        `the abandoned windmill standing tall against the horizon`, 
        `the glistening cave walls adorned with shimmering crystals`, 
        `the secluded beach with smooth stones and seashells`, 
        `the sacred grove where rare and magical creatures dwell`, 
        `the labyrinthine catacombs with countless winding passages`, 
        `the hauntingly beautiful melody coming from a distant harp`, 
        `the mesmerizing display of colorful northern lights in the sky`, 
        `the peculiar rock formation resembling a sleeping giant`, 
        `the massive boulder balanced precariously on the edge of a cliff`, 
        `the serene pond with floating water lilies and croaking frogs`, 
        `the ancient tree stump with mysterious carvings all over it`, 
        `the remnants of an old shipwreck half-buried in the sand`, 
        `the hidden glade where fireflies illuminate the night sky`, 
        `the enigmatic rune-inscribed stone said to grant wisdom`, 
        `the towering sand dunes sculpted by the relentless wind`, 
        `the majestic ruins of a forgotten temple with ancient relics`, 
        `the majestic herd of wild horses galloping across the plains`, 
        `the shimmering mirage that dances on the horizon`, 
        `the eerie echo chamber hidden within a rocky cavern`,
        `the ancient tree with branches forming a natural archway`, 
        `the sparkling emerald lake nestled between tall mountains`, 
        `the labyrinth of underground tunnels with ancient carvings`, 
        `the serene garden with exotic flowers and calming fountains`, 
        `the towering statue of a legendary hero overlooking the land`, 
        `the hidden hot springs with warm, healing waters`, 
        `the mystical cave with glowing crystals lining the walls`, 
        `the ancient stone steps leading to a hidden observatory`, 
        `the vast expanse of golden wheat fields swaying in the breeze`, 
        `the mysterious fog-covered marshland with strange lights`, 
        `the sunlit glen where rare creatures frolic in harmony`, 
        `the ancient battleground where tales of heroes were born`, 
        `the towering cliffs with breathtaking views of the sea below`, 
        `the tranquil pond where colorful koi fish swim gracefully`, 
        `the crumbling ruins of an old castle lost to time`, 
        `the mystical grove with trees that whisper ancient secrets`, 
        `the hidden cave with walls adorned in sparkling gemstones`, 
        `the ancient stone circle believed to have mystical powers`, 
        `the cascading waterfalls with rainbows forming in the mist`, 
        `the abandoned shipwreck entangled in a web of seaweed`, 
        `the majestic grove of ancient trees that touch the sky`, 
        `the towering ice cave with dazzling ice formations`, 
        `the quiet village where time seems to slow down`, 
        `the ancient ruins of a forgotten civilization`, 
        `the mysterious cave paintings that tell ancient stories`, 
        `the enchanted forest where trees come to life at night`, 
        `the tranquil meadow with a carpet of colorful wildflowers`, 
        `the vast desert with shifting sand dunes and mirages`, 
        `the hidden underground chamber filled with ancient treasures`, 
        `the ancient stone bridge spanning a roaring river`, 
        `the abandoned temple with mysterious symbols on its walls`, 
        `the peaceful oasis with palm trees and cool, clear water`, 
        `the eerie fog-covered graveyard with weathered tombstones`, 
        `the enchanting glade where fairies are said to dance at dusk`, 
        `the ancient well with water rumored to grant eternal life`, 
        `the remote waterfall hidden deep within the forest`, 
        `the sprawling vineyard with rows of ripe, juicy grapes`, 
        `the secluded cave with walls adorned in ancient hieroglyphs`, 
        `the towering lighthouse standing tall on a rocky coastline`
    ]
    let thenThree = [
        `go north for ${1 + rollDice(15)} mile(s)`, 
        `go south for ${1 + rollDice(15)} mile(s)`, 
        `go east for ${1 + rollDice(15)} mile(s)`, 
        `go west for ${1 + rollDice(15)} mile(s)`, 
        `go northeast for ${1 + rollDice(15)} mile(s)`, 
        `go northwest for ${1 + rollDice(15)} mile(s)`, 
        `go southeast for ${1 + rollDice(15)} mile(s)`, 
        `go southwest for ${1 + rollDice(15)} mile(s)`,
        `follow the path of the glowing fireflies`, 
        `venture through the misty swamp of the lost souls`, 
        `cross the bridge guarded by stone gargoyles`, 
        `ascend the staircase of the ancient spiral tower`, 
        `follow the haunting melody of a distant flute`, 
        `navigate through the labyrinth of twisted tree roots`, 
        `follow the stars that align with a hidden constellation`, 
        `climb the cliffside where the winds whisper a secret`, 
        `make your way through the shifting sands of the time desert`, 
        `follow the trail of glowing crystals illuminating the path`, 
        `venture into the enchanted forest where trees come alive`, 
        `follow the moonlit river leading to a mysterious cavern`, 
        `climb the giant mushroom staircase to the floating island`, 
        `make your way through the valley of echoing whispers`, 
        `follow the trail of floating lanterns into the hidden cave`, 
        `navigate through the maze of mirrors reflecting illusions`, 
        `venture into the underground catacombs where shadows dance`, 
        `follow the ancient prophecy etched on the stone walls`, 
        `climb the crystal staircase to the realm of eternal twilight`, 
        `make your way through the dense fog covering the forgotten land`, 
        `follow the trail of ancient runes leading to the time portal`, 
        `venture into the abandoned mine with echoes of lost miners`, 
        `navigate through the enchanted marsh with glowing will-o'-wisps`, 
        `follow the trail of mythical creatures towards the hidden shrine`, 
        `climb the tower of riddles to unveil the final path`, 
        `make your way through the mystical waterfall's hidden entrance`, 
        `follow the trail of enchanted feathers left by the mythical phoenix`, 
        `venture into the cave of echoes where past and future intertwine`, 
        `navigate through the enchanted garden with talking statues`, 
        `follow the map of stars`, 
        `climb the ancient tree with branches revealing the way forward`, 
        `make your way through the shifting sands of the labyrinth desert`, 
        `follow the trail of shimmering pixie dust guiding the path`, 
        `venture into the floating cloud passage to reach the celestial isle`, 
        `navigate through the ancient library with secrets written in books`, 
        `follow the melody of the magical flute`,
        `follow the path along the riverbank lined with weeping willows`, 
        `navigate through the narrow mountain pass with towering cliffs`, 
        `make your way through the ancient ruins of a forgotten city`, 
        `climb the steep hills to reach the plateau with panoramic views`, 
        `follow the ancient cobblestone road leading to the destination`, 
        `venture into the dense forest with sunlight filtering through trees`, 
        `navigate through the rolling hills dotted with grazing cattle`, 
        `follow the winding trail along the coastline with crashing waves`, 
        `climb the rocky mountain trail to the summit for a breathtaking view`, 
        `make your way through the vast meadow of wildflowers in bloom`, 
        `follow the footprints of wildlife leading in the right direction`, 
        `venture into the peaceful valley surrounded by majestic mountains`, 
        `navigate through the open plains with wild grass swaying in the wind`, 
        `follow the path along the peaceful stream to a hidden waterfall`, 
        `climb the gentle slope of the hill to overlook the entire landscape`, 
        `make your way through the quiet village with friendly locals`, 
        `follow the winding road bordered by colorful fields of crops`, 
        `venture into the serene forest with sunlight dappling the ground`, 
        `navigate through the quaint town with charming architecture`, 
        `follow the trail marked by old road signs pointing the way`, 
        `climb the stony steps leading to an ancient watchtower ruins`, 
        `make your way through the cool, shaded canyon with echoing sounds`, 
        `follow the river's bend to the spot where it meets a tranquil lake`, 
        `venture into the picturesque vineyard with rows of grapevines`, 
        `navigate through the bustling market filled with vendors and stalls`, 
        `follow the path along the cliffs with stunning coastal views`, 
        `climb the wooden lookout tower for a bird's-eye view of the land`, 
        `make your way through the charming village's narrow, cobbled streets`, 
        `follow the trail surrounded by tall trees in the ancient forest`, 
        `venture into the peaceful countryside with rolling green hills`, 
        `navigate through the scenic valley with fields of wildflowers`, 
        `follow the stone path leading to the entrance of an old castle`, 
        `climb the gentle slope of the hill for an expansive horizon view`, 
        `make your way through the orchard with fruit-laden trees`, 
        `follow the winding road through a picturesque countryside`, 
        `venture into the quiet woods with the rustling of leaves above`, 
        `navigate through the quaint town with charming old buildings`, 
        `follow the riverbank trail with soothing sounds of flowing water`
       ]
    let xMarks = [
        `buried at the foot of a cliff`, 
        `buried under a mighty oak tree`, 
        `buried under some tower ruins`, 
        `buried under a pile of skulls`, 
        `buried in the grave of (famous person)`, 
        `hidden at the top of an old tower`, 
        `hidden behind an old painting`, 
        `hidden at the bottom of an old rabbit's warren`, 
        `hidden in the bole of an ancient elm tree`, 
        `hidden in a shipwreck's hold`, 
        `guarded by assassins`, 
        `guarded by monsters`, 
        `guarded by soldiers`, 
        `guarded by spirits`, 
        `guarded by a terrible monster`, 
        `protected by magical wards`, 
        `protected by astral locks`, 
        `protected by physical traps`, 
        `protected by necromantic curses`, 
        `protected by spiritual prayers`,
        `concealed in a secret compartment beneath the throne`, 
        `entombed within a sacred temple guarded by ancient priests`, 
        `hidden within the ancient catacombs beneath the city`, 
        `safeguarded in a hidden chamber accessible only by a riddle`, 
        `stashed in a secret cave behind a cascading waterfall`, 
        `locked away in a forgotten vault beneath the mansion`, 
        `tucked inside a statue with a hidden mechanism to reveal it`, 
        `enshrined within an old chapel surrounded by enigmatic symbols`, 
        `protected within a magical mirror accessible by a special chant`, 
        `veiled within the ethereal realm, accessible through a portal`, 
        `kept safe in a mystical chest guarded by celestial guardians`, 
        `hidden within the labyrinth of illusions and shifting corridors`, 
        `placed within a treasure chest buried deep in the haunted graveyard`, 
        `concealed in a chest hidden beneath the ocean floor on a sunken ship`, 
        `ensconced within the heart of a dormant volcano with fiery guardians`, 
        `kept secure in a mystical garden, guarded by mythical creatures`, 
        `hidden beneath the ancient stone altar of a long-forgotten temple`, 
        `entwined within the roots of the World Tree, protected by ancient magic`, 
        `enshrined in a sacred shrine within a secluded and forgotten shrine`, 
        `concealed in the dream realm, accessible only during certain moon phases`,
        `hidden within the heart of a lush and ancient forest`, 
        `buried beneath the floor of an abandoned castle's great hall`, 
        `concealed within the deepest chamber of an underground dungeon`, 
        `kept safe in an old and forgotten cave deep within the mountains`, 
        `tucked away inside a well-protected chamber in an ancient pyramid`, 
        `enshrined within a sacred temple protected by devoted priests`, 
        `concealed within a remote and secluded island surrounded by reefs`, 
        `locked away in a secret chamber beneath the floor of a church`, 
        `hidden in the shadows of a massive and ancient stone colossus`, 
        `guarded by the enigmatic and intelligent guardians of an ancient race`, 
        `concealed within the hollowed-out trunk of a massive ancient tree`, 
        `buried within the grounds of an ancient battleground of heroes past`, 
        `kept secure within the treasury of a powerful and ancient king's tomb`, 
        `hidden deep within the vast network of underground catacombs`, 
        `veiled behind a hidden door disguised as an ordinary bookshelf`, 
        `concealed in a long-forgotten underground city lost to the ages`, 
        `enshrined within a sacred cave sought after by intrepid explorers`, 
        `guarded by the powerful and mystical beings of a hidden realm`, 
        `buried deep beneath the shifting sands of a vast desert wasteland`, 
        `kept safe within an ancient library filled with forbidden knowledge`, 
        `hidden within the ruins of an ancient and sunken city below the sea`, 
        `tucked away inside the crumbling walls of a once-mighty fortress`, 
        `concealed within the heart of a dense and uncharted jungle wilderness`, 
        `ensconced within the secret chambers of an enigmatic and haunted mansion`, 
        `guarded by the mythical creatures said to protect ancient treasures`, 
        `hidden within the depths of a treacherous and unexplored cave system`, 
        `kept secure within the ancient treasury of a long-lost civilization`, 
        `veiled behind an intricate puzzle that only the worthy can decipher`, 
        `concealed within the magical realm accessible through a mystical portal`, 
        `enshrined within the sacred grounds of an ancient and forgotten temple`, 
        `hidden in plain sight among the bustling streets of a thriving city`, 
        `buried beneath a field of ancient and mystical standing stone formations`, 
        `guarded by the spectral spirits of the long-deceased guardians of old`, 
        `concealed within a hidden and enchanted garden with alluring beauty`,
        `concealed within the crypt of a malevolent and vengeful spirit`, 
        `hidden deep within a haunted mansion with eerie apparitions`, 
        `buried beneath a cursed graveyard with restless, wandering souls`, 
        `kept safe in the realm of the undead, guarded by ancient vampires`, 
        `veiled within the forsaken catacombs haunted by ghostly whispers`, 
        `guarded by a spectral wraith, forever bound to protect its resting place`, 
        `hidden within the shadowy depths of a spectral forest with glowing eyes`, 
        `enshrined within the chamber of a malevolent sorcerer's cursed tower`, 
        `concealed beneath the eerie glow of a haunted swamp with glowing will-o'-wisps`, 
        `tucked away within the haunted shipwreck, surrounded by the ghostly crew`, 
        `kept secure in the forgotten and desolate manor plagued by dark enchantments`, 
        `hidden within the chilling underground catacombs haunted by lost souls`, 
        `veiled behind a cursed painting that brings misfortune to those who gaze upon it`, 
        `concealed within the depths of a sinister cave said to be cursed by dark magic`, 
        `enshrined within the eerie chamber of an ancient witch's cursed sanctuary`, 
        `guarded by the malevolent spirits of long-deceased guardians with haunting gazes`, 
        `hidden in the heart of a spectral marsh where eerie mists obscure all sight`, 
        `buried deep within a cursed cemetery with tombstones that shift and move`, 
        `kept safe within a macabre crypt guarded by skeletal sentinels of the night`, 
        `veiled behind a cursed tapestry that seems to show the future in haunting images`, 
        `concealed within the haunting echo chamber, where voices of the past still linger`, 
        `enshrined within the chilling temple of a forgotten deity, said to bring misfortune`, 
        `hidden within the chamber of a malevolent spirit, doomed to guard the treasure`, 
        `guarded by the restless souls of those who sought the treasure but met their doom`, 
        `concealed beneath the eerie glow of the spectral will-o'-wisps, leading the way`, 
        `ensconced within the abandoned mansion with doors that lead to other dimensions`, 
        `kept secure within the cursed tomb of a powerful sorcerer seeking eternal life`, 
        `hidden deep within the cursed forest, where trees whisper eerie incantations`, 
        `veiled behind the ghostly visage of a long-lost spirit who still mourns its loss`, 
        `enshrined within the spectral chapel, where echoes of haunting hymns can be heard`, 
        `guarded by the malevolent spirits of long-deceased warriors who still fight on`, 
        `hidden within the labyrinth of mirrors, where reflections show otherworldly realms`,
        `concealed within an underground chamber filled with sparkling gemstones`, 
        `hidden within a time rift, accessible only during certain celestial events`, 
        `veiled behind an illusionary wall that only reveals itself to the worthy`, 
        `enshrined within a majestic statue that comes to life to protect the treasure`, 
        `guarded by a group of reclusive scholars seeking the knowledge it holds`, 
        `hidden within an enchanted mirror that transports explorers to another realm`, 
        `tucked away inside a music box that plays a haunting melody when opened`, 
        `kept safe within the pages of a magical book that can rewrite reality`, 
        `veiled behind an ever-shifting maze that rearranges itself to confound intruders`, 
        `concealed within an elaborate puzzle box that challenges the mind of its solver`, 
        `enshrined within the heart of a sentient tree, the oldest being in the land`, 
        `hidden within a constellation of stars, accessible by deciphering the night sky`, 
        `guarded by an ancient and benevolent spirit who tests the purity of the seekers`, 
        `veiled behind a painting that comes to life, taking those who gaze upon it inside`, 
        `kept secure within a magic lantern that can show glimpses of distant lands`, 
        `hidden within a mystical snow globe that reveals the treasure upon shaking`, 
        `concealed within a series of magical portals, each leading to a different location`, 
        `enshrined within a magical crystal, which absorbs and amplifies the energy around it`, 
        `guarded by a riddle-speaking guardian, offering the treasure to those who solve it`, 
        `hidden within a magical puzzle maze where the walls shift and change positions`, 
        `veiled behind an ancient map that requires the exploration of multiple realms`, 
        `concealed within an otherworldly garden, where plants come to life and guide the way`, 
        `kept safe within a mystical fountain, accessible only to those with pure intentions`, 
        `hidden within the dreams of a sleeping dragon, guarded by the power of imagination`, 
        `guarded by a tribe of benevolent forest spirits who test the seekers' intentions`, 
        `enshrined within a mysterious crystal ball that reveals glimpses of the past and future`, 
        `tucked away inside a magical lantern that illuminates the way to the treasure`, 
        `veiled behind an ancient and enchanted tapestry that tells the story of its location`, 
        `concealed within a secret chamber that can only be accessed through a magical key`, 
        `hidden within a celestial vault, accessible during a celestial alignment every century`, 
        `kept secure within an unbreakable vault, surrounded by mirrors reflecting true selves`, 
        `guarded by a riddle-loving sphinx, who challenges seekers to prove their worthiness`, 
        `veiled behind a shimmering waterfall that reveals a hidden cave behind its curtain`, 
        `enshrined within a chamber protected by the ancient spirits of long-lost explorers`, 
        `hidden within a puzzle cube that shifts its shape and can only be solved with skill`, 
        `concealed within a mysterious mist that only reveals the treasure to the chosen one`,
        `concealed within the pocket dimension of an eccentric interdimensional traveler`, 
        `hidden within the twisted and ever-shifting labyrinth of a mad sorcerer's mind`, 
        `veiled within a mysterious void where the laws of physics and reality bend`, 
        `enshrined within an animated painting that acts as a portal to other realms`, 
        `guarded by an enigmatic and quirky group of time-traveling aliens`, 
        `hidden within a mystical chamber accessible only through a series of dance moves`, 
        `tucked away inside an ancient puzzle box that responds to laughter and jokes`, 
        `kept safe in a sentient treasure chest that befriends and helps the seekers`, 
        `veiled behind a series of whimsical riddles that challenge conventional logic`, 
        `concealed within a gigantic kaleidoscope that transports the explorers to new realms`, 
        `enshrined within the colorful and surreal dreamscape of a whimsical artist`, 
        `hidden within a mystical tree that grants visions to those who touch its bark`, 
        `guarded by a band of enigmatic and whimsical forest creatures with strange powers`, 
        `veiled within an underwater cave where the laws of buoyancy are magically altered`, 
        `kept secure in a chamber that only unlocks its door with a tune played on a kazoo`, 
        `hidden within a magical puppet show where the marionettes come to life at night`, 
        `concealed within a floating island made of giant balloons in the sky`, 
        `tucked away within a secret sanctuary where time flows backward and forward`, 
        `enshrined within the eerie melody of a music box that plays on its own`, 
        `guarded by a mysterious creature that communicates through peculiar dance moves`, 
        `veiled behind a curtain of shimmering bubbles that lead to a submerged grotto`, 
        `concealed within an enormous hourglass where time and space intertwine`, 
        `hidden within an ancient library of peculiar and cryptic books that change content`, 
        `kept safe in a magical, bottomless pouch carried by a peculiar traveling merchant`, 
        `veiled within an ever-morphing, living maze that rearranges itself constantly`, 
        `enshrined within a room with walls adorned in optical illusions and puzzles`, 
        `guarded by a mystical being that grants passage only to those who tell jokes`, 
        `hidden within a mysterious forest where trees whisper riddles to passing travelers`, 
        `tucked away in a pocket dimension accessible through a peculiar, rotating mirror`, 
        `concealed within a bizarre realm that can only be accessed through sleepwalking`, 
        `veiled behind an enormous, sentient and talking puppet that holds the key to entry`, 
        `kept secure in a chamber of mirrors, each reflecting a different version of the seeker`, 
        `hidden within the realm of a mischievous trickster spirit who loves to play pranks`, 
        `enshrined within a temple guarded by a peculiar order of shape-shifting guardians`, 
        `guarded by a group of extraterrestrial beings who communicate through strange symbols`, 
        `veiled within a foggy, ethereal dimension accessible only during the witching hour`, 
        `concealed within an enchanted carnival where attractions come to life after midnight`, 
        `hidden within the bizarre and psychedelic landscape of a whimsical dream world`,
        `tucked away inside a room of colorful inflatable bouncy castles`, 
        `veiled within a gigantic treasure chest-shaped piñata waiting to be cracked open`, 
        `enshrined within a room filled with giant bubblegum bubbles floating in the air`, 
        `guarded by a troop of mischievous but friendly gnomes with a love for pranks`, 
        `hidden within a treasure-themed escape room filled with puzzles and challenges`, 
        `concealed within a fantastical treehouse adorned with playful gadgets and toys`, 
        `kept safe in the care of a magical puppeteer and his lively and animated puppets`, 
        `veiled behind a whimsical rainbow-colored waterfall with hidden chambers`, 
        `guarded by a group of friendly and chatty ghosts who love to tell jokes`, 
        `hidden within a room where gravity behaves oddly, leading to fun upside-down antics`, 
        `tucked away in a mystical fairy garden, home to playful and mischievous fairies`, 
        `enshrined within a whimsical carousel where the animals come to life at night`, 
        `veiled within a giant treasure chest-shaped sandbox filled with hidden surprises`, 
        `concealed behind a magical painting that brings to life the characters within`, 
        `hidden within a whimsical candyland with edible landscapes and sweet surprises`, 
        `kept secure within an enchanted treasure hunt board game come to life`, 
        `guarded by a group of friendly and quirky animated statues that talk and sing`, 
        `veiled behind an ever-changing maze of funhouse mirrors and optical illusions`, 
        `enshrined within a room where everything is oversized, making seekers feel tiny`, 
        `hidden within a fantastical toy factory run by playful and helpful toy makers`, 
        `tucked away within a hidden garden with flowers that light up like lanterns`, 
        `concealed behind an enormous, magical tapestry that tells stories of adventure`, 
        `veiled within a room of levitating objects and floating furniture in zero gravity`, 
        `guarded by a group of whimsical and mischievous animated toy soldiers`, 
        `hidden within a lively circus tent filled with acrobats, clowns, and circus animals`, 
        `kept safe within a magical library where books come to life and guide the way`, 
        `enshrined within a room that transforms into a giant puzzle when the moon rises`, 
        `veiled behind an enchanting waterfall that leads to a shimmering underwater cave`, 
        `concealed within a magical garden maze where the hedges whisper clues`, 
        `hidden within a room filled with magical flying broomsticks and floating objects`, 
        `guarded by a group of playful and mischievous mythical creatures with good intentions`, 
        `tucked away in a room filled with delightful and playful illusions and tricks`, 
        `enshrined within a room where the walls are made of colorful and interactive art`, 
        `veiled within a fantastical library filled with books that contain incredible adventures`, 
        `hidden behind a series of magical paintings that act as doorways to other worlds`
    ]

    document.getElementById("Treasure Map").innerHTML = `The map starts at the ${searchArray(start)}. ${searchArray(then)} until you find the ${searchArray(until)}. Then ${searchArray(thenTwo)} until you find ${searchArray(untilTwo)}. Lastly ${searchArray(thenThree)} and you will find the treasure ${searchArray(xMarks)}.`
};
function treasureChest() {
    let style = [
        "crude", 
        "standard", 
        "fancy", 
        "elven", 
        "bejeweled", 
        "draconic", 
        "dwarven", 
        "pink, gem encrusted", 
        "pirate", 
        "woven", 
        "creepy", 
        "heavy duty",
        "gilded",
        "ancient",
        "enchanting",
        "rustic",
        "glowing",
        "mechanical",
        "ornate wooden",
        "crystal-studded",
        "bone-carved",
        "feather-lined",
        "mermaid-scale",
        "intricately carved",
        "mirrored",
        "mystical",
        "floating",
        "cursed",
        "time-worn",
        "enchanted",
        "celestial",
        "rainbow-hued",
        "music-playing",
        "invisible to the naked eye",
        "marble and gold",
        "leather-bound",
        "stained glass",
        "whispering",
        "silver filigree",
        "clockwork",
        "moonlit",
        "forgotten",
        "crystal-clear",
        "crimson velvet",
        "animated",
        "jewel-encrusted",
        "glistening with dew",
        "frozen in ice",
        "ivory-inlaid",
        "phoenix feather-covered",
        "galactic",
        "stardust-infused",
        "dragon scale",
        "reptilian",
        "frozen flame",
        "astral",
        "secret compartment",
        "unbreakable",
        "spellbound",
        "diamond-studded",
        "amber-encased",
        "spell-scroll-covered",
        "invisible to magical detection"   
    ]

    let material = [
        "old, rotting wood", 
        "sturdy oak", 
        "diamondwood", 
        "iron", 
        "steel", 
        "bone", 
        "obsidian", 
        "glass", 
        "platinum", 
        "electrum", 
        "silver", 
        "gold", 
        "ebony", 
        "stone",
        "dragon scale", 
        "crystal", 
        "pearlescent shell", 
        "enchanted ice", 
        "living vines", 
        "moonstone", 
        "ancient parchment", 
        "meteorite metal", 
        "frozen water", 
        "celestial star metal", 
        "bloodwood", 
        "thunderstone", 
        "magical crystal", 
        "gilded coral", 
        "stardust-infused glass", 
        "fire-ruby", 
        "time-worn leather", 
        "whispering silk", 
        "voidstone", 
        "living wood", 
        "mermaid-scale", 
        "galactic meteorite", 
        "phoenix feather", 
        "golden-threaded fabric", 
        "spellbound velvet", 
        "eternal ice", 
        "ancient dragon bone", 
        "rainbow gemstone", 
        "astral pearl", 
        "frozen flame crystal", 
        "amber-encased fossil", 
        "ancient silvered bronze", 
        "spell-scroll parchment", 
        "fae-glowing petals", 
        "titanium alloy", 
        "dragonhide", 
        "ethereal moonlight glass"
    ]

    let trim = [
        "iron", 
        "steel", 
        "brass", 
        "silver", 
        "gold", 
        "bronze", 
        "ebony", 
        "leather", 
        "wood", 
        "mithril", 
        "adamantite", 
        "dragon leather",
        "sapphire-encrusted", 
        "ruby-embellished", 
        "emerald-inlaid", 
        "diamond-studded", 
        "pearl-bordered", 
        "obsidian-carved", 
        "crystal-infused", 
        "platinum-filigree", 
        "opalescent-lined", 
        "enamel-coated", 
        "garnet-trimmed", 
        "silver-threaded", 
        "gold-plated", 
        "titanium-accented", 
        "moonstone-encrusted", 
        "amethyst-edged", 
        "amber-coated", 
        "topaz-embossed", 
        "coral-encrusted", 
        "stardust-speckled", 
        "ivory-inlaid", 
        "copper-wrought", 
        "crimson-stained", 
        "crystal-clear", 
        "silk-lined", 
        "leather-bound", 
        "sapphire-adorned", 
        "ruby-trimmed", 
        "emerald-bordered", 
        "diamond-inset", 
        "pearl-encrusted", 
        "obsidian-adorned", 
        "crystal-etched", 
        "platinum-laced", 
        "opalescent-rimmed", 
        "enamel-studded", 
        "garnet-accented", 
        "silver-laced", 
        "gold-encrusted", 
        "titanium-bordered", 
        "moonstone-trimmed", 
        "amethyst-encased", 
        "amber-bordered", 
        "topaz-inlaid", 
        "coral-trimmed", 
        "stardust-embellished", 
        "ivory-lined", 
        "copper-trimmed", 
        "crimson-tinged", 
        "crystal-gemmed", 
        "silk-embroidered", 
        "leather-wrapped",
        "made of dragon scale", 
        "reminiscent of phoenix feathers", 
        "inlaid with unicorn hair", 
        "reminscent of sylvan bark", 
        "covered in celestial ribbon", 
        "made of volcanic obsidian", 
        "studded with frozen ice shards", 
        "covered in time-worn runes", 
        "studded with moonlit pearls", 
        "studded with ethereal moonstone", 
        "carved to look likemermaid scale", 
        "reminiscent of angelic feathers", 
        "studded with shadowy onyx", 
        "reminiscent of fae butterfly wings", 
        "covered in thunderbolt etchings", 
        "mad eof crimson dragon leather", 
        "made of iridescent beetle carapace", 
        "gemstone-embedded", 
        "inlaid with lunar crystal", 
        "made of carved ancient bone", 
        "starlight-embossed", 
        "covered in dreamweaver silk", 
        "made of crystal spiderweb", 
        "made of enchanted vine", 
        "covered in forgotten glyph markings", 
        "inlaid with galactic comet fragments", 
        "peppered with sun-kissed sand", 
        "reminsicent of moonlit moth wings", 
        "surrounded by whispering spirits", 
        "covered in living plant tendrils", 
        "inlaid with iridescent moonstone", 
        "studded with sunburst gemstones", 
        "inlaid with whalebone", 
        "covered with a feathered serpent motif", 
        "glowing with an ethereal starlight", 
        "covered in mythical creature engravings", 
        "inlaid with seafoam coral tracings", 
        "embedded with frozen crystal shards", 
        "glowing with a luminous firefly glow", 
        "covered in spell-sealed runes", 
        "made of ancient tree bark", 
        "inlaid with oceanic mother-of-pearl", 
        "glowing with an enchanted rainbow aura", 
        "peppered with spellbound crystal filaments", 
        "studded with soul-bonded gemstones", 
        "covered in timeless celestial motifs", 
        "covered in stardust-woven fabric", 
        "covered in whispering wind engravings", 
        "reminsicent of magical feather quills", 
        "covered in dreamcatcher beadwork", 
        "reminsicent of galactic nebula swirls", 
        "reminsicent of a frozen starry night", 
        "glowing with eternal ethereal flames", 
        "reminsicent of fae enchanted leaves", 
        "covered in shadowy moonlit runes"    
    ]

    let mark = [
        "artistic scrollwork", 
        "a tree pattern", 
        "dwarven runes", 
        "elvish script", 
        "a lion emblem", 
        "a carving of a dragon", 
        "a decorative skull relief", 
        "embedded glowing crystals", 
        "mystic sigils", 
        "staring eyes", 
        "claw-like feet", 
        "a bas-relief of a battle",
        "an intricate labyrinth design",
        "a celestial constellation",
        "phoenix feathers in a circular pattern",
        "ancient hieroglyphs depicting a forgotten legend",
        "twisting serpent motifs",
        "whispering wisps entwined",
        "intricate clockwork gears and cogs",
        "a celestial spiral of stars",
        "a majestic griffin in flight",
        "an ocean wave with pearl droplets",
        "an ethereal moonlit night",
        "a roaring waterfall cascading",
        "a blazing sun with fiery rays",
        "enchanting musical notes",
        "a compass rose pointing to adventure",
        "interlocking puzzle pieces",
        "a keyhole to unlock hidden secrets",
        "a winged angel with outstretched arms",
        "a howling wolf under a crescent moon",
        "a thunderous storm with lightning bolts",
        "a swirling vortex to another realm",
        "a rose with thorns and blooming petals",
        "a mystical hourglass with sand flowing",
        "ancient tree roots embracing the chest",
        "an all-seeing eye in a triangle",
        "a labyrinth of twisting paths",
        "a radiant sunburst with rays extending",
        "a pair of majestic phoenixes rising",
        "a maze of mirrored reflections",
        "a cascading waterfall in a lush forest",
        "a shimmering peacock in full display",
        "a celestial compass guiding the way",
        "a winding dragon encircling the chest",
        "an intricate web spun by a spider",
        "a fierce thunderstorm with lightning",
        "a glimmering crescent moon",
        "a howling wolf with lunar backdrop",
        "a fiery phoenix rising from the ashes",
        "a clockwork heart at the center",
        "a celestial map of the night sky",
        "a mythical sea creature in motion",
        "an enchanted forest with magical beings",
        "a radiant sun with intricate rays",
        "a swirling galaxy of stars",
        "an angelic figure with divine wings",
        "a maze of intricate labyrinths",
        "a shimmering waterfall in the moonlight",
        "a majestic peacock displaying its feathers",
        "a celestial compass with astral symbols",
        "a twisting dragon intertwining",
        "an ethereal spider weaving its web",
        "a stormy seascape with crashing waves",
        "a radiant crescent moon with stars",
        "a wolf in mid-howl under the night sky",
        "a fiery phoenix with vibrant colors",
        "an intricate clockwork mechanism",
        "a celestial map charting the constellations",
        "a mythical creature emerging from the sea",
        "a mystical forest filled with enchantment",
        "a radiant sunburst with intricate details",
        "a swirling galaxy with nebulas",
        "a divine angelic figure with outstretched arms",
        "an intricate labyrinth with hidden paths",
        "a shimmering waterfall in a magical glade",
        "a peacock in resplendent display of feathers",
        "a celestial compass guiding through realms",
        "a dragon coiled around the treasure chest",
        "an intricate spiderweb with dewdrops",
        "a turbulent storm with thunder and lightning",
        "a luminous crescent moon with celestial beings",
        "a fiery phoenix in a display of rebirth",
        "an ornate clockwork mechanism",
        "a celestial map with mythical symbols",
        "a mythical sea serpent rising from the depths",
        "an enchanted forest with mystical creatures",
        "a radiant sun with celestial rays",
        "a swirling galaxy with cosmic wonders",
        "an angelic figure with divine wings and a halo",
        "a complex labyrinth with hidden treasures",
        "a shimmering waterfall with magical energies",
        "a peacock with mesmerizing patterns",
        "a celestial compass showing the way to wonders",
        "a dragon and phoenix in harmonious dance",
        "a mystical spiderweb spun with moonlight",
        "a raging storm with lightning bolts and rain",
        "a luminous crescent moon with sparkling stars",
        "a blazing phoenix with resplendent plumage",
        "an intricate clockwork design with moving parts",
        "a celestial map depicting the cosmos",
        "a mythical kraken emerging from the depths",
        "an enchanted forest with whimsical enchantments",
        "a radiant sun with beams of warm light",
        "a swirling galaxy with distant constellations",
        "an angelic figure surrounded by heavenly light",
        "a winding labyrinth with mythical creatures",
        "a shimmering waterfall cascading into wonder",
        "a peacock with eyes that seem to gaze",
        "a celestial compass leading to untold realms",
        "a dragon and phoenix embracing in unity",
        "an intricate spiderweb with dewdrops glistening",
        "a tempestuous storm with turbulent winds",
        "a luminous crescent moon with ethereal glow",
        "a blazing phoenix in a triumphant stance",
        "an ornate clockwork heart at the core",
        "a celestial map charting the stars",
        "a mythical griffin soaring through the skies",
        "an enchanted forest with hidden enchantments",
        "a radiant sun with rays of divine light",
        "a swirling galaxy with celestial wonders",
        "an angelic figure with divine grace",
        "a mysterious labyrinth with secrets within",
        "a shimmering waterfall in a sacred glade",
        "a peacock displaying vibrant and intricate feathers",
        "a celestial compass guiding through the cosmos",
        "a dragon and phoenix united in harmony",
        "an intricate spiderweb spun with moonlit threads",
        "a thunderstorm with lightning bolts and thunderclaps",
        "a crescent moon with stars scattered across the night sky",
        "a blazing phoenix in a triumphant pose of rebirth",
        "an ornate clockwork mechanism adorned with gears",
        "a celestial map depicting the constellations and galaxies",
        "a mythical sea dragon rising majestically from the sea",
        "an enchanted forest with a myriad of magical beings",
        "a radiant sun with rays illuminating the world",
        "a swirling galaxy with stars and cosmic phenomena",
        "an angelic figure with outstretched arms and celestial glow",
        "a mysterious labyrinth with ever-changing paths",
        "a shimmering waterfall in a serene and mystical realm",
        "a peacock with its plumage unfolding in mesmerizing patterns",
        "a celestial compass guiding through time and space",
        "a dragon and phoenix intertwined in a dance of eternity",
        "an intricate spiderweb woven with dreams and destinies",
        "a thunderstorm with powerful bolts of lightning",
        "a crescent moon surrounded by an array of celestial wonders",
        "a blazing phoenix rising with vibrant flames of rebirth",
        "an ornate clockwork heart with gears turning in unison",
        "a celestial map revealing the mysteries of the universe",
        "a mythical winged lion standing guard with regal majesty",
        "an enchanted forest with enchanting whispers in the breeze",
        "a radiant sun with rays reaching out to touch the horizon",
        "a swirling galaxy with constellations forming tales of old",
        "an angelic figure emanating celestial light and benevolence",
        "a maze-like labyrinth with secrets hidden at every turn",
        "a shimmering waterfall cascading into a hidden oasis",
        "a peacock displaying its magnificent feathers in splendor",
        "a celestial compass leading to unexplored realms of wonder",
        "a dragon and phoenix intertwined, representing harmony",
        "an intricate spiderweb spun with the magic of the night",
        "a thunderstorm with electrifying bolts and rumbling thunder",
        "a crescent moon surrounded by twinkling stars and galaxies",
        "a blazing phoenix in a triumphant display of resurrection",
        "an ornate clockwork mechanism with intricate precision",
        "a celestial map unveiling the mysteries of the cosmos",
        "a mythical dragon coiled around the chest, guarding its treasure",
        "an enchanted forest with ancient trees whispering forgotten knowledge",
        "a radiant sun with rays stretching across the vast expanse of the sky",
        "a swirling galaxy with celestial bodies forming intricate patterns",
        "an angelic figure with luminous wings and an aura of divine grace",
        "a complex labyrinth with a labyrinthine pattern, revealing its secrets",
        "a shimmering waterfall flowing from a hidden source of eternal magic",
        "a peacock with iridescent feathers, displaying a mesmerizing spectacle",
        "a celestial compass that guides travelers across the vast cosmic seas",
        "a dragon and phoenix in an eternal dance, embodying the balance of nature",
        "an intricate spiderweb adorned with dewdrops, sparkling like precious gems",
        "a thunderstorm with dramatic lightning strikes and rumbling thunderclaps",
        "a crescent moon surrounded by a galaxy of stars, shining with celestial light",
        "a blazing phoenix rising from the ashes, symbolizing resilience and renewal",
        "an ornate clockwork heart with gears interlocking, representing unity and love",
        "a celestial map mapping the constellations, guiding explorers to new horizons",
        "a mythical griffin, a majestic creature with the body of a lion and the wings of an eagle",
        "an enchanted forest filled with magical beings, ancient trees, and ethereal glimmers",
        "a radiant sun with rays extending outward, illuminating the world with its warmth",
        "a swirling galaxy with stars forming patterns that tell stories of distant worlds",
        "an angelic figure with outstretched arms, offering protection and divine guidance",
        "a mysterious labyrinth with intricate paths, concealing treasures and riddles",
        "a shimmering waterfall cascading into a pool of mystical waters, brimming with magic",
        "a peacock with its resplendent tail fanned out, displaying a mesmerizing array of colors",
        "a celestial compass, an otherworldly tool guiding seekers through celestial mysteries",
        "a dragon and phoenix in harmonious dance, representing the balance of opposing forces",
        "an intricate spiderweb spun with moonlit threads, capturing dreams and moonbeams",
        "a thunderstorm with electrifying lightning and booming thunder, a display of nature's power",
        "a crescent moon surrounded by stars and galaxies, a window to the mysteries of the cosmos",
        "a blazing phoenix soaring with fiery plumage, a symbol of resurrection and transformation",
        "an ornate clockwork mechanism with gears and cogs, a testament to ingenuity and craftsmanship",
        "a celestial map, a guide to the heavens, uncovering the secrets of distant constellations",
        "a mythical sea dragon, a majestic creature of the deep, guarding the treasures within",
        "an enchanted forest with mystical creatures, where ancient magic thrives in every whisper",
        "a radiant sun with beams of light spreading across the world, illuminating all in its path",
        "a swirling galaxy with cosmic wonders, a glimpse into the vastness of the universe",
        "an angelic figure with radiant wings, emanating divine light and celestial harmony",
        "a complex labyrinth with intricate passages, a challenge to those seeking its center",
        "a shimmering waterfall cascading into a hidden grotto, a sanctuary of ethereal beauty",
        "a peacock with its tail feathers unfurled, displaying an array of brilliant hues",
        "a celestial compass guiding travelers through the celestial realms and beyond",
        "a dragon and phoenix entwined, embodying the harmony of opposing forces",
        "an intricate spiderweb adorned with dewdrops, a masterpiece of delicate artistry",
        "a thunderstorm with dramatic lightning strikes and rumbling thunder, nature's power unleashed",
        "a crescent moon surrounded by stars and galaxies, a celestial embrace of the night sky",
        "a blazing phoenix rising from the flames, a symbol of renewal and eternal life",
        "an ornate clockwork heart, a marvel of precision engineering and boundless love",
        "a celestial map, a chart of the cosmic wonders, guiding explorers to unknown territories",
        "a mythical griffin in flight, a creature of majestic strength and divine wisdom",
        "an enchanted forest with ethereal whispers and secrets hidden beneath the ancient trees",
        "a radiant sun with rays extending, bringing warmth and light to the world",
        "a swirling galaxy with stars forming constellations that tell mythical tales",
        "an angelic figure with outstretched arms and a gentle presence of divine protection",
        "a mysterious labyrinth with enigmatic paths leading to hidden treasures",
        "a shimmering waterfall flowing from an otherworldly source of mystical energy",
        "a peacock with its plumage displaying an opulent and mesmerizing spectacle",
        "a celestial compass guiding the way through the vastness of the cosmic expanse",
        "a dragon and phoenix in harmonious dance, symbolizing the unity of opposites",
        "an intricate spiderweb woven with silken threads, capturing the magic of the night",
        "a thunderstorm with electrifying lightning and rumbling thunder, a display of natural power",
        "a crescent moon surrounded by stars and constellations, a glimpse into the celestial realm",
        "a blazing phoenix rising from the flames, a symbol of transformation and rebirth"
    
    ]

    let trap = [
        "poison darts to shoot", 
        "arrows to shoot", 
        "a small explosive", 
        "an alarm", 
        "a pit to open", 
        "a boulder", 
        "a heavy blade to swing", 
        "a spear to stab", 
        "water filling the room", 
        "sand filling the room", 
        "poison gas to start spilling in", 
        "a random spell effect",  
        "a collapsing ceiling of spikes",
        "a concealed trapdoor leading to a pit of hungry beasts",
        "a hidden compartment releasing venomous snakes",
        "a magical glyph that triggers a chain reaction of elemental explosions",
        "a pressure plate activating a deadly swinging blade mechanism",
        "an illusionary treasure chest concealing an actual trap",
        "a powerful gust of wind blowing harmful projectiles in all directions",
        "a hidden mechanism triggering a swarm of enchanted arrows",
        "an acid spray that dissolves anything inside the chest",
        "a cursed gemstone that releases a malevolent spirit upon touch",
        "a magical portal transporting anyone who opens the chest to a dangerous location",
        "a freezing spell turning the chest and its surroundings into solid ice",
        "a time-delayed trap that activates when the chest is taken far from its original location",
        "an electrified metal lining inside the chest, delivering a shocking surprise",
        "a teleportation enchantment, transporting the opener to a perilous dimension",
        "a mesmerizing illusion making the chest seem empty while the trap is triggered",
        "a hidden compartment filling with quicksand, pulling intruders down",
        "a cascade of fiery meteors summoned upon opening the chest",
        "a darkness spell enveloping the room, rendering the intruders blind",
        "a spell that causes the chest to grow impossibly heavy and immovable",
        "an enchanted mirror reflecting harmful beams of energy back at the opener",
        "a series of elemental symbols that, when touched in the wrong sequence, unleash chaos",
        "a magical storm of lightning and thunder bolts striking the chest",
        "a cursed curse scroll that brings a curse upon anyone who tries to take the treasure",
        "a chilling frost trap that freezes the opener in place",
        "a swarm of animated objects, defending the treasure with relentless fervor",
        "an illusionary treasure, luring intruders into a trapped decoy",
        "a powerful magnet drawing all metallic objects towards the chest",
        "a magical aura that causes weapons to become uncontrollable and dangerous",
        "a swarm of enchanted insects released upon opening the chest",
        "a spectral guardian appearing to protect the treasure",
        "a curse of endless hunger, causing the opener to crave the treasure forever",
        "a trap of shifting gravity, making movement around the chest nearly impossible",
        "a deadly mist filling the room upon opening the chest",
        "a cursed coin that brings misfortune to anyone who takes it",
        "a spell that triggers uncontrollable laughter in anyone who touches the chest",
        "a temporal loop trap, causing the chest to endlessly reset after being opened",
        "an illusory treasure chest that disappears upon touch, leaving intruders empty-handed",
        "a magical silence field, rendering anyone inside the room mute and unable to call for help",
        "a trap that summons an elemental guardian to protect the treasure",
        "a magical mirror that reflects harmful spells back at the caster",
        "a trap that causes the chest to meld with the opener's hand, preventing them from letting go",
        "an enchantment that conjures a phantom treasure chest, diverting attention from the real one",
        "a spell of vertigo, causing the room to spin and disorient intruders",
        "a trap that floods the room with mesmerizing illusions, causing confusion and disarray",
        "a cursed key that binds the opener's fate to the treasure",
        "a trap that activates a series of deadly illusions, testing the intruder's resolve",
        "an arcane lock that seals the chest and prevents anyone from opening it",
        "a trap that causes the chest to levitate, out of reach of intruders",
        "a swarm of enchanted vines, ensnaring anyone who comes near the chest",
        "a spell that causes the floor to crumble away, revealing a treacherous chasm",
        "a trap of mirrors reflecting deadly beams of light in all directions",
        "a magical pressure plate that triggers a collapsing ceiling",
        "an illusionary trap of shifting walls, creating a labyrinth that leads nowhere",
        "a spell that grants the chest sentience, allowing it to defend itself",
        "a trap that polymorphs the opener into a harmless creature",
        "an enchantment that causes the chest to emit a powerful sonic blast",
        "a trap that turns the floor into a slippery surface, making movement hazardous",
        "a cursed treasure that brings bad luck and misfortune to its owner",
        "a trap that summons spectral phantoms to haunt and deter intruders",
        "a magical firewall that engulfs the chest in flames upon opening",
        "a spell that binds the opener's hands together, preventing them from reaching for weapons",
        "a trap of mesmerizing lights, luring intruders into a state of trance",
        "an enchanted trap that teleports intruders to a different part of the dungeon",
        "a cursed scroll of endless darkness, creating an inescapable void around the chest",
        "a magical force field that repels anyone attempting to get near the chest",
        "a trap that projects illusionary threats, causing intruders to flee in fear",
        "an arcane curse that leaves the opener unable to let go of the chest's lid",
        "a trap that causes the walls to close in, squeezing anyone inside the room",
        "a spell of illusion, making the chest seem much larger than it actually is",
        "a trap of cursed vines that drain the life force of those who touch them",
        "a magical mirror trap that reflects harmful spells back at their casters",
        "an enchantment that causes the ceiling to lower slowly, threatening to crush intruders",
        "a trap that conjures spectral hands to grab and restrain intruders",
        "a spell of darkness that plunges the room into pitch-black darkness",
        "an arcane glyph that triggers a cascade of powerful elemental forces",
        "a trap that summons a guardian construct to protect the treasure",
        "a spell that causes the chest to become intangible and pass through the opener's hand",
        "a curse of eternal slumber, causing the opener to fall into a deep sleep",
        "a trap of shifting walls, constantly rearranging the room's layout",
        "an enchantment that induces a state of uncontrollable laughter in anyone who approaches the chest",
        "a trap that releases a swarm of spectral moths, devouring all light",
        "a magical freeze trap, encasing intruders in solid ice",
        "a cursed treasure that drains the life force of anyone who touches it",
        "a trap of illusory stairs, leading intruders in circles around the room",
        "a spell that summons a fog of choking darkness, impairing vision and breathing",
        "an arcane trap that causes the room to shrink, compressing intruders",
        "a trap that triggers an illusion of immense treasure, enticing intruders to waste time searching",
        "a magical ward that causes the floor to collapse if anyone attempts to step on it",
        "a cursed mirror trap that reflects a distorted and horrifying image of the opener",
        "a trap that summons ethereal chains to bind and immobilize intruders",
        "a spell of confusion, causing intruders to forget their purpose and intentions",
        "an arcane lock that triggers a torrent of water to flood the room",
        "a trap that activates a whirlwind, tossing intruders about the room",
        "a spell that causes the walls to move and shift, reconfiguring the room's layout",
        "a trap that creates illusory duplicates of the treasure chest, confusing intruders",
        "a magical gravity well that pulls intruders towards the center of the room",
        "a curse of relentless shadows, causing darkness to cling to intruders",
        "a trap that causes the chest to become invisible, hiding its true location",
        "an enchantment that bestows the chest with a sentient voice, issuing ominous warnings",
        "a trap of shifting illusions, making intruders lose their sense of direction",
        "a spell that summons spectral hands to snatch away weapons and items",
        "an arcane ward that causes intruders to forget their purpose and lose their way",
        "a trap that summons a blinding flash of light upon opening the chest",
        "a curse of eternal silence, preventing the opener from making any sound",
        "a trap of enigmatic symbols, creating a riddle that must be solved to proceed",
        "a magical enchantment that causes the floor to become slippery as ice",
        "a spell that fills the room with swirling winds, creating a dangerous vortex",
        "an arcane trap that transforms intruders into harmless creatures",
        "a trap that releases a swarm of spectral butterflies, causing confusion and distraction",
        "a spell of illusion, making the chest seem heavier than it actually is",
        "a curse of eternal darkness, creating an inescapable shroud of shadows",
        "a trap of spectral chains, binding intruders and preventing escape",
        "a magical storm of hail and ice, pelting anyone inside the room",
        "a spell that summons a swarm of ethereal bats, creating chaos and disarray",
        "an enchantment that causes the chest to emit a deafening noise upon touch",
        "a trap that teleports the chest to a different location, evading intruders",
        "a cursed scroll of maddening whispers, causing hallucinations and paranoia",
        "a magical force field that repels all attempts to touch or open the chest",
        "a trap of shifting shadows, concealing hidden dangers",
        "an arcane glyph that triggers a storm of fiery meteors",
        "a trap that summons a guardian construct to attack intruders",
        "a spell that causes the chest to shrink and become impossibly small",
        "a curse of uncontrollable dancing, making the opener dance uncontrollably",
        "a trap of shifting mirrors, creating a maze of reflections and confusion",
        "an enchantment that causes the room to fill with dense fog",
        "a trap that releases a swarm of ghostly apparitions, terrifying intruders",
        "a spell of illusion, making the chest seem to float in mid-air",
        "a magical barrier that renders the chest and its contents intangible",
        "a trap that summons spectral hands to snatch away valuable items",
        "an arcane ward that causes intruders to forget their past and identities",
        "a trap that activates a torrent of molten lava to flow into the room",
        "a spell that summons a blinding flash of light, temporarily blinding intruders",
        "a curse of cursed treasure, plaguing the opener with misfortune and bad luck",
        "a trap of illusory mirrors, reflecting and distorting reality",
        "a magical enchantment that causes the floor to become sticky and difficult to move on",
        "a spell that fills the room with suffocating darkness, sapping intruders' strength",
        "an arcane trap that transforms intruders into harmless animals",
        "a trap that releases a swarm of spectral butterflies, causing confusion and distraction",
        "a spell of illusion, making the chest seem heavier than it actually is",
        "a curse of eternal darkness, creating an inescapable shroud of shadows",
        "a trap of spectral chains, binding intruders and preventing escape",
        "a magical storm of hail and ice, pelting anyone inside the room",
        "a spell that summons a swarm of ethereal bats, creating chaos and disarray",
        "an enchantment that causes the chest to emit a deafening noise upon touch",
        "a trap that teleports the chest to a different location, evading intruders",
        "a cursed scroll of maddening whispers, causing hallucinations and paranoia",
        "a magical force field that repels all attempts to touch or open the chest",
        "a trap of shifting shadows, concealing hidden dangers",
        "an arcane glyph that triggers a storm of fiery meteors",
        "a trap that summons a guardian construct to attack intruders",
        "a spell that causes the chest to shrink and become impossibly small",
        "a curse of uncontrollable dancing, making the opener dance uncontrollably",
        "a trap of shifting mirrors, creating a maze of reflections and confusion",
        "an enchantment that causes the room to fill with dense fog",
        "a trap that releases a swarm of ghostly apparitions, terrifying intruders",
        "a spell of illusion, making the chest seem to float in mid-air",
        "a magical barrier that renders the chest and its contents intangible",
        "a trap that summons spectral hands to snatch away valuable items",
        "an arcane ward that causes intruders to forget their past and identities",
        "a trap that activates a torrent of molten lava to flow into the room",
        "a spell that summons a blinding flash of light, temporarily blinding intruders",
        "a curse of cursed treasure, plaguing the opener with misfortune and bad luck",
        "a trap of illusory mirrors, reflecting and distorting reality",
        "a magical enchantment that causes the floor to become sticky and difficult to move on",
        "a spell that fills the room with suffocating darkness, sapping intruders' strength",
        "an arcane trap that transforms intruders into harmless animals",
        "a trap that releases a swarm of venomous snakes, striking at intruders",
        "a curse of eternal echoes, causing all sounds to repeat endlessly",
        "a trap of shifting illusions, making the chest seem to disappear and reappear",
        "an enchantment that causes the room to become engulfed in flames",
        "a spell that summons spectral hands to snatch away intruders' weapons",
        "a trap of mind-bending illusions, distorting perception and reality",
        "a magical ward that seals the chest and prevents any attempts to open it",
        "a trap that triggers an avalanche of rocks and debris",
        "a curse of eternal blindness, rendering the opener unable to see",
        "a trap of illusory walls, creating a labyrinth that leads nowhere",
        "a magical enchantment that causes the room to fill with dense mist",
        "a spell that summons a swarm of ghostly crows, pecking at intruders",
        "an arcane trap that turns intruders into harmless creatures",
        "a trap that summons a powerful gust of wind, blowing intruders away",
        "a curse of uncontrollable sneezing, making the opener unable to stop sneezing",
        "a trap of shifting illusions, causing intruders to lose their sense of balance",
        "an enchantment that causes the ceiling to lower slowly, threatening to crush intruders",
        "a trap that conjures a phantom treasure chest, luring intruders away from the real one",
        "a spell that creates illusory threats, causing intruders to panic and flee",
        "an arcane glyph that triggers a swarm of deadly insects",
        "a trap that summons a guardian serpent to defend the treasure",
        "a magical barrier that repels anyone attempting to approach the chest",
        "a trap that activates a torrent of freezing water to flood the room",
        "a spell that creates a powerful whirlpool, pulling intruders towards the center",
        "a curse of uncontrollable levitation, causing the opener to float in mid-air",
        "a trap of illusory mirrors, creating a hall of reflections that leads astray",
        "a magical enchantment that causes the floor to become slippery with ice",
        "a spell that fills the room with blinding light, temporarily dazzling intruders",
        "an arcane trap that transforms intruders into harmless insects",
        "a trap that releases a swarm of spectral bats, causing disorientation and fear",
        "a curse of eternal laughter, making the opener unable to stop laughing",
        "a trap of shifting shadows, concealing deadly hazards",
        "an enchantment that causes the chest to emit a deafening noise, disorienting intruders",
        "a trap that teleports the opener to a different part of the dungeon",
        "a cursed scroll of night terrors, causing horrifying nightmares",
        "a magical force field that repels anyone attempting to touch the chest",
        "a trap of twisting illusions, making intruders lose their sense of direction",
        "an arcane glyph that triggers a swarm of fiery insects",
        "a trap that summons a guardian elemental to protect the treasure",
        "a spell that causes the chest to grow larger and heavier upon touch",
        "a curse of uncontrollable shrinking, making the opener gradually diminish in size",
        "a trap of shifting mirrors, creating a maze of reflections and confusion",
        "a magical ward that causes the room to fill with a suffocating mist",
        "a trap that releases a swarm of ghostly butterflies, causing distraction and confusion",
        "a spell of illusion, making the chest seem to multiply into numerous replicas",
        "a trap that conjures spectral hands to grab and restrain intruders",
        "an arcane ward that causes intruders to lose their memories and identities",
        "a trap that activates a torrent of molten lava to flow into the room",
        "a spell that summons a blinding flash of light, temporarily blinding intruders",
        "a curse of cursed treasure, bringing misfortune and ill luck to the opener",
        "a trap of illusory mirrors, reflecting and distorting reality",
        "a magical enchantment that causes the floor to become sticky and difficult to move on",
        "a spell that fills the room with suffocating darkness, sapping intruders' strength",
        "an arcane trap that transforms intruders into harmless animals",
        "a trap that releases a swarm of venomous snakes, striking at intruders",
        "a curse of eternal echoes, causing all sounds to repeat endlessly",
        "a trap of shifting illusions, making the chest seem to disappear and reappear",
        "an enchantment that causes the room to become engulfed in flames",
        "a spell that summons spectral hands to snatch away intruders' weapons",
        "a trap of mind-bending illusions, distorting perception and reality",
        "a magical ward that seals the chest and prevents any attempts to open it",
        "a trap that triggers an avalanche of rocks and debris",
        "a curse of eternal blindness, rendering the opener unable to see",
        "a trap of illusory walls, creating a labyrinth that leads nowhere",
        "a magical enchantment that causes the room to fill with dense mist",
        "a spell that summons a swarm of ghostly crows, pecking at intruders",
        "an arcane trap that turns intruders into harmless creatures",
        "a trap that summons a powerful gust of wind, blowing intruders away",
        "a curse of uncontrollable sneezing, making the opener unable to stop sneezing",
        "a trap of shifting illusions, causing intruders to lose their sense of balance",
        "an enchantment that causes the ceiling to lower slowly, threatening to crush intruders",
        "a trap that conjures a phantom treasure chest, luring intruders away from the real one",
    ]

    let lock = [
        "padlock", 
        "internal mechanism lock", 
        "combination lock", 
        "puzzle lock", 
        "password lock", 
        "hidden lock mechanism",
        "biometric lock with fingerprint recognition",
        "voice-activated lock with a secret passphrase",
        "retinal scanner that requires specific eye identification",
        "magical sigil lock, requiring the correct sequence of runes to be traced",
        "time-based lock that opens only at a specific astrological alignment",
        "musical lock, requiring a particular melody to be played on a set of keys",
        "ancient mechanical lock with intricate gears and moving parts",
        "enchanted riddle lock, requiring the solution to a cryptic puzzle",
        "magnetic lock, requiring a specific magnetic key to activate",
        "heat-sensitive lock, requiring the chest to be warmed to a certain temperature",
        "cold-sensitive lock, requiring the chest to be chilled to a certain degree",
        "light-based lock, needing a specific pattern of light to be projected onto it",
        "shadow puzzle lock, requiring the correct arrangement of objects to cast specific shadows",
        "clockwork lock, needing the hands of a clock to be set at a precise time",
        "celestial lock, aligning with the positions of celestial bodies in the sky",
        "water-based lock, reacting to the flow of water or the level of liquid",
        "fire puzzle lock, requiring specific torches to be lit in the correct sequence",
        "wind-powered lock, needing a continuous flow of air to activate",
        "gemstone combination lock, requiring certain precious gems to be inserted in order",
        "steampunk-style lock, combining mechanical gears with retro-futuristic elements",
        "mechanical keypad lock, needing the correct sequence of buttons to be pressed",
        "engraved lock, requiring a particular pattern or design to be traced",
        "enchanted lock that can only be opened by moonlight or sunlight",
        "mirror-based lock, needing light to be reflected in a specific manner",
        "invisible lock, where the mechanism is hidden and must be sensed through touch",
        "crystal lock, requiring a certain crystal to be inserted to unlock the chest",
        "gravity-based lock, responding to the positioning of the chest in space",
        "emblem lock, requiring the placement of specific symbols in the correct positions",
        "animal-shaped lock, where different animal figurines must be turned to open",
        "magical lock with shifting symbols, requiring the right sequence to be selected",
        "wooden combination lock, with notches and grooves aligning in a particular way",
        "astronomical lock, aligning with astronomical events or constellations",
        "morse code lock, needing a sequence of taps or sounds to be transmitted",
        "invisible ink lock, requiring the application of a specific substance to reveal the code",
        "astral projection lock, where the opener must enter a spiritual realm to unlock",
        "liquid metal lock, with the mechanism formed from a shape-shifting metal",
        "moon phase lock, aligning with the current phase of the moon",
        "dial lock with movable rings, requiring specific symbols to align",
        "alphabet lock, requiring certain letters to be pressed in order",
        "time-based combination lock, requiring specific actions to be performed at precise intervals",
        "wind chime lock, requiring the right chimes to be triggered in harmony",
        "holographic lock, requiring the projection of specific holographic images",
        "gemstone puzzle lock, needing specific gems to be inserted in a specific order",
        "levitation lock, requiring the chest to be lifted using levitation magic",
        "magnetic puzzle lock, where pieces must be aligned using magnetic forces",
        "color-based lock, requiring certain colors to be displayed in a particular pattern",
        "night sky lock, aligning with the position of stars and planets in the night sky",
        "chessboard lock, requiring specific chess pieces to be moved in a certain sequence",
        "crystal pendulum lock, with the pendulum swinging in a specific pattern to unlock",
        "zodiac lock, aligning with the current position of the zodiac signs",
        "fire and ice lock, needing specific flames and ice sources to activate",
        "shape-shifting lock, with the mechanism changing form upon touch",
        "clockwork puzzle lock, with gears that must be rotated to fit in the right positions",
        "elemental lock, requiring the use of elemental powers to unlock",
        "music box lock, where a particular tune must be played on a music box to unlock",
        "night and day lock, with two different mechanisms activated at different times",
        "mirror maze lock, needing the opener to navigate through a maze of mirrors",
        "constellation lock, aligning with the current arrangement of constellations",
        "glyphic lock, requiring specific glyphs to be pressed in the correct sequence",
        "waterwheel lock, requiring the chest to be turned like a waterwheel to unlock",
        "planetary lock, aligning with the current positions of the planets",
        "firefly lock, requiring the correct fireflies to be captured and placed in a container",
        "morphing lock, with the mechanism changing shape and configuration randomly",
        "wind puzzle lock, requiring the correct gusts of wind to be generated",
        "ancient language lock, needing the correct phrases or words to be spoken or written",
        "holographic keypad lock, with a holographic display showing changing patterns",
        "star map lock, aligning with the current arrangement of stars",
        "frozen lock, requiring the chest to be frozen in ice to activate",
        "gemstone constellation lock, needing specific gems to be arranged like constellations",
        "alchemy lock, requiring the correct alchemical reagents to be mixed together",
        "mathematical puzzle lock, requiring specific equations or formulas to be solved",
        "time sandglass lock, needing sand to be poured in a specific time frame",
        "phoenix lock, requiring the chest to be exposed to fire before unlocking",
        "bio-organic lock, responding to the touch of a living organism",
        "clock tower lock, requiring the chest to be placed in a specific clock tower",
        "ancient tablet lock, needing the correct sequence of tablet rotations",
        "ethereal lock, requiring the opener to shift into an ethereal form to unlock",
        "memory lock, with the mechanism activated by specific memories or experiences",
        "gear puzzle lock, with interlocking gears that must be set in the right positions",
        "crystal prism lock, requiring light to be refracted in a specific manner",
        "sundial lock, aligning with the current position of the sun's shadow",
        "water puzzle lock, requiring the flow of water to activate certain mechanisms",
        "magnetic pendulum lock, with the pendulum influencing the magnetic mechanism",
        "ancient hieroglyph lock, needing specific hieroglyphs to be pressed in order",
        "sound-based lock, requiring specific musical notes to be played or sung",
        "living vine lock, with vines that must be guided and woven to unlock",
        "alchemy circle lock, requiring the correct arrangement of alchemical symbols",
        "time warp lock, with the mechanism activating during specific temporal distortions",
        "fire maze lock, needing the opener to navigate through a maze of fire barriers",
        "wind compass lock, aligning with the direction of the wind",
        "tide-based lock, aligning with the current tidal patterns",
        "runic lock, needing the correct runic sequence to be traced",
        "shadow clock lock, with the shadow of an object indicating the correct time to unlock",
        "solar beam lock, requiring mirrors to align and reflect sunlight onto the mechanism",
        "living statue lock, with statues that must be moved into specific positions",
        "alchemy cauldron lock, requiring the correct ingredients to be mixed in a cauldron",
        "heartbeat lock, with the mechanism activated by the touch of a living being's heartbeat",
        "gong lock, requiring specific gongs to be struck in the right order",
        "crystal prism lock, requiring light to be refracted in a specific manner",
        "sundial lock, aligning with the current position of the sun's shadow",
        "water puzzle lock, requiring the flow of water to activate certain mechanisms",
        "magnetic pendulum lock, with the pendulum influencing the magnetic mechanism",
        "ancient hieroglyph lock, needing specific hieroglyphs to be pressed in order",
        "sound-based lock, requiring specific musical notes to be played or sung",
        "living vine lock, with vines that must be guided and woven to unlock",
        "alchemy circle lock, requiring the correct arrangement of alchemical symbols",
        "time warp lock, with the mechanism activating during specific temporal distortions",
        "fire maze lock, needing the opener to navigate through a maze of fire barriers",
        "wind compass lock, aligning with the direction of the wind",
        "tide-based lock, aligning with the current tidal patterns",
        "runic lock, needing the correct runic sequence to be traced",
        "shadow clock lock, with the shadow of an object indicating the correct time to unlock",
        "solar beam lock, requiring mirrors to align and reflect sunlight onto the mechanism",
        "living statue lock, with statues that must be moved into specific positions",
        "alchemy cauldron lock, requiring the correct ingredients to be mixed in a cauldron",
        "heartbeat lock, with the mechanism activated by the touch of a living being's heartbeat",
        "gong lock, requiring specific gongs to be struck in the right order",
        "spiritual resonance lock, needing a specific frequency of spiritual energy to activate",
        "time crystal lock, requiring a crystal that is attuned to a specific point in time",
        "phase-shift lock, responding to the correct phase shift of an energy source",
        "levitating key lock, where a levitating key must be manipulated to unlock",
        "ancient artifact lock, requiring the use of a specific ancient artifact to activate",
        "geomagnetic lock, aligning with the Earth's magnetic field",
        "mystical hourglass lock, requiring sand to flow through an hourglass to unlock",
        "quantum lock, with the mechanism activated by the quantum state of particles",
        "holographic puzzle lock, requiring the manipulation of holographic projections",
        "time dilation lock, with the mechanism activated during time dilation events",
        "moonlit lake lock, with the chest needing to be submerged in moonlit water",
        "dimensional key lock, where the key must be inserted from a different dimension",
        "moon and star alignment lock, requiring the alignment of celestial bodies",
        "time-traveling lock, needing the chest to be taken back in time to unlock",
        "sound wave lock, with sound waves generating specific resonances to unlock",
        "crystalline chamber lock, requiring crystals to be placed in specific chambers",
        "lunar clock lock, aligning with the phases of the moon",
        "quantum entanglement lock, requiring entangled particles to unlock",
        "energy prism lock, needing beams of energy to pass through a prism to unlock",
        "dream realm lock, requiring the chest to be accessed in the realm of dreams",
        "synchronized clockwork lock, with gears needing to move in precise synchronization",
        "starlight constellation lock, requiring stars to align in specific constellations",
        "time crystal chamber lock, with crystals needing to be inserted in a chamber",
        "celestial alignment lock, requiring the alignment of planets and stars",
    ]

    let keyLoc = [
        "hidden in the same room", 
        "hidden in plain sight", 
        "protected by a guardian", 
        "in another room", 
        "held by the owner", 
        "lost",
        "submerged in a hidden underwater cave",
        "concealed within a hollowed-out book on a bookshelf",
        "buried in a secret compartment beneath the floorboards",
        "guarded by a riddle that reveals its location",
        "entrusted to a loyal companion or ally",
        "locked in a secured safe or vault",
        "sealed within a glass case protected by traps",
        "suspended from the ceiling by an intricate pulley system",
        "hidden within a painting or artwork on the wall",
        "enchanted to be invisible, requiring magic to reveal its presence",
        "frozen inside a block of ice in a magical freezer",
        "hidden behind a moveable brick or stone in a wall",
        "transformed into a small creature that must be caught or charmed",
        "concealed in a secret compartment within a piece of furniture",
        "protected by a magical force field that requires a specific activation",
        "entwined within the roots of an ancient tree deep in the forest",
        "enchanted to be shrunken and hidden within a small trinket or ornament",
        "concealed within the belly of a carved stone statue",
        "camouflaged as part of an intricate mechanical device or automaton",
        "kept within a nest high up on a cliff, guarded by territorial creatures",
        "hidden within the intricate workings of a grandfather clock",
        "concealed beneath the feathers of a rare and elusive bird",
        "locked within a puzzle box that requires careful manipulation to open",
        "kept in the possession of a mischievous and elusive spirit",
        "hidden within a collection of identical keys, requiring trial and error",
        "placed within a labyrinth of mirrors, making it difficult to find the real key",
        "locked away in a treasure chest of another similar-looking room",
        "concealed within the petals of an enchanted flower",
        "hidden in a constellation of stars in the night sky",
        "concealed within the gears of a massive clockwork mechanism",
        "kept within a nest of venomous serpents in a dangerous location",
        "enchanted to change locations at random intervals",
        "hidden in the lair of a powerful and territorial beast",
        "sealed inside a series of nested boxes, each requiring a key",
        "locked away in a vault at the heart of a bustling city",
        "concealed within the flowing robes of a mysterious wanderer",
        "hidden beneath a layer of molten lava in a volcanic cavern",
        "kept within a secure chamber guarded by loyal followers",
        "concealed inside an ancient artifact or relic",
        "locked within a chest that can only be opened by an ancient ritual",
        "hidden within a massive library, among countless other books",
        "enchanted to float and move, making it elusive to catch",
        "protected by a powerful illusion that disguises its true location",
        "sealed within a bottle floating in the middle of a vast ocean",
        "hidden inside a musical instrument, producing specific notes to reveal it",
        "kept within a massive hoard of coins and valuables",
        "concealed within a swirling vortex of wind in the skies",
        "locked within a cage guarded by ferocious creatures",
        "hidden in a realm accessible only through magical portals",
        "enchanted to blend into its surroundings, matching the environment",
        "protected by a complex maze of shifting tunnels and passageways",
        "kept within the nest of a mythical and majestic creature",
        "concealed within a magical fog that obscures its location",
        "hidden in a realm of dreams, requiring an arduous quest to retrieve it",
        "locked away within the inner chambers of a great palace",
        "concealed within an enchanted puzzle that must be solved",
        "kept within the lair of a reclusive and enigmatic hermit",
        "hidden inside an otherworldly realm accessible through a magical mirror",
        "enchanted to be weightless, requiring keen perception to locate it",
        "protected by the guardian spirits of an ancient forest",
        "concealed within the heart of a living labyrinth",
        "hidden in a realm of eternal twilight, accessible only during specific hours",
        "locked within a magical mechanism that phases in and out of existence",
        "kept within a vault guarded by sentient constructs",
        "concealed within the whispers of the wind, requiring acute listening",
        "hidden at the top of an impossibly tall tower, requiring a daring climb",
        "enchanted to blend into the night sky, making it appear as a star",
        "protected by a powerful curse that obscures its true form",
        "concealed in the form of a rare and valuable gemstone",
        "kept within a cryptic and shifting pocket dimension",
        "hidden within a complex network of underwater caves and tunnels",
        "locked away in a vault located within the heart of a mountain",
        "concealed within the heart of a massive crystal formation",
        "hidden among the treasures of a legendary pirate's trove",
        "enchanted to mimic the appearance of a common household object",
        "protected by a maze of enchanted thorns and brambles",
        "concealed within a floating island, reachable through airships",
        "kept within a secret chamber protected by an ancient order",
        "hidden in the lair of a powerful and ancient dragon",
        "locked away in a massive tree with branches reaching the sky",
        "concealed within a constellation of floating islands in the sky",
        "sealed within an ancient vault guarded by spectral sentinels",
        "hidden beneath the shifting sands of a vast desert",
        "enchanted to be intangible, existing partially in the spirit realm",
        "protected by a tribe of elusive and skilled forest-dwelling nomads",
        "concealed within the dreams of a slumbering deity",
        "kept within a massive ice cavern, requiring warmth to reach it",
        "hidden within the embrace of a colossal statue, deep in a jungle",
        "locked away in the heart of a haunted and abandoned castle",
        "concealed in the ruins of an ancient civilization, deep underground",
        "hidden within a floating crystal fortress in the clouds",
        "enchanted to change its size and appearance, making it hard to identify",
        "protected by a powerful curse that obscures its true form",
        "concealed within the heart of a massive crystal formation",
        "hidden among the treasures of a legendary pirate's trove",
        "enchanted to mimic the appearance of a common household object",
        "kept within a cryptic and shifting pocket dimension",
        "hidden within a complex network of underwater caves and tunnels",
        "locked away in a vault located within the heart of a mountain",
        "concealed within the heart of a floating island, reachable through airships",
        "hidden in the lair of a powerful and ancient dragon",
     ]
    let output = `The treasure is enclosed by a ${searchArray(style)} chest made of ${searchArray(material)}. The trim and hinges are ${searchArray(trim)}. The craftsman left a mark in the form of ${searchArray(mark)}. Carelessness will trigger ${searchArray(trap)}. To get past the ${searchArray(lock)}, one would need the key, which is currently ${searchArray(keyLoc)}.`
    document.getElementById("Chest").innerHTML = output
};
function weapon() {
    function weaponGenerator() {
        function weaponType() {
            let x = rollDice(1000)
            if (x < 4) {
                return "Club"
            } else if (x < 39) {
                return "Dagger"
            } else if (x < 43) {
                return "Greatclub"
            } else if (x < 67) {
                return "Handaxe"
            } else if (x < 75) {
                return "Javelin"
            } else if (x < 79) {
                return "Light Hammer"
            } else if (x < 149) {
                return "Mace"
            } else if (x < 172) {
                return "QuarterStaff"
            } else if (x < 176) {
                return "Sicle"
            } else if (x < 213) {
                return "Spear"
            } else if (x < 230) {
                return `${searchArray(["Tonfa","Tiger Claws","Knuck;e Dusters","Iron Fan","Katar","Emeici","Cestus","Tekko","Maduvu","Pata","Crecent Moon Knives","Knife Wheel"])} (fist weapon)`
            } else if (x < 271) {
                return "Light Crossbow"
            } else if (x < 287) {
                return "Dart"
            } else if (x < 303) {
                return "Shortbow"
            } else if (x < 319) {
                return "Sling"
            } else if (x < 404) {
                return "Battleaxe"
            } else if (x < 413) {
                return "Flail"
            } else if (x < 420) {
                return "Glaive"
            } else if (x < 498) {
                return "Greataxe"
            } else if (x < 576) {
                return "Greatsword"
            } else if (x < 581) {
                return "Halberd"
            } else if (x < 586) {
                return "Lance"
            } else if (x < 773) {
                return "Longsword"
            } else if (x < 774) {
                return "Maul"
            } else if (x < 778) {
                return "Morningstar"
            } else if (x < 779) {
                return "Pike"
            } else if (x < 809) {
                return "Rapier"
            } else if (x < 848) {
                return "Scimitar"
            } else if (x < 887) {
                return "Shortsword"
            } else if (x < 891) {
                return "Trident"
            } else if (x < 893) {
                return "War Pick"
            } else if (x < 903) {
                return "Warhammer"
            } else if (x < 905) {
                return "Whip"
            } else if (x < 907) {
                return "Blowgun"
            } else if (x < 914) {
                return "Hand Crossbow"
            } else if (x < 955) {
                return "Heavy Crossbow"
            } else if (x < 996) {
                return "Longbow"
            } else if (x < 1000) {
                return "Net"
            }
        }
        let damageTypes = [
            "Slashing, or the Weapon’s base damage type (Attack)", "Fire", "Cold", "Lightning", "Poison", "Acid", "Thunder", "Necrotic", "Radiant", "Psychic", "Force",
        ]
        let animalArray = [
            "Frog", "Boar", "Rat", "Elk", "Lizard", "Wolf", "Bat", "Panther", "Ape", "Black Bear", "Constrictor Snake", "Crocodile", "Giant Crab", "Giant Frog", "Giant Goat", "Giant Poisonous Snake", "Giant Sea Horse", "Giant Wasp", "Poisonous Snake", "Reef Shark", "Rhinoceros", "Warhorse", "Axe beak", "Camel", "Draft Horse", "Elk ", "Giant Badger", "Giant Centipede", "Giant Fire Beetle", "Giant Lizard ", "Giant Rat ", "Giant Weasel", "Giant Wolf Spider", "Mastiff", "Mule ", "Pony", "Scorpion", "Spider", "Swarm of Rats",
        ]
        let abilityTypes = [
            "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma",
        ]
        let optionalProps = [
            "Named Weapon – The weapon is uniquely named. It may whisper this name when held, or be engraved with it.", "Fame or Infamy – The weapon is well known for its relationship to a particular historical figure or event.", "Odd Noise – The material of the weapon vibrates faintly to emit a particular hum, drone, buzz or squeal.", "Odd Smell – The material of the weapon emits an odd smell, which can’t be masked. May be pleasant or unpleasant.", "Odd Shape – The weapon is particularly long, stout, broad, slim, or otherwise identifiably unorthodoxly shaped. Were it not magical, it would be impractical to use.", "Odd Colour – The materials of the weapon are uncommon colours, or change colours under certain conditions.", "Faint Aura – The material of the weapon emits a faint, coloured glow. It may leave tracers, flicker, appear as a flame or float upwards.", "Gemstones – The weapon is inset with a particularly large gemstone, or a variety of smaller gemstones.", "Detailing – The weapon is gilded, engraved, sculpted, or otherwise decorated in a fantastic way.", "Aspected – The weapon amplifies a quality of the bearer’s personality, such as bravery, piousness, or jealousy.",
        ]
        let enchantmentArray = [
            
            `+1 ${weaponType()} of Singing - When this weapon is used, a beautiful song can be heard.`, `+1 ${weaponType()} of Beacon - The bearer can use a bonus action and speak a command word to cause this weapon to shed bright light in a 10-foot radius and dim light for an additional 10 feet.`, `+1 Malleable ${weaponType()} - The bearer can alter the apparent color, material, and design of the weapon as a bonus action – this does not affect the weapon’s type, stats or abilities.`, `+1 ${weaponType()} of Guardian - The weapon whispers warnings, giving +2 bonus to initiative.`, `+1 Waterborne ${weaponType()} - This weapon floats on water and other liquids. Its bearer has advantage on Strength (Athletics) checks to swim.	`, `+1 ${weaponType()} of Delving - While underground , the bearer of this item always knows the item’s depth below the surface and the direction to the nearest staircase, ramp, or other path leading upward.`, `+1 Imperious ${weaponType()} - The bearer of this item knows the Thaumaturgy cantrip.`, `+1 Weightless ${weaponType()} - This weapon falls slowly, like a feather. It is treated as having no weight for the purposes of encumbrance.`, `+1 Adhesive ${weaponType()} - The bearer cannot be disarmed of this weapon.`, `+1 Wieldy ${weaponType()} - The bearer may attack as though they are proficient with this weapon, even if they are not.`, `+1 ${weaponType()} of Prying - The bearer has advantage on Strength (Athletics) or Dexterity (Acrobatics) checks to break free of grapples.`, `+1 Fleet ${weaponType()} - The owner’s base speed is increased by 5 ft. (Requires Attunement)`, `+1 ${weaponType()} of Striding - The bearer is unaffected by difficult terrain.`, `+1 ${weaponType()} of Swimming - The bearer gains a swim speed equal to its walking speed.`, `+1 ${weaponType()} of Climbing - The bearer gains a climb speed equal to its walking speed.`, `+1 ${weaponType()} of Safe Landing - The bearer never takes damage from falling, although they fall at normal speed.`, `+1 ${weaponType()} of Jumping - The bearer may cast the spell Jump as a bonus action, targeting themselves, at will.(Requires Attunement)`, 
            `+1 ${weaponType()} of Shackling - A creature dealt a non-lethal blow by this weapon is restrained by ethereal shackles. They may make a DC 25 Strength (Athletics) check every hour to escape, once they regain consciousness. The owner of this weapon may dispel this effect by speaking a command word. (Requires Attunement)`, `+1 ${weaponType()} of Stability - The bearer gains advantage on all saving throws to avoid being knocked prone or moved against their will.`, `+1 Throwing ${weaponType()} - This weapon has the thrown property with a normal range of 20 feet and a long range of 60 feet. If the weapon already has the throwing property, the normal range and long range of the weapon are both doubled.`, `+1 Wakeful ${weaponType()} - The owner requires half the normal amount of sleep or meditation to gain the effects of a long rest, or avoid the effects of exhaustion.(Requires Attunement)`, `+1 Invigorating ${weaponType()} - When a 20 is rolled on an attack roll with this weapon, the bearer gains 3d4 temporary HP.`, `+1 ${weaponType()} of Detection - The bearer may cast the spell Detect Magic as an action at will.(Requires Attunement)`, `+1 ${weaponType()} of Scanning - The bearer may cast the spell Detect Evil and Good as an action at will.(Requires Attunement)`, `+1 ${weaponType()} of Communing - The bearer may cast the spell Animal Friendship, targeting themselves, as an action at will.(Requires Attunement)`, `+1 Quick ${weaponType()} - The bearer may take a Dash action which does not expend their regular action for the turn. This effect has one charge which it regains at dawn.(Requires Attunement)`, 
            `+1 Brave ${weaponType()} - The bearer has advantage on saving throws against Fear.`, `+1 Resolute ${weaponType()} - The bearer has advantage on saving throws against magical Charm effects.`, `+1 Mindful ${weaponType()} - The owner receives a +3 bonus to their Passive Perception and Passive Investigation scores.(Requires Attunement)`, `+1 Embiggened ${weaponType()} - The bearer may cast Enlarge targeting themselves. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+1 ${weaponType()} of Darksight - The bearer has darkvision with a range of 60 ft. If you already have darkvision, the range increases to 120 ft.(Requires Attunement)`, `+1 ${weaponType()} of Shielding - The bearer may cast the spell Shield. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+1 ${searchArray(damageTypes)} Shifted ${weaponType()} - By speaking a command word, the bearer can change the damage type dealt by this weapon to (element type in name) until the end of turn.`, 
            `+1 ${weaponType()} of Admonishment - When you hit with an opportunity attack, weapon deals an additional +1d8 Thunder damage and hurls an insult.`, `+1 ${searchArray(damageTypes)} Tinged ${weaponType()} - This weapon deals an additional +1d4 (element type in name) damage.`, `+1 ${weaponType()} of Water Breathing - The owner can breathe underwater.(Requires Attunement)`, `+1 Shrouded ${weaponType()} - When this weapon is stowed, the owner may speak a command word to make the weapon invisible. A creature attempting to discover the hidden weapon must pass a Intelligence (Investigation) check with a DC 16. (Requires Attunement)`, `+1 ${weaponType()} of Invisibility - The bearer may cast Invisibility targeting themselves, using the weapon as their focus. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+1 Lucky ${weaponType()} - You may reroll a single attack roll with this weapon. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+1 ${weaponType()} of Revealing - The bearer can use a bonus action and speak a command word to cause this weapon to shed bright light in a 20-foot radius and dim light for an additional 20 feet. Invisible creatures are visible as long as they are in the light cast by this weapon.`, `+1 Restorative ${weaponType()} - The bearer may cast Cure Wounds as a first level spell, using Wisdom as their spellcasting ability and the weapon as their focus. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+1 Vital ${weaponType()} - The bearer has advantage on all Constitution saving throws against Poison and Disease.`, `+1 Restless ${weaponType()} - The owner does not need to sleep or meditate during a long rest, and is immune to negative effects, including exhaustion, due to lack of sleep.(Requires Attunement)`, `+1 Shining ${weaponType()} - As a bonus action, the bearer may speak a command word, causing the weapon to erupt in illusory flames that shed bright light in a 40 foot radius and dim light in an additional 40 ft.`, `+1 ${weaponType()} of Bleeding - When a 20 is rolled on an attack roll with this weapon, the critical hit infers a “Bleed” condition, dealing 1d4 damage at the start of the targets next 3 turns.`, `+1 Vicious ${weaponType()} - When a 20 is rolled on an attack roll with this weapon, its critical hit deals an extra 2d6 damage of the weapon’s type.`, 
            `+1 Poisonous ${weaponType()} - You can spend an action to coat the weapon in magical poison. The poison remains for 1 minute or until an attack using this weapon hits a creature. When an attack with this weapon deals damage, the creature must succeed a DC 13 Constitution saving throw or take 2d6 poison damage and be poisoned until the end of their next turn.`, `+1 Eager ${weaponType()} - The owner gains a +5 bonus to initiative.`, `+1 ${weaponType()} of Relentlessness - When the bearer is reduced to 0 hit points but not killed outright, they may drop to 1 hit point instead. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+1 ${weaponType()} of Water Walking - The bearer may stand on and move across any liquid surface as if it were solid ground.`, `+1 ${weaponType()} of Marking - When a creature is struck by this weapon, the next attack made by an ally against it gains Advantage. This effect does not stack.`, `+1 ${weaponType()} of Mind-Shielding - The bearer is immune to magic that allows other creatures to read their thoughts, determine whether they are lying, know their alignment, or know their creature type. Creatures can telepathically communicate with the bearer only if they allow it.(Requires Attunement)`, `+1 Blinking ${weaponType()} - When the bearer is struck by a critical hit, they may choose to use their reaction to cast the Blink spell, targeting themselves. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+1 Chilling ${weaponType()} - This weapon deals an additional +1d4 cold damage. On a hit, the target has all movement speeds reduced by 5 until the end of it’s next turn.`, `+1 ${weaponType()} of  Charged ${searchArray(damageTypes)} - This weapon deals an additional +1d6 damage (of the damage type in name).`, `+1 ${weaponType()} of Resistance - The bearer has resistance to one type of damage. (Requires Attunement)`, `+1 ${weaponType()} of Deflection - The bearer gains +2 bonus to AC against ranged attacks.`, `+1 ${weaponType()} of Floating - The bearer gains a fly speed of 10 ft.(Requires Attunement)`, `+1 ${weaponType()} of Sustenance - The owner does not need to eat or drink.(Requires Attunement)`, `+1 Filtering ${weaponType()} - The bearer can breathe and speak normally in any environment (including liquids and vacuums), and has advantage on saving throws made to resist harmful gases and vapors.(Requires Attunement)`, 
            `+1 Venomous ${weaponType()} - You can use an action to coat the weapon in magical poison. The poison remains for 1 minute or until an attack using this weapon hits a creature. That creature must succeed on a DC 15 Constitution saving throw or take 2d10 poison damage and become poisoned for 1 minute. Any creature that fails their save can repeat their saving throw at the end of each turn. This effect has one charge which it regains at dawn. (Requires Attunement)`, `+1 Frightful ${weaponType()} - When a 20 is rolled on an attack roll with this weapon, the target and all other creatures within 10 ft must succeed a DC 15 Wisdom saving throw become effected by fear for one minute. Any creature that fails their save can repeat their saving throw at the end of each turn.`, `+1 ${weaponType()} of ${searchArray(animalArray)} Transmogrifying - The bearer may transform into one type of animal, as though using the Druid class feature Wild Shape. This effect lasts 1 hour, and has one charge which it regains at dawn.(Requires Attunement)`, `+1 ${weaponType()} of Warning - The owner gains advantage on initiative rolls. The owner and any allies within 30 ft can’t be surprised, except when incapacitated by something other than non-magical sleep. The weapon magically awakens the owner and companions within range if any are sleeping naturally when combat begins.(Requires Attunement)`, 
            `+1 Resilient ${weaponType()} - The bearer gains proficiency in an additional saving throw.(Requires Attunement)`, `+1 ${weaponType()} of Disorienting - When a creature is struck by this weapon, the first attack it takes on it’s following turn is taken with disadvantage. This effect does not stack.`, `+1 ${weaponType()} of Non-Detection - The owner is hidden from divination magic and can’t be targeted by such magic or perceived through magical scrying sensors.(Requires Attunement)`, `+1 ${weaponType()} of Lesser Spell-Storing - Any creature can Cast a Spell of 1st through 3th level into the weapon by touching the weapon as the spell is cast. This weapon can store up to 3 levels worth of Spells at a time. The bearer can cast any spell stored into this weapon without using components. The spell uses the slot level, spell save DC, spell Attack bonus, and spellcasting ability of the original caster, but is otherwise treated as if you cast the spell. The spell cast from the weapon is no longer stored in it, freeing up space.(Requires Attunement)`, `+1 ${weaponType()} of Aspected ${searchArray(damageTypes)} - This weapon deals an additional +1d8 damage.`, `+1 ${searchArray(damageTypes)} Laden ${weaponType()} - This weapon deals an additional +1d10 damage.`, 
            `+2 ${weaponType()} of ${searchArray(abilityTypes)} - The owner gains +2 to a single ability score. (Requires Attunement)`, `+2 ${weaponType()} of Soaring - The bearer gains a fly speed equal to its walking speed.(Requires Attunement)`, `+2 Dragon Slayer ${weaponType()} - When hit, dragons take an extra 3d6 damage of this weapon’s type.`, `+2 ${weaponType()} of Returning - This weapon has the thrown property with a normal range of 20 feet and a long range of 60 feet. If the weapon already has the throwing property, the normal range and long range of the weapon are both doubled. At any time, a bonus action may be used to return the weapon to its owner’s hand.(Requires Attunement)`, `+2 ${weaponType()} of Regeneration - The bearer regains 1 hit point every 5 minutes provided that the bearer has at least 1 hit point.(Requires Attunement)`, `+2 ${weaponType()} of ${searchArray(damageTypes)} Blast - When a 20 is rolled on an attack roll with this weapon, its critical hit deals an extra 4d6 damage.`, `+2 ${weaponType()} of Wounding - When a 20 is rolled on an attack roll with this weapon, its critical hit infers a “Wound” condition, dealing 2d4 damage at the start of the targets next 5 turns.`, `+2 ${weaponType()} of Opportunity - When the bearer makes their first opportunity attack per round, it does not consume a reaction.`, `+2 Transformative ${weaponType()} of the ${searchArray(animalArray)} - The bearer may transform into a single type of animal, as though using the Druid class feature Wild Shape. This effect lasts 1 hour, and has one charge which it regains at dawn.(Requires Attunement)`, 
            `+2 Curative ${weaponType()} - The bearer may cast Cure Wounds as a fifth level spell, using Wisdom as their spellcasting ability and the weapon as their focus. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+2 ${weaponType()} of Speed - The bearer can make one attack with this weapon as a bonus action on each of their turns.(Requires Attunement)`, `+2 Well-Rounded ${weaponType()} - The bearer gains a +1 bonus to all saving throws.(Requires Attunement)`, `+2 Adamant ${weaponType()} - This weapon negates all critical hits against the bearer.(Requires Attunement)`, `+2 ${weaponType()} of Spell-Storing - Any creature can Cast a Spell of 1st through 5th level into the weapon by touching the weapon as the spell is cast. This weapon can store up to 5 levels worth of Spells at a time. The bearer can cast any spell stored into this weapon without using components. The spell uses the slot level, spell save DC, spell Attack bonus, and spellcasting ability of the original caster, but is otherwise treated as if you cast the spell.The spell cast from the weapon is no longer stored in it, freeing up space.(Requires Attunement)`, `+2 ${weaponType()} of ${searchArray(damageTypes)}-Energy - This weapon deals an additional +2d6 damage.`, `+2 ${weaponType()} of ${searchArray(damageTypes)} Immunity - The bearer has immunity to one type of damage.(Requires Attunement)`, `+2 ${weaponType()} of Mage Hunting - The bearer has resistance to all damage dealt by spells.(Requires Attunement)`, `+2 ${weaponType()} of Protection - The bearer gains a +1 bonus to AC.(Requires Attunement)`, 
            `+2 ${weaponType()} of Mastery - The bearer’s proficiency bonus increases by +1.(Requires Attunement)`, `+2 Keen ${weaponType()} - The critical hit range for this weapon is increased by one.`, `+2 ${weaponType()} of Finality - Hit points lost to this weapon’s damage can be regained only through a short or long rest, rather than by regeneration, magic, or any other means. Creatures killed by this weapon can only be brought back to life by a True Resurrection or Wish spell.`, `+2 ${weaponType()} of Greater Spell-Storing - Any creature can Cast a Spell of 1st through 7th level into the weapon by touching the weapon as the spell is cast. This weapon can store up to 7 levels worth of Spells at a time. The bearer can cast any spell stored into this weapon without using components. The spell uses the slot level, spell save DC, spell Attack bonus, and spellcasting ability of the original caster, but is otherwise treated as if you cast the spell. The spell cast from the weapon is no longer stored in it, freeing up space.(Requires Attunement)`, `+2 Ethereal ${weaponType()} - The bearer may speak a command word as an action to gain the effect of the Etherealness spell, which last for 10 minutes or until the weapon is dropped or stowed. This effect has one charge which it regains at dawn.(Requires Attunement)`, `+2 Vorpal ${weaponType()} - The weapon ignores resistance to the weapon’s damage type. When a 20 is rolled on an attack roll with this weapon, if the target is a creature with at least one head, you remove one of the creature’s heads. The creature dies if it can’t survive without the lost head. Otherwise, the attack deals an additional extra 6d8 damage of the weapons type.(Requires Attunement)`, 
            `+2 ${weaponType()} of ${searchArray(damageTypes)} Fury - This weapon deals an additional +2d10 damage. `, `+3 ${weaponType()} of Greater ${searchArray(abilityTypes)} - The owner has a single ability score raised to 19 if it is below 19.(Requires Attunement)`, `+3 ${weaponType()} of Spellguard - The bearer receives advantage on saving throws against Spells and other magical effects, and spell attacks have disadvantage against you.(Requires Attunement)`, `+3 ${weaponType()} of Wondrous Protection - The bearer gains a +2 bonus to AC.(Requires Attunement)`, `+3 ${weaponType()} of Omniscience - The bearer has truesight with a radius of 30 ft.(Requires Attunement)`, `+3 ${weaponType()} of Wishing - The bearer may cast the spell Wish. This effect has one charge which it regains after one century has passed.(Requires Attunement)`,
            `Adamantine ${weaponType()} - This item is indestructible.`, 
            `${weaponType()} of Lunacy - Once attuned, the bearer constantly hears the ongoing, utterly insane mutterings of an alien intelligence trapped inside this weapon. Should this weapon be destroyed, the being will be released.`, `Ancient ${weaponType()} - This worn weapon inscribed with ancient runes can be used as a Spellcasting Focus`, `Antikytheran ${weaponType()} - An ancient mechanism is housed within this weapon that never configures the same way twice. Once per long rest the bearer can spend one minute to attempt a DC 20 investigation check to configure the device. If successful, the weapon becomes a +1 weapon until the end of the next long rest.`, `Arcane ${weaponType()} - This weapon can project a spectral tome suspended in mid-air that the bearer can interact with like a physical book. This tome can be used as a spellbook and may contain some spells from its previous bearer.`, `${weaponType()} of Snow - Icy wind and snowflakes bluster around this weapon, even in warm environments. The bearer can walk on the surface of the lightest snow, leaving no footprints.`, `Artist's ${weaponType()} - The bearer may use this weapon to make colored marks on any surface. The marks will fade away in 24 hours.`, `${weaponType()} of the Assasin - The bearer may add 1d4 poison damage to all attacks made during surprise rounds`, `${weaponType()} of Falling Leaves - The weapon contains a reservoir of natural magic that can a sustain a cascade of falling leaves for up to 30 seconds. The bearer may use an action to plant this weapon in the ground and release this magic. While planted and undepleted, creatures within 10 feet of this weapon have half cover. A long rest restores 1d6 sconds of energy to the weapon's resevoir.`, `Barbed ${weaponType()} - After an attack roll, the bearer may use their reaction to add 1d4 to the damage roll and take 1d4 damage.`, `${weaponType()} of Binding - When you hit a creature with this weapon, the ground beneath binds to its feet, slowing its speed by 5 feet until the end of its next turn. This has no effect on creatures that are flying or swimming.`, `Blasted ${weaponType()} - The bearer may use a bonus action to activate destructive magic within this weapon. It begins to glow with white-hot intensely, and at the beginning of the bearer's next turn, the weapon casts a level 1 Shatter spell (DC 12) centered on the weapon. The weapon then loses this property.`, 
            `${weaponType()} of Parables - Whenever the bearer of this item receives magical healing from a spell on the Cleric’s spell list, they gain an additional amount of hit points equal to their Wisdom (Religion) skill.`, -`${weaponType()} of Eyes - Garrish eyes are painted on this weapon. The bearer can use an action to see/unsee through the eyes, even if their own senses are compromised.`, `Blithe ${weaponType()} - The bearer is filled with inexplicable joy. All charisma skill and saving throw rolls gain a +1 bonus, but all wisdom skill and saving throw rolls gain a -1 penalty.`, `${weaponType()} of Bloodthirst - The bearer of this weapon spend a bonus action and a hit die to turn this weapon into a +1 magic weapon for 1d4 turns.`, `Bonded ${weaponType()} - This item is part of a pair of identical items. The bearer of either knows the location of the other at all times.`, `Booming ${weaponType()} - The bearer may choose to deal Thunder damage with this weapon and gain a +1 bonus to damage.`, `${weaponType()} of Knots - The bearer may use their action to cause the weapon to become a 50 ft length of hemp rope at will.`, `${weaponType()} of the Deep - The bearer can hold their breath for 5 minutes before the onset of asphyxiation.`, `Broken ${weaponType()} - This weapon is badly damaged. It is a testament to its former power that it is still serviceable. If reforged, it might regain its former power.`, `Capricious ${weaponType()} - If the weapon is attuned to a Chaotic aligned character, they may roll a die after completing a long rest. If the result was an even number, treat this as a +1 magic weapon until they finish a long rest.`, `${weaponType()} of the Lodestone - The bearer always knows which way is north and has advantage on Wisdom (Survival) checks for land navigation.`, `Caustic ${weaponType()} - The bearer may choose to deal Acid damage with this weapon and gain a +1 bonus to damage.`, `Chained ${weaponType()} - The bearer can spend an action to mystically bind or unbind themselves to this weapon. While bound, the bearer can no longer be disarmed but cannot switch out or throw this weapon.`, 
            `${weaponType()} of Saving Graces - While the bearer is at 0 hp, they begin to hear the most beautiful music they have ever heard. The bearer has advantage on death saving throws and cannot recall details about the music if they wake.`, `Charged ${weaponType()} - The bearer may choose to deal Lightning damage with this weapon and gain a +1 bonus to damage.`, `Chilled ${weaponType()} - The air around the bearer of this weapon is always unnaturally cold. One's breath becomes visible, and frost continually forms on the surface of the bearer's hair, weapons, and armor. The bearer suffers no ill effect from being in extremely cold environments.`, `${weaponType()} of the Capital - The bearer gains +1 to intelligence saving throws.`, `${weaponType()} of Compassion - Wounds inflicted with this weapon cause no pain.`, `Consecrated ${weaponType()} - Treat as a +1 magic weapon when attacking Undead. Any creature slain with this weapon cannot be raised as undead.`, `${weaponType()} of Dissolving - When the bearer hits a creature with this weapon, they may deal their proficiency bonus in acid damage to a different creature within 5 feet of the target.`, `Courser's ${weaponType()} - The bearer can placate and calm any mount not under the influence of a spell or possession.`, `${weaponType()} of the Crashing Waves - Whenever the bearer deals damage to a hostile creature, this weapon gains a charge. As a bonus action, the bearer can use any number of charges to deal that much extra lightning damage on their next attack. If a round (6 seconds) goes by and the weapon has not struck a foe, it loses all charges.`, 
            `${weaponType()} of Vermin - The crawling things of the earth, such as insects, snakes, and vermin, are attracted to this item. When placed on the ground, such creatures will scurry toward the item like moths drawn to the flame.`, `Cruel ${weaponType()} - The bearer may re-roll damage from critical hits scored with this weapon and take the second result.`, `${weaponType()} of Strings - The bearer may spend an action to permanently animate this weapon. Use the Flying Sword stat block from the Monster Manual p. 20. Also, the weapon retains any other magical properties. Once the animated weapon is reduced to 0 hp or unattuned, the weapon shatters like glass.`, `${weaponType()} of Darkness - The bearer may choose to deal Necrotic damage with this weapon and gain a +1 bonus to damage.`, `${weaponType()} of Rigor Mortis - If this weapon is entombed within a corpse for 8 hours, the bearer may treat it as a +1 magic weapon until the end of their next long rest`, `Deceptive ${weaponType()} - When the bearer attunes this item, choose a harmless object within sight such as a tea cup, a ball of yarn, or a hairpin. If the bearer is touching the item, they may use an action to transform the weapon in or out of this form.`, `${weaponType()} of Defense - Whenever the bearer takes a dodge or disengage action, they may move an additional 5 feet that round.`, 
            `${weaponType()} of the Delver - While underground, the bearer of this item always knows the item's depth below the surface and the direction to the nearest path leading upward.`, `Desperate ${weaponType()} - The bearer may use an action to release divine magic within, equivalent to a level 1 Cure Wounds spell being cast on all creatures (friend or foe) within 5 feet of the bearer. The weapon is destroyed and loses all magical properties.`, `${weaponType()} of Diplomacy - The bearer gains one language proficiency chosen by the DM.`, `${weaponType()} of Dragons - Treat as a +1 weapon when attacking Dragons.`, `${weaponType()} of Draining - When the bearer makes a successful attack with this weapon, they gain 10% of the damage as temporary hit points (round down, minimum of 1).`, `Dreamscribe's ${weaponType()} - The bearer can read books they are touching while sleeping.`, `Drunkard's ${weaponType()} - The bearer always knows the direction to the nearest tavern in a 60 mile radius.`, `Dryad's ${weaponType()} - When the bearer is outdoors, harmless creatures such as squirrels and birds flock to them when they sing songs for a minute or longer.`, `Eager ${weaponType()} - The bearer does not require an action to draw or sheath this weapon`, `Earthen ${weaponType()} - The bearer of this weapon is firmly rooted to the ground. When standing on solid earth or stone, if an effect would move the bearer against his will the distance is reduced by 5 feet.`, `${weaponType()} of the East - The bearer gains +1 to wisdom saving throws.`,
            `+1 Effortless ${weaponType()} - This weapon takes only one minute to attune.`, `Effulgent ${weaponType()} - The bearer can use this item to cast the Light cantrip on itself at will. While lit, it deals radiant damage instead of its usual damage type.`, `${weaponType()} of Apparitions - Dark apparitions bound to this weapon haunt the edges of the bearer's peripheral vision, becoming hideously visible to devour the bodies of beings slain by this weapon. Once 666 bodies have been devoured, the apparitions will be released to prey upon our world and the sword becomes a permanent +3 weapon. So far, the weapon has eaten ${(1+rollDice(6)) * 100 + (3* rollDice(20))} bodies.`, `Enchanting ${weaponType()} - Treat this as a +1 weapon as long as the bearer is enchanted by a spell from the enchantment school of magic.`, `${weaponType()} of Inner Strength - Once per long rest, the bearer may spend one minute contemplating the patterns etched on this weapon's surface and regain 1 expended ki point.`, `${weaponType()} of Truth - The bearer has advantage on investigation checks to see through illusions. In addition the bearer can gains advantage on an Insight check to check if someone is lying and disadvantage on all Deception checks.`, `${weaponType()} of Balance - When attuned to neutral aligned characters, this weapon has a +1 attack bonus during the day and a +1 damage bonus at night.`, `Etched ${weaponType()} - Ancient glyphs adorn the surface of this weapon, telling a story with a moral of the player's choosing (such as "One good turn deserves another" or "United we stand, divided we fall"). While attuning to this weapon, the glyphs spread across the entire skin of the bearer and the moral of the story becomes a bond trait for this character.`, `Fairweather ${weaponType()} - Treat this as a +1 weapon if the bearer has more than half of their maximum hit points.`, 
            `${weaponType()} of Intertwined Fates - Once per short rest, when the bearer crits with this weapon they gain inspiration.`, `${weaponType()} of the Favored - Once per long rest, the bearer may roll a saving throw with advantage.`, `Feathered ${weaponType()} - The bearer may use their reaction to reduce fall damage by 1d6 until the end of turn. They cannot use this feature again until completing a long rest.`, `${weaponType()} of Last Hope - The bearer may spend an action beseeching the spirits within this weapon. Roll a DC 20 Persuasion check or make a sufficiently impassioned plea. If successful, the spirits will sacrifice themselves so that for the next minute the next attack with this weapon will be a crit. The weapon then loses this property forever.`, `${weaponType()} of Speed - The bearer gains a +1 bonus to initiative rolls. As long as the bearer is first in the initiative order, their speed increases by 5 feet.`, `Forgotten ${weaponType()} - The bearer may spend an action to attempt to ignite the old magic in this weapon with a DC 13 Charisma check. If successful, treat the weapon as a +1 weapon as long as the bearer maintains concentration on this effect, maximum 10 minutes.`, `${weaponType()} of Friendship - Contains 1d4 unreplenishable charges of the Animal Friendship spell (1st level).`, `${weaponType()} of Ice - The bearer may choose to deal Cold damage with this weapon and gain a +1 bonus to damage.`, `${weaponType()} of Fury - Treat as a +1 magic weapon when the bearer is raging.`, `Ghost-Tipped ${weaponType()} - Whenever the bearer crits with this weapon, it gains the reach property (10 ft) for 1 minute. If it already had the reach property, increase its reach by 5 ft.`, `${weaponType()} of Remembered Glory - This weapon can be wielded by a missing limb. If so, it becomes a +1 weapon.`, `Glorious ${weaponType()} - The bearer may choose to change the damage type of weapon to Radiant and its damage roll gains a +1 bonus.`, `Goading ${weaponType()} - Once per short rest, when the bearer crits with this weapon it casts Compelled Duel on the creature it hit, DC 12.`, 
            `${weaponType()} of Protection - When the bearer attunes this weapon they must choose a being in their mind. Henceforth, if the bearer is within 5 feet of the chosen being they may use their reaction to impose disadvantage on an attack roll against that creature. They cannot do this again until they have finished a short or long rest.`, `${weaponType()} of Eavesdropping - As long as it is on the same plane of existence, the bearer can hear through this weapon as if they were present.`, `Haunted ${weaponType()} - Smoke rises from this weapon revealing the apparitions that haunt it. They lash out at living targets every time the bearer scores a hit, doing an additional +2 necrotic damage.`, `${weaponType()} of Healing - This item contains a healing node. Once per long rest the bearer can use the node and an action to heal 1d4 hit points at touch range.`, `Heroic ${weaponType()} - Ancient heroes have wielded this weapon throughout the ages, and their courage still lingers. The bearer has advantage on saving throws vs. fear effects.`, `Holy ${weaponType()} - When the bearer of this item rolls hit dice, they can choose to re-roll them and take the second result.`, `${weaponType()} of Symbols - The weapon is inscribed with holy symbols of the God of the DM's choice. A cleric or paladin that serves that god may use this weapon as a divine focus.`, 
            `Imaginary ${weaponType()} - Once attuned, this weapon exists only in the bearer's imagination until held with intent to do harm. It becomes imaginary again after a short rest.`, `${weaponType()} of Impact - Once per long rest, the bearer may spend an action to activate an ancient mechanism within the weapon. Gears turn and parts shift as the weapon reconfigures itself into a more menacing version of the original. For 1 minute, attacks made with this weapon ignore resistances (but not immunities).`, `${weaponType()} of Indifference - The bearer no longer feels emotions. They have immunity to fear effects but disadvantage on Insight and Performance checks, and cannot Rage.`, `${weaponType()} of Surging Strength - When the bearer is grappled by multiple targets, they may choose to break the strongest grapple. If they succeed, then all grapples are broken.`, `Inspired ${weaponType()} - The bearer gains their Constitution modifier in temporary hit points whenever they gain or use inspiration.`, `Jagged ${weaponType()} - Once hit by this weapon, the victim cannot regain hit points until the beginning of their next turn.`, `${weaponType()} of Madness - Once per short rest, when the bearer crits with this weapon it casts Crown of Madness on the creature it hit, DC 12`, `${weaponType()} of Leaping - Contains 1d4 unreplenishable charges of the Jump spell (1st level).`, `${weaponType()} of Lies - Contains 1d4 unreplenishable charges of the Silent Image spell (1st level).`, `Mage Killer's ${weaponType()} - Ignores the AC bonuses given by spells such as Mage Armor and Shield.`, 
            `${weaponType()} of Malediction - Contains 1d4 unreplenishable charges of the Bane spell(1st level).`, `${weaponType()} of Maligning - This weapon does an additional 1d4 damage on attacks of opportunity.`, `Marquis' ${weaponType()} - Once per short rest, when you crit with this weapon it casts Command on its target with the word "grovel", DC 12`,
            `${weaponType()} of Still Winds - The bearer and all of their possessions are completely odorless.`, `Master's ${weaponType()} - Contains 1d4 unreplenishable charges of the Unseen Servant spell (1st level).`, `${weaponType()} of the Meadow - A gentle kaleidoscope of butterflies always accompanies this weapon. The bearer has advantage on persuasion checks with Fae creatures less than CR 3.`, `${weaponType()} of Memories - When the bearer kills a monster with this weapon, treat this weapon as a +1 weapon whenever you fight another monster of this kind. When the weapon is unattuned, it loses its memory.`, `${weaponType()} of Mimicry - When the bearer places this weapon beside another melee weapon for 1 minute, this weapon changes weapon type, size, and physical qualities to become an exact replica of the other weapon. It does not gain any of the other weapon's magical properties.`, `Mindscour ${weaponType()} - This weapon disrupts all telepathic communication within 20 feet. Psychic attacks are not affected.`, `${weaponType()} of the Mind's Eye - The bearer may choose to deal Psychic damage with this weapon and gain a +1 bonus to damage`, `${weaponType()} of the Mortal Coil - The bearer's vital signs, such as a pulse and breathing, are masked by this weapon and are undetectable by non-magical inspection.`, `${weaponType()} of Last Words - Contains one charge of the Speak With Dead spell. It regains the charge when the bearer dies.`, `Murderous ${weaponType()} - When the bearer reduces a creature to zero hit points they may use a bonus action to move half their movement speed towards another hostile creature.`, `${weaponType()} of the North - The bearer gains +1 to constitution saving throws`, `${weaponType()} of Comfort - Once per long rest, the bearer may lay this weapon beside a bowl of water. After a moment, the bowl of water will begin to boil and after a minute it will transform into a hot meal of special significance to the bearer (Their mother's noodle soup or father's elk stew). Eating this delicious meal is so satisfying that it counts as nourishment for an entire day and restores 1d4 hit points. To anyone other than the bearer, the bowl and its contents appears unchanged.`, `Nullifying ${weaponType()} - Any spell of 1st level or lower that includes the bearer as a target has a 10% chance to fail, cast by both friendly and enemy spellcasters.`, 
            `${weaponType()} of Pain - Treat this as a +1 weapon for 1 minute if the bearer takes 13 or more damage in a single round of combat.`, `${weaponType()} of Parrying - The bearer may use their reaction to gain a +1 AC bonus until the end of the turn.`, `Patient ${weaponType()} - Whenever the bearer readies an action, they have advantage on constitution saving throws to maintain concentration.`, `${weaponType()} of the Snake - The bearer may choose to deal Poison damage with this weapon and gain a +1 bonus to damage.`, `Phantom ${weaponType()} - Damage inflicted with this weapon leaves no physical sign of injury, such as cuts and bruises, and draws no blood.`, `${weaponType()} of the Pious - The bearer may spend ten minutes paying honor to the spirits that govern this weapon, shaving their head in tribute. Once the ceremony is finished, it becomes a +1 weapon until the end of the next long rest. They must wait 10 days until they have long enough hair to re-enact this ritual.`, `Preacher's ${weaponType()} - This weapon increases the bearer's Channel Divinity range by 5 feet.`, `${weaponType()} of Force - The bearer may choose to deal Force damage with this weapon and gain a +1 bonus to damage.`, `${weaponType()} of Uncertainty - Every time the bearer takes a long rest, this weapon changes in appearance and function. It retains this property but any other properties are lost.`, `Quicksilver ${weaponType()} - The bearer may use a bonus action to change the form of the weapon to any other simple or martial melee weapon. It always counts as a silvered weapon no matter what form it takes.`, `Prismatic${weaponType()} - The bearer may change the damage type of a spell they cast once per long rest.`, `Refined ${weaponType()} - This weapon is so finely constructed it never needs maintenance, cannot rust or tarnish, and gains a +1 to damage rolls.`,
             `Reliable ${weaponType()} - When attacking with this weapon, crit fails (rolling 1) on attack rolls do not automatically miss the target.`, `${weaponType()} of the Renaissance - Once per long rest, the bearer may gain +1 to any skill check.`, `Resonant ${weaponType()} - The bearer can spend an action and 1 ki point to treat this as a +1 weapon for 1 minute.`, `${weaponType()} of Subdual - This weapon only deals non-lethal damage to living targets`, `${weaponType()} of Righteousness - Treat this as a +1 weapon during the day when attuned to a good aligned character.`, `Rosen ${weaponType()} - A ruby worth 30gp is the center stone in a rose-shaped setting on the weapon. If the bearer removes the ruby, the weapon grows a new one at the end of the month. The weapon always smells of roses while the ruby is in its setting.`, `Runic ${weaponType()} - Whenever bearer casts a spell, treat this weapon as a +1 weapon until the beginning of their next turn.`, `Scarlet ${weaponType()} - This weapon perpetually drips the blood of a monstrous race, chosen by the DM. The bearer can speak that race's language and has advantage on intimidation checks against monsters of that race when the weapon is revealed.`, `${weaponType()} of Sieges - This weapon does maximum damage against man-made, inanimate objects.`, 
             `${weaponType()} of Shade - The bearer suffers no harm or discomfort in temperatures as high as 120 degrees Fahrenheit.`, `${weaponType()} of Shadows - Treat as a +1 magic weapon when in dim light.`, `Shamanic ${weaponType()} - Whenever the bearer is casting a spell as a ritual, they have advantage to maintain concentration during the ritual.`, `${weaponType()} of Disgrace - Any humanoid creature hit with this weapon loses all of the hair on their head and face.`, `${weaponType()} of Shielding - This item contains 1d4 unreplenishable charges of the Shield spell.`, `${weaponType()} of Unusual Gravity - This weapon falls up instead of down. Its weight does not contribute towards encumbrance.`, `${weaponType()} of Slaying - Treat as a +1 weapon when attacking Demons and Devils.`, `${weaponType()} of Flame - The bearer may choose to deal Fire damage with this weapon and gain a +1 bonus to damage.`, `Smuggler's ${weaponType()} - This weapon contains a small, secret compartment. A character must succeed on a DC 20 Wisdom (Perception) check to reveal the compartment when searching the bearer.`, `Sojourner's ${weaponType()}- A poem, story, or map that describes a long-forgotten treasure that will make this weapon more powerful is etched on the surface of the weapon.`, `Solemn ${weaponType()} - The bearer may spend an action to stabilize a dying creature within 5 feet. They cannot do so again until they have completed a long rest.`, `${weaponType()} of Imprisonment - A powerful malevolent being is bound within this weapon and it will be released upon the weapon's destruction.`, 
             `${weaponType()} of the South - The bearer gains +1 to dexterity saving throws.`, `${weaponType()} of Spring Rain - The weapon contains a pool of healing energy that can restore up to 30 hp. The bearer may use an action to plant this weapon in the ground and release this energy. While planted and undepleted, creatures that end their turn within 10 feet of the weapon are showered in warm rain that restores 1 hp per round. A long rest restores 1d6 hp of energy to the weapon's pool.`, `Staunch ${weaponType()} - Anyone except the bearer must attempt a DC 10+x Charisma check to pick up this weapon, where x is the bearer's level. Any attack made with this weapon against the bearer has disadvantage.`, `Strange ${weaponType()}- Treat this as a +1 weapon when attacking Aboleths and other creatures from the Far Realm`, `Strapping ${weaponType()} - Whenever the bearer breaks a grapple, they may choose to push the grappler up to 10 feet away from them as a bonus action.`, `${weaponType()} of Strides - Contains 1d4 unreplenishable charges of the Longstrider spell (1st level).`, `${weaponType()} of the Scorching Sun - The weapon contains a reservoir of scorching light that can deal up to 30 hp of radiant damage. The bearer may use an action to plant this weapon in the ground and release this energy. While planted and undepleted, creatures that end their turn within 10 feet of the weapon are brightly illuminated and seared for 1 radiant damage per round. A long rest restores 1d6 hp of energy to the weapon's reservoir.`, `${weaponType()} of the Surgeon - The bearer may use a bonus action to gain advantage to Wisdom (Medicine) checks for the rest of the turn.`, `Reflexive ${weaponType()} - If the bearer is first in the initiative order, they may treat this as a +1 weapon.`, `${weaponType()} of the Tenacious - When the bearer takes a long rest, they gain back one additional hit die.`, 
             `${weaponType()} of Tithes - The bearer may lay 10 gold coins along the surface of the weapon and pray to a God of their choice for 10 minutes. At the end of this ritual, the weapon becomes a +1 weapon until the next long rest and the 10 gold coins are permanently gone. This boon will be lost if the bearer acts in a way that is contradictory to that deity's teachings.`, `${weaponType()} of the Breaking Seal - Over the course of a long rest, the bearer may transfer the other magic properties of this weapon to a melee weapon of their choosing. This weapon then loses those properties.`, `${weaponType()} of Translucence - The bearer gains an extra level one spell slot, which recovers only after a full moon rises.`, `Trusty ${weaponType()}- Treat this as a +1 weapon if the bearer has half their maximum hit points or less.`, `${weaponType()} of Crashing Waves - Once per short rest, when the bearer crits with this weapon, all creatures other than the bearer within 5 feet of the target (including the target) must roll a DC 12 constitution saving throw or be knocked prone by a wave of concussive force.`, `Twilight's ${weaponType()} - Once per short rest, when you crit with this weapon it casts Hex on the target. Roll a d6 to determine which of the target's attributes is weakened. The bearer cannot transfer the curse to another creature.`, `${weaponType()} of Unity - Whenever the bearer of this weapon takes a help action in combat, the aided ally may treat their weapon as a +1 magic weapon until the end of their next turn.`, `${weaponType()} of Victory - Whenever the bearer kills a creature with this weapon, they gain temporary hit points equal to the creature's CR (minimum of 1).`, `Vigilant ${weaponType()} - The bearer gains +1 to their Passive Perception.`, `Violent ${weaponType()} - Everytime you crit with this weapon, it gains 1 charge. As a bonus action, use a charge to make this a +1 weapon for 1 minute. All charges are lost at the end of a long rest.`, `Vile ${weaponType()} - Treat this as a +1 weapon at night when attuned to an evil aligned character.`, `${weaponType()} of the Visionary - The weapon does an additional 1 elemental damage based on the color of the bearer's eyes: (amber: lightning, black: necrotic, blue: cold, brown: acid, green: force, gray: thunder, hazel: poison, purple: psychic, red: fire, white: radiant)`, 
             `${weaponType()} of Vitality - The bearer's maximum hit points increases by their constitution modifier while attuned to this item. These hit points are lost when the bearer unattunes the item.`, `${weaponType()} of the Void - This weapon cannot be detected by the "Detect Magic" spell unless the caster touches the weapon.`, `Voltaic ${weaponType()} - Whenever the bearer deals damage to a creature, this weapon gains a charge. As a bonus action, the bearer can use any number of charges to deal that much extra lightning damage on their next attack. If a round (6 seconds) goes by and the weapon has not struck a foe, it loses all charges.`, `${weaponType()} of the War Leader - The bearer can use an action to amplify their voice three times louder than normal.`, `Warded ${weaponType()} - Once per long rest the bearer may draw a 20 foot line in the ground with this weapon that lasts for 1 minute. The Undead must succeed on a DC 12 wisdom saving throw to move across this line. If they fail, they cannot move again until their next turn.`, 
             `${weaponType()} of the Sea - The item floats on water or other liquids. Its bearer has advantage on Strength (Athletics) checks to swim.`, `${weaponType()} of the Weave - Whenever the bearer casts a spell, this weapon gains charges equal to the spell's level. The bearer can use a bonus action to remove 13 charges and make this a +1 weapon until the start of the next round. All charges are lost during a long rest.`, `${weaponType()} of the West - The bearer gains +1 to charisma saving throws.`, `${weaponType()} of the Wilds - The bearer gains +1 to strength saving throws.`, `Winged ${weaponType()} - Once per long rest, the bearer may use an action to transform this weapon into a magical raven that can deliver a message to anyone in a 50 mile radius, provided the bearer knows their name and face. When the raven returns, it reverts into its weapon form. If the bird should die en route, it reverts into weapon form and unattunes from the bearer.`, `Winter's ${weaponType()} - The weapon contains a reservoir of ice magic that can a freeze the ground for up to 30 seconds. The bearer may use an action to plant this weapon in the ground and release the ice magic within. While planted and undepleted, the ground in a 10 foot radius of this weapon becomes difficult terrain. A long rest restores 1d6 seconds of energy to the weapon's reservoir.`, `${weaponType()} - of Felling - This weapon does maximum damage against plant creatures.`, `Zen ${weaponType()} - Treat this as a +1 weapon for 1 minute after meditating with it for 1 minute.`,
        ]
        let runes = [
            "Rune of the Wind - When an enemy is struck with this weapon, the must make a DEX saving throw or be blown back 5 ft.", "Rune of the Squirrel - Grants advantage to the acrobatics skill.", "Rune of the Dog - Grants advantage to the animal handling skill.", "Rune of the Raven - Grants advantage to the arcana skill.", "Rune of the Bear - Grants advantage to the athletics skill.", "Rune of the Snake - Grants advantage to the deception skill.", "Rune of the Elephant - Grants advantage to the history skill.", "Rune of the Owl - Grants advantage to the insight skill.", "Rune of the Lion - Grants advantage to the intimidation skill.", "Rune of the Crow - Grants advantage to the investigation skill.", "Rune of the Lobster - Grants advantage to the medicine skill.", "Rune of the Elk - Grants advantage to the nature skill.", "Rune of the Eagle - Grants advantage to the perception skill.", "Rune of the Peacock - Grants advantage to the performance skill.", "Rune of the Feline - Grants advantage to the persuasion skill.", "Rune of the Mantis - Grants advantage to the religion skill.", "Rune of the Spider - Grants advantage to the sleight of hand skill.", "Rune of the Chameleon - Grants advantage to the stealth skill.", "Rune of the Cockroach - Grants advantage to the survival skill.", "Rune of Orcus - any humanoid creature of size large or smaller killed by this weapon rises as a zombie under your control for 20 minutes. After 20 minutes, the zombie collapses and turns back into a corpse.", "Rune of Confusion - every time a creature is hit by this weapon, it must make a charisma saving throw against a DC equal to 8 + wielders prof bonus + wielders strength modifier (or dex if it’s a finesse weapon). On a failed save, the creature has disadvantage on its next attack against the wielder. Once a creature succeeds against this saving throw, this rune no longer affects it until its next long rest.", "Rune of Defense Crushing - each time a creature is hit by this weapon, it must make a strength saving throw against a DC equal to 8 + wielders prof bonus + wielders strength modifier (or dex if it’s a finesse weapon). On a failed save, the creatures armor class is lowered by 1. This rune may not bring a creatures armor class below 10 + their dexterity modifier.", "Rune of Unjo (Joy and Wellness) - The bearer of this rune is able to stave off one level of exhaustion.", 
            "Rune of Hagalaz (Chaos and Destruction) - The bearer of this rune can cast Thunderwave once per day.", "Rune of Pertho (Protection from enemies) - The bearer of this rune can cast Protection from Evil one per day.", "Rune of Ehwaz (Trust, faith and companionship) - the bearer of this rune can cast Bless once per day.", "Rune of Swordbreaker - If the wielder is attacked with melee weapon and the attack is a critical failure, the player can break the attacker’s weapon.", "Rune of Leaden Steps - adds 10 pounds to the target’s weight on each attack.", "Rune of Vaporization - Once a day you can submerge the weapon into water and vaporize 1d20 cubic feet of water.", "Rune of Returning - Once etched on the weapon, it allows the user to call the weapon into their hand if it’s within 10 ft.", "Rune of Safety - Renders the edges/points of the weapon dull when children touch the weapon.", "Rune of Green Thumbs - If the weapon to be planted in soil, a 30 foot tall tree will out of it in 1d4 days. The weapon is destroyed in the process.", "Rune of Invisibility - Makes the weapon appear invisible to all, except for those designated by the rune-maker.", "Rune of Poison Detection - If the weapon is dipped into poisoned food, the hilt changes color. The colors return to normal once poisoned is removed from the weapon.", "Rune of Screaming - When the weapon this rune is inscribed upon strikes an enemy, the target must make a Wisdom saving throw with a 13 DC. If it fails, the target starts screaming uncontrollably for 1d10 minutes and is terrified of the attacker.", "Rune of the Cliff - Allows the casting of Featherfall on command.", 
            "Rune of the Worg - This weapon seems easy to hold in your mouth, you don’t know why. You can now use your mouth as an ‘arm’ to hold this weapon – even if it requires two hands. You also know how to run on four legs like a beast (Your speeds increases by 10 ft. while doing so). You have disadvantage to make weapon attacks with your arms.", "Rune of the Gryphon - When this weapon is swung upward, your jump distance is multiplied per 10. If you manage to hit an enemy while falling, you ignore all falling damage. If you keep swinging this weapon while spinning you might fly…", "Rune of the Manticore - The weapon inscribed starts growing 1d10 spikes each day that, if removed, can be thrown as daggers with the range of a Longbow, or used as ammunition for the inscribed weapon. A weapon can have up to 10 spikes if one handed or 30 if two handed. The spikes seem very efficient for impaling or piercing hard surfaces like rock. If you leave a spike grow for a week, it becomes the length of a short sword; for a month of a longsword; for two months of a spear and for three months of a pike. All these weapons can be thrown at the range of a Longbow.", "Rune of Fire - This weapon’s damage type has changed to fire.", "Rune of Ice - This weapon’s damage type has changed to ice.", "Rune of Mirrors - Once per short rest, as a bonus action, the user can break this weapon into two identical copies of the original. If either copy leaves the possession of the character who broke the weapon in two, the copy disappears and the effect is ended.", "Rune of the Firebreather - This weapon, when slashed, creates a ten-foot line of fire. All creatures in the line must make DEX save or take 1d6 Fire damage.", "Rune of Echoes - The wielder must make a noise into the enchanted weapon. When this weapon attacks, it leaves behind a rune on the target object. This rune continues to repeat the noise that the wielder recorded earlier, acting as a distraction.", "Rune of the Kebab (pike or spear only) - As an Action, you cause the weapon to grow outward then retract in a 30 ft. line. Make an attack against every creature in this line.", 
            "Rune of Helium - Once in a long rest as a bonus action you can put your weapon in front of your neck and make your voice squeakier like that of a mouse. You have an advantage on performances check and intimidation check against Large or larger creatures that are capable of hearing you.", "Rune of Sulfur Hexafluoride - Once in a long rest as a bonus action you can put your weapon in front of your neck and make your voice deeper like that of a dragon. You have an advantage on performances check and intimidation check against Medium or smaller creatures that are capable of hearing you.", "Rune of Wild Magic - On a critical hit with this weapon, roll on the Wild Magic Surge table to create a random magical effect.", "Rune of Snail Shell - This weapon or shield is nearly unbreakable by non-magical means, however becomes so dense and heavy that it effectively eliminates any dex bonus the player has to their AC.", "Rune of the Bull - Any weapon or shield this rune is attached too gives the player advantage on attempts to shove large or smaller creatures. Shove attempts send the target back 5 feet more than usual.", "Rune of the Phoenix Feather - This rune provides the item it is slotted in, to turn into flames dealing 1 fire damage per round to players and creatures unless they have fire resistance. The item magically reforms if it is ever destroyed.", "Rune of Absorbing - Once per day, you can spend a minute to change the material of the weapon to any material that it is in contact with.", "Rune of the Open Door (any bludgeoning weapon) - This weapon deals double damage against structures. Any damage done to the structure using this weapon does not affect the stability of the structure. (For instance, this weapon can create a hole in a load-bearing wall while the rest of the building is unaffected). This structural protection effect ends after 1d4 hours.", 
            "Rune of Terran Blessing - The wielder cannot be knocked prone by any environmental hazards (earthquakes, slippery ground, falling rocks, etc.).", "Rune of Heaven’s Fan - when this weapon is swung, a gust of cool wind is released, extinguishing fires and briefly turning the ambient temperature tolerable regardless of its previous state. Twice a day, the wielder can slash the weapon downwards to create a 40-ft long, 5-ft wide blast of downwards wind that forces everyone hit to make a STR save or be knocked prone (if flying, they’ll fall out of the air), with DC potentially modified by one’s own eight. This ability slaps most projectiles out of the air, and can be used as a reaction to a projectile attack.", "Rune of Time’s Shadow - any attack made with this weapon is repeated by a translucent, phantasmal shadow of it on the next turn at the same location. That shadow attack does the same damage, but can only hit an enemy in the same space as the original attack’s target.", "Rune of Death’s Tongues - any successful hit with this weapon causes hungry, flesh-eating worms to spontaneously appear where the weapon hit. As they burrow into the wound, they prevent regeneration from the damage dealt, and deal 1d6-4 poison damage each subsequent round for 1d10 subsequent rounds.", "Rune of Fire’s Wake - things hit by this weapon release a cloud of thick smoke that visually obscures an area of 10ft radius. Enemies or at least partially empty containers hit by this weapon fill up with a thick smoke. Those hit make a CON save as their respiratory system fills up completely with smoke; on a success, they expend their upcoming bonus action to cough out the smoke, but on a failure, they lose their upcoming action to do so.", 
            "Rune of the Journey - any enemy hit by this weapon makes a WIS save; otherwise, they will spend their upcoming movement to double back on the last turn of movement they took. If this takes less movement than their speed, they can use the remainder of this turn’s movement normally. If doubling back proves impossible (e.g. on the last turn they moved, they dropped from a high ledge, but on this turn it’s impossible for them to jump back up onto that ledge) they will still try to go back on that path if a logical alternative (in this example, climbing a nearby staircase to get to that ledge) is obvious to them. If no logical alternative presents itself, the effect is broken.", "Rune of the Immanence - the wielder may cast Misty Step once per day. With the proper material components, the wielder may cast Plane Shift once per day.", "Rune of the Inhabitance - the wielder gains the effects of a short rest on a critical hit with this weapon.", 
            "Rune of Fehu (Wealth, Fulfillment, Fire) - the wielder of this weapon may activate this rune once per day for the duration of one encounter, causing the weapon to burst into golden flames that deal extra fire damage. Successful hits while the rune is active cause 2d10 gp to fall from where it hit.", "Rune of Gifu (Gifts) - the wielder of this weapon can freely teleport this weapon into the hands of another creature they can see within 120 feet. This method of transference does not harm the recipient, but will displace any objects they are currently holding. This ability stores three charges and regains one charge per day.", "Rune of Alliance’s Might - this weapon gains 1d6 extra damage of the type it would normally deal per person allied with the wielder in 60ft.", "Rune of the Carousel - Causes sentient beings struck by the weapon to spin uncontrollably at a fairly high speed for a few seconds. The affected must pass a DC 7 Constitution check or lose their turn as they try to regain their bearings and not vomit.", "Rune of Refraction (Melee Weapon Only) - The weapon refracts light strangely causing it to look broken (e.g. when observing a straw above and below water-line at an angle) causing everyone but the wielder to have trouble discerning its actual location. +1D4 to Attack Rolls & +1 AC against Melee Attacks to adjust for enemies not being able to block/dodge as easily while giving them mild motion sickness as they attempt to track the actual location of your weapon.", "Rune of a Stranger - Once per long rest, if you invoke this ability, every creature in the battle has to succeed a DC 10 WIS save or forget your alliance for one round.", 
            "Rune of Enlarging - When you touch this rune as a bonus action your weapon becomes bulky and now has the Heavy Tag. During this time your weapon deals an extra 1d6 of damage on each successful attack. This transformation ends after 1 minute, if you drop the weapon or if you touch the rune again as a bonus action. Using this ability on a weapon that already has the Heavy Tag has no effect.", "Rune of the Goose - On your turn, you may reduce your bonus to hit by half when you make an attack. On a successful hit, the target must make a DC 8 + your weapon’s bonus to hit Wisdom saving throw, or become frightened for 1 minute. The affected creature may repeat the saving throw at the end of each of its turns. Once you use this rune, you cannot use it again until after a short or long rest. You may apply up to 3 Rune of the Gooses to gain additional uses of this feature between rests, 1 use for each rune.", "Rune of the Dawn/Zenith/Dusk/Midnight Shine - During the corresponding time of day, lasting two hours, the weapon shines as under the effect of the Light cantrip, and deals an extra 1d10 radiant damage. (Upon rolling the rune, you may roll a d4 to determine the corresponding time of day.)", "Rune of Bloodlust - While using the weapon, you can enter a rage once per long rest, with the features of a level 3 Barbarian’s rage (minus Primal Path benefits). If you have a Barbarian level greater than 3, you may use your own rage features (including Primal Path ones) while entering this rage.", "Rune of Melody - In combat, the weapon emits a soft, musical humming. With practice, you may use the weapon as an instrument.", 
            "Rune of Celestial/Fey/Fiend/Elemental/Undead Slaying - The weapon shines when a creature of the appropriate type is 30 ft. or closer. The wielder is protected from those creatures as by the Protection From Evil And Good spell, and the weapon deals an extra 1d6 damage against them.", "Rune of Foresight - You can use the weapon once to cast Augury as a 2nd-level spell per short rest. Wisdom is your spellcasting ability for this spell.", "Rune of True Strike - Every time you attack, roll a d10. On a 10, you gain advantage on your attack roll and, upon a successful hit, you can roll for damage twice and choose either result.", "Rune of Vampirism - Every time you hit, roll a d4. On a 4, you regain an amount of hp equal to half the inflicted damage.", "Rune of Arcane Storage - You may store up to 5 levels’ worth of spell slots within the rune. Doing so requires 10 minutes per level, consumes the spell slot, and counts as a ritual. If you are touching the rune while casting a spell, you may choose to consume an amount of stored levels equal to the level of the spell instead of your own spell slots.", "Rune of Truth - When a creature speaks a deliberate lie within 15 ft. of the rune, the weapon vibrates slightly for a few seconds. Detecting this vibration is no challenge, unless the wielder isn’t paying attention to the weapon’s response.", "Rune of Speed - While holding the weapon, you can use the Dash action as a bonus action on each of your turns.", "Rune of Wild Magic - On a critical failure using the weapon to attack triggers a Wild Magic Surge. Effects that require targeting are directed at the creature closest to the wielder.", 
            "Rune of Aquan Blessing - Wielder’s base speed increases by 10 ft. anytime it is raining or they are standing at least ankle deep in water.", "Rune of the Primordial - Wielder can speak Primordial, and has advantage on Charisma checks on creatures that understand it.", "Rune of Transformation - As a bonus action, on a successful Intelligence skill check, the wielder may cause the weapon to turn into any other weapon they are proficient with. No ammunition is produced this way. The weapon reverts to its true form after one hour or if the wielder loses hold of it.", "Rune of Reflexes - You can use an extra opportunity attack per turn with this weapon, in addition to your reaction.", "Rune of Bombardment - You can activate this rune with a power word of your choice. One turn after activation, the weapon will produce a 3rd-level Fireball spell centered on itself. This destroys the weapon.", "Rune of Vanishing - The last rune to be carved into the item. Upon completion all runes carved into the item vanish from sight and are only visible to the creator of the item.", "Rune of Life - This greater rune of enchantment gives item wielder immortality. He will not age, get sick or be harmed by poison. Normal damage and weapons will still kill him.", "Rune of Alarm - This rune will begin to glow (or emit audible alarm) when certain type of creature (Dragonkind, undead, bald men…) approaches within certain range.", "Rune of Possession - Unless the weapon is freely given or taken from its owner upon their death, this rune refuses to be attuned to another person. In addition, non-owners take -4 penalty on attack rolls if they attempt to use in the first round of combat. Subsequent rounds of combat, the weapon heats up and the holder takes 1d4 points of damage.", "Rune of Sundering - When using the weapon to sunder objects, take a +4 bonus to attack rolls.", 
            "Rune of Spirit - Grants +2 morale bonus to attack rolls. In addition the weapon gains the ghost touch trait.", "Rune of Auran Blessing - Wielder gains advantage on Animal Handling checks against creatures with a natural flight speed.", "Rune of Returning - When the weapon is lost or stolen, it will always return to its true owner’s side after one long rest, along with one-piece ammunition if it’s a ranged weapon.", "Rune of the Impersonnel - Once per turn when melee attacking using this weapon you can teleport to the opposite side of the creature.", "Runs of Diplomacy - This rune allows the user to cast comprehend languages 3 times per short rest, the rune also gives you proficiency in the persuasion skill, however, due to the rune’s desire for peace, the rune gives -2 to attack and damage rolls against good aligned creatures.", "Rune of Stone - Typically engraved on mauls, maces, and hammers, it is found on some heavy swords. This rune, it’s said, makes your weapon unbreakable in battle, and allows you to smash through enemy defenses, and cut through stone as if it were flesh.", "Rune of Bees - Once per long or short rest, this rune allows the user to summon a swarm of bees to deal 2d4+2 Piercing or Poison damage as a bonus action. The user also gains a strange fondness for flowers.", "Rune of the Duelist - When targeted by an enemy melee attack, you may impose disadvantage on the attack as a reaction. If the melee attack misses, you may attack the enemy who just attacked you.", "Rune of Ignan Blessing - Natural flames in the area around the wielder glow brighter and hotter, shedding light an extra 10 ft. and dealing an extra 1d4 damage when applicable.",
        ]
        let chance = rollDice(100)
        if (chance < 50) {
            return searchArray(enchantmentArray);
        } else if (chance < 75) {
            return searchArray(enchantmentArray) + ' Special effect: ' + searchArray(optionalProps);
        } else {
            return searchArray(enchantmentArray) + ' Also, the weapon is covered in a beautiful runic inscription: ' + searchArray(runes);
        }
    }
    document.getElementById("Weapon").innerHTML = weaponGenerator()
};
function findHistory() {
    let weaponHistories = [
        "...was forged in the Age of Mists by a powerful necromancer who wanted to use it against his most dread foes - a powerful paladin order.", "...was coughed up from the belly of the sleeping Tarrasque after it was fired upon by a Githyanki starship.", "...was dreamed into existence by the oldest of the Fey, and still carries a touch of the Wild upon it.", "… was birthed into existence during a brutal battle by the dying screams of the vanquished.", "… fell from the sky, thrown to earth by a goddess, which caused discord in the heavens.", "… broke apart from a bigger item, and was repurposed twice to fit its current state.", "… a living piece of a dying deity, long lost to time.", "… was pulled from the pages of a magical storybook.", "… has been tinkered together by Morman The Forlorn under threat of death, with his hate still inside.", "… was a rumor that was believed into reality.", "… was mistakenly stolen by Balog the Spoon Thief, twice.", "… was a royal heirloom that went missing when the last living heir disappeared without a trace.", "… was passed between several pirate lords as a result of lost bets and foul wagers.", "… famously stolen by the mistress of the prince at the time as punishment for bragging to his comrades about her acts.", "… had a war fought over it, a war that cost 10.000 lives.", "… was shaped from darkness on the day, three eons ago, that the Sun didn't rise.", "… was a gift between two lovers, who cooperatively created it as an act of love.", "… forged by the first dwarf, the first weapon of its kind.", "… is a vessel of significant power, even though the vessel is leaking and the content unknown.", 
        "… it was simply found one day, several centuries ago, bearing only a single marking in an ancient language meaning “be godless”.", "… ordered to exist by The Creator, an entity that helped shape the world.", "… a magical ripple broke the fabric of reality, and a creature of the beyond bestowed it upon their unwilling champion.", "… said to be distilled from the moon itself.", "… nature itself created it from all over, specifically made to defend her.", "… it was meant to be broken up into pieces and spread across the world, at the word of an ill-omened prophecy, but it never was.", "… grafted from the root of the world tree.", "… famed for its role in the last stand of the Fuari, and their extinction.", "… once claimed after tricking the deity of Fertility into a bet.", "… was promised to be enchanted by an Archfey, the rightful price was never payed.", "… wielded by a fair maiden so beautiful that most lost both their hearts and their lives.", "… crash landed on this world in a mass of vines and buds found native only to a few small islands in the western hemisphere.", "… was thrust from a realm far beyond the horizon after a game of throwing bones.", "… sprouted from a tumor on a troll’s foot.", "… manifested when a demon child broke his toy.", "… was produced when a crazed detective sprouted from a hippopotamus's backside.", "... is a part of the social conscious and came to be through sheer willpower", "... fell from the sky one day and clonked you on the head.", "… was hidden in the reflection of another weapon, pulled forth from the glass.", "… was a living person before being polymorphed.", 
        "… was a gift from a screaming demon, come down upon their Comet-Crusher and impaled in the heart of a king.", "… fell out of a magic mirror.", "… came from inside your own heart. Just reach in and pull it out.", "… is the shadow of a holy weapon, cast up from the lights of Hell.", "… came from the future.", "… was carried over from another campaign.", "… was stolen from a Dragon’s hoard who still seeks it.", "… made from the bones of a Hydra, a Catoblepas, and an Umber Hulk.", "… was inside of the oldest tree in the forest forgotten", "… fell to the deepest depths of the oceans and was cast out back upon the land.", "… was sold by a poor aging knight for a day’s rations", "… forged in honor of the dying prince so his memory lived on.", "… came to be when the druid asked the pig what did you eat today.", "… a star streaked across the sky and the mother wished to always protect her son.", "… when the old elf riddled with worry dreamed of impending doom the answer lie in his hands when his eyes opened.", "… when a seed was planted it grew instead of the crop.", "… was found stuck in the gums of old Ripple Belly the fat dragon when he finally passed away.", "… was stolen by a time thief hearing of its great power to forever alter the course of time.", "… was tossed away as scrap by the blacksmith thinking he had failed his task.", "… found stuck in a stone in a forgotten glade of beauty and peace", "… made from the bones and hair of his lover the hero used it to exact revenge upon the foul murder.", "… was created in a time before time as The Universe gave its first breath.", "… coalesced from the wasted energies in a ritual of dark intent.", "… formed in the bowels of a forgotten beast.", "… was molded from clay and given substance by the blood of a god.", "… was lanced from the tumors of a sewer mutant.", "… formed in a clot from a river of blood on an ancient battle field.", 
        "… was spun from the wool of a golden sheep.", "… was regurgitated by a drunken Otyugh.", "… was found in the privy at a local brothel.", "... was forged from the knuckle bones of fifty devils.", "… carved from the fossilized dung of a prehistoric monster.", "… eaten by a Shoggoth, then spat up changed…", "… found at the bottom of a packrat midden", "… found in the debris left by a landslide", "… fell from the sky on the equinox", "… rendered from the fat of seven hanged men", "… is what's left of the phylactery of a long dead Lich", "… was found lodged deep in a glacier far to the north", "… was found in the core of a toppled tyrant’s statue", "… was cut from the stomach of a possessed man", "… created by hags from the fingernails of lost children", "… was carried by a living snowman who said I could keep it if I killed him with it.", "… fell from the Plane of the Gods.", "… came to me in a dream where a masked figure stabbed me with it. When I woke up, it sticking out of my gut.", "… fell out of a painting of a great battle I was staring at.", "… was forged from the drainage caught in a grease trap.", "… was a graduation present from a relative only I remember.", "… was crafted from the teeth of komodo dragons.", "… is made from the tendrils of a mage who polymorphed into a giant squid.", "… was in the stomach of a beached sea creature.", "… was hidden in the same hole I saw a squirrel burying its nuts.", "… showed up in the post. It was addressed to someone else, but it was my address.", "… was given to me by a demon. They said “You can either make a deal with me or take this weapon.”", "… kept replacing things I owned. Every time I didn’t take it, it would appear somewhere else, replacing the object that was there before.", "… was sticking out of the ground in the center of an abandoned town.", "… formed as I was pouring myself a glass of wine. I thought I was just drunk, but it was still there when I sobered.", "… crawled toward me with brittle arms, a shrill voice calling my name. It only stops if it’s on my person.", "… only manifests if I truly believe it is there.", "… bought me a drink at the pub.", "… was actually my barber’s preferred cutting tool. When they passed, they left it to me in their will.", "… was found in the shards of a broken mirror.", "… was built from pieces of several older and more powerful artifacts.", "… was spun from silk by a fey spider queen.", 
        "… condensed from the essence of an elemental plane.", "… was crafted as a gift for an imperial wedding.", "… was won in a bet with a beggar.", "… was found at the bottom of a mass grave.", "… was forged to win a divine competition.", "… was empowered by the play of a child with uncontrolled power.", "… was found tucked in the pages of a forgotten book on a library shelf.", "… was accidentally created as an apprentice artificer’s class project, intended to do something else.", "… was once a star, plucked from the sky by a dragon.", "… was infused with power by the death throes of a dying psion.", "… spontaneously manifested from pure chaos.", "… is all that was left when a failed ritual engulfed a city.", "… was crafted to defend against eldritch incursions.", "… was torn from an angel’s shadow.", "… appeared in response to a priest’s prayers.", "… was forged as repentance for a great crime by a master smith, who died in the making.", "… was carried by a traveler who fell through the cracks from another world.", "… was carved from a Tarrasque’s broken claw.", "… will be crafted by a dying hero during the End Times, and with his dying breath, sent back in time to prevent the Enemy from rising to end the world.", "… was found at the center of the Elemental Plane of Earth, on a plinth surrounded by prostrate, worshipful Crysmals and Elementals. Origins and crafters unknown.", "… was dropped by The Lady of Pain, as if by accident, on High Street in Sigil. Nobody touched it out of fear of her wrath, and it lay there, her bladed shadow lingering over it for years until the unwary adventurers blithely picked it up.", 
        "… grew from the branches of Yggdrasil, plucked and delivered by the Ratatoskr itself to a hero in a time of need.", "… was an illusionary weapon conjured to threaten an evil god’s avatar during a desperate battle between the Order and the hordes of Chaos Unbound. The all-powerful avatar’s belief in the illusion granted it a measure of his own power, so it became real.", "… fell from a dying god’s hand to earth during the creation of the world.", "… fell out of a dead Kender’s pockets. Whoops.", "… was created in another realm, the riders of a falling metal star brought it to the world. When their craft crashed, it killed most of the occupants. Their ruined metal ship kept one alive, asleep for centuries. When awakened, he bequeathed it to the party, in return for a way home, as the magic of the craft had faded beyond recovery.", "… was hawked at a pawn store and the adventurers never returned to claim their ticket.", "… was forged by a master Dwarven blacksmith during a period of blackout drunkenness. Although he has tried several times to replicate this weapon, it has never been successful.", "… was being used as a latch lock on a country farmhouse gate.", "… was being used as a prop by a local traveling troupe of bards.", "… was gifted to a mistress who then gave it away in spite after the affair ended.", "… was crafted by a mad tinkerer who was barricaded in his shop during the times of trouble.", "… really is none of your business, now go away!", "… was assembled from stolen components from the smithy", "… was traded at a flea market for a couple of pelts.", "… just appeared in my gear after checking it (the gear) at an event.", "… was given by a Nothic in exchange for bringing a wizard of some renown to see it.", "… was exposed after a flash flood eroded the ground around it.", "… was stashed at my place by a buddy who didn’t want his wife to know he got it. I can use it anytime, so it’s cool…", "… is a prototype, and I was asked to test it out and report back on how it performs in real world applications.", "… has never given me a straight answer.", "… it came into being after a wild mage screwed up an enchantment.", 
        "… was unearthed by a farmer plowing his field in preparation for planting", "… was brought back in a hounds mouth after it ran into the woods", "… was the only thing left after a massive fire destroyed old man Jenkins home.", "… was in a store window display before being recognized for what it truly was by a passing scholar.", "… was worshiped as a god by a group of Kuo-Toa.",
        "This weapon was forged in the deepest chasm of a great Volcano. Legend has it that only the Titans could have forged a blade in such a way. ", "This weapon was forge by an evil apprentice of a great blacksmith. The apprentice used it to kill his teacher, forever staining it with a dark red hue. ", "This weapon sprung into existence fully formed from the spilled blood of the legendary White Gorgon. ", "This weapon was retrieved from another Plane where it was used as a game piece by angelic beings in an eternal tournament. ", "This weapon was forged by the High Artificer of an ancient kingdom for the coronation ceremony of Prince Darek Half-Elven the Zerule. The prince's treacherous brother used it to slay Darek as he was being crowned and then fled the land with the weapon. A Royal Assassin tracked down the brother and used the weapon to kill him, thus giving it its nickname, the 'Prince Slayer'.", "This weapon was crafted with immemse precision and is still in pristine condition. The original owner was exploring a cave when a small portal opened that dropped the weapon and closed immediately after. ", 
        "The weapon was found stuck in the hide/skin of an appropriate monster (big or undead). ", "The weapon was found on the body of a low-ranking warrior (not necessarily an enemy). Although it has clearly been meticulously cleaned and polished. The warrior did not wield it in combat that you know of. ", "The weapon was discovered in a copper mine, encased in solid rock. ", "The weapon fell from the sky on a clear day. ", "The weapon has hung above the bar of the low-class Dragonslayer Inn for generations. It looks rusty and cheap, and everyone assumes it is a fake.", "The weapon was fully embedded in the heart of an anchient oak, and only discovered she the oak was toppled in a thunderstorm.", "The weapon has been used as the ceremonial symbol of office of the lamplighter guild for centuries. There are no records of it being used as a weapon. ", "The weapon was forged as a journeyman project of a blacksmith’s apprentice who immediately disappeared afterwards.", "This weapon was used as a farming tool for many years by one of a race of lower natural intelligence. ", "This weapon was used to frame an innocent man for a serial murder spree.", "This weapon is a replica of a legendary weapon that has been lost to history.", "This weapon was thrown and lost by a dying fighter in a last ditch, improvised ranged attack.", "This weapon is often mistaken by travelers for a weapon they have recently lost, misplaced, or had stolen.", "This weapon was cobbled together and slowly improved over years of adventuring by a traveling craftsman.", "This weapon is crudely/masterfully etched with events from the weapons history, though even a vague chronological order is unable to be determined.", "This weapon was owned by a sorcerer king who barely used it, mostly relying on his magic.", "This weapon has taken thousands of innocent lives, including the lives of some of the most revered heroes from history.", 
        "This weapon was forged by a man possessed by a demon.", "This weapon was found buried deep beneath the catacombs of an ancient temple, it has no known source and very well could be the last of its kind.", "After being dipped through a vat of giant's saliva, this once pristine piece has never been more slippery.", "A gift from a close relative or friend, they received it at a fair price from a man they've never seen anyone like.", "The lumber used in this piece has a texture and composure unlike much that you've seen. It's nearly as dark as night, smooth as skin, and may bend to extreme lengths but always seems to bounce back.", "This was brought to you deep in the night atop a tiny palanquin wrapped in a blanket carried by cats. they set it at your feet and refused to leave you alone until the weapon was taken.", "The smith who made the weapon spent all his wealth on crafting it, eventually becoming homeless and have the weapon stolen from him before he could find a wealthy enough buyer for it.", "The hilt has a notch for each kill made with the weapon. Although it was wielded by a great hero for many years, it only has one notch.", "The blade has been broken and reforged many times, never losing potency. It has become a mark of pride for many a smith to be able to say that they repaired this legendary weapon at least once.", "The wood in this weapon was provided willingly for the original owner, by a powerful forest god. Each following bearer has either sought out the God's blessing, or warred with nature itself.", "The secrets to steel folding were lost with the ancient elven smith who forged this blade, a relic even by their standards. They were supposedly the last inheritor to an ancient empire's secrets.", "This blade has hanged above the head of the king. He used it to slay his despotic mother, and never allows himself, or others in his company, to forget. The blade is still caked with her blood.",
        "This sword seems much to thin to be effective in a real battle. It is a relic of a more civilized era.", "This weapon has had more than its fair share of blunders. It has led to the deaths of 7 of its previous owners through a variety of mishaps. However, they were all pretty bad people. Maybe someone such as yourself will have better luck.", "This weapon was once wielded by Faris of Baare. He's not notable whatsoever.", "This weapon was formed from the compressed scales of an elder dragon.", "This weapon has a sordid and disquieting history of not staying in the place it was set down.", "This weapon has some very confusing design choices. It seems it was likely created by a nearly blind smithy.", "This weapon has some very whimsical embellishments on it such as hearts and flowers. Carved into the hilt is 'A+M Forever'.", "This weapon is lightweight and feels hollow. It appears to have been artfully crafted from the wood of an ancient black oak, purified black iron, and leather from a dire wolf of Charr.", "This weapon was found by an alchemist inside a cloud of his own making.", "A wizard failed his experiment and transformed into this weapon.", "This weapon was found in the gizzard of a massive crocodile among a plethora of large rough stones.", "This weapon has been a favorite for all who have ever wielded it. It radiated with bright light in the hands of all who have held it, but in yours, it emanates only shadow.", "This weapon was much smaller when it was originally discovered. But after years of battle, it has grown exponentially to the size it is today.", "One of two swords which were forged at a dwarven forge by a sorcerer under the cover of night, both of which hum softly and glow with blue hues when the other is near.", "An arrow which has always been successfully retrieved, whenever used.", "A sword which has slain thousands of goblins, kobolds, and other such lesser creatures, which is known to all in legend, and inspires fear in their hearts.", "A lich forged this weapon for an assassin.", "This weapon was lovingly forged by an elf over the course of three centuries.", "This weapon has been the prize of many a dragon's hoard but no mortal remembers the deeds that originally brought it fame.",
        "This weapon was forged from the armor of the fallen Hero of Angnmar Marsh by his widow.", "This weapon was merely a prop used by a traveling band of performers until they were attacked by the Blood Raiders in the wilds. A young performer used it to defend herself while praying to her gods. Her prayers were answered and the weapon became a devastating engine of war in her hands. After fending off the raiders she went on to lead a long, illustrious career as a paladin.", "This weapon was carved from the tooth of a dragon.", "The weapon was made specifically to fight dire rats, back in the days of the great plague. It's not as good at fighting anything else but rats.", "A small hammer that was meant to be a simple tool was used in a spree of murders and learned the taste of blood, now it seeks it out.", "A blunt sword that was made by a forge tired of making tools for death. It cannot hurt it's opponents but instead makes them feel shame.", "A weapon that was found washed ashore after a great battle at sea.", "A weapon carved out of the hipbone of a giant who destroyed the carver's village.", "A weapon given to a stargazer as a gift from his favorite star.", "This weapon is as ancient as time and its history can not be known through story telling, but is repeated over and over through different iterations of the owners life.", "This weapon has only been used for paid assassinations carried out by a secret society.", "This weapon was stolen from every owner who possessed it.", "It would seem each wielder has modified this weapon in some way. Carvings and varying artisan styles cover it and span multiple cultures and time periods.", "This weapon is extremely plain, except for a small inscription on the bottom that says 'feed me, Seymour'.", "Forged by the Duergar, this weapon lacks any ornamentation. All refinement is solely focused on it's devistating effectiveness.",
        "This weapon was forged by some blacksmiths of the Kingdom. The Dragonborns provided the iron, the Elves brought the wood, the Dwarfs supplied the gems and the Humans worked in the furnace.", "This weapon was found stuck in the head of a dead ghoul, the legend says that the owner is still looking for his beloved weapon.", "This weapon was made by an ancient silver dragon for their (relevant class) companion.", "The weapon was wielded by a wealthy Inquisitor. It has pinprick holes in flat of the blade to release holy water as it cuts, which can be filled up by unscrewing the pommel. However the blade is constantly leaking whenever the blade is out of it's sheathe.", "The weapons handle is branded with two hand prints which, on closer inspection, appear to be from the wielder spontaneously combusting.", "The weapon is etched with a plethora of jumbled letters: A coded message between the top brass of an army long dead. If decoded it reveals troop movements (Needless to say this information is useless.)", "This weapon is nicked and chipped from what looks to be a decade of service, but the blade is completely clean of rust and blood stains: This is the work of a Gelatinous cube!", "This weapon was wielded by the leaders of an old cult.", "This weapon was found in the body of an ancient monster that even the gods feared.", "This weapon is the physical key to a ship now haunted. Once belonging to a great pirate to hide his founded wealth it is now the only way to restore the ship to its former glory (the treasure being the ship itself). While the weapon is inserted into the keyhole a silent ghost crew works about the ship managing its sails. Without the weapon inserted it creates an illusion that it is haunted once again, great for anti-theft!", "A weapon that bleeds. It is said that it was originally made to draw blood from ones foes weakening them further even as it made a wound. Later it came into possession of a cult that was very fond of sacrificing creatures to their dark god. The weapon was used to kill the victims of the cult and after the deed was done, it would be left to lie in a pool of blood. After a century of being used by the cult the weapon was done. It was overfilled with blood. So now it bleeds blood.",
        "The weapon was used by a guardsman on a caravan and has seven camels carved/etched into it, one for each desert crossing he made.", "This weapon was reforged from the shattered weapons of three mighty heroes who slew each other in the final hours of the Battle of Dagford Keep. It was assembled to signify a new truce between the three kingdoms.", "This weapon has a permanent crack down the center from when it struck a demigod.", "This weapon was made by pixies.", "This weapon was wielded by a great hero who hunted and killed most of the world's liches centuries ago.", "This weapon was used by an ancient executioner to execute his empire's most revered enemies.", "This weapon was unexpectedly found among a street vendor's stock, and they seem just as surprised as you to find it there. Who could have left it?", "This was the weapon of a once-great legendary hero, and has been kept in a museum for ages. However, it was thrown out after the hero's deeds were found to be farcical.", "This weapon was forged from an unknown metal long ago, with skill and precision lost to the ages.", "This weapon once belonged to the queen's handmaid, and some say it had a hand in her death.", "This weapon glitters like stars in moonlight. Rumor has it that it was a gift from an otherworldly visitor.", "This throwing Hammer deals thunder damage whenever it strikes a foe. Hence its name: The 'Boom-er-Hamm'.", "Upon close inspection, these two blades were once part of a ceremonial pair of scissors from an ancient guild of haberdashers. Rumor is they unlock a secret in the old guild hall when put together on a plinth.",
        "This seemingly larger than the norm weapon belonged to an infamous Goliath warlord. Seemingly larger on the account that to the Goliath this would have been in proportion.", "This weapon was used to murder a great king. The butler did it.", "The weapon is named after a powerful weapon once wielded by a great hero of legend. Everyone seems to have different versions of who it was wielded by and what that individual used it for, though.", "The weapon has been stuck in a local monument for as long as anyone can remember.", "The weapon was delivered to a ruler of old, along with a cryptic note seemingly warning of an assassination. No such assassination occurred, however, and the ruler is long dead to illness.", "Centuries ago, an Evil blacksmith trapped a Lawful Good God in this weapon. Every time someone is killed by this weapon, it emits a loud scream, due to the will of the God to harm no one. On the hilt of this weapon there are 3 unknown symbols, the lore says they are the key to release the God from his prison.", "A weapon sneezed into creation by a Dwarven Forge god. ",
    ]
    document.getElementById("History").innerHTML = rollArray(weaponHistories)
};
function armor() {
    function armorGenerator() {

        let material = [
            [
                "Platinum", "Cold Iron", "Steel", "Bronze", "Iron", "Mithril", "Adamantine", "Silver"
            ],
            [
                "Boar", "Bear", "Cow", "Deer", "Patchwork", "Dragon"
            ]
        ]
        let armorTypes = [
            `(heavy) ${searchArray(material[0])} Splint`,
            `(heavy) ${searchArray(material[0])} Ring Mail`,
            `(heavy) ${searchArray(material[0])} Plate`,
            `(heavy) ${searchArray(material[0])} Chain Mail`,
            `(medium) ${searchArray(material[0])} Scale Mail`,
            `(medium) ${searchArray(material[1])} Hide Armor`,
            `(medium) ${searchArray(material[0])} Half Plate`,
            `(medium) ${searchArray(material[0])} Chain Shirt`,
            `(medium) ${searchArray(material[0])} Breastplate`,
            `(light) ${searchArray(material[1])} Leather Armor`,
            `(light) ${searchArray(material[1])} Studded Leather Armor`,
            `${searchArray(material[0])} Shield`,
            `${searchArray(material[1])} Hide Shield`,
        ]
        let enchantmentArray = [
            `Acolyte's ${searchArray(armorTypes)} - The bearer gains a +1 bonus to Wisdom (Religion) checks.`, `Amethyst ${searchArray(armorTypes)} - Reduces psychic damage to the bearer by 1.`, `${searchArray(armorTypes)} of the Woodlands - Treat as a +1 armor after the bearer has taken a long rest in a forest. If the bearer leaves the forest, this property becomes temporarily inert.`, `${searchArray(armorTypes)} of the Wastelands - Treat as a +1 armor after the bearer has taken a long rest in a desert. If the bearer leaves the desert, this property becomes temporarily inert.`, `Astute ${searchArray(armorTypes)} - It takes half the time to don or doff this armor than a normal armor of this type.`, `${searchArray(armorTypes)} of the North - The bearer suffers no harm in temperature as cold as -20 degrees Fahrenheit.`, `Artisan's ${searchArray(armorTypes)} - This armor is a swiss army knife of enchanted appendages that can take the form of any artisan's tools, from Alchemist's and Brewer's supplies to Weaver's and Woodcarver's tools (see p. 154 of the PHB for a complete set of artisan's tools).`, `Barbarian's ${searchArray(armorTypes)} - The bearer gains a +1 bonus to Strength (Athletics) checks.`, `Bard's ${searchArray(armorTypes)} - The bearer gains +1 to Charisma (Performance) checks.`, `Blessed ${searchArray(armorTypes)} - Whenever bearer of this item receives divine healing, they gain an additional 1d4 hit points.`, 
            `Bloodthirsty ${searchArray(armorTypes)} - The bearer can expend a hit die to turn this into a +1 armor for a number of turns equal to their roll on that die.`, `Burglar's ${searchArray(armorTypes)} - The bearer gains +1 to Dexterity (Sleight of Hand) checks.`, `${searchArray(armorTypes)} of the Underdark - Treat as a +1 armor after the bearer has taken a long rest in a cave. If the bearer leaves the cave, this property becomes temporarily inert.`, `${searchArray(armorTypes)} of the Lodestone - The wielder always knows which way is north when on the material plane. When the bearer is on a plane without cardinal directions, they are aware of that absence.`, `Cerulean ${searchArray(armorTypes)} - Reduces lightning damage to the bearer by 1.`, `Channelling ${searchArray(armorTypes)} - Once per day, the bearer may ignore the Verbal and/or Somatic components of a spell they are casting.`, `${searchArray(armorTypes)} of Charity - If the bearer donates 100gp or more to a temple of a goodly deity, this becomes a +1 armor for the next 24 hours. If they go longer than a month without making any such donations, they gain a -1 AC penalty until a suitable donation is made.`, `${searchArray(armorTypes)} of the Hearth - Treat as a +1 armor after the bearer has taken a long rest in an living urban environment. If the bearer leaves the city, this property becomes temporarily inert.`, `${searchArray(armorTypes)} of the Climber - This armor is suited with harnesses, rope, and other climbing tools readily in reach. The bearer may treat this armor as a climbing kit.`, `Concealing ${searchArray(armorTypes)} - The bearer may spend one action assembling components of this armor into a dagger. A person searching the bearer for weapons must make a DC 20 Intelligence (Investigation) check to discover this property.`, 
            `Consecrated ${searchArray(armorTypes)} - Treat this as a +1 armor when the bearer is being attacked by Undead.`, `Crystalline ${searchArray(armorTypes)} - Treat as +1 armor until the bearer takes a critical hit, at which point it loses this property forever.`, `Dancer's ${searchArray(armorTypes)} - The bearer gains a +1 bonus to Dexterity (Acrobatics) checks.`, `Dazzling ${searchArray(armorTypes)} - Once per day, the bearer may spend an action to ignite the magic in this armor, causing it to flare brilliantly. Any creature within a 10 foot radius must use their reaction to shield their eyes or be blinded until the end of their next turn.`, `Debtor's ${searchArray(armorTypes)} - The first 1 bludgeoning, piercing, or slashing damage from any source is negated. However, the total amount of damage prevented from that day accumulates as a negative modifier on death saving throws. So, if the armor prevented 5 points of damage that day, the bearer has a -5 penalty on death saving throws. The penalty resets to zero after a long rest.`, `Defensive ${searchArray(armorTypes)} - Whenever the wearer takes a dodge action, they gain +1 AC until the end of the turn.`, `Deflecting ${searchArray(armorTypes)} - The bearer may spend their reaction to gain +1 AC vs. ranged weapon attacks until the beginning of their next turn.`, `Delver's ${searchArray(armorTypes)} - While underground, the bearer of this item always knows the item's depth below the surface and the direction to the nearest staircase, ramp, or other path leading upward.`, `${searchArray(armorTypes)} of Diplomacy - Once per long rest, the bearer can gain proficiency in any language for 24 hours that they are able to correctly speak the activation phrase: "The limits of my language are the limits of my world."`, `${searchArray(armorTypes)} of the Druid - The bearer gains a +1 bonus to Intelligence (Nature) checks.`, `Ephemeral ${searchArray(armorTypes)} - Once per day, the bearer may spend their reaction to gain their Wisdom modifier to their AC until the beginning of their next turn.`, `Evasive ${searchArray(armorTypes)} - Whenever the bearer takes a dodge action, they may move an additional 10 feet.`, 
            `Fair-weather ${searchArray(armorTypes)} - The bearer may treat this as +1 armor if the bearer has more than half of their maximum hit points.`, `${searchArray(armorTypes)} of Falsehoods - The bearer gains a +1 bonus to Charisma (Deception) checks.`, `${searchArray(armorTypes)} of the Favored - Once per day, the bearer may roll a saving throw with advantage.`, `Feinting ${searchArray(armorTypes)} - Whenever the bearer uses the help action in combat, they may treat this as a +1 armor until the beginning of their next turn.`, `${searchArray(armorTypes)} of the Glade - Treat as a +1 armor after the bearer has taken a long rest in a swamp. If the bearer leaves the swamp, this property becomes temporarily inert.`, `${searchArray(armorTypes)} of the Flanked - The wearer may treat this as +1 armor if two or more enemies are adjacent to them.`, `Quick ${searchArray(armorTypes)} - The bearer gain a +1 bonus to initiative rolls`, `${searchArray(armorTypes)} of Cleansing - This armor never gets dirty and remains odorless, even in the most filthy dungeon.`, 
            `${searchArray(armorTypes)} of the Forgotten - The bearer may spend an action to attempt to ignite the old magic in this armor with a DC 13 Charisma check. If successful, treat this as a +1 armor as long as the bearer maintains concentration on this effect, maximum 10 minutes.`, `${searchArray(armorTypes)} of Fury - This plain suit of armor takes on a formidable appearance when the bearer goes into a rage. The bearer receives +1 AC when they are raging but -1 AC when they are not.`, `Garnet ${searchArray(armorTypes)} - Reduces fire damage to the bearer by 1.`, `${searchArray(armorTypes)} of Glass - The bearer may treat this as +1 armor as long as the bearer is at full health.`, `${searchArray(armorTypes)} of the Mountain - Any effect that would move the bearer against their will is reduced in distance by 5 feet.`, `${searchArray(armorTypes)} of Coercion - The bearer gains a +1 bonus to Charisma (Intimidation) checks if their armor is visible.`, `${searchArray(armorTypes)} of Harmony - Attuning to this item takes only 1 minute.`, `Heroic ${searchArray(armorTypes)} - The bearer has advantage on saving throws vs. fear.`, `Histrionic ${searchArray(armorTypes)} - the bearer gains +1 to Charisma (Performance) checks.`, `Holy ${searchArray(armorTypes)} - When the bearer of this item rolls hit dice, they can choose to re-roll them and take the second result.`, `Inquisitor's ${searchArray(armorTypes)} - The bearer gains a +1 bonus to Intelligence (Investigation) checks.`, `Inspired ${searchArray(armorTypes)} - The bearer receives their proficiency bonus in temporary hit points whenever they gain or use inspiration.`, `Invisible ${searchArray(armorTypes)} - Once worn, this armor turns invisible (although not the wearer).`, `Lightweight ${searchArray(armorTypes)} - This armor is 10% lighter than normal armor of this type. If it has a Strength requirement to use, it is reduced by 1.`, 
            `${searchArray(armorTypes)} of the Silver Tongue - The bearer gains +1 to Charisma (Persuasion) checks.`, `Mage Killer's ${searchArray(armorTypes)} - The bearer may spend their reaction to treat this as +1 armor vs. spell attacks until the beginning of their next turn.`, `Malachite ${searchArray(armorTypes)} - Reduces poison damage to the bearer by 1.`, `Masquarading ${searchArray(armorTypes)} - The bearer has advantage on skill checks involving disguise kits.`, `Medic's ${searchArray(armorTypes)} - Lined with compartments stocked with medical supplies, the bearer may treat this armor as a healer's kit.`, `Moonlit ${searchArray(armorTypes)} - The bearer may treat this as +1 armor when moonlight is shining directly on this armor.`, `Mortals' ${searchArray(armorTypes)} - At the end of a turn where the bearer failed a death saving throw, the magic within this armor will attempt to stabilize the bearer. It rolls a Wisdom (Medicine) check with a +3 modifier.`, `Mournful ${searchArray(armorTypes)} - When an ally falls unconscious in battle, the bearer gains a +1 AC bonus for the next 10 minutes. If that ally stabilizes or awakens, the bearer loses this bonus.`, `Obsidian ${searchArray(armorTypes)} - Reduces acid damage to the bearer by 1.`, `Opal ${searchArray(armorTypes)} - Reduces cold damage to the bearer by 1.`, `${searchArray(armorTypes)} of the Pious - Whenever the bearer shaves their head, treat this as a +1 armor until the end of the day. They must wait a week until they have long enough hair to re-enact this ritual.`, `${searchArray(armorTypes)} of the Plains - Treat as a +1 armor after the bearer has taken a long rest in a grassland. If the bearer leaves the grassland, this property becomes temporarily inert.`, `Preacher's ${searchArray(armorTypes)} - The bearer may extend the range of their Channel Divinity by 5 feet.`, `${searchArray(armorTypes)} of the Crags - Treat as a +1 armor after the bearer has taken a long rest in the mountains. If the bearer leaves the mountain, this property becomes temporarily inert.`, `Primeval ${searchArray(armorTypes)} - Treat as a +1 armor after the bearer has taken a long rest in a jungle. If the bearer leaves the jungle, this property becomes temporarily inert.`, `Reflexive ${searchArray(armorTypes)} - If the bearer is first in initiative order, treat this as +1 armor for 1 minute.`, `${searchArray(armorTypes)} of the Renaissance - Once per day, the bearer may gain +1 to any ability check.`,
            `Resonant ${searchArray(armorTypes)} - The bearer can spend an action and 1 ki point to treat this as +1 armor for 1 minute.`, `${searchArray(armorTypes)} of Righteousness - Treat this as +1 armor during the day when attuned to a good aligned character.`, `Regal ${searchArray(armorTypes)} - This armor is richly decorated and fashionable. Although it retains a hint of the ruggedness of a military garment, it could function as well in a ballroom as the battlefield. To the outside observer, you appear to be keeping an Aristocratic lifestyle expense.`, `Runic ${searchArray(armorTypes)} - Whenever bearer casts a spell of first level or higher, treat this as +1 armor until the beginning of their next turn.`, `Sacred ${searchArray(armorTypes)} - The bearer may increase their Lay on Hands hit point pool by 5.`, `${searchArray(armorTypes)} of Acumen - The bearer gains +1 to Wisdom (Insight) checks.`, `Sage's ${searchArray(armorTypes)} - The bearer gains a +1 bonus to Intelligence (History) checks.`, `Sailor's ${searchArray(armorTypes)} - Treat as a +1 armor after the bearer has taken a long rest on the high seas. If the bearer leaves the ocean, this property becomes temporarily inert.`, `${searchArray(armorTypes)} of the Scribe - This armor unfolds to reveal animated appendages that are equipped with writing implements, magnifying glasses, and book stands. The armor aids the bearer in transcription tasks: it knows 3 languages of the DM's choice and halves the amount of time it takes the bearer to copy any text, including spells into spellbooks.`, `${searchArray(armorTypes)} of Shade - The bearer suffers no harm in temperatures as high as 120 degrees Fahrenheit.`, 
            `${searchArray(armorTypes)} of Shadows - Treat as a +1 armor when in dim light.`, `Shepherd's ${searchArray(armorTypes)} - The bearer gains a +1 bonus to (Wisdom) Animal Handling checks.`, `Shifting ${searchArray(armorTypes)} - The bearer may spend an action to change minor aspects of the physical appearance of this item.`, `${searchArray(armorTypes)} of the Night - If this armor imposed disadvantage to stealth, it no longer does. Otherwise, the bearer gains a +1 bonus to Dexterity (Stealth) checks.`, `${searchArray(armorTypes)} of the Sun - The bearer may treat this as +1 armor when in direct sunlight.`, `Spiked ${searchArray(armorTypes)} - Whenever a creature begins their turn grappling or being grappled by the bearer, they take 1d4 piercing damage.`, `Spiritual ${searchArray(armorTypes)} - This armor is naught but a prayer written on a scrap of vellum, decorated with religious motifs of a particular god. Once per day, the bearer may spend 1 minute to read the prayer out loud, and at the end this armor will manifest and encase the bearer. The armor disappears if you act in any way that is not in accordance to the god's teachings.`, `Subtle ${searchArray(armorTypes)} - The bearer gains proficiency in Thieves' Cant.`, `Surgeon's ${searchArray(armorTypes)} - The bearer gains a +1 bonus to Wisdom (Medicine) checks.`, `Tenacious ${searchArray(armorTypes)} - When the bearer takes a long rest, they gain back one additional hit die.`, `${searchArray(armorTypes)} of the Tracker - The bearer gains a +1 to Wisdom (Survival) checks.`, `Trusty ${searchArray(armorTypes)} - Treat this as +1 armor if the bearer has half their maximum hit points or less.`, `Turquoise ${searchArray(armorTypes)} - Reduces thunder damage to the bearer by 1.`, `${searchArray(armorTypes)} of Twilight - Within 1 hour before or after the rising and setting of the sun, or during a solar eclipse, the armor comes alive with magic and the bearer may treat this as +1 armor.`, `${searchArray(armorTypes)} of the Undertaker - Once deceased, the body wearing this armor cannot be animated or raised from the dead.`, `Unyielding ${searchArray(armorTypes)} - The bearer may treat this as +1 armor if they have taken damage since the beginning of their last turn. This effect ends at the beginning of their next turn.`, `Vanguard ${searchArray(armorTypes)} - The bearer may spend their reaction to gain a +1 AC bonus vs. melee weapon attacks until the beginning of their next turn.`, 
            `Veiled ${searchArray(armorTypes)} - The wearer gains a +1 bonus to Dexterity (Stealth) checks when taking a hide action.`, `Victorious ${searchArray(armorTypes)} - Whenever the bearer kills a creature while wearing this amror, they gain temporary hit points equal to the creature's CR.`, `Vigilant ${searchArray(armorTypes)} - The bearer gains +2 to their Passive Perception.`, `Vile ${searchArray(armorTypes)} - Treat this as +1 armor at night when attuned to an evil aligned character.`, `${searchArray(armorTypes)} of Violence - The bearer may choose to treat the heavy metal gauntlets of this armor as a Mace.`, `${searchArray(armorTypes)} of the Warchief - The bearer can use an action to amplify their voice so that it clearly carries for up to 300 feet.`, `Warded ${searchArray(armorTypes)} - The wearer cannot be possessed while wearing this armor.`, `Watcher's ${searchArray(armorTypes)} - Treat as +1 armor when the bearer is surprised.`, `${searchArray(armorTypes)} of the Sea - This armor floats. Its bearer has advantage on Strength (Athletics) checks to swim.`, `Winged ${searchArray(armorTypes)} - The bearer gains +5 speed.`, `Wizard's ${searchArray(armorTypes)} - The bearer gains a +1 to Intelligence (Arcana) checks.`, `Zen ${searchArray(armorTypes)} - Treat this as +1 armor for one minute after meditating with it for one minute.`, `Zircon ${searchArray(armorTypes)} - Reduces force damage to the bearer by 1.`, `Abyssal ${searchArray(armorTypes)} - When on the plane of the Abyss, the bearer has advantage on saving throws against Abyssal Corruption. (DMG p. 62)`, `Alarming ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Alarm spell (1st level).`, 
            `${searchArray(armorTypes)} of Arborea - When on the plane of Arborea, the bearer has advantage on saving throws against the effects of Intense Yearning. (DMG p. 61)`, `${searchArray(armorTypes)} of Arcadia - When on the plane of Arcardia, the bearer is unaffected by Planar Vitality (DMG p. 67)`, `${searchArray(armorTypes)} of the Astral Sea - When travelling the Astral Sea, it takes half the number of hours to locate a Color Pool to a specific plane. You have advantage on saving throws vs. the effects of Psychic Wind (DMG p. 47-48)`, `Beastial ${searchArray(armorTypes)} - When on the plane of The Beastlands, the bearer has advantage on saving throws vs. Beast Transformation (DMG p. 60)`, `Beastspeaker's ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Speak with Animals spell (1st level).`, `Benedictine ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Healing Word spell (1st level).`, `Blasted ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Fire Bolt spell (1st level).`, `${searchArray(armorTypes)} of Boldness - Contains 1d4 unreplenishable charges of the Heroism spell (1st level).`, `${searchArray(armorTypes)} of Bounty - Contains 1d4 unreplenishable charges of the Goodberry spell (1st level).`, `${searchArray(armorTypes)} of Bytopia - When on the plane of Bytopia, the bearer has advantage on saving throws against Pervasive Goodwill. (DMG p. 59-60)`, `${searchArray(armorTypes)} of Carceri - When on the plane of Carceri, the bearer knows the direction to the closest secret exit from this prison plane. (DMG p. 63)`, `${searchArray(armorTypes)} of Cartography - On its own volition, the item records a map of the environments that the bearer is exploring, and can magically project it for the bearer to see.`, `${searchArray(armorTypes)} of Chills - Contains 1d4 unreplenishable charges of the Ray of Frost spell (1st level).`, `${searchArray(armorTypes)} of Gears - When on the plane of Mechanus, the bearer has advantage on saving throws against Imposing Order (DMG p. 66)`, `Cloy ${searchArray(armorTypes)} - The bearer may cast Friends once per day.`,
            `Compassionate ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Cure Wounds spell (1st level).`, `Concordant ${searchArray(armorTypes)} - The bearer has advantage on saving throws vs. Psychic Dissonance when travelling the Outer Planes. (DMG p. 59)`, `Conjurer's ${searchArray(armorTypes)} - The bearer may cast Prestidigitation once per day.`, `Corrosive ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Acid Splash spell (1st level).`, `${searchArray(armorTypes)} of Vermin - The crawling things of the earth, such as insects, snakes, and vermin, are attracted to this item. When placed on the ground, such creatures will scurry toward the item like moths drawn to the flame.`, `Drunkard's ${searchArray(armorTypes)} - The bearer always knows the direction to the closest alcoholic beverage.`, `Elysian ${searchArray(armorTypes)} - When on the plane of Elysium, the bearer has advantage on saving throws against the effects of Overwhelming Joy (DMG p. 60)`, `Etherbound ${searchArray(armorTypes)} - The bearer can see creatures in the Border Ethereal that overlap with their plane as clearly as if they were fully in the bearer's plane. Such creatures appear as apparitions or ghosts.`, `Exalting ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Bless spell (1st level).`, `Expeditious ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Expeditious Retreat spell.`, `${searchArray(armorTypes)} of Tongues - Contains 1d4 unreplenishable charges of the Comprehend Languages spell.`, `Feathered ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Feather Fall spell (1st level).`, 
            `${searchArray(armorTypes)} of the Fey - The bearer knows the general direction to the closest Fey Crossing within a 60 mile radius. (DMG p. 50)`, `Forgiven ${searchArray(armorTypes)} - When on the plane of Mount Celestia, the bearer of this item can receive the benefits of Blessed Beneficence regardless of their alignment.`, `Fortune Teller's ${searchArray(armorTypes)} - Every time you are hit by a monster, you glimpse a random image of its future or past.`, `Friendly ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Animal Friendship spell (1st level).`, `${searchArray(armorTypes)} of Gehenna - When on the plane of Gehenna, the bearer has advantage on saving throws against Cruel Hindrance. (DMG p. 63)`, `Gracious ${searchArray(armorTypes)} - The bearer may cast Spare the Dying once per day.`, `Hadean ${searchArray(armorTypes)} - When on the plane of Hades, the bearer has advantage on saving throws against Vile Transformation. (DMG p. 63)`, `Healing ${searchArray(armorTypes)} - This item contains 4 weak healing nodes. As an action, a character can use one node to heal 1d4 hit points at touch range. The item regains 1d4 charges at sunrise.`, `${searchArray(armorTypes)} of the Nine Hells - When in the Nine Hells, the bearer has advantage on saving throws against Pervasive Evil. (DMG p. 64)`, `Desperate ${searchArray(armorTypes)} - The bearer has advantage on perception checks when searching for items long lost in the the Swamp of Oblivion on the Plane of Earth. (DMG p. 54)`, `Leaping ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Jump spell (1st level).`,
             `Liar's ${searchArray(armorTypes)} - The bearer cannot be magically compelled to speak the truth while wearing this armour.`, `${searchArray(armorTypes)} of Limbo - When on the plane of Limbo, the bearer has advantage to Intelligence checks to alter or move non-magical objects within the plane. (DMG p. 61-62)`, `${searchArray(armorTypes)} of Locating - Once attuned, the bearer always knows the exact location of this item`, `${searchArray(armorTypes)} of Malediction - Contains 1d4 unreplenishable charges of the Bane spell(1st level).`, `${searchArray(armorTypes)} of Manipulation - The bearer may cast Mage Hand once per day.`, `Master's ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Unseen Servant spell (1st level).`, `${searchArray(armorTypes)} of the Maverick - The bearer has a +1 bonus to any skill check involving gambling and games of chance (Insight, Sleight of Hand, Investigation, etc).`, `${searchArray(armorTypes)} of Messages - The bearer may cast Message once per day.`, `${searchArray(armorTypes)} of Falling Stars - Contains 1 unreplenishable charge of Scorching Ray cast at 2nd level.`, `${searchArray(armorTypes)} of Miracles - The bearer may cast Thaumaturgy once per day.`, `${searchArray(armorTypes)} of Mockery - The bearer may cast Vicious Mockery once per day.`,
             `${searchArray(armorTypes)} of Nature - Contains 1d4 unreplenishable charges of the Locate Animals or Plants spell (1st level).`, `Neutralizing ${searchArray(armorTypes)} - Contains 1d4 unreplenishable charges of the Protection from Good and Evil spell (1st level).`, `${searchArray(armorTypes)} of Nourishment - The bearer rarely feels hungry, and only needs to consume one-fifth the usual amount of food.`, `${searchArray(armorTypes)} of Pandemonium - When on the plane of Pandemonium, the bearer has advantage on saving throws against the Mad Winds. (DMG p. 62)`, `Projecting ${searchArray(armorTypes)} - The bearer can send messages mentally to willing characters within 30 feet. This communication is one-way only.`, `Protective ${searchArray(armorTypes)} - The bearer may cast Blade Ward once per day.`, `${searchArray(armorTypes)} of Revelation - Contains 1d4 unreplenishable charges of the Detect Magic spell (1st level).`, `Riutal ${searchArray(armorTypes)} - Whenever the bearer is casting a spell as a ritual, they have advantage to maintain concentration during the ritual.`, `${searchArray(armorTypes)} of the Sea - Treat as a +1 weapon after the bearer has taken a long rest at sea. If the bearer steps on dry land, this property becomes temporarily inert.`, `${searchArray(armorTypes)} of Secrets - Contains 1d4 unreplenishable charges of the Illusory Script spell (1st level).`, `${searchArray(armorTypes)} of the Shadowfell - The bearer knows the general direction to the closest Shadow Crossing within a 60 mile radius. They have advantage on saving throws vs. Shadowfell Dispair (DMG p. 51-52)`,
              `Shielding ${searchArray(armorTypes)} - This item contains 1d4 unreplenishable charges of the Shield spell.`, `Smith's ${searchArray(armorTypes)} - The bearer may cast Mending once per day.`, `${searchArray(armorTypes)} of Lights - The bearer may cast Dancing Lights once per day.`, `${searchArray(armorTypes)} of Strides - Contains 1d4 unreplenishable charges of the Longstrider spell (1st level).`, `Translucent ${searchArray(armorTypes)} - The bearer gains an extra level one spell slot, which recovers only after a full moon rises.`, `Trickster's ${searchArray(armorTypes)} - If the bearer uses no movement this turn, they may use a bonus action activate the magic in this armor to record their action. At the beginning of their next turn, an intangible illusory replica of themselves appears within 5 ft., repeatedly doing that action. It will continue to do this for 1 minute or until dispelled. The bearer may not use this magic again until they take a long rest.`, `${searchArray(armorTypes)} of Truth - The bearer may cast True Strike once per day.`, 
             `Verdant ${searchArray(armorTypes)} - The bearer may cast Druidcraft once per day.`, `${searchArray(armorTypes)} of the Labyrinth Wind - When in the Plane of Air, the bearer can navigate the Labyrinth Wind intuitively, and knows the path to the nearest Earth Mote within 60 miles.`, `${searchArray(armorTypes)} of Ysgard - When on the plane of Ysgard, the bearer is unaffected by Immortal Wrath. (DMG p. 61)`, `Thunderous ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Shatter cast at 2nd level.`, `Chained ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Hold Person cast at 2nd level.`, `Spider's ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Web cast at 2nd level.`, `Heliacal ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Flaming Sphere cast at 2nd level.`, `Crippling ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Ray of Enfeeblement cast at 2nd level.`, `Lunar ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Moonbeam cast at 2nd level.`, `Fatespinner's ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Augury cast at 2nd level.`, `Rooting ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Entanglement cast at 2nd level.`, `Mirrored ${searchArray(armorTypes)} - Contains 1 unreplenishable charge of Mirror Image cast at 2nd level.`, 
             `Vulpine ${searchArray(armorTypes)} - Characters trying to track the bearer have a disadvantage on their skill checks.`, `${searchArray(armorTypes)} of the Depths - Treat as a +1 armor when completely submerged in water.`, `Comforting ${searchArray(armorTypes)} - Treat as a +1 armor if the bearer has any levels of exhaustion.`, `Brawler's ${searchArray(armorTypes)} - Whenever a bearer makes an attack with an improvised weapon, treat as a +1 armor until the beginning of the bearer's next turn.`, `${searchArray(armorTypes)} of the Eagle - The bearer can clearly see twice as far and gains advantage on Wisdom (perception) checks that use sight.`, `${searchArray(armorTypes)} of the Wolf - The bearer can detect and distinguish scents like a wolf and gains advantage on Wisdom (Perception) checks that use smell.`, `${searchArray(armorTypes)} of the Bat - The bearer can hear a pin drop in a crowded room and gains advantage on Wisdom (Perception) checks that use hearing.`, `${searchArray(armorTypes)} of Darkness - Contains 1 unreplenishable charge of Darkness cast at 2nd level.`, `Sober ${searchArray(armorTypes)} - The bearer cannot become intoxicated while this armor is donned.`,
        ]
        let optionalProps = [
            "Named Armor – The armor is uniquely named. It may whisper this name when donned, or be engraved with it.", "Fame or Infamy – The armor is well known for its relationship to a particular historical figure or event.", "Odd Noise – The material of the armor vibrates faintly to emit a particular hum, drone, buzz or squeal.", "Odd Smell – The material of the armor emits an odd smell, which can’t be masked. May be pleasant or unpleasant.", "Odd Shape – The armor is particularly long, stout, broad, slim, or otherwise identifiably unorthodoxly shaped. Were it not magical, it would be impractical to use.", "Odd Colour – The materials of the armor are uncommon colours, or change colours under certain conditions.", "Faint Aura – The material of the armor emits a faint, coloured glow. It may leave tracers, flicker, appear as a flame or float upwards.", "Gemstones – The armor is inset with a particularly large gemstone, or a variety of smaller gemstones.", "Detailing – The armor is gilded, engraved, sculpted, or otherwise decorated in a fantastic way.", "Aspected – The armor amplifies a quality of the bearer’s personality, such as bravery, piousness, or jealousy.",
        ]
        let runes = [
            "Rune of Confusion - Upon taking a hit, the wearer can cast Confusing Rebuke. The attacker must make a DC 14 CHA check or become confused ", "Rune of Perth - The bearer of this rune can cast Protection from Good and Evil once per day", "Rune of Ehwaz - The bearer of this rune can cast Bless once per day ", "Rune of Helium - One per long rest, as a bonus action you can use the rune to make your voice squeaky like that of a mouse. You have advantage on performance checks and intimidation checks against large or larger creatures that are capable of hearing and understanding you", "Rune of Echoes - Once a day, the armour can perfectly replicate a noise it has heard that day, acting as a distraction for example", "Rune of Leaden Steps - Adds 10 pounds of weight to the weapon that makes a successful attack against the bearer", "Rune of the Elk - Grants advantage to the nature skill", "Rune of Defence - Boost Once per day, the bearer of the rune can take an attack roll that hits the AC of the armour and ignore the attack.", "Rune of Reflexes - Once per long rest, use advantage on initiative rolls", "Rune of Vanishing - The last rune to be carved into the item. Upon completion, all runes carved into the item disappear and are only visible to the creator of the item. No additional runes can be added", "Rune of Life - This is a greater rune of enchantment and will prevent additional runes being added onto the item. It grants the wielder immortality. They will not age, get sick or be harmed by poison. Normal damage and weapons will still kill them", "Rune of Transformation - As a bonus action, on a successful Intelligence skill check, the wielder may cause the armour to turn into any other armour they are proficient with. The armour reverts into its true form after one hour ", "Rune of Vampirism - Every time you are hit, roll a D4. On a 4, you regain an amount of HP equal to half the inflicted damage", 
            "Rune of Melody - In combat, the armour emits a soft, musical humming. With practise, you could use this armour as an instrument", "Rune of Speed - Whilst wielding the armour, you can use the Dash action as a bonus action on each of your turns", "Rune of Arcane Storage - You may store up to 5 levels' worth of spell slots within the rune. Doing so requires 10 minutes per level, consumes the spell slot and counts as a ritual. If you are touching the rune while casting a spell, you may choose to consume an amount of stored levels equal to the level of the spell instead of your own spell slots", "Rune of Truth - When a creature speaks a deliberate lie within 15 feet of the rune, the armour vibrates slightly for a few seconds. Detecting this vibration is no challenge, unless the wielder isn't paying attention to the armour’s response", "Rune of Aquan Blessing - Wielder's base speed increases by 10 feet anytime it is raining, or they are standing at least ankle deep in water", "Rune of Remembrance - The wearer of this armour has perfect recall of everything since meeting this rune. The wearer may also make a DC8 Intelligence check to remember information from previous wielders of the rune, but the knowledge of the wearer can also be remembered by other wielders for the same DC check", "Rune of Wild Magic On a critical failure attack against the bearer, the attack triggers a Wild Magic Surge. Effects that require targeting are directed at the creature closest to the wielder", "Rune of the Stranger - Once per long rest, if you invoke this ability, every creature in the battle must succeed a DC 10 WIS save or forget your alliance for one round - Including the bearer",
             "Rune of the Carousel - An attack against the wielder of the armour that missed the wielders AC by 3 or less causes the attacker to spin uncontrollably at a high speed for 3 rounds of combat. The affected must pass a DC 7 CON check or lose their turn as they try to regain their bearings", "Rune of the Bear - Gains advantages to athletic skill checks", "Rune of the Goose - This rune allows for the wearer to walk on water. If the wearer runs, the rune glows and the wearer can glide", "Rune of Enlarging - When you touch this rune as a bonus action, you increase the size of the armour, causing the AC of the item to increase by 3. This transformation lasts for one minute, or if you dismiss the effect.", "Rune of Refraction - The armour refracts light strangely when in direct sunlight, causing everyone but the wielder to have trouble discerning the actual location, causing disadvantage against melee and ranged attacks", "Rune of Sundering - The armour grants a plus 2 to AC when attacked with heavy- or two-handed weapons", "Rune of Returning - When the armour is lost or stolen, it will always return to its true owners’ side after one long rest", "Rune of the Lion - Grants advantage to the intimidation skill", "Rune of the Squirrel - Grants advantage to the acrobatics skill", 
            "Rune of Invisibility - Makes the armour invisible to all, except those designated by the rune-maker and the true owner. The does not grant full invisibility to the wearer, just to the armour", "Rune of Screaming - This rune grants the wielder the ability to cast the cantrip Thaumaturgy", "Rune of the Chameleon - Grants advantage to the stealth skill", "Rune of Mirrors - Once per short rest, as a bonus action, the user can break this armour into two identical copies of the original. If either copy leaves the possession of the character who broke the armour in two, the copy disappears, and the effect is ended", "Rune of the Manticore - The armour inscribed with the rune grows 1d10 spikes each day, granting advantage against grapples. If removed, the spikes can be thrown as daggers with the range of a longbow or used as ammunition for a ranged weapon. Each day, the spikes vanish if not removed. The spikes are efficient for impaling or piercing hard surfaces like rock.", "Rune of the Cockroach - Grants advantage to the survival skill", "Rune of Return - Once etched on the armour, it allows the user to summon the armour on to a worn and equipped status if within 10 feet", "Rune of Unjo - The bearer of this run can stave off one level of exhaustion", "Rune of the Open Door - The bearer gets advantage on strength checks against locked doors", "Rune of the Phoenix Feather - The is a greater rune. As a bonus action, the wearer can cause the armour to turn into flames granting immunity to fire attacks and deals 1 fire damage per round to all players and creatures in 15 foot unless have fire resistance. This item magically reforms if it is ever destroyed",
             "Rune of the Spider - Grants Advantage to sleight of hand skills", "Rune of Death's Tongue - After a successful attack against the wearer, the wearer can cause hungry, flesh eating worms to spontaneously appear in wounds of the attacking enemy. As they burrow into the wound, they prevent regeneration from the damage dealt, and deal 1d6-4 poison damage for 1d10 subsequent rounds. If they have no wounds, the worms cannot be summoned", "Rune of the Bull - Grants the wearer advantage on attempts to shove large or smaller creatures. Shove attempts send the target back 10 feet", "Rune of the Eagle - Grants advantage to the perception skill", "Rune of Green Thumbs - If the armour is planted in soul, a 30-foot-tall tree will sprout out of it in 1d4 days. The tree has 1d12 good berries on the branches. The armour is destroyed in the process", "Rune of Snail Shell - This armour is unbreakable by non-magical means, however, becomes so heavy that when equipped is becomes so dense and heavy that it eliminates all DEX bonuses to their AC ", "Rune of Heaven's Fan - The armour can cause gusts of wind, to extinguish fires and turn the ambient temperature to tolerable levels regardless of the previous state. Twice a day, the wielder can activate the rune and create a 40-foot-long, 5-foot-wide blast of downwards wind that forces everyone hit to make a STR save or be knocked prone. This ability will knock all projectiles and flying creatures out of the air and can be used as a reaction to projectile attack", "Rune of the Mantis - Granted advantage to the religion skill", "Rune of Orcus - Any humanoid creature of size large or smaller killed by the wielder of this rune when it is activated (as a bonus action) rises as a zombie under your control for 20 minutes. After 20 minutes, the zombie collapses and turns back into a corpse", "Rune of the Lobster - Grants advantage to the medicine skill", 
             "Rune of the Peacock - Grants advantage to the performance skill", "Rune of Ice - Grants ice resistance to the armour and it's wielder", "Rune of Fire - Grants fire resistance to the armour and it's wielder", "Rune of Spirit - This rune allows the user to cast the 3rd level spell Spirit Guardians. 3 spirits (fey, angelic or fiend) appear around you to a distance of 15 feet. You can designate any number of creatures to be safe from their affects. Any affected creature's speed is halved in the area, and when the creature enters the area for the first time on a turn or starts its turn there, it must make a WIS saving throw. On a failed save, the creature takes 3d8 radiant or necrotic damage (depending on the form of the spirits). On a successful save, the creature takes half damage", "Rune of the Raven - Grants advantage to the arcana skill", "Rune of the Fire's Walk - On a successful attack against the wielder, the armour releases a cloud of thick smoke that visually obscures an area of 10 ft radius. All those hit make a CON save as their lungs fill up, on a success they expend a bonus action to cough the smoke out, but on a failure, it takes the whole turn", "Rune of the Journey - When an attacker fails a melee attack against the wielder, the attacker makes a WIS save otherwise they spend their next move returning the way they came. If this is impossible, they must take a logical alternative", 
             "Rune of the Elephant - Grants advantage to the history skill", "Rune of the Snake - Grants advantage to the deception skill", "Rune of Bombardment - You can activate this rune with a power word of your choice. One turn after activation, the armour will produce a 3rd level Fireball spell, centred on itself. This destroys the armour", "Rune of the Owl - Grants advantage to the Insight skill", "Rune of the Feline Grants advantage to the persuasion skill", "Rune of Alarm - This rune will begin to glow or emit an audible alarm when a certain type of creature (dragon-kind, undead, drow, demon etc) approaches within 150 feet. The type of creature will can be changed once per day", `Rune of the ${searchArray(["Dawn","Zenith","Dusk","Midnight"])} - Shines During the corresponding time of day/night, last two hours, the armour shines as under the effect of the Light cantrip, and grants 1d10 radiant damage to successful melee attacks.`, "Rune of the Crow - Grants advantage to the investigation skill", "Rune of Hagalaz - The bearer of this rune can cast Thunderwave once per day", "Rune of the Immanence - The wielder may cast Misty Step once per day. With the proper material components, the wielder may cast Plane Shift once per day", "Rune of Time's Shadow - Upon activation, the rune can record a shadow of the wielders action that lasts for 1 minute. This shadow has physical form, all the stats of the wearer of the armour and 1HP. This shadow can be activated anytime within a day of being recorded", "Rune of the Primordial - Wielder can speak Primordial and has advantage on Charisma checks on creatures that understand it", 
             "Rune of Alliance's Might - Upon activation, once per day the wielder gains 5 temporary hit points per ally within 60 ft of the wielder", "Rune of Possession - Unless the armour is freely given or taken from its owner upon their death, this rune refuses to be attuned to another person. In addition, non-owners take -4 penalty to AC if they attempt to wear the armour in combat", "Rune of Gifu - The wielder of this armour can freely teleport the armour into the hands or into the equipped position of another creature they can see within 120 feet. This method of transference does not harm the recipient but will displace any other armour or item they are wearing. This ability has three charges per day and regains one charge per day", "Rune of Bloodlust - This grants the wielder the ability to enter a rage once per long rest, with the features of a level 3 barbarian. If you have a barbarian level greater than 3, you may use your own rage features whilst entering this rage", `Rune of ${searchArray(["Celestial","Fey","Fiend","Elemental","Undead"])} Slaying - This armour shines when a creaute of the appropriate type is within 30 feet. The wielder is protected from those creatures as by the Protection from Evil and Good spell`, "Rune of Terran Blessing - The wielder cannot be knocked prone by any environmental hazards", "Rune of the Cliff - Allows the casting of Featherfall on command", "Rune of Foresight - You can use the weapon once to cast Augury as a 2nd level spell per short rest. Wisdom is your spell casting ability for this", "Rune of Ignan Blessing - Natural flames in the area around the wielder glow brighter and hotter, shedding an extra 10 ft of light and dealing an extra 1d4 damage where applicable", "Rune of the Duelist - When targeted by an enemy melee attack, you may impose disadvantage on the attack as a reaction. If the melee attack misses, you may attack the enemy who just attacked you", "Rune of Bees - Once per long or short rest, this rune allows the user to summon a swarm of bees to deal 2d4+2 piercing or poison damage as a bonus action. The user also gains a strange fondness for flowers", "Rune of Stone - This makes shields unbreakable in combat, granting +4 AC", "Rune of the Dog - Grants advantage to the animal handling skill", "Rune of the Swordbreaker - If the wielder is attacked with a melee weapon and the attack is a critical failure, the attackers weapon shatters", 
             "Rune of Vaporization - Once a day, you can submerge the armour into water and vaporize 1d20 cubic feet of water", "Rune of Poison Detection - If the armour is dipped into poisoned food, it changes colour. The colours return to normal once the poison is removed from the weapon", "Rune of the Worg - This rune allows the wearer to eat or consume any non-magical item as food and gain 1d4 HP per item", "Rune of the Gryphon - When this rune is activated, your jump distance is multiplied by 10. If you manage to hit an enemy while falling, you ignore all falling damage. If you flap your arms, you might fly", "Rune of the Firebreather - When activated, the rune belches forth a ten-foot line of fine. All creatures in the line must make a DEX save or take 1d6 Fire damage", "Rune of the Kebab - Once a day, this armour can be taken off and, by using a power word, fills the armour with fresh, delicious and hot kebabs. This will feed 1d12+6 people for a day", "Rune of Sulfer Hexafluoride - Once in a long rest as a bonus action, you can activate this rune and make your voice deeper, like that of a dragon. You have an advantage on performance checks and intimidation checks against Medium or Smaller Creatures that are capable of hearing and understanding you", "Rune of Safety - Whilst wearing this armour, the wielder has advantages against all- natural hazards and trap saving rolls", "Rune of the Wind - This is a greater rune of enchantment. This rune doubles the speed and jump distance of the wearer, and once a day can double the speed of the allies as well. The wearer can cast three of the following spells a day; Gust of Wind, Wind Wall, Wind Walk (once). You can also use the Disengage or Dash action as a Bonus action on your turn once per short rest. Once per short or long rest you can use a bonus action to regain hit points equal to 1d10+ your DEX modifier", 
             "Rune of Absorbing - Once per day, you can spend a minute to change the material of the armour to any material that it is in contact with. This may affect the armour class of the weapon. This change is permanent, or until you repeat this action", "Rune of the Impersonal - Once per turn, whilst in melee combat whilst wearing this armour you can teleport to the opposite side of the creature", "Rune of Diplomacy - This rune allows the user to cast comprehend languages 3 times per short rest. This rune also gives you proficiency in the persuasion skill, however, due to the rune's desire for peace, the armour does not work against good aligned creatures", "Rune of Auran Blessing - Wielder gains advantage on Animal Handling checks against creatures with a natural flight speed", "Rune of True Strike - Every time you attack, roll a d10. On a 10, you gain advantage on your attack roll and any successful hit automatically deals maximum damage", "Rune of Fehu - The wearer of this armour may activate this rune once per day for the duration of one encounter, causing the armour to burst into golden flames that cause all attacks against the wearer to have disadvantage. Any successful attacks on the armour causes 2d10 gp to fall from where it was hit", "Rune of the Inhabitancy - The wielder gains the effect of a short rest on a critical failure attack made against the wearer"

        ]
        let chance = rollDice(100)
        if (chance < 50) {
            return searchArray(enchantmentArray);
        } else if (chance < 75) {
            return searchArray(enchantmentArray) + ' Special effect: ' + searchArray(optionalProps);
        } else {
            return searchArray(enchantmentArray) + ' Also, the armor piece is covered in a beautiful runic inscription: ' + searchArray(runes);
        }
    }
    document.getElementById("Armor").innerHTML = armorGenerator()
};
function findScabbard() {
    let scabbards = [
        "Scabbard of Sharpening - A blade drawn from this metal scabbard is magically honed to razor sharpness, doing +1 extra damage when it strikes an opponent. The first time you miss, however, the enchantment wears off as the blade is dulled by your opponent's shield or armor or it hits the stone floor or whatever. (To get the bonus again, you have to sheathe and draw it again. The damage bonus does not stack with multiple drawings, it can only be +1, and only on one weapon at a time.) Every time the blade is sheathed or drawn, there's the distinct, and rather loud, sound of metal being sharpened.", "Snakeskin Sheath (Requires attunement) - This sheath is made of python skin. If you draw your sword and throw the sheath on the ground, it functions as per the magic item Staff of the Python.", "Mace Miter (Requires attunement) - This ornately decorated cone-shaped hat was once worn by a long-dead bishop. It still makes a fine head covering, if you want to wear it that way. But even better, you can turn it upside down, lash it to your belt, and carry your mace around in it. Whether used as a hat or a mace holder, the miter functions as a Holy Symbol +1.", "Flamesheath - This 'sheath' is not made of leather or metal, but flame! Well, sort of. It's just a permanent illusion cast on a normal leather sheath. But it looks pretty awesome. A weapon drawn from this sheath does an extra 1D4 fire damage the first time it's used after being drawn; hit or miss, the flames die out until it's resheathed and drawn again. The sheath itself can be used as a light source, functioning as the Light cantrip (but looking more like a torch). To hold the scabbard aloft, you'll have to have your weapon sheathed. Note it can't be turned on or off; the only way to hide the flames is to stick the sheath into a sack or other opaque object.", "Assassin's Sheath - This small leather sheath would appear to hold nothing larger than a tiny folding knife, but any weapon up to a great sword can be sheathed in it. The size of the weapon is revealed only when it is drawn from the scabbard, whether by the wearer or a wary guard. Unlike most scabbards, to draw a weapon from this one requires the Use an Object action. (The weapon's actual size can be revealed by Truesight.)",
        "Living Quiver (Requires attunement) - Prized among Elves, Rangers, and Druids, this quiver is not made but grown, of meticulously cultivated living plants. It requires daily watering and must have a long rest in sunshine at least once a week, or it withers and dies. Once bonded with the quiver, it responds to your thought. Just reach a hand back and it will be filled with the arrow, javelin, or dart you desired. After every long rest in the sunshine, the quiver 'grows' 1D4 arrows (or 1D8 darts or one javelin), up to a maximum of 20 arrows, 40 darts, or 5 javelins. They look roughly made of primitive materials, almost like something a child would make, but they fly true and are considered magical for the purposes of enemy immunity or resistance. Alas, these arrows (or darts or javelins) always break on impact, and therefore can't be recovered at the end of the battle as other expended ammunition can be.", "Bloodthirsty Scabbard (Requires attunement) - If a blood-covered blade is sheathed in this blood-red scabbard, the creature attuned to it regains 2D6 hit points, up to a maximum of however much damage the blade did to the creature it drew blood from. (Not a construct or undead). Works once per long rest.",
         "Sorcerer's Scabbard - This scabbard is preferred by magic-users who don't want to be targeted in the first round. It's not a scabbard at all, but a waterproof case large enough to house one staff, two wands, or four scrolls. (Only the top-most item can be accessed; you have to remove it to get to the one below.) The case's 'cap' is the hilt of a gnarly looking sword. Any item stored in the case is protected from Detect Magic or Truesight (though a wise creature with Truesight will know something's awry by the fact that they can't see through it).", "Jawbreaker Pouch - This magic pouch contains six brightly colored, perfectly round bullets... great ammunition for slings. If for some reason you were to put one of these bullets into your mouth, you would discover it's a Goodberry as per the spell. Any expended stone, either fired or consumed, regrows in 24 hours.", "Sheath of Teeth - This rather cumbersome scabbard appears to be made out of ivory. No, wait. Oh man, those are teeth. Some barbarian warlord ordered the teeth of his enemies ripped out of their mouths and made into a scabbard for his great sword. The teeth chatter in terror whenever an invisible or ethereal creature is within line of sight. Every time a blade is drawn or sheathed, the teeth gnash in agony. Not great for stealth but it's so. Damn. Metal.", "Quiver of Love - A masterwork or better arrow kept in this small six shaft sleeve for at least a day will do no damage if drawn and fired. Instead the target will be affected by raising its reaction attitude by two steps. Hostile would be indifferent. Unfriendly would become friendly. Indifferent would become helpful.", 
         "Wary Scabbard - This scabbard can sense when a fight is about to happen, and will therefore assist when you draw your sword. You get advantage on initiative rolls.", "Bard's Baldric - This deceptively flashy sash can hold an enormous number of weapons and musical instruments. Every hour, one weapon or instrument hung on the Bard's Baldric turns into an embroidered 'patch' that can be removed as if drawing the weapon or musical instrument forth. Twelve daggers, two rapiers, a crossbow, three cantrip shooter pistols, four wands, two staves, two lutes, a flute, a flugelhorn, a bassoon, a lyre, a set of five dwarvish pan-drums, nine chimes, plus 29 full, three partial, and eight empty bottles of elvish wine were reputed to have been stored on the sash at the same time. The embroidery patches are allowed to overlap without affecting their accessibility as long as the wearer stays aware of what is where. Apparently elvish wine bottles can be used as musical instruments, full or empty.", "Heavy Hangers - These braces seem to weigh far too much at 10 pounds empty, but whatever weapons are carried by the two loops on the wearers back will weigh up to 20 pounds less each.", "Launching Scabbard (Requires attunement) - When the command word is spoken, the weapon stored in the scabbard is launched forward at high speed, as per the Catapult spell. The wearer can attempt a DC 20 DEX or sleight of hand check to catch the weapon. If they succeed, then they have drawn the weapon as a free action. If they fail, the weapon goes flying off in a straight line (again, as per the Catapult spell).", "Wand Sheath of Charging - Fits any wand and has its own set of 50 charges. When you place a wand in it, the next use will use the sheath's charges instead of the wand's.", "Scab-Bard - This metal scabbard is made for a rapier. Tiny holes drilled at strategic locations along its length allow it to be used, in a pinch, as a flute.", 
         "Sheath of Shadow - The blade drawn from this scabbard will start out looking like a dim shadowy illusion, and for 2d6 rounds will remain indistinct, completely silent, and gain the ghost touch property. Not only is the sword silent and hidden, but by will of wanting stealth, but a victim so wounded can make no sound, and if killed while the blade is a shadow, the victim's body is shifted to the plane of Shadow. Blood drawn fades as shadow-like smoke.", "Scabbard of Souls - This scabbard contains the souls of enemies slain by the sword it holds. The screams of the entrapped souls howl in terror whenever sheathing or unsheathing your sword from this scabbard. The sword kept in this scabbard does an additional +1 necrotic damage, and the soul of any creature killed by the sword is trapped in the scabbard and the creature cannot be resurrected as long as the scabbard is intact.", "Defender's Scabbard - This heavy metal scabbard for a one handed blade magically unfolds into a shield when no weapon rests inside it. You can equip the scabbard as a shield in the same action you draw the weapon from it. When a weapon is inserted, it returns to being a compact scabbard.", "Flash of Steel - You may draw the blade sheathed within this scabbard as a Reaction. When you do so, a Physical Attack against you is Deflected and misses you, should you best the Attacker in a Contested Sleight of Hand (Dexterity) Check, so long as you are Proficient in the Skill. If you win the Contested Check, you may then Move up to 5 Feet away from the direction of the Attack (either straight or diagonally), this Movement does not Provoke Opportunity Attacks. You may perform this Reaction a number of times a day Equal to your Dexterity Modifier.", "Scabbard of Disarming - Any length of steel placed into this scabbard is permanently destroyed. Half-sheathing your sword will leave you with half of a sword. Fully sheathing will leave you with just the hilt. There is no way to recover a blade lost via this method.", 
         "Immovable Scabbard - A scabbard that is also an immovable rod.", "Grung hide sheath/quiver - Multicolored with vibrant reds, blues, and yellows, and smooth to the touch. Any weapon/ammunition stored in it gain one use of paralytic poison. Target must make a DC 11 Con save or be paralyzed for 1d4-1 turns, they may attempt this save at the beginning of any remaining turns while this effect is active.", "Sheath of Sheathing - This sheath functions as a bag of holding, but for any sword that would fit in it. There is always a sword handle poking out of it which you grab to pull out a sword, that you think of, that you have already placed inside of it. The handle disappears when no swords are being held or you are about to sheath one. You can decide which sword’s handle is poking out, but it has to be one that is already inside. The Sheath of Sheathing can hold up to 100 swords. Such as a Bag of Holding, the Sheath does not require attunement and if you try to put it in another extra dimensional space which functions similar, both are destroyed.", "Sword Poacher - This black scabbard is seemingly unremarkable, with a plain looking sword hilt placed in its top. As an action you can draw the sword hilt and force a target within 60 ft you can see who has a melee weapon to make a Charisma saving throw. On a failure, the weapon is transported in to your hand and the hilt will returns to the scabbard. If the target isn’t holding their weapon, they make the save with disadvantage. If you target a weapon that isn’t being worn, carried or held, there is no saving throw and the weapon is transported to your hand. You can use this feature 3 times, regaining all uses at dawn. If you lose the hilt, you must replace it with a different hilt by it in to the scabbard and leaving it there for 24 hours.",
        "Elemental Syphon (Only works on one weapon type, determined by DM) - This brown scabbard has a large clear gem embedded in to its surface, with brass detailing. When you take acid, cold, fire, lightning, or thunder damage, you can spend a charge and use your reaction to halve the amount taken. To do so, you must be holding the scabbard in your hand. The scabbard stores the energy, causing the gem to flow the corresponding colour and glow with 5 ft of dim light. The scabbard stores the energy for 1 hour, or until you use this feature again. The next time you draw a weapon from the scabbard, it is charged with elemental energy for 1 minute and deals an additional 1d6 damage (of the stored type) on a hit. This scabbard has 4 charges, and regains 1d4 daily at dawn.", "Paytowin (Only works for one weapon type, determined by DM) - This ornately carver and decorated golden scabbard has silver and platinum details. The whole at the top of it where you would place a sword is too small to fit a normal sword, instead roughly the right size to fit a standard coin. (If there are coins of various shapes and sizes in your setting, you can decide which type of coin fits.) You can feed coins in to the scabbard through the slot, which magically seem to disappear as there is not enough space to fit them in to the scabbard otherwise. After the coins have been placed inside, and the sword is left along for 1 hour, a magical sword made of the matching precious metals appears inside of it. The sword can be removed and placed back in to the scabbard, but no other sword can be. The sword is either +1 (300 gp), +2 (900 gp) or +3 (2700 gp). The sword remains until broken or you create a new one from the scabbard.",
        "Dusks Breath (Fits regular daggers) - This dark black dagger sheath has a small stone decoration of a woman’s mouth with a finger to it, like it is hushing. When you draw a dagger from the sheath, an area of silence (as if you had cast the spell) appears in a 10ft radius centered on you (but not moving with you). The area remains until the end of your next turn. Once used, this feature can’t be used again for 1 minute.", "Forge Breath (Fits regular long swords) - This iron scabbard is engraved with dwarven runes, with a large central giant “ild” rune at the top that glows like warm coals. When a non-magical metal sword is placed in to scabbard, the ild rune flares up. If the sword is left in the scabbard for 1 minute it heats up, remaining heated for 1 minute after removed. A heated blade deals an additional 1d8 fire damage on a hit.", "Multiblade (Works on any weapon that would reasonably fit in to it) - This scabbard has a small rotating dial with five gemstones embedded in to it, and another gem stone above the dial. As an action you can place a weapon in to the scabbard and speak its command word to bond it with the scabbard, causing a gemstone to light up. When the dial is rotated sword magically disappears in to an extradimensional space. When rotated so it’s correspond gem is selected, that weapon’s hilt reappears so that you can draw it from the scabbard. You can store up to five weapons in the scabbard at a time.", 
        "Hidden Edge (Works on any weapon that would reasonably fit in to it) - This small sheath always weighs 1 lb, and is an unremarkable brown leather. The inside of the sheath is magically enlarged, so when a weapon is placed in to the sheath it fits even though it doesn’t look like it normally would. Additionally, when a weapon is placed in the sheath both the hilt and the sheath turn invisible until the weapon is drawn from the sheath again.", "Daggerstorm (Fits any normal sized dagger) - This fairly normal looking sheath has three holes, two at the back and one at the front on top of the others. The sheath has 3 charges. When a dagger is placed in to the top hole, nothing magical happens. When placed in to the left hole, you cast conjure volley and when placed in to the right hole, you cast blade barrier. Neither spell requires components or concentration, but end early if the dagger is removed, and spends a charge when used. If you place a dagger in to the left and right hole at the same time, the sheath explodes and is destroyed, throwing shrapnel around. Each forcing creature in a 30ft radius must make a Dexterity saving throw, taking 6d6 piercing damage on a failure or half as much on a success. You automatically fail this saving throw if the sheath is attached to you. The sheath regains 1d3 charges daily at dawn.", 
        "Mirrorune (Works for one weapon type, determined by the DM; requires attunement) This scabbard is white, with reflective metal decorations and the symbol of three crossing arms gripping each other on the wrist. As a bonus action when you draw your weapon from this scabbard, you can speak its command word to cast mirror image on yourself. The spell ends early if you return the weapon to the scabbard. When you hit a creature with a melee weapon attack, you can cause one of your duplicates to attack with you, dealing an additional 1d8 psychic damage. You can do this a number of times per turn equal to the number of duplicates you have. When you’ve used this feature, you can’t do so again until you finish a long rest.", "Spellscribed (Works for one weapon type, determined by the DM; requires attunement) - This scabbard is carved with intricate arcane tunes which shimmer and glow with magical energy. The magic of this scabbard only works while it is on your person, and a non-magical weapon is placed inside of it. When you successfully counter or dispel a spell, the scabbard captures it and burns runes and symbols on to the weapon inside of it. A creature holding the weapon can cast the spell using their own spell slots and consuming the sword in the process. If the spell requires material components, the destruction of the sword replaces them. A wizard can copy the spell in to their spell book if they use the sword as a guide.", 
        "Returning Quiver Arrows and ranged weapons fired/thrown are magnetized back to the quiver (either just instantly returning, or travelling in a straight line back to the wearer. If they travel, they can damage anything in their path, are stopped by solid objects, and must be caught or they might harm the wearer.)", "Sentient Quiver (Requires attunement) - The quiver binds to the consciousness of the wearer. Ranged items stored in this can be curved round simple curves and corners.", "Elemental Sheath - Three times per day the sheath can impart a temporary enchantment on the weapon. While enchanted the weapon does +1d6 elemental damage (acid, cold, eldritch energy, electricity, fire, necrotic, thunder). The enchantment last for 10 minutes.", "Sheath of Invisibility	Any weapon placed in the sheath becomes invisible, giving it the appearance of an empty sheath.", "Sheath of Holding - The sheath can hold any size of sword.", "Sheath of Summoning - The wielder can point the empty sheath at a sword or dagger within 50 ft. Upon command the blade will be pulled into the sheath. If the weapon is held, the wielder must make a DC 15 Str check or be disarmed.", "Bloodless Sheath -Used mostly for training, any weapon drawn from this sheath is mostly non-lethal for the next minute. During this time, damage rolls with the weapon roll no dice, instead the weapon deals 1 point of damage.", "Divining Sheath - Once per day, when a weapon is drawn from this sheath, the weapon may be used as a focus to cast the spell locate object without expending a spell slot. The tip of the hilt (or tip of the blade) points the direction toward the target object.", "Duplication Sheath -Once a weapon is placed into this sheath, duplicates of the weapon may be drawn from the sheath at any time. These duplicate weapons do not have any magical properties and disappear 1 minute after being drawn from the sheath.", "Poisoning Sheath - The edges of this sheath are coated in a magically regenerating poison. Any weapon that fits into the sheath and is then drawn deals 1d10 poison damage on the next hit. The target must suceed upon a DC 15 Con save or be poisoned for a minute. This effect can be used up to 3 times a day.",
         "Grinny, the Mimic Sheath (Wondrous Item, uncommon, requires attunement) - Grinny is a tame mimic created in an age long past by a powerful sorcerer as a gift for a warrior companion. (Based from, and meant to be paired with, Toothy the Trusty Mimic.", "Scabbard of Animation - A magical artifact of unknown origin. Whatever weapon (although a sword usually fits best) is placed into it is immediately bestowed sentience.", "Dragonscale Sheath (Requires attunement) - A blade drawn from this form-fitting sheath deals +1 damage to draconic creatures, and confers many powers.", "Thunder - You may draw the blade within this scabbard as a Bonus Action, dealing 1d4 Thunder Damage to the first Target within 15ft of you that you point your Blade at. The Target must succeed a DC 14 Constitution Save, or be Deafened until the End of Your Next Turn. The First Attack you make with the Blade after Drawing it gains +1 Lightning Damage. You may use this Bonus Action a number of times per day equal to twice your Constitution Modifier.", "Whetstone Sheath - Only usable once on short/long rest, can not be applied to magical items. Adamantine gives the ability to bypass damage reduction or resistance for 1d4 swings of that slashing or piercing weapon; Mithral gives silvered and a plus one for 2d4 attacks with that slashing or piercing weapon.", "Dryad Tears - This sack was once soaked in Dryad Tears. Any wooden melee weapon stored in it can add 1D4 debuff for one round, effective for 1d6 attacks.", "Phoenix Quiver - A non-magical, unfletched arrow or quarrel placed into this quiver will grow fletches that burst into flames on impact, causing 1D6 fire damage in a 5-foot radius from the target. The arrow or quarrel is consumed by the flames.", 
         "Shielding Sheath - This sword sheath can give you a bonus +2 to your ac as a reaction. It can be used as a club for use as two weapon fighting.", "Sheath of Speed - As a draw action, you may make a melee attack with the sword in this sheath. The target may use a reaction to take a five foot step away from the opponent to avoid this attack. Usable once per short rest.", "Faithful Scabbard - (Requires attunement) This scabbard was made for a warrior who liked to draw his sword and dramatically toss away his scabbard... but also wanted to get the scabbard back at the end of the battle. Once tossed aside, the scabbard will slowly but relentless wriggle and writhe on the ground, snake-like, until it returns to the creature attuned to it. Could backfire if you're attempting to hide after a losing battle.", "Sheath of Avarice - A gilded sheath of some kind, and Detect Magic would discover Transmutation. Any weapon put in becomes coated in gold but (if you opt for it to be cursed), loses any magical properties unless it is an artifact or a higher rarity (probably Rare or higher), or it is made out of Mithral or Adamantine. If you cast Remove Curse on the sheath and put a weapon gilded by it inside, it will turn back to normal. If the weapon is non-magical, treat as 10 times the price (minimum of 5 Gold Pieces).", "Scabbard of Dispense - This scabbard can hold any appropriate weapon, but up 10 of them, as it is longer on the inside than the outside (Bag of Holding rules for piercing it and throwing it inside another). You may draw from it as part of the attack action (even if the weapon is thrown) if you are the person directly holding it. Otherwise, it's an action. The weapons come out in the order you put them in, so the last weapon put in comes out first, and so on. The hilt of the last weapon is shown outside of it. It is an action to stow weapons in it, which happens when you move an appropriate weapon nearby it (which then causes the top weapon's hilt to disappear, unless at max).",
          "Attachable Quiver (or Case) - This 'quiver' appears as a normal quiver, except for some hooks it has at the end. You may attach this to object, items, and similar, where the hooks magically attach themselves to the object or item (action). The quiver, however, also adjusts its size in regards to what its attaching to. The amount of arrows the quiver can carry stay the same regardless, however. It may be attached to the base of a weapon that requires ammo (if it makes sense to fit), whereupon it will automatically dispense the next ammo you need when you draw it (and gives the exact type, in the case of magic arrows or different types of ammo stored inside). Variants of this may actually assist in firing, in which case, if the weapon has the reload or loading property, it may be done as a free action.", "Sheath of Rust - This sheath looks like a normal sheath, but is actually host to the slime of a grey ooze inside it (or is made out of rust monster parts, has an actual grey ooze inside, however you want to flavor it). Whenever a nonmagical ferrous metal weapon is put it, it corrodes it. every day at dawn, if a weapon is inside the sheath, it takes a permanent -1 to damage rolls. This is accumulative, and once it reaches -5, all of the weapon is eaten away except the hilt. Additionally (if the weapon has grey ooze slime coated inside, or has an actual grey ooze inside), if it eats 2 weapons like this, it may create a new grey ooze, which comes out of the sheath and forms outside the sheath. This Grey Ooze may follow the sheath around so long as it has reason to (ie: metal to eat). Only one Grey Ooze may be born like this. This weapon isn't necessarily magic, but if it is enchanted, it gives off Abjuration Magic (which protects the sheath from it's own damaging conditions).", 
         "Quiver of Repair - This quiver repairs arrows and ammo inside, and even houses additional strings for bows or crossbows. If you put any pieces of arrows or bolts inside, (if the parts correspond) after a long rest it will connect them together. Additionally, it has a pouch which carries 2 bow or crossbow strings. If you take this out, and lay it on top of the bow (the bow must be next to the quiver), the magic from the quiver will transfer over to the string, which will magically attach itself to the bow or crossbow over the course of a rest. Every 5 days, the quiver forms another string. The Quiver does not restore magical properties to any repaired arrows or bolts, however. The Quiver itself will repair any harm it takes over the course of a rest, so long as it doesn't 'completely destroy it' (i.e., minor damage it doesn't, if the quiver was cut in half however, you'd need to get both parts so it can repair itself).", "Trickster's Sheath - When a one-handed Bladed Weapon is placed within the Sheath, it changes shape to replicate it, becoming a slightly larger copy. It can be held in your Offhand and easily be mistaken for an exact copy of the bladed weapon, while having none of the stats. This Sheath can stick to a belt as though it were looped, to allow for easy drawing as a faux-offhand weapon.", "Scabbard of the Divine Messenger - When you place a blade of non-prime material origin in the scabbard you can send once a day a message to its creator (like the raven queen, a fire giant, celestial, fiend or another powerful being who made your weapon).",
    ]
    document.getElementById("Scab").innerHTML = rollArray(scabbards)
};
function findTrinket() {
    let trinket = [
        "A miniature, tame mimic.", "A carved marble elephant.", "A small round cactus with two eyes.", "A pocket book of dwarven poetry.", "A bronze box containing a tiny wooden owl.", "A solid blue metal sphere, one inch in diameter, with three parallel grooves around the circumference.", "A pouch containing ten dried peas.", "A ceramic puzzle cube, with each face divided into four independently rotating squares enameled with astronomical signs.", "A square of bear-beetle leather, a creature unique to the misty woods of Cix.", "A sheet of vellum on which is crudely painted a herbal plant that you have yet to identify.", "A petrified frog.", "A twenty-sided die.", "A cut yellow chrysanthemum that never dies.", "A palm-sized iron cage: the door doesn't shut properly, as the tiny lock was broken from the inside.", "A blob of grey goo, slippy but safe to touch, kept in a ceramic pot.", "A dried sky lily, from the tip of the Godshead, an impossibly high mountain.", "A glowing blue-green line, six inches long, but with no discernible radius.", "A pretty conch shell.", "A scrap of paper on which is written, in Goblin, 'My dearest Bess,'.", 
        "A keychain holding the head of a broken key.", "An echo pearl from the depths of the Vibration Lake.", "A toy crossbow.", "Lip balm.", "A fossil of an extinct many-limbed critter.", "A brass prosthetic nose.", "A corkscrew.", "A dried poison gland of a jagged fish.", "A bronze gear on which is etched the word 'Moon'.", "A map of a labyrinth, on which is penciled a line that starts at the centre but fails to connect to the entrance.", "A cube of ice that never melts.", "A square of ironsilk sewn by the geargrubs of ancient Siclari.", "An ivory knitting needle.", "A peacock feather.", "A travel set of paints: someone has used up all the black.", "A wig of short platinum-blonde hair.", "A child's charm bracelet.", "A small bar of orichalcum, a metal only mentioned in ancient literature.", "A deed to a ruined tower.", "An invitation to a formal ball to be held in two years time.", "A smoking pipe carved from granite.", "A vial of scented oil.", "A preserved basilisk eye.", "A torn page on which is written 'Death! / Plop. / The barges down in the river flop. / Flop, plop. / Above, beneath'.", "An intricate knot that nobody seems to know how to tie or untie – sailors believe it to be bad luck.", "Pages ripped out of an accounting journal of a local merchant.", "A ring with a poison reservoir for slipping into drinks and a tiny razor edge for cutting purse-strings.",
        "A glass globe of swirling green goop, no openings.", "A bundle of ragged 'treasure maps' drawn by inventive local children.", "A sliver from a spear said to have pierced the armpit of a saint.", "A portfolio of pressed flowers.", "A small handbook of foreign coins, for travelers to identify denominations.", "A slightly out of date guidebook to foreign inns, taverns, and transportation.", "Six useless wooden tokens previously issued by a traitor-prince as currency.", "Two false fingernails painted with mysterious symbols.", "A set of cosmetic tools for cleaning the ears.", "A harmless stage dagger with retracting blade and blood-compartment.", "A floating glass orb that follows you around and makes whirring sounds.", "A goblin-made key that can lock any door, but unlock none.", "A translucent coin, minted in an unknown land.", "A bronze ring engraved with dark symbols that was supposedly buried with a legendary necromancer long ago.", "A ring carved with the unfinished insignia to a defunct secret organization.", "A thimble on which is an enamel painting of a turtle.", "A puzzle box holding 10 fingernail clippings.", "A pair of badly worn hairdressing scissors.", "A wax hand shaped to hold a large cup.", "A measuring tape, marked in ink at 23 inches.", "A seashell that is silent when held up to your ear.", "A coprolite.", "One piece of unknown paper currency with no obvious denomination.", "A bootlace entwined with gold thread.", "A dented sheriff's badge.", "A tiny bubble level that is calibrated incorrectly.", "A belt buckle.", "A letter of complaint to a toy shop owner.", "A decorative leather stud.", "A penny whistle that plays the same note no matter which holes are covered.", "A ticket admitting an adult and child onto a thing called a 'semiotic tram'.", "A small glass vial holding three eyelashes.", "A tub of putty.", "A leather shoe made for a dog.", "A doll head with no hair and poorly applied makeup.", 
        "A pewter spork.", "Illustrated instructions on how to make a paper hat.", "A clear glass dish with four round notches around the outside edge.", "A wire circlet that bestows upon its wearer perfect posture.", "A small hand-sized box covered with numbered buttons.", "An empty whiskey tumbler that causes any liquid poured into it to become bourbon.", "A book of flumph grammar.", "A hunk of metal which appears to be several gears jammed together at unnatural and impossible angles: attempting to turn it causes it to emit a horrible shrieking sound.", "A crystal prism that refracts shadow instead of light.", "A smokeless and odorless candle.", "A flat disc of layered metal and prismatic glass with a hole in the centre.", "An ornate pewter tankard made without a bottom.", "A wooden device designed to be gripped in two hands; two levers protrude from the top, and two triggers from the underside.", "Two perfectly identical pine cones.", "A sponge that can absorb 60 gallons of ale (and only ale).", "A pepper grinder containing an unlimited supply of pepper unless opened, at which point it becomes half empty.", "A poorly cultivated bonsai juniper in a glazed ceramic pot.", "An oval-shaped soapstone tablet inscribed with a short list of religious prohibitions.", "A wooden doll with a door that opens to reveal a slightly smaller, identical, doll; this one is empty, perhaps there are still smaller dolls that are missing?", "A stone figure of a snake that changes positions after every full moon.", "A silver key of unknown origins on a leather cord as a pendant that emits strange magical energy.", "The right half of a broken bronze circlet with a light leafy pattern that when placed on your head, stays in place as though the other half was still there.", "A small silver rod which when rolled between your hands emits sounds as though a lute were being played by a master softly nearby.", "A music box that can only be heard by someone who as wound it at least once.", 
        "A small stone cube that, when tapped with a rod of metal, looks as though it were made of that metal for a few seconds.", "A wooden sphere with a white marking that always faces the sun, and a black marking that always faces the moon.", "An opaque jar that cannot be opened or broken, no matter how hard you try.", "A journal that details the great adventures of a hero you have never heard of, complete with vivid descriptions of nonsensical creatures and terms, all written in messy handwriting, but with impressive diction.", "A tiny sack that, when opened, is full of sand, but feels as heavy as a large stone when lifted.", "A puppet in the likeness of someone you distantly know, that echoes your movements when you (and only you) place it on the ground.", "An iron rod that bends in unusual ways when you look directly at it, but rights itself when you look away.", "A book that perfectly records the holder's dreams when held while sleeping.", "A tin pot that is just the right size for you to wear as a helmet.", "A marble sculpture of a tiny elf holding a lute seated on a chair that plays music every so often.", "A piece of pure white cloth that never gets dirty.", "A hat that never gets wet.", "A mask that copies its wearer's facial expressions.", "A humanoid skull with ethereal green orbs in its eye sockets.", "A wineskin that only holds wine. Any other liquid pours out after a few seconds.", "A leather belt that, when worn, glows with faint blue light.", "A tiny javelin with an ornately carved shaft that always returns when thrown, exactly halfway between you and the person closest to you.", "A sphere of crystal with a tiny shard of obsidian at the exact centre.", "A flask that freezes any liquids stored in it at midnight, and unfreezes them at noon.", "A book with words that change every time it is read.", "A chain that feels warm when its holder is standing directly beside an awakened tree.", "A cube with tiny animals wandering on each face that change when they cross onto a different face.", "The preserved hand of a famous noble that moves when pointed at the ground.", "A terribly written novel whose plot seems to match events that have happened in your life.", 
        "A recount of a famous battle that contradicts what is commonly thought about that battle, written by a great sage who was present.", "A crown made out of ice that never melts.", "A piece of string that always emits smoke.", "A rod of indeterminate metal that changes its length at random every other day.", "The hilt of a dagger that was used to assassinate a king, with an onyx on the end that glows ominously on nights with a full moon.", "A stone carved to look like a head that occasionally speaks, asking questions that change every time.", "A stick that glows brightly when held by an undead creature.", "A flute that, when played, makes the sound of a random instrument, though never a flute.", "An invitation to an event that has already ended.", "A copper ring that feels abnormally light.", "A turban that, when worn, makes your steps feel very light.", "A cube of glass with mysterious runes etched on each corner.", "A towel with a set of instructions embroidered on it that clearly state to wear it on the head in case of mind flayer attack.", "A rose that, when placed in a bouquet with exactly 5 other flowers, glows brightly, and seems to move.", "A set of brass wind chimes that only chime when hung on a rod of precious metal.", "A grotesque statuette of a humanoid with rat-like features.", "A drawing of a spider with twelve legs being used as a mount by a crudely drawn hobgoblin without a head, with a set of poems on the back written in poor Common.", "The badge of a powerful organisation, with writing etched on the back that defames that group.", "The diary of a prison guard with half of the pages written in a different language.", "A handbook of etiquette for nobles of an empire that fell.", "A translation guide for a fictional language.", "The head of a pickaxe that was used in a lost gold mine, with names carved in Dwarvish runes along the sides.", "A wooden plank that refuses to burn.", "A detailed guide on the anatomy of rocs.", "A muddy book with a single phrase repeated over and over.", "A surprisingly realistic replica of a rakshasa hand.", "A stone rod with a tin coating that has worn through in several places.", "A compass that points towards the nearest bottle of rum.", 
        "A stone that feels very heavy, yet floats effortlessly.", "A map with no key or locations, only red circles with lines connecting them.", "A shard of glass that floats a tiny distance off of the ground when near an open flame.", "A diagram of a forest on an island with no named artist.", "An orb that glows with a flash of green light at noon.", "A locket with a strange rune carved inside.", "A green coat with numerous pockets, each with a separate piece of a moustache trimming kit inside.", "A silver plate that feels rough, though it were made from coarse stone, but never feels painful to touch.", "A figurine of a fiend, so lifelike it seems like it might come to life and attack any second.", "A sapling that cannot be placed into soil, but never dies and has a single sweet fruit on its branches that grows back after one day when picked.", "A red coat that makes you feel colder when it is worn.", "A vial of tree sap.", "A rod of metal that produces tiny sparks from a red marking when a black button on the other end is pressed.", "A wooden cane that, when placed on the ground, stands perfectly straight, and cannot be tipped over.", "A bottle of red liquid that sparkles ever so slightly under direct moonlight, with a faded blue label that cannot be read.", "A sack of shed dragon claws.", "A feather with a piece of red string tied on the end of the shaft.", "An engagement ring that belonged to one of your parents.", "A book that you faintly remember from your childhood that you thought was lost for many years.", "An odd stone that seems to permeate energy.", "A sword sized for a child.", "A vial of water from a hot spring.", "A squat metal tin full of brown powder that always feels cold to the touch, regardless of the temperature.", "A glove worn by someone you deeply admire.", "A shard of crystal that glows when near places dedicated to a certain deity, and glows brighter the closer you are.", "A tome from an abandoned library.", 
        "A gear that refuses to mesh with any other.", "A box of nuts that feel like they are made from metal, but can be eaten as though they were normal.", "A tree branch with an odd symbol.", "A yew wood figurine of a satyr with wings, carrying a willow wood staff.", "A suit of armour made from oak wood, sized for a doll, painted in vivid red and black.", "A stone with odd indentations, that seem to spell out a message of some kind.", "A vial of mysterious pale blue liquid that slithers back in when poured out, and has a pleasant floral scent.", "A jug that turns liquids stored in it into milk after a few minutes.", "A seed that never grows when planted, but looks very similar to an acorn with a few green lumps.", "A waxy white flower that constantly moves as though a gust of wind were blowing it around.", "A robe with a tag on the inside that reads 'to my dearest pupil,' given to you by someone you deeply respect.", "A tome filled with cryptic writings, all in Common, but with confusing terminology.", "A beige jar of red ointment without a label.", "A famous calligrapher's personal brush.", "A band of iron that shines brilliantly despite being completely rusted.", "A small cylinder of stone that smells faintly of blood.", "A tunic that smells of saltwater and bears the emblem of an established land-locked nation on the front.", "A curious looking pair of goggles with the words 'Property of Ice! DON'T TOUCH!' scrawled into the side.", "A small blue cube that faintly glows for some unknown reason.", "A small orb with water and a small living jellyfish inside.", "A cat figurine.", "A hat that has a secret space on the inside which is the size of a small pouch and very hard to locate.", "A bar of scented soap that bubbles.", "A book of lore, that is hollow inside.", "A belt buckle stolen from a noble or a king.", "A slip of parchment with the phrase 'I am not dead' written on it.", "A small fist-sized cube that occasionally makes strange noises.", 
        "An unusually sharp spoon.", "The symbol of a powerful religion, covered in soot that stays no matter how much it is cleaned.", "The diary of a philanderer that contains detailed descriptions of common monsters.", "A gigantic snake's tooth that has an unsettling aura about it.", "An unusually small humanoid skull.", "A bit of rock from a headstone.", "A tiny bag of yellowish powder.", "A small indestructible talking skull that tends to mumble racist slurs whenever it sees an elf.", "A box of black licorice.", "A strangely shaped bone.", "An iron ring that, when worn, makes the wearer feel calm.", "A group of small glassy spheres, all attached to each other in such a way that they form a rough pyramidal shape.", "An empty bottle that once held the blood of a demon.", "A tiny glass vial that contains a portion of the ashes of a statue of a god that was destroyed by marauders.", "A detailed guide to making pickled foods.", "A mask in the shape of a lion's head that moves from side to side occasionally when worn, yet the wearer experiences no change.", "An axehead that appears to have been snapped off.", "A palm-sized greenish stone with the carved image of a dragon on one side, and a humanoid on the other.", "The head of a mummy.", "A flask of giant's blood.", "A miniature shield.", "A sea shell with a strange rune carved into it.", "A corn husk doll which dances under its own power when music is played nearby.", "An arm band in the shape of a snake, with emeralds for eyes.", "A tiny, fossilized ammonite made into a necklace.", "An old coin, showing a hare on one side and the moon on the reverse.", "The banner of a noble house.", "A bird carved out of lapis lazuli.", 
        "A small pouch filled with the teeth of various shark species.", "A tiny painting showing a vulture carrying a bone in its beak.", "A fist-sized stone that glows slightly and feels incredibly hot to the touch.", "An ingot of copper with an unusual hue.", "A small notebook full of drawings.", "A fist sized turtle shell.", "A drawing of a flower that looks different when viewed from an angle.", "A perfectly flat wheel made from terracotta.", "The journal of a philosopher, full of wise sayings and anecdotes.", "A malevolent-looking raven skull that has been charred black.", "A small glass case containing several glossy butterfly wings.", "A preserved frog that moves and croaks like a living frog, but to even an untrained eye is undeniably deceased.", "A mahogany box of religious scrolls.", "A guide to changing bowstrings full of grammatical errors.", "A ceramic troll statuette with no arms, just legs.", "A glass bottle that shines like gold.", "An iron door-handle that makes menacing noises when underground.", "A sliver ring that feels very slippery.", "An ornately carved figurine of a giant made from bone.", "A rusted fork.", "A shoe made from crystal.", "A piece of tree bark that is coated in blood.", "A small oak wood box of vibrantly-coloured powders, each colour in its own tiny drawer.", "A silver hand mirror with a dragon etched onto the back.", "A tine of a deer's antler.", "A miniature teapot and teacup.", "A bejeweled statuette of a knight that is a replica of a famous sculpture.", "A box of small orange cylinders that break and burn easily.", "A stone carving of a piece of bacon.",
        "A horn that has been cut cleanly in half.", "A thin tube of iron filings with the seal of a noble house on both ends.", "A small clay pig toy.", "A small metal can that contains black colored pudding. If touched, the pudding leaves a slight stinging sensation to the hand.", "A necklace strung with tiny snail shells.", "Half of a coin with unusual markings engraved on both sides that cut off where the other half would connect.", "A sack full of pieces of half-eaten bread.", "A small bottle labeled 'otyugh perfume' that really stinks.", "An odd lump of metal that smells like sweat and rotten fish.", "A fist-sized green seed covered in brown spines.", "A fist-sized metal frog or toad (your choice).", "A glass figurine in the shape of a lobster.", "A wooden spoon, carved from a bigger spoon.", "A jeweled goblet that will never, ever spill its contents.", "An amulet that, when worn, makes you look older when you are injured.", "A bowl covered in ornate designs depicting hill giants in combat with dwarves.", "A copper badge that you have never seen before in your life, though it has your name on it.", "The preserved finger of a giant that you once knew.", "A set of ceramic castles that have a space for a candle in the middle. When the candle is lit the castle looks like it has lights on in the windows.", "A perfectly reflective ball with a magnetic stick which allows it to be used to look around corners.", "A laurel of flowers which never wilt or die.", "A purple amulet in the shape of a pig's head.", "A magically shrunken goblin in a tiny cage.", "A copper lighter that never runs out of fluid", "A fist-sized sphere; half of which is blue while the other half is red.", "A pair of gloves that seem unusually warm to the touch.", "A severed ape arm covered in black fur.", "A vine covered in thorns that writhes around occasionally.", "A petrified goat skull.", "A brown mushroom of extraordinary size.", "A drawing of a bird that you have never seen before.", "A tiny piece of metal that floats on water.",
        "A tiny stone orb that hangs in the air for a bit when you throw it.", "An iron cuirass far too large to be worn by a humanoid.", "An extremely large leaf that causes food that it touches to become very bitter.", "A single leather boot with unknown markings on the bottom.", "A leather pouch that contains a single wooden token depicting a crab.", "A belt with a buckle made from an unusually twisted piece of copper.", "An eyeball carved from stone that occasionally moves around, as though looking for something.", "A piece of rope that is always too short to be useful.", "A d8 die that looks to have been split in half by a large axe.", "A carved wooden statuette of a hawk.", "A tiny box that contains a model chair.", "An eerily lifelike wooden bear figurine that is never found where you left it.", "A small section of a snakeskin belt that seems to slither when it touches the ground.", "A tiny carved skull with jewels in its eyes. You have a feeling like someone is watching you whenever you hold it.", "A bottle of rum that never runs out.", "A cloak that always flaps gently, as if pushed by a slight breeze.", "A split piece of unknown wood, decorated to look as if it once was a piece of a druidic focus.", "A small mirror in which your reflection remains, crying hideously whenever you look at it.", "A small rodent's heart. Still beating.", "A tiny, tame earth elemental that is afraid of beetles.", "A book that gives you a headache whenever you try to read it. You are still unsure of what knowledge or story it holds.", "A tankard that is always full of a wretched black fluid. If tipped, the fluid runs endlessly.", "An obsidian dagger that reflects shadow as a monochrome rainbow.", "An undead fly tied to an invincible foot long piece of thread.", "A small gem that changes color and detail to any object it touches.", "A miniature platinum lightning bolt that vibrates and zooms around when a storm is coming.", "A deck of cards with unknown runes on each card.",
        "A creepy idol of a black dragon with red jewels as eyes, whenever someone looks at the idol eyes their eyes flash red.", "A miniature shield painted with gold designs, when you clutch it you feel slightly more confident.", "A lava stone carved to look like a flame, it gives off endless heat.", "A set of golden letters that move around when nothing sees them, creating random words.", "A vial of red liquid that moves up or down depending on the current danger.", "Extremely hard to see moon stone fragments that make small laughing noises when you can't find them.", "A piece of taffy that always reappears when you eat it.", "A large pitcher of liquid that seems to always change flavor.", "A small marble that randomly changes color.", "A small crystal that shakes very violently when wet.", "Some random objects such as bones or stones that always come back together when destroyed", "A clear piece of fabric that hovers unless you pull it down.", "A marble that changes size when you aren't looking. Sometimes something that is touching it changes size slightly too, but changes back in 10 seconds.", "A page with unknown runes depicting and ancient spell but unreadable no matter what.", "A glass eye that spins to look at things other people are looking at.", "A vial shaped like a cylinder. Any liquid put inside gets tainted blue and gains a slight taste like blue raspberry.", "An expired potion of growth, now only makes you get slightly bigger when you take a sip, tastes like powdered iron for some apparent reason.", "An expired potion of darkvision, now just makes everything bright when you take a sip, tastes like dry carrots for some apparent reason.", "Some frog legs made of ivory that bounce around randomly.", "A bar of titanium that feels squishy and soft to touch.", "A book with a harmonious story, however whenever you turn the last page it takes you back to the middle of the story so you don't know how it ends.",
        "A clockwork device that's button won't press no matter what you do.", "A lens that reverses the color of things seen through it, black becomes white, cyan becomes orange, red becomes blue, and so on.", "The blade of a huge axe that feels insanely heavy to any creature smaller than Huge, but creatures that are Huge or larger think it is as light as a feather.", "A small worm statue that causes any creature that touches it to shrink by 1d4 inches over 1d4 minutes. Touching the statue again returns the creature to normal size.", "A green tonic labeled 'growth'. If anything drinks it they grow an inch each second for 1d4 minutes, then shrink 1 foot each second until they return to normal size. Their equipment changes size too but doesn't increase damage.", "A bloody hand that grips onto things and doesn't let go.", "Some vials of liquid that create moss on anything they touch. This moss keeps growing and will eventually cover the whole thing. Then the moss withers and flakes off.", "A packet of mints that cause the eater to change color for 1d6 hours.", "A set of thieves tools that are bent and broken yet they still work perfectly.", "A miniature brain made of coral.", "The branch of a tree that caught fire when you were nearby.", "A picture that has a field in it, as time goes, the picture changes and adds things like people and houses to itself.", "The eye of a cat, for some reason it commonly looks around at anything powerful.", "An acorn that makes ringing noises and shakes violently when touched.", "A hammer from a long gone blacksmith. Sometimes at night you can see the hammer float and pound any weapons nearby.", "A glass sphere containing ooze, still alive; it sometimes causes green acidic liquid to gush out of the sphere.", "A crystal dagger, it is engraved with the symbol of a flaming skull with a rune covered ring around it.", "A wizard's journal, recounting the tales of many arcane experiments.", "A red gemstone shaped like a heart.",
        "A purple gemstone shaped like a cage.", "A piece of coal vaguely shaped like a head.", "A pouch full of a fine black substance of unknown origin.", "A gem that can summon a dim orb of light that does nothing but follow the summoner for a while.", "A ceramic tile with a silvery sheen.", "An incredibly heavy bone with countless words inscribed into it.", "A small jar that has a lid attached to it. When the lid is closed, it turns its contents into fresh milk.", "An incomplete book that adds to itself constantly.", "A merchant's scale that is covered in blood stains.", "A hat that drenches the wearer in a viscous orange fluid.", "A vial of blood from an unknown creature.", "A child's severed finger, still fresh, and periodically twitching.", "A small painting of a skeleton in noble's clothes.", "A ring carved from the sternum of a serial killer's most beloved victim.", "The hilt of a broken greatsword. When held with both hands, blood runs down along the remnants of the blade.", "The left glove of a well-known murderer. You periodically find yourself wearing it.", "A small jar of sugar that makes all food and drink taste of salmon.", "A stuffed bear given to you by a child that wouldn't speak.", "A bundle of differently colored strands of hair.", "A small box containing bloody teeth and fingernails. The box has the word 'Mother' inscribed on the top.", "A tiny hat that makes you feel very confident whilst wearing it.", "An old piece of parchment reading 'Fredrick, Why?'", "A rat's skull with a beautiful, yet unidentifiable family crest carved into it.", "An apple with a single bite taken out of it. It does not decay, it tastes terrible, and you can't bring yourself to throw it out.", "A miniature painted wooden elephant with a single ivory tusk, the other one is snapped off with a jagged break.", "A magical tome. When the spells inside are cast, the effect is never the same, are extremely stupid, and the spells cast aren't what's written in the tome.", "A piece of frayed rope about a foot long. The ends are slightly burned.", "A war veteran's glass eye.", "A deformed human infant's skull.", "A ceramic jar containing rice grains. When opened, a foul odor emanates from the jar.",
        "A necklace adorned with a wooden medallion depicting a crudely-painted smiling face.", "A sacrificial dagger that cuts into your palm whenever you grip the hilt.", "A terrible love novel written by a hack author. For whatever reason, you love the story, even though you know it's terrible.", "A whistle that causes all that hear it to feel incredibly nauseous.", "An incredibly venomous snake that refuses to bite you, however, it likes to wrap itself around your arm.", "An ancient hero's heart, bound in linen and kept in a clay jar.", "A ring which makes the wearer reek of rotting fish.", "A pair of pants that supposedly belonged to a powerful necromancer.",
        "A pewter spoon that was owned by a powerful, fat landlord.", "A jar containing an alchemical salve that is labeled 'Apply to soles once per week.' However, the salve has solidified into a waxy mass.", "A helmet forged to fit the head of a child.", "A small, black-furred creature that wears a bone-carved mask. It's kinda cute, but it always follows you, and remains just out of arms' reach.", "A crystal prison in which a lich's soul is trapped. It is damaged, however, and the lich perpetually complains.", "A small bottle of chalk tablets. Unmarked, but scented with the smell of lilacs.", "A folded paper frog. When unfolded, you can read an uplifting message.", "A bracelet braided from the ligaments of some large creature, with a charm carved from a humanoid tooth.", "A piece of torn linen cloth worn soft by someone else's fingers. Up close, you can see marks where embroidery has been picked away.", "A small glass jar with a gilt-painted image of a minor goddess; empty with a waxy residue at the mouth.", "A glass file; intended for the care of nails, claws or talons.", "A string of rough, red beads that smell faintly of cinnamon.", "A carved bone portrait of a famous pirate; the enamel has worn thin.", "A small doll. Someone thought it would be a good idea to carve its head from an apple; the face is brown, dry and wizened.", "A wolf-hair paintbrush, perfect for calligraphy, though the binding is coming loose.", "A walnut-sized terracotta jar containing traces of red makeup.", "A fist-sized stone sphere that rolls after you when you put it down and walk away.", "A box of odd beads that bear no resemblance to eyes, yet always seem to watch you.",
        "A vial of dragon's blood.", "A wooden cup that, when put to the ear, relays the sounds of a tavern party.", "A violin that makes the player sound like an expert musician.", "A book with a mysterious bloody stain on the back cover.", "A waterskin that turns anything inside it into fresh, clean water.", "A life-sized statue of a gnome.", "A perfectly round snowball that never melts.", "A broken table knife that can only be held by red-haired humanoids.", "A 1-centimeter long perfectly functional crossbow.", "A crystal pen that will only write with green ink.", "A pair of silk trousers that are always a tad too big.", "A small coin purse with gold inside that cannot be removed.", "A wanted poster that bears the face of a terrified elf.", "A bright orange, ceramic throwing star that will always miss its target.", "A white metal goblet that grumbles angrily in Dwarvish when filled.", "A set of blue marble earrings that glow faintly in the presence of pork.", "A small humanoid skull that cackles every morning at the break of dawn.", "A pair of scissors that only cuts eyebrow hair.", "A silver coin with an engraved human that continuously waves to the holder.", "A cast iron pot with a love letter carved into the side.", "A bag that is full of rainbow-coloured sand.", "A leaf that will never blow away in the wind.", "A single iron shackle that was once worn by a deaf musician.", "A shirt button that changes shape every day.", "A single leather shoe that can be worn on either foot.", "A tiny oak barrel filled with even tinier apples that refills every full moon.", "A wooden dagger that's shaped to resemble a sacrificial blade.", "A purple banana that never rots and tastes like saltwater.", 
        "A short metal chain that doesn't make and sound when shaken.", "A map with directions to an abandoned gnome's house.", "A dragon's tooth that perpetually feels wet.", "A loincloth that's far too long.", "A mahogany dinner plate with the phrase 'POETRY IS DEAD' carved into the bottom.", "A small wooden box that contains a single, worn thimble.", "A fully articulate plate gauntlet made out of unbreakable, unmelting chocolate.", "A clear glass bottle that can be used as an eyeglass.", "A child's leather vest with a small club logo on the back.", "A codpiece with the entire Sylvan alphabet written on it.", "A black feather that somehow weighs 40 pounds.", "A salmon painting that repels mosquitoes.", "A pair of socks that tickle the wearer.", "A rolled-up scroll that displays the holder's exact height when opened.", "A pair of marble chess pieces, black and white, that argue with each other.", "A bandana that makes the wearer look 10 pounds lighter.", "A rock that screams in fear when it's thrown.", "A piece of parchment with an ink drawing of a centaur that always points north.", "A green, metal orb that slowly orbits any obese humanoid it's thrown at.", "A mouthpiece for an unknown musical instrument.", "A single newt's eye in a glass jar.", "A brass face mask that insults the wearer's outfit.", "A small jar of nails that can only be driven by a glass hammerhead.", "A closed lute case that incites extreme fear when someone tries to open it.", "A sword scabbard that's full to the brim with tiny wooden swords.", "A book that details a list of embarrassing childhood moments.", "A guide to living with a house full of talking objects.", "A fine, leather pouch that contains exactly 248 stone pebbles.", "A cookbook that only holds the phrase 'Don't cook fairies' scrawled in blood.", "A thin sheet of cooking paper that's been folded into a swan.", "A warm winter scarf knitted from skunk fur.", "A stone slab that floats.", "A backpack that makes eating sounds when items are put inside.", "A small unbreakable string that spans 10 feet.", "A decaying wooden knife inscribed by a child that reads 'the ultimate blade of destruction'.", "A small iron sculpture of a phoenix that fills you with peace due to it containing an aura of protection.", "A miniature cannon made of glass that when heated release a large amount of smoke.", "A pair of copper rimmed glasses that contain cracked lenses that slightly enhance your vision in the dark when worn.", 
        "A gigantic blade when used in combat of any kind it becomes immobile and unable to move at all otherwise it's as light as a feather.", "An old doll you found in an abandoned manor. The doll's eyes follow you and you usually have nightmares when you sleep near it even when you throw it away it comes right back to you.", "A cane sword that refuses to be unsheathed unless on a full moon.", "A black triangular pendant that gives off a rich king purple glow it is said to nullify pain but many believe not.", "A diary that when shaken reveals a secret that a nearby entity knows although the secrets are almost always useless.", "The soul of a hero long gone. It does nothing except look pretty and follow you incessantly.", "A strand of hair from a lower goddess.", "A small wooden box containing a pair of small sentient clay men that wonder around aimlessly they magically return to the box when it is closed.", "A shovel made from unusual blue metal.", "A sickly green humanoid bone.", "A tattered red cloak that patches itself up when its wearer is in a graveyard.", "An odd cog that spins on its own every so often.", "A stoppered bottle that contains a harmless undead spider.", "A small drone carving that depicts a naked goblin scratching his hindquarters.", "A wooden mask that makes the wearer see the people around them as unnaturally beautiful.", "A letter addressed to you from a king that has been long dead. It was sent recently.", "A small dull dagger that refuses to sharpen.", "A rusted coin that absorbs any oil it comes into contact with.", "A long letter of complaint addressed to a teacher you once had written on it.", "A glass jar that has about 12 living, miniature frogs inside of it.",
        "Some candy that tastes faintly of pineapple, and never seems to go bad.", "A broken piece of technology from the distant future it seems. Nobody can tell the purpose of the device, and nothing seems to repair it.", "A small doll with a cloak and toy dagger attached. On the back of the doll, the letters 'TDG' are written.", "A drinking horn with an odd rune carved on it.", "A tiny pink bottle that smells of roses when it is empty.", "A hunting horn that sounds like a trumpet when blown into.", "An owl feather quill that makes the holder always talk in the third person.", "A leather glove that talks when worn. It uses the wearer's fingers and thumb as a mouth.", "A miniature treasure chest that yells at you to shut it when it's opened.", "A wooden carving of an orc doing a handstand.", "A metal rod that can't conduct electricity.", "A small twig that doubles as the perfect toothpick, no matter who uses it.", "A gnome's hair brush.", "A small painting of a horse's rear end.", "A mirror that breaks when someone smiles in it.", "A cork for an old wine bottle that won't fit in any other bottle.", "A copper coin that, when flipped, tells the flipper a fake fortune.", "An erotic novel that's written backwards.", "A boomerang that comes back when you least expect it to.", "A pair of worn leather boots that won't move when someone wears them.", "A small pot of horse glue that says 'NOT FOOD, SERIOUSLY' on the side.", "A drinking glass that spits out whatever's poured into it. It then proceeds to tell off the person who filled it.", "A spyglass that works backwards.", "A centuries-old pack of rations that's perfectly preserved. The food inside tastes like chicken.", "A bowl of grapes that are harder than stone.", "A pitcher full of goblin tears.", "A legal deed for a house that doesn't exist.", "A brass tube that acts as a portal to Mechanus. It's impossible to put anything inside.", "A dagger made of folded parchment.", "A green wine bottle that can't break.", "A tiny skeleton that animates and dances when music is played.", "A prayer book to a made-up religion.", "An object that can't be accurately described. When someone tries to describe it, they're at a loss for words.",
        "A bell that summons a fox from the nearest unoccupied space. It does nothing but stare at the person who rang the bell for exactly three minutes and forty-two seconds, after which it runs off.", "A box of twelve matching pieces of broccoli.", "A live beehive full of bees. They're not happy.", "A tiny fairy in a jar that tells awful jokes.", "A journal written by a very racist tiefling.", "A bar of soap that smells like rotten meat.", "A key that breaks when it's used on a door. It doesn't open the door.", "A wheel of blue cheese that's been dyed red.", "A 300-page rulebook for rock-paper-scissors.", "A tin of makeup that's the most absurd color of orange.", "An apple that tastes like an orange.", "A large, steel lock without a key.", "A letter from an unknown sender. It reads, 'I told you so!' and the return address is simply labeled 'Feywild'.", "A slice of piping hot cherry pie, but it has no plate or utensils.", "A carefully detailed drawing of a halfling toe.", "A ruby that holds the soul of a long-dead evil sorcerer. He constantly gives bad advice.", "A ham and butter sandwich with lettuce, but the bread is made of cotton.", "A teacup full of live, non-venomous spiders.", "A costume mask made from a wolf's skull and pelt.", "A backscratcher, downsized for use by gnomes.", "A tattered blacksmith cap full of red dwarf hair.", "A small roll of leather that's been cured with giant urine.", "The hollowed-out shell of a large hermit crab.", "A book full of jokes about dragons.", "A lute made out of dry grass.", "A quill that never runs out of ink, but changes its ink color every hour.", "A repeating crossbow that won't fire bolts. It will, however, fire toothpicks.", 
        "A silver piece that glows red when exposed to methane.", "An iron ring inscribed with your name that perfectly fits your left index finger, and only yours.", "A treasure map that leads to a beggar's dandelion garden.", "A lovingly crafted travel tankard that makes all manners of drink taste of mead.", "A small wooden box containing a blood-stained pommel and a detailed account of a judicial duel.", "A flute in the shape of a skull made out of dead wood that whenever played makes the listeners feel scared.", "A ring embedded with a topaz containing a soul of a clueless wizard. He gives little to no insight into objects of intrigue.", "A small sword from a figurine it is incredibly sharp and able to cut through steel if given the time, unfortunately, it's way too small to use properly.", "A piece of bark from a fabled tree that never decays nor gets damaged it talks to you in a different language from a roster of 4 languages and it changes the language it speaks daily.", "A handbook that details all the different creatures from another world though you have never seen nor heard of any of them before or has anyone else.", "A tattered old hat you received from a beggar that when worn makes people want to avoid the wearer and or hurry past the wearer.", "A a violin you found clutched in the hand of a dead old man whenever you play it regardless of the tune it makes people incredibly sad.", "A small stone that feels like silk when you touch it.", "Half of a medallion that emanates dark power untold by mortals yet something feels missing from it like it's missing half of itself.", "Half of a medallion that emanates a sense of security and warmth yet something feels missing from it like it's missing half of itself.", "A pocket sundial that only works in the moonlight.", "The deed to an invisible hut — at least, that's what the merchant said.", "A song that cannot be played on any mortal instrument no matter how hard you try.", 
        "A riddle so tough just the sight of it makes even the most intelligent person frustrated at how hard it is.", "A a multitool with only one tool in it. That tool being a magnifying glass that has the words 'try to find the other tools' inscribed on it in Common. The magnifying glass itself gives the one using it more insight into what they are looking at through it.", "A ring that has -C'est inutile- inscribed on it, for some reason it makes you feel special when you wear it.", "A wand that when waved over anything that could be considered food makes it taste of mixed berries.", "A plate made of strange clay whenever something is eaten off it a growling noise is heard from somewhere nearby.", "Half of a cookie that, when eaten, causes another half of a cookie appears in an empty space nearby.", "A sandwich bag that has the words 'for panzer only' written on it. Inside the bag is a sandwich so perfect and mouthwatering but no matter what you are forced away if you try to eat the sandwich or remove it from its bag.", "A 3-foot cube box that causes bread placed in it for more than one minute to become toasted and buttered on one side.", "A scroll case full of ash. The lid has a tiny iron spike on the top.", "A woodcutter's axe that refuses to cut anything but wood.", "A small box with a button.When pressed a repetitive 30 - second tune will play. If the button is held down button for 20 seconds, it imprints a new tune.", "A jar containing two eyeballs peering with innocence at you with a label that reads 'Lithians treasure' scribbled in crayon.", "An eye patch of white stained leather with the word 'Skipper'on the inside.", "A silver ring with 'Dax <3 Mariva' inscribed on the inside. If you try and wear it, it slips off of your finger almost immediately.", "A deed to a bear sanctuary in another land.", "A locket containing a picture of an unrecognizable child.", "A bracer that is too hot to touch.", "A freezing cold gauntlet.", 
        "A map of an infinite labyrinth that is illegible.", "A book of ideas that will never be used.", "A miniature functioning siege set.", "A book of smut.", "A miniature canoe with what appears to be a dragonborn living on it.", "A captain's hat with the name 'sexy captain Alice' on the inside.", "An unfinished nude drawing of a man with an eye patch.", "A deflated rubber ball.", "A pamphlet preaching Nameless The Double Fae Gnome.", "A crude sketch of a goblin entitled Leanord.", "A necklace made from seven owl feathers.", "An unknown ancient relic that was forgotten through time.", "A half-built sled.", "A vial containing a small ember.", "A bubblegum scented sword.", "A bag of odd mushrooms.", "A statuette made from a coprolite.", "A book that details etiquette for acolytes of a major religion.", "A wand sized for a kobold.", "A whip crafted from ink-black leather.", "A hag's hairpin.", "A wrestling belt.", "A whistle that, when blown, makes you feel certain that there's a horse not too far away from you.", "A pair of undies with bats on them", "A crown made out of thirty broken spoons.", "A cabbage that cannot be eaten.", "A gold-painted rock.", "A tiny lizard skull.", "A pink scabbard that feels lighter than it actually is.", "A map to your ancestral home.", "A jester's hat.", "A harlequin mask that makes you feel oddly sad when you wear it.", "A pair of pumped up kicks.", "A shooting star contained in a bag.", "A coupon for a free hug from a king.", "A tiny hand carved from amber that flies around you and pokes people.", "A red boomerang that never comes backs to you.", "A tiny bit of a dragon's scale.", "A deed to a place that you made up.", 
        "A dented helmet that has an odd swirling design on the back.", "A book of myths.", "A cork that has a faint aroma of orange.", "A mushroom that smells of butterscotch and rots.", "A scabbard that smells of cheese.", "A trumpet that plays a mocking tune whenever you fail at something. You can't get rid of it.", "A set of very erotic undergarments.", "A jar full of petrified wasps.", "A hat that belongs to a violent marauder lord.", "A noble's journal, detailing his love affair with a goblin barmaid.", "A rusty speculum.", "A broken lute covered in bloodstains.", "A portrait of an incredibly muscular man wearing a short dress.", "A necromancer's reanimated pet frog.", "A platinum piece that merchants seem frightful of.", "A dagger that can't be removed from its sheath.", "A miser's coin purse. You just can't figure out how to untie the drawstrings.", "A pebble, delicately carved to resemble a dwarven mine baron.", "A flip book that depicts a cartoonish spine devil operating a riverboat.", "A beautifully crafted doll that belonged to a knight named Beirand.", "An undelivered letter addressed to a lord from the east. It simply states 'kill you' repeatedly.",
        "A child's wooden sword, with the names of several children carved into the side. It is completely bloodstained...", "An opium pipe made from beautifully carved jade. The name 'Lawrence' is inscribed at the bottom.", "A bit of slime in a jar. When the jar is opened, the slime tries its hardest to stay as far into the jar as it can, and something tells you you shouldn't touch it.", "A small bottle full of everlasting fire, when opened the sentient fire leaps onto whoever opened it and acts like a familiar; does not burn the owner, will attack anyone who threatens the owner of the fire.", "A music box that when opened plays strange music extremely loud.", "A journal with writing about the mass murder of orphans that lived at a temple, the murderer was never found; the writer seems to want revenge.", "An explorer's journal that goes very in depth of his discoveries while in his own house", "A small, sticky substance that is unidentifiable. Animals seem to enjoy eating it.", "A box full of green shirts, dresses, hats, basically anything clothes as long as it's green. Though, you have discovered a large pea in the corner of the box in the past.", "A necklace of obviously fake black pearls.", "Sheet music, with explicit instructions to play it using only sounds made by various animals instead of normal instruments.", "A blanket that makes anyone sleeping under it snore heavily for one hour, before flying off their body.", "A drum that makes someone within a 30 foot radius sneeze tremendously on every 7th beat.", "A book that translates anything you say into any language you wish, however it also adds in several random words, completely changing the meaning of whatever you say.",
        "A wise ghost that will give mildly helpful advice on occasion, but thinks its hilarious to play the bongos at inconceivable volume whenever you are trying to remain undetected.", "An extremely vulgar pocket watch that only shuts up when you wrap it in a special cloth that is fragile and can never be replaced.", "A lime-green sandal that is sized for a giant.", "A dung beetle the size of a pony that refuses to do anything but follow you, and push a gigantic wad of dung.", "A magic sphere that replays the most horrid-yet-catchy tune you have ever heard at random.", "A squirrel that will occasionally bring you nuts, but will hide any small objects or string you posses nearby just as often.", "An earring that will make you slightly more attractive to the opposite sex when pierced on your left buttock.", "A cup that remains totally unmovable from where it was set unless there is absolutely no liquid left inside of it.", "An elegant pair of shoes that make you run into walls on rare occasions.", "A perfect cube of polished, solid dirt.", "An artist's canvas that always appears to have mildly suggestive and socially unacceptable material portrayed on it, but is always masterfully done. The artwork changes at random.", "An endless, near-weightless bag, that produces only rubbish when you urgently need something specific from it. Will only produce items you have stored in it otherwise, but always at random.", "A ring that gives you the ability to command sheep in small numbers, but sheds dog hair in excessive amounts every 9 days.", "A jack-in-the-box that will always produces a somewhat disturbing illusion that changes every time you use it.", "A trusty sword of good steel that is haunted by several ornery, elderly, racist veterans of several different wars. They are almost always present, and they all hate each other.", "A walnut. There seems to be magical properties to it... maybe?", "A bag of salt. You have tasted a small bit of it, and amazingly, you can taste the magic in the salt, though it doesn't seem holy.", "A child-sized thumb. You don't recall how you got it, but you're sure you knew somebody who was missing a thumb when you were younger.", "An incredibly large ear that presumably belonged to a giant.", "A small slip of paper that reads 'Ce message n'est pas pour vous, imbécile.'", "The head of a polearm.", "A bag containing three history books so out of date they're not even written in modern Common.", 
        "A long list of miscellaneous items. There’s about 700 of them on the list.", "A pint of milk that never goes bad, but always tastes like it's not quite right. The pint bottle refills every day at the exact moment that the sun rises.", "A one-man band comprised of a drum, an accordion, a harmonica, a tuba, cymbals, and a horn. It seems to play whatever it wants though.", "A broken dagger with the last part of a name inscribed on the remaining portion of the blade. It reads '-dius'.", "A small blue-black orb that when held up to the ear seems to emit the tiny screams of a thousand souls.", "A hand mirror that holds the attention of anyone looking into it. You feel absolutely fabulous.", "A small device that when held right can be spun. It has three protruding limbs and other than spinning seems to be of no particular interest.", "A belt with a note accompanying it reading 'This belt shall give power to those that wear it.' It's buckle is missing and cannot be found.", "A small slip of paper with wishes on it. It will grant three wishes but will kill the person that makes the third wish. Two wishes have already been used.", "A sword made to harness the power of demon's blood. It seems the blood has since been returned to its rightful owner.", "A puzzle set that is missing a piece which never seems to be the same piece as last time.", "A scroll on which is inscribed a childish insult that isn't very amusing.", "A tiny cage containing a goblin that seems to hate you for something you apparently did to it despite never having seen or heard of this goblin until now.", "A tiny book containing a list of ships that have docked but have never existed in real life or in fantasy literature.", "A hardback blue book containing a list of every monster in the world and their exact demographics. The book seems very old.", "A metal butter container marked with the words 'Property of Professor Chaos.'",
        "A tin hat that is said to ward off creatures that steal your thoughts.", "A leather-bound diary that when written in will make the ink disappear and answer back before once more disappearing.", "An instruction manual that states what not to do in the events of potentially apocalyptic events.", "Three green diamonds made of cloth that attach to each other when put near each other but separate when placed near water.", "A cube made up of smaller cubes with images of even smaller cubes inside those cubes. It seems to keep going on and on.", "A fabric doll of a guard with an angry expression on it.", 
        "A tent that seems to get smaller and smaller with each use. Who knows how small it can actually get...", "A card game with monsters, traps, and spells on each card. Playing one makes a small image of it appear and when played against another monster will attack one another.", "A cube that plays a song from another time period. It doesn't sound like anything that has existed so far.", "A die with the classic six sides. It seems each face shows a different outcome constantly and rolling it will reveal that outcome. There seem to be an infinite number of potential outcomes.", "Toothpicks made of razor blades and broken glass. Who would even want to use this?", "A broken compass that seems to point away from your destination and doesn't seem to be able to be deceived.", "A piece of chocolate that tastes bitter with a sweet aftertaste, it burns your tongue when tasted as well.", "A weird brass pot that when opened reveals a hot steaming meal of great distaste to he who opens it.", "A bag of weird living figurines of everyone you know, including yourself, and they seem to be unable to see you despite your ability to interact with them.", "A weird yellow hat that belches into your ear when worn.", "A vial of vomit that smells like roses for some odd reason.", "A picture of the nastiest thing you have ever laid eyes on.", "A box of jewels with an inscription on the box with the end scratched off. It reads 'Elements of..' These jewels are powerful but seem to be unable to work.", "A giant cupcake that has been half eaten.", "A large sum of gold coins. Upon closer inspection they are made of bone, without looking so closely you'd never be able to tell they were fake", 
        "A metal bucket with an old note in it. It says 'Gentleman. This, is a bucket' followed by another note that says 'dear god' followed by yet another that says 'Wait, there's more' and finally one that simply says 'NOoo...' as if the person was in a state of disbelief.", "A thin metal box with images of people you hate and six bags of tobacco for smoking.", "A very scary painting of yourself that seems to age the longer you look at it. It resets by morning.", "A thing made of materials. None of this looks familiar to you in any shape or form and makes you very uncomfortable.", "A broken staff that partly disintegrates when it is touched, but always leaves some material behind.", "A plush toy of an owl with a label attached to it that reads 'Comet'.", "A tiny wheel of cheese with a hole in the middle.", "A loaf of bread made into the shape of a longsword that is stale.", "A picture that shows a random location you ask about in the general area, though it usually shows you perverted things as if it had a mind of its own. You feel its name is Jiraiya.", "A cow leather belt that allows you to speak with cows, yet makes you sheepish in the presence of sheep.", "A ring that seems to get smaller while you wear it.", "A hammer that whispers to you seductively in your sleep and takes pleasure in being used. You are usually creeped out by it.", "A bottle that contains an odd green liquid that floats on water.", 
        "A leather pouch that contains seventeen sewing needles.", "A letter that can barely be read, smudged by tears and withered by seawater, with the legible parts reading 'Cam.....ere..on..e'll b..hap...med.y....-N...'", "A baked clay figurine of a wide-eyed kobold with a bone in its mouth.", "A rudimentary deck of playing cards made on the backs of 'Wanted Person' leaflets.", "A thick leather belt with impressions and engravings depicting the stages of a moon.", "An old farmers almanac with pages cut to conceal small items inside.", "A highly-polished, palm-sized steel orb that always rolls downhill.", "A ship's flag that doesn't move in the wind.", "The fantastical skull of a rare hornless unicorn... or at least that's what the merchant who sold it to you claimed it was. He wouldn't have lied to you now, would he?", "An otherwise ordinary skull, if not for the third eyehole nestled in the center of its forehead.", "A scrimshaw depicting several northern nomads hunting a great elk, carved into the tooth of a saber-toothed tiger.", "A black ring covered with some very faint, illegible etchings that glow with a red light when in darkness. It feels somewhat warm to the touch when worn.", "The last baby tooth of a young giant, who lost it long ago.", "The skull of a wolf, peculiar for the rack of antlers sprouting from the top of its head.", "A small, mechanical bear that fits in the palm of your hand. It dances whenever music is played, yet no power source nor mechanism can be detected.", "A small wooden top that refuses to stop spinning, despite your best efforts.",
        "A sealed glass jar filled with a pale, reddish liquid. A small, deformed humanoid floats in the middle of it, and you swear that you can see it twitch whenever you are not looking directly at it.", "A note you found in your pocket one day instead of a pouch of coins. It only says 'IOU'.", "An odd torch that produces a blue flame yet seemingly no heat or light. At least it never goes out.", "A set of exquisitely crafted dice, carved from the tusks of a mammoth. Dwarvish runes replace the typical pips on the sides, and glow a faint blue.", "A vial of purple fluid that, when poured onto an inanimate object of size small or tiny, will cause said object to become translucent in appearance for one hour.", "An incredibly crude knife seemingly carved from a stone giant's toenail.", "A silver ring with runic etchings. In place of where a jewel would go, however, there is instead a small depression wherein rests an orb of green flame that never goes out but which also does not burn.", "A walking stick shaped from a gnarled elm root. A small branch is sprouting from it, tipped with several leaves.",
        "A sealed Ship in a Bottle, enchanted by a wizard. As you watch, the ship rocks back and forth as tiny waves crash about it.", "A small bird unlike any you've ever seen, trapped in a chunk of amber.", "A tumorous mass of flesh that squelches along the ground behind you, aided by a sinewy mass of veins and arteries that act akin to tentacles.", "A pewter armlet adorned with a pack of wolves engraved into its surface. When you rub your fingers lightly over it, the sounds of distant howls echo through the air.", "A gold stud earring that whispers completely useless facts into its wearer's ear.", "A silver pocketwatch that can correctly tell the time on whatever plane it is currently on.", "Small bits of nuts and fruit that seemingly never go bad and you cannot bring yourself to eat. Reminds you of a pet bird you once had.", "A blue flame in a jar that gives encouraging statements when you're feeling sad.", "A old box that used to contain your favorite poem. You're not quite sure where the poem went though you can remember having it just a few minutes ago.", "A gold nugget that merchants never seem to want to buy. You remember one merchant in particular who mumbled something about a curse after attempting to sell it to him, though you feel no effect.", "A sad looking wooden idol. It makes you and others around you feel sad just by looking at it.", "Three pairs of shoes that each wouldn't even fit a baby.", "Your favorite pair of socks. They're worn down and aren't worth wearing anymore.", "A painting about the size of your hand. It depicts a crudely drawn man holding a flower. Who drew this?", "A calendar with every day of the year labeled with the phrase 'CLEAN CLEAN IT ALL.'You never want to meet the person who did this.", "The leg of a chair that broke off with a friend of yours sitting in it. You remember using it as a fake weapon when you were young.", "Five identical pieces of wood. They're too perfect to use for anything.", "A poorly crafted clay animal. You can't quite tell which one it's supposed to be.", "A chalice with the words 'You drink too much' at the bottom of the cup.", "The cowl of a renowned thief. It seems to be cursed and you can't bring yourself to put it on.", 
        "The deed to a plot of land in the middle of the ocean.", "A small box full of miniature instruments. They all play quite beautifully in the hands of something that can play them.", "A map of a place that doesn't exist. You get a sinking feeling whenever you look at it.", "A poster for a play for the deaf. Everybody in the photo is wearing ridiculous masks to play different characters.", "A painting of the most horrid, obscene thing you've ever seen in your life. The brushwork and composition are impeccable.", "A book detailing the workings of a fake machine.", "A mask of an unknown person. His expressions seem too big for his face.", "A fabled lockpick that supposedly never breaks. It seems to have lost its power, however, as it had broken on the first use.", "Three thousand tiny hats that you almost can't see. You can only tell they're hats because you get a wizard to enlarge one for a short period of time.", "A tiny figurine of a wolf that whines when left alone.", "A miniature replica anchor that refuses to sink.", "The equivalent of two hundred million gold pieces in orange pieces of paper. They go to a game you played when you were little.", "A piece of string about 3 inches in length with a tiny, crude-looking shoe tied to one end made of wood that, when pinched, shocks you harmlessly.", "A clay bowl with a painting of a fingernail in it.", "A box full of childhood possessions. You can't seem to remember any of them.", "A small card welcoming you to a famous city. It has a letter on the back that's from a friend of yours explaining their experiences in the city.", "A large, metal wheel of cheese that always smells like the ocean.", "Three balls bound by a metal wire, one made of wood, one made of lead, and one made of flesh...", "A shred of paper that partially reads 'One for the dame, one fo-.'", "A love letter written by a beggar from your hometown. Funny, you don't remember being given this...",
        "A small cheat sheet that went to a test from school. It didn’t help much.", "An old, rusty and dull sword. It’s so dull it almost qualifies as a club.", "Protective eyewear. It’s a bit small for a human, but can fit perfectly on any other race, oddly enough.", "A long-winded and ultimately misleading report on the growth of peanuts.", "An almost lifelike painting of a bald, half-naked man holding fish in every appendage, including his mouth.", "A collection of figurines of every kind of dragon.", "An incomplete collection of cheese knives. There’s about seventeen of them in the container.", "A deck of cards that, when left alone for too long, will start shuffling and dealing themselves to all nearby people.", "A die with 7 sides made of bone. The side where '7' would be shown is instead replaced with a heart.", "A miniature piano that can fit in the palm of your hand but still plays and sounds exactly like a full-sized one.", "A petrified leaf.", "The bloody pointed tooth of a famous vampire.", "A loaf of bread you never ended up eating. It hasn’t gotten moldy, somehow.", "A small fluegelhorn that cannot be played correctly, even in the hands of a master.", "Eighteen miniature cabbage heads. They aren’t edible.", "An unreadable note. The only words you can make out are 'get the body bag Seymour.'", "A list of ingredients to make a potion that makes everything taste faintly of cauliflower.", "The ashes of your paternal figure.", "A singing bee. It. Doesn’t seem to mind being kept in a jar.", "A white cloak that cannot be stained by any means", "A witch's undergarments. Why do you have this?! Seriously!", "A beautiful sundress made by a blind seamstress", "A collar that fits any creature it is placed on. It's got the cutest little bell affixed to the front of it.", "A completely normal silk glove that you absolutely should not ask any questions about.", "A tiny dragon figurine that is animated when put in direct sunlight. It's very friendly.", "A painting of a baby that giggles when you look away from it.", "A journal containing stories of the owner's adventures with a bugbear", "A singular playing card. If you try to cheat with it, it laughs. It’s the ace of diamonds.",
        "A set of very powerful rattle snake magnets", "Five keys fused together in such a way that they could never open anything. You have nightmares of being burned alive whenever you sleep near it.", "A hypercube that dings lightly every eight days, eight hours, eight minutes, and eight seconds.", "A small chalkboard that can never be written on but shows a random word. If you ever try to erase it, a new word is shown.", "A tiny stone angel in an unbreakable glass box. It moves whenever you're not looking.", "A brown, thousand-page book with the word resurrection written a thousand times on each page.", "A random trinket that turns itself into another random trinket at every twenty-five hours.", "A ball of clay that grows a new eye every 1d4 hours. 1d4 hours later, that eye disappears. No matter what, the eyes are always staring into yours.", "A small golden bell with a red velvet ribbon and no ringer. The bells chimes very faintly when in the presence of royalty.", "A silver ring with an amethyst on it. It feels calming to put it on.", "Two sweet smelling branches. Smelling them for too long makes you nauseous and gives you a headache.", "A large skull of a were-chicken. Who knows how he got like that?", "A tiny decorative anchor that glows slightly whenever a nearby creature teleports.", "A brick that always feels slippery.", "A large snow globe that houses a tiny kobold and his family.", "A sacred chime that’s supposedly connected to faith and the gods.", "A pair of leather gloves that can never get wet.", "A singular strand of wire about three feet long. It shocks you frequently, even through something like leather.", "An old and blue greatsword. There seems to be some magical properties attached to it, though it seems lifeless. Perhaps something happened?", "Four jars with flaming butterflies inside. When broken, the butterflies ignite whatever it was broken over.",
        "A collar that fits perfectly around your neck, and no other creature's. You feel a powerful sense of forbearance in its presence.", "A septum piercing that causes the wearer to grow orc-like tusks.", "An earring that causes the wearer's ears to point in an elfish fashion.", "A golden tooth-cap that causes the wearer to grow a thick beard and/or chest hair.", "A mummified goblin hand.", "A piece of crystal that faintly glows in the moonlight.", "A diary written in a language you don’t know", "A gold coin minted in an unknown land..", "A brass ring that never tarnishes.", "An old chess piece made from glass.", "A pair of knucklebone dice, each with a skull symbol on the side that would normally show six pips.", "A small idol depicting a nightmarish creature that gives you unsettling dreams when you sleep near it.", "A rope necklace from which dangles four mummified elf fingers.", "The deed for a parcel of land in a realm unknown to you.", "A 1-ounce block made from an unknown material.", "A small cloth doll skewered with needles.", "An enormous scale, perhaps from a dragon.", "A tooth from an unknown beast.", "A bright green feather.", "An old divination card bearing your likeness.", "A glass orb filled with moving smoke.", "A 1-pound egg with a bright red shell.", "A pipe that blows bubbles.", "A glass jar containing a weird bit of flesh floating in pickling fluid.", "A small wooden statuette of a smug halfling.", "A tiny gnome-crafted music box that plays a song you dimly remember from your childhood.", "A brass orb etched with strange runes.", "A multicolored stone disk.", "A tiny silver icon of a raven.", "A bag containing forty-seven humanoid teeth, one of which is rotten.", "A shard of obsidian that always feels warm to the touch.", "A dragon's bony talon hanging from a plain leather necklace.", "A pair of old socks.", "A blank book whose pages refuse to hold ink, chalk, graphite, or any other substance for marking.", "A silver badge in the shape of a five-pointed star.", "A knife that belonged to a relative.", "A glass vial filled with nail clippings.",
        "A rectangular metal device with two tiny metal cups on one end that throws sparks when wet.", "A picture you drew as a child of your imaginary friend.", "Pallid leather gloves crafted with ivory fingernails.", "A lock that opens when blood is dripped in its keyhole.", "Dice made from the knuckles of a notorious charlatan.", "Clothes stolen from a scarecrow.", "A ring of keys for forgotten locks.", "A spinning top carved with four faces: happy, sad, wrathful, and dead.", "Nails from the coffin of a murderer.", "The necklace of a sibling who died on the day you were born.", "A key to the family crypt.", "A wig from someone executed by beheading.", "An bouquet of funerary flowers that always looks and smells fresh.", "An unopened letter to you from your dying father.", "A switch used to discipline you as a child.", "A pocket watch that runs backward for an hour every midnight.", "A music box that plays by itself whenever someone holding it dances.", "A winter coat stolen from a dying soldier.", "A walking cane with an iron ferrule that strikes sparks on stone.", "A bottle of invisible ink that can only be read at sunset.", "A flag from a ship lost at sea.", "A wineskin that refills when interred with a dead person for a night.", "Porcelain doll’s head that always seems to be looking at you.", "A set of silverware used by a king for his last meal.", "A wolf’s head wrought in silver that is also a whistle.", "A spyglass that always shows the world suffering a terrible storm.", "A small mirror that shows a much older version of the viewer.", "A cameo with the profile’s face scratched away.", "A small, worn book of children’s nursery rhymes.", "A lantern with a black candle that never runs out and that burns with green flame.", "A mummified raven claw.", "A teacup from a child’s tea set, stained with blood.", "A broken pendent of a silver dragon that’s always cold to the touch.",
        "A little black book that records your dreams, and yours alone, when you sleep.", "A small locked box that quietly hums a lovely melody at night but you always forget it in the morning.", "A necklace formed of the interlinked holy symbols of a dozen deities.", "An inkwell that makes one a little nauseous when staring at it.", "A hangman’s noose that feels heavier than it should.", "An old little doll made from a dark, dense wood and missing a hand and a foot.", "A birdcage into which small birds fly but once inside never eat or leave.", "A black executioner’s hood.", "A lepidopterist’s box filled dead moths with skull-like patterns on their wings.", "A pouch made of flesh, with a sinew drawstring.", "A jar of pickled ghouls’ tongue.", "A tiny spool of black thread that never runs out.", "The wooden hand of a notorious pirate.", "A tiny clockwork figurine of a dancer that’s missing a gear and doesn’t work.", "A urn with the ashes of a dead relative.", "A black wooden pipe that creates puffs of smoke that look like skulls.", "A hand mirror backed with a bronze depiction of a medusa.", "A vial of perfume, the scent of which only certain creatures can detect.", "A bag containing forty-seven humanoid teeth, one of which is rotten.", "A four-leaf clover pressed inside a book discussing manners and etiquette.", "A shard of obsidian that always feels warm to the touch.", "A sheet of parchment upon which is drawn a complex mechanical contraption.", "A dragon's bony talon hanging from a plain leather necklace.", "An ornate scabbard that fits no blade you have found so far.", "An invitation to a party where a murder happened.", "A blank book whose pages refuse to hold ink, chalk, graphite, or any other substance for marking.", "A bronze pentacle with an etching of a rat's head in its center.", "A silver badge in the shape of a five-pointed star.", "A purple handkerchief embroidered with the name of a powerful archmage.", "A knife that belonged to a relative.", "Half of a floorplan for a temple, castle, or some other structure.", "A glass vial filled with nail clippings.", "A bit of folded cloth that, when unfolded, turns into a stylish cap.", 
        "A rectangular metal device with two tiny metal cups on one end that throws sparks when wet.", "A receipt of deposit at a bank in a far-flung city.", "A white, sequined glove sized for a human.", "A diary with seven missing pages.", "A vest with one hundred tiny pockets.", "An empty silver snuff box bearing an inscription on the surface that says “dreams’’.", "A small, weightless stone block.", "An iron holy symbol devoted to an unknown god.", "A tiny sketch portrait of a goblin.", "A book that tells the story of a legendary hero's rise and fall, with the last chapter missing.", "An empty glass vial that smells of perfume when opened.", "A gemstone that looks like a lump of coal when examined by anyone but you.", "An ancient arrow of elven design.", "A scrap of cloth from an old banner.", "A needle that never bends.", "A rank insignia from a lost legionnaire.", "An ornate brooch of dwarven design.", "A tiny silver bell without a clapper.", "An empty wine bottle bearing a pretty label that says, 'The Wizard of Wines Winery, Red Dragon Crush, 331422-W'.", "A mechanical canary inside a gnomish lamp.", "A mosaic tile with a multicolored, glazed surface.", "A tiny chest carved to look like it has numerous feet on the bottom.", "A petrified mouse.", "A dead sprite inside a clear glass bottle.", "A black pirate flag adorned with a dragon's skull and crossbones.", "A metal can that has no opening but sounds as if it is filled with liquid, sand, spiders, or broken glass (your choice).", "A tiny mechanical crab or spider that moves about when it’s not being observed.", "A glass orb filled with water, in which swims a clockwork goldfish.", "A glass jar containing lard with a label that reads, 'Griffon Grease'.", "A silver spoon with an M engraved on the handle.", "A wooden box with a ceramic bottom that holds a living worm with a head on each end of its body.", 
        "A whistle made from gold-colored wood.", "A metal urn containing the ashes of a hero.", "A crystal knob from a door.", "A piece of paper with an undistinguishable face on it.", "A Compass that always points to Mulmaster.", "A book filled with writing that only appears when the book is held underwater.", "A paper fan that won't produce a breeze no matter how hard it's waved.", "A sealed envelope made of red leather that you haven’t been able to open. It smells of campfire.", "A petrified potato that resembles someone important to you.", "A locket of hair that is rumored to have come from a famed fire genasi.", "A glass cup that can only be filled half way no matter how much liquid is poured into it.", "Flint and steel that, when used to start a fire, creates a random colored flame.", "A mirror that only shows the back of your head.", "A blank piece of wet parchment that never seems to dry.", "A small glass bird that when set down near water dips its head in as if to get a drink.", "A small puzzle box made of brass, that is slightly warm to the touch.", "A lady's coin purse containing two sharp fangs.", "A cloudy chunk of glass that is said to hold a spark of breath from a blue dragon.", "A small sea conch with the words 'From the beginning' painted on the lip.", "A crude chalice made of coal.", "A frost-covered silver locket that's frozen shut.", "A miniature brass horn, silent when played, but fills the air with the scent of warm and exotic spices.", "A seal which imprints a mysterious, unknown coat of arms into hard rock.", "An eye-sized blue pearl that floats in salt water.", "A small wooden doll that when held brings back fond memories.", "A tuning fork made from a dark metal which glows with a pale, white light during thunderstorms.", "A small hand mirror which only reflects inanimate objects.", "A small vial that is always filled with the smell of autumn wind.", 
        "A glass eyeball that looks about of its own accordance, and can roll around.", "A clear marble that slowly rolls toward the nearest source of running water.", "A glass orb that replicates yesterday's weather inside itself.", "A small collapsible silver cup that perspires constantly when opened.", "A drinking cup, that randomly fills with fresh or salt water. Refilling once emptied.", "An hourglass that tells time with falling mist instead of sand.", "A deep blue piece of flint, that when struck with steel produces not a spark but a drop of water.", "An ornate razor, which only cuts in freezing cold temperature.", "A conch shell which is always damp and constantly drips saltwater.", "A shark tooth covered in tiny etched words from a lost language.", "A charred, half-melted pewter clasp that glows as if smoldering but releases no heat.", "A large brass coin with no markings or images on it.", "A clockwork finch that flaps its wings in the presence of a breeze.", "A small wooden box filled with a strange red clay.", "A unbreakable sealed jar of glowing water that hums when shaken.", "A necklace with a small, rusted iron anchor.", "A small, finely polished geode whose crystals slowly fade between every color of the spectrum.", "A small brass flute adorned with silver wire that is always faintly sounding.", "A rough stone eye pulled from a petrified creature.", "A red and black Aarakocra feather.", "A stone smoking pipe that never needs lighting.", "A palm-sized stone with a hole in it, through which can be heard a constantly whispering wind.", "A small whistle, that when blown, whispers a name of a person or place unknown to you, instead of the whistle sound.", "A small conch shell covered in black crystal.", "A fist sized rock that 'beats' like a heart.", "A small music box made of brass. It features a pair of tiny automatons that resemble Azer working at a forge.", 
        "A pair of bronze scissors in the shape of a pair of leaping dolphins.", "A glass jar containing the preserved corpse of an unfamiliar aquatic creature.", "A bronze oil lamp which is rumored to have once held a genie.", "A piece of petrified wood carved into the shape of a seashell.", "A single gauntlet inscribed with a fire motif and an unfamiliar name in Primordial.", "A wooden puzzle cube covered in elemental symbols.", "A one-eyed little fish inside a spherical vial, much bigger than the vial's neck. He has a cunning look.", "A small stone cube that acts as a magnet when placed against another stone.", "The tiny skull of a rabbit that whispers scathing insults when nobody is looking.", "A ring made of a white metal. On the inside is a name etched in Auran.", "A rag doll in the likeness of an owlbear.", "A bracelet made of silvered fish hooks.", "The desiccated body of a small eight-legged black lizard.", "A journal filled with poetry hand-written in Primordial.", "A small toy boat made with a walnut shell, toothpick, and piece of cloth.", "A yellow gemstone that glows dimly when a storm is nearby.", "A small pocket mirror that slowly fogs over while held.", "A charred chisel with an unfamiliar symbol stamped into its base.", "Wind chimes that glow when the wind blows.", "A canteen filled with a foul smelling orange mud.", "A small, clay square with an unknown rune etched into one side.", "A faceless doll made of driftwood.", "A tea kettle that heats itself when filled with water.", "A heavy iron key bearing the name of a ship long lost to the sea.", "An old scratched monocle which shows an underwater landscape whenever someone looks through it.", "A small jewelry box made from the shell of a turtle.", "A rose carved from coral.", "A chess piece fashioned to look like fire myrmidon.", "A set of dice with elemental symbols and primordial runes instead of pips or numbers.", 
        "A spinning top with an image of one of the four elements on each side.", "A amulet filled with liquid that churns, freezes, or boils to match its wearer's mood.", "A single hoop earring made of a porous red stone.", "A small silver bell that makes a sound like quiet, distant thunder when it's struck.", "An arrowhead carved from seasalt", "A small vial of black sand that glows slightly in the moonlight.", "A small comb made of blue coral.", "A small whale tooth with etched with an image of waves crashing upon a beach.", "Seven small beads of sandstone on a string, all different colors.", "An hourglass in which the sands pour upward instead of downward.", "A romance chapbook written in undercommon titled 'Just one Layer of Grey'.", "A glass pendant with a hole in the center that a mild breeze always blows out of.", "A tiny, broken clockwork Harpy.", "A soft feather that falls like a stone when dropped.", "An ivory whale statuette.", "A large transparent gem that, when gripped tightly, whispers in Terran.", "A fist-sized cog, covered in barnacles.", "A small crystal snow globe that, when shaken, seems to form silhouettes of dancing forms.", "An eyepatch made of obsidian and a black leather cord.", "Half of a palm-sized geode that pulses dimly with purple light.", "A glass bottle with a tiny ship of unfamiliar design inside.", "A small wooden carving of a jackalope.", "A bracket that changes colors depending on the day of the week.", "A pair of bronze earrings that show a hidden inscription when blood touches them.", "A white, sequined glove sized for a human.", "A small, weightless stone block.",
        "A vest with one hundred tiny pockets.", "A tiny sketch portrait of a goblin.", "An empty glass vial that smells of perfume when opened.", "A gemstone that looks like a lump of coal when examined by anyone but you.", "A scrap of cloth from an old banner.", "A rank insignia from a lost legionnaire.", "A tiny silver bell without a clapper.", "A mechanical canary inside a gnomish lamp.", "Ink and Quill, but the quill will not take the ink.", "A scabbard for a longsword with a 5-inch section of rusted steel blade inside.", "A gold ring that glows with strange runes when heated with a flame.", "A worn wooden plank that, after nightfall, makes the faint sound of a beating heart.", "A sealed glass jar of sourdough starter, given to you by an old woman two days ago.", "A copper coin that weighs 1 pound.", "A small wooden box with the word 'jail' burned into the side. Inside is are three worn dice made of bone.", "A belt pouch filled with dried catnip.", "A worn, but still strong, stick.", "A small wooden box that holds two identical, 1-inch diameter silver spheres inside.", "A rusted dagger, that no matter how much you try to polish it, is always rusted.", "An eyeball floating in a small jar of clear fluid. The iris reacts to changing amounts of light.", "A bottle of liquid with a paper label adhered to it. It bears only a single word, in gnomish: Oops.", "A large, perfectly red apple. It is carved from wood and painted.", "An apple, that when eaten, has the flavor of cinnamon already inside it.", "A small book of recipes. Every page, except for one, is stained from years of use.", "A deck of cards, with every card bearing a different crudely drawn, inappropriate image.", "A sealed glass jar containing what appears to be a pair of snake skins.", "A stack of 48 copper coins, tightly rolled up in a piece of paper. The paper is labeled with the number 50.", "A circle of wood, cut from a tree and stained, covered with hundreds of small holes and cuts on one side.", "A dagger, expertly carved from a single piece of wood.",
        "A flat, curved piece of wood that when thrown, either returns to your location or lands on the closest roof if it doesn't hit anything.", "A set of three eating utensils. The knife is etched with 'spoon', the spoon is etched with 'fork', and the fork is etched with 'knife'.", "A irregularly shaped pearl that always feels cool to the touch.", "A wooden cube etched with lines that divide each side into 9 squares. The squares are randomly painted in six different colors.", "A vial that appears to be filled with a potion of healing, but the liquid inside never comes out of the vial.", "A small, flat bladder with one opening that can be folded over to close it off. It makes embarrassing sounds when squeezed.", "A pouch with a dozen small, matching glass spheres inside. Stitched into the pouch is the name 'Gideon'.", "A covered basket that is just large enough to hold a single meal's worth of food for one person. It is always cold inside.", "A piece of polished amber with a 2-inch long mosquito preserved in the center of it.", "A single blue sock that never gets wet.", "A single red sock that is always warm.", "A book entitled 'The Meaning of Life ', which has only 1 page inside. The page is blank.", "A green crystalline key, which seems to be unbreakable and always sparkles in the least amount of light.", "A book of written gibberish, which has one line that clearly reads, 'It will happen in the City of Greed, when the Sun is Highest on the Longest Day.'", "A mummified duck foot.", "A bronze sword hilt that bears runes in an unknown language.", "A love letter written to the orcish warlord Durgak Stone-Fist, addressed from the high-elven princess Aleria Ulathi. You have no idea who either of these people are, but the letter is lovely.", "A lovingly crafted wand made from ivory an finely carved sequoia. It clearly held some great power at one point, but the cracked gemstone at the end implies that that magic is lost.", "A splinter from an outlander's shield, that when held fills you with courage and hope.", "A handheld cauldron, that always is a little hot.", "A cold but always lit candle.", "A colored piece of bread.", "A burnt and unreadable scroll given to you.", 
        "A uniquely colored pill.", "A palm - sized iron cage: the door doesn't shut properly, as the tiny lock was broken from the inside.", "An invitation to a formal ball to be held in two years time.", "A floating glass orb that follows you around and makes whirring sounds.", "A goblin-made key that can lock any door, but unlock none.", "A translucent coin, minted in an unknown land.", "A bronze ring engraved with dark symbols that was supposedly buried with a legendary necromancer long ago.", "A ring carved with the unfinished insignia to a defunct secret organization.", "A thimble on which is an enamel painting of a turtle.", "A puzzle box holding 10 fingernail clippings.", "A pair of badly worn hairdressing scissors.", "A bag filled with the smell of pastries.", "A small metal bell that seems to be missing the clapper.", "A genie’s golden arm bracelets.", "A single fiery strand of hair from a fire genasi.", "A crystal orb that sees into the past… two seconds ago.", "A piece of parchment, that reflects things like a mirror but in pencil, when you see your own reflection you feel unexplainable dread.", "A living drawing of a cow grazing.", "A silver coin that has heads on both sides. A deep scratch is etched into one side", "A red blindfold, covered in strange teal liquid", "A skeletal kitten in a jar. Any item placed near it and the edge of a surface is knocked over when nobody is looking.", "A glass orb filled with a tiny ooze. It has a sprite skull inside of it.", "A ash elemental in a bottle, made from the ashes of your dead grandfather.", "A wooden carving of a brain. It grows warm when you think hard enough.", 
        "A tea set in a traveling case. If you use the tea set, the tea will always taste a bit tart, regardless of how much sugar you add.", "A 6-inch maple wood ruler, finely engraved.", "An ugly woolen hat that's soft as a cloud.", "A beautiful miniature portrait of you and someone you don 't recognize.", "A small onyx statuette of a unicorn with red glass beads for the eyes. Something about it is unsettling.", "A feather that changes color when wet.", "A mosaic tile that glows softly.", "A single scissor blade. Where did the other one go?", "A palm - sized, circular wooden maze with a piece of glass covering it and a tiny metal ball inside.", "A red leaf that never decays.", "A paper menu from an unknown tavern.", "A gear made of an unknown material.", "A ceramic shard with what appears to be a dragon's head painted onto it.", "A very tiny journal with very tiny text written in Sylvan.", "A drawing of an unknown person that appears to stare at you no matter what angle you 're looking at it from.", "A small ivory statuette of a unicorn with blue glass beads for the eyes. Something about it is somewhat calming.", "A glass jar filled with seashells and beach glass.", "A tiny sun that produces no heat, and can make small pebbles orbit around it.It always floats a few inches above whatever surface it's on.", "A marble made of smoky quartz.",
    ]
    let trinketMagic = [
        [
            `of the Abyss - When on the plane of the Abyss, the bearer has advantage on saving throws against Abyssal Corruption. (DMG p. 62)`, `of the Acolyte - The bearer gains a +1 bonus to Wisdom (Religion) checks.`, `of Adamantine - The item is indestructible.`, `of Intellect - The bearer gains +1 bonus to Intelligence saving throws.`, `of Alarms - Contains 1d4 unreplenishable charges of the Alarm spell (1st level).`, `of Arborea - When on the plane of Arborea, the bearer has advantage on saving throws against the effects of Intense Yearning. (DMG p. 61)`, `of Arcadia - When on the plane of Arcardia, the bearer is unaffected by Planar Vitality (DMG p. 67)`, `of the North - The bearer suffers no harm in temperature as cold as -20 degrees Fahrenheit.`, `of Safety - Once per day, the bearer may use their reaction to reduce fall damage by 1d6 until the end of turn.`, `of the Assassin - The bearer may add their proficiency bonus to damage rolls dealt during surprise rounds.`, `of the Astral Sea - When travelling the Astral Sea, it takes half the number of hours to locate a Color Pool to a specific plane. You have advantage on saving throws vs. the effects of Psychic Wind (DMG p. 47-48)`, `of the Barbarian - The bearer gains a +1 bonus to Strength (Athletics) checks.`, `of the Bard - The bearer gains +1 to Charisma (Performance) checks.`, `of the Beastlands - When on the plane of The Beastlands, the bearer has advantage on saving throws vs. Beast Transformation (DMG p. 60)`, `of Beastspeakers - Contains 1d4 unreplenishable charges of the Speak with Animals spell (1st level).`, `of Benediction - Contains 1d4 unreplenishable charges of the Healing Word spell (1st level).`, `of Blasting - Contains 1d4 unreplenishable charges of the Fire Bolt spell (1st level).`, `of Blessings - Whenever bearer of this item receives divine healing, they gain an additional 1d4 hit points.`, `of Boldness - Contains 1d4 unreplenishable charges of the Heroism spell (1st level).`, `of Bounty - Contains 1d4 unreplenishable charges of the Goodberry spell (1st level).`, `of the Burglar - The bearer gains +1 to Dexterity (Sleight of Hand) checks.`, `of Bytopia - When on the plane of Bytopia, the bearer has advantage on saving throws against Pervasive Goodwill. (DMG p. 59-60)`, `of Carceri - When on the plane of Carceri, the bearer knows the direction to the closest secret exit from this prison plane. (DMG p. 63)`,
            `of the Lodestone - The wielder can use an action to learn which way is north.`, `of Cartography - On its own volition, the item records a map of the environments that the bearer is exploring, and can magically project it for the bearer to see.`, `of Channelling - Once per day, the bearer may ignore the Verbal and/or Somatic components of a spell they are casting.`, `of Chills - Contains 1d4 unreplenishable charges of the Ray of Frost spell (1st level).`, `of Gears - When on the plane of Mechanus, the bearer has advantage on saving throws against Imposing Order (DMG p. 66)`, `of Cloying - The bearer may cast Friends once per day.`, `of Compassion - Contains 1d4 unreplenishable charges of the Cure Wounds spell (1st level).`, `of Concordance - The bearer has advantage on saving throws vs. Psychic Dissonance when travelling the Outer Planes. (DMG p. 59)`, `of the Conjurer - The bearer may cast Prestidigitation once per day.`, `of Dissolving - Contains 1d4 unreplenishable charges of the Acid Splash spell (1st level).`, `of Vermin - The crawling things of the earth, such as insects, snakes, and vermin, are attracted to this item. When placed on the ground, such creatures will scurry toward the item like moths drawn to the flame.`, `of the Dancer - The bearer gains a +1 bonus to Dexterity (Acrobatics) checks.`, 
            `of Defence - Whenever the bearer takes a dodge action, they may move an additional 5 feet.`, `of the Delver - While underground, the bearer of this item always knows the item's depth below the surface and the direction to the nearest staircase, ramp, or other path leading upward.`, `of Last Chances - The bearer has advantage on perception checks when searching for items long lost in the the Swamp of Oblivion on the Plane of Earth. (DMG p. 54)`, `of the Druid - The bearer gains a +1 bonus to Intelligence (Nature) checks.`, `of Taverns - The bearer always knows the direction to the closest alcoholic beverage.`, `of the Dynamo - The bearer has +1 to Charisma saving throws.`, `of Eavesdropping - As long as it is on the same plane, the bearer can hear through this item as if they were present.`, `of Elysium - When on the plane of Elysium, the bearer has advantage on saving throws against the effects of Overwhelming Joy (DMG p. 60)`, `of Ethereal Shores - The bearer can see creatures in the Border Ethereal that overlap with their plane as clearly as if they were fully in the bearer's plane. Such creatures appear as apparitions or ghosts.`, `of Exaltation - Contains 1d4 unreplenishable charges of the Bless spell (1st level).`, `of Expedience - Contains 1d4 unreplenishable charges of the Expeditious Retreat spell.`, 
            `of Falsehoods - The bearer gains a +1 bonus to Charisma (Deception) checks.`, `of Tongues - Contains 1d4 unreplenishable charges of the Comprehend Languages spell.`, `of the Favored - Once per day, the bearer may roll a saving throw with advantage.`, `of Feathers - Contains 1d4 unreplenishable charges of the Feather Fall spell (1st level).`, `of the Fey - The bearer knows the general direction to the closest Fey Crossing within a 60 mile radius. (DMG p. 50)`, `of Speed - The bearer gain a +1 bonus to initiative rolls`, `of Forgiveness - When on the plane of Mount Celestia, the bearer of this item can receive the benefits of Blessed Beneficence regardless of their alignment.`, `of the Fortune Teller - Every time you are hit by a monster, you glimpse a random image of its future or past.`, `of Friendship - Contains 1d4 unreplenishable charges of the Animal Friendship spell (1st level).`, `of Gehenna - When on the plane of Gehenna, the bearer has advantage on saving throws against Cruel Hindrance. (DMG p. 63)`, `of Grace - The bearer may cast Spare the Dying once per day.`, `of Coercion - The bearer gains a +1 bonus to Charisma (Intimidation) checks if the target can see this item.`, `of Hades - When on the plane of Hades, the bearer has advantage on saving throws against Vile Transformation. (DMG p. 63)`, `of Harmony - Attuning to this item takes only 1 minute.`, `of Healing - This item contains 4 weak healing nodes. As an action, a character can use one node to heal 1d4 hit points at touch range. The item regains 1d4 charges at sunrise.`, `of the Nine Hells - When in the Nine Hells, the bearer has advantage on saving throws against Pervasive Evil. (DMG p. 64)`, `of Heroes - The bearer has advantage on saving throws vs. fear.`, `of Histrionics - the bearer gains +1 to Charisma (Performance) checks.`, 
            `of Faith - When the bearer of this item rolls hit dice, they can choose to re-roll them and take the second result.`, `of Symbols - The item is inscribed with holy symbols of the God of the DM's choice. A cleric or paladin that serves that god may use this item as a divine focus.`, `of the Inquisitor - The bearer gains a +1 bonus to Intelligence (Investigation) checks.`, `of Inspiration - The bearer regains their Constitution modifier in temporary hit points whenever they gain or use inspiration.`, `of Leaping - Contains 1d4 unreplenishable charges of the Jump spell (1st level).`, `of Lies - Contains 1d4 unreplenishable charges of the Silent Image spell (1st level).`, `of Limbo - When on the plane of Limbo, the bearer has advantage to Intelligence checks to alter or move non-magical objects within the plane. (DMG p. 61-62)`, `of Locating - Once attuned, the bearer always knows the exact location of this item`, `of the Silver Tongue - The bearer gains +1 to Charisma (Persuasion) checks.`, `of Malediction - Contains 1d4 unreplenishable charges of the Bane spell(1st level).`, `of Manipulation - The bearer may cast Mage Hand once per day.`, `of Servants - Contains 1d4 unreplenishable charges of the Unseen Servant spell (1st level).`, `of the Maverick - The bearer has a +1 bonus to any skill check involving gambling and games of chance (Insight, Sleight of Hand, Investigation, etc).`, `of Messages - The bearer may cast Message once per day.`, `of Falling Stars - Contains 1 unreplenishable charge of Scorching Ray (1st level).`, `of Mindfulness - The bearer gains a +1 bonus to Wisdom saving throws.`, `of Miracles - The bearer may cast Thaumaturgy once per day.`, `of Mockery - The bearer may cast Vicious Mockery once per day.`, `of Nature - Contains 1d4 unreplenishable charges of the Locate Animals or Plants spell (1st level).`, 
            `of Neutrality - Contains 1d4 unreplenishable charges of the Protection from Good and Evil spell (1st level).`, `of Agility - The bearer gains a +1 bonus to Dexterity saving throws.`, `of Nourishment - The bearer rarely feels hungry, and only needs to consume one-fifth the usual amount of food.`, `of Pandemonium - When on the plane of Pandemonium, the bearer has advantage on saving throws against the Mad Winds. (DMG p. 62)`, `of the Preacher - The bearer may extend the range of their Channel Divinity by 5 feet.`, `of Projection - The bearer can send messages mentally to willing characters within 30 feet. This communication is one-way only.`, `of Protection - The bearer may cast Blade Ward once per day.`, `of the Reaper - The bearer has advantage on death saving throws.`, `of the Renaissance - Once per day, the bearer may gain +1 to any skill check.`, `of Revelation - Contains 1d4 unreplenishable charges of the Detect Magic spell (1st level).`, `of Rituals - Whenever the bearer casts a spell as a ritual, they have advantage to maintain concentration during the ritual.`, `of the Sacred - The bearer may increase their Lay on Hands hit point pool by 5.`, `of Acumen - The bearer gains +1 to Wisdom (Insight) checks.`, `of the Sage - The bearer gains a +1 bonus to Intelligence (History) checks.`, `of Secrets - Contains 1d4 unreplenishable charges of the Illusory Script spell (1st level).`, `of the Sentinel - Faintly glows when creatures of a certain race (DMs choice) are within a 100 foot radius.`, `of Shade - The bearer suffers no harm in temperatures as high as 120 degrees Fahrenheit.`,
            `of the Shadowfell - The bearer knows the general direction to the closest Shadow Crossing within a 60 mile radius. They have advantage on saving throws vs. Shadowfell Dispair (DMG p. 51-52)`, `of the Shepherd - The bearer gains a +1 bonus to (Wisdom) Animal Handling checks.`, `of Shielding - This item contains 1d4 unreplenishable charges of the Shield spell.`, `of Shifting - The bearer may change minor aspects of the physical appearance of this item.`, `of the Night - The bearer gains a +1 bonus to Dexterity (Stealth) checks.`, `of Reparations - The bearer may cast Mending once per day.`, `of the Sojouner - A poem, story, or map that describes a long-forgotten treasure is etched on the surface of the item.`, `of Solemnity - The bearer may spend an action removing all the failed death saving throws from a target within 5 feet of them. The target is still not stabilized.`, `of Lights - The bearer may cast Dancing Lights once per day.`, `of Strides - Contains 1d4 unreplenishable charges of the Longstrider spell (1st level).`, `of the Surgeon - The bearer gains a +1 bonus to Wisdom (Medicine) checks.`, `of the Tenacious - When the bearer takes a long rest, they gain back one additional hit die.`, `of the Tracker - The bearer gains a +1 to Wisdom (Survival) checks.`, `of Translucence - The bearer gains an extra level one spell slot, which recovers only after a full moon rises.`, `of Trickery - The bearer may cast Minor Illusion once per day.`, `of Truth - The bearer may cast True Strike once per day.`, `of Heart - The bearer gains a +1 bonus to Constitution saving throws.`, `of Druidcraft - The bearer may cast Druidcraft once per day.`, `of Victory - Whenever the bearer kills a creature they gain temporary hit points equal to the creature's CR.`, `of Vigilance - The bearer gains +2 to their Passive Perception.`,
            `of Vigor - The bearer gains a +1 bonus to Strength saving throws.`, `of Vitality - The bearer's maximum hit points increases by their constitution modifier while attuned to this item. These hit points are lost when the bearer unattunes the item.`, `of the War Leader - The bearer can use an action to amplify their voice so that it clearly carries for up to 300 feet.`, `of the Sea - The item floats on water or other liquids. Its bearer has advantage on Strength (Athletics) checks to swim.`, `of the Labyrinth Wind - When in the Plane of Air, the bearer can navigate the Labyrinth Wind intuitively, and knows the path to the nearest Earth Mote within 60 miles.`, `of the Wizard - The bearer gains a +1 to Intelligence (Arcana) checks.`, `of Ysgard - When on the plane of Ysgard, the bearer is unaffected by Immortal Wrath. (DMG p. 61)`,
        ],
        [
            "The item becomes branded with the icon of courage. This person receives advantage on intimidation checks", "The item becomes imbued with necrotic energy, making it partly undead. The item can deal an extra 1d8 of necrotic damage but becomes useless against radiant beings", "The item becomes imbued with chaotic energy, the user can tap into this energy with a bonus action and become imbued with chaos, doubling damage for 3 turns but taking half their max health from their current health. The user can be killed by this effect.", "The item becomes sanctified by angels, when swung will release a cone of radiant energy that gets stronger the further it travels (base damage for the cone is 1d8. +1d8 for every 10 feet travelled, up to 50ft.)", "The item becomes vampiric. When coated in blood the item will regenerate the users hit points by 4d4 per round but the item will become permanently useless in the sunlight.", "The item becomes branded with the language of the gods. If the celestial language is known, these words can be spoken to ‘summon a phoenix under the control of the user. (one phoenix max)", "The item warps into an unnatural shape, the user may roll a d20. On a natural 20 the user may pick one opponent within its line of sight to violently explode.", "The item becomes imbued with radiant energy, creating a magical protection ward around the user making them immune to magical projectiles on the use of an action.` (physical projectiles imbued with magic will lose their magical properties but continue through the ward.)", "The item becomes possessed by the ghost of a fallen medic. You may roll a D20, on a 15+ any living thing the item touches will heal for 4d4", "The item gains three spark charges. When used, any damage dealt by the item will be doubled. Once the last charge is used and resolved the item explodes into a fireball 15ft in diameter", "The item becomes spectral, it becomes useless against corporeal entities but deals an extra d10 damage to spectres and ghosts", "The item becomes branded with spiral runes. Anything the item harms becomes totally unaware of the events that took place in the last five minutes.",
            "The item gains the ability to transform into a stone wall of cover (5ft. wide by 3ft tall). Activating this effect destroys the item", "The item becomes branded with the hymns of kyne. If the user can read elvish and utters these words, they will be able to deal an extra 1d8 of damage to animals until a long rest.", "The item gains the ability to harness the effects of the weather. (If it is raining, the blade instantly kills beings made of pure fire, thunder adds 1d8 of lightning damage to the weapon, the sun sets the blade ablaze adding 1d8 of fire damage and snow coats the blade in ice that can fire an ice spike using a bonus action)", "The item cracks and splinters. Plunge the blade into the ground and roll a d20. If 17+, roll a d10. The number rolled from the D10 dictates the magnitude of earthquake that will result.", "The item begins to glow a bright white, lighting up even the darkest of caverns brightly enough to be able to see normally (50ft. range).", "Imbues an item with ancient dwarven runes. If the dwarven language is known, these runes can be spoken and summon dwarven spirit armour, which adds a 2+ to their armour class.", "The item begins to resonate. On a death blow the item absorbs the targets soul. Once five souls have been absorbed the item can emit a soul charge, a ball of soul energy deals 5d10 of damage to everything around the user, but not the user, in a 20ft radius.", "The item becomes imbued with the power of ultimate siphon revivify. The item can touch a corpse and return it to life, at the cost of 100 hit points from the user.", "The item turns grayscale in colour and becomes branded with an emblem of the moon. Under the moon, the item deals an extra 1d10 of lunar damage, 2d10 against animorphs.", "The item begins to ooze green slime. This slime is a highly toxic poison. On a successful hit the target must make a constitution save (DC16). On a failed save, the target will take 3d4 damage for 3 turns. This effect does not stack.", "The item gains five mana restoration charges. Pointed at a target with in 50ft and used, it will regenerate one of the targets spell slots. If the target cannot recover spell slots the charge is wasted.", "The item becomes fused with the user through stone like growths and imbues the user with the power of the stone knight. A blow that would normally kill the user would instead leave the user with one hit point", 
            "The item becomes one with shadows and by extension, its user. Encompassed in a dark mist the user can activate this effect once per hour to disappear into any shadow they can move to without a trace.", "The item triples in size and fills the user’s muscles with the power of a giant, forcing them to triple in size. Their strength becomes 25, but their dexterity is reduced by 4.", "The item can tap into the heavens itself. Roll a d100, if the number is 90 or higher, summon a random angel. The item loses any magical property after this effect is resolved.", "The item begins to glow slightly blue, it becomes clairvoyant and will warn the user through telepathy of impending danger, it cannot discern the magnitude of danger, just that there is danger nearby.", "The item is branded with the emblem of a dagger and gains the ability to fire daggers by using a bonus action. If the user would like to use a whole action to fire this dagger, the fired dagger becomes a great sword, gaining the swords damage stats.", "The item begins to be orbited by three different coloured spheres, one red, one blue and one yellow. The red sphere will restore 50 hit points. The blue sphere restores one spell slot. The yellow sphere spawns 100 gold.", "The item becomes decorated in red glowing stripes and gains the ability to fire flares at will. If the flares hit a target, they deal 1d4 damage. On a hit, roll a d20. On a natural 20 the target is set ablaze dealing 5d10 damage per turn.", 
            "The item becomes warped into the shape of a spiral and grants the user the ability to cast one shot of wild magic per long rest.", "the item begins to grow jagged teeth all over adding 1d4 of damage to the item. On a death blow the item absorbs the targets soul. Once five souls have been absorbed the item will restore the user to max health", "The item becomes so heavy only those with a strength of 25 or above can wield it, but all hits with this weapon are guaranteed, regardless of AC.", "The item becomes branded with the emblem of a hooded figure, DEX saves are done with advantage.", "The item becomes coated in black flames. On a successful hit, whatever it touches must succeed a wisdom saving throw (DC 14), if it fails the target becomes friendly for one turn. This effect only works once per target.", "The item becomes branded with the emblem of a smiley face. Charisma checks are done with advantage", "The item becomes covered with leaves and branches and gains the ability to calm any animal creature its pointed at. The twigs add an extra +1 AC if the item is a shield, piece of armour or a creature.", "The item turns from its original material into enchanted magma. The magma cannot damage the user but deals an extra 2d8 of fire damage to a target. Once per long rest the blade can summon a magma mephit under the control of the user.", "The item begins to radiate an unknown energy. The item can now create minor illusions, any target that would be fooled by the illusion must make a wisdom saving throw (DC15), on a success the target is not fooled by the illusion.", "The item is swarmed by flies. On a successful hit, anything the item touches must make a constitution saving throw, on a fail, the target is incapacitated with sickness for one turn.", "The item is branded with words of courage, when spoken, the user makes all allies immune to fear and intimidation checks", 
            "The item is filled with the energy of the god the user serves. Anyone who serves another god gains disadvantage on initiative. If the user serves no god, the item turns feral, the user has disadvantage on all combat-based rolls", "The item becomes two times lighter. The user gains the fast hands reaction. If an attempted hit should miss, they can reroll the hit.", "The item thins out to an arrow tip somewhere on its form. The user may now activate its one arrow charge to bring down a hail of arrows upon the entirety of the battle field. Everyone in combat must make three DEX saves, any fails and the target will take 1d8 damage per fail. Once the charge is used the item returns to its original form and loses its magical properties", "The item becomes shrouded in a white mist. The user can tap into the item and turn spectral at will.", "The item can now turn into a bow at will. Firing spectral arrows that require nothing to create. The arrows deal 2d4 damage and will always find their mark, regardless of AC", "The item gains a voodoo doll attachment. Roll a d20 per target while in combat. On a 19 or 20 the user gains total control of the target so long as that target is below a challenge level of 10. When combat ends the target dies. One target per combat.", "The item is branded with the words “sword breaker”. If the item misses an attack, roll a d20. On a natural 20, the targets weapon is shattered into dust.",
            "The item becomes branded with the vow of calamities. When the vow is uttered everyone in the area must make a constitution save (DC5). On a failed save, the targets suffer massive internal organ failure, dealing 10d10 damage. Every time the vow is uttered, the user is permanently deducted 20 hit points.", "The item becomes decorated with golden spines and celestial runes. Should a member of the party be permanently killed by a hostile attack. The user can sacrifice the item and save their life, restoring them to 1 hit point.", "The item becomes coated in a thin layer of mucus. This mucus can be bottled once per long rest. Should a bottle of mucus be emptied on a target, the target begins to become encased in the mucus. The target must make a strength saving throw (DC13) to pull the mucus off. After a certain number of turns based on the targets size, the target will become encased in the mucus totally, incapacitating the target. The target then has three turns to be freed before being dissolved in the mucus. (tiny creatures: 1 turn/small creatures: 3 turns/medium creatures: 5 turns/ large creatures: 10 turns/gigantic creatures: 20 turns)", "The item becomes decorated in tentacles. The item receives 3 tentacle charges. Each charge deploys a grappling tentacle from the item that can pull the target towards the user on a failed strength check (DC15).", "The item becomes swathed in magical wrappings. If the user activates the power of the item using an action, all allied spell casters gain an extra plus five to hit for one turn.",
            "The item gains the emblem of despair. The target may summon a wraith for the duration of the battle that’s under the control of the user (one wraith max)", "The item becomes shrouded in the faces of lost souls. The user may activate the item, using an action, to open a portal to the soul cairn, allowing the lost souls to pull one target to its realm. The target must succeed a strength check (DC 5) to stay within the material plane.", "The item is given the seal of lesser reincarnation. This seal may be removed and placed on the skull of a corpse to bring back a zombie under the control of the user.", "The item grows an eye. The item can now deploy this eye as a scout within 50 meters of the user. If the eye is damaged or destroyed, the item is also destroyed", "The item becomes possessed by a deep voice that speaks to its user of dishonourable deeds. The item becomes doubly powerful against unarmed opponents", "The item becomes possessed by an ancient wraith king. Any undead allies gain advantage on all hit rolls", "The item becomes decorated with three porcelain hands. The user can discharge one of the hands as a mage hand.", "The item becomes wrapped and surrounded with horned vines. Any attack made with the item that would intend to trip, disarm or incapacitate deals an extra +1d4 damage and is done with advantage.", "The item begins to glow with all the colours of the rainbow. You gain a +2 to your charisma stat while using the item and gain advantage on persuasion rolls with characters of the same gender.", "The item becomes fused with a large gold piece worth 1000 gold. The item can now fire gold pieces, using gold in the user’s possession dealing 1d4 damage, if the fired coin lands a kill shot, the target explodes into a multitude of valuable items", "The item is imbued with the soul of a former bard. The item now boosts the user’s charisma stat by 1 and grants advantage on all charisma-based rolls", "The item gains a small gun barrel somewhere on its form. This gun comes with five ancient seeds of Gaia that when fired into a target, they will instantly sprout. Roll a d10, the number rolled will determine how many d10s of damage will be dealt.",
            "The item partly turns to stone. When the item deals damage to a target, the target must succeed in a constitution saving throw (DC5) or be permanently turned to stone", "The item becomes imbued with the energy of the unwoven. The user may command the item to reduce the enemies hit points by as many as they choose, however the user will take an equal amount of damage", "The item becomes branded with the words of the vampire king. It has one vampiric singularity charge. The user can sacrifice the item to create a vampiric singularity. Everyone in the battlefield must make a DC 15 dexterity saving throw to prevent themselves being pulled into the red ball. Anyone pulled in is instantly killed, once all dexterity saves have been made, the remaining parties gain health equal to the sum of the killed creatures hit points as the ball dissipates", "The item becomes wrapped in black linin. The curse of the mythic assassins has been lain upon you. When initiative is rolled, you must roll a d20 for everyone in the battle. If you roll a natural 20 for anyone, you teleport to them dealing 10d6 worth of damage but if you teleport to more than 3 people, you are banished to another plane of existence.", "The item becomes a stein of beer. This is the stein of never-ending mead. No matter how much you drink, you can’t seem to finish your glass", "The item transforms into a spoon. This is the sliver spoon of the snow elves. When placed into the mouth of a target, feeds them a mouthful of their favourite food.", "The item becomes magically connected to Gaia, the god of nature. When pointed at the ground the item will begin to grow a tree. How long the item is pointed at the ground dictates how large the tree will be", "The item gains the symbol of stamina. This symbol grants the user 10 extra feet of movement and proficiency in athletics and acrobatics", 
            "The item becomes infested with insects. It has five insect charges. When a charge is spent, the battlefield becomes infested with a swarm of insects chosen by the user. Everyone must succeed on a DC 12 constitution save or be incapacitated with fear for a turn", "The item becomes braded with the emblem of terror. When activated the user can begin to place marks of madness on a target. The target must succeed in a (DC10) wisdom save or have a mark of madness placed on them. If three marks of madness a placed on a target they become feral, attacking anything nearby. If the target succeeds any of these saves, they are immune to the emblem of terror for 24 hours.", "The item begins to glow white hot. The item can now refuge any broken blades and amour at a single touch.", "The item becomes tethered to the user through an umbilical cord. This connection allows the user to spend 10 points of their own lifeforce to grant the item an extra +10 to all damage they deal, but if the cord is severed the user takes 10D10 damage and the item is destroyed.", "The item becomes fused with the scythe of the burning mother. The scythe does 4D6 slashing damage and a further 4D4 burning damage.", "The item becomes fused with mechanical technology from the far future. A fusion core is placed on the weapon, charging it with nuclear energy. The item can now fire a beam of energy that can travel 130ft. and deal 5D8 radiant damage. However, if the core is damaged it will explode in a 20ft. sphere, dealing 10d10 radiant damage to everyone inside.", "The item becomes consumed by pestilence. When the item is pointed at a target, using an action, a cloud of flies consumes them, incapacitating them for a turn.", "The item grows a mouth. this mouth can perfectly replicate anyone’s voice but only on a performance check (DC7).", "The item becomes reflective. If two living things share the same reflection their minds are swapped for 1D4 days.", "The item is now orbited by white orb. This is the orb of protection against the night. The user can activate this orb to ward off any evil targets within a 20ft. cone, so long as the target is below a challenge level 7. Can be used once per long rest.",
            "The item turns partly to bone. The target can choose one skeletal entity within their line of sight to crumble into meal. Can be used once per short rest.", "The item gains the seal of the unbound. Should the user become bound or unable to move, using their action they can free themselves from their bindings.", "The item gains the ability to enter the astral realm and bring its user with it. The user can astral project themselves up to 100ft. in any direction. The user cannot be seen, take damage or deal damage while in this state and once the enchantment is broken or the range exceeded, the user is returned to their original position.", "The item becomes fused with a hypodermic needle somewhere on its form. Should a target be stuck with this needle, they must succeed on a constitution save (DC14) or be paralyzed for 1d4 turns.", "The item turns black and its texture becomes course. It has been possessed by shade. Should the user take damage, half of the damage taken is reflected at the target.", "The item becomes branded with the words of the ultimate masque. Wave the item in front of your face to change your appearance for an hour.", "The item becomes lined with green, pulsating veins. Should the item be embedded in a target for 3 turns, the target’s blood becomes poisoned. This poison deals 20 points of damage per turn until the target dies or the blade is removed.", "The item gains the blessing of the reborn ribbon. Placing the item upon a fallen ally will instantly revive them to full health but will destroy the item", "The item is branded with the image of a key. Touch the item to any conventional lock to open it instantly.", "The item becomes slender, elegant and beautiful. Its user is infatuated with the item and will refuse to replace it with any other. should the user kill a target with a challenge level of 20 or higher, increase their charisma by 1.", 
            "The item’s colour turns to a mix of dark greens and blues while a sinister grin appears somewhere on its form. The user gains 2 extra attacks.", "The item becomes jagged and turns black. Its gains the sin of wrath. Once per long rest, the item can unleash a lighting bolt upon a target. If a hit, roll a D100. If its 90 or higher, the target is immediately killed. If its 50 – 89, the target takes 5d12 damage. If it is 2 -50 the target is incapacitated for a turn. If it is a 1, the user is immediately killed.", "The item turns green and its form begins to bubble. Should a target possess something the user desires, the item can be sacrificed to create an exact replica of the desired object.", "The item turns a deep red colour, becomes slender and smooth and oozes an unfamiliar red fluid. Once per long rest, the user can call upon the item to turn themselves into a succubus for one hour.", "The item becomes heavy and much larger. Only those with a strength of 18 or higher can use the item. Should the user be on full health, death blows will grant 20 temporary hit points.", "The item begins to exude black smoke. The user’s movement speed is decreased by 5. When the item is pointed at the target a beam of smoke will connect the target to the weapon. While this connection remains uncut, reduce the targets strength by 2 per turn. If the targets strength reached 0 before they can break the connection, they will wither away and die. If the connection is broken, the target is restored to full strength instantly and cannot be targeted again.",
        ],
        [
            "Reflective. Once per day, when a creature you can see deals radiant or fire damage to you, you can force them to make a DC 14 Constitution saving throw or be blinded until the start of your next turn.", "Misty. The item appears to be light and diaphanous, as if made from pure mist. It weighs half as much as it normally would.", "Sonorous. Whenever you score a critical hit the item emits a ringing noise audible within 300 feet of you.", "Temporal. At dawn the item looks to be brand new and in pristine condition. At dusk it looks weathered, old and broken.", "Gluttonous. While the item is on your person you no longer need to eat, but you feel constantly hungry.", "Mechanical. The item is adorned with moving gears and quietly beeps and whirs at random intervals.", "Piscine. Part of the item is transparent and filled with water. A tiny immortal fish is present in the water, and counts as part of the item for the purposes of targeting.", "Steaming. The item is hot to the touch and gives off steam when in use.", "Clairvoyant. As a bonus action you can focus on the item and gain a +2 bonus to your next attack roll or ability check. You cannot use this ability again until the next dawn.", "Phoenix. When you drop to 0 hp but aren't killed outright, you can choose to regain 10 hit points and deal 10 fire damage to all creatures in a 10 foot radius of yourself. The item then permanently loses this property.", "Tallying. Each time you kill a creature a new mark is added to a tally on this item's surface.", "Edible. You can spend 1 minute eating this item. It provides enough nourishment to sustain you for 1 week.", "Timekeeping. You always know the exact time and date of your current location.", "Bestial. You gain fur, sharpened teeth and elongated ears while this item is worn or wielded.", "Avian. You can subtract 10 feet from your total distance fallen when calculating fall damage.", "Guide. You gain a +1 bonus to all ability checks made to avoid getting lost.", "Light Eater. This item is pitch black. As an action you can surround yourself with 10 feet of non magical darkness until the start of your next turn. You cannot do so again until the next dusk.",
            "Nostalgic. You always know your exact distance from the place you first found this item.", "Blossoming. Touching this item to a non-magical flower causes the flower to blossom.", "Colourful. If you have darkvision, you can discern colour in darkness.", "Menacing. While this item is being worn or wielded your voice becomes deeper and your eyes glow red. Once per short rest you can give yourself advantage on a Charisma (intimidation) check.", "Ominous. The item constantly whispers indecipherable messages to you and is covered in untranslatable runes.", "Positive. The item constantly whispers words of encouragement to you. Once per short rest you can give yourself advantage on a saving throw made against being frightened or possessed.", "Extraplanar Repellent. This object's presence is repulsive to aberrations, celestials, elementals, fey and fiends. It offends all of their senses.", "Fiendish. While the object is on your person, you can speak and understand Infernal and Abyssal and abilities and spells that detect or sense creature type detect you as a fiend.", "Celestial. While the object is on your person, you can speak and understand Celestial and abilities and spells that detect or sense creature type detect you as a celestial.", "Fey. While the object is on your person, you can speak and understand Sylvan and abilities and spells that detect or sense creature type detect you as a fey.", "Imaginary. To creatures other than yourself, those with true sight or those with a Wisdom score of 14 or greater, this item is invisible.", "Heart Breaker. Once per turn you can deal an additional 2d6 psychic against a creature charmed by yourself or an ally when you damage them.", "Immortal. Each dawn roll a d20. On a 20 your life span increases by 1 year.", "Fate Tied. If you die this item is completely destroyed.", "Stoic. Any injuries you sustain are invisible unless you willingly reveal them (no action required) and you barely bleed, even when severely injured.", "Companion. An illusory tiny animal of the DM's choice follows you, remaining in your space. You can dismiss it or resummon it as bonus action.",
            "Searing. As an action you can touch this item to a flammable object not being worn or carried to set the object alight.", "Well Rested. Whenever you finish a long rest you gain 1 temporary hit point and your movement speed increases by 5 feet for 1 hour.", "Empathetic. Dealing damage while in possession of the item causes harmless pain to course through your body.", "Clean. This item functions as an endless bar of soap.", "Armed. As a bonus action you can transform this item into a dagger or a shortsword. The item then loses all properties but this one until you use a bonus action to change it back.", "Alerting. This item emits a harmless shock every 6 seconds, which wakes you up if you were involuntarily put to sleep.", "Solemn. Whenever a creature within 30 feet of you dies, this item briefly turns black and emits the sound of tolling bells.", "Accounting. You can touch this item to a pile of gold, silver or copper coins within a 5 foot cube to convert them to their equivalent value in gold, silver or copper coins.", "Doubled. When you speak you produce 2 voices, and your movements produce a brief after image.", "Forecast. As an action you can ask the item for a weather forecast. It then produces an illusory image representing the predicted weather in your area over the next 8 hours.", "Enlightened Rest. Whenever you fall asleep or spend at least half an hour meditating with this item, you levitate 3 feet off the ground. This effect ends immediately if you wake up or end your meditation.", "Inspiring Defiance. When you succeed on a death saving throw, a creature of your choice within 30 feet of you that can see you gains 1d4 temporary hit points.", "Bloodthirst. Whenever you deal damage to a humanoid, beast, monstrosity, giant or dragon they spill copious amounts of blood no matter the severity of the wound. This additional blood spillage does not harm or otherwise effect them.",
            "And Everything Nice. This item is covered in and produces magical flakes. You can use these flakes to flavour food, drink or objects to be sweet, salty, or spicy (your choice).", "Squeaky. Whenever this item strikes an object or creature, or is squeezed, it produces a squeaking noise that can be heard up to 10 feet away.", "Shadow. Peering into this object causes you to see a twisted reflection of yourself. Its expression is the exact opposite of your own when you look into it.", "Folded. Multiple seams run across the item's surface. It can be folded up to be a quarter of its size for compact storage.", "Handy. This item has a magical compartment containing a 10 foot pole, 50 feet of rope and a single gold piece. This compartment cannot store anything else.", "Strong Aura. Creatures capable of casting 3rd level spells or above are made instantly aware of the item's presence, but not exact location, if it's within 100 feet of them.", "Breezy. This item emits a perpetual soft breeze.", "Starry. This item is covered in a pattern of stars. This pattern is the same as the formation of stars in the night sky over your current location.", "Cloudy. This item has a solid colour surface with images of clouds moving across it. The colour of its surface is the same as the colour of the sky over your current location.", "Liquid. This item appears to be made almost entirely out of liquid. You have advantage on Dexterity (stealth) checks if you are wearing the item and you are completely submerged.", "Absorbent. If you place this item in a non-magical liquid it can absorb a volume of the liquid equal to the volume of a 5 foot cube over the course of 1 minute. You can release the stored liquid as an action and can only store 1 liquid at a time.", "Adhesive. Pressing this item upon a solid surface or object not being worn or carried causes them to stick together.",
            "Gravitational. Once per short rest, you can use an action to brandish this item and cause all unrestrained objects with 20 feet of you to be pulled 10 feet closer.", "Masculine. Wearing, wielding or using this item causes you to instantly grow thick facial hair, even if your race is normally incapable of doing so.", "Spacial Warp. Once per long rest, you can use a bonus action to choose an unoccupied space within 10 feet of you. Until the end of your turn you can attack, cast spells or interact with objects as if you were standing in that space.", "Seasonal. This item changes slightly to match the seasons, for example emitting a warm glow in summer or becoming pale and cold in winter.", "Reforming. If this item is destroyed by taking damage, it reforms in the same space in 1d4 hours.", "Far Sight. You can use an action to gain the ability to see 5 times as far until the end of your turn.", "Western. Every so often tumbleweed blows past the bearer of this item then disappears.", "Chew Toy. Beasts find this item extremely pleasurable to chew on.", "Eldritch. This item is covered in several writhing tentacles and emits ominous phrases in Deep Speech when used.", "Mood Sense. This object changes colour depending on its bearer's mood.", "Heart. This object pulsates at regular intervals like a beating heart. The rate of beating increases when its bearer successfully charms a creature or if they become charmed or frightened.", "Heroic. This item's bearer receives regular thoughts of slaying dragons and protecting innocents.", 
            "Official. You can use a bonus action to manifest a sheet of paper that declares the item's bearer as its official owner.", "Censoring. Whenever the item's bearer speaks a curse word or insulting phrase, their words are replaced with soft music.", "Panacea. You can use an action and touch a creature with this item to restore 5 hit points, cure a disease or remove the poisoned condition. You can do each of these only once, then this item loses this property.", "Dense. This item is inexplicably heavy. It weighs twice as much and causes the area in a 30 foot radius to shake harmlessly when dropped onto the ground.", "Photosynthetic. While this item is on your person you can sustain yourself by spending 1 hour in natural sunlight rather than eating or drinking.", "Calculator. This item has a small keypad and illusory screen that can be used to carry out calculations.", "Oathsworn. An oath is inscribed on this item. The item glows warmly when its bearer abides by it.", "Orbital. The item's bearer can choose for this item to orbit around them, in their space. Any other creature that attempts to remove it must succeed on a DC 14 Strength check to do so.", "Royal. This item bears the crest of the nearest noble or royal family. If none, or multiple, are present it picks one at random.", "Unstable. Whenever this item or its bearer takes damage it violently shifts in shape and size for several seconds before returning to normal.", "Planar. This item glows in the presence of portals to or artifacts from other planes.", "Dream Bound. Whenever this item's bearer dreams or experiences a vision, the item appears in the dream or vision with them.",
            "Pathological. Each dawn this item generates a blatantly false statement somewhere on its surface.", "Power Word. You can speak a word engraved on the item's surface as an action, causing all fiends, undead, celestials, fey, aberrations and elementals within 300 feet to be made instantly aware of your exact location. The word then disappears.", "Recipes. This item's bearer gains the knowledge of how to cook 3 meals of the DM's choice.", "Eloquent. This item can be used as a quill. Words written with it are written with perfect handwriting.", "Drab. Wearing or wielding this item causes you to see colours as more dull and less saturated.", "Levitating. When not being worn or carried this item floats 1 foot off the ground.", "Masterwork. This item looks impossibly well made. You have advantage on all ability checks made to convince people of its worth, quality or power.", "Forgetful. When left unattended or out of sight for at least an hour this item always ends up about 10 feet from where it was last seen.", "Birdcall. This item's bearer can communicate simple ideas and emotions to birds.", "Fail-Safe. When you are subjected to a spell that allows you to make a saving throw to take only half damage, you can use your reaction to take half damage if you fail. This property is then lost.", "Storm Born. Neither this item nor its bearer gets wet when it rains or snows.", "Ironclad. This item is made from heavy metals. Its bearer has advantage on saving throws made against being pushed, pulled or knocked prone.", "Pure Evil. Abilities and spells that detect creature type, alignment or magic detect this item as a Chaotic Evil Fiendish creature emanating Necromantic magic.", "Bastion of Good. Abilities and spells that detect creature type, alignment or magic detect this item as a Lawful Good Celestial creature emanating Abjuration magic.", "Druidic. This item is made from wood and covered in vines. Its bearer can understand Druidic.", "Void. This item appears as if it were made from writhing purple energy. Each minute it does 5 force damage to non-magical objects it's touching that aren't being worn or carried.", "Ocular. This item is covered in many constantly shifting, unblinking eyes. While holding or wearing it you gain a +1 bonus to perception checks and initiative rolls.", "Indecisive. Roll for two more properties, rerolling if you get this one again. This item switches between those two properties each day.",
        ],
        [
            "You learn a cantrip choosen by the DM", "You gain proficiency with improvised weapons", "Once per short rest when you get hit by a weapon attack, you can use your reaction to decrease the damage taken eual to your proficiency modifier", "You have advantage on perception checks when keeping watch on a long rest", "Shops always give you a small discount", "You gain a +1 to a skill check chosen by the DM", "You tend to stay dry no matter the situation", "You can get advantage on distracting others", "You only need to eat every couple days", "You can sense an item is magical when you have it in your hands", "You may use your Wisdom modifier instead of Charisma when making a persuasion check to solve a situation diplomatically", "You get +2 to charisma based checks while speaking one of you languages other than common (choosen by the DM)", "Whenever you would gain temporary hp, you gain 2 extra", "You gain +2 on intimidation checks to hostile targets", "You can convert raw food, such as meat or plants into rations", "When you trigger a trap, there is a 10% chance (1 on a d10) the trap will malfunction and not work", "You can try casting augury once per day while you long rest, it has a 50% chance of the spell not working", "If you try to surpise the target but fail, you have advantage on the initiave roll for that combat", "You gain proficient with one tool or gaming set (DM chooses)", "If you roll a 20 on a dex saving throw, a target within 5ft of you gain advantage on that same save", "You gain gain darkvision of 30ft or if you already have darkvision it increase its range in 15ft", "You gain +2 on deception checks if you can provide anecdotal evidence of your claim", "Once per day, whenever you use your hit dice to recover HP during a short rest you can reroll one of the die", "You and your allies can travel faster outdoors (outside of combat)", "You gain extra 5ft of movement", "You only need half the usual time to craft a non magical item", "You can hold your breath for 1 minute longer than you normally would", "Whenever a monster resist a damage you've dealt (including saving throws sucesses) you round the damage up instead of down", 
            "Whenever you would gain a level of exhaustion you can do a con save with disadvantage DC15, if you pass you don't get that level of exhaustion and the dc increase by 5 (the dc resets after a long rest)", "If you take damage that would reduce you to exactly 0hp, you get reduced to 1hp instead", "Your death saving throws also crits on a 19 rolled", "If you roll a 1 on a death saving throw, you only get 1 failure instead of 2", "If you hit an enemy with a critical hit, you and all the allies within 30 ft that can see you gain 2 temporary hit points", "You gain proficiency in a laguage (choosen by the DM)", "Have a spell permanently added to your prepared list, and it doesn't count against the number you can prepare each day", "You only need 4 hours or sleep to complete a long rest", "If you are attacking from 10ft or more above the target, you get +2 on attack rolls", "You get +2 on checks with gaming tools that you are proficient with", "Advantage on Con saves for drinking alcohol", "You can communicate basic ideas silently, through hand signals and body language", "You can sleep with medium/heavy armor without penalty", "You can draw or stow an additional item as part of an object interaction action", "Your maximum hit points increase by 2", "You can cast spells from a spell scroll even if its not in your class spell list by passing a arcana check DC 10+ (2x the spell level)", "Everyday that you spend in the wilds you have 20% chance of salvaging enough herbs for a healing potion, but you still need to spend time crafting the potion", "If your attack surpass the enemy AC by 10 or more, you do extra 2 damage", "You have +1 on skill checks involving monsters of a particular type (Choosen by the DM)", "If you are below 8hp, you can add 1d4 damage to any damage you cause. (max once per turn)", "When you wake up from a successfull long rest you get 2 temporary hp and +2 on the first roll skill check of the day", "You can move an extra 10ft when you use the dash action", "You are immune to ingested poison", "You can carry extra 60lbs", "You can identify a potion with a tiny taste of it", "A spellcaster hireling, hired to cast a spell of level 4 or lower as a service will upcast the spell by one level without charging extra (once per day)", "A horse or another non-evil beast of CR 1/4 or lower (determined by the DM) take a likeing to you and will obey you outside of battle", 
            "You can permanently lose proficiency in one skill of your choice and permanently gain proficiency in another skill of your choice that you have made a check for in the last 7 days", "You can recover more ammunition after fights", "If you wake up from a long rest in a room which you had to rent (inn/tavern/hotel/etc) you wake up to a single goodberry on your pillow. From a tiny beast that admires you", "It takes one minute for someone other than you to be able to open your backpack", "Once per combat you can give a creature advantage on save throws against aoe spells cast by their allies (friendly fire) as long as none of the allies are under a charm effect", "Once per combat, when you take the attack action and miss every attack, you can do one extra attack as a bonus action but this extra attack has a penalty to equal to twice your proficiency modifier to a max of -10", "Once per combat you can use an action to spend a hit die to heal.", "Once per day, you can treat a level 1 spell with range of 'self' as 'touch' if you spend a lvl 2 spell slot without the benefits of an upcast", "Once every 5 days, if you find a treasure with at least 50gp worth of coin, you can roll 1d20 and find that many more gold pieces", "You got to fail 4 death saves (instead of 3) to die", "You can roll initiative adding your wisdom modifier instead of dexterity", "You have advantage on initiative rolls if you are outnumbered at least 2-to-1", "Once per day you can add a 1d4 to one roll, you can choose to add after the roll but before knowing the result", "Once per day you can have advantage on a skill check but you have to declare you are using it BEFORE the roll", "Creatures do not bother your body while unconcious for 1hr (no atacks while down)", "If you drop to 0hp but is healed, creatures assume you are still unconcious untill you take a turn", "Any magical items that have charges and are attuned to you, have one extra maximum charge.", 
            "You gain advantage on smell related perception checks", "You get a +2 bonus to charisma checks 'against' dedicated arcane users (wizards, sorcerers, etc.)", "You get a +2 bonus to charisma checks 'against' dedicated religious people (clerics, priests, etc.)", "You can estimate counts really well, with a quick glance you can have an aproximation of any coin or other contable objects (example: if a pile has 280 coins in it you know with a glance it has 'bit less than 300'. But you cannot count things like stars, which are uncountable)", "When you take fall damage, you take 1d6 less than you normally would", "When you flip a coin you have 60%(12/20)chance of being right instead of 50%", "Your unarmed attacks do 1d4+str dmg instead of just 1+str", "You can use your dexterity score (instead of str) to determine high and long jump distances", "While surprised you have +2AC", "Once per day, if you or an ally that you can see take a critical hit, you can use your reaction to decrease the damage dealt equals to your proficiency modifier", "Once per day you can attempt to use the divine intervention feature, with 5% chance of working. The Deity favor is lesser but still there. Once you sucessfully use this feature you cannot use it again", "If you miss a ranged attack against a target you have 5% chance of hitting an enemy behind the initial target.", "You can't critical fail attacks, as long as you still meet the target's AC you still hit", "If a target is huge or bigger, you don't have disadvantage with range attack thems if they are prone", "If you an attack match your AC exactly, you are still hit but are resistant to the weapon damage for that attack only",
            "Everytime you get healed in combat, you get healed by extra 2hp", "Attacks of opportunity against you have disadvantage if you use the dash action", "If you use the shove action you can shove an enemy up to 15ft, instead of the normal 5ft", "If you are fighting 1v1 and there are no extra enemies or allies causing damage to the target or you and there are no concious enemies or allies withing 50ft of you. You can choose to have advantages on all your attacks for the turn but if you use this feature, the enemies will also have advantage on attacks against you until the start of your next turn", "Once per long rest, whenever you cause damage, you can increase that damage by your proficiency modifier", "If a healing spell would heal enough for you to go over max hp, the remainning hit points become temporary hp up to an max equal to your proficiency modifier", "On the first turn of combat, as long as your were not surprised, you can drink a potion as a bonus action", "You cannot become undead by any means", "You have +2 against save throws to curse you", "Being critically hit while at 0 hp only gives you 1 failled death save, instead of 2", "If you are frightened you can still move towards the source of your feat but a max of 10ft", "If you surprise your enemies, you can use the dash action as a bonus action", "When a non magical effect would cause you to be restrained you are considered grappled instead",
        ]

    ]
    

    let output = searchArray([`${searchArray(trinket)} Due to it's history, this trinket is considered to be imbued with the magic ${searchArray(trinketMagic[0])}`,`${searchArray(trinket)} ${searchArray(trinketMagic[1])}`, `${searchArray(trinket)} This trinket is magical: ${searchArray([`${searchArray(trinketMagic[2])}`,`${searchArray(trinketMagic[3])}`])}`])
    document.getElementById("Trinket").innerHTML = output
};
function findGrimoire(){
    let author = [
        `by precursors or the inhabitants of a previous reality`, `the work of a deity, saint or otherwise somehow divine in origin`, `a powerful mage or other form of spell caster`, `a(n) ${searchArray(['illithid', 'aboleth', 'neogi', 'beholder'])}`, `${searchArray([`a(n) ${searchArray(['celestial', 'fiend', `${searchArray(['elemental','genie'])}`, 'fae'])}`, `someone possessed by a(n) ${searchArray(['celestial', 'fiend', `${searchArray(['elemental','genie'])}`, 'fae'])}`])}`, `the culmination of the efforts of generations of scholars`, `a person that was taken by a eerie mood and wrote the work in a fortnight`, `nobody... it merely appeared one day, fully formed`, `by a doomed poet who dove deep into a mystery cult for inspiration`, `by a scholar who claimed to have tapped into the Akashic Records, where all knowledge is stored`, `by a popular medium while in a trance, shortly before their mysterious disappearance`, `by a priest who became obsessed with dubious apocrypha`, `by an unknown authour. It simply appeared in history one day`, `by an entire village, one page to a person, before they walked together into the night, never to be seen again`, `by a thousand deranged monkeys`, `by the head doctor of an asylum, based on the rantings of their patients`, `by the hands of an infamous thief, after they were cut off as punishment`, `by a historian based on their collated research on several lost civilizations`, `by a child who claimed to have been inspired by their imaginary friend`, `some time in the future. What you might find of it now is an imperfect, backwards copy anticipating its own original`, `shamefully, by a secret heresiarch`, `apparently long before any other example of written language`, `by a self-proclaimed prophet who claimed to have received its text in a god-granted vision`, `by a hermit best known for throwing their feces at visitors`, `by a jaded noble who brought ruin to their estate in pursuit of limit-experiences`, `by a professor and their closest students, who barricaded their university and slaughtered the rest of the inhabitants`, `as a bowdlerization of a yet more dreadful tome`, `by the hands of the true creator of the world, allegedly`,
    ]
    let form = [
        `tablets made of ${searchArray([`${searchArray(['stone','clay'])}`, 'metal', 'wax', 'wood'])}`, `tome bound in ${searchArray(['leather', 'metal', 'ivory', 'loose sheaves'])}`, `scroll crafted of ${searchArray(['paper', 'hides', 'leaves', 'cloth'])}`, `graffiti, scrawling or runes etched onto a ${searchArray(['structure', 'natural feature', 'path or road', 'cave'])}`, `tangles of intricate ropes and beads in a language that may not still be known. may be read in the dark`, `a puzzle box or similar device. The secrets within are whispered into the mind of those who solve it`, `scrimshaw upon the bones of a(n) ${searchArray(['humanoid', 'outsider', 'aberration', 'monster'])}. may be read in the dark`, `woven into the fabric of a(n) ${searchArray(['article of clothing', 'tapestry', `${searchArray(['blanket','quilt'])}`, `${searchArray(['tent','yurt'])}`])}`, `a tome bound with a cover made from human teeth and nails`, `a tome that was inked with the discoloured blood of inhuman beasts`, `a tome that is a mere fragment of a greater work, all that could be preserved from a purge`, `a tome that is, or has become, a living creature. Its pages pulse with a faint heartbeat, and absorb unwary worms for sustenance`, `a tome that has synaesthetic text, words that are smelled or felt more than read`, `a tome that changes its exact wording each time it’s read`, `a tome that always appears in the dreams of those who’ve read it before, where it remains perfectly legible`,
        `a tome that will pluck at the strings of fate to place itself in the possession of ambitious sorts if it’s sealed away for too long`, `a glass puzzlebox which projects its text when a light is shone through it. Rearranging it reveals another segment of text`, `a tome that has increasingly deranged marginalia scribbled in a dozen different hands in its open spaces`, `a tome that makes you speak its words aloud as you read it, someone else’s voice coming from your throat`, `a tome that appears to be written in gibberish until you add your signature to the many that fill its otherwise blank front page`, `a tome that glows with a sickly light, so that it is legible even in total darkness`, `a tome that seems fated to injure its readers. One can scarcely turn a page without getting a papercut`, `a tome that has a section of actual human spine as its spine`, `a tome that is fireproof, and can only be read in full by immolating it`, `a tome that causes its reader’s eyes to bleed. Reading it too much inflicts blindness, as readers become unable to see anything but the grimoire`, `a stack of clay tablets. There’s more tablets in the stack than it seems there should be based on its size and weight, and any tablets removed or destroyed inexplicably return to the stack`, `a tome that heals any damage done to it, leaving a mottled scar`, `is written in a code that takes sustained effort to crack. Without this effort, it seems to be a mundane cookbook`,
    ]
    let lore = [
        `the true names of ${searchArray(['celestials', 'fiends', 'genies', 'fae'])}`, `exhaustively indexed knowledge on an extremely niche topic such as elven architecture or goblin poetry. Worth a small amount to most, but a huge sum to the right collector`, `a creeping form of madness which provides insight into the world. In exchange for losing one's mind permanently, the bearer of the work may ask it questions and gain answers 1d6 times per day as if they were using the spells find the path, augury, identify or clairaudience`, `a compendium covering the habits and weaknesses of ${searchArray(['outsiders', 'aberrations', 'magical creatures', 'undead'])}`, `the true and secret history of a ${searchArray(['major empire', 'noble family', 'trade league', `${searchArray(['faith','cult'])}`])}`, `prophecies relating to the ${searchArray(['end of the world', 'death of a deity', 'fall or destruction of a major empire', `death of a famous ${searchArray(['warlord', 'archmage'])}`])}`, `insight into a complicated and fraught magical process such as ${searchArray(['summoning outsiders', 'alchemy', 'reviving the dead', 'creating constructs such as golems'])}`, 
        `detailed accounting ledgers of a ${searchArray(['trade league', 'noble family', 'guild', `${searchArray(['town','city'])} council`])}`, `rituals to summon demons, though not to control or banish them`, `secrets to mix potions which induce mutation`, `the secret names of angels, which allow them to be bound against their will`, `the location of a dormant undead army and the means to command it`, `secrets to open portals to inchoate realms beyond the conventional cosmos`, `knowledge of how to enslave human souls to animate fell golems`, `rituals to transform oneself into ${searchArray(['a vampire', 'a ghoul', 'a lich'])}`, `a tragically flawed ritual to resurrect the dead`, `spells to cook together living things into hybrid monsters`, `rites to commune with a banished and vengeful divinity`, `a rite to shuck one’s own dooms, curses, and misfortunes onto a more innocent scapegoat`, `instructions on how to slip one’s soul away from just punishment in the hereafter, or damn another to far worse than they deserve`, `rituals to transfer your mind into another’s body, consuming their self in the process, or to splinter off pieces of your mind to fester and infect another’s`, `secrets to call up plagues, but not how to cure them`, `the method to create a sphere of annihilation`, `instructions to immanentize the eschaton`, `knowledge of how to remove human organs and replace them with empowering alien substitutes`, `secrets to steal life-force from others to enhance and extend one’s own`, `charms to bend the minds of others`, `secrets to steal and pervert divine magic`,
    ]
    let forbidden = [
        `so that its temptation to prospective seekers would be increased`, `not for the lore it contained, but rather for its satirical preface which offended a political leader`, `because hidden in its text is a memetic weapon that drives readers mad`, `because its cover forms a seal that unleashes a malign spirit while it is open`, `because it’s a failed attempt at a phylactery, and so its writer(s)’s ghost(s) can haunt anyone who’s read it`, `because it was used to facilitate an atrocity`, `due to the blasphemous ideas its text promulgates`, `because none of its lore is accurate, and is in fact a trick for an even darker purpose`, `because reading it is a spiritual hazard that dooms one’s soul to a truly unfortunate afterlife`, `because it’s proof of the limits of safe, sane magic`, `because of the machinations of a sorcerer who thought it plagiarized their own work`, `because it was once the key element in a plot to hasten the apocalypse`, `because the lore it contains could destabilize the natural order of things`, `because prophecy held that great evil would follow if it were not kept out of sight of perusing eyes`, `because the gods have a habit of smiting indiscriminately around it`, `by a tyrant who didn’t want anyone else to be able to tap its power`, `because as it’s read it refines and expands on itself by reading in turn the minds of its readers`, `because the publishing house that owns the rights to it gets violently litigious if there’s any chance it might be copied`, `as an excuse to seize it for an authority’s use`,
    ]
    let location = [
        `locked up in the archives of a scholastic monastery`, `in the hoard of a dragon who gathers knowledge rather than gold`, `in a parasitic, paradimensional library that siphons the collection and readers of other libraries`, `in the study of a libertine aristocrat`, `as the centrepiece of a mystery cult`, `in a sealed chest in a mermaid’s sea-cave, looted from a shipwreck`, `chained to the wrist of a cenobite-censor`, `within the wooden shell of a filing-golem`, `in the possession of a cult transcribing it onto woodblocks for printing and widespread distribution`, `through a map encoded in an occultist’s notes`, `clutched in a dead wizard’s desiccated claws`, `in the lab of a researcher trying to extract insights palatable to conventional magical practice`, `in a revolutionary’s hideout, as a weapon of last resort`, `as the heirloom of a clan of backwoods hedge-witches`, `in a tower on a barren island, its garrison all dead of simultaneous suicide`, `sorted among mundane codexes by a senile bureaucrat`, `locked in a safe in an inquisitor’s office`, `in the possession of an orphan being groomed by a loose familiar to become an obedient archmage`, `in a decrepit sanctum, guarded by a vampire awaiting the return of their master’s reincarnation to claim it`, `in the ash-piles of a failed book burning`,
    ]
    let defense = [
        `it animates a mouth upon its surface and bites those who try to read it without the proper password. 1d6+3 bludgeoning damage. It bites again every 2d10 rounds`, `it lets out a blood-curdling scream and flies away at 60' turn if read anywhere except ${searchArray(['under the stars', 'within a chamber with no natural light', 'upon unworked earth', 'a place of spiritual significance'])}`, `it is locked. If an attempt is made to force it open it begins to weep gallons upon gallons of ${searchArray(['blood', 'ink', 'water', 'ichor'])}`, `the work is a keystone or plug of sorts, if removed or reproduced then ${searchArray([`the area containing the work shakes itself to bits in ${3+rollDice(6)} minutes`, 'undead begin to appear around where the work is held', 'animals of all stripes become hostile to whomever bears it', 'bad luck follows the bearer', `the player gets disadvantage on ${1+rollDice(3)} rolls per day at the DM's discretion`])}`, `a cult or religious order is dedicated to safeguarding the work in some way. If it is stolen of copied without consent then they will surely seek to rectify the situation`, `a guardian is magically bound to defend the work in some way until their destruction, the guardian is a powerful ${searchArray(['undead creature', 'outsider', 'monster', 'construct'])}`, `only certain type of folk are able to read the work, it is gibberish to everyone except ${searchArray(['non-spellcasters', 'followers of an obscure faith', 'the mad', 'someone who has never taken a life'])}`, `the work itself is famous. While there is no one specifically looking for it, the very news of it changing hands may attract unwanted attention to those who now have it`,
    ]
    let output = `A legendary grimoire in the form of ${searchArray(form)}, and its authorship is ${searchArray(author)}. This grimoire is rumored to contain ${searchArray(lore)} and it was forbidden ${searchArray(forbidden)}. You can find this grimoire ${searchArray(location)}, and it has defense in that ${searchArray(defense)}.`
    document.getElementById("Grimoire").innerHTML = output
};
function findRing() {
    function ringBuilder(){
        let material = [`gold`, `white gold`, `tarnished silver`, `polished silver`, `gold-plated brass`, `silver-plated brass`, `gold-plated steel`, `silver-plated steel`, `brass`, `black steel`, `bone`, `ivory`, `ebony`, `mahogany`, `walnut`, `turquoise`, `jade`, `iron`, `copper`, `platinum`,]
        let gemstone = [`diamond`, `blue diamond`, `pink diamond`, `yellow diamond`, `ruby`, `fire opal`, `white opal`, `black opal`, `yellow opal`, `green opal`, `emerald`, `blue sapphire`, `purple sapphire`, `pink sapphire`, `star sapphire`, `garnet`, `pearl`, `black pearl`, `amethyst`, `topaz`,]
        let decor = [`handful of small ${searchArray(gemstone)}s arrayed around the band`, `trio of small ${searchArray(gemstone)}s`, `single small ${searchArray(gemstone)}`, `single large ${searchArray(gemstone)}`, `large ${searchArray(gemstone)} with flanking smaller stones`, `snake's head with a ${searchArray(gemstone)} set in each eye`, `dragon's head with a ${searchArray(gemstone)} set in each eye`, `fiend with ${searchArray(gemstone)}s set in each eye`, `skull with ${searchArray(gemstone)}s set in its eyes`, `floral pattern`, `leafy motif`, `antler motif`, `thorny motif`, `hexagonal pattern`, `wavy pattern`, `spider-web motif`, `cross-hatching pattern`, `phrase written in a dwarvish script`, `phrase written in an elvish script`, `handful of arcane runes`,]
        let creator = [`dwarvish king`, `elvish prince`, `terrifying elf-witch`, `gnomish gemcutter`, `ancient hero`, `dark sorceress`, `notorious witch`, `legendary mage`, `high priest or priestess`, `mysterious knight`, `sinister lich`, `devious rogue`, `eccentric wizard`, `powerful queen`, `beautiful princess`, `wealthy lord`, `conniving fiend`, `infamous warlord`, `renowned explorer`, `famous singer`,]
        let power = [`absorb ${searchArray(['fire damage','lightning damage','memories','souls','spells','water',])}`, `attract ${searchArray(['birds','ghosts','members of the opposite sex','rats','snakes','stirges',])}`, `avoid ${searchArray(['former lovers','sobriety','trap triggers','trolls','vampires','werewolves'])}`, `bolster your ${searchArray(['agility and reflexes','awareness and senses','confidence and self-esteem','health and toughness','intellect and problem-solving skills','strength and endurance'])}`, `cast a spell ${searchArray(['at random','prepared and stored in the ring by the rings creator','prepared and stored in the ring by you','that creates a disguise','that restores lost hit points','that grants invisibility'])}`, `command ${searchArray(['air elementals','earth elementals','fire elementals','ghouls','water elementals','wolves'])}`, `conjure a swarm of ${searchArray(['bats','parrots','ravens','rats','spiders','zombies'])}`, `control ${searchArray(['demons','dwarves','elves','flames','human minds','weather'])}`, `detect ${searchArray(['lies','illusions','poisoned food and drink','secret doors','traps','water sources'])}`, `disappear in/into a ${searchArray(['hole in the earth','flash of light','nearby tree','shimmering mist','swirl of shadows','wisp of smoke'])}`, `dodge ${searchArray(['attacks from dragons','attacks from giants','lightning bolts','mechanical traps','spell attacks','weapon attacks'])}`, 
        `locate the nearest ${searchArray(['corpse','dragon','gold','living creature','poisonous plant','undead'])}`, `move like a/an ${searchArray(['dolphin','burrowing badger','gust of wind','jackrabbit','ooze','spider'])}`, `predict ${searchArray(['deaths','fluctuations in the price of grain','future catastrophes','military victories','storms','winning horses'])}`, `recover ${searchArray(['expended spell slots','lost dignity','lost hit points','lost gold','lost time','used torches'])}`, `resist ${searchArray(['diseases','mind-affecting charms','persuasion','poisons','psionic powers','seduction'])}`, `see ${searchArray(['faraway places','into others dreams','invisible creatures and objects','people dear to you wherever they are','through the eyes of a beast','through the eyes of a corpse'])}`, `speak with a/an ${searchArray(['dear friend or lover','long-dead person','recently deceased person','snake','spider','wolf'])}`, `summon a/an ${searchArray(['angel','demon','devil','djinni','efreet','pack of wolves'])}`, `teleport ${searchArray(['up to ten feet','to another room nearby','to a well-known temple','to a previously prepared teleportation circle','to the presence of a powerful fiend','to an ancient crypt'])}`,]
        let actAmppower=[`in the ${searchArray(['celestial realm','fiendish realm','mortal world','realm of death','realm of dreams and magic','realm of shadow and death'])}`, `when worn by a ${searchArray(['dwarf','half-dragon','high elf','serpentfolk','shadowfolk','wood elf'])}`, `in sunlight`, `in moonlight`, `underground`, `under starlight`,]
        let reliabilityCost = [`it works ${searchArray(['perfectly, every time','most of the time with infrequent mishaps','as expected about half the time','only occasionally','when the proper conditions are met','rarely and unpredictably','only the first time the wearer uses the power'])}`, `using it comes at a${searchArray([' temporary', 'n acute health'])} cost of ${searchArray(['chills','fatigue','flatulence','headaches','nausea','unsightly and rapid hair growth'])} for ${toWords(1 + rollDice(10))} ${searchArray(['seconds','hours','days'])}`, `using it comes at a chronic or permanent health cost of ${searchArray(['blurred vision or blindness','loss of the power of speech','painful scarring and deformity','poor wound healing','tumorous growths and deformity','wasting sickness'])} for ${1 + rollDice(10)} ${searchArray(['weeks','months','years'])}`, `using it brings on mental distress in the form of ${searchArray(['anxiety','bad dreams',`compulsive ${searchArray(['drinking', 'smoking', 'scratching', 'lack of hygiene'])}`,'insomnia','short temper (irritability)','weight gain (stress eating)'])}`, `using it attracts the attention of a powerful and malevolent ${searchArray(['aberrations','dragons','fiends','ghosts and wraiths','spiders or snakes','zombies and wights'])}`, `using it can occasionally cause ${searchArray(['blizzards','earthquakes','rapid plant growth','thick fog','thunderstorms','volcanic eruptions'])}`,]
        let rumoredImportant =[`quirky individual who claims to be descended from a/an ${searchArray(['ancient monarch','dragon','fiend','legendary warrior','notorious giant','well-known prophet'])}`, `powerful ${searchArray(['arch-lich','master conjurer or illusionist','high priest or priestess','shadow-witch or warlock','dark sorcerer or sorceress','druid or woods-witch'])}`, `heir to a fallen noble house`, `sitting monarch`, `fiendish prince or elemental lord`, `forgotten god or ancient evil`,]
        let rumoredPurpose = [`be sold for an unimaginable fortune`, `gain the cooperation of a ${searchArray(['brutal warlord','high priest or priestess','infamous pirate captain or outlaw','monarch','merchant-prince','vampire lord'])}`, `unlock ancient knowledge and secrets`, `cause the owner gain immense wealth and influence`, `conquer the world`, `open portals to other realms`,]
    
        let output = `A(n) ${searchArray(material)} ring designed with a(n) ${searchArray(decor)}. It was created ${searchArray(['by a(n)'])} ${searchArray(creator)} who imbued the ring with the ability to ${searchArray(power)}. This ability is ${searchArray(["especially powerful","only usable"])} when ${searchArray(actAmppower)}... interestingly, ${searchArray(reliabilityCost)}. If word gets out, a ${searchArray(rumoredImportant)} will pursue the ring for an unknown reason. Commoners will believe that the ring can ${searchArray(rumoredPurpose)}.`
        return output
    }
    let rings = [
        `Ring of Blood: a ring with a clear crystal band filled with blood. As a bonus action the wearer can focus on the ring and the blood inside the ring will flow. When the blood in the ring flows the wielders next physical attack deals an extra 1d6 necrotic damage and all damage dealt in that attack will heal the wearer. This effect can be used once every long rest.`, `Ring of The Stone Giant: a +1 ring made of iron. The wearer can cast the stoneskin spell once a day.`, `Occam’s Ring: a +1 ring made of silver with a pearl in the center. The wearer once attuned gains a +2 in wisdom and proficiency in wisdom saves but a -1 in intelligence as well as disadvantage on all intelligence saving throws. If the wearer has proficiency in wisdom saving throws already then they gain a +3 in wisdom saving throws.`, `Ring of The Blue Dagger: a +1 gold ring that is worn by Blue Dagger members when making shady deals. The ring will turn copper for one minute when it touches a fake gold coin.`, `Ring of Light: a +2 golden ring with a glowing ruby. Once a day the wearer can cast color spray at the third level.`, `Ancient Dragons Band: a red stained platinum ring with a diamond that once attuned grants the wearer resistance to their choice of fire, cold, acid, poison, or lightning damage as well as the ability to speak draconic. The wearer also gains a +2 in persuasion and intimidation.`, `Ring of The Eldritch Eye: a +1 black steel ring with a green eye in the center. Once attuned the wearer gains a +5 in perception and has resistance to psychic damage.`, `Ring of Dwarvenkind: a +2 golden band ring with a black opal center. Once attuned the wearer gains 1 hit point for every level they are. The ring also grants resistance to poison damage.`, `Ring of The Kings Tournament: a +3 platinum band ring with three 5000gp diamonds studded around it. Once attuned the wearer can use action surge as if they were a fighter. This feature can be used once every short it long rest. Additionally the wearer gains an extra attack when making an attack action.`, `Ring of The Black Waters: a rusty iron band ring with an amethyst gemstone. The wearer can cast black tentacles once a day.`,
        `Fury of Orcus: a +2 steel band with a pink gold horned devil with a ruby in its mouth. The wearer once attuned can summon four quasits. One of the quasits is a king quasit. King quasits are a small creature and have 14 hit points instead of 7.`, `Ring of Magic Bullet: While wearing the ring, you can shoot a bullet of magical energy while pointing your index finger. Deals 1d4 damage.`, `Ring of Iron Grip: The hand on which the ring is attached becomes detachable at will, and if detached while grabbing onto something, the grip is as strong as iron. The wearer has psychic knowledge of where their detached hand is at all times.`, `Ring of The Druid: a +1 bronze ring with an emerald that once attuned allows the wearer to turn into a small beast once a day.`, `Ring of Hadar: a +3 ring forged in the frost of the deepest depths in hell. The wearer once attuned becomes immune to cold damage and grants the wearer a favor from a devil king.`, `Ring of Medicine: a +1 ring that grants the wearer proficiency in medicine.`, `Ring of Spiders: a +1 ring that grants the wearer climbing speed equal to their walking speed. The wearer also gains resistance to poison damage.`, `Ring of The Grand Blacksmith: a ring that once attuned to can summon a +3 simple or martial weapon. The weapon also does an additional 1d4 of either fire, cold, or lightning damage.`, `Ring of Hinalia: a ring forged by a cleric of Hinalia, a goddess of luck. The ring is made of platinum with a diamond gem. Every morning the wearer wakes up with a platinum piece.`, `Ring of Broma: an ancient ring made of an unknown metal with a dune etched into the side of a language long forgotten. Attuning to the ring grants the wearer +2 dexterity and +2 charisma. When touched with the Ring of Vistal and the Ring of Shevo the effects of each ring are imbued into the three wearers permanently giving the three their benefits before each ring crumbles to dust.`, 
        `Ring of Vistal: an ancient ring made of an unknown metal with a dune etched into the side of a language long forgotten. Attuning to the ring grants the wearer +2 constitution and +2 wisdom. When touched with the Ring of Vistal and the Ring of Shevo the effects of each ring are imbued into the three wearers permanently giving the three their benefits before each ring crumbles to dust.`, `Ring of Shevo: an ancient ring made of an unknown metal with a dune etched into the side of a language long forgotten. Attuning to the ring grants the wearer +2 strength and +2 intelligence. When touched with the Ring of Vistal and the Ring of Shevo the effects of each ring are imbued into the three wearers permanently giving the three their benefits before each ring crumbles to dust.`, `Ring of Malice: a ring made of black crystal and has a glowing purple gem set into it. Anyone who looks into the gem thinks of their most hated foe. As an action, the wearer can picture someone they've come into contact with before and cast Locate Creature on them without expending a spell slot or material components. The wearer can do this once per day, the ability recharging at midnight.`, `Fairy Ring: looks like a small band made of toadstools. Once attuned can be used as a one time use portal into (or out of) they feywild. The portal appears to be a 5ft radius fairy ring on the floor made of red toadstools. This can be used once every sunrise.`, `Ring of Poison Detection: a simple brass band with a snake engraved around it. When the wearer is wearing the ring and comes into contact with a poisonous liquid it will turn shiny and silver.`, `Peephole Ring: an ordinary looking ring with the symbol of an eye engraved in it. When the ring is placed against any solid surface it acts as a peephole. Peephole can be used to see through up to 3ft of any solid matter except lead. Note there is no actual hole in the surface the ring only allows you to see through it as if there was a peephole at the location of the ring.`, `Ring of Honesty: a +2 glass ring with an emerald gem. The wearer once attuned has disadvantage on deception checks. Three times a day the wearer can lay a curse on another creature. The creature must make a DC 20 wisdom save or be forced to say whatever they are thinking for 24 hours.`, `Ring of Renewed Resolve: When wearing this ring, and being the target of a healing spell from a source other than yourself, as a reaction you may use one hit die.`, 
        `Ring of Rosies: This ring with a delightful tiny metal rose grants its wearer the Cantrip known as Druidcraft and the ability to cause flowers to bloom or revitalise simply by touching them.`, `Coffee Ring: Strange ring that, when dropped in hot water, causes the liquid to turn brown and take on a bitter, yet enjoyable taste identical to coffee... just be careful not to forget about the ring. You don’t want to know what it does to your insides...`, `Ring of Recalling: Each holder of the ring may bestow it a memory. Once stored, this memory is lost to you without the ring. It could be a secret hiding hole, a safe combination or the last time you saw your beloved wife. Either way, the memory says with the ring and is remembered by anyone else who uses it. This ring is special, requiring attunement, but not counting against your attunement cap. To attune you must spend a long rest wearing the ring and bestow it a memory. Once done, you will have access to all the stored memories, including your own.`, `Ring of the Rooster: Although a bit larger than the average finger ring (yet smaller than a wrist bangle) this peculiar golden ring, engraved with a rooster mark, conveys certain benefits befitting its animal. You can cause your voice to boom out much louder than normal (as of using the Thaumaturgy cantrip) as a free action similar to a Cock’s crow. This increases the spell range of sound based abilities and spells (such as those of a Bard) by 15 feet. You may also cast Featherfall for free once per day, landing in a cloud of white feathers.`, `Cling Ring: a silver ring shaped like two hands clutching each other. The wearer is immune to effects that drain their maximum HP or prevent healing.`, `Ring of the Iron Golem: Thick cast iron ring that never rusts. The wearer’s Constitution score becomes 24 if it’s not already equal or higher. They also become magnetic; ferrous metal objects up to ten pounds in weight will stick to them, and attacks against them with metal weapons can’t miss.`, 
        `War Oath Ring: A wide band made of old papyrus, strangely impervious to any kind of damage, with an evergreen tree drawn on it surrounded by angular runes. The wearer becomes proficient with all weapons. If they gain four levels or three years pass by wherein the wearer only ever used one non-magical sword, it becomes a +3 magical weapon which can cast a 1st level Cleric spell of the wearer’s choice, once a day.`, `Ring of Aves: a +1 ring with a pearl band and a sapphire gem. Once attuned the wearer can cast featherfall once every short rest and can speak auran.`, `Dead Man's Ring: a simple metal righ found off of a dead npc. A while after wearing the ring, the ghost of the original owner will start to appear only the the current person wearing the ring.`, `Spiked Ring - This simple black stone band has a series of small spikes around it. As a bonus action, the ring causes the wearer to grow stone spikes from their knuckles, which deal an extra 1d4 piercing damage when attacking unarmed. The user may use an action to fire the spikes from their fist, making a ranged attack roll on 1 creature, on a successful fit, the spikes deal 1d8 + dex piercing damage (range (20/60), and the spike effect on the knuckles ends immediately. otherwise, the knuckles last for 1 hour or until dismissed.`, `Ring of Signets: A favorite of spies and saboteurs, this ring can be used to copy and replicate other seals. Once per day the wearer can press it against a wax seal to 'learn' that design or command the ring to switch to some previously learned design. The ring also grants +1 AC and a +2 in stealth.`, `Ring of Chet: a +3 ring made out of a strange rainbow material. The ring grants the wearer the ability to cast color spray and prismatic wall once a day. Additionally very rarely an ancient wizard named Chet known for his pageantry and his boyfriend Tim will give advice to the wearer.`,
        `Ring of Elven Grace: a +1 ring with a cedar wood band and an emerald gem that once attuned to grants the wearer +10 to movement and a +2 to all ranged attack rolls.`, `Ring of the Right Path: Once per day, if the wearer is presented with a decision that has some physical representation, such as a fork in the road, or selecting a person, they can bid the ring to make a decision. The ring will tug the wearer's hand towards the best, or least-bad option at that precise moment, subject to DM interpretation.`, `Ring of Remote: The wearer of this ring can cast the Mage Hand cantrip. The hand that the ring is worn on detaches, and acts as the mage hand, becoming transparent and made of force energy until the end of the spell. When the spell ends, the wearer's hand reappears.`, `Ring of The Desert: a +1 clay band ring with a yellow diamond gem. The ring when attuned to the wearer no longer requires water and can transmute water into sand.`, `Lich Ring: a +2 pitch black ring with a green flame burning in the center. Once attuned the wearer is invisible to undead with challenge ratings below 6.`, `Ring of The Far Travelers: a +1 ring made of a grey alloy with a diamond gem. Once attuned the wearer gains resistance to fire and cold damage.`, `Winters Breath Ring: a blueish metal alloy band with a wolfs head holding a sapphire in it’s mouth. Once attuned to the wearer can summon a friendly winter wolf named winter who will protect the ring wearer to the best of her abilities. If winter dies the ring wearer can do an hour ritual to bring her back to life. The ring cannot be attuned to by evil creatures.`, `Ring of Linguistic Achievement: After wearing this ring for one week, the ring will dissolve into the skin of the wearer, leaving a magical tattoo of a rotating script that the wearer understands. Once dissolved, the DM chooses a language the wearer does not understand, and that language becomes known to the wearer. Only one of these can exist in the world, and will magically avoid the party of anyone who has already used the ring.`,
        `Ring of Past Sight: a glossy ebon ring with a small vein of material running through it that is either green or red, depending on the lighting. When attuned, the wearer can choose to experience the recent past of the area they are currently in by going to sleep for at least five minutes. While asleep, the wearer can choose any point between mere seconds ago and up to ten days, although the further back they go the longer they remain asleep in the present. Alternatively, they can attempt to view the past without going to sleep first, but the strain on one's consciousness immediately forces an INT save of 15 to avoid 2d8 psychic damage. If the save is failed the wearer must try again.`, `Monkey's Tail Ring: two tiny smoky quartz gems dangle from this loop of twine. Anyone wearing it cannot fail climb-related checks, their long jump distance increases by 10 ft, their high jump distance increases by 5 ft, and Athletics checks related to jumping are made with advantage. When attuned, the wearer is treated as if persistently under the effect of Spider Climb.`, `Ring of Animal Dowsing: this four-sided ring is made of teak-like wood with a band of amber running across each side. When attuned, the wearer can press the ring to any solid surface to know the location and species of living creatures within 60 feet. The ring stores three charges, and regains one each dawn. An attuned wearer can use one charge to cast Animal Friendship on any animal the ring has recently detected, ignoring the spell's restrictions on both line of sight and the animal needing to see and hear the caster.`, `Ring of Love: This gold plated ring has a ruby shaped like a heart set in the center and allows charm person to be cast once per short rest by the wearer once attuned. The ring is valued around 250gp.`, `Ring of Shadows: an invisible ring that can only be seen in dim light as a band made of darkness. Once attuned the wearers attacks deal an extra 1d6 necrotic and the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. The ring has no effects in broad daylight.`, `Pink Key Ring: This small pink ring can be used once a day to unlock a non magical lock. When activated the finger on which it is worn temporarily transmutes into a skeleton key which can be used to unlock the lock.`, 
        `Kobara’s Ring: a +2 ring made of iron with a pearl in the middle made by an infamous illusionist. As an action the wearer can produce 2d10 caltrops which disappear after 5 minutes.`, `Ring of Spells: a +3 lead and gold ring that allows the wearer to cast a level three spell of their choice once every long rest.`, `Luck Ring: a golden ring with vine patterns carved in and an emerald gem. The wearer once attuned gets +1 to all saving throws and gets advantage on one saving throw every long rest.`, `Ring of The Artisan: an oak wood ring that grants the wearer proficiency in one tool of their choice. That tool can be changed every long rest.`, `Ring of Chronos: a +1 silver ring that triples the wearers expected lifetime.`, `Ring of The Navigator: a bronze ring with an opal gem. The wearer can once every sunrise ask the ring for water, civilization, or a cave and the ring will glow when pointed in the direction of the object desired. This ring was made by Druids as a gift to a local farm town.`, `Ring of The Forgotten Glade: the ring is spotted green copper (but doesn't leave stains on the wearers' skin) with a ruby in the shape of a bear set on top. When it is worn, add +2 to Performance checks as the wearer is suddenly inspired with visions of a peaceful forest glade to ease their spirit, and Advantages on saves vs mental or emotional magical attacks.`, `Ring of The Stars: a black iron ring with platinum spots that once attuned grants the wearer +1 to all saving throws and the wearer no longer requires sleep.`, `Ring of The Sun: a golden ring with a sun carved into it. Once attuned to the wearer gains +2 AC and +2 on all saving throws. The wearer gains resistance to radiant damage and an immunity to blindness. Once every sunrise the wearer can release a burst of radiant energy as an action dealing 4d6 radiant damage and healing the wearer for 4d6 hit points.`, 
        `Ring of The Moon: a silver ring with a moon carved into it. Once attuned to the wearer gains +2 AC and +2 on all saving throws. The wearer gains resistance to necrotic damage and immunity to deafness. Once every midnight the wearer can release a burst of shadowy energy as an action dealing 4d6 necrotic damage and healing the wearer for 4d6 hit points.`, `Ring of Shrooms: a ring made by a spore druid that once attuned allows the wearer to cast crown of madness a number of times a day equal to their wisdom modifier.`, `Ring of The Scholar: a bronze ring with an amethyst gem. The ring once attuned gives the wearer +2 intelligence and can summon a book of lore in the wearers hand at will.`, `Ring of The City: a ring that changes the metal the band is made of depending on the city the wearer is in. The wearer can summon a map of the city or town that the wearer is in.`, `Spiked Ring: a +2 steel ring with spikes covered around the ring. Puttong on the ring deals 4d4 piercing damage. Once attuned to the ring grants the wearer resistance to piercing damage.`,
        `Ring of Jaq: a +1 purple band ring with dwarven runes carved into it. Once attuned to the wearer becomes immune to poisoning and has advantage on constitution and charisma saving throws.`, `Ring of Lightning: a glass ring with lightning trapped inside of the band. the ring has 6 charges. The wearer can expend one charge to cast absorb element, two charges for thunderclap, or three charges for either lightning bolt or thunderstep.`, `Ring of Displacement: as a reaction after an enemy has hit, you may use this rings charge to swap places with one other creature. If the creature is willing it happens instantaneously, but if its not, it must first succeed on a wisdom saving throw of dc 15. This ring has one charge and recharges daily at dawn.`, `Ring of Freshwater: a +1 blue porcelain ring that when touched to saltwater transmutes it into freshwater. The rings effects do not work on bodies of water larger than 100 feet in diameter.`, `Ring of Saltwater: a +1 blue porcelain ring that when touched to freshwater transmutes it into saltwater. The rings effects do not work on bodies of water larger than 100 feet in diameter.`, `Invisible Ring: This ring is impossible to find unless you have an ability to see invisible things. When worn, it looks like the wearer is missing the finger the ring is on.`, `Ring of The Woodcarver: a mahogany ring with a ruby gem that once attuned to grants the wearer a +5 to woodcarving.`, `Ring of Sylvanus: a +1 ring with an emerald band that once attuned to grants the wearer the ability to speak to plants. The wearee can also regenerate 1d6 hit points every hour they are in sunlight.`, `Holy Ward of The Templar: a +2 red and white steel ring that grants the wearer advantage on initiative rolls.`, `Great Leviathans Eyes: a red leather ring that grants the wearer +2 perception, an additional 30 feet of darkvision, and the ability to sense any fiends in a 60 foot radius.`, 
        `Ring of Freshness: a golden ring with a pink diamond carved into a heart shape. Once attuned the wearee gains a +2 charisma and always smells wonderful.`, `Ring of illusion: a ring that looks platinum with a diamond gem. The ring is actually a regular tarnished copper ring disguised as something more valuable.`, `Ring of Autumn: a mahogany ring with an orange gem carved into a leaf on it. The ring when touched to a tree will turn all of it's leaves red orange and brown.`, `Ring of The Professor: a white marble band that once attuned to gives the wearer +2 intelligence and the ability to calculate numbers with precision.`, `Ring of The Thief: a cast iron ring with runes scratched on it. the wearer has advantage on all slight of hand checks`, `Rangers Ring: an elvenwood ring that his glowing elven runes written on it. Once attuned all ranged attacks gain a 1d6 to damage rolls and all bolts or arrows become replenished if the attack hits.`, `Ring of Arthur: a +2 golden ring studded with rubies. Once attuned the wearer gains a +1 to attack rolls and can counterspell a spell that is an abjuration spells at level 5 or lower a number of times a day equal to the wearers intelligence modifier to a minimum of 1.`, `Barbers Ring: a porcelain blue and red ring that can summon a pair of scissors at will.`, `Ring of kinetic storage: During combat, this ring stores the kinetic energy of all your attacks both hits and misses. Each hit adds 1 charge and each miss adds 3 charges for a max of 20 charges. On a hit after making an attack (spell attack or melee) you may consume any increment of 5 (5,10,15 or 20) charges and add that number as force damage in addition to your damage roll. Alternatively, you may make an unarmed strike as a bonus action and add the force damage on a hit.`, `Ring of Mage Sight: a ring that once attuned to grants the wearer a +1 on all saving throws and the wearer can cast detect magic 3 times a day.`, 
        `Ring of Air: a silver band with and a smoothed stone. When knocked prone a gust of wind immediately picks the wearer back up on their feet making the wearer immune to being knocked prone.`, `Ring of Safe Passage: These rings vary widely in their appearance. Each of these rings is attuned to a specific place. The wearer can safely pass through any area the ring is keyed to without setting off any magical traps or wards. Any magical guardians will treat the wearer as if they are guest of the rightful owner. The ring will also unlock specific magically locked doors.`, `Ring Golem: Upon command the ring unfolds itself into a tiny 3 inch tall golem. It's strong enough to carry about 1 pound. It's uses may require some imagination like "crawl inside that lock an unlock it from the inside".`, `The Pilgrims Knowledge: a copper ring that once attuned to grants the wearer +2 intelligence and gives the wearer the ability to know the name of any creature they see.`, `Ring of The Farmer: a copper ring that once attuned to grants the wearer +2 wisdom and proficiency in survival. The ring when touched to soil makes the soil very fertile.`, `Ring of Gluttony: a thick iron band that once attuned grants the wearer +2 constitution and advantage on all constitution saving throws, however, every day the ring is worn the wearer gains 2d6 pounds and requires twice the amount of food and water.`, `Ring of The Imprisoned One: a +2 ring made out of a mysterious glowing yellow material. Once attuned to the wearer can choose to replace their movement speed for teleportation equal to their movement speed.`, `Ring of The Dark Count: a black and red ring with a ruby gem that can cast bestow curse once a day.`, `Ring of Divine Invisibility: a golden and silver ring. Once worn celestial and fiend creatures cannot see the wearer.`,
        `Ring of Necromancy: a +1 ring that grants the wearer immunity to necrotic damage and allows the wearer the option to replace any bludgeoning, piercing, and slashing damage with necrotic damage.`, `Ring of the Windweaver: While attuned to this ring of twisted platinum wire, you may expend the ring's seven charges to create the following effects. The DC for any saving throw is 15, and the ring regains 1d6+1 charges daily at dawn. Updraft (2 charges) You cast levitate, targeting one creature within 120 feet of you and requiring no concentration. Alternatively, you cast feather fall, with a range of 120 feet and requiring no concentration. Downdraft (1 charge) A creature of your choice within 120 feet of you can't jump for 1 minute unless it passes a Strength check. If the creature is flying, it is forced down at 60 feet per round unless it passes the check, landing safely if it hits the ground. Tailwind (2 charges) One creature within 120 feet of you may Dash as a bonus action for 1 minute. You may target additional creatures by spending 1 charge per creature. Wind Spear (3 charges) Lashing out with a gust of violent air, you create a line up to 120 feet long and 5 feet wide, originating from you. It deals 3d6 bludgeoning damage to all creatures in the line, with a DEX save for half damage. Gale (4 charges) You create a sphere of turbulent wind with a radius of 20 feet within 120 feet of you. This area counts as difficult terrain, and a creature that enters the area for the first time on its turn or starts its turn there takes 1d6 bludgeoning damage. The sphere lasts for 1 minute. Hurricane (7 charges) A 120 foot wide, 40 foot tall cylinder centered on you is filled with a raging storm. Creatures in the area and take 3d6 bludgeoning damage when they enter the area for the first time on their turn or start their turn there. When moving in the area, a creature must pass a Strength check or be forced to move in a circle around you (clockwise or anticlockwise, determined when you use the ring. You and up to 6 other creatures of your choice are immune to these effects.`, 
        `Ring of The Weave-spinning Warrior: A +3 ring made by a powerful evocation wizard, a war cleric, and a solar. The ring is made of pure diamond and has a crystal filled with diamond dust. The ring has one charge and the charge replenishes every week. When the wearer casts a spell the wearer can choose the expend one charge to double the damage of the spell being casted. One the charge is used the wearer gains exhaustion levels equal to the spell level -1 divided by two.`,
    ]
    document.getElementById("Ring").innerHTML = searchArray([rollArray(rings),ringBuilder()])
};
function findCard() {
    let deckOfAllTheThings = [
        "Kettle - This card is uncomfortably warm to the touch.", "Iron - This card is far heavier when held. When put away it returns to the weight of card, It always behaves as if it were made of card.", "Flagon - A large amount of liquid can be held on the card without it dripping off. The card is waterproof.", "Worm - Fish and birds are unusually attracted to this card.", "Coin - The card glimmers in the light, like a fine jewel.", "Knife - The sides of the card a very sharp, still bends like card.", "Quill - Draws a thin line when rubbed on a surface.", "Dice - When drawn a random number is displayed on the card.", "Book - This card shows a sentence of the last book the holder has read.", "Pepper - Storing this card with meat makes it taste better.", "Arrow - This card travels in a straight path when thrown.", "Bandage - This card sticks to the skin.", "Boot - The card slowly moves west.", "Coat - The card never gathers dirt nor gets wet.", "Pitchfork - The card smells exceptionally bad.", "Basket - Any object balanced on the card feels nearly weightless.", "Fork - Small objects stick to the edge of the card.", "Cloth - This card slowly absorbs liquids.", "Eyeglass - The card bends slightly at one corner, pointing to the nearest 'interesting' thing.", "Mirror - After 5 hours of the card remaining undamaged, a copy appears. (this card does not dissolve)",
        "The Mule - The card fizzles into a dust cloud that solidifies into a cranky old donkey, complete with saddlebags and a lead.", "The Magician - The card bursts into sparkles and settles into a beaver-fur black top hat, a pair of white gloves, a docile rabbit, and a two-headed coin.", "The High Priestess - The card swings open into the nearest solid wall, becoming a curtained doorway. It passes into whatever space was naturally on the other side of the wall.", "The Empress - The card flutters into a beautiful and elegant gown that will fit the nearest female. It is embroidered with silver thread.", "The Emperor - The card flourishes into a golden crown that fits the one who pulled the card. It is bejeweled and valued at 600 gold, but selling it openly can cause suspicion.", "The Hierophant - The card multiplies itself into the many pages of the Holy Scripture appropriate for the religion of the one who pulled the card. It is leather-bound, weighs 14 lbs. and is about the size of a breadbox.", "The Lovers - The card pulls itself into two powerful, rare earth magnets. Each has a pull of 5 lbs. and together, 9 lbs.", "The Steed - The card dashes forth into a war horse.", "Justice - The card slams to the ground and becomes a heavy war hammer. If pulled by a cleric, the hammer has the cleric's holy symbol engraved on the side.", "The Hermit - The card flops to the earth and grows into a small stone and wooden hut with a fireplace and lockable door.", "Wheel of Fortune - The card unfolds into a sturdy market stall wagon, filled with dry goods valued at 300 gold if sold.", "Strength - The card thuds to the ground, having become a six foot long crow bar of strong iron.", "The Hanged Man - The card unwinds into a coil of bloodstained hemp rope, 50 ft. long.", "Death - The card wilts into a gleaming war scythe.",
        "Temperance - The card wobbles into a fine brass merchant's scale, complete with set of standard brass weights.", "The Devil - The card burns up and the ashes form a formidable trident or pitchfork (appropriate for the location).", "The Tower - The card rises from the hand into a twelve foot wooden ladder with iron hooks on one end.", "Lantern - The card flashes into a lit oil lantern with a full reservoir.", "Cover - The card rumples into a soft, black cloak of deep velour.", "Torch - The card ignites into a lit torch that will last for four hours.", "Judgment - The card shines with a glint of light from a bright, clear hand mirror set in a rosewood frame.", "The World - The card coils into a circle that becomes a signet ring and wax set that will emboss the local kingdom's seal.", "Two Face - Either an Ally you meet will feel compelled to betray you, or an Enemy will be compelled to assist you. They can resist it, but only at great expense of their own.(DM decides which happens and who. This can be from NPC motivations or arcane impulse)", "The Pickaxe - A meteor strikes near your location. It contains a hard encounter of abberitions or monstrocities. The metal from the comet is adamantine and can be used to make adantine plate. It can be sold to a skill smith for 1000gp.", "Excavate - You come into possession of a map of a forgotton tomb or some other dungeon like area. You know where the dungeon is located and know its layout. (The dungeon may have been modified by weather or new inhabitants since the map was made. Making it less effective)", "Sacrifice - you are forced to take on a minor curse, but gain a minor blessing (Dms discretion as to what these are). The effect can be removed by remove curse, but it removes the blessing as well.", "Flames - You have a haunting realization that someone you offended was a devil in disguise. (Dm gets to pick who, the player gets to pick how)", 
        "Wealth - A bag of gems worth 25cp appears before you, but know that it is worth at least 5000gp in a far off land or a big city. (DM decides where and exactly how much.)", "The Sheathe - You gain a +1 weapon that takes on one form of your choosing which cannot be changed later.(If the weapon is a staff or the owner is a magic user, it can instead hold up to 4 spell slots [highest 3rd]) It plays an important roll in a profecy and becomes a +3 weapon if its duty is fulfilled(10 slots [max 5th]). It is a non magical weapon if anyone else uses it and cannot be used to harm you. (cultists or jealous heroes may attempt to steal the weapon, which requires killing the character)", "The Commander - You gain an apprentice/accolyte/squire who is completely loyal to you, though they won't allow mistreatment. They are proficient in one trade skill if you have one yourself. While not effective in combat ( unless DM decides otherwise later) they are effective with running businesses you might own or helping to craft armor/items. Crafting requires the same amount of gold, but 2/3rds less time.", "The Lazy Builder - You will cause someone to lose everything they ever held dear. Everyone shall know it is your fault and the person shall dedicate their life to revenge. Only a wish used to restore everything they lost, plus interest will be able to dissuade them.", 
        "Host - You have been blessed with starlight. You now glow slightly, emitting 30ft of dim light. You have disadvantage on all stealth saving throws. This effect persists through invisibility. You gain proficiency in saving throws connected to your lowest stat that you aren't proficient in.", "The Wilted Flower - Someone you love has died. (Dm decides how, if they were murdered, the player knows who they are) If you have no loved ones, you are instead falsely accused of murder.", "The Seal - You gain the deed to a medium sized castle and a few of the surrounding territories. You do not know the location of the castle, but it can be found through mundane or arcane means and know where to begin searching for it. Additionally, you have advantage on persuasion and intimidation rolls regarding matters of your territories.(DM decides the condition of the castle and any current 'owners', there might be an investment to fully restore it. If the player doesn't have an ally that would be a steward they can easily acquire one)", "The Wealthy Friend - You will gain the aid of a member of the upper class who will support in minor ways. They can be persuaded to use their influence to aid you in a more major way, but each time is more difficult than the last. (the ally can be a simple noble, a high cleric, or a king)",
        "Weeping Woman - Soon, your character will have a chance to correct or atone for what they view as their biggest mistake-with dire consequences if they should not do so. Player decides what- DM decides how.", "Branch - You lose a class level but in exchange gain another random class level. You can retrain this in two levels.", "Ogre - You lose 1 point of intelligence but gain advantage in dealing with NPCs below 9 Intelligence.", "Spy - Draw two more cards. You may, if you wish, bestow one on someone in sight.", "The Shifter - You will undergo an extensive and probably permanent physical transformation. You may be attacked by a lycanthrope, targeted by Baleful Polymorph, or become deformed in an accident, or other effects.", "The Shadows - A criminal organization targets you for your wealth, influence, or because you pissed them off in the past. At first they send threatening notes, but it quickly escalates into violence.", "The Crown - In the future, you will be granted a noble title by royalty as proof of your deeds- or are elected to a powerful office, or become a folk hero. Wherever you go, you will be accepted and supported, sometimes clandestinely, other times openly.", "The Displacer - The weave of magic is less stable in your presence. Whenever you cast a spell or are affected by a spell roll a d20. If it is a one, roll on the wild magic table (this is in addition to any other reason to roll on the table)", "Haunt - You will die. SOON. And not under pleasant circumstances. Nightmares will haunt you until your dying day. Demons and undead will attack you as you sleep. A Remove Curse will only succeed at suppressing it- the Void will return in a year. But on the bright side, if you are resurrected you will be unaffected afterwards. The curse can be removed permanently, but you do not know how.",
        "Balance - Your mind suffers a wrenching alteration, causing your Alignment to change. Lawful becomes chaotic, good becomes evil, and vice versa. If you are true neutral or unaligned, this card has no effect on you.", "Comet - If you single-handedly defeat the next Hostile monster or group of Monsters you encounter, you gain Experience Points enough to gain one level. Otherwise, this card has no effect.", "Donjon - You disappear and become entombed in a state of suspended animation in an extradimensional Sphere. Everything you were wearing and carrying stays behind in the space you occupied when you disappeared. You remain imprisoned until you are found and removed from the Sphere. You can't be located by any Divination magic, but a wish spell can reveal the location of your prison. You draw no more cards.", "Euryale - The card's medusa-like visage curses you. You take a -2 penalty on Saving Throws while Cursed in this way. Only a god or the magic of The Fates card can end this curse.", "The Fates - Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. You can use the card's magic as soon as you draw the card or at any other time before you die.", "Flames - A powerful devil becomes your enemy. The devil seeks your ruin and plagues your life, savoring your suffering before attempting to slay you. This enmity lasts until either you or the devil dies.", "Fool - You lose 10,000 XP, discard this card, and draw from the deck again, counting both draws as one of your declared draws. If losing that much XP would cause you to lose a level, you instead lose an amount that leaves you with just enough XP to keep your level.", "Gem - Twenty-five pieces of jewelry worth 2,000 gp each or fifty gems worth 1,000 gp each appear at your feet.", "Idiot - Permanently reduce your Intelligence by 1d4 + 1 (to a minimum score of 1). You can draw one additional card beyond your declared draws.", "Jester - You gain 10,000 XP, or you can draw two additional cards beyond your declared draws.", "Key - A rare or rarer Magic Weapon with which you are proficient appears in your hands. The DM chooses the weapon.", 
        "Knight - You gain the service of a 4th-level Fighter who appears in a space you choose within 30 feet of you. The Fighter is of the same race as you and serves you loyally until death, believing the fates have drawn him or her to you. You control this character.", "Moon - You are granted the ability to cast the wish spell 1d3 times.", "Rogue - A nonplayer character of the DM's choice becomes Hostile toward you. The identity of your new enemy isn't known until the NPC or someone else reveals it. Nothing less than a wish spell or Divine Intervention can end the NPC's hostility toward you.", "Ruin - All forms of Wealth that you carry or own, other than Magic Items, are lost to you. Portable property vanishes. Businesses, buildings, and land you own are lost in a way that alters reality the least. Any documentation that proves you should own something lost to this card also disappears.", "Skull - You summon an avatar of death-a ghostly Humanoid Skeleton clad in a tattered black robe and carrying a spectral scythe. It appears in a space of the DM's choice within 10 feet of you and attacks you, warning all others that you must win the battle alone. The avatar fights until you die or it drops to 0 Hit Points, whereupon it disappears. If anyone tries to help you, the helper summons its own Avatar of Death. A creature slain by an Avatar of Death can't be restored to life.", 
        "Star - Increase one of your Ability Scores by 2. The score can exceed 20 but can't exceed 24.", "Sun - You gain 50,000 XP, and a wondrous item (which the DM determines randomly) appears in your hands.", "Talons - Every magic item you wear or carry disintegrates. Artifacts in your possession aren't destroyed but do Vanish.", "Throne - You gain proficiency in the Persuasion skill, and you double your Proficiency Bonus on checks made with that skill. In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently in the hands of Monsters, which you must clear out before you can claim the keep as. yours.", "Vizier - At any time you choose within one year of drawing this card, you can ask a question in meditation and mentally receive a truthful answer to that question. Besides information, the answer helps you solve a puzzling problem or other dilemma. In other words, the knowledge comes with Wisdom on how to apply it.", "The Void - This black card Spells Disaster. Your soul is drawn from your body and contained in an object in a place of the DM's choice. One or more powerful beings guard the place. While your soul is trapped in this way, your body is Incapacitated. A wish spell can't restore your soul, but the spell reveals the location of the object that holds it. You draw no more cards.",
        "Surprise - Decrease your top 3 stats by 1 point, increase your bottom 3 stats by 1 point.", "The Magician - You gain a cantrip of your choice from the Wizard's list of cantrips. Figure out logistics depending on character.", "The High Priestess - You may ask one question of your God. This power does not need to be used immediately.", "The Empress - 5,000 Gold appears at your feet. Scale based on level?", "The Emperor - You gain rightful ownership of a small keep somewhere in the world. The keep is currently occupied and you must clear them out before claiming the keep.", "The Hierophant - Gain proficiency in a skill of your choice.", "The Lovers - An NPC falls in love with you.", "The Chariot - An NPC becomes your follower. Low CR NPC stat block that makes sense for the character. Scale based on level?", "The Anvil - Gain a magical weapon or piece of armor. Scale quality based on level.", "Tactician - Draw two more cards. Choose one.", "The Coin Flip - Draw two more cards. You get both.", "Wings - A powerful angel becomes your enemy.", "The Tipped Cow - An NPC becomes your enemy.", "The Hourglass - You will die. Maybe not today, maybe not tomorrow, but your fate is sealed. You will not live much longer.", "Aid - Gain the Healer Feat.", "Horns - A powerful devil becomes your enemy.", "The Shattered Glass - A calamity will befall a place important to you.", "The Curio - Gain a magical item (non-weapon/armor). Scale quality based on level.", "The Club - Decrease one of your ability scores by 2. Can't be your lowest.", "The Mind - Increase one of your ability scores by 2. Can't be your highest.", "Judgement - Your life up to this point will be judged. Potentially warrants for your arrest or boons for being a hero, potentially nothing.", "The Council - Each player (including you) draws a card.",
        "The Zoo - A plate of iced cookies shaped like many exotic animals.", "The Clown - A sugar-spun butterfly that flutters around. Whoever catches and eats it is able to cast Magic Missle as a level 1 wizard spell once per long rest. Casting Magic Missile in this way does not require spell components. This effect lasts for 1d20 days.", "The Nun - A single pomegranate.", "The Tree - A bowl of fruit.", "The The Cow - A 5-foot cube of a very hard cheese drops from the sky in front of the bearer.", "The Cleric - A goblet of holy wine. Whoever drinks this wine will utter a long-forgotten secret.", "The Baker - A delicate, heart-shaped cake.", "The Farmer - A wagon laden with fruit, vegetables, and dried meats.", "Justice - A set of scales. One scale contains the bearer's favorite food, while the other contains their least favorite food. The scales are in perfect balance.", "The Druid - A wooden bowl filled with edible roots, twigs, and woodland berries. They are very bitter.", "The Kingdom - A meal for a single person. The bearer must roll 1d10. The outcome of the roll determines what the meal contains, as described below - (A worm-eaten apple; Hard-tack. It is hard enough to break teeth if not softened; Overcooked vegetables; A slightly stale loaf of bread; A plate of fresh vegetables; A small plate of cheese, sliced meats, and crackers; A plate of perfectly cooked vegetables, with a slice of warm bread; A whole roast chicken, complete with stuffing; A fine steak served with a tankard of delicious ale; A roast leg of lamb, served on a bed of fresh greens and roasted root vegetables, and paired with a rather nice wine) ", 
        "The Nosering - A roasted bull.", "The Last Pig. An empty plate. The user may draw another card from the deck immediately after they realize that the plate is, in fact, empty.", "The Cheater - A plate of rotten, maggot-infested food.", "The GoodWife - A modest meal that is appropriately portioned for the user.", "The Mole - An exquisite mug of delicious hot chocolate, spiced with cinnamon and cayenne pepper. Whoever drinks this mug can understand and speak Infernal for 1d10 days.", "The Fountain - A 5-foot tower made entirely of candy glass. If broken, the bearer receives a vision of an overwhelming tragedy that will occur in the future.", "The Daze - A bottle of sparkling wine. Whoever drinks this must immediately casts Dancing Lights without requiring spell components.", "The Pulled Cloth - A sumptuous banquet. Upon inspection, this banquet is found to be an illusion. After determining that this is, in fact, not a real banquet, the bearer may draw again if they are able.", "The Bird - A small satchel of sunflower seeds. Whoever eats this entire satchel will feel as if they have just woken up from a long rest, and they regain any abilities as if they had just received a long rest.", "The Measure - The effects of this card is determined by the alignment of the bearer. If good, the bearer receives a goblet of faintly glowing wine that, if drank, gains one minor blessing for the next 24 hours. If neutral, the bearer receives an ordinary goblet of wine. If evil, the bearer receives a goblet of what seems to be bloodwine that, if drank, bestows a minor curse for the next 24 hours.", "The Feast - A massive banquet with enough food for 10x1d20 people.",
        "The Poet - The user must now speak in rhyme. Meter does not matter but each couplet (at least) must rhyme. Failure to do so causes a Magic Missile to manifest, and strike the user	A tiny silver pickle", "The Scholar - A spellbook appears in the user's hands. It cannot be opened by any means, and is engraved in a language that cannot be deciphered. Once a day it grants the user a random spell from all available spells. If the spell is not used by the end of the day, it disappears from the user's mind, to be replaced after a long rest with a new spell.	A wooden arrow with a metal hunting tip.", "The Demon - None of the Deities can manifest an avatar for the next year. Cue uproar in the Faithful.	A wooden splinter", "The Bee - The Highest Lord of the Realm vanishes and his wife/consort assumes the throne as steward. The Lord is never found.	Tiny scepter of lead. Worth 2 cp.", "The Locked Door - The Highest Lord of the current realm gains a mysterious wasting disease that cannot be cured, and he will die in 1 week	Tiny crown of pewter. Worth 2 gp.", 
        "The Scriptures - Something the user does in the next town, some feat, or overt act, is picked up by some locals as a sign of the user's divinity. A cult will form and followers will begin to appear	A set of tin prayer beads", "The Dagger - The user suddenly realizes that out there, somewhere, their true love awaits. The true love also is aware of the user's existence, and feels the same. But there is something wrong with the true love. Something is terribly wrong.	A dead rose", "The Marble - The seasons in the current realm, suddenly switch (summer to winter, spring to autumn). Chaos ensues	A crude grass dolly", "The Criminal - The user is now a hunted person. Bountymen(and women) from the multiverse will begin to appear. An enemy from the Far Realms has put a reward on the user's death for X amount of platinum	A rabbit's foot", "The Ghost - A mad sage appears, that only the user can see, and follows the user for 1 year, babbling nonsense as well as snippets of truth, and sometimes peeks of the future	A small vial of laudanum", "The Cog - 255 Modron appear and ask the user one question - 'What is your designation?' Any answer other than '256' will result in the Modron experiencing a feedback loop and the entire group teleports 1-100 miles in random cardinal directions, where they will attempt to catalogue the local lifeforms and reunite with the collective. If '256' is given as an answer, the Modron will serve the user to the best of their ability short of suicide or death for 1 week, after which time they will return to the Outer Planes (Mechanus)	A handful of tiny cogs and gears", "The Ape - All the men in the closest civilized area suddenly become unnaturally strong, having a STR score of 23. They all become filled with rage for any living thing, but will not attack each other.	A tiny barbell", "The Cultist - The Hanged Man appears and will protect the user for 1 week. Treat as a 10th level Warlock with the stats of a Ghost	A small metal brooch in the form of an atom", "The Tomb - The next person that angers the user will die (no saving throw)	Handful of graveyard dirt", 
        "The Bottle - The user become allergic to alcohol in any form. Reactions include projective vomiting, chills, sweats, diarrhea, muscle cramps and headache	A cork", "The Deal - A business man appears at his desk. He is dressed sumptiously and looks quite comfortable, despite his infernal appearance. The devil says that the user's family is in debt to the tune of 1 dragon's heart. To be paid in full within 1 year or forfeiture of the user's life must be enforced.	A tiny iron chain", "The Box - A quantum tower appears before the user (and any companions). Each floor shows a different part of the realm, world, universe or multiverse, and never shows the same vista again after every sapient life form leaves the floor. The entryway always remains rooted in the location where it was first discovered. Climbing out of the window of each individual floor will allow physical transport to the location shown. After 24 hours the tower will vanish (taking any still inside the tower with it) and reappear somewhere else in the realm, world, universe, multiverse.	A tiny box", "The Quilt - All of the stars in the sky suddenly go dark. If it is daytime, its now nighttime, and will remain so for the next year.	A cloth blindfold", "The Tooth - For the next 12 full moons (assuming an Earth year), the user will transform into a different Therianthrope. The forms taken are always the last non-humanoid creature seen before the full moon rises. The change lasts until morning and the user will have full memories of what transpired. The new form is always Chaotic Evil.	An animal tooth", "The Flower - The user regenerates 1 HP per hour when exposed to full sunlight. In the absence of sunlight, the user bleeds for 1 HP per hour.	A magnifying glass", "Glasses - For one week the user will be able to identify an individual's alignment or general Good/Neutral/Evil tendencies upon sight.	A feather and a stone", "The Wife - All of the females in the world, regardless of race, now speak an additional language that cannot be understood, or learned, by men.	A tiny scroll inscribed with Lorem Ipsum",
        "Mini King - This little man is a brilliant military strategist. Undeterred by his diminutive stature, he whispers brilliant tactics into your ear promising to conquer the world. You gain advantage on the next Intelligence (History) check that you make regarding military history or battlefield tactics.", "Mini Queen - She's dainty and sweet, and she offers you a mini cake. You gain advantage on the next Charisma check you make to deceive, persuade, or intimidate a person of lower social standing than you.", "Mini Fool - This little guy slings some of the most offensive insults at you that you've ever heard. He uses vicious mockery against you (spell save DC 15). If you decide to squash him like a bug, no one will think less of you.", "Mini Death - All mosquitoes, houseflies, ants, small spiders, earthworms, minnows, butterflies, and creatures of similar size within 10 ft. of you die.", "Mini Magician - This little performer persists for 1 minute and will happily cast minor illusion or prestidigitation for you at will during that time. The mini magician must remain within 10 ft. or else he and any spell effects he creates disappear.", 
        "Mini Cup - There's a drop of wine in this thimble sized cup. It would get you drunk—if you were a pixie.", "Mini Sword - This little sword is big enough to slice a pea or a bean in half. It can be useful when your food supplies are running low.", "Mini Crown - The mini king storms out of the deck and demands that you place this card on top of his.", "Mini Scales - These scales are quite useful for accurately measuring extremely small quantities of alchemical reagents.", "Mini Sun - This card summons a mini sun that sheds bright light in a 10 ft. radius.", "Mini Moon - This card summons a mini moon. There is a 25% chance it is a new moon and sheds no light, a 50% chance it is waning or waxing and sheds dim light in a 5 ft. radius, and a 25% change it is a full moon and sheds dim light in a 10 ft. radius.", "Mini Stars - This card is a paradox. Stars are huge but they are so far away they appear as tiny points of light, yet hear you hold some in your hand. How is this possible?", "Mini Pincher - From this card reaches a tiny claw that attempts to pinch your hand. The claw makes the following melee weapon attack against you: +2 to hit; 1d3 bludgeoning damage.", "Mini Golf - This card transforms the area around you in a 30 ft. radius into a 9 hole mini golf course. The golf course lasts for 1 round.", "Mini Cooper - This little guy is rippling with muscles and will work tirelessly to make you mini barrels. Each barrel holds about 2 ounces of liquid. They work pretty well for small doses of potions and poisons. The mini cooper will make 1d4 mini barrels at a rate of one barrel per hour. The mini cooper must remain within 10 ft. or else he and any incomplete barrels disappear.", "Mini Me - A miniature replica of yourself appears. It is mute. It adores you. It is extraordinarily cruel to everyone else.", "Mini Ice Age - The area around you gets really cold. Water within 10 ft. of you freezes instantly and the air within 30 ft. of you is noticeably colder.", "Mini Liquor Bottle - A spot of whisky for a wee little lad? You can light the whisky on fire, dealing 1d2 fire damage to yourself if you do so.", "Mini Mouse - Is that mouse wearing a skirt?", "Mini Fridge - There are some snacks for the party (and the Dungeon Master) in here. Unfortunately, they are all smaller-than-bite-size.",
        "King Crab Legs - It's pretty good, especially with extra butter. You gain 1d4 temporary hit points, and you have disadvantage on Dexterity (Sleight of Hand) checks until you finish a long rest.", "Queen Mother's Meatloaf - It's kind of slimy, and 'Hey, there are vegetables in my meat?!' You have disadvantage on saving throws against disease and poison until you finish a long rest. You gain advantage on the next Wisdom saving throw you make before you finish a long rest.", "Foolish Turkey Bacon - This isn't bacon! This is a trick! You lose 1d4 hit points, and you have disadvantage on saving throws against disease and poison until you finish a long rest. You make all Intelligence checks with disadvantage until you finish a long rest.", "Death by Bacon - Mmmm. It is so delicious. How can this be bad for you? You gain 2d6 temporary hit points, and you gain advantage on saving throws against disease and poison until you finish a long rest. You also have disadvantage on the next Wisdom saving throw you make.", "Strength from Beef Jerky - Snap into it. If you shout 'Oooh yeah!' or if you start rambling about 'the madness,' you gain advantage on Strength checks made to grapple, to push, or to knock a target prone. This benefit lasts until you finish a short rest.", "Lucky Duck Confit - Some rave about it being crispy and delicious, but if you don't get it hot and fresh, it is soggy and disgusting. Roll a d20, on an 11 or higher, you gain the benefit of eating Death by Bacon. On a 10 or lower, you gain the 'benefit' of eating Queen Mother's Meatloaf.", "Pentacular Chicken Breasts - Star-shaped chicken nuggets. They're real, and they're pentacular. You gain 1d2 temporary hit points. You have advantage on all Charisma (Deception) and Charisma (Persuasion) checks until you finish a long rest.", "Filet Mignon Coins - This steak is pretty good. I recommend it with a bleu cheese sauce or crusted in black peppercorns. You gain 1d4 temporary hit points.", "Cup o' Mutton Chops - This stuff is putrescent. It might have been okay last week. You lose 1d2 hit points. You have disadvantage on all Charisma (Intimidation) checks until you finish a long rest.", 
        "Club of Lamb - It's hot off the rotisserie and tastes better than mutton chops. You gain 1d2 hit points. You have advantage on Constitution checks to resist cold weather until you finish a long rest.", "Sword Fish - This sure isn't the silver tuna, but you could do worse. You gain 1d2 temporary hit points. Once before you complete a long rest, you can reroll one damage die on a melee weapon attack that you make using a shortsword, a longsword, a greatsword, or a scimitar.", "Scaly Silver Tuna - Silver tuna tonight! You gain 1d2 temporary hit points. Once before you complete a long rest when can make one melee weapon attack you can treat your weapon as silvered even if it is not. Additionally, you gain advantage on the next Dexterity (thieves' tools) or Intelligence (thieves' tools) check you make before you finish a long rest.", "Pork Chop - It's a little greasy and chewy, but nourishing. You gain 1d4 temporary hit points. You have disadvantage on Charisma (Persuasion) checks until you finish a long rest.", "Prime Rib - Its nothing like the filet, but it is satisfying. Pair it with a decent red wine. You gain 1d4 temporary hit points, but you have disadvantage on the next initiative check you make before you finish a long rest.", "Smoked Brisket - This brisket is so bold, it will come to your house cook you dinner and then take your spouse into the bedroom. You gain advantage on Charisma (Intimidation) and Charisma (Persuasion) checks until you finish a long rest.", "Spicy Chicken - This will help clear those sinuses and fight off the chills. You gain 1d4 temporary hit points, and you have advantage on saving throws against disease and poison until you finish a long rest. Once before you complete a long rest when you make a melee weapon attack against a creature, you can breathe fire on the target. The target must make a Reflex save against a DC 15. The target takes 2d6 fire damage on a failed save, and half as much on a successful save.", "Sweet and Sour Pork - This is always a bit disappointing, but it could be worse. You gain advantage on saving throws against poison until you finish a long rest.", 
        "Turkey Leg - You feel extraordinarily festive when you sink your teeth into the flesh about the fat fowl's femur, but it does make you a bit sleepy. You gain advantage on Charisma saving throws and saving throws against being frightened until you finish a long rest. You also have disadvantage on all initiative checks you make until you finish a long rest.", "Veal Cutlet - It's stronger than that weak cup of coffee. Once before you finish a long rest, you can make a Strength check with advantage.", "Venison Sausage - With the right mix of spices, you can cover up the gamey flavor. You feel you could dash across the forest and leap enormous fallen logs. You gain advantage on Strength (Athletics) checks until you finish a long rest.",
        "The Dead King - You have a vision specifying the precise time and manner of the death of the sovereign ruler of the realm in which you currently are. The sovereign experiences the same vision. The sovereign's death will occur 3d10 days from the day you draw the card. You also learn that the sovereign's spirit will linger as an angry ghost that will haunt all future rulers of the realm.", "The Deadly Queen - You are overcome with the strong sense that the last meal you ate was poisoned. In 1d4 hours, you and all creatures who shared that meal with you gain the poisoned condition. At the end of the next long rest, you must make a DC 15 Constitution saving throw. On a successful save, the poisoned condition ends. On a failed save, the poisoned condition persists, and you must repeat the saving throw the end of your next long rest. If you fail the second saving throw, you die. Anyone who dies from this poison rises as a wight in 1d4 days.", "The Fool's Thought - You have a strong feeling that someone you are searching for to gain counsel and wisdom, to save from abominable circumstances, or to bring to justice yourself is already dead. In 1d4 days, you receive confirmation of that person's death.", "The Mad Magician - You have a vision of burning books and a magical massacre. The most powerful mage within 100 miles of your current location is overcome by madness. The mage seeks the greatest collection of books in the vicinity (an academy library, a temple library, or his own personal library) and sets it ablaze. The mage then seeks the most populated area in the vicinity and begins casting the most destructive spells within the mage's power. As people flee, the mage hides and seeks out another densely populated location to begin another massacre.", "The Dangerous Hierophant - You have a vision of many innocents slaughtered in the name of a god. The most powerful high priest or priestess within 100 miles of your current location begins a campaign of militant purification, assembling a mass of violent fanatics and ceremoniously executing all infidels that refuse to convert.", "Misfortune - You learn that you or one of your companions will be killed in a freak accident. You don't learn exactly when it will occcur, but you gain a vague sense of one particular object, place, or other person that will be involved in the accident. You also learn that the person's soul will linger as a disillusioned ghost.", 
        "Injustice - You gain knowledge that someone close to you (a traveling companion, a family member, or an old friend) will be put to death for a crime they did not commit. You also learn that the execution will occur in the 3d10 days. You also learn that the falsely accused's spirit will linger as a hateful ghost.", "The Hanging Tree - You gain knowledge that someone in your current company is a traitor and has sold you out to your enemies. You know who the traitor is, and you know that the veil of his or her treachery will fall in 2d8 days. If the traitor dies at your hand, he or she will rise as a revenant.", 
        "The Boss - A powerful devil manifests and speaks to you, promising you the thing your heart most desires, and begins bargaining for your soul. The devil fulfills its end of the contract in 1d4 days. You must fulfill your part of the bargain within 2d10 years. If you refuse, the devil will speak to someone known to you and convince them to betray you.", "The World. You gain knowledge of the time and manner of the world's ending. Unless another course is set, the world will cease to exist in 2d10 years.", "The Underworld - You have a vision of the earth opening up and swallowing an entire city or town known to you. In 2d10 days, a tremendous earthquake occurs and does just that. Almost no one in that location will survive. The region where the city or town used to be becomes haunted by many wraiths 1d4 days after the earthquake.", 
        "The Malign Stars - You have a vision of an immense, dark and hateful tentacular thing lurking beneath the sea. This thing will attack a coastal city or town that is known to you in 2d10 days. A significant portion of the city or town will sink into the sea, serious destruction will wrack the other districts, and many residents will perish. Those who perish rise as twisted aquatic ghouls 1d4 days after the attack.", "Blight - You have a vision of dead trees as far as the eye can see. The oldest tree within 100 miles of your current location dies instantly. A terrible blight spreads from that old tree. All other trees and plants within 25 miles of the oldest tree will be dead in 1d10 days, and all other trees and plants within 100 miles of the oldest tree will be dead in 3d10 days. The blight can continue to spread beyond that radius.", "Ashes - You have a vision of the burnt out shell of a city or town known to you. In 2d10 days, a terrible conflagration fill consume that location. Many of the residents will perish. Residents whose bones remain in tact through the disaster will rise as skeletons 1d4 days after the fire burns out.", "The Deathly Illness - You have a vision of a loved one taking deathly ill. That person falls ill 1d4 days from now and dies of that illness 2d8 days from now. Every day after you draw this card, 1d4 people who came in contact with your loved one while ill contract the same mysterious illness.", "The Death Plague - You have a vision of zombies shambling about a village or town familiar to you and within 100 miles of your current location. That location is rapidly afflicted with a zombie plague. Within 2d4 hours, 95% of the population will have turned into zombies. The following day, 1d4 additional settlements nearest to the plague's origin are also afflicted. This spread continues for 2d10 days. The plague can continue to spread after that.", 
        "The Boatman - You and up to eight creatures within 10 ft. of you are instantly transported to a graveyard or mausoleum in the Shadowfell. If you need to go back to where you were, you must find your own way back.", "The Executioner - You have a vision of yourself killing a loved one for some trifling wrong they did to you. Whenever you take a long rest, the vision repeats itself in a dream. After you finish the long rest, you must make a DC 10 Wisdom saving throw or be consumed by the vision. While consumed by the vision, you are convinced that your soul will not be at peace until that loved one dies. When you finish a long rest while consumed by the vision, you can make a DC 15 Wisdom saving throw to shake the vision. You continue to have the dreams, but you are no longer compelled to bring about what it foretells. If you successfully kill the loved one, he or she rises as a revenant. If you die before the loved one does, your ghost haunts the loved one until he or she joins you in death.", "The Children - You have a vision of a child with a sinister grin holding a bloody knife in the house of someone who is known to you and within 100 miles of your current location. This coming night, while asleep in bed, the owner of that house will be slain by a possessed child who lives in the same house. The following night, the same fate will befall the owners of all houses within 1 mile. The night after that, the same fate will befall the owners of all houses within 10 miles. Each person slain by this curse rises as a wight 2d6 days after dying.", "The Despair - You have a vision of dead children lying beside their toys, beside their favorite swimming holes, on their front porches, and along the streets of their neighborhoods. Every child under the age of 1d8 within 100 miles of your currently location suddenly falls dead. These children rise as poltergeists to torment the living who remain.",
        "The Chef - The cardstock automaton prepares a hearty feast.", "The Baker - The cardstock automaton prepares a tray of freshly baked cakes.", "The Bed - The cardstock automaton replenishes your spell components, as it can, or it polishes your spell focus.", "The Maid - The cardstock automaton polishes your relics and trinkets.", "The Dolt - The cardstock automaton builds a small campfire, in which it catches itself and burns.", "The Land - The cardstock automaton paces the ground in an ever increasing spiral to prepare a map of the area. It can cover an area of a radius of 100 ft - in 5 min. After this time, it returns to you if it can and it has drawn a map of the area on its own back side.", "The River - The cardstock automaton washes your laundry, during the process of which it transforms itself into a soggy mess of paper.", "The Match - The cardstock automaton sets itself aflame. It sheds bright light in a 5 ft. radius and dim light in a 10 ft. radius for 1 minute before burning out.", "The Insult - The cardstock automaton perches on your shoulder and waits for you to give it an order to slap someone in the face.", 
        "The Smoke - The cardstock automaton smothers the nearest candle or torch, snuffing out the flame and burning itself beyond repair in the process.", "The Page - The cardstock automaton organizes your notes, maps, or spells in a manner that you choose: alphabetical, chronological, categorical, geographical, or autobiographical.", "The Swords - The cardstock automaton polishes your weapons, armor, and boots.", "The Waterfall - The cardstock automaton refills your waterskin (and wineskin, if you have one).", "The Pentacles - The cardstock automaton perches on your shoulder and waits to warn you of the approach of any fiends by flicking your ear. It can detect the presence of a fiend within 100 ft.", "The Sticks - The cardstock automaton gathers firewood for you.", "The Ant - The cardstock automaton gathers bits of herbs and alchemical reagents as it can find in the area.", "The Runner - You speak a short message. The cardstock automaton jots the note down upon itself and scurries off to deliver the message to one person known to you who is within 1 mile.", "The Grasshopper - The cardstock automaton hops along beside you. When you command it to, it retrieves small items from your back and hops up to your hand with them.", "The Banker - The cardstock automaton polishes your coins and gems and organizes them within your purse.", "The Basin - The cardstock automaton rubs your tired travelers' feet.",
        "The Pocket - You find 10 gp in your purse that wasn't there before.", "The Purse - You lose 10 gp from your purse for inexplicable reasons.", "The Tunic - You find 5 gp up your sleeve.", "The Offering Plate - Your god takes 5 gp away from you, right from out of your purse.", "The Lost Coin - You lose 10 gp, but you find it again 2d12 hours later.", "The Trick - You spot a 1 gp piece on the ground. When you bend down to pick it up, it leaps away from your hand. Then you realize it is tied to a string just as some jerk pulls the string and puts the coin back into his own pocket.", "The Lamp - You find 5 sp shining beneath a lamp.", "The Pig - You find 10 sp scattered in some mud.", "The Guard - The local magistrate demands that you pay 10 sp as a fine for some minor infraction against the local laws.", "The Goblet - You find 1 sp in the bottom of your wine glass.", "The Brigand - A watchman demands a 5 sp bribe to keep quiet about your less-than-wholesome activities in the town (whether the accusation is true or not).", "The Opportunist - You drop 1 sp on the ground accidentally. It rolls over to an ugly, tough-looking brute who picks it up and pockets it.", "The Wish - You feel compelled to throw 2d4 cp into the fountain in the square outside the local temple.", "The Dust - You find 2d4 cp hidden in a dusty corner of the room.", "The Lottery - You find a purse containing exactly the same amount of coin that your purse currently is holding.", "The Tragedy - You lose your purse. Any objects other than coins that were in it are either on your person (in a pocket) or strewn about the ground.", "The Cupid - You find a pair of 2 shiny copper coins. You will have good luck in love!", "The Shattered Heart You lose 2 copper coins. This is often taken as an omen that something bad may happen in one of your relationships.", "The Outdoorsman - You are overcome by a sense that money doesn't matter. You feel particular charitable to causes you champion.", "The Trump - You are overcome by greed, possessiveness, self-importantance, and a need to vocalize whatever unreasonable thought pops into the space between your ears.",
        "The Warlord - The card bellows, 'Long live the king!' as it conjures a hobgoblin commander.", "The Statue - The card intones, 'Who is the fairest of them all?' as it conjures a medusa.", "The Theif - The card laughs maniacally as it conjures a goblin sneak.", "The Ogre - The card chants, 'Woogie-woogie-shazaam!' as it conjures an ogre mage.", "The Fungi - The card skitters across your palm as it conjures an ettercap.", "The Contract - The card shouts, 'No deal!' as it conjures a bearded devil.", "The Meat - The card drools on your hand as it conjures a werewolf.", "The Sewers - The card nips your hand as it conjures a wererat.", "The Bird - The card shrieks as it conjures a manticore.", "The Rock - The card grunts as it conjures a hill giant.", "Summer - The card singes your hand as it conjures a fire giant.", "Winter - The card turns painfully cold in your hand as it conjures a frost giant.", "Skeleton - The card mocks you, 'Dead is dead,' as it conjures a wight.", "The Fish - The card whoops, 'The madness! Woo!' as it conjures a kuo-toa warrior.", "The Goon - The card belches as it conjures an ogre with a greatclub.", "The Scales - The card hisses at you as it conjures a lizardfolk brute.", "Noon - The card cackles at you as it conjures a slavering gnoll.", "Evening - The card jeers at you, 'I'll get you, my pretty!' as it conjures a green hag.", "Night - The card coos at you, 'Sweet dreams,' as it conjures a night hag.", "The Severed Arm - The card scolds you, 'And that's why you don't draw cards from magic decks!' as it conjures a troll. ",
        "Seal/Walrus - Your body undergoes permanent changes. You gain a thick layer of blubber that gives you +1 natural armor and tusks as natural weapons. You lose 2 Dex and gain the language: Walrus. 'You bloat outwards, as if you've done nothing but feast for the past months. The extra weight seems protective enough, but slows you down.'", "Platypus - +2 Craft Alchemy with poisons. 'You gain a sudden insight in the brewing of poisons.'", "Sphinx - You gain a +4 bonus on diplomacy, bluff, and sense motive checks if you've used a riddle in a conversation involving the person you're attempting to converse with. 'You're hit with the sudden realisation that riddles  and rhymes contain more knowledge than any average sentence, and your mind begins to think in riddles, affecting your speech as well.'", "Dolphin - Your charisma is given a +2 modifier whenever speaking with aquatic creatures and you gain the language Aquan. 'You're granted an understanding of aquatic environments and their inhabitants.'", "Minotaur - Your race is suddenly morphed into a Minotaur! This changes your ability scores accordingly if they were physical. Mental stats stay the same. If you were already a Minotaur, you draw one new card. 'Without warning you begin to morph. Sprouting a tail, growing larger, getting hoofs and horns. Within a few seconds, you've transformed into a Minotaur.'", 
        "Dog - You swear allegiance to whichever party member has treated you best in the past, and gain +1 to all assists with or for that character. Lose 100xp per character level on death of the one you've sworn yourself to, this loss cannot make you lose a level. Lose 50 per level instead if you succeed a DC 15+Character level will save. 'A voice in your head speaks to you. 'Loyalty' it says 'Is the key to everything.''", "Squirrel - -2 Str. 'You grow weak, and frail, with a sudden passion for nuts.'", "Anteater - Gain +2 to hit, damage and caster level against Diminutive and Fine creatures. 'Glimpses of small animals appear in your mind. Their erratic and spontaneous movements appear confusing and difficult to predict, but only for a second. Suddenly, you see into their minds, and thus their next moves.'", "Rabbit/Hare - +10ft. Movement Speed, and ×2 damage to all kicks. 'You feel lighter on your feet, as if they've grown stronger.'", "Lion - Your next Intimidate check results in an ear shattering roar, granting you a +10, but dealing 2d6 Sonic damage to everyone within 60ft (Including you!). 'You feel a certain power reside in your chest, waiting to be released.'", "Raccoon - A random item from your inventory disappears. This happens in 1d3 days during the night, stolen by a specter. 'Nothing happens.'", "Rodent - You're infected with a random disease. 'You suddenly feel horribly ill.'", "Fish - You reek of fish, -2 Cha. 'As stench begins to surround you.'", "Sea Horse - Next creature you meet is compelled to do whatever you wish, as if under a Charm spell. 'Nothing happens.'", "Dragonfly - +4 Ref. -2 Fort. -2 Will 'Your movements become fast, but your mind and heart become slow.'", "Turtle - Movement speed is halved, as if by a Slowed spell. 'You feel sluggish, dragged down by some invisible weight.'", "Bee - -2 Wis. 'You're head is filled with the buzzing of bees, drowning out the outside world. You can practically feel them crawling around in your skull.'", "Centaur - The last weapon you used is granted a +1 magical bonus to a neutral alignment of your choice. Permanent. 'An animalistic voice speaks to you: 'Choose your enemies, before they choose you.''",
        "Owl - +2 to Wisdom, and rats taste amazing. 'You seem to have gained a better understanding of the surrounding world, and an urge to feed on rodents.'", "Phoenix - On death (-10hp, or whichever you use), explode as a 10HD widened fireball and be affected by true resurrection, all gear, including magical, is destroyed. Until this happens, your eyes glow with weak embers. Only works once. 'Your eyes glow like the embers of a dying fire.'", "Deer - -2 Will 'Each sound, each movement around you seems so sudden and loud. You startle easily. Even growing slightly paranoid.' ", "Crow - +4 on Perception checks if the object is shiny (metal, gems, etc.). 'You gain a newfound love for gleaming, shiny objects.'", "Skunk - A random item in your inventory begins to smell horribly. 'The stench is gruesome.' ", "Ferret - Eyes and hair randomly change color. (Hair: 1d6,1=Red,2=Brown,3=Black,4=White,5=Blond,6=Grey) (Eyes: 1d4,1=Brown,2=Green,3=Blue,4=Black). Permanent. 'You get a slight tingling sensation.'", "Boar - Grow tusks, speak in growls. -4 Cha. and roll a 1d4 when trying to speak. On a one it's just growls and snarls. 'Out from your mouth sprouts tusks, distorting your appearance and speech.", "Horse - You gain 20 ft. to your base movement speed, and can replace rations with grass in a grassy region, so long as you spend at least 2 hours per day grazing. 'You seem to have gained stronger legs and a more robust stomach.'", "Wild Dog - Gain +2 to tracking checks, track is always considered trained and a class skill for you. 'Your sense of smell is heightened.'", "Hippo - In combat you're considered to always be flanked, if you are actually flanked, the effects stack. +3 str. 'You feel slow, aggressive and highly unsuited for battle.'", "Quagga - Gain immunity to one energy type of choice, but GM decides another. 'You hear a voice in your head: 'Choose your strong side, and the gods will choose your weak one.'", 
        "Wolf - 1d6 Wolves are summoned around you to aid you per day. Wolves turn to dust at midnight, with a new 1d6 spawning out of the dust. 'You feel a sense of responsibility as a leader as wolves are summoned around you, waiting for their leader's orders.'", "Snake - Your legs merge into a 10ft long tail. You gain +10 to climb checks on cylindrical objects such as columns and trees. But you require specially made armour and clothing for your lower half, or you suffer -5 to saves vs cold weather, AC gained from armour is also halved until you acquire this. Humanoids consider you monstrous unless they know you well, and may flee. 'You feel your body changing.'", "Werewolf - The next person you converse with contracts lycanthropy. This effect is kept secret until it resolves. 'Nothing happens.'", "Cockroach - On death (-10hp) you have a 75% chance to stabilise at 0hp instead of dying. Unless subject to a disintegration effect or coup de grace. This effect can work multiple times. 'Nothing happens.'", "Parrot - +8 to bluff checks to imitate a language. 'You feel confident in your speech.'", "Shark - You can cast Locate Creature as CL5 once per day. This is succeeded by a combination of smell and magic. If you lose the ability to smell, you have a 50% chance of the spell failing. 'You seem to have received an ability from the gods.'", "Vulture - If anything dies within 60 feet of you, you are instantly aware of it. You can detect carrion and recently deceased creatures of size Diminutive or larger in a 60ft radius centered on your character at will. 'You become sensitive to the event of death.'", "Eagle - +2 Perception 'Your eyesight sharpens and improves.'", "Hummingbird - Put this card back, draw two, choose one. 'The card flies out of your hand, hovers in midair for a second, and dives back into the deck. Two more cards fly off from the top.'", "Koala - Nothing happens. 'Nothing happens.'", 
        "Lynx - The card effect of a random nearby person is negated. You draw a new card. 'The card flies out of your hand and floats in midair, suddenly another card appears next to it and they both fly back into the deck. A new card flies out to your hand.'", "Penguin - Every hostile creature within 50ft. is turned to ice.'As you draw the card, it creates an explosion of cold mist!'", "Whale - Instantly age 1d20 years. 'You feel as if time has caught up with you.'", "Fox - +2 Cha. 'You feel more confident in yourself, you just in your ability to convince other's you're confident.'", "Elephant - Put this card back in the deck. Draw three new cards, you get the effect of all of them. 'The card flies back into the deck, and three new fly out.'", "Alligator - +2 Str. 'You feel your muscles growing in strength.'", "Ant - You go down a size category, but gain +4 Str. 'You shrink in size, but yet your muscles seem ever more powerful.'", "Crane - Instantly change gender. 'Your body changes…'", "Cheetah - Every Time you roll Initiative, roll twice and take the best roll. 'You feel as if the surrounding world is horribly slow to react.'", 
        "Cat - +2 Acrobatics -4 Swim 'You feel agile and fast, but for some reason uneasy about the thought of water.'", "Lemur - You gain low-light vision, but also become nocturnal (Can not sleep if it is night time). 'Your eyes tune themselves to the darkness, but so does your mind.'", "Unicorn - If you are a spell-caster, you can pick one new spell to add to your spell list, otherwise draw one new card. 'You suddenly receive knowledge you didn't know you had.' OR 'The card is black and flies back to the deck. A new one flies out.'", "Gazelle - All predators and monsters are hostile to you. 'You feel watched.'", "Butterfly - You gain extremely frail wings, a single attack will completely destroy them, but you can negate fall damage as if by a Featherfall Potion until that time that they are destroyed. 'Large, beautiful wings sprout from your back. They look thin and fragile, yet durable enough to carry you.'", "Cougar - +10 Movement Speed, +2 Stealth in rocky, mountainous biomes, else you get -10 Movement Speed and -10 Stealth. 'You feel a suddenly longing for the mountains.'", "Tiger - All attacks you make that threat, are automatically confirmed, but so are all threats against you. 'You feel lucky and unlucky at the same time.'", "Duck - You fight from a crouched position at no penalty to you, and no benefit to your enemies. This is a compulsion and can be resisted for an encounter with a DC15 will save. 'You crouch. Why? Because.'", "Swan - Gain 1d4 charisma from your true beauty finally showing. 'You gained a divine blessing of beauty.'", 
        "Primate - +2 Climb, -4 Cha. 'You gained knowledge and strength about the arts of climbing, but your face morphed into a hairy mess with a large nose.'", "Hyena - +5 to demoralize your enemies with an intimidate check. 'You feel frightful. Terrifying. Fantastic.'", "Kitsune - Your race is suddenly morphed into a Kitsune! This changes your ability scores accordingly if they were physical. Mental stats stay the same. If you were already a Kitsune, you draw one new card. 'You feel your body changing!'", "Puffin - You shrink a size category but gain +2 Cha. Gear does not scale. 'You shrink in size, but feel more attractive'", "Dragon - Grow one size category and gain +2 to strength. Gear does not scale with character and can inflict 1d6 points of damage per AC gained from metallic armour. 'You grow in size, as does your strength!'", "Opossum - You gain +2 on Deception checks under duress. 'You feel like you can fool your enemies.'", "Gryphon - Two magic items in your inventory swap effects. 'Insert effect here.'", "Hawk - A random item on your person becomes sentient. 'Insert effect here.'", 
        "Kangaroo - You are always considered running when making a jump, but you require specially made footwear for your enlarged feet. 'Your feet grow in size, as does their strength.'", "Dingo/Dhole - Every assist you receive counts double, as does every assist you do. 'You understand now that allies are the key to success, to victory.'", "Bat - You go permanently blind, but gain the ability to echo-locate. As long as there is sound, your character can see. Your character is unaffected by darkness (concealment, miss chances, etc.) but you take extra damage from sonic attacks. 'You sight grows dark, your vision slips. Soon enough, you're entirely blind. Suddenly, a nearby sound lights up the room, giving you vision again, as if the sound is light.'", "Frog - Gain a +2 bonus on jump checks if you jump from crouching. 'You feel a sudden surge of power in your legs.'", "Giraffe - You gain a +2 to Survival if looking for food. 'You seem to have received some previously unknown knowledge.'", "Zebra - Your alignment shifts permanently to the opposite end of the spectrum (Good < > Evil as well as Lawful < > Chaotic). If you're true neutral, draw again. 'You mind changes, as do your morals.'", "Jaguar - An outsider sets his mind on destroying you. 'You hear thunder, then, nothing.'", "Porcupine - You spontaneously grow large spikes over your whole body. They effectively increase your size by 1 category, before dissolving into dust and returning you to your normal size. Destroys all armor and clothing. 'Giant spikes begin to sprout from your body, painfully and quickly. They continue growing for a few seconds, almost doubling your size before they turn to dust, leaving no scars. Your armor and clothing  on the other hand is ruined.'", "Panda - Gain +2 to wisdom, but -2 dex, and you require double the amount of food. 'You see the world in a new light, your mind has improved. Your body on the other hand feels sluggish...and hungry.'", "Rhino - Ignore penalties to AC from charging and gain a further +2 to hit and +2 to damage when charging. 'You feel as if you've gained an invisible strength.'", 
        "Satyr - This card does nothing immediately, but next combat, failing a DC 15 will save results in a compulsion to dance during combat (ie: boots of dancing). 'Nothing happens.'", "Scarab - You gain a +2 bonus to saving throws against endure warm elements, but a -4 against cold. 'You long for the warmth of the sun...and begin to fear the cold.'", "Thylacine - You gain access to the attack granted by the feat Whirlwind Attack once per day. 'You've received a newfound knowledge of battle.'", "Spider - You can use Spider Climb with a CL equal to your character level three times per day. 'Your hands become sticky and your mind is filled with images of spiders.'", "Leopard - Unarmed attacks deal an extra 1d6 lethal damage. 'Your hands grow in strength and claws grow out from your fingers.'", "Okapi - You receive two visions, one true, one false. 'Insert visions here.'", "Wolverine/Badger - For every crit. you confirm, confirm again to deal even more damage. If you do manage this second confirmation, you deal your weapon's damage to yourself as well (For example 1d8 for a crossbow). 'You feel more powerful in combat, as if being watched by the gods of battle...but at the same time, you feel vulnerable, as if you're being tested.'", "Sabertooth Cat - 1d6 copies of you are created within a mile. All have the polar opposite alignment from you, and oppose your goals. 'Nothing happens.'",
        "The Sidekick - A member of the goblin or gnome or pixie or any other dumb/jokey/mad race of DM's choice appears besides you. He/she will promise eternal obedience to you, but every order you give to him will end up with getting yourself into troubles. Also, he will always speak his mind on everything, often bringing up very strange and unpopular opinions.", "The Spell - The next time the nearest grimoire is opened, the page at which it was opened flies away as it was blown by the wind.", "The Artifact - The most important relic of the reign vanishes into thin air.", "The Harvest - Crops begins to rot in all the kingdom.", "The Coronation - The king is murdered.", "The Appointment - The higher rank among the most followed cult is kidnapped by members of the opposite cult.", "The Baby - Women in the kingdom became sterile.", "The Victory - Something in your near future will go irremediably wrong. No matter how much preparation or how much efforts you put into it. You will fail your next task.", "The Hero - The party is accused of a crime that they have not committed.", "The Planner - You lose any form of caution. If no one else stops you, you keep drawing cards from the deck.", "The Abundance - The rich become poor and the poor stays poor.", "The Protector - Fear strikes into your mind, distorting things around you into monsters. Also, in your sleep you experience vivid nightmares that often carry on when you wake up.", "The Law - In the kingdom no one else follows the law, chaos ensues.", "The Grave - The next time you would die, you don't.", "The Preist - You start filling with exaggerations and cursing every phrase you say.", "The Shadow - The nearest cursed item is purged.", "The Oppression - An enslaved race or the BBEG or a big captive monster is set free.", "The Clear Day - The BBEG makes a big step further with his plans.", "The Stormy Day - The BBEG has some difficulties going on with his plans or the party randomly finds a shortcut.", "The Spring - It's night. And will be night for a very long time...", "The Peak - The next time a player would level up, he/she doesn't.", "The Family - You lose what you love more than anything else.",
        "The Duplicate - A portal through time opens and your future and past selves confront eachother for a moment. You gain insight into one event from your past that was a mystery to you, and a portent of one event in the future that will place you in peril.", "The Seer - You learn the weather patterns of your immediate general location for the next month, and can perfectly recall them at any time.", "The Broken Hourglass - Your body becomes time-locked. Though you may take actions and be wounded etc. as normal you do not physically age for the next ten years. This can extend your lifespan.", "The Future - You become frozen by indecision, seeing as many possible futures as a gorgon's head has eyes. You cannot gain advantage on any saving throw, ability check or attack roll while this effect is active. It can only be removed by divine intervention to soothe your mind or via The Fates.", "The Past - You see the weave of fate and may change it in a small way. Pick one event that occurred to you in your past, you may change it to have had the outcome you desire or to have never happened at all.", "Doom - A vision of coming doom assails you. The experience is harrowing and you have disadvantage on all Wisdom saving throws and skill checks until you finish a long rest, but you gain insight into the machinations of a powerful fiend with designs on your world. Unfortunately it also receives a vision of you and your plans, learning your name and appearance.", "The Lost Sheep - Your memories of everything before two years ago are erased, they may be restored via some means but no mortal magic can do so.", 
        "The Horde - A crystal clear vision of wealth appears to you, you learn the location of a valuable treasure worth at least 25,000 gold pieces", "The Brain - You begin to forget things easily, and can no longer recall any specific details about people and places you have not seen in the past week.", "The Plight Your future is fixed and you will make a fool of yourself at the next opportunity when it will embarrass you in front of a large group of people.", "The Clairvoyant - You learn the solution to a puzzle or conundrum of the DM's choosing, gaining perfect clarity for an instant. For the next 24 hours you have advantage on all Intelligence based skill checks.", "The Fighting Master - The knowledge of a noble and skilled fighter echoes down the ages to you, granting you proficiency in one weapon of your choice.", "The Whisper - You see a reflection of the future, it is a vision of an event that will occur within a month but conveyed in metaphor. e.g. a betrayal may appear as a vision of you being bitten by a snake, or a sudden financial windfall may be shown as you eating a bountiful feast.", 
        "The Master Theif - The knowledge of a dashing and skilled agent echoes down the ages to you, granting proficiency in one skill of your choice.", "The Prophecy -You see the destruction of something or somebody you hold dear, while the method is revealed to you the context or the timing is not. It is up to you to find out the when and why if you wish to prevent the prophecy.", "The Forefather - The bones rattle as you gaze into time, you may speak with one deceased person whose soul is free and willing and ask them three questions which they must answer honestly and to the best of their ability.", "The Constellation - Your past changes, as though you had always been born under a lucky star. You gain one Luck Point to be used as described under the Lucky feat.", "The Plan - The future burns bright in your eyes as you see its full glory. A vision of a coming event is fully revealed to you in exact detail.", "The Lost Trinket - A random item you possess is thrown through time, vanishing into the continuum. You may or may not encounter it later, but it is unlikely.", "The Home - You see a vision of a small keep somewhere in the multiverse that will soon be unclaimed and ripe for the taking. However several other interested parties (who exactly is determined by the DM) also see this vision, and desire the stronghold for themselves.", "The Counsellor - At any point in the next year you may meditate and ask one question about a future course of action, you will receive a truthful insight into the odds of success, the potential pitfalls and the exact nature of any opposition to the plan.", "The Tendrils - You see through time to the beginning and end of all things, and glimpse the space beyond. Gazing upon this location is anathema to beings of linear time such as yourself, and you gain a form of madness determined by the DM.",
        "Ally - A nonplayer character of the DM's choice becomes enamored with you. The identity of the new friend isn't known until the NPC or someone else reveals it. The NPC will do everything in their power to aid you as though you were a life-long friend.", "Arcane - You lose all forms of wealth as per the Ruin card, however you are compensated by the gods with a magical item that appears at your feet.", "Bull - You feel great strength coursing through you, but at the expense of your mind. Roll 1d4 and add that much to your strength score. Subtract the same amount from your Intelligence score.", "Cat Burglar - You feel yourself growing nimbler and more agile, but at the cost of your wisdom. Roll 1d4 and add that much to your Dexterity score. Subtract the same amount from your Wisdom score.", "Stars Aligned - If you single-handedly defeat the next hostile monster or group of monsters you encounter, you gain enough experience points to gain one level. Otherwise, this card has no effect.", "Doppelganger - Somewhere in the world, an exact duplicate of you appears. It has the same appearance, equipment, and knowledge as you. The only difference is that its alignment is opposite yours. Lawful becomes chaotic, and good becomes evil, or vice-versa.", "Feeble - This card's medusa-like visage curses you. You take a -2 penalty on saving throws while cursed in this way. Only a god or the magic of the Fates card can end this curse.", "The Golden Thread - Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. You can use the card's magic as soon as you draw the card or at any other time before you die.", 
        "The Burned Pages - Lose 10,000 XP, discard this card, and draw from the deck again, counting both draws as one of your declared draws. If losing that much XP would cause you to lose a level, you instead lose an amount that leaves you with just enough XP to keep your level.", "Gambler - You add 2 to your number of declared draws. You must draw them as if they were in your initial number of declared draws.", "Golem - You gain a tough exterior and more hardy body, but at the cost of your charisma. Roll 1d4 and add that much to your Constitution score. Subtract the same amount from your Charisma score.", "Guillotine - This card signals peril. You magically lose one limb or appendage, the wound healing instantly except for the limb. Roll 1d10. The number rolled determines which limb is lost. See the lost limb table for additional details. Lost Limb Table: d10 10: One Ear 9: One Finger 8-7: Left Foot 6-5: Right Foot 4-3: Off Hand 2: Main Hand 1: Head (Death)", "Artist - Twenty-five pieces of jewelry worth 2,000 gp each or fifty gems worth 1,000 gp each appear at your feet.", 
        "Jester - You gain 10,000 XP, or you can draw two additional cards beyond your declared draws.", "Craftsman - A rare or rarer magic weapon with which you are proficient appears in your hands. The DM chooses the weapon.", "Lightfoot - You feel your steps become lighter, making moving easier. You permanently gain 10 movement speed.", "Mire - You feel your mind slow as your draw his card. You cannot keep your defences up as efficiently in combat, permanently suffering a -2 penalty to AC. Only a god or the Fates card and end this curse.", "Riches - All magic items in your posession instantly disintegrate or disappear as per the Talons card, however you are compensated by the gods with 5,000 platinum pieces (woth 10g each)which appear at your feet.", "Enemy - A nonplayer character of the DM's choice becomes hostile toward you. The identity of your new enemy isn't known until the NPC or someone else reveals it. Nothing less than a wish spell or Divine Intervention can end the NPC's hostility toward you.", "Peasant - All forms of wealth that you carry or own, other than Magic Items, are lost to you. Portable property vanishes. Businesses, buildings, and land you own are lost in a way that alters reality the least. Any documentation that proves you should own something lost to this card also disappears.", "Sage - You feel a transformation in your mind, bringing with it the wisdom of an old wise one. However, you also feel ourself becoming less agile with your newfound wisdom. Roll 1d4. Add the number to your Wisdom score, and subtract the same amount from your Dexterity score.", 
        "Scale - You instantly age by 2d10 years, taking the same amount as phychic damage. You then have advantage on all skill checks that you and proficient in, and disadvantage in all others. A god, a wish spell or the Fates card can reverse this effect.", "The Book - Your mind undergoes spontaneous growth, and you feel yourself becoming more intelligent, but at the cost of your physical strength. Roll 1d4. Add the number to your Intelligence score, and subtract te same amount from your Strength score.", "Revenant - You summon an avatar of death - a ghostly humanoid Skeleton clad in a tattered black robe and carrying a spectral scythe. It appears in a space of the DM's choice within 10 feet of you and attacks you, warning all others that you must win the battle alone. The avatar fights until you die or it drops to 0 hit points, whereupon it disappears. If anyone tries to help you, the helper summons its own avatar of death. A creature slain by an avatar of death can't be restored to life.", "The Expert - Increase one of your Ability Scores by 2. The score can exceed 20 but can't exceed 24.", "The Trick - Every magic item you wear or carry disintegrates. Artifacts in your possession aren't destroyed but do Vanish.", "The politician - You gain proficiency in the Persuasion skill, and you double your proficiency bonus on checks made with that skill. In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently in the hands of Monsters, which you must clear out before you can claim the keep as. yours.", "The Silver Tongue - You feel a change in your mind, feeling yourself able to speak and act more persuasively. However, this comes at the expense of your physical endurance. Roll 1d4. Add the number to your Charisma score, and subtract the same amount from your Constitution score.", "Tribe - When you draw this card, you instantly die and are brought back to life as though Reincarnation had been cast on you.",
        "The Rose - A creature of the DM's choice falls madly in love with you, and will stop at nothing to be alone by your side.", "The Drake - A Dragon of the DM's choice appears in the nearest open space, and immediately attacks.", "The Magi - A scroll for a random spell appears in your hand. Roll 1d10 -1 to determine the spell's level.", "The Coin - You gain 1d10 x 1000 gold pieces. These coins are contained within a chest, which appears within 20 ft of you.", "The Mountain - Your body is petrified, although you can still speak, and move somewhat freely. Your movement speed is halved (minimum 15 feet), your weight is doubled, your Dexterity score is decreased to 1, you have disadvantage on attack rolls, as well as Dexterity checks and saving throws, you become vulnerable to Thunder damage, resistant to non-magical damage, and immune to poison and disease. This effect lasts until removed by the Greater Restoration spell or similar magic.", "The Mask - A random creature close to you loses all memory of you.", "The Bear - Assign each of your ability scores a number 1-6 and roll 1d6. Increase the corresponding stat by 2 to a maximum of 30.", "The Mirror - An exact clone of you appears within 20 feet of you. The clone has your exact stats, appearance, equipment, and abilities (regardless of requirements for those abilities), but exact opposite alignment. If the clone can cast spells, the DM determines what spells it has. This clone immediately attacks the creature it is a clone of. In addition, it believes that it is the original, and you are the clone. You must then fight them in single combat. Anyone who tries to help you will receive a clone to fight as well. The clone dies after failing three death saving throws, and it, along with anything it possessed, is irrevocably destroyed. This happens to you if your clone kills you. If you are True Neutral or unaligned, this card has no effect, returns to the deck, and you must draw again.", "The Ring - You become betrothed to the princess of the nearest kingdom (wherever they are). Messengers are sent to deliver summons to the wedding.", "The Crown - A non-magical, jeweled trinket worth at least 1000gp appears somewhere on your body. For example, a necklace would appear around your neck, and a ring would appear on your finger.", "The Clover - You automatically succeed on the next ability check or saving throw you make within 24 hours of drawing this card.", 
        "The Raven - Your closest friend becomes hellbent on killing you.", "The Vial - At dawn of every day, 1d4 Potions of Greater Healing appear at your feet. However, any unused potions from the previous day cease to exist.", "The Coward - Every time you roll initiative, you must also roll a Wisdom Saving throw (DC 15) to avoid getting Frightened. This effect lasts until dispelled by Greater Restoration or similar magic.", "The Well - You gain the ability to cast the Wish spell once. If you draw this card while under its effects, you do not gain multiple wishes. You must use this wish within one year of drawing this card. Additionally, you must roll 1d20 when you make your wish. On a roll of 1, the wish is not granted and the casting is wasted.*", "The Snake - Each of your ability scores is permanently decreased by 1 (minimum 1).", "The Bard - An instrument of the DM's choice appears in your hands. You gain proficiency with this instrument.", "The Tree - Your height increases by 1d4 feet.", "The Fang - 3d4 Wolves, 2d4 Dire Wolves, and 1d4 Winter Wolves appear within 30 feet of you, each in its own space, and immediately attack.", "The Heart - Your Hit Point Maximum increases by 1d20 + your Constitution modifier + your level.",
        "The Adept - Magic users can gain an additional level 2 spell slot, or two level 1 spell slots. Non-magic users gain access to a cantrip (randomized or player choice) and may cast it as if they are a sorcerer or wizard of their current level.", "The Sinner You are cursed to indulge one of the seven deadly sins in excess for a whole week, and can only overcome the effects when they press with a DC18 constitution save.", "The Joker - Once a day, your character may send them self into a laughing fit for no less than ten minutes. This fit of boundless happiness will clear fear and sadness based debuffs for 1d4 hours, and will inspire the character for 10d4 minutes.", "The Ram - While this curse is active, which is at any point the sun has set or cannot be directly seen, the cursed will act upon any hostile emotions with a deep rage, usually engaging the minor inconvenience in combat. This includes inanimate objects. While cursed, the creature will also believe that inanimate objects can not only hear it, but are actively trying to argue with them if they become enraged towards that object.", 
        "The Treaty - The character immediately gains 2d2 charisma, and also the ability Enemy of my Enemy. Enemy of my Enemy allows the user to attempt convince a creature that it is not friendly with that they share a common enemy, and the creature must then pass a DC16 intelligence check or become convinced. Creatures convinced this way will strive to take out this common enemy with the character, but will still maintain their hostile emotions, typically seeing it as an uneasy alliance. The effect wears off after 1d4 days. This curse lasts one month.", "Teh Illusion - The cursed becomes flogged with visions of horrific things at every waking hour, and must pass a DC16 intelligence save or become frozen with fear. The visions will also drive the user to attack any nearby creature if critically failed on a roll of a natural 1.", "The Eye - The creature can witness any event another creature has witnessed as if it were through their own eyes once per day. In order to activate this effect, the creature must succeed a DC14 Charisma check.", "The Paraniod - The cursed will slowly begin to believe that it has become hated by their allies for inexplicable reasons. It will seek at any possible test of faith to not only prove, but over-prove its loyalty to its allies, almost always to its own detriment. The curse ends after one week.", "The Cleanly - The user gains the cleaning and soiling ability of prestidigitation and can use it any time they come in contact with an object. Additionally, the user may spend one entire day with an object to 'masterwork' it, making it better than it was before. For weapons, their hit dice are split in two (IE 1d8 becomes 2d4, 3d6 becomes 6d3, ect.), and for armor, they become indestructible while worn by the user that 'masterworked' the item. Other things may be 'masterworked' to the DM's discretion.", "The Mistake - Twice per day, something the cursed says may be instead spoken as a horrible insult towards who they are speaking to. This effect is significantly more likely to happen the first time the cursed meets a new creature, often being the first words they say.", 
        "The Reward - Any time the affected takes damage for the next year, they gain 1sp per each point of damage taken. This currency will always appear on their person, and if there is no room, in their person.", "The Shield - Any damage the user takes will have 50% of it redirected to a random creature nearby. If no creatures are nearby, the user instead takes 50% more damage than they should have.", "The Beard - The user gains a permanent +2 to charisma, and can change their facial hair to anything they wish at will.", "The Stick - Once per day for an entire year, the user will trip and slam face-first into the ground. This will always result in 1d4 bludgeoning damage. The user must then roll 1D20, if this roll is a critical fail, roll again. If the second roll is also a critical fail, the cursed will have their HP reduced to 0.", "The Encyclopedia - Intelligence permanently increased by 2. Additionally, the user immediately becomes intimately aware about one fact involving every creature they meet for the first time thereafter.", "The Parent - Your parents find you. If they are dead, they are revived as if the 'resurrection' spell was cast on them a mere moment after they died. Both of them will be acutely aware of everything their child has done since the last time they saw them, and will berate them for every single negative thing that has happened. This demoralizing encounter will make the cursed unable to leave until their parents are done, and it will take a minimum of 1 hour to get through. Additionally, their parents will end their own lives immediately after.",
        "Upheaval - Changes the alignment of the Deity worshiped by the character who draws it.", "The Black Cat - If the character refuses to participate in the next hostile combat and the party must retreat, the character gains an experience level. If the character participates or informs any other member of the party, they lose an experience level instead.", "Freedom - Instantly relieves the character of all imprisonment/deals/obligations/pacts/geases that they are subject to, and makes them the undisputed owner of all objects on their person.", "Stonesalve - The character gains a permanent bonus to all saving throws.", "Chaos - Immediately and irrevocably locks one aspect of the character's fate, forcing it to occur as soon as possible. However, after the event is satisfied the character no longer has a fate; any prophecies regarding the player are unmade or redirected, and any attempts to view their future are unsuccessful.", "The Frost - Causes an outsider to immediately ally themselves with the character", "The Sage - The character gains experience and is unable to draw further. Unless another character intends to draw from the deck, it disappears immediately.", "Asceticism - The character immediately loses all wealth, including land and titles, and is left with only their current non-monetary possessions.", "The Genius - The character receives a permanent bonus to intelligence", "The Cynic - The character may choose to either lose experience points, or negate the last two changes brought about by this deck. If the character chooses to negate the changes they are only nullified, not undone, and any consequences rendered remain unless corrected.", 
        "The Lock - The most powerful magic item within 100 feet of the character is instantly removed to a nearly unreachable place, and the character is aware of it's new location. If no magical items are present, the nearest magical creature is removed instead. This card does not consider the deck a valid target.", "The Peon - A worthless, skill-less person appears and dedicates their life to obstructing the character. They cannot be killed, and if restrained they will escape and find their way to the character in 1d4 days.", "Redemption - An enemy of the party becomes an ally.", "Security - The character is unable to lose possessions, willingly or unwillingly. Anything dropped, stolen, or removed from the character will return to them, or to a property that the character owns (determined randomly) in 1d4 days.", "The Blossom - The character must assist a minor angel with a task assigned by it's god. This compulsion can only be removed by Freedom or The Cynic.", "The Soil - The character suffers a permanent -2 detriment to a stat of their choice.", "The Exile - The character suffers a permanent penalty to Diplomacy and loses all land and titles that they have. They lose all citizenship, and are incapable of gaining citizenship in any nation.", "Cassandra - A problem that the character has solved in the past returns, and cannot be dealt with the same way that it previously was.", "Creation - The soul of another person is trapped within the character's body. The character may access the soul's knowledge or skill, but each time they do the line between the two souls becomes more obscured, eventually resulting in either the reversal of the souls' positions of power in the body, the merging of the souls, or the destruction of one or both of the souls.",
        "The Maiden : A random person you have met throughout your adventure becomes hopelessly, obsessively in love with you", "The Wizard : You may choose a spell from the first level list of wizard spells and once per day that spell may be cast without expending a spell slot. Using it at higher tiers still uses higher tier spell slots.", "The Mountain : You permanently grow by one size class. The only way to undo this is a wish spell.", "Sloth (As in the Sin) : You fall into a deep sleep and will not wake by any normal method. You are magically sustained and your body does not age while this effect is active.", "The Mime : You lose the ability to speak. Can only be cured by a wish spell ", "The Sun : You glow brilliantly like the sun and shed bright light in a 60 foot radius around you, and dim light up to 180 feet. ", "The Comedian : +2 To charisma skill checks and saving throws. -1 to all others. ", "Wrath : You gain the flaw 'I am quick to anger, driven to extract vengeance from those who have wronged me and a real bear first thing in the morning.' ", "Greed : all non-magical coins, trade goods and other currency, gemstones and art objects on your person, held in your containers (including e.g. a bag of holding), stored within your legal property or held on your behalf in a bank or other institution under your name are instantly replicated 10 times. The copies are identical and indistinguishable, including any identifying features, flaws or serial numbers. If there is insufficient space for them to be held, the objects spill out, rupture or otherwise force their way into the world. ", "Gluttony : You develop an insatiable hunger. Your normal requirements for sustenance are doubled and you find it difficult to stop consuming. If you do not currently require sustenance, or if you are unable to satisfy your newly increased needs for 48 hours, you develop a need to consume something unusual, taboo or difficult to acquire. ", 
        "The Void : (opposite of the Sun) Light seems to dim when you are around. If you are in bright light, it becomes dim light for a 60 ft radius around you. If you are in dim light, it become dark for a 60 ft radius around you. Creatures can not see you, unless they have true sight, if you are in dim light. (Similar to the Darkness spell) ", "Serpents : You immediately contract a poison that will kill you in 1d10 days. The only way to cure it is with a potato from a different continent. Your character and party know this] ", "The Orchard : You gain an apple, that, when bitten into, heals itself over time, effectively granting you infinite food. However, if another person were to bite the apple, it would become just a normal apple. Your character does not know this.] ", "4 Leaf Clover : the card turns into a 4 leaf clover that is unaffected by the use of force or magic and can only be destroyed by the use of the wish spell or Divine intervention. The creature in possession of this clover is imbued with great luck and gains the following abilities. You may pick one ability where any ability checks, skill checks, attack rolls, or saving throws that you make using that skill automatically succeed for 24 hours. Using this feature drains the available luck from the artifact for 1d4+1 days rendering it useless for that amount of time after the 24 hours expire. Once per day, you can change any dice roll you make excluding d100 to be equal to x-1 where x is the number of sides on the dice. This must be done prior to finding out the result of the action intended by the roll. Once per short or long rest, you have advantage on one ability check and one saving throw of your choice. ", "Lust : Every person you meet of the opposite sex must make a dc10 wisdom saving throw or immediately try to seduce you from now on.", "The Orchestra : summons 20 unseen servants that repeat everything you say/sing. If you cast a spell with a verbal component, it counts as being one level higher if applicable. You also have advantage on performance checks. The Unseen servants do not obey your commands and last until killed. ",
        "The Liar : you gain advantage on Deception checks but you are unable to tell the truth — your party has to roll Insight checks whenever you reveal to them information ", "The Crystal : Your skin crystallizes. Your speed decreases by 5 feet and you are put under the effect of a stoneskin spell. ", "Uno Reverse Card : Allows the user to hold up the card to deflect things back at the person who the card is facing, once per short or long rest. ", "The Cornicopia : you no longer need to eat, drink, sleep, or breathe, and you do not age. ", "The Fates : You gain the Lucky feat, but you have also gained The Fates disdain. When you re-roll your dice using the Lucky feat roll an additional 1d4 and subtract it from your new roll. ", "The Smith : This card immediately transforms into a +3 Warhammer that deals an additional 1d8 fire damage on a hit. The person who drew this card becomes proficient with Warhammers and loses all other weapon proficiencies. ", "The Coin : Immediately after drawing this card the users hand is burned and takes 1d4 damage and drops the card as a reaction to the pain. As the card is falling to the floor it transforms into a coin. If the coin lands face up (Heads) the person who drew this card doubles the amount of currency they are carrying. If the coin lands face down (Tails) the person who drew this card has their currency vanish. The Coin itself is now worth 50gp. ",
        "The Beast : Once per day, you can Wildshape. Upon transforming back into your normal self you take 1 point of Exhaustion. ", "The Leviathan : A great beast has your scent. It will arrive in 1d10+5 days or at the DM’s choosing. Only you can slay the beast and all damage not caused by you directly or indirectly (such as through traps) is halved. ", "The Casino : You are transported to the demiplane of luck. This demiplane consists of a silver road in a desert with extravagant casinos glowing with displays of light against the permanent night sky. The casinos themselves are owned by the permanent residents of the plane, known as the Casino Barons. Barons include everything from human crime bosses to powerful wealthy monsters such as cloud giants, red dragons, and genies. The casino's appearances match with the baron or baroness who owns it. ", "The Blank : When you draw this blank card it begins to emit bright light and smoke, than dissapear along with whatever equipment you had on you. The card then drops to the floor. The next person to pick up the card sees a stylized image of you printed on it. They will recieve an item, ability, or personality trait from your character sheet at the GM's descretion. The effects can be reversed with a wish spell. ", "The hermit : You gain disavantage on any charisma checks. You gain advantage on any wisdom checks. Can be undone by a wish spell. ", "The Clock : You gain a small tattoo of an oddly-shaped arrow somewhere on your body. The tattoo is imbued with magical power, and will appear as a transmutation effect when viewed with Detect Magic. As an action, you may invoke this power to cast Time Stop. Once the spell ends, the power is lost forever. ", "Judgement : you forever feel sickened when in the presence of evil-aligned people, and forever anxious around those of chaotic alignment. ", "Temperence : you can no longer feel intoxicated, no matter how much you drink. Furthermore, you are made immune to damage/drain of your int, wis, and cha, but also immune to effects that raise those abilities ", "The world : you are teleported to a random location on the other side of the world.", "The Pack : 1d6 hell hounds come every 1d10 days to try and bring the person who drew the card down to the nine hells. The player can hear the howls, and is frightened for 1d4 rounds when they come. ", "The Blind Man : your character is now permanently blinded, physically losing their eyes, and gains tremorsense up to 30 feet. ",
        "The Artist : your character is now exceptionally skilled in a random art(painting, cooking, singing, etc.) and is known around the world for their talent. ", "The Fib : your character is now a pathological liar and must make a Wisdom saving throw to tell the truth about anything their audience doesn’t already know(I.E, can state the obvious, but must roll to explain a plan or tell a secret truthfully). ",
        "The Goblin : Permanently gain +2 to dexterity and Constitution Permanently lose -2 to charisma and intelligence ", "The Mirror : whoever draws this card immediately understands to an instinctual, spiritual, emotional, and/or philosophical degree why their most hated enemy/enemies are the way they are and are doing what they're doing. They are able to completely sympathise. ", "The behemoth : when next the character is slain in battle, they shall rise again with temporary hit points double that of the nearest healthy enemy. For the battle, they lose the ability to cast spells, but their Strength score temporarily increases to 30 (+10). When the last nearby enemy dies, they return to normal, and are rendered unconscious, but stable at 1 hit point. ", "The Mask : You immediately, and permanently change races into a random race. You retain all of your memories of your previous life, but lose all ability score changes and abilities your previous race granted you. You gain all ability score increases and/or abilities that this new race grants you. (NoireGarde)", "Dead weight : a 5 ton steel cube appears with shackle welded onto it. you are shackled to it. you cant move five feet from the cube until its shackle is removed. if it is removed, the cube and shackle disappear. (By Tobymaxgames", "The fondler : you can cast mage hand if you couldn't before. this doesn't require a spell slot. ",
        "The substrate : a boulder, weighing 3d12 tons appears in above a random person around you, and promptly falls down. its made of some type of metal ore. it its in your possession, and you may do what you will with it. ", "The captain : if the drawer of the card owns some type of vehicle (cart, boat, etc.), they will physically merge with that vehicle. a wish spell is undo the merge. ", "The Holdout : after drawing, the location you take a long rest at is converted into some type of fortified structure. the structure takes a form that makes scene for its location. a forest will grow a great tree fort. fields become palisade camps. mountains spring forth castles to rock the heavens. caves dig themselves out and become elaborate dungeons. the one who draws the card is considered the owner of this structure. however, 3d10 days later, the structure is attacked by some force. it can be a powerful wizard, a dragon, an ork warband, etc. if the structure is not defended, that force will destroy it. ", "The Jinx : You are rendered mute until someone says your name three times. You cannot speak or cast any verbal spells during this time. (Your party does not know this). ", "Greater Balance : The next time you roll a d20 and roll a critical success or fail, you receive an outcome beyond all expectations. The impossible happens despite all likelihood. Example: On a success, the Queen not only agrees with your theories and plans for the coming battle but trusts you over her advisors. On a fail, the Queen looks disgusted at your sad attempt of sharing information and banishes you to the dungeon for your ignorance just to get you out of the way. Should a critical success happen during combat, the number of damage dice is multiplied by 4 instead of 2, but if a critical fail happens, you or an ally are damaged by double the dice. This affect is a one time use. ", 
        "Null : The deck of many things vanishes. ", "Discord : For the next hour your character cannot speak common, elvish, gnomish, dwarven, etc.", "Yes : For the next two weeks your character cannot decline any offers for samples, work, quests, magic items, etc. and cannot say the word 'no' or similar. ", "Butterflies : A force of immense change you may use this card to change one small moment in the past. This will have rippling effects through time to the present day. Choose wisely. ", "The Damned : you are immediately teleported to one of the nine hells roll a D10 on the roll of a 10 you are trapped between two of the hells roll two more D10 and reroll all 10s. ", "Surface : Your body and soul are bound to a random humanoid within 60 feet, determined by the GM. Your appearance changes to match that of the chosen humanoid and neither of you may move more then 120 feet away from each other, and attempting to do so will result in running against an invisible wall. A Greater Restoration or Remove Curse spell cast at 5th level or higher on either one of you ends both effects. ", 
        "Talking Head : You become incapable of saying, writing, or otherwise expressing a truthfull message instead, any attempt to do so will result in you telling a lie instead, usually the opposite of what you meant. You are not affected by the Zone of Truth spell, as these lies are not deliberate. A Greater Restoration or Remove Curse spell cast at 5th level or higher on either one of you ends the effect. ", "Father : A Will-o'-Wisp (MM 301) with the memories, mental ability scores and alignment of a deceased relative appears within 10 feet and is bound to you as a familliar. The Will-o'-Wisp acts independently of you, but it always obeys your commands. In combat, it rolls its own initiative and acts on its own turn. It can't attack and loses the Shock action, but it can take other actions as normal. As an action, you can temporarily dismiss your familiar. It disappears into a pocket dimension where it awaits your summons. As an action while it is temporarily dismissed, you can cause it to reappear in any unoccupied space within 30 feet of you. If the Will-o'-Wisp dies, it is gone forever. ", 
        "Experience : Your mind speeds up, enhancing your senses and reflexes but leaving you more exposed to mental assault. You gain advantage on Dexterity saving throws and Wisdom (Perception) checks, but gain disadvantage on Wisdom saving throws and vulnerability to psychic damage. A Greater Restoration spell can end this effect. ", "Door : A magical book appears in your posession, containing the entirety of your memories written on it's pages, even ones you have forgotten through non-magical means. The book updates itself whenever you finish a long rest. Turning a page will always take you to the memory you'd like to see, and the book will always appear to be the same size, regardless of how many pages it has. You or a creature that has stolen the book can modify your memory by writing on the book, either writing fake memories or crossing or tearing out real ones. If the book is completely destroyed, you lose all your memories for 1 week, before getting them back, excluding fake memories from the book, and including memories that were removed from the book. ", "Diamond : You can cast the Creation, Greater Restoration, Mass Cure Wounds or Wall of Stone spells once per day. ", "Company : You gain the service of twelve Guards (MM 347) who appear in a space you choose within 30 feet of you. The guards are of the same race as you and serve you loyally until death, believing the fates have drawn them to you. ", "The Death Note : The first name that is written on this card immediately dies, no saving throw. ", "The Infant : Your character immediately turns into a newborn baby. ", 
        "The Mirror : An exact duplicate of the PC pulling this card is instantly created somewhere in the world. This copy has one purpose, to supplant the PC that pulled the card. The copy is indistinguishable from the PC in every visible way, and is physically in essence that PC. This copy differs only in that they believe that pulling the card sent them across the world and supplanted THEM with a copy located at the DOMT. This copy can accomplish supplanting the PC using any method (Violent, non violent, etc) that they wish as long as the final result is taking the place of the original PC. For rules purposes this created copy is the same level, class, and alignment as the PC that drew the card, and has access to all of the items that PC had on their person when drawing the Mirror. ", "The Fish : The character reeks of fish in a way that cannot be masked or removed. Additionally, any dead fish with the Beast creature type that the character touches, comes back to life as if had the True Resurrection spell cast on it. All Kuo-Toa are made aware of and believe in this effect on the character making it unremovable, even against the wish spell, except by the complete genocide of all Kuo-Toa. ", "Mystery : Something extraordinary has happened, but the players don't know what. The DM will roll randomly to determine if it is a good, bad, or neutral thing for the players and decide what it is in secret. Regardless of the roll the event will have a significant effect on the entire region (if not the whole world) and, upon encountering the event, the character who drew the card will be made aware drawing this card was the cause. ", 
        "Wayfinder : A gate to another dimension appears before the character. This gate connects to the GM's choice of Sigil, The Outlands, The Astral Plane, or another Material Plane. Regardless of the GM's choice, the other side of this gate is guarded by both an Androsphinx and a Gynosphinx that the players will need to bypass in order to freely pass through the gate. ", "Destruction : 8 bolts of chaotic energy fly out of the card extremely fast and attack all creatures within a 120ft radius sphere centered on where the card was drawn. The bolts acquire targets randomly each round and make a single attack at initiative 20. The attack is a ranged spell attack with +7 to the attack roll and deal 2d8 + 6d6 damage. Each orb deals a different type of one these 8 damage types: Acid, Cold, Fire, Force, Lightning, Poison, Psychic, Thunder. The bolts cannot be harmed or dispelled, do not attack anything that leaves the sphere, and disappear after 1 minute. ", "Creation : Immediately after drawing this card the player who drew it chooses one item that they can create as if they had cast the Fabrication spell and it appears before them. No material components for the crafted item are required and the casting time is instant. Players who don't know how to make anything can create a single item of raw materials such a log or cube of gold. They must still meet the dimension requirements of the Fabrication spell. ", "Animosity : From now on all creatures the character encounters with intelligence 6 or greater are initially hostile towards the character. This effect does not change their opinion of the character's companions and does not necessarily mean they will attack on sight. ", 
        "Friendship : From now on all creatures the character encounters with intelligence 6 or greater are initially friendly towards the character. This effect does not change their opinion of the character's companions and does not mean they will treat them as an equal. ", "The Dragon : The entire contents of the nearest dragon's horde is placed before you. Immediately after, the dragon is made aware of your name, appearance and current location. The dragon believes you culpable and cannot be convinced otherwise. ", "The Rose : the card puller gains a +3 to all charisma skill tests for 24 hours ", "The Flood : a soft gentle rain slowly grows over the next hour into a torrential downpour that follows the card puller, centered over then the entire hour. ", "The Fop : for one hour, you fail every skill test, attack roll, and saving throw. You cannot succeed at anything. ", "The Reward : for one hour, you have the exact funds to purchase anything you want. Just reach into your backpack and the gold coins are there. ", "The Flumph : After 1d4 hours a Flumph painlessly grows from your body and detaches itself. The Flumph is completely loyal to you and you gain the ability to communicate with it and other Flumphs telepathically. If a Flumph dies two more Flumphs will grow from your body in 1d4 hours; this process continues until you have accumulated twelve Flumps. When the twelveth Flumph dies you magically transform into a Flumphp yourself, keeping all your statistics and abilities. ", "Granite skin : +2 AC, disadvantage on Dex saving throws as your skin becomes a hardy but unwieldy mottled grey colour ", 
        "The Elder : There are no immediate effects to drawing the card until you attempt to sleep, the further you lull to sleep the more a sense of dread begins to build. This effect ends until you sleep or die from exhaustion. If you do sleep your consciousness is transported to a unknown realm outside the material plane, this realm appears to be a endless slab of carved mossy stone ground, floating above a dark abyssal ocean. The only sight within miles being the faint outline of a pillar. You can get closer to the pillar every night before waking up, each night you walk towards the pillar your character loses 5 max hp. It takes 10 nights to get to the pillar, which depicts a large tentacled being with its appendages wrapped around the planes of existence. If you choose not to touch the pillar or give up before reaching it, you awake with your hit points back and a forever lingering sense of dread. If you touch the pillar, the slab begins to sink and you are consumed by water before you glimpse at hundreds of orange beady eyes and tentacles, then you wake up,with your hp back and with the ability to see the world as it truly is, along with the knowledge that something terrible and older than the universe has been unleashed. ", "Open Chest : The image of an open box resting on the ground grants the person who drew the card a random magical item of random rarity determined by the DM using either the magic tables in the DMG or the DMs choice. ", "Insignificance : You are placed under a modified version of the Silence spell for 1d8 hours ", "The Card : This card features the image of a card on it. It negates all effects of the next card you draw. ", 
        "Beast : next full moon you will transform into a werewolf. ", "Self-Control: You gain resistance to psychic damage and are less impulsive overall. Barbarians temporary lose these effects when raging. ", "Gentleness: You take a permanent -2 to your AC. All non-hostile creatures with an intelligence greater than 6 now take a paternal affection towards you and are more likely to offer you assistance when possible. You gain advantage on persuasion checks against hostile creatures when the goal of your persuasion is to prevent conflict. If you witness someone close to you get killed you lose all effects of this card and gain +2 AC and +2 Strength for 1D4 hours afterwards. ", "Faithfulness: For the next 1D10 days, everything you do is motivated by your deity. If you do not follow a deity, one appears to you and anoints you as it’s new follower. The deity that appears is based on your alignment, race, and background, at the DM’s discretion. If you roll a 10, you gain the Channel Divinity feature at its lowest level, based on the domain associated with your deity. ", 
        "Kindness: You find yourself drawn towards charity. For the next 1D6 days, anytime you see someone or something in need and you can assist in any way, you feel compelled to do so. This includes things such as healing, giving away your money, or assisting in a task that doesn’t take longer than the duration rolled earlier. ", "Patience: If you’re the last person to enter a room, speak in a conversation, or take your turn in combat, you gain advantage on your next skill check relevant to that scenario. If you are the first, you have disadvantage. ", "Peace: You gain the Calm Emotions spell and can cast it for free once per long rest. ", "Joy: You find yourself overcome with obnoxious optimism. No matter what happens you always feel like it’s going to turn out okay. You become immune to being frightened but gain disadvantage on insight checks. This can be dismissed by the wish spell or by being knocked unconscious by a hostile creature. ", "Love: You fall in love with the next non-hostile humanoid stranger you meet. You have disadvantage on any malicious skill checks against this person. This can be dismissed by the Wish spell or an act of true love by someone else towards you. ",
        "The Diminutive Tree : A random player character of the party is suddenly and unceremoniously turned into a bonsai tree. Only vocal communication is available while in the form of the bonsai. The bonsai speaks only Sylvan. The bonsai is otherwise an inanimate object. The PC retains their HP and is able to cast spells of vocal components or freecast. To revert from the bonsai, the tree must either be planted and grown for three days with plenty of water, or with a wish/miracle/etc. Otherwise the PC will remain a bonsai tree, incapable of thirst, hunger, aging, or sleep. ", "The Changeling : You immediately exchange powers and abilities with the nearest person or creature with an equivalent power level (as determined by level / challenge rating. ", "The Mind Reader : you gain the psychic abilities of an Illithid but also gain the face sucking tentacles. ", "The Ghost : You immediately become semi-transparent, along with all clothing and equipment that you don (items lose this state if contact is lost. You are unable to change your opacity beyond this; you cannot turn invisible, or be made more visible (except by means of a wish spell). ", "Platinum : All platinum you possess (wherever it is) is tripled, but teleported to the lair of a powerful monster or dragon. The name of the monster appears on the card before disappearing. ", "Gold : You double all Gold coin you possess on this plane (so not in a bag of holding) ", "Silver : You become vulnerable to silver weapons. When you touch silver at the end of your turn, you gain a level of exhaustion ", "Bronze : You can always choose to be third in the Initiative Order in combat ", 
        "The Tolling Bell : Shows a tolling bell with the words of John Donne 'Therefore, send not to know/For whom the bell tolls,/It tolls for thee.' Throw 1d12. The one who holds the card will die at dawn in as much days. Each day they will here a bell ringing the number of days left. You can pass the card but only unbeknownst to the other person, you can't sell it. When the time is other, instead of waking up, the person will see a gigantic black bell with an eye in its center. It will toll one last time, and the soul of the person will be consumed by the bell. No resurection possible. A tatoo of a black bell will appear on the head of the dead. If it is a PC, the card will disappear. If the person is not the PC who drawed the card, the card will appear in their inventory at the very moment the bell had tolled. Throw 1d12. For whom will she toll now? ", "The Prophet : When this card is pulled, a projection of that players Deity forms in front of them, telling your player that they have been chosen as that deities prophet (DM role plays the Deity projection). The twist is that there is no actual affect that is granted to the player, but the DM should NEVER reveal this to the player. If the player has no religion or doesn't worship any deities, instead the card shouts at the player 'You are not worthy, heretic!' in a deep booming voice, and then disappears in their hand and goes back into the deck randomly. ", "The changeling : your character dies and the spell reincarnation is cast on your character. ", "Envy : Rather than sharing in their victory, your PC becomes saddened at the successes of those closest to them. Every time a party member besides the players rolls a natural 20 on a skill check, you have disadvantage on your next skill check. ",
    ]

    document.getElementById("Card").innerHTML = rollArray(deckOfAllTheThings)
};
function artGenerator() {
    document.getElementById("Art").innerHTML = ""
    let pottery = [
        "vase", "decanter", "pot", "jar", "jug", "plate", "platter", "tankard", "bowl", "oil-lamp", "teapot", "ewer", "tray",
        "Dish", "Cup", "Mug", "Saucer", "Pitcher", "Casserole", "Urn","Chalice", "Stein", "Crock", "Tureen", "Ramekin", "Gravy Boat", 
        "Basin", "Goblet", "Kiln", "Cauldron", "Flagon",  "Censer",  "Serving Dish"
        ]
    let jewelry = [
        "arm-band", "ring", "necklace", "choker", "crown", "scepter", "bracelet", "pair of earrings", "anklet", "chalice", "locket", "broach", 
        "music box", "jewelry box", "pocketwatch", "container", "whistle", "mirror"," horn",
        `faberge ${searchArray(['figurine','doll','skull', 'egg','box','vessel'])}`, "tiara", "bangle", "pendant", "belly chain", 
        "toe ring", "cufflinks", "signet ring", "hairpin", "nose ring", "torc", "lapel pin", "hair comb", "cameo", "circlet", "medallion", 
        "waist chain", "prayer chain", "clasp", "diadem", "belly ring", "bookmarker", "chatelaine", "ear cuff", "fob watch", "snuff box",
        "garter belt", "hatpin", "ceremonial dagger", "body chain", "opera glasses", "walking stick", "cane"
        ]
    let gems = [ 
        "azurite", "banded agate", "blue quartz", "cats eye agate", "hematite", "lapis lazuli", "malachite", "moss agate", "obsidian", 
        "rhodochrosite", "turquoise", "tiger eye","bloodstone", "carnelian", "chalcedony", "chrysoprase", "citrine", "jasper", "moonstone", 
        "quartz", "sardonyx", "zircon", "onyx", "star rose quartz","alexandrite", "aquamarine", "black pearl", "blue spinel", "peridot", 
        "topaz","black opal", "blue sapphire", "emerald", "fire opal", "opal", "star ruby", "star sapphire", "yellow sapphire","black sapphire", "diamond", "jacinth", "ruby" 
        ]
    let size = [
        "large", "small", "tiny", "life-size", "huge", "gargantuan", "miniature", "medium", "oversized", "petite", "colossal", "mammoth", "modest", 
        "compact", "towering", "grandiose", "immense", "pocket-sized", "room-filling", "dominant", "dainty"
        ]
    let many = [
        "a small group of", "a large group of", "a group of","a small army of", "a few", "a large force composed of","a multitude of", 
        "a swarm of", "a collection of", "a flock of", "a gathering of", "a handful of", "An assembly of", "a horde of", "a myriad of", 
        "a band of", "a host of", "a throng of", "a cluster of", "a pack of", "a troop of", "a legion of", "an array of", "a battalion of", 
        "an ensemble of", "a platoon of", "a squadron of", "a mass of", "a congregation of", "a posse of", "a sea of", "a team of", "an abundance of", 
        "a pile of", "a crowd of", "a colony of", "an expanse of"
        ]
    let monster = [
        [//sentient
        'aarakocra', 'aboleth', 'angel', 'azer', 'beholder', 'bugbear', 'bullywug', 'cambion', 'centaur', 'cyclops',  'death knight', 'demilich', 'demon', 'devil', 'doppleganger', 'dracolich', 'shadow dragon', 'dragon', 'dragon turtle', 'drider', 'dryad', 'duergar', 'empyrean', 'ettercap', 'ettin', 'faerie dragon', 'flameskull', 'flumph', 'genie', 'ghost', 'giant',  'gith', 'gnoll', 'goblin', 'golem', 'gorgon', 'grell', 'griffon', 'grimlock', 'hag', 'half dragon', 'harpy',  'helmed horror', 'hobgoblin', 'homunculus', 'intellect devourer', 'invisible stalker', 'jakalwere', 'kenku', 'kobold', 'kraken', 'kuo-toa', 'lamia', 'lich', 'lizardfolk', 'lycanthrope', 'magmin', 'manticore', 'medusa', 'mephits', 'merfolk', 'merrow', 'mimic', 'mind flayer', 'minotaur', 'modron',  'myconid', 'naga', 'nightmare', 'nothic', 'ogre', 'oni', 'otyugh', 'pegasus', 'peryton', 'pixie', 'psuedodragon', 'rakshasa', 'revenant', 'sahuagin', 'satyr', 'slaadi', 'specter', 'sphinx', 'sprite', 'succubus', 'incubus', 'thri-kreen', 'treant', 'troll', 'umber hulk', 'unicorn', 'vampire', 'wight', `will-o'-wisp`, 'wraith',  'xorn', 'yeti', 'yuan-ti', 'yugoloth', 
        ],
        [//non-sentient
        'animated object', 'animated weapon', 'ankheg', 'banshee', 'basilisk', 'behir', 'blight', 'carrion crawler', 'chimera', 'chuul', 'cloaker', 'cockatrice', 'couatl', 'crawling claw', 'darkmantle','dinosaur', 'displacer beast', 'elemental', 'fungi', 'hippogriph', 'rust monster', 'ape', 'awakened tree', 'awakened shrub', 'hydra', 'fomorian', 'galeb duhr', 'gargoyle', 'axe beak', 'baboon', 'badger', 'bat', 'black bear', 'blink dog', 'grick', 'blood hawk', 'boar', 'brown bear', 'water weird', 'camel', 'cat', 'constrictor snake', 'crab', 'hook horror', 'gibbering mouther', 'crocodile', 'death dog', 'deer', 'dire wolf', 'draft horse', 'mummie','eagle', 'elephant', 'elk', 'owlbear', 'flying snake', 'frog', 'giant ape', 'giant badger', 'roper', 'skeleton', 'shadow', 'scarecrow', 'roc', 'salamander', 'remorhazes', 'stirge', 'terrasque', 'giant bat', 'troglodyte', 'giant boar', 'giant centipede', 'giant constrictor snake', 'giant crab', 'giant crocodile', 'giant eagle', 'shambling mound', 'shield guardian', 'giant elk', 'giant fire beetle', 'giant frog', 'purple worm', 'giant goat', 'zombie', 'giant hyena', 'wyvern', 'giant lizard', 'giant octopus', 'giant owl', 'giant poisonous snake', 'giant rat', 'giant scorpion', 'giant sea horse', 'giant shark', 'giant spider', 'quaggoth', 'giant toad', 'giant vulture', 'giant wasp', 'giant weasel', 'giant wolf spider', 'goat', 'hawk', 'hunter shark', 'hyena', 'jackal', 'killer whale', 'lion', 'lizard', 'mammoth', 'mastiff', 'mule', 'octopus', 'owl', 'panther', 'phase spider', 'poisonous snake', 'polar bear', 'pony','hell hound',
        ]
        ]
    let eventRandomizer = [
        'battle', 'deal', 'bargain', 'wedding',"treaty", "alliance", "duel", "peace talks", "trade agreement", 
        "summit", "ceasefire", "conquest", "expedition", "exploration", "merger", "collaboration", "diplomatic mission", 
        "cultural exchange", "religious conversion", "invasion", "colonization", "migration", "revolution", "scientific discovery", 
        "armistice", "secession", "debate", "uprising", "signing of a charter", "landmark legislation", "exposition", "intercultural celebration", "joint invention", "reconciliation"
        ]
    let tool = [
        'weapon', 'tool', 'treasure chest', 'sword', 'spade', "torch", "book", "scroll", "lantern" , "shield"
        ]
    let item = [
        'whistle', 'anchor', 'nail', 'scale', 'open book', 'bugle', 'keystone', 'hook', 'tree', 'flower', 'drum', 'buckle', 'chair', 'spoon', 'fork', 'axe', 
        'sword', 'shield', 'armor', 'bedroll', 'barrel', 'keg', 'crate', 'box', 'pot', 'vial', 'arrow', 'broom', 'shovel', 'pillow', 'candle', 'lantern', 
        'mug', 'cup', 'tankard', 'bottle', 'plate', 'plow', 'pot', 'pan', 'lamp', 'rug', 'hammer', 'goblet', 'chest', 'tankard of alcohol', 'feather', 'oar', 
        'cask', 'harp', 'lute', 'necklace', 'bracelet', 'comb', 'crown', 'ring', 'oil-lamp', 'potion', 'gem', 'scroll', 'wand', 'horseshoe', 'pike', 'bow', 'pair of slippers', 
        'trident', 'brooch', 'amulet', 'pipe', 'figurine', 'deck', 'circlet', 'fan', 'boot', 'quiver', 'helm', 'gloves', 'belt', 'cape', 'dagger', 'shackles', 'horn', 
        'staff', 'book', 'wings', 'crystal ball', 'carpet', 'cask', 'flask', 'map', 'artifact', 'trap', 'spear', 'halberd', 'key', 'stone', 'talisman', 'scimitar', 
        'bracer', 'bowl', 'chime', 'elixer', 'hat', 'clothes', 'headband', 'haversack', 'mirror', 'mace', 'rope', 'trinket', 'statue', 'hankercheif', 'locket', 'bone', 'skull', 'sickle'
        ]
    let location = [
        "underfoot", "next to it", "in its mouth", "on its back",
        "held captive by smaller creatures that serve it",
        "surrounded by a protective barrier or force it conjures"
        ]
    let ageDescriptor = ["younger", "older", "adolescent", "mature", "childlike", "ancient", "middle-aged", "youthful", "elderly", "infantile", "senior", "juvenile", "venerable", "baby-faced", "grizzled", "time-worn", "nascent", "seasoned", "veteran", "fresh-faced"]
    let adultGender = ["man", "woman"]
    let anyAgeGender = ["man", "woman", "boy", "girl"]
    let youngGender = ["boy", "girl"]
    let age = ['child',"preteen", 'adolescent', "young adult", "middle-aged", "mature adult", "senior", "elder"  ]
    let ruler = ['king','queen', 'warlord',"emperor", "empress", "monarch", "pharaoh", "sultan", "shah", "kaiser", "czar", "tsar", "caliph", "duke", "duchess", "prince", "princess", "regent", "lord", "lady", "chieftain", "chief", "patriarch" , "matriarch", "sovereign", "governor", "despot", "tyrant", "tribal leader", "noble", "baron", "baroness", "magnate", "sheikh", "vizier"]
    let historicalEvent = [
        "a creation myth", 
        "a constellation", 
        "an ascension story", 
        `a historical ${searchArray(eventRandomizer)}`, 
        `a coronation of a(n) ${searchArray([`${variableEvent(age)}${findRace()} ${searchArray(ruler)}`,
        `${variableEvent(age)}${searchArray(ruler)}`, 
        `intelligent ${searchArray(monster)}`])}`, 
        "an ancient disaster", "an ancient prophecy",
        "the alignment of the stars", 
        `the rise of a great ${findRace()} hero`, 
        `the fall of a great ${findRace()} hero`, 
        `the rise of a great ${findRace()} villain`, 
        `the fall of a great ${findRace()} villain`, 
        "the defeat of a powerful nation", 
        "the creation of a powerful artifact", 
        "the destruction of a powerful artifact", 
        "the fall of an angel", 
        "the rise of a demon", 
        "the affair of a god",
        "entrance to another plane", 
        "a mortal besting a God", 
        "a hero's quest", 
        `a historical ${searchArray(eventRandomizer)} between ${findRace()}s and ${searchArray(monster[0])}s`, 
        `a historical ${searchArray(eventRandomizer)} between ${findRace()}s and ${findRace()}s`, 
        `a historical ${searchArray(eventRandomizer)} between ${searchArray(monster[0])}s and ${searchArray(monster[0])}s`
    ]

    let time = [
        'beautiful but wrong',
        "somehow up to date", 
        "changing-in-real-time", 
        "slightly outdated",
        "meticulously detailed",
        "rough sketch",
        "impressionistic",
        "historically accurate for its time",
        "artistically embellished",
        "modernized rendition",
        "generally reliable",
        "needs recalibration",
        "abstract representation",
        "lacking crucial details",
        "with noticeable omissions",
        "compiled from various sources",
        "faithful to the original",
        "topographically precise",
        "with artistic liberties",
        "dated but valuable",
        "showing visible wear and corrections",
        "cross-referenced for accuracy",
        "showing only specific features",
        "reliably comprehensive",
        "with speculative territories",
        "hand-drawn and approximate",
        "fading but legible",
        "stylized for aesthetic appeal"
    ]

    let drink = [
        "tankard of mead", "cup of ale", "glass of wine", "goblet of blood","flask of elixir", "horn of grog", "chalice of ambrosia", "bottle of enchanted brew", 
        "vial of moonlight", "jar of faerie nectar", "phial of liquid mana", "mug of root beer", "potion of invincibility", "urn of ancient tea", 
        "carafe of crystalline water", "tumbler of sapphire gin", "glass of midnight absinthe", "jug of molten gold", "steaming cauldron of witch's broth", 
        "glass flute of sparkling fairy champagne", "beaker of alchemical concoction", "bowl of druidic herbal infusion", "shot of dragon's fire", 
        "mug of dwarven stout", "goblet filled with mermaid tears", "glass of starlight liqueur", "cup of ethereal mist", "horn filled with centaur's cider", "chalice of dark void"
    ]
    let scene = [
        'swamp', 'mire', 'bridge', 'gate', 'road', 'paradise', 'fort', 'house', 'hut', 'keep', 'garden', 'room', 'sanctum', 'asylum', 'hideaway', 'refuge', 
        'shelter', 'shack', 'den', 'clearing', 'dungeon', 'castle', 'cottage', 'dungeon', 'field', 'camp', 'lean-to', 'mountain', 'cave', 'town', 'city', 'lake', 
        'pond', 'lair', 'chamber', 'hovel', ]
    let weapons = [
        "sword", "dagger", "axe", "mace", "staff", "wand", "quarterstaff", "broadsword", "skull", "book", "spear", "halberd", "flail", "morningstar", "warhammer", "scimitar", "katana", 
        "longbow", "falchion", "gladius", "whip", "rapier", "pike", "sabre", "war scythe"
    ]
    let bodyparts = ["eyes", "teeth", "external markings", "claws", "musculature definition", "osseous growths or bone extrusions", "crests or ridges", "underbelly texture or patterns"]
    let audience = [
        "royals", "monsters", "commoners", "villagers", "dragons", "tavern patrons", "heroes", `${findRace()}s`, `${searchArray(monster)}s`,
        "merchants", "travelers", "wanderers", "knights", "warriors", "priests", "clerics", "mystics", "seers", "sailors", "pirates", "minstrels", 
        "bards", "nymphs", "forest spirits", "dwarves", "miners", "elves", "elven lords", "faeries", "sprites", "witches", "wizards", "ghouls", 
        "spirits", "beast tamers", "hunters", "children", "scholars", "sages", "thieves", "rogues", "merfolk", "sea creatures", "mountaineers", 
        "highlanders", "nomads", "desert wanderers", "oracles", "fortune tellers", "goblins", "orcs", "centaurs", "satyrs", "angels", "demons", 
        "noble courtiers", "diplomats", "adventurers", "farmers", "shepherds", "soldiers", "guards", "wild animals", "enchanted beasts"
    ]
    let instruments = [
        "a harpsichord", "a piano", "a pipe organ", "bells", "chimes", "drums", "a gong", "a fiddle", "a harp", "a lute", "a mandolin", "a flute", "pan pipes", "a shawm", "a trumpet",
    "a lyre", "a dulcimer", "a zither", "a bagpipe", "a hurdy-gurdy", "a viola da gamba", "a recorder", "a gemshorn", "a crumhorn", "a tambourine", "a rebec", "a psaltery", "a cittern", "a theorbo", "a sackbut"
]
    let color = [
        "pearlescent",
        "moonlit silver",
        "sunflare orange",
        "starshine blue",
        "faerie green",
        "phantom violet",
        "mermaid teal",
        "unicorn pink",
        "eldritch black",
        "dragon scale bronze",
        "enchantment lavender",
        "abyssal blue",
        "wizard robe maroon",
        "mystic rose",
        "sorcerer's sapphire",
        "goblin green",
        "phoenix feather crimson",
        "wyvern wing white",
        "enigma ebony",
        "twilight taupe",
        "celestial cerulean",
        "frostbite blue",
        "inferno red",
        "ethereal emerald",
        "mystical mauve",
        "shadowshade gray",
        "potion pink",
        "arcane amber",
        "bewitched burgundy",
        "chimera chartreuse",
        "dream dust peach",
        "fey frost",
        "haunted heliotrope",
        "illusionary indigo",
        "jewel of the jinn ruby",
        "knight's armor silver",
        "lunar glow",
        "midnight's allure"
    ]
    let projectile = ["dart", "javelin", "arrow", "wood shard", "glass shard", "metal shrapnel", "spear", "crossbow bolt", "slingshot pellet", "boomerang", "throwing knife", "rock", "stone", "bolas", "net", "sling stone", "tomahawk", "fireball", "ice shard", "lightning bolt", "blowgun needle", "caltrop", "flaming arrow", "poisoned dart", "magic missile", "smoke bomb", "holy water vial"]
    let celebration = [ "a bonfire", "a feast table", "an encampment", "a pile of bodies", "a pole in the center of town", "a pile of gold and gems", "a large ceremonial altar", "a grand throne or chair", "a magical fountain", "a towering statue or idol", "a decorated tree or plant", "a sacrificial pit", "a colossal tent or pavilion", "a stage for performers", "an intricate sand or flower mandala", "a chained mythical creature or beast", "a series of flag poles with banners", "an astronomical observatory", "a sacred relic or artifact on display", "a grand ship or vessel", "a floating platform or island", "a gleaming crystal or prism", "a woven tapestry telling a story", "a collection of rare and magical items", "a mural or fresco", "a fireworks launch site", "a book or scroll of prophecies", "a sacred stone or monument"]
    let hair = ["long flowing", "short", "no", "braided", "wild and untamed", "sleek and straight", "curly and voluminous", "tightly coiled", "bald with tattoos", "mohawk", "topknot", "ponytail", "side-shaved", "rugged dreadlocks", "slicked back", "crown of braids", "windswept waves", "bun with ornamental pins", "twisted locs", "spiky", "feathered", "wispy", "long and silver", "thick mane", "short with a side part", "bedhead", "bald with a shining crown", "intricately styled", "wavy with highlights", "tight curls with a headband"]
    let mount = ["dinosaur", "griffon", "pegasus", "dragon", "displacer beast", "mammoth", "lion", "tiger", "warhorse", "horse", "moose", "phoenix", "dire wolf", "giant eagle", "unicorn", "wyvern", "rhinoceros", "giant spider", "elephant", "manticore", "giant bat", "giant seahorse", "hippogriff", "giant snail", "giant turtle", "chimera", "giant stag", "floating disk", "giant owl", "mechanical steed", "nightmare", "ghostly apparition", "abyssal charger"]
    let organization = ['theives guild', 'city', 'temple', "oracle's", "king's", "thieves guild", "city", "temple", "oracle's", "king's", "knight's order", "mage's academy", "alchemist's society", "hunter's lodge", "sailor's league", "merchant's union", "bard's college", "farmer's cooperative", "assassin's syndicate", "explorer's club", "healer's association", "blacksmith's forge", "druid's circle", "warrior's clan", "librarian's consortium", "monk's monastery", "priest's clergy", "adventurer's guild", "noble family", "courier's network", "guard's battalion", "craftsman's guild", "scholar's institution", "herald's office", "paladin's order", "ambassador's envoy", "brewer's tavern", "beastmaster's ring", "ranger's patrol", "jester's troupe"]
    let facialExpression = ["awed", "angry", "disgusted", "surprised", "grinning", "stern", "fearful", "sad", "appalled", "smirking", "smiling", "beaming", "grimacing", "winking", "scowling", "terrified", "hardened", "stone-faced", "frowning",     "contemplative", "pensive", "amused", "suspicious", "intrigued", "ecstatic", "shocked", "exasperated", "embarrassed", "daydreaming", "glaring", "confused", "hopeful", "bored", "anxious", "overwhelmed", "nonchalant", "melancholic", "horrified", "jubilant", "indifferent"]
    let thesaurus = ['depicting','representing','showing','displaying','presenting','exhibiting','portraying',  "illustrating", "revealing", "expressing", "demonstrating", "manifesting"]

    let status = [
        [ /*Stained Glass*/ "dusty", "dirty", "vandalized", "scratched", "broken", "faded", "discolored", "unfinished", "incomplete", "cracked", "pristine", "vibrant", "well-repaired", "poorly-repaired"],
        [ /*Mural*/ "dusty", "dirty", "vandalized", "scratched", "broken", "cracked", "stained", "faded", "eroded", "unfinished", "incomplete", "pristine", "moss/ivy-covered", "well-repaired", "poorly-repaired"],
        [ /*Pottery*/ "dusty", "dirty", "vandalized", "scratched", "broken", "cracked", "stained", "faded", "shattered", "unfinished", "pristine", "well-repaired", "poorly-repaired"],
        [ /*Figurine/ stauette/ carving*/ "dusty", "dirty", "vandalized", "scratched", "broken", "cracked", "stained", "broken (and missing some pieces)", "eroded", "shattered", "unfinished", "pristine", "moss/ivy-covered", "well-repaired", "poorly-repaired", "sliced in half"],
        [ /*Painting*/ "dusty", "dirty", "torn", "stained", "cut", "water-stained", "vandalised", "faded", "unfinished", "vibrant", "pristine", ],
        [ /*Relief*/ "dusty", "dirty", "vandalized", "scratched", "cracked", "unfinished", "incomplete", "pristine", "moss/ivy-covered", "well-repaired", "poorly-repaired"],
        [ /*Tapestry*/ "dusty", "dirty", "torn", "thread-bare", "worn", "water-stained", "shredded", "stained", "cut", "vandalised", "faded", "unfinished", "vibrant", "pristine", ],
        [ /*Fine Jewelry*/ "fine", "dusty", "dirty", "broken", "bent", "unfinished", "incomplete", "pristine", "vibrant", "well-repaired", "poorly-repaired"],
        [ /*Fine clothes*/ 'fine', 'thread-bare','moth-eaten', 'mildewed', 'singed', 'pristine','shredded','bloodstained','faded'],
        [ /*Fine Armaments */ "dented and bent",'dusty','dirty','tarnished','pristine','broken',"in the claws of a statue", "trapped in crystalline amber",`veiled in thick cobwebs`,"camouflaged as a mundane item"],
    ]
    function weaponType() {
        let x = rollDice(1000)
        if (x < 4) {
            return "club"
        } else if (x < 39) {
            return "dagger"
        } else if (x < 43) {
            return "greatclub"
        } else if (x < 67) {
            return "handaxe"
        } else if (x < 75) {
            return "javelin"
        } else if (x < 79) {
            return "light hammer"
        } else if (x < 149) {
            return "mace"
        } else if (x < 172) {
            return "quarterstaff"
        } else if (x < 176) {
            return "sicle"
        } else if (x < 213) {
            return "spear"
        } else if (x < 230) {
            return `${searchArray(["tonfa","tiger claws","knuckle dusters","iron fan","katar","emeici","cestus","tekko","maduvu","pata","crecent moon knives","knife wheel"])} (fist weapon)`
        } else if (x < 271) {
            return "light crossbow"
        } else if (x < 287) {
            return "dart"
        } else if (x < 303) {
            return "shortbow"
        } else if (x < 319) {
            return "sling"
        } else if (x < 404) {
            return "battleaxe"
        } else if (x < 413) {
            return "flail"
        } else if (x < 420) {
            return "glaive"
        } else if (x < 498) {
            return "greataxe"
        } else if (x < 576) {
            return "greatsword"
        } else if (x < 581) {
            return "halberd"
        } else if (x < 586) {
            return "lance"
        } else if (x < 773) {
            return "longsword"
        } else if (x < 774) {
            return "maul"
        } else if (x < 778) {
            return "morningstar"
        } else if (x < 779) {
            return "pike"
        } else if (x < 809) {
            return "rapier"
        } else if (x < 848) {
            return "scimitar"
        } else if (x < 887) {
            return "shortsword"
        } else if (x < 891) {
            return "trident"
        } else if (x < 893) {
            return "war pick"
        } else if (x < 903) {
            return "warhammer"
        } else if (x < 905) {
            return "whip"
        } else if (x < 907) {
            return "blowgun"
        } else if (x < 914) {
            return "hand crossbow"
        } else if (x < 955) {
            return "heavy crossbow"
        } else if (x < 996) {
            return "longbow"
        } else if (x < 1000) {
            return "net"
        }
    }
    let armorTypes = [
        [ `splint armor`, `ring mail armor`, `full plate armor`, `chain mail armor`, `scale mail armor`, `hide armor`, `half plate armor`, `leather armor`, `studded leather armor`, ],
        [ `chain shirt`, `breastplate`, `helmet`, ],
    ]
    let material = [
        [ /*pottery*/ "pewter", "lead", "bronze", "gold", "iron", "silver", "platinum", "electrum", "copper", "nickel", "jade", "bone", "teeth-bone", "clay", "granite", "marble", "obsidian", "porcelain", "sandstone", "quartz", "cork", "petrified wood", "unidentifiable substance", "mohogany", "cherry wood", "oak wood", "apple wood", "teak wood", "pine wood", "birch wood", "shell", "sea glass", "glass", ],
        [ /*statues*/ "marble", "golden", "granite", "silver", "platinum", "copper", "bronze", "electrum", "obsidian", "clay", "bone"],
        [ /*Carvings*/ "bone", "mohogany", "cherry wood", "oak wood", "apple wood", "teak wood", "pine wood", "birch wood", ],
        [ /*Fine jewelry*/ "gold", "platinum", "electrum", "silver", "bronze","copper", "gold with platinum inlay", "gold and copper alloy", "gold and silver alloy", `${searchArray(gems)} jeweled gold`, `${searchArray(gems)} jeweled platinum`, `${searchArray(gems)} jeweled electrum`, `${searchArray(gems)} jeweled silver`, `${searchArray(gems)} jeweled copper`, `${searchArray(gems)} jeweled gold with platinum inlay`, `${searchArray(gems)} jeweled gold and copper alloy`, `${searchArray(gems)} jeweled gold and silver alloy`, `solid ${searchArray(gems)}`],
        [ /*Fine Clothes*/ "griffon feather weave", "chimera leather", "dragon scale mesh", "phoenix feather down", "nymph hair thread", `${searchArray(color)} brocade`, "moonbeam-infused linen", "sun ray-embroidered fabric", "starlit tulle", "basilisk hide", "unicorn mane weave", "elf-spun cotton", "fairy wing lace", "siren silk", "dwarf-forged chainmail", "titan-tanned leather", "celestial chiffon", "abyssal black denim", "shadow-woven satin", "mermaid scale sequins", "ether fabric", "enchanted ivy weave", "kraken skin leather", "gossamer of moonlight", "fabric of bottled starlight", "feywild silk", "roc feather cloth", "centaur hide suede", "banshee veil netting", "ethereal essence tulle", "minotaur horn mesh", "fabric woven from dreams", "cloth dipped in the River Styx", "satyr's beard wool", "clothes made of woven spells", "mystical lava-forged fabric", "giant squid ink dyed cloth", "dryad leaf linen", "vampire bat wing leather", "thread spun from prophecies", "changeling camouflage cloth", "phoenix ash infused fabric", "will-o'-the-wisp woven mesh", "sprite's shimmer scale sequins", "medusa hair thread", "troll skin rubberized fabric", "cloth blessed by ancient deities", "harpy's song-woven silk", "fabric of trapped tempests", "wendigo fur", "cloth soaked in eldritch energies"
    ],
        [ /*Fine Armaments*/ "platinum","gold","copper","silver","silver with mithril inlay","gold with platinum inlay", "platinum with adamantium inlay", "copper with silver inlay","silver with gold inlay"]
    ]
    function classReturn() {
        let classes = [
            [ 'bardic performance', 'cleric holy', `fighter's dueling`, 'paladin ceremonial', 'ranger ceremonial', 'rogue honorific', 'warlock ritual', ],
            [ 'barbarian tribal', 'druidic', 'monk ceremonial', ],
            [ `sorcerer ritual`, `wizard's ritual`, 'artificer', `summoner's`,'mystic' ],
        ]
        var chance = rollDice(100);
        if (chance > 70) {
            return searchArray(classes[2]);
        } else if (chance > 40) {
            return searchArray(classes[1]);
        } else {
            return searchArray(classes[0]);
        }
    }

    let culturalEvents =[
        'festivals','weddings','funerals','combat','singing','chanting','instrumentation','storytelling','gift-giving','feasting','dancing','body adornment','greetings','rite of passage','reenactments','competitions','races','gatherings'
    ]
    let culturalPurpose = [
        'family','religion','community','social order','justice','food','shelter','water','safety','ethics','morality','knowledge','language',
        'heritage','resilience','dignity','honor','work','technology','life','death','survival','nature','strength','harmony','balance','eternity','love'
    ]
    let reason = [
        'preservation','celebratation','bonding','education','expression','entertainment','inspiration','rememberance'
    ]
    let writtenArtifact = [
        "novel", "short story", "poem", "biography", "autobiography", "memoir", "drama", "journal", "diary", "letter", "speech", "how-to guide", "review", "critique", 
        "anecdote", "allegory", "fable", "myth", "legend", "chronicle", "epic", "haiku", "sonnet", "eulogy", "sermon", "prose", "lyric", "script", "commentary",'series of proverbs'
    ]
    let physicalArtifact = [
        "painting", "sculpture", "drawing", "print", "etching", "lithograph", "mosaic", "tapestry", "installation art", "performance art", "pottery", 
        "ceramics", "glass art", "stained glass", "collage", "bas-relief", "high relief", "metalwork", "jewelry", "fiber art", "textile art", "wood carving", "stone carving", 
        "assemblage", "kinetic sculpture", "found object art", "cast iron piece", "forged metal artwork", "wearable art", "diorama", "shadow box", "origami", "paper mâché", 
        "murals", "frescoes", "land art"
    ]



    function culture() {
        let x = rollDice(100)
        if (x>77){
            return `${searchArray([`a ${searchArray(writtenArtifact)} describing ${searchArray(culturalEvents)} based on ${searchArray(culturalPurpose)} - for the purpose of ${searchArray(reason)}`,
            `a ${searchArray(writtenArtifact)} describing ${searchArray(culturalEvents)} for the purpose of ${searchArray(reason)}`,
            `a ${searchArray(writtenArtifact)} describing ${searchArray(culturalEvents)} around the concept of ${searchArray(culturalPurpose)}`,
            `a ${searchArray(writtenArtifact)} on ${searchArray(culturalPurpose)} for ${searchArray(reason)}`])}`
        } else if (x >33) {
            return `${searchArray([`a ${searchArray(physicalArtifact)} depicting ${searchArray(culturalEvents)} reinforcing the culure's beliefs on ${searchArray(culturalPurpose)} - made for the purpose of ${searchArray(reason)}`,
            `a ${searchArray(physicalArtifact)} depicting a ${searchArray(culturalEvents)} around the concept of ${searchArray(culturalPurpose)}`,
            `a ${searchArray(physicalArtifact)} depicting a ${searchArray(culturalEvents)} for the purpose of ${searchArray(reason)}`,
            `a ${searchArray(physicalArtifact)} depicting a ${searchArray(culturalPurpose)}`])}`
        } else {
            return `${searchArray([`cultural symbols describing a ${searchArray(culturalEvents)} around the concept of ${searchArray(culturalPurpose)} for the purpose of ${searchArray(reason)}`,
            `cultural symbols describing a ${searchArray(culturalEvents)}for the purpose of ${searchArray(reason)}`,
            `cultural symbols describing a ${searchArray(culturalEvents)} around the concept of ${searchArray(culturalPurpose)}`,
            `cultural symbols on the concept of ${searchArray(culturalPurpose)}`])}`
        }
    }

    let cermonialDesign = [
        "Radiantly gilded", "Elegantly baroque", "Intricately carved", "Exquisitely enameled", "Lavishly adorned", "An unapologetically extravagant", "A painstakingly detailed", "A mythology-inspired", "Regally embossed", "Masterfully sculpted", "Sophisticatedly filigreed", "Luxuriously garnished", "Exotically bejeweled", "Artistically wrought", 
        "Symbolically etched", "Meticulously inlaid", "Timelessly elegant", "Spectacularly bedecked", "Richly burnished", "An heirloom-quality","A jewel encrusted", "An extraordnarily ornate", "An impossibly opulent"
    ]

    let artForm = [
        [//craft
            `${variableEvent(status,0)}stained glass window`,
            `${variableEvent(status,1)}mural`,
            `${variableEvent(status,2)}${searchArray(material[0])} ${searchArray(pottery)}`,
            `${variableEvent(status,3)}${searchArray(material[2])} carving`,
            `${variableEvent(status,4)}painting`,
            `${variableEvent(status,5)}relief`,
            `${variableEvent(status,6)}tapestry`,
        ],
        [//jewelry
            `${variableEvent(status,7)}${searchArray(material[3])} ${searchArray(jewelry)}`,            
        ],
        [//statues
            `${variableEvent(status,3)}${searchArray(material[1])} ${searchArray(["statuette","figurine",])}`,
        ],
        [//weapons
            `${searchArray(cermonialDesign)} ${variableEvent(status,9)}${searchArray(material[5])} ${searchArray([`${weaponType()}`,`${searchArray([`set of ${searchArray(armorTypes[0])}`, `${searchArray(armorTypes[1])}`])}`, `shield and ${weaponType()} display set`])}, 
            ${searchArray([`seemingly of ${findRace()} make with ${searchArray([`${culture()}`,`extraordinarily intricate designwork and filigree`])}`])}.`
        ],
        [//clothes
            `A ${variableEvent(status,8)} set of ${searchArray(material[4])} ${searchArray(
                [`${findRace()} ${searchArray(culturalEvents)} vestments`,
                'cultic vestments',
                `vestments from a long forgotten ${searchArray(['kingdom','culture'])}`,
                `${classReturn()} vestments`,
                'royal drapery',
                'enchanter’s robe',
                'diviner’s attire',
                'time-honored ceremonial cloak',
                'dimensional weaver’s outfit',
                'Archmage robes',
                `garments blessed by ${searchArray(['moon', 'sun', 'stars', 'ocean'])} deities`,
                'sorceress evening gown',
                'warrior prince tunic',
                'grand oracle’s ensemble',
                'sacred guardian attire',
                'holy emissary’s raiments',
                'cloak of ancient prophecies',
                'time-traveler’s tailored suit',
                'mystical seer’s garb',
                'necromancer’s robe adorned with lost souls',
                'grandmaster alchemist’s attire'
            ])}.`
        ],
        [//manuscripts
            `illuminated manuscript`
        ],
        [//toys

        ]
    ]


    let adjective = [
        [
            'airborne', 'slouching', 'giddy', 'brazen', 'hobbled', 'wrinkled', 'broken', 'happy', 'sunken', 'headless', 'burning', 'toothy', 'mighty', 'frisky', 'staggering', 'gutted', 'glorious', 'crooked', 'joyful', 'wise', 'sweet', 'surly', 'reverent', 'clumsy', 'clever', 'prone', 'restrained', 'unconscious', 'invisible', 'petrified', 'poisoned', 'charmed', 'frightened', 'grappled', 'acrobatic', 'dextrous', 'intelligent', 'strong', 'athletic', 'deceitful', 'charismatic', 'insightful', 'intimidating', 'observant', 'perceptive', 'persuasive', 'stealthy', 'dirty', 'dangerous', 'deadly', 'hidden', 'alert', 'brave', 'wicked', 'tricky', 'mysterious', 'kind', 'handsome', 'frantic', 'foolish', 'adorable', 'cruel', 'elegant', 'friendly', 'gnashing', 'winking', 'smiling', 'waving', 'ugly', 'busy', 'creepy', 'grotesque', 'poor', 'puzzled', 'obnoxious', 'fierce', 'fancy', 'magnificent', 'enchanting', 'eager', 'determined', 'horrible', 'wide-eyed', 'victorious', 'uptight', 'unusual', 'troubled', 'thankful', 'terrible', 'tame', 'repulsive', 'sparkling', 'exuberant', 'exotic', 'graceful', 'majestic', 'rambunctious', 'sassy', 'spirited', 'spooky', 'vigilant', 'ambitious', 'bewildered', 'captivating', 'comical', 'daring', 'elusive', 'ferocious', 'gleaming', 'insane', 'jovial', 'luminous', 'melancholy', 'nefarious', 'ornate', 'precarious', 'reckless', 'seductive', 'tremendous', 'unruly', 'vulnerable', 
            'whimsical', 'zealous', 'precious', 'mirthful', 'adventurous', 'cautious', 'enigmatic', 'fearless', 'graceful', 'hilarious', 'impish', 'loathsome', 'mischievous', 'nervous', 'playful', 'reclusive', 'serene', 'tactful', 'voracious', 'wily', 'zealous', 'exquisite', 'gloomy', 'haunting', 'inquisitive', 'loving', 'misunderstood', 'naughty', 'peaceful', 'ruthless', 'stoic', 'tantalizing', 'vexing', 'wary', 'yawning', 'zany', 'aching', 'bewitched', 'carefree', 'delightful', 'enchanted', 'fascinating', 'gleeful', 'hasty', 'imposing', 'jubilant', 'lucky', 'mystifying', 'noble', 'playful', 'radiant', 'silly', 'thoughtful', 'whimsical', 'yearning', 'zealous', 'eccentric', 'giddy', 'humble', 'intrepid', 'lively', 'magnanimous', 'nifty', 'overt', 'precocious', 'quirky', 'radiant', 'selfless', 'turbulent', 'unwavering', 'vivid', 'wondrous', 'zesty', 'ablaze', 'bizarre', 'capricious', 'dazzling', 'ecstatic', 'flamboyant', 'gorgeous', 'hallowed', 'illustrious', 'jocular', 'kooky', 'luminous', 'misleading', 'nurturing', 'ornery', 'pensive', 'quirky', 'ravishing', 'scintillating', 'tenacious', 'unyielding', 'vibrant', 'whimsical', 'yearning', 'zealous', 'ambivalent', 'bemused', 'capable', 'delicious', 'erratic', 'fickle', 'glorious', 'hallowed', 'indomitable', 'judicious', 'keen', 'lively', 'momentous', 'notorious', 'outlandish', 'passionate', 'quizzical', 'rhapsodic', 'serendipitous', 'tumultuous', 'unabashed', 'versatile', 'wistful', 'zealous'
        ],
        []
    ]
    let action = [
        [// bad to good
            "fighting a(n)", 
            "being killed by a(n)", 
            "stalking a(n)", 
            "conquered by a(n)", 
            "standing over a(n)",
            "capturing a(n)",
            "taunting a(n)",
            "engaging in a deadly duel with a(n)",
            "ambushing a(n)",
            "menacingly approaching a(n)",
            "casting a curse on a(n)",
            "using dark shadows to engulfing a(n)",
            "conjuring dark magic against a(n)",
            "engaging in a fierce battle with a(n)",
            "casting a spell on a(n)",
            "summoning a terrifying creature to attack a(n)",
            "gloating over a(n)",
            "sending minions to attack a(n)",
            "engaging in a psychological mind game with a(n)",
            "using a dark and treacherous labyrinth to trap a(n)",
            "using sinister strength to overpower a(n)",
            "whispering malevolent promises to a(n)",
            "using dark sorcery to control a(n)",
            "inflicting a deadly wound upon a(n)",
            "using a web of deceit to ensnare a(n)",
            "corrupting the mind of a(n)",
            "cursing the fate of a(n)",
            "composing a dreadful choice for a(n)",
            "unleashing a torrent of destructive power upon a(n)",
            "using a sinister aura to envelope a(n)",
            "shattering the spirit of a(n)",
            "bestowing a cursed artifact upon a(n)",
            "draining the life force of a(n)",
            "revealing its monstrous form to a(n)",
            "manipulating the emotions of a(n)",
            "haunting the dreams of a(n)",
            "engaging in a deadly dance of blades with a(n)",
            "sending nightmares to torment a(n)",
            " using dark chains to bind a(n)",
            "conducting a malevolent experiment on a(n)",
            "baiting a treacherous trap to lure a(n)",
            "instilling fear in the heart of a(n)",
            "corrupting the soul of a(n)",
            "casting a dark enchantment upon a(n)",
            "using hypnotic malevolence to mesmerize a(n)",
            "sharing wicked thoughts to infest the mind of a(n)",
            "bargaining for the soul of a(n)",
            "causing the despair of a(n)",
            "sending cursed illusions to deceive a(n)",
            "using a web of lies and treachery to ensnare a(n)",
            "engaging in a deadly ritual to curse a(n)",
            "whispering sinister promises of power to a(n)",
            "leading a horde of evil creatures against a(n)",
            "brandishing a cursed weapon at a(n)",
            "preparing to steal life force of a(n)'s",
            "inflicting a curse of eternal suffering upon a(n)",
            "dominating the will of a(n)",
            "using fate with a dark prophecy to manipulating a(n)'s",
            "using haunting visions to cause the madness of a(n)",
            "creating a torrent of malevolent flames to engulf a(n)",
            "inciting the darkest fears and insecurities of a(n)'s",
            "explaing a deadly and doomed quest to a(n)",
            "whispering forbidden knowledge into the ears of a(n)",
            "creating a never-ending nightmare for a(n)",
            "wielding dark and forbidden magic against a(n)",
            "creating a deadly trial of malevolence for a(n)",
            "using illusions to twist the perceptions of a(n)",
            "casting a spell of cursed paralysis upon a(n)",
            "Enslaving a(n)",
            "enthralling a(n)",
            "using dark and forbidden knowledge to curse a(n)",
            "stealing the light and hope from the heart of a(n)",
            "engaging in a deadly game of cat and mouse with a(n)",
            "using a malevolent spell of enchantment to bewitch a(n)",
            "unleashing a torrent of destructive energy upon a(n)",
            "imposing a doomed and sinister destiny upon a(n)",
            "seductively enticing a(n)",
            "concealing itself in the shadows to stalk a(n)",
            "engaging in a malevolent pact with a(n)",
            "banishing a(n)",
            "shattering the reolve of a(n)",
            "introducing a(n) to its own inner darkness",
            "enthroned as a malevolent ruler over a(n)",
            "inflicting a curse of eternal suffering upon a(n)",
            "siphoning the life force of a(n)",
        ],
        [// general actions
            "looking towards the sky", "preparing to attack", "ready to fight", "sitting on a rock", "bracing for impact", "singing", "dancing in ceremonial dress"
        ],
        [//evil actions
            "sitting in its lair", `clutching a(n) ${searchArray(item)} tightly`, "stalking around a city", "in a house", "standing on top of a large building", "on top of a building"
        ]
    ]
    let verb = [
        [/*Evil*/
            `ready to ${searchArray(['ambush','capture','sell','swindle'])} a group of people`,
            `${searchArray(['raiding', 'razing', 'destroying', 'caturing', 'extorting', 'robbing'])} a ${searchArray(['village', 'caravan', 'castle'])}`, 
            `being ${(['killed', 'captured', 'defeated'])} by a ${searchArray(['hero', 'group of townsfolk', 'small militia', 'group of heroes'])}`, 
            `${searchArray(['attacking', 'killing'])} a ${searchArray(['group of heroes', 'a child'])}`, 
            `${(['fleeing from', 'being attacked by', 'defeated by'])} ${searchArray(['something large and ominous', 'a group of heroes','a group of townsfolk',  `a ${variableEvent(['ominous, evil-looking', 'bloodsoaked'])} child`])}`,
            "preparing to unleash dark and forbidden magic",
            "plotting the downfall of a noble kingdom",
            "conspiring with sinister allies",
            "whispering malevolent secrets to corrupt hearts",
            "engaging in dark rituals to gain forbidden power",
            "manipulating the innocent for nefarious purposes",
            "spreading fear and despair throughout the land",
            "twisting the minds of the weak-willed",
            "feeding on the suffering of others",
            "planning to unleash an ancient evil",
            "enslaving the souls of the innocent",
            "casting a malevolent curse on a rival",
            "hatching a diabolical scheme for world domination",
            "subjugating the weak to serve an evil agenda",
            "summoning demonic forces to wreak havoc",
            "devising a treacherous trap for a noble hero",
            "unleashing a plague of darkness upon the land",
            "ensnaring the hearts of the virtuous in wickedness",
            "spreading chaos and discord throughout the realm",
            "gathering an army of darkness to conquer all",
            "corrupting the hearts of the once-pure with evil temptations",
            "spreading malevolent rumors to sow discord",
            "enthralling the minds of the powerful to serve malevolence",
            "conjuring shadows to envelop the world in darkness",
            "usurping the throne of a benevolent ruler",
            "subverting the laws of nature with dark sorcery",
            "poisoning the minds of the innocent with lies",
            "enslaving the spirits of ancient beings to serve dark whims",
            "stealing the life force of the land to fuel sinister power",
            "cursing the once-prosperous kingdom with eternal night",
            "deceiving the righteous with cunning lies",
            "unleashing an army of undead to terrorize the living",
            "corrupting the sacred places with blasphemous rituals",
            "banishing benevolent spirits to bring forth malevolent ones",
            "sacrificing innocent souls to gain demonic favor",
            "shrouding the world in an eternal eclipse",
            "twisting the fate of the world with wicked machinations",
            "desecrating sacred relics to weaken the forces of good",
            "calling forth malevolent creatures from the abyss",
            "tearing open the fabric of reality to let in dark forces",
            "perverting the magic of nature to bring forth destruction",
            "unleashing a tide of darkness upon the unsuspecting world",
            "weaving a web of deceit to ensnare the virtuous",
            "opening a portal to unleash unspeakable horrors",
            "bringing forth ancient curses to torment the living",
            "warping the minds of the virtuous to turn them into pawns",
            "invoking forbidden names to gain ultimate power",
            "ensnaring the dreams of the innocent with nightmares",
            "whispering forbidden knowledge into the ears of the desperate",
            "calling forth storms of destruction to ravage the land",
            "blighting the once-verdant lands with dark energies",
            "sowing the seeds of distrust among former allies",
            "unleashing a plague of malevolent creatures to overrun the world",
            "binding the wills of the powerful to serve the wicked",
            "unleashing a tide of darkness that swallows all hope",
            "wielding a cursed weapon to bring about doom and despair",
            "erasing the memories of the innocent to create obedient servants",
            "conjuring illusions to lead the noble astray",
            "bringing forth a reign of terror and chaos",
            "feeding on the fear and anguish of the innocent",
            "corrupting the hearts of the noble with insidious whispers",
            "shrouding the world in eternal darkness to extinguish hope",
            "ensnaring the minds of the righteous to turn them to darkness",
            "summoning ancient and malevolent spirits to do its bidding"
        ],
        [/*Singular*/ 
        "nursing a friend back to health", 
        "holding a baby in their hands", 
        `defending against an onslaught of ${searchArray(monster)}s`, 
        "playing with a pet", 
        "laughing with friends", 
        "playing a tabletop game with friends", 
        `holding (a(n)) ${searchArray(item)} in one hand, and a ${searchArray(item)} in the other`, 
        `weeping with a lifeless ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} ${searchArray([ 'in their arms', 'at their feet', 'across the battlefield', 'hanging from the gallows', 'lying peacefully in a bed of flowers', 'cradled in the branches of a sacred tree', 'resting beneath a serene waterfall', 'entombed in a grand mausoleum', 'floating peacefully in the depths of a tranquil lake', 'adorned with flowers on a funeral pyre', 'resting among the ancient ruins of a fallen city', 'surrounded by mourners paying their respects', 'protected in the embrace of a guardian spirit', 'laid to rest in a sacred burial ground', 'enclosed within a mystical crystal tomb', 'entwined with ivy on a weathered stone monument', 'enshrined in a magnificent marble sarcophagus', 'buried in the heart of an enchanted forest', 'surrounded by flickering candles in a dark crypt', 'watched over by celestial beings in the afterlife', 'floating peacefully in the night sky as a guiding star', 'resting on a bed of fallen leaves in a peaceful glade', 'remembered through a towering statue in their honor', 'reunited with their ancestors in the realm of spirits', 'surrounded by ancient symbols of protection and guidance', 'becoming part of the eternal tapestry of the cosmos', 'embodying the essence of the natural world as a spirit guardian', 'residing in a tranquil and ethereal dreamscape', 'immortalized in a majestic painting, forever remembered', 'dwelling in a realm of eternal twilight and peaceful slumber', 'watched over by a benevolent and celestial being', 'resting on a bed of glowing crystals in a mystical cavern', 'surrounded by angels, guiding them to the afterlife', 'enclosed within a magnificent and elaborate tomb', 'becoming one with the vibrant and ever-changing universe', 'surrounded by a chorus of spirits, singing them into the beyond', 'protected by ancient and powerful magical wards', 'resting peacefully in the embrace of a guardian deity', 'residing in a realm of eternal sunshine and happiness', 'watched over by the gentle and guiding light of the moon', 'enclosed within the heart of a majestic and ancient tree', 'surrounded by their cherished belongings and mementos', 'embodying the spirit of the earth, forever connected to nature', 'dwelling in the realm of dreams, a place of infinite possibilities', 
        'watched over by a wise and benevolent spirit of the afterlife', 'resting on a bed of stars, their spirit soaring through the cosmos', 'surrounded by the warmth and comfort of ancestral spirits', 'protected by the embrace of a mythical and divine creature', 'residing in a realm of eternal peace and tranquility', 'enclosed within a sacred and mystical burial chamber', 'watched over by guardian spirits, their journey guided and protected', 'embodying the essence of the ocean, forever flowing with the tides', 'dwelling in a realm of eternal spring, where life is everlasting', 'resting among the shimmering and ethereal lights of the aurora', 'surrounded by the whispers of ancient and wise spirits', 'watched over by the spirits of their ancestors, guiding them home', 'residing in a realm of eternal night, where dreams come to life', 'enclosed within a hidden and sacred burial ground', 'protected by the watchful eyes of celestial beings', 'resting in the heart of a sacred and ancient temple', 'surrounded by the gentle embrace of a benevolent and loving spirit', 'watched over by the spirits of nature, forever connected to the earth', 'embodying the essence of the stars, forever shining in the sky', 'dwelling in a realm of eternal autumn, where colors never fade', 'residing among the echoes of the past and the dreams of the future', 'enclosed within a serene and peaceful memorial garden', 'protected by the wings of a majestic and mythical creature', 'resting on a bed of moonlit clouds, their spirit soaring free', 'surrounded by the soft and comforting glow of ethereal light', 'watched over by the eternal and guiding flame of a sacred fire', 'embodying the spirit of the mountains, forever standing tall', 'dwelling in a realm of eternal winter, where snow never melts', 'residing among the whispers of the wind, forever wandering', 'enclosed within the heart of a mystical and ancient forest', 'protected by the watchful and guiding eye of a guardian deity', 'resting on a bed of ancient and sacred runes, forever remembered', 'surrounded by the gentle and soothing melodies of celestial musicians', 
        'watched over by the radiant and comforting light of the sun', 'embodying the essence of the flame, forever burning bright', 'dwelling in a realm of eternal summer, where flowers always bloom', 'residing among the twinkling and shimmering lights of the night sky', 'enclosed within a hidden and sacred burial mound', 'protected by the swirling and mysterious currents of the sea', 'resting on a bed of glowing embers, forever aflame with life', 'surrounded by the whispers of ancient and powerful magic', 'watched over by the guiding and protective spirits of the forest', 'embodying the spirit of the wind, forever moving with grace', 'dwelling in a realm of eternal rain, where waters never recede', 'residing among the radiant and colorful lights of the sunset', 'enclosed within the heart of a majestic and mythical mountain', 'protected by the shimmering and magical aura of a sacred crystal', 'resting on a bed of fallen petals, forever connected to nature', 'surrounded by the comforting and gentle embrace of the moonlight', 'watched over by the eternal and wise eyes of the stars', 'embodying the essence of the earth, forever grounded and strong', 'dwelling in a realm of eternal dusk, where shadows never fade', 'residing among the soft and soothing murmurs of the river', 'enclosed within a hidden and mystical burial cave', 'protected by the ancient and powerful energies of the ley lines', 'resting on a bed of ethereal mist, forever wandering and exploring', 'surrounded by the glowing and vibrant colors of the rainbow', 'watched over by the gentle and nurturing light of the morning sun', 'embodying the spirit of the thunderstorm, forever powerful and awe-inspiring', 'dwelling in a realm of eternal thunder, where storms never cease', 'residing among the radiant and twinkling lights of the fireflies', 'enclosed within the heart of a grand and ancient temple', 'protected by the comforting and guiding presence of a guardian spirit', 'resting on a bed of soft and fragrant petals, forever at peace', 'surrounded by the ethereal and enchanting melodies of celestial birds', 'watched over by the eternal and watchful eyes of a celestial deity', 'embodying the essence of the ocean, forever flowing and changing', 'dwelling in a realm of eternal fog, where mysteries never reveal themselves', ])}`, 
        `working on a ship`, 
        'leaning against a cannon', 
        'loading a cannon', 
        'boarding a flying airship', 
        'seated on an ornate throne', 
        'seated on an ornate throne, an arrow is headed towards their head',
        `walking underneath an archway surrounded by woodland creatures`,
        "dancing in long flowing clothes",
        "with an anguished expression on their face and a broken crown on their head",
        "holding a book, deep in thought while reading",
        "painting a masterpiece on a canvas",
        "meditating under a serene waterfall",
        "practicing archery with impressive precision",
        "performing a mesmerizing magic trick",
        "standing in front of a gathering, delivering an impassioned speech",
        "confronting a powerful enemy with unwavering courage",
        "standing tall amidst a storm, facing the fury of the elements",
        "embarking on an epic adventure, map in hand",
        "gazing at the stars, pondering the mysteries of the universe",
        "performing a graceful dance with ribbons",
        "leading a group of brave explorers into the unknown",
        "standing at the edge of a precipice, surveying the vast landscape",
        "teaching a group of eager students a valuable skill",
        "seeking solace in the quiet embrace of nature",
        "weaving intricate patterns on a loom",
        "delving into the depths of an ancient library",
        "tending to a beautiful garden with loving care",
        "embracing a loved one after a long journey",
        "engraving intricate designs on a piece of armor",
        "practicing swordplay with graceful precision",
        "giving a warm hug to someone in need of comfort",
        "writing a heartfelt letter to a distant friend",
        "performing a stunning acrobatic feat",
        "carving a delicate sculpture out of stone",
        "crafting a powerful potion with skilled hands",
        "contemplating life's mysteries under a starry night sky",
        "releasing a caged bird back into the wild",
        "composing a hauntingly beautiful melody on a musical instrument",
        "wandering through a magical forest, surrounded by mystical creatures",
        "sharing a moment of laughter with a group of merry companions",
        "casting a spell with an ancient and weathered grimoire",
        "discovering a hidden treasure in a long-forgotten cave",
        "engaging in a friendly sparring match with a fellow warrior",
        "sitting by a crackling fireplace, lost in thought",
        "savoring a delicious feast with a grateful heart",
        "contemplating a breathtaking sunset from a mountaintop",
        "setting out on a daring quest with unwavering determination",
        "standing as a beacon of hope in a world consumed by darkness",
        "engaging in a thrilling chase through the bustling streets of a city",
        "resting under the shade of a towering ancient tree",
        "engrossed in deciphering an ancient and mysterious script",
        "bravely facing a mythical beast with fierce resolve",
        "offering a helping hand to someone in need",
        "standing as a stalwart guardian, protecting the weak and defenseless",
        "participating in a joyous celebration with a jubilant crowd",
        "flying on the back of a majestic dragon, soaring through the skies",
        "standing in awe before a majestic waterfall, feeling the power of nature",
        "traversing a treacherous mountain pass, determined to reach the summit",
        "forging a powerful weapon with skilled craftsmanship",
        "witnessing the first rays of dawn break over the horizon with reverence",
        "embracing the beauty of a blooming flower in a tranquil meadow",
        "engaging in a philosophical debate, seeking knowledge and wisdom",
        "taming a wild creature with patience and understanding",
        "listening attentively to the woes of a troubled friend, offering solace",
        "giving a heartfelt gift to someone they hold dear",
        "standing tall as a bastion of virtue in a world tainted by corruption",
        "celebrating a victorious moment with jubilant cheers",
        "observing a mesmerizing celestial event in the night sky",
        "imbuing an object with powerful enchantments using ancient magic",
        "standing firm in the face of adversity, refusing to yield to darkness",
        "building a magnificent structure, a testament to their skill and determination",
        "reuniting with a long-lost loved one, tears of joy streaming down their face",
        "engaging in a solemn ceremony, honoring fallen heroes and lost friends",
        "spreading kindness and compassion to all they encounter",
        "carrying a flickering torch through the depths of a dark and ominous cave",
        "navigating treacherous waters with expertise and courage",
        "standing at the helm of a grand ship, guiding its course with authority",
        "speaking words of wisdom to a rapt audience, inspiring hope and courage",
        "trekking through a vast desert, braving the scorching sun with determination",
        "standing at the edge of a cliff, contemplating the vastness of the world below",
        "offering a helping hand to a wounded creature, nursing it back to health",
        "embarking on a dangerous mission to rescue a kidnapped loved one",
        "gazing at the full moon with a sense of wonder and mystery",
        "performing a healing ritual, mending the wounds of the injured and weary",
        "standing as a beacon of light in a world engulfed by darkness",
        "weaving a tapestry of intricate patterns and colors",
        "exploring an ancient ruin, unraveling its secrets with curiosity",
        "singing a hauntingly beautiful melody that echoes through the night",
        "painting a breathtaking landscape, capturing the essence of nature's beauty",
        "taming a fearsome beast with gentle words and a calm demeanor",
        "sitting by a tranquil lake, reflecting on life's journey",
        "unearthing an ancient artifact, shrouded in mystery and power",
        "standing amidst a field of flowers, feeling the gentle caress of the breeze",      
        ],
        [/*Group*/
        "nursing a friend back to health together",
        `defending against an onslaught of ${searchArray(monster)}s as a team`,
        "playing with their pets joyfully",
        "laughing together in sheer delight",
        "engaging in a friendly tabletop game",
        `- one holding (a(n)) ${searchArray(item)}, the other holding (a(n)) ${searchArray(item)}, looking at each other with curiosity`,
        `weeping together over a lifeless ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} ${searchArray([  'in their arms', 'at their feet', 'across the battlefield', 'hanging from the gallows', 'lying peacefully in a bed of flowers', 'cradled in the branches of a sacred tree', 'resting beneath a serene waterfall', 'entombed in a grand mausoleum', 'floating peacefully in the depths of a tranquil lake', 'adorned with flowers on a funeral pyre', 'resting among the ancient ruins of a fallen city', 'surrounded by mourners paying their respects', 'protected in the embrace of a guardian spirit', 'laid to rest in a sacred burial ground', 'enclosed within a mystical crystal tomb', 'entwined with ivy on a weathered stone monument', 'enshrined in a magnificent marble sarcophagus', 'buried in the heart of an enchanted forest', 'surrounded by flickering candles in a dark crypt', 'watched over by celestial beings in the afterlife', 'floating peacefully in the night sky as a guiding star', 'resting on a bed of fallen leaves in a peaceful glade', 'remembered through a towering statue in their honor', 'reunited with their ancestors in the realm of spirits', 'surrounded by ancient symbols of protection and guidance', 'becoming part of the eternal tapestry of the cosmos', 'embodying the essence of the natural world as a spirit guardian', 'residing in a tranquil and ethereal dreamscape',
         'immortalized in a majestic painting, forever remembered', 'dwelling in a realm of eternal twilight and peaceful slumber', 'watched over by a benevolent and celestial being', 'resting on a bed of glowing crystals in a mystical cavern', 'surrounded by angels, guiding them to the afterlife', 'enclosed within a magnificent and elaborate tomb', 'becoming one with the vibrant and ever-changing universe', 'surrounded by a chorus of spirits, singing them into the beyond', 'protected by ancient and powerful magical wards', 'resting peacefully in the embrace of a guardian deity', 'residing in a realm of eternal sunshine and happiness', 'watched over by the gentle and guiding light of the moon', 'enclosed within the heart of a majestic and ancient tree', 'surrounded by their cherished belongings and mementos', 'embodying the spirit of the earth, forever connected to nature', 'dwelling in the realm of dreams, a place of infinite possibilities', 'watched over by a wise and benevolent spirit of the afterlife', 'resting on a bed of stars, their spirit soaring through the cosmos', 'surrounded by the warmth and comfort of ancestral spirits', 'protected by the embrace of a mythical and divine creature', 'residing in a realm of eternal peace and tranquility', 'enclosed within a sacred and mystical burial chamber', 'watched over by guardian spirits, their journey guided and protected', 'embodying the essence of the ocean, forever flowing with the tides', 'dwelling in a realm of eternal spring, where life is everlasting', 'resting among the shimmering and ethereal lights of the aurora', 'surrounded by the whispers of ancient and wise spirits', 'watched over by the spirits of their ancestors, guiding them home', 'residing in a realm of eternal night, where dreams come to life', 'enclosed within a hidden and sacred burial ground', 'protected by the watchful eyes of celestial beings', 'resting in the heart of a sacred and ancient temple', 'surrounded by the gentle embrace of a benevolent and loving spirit', 
        'watched over by the spirits of nature, forever connected to the earth', 'embodying the essence of the stars, forever shining in the sky', 'dwelling in a realm of eternal autumn, where colors never fade', 'residing among the echoes of the past and the dreams of the future', 'enclosed within a serene and peaceful memorial garden', 'protected by the wings of a majestic and mythical creature', 'resting on a bed of moonlit clouds, their spirit soaring free', 'surrounded by the soft and comforting glow of ethereal light', 'watched over by the eternal and guiding flame of a sacred fire', 'embodying the spirit of the mountains, forever standing tall', 'dwelling in a realm of eternal winter, where snow never melts', 'residing among the whispers of the wind, forever wandering', 'enclosed within the heart of a mystical and ancient forest', 'protected by the watchful and guiding eye of a guardian deity', 'resting on a bed of ancient and sacred runes, forever remembered', 'surrounded by the gentle and soothing melodies of celestial musicians', 'watched over by the radiant and comforting light of the sun', 'embodying the essence of the flame, forever burning bright', 'dwelling in a realm of eternal summer, where flowers always bloom', 'residing among the twinkling and shimmering lights of the night sky', 'enclosed within a hidden and sacred burial mound', 'protected by the swirling and mysterious currents of the sea', 'resting on a bed of glowing embers, forever aflame with life', 'surrounded by the whispers of ancient and powerful magic', 'watched over by the guiding and protective spirits of the forest', 'embodying the spirit of the wind, forever moving with grace', 'dwelling in a realm of eternal rain, where waters never recede', 'residing among the radiant and colorful lights of the sunset', 'enclosed within the heart of a majestic and mythical mountain', 
        'protected by the shimmering and magical aura of a sacred crystal', 'resting on a bed of fallen petals, forever connected to nature', 'surrounded by the comforting and gentle embrace of the moonlight', 'watched over by the eternal and wise eyes of the stars', 'embodying the essence of the earth, forever grounded and strong', 'dwelling in a realm of eternal dusk, where shadows never fade', 'residing among the soft and soothing murmurs of the river', 'enclosed within a hidden and mystical burial cave', 'protected by the ancient and powerful energies of the ley lines', 'resting on a bed of ethereal mist, forever wandering and exploring', 'surrounded by the glowing and vibrant colors of the rainbow', 'watched over by the gentle and nurturing light of the morning sun', 'embodying the spirit of the thunderstorm, forever powerful and awe-inspiring', 'dwelling in a realm of eternal thunder, where storms never cease', 'residing among the radiant and twinkling lights of the fireflies', 'enclosed within the heart of a grand and ancient temple', 'protected by the comforting and guiding presence of a guardian spirit', 'resting on a bed of soft and fragrant petals, forever at peace', 'surrounded by the ethereal and enchanting melodies of celestial birds', 'watched over by the eternal and watchful eyes of a celestial deity', 'embodying the essence of the ocean, forever flowing and changing', 'dwelling in a realm of eternal fog, where mysteries never reveal themselves'])}`,
        `working together on a ship`,
        'leaning against cannons with camaraderie',
        'loading cannons with synchronized precision',
        'boarding a flying airship as a united force',
        'seated together in a grand throneroom',
        'seated in a throneroom, arrows are headed towards their heads, but they stand united and resolute',
        `walking underneath an archway surrounded by woodland creatures, sharing the journey`,
        "dancing gracefully in long flowing clothes as one harmonious group",
        "standing shoulder to shoulder, ready to face whatever comes their way",
        "performing an intricate and synchronized dance routine",
        "collaborating on a beautiful and intricate mural",
        "sharing a meal together, enjoying each other's company",
        "engaging in a lively debate, expressing diverse opinions",
        "playing musical instruments in perfect harmony",
        "supporting each other during difficult times, offering strength and comfort",
        "training together to hone their combat skills",
        "holding a banner aloft, symbolizing their unity and purpose",
        "exploring an ancient and mysterious labyrinth as a team",
        "embarking on a perilous journey, each with a role to play",
        "performing a breathtaking acrobatic display",
        "standing united against a common foe, undeterred and brave",
        "celebrating a joyous occasion with shared laughter and happiness",
        "building a magnificent structure together, their efforts combined",
        "listening to a captivating storyteller, engrossed in the tale",
        "conducting a scientific experiment, combining their knowledge",
        "forming a human chain to cross a treacherous chasm",
        "enacting a traditional ceremony, upholding their cultural heritage",
        "painting a mural that depicts their shared history and triumphs",
        "standing in a circle, raising their arms in a show of unity and power",
        "rallying together, motivated by a common cause",
        "sailing a ship through stormy seas, guided by teamwork",
        "sharing wisdom and knowledge, each contributing their expertise",
        "celebrating a victory, lifting their arms in triumphant cheers",
        "working diligently in a bustling marketplace, their trades complementing each other",
        "collaborating on a complex magical ritual, pooling their magical energies",
        "standing in formation, prepared to face a formidable enemy",
        "posing together for a group portrait, capturing their bond",
        "practicing a sacred dance, connecting with their cultural roots",
        "gathering around a campfire, sharing stories and warmth",
        "planting saplings in unison, contributing to the growth of a forest",
        "rescuing a trapped companion, pulling together with strength",
        "crafting intricate armor and weapons for each other's protection",
        "performing a mesmerizing symphony, each musician playing their part",
        "building a bridge to connect two sides, working hand in hand",
        "supporting each other in a challenging climb, reaching new heights",
        "joining hands in a circle, creating a bond of trust and solidarity",
        "dancing around a sacred bonfire, celebrating a spiritual ritual",
        "shouting battle cries, charging into battle as a united force",
        "assisting each other in overcoming obstacles, united in purpose",
        "orchestrating a complex strategy, using their diverse skills",
        "defending their homeland, forming a line of defense",
        "crafting intricate artwork together, blending their artistic styles",
        "standing united under a banner of peace and diplomacy",
        "performing a theatrical play, expressing emotions together",
        "harvesting crops in sync, reaping the rewards of their labor",
        "standing vigil over a fallen comrade, honoring their memory",
        "working together to rescue people in need, showing compassion",
        "cheering together in a grand stadium, united in their support",
        "aligning their staffs in a magical ritual, channeling their power",
        "flying on the backs of majestic creatures, soaring through the skies as one",
        "forging alliances, shaking hands in a gesture of trust",
        "chanting ancient hymns, invoking blessings and protection",
        "standing together in a council, making important decisions as a group",
        "reuniting with long-lost companions, embracing each other warmly",
        "conducting a scientific experiment, combining their knowledge and expertise",
        "practicing a martial arts form, moving as one harmonious unit",
        "decorating a festive parade float, bringing their creative ideas to life",
        "standing together with torches, illuminating the darkness",
        "working in harmony to repair a damaged structure, rebuilding together",
        "joining voices in a powerful chorus, creating harmonious music",
        "participating in a lively and colorful festival, celebrating life",
        "exploring a magical wonderland, filled with awe and excitement",
        "standing as guardians of nature, protecting the forest with reverence",
        "building a monument to honor their shared achievements",
        "standing in a circle, reciting an oath of loyalty and friendship",
        "embarking on a quest to uncover ancient secrets, united by curiosity",
        "forming a human ladder, rescuing someone trapped in a high place",
        "training together in a sacred martial art, mastering their skills",
        "gathering around a mystical portal, venturing into the unknown together",
        "celebrating a joyous wedding, raising their glasses in a toast",
        "rowing a boat in sync, navigating treacherous waters as a team",
        "standing united on a battlefield, facing a formidable enemy with resolve",
        "collaborating on a grand invention, combining their knowledge",
        "working together in a bustling kitchen, preparing a delicious feast",
        "engaging in a group meditation, finding inner peace as one",
        "holding hands in a circle, channeling their magic to create a powerful spell",
        "forming a human shield, protecting the vulnerable from harm",
        "marching together in a parade, celebrating their shared identity",
        "building a sanctuary for all, laying each brick with care and purpose",
        "planting a community garden, sowing the seeds of togetherness",
        "standing in a circle, sharing stories and wisdom around a bonfire",
        "forging a pact of loyalty, sealing it with a solemn oath",
        "working together to tame a wild creature, showing patience and cooperation",
        "gazing at the stars in wonder, contemplating the vastness of the cosmos",
        "standing united under a common banner, representing their shared values",
        "helping each other across a treacherous rope bridge, ensuring safety for all",
        "confronting a powerful adversary, coordinating their attacks strategically",
        "standing tall and proud, their unity and strength evident to all who see",
        "traversing a dangerous desert together, sharing water and encouragement",
        "forming a circle of support, offering comfort to someone in distress",
        "standing in a line, ready to face an impending threat with bravery",
        "crafting intricate jewelry together, combining their artistic talents",
        "performing a synchronized swimming routine, a breathtaking display of grace",
        "supporting each other during a difficult climb, reaching the summit together",
        "painting a majestic mural, capturing the beauty and diversity of nature",
        "gathering around a campfire, their faces illuminated by the warm glow",
        "standing together under a magical waterfall, cleansing their spirits",
        "trading stories and laughter around a banquet table, united in camaraderie",
        "forming a human chain to rescue someone from a raging river",
        "building a bridge between cultures, fostering understanding and acceptance",
        "chanting in unison, invoking the powers of the elements",
        "practicing archery as one, their arrows hitting the targets in perfect harmony",
        "standing united in a circle, their different races and backgrounds united by friendship",
        "tending to a communal garden, nurturing the earth and each other",
        "performing a traditional dance, their movements coordinated and graceful",
        "working together to extinguish a dangerous fire, showing bravery and cooperation",
        "carrying a heavy load together, their strength multiplied in unity",
        "standing as guardians of a sacred grove, protecting its ancient secrets",
        "forming a circle of trust, each one pledging loyalty to the others",
        "rebuilding a fallen city together, their determination unwavering",
        "performing a ceremonial ritual, their actions synchronized and purposeful",
        "standing on the precipice of a cliff, preparing to jump into the unknown together",
        "training together in a martial arts dojo, honing their combat skills",
        "joining hands to create a powerful barrier, protecting their community",
        "participating in a grand festival, celebrating their cultural heritage",
        "forming a human pyramid, reaching new heights of teamwork",
        "standing together in a garden, their hands dirty with soil and friendship",
        "holding hands in a circle, their magic intertwining in a beautiful display",
        "supporting each other during a difficult climb, conquering the mountain together",
        "collaborating on a scientific experiment, their minds sharp and curious",
        "standing united as representatives of their diverse and vibrant community",
        "building a bridge between two kingdoms, forging a lasting alliance",
        "marching together in a protest, advocating for a shared cause",
        "standing in a line, their arrows raised and ready to defend their home",
        "creating a beautiful tapestry together, weaving their individual stories",
        "standing as guardians of the forest, protecting its inhabitants with reverence",
        "joining voices in a powerful chorus, their song echoing through the land",
        "gathering around a campfire, sharing stories and laughter",
        "standing together in a circle, raising their weapons in unity",
        "forming a circle of support, offering strength to someone in need",
        "working as a team to build a grand structure, their efforts harmonious",
        "collaborating on an intricate dance routine, their movements flowing as one",
        "forming a circle of friendship, their bond unbreakable",
        "crafting a powerful artifact together, combining their magical abilities",
      
        ],
    ]
    let subject = [
        [/*Singular*/
        'knight', 'refugee', 'acolyte', 'archmage', 'assassin', 'bandit', 'berserker', 'commoner', 'cultist', 'fanatic', 'gladiator', 'mage', 'priest', 'scout', 'spy', 'thug', 'veteran', 'dutchess', 'paladin', 'farmer', 'scholar', 'seadog', 'jester', 'noble', 'king', 'thief', 'sailor', 'farmer', 'soldier', 'beggar', 'bard', 'guard', 'merchant', 'smuggler', 'fool', 'druid', 'witch', 'traveler', 'fisherman', 'lady', 'harlot', 'bounty hunter', 'gardener', 'gambler', 'prince', 'princess', 'pirate', 'journeyman', 'chieftain', 'lord', 'archer', 'lumberjack', 'miner', 'hunter', 'villager', 'settler', 'butcher', 'oracle', 'pilgrim', 'courier', 'hero', 'necromancer', 'sorcerer', 'wizard', 'barbarian', 'ranger', 'fighter', 'monk', 'warlock', 'summoner', 'arcanist', 'blood hunter', 'cleric', 'rogue', 'artificer', 'outlander', 'exile', 'falconer', 'scribe', 'beastmaster', 'dancer', 'hermit', 'blacksmith', 'astronomer', 'explorer', 'alchemist', 'tavern owner', 'illusionist', 'baker', 'inquisitor', 'fortune teller', 'minstrel', 'gravedigger', 'fencer', 'philosopher', 'animal tamer', 'apothecary', 'court jester', 'seer', 'brawler', 'watchman', 'musician', 'volunteer', 'innkeeper', 'cartographer', 'executioner', 'shaman', 'sculptor', 'tax collector', 'acrobat', 'archaeologist', 'herbalist', 'weaver', 'beekeeper', 'librarian', 'trapper', 'gypsy', 'skald', 'messenger', 'almsman', 'governess', 'herald', 'peddler', 'storyteller', 'taxidermist', 'exorcist', 'juggler', 'sword swallower', 'fakir', 'prison guard', 'master thief', 'con artist', 'medicine woman', 'snake charmer', 'peasant', 'vagrant', 'glazier', 'magistrate', 'armorer'
        ],
        [/*Plural*/
        'knights', 'refugees', 'acolytes', 'archmages', 'assassins', 'bandits', 'berserkers', 'commoners', 'cultists', 'fanatics', 'gladiators', 'mages', 'priests', 'scouts', 'spies', 'thugs', 'veterans', 'dutchesses', 'paladins', 'farmers', 'scholars', 'seadogs', 'jesters', 'nobles', 'kings', 'thieves', 'sailors', 'farmers', 'soldiers', 'beggars', 'bards', 'guards', 'merchants', 'smugglers', 'fools', 'druids', 'witches', 'travelers', 'fishermen', 'ladies', 'harlots', 'bounty hunters', 'gardeners', 'gamblers', 'princes', 'princesses', 'pirates', 'journeymen', 'chieftains', 'lords', 'archers', 'lumberjacks', 'miners', 'hunters', 'villagers', 'settlers', 'butchers', 'oracles', 'pilgrims', 'couriers', 'heroes', 'necromancers', 'sorcerers', 'wizards', 'barbarians', 'rangers', 'fighters', 'monks', 'warlocks', 'summoners', 'arcanists', 'blood hunters', 'clerics', 'rogues', 'artificers', 'outlanders', 'exiles', 'falconers', 'scribes', 'beastmasters', 'dancers', 'hermits', 'blacksmiths', 'astronomers', 'explorers', 'alchemists', 'tavern owners', 'illusionists', 'bakers', 'inquisitors', 'fortune tellers', 'minstrels', 'gravediggers', 'fencers', 'philosophers', 'animal tamers', 'apothecaries', 'court jesters', 'seers', 'brawlers', 'watchmen', 'musicians', 'volunteers', 'innkeepers', 'cartographers', 'executioners', 'shamans', 'sculptors', 'tax collectors', 'acrobats', 'archaeologists', 'herbalists', 'weavers', 'beekeepers', 'librarians', 'trappers', 'gypsies', 'messengers', 'almsmen', 'governesses', 'heralds', 'peddlers', 'storytellers', 'taxidermists', 'exorcists', 'jugglers', 'sword swallowers', 'prison guards', 'master thieves', 'con artists', 'medicine women', 'snake charmers', 'peasants', 'vagrants', 'glaziers', 'magistrates', 'armorers'
         ],
        [/*Inanimate*/ 
        "ancient city", "abandoned castle", "enchanted forest", "ruined temple", "hidden cave", "majestic waterfall", "ancient library", "mysterious lighthouse", "deserted island", "eerie graveyard", "serene lake", "grand cathedral", "magical observatory", "mystic stone circle", "secret underground passage", "celestial observatory", "haunted mansion", "enigmatic underwater city", "tranquil garden", "lost city in the clouds", "otherworldly portal", "time-worn stone bridge", "ethereal moonlit beach", "towering mountain peak", "vibrant marketplace", "whimsical fairy ring", "steampunk factory", "dystopian cityscape", "futuristic space station", "cozy tavern by the fireplace", "gleaming crystal cavern", "surreal dreamscape", "rustic windmill", "ancient pyramids", "mystical starlit meadow", "enchanted ice castle", "mesmerizing nebula", "barren wasteland", "steaming volcano", "neon-lit cyber city", "blossoming cherry orchard", "floating sky islands", "spooky abandoned asylum", "subterranean crystal cave", "enigmatic stonehenge", "magical coral reef", "abandoned space station", "lush tropical rainforest", "frozen arctic tundra", "astral observatory", "underwater atlantis", "enchanted tapestry", "mystical portal", "forgotten crypt", "cosmic black hole", "fairy-tale castle", "ancient colosseum", "enchanted fountain", "lost shipwreck", "enchanted maze", "enchanted garden", "hidden grotto", "crystal oasis", "mystical cavern", "haunted forest", "lost caverns", "enchanted ruins", "celestial nebula", "enchanted glade", "mysterious cave", "ancient catacombs", "enchanted kingdom", "hidden waterfall", "enchanted forest glade", "enchanted star system", "mystical desert oasis", "enchanted lake", "cosmic observatory", "forgotten ruins", "enchanted ice caverns", "enchanted meadow", "mystical labyrinth", "forgotten spaceship", "enchanted city of light", "mystical time portal", "cosmic constellation", "mysterious stone circle", "enchanted crystal forest", "enchanted moonlit garden", "mystical underwater grotto", "forgotten civilization", "cosmic galaxy", "enchanted starlit lake", "enchanted ancient tree", "mystical floating island", "enchanted celestial palace", "hidden temple of wonders", "mystical realm of dreams"
        ]
    ]

    function findRace() {
        var races = {
            "Common": { 'human': undefined, },
            'Uncommon': { 'dwarf': undefined, 'high-elf': undefined, 'wood-elf': undefined, 'gnome': undefined, 'half-elf': undefined, 'halfling': undefined, },
            'Rare': { 'dragonborn': undefined, 'tiefling': undefined, 'genasi': undefined, 'aasimar': undefined, 'half-orc': undefined, 'tabaxi': undefined, 'drow': undefined, },
            "Very Rare": { 'kalashtar': undefined, 'shifter': undefined, 'warforged': undefined, 'simic hybrid': undefined, 'changeling': undefined, 'goliath': undefined, 'gith': undefined, 'yuan-ti': undefined, 'tortle': undefined, 'aarakocra': undefined, 'orc': undefined, },
            'Ultimate Rare': { 'bugbear': undefined, 'firbolg': undefined, 'goblin': undefined, 'hobgoblin': undefined, 'kenku': undefined, 'kobold': undefined, 'triton': undefined, 'lizardfolk': undefined, 'vedalken': undefined, 'verdan': undefined, 'locathah': undefined, 'grung': undefined, 'centaur': undefined, 'loxodon': undefined, 'minotaur': undefined, },
        };
        let chance = rollDice(100)
        if (chance > 98) {
            return searchArray(Object.keys(races["Ultimate Rare"]));
        } else if (chance > 95) {
            return searchArray(Object.keys(races["Very Rare"]));
        } else if (chance > 80) {
            return searchArray(Object.keys(races["Rare"]));
        } else if (chance > 50) {
            return searchArray(Object.keys(races["Uncommon"]));
        } else {
            return searchArray(Object.keys(races["Common"]));
        }
        //document.getElementById("Race").innerHTML = characterRace
    };

    function stages(){
        let story = [
            "heroic quest",
            "epic battle",
            "mythical journey",
            "tragic love story",
            "legendary adventure",
            "fantastical discovery",
            "mystical transformation",
            "ancient prophecy",
            "cosmic exploration",
            "time-traveling escapade",
            "cultural celebration",
            "supernatural encounter",
            "scientific expedition",
            "futuristic odyssey",
            "magical conflict",
            "reimagined fairy tale",
            "intergalactic war",
            "legendary artifact hunt",
            "fantasy realm exploration",
            "spiritual awakening",
            "dystopian struggle",
            "enchanting romance",
            "folklore retelling",
            "steampunk adventure",
            "cyberpunk revolution",
            "post-apocalyptic survival",
            "space colonization",
            "enchanted forest quest",
            "timeless battle of good vs. evil",
            "alternate reality quest",
            "cosmic beings' intervention",
            "cultural clash and harmony",
            "forgotten civilization's legacy",
            "mythical creature uprising",
            "adventurous pirate tale",
            "discovery of hidden powers",
            "magical academy initiation",
            "lost treasure expedition",
            "alien encounter",
            "artificial intelligence revolution",
            "journey through dreamscape",
            "exploration of parallel worlds",
            "ancient prophecy fulfillment",
            "virtual reality adventure",
            "sorcerer's apprentice training",
            "enchanted monarchy struggle",
            "futuristic rebellion",
            "struggle for survival in the wild",
            "interdimensional portal exploration",
            "time-loop conundrum",
            "enchanted kingdom restoration",
            "mysterious unsolved mysteries",
            "cosmic guardian's quest",
            "lost civilization's resurrection",
            "fantastical creatures' alliance",
            "spacefaring colonization mission",
            "enchanted object's curse",
            "cultural folklore unification",
            "spiritual guardian's awakening",
            "post-apocalyptic hope restoration",
            "magical melody's discovery",
            "reimagined historical events",
            "time traveler's paradox",
            "fantasy land's liberation",
            "supernatural beings' secret world",
            "ancient artifact's power",
            "cosmic journey beyond the stars",
            "virtual reality escape",
            "sorcerer's duel of destinies",
            "enchanted kingdom's rule",
            "futuristic utopia",
            "stranded on a mysterious island",
            "interstellar diplomacy",
            "timeless love rekindling",
            "enchanted forest's harmony",
            "fateful decision to be made",
            "cultural secrets revealed",
            "spiritual journey of enlightenment",
            "dystopian society's rebellion",
            "otherworldly romance",
            "folklore creatures' alliance",
            "steampunk inventions' competition",
            "cyberpunk hacker's mission",
            "post-apocalyptic refuge",
            "space explorer's discovery",
            "enchanted book's adventure",
            "time-bending escapade",
            "fantasy realm's fate",
            "cosmic entity's awakening",
            "virtual world's glitch",
            "sorcerer's ancient prophecy",
            "enchanted monarchy's curse",
            "futuristic cityscape",
            "struggle for survival in the wilderness",
            "interdimensional time travel",
            "time traveler's journey",
            "fantasy land's restoration",
            "supernatural beings' hidden world",
            "ancient artifact's mystery",
            "cosmic forces' clash",
            "virtual reality challenge",
            "sorcerer's quest for knowledge",
            "enchanted kingdom's legacy",
            "futuristic dystopia",
            "struggle against mythical creatures",
            "interstellar journey home",
            "timeless enchantment",
            "enchanted forest's enchantment",
            "fateful choice to be made",
            "cultural traditions' revival",
            "spiritual realm's secrets",
            "dystopian rebellion",
            "otherworldly adventure",
            "folklore realm's balance",
            "steampunk airship race",
            "cyberpunk city's secrets",
            "post-apocalyptic wasteland",
            "spacefarer's exploration",
            "enchanted map's quest",
            "time-altering paradox",
            "fantasy realm's salvation",
            "cosmic mysteries' revelation",
            "virtual reality escape room",
            "sorcerer's ancient spell",
            "enchanted monarchy's prophecy",
            "futuristic space exploration",
            "struggle for survival in a magical wilderness",
            "interdimensional artifact's power",
            "time traveler's quest",
            "fantasy land's liberation",
            "supernatural beings' hidden agenda",
            "ancient artifact's forgotten history",
            "cosmic harmony and chaos",
            "virtual reality gaming tournament",
            "sorcerer's ultimate challenge",
            "enchanted kingdom's revival",
            "futuristic utopian society",
            "stranded on an uncharted planet",
            "interstellar peacekeeping",
            "timeless tale of true love",
            "enchanted forest's guardians",
            "fateful decision that changes everything",
            "cultural heritage preservation",
            "spiritual enlightenment journey",
            "dystopian uprising",
            "otherworldly friendship",
            "folklore creatures' alliance",
            "steampunk revolution",
            "cyberpunk city's underbelly",
            "post-apocalyptic hope",
            "space explorers' adventure",
            "enchanted relic's quest",
            "time-traveling adventure",
            "fantasy realm's destiny",
            "cosmic guardians' mission",
            "virtual reality enigma",
            "sorcerer's magical legacy",
            "enchanted monarchy's revival",
            "futuristic cityscape exploration",
            "struggle against a formidable enemy",
            "interstellar journey to the unknown",
            "timeless journey through history",
            "enchanted forest's secrets",
            "fateful encounter that changes fate",
            "cultural harmony and understanding",
            "spiritual awakening and transformation",
            "dystopian survival",
            "otherworldly exploration",
            "folklore realm's magic",
            "steampunk invention's unveiling",
            "cyberpunk city's rebellion",
            "post-apocalyptic renewal",
            "space pioneers' courage",
            "enchanted tapestry's tale",
            "time-bending adventure",
            "fantasy realm's quest for peace",
            "cosmic realm's balance",
            "virtual reality challenge",
            "sorcerer's ancient grimoire",
            "enchanted monarchy's awakening",
            "futuristic spacefaring civilization",
            "struggle against dark forces",
            "interdimensional portal's mystery",
            "time traveler's mission",
            "fantasy land's restoration",
            "supernatural beings' quest",
            "ancient artifact's rediscovery",
            "cosmic conflict and resolution",
            "virtual reality escapade",
            "sorcerer's epic trial",
            "enchanted kingdom's legacy",
            "futuristic metropolis",
            "struggle for survival in an enchanted wilderness",
            "interdimensional journey through dimensions",
            "timeless journey of self-discovery",
            "enchanted forest's mystical guardians",
            "fateful encounter with destiny",
            "cultural celebration of unity",
            "spiritual realm's enlightenment",
            "dystopian rebellion against tyranny",
            "otherworldly odyssey",
            "folklore creatures' alliance",
            "steampunk gadget competition",
            "cyberpunk revolution against corruption",
            "post-apocalyptic rebirth",
            "spacefarer's cosmic exploration",
            "enchanted book's magical tales",
            "time-traveling escapade through eras",
            "fantasy realm's prophecy",
            "cosmic guardian's ancient quest",
            "virtual reality realm's secret",
            "sorcerer's quest for the ultimate power",
            "enchanted monarchy's redemption",
            "futuristic space colonization",
            "struggle for survival against mythical creatures",
            "interstellar diplomacy and alliance",
            "timeless love transcending time and space",
            "enchanted forest's hidden realm",
            "fateful decision with dire consequences",
            "cultural folklore unification",
            "spiritual journey to enlightenment",
            "dystopian society's resistance",
            "otherworldly friendship forged in adversity",
            "folklore realm's balance in jeopardy",
            "steampunk adventure in the skies",
            "cyberpunk city's dark secrets",
            "post-apocalyptic hope for a new beginning",
            "space explorer's cosmic odyssey",
            "enchanted map's quest for treasures",
            "time-altering adventure of paradoxes",
            "fantasy realm's salvation from darkness",
            "cosmic mysteries' revelation",
            "virtual reality escapade in a digital world",
            "sorcerer's ancient spell of power",
            "enchanted monarchy's prophecy fulfilled",
            "futuristic journey through the stars",
            "struggle for survival in an enchanted wilderness",
            "interdimensional artifact's power unleashed",
            "time traveler's quest to alter fate",
            "fantasy land's liberation from tyranny",
            "supernatural beings' hidden world exposed",
            "ancient artifact's forgotten history revealed",
            "cosmic harmony and chaos clash",
            "virtual reality gaming tournament of champions",
            "sorcerer's ultimate challenge for supremacy",
            "enchanted kingdom's revival and restoration",
            "futuristic utopian society's challenges",
            "stranded on an uncharted planet in space",
            "interstellar peacekeeping for the galaxy",
            "timeless tale of true love's triumph",
            "enchanted forest's guardians protecting its secrets",
            "fateful decision that changes destiny",
            "cultural heritage preservation for future generations",
            "spiritual enlightenment journey of self-discovery",
            "dystopian society's uprising against oppression",
            "otherworldly exploration of uncharted realms",
            "folklore realm's magic and wonder",
            "steampunk revolution against industrial tyranny",
            "cyberpunk city's underbelly of crime and rebellion",
            "post-apocalyptic renewal and hope for a new world",
            "space explorers' adventure beyond the stars",
            "enchanted tapestry's tale of forgotten legends",
            "time-bending adventure through past and future",
            "fantasy realm's quest for peace and unity",
            "cosmic realm's balance of light and darkness",
            "virtual reality challenge of mind and spirit",
            "sorcerer's ancient grimoire of arcane knowledge",
            "enchanted monarchy's awakening to its true power",
            "futuristic spacefaring civilization's grand vision",
            "struggle against dark forces threatening the world",
            "interdimensional portal's mystery unraveling",
            "time traveler's mission to preserve the timeline",
            "fantasy land's restoration from chaos to order",
            "supernatural beings' quest to protect their realm",
            "ancient artifact's rediscovery and its secrets",
            "cosmic conflict and resolution among celestial beings",
            "virtual reality escapade through a digital dreamscape",
            "sorcerer's epic trial for mastery of magic",
            "enchanted kingdom's legacy passed down through generations",
            "futuristic metropolis of innovation and wonder",
            "struggle for survival in an enchanted wilderness",
            "interdimensional journey through portals of possibility",
            "timeless journey of self-discovery and enlightenment",
            "enchanted forest's mystical guardians protecting its realm",
            "fateful encounter with destiny's design",
            "cultural celebration of unity and diversity",
            "spiritual realm's enlightenment and transcendence",
            "dystopian rebellion against totalitarian rule",
            "otherworldly odyssey through uncharted realms",
            "folklore creatures' alliance to restore peace",
            "steampunk gadget competition of brilliant inventors",
            "cyberpunk revolution against corporate control",
            "post-apocalyptic rebirth of a new civilization",
            "spacefarer's cosmic exploration beyond the stars",
            "enchanted book's magical tales of wonder",
            "time-traveling escapade through historical eras",
            "fantasy realm's prophecy of a chosen hero",
            "cosmic guardian's ancient quest to protect the universe",
            "virtual reality realm's secret hidden within the code",
            "sorcerer's quest for the ultimate power and wisdom",
            "enchanted monarchy's prophecy fulfilled by a chosen one",
            "futuristic journey through the cosmos and beyond",
            "struggle for survival against mythical creatures",
            "interstellar diplomacy and alliance between planets",
            "timeless love transcending time, space, and even death",
            "enchanted forest's hidden realm of magical beings",
            "fateful decision with dire consequences for the world",
            "cultural folklore unification to preserve ancient tales",
            "spiritual journey to enlightenment and inner peace",
            "dystopian society's resistance against oppressive rule",
            "otherworldly friendship forged in adversity and trust",
            "folklore realm's balance in jeopardy of being disrupted",
            "steampunk adventure in the skies on magnificent airships",
            "cyberpunk city's dark secrets and hidden rebellions",
            "post-apocalyptic hope for a new beginning and rebuilding",
            "space explorer's cosmic odyssey to explore new worlds",
            "enchanted map's quest for hidden treasures and relics",
            "time-altering adventure of paradoxes and alternate realities",
            "fantasy realm's salvation from darkness and tyranny",
            "cosmic mysteries' revelation of ancient cosmic beings",
            "virtual reality escapade in a digital world of wonders",
            "sorcerer's ancient spell of power and ancient secrets",
            "enchanted monarchy's prophecy fulfilled by a destined ruler",
            "futuristic journey through the stars to discover new horizons",
            "struggle for survival in an enchanted wilderness filled with challenges",
            "interdimensional artifact's power unleashed with unforeseen consequences",
            "time traveler's quest to preserve the fabric of time and space",
            "fantasy land's liberation from tyranny and darkness",
            "supernatural beings' hidden world exposed to the mortal realm",
            "ancient artifact's forgotten history revealed, unveiling its true purpose",
            "cosmic harmony and chaos clash, shaping the destiny of worlds",
            "virtual reality challenge that tests the limits of human potential",
            "sorcerer's ultimate challenge to confront ancient and powerful adversaries",
            "enchanted kingdom's revival, restoring its former glory and grandeur",
            "futuristic utopian society's challenges in maintaining peace and harmony",
            "stranded on an uncharted planet in space, fighting for survival and escape",
            "interstellar peacekeeping mission to prevent galactic conflicts",
            "timeless tale of true love that transcends time and space",
            "enchanted forest's guardians protecting its mystical wonders",
            "fateful decision that changes the course of destinies",
            "cultural heritage preservation to safeguard ancient traditions",
            "spiritual enlightenment journey to discover inner truths",
            "dystopian society's rebellion against oppressive regimes",
            "otherworldly exploration of uncharted realms and civilizations",
            "folklore creatures' alliance to defend the realm from evil forces",
            "steampunk revolution against industrial oppression",
            "cyberpunk city's underbelly of corruption and rebellion",
            "post-apocalyptic renewal, rebuilding from the ashes of destruction",
            "spacefarer's cosmic exploration to discover new planets and lifeforms",
            "enchanted tapestry's tale of forgotten legends and ancient myths",
            "time-bending adventure through the past and future",
            "fantasy realm's quest for peace and unity among diverse factions",
            "cosmic realm's balance of light and darkness hanging in the balance",
            "virtual reality challenge that tests the mind and spirit",
            "sorcerer's ancient grimoire filled with arcane wisdom and spells",
            "enchanted monarchy's awakening to its true power and potential",
            "futuristic spacefaring civilization's grand vision for the universe",
            "struggle against dark forces threatening to plunge the world into chaos",
            "interdimensional portal's mystery unraveling, revealing hidden truths",
            "time traveler's mission to preserve the timeline and protect history",
            "fantasy land's restoration from chaos to peace and prosperity",
            "supernatural beings' quest to protect their realm from impending danger",
            "ancient artifact's rediscovery and the revelation of its secrets",
            "cosmic conflict and resolution among celestial beings and cosmic forces",
            "virtual reality escapade through a digital dreamscape of imagination",
            "sorcerer's epic trial to prove their worth and mastery of magic",
            "enchanted kingdom's legacy passed down through generations of rulers",
            "futuristic metropolis of innovation, wonder, and technological marvels",
            "struggle for survival in an enchanted wilderness teeming with mythical creatures",
            "interdimensional journey through portals of possibility and parallel worlds",
            "timeless journey of self-discovery and enlightenment, seeking inner truths",
            "enchanted forest's mystical guardians protecting its sacred and magical essence",
            "fateful encounter with destiny's design, shaping the fate of individuals and worlds",
            "cultural celebration of unity, embracing the rich diversity of traditions and customs",
            "spiritual realm's enlightenment and transcendence, seeking higher states of consciousness",
            "dystopian rebellion against totalitarian rule, fighting for freedom and justice",
            "otherworldly odyssey through uncharted realms, encountering strange and wondrous beings",
            "folklore creatures' alliance to restore peace and harmony to a world in turmoil",
            "steampunk gadget competition of brilliant inventors, showcasing ingenious creations",
            "cyberpunk revolution against corporate control and technological oppression",
            "post-apocalyptic rebirth of a new civilization, rebuilding society from the ground up",
            "spacefarer's cosmic exploration beyond the stars, discovering distant galaxies and worlds",
            "enchanted book's magical tales of wonder, unlocking the power of imagination and dreams",
            "time-traveling escapade through historical eras, witnessing significant moments in time",
            "fantasy realm's prophecy of a chosen hero destined to bring about change and restoration",
            "cosmic guardian's ancient quest to protect the universe from impending threats",
            "virtual reality realm's secret hidden within the code, unveiling virtual mysteries",
            "sorcerer's quest for the ultimate power and wisdom, embarking on a magical journey",
            "enchanted monarchy's prophecy fulfilled by a chosen one, destined to rule with wisdom",
            "futuristic journey through the cosmos and beyond, exploring the wonders of space",
            "struggle for survival against mythical creatures, battling legendary beasts and monsters",
            "interstellar diplomacy and alliance between planets, forging intergalactic relations",
            "timeless love transcending time, space, and even death, a love that defies all odds",
            "enchanted forest's hidden realm of magical beings, uncovering the mysteries of the woods",
            "fateful decision with dire consequences for the world, leading to unforeseen outcomes",
            "cultural folklore unification to preserve ancient tales and myths for future generations",
            "spiritual journey to enlightenment and inner peace, seeking spiritual awakening",
            "dystopian society's resistance against oppressive forces, fighting for a better future",
            "otherworldly exploration of uncharted realms, encountering wonders and dangers alike",
            "folklore realm's magic and wonder, exploring a world filled with mythical beings and powers",
            "steampunk revolution against industrial tyranny, challenging oppressive regimes",
            "cyberpunk city's underbelly of crime and rebellion, navigating a world of corruption",
            "post-apocalyptic renewal and hope for a new world, rebuilding after catastrophe",
            "space explorers' adventure beyond the stars, discovering new frontiers in space",
            "enchanted tapestry's tale of forgotten legends, unraveling ancient stories",
            "time-bending adventure through past and future, experiencing temporal twists",
            "fantasy realm's quest for peace and unity, overcoming conflicts and divisions",
            "cosmic realm's balance of light and darkness, a cosmic struggle for equilibrium",
            "virtual reality challenge of mind and spirit, testing the limits of human potential",
            "sorcerer's ancient grimoire of arcane knowledge, unlocking powerful magic",
            "enchanted monarchy's awakening to its true power, a transformation of rulership",
            "futuristic spacefaring civilization's grand vision, exploring the cosmos",
            "struggle against dark forces threatening the world, battling malevolent entities",
            "interdimensional portal's mystery unraveling, uncovering multidimensional secrets",
            "time traveler's mission to preserve the fabric of time and space, safeguarding history",
            "fantasy land's restoration from chaos to order, bringing harmony to the realm",
            "supernatural beings' hidden world exposed, revealing the existence of magical beings",
            "ancient artifact's forgotten history revealed, unlocking its purpose and significance",
            "cosmic harmony and chaos clash, shaping destinies of worlds and beings",
            "virtual reality challenge that tests the mind and spirit, pushing the limits of imagination",
            "sorcerer's ultimate challenge to confront ancient and powerful adversaries",
            "enchanted kingdom's revival, restoring its former glory and grandeur",
            "futuristic utopian society's challenges in maintaining peace and harmony",
            "stranded on an uncharted planet in space, fighting for survival and escape",
            "interstellar peacekeeping mission to prevent galactic conflicts",
            "timeless tale of true love that transcends time and space",
            "enchanted forest's guardians protecting its mystical wonders",
            "fateful decision that changes the course of destinies",
            "cultural heritage preservation to safeguard ancient traditions",
            "spiritual enlightenment journey to discover inner truths",
            "dystopian society's rebellion against oppressive regimes",
            "otherworldly exploration of uncharted realms and civilizations",
            "folklore creatures' alliance to defend the realm from evil forces",
            "steampunk revolution against industrial oppression",
            "cyberpunk city's underbelly of corruption and rebellion",
            "post-apocalyptic renewal, rebuilding from the ashes of destruction",
            "spacefarer's cosmic exploration to discover new planets and lifeforms",
            "enchanted tapestry's tale of forgotten legends and ancient myths",
            "time-bending adventure through the past and future",
            "fantasy realm's quest for peace and unity among diverse factions",
            "cosmic realm's balance of light and darkness hanging in the balance",
            "virtual reality challenge that tests the mind and spirit",
            "sorcerer's ancient grimoire filled with arcane wisdom and spells",
            "enchanted monarchy's awakening to its true power and potential",
            "futuristic spacefaring civilization's grand vision for the universe",
            "struggle against dark forces threatening to plunge the world into chaos",
            "interdimensional portal's mystery unraveling, revealing hidden truths",
            "time traveler's quest to preserve the timeline and protect history",
            "fantasy land's restoration from chaos to peace and prosperity",
            "supernatural beings' quest to protect their realm from impending danger",
            "ancient artifact's rediscovery and the revelation of its secrets",
            "cosmic conflict and resolution among celestial beings and cosmic forces",
            "virtual reality escapade through a digital dreamscape of imagination",
            "sorcerer's epic trial to prove their worth and mastery of magic",
            "enchanted kingdom's legacy passed down through generations of rulers",
            "futuristic metropolis of innovation, wonder, and technological marvels",
            "struggle for survival in an enchanted wilderness teeming with mythical creatures",
            "interdimensional journey through portals of possibility and parallel worlds",
            "timeless journey of self-discovery and enlightenment, seeking inner truths",
            "enchanted forest's mystical guardians protecting its sacred and magical essence",
            "fateful encounter with destiny's design, shaping the fate of individuals and worlds",
            "cultural celebration of unity, embracing the rich diversity of traditions and customs",
            "spiritual realm's enlightenment and transcendence, seeking higher states of consciousness",
            "dystopian rebellion against totalitarian rule, fighting for freedom and justice",
            "otherworldly exploration of uncharted realms, encountering wonders and dangers alike",
            "folklore creatures' alliance to restore peace and harmony to a world in turmoil",
            "steampunk gadget competition of brilliant inventors, showcasing ingenious creations",
            "cyberpunk revolution against corporate control and technological oppression",
            "post-apocalyptic rebirth of a new civilization, rebuilding society from the ground up",
            "spacefarer's cosmic exploration beyond the stars, discovering distant galaxies and worlds"
        ]
        return `${variableEvent([
            `multiple scenes of a ${searchArray(story)} ${searchArray(['starting with', 'ending with'])}` ])}`
    }

    function artPiece(){
        return variableEvent(size) + searchArray(artForm[0])
    }
function background() {
    let background = [
        `${searchArray(['an impressive', 'a typical', 'a ruined'])} ${findRace()} ${searchArray( ['village','city','town','caravan','tower','castle'] )} ${searchArray( ['sitting quietly','is burning','during a thunderstorm','during sunset','with a red sky','wreathed in storm',`being overtaken by ${searchArray([`${findRace()}s`,`${searchArray(monster[rollDice(1)])}`])}`])}`,
        `a(n) ${searchArray(['grand feast being held in a cramped tavern room','pack of gnolls battling a town militia','large army of dark knights being driven away by angels','creature of colossal size','sunset in the Feywild','Illithid Nautiloid Spelljammer','castle overlooking an active volcano','surrealism landscape of an elemental plane','wonderful cathedral standing on a hill, dedicated to whatever god the ruler follows','waterfall and lake in the Feywilds with fey creatures gathered round','sunset reflecting through an icy glacier', 'active volcanic mountain, casting a glow into the night sky','active volcano','expansive seascape','abundant hilly plains',' expanse of mountains','icy glacier and rough waters',' abundance of tidal pools on a rocky shore, full of unfamiliar sea creatures', 'endless cityscape'])}`,
        `a(n) ${searchArray(monster[rollDice(1)])} ${searchArray(['dueling','fighting','struggling against','battling','attacking'])} a ${searchArray([searchArray(monster[rollDice(1)]),`${searchArray(['group of adventurers', `group of ${searchArray(subject[0])}s`])} while a group of ${findRace()}s flee`])}`,
        `an epic battle scene of ${searchArray([`two ${findRace()} armies fighting each other`, `${findRace()} army against a ${searchArray([searchArray(monster[rollDice(1)]), 'demonic','abyssal','divine','elemental'])} incursion`])}`,
        `a ${searchArray(['tranquil landscape', 'fine castle interior','looming storm over the mountains'])}`,
                
    ] 
    let backgroundTemplates =[
        [//specific
        `Behind you see ${searchArray(background)}`,
        `While ${searchArray(background)} is behind`,
        `As ${searchArray(background)} forms the backdrop`,
        `Against the backdrop of ${searchArray(background)}`,
        `With the distant ${searchArray(background)}`,
        `While ${searchArray(background)} adorns the horizon`,
        `With ${searchArray(background)} adding a touch of mystery`,
        `Featuring ${searchArray(background)}.`,
        `Set amidst ${searchArray(background)}`,
        `Encompassed by ${searchArray(background)}`,
        `Set against ${searchArray(background)}`,
        `${searchArray(background)} wraps around the subject`,
        `With ${searchArray(background)} in the disctance`,
        `You can see ${searchArray(background)} in the distance`,
        `There is${searchArray(background)} is detailed`
        ],
        [//nonspecific
            `Enchanted Aura: A glowing aura of magical energy surrounding the main subject, radiating fantastical colors like shimmering gold, iridescent blue, or ethereal green`,
            `Mystical Mist: A soft, mystical mist veiling the background, giving an otherworldly and enchanting atmosphere to the artwork`,
            `Runed Patterns: Elaborate runes and symbols etched into the background, hinting at ancient spells and arcane knowledge`,
            `Celestial Sky: A celestial sky with floating constellations and a distant moon or planets, creating a magical and cosmic ambiance`,
            `Faerie Glitter: Delicate glimmers of faerie dust or glitter sprinkled across the background, adding a touch of whimsy and enchantment`,
            `Elemental Wisps: Faint, swirling elemental wisps like fire, water, earth, or air, creating an elemental backdrop that complements the main subject`,
            `Elven script: An intricately written elven as a backdrop, featuring mythical creatures and legendary heroes from ancient folklore`,
            `Spellbound Portal: A magical portal or doorway in the background, suggesting a connection to another realm or hidden dimension`,
            `Dragon Scales: A pattern of dragon scales adorning the background, evoking the presence of mighty dragons and their mythical power`,
            `Ancient Glyphs: Ancient glyphs and hieroglyphs decorating the background, imbuing the artwork with an aura of ancient mysticism`,
            `Enchanted Runes: Intricate runes and glyphs floating in the background, radiating a mystical aura of ancient magic`,
            `Ethereal Mist: A soft, ethereal mist gently enveloping the scene, adding an otherworldly and mysterious ambiance`,
            `Celestial Alignment: A pattern of stars and constellations forming a celestial alignment in the backdrop, hinting at cosmic forces at play`,
            `Arcane Symbols: An assortment of arcane symbols and sigils scattered across the background, alluding to hidden secrets and powerful spells`,
            `Elemental Swirls: Swirling patterns representing the four elements (fire, water, earth, air) intertwining in a harmonious dance`,
            `Fae Tracery: Delicate tracery of leaves, flowers, and faerie wings etched gracefully in the background, evoking the presence of magical beings`,
            `Dragon Scales: An abstract motif of dragon scales creating a sense of strength and ancient power surrounding the main subject`,
            `Stardust Glimmer: Glittering stardust scattered throughout the backdrop, evoking the grandeur of the cosmos and the vastness of space`,
            `Mythical Creatures Silhouettes: Subtle silhouettes of mythical creatures, such as dragons, griffins, and unicorns, hinting at unseen wonders`,
            `Ancient Tapestry: An illusion of an ancient tapestry adorned with mythical scenes, weaving a tale of legendary heroes and epic adventures`,
            `Elven Weave: An elegant elven weave pattern intricately adorning the background, reflecting the timeless artistry of elven craftsmanship`,
            `Timeless Scrolls: Scrolls and parchments with faded inscriptions, representing the passage of ancient knowledge through the ages`,
            `Celestial Whirls: Spiraling whirls resembling cosmic energy, symbolizing the connection between the mundane and celestial realms`,
            `Elemental Essences: Essence vials containing swirling colors representing elemental energies, lending an elemental touch to the scene`,
            `Mystical Glyphs: Enigmatic glyphs etched with magical intent, creating an air of mystery and enchantment`,
            `Faerie Trails: Faint trails of faerie lights darting playfully in the backdrop, leading to a realm of magic and whimsy`,
            `Astral Veil: An illusion of a shimmering astral veil, revealing glimpses of distant planes and parallel dimensions`,
            `Dragonfire Embers: Glowing embers of dragonfire floating in the background, infusing the scene with a sense of danger and power`,
            `Enchanted Vortex: A mesmerizing vortex swirling in the background, signifying a portal to other realms and realms beyond`,
            `Mythical Ouroboros: An abstract ouroboros symbol, representing the eternal cycle of life, death, and rebirth in the realm of fantasy`,
            `Elusive Shadows: Playful shadows dancing in the background, hinting at unseen magical creatures lurking just beyond the viewer's sight`,
            `Enchanted Runestones: Glimmering runestones scattered throughout the scene, each holding a unique magical essence and power`,
            `Fey Enchantment: Soft glimmers of fey enchantment gently illuminating the background, weaving a spell of enchantment and wonder`,
            `Elemental Whispers: Whispers of elemental energies resonating in the backdrop, evoking the raw power of nature's forces`,
            `Celestial Dust: Celestial dust particles sprinkled across the canvas, creating a sense of celestial wonder and cosmic connection`,
            `Mythical Constellations: Faint outlines of mythical constellations forming a celestial map, guiding the viewer through the realm of fantasy`,
            `Timeless Gates: Imaginary gates opening to fantastical realms, symbolizing the endless possibilities of the fantasy world`,
            `Dreamcatcher Weave: An intricate dreamcatcher weave pattern, filtering out nightmares and capturing dreams of magic and adventure`,
            `Whimsical Ripples: Subtle ripples of magic spreading across the background, conveying the fluidity and unpredictability of fantasy`,
            `Ancient Scrolls: Ancient scrolls unfurling in the backdrop, revealing the hidden wisdom and ancient prophecies of fantasy realms`,
            `Ethereal Vines: Ethereal vines twirling and winding through the background, connecting the artwork to the natural magic of the world`,
            `Celestial Orbs: Celestial orbs suspended in the air, representing distant celestial bodies and the mysteries of the cosmos`,
            `Enchanted Swirls: Enchanting swirls and patterns conjuring visions of magical spells and rituals`,
            `Fae Illusions: Subtle illusions cast by mischievous fae beings, inviting the viewer into a realm of delightful trickery`,
            `Elemental Sparks: Elemental sparks emanating from the backdrop, igniting the magic within the scene`,
            `Whispers of Destiny: Whispers of destiny floating in the background, weaving the threads of fate for the fantasy characters`,
            `Mystical Crystal Vein: A mystical crystal vein meandering through the canvas, channeling the energies of the fantasy world`,
            `Dragon's Breath: Trails of dragon's breath swirling around the backdrop, evoking the presence of majestic dragons`,
            `Starlit Canopy: A starlit canopy stretching overhead, immersing the viewer in the wonder of the night sky`,
            "Soft, mystical mist creating an otherworldly atmosphere.",
            "Elaborate runes etched into the background, hinting at ancient spells.",
            "A celestial sky with floating constellations, creating a magical ambiance.",
            "Delicate glimmers of faerie dust or glitter sprinkled across the background.",
            "Faint, swirling elemental wisps like fire, water, earth, or air, adding an elemental touch.",
            "An intricately written elven script as a backdrop, featuring mythical creatures.",
            "A magical portal or doorway in the background, suggesting a connection to other realms.",
            "A pattern of dragon scales adorning the background, evoking the presence of mighty dragons.",
            "Ancient glyphs and hieroglyphs decorating the background, imbuing the artwork with ancient mysticism.",
            "Intricate runes and glyphs floating in the background, radiating a mystical aura of ancient magic.",
            "A soft, ethereal mist gently enveloping the scene, adding mystery and wonder.",
            "A pattern of stars and constellations forming a celestial alignment, hinting at cosmic forces at play.",
            "An assortment of arcane symbols and sigils scattered across the background, alluding to hidden secrets.",
            "Swirling patterns representing the four elements (fire, water, earth, air), intertwining in a harmonious dance.",
            "Delicate tracery of leaves, flowers, and faerie wings etched gracefully in the background.",
            "Glowing embers of dragonfire floating in the background, infusing the scene with a sense of power.",
            "A mesmerizing vortex swirling in the background, signifying a portal to other realms.",
            "An abstract ouroboros symbol, representing the eternal cycle of life, death, and rebirth.",
            "Playful shadows dancing in the background, hinting at unseen magical creatures.",
            "Soft glimmers of fey enchantment gently illuminating the background, weaving a spell of enchantment and wonder.",
            "Whispers of elemental energies resonating in the backdrop, evoking the raw power of nature's forces.",
            "Celestial dust particles sprinkled across the canvas, creating a sense of celestial wonder and cosmic connection.",
            "Faint outlines of mythical constellations forming a celestial map, guiding the viewer through the realm of fantasy.",
            "Imaginary gates opening to fantastical realms, symbolizing the endless possibilities of the fantasy world.",
            "An intricate dreamcatcher weave pattern, filtering out nightmares and capturing dreams of magic and adventure.",
            "Subtle ripples of magic spreading across the background, conveying the fluidity and unpredictability of fantasy.",
            "Ancient scrolls unfurling in the backdrop, revealing the hidden wisdom and ancient prophecies of fantasy realms.",
            "Ethereal vines twirling and winding through the background, connecting the artwork to the natural magic of the world.",
            "Celestial orbs suspended in the air, representing distant celestial bodies and the mysteries of the cosmos.",
            "Enchanting swirls and patterns conjuring visions of magical spells and rituals.",
            "Subtle illusions cast by mischievous fae beings, inviting the viewer into a realm of delightful trickery.",
            "Elemental sparks emanating from the backdrop, igniting the magic within the scene.",
            "Whispers of destiny floating in the background, weaving the threads of fate for the fantasy characters.",
            "A mystical crystal vein meandering through the canvas, channeling the energies of the fantasy world.",
            "Trails of dragon's breath swirling around the backdrop, evoking the presence of majestic dragons.",
            "A starlit canopy stretching overhead, immersing the viewer in the wonder of the night sky.",
            "Enigmatic mist shrouding the background, hinting at mysterious and ancient secrets.",
            "Crackling arcane energy pulsating through the backdrop, infusing the artwork with magical power.",
            "Astral constellations dancing in the background, portraying the tapestry of fate in the realm of fantasy.",
            "Whimsical silhouettes of fantastical creatures lurking in the shadows, waiting to reveal themselves.",
            "A veil of enchantment descending upon the backdrop, captivating the viewer with its magical allure.",
            "Ancient ruins half-buried in the background, hinting at lost civilizations and forgotten history.",
            "A shimmering waterfall cascading down the backdrop, symbolizing the flow of magical energies.",
            "Mysterious misty mountains rising in the background, concealing ancient legends and mythical beings.",
            "A swirling vortex of colors engulfing the backdrop, transporting the viewer to a realm of dreams and magic.",
            "Glimpses of fairy lights twinkling in the background, hinting at the presence of mischievous sprites.",
            "A celestial phenomenon like an eclipse or comet lighting up the backdrop, signifying a momentous event in the fantasy world.",
            "Intricate patterns of enchanted flora adorning the background, reflecting the magical essence of the realm.",
            "A luminescent full moon casting an ethereal glow on the backdrop, revealing hidden wonders in the night.",
            "Ethereal echoes of forgotten incantations resonating in the background, echoing the passage of time.",
            "A vibrant and colorful aurora borealis illuminating the backdrop, adding an otherworldly and mesmerizing touch.",
            "A floating island or mystical landmass suspended in the background, representing a realm of fantasy.",
            "Whirling sandstorms or vortexes hinting at the presence of desert spirits and ancient desert magic.",
            "Iridescent sea waves crashing against the backdrop, embodying the untamed power of the ocean.",
            "A starry night sky with shooting stars streaking across the backdrop, promising wishes come true.",
            "A hidden forest glade tucked away in the background, teeming with magical flora and fauna.",
            "A hidden cave entrance in the backdrop, leading to an underground world filled with secrets.",
            "An enchanted garden with mystical flowers and plants blooming in the background, creating a magical oasis.",
            "A shimmering lake reflecting the stars and moon in the background, mirroring the fantasy realm.",
            "A swirling portal of light in the backdrop, connecting different dimensions and realms.",
            "A magical clock or timepiece indicating a moment of profound significance in the fantasy narrative.",
            "Ancient stone ruins rising from the background, a testament to the passage of time and history.",
            "A labyrinth of glowing archways and passages stretching into the background, leading to unseen destinations.",
            "A hidden library filled with dusty tomes and arcane knowledge, waiting to be explored.",
            "A floating city or castle suspended in the backdrop, symbolizing the grandeur and wonder of fantasy architecture.",
            "Majestic waterfalls cascading from the background, embodying the raw power and beauty of nature's magic.",
            "A mystical tree with glowing leaves and roots reaching into the backdrop, representing the heart of the fantasy world.",
            "An enigmatic and ancient artifact or relic concealed in the background, holding immense power and significance.",
            "A magical marketplace bustling in the background, filled with fantastical wares and curious creatures.",
            "An enchanted forest with glowing flora and fauna in the backdrop, a realm of mystical beings.",
            "A whirlwind of swirling leaves and petals creating an ethereal vortex in the background.",
            "A celestial palace or temple gleaming in the backdrop, a sanctuary for gods and mythical beings.",
            "A frozen landscape with shimmering ice crystals in the background, evoking a sense of frozen magic.",
            "A portal of shadowy mist leading to the unknown in the background, tempting the adventurous at heart.",
            "A colorful and fantastical sky with multiple moons or suns in the backdrop, adding a touch of surrealism.",
            "An ancient stone circle or magical circle etched into the background, holding secrets of the ages.",
            "An underwater realm with swirling currents and marine creatures adorning the background.",
            "A mystical waterfall flowing upward in the backdrop, defying the laws of nature.",
            "A floating island with gravity-defying structures and landscapes, a feat of magical engineering.",
            "A mystical storm brewing in the background, crackling with elemental energy.",
            "An astral plane with shimmering stars and galaxies as the backdrop, transcending the bounds of reality.",
            "A hidden portal to the realm of dreams, where imagination and reality intertwine.",
            "A shimmering field of magic crystals sparkling in the background, resonating with mystical energy.",
            "An ever-changing and swirling vortex of color representing the realm of illusions.",
            "A hidden underground city with glowing mushrooms and crystals adorning the background.",
            "An ethereal sky with floating islands and celestial creatures soaring in the backdrop.",
            "An ancient tree of life with intricate roots stretching through the background, symbolizing the interconnectedness of all things.",
            "A mysterious and ancient floating monolith looming in the background, shrouded in enigmatic power.",
            "A chaotic storm of elemental forces colliding in the backdrop, signifying a climactic battle of magic.",
            "A mythical beast or creature in the background, roaming the fantasy landscape.",
            "An ever-changing and mesmerizing kaleidoscope of colors in the backdrop, reflecting the ever-shifting nature of fantasy realms.",
            "A surreal and abstract dreamscape in the background, blurring the lines between fantasy and reality.",
            "A magical doorway or portal that leads to hidden realms beyond the canvas.",
            "A vibrant rainbow stretching across the backdrop, symbolizing the bridge between the mortal and magical worlds.",
            "An ancient city with grand architecture and mystical towers rising in the background, a testament to the marvels of fantasy civilization.",
            `A serene landscape with snow-capped mountains, a crystal-clear river, and lush green forests`,
            `An enchanting view of misty mountains, a meandering river, and abundant foliage`,
            `A breathtaking scene of majestic peaks, a tranquil river, and verdant green fields`,
            `A postcard-perfect sight featuring rugged mountains, a winding river, and dense green forests`,
            `A picturesque setting with towering mountains, a babbling brook, and lush vegetation`,
            `A captivating view of jagged mountains, a glistening river, and vibrant green meadows`,
            `An idyllic landscape showcasing rocky mountains, a peaceful river, and flourishing forests`,
            `A scenic panorama of majestic peaks, a serene river, and lush greenery`,
            `A tranquil scene with rolling mountains, a gentle river, and abundant vegetation`,
            `An awe-inspiring sight of grand mountains, a meandering river, and dense green foliage`,
            `An enchanted cityscape with towering magical spires and bustling streets filled with fantastical creatures`,
            `A vibrant metropolis in a fantasy realm, where towering elven towers and bustling marketplaces create a sense of wonder`,
            `A bustling urban landscape in a steampunk fantasy world, with towering clockwork buildings and busy steam-powered streets`,
            `An enchanting cityscape featuring floating buildings and busy streets filled with wizards, witches, and magical beings`,
            `A bustling urban setting in a fantasy kingdom, with towering castles and busy streets bustling with knights, merchants, and mythical creatures`,
            `A magical cityscape with towering crystal structures and busy streets illuminated by floating orbs of light`,
            `An otherworldly urban setting with towering alien buildings and busy streets filled with futuristic beings and flying vehicles`,
            `A bustling city in a cyberpunk fantasy world, with towering neon-lit buildings and busy streets crowded with cyborgs and futuristic technology`,
            `An enchanted metropolis with towering treehouses and busy streets where fairies, elves, and magical beings roam`,
            `A bustling urban landscape in a dystopian fantasy world, with towering industrial buildings and busy streets filled with rebels and steampunk contraptions`,
            `A tranquil beach at sunset, with the golden sun sinking below the horizon, casting a warm glow over the sand and waves`,
            `An idyllic coastal setting, where the sun paints the sky in hues of pink and orange as it sets over the serene beach`,
            `A picturesque beach scene with the setting sun creating a stunning reflection on the calm waters, surrounded by palm trees and seashells`,
            `An enchanting view of a beach at sunset, where the sky is ablaze with colors and the waves gently kiss the shore`,
            `A mesmerizing coastal landscape with the sun setting over the water, casting a magical light on the sandy beach and rocky cliffs`,
            `A romantic beach scene at sunset, with the sun dipping below the horizon, creating a breathtaking backdrop for a seaside stroll`,
            `A peaceful and dreamy beach setting, where the setting sun creates a beautiful silhouette against the palm trees and seagulls flying in the sky`,
            `An ethereal beach at sunset, where the sky is a canvas of pastel colors and the waves gently lap against the shore`,
            `A tranquil and serene beach scene, where the setting sun casts long shadows and the sea reflects the fading light`,
            `A magical beachscape at sunset, where the sun sinks into the water, creating a scene of natural beauty and tranquility`,
            `A mysterious forest path, dappled with sunlight filtering through the dense canopy of ancient trees`,
            `An enchanting woodland trail, winding through a dense forest filled with magical creatures and hidden secrets`,
            `A captivating forest path, shrouded in mist and surrounded by towering trees, leading deeper into the heart of the mystical woods`,
            `A magical pathway meandering through an enchanted forest, where rays of sunlight break through the foliage to illuminate the way`,
            `A tranquil forest trail, carpeted with fallen leaves and lined with ancient trees, creating an air of mystery and wonder`,
            `An alluring forest path, with the whispering of leaves and the chirping of birds filling the air as it leads deeper into the enchanted woods`,
            `A mysterious woodland trail, where shafts of moonlight pierce through the branches, guiding the way through the mystical forest at night`,
            `An inviting forest path, with moss-covered stones and ancient tree roots, creating a sense of adventure and discovery`,
            `A magical pathway winding through an ancient forest, with luminescent plants and mystical creatures illuminating the way`,
            `A secluded forest path, surrounded by lush vegetation and filled with the aroma of earth and moss, inviting exploration and contemplation`,
            `A captivating starry night, where the celestial sky is adorned with countless twinkling stars and a slender crescent moon`,
            `An enchanting night scene, with a canopy of stars twinkling in the velvety darkness and a delicate crescent moon casting a soft glow`,
            `A mesmerizing starry night sky, where the brilliance of the stars and the crescent moon create a breathtaking celestial display`,
            `A magical night sky, filled with a myriad of sparkling stars and a crescent moon that seems to smile down on the world below`,
            `A dreamlike starry night, with a crescent moon hanging low in the sky and the stars reflecting on still waters, creating a tranquil scene`,
            `An ethereal night sky, where the stars form a celestial tapestry and the crescent moon adds a touch of mystery to the dark canvas`,
            `A celestial spectacle of a starry night, with the crescent moon surrounded by a sea of twinkling stars, illuminating the landscape below`,
            `A serene starry night, with the crescent moon and stars casting a soft glow over the peaceful and tranquil surroundings`,
            `A captivating nocturnal scene, where the crescent moon and stars create an atmosphere of enchantment and wonder`,
            `A breathtaking starry night sky, with the crescent moon and stars shining brightly, inviting the viewer to gaze up and marvel at the beauty of the cosmos`,
            `A magnificent waterfall paradise, where the cascading waters plunge into a crystal-clear pool amidst a vibrant tropical oasis`,
            `An enchanting scene of a tropical waterfall paradise, with lush greenery and colorful flowers framing the majestic cascade`,
            `A captivating waterfall paradise, with the rushing waters surrounded by towering palm trees and exotic plants`,
            `A hidden waterfall paradise, nestled deep within a tropical rainforest, offering a serene and magical retreat`,
            `An idyllic waterfall paradise, with the soothing sound of water blending harmoniously with the vibrant colors of tropical foliage`,
            `A mesmerizing tropical scene, where the waterfall cascades gracefully into a lush paradise of ferns, moss, and tropical flora`,
            `A serene waterfall paradise, with the sparkling waters framed by a canopy of emerald leaves and vibrant blooms`,
            `An ethereal waterfall paradise, where the lush vegetation and sparkling waters create a surreal and dreamlike ambiance`,
            `A secluded waterfall paradise, with the lush landscape offering a peaceful and refreshing escape from the outside world`,
            `A breathtaking waterfall paradise, with the powerful cascade surrounded by a kaleidoscope of tropical colors and lush greenery`,
            `A mesmerizing desert dunescape, where the endless expanse of golden sand dunes creates an awe-inspiring and surreal landscape`,
            `An enchanting scene of desert dunes, with the undulating waves of sand stretching out to the horizon under the scorching sun`,
            `A captivating desert vista, where the rolling dunes form intricate patterns and shadows in the shifting desert light`,
            `A serene desert dunes scene, with the vast emptiness of the desert interrupted only by the majestic sand dunes`,
            `An ethereal desert landscape, where the desert dunes seem to ripple like waves frozen in time, giving an illusion of movement`,
            `A tranquil desert dunescape, with the soft curves of the sand dunes creating a sense of harmony and balance in the arid terrain`,
            `A surreal desert dunes scene, with the play of light and shadow on the sand dunes adding a touch of mystery to the landscape`,
            `An isolated desert dunes vista, where the solitude and vastness of the desert evoke a feeling of wonder and introspection`,
            `A breathtaking desert dunes view, with the vast expanse of sand dunes and clear blue skies creating a striking and dramatic contrast`,
            `An otherworldly desert dunescape, with the towering sand dunes resembling a landscape from a distant and alien world`,
            `An enchanting garden, where vibrant flowers bloom in every hue imaginable, and mystical creatures frolic among the petals`,
            `A whimsical scene of an enchanted garden, with glowing flowers and mischievous fairies dancing in the moonlight`,
            `A captivating garden filled with enchantment, where each flower possesses magical properties and secret wonders await discovery`,
            `An ethereal garden, where luminescent flowers emit a soft, otherworldly glow, and mystical creatures roam freely in the moonlit night`,
            `A mesmerizing garden filled with enchanting flora and fauna, where unicorns graze peacefully among the sparkling flowers`,
            `An idyllic enchanted garden, with ethereal butterflies fluttering around, leaving trails of shimmering dust in their wake`,
            `A serene scene of an enchanted garden, with colorful fireflies illuminating the night and casting a magical glow on the surroundings`,
            `A magical oasis, where an array of enchanted flowers bloom year-round, bringing everlasting beauty to the secret garden`,
            `A fantastical garden, with mythical creatures such as talking animals and elegant nymphs adding a touch of whimsy to the scene`,
            `A dreamlike garden, where the scent of exotic flowers fills the air, and mystical beings weave spells of enchantment among the lush foliage`,
            `A breathtaking snowy mountain scene, with towering peaks and snow-capped pine trees stretching into the wintry sky`,
            `A serene snow-covered landscape, where majestic mountains are blanketed in glistening white snow, creating a peaceful and magical ambiance`,
            `An enchanting snowy mountain vista, with the crisp air and pristine snow creating a sense of tranquility and wonder`,
            `A mesmerizing scene of snowy mountains, with the sun peeking through the clouds, casting a warm glow on the snow-covered terrain`,
            `A captivating snowy mountain view, with the jagged peaks of the mountains forming a dramatic backdrop against the snowy landscape`,
            `An ethereal snowy mountain landscape, where snowflakes gently fall from the sky, creating a magical and wistful atmosphere`,
            `A majestic snow-covered mountain scene, with evergreen trees dotting the snowy slopes, adding a touch of life to the winter wonderland`,
            `A tranquil snowy mountain vista, with the stillness of the winter landscape evoking a feeling of serenity and solitude`,
            `A picturesque snowy mountain landscape, with icy streams and frozen waterfalls adding to the beauty and allure of the scene`,
            `A surreal scene of snowy mountains, where the landscape appears frozen in time, creating a sense of awe and reverence for nature's grandeur`,
            `An enchanting underwater wonderland, with vibrant coral reefs teeming with a kaleidoscope of colorful fish and sea creatures`,
            `A mesmerizing scene of an underwater paradise, where sunbeams filter through the crystal-clear waters, illuminating the bustling marine life below`,
            `An ethereal underwater wonderland, with bioluminescent sea creatures creating a magical glow that lights up the ocean depths`,
            `A captivating underwater landscape, where graceful sea turtles glide through the turquoise waters, surrounded by an array of exotic fish`,
            `A serene underwater haven, with swaying coral formations creating a mesmerizing backdrop for the diverse marine life that calls this place home`,
            `A surreal underwater paradise, where dolphins playfully dance among the swaying seaweed, and schools of fish create breathtaking displays of movement`,
            `An idyllic scene of an underwater wonderland, where sea anemones sway gently in the currents, and seahorses gracefully navigate the underwater world`,
            `An enchanting underwater sanctuary, with ancient shipwrecks adding a sense of mystery and history to the vibrant marine ecosystem`,
            `A magical underwater oasis, where jellyfish with glowing tendrils drift gracefully through the depths, creating an otherworldly ambiance`,
            `A picturesque underwater wonderland, where colorful coral reefs provide shelter and sustenance for a diverse array of marine life, creating a harmonious and thriving ecosystem`,
            `A hauntingly beautiful scene of ancient ruins, with crumbling stone structures covered in lush vines and foliage, evoking a sense of lost grandeur`,
            `An awe-inspiring sight of ancient ruins, with towering pillars and ornate carvings, standing as silent witnesses to a long-forgotten civilization`,
            `A captivating view of ancient ruins, with intricate stonework and weathered sculptures, offering a glimpse into the artistic achievements of the past`,
            `A mystical setting of ancient ruins, where sunlight filters through the cracks in the stone, casting intriguing patterns of light and shadow`,
            `An enigmatic scene of ancient ruins, with hidden passages and underground chambers, holding untold secrets waiting to be discovered`,
            `A breathtaking view of ancient ruins, perched on a cliffside overlooking a vast and untamed wilderness, creating a powerful juxtaposition of nature and civilization`,
            `A hauntingly atmospheric sight of ancient ruins, with eerie echoes of the past, where whispers of ancient tales seem to linger in the air`,
            `An evocative scene of ancient ruins, with carved symbols and glyphs, offering tantalizing clues about the rituals and beliefs of the long-gone society`,
            `A mysterious setting of ancient ruins, partially submerged in water, adding an element of intrigue and fascination to the forgotten city`,
            `An awe-inspiring vista of ancient ruins, framed by a dramatic sky and surrounded by an overgrown landscape, evoking a sense of adventure and discovery`,
            `A mesmerizing view of a moonlit lake, where the moon's silvery light dances on the ripples of the water, creating a serene and enchanting atmosphere`,
            `A serene and mystical scene of a moonlit lake, with the moon's gentle glow illuminating the surrounding trees and casting a soft shimmer on the water`,
            `A captivating sight of a moonlit lake, with the moon's reflection appearing like a pathway of light leading to a world of dreams and imagination`,
            `A tranquil and ethereal view of a moonlit lake, with the moon's radiance transforming the water into a magical mirror that captures the night sky's beauty`,
            `A peaceful and enchanting scene of a moonlit lake, with the moon's soft glow casting a serene ambiance that invites contemplation and reflection`,
            `A breathtaking view of a moonlit lake, with the moon hanging low in the night sky, surrounded by stars that twinkle like precious jewels`,
            `A romantic and dreamy setting of a moonlit lake, where the moon's luminous glow creates a magical backdrop for a night of wonder and enchantment`,
            `A mesmerizing and mystical sight of a moonlit lake, with the moon's shimmering light guiding the way for night travelers and dreamers alike`,
            `An evocative scene of a moonlit lake, with the moon's reflection gently swaying with the movement of the water, creating a sense of tranquility and harmony`,
            `A serene and magical view of a moonlit lake, with the moon's radiance casting a soft and ethereal glow on the surrounding landscape, making it feel like a place of enchantment and wonder`,
            `A wondrous sight of a floating island, its lush vegetation and waterfalls defying gravity as it hovers high above the ground, a true marvel of fantasy engineering`,
            `An awe-inspiring view of a floating island, surrounded by wisps of clouds and held aloft by magical forces, offering a glimpse of a world untouched by the laws of physics`,
            `A breathtaking scene of a floating island, adorned with towering trees and mystical architecture, seemingly detached from the earthly realm and beckoning adventurers to explore its mysteries`,
            `A fantastical sight of a floating island, its rocky cliffs and cascading waterfalls creating a surreal and enchanting landscape that defies the laws of nature`,
            `An ethereal view of a floating island, bathed in the soft glow of floating crystals and inhabited by mythical creatures, transporting viewers to a realm of pure imagination`,
            `A captivating glimpse of a floating island, suspended in the sky amidst billowing clouds, inviting wonder and curiosity about the magical forces that keep it aloft`,
            `An otherworldly scene of a floating island, with its vibrant flora and fauna thriving in harmony, untouched by the confines of the ground below`,
            `A dreamlike vision of a floating island, its majestic waterfalls plunging into nothingness, surrounded by a swirling mist that adds an air of mystery to its existence`,
            `A mesmerizing view of a floating island, its ethereal beauty capturing the essence of fantasy and igniting the imagination with possibilities of hidden treasures and ancient wonders`,
            `A surreal sight of a floating island, with its gravity-defying terrain and fantastical architecture, evoking a sense of awe and amazement at the marvels of a fantasy world`,
            `A regal sight of a castle on the hill, its towering spires reaching towards the heavens, a symbol of power and nobility in the fantasy realm`,
            `An imposing view of a castle on the hill, surrounded by a sprawling landscape and a protective moat, standing as a formidable stronghold against any adversary`,
            `A majestic scene of a castle on the hill, its walls adorned with intricate carvings and its flags waving proudly in the breeze, a beacon of authority and honor`,
            `A breathtaking sight of a castle on the hill, silhouetted against the setting sun, radiating an aura of ancient history and royalty`,
            `An enchanting view of a castle on the hill, surrounded by lush gardens and enchanted forests, evoking a sense of magical wonder and medieval charm`,
            `A captivating glimpse of a castle on the hill, its turrets and battlements casting shadows on the surrounding lands, a testament to the valor and legacy of its rulers`,
            `A fantastical scene of a castle on the hill, with its fairy-tale-like architecture and soaring towers, transporting viewers to a world of knights and princesses`,
            `An ethereal sight of a castle on the hill, shrouded in a mystical mist that adds an air of mystery and intrigue to its imposing presence`,
            `A serene view of a castle on the hill, its reflective moat mirroring the grandeur of its architecture, an image that evokes a sense of peace and tranquility in the midst of a fantasy world`,
            `A magical vision of a castle on the hill, with its windows illuminated by the warm glow of candlelight, promising tales of chivalry and adventure within its walls`,
            `A lush and vibrant steamy rainforest, teeming with a kaleidoscope of exotic plants and flowers, and echoing with the calls of colorful birds and monkeys`,
            `An enchanting sight of a steamy rainforest, where misty tendrils rise from the forest floor, creating an ethereal and mysterious atmosphere`,
            `A captivating view of a steamy rainforest, with ancient trees draped in lush green foliage, and a canopy that filters dappled sunlight onto the forest floor`,
            `A magical scene of a steamy rainforest, where bioluminescent creatures light up the dark corners of the forest, and waterfalls cascade down moss-covered cliffs`,
            `An awe-inspiring sight of a steamy rainforest, with towering trees reaching for the sky, and vibrant flowers blooming in a riot of colors beneath their canopy`,
            `An adventurous journey through a steamy rainforest, where hidden pathways lead to secret glades and magical clearings, where mythical creatures may dwell`,
            `A tranquil view of a steamy rainforest, where a gentle mist hangs in the air, and the soothing sounds of running water create a serene and calming ambiance`,
            `A paradise of biodiversity in the steamy rainforest, where rare and unique species of plants and animals thrive in the humid and fertile environment`,
            `A dense and enchanting steamy rainforest, where tree roots form natural bridges over trickling streams, and vines create a tapestry of greenery throughout the forest`,
            `A wild and untamed steamy rainforest, where the air is filled with the scent of earth and foliage, and the undergrowth teems with life and unseen wonders`,
            `A mystical futuristic city, hidden within a pocket dimension accessible only by ancient portals, where time flows differently, and mythical creatures serve as guardians of the city's secrets`,
            `A city of ethereal beauty and wonder, hovering above the clouds on massive levitating platforms, where celestial constellations are intricately woven into the city's architecture`,
            `An enchanted futuristic city nestled within the heart of an ancient forest, where sentient treefolk and mystical creatures coexist, protecting the city with their magical powers`,
            `A futuristic city built around a colossal ancient tree, where its roots serve as the foundation, and the city's inhabitants harness the tree's energy for their technological marvels`,
            `A mesmerizing futuristic city located deep underwater, enclosed within a shimmering energy dome that allows the inhabitants to breathe and thrive beneath the waves`,
            `A steampunk-inspired futuristic city, where clockwork mechanisms and magical steam engines power the city's machines and create an industrial yet magical atmosphere`,
            `A city of floating islands, connected by ornate bridges and airships, where the citizens harness the power of floating crystals to create a harmonious and sustainable society`,
            `A futuristic city built upon the back of a colossal mythic creature, whose every movement influences the city's architecture, creating a living and ever-changing metropolis`,
            `An awe-inspiring futuristic city situated atop ancient and colossal stone pillars, where the city's architects harness the mystical energy of these pillars for their advanced technologies`,
            `A city of dreams and imagination, where the buildings and structures are ever-changing and molded by the collective consciousness of the city's inhabitants, blurring the line between reality and fantasy`,
            `A mesmerizing art piece depicting a celestial realm where floating islands adorned with luminescent flowers and sparkling crystals drift among the stars, guided by the constellations themselves`,
            `An enchanting backdrop featuring an ethereal realm bathed in the light of distant nebulae, where celestial beings with iridescent wings soar gracefully through the cosmic expanse`,
            `A majestic art piece set in a realm of eternal twilight, with silver moons and twinkling stars illuminating vast palaces carved from stardust, where celestial royalty resides`,
            `The Celestial Court portrayed in stunning detail, a realm of divine beings and celestial deities, presiding over the fates of mortals and the harmony of the universe`,
            `A dreamlike painting showcasing a celestial garden, filled with mythical plants and glowing flora, tended to by benevolent celestial spirits who weave the fabric of dreams`,
            `An awe-inspiring art piece depicting the Starlit Observatory, a celestial realm dedicated to the study of the cosmos, where scholars and sages unravel the mysteries of the universe`,
            `A dynamic scene featuring the Celestial Arena, a magnificent battleground where celestial warriors clash in epic duels, their weapons empowered by the very stars`,
            `An art piece showcasing a realm of ever-changing constellations, where celestial artists paint the sky with celestial brushstrokes, crafting new patterns with each stroke`,
            `An ethereal art piece featuring the Silver Labyrinth, a celestial maze where travelers must navigate starlit pathways and solve cosmic riddles to reach its heart, rumored to grant celestial wisdom`,
            `An exquisite painting showcasing the Celestial Library, an immense repository of knowledge located among the stars, holding ancient tomes and celestial scrolls that contain the secrets of the cosmos`,
            `An enchanted forest filled with ancient, moss-covered trees, their branches reaching out like wise guardians of the woodland realm`,
            `A mysterious mist veiling the forest, creating an otherworldly and magical atmosphere, where mythical creatures and fairytale beings roam`,
            `Elaborate runes and symbols etched into the trees and stones, hinting at powerful spells and ancient enchantments that linger in the air`,
            `Delicate glimmers of faerie dust floating through the foliage, illuminating the forest with an ethereal and enchanting glow`,
            `Soft, glowing wisps of elemental energy, dancing amidst the trees, reflecting the harmony between nature and magic in the enchanted forest`,
            `Whispers of enchanting melodies drifting through the air, as if the very sounds of nature are alive with magical harmony`,
            `Ancient tapestries hanging between the branches, depicting mythical creatures and legendary tales, weaving the forest into a realm of wonder`,
            `A shimmering, enchanted pond hidden within the forest, reflecting the stars above and mirroring the beauty of the magical realm`,
            `Luminescent flowers and plants dotting the forest floor, emanating a soft and magical radiance in the moonlight`,
            `A gentle, radiant glow emanating from the heart of the forest, where the source of its enchantment lies, inviting viewers to step into a world of fantasy and wonder`,
            `A labyrinth of mystical caves adorned with bioluminescent crystals, casting a mesmerizing glow on the walls and revealing hidden treasures within`,
            `Delicate veins of shimmering crystals weaving through the cave's walls, like a network of enchanted pathways leading to secret chambers`,
            `Soft, glowing orbs of light floating in the air, illuminating the cave's interior and creating an otherworldly and magical ambiance`,
            `Ancient runes carved into the cave walls, their faint glow hinting at the ancient magic that once thrived within these mysterious depths`,
            `Hidden alcoves filled with enchanted artifacts and valuable gemstones, waiting to be discovered by brave adventurers`,
            `A mystical waterfall cascading down from the cave's ceiling, its waters infused with magical properties, nourishing the cave's thriving ecosystem`,
            `Shadows dancing across the cave walls, hinting at the presence of elusive and magical creatures that call this cave their home`,
            `Glowing crystals suspended from the cave's ceiling, resembling a breathtaking natural chandelier that fills the cave with an ethereal radiance`,
            `Sparkling pools of luminescent water reflecting the cave's enchanting beauty, creating a surreal and captivating scene`,
            `The echoes of ancient incantations still lingering in the air, as if the cave itself holds the secrets to long-forgotten spells and mysteries`,
            `A celestial sky with fluffy clouds forming whimsical shapes like dragons, unicorns, and castles, evoking a sense of wonder and magic`,
            `Pastel-colored clouds drifting lazily across the sky, creating a serene and dreamy backdrop for the main subject of the artwork`,
            `Golden-hued clouds tinged with the light of the setting sun, painting the sky in warm and enchanting tones`,
            `Clouds infused with vibrant colors like pink, purple, and turquoise, as if touched by the magic of a sorcerer's spell`,
            `Celestial beings soaring among the clouds, their ethereal presence adding a sense of mystique and wonder to the scene`,
            `Clouds shaped like fantastical creatures, such as phoenixes, griffins, and mermaids, floating serenely in the boundless sky`,
            `Rays of soft, diffused light breaking through the clouds, creating a heavenly and tranquil atmosphere`,
            `The silhouette of an ancient castle nestled among the clouds, suggesting a hidden kingdom in the skies`,
            `Wisps of enchanting mist intertwining with the clouds, hinting at the presence of mystical beings dwelling in the ethereal realm`,
            `Starry constellations peeking through gaps in the clouds, as if the sky is a portal to the vast unknown of the cosmos`,
            `A volcanic wasteland, with fiery lava rivers flowing through charred and rocky terrain, creating an ominous and dangerous atmosphere`,
            `The peak of a towering volcano spewing molten lava into the sky, painting the horizon in shades of red, orange, and black`,
            `Fiery geysers erupting from the ground, sending plumes of smoke and sparks into the air, adding a sense of chaos and power to the scene`,
            `Cracked and scorched earth, with streams of lava snaking through the desolate landscape, as if the very ground itself is ablaze`,
            `An ancient dragon's lair nestled amidst the fiery landscape, its fiery breath mingling with the lava, suggesting a fearsome and powerful guardian`,
            `Crumbling ruins of a once-mighty civilization, now engulfed by the unstoppable force of volcanic eruptions and lava flows`,
            `Glowing embers floating in the air, illuminating the dark sky and reflecting the intensity of the volcanic activity below`,
            `The silhouette of dark and imposing volcanic mountains against a fiery sky, creating a sense of foreboding and danger`,
            `Fiery phoenixes soaring through the lava-filled sky, symbolizing rebirth and renewal amidst the destructive force of the volcanic landscape`,
            `Ancient runes etched into the volcanic rocks, hinting at forgotten rituals and dark powers that once ruled this fiery realm`,
            `A decrepit mansion, its dilapidated walls covered in creeping vines and the windows glowing with an unnatural pale light from within, giving it an ominous and haunting appearance`,
            `Wisps of ghostly apparitions floating through the mansion's halls, their translucent forms exuding an ethereal and eerie aura`,
            `An overgrown and shadowy garden surrounding the haunted mansion, with twisted trees and eerie mist adding to the foreboding atmosphere`,
            `Moonlight casting eerie shadows on the mansion's exterior, as if the building itself is alive with a haunting presence`,
            `A full moon hanging in the night sky, illuminating the haunted mansion with an eerie glow, while dark clouds gather ominously overhead`,
            `Tattered curtains billowing in the wind through broken windows, giving the mansion a haunted and abandoned feel`,
            `Ancient portraits lining the walls of the mansion, their eyes seemingly following the viewer, adding to the sense of mystery and unease`,
            `Creaking floorboards and the distant echo of haunting whispers, suggesting that the mansion is alive with restless spirits`,
            `Eerie sounds of laughter and music emanating from the mansion, even though no living soul can be seen within, creating an unsettling and ghostly ambience`,
            `Flickering candles casting dancing shadows on the mansion's walls, creating an eerie and macabre scene reminiscent of a haunted tale`,
            `A majestic Spelljammer ship soaring through the astral sea, its sails adorned with magical runes that glimmer with an ethereal light, as it navigates the cosmic expanse between distant planets and stars`,
            `Celestial constellations and ancient sigils decorating the Spelljammer ship's hull, imbuing it with the power to traverse the realms of the unknown`,
            `Nebula clouds swirling in vibrant colors, creating a mesmerizing backdrop as the Spelljammer ship sails through the astral sea, hinting at the mysteries and wonders that lie ahead`,
            `Alien worlds with bizarre landscapes and floating islands in the distance, inviting the viewer to imagine the fantastical realms that can be discovered during the Space Odyssey`,
            `Glimpses of ancient ruins on distant planets, revealing the remnants of forgotten civilizations and ancient magic, adding an air of intrigue and exploration to the cosmic journey`,
            `A cosmic storm of spell-infused energy crackling around the Spelljammer ship, demonstrating the magical prowess and defensive measures it employs to navigate through perilous regions of space`,
            `Celestial beings and extraterrestrial creatures flying alongside the Spelljammer ship, showcasing the diverse and magical inhabitants of the cosmos`,
            `Spacefaring dragons with shimmering scales, soaring majestically through the astral sea, reminding viewers of the powerful and mythical creatures that dwell beyond the confines of a single world`,
            `A cosmic convergence of magical energies, forming a portal to other planes and dimensions, offering a glimpse of the infinite possibilities that await the Spelljammer crew during their interstellar odyssey`,
            `The radiant glow of distant stars and celestial bodies, guiding the Spelljammer ship on its epic voyage through the vastness of space, with the promise of adventure and discovery at every turn`,
            `A City of Towers, rises majestically with its towering spires and sky-scraping buildings adorned with elemental-powered airships floating elegantly amidst the clouds`,
            `An intricate network of lightning rails crisscrosses the city, connecting districts with fast-moving trains powered by bound elementals, showcasing the fusion of arcane magic and steampunk engineering`,
            `Warforged automatons populate the bustling streets, their gears and cogs humming with the energy of artificer-crafted enhancements, adding a touch of magical steampunk wonder to the urban landscape`,
            `The central district of the city is a hub of bustling activity, where extravagant lightning-powered contraptions and enchanted clockwork mechanisms create an atmosphere of technological marvels`,
            `Tall smokestacks release clouds of steam and elemental energy into the air, signifying the pervasive use of elemental boundries to power various machinery across the Steampunk City`,
            `Airships of various shapes and sizes dock at floating platforms, fueled by elemental power sources and crewed by skilled airship pilots known as Sky Captains, adding a sense of adventure and exploration to the cityscape`,
            `The city's clock tower, an engineering marvel, is adorned with intricate gears and glowing crystals that regulate time across the metropolis, displaying the seamless integration of magic and mechanics`,
            `The district of the Artificers' Guild hums with creativity and innovation, as skilled inventors and tinkerers work on crafting marvelous devices, blurring the lines between magic and science`,
            `The City Council convenes in a grand steampunk-style council chamber, where the representatives discuss matters of state while the floor is adorned with intricate magic-infused runes`,
            `Arcane-powered street lamps cast a warm glow on the cobblestone streets, offering glimpses of artificer-designed mechanical automatons patrolling the city for added security and protection`,
            `A surreal and alien landscape stretches as far as the eye can see, with towering crystal formations emitting an otherworldly glow amidst an ever-shifting sea of bioluminescent flora`,
            `Strange and spiky flora dot the surface of the alien terrain, each plant pulsating with vibrant colors and releasing sparkling particles into the atmosphere`,
            `Exotic creatures with iridescent wings soar through the sky, leaving behind streaks of mesmerizing trails as they fly above the alien landscape`,
            `The landscape is dominated by colossal rock formations that seem to defy gravity, their surfaces covered in mysterious runes and symbols left behind by an ancient alien civilization`,
            `Luminescent lakes of unknown liquid shimmer in various shades, reflecting the kaleidoscope of colors from the alien sky above`,
            `Gigantic mushrooms with glowing caps tower over the landscape, their faint hum creating an eerie symphony in the air`,
            `Amidst the alien flora, small floating orbs of light dance and flicker, emitting a gentle hum that adds an ethereal ambiance to the scene`,
            `The sky is a tapestry of vibrant colors, with swirling nebulae and unfamiliar constellations that cast an otherworldly glow over the entire landscape`,
            `Mysterious monoliths rise from the ground, seemingly carved with enigmatic symbols and surrounded by a pulsating energy that hums with unknown power`,
            `Alien ruins peek through the vegetation, their architecture hinting at a civilization far more advanced than anything known in the mortal realm`,
            `A hidden sanctuary amidst the fabric of time, with portals to different historical periods appearing like shimmering doorways leading to diverse and wondrous worlds`,
            `The retreat is nestled in a lush, tranquil valley, where ancient ruins from long-forgotten civilizations coexist with futuristic structures from advanced societies`,
            `Time travelers can be seen strolling through a vibrant marketplace, where traders from different eras exchange exotic goods from past and future realms`,
            `The background showcases a series of floating islands, each representing a different historical period, connected by mystical bridges that traverse the ages`,
            `An ancient library with soaring spires contains vast collections of knowledge, offering the time traveler's refuge to learn from the past, present, and future`,
            `Temporal gardens bloom with flowers from different epochs, displaying a mesmerizing array of colors and shapes that shift with the ebb and flow of time`,
            `The retreat features a celestial observatory where time travelers can witness cosmic phenomena and celestial events from past and future stars`,
            `Majestic clock towers rise from the landscape, ticking in synchrony with the passage of time, symbolizing the constant movement and evolution of history`,
            `Time travelers relax in hot springs that flow from different historical eras, providing rejuvenation and healing from the rigors of their temporal journeys`,
            `A magical hourglass stands at the center of the retreat, its sands shifting and swirling to mark the passage of time across the ages`,
            `The lagoon shimmers under the moonlight, with its waters illuminated by ethereal, bioluminescent organisms, creating a breathtaking display of colors that dance and ripple across the surface`,
            `Ancient ruins surround the lagoon, hinting at a forgotten civilization that once revered the mystical waters and their ability to bestow magical powers upon those who immerse themselves in its depths`,
            `Mythical sea creatures, such as mermaids, water nymphs, and selkies, frolic playfully in the lagoon, adding an air of enchantment and wonder to the scene`,
            `The lagoon is guarded by a majestic sea serpent, whose scales shimmer with the same mesmerizing glow as the waters, keeping watch over its magical domain`,
            `A hidden underwater cave, accessible only through the lagoon, conceals an ancient treasure guarded by a riddle, inviting brave adventurers to solve its mysteries and claim their reward`,
            `The lagoon's shores are adorned with delicate, phosphorescent flowers that bloom only under the light of the moon, filling the air with a sweet and enchanting fragrance`,
            `The lagoon's waters possess the power to reveal glimpses of the past and future to those who gaze upon its surface, offering glimpses of untold stories and secrets of the realm`,
            `An enchanted waterfall flows into the lagoon, cascading with liquid silver and granting those who bathe beneath its spray visions of their deepest desires and wishes`,
            `The lagoon is said to be a gateway to the spirit world, and on certain nights, the barrier between the mortal realm and the ethereal plane becomes thin, allowing spirits and ghosts to walk among the living`,
            `The lagoon is surrounded by a ring of ancient standing stones, each inscribed with ancient runes and symbols that amplify the magical energies emanating from the waters`,
            `Ancient temples rise majestically, their spires reaching towards the heavens, adorned with intricate carvings of mythical creatures and celestial symbols`,
            `Soft, ethereal glows emanate from the temples, casting an enchanting light on the surrounding landscape, creating an aura of mysticism and magic`,
            `The temples stand amidst a lush overgrowth of vibrant plants and foliage, as if nature has reclaimed its sacred space`,
            `Whispers of ancient prayers and rituals seem to linger in the air, carried by gentle winds that sweep through the temple grounds`,
            `Weathered statues of long-forgotten gods stand guard at the temple entrance, their stony faces hinting at the once-great power they represented`,
            `Enigmatic symbols and runic inscriptions adorn the temple walls, their meanings lost to time but radiating an unmistakable air of magic`,
            `The temples are perfectly aligned with the stars, creating an awe-inspiring connection between the earthly and celestial realms`,
            `Stone-carved guardians, once protectors of the sacred grounds, now stand frozen in time, their watchful gazes forever etched in stone`,
            `A subtle shimmering veil of magic envelops the temples, obscuring their true nature and inviting curious adventurers to unveil their secrets`,
            `The temples are mirrored by a serene, ancient pool, reflecting their grandeur and creating a mesmerizing image that blurs the line between reality and fantasy`,
            `The surreal dreamscape is an enchanting tapestry of swirling colors and ethereal mists, giving birth to a realm where reality and fantasy intertwine`,
            `Within the surreal dreamscape, gravity seems to bend to the will of imagination, allowing floating islands and levitating structures to grace the fantastical landscape`,
            `A kaleidoscope of bizarre and wondrous creatures roams freely in the dreamscape, each embodying the essence of magic and otherworldliness`,
            `The dreamscape is a realm of infinite possibilities, where time becomes a mere illusion, and past, present, and future coalesce into a mesmerizing continuum`,
            `As one delves deeper into the dreamscape, ancient symbols and enigmatic runes emerge, hinting at hidden wisdom and arcane secrets`,
            `The dreamscape's abstract forms and shapes dance harmoniously, creating an ever-changing masterpiece that challenges the boundaries of artistic expression`,
            `An aura of mystique envelops the surreal world, beckoning adventurers to embark on a journey of self-discovery and exploration of the subconscious`,
            `Within the dreamscape, dreamlike scenarios unfold, blurring the line between illusion and reality, leaving viewers in a state of awe and bewilderment`,
            `The surreal dreamscape is a playground of the mind, where the laws of nature yield to the whimsical desires of the imagination, producing awe-inspiring phenomena`,
            `Ethereal music fills the air of the dreamscape, its melody resonating with the deepest recesses of the soul, leading travelers on a symphonic odyssey through the magical realm`,
            `The frozen wasteland stretches endlessly, a frigid expanse of ice and snow, where time appears to stand still, preserving the desolation for eternity`,
            `Jagged ice formations rise like ancient sentinels from the frozen ground, their icy spires reaching towards the heavens in a mesmerizing display of frozen beauty`,
            `The wasteland is a hauntingly serene landscape, with a soft, silvery glow cast by the shimmering moonlight reflecting off the icy surface`,
            `Ethereal wisps of frosty mist drift across the frozen wasteland, giving an otherworldly ambiance to the desolate and chilling scenery`,
            `Amidst the frozen wasteland, ancient ruins lay buried beneath layers of snow, hinting at a forgotten civilization lost in the icy embrace of time`,
            `The frozen wasteland is home to elusive and mythical creatures that have adapted to the harsh environment, adding an air of mystery and enchantment`,
            `Crystalline ice caves glisten with an inner light, providing a sanctuary from the biting cold and revealing the untold wonders hidden within the frozen realm`,
            `The frozen wasteland is dominated by an enormous ice fortress, a relic of a bygone era, standing as a silent testament to the indomitable spirit of its creators`,
            `Shimmering auroras dance gracefully across the icy sky, painting the frozen wasteland with hues of green, purple, and blue, evoking a magical and surreal spectacle`,
            `The frozen wasteland seems to hold secrets untold, its silent stillness inviting brave adventurers to explore the chilling mysteries that lie beneath its icy surface`,
            `A majestic floating city nestled among the clouds, with intricate spires and bridges connecting the towering buildings, surrounded by a breathtaking view of the open sky`,
            `A bustling metropolis suspended in the air, where airships dock at majestic docking stations and fantastical creatures soar through the skies`,
            `A sprawling cityscape of floating platforms and levitating structures, adorned with glowing crystals and vibrant banners that flutter in the wind`,
            `A mesmerizing floating city surrounded by celestial orbs, giving it an otherworldly and cosmic ambiance that captivates the imagination`,
            `A colossal citadel that floats serenely among the clouds, protected by magical barriers and guarded by mythical creatures`,
            `A bustling marketplace within the floating city, where traders and adventurers from all corners of the fantasy world gather to exchange goods and stories`,
            `An observatory perched atop a floating tower, offering breathtaking views of the ever-changing sky and the distant lands below`,
            `Floating gardens suspended in the air, adorned with colorful flowers and enchanted plants that thrive in the magical atmosphere`,
            `An enchanting harbor within the floating city, with graceful airships docking and setting sail to distant realms, filled with an aura of adventure`,
            `The regal palace of the floating city, with glistening domes and elegant spires, serving as the seat of power and wisdom in the realm of magic and fantasy`,
            `A desolate cityscape with decaying skyscrapers, crumbling infrastructure, and polluted skies, portraying the bleak aftermath of a technological downfall`,
            `A once-thriving metropolis now reduced to ruins, where remnants of advanced technology lie amidst the desolation, serving as a haunting reminder of a lost civilization`,
            `A dystopian wasteland stretching as far as the eye can see, with abandoned factories, rusted machinery, and overgrown vegetation reclaiming the land`,
            `A post-apocalyptic landscape with twisted metal and shattered buildings, symbolizing the collapse of a once-advanced society`,
            `A grim cityscape with flickering neon lights and holographic advertisements, hinting at the remnants of a technologically advanced but now decaying world`,
            `An ominous and polluted sky filled with dark clouds and smog, reflecting the environmental consequences of technological decay`,
            `A desolate industrial district with broken machinery and polluted rivers, representing the destructive effects of uncontrolled technological advancement`,
            `A hauntingly empty street with holographic projections of long-gone inhabitants, illustrating the isolation and loneliness of a dystopian future`,
            `A wasteland littered with discarded robots and machinery, revealing the remnants of an artificial intelligence uprising that led to societal collapse`,
            `A massive junkyard filled with discarded technology and electronic waste, showcasing the consequences of unchecked technological progress in a dystopian world`,
            `A cosmic canvas adorned with vibrant swirls of nebulae in various hues of pink, purple, and blue, creating a mesmerizing and otherworldly backdrop`,
            `An interstellar voyage through a dense nebula, with glowing gas clouds and sparkling stars illuminating the infinite expanse of deep space`,
            `A breathtaking view of a star cluster nestled within a vast nebula, where distant stars shine through the colorful gases, evoking a sense of wonder and exploration`,
            `A celestial dreamscape with wispy tendrils of nebulae stretching across the canvas, reminiscent of the delicate brushstrokes of an artist's palette`,
            `A cosmic symphony of colors, where shimmering nebulae form an enchanting tapestry, captivating the viewer's imagination and drawing them into the depths of space`,
            `A journey through a celestial storm of swirling gases and cosmic dust, depicting the chaotic yet ethereal beauty of deep space nebulae`,
            `An abstract representation of a nebula, with bold strokes of vibrant colors merging and intertwining to create a visually stunning and otherworldly effect`,
            `A distant galaxy viewed through the veil of a luminous nebula, adding an element of mystery and intrigue to the cosmic scene`,
            `A cosmic ballet of stars and nebulae, where the interplay of light and color creates a mesmerizing dance of celestial bodies`,
            `An immersive view of a space traveler navigating through a vast and ethereal nebula, experiencing the breathtaking beauty and majesty of the cosmos`,
            `A mystical twilight scene with the enchanted castle perched atop a hill, bathed in the soft glow of moonlight and surrounded by an aura of magical energies`,
            `A magical forest backdrop, where ancient trees and whimsical flora embrace the majestic castle, creating an enchanted sanctuary in the heart of nature`,
            `A breathtaking aerial view of the enchanted castle, with floating islands and ethereal clouds adding to the sense of wonder and fantasy`,
            `A starry night sky above the enchanted castle, with constellations forming patterns that seem to tell tales of the realm's ancient history and legends`,
            `An underwater kingdom beneath the castle, where mystical sea creatures and luminescent flora create a surreal and enchanting underwater world`,
            `An enchanted garden with blooming flowers and playful fairies, surrounding the castle and infusing the scene with magic and whimsy`,
            `A vibrant and colorful panorama of the enchanted castle during a grand festival, with fireworks lighting up the sky and filling the air with magic`,
            `A portal in the castle's courtyard, opening to a realm of magic and mystery, beckoning adventurers to embark on daring quests`,
            `An enchanted winter wonderland, with the castle standing tall amidst glistening snow and crystalline ice sculptures, evoking a sense of icy enchantment`,
            `A dreamscape of floating islands, where the enchanted castle hovers above a sea of clouds, creating a surreal and otherworldly atmosphere`,
            `A rugged coastal landscape surrounding the Viking village, with imposing cliffs, crashing waves, and Viking longships docked at the shore`,
            `A misty fjord backdrop, with the Viking village nestled between towering mountains, giving a sense of isolation and adventure`,
            `A snowy winter scene, where the Viking village is covered in a blanket of snow, and villagers gather around a roaring fire for warmth and storytelling`,
            `A fiery sunset over the Viking village, with the sky ablaze in hues of red and orange, setting the backdrop for heroic tales of battles and conquests`,
            `An ancient forest shrouding the Viking village, with towering trees and hidden pathways, evoking a sense of mystery and exploration`,
            `A starlit night sky above the Viking village, with the Northern Lights dancing in the heavens, filling the scene with a mystical and magical ambiance`,
            `A thunderstorm brewing over the Viking village, with lightning flashing in the sky and rain pouring down, adding drama and intensity to the setting`,
            `A serene summer landscape, with lush green fields and meadows surrounding the Viking village, creating a peaceful and idyllic scene`,
            `A mystical aurora borealis illuminating the sky above the Viking village, casting an ethereal glow on the rugged terrain and ancient structures`,
            `A bird's-eye view of the Viking village from a high vantage point, showcasing its strategic location and the surrounding untamed wilderness`,
            `A grand hall filled with towering bookshelves that seem to stretch endlessly into the distance, each shelf holding ancient tomes and scrolls from diverse realms`,
            `A magical glow emanating from the books and manuscripts, casting an ethereal light that bathes the library in a timeless and mystical ambiance`,
            `A central reading area with cozy nooks and comfortable armchairs, inviting visitors to immerse themselves in the knowledge and stories held within the library's vast collection`,
            `Intricate and ornate architecture adorning the library's ceiling and walls, hinting at the wisdom and craftsmanship that went into creating this revered place of learning`,
            `A mystical portal in one corner of the library, suggesting that it holds the knowledge of not only this realm but also of other dimensions and distant worlds`,
            `Enchanted staircases and floating platforms, allowing visitors to access the higher shelves and explore the upper reaches of the library's extensive collection`,
            `Whispers of long-forgotten scholars and sages echoing throughout the library, adding an otherworldly aura to the environment`,
            `Windows looking out onto distant landscapes, each window revealing a different realm, as if the library is a gateway to the vast expanse of knowledge across the multiverse`,
            `Ancient statues and sculptures of mythical creatures and legendary figures that guard the library and symbolize the wisdom and power contained within its walls`,
            `An enormous, mystical book at the center of the library, radiating an aura of ancient magic and believed to hold the most profound secrets of the universe`,
            `A lush and vibrant forest filled with towering ancient trees, their canopies forming a magical canopy that filters sunlight into dappled beams of enchanting light`,
            `A babbling brook winding through the forest, its waters imbued with magic that grants the ability to understand the whispers of the woodland creatures`,
            `Enchanted mushrooms scattered across the forest floor, glowing softly with luminescent colors, leading the way to hidden wonders`,
            `A charming cottage nestled within the woods, home to a friendly witch or kind-hearted wizard who offers assistance to travelers on their fantastical journeys`,
            `A mystical fog that hangs low over the forest, creating an ethereal and mysterious atmosphere, where the boundary between the real world and the magical realm blurs`,
            `Enchanted fireflies dancing through the air, casting a soft, radiant glow that guides adventurers along the forest paths during the twilight hours`,
            `Whimsical flowers that bloom in various fantastical hues, each with unique magical properties, bestowing blessings or curses upon those who interact with them`,
            `Ancient stone ruins overgrown with vines and moss, hinting at a forgotten history where mystical beings once thrived`,
            `A hidden glade where fairies and other mystical creatures come to frolic and celebrate, filling the air with their laughter and joyous music`,
            `A majestic waterfall cascading down a cliffside, its waters said to hold the power to grant wishes to those who bathe in its magical spray`,
            `A grand observatory perched atop a hill, its domed roof housing an array of intricate astronomical instruments, poised to unlock the mysteries of the cosmos`,
            `Celestial maps and star charts adorning the walls of the observatory, revealing the positions of constellations and guiding the way for celestial navigation`,
            `A mesmerizing celestial event unfolding in the night sky, with shooting stars and comet trails painting a breathtaking spectacle of cosmic beauty`,
            `Ancient astronomical texts and manuscripts displayed on ornate bookshelves, containing the wisdom of astronomers and sages from ages past`,
            `A massive telescope extending toward the heavens, its lenses capable of peering into distant galaxies and unexplored cosmic wonders`,
            `Elaborate astrolabes and intricate orreries, mechanical marvels that demonstrate the movements of celestial bodies and the dance of the planets`,
            `A mysterious celestial alignment occurring once in a millennium, where the stars and planets converge to unveil prophetic omens and cosmic revelations`,
            `The observatory's rooftop adorned with mystical symbols and astrological signs, serving as a focal point for harnessing the powers of the celestial bodies`,
            `Astronomers huddled together in deep contemplation, deciphering the secrets of the universe, while gazing through telescopes and recording their celestial observations`,
            `A magical aurora shimmering in the night sky, believed to be the manifestation of celestial energy and the celestial beings' ethereal dance among the stars`,
            `The magnificent Spelljammer space station gliding gracefully through the Phlogiston, its magical sails billowing with arcane energies as it journeys among distant crystal spheres`,
            `A bustling docking bay on the Spelljammer station, with exotic spelljamming ships from various worlds arriving and departing, carrying adventurers and traders from across the multiverse`,
            `The mesmerizing view of a radiant nebula from the observation deck, its vibrant colors and swirling energies creating a surreal and otherworldly backdrop`,
            `Enchanted laboratories within the space station, where master spellcasters and artificers experiment with potent magics and develop innovative spelljamming technologies`,
            `The central chamber of the space station, a meeting place for representatives from different spheres, fostering interplanetary diplomacy and cooperation`,
            `Spelljamming helms powering the station, imbuing it with the ability to traverse the Astral Plane and visit remote crystal spheres filled with unique wonders and civilizations`,
            `A celestial garden within the Spelljammer station, flourishing with plants and creatures from countless worlds, harmonizing in a symphony of magical biodiversity`,
            `Ethereal observatories equipped with divination magic, peering into the Tapestry of Fate to glimpse the paths of celestial bodies and foretell cosmic events`,
            `Thrilling skywalks along the outer hull of the station, allowing adventurous visitors to experience the awe-inspiring beauty of the endless cosmos`,
            `The Spelljammer station's heart, a colossal crystal engine radiating powerful energies, propelling it through the vastness of wildspace and beyond`,
            `A hidden desert oasis, its tranquil waters shimmering under the radiant desert sun, surrounded by lush palm trees and colorful flowers`,
            `A group of mystical creatures, like genies and desert spirits, gathering around the oasis, creating an aura of enchantment and magic`,
            `Ancient ruins nestled near the oasis, hinting at long-lost civilizations and forgotten secrets buried beneath the desert sands`,
            `A majestic sandstorm forming in the distance, its swirling winds contrasting with the serene stillness of the oasis`,
            `An enchanting pool within the oasis, its waters rumored to possess healing properties or grant wishes to those who bathe in them`,
            `Desert nomads and their caravan, seeking refuge at the oasis during their arduous journey across the unforgiving desert`,
            `A mystical creature, like a phoenix or a dragon, perched near the oasis, adding an element of fantasy and wonder to the scene`,
            `The desert night sky above the oasis, filled with twinkling stars and a crescent moon, casting a magical glow over the landscape`,
            `A secret entrance to an underground cavern hidden beneath the oasis, leading to a hidden realm of ancient treasures and magical beings`,
            `Ancient hieroglyphs etched into the rocks surrounding the oasis, depicting stories of desert gods and legendary quests`,
            `A dark and ominous underworld abyss, its depths filled with eerie shadows and mysterious glows, where ancient mythical creatures lurk`,
            `A network of twisted and labyrinthine caves, leading deeper into the abyss, with glowing crystals illuminating the way`,
            `Sinister and imposing statues of mythical creatures, serving as guardians of the underworld and adding an air of foreboding`,
            `A river of glowing lava flowing through the abyss, creating an otherworldly and dangerous atmosphere`,
            `Enormous caverns filled with underground waterfalls, creating a mesmerizing display of magical water cascading into bottomless pools`,
            `Bioluminescent flora and fauna, emitting an ethereal glow that guides travelers through the treacherous paths of the underworld`,
            `An ancient portal hidden within the abyss, said to lead to other realms and dimensions, adding an element of mystery and wonder`,
            `Dark and shadowy passageways adorned with ancient runes and symbols, hinting at powerful magic within the depths`,
            `Glimpses of mythical creatures like gorgons, chimeras, and specters moving through the shadows, creating an eerie and fantastical ambiance`,
            `A massive underground colosseum, where mythical creatures engage in epic battles and contests, watched by spectral audiences`,
            `An enchanting floating garden, nestled among the clouds, with vibrant flowers and lush greenery hanging from aerial platforms`,
            `A cascade of floating islands, each adorned with a unique array of flowers, creating a breathtaking aerial garden landscape`,
            `Hanging bridges connecting floating garden islands, providing a picturesque walkway through the magical and colorful flora`,
            `Graceful waterfalls cascading from above, nurturing the floating gardens with their life-giving waters`,
            `Exotic and fantastical creatures, like winged fairies and ethereal butterflies, adding an element of wonder to the floating garden scene`,
            `Floating orbs of light, casting a soft glow on the gardens and illuminating the night sky, making the scene truly magical`,
            `Ancient ruins integrated into the floating garden structure, hinting at a long-lost civilization that once thrived in the skies`,
            `Whimsical water fountains, spraying sparkling water into the air, creating a playful and enchanting atmosphere`,
            `Airships and hot air balloons passing by, emphasizing the fantastical nature of the floating gardens and the world they inhabit`,
            `Celestial bodies and constellations visible in the background, as if the floating gardens are part of a celestial realm, transcending the boundaries of the earthly realm`,
            `A sprawling magic academy nestled in the heart of a lush enchanted forest, with ancient trees serving as natural classroom walls`,
            `Towering spires and grand architecture make up the Magic Academy's main building, standing tall against a backdrop of mystical skies`,
            `Enchanted waterfalls cascading down the academy's walls, providing a serene and magical ambiance to the surroundings`,
            `Gargoyles and mythical creatures acting as guardians of the Magic Academy, perched atop walls and gates, adding a sense of mystery and protection`,
            `Floating books and scrolls hovering in mid-air, carrying knowledge and magical secrets throughout the academy's libraries and study halls`,
            `Whimsical gardens filled with talking plants and flowers, creating a lively and magical environment for the students to explore`,
            `The night sky above the Magic Academy adorned with sparkling stars and mystical constellations, signifying the limitless potential of magic`,
            `Ethereal creatures like unicorns and phoenixes roaming freely on the academy grounds, offering inspiration and guidance to the young wizards and sorcerers`,
            `Crystal-clear ponds reflecting the magic-infused architecture of the academy, creating a sense of harmony between nature and magic`,
            `A grand magical portal within the academy grounds, hinting at the ability of the students to travel to distant realms and unlock the secrets of the multiverse`,
            `A secluded and mysterious island covered in thick vegetation, concealing ancient ruins and forgotten artifacts`,
            `The Lost Island surrounded by treacherous reefs and swirling mist, deterring explorers and adding an air of mystery`,
            `Crystal-clear waterfalls cascading down lush cliffs, providing a serene and magical atmosphere to the island`,
            `Giant trees with roots intertwining with ancient stone structures, giving the island an aura of ancient wisdom`,
            `Luminescent flora and fauna illuminating the island at night, creating a surreal and otherworldly ambiance`,
            `A network of underground caves and tunnels, concealing hidden chambers and secrets waiting to be discovered`,
            `Statues of mythical creatures scattered throughout the island, hinting at the island's connection to ancient myths and legends`,
            `A magical barrier enveloping the Lost Island, protecting it from outsiders and preserving its untouched beauty`,
            `Floating islands suspended in the sky above the main island, providing a breathtaking view of the surrounding magical landscape`,
            `An ancient temple at the heart of the Lost Island, housing powerful artifacts and guarded by mystical beings, awaiting brave adventurers to unlock its mysteries`,
            `An enchanting lagoon nestled amidst a lush, tropical paradise, with crystal-clear waters reflecting the vibrant colors of the surrounding flora`,
            `Underwater caves and grottos adorned with bioluminescent plants, creating a magical underwater wonderland for mermaids to explore`,
            `Sunlight streaming through the water's surface, casting a mesmerizing dance of light and shadows on the ocean floor of the lagoon`,
            `An underwater coral garden teeming with fantastical sea creatures and vibrant marine life, adding a touch of wonder and enchantment`,
            `Majestic underwater rock formations creating a natural sanctuary for mermaids to gather and create beautiful melodies`,
            `An ancient shipwreck lying at the bottom of the lagoon, becoming a playground for curious mermaids to explore and find hidden treasures`,
            `Pillars of shimmering pearls rising from the lagoon's depths, serving as the mermaids' regal meeting place`,
            `A captivating waterfall flowing into the lagoon from a hidden source, adding a touch of magic and serenity to the surroundings`,
            `Magical seashells scattered along the lagoon's shores, each possessing unique powers and secrets known only to the mermaids`,
            `Moonlit nights where the lagoon glows with an ethereal light, captivating both mermaids and onlookers with its magical allure`,
            `A magnificent castle standing proudly amidst rolling hills and lush gardens, a symbol of regal elegance and timeless beauty`,
            `Ancient stone bridges spanning over gently flowing rivers, connecting various parts of the kingdom and adding a sense of grandeur`,
            `Towering spires and domed rooftops reaching towards the sky, reflecting the architectural marvels of a bygone era`,
            `Lavish ballrooms adorned with intricate chandeliers and opulent decor, where nobles and royalty gather for enchanting evenings`,
            `A majestic fountain at the heart of the kingdom, gushing with sparkling water and surrounded by ornate sculptures`,
            `Elaborate gardens filled with blooming flowers, carefully manicured hedges, and whimsical topiaries, showcasing the kingdom's love for beauty and nature`,
            `Enchanted forests bordering the kingdom, home to mythical creatures and magical beings, adding an air of mystery and wonder`,
            `Ancient ruins scattered around the kingdom, remnants of a rich history filled with tales of heroism and myth`,
            `A magnificent throne room within the castle, adorned with intricate tapestries and murals, where the kingdom's ruler holds court`,
            `Towering mountains in the distance, their snow-capped peaks touching the heavens, guarding the kingdom from the outside world and preserving its timeless charm`,
            `A bustling futuristic cityscape with towering buildings and advanced technology, now overshadowed by the ominous presence of massive alien spacecraft descending from the skies.`,
            `Brilliant streaks of colorful lights and energy beams filling the night sky as the alien ships unleash their powerful weapons upon the city below.`,
            `Swarms of alien fighters and spacecraft engaging in dogfights with the city's defense forces, creating a chaotic and intense aerial battle.`,
            `The city's skyline ablaze with explosions and fire as the invading alien forces lay waste to the once-thriving metropolis.`,
            `Brave Spelljammer pilots soaring through the skies on their own spacecraft, bravely taking on the alien invaders to protect their home.`,
            `Strange and otherworldly creatures emerging from the alien ships, adding an eerie and fantastical element to the chaotic scene.`,
            `The city's inhabitants fleeing in panic and terror, seeking shelter from the onslaught of the alien invasion.`,
            `Spelljammer vessels forming a defensive line against the alien fleet, their cannons blazing with magical energy in an attempt to push back the invaders.`,
            `The sky ablaze with spellfire and alien technology colliding, creating mesmerizing and surreal visuals in the midst of the chaos.`,
            `A glimpse of other planets and celestial bodies in the background, hinting at the vastness of space and the scope of the interstellar conflict.`,
            `A vast underground chamber illuminated by the soft glow of luminous crystals, casting a mesmerizing display of colors across the rocky walls.`,
            `Stalactites and stalagmites adorned with sparkling gemstones, creating a breathtaking spectacle of natural beauty within the caverns.`,
            `Magical runes etched into the walls, adding an air of mysticism to the already enchanting crystal-filled surroundings.`,
            `Subterranean pools of water reflecting the shimmering crystals above, creating a magical mirror-like effect that seems to transport viewers to another world.`,
            `Hidden chambers within the caverns, containing rare and precious crystals that emit an ethereal light, bathing the area in a gentle luminescence.`,
            `Mythical creatures and magical beings dwelling within the depths of the crystal caverns, adding an element of fantasy and wonder to the scene.`,
            `Crystal formations resembling delicate flowers, frozen in time as if a spell had captured their growth for eternity.`,
            `A network of tunnels and passages leading deeper into the heart of the caverns, inviting viewers to explore the unknown and discover hidden treasures.`,
            `Crystal stalactites that hang from the ceiling like chandeliers, creating a surreal and grandiose atmosphere within the underground realm.`,
            `The caverns extending far beyond what the eye can see, with no end in sight, evoking a sense of mystery and limitless possibilities within this magical underground world.`,
            `A fleet of majestic spelljamming ships soaring through the cosmos, with colorful sails billowing in the stellar winds as they explore distant planets and galaxies.`,
            `A cosmic tapestry of stars, nebulas, and swirling galaxies serving as the backdrop for the spelljammers as they venture into the great unknown.`,
            `Celestial phenomena like comet trails and shooting stars streaking across the sky, adding a sense of wonder and adventure to the space odyssey.`,
            `Spelljammer helms and magical engines glowing with arcane energy as they propel the ships through the vastness of space.`,
            `Extraterrestrial worlds with unique landscapes and fantastical creatures, waiting to be discovered and explored by intrepid spelljammers.`,
            `Ancient space ruins and mysterious artifacts floating amidst the void, hinting at the existence of long-lost civilizations and forgotten secrets.`,
            `Cosmic portals and interdimensional rifts, serving as gateways to unexplored realms and alternate planes of existence.`,
            `Spaceborne leviathans and celestial behemoths drifting lazily through the astral sea, creating awe-inspiring encounters for the spelljammers.`,
            `Spelljammer caravans and bustling trading posts nestled within asteroids and spaceborne islands, forming a network of commerce and interaction among the stars.`,
            `A breathtaking view of the radiant Astral Plane, with its vast silver void and luminous motes of light guiding the spelljammers on their extraordinary journey through space and time.`
        ]
    ]
    if (rollDice(100) >80){
        return `Background: ${searchArray(backgroundTemplates[0])}`
    } else {
        return `Background: ${searchArray(backgroundTemplates[1])}`
    }
}


    let holdingLocation =[
        'over their heads', 'at their sides', 'behind their backs', 'held in an outstretched hand', 'cradled in their lap', 'leaning against their body or leaning on an object', 'wrapped in cloth or fabric', 'enveloped by magical energy or aura', 'floating or levitating', 'in their hands', 'clutched in their grasp', 'resting on their palm', 'cradled in their arms', "tucked under their arm", "strapped across their back", "secured in a holster or sheath", "held aloft in victory", "balanced on their shoulder", "draped over their shoulders", "positioned across their knees", "displayed on a raised platform", "mounted on a wall or stand", "encased in a transparent container", "held in the crook of their elbow", "securely gripped in both hands", "held in place by mechanical arms or supports", "resting against their chest", "swathed in a beam of light"
    ]
    const storyTemplate = [
        [
            `${variableEvent(ageDescriptor)+findRace()+' '+ searchArray([`${searchArray(subject[0])}`,`${searchArray(adultGender)}`])+' '+ searchArray([`${searchArray(verb[1])}.`,`${searchArray(verb[0])}.`])} ${variableEvent([ `${background()}`])}`,
            `${searchArray([`${searchArray(monster[rollDice(1)])} ${searchArray(action[0])} ${searchArray(monster[rollDice(1)])}.`,`${searchArray(monster[rollDice(1)])} ${searchArray(action[0])} ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(subject[0])}.`,`${searchArray(monster[rollDice(1)])} ${searchArray(action[0])} ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)}.`,])} ${variableEvent([ `${background()}`])}`,
            `${variableEvent(ageDescriptor)+findRace()+ " "+ searchArray(anyAgeGender)} ${searchArray([`astride a(n) ${searchArray(monster[rollDice(1)])}, holding a(n) ${searchArray(weapons)} in their hand.`, `playing ${searchArray(instruments)} to ${searchArray(many)} ${searchArray(audience)}.`, `kissing a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} on the cheek.`, `with ${searchArray(projectile)}s stuck in their back, protectively holding a small ${searchArray(monster[rollDice(1)])}.`, `with ${searchArray(projectile)}s stuck in their back, protectively holding a tiny ${searchArray(item)}.`, `with ${searchArray(projectile)}s stuck in their back, protectively holding a baby ${findRace()} ${searchArray(youngGender)}.`, `in a loincloth with a ${searchArray(ageDescriptor)} ${searchArray(monster[rollDice(1)])} next to them.`, `holding a large bouquet of flowers in their arms.`,])} ${variableEvent([ `${background()}`])}`,
            `${variableEvent(ageDescriptor)+findRace()+ " "+ searchArray(anyAgeGender)} ${searchArray(verb[1])}. ${variableEvent([ `${background()}`])}`,
            `${variableEvent(adjective,0)}${searchArray(monster[rollDice(1)])} ${searchArray(action[2])}. ${variableEvent([ `${background()}`])}`,
            `${searchArray(monster[rollDice(1)])} ${searchArray(action[2])} with a(n) ${searchArray(item)} ${searchArray(location)}. ${variableEvent([ `${background()}`])}`,
            `${searchArray(monster[rollDice(1)])} ${searchArray(action[2])}.`,
            `${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} raising a ${searchArray(drink)}. ${variableEvent([ `${background()}`])}`,
            `${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} with two ${searchArray(weapons)}s, one ${searchArray(['by each side', `in each ${variableEvent(["raised"])}hand`, "over each shoulder"])}. ${variableEvent([ `${background()}`])}`,
            `${searchArray(monster[rollDice(1)])} with large and intricately detailed ${searchArray(bodyparts)}. ${variableEvent([ `${background()}`])}`,
            `${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} with a sword and shield ${searchArray(['training for battle','playing with friends',`fighting an imposing ${searchArray(monster[rollDice(1)])}`])}.`,
            `${searchArray(monster[rollDice(1)])} on top of (a(n)) ${searchArray(item)} with a ${searchArray(organization)} crest on it.`,
            `${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} pouring a(n) ${searchArray(color)} liquid into a(n) ${searchArray(color)} flask.`,
            `${variableEvent([searchArray(facialExpression),'extremely detailed', 'tough-looking', 'badly beaten and bloodied',searchArray(adjective[0])])} ${variableEvent(ageDescriptor)}${findRace()} ${variableEvent([searchArray(subject[0]), searchArray(anyAgeGender)])}.`,
            `${searchArray(item)} with various birds perched on it. ${variableEvent([ `${background()}`])}`,
            `${searchArray(subject[0])+" on a " + searchArray(mount)}. ${variableEvent([ `${background()}`])}`,
            `${findRace() +' ' + searchArray(['prince','princess','king','queen'])} ${searchArray(['in all of their royal finery','brought low and dragged through the streets','being coronated amongst a host of noble onlookers',])} ${variableEvent([ `${background()}`])}`,
        ],
        [
            `gilded ceremonial ${searchArray(item)} being held by a(n) ${findRace()} ${searchArray(subject[0])}. ${variableEvent([ `${background()}`])}`,
            `crying ${findRace()} ${searchArray(anyAgeGender)} holding a(n) ${searchArray(item)} in their hands. ${variableEvent([ `${background()}`])}`,
            `${variableEvent(time)}map, with the name of ${toWords(2+rollDice(10))}locations on it.`,
            `snake coiled around (a(n)) ${searchArray(item)}. ${variableEvent([ `${background()}`])}`,
            `${searchArray(scene)}, a(n) ${searchArray(monster[rollDice(1)])}, and ${toWords(2+rollDice(4))}humanoid figures ${searchArray(action[1])}. ${variableEvent([ `${background()}`])}`,
            `distraught ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} clutching their chest with one hand and reaching out with the other. ${variableEvent([ `${background()}`])}`,
            `winged ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} in a combat stance with a(n) ${searchArray(item)} in their hand. ${variableEvent([ `${background()}`])}`,
            `seated crying ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} holding a lifeless ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} in their arms. ${variableEvent([ `${background()}`])}`,
            `large group of mostly ${findRace()}s dancing and celebrating around ${searchArray(celebration)}. ${variableEvent([ `${background()}`])}`,
            `${searchArray([`handsome bare chested ${variableEvent(ageDescriptor)}${findRace()} man with ${searchArray(hair)} hair with a(n) ${searchArray(weapons)} in his hand`,`beautiful ${variableEvent(ageDescriptor)}${findRace()} woman with ${searchArray(['long flowing', 'braided', 'buzzed','jewel decorated'])} hair with a(n) ${searchArray(weapons)} in her hand`])} riding a ${searchArray(mount)}. ${variableEvent([ `${background()}`])}`,
            `faceless angelic being holding a(n) ${searchArray(item)}. ${variableEvent([ `${background()}`])}`,
            `${searchArray(size)} ${searchArray(monster[rollDice(1)])} daintily picking up a ${searchArray(item)} from the ground. ${variableEvent([ `${background()}`])}`,
            `${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} playing an ${searchArray(instruments)} with ${toWords(2+rollDice(4))}${searchArray(monster[rollDice(1)])}s looking at them. ${variableEvent([ `${background()}`])}`,
            `${searchArray(facialExpression)} ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} playing chess with a(n) ${searchArray(facialExpression)} ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)}. ${variableEvent([ `${background()}`])}`,
            `group of ${searchArray(['adventurers', `${searchArray(subject[0])}s`])} ${searchArray(['setting off from', 'heading towards', 'in the midst of'])} a ${searchArray(['campsite','village','city','battefield','cave','portal','wasteland'])}. ${variableEvent([ `${background()}`])}`,
            `${findRace()+' '+searchArray(adultGender)} in a ${searchArray(['flattering','relaxed','provocative','commanding'])} pose. ${variableEvent([ `${background()}`])}`,
        ],
        [
            `${searchArray(many)} ${searchArray(monster[rollDice(1)])}s ${searchArray(verb[0])}. ${variableEvent([ `${background()}`])}`,
            `${searchArray(many)} ${searchArray(subject[0])}s holding ${searchArray(tool)}s and ${searchArray(action[1])}. ${variableEvent([ `${background()}`])}`,
            `${searchArray(historicalEvent)}.`,
            `two ${findRace()}s ${searchArray(verb[2])}. ${variableEvent([ `${background()}`])}`,
            `${toWords(5+rollDice(15))}humanoids of various races holding a(n) ${searchArray(item)} ${searchArray(holdingLocation)}. ${variableEvent([ `${background()}`])}`,
            `a schematic of all the planes of existence.`,
            `${toWords(2+rollDice(10))}${searchArray(subject[0])}s looking at (a(n)) ${searchArray(item)} held by the one in the center. ${variableEvent([ `${background()}`])}`,
            `${toWords(2+rollDice(10))}${searchArray(monster[rollDice(1)])}s looking at (a(n)) ${searchArray(item)} on the ground between them. ${variableEvent([ `${background()}`])}`,
            `${searchArray([`a ${searchArray(['trial being held','hero being rewarded','disagreement','battle','vision','celebration',])} in a heavenly court`,`a ${searchArray(['deal being struck','souls being wagered','trial being held','villain being rewarded','disagreement','battle','vision','celebration'])} in a hellish court`,"a desert oasis","an ancient city", 'some ruins', 'the sunset', `a ${searchArray(['beautiful but unfamiliar', 'chaotic and unnerving', 'dark and desroyed', "distant and alien"])} landscape`,])}.`,
        ],
    ]

    //by thought
        //ART
            //Fears
            //Hopes
            //Events
            //Prophecies
            //Values
            //Portraits and important people
            //Satire
            //Dreams
            //Social Norms
            //BEauty and value
            //self expression


    /* @@size@@ @@Quality@@ @@artform@@, @@story@@
        @@story Templates
        @@description subject@@
        @@description subject Verb@@
        @@subject and subject verb@@
        @@subject verb subject@@
        @@object of interest@@
        @@point of interest@@ 
    */


    let combiner = [
        `A(n) ${artPiece()} ${searchArray(thesaurus)} ${stages()}a(n) ${searchArray(storyTemplate[0])}`,
        `A(n) ${artPiece()} ${searchArray(thesaurus)} ${stages()}a(n) ${searchArray(storyTemplate[0])}`,
        `A(n) ${artPiece()} ${searchArray(thesaurus)} ${stages()}a ${searchArray(storyTemplate[1])}`,
        `A(n) ${artPiece()} ${searchArray(thesaurus)} ${stages()}a ${searchArray(storyTemplate[1])}`,
        `A(n) ${artPiece()} ${searchArray(thesaurus)} ${stages()}${searchArray(storyTemplate[2])}`,
        `A(n) ${artPiece()} ${searchArray(thesaurus)} ${stages()}${searchArray(storyTemplate[2])}`,
        `A(n) ${searchArray(artForm[1])} with designs telling that it ${searchArray([`is from an ancient ${findRace()} kingdom`,"is of extraplanar origin","is of modern and local make","is of unknown and alien make"])}.`,
        `A(n) ${variableEvent(['small', 'normal sized','large'])} ${searchArray(material[3])} beaded ${searchArray(['bracelet','necklace','chain'])}, each bead is carved to represent a different ${searchArray(['race','school of magic','monster','plane','divine being','fiendish lord','kingdom','historical moment','historical disaster','tenet of faith'])}.`,
        `A(n) ${variableEvent(['dull','pristine'])} ${searchArray(material[3])} ${searchArray(['coin','bar', 'tablet'])}, stamped with ${searchArray([`the profile of a${searchArray(['n ancient and forgotten god',' god', ' demon', 'n ancient king'])}`, 'a strange symbol', `what looks like a(n) ${searchArray(subject[0])}`, `the face of a(n) ${searchArray(monster[rollDice(1)])}`, `the image of a(n) ${searchArray(item)}`])}.`,
        `${searchArray(artForm[3])}`,
        `${searchArray(artForm[4])}`,
        ]

    printFrom(combiner, 10, "Art")

};
/* Future Art Generator Ideas
"Silver ewer",
"Carved bone statuette",
"Small gold bracelet",
"Cloth-of-gold vestments",
"Black velvet mask stitched with silver thread",
"Copper chalice with silver filigree",
"Pair of engraved bone dice",
"Small mirror set in a painted wooden frame",
"Embroidered silk handkerchief",
"Gold locket with a painted portrait inside"
"Gold ring set with bloodstones",
"Carved ivory statuette",
"Large gold bracelet",
"Silver necklace with a gemstone pendant",
"Bronze crown",
"Silk robe with gold embroidery",
"Large well-made tapestry",
"Brass mug with jade inlay",
"Box of turquoise animal figurines",
"Gold bird cage with electrum filigree"
"Silver chalice set with moonstones",
"Silver-plated steel longsword with jet set in hilt",
"Carved harp of exotic wood with ivory inlay and zircon gems",
"Small gold idol",
"Gold dragon comb set with red garnets as eyes",
"Bottle stopper cork embossed with gold leaf and set with amethysts",
"Ceremonial electrum dagger with a black pearl in the pommel",
"Silver and gold brooch",
"Obsidian statuette with gold fittings and inlay",
"Painted gold war mask"
"Fine gold chain set with a fire opal",
"Old masterpiece painting",
"Embroidered silk and velvet mantle set with numerous moonstones",
"Platinum bracelet set with a sapphire",
"Embroidered glove set with jewel chips",
"Jeweled anklet",
"Gold music box",
"Gold circlet set with four aquamarines",
"Eye patch with a mock eye set in blue sapphire and moonstone",
"A necklace string of small pink pearls"
"Jeweled gold crown",
"Jeweled platinum ring",
"Small gold statuette set with rubies",
"Gold cup set with emeralds",
"Gold jewelry box with platinum filigree",
"Painted gold child's sarcophagus",
"Jade game board with solid gold playing pieces",
"Bejeweled ivory drinking horn with gold filigree"

`An adventuring party setting off from a village for their first adventure. Goblins can be seen peering out of some bushes.`,
`group of ${searchArray(['adventurers', `${searchArray(subject[1])}`])}` 
`${searchArray(['setting off from', 'heading towards', 'in the midst of'])} a ${searchArray(['campsite','village','city','battefield','cave','portal','wasteland'])}`,
`A handsome painting of a local lord or other noble, signed “To my dearest friend ______.”`,
`A cat with wings sitting on a hill licking its paws.`,
`A treent patting a blushing dryad on the head.`,
`A charismatic devil in a suit, sipping wine from a goblet while sitting on a fine chair that itself sits stop a massive pile of gold and jewels.`,
`A ruined city in the middle of a desert. A giant broken crystal hovers above the tallest tower.`,
`${searchArray(['ruined city', 'mountain', 'metropolis'])} ${searchArray(["in the middle of the"])}`,
`A nearly nude female dragonborn, draped in silks and eating grapes on a sofa.`,
`A jeweled sword stuck in a common stone.`,
`A beholder in a top hat whose eyes follow you. But each time you look, it's a different eye.`,
`A man with a flute and a naked female of every other race.`,
`A gnome standing proudly in front of some unidentifiable machine. Perhaps it flies?`,
`The danse macabre: several skeletons, some in rags and some bedecked in finery, dance together. It is a reminder that after death, all bodies, regardless of status, are the same to a necromancer.`,
`A troll intimidating a traveler on his bridge.`,
`A red-faced drunken giant.`,
`A still-life of potions and alchemical supplies.`,
`A solemn saint with a halo of actual enchanted flames.`,
`An archer posing with a dead peryton.`,
`A hero raising their magical spear to the sky in triumph.`,
`A haggard old crone with a crystal ball. The ball contains the painter's reflection, distorted and upside down.`,
`An artifact in a glowing crystal cage.`,
`The prophesied end of the world.`,
`You. The painting is enchanted to depict the viewer.`,
`A mirror depicting the room it is in, devoid of people. A small plaque on the frame titles it "Vampires"`,
`A formal-looking portrait of a headless woman, holding the decapitated head of a man.`,
`A figure sits writing at a desk, surrounded by stacks of books and parchment.`,
`A bunch of poorly-rendered stick figures and...is that a house? And it might be on fire? The only clear thing about this painting is that it was likely done by a child.`,
`Geometric forms that overlap and intertwine, into which you can sort of apply some level of anthropomorphization. That might be a set of eyes, and that might be a mouth, after all.`,
`A coronation scene, with a woman being crowned amidst a court of noble onlookers.`,
`A scientific-looking rendering of a local animal/plant, annotated with biological observations.`,
`An underwater shipwreck, surrounded by murky water and ethereal forms.`,
`An evening sky lit by the aurora.`,
`A bridge spanning a wide river, still in mid-construction.`,
`A formal-looking portrait of a pig and an anteater.`,
`Starry Night with a Nautiloid in the sky`,
`An painting from a remote country. It depicts a magnificent walled city, with a golem in the background that towers over it. The golem bears the symbol of a foreign deity on its chest, representing the god’s role as a guardian of the city.`,
`A golem of Hextor burning a village of elves. Drow army can be seen below helping the Golen -Circa 32 year of present day.`,
`A mated pair of displacer beasts trying to scare off an invading owlbear from their recent kill.`,
`A nature conservationist caring for and trying to nurse a winter wolf back to health.`,
`A day in the life of dwarf miners plying their craft.`,
`A wizard and apprentice(s) discussing magical lore or performing a magical case study.`,
`A portrait of adventuring friends before setting out for the first time.`,
`A portrait of adventuring friends as kids in their neighborhood or perhaps at a fair.`,
`A portrait of adventuring friends surrounded by many/some of their accumulated wealth and accomplishments before one or more of them moved away and/or were killed.`,
`A family portrait of some noble family.`,
`A family portrait of a wealthy merchant's family.`,
`large caravan (entering, leaving) a city.`,
`Ships docket at a large port city.`,
`A portrait of a busy market street with lots of people buying and selling goods.`,
`A brave knight battling a horrible monster. Both are being controlled by puppet strings.`,
`A portrait of an adventuring group that looks like a (younger, older) version of the PCs.`,
`A woman and a bear standing beside one another, they each have matching multi colored eyes.`,
`A pantion of L-G and L-N deities arguing in a court room.`,
`The deity of wisdom lecturing the hungover deity of festivities`,
`A ancient red dragon battling a ancient white dragon.`,
`A wizard being taunted by his lich-like reflection in a mirror.`,
`A nobleman singing a pact with a grinning succubus`,
`A druidic protection ritual performed in a beautiful forest by charming but animal-like people. They have e.g. antlers or wings.`,
`A religious picture about the fight between the good and the evil.`,
`A portrait of a long dead ancestor, with telltale signs of something demonic about them.`,
`A large ship battling a kraken in the middle of a raging storm.`,
`A group of skeletons in a dungeon, peeking around a corner that some unsuspecting adventurers are approaching, planning an ambush.`,
`An idealized painting of famous Wizards at a library discussing principles of magic (Think School of Athens)`,
`A historical gathering of clerics/cultists promoting their faith in a courtyard.`,
`A portrait of a long dead ancestor, with telltale signs of something demonic about them.`,
`large ship battling a kraken in the middle of a raging storm.`,
`Dead nature ( don't know the translation, those training paintings everyone does first to test styles.`,
`Graphite sketches of an ancient, now outdated, dwarven war machine.`,
`A collection of paintings of forest scenes with a red hooded girl and a werewolf:`,
`1st the girl is on the foreground, giving the perspective of natural movement. The creature is on the background, lurking, with vicious intent.`,
`2nd the girl forces through a narrow rock formation giving the impression she will be ambushed at any time.`,
`3rd represents a flung of the werewolf leaping towards the child`,
`4th a darker scene sets a circle of red hooded people facing the werewolf over a stone alter in the forest. It is faintly visible from some angles the form of three greenish tentacles surrounding the altar, and a gaping maw with nightmarish properties.`,
`Satyr peeps through trees and watches the dryads bathe joyesly.`,
`he market of meerkhat, a sensorial confounding painting of a desert based market, with vibrant colours, hundreds of depicted heads ( as in shoppers and sellers) all almost running over each other, and what looks like a parade on a higher road in the background. The looker of the painting makes a DC 13 Wisdom saving throw to resist an urge to go shopping ( either the gift shop at the museum or going to the closest market and going on a spree ).`,
`A group of gnomes or halflings tiptoeing around a sleeping dragon and their hoard`,
`A large army of dark knights being driven away by angels, their awesomely armored leader holding an evil looking great sword being struck in the chest by a spear of light.`,
`A portrait of a striking military leader's top half. Not shown is the bottom half, where the leader is wearing very silly underwear and women's shoes.`,
`A necromancer animating skeletons like puppets to play instruments. One of them is playing a trumpet.`,
`A grand feast being held in a cramped tavern room.`,
`A group of six werewolves playing poker.`,
`A sad dwarf with his ear cut off.`,
`A banshee screaming on a bridge.`,
`A group of gnomes or halflings tiptoeing around a sleeping dragon and their hoard`,
`A pack of gnolls battling a town militia`,
`The Ascension of a cleric into a saint or celestial`,
`A warlock being contacted and accepting a pact with their patron (whichever kind)`,
`A noble knight breaking a liches phylactery`,
`A large army of dark knights being driven away by angels, their awesomely armored leader holding an evil looking great sword being struck in the chest by a spear of light`,
`A trio of giant humanoids carving out mountains from the earth, as a god watches over them.`,
`A Yuan-Ti Pureblood crown found at the site of an unearthed ruin.`,
`Leather gloves, with 4 slots on the knuckles for jewels; to the side, one of the jewels, cracked and faded with color. Rumored to hold the power to cast any magic spell once if all four gems can be seated (one set per glove).`,
`Tools thought to be the earliest concepts for modern Dwarven forging. Among the menagerie is a small anvil, shaped like a Dwarven head, probably used for working with gold.`,
`A painting, on magical parchment, displays an epic magical encounter between former wizards of the realm. This painting's details of the spells are all magically flowing across the parchment, giving the painting the feel that the spells are being cast at the viewer!`,
`A single solitary rune stone found within the core of an ancient tree, recently felled due to some evil force. The rune written on the stone reads "growth".`,
`A green tinged chest-plate, which is a remnant of a ancient society of Dwarven druids.`,
`An ancient cave painting from the early days of the world which depicts a creature of colossal size. Archaeologists have theorized that this might be one of the first artistic depictions of the legendary Tarrasque.`,
`The perfectly preserved corpse of a mindflayer.`,
`The tooth of a Kraken.`,
`A silk dress spun by the spiders of the Feywild.`,
`A sculpture depicting a hypothetical gate to the Nine Hells. It’s been rumored that if the doors on it were opened it would capture and drag those unwary souls to meet eternal damnation. Such rumors are naturally considered unfounded in the greater scientific community but as a precaution the doors are chained shut.`,
`A full suit of armor once worn by a legendary hero.`,
`A collection of old Elven vases, if broken or shattered they unleash a wave of liquid; water, lava, gold, or acid.`,
`A bunch of carved rocks that float of their own violation. They in fact are just levitating via magnetism but the museum curator believes they are magical.`,
`A mummy, in all it's golden regalia on a throne. Must have a sleep spell cast on it or it rises and generally acts like an old forgetful man bothering people.`,
`The very large skull of an unknown creature. It has six eye sockets and dagger sized teeth.`,
`A large rock covered with runes. Otherwise ordinary but a group of cultists have gathered outside the museum chanting 'release our master' ever since the rock arrived.`,
`An obsidian Idol, which scholars believe depicts an ancient Lizardfolk god, whose name is now forgotten.`,
`The perfectly preserved Mask of a Merregon, retrieved from an abandoned Cult site.`,
`A rare example of Derro Art, A statue made of granite, seemingly twisted into curious shapes with magic. Its meaning is subject for speculation .`,
`The Book of Ur: A mysterious manuscript written in an unknown language nobody has been able to decipher in 50 years. Somehow, the book is immune to spells, such as Comprehend Languages. (Either the only source about an ancient secret society or just gibberish).`,
`A dagger carved out of a large opal. Believed to have been used in ceremonies by early tribes in Kara-Tur.`,
`A ceremonial bronze helmet from a Uthgard burial mound. The Uthgard are not happy about that.`,
`The remains of an early gnomish automaton.`,
`A cube made up off interlocking smaller cubelets. It was used as a mental exercise by an ancient group of monks and philosophers.`,
`The ruins of Modron that was severely damaged and shut down during The Great Modron March. If it where to deactivate, it would return to the preset path of that specific march.`,
`A handful of glowing dust-like material from an unknown plane, and is said to be highly poisonous and able to warp flesh. The dying man who brought the strange material spoke only of a place called "Trinity".`,
`An ancient Dwarven rune carving which depicts an ancient disaster. On loan from the clan which carved it until other depictions of the disaster are unearthed and used instead.`,
`A map of a magical moving island.`,
`A large painting of a badly disguised Kobold wizard riding a dragon and throwing lightning bolts.`,
`A small pouch of black sand, rumored to cause any cut the sand touches to infect and cause rot.`,
`An ever-full wine skin, known to never be consumed no matter how much you take from it.`,
`A very old map of an unknown land. You've never seen a map quite like it. It shows an island, or a continent, surrounded by water. But that's only the beginning. Everything is out of proportion: Dots indicate major cities, but these cities are larger than life, each the size of our own Kingdom! And this island is much smaller than our own land!`,
`A single gauntlet, similar to the combat gauntlets of a knight, but with an attachment that allows it to be affixed to the arm.`,
`A small pocketwatch with the power to slow down time for a brief moment, just long enough to get away with something.`,
`A blood-stained journal page, with a poem that speaks of an ancient terror rising.`,
`An onyx and diamond jeweled broach, known to give the user access to the memories of its previous owners for a few moments.`,
`A small ornate music box, covered in demonic faces. When wound it plays a dark and thudding tune that puts those who hear it in a state of hypnosis.`,
`A silver whistle, rumored to summon the beast that was used to make the whistle.`,
`A small wooden box containing several intricate puzzles, each one fitting into another like a puzzle within a puzzle.`,
`A glass bottle containing the glowing essence of lightning.`,
`A glossy obsidian stone, with an eyehole carved in it for looking into a different dimension.`,
`A small, ornate hourglass, holding back the sands of time.`,
`A pipe shaped like a demon's head, with a unique kind of bowl that cools hot tabacs into a pleasant fruit flavor.`,
`A very old and dusty tome, containing the story of a warrior from an age long forgotten.`,
`A golden ring with an embedded ruby that forms the image of a roaring dragon.`,
`A small ornate container of face paint, traditionally used for festivals where the user paints their face to look like the fearsome undead.`,
`A notebook with complex mathematical formulas covering every page.`,
`An album containing several family portraits spanning multiple generations.`
*/


function artEffect() {
    document.getElementById("Effect").innerHTML = ''

    function findRace() {
        var races = {
            "Common": { 'Human': undefined, },
            'Uncommon': { 'Dwarf': undefined, 'High-Elf': undefined, 'Wood-Elf': undefined, 'Gnome': undefined, 'Half-Elf': undefined, 'Halfling': undefined, },
            'Rare': { 'Dragonborn': undefined, 'Tiefling': undefined, 'Genasi': undefined, 'Aasimar': undefined, 'Half-Orc': undefined, 'Tabaxi': undefined, 'Drow': undefined, },
            "Very Rare": { 'Kalashtar': undefined, 'Shifter': undefined, 'Warforged': undefined, 'Simic Hybrid': undefined, 'Changeling': undefined, 'Goliath': undefined, 'Gith': undefined, 'Yuan-Ti': undefined, 'Tortle': undefined, 'Aarakocra': undefined, 'Orc': undefined, },
            'Ultimate Rare': { 'Bugbear': undefined, 'Firbolg': undefined, 'Goblin': undefined, 'Hobgoblin': undefined, 'Kenku': undefined, 'Kobold': undefined, 'Triton': undefined, 'Lizardfolk': undefined, 'Vedalken': undefined, 'Verdan': undefined, 'Locathah': undefined, 'Grung': undefined, 'Centaur': undefined, 'Loxodon': undefined, 'Minotaur': undefined, },
        };
        let chance = rollDice(100)
        if (chance > 98) {
            return searchArray(Object.keys(races["Ultimate Rare"]));
        } else if (chance > 95) {
            return searchArray(Object.keys(races["Very Rare"]));
        } else if (chance > 80) {
            return searchArray(Object.keys(races["Rare"]));
        } else if (chance > 50) {
            return searchArray(Object.keys(races["Uncommon"]));
        } else {
            return searchArray(Object.keys(races["Common"]));
        }
        //document.getElementById("Race").innerHTML = characterRace
    };
    let color = [
        `black`, `pink`, `bordeaux red`, `hazel`, `fire red`, `indigo`, `purple`, `rainbow`, `white`, `lime`, `grey`, `dark green`, `dark brown`, `orange`, `blue`, `yellow`, `gold`, `turquoise`,
    ]
    let genderThree = [
        "men", "women", "boys", "girls"
    ]
    let ifYou = [
        "touch the artwork", `stare at the artwork for ${5+rollDice(15)} minutes`, "damage the artwork"
    ]
    let thenThis = [
        ["you to be overwhelmed with strong emotions, gain advantage on your next roll", `you to be deeply touched, gain one inspiration die (d${searchArray([4,6,8,10,12])})`, "you to be shaken to your core, your next roll is with disadvantage"],
        [`your voice is in a high pitch for ${2*(1+rollDice(12))} minutes`, `your voice is very deep for ${2*(1+rollDice(12))} minutes`, `you find everything hilarious for ${1+rollDice(4)} minutes`, `A flower grows on your head. It does nothing more and can be picked. Now you have a flower.`, `you take ${1+rollDice(4)} poison damage.`, `you are healed for ${1+rollDice(4)} health.`, `you can't sit still for ${1+rollDice(4)} hours.`, `you say everything you think for ${2+rollDice(4)} minutes.`, `you become happy for ${1+rollDice(4)} hours and there is nothing that can make you sad for the duration.`, `you become sad for ${1+rollDice(4)} hours and there is nothing that can make you happy for the duration.`, `all the your hair falls out and grows back over a period of ${2*(1+rollDice(4))} days.`, `if you try to talk you will bark instead for ${2*(1+rollDice(12))} minutes.`, `if you try to talk you will meow instead for ${2*(1+rollDice(12))} minutes.`, `if you try to talk you will roar instead for ${2*(1+rollDice(6))} minutes.`, `you turn into a chicken for ${1+rollDice(4)} minutes.`, `your regain a lvl 1 spell slot. If non caster nothing happens.`, `you become proficient at everything for ${1+rollDice(4)}.`, `you next poop will turn gold.`, `your hair gains ${searchArray(color)} for ${1+rollDice(4)} days. `, `your eyes gain ${searchArray(color)} for ${1+rollDice(4)} days. `, `you become nauseous for the next ${1+rollDice(4)} hours and need to throw up at least twice an hour.`, `you gain ${1+rollDice(6)} temporary hit points for 24 hours.`, `you gain hiccups for ${1+rollDice(4)} hours.`, `you can only lie for ${2*(1+rollDice(12))} minutes.`, `you can only say the truth for ${2*(1+rollDice(12))} minutes.`, `you have diarrhea for ${1+rollDice(4)} hours.`, `you travel 6 seconds (1 round) into the future.`, `your left hand gets an extra ${1+rollDice(4)} fingers for the next 2 hours.`, `your right leg become invisible for ${1+rollDice(4)} hours.`, `you become hyperactive for ${1+rollDice(4)} hours.`, `you see everything as a weapon for ${1+rollDice(4)} minutes.`, `your hand switch with your feet for ${1+rollDice(4)} minutes.`, `your hands switch place for ${1+rollDice(4)} minutes.`, 
        `you gain two left hands for ${1+rollDice(4)} minutes.`, `you need to fart every 6 seconds for ${1+rollDice(4)} minutes.`, `your strength is increased by 2 for ${1+rollDice(4)} hours.`, `your intelligence is increased by 2 for ${1+rollDice(4)} hours.`, `you gains an uncontrollable urge to shake the hand of everyone you comes across for ${1+rollDice(4)} hours.`, `a magical music surrounds you that reflects your mood for ${1+rollDice(4)} hours. (30 feet range)`, `you become blind for ${1+rollDice(4)} hours.`, `you become deaf for ${1+rollDice(4)} hours.`, `you can understand animal speech for ${1+rollDice(4)} hours.`, `you hallucinate for ${1+rollDice(4)} hours.`, `you become highly attractive in the eyes of the opposite gender for 1 day.`, `you become afraid of the opposite gender for ${1+rollDice(4)} hours.`, `every glass/mug of water you touch turns into wine for ${1+rollDice(4)} hours.`, `you grows double in size for 1 day`, `you sparkle in the sunlight for ${1+rollDice(4)} days`, `you are seen as an ally by everyone for ${1+rollDice(4)} hours.`, `if you try to talk you will sing it instead for ${1+rollDice(4)} hours.`, `your skin become acidic to others for ${1+rollDice(4)} hours. If any creature touches you they take ${1+rollDice(4)} acid damage.`, `you will not feel hungry nor need food for ${1+rollDice(4)} days.`, `you can only talk in rhyme for ${1+rollDice(4)} hours.`, `you have hiccups that cause small bursts of fire for ${1+rollDice(4)} minutes. The flames are too small to do any damage unless it is very close to your mouth, at which it will deal 1 fire damage.`, `you say everything twice for ${1+rollDice(4)} hours.`, `you become very horny for the next ${1+rollDice(4)} hours.`, `you turn into a cat for ${3*(1+rollDice(4))} minutes.`, `you turn into a dog for ${3*(1+rollDice(4))} minutes.`, `you leave a magical ${searchArray(color)} trail, that stays for 1 second, with every movement for ${1+rollDice(4)} hours.`, `for ${2+rollDice(4)} minutes every non living object you touch turns ${searchArray(color)} for 2 hours. `, `for ${2+rollDice(10)} rounds everything the user touches goes 6 seconds (1 round) into the future.`, `the first object you touch duplicates. The duplicate stays for ${1+rollDice(4)} hours.`, `${2*(1+rollDice(6))} Small worms crawl out of your nose.`, `you become obsessed with reading for ${1+rollDice(4)} days.`, `you glow in the dark for ${1+rollDice(4)} days. (Emitting dim light 10 foot around the user when its dark)`, 
        `you become paranoia for ${2*(1+rollDice(12))} minutes.`, `you become transparent for ${1+rollDice(4)} hours. (like a ghost or glass)`, `whatever you say, others will believe him/her for ${2*(1+rollDice(4))} minutes.`, `you change sex for ${1+rollDice(4)} days.`, `when you speak, coloured bubbles will come out of your mouth as well for ${1+rollDice(4)} hours. `, `you become very greedy for ${1+rollDice(4)} hours.`, `you will say everything you do out loud for ${1+rollDice(4)} hours.`, `A magical voice calmly narrates everything you do for ${1+rollDice(4)} hours. (30 feet range)`, `A magical voice dramatically narrates everything you do for ${1+rollDice(4)} hours. (30 feet range)`, `you can't sleep the coming long rest and will get one point of exhaustion after the night.`, `increase your max HP by 1`, `you become obsessed with the artwork and will do anything to become the owner of it`, `you must make jokes about everything that is said for ${1+rollDice(4)} hours.`, `you can walk on water for ${1+rollDice(4)} hours`, `your thoughts are written out on your forehead for ${1+rollDice(4)} hours`, `everything you touch stands still in time until you release your touch for ${1+rollDice(4)} hours.`, `a magical voice makes puns about everything you say for ${1+rollDice(4)} hours (30 feet range)`, `everything you eat or drink will taste wonderful for ${1+rollDice(4)} hours`, 
        `everything you eat or drink will taste awful for ${1+rollDice(4)} hours`, `The first thing you say will become real for 1 hour after which it returns to as it was before.`, `you will get lucky with the next thing you do and will have an advantage on your next roll.`, `you will get unlucky with the next thing you do and will have a disadvantage on your next roll.`, `for the next ${1+rollDice(6)} days you will find money in almost every place you come across. (Amount is chosen by the DM)`, `you will insist to sleep on the floor the next long rest.`, `you become colour blind for ${1+rollDice(6)} days`, `you are classified as Undead for ${1+rollDice(4)} days`, `you have to visit the toilet every hour for ${2*(1+rollDice(6))} hours`, `your tongue is forked for ${1+rollDice(4)} hours. (Or not forked if the tongue was already forked)`, `you will stub your toe every instance that it is possible until you have stubbed it for ${3*(1+rollDice(4))} times.`, `you will get a jumpscare of almost anything for ${1+rollDice(4)} hours.`, `A magical voice will say "That's what she said" after every sentence the you say for ${1+rollDice(4)} hours.`, `you will hear all thoughts of people within 10 feet for ${2*(1+rollDice(4))} minutes`, `you will consider the first person that will talks to you as a friend for ${1+rollDice(4)} hours.`, `you turn into a ${findRace()} for ${1+rollDice(12)} hours`, ],
    ]
    let passive = [
        "You notice this artwork attracts cats", "You notice this artwork hums queitly at night.", "You notice this artwork sparkles in the light.", "You notice this artwork sounds like it is whispering something to you.", "You notice this artwok seems to watch you wherever you go.", "You notice that the people and places in this artwork look vaguely familiar.", "You swear it changes a little everytime you look away.", "You notice there are offerings around it like it is being worshipped.", "You notice animals dont come near this artwork.", "You notice this artwork seems to be part of a missing set stolen from your homeland.", "You hear ringing when you get close to it.", `You notice that that only ${findRace()}s can see this artwork.`, `You notice that only ${searchArray(genderThree)} can see this artwork.` 
    ]
    let curse = [
        "The character cannot turn right until the curse is lifted.", "Characters feet always sink at least 1 inch into any surface they walk on (the at least accounts for walking on water, as in if they try to walk on water they sink normally)", "All [food] type becomes tasteless (meat, vegetables, fruit)", "When the character fires a ranged weapon, the ammunition always breaks on impact (no effect on damage)", "Until the curse is lifted, when the character falls to 0hp, roll a D100. If you roll equal to or below the CR of the creature that cursed you, you instantly die.", "A player must close every door they walk through, even if there are people behind them.", "A player's weapon becomes lodged inside the body of their enemy after any stab attack, a strength check (DC 15) is needed to free the weapon.", "A player's weapons become twice as heavy, requiring two actions to strike once, until the curse is lifted.", "A player is stalked by an imp, who simply follows him, saying nothing, always staring. No one else can see the imp.", "The player's backpack is enchanted, to always give the player an item they needed in the past, but never what they will need in the future or present.", "The next item the cursed player grabs is bound to them forever, they can never get rid of it.", "Everytime the cursed character kills someone stealthily, the slain thing lets out an incredibly loud scream that can be heard from 500 ft away, even if it wouldn't be possible for the dead thing to scream.", "Character takes on the appearance and smell of being undead, but isn't.", "Characters must only answer questions with lies, unless they are asked about the reason for their behaviour (ex: 'are you cursed?' 'Are you lying on purpose?') In which case they must respond in the affirmative.", "Characters must agree to every suggestion or request made within 30 feet of them. Curse is broken after a week.", 
        "The cursed character takes 1 damage whenever a creature within 30 feet of them takes any damage.", "Character cannot willingly kill/spare the life of any living creature (choose depending on character personality).", "Character becomes incapable of visually perceiving living creatures.", "Characters low-light vision and high-light vision switch (i.e. sunlight is effectively dark, but can see areas in shadow as if they were brightly lit).", "Roll a d100. After the amount of dies shown on dice, the character explodes for (as per a 5th level Fireball) the next time they take a long rest, then is immediately put under the effects of a Reincarnation spell. The cycle continues until a Wish spell dispels it.", "Character is struck with blindness, but can accurately identify objects by taste through the air up to 60 feet away.", "Butt switches place with face. Switches every time either orifice expels any substance.", "Your CHA stat becomes your CHAR stat, determining your effectiveness at cooking up a mean barbeque. Reflavour spells and skill checks accordingly.", 
        "When the target of the curse next goes to sleep, they dream of a burning lake. The dreams progress, becoming nightmares over time. The target instinctively becomes aware of the direction of the lake, and must save vs Wis or spend that day trying to reach the lake. The target must save every day to prevent the condition progressing, taking a penalty to mental rolls for every stage it advances. To completely recover, the target must make 3 saves in a row, if they fail a save it regresses to its initial condition, and if they fail 3 times in a row the target becomes maddened until they reach the lake. Upon reaching the lake they will see it is not engulfed in flames, and will take d6 Psychic damage for the number of days they have been affected by the urges.", "The first ritual performed after being cursed succeeds instantly, but when they next sleep the target must save vs. Con. If they fail, their skin dries and their body catches alight, taking d6 damage per turn. The fire can be put out by magical or mundane conventions.", "The cursed begins aging at 5 years an hour. When they reach 100 years, they die, and an infant crawls from their body’s clothing. It continues to age at the same rate until it reaches 20. Same character, same memories.", "As the curse is activated, the target's hands detach from their wrists and scuttle away, and new hands grow in their place. For the rest of the day, every time they cast a spell, the same thing happens. The hands remain animate until destroyed, and will do their best to make terrible mischief.", "A thunderous voice narrates everything the cursed does, says, or thinks for the next d4 hours.", 
        "For the next d4 days, every time the cursed attempts to speak, including to cast a spell, they must Save vs Int or instead deliver a lengthy and discursive monologue on: 1: bean cultivation; 2: the daily schedule of an emperor who died thousands of years ago; 3: the spiritual beliefs of spiders; 4: the life cycle of the cherub; 5: the various manias, phobias, or perversions of the nearest, most powerful monarch; 6: the correct method of preparing, storing, and administering a heretofore unknown and spectacularly deadly poison; 7: the best tourist destinations in the nearest village; 8: famous fish poets; 9: the dangers of breathing; 10: the magical properties of cheese; On a repeated roll, the target must continue their lecture from where they left off before.", "Until the curse is lifted the character constantly sniffs and has a runny nose. Disadvantage on stealth, persuasion and deception checks.", "Character can not control the volume at which he speaks. Player rolls a D6 every time their character speaks, even rolls are spoken in a whisper, odd rolls are shouting.", "Animals and children are always aware of your presence and are able to locate you without difficulty.", "'Curse of Popularity' - In populated area with non-hostile NPCs, everyone knows who you are and will not leave you alone. Roll a charisma check/save (DC varies). If failed, you are viewed in an unfavorable light. If passed, you are viewed in a favorable one.", "Everytime a player deals damage the same amount is reflected back to a random party member.", "All food and drink consumed immediately tastes of rotten flesh a successful fortitude save of DC 15 can overcome this taste.", 
        "Whenever the PC comes into a hallway/corridor they are compelled to Sprint at full speed to the end. Will save to resist at DMs discretion.", "The PC must only speak in rhyme.", "The PC gains a new fear based on popular vote of the party until dispelled.", "All the player's equipment glows brightly for 24 hours. All of it.", "The player becomes magnetic.", "It is always raining in a 5ft cube around the player. The intensity randomly varies from a drizzle to a downpour and can exist even underwater or indoors.", "The character finds themselves unable to open any containers or doors which require a twisting motion.", 
        "The character perceives traps everywhere where none exist.", "The cursed becomes lactose intolerant. Consuming any dairy leads to 1d4 hour(s) of insufferable gas & diarrhea.", "The player must compulsively juggle items any time the player has two or more of an object in easy reach. DC 10+the number of items being juggled Acrobatics check, or an item gets dropped, with appropriate consequences.", "Boots squeak loudly with each step.", "Effects of alcohol are heavily amplified, so that even drinking one drop of a fairly weak alcoholic beverage will make the PC drunk. Drinking a full glass of a strong alcoholic beverage could potentially cause death.", "All of the PC's armor and clothing teleported off their body and always floats just out of reach. Any attempt to put on other clothing or armor produces the same effect.", "Character's known languages are randomly determined after a long rest. Roll 1d8 per standard language known & 1d8 per exotic language known. You decide whether to exclude common from these rolls or not.", "After a long rest a random amount of GP the character is carrying is randomly changed to an amount of either Electrum, Silver or Copper pieces of the same worth, increasing number of coins. eg. (1d20 Amount, Roll 1d6 to determine type) Won't take long for pockets to become overflowing if character doesn't spend loose change.", "Any divination spells where the caster or target is within a certain range of a character are retargeted to that character.", "The cursed begins to weep tears of blood uncontrollably, reducing their hit point maximum by 1 for every hour the curse remains active. The cursed dies if this effect reduces its hit point maximum to 0.", 
        "The cursed is compelled to repeat the last word of each sentence they say 3 times, each time speaking a little bit softer than the last. If the curse remains active for more than 24 hours, the cursed is compelled to dramatically flick their hands open and closed with each echo.", "Cursed characters are hated by all cats until cured. Every cat will hiss and attempt to swipe and bite the character. Irregardless of the cat is successful or not the cat will run away and hide. If the cat is successful in the attack any wounds caused will not heal (even with healing spells and potions) and will continuously weep foul smelling pus.", "The character cannot be convinced by any means that magic exists. They rationalize magical events away by using insane, impossible logic.", "The character believes themselves to have swapped bodies with the nearest person. Nothing has happened.", "One of the character's limbs no longer has any bones. It flops around uselessly until the bones have successfully regrown in 1d4 days.", "The character is unable to sleep when others are sleeping in a 60' radius.", "Once the character has fallen asleep they cannot be awoken by any non-magical means until 8 hours have passed.", "The character must consume 1d4+1 times the amount of food and drink a normal person does do sustain themselves. They experience terrible thirst and hunger pains. Treat as exhaustion if they do not actively maintain this regimen.", "The character cannot see anyone within 10 feet of them.", "The character finds a wooden spoon in their bag. Every time they retrieve an item they find another wooden spoon. Every time they investigate an area they find another wooden spoon. Every time the search a body they find another wooden spoon. If they intentionally attempt to locate, retrieve, or use a spoon the task is impossible.", "Incapable of ignoring direct orders given to their person.", "When splashed with cold water transforms the character into the opposite gender. Warm water temporarily reverses the transition.", "Must make one significant lie per day.", "Automatically fails all swimming checks; it's as if the character weights 10 times their normal weight while in water.", 
        "Turned into a lycanthrope... with the form of a rabbit.", "All creatures of a specific species are invisible to the character.", "A perpetually magical darkness surrounds the character for 25 feet. It is transmittable by touch.", "When killed for the first time each day, the wounds heal and they instead stabilize. If they are not killed once a day, they are permanently slain.", "Makes an unarmed attack against themselves whenever they say 'what'.", "Characters ears and eyes switch place. PC cannot look straight ahead. This lasts until the next full day ends.", "PC summons a little foot tall naked man with a hat that goofs around and makes as much noise as possible. Everyone can hear him and see his impact in the area, but cannot see him. He has no name and will not speak back. He just speaks in sounds and screams.", "PC thinks their eyes have the same effect as a beholder and use them as much as possible in combat.", "PCs teeth are as weak as glass.", "PCs weapon changes to the next material they touch.", "PC is followed by all bugs within 20 yards. (Bonus points if there are ant hills around).", "PC grows a mouth in their chest. You can feed the mouth but you do not know what it will do. Overtime the mouth will grow if unfed.", "PCs money all goes down a material (gold turns to silver) until curse is lifted. Copper turns into wooden toy coins that children would play with.", "All plants the PC touches turn to dust for the next week. (Bonus points if a druid gets this)", "All potions being held by PC give a delusion effect (example: PC thinks they are invisible but are not.)", "All damage given to the PC for the next 12 minutes are irreversible.", "The next person the PC touches switches all items.", 
        "PC's armor or clothing (whichever applicable) is made entirely out of shards of glass magically held together.", "Character must kill one humanoid per week or die themselves.", "Character must read one book per week or die, it must be a book they have not read before.", "Every dawn, gravity reverses for the character for one hour.", "Whenever the character physically harms another sentient being the character must apologize.", "Whenever the character is on a sea vehicle of any kind the character vomits anything he/she eats and cannot sleep.", "The PCs hand's tense up, and are stuck in a fist until the curse is removed.", "The character's left and right hands, and/or left and right feet switch sides until the curse is lifted.", "This curse hardens all food this character tries to eat like stone, unless they have the correct eating utensil to eat it. (ie They need a spoon to eat soup, a fork to eat pie, a knife to cut meat, etc).", "The player believes that their mentor/parent has just died.", "The player receives at least one false vision from their deity a day.", "The cursed player can no longer fail the expectations of those they come across. (For example, if an NPC learns the player's name and they believe their name to be elfish, they will become an elf. If they expect that he is a weakling due to rumors they have heard of him losing an important fight, the player looses some of his strength. If they thought he would be taller, the character would become taller, etc...)", "The player is cursed to look down at the ground; they can no longer make eye contact with others, unless they are able to look down on them...", "Until this player's curse is lifted, as long as they wear shoes/boots, they will feel as if their feet are walking on burning hot coals.", "This player has been cursed to be afraid of the sun.", "This curse makes the player compelled to hug all characters they come across, even if it would be inappropriate or awkward.", "This curse makes the character forcibly say gibberish every time they cast a spell.",
    ]

    let effectArray = [variableEffect(ifYou, thenThis, passive, curse), variableEffect(ifYou, thenThis, passive, curse), variableEffect(ifYou, thenThis, passive, curse), variableEffect(ifYou, thenThis, passive, curse), variableEffect(ifYou, thenThis, passive, curse), ]
    printFrom(effectArray, 5, "Effect")
};
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
    document.getElementById("AlternateReward").innerHTML = ""
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
    let magicItemsI = [`Spell scroll (7thlevel) ${searchArray(seventh)}`, `Spell scroll (8thlevel) ${searchArray(eighth)}`, `Spell scroll (9th level) ${searchArray(ninth)}`, "Defender", "Hammer of thunderbolts", "Luck Blade", "Sword of answering", "Holy avenger", "Ring of djinni summoning", "Ring of invisibility", "Ring of spell turning", "Rod of lordly might", "Vorpal sword", "Belt of cloud giant strength", "Armor, +2 breastplate", "Armor, +3 chain mail", "Armor, +3 chain shirt", "Cloak of invisibility", "Crystal ball (legendary version)", "Armor, + 1 half plate", "Iron flask", "Armor, +3 leather", "Armor, +1 plate", "Robe of the archmagi", "Rod of resurrection", "Armor, +1 scale mail", "Scarab of protection", "Armor, +2 splint", "Armor, +2 studded leather", "Well of many worlds", "Armor, +2 half plate", "Armor, +2 plate", "Armor, +3 studded leather", "Armor, +3 breastplate", "Armor, +3 splint", "Armor, +3 half plate", "Armor, +3 plate", "Apparatus of Kwalish", "Armor of invulnerability", "Belt of storm giant strength", "Cubic gate", "Deck of many things", "Efreeti chain", "Armor of resistance (half plate)", "Horn of Valhalla (iron)", "Instrument of the bards (OIIamh harp)", "loun stone (greater absorption)", "loun stone (mastery)", "loun stone (regeneration)", "Plate armor of etherealness", "Plate armor of resistance", "Ring of air elemental command", "Ring of earthelemental command", "Ring of fire elemental command", "Ring of three wishes", "Ring of water elemental command", "Sphere of annihilation", "Talisman of pure good", "Talisman of the sphere", "Talisman of ultimate evil", "Tome of the stilled tongue"]
    let gemsA = ["Azurite (opaque mottled deep blue)(10gp)", "Banded agate (translucent striped brown, blue, white, or red)(10gp)", "Blue quartz (transparent pale blue)(10gp)", "Eye agate (translucent circles of gray, white, brown, blue, or green)(10gp)", "Hematite (opaque gray-black)(10gp)", "Lapis lazuli (opaque light and dark blue with yellow flecks)(10gp)", "Malachite (opaque striated light and dark green)(10gp)", "Moss agate (translucent pink or yellow-white with mossy gray or green markings)(10gp)", "Obsidian (opaque black)(10gp)", "Rhodochrosite (opaque light pink)(10gp)", "Turquoise (opaque light blue-green)(10gp)", "Tiger eye (translucent brown with golden center)(10gp)"]
    let gemsB = ["Bloodstone (opaque dark gray with red flecks)(50gp)", "Carnelian (opaque orange to red-brown)(50gp)", "Chalcedony (opaque white)(50gp)", "Chrysoprase (translucent green)(50gp)", "Citrine (transparent pale yellow-brown)(50gp)", "Jasper (opaque blue, black, or brown)(50gp)", "Moonstone (translucent white with pale blue glow)(50gp)", "Quartz (transparent white, smoky gray, or yellow)(50gp)", "Sardonyx (opaque bands of red and white)(50gp)", "Zircon (transparent pale blue-green)(50gp)", "Onyx (opaque bands of black and white, or pure black or white)(50gp)", "Star rose quartz (translucent rosy stone with white star-shaped center)(50gp)"]
    let gemsC = ["Alexandrite (transparent dark green)(500gp)", "Aquamarine (transparent pale blue-green)(500gp)", "Black pearl (opaque pure black)(500gp)", "Blue spinel (transparent deep blue)(500gp)", "Peridot (transparent rich olive green)(500gp)", "Topaz (transparent golden yellow)(500gp)"]
    let gemsD = ["Black opal (translucent dark green with black mottling and golden flecks)(1000gp)", "Blue sapphire (transparent blue-white to medium blue)(1000gp)", "Emerald (transparent deep bright green)(1000gp)", "Fire opal (translucent fiery red)(1000gp)", "Opal (translucent pale blue with green and golden mottling)(1000gp)", "Star ruby (translucent ruby with white star-shaped center)(1000gp)", "Star sapphire (translucent blue sapphire with white star-shaped center)(1000gp)", "Yellow sapphire (transparent fiery yellow or yellow green)(1000gp)"]
    let gemsE = ["Black sapphire (translucent lustrous black with glowing highlights)(5000gp)", "Diamond (transparent blue-white, canary, pink, brown, or blue)(5000gp)", "Jacinth (transparent fiery orange)(5000gp)", "Ruby (transparent clear red to deep crimson)(5000gp)"]
    let artA = ["Silver ewer(25gp)", "Carved bone statuette(25gp)", "Small gold bracelet(25gp)", "Cloth-of-gold vestments(25gp)", "Black velvet mask stitched with silver thread(25gp)", "Copper chalice with silver filigree(25gp)", "Pair of engraved bone dice(25gp)", "Small mirror set in a painted wooden frame(25gp)", "Embroidered silk handkerchief(25gp)", "Gold locket with a painted portrait inside(25gp)"]
    let artB = ["Gold ring set with bloodstones(250gp)", "Carved ivory statuette(250gp)", "Large gold bracelet(250gp)", "Silver necklace with a gemstone pendant(250gp)", "Bronze crown(250gp)", "Silk robe with gold embroidery(250gp)", "Large well-made tapestry(250gp)", "Brass mug with jade inlay(250gp)", "Box of turquoise animal figurines(250gp)", "Gold bird cage with electrum filigree(250gp)"]
    let artC = ["Silver chalice set with moonstones(750gp)", "Silver-plated steel longsword with jet set in hilt(750gp)", "Carved harp of exotic wood with ivory inlay and zircon gems(750gp)", "Small gold idol(750gp)", "Gold dragon comb set with red garnets as eyes(750gp)", "Bottle stopper cork embossed with gold leaf and set with amethysts(750gp)", "Ceremonial electrum dagger with a black pearl in the pommel(750gp)", "Silver and gold brooch(750gp)", "Obsidian statuette with gold fittings and inlay(750gp)", "Painted gold war mask(750gp)"]
    let artD = ["Fine gold chain set with a fire opal(2500gp)", "Old masterpiece painting(2500gp)", "Embroidered silk and velvet mantle set with numerous moonstones(2500gp)", "Platinum bracelet set with a sapphire(2500gp)", "Embroidered glove set with jewel chips(2500gp)", "Jeweled anklet(2500gp)", "Gold music box(2500gp)", "Gold circlet set with four aquamarines(2500gp)", "Eye patch with a mock eye set in blue sapphire and moonstone(2500gp)", "A necklace string of small pink pearls(2500gp)"]
    let artE = ["Jeweled gold crown(7500gp)", "Jeweled platinum ring(7500gp)", "Small gold statuette set with rubies(7500gp)", "Gold cup set with emeralds(7500gp)", "Gold jewelry box with platinum filigree(7500gp)", "Painted gold child's sarcophagus(7500gp)", "Jade game board with solid gold playing pieces(7500gp)", "Bejeweled ivory drinking horn with gold filigree(7500gp)"]

    if (level === 1) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 2)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsA))
            art.push(searchArray(artA))
            loot.push(searchArray(magicItemsA))
        }
        loopCountPushGems(gems, loot, (fights * 10))
        loopCountPushArt(art, loot, (fights * 25))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 2) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 2)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsA))
            gems.push(searchArray(gemsA))
            art.push(searchArray(artA))
            loot.push(searchArray(magicItemsA))
        }
        loopCountPushGems(gems, loot, (fights * 20))
        loopCountPushArt(art, loot, (fights * 25))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 3) {
        let loot = []
        let art = []
        let gems = []
        let x = Math.floor(1 + fights / 2)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsA))
            gems.push(searchArray(gemsA))
            art.push(searchArray(artA))
            art.push(searchArray(artA))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsA))
        }
        loopCountPushGems(gems, loot, (fights * 20))
        loopCountPushArt(art, loot, (fights * 50))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 4) {
        let loot = []
        let art = []
        let gems = []
        let x = Math.floor(1 + fights / 2)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsA))
            gems.push(searchArray(gemsA))
            art.push(searchArray(artA))
            art.push(searchArray(artA))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsA))
        }
        loopCountPushGems(gems, loot, (fights * 20))
        loopCountPushArt(art, loot, (fights * 50))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 5) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 4)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsA))
            gems.push(searchArray(gemsB))
            art.push(searchArray(artA))
            art.push(searchArray(artB))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsB))
        }
        loopCountPushGems(gems, loot, (fights * 60))
        loopCountPushArt(art, loot, (fights * 275))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 6) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 4)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsA))
            gems.push(searchArray(gemsB))
            art.push(searchArray(artA))
            art.push(searchArray(artB))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsB))
            loot.push(searchArray(magicItemsB))
        }
        loopCountPushGems(gems, loot, (fights * 60))
        loopCountPushArt(art, loot, (fights * 275))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 7) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 4)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsB))
            gems.push(searchArray(gemsB))
            art.push(searchArray(artA))
            art.push(searchArray(artB))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsB))
        }
        loopCountPushGems(gems, loot, (fights * 100))
        loopCountPushArt(art, loot, (fights * 275))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 8) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 4)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsB))
            gems.push(searchArray(gemsB))
            art.push(searchArray(artB))
            art.push(searchArray(artB))
            loot.push(searchArray(magicItemsA))
            loot.push(searchArray(magicItemsB))
            loot.push(searchArray(magicItemsB))
        }
        loopCountPushGems(gems, loot, (fights * 100))
        loopCountPushArt(art, loot, (fights * 500))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 9) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 4)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsB))
            gems.push(searchArray(gemsB))
            art.push(searchArray(artB))
            art.push(searchArray(artB))
            loot.push(searchArray(magicItemsB))
            loot.push(searchArray(magicItemsB))
            loot.push(searchArray(magicItemsB))
        }
        loopCountPushGems(gems, loot, (fights * 100))
        loopCountPushArt(art, loot, (fights * 500))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 10) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 6)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsB))
            gems.push(searchArray(gemsB))
            art.push(searchArray(artB))
            art.push(searchArray(artB))
            loot.push(searchArray(magicItemsB))
            loot.push(searchArray(magicItemsB))
            loot.push(searchArray(magicItemsC))
        }
        loopCountPushGems(gems, loot, (fights * 100))
        loopCountPushArt(art, loot, (fights * 500))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 11) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 6)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsB))
            gems.push(searchArray(gemsC))
            art.push(searchArray(artB))
            art.push(searchArray(artC))
            loot.push(searchArray(magicItemsB))
            loot.push(searchArray(magicItemsC))
            loot.push(searchArray(magicItemsC))
        }
        loopCountPushGems(gems, loot, (fights * 550))
        loopCountPushArt(art, loot, (fights * 1000))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 12) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 6)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsC))
            gems.push(searchArray(gemsC))
            art.push(searchArray(artC))
            art.push(searchArray(artC))
            loot.push(searchArray(magicItemsC))
            loot.push(searchArray(magicItemsC))
            loot.push(searchArray(magicItemsC))
        }
        loopCountPushGems(gems, loot, (fights * 1000))
        loopCountPushArt(art, loot, (fights * 1500))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 13) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 6)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsC))
            gems.push(searchArray(gemsC))
            art.push(searchArray(artC))
            art.push(searchArray(artC))
            loot.push(searchArray(magicItemsC))
            loot.push(searchArray(magicItemsC))
            loot.push(searchArray(magicItemsD))
        }
        loopCountPushGems(gems, loot, (fights * 1000))
        loopCountPushArt(art, loot, (fights * 1500))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 14) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 6)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsC))
            gems.push(searchArray(gemsD))
            art.push(searchArray(artC))
            art.push(searchArray(artD))
            loot.push(searchArray(magicItemsC))
            loot.push(searchArray(magicItemsD))
            loot.push(searchArray(magicItemsD))
        }
        loopCountPushGems(gems, loot, (fights * 1500))
        loopCountPushArt(art, loot, (fights * 3250))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 15) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 6)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsD))
            gems.push(searchArray(gemsD))
            art.push(searchArray(artD))
            art.push(searchArray(artD))
            loot.push(searchArray(magicItemsD))
            loot.push(searchArray(magicItemsD))
            loot.push(searchArray(magicItemsD))
        }
        loopCountPushGems(gems, loot, (fights * 2000))
        loopCountPushArt(art, loot, (fights * 5000))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 16) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 8)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsD))
            gems.push(searchArray(gemsD))
            art.push(searchArray(artD))
            art.push(searchArray(artD))
            loot.push(searchArray(magicItemsD))
            loot.push(searchArray(magicItemsD))
            loot.push(searchArray(magicItemsE))
        }
        loopCountPushGems(gems, loot, (fights * 2000))
        loopCountPushArt(art, loot, (fights * 5000))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 17) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 8)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsD))
            gems.push(searchArray(gemsE))
            art.push(searchArray(artD))
            art.push(searchArray(artE))
            loot.push(searchArray(magicItemsD))
            loot.push(searchArray(magicItemsE))
            loot.push(searchArray(magicItemsE))
        }
        loopCountPushGems(gems, loot, (fights * 6000))
        loopCountPushArt(art, loot, (fights * 10000))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 18) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 8)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsD))
            gems.push(searchArray(gemsE))
            art.push(searchArray(artD))
            art.push(searchArray(artE))
            loot.push(searchArray(magicItemsE))
            loot.push(searchArray(magicItemsF))
            loot.push(searchArray(magicItemsG))
        }
        loopCountPushGems(gems, loot, (fights * 6000))
        loopCountPushArt(art, loot, (fights * 10000))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 19) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 8)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsD))
            gems.push(searchArray(gemsE))
            art.push(searchArray(artD))
            art.push(searchArray(artE))
            loot.push(searchArray(magicItemsF))
            loot.push(searchArray(magicItemsG))
            loot.push(searchArray(magicItemsH))
        }
        loopCountPushGems(gems, loot, (fights * 6000))
        loopCountPushArt(art, loot, (fights * 10000))
        loopCountPrintList(loot, "AlternateReward")
    } else if (level === 20) {
        let loot = []
        let gems = []
        let art = []
        let x = Math.floor(1 + fights / 8)
        for (i = 0; i < x; i++) {
            gems.push(searchArray(gemsD))
            gems.push(searchArray(gemsE))
            art.push(searchArray(artD))
            art.push(searchArray(artE))
            loot.push(searchArray(magicItemsG))
            loot.push(searchArray(magicItemsH))
            loot.push(searchArray(magicItemsI))
        }
        loopCountPushGems(gems, loot, (fights * 6000))
        loopCountPushArt(art, loot, (fights * 10000))
        loopCountPrintList(loot, "AlternateReward")
    }
};


let gems = [
    /*Tier 1 10gp*/["Azurite (opaque mottled deep blue)(10gp)", "Banded agate (translucent striped brown, blue, white, or red)(10gp)", "Blue quartz (transparent pale blue)(10gp)", "Eye agate (translucent circles of gray, white, brown, blue, or green)(10gp)", "Hematite (opaque gray-black)(10gp)", "Lapis lazuli (opaque light and dark blue with yellow flecks)(10gp)", "Malachite (opaque striated light and dark green)(10gp)", "Moss agate (translucent pink or yellow-white with mossy gray or green markings)(10gp)", "Obsidian (opaque black)(10gp)", "Rhodochrosite (opaque light pink)(10gp)", "Turquoise (opaque light blue-green)(10gp)", "Tiger eye (translucent brown with golden center)(10gp)"],
    /*Tier 2 50gp*/["Pearl (white, lustrous) (50gp)","Bloodstone (opaque dark gray with red flecks)(50gp)", "Carnelian (opaque orange to red-brown)(50gp)", "Chalcedony (opaque white)(50gp)", "Chrysoprase (translucent green)(50gp)", "Citrine (transparent pale yellow-brown)(50gp)", "Jasper (opaque blue, black, or brown)(50gp)", "Moonstone (translucent white with pale blue glow)(50gp)", "Quartz (transparent white, smoky gray, or yellow)(50gp)", "Sardonyx (opaque bands of red and white)(50gp)", "Zircon (transparent pale blue-green)(50gp)", "Onyx (opaque bands of black and white, or pure black or white)(50gp)", "Star rose quartz (translucent rosy stone with white star-shaped center)(50gp)"],
    /*Tier 3 100gp*/["Jet (opaque, deep black) (100gp)", "Jade (translucent deep green) (100gp)", "Amber (transparent, watery to rich gold) (100gp)", "Coral (opaque, crimson) (100gp)", "Pink Pearl (opaque, lustrous pink) (100gp)","Sapphire (deep blue, transparent) (100gp)"],
    /*Tier 4 500gp*/["Diamond (blue-white, brown, or blue)(3-500gp)","Alexandrite (transparent dark green)(500gp)", "Aquamarine (transparent pale blue-green)(500gp)", "Black pearl (opaque pure black)(500gp)", "Blue spinel (transparent deep blue)(500gp)", "Peridot (transparent rich olive green)(500gp)", "Topaz (transparent golden yellow)(500gp)","Cat's Eye Agate (Yellowish green, gray, or brownish red with a white stripe down the middle) (500gp)"],
    /*Tier 5 1000gp*/["Black opal (translucent dark green with black mottling and golden flecks)(1000gp)", "Blue sapphire (transparent blue-white to medium blue)(1000gp)", "Emerald (transparent deep bright green)(1000gp)", "Fire opal (translucent fiery red)(1000gp)", "Opal (translucent pale blue with green and golden mottling)(1000gp)", "Star ruby (translucent ruby with white star-shaped center)(1000gp)", "Star sapphire (translucent blue sapphire with white star-shaped center)(1000gp)", "Yellow sapphire (transparent fiery yellow or yellow green)(1000gp)", "Amethyst (deep purple, transparent) (1000gp)","Sapphire (deep pink with striping) (1000gp)"],
    /*Tier 6 5000gp*/["Black sapphire (translucent lustrous black with glowing highlights)(5000gp)", "Diamond (transparent blue-white, canary, pink, brown, or blue)(5000gp)", "Jacinth (transparent fiery orange)(5000gp)", "Ruby (transparent clear red to deep crimson)(5000gp)"],
]
let jewelry =[
    /*Tier 1 25gp*/[],
    /*Tier 2 250gp*/[],
    /*Tier 3 750gp*/[],
    /*Tier 4 2500gp*/[],
    /*Tier 5 7500gp*/[],

]


/*
Other Valuable rewards
1: Lore and Knowledge
2: Cool but mostly useless items
3: Plot Relevant Items
4: NPC Contacts, allies and friends
5: Pets and Followers
6: New skills and languages
7: Trinkets
8: Boons Blessings and Charms
9: Properties
10: Mundane Weapons and Armor
11: Broken items
12: A brand new car!
13: Land and Title
14: Faction Favor
15: Backstory Stuff


*/