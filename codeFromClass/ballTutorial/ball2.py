import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    #events = pygame.event.get()
    #for event in events:
    xMove = 0
    yMove = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xMove = -10
            if event.key == pygame.K_RIGHT:
                xMove = 10
            if event.key == pygame.K_UP:
                yMove = -10
            if event.key == pygame.K_DOWN:
                yMove = 10
    ballrect = ballrect.move((xMove, yMove))
    
    if ballrect.left < 0:
        ballrect = ballrect.move((width, 0))
    elif ballrect.right > width:
        ballrect = ballrect.move((-width, 0))
    if ballrect.top < 0:
        ballrect = ballrect.move((0, height))
    elif ballrect.bottom > height:
        ballrect = ballrect.move((0, -height))
        

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()