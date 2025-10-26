import os

# Временно переименовываем конфликтующую библиотеку в essentia
essentia_lib_path = "/Users/DmitryKhramov/Desktop/SoundScope/.venv/lib/python3.13/site-packages/essentia/.dylibs/libSDL2-2.0.0.dylib"
backup_path = "/Users/DmitryKhramov/Desktop/SoundScope/.venv/lib/python3.13/site-packages/essentia/.dylibs/libSDL2-2.0.0.dylib.backup"

if os.path.exists(essentia_lib_path):
    #os.rename(essentia_lib_path, backup_path)
    print("Temporarily disabled essentia's SDL2 library")

try:
    import essentia
    import pygame
    # ... ваш код
finally:
    # Восстанавливаем обратно после завершения
    if os.path.exists(backup_path):
        #os.rename(backup_path, essentia_lib_path)
        print("Restored essentia's SDL2 library")

"""
cd /Users/DmitryKhramov/Desktop/SoundScope
DYLD_LIBRARY_PATH="/Users/DmitryKhramov/Desktop/SoundScope/.venv/lib/python3.13/site-packages/pygame/.dylibs" python3 app_test3.py
"""