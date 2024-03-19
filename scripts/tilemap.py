import pygame

# all permutations of (-1 through 1)
NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}


class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # create tiles
        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

    # COLLISION DETECTION
    def tiles_around(self, pos):
        tiles = []
        # convert pixel position to grid position
        # // is integer division to chop off the remainder
        # (x,y) axis
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            # generate all pixels around pos
            # then adding neighbor_offset numbers base location to get 9 tiles in that area
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            # check if tile exists
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    # convert all tiles that have physics to pygame.rect()
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            # if in physics_tiles then we know it's something we can collide with
            if tile['type'] in PHYSICS_TILES:
                rects.append(
                    pygame.Rect(
                        tile['pos'][0] * self.tile_size,  # x pos
                        tile[pos][1] * self.tile_size,    # y pos
                        self.tile_size, self.tile_size)   #
                )

    def render(self, surf):
        # want offgrid tiles to be rendered in the back
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tilemap:
            # look up location in tilemap
            tile = self.tilemap[loc]
            surf.blit(
                self.game.assets[tile['type']][tile['variant']],
                (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size)
            )
