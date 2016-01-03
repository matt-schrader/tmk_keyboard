#!/usr/bin/env python

"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2013 David Howland, All rights reserved.

"""

description = "Tau (Qazpad)"
unique_id = "TAU_002"
firmware = "TAU"

display_height = int(6.25*4)
display_width = int(6.25*4)

num_rows = 6
num_cols = 6
num_leds = 2

uc_size = 'large'

#autogen start
layers_map = 0x000004c2

actions_map = 0x0000035a

tapkeys_map = 0x000001f2

macro_map = 0x0000062a

led_map = 0x00001643
bl_mask_map = 0x0000163e

pw_defs_map = 0x0000167a

led_hw_map = 0x00001653
row_hw_map = 0x0000166e
col_hw_map = 0x00001662
#autogen finish

led_definition = [
    ('Top Left', 'Fn Lock'),
    ('Num', 'Num Lock')
]

backlighting = True

keyboard_definition = [
    [((4, 4), (0, 0), 'HID_KEYBOARD_SC_ESCAPE'),
     ((4, 4), (0, 1), 'SCANCODE_FN'),
     (1, None, '0'),
     ((4, 4), (0, 2), 'HID_KEYBOARD_SC_HOME'),
     ((4, 4), (0, 3), 'HID_KEYBOARD_SC_END'),
     ((4, 4), (0, 4), 'HID_KEYBOARD_SC_DELETE'),
     ((4, 4), (0, 5), 'HID_KEYBOARD_SC_BACKSPACE')],

    1,

    [((4, 4), (1, 0), 'HID_KEYBOARD_SC_A'),
     ((4, 4), (1, 1), 'HID_KEYBOARD_SC_B'),
     (1, None, '0'),
     ((4, 4), (1, 2), 'HID_KEYBOARD_SC_NUM_LOCK'),
     ((4, 4), (1, 3), 'HID_KEYBOARD_SC_KEYPAD_SLASH'),
     ((4, 4), (1, 4), 'HID_KEYBOARD_SC_KEYPAD_ASTERISK'),
     ((4, 4), (1, 5), 'HID_KEYBOARD_SC_KEYPAD_MINUS')],

    [((4, 4), (2, 0), 'HID_KEYBOARD_SC_C'),
     ((4, 4), (2, 1), 'HID_KEYBOARD_SC_D'),
     (1, None, '0'),
     ((4, 4), (2, 2), 'HID_KEYBOARD_SC_KEYPAD_7_AND_HOME'),
     ((4, 4), (2, 3), 'HID_KEYBOARD_SC_KEYPAD_8_AND_UP_ARROW'),
     ((4, 4), (2, 4), 'HID_KEYBOARD_SC_KEYPAD_9_AND_PAGE_UP'),
     ((4, 8), (3, 5), 'HID_KEYBOARD_SC_KEYPAD_PLUS')],

    [((4, 4), (3, 0), 'HID_KEYBOARD_SC_E'),
     ((4, 4), (3, 1), 'HID_KEYBOARD_SC_F'),
     (1, None, '0'),
     ((4, 4), (3, 2), 'HID_KEYBOARD_SC_KEYPAD_4_AND_LEFT_ARROW'),
     ((4, 4), (3, 3), 'HID_KEYBOARD_SC_KEYPAD_5'),
     ((4, 4), (3, 4), 'HID_KEYBOARD_SC_KEYPAD_6_AND_RIGHT_ARROW'),
     (-4, None, '0')],

    [((4, 8), (4, 0), 'HID_KEYBOARD_SC_SPACE'),
     ((4, 8), (4, 1), 'HID_KEYBOARD_SC_TAB'),
     (1, None, '0'),
     ((4, 4), (4, 2), 'HID_KEYBOARD_SC_KEYPAD_1_AND_END'),
     ((4, 4), (4, 3), 'HID_KEYBOARD_SC_KEYPAD_2_AND_DOWN_ARROW'),
     ((4, 4), (4, 4), 'HID_KEYBOARD_SC_KEYPAD_3_AND_PAGE_DOWN'),
     ((4, 8), (5, 5), 'HID_KEYBOARD_SC_KEYPAD_ENTER')],

    [(-8, None, '0'),
     (1, None, '0'),
     ((8, 4), (5, 3), 'HID_KEYBOARD_SC_KEYPAD_0_AND_INSERT'),
     ((4, 4), (5, 4), 'HID_KEYBOARD_SC_KEYPAD_DOT_AND_DELETE'),
     (-4, None, '0')]
]

alt_layouts = {}

if __name__ == '__main__':
    print("Keyboard definition for Tau keyboard")
