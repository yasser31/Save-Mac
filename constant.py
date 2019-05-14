import pygame
from pygame.locals import *

pygame.init()

windowWidth = 735
windowHeight = 500
game_window = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)
pygame.display.set_caption('Save Mac')
mac_image = pygame.image.load("images/MacGyver.png").convert()
agent_image = pygame.image.load("images/gardien.png")
back_image = pygame.image.load("images/back_ground.png").convert()
wall_image = pygame.image.load('images/wall.png').convert()
syringe = pygame.image.load("images/syringe.png").convert()
tube = pygame.image.load("images/tube.jpeg").convert()
ether = pygame.image.load("images/ether.png").convert()
wall_wth = 41
wall_hght = 41
m_width = 29
m_height = 33
o_width = 41
o_height = 41
object_pkd = 0