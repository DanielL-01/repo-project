import pygame

class Pipe():
	def __init__(self, pipe_location, screen_location):
		self.pipe = pygame.Rect(0,0, 0.15*screen_rect.width, 0.4*screen_rect.height)
		self.pipe_head = pygame.Rect(0,0,1.2*pipe.width, 0.1*pipe.height)
		
		self.pipe_location = pipe_location
		self.pipe_location = screen_location 


	def show(self):
		pygame.draw.rect(screen, (60,60,60), self.pipe)
		pygame.draw.rect(screen, (60,60,60), self.pipe_head)

	def location(self)
	 
	def move(self):

		self.pipe.x -= 5
		if self.pipe.right<= 0:
			self.pipe.left = screen_rect.right
			
			#bird_pass_pipe = False
		self.pipe_head.midbottom = pipe.midbottom