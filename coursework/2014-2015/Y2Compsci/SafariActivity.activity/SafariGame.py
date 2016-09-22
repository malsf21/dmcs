#!/usr/bin/python
import pygame
import json
import random
from gi.repository import Gtk

class SafariGame:
    def __init__(self):
	self.data = self.read_data("data/questions.json")
	self.q_index = "1"
	self.used = [1]
	
    def read_data(self,fileondisk):
	file = open(fileondisk)
	return json.load(file)

    def randnum(self):
        while True:
                q_index = random.randint(1,len(self.data)-1)
                if self.used.count(q_index) == 0:
                        self.used.append(q_index)
                        return str(q_index)
		elif len(self.used) == len(self.data)-1:
			self.q_index = "1"
			self.used = [1]
			return str(q_index)

    # The main game loop.
    def run(self):

        screen = pygame.display.get_surface()
	q_font = pygame.font.SysFont("arial",30)
	q_text = q_font.render(self.data[self.q_index]["question"],True,(255,0,0))
	a_font = pygame.font.SysFont("arial",20)
	correct = int(self.data[self.q_index]["answer"])
	print "initial correct " + str(correct)
	q_x = 300
	
	while True:

	    clickstatus = False
	    q_y = 400
            
            while Gtk.events_pending():
                Gtk.main_iteration()

            screen.fill((255, 255, 255))  # 255 for white
	    screen.blit(q_text,(q_x,q_y))
	    answers = []
	    answer_rects = []
	    for i in self.data[self.q_index]["answers"]:
		a_text = a_font.render(i,True,(0,0,0))
		q_y = q_y + 30
		screen.blit(a_text,(q_x,q_y))
		answers.append(i)
		answer_rects.append(pygame.Rect(q_x,q_y,200,30))
		
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

		if event.type == pygame.MOUSEBUTTONDOWN:
			if answer_rects[correct].collidepoint(pygame.mouse.get_pos()):
				self.q_index = self.randnum()	
				q_text = q_font.render(self.data[self.q_index]["question"],True,(255,0,0))
				correct = int(self.data[self.q_index]["answer"])


# This function is called when the game is run directly from the command line:
def main():
    pygame.init()
    pygame.display.set_mode((0, 0))
    game = SafariGame()
    game.run()

if __name__ == '__main__':
    main()
