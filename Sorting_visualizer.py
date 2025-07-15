import pygame
import sys
import random

pygame.init()

HEIGHT=500
WIDTH= 800

#setting up the display screen
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorter visualizer")
screen.fill("Grey")

#creating the clock to set FPS
clock=pygame.time.Clock()

def get_random_data(n=50):
      return [random.randint(10,HEIGHT-10) for _ in range(n)]

def draw_bars(surface, data):
      bar_width= WIDTH//len(data)

      for i, value in enumerate(data):
            x= i*bar_width
            y=HEIGHT-value
            # pygame.draw.rect(surface, color, (x, y, width, height))
            pygame.draw.rect(surface, "Blue", (x,y, bar_width-2, value))




data=get_random_data()

while True:
      draw_bars(screen, data)


      for event in pygame.event.get():      
            #terminating the loop if the user press escape
            if event.type== pygame.QUIT:
                  pygame.quit()
                  exit()

      pygame.display.update()
      clock.tick(60)