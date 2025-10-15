import pygame
import LinkJump
import config as c
import Button

class Info:
    def __init__(self, screen):
        pygame.init()

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.Height = c.Height

        self.meb_x, self.meb_y = c.meb_x, c.meb_y
        self.meb_width, self.meb_height = c.mini_b_size
        self.wb_width, self.wb_height = c.website_size
        self.wb_x, self._wb_y = c.website_pos
        self.wt_pos = c.wt_x, c.wt_y
        self.f_text_pos = c.f_text_pos
        self.website_rext = c.website_text

        self.f_text = c.f_text
        self.f_text_rect = self.f_text.get_rect(center=(self.f_text_pos))
        self.website_text_rect = self.website_rext.get_rect(center=self.wt_pos)

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

        self.website_button = Button.Button(self.screen, c.website_button,
                                            self.wb_x, self._wb_y,
                                            self.wb_width, self.wb_height,
                                            c.community_button_layer, smooth=c.smooth)
        self.website_button_rect = self.website_button.set_rect()

        self.info_text = c.info_text
        self.info_text_rect = self.info_text.get_rect(center=(c.it_x, c.it_y))
    
    def extra_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
                return None
        return 'N'
    
    def check_buttons(self, mouse_x, mouse_y):
        if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
            self.mini_exit_button.button_predict()
        if self.website_button_rect.collidepoint(mouse_x, mouse_y):
            self.website_button.button_predict()
        
    def WebsiteJump(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.website_button_rect.collidepoint(mouse_x, mouse_y):
                LinkJump.link_jump('file://' + c.info_path)

    def draw(self):
        self.screen.blit(self.black_layer, (0, 0))
        self.screen.blit(self.menu_frame, self.menu_frame_rect)
        self.screen.blit(self.mini_exit_button.button_image, (self.mini_exit_button_rect))
        self.screen.blit(self.info_text, (self.info_text_rect))
        self.screen.blit(self.website_button.button_image, (self.website_button_rect))
        self.screen.blit(self.website_rext, (self.website_text_rect))
        self.screen.blit(self.f_text, (self.f_text_rect))