import pygame
from pygame.locals import* 


class Player:
    
    x=42
    y=42
    speed=3
       
        
        
    def move_right(self):
        self.x=self.x+self.speed
            
    def move_left(self):
        self.x=self.x-self.speed
    
    def move_up(self):
        self.y=self.y-self.speed
    
    def move_down(self):
        self.y=self.y+self.speed

player=Player()               

class App:

    

    def launch(self):    
            pygame.init()
            self.game_window=pygame.display.set_mode((756,500),RESIZABLE)
    
    def draw(self):
        
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

        self.wall_image=pygame.image.load('images/wall.png').convert()
        self.a=0
        self.b=0
        self.wall_image_width=41
        self.wall_image_height=41
        
        for i in self.game_maze:
    
            if i==1:
                self.game_window.blit(self.wall_image, self.wall_image.get_rect(left=self.a*self.wall_image_width, 
                top=self.b*self.wall_image_height ))
            self.a+=1
            if self.a >17:
                self.a=0
                self.b+=1
    
    def render(self):
        back_ground_image= pygame.image.load('images/back_ground.png').convert()
        mac_gyver= pygame.image.load('images/MacGyver.png').convert()
        the_maze_agent=pygame.image.load('images/gardien.png').convert()
        mac_gyver_rect= mac_gyver.get_rect(left=player.x,top=player.y)
        self.game_window.blit(back_ground_image,(0,0))
        self.game_window.blit(the_maze_agent,(697,410))
        self.game_window.blit(mac_gyver,mac_gyver_rect)
        app.draw()
        pygame.display.flip()
    
    

app= App()


continue_loop=1
while continue_loop:
    
    app.launch()
    app.render()
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if (keys[K_RIGHT]):
        player.move_right()
 
    if (keys[K_LEFT]):
        player.move_left()
 
    if (keys[K_UP]):
        player.move_up()
 
    if (keys[K_DOWN]):
        player.move_down()
        
    if (keys[K_ESCAPE]):
        continue_loop=0
    
    