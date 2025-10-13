import pygame
import sys
from Cocoa import NSOpenPanel, NSApplication, NSApp

# Инициализация Pygame
pygame.init()

# Создание окна Pygame
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Выбор файла в Pygame")

# Переменная для хранения пути к выбранному файлу
selected_file_path = ""

def choose_file():
    global selected_file_path

    # Создаем панель выбора файла
    panel = NSOpenPanel.openPanel()
    panel.setAllowsMultipleSelection_(False)  # Не разрешать множественный выбор
    panel.setCanChooseDirectories_(False)  # Не разрешать выбор директорий
    panel.setCanChooseFiles_(True)  # Разрешить выбор файлов

    # Отображаем панель и ждем выбора файла
    if panel.runModal() == 1:  # 1 означает, что пользователь нажал "Открыть"
        selected_file_path = panel.URLs()[0].path()  # Получаем путь к выбранному файлу
        print("Выбранный файл:", selected_file_path)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Если нажата пробел
                choose_file()  # Вызываем функцию выбора файла

    # Обновление экрана
    screen.fill((25, 25, 25))  # Заливаем экран белым цветом
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()