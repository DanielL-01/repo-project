import pygame
import sys
from random import choice

pygame.init()

class Settings():
	screen_size = [500,500]
	screen_bg_color = [107,52,235]
	land_speed = 5
	bird_fly_speed = 3
	bird_fall_speed = 1
	fps = 25


screen = pygame.display.set_mode(Settings.screen_size)
screen_rect = screen.get_rect()

class Land():

	image = pygame.transform.scale( pygame.image.load("images/land.png"),(2*screen_rect.width, screen_rect.height//5))
	rect = image.get_rect()
	rect.midbottom = screen_rect.midbottom

	@classmethod
	def move(self):
		self.rect.x -= Settings.land_speed 
		if self.rect.centerx <= 0 :
			self.rect.left = screen_rect.left

	@classmethod
	def show(self):
		screen.blit(self.image, self.rect)


class Bird():
	def __init__(self):
		self.image = pygame.image.load("images/bird.png")
		self.rect =  self.image.get_rect()
		self.rect.center = screen_rect.center

		self.fly = False
		self.pass_pipe = False

	def move(self):
		if self.fly:
			self.rect.y -= Settings.bird_fly_speed
		else:
			self.rect.y += Settings.bird_fall_speed

	def show(self):
		screen.blit(self.image, self.rect)





class Pipe():
	def __init__(self,position):
		self.rect = pygame.Rect(0,0, 0.15*screen_rect.width, 0.4*screen_rect.height)
		self.head = pygame.Rect(0,0,1.2*self.rect.width, 0.1*self.rect.height)
		self.position = position
		self.colour = (0,200,0)

		if self.position == "top":
			self.rect.topright = screen_rect.topright
			self.head.midbottom = self.rect.midbottom
		elif self.position == "bottom":
			self.rect.bottomright = screen_rect.bottomright
			self.head.midtop = self.rect.midtop

	def move(self):
		self.rect.x -= 5
		
		if self.position == "top":
			self.head.midbottom = self.rect.midbottom
		elif self.position == "bottom":
			self.head.midtop = self.rect.midtop


	def show(self):
		pygame.draw.rect(screen, self.colour, self.rect)
		pygame.draw.rect(screen, self.colour, self.head)

bird = Bird()

pipes = [Pipe(position) for position in ["top","bottom"]]




def main():
	while True:

		screen.fill(Settings.screen_bg_color)

		bird.show()
		bird.move()

		for pipe in pipes:
			
			if pipe.rect.right <0:
				pipes[0].rect.topleft = screen_rect.topright
				pipes[1].rect.bottomleft = screen_rect.bottomright

				random_height = choice([0,25,50,75,100,125,150])
				minimum_height = Land.rect.height + (0.1*screen_rect.height)
				new_height_bottom = minimum_height + random_height
				new_height_top = screen_rect.height - new_height_bottom-screen_rect.height//5 

				pipes[1].rect = pygame.Rect(0,0,0.15*screen_rect.width, new_height_bottom)
				pipes[0].rect = pygame.Rect(0,0,0.15*screen_rect.width, new_height_top)

				pipes[0].rect.topleft = screen_rect.topright
				pipes[1].rect.bottomleft = screen_rect.bottomright

			pipe.show()
			pipe.move()

		Land.show()
		Land.move()

		pygame.display.flip()
		pygame.time.Clock().tick(Settings.fps)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					bird.fly = True 
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					bird.fly = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_position = pygame.mouse.get_pos()

if __name__ == "__main__":
	
	main()

	
			
