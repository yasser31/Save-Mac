import pygame
from pygame import *
from constant import *


mac_coor = {}
w_rect = []


class Maze:
    
    def __init__(self):
        
        self.coor = []
        with open('Maze.txt', 'r') as self.file:
            self.maze = self.file.read()
                
    def draw(self, game_window, wall_image):
        wall_x = 0
        wall_y = 0
        
        for i in self.maze:
            
            if i == 'm':
                mac_rect = mac_image.get_rect(left=wall_x*wall_wth, top=wall_y*wall_hght)
                self.coor.append({'x': mac_rect.left, 'y': mac_rect.top, 'i': i})
                mac_coor['C'] = {'x': mac_rect.left, 'y': mac_rect.top}
            
            if i == 'S':
                self.coor.append({'x': wall_x * wall_wth, 'y': wall_y * wall_hght, 'i': i})
            
            if i == '1':
                wall_rect = wall_image.get_rect(left=wall_x*wall_wth, 
                                                top=wall_y*wall_hght)
                pygame.draw.rect(wall_image, (255, 0, 0), wall_rect, 2)
                w_rect.append(wall_rect)
                self.coor.append({'x': wall_rect.left, 'y': wall_rect.top, 'i': i})
            
            if i == 'a':
                self.coor.append({'x': 697, 'y': 410, 'i': i})
            
            wall_x += 1
            if i == '\n':
                wall_x = 0
                wall_y += 1
            
        




