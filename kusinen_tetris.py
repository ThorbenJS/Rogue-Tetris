import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Grid parameters
CELL_SIZE = 40  # Size of each cell
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):  # Vertical lines
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):  # Horizontal lines
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Main loop
while True:
    screen.fill(BLACK)  # Clear screen

    draw_grid()  # Draw grid
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()  # Update display


#muoto1
l = 1