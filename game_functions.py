import pygame
import sys
from bullet import Bullet
from ship import Ship
from life import Life
from life_2 import Life_2
from sound import Sound
from ship_2 import Ship_2
from bullet_2 import Bullet_2
from ground_1 import Ground_1
def check_events(ship, screen, bullets,sound,ship_2,bullets_2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # key down
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_COMMA:
                if len(bullets) < ship.bullets_allowed:
                    new_bullet = Bullet(screen, ship)
                    bullets.add(new_bullet)
                    new_bullet.moving_fire2 = True
                    sound.sound_1_v = True
            elif event.key == pygame.K_PERIOD:
                if len(bullets) < ship.bullets_allowed:
                    new_bullet = Bullet(screen, ship)
                    bullets.add(new_bullet)
                    new_bullet.moving_fire1 = True
                    sound.sound_1_v = True
            if event.key == pygame.K_a:
                ship_2.moving_left = True
            elif event.key == pygame.K_d:
                ship_2.moving_right = True
            elif event.key == pygame.K_w:
                ship_2.moving_up = True
            elif event.key == pygame.K_s:
                ship_2.moving_down = True
            elif event.key == pygame.K_g:
                if len(bullets_2) < ship_2.bullets_allowed:
                    new_bullet_2 = Bullet_2(screen, ship_2)
                    bullets_2.add(new_bullet_2)
                    new_bullet_2.moving_fire2 = True
                    sound.sound_1_v = True
            elif event.key == pygame.K_h:
                if len(bullets_2) < ship_2.bullets_allowed:
                    new_bullet_2 = Bullet_2(screen, ship_2)
                    bullets_2.add(new_bullet_2)
                    new_bullet_2.moving_fire1 = True
                    sound.sound_1_v = True

        elif event.type == pygame.KEYUP:  # key up
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False
            if event.key == pygame.K_d:
                ship_2.moving_right = False
            elif event.key == pygame.K_a:
                ship_2.moving_left = False
            elif event.key == pygame.K_w:
                ship_2.moving_up = False
            elif event.key == pygame.K_s:
                ship_2.moving_down = False

                
def update_screen(ai_settings, screen, ship, bullets,life,life_2,sound,ship_2,bullets_2, ground_1,ground_2,ground_3,ground_4,ground_5):
    pygame.display.flip()
    ship.update(ground_1,ground_2,ground_3,ground_4,ground_5)
    ship_2.update(ground_1,ground_2,ground_3,ground_4,ground_5)
    screen.fill(ai_settings.bg_color)
    life.damage()
    life.draw_life()
    life_2.damage()
    life_2.draw_life()
    ground_1.draw_ground()
    ground_2.draw_ground()
    ground_3.draw_ground()
    ground_4.draw_ground()
    ground_5.draw_ground()
    sound.fire_sound()
    for i in bullets:
        i.update(life_2,ship_2)
        i.draw_bullet()
    for j in bullets_2:
        j.update(life,ship)
        j.draw_bullet()
    ship.blitme()
    ship_2.blitme()
    


def remove_bullet(bullets):
    for i in bullets.copy():
        if i.rect.right >= 1000 or i.rect.left <= 0:
            bullets.remove(i)
def remove_bullet(bullets_2):
    for j in bullets_2.copy():
        if j.rect.right >= 1000 or j.rect.left <= 0:
            bullets_2.remove(j)
