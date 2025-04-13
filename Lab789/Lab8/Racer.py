import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
LANES = [216, 337, 464, 594]  # Полосы движения

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Загрузка изображений
car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (50, 100))
obs_img = pygame.image.load("car2.png")
obs_img = pygame.transform.scale(obs_img, (50, 100))
coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))
bg_img = pygame.image.load("Street.png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

# Класс машины
class Car:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 120
        self.speed = 5
        self.lane = 1  # 1 - вторая полоса

    def move(self, direction):
        if direction == "left" and self.lane > 0:
            self.lane -= 1
        elif direction == "right" and self.lane < len(LANES) - 1:
            self.lane += 1
        self.x = LANES[self.lane] - 25

    def draw(self, screen):
        screen.blit(car_img, (self.x, self.y))

# Класс препятствий
class Obstacle:
    def __init__(self):
        self.lane = random.choice(LANES)
        self.x = self.lane - 25
        self.y = -100
        self.speed = 5

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(obs_img, (self.x, self.y))

    def collision(self, car):
        car_rect = pygame.Rect(car.x, car.y, 50, 100)
        obs_rect = pygame.Rect(self.x, self.y, 50, 100)
        return car_rect.colliderect(obs_rect)

# Класс монет
class Coin:
    def __init__(self):
        self.lane = random.choice(LANES)
        self.x = self.lane - 15
        self.y = -50
        self.speed = 5

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(coin_img, (self.x, self.y))

    def collected(self, car):
        car_rect = pygame.Rect(car.x, car.y, 50, 100)
        coin_rect = pygame.Rect(self.x, self.y, 30, 30)
        return car_rect.colliderect(coin_rect)

# Основная игра
def game_loop():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    car = Car()
    obstacles = []
    coins = []
    running = True
    paused = False
    score = 0
    coins_collected = 0
    last_obstacle_lanes = []

    # Timer for spawning obstacles
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1000)

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def pause_game():
        nonlocal paused
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
            screen.blit(bg_img, (0, 0))
            draw_text('Paused. Press P to continue', pygame.font.SysFont(None, 35), BLACK, screen, WIDTH // 4, HEIGHT // 3)
            pygame.display.update()
            clock.tick(5)

    def game_over():
        nonlocal running
        screen.blit(bg_img, (0, 0))
        draw_text('Game Over', pygame.font.SysFont(None, 75), RED, screen, WIDTH // 3, HEIGHT // 3)
        draw_text('Press R to Restart or Q to Quit', pygame.font.SysFont(None, 35), BLACK, screen, WIDTH // 4, HEIGHT // 2)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:     
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_r:
                        running = True
                        game_loop()
                        return

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car.move("left")
                if event.key == pygame.K_RIGHT:
                    car.move("right")
                if event.key == pygame.K_p:
                    pause_game()
            if event.type == obstacle_timer:
                if len(obstacles) < 5:
                    new_obs = Obstacle()
                    lanes_with_coins = [coin.lane for coin in coins]
                    while new_obs.lane in lanes_with_coins or last_obstacle_lanes.count(new_obs.lane) >= 2:
                        new_obs = Obstacle()
                    obstacles.append(new_obs)
                    last_obstacle_lanes.append(new_obs.lane)
                    if len(last_obstacle_lanes) > 2:
                        last_obstacle_lanes.pop(0)

        # Добавляем монеты
        if len(coins) < 4 and random.randint(1, 50) == 1:
            new_coin = Coin()
            lanes_with_obstacles = [obs.lane for obs in obstacles]
            while new_coin.lane in lanes_with_obstacles:
                new_coin = Coin()
            coins.append(new_coin)

        # Движение препятствий и монет
        for obs in obstacles[:]:
            obs.move()
            if obs.y > HEIGHT:
                obstacles.remove(obs)
            if obs.collision(car):
                game_over()  # Столкновение с препятствием

        for coin in coins[:]:
            coin.move()
            if coin.y > HEIGHT:
                coins.remove(coin)
            if coin.collected(car):
                coins_collected += 1
                coins.remove(coin)

        # Отрисовка
        screen.blit(bg_img, (0, 0))
        car.draw(screen)
        for obs in obstacles:
            obs.draw(screen)
        for coin in coins:
            coin.draw(screen)

        # Отображение счета
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, BLACK)
        coins_text = font.render(f"Coins: {coins_collected}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(coins_text, (10, 50))

        pygame.display.flip()
        clock.tick(30)
        score += 1

    pygame.quit()

game_loop()