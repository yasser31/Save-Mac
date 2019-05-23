from constant import *


class Maze:
    
    def __init__(self):
        # starting position of Mac Gyver
        self.mac_coor = {}
        # list of the maze wall's rects, used for Mac collision with walls 
        self.w_rect = []
        # dict for all the coordinates, with a letter specifying wich element 
        # it is 
        self.coor = []
        with open('Maze.txt', 'r') as self.file:
            self.maze = self.file.read()
    
    # sets the maze coordinates including the player and agent and the space            
    
    def set_coordinates(self, wall_image):
        # wall sprit in x
        wall_x = 0
        # wall sprit in y
        wall_y = 0
        for i in self.maze:
            # m is Mac Gyver
            if i == 'm':
                self.coor.append({'x': wall_x*WALL_WTH, 'y': wall_y*WALL_HGHT, 
                                 'i': i})
                self.mac_coor['C'] = {'x': wall_x*WALL_WTH, 
                                      'y': wall_y*WALL_HGHT}
            # S is empty space
            if i == 'S':
                self.coor.append({'x': wall_x * WALL_WTH, 'y': wall_y * 
                                 WALL_HGHT, 'i': i})
            # 1 is the wall
            if i == '1':
                wall_rect = wall_image.get_rect(left=wall_x*WALL_WTH, 
                                                top=wall_y*WALL_HGHT)
                self.w_rect.append(wall_rect)
                self.coor.append({'x': wall_rect.left, 'y': wall_rect.top, 'i': 
                                 i})
            # a is the agent
            if i == 'a':
                self.coor.append({'x': 697, 'y': 410, 'i': i})
            
            wall_x += 1
            if i == '\n':
                wall_x = 0
                wall_y += 1
            
        




