#!/usr/bin/env python

"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2015 David Howland, All rights reserved.

"""

description = "Atreus"
unique_id = "ATREUS_001"
firmware = "ATREUS"

display_height = int(4*4)
display_width = int(12*4)

num_rows = 4
num_cols = 11
num_leds = 0

uc_size = 'large'

#autogen start
layers_map = 0x00000562

actions_map = 0x000003aa

tapkeys_map = 0x000001f2

macro_map = 0x0000071a

led_map = 0x0000171a
bl_mask_map = None

pw_defs_map = 0x0000174b

led_hw_map = 0x0000172a
row_hw_map = 0x00001743
col_hw_map = 0x0000172d
#autogen finish

led_definition = [
    ('A* LED 13', 'Caps Lock')
]

backlighting = False

keyboard_definition = [
    [((4, 4), (0, 0), 'HID_KEYBOARD_SC_Q'),
     ((4, 4), (0, 1), 'HID_KEYBOARD_SC_W'),
     ((4, 4), (0, 2), 'HID_KEYBOARD_SC_E'),
     ((4, 4), (0, 3), 'HID_KEYBOARD_SC_R'),
     ((4, 4), (0, 4), 'HID_KEYBOARD_SC_T'),
     (4, None, '0'),
     (4, None, '0'),
     ((4, 4), (0, 6), 'HID_KEYBOARD_SC_Y'),
     ((4, 4), (0, 7), 'HID_KEYBOARD_SC_U'),
     ((4, 4), (0, 8), 'HID_KEYBOARD_SC_I'),
     ((4, 4), (0, 9), 'HID_KEYBOARD_SC_O'),
     ((4, 4), (0, 10), 'HID_KEYBOARD_SC_P')],

    [((4, 4), (1, 0), 'HID_KEYBOARD_SC_A'),
     ((4, 4), (1, 1), 'HID_KEYBOARD_SC_S'),
     ((4, 4), (1, 2), 'HID_KEYBOARD_SC_D'),
     ((4, 4), (1, 3), 'HID_KEYBOARD_SC_F'),
     ((4, 4), (1, 4), 'HID_KEYBOARD_SC_G'),
     (4, None, '0'),
     (4, None, '0'),
     ((4, 4), (1, 6), 'HID_KEYBOARD_SC_H'),
     ((4, 4), (1, 7), 'HID_KEYBOARD_SC_J'),
     ((4, 4), (1, 8), 'HID_KEYBOARD_SC_K'),
     ((4, 4), (1, 9), 'HID_KEYBOARD_SC_L'),
     ((4, 4), (1, 10), 'HID_KEYBOARD_SC_SEMICOLON_AND_COLON')],

    [((4, 4), (2, 0), 'HID_KEYBOARD_SC_Z'),
     ((4, 4), (2, 1), 'HID_KEYBOARD_SC_X'),
     ((4, 4), (2, 2), 'HID_KEYBOARD_SC_C'),
     ((4, 4), (2, 3), 'HID_KEYBOARD_SC_V'),
     ((4, 4), (2, 4), 'HID_KEYBOARD_SC_B'),
     (4, None, '0'),
     (4, None, '0'),
     ((4, 4), (2, 6), 'HID_KEYBOARD_SC_N'),
     ((4, 4), (2, 7), 'HID_KEYBOARD_SC_M'),
     ((4, 4), (2, 8), 'HID_KEYBOARD_SC_COMMA_AND_LESS_THAN_SIGN'),
     ((4, 4), (2, 9), 'HID_KEYBOARD_SC_DOT_AND_GREATER_THAN_SIGN'),
     ((4, 4), (2, 10), 'HID_KEYBOARD_SC_SLASH_AND_QUESTION_MARK')],

    [((4, 4), (3, 0), 'HID_KEYBOARD_SC_ESCAPE'),
     ((4, 4), (3, 1), 'HID_KEYBOARD_SC_TAB'),
     ((4, 4), (3, 2), 'HID_KEYBOARD_SC_LEFT_GUI'),
     ((4, 4), (3, 3), 'HID_KEYBOARD_SC_LEFT_SHIFT'),
     ((4, 4), (3, 4), 'HID_KEYBOARD_SC_BACKSPACE'),
     ((4, -6), (3, 5), 'HID_KEYBOARD_SC_LEFT_CONTROL'),
     ((4, -6), (2, 5), 'HID_KEYBOARD_SC_RIGHT_ALT'),
     ((4, 4), (3, 6), 'HID_KEYBOARD_SC_SPACE'),
     ((4, 4), (3, 7), 'SCANCODE_FN'),
     ((4, 4), (3, 8), 'HID_KEYBOARD_SC_EQUAL_AND_PLUS'),
     ((4, 4), (3, 9), 'HID_KEYBOARD_SC_APOSTROPHE_AND_QUOTE'),
     ((4, 4), (3, 10), 'HID_KEYBOARD_SC_ENTER')]
]

alt_layouts = {}

if __name__ == '__main__':
    print("Keyboard definition for JD45 keyboard")
