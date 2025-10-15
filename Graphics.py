import pygame
import Data
import Button
import config as c

class Graphics:
    def __init__(self, screen):
        pygame.init()

        self.screen: pygame.Surface = screen
        self.width, self.height = c.width, c.height
        self.true_width, self.true_height = c.true_width, c.true_height
        self.Height = c.Height

        self.meb2_x, self.meb2_y = c.meb2_x, c.meb2_y
        self.meb_width, self.meb_height = c.mini_b_size
        self.srb_width, self.srb_height = c.srb_size
        self.ab_x, self.ab_y = c.ab_pos

        self.black_layer = pygame.transform.smoothscale(pygame.image.load(c.black_layer).convert_alpha(), (self.width, self.Height))
        self.black_layer.set_alpha(150)
        self.graphics_frame = pygame.transform.smoothscale(pygame.image.load(c.graphics_frame).convert(), (c.gf_size))
        self.graphics_frame_rect = self.graphics_frame.get_rect(center=(c.mf_x, c.mf_y))

        #config.buttons
        self.mini_exit_button = Button.Button(screen=self.screen,
                                              filename=c.mini_exit_button,
                                              center_x=self.meb2_x, center_y=self.meb2_y,
                                              width=self.meb_width, height=self.meb_height,
                                              layername=c.light_button_layer3, smooth=c.smooth)
        self.mini_exit_button_rect = self.mini_exit_button.set_rect()

        self.sr1_button = Button.Button(screen=self.screen,
                                              filename=c.screen_resolution_button,
                                              center_x=c.sr1b_x, center_y=c.sr1b_y,
                                              width=self.srb_width, height=self.srb_height,
                                              layername=c.screen_resolution_layer, smooth=c.smooth)
        self.sr1_button_rect = self.sr1_button.set_rect()
        self.sr2_button = Button.Button(screen=self.screen,
                                              filename=c.screen_resolution_button,
                                              center_x=c.sr2b_x, center_y=c.sr2b_y,
                                              width=self.srb_width, height=self.srb_height,
                                              layername=c.screen_resolution_layer, smooth=c.smooth)
        self.sr2_button_rect = self.sr2_button.set_rect()
        self.sr3_button = Button.Button(screen=self.screen,
                                              filename=c.screen_resolution_button,
                                              center_x=c.sr3b_x, center_y=c.sr3b_y,
                                              width=self.srb_width, height=self.srb_height,
                                              layername=c.screen_resolution_layer, smooth=c.smooth)
        self.sr3_button_rect = self.sr3_button.set_rect()
        self.fb_button = Button.Button(screen=self.screen,
                                              filename=c.screen_resolution_button,
                                              center_x=c.fb_x, center_y=c.fb_y,
                                              width=self.srb_width, height=self.srb_height,
                                              layername=c.screen_resolution_layer, smooth=c.smooth)
        self.fb_button_rect = self.fb_button.set_rect()
        self.ab_button = Button.Button(screen=self.screen,
                                              filename=c.screen_resolution_button,
                                              center_x=self.ab_x, center_y=self.ab_y,
                                              width=self.srb_width, height=self.srb_height,
                                              layername=c.screen_resolution_layer, smooth=c.smooth)
        self.ab_button_rect = self.ab_button.set_rect()
        self.sy_button = Button.Button(screen=self.screen,
                                              filename=c.screen_resolution_button,
                                              center_x=c.syt_x, center_y=c.syt_y,
                                              width=self.srb_width, height=self.srb_height,
                                              layername=c.screen_resolution_layer, smooth=c.smooth)
        self.sy_button_rect = self.sy_button.set_rect()
        self.sn_button = Button.Button(screen=self.screen,
                                              filename=c.screen_resolution_button,
                                              center_x=c.snt_x, center_y=c.snt_y,
                                              width=self.srb_width, height=self.srb_height,
                                              layername=c.screen_resolution_layer, smooth=c.smooth)
        self.sn_button_rect = self.sn_button.set_rect()

        self.graphics_text = c.graphics_text
        self.graphics_text_rect = self.graphics_text.get_rect(center=(c.gt_x, c.gt_y))
        self.screen_resolution_text = c.screen_resolution_text
        self.screen_resolution_text_rect = self.screen_resolution_text.get_rect(center=(c.srt_x, c.srt_y))
        self.textures_text = c.textures_text
        self.textures_text_rect = self.textures_text.get_rect(center=(c.tt_x, c.tt_y))
        self.apply_text = c.apply_text
        self.apply_text_rect = self.apply_text.get_rect(center=(self.ab_x, self.ab_y))

        self.sr1t_rect = c.sr1b_text.get_rect(center=(c.sr1b_x, c.sr1b_y))
        self.sr2t_rect = c.sr2b_text.get_rect(center=(c.sr2b_x, c.sr2b_y))
        self.sr3t_rect = c.sr3b_text.get_rect(center=(c.sr3b_x, c.sr3b_y))
        self.fbt_rect = c.fullscreen_text.get_rect(center=(c.fb_x, c.fb_y))

        self.syt_text = c.smooth_yes_text
        self.syt_text_rect = self.syt_text.get_rect(center=(c.syt_x, c.syt_y))
        self.snt_text = c.smooth_no_text
        self.snt_text_rect = self.snt_text.get_rect(center=(c.snt_x, c.snt_y))

        self.rt_text = c.reset_text
        self.rt_text_rect = self.rt_text.get_rect(center=(c.rt_pos))

    def check_buttons(self, mouse_x, mouse_y):
        if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
            self.mini_exit_button.button_predict()
        if self.sr1_button_rect.collidepoint(mouse_x, mouse_y):
            self.sr1_button.button_predict()
        if self.sr2_button_rect.collidepoint(mouse_x, mouse_y):
            self.sr2_button.button_predict()
        if self.sr3_button_rect.collidepoint(mouse_x, mouse_y):
            self.sr3_button.button_predict()
        if self.fb_button_rect.collidepoint(mouse_x, mouse_y):
            self.fb_button.button_predict()
        if self.ab_button_rect.collidepoint(mouse_x, mouse_y):
            self.ab_button.button_predict()
        if self.sy_button_rect.collidepoint(mouse_x, mouse_y):
            self.sy_button.button_predict()
        if self.sn_button_rect.collidepoint(mouse_x, mouse_y):
            self.sn_button.button_predict()

    def buttons_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.sr1_button_rect.collidepoint(mouse_x, mouse_y):
                return '1'
            if self.sr2_button_rect.collidepoint(mouse_x, mouse_y):
                return '2'
            if self.sr3_button_rect.collidepoint(mouse_x, mouse_y):
                return '3'
            if self.fb_button_rect.collidepoint(mouse_x, mouse_y):
                return '4'
        return None
    
    def buttons2_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.sy_button_rect.collidepoint(mouse_x, mouse_y):
                return 'yes'
            if self.sn_button_rect.collidepoint(mouse_x, mouse_y):
                return 'no'
            
    def save_changes(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.ab_button_rect.collidepoint(mouse_x, mouse_y):
                return 'SAVE'
        return None

    def extra2_event(self, event, mouse_x, mouse_y):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.mini_exit_button_rect.collidepoint(mouse_x, mouse_y):
                return None
        return 'N'
    

    def draw(self):
        self.screen.blit(self.black_layer, (0, 0))
        self.screen.blit(self.graphics_frame, self.graphics_frame_rect)
        self.screen.blit(self.mini_exit_button.button_image, (self.mini_exit_button_rect))
        self.screen.blit(self.graphics_text, (self.graphics_text_rect))
        self.screen.blit(self.screen_resolution_text, (self.screen_resolution_text_rect))
        self.screen.blit(self.textures_text, (self.textures_text_rect))
        self.screen.blit(self.sr1_button.button_image, (self.sr1_button_rect))
        self.screen.blit(self.sr2_button.button_image, (self.sr2_button_rect))
        self.screen.blit(self.sr3_button.button_image, (self.sr3_button_rect))
        self.screen.blit(self.fb_button.button_image, (self.fb_button_rect))
        self.screen.blit(self.ab_button.button_image, (self.ab_button_rect))
        self.screen.blit(self.sy_button.button_image, (self.sy_button_rect))
        self.screen.blit(self.sn_button.button_image, (self.sn_button_rect))
        self.screen.blit(c.sr1b_text, (self.sr1t_rect))
        self.screen.blit(c.sr2b_text, (self.sr2t_rect))
        self.screen.blit(c.sr3b_text, (self.sr3t_rect))
        self.screen.blit(c.fullscreen_text, (self.fbt_rect))
        self.screen.blit(self.apply_text, (self.apply_text_rect))
        self.screen.blit(self.syt_text, (self.syt_text_rect))
        self.screen.blit(self.snt_text, (self.snt_text_rect))
        self.screen.blit(self.rt_text, (self.rt_text_rect))