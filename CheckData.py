import pygame
import config as c
import Data, Button, GetFilePath

class CheckData:
    def __init__(self, screen: pygame.Surface, bpm: float, ac_bpm: float, key: str, scale: str, strength: int) -> None:
        pygame.init()

        self.oGetFilePath = GetFilePath.GetFilePath()

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.Height = c.Height

        self.data_font = c.TTC_regular_menu

        self.song_data = {
            'bpm': int(bpm),
            'ac_bpm': ac_bpm,
            'key': key,
            'scale': scale,
            'strength': strength
        }

        self.strength_text_color = None
        if self.song_data['strength'] >= 80:
            self.strength_text_color = c.SS_CDGREEN
        elif 60 <= self.song_data['strength'] < 80:
            self.strength_text_color = c.SS_CDYELLOW
        elif 40 <= self.song_data['strength'] < 60:
            self.strength_text_color = c.SS_CDORANGE
        elif self.song_data['strength'] < 40:
            self.strength_text_color = c.SS_CDRED

        self.cd_glow_1 = pygame.transform.smoothscale(pygame.image.load(c.cd_glow_1).convert_alpha(), (self.width*0.6, self.Height))
        self.cd_glow_2 = pygame.transform.smoothscale(pygame.image.load(c.cd_glow_2).convert_alpha(), (self.width*0.4, self.Height))

        self.cover = pygame.transform.smoothscale(pygame.image.load(self.oGetFilePath.load_file('songs', 'temp_cover.jpg')).convert_alpha(), (self.Height, self.Height))

        self.bpm_text_2 = self.data_font.render(f' {self.song_data['bpm']} BPM', c.smooth, c.SS_WHITE)
        self.ac_bpm_text_2 = self.data_font.render(f' {self.song_data['ac_bpm']} BPM', c.smooth, c.SS_WHITE)
        self.key_text_2 = self.data_font.render(f' {self.song_data['key']} {self.song_data['scale']}', c.smooth, c.SS_WHITE)
        self.strength_text_2 = self.data_font.render(f' {self.song_data['strength']}%', c.smooth, self.strength_text_color)

        self.music_data_text_rect = c.music_data_text.get_rect(topleft=(self.width//25, self.height//16))
        self.bpm_text_rect = c.bpm_text.get_rect(topleft=(self.width//25, self.height//16 + self.height//11))
        self.ac_bpm_text_rect = c.ac_bpm_text.get_rect(topleft=(self.width//25, self.height//16 + self.height//11*2))
        self.key_text_rect = c.key_text.get_rect(topleft=(self.width//25, self.height//16 + self.height//11*3))
        self.strength_text_rect = c.strength_text.get_rect(topleft=(self.width//25, self.height//16 + self.height//11*4))

        self.bpm_text_2_rect = self.bpm_text_2.get_rect(topleft=(self.bpm_text_rect.topright))
        self.ac_bpm_text_2_rect = self.ac_bpm_text_2.get_rect(topleft=(self.ac_bpm_text_rect.topright))
        self.key_text_2_rect = self.key_text_2.get_rect(topleft=(self.key_text_rect.topright))
        self.strength_text_2_rect = self.strength_text_2.get_rect(topleft=(self.strength_text_rect.topright))


    def draw(self):
        self.screen.fill((13, 14, 15))
        self.screen.blit(self.cd_glow_1, (0, 0))
        self.screen.blit(self.cover, (self.width*0.6, 0))
        self.screen.blit(self.cd_glow_2, (self.width*0.6, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(c.music_data_text, self.music_data_text_rect)
        self.screen.blit(c.bpm_text, self.bpm_text_rect)
        self.screen.blit(c.ac_bpm_text, self.ac_bpm_text_rect)
        self.screen.blit(c.key_text, self.key_text_rect)
        self.screen.blit(c.strength_text, self.strength_text_rect)
        self.screen.blit(self.bpm_text_2, self.bpm_text_2_rect)
        self.screen.blit(self.ac_bpm_text_2, self.ac_bpm_text_2_rect)
        self.screen.blit(self.key_text_2, self.key_text_2_rect)
        self.screen.blit(self.strength_text_2, self.strength_text_2_rect)
        

    def __del__(self):
        pass