import pygame,os,sys
pygame.init()

#Configurations
WIDTH, HEIGHT= 900,500
WINDOW= pygame.display.set_mode((WIDTH,HEIGHT))
FPS= 60
W_Speed= 3
S_speed=6
pygame.display.set_caption("MADNESS: infiltration(DEMO)")

#Sprites
TRAINING_ROOM= pygame.image.load('Training room (2).jpeg')
BACKGROUND=(100,240,167)

#Commando Animations
#Commando_Test= pygame.image.load('Commando Idle 1.png')

class Assasin(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites=[]
        self.is_animating= True
        self.sprites.append(pygame.image.load('Commando Idle 1.png'))
        self.sprites.append(pygame.image.load('Commando Idle 2.png'))
        self.sprites.append(pygame.image.load('Commando Idle 3.png'))
        self.sprites.append(pygame.image.load('Commando Idle 4.png'))
        self.current_sprite= 0
        self.image = self.sprites[self.current_sprite]

        self.rect= self.image.get_rect()
        self.rect.topleft= [pos_x,pos_y]
    
    def movement(movement,self):
        if movement[pygame.K_a]:
            self.x -= W_Speed
        if movement[pygame.K_d]:
            self.x += W_Speed
    
    def animate(self):
        self.is_animating= True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.1

        if self.current_sprite>= len(self.sprites):
            self.current_sprite=0

        self.image = self.sprites[int(self.current_sprite)]


#Placing the character
moving_sprites=pygame.sprite.Group()
player = Assasin(20,100)
moving_sprites.add(player)


#Screen display
def window():
    WINDOW.blit(TRAINING_ROOM,(0,0))
    moving_sprites.draw(WINDOW)
    moving_sprites.update()
    pygame.display.flip()
    pygame.display.update()
    
#Main game loop
def main_loop():
    clock = pygame.time.Clock()
    loop = True
    while loop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop= False 
        movement=pygame.key.get_pressed()
        window()
    pygame.quit()

if __name__ == "__main__":
    main_loop()


