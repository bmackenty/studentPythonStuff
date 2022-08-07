# this is a procedural generator that makes weapon names and types
import random

weapon_culture = ["Dwarven", "Elvish", "Human", "Infernal", "Gnomish", "Orcish"]
selected_weapon_culture = random.choice(weapon_culture)

weapon_age = ["Peace", "War", "Tranquility", "Sundering", "Rage", "Destruction", "Terror", "Doom", "Despair", "Glory", "Victory", "Darkeness", "Light", "Discovery"]
selected_weapon_age = random.choice(weapon_age)

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

def weapon_name(culture):
    print(culture)
    if culture == "Dwarven":
        dwarven_names = ["Graddag Granitefall", "Baridgrami Ashdelver", "Erirnoick Orehead", "Theddumlin Bottlebrand", "Hastom Flintgut", "Brourhal Warmgrog", "Lovraic Bitterbreaker", "Bhagrec Leathercloak", "Nukdruth Lightcloak","Vosgrolin Bloodshield"]
        return random.choice(dwarven_names)
    elif culture == "Elvish":
        elvish_names = ["Iyrandrar Sarmaer","Haryk Olayarus","Elaith Theran","Felaern Enna","Alluin Olofiel","Hagduin Nerirora","Otaehryn Keathyra","Ryo Pawenys","Phaendar Keabalar","Iolas Iarkrana"]
        return random.choice(elvish_names)
    elif culture == "Human":
        human_names = ["Boron","Celestine","Dagmara","Eleanor","Fiona","Gillian","Hannah","Irene","Jasmine","Katherine","Lillian","Maggie","Natalie","Olivia","Pamela","Quinn","Rachel","Samantha","Tanya","Una","Vivian","Wendy","Xaviera","Yvonne","Zoe"]
        return random.choice(human_names)
    elif culture == "Infernal":
        infernal_names = ["Boron","Celestine","Eleanor","Fiona","Gillian","Hannah","Irene","Jasmine","Katherine","Lillian","Maggie","Natalie","Olivia","Pamela","Quinn","Rachel","Samantha","Tanya","Una","Vivian","Wendy","Xaviera","Yvonne","Zoe"]
        return random.choice(infernal_names)
    elif culture == "Gnomish":
        gnomish_names = ["Ipawor Paleback","Sinmin Bellyreach","Yosston Singlespell","Warryn Flukecase","Poybar Sparklecollar","Lokur Dampletomple","Orumop Pugglorebas","Yosyur Wargebas","Tanzu Wusabade","Jordon Wadlenadle"]
        return random.choice(gnomish_names)
    elif culture == "Orcish":
        orcish_names = ["Zorhgigoth","Lob","Xaakt","Dorgarag","Routhu","Yamarz","Rarfu","Cubub","Nagrub","Urzog","Thagsplitter", "SkullCrusher"]
        return random.choice(orcish_names)
    else:
        return "Unknown"

weapon_material = ["hard wood", "dark wood", "exotic wood", "rare stone", "semi-precious gems", "rare metals", " obsidian", "incadescent stone", "silver", "dark matter", "metorite"]

weapon_construction_pattern = ["a helix-shaped", "an interlocking", "a spiral-shaped"]
selected_weapon_construction_pattern = random.choice(weapon_construction_pattern)

weapon_alignment = ["lawful", "neutral", "chaotic", "unaligned", "evil"]
selected_weapon_alignment = random.choice(weapon_alignment)

weapon_personality = ["optimisiticness", "pessimisticness", "jealously", "bloodthirstness", "uncertainty", "self-consciousness"]
selected_weapon_personality = random.choice(weapon_personality)

weapon_sentience = ["sentient", "unsentient"]
selected_weapon_sentience = random.choice(weapon_sentience)

weapon_size = ["tiny", "small", "medium", "large", "huge"]
selected_weapon_size = random.choice(weapon_size)

final_weapon_material = ""
selected_weapon_material = random.sample(weapon_material, random.randint(2,5))
for i in selected_weapon_material:
    final_weapon_material = final_weapon_material + ", " + i
final_weapon_material = final_weapon_material.lstrip(",")
last_comma = final_weapon_material.rfind(",")
final_weapon_material = final_weapon_material[:last_comma] + " and" + final_weapon_material[(last_comma+1):]

weapon_story_1 = "Long ago, during the age of " + selected_weapon_age + ", " + selected_weapon_culture 
weapon_story_2 = "smiths forged " + weapon_name(selected_weapon_culture) + "'s " + selected_weapon_prefix
weapon_story_3 = selected_weapon_heavy_melee + ". Constructed in " + selected_weapon_construction_pattern + " combination of" + final_weapon_material + ", it is clear careful and experienced craftmanship went into the creation."
print(selected_weapon_sentience)
if selected_weapon_sentience == "sentient":
    weapon_story_4 = "This weapon is sentient. Moving your hand near it, you can feel a vague sense of " + selected_weapon_alignment + " " + selected_weapon_personality + "."
else:
    weapon_story_4 = "You detect no magic, sentient or otherwise, within this weapon."


print(weapon_story_1, weapon_story_2, weapon_story_3, weapon_story_4)   

