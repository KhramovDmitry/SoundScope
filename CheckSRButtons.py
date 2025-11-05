import config as c
import Data, Button
from LoadImage import load_image

def check_sr_buttons(b1: Button.Button, 
                     b2: Button.Button, 
                     b3: Button.Button, 
                     b4: Button.Button,
                     b5: Button.Button, 
                     b6: Button.Button,
                     answer: str
                     ):

    if answer == '1':
        b1.button_image = load_image(c.pressed_screen_resolution_button, c.smooth, (b1.width, b1.height))
        b2.button_image = load_image(c.screen_resolution_button, c.smooth, (b2.width, b2.height))
        b3.button_image = load_image(c.screen_resolution_button, c.smooth, (b3.width, b3.height))
        b4.button_image = load_image(c.screen_resolution_button, c.smooth, (b4.width, b4.height))
    elif answer == '2':
        b1.button_image = load_image(c.screen_resolution_button, c.smooth, (b1.width, b1.height))
        b2.button_image = load_image(c.pressed_screen_resolution_button, c.smooth, (b2.width, b2.height))
        b3.button_image = load_image(c.screen_resolution_button, c.smooth, (b3.width, b3.height))
        b4.button_image = load_image(c.screen_resolution_button, c.smooth, (b4.width, b4.height))
    elif answer == '3':
        b1.button_image = load_image(c.screen_resolution_button, c.smooth, (b1.width, b1.height))
        b2.button_image = load_image(c.screen_resolution_button, c.smooth, (b2.width, b2.height))
        b3.button_image = load_image(c.pressed_screen_resolution_button, c.smooth, (b3.width, b3.height))
        b4.button_image = load_image(c.screen_resolution_button, c.smooth, (b4.width, b4.height))
    elif answer == '4':
        b1.button_image = load_image(c.screen_resolution_button, c.smooth, (b1.width, b1.height))
        b2.button_image = load_image(c.screen_resolution_button, c.smooth, (b2.width, b2.height))
        b3.button_image = load_image(c.screen_resolution_button, c.smooth, (b3.width, b3.height))
        b4.button_image = load_image(c.pressed_screen_resolution_button, c.smooth, (b4.width, b4.height))
    elif answer == 'yes':
        b5.button_image = load_image(c.pressed_screen_resolution_button, c.smooth, (b5.width, b5.height))
        b6.button_image = load_image(c.screen_resolution_button, c.smooth, (b6.width, b6.height))
    else:
        b5.button_image = load_image(c.screen_resolution_button, c.smooth, (b5.width, b5.height))
        b6.button_image = load_image(c.pressed_screen_resolution_button, c.smooth, (b6.width, b6.height))