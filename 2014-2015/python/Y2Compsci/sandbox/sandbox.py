import pygame
import random
class Splash:
    def run(self):
	screen = pygame.display.get_surface()
	playbutton = pygame.image.load ('hl2.png').convert()
	playbutton2 = pygame.image.load ('hl3.png').convert()
	insound = pygame.mixer.Sound("chime.wav")
	oversound = pygame.mixer.Sound("over.wav")
	cur_img = playbutton
	invisi_rect = pygame.Rect(200,200,256,256) # invisible rect to check for mouse collision
	while True: # game loop
		for event in pygame.event.get():  # listen for user input
			if event.type == pygame.QUIT: 
				return
			screen.fill((0, 0, 0))  # white screen 
		if invisi_rect.collidepoint(pygame.mouse.get_pos()): # if user clicks go to game
			if event.type == pygame.MOUSEBUTTONDOWN:
				insound.play(0)
				return
			else:
				oversound.play(0)
				cur_img = playbutton2
		else:
			cur_img = playbutton
		screen.blit (cur_img, (200, 200)) # draw button


		pygame.display.flip() # redraw screen	

    
class TestGame:
	def __init__(self,x,y,sound):
		self.my_x = x
		self.my_y = y
		self.step = pygame.mixer.Sound (sound)
		self.clock = pygame.time.Clock()

	def run(self):
		screen = pygame.display.get_surface()
		mouse_x = 0
		mouse_y = 0

		player = pygame.image.load ('gaben1.png').convert()
		font = pygame.font.SysFont("arial", 30) 
		text = font.render ("Half-Life 3 Delayed!", True, (255, 255, 255))

		r1 = pygame.Rect (random.randint(0,1200),random.randint(0,900),random.randint(0,100),random.randint(0,100))
		r2 = pygame.Rect (random.randint(0,1200),random.randint(0,900),random.randint(0,100),random.randint(0,100))
		'''r3 = pygame.Rect (random.randint(0,1200),random.randint(0,900),random.randint(0,100),random.randint(0,100))
		r4 = pygame.Rect (random.randint(0,1200),random.randint(0,900),random.randint(0,100),random.randint(0,100))
		r5 = pygame.Rect (random.randint(0,1200),random.randint(0,900),random.randint(0,100),random.randint(0,100))'''
		rects = [r1,r2]
		while True:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					return
				if event.type == pygame.KEYDOWN:
					self.step.play(-1)
					if event.key == pygame.K_UP:
						self.my_y = self.my_y - 10
					if event.key == pygame.K_DOWN:
						self.my_y = self.my_y + 10
					if event.key == pygame.K_LEFT:
						self.my_x = self.my_x - 10
					if event.key == pygame.K_RIGHT:
						self.my_x = self.my_x + 10

				if event.type == pygame.KEYUP:
					self.step.stop()

				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_x = event.pos[0]
					mouse_y = event.pos[1]
				screen.fill((0, 0, 0))
				screen.blit (player, (self.my_x, self.my_y)) 
				for i in rects:
					if i.collidepoint(mouse_x,mouse_y):
						screen.blit (text, (mouse_x,mouse_y))
						collided = True
					elif i.colliderect (self.my_x,self.my_y,100,100):
						screen.blit (text, (self.my_x,self.my_y))
						collided = True
					else:
						if collided == True:
							r1 = pygame.Rect (random.randint(0,1200),random.randint(0,900),random.randint(0,100),random.randint(0,100))
							r2 = pygame.Rect (random.randint(0,1200),random.randint(0,900),random.randint(0,100),random.randint(0,100))
						pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (i.x,i.y,i.width,i.height))
					pygame.display.flip()

def main():
    pygame.init()
    # HOEL - make full screen
    pygame.display.set_mode((1200, 900))
    splash = Splash() # create instance of splash class
    splash.run() # run the run method in new object instance
    game = TestGame(600,450,'step.wav')
    collided = False
    game.run()

if __name__ == '__main__':
    main()
