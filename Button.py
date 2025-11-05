import pygame
import config as c
from LoadImage import load_image

class Button:
    def __init__(self, screen, filename: str, center_x: int | float, center_y: int | float, width: int, height: int, layername: str | None, smooth: bool):
        pygame.init()

        self.screen: pygame.Surface = screen

        self.layername = layername
        self.width, self.height = width, height


        self.button_image = load_image(filename, smooth, (self.width, self.height))

        self.center_x, self.center_y = center_x, center_y

    def set_rect(self):
        self.button_rect = self.button_image.get_rect(center=(self.center_x, self.center_y))
        return self.button_rect
    
    def button_predict(self):
        if self.layername != None:
            self.layer_image = pygame.transform.smoothscale(pygame.image.load(self.layername).convert_alpha(), (self.width, self.height))
            self.screen.blit(self.layer_image, (self.button_rect), special_flags=pygame.BLEND_RGBA_MAX)