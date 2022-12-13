# this is a procedural generator that makes weapon names and types
import random
import os
os.system("clear")

weapon_culture = ["Dwarven", "Elvish", "Human", "Infernal", "Gnomish", "Orcish"]
selected_weapon_culture = random.choice(weapon_culture)

weapon_age = ["Peace", "War", "Tranquility", "Sundering", "Rage", "Destruction", "Terror", "Doom", "Despair", "Glory", "Victory", "Darkeness", "Light", "Discovery"]
selected_weapon_age = random.choice(weapon_age)

weapon_category = ["ranged", "light_melee", "heavy_melee", "magic", "thrown"]
selected_weapon_category = random.choice(weapon_category)

weapon_types_ranged = ["short bow", "long bow", "crossbow"]
selected_weapon_ranged= random.choice(weapon_types_ranged)

weapon_types_thrown = ["javelin", "throwing axe", "throwing hammer", "throwing knife", "throwing spear", "dart", "sling"]
selected_weapon_thrown = random.choice(weapon_types_thrown)

weapon_types_light_melee = ["short sword", "dagger", "staff","rapier", "scimitar", "sickle", "whip"]
selected_weapon_light_melee = random.choice(weapon_types_light_melee)

weapon_types_heavy_melee = ["great sword", "mace", "morning star", "great axe", "two-handed sword", "war hammer","mighty-club-of-clubbing"]
selected_weapon_heavy_melee = random.choice(weapon_types_heavy_melee)

weapon_types_magic = ["wand","staff"]
selected_weapon_magic = random.choice(weapon_types_magic)

weapon_prefix = ["sharp", "broken", "exquisite", "normal", "flaming", "frosty", "furious", "glowing"]
selected_weapon_prefix = random.choice(weapon_prefix)

if selected_weapon_prefix == "sharp":
    weapon_crunch = "This weapon does " + str(random.randint(1,4)) + "d6 damage."
elif selected_weapon_prefix == "broken":
    weapon_crunch = "Without extraordinary (and most likely skillful) repair from a " + selected_weapon_culture + " blacksmith, this weapon will crumble into little tiny pieces."
elif selected_weapon_prefix == "exquisite":
    weapon_crunch = "This weapon is a masterpiece of craftsmanship, and is a veritable work of art. You have +2 on any rolls to pick up romantic partners while holding this weapon."
elif selected_weapon_prefix == "normal":
    weapon_crunch = "This weapon is normal, but very beautiful. It does normal damage."
elif selected_weapon_prefix == "flaming":
    weapon_crunch = "This weapon is aflame, and does " + str(random.randint(1,4)) + "d6 fire damage."
elif selected_weapon_prefix == "frosty":
    weapon_crunch = "This weapon radiates cold, and does " + str(random.randint(1,4)) + "d6 frost damage."
elif selected_weapon_prefix == "furious":
    weapon_crunch = "Once this weapon hits an enemy, that enemy will relentlessly attack whomever wields the weapon."
elif selected_weapon_prefix == "glowing":
    weapon_crunch = "This weapon is glowing, It will glow when there is no danger or risk to the owner. When there is even the slightest hint of danger, it will stop glowing."
elif selected_weapon_prefix == "flaming":
    weapon_crunch = "This weapon is aflame, and does " + str(random.randint(1,4)) + "d6 fire damage."
# BILL start working here


def weapon_name(culture):
    if culture == "Dwarven":
        dwarven_names = ["Graddag Granitefall", "Baridgrami Ashdelver", "Erirnoick Orehead", "Theddumlin Bottlebrand", "Hastom Flintgut", "Brourhal Warmgrog", "Lovraic Bitterbreaker", "Bhagrec Leathercloak", "Nukdruth Lightcloak","Vosgrolin Bloodshield"]
        return random.choice(dwarven_names)
    elif culture == "Elvish":
        elvish_names = ["Iyrandrar Sarmaer","Haryk Olayarus","Elaith Theran","Felaern Enna","Alluin Olofiel","Hagduin Nerirora","Otaehryn Keathyra","Ryo Pawenys","Phaendar Keabalar","Iolas Iarkrana"]
        return random.choice(elvish_names)
    elif culture == "Human":
        human_names = ["Adrian", "Amber", "Tyler", "Devon", "Boron","Celestine","Dagmara","Eleanor","Fiona","Gillian","Hannah","Irene","Jasmine","Katherine","Lillian","Maggie","Natalie","Olivia","Pamela","Quinn","Rachel","Samantha","Tanya","Una","Vivian","Wendy","Xaviera","Yvonne","Zoe"]
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

weapon_personality = ["optimisiticness", "pessimisticness", "jealously", "bloodthirstyness", "uncertainty", "self-consciousness"]
selected_weapon_personality = random.choice(weapon_personality)

weapon_sentience = ["sentient", "unsentient"]
selected_weapon_sentience = random.choice(weapon_sentience)
if weapon_category == "magic":
    selected_weapon_sentience = "sentient"

weapon_size = ["tiny", "small", "medium", "large", "huge"]
selected_weapon_size = random.choice(weapon_size)

final_weapon_material = ""
selected_weapon_material = random.sample(weapon_material, random.randint(2,5))
for i in selected_weapon_material:
    final_weapon_material = final_weapon_material + ", " + i
final_weapon_material = final_weapon_material.lstrip(",")
last_comma = final_weapon_material.rfind(",")
final_weapon_material = final_weapon_material[:last_comma] + " and" + final_weapon_material[(last_comma+1):]

weapon_past_event_1 = {
    1: "At one point in this weapon's history it was in a young dragon's horde. It is unknown if the dragon continues to look for it.", 
    2: "For 30 years, this weapon was used as a table ornament in the modest home of Prince Fumbledick, who was unaware of it's importance.", 
    3: "This weapon was once stolen by a goblin. When the litch who owned the weapon found the goblin, he punished the golbin severely, which is why goblin soup is now a popular dish amongst evil wizards and litches.",
    4: "This weapon was once wielded by a young Kawian apprentice, who later became a fearsome warrior.",
    5: "For 1000 years, this weapon was displayed in an Elvish museum of ancient antiquities.",
    6: "When this weapon was created, the blacksmith had great regret for the pain it would cause. She asked the Gods for forgiveness. They declined to forgive her, so she swore never to craft another weapon again.",
    7: "This weapon was used by Gnarl Tooth Fang in the battle of lost hope during the 8th Great War."
}

selected_past_event_1 = random.choice(list(weapon_past_event_1.values()))


# ========= build weapon story here =========

weapon_story_1 = "Long ago, during the age of " + selected_weapon_age + ", " + selected_weapon_culture 
weapon_story_2 = "smiths forged " + weapon_name(selected_weapon_culture) + "'s " + selected_weapon_prefix
if selected_weapon_category == "ranged":
    weapon_story_3 = selected_weapon_ranged + ". The wood on this weapon is constructed in " + selected_weapon_construction_pattern + " combination of" + final_weapon_material + ", it is clear careful and extraordinary craftmanship went into the creation. " + weapon_crunch
elif selected_weapon_category == "light_melee":
    weapon_story_3 = selected_weapon_light_melee + ". Elegantly crafted in " + selected_weapon_construction_pattern + " combination of" + final_weapon_material + ", it is clear careful and extraordinary craftmanship went into the creation. " + weapon_crunch
elif selected_weapon_category == "heavy_melee":
    weapon_story_3 = selected_weapon_heavy_melee + ". he handle is constructed in " + selected_weapon_construction_pattern + " combination of" + final_weapon_material + ", it is clear careful and extraordinary craftmanship went into the creation. " + weapon_crunch
elif selected_weapon_category == "magic":
    weapon_story_3 = selected_weapon_magic + ". Constructed in " + selected_weapon_construction_pattern + " combination of" + final_weapon_material + ", it is clear careful and extraordinary craftmanship went into the creation. " + weapon_crunch
elif selected_weapon_category == "thrown":
    weapon_story_3 = selected_weapon_thrown + ". Constructed in " + selected_weapon_construction_pattern + " combination of" + final_weapon_material + ", it is clear careful and extraordinary craftmanship went into the creation. " + weapon_crunch



weapon_story_4 = "This weapon is sentient. Moving your hand near it, you can feel a vague sense of " + selected_weapon_alignment + " " + selected_weapon_personality + "."


weapon_story_5 = selected_past_event_1

print(weapon_story_1, weapon_story_2, weapon_story_3, weapon_story_4, weapon_story_5)   
