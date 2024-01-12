import pygame

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image
    ###SPRITE ANIMS#########
    def get_image(self,frame,width,height,scale,colour):
        image =  pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame*width),0,width,height))
        image =  pygame.transform.scale(image,(width*scale, height*scale))
        image.set_colorkey(colour)
        return image

class player():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y = 0
        self.attack_type = 0
    
    def move(self,screen_width,screen_height,surface):
        S_SPEED = 10
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        #Movement
        if key[pygame.K_a]:
            dx= -S_SPEED
        if key[pygame.K_d]:
            dx= +S_SPEED
        if key[pygame.K_s]:
            dy= +S_SPEED
        if key[pygame.K_w]:
            dy= -S_SPEED
        
        #Jumping
            
        #Attacking
            if key[pygame.K_SPACE]:
                self.attack(surface)


                
        
        #Border
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            dy =screen_height - 110 - self.rect.bottom

        
        self.rect.x += dx
        self.rect.y += dy
    def attack(self,surface):
        attacking_rect =  pygame.Rect(self.rect.centerx, self.rect.y, 2*self.rect.width, self.rect.height)
        pygame.draw.rect(surface,(0,255,0),attacking_rect)
    
    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0), self.rect)

