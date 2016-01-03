#!/usr/bin/env python

"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2014 David Howland, All rights reserved.

"""

description = "Techkeys Card"
unique_id = "TECHCARD_001"
firmware = "TECHCARD"

macro_length = 512

display_height = int(2*4)
display_width = int(4*4)

num_rows = 1
num_cols = 3
num_leds = 1

uc_size = 'small'

#autogen start
layers_map = 0x000000c4

actions_map = 0x000000a6

tapkeys_map = 0x00000088

macro_map = 0x000000e2

led_map = 0x000004ee
bl_mask_map = 0x000004ea

pw_defs_map = None

led_hw_map = 0x000004fe
row_hw_map = 0x00000510
col_hw_map = 0x0000050a
#autogen finish

led_definition = [
    ('Corner', 'Fn Lock')
]

backlighting = True

keyboard_definition = [
    [(4, None, '0'),
     ((4, 4), (0, 0), 'SCANCODE_BROWSER'),
     ((4, 4), (0, 1), 'SCANCODE_MAIL'),
     ((4, 4), (0, 2), 'SCANCODE_MEDIA')],

    [(4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (4, None, '0')]
]

alt_layouts = {}

if __name__ == '__main__':
    print("Keyboard definition for the Techkeys card")
