import pygame
import numpy as np

J = 3
K = 2
L = 3
gameState = 0

scaler = 20
class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.size = (self.rows + 1, self.columns + 1)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset
        self.font_name = pygame.font.get_default_font()

    def StartGrid(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = 0


    def Conway(self, off_color, on_color, surface, pause):
        global gameState
        ### Conway
        if gameState == 0:
            for x in range(self.rows):
                for y in range(self.columns):
                    y_pos = y * self.scale
                    x_pos = x * self.scale
                    if self.grid_array[x][y] == 1:
                        pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    else:
                        pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

            next = np.ndarray(shape=(self.size))
            if pause == False:
                for x in range(self.rows):
                    for y in range(self.columns):
                        state = self.grid_array[x][y]
                        neighbours = self.get_neighbours(x, y)
                        #if the cell is dead, and has 3 alive neighbors
                        if state == 0 and neighbours == J:
                            next[x][y] = 1
                        #if the cell is alive, and has less than 2 or more than 3 alive neighbors
                        elif state == 1 and (neighbours < K or neighbours > L):
                            next[x][y] = 0
                        #if the cell is dead and doesnt have 3 alive neighbors, or alive with 2 or 3 alive nieghbors
                        else:
                            next[x][y] = state
                self.grid_array = next
        ### Rule 30 Wolfram
        elif gameState == 1:
            for x in range(self.rows):
                for y in range(self.columns):
                    y_pos = y * self.scale
                    x_pos = x * self.scale
                    if self.grid_array[x][y] == 1:
                        pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    else:
                        pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

            next = np.ndarray(shape=(self.size))
            if pause == False:
                for x in range(self.rows):
                    for y in range(self.columns):
                        state = self.grid_array[x][y]
                        #Wolfram Rule 30 Logic
                        if self.grid_array[x-1][y] == 0 and self.grid_array[x][y] == 0 and self.grid_array[x+1][y] == 0:
                            self.grid_array[x][y+1] = 0
                        #    print("a")
                        elif self.grid_array[x-1][y] == 1 and self.grid_array[x][y] == 1 and self.grid_array[x+1][y] == 1:
                            self.grid_array[x][y+1] = 0
                        #    print("b")
                        elif self.grid_array[x-1][y] == 1 and self.grid_array[x][y] == 1 and self.grid_array[x+1][y] == 0:
                            self.grid_array[x][y+1] = 0
                        #    print("c")
                        elif self.grid_array[x-1][y] == 1 and self.grid_array[x][y] == 0 and self.grid_array[x+1][y] == 1:
                            self.grid_array[x][y+1] = 0
                        #    print("d")
                        elif self.grid_array[x-1][y] == 1 and self.grid_array[x][y] == 0 and self.grid_array[x+1][y] == 0:
                            self.grid_array[x][y+1] = 1
                        #    print("e")
                        elif self.grid_array[x-1][y] == 0 and self.grid_array[x][y] == 1 and self.grid_array[x+1][y] == 1:
                            self.grid_array[x][y+1] = 1
                        #    print("f")
                        elif self.grid_array[x-1][y] == 0 and self.grid_array[x][y] == 1 and self.grid_array[x+1][y] == 0:
                            self.grid_array[x][y+1] = 1
                          #  print("g")
                        elif self.grid_array[x-1][y] == 0 and self.grid_array[x][y] == 0 and self.grid_array[x+1][y] == 1:
                            self.grid_array[x][y+1] = 1
                        #    print("h")

        ### Rule 82
        else:
            for x in range(self.rows):
                for y in range(self.columns):
                    y_pos = y * self.scale
                    x_pos = x * self.scale
                    if self.grid_array[x][y] == 1:
                        pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    else:
                        pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

            next = np.ndarray(shape=(self.size))
            if pause == False:
                for x in range(self.rows):
                    for y in range(self.columns):
                        state = self.grid_array[x][y]
                        #Rule 82 Logic
                        if self.grid_array[x-1][y] == 0 and self.grid_array[x][y] == 0 and self.grid_array[x+1][y] == 0:
                            self.grid_array[x][y+1] = 0
                        #    print("a")
                        elif self.grid_array[x-1][y] == 1 and self.grid_array[x][y] == 1 and self.grid_array[x+1][y] == 1:
                            self.grid_array[x][y+1] = 0
                        #    print("b")
                        elif self.grid_array[x-1][y] == 1 and self.grid_array[x][y] == 1 and self.grid_array[x+1][y] == 0:
                            self.grid_array[x][y+1] = 1
                        #    print("c")
                        elif self.grid_array[x-1][y] == 1 and self.grid_array[x][y] == 0 and self.grid_array[x+1][y] == 1:
                            self.grid_array[x][y+1] = 0
                        #    print("d")
                        elif self.grid_array[x-1][y] == 1 and self.grid_array[x][y] == 0 and self.grid_array[x+1][y] == 0:
                            self.grid_array[x][y+1] = 1
                        #    print("e")
                        elif self.grid_array[x-1][y] == 0 and self.grid_array[x][y] == 1 and self.grid_array[x+1][y] == 1:
                            self.grid_array[x][y+1] = 0
                        #    print("f")
                        elif self.grid_array[x-1][y] == 0 and self.grid_array[x][y] == 1 and self.grid_array[x+1][y] == 0:
                            self.grid_array[x][y+1] = 0
                          #  print("g")
                        elif self.grid_array[x-1][y] == 0 and self.grid_array[x][y] == 0 and self.grid_array[x+1][y] == 1:
                            self.grid_array[x][y+1] = 1
                        #    print("h")

    def HandleLeftClick(self, x, y):
        _x = x//self.scale
        _y = y//self.scale

        if self.grid_array[_x][_y] == 0:
            self.grid_array[_x][_y] = 1

    def HandleRightClick(self, x, y):
        _x = x//self.scale
        _y = y//self.scale

        if self.grid_array[_x][_y] == 1:
            self.grid_array[_x][_y] = 0
        

    def WipeBoard(self, x, y):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = 0
        
        
    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total

    def cellCycle(self):
        global gameState
        if gameState == 0:
            gameState = 1
        elif gameState == 1:
            gameState = 2
        else:
            gameState = 0
        return


    