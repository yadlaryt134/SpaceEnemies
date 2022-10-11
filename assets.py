
import pygame
import random 
import math

class Player():

    def __init__(self, start_x, start_y, image):

        self.image = image
        self.rect = self.image.get_rect(center=(start_x, start_y))
        self.player_x_change = 1
        self.player_y_change = 1

    def draw(self, screen, x, y):

        screen.blit(self.image, (x,y))

class Bullet():

    def __init__(self):

        self.bullet_state = False
        self.bullet_y_change = 8
        self.bulletY = 0
        self.bulletX = 0
        self.fired = True

    
    def fire_bullet(self, screen, x, y, bulletimg):

        self.bullet_state = True

        screen.blit(bulletimg, (x+10,y+10))
    
    def collision(self, enemyX, enemyY, bulletX, bulletY):

        distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))

        if distance < 18:
            return True
        else:
            return False


class Enemy:

    def __init__(self, screen, enemyimg, x, y):

        self.image = enemyimg
        self.enemy_x_change = 0.3
        self.enemy_y_change = 40
        self.enemyX = x
        self.enemyY = y
        self.screen = screen
        self.alive = True

    def draw(self):

        if self.alive:
            self.screen.blit(self.image, (self.enemyX, self.enemyY))

    def movement(self):

        self.enemyX += self.enemy_x_change

        if self.enemyX <= 0:
            self.enemy_x_change = abs(self.enemy_x_change)
            self.enemyY += self.enemy_y_change
        elif self.enemyX >= 736:
            self.enemy_x_change = -abs(self.enemy_x_change)
            self.enemyY += self.enemy_y_change 

class Display:

    def __init__(self, screen):
        self.score_value = 0
        self.textX = 10
        self.textY = 10
        self.screen = screen

    def show_score(self):

        font = pygame.font.Font('freesansbold.ttf', 32)
        
        score = font.render("Score: " + str(self.score_value), True, (255,255,255))
        self.screen.blit(score, (self.textX,self.textY))

    def game_over_text(self):

        font = pygame.font.Font('freesansbold.ttf', 64)

        game_over = font.render("GAME OVER", True, (255,255,255))
        self.screen.blit(game_over, (200, 270))

# class Powerups:


        
        




