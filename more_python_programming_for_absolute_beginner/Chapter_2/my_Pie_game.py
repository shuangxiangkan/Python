import pygame
from pygame.locals import *
import sys
import math

pygame.init()

screen_width=600
screen_heigh=500

bg_color=(255,255,255)
font_color=(0,0,255)

screen=pygame.display.set_mode((screen_width,screen_heigh))
pygame.display.set_caption("my_pie_game")


screen_rect=screen.get_rect()
offset=10

pie_centerx=screen_rect.centerx
pie_centery=screen_rect.centery
radius=200

line_width=4






piece1=False
piece2=False
piece3=False
piece4=False

pie_position=(pie_centerx-radius, pie_centery-radius, radius*2, radius*2)


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==KEYUP:
            if event.key==K_SPACE:
                sys.exit()
            elif event.key==K_1:
                piece1=True
            elif event.key==K_2:
                piece2=True
            elif event.key==K_3:
                piece3=True
            elif event.key==K_4:
                piece4=True



    screen.fill(bg_color)

    font1 = pygame.font.Font(None, 60)
    num1 = font1.render("1", True, font_color)
    font2 = pygame.font.Font(None, 60)
    num2 = font1.render("2", True, font_color)
    font3 = pygame.font.Font(None, 60)
    num3 = font1.render("3", True, font_color)
    font4 = pygame.font.Font(None, 60)
    num4 = font1.render("4", True, font_color)

    screen.blit(num1, (pie_centerx - radius / 2 - offset, pie_centery - radius / 2 - offset))
    screen.blit(num2, (pie_centerx + radius / 2 - offset, pie_centery - radius / 2 - offset))
    screen.blit(num3, (pie_centerx - radius / 2 - offset, pie_centery + radius / 2 - offset))
    screen.blit(num4, (pie_centerx + radius / 2 - offset, pie_centery + radius / 2 - offset))

    if piece1:
        pygame.draw.line(screen, font_color, (pie_centerx, pie_centery - radius), (pie_centerx, pie_centery),
                         line_width)
        pygame.draw.line(screen, font_color, (pie_centerx - radius, pie_centery), (pie_centerx, pie_centery),
                         line_width)
        pygame.draw.arc(screen, font_color, pie_position, math.radians(90), math.radians(180), line_width)

    if piece2:
        pygame.draw.line(screen, font_color, (pie_centerx, pie_centery - radius), (pie_centerx, pie_centery),
                         line_width)
        pygame.draw.line(screen, font_color, (pie_centerx + radius, pie_centery), (pie_centerx, pie_centery),
                         line_width)
        pygame.draw.arc(screen, font_color, pie_position, math.radians(0), math.radians(90), line_width)

    if piece3:
        pygame.draw.line(screen, font_color, (pie_centerx, pie_centery + radius), (pie_centerx, pie_centery),
                         line_width)
        pygame.draw.line(screen, font_color, (pie_centerx - radius, pie_centery), (pie_centerx, pie_centery),
                         line_width)
        pygame.draw.arc(screen, font_color, pie_position, math.radians(180), math.radians(270), line_width)

    if piece4:
        pygame.draw.line(screen, font_color, (pie_centerx, pie_centery + radius), (pie_centerx, pie_centery),
                         line_width)
        pygame.draw.line(screen, font_color, (pie_centerx + radius, pie_centery), (pie_centerx, pie_centery),
                         line_width)
        pygame.draw.arc(screen, font_color, pie_position, math.radians(270), math.radians(360), line_width)


    if piece1 and piece2 and piece3 and piece4:
        font_color=(0,255,0)


    pygame.display.update()