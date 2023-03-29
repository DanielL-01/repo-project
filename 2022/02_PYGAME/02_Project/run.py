import pygame
import sys
from random import choice



from settings import Settings
from land import Land
from bird import Bird
from pipe import Pipe







class Game():
	pygame.init()
	settings = Settings()

	screen = pygame.display.set_mode(settings.screen_size)
	screen_rect = screen.get_rect()


	def __init__(self):
		self.land = Land(self)
		self.pipes = [Pipe(self,position) for position in ["top","bottom"]]
		self.bird = Bird(self)


	def reset_pipes(self):
		self.pipes[0].rect.topleft = self.screen_rect.topright
		self.pipes[1].rect.bottomleft = self.screen_rect.bottomright

		random_height = choice([0,25,50,75,100,125,150])
		minimum_height = self.Land.rect.height + (0.1*self.screen_rect.height)
		new_height_bottom = minimum_height + random_height
		new_height_top = self.screen_rect.height - new_height_bottom-self.screen_rect.height//5 

		self.pipes[1].rect = pygame.Rect(0,0,0.15*self.screen_rect.width, new_height_bottom)
		self.pipes[0].rect = pygame.Rect(0,0,0.15*self.screen_rect.width, new_height_top)

		self.pipes[0].rect.topleft = self.screen_rect.topright
		self.pipes[1].rect.bottomleft = self.screen_rect.bottomright


	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.bird.fly = True 
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					self.bird.fly = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_position = pygame.mouse.get_pos()

	
	def main(self):
		while True:

			self.screen.fill(self.settings.screen_bg_color)

			self.bird.show()
			self.bird.move()

			for pipe in self.pipes:
				if pipe.rect.right <0:
					self.reset_pipes()

				pipe.show()
				pipe.move()

			self.land.show()
			self.land.move()

			pygame.display.flip()
			pygame.time.Clock().tick(self.settings.fps)
			self.check_events()

			

				
game = Game()

if __name__ == "__main__":
	
	game.main()

	
			