import pygame
import random
from database import init_db, get_or_create_user, save_score

# ==== Настройки ====
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS_BY_LEVEL = [10, 15, 20]
LEVEL_WALLS = {
    1: [],
    2: [(x, 10) for x in range(5, 25)] + [(x, 15) for x in range(10, 30)],
    3: [(15, y) for y in range(5, 20)] + [(25, y) for y in range(10, 25)],
}

# ==== Инициализация базы ====
init_db()

# ==== Ввод пользователя ====
username = input("Enter your username: ")
user_id = get_or_create_user(username)

# ==== Pygame ====
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# ==== Игровые функции ====
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*block, CELL_SIZE, CELL_SIZE))

def draw_food(pos):
    pygame.draw.rect(screen, (255, 0, 0), (*pos, CELL_SIZE, CELL_SIZE))

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, (150, 150, 150), (*wall, CELL_SIZE, CELL_SIZE))

def random_food(snake, walls):
    while True:
        x = random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE
        y = random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)

# ==== Начальные параметры ====
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = random_food(snake, [])
score = 0
level = 1
walls = [(x * CELL_SIZE, y * CELL_SIZE) for x, y in LEVEL_WALLS[level]]
pause = False
running = True

# ==== Игровой цикл ====
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE): direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE): direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0): direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0): direction = (CELL_SIZE, 0)
            elif event.key == pygame.K_p:
                pause = not pause
            elif event.key == pygame.K_s:
                save_score(user_id, level, score)
                print("Game saved!")

    if not pause:
        # движение змейки
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (
            new_head in snake or
            new_head in walls or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT
        ):
            print("Game Over!")
            save_score(user_id, level, score)
            break

        snake = [new_head] + snake[:-1]

        if new_head == food:
            snake.append(snake[-1])
            score += 1
            food = random_food(snake, walls)

            if score in [5, 10] and level < 3:
                level += 1
                walls = [(x * CELL_SIZE, y * CELL_SIZE) for x, y in LEVEL_WALLS[level]]

    # отрисовка
    draw_snake(snake)
    draw_food(food)
    draw_walls(walls)

    text = font.render(f"User: {username}  Score: {score}  Level: {level}  (P=Pause, S=Save)", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS_BY_LEVEL[level - 1])

pygame.quit()
