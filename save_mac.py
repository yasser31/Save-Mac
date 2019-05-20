#! /home/yasser/Bureau/projets N°3/env/bin/python
# coding: utf-8
from App import *
from constant import COLOR, BACKCOLOR
from Player import *

# the main loop


def main():
    player = Player()
    while(app.running):
        while app.game_over is True:
            if player.loose() == 'loose':
                app.messageToScreen('sorry, you lost, click C to restart, Q to quit', 
                                    COLOR, BACKCOLOR)
            if player.win() == 'win':
                app.messageToScreen("You'r the champ, C to restart, Q to quit", 
                                    COLOR, BACKCOLOR)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        app.game_over = False
                        app.running = False
                    elif event.key == K_c:
                        app.game_over = False
                        main()
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
            app.running = False
            
        for event in pygame.event.get():
            if event.type == QUIT:
                app.running = False
        app.on_render()
        app.game_window.blit(player.mac_image, (player.x, player.y))
        player.objectsBlit()
        player.objPlayerCollision()               
        player.loose()
        player.win()
        player.counter()
        pygame.display.flip()
       

if __name__ == '__main__':
    main()
    
    
