import pygame
import sys
from Py_Vid_Player import Video
from Buttons import Button
from pygame import mixer
pygame.init()

####### BASIC SETTINGS ########
SCREEN_W=1000
SCREEN_H=500
BG=(50,50,50)
BLACK=(0,0,0)
Screen= pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption('Main')
W_Speed=10

#####FRAME RATE#####
clock=pygame.time.Clock()
FPS = 60
##### MUSIC ######
BGM =  mixer.music.load('Impernament.mp3')

###### SPRITESHEET LOAD #####
##### MAPS #######
#SECTOR 1
TRAINING_ROOM = pygame.image.load('Training room (2).png')
BARRACKS = pygame.image.load('Sector 1 Barracks.png')
CAFETERIA = pygame.image.load('Sector 1 Cafeteria.png')
DOCKS = pygame.image.load('Sector 1 Docks.png')
L_DOCKS = pygame.image.load('Sector 1 Loading dock.png')
OBSERVATORY = pygame.image.load('Sector 1 Observatory.png')
START_ROOM = pygame.image.load('Sector 1A (1).png')
CORRIDOR = pygame.image.load('Sector 1C.png')
LOBBY1 =  pygame.image.load('Sector A lobby.png')

#SECTOR 2 
BRIDGE = pygame.image.load('Sector 2 Bridge.png')
CIRUIT_BREAK = pygame.image.load('Sector 2 circuit breaker.png')
PARKING = pygame.image.load('Sector 2 Parking lots.png')
ROADS = pygame.image.load('Sector 2 Roads.png')
TOWER_GATE = pygame.image.load('Sector 2 Tower gate.png')

#SECTOR 3 
HQ_ZONE = pygame.image.load('Sector 3 HQ zone (1).png')
LOBBY2 = pygame.image.load('Sector 3 Lobby.png')
BOSS =  pygame.image.load('Sector 3 Reactor room.png')

#CHARACTERS
COMMANDO = pygame.image.load('RCG N51 Commando (1).png')
ASSASSIN = pygame.image.load('RCG N51 Assassin .png')
RECRUIT = pygame.image.load('RCG MERC Recruit.png')
GUNNER =  pygame.image.load('RCG MERC gunner (1).png')
SERGEANT =  pygame.image.load('RCG MERC Sergeant (1).png')
CAPTAIN = pygame.image.load('RCG MERC Captain.png')

#BUTTONS
START_BUTTON = pygame.image.load('RCG MADNESS start button.png')
QUIT_BUTTON =  pygame.image.load('RCG MADNESS Quit button.png')
TITLE_SCREEN =  pygame.image.load('RCG MADNESS Title screen.png')
QUIT_DISPLAY = pygame.transform.scale(QUIT_BUTTON, (400, 150))
START_DISPLAY = pygame.transform.scale(START_BUTTON, (400, 150))

####### STARTUP VIDEO #####
vid = Video('Frenchmen Studios1.mp4')
vid.set_size=((SCREEN_W,SCREEN_H))

def intro():
    while True:
        pygame.init()
        vid.draw(Screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.K_0:
                vid.close()
                play()
            if event.type == pygame.QUIT:
                pygame.quit()

def play():
    run = True
    while run:
        Screen.blit(TRAINING_ROOM,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        pygame.display.update



####### GAME LOOP ########
    
run = True
while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

pygame.quit()
intro()                    

    