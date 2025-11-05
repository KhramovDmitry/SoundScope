import pygame
import sounddevice as sd
import numpy as np
import threading

class AudioAnalyzer:
    def __init__(self):
        self.volume = 0.0
        self.running = True
        
        # Получаем список аудиоустройств
        devices = sd.query_devices()
        print("Доступные аудиоустройства:")
        for i, device in enumerate(devices):
            print(f"{i}: {device['name']} (in: {device['max_input_channels']}, out: {device['max_output_channels']})")
        
        # Выбираем виртуальное устройство для захвата вывода (зависит от системы)
        # На Windows: "Stereo Mix", "What U Hear"
        # На macOS: "BlackHole", "SoundFlower", "Loopback"
        # На Linux: "pulse" или "default"
        
        self.device_id, self.channels = self._find_output_device()
        
        if self.device_id is None:
            print("Не найдено подходящее устройство для захвата вывода. Использую default.")
            self.device_id = None
        
        self.audio_thread = threading.Thread(target=self.capture_audio)
        self.audio_thread.daemon = True
        self.audio_thread.start()
    
    def _find_output_device(self):
        """Найти устройство для захвата аудиовыхода"""
        devices = sd.query_devices()
        
        # Ищем устройства с возможностью захвата вывода
        for i, device in enumerate(devices):
            # Устройство должно иметь входные каналы и быть устройством вывода
            if device['max_input_channels'] > 0 and device['max_output_channels'] == 0 and 'MacBook' in device['name']:
                print(f"Найдено устройство для захвата: {i} - {device['name']}")
                return 1, 1
        
        return None
    
    def capture_audio(self):
        def audio_callback(indata, frames, time, status):
            if status:
                print(f"Audio status: {status}")
            
            # Расчет громкости только если есть данные
            if indata.any():
                rms = np.sqrt(np.mean(indata**2))
                self.volume = min(rms * 10, 1.0)  # Усиление может потребовать настройки
        
        #print(channels)
        try:
            with sd.InputStream(callback=audio_callback,
                              channels=1,
                              samplerate=44100,
                              blocksize=1024,
                              device=self.device_id):  # Указываем конкретное устройство
                while self.running:
                    sd.sleep(100)
        except Exception as e:
            print(f"Audio capture error: {e}")
    
    def get_volume(self):
        return self.volume
    
    def stop(self):
        self.running = False

class SoundDeviceVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 1100))
        self.clock = pygame.time.Clock()
        
        # Инициализация анализатора
        self.analyzer = AudioAnalyzer()

        pygame.mixer.init(frequency=44100, size=-16, channels=self.analyzer.channels)
        
        # Загрузка и воспроизведение музыки
        pygame.mixer.music.load('/Users/DmitryKhramov/Desktop/SoundScope/media/songs/confess your love.mp3')
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
        
    def run(self):
        running = True
        volumes_history = []  # История громкости для сглаживания
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.analyzer.stop()
                    running = False
            
            # Получаем текущую громкость
            current_volume = self.analyzer.get_volume()
            
            # Добавляем в историю для сглаживания
            volumes_history.append(current_volume)
            if len(volumes_history) > 10:  # Храним последние 10 значений
                volumes_history.pop(0)
            
            # Сглаженная громкость (среднее за последние кадры)
            smoothed_volume = np.mean(volumes_history)
            
            # Отрисовка
            self.screen.fill((0, 0, 0))
            
            # Визуализация громкости - вертикальная линия
            line_height = int(smoothed_volume * 900)
            line_x = 400
            line_y = 1000 - line_height
            
            # Цвет меняется от зеленого к красному в зависимости от громкости
            color = (int(float(smoothed_volume) * 255), int((1 - float(smoothed_volume)) * 255), 100)
            
            pygame.draw.line(self.screen, color, 
                           (line_x, 1000), (line_x, line_y), 20)
            
            # Отображение численного значения
            font = pygame.font.Font(None, 36)
            text = font.render(f'Volume: {smoothed_volume:.3f}', True, (255, 255, 255))
            self.screen.blit(text, (50, 50))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    app = SoundDeviceVisualizer()
    app.run()