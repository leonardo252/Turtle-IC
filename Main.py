from Grid import Grid
from Background import Background
from Turtle import Turtle
from random import randint
import pygame
import time

print("Novo Python\n")
# screen.get_size()

pygame.init()
pygame.display.set_caption('Turtle of IC')

size = width, height = 680, 680
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])

grid = Grid()
background = Background()
turtle = Turtle(40, 40, 45, 45)
moves = ["up", "down", "left", "right"]

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    background.drawBackground(screen)    
    grid.drawGrid(screen)

    screen.blit(turtle.image, turtle.rect)

    move = randint(0,3)
    turtle.moveTurtle(moves[move])
    
    pygame.display.flip()

    time.sleep(0.2)
