import pygame
import multiprocessing as mp
import time
import math
import sys

# Глобальная переменная для управления процессом визуализатора
visualizer_process = None

class Button:
    def __init__(self, x, y, width, height, text, color=(100, 100, 200), hover_color=(120, 120, 220)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.font = pygame.font.Font(None, 32)
        self.is_hovered = False
    
    def draw(self, screen):
        # Рисуем кнопку с закругленными углами
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (200, 200, 200), self.rect, 2, border_radius=12)
        
        # Текст кнопки
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.current_color = self.hover_color if self.is_hovered else self.color
        return self.is_hovered
    
    def is_clicked(self, mouse_pos, mouse_click):
        return self.rect.collidepoint(mouse_pos) and mouse_click

def visualizer_window():
    """Процесс для окна визуализации"""
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Audio Visualizer - Close with ESC")
    clock = pygame.time.Clock()
    
    running = True
    start_time = time.time()
    volume_history = []
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Симуляция визуализации
        current_time = time.time() - start_time
        volume = (math.sin(current_time * 5) + 1) / 2
        
        # Добавляем в историю для сглаживания
        volume_history.append(volume)
        if len(volume_history) > 50:
            volume_history.pop(0)
        
        smoothed_volume = sum(volume_history) / len(volume_history)
        
        # Отрисовка
        screen.fill((20, 20, 40))
        
        # Заголовок
        font_large = pygame.font.Font(None, 36)
        title = font_large.render("Audio Visualizer", True, (255, 255, 255))
        screen.blit(title, (150, 20))
        
        # Визуализация громкости - вертикальные бары
        bar_height = volume * 200
        smoothed_height = smoothed_volume * 200
        
        # Текущая громкость
        pygame.draw.rect(screen, (0, 255, 127), 
                        (150, 350 - bar_height, 80, bar_height))
        
        # Сглаженная громкость
        pygame.draw.rect(screen, (64, 224, 208), 
                        (270, 350 - smoothed_height, 80, smoothed_height))
        
        # Волновая форма
        if len(volume_history) >= 2:
            points = []
            for i, vol in enumerate(volume_history):
                x = 50 + (i / (len(volume_history) - 1)) * 400
                y = 350 - (vol * 200)
                points.append((x, y))
            pygame.draw.lines(screen, (255, 105, 180), False, points, 3)
        
        # Текст
        font_small = pygame.font.Font(None, 24)
        current_text = font_small.render(f'Live: {volume:.2f}', True, (255, 255, 255))
        smoothed_text = font_small.render(f'Smoothed: {smoothed_volume:.2f}', True, (255, 255, 255))
        info_text = font_small.render('Press ESC to close', True, (200, 200, 200))
        
        screen.blit(current_text, (145, 360))
        screen.blit(smoothed_text, (265, 360))
        screen.blit(info_text, (180, 380))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

def main_window():
    """Основное окно приложения"""
    global visualizer_process
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Main Application - Audio Player")
    clock = pygame.time.Clock()
    
    # Создаем кнопку
    open_visualizer_btn = Button(300, 200, 200, 60, "Open Visualizer")
    close_visualizer_btn = Button(300, 280, 200, 60, "Close Visualizer", (200, 100, 100), (220, 120, 120))
    
    # Загрузка музыки
    pygame.mixer.init()
    try:
        pygame.mixer.music.load('/Users/DmitryKhramov/Desktop/SoundScope/media/songs/confess your love.mp3')
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
        music_loaded = True
    except:
        print("Музыкальный файл не найден")
        music_loaded = False
    
    running = True
    visualizer_open = False
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP and music_loaded:
                    current_vol = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(min(current_vol + 0.1, 1.0))
                elif event.key == pygame.K_DOWN and music_loaded:
                    current_vol = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(max(current_vol - 0.1, 0.0))
                elif event.key == pygame.K_v:  # Горячая клавиша для визуализатора
                    if not visualizer_open:
                        open_visualizer()
                        visualizer_open = True
                    else:
                        close_visualizer()
                        visualizer_open = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    mouse_click = True
        
        # Проверка наведения на кнопки
        open_visualizer_btn.check_hover(mouse_pos)
        close_visualizer_btn.check_hover(mouse_pos)
        
        # Обработка кликов по кнопкам
        if open_visualizer_btn.is_clicked(mouse_pos, mouse_click) and not visualizer_open:
            open_visualizer()
            visualizer_open = True
        
        if close_visualizer_btn.is_clicked(mouse_pos, mouse_click) and visualizer_open:
            close_visualizer()
            visualizer_open = False
        
        # Отрисовка основного окна
        screen.fill((40, 40, 60))
        
        # Заголовок
        font_large = pygame.font.Font(None, 48)
        title = font_large.render("Audio Player", True, (255, 255, 255))
        screen.blit(title, (280, 50))
        
        # Информация о статусе
        font_medium = pygame.font.Font(None, 36)
        status_text = "Visualizer: OPEN" if visualizer_open else "Visualizer: CLOSED"
        status_color = (100, 255, 100) if visualizer_open else (255, 100, 100)
        status_surface = font_medium.render(status_text, True, status_color)
        screen.blit(status_surface, (320, 120))
        
        # Информация о музыке
        music_status = "Music: Loaded" if music_loaded else "Music: Not Found"
        music_surface = font_medium.render(music_status, True, (200, 200, 200))
        screen.blit(music_surface, (320, 160))
        
        # Кнопки
        open_visualizer_btn.draw(screen)
        close_visualizer_btn.draw(screen)
        
        # Управление
        font_small = pygame.font.Font(None, 28)
        controls = [
            "UP/DOWN: Adjust Volume",
            "V: Toggle Visualizer", 
            "ESC: Exit Program"
        ]
        
        for i, text in enumerate(controls):
            rendered = font_small.render(text, True, (180, 180, 180))
            screen.blit(rendered, (100, 400 + i * 35))
        
        # Текущая громкость
        if music_loaded:
            current_vol = pygame.mixer.music.get_volume()
            vol_text = font_medium.render(f"Volume: {current_vol:.1f}", True, (100, 255, 100))
            screen.blit(vol_text, (350, 500))
        
        pygame.display.flip()
        clock.tick(120)
    
    # Завершение программы
    close_visualizer()
    pygame.quit()

def open_visualizer():
    """Открыть окно визуализатора"""
    global visualizer_process
    if visualizer_process is None or not visualizer_process.is_alive():
        visualizer_process = mp.Process(target=visualizer_window)
        visualizer_process.start()
        print("Visualizer window opened")

def close_visualizer():
    """Закрыть окно визуализатора"""
    global visualizer_process
    if visualizer_process and visualizer_process.is_alive():
        visualizer_process.terminate()
        visualizer_process.join()
        visualizer_process = None
        print("Visualizer window closed")

if __name__ == "__main__":
    try:
        main_window()
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        # Гарантированное закрытие процессов при выходе
        close_visualizer()
        sys.exit()