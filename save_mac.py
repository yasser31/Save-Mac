#! /home/yasser/Bureau/projets N°3/env/bin/python
# coding: utf-8
from App import *
from Player import * 
from constant import mac_image, game_window, agent_image
# from function import objects_draw


player = Player() 

 
while(app.running):
        
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
    game_window.blit(mac_image, (player.x, player.y))
    player.obj()
    # objects_draw()
    pygame.display.flip()