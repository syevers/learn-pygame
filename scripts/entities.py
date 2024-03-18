import pygame


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type  # entity type
        self.pos = list(pos)  # converts iterable to a list
        self.size = size
        self.velocity = [0, 0]  # used to show represent rate of change in position

    def update(self, movement=(0, 0)):
        # creating vector that represents how much it moves in this frame
        # plus however much the velocity is
        # based on how much we want it to move based on the movement parameter frame passed in
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]  # updating x position
        self.pos[1] += frame_movement[1]  # updating y position

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)
