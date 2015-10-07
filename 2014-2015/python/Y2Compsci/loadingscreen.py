import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
pygame.init()
gender = "na"
named = False
name = ""

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def intro(screen):
	screen.fill((255,255,255))
	font = pygame.font.SysFont("arial",30)
	text = font.render("Click to Start", True, (0,0,0))
	rect = pygame.Rect(320,240,96,96)
	screen.blit(text,(100,100))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if rect.collidepoint(pygame.mouse.get_pos()):
				return
	pygame.display.flip()
	
def display_box(screen, message):
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def choose(screen):
	screen.fill((255,255,255))
	font = pygame.font.SysFont("arial",30)
	text = font.render("Click to Start", True, (0,0,0))
	boy = pygame.Rect(160,120,96,96)
	girl = pygame.Rect(480,360,96,96)
	screen.blit(text,(100,100))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if boy.collidepoint(pygame.mouse.get_pos()):
				gender = "boy"
				return
			elif girl.collidepoint(pygame.mouse.get_pos()):
				gender = "girl"
				return
	pygame.display.flip()
def main():
  screen = pygame.display.set_mode((640,480))
  print ask(screen, "Name") + " was entered"

'''def name(screen):
	while named = False:
		screen.fill((255,255,255))
		font = pygame.font.SysFont("arial",30)
		txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == K_RETURN:
					txtbx

		screen.fill((255,255,255))
		txtbx.update(pygame.event.get())
		txtbx.draw(screen)
		pygame.display.flip()

'''
