

import pygame

#button class
class Button():
	def __init__(self,game, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.screen = game.screen
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.clicked = False

	def draw(self):

		#draw button on screen
		self.screen.blit(self.image, (self.rect.x, self.rect.y))


	
	#def clicked(self):
#		action = False
#		pos = pygame.mouse.get_pos()
#
		#check mouseover and clicked conditions
#		if self.rect.collidepoint(pos):
#			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
#				self.clicked = True
#				action = True
#
#		return action