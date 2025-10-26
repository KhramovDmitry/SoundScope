import pygame
import Button
import config as c

class Help:
    def __init__(self, screen):
        pygame.init()

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.true_width, self.true_height = c.true_width, c.true_height
        self.Height = c.Height

        self.meb2_x, self.meb2_y = c.meb_x, c.meb_y
        self.meb_width, self.meb_height = c.mini_b_size

        self.black_layer = pygame.transform.smoothscale(pygame.image.load(c.black_layer).convert_alpha(), (self.width, self.Height))
        self.black_layer.set_alpha(150)
        self.menu_frame = pygame.transform.smoothscale(pygame.image.load(c.menu_frame).convert(), (c.mf_size))
        self.menu_frame_rect = self.menu_frame.get_rect(center=(c.mf_x, c.mf_y))
        self.powered_by_python = pygame.transform.smoothscale(pygame.image.load(c.powered_by_python).convert_alpha(), (c.pbp_size))
        self.pbp_rect = self.powered_by_python.get_rect(center=(c.pbp_pos))

        #config.buttons
        self.mini_exit_button = Button.Button(screen=self.screen,
                                              filename=c.mini_exit_button,
                                              center_x=self.meb2_x, center_y=self.meb2_y,
                                              width=self.meb_width, height=self.meb_height,
                                              layername=c.light_button_layer3, smooth=c.smooth)
        self.mini_exit_button_rect = self.mini_exit_button.set_rect()

        self.help_text = c.help_text
        self.help_text_rect = self.help_text.get_rect(center=(c.st_x, c.st_y))
        self.support_text = c.support_text
        self.support_text_rect = self.support_text.get_rect(center=(c.supt_x, c.supt_y))
        self.gmail_text = c.gmail_text
        self.gmail_text_rect = self.gmail_text.get_rect(center=(c.gmailt_x, c.gmailt_y))


    def check_buttons(self, mouse_x, mouse_y):
        if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
            self.mini_exit_button.button_predict()

    def extra2_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
                return None
        return 'N'
    
    def draw(self):
        self.screen.blit(self.black_layer, (0, 0))
        self.screen.blit(self.menu_frame, self.menu_frame_rect)
        self.screen.blit(self.mini_exit_button.button_image, (self.mini_exit_button_rect))
        self.screen.blit(self.help_text, (self.help_text_rect))
        self.screen.blit(self.support_text, (self.support_text_rect))
        self.screen.blit(self.gmail_text, (self.gmail_text_rect))
        self.screen.blit(self.powered_by_python, (self.pbp_rect))