import pygame
import random

# Initialize pygame
pygame.init()

# Set the dimensions of the canvas
WIDTH, HEIGHT = 512, 512
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Pixel Art")

# Function to generate a random color
def random_color(num_1, num_2):
    w = num_1
    h = num_2
    x = (w + h) % 256
    return (random.randint(0, x), random.randint(0, x), random.randint(0, x))

# Fill the canvas with randomly colored pixels
for y in range(HEIGHT):
    for x in range(WIDTH):
        color = random_color(y,x)
        canvas.set_at((x, y), color)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the canvas on the display
    pygame.display.flip()

# Clean up
pygame.quit()
