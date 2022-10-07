
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, start_x, start_y,image):

        super().__init__()
 
        self.image = image
        self.rect = self.image.get_rect(center=(start_x, start_y))
        self.player_x_change = 0.3

 
