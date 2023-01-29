# This code was written by a student Anna.
import random
import os
os.system("clear")


habitat_terrain = ["mountain", "plain", "forest", "desert", "glacier", "tundra", "jungle"]
habitat_terrain = random.choice(habitat_terrain)


habitat_rainfall_min = 0
habitat_rainfall_max = 3000
habitat_rainfall = str(random.randint(habitat_rainfall_min, habitat_rainfall_max)) + " mm"


habitat_min_temp = -70
habitat_max_temp = 70
habitat_temp = str(random.randint(habitat_min_temp, habitat_max_temp))


habitat_prefix = ["majestic", "tropical", "magical", "wonderful", "fantastic", "floral", "atmospheric", "dying", "safe", "dangerous", "quiet", "calm", "unique", "atmospheric", "pristine", "rugged", "diverse", "untouched", "beautiful", "lush", "exotic", "serene", "mysterious", "wild", "remote", "endangered", "thriving", "dramatic", "spectacular"]
habitat_prefix = random.choice(habitat_prefix)

habitat_water = ["lake", "river", "stream", "pond"]
habitat_water = random.choice(habitat_water)


def habitat_weather(habitat):
    habitat_weather = {
        "jungle": ["humid","hot","monsoonal"],
        "desert": ["dry","sandy","blistering"],
        "ocean": ["windy","overcast","breezy"],
        "forest": ["foggy","misty","shaded"],
        "mountain": ["windy","frosty","icy"],
        "plain": ["dry","drought","windy"],
        "glacier": ["icy","frosty","blizzard"],
        "tundra": ["frigid","icy","windy"]
    }
    if habitat in habitat_weather:
        weather = random.choice(habitat_weather[habitat])
    return weather


def habitat_smell(habitat):
    habitat_smells = {
        "jungle": ["humid", "damp", "mossy", "verdant", "exotic", "pungent"],
        "desert": ["arid", "dusty", "sandy", "cactus", "sun-baked", "dry"],
        "ocean": ["salty", "briny", "seaweed", "fishy", "oceanic", "tropical"],
        "forest": ["piney", "mossy", "woodsy", "fresh", "earthy", "mushroomy"],
        "mountain": ["rocky", "mineral", "pebbly", "herbal", "cool", "crisp"],
        "plain": ["grassy", "earthy", "herbaceous", "fertile", "rich", "warm"],
        "glacier": ["icy", "frosty", "snowy", "frozen", "crisp", "brisk"],
        "tundra": ["peaty", "marshy", "boggy", "muggy", "damp", "muddy"]
    }
    if habitat in habitat_smells:
        smell = random.choice(habitat_smells[habitat])
    return smell


def habitat_sound(habitat):
    habitat_sounds = {
        "jungle": ["birds chirping", "animals howling", "insects chirping", "leaves rustling", "waterfalls roaring", "monkeys screeching"],
        "desert": ["wind blowing", "coyotes howling", "insects chirping", "desert foxes yipping", "cacti rustling", "sand dunes whistling"],
        "ocean": ["waves crashing", "seagulls squawking", "dolphins calling", "whales singing", "seals barking"],
        "forest": ["monkeys chattering", "parrots squawking", "birds singing", "cicadas buzzing", "owl hooting", "crickets chirping"],
        "mountain": ["rocks tumbling", "waterfalls cascading", "animals hooting", "eagles soaring", "wind whistling", "thunder rumbling"],
        "plain": ["grass rustling", "crickets chirping", "birds singing", "wind blowing", "cows mooing", "horses neighing"],
        "glacier": ["icy winds blowing", "cracking of ice", "snow crunching underfoot", "avalanches rumbling", "faint echoes of glaciers calving", "high altitude bird calls"],
        "tundra": ["arctic foxes howling", "reindeer bellowing", "wolves howling", "snowy owls hooting", "lemmings scurrying", "frosty winds blowing"]
    }
    if habitat in habitat_sounds:
        sound = random.choice(habitat_sounds[habitat])
        return sound


def habitat_name(terrain):
    if terrain == "mountain":
        mountain_names = ["The Desolate Summit", "The Voiceless Mountains", "The Collapsing Volcano", "The Yelling Highlands", "The Snowy Tips", "The Northern Rise", "The Unwelcoming Heights"]
        return random.choice(mountain_names)
    elif terrain == "ocean":
        ocean_names = ["The Lonely Waves", "The Soundless Waves", "The Jade Depths", "The Frozen Waves", "The Moon-lit Abyss", "The Surging Waves", "The Dark Deep"]
        return random.choice(ocean_names)
    elif terrain == "river":
        river_names = ["Bloody River", "Laughing River", "Lifeless River", "Cold Channel", "Dreaded River", "Bland River", "Unknown River", "Amazon Falls River"]
        return random.choice(river_names)
    elif terrain == "plain":
        plain_names = ["Thin Meadow", "Peaceful Grassland", "Giant Plains", "Laughing Boa Prairie", "Big Territory", "Southern Bee Gardens"]
        return random.choice(plain_names)
    elif terrain == "forest":
        forest_names = ["Huge Pine Wood", "Into Woodlands", "Massive Woods", "Reflecting Woods", "Shadow Wood"]
        return random.choice(forest_names)
    elif terrain == "desert":
        desert_names = ["The Hungry Fields", "The Dead Savanna", "Decaying Expanse", "Dehydrated Flats", "The Deserted Flats", "Flat Emptiness"]
        return random.choice(desert_names)
    elif terrain == "jungle":
        jungle_names = ["The Lunar Jungle", "The Waking Paradise", "The Dark Paradise", "The Predator Gardens", "The Mighty Jungles"]
        return random.choice(jungle_names)
    elif terrain == "tundra":
        tundra_names = ["The Awaiting Flower", "The Penguin", "The Snow Crystal Fields", "The Icy Tundra", "The Ice Needle Tundra"]
        return random.choice(tundra_names)
    elif terrain == "glacier":
        glacier_names = ["The Shivering Sheet", "The Blind Berg", "le Champ Croissant", "The Lonely Glacier", "The Infinite Slide", "The Auroral Ice Field"]
        return random.choice(glacier_names)
    else:
        return "Unknown"


habitat_animals_group = ["mammals", "reptiles", "birds", "fish", "amphibians", "arthropods"]

habitat_animals_desc = ["aggressive", "fury", "fast", "loud", "sensitive", "gentle", "cautious", "curious", "intelligent", "adorable", "rare", "endangered", "migratory", "nocturnal", "diurnal", "solitary", "social", "diverse", "unique", "endemic", "predatory", "scavenging"]

def habitat_animal(group):
    if group == "mammals":
        mammals_animal = ["polar bears", "grizzly bears", "black bears", "seals", "pigs", "ocelots", "foxes", "wolves", "squirrels", "leopards", "llamas", "snow leopards", "tigers", "lions ", "lynx", "mountain lions", "coyote", "rabbits", "rats", "mice", "deer", "boars", "cows", "buffalos", "hares", "cheetah", "girrafes", "rhinos", "zebras", "horses", "elephants", "goats", "platypus", "koalas", "pandas", "moose", "chipunk", "capybara", "raccons", "otters", "sloths", "walrus", "gorillas", "monkeys", "apes", "bats", "whales", "donkeys", " kangaroo", "hippopotamus", "sheep", "hedgehog", "dolphins", "jaguars", "bobcats"]
        return random.choice(mammals_animal)
    elif group == "reptiles":
        reptiles_animal = ["sea turtles", "snakes", "alligators", "crocodiles"]
        return random.choice(reptiles_animal)
    elif group == "birds":
        birds_animal = ["macaw", "toucans", "bald eagles", "woodpeckers", "penguins", "ducks", "parrots"]
        return random.choice(birds_animal)
    elif group == "amphibians":
        amphibians_animal = ["frogs", "toads", "salamanders", "newts"]
        return random.choice(amphibians_animal)
    elif group == "fish":
        fish_animal = ["sharks", "pufferfish", "salmon", "cod", "tuna", "catfish", "trout", "bass", "swordfish", "goldfish", "clownfish"]
        return random.choice(fish_animal)
    elif group == "arthropods":
        arthropod_animal = ["crayfish", "crabs", "spiders", "scorpions", "millipedes", "centipedes", "lobsters", "shrimp", "caterpillars", "butterflies", "moths", "grasshoppers", "crickets", "termites", "ants", "bees", "wasps", "hornets", "dragonflies", "damselflies", "fireflies", "ladybugs", "praying mantises"]
        return random.choice(arthropod_animal)
    else:
        return "Unknown"


animal1 = random.choice(habitat_animals_desc) + " " + habitat_animal(random.choice(habitat_animals_group))
animal2 = random.choice(habitat_animals_desc) + " " + habitat_animal(random.choice(habitat_animals_group))
animal3 = random.choice(habitat_animals_desc) + " " + habitat_animal(random.choice(habitat_animals_group))
animal4 = random.choice(habitat_animals_desc) + " " + habitat_animal(random.choice(habitat_animals_group))
animal5 = random.choice(habitat_animals_desc) + " " + habitat_animal(random.choice(habitat_animals_group))
animal6 = random.choice(habitat_animals_desc) + " " + habitat_animal(random.choice(habitat_animals_group))

habitat_animals = []
for i in range(6):
    animal_group = random.choice(habitat_animals_group)
    animal = habitat_animal(animal_group)
    animal_desc = random.choice(habitat_animals_desc)
    habitat_animals.append(animal_desc + " " + animal)


habitat_plants_type = ["Trees", "Flowers", "Shrubs", "Creepers", "Climbers"]

habitat_plants_desc = ["majestic", "aromatic", "lush", "colorful", "tropical", "dense", "endangered", "rare", "medicinal", "delicate", "towering", "gigantic", "creepy", "scary", "strange", "unusual", "unique", "exotic"]


def habitat_plant(type):
    if type == "Trees":
        trees_plant = ["weeping willow", "birch", "chestnut", "pine", "palm", "maple", "oak", "poplar", "elm", "fir", "spruce", "cactus"]
        return random.choice(trees_plant)
    elif type == "Flowers":
        flowers_plant = ["orchid", "sunflower", "lily", "roses", "violet", "tulip", "chrysanthemum", "marigold", "hibiscus", "lavender", "iris"]
        return random.choice(flowers_plant)
    elif type == "Shrubs":
        shrubs_plant = ["rose", "tulsi", "lemon", "jasmine"]
        return random.choice(shrubs_plant)
    elif type == "Creepers":
        creepers_plant = ["watermelon", "strawberry", "pumpkin", "sweet potatoes"]
        return random.choice(creepers_plant)
    elif type == "Climbers":
        climbers_plant = ["cucumber", "gourd"]
        return random.choice(climbers_plant)
    else:
        return "Unknown"


plant1 = random.choice(habitat_plants_desc) + " " + habitat_plant(random.choice(habitat_plants_type))
plant2 = random.choice(habitat_plants_desc) + " " + habitat_plant(random.choice(habitat_plants_type))
plant3 = random.choice(habitat_plants_desc) + " " + habitat_plant(random.choice(habitat_plants_type))
plant4 = random.choice(habitat_plants_desc) + " " + habitat_plant(random.choice(habitat_plants_type))
plant5 = random.choice(habitat_plants_desc) + " " + habitat_plant(random.choice(habitat_plants_type))
plant6 = random.choice(habitat_plants_desc) + " " + habitat_plant(random.choice(habitat_plants_type))


habitat_plants = []
for i in range(6):
    habitat_type = random.choice(habitat_plants_type)
    plant = habitat_plant(habitat_type)
    plant_desc = random.choice(habitat_plants_desc)
    habitat_plants.append(plant_desc + " " + plant)


if int(habitat_temp) < -30:
    habitat_terrain = "glacier"
if int(habitat_temp) > 45:
    habitat_terrain = "desert"
else:
    random.choice(habitat_terrain)


has_water = random.choice([True, False])
if has_water:
    water_size_range = (1, 1000)
    water_depth_range = (1, 1000)
    water_size = str(random.randint(*water_size_range))
    water_depth = str(random.randint(*water_depth_range))


# if int(water_size) < 150:
#     if int(water_depth) < 6:
#         habitat_water = "pond"
# else:
#     random.choice(habitat_water)

paragraph = habitat_name(habitat_terrain) + " is a " + habitat_prefix + " habitat characterized by its " + habitat_terrain + " terrain. It is home to a diverse array of plant and animal life."
paragraph += " It is home to a variety of animals such as " + animal1 + ", " + animal2 + ", " + animal3 + ", " + animal4 + ", " + animal5 + ", and " + animal6 + "."
paragraph += " This habitat is also home to many different kinds of plants such as " + plant1 + ", " + plant2 + ", " + plant3 + ", " + plant4 + ", " + plant5 + ", and " + plant6 + "."
paragraph += " The weather and climate in this habitat is usually " + habitat_weather(habitat_terrain) +  "."
paragraph += " The annual rainfall is about " + habitat_rainfall + " yearly and the average temperature is " + habitat_temp + "."
paragraph += " You can hear many different sounds in this habitat such as " + habitat_sound(habitat_terrain) + "."
paragraph += " This habitat has a " + habitat_smell(habitat_terrain) + " smell."

if has_water:
    paragraph += "The habitat also has a body of water, a/an " + habitat_water + " with a size of " + water_size + " square meters and a depth of " + water_depth + " meters."
paragraph += "Hope you were able to somewhat visualize and/orimagine how the habitat looks like and it's unique inhabitants."

print(paragraph)
