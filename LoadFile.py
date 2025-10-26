import pygame
import Button
from LoadCover import extract_cover_image
import ChooseFile, SongInfo, GetFilePath
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

        self.bg = pygame.transform.smoothscale(pygame.image.load(c.menu_bg).convert_alpha(), (self.width, self.Height))

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

    def check_buttons(self, mouse_x, mouse_y):
        if self.choose_file_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'before':
            self.choose_file_button.button_predict()
        if self.play_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'after':
            self.play_button.button_predict()

    def load_file(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.state == 'before':
            if self.choose_file_button_rect.collidepoint(mouse_x, mouse_y):
                self.state = 'after'
                self.audio_path = self.oChooseFile.choose_file()
                
                if self.audio_path.lower().endswith('.mp3') == False:
                    self.state = 'before'
                elif self.audio_path == None:
                    self.state = 'before'
                else:
                    self.cover = extract_cover_image(self.audio_path)
                    if self.cover != None:
                        if c.smooth:
                            self.cover = pygame.transform.smoothscale(pygame.image.load(self.oGetFilePath.load_file('songs', 'temp_cover.jpg')).convert_alpha(), (self.Height//2.5, self.Height//2.5))
                        else:
                            self.cover = pygame.transform.scale(pygame.image.load(self.oGetFilePath.load_file('songs', 'temp_cover.jpg')).convert_alpha(), (self.Height//2.5, self.Height//2.5))
                    #elif self.cover == None:
                    #    if c.smooth:
                    #        self.cover = pygame.transform.smoothscale(pygame.image.load(c.error_cover).convert_alpha(), (self.Height//2.5, self.Height//2.5))
                    #    else:
                    #        self.cover = pygame.transform.scale(pygame.image.load(c.error_cover).convert_alpha(), (self.Height//2.5, self.Height//2.5))
                    self.cover_pos = self.cover.get_rect(center=(self.width//2, self.Height//2 - self.Height//4))

                    self.oSongInfo = SongInfo.SongInfo(self.audio_path)
                    self.accuracy_bpm = self.oSongInfo.get_tempo(True)
                    self.bpm = self.oSongInfo.get_tempo(False)
                    self.key_list = self.oSongInfo.get_key('all')
                    self.key, self.scale, self.strength = self.key_list[0], self.key_list[1], self.key_list[2]

    def open_play_window(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.play_button_rect.collidepoint(mouse_x, mouse_y) and self.state == 'after':
                return True
            
        return False
    
    def return_song(self):
        return [self.audio_path]

    
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        if self.state == 'before':
            self.screen.blit(self.choose_file_button.button_image, (self.choose_file_button_rect))
        if self.state == 'after':
            try:
                pygame.draw.rect(self.screen, (63, 70, 75), (self.cover_pos.centerx - self.cover_pos.width//2 - 2, self.cover_pos.centery - self.cover_pos.height//2 - 2, self.cover_pos.width + 4, self.cover_pos.height + 4), 5)
                self.screen.blit(self.cover, (self.cover_pos))
            except AttributeError:
                pass