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
function rollArray(array) {
    let shuffled = shuffle(array)
    let index = Math.floor(Math.random() * shuffled.length)
    return `(Roll: ${index}/${shuffled.length}) ${shuffled[index]}`;
};
function toWords(s) {
    var th = ['', 'thousand', 'million', 'billion', 'trillion'];
    var dg = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    var tn = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'eineteen'];
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

function origin() {
    var worldOrigin = [
        "Unfinished - The creation of the world is ongoing, and may never cease. Some things we take for granted may not yet exist, the laws of reality seem illogical at times, and the half-formed landscape is in a constant state of flux.", 
        "Alien Forged - The world was created to serve as a permanent abode for a series of strange and alien entities, and it is likely they will one day return. The world is bizarre and confounds earthly logic.", 
        "Dreamscape - The world is nothing but the dream of a slumbering deity, and none can say when they’ll awaken. Though the world seems mundane enough at first glance, a deeper look reveals that not all is as it seems.", 
        "Demiurge - An imperfect being of immense power created the world, and thus, it is flawed. The world is fundamentally broken, and though the Demiurge is silent; shackled, slumbering, ashamed, or slain, in time, they may free themselves and undo their mistake.", 
        "True Creator - A perfect being of immense power created the world, and at first, it was likewise flawless, but its perfection did not last. Whether by the Creator’s intent, subsequent abandonment, or unforeseen tragedy, the world has become flawed, but it could be far worse.", 
        "By Committee - Numerous divine entities of varying power set out to create the world, and despite their ceaseless bickering, stubborn compromise was made, and in time, it came into being. The world is a diverse landscape, the work of many craftsmen.", 
        "Mechanistic - Impersonal forces of nature created the world, and for better or worse, no deity had a hand in its creation. The world is as could be expected, to the benefit or the detriment of its denizens.", 
        "Disaster - The world came about as the unintentional byproduct of an incomprehensibly vast struggle in the void before creation. The world, though much calmer to an extent, still bears the scars of its birth.", 
        "Precursors - An impossibly advanced post-scarcity civilization created the world with seemingly magical technology to serve their inscrutable needs. Though they are long gone, their legacy remains in the ancient ruins scattered across the world.", 
        "Profane Assemblage - A hubristic arch-demon of unparalleled power created the world in an attempt to make a work of art that would last the test of time. The world is hellish and cruel, but beautiful in its own way.", 
        "Eternal Existence The world is an enigma, in that it has never not existed in some way, shape, or form. Even the deities can’t remember when it emerged because it has no true beginning, and should all but the most ruinous of ends come to pass, it shall have no end.", 
        "Dimensional Conflux - The world is situated in the center of a plane where extra-dimensional energies once clashed, bringing it forth at the center of the maelstrom. Though the storm has passed and the world is stable, occasionally outsiders find their way in.",
        `Arcane Anomaly - The world exists within a massive arcane bubble, formed from the mingling of countless spells gone awry. Magic is unpredictable and diverse here, giving rise to wondrous creatures, terrains, and phenomena.`,
        `Fossilized Thought - The world is the crystallized thought of a being beyond comprehension. Every element, creature, and event is a manifestation of this entity's consciousness, though it no longer actively shapes its own creation.`,
        `Chaos Calmed - Before this realm, there was only a wild storm of raw magic and primordial essence. A mysterious force or ritual brought order to this storm, and the world was born from the resulting equilibrium.`,
        `Infernal Bet - Two powerful demons made a bet, with the creation of this world as their wager. Each facet of the world reflects their whims, vices, and virtues as they tried to outdo one another.`,
        `Fading Echo - The world is the decaying echo of another universe that was once vibrant and alive. As the original fades, this one grows stronger, though elements of the old world occasionally bleed through.`,
        `Celestial Melody - The world is the result of a cosmic song sung by a choir of ancient, astral entities. Each note shaped mountains, oceans, and skies, and the echoes of this song can still be heard in the world's harmonious places.`,
        `Gigantic Relic - The world is actually a dormant, colossal entity or machine from another universe. Its inner workings, fluids, and energies create the landscapes, weather, and magical phenomena experienced by its inhabitants.`,
        `Tale Woven - Renowned cosmic storytellers of the multiverse gathered to weave a world from their tales, each contributing to its rich history, mythos, and destiny.`,
        `Shattered Prism - The world was birthed when a cosmic prism containing various realities shattered. The fragments of different worlds combined to form this unique, mosaic-like realm.`,
        `Temporal Nexus - Time itself created the world at the point where various timelines intersected, merged, and diverged. Because of this, the world is a melting pot of epochs, civilizations, and futures.`,
        `Divine Experiment - A curious deity wondered what would happen if they mixed a bit of every known world ingredient into a single cauldron. The result was this world, unpredictable and filled with contrasts.`,
        `Lost Realm - This world was once part of a larger universe but was severed and lost in the void. Over eons, it evolved and grew in isolation, developing its unique properties and creatures.`,
        `Cursed Craft - A mighty sorcerer sought to craft the perfect realm for themselves but was betrayed, and their creation was cursed. This world is the result, teeming with wonder but tainted by underlying malevolence.`,
        `Astral Ark - As an old universe faced destruction, beings from various planets and realms boarded an astral ark. This ark eventually became the world, a refuge and new home for countless displaced entities.`,
        `Guardian's Domain - An omnipotent guardian, sworn to protect all life, created this world as a sanctuary for endangered species, cultures, and magics from across the multiverse.`        
    ];
    document.getElementById("Origin").innerHTML = searchArray(worldOrigin);
};
function comp() {
    let physComp = [
        "Frozen - The world is icy cold, dominated by endless swathes of tundra, vast pine forests, and glacial clusters, here, warm weather is rare, and food is scarce.", 
        "Far Up Above - The world’s landmass is comprised of a series of floating islands, constantly orbiting and colliding with one another, far above a bottomless void.", 
        "Archipelago - The world is ocean as far as the eye can see, there are no landmasses save a series of scant island chains and coral reefs, and the concept of continents is widely regarded as fiction.", 
        "Almost Archipelago - The world is almost entirely ocean, and aside from a handful of middling continents, the entirety of the world’s landmass is made of scant island chains and coral reefs.", 
        "Earth-Like - The world boasts a balanced spread of continents and islands of various size, with a wide array of biomes and environs.", 
        "Almost Pangean - The majority of the world’s landmass is contained within a single large continent, though there are some lesser continents and scant island chains.", 
        "Pangean - The entirety of the world’s landmass is contained within a single, enormous continent, surrounded by seemingly endless oceans.", 
        "Deep Underground - The world is so deep the sky is considered a myth, consisting of a series of vast caverns, sprawling tunnel networks, and the rare water-flow from above.", 
        "Interplanar Maze - The world isn’t contained in the same dimension, rather, it is a series of pocket dimensions linked by an intricate network of portals, either naturally occurring or generated by magic. If deemed appropriate, this table may be rerolled to determine trends in the sub-dimensions.", 
        "Scorching - The world is scorching hot, dominated by endless swathes of rocky desert, parched badlands, and winding rivers, here, cold weather is rare, and water is scarce.",
        `Eternal Twilight - There's no day or night here. Instead, a perpetual twilight shrouds the world, creating unique ecosystems that thrive in the half-light. Forests glow with bioluminescence and creatures navigate with enhanced senses.`,
        `Forest World - The land is covered in massive, unending forests. From the evergreen woods of the colder regions to the dense jungles near the equator, the world teems with various kinds of trees and undergrowth.`,
        `Mountainous Realm - Rugged terrains dominate the world, from towering peaks touching the clouds to deep valleys and canyons. Most civilizations carve their homes into the mountainsides or nestle within the valleys.`,
        `Sky Lakes - Vast, floating lakes and rivers drift above the land. They are held aloft by a mysterious force, their waterfalls nourishing the world below. Cultures here often revolve around these sky-borne waters.`,
        `Mystic Storms - The world is a place where storms aren't just weather but are sentient, ever-moving entities. These storms can be negotiated with, revered, or feared, and many hold arcane secrets or energies.`,
        `Crystalline Landscape - Massive crystal formations pepper the world, ranging from quartz-like mountains to amethyst plains. The unique properties of these crystals influence magic, technology, and life in various ways.`,
        `Fog Enveloped - Thick mists and fogs cover the world, only occasionally lifting to reveal the land beneath. Navigation is a challenge, and many creatures and civilizations have adapted to a life in near-constant obscurity.`,
        `Living Land - The very earth itself is alive, with mountains that breathe, forests that move, and rivers with a heartbeat. The inhabitants live in harmony with, or sometimes in fear of, the sentient world around them.`,
        `Volcanic Terrain - The world is dotted with countless volcanoes, from bubbling lava pools to towering ash-spewing mountains. This makes for fertile but dangerous lands, and civilizations often harness the power of these fiery mountains.`,
        `Winding Labyrinths - Instead of traditional landscapes, the world is a vast maze, with walls made of stone, hedge, or even water. It is said that at the heart of the maze lies a great treasure or secret.`,
        `City World - Every inch of the planet is urbanized, a sprawling metropolis that never ends. Parks and green spaces are rare and highly valued. The history of how such a world came to be is often a mystery.`,
        `Magnetized - Strong magnetic fields crisscross the world. Metallic objects float or stick to surfaces unpredictably. The inhabitants have developed unique ways to harness or counteract these magnetic anomalies.`,
        `Astral Sea - The world is less solid land and more a vast sea of stars and cosmic energies, where islands float amidst star clusters and navigation is as much about astrology as it is cartography.`,
        `Cascade of Realms - The world is a vertical stack of different landscapes, each layer with its own sky, horizon, and rules. Ascending or descending to a new level is a rite of passage for many inhabitants.`,
        `Temporal Flux - The world’s regions each exist in different time periods, from prehistoric jungles to futuristic cities. Traveling from one place to another might mean journeying to another age.`
    ];
    document.getElementById("Comp").innerHTML = searchArray(physComp);
};
function age() {
    const worldAge = [
        "The World is in its Cradle - The creation of the world came to a close recently, if it ever did, and its denizens have only begun to master the rudiments of tool-crafting and fire-building.", 
        "The World is in its Infancy - The world is savage, primal, and dominated by wilderness, and armed with the knowledge of their ancestors, its denizens have begun to explore and exploit it.", 
        "The World is Still Young - By and large, nature reigns supreme, but in several regions its denizens have begun to till the earth, construct city-states, and establish sophisticated culture.", 
        "The World is in its Adolescence - Little by little, nature has begun to give way to civilization, and its denizens have begun to sail to distant lands, subjugating other peoples and being subjugated in turn.", 
        "The World is No Longer Young - The lion’s share of its denizens have settled and founded great nations by the sweat of their brow, though the wildest lands and those within them are yet untamed.", 
        "The World is Mature - The world has finally been explored and the wild settled, its denizens have a wealth of wondrous accomplishments, discoveries, and prosperity, and the surplus is such that some have come to question their deepest held notions and certainties.", 
        "The World is at its Zenith - The illustrious civilizations, technological wonders, and horrific wars of the world’s denizens are breathtaking, though in time, their burden on the land may prove too much to carry.", 
        "The World has begun to Age - The world’s denizens have succumbed to decadence, and grown complacent while the resources needed to sustain their comfort run thinner each generation.", "The World is No Longer Relevant - The world’s denizens have managed to overcome their ennui, and in the dawn of a new age, have begun to expand beyond the world, exploring and settling new worlds and dimensions beyond their plane.", 
        "The World has grown Old - The world’s denizens were unable to overcome their ennui, and in time it consumed them. The zenith of the world is a distant memory, civilization has crumbled, and its surviving denizens struggle to scrape by on what little remains.", 
        "The World is on the Verge of Death - The end is nigh, the world has outlived its time, the stench of decay has begun to set in, and final death is inevitable, but it is slow to come, painful, and hard-fought by the few denizens that endure.", 
        "The World is on the Cusp of Rebirth - The end has come, the world has died, and much of the legacy of the ancients has been lost, but little by little, life has begun to return, and the still remaining denizens, hardened by their ancestor’s struggle, have begun to thrive in the ashes.",
        `The World is in Stasis - Time seems to stand still. The same empires, cultures, and traditions persist without much change. Its denizens are trapped in a seemingly never-ending cycle of repetition, struggling to break free.`,
        `The World Breathes in Legends - The golden age of heroes has dawned. Every corner of the world is filled with tales of extraordinary individuals, magic, and fantastical creatures. The denizens look up to these legends for inspiration or fear.`,
        `The World Feels a Stirring - An unseen force or energy is slowly awakening, bringing with it new magic, technologies, or even species. The world's denizens are curious and anxious about this unfolding mystery.`,
        `The World Sits in Contemplation - There’s been a global move towards introspection, spirituality, and the mysteries of the universe. The denizens are more focused on inner growth and understanding than external conquest.`,
        `The World Faces Renewal - New civilizations are rising, challenging the old. A renaissance of art, technology, and thought sweeps across the lands. Its denizens are filled with hope and the energy of possibility.`,
        `The World is Fragmented - Once a unified or coherent entity, the world has fractured into countless small territories, each fiercely independent and protective. Its denizens face the challenge of diplomacy and skirmishes.`,
        `The World in Regression - Due to some calamity or choice, civilizations are moving away from complex technologies and systems, reverting to simpler ways. Its denizens find solace in traditions, though some mourn the lost progress.`,
        `The World Embraces Shadows - Darkness, both literal and metaphorical, encroaches upon the world. Secrets, mysteries, and hidden agendas dominate. Its denizens either adapt to this clandestine existence or fight against the encroaching obscurity.`,
        `The World at Balance - Neither advancing nor regressing, the world exists in a delicate equilibrium. Every action has an equal reaction, and its denizens are hyper-aware of the consequences of their choices.`,
        `The World in Memory - The world lives more in the past than the present. Great achievements are behind them, and its denizens are in a state of nostalgia, cherishing and preserving remnants of the golden days.`,
        `The World Echoes with Silence - Great civilizations have fallen, and vast expanses of the world are uninhabited. The few denizens left seek each other out amidst the ruins, cherishing any signs of life.`,
        `The World Awaits a Signal - There's an anticipation, a prophecy, or a foretold sign that the world's denizens are waiting for. This expected event or moment keeps them in suspense and dictates their actions.`,        
    ];
    document.getElementById("Age").innerHTML = searchArray(worldAge);
};
function dieties() {
    const worldDieties = [
        "Absent - The deities of the world are dead, gone, or were never there to begin with. There is nothing to intervene or answer prayers.", 
        "They Watch - The deities of the world are distant observers, and it would take something truly extraordinary to get their attention.", 
        "Ascended Mortals - The deities of the world are not deities, but rather, former mortals that, through strength or through guile, transcended their mortality to become something more.", 
        "Not Of This World - The deities of the world are not of this world at all, but rather, came from another place or another time, perhaps fleeing ennui or seeking to settle.", 
        "Strange Cosmos - The deities of the world are non-anthropomorphic entities, and their logic is nigh-incomprehensible to those who serve them.", 
        "Familiar Cosmos - The deities of the world are a varied lot, resembling larger than life mortals more than anything, with all the good, the bad, and mostly true mythologies that entails.", 
        "Heavenly Feud - The deities of the world are petty, meddling, and powerful, but luckily, the threat of mutually assured deicide keeps them from open conflict, to an extent.", 
        "Exalted Beasts - The deities of the world are dreadful monsters, mindless beasts and natural disasters given godhood.", 
        "True Divinities - The deities of the world are truly supreme beings, present in all places at once, with nigh-limitless power to bring to bear, and a sense of restraint most in their position would lack.", 
        "Profane Idols - The deities of the world are in fact demons, and thus, are much more callous and cruel than one would expect.", 
        "Artificial Idols - The deities of the world were created by the mortal races, either formed from their collective subconscious, or arcane constructs of unimaginable potency wrought in the long-forgotten past.",
        `Celestial Drama - The deities of the world are engaged in a celestial theater, playing roles in an eternal drama that influences the events below, with mortals as their audience and sometimes, unwitting actors.`,
        `Cycle of Rebirth - The deities of the world live, age, and then die, only to be reborn again. Each age witnesses different gods with varying personalities and domains.`,
        `Embodied Concepts - The deities of the world are embodiments of abstract ideas, emotions, and principles. They rise and wane in power based on the prominence of their domain in the world.`,
        `Sleeping Titans - The deities of the world are dormant, slumbering through eons, but their dreams influence reality. Their awakening, should it happen, would be a world-shattering event.`,
        `Ephemeral Spirits - The deities are numerous and short-lived, living only for a few generations before fading away. They're born from strong emotions or significant events.`,
        `One Above All - There exists only a single deity, multifaceted and omnipotent. The various gods worshipped are mere aspects or interpretations of this singular entity.`,
        `Mortal-made Gods - The deities are powerful entities created or uplifted by ancient civilizations. They once served mortals but have since risen to be revered.`,
        `The Quiet Whisperers - The deities seldom interact directly. Instead, they subtly inspire, influence thoughts, and gently guide through quiet whispers in the minds of mortals.`,
        `Deities in Exile - Once powerful rulers of the realm, these deities were cast out or chose to retreat, living now in hidden sanctuaries, dreaming of a return.`,
        `Mortal Masks - These deities walk among mortals, hiding their divine essence. They might be kings, hermits, or even beggars, influencing events from within the mortal coil.`,
        `The Unknowable - The true nature and count of the deities remain a mystery. The world has countless myths, and each might hold a grain of truth, but no one knows for certain.`,
        `Shattered Pantheon - Once a cohesive group, a great schism shattered the deities into factions. They now vie for dominance, favor, and worship.`,        
    ];
    document.getElementById("Dieties").innerHTML = searchArray(worldDieties);
};
function magic() {
    const worldMagic = [
        "Magic is Mundane - Mortals have no magic, it is solely the domain of the world’s deities and lesser supernatural entities.", 
        "Magic is Rare - The world’s magic is hard to find and harder to use. The vast majority is useless superstition, incredibly tedious to employ, or dangerous to the user, but what works tends to be stronger than the freely available magic of other worlds.", 
        "Magic is Dark - All but the weakest magic comes only through diabolical pacts and unspeakable deeds, and when it does, it is corrupting, chaotic, and catastrophic to the user and their victims alike.",
        "Magic takes Tools - The mortal mind can’t grasp any but the weakest of magic, only through artifice, scroll-scribbling, alchemy, and enchantments can its energies be brought to bear.", 
        "Magic is Demanding - Magic is both powerful and attainable, but it requires decades of difficult study, ironclad self-control, and immense personal sacrifice from its users.", 
        "Magic is Inherited - Only mortals descended from or greatly favored by supernatural entities can channel magic, and while great within its scope, their power is narrow and limited.", 
        "Magic is Common - The study of magic is well-known and widespread, to the extent a town may have a wizard living between its carpenter and smith, but due to its ubiquity, it tends to be weaker than the less available magic of other worlds.", 
        "Magic is Myriad - Numerous methods of magic exist, everything from dark pacts, to artificial tools, to arduous study, and simple circumstance of birth, and its divergent practitioners may have an intense and oft-bloody rivalry with one another.", 
        "Magic is Science - In their curiosity, mortals have codified and tested magic to the extent it’s seen as merely another discipline of science, and broadly implemented in technology.", 
        "Magic is Everywhere - Powerful magic is freely accessible, at minimal to no cost and risk to its users, and magical entities that may be rare in other worlds readily serve mortals in all aspects of life.", 
        "Magic is Bound - The mortal races aren’t able to wield magic on their own, instead they must give up a part of themselves to bind a spirit’s soul to theirs, or entrap a spirit in an item of precious value and force it to cast at its wielder’s command.",
        "Magic is Wild - Magic is an unpredictable and untamed force, constantly shifting and changing. Those who dare to use it must be prepared for unintended consequences, as the magic may have a will of its own.",
        "Magic is Forbidden - Governments, religions, or other powerful institutions have outlawed the use of magic. Its practice is hidden, secretive, and often associated with rebellion or criminality.",
        "Magic is Dying - Once vibrant and widespread, the world's magical energies are waning. The causes might be mysterious or known, but the effects are felt by all magic users, leading to a desperate race to preserve or exploit what remains.",
        "Magic is Nature - Magic is intertwined with the natural world, drawn from the plants, animals, and elements. It promotes harmony and balance but can be wrathful if misused or if nature is harmed.",
        "Magic is Monopolized - A single entity, be it a government, corporation, or individual, controls the majority of magical knowledge and resources. This concentration of power may lead to inequality, unrest, and conflict.",
        "Magic is Symbiotic - Magic can only be used through a mutual agreement or bond with magical creatures or entities. These relationships may be based on respect, manipulation, or coercion, and form a unique magical system.",
        "Magic is Time-bound - The use of magic is connected to specific times or celestial events. Whether it's phases of the moon, solstices, or other temporal factors, magic ebbs and flows with the passage of time.",
        "Magic is Sentient - The magical energies of the world are not merely a force to be harnessed but possess consciousness and intent. Communication, negotiation, or conflict with these sentient energies forms the basis of magical practice.",
        "Magic is Sacrificial - The power to wield magic requires physical, emotional, or spiritual sacrifices. The greater the magic, the greater the cost, leading to profound ethical dilemmas and personal struggles for those who pursue this path.",
        "Magic is Healing - The primary purpose and function of magic in this world is to heal and nurture. Combat and destructive uses of magic are rare or non-existent, and magical practice focuses on restoration, growth, and empathy.",
        "Magic is Transformative - Magic primarily functions to change and transmute, whether it's the alteration of objects, the metamorphosis of beings, or the shifting of reality itself. This leads to a world of constant flux and potential.",
        "Magic is Artistic - Magic is expressed through art, music, poetry, and other creative endeavors. The most powerful magic users are those with profound artistic talents, and magical duels might look more like artistic competitions.",
        "Magic is Ancestral - Magic is deeply rooted in family lines and traditions. Knowledge and abilities are passed down through generations, and a person's lineage may determine their potential as a magic user.",
        "Magic is Cultural - Different cultures within the world have unique magical traditions, methods, and philosophies. Interactions between these diverse magical systems can lead to cooperation, conflict, or synthesis.",
        "Magic is Gendered - Magic operates differently based on gender, with specific abilities or roles assigned to different genders. This can influence societal norms, relationships, and the personal journey of magic users.",
        "Magic is Cursed - Magic comes with inherent curses or risks that affect both the user and those around them. This might be a deliberate design by some higher power or a side effect of tapping into forces beyond mortal understanding.",
        "Magic is Compassionate - Magic is driven by empathy and compassion, acting as a force for good. It refuses to be used for harm or selfish gains and aligns itself with those who seek to make positive changes in the world.",
        "Magic is Seasonal - The power and nature of magic change with the seasons. Magic users must understand and adapt to these shifts, and some may specialize in the magic of a particular season.",
        "Magic is Collective - Magic is not an individual force but thrives on community, connection, and shared intention. It grows stronger when practiced collectively and may be weaker or even inaccessible to lone practitioners.",
        "Magic is Competitive - Magic is a central aspect of competition, sport, or games within the world. Mastery of magic is as much about strategy, teamwork, and skill as it is about understanding mystical forces.",
        "Magic is Love-bound - Magic is intimately tied to love and relationships. Whether it's romantic, familial, or platonic, the strength and nature of one's magical abilities are closely linked to their bonds with others.",
        "Magic is Dreamt - Magic is accessed and shaped within dreams. Dream mages walk a fine line between reality and imagination, and the dream world is a place of both incredible power and potential danger.",
        "Magic is Reflective - Magic acts as a mirror of the user's inner self, reflecting their virtues, flaws, desires, and fears. Personal growth and self-awareness become crucial in mastering this form of magic.",
        "Magic is Historical - Magic is tied to historical events, figures, or artifacts. The past holds the key to magical power, and those who delve into history can unlock abilities lost to time.",
        "Magic is Commercialized - Magic has become a commodity, bought and sold like any other good. This commercialization has broad impacts on the economy, society, ethics, and the personal experiences of magic users.",
        "Magic is Environmental - Magic is directly tied to the health and state of the environment. Pollution, deforestation, or other ecological issues can weaken or corrupt magic, leading to a complex relationship between magic users and their world.",
        "Magic is Regional - Magic varies significantly by geography, with different regions having access to unique magical resources, traditions, or restrictions. This creates a rich tapestry of magical diversity across the world.",
        "Magic is Harmonious - Magic must be practiced in balance and harmony with other forces, both magical and natural. Imbalance leads to weakness or catastrophe, and magic users must strive for equilibrium in all things.",
        "Magic is Organic - Magic is grown, cultivated, and harvested like a crop. Magical farms or gardens might be tended by specialized practitioners, and the quality of the 'harvest' affects the potency of the magic.",
        "Magic is Hierarchical - Magic operates within a strict hierarchy, with levels or ranks that determine a user's power and privileges. Ascending this hierarchy requires formalized testing, challenges, or other criteria.",
        "Magic is Animalistic - Magic is closely tied to animals and their instincts, behaviors, and spirits. Magic users often form bonds with magical creatures or learn to harness the inherent magic within the animal kingdom.",
        "Magic is Celestial - Magic is influenced by celestial bodies such as stars, planets, and comets. Astrological knowledge and timing play a crucial role in wielding this type of magic.",
        "Magic is Philosophical - Magic is deeply entwined with philosophy and ethical considerations. Different schools of thought lead to different magical practices, and debates over magical ethics are common.",
        "Magic is Judicial - Magic is used primarily for law, justice, and governance. It may be employed by judges, law enforcement, or politicians to maintain order, solve disputes, or enforce societal rules.",
        "Magic is Musical - Magic is channeled and controlled through music, whether vocal or instrumental. The rhythm, melody, and harmony of the music direct the flow of magical energy.",
        "Magic is Industrial - Magic has been harnessed for industrial purposes, powering machinery, transportation, and manufacturing. This has led to economic growth but may also raise ethical or environmental concerns.",
        "Magic is Festive - Magic is strongest during festivals, holidays, and communal celebrations. These events become focal points for magical activities, and the joy and unity of the people amplify the magical energies.",
        "Magic is Aesthetic - Magic is directly linked to beauty, elegance, and aesthetic appreciation. The crafting of beautiful objects, art, or architecture is a magical act, and aesthetic sensibilities guide magical practice.",
        "Magic is Theatrical - Magic is performed and experienced as a form of theater or entertainment. Showmanship, drama, and audience engagement are key to this magical tradition.",
        "Magic is Aquatic - Magic is drawn from the sea, rivers, and other bodies of water. Water mages may have unique abilities, rites, and connections to aquatic creatures and deities.",
        "Magic is Nomadic - Magic is not tied to a particular place but travels with nomadic tribes or individuals. It adapts and changes with the journey, drawing power from movement and exploration.",
        "Magic is Linguistic - Magic is tightly bound to language, with each word, phrase, or script carrying intrinsic magical properties. Linguists, poets, and scholars become the primary wielders of magical power.",
        "Magic is Elemental - Magic is divided into distinct elemental forces such as fire, water, earth, and air. Mastery of these elements, or the fusion of them, becomes central to magical practice.",
        "Magic is Chronological - Magic is tied to the manipulation and understanding of time. Whether speeding it up, slowing it down, or glimpsing possible futures, time magic is a delicate and profound art.",
        "Magic is Agricultural - Magic is used primarily for farming and food production. It can enhance growth, control weather, and protect crops, forming the backbone of the world's food supply.",
        "Magic is Therapeutic - Magic is used for mental and emotional healing, as well as physical restoration. Therapists and healers use it to mend broken minds and spirits, creating a world focused on well-being.",
        "Magic is Athletic - Magic enhances physical abilities, sports, and athleticism. Competitions and games that integrate magic become central to the culture, and athletes train in both physical prowess and magical skill.",
        "Magic is Aquatic - Magic is derived from or primarily used in oceans, rivers, or lakes. Water-based magic might involve control over tides, communication with aquatic life, or special underwater abilities.",
        "Magic is Meteorological - Magic is connected to weather patterns and atmospheric conditions. Weather mages can summon storms, clear skies, or manipulate temperatures, affecting both daily life and strategic decisions.",
        "Magic is Emotional - Magic is fueled by emotions such as love, anger, fear, or joy. The intensity and control of emotions directly impact the effectiveness and nature of magical abilities.",
        "Magic is Geometric - Magic is based on geometrical shapes, symbols, and patterns. Creating precise geometric designs is essential for casting spells, and errors in design can lead to unintended effects.",
        "Magic is Dynastic - Magic is controlled by a few powerful families or dynasties. Their control over magical resources, knowledge, and lineage creates a power structure that influences politics and society.",
        "Magic is Educational - Magic is taught openly in schools and universities. The education of magic is as common as other subjects, with standardized curriculums, exams, and varying levels of expertise.",
        "Magic is Architectural - Magic is embedded in buildings, bridges, and structures. Architects and builders use magic to create impossible designs, enhance durability, or imbue structures with special properties.",
        "Magic is Memorial - Magic is tied to memory and history. It can be used to preserve memories, explore historical events, or even manipulate the memories of individuals.",
        "Magic is Celestial - Magic is connected to celestial navigation and the alignment of stars. It might be used for navigation, prophecy, or to draw power from constellations.",
        "Magic is Diplomatic - Magic plays a key role in diplomacy and international relations. Envoys and diplomats use it to negotiate treaties, resolve conflicts, or gather intelligence.",
        "Magic is Mechanized - In a blend of technology and mysticism, magic powers machines and mechanical devices. Engineers and inventors create magical machinery that impacts transportation, industry, and warfare.",
        "Magic is Gastronomic - Magic is cooked, brewed, and baked. Culinary wizards craft magical dishes, potions, and feasts that can heal, enchant, transform, or even curse those who partake.",
        "Magic is Archaeological - Magic is unearthed through the excavation of ancient ruins, artifacts, and relics. Archaeological mages engage in adventurous exploration to rediscover lost magical civilizations and techniques.",
        "Magic is Sensory - Magic is tied to the five senses, and practitioners can manipulate taste, smell, sight, touch, and hearing through magical means. Sensory mages have unique abilities to affect perception and sensation.",
        "Magic is Technological - Magic is integrated with technology, allowing for magi-tech devices, vehicles, and systems. Tech mages combine engineering with arcane knowledge to push the boundaries of both fields.",
        "Magic is Mystical - Magic remains a profound mystery, even to its practitioners. It resists categorization, analysis, or consistent rules, making it a force of wonder, unpredictability, and profound reverence.",
        "Magic is Karmic - Magic operates on principles of karma, aligning with a user's ethical choices and deeds. Good and bad actions resonate through one's magical power, influencing success, potency, and consequences.",
        "Magic is Mathematical - Magic is accessed through complex mathematical formulas and calculations. Mathematical wizards must solve intricate equations, utilizing logic and numerical skill to cast spells.",
        "Magic is Ritualistic - Magic requires elaborate rituals and ceremonies. These rituals may take hours or even days to perform and often involve specific materials, symbols, and precise timing.",
        "Magic is Literary - Magic resides in books, scrolls, and written texts. Libraries and archives become powerful magical repositories, and literary scholars are revered as mighty spellcasters.",
        "Magic is Martial - Magic is a key component in warfare and military strategy. Soldiers are trained in battle magic, and generals must consider magical tactics and defenses in their planning."
    ]
    
    document.getElementById("Magic").innerHTML = searchArray(worldMagic);
};
function titan() {
    let worldTitan = [
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
    ]
    document.getElementById("Titan").innerHTML = searchArray(worldTitan);
};
function populate() {
    document.getElementById("Arches").innerHTML = "";
    document.getElementById("Intera").innerHTML = "";
    let worldIntSpecies = [
        "Only one species, Humans, exist in this world.", 
        "Only Humans and " + '@@Placeholder@@' + "other significant subspecies exist in the world.", 
        "Humans and " + '@@Placeholder@@' + "other species exist in the world.", 
        "Humans and " + '@@Placeholder@@' + "other species exist in the world.", 
        "Humans and " + '@@Placeholder@@' + "other species exist in the world.", 
        "Humans and " + '@@Placeholder@@' + "other species exist in the world.", 
        "No Humans exist in the world, instead, there is/are " + '@@Placeholder@@' + "other species.", 
        "No Humans exist in the world, instead, there is/are " + '@@Placeholder@@' + "other species.", 
        "No Humans exist in the world, instead, there is/are " + '@@Placeholder@@' + "other species.",
    ];
    let worldSpecArchetypes = [
        "Brute - known for prodigal strength, near-endless endurance, and dim wittedness.", 
        "Vermin - known for individual incompetence, short lifespan, and rapid rate of reproduction.", 
        "Agile - known for incredible dexterity, mind-boggling flexibility, and skill at moving unseen.", 
        "Elder - known for ancient history, long lifespan, deep wisdom, and keen intellect.", 
        "Comfy - known for tight-knit families, friendly demeanor, and talent at agriculture.", 
        "Alien - known for the unsettling adaptations that allow it to thrive in areas other species couldn’t.", 
        "Artisan - known for industriousness, secretive demeanor, and talent at craftsmanship.", 
        "Big/Tiny - known for physical stature, which is much larger, or smaller than other species.", 
        "Arcane - known for high affinity for the supernatural, or seemingly supernatural abilities.", 
        "Collective - known for intensely hierarchal society, and the huge variation between castes.", 
        "Mundane - known for lack of distinguishing traits, versatile mediocrity, and widespread settlement.",
        `Nomad - known for their wandering lifestyle, adaptability to various environments, and vast oral traditions.`,
        `Aquatic - known for their ability to thrive in underwater environments, sleek adaptations, and deep understanding of marine ecosystems.`,
        `Aerial - known for their mastery of the skies, lightweight builds, and acute vision or sensing abilities.`,
        `Isolationist - known for their preference for solitude or seclusion, often residing in hard-to-reach places and exhibiting unique evolutionary traits.`,
        `Symbiotic - known for their close, often mutualistic, relationships with another species, leading to intertwined cultures and survival strategies.`,
        `Warrior - known for their martial prowess, strict codes of honor, and society focused on combat readiness.`,
        `Empath - known for their heightened emotional sensitivity, ability to perceive the feelings of others, and deep communal bonds.`,
        `Scholar - known for their thirst for knowledge, extensive archives, and institutions of learning.`,
        `Hibernator - known for cyclical periods of deep slumber, slow metabolism, and keen preparation skills.`,
        `Terraformer - known for their ability to modify and adapt environments to their needs, often leaving a transformed landscape in their wake.`,
        `Adaptable - known for their rapid evolution or metamorphic capabilities in response to environmental changes.`,
        `Mystic - known for their spiritual pursuits, rituals, and innate connection to the unknown.`,
        `Explorer - known for their insatiable curiosity, knack for discovery, and always pushing the boundaries of known territories.`,
        `Survivor - known for their resilience, ability to thrive in extreme conditions, and resourcefulness in the face of adversity.`,
        `Harmonious - known for their balanced relationship with nature, taking only what they need, and leaving minimal impact on their habitats.`,
        `Psionic - known for their mental abilities, including telepathy, telekinesis, and other mind-based powers, often possessing a collective consciousness or hive mind.`,
        `Luminous - known for their ability to produce and manipulate light, often bioluminescent and revered for their radiant beauty.`,
        `Guardian - known for their protective nature, often tasked with safeguarding sacred places, knowledge, or weaker species.`,
        `Mimic - known for their ability to imitate other species, objects, or environments, using this skill for either predation or defense.`,
        `Desert Dweller - known for their adaptations to survive in arid environments, including water conservation and nocturnal habits.`,
        `Toxic - known for their poisonous or venomous attributes, either for hunting prey or for defense against predators.`,
        `Ephemeral - known for their short but impactful lifespans, often living intensely for mere days or weeks but leaving a lasting impression on their surroundings.`,
        `Elemental - known for their strong affinity and connection to a particular natural element such as fire, water, earth, or air, often seen as incarnations of these elements.`,
        `Wanderer - known for their constant movement and inability to settle in one place, often in search of something elusive.`,
        `Hermit - known for their solitary nature, often seeking isolation for spiritual enlightenment or because of a unique life cycle.`,
        `Titan - known for their monumental size and the immense impact they have on their environment, often seen as god-like entities.`,
        `Shapeshifter - known for their ability to change their form and appearance at will, either as a means of adaptation, camouflage, or deception.`,
        `Sentinel - known for their keen observational skills, often serving as watchers or scouts, alerting their communities to dangers or opportunities.`,
        `Regenerative - known for their ability to heal rapidly or grow back lost parts, often considered almost immortal due to this trait.`,
        `Feral - known for their wild, untamed nature, often eschewing civilization in favor of primal instincts and behaviors.`
    ];
    let specInterRelat = [
        "Master Race - One species is widely considered to be superior paragons, to which others should defer.", 
        "Enslaved - One species is widely considered to be inferior, and is enslaved to an extent by the other species.", 
        "Race War - The species rarely meet, unless weapons are drawn. There is a long-held and irreconcilable animosity between the species.", 
        "Deep Mistrust - The species shun and avoid one another if possible, though outright violence is uncommon, race riots aren’t unheard of.", 
        "That Part of Town - Members of both species that live in the same region are discouraged from closer association. Any close relationships would mark those involved as pariahs.", 
        "Separate But Equal - The species have no hate for one another, and show their respect by staying out of each other’s way. Though there may be trade, the societies themselves are largely separate.", 
        "Pragmatic - Members of both species are businesslike in their dealings with one another, if it pays off to band together they’ll do so, but they won’t go out of their way to integrate.", 
        "Melting Pot - The species meet, trade, and form alliances fairly cordially, but primarily in trade hubs and major population centers. Sparks fly and cultures blend.", 
        "Amicable - Members of both species get along fairly well, all things considered. There are prejudices, but they are by no means universal.", 
        "Friendly - The species are quite close to one another, and interspecies marriages are not uncommon, though there are some few who’d prefer to remain separate.", 
        "What Species? - Members of both species are blind to their differences, and view themselves as one and the same in all matters, save mutually exclusive physical needs, of course.", 
        "The Same Species - Members of both species are in fact members of the same species, and can’t exist without one another, each is either different phases in the same species’ lifespan, or comprised of only gender that requires the other to reproduce. If deemed appropriate, this table may be rerolled to determine the relations between each part of the species.",
        `Patron & Ward - One species serves as protectors or guardians for the other, often due to some past pact or an innate sense of duty. This can be mutual or one-sided.`,
        `Mutualistic Symbiosis - Both species benefit significantly from their interactions with one another, such as one providing shelter while the other provides food.`,
        `Commensalism - One species benefits from the other without necessarily harming or helping them. Their interaction is neutral for one side.`,
        `Parasitic - One species benefits at the direct expense of the other, drawing resources or other benefits while harming their counterpart.`,
        `Religious Devotion - One species worships the other as gods or divine entities, offering sacrifices, prayers, and other forms of devotion.`,
        `Cultural Exchange - Both species greatly appreciate and integrate aspects of each other’s cultures, from arts and cuisine to philosophy and technology.`,
        `Guardian & Charge - One species has taken it upon themselves to watch over and protect the other, often without the latter's knowledge or against their will.`,
        `Research & Curiosity - One species is deeply intrigued by the other and dedicates significant resources to studying and understanding them. This can be mutual or one-sided.`,
        `Flee & Pursue - One species constantly flees or migrates to avoid the other, either due to predation, competition, or some other threat.`,
        `Competitive Rivalry - Both species see each other as rivals in many aspects of life, from resources to territory, leading to frequent non-lethal confrontations.`,
        `Mentor & Student - One species plays the role of teacher or mentor to the other, imparting knowledge, wisdom, or skills that the other lacks.`,
        `Ambassadors & Diplomats - Each species sends representatives to the other's communities to maintain peaceful relations, trade negotiations, and cultural exchanges.`,
        `Mimics & Models - One species has evolved to mimic or resemble the other for various reasons, such as protection from predators or to aid in hunting.`,
        `Trade Dependency - Both species rely heavily on one another for essential goods or services, forging a bond based on mutual economic interest.`,
        `Ancestral Debt - One species owes a great historic debt to the other due to an ancient act of salvation or sacrifice. This can often lead to one race being in service or offering regular tributes.`,
        `Dreamwalkers - One species can enter the dreams of the other. This has led to a unique dynamic where one species guides, terrifies, or manipulates the other through dream encounters.`,
        `Twin Souls - Legend says that members of both species once shared a single soul. Now, each individual seeks their counterpart from the other species, believing them to be their destined partner or soulmate.`,
        `Marked & Chosen - One species is born with marks that are said to be blessings or curses from the other species. The marked ones are often treated with reverence or fear, depending on the lore associated with these marks.`,
        `Lost Kin - Both species believe they descended from a common ancestor. Rituals, festivals, or reunions are held to commemorate their shared lineage.`,
        `Cursed/Blessed Transformations - Individuals from one species can transform into members of the other under specific conditions, be it a curse, a blessing, or a rite of passage.`,
        `Voiceless Pact - One species cannot speak but can perfectly understand the other. They rely on the other species to be their voice in interspecies matters.`,
        `Seasonal Migrations - One species migrates to the territories of the other during specific seasons. These migrations are pivotal events, leading to grand markets, festivals, or territorial disputes.`,
        `Shared Spirits - When a member of one species dies, their spirit is believed to reincarnate into the body of the other species. This belief can lead to a profound respect between the two species.`,
        `Guardians of Secrets - One species holds ancient secrets or forbidden knowledge, and the other seeks to learn, guard, or suppress this knowledge.`,
        `Harmonious Duality - Both species believe they represent two sides of the same coin, like day and night or yin and yang. Each complements the other, leading to a balance in their shared territories.`,
        `Echoed Lives - Important events in the life of an individual from one species are said to have mirrored events in the lives of those from the other species. These echoes are seen as omens or prophecies.`,
        `Fading Legacy - One species is dying out, and the other is trying to preserve their culture, traditions, and memories out of respect or shared history.`,
        `Champions & Challengers - Trials of combat, wit, or skill are frequently held between the species, with champions representing each side. These trials might determine resource rights, territorial boundaries, or simply honor.`,
        `Moonlit Bond - The two species can only interact during specific lunar phases. These brief windows of interaction are precious, leading to events ranging from sacred ceremonies to clandestine affairs.`,
        `Guardian & Ward - One species is seen as the protector of the other. This could be due to a physical advantage, magical ability, or simply an ancient vow that binds them.`,
        `Divine Interweave - The pantheon of gods worshipped by both species is a blend of their individual beliefs, with each god being a fusion of aspects from both species.`,
        `Shared Burdens - Both species suffer from the same affliction or curse, leading them to cooperate closely in search of a cure or mitigation.`,
        `Nature's Balance - The well-being of one species directly affects the well-being of the other. For instance, if one flourishes, the other might wither, leading to a delicate balance of power and survival.`,
        `Trade & Tribute - One species possesses a unique resource the other desperately needs. This dynamic sets the stage for intricate trade agreements or tributary systems.`,
        `Eternal Debaters - Both species have a tradition of engaging in long, intricate debates on philosophy, magic, or the nature of existence. These discussions can last for days and are a cornerstone of their shared culture.`,
        `Shadow & Form - One species exists only in the material plane, while the other exists as shadows or ethereal entities. Their interactions are fleeting but deeply meaningful.`,
        `Tied Fates - The destinies of both species are intertwined. Prophecies speak of events where both species must cooperate to avert disasters or achieve great victories.`,
        `Cultural Exchange - Both species have a ritual of exchanging individuals for a year to learn about each other's cultures, fostering understanding and camaraderie.`,
        `Harbingers & Omens - The appearance or behavior of one species is seen as an omen or harbinger of events by the other. This could be due to natural phenomena, migrations, or unusual behaviors.`,
        `Silent Pacts - While both species rarely engage in vocal communications, they have developed a complex system of signs, symbols, and rituals to communicate and make agreements.`,
        `Warriors & Scholars - One species prides itself on its martial prowess, while the other is renowned for its scholarly achievements. Both recognize and respect the strengths of the other, leading to an exchange of knowledge and skills.`,
        `Dreamweavers & Dreamers - One species has the ability to weave dreams and the other experiences them. These dreams could be messages, lessons, or simply experiences shared between them.`,
        `Twilight Kinship - The two species can only interact during the twilight hours of dawn and dusk, creating a unique culture centered around these ephemeral moments.`        
    ];

    let intSpecIndexObj = {
        '0': 0,
        '1': 3,
        '2': 4,
        '3': 6,
        '4': 2,
        '5': 8,
        '6': 3,
        '7': 6,
        '8': 9,
    };

    function findSpec() {
        let intSpecIndex = Math.floor(Math.random() * worldIntSpecies.length);
        //console.log(intSpecIndex)
        let rawString = worldIntSpecies[intSpecIndex];
        let otherSpecies = (1 + rollDice(intSpecIndexObj[intSpecIndex].valueOf()));
        let numbSpecInWords = toWords(otherSpecies);
        let fixedString = rawString.replace("@@Placeholder@@", numbSpecInWords);
        document.getElementById("Species").innerHTML = fixedString;
        if (intSpecIndex >= 6) {
            let numbSpecies = otherSpecies;
            return numbSpecies
        } else if (intSpecIndex === 0) {
            let numbSpecies = 1
            return numbSpecies
        } else {
            let numbSpecies = 1 + otherSpecies;
            return numbSpecies
        };

    }
    let numbSpecies = findSpec()
        //console.log(numbSpecies)

    function findSpecArchs() {
        let numArchs = numbSpecies;
        let finalArchs = shuffle(worldSpecArchetypes).slice(0, numArchs)
        return finalArchs
    }
    let archetypes = findSpecArchs()
        //console.log(archetypes)
    archetypes.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById("Arches").appendChild(li);
    });

    function findInteractions() {
        if (numbSpecies === 1) {
            let output = 'There are no other species, this race has taken over the world.'
            return output
        } else if (numbSpecies === 2) {
            let interaList = specInterRelat;
            shuffle(interaList);
            let finalIntera = interaList.slice(0, 1)
            let output = 'There is only one relationship between these two species: ' + '\n#1: ' + finalIntera[0];
            return output
        } else {
            let numOfInteract = Math.floor((numbSpecies / 1.5) + .6);
            let interaList = specInterRelat;
            shuffle(interaList);
            var multipleIntera = interaList.slice(0, numOfInteract)
            return multipleIntera
        };
    };
    let interactions = findInteractions()
    if (Array.isArray(interactions) === true) {
        interactions.forEach(function(item) {
            var li = document.createElement("li");
            var text = document.createTextNode(item);
            li.appendChild(text);
            document.getElementById("Intera").appendChild(li);
        });
    } else {
        document.getElementById("Intera").innerHTML = interactions
    }

    //console.log(interactions)
};
function buildWorld() {
    origin();
    comp();
    age();
    dieties();
    magic();
    titan();
    populate();
};

//Weather
let windDirection = [ "North", "East", "South", "West","North-West", "South-West", "North-East","South-East",];
let strangePhenomena = [
    `Ashfall - (Heavy white clouds of swirling smoke fill the sky, and it rains ash that coats everything in little flecks. A smell of burning wood or sulphur permeates the air.)    
        Also has the the effect of 
            Heavy Clouds (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.)`,
    "Solar Eclipse (For 1 hour during the day, it becomes night. Either select a dramatic time or roll a d12 for the hour. May or may not have prophetic ramifications.)",
    "Strange Lights (Strange swirling lights fill the sky, swirls of green, blue, and purple. Night becomes dim (strangely hued) light until the effect ends.)",
    "Meteor Shower (Stars begin to fall from the sky as lumps of stone and metal. All creatures gain 1 luck point as per the Lucky feat, which lasts until used or the weather changes. If you travel 4 or more hours outdoors through this weather, roll a d100. On a 1, a meteor strikes nearby, leaving 40d6 of devastation in it's wake, but perhaps you'll find something cool. Potential consequences: 2d12 damage from the shock wave, difficult terrain, or heavily obscuring dust clouds.)",
    `Malevolent Storm (The lightning seems to seek creatures out. While outside during this storm, roll a d20 every 1 hour you outside without shelter. On a 2-5, you are struck by a lightning bolt dealing 3d12 lightning damage. On a 1, you are attacked by an air elemental.)
    Has the effects of 
        Thunderstorm - (Lightning flashes and thunder crashes. All creatures are partially obscured if they are more than 20 feet from you. If you travel for 4 or more hours during a Thunderstorm, roll a d20. On a 1, you are struck by a lightning bolt dealing 3d12 lightning damage. Lightning and Thunder damage rolls have a +2. 
            Also has the effect of 
                Rain - (Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. If you attempt to take a long rest without cover, you must make a DC 12 Constitution saving throw gain the benefits for a long rest. All fire damage rolls have a –2. 
            Also has the effect of 
                Heavy Clouds - (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.), 
            Also has the effect of 
                High Winds - (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind).`,
    "Wild Magic Storm - (Fluctuations in the weave drive strange flashing lights and odd phenomena sweeping across the world. Rain falls upwards, plants bloom unseasonably, and people see apparitions of the dead and gone. High chance of encounters with sentient plants, ghosts, and strange illusions. All spells cast are naturally upcast by 1 level, but trigger a Wild Surge as per a Wild Magic Sorcerer class feature until the storm subsides)",
    `Frozen Echo - (The air grows still and thick with frost. Eerie, translucent replicas of objects and creatures that were present in the location a week prior appear and act as silent reenactments of the past. They cannot interact with the current environment or its inhabitants and disappear after 24 hours.)
        Also has the effect of Intense Cold - (The temperature drops sharply. Creatures without proper cold protection must make a DC 12 Constitution saving throw every hour or gain a level of exhaustion. Puddles freeze, and creatures not adapted to the cold move at half speed due to the chill.)
        Also has the effect of Heavy Clouds - (The sky is thick with an overcast gloom. Aerial creatures flying high have total cover, and outdoor light is weakened considerably. Navigation using celestial observation becomes tricky and is made with disadvantage.)`,
    `Glass Rain - (Transparent, razor-sharp shards of crystalline rain fall from the sky. They shimmer beautifully but are deadly to the touch. Cover is essential during such a storm.)
        Also has the effect of High Winds - (The winds carry the deadly glass shards at high speed, making the threat even more dangerous. Flying creatures are particularly vulnerable, facing piercing damage from the flying shards. All ranged weapon attacks are affected by the erratic movement of the glass.)`,
    `Time Distortion Field - (The sky shifts between day and night erratically, causing disorientation. Within this zone, time flows differently; minutes can feel like hours or vice versa.)
        Also has the effect of Temporal Echoes - (Past and future versions of creatures and objects momentarily appear as ghostly visions, sometimes acting out events or simply standing still, leading to confusion and potential forewarnings of imminent threats.)`,
    `Blood Mist - (A thick, crimson mist rolls in, limiting visibility. The mist has an iron scent, reminiscent of fresh blood. Legends speak of it being the manifestation of collective sorrow from a past tragedy.)
        Also has the effect of Whispering Shadows - (Silent phantoms lurk in the mist, their whispers just on the edge of hearing. They don’t cause harm but can be a significant distraction. Concentration checks are made with disadvantage due to the eerie ambiance.)
        Also has the effect of Sticky Ground - (The terrain becomes sticky and challenging to traverse, as if the sorrow of the mist infuses the land. Movement is halved, and creatures without proper footing might find themselves stuck temporarily.)`,
    `Rainbow Deluge - (A downpour of multicolored rain, each hue having a different magical property. Blue might heal minor wounds, red might induce short-lived passion or anger, and green could cause temporary growth of flora.)
        Also has the effect of Prismatic Vision - (The vibrant rain causes everyone's vision to be tinted in shifting colors, making it hard to discern the actual color of objects and potentially leading to misinterpretations.)
        Also has the effect of Euphoric Breeze - (The winds during this storm carry an uplifting scent that invigorates those who breathe it in, granting them temporary hit points but also making them slightly more susceptible to illusions.)`
];

function winterWeather() {
    let Winter = [
        `Blizzard (At the end of every hour spend in a Blizzard, make a DC 12 Constitution saving. On failure, you take 3d4 cold damage and gain one level of exhaustion. You make this check with advantage if you have proper gear. All creatures are heavily obscured if they are more than 20 feet from you. All terrain is difficult terrain.)
        Also has the effect of
            Snow (Unpleasant to travel in. All travel speed is halved. If snow occurs for two days in row, all terrain is difficult terrain and wagon travel is impossible until one day without snow passes. 
        Also has the the effect of
            Heavy Clouds - (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.) 
        Also has the effect of
            Freezing Cold - (If you attempt to take a long rest without cover and heat, you must make a DC 15 Constitution saving throw gain the benefits for a long rest. If you fail by 5 or more, you gain an additional level of Exhaustion. All cold damage rolls have a +2.)
        Also has the effect of
            High Winds - (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind)
        Replace with Thunderstorm when in climates without snow.
        Thunderstorm - (Lightning flashes and thunder crashes. All creatures are partially obscured if they are more than 20 feet from you. If you travel for 4 or more hours during a Thunderstorm, roll a d20. On a 1, you are struck by a lightning bolt dealing 3d12 lightning damage. Lightning and Thunder damage rolls have a +2. 
            Also has the effect of
                Rain - (Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. If you attempt to take a long rest without cover, you must make a DC 12 Constitution saving throw gain the benefits for a long rest. All fire damage rolls have a –2. 
            Also has the effect of
                Heavy Clouds - (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.), 
            Also has the effect of
                High Winds - (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind)`,
        `Snow (Unpleasant to travel in. All travel speed is halved. If snow occurs for two days in row, all terrain is difficult terrain and wagon travel is impossible until one day without snow passes. 
        Also has the the effect of 
            Heavy Clouds -The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage. 
        Also has the the effect of
            Freezing Cold -If you attempt to take a long rest without cover and heat, you must make a DC 15 Constitution saving throw gain the benefits for a long rest. If you fail by 5 or more, you gain an additional level of Exhaustion. All cold damage rolls have a +2. 
            Replace with Rain when in climates without snow - 
                Rain - (Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. If you attempt to take a long rest without cover, you must make a DC 12 Constitution saving throw gain the benefits for a long rest. All fire damage rolls have a –2. 
            Also has the effect of 
                Heavy Clouds - The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.)`,
        `Freezing Cold (If you attempt to take a long rest without cover and heat, you must make a DC 15 Constitution saving throw gain the benefits for a long rest. If you fail by 5 or more, you gain an additional level of Exhaustion. All cold damage rolls have a +2.)`,
        `Heavy Clouds (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.)`,
        `Light Clouds (This is the game as you normally play it. Clear bright light during day time, view of the stars and moon at night. No modifiers are added to play.)`,
        `Clear Skies (This is the game as you normally play it. Clear bright light during day time, view of the stars and moon at night. No modifiers are added to play.)`,
        `Strange Phenomena - (${searchArray(strangePhenomena)})`,
    ]
    document.getElementById("weather").innerHTML = searchArray(Winter);
};
function springWeather() {
    let Spring = [
        `Thunderstorm (Lightning flashes and thunder crashes. All creatures are partially obscured if they are more than 20 feet from you. If you travel for 4 or more hours during a Thunderstorm, roll a d20. On a 1, you are struck by a lightning bolt dealing 3d12 lightning damage. Lightning and Thunder damage rolls have a +2. 
        Also has the effect of 
            Rain - (Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. If you attempt to take a long rest without cover, you must make a DC 12 Constitution saving throw gain the benefits for a long rest. All fire damage rolls have a –2. 
        Also has the effect of 
            Heavy Clouds - (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.), 
        Also has the effect of 
            High Winds (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind)`,
        `Heavy Rain (Same as rain, but the DC becomes 16 to benefit from a long rest without shelter and if Heavy Rain occurs two days in a row wagon travel becomes impossible until one day without rain occurs. May cause flooding. All fire damage rolls have a –4. Lightning and Cold damage rolls gain a +2.)
        Also has the effect of
            Heavy Clouds - (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.)`,
        `Rain (Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. If you attempt to take a long rest without cover, you must make a DC 12 Constitution saving throw gain the benefits for a long rest. All fire damage rolls have a –2.) 
        Also has the effect of 
            Heavy Clouds - (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.)`,
        `Light Clouds (This is the game as you normally play it. Clear bright light during day time, view of the stars and moon at night. No modifiers are added to play.)`,
        `Clear Skies (This is the game as you normally play it. Clear bright light during day time, view of the stars and moon at night. No modifiers are added to play.)`,
        `High Winds (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind)`,
        `Scorching Heat (Blistering heat that is unpleasant to travel in. Creatures that attempt to travel during day light hours require twice the ration of water, and creature that travel for 4 or more hours or engage in heavy activity for 1 or more hour during the day and do not immediately take a short or long rest under cover must make a DC 10 Constitution saving throw or gain a level of Exhaustion. All fire damage rolls have a +2. All cold damage rolls have a –2.)`,
        `Strange Phenomena - (${searchArray(strangePhenomena)})`,
    ]
    document.getElementById("weather").innerHTML = searchArray(Spring);
};
function summerWeather() {
    let Summer = [
        `Thunderstorm (Lightning flashes and thunder crashes. All creatures are partially obscured if they are more than 20 feet from you. If you travel for 4 or more hours during a Thunderstorm, roll a d20. On a 1, you are struck by a lightning bolt dealing 3d12 lightning damage. Lightning and Thunder damage rolls have a +2. 
        Also has the effect of 
            Rain - (Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. If you attempt to take a long rest without cover, you must make a DC 12 Constitution saving throw gain the benefits for a long rest. All fire damage rolls have a –2. 
        Also has the effect of 
            Heavy Clouds - (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.), 
        Also has the effect of 
            High Winds (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind)`,
        `Light Clouds (This is the game as you normally play it. Clear bright light during day time, view of the stars and moon at night. No modifiers are added to play.)`,
        `Clear Skies (This is the game as you normally play it. Clear bright light during day time, view of the stars and moon at night. No modifiers are added to play.)`,
        `High Winds (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind)`,
        `Scorching Heat (Blistering heat that is unpleasant to travel in. Creatures that attempt to travel during day light hours require twice the ration of water, and creature that travel for 4 or more hours or engage in heavy activity for 1 or more hour during the day and do not immediately take a short or long rest under cover must make a DC 10 Constitution saving throw or gain a level of Exhaustion. All fire damage rolls have a +2. All cold damage rolls have a –2.)`,
        `Strange Phenomena - (${searchArray(strangePhenomena)})`,
    ]
    document.getElementById("weather").innerHTML = searchArray(Summer);
};
function fallWeather() {
    let Fall = [
        `Thunderstorm (Lightning flashes and thunder crashes. All creatures are partially obscured if they are more than 20 feet from you. If you travel for 4 or more hours during a Thunderstorm, roll a d20. On a 1, you are struck by a lightning bolt dealing 3d12 lightning damage. Lightning and Thunder damage rolls have a +2. 
        Also has the effect of 
            Rain - (Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. If you attempt to take a long rest without cover, you must make a DC 12 Constitution saving throw gain the benefits for a long rest. All fire damage rolls have a –2. 
        Also has the effect of 
            Heavy Clouds - (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.), 
        Also has the effect of 
            High Winds (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind)`,
        `Snow (Unpleasant to travel in. All travel speed is halved. If snow occurs for two days in row, all terrain is difficult terrain and wagon travel is impossible until one day without snow passes. 
        Also has the the effect of 
            Heavy Clouds -The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage. 
        Also has the the effect of
            Freezing Cold -If you attempt to take a long rest without cover and heat, you must make a DC 15 Constitution saving throw gain the benefits for a long rest. If you fail by 5 or more, you gain an additional level of Exhaustion. All cold damage rolls have a +2. 
            Replace with Rain when in climates without snow - 
                Rain - (Unpleasant to travel in. If you have wagons, your travel pace is slowed by half. If you attempt to take a long rest without cover, you must make a DC 12 Constitution saving throw gain the benefits for a long rest. All fire damage rolls have a –2. 
            Also has the effect of 
                Heavy Clouds - The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.)`,
        `Heavy Clouds (The sky is blocked. High flying aerial creatures have total cover, and outdoor light does not count as sunlight (for the purposes of sunlight sensitivity and similar traits). Checks using Navigation Tools to determine your location based on celestial observation are made with disadvantage.)`,
        `Light Clouds (This is the game as you normally play it. Clear bright light during day time, view of the stars and moon at night. No modifiers are added to play.)`,
        `Clear Skies (This is the game as you normally play it. Clear bright light during day time, view of the stars and moon at night. No modifiers are added to play.)`,
        `High Winds (Turbulent gusts sweep across the land. Wind direction = ${searchArray(windDirection)}. Flying creatures gain +10 movement speed when moving with the wind, and –10 movement speed when moving against it. All ranged weapon attacks have a –2 to attack rolls, and their range is reduced by half when shooting into the wind)`,
        `Scorching Heat (Blistering heat that is unpleasant to travel in. Creatures that attempt to travel during day light hours require twice the ration of water, and creature that travel for 4 or more hours or engage in heavy activity for 1 or more hour during the day and do not immediately take a short or long rest under cover must make a DC 10 Constitution saving throw or gain a level of Exhaustion. All fire damage rolls have a +2. All cold damage rolls have a –2.)`,
        `Strange Phenomena - (${searchArray(strangePhenomena)})`,
    ]
    document.getElementById("weather").innerHTML = searchArray(Fall);
};
function findSurge() {
    let wildMagic = [
        "Roll on this table at the start of each of your turns for the next minute, ignoring this result on subsequent rolls", 
        "Roll a d10. Your height changes by a number of inches equal to the roll. If the roll is odd, you shrink. If the roll is even, you grow.", 
        "You cast Confusion centered on yourselfScreen reader support enabled.", 
        "You grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode out from your faceScreen reader support enabled.", 
        "Your skin turns a vibrant shade of blue. A Remove Curse spell can end this effect.", 
        "An eye appears on your forehead for the next minute. During that time, you have advantage on Wisdom (Perception) checks that rely on sight.", 
        "Roll a d10. Your age changes by a number of years equal to the roll. If the roll is odd, you get younger (minimum 1 year old). If the roll is even, you get older.", 
        "1d6 flumphs controlled by the DM appear in unoccupied spaces within 60 feet of you and are frightened of you. They vanish after 1 minute.", 
        "You turn into a potted plant until the start of your next turn. While a plant, you are incapacitated and have vulneravility to all damage. If you drop to 0 hit points, your pot breaks, and your form reverts.", 
        "A unicorn controlled by the DM appears in a space within 5 feet of you, then disappears 1 minute later.", 
        "You can't speak for the next minute. Whenever you try, pink bubbles float out of your mouth.", 
        "You are immune to being intoxicated by alcohol for the next 5d6 days.", 
        "Your hair falls out but grows back within 24 hours", 
        "For the next minute, any flammable object you touch that isn't being worn or carried by another creature bursts into flame.",
        "For the next minute your voice is very loud, as if the Thaumaturgy spell had been used on it.", 
        "You glow with bright light in a 30-foot radius for the next minute. Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn.", 
        "Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute.", 
        "Your size increases by one category size for the next minute", 
        "Your size decreases by one category size for the next minute", 
        "You are surrounded by faint, ethereal music for the next minute.", 
        "The plant nearest to you grow to twice it's size.", 
        "The horrible smell of rotting compost surrounds you in a 15 foot radius for the next minute.", 
        "Poison Ivy grows rapidly in a 10 foot radius centered on the caster. Each living creature in the radius must make a percentile roll. 1-84 causes a rash that causes -1 to all rolls for 1d4 days.", 
        "The hair of a random creature within 30 feet is turned into feathers", 
        "The caster smells like a skunk for as long as the spell lasts.", 
        "The caster shoots forth eight non poisonous snakes from his fingertips. The snakes do not attack.", 
        "A stream of butterflies pours from the caster's mouth.", 
        "The spell appears to fail when cast, but appears 1d4 rounds later.", 
        "Flowers grow in the caster's footsteps for the next 1d6 hours.", 
        "The plant nearest to you shrinks to half it's normal size.", 
        "The area around you in a 100 foot radius suddenly turns to the next season.", 
        "You cast Speak With Animals.", 
        "Small animals are drawn to the caster's location and want to be around the caster for the next 1d4 hours.",
        "The caster's feet become talons capable of grasping small objects, but they do no damage.", 
        "The Bee of Doom appears: very tiny beast, true neutral HP 1 SPEED 60 fly AC 25 natural armour Str 2 Dex 20 Con 5 Int 3 Wis 10 Cha 16 Saving throws: dexterity, wisdom sting +5, 1 point fixed piercing damage. Ignores immunity and resistance to piercing damage. Universally hostile, will fly to and attack the farthest target within range at the beginning of its turn.", 
        "The caster forgets the events of the last 1d10 hours.", 
        "The caster gains 2d20 pounds instantly .", 
        "The caster loses 2d20 pounds instantly.", 
        "The caster becomes drunk and suffers one point of exhaustion.", 
        "The caster gains darkvision for 1d4 hours.", 
        "It begins raining instantly.", 
        "A small songbird pops into existence in mid-flight 10 feet above the caster. Roll a d20. On a 1, the bird poops and it lands on the caster. On a 20, the bird poops and it lands on the target of the spell.", 
        "The caster gets the hiccups, which last for 1d6 minutes.", 
        "The caster's hair turns green for 1d8 hours.", 
        "The caster's shadow detaches from you and becomes a shadow (the creature).", 
        "The caster experienced extreme discomfort in their stomach for 1d4 turns before finally releasing a monstrous belch for another 1d4 turns. This belch functions as per the description of the spell Gust of Wind, with the direction of the wind being whichever direction the caster is facing.", 
        "Instead of the spell you wanted, a disgruntled 6 inch pixie appears, flies up to you, punches you in the forehead, sprinkles you with a dust that makes you sneeze violently, and then vanishes in a puff of neon pink and orange glitter.", 
        "The caster vomits up a huge slug after casting the spell.", 
        "The target of the spell turns into a potted plant. While a plant, a creature is incapacitated and has vulnerability to all damage. If it drops to 0 hitpoints, the pot breaks and the creature's form reverts.",
        "The caster cannot speak for 1d20 minutes.", 
        "You cast magic missile as a 5th-level spell, summoning 7 darts of magical force that deal 1d4+1 force damage each to one or several creatures of your choice.", 
        "Roll a d10. Your height changes by a number of inches equal to the roll. If the roll is odd you taste a combination of cherry tart, custard, pineapple, roast turkey, toffee and hot buttered toast, all mixed up! You also shrink. If the roll is even you taste cranberry pomegranate cake, it’s delicious and like all cake is prone to do, it makes you grow.", 
        "You seem to have forgotten what you’re doing. You cast confusion centered on yourself. ", 
        "For the next minute, you regain 5 hit points at the start of each of your turns. Your knuckles itch a little but you can’t find anything wrong with them.", 
        "You grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode out from your face.", 
        "You cast grease centered on yourself. Whoopsie!", 
        "Your skin turns a vibrant shade of blue, you grow foot long wavy antennae from your scalp and a glowing halo floats above your head for 24 hours. The halo emits light in a 5 foot radius.", 
        "An eye appears on your forehead for the next 10 minutes. During that time, you have advantage on Wisdom (Perception) checks that rely on sight. You have the strange urge to make triangle shapes with your hands.", 
        "Your hands grow strange suckers that excrete a sticky web like substance. You have advantage on climb and grapple checks but must make a Strength check to release items held. This effect persists for 24 hours.", 
        "You are transported to the Astral Plane until the end of your next turn, after which time you return to a random space that is unoccupied within 30 feet of your original space. Roll a percentage die. 01-50 and you are standing on a barren rock flying through the far reaches of space, nothing but twinkling stars and colorful  corona’s as far as the eye can see. 51-100 and you are standing in the private quarters of a Githyanki astral ship captain who is currently neck deep in pink bubbles. His eyes widen as he bellows in a startled voice “By the gods! ANOTHER ONE!” He shouts just before you pop back to your own plane of existence.",
        "Power courses through your veins as you grip a pulsing string of nether in your hand. Maximize the damage of the next damaging spell you cast within the next 10 turns.", 
        "Flip a coin! If it lands on Heads then your Charisma score changes to 20 but if it lands on tails your Charisma score becomes a 3 (ewwww). Your score reverts back to its original number in 1 minute.", 
        "A bloated hill giant corpse appears nearby. It appears to have been sitting in the sun for several days but it seems the giant’s bag is intact! If you have a copy of Storm King’s Thunder then roll 1d4 times on the “Items In A Giant’s Bag” table, if not you only find a dented metal helmet and dead sheep.  ", 
        "You turn into a potted plant until the start of your next turn. While a plant, you are incapacitated and have vulnerability to all damage. If you drop to 0 hit points, your pot breaks and your form reverts.", 
        "You suddenly grow a long, hairless blue tail that allows you to teleport up to 20 feet as a bonus action on each of your turns. The tail disappears in one minute or if severed.", 
        "Did somebody turn the gravity off? Nope, you just cast levitate on everything in a 30 foot radius. ", 
        "A unicorn controlled by the DM appears within 5 feet of you. It heals any wounds you may have and disappears in one turn.", 
        "You can’t speak for the next minute. Whenever you try, pink bubbles float out of your mouth with written text floating inside them. When you pop the bubbles the words are released!", 
        "A spectral shield hovers near you for the next minute, granting you a +2 bonus to AC and immunity to magic missiles.", 
        "You are immune to being intoxicated by alcohol for the next 1d6 days. The upside is that you can win any drinking contest without even slurring your insults!", 
        "Your hair bursts from your head and showers the ground leaving you bald. Your head itches for the next 24 hours as it quickly grows back to its normal length.", 
        "You summon an invisible humanoid that tells amazing jokes. Only you can see or hear it.", 
        "Your voice booms to 5 times its normal volume, including your breathing. You annoy people nearby and gain disadvantage on stealth checks for the next 10 minutes.", 
        "A 15 foot cone of fire explodes out in front of you; anything it hits takes 2d8 cold damage and is slowed by10 feet for until the end of their next turn.", 
        "Up to three creatures you choose within 30 feet of you take (X)d10 lightning damage. (X) is equal to the highest level of spell you are able to cast.", 
        "Whoa, why does everything have such big teeth? You are frightened by the nearest creature to you at the start of your turn for the next 5 turns.", 
        "Each creature within 30 feet of you becomes invisible for 1 minute. The invisibility ends on a creature when it attacks or casts a spell.", 
        "Your skin begins to ripple with a rainbow of colors; you gain resistance to all damage for the next minute.", 
        "You glow with a bright light in a 30-foot radius for the next minute. Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn.", 
        "You cast polymorph on yourself. If you fail the saving throw, you turn into a sheep for the spell’s duration.", 
        "Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute.", 
        "Ultimate cosmic power! Each creature within 30 feet of you takes (X)d10 necrotic damage. You regain hit points equal to the sum of the necrotic damage dealt. (X) is equal to the highest level spell slot you possess. Any excess hit points above your maximum become bonus hit points that persist for 1 hour.", 
        "You become invisible for the next 10 minutes and other creatures can’t hear you. The invisibility ends if you attack or cast a spell.", 
        "Your magical essence receives a hard reset by the universe. Your spells all become prestidigitation for the next 10 minutes, at the end of this period you regain all spent spell slots as if receiving a full nights rest.", 
        "You are surrounded by faint, ethereal music for the next minute, tiny violins float in the air about you.", 
        "Your skin crackles with arcane magic; it rushes into your pores and fills you with potential. You regain all expended sorcery points.", 
        "You change gender for one minute but retain the general body features of your original form. For example; a female with a hairy chest and full beard or a man with elegant finger nails and pig tails!", 
        "Your feet feel impossibly heavy; as a matter of fact they’re turned to stone! Your speed is halved for 1 minute.", 
        "You summon a thin green fog that fills a 60 foot area and stinks horribly. It leaves a bad taste in your mouth too.", 
        "Grass, flowers and strange plants sprout wherever you step for the next minute. Roll 1d4 and find that many magical “Goodberries” ready for harvest.", 
        "All lights, even magical, within 30 feet of you are extinguished as a gust of primal wind surrounds you momentarily, small dust flurries dance nearby for the next minute.", 
        "All of the water within 30 feet of you turns to cheap wine. All of the wine within 30 feet of you turns to water. If this occurs when you are near a body of still water then you’ve probably just caused an ecological disaster of delicious (yet probably deadly) consequences.", 
        "For the next minute your speed doubles and you gain a free standard action every turn but you must make a successful 10 Dexterity check for every action you take or you fumble it. You’re just too fast and jittery to properly control your movements!", 
        "Your stomach feels like it’s turned into a black hole! You must eat double your portion of daily food", 
        "starting on your next turn or immediately take a level of exhaustion due to starvation. You may use your bonus action to consume food each round, this ends when you have eaten 2 pounds of food or 0 speed.", 
        "A small cloud appears above your head and drizzles a cold rain on your parade. The pesky thing sticks around for 10 minutes.", 
        "Small bugs keep finding their way up your pants leg and into your shirt. They pinch and make you unable to rest easily for the next 24 hours no matter how many times you bathe.", 
        "Your hair stands on end and your hands emit a static charge dealing 1 point of damage to anything you touch for the next 24 hours.", 
        "You emit an aura of cold, chilling everyone and everything around you for 24 hours or until you bundle up in something warm for a long rest. People begin to call you “Winter” and mumble about “look who’s coming” whenever you’re near.", 
        "You take on a deathly pallor and the stench of the grave for 24 hours. Magic detects you as undead during this time and you cast no reflection or shadow for the duration.", 
        "Your eyes turn a deep violet. You gain dark vision of 120 feet and sensitivity to light for 24 hours. Why does everyone keep yelling “Drow”?", 
        "The visibility of light and dark become reversed for the caster. Darkness is bright as day and day is dark as night.", 
        "Every creature slain within 20 feet of the caster for the next 1d4 weeks animates and begins burying itself immediately upon dying.", 
        "4d20 trees within 1 mile of the caster begin producing nonmagical items as fruit.", 
        "The caster’s legs double in length and their torso shrinks to half its size.",
        "All treasure carried by the caster becomes sentient, sprouts tiny arms and legs, and tries to escape from them.", 
        "Every cricket within 10 miles of the caster no longer makes a chirping sound when rubbing their legs together, and instead makes the sound of screaming.", 
        "All foods and drinks the caster eat become either freezing cold or burning hot.", 
        "Horses within 100 miles of the caster all vanish and are replaced with wheel barrows.", 
        "Nearest squirrel gains sentience, an Intelligence score of 24, knows and can speak Deep Speech, and becomes obsessed with the caster.", 
        "The caster becomes incredibly aroused by the next person they see. This continues to occur for the next 1d10 days.", 
        "For the next 1d4 weeks, the clouds in the sky all appear to look like the caster in various embarrassing situations (i.e. beaten up by kobolds, sitting on a latrine, etc.)", 
        "A random party member or the caster themselves has their hands and feet become detachable.", 
        "The ground beneath the caster’s feat rises rapidly 30 feet into air.", 
        "The caster is compelled to repeat the last word of each sentence they speak twice.", 
        "The next person the caster touches will have their face flipped upside down.", 
        "Fish within 1,000 miles of the caster gain the ability to breath air and swim through the air like they would the water. ", 
        "Caster no longer is able to speak. Instead, when they try to talk, clouds of letters float from their mouth to form the words they wish to say.", 
        "Whenever the caster falls asleep, gravity stops affecting their body.", 
        "Objects that weight less than twenty pounds now feel as though they weight ten times as much to the caster.", 
        "The caster’s clothing becomes filled with 1d100 ladybugs.", 
        "All weapons within 50 feet of the caster appear to be normal, but when striking a creature take on the properties of harmless plastic foam.", 
        "All non-magical clothing within 50 feet of the caster turns to smoke.", 
        "The caster grows two extra mouths, one under each armpit.", 
        "The contents of the nearest lake is teleported 20 feet above the party.", 
        "The nearest paladin believes the caster to secretly be a lich.", 
        "When the caster defecates, it glows and emits a low humming sound.", 
        "Everyone within 2 miles of the caster can only speak backwards for the next 1d4 days.", 
        "The caster lays a clutch of eggs during the next extended rest. What hatches follow the caster around and treats them as their mother.", 
        "The caster smells unique to those around him. Those around him each smell their least favorite smell.", 
        "Caster's fingers and toes randomly shuffle their placements", 
        "People of the nearest town develop an intense hatred of adventurers of a random class present in the party.", 
        "A random item within 50 feet of the party ignites each morning at sunrise.", 
        "Everyone the caster sees appears to be either twice their age or half their age.", 
        "The weather and temperature within 10 miles of the caster becomes permanently stuck as the current weather and temperature occurring there.", 
        "Each NPC the party meets for the next 1d6 days has a 50% chance to be an illusion created by the wild magic surge", 
        "The caster's hair grows 1d10 inches ", 
        "All women within 5 miles of the caster instantly grow thick beards.", 
        "The caster now salivates mead", 
        "Whenever the caster lies, a lit candle tumbles from their mouth.", 
        "Every day for 1d6 weeks, a member of the party is mysteriously tripped by an unseen force each day and hears cackling laughter that only they can hear.", 
        "The caster can now communicate conversationally wi th ducks.", 
        "The next NPC the caster touches turns into a swarm of bees for 24 hours.", 
        "The caster is instantly teleported back to where they stood two minutes ago.", 
        "Whenever the caster coughs, sniffs, or makes some other simple au bodily", 
        "All plant life within 20 feet of the caster immediately grows by 4d4ft", 
        "Caster gains the ability to walk on water, but only for the first six steps.", 
        "The caster's eyeballs disappear and reappear each time that they blink.", 
        "The nearest large body of water is turned to pudding", 
        "A large, metal statue of the caster falls from the sky.", 
        "The nearest townss inhabitants are all transformed into chickens, but are all in denial of this fact and continue about their business as normal.", 
        "The caster is sent back in time 1d20 hours. Make sure your DM is okay with this one!", 
        "The party is plagued by voices in their head. The voice sounds exactly like each PC’s mother and criticizes and chastises everything they do for 1d4 weeks. Things such as, “Oh, why would you kill that poor goblin? What did he do to you?” and, “You need to wipe your feet before going into an inn! Where are your manners?”", 
        "Whenever the caster is hurt, a blast of confetti shoots out of their ears, accompanied by the sound of a party noise maker.", 
        "Every goblin within 100 miles gains a deep understanding of fine wines and high society.", 
        "The solar and lunar cycles reverse (sun/moon rises in the west and sets in the east.).", 
        "The caster’s skin becomes covered in bright polka dots. ", 
        "The nearest nobility/royalty is convinced that the party has stolen something of importance from them.", 
        "The caster and the next party member they speak to swap minds. Exchange all mental scores, but keep all physical scores. They swap back after 1d10 days.", 
        "The nearest town loses the ability to speak and becomes proficient in interpretive dance.", 
        "The caster’s pockets become filled with honey.", 
        "The caster experiences particularly severe flatulence for 1d4 days, though the scent is of fresh-cut spring flowers rather than… the usual scent of flatulence.", 
        "Storm clouds form in the area and rain down upon the land. The rain isn’t water however, instead it is melted butter. ", 
        "Natural beasts within 10 miles quadruple in size instantly. This does not affect druids that have transformed with Wild Shape.", 
        "The caster gains the ability to pass through walls, but only 50% of the way. They become stuck if they try to move further forward.", 
        "The next creature to come in physical contact with the caster becomes instantly covered in black, sticky tar.", 
        "The nearest cleric develops an insatiable appetite for dirt.", 
        "The caster discovers that their nose has become detachable.", 
        "The next item the caster touches becomes stuck to their hand as though held there by Sovereign Glue (see Dungeon Master’s Guide). However, it may be removed by Dispel Magic or Remove Curse. ", 
        "The caster gains eat vision. By staring at food or drink, they can focus their energy and eat/drink it from up to 100 feet away. While using this ability, their eyes glow white and there is a faint smell of burning flesh around them.", 
        "The nearest tree to the caster takes off into the sky like a rocket until it reaches 5,000 feet above the ground, then promptly falls. ", 
        "The caster’s hair writes like snakes and gains nerves so that they feel pain whenever they are cut. If they have no hair, they grow hair as well! ", 
        "A squad of modrons appear and begin performing a musical symphony for the party. When they finish, they leave immediately.", 
        "An extra arm sprouts from the caster’s forehead and lasts for 1d4 days before vanishing with a loud pop. It is devoted to playing practical jokes on the caster or causing them general (though non life threatening) distress. Things like covering their eyes, giving wet willies, etc.", 
        "All weapons within 50 feet of the caster leap from their owner’s hands and bury themselves 5 feet into the ground.", 
        "The nearest allied PC becomes certain that the party is being stalked by an ancient red dragon.", 
        "The caster’s teeth all begin screaming, and continue doing so for 1d8 days.", 
        "Creatures within 100 feet of the caster and the caster themself emit bright light", 
        "The sun and moon both gain large, menacing smiles. These are visible to those who look closely enough.", 
        "The caster’s boots now squeak like mice with every step they take.", 
        "Whenever the caster speaks it is in rhyme. If they attempt to speak in anything but rhyme, the cr eatures around them only hear the sound of static", 
        "The caster becomes un able to walk in a straight line , as if permanently drunk", 
        "The caster becomes invisible but only while sneezing.", 
        "Whenever the caster enters a building, the amount of light available dims to darkness and then a spotlight of bright light appears around the caster (accompanied with trumpet sounds). Then the light returns to normal immediately afterward.", 
        "All food within 20 feet of the caster now attracts bees from up to 10 miles away.", 
        "The nearest evil aligned creature believes the party to be their greatest foe.", 
        "The nearest f ield of crop s animates and rises up against the farmer s of the region", 
        "All wheels within 1 mile morph into square shapes.", 
        "Whenever the caster is silent, an audible ticking sound can be heard emanating from inside their chest.", 
        "The nearest huge creature finds that they absolutely need to hug out their problems with ever yone they meet; much to the smaller creatures dismay!", 
        "Every night when the party rests, while they sleep their body slowly sinks into the ground, forming a small hole around them as the dirt magically moves aside. The hole gets 1 foot deeper per hour of sleep. ", 
        "Each spell cast by the caster now also summons a duck under the DM s control.", 
        "The next NPC the party speaks to will begin shrinking slowly the longer they converse with them", 
        "The caster s gender swaps.", 
        "For the next 1d8 days, the region experiences weather opposite of the current season.", 
        "All coins held by the party turn into platinum for the next 1d4 days, the return to their original state.", 
        "Half of the caster s body triples in age, while the other half becomes three times as young as their current age", 
        "All creatures within a 30 foot radius vanish and then reappear at the center stacked atop one another in a random order.", 
        "The moon becomes invisible. ", 
        "The nearest king abdicates their throne to live as a peasant on a homestead in the country", 
        "The caster becomes aware of the fact that they are actually just a fictional character in a role playing game for the next 1d4 hours , and then they magically forget this fact . Enjoy this short existential crisis!", 
        "Whenever anyone in the party fails their first death saving throw, a wooden coffin magically appears around them to hold their body. On a second fail, funeral flowers in vases appear around the coffin. On a final failed save, a priest appears and begins giving a eulogy (has the stats of a commoner), then disappears once finished.", 
        "The caster’s eyes bulge an inch out of their skull.", 
        "Every male within 1 mile instantly goes bald.", 
        "The caster’s shadow becomes blue. ", 
        "The nearest party member to the caster gains 100 pounds in body weight.", 
        "The nearest dwarf has their limbs stretch so that they are the same height as an elf, though their torso and head do not change to be proportionate.", 
        "All mice in the area gain the ability to run at Mach 2.", 
        "Plants within a 1 mile of the caster begin growing downward instead of upward and no longer need sunlight in order to survive.", 
        "The nearest ally of the caster finds that every time they attempt to grab their weapons that they turn into slugs. The slugs will then reform into their weapon when the affected ally leaves the weapon alone.", 
        "The party and anyone they are engaged with (combat, dialogue, etc.) find that time has skipped and that it is now the following day.", 
        "The next body of water the party finds freezes whenever they interact with it.", 
        "When spilled, the caster’s blood takes on the taste and consistency of ketchup.", 
        "The nearest NPC or enemy creature becomes two dimensional.", 
        "The nearest allied PC to the caster can speak to animals permanently, but only knows how to say the phrases, “Hello”, “Goodbye”, “Where is the bathroom?”, and “Nice weather we are having.” They can understand the animals responses perfectly however.", 
        "When the caster is knocked unconscious, their body stands, and begins dancing and singing show tunes. The caster has no memory of this when they regain consciousness.", 
        "The nearest wild animal’s fur coat turns to gold and the animal can now shift between the material and ethereal planes as a bonus action.", 
        "The caster’s eyes become hollow and filled with water. A small gold fish can be seen swimming in each. This does not negatively affect their vision in anyway, besides the fact that sometimes a bubble or two from the fish my float in front of their eyes (purely cosmetic and flavor though).", 
        "The caster becomes permanently charged with static electricity, such that everyone they touch receives a painful (though mostly just annoying) shock whenever they touch the caster or the caster touches them.", 
        "The caster’s body hair is replaced with strands of wet spaghetti.", 
        "The next door the party opens leads to a bottomless pit rather than where it typically should.", 
        "Whenever the caster sneezes, they discharge from their nose/mouth a random, harmless, elemental effect", 
        "The nearest settlement begins using peanut butter as currency.", 
        "The caster finds themselves unable to speak unless they end what they say with the phrase, All will be one.", 
        "The nearest allied PC without a fly speed gains a fly speed of 5, but only when they flap their arms.", 
        "Black smoke pours from the caster's nose constantly, though not in a high enough quantity to obscure vision.", 
        "The caster's body permanently vibrates. 27 Whenever the caster s teeth touch each other, there is a burst of sparks from their mouth.", 
        "Humanoids within 50 feet of the caster begin disgorging frogs from the various orifices of their bodies This continues for 1d12 hours or until 1d1000 frogs have been disgorged (DM s choice of course).", 
        "A small rift in space appears randomly within 1 mile of the caster and serves as a gateway to and from the Astral Sea.", 
        "The next person the caster looks at gains a very noticeable lisp.", 
        "All leaves of plants within 10 miles become vibrant neon colored. This does not negatively affect the plants in any way.", 
        "The nearest ally's head swells up like a balloon and then pops, spraying candy in a 15 foot radius around them. Their head regrows to its normal size instantly afterward and the ally suffers no physical harm from this.",
        "The caster or a random ally within 100 feet gets amnesia for 1d10 hours every time they find treasure.", 
        "One of the caster's items cannot be found by them, no matter how hard they look.", 
        "The caster's pants become infested with skunks.", 
        "The caster finds that all the hair on their head has migrated to their back.", 
        "The nearest NPC splits into two copies of themselves One is chaotic evil and the other is lawful good. Both are convinced that they are the original and the other is an imposter.", 
        "The nearest dragon begins giving their hoard to charity, though once all their treasure is gone they lose this feeling of generosity and will certainly want their hoard back.", 
        "The nearest woman becomes pregnant with a clone of the caster.", 
        "Vines sprout from the ground and restrain any creatures in a 30 foot sphere centered on the caster. They can be cut away with two attack actions.", 
        "The floor/ground within 200 feet becomes lava, or at least behaves like it when touched for the next 1d6 minutes. A creature touching it will take 1d10 fire dam age As long as a creature is not touching the floor/ ground, they are safe from this damage.", 
        "The temperature in a 20 foot sphere around the caster is 20F hotter than the rest of the area.", 
        "A random creature within 30 feet of the caster has a small rain cloud form above their head that commences to precipitate piles of dung which fall upon the creature for the next 1d12 minutes.", 
        "The caster feels searing pain whenever they put clothing on (though they are not physically harmed by this).", 
        "A random bone in the caster's arm or leg becomes elastic", 
        "The nearest mop gains the properties of a Vorpal Sword for the next 1d4 weeks.", 
        "Every other day , the caster loses one of their five senses. It returns the next day at dawn.", 
        "A random PC becomes insubstantial while under the light of a full moon. ", 
        "Whenever the caster receiving healing, slugs crawl out of their nose and attempt to go in the caster's mouth.", 
        "The nearest peasantry begins a revolution against the nobility.", 
        "A random microbial organism within 50 feet becomes Large in size.", 
        "All birds within 1 mile turn inside out", 
        "The caster's clothing gains a desire to consume the flesh of humanoids and attempts to devour them.", 
        "All creatures within a 100 foot sphere centered on the caster become contained in glass jars with labels that show their stats. The jars are large enough that the creatures have free movement within their respective jars and the jars have 5 AC and 10 HP.", 
        "The caster s heart pumps 50 times louder when they are afraid.", 
        "Whenever the caster is within 5 feet of common household objects they begin to levitate and follow the caster around.", 
        "When the caster is slain, all creatures within 100 feet weep uncontrollably for 1 minute",
        "Whenever the caster lifts their right arm, a trout materializes and leaps from their armpit.", 
        "A random shoe within 20 feet of the caster gains the properties of a bag of holding. It loses these properties and expels its contents after the next full moon.", 
        "The nearest princess/prince teleports into the caster's arms. 61 A random PC becomes obsessed with cleaning a particular object or part of their body.", 
        "The caster gains a soundtrack for their life. As they go about their business, thematically appropriate music plays loudly enough for those around to hear, but not so loud that it impedes communication between the caster and others.", 
        "The nearest field of crops yields wax versions of their produce rather than healthy, edible food.", 
        "The nearest kobold becomes omniscient.", 
        "An elderly dwarven wo man appears dressed as a school marm . She proceeds to teach a lesso n to the party as if they were children about why mountains are big.", 
        "For the rest of the current encounter, or the next encounter the PC s face, the encounter is accompanied by a disembodied voice giving a play by play.", 
        "A random ally of the caster believes that the caster is actually a doppelganger.", 
        "The next NPC the caster touches begins to turn to stone.", 
        "Each time the caster tells a lie they grow a finger on a random part of their body.", 
        "All wild game within 1 mile become made of balloons, but are otherwise unharmed and continue to function as normal. ", 
        "The next creature the PC s behead spays candy from its wound.", 
        "The caster becomes naturally intoxicated and alcohol now has a sobering effect on them.", 
        "Each step the caster takes causes a small, (mostly harmless) burst of magical energy from beneath their feet that cycle s through the following types: fire, cold, acid, and lightning", 
        "The sky darkens and lightning flashes. A deep roar echoes through the area and then a voice speaks in draconic, saying, Soon, you shall know my name and I shall consume thee. After this the region returns to normal, and nothing else out of the ordinary occurs ", 
        "When the caster awakens from sleeping, their voice goes up an octave every hour until they sleep again. When they sleep their voice resets to w hat it normally sounds like.", 
        "A small parrot appears and begins following them around and annoyingly copying phrases the party says. The parrot has a mocking tone and if killed, resurrects 1 minute later and resumes its copying.", 
        "The next spell the caster casts has the opposite effect. The way the spell manifests is up to the DM. For example, the spell Fireball may instead be a ball of ice and do cold damage, or perhaps instead the spell heals the creatures in burst instead of damaging.", 
        "The next item the caster touches replicates instantly until there are 4 copies of the original. It is impossible to distinguish which is the original. The copies function normally for 1d6 days, and then turn into strawberry jelly, leaving only the original", 
        "The area within a ½ a mile of the caster becomes covered in banana peels. ", 
        "The caster gains the ability to unhinge their jaw like a snake. Their nose also shrinks until i t is just two slits in their face, giving them a reptilian look. ", 
        "The caster gains the ability to see into the future, but only when it concerns a particular mundane item in their possession , such as a shoe or candle. For exa mple, the player may see a vision of their party being sl ain by bandits if these bandits, through their attack on the party, wou ld interact with the candle in some fashion damaging it o r stealing it)", 
        "The nearest horse grows the wings of a Pegasus but cannot fly whatsoever. ", 
        "All glass within 1 mile of the caster reflects their image within it for 1 minute and then shatters with a loud crash.", 
        "The caster grows a second face on the back of their head. This face has its own conscience separate of that from the caster. It has no soul, though appears to have one should anyone examine it or question it.", 
        "A random PC within 30 feet of the caster begins sprouting roots from their feet which then begin burrowing into the ground. This occurs whenever they stay still for more than 1 minute (unless they are sleeping).", 
        "A random PC is teleported 1,000 feet from the party and buried in the ground up to their head in fresh soil. They also find a smal l metal spoon in their mouth, which they may of course use to dig themselves out. ", 
        "A goblin appears and claims to be the slave of the caster. The goblin will not under any circumstance leave the caster s side.", 
        "A scroll appears at the feet of the caster. Written on the scroll is some mundane, though intere sting prediction of the future, such as the weather for the next month or when the local villagers will bear children. ", 
        "The nearest blacksmith crafts a sentient item which calls out to one or more of the PC s to be found and wielded.", 
        "The PCs become magically compelled to travel in a conga line whenever they are not in combat. ", 
        "No matter how hard the caster tries, they can not satisfy a n itch on their foot. They become increasingly obsessed with this to the point of absurdity.", 
        "The nearest rogue gains a flair for theatrics and canno t help but leave a calling card whenever they do something nefarious from now on.", 
        "The caster finds they can only fall asleep while standing on their head.", 
        "The nearest town develops a cult like fanaticism for one the party members and begins a religion around them.",
        "For the next 1d6 hours, the caster's bones all vanish. They are otherwise unharmed by this.", 
        "The ground begins swelling beneath the caster's feet. This continues over the next 1d10 days until a mountain has formed at the location where this surge first occurred ", 
        "The caster becomes terribly allergic to a common creature or item found in the region. Whenever they sneeze as a result of this allergy, they produce a small puff of flame.", 
        "Tattoos appear and cover a random PCs body. They swirl and move about their skin as time goes on, appearing to be alive.", 
        "All mundane weapons and armor within 50 feet of the caster begins floating and ascends into space over the next 1d8 rounds.", 
        "A random item in the partys inventory g ains the same properties of a magic item from the Dungeon Master s Guide (DM's choice which item and the magic it gains", 
        "Roll on this table at the start of each of your turns for the next minute, ignoring this result on subsequent rolls.", 
        "A spectral shield hovers near you for the next minute, granting you a +2 bonus to AC and immunity to Magic Missile.", 
        "For the next minute, you can see any invisible creature if you have line of sight to it.	", 
        "You are immune to being intoxicated by alcohol for the next 5d6 days.", 
        "A modron chosen and controlled by the DM appears in an unoccupied space within 5 feet of you, then disappears I minute later.	", 
        "Your hair falls out but grows back within 24 hours.", 
        "You cast Fireball as a 3rd-level spell centered on yourself.	", 
        "For the next minute, any flammable object you touch that isn't being worn or carried by another creature bursts into flame.", 
        "You cast Magic Missile as a 5th-level spell.	", 
        "You regain your lowest-level expended spell slot.", 
        "Roll a d10. Your height changes by a number of inches equal to the roll. If the roll is odd, you shrink. If the roll is even, you grow.	", 
        "For the next minute, you must shout when you speak.", 
        "You cast Confusion centered on yourself.	", 
        "You cast Fog Cloud centered on yourself.", 
        "For the next minute, you regain 5 hit points at the start of each of your turns.	", 
        "Up to three creatures you choose within 30 feet of you take 4d10 lightning damage.", 
        "You grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode out from your face.	", 
        "You are frightened by the nearest creature until the end of your next turn.", 
        "You cast Grease centered on yourself.	", 
        "Each creature within 30 feet of you becomes invisible for the next minute. The invisibility ends on a creature when it attacks or casts a spell.", 
        "Creatures have disadvantage on saving throws against the next spell you cast in the next minute that involves a saving throw.	", 
        "You gain resistance to all damage for the next minute.", 
        "Your skin turns a vibrant shade of blue. A Remove Curse spell can end this effect.	", 
        "A random creature within 60 feet of you becomes poisoned for 1d4 hours.", 
        "An eye appears on your forehead for the next minute. During that time, you have advantage on Wisdom (Perception) checks that rely on sight.	", 
        "You glow with bright light in a 30-foot radius for the next minute. Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn.", 
        "For the next minute, all your spells with a casting time of 1 action have a casting time of 1 bonus action.	", 
        "You cast Polymorph on yourself. If you fail the saving throw, you turn into a sheep for the spell's duration.", 
        "You teleport up to 60 feet to an unoccupied space of your choice that you can see.	", 
        "Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute.", 
        "You are transported to the Astral Plane until the end of your next turn, after which time you return to the space you previously occupied or the nearest unoccupied space if that space is occupied.	", 
        "You can take one additional action immediately.", 
        "Maximize the damage of the next damaging spell you cast within the next minute.	", 
        "Each creature within 30 feet of you takes 1d10 necrotic damage. You regain hit points equal to the sum of the necrotic damage dealt.", 
        "Roll a d10. Your age changes by a number of years equal to the roll. If the roll is odd, you get younger (minimum 1 year old). If the roll is even, you get older.	",
        "You cast Mirror Image.", 
        "1d6 flumphs controlled by the DM appear in unoccupied spaces within 60 feet of you and are frightened of you. They vanish after 1 minute.	", 
        "You cast Fly on a random creature within 60 feet of you.", 
        "You regain 2d10 hit points.	", 
        "You become invisible for the next minute. During that time, other creatures can't hear you. The invisibility ends if you attack or cast a spell.", 
        "You turn into a potted plant until the start of your next turn. While a plant, you are incapacitated and have vulnerability to all damage. If you drop to 0 hit points, your pot breaks, and your form reverts.	", 
        "If you die within the next minute, you immediately come back to life as if by the Reincarnate spell.", 
        "For the next minute, you can teleport up to 20 feet as a bonus action on each of your turns.	", 
        "Your size increases by one size category for the next minute.", 
        "You cast Levitate on yourself.	", 
        "You and all creatures within 30 feet of you gain vulnerability to piercing damage for the next minute.", 
        "A unicorn controlled by the DM appears in a space within 5 feet of you, then disappears 1 minute later.	", 
        "You are surrounded by faint, ethereal music for the next minute.", 
        "You can't speak for the next minute. Whenever you try, pink bubbles float out of your mouth.	", 
        "You regain all expended sorcery points.", 
        "A fireball explodes with you at the center. You and each creature within 20 feet of you who must make a Dexterity saving throw using your spell save DC, taking 5d6 fire damage on a failed save, or half as much damage on a successful one.", 
        "For the next day, your skin tone changes color every 30 minutes, cycling through the colors of the rainbow.", 
        "A puddle of grease appears where you are standing, with a 10-foot radius. You and anyone within 10 feet of you must make a Dexterity check at your spell save DC or fall prone.", 
        "You recover all your expended spell slots.", 
        "You are confused for 1 minute, as though you were affected by the confusion spell.", 
        "You levitate 6 inches off the ground for 1 minute.", 
        "You lose the ability to hear for 1 day.", 
        "Your Strength is increased by 2 for 1 day.", 
        "You gain tremorsense with a range of 30 feet for 1 minute.", 
        "Each creature within 30 feet of you takes 1d10 necrotic damage. You regain hit points equal to the sum of damage dealt.", 
        "A third eye appears in your forehead, giving you advantage on sight-based Wisdom (Perception) checks for 1 minute.", 
        "You make no sounds for 1 minute and you gain advantage on any Dexterity (Stealth) checks.", 
        "You teleport to an alternate plane, then return to the location where you started after 1 minute.", 
        "The next spell you cast within the next minute that does damage, the damage is maximized.	", 
        "You grow a beard made of feathers, which remains until you sneeze.", 
        "You transform into a large empty barrel for 1 minute, during which time you considered petrified.", 
        "For the next minute, you can teleport up to 20 feet as part of your movement on each of your turns.	", 
        "You can't speak for 1 minute. When you try, pink bubbles float out of your mouth.", 
        "You are at the center of a darkness spell for 1 minute.", 
        "You become intoxicated for 2d6 hours.", 
        "You are immune to intoxication for the next 5d6 days.", 
        "You are frightened by the nearest creature until the end of your next turn.", 
        "Your Intelligence is decreased by 2 for 1 day.", 
        "You recover your lowest-level expended spell slot.", 
        "You are resistant to all damage types for 1 minute.	", 
        "Your Wisdom is increased by 2 for 1 day.", 
        "For the next minute, you must shout when you speak.", 
        "A random creature within 60 feet of you is poisoned for 1d4 hours.	", 
        "For 1 minute, any flammable item you touch, that you aren't already wearing or carrying, bursts into flame.	", 
        "Illusory butterflies and flower petals flutter in the air around you in a 10-foot radius for 1 minute.", 
        "Make a Wisdom saving throw against your own spell save DC. If you fail, you are polymorphed into giant dragonfly for 1 minute.", 
        "Plants grow around you and you are restrained for 1 minute.", 
        "You cast mirror image on yourself, which lasts for 1 minute and does not require concentration.", 
        "Up to three creatures you choose within 30 feet of you take 4d10 lightning damage.	", 
        "A random creature within 30 feet of you gains a flying speed equal to its walking speed for 1 minute.	", 
        "You are surrounded by faint, ethereal music for 1 minute.", 
        "You immediately gain 20 temporary hit points.", 
        "You may immediately take 1 additional action.", 
        "You regain all expended sorcery points.", 
        "You teleport up to 60 feet to an unoccupied space that you can see.", 
        "If you fall within the next day, you automatically have the benefit of the feather fall spell.", 
        "Your hair grows to double its current length over the next minute.", 
        "You are the center of a silence spell for 1 minute.", 
        "You recover 1 expended spell slot of your choice.", 
        "Your hair falls out but grows back within 1 day.", 
        "You are vulnerable to fiends for 1 hour. Such creatures gain advantage on attack rolls made against you.", 
        "For the next spell you cast within 1 minute that does damage, the damage is minimized.", 
        "You gain the ability to speak one additional language of your choice for 1 hour.", 
        "For the next day, any time you make an ability check, roll 1d6 and subtract the result.", 
        "You have are surrounded by a spectral shield for 1 minute, giving you a +2 bonus to your AC and immunity to magic missile.", 
        "You are invisible for 1 minute.", 
        "For any spell that requires a saving throw you cast within the next minute, the target gains advantage.", 
        "You and all creatures within 30 feet of you gain vulnerability to piercing damage for 1 minute.", 
        "Your eyes permanently change color. If they are a blue or grey shade, they turn dark brown, or vice versa. A spell such as remove curse can end this effect.", 
        "The next single target spell you cast within the next minute must target one additional target.", 
        "For 1 minute, you gain resistance to nonmagical bludgeoning, piercing, and slashing damage.", 
        "Small birds flutter and chirp in your vicinity for 1 minute, during which time you automatically fail any Stealth check.", 
        "A demon whose CR is equal to your level appears near you. Make a Charisma saving throw against your spell save DC. If you make it, the demon is subservient, otherwise, it is hostile. The demon, if not banished or defeated, vanishes after 1 day.", 
        "You are protected from Elementals for 1 hour. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "You feel the incredible urge to relieve yourself. Until you do, your Strength and Intelligence are reduced by 1. If you don't relieve yourself in the next 2 minutes, the above effects are removed, but your Charisma score is reduced by 4 for 1 hour or until you change your trousers.", 
        "For the next minute, every creature within 60 feet of you that hears you speak only hears insults as if you are casting vicious mockery at first level.", 
        "For the next minute, one creature of your choice gets a -2 penalty to its AC, attack rolls, and damage rolls.", 
        "Gnats buzz around your head for 1 minute, distracting you. You must make a Constitution saving throw against your own spell save DC to cast any spell.", 
        "For the next day, you have advantage on the next 2d6 rolls you make where you don't already have advantage.", 
        "You and all creatures within 30 feet of you gain vulnerability to bludgeoning damage for 1 minute.", 
        "You are surrounded by a faint, offensive odor for 1 minute. You gain disadvantage on all Charisma checks.", 
        "You are protected from Aberrations for 1 day. Such creatures cannot attack you or harm you unless they save a Charisma saving throw against your spell save DC.", 
        "You emanate light in a 30-foot radius for 1 minute. Any creature within 5 feet of you that can see is blinded until the end of its next.", 
        "For the next minute, all spells with a casting time of 1 action or 1 bonus action require 2 consecutive actions to cast.", 
        "For 1 minute, a duplicate of yourself appears in the nearest open space which can take actions independently, and goes on the same Initiative as you. However, any damage it takes as well as any spell slots or sorcery point it uses applies to you as well.", 
        "For the next hour, you gain advantage on Charisma checks when dealing with any creature wearing black, but disadvantage if they are wearing white. If they are wearing both, this doesn't apply.", 
        "You have the irresistible urge to scratch an itch in the middle your back, just out of reach, for 1 minute. If you don't scratch it using a back scratcher or some similar device , you must succeed a Constitution saving throw against your spell save DC to cast a spell.", 
        "A loud boom emanates from you. All creatures within 15 feet take 2d8 thunder damage and must make a Constitution saving throw against your spell save DC or be deafened for 1 minute.", 
        "You are protected from Plants for 1 hour. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "You have a momentary vision of your own death. If you fail a Wisdom saving roll at your spell DC, you are frightened for 1 minute.", 
        "All creatures within 60 feet of you regain 2d8 hit points.", 
        "Your Intelligence is increased by 2 for 1 day.", 
        "Your Charisma is increased by 2 for 1 minute.", 
        "You transform into a marble statue of yourself for 1 minute, during which time you are considered petrified.", 
        "Within the next hour, you have advantage on the next roll you make where you don't already have advantage.", 
        "Over the next minute, all plants within 20 feet of you grow as if affected by the plant growth spell when cast as an action.", 
        "You are immune to disease for 1 week.", 
        "You gain a +2 bonus to your AC for 1 minute.", 
        "Your eyes glow red for 1 minute.", 
        "You immediately drop to 0 hit points.", 
        "For the next minute, you are in the Border Ethereal near the location you were last in.", 
        "Your Constitution is increased by 2 for 1 minute.", 
        "Make a Wisdom saving throw against your own spell save DC. If you fail, you are transformed into a raven for 1 minute, as if by a polymorph spell.", 
        "For the next minute, you gain resistance to thunder and force damage.", 
        "You add your proficiency bonus to all Charisma checks for the next hour, if you don't already add it.", 
        "You are protected from Beasts for 1 day. Such creatures cannot attack you or harm you unless they save a Charisma saving throw against your spell save DC.", 
        "An imp appears within 30 feet of you. Make a Charisma saving throw against your spell save DC. If you succeed it, the imp is subservient, otherwise, it is hostile. The imp, if not banished or defeated, vanishes after 1 day.", 
        "Your spell components seem to have been rearranged. During the next hour, you must make an Intelligence check against your spell save DC to cast any spell that requires a material component.", 
        "You transform into a stuffed toy resembling yourself for 1 minute, during which time you are considered petrified.", 
        "For the next minute, you gain resistance to fire and cold damage.", 
        "For the next minute, you have advantage on the next roll you make where you don't already have advantage.", 
        "You stand at the center a circular wall of fire with a radius of 15 feet. Any creature in any of the spaces covered by this fire must make a Dexterity saving throw against your spell DC or take 5d8 fire damage.The wall of fire remains for 1 minute.", 
        "For the next hour, you gain advantage on Charisma checks when dealing with any creature wearing red, but disadvantage if they are wearing green. If they are wearing both, this doesn't apply.", 
        "Every creature within 15 feet of you takes 1 necrotic damage. If you are wounded, you regain hit points up to the amount of damage dealt. If you are not wounded, you gain this amount of temporary hit points.", 
        "Choose 1 permanent or triggered effect that has happened to you or somebody else that you’ve received from this chart and remove it, even if it was beneficial.", 
        "You gain the service of an arcane eye for 1 minute that does not require concentration.", 
        "A magic mouth appears on a nearby wall or flat surface. When you speak, your voice comes from the magic mouth. This lasts for 1 minute.", 
        "You are vulnerable to Beasts for 1 hour. Such creatures gain advantage when attacking you.", 
        "You lose the ability to smell for 1 day.", 
        "You can hear exceptionally well for 1 minute, gaining advantage for all Perception checks related to sound.", 
        "You permanently lose the ability to smell. This sense can be restored with a spell that removes curses such as remove curse.", 
        "You gain a -2 penalty to your AC for 1 minute.", 
        "You lose the ability to smell for 1 hour.", 
        "You are vulnerable to Celestials for 1 hour. Such creatures gain advantage when attacking you.", 
        "You and all creatures within 30 feet of you gain vulnerability to necrotic damage for 1 minute.", 
        "For the next day, each time you say a word with the 's' sound, it sounds like a hissing snake.", 
        "Make a Wisdom saving throw against your spell save DC. If you fail, you are transformed into a cat for 1 minute, as if by a {5e|Polymorph}} spell.", 
        "You become invisible and silent for 1 minute.", 
        "A gentle gust of wind blows outward from you. All creatures within 40 feet of you can feel it, but it otherwise does nothing.", 
        "You are vulnerable to Plants for 1 hour. Such creatures gain advantage when attacking you.", 
        "Your Dexterity is increased by 2 for 1 day.", 
        "Your Dexterity is increased by 2 for 1 minute.", 
        "You gain the service of an arcane eye for 1 hour that does not require concentration.", 
        "You can detect the thoughts of 1 creature you can see within 30 feet of you for 1 minute.", 
        "You immediately take 1d10 radiant damage.", 
        "You are protected from Celestials for 1 day. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "For the next minute, all melee attacks you make with a non-magical weapon gain a +1 bonus to hit and to damage, and are considered magical for the purpose of overcoming resistances.", 
        "One randomly-chosen non-magical item in your possession that weighs 1 pound or less vanishes and is forever gone.", 
        "You transform into a medium-sized potted plant for 1 minute, during which time you are considered petrified.", 
        "Your Strength is decreased by 2 for 1 hour.", 
        "Your Wisdom is increased by 2 for 1 minute.", 
        "3d6 random gems appear near you, worth 50gp each.", 
        "You gain freedom of movement for 1 day.", 
        "You immediately gain 10 temporary hit points.", 
        "All allies within 20 feet of you gain a +2 bonus to attack and damage rolls on any melee weapon attack they make within the next minute.", 
        "Your Dexterity is decreased by 2 for 1 hour.", 
        "3d6 silver pieces appear near you.", 
        "For 2d6 days, you glow bright yellow. You have disadvantage on Stealth checks and anyone trying to perceive you has advantage on their Perception check.", 
        "You are affected by a faerie fire spell for 1 minute. You automatically fail the saving throw.", 
        "You regain 5 hit points per round for 1 minute.", 
        "You stand at the center a circular wall of force with a radius of 15 feet. Any creature in any of the spaces covered by this wall must make a Dexterity saving throw against your spell DC or take 5d8 force damage. The wall remains for 1 minute.", 
        "You are protected from Beasts for 1 hour. Such creatures cannot attack you or harm you unless they succeed a Charisma saving throw against your spell save DC.", 
        "An imp appears near you. Make a Charisma saving throw against your spell save DC. If you succeed, the imp is subservient, otherwise, it is hostile. The imp, if not banished or defeated, vanishes after 1 hour.", 
        "All creatures within 20 feet of you are knocked prone.", 
        "3d6 gold pieces appear near you.",
        "Your speed is increased by 10 feet for 1 minute.", 
        "You are vulnerable to Aberrations for 1 hour. Such creatures gain advantage when attacking you.", 
        "For 2d6 hours, you have a faint pink glow. Anyone trying to perceive you has advantage on their Perception check.", 
        "You gain proficiency on all Strength checks for the next hour, if you don’t already have it.", 
        "For the next day, you are in the Border Ethereal near the location you were last in.", 
        "You gain the ability to breath water for 1 day.", 
        "Your Intelligence is increased by 2 for 1 minute.", 
        "All allies within 20 feet of you gain a +2 bonus to attack and damage rolls on any ranged weapon attack they make within the next minute.", 
        "You and all creatures within 30 feet of you gain vulnerability to slashing damage for 1 minute.", 
        "One randomly-chosen non-magical item in your possession that weighs 1 pound or less is duplicated.", 
        "You are at the center of a 10-foot radius antimagic field that negates all magic equal to or less than your level for 1 hour and does not require concentration.	For the next minute, light and darkness quickly alternate around you in a 30-foot radius, creating a strobe effect.", 
        "Sight-based creatures gain a -1 penalty on attack rolls against you and Perception checks against you, and you gain a +1 bonus to Stealth checks.", 
        "Mushrooms sprout around you in a 5-foot radius and vanish after 1 minute. If one is harvested and eaten within this time, the creature must make a Constitution saving throw against your spell save DC. On a failed save, it takes 5d6 poison damage. On successful one, it gains 5d6 temporary hit points.", 
        "Make a Wisdom saving throw against your spell save DC. If you fail, you are transformed into a wolf for 1 minute, as if by a polymorph spell.", 
        "All creatures within 20 feet of you must make a Strength saving throw against your spell save DC or be knocked prone.", 
        "You can smell exceptionally well for 1 minute, gaining blindsight with a radius of 10 feet and advantage on all Perception checks related to odor.", 
        "You are protected from Elementals for one day. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "You are protected from Undead for one hour. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "Your feet sink into the ground, making you completely immobile for one minute. This has no effect if you were not standing on the ground when the spell was cast.", 
        "All of your hair permanently falls out. Only a spell such as remove curse can end this effect.", 
        "For the next minute, you can pass through any solid, non-magical wall that is 6 or fewer inches thick.", 
        "One random gem worth 100gp appears near you.", 
        "You gain the ability to speak one new language of your choice. However, you lose the ability to speak one language you already know.", 
        "You are protected from Fiends for one hour. Such creatures cannot attack you or harm you unless they succeed on a Charisma save against your spell save DC.", 
        "For the next minute, you have double vision. This gives you disadvantage on ranged attacks (including spell attacks) and Perception checks involving sight.", 
        "A 30-foot cube hypnotic pattern appears with you at the center. All creatures within the pattern must succeed on a Wisdom saving throw or fall asleep for 1 minute or until they take damage.", 
        "You permanently gain one 1st-level spell slot but forget one cantrip that you already know. A spell such as remove curse can end this effect.", 
        "You are surrounded by a faint, pleasant odor. You gain advantage on all Charisma checks you make within the next minute.", 
        "You permanently forget one cantrip. A spell such as remove curse can restore your memory.", 
        "You immediately gain 15 temporary hit points.", 
        "You lose proficiency on all skill checks for 1 minute.", 
        "You immediately take 2d10 psychic damage.", 
        "All gold you are carrying is now silver.", 
        "You gain freedom of movement for 1 minute.", 
        "You are vulnerable to Undead for 1 hour. Such creatures gain advantage when attacking you.", 
        "For the next minute, you gain resistance to necrotic and radiant damage.", 
        "You gain darkvision with a radius of 60 feet for 1 minute. If you already have darkvision, you lose it for 1 minute.", 
        "You transform into an iron statue of yourself for 1 minute, during which time you are considered petrified.", 
        "You are at the center of a fog cloud spell which lasts for 1 minute.", 
        "Approximately 100 gallons of water appear over your head and those within 10 feet of you, evenly distributed above everybody within the radius.", 
        "You gain an additional spell slot of your highest level for 1 week.", 
        "Your Charisma is increased by 2 for 1 day.", 
        "You gain a +1 to your AC for one minute.", 
        "If you die within the next minute, you come back to life as if by the reincarnate spell.	", 
        "You and all creatures within 30 feet of you gain vulnerability to lightning damage for 1 minute.", 
        "You fall victim to a horrible cramp in both legs, reducing your speed by 10 feet for 1 hour.", 
        "You permanently gain one spell slot of one level below your highest-level spell slot, but lose one 1st-level spell slot. A spell such as remove curse can end this effect.", 
        "You and all creatures within 30 feet of you gain vulnerability to force damage for 1 minute.", 
        "The next spell you cast within the next hour uses a spell slot of one level lower than what it normally requires. If the spell is a spell of 1st level, you still must expend a spell slot to cast it.", 
        "All creatures that can perceive you must make a Wisdom saving throw against your spell save DC or be frightened of you.", 
        "For the next minute, any creature you touch takes 2d6 lightning damage.", 
        "For the next hour, you are unable to read as the letters all appeared jumbled.", 
        "You are vulnerable to Elementals for 1 hour. Such creatures gain advantage when attacking you.", 
        "You gain blindsight with a radius of 60 feet for 1 minute.", 
        "For the next day, everything you say must rhyme. If it doesn’t, you take 1d6 psychic damage.", 
        "You are protected from Fey for 1 day. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "You are surrounded by a horrible, noxious odor for 1 minute. Anyone within 10 feet of you must make a Constitution saving throw or be stunned.", 
        "During the next hour, you may re-roll one save, attack roll, or skill check. If you do, you must take the new roll’s result.", 
        "You gain the service of an arcane sword that does not require concentration until your next short or long rest.", 
        "Your Charisma is decreased by 2 for 1 hour.	You grow 1d6 inches in height. You gradually return to your original height over the course of 1 day.", 
        "You permanently gain one cantrip. A spell such as remove curse can end this effect.", 
        "You gain the service of a phantom steed for 1 day.", 
        "You immediately take 2d4 psychic damage.", 
        "All allies within 20 feet of you get gain a -2 penalty on attack and damage rolls for any melee attack they make in the next minute.", 
        "You and all creatures within 30 feet of you gain vulnerability to acid damage for 1 minute.", 
        "For the next hour, any time you make an ability check, roll 1d4 and subtract the result.", 
        "All allies within 20 feet of you heal up to 3d8 hit points.", 
        "Your Wisdom is decreased by 2 for 1 hour.", 
        "You gain the ability to speak with animals for one hour.", 
        "You lose the ability to see for 1 day. During this time, you have the blinded condition.", 
        "Your speed is increased by 10 feet for 1 day.", 
        "You get gain a -1 penalty to your AC for 1 minute.", 
        "You gain the service of a phantom steed for 1 week.	", 
        "You gain the ability to walk on water for 1 day.", 
        "You gain the use of an unseen servant for 1 hour.", 
        "Make a Constitution saving throw against your spell save DC. If you fail, you are stunned for 1 minute.", 
        "You and all creatures within 30 feet of you gain vulnerability to psychic damage for 1 minute.", 
        "The next spell you cast within the hour uses a slot level one level higher than what it normally requires.", 
        "You transform into a stone statue of yourself for 1 minute, during which time you are considered petrified.", 
        "One creature of your choice gets a +2 bonus to all attack rolls, damage rolls, and their armor class AC for 1 minute.", 
        "A bad joke comes to mind and until you tell it (which takes an entire action), you suffer a Wisdom penalty of 1.", 
        "All creatures within 20 feet of you, including you, must make a Dexterity save against your spell save DC or be affected by a faerie fire spell.", 
        "You lose proficiency in one randomly chosen skill, tool, or weapon type for 2d6 days.", 
        "You hear a ringing in your ears for 1 minute. During this time, casting a spell that requires a verbal component requires a Constitution check against your spell save DC.", 
        "Permanently increase one ability score of your choice by 1 point. ", 
        "Permanently decrease a different ability score of your choice by 1 point. A spell such as remove curse can end this effect.", 
        "All food and drink within 30 feet of you becomes putrid, spoiled, or rotten. Consuming this food deals 2d6 poison damage and causes the poisoned condition for 1 hour.", 
        "You lose 1d6x5 pounds. You gradually return to your original weight over the course of 1 day.", 
        "You gain proficiency in one tool or weapon type you don’t already have for 1 day.", 
        "All silver you are carrying is now copper.", 
        "Your clothes become dirty and filthy. Until you can change and/or clean your clothes, your Charisma is reduced by 1.", 
        "Make a Wisdom saving throw against your spell save DC. If you fail, you are transformed into a giant spider for 1 minute, as if by the polymorph spell.", 
        "You and all creatures within 30 feet of you gain vulnerability to fire damage for 1 minute.", 
        "You gain proficiency in Wisdom checks for the next hour, if you don’t already have it.", 
        "Gain the sympathy effects of the antipathy/sympathy spell for 3d6 days.", 
        "You lose proficiency in all skill rolls for 1d4 hours.", 
        "You shrink 1d6 inches in height. You gradually return to your original height over the course of 1 day.", 
        "You are protected from Fiends for one day. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "You are protected from Fey for one hour. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "Your skin permanently darkens as if you have a tan, or if you are already dark-skinned, your skin becomes one shade lighter. A spell such as remove curse can end this effect.", 
        "All allies within 20 feet of you gain a -2 penalty to attack and damage rolls for any ranged attack they make within the next minute.", 
        "For the next hour, any time you make an ability check, roll 1d6 and subtract the result.", 
        "For 1 minute, one creature of your choice within 30 feet of you gains a -1 penalty to attack rolls, damage rolls, and their AC.", 
        "For one minute, any spell with a casting time of 1 action can be cast as a bonus action.", 
        "For the next minute, you gain resistance to poison and psychic damage.", 
        "For the next hour, any time you make an ability check, roll 1d4 and add the result.", 
        "Make a Wisdom saving throw against your spell save DC. If you fail, you are transformed into a giant rabbit for 1 minute, as if by the polymorph", 
        "You’re feeling lucky. For the next hour, any time you make an ability check, roll 1d6 and add the result.", 
        "If you cast a spell with a saving throw within the next minute, the target gains disadvantage on its saving throw.", 
        "The next time you cast a spell, do not roll on this chart.", 
        "You immediately take 2d6 psychic damage.", 
        "Your Strength is increased by 2 for 1 minute.", 
        "For the next day, you gain proficiency in all skills that you are not already proficient in.", 
        "You gain proficiency in one skill of your choice that you're not already proficient in for one hour.", 
        "One creature of your choice gains a +1 bonus to attack rolls, damage rolls, and its AC for 1 minute.", 
        "The next time you cast a spell, roll twice on this chart. Both effects will apply.", 
        "Your Constitution is increased by 2 for 1 day.", 
        "You immediately heal 2d10 hit points.", 
        "You are vulnerable to Fey for 1 hour. Such creatures gain advantage when attacking you.", 
        "You and all creatures within 30 feet of you gain vulnerability to thunder damage for 1 minute.", 
        "You gain proficiency on all Intelligence checks for the next hour, if you don’t already have it.", 
        "You transform into an empty wooden chest for 1 minute, during which time you are considered petrified.", 
        "You and all creatures within 30 feet of you gain vulnerability to cold damage for 1 minute.", 
        "The power of your magic is strong! For the next hour, any spell you cast does not require a verbal component.", 
        "Gain the antipathy effects of the antipathy/sympathy spell for 3d6 days.", 
        "You gain the ability to speak one language of your choice for 1 day.", 
        "You gain 1d6x10 pounds. You gradually return to your original weight over the course of 1 day.", 
        "All creatures within 30 feet of you must make a Wisdom saving throw. Any creature immune to magical sleep automatically succeeds on its saving throw.", 
        "Those that fail fall asleep for 1d6 minutes.	You and all creatures within 30 feet of you gain vulnerability to radiant damage for 1 minute.", 
        "You gain proficiency in all Dexterity checks for the next hour, if you don’t already have it.", 
        "You are protected from Plants for 1 day. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.", 
        "You are protected from Celestials for 1 hour. Such creatures cannot attack you or harm you unless they succeed a on a Charisma saving throw against your spell save DC.", 
        "Your fingernails and toenails grow to an uncomfortable length. Until you trim them, your Dexterity is reduced by 1 and your speed is reduced by 5 feet, even if you’re not wearing shoes.", 
        "All your allies within 20 feet of you gain a +2 bonus to their AC for 1 minute.", 
        "For the next minute, you are unable to cast any spell that causes damage of any type.", 
        "You gain the effects of the blur spell for 1 minute, which does not require concentration to maintain.", 
        "The next time you fall below 0 hit points within the next month, you automatically fail your first death saving throw.", 
        "You gain spider climb for 1 minute, and it does not require concentration to maintain.", 
        "For the next hour, you appear to others to be the opposite gender.", 
        "You gain two spell slots at your second-highest level for 1 week.", 
        "You immediately lose all unspent sorcery points and may not regain them until you have finished a long rest.", 
        "You gain the service of a 2nd-level spiritual weapon for 1 minute.", 
        "For the next day, any time you make an ability check, roll 1d6 and add the result.", 
        "You and all creatures within 30 feet of you gain vulnerability to poison damage for 1 minute.", 
        "The power of your magic is strong! For the next hour, any spell you cast does not require a somatic component.", 
        "Make a Wisdom saving throw against your spell save DC. If you fail, you are transformed into a sheep for 1 minute, as if by the polymorph spell.", 
        "You gain the ability to speak with animals for 1 day.", 
        "You gain proficiency in all Constitution checks for the next hour, if you don’t already have it.", 
        "All allies within 30 feet of you gain a -2 penalty to their AC for 1 minute.", 
        "All food and drink within 30 feet of you is purified.", 
        "Every inanimate object that isn't being worn or carried within 40 feet of you becomes enshrouded with shadows for 1 minute. Enshrouded objects are considered heavily obscured.", 
        "You are protected from Undead for 1 day. Such creatures cannot attack you or harm you unless they succeed on a Charisma saving throw against your spell save DC.",
        "You are protected from Aberrations for 1 hour. Such creatures cannot attack you or harm you unless they succeed on a Charisma savinng throw against your spell save DC.", 
        "Your fingers become sore for 1 hour. During this time, you must succeed on a Dexterity saving throw against your spell save DC to cast a spell with a somatic component.", 
        "You jump forward in time exactly 1 minute, for 1 minute. From the perspective of everyone else, you cease to exist during that time.", 
        "All your clothing and equipment teleports to the nearest open space at least 15 feet from you that you can see.", 
        "You feel extremely nauseated. Make a Constitution saving throw against your spell save DC. If you fail, you must spend your next action throwing up.", 
        "All spells you cast within the next minute automatically fail.	", 
        "Your Constitution is decreased by 2 for 1 hour.	", 
        "You immediately lose one unspent sorcery point.", 
        "A caster teleports 25 ft. to the left of their location. A trail of fire appears from their starting position to their teleported position.", 
        "The spell fails to take effect… until 1d4 rounds later.", 
        "Something Fishy: the caster is left smelling of fish. The target of the spell also smells of fish. If the spell affects an area, the area smells of fish. If the spell produces a projectile the projectile becomes a fish(no change to damage type).", 
        "All the players randomly change bodies for 1d4 rounds.", 
        "It rains literal cats and dogs for one round, causing 1d4 bludgeon damage to any creature hit by a dog and 1d6 slashing damage to any creature hit by a cat.", 
        "Feathers – The caster hair follicle’s sprout feathers of one type and in the next round, these fall off, or fly away and a round after, they sprout different feathers. This effect lasts a number of turns = d6+spell level . So the caster was casting Chain Lightning a 6th level spell. 6d6 turns.", 
        "A genie offers the caster a Wish, but refuses to grant it and disappears.", 
        "The caster can see one round into the future.", 
        "Everyone in a 3d6 foot radius has to make a DC 15 Con save or falls asleep for 1d4 rounds.", 
        "2d8 gp fly out of the casters hands. 2d8 of them hit (if the second roll exceeds the first, they all hit), dealing 1d4-1 bludgeoning damage each.", 
        "The caster and the target both get an intense sense of kinship and refuse to fight each other for 1d4 rounds.", 
        "The caster loses containment of his or her magical power, which all goes pouring out to the nearest creature. The caster expends all his or her remaining spell slots and sorcery points, adding all the spell levels together (with each sorcery point counting as 1 level). The target takes 1d6 force damage for each spell level expended this way. If this damage kills the target, the leftover damage continues to the next closest creature, and so on until all damage has been applied.", 
        "The spell builds up at the users magical implement, charging. The spell is not cast this turn, but next, dealing double damage to those hit.", 
        "A force explodes out in a ring around the caster, knocking everybody back 5 feet (Fort save DC14, range 25ft)", 
        "The caster begins to glow. (As Light spell, no save)", 
        "The caster loses control of their bladder. Constitution save DC18 or they urinate on the spot.", 
        "The user is driven mad by the spell, causing them to go into a barbarian rage for one minute.", 
        "Your shadow detaches from you and becomes a shadow (the creature).", 
        "You flash with golden light that seems to hang in the air around you. Everyone caught in this light (20 foot radius) receives double healing and cannot lie for the next 10 turns (one minute outside combat).", 
        "The world seems to dim and plants seem to wilt around you. Everybody in a 20 foot radius takes double damage from necrotic damage and take one point of exhaustion on any critical failures for the next 10 turns (one minute outside combat).", 
        "You feel very attractive… All unsecured objects and creatures in a 100 ft radius moves towards you by 5 feet.", 
        "You feel like you really need to sneeze. Make a constitution saving throw with a DC of 10+your spell casting modifier. On a failure, you sneeze, and involuntarily cast prismatic spray (without consuming a spell slot) in the direction you are facing. On a successful save, you sneeze normally, without any ill effects.", 
        "The world seems to slow to a crawl around you. You get to take 1 additional action.", 
        "The smell of cinnamon fills the area in a 30-foot radius around the caster.", 
        "A small songbird pops into existence in mid-flight 10 feet above the caster. Roll a d20. On a 1, the bird poops and it lands on the caster. On a 20, the bird poops and it lands on the target of the spell.", 
        "The caster develops severe claustrophobia for 1d4 hours.", 
        "A sinkhole, 20 feet deep and 10 feet in diameter, appears at a random location within 100 feet of the caster.", 
        "The caster gets the hiccups, which last for 1d6 minutes.", 
        "Any non-magical pouches or containers on the caster’s person tear open and spill their contents onto the ground.", 
        "Around the caster spawns 10 frogs, all of them are passive.", 
        "Around the caster spawns 10 rats, all of them hostile.", 
        "A lit birthday candle appears before the caster. In front of the candle is a note. The note reads “blow the candle out to make a wish.", 
        "A tiny elemental of the caster’s choice appears as a familiar.", 
        "Fog seeps up from the ground, obscuring everything within a 20′ radius of the target, or caster, for 1d4 rounds.", 
        "The next person the caster physically touches takes 1d6 lightning damage.", 
        "The caster grows an extra finger on one of their hands. A remove curse spell or a successful DC20 medicine check can remove the finger.", 
        "The spell is unexpectedly loud and everyone within 10 feet of you (including you) takes 1d6 thunder damage and the spell can be heard 600 feet away.", 
        "The casters eyes catch on fire and their hands are covered in ice crystals. Any unarmed attack deals an additional 1d4 cold damage for 1d4 rounds.", 
        "Caster’s race changes every day for the next week.", 
        "Both caster must make a DC 15 Wis save. On failure, they drop whatever they are holding.", 
        "Caster knows a new language, chosen by the DM.", 
        "Any loose objects move 10ft closer to caster.", 
        "Caster’s hair changes color.", 
        "After casting the spell, the caster hears strange whispers in an unknown language for 1d20 minutes. Occasionally the whispers seem to go quiet, as though they know someone is listening.", 
        "After 1d4 rounds of casting the spell, a bear intent on violence towards the party, and with knowledge of their whereabouts, is summoned 200 feet away.", 
        "Five Violet Fungus sprout up from the ground and begin attacking the party when the spell is cast.", 
        "A Couatl, sensing a spell being cast, swoops within 10 feet of the party’s heads, and flies away after examining the magic cast.", 
        "The caster experienced extreme discomfort in their stomach for 1d4 turns before finally releasing a monstrous belch for another 1d4 turns. This belch functions as per the description of the spell Gust of Wind, with the direction of the wind being whichever direction the caster is facing.", 
        "For the next 24 hours, the caster’s nose grows outwards by 1 inch every time they knowingly tell a lie. The nose returns to it’s previous size once the duration is up.", 
        "For the next hour, the caster bursts into a fit of evil, maniacal laughter every time they open their mouth. Each time they do so, they must make a DC 13 Wisdom saving throw or be compelled to pull a minor prank of some kind. The nature of the prank is at the player’s discretion, so long as it is suitably mischevious and harmless.", 
        "Every writing in a 10-foot radius of the caster immediately transforms into incredibly petty criticism of the caster. If the caster reads any of it, they must make a DC 10 Wisdom saving throw or believe whatever minor putdown the writing describes.", 
        "A chorus of ethereal voices congratulate the caster on casting the spell and compliment the quality of both the casting and the spell itself. Anytime the caster uses magic within an hour of the casting of the original spell, they are met with the murmured approval and commentary of the voices.", 
        "You immediately grow a bunch of body hair that falls off after a day.", 
        "Instead of the fireball you were expecting, you begin summoning countless cabbages, pouring out in a cone in front of you.", 
        "Instead of doing any damage the full points of damage would heal the person instead.", 
        "Instead of the cone of ice you wanted, a disgruntled 6 inch pixie appears, flies up to you, punches you in the forehead, sprinkles you with a dust that makes you sneeze violently, and then vanishes in a puff of neon pink and orange glitter.", 
        "The somatic components for the song are replaced with the theme song to friends, and the hand-gestures are the clapping.", 
        "They grow rabbit ears that give them advantage on all perception rolls for 1 hour.", 
        "The caster’s eyes glow and they’re able to see in the dark but the glow allows everything in the darkness to see them.", 
        "The cast vomits up a huge slug after casting the spell.", 
        "The caster’s arms disappear and are replaced with mist-limbs. They can only lift up to ten pounds but can fit under doors, open non-magical locks, and even cool hot metals. Lasts for 1d10 minutes.", 
        "The target for the spell becomes immobilized for 1 round, and until they succeed in a con save (DC 10).", 
        "The target is effect by the same spell twice. The caster still uses one spell slot. If the first casting is within the caster’s control (ploy morph, alter self), the second effect is totally random.", 
        "The caster spits glitter when he talks. It gets everywhere. The effect ends after 1 minute but the glitter never goes away.", 
        "The first person who says the casters name then has total mental control over them for 1d4 rounds.", 
        "Target turns into a marble figurine of itself. When the figurine is activated (by throwing it into an unoccupied space) it transforms back into its living form and is hostile towards all creatures.", 
        "Any keratin on the caster’s body (hair, nails, feathers, some skin, horns, hooves, etc…) turn a vibrant hue.", 
        "The caster spontaneously combusts.", 
        "The caster is launched ten feet into the air and falls back down.", 
        "Caster turns into massive oak tree.", 
        "All the PCs and NPCs including monsters change places, rotate places 1d4 spots clockwise", 
        "The caster’s hair grows very rapidly, if male, so does the beard. It grows to about 2meters length, and turns purple, green or blue.", 
        "Bubbles sprout from the casters mouth every time he exales, lasts 1 hour.", 
        "Next book the caster reads, has him/her as protagonist", 
        "1d8 medium sized purple tentacles rise from the ground. They are semi-sentinel and not aligned to caster nor foe. They attempt to grapple anything within range (DC 14)", 
        "Regardless of the amount of time that passes in game the caster of this spell can see and hear all that happens in the real world surrounding the player of said character for the next 1d6 minutes per level of spell cast.", 
        "The caster and target switch classes but retain their respective level, if the target does not have a class then the caster switches classes with the closest humanoid with one.", 
        "In the next 1d6 hours the caster grows 1d6 feet, but gains no mass, so a halfling would become an extremely tall thin creature. No negative effects purely cosmetic, can be reversed with remove curse.", 
        "The casters eyes and veins glow in the dark for 1d6 days.", 
        "A weapon within 30 feet of caster becomes sentient, it’s always grumbling about being dirty and grants disadvantage to the user if they don’t spend an hour a day cleaning it.", 
        "The caster rolls 1d2. 1 = the age 1d10 years. 2 = they lose 1d10 years.", 
        "Any object or being that the caster touches for 1d10 rounds ( 1 minute out of combat) turns to leaves for 1d10 minutes.", 
        "If the caster is using a spell casting focus, it grows 100 times heavier for one minute.", 
        "The casters eyes flash with a strange color. To the caster, everybody’s skin and muscles are transparent, revealing their organs. This lasts for 1 minute.", 
        "Magical silence falls in a 50 ft radius that lasts for 10 minutes.", 
        "All noises the caster makes for the next minute are x100 times louder.", 
        "The next piece of metal the caster touches turns to gold.", 
        "All water in a 50 ft radius evaporates instantly.", 
        "A small lead figure of the caster in the exact pose they were in appears in mid air and falls to the ground. Despite being so small, it weighs exactly as much as the caster.", 
        "The caster suddenly witnesses a memory from one of their ancestors.", 
        "The casters hair disappears, reappearing 1d6 days later, washed, braided and decorated with flowers.", 
        "Instead of the effect you were intending, there is a burst of silent and illusionary fireworks in a 100 foot radius around you, and all creatures affected by them are stunned until their next turn.", 
        "Instead of the intended effect, 10d10 trees in the area grow mouths, and begin singing for 1d8 rounds. If the original spell was supposed to be a spell of healing, the song is a rousing chorus that washes away fatigue and ends any emotional (fear, charm, etc.) effect that is currently afflicting any that hear it. If the original spell was supposed to be an attack spell, the song is an irresistible tune that catches up all that hear it into singing it with the trees, and all the attitudes of the combatants is changed to neutral towards each other when the song ends. If the spell was supposed to be anything else, the song is a soothing song that makes the listeners sleepy, making it hard to take reactionary attacks until the song ends.", 
        "In front of the caster a portal, no larger than a fist, opens to the realm of infinite (insert desired liquid here). That liquid begins to pour out uncontrollably for 1 rnd / caster level.", 
        "The caster casts grease centered on self.", 
        "The caster is trapped in a giant glass ball. Must be broken to be freed.", 
        "The caster sees everyone as a decaying corpse for 24h.", 
        "The caster becomes a potted plant until start of next turn.", 
        "The caster has max damage on the spell they were casting.", 
        "The caster gains 50 lbs.",
    ]
    document.getElementById("Surge").innerHTML = rollArray(wildMagic)
};