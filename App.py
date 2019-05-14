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
                game_window.blit(agent_image, (697, 410))
            elif w['i'] == '1':
                game_window.blit(wall_image, (w['x'], w['y']))
            

app = App() 
app.maze.draw(game_window, wall_image)   

