import pygame
import button

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button image
exit_img = pygame.image.load('save.png').convert_alpha()

#create button instance
exit_button = button.Button(450, 200, exit_img, 0.25)

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	if exit_button.draw(screen):
		run = False

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()