import pygame
import sys
from globals import *
from scene import Scene


class Game:  # Основной класс игры
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size_screen)  # экран
        self.clock = pygame.time.Clock()  # время

        self.running = True  # работает

        self.scene = Scene(self)

    def run(self):  # начать работу
        while self.running:  # пока работает
            self.update()  # ФЯ обновлять
            self.draw()  # ФЯ рисовать
        self.close()  # ФЯ закрыть когда не работает

    def update(self):  # обновление
        while pygame.event.wait().type != pygame.QUIT:  # ожидание выхода
            self.running = False  # не работает

        self.scene.update()  # обновление сцены

        pygame.display.update()  # обновление экрана
        self.clock.tick(FPS)  # частота кадров

    def draw(self):  # рисование
        self.scene.draw()

    def close(self):  # закрытие
        pygame.quit()  # выход
        sys.exit()  # закрытие чтения ввода


if __name__ == "__name__":  # основной блок работы программы
    game = Game()  # присваивание класса
    game.run()  # начало работы
