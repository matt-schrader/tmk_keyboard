#!/usr/bin/env python

"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2015 David Howland, All rights reserved.

"""

description = "CM Tester (SixShooter)"
unique_id = "SIXSHOOTER_001"
firmware = "SIXSHOOTER"

display_height = int(2*4)
display_width = int(3*4)

num_rows = 1
num_cols = 6
num_leds = 3

uc_size = 'large'

#autogen start
layers_map = 0x00000138

actions_map = 0x000000fc

tapkeys_map = 0x000000c0

macro_map = 0x00000174

led_map = 0x00001186
bl_mask_map = 0x00001180

pw_defs_map = None

led_hw_map = 0x00001196
row_hw_map = 0x000011b4
col_hw_map = 0x000011a8
#autogen finish

led_definition = [
    ('Top Left', 'Backlight'),
    ('Top Middle', 'Backlight'),
    ('Top Right', 'Backlight'),
    ('Bottom Left', 'Backlight'),
    ('Bottom Middle', 'Backlight'),
    ('Bottom Right', 'Backlight')
]

backlighting = True

keyboard_definition = [
    [((4, 4), (0, 2), 'SCANCODE_MUTE'),
     ((4, 4), (0, 1), 'SCANCODE_VOL_DEC'),
     ((4, 4), (0, 0), 'SCANCODE_VOL_INC')],

    [((4, 4), (0, 5), 'SCANCODE_PREV_TRACK'),
     ((4, 4), (0, 4), 'SCANCODE_PLAY_PAUSE'),
     ((4, 4), (0, 3), 'SCANCODE_NEXT_TRACK')],
]

alt_layouts = {}

if __name__ == '__main__':
    print("Keyboard definition for the CM Storm switch tester")
