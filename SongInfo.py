import essentia
from essentia.standard import MonoLoader, RhythmExtractor2013, KeyExtractor

class SongInfo:
    def __init__(self, file):
        self.audio = MonoLoader(filename=file)()

    def get_tempo(self, accuracy_flag: bool) -> int | float:
        """
        Метод получает информацию о темпе трека.

        :param accuracy_flag: Булевая переменная, отвечающая за точность темпа BPM.

        :return: Показатель темпа в BPM.
        """
        self.rhythm_extractor = RhythmExtractor2013()
        self.bpm, _, _, _, _ = self.rhythm_extractor(self.audio)
        if accuracy_flag:
            return round(self.bpm, 3)
        else:
            return round(self.bpm, 0)
    
    def get_key(self, option):
        """
        Метод получающий тональность, окраску лада и силу (активность) трека.

        :param option: Опция(-ии), которую возвратит метод: 'key', 'scale', 'strength' или 'all'.

        :return: Данные, которые выбрали опцией.
        """
        self.key_extractor = KeyExtractor()
        self.key, self.scale, self.strength = self.key_extractor(self.audio)
        if option == "key":
            return self.key
        elif option == "scale":
            return self.scale
        elif option == "strength":
            return int(round(self.strength, 2)*100)
        elif option == "all":
            return [self.key, self.scale, int(round(self.strength, 2)*100)]