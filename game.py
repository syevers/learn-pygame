import pygame
import sys

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ninja game')

        # creates the window
        self.screen = pygame.display.set_mode((640, 480))

        # render onto the display and scale it up
        self.display = pygame.Surface((320, 240))

        # restrict framerate to 60fps
        self.clock = pygame.time.Clock()


        self.movement = [False, False]

        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)

    def run(self):
        while True:
            # need to clear screen after each frame
            self.display.fill((14, 219, 248))
            self.tilemap.render(self.display)

            # 0 on y-axis bc platformers only go right/left not up/down
            self.player.update((self.movement[1] - self.movement[0], 0))

            self.player.render(self.display)
            print(self.tilemap.tiles_around(self.player.pos))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # gets user input
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

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()
