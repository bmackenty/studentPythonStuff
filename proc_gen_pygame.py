import pygame
import numpy as np
from noise import snoise2
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colored Perlin Noise Map with Obstacles")
player_x, player_y = 400, 400
player_size = 5
num_obstacles = 10
obstacle_size = 10
obstacles = []
character_sheet_visible = False
font = pygame.font.SysFont(None, 36)  # Initialize a font for the text display

character_data = {
    "Name": "John Doe",
    "Level": 1,
    "HP": 100,
    "MP": 50,
    "Skills": ["Fireball", "Heal"],
    "Equipment": ["Sword", "Shield"]
}


def draw_character_sheet():
    pygame.draw.rect(WIN, (150, 150, 150), (50, 50, 300, 300))
    
    title_text = font.render("Character Sheet", True, (0, 0, 0))
    WIN.blit(title_text, (150, 60))
    
    y_offset = 90
    for key, value in character_data.items():
        text = f"{key}: {value}"
        info_text = font.render(text, True, (0, 0, 0))
        WIN.blit(info_text, (60, y_offset))
        y_offset += 30


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
        if noise_value < -0.1:
            color = (0, 0, 128)  # Dark blue for deep water
        elif noise_value < 0.1:
            color = (0, 0, 255)  # Light blue for shallow water
        elif noise_value < 0.6:
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
movement_increment = .1  # Smaller increment for smoother movement
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

        # Wrap-around logic
    if new_x < 0:
        new_x = WIDTH - player_size
    elif new_x >= WIDTH:
        new_x = 0
    if new_y < 0:
        new_y = HEIGHT - player_size
    elif new_y >= HEIGHT:
        new_y = 0

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
    # Create a background for the terrain information text
    background_color = (200, 200, 200)  # Light gray
    border_color = (150, 150, 150)  # Darker gray
    text_color = (0, 0, 0)  # Black
    
    # Determine text size to create a background rectangle
    text_surface = font.render(f"Terrain: {terrain_name}", True, text_color)
    text_rect = text_surface.get_rect()
    
    # Draw background rectangle and border
    pygame.draw.rect(WIN, background_color, (text_rect.x + 8, text_rect.y + 8, text_rect.width + 4, text_rect.height + 4))
    pygame.draw.rect(WIN, border_color, (text_rect.x + 8, text_rect.y + 8, text_rect.width + 4, text_rect.height + 4), 1)
    
    # Render and display the text on top of the background
    WIN.blit(text_surface, (text_rect.x + 10, text_rect.y + 10))

    if character_sheet_visible:
        draw_character_sheet()

    pygame.display.update()

pygame.quit()
