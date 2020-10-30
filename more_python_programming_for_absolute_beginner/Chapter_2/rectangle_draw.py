import pygame
from pygame.locals import *
import sys

pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Rectangles")

pos_x=300
pos_y=250
vel_x=2
vel_y=10

bg_color=(0,0,200)
rectangle_color=(255,255,0)


while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()


    screen.fill(bg_color)

    # move the rectangle
    pos_x+=vel_x
    pos_y+=vel_y

    # keep rectangle on the screen
    if pos_x>screen.get_rect().right or pos_x<screen.get_rect().left:
    # if pos_x>500 or pos_x<0:
        vel_x=vel_x*(-1)
    elif pos_y>screen.get_rect().top or pos_y<screen.get_rect().bottom:
    # if pos_y>400 or pos_y<0:
        vel_y=vel_y*(-1)

    # draw the rectangle
    width=0 # solid fill
    rectangle_position = (pos_x, pos_y, 100, 100)
    pygame.draw.rect(screen,rectangle_color,rectangle_position,width)


    pygame.display.update()

