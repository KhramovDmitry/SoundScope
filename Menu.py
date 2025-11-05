import pygame
import config as c
import Button

class Menu:
    def __init__(self, screen):
        pygame.init()
        pygame.font.init()

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.Height = c.Height

        self.mpb_x, self.mpb_y = c.mpb_x, c.mpb_y
        self.lfb_x, self.lfb_y = c.lfb_x, c.lfb_y
        self.mcb_x, self.mcb_y = c.mcb_x, c.mcb_y
        self.ab_x, self.ab_y = c.ab_x, c.ab_y
        self.sb_x, self.sb_y = c.sb_x, c.sb_y
        self.ib_x, self.ib_y = c.ib_x, c.ib_y

        self.mpb_width, self.mpb_height = c.mb1_size
        self.lfb_width, self.lfb_height = c.mb1_size
        self.mcb_width, self.mcb_height = c.mb1_size
        self.ab_width, self.ab_height = c.mb2_size
        self.sb_width, self.sb_height = c.mb2_size
        self.ib_width, self.ib_height = c.mb2_size
        self.eb_width, self.eb_height = c.mb2_size

        self.greet1_x, self.greet1_y = c.greet1_x, c.greet1_y
        self.greet2_x, self.greet2_y = c.greet2_x, c.greet2_y

        self.bg = pygame.transform.smoothscale(pygame.image.load(c.menu_bg).convert_alpha(), (self.width, self.Height))
        self.waveform = pygame.transform.smoothscale(pygame.image.load(c.waveform).convert_alpha(), (c.waveform_size))

        self.greet_1_text = c.greet_1_text
        self.greet_2_text = c.greet_2_text

        self.greet1_rect = self.greet_1_text.get_rect(center=(self.greet1_x, self.greet1_y))
        self.greet2_rect = self.greet_2_text.get_rect(center=(self.greet2_x, self.greet2_y))


        #config.buttons
        #big.buttons
        self.my_playlist_button = Button.Button(screen=self.screen,
                                                  filename=c.my_playlist_button,
                                                  center_x=self.mpb_x, center_y=self.mpb_y,
                                                  width=self.mpb_width, height=self.mpb_height,
                                                  layername=c.light_button_layer, smooth=c.smooth)
        self.my_playlist_button_rect = self.my_playlist_button.set_rect()
        self.load_file_button = Button.Button(screen=self.screen,
                                                  filename=c.load_file_button,
                                                  center_x=self.lfb_x, center_y=self.lfb_y,
                                                  width=self.lfb_width, height=self.lfb_height,
                                                  layername=c.light_button_layer, smooth=c.smooth)
        self.load_file_button_rect = self.load_file_button.set_rect()
        self.my_creations_button = Button.Button(screen=self.screen,
                                                  filename=c.my_creations_button,
                                                  center_x=self.mcb_x, center_y=self.mcb_y,
                                                  width=self.mcb_width, height=self.mcb_height,
                                                  layername=c.light_button_layer, smooth=c.smooth)
        self.my_creations_button_rect = self.my_creations_button.set_rect()
        #small.buttons
        self.account_button = Button.Button(screen=self.screen,
                                            filename=c.account_button,
                                            center_x=self.ab_x, center_y=self.ab_y,
                                            width=self.ab_width, height=self.ab_height,
                                            layername=c.light_button_layer2, smooth=c.smooth)
        self.account_button_rect = self.account_button.set_rect()
        self.settings_button = Button.Button(screen=self.screen,
                                            filename=c.settings_button,
                                            center_x=self.sb_x, center_y=self.sb_y,
                                            width=self.sb_width, height=self.sb_height,
                                            layername=c.light_button_layer2, smooth=c.smooth)
        self.settings_button_rect = self.settings_button.set_rect()
        self.info_button = Button.Button(screen=self.screen,
                                            filename=c.info_button,
                                            center_x=self.ib_x, center_y=self.ib_y,
                                            width=self.ib_width, height=self.ib_height,
                                            layername=c.light_button_layer2, smooth=c.smooth)
        self.info_button_rect = self.info_button.set_rect()
        self.escape_button = Button.Button(screen=self.screen,
                                            filename=c.escape_button,
                                            center_x=c.escape_button_x, center_y=c.escape_button_y,
                                            width=self.eb_width, height=self.eb_height,
                                            layername=c.light_button_layer2, smooth=c.smooth)
        self.escape_button_rect = self.escape_button.set_rect()

    
    def check_buttons(self, mouse_x, mouse_y, menu_touchable):
        if self.my_playlist_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
            self.my_playlist_button.button_predict()
        if self.load_file_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
            self.load_file_button.button_predict()
        if self.my_creations_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
            self.my_creations_button.button_predict()
        if self.account_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
            self.account_button.button_predict()
        if self.settings_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
            self.settings_button.button_predict()
        if self.info_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
            self.info_button.button_predict()
        if self.escape_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
            self.escape_button.button_predict()


    def handle_event(self, event, mouse_x, mouse_y, menu_touchable):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.my_playlist_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
                return 'my_playlist'
            if self.load_file_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
                return 'load_file'
            if self.my_creations_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
                return 'my_creations'
            if self.escape_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
                return 'exit'
        return None
    

    def extra_event(self, event, mouse_x, mouse_y, menu_touchable):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: 
            if self.account_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
                return 'account'
            if self.settings_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
                return 'settings'
            if self.info_button_rect.collidepoint(mouse_x, mouse_y) and menu_touchable:
                return 'info'
        return 'N'


    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.waveform, (0, 0), special_flags=pygame.BLEND_RGBA_MAX)
        self.screen.blit(self.greet_1_text, self.greet1_rect)
        self.screen.blit(self.greet_2_text, self.greet2_rect)
        self.screen.blit(self.escape_button.button_image, (self.escape_button_rect))
        self.screen.blit(self.my_playlist_button.button_image, (self.my_playlist_button_rect))
        self.screen.blit(self.load_file_button.button_image, (self.load_file_button_rect))
        self.screen.blit(self.my_creations_button.button_image, (self.my_creations_button_rect))
        self.screen.blit(self.account_button.button_image, (self.account_button_rect))
        self.screen.blit(self.settings_button.button_image, (self.settings_button_rect))
        self.screen.blit(self.info_button.button_image, (self.info_button_rect))