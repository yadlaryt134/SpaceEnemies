
import pygame
import random 

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
        self.bulletX = 0

    
    def fire_bullet(self, screen, x, y, bulletimg):

        self.bullet_state = True

        screen.blit(bulletimg, (x+10,y+10))

class Enemy:

    def __init__(self, screen, enemyimg, x, y):

        self.image = enemyimg
        self.enemy_x_change = 0.22
        self.enemy_y_change = 40
        self.enemyX = x
        self.enemyY = y
        self.screen = screen

    def draw(self):
    
        self.screen.blit(self.image, (self.enemyX, self.enemyY))

    def movement(self):

        self.enemyX += self.enemy_x_change

        if self.enemyX <= 0:
            self.enemy_x_change = abs(self.enemy_x_change)
            self.enemyY += self.enemy_y_change
        elif self.enemyX >= 736:
            self.enemy_x_change = -abs(self.enemy_x_change)
            self.enemyY += self.enemy_y_change 
        
        




