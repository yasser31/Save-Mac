from App import *
from constant import COLOR, MAC, SPEED
from Maze import mac_coor, w_rect


class Player:
    
    def __init__(self, app):
        self.mac_image = pygame.image.load(MAC).convert()
        self.app = app
        self.rect1 = app.objectsRect(app.syringe)
        self.rect2 = app.objectsRect(app.tube)
        self.rect3 = app.objectsRect(app.ether)
        self.rects = [self.rect1, self.rect2, self.rect3]
        self.objects_collected = 0

    def set_X_Y(self):
        self.x = mac_coor['C']['x']
        self.y = mac_coor['C']['y'] 
        
        return self.x, self.y
    
    def move_right(self):
        self.x = self.x + SPEED
        self.playerWallCollision('x', 'r')

    def move_left(self):
        self.x = self.x - SPEED
        self.playerWallCollision('x', 'l')
    
    def move_up(self):
        self.y = self.y - SPEED
        self.playerWallCollision('y', 'u')
       
    def move_down(self):
        self.y = self.y + SPEED
        self.playerWallCollision('y', 'd')
    
    args = ['x', 'y', 'r', 'l', 'd', 'u']
    
    # detect collision between Mac and walls
    
    def playerWallCollision(self, *args):
        mac_rect = self.mac_image.get_rect(left=self.x, top=self.y)
        for wall in w_rect:
            if mac_rect.colliderect(wall):
                if 'y' in args and 'u' in args:
                    self.y = self.y + SPEED
                elif 'x' in args and 'r' in args:
                    self.x = self.x - SPEED
                elif 'y' in args and 'd' in args:
                    self.y = self.y - SPEED
                elif 'x' in args and 'l' in args:
                    self.x = self.x + SPEED
    
    # detect wich object has been touched
    
    def objPlayerCollision(self):
        mac_rect = self.mac_image.get_rect(left=self.x, top=self.y)
        for item in self.rects:
            if item == self.rect1:
                self.removeObject(self.rect1)
            elif item == self.rect2:
                self.removeObject(self.rect2)
            elif item == self.rect3:
                self.removeObject(self.rect3)
    
    # blit the objects on the screen               
    
    def objectsBlit(self):
        for rect in self.rects:
            if rect == self.rect1:
                self.app.game_window.blit(self.app.syringe, rect) 
            elif rect == self.rect2:
                self.app.game_window.blit(self.app.tube, rect)
            elif rect == self.rect3:
                self.app.game_window.blit(self.app.ether, rect)   
    
    # detect Mac Gyver has escaped   
    
    def win(self):
        mac_rect = self.mac_image.get_rect(left=self.x, top=self.y)
        agent_rect = self.app.agent_image.get_rect(left=697, top=410)
        if mac_rect.colliderect(agent_rect): 
            if self.objects_collected == 3:
                self.app.game_over = True
                return 'win'
    
    # detect if Mac went to the end without the three objects
    
    def loose(self):
        mac_rect = self.mac_image.get_rect(left=self.x, top=self.y)
        agent_rect = self.app.agent_image.get_rect(left=697, top=410)
        if mac_rect.colliderect(agent_rect): 
            if self.objects_collected != 3:
                self.app.game_over = True
                return 'loose'
    
    # render the objects counter on the screen
    
    def counter(self):
        font = pygame.font.SysFont(None, 25)
        text = font.render(str(self.objects_collected), True, COLOR)
        self.app.game_window.blit(text, (42, 42))

    # detect collision and remove the object   
    
    def removeObject(self, rect):
        mac_rect = self.mac_image.get_rect(left=self.x, top=self.y)
        if mac_rect.colliderect(rect):
            self.rects.remove(rect)
            self.objects_collected += 1