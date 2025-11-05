import pygame
import Button
from LoadCover import extract_cover_image
from CopyFile import copy_audio_file
import ChooseFile, SongInfo, GetFilePath, LoadImage
import config as c

class LoadFile:
    def __init__(self, screen):
        pygame.init()

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.Height = c.Height

        self.oChooseFile = ChooseFile.ChooseFile()
        self.oGetFilePath = GetFilePath.GetFilePath()

        self.state = 'before'
        self.audio_path = None
        self.bpm = None

        self.possible_extensions = ['.mp3', '.MP3', '.waw', '.WAW']
        self.eb_width, self.eb_height = c.mb2_size

        self.bg = pygame.transform.smoothscale(pygame.image.load(c.menu_bg).convert_alpha(), (self.width, self.Height))
        self.black_layer = pygame.transform.smoothscale(pygame.image.load(c.black_layer).convert_alpha(), (self.width, self.Height))
        self.black_layer.set_alpha(150)

        self.cover = LoadImage.load_image(self.oGetFilePath.load_file('sprites', 'error_cover.png'), c.smooth, (self.Height//2.5, self.Height//2.5))
        self.cover_pos = self.cover.get_rect(center=(self.width//2, self.Height//2 - self.Height//4))

        self.choose_file_button = Button.Button(screen=self.screen,
                                              filename=c.choose_file_button,
                                              center_x=c.cfb_x, center_y=c.cfb_y,
                                              width=c.cfb_width, height=c.cfb_height,
                                              layername=c.choose_file_layer, smooth=c.smooth)
        self.choose_file_button_rect = self.choose_file_button.set_rect()
        self.play_button = Button.Button(screen=self.screen,
                                              filename=c.cover_layer,
                                              center_x=self.width//2, center_y=self.Height//2 - self.Height//4,
                                              width=self.Height//2.5, height=self.Height//2.5,
                                              layername=c.cover_layer, smooth=c.smooth)
        self.play_button_rect = self.play_button.set_rect()
        self.add_song_button = Button.Button(screen=self.screen,
                                              filename=c.add_song_button,
                                              center_x=c.fb1_pos[0], center_y=c.fb1_pos[1],
                                              width=c.file_button_size[0], height=c.file_button_size[1],
                                              layername=c.file_button_layer, smooth=c.smooth)
        self.add_song_button_rect = self.add_song_button.set_rect()
        self.check_data_button = Button.Button(screen=self.screen,
                                              filename=c.check_data_button,
                                              center_x=c.fb2_pos[0], center_y=c.fb2_pos[1],
                                              width=c.file_button_size[0], height=c.file_button_size[1],
                                              layername=c.file_button_layer, smooth=c.smooth)
        self.check_data_button_rect = self.check_data_button.set_rect()
        self.listen_file_button = Button.Button(screen=self.screen,
                                              filename=c.listen_file_button,
                                              center_x=c.fb3_pos[0], center_y=c.fb3_pos[1],
                                              width=c.file_button_size[0], height=c.file_button_size[1],
                                              layername=c.file_button_layer, smooth=c.smooth)
        self.listen_file_button_rect = self.listen_file_button.set_rect()
        self.escape_button = Button.Button(screen=self.screen,
                                            filename=c.escape_button,
                                            center_x=c.escape_button_x, center_y=c.escape_button_y,
                                            width=self.eb_width, height=self.eb_height,
                                            layername=c.light_button_layer2, smooth=c.smooth)
        self.escape_button_rect = self.escape_button.set_rect()


    def check_buttons(self, mouse_x, mouse_y, touchable):
        if self.choose_file_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'before':
            self.choose_file_button.button_predict()
        if self.play_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'after' and touchable:
            self.play_button.button_predict()
        if self.add_song_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'after' and touchable:
            self.add_song_button.button_predict()
        if self.check_data_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'after' and touchable:
            self.check_data_button.button_predict()
        if self.listen_file_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'after' and touchable:
            self.listen_file_button.button_predict()
        if self.escape_button_rect.collidepoint(mouse_x, mouse_y) and touchable:
            self.escape_button.button_predict()


    def load_file(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.state == 'before':
            if self.choose_file_button_rect.collidepoint(mouse_x, mouse_y):
                self.cover = LoadImage.load_image(self.oGetFilePath.load_file('sprites', 'error_cover.png'), c.smooth, (self.Height//2.5, self.Height//2.5))
                self.audio_path = self.oChooseFile.choose_file()
                self.state = 'after'

                if self.audio_path == None or self.audio_path.lower().endswith('.mp3') == False and self.audio_path.lower().endswith('.wav') == False:
                    self.state = 'before'
                else:
                    self.cover = LoadImage.load_image(extract_cover_image(self.audio_path), c.smooth, (self.Height//2.5, self.Height//2.5))
                    copy_audio_file(filename=self.audio_path)

                    self.cover = LoadImage.load_image(self.oGetFilePath.load_file('songs', 'temp_cover.jpg'), c.smooth, (self.Height//2.5, self.Height//2.5))
                self.cover_pos = self.cover.get_rect(center=(self.width//2, self.Height//2 - self.Height//4))


    def load_song_data(self):
        self.oSongInfo = SongInfo.SongInfo(self.audio_path)
        self.accuracy_bpm = self.oSongInfo.get_tempo(True)
        self.bpm = self.oSongInfo.get_tempo(False)
        self.key_list = self.oSongInfo.get_key('all')
        self.key, self.scale, self.strength = self.key_list[0], self.key_list[1], self.key_list[2]


    def check_events(self, event, mouse_x, mouse_y, touchable):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.state == 'after' and touchable:
            if self.add_song_button_rect.collidepoint(mouse_x, mouse_y) and touchable:
                return 'add_song'
            if self.check_data_button_rect.collidepoint(mouse_x, mouse_y) and touchable:
                return 'check_data'
            if self.listen_file_button_rect.collidepoint(mouse_x, mouse_y) and touchable:
                return 'listen_file'
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and touchable:
            if self.escape_button_rect.collidepoint(mouse_x, mouse_y):
                return 'exit'
        return None


    def open_play_window(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.play_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'after':
                return True
        return False
    

    def return_song(self):
        return [self.audio_path]
    

    def return_song_data(self):
        return self.bpm, self.accuracy_bpm, self.key, self.scale, self.strength

    
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.escape_button.button_image, (self.escape_button_rect))
        if self.state == 'before':
            self.screen.blit(self.choose_file_button.button_image, (self.choose_file_button_rect))
        if self.state == 'after':
            try:
                pygame.draw.rect(self.screen, (63, 70, 75), (self.cover_pos.centerx - self.cover_pos.width//2 - 2, self.cover_pos.centery - self.cover_pos.height//2 - 2, self.cover_pos.width + 4, self.cover_pos.height + 4), 5)                
                self.screen.blit(self.cover, (self.cover_pos))
                self.screen.blit(self.add_song_button.button_image, (self.add_song_button_rect))
                self.screen.blit(self.check_data_button.button_image, (self.check_data_button_rect))
                self.screen.blit(self.listen_file_button.button_image, (self.listen_file_button_rect))
            except Exception as e:
                print(f'ERROR: {e}')

    
    def draw_loading(self):
        self.screen.blit(self.black_layer, (0, 0))
        c.SS_LOADING_GIF.render(self.screen, (self.width//2 - c.gif_width//2, self.Height//2 - c.gif_height//2))
                

    def __del__(self):
        pass