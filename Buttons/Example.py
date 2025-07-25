import pygame
import sys
import random
import Ball_class

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls with Reset Button")
clock = pygame.time.Clock()

# Ball storage
balls = []

# Define button properties
button_color = (100, 200, 100)
hover_color = (150, 250, 150)
text_color = (0, 0, 0)
button_rect = pygame.Rect(10, 10, 120, 40)
font = pygame.font.SysFont(None, 30)

def draw_button():
    mouse_pos = pygame.mouse.get_pos()
    current_color = hover_color if button_rect.collidepoint(mouse_pos) else button_color
    pygame.draw.rect(screen, current_color, button_rect, border_radius=5)
    
    text = font.render("Reset", True, text_color)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

# Main loop
running = True
while running:
    screen.fill((200, 200, 200))

    # Draw the reset button
    draw_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                balls.clear()  # Reset all balls
            else:
                # Spawn a new ball
                x, y = event.pos
                size = random.randint(30, 60)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                balls.append(Ball_class.Circle(x, y, size, color))

    # Update and draw balls
    for ball in balls:
        ball.move(WIDTH, HEIGHT)
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), radius=ball.radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
