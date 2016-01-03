#!/usr/bin/env python

"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2014 David Howland, All rights reserved.

"""

description = "JD45"
unique_id = "JD45_001"
firmware = "JD45"

display_height = int(4*4)
display_width = int(13*4)

num_rows = 4
num_cols = 12
num_leds = 1

uc_size = 'large'

#autogen start
layers_map = 0x000005b2

actions_map = 0x000003d2

tapkeys_map = 0x000001f2

macro_map = 0x00000792

led_map = 0x00001795
bl_mask_map = 0x00001794

pw_defs_map = 0x000017c8

led_hw_map = 0x000017a5
row_hw_map = 0x000017c0
col_hw_map = 0x000017a8
#autogen finish

led_definition = [
    ('LED1', 'Backlight')
]

backlighting = True

keyboard_definition = [
    [((4, 4), (0, 0), 'HID_KEYBOARD_SC_TAB'),
     ((4, 4), (0, 1), 'HID_KEYBOARD_SC_Q'),
     ((4, 4), (0, 2), 'HID_KEYBOARD_SC_W'),
     ((4, 4), (0, 3), 'HID_KEYBOARD_SC_E'),
     ((4, 4), (0, 4), 'HID_KEYBOARD_SC_R'),
     ((4, 4), (0, 5), 'HID_KEYBOARD_SC_T'),
     ((4, 4), (0, 6), 'HID_KEYBOARD_SC_Y'),
     ((4, 4), (0, 7), 'HID_KEYBOARD_SC_U'),
     ((4, 4), (0, 8), 'HID_KEYBOARD_SC_I'),
     ((4, 4), (0, 9), 'HID_KEYBOARD_SC_O'),
     ((4, 4), (0, 10), 'HID_KEYBOARD_SC_P'),
     ((4, 4), (0, 11), 'HID_KEYBOARD_SC_OPENING_BRACKET_AND_OPENING_BRACE'),
     ((4, 4), (3, 11), 'HID_KEYBOARD_SC_CLOSING_BRACKET_AND_CLOSING_BRACE')],

    [((5, 4), (1, 0), 'HID_KEYBOARD_SC_CAPS_LOCK'),
     ((4, 4), (1, 1), 'HID_KEYBOARD_SC_A'),
     ((4, 4), (1, 2), 'HID_KEYBOARD_SC_S'),
     ((4, 4), (1, 3), 'HID_KEYBOARD_SC_D'),
     ((4, 4), (1, 4), 'HID_KEYBOARD_SC_F'),
     ((4, 4), (1, 5), 'HID_KEYBOARD_SC_G'),
     ((4, 4), (1, 6), 'HID_KEYBOARD_SC_H'),
     ((4, 4), (1, 7), 'HID_KEYBOARD_SC_J'),
     ((4, 4), (1, 8), 'HID_KEYBOARD_SC_K'),
     ((4, 4), (1, 9), 'HID_KEYBOARD_SC_L'),
     ((4, 4), (1, 10), 'HID_KEYBOARD_SC_SEMICOLON_AND_COLON'),
     ((7, 4), (1, 11), 'HID_KEYBOARD_SC_APOSTROPHE_AND_QUOTE')],

    [((7, 4), (2, 0), 'HID_KEYBOARD_SC_LEFT_SHIFT'),
     ((4, 4), (2, 1), 'HID_KEYBOARD_SC_Z'),
     ((4, 4), (2, 2), 'HID_KEYBOARD_SC_X'),
     ((4, 4), (2, 3), 'HID_KEYBOARD_SC_C'),
     ((4, 4), (2, 4), 'HID_KEYBOARD_SC_V'),
     ((4, 4), (2, 5), 'HID_KEYBOARD_SC_B'),
     ((4, 4), (2, 6), 'HID_KEYBOARD_SC_N'),
     ((4, 4), (2, 7), 'HID_KEYBOARD_SC_M'),
     ((4, 4), (2, 8), 'HID_KEYBOARD_SC_COMMA_AND_LESS_THAN_SIGN'),
     ((4, 4), (2, 9), 'HID_KEYBOARD_SC_DOT_AND_GREATER_THAN_SIGN'),
     ((4, 4), (2, 10), 'HID_KEYBOARD_SC_SLASH_AND_QUESTION_MARK'),
     ((5, 4), (2, 11), 'HID_KEYBOARD_SC_RIGHT_SHIFT')],

    [((5, 4), (3, 0), 'HID_KEYBOARD_SC_LEFT_CONTROL'),
     ((4, 4), (3, 1), 'SCANCODE_FN'),
     ((5, 4), (3, 2), 'HID_KEYBOARD_SC_LEFT_GUI'),
     ((5, 4), (3, 3), 'HID_KEYBOARD_SC_LEFT_ALT'),
     ((7, 4), (3, 4), 'HID_KEYBOARD_SC_SPACE'),
     ((7, 4), (3, 6), 'HID_KEYBOARD_SC_SPACE'),
     ((5, 4), (3, 7), 'HID_KEYBOARD_SC_RIGHT_ALT'),
     ((5, 4), (3, 8), 'HID_KEYBOARD_SC_APPLICATION'),
     ((4, 4), (3, 9), 'SCANCODE_FN2'),
     ((5, 4), (3, 10), 'HID_KEYBOARD_SC_RIGHT_CONTROL')]
]

alt_layouts = {}

if __name__ == '__main__':
    print("Keyboard definition for JD45 keyboard")
