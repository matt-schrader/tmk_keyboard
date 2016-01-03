#!/usr/bin/env python

"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2013 David Howland, All rights reserved.

"""

description = "ErgoDox"
unique_id = "ERGODOX_001"
firmware = "ERGODOX"

display_height = int(6*4)
display_width = int(19.5*4)

num_rows = 6
num_cols = 6

#autogen start
address_map = {
    "LAYER0": 0x0000084a,
    "LAYER1": 0x00000826,
    "LAYER2": 0x00000802,
    "LAYER3": 0x000007de,
    "LAYER4": 0x000007ba,
    "LAYER5": 0x00000796,
    "LAYER6": 0x00000772,
    "LAYER7": 0x0000074e,
    "LAYER8": 0x0000072a,
    "LAYER9": 0x00000706
}

fn_action_map = 0x000006e8
fn_mode_map = 0x000006d6

mod_action_map = 0x000006e0
mod_mode_map = 0x000006ce

macro_map = 0x0000086e
#autogen finish

keyboard_definition = [
    [((6, 4), None, 'HID_KEYBOARD_SC_EQUAL_AND_PLUS'),
     ((4, 4), None, 'HID_KEYBOARD_SC_1_AND_EXCLAMATION'),
     ((4, 4), None, 'HID_KEYBOARD_SC_2_AND_AT'),
     ((4, 4), None, 'HID_KEYBOARD_SC_3_AND_HASHMARK'),
     ((4, 4), None, 'HID_KEYBOARD_SC_4_AND_DOLLAR'),
     ((4, 4), None, 'HID_KEYBOARD_SC_5_AND_PERCENTAGE'),
     ((4, 4), None, 'HID_KEYBOARD_SC_ESCAPE'),
     (4, None, '0'),
     (4, None, '0'),
     (2, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     ((4, 4), None, 'HID_KEYBOARD_SC_NUM_LOCK'),
     ((4, 4), None, 'HID_KEYBOARD_SC_6_AND_CARET'),
     ((4, 4), None, 'HID_KEYBOARD_SC_7_AND_AND_AMPERSAND'),
     ((4, 4), None, 'HID_KEYBOARD_SC_8_AND_ASTERISK'),
     ((4, 4), None, 'HID_KEYBOARD_SC_9_AND_OPENING_PARENTHESIS'),
     ((4, 4), None, 'HID_KEYBOARD_SC_0_AND_CLOSING_PARENTHESIS'),
     ((6, 4), None, 'HID_KEYBOARD_SC_MINUS_AND_UNDERSCORE')],

    [((6, 4), None, 'HID_KEYBOARD_SC_BACKSLASH_AND_PIPE'),
     ((4, 4), None, 'HID_KEYBOARD_SC_Q'),
     ((4, 4), None, 'HID_KEYBOARD_SC_W'),
     ((4, 4), None, 'HID_KEYBOARD_SC_E'),
     ((4, 4), None, 'HID_KEYBOARD_SC_R'),
     ((4, 4), None, 'HID_KEYBOARD_SC_T'),
     ((4, 6), None, 'SCANCODE_FN'),
     (4, None, '0'),
     (4, None, '0'),
     (2, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     ((4, 6), None, 'HID_KEYBOARD_SC_OPENING_BRACKET_AND_OPENING_BRACE'),
     ((4, 4), None, 'HID_KEYBOARD_SC_Y'),
     ((4, 4), None, 'HID_KEYBOARD_SC_U'),
     ((4, 4), None, 'HID_KEYBOARD_SC_I'),
     ((4, 4), None, 'HID_KEYBOARD_SC_O'),
     ((4, 4), None, 'HID_KEYBOARD_SC_P'),
     ((6, 4), None, 'HID_KEYBOARD_SC_CLOSING_BRACKET_AND_CLOSING_BRACE')],

    [((6, 4), None, 'HID_KEYBOARD_SC_TAB'),
     ((4, 4), None, 'HID_KEYBOARD_SC_A'),
     ((4, 4), None, 'HID_KEYBOARD_SC_S'),
     ((4, 4), None, 'HID_KEYBOARD_SC_D'),
     ((4, 4), None, 'HID_KEYBOARD_SC_F'),
     ((4, 4), None, 'HID_KEYBOARD_SC_G'),
     (-4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (2, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (-4, None, '0'),
     ((4, 4), None, 'HID_KEYBOARD_SC_H'),
     ((4, 4), None, 'HID_KEYBOARD_SC_J'),
     ((4, 4), None, 'HID_KEYBOARD_SC_K'),
     ((4, 4), None, 'HID_KEYBOARD_SC_L'),
     ((4, 4), None, 'HID_KEYBOARD_SC_SEMICOLON_AND_COLON'),
     ((6, 4), None, 'HID_KEYBOARD_SC_APOSTROPHE_AND_QUOTE')],

    [((6, 4), None, 'HID_KEYBOARD_SC_LEFT_SHIFT'),
     ((4, 4), None, 'HID_KEYBOARD_SC_Z'),
     ((4, 4), None, 'HID_KEYBOARD_SC_X'),
     ((4, 4), None, 'HID_KEYBOARD_SC_C'),
     ((4, 4), None, 'HID_KEYBOARD_SC_V'),
     ((4, 4), None, 'HID_KEYBOARD_SC_B'),
     ((4, -6), None, 'SCANCODE_FN2'),
     ((4, 4), None, 'HID_KEYBOARD_SC_LEFT_CONTROL'),
     ((4, 4), None, 'HID_KEYBOARD_SC_LEFT_ALT'),
     (2, None, '0'),
     ((4, 4), None, 'HID_KEYBOARD_SC_RIGHT_ALT'),
     ((4, 4), None, 'HID_KEYBOARD_SC_RIGHT_CONTROL'),
     ((4, -6), None, 'SCANCODE_FN3'),
     ((4, 4), None, 'HID_KEYBOARD_SC_N'),
     ((4, 4), None, 'HID_KEYBOARD_SC_M'),
     ((4, 4), None, 'HID_KEYBOARD_SC_COMMA_AND_LESS_THAN_SIGN'),
     ((4, 4), None, 'HID_KEYBOARD_SC_DOT_AND_GREATER_THAN_SIGN'),
     ((4, 4), None, 'HID_KEYBOARD_SC_SLASH_AND_QUESTION_MARK'),
     ((6, 4), None, 'HID_KEYBOARD_SC_RIGHT_SHIFT')],

    [(2, None, '0'),
     ((4, 4), None, 'HID_KEYBOARD_SC_LEFT_GUI'),
     ((4, 4), None, 'HID_KEYBOARD_SC_GRAVE_ACCENT_AND_TILDE'),
     ((4, 4), None, 'HID_KEYBOARD_SC_BACKSLASH_AND_PIPE'),
     ((4, 4), None, 'HID_KEYBOARD_SC_LEFT_ARROW'),
     ((4, 4), None, 'HID_KEYBOARD_SC_RIGHT_ARROW'),
     (4, None, '0'),
     ((4, 8), None, 'HID_KEYBOARD_SC_BACKSPACE'),
     ((4, 8), None, 'HID_KEYBOARD_SC_DELETE'),
     ((4, 4), None, 'HID_KEYBOARD_SC_HOME'),
     (2, None, '0'),
     ((4, 4), None, 'HID_KEYBOARD_SC_PAGE_UP'),
     ((4, 8), None, 'HID_KEYBOARD_SC_ENTER'),
     ((4, 8), None, 'HID_KEYBOARD_SC_SPACE'),
     (4, None, '0'),
     ((4, 4), None, 'HID_KEYBOARD_SC_LEFT_ARROW'),
     ((4, 4), None, 'HID_KEYBOARD_SC_DOWN_ARROW'),
     ((4, 4), None, 'HID_KEYBOARD_SC_UP_ARROW'),
     ((4, 4), None, 'HID_KEYBOARD_SC_RIGHT_ARROW'),
     ((4, 4), None, 'HID_KEYBOARD_SC_RIGHT_GUI'),
     (2, None, '0')],

    [(6, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (-4, None, '0'),
     (-4, None, '0'),
     ((4, 4), None, 'HID_KEYBOARD_SC_END'),
     (2, None, '0'),
     ((4, 4), None, 'HID_KEYBOARD_SC_PAGE_DOWN'),
     (-4, None, '0'),
     (-4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (4, None, '0'),
     (6, None, '0')]
]

alt_layouts = {}

if __name__ == '__main__':
    print("Keyboard definition for Ergo Dox keyboard")
