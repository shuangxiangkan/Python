import sys,pygame,random
from pygame.locals import *


pygame.init()
screen_width=600
screen_height=500
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My_Bomb_Catcher")

bg_color=(0,200,0)
bomb_color=(255,255,0)
catcher_color=(255,0,0)
bomb_radius=25
bomb_x=random.randint(bomb_radius,screen_width-bomb_radius*2)
bomb_y=0
bomb_velocity=0.4

catcher_width=120
catcher_height=50
catcher_x=random.randint(0,screen_width-catcher_width)
catcher_y=screen_height-catcher_height

mouse_position_x=catcher_x
mouse_position_y=catcher_y

score_x=screen_width-120
score_y=5
score_color=(0,0,255)

lives_number=3
lives_x=10
lives_y=5
lives_color=(0,0,255)

score=0
lives=lives_number

game_over=True
font=pygame.font.Font(None,40)
font2=pygame.font.Font(None,30)

pygame.mouse.set_visible(False)

def print_text(font,text,position,color):
    text_image=font.render(text,True,color)
    screen.blit(text_image,position)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,K_ESCAPE):
            sys.exit()
        elif event.type==MOUSEBUTTONUP:
            if game_over:
                game_over=False
        elif event.type==MOUSEMOTION:
            mouse_position_x,mouse_position_y=event.pos


    screen.fill(bg_color)

    if game_over:
        print_text(font,"<CLICK TO START>",(300,200),(255,255,255))
    else:
        bomb_y += bomb_velocity
        catcher_x=mouse_position_x
        # catcher_y=mouse_position_y


        if bomb_y+bomb_radius>catcher_y:
            if bomb_x<catcher_x or bomb_x>catcher_x+catcher_width:
                lives-=1
                if lives<=0:
                    game_over=True
                    lives=lives_number
                    score=0
            else:
                score+=10
            bomb_x = random.randint(bomb_radius, screen_width - bomb_radius * 2)
            bomb_y = 0

        pygame.draw.circle(screen, bomb_color, (bomb_x, int(bomb_y)), bomb_radius, 0)
        pygame.draw.rect(screen, catcher_color, (catcher_x, catcher_y, catcher_width, catcher_height), 0)
        print_text(font2,"SCORE:"+str(score),(score_x,score_y),score_color)
        print_text(font2, "LIVES:" + str(lives), (lives_x, lives_y), lives_color)



    pygame.display.update()