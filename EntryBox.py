import pygame
import Data
import config as c

class EntryBox:
    def __init__(self, screen, rect, font_file, size, color, text_x, text_y, text, text2):
        pygame.init()
        pygame.font.init()

        self.oData = Data.Data()
        self.data = self.oData.load_data('account_data.json')

        self.screen = screen
        self.rect, self.text = rect, text
        self.font_file, self.size, self.oldsize = font_file, size, size
        self.font = pygame.font.Font(font_file, self.size)
        self.font2 = pygame.font.Font(font_file, self.oldsize)
        self.color = color
        self.text_x, self.text_y = text_x, text_y
        self.text2 = text2
        self.alpha = 20

        self.error_text = ''
        self.error_color = (0, 0, 0)
        self.error = False


    def draw_text(self):
        self.input_text = self.font.render(self.text, True, self.color)
        self.text2_ = self.font2.render(self.text2, True, self.color).convert_alpha()
        self.text2_.set_alpha(self.alpha)
        self.text_rect = self.input_text.get_rect(center=(self.text_x, self.text_y))
        self.text2_rect = self.text2_.get_rect(center=(self.text_x, self.text_y))
        if self.text_rect.width + c.width//110 > self.rect.width:
            self.size = int(round(self.size - self.size*0.2))
            self.font = pygame.font.Font(self.font_file, self.size)
        self.screen.blit(self.input_text, self.text_rect)
        self.screen.blit(self.text2_, self.text2_rect)
        if len(self.text) == 0:
            self.alpha = 11
        else:
            self.alpha = 0

    def draw_error(self, font, x, y):
        self.error_message = font.render(self.error_text, True, self.error_color)
        self.error_message_rect = self.error_message.get_rect(center=(x, y))
        self.screen.blit(self.error_message, self.error_message_rect)

    def typing(self, event, rect: pygame.Rect, mouse_x, mouse_y, flag, predicted_flag):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if flag == predicted_flag:
                    if len(self.text) > 25:
                        self.error_color = c.SS_RED
                        self.error_text = 'Ввод не более 25 символов!'
                        self.error = True
                        return None
                    elif len(self.text) <= 25:
                        self.error_color = c.SS_GREEN
                        self.error_text = 'Данные успешно сохранены.'
                        self.error = False
                        return self.text
                return 'N'
                
            elif event.key == pygame.K_BACKSPACE:
                if flag == predicted_flag:
                    self.text = self.text[:-1]
                    if self.text_rect.width + c.width//110 < self.rect.width:
                        if self.size < self.oldsize:
                            self.size = int(round(self.size + self.size*0.1))
                            self.font = pygame.font.Font(self.font_file, self.size)
            else:
                if flag == predicted_flag:
                    self.text += event.unicode
                    if self.text_rect.width > self.rect.width:
                        self.size = int(round(self.size - self.size*0.1))
                        self.font = pygame.font.Font(self.font_file, self.size)
                    

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if rect.collidepoint(mouse_x, mouse_y):
                    if len(self.text) > 25:
                        self.error_color = c.SS_RED
                        self.error_text = 'Ввод не более 25 символов!'
                        self.error = True
                    elif len(self.text) <= 25:
                        self.error_color = c.SS_GREEN
                        self.error_text = 'Данные успешно сохранены.'
                        self.error = False
                        return self.text