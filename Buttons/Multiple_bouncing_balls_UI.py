import pygame
import sys
import random
import Ball_class
from Button_class import Button


pygame.init()
#Display settings
WIDTH, HEIGHT= 800,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing balls")
screen.fill('Grey')
clock = pygame.time.Clock()

# Initial ball settings
circles_list= []

# Create buttons
button1 = Button("Add 5 balls", 50, 50, 200, 60, "Blue", (100, 180, 255), "White")
button2 = Button("Reset", 50, 130, 200, 60, "White", (100, 100, 100), "Black")


#While loop for window
running= True
while running:
      
      
      #stopping the program if you press quit
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
      
      # Create a new circle only when the left mouse button is pressed down (not held)
            elif button1.is_clicked(event) :
                  for drawing in range(4):
                        x, y = event.pos
                        size = random.randint(50, 100)
                        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        circles_list.append(Ball_class.Circle(x, y, size, color))

            elif button2.is_clicked(event):
                  circles_list.clear()

      screen.fill("Grey")
      for ball in circles_list:
            
            ball.move(WIDTH, HEIGHT)
            pygame.draw.circle(screen, ball.color, (ball.x, ball.y), radius=ball.radius)
            #update position
            
      button1.draw(screen)
      button2.draw(screen)
      
            
      #set the framerate
      clock.tick(60)
      pygame.display.update()
