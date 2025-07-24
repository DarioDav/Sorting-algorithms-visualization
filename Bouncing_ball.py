import pygame
import sys

pygame.init()

# Window settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

# Ball settings
x, y = 100, 100
radius = 30
velocity_x = 5
velocity_y = 3
color = (100,250,200)

running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position
    x += velocity_x
    y += velocity_y

    # Bounce off walls
    if x - radius <= 0 or x + radius >= width:
        velocity_x *= -1
    if y - radius <= 0 or y + radius >= height:
        velocity_y *= -1

    # Clear screen and redraw
    screen.fill((200, 200, 200))
    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.update()

pygame.quit()
sys.exit()
