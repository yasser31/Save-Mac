from App import *

from constant import COLOR, BACKCOLOR

from Player import *


class Game():
    
    def __init__(self):
        self.app = App()
        self.app.maze.set_coordinates(self.app.wall_image)
        self.player = Player(self.app)
        self.player.x, self.player.y = self.player.set_X_Y()
    
    def main(self):
        while(self.app.running):
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
                self.app.running = False
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.app.running = False
            self.app.on_render()
            self.app.game_window.blit(self.player.mac_image, 
                                      (self.player.x, self.player.y))
            self.player.objects_blit()
            self.player.obj_player_collision()               
            self.player.loose()
            self.player.win()
            self.player.counter()
            pygame.display.flip()
            if self.app.game_over is True:
                break
        while self.app.game_over is True:
            if self.player.loose() == 'loose':
                self.app.message_to_screen('sorry, you lost, click C to restart, Q to quit', 
                                           COLOR, BACKCOLOR)
            if self.player.win() == 'win':
                self.app.message_to_screen("You'r the champ, C to restart, Q to quit", 
                                           COLOR, BACKCOLOR)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        self.app.game_over = False
                        self.app.running = False
                    elif event.key == K_c:
                        self.app.game_over = False
                        self.restart()

    def restart(self):
        game = Game()
        game.main()

if __name__ == '__main__':
    game = Game()
    game.main()