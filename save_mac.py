import pygame
from random import choice
from pygame.locals import* 

class Player:
    
    
    x=42
    y=42
    speed=1
        
    
    def move_right(self):
        
        self.x=self.x+self.speed
        maze.wall.sort()
        
        for wall in maze.wall:
            if collision.isCollision(wall.left,wall.top,self.x, self.y,30):
                self.x=42
        
     
                
    def move_left(self):
        self.x=self.x-self.speed
        maze.wall.sort()
        for wall in maze.wall:
            if collision.isCollision(wall.left,wall.top,self.x, self.y,30):
                self.x=self.x+42
       
     
    def move_up(self):
        self.y=self.y-self.speed
        maze.wall.sort()
        for wall in maze.wall:
            if collision.isCollision(wall.left,wall.top,self.x, self.y,30):
                self.y=self.y+42
            if self.y<=41:
                self.y=42

    
    def move_down(self):
        self.y=self.y+self.speed
        maze.wall.sort()
        for wall in maze.wall:
            if collision.isCollision(wall.left,wall.top,self.x, self.y,32):
                self.y=self.y-42
            if self.y+37==500:
                self.x=459

player=Player()   



objects =['syringe', 'tube','ether']

liste1=[41,123,205,287,328,369,410,492,574,656]    
liste2=[82,123,164,246,328,369,410]
        
for hack in objects:
    
    xo =choice(liste1)
    yo = choice(liste2)
    
    if hack=='syringe':
        image1=pygame.image.load("images/syringe.png")
        rect1 =image1.get_rect(left=xo, top=yo)
        
    elif hack=='tube':
        image2=pygame.image.load("images/tube.jpeg")
        rect2 =image2.get_rect(left=xo, top=yo)
      
    elif hack=='ether':
        image3=pygame.image.load("images/ether.png")
        rect3 =image3.get_rect(left=xo, top=yo)
    
    

    
class Collision:
    
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:  
            if y1 >= y2 and y1 <= y2 + 37:
                return True 
           
            return False

collision=Collision()


class Maze:
    
    def __init__(self):
    
        self.game_maze= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
         1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,
         1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,
         1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,
         1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,
         1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,
         1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,
         1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,
         1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,
         1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,
         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,
         1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        ] 
        self.wall=[]
    
    def draw(self,game_window, wall_image):
    
        self.wall_image=pygame.image.load('images/wall.png').convert()
        self.w_sprit_x=0
        self.w_sprit_y=0
        self.wall_image_width=41
        self.wall_image_height=41
        self.wall=[]
        
        for i in self.game_maze:
            
            if i==1:
                self.wall_image_rect=self.wall_image.get_rect(left=self.w_sprit_x*self.wall_image_width, 
                top=self.w_sprit_y*self.wall_image_height )
                game_window.blit(self.wall_image,self.wall_image_rect,)
                self.wall.append(self.wall_image_rect)
                pygame.draw.rect(self.wall_image,(255,0,0),self.wall_image_rect,2)
            
            self.w_sprit_x+=1
            
            if self.w_sprit_x >17:
                self.w_sprit_x=0
                self.w_sprit_y+=1
            
maze=Maze()

class App:
 
    windowWidth = 735
    windowHeight = 500
    player = 0
 
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.back_image = None
        self.wall_image = None
        self.player = Player()
        self.maze = maze
        

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Save Mac')
        self.game_window = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        self.running = True
        self.gardien_image=pygame.image.load("images/gardien.png")
        self.mac_image = pygame.image.load("images/MacGyver.png").convert()
        self.back_image= pygame.image.load("images/back_ground.png").convert()
    
    def on_event(self, event):
        if event.type == QUIT:
            self.running = False
 
     
    
    def on_render(self):
        self.game_window.blit(self.back_image,(0,0))
        self.game_window.blit(self.gardien_image,(697,410))
        self.game_window.blit(image1,rect1)
        self.game_window.blit(image2,rect2)
        self.game_window.blit(image3,rect3)
        self.mac_rect=self.mac_image.get_rect(left=self.player.x, top=self.player.y)
        self.game_window.blit(self.mac_image,self.mac_rect)
        self.maze.draw(self.game_window, self.wall_image)
        pygame.display.flip()
    
   
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
 
        while( self.running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if (keys[K_RIGHT]):
                self.player.move_right()
 
            if (keys[K_LEFT]):
                self.player.move_left()
 
            if (keys[K_UP]):
                self.player.move_up()
 
            if (keys[K_DOWN]):
                self.player.move_down()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute() 


