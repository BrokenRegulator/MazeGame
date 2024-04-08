import pygame, sys , random # import pygame and sys
 
clock = pygame.time.Clock() # set up the clock
 
from pygame.locals import * # import pygame modules
pygame.init() # initiate pygame
 
pygame.display.set_caption('Pygame Window') # set the window name

# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')
 
WINDOW_SIZE = (400,400) # set up window size
 
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen
 
player_image = pygame.image.load('wall1.jpg') # just make your own image :)
player_image = pygame.transform.scale(player_image, (10, 10))
 
right = False
left = False
up = False
down = False

player_location = [50,50]
player_y_momentum = 0
 
player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())

def open_right():
    center_dotx = 15
    center_doty = 15
    center_dot = pygame.Rect(center_dotx, center_doty, 5, 5)
    center_dot = 0
    left_wall = pygame.image.load('wall.jpg')
    left_wall = pygame.transform.scale(left_wall, (5, 15))
    bottom_wall = pygame.image.load('wall.jpg')
    bottom_wall = pygame.transform.scale(bottom_wall, (15, 5))
    top_wall = pygame.image.load('wall.jpg')
    top_wall = pygame.transform.scale(top_wall, (15, 5))

run = True
while True: # game loop
    screen.fill((146,244,255)) # clear screen by filling it with blue
    
    screen.blit(player_image,player_location) # render player
 
    
   
    
    # movement
    if right == True:
        player_location[0] += 4
        walkRight = True
        walkLeft = False
    if left == True:
        player_location[0] -= 4
    if up == True:
        player_location[1] -= 4
    if down == True:
        player_location[1] += 4
    player_rect.x = player_location[0] # update rect x
    player_rect.y = player_location[1] # update rect y
 
    # test rect for collisions
    if player_location[0] == 400:
        right = False
    
    
    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script
        if keys[pygame.K_LEFT] and x > vel: 
            x -= vel
            left = True
            right = False

        elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
            x += vel
            left = False
            right = True
        
        else: # If the character is not moving we will set both left and right false and reset the animation counter (walkCount)
            left = False
            right = False
            walkCount = 0





            
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right = True
                
            if event.key == K_LEFT:
                left = True
                
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                right = False
                
            if event.key == K_LEFT:
                left = False
                
        if event.type == KEYDOWN:
            if event.key == K_UP:
                up = True
                
            if event.key == K_DOWN:
                moving_down = True
                
        if event.type == KEYUP:
            if event.key == K_UP:
                moving_up = False
                
            if event.key == K_DOWN:
                down = False
        
    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps
