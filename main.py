
from asyncio import shield
from distutils.spawn import spawn
from re import M, S
import pygame
from assets import Player
from assets import Bullet
from assets import Enemy
from assets import Display
from assets import Powerups

import random
import math
import datetime
import time
from time import perf_counter

pygame.init()
t1_start = perf_counter()

clock = pygame.time.Clock()

counter = 0

# Backgound Image
background = pygame.image.load("images/space-background.jpg")

playerimg = pygame.image.load("images/spaceship.png")

bulletimg = pygame.image.load("images/bullet.png")

enemyimg = pygame.image.load("images/enemy.png")

enemyimg = pygame.transform.scale(enemyimg, (50,50))

enemy_spaceship_img = pygame.image.load("images/enemy-spaceship.png")
enemy_spaceship_img = pygame.transform.scale(enemy_spaceship_img, (50,50))

fast_powerup_img = pygame.image.load("images/flash.png")

fast_powerup_img = pygame.transform.scale(fast_powerup_img, (50,50))

heart_powerup_img = pygame.image.load("images/heart.png")

heart_powerup_img = pygame.transform.scale(heart_powerup_img, (50,50))

shield_img = pygame.image.load("images/shield.png")
shield_img = pygame.transform.scale(shield_img, (50,50))


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

def spawn_enemies():

    # Enemy
    for i in range(int(num_of_enemies/2)):

        # don't have the enemies near each other
        enemy_obj_list.append(Enemy(screen, enemyimg, random.randint(0,735), random.randint(50,150), False))

    for i in range(int(num_of_enemies/2)):
        enemy_obj_list.append(Enemy(screen, enemy_spaceship_img, random.randint(0,735), random.randint(50,150), True))

spawn_enemies()
spawn_count = 0

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

# Powerups

powerup = Powerups(screen, fast_powerup_img, heart_powerup_img, shield_img)

powerup.define_powerups()

miliseconds = pygame.time.get_ticks()
start_seconds = pygame.time.get_ticks()

trigger = pygame.USEREVENT + 0
pygame.time.set_timer(trigger, 1000)

miliseconds = pygame.time.get_ticks() - start_seconds
timer = str(datetime.timedelta(seconds=(round(miliseconds/1000))))[3:]

while running:

    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == trigger:
            miliseconds = pygame.time.get_ticks() - start_seconds
            timer = str(datetime.timedelta(seconds=(round(miliseconds/1000))))[3:]
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
            if event.key == pygame.K_SPACE and bullet.ammo > 0:
                bullet.bulletX = playerX
                bullet.bulletY = playerY
                bullet.fire_bullet(screen,  playerX, playerY, bulletimg)
                bullet.fired = True
            if event.key == pygame.K_r:
                # Reload bullets
                bullet.ammo = 200
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
                # if display.score_value <= grand_num_of_enemies-1:
                display.score_value += 1
                enemy_obj_list[count].alive = False

        enemy_obj_list[count].draw()
        enemy_obj_list[count].movement()
        enemy_obj_list[count].enemy_bullet_movement()

        if enemy_obj_list[count].damage(playerX, playerY):
            display.hit = True

        if enemy_obj_list[count].alive == False:
            enemy_obj_list.pop(count)
            num_of_enemies -= 1
            count = 0
        else:
            count += 1

       
    count = 0

    if not enemy_obj_list:

        # Get the coordinates
        powerup.respawn_powerups()

        # Revert back to default
        if powerup.fast_powerup == False:
            # powerup.fast_powerup = True
            player.player_x_change = 1
            player.player_y_change = 1
        if powerup.shield_powerup == False:
            # powerup.shield_powerup = True
            display.shield = False
            player.shield = False

        powerup.define_powerups()

        if grand_num_of_enemies < 16:
            grand_num_of_enemies += 2
            num_of_enemies = grand_num_of_enemies
            spawn_enemies()
        if grand_num_of_enemies >= 16:
            powerup.fast_powerup = False
            powerup.heart_powerup = False
            powerup.shield_powerup = False
            display.game_over_text()

    if display.total_health <= 0:

        display.game_over_text()

    if powerup.fast_powerup:

        powerup.fast_powerup_movement()

        # Powerup collision
        if powerup.get_powerup(playerX, playerY, "fast"):

            player.player_x_change = 4
            player.player_y_change = 4
            powerup.fast_powerup = False

    if powerup.heart_powerup:

        powerup.heart_powerup_movement()

        if powerup.get_powerup(playerX, playerY,"heart"):
            display.total_health = 200
            powerup.heart_powerup = False

    if powerup.shield_powerup:

        powerup.shield_powerup_movement()

        if powerup.get_powerup(playerX, playerY, "sheild"):
            
            powerup.shield_powerup = False

            # Sheild is on, so don't deduct health
            display.shield = True
            player.shield = True


    display.show_score()
    display.health_bar_status()
    display.ammo_bar_starus(bullet.ammo)
    display.show_timer(timer)
    pygame.display.update()


# when an enemy becomes a frenemy it crosses the path of other enemies and kills them