import pygame

class Grid:


    
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 45
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()


    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):        
                print(self.grid[row][column], end = " ")
            print()

    def get_cell_colors(self):
        
        grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 214)

        return [grey, green, red, orange, yellow, purple, cyan, blue]

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, 
                self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
#joo elikkäs siis vittu kun esim row = 0 niin:

# print(self.grid[0][column]) / niin grid[0] = [0, 0, 0, 0, 0, 0, 0]
# column printtaa taas ton listan jokasen elementin ja end= " " parametri estää sen, että
# aina kun nolla on printattu niin se ei hyppää seuraavalle riville vaan printtaa kaikki
# nollat samalle riville kunnes koko column looppi on menty läpi XDDD
