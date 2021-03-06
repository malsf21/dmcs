import pygame
class TestGame:
    def __init__(self,x,y,sound):
	self.my_x = x
	self.my_y = y
	self.step = pygame.mixer.Sound (sound)

    def run(self):
        screen = pygame.display.get_surface()
	player = pygame.image.load ('player.jpg').convert()
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
                        self.step.play(-1)
      			if event.key == pygame.K_UP:
        			self.my_y = self.my_y - 10
      			if event.key == pygame.K_DOWN:
        			self.my_y = self.my_y + 10
		if event.type == pygame.KEYUP:
    			self.step.stop()				
			

            screen.fill((255, 255, 255))
	    # HOEL changed circle for image
	    screen.blit (player, (self.my_x, self.my_y)) 
	    for i in rects:
		# HOEL added collision detection on rectangles using pygame Rect class built-in method colliderect
		if i.colliderect (self.my_x,self.my_y,30,30):
			screen.blit (text, (self.my_x,self.my_y))
		else:
	    		pygame.draw.rect(screen, (0,255,0), (i.x,i.y,i.width,i.height))
            pygame.display.flip()

#----------------------------------------
# Main method creates a TestGame instance
#----------------------------------------

def main():
    pygame.init()
    pygame.display.set_mode((640, 480))
    game = TestGame(200,200,'step.wav')
    game.run()

if __name__ == '__main__':
	main()