import sys
import time
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from life import Life
from life_2 import Life_2
from sound import Sound
from ship_2 import Ship_2
from ground_1 import Ground_1
from ground_2 import Ground_2
from ground_3 import Ground_3
from ground_4 import Ground_4
from ground_5 import Ground_5
def run_game():
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shooting game")
    ship = Ship(screen)
    ship_2 = Ship_2(screen)
    life = Life(screen)
    life_2 = Life_2(screen)
    ground_1 = Ground_1(screen)
    ground_2 = Ground_2(screen)
    ground_3 = Ground_3(screen)
    ground_4 = Ground_4(screen)
    ground_5 = Ground_5(screen)
    sound = Sound()
    bullets = Group()
    bullets_2 = Group()
    
    while True:
        if life_2.finish or life.finish:
            break
        gf.check_events(ship, screen, bullets,sound,ship_2,bullets_2)
        gf.remove_bullet(bullets)
        gf.remove_bullet(bullets_2)
        gf.update_screen(ai_settings, screen, ship, bullets,life,life_2,sound,ship_2,bullets_2,ground_1,ground_2,ground_3,ground_4,ground_5)
        time.sleep(0.02)
    pygame.quit()
    sys.exit()

print("Game initialization complete ...")
print()
print("rules")
print("Two sides control their own object")
print("PLAYER1: arrow as direction, ',','.' open fire" )
print("PLAYER2: WASD as direction, 'g','h' open fire")
print()
input("press return to start")

run_game()








