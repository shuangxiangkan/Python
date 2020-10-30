import pygame
import sys
from pygame.locals import *



pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("My_Mouse_Demo")


font=pygame.font.Font(None,24)
mouse_x=mouse_y=0
mouse_rel_x=mouse_rel_y=0
mouse_down_x=mouse_down_y=0
mouse_up_x=mouse_up_y=0
mouse_down=mouse_up=0

def print_text(font,text,position,color):
    text_image=font.render(text,True,color)
    screen.blit(text_image,position)


while True:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE:
            sys.exit()
        elif event.type==MOUSEMOTION:
            mouse_x,mouse_y=event.pos
            mouse_rel_x,mouse_rel_y=event.rel
        elif event.type==MOUSEBUTTONDOWN:
            mouse_down=event.button
            mouse_down_x,mouse_down_y=event.pos
        elif event.type==MOUSEBUTTONUP:
            mouse_up=event.button
            mouse_up_x,mouse_up_y=event.pos





    screen.fill((0,100,0))

    print_text(font, "Mouse Events", (5, 5), (255, 255, 0))
    print_text(font, "Mouse position: ("+str(mouse_x)+","+str(mouse_y)+")", (5, 25), (255, 255, 0))
    print_text(font, "Mouse relative: ("+str(mouse_rel_x)+","+str(mouse_rel_y)+")", (5, 45), (255, 255, 0))
    print_text(font, "Mouse button down: "+str(mouse_down)+" at ("+str(mouse_down_x)+","+str(mouse_down_y)+")", (5, 65), (255, 255, 0))
    print_text(font, "Mouse button up: "+str(mouse_up)+" at ("+str(mouse_up_x)+","+str(mouse_up_y)+")", (5, 85), (255, 255, 0))


    x,y=pygame.mouse.get_pos()
    b1,b2,b3=pygame.mouse.get_pressed()


    print_text(font, "Mouse Polling", (5, 150), (255, 255, 0))
    print_text(font, "Mouse position: ("+str(x)+","+str(y)+")", (5, 170), (255, 255, 0))
    print_text(font, "Mouse buttons: ("+str(b1)+","+str(b2)+str(b3)+")", (5, 190), (255, 255, 0))

    pygame.display.update()