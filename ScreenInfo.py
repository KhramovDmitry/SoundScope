import pygame

class ScreenInfo:
    def __init__(self):
        pygame.init()

    def get_info(self):
        """
        Метод получает информацию о размерах окна пользователя.

        :return: Длина и ширина экрана пользователя.
        """

        self.info_object = pygame.display.Info()
        self.width, self.height = self.info_object.current_w, self.info_object.current_h

        return self.width, self.height