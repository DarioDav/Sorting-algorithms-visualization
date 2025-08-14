import pygame
import sys
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Bar data
NUM_BARS = 60
data = []

def generate_data():
    return [random.randint(10, HEIGHT - 60) for _ in range(NUM_BARS)]

data = generate_data()

def draw_bars(data, highlight_indices=None):
    screen.fill(WHITE)
    bar_width = WIDTH // len(data)

    for i, height in enumerate(data):
        x = i * bar_width
        y = HEIGHT - height
        color = RED if highlight_indices and i in highlight_indices else BLUE
        pygame.draw.rect(screen, color, (x, y, bar_width - 2, height))

    draw_button()  # Redraw button on top
    pygame.display.update()

# Button
BUTTON_RECT = pygame.Rect(WIDTH - 120, 10, 100, 30)

def draw_button():
    pygame.draw.rect(screen, GRAY, BUTTON_RECT)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Reset", True, BLACK)
    screen.blit(text, (BUTTON_RECT.x + 20, BUTTON_RECT.y + 5))

# Bubble sort animation (generator)
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_bars(data, highlight_indices=[j, j + 1])
                yield True  # Pause after each swap
                

# Main loop
sorting = False
sort_generator = None
running = True

while running:
    if sorting:
        try:
            next(sort_generator)
            clock.tick(60)
        except StopIteration:
            sorting = False
    else:
        draw_bars(data)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if BUTTON_RECT.collidepoint(event.pos):
                data = generate_data()
                sorting = False
                sort_generator = None

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sorting = True
                sort_generator = bubble_sort(data)

pygame.quit()
sys.exit()
