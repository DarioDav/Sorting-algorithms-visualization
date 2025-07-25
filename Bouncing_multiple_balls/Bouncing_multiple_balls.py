from turtle import color
import pygame
import sys
import random
import Ball_class
import Button_class

pygame.init()
#Display settings
WIDTH, HEIGHT= 800,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing balls")
screen.fill('Grey')
clock = pygame.time.Clock()

# Initial ball settings
circles_list= []

#While loop for window
running= True


while running:
      
      
      #stopping the program if you press quit
      for event in pygame.event.get():
            
      
      # Create a new circle only when the left mouse button is pressed down (not held)
            if event.type == pygame.MOUSEBUTTONDOWN :
                  x, y = event.pos
                  size = random.randint(50, 100)
                  color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                  circles_list.append(Ball_class.Circle(x, y, size, color))
            
      screen.fill("Grey")
      for ball in circles_list:
            
            ball.move(WIDTH, HEIGHT)
            pygame.draw.circle(screen, ball.color, (ball.x, ball.y), radius=ball.radius)
            #update position
            
                 
            if event.type == pygame.QUIT:
                  running = False
      #set the framerate
      clock.tick(60)
      pygame.display.update()
