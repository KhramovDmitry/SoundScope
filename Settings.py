import pygame
import Data
import Button
import config as c

class Settings:
    def __init__(self, screen):
        pygame.init()
        pygame.font.init()

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.Height = c.Height

        self.meb_x, self.meb_y = c.meb_x, c.meb_y
        self.mob1_x, self.mob1_y = c.mob1_x, c.mob1_y
        self.mob2_x, self.mob2_y = c.mob2_x, c.mob2_y

        self.meb_width, self.meb_height = c.mini_b_size
        self.mob1_width, self.mob1_height = c.mini_b_size
        self.mob2_width, self.mob2_height = c.mini_b_size

        self.black_layer = pygame.transform.smoothscale(pygame.image.load(c.black_layer).convert_alpha(), (self.width, self.Height))
        self.black_layer.set_alpha(150)
        self.menu_frame = pygame.transform.smoothscale(pygame.image.load(c.menu_frame).convert(), (c.mf_size))
        self.menu_frame_rect = self.menu_frame.get_rect(center=(c.mf_x, c.mf_y))

        #config.buttons
        self.mini_exit_button = Button.Button(screen=self.screen,
                                              filename=c.mini_exit_button,
                                              center_x=self.meb_x, center_y=self.meb_y,
                                              width=self.meb_width, height=self.meb_height,
                                              layername=c.light_button_layer3, smooth=c.smooth)
        self.mini_exit_button_rect = self.mini_exit_button.set_rect()

        self.graphics_button = Button.Button(self.screen, c.graphics_button,
                                            c.gb_x, c.gb_y, 
                                            c.gb_width, c.SB_height, 
                                            c.gb_layer, c.smooth)
        self.graphics_button_rect = self.graphics_button.set_rect()
        self.sound_button = Button.Button(self.screen, c.sound_button,
                                            c.soundbutton_x, c.soundbutton_y, 
                                            c.soundbutton_width, c.SB_height, 
                                            c.sb_layer, c.smooth)
        self.sound_button_rect = self.sound_button.set_rect()
        self.help_button = Button.Button(self.screen, c.help_button,
                                            c.hb_x, c.hb_y, 
                                            c.hb_width, c.SB_height, 
                                            c.hb_layer, c.smooth)
        self.help_button_rect = self.help_button.set_rect()
        self.community_button = Button.Button(self.screen, c.community_button,
                                            c.cb_x, c.cb_y, 
                                            c.cb_width, c.SB_height, 
                                            c.cb_layer, c.smooth)
        self.community_button_rect = self.community_button.set_rect()


        self.settings_text = c.settings_text
        self.settings_text_rect = self.settings_text.get_rect(center=(c.st_x, c.st_y))


    def check_buttons(self, mouse_x, mouse_y):
        if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
            self.mini_exit_button.button_predict()
        if self.graphics_button_rect.collidepoint(mouse_x, mouse_y):
            self.graphics_button.button_predict()
        if self.sound_button_rect.collidepoint(mouse_x, mouse_y):
            self.sound_button.button_predict()
        if self.help_button_rect.collidepoint(mouse_x, mouse_y):
            self.help_button.button_predict()
        if self.community_button_rect.collidepoint(mouse_x, mouse_y):
            self.community_button.button_predict()


    def extra_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
                return None
        return 'N'
    
    def extra2_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.graphics_button_rect.collidepoint(mouse_x, mouse_y):
                return 'graphics'
            if self.sound_button_rect.collidepoint(mouse_x, mouse_y):
                return 'sound'
            if self.help_button_rect.collidepoint(mouse_x, mouse_y):
                return 'help'
            if self.community_button_rect.collidepoint(mouse_x, mouse_y):
                return 'community'


    def draw(self):
        self.screen.blit(self.black_layer, (0, 0))
        self.screen.blit(self.menu_frame, self.menu_frame_rect)
        self.screen.blit(self.mini_exit_button.button_image, (self.mini_exit_button_rect))
        self.screen.blit(self.settings_text, (self.settings_text_rect))
        self.screen.blit(self.graphics_button.button_image, (self.graphics_button_rect))
        self.screen.blit(self.sound_button.button_image, (self.sound_button_rect))
        self.screen.blit(self.help_button.button_image, (self.help_button_rect))
        self.screen.blit(self.community_button.button_image, (self.community_button_rect))