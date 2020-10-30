import sys,math,pygame,datetime
from pygame.locals import *

pygame.init()

screen_width=600
screen_height=500
center_x=int(screen_width/2)
center_y=int(screen_height/2)
radius=240
orange=(220,180,0)
white=(255,255,255)
yellow=(255,255,0)
pink=(255,100,100)


screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My_Clock_Demo")

font=pygame.font.Font(None,36)


def print_text(font,text,positoin,color):
    text_image = font.render(text, True, color)
    screen.blit(text_image,positoin)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill((0, 0, 100))

    # draw the circle
    pygame.draw.circle(screen, white, (center_x, center_y), radius, 10)

    # draw the number 1~12
    for i in range(1, 13):
        number_position_x = math.cos(math.radians(i * (360 / 12) - 90)) * (radius - 20) - 10
        number_position_y = math.sin(math.radians(i * (360 / 12) - 90)) * (radius - 20) - 10
        print_text(font, str(i), (center_x + number_position_x, center_y + number_position_y), white)

    # get the current time
    now_time = datetime.datetime.now()


    # draw the hour hand
    now_hour = now_time.hour
    hour_position_x = math.cos(math.radians(now_hour * (360 / 12) - 90)) * (radius - 70)
    hour_position_y = math.sin(math.radians(now_hour * (360 / 12) - 90)) * (radius - 70)
    pygame.draw.line(screen, pink, (center_x, center_y), (center_x + hour_position_x, center_y + hour_position_y), 20)

    # draw the minute hand
    now_minute = now_time.minute
    minute_position_x = math.cos(math.radians(now_minute * (360 / 60) - 90)) * (radius - 50)
    minute_position_y = math.sin(math.radians(now_minute * (360 / 60) - 90)) * (radius - 50)
    pygame.draw.line(screen, yellow, (center_x, center_y), (center_x + minute_position_x, center_y + minute_position_y), 10)

    # draw the minute hand
    now_second = now_time.second
    second_position_x = math.cos(math.radians(now_second * (360 / 60) - 90)) * (radius - 30)
    second_position_y = math.sin(math.radians(now_second * (360 / 60) - 90)) * (radius - 30)
    pygame.draw.line(screen, orange , (center_x, center_y), (center_x + second_position_x, center_y + second_position_y),
                     3)

    # cover the center point
    pygame.draw.circle(screen,white,(center_x,center_y),20)

    # display time in digital form in the upper left corner of the screen
    time_string=""+str(now_time.hour)+":"+str(now_time.minute)+":"+str(now_time.second)
    print_text(font,time_string,(5,5),white)


    pygame.display.update()