import os

class GetFilePath:
    def __init__(self):

        self.current_path = os.path.dirname(__file__)

    def load_file(self, foldername: str, filename: str) -> str:
        """
        Метод находит точный путь к файлу.

        :param foldername: Название папки в папке 'media', в которой лежит нужный нам файл.
        :param filename: Название нужного вам файла.

        :return: Точный путь к файлу 'filename'.
        """
        self.file_path = os.path.join(self.current_path, 'media', foldername, filename)

        return self.file_path
    
    def load_datafile(self, filename: str) -> str:
        """
        Метод находит точный путь к json-файлу.

        :param filename: Название нужного вам файла.

        :return: Точный путь к файлу 'filename'.
        """
        self.file_path = os.path.join(self.current_path, 'data', filename)

        return self.file_path
    
    def load_htmlfile(self, filename: str) -> str:
        """
        Метод находит точный путь к html-файлу.

        :param filename: Название нужного вам файла.

        :return: Точный путь к файлу 'filename'.
        """
        self.file_path = os.path.join(self.current_path, 'templates', filename)

        return self.file_path