
import pygame
from assets import Player
from assets import Bullet
from assets import Enemy

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

# Enemy
enemy = Enemy(enemyimg, enemy_start_x, enemy_start_y)

playerX = start_x
playerY = start_y

global player_x_change
player_x_change = 0

global player_y_change
player_y_change = 0

# Bullet
bullet = Bullet()
bullet.bulletY = start_x

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
                bullet.fire_bullet(screen, playerX, bullet.bulletY, bulletimg)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_x_change = 0
                player_y_change = 0

    if bullet.bulletY <= 0:
        bullet.bulletY = start_x
        bullet.bullet_state = False

    if bullet.bullet_state:
        bullet.fire_bullet(screen, playerX, bullet.bulletY, bulletimg)
        bullet.bulletY -= bullet.bullet_y_change

    playerY += player_y_change
    playerX += player_x_change

    player.draw(screen, playerX, playerY)
    enemy.draw(screen, enemy_start_x, enemy_start_y)

    pygame.display.update()