import os, shutil
import GetFilePath

def copy_audio_file(filename: str):
    """Функция для копирования аудио файла"""
    
    oGetFilePath = GetFilePath.GetFilePath()

    source_file = filename
    
    destination_folder = oGetFilePath.load_folder('songs')
    
    home_dir = os.path.expanduser("~")
    destination_folder = os.path.join(home_dir, destination_folder)

    try:
        os.makedirs(destination_folder, exist_ok=True)
        
        file_name = os.path.basename(source_file)
        
        destination_file = os.path.join(destination_folder, file_name)
        
        shutil.copy2(source_file, destination_file)
        
        return True
        
    except FileNotFoundError:
        error_msg = f"Исходный файл не найден: {source_file}"
        print(error_msg)
        return False
    except PermissionError:
        error_msg = "Ошибка доступа к файлу"
        print(error_msg)
        return False
    except Exception as e:
        error_msg = f"Ошибка при копировании: {str(e)}"
        print(error_msg)
        return False