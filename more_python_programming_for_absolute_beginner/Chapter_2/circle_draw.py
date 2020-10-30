import pygame
from pygame.locals import *
import sys

pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("circle")

bg_color=(60,60,60)
circle_color=(255,0,0)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()


    # fill the background color
    screen.fill(bg_color)


    # draw the circle
    position=(300,250)
    radius=100
    width=1
    pygame.draw.circle(screen,circle_color,position,radius,width)

    pygame.display.update()