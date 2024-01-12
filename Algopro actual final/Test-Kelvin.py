import pygame
import Sprites
from Sprites import player

pygame.init()

####### BASIC SETTINGS ########
SCREEN_W=500
SCREEN_H=500
BG=(50,50,50)
BLACK=(0,0,0)
Screen= pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption('spritesheets')
W_Speed=10
#####FRAME RATE#####
clock=pygame.time.Clock()
FPS = 60

#####SPRITESHEET LOAD#####
TRAINING_ROOM = pygame.image.load('Training room (2).jpeg').convert_alpha()
Assassin= pygame.image.load('RCG N51 Assassin Idle (1).png').convert_alpha()

sprite_sheet= Sprites.SpriteSheet(Assassin)

####### ANIMATION ########


animation_list=[]
animation_steps = [4, 4, 6]
action = 0
last_update =  pygame.time.get_ticks()
animation_cooldown= 200
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list=[]
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter,480,484,0.4,BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

######### WHAT THE SCREEN SHOWS############
def window():
    Screen.blit(TRAINING_ROOM,(0,0))
    pygame.display.flip()
    pygame.display.update()



###Player creation###
Player_1 = player(200,310)
Player_2 = player(0,0)


run= True
while run:
    clock.tick(FPS)
    Screen.blit(TRAINING_ROOM,(-200,-300))
    
    Player_1.draw(Screen)
    Player_2.draw(Screen)
    
    Player_1.move()
    #Player_2.move()
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    Screen.blit(animation_list[action][frame],(step_counter*0,0))

###ANIMATION CYCLE####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and action > 0:
                action = 1
                frame = 0
            if event.key == pygame.K_d and action > 0:
                action = 1
                frame = 0
                
            if event.key == pygame.K_r and action < len(animation_list) - 1:
                action += 1 
                frame = 0
            else:
                action = 0
###MOVEMENT OPTIONS####

    pygame.display.update()