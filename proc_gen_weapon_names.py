# this is a procedural generator that makes weapon names and types
import random

weapon_culture = ["Dwarven", "Elvish", "Human", "Infernal", "Gnomish", "Orcish"]
selected_culture = random.choice(weapon_culture)

weapon_age = ["Peace", "War", "Tranquility", "Sundering", "Rage", "Destruction", "Terror", "Doom", "Despair", "Glory", "Victory", "Darkeness", "Light", "Discovery"]
selected_age = random.choice(weapon_age)

weapon_category = ["ranged", "melee", "magic", "thrown", "other"]
selected_weapon_category = random.choice(weapon_category)


weapon_types_ranged = ["short bow", "long bow", "crossbow"]
selected_weapon_ranged= random.choice(weapon_types_ranged)

weapon_types_thrown = ["javelin", "throwing axe", "throwing hammer", "throwing knife", "throwing spear", "dart", "sling"]
selected_weapon_thrown = random.choice(weapon_types_thrown)

weapon_types_light_melee = ["short sword", "dagger", "staff","rapier", "scimitar", "sickle", "whip"]
selected_weapon_light_melee = random.choice(weapon_types_light_melee)

weapon_types_heavy_melee = ["great sword", "mace", "morning star", "great axe", "two-handed sword", "war hammer","mighty-club-of-clubbing"]
selected_weapon_heavy_melee = random.choice(weapon_types_heavy_melee)

weapon_types_magic = ["wand","orb","amulet"]
selected_weapon_magic = random.choice(weapon_types_magic)

weapon_prefix = ["sharp", "broken", "exquisite", "normal", "sentient", "flaming", "frosty", "furious", "glowing", "hot", "icy", "lightning", "magic", "mighty", "mystic", "poisoned", "sharp", "silent", "slimy", "sneaky", "sparkling", "thundering", "twilight", "vicious", "wicked", "opinionated", "wrenching", "zealous"]
selected_weapon_prefix = random.choice(weapon_prefix)

# weapon_previous_owner = ["Friar's", "Votran's", "Anna's", "Gorg's", "Ar'rian's", "Thag's", "Quein's", "Worble's"]

weapon_material = ["wood", "stone", "rare metals", "incadescent stone", "silver", "dark matter", "metorite"]

weapon_alignment = ["lawful", "neutral", "chaotic", "unaligned", "evil"]
selected_weapon_alignment = random.choice(weapon_alignment)

weapon_personality = ["optimisitic", "pessimistic", "jealous", "bloodthirsty", "uncertain", ""]

weapon_sentience = ["sentient", "unsentient"]
selected_weapon_sentience = random.choice(weapon_sentience)

weapon_size = ["tiny", "small", "medium", "large", "huge"]
selected_weapon_size = random.choice(weapon_size)



# weapon_name = "Long ago, during the era of " + random.choice(weapon_age) + ", " + random.choice(weapon_culture) + " smiths forged " + random.choice(weapon_previous_owner) + " " + random.choice(weapon_prefix) + " " + random.choice(weapon_types) + ". " + "Forged of " + random.choice(weapon_material) + "," 
# print(weapon_name)
