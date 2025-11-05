import pygame, GetFilePath
import shutil
import os
import sys

# Инициализация Pygame
pygame.init()

oGetFilePath = GetFilePath.GetFilePath()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SoundScope")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 150, 255)

# Шрифт
font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = GRAY
        self.hover_color = (180, 180, 180)
        self.current_color = self.color
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.current_color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)
    
    def update(self, pos):
        if self.is_hovered(pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

def copy_audio_file():
    """Функция для копирования аудио файла"""
    
    # Путь к исходному файлу (замените на ваш путь)
    source_file = "/Users/DmitryKhramov/Documents/From The Start.mp3"
    
    # Путь к папке назначения
    destination_folder = oGetFilePath.load_folder('SoundScope')
    
    # Для MacOS лучше использовать абсолютный путь в домашней директории
    home_dir = os.path.expanduser("~")
    destination_folder = os.path.join(home_dir, destination_folder)
    
    try:
        # Создаем папку, если она не существует
        os.makedirs(destination_folder, exist_ok=True)
        
        # Получаем имя файла из пути
        file_name = os.path.basename(source_file)
        
        # Полный путь к файлу назначения
        destination_file = os.path.join(destination_folder, file_name)
        
        # Копируем файл
        shutil.copy2(source_file, destination_file)
        
        print(f"✅ Файл успешно скопирован в: {destination_file}")
        return True, f"Файл скопирован: {file_name}"
        
    except FileNotFoundError:
        error_msg = f"❌ Исходный файл не найден: {source_file}"
        print(error_msg)
        return False, error_msg
    except PermissionError:
        error_msg = "❌ Ошибка доступа к файлу"
        print(error_msg)
        return False, error_msg
    except Exception as e:
        error_msg = f"❌ Ошибка при копировании: {str(e)}"
        print(error_msg)
        return False, error_msg

# Создаем кнопку
copy_button = Button(300, 250, 200, 50, "Копировать файл")

# Переменная для сообщения
message = ""
message_color = BLACK

# Главный цикл
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if copy_button.is_hovered(mouse_pos):
                success, msg = copy_audio_file()
                message = msg
                message_color = BLUE if success else (255, 0, 0)
    
    # Обновляем кнопку
    copy_button.update(mouse_pos)
    
    # Отрисовка
    screen.fill(WHITE)
    copy_button.draw(screen)
    
    # Отображаем сообщение
    if message:
        msg_surf = font.render(message, True, message_color)
        screen.blit(msg_surf, (50, 350))
    
    pygame.display.flip()

pygame.quit()
sys.exit()