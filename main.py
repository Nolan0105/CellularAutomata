import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 1920,1080
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 0, 10)
#blue1 = (0,0,0)
white = (200, 200, 200)

scaler = 20
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.StartGrid()

pause = True
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_BACKSPACE:
                mouseX, mouseY = pygame.mouse.get_pos()
                Grid.WipeBoard(mouseX, mouseY)
            if event.key == pygame.K_s:
                Grid.cellCycle()
              

    
    Grid.Conway(off_color=blue, on_color=white, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleLeftClick(mouseX, mouseY)

    if pygame.mouse.get_pressed()[2]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleRightClick(mouseX, mouseY)


    pygame.display.update()

pygame.quit()

