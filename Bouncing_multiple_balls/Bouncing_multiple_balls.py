from turtle import color
import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT= 800,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing balls")
screen.fill('Grey')

clock = pygame.time.Clock()
circles_list= []

r,g,b= random.randint(0,255), random.randint(0,255), random.randint(0,255)
size= random.randint(50,100)


x_velocity=15
y_velocity =10 
x,y= None,None

circ_dict= { "r_value":r, "g_value":g, "b_value":b}

#While loop for window

running= True
circle=False
while running:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
                 pos= pygame.mouse.get_pos()
                 x,y= pos
      if circle:
            pygame.draw.circle(screen, (r,g,b), (400,300), size)
           
                  
                  
      
      #set the framerate
      clock.tick(60)
      pygame.display.update()
