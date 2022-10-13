
import pygame
import random 
import math

class Player():

    def __init__(self, start_x, start_y, image):

        self.image = image
        self.rect = self.image.get_rect(center=(start_x, start_y))
        self.player_x_change = 1
        self.player_y_change = 1
        self.shield = False

    def draw(self, screen, x, y):

        screen.blit(self.image, (x,y))

        if self.shield == True:
            pygame.draw.circle(screen, (255,255,255), (x+25,y+25), 50, width=5) # Here <<<

class Bullet():

    def __init__(self):

        self.bullet_state = False
        self.bullet_y_change = 8
        self.bulletY = 0
        self.bulletX = 0
        self.fired = True
        self.ammo = 200

    
    def fire_bullet(self, screen, x, y, bulletimg):

        self.bullet_state = True
        self.ammo -= 0.1

        screen.blit(bulletimg, (x+10,y+10))
    
    def collision(self, enemyX, enemyY, bulletX, bulletY):

        distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))

        if distance < 18:
            return True
        else:
            return False


class Enemy:

    def __init__(self, screen, enemyimg, x, y, attack):

        self.image = enemyimg
        self.enemy_x_change = 0.3
        self.enemy_y_change = 40
        self.enemyX = x
        self.enemyY = y
        self.screen = screen
        self.alive = True
        self.attacking_enemy = attack
        self.bulletimg = pygame.image.load("images/enemy-bullet.png")
        self.bulletimg = pygame.transform.rotate(self.bulletimg, 180)
        self.bulletimg = pygame.transform.scale(self.bulletimg , (50,50))
        self.enemy_bullet_x = self.enemyX
        self.enemy_bullet_y = self.enemyY
        self.enemy_bullet_y_change = 2

    def draw(self):

        if self.alive:
            self.screen.blit(self.image, (self.enemyX, self.enemyY))
            self.screen.blit(self.image, (self.enemyX, self.enemyY))

    def enemy_bullet_movement(self):

        if self.attacking_enemy:

            self.enemy_bullet_y += self.enemy_bullet_y_change

            self.screen.blit(self.bulletimg, (self.enemy_bullet_x+7 ,  self.enemy_bullet_y+25))

            if self.enemy_bullet_y >= 800:
                self.enemy_bullet_x = self.enemyX
                self.enemy_bullet_y = self.enemyY

    def damage(self, playerX, playerY):

        distance = math.sqrt(math.pow(playerX-self.enemy_bullet_x,2) + (math.pow(playerY-self.enemy_bullet_y,2)))

        if distance < 18:
            return True
        else:
            return False


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
        self.total_health = 200
        self.health_bar_w = 200
        self.health_bar_h = 20
        self.hit = False
        self.shield = False
        self.ammo_bar_w = 200
        self.ammo_bar_h = 20
    
    def show_timer(self, timer):

        font = pygame.font.Font('freesansbold.ttf', 32)

        time = font.render(timer, True, (255,255,255))
        self.screen.blit(time, (self.textX, self.textY+50))

    def show_score(self):

        font = pygame.font.Font('freesansbold.ttf', 32)
        
        score = font.render("Score: " + str(self.score_value), True, (255,255,255))
        self.screen.blit(score, (self.textX,self.textY))

    def game_over_text(self):

        font = pygame.font.Font('freesansbold.ttf', 64)

        game_over = font.render("GAME OVER", True, (255,255,255))
        self.screen.blit(game_over, (200, 270))
    
    def health_bar_status(self):

        if self.hit and self.shield == False:

            if self.total_health <= 200:
                self.total_health -= 1
                self.hit = False
        else:
            pass

        pygame.draw.rect(self.screen,(255,0,0),(5,550, self.total_health, self.health_bar_h))
        pygame.draw.rect(self.screen,(255,255,255),(5, 550, self.health_bar_w, self.health_bar_h),4)

    def ammo_bar_starus(self, total_ammo):

        pygame.draw.rect(self.screen,(255,255,0),(5,510, total_ammo, self.ammo_bar_h))
        pygame.draw.rect(self.screen,(255,255,255),(5, 510, self.ammo_bar_w, self.ammo_bar_h),4)

class Powerups:

    def __init__(self, screen, fast_img, heart_img, shield_img):

        self.screen = screen
        self.fast_img = fast_img
        self.heart_img = heart_img
        self.shield_img = shield_img
        self.fast_player_x =  random.randint(0,735)
        self.fast_player_y = random.randint(50,150)
        self.heart_player_x =  random.randint(0,735)
        self.heart_player_y = random.randint(50,150)
        self.fast_player_y_change = 0.3
        self.shield_player_x =  random.randint(0,735)
        self.shield_player_y = random.randint(50,150)
        self.fast_powerup = False
        self.heart_powerup = False
        self.shield_powerup = False

    
    def respawn_powerups(self):
        self.fast_player_x =  random.randint(0,735)
        self.fast_player_y = random.randint(50,150)
        self.heart_player_x = random.randint(0,735)
        self.heart_player_y = random.randint(50,150)
        self.shield_player_x = random.randint(0,735)
        self.shield_player_y = random.randint(50,150)
        self.fast_powerup = False
        self.heart_powerup = False
        self.shield_powerup = False

    def fast_powerup_movement(self):

        self.fast_player_y += self.fast_player_y_change

        self.screen.blit(self.fast_img, (self.fast_player_x, self.fast_player_y))

    def heart_powerup_movement(self):

        self.heart_player_y += self.fast_player_y_change

        # Health Powerup
        self.screen.blit(self.heart_img, (self.heart_player_x, self.heart_player_y))
    
    def shield_powerup_movement(self):

        self.shield_player_y += self.fast_player_y_change

        # Health Powerup
        self.screen.blit(self.shield_img, (self.shield_player_x, self.shield_player_y))

    def get_powerup(self, playerX, playerY, powerup):

        match powerup:
            case "fast":
                distance = math.sqrt(math.pow(playerX-self.fast_player_x,2) + (math.pow(playerY-self.fast_player_y,2)))
            case "heart":
                distance = math.sqrt(math.pow(playerX-self.heart_player_x,2) + (math.pow(playerY-self.heart_player_y,2)))
            case "sheild":
                distance = math.sqrt(math.pow(playerX-self.shield_player_x,2) + (math.pow(playerY-self.shield_player_y,2)))

        if distance < 18:
            return True
        else:
            return False

    def define_powerups(self):

        rand_num = random.randint(0,30)

        if rand_num%2 == 0:
            self.fast_powerup = True
        else:
            self.fast_powerup = False
            
        if rand_num%3 == 0:
            self.heart_powerup = True
        else:
            self.heart_powerup = False

        if rand_num%6 == 0:
            self.shield_powerup = True
        else:
            self.shield_powerup = False
      

        
        


        
        




