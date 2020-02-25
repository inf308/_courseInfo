import pygame
import random

class Blob:
    
    def __init__(self, color, win):
        self.WIDTH = win.get_width()
        self.HEIGHT = win.get_height()
        self.x = random.randrange(0, self.WIDTH)
        self.y = random.randrange(0, self.HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color
        self.win = win

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
        pygame.draw.circle(self.win, self.color, [self.x, self.y], self.size)
