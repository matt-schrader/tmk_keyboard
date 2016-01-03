#!/usr/bin/env python

"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2013 David Howland, All rights reserved.

"""

description = "GHpad"
unique_id = "GHPAD_001"
firmware = "GHPAD"

display_height = int(6*4)
display_width = int(4*4)

num_rows = 6
num_cols = 4
num_leds = 4

uc_size = 'large'

#autogen start
layers_map = 0x000003d2

actions_map = 0x000002e2

tapkeys_map = 0x000001f2

macro_map = 0x000004c2

led_map = 0x000014c2
bl_mask_map = None

pw_defs_map = 0x000014f2

led_hw_map = 0x000014d2
row_hw_map = 0x000014e6
col_hw_map = 0x000014de
#autogen finish

led_definition = [
    ('Num', 'Num Lock'),
    ('Top 1', 'Fn Lock'),
    ('Top 2', 'Unassigned'),
    ('Top 3', 'Unassigned')
]

backlighting = False

keyboard_definition = [
    [((4, 4), (0, 0), 'HID_KEYBOARD_SC_NUM_LOCK'),
     ((4, 4), (0, 1), 'HID_KEYBOARD_SC_KEYPAD_SLASH'),
     ((4, 4), (0, 2), 'HID_KEYBOARD_SC_KEYPAD_ASTERISK'),
     ((4, 4), (0, 3), 'HID_KEYBOARD_SC_KEYPAD_MINUS')],

    [((4, 4), (1, 0), 'HID_KEYBOARD_SC_KEYPAD_7_AND_HOME'),
     ((4, 4), (1, 1), 'HID_KEYBOARD_SC_KEYPAD_8_AND_UP_ARROW'),
     ((4, 4), (1, 2), 'HID_KEYBOARD_SC_KEYPAD_9_AND_PAGE_UP'),
     ((4, 4), (1, 3), 'HID_KEYBOARD_SC_KEYPAD_PLUS')],

    [((4, 4), (2, 0), 'HID_KEYBOARD_SC_KEYPAD_4_AND_LEFT_ARROW'),
     ((4, 4), (2, 1), 'HID_KEYBOARD_SC_KEYPAD_5'),
     ((4, 4), (2, 2), 'HID_KEYBOARD_SC_KEYPAD_6_AND_RIGHT_ARROW'),
     ((4, 4), (2, 3), '0')],

    [((4, 4), (3, 0), 'HID_KEYBOARD_SC_KEYPAD_1_AND_END'),
     ((4, 4), (3, 1), 'HID_KEYBOARD_SC_KEYPAD_2_AND_DOWN_ARROW'),
     ((4, 4), (3, 2), 'HID_KEYBOARD_SC_KEYPAD_3_AND_PAGE_DOWN'),
     ((4, 4), (3, 3), 'HID_KEYBOARD_SC_KEYPAD_ENTER')],

    [((4, 4), (4, 0), 'HID_KEYBOARD_SC_KEYPAD_0_AND_INSERT'),
     ((4, 4), (4, 1), 'HID_KEYBOARD_SC_UP_ARROW'),
     ((4, 4), (4, 2), 'HID_KEYBOARD_SC_KEYPAD_DOT_AND_DELETE'),
     ((4, 4), (4, 3), '0')],

    [((4, 4), (5, 0), 'HID_KEYBOARD_SC_LEFT_ARROW'),
     ((4, 4), (5, 1), 'HID_KEYBOARD_SC_DOWN_ARROW'),
     ((4, 4), (5, 2), 'HID_KEYBOARD_SC_RIGHT_ARROW'),
     ((4, 4), (5, 3), 'SCANCODE_FN')]
]

alt_layouts = {}

if __name__ == '__main__':
    print("Keyboard definition for GHpad numpad")
