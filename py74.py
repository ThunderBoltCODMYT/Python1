import math
import random
import pygame
#Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
PLAYER_START_X, PLAYER_START_Y = 370, 380
ENEMY_SPEED_X, ENEMY_SPEED_Y = 4, 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
#Initialize Pygame
pygame.init()
#Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Background
background = pygame.image.load('background.png.jpeg')
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png.jpeg')
pygame.display.set_icon(icon)
# Player

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
# Player Movement
        playerX +- playerX_change
        playerX = max(0, min(playerX, SCREEN_WIDTH - 64))#the size of the player is 64
#Enemys movement
        for i in range(num_of_enemies):
            if enemyY[i] > 340:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] <= SCREEN_WIDTH - 64:
                enemyX_change[i] *= -1:
                enemyY[i] += enemyY_change[i]#Collision check
            if isCollision(enemyX[i], enemyY[i], ):


