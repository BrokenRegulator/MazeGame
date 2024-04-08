import pygame, sys, random, math
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Maze Game")

char_size = 50
#Sprites & Rects
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (500,500))
bg_bad = pygame.image.load('Forest.jpg')
bg_bad = pygame.transform.scale(bg_bad, (500,500))
wall = pygame.image.load('wall1.jpg')
wall = pygame.transform.scale(wall, (50,50))
wall_Bot = wall.get_rect()
fin_rect = pygame.Rect(300, 0, 50, 20)
#player_rect = pygame.image.load('R1.png').get_rect()
player_rect = pygame.Rect(*win.get_rect().center, 0, 0).inflate(25, 25)
#wall_Bot = pygame.Rect(225, 140, 0, 0).inflate(75, 75)
#wall_Bot = pygame.transform.scale(wall_Bot,(30,10))
bg = pygame.transform.scale(bg,(500, 500))

rect_List = []
touch_wall = False
x = 50
y = 400
width = 40
height = 60
vel = 2.5
player_location = player_rect.center


clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0
maze = [[1,1,1,1,1,1,0,1,1,1],
        [1,1,1,0,0,0,0,1,1,1],
        [1,1,1,1,0,0,1,1,1,1],
        [1,1,0,0,0,1,1,1,1,1],
        [1,1,0,1,0,0,0,0,0,1],
        [1,0,0,1,1,0,1,1,0,1],
        [1,0,1,0,0,0,1,1,1,1],
        [1,1,0,0,1,0,0,0,1,1],
        [1,0,0,0,0,1,1,0,1,1],
        [1,0,0,1,1,1,1,1,1,1]]

def drawMaze():
    row_num=0
    col_num=0
    global rect_List
    rect_List = []

    for row in maze:
        #print(row)
        col_num=0
        for x in row:
            #print (x)
            if x==1:
                new_wall = wall.get_rect()
                new_wall.center = (25+col_num*50,25+row_num*50)
                win.blit(wall, new_wall)
                rect_List.append(new_wall)
            col_num+=1
        row_num+=1

def checkCol(player):
    for wall in rect_List:
        if player.colliderect(wall):
            print(x,y,player,wall)
            return True
    return False

def EndGame():
    print('Nice Job')
    
    
def resizeChar(fileName):
    img = pygame.image.load(fileName)
    img = pygame.transform.scale(img, (char_size, char_size))
    return img
    
def redrawGameWindow():
    global walkCount

    #draw background
    win.blit(bg, (0,0))

    drawMaze()
    
    if walkCount + 1 >= 27:
        walkCount = 0

    
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    #draw hitbox smaller than image
    player_rect.topleft = (x+14, y+14)
    
    pygame.display.update() 
    

char = resizeChar('standing.png')
char = pygame.transform.scale(char,(50,50))
walkRight = [resizeChar('R1.png'), resizeChar('R2.png'), resizeChar('R3.png'), resizeChar('R4.png'), resizeChar('R5.png'), resizeChar('R6.png'), resizeChar('R7.png'), resizeChar('R8.png'), resizeChar('R9.png')]
walkLeft = [resizeChar('L1.png'), resizeChar('L2.png'), resizeChar('L3.png'), resizeChar('L4.png'), resizeChar('L5.png'), resizeChar('L6.png'), resizeChar('L7.png'), resizeChar('L8.png'), resizeChar('L9.png')]

run = True



while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #collition
    touch_wall = checkCol(player_rect)
    if touch_wall:
        print('Game Over')
        break  

    
    if player_rect.colliderect(fin_rect):
        EndGame()
        break

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    elif keys[pygame.K_UP] and y > 0:
        y -= vel
        right = True
        left = False
    elif keys[pygame.K_DOWN] and y < 400:
        y += vel
        left = True
        right = False
    else: 
        left = False
        right = False
        walkCount = 0
        
  

    redrawGameWindow() 
    
    
pygame.quit()
