import pygame
import random
import sys
import time
from Button_class import Button

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")
clock = pygame.time.Clock()
screen.fill("Grey")

# Bar settings
num_bars = 100
bar_width = WIDTH // num_bars
values = [random.randint(10, HEIGHT - 20) for _ in range(num_bars)]
colors = [(0, 0, 255)] * num_bars  # default blue

def draw_bars(values, colors):
    for i, val in enumerate(values):
        x = i * bar_width
        y = HEIGHT - val
        pygame.draw.rect(screen, colors[i], (x, y, bar_width - 1, val))
    pygame.display.update()

def bubble_sort(values):
    n = len(values)
    for i in range(n):
        for j in range(n - i - 1):
            colors[j], colors[j+1] = (255, 0, 0), (255, 0, 0)  # highlight compared bars
            yield
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
            colors[j], colors[j+1] = (0, 0, 255), (0, 0, 255)  # reset color

# Adding buttons
reset_button = Button("Reset", 650, 50, 100, 50, "White", (100, 100, 100), "Black")
sort_button = Button("Sort", 650, 120, 100, 50, "Green", (100, 255, 100), "White")

# Generator to step through sorting
sort_generator = bubble_sort(values)

running = True
while running:
    clock.tick(60)
    draw_bars(values, colors)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif sort_button.is_clicked(event):
            try:
                next(sort_generator)
            except StopIteration:
                pass  # Sorting is done
    sort_button.draw(screen)
    reset_button.draw(screen)

pygame.quit()
sys.exit()
