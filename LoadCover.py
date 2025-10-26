'''
import os
from mutagen import File
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, APIC  # Для MP3
import config as c

def extract_cover_image(audio_file_path):
    """
    Извлекает обложку альбома из аудиофайла и сохраняет её во временный файл.
    Возвращает путь к временному файлу с изображением или None, если обложка не найдена.
    """
    try:
        audio = File(audio_file_path)
        
        if audio is None:
            print("Файл не распознан mutagen.")
            return None

        if audio_file_path.lower().endswith('.mp3'):
            if 'APIC:' in audio.tags:
                cover_art = audio.tags['APIC:'].data
            else:
                audio_id3 = ID3(audio_file_path)
                for tag in audio_id3.values():
                    if isinstance(tag, APIC):
                        cover_art = tag.data
                        break
                else:
                    return None
        
        elif audio_file_path.lower().endswith('.flac'):
            if 'pictures' in audio.tags and len(audio.tags.pictures) > 0:
                cover_art = audio.tags.pictures[0].data
            else:
                return None
        
        elif audio_file_path.lower().endswith(('.wav', '.wave')):
            print("WAV файлы обычно не содержат обложек в метаданных.")
            return None
        
        else:
            print(f"Формат файла не поддерживается для извлечения обложки: {audio_file_path}")
            return None

        songs_folder = "media/songs"
        if not os.path.exists(songs_folder):
            os.makedirs(songs_folder)
        
        temp_image_path = os.path.join(songs_folder, "temp_cover.jpg")
        with open(temp_image_path, 'wb') as img_file:
            img_file.write(cover_art)
        
        return temp_image_path

    except Exception as e:
        print(f"Ошибка при извлечении обложки: {e}")
        return None
'''

import os
from mutagen import File
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, APIC  # Для MP3
import config as c
import shutil

def extract_cover_image(audio_file_path):
    """
    Извлекает обложку альбома из аудиофайла и сохраняет её во временный файл.
    Возвращает путь к временному файлу с изображением или использует стандартную обложку при ошибке.
    """
    try:
        audio = File(audio_file_path)
        
        if audio is None:
            print("Файл не распознан mutagen.")
            return use_error_cover()

        if audio_file_path.lower().endswith('.mp3'):
            if 'APIC:' in audio.tags:
                cover_art = audio.tags['APIC:'].data
            else:
                audio_id3 = ID3(audio_file_path)
                for tag in audio_id3.values():
                    if isinstance(tag, APIC):
                        cover_art = tag.data
                        break
                else:
                    return use_error_cover()
        
        elif audio_file_path.lower().endswith('.flac'):
            if 'pictures' in audio.tags and len(audio.tags.pictures) > 0:
                cover_art = audio.tags.pictures[0].data
            else:
                return use_error_cover()
        
        elif audio_file_path.lower().endswith(('.wav', '.wave')):
            print("WAV файлы обычно не содержат обложек в метаданных.")
            return use_error_cover()
        
        else:
            print(f"Формат файла не поддерживается для извлечения обложки: {audio_file_path}")
            return use_error_cover()

        songs_folder = "media/songs"
        if not os.path.exists(songs_folder):
            os.makedirs(songs_folder)
        
        temp_image_path = os.path.join(songs_folder, "temp_cover.jpg")
        with open(temp_image_path, 'wb') as img_file:
            img_file.write(cover_art)
        
        return temp_image_path

    except Exception as e:
        print(f"Ошибка при извлечении обложки: {e}")
        return use_error_cover()

def use_error_cover():
    """
    Копирует стандартное изображение ошибки в папку песен как temp_cover.jpg
    Возвращает путь к скопированному файлу
    """
    try:
        error_cover_path = "media/sprites/error_cover.png"
        songs_folder = "media/songs"
        temp_image_path = os.path.join(songs_folder, "temp_cover.jpg")
        
        # Создаем папку, если она не существует
        if not os.path.exists(songs_folder):
            os.makedirs(songs_folder)
        
        # Копируем файл error_cover.png как temp_cover.jpg
        shutil.copy2(error_cover_path, temp_image_path)
        print(f"Используется стандартная обложка: {error_cover_path}")
        
        return temp_image_path
        
    except Exception as e:
        print(f"Ошибка при копировании стандартной обложки: {e}")
        return None