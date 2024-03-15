import sys
import pygame



class Game:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption('ninja game')
        # creates the window
        self.screen = pygame.display.set_mode((640,480))

        #restrict framerate to 60fps
        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('./data/images/clouds/cloud_1.png')

        self.img_pos = [160,260]

    def run(self):
        while True:
            self.screen.blit(self.img, self.img_pos)
            # gets user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)

Game().run()
