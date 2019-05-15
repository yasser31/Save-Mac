from Maze import *
from constant import*


class App:
 
    def __init__(self):
        self.running = True
        self.maze = Maze()
    
    def on_init(self):
        self.running = True
        
    def on_render(self):
        game_window.blit(back_image, (0, 0))
        for w in self.maze.coor:
            if w['i'] == 'a':
                agent_rect = agent_image.get_rect(left=697, top=410)
                game_window.blit(agent_image, agent_rect)
            elif w['i'] == '1':
                wall_rect = wall_image.get_rect(left=w['x'], top=w['y'])
                game_window.blit(wall_image, wall_rect)
app = App() 
app.maze.draw(game_window, wall_image)   

