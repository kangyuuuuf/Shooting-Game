import pygame
class Ground_3():
    def __init__(self,screen):
        self.screen = screen
        self.width = 600
        self.height = 20
        self.color = 255,255,255
        self.rect = pygame.Rect(200,350,self.width,self.height)
    def draw_ground(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

