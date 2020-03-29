# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 01:08:48 2020

pygame tutorial project part 1 from 101computing.net
"""

#import pygame and random packages
import pygame, random
pygame.init()

#import car class
from car import Car

#define colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

#define screen dimensions
screen_width = 700
screen_height = 500

#define background rect dimensions
rect_width = screen_width//6

#open a new window
size = (screen_width,screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

#list of sprites
all_sprites_list = pygame.sprite.Group()

playerCar = Car(red, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300


#set bool carryOn to run loop until game exits
carryOn = True

#set clock to control how fast screen updates
clock = pygame.time.Clock()

### Main Program Loop ###
while carryOn:
    ### Main Event Loop ###
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user closed game
            carryOn = False
    
    # Game logic
    
    # Drawing code

    #Clear screen to white
    screen.fill(white)
    
    #Draw shapes 
    #pygame.draw.line(screen, green, [0,0], [100, 100], 5)
    #pygame.draw.ellipse(screen, black, [20,20,250,100], 2)
    
    #green rectangles
    pygame.draw.rect(screen, green, [0,0,rect_width, screen_height],0)
    pygame.draw.rect(screen, green, [rect_width*5,0, rect_width, screen_height],0)
    #red rectangles
    for pos in range(1,5):
        pygame.draw.rect(screen, red, [rect_width*pos,0, rect_width, screen_height],2)
    
    
    #update screen
    pygame.display.flip()
    
    #limit to 60 FPS
    clock.tick(60)
    
#Stop game engine when main program loop exits
pygame.quit()