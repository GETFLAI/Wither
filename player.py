import pygame
from globals import *


class Player(pygame.sprite.Sprite):  # класс игрока
    def __init__(self, groups, image=pygame.Surface((TILESIZE * 2, TILESIZE * 3)), position=(size_screen)):
        super().__init__(groups)
        self.image = image
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=position)

    def input(self):  # обработка нажатия
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # влево
            self.rect.x -= 1

        if keys[pygame.K_d]:  # вправо
            self.rect.x += 1

    def update(self):  # обновление движение
        self.input()
