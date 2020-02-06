#!../env/bin/python3

import sys, pygame, random
pygame.init()

class Ball():
  def __init__(self, speed, win):
    self.speed = speed
    self.win = win
    self.img = pygame.image.load("intro_ball.gif")
    self.rect = self.img.get_rect()

  def onMouseClick(self, x, y):
    if self.rect.collidepoint(x, y):
      self.speed = [random.randint(0,5), random.randint(0,5)]

  def move(self):
    self.rect = self.rect.move(self.speed)
    if self.rect.left < 0 or self.rect.right > self.win.get_width():
      self.speed[0] = -self.speed[0]
    if self.rect.top < 0 or self.rect.bottom > self.win.get_height():
      self.speed[1] = -self.speed[1]


size = width, height = 1080, 760
speed = [4, 4]
speed2 = [3, 3]
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

screen = pygame.display.set_mode(size)


ball1 = Ball([2, 2], screen)
ball2 = Ball([3, 3], screen)


while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
      ## if mouse is pressed get position of cursor ##
      x, y = event.pos
      print(x, y, end=" ")
      ## check if cursor is on button ##
      ball1.onMouseClick(self, x, y)
      ball2.onMouseClick(self, x, y)

  ball1.move()
  ball2.move()
  
    
'''
    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(ball2, ball2rect)
    pygame.display.flip()
'''