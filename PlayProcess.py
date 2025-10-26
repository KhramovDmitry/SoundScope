import pygame
import multiprocessing as mp
import time
import math
import sys
import config as c
from BlurImage import blur_image_with_pillow
import GetFilePath, Data, Button

class PlayProcess:
    def run(self):
        pygame.init()
        pygame.mixer.init()

        self.oData = Data.Data()
        self.songs_data = self.oData.load_data('songs.json')

        self.songs = self.songs_data['songs_names']
        self.songs_names = []
        for song in self.songs:
            song: str
            self.song_name = song.split('/')
            self.song_name = self.song_name[-1]
            self.song_name = self.song_name.split('.')
            self.song_name = self.song_name[0]
            try:
                self.song = pygame.mixer.music.load(song)
                pygame.mixer.music.set_volume(0.7)
            except Exception as e:
                print(f'ERROR: {e}')

        self.width, self.height = c.true_width//9.87, c.true_height//3.44
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        if len(self.songs) == 1:
            pygame.display.set_caption(f'{self.song_name}')

        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.running = True

        self.button_state = 'play'

        self.oGetFilePath = GetFilePath.GetFilePath()

        self.pbx, self.pby = self.width//2, self.height//2 + self.height//8
        self.pb_width, self.pb_height = self.height//10, self.height//10

        if c.smooth:
            self.album_image = pygame.transform.smoothscale(pygame.image.load(self.oGetFilePath.load_file('songs', 'temp_cover.jpg')).convert_alpha(), (self.width - self.width//12, self.width - self.width//12))
        else:
            self.album_image = pygame.transform.scale(pygame.image.load(self.oGetFilePath.load_file('songs', 'temp_cover.jpg')).convert_alpha(), (self.width - self.width//12, self.width - self.width//12))

        self.blurred_image = blur_image_with_pillow(self.oGetFilePath.load_file('songs', 'temp_cover.jpg')).convert_alpha()
        self.blurred_image = pygame.transform.smoothscale(self.blurred_image, (self.width*2, self.width*2))

        self.frame_glow = pygame.transform.scale(pygame.image.load(c.glow_1).convert_alpha(), (self.width - self.width//12 + self.width//1.5, self.width - self.width//12 + self.width//1.5))
        
        self.song_frame = pygame.transform.scale(pygame.image.load(c.song_frame).convert_alpha(), (self.width - self.width//12 + self.width//58, self.width - self.width//12 + self.width//58))
        
        self.album_image_rect = self.album_image.get_rect(center=(self.width//2, self.width//2))
        self.song_frame_rect = self.song_frame.get_rect(center=(self.width//2, self.width//2))
        self.frame_glow_rect = self.frame_glow.get_rect(center=(self.width//2, self.width//2 + self.width//11))
        self.blurred_image_rect = self.blurred_image.get_rect(center=(self.width//2, self.height//2))

        pygame.mixer.music.play(-1)

        self.play_button = Button.Button(self.screen, c.pause_button, 
                                         self.pbx, self.pby, self.pb_width, self.pb_height, None, c.smooth)
        self.play_button_rect = self.play_button.set_rect()
        self.play_button_glow = pygame.transform.scale(pygame.image.load(c.glow_2).convert_alpha(), (self.height//8, self.height//8))
        #self.play_button_glow = pygame.transform.scale(pygame.image.load(c.glow_1).convert_alpha(), (self.height//5.6, self.height//5.6))
        self.play_button_glow_rect = self.play_button_glow.get_rect(center=(self.width//2, self.height//2 + self.height//7.6))

        while self.running:
            self.mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.play_button_rect.collidepoint(self.mouse_pos):
                        if self.button_state == 'play':
                            pygame.mixer.music.pause()
                            if c.smooth:
                                self.play_button.button_image = pygame.transform.smoothscale(pygame.image.load(c.play_button).convert_alpha(), (self.pb_width, self.pb_height))
                            else:
                                self.play_button.button_image = pygame.transform.scale(pygame.image.load(c.play_button).convert_alpha(), (self.pb_width, self.pb_height))
                            self.button_state = 'pause'
                        elif self.button_state == 'pause':
                            pygame.mixer.music.unpause()
                            if c.smooth:
                                self.play_button.button_image = self.play_button.button_image = pygame.transform.smoothscale(pygame.image.load(c.pause_button).convert_alpha(), (self.pb_width, self.pb_height))
                            else:
                                self.play_button.button_image = self.play_button.button_image = pygame.transform.scale(pygame.image.load(c.pause_button).convert_alpha(), (self.pb_width, self.pb_height))
                            self.button_state = 'play'
                    

            self.screen.blit(self.blurred_image, (self.blurred_image_rect))
            self.screen.blit(self.frame_glow, (self.frame_glow_rect), special_flags=pygame.BLEND_RGBA_MULT)
            self.screen.blit(self.song_frame, (self.song_frame_rect), special_flags=pygame.BLEND_RGBA_ADD)
            self.screen.blit(self.album_image, (self.album_image_rect))
            self.screen.blit(self.play_button_glow, (self.play_button_glow_rect), special_flags=pygame.BLEND_RGBA_MULT)
            self.screen.blit(self.play_button.button_image, (self.play_button_rect), special_flags=pygame.BLEND_RGBA_ADD)

            pygame.display.flip()
            self.clock.tick(self.FPS)
    
        pygame.quit()