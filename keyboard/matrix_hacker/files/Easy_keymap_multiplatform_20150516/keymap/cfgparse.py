#!/usr/bin/env python
"""Easy AVR USB Keyboard Firmware Keymapper.

Copyright 2013 David Howland, All rights reserved.

"""

import re

regex_header = re.compile(r"^\[(.+)\]$")
regex_command = re.compile(r"^(MAKE_[SPACERKYBLN]+)\(([ ,\d-]+)\)$")


def parse(cfg_file):
    cfg = {}
    with open(cfg_file, 'r') as infd:
        mod_list = []
        mod_name = None
        for i, line in enumerate(infd):
            line = line.strip()
            if not line:
                continue
            if line.startswith('#'):
                continue
            m = regex_header.match(line)
            if m:
                if mod_name:
                    cfg[mod_name] = mod_list
                mod_name = m.group(1)
                mod_list = []
                continue
            m = regex_command.match(line)
            if m:
                try:
                    args = m.group(2).split(',')
                    if m.group(1) == "MAKE_KEY":
                        row = int(args[0].strip())
                        col = int(args[1].strip())
                        width = int(args[2].strip())
                        height = int(args[3].strip())
                        mod_list.append(((row, col), (width, height)))
                    elif m.group(1) == "MAKE_SPACER":
                        row = int(args[0].strip())
                        col = int(args[1].strip())
                        width = int(args[2].strip())
                        mod_list.append(((row, col), width))
                    elif m.group(1) == "MAKE_BLANK":
                        row = int(args[0].strip())
                        col = int(args[1].strip())
                        width = int(args[2].strip()) * -1
                        mod_list.append(((row, col), width))
                    else:
                        raise Exception("%s:%d: invalid command %s" %
                                        (cfg_file, i, m.group(1)))
                except IndexError:
                    raise Exception("%s:%d: Not enough arguments" %
                                    (cfg_file, i))
                except ValueError:
                    raise Exception("%s:%d: Argument is not integer" %
                                    (cfg_file, i))
                continue
            raise Exception("%s:%d: Unrecognized: %s" %
                            (cfg_file, i, line))
        if mod_name:
            cfg[mod_name] = mod_list
    return cfg

if __name__ == '__main__':
    import sys
    try:
        print(parse(sys.argv[1]))
    except:
        pass
