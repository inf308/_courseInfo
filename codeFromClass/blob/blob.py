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


    def getColor(self):
        return (int(self.chromosome["r"]), int(self.chromosome["g"]), int(self.chromosome["b"]))


    def getCoords(self):
        return (int(self.chromosome["x"]), int(self.chromosome["y"]))


    def getSize(self):
        return int(self.chromosome["size"])


    def getSpeed(self):
        return self.chromosome["speed"]


    def getX(self):
        return int(self.chromosome["x"])


    def getY(self):
        return int(self.chromsome["y"])


    def move(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.chromosome["x"] += random.random()*2*self.getSpeed()-self.getSpeed()
        self.chromosome["y"] += random.random()*2*self.getSpeed()-self.getSpeed()
        
        if self.chromosome["x"] < 0: self.chromosome["x"] = 0
        elif self.chromosome["x"] > self.WIDTH: self.chromosome["x"] = self.WIDTH
        
        if self.chromosome["y"] < 0: self.chromosome["y"] = 0
        elif self.chromosome["y"] > self.HEIGHT: self.chromosome["y"] = self.HEIGHT
    




    def draw(self):
        self.rect = pygame.draw.circle(self.win, self.getColor(), self.getCoords(), self.getSize())


    def findMate(self, potentialMates):

        #potentialMates.remove(self)

        mates = self.rect.collidelistall(potentialMates)
        if len(mates) <= 0:
            return False
        
        mate = random.choice(mates)

        return potentialMates[mate]
    
    def splice(self, mate):
        '''TODO: create this function. I copied code from simpleGA as 
        reference but it won't work in this context'''
        child = parent1[0:crossover] + parent2[crossover:]
        return child
