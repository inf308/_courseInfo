import pygame
import random

class Blob:
    
    def __init__(self, win, coords=None, size=None, speed=None, color=None):
        self.WIDTH = win.get_width()
        self.HEIGHT = win.get_height()
        self.MUT_PROB = 0.05
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


    def mutateGene(self, gene, mutAmount, min, max):
        if random.random() < self.MUT_PROB:
            self.chromosome[gene] += random.random()*mutAmount*2 - mutAmount
            if self.chromosome[gene] < min: self.chromosome[gene] = min
            if self.chromosome[gene] > max: self.chromosome[gene] = max

    
    def mutate(self):
        # ["x", "y", "size", "speed", "r", "g", "b"]
        self.mutateGene("x", 10, 0, self.WIDTH)
        self.mutateGene("y", 10, 0, self.HEIGHT)
        self.mutateGene("size", 1, 4, 20)
        self.mutateGene("speed", 1, 0, 10)
        self.mutateGene("r", 5, 0, 255)
        self.mutateGene("g", 5, 0, 255)
        self.mutateGene("b", 5, 0, 255)
        


    def moveOneDimension(self, d):
        self.chromosome[d] += random.random()*2*self.getSpeed()-self.getSpeed()
        if self.chromosome[d] < 0: 
            self.chromosome[d] = 0
        elif self.chromosome[d] > self.WIDTH: 
            self.chromosome[d] = self.WIDTH


    def move(self):
        self.moveOneDimension("x")
        self.moveOneDimension("y")


    def draw(self):
        self.rect = pygame.draw.circle(self.win, self.getColor(), self.getCoords(), self.getSize())


    def findMate(self, potentialMates):

        #potentialMates.remove(self)
        # TODO: ideally we want to remove self frompotential Mates but
        # using .remove removes it permanently from the population
        # so we need to either use deep copy or remove then immediately
        # put back

        mates = self.rect.collidelistall(potentialMates)
        if len(mates) <= 0:
            return False
        
        mate = random.choice(mates)

        return potentialMates[mate]
    

    def splice(self, mate):
        # randomize parent order
        parent = [self, mate]
        random.shuffle(parent)

        # splice chromosome into child chromosome dictionary
        cc = {}
        for i in self.order[0:self.CROSSOVER]:
            cc[i] = parent[0].chromosome[i]
        for i in self.order[self.CROSSOVER:]:
            cc[i] = parent[1].chromosome[i]

        # create child blob
        child = Blob(self.win, (cc["x"], cc["y"]), cc["size"], cc["speed"], (cc["r"], cc["g"], cc["b"]))

        child.mutate()

        return child


    def mate(self, potentialMates):
        mate = self.findMate(potentialMates)
        if mate:
            child = self.splice(mate)
            # TODO: add mutation here
            return child
        return False