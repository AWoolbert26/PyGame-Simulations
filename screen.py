import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 1000
window_height = 500
window_size = (window_width, window_height)

# Create the window
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Conway's Game of Life")

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with white color
    window.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
