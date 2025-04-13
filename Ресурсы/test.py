import pygame as pg
import random
import time

pg.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

WIDTH, HEIGHT = 1000, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
snake_block = 20
clock = pg.time.Clock()

font_style = pg.font.SysFont(None, 25)
score_font = pg.font.SysFont(None, 35)

def u_score(score):
    val = score_font.render("Your score"+str(score), True, yellow)
    screen.blit(val, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])
def message(text, color):
    mesg = font_style.render(text, True, color)
    screen.blit(mesg, [WIDTH//6, HEIGHT//3])
def choos_dif():
    screen.fill(blue)
    message("choose the level, 1  , 2  , 3", yellow)
    pg.display.update()
    while True:
        for e in pg.event.get():
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_1:
                    return 10
                if e.key == pg.K_2:
                    return 15
                if e.key == pg.K_3:
                    return 20
def Pause():
    pause = True
    message("q to quit , p to return", yellow)
    pg.display.update()
    while pause:
        for e in pg.event.get():
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_q:
                    pg.quit()
                    quit()
                if e.key == pg.K_p:
                    pause = False
def game():
    game_over = False
    game_close = False

    speed = choos_dif()

    x1 = WIDTH//2
    y1 = HEIGHT//2

    x2 = 0
    y2 = 0

    snake_list = []
    len_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block)/20)*20.0
    foody = round(random.randrange(0, HEIGHT - snake_block)/20)*20.0

    while not game_over:
        while game_close:
            screen.fill(blue)
            message("you lose q to quit, r to restart", yellow)
            u_score(len_snake-1)
            pg.display.update()
            for e in pg.event.get():
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if e.key == pg.K_r:
                        game_over = False
                        game_close = False
                        game()
        for e in pg.event.get():
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    x2 = -snake_block
                    y2 = 0
                elif e.key == pg.K_RIGHT:
                    x2 = snake_block
                    y2 = 0
                elif e.key == pg.K_UP:
                    x2 = 0
                    y2 = -snake_block
                elif e.key == pg.K_DOWN:
                    x2 = 0
                    y2 = snake_block
                elif e.key == pg.K_p:
                    Pause()

        if x1 < 0 or x1 > WIDTH or y1 < 0 or y1 > HEIGHT:
            game_close = True
        x1 += x2
        y1 += y2
        screen.fill(blue)
        pg.draw.rect(screen, yellow, [foodx, foody, snake_block, snake_block])
        snake_h = []
        snake_h.append(x1)
        snake_h.append(y1)
        snake_list.append(snake_h)
        if len(snake_list) > len_snake:
            del snake_list[0]
        
        if snake_h in snake_list[:-1]:
            game_close = True
        
        draw_snake(snake_block, snake_list)
        u_score(len_snake-1)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH-snake_block)/20)*20.0
            foody = round(random.randrange(0, HEIGHT-snake_block)/20)*20.0
            len_snake += 1

        pg.display.update()
        clock.tick(speed)
    pg.quit()
    quit()
game()
