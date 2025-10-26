import pygame, time, multiprocessing as mp
import ConfigWindow
import Menu, Account, Settings, Community, Graphics, Help, Sounds, Info
import LoadFile
import Data
import PlayProcess
from CleanInput import clean_input
import config as c

play_process = None

class Application:
    def __init__(self):
        global play_process

        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.__current_state = c.current_state
        self.__extra_state = 'N'
        self.__extra2_state = None
        self.__new_state = None
        self.__new_extra_state = None
        self.__new_extra2_state = None
        self.__entry_event = None
        self.__previous_entry_event = c.previous_entry_event
        self.__graphics_event = None
        self.__graphics2_event = None
        self.__menu_touchable = True
        self.__settings_touchable = True

        #config.data
        self.oData = Data.Data()
        self.data = self.oData.load_data('app_data.json')

        self.account_data = self.oData.load_data('account_data.json')

        #config.screen
        self.__oConfigWindow = ConfigWindow.ConfigWindow()

        self.__oConfigWindow.configure_window()
        self.__width, self.__height = c.width, c.height
        self.__true_width, self.__true_height = c.true_width, c.true_height

        self.__fullscreen = self.data['fullscreen']

        if self.__fullscreen and self.data['screen_resolution'] == False:
            self.__screen = pygame.display.set_mode((self.__width, self.__height), pygame.FULLSCREEN)
        else:
            self.__screen = pygame.display.set_mode((self.__width, self.__height))

        self.__fps = 120
        self.__clock = pygame.time.Clock()

        #config.menu.classes
        self.__oMenu = Menu.Menu(self.__screen)
        self.__oAccount = Account.Account(self.__screen)
        self.__oSettings = Settings.Settings(self.__screen)
        self.__oCommunity = Community.Community(self.__screen)
        self.__oGraphics = Graphics.Graphics(self.__screen)
        self.__oHelp = Help.Help(self.__screen)
        self.__oSounds = Sounds.Sounds(self.__screen)
        self.__oInfo = Info.Info(self.__screen)

        #config.loadfile.classes
        self.__oLoadFile = LoadFile.LoadFile(self.__screen)

        #work.end.flag
        self.__work_end = False

    #app.cycle
    def run(self):
        while not self.__work_end:

            self.__clock.tick(self.__fps)

            self.__mouse_x, self.__mouse_y = pygame.mouse.get_pos()

            self.__check_logic()
            self.__draw()
            self.__check_events()

    #check.events
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.oData.dump_data('app_data.json', self.data)
                self.oData.dump_data('account_data.json', self.account_data)
                self.__work_end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and (self.__entry_event == 'N' or self.__entry_event == None) and self.data['screen_resolution'] == False:
                    self.__fullscreen = not self.__fullscreen
                    if self.__fullscreen:
                        self.__screen = pygame.display.set_mode((self.__width, self.__height), pygame.FULLSCREEN)
                    if self.__fullscreen == False:
                        self.__screen = pygame.display.set_mode((self.__width, self.__height))
                if event.key == pygame.K_ESCAPE:
                    if self.__current_state == 'menu' and self.__menu_touchable:
                        self.oData.dump_data('app_data.json', self.data)
                        self.oData.dump_data('account_data.json', self.account_data)
                        self.__work_end = True
                    if self.__extra_state == 'account':
                        self.__extra_state, self.__menu_touchable = None, True
                        self.__oAccount.oEntryBox1.error_text, self.__oAccount.oEntryBox2.error_text = '', ''
                        self.__oAccount.oEntryBox1.text, self.__oAccount.oEntryBox2.text = self.account_data['e-mail'], self.account_data['nickname']
                        if self.account_data['nickname'] == '':
                            c.greet_2_text__ = f'Добро пожаловать!'
                        else:
                            c.greet_2_text__ = f'С возвращением, {self.account_data['nickname']}!'
                        self.__oMenu.greet_2_text = c.TTC_demibold_menu.render(c.greet_2_text__, c.TTC_db_menu_size, c.SS_DARKBLUE)
                        self.__oMenu.greet2_rect = self.__oMenu.greet_2_text.get_rect(center=(c.greet2_x, c.greet2_y))
                        self.__entry_event, self.__previous_entry_event = 'N', 'N'
                    if self.__extra_state == 'settings' and self.__settings_touchable:
                        self.__extra_state, self.__menu_touchable = None, True
                    if self.__extra2_state == 'community':
                        self.__extra2_state, self.__settings_touchable = None, True
                    if self.__extra2_state == 'graphics':
                        self.__extra2_state, self.__settings_touchable = None, True
                        self.__graphics_event, self.__graphics2_event = None, None
                    if self.__extra_state == 'info':
                        self.__extra_state, self.__menu_touchable = None, True
                    if self.__current_state == 'load_file':
                        self.__current_state = 'menu'

        #--------------------MENU-------------------#
            if self.__current_state == 'menu':
                self.__new_state = self.__oMenu.handle_event(event=event, mouse_x=self.__mouse_x, mouse_y=self.__mouse_y, menu_touchable=self.__menu_touchable)
                if self.__new_state == 'my_playlist':
                    self.__current_state = 'my_playlist'
                if self.__new_state == 'load_file':
                    self.__current_state = 'load_file'
                if self.__new_state == 'my_creations':
                    self.__current_state = 'my_creations'

                self.__new_extra_state = self.__oMenu.extra_event(event=event, mouse_x=self.__mouse_x, mouse_y=self.__mouse_y, menu_touchable=self.__menu_touchable)
                if self.__new_extra_state == 'account':
                    self.__extra_state = 'account'
                if self.__new_extra_state == 'settings':
                    self.__extra_state = 'settings'
                if self.__new_extra_state == 'info':
                    self.__extra_state = 'info'

        #------------------ACCOUNT---------------#
            if self.__extra_state == 'account':
                self.__new_extra_state = self.__oAccount.extra_event(event=event, mouse_x=self.__mouse_x, mouse_y=self.__mouse_y)
                self.__entry_event = self.__oAccount.entry_event(event, self.__mouse_x, self.__mouse_y)
                if self.__new_extra_state == None:
                    self.__extra_state, self.__menu_touchable = None, True
                    self.__oAccount.oEntryBox1.error_text, self.__oAccount.oEntryBox2.error_text = '', ''
                    self.__oAccount.oEntryBox1.text, self.__oAccount.oEntryBox2.text = self.account_data['e-mail'], self.account_data['nickname']
                    if self.account_data['nickname'] == '':
                        c.greet_2_text__ = f'Добро пожаловать!'
                    else:
                        c.greet_2_text__ = f'С возвращением, {self.account_data['nickname']}!'
                    self.__oMenu.greet_2_text = c.TTC_demibold_menu.render(c.greet_2_text__, c.TTC_db_menu_size, c.SS_DARKBLUE)
                    self.__oMenu.greet2_rect = self.__oMenu.greet_2_text.get_rect(center=(c.greet2_x, c.greet2_y))
                    self.__entry_event, self.__previous_entry_event = 'N', 'N'

                for entry_event in 'N', 'e-mail', 'nickname':
                    if self.__entry_event == entry_event:
                        if self.__previous_entry_event == 'N':
                            self.__entry_event = entry_event
                            self.__previous_entry_event = self.__entry_event
                        elif self.__previous_entry_event == 'e-mail' and entry_event != 'N':
                            self.__entry_event = entry_event
                            self.__previous_entry_event = entry_event
                        elif self.__previous_entry_event == 'e-mail' and entry_event == 'N':
                            self.__entry_event = 'e-mail'
                            self.__previous_entry_event = 'e-mail'
                        elif self.__previous_entry_event == 'nickname' and entry_event != 'N':
                            self.__entry_event = entry_event
                            self.__previous_entry_event = entry_event
                        elif self.__previous_entry_event == 'nickname' and entry_event == 'N':
                            self.__entry_event = 'nickname'
                            self.__previous_entry_event = 'nickname'

                self.__e_mail_to_dump = self.__oAccount.oEntryBox1.typing(event, self.__oAccount.mini_ok1_button_rect, self.__mouse_x, self.__mouse_y, self.__entry_event, 'e-mail')
                self.__nickname_to_dump = self.__oAccount.oEntryBox2.typing(event, self.__oAccount.mini_ok2_button_rect, self.__mouse_x, self.__mouse_y, self.__entry_event, 'nickname')

                if self.__e_mail_to_dump is not None:
                    self.account_data['e-mail'] = clean_input(self.__e_mail_to_dump)
                if self.__nickname_to_dump is not None:
                    self.account_data['nickname'] = clean_input(self.__nickname_to_dump)

        #-------------------SETTINGS-----------------#
            if self.__extra_state == 'settings':
                self.__new_extra_state = self.__oSettings.extra_event(event, self.__mouse_x, self.__mouse_y)
                self.__new_extra2_state = self.__oSettings.extra2_event(event, self.__mouse_x, self.__mouse_y)
                if self.__new_extra_state == None:
                    self.__extra_state, self.__menu_touchable = None, True
                if self.__new_extra2_state == 'graphics' and self.__settings_touchable:
                    self.__extra2_state, self.__settings_touchable = 'graphics', False
                if self.__new_extra2_state == 'sound' and self.__settings_touchable:
                    self.__extra2_state, self.__settings_touchable = 'sound', False
                if self.__new_extra2_state == 'help' and self.__settings_touchable:
                    self.__extra2_state, self.__settings_touchable = 'help', False
                if self.__new_extra2_state == 'community' and self.__settings_touchable:
                    self.__extra2_state, self.__settings_touchable = 'community', False

        #------------------COMMUNITY----------------#
            if self.__extra2_state == 'community':
                self.__new_extra2_state = self.__oCommunity.extra2_event(event, self.__mouse_x, self.__mouse_y)
                self.__oCommunity.buttons_event(event, self.__mouse_x, self.__mouse_y)
                if self.__new_extra2_state == None:
                    self.__extra2_state, self.__extra_state = None, 'settings'
                    self.__settings_touchable = True
        
        #------------------GRAPHICS-----------------#
            if self.__extra2_state == 'graphics':
                self.__new_extra2_state = self.__oGraphics.extra2_event(event, self.__mouse_x, self.__mouse_y)
                self.__new_graphics_event = self.__oGraphics.buttons_event(event, self.__mouse_x, self.__mouse_y)
                self.__new2_graphics_event = self.__oGraphics.buttons2_event(event, self.__mouse_x, self.__mouse_y)
                self.__save_event = self.__oGraphics.save_changes(event, self.__mouse_x, self.__mouse_y)
                if self.__new_extra2_state == None:
                    self.__extra2_state, self.__extra_state = None, 'settings'
                    self.__settings_touchable = True
                if self.__new_graphics_event == '1':
                    self.__graphics_event = '1'
                if self.__new_graphics_event == '2':
                    self.__graphics_event = '2'
                if self.__new_graphics_event == '3':
                    self.__graphics_event = '3'
                if self.__new_graphics_event == '4':
                    self.__graphics_event = '4'
                if self.__new2_graphics_event == 'yes':
                    self.__graphics2_event = 'yes'
                if self.__new2_graphics_event == 'no':
                    self.__graphics2_event = 'no'

                if self.__save_event == 'SAVE':
                    if self.__graphics_event == '1':
                        c.width, c.height = (self.__true_width - self.__true_width//10), (self.__true_height - self.__true_height//10)
                        self.data['screen_resolution'] = f'{c.width} {c.height}'
                        self.oData.dump_data('app_data.json', self.data)
                    if self.__graphics_event == '2':
                        c.width, c.height = (self.__true_width - self.__true_width//5), (self.__true_height - self.__true_height//5)
                        self.data['screen_resolution'] = f'{c.width} {c.height}'
                        self.oData.dump_data('app_data.json', self.data)
                    if self.__graphics_event == '3':
                        c.width, c.height = (self.__true_width - self.__true_width//3), (self.__true_height - self.__true_height//3)
                        self.data['screen_resolution'] = f'{c.width} {c.height}'
                        self.oData.dump_data('app_data.json', self.data)
                    if self.__graphics_event == '4':
                        c.width, c.height = self.__true_width, self.__true_height
                        self.data['screen_resolution'] = False
                        self.oData.dump_data('app_data.json', self.data)
                    if self.__graphics2_event == 'no':
                        self.data['smooth'] = False
                        self.oData.dump_data('app_data.json', self.data)
                    if self.__graphics2_event == 'yes':
                        self.data['smooth'] = True
                        self.oData.dump_data('app_data.json', self.data)

        #--------------------HELP-------------------#
            if self.__extra2_state == 'help':
                self.__new_extra2_state = self.__oHelp.extra2_event(event, self.__mouse_x, self.__mouse_y)
                if self.__new_extra2_state == None:
                    self.__extra2_state, self.__extra_state = None, 'settings'
                    self.__settings_touchable = True

        #-------------------SOUNDS------------------#
            if self.__extra2_state == 'sound':
                self.__new_extra2_state = self.__oSounds.extra2_event(event, self.__mouse_x, self.__mouse_y)
                if self.__new_extra2_state == None:
                    self.__extra2_state, self.__extra_state = None, 'settings'
                    self.__settings_touchable = True
        
        #--------------------INFO-------------------#
            if self.__extra_state == 'info':
                self.__new_extra_state = self.__oInfo.extra_event(event, self.__mouse_x, self.__mouse_y)
                self.__oInfo.WebsiteJump(event, self.__mouse_x, self.__mouse_y)
                if self.__new_extra_state == None:
                    self.__menu_touchable, self.__extra_state = True, None
        
        #------------------LOADFILE-----------------#
            if self.__current_state == 'load_file':
                self.__oLoadFile.load_file(event, self.__mouse_x, self.__mouse_y)
                self.__play_process_flag = self.__oLoadFile.open_play_window(event, self.__mouse_x, self.__mouse_y)
                self.songs = self.__oLoadFile.return_song()
                self.songs = {"songs_names": self.songs}
                if self.__play_process_flag:
                    self.oData.dump_data('songs.json', self.songs)
                    open_play()

    def __check_logic(self):
        pass


    def __draw(self):
        if self.__current_state == 'menu':
            self.__oMenu.draw()
            self.__oMenu.check_buttons(self.__mouse_x, self.__mouse_y, menu_touchable=self.__menu_touchable)
            if self.__extra_state == 'account':
                self.__menu_touchable = False
                self.__oAccount.draw()
                self.__oAccount.check_buttons(self.__mouse_x, self.__mouse_y)
            if self.__extra_state == 'settings':
                self.__menu_touchable = False
                self.__oSettings.draw()
                self.__oSettings.check_buttons(self.__mouse_x, self.__mouse_y)
                if self.__extra2_state == 'graphics':
                    self.__settings_touchable = False
                    self.__oGraphics.draw()
                    self.__oGraphics.check_buttons(self.__mouse_x, self.__mouse_y)
                if self.__extra2_state == 'sound':
                    self.__settings_touchable = False
                    self.__oSounds.draw()
                    self.__oSounds.check_buttons(self.__mouse_x, self.__mouse_y)
                if self.__extra2_state == 'help':
                    self.__settings_touchable = False
                    self.__oHelp.draw()
                    self.__oHelp.check_buttons(self.__mouse_x, self.__mouse_y)
                if self.__extra2_state == 'community':
                    self.__settings_touchable = False
                    self.__oCommunity.draw()
                    self.__oCommunity.check_buttons(self.__mouse_x, self.__mouse_y)
            if self.__extra_state == 'info':
                self.__menu_touchable = False
                self.__oInfo.draw()
                self.__oInfo.check_buttons(self.__mouse_x, self.__mouse_y)
        if self.__current_state == 'load_file':
            #self.__menu_touchable = False
            self.__oLoadFile.draw()
            self.__oLoadFile.check_buttons(self.__mouse_x, self.__mouse_y)


        pygame.display.flip()


    def __del__(self):
        close_play()
        pygame.quit()


def close_play():
    global play_process
    if play_process and play_process.is_alive():
        play_process.terminate()
        play_process.join()
        play_process = None

def open_play():
    global play_process
    if play_process is None or not play_process.is_alive():
        oPlayProcess = PlayProcess.PlayProcess()
        play_process = mp.Process(target=oPlayProcess.run)
        play_process.start()