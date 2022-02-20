import pygame
from pygame.sprite import Sprite
from life_2 import Life_2
from ship_2 import Ship_2


class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.width = 10
        self.height = 8
        self.moving_fire1=False
        self.moving_fire2=False
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = ship.rect.x + 5
        self.rect.y = ship.rect.y + 5
        self.x = float(self.rect.x)
        self.color = 255, 255, 0
        self.speed_factor = 30

    def update(self,life_2,ship_2):
        if self.moving_fire1:
            self.x += self.speed_factor
            self.rect.x = self.x
        if self.moving_fire2:
            self.x -= self.speed_factor
            self.rect.x = self.x
        if pygame.sprite.collide_rect(self,ship_2):
            life_2.damage_hit = True
            self.x = 1000;
            self.y = 1000;

            

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
