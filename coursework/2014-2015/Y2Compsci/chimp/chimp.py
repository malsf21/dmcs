
import os, pygame
import math
import time
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


#functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound


#classes for our game objects
class Fist(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('fist.bmp', -1)
        self.punching = 0

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        "returns true if the fist collides with the target"
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        "called to pull the fist back"
        self.punching = 0


class Chimp(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = x, y
        self.move = 9
        self.dizzy = 0

    def update(self):
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        newpos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or \
           self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        "this will cause the monkey to start spinning"
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image


def main():
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Monkey Fever')
    pygame.mouse.set_visible(0)
    amtpunch = 0
    level = 1
    levelup = False

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(str(amtpunch) + "Poachers stopped!", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

#Prepare Game Objects
    clock = pygame.time.Clock()
    whiff_sound = load_sound('whiff.wav')
    punch_sound = load_sound('punch.wav')
    chimp1 = Chimp(32,32)
    chimps = [chimp1]
    fist = Fist()
    allsprites = pygame.sprite.RenderPlain((fist, chimps))

#Main Loop
    while 1:
        clock.tick(60)
        if amtpunch == math.pow(10, level):
        	levelup = True 
        	level = level + 1

        if levelup == True:
            #background.fill((250, 250, 250))
            #text = font.render("Man, you're mean. More chimps incoming.", 1, (10, 10, 10))
            #background.blit(text, textpos)
            '''if level == 2:
                chimp2 = Chimp(96,96)
                chimps.append(chimp2)
            if level == 3:
                chimp3 = Chimp(144,144)
                chimps.append(chimp3)
            levelup = False'''

    	else:
	    	background.fill((250, 250, 250))
	        text = font.render(str(amtpunch) + "Poachers stopped!", 1, (10, 10, 10))
	        background.blit(text, textpos)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                for chimp in chimps:
                    if fist.punch(chimp):
                        punch_sound.play() #punch
                        chimp.punched()
                        amtpunch = amtpunch + 1
                    else:
                        whiff_sound.play() #miss
            elif event.type is MOUSEBUTTONUP:
                fist.unpunch()

        allsprites.update()

    #Draw Everything
        screen.blit(background, (0, 0))
        pygame.sprite.RenderPlain(chimps).draw(screen)
        pygame.sprite.RenderPlain(fist).draw(screen)
        pygame.display.flip()

if __name__ == '__main__': main()