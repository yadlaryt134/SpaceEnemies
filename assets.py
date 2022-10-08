
import pygame

class Player():

    def __init__(self, start_x, start_y, image):

        self.image = image
        self.rect = self.image.get_rect(center=(start_x, start_y))
        self.player_x_change = 0.3
        self.player_y_change = 0.3

    def draw(self, screen, x, y):

        screen.blit(self.image, (x,y))

class Bullet():

    def __init__(self):

        self.bullet_state = False
        self.bullet_y_change = 8
        self.bulletY = 0
    
    def fire_bullet(self, screen, x, y, bulletimg):

        self.bullet_state = True

        # draw bullet onto the screen

        screen.blit(bulletimg, (x+10,y+10))

class Enemy:

    def __init__(self, enemyimg, x, y):
        self.image = enemyimg
        self.rect = self.image.get_rect(center=(x, y))
        self.enemy_x_change = 0.3
        self.enemy_y_change = 0.3
    

    def draw(self, screen, x, y):
    
        screen.blit(self.image, (x,y))




