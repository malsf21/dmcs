import pygame
# make a game class
class TestGame:
    def __init__(self,x,y,sound):
	self.my_x = x
	self.my_y = y
	self.step = pygame.mixer.Sound (sound)

    def run(self):
    	pygame.display.set_mode((640, 480))
        screen = pygame.display.get_surface()

	r1 = pygame.Rect(100,100,100,60)
	r2 = pygame.Rect(200,200,50,40)
	rects = [r1,r2]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    return

		# HOEL - added movement and sound on keydown and keyup
		if event.type == pygame.KEYDOWN:
                        self.step.play(-1)
      			if event.key == pygame.K_UP:
        			self.my_y = self.my_y - 10
      			if event.key == pygame.K_DOWN:
        			self.my_y = self.my_y + 10
                if event.key == pygame.K_a:
                    self.my_y = self.my_x - 10
                if event.key == pygame.K_d:
                    self.my_y = self.my_x + 10
		if event.type == pygame.KEYUP:
    			self.step.stop()				
			

            screen.fill((255, 255, 255))  # 255 for white
            pygame.draw.circle(screen, (255, 0, 0), (self.my_x, self.my_y), 30)
	    for i in rects:
	    	pygame.draw.rect(screen, (0,255,0), (i.x,i.y,i.width,i.height))
            pygame.display.update()

#----------------------------------------
# Main method creates a TestGame instance
#----------------------------------------

def main():
    pygame.init()
    game = TestGame(200,200,'step.bounce')
    game.run()

if __name__ == '__main__':
    main()