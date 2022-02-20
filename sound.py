import pygame
from pygame.locals import *

class Sound():
    def __init__(self):
        self.sound_1 = pygame.mixer.Sound("sound1.wav")
        self.sound_1.set_volume(10)
        self.sound_1_v = False
    def fire_sound(self):
        if self.sound_1_v:
            self.sound_1.play()
            self.sound_1_v = False
            
