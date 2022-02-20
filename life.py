import pygame
class Life():
    def __init__(self,screen):
        self.screen = screen
        self.width = 400
        self.height = 20
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.color = 255,0,0
        self.damage_hit = False
        self.finish = False
    def damage(self):
        if self.damage_hit:
            self.width -= 20
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.damage_hit = False
        if self.width < 5:
            self.finish = True
            print("GAMEOVER PLAYER2 WIN")
            
    def draw_life(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
