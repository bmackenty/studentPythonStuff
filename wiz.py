import pygame

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((900, 700))

# Set the game title
pygame.display.set_caption("Wizardry 2")

# Create a font for text
font = pygame.font.Font(None, 30)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define some rectangles for the UI sections
status_rect = pygame.Rect(5, 5, 890, 100)
map_rect = pygame.Rect(5, 120, 430, 400)
commands_rect = pygame.Rect(450, 120, 445, 400)
characters_rect = pygame.Rect(5, 530, 890, 155)


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
    screen.blit(text, (10, 130))

    text = font.render("Commands", True, WHITE)
    screen.blit(text, (458, 130))

    text = font.render("Characters", True, WHITE)
    screen.blit(text, (10, 600-80))
        # Render text to the characters section
    text = font.render("Character 1", True, WHITE)
    screen.blit(text, (10, 550))
        # Render text to the characters section
    text = font.render("Character 2", True, WHITE)
    screen.blit(text, (10, 570))
    text = font.render("Character 3", True, WHITE)
    screen.blit(text, (10, 590))
    text = font.render("Character 4", True, WHITE)
    screen.blit(text, (10, 610))
    
    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
