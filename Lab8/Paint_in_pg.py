import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLACK

# Brush settings
brush_size = 5
tool = "brush"  # Default tool

# Fill the screen with white
screen.fill(WHITE)

# Main loop
running = True
start_pos = None  # For rectangle and circle drawing
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_c:
                screen.fill(WHITE)
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_o:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if tool in ["rectangle", "circle"]:
                    start_pos = event.pos
                elif tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, brush_size)
                elif tool == "brush":
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos and tool in ["rectangle", "circle"]:
                end_pos = event.pos
                if tool == "rectangle":
                    rect = pygame.Rect(*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, current_color, rect, width=brush_size)
                elif tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, start_pos, radius, width=brush_size)
                start_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button held down
                if tool == "brush":
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)
                elif tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, brush_size)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()