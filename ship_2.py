import pygame
from ground_1 import Ground_1
from ground_2 import Ground_2
from ground_3 import Ground_3
from ground_4 import Ground_4
from ground_5 import Ground_5


class Ship_2():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("object2.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = 0
        self.rect.y = 250
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving = False
        self.moving_down = False
        self.ship_speed_factor = 0
        self.ship_speed_factor2 = 0
        self.bullets_allowed = 4
        self.center_x = 980
        self.center_y = 300
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self,ground_1,ground_2,ground_3,ground_4,ground_5):
        if self.rect.bottom < self.screen_rect.bottom:
            self.ship_speed_factor2 += 2
            self.moving = False
        result_1 = pygame.sprite.collide_rect(self,ground_1)
        result_4 = pygame.sprite.collide_rect(self,ground_2)
        result_2 = pygame.sprite.collide_rect(self,ground_3)
        result_3 = pygame.sprite.collide_rect(self,ground_4)
        result_5 = pygame.sprite.collide_rect(self,ground_5)
        if self.ship_speed_factor2 > 0:
            if result_1:
                self.moving= True
                self.center_y = 481
            if result_4:
                self.moving= True
                self.center_y = 481
            if result_2:
                self.moving= True
                self.center_y = 331
            if result_3:
                self.moving= True
                self.center_y = 181
            if result_5:
                self.moving= True
                self.center_y = 181
        if self.rect.bottom >= self.screen_rect.bottom:
            self.moving = True
            self.center_y = 630
        if self.moving:
            self.ship_speed_factor2 = 0
            if self.moving_up:
                self.ship_speed_factor2 -= 30
            if self.moving_right:
                if self.ship_speed_factor < 20:
                    self.ship_speed_factor = self.ship_speed_factor + 5
            if self.moving_left:
                if self.ship_speed_factor > -20:
                    self.ship_speed_factor = self.ship_speed_factor - 5

            if self.ship_speed_factor > 0:
                self.ship_speed_factor = self.ship_speed_factor - 2 * 2
                if self.ship_speed_factor <0:
                    self.ship_speed_factor = 0
            if self.ship_speed_factor < 0:
                self.ship_speed_factor = self.ship_speed_factor + 2 * 2
                if self.ship_speed_factor >0:
                    self.ship_speed_factor = 0
        if self.rect.right > self.screen_rect.right:
                self.ship_speed_factor = 0
                self.center_x = 980
        if self.rect.left < self.screen_rect.left:
                self.ship_speed_factor = 0
                self.center_x = 0
        self.center_x += self.ship_speed_factor
        self.rect.x = self.center_x


        self.center_y += self.ship_speed_factor2
        self.rect.y = self.center_y
