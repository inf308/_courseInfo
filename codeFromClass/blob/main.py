import pygame
import random
from blob import *

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
START_POPULATION = 10
MAX_POPULATION = 256

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

def drawEnvironment(blobList):
    game_display.fill(WHITE)
    for blob in blobList:
        blob.draw()
    pygame.display.update()

def move(blobList):
    for blob in blobList:
        blob.move()

def reproduce(blobList):
    children = []
    for blob in blobList:
        child = blob.mate(blobList)
        if child:
            children.append(child)
    blobList += children
    

def update(blobList):
    drawEnvironment(blobList)
    move(blobList)
    reproduce(blobList)

    while len(blobList) > MAX_POPULATION:
        print("kill: ", blobList.pop(random.randrange(1, len(blobList))))


    
def main():
    blobs = []
    for i in range(START_POPULATION):
        blobs.append(Blob(game_display))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        update(blobs)
        clock.tick(60)

if __name__ == '__main__':
    main()
