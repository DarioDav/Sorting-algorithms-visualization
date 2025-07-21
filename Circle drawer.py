import pygame
import sys
import random

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Shapes")

clock = pygame.time.Clock()

# Store all circle positions
circle_positions = []



running = True
while running:
    screen.fill((200, 200, 200))  # Refresh background every frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            circle_positions.append(pos) 
            print(pos)
             # Save position of circle
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    circle_positions= []

    # Draw all saved circles
    for pos in circle_positions:
        
        pygame.draw.circle(screen, (100,250,200), pos, 50)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
