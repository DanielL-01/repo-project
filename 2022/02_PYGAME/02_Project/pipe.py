import pygame

class Pipe():
	def __init__(self,game,position):
		self.settings = game.settings
		self.screen = game.screen
		self.screen_rect = game.screen_rect


		self.rect = pygame.Rect(0,0, 0.15*self.screen_rect.width, 0.4*self.screen_rect.height)
		self.head = pygame.Rect(0,0,1.2*self.rect.width, 0.1*self.rect.height)
		self.position = position
		self.colour = (0,200,0)

		if self.position == "top":
			self.rect.topright = self.screen_rect.topright
			self.head.midbottom = self.rect.midbottom
		elif self.position == "bottom":
			self.rect.bottomright = self.screen_rect.bottomright
			self.head.midtop = self.rect.midtop

	def move(self):
		self.rect.x -= 5
		
		if self.position == "top":
			self.head.midbottom = self.rect.midbottom
		elif self.position == "bottom":
			self.head.midtop = self.rect.midtop


	def show(self):
		pygame.draw.rect(self.screen, self.colour, self.rect)
		pygame.draw.rect(self.screen, self.colour, self.head)