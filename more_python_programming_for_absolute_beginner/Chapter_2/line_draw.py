import pygame
from pygame.locals import *
import sys

pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")

# background color of screen
bg_color=(0,80,0)
line_color=(100,255,200)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill(bg_color)

    # draw the line
    width=8
    pygame.draw.line(screen,line_color,(100,100),(500,400),width)

    pygame.display.update()
