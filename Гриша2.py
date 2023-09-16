import pygame
import sys

pygame.init()

flLeft = False
flRight = False
xp = 300
yp = 450
speed = 1

screen = pygame.display.set_mode((700, 500))

r = pygame.Rect(xp, yp, 100, 25)
pygame.draw.rect(screen, (255, 255, 255), r, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flLeft = flRight = False
    if flLeft:
        xp -= speed
        if xp == -100:
            xp = 799
    elif flRight:
        xp += speed
        if xp == 800:
            xp = -99
        
    screen.fill((0, 0 ,0))
        
    r = pygame.Rect(xp, yp, 100, 25)
    pygame.draw.rect(screen, (255, 255, 255), r, 0)
    
    pygame.display.flip()
    
 
