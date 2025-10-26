import sounddevice as sd
import numpy as np
import threading

class AudioAnalyzer:
    def __init__(self):
        self.volume = 0.0
        self.running = True
        
        # Настройки для захвата аудио
        self.sample_rate = 44100
        self.block_size = 1024
        
        # Запуск захвата аудио
        self.audio_thread = threading.Thread(target=self.capture_audio)
        self.audio_thread.daemon = True
        self.audio_thread.start()
    
    def capture_audio(self):
        """Захват аудио с устройства вывода"""
        def audio_callback(indata, status):
            if status:
                print(status)
            
            # Расчет RMS громкости
            rms = np.sqrt(np.mean(indata**2))
            self.volume = min(rms * 5, 1.0)  # Усиление и ограничение
        
        try:
            with sd.InputStream(callback=audio_callback,
                              channels=2,
                              samplerate=self.sample_rate,
                              blocksize=self.block_size):
                while self.running:
                    sd.sleep(100)
        except Exception as e:
            print(f"Audio capture error: {e}")
    
    def get_volume(self):
        return self.volume
    
    def stop(self):
        self.running = False