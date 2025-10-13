import GetFilePath
import ScreenInfo
import Data
import pygame

#load.data
oData = Data.Data()
data = oData.load_data(filename='app_data.json')
acc_data = oData.load_data(filename='account_data.json')

#config.window
oScreenInfo = ScreenInfo.ScreenInfo()
width, height = oScreenInfo.get_info()
#width, height = width//2, height//2
Height = height
height -= 62

#config.statement
current_state = 'menu'

#config.classes
oGetFilePath = GetFilePath.GetFilePath()

#config.colors
SS_WHITE = (217, 240, 255)
SS_BLUE = (130, 175, 225)
SS_DARKBLUE = (92, 122, 158)
SS_RED = (184, 47, 42)
SS_GREEN = (123, 152, 62)

#config.fonts
TTC_eb_menu_size = int(width//26.5)*2
TTC_r_menu_size = int(width//69.12)*2
TTC_r_eb_size = int(width//80)*2
TTC_l_error_size = int(width//110)*2
TTC_db_menu_size = int(width//87)*2
TTC_db_community_size = int(width//72*1.2)
TTC_l_community_size = int(width//72*0.95)
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
light_button_layer2 = oGetFilePath.load_file('sprites', 'light_button_layer2.png')

waveform = oGetFilePath.load_file('sprites', 'waveform.png')

waveform_size = width, height

mb1_size = width//5.5, width//5.5//1.6
mb2_size = width//10.2//2, width//9.6//2

mpb_x, mpb_y = width//2 - width//5.5 - width//43.2, height//2 + height//20
lfb_x, lfb_y = width//2, height//2 + height//20
mcb_x, mcb_y = width//2 + width//5.5 + width//43.2, height//2 + height//20
ab_x, ab_y = width//2 - width//10.2//2 - width//90, height - width//9.6//2 + height//95
sb_x, sb_y = width//2, height - width//9.6//2 + height//95
ib_x, ib_y = width//2 + width//10.2//2 + width//90, height - width//9.6//2 + height//95

greet_1_text__ = 'SoundScope'
greet_1_text = TTC_extrabold_menu.render(greet_1_text__, True, SS_WHITE)
if acc_data['nickname'] == '':
    greet_2_text__ = f'Добро пожаловать!'
else:
    greet_2_text__ = f'С возвращением, {acc_data['nickname']}!'
greet_2_text = TTC_demibold_menu.render(greet_2_text__, True, SS_DARKBLUE)

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
account_text = TTC_regular_menu.render(account_text__, True, SS_WHITE)

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
settings_text = TTC_regular_menu.render(settings_text__, True, SS_WHITE)

st_x, st_y = width//2, height//2 - height//6.9

# GRAPHICS
max_button = oGetFilePath.load_file('sprites', 'max_button.png')
telegram_button = oGetFilePath.load_file('sprites', 'telegram_button.png')
community_button_layer = oGetFilePath.load_file('sprites', 'community_button_layer.png')

max_text__ = 'Группа в MAX'
telegram_text__ = 'Канал в Телеграм'
max_text = TTC_demibold_community.render(max_text__, True, SS_BLUE)
telegram_text = TTC_demibold_community.render(telegram_text__, True, SS_BLUE)
community_text__ = 'Сообщество'
community_text = TTC_regular_menu.render(community_text__, True, SS_WHITE)
f_text__ = 'Выходите из полноэкранного режима для перехода по ссылке!'
f_text = TTC_light_community.render(f_text__, True, SS_WHITE)

community_text_x, community_text_y = width//2, height//2 - height//6.9
max_text_pos = width//2 - width//15, height//2 - height//80 + height//10 - height//45
telegram_text_pos = width//2 + width//15, height//2 - height//80 + height//10 - height//45
f_text_pos = width//2, height//2 + height//7.2

community_size = width//35*2, width//35*2
max_button_x, max_button_y = width//2 - width//15, height//2 - height//45
telegram_button_x, telegram_button_y = width//2 + width//15, height//2 - height//45

telegram_link = 'https://t.me/SoundScope_news'
max_link = 'https://max.ru/join/-3CCc-oSJwQwymE1Vfd-MMgYGy94BL7PV97Urrwx-JA'
#------------------------------------------------------------------------#

#----------------------------------INFO----------------------------------#
website_button = oGetFilePath.load_file('sprites', 'website_button.png')

info_text__ = 'Информация'
info_text = TTC_regular_menu.render(info_text__, True, SS_WHITE)
website_text__ = 'Сайт с информацией'
website_text = TTC_demibold_community.render(website_text__, True, SS_BLUE)
info_path = oGetFilePath.load_htmlfile('index.html')

it_x, it_y = width//2, height//2 - height//6.9
wt_x, wt_y = width//2, height//2 - height//80 + height//10 - height//45

website_size = width//30*2, width//30*2
website_pos = width//2, height//2 - height//50