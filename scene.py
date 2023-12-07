import pygame
from globals import *
from sprite import Entity
from player import Player


class Scene:  # класс сцены
    def __init__(self, app):
        self.app = app  # приложение

        self.sprites = pygame.sprite.Group()  # группа спрайтов
        self.entity = Entity([self.sprites])  # назначение переменной класс
        Entity([self.sprites], position=(100, 100))  # назначение движения
        Entity([self.sprites], position=(200, 200))

        self.player = Player([self.sprites])  # переменная класа Player

    def update(self):  # обновление спрайтов
        self.sprites.update()

    def draw(self):  # рисование
        self.app.screen.fill("lightblue")  # фон
        self.sprites.draw(self.app.screen)  # рисование спрайтов
