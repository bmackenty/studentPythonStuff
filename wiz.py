import pygame

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))

# Set the game title
pygame.display.set_caption("Wizardry 2")

# Create a font for text
font = pygame.font.Font(None, 30)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define some rectangles for the UI sections
status_rect = pygame.Rect(0, 0, 800, 100)
map_rect = pygame.Rect(0, 100, 400, 400)
commands_rect = pygame.Rect(400, 100, 400, 400)
characters_rect = pygame.Rect(0, 500, 800, 100)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the white borders around the sections
    pygame.draw.rect(screen, WHITE, status_rect, 2)
    pygame.draw.rect(screen, WHITE, map_rect, 2)
    pygame.draw.rect(screen, WHITE, commands_rect, 2)
    pygame.draw.rect(screen, WHITE, characters_rect, 2)

    # Render some text to the screen
    text = font.render("Status", True, WHITE)
    screen.blit(text, (10, 10))

    text = font.render("Map", True, WHITE)
    screen.blit(text, (10, 110))

    text = font.render("Commands", True, WHITE)
    screen.blit(text, (410, 110))

    text = font.render("Characters", True, WHITE)
    screen.blit(text, (10, 600-90))
    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
