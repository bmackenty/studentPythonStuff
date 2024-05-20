def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

# Define map elements with colors
def generate_map():
    # Use a dictionary to store color codes for different map elements
    colors = {
        'water': (0, 0, 255),
        'land': (0, 255, 0),
        'mountain': (139, 69, 19),
        'forest': (34, 139, 34),
        'desert': (210, 180, 140),
    }

    # Define a small ASCII map
    map_data = [
        "~~~~~~^^^^^^^",
        "~~~~~~^^^^^^^",
        "~~~~~~^^^^^^^",
        "~~~######^^^~",
        "~~########~~#",
        "~~#######~~~#",
        "~~~######~~~#",
        "~~~~~~~^^^^^^",
        "~~~~~~~^^^^^^",
        "~~~~~~~^^^^^^",
    ]

    # Convert map characters to colored text
    color_map = {
        '~': colors['water'],
        '#': colors['land'],
        '^': colors['mountain'],
        '@': colors['forest'],
        '*': colors['desert'],
    }

    for line in map_data:
        colored_line = ""
        for char in line:
            if char in color_map:
                r, g, b = color_map[char]
                colored_line += colored(r, g, b, char)
            else:
                colored_line += char
        print(colored_line)

# Generate and print the map
generate_map()
