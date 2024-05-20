import random
import noise

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def generate_terrain_map(width, height, scale=100, octaves=6, persistence=0.5, lacunarity=2.0):
    # Use a dictionary to store color codes for different map elements
    colors = {
        'water': (0, 0, 255),
        'land': (0, 255, 0),
        'mountain': (139, 69, 19),
        'forest': (34, 139, 34),
        'desert': (210, 180, 140),
    }

    # Map character symbols
    symbols = {
        'water': '~',
        'land': '#',
        'mountain': '^',
        'forest': '@',
        'desert': '*',
    }

    # Initialize the map
    terrain_map = []

    # Random seed for different map each run
    seed = random.randint(0, 100)

    for y in range(height):
        line = []
        for x in range(width):
            # Generate noise value for each point
            nx = x / scale
            ny = y / scale
            noise_value = noise.pnoise2(nx * octaves, ny * octaves, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=width, repeaty=height, base=seed)
            
            # Assign terrain based on noise value
            if noise_value < -0.3:
                terrain = 'water'
            elif noise_value < 0:
                terrain = 'land'
            elif noise_value < 0.3:
                terrain = 'forest'
            elif noise_value < 0.6:
                terrain = 'mountain'
            else:
                terrain = 'desert'
            
            line.append((terrain, symbols[terrain]))
        terrain_map.append(line)

    return terrain_map, colors

def print_colored_map(terrain_map, colors):
    for line in terrain_map:
        colored_line = ""
        for terrain, symbol in line:
            r, g, b = colors[terrain]
            colored_line += colored(r, g, b, symbol)
        print(colored_line)

# Generate and print the map
width, height = 80, 20
terrain_map, colors = generate_terrain_map(width, height)
print_colored_map(terrain_map, colors)
