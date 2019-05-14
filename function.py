import pygame
from App import *
from random import choice
from Maze import w_rect
from Player import *
from constant import (syringe, tube, ether, game_window, back_image, 
                      mac_image, agent_image, object_pkd)


def objCollision(image):
    pygame.init()
    em_space_x = []
    em_space_y = []
    for coor in app.maze.coor:
        if coor['i'] == 'S':
            em_space_x.append(coor['x'])
            em_space_y.append(coor['y'])
    xo = choice(em_space_x)
    yo = choice(em_space_y)
    rect = image.get_rect(left=xo, top=yo)
    return rect

rect1 = objCollision(syringe)
rect2 = objCollision(tube)
rect3 = objCollision(ether)


# def objects_draw():
    # game_window.blit(syringe, (xo1, yo1))
    # game_window.blit(tube, (xo2, yo2))
    # game_window.blit(ether, (xo3, yo3))

