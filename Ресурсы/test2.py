import pygame as pg
import random 
import sys

pg.init()

WIDTH = 800
HEIGHT = 600

CAR_WIDTH = 30
CAR_HEIGHT = 70
COIN_R = 20

LANES = [216, 337, 464, 594]  # Полосы движения

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


car_img = pg.image.load("car.png")
car_img = pg.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))

obs_img = pg.image.load("car2.png")
obs_img = pg.transform.scale(obs_img, (CAR_WIDTH, CAR_HEIGHT))

coin_img = pg.image.load("coin.png")
coin_img = pg.transform.scale(coin_img, (COIN_R, COIN_R))

bg_img = pg.image.load("street.png")
bg_img = pg.transform.scale(bg_img, (WIDTH, HEIGHT))

class Car:
    def __init__(self):
        self.speed = 5
        self.x = LANES[1]
        self.y = HEIGHT - 120
        self.lane = 1
    def move(self, direction):
        if direction == "left" and self.lane > 0:
            self.lane -= 1
        elif direction == "right" and self.lane < len(LANES) - 1:
            self.lane += 1
        self.x = LANES[self.lane] - CAR_WIDTH//2
    def draw(self, screen):
        screen.blit(car_img, (self.x, self.y))

class Obs:
    def __init__(self):
        self.speed = 5
        self.y = -100
        self.lane = random.choice(LANES)
        self.x = self.lane - 25
    def draw(self, screen):
        screen.blit(obs_img, (self.x, self.y))
    def move(self):
        self.y += self.speed
    def collapse(self, car):
        car_rect = pg.Rect(car.x, car.y, CAR_WIDTH, CAR_HEIGHT)
        obs_rect = pg.Rect(self.x, self.y, CAR_WIDTH, CAR_HEIGHT)
        return car_rect.colliderect(obs_rect)

class Coin:
    def __init__(self):
        self.speed = 5
        self.lane = random.choice(LANES)
        self.x = self.lane - COIN_R//2
        self.y = -100
    def draw(self, screen):
        screen.blit(coin_img, (self.x, self.y))
    def move(self):
        self.y += self.speed
    def collect(self, car):
        car_rect = pg.Rect(car.x, car.y,CAR_WIDTH, CAR_HEIGHT)
        coin_rect = pg.Rect(self.x, self.y, COIN_R, COIN_R)
        return car_rect.colliderect(coin_rect)

def game():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    car = Car()
    obss = []
    coins = []
    last_obs_lane = []
    score = 0
    coins_collected = 0
    run = True
    pause = False
    clock = pg.time.Clock()
    
    obs_timer = pg.USEREVENT + 1
    pg.time.set_timer(obs_timer, 1000)

    def Text(text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def Pause():
        nonlocal pause
        pause = True
        while pause:
            for e in pg.event.get():
                if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_q):
                    pg.quit()
                elif e.type == pg.KEYDOWN and e.key == pg.K_p:
                    pause = False
                
            screen.blit(bg_img, (0, 0))
            Text("Game paused, press \"p\" to continue", pg.font.SysFont(None, 30), BLACK, screen, WIDTH//4, HEIGHT//4)
            pg.display.update()
            clock.tick(5)

    def game_over():
        nonlocal run, coins_collected, score, coins, obss
        run = False
        screen.blit(bg_img, (0,0))
        Text("Game over, R to restart, q to quit", pg.font.SysFont(None, 30), BLACK, screen, WIDTH//4, HEIGHT//4)
        pg.display.update()
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_q):
                    pg.quit()
                    quit()
                if e.type == pg.KEYDOWN and e.key == pg.K_r:
                    obss = []
                    coins = []
                    score = 0
                    coins_collected = 0
                    run = True
                    return

    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_q):
                run = False
                pg.quit()
                quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    car.move("left")
                if e.key == pg.K_RIGHT:
                    car.move("right")
                if e.key == pg.K_p:
                    Pause()

            if e.type == obs_timer:
                new_obs = Obs()
                attemp = 10
                while last_obs_lane.count(new_obs) >= 2 and attemp > 0:
                    new_obs = Obs()
                    attemp -= 1
                obss.append(new_obs)
                last_obs_lane.append(new_obs)
                if len(last_obs_lane) > 2:
                    last_obs_lane.pop(0)
        
        if len(coins) < 4 and random.randint(1, 50) == 1:
            valid_lanes = [lane for lane in LANES if lane not in [obs.lane for obs in obss]]
            if valid_lanes:
                new_coin = Coin()
                new_coin.lane = random.choice(valid_lanes)
                new_coin.x = new_coin.lane - COIN_R//2
                coins.append(new_coin)

        for obs in obss[:]:
            obs.move()
            if obs.y > HEIGHT:
                obss.remove(obs)
            if obs.collapse(car):
                game_over()
        
        for coin in coins[:]:
            coin.move()
            if coin.y > HEIGHT:
                coins.remove(coin)
            if coin.collect(car):
                coins_collected += 1
                coins.remove(coin)
        screen.blit(bg_img, (0, 0))
        car.draw(screen)
        for obs in obss:
            obs.draw(screen)
        for coin in coins:
            coin.draw(screen)
        myfont = pg.font.SysFont(None, 35)
        Text(f"score:{score}", myfont, BLACK, screen, 10, 10)
        Text(f"coins:{coins_collected}", myfont, BLACK, screen, 10, 50)
        pg.display.update()
        clock.tick(30)
        score += 1
    pg.quit()
game()

