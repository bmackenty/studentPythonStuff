# this is a procedural generator that makes weapon names and types
import random

weapon_types = ["long sword", "short sword", "dagger", "short bow", "long bow", "staff", "mace", "morning star", "crossbow", "dart", "rapier", "great axe", "two-handed sword"]
weapon_prefix = ["sharp", "broken", "exquisite", "normal", "sentient", "flaming", "frost", "furious", "glowing", "hot", "icy", "lightning", "magic", "mighty", "mystic", "poisoned", "sharp", "silent", "slimy", "sneaky", "sparkling", "thundering", "twilight", "vicious", "wicked", "opinionated", "wrenching", "zealous"]
weapon_previous_owner = ["Votran's", "Anna's", "Gorg's", "Ar'rian's", "Thag's", "Quein's", "Worble's"]

for i in range(10):
    weapon_name = random.choice(weapon_previous_owner) + " +" + str(random.randint(1,3)) + " " + random.choice(weapon_prefix) + " " + random.choice(weapon_types)
    print(weapon_name)
