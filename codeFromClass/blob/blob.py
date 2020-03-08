import pygame
import random

class Blob:
    
    def __init__(self, win, coords=None, size=None, speed=None, color=None):
        self.WIDTH = win.get_width()
        self.HEIGHT = win.get_height()
        self.order = ["x", "y", "size", "speed", "r", "g", "b"]
        self.CROSSOVER = int(len(self.order)/2)
        self.chromosome = {}

        if coords is None: 
            coords = [0, 0]
            coords[0] = random.randrange(0, self.WIDTH)
            coords[1] = random.randrange(0, self.HEIGHT)
        self.chromosome["x"] = coords[0]
        self.chromosome["y"] = coords[1]

        if size is None:
            size = random.randrange(4,20)
        self.chromosome["size"] = size

        if speed is None:
            speed = random.randrange(0,10)
        self.chromosome["speed"] = speed

        if color is None:
            color = [0, 0, 0]
            color[0] = random.randint(0, 255)
            color[1] = random.randint(0, 255)
            color[2] = random.randint(0, 255)
        self.chromosome["r"] = color[0]
        self.chromosome["g"] = color[1]
        self.chromosome["b"] = color[2]

        self.win = win
        self.rect = None

    def move(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y
        
        if self.x < 0: self.x = 0
        elif self.x > self.WIDTH: self.x = self.WIDTH
        
        if self.y < 0: self.y = 0
        elif self.y > self.HEIGHT: self.y = self.HEIGHT
    


    def draw(self):
        self.rect = pygame.draw.circle(self.win, self.color, [self.x, self.y], self.size)

    def findMate(self, potentialMates):
        mates = self.rect.collidelistall(potentialMates)
        if mates < 0:
            return False
        
        mate = random.choice(mates)
        return potentialMates[mate]
    
    def splice(self, mate):
        '''TODO: create this function. I copied code from simpleGA as 
        reference but it won't work in this context'''
        child = parent1[0:crossover] + parent2[crossover:]
        return child
