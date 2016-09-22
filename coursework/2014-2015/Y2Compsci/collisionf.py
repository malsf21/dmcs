import pygame


pygame.init()
pygame.display.set_mode((640, 480))
screen = pygame.display.get_surface()
player = pygame.image.load ('player.jpg').convert()
font = pygame.font.SysFont("arial", 30) 
text = font.render ("Meow", True, (255, 0, 0))
r1 = pygame.Rect (0,100,100,60)
r2 = pygame.Rect (200,100,50,40)
rects = [r1,r2]
chary = 0
charx = 0
bounce = pygame.mixer.Sound('bounce.wav')

for event in pygame.event.get():
	if event.type == pygame.QUIT: 
		break
	if event.type == pygame.KEYDOWN:
		bounce.play(-1)
		if event.key == pygame.K_UP:
			chary = self.chary - 10
		elif event.key == pygame.K_DOWN:
			chary = self.chary + 10
		elif event.key == pygame.K_LEFT:
			chary = self.charx - 10
		elif event.key == pygame.K_RIGHT:
			chary = self.charx + 10
	if event.type == pygame.KEYUP:
		bounce.stop()			
		screen.fill((255, 255, 255))
	screen.blit (player, (charx, chary)) 
	for i in rects:
		if i.colliderect (charx,chary,30,30):
			screen.blit (text, (charx,chary))
		else:
			pygame.draw.rect(screen, (0,255,0), (i.x,i.y,i.width,i.height))
			pygame.display.flip()