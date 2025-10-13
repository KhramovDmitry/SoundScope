import pygame
import Data
import Button
import EntryBox
import config as c

class Account:
    def __init__(self, screen):
        pygame.init()
        pygame.font.init()

        self.eb_font = c.TTC_regular_eb

        self.oData = Data.Data()
        self.data = self.oData.load_data('account_data.json')

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.Height = c.Height

        self.meb_x, self.meb_y = c.meb_x, c.meb_y
        self.mob1_x, self.mob1_y = c.mob1_x, c.mob1_y
        self.mob2_x, self.mob2_y = c.mob2_x, c.mob2_y

        self.meb_width, self.meb_height = c.mini_b_size
        self.mob1_width, self.mob1_height = c.mini_b_size
        self.mob2_width, self.mob2_height = c.mini_b_size

        self.eb_width, self.eb_height = c.eb_size

        self.black_layer = pygame.transform.smoothscale(pygame.image.load(c.black_layer).convert_alpha(), (self.width, self.Height))
        self.black_layer.set_alpha(150)
        self.menu_frame = pygame.transform.smoothscale(pygame.image.load(c.menu_frame).convert(), (c.mf_size))
        self.menu_frame_rect = self.menu_frame.get_rect(center=(c.mf_x, c.mf_y))
        self.entry_box = pygame.transform.scale(pygame.image.load(c.entry_box).convert_alpha(), (c.eb_size))
        self.entry_box1_rect = self.entry_box.get_rect(center=(c.eb1_x, c.eb1_y))
        self.entry_box2_rect = self.entry_box.get_rect(center=(c.eb2_x, c.eb2_y))
        self.oEntryBox1 = EntryBox.EntryBox(self.screen, 
                                            self.entry_box1_rect,
                                            c.TTC_regular_path,
                                            c.TTC_r_eb_size,
                                            c.SS_BLUE, 
                                            c.eb1_x, c.eb1_y,
                                            self.data['e-mail'],
                                            'почта Гугл')
        self.oEntryBox2 = EntryBox.EntryBox(self.screen,
                                            self.entry_box1_rect,
                                            c.TTC_regular_path,
                                            c.TTC_r_eb_size,
                                            c.SS_BLUE,
                                            c.eb2_x, c.eb2_y,
                                            self.data['nickname'],
                                            'псевдоним')

        self.account_text = c.account_text
        self.account_text_rect = self.account_text.get_rect(center=(c.at_x, c.at_y))

        #config.buttons
        self.mini_exit_button = Button.Button(screen=self.screen,
                                              filename=c.mini_exit_button,
                                              center_x=self.meb_x, center_y=self.meb_y,
                                              width=self.meb_width, height=self.meb_height,
                                              layername=c.light_button_layer3, smooth=True)
        self.mini_exit_button_rect = self.mini_exit_button.set_rect()
        self.mini_ok1_button = Button.Button(screen=self.screen,
                                              filename=c.mini_ok_button,
                                              center_x=self.mob1_x, center_y=self.mob1_y,
                                              width=self.mob1_width, height=self.mob1_height,
                                              layername=c.light_button_layer3, smooth=True)
        self.mini_ok1_button_rect = self.mini_ok1_button.set_rect()
        self.mini_ok2_button = Button.Button(screen=self.screen,
                                              filename=c.mini_ok_button,
                                              center_x=self.mob2_x, center_y=self.mob2_y,
                                              width=self.mob2_width, height=self.mob2_height,
                                              layername=c.light_button_layer3, smooth=True)
        self.mini_ok2_button_rect = self.mini_ok2_button.set_rect()

    
    def check_buttons(self, mouse_x, mouse_y):
        if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
            self.mini_exit_button.button_predict()
        if self.mini_ok1_button_rect.collidepoint(mouse_x, mouse_y):
            self.mini_ok1_button.button_predict()
        if self.mini_ok2_button_rect.collidepoint(mouse_x, mouse_y):
            self.mini_ok2_button.button_predict()


    def extra_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
                return None
        return 'N'
    
    def entry_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.entry_box1_rect.collidepoint(mouse_x, mouse_y):
                return 'e-mail'
            if self.entry_box2_rect.collidepoint(mouse_x, mouse_y):
                return 'nickname'
        return 'N'


    def draw(self):
        self.screen.blit(self.black_layer, (0, 0))
        self.screen.blit(self.menu_frame, (self.menu_frame_rect))
        self.screen.blit(self.account_text, (self.account_text_rect))
        self.screen.blit(self.mini_exit_button.button_image, (self.mini_exit_button_rect))
        self.screen.blit(self.mini_ok1_button.button_image, (self.mini_ok1_button_rect))
        self.screen.blit(self.mini_ok2_button.button_image, (self.mini_ok2_button_rect))
        self.screen.blit(self.entry_box, (self.entry_box1_rect), special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(self.entry_box, (self.entry_box2_rect), special_flags=pygame.BLEND_RGBA_MULT)
        self.oEntryBox1.draw_text()
        self.oEntryBox1.draw_error(c.TTC_light_error, c.error1_x, c.error1_y)
        self.oEntryBox2.draw_text()
        self.oEntryBox2.draw_error(c.TTC_light_error, c.error2_x, c.error2_y)