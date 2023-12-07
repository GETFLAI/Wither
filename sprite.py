import pygame
from globals import *


class Entity(pygame.sprite.Sprite):  # класс движения
    def __init__(self, groups, image=pygame.Surface((TILESIZE, TILESIZE)), position=(0, 0)):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

    def update(self): # движение
        self.rect.x += 1
