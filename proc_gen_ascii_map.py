import random
# This is very random , with no structure

# Define the possible colors and symbols for the map
colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

# Define the terrain types and their corresponding symbols
terrain_types = [
    ("mountain", "^"),
    ("forest", "*"),
    ("river", "~"),
    ("desert", "#"),
    ("grassland", "."),
    ("plain", " "),
]

# Create a dictionary to map terrain types to symbols
terrain_map = dict(terrain_types)

# Create an empty list to hold the map
map = []

# Define the size of the map
width = 40
height = 20

# Generate the map by filling it with random terrain types and colors
for y in range(height):
    row = []
    for x in range(width):
        terrain = random.choice(terrain_types)[0]
        color = random.choice(colors)
        row.append((terrain, color))
    map.append(row)

# Print the map
for y in range(height):
    for x in range(width):
        terrain, color = map[y][x]
        symbol = terrain_map[terrain]
        print(f"\033[1;3{colors.index(color)}m{symbol}\033[0m", end="")
    print()
