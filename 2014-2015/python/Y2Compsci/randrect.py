import pygame
import random
import time
class TestGame:
    def __init__ (self, sound):
        self.bounce = pygame.mixer.Sound (sound)
    def run(self):
    	pygame.display.set_mode((640, 480))
        window = pygame.display.get_surface()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    return
            window.fill((255, 255, 255))
            for i in range(10):
                pygame.draw.rect(window,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), (random.randint(0,640),random.randint(0,180),random.randint(0,300),random.randint(0,300)))
            pygame.display.update()
            self.bounce.play(-1)
            time.sleep(1)
            self.bounce.stop()


def main():
    pygame.init()
    game = TestGame(bounce.wav)
    game.run()

if __name__ == '__main__':
    main()