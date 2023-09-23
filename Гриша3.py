import pygame
import sys

pygame.init()

flLeft = False
flRight = False
xp = 300
yp = 450

fps = 100

dx = -1
dy = -1

Clock = pygame.time.Clock()

speed = 10
speedball = 5

def detect_collision (dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
        
    if dy > 0:
        delta_y = ball.bottom - ball.top
    else:
        delta_y = rect.bottom - ball.top
    
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

screen = pygame.display.set_mode((700, 500))

# Ball
ball_hitbox = pygame.Rect(700 // 2 , 500 // 2, 50, 50)
    
ball = 25
    
# Player
plr = pygame.Rect(xp, yp, 100, 25)
pygame.draw.rect(screen, (255, 255, 255), plr, 0)

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
        if xp < -100:
            xp = 799
    elif flRight:
        xp += speed
        if xp > 800:
            xp = -99
            
    screen.fill((0, 0 ,0))
    
    if ball_hitbox.centerx < ball or ball_hitbox.centerx > 700 - ball:
        dx = -dx
    if ball_hitbox.centery < ball or ball_hitbox.centery > 500 - ball:
        dy = -dy
        
    if ball_hitbox.colliderect(plr) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball_hitbox, plr)
    
    # Player
    plr = pygame.Rect(xp, yp, 100, 25)
    pygame.draw.rect(screen, (255, 255, 255), plr, 0)
    
    ball_hitbox.x += speedball * dx
    ball_hitbox.y += speedball * dy
    
    # Ball    
    ball = 25
    pygame.draw.circle(screen, (255, 255, 255), ball_hitbox.center, ball)
    
    Clock.tick(fps)
    pygame.display.flip()
    
 