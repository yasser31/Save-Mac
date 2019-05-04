import pygame
from pygame.locals import*

pygame.init()

game_window= pygame.display.set_mode((720, 476), RESIZABLE)

back_ground_image=pygame.image.load('images/back_ground.png').convert()

game_window_background=game_window.blit(back_ground_image,(0,0))

mac_gyver= pygame.image.load('images/MacGyver.png').convert()

mac_gyver_position=mac_gyver.get_rect()

game_window.blit(mac_gyver,mac_gyver_position)

pygame.display.flip()


while 1:
    continue