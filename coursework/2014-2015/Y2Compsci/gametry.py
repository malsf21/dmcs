import pygame
# make a game class
class TestGame:
    def __init__(self,x,y,sound):
	self.my_x = x
	self.my_y = y
	self.bounce = pygame.mixer.Sound(sound)

    def run(self):
        screen = pygame.display.get_surface()

	mouse_x = 0
	mouse_y = 0

	player = pygame.image.load ('Gaben.jpg').convert()
	font = pygame.font.SysFont("arial", 30) 
	text = font.render ("Meow", True, (255, 0, 0))

	r1 = pygame.Rect (0,100,100,60)
	r2 = pygame.Rect (200,100,50,40)
	rects = [r1,r2]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    return
		if event.type == pygame.KEYDOWN:
                        self.bounce.play(-1)
      			if event.key == pygame.K_UP:
        			self.my_y = self.my_y - 10
      			if event.key == pygame.K_DOWN:
        			self.my_y = self.my_y + 10

		if event.type == pygame.KEYUP:
    			self.bounce.stop()				

		# HOEL test for mouse click
		if event.type == pygame.MOUSEBUTTONDOWN:
            		mouse_x = event.pos[0]
            		mouse_y = event.pos[1]
			

            screen.fill((255, 255, 255))
	    screen.blit (player, (self.my_x, self.my_y)) 
	    for i in rects:
		if i.collidepoint(mouse_x,mouse_y):
			screen.blit (text, (mouse_x,mouse_y))
		elif i.colliderect (self.my_x,self.my_y,30,30):
			screen.blit (text, (self.my_x,self.my_y))
		else:
	    		pygame.draw.rect(screen, (0,255,0), (i.x,i.y,i.width,i.height))

	    # HOEL - does the same thing as update()
            pygame.display.flip()

#----------------------------------------
# Main method creates a TestGame instance
#----------------------------------------

def main():
    pygame.init()
    # HOEL - make full screen
    pygame.display.set_mode((0, 0))
    game = TestGame(200,200,'bounce.wav')
    game.run()

if __name__ == '__main__':
    main()