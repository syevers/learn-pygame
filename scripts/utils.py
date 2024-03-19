import pygame
import os

BASE_IMG_PATH = 'data/images/'


def load_image(path):
    # optimizes image when loading
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


# loading multiple images at once
def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

