import pygame
class TestGame:
    def __init__(self,x,y,sound):
        self.my_x = x
        self.my_y = y
        self.step = pygame.mixer.Sound(sound)
    def run(self):
        pygame.display.set_mode((640, 480))
        screen = pygame.display.get_surface()
    r1 = pygame.Rect(100,100,100,60)
    r2 = pygame.Rect(200,200,50,40)
    rects = [r1,r2]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                break
            if event.type == pygame.KEYDOWN:
                self.step.play(-1)
                if event.key == pygame.K_W:
                    self.my_y = self.my_y - 10
                if event.key == pygame.K_S:
                    self.my_y = self.my_y + 10
                if event.key == pygame.K_A:
                    self.my_x = self.my_x - 10
                if event.key == pygame.K_D:
                    self.my_x = self.my_x + 10

            if event.type == pygame.KEYUP:
                self.step.stop()
            screen.fill((255, 255, 255))  # 255 for white
            pygame.draw.circle(screen, (255, 0, 0), (self.my_x, self.my_y), 30)
            for i in rects:
                pygame.draw.rect(screen, (0,255,0), (i.x,i.y,i.width,i.height))
                pygame.display.update()

def main():
    pygame.init()
    game = TestGame(200,200,'bounce.wav')
    game.run()

if __name__ == '__main__':
    main()