import pygame
import os
import GetFilePath

class ConfigWindow:
    def __init__(self):
        pygame.init()

        self.oGetFilePath = GetFilePath.GetFilePath()
        self.icon = pygame.image.load(self.oGetFilePath.load_file('sprites', 'SS_icon.png'))

    def configure_window(self):
        pygame.display.set_caption('SoundScope')
        pygame.display.set_icon(self.icon)