import random,time,sys
import pygame
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("My_Keyboard_Demo")


score=0
game_over=True
character_answer=97 # 'a'
start_time=time.time()
totle_time=11


font1=pygame.font.Font(None,30)
font2=pygame.font.Font(None,200)


def print_text(font,text,color,position):
    text=font.render(text,True,color)
    screen.blit(text,position)


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_SPACE:
                sys.exit()

    keys=pygame.key.get_pressed()

    screen.fill((0, 100, 0))

    # start the game
    if keys[K_RETURN]:
        game_over=False
        score = 0

    time_interval = time.time() - start_time

    if not game_over:
        if keys[character_answer]:
            character_answer=random.randint(97,122)
            score+=1
        if totle_time >= time_interval:
            print_text(font1, "Time: " + str(int(totle_time - time_interval)), (255, 255, 255), (0, 130))
        else:
            game_over = True
            start_time=time.time()

    else:
        print_text(font1,"Press Enter to start...",(255,255,255),(0,180))





    print_text(font1,"Let's see how fast you can type",(255,255,255),(0,0))
    print_text(font1,"Try to keep up for 10 seconds",(255,255,255),(0,30))
    print_text(font1,"Speed: "+str(int(score))+" letters/min",(255,255,255),(0,150))

    # chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
    print_text(font2,str(chr(character_answer-32)),(255,255,0),(20,220))

    # time_interval=time.time()-start_time
    # if totle_time >= time_interval and not game_over:
    #     print_text(font1,"Time: "+str(int(totle_time-time_interval)),(255,255,255),(0,130))
    # else:
    #     game_over=True
    #     start_time=time.time()


    pygame.display.update()
