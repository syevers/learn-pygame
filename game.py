import sys
import pygame

from scripts.utils import load_image
from scripts.entities import PhysicsEntity


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ninja game')

        # creates the window
        self.screen = pygame.display.set_mode((640, 480))

        # restrict framerate to 60fps
        self.clock = pygame.time.Clock()

        # demonstration stuff
        # self.img = pygame.image.load('./data/images/clouds/cloud_1.png')
        #  set specific color (black) to be transparent
        # self.img.set_colorkey((0, 0, 0))
        #
        # self.img_pos = [160, 260]
        #
        #  collision detection
        # self.collision_area = pygame.Rect(50, 50, 300, 50)

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        while True:
            # need to clear screen after each frame
            self.screen.fill((14, 219, 248))
            # 0 on y-axis bc platformers only go right/left not up/down
            self.player.update((self.movement[1] - self.movement[0], 0))
            # MORE DEMONSTRATION CODE USEFUL TO KNOW -- KEEPING IT
            # render image
            # img_r = pygame.Rect(*self.img_pos, *self.img.get_size())
            #  IF COLLISION -> BLUE COLOR CHANGES TO LIGHTER BLUE
            #
            #  TODO: IN PROJECT CODE: MAKE SEPERATE FUNCTION FOR COLLISION AND RENDER
            # if img_r.colliderect(self.collision_area):
            #     pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            # else:
            #
            # pygame.draw.rect(self.screen, (0, 50, 255), self.collision_area)
            # true gets converted to 1 and false gets converted to 0
            # self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            # self.screen.blit(self.img, self.img_pos)

            # gets user input

            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # key was pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  # down key
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:  # down key
                        self.movement[1] = True

                # key is no longer pressed
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()
