import pygame
from pygame.locals import* #imports pygame CONSTANTS so we can write 
                           #CONSTANTS rather than pygame.CONSTANTS


# initializes pygame
pygame.init() 


# creates a window for th game
game_window= pygame.display.set_mode((739, 490), RESIZABLE) 

# uploads the background image for the game
back_ground_image=pygame.image.load('images/back_ground.png').convert() 

# displays the background image
game_window_background=game_window.blit(back_ground_image,(0,0))

#loading MacGyver image
mac_gyver= pygame.image.load('images/MacGyver.png').convert()

# setting the starting position of MacGyver
mac_gyver_position=mac_gyver.get_rect(left=42,top=42)

# shows MacGyver image   
game_window.blit(mac_gyver,mac_gyver_position)

# the structure of ou maze game
game_maze= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
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

# uploads the image that will represent the maze wall
wall_image=pygame.image.load('images/wall.png').convert()

# represent the coefficient that will be multiplied with the width and height of the wall's image
# so we can get the exact x and y of the wall's image
a=0
b=0
wall_image_width=41
wall_image_height=41

# draws the maze 
for i in game_maze:
    
    if i==1:
        game_window.blit(wall_image, wall_image.get_rect(left=a*wall_image_width, top=b*wall_image_height ))
    x+=1
    if x >17:
        x=0
        y+=1
    # update the window so we can see the changes
    pygame.display.flip()

# stops the window from closing
while 1:
    continue