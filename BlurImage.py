from PIL import Image, ImageFilter
import pygame

def blur_image_with_pillow(image_path, blur_radius=7):
    pil_image = Image.open(image_path)
    
    blurred_pil = pil_image.filter(ImageFilter.GaussianBlur(blur_radius))
    
    mode = blurred_pil.mode
    size = blurred_pil.size
    data = blurred_pil.tobytes()
    
    return pygame.image.fromstring(data, size, mode)