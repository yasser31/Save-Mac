from random import choice

import pygame

from pygame.locals import *

from constant import*

from Maze import *


class App:
    # init the App instance
    def __init__(self):
        pygame.init()
        self.running = True
        self.game_over = False
        self.maze = Maze()
        self.game_window = pygame.display.set_mode((WINDOW_WIDTH, 
                                                   WINDOW_HEIGHT)) 
        self.back_image = pygame.image.load(BACK_IMAGE).convert()
        self.agent_image = pygame.image.load(AGENT).convert()
        self.wall_image = pygame.image.load(WALL_IMAGE).convert()
        self.syringe = pygame.image.load(SYRINGE).convert()
        self.tube = pygame.image.load(TUBE).convert()
        self.ether = pygame.image.load(ETHER).convert()
    
    # render the maze, background image and the agent     
    
    def on_render(self):
        pygame.display.set_caption('Save Mac')
        self.game_window.blit(self.back_image, (0, 0))
        for w in self.maze.coor:
            if w['i'] == 'a':
                agent_rect = self.agent_image.get_rect(left=697, top=410)
                self.game_window.blit(self.agent_image, agent_rect)
            elif w['i'] == '1':
                wall_rect = self.wall_image.get_rect(left=w['x'], top=w['y'])
                pygame.draw.rect(self.wall_image, (255, 0, 0), wall_rect, 2)
                self.game_window.blit(self.wall_image, wall_rect)
    
    # look for the possible coordiantes for the objects and get their rects
    
    def objects_rect(self, image):
        em_space = [{'x': coor['x'], 'y':coor['y']} for coor in self.maze.coor 
                    if coor['i'] == 'S']
        object_coor = choice(em_space)
        rect = image.get_rect(left=object_coor['x'], top=object_coor['y'])
        return rect
    
    # shows the message at the end of the game
    
    def message_to_screen(self, msg, Color, backcolor):
        font = pygame.font.SysFont(None, 25)
        text = font.render(msg, True, Color)
        self.game_window.fill(backcolor)
        self.game_window.blit(text, (WINDOW_WIDTH / 4, 
                                     WINDOW_HEIGHT / 2))
        pygame.display.flip()

        