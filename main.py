
from re import S
import pygame
from assets import Player
from assets import Bullet
from assets import Enemy
from assets import Display
import random
import math

pygame.init()

# Backgound Image
background = pygame.image.load("images/space-background.jpg")

playerimg = pygame.image.load("images/spaceship.png")

bulletimg = pygame.image.load("images/bullet.png")

enemyimg = pygame.image.load("images/enemy.png")
enemyimg = pygame.transform.scale(enemyimg, (50,50))

screen = pygame.display.set_mode((800,600))

running = True

start_x = screen.get_rect().center[0]
start_y =  screen.get_rect().center[1] + 200

# Player
player = Player(start_x, start_y, playerimg)


enemy_start_x = 0
enemy_start_y = 20

# for another group of enemies, make another group of 6
num_of_enemies = 6
grand_num_of_enemies = num_of_enemies
enemy_obj_list = []

# Enemy
for i in range(num_of_enemies):

    # don't have the enemies near each other
    enemy_obj_list.append(Enemy(screen, enemyimg, random.randint(0,735), random.randint(50,150)))

playerX = start_x
playerY = start_y

global player_x_change
player_x_change = 0

global player_y_change
player_y_change = 0

# Bullet
bullet = Bullet()
bullet.bulletY = start_y
bullet.bulletX = start_x 

# Display

display = Display(screen)
count = 0
while running:

    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change = player.player_x_change
            if event.key == pygame.K_LEFT:
                player_x_change = -(player.player_x_change)
            if event.key == pygame.K_UP:
                player_y_change = -(player.player_y_change)
            if event.key == pygame.K_DOWN:
                player_y_change = player.player_y_change
            if event.key == pygame.K_SPACE:
                bullet.bulletX = playerX
                bullet.bulletY = playerY
                bullet.fire_bullet(screen,  playerX, playerY, bulletimg)
                bullet.fired = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_x_change = 0
                player_y_change = 0

    if bullet.bulletY <= 0:
        bullet.bulletX = playerX
        bullet.bulletY = playerY
        bullet.bullet_state = False

    if bullet.bullet_state:
        bullet.fire_bullet(screen, playerX, bullet.bulletY, bulletimg)
        bullet.bulletY -= bullet.bullet_y_change

    playerY += player_y_change
    playerX += player_x_change

    player.draw(screen, playerX, playerY)

    while count < num_of_enemies:

        enemyY = enemy_obj_list[count].enemyY
        enemyX = enemy_obj_list[count].enemyX

        if bullet.fired:
            collision = bullet.collision(enemyX, enemyY, bullet.bulletX, bullet.bulletY)

            if collision:
                bullet.fired = False
                collision = False
                if display.score_value <= grand_num_of_enemies-1:
                    display.score_value += 1
                enemy_obj_list[count].alive = False

        enemy_obj_list[count].draw()
        enemy_obj_list[count].movement()

        if enemy_obj_list[count].alive == False:
            enemy_obj_list.pop(count)
            num_of_enemies -= 1
            count = 0
        else:
            count += 1
       
    count = 0


    display.show_score()
    pygame.display.update()