# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 01:48:33 2020

pygame tutorial project part 2 from 101computing.net
car class
"""
import pygame

#define color
white = (255,255,255)

#class car
class Car(pygame.sprite.Sprite):
    #derive class from Sprite class in Pygame
    
    def __init__(self, color, width, height):
        #call parent class (Sprite) constructor
        super().__init__()
        
        #pass in the car arguments
        #set background color and set transparency
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        
        #draw rectangle for car
        pygame.draw.rect(self.image, color, [0,0, width, height])
        
        #placeholder for actual sprite
        #self.image = pygame.image.load("car.png).convert_alpha()
        
        #fetch rectangle object with dimensions of image
        self.rect = self.image.get_rect()
    
    #define movement procedures
    def moveRight(self, pixels):
        self.rect.x += pixels
        
    def moveLeft(self, pixels):
        self.rect.x -=pixels