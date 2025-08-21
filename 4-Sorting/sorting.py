import pygame
import sys
import random
from Button_class import Button

pygame.init()
# Display settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sortihng Visualization")
clock = pygame.time.Clock()
screen.fill("Grey")

# Bar settings
num_bars = 100
bar_width = WIDTH // num_bars
values = [random.randint(10, HEIGHT - 20) for _ in range(num_bars)]
colors = [(50, 50, 50)] * num_bars  # default blue

def draw_bars(values, colors):
    for i, val in enumerate(values):
        x = i * bar_width
        y = HEIGHT - val
        pygame.draw.rect(screen, colors[i], (x, y, bar_width - 1, val))
    pygame.display.update()

#adding buttons
reset_button = Button("Reset", 650, 50, 100, 50, "White", (100, 100, 100), "Black")
sort_button = Button("Sort", 650, 120, 100, 50, "Green", (100, 255, 100), "White")
#while loop for window
running = True
while running:
    # Stopping the program if you press quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif reset_button.is_clicked(event):
            print("Reset clicked")
            
        elif sort_button.is_clicked(event):
            print("Sort clicked")

    screen.fill("Grey")
    reset_button.draw(screen)
    sort_button.draw(screen)
    draw_bars(values, colors)


    # Set the framerate
    clock.tick(60)
    pygame.display.update()