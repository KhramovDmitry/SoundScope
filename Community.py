import pygame
import Data
import Button
import config as c
import LinkJump

class Community:
    def __init__(self, screen):
        pygame.init()
        pygame.font.init()

        self.oData = Data.Data()
        self.data = self.oData.load_data('account_data.json')

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.Height = c.Height

        self.community_text_pos = c.community_text_x, c.community_text_y
        self.max_text_pos = c.max_text_pos
        self.telegram_text_pos = c.telegram_text_pos
        self.f_text_pos = c.f_text_pos

        self.max_button_x, self.max_button_y = c.max_button_x, c.max_button_y
        self.telegram_button_x, self.telegram_button_y = c.telegram_button_x, c.telegram_button_y
        self.community_button_width, self.community_button_height = c.community_size

        self.meb_x, self.meb_y = c.meb_x, c.meb_y
        self.meb_width, self.meb_height = c.mini_b_size

        self.black_layer = pygame.transform.smoothscale(pygame.image.load(c.black_layer).convert_alpha(), (self.width, self.Height))
        self.black_layer.set_alpha(150)
        self.menu_frame = pygame.transform.smoothscale(pygame.image.load(c.menu_frame).convert(), (c.mf_size))
        self.menu_frame_rect = self.menu_frame.get_rect(center=(c.mf_x, c.mf_y))

        self.community_text = c.community_text
        self.community_text_rect = self.community_text.get_rect(center=(self.community_text_pos))
        self.max_text = c.max_text
        self.max_text_rect = self.max_text.get_rect(center=(self.max_text_pos))
        self.telegram_text = c.telegram_text
        self.telegram_text_rect = self.telegram_text.get_rect(center=(self.telegram_text_pos))
        self.f_text = c.f_text
        self.f_text_rect = self.f_text.get_rect(center=(self.f_text_pos))

        #config.buttons
        self.mini_exit_button = Button.Button(screen=self.screen,
                                              filename=c.mini_exit_button,
                                              center_x=self.meb_x, center_y=self.meb_y,
                                              width=self.meb_width, height=self.meb_height,
                                              layername=c.light_button_layer3, smooth=True)
        self.mini_exit_button_rect = self.mini_exit_button.set_rect()
        self.max_button = Button.Button(screen=self.screen, 
                                        filename=c.max_button,
                                        center_x=self.max_button_x, center_y=self.max_button_y, 
                                        width=self.community_button_width, height=self.community_button_height,
                                        layername=c.community_button_layer, smooth=True)
        self.max_button_rect = self.max_button.set_rect()
        self.telegram_button = Button.Button(screen=self.screen, 
                                        filename=c.telegram_button,
                                        center_x=self.telegram_button_x, center_y=self.telegram_button_y, 
                                        width=self.community_button_width, height=self.community_button_height,
                                        layername=c.community_button_layer, smooth=True)
        self.telegram_button_rect = self.telegram_button.set_rect()

    def check_buttons(self, mouse_x, mouse_y):
        if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
            self.mini_exit_button.button_predict()
        if self.max_button_rect.collidepoint(mouse_x, mouse_y):
            self.max_button.button_predict()
        if self.telegram_button_rect.collidepoint(mouse_x, mouse_y):
            self.telegram_button.button_predict()

    def extra2_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
                return None
        return 'N'
    
    def buttons_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.telegram_button_rect.collidepoint(mouse_x, mouse_y):
                LinkJump.link_jump(c.telegram_link)
            if self.max_button_rect.collidepoint(mouse_x, mouse_y):
                LinkJump.link_jump(c.max_link)

    def draw(self):
        self.screen.blit(self.black_layer, (0, 0))
        self.screen.blit(self.menu_frame, self.menu_frame_rect)
        self.screen.blit(self.mini_exit_button.button_image, (self.mini_exit_button_rect))
        self.screen.blit(self.community_text, self.community_text_rect)
        self.screen.blit(self.f_text, self.f_text_rect)
        self.screen.blit(self.max_button.button_image, self.max_button_rect)
        self.screen.blit(self.telegram_button.button_image, self.telegram_button_rect)
        self.screen.blit(self.telegram_text, self.telegram_text_rect)
        self.screen.blit(self.max_text, self.max_text_rect)