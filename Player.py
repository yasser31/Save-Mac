import pygame
from App import *
from Maze import mac_coor, Maze, w_rect
from constant import (mac_image, agent_image, back_image, 
                      game_window, object_pkd, syringe, tube, ether)
from function import rect1, rect2, rect3


class Player:
    
    speed = 0.5
    x = mac_coor['C']['x']
    y = mac_coor['C']['y']
    
    def move_right(self):
        self.x = self.x + self.speed
        self.collision('x', 'r')

    def move_left(self):
        self.x = self.x - self.speed
        self.collision('x', 'l')
    
    def move_up(self):
        self.y = self.y-self.speed
        self.collision('y', 'u')
       
    def move_down(self):
        self.y = self.y + self.speed
        self.collision('y', 'd')
    
    args = ['x', 'y', 'r', 'l', 'd', 'u']
    
    def collision(self, *args):
        mac_rect = mac_image.get_rect(left=self.x, top=self.y)
        for wall in w_rect:
            if mac_rect.colliderect(wall):
                if 'y' in args and 'u' in args:
                    self.y = self.y + self.speed
                elif 'x' in args and 'r' in args:
                    self.x = self.x - self.speed
                elif 'y' in args and 'd' in args:
                    self.y = self.y - self.speed
                elif 'x' in args and 'l' in args:
                    self.x = self.x + self.speed
    
    def obj_pkd(self):
        mac_rect = mac_image.get_rect(left=self.x, top=self.y)
        rects = [rect1, rect2, rect3]   
        if mac_rect.colliderect(rect1):
            rects.remove(rect1)
        elif mac_rect.colliderect(rect2):
            rects.remove(rect2)
        elif mac_rect.colliderect(rect3):
            rects.remove(rect3)
        
        return rects
    
    def obj(self):
       
        # agent_rect = agent_image.get_rect(left=697, top=410)
        rects = self.obj_pkd()
        for rect in rects:
            if rect == rect1:
                game_window.blit(syringe, rect) 
            elif rect == rect2:
                game_window.blit(tube, rect)
            elif rect == rect3:
                game_window.blit(ether, rect)   
    
        