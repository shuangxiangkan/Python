import pygame
from pygame.locals import *
import sys
import math

pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Arcs")

# background color of screen
bg_color=(0,0,200)
Arc_color=(100,255,200)
# set the position of Arc
position=(200,150,200,200)

# convert the degree to radian
start_angle=math.radians(0)
end_angle=math.radians(180)

# line widht
width=8

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill(bg_color)

    # draw the arc
    pygame.draw.arc(screen,Arc_color,position,start_angle,end_angle,width)

    pygame.display.update()



