import pygame

def load_image(file_path: str, smooth: bool, size: tuple[int, int]) -> pygame.Surface:

    if smooth:
        image = pygame.transform.smoothscale(pygame.image.load(file_path), size)
    else:
        image = pygame.transform.scale(pygame.image.load(file_path), size)

    return image