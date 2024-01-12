import pygame
import sys
from pygame import mixer


pygame.init()
mixer.init
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Button!")

##### TITLE SCREEN MUSIC######
class Button():
	def __init__(self, image, x_pos,y_pos):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False		

