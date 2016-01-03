#!/usr/bin/env python
"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2015 David Howland, All rights reserved.

"""

import re
import copy
try:
    import ConfigParser as configparser
except:
    import configparser

regex_pin_name = re.compile(r"^(row|col|led)([0-9]+)$", re.I)
regex_pin_asmt = re.compile(r"^([BCDEF])([0-9])$", re.I)

SECTION = "MATRIX"

PORTS = {
    "B": 0,
    "C": 1,
    "D": 2,
    "E": 3,
    "F": 4
}

# Phantom configuration

LED_DIRECTION = 0
HANDWIRE_ROWS=6
HANDWIRE_COLS=17
HANDWIRE_LEDS=2

DEFAULT = {
    'row': [
        (0, 5),
        (0, 4),
        (0, 3),
        (0, 2),
        (0, 1),
        (0, 0)
    ],
    'col': [
        (2, 5),
        (1, 7),
        (1, 6),
        (2, 4),
        (2, 0),
        (3, 6),
        (4, 0),
        (4, 1),
        (4, 4),
        (4, 5),
        (4, 6),
        (4, 7),
        (2, 7),
        (2, 6),
        (2, 1),
        (2, 2),
        (2, 3)
    ],
    'led': [
        (0, 6, 0),
        (0, 7, 0)
    ]
}

def parse(cfg_file):
    cfg = copy.deepcopy(DEFAULT)
    cp = configparser.RawConfigParser()
    cp.read(cfg_file)
    pins = cp.items(SECTION)
    for pin in pins:
        name, asmt = pin
        mn = regex_pin_name.match(name)
        if mn:
            ma = regex_pin_asmt.match(asmt)
            if ma:
                try:
                    if 'led' in mn.group(1):
                        cfg[mn.group(1)][int(mn.group(2))] = (PORTS[ma.group(1)], int(ma.group(2)), 0)
                    else:
                        cfg[mn.group(1)][int(mn.group(2))] = (PORTS[ma.group(1)], int(ma.group(2)))
                except:
                    raise Exception('Invalid hardware config option "%s = %s"' % (name, asmt))
            else:
                raise Exception('Error parsing hardware config option "%s = %s"' % (name, asmt))
        else:
            raise Exception('Error parsing hardware config option "%s = %s"' % (name, asmt))
    return cfg

if __name__ == '__main__':
    import sys
    try:
        print(parse(sys.argv[1]))
    except:
        raise
