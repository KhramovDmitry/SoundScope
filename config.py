import GetFilePath
import ScreenInfo
import Data
import pygame, gif_pygame

#load.data
oData = Data.Data()
data = oData.load_data(filename='app_data.json')
acc_data = oData.load_data(filename='account_data.json')

screen_resolution = data['screen_resolution']
smooth = data['smooth']

#config.window
oScreenInfo = ScreenInfo.ScreenInfo()
true_width, true_height = oScreenInfo.get_info()
true_width *= 2
true_height *= 2

if data['screen_resolution'] == False:
    width, height = oScreenInfo.get_info()
else:
    width, height = data['screen_resolution'].split()
    width, height = int(width)//2, int(height)//2
Height = height
height -= 62

"""
1. width - width//10, height - height//10
2. width - width//5, height - height//5
3. width - width//3, height - height//3
"""

#config.statement
current_state = 'menu'

#config.classes
oGetFilePath = GetFilePath.GetFilePath()

#config.colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SS_WHITE = (217, 240, 255)
SS_BLUE = (130, 175, 225)
SS_DARKBLUE = (92, 122, 158)
SS_RED = (184, 47, 42)
SS_GREEN = (123, 152, 62)
SS_LIGHTORANGE = (255, 213, 158)
SS_LIGHTRED = (255, 193, 193)
SS_LIGHTGREEN = (228, 255, 170)
SS_LIGHTBLUE = (140, 209, 255)
SS_CDGREEN = (175, 255, 0)
SS_CDYELLOW = (253, 255, 0)
SS_CDORANGE = (255, 145, 0)
SS_CDRED = (255, 0, 4)

#config.fonts
TTC_eb_menu_size = int(width//26.5)*2
TTC_r_menu_size = int(width//69.12)*2
TTC_r_eb_size = int(width//80)*2
TTC_l_error_size = int(width//110)*2
TTC_db_menu_size = int(width//87)*2
TTC_db_community_size = int(width//72*1.2)
TTC_l_community_size = int(width//72*0.95)
TTC_db_graphics_size = int(width//69.12*2.25//1.25)
TTC_eb_cd_size = int(width//69.12*2.4)
TTC_extrabold_path = oGetFilePath.load_file('fonts', 'TTC_extrabold.otf')
TTC_demibold_path = oGetFilePath.load_file('fonts', 'TTC_demibold.otf')
TTC_regular_path = oGetFilePath.load_file('fonts', 'TTC_regular.otf')
TTC_light_path = oGetFilePath.load_file('fonts', 'TTC_light.otf')
TTC_extrabold_menu = pygame.font.Font(TTC_extrabold_path, (TTC_eb_menu_size))
TTC_regular_menu = pygame.font.Font(TTC_regular_path, (TTC_r_menu_size))
TTC_regular_eb = pygame.font.Font(TTC_regular_path, (TTC_r_eb_size))
TTC_light_error = pygame.font.Font(TTC_light_path, (TTC_l_error_size))
TTC_demibold_menu = pygame.font.Font(TTC_demibold_path, (TTC_db_menu_size))
TTC_demibold_community = pygame.font.Font(TTC_demibold_path, (TTC_db_community_size))
TTC_light_community = pygame.font.Font(TTC_light_path, (TTC_l_community_size))
TTC_demibold_graphics = pygame.font.Font(TTC_demibold_path, (TTC_db_graphics_size))
TTC_extrabold_cd = pygame.font.Font(TTC_extrabold_path, (TTC_eb_cd_size))
TTC_demibold_cd = pygame.font.Font(TTC_demibold_path, (TTC_r_menu_size))

#---------------------------------M_E_N_U-------------------------------------------#
menu_bg = oGetFilePath.load_file('sprites', 'bg.png')
#big.buttons
my_playlist_button = oGetFilePath.load_file('sprites', 'my_playlist_button.png')
load_file_button = oGetFilePath.load_file('sprites', 'load_file_button.png')
my_creations_button = oGetFilePath.load_file('sprites', 'my_creations_button.png')
light_button_layer = oGetFilePath.load_file('sprites', 'light_button_layer.png')
#small.buttons
account_button = oGetFilePath.load_file('sprites', 'account_button.png')
settings_button = oGetFilePath.load_file('sprites', 'settings_button.png')
info_button = oGetFilePath.load_file('sprites', 'info_button.png')
escape_button = oGetFilePath.load_file('sprites', 'escape_button.png')
light_button_layer2 = oGetFilePath.load_file('sprites', 'light_button_layer2.png')

waveform = oGetFilePath.load_file('sprites', 'waveform.png')

waveform_size = width, height

mb1_size = width//5.5, width//12.3
mb2_size = width//10.2//2, width//9.6//2

mpb_x, mpb_y = width//2 - width//5.5 - width//43.2, height//2 + height//20
lfb_x, lfb_y = width//2, height//2 + height//20
mcb_x, mcb_y = width//2 + width//5.5 + width//43.2, height//2 + height//20
ab_x, ab_y = width//2 - width//10.2//2 - width//90, height - width//9.6//2 + height//95
sb_x, sb_y = width//2, height - width//9.6//2 + height//95
ib_x, ib_y = width//2 + width//10.2//2 + width//90, height - width//9.6//2 + height//95

escape_button_x, escape_button_y = width//25, width//25

greet_1_text__ = 'SoundScope'
greet_1_text = TTC_extrabold_menu.render(greet_1_text__, smooth, SS_WHITE)
if acc_data['nickname'] == '':
    greet_2_text__ = f'Добро пожаловать!'
else:
    greet_2_text__ = f'С возвращением, {acc_data['nickname']}!'
greet_2_text = TTC_demibold_menu.render(greet_2_text__, smooth, SS_DARKBLUE)

greet1_x, greet1_y = width//2, height//4.6 - height//17
greet2_x, greet2_y = width//2, height//3.2 - height//17

menu_touchable = True
#-----------------------------------------------------------------------------------#

#-----------------------------------A_C_C_O_U_N_T-----------------------------------#

black_layer = oGetFilePath.load_file('sprites', 'black_layer.png')
menu_frame = oGetFilePath.load_file('sprites', 'menu_frame.png')
entry_box = oGetFilePath.load_file('sprites', 'entry_box.png')

mf_x, mf_y = width//2, height//2
eb_size = width//5.2, width//5.2//4.8
eb1_x, eb1_y = width//2, height//2 - height//22
eb2_x, eb2_y = width//2, height//2 + height//14
error1_x, error1_y = width//2, height//2 - height//22 + height//20
error2_x, error2_y = width//2, height//2 + height//14 + height//20

email_flag, nickname_flag, previous_entry_event = 'n', 'n', 'N'

#buttons
mini_exit_button = oGetFilePath.load_file('sprites', 'mini_exit_button.png')
mini_ok_button = oGetFilePath.load_file('sprites', 'mini_ok_button.png')
light_button_layer3 = oGetFilePath.load_file('sprites', 'light_button_layer3.png')

mf_size = width//2.6, height//3.1 + height//30
mini_b_size = width//33, width//33

mf_x, mf_y = width//2, height//2
meb_x, meb_y = (width - width//2.6)//2 + width//24*0.5, height//2 - height//7
mob1_x, mob1_y = (width + width//4.2)//2, height//2 - height//22
mob2_x, mob2_y = (width + width//4.2)//2, height//2 + height//14

account_text__ = 'Аккаунт'
account_text = TTC_regular_menu.render(account_text__, smooth, SS_WHITE)

at_x, at_y = width//2, height//2 - height//6.9
#-----------------------------------------------------------------------------------#

#----------------------------------S_E_T_T_I_N_G_S----------------------------------#
graphics_button = oGetFilePath.load_file('sprites', 'graphics_button.png')
sound_button = oGetFilePath.load_file('sprites', 'sound_button.png')
help_button = oGetFilePath.load_file('sprites', 'help_button.png')
community_button = oGetFilePath.load_file('sprites', 'community_button.png')
gb_layer = oGetFilePath.load_file('sprites', 'graphics_layer.png')
sb_layer = oGetFilePath.load_file('sprites', 'sound_layer.png')
hb_layer = oGetFilePath.load_file('sprites', 'help_layer.png')
cb_layer = oGetFilePath.load_file('sprites', 'community_layer.png')

SB_height = height//31.9 * 2
gb_width, soundbutton_width, hb_width, cb_width = width//14 * 2, width//22 * 2, width//14.5 * 2, width//10.8 * 2

gb_x, gb_y = width//2, height//2 - height//18
soundbutton_x, soundbutton_y = width//2 - width//13, height//2 + height//30
hb_x, hb_y = width//2 + width//20, height//2 + height//30
cb_x, cb_y = width//2, height//2 + height//16 * 2

settings_text__ = 'Настройки'
settings_text = TTC_regular_menu.render(settings_text__, smooth, SS_WHITE)

st_x, st_y = width//2, height//2 - height//6.9

# COMMUNITY
max_button = oGetFilePath.load_file('sprites', 'max_button.png')
telegram_button = oGetFilePath.load_file('sprites', 'telegram_button.png')
community_button_layer = oGetFilePath.load_file('sprites', 'community_button_layer.png')

max_text__ = 'Группа в MAX'
telegram_text__ = 'Канал в Телеграм'
max_text = TTC_demibold_community.render(max_text__, smooth, SS_BLUE)
telegram_text = TTC_demibold_community.render(telegram_text__, smooth, SS_BLUE)
community_text__ = 'Сообщество'
community_text = TTC_regular_menu.render(community_text__, smooth, SS_WHITE)
f_text__ = 'Выходите из полноэкранного режима для перехода по ссылке!'
f_text = TTC_light_community.render(f_text__, smooth, SS_WHITE)

community_text_x, community_text_y = width//2, height//2 - height//6.9
max_text_pos = width//2 - width//15, height//2 - height//80 + height//10 - height//45
telegram_text_pos = width//2 + width//15, height//2 - height//80 + height//10 - height//45
f_text_pos = width//2, height//2 + height//7.2

community_size = width//35*2, width//35*2
max_button_x, max_button_y = width//2 - width//15, height//2 - height//45
telegram_button_x, telegram_button_y = width//2 + width//15, height//2 - height//45

telegram_link = 'https://t.me/SoundScope_news'
max_link = 'https://max.ru/join/-3CCc-oSJwQwymE1Vfd-MMgYGy94BL7PV97Urrwx-JA'

#-----------------------------G_R_A_P_H_I_C_S------------------------------#
graphics_frame = oGetFilePath.load_file('sprites', 'graphics_frame.png')
accept_button = oGetFilePath.load_file('sprites', 'screen_size_button.png')
accept_button_layer = oGetFilePath.load_file('sprites', 'screen_size_layer.png')
screen_resolution_button = oGetFilePath.load_file('sprites', 'pressed_screen_resolution_button.png')
pressed_screen_resolution_button = oGetFilePath.load_file('sprites', 'screen_resolution_button.png')
screen_resolution_layer = oGetFilePath.load_file('sprites', 'screen_resolution_layer.png')

graphics_text__ = 'Графика'
graphics_text = TTC_regular_menu.render(graphics_text__, smooth, SS_WHITE)
screen_resolution_text__ = 'Разрешение окна'
screen_resolution_text = TTC_regular_menu.render(screen_resolution_text__, smooth, SS_WHITE)
textures_text__ = 'Текстуры'
textures_text = TTC_regular_menu.render(textures_text__, smooth, SS_WHITE)

sr1b_text__ = f'{true_width - true_width//10} x {true_height - true_height//10}'
sr2b_text__ = f'{true_width - true_width//5} x {true_height - true_height//5}'
sr3b_text__ = f'{true_width - true_width//3} x {true_height - true_height//3}'
fullscreen_text__ = 'original'

screen_resolutions = [f'{true_width - true_width//10} {true_height - true_height//10}', 
                      f'{true_width - true_width//5} {true_height - true_height//5}', 
                      f'{true_width - true_width//3} {true_height - true_height//3}', 
                      False]

sr1b_text = TTC_demibold_graphics.render(sr1b_text__, smooth, SS_LIGHTORANGE)
sr2b_text = TTC_demibold_graphics.render(sr2b_text__, smooth, SS_LIGHTRED)
sr3b_text = TTC_demibold_graphics.render(sr3b_text__, smooth, SS_LIGHTGREEN)
fullscreen_text = TTC_demibold_graphics.render(fullscreen_text__, smooth, SS_LIGHTBLUE)

b1_image = pressed_screen_resolution_button if screen_resolution == screen_resolutions[0] else screen_resolution_button
b2_image = pressed_screen_resolution_button if screen_resolution == screen_resolutions[1] else screen_resolution_button
b3_image = pressed_screen_resolution_button if screen_resolution == screen_resolutions[2] else screen_resolution_button
b4_image = pressed_screen_resolution_button if screen_resolution == screen_resolutions[3] else screen_resolution_button

b5_image = pressed_screen_resolution_button if smooth else screen_resolution_button
b6_image = screen_resolution_button if smooth else pressed_screen_resolution_button

smooth_yes_text__ = 'Гладкие'
smooth_yes_text = TTC_demibold_graphics.render(smooth_yes_text__, smooth, SS_LIGHTBLUE)
smooth_no_text__ = 'Резкие'
smooth_no_text = TTC_demibold_graphics.render(smooth_no_text__, smooth, SS_LIGHTBLUE)
apply_text__ = 'Применить'
apply_text = TTC_demibold_graphics.render(apply_text__, smooth, SS_WHITE)

reset_text = TTC_light_community.render('Перезапустите программу для просмотра изменений.', smooth, SS_WHITE)

gf_size = width//2.6*1.4, (height//3.1 + height//30) * 1.6
srb_size = width//6.55, height//31.9 * 2
meb2_x, meb2_y = (width - width//2.6)//2 - width//18, height//2 - height//4
gt_x, gt_y = width//2, height//2 - height//4
srt_x, srt_y = width//2, height//2 - height//5.6
tt_x, tt_y = width//2, height//2 + height//20
sr1b_x, sr1b_y = width//2 - width//13, height//2 - height//10
sr2b_x, sr2b_y = width//2 + width//13, height//2 - height//10
sr3b_x, sr3b_y = width//2 - width//13, height//2 - height//30
fb_x, fb_y = width//2 + width//13, height//2 - height//30

syt_x, syt_y = width//2 - width//13, height//2 + height//8.6
snt_x, snt_y = width//2 + width//13, height//2 + height//8.6
ab_pos = width//2, height//2 + height//5

rt_pos = width//2, height//2 + height//3.9
#------------------------------------------------------------------------#

#--------------------------------H_E_L_P---------------------------------#
powered_by_python = oGetFilePath.load_file('sprites', 'pygame_logo.PNG')

help_text__ = 'Помощь'
help_text = TTC_regular_menu.render(help_text__, smooth, SS_WHITE)
support_text = TTC_regular_menu.render('Контакты Тех.Поддержки', smooth, SS_WHITE)
gmail_text = TTC_demibold_community.render('soundscopehelp@gmail.com', smooth, SS_BLUE)

supt_x, supt_y = width//2, height//2 - height//18
gmailt_x, gmailt_y = width//2, height//2

pbp_size = width//15.36, height//25.1
pbp_pos = width//2 + width//6.5, height//2 + height//7
#------------------------------------------------------------------------#

#-------------------------------S_O_U_N_D_S------------------------------#
sounds_text = TTC_regular_menu.render('Звук', smooth, SS_WHITE)
on_text = '×'


#---------------------------------I_N_F_O--------------------------------#
website_button = oGetFilePath.load_file('sprites', 'website_button.png')

info_text__ = 'Информация'
info_text = TTC_regular_menu.render(info_text__, smooth, SS_WHITE)
website_text__ = 'Сайт с информацией'
website_text = TTC_demibold_community.render(website_text__, smooth, SS_BLUE)
info_path = oGetFilePath.load_htmlfile('index.html')

it_x, it_y = width//2, height//2 - height//6.9
wt_x, wt_y = width//2, height//2 - height//80 + height//10 - height//45

website_size = width//30*2, width//30*2
website_pos = width//2, height//2 - height//50
#------------------------------------------------------------------------#

#----------------------------L_O_A_D_F_I_L_E-----------------------------#
choose_file_button = oGetFilePath.load_file('sprites', 'choose_file_button.png')
choose_file_layer = oGetFilePath.load_file('sprites', 'choose_file_layer.png')
error_cover = oGetFilePath.load_file('sprites', 'error_cover.png')
cover_layer = oGetFilePath.load_file('sprites', 'cover_layer.png')
listen_file_button = oGetFilePath.load_file('sprites', 'listen_file_button.png')
add_song_button = oGetFilePath.load_file('sprites', 'add_song_button.png')
check_data_button = oGetFilePath.load_file('sprites', 'check_data_button.png')
file_button_layer = oGetFilePath.load_file('sprites', 'file_button_layer.png')

SS_LOADING_GIF = gif_pygame.load(oGetFilePath.load_file('sprites', 'SS_LOADING_GIF.gif'))
current_frame = SS_LOADING_GIF.blit_ready()
gif_width, gif_height = current_frame.get_width(), current_frame.get_height()

file_button_size = [width//5.5, width//5.5//2.5]
fb1_pos = [width//2 - width//5, height//2 + height//8]
fb2_pos = [width//2, height//2 + height//8]
fb3_pos = [width//2 + width//5, height//2 + height//8]

cfb_x, cfb_y = width//2, height//2
cfb_width, cfb_height = width//5.5, height//7.2

#check.data
cd_glow_1 = oGetFilePath.load_file('sprites', 'cd_glow_1.png')
cd_glow_2 = oGetFilePath.load_file('sprites', 'cd_glow_2.png')

music_data_text = TTC_extrabold_cd.render('Музыкальные данные', smooth, (0, 152, 255))
metadata_text = TTC_extrabold_cd.render('Метаданные', smooth, (255, 103, 105))
bpm_text = TTC_demibold_cd.render('Темп:', smooth, SS_LIGHTBLUE)
ac_bpm_text = TTC_demibold_cd.render('Точный темп:', smooth, SS_LIGHTBLUE)
key_text = TTC_demibold_cd.render('Тональность:', smooth, SS_LIGHTBLUE)
strength_text = TTC_demibold_cd.render('Точность предоставленных данных:', smooth, SS_LIGHTBLUE)

#-----------------#
play_process = None
play_button = oGetFilePath.load_file('sprites', 'play_button.png')
pause_button = oGetFilePath.load_file('sprites', 'pause_button.png')
song_frame = oGetFilePath.load_file('sprites', 'song_frame.png')
glow_1 = oGetFilePath.load_file('sprites', 'glow_1.png')
glow_2 = oGetFilePath.load_file('sprites', 'glow_2.png')
#-----------------#