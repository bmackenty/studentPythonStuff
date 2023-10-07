import pygame
import numpy as np
from noise import snoise2
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colored Perlin Noise Map with Obstacles")
player_x, player_y = 200, 200
player_size = 10
num_obstacles = 10
obstacle_size = 10
obstacles = []
character_sheet_visible = False
font = pygame.font.SysFont(None, 36)  # Initialize a font for the text display


def draw_character_sheet():
    pygame.draw.rect(WIN, (150, 150, 150), (50, 50, 300, 300))
    character_text = font.render("Character Sheet", True, (0, 0, 0))
    WIN.blit(character_text, (150, 60))


def get_terrain_name(color):
    if color == (0, 0, 128):
        return "Deep Water"
    elif color == (0, 0, 255):
        return "Shallow Water"
    elif color == (34, 139, 34):
        return "Land"
    elif color == (139, 69, 19):
        return "Mountains"
    else:
        return "Unknown"


# Generate a random seed for Perlin noise
random_seed = random.randint(0, 10000)

# Generate Perlin noise map
grid = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)
for i in range(WIDTH):
    for j in range(HEIGHT):
        noise_value = snoise2(x=i / 40.0, y=j / 40.0, octaves=6, persistence=0.5, lacunarity=2.0, base=random_seed)
        
        # Map noise_value to a color
        if noise_value < -0.5:
            color = (0, 0, 128)  # Dark blue for deep water
        elif noise_value < 0:
            color = (0, 0, 255)  # Light blue for shallow water
        elif noise_value < 0.5:
            color = (34, 139, 34)  # Green for land
        else:
            color = (139, 69, 19)  # Brown for mountains

        grid[i, j] = color

# Generate random obstacles
for _ in range(num_obstacles):
    x, y = random.randint(0, WIDTH - obstacle_size), random.randint(0, HEIGHT - obstacle_size)
    obstacles.append((x, y))


# Main loop
run = True
movement_increment = 0.2  # Smaller increment for smoother movement
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                character_sheet_visible = not character_sheet_visible

    keys = pygame.key.get_pressed()
    new_x, new_y = player_x, player_y

    if keys[pygame.K_LEFT]:
        new_x -= movement_increment
    if keys[pygame.K_RIGHT]:
        new_x += movement_increment
    if keys[pygame.K_UP]:
        new_y -= movement_increment
    if keys[pygame.K_DOWN]:
        new_y += movement_increment

    # Check for collisions with obstacles
    for ox, oy in obstacles:
        if pygame.Rect(new_x, new_y, player_size, player_size).colliderect(pygame.Rect(ox, oy, obstacle_size, obstacle_size)):
            new_x, new_y = player_x, player_y
            break

    player_x, player_y = new_x, new_y

    # Draw everything
    pygame.surfarray.blit_array(WIN, grid)
    pygame.draw.rect(WIN, (255, 0, 0), (int(player_x), int(player_y), player_size, player_size))
    
    for ox, oy in obstacles:
        pygame.draw.rect(WIN, (0, 0, 0), (ox, oy, obstacle_size, obstacle_size))


        # Get the terrain under the player
    terrain_color = tuple(grid[int(player_x)][int(player_y)])
    terrain_name = get_terrain_name(terrain_color)

    # Render and display the text
    text_surface = font.render(f"Terrain: {terrain_name}", True, (255, 255, 255))
    WIN.blit(text_surface, (10, 10))

    if character_sheet_visible:
        draw_character_sheet()

    pygame.display.update()

pygame.quit()
