import sys
import pygame
from pygame.locals import *
from My_Trivia_Class import my_trivia

def trivia_game():

    pygame.init()
    # set the width and height of the screen
    screen = pygame.display.set_mode((600, 500))
    # set the name of the screeen
    pygame.display.set_caption("My_Trivia_Game")

    # screen background color
    bg_color = (0, 0, 200)

    # color of font
    white=(255,255,255)
    yellow=(255,255,0)
    green=(0, 255, 0)
    red=(255,0,0)

    colors=[white,yellow,green,red]

    tri = my_trivia("trivia_data.txt",screen,colors)
    tri.read_file_content()

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    sys.exit()
                elif event.key==K_1:
                    tri.hand_input(1)
                elif event.key==K_2:
                    tri.hand_input(2)
                elif event.key==K_3:
                    tri.hand_input(3)
                elif event.key==K_4:
                    tri.hand_input(4)
                elif event.key==K_RETURN:
                    tri.hand_input(-1)

        # set background color
        screen.fill(bg_color)

        tri.context()

        pygame.display.update()




trivia_game()