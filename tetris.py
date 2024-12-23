import pygame
import sys
from grid import Grid
pygame.init()

game_grid = Grid()
game_grid.print_grid()

width = 450
height = 900

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

#colors:
white = (200 ,200, 200)
black = (0, 0, 0)
dark_blue = (44, 44, 127)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)

    #drawing shit :DD
    screen.fill(dark_blue)
    game_grid.draw(screen)
