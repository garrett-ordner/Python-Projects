# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 01:08:48 2020

pygame tutorial project part 1 from 101computing.net
https://www.101computing.net/pygame-how-to-control-your-sprite/
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
grey = (210,210,210)
purple = (255,0,255)

#define screen dimensions
screen_width = 700
screen_height = 500

#define background rect dimensions
rect_width = screen_width//6

#open a new window
size = (screen_width,screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

#list of sprites
all_sprites_list = pygame.sprite.Group()

playerCar = Car(red, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

# Add car to list of objects
all_sprites_list.add(playerCar)

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
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #pressing x key to quit
                carryOn=False
                
    #movement handlers
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    
    # Game logic
    all_sprites_list.update()
    
    #Clear screen to green
    screen.fill(green)
    
    #Draw The Road
    pygame.draw.rect(screen, grey, [40,0, 200,300])
    
    #Draw Line painting on the road
    pygame.draw.line(screen, white, [140,0],[140,300],5)

    #draw sprites
    all_sprites_list.draw(screen)
    
    #update screen
    pygame.display.flip()
    
    #limit to 60 FPS
    clock.tick(60)
    
#Stop game engine when main program loop exits
pygame.quit()