import sys, pygame

pygame.init()

screenX = 2000
screenY = 1000

screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('My Game')

gilgamesh = pygame.image.load('gilg.jpg').convert()
gilgRect = gilgamesh.get_rect()

#gilgRect.centerx = 200

while True:

	screen.fill((255, 255, 255))
	screen.blit(gilgamesh, gilgRect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				gilgRect.x += 10

	pygame.display.flip()
