#!../env/bin/python3

import sys, pygame, random
pygame.init()

size = width, height = 1080, 760
speed = [4, 4]
speed2 = [3, 3]
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

ball2 = pygame.image.load("intro_ball.gif")
ball2rect = ball2.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.mouse.get_pressed():
            ## if mouse is pressed get position of cursor ##
            pos = pygame.mouse.get_pos()
            print(pos, end=" ")
            ## check if cursor is on button ##
            if ballrect.collidepoint(pos):
                print("ball")
                speed = [random.randint(0,5), random.randint(0,5)]
            if ball2rect.collidepoint(pos):
                print("ball2")
                speed2 = [random.randint(0,5), random.randint(0,5)]


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    ball2rect = ball2rect.move(speed2)
    if ball2rect.left < 0 or ball2rect.right > width:
        speed2[0] = -speed2[0]
    if ball2rect.top < 0 or ball2rect.bottom > height:
        speed2[1] = -speed2[1]

    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(ball2, ball2rect)
    pygame.display.flip()
