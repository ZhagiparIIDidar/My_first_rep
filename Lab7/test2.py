import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1100, 750), pygame.RESIZABLE)
pygame.display.set_caption("Pygame Window")

# Load the background image
background_image = pygame.image.load('mickeyclock_cleanup.png').convert()
background_rect = background_image.get_rect()

# Load the overlay image (hour hand)
overlay_image = pygame.image.load('hour_mickeyclock.png').convert_alpha()

# Load the minute hand image
minute_image = pygame.image.load('min_mickeyclock.png').convert_alpha()
minute_image.set_alpha(255)  # Ensure the minute hand is fully opaque and drawn on top

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Resize the screen and scale the background
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background_image = pygame.transform.scale(
                pygame.image.load('mickeyclock_cleanup.png').convert(), (event.w, event.h)
            )
            background_rect = background_image.get_rect()

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Calculate the position to center the overlay image
    center_x, center_y = background_rect.center

    # Get the current time
    current_time = pygame.time.get_ticks() // 1000
    hours = (current_time // 60) % 12
    minutes = (current_time // 1) % 60

    # Rotate the hour hand image
    hour_angle = -30 * hours  # Each hour is 30 degrees
    rotated_hour_image = pygame.transform.rotate(overlay_image, hour_angle)
    rotated_hour_rect = rotated_hour_image.get_rect(center=(center_x, center_y))

    # Rotate the minute hand image
    minute_angle = -6 * minutes  # Each minute is 6 degrees
    rotated_minute_image = pygame.transform.rotate(minute_image, minute_angle)
    rotated_minute_rect = rotated_minute_image.get_rect(center=(center_x, center_y))

    # Draw the rotated hour and minute hand images
    screen.blit(rotated_hour_image, rotated_hour_rect.topleft)
    screen.blit(rotated_minute_image, rotated_minute_rect.topleft)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()