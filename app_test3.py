import pygame
import webbrowser
import threading
from flask import Flask, render_template, request

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'home', self.home)

    def home(self):
        return render_template('index.html')

    def run(self):
        self.app.run(debug=False)



class PygameApp:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()

        self.flask_app = FlaskApp()

        # Установка размеров окна
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Open HTML Page Example")

        # Определение цветов
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)

        # Определение шрифта
        self.font = pygame.font.Font(None, 36)

        # Определение кнопки
        self.button_rect = pygame.Rect(300, 250, 200, 50)
        self.button_text = self.font.render("Open HTML Page", True, self.WHITE)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Проверка нажатия кнопки мыши
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.button_rect.collidepoint(event.pos):
                        self.flask_app.run()
                        webbrowser.open('http://127.0.0.1:5000/')  # URL вашего Flask-приложения

            # Отрисовка фона и кнопки
            self.screen.fill(self.BLUE)
            pygame.draw.rect(self.screen, (0, 128, 255), self.button_rect)
            self.screen.blit(self.button_text, (self.button_rect.x + 10, self.button_rect.y + 10))

            # Обновление экрана
            pygame.display.flip()

        # Завершение работы Pygame
        pygame.quit()

def main():
    flask_app = FlaskApp()
    flask_thread = threading.Thread(target=flask_app.run)
    flask_thread.start()

    pygame_app = PygameApp()
    pygame_app.run()

    # После выхода из Pygame отправляем запрос на завершение Flask-сервера
    requests.post('http://127.0.0.1:5000/shutdown')

if __name__ == '__main__':
    main()