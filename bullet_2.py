import pygame
from pygame.sprite import Sprite


class Bullet_2(Sprite):
    def __init__(self, screen, ship_2):
        super().__init__()
        self.screen = screen
        self.width = 10
        self.height = 8
        self.moving_fire1=False
        self.moving_fire2=False
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = ship_2.rect.x + 5
        self.rect.y = ship_2.rect.y + 5
        self.x = float(self.rect.x)
        self.color = 0,191,255
        self.speed_factor = 30

    def update(self,life,ship):
        if self.moving_fire1:
            self.x += self.speed_factor
            self.rect.x = self.x
        if self.moving_fire2:
            self.x -= self.speed_factor
            self.rect.x = self.x
        if pygame.sprite.collide_rect(self,ship):
            life.damage_hit = True
            self.x = 1000
            self.y = 1000


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
