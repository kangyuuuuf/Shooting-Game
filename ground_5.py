import pygame
class Ground_5():
    def __init__(self,screen):
        self.screen = screen
        self.width = 250
        self.height = 20
        self.color = 255,255,255
        self.rect = pygame.Rect(750,200,self.width,self.height)
    def draw_ground(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

