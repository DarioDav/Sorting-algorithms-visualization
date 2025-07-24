import pygame
import sys

pygame.init()
# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Shapes")

clock= pygame.time.Clock()


running= True
while running:
      screen.fill((200, 200, 200))

      for event in pygame.event.get():
            if event.type == pygame.QUIT:
            running = False