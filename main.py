
import pygame
from assets import Player

pygame.init()

# Backgound Image
background = pygame.image.load("images/space-background.jpg")

playerimg = pygame.image.load("images/spaceship.png")

screen = pygame.display.set_mode((800,600))

running = True

# Player
active_sprites_list = pygame.sprite.Group()

player = Player(screen.get_rect().center[0], screen.get_rect().center[1] + 200, playerimg)

all_sprites = pygame.sprite.Group([player])


while running:


    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    all_sprites.update(screen)

    all_sprites.draw(screen)

    pygame.display.update()