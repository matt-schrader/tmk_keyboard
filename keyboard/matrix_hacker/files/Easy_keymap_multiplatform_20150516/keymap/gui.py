#!/usr/bin/env python

"""Easy AVR USB Keyboard Firmware Keymapper.

This is a stand-alone tool for creating and editing key maps for the
various keyboards supported by the Easy AVR USB Keyboard Firmware.  User
keymaps can be compiled directly into functional HEX files for programming.

Copyright 2013-2015 David Howland, All rights reserved.

"""

from __future__ import print_function

try:
    from Tkinter import *
    from ttk import *
    import tkFileDialog as filedialog
    import tkSimpleDialog as simpledialog
    import tkMessageBox as messagebox
except ImportError:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import filedialog
    from tkinter import simpledialog
    from tkinter import messagebox

import pickle
import copy
from array import array
import os.path

from keymap.scancodes import scancodes, keysyms
from keymap.picker import Picker
from keymap.password import Password
import keymap.intelhex as intelhex
import keymap.macroparse as macroparse
import keymap.cfgparse as cfgparse
import keymap.cfghwparse as cfghwparse

import keymap.epsilon
import keymap.tau
import keymap.sigma
import keymap.zeta
import keymap.filco
import keymap.filco87
import keymap.filco87v2
import keymap.filco104
import keymap.qfr
import keymap.qfrv2
import keymap.qfxt
import keymap.rosewill
import keymap.phantom
import keymap.handwire
import keymap.gh60
import keymap.ghpad
import keymap.kmac
import keymap.orion
# import keymap.ergodox
import keymap.jd45
import keymap.smallfry
import keymap.gh36
import keymap.techcard
import keymap.sixshooter
import keymap.lightsaver
import keymap.octagon
import keymap.atreus
import keymap.planck

VERSION = 12

ABOUT = """Easy AVR USB Keyboard Firmware Keymapper     (Version %d)

For support contact me on geekhack.org, username 'metalliqaz'.

Copyright 2013 David Howland. See LICENSE.txt for details.""" % VERSION

configurations = {}
configurations[keymap.epsilon.unique_id] = keymap.epsilon
configurations[keymap.tau.unique_id] = keymap.tau
configurations[keymap.sigma.unique_id] = keymap.sigma
configurations[keymap.zeta.unique_id] = keymap.zeta
configurations[keymap.filco.unique_id] = keymap.filco
configurations[keymap.filco87.unique_id] = keymap.filco87
configurations[keymap.filco87v2.unique_id] = keymap.filco87v2
configurations[keymap.filco104.unique_id] = keymap.filco104
configurations[keymap.qfr.unique_id] = keymap.qfr
configurations[keymap.qfrv2.unique_id] = keymap.qfrv2
configurations[keymap.qfxt.unique_id] = keymap.qfxt
configurations[keymap.rosewill.unique_id] = keymap.rosewill
configurations[keymap.phantom.unique_id] = keymap.phantom
configurations[keymap.handwire.unique_id] = keymap.handwire
configurations[keymap.gh60.unique_id] = keymap.gh60
configurations[keymap.ghpad.unique_id] = keymap.ghpad
configurations[keymap.kmac.unique_id] = keymap.kmac
configurations[keymap.orion.unique_id] = keymap.orion
# configurations[keymap.ergodox.unique_id] = keymap.ergodox
configurations[keymap.jd45.unique_id] = keymap.jd45
configurations[keymap.smallfry.unique_id] = keymap.smallfry
configurations[keymap.gh36.unique_id] = keymap.gh36
configurations[keymap.techcard.unique_id] = keymap.techcard
configurations[keymap.sixshooter.unique_id] = keymap.sixshooter
configurations[keymap.lightsaver.unique_id] = keymap.lightsaver
configurations[keymap.octagon.unique_id] = keymap.octagon
configurations[keymap.atreus.unique_id] = keymap.atreus
configurations[keymap.planck.unique_id] = keymap.planck

#pixels for 1/4x key size
UNIT = 12

MACRO_NUM = 14
DEFAULT_MACRO_LENGTH = 1024 * 2

NULL_SYMBOL = '0'
DEBUG_NULL_SYMBOL = 'HID_KEYBOARD_SC_KEYPAD_ASTERISK'

master_layers = ["Default", "Fn", "Layer 2", "Layer 3", "Layer 4",
                 "Layer 5", "Layer 6", "Layer 7", "Layer 8", "Layer 9"]
default_layer = "Default"

key_modes = ['Normal', 'Toggle', 'Tap Key', 'Lockable', 'Rapid Fire']
key_mode_map = {'Normal': 0x00, 'Toggle': 0x01, 'Tap Key': 0x04,
                'Lockable': 0x02, 'Rapid Fire': 0x08}
default_mode = 'Normal'

with_mods = ['Shift', 'Ctrl', 'Alt', 'Win']
with_mods_map = {'Shift': 0x20, 'Ctrl': 0x10, 'Alt': 0x40, 'Win': 0x80}

led_assignments = {'Num Lock': 0, 'Caps Lock': 1, 'Scroll Lock': 2,
                   'Compose': 3, 'Kana': 4, 'Win Lock': 5, 'Fn Active': 6,
                   'Fn2 Active': 7, 'Fn3 Active': 8, 'Fn4 Active': 9,
                   'Fn5 Active': 10, 'Fn6 Active': 11, 'Fn7 Active': 12,
                   'Fn8 Active': 13, 'Fn9 Active': 14, 'Any Fn Active':15,
                   'Backlight': None, 'Unassigned': None}
unassigned_string = 'Unassigned'
backlight_string = 'Backlight'


class GUI(object):

    """The main window object.

    Displays the main window and contains most of the functions.

    """

    def __init__(self, runpath):
        self.runpath = runpath
        self.check_py2exe()
        self.mypath = os.path.dirname(os.path.realpath(__file__))
        self.root = Tk()
        self.layers = []
        self.layers.extend(master_layers)
        self.leds = []
        self.macros = [''] * MACRO_NUM
        self.selectedconfig = None
        self.selectedlayoutmod = None
        self.keys = None
        self.ignorelist = None
        self.maps = None
        self.modes = None
        self.actions = None
        self.wmods = None
        self.namevar = StringVar()
        self.namevar.set('None')
        self.altvar = StringVar()
        self.altvar.set('None')
        self.layoutrowvar = StringVar()
        self.matrixrowvar = StringVar()
        self.layoutcolvar = StringVar()
        self.matrixcolvar = StringVar()
        self.bindvar = StringVar()
        self.actionvar = StringVar()
        self.actionwidget = None
        self.modevar = StringVar()
        self.modewidget = None
        self.wmodvars = [StringVar() for x in with_mods]
        self.layervar = StringVar()
        self.macrovar = StringVar()
        self.currentmacro = None
        self.activekey = None
        self.unsaved_changes = False
        self.clipboard = None
        self.pickerwindow = Picker(self)
        self.password = Password()
        self.creategui()
        self.loadlayouts()

    def go(self):
        self.root.mainloop()

    def check_py2exe(self):
        if hasattr(sys, 'frozen'):
            self.runpath = os.path.dirname(sys.executable)
            return True
        return False

    def loadlayouts(self):
        for config in configurations.values():
            if "Handwire" in config.description:
                cfg_file = "handwire.cfg"
            else:
                cfg_file = "%s.cfg" % config.firmware.lower()
            cfg_path = os.path.join(self.runpath, 'cfg', cfg_file)
            if os.path.exists(cfg_path):
                try:
                    config.alt_layouts = cfgparse.parse(cfg_path)
                except Exception as err:
                    msg = str(err)
                    if len(msg) == 0:
                        msg = str(type(err))
                    messagebox.showerror(title="Can't read config file",
                                         message='Error: ' + msg,
                                         parent=self.root)

    def creategui(self):
        # top level window
        self.root.title("Easy AVR USB Keyboard Firmware Keymapper")
        self.root.option_add('*tearOff', FALSE)
        self.root.resizable(0, 0)
        if self.check_py2exe():
            iconpath = os.path.join(self.runpath, 'icons', 'keyboard.ico')
        else:
            iconpath = os.path.join(self.mypath, 'icons', 'keyboard.ico')
        try:
            self.root.iconbitmap(default=iconpath)
        except:
            pass
        self.root.protocol("WM_DELETE_WINDOW", self.checksave)
        # menu bar
        menubar = Menu(self.root)
        menu_file = Menu(menubar)
        menu_file.add_command(label='New Default Layout...',
                              command=self.newfile)
        menu_file.add_command(label='Open Saved Layout...',
                              command=self.openfile)
        menu_file.add_command(label='Save Layout As...', command=self.savefile)
        menu_file.add_command(label='Generate Source...',
                              command=self.generate)
        menu_file.add_command(label='Build Firmware...', command=self.build)
        menu_file.add_command(label='Build Debug Firmware...',
                              command=self.debugbuild)
        menu_file.add_command(label='Exit', command=self.checksave)
        menubar.add_cascade(menu=menu_file, label='File')
        menu_edit = Menu(menubar)
        menu_edit.add_command(label='Copy Layer', command=self.copylayer)
        menu_edit.add_command(label='Paste Layer', command=self.pastelayer)
        menubar.add_cascade(menu=menu_edit, label='Edit')
        menu_view = Menu(menubar)
        menu_view.add_command(label='Picker', command=self.showpicker)
        menu_view.add_command(label='Password Generator',
                              command=self.showpassword)
        menubar.add_cascade(menu=menu_view, label='View')
        menu_help = Menu(menubar)
        menu_help.add_command(label="Beginner's Guide",
                              command=self.helpreadme)
        menu_help.add_command(label='Help on Functions and Layers',
                              command=self.helplayers)
        menu_help.add_command(label='Help on Writing Macros',
                              command=self.helpmacros)
        menu_help.add_command(label='Help on Special Config Settings',
                              command=self.helpconsole)
        menu_help.add_command(label='Help on the Password Generator',
                              command=self.helppasswords)
        menu_help.add_command(label='About',
                              command=self.about)
        menubar.add_cascade(menu=menu_help, label='Help')
        self.root['menu'] = menubar
        # frame to hold info labels
        infoframe = Frame(self.root)
        Label(infoframe, text="Hardware: ").pack(side=LEFT)
        Label(infoframe, textvariable=self.namevar).pack(side=LEFT)
        Label(infoframe, text="      Layout: ").pack(side=LEFT)
        Label(infoframe, textvariable=self.altvar).pack(side=LEFT)
        Label(infoframe, text="      Layout Row: ").pack(side=LEFT)
        Entry(infoframe, textvariable=self.layoutrowvar, state='readonly',
              width=2).pack(side=LEFT)
        Label(infoframe, text=" Col: ").pack(side=LEFT)
        Entry(infoframe, textvariable=self.layoutcolvar, state='readonly',
              width=2).pack(side=LEFT)
        Label(infoframe, text="      Matrix Row: ").pack(side=LEFT)
        Entry(infoframe, textvariable=self.matrixrowvar, state='readonly',
              width=2).pack(side=LEFT)
        Label(infoframe, text=" Col: ").pack(side=LEFT)
        Entry(infoframe, textvariable=self.matrixcolvar, state='readonly',
              width=2).pack(side=LEFT)
        infoframe.pack()
        Separator(self.root, orient=HORIZONTAL).pack(fill=X, pady=2)
        # frame to hold the editing controls
        modframe = Frame(self.root)
        Label(modframe, text="Set: ").pack(side=LEFT)
        temp = sorted(scancodes.keys())
        temp2 = [x for x in temp if not x.startswith("SCANCODE_")]
        setbox = Combobox(modframe, width=40, height=40)
        setbox['values'] = temp
        setbox['textvariable'] = self.bindvar
        setbox.state(['readonly'])
        setbox.bind('<<ComboboxSelected>>', self.updatekey)
        setbox.pack(side=LEFT)
        Label(modframe, text="      Mode: ").pack(side=LEFT)
        setbox = Combobox(modframe, width=10)
        setbox['values'] = key_modes
        setbox['textvariable'] = self.modevar
        setbox.state(['readonly', 'disabled'])
        setbox.bind('<<ComboboxSelected>>', self.updatelockmode)
        setbox.pack(side=LEFT)
        self.modewidget = setbox
        setbox = Combobox(modframe, width=40, height=40)
        setbox['values'] = temp2
        setbox['textvariable'] = self.actionvar
        setbox.state(['readonly', 'disabled'])
        setbox.bind('<<ComboboxSelected>>', self.updateaction)
        setbox.pack(side=LEFT)
        self.actionwidget = setbox
        modframe.pack()
        modframe2 = Frame(self.root)
        Label(modframe2, text="With mods:   ").pack(side=LEFT)
        for modifier, modvar in zip(with_mods, self.wmodvars):
            modvar.set('False')
            cb = Checkbutton(modframe2, text=modifier, variable=modvar,
            onvalue='True', offvalue='False', command=self.updatewmods)
            cb.pack(side=LEFT, padx=8)
        modframe2.pack()
        Separator(self.root, orient=HORIZONTAL).pack(fill=X, pady=2)
        #frame to hold the layer selectors
        layerframe = Frame(self.root)
        Label(layerframe, text="Layer: ").pack(side=LEFT)
        for layer in self.layers:
            Radiobutton(layerframe, text=layer,
                        variable=self.layervar, value=layer,
                        command=self.selectlayer).pack(side=LEFT, padx=5)
        layerframe.pack()
        Separator(self.root, orient=HORIZONTAL).pack(fill=X, pady=2)
        # frame for the layout
        self.layoutframe = Frame(self.root)
        self.layoutframe.pack(fill=BOTH, expand=1)
        self.subframe = None
        Separator(self.root, orient=HORIZONTAL).pack(fill=X, pady=2)
        self.ledframe = Frame(self.root)
        self.ledframe.pack(fill=BOTH, expand=1)
        self.ledsubframe = None
        Separator(self.root, orient=HORIZONTAL).pack(fill=X, pady=2)
        # macros frame
        macroframe = Frame(self.root)
        macrosubframe = Frame(macroframe)
        Label(macrosubframe, text="Macro: ").pack(side=LEFT)
        for i in range(MACRO_NUM):
            Radiobutton(macrosubframe, text="M%d" % (i+1),
                        variable=self.macrovar, value=str(i),
                        command=self.selectmacro).pack(side=LEFT, padx=3)
        macrosubframe.pack()
        macrosubframe = Frame(macroframe)
        macrosubframe.rowconfigure(0, weight=1)
        macrosubframe.columnconfigure(0, weight=1)
        self.macrotext = Text(macrosubframe, height=5)
        self.macrotext.bind('<<Modified>>', self.macrochange)
        self.macrotext.grid(row=0, column=0, sticky=(N, W, E, S))
        scroll = Scrollbar(macrosubframe, orient=VERTICAL,
                           command=self.macrotext.yview)
        scroll.grid(row=0, column=1, sticky=(N, S))
        self.macrotext['yscrollcommand'] = scroll.set
        macrosubframe.pack(fill=X)
        self.resetmacros()
        macroframe.pack(fill=X)
        # set up some styles
        style = Style()
        style.configure("Gold.TButton", background="Gold")

    def showpicker(self):
        self.pickerwindow.show()

    def showpassword(self):
        limit = 0
        if self.selectedconfig:
            config = configurations[self.selectedconfig]
            if config.uc_size == 'large':
                limit = 40
            elif config.uc_size == 'small':
                limit = 20
        self.password.popup(self.root, limit)

    def checksave(self):
        if self.askchanges():
            self.root.destroy()

    def askchanges(self):
        if self.unsaved_changes:
            return messagebox.askokcancel(
                title="Discard changes",
                message="There are unsaved changes.  Continue?",
                parent=self.root)
        return True

    def resetmacros(self):
        self.macrotext.delete('1.0', 'end')
        self.macrovar.set('0')
        self.currentmacro = 0
        self.macros = [''] * MACRO_NUM

    def macrochange(self, event):
        if self.selectedconfig:
            self.unsaved_changes = True

    def selectmacro(self, withsave=True):
        if withsave:
            macro_string = self.macrotext.get('1.0', 'end')
            # the text widget always seems to add a newline to every string
            if macro_string[-1] == '\n':
                macro_string = macro_string[:-1]
            self.macros[self.currentmacro] = macro_string
        self.currentmacro = int(self.macrovar.get())
        self.macrotext.delete('1.0', 'end')
        if self.macros[self.currentmacro]:
            self.macrotext.insert('1.0', self.macros[self.currentmacro])
        self.macrotext.focus_set()

    def selectlayer(self):
        if self.maps:
            selectedmap = self.maps[self.layervar.get()]
            if self.keys:
                for row in self.keys:
                    for kb in row:
                        kb.set(selectedmap[kb.row][kb.col])
                self.setactivekey(self.keys[0][0])

    def updatekey(self, event):
        if self.maps and self.activekey:
            selectedmap = self.maps[self.layervar.get()]
            selectedmap[self.activekey.row][self.activekey.col] = (
                self.bindvar.get())
            self.activekey.set(self.bindvar.get())
            self.managefnchange(self.activekey)
            self.unsaved_changes = True

    def updateaction(self, event):
        if self.actions and self.activekey:
            selectedactions = self.actions[self.layervar.get()]
            selectedactions[self.activekey.row][self.activekey.col] = (
                self.actionvar.get())
            self.unsaved_changes = True

    def updatelockmode(self, event):
        if self.modes and self.activekey:
            selectedmodes = self.modes[self.layervar.get()]
            selectedmodes[self.activekey.row][self.activekey.col] = (
                self.modevar.get())
            if self.modevar.get() == 'Tap Key':
                selectedactions = self.actions[self.layervar.get()]
                self.actionvar.set(
                    selectedactions[self.activekey.row][self.activekey.col])
                self.actionwidget.state(['readonly', '!disabled'])
            else:
                self.actionvar.set('')
                self.actionwidget.state(['readonly', 'disabled'])
            self.unsaved_changes = True

    def updatewmods(self):
        if self.wmods and self.activekey:
            selectedwmods = self.wmods[self.layervar.get()]
            wmodval = 0
            for modifier, wmodvar in zip(with_mods, self.wmodvars):
                if wmodvar.get() == 'True':
                    wmodval |= with_mods_map[modifier]
            selectedwmods[self.activekey.row][self.activekey.col] = wmodval
            self.unsaved_changes = True

    def updateled(self, name, index, mode):
        # find out which LED it is and what the new setting is
        for var in self.leds:
            if name == var._name:
                setting = var.get()
                break
        # see if we have a conflict and resolve it
        if (setting != unassigned_string) and (setting != backlight_string):
            for var in self.leds:
                if (var._name != name) and (var.get() == setting):
                    var.set(unassigned_string)
        self.unsaved_changes = True

    def managefnchange(self, kb):
        kbwmod = self.wmods[self.layervar.get()][kb.row][kb.col]
        for modifier, wmodvar in zip(with_mods, self.wmodvars):
            if ((kbwmod & with_mods_map[modifier]) > 0):
                wmodvar.set('True')
            else:
                wmodvar.set('False')
        if kb.fnbound:
            kbmode = self.modes[self.layervar.get()][kb.row][kb.col]
            self.modevar.set(kbmode)
            self.modewidget.state(['!disabled'])
            if kbmode == 'Tap Key':
                kbaction = self.actions[self.layervar.get()][kb.row][kb.col]
                self.actionvar.set(kbaction)
                self.actionwidget.state(['readonly', '!disabled'])
            else:
                self.actionvar.set('')
                self.actionwidget.state(['readonly', 'disabled'])
        else:
            self.actionvar.set('')
            self.actionwidget.state(['readonly', 'disabled'])
            self.modevar.set('')
            self.modewidget.state(['disabled'])

    def setactivekey(self, kb):
        if self.activekey:
            self.activekey.normal()
        self.activekey = kb
        self.activekey.highlight()
        config = configurations[self.selectedconfig]
        self.layoutrowvar.set(str(kb.row))
        self.layoutcolvar.set(str(kb.col))
        r, c = config.keyboard_definition[kb.row][kb.col][1]
        self.matrixrowvar.set(str(r))
        self.matrixcolvar.set(str(c))
        selectedmap = self.maps[self.layervar.get()]
        self.bindvar.set(selectedmap[kb.row][kb.col])
        self.managefnchange(kb)

    def keypress(self, evt):
        if (evt.keysym_num in keysyms):
            self.bindvar.set(keysyms[evt.keysym_num])
            self.updatekey(None)

    def pickerselect(self, scancode):
        self.bindvar.set(scancode)
        self.updatekey(None)
        self.root.lift()

    def getlayoutmod(self, layoutmod, row, col, default):
        for mod in layoutmod:
            if mod[0] == (row, col):
                return mod[1]
        return default

    def loadconfig(self, unique_id, layoutmod=None):
        #remove the old layout graphic
        if self.subframe:
            self.subframe.destroy()
            self.ledsubframe.destroy()
        self.keys = []
        self.ignorelist = []
        self.activekey = None
        #lookup the new configuration
        config = configurations[unique_id]
        self.selectedconfig = unique_id
        self.selectedlayoutmod = layoutmod
        #check to see if layout is changing
        if self.namevar.get() != config.description:
            self.clipboard = None
        #create the new layout graphic
        self.namevar.set(config.description)
        if layoutmod:
            if layoutmod not in config.alt_layouts:
                messagebox.showerror(
                    title="Can't load config",
                    message='Error: can not find layout %s' % layoutmod,
                    parent=self.root)
                return
            self.altvar.set(layoutmod)
        else:
            self.altvar.set(config.description)
        self.subframe = Frame(self.layoutframe,
                              width=(config.display_width*UNIT),
                              height=(config.display_height*UNIT))
        x = y = 0
        for i, rowdef in enumerate(config.keyboard_definition):
            if isinstance(rowdef, list):
                keylist = []
                for j, keydef in enumerate(rowdef):
                    if layoutmod:
                        keydef = self.getlayoutmod(
                            config.alt_layouts[layoutmod],
                            i, j, keydef[0])
                    else:
                        keydef = keydef[0]
                    if isinstance(keydef, tuple):
                        w, h = keydef
                        if (w > 0) and (h > 0):
                            btn_frame = Frame(self.subframe, width=(w*UNIT),
                                              height=(h*UNIT))
                            btn_frame.pack_propagate(0)
                            kb = KeyButton(i, j, btn_frame, self)
                            kb.btn.pack(fill=BOTH, expand=1)
                            keylist.append(kb)
                            btn_frame.grid(row=y, column=x, rowspan=h,
                                           columnspan=w)
                        elif (w > 0) and (h < 0):
                            h = (-1 * h)
                            tmpy = y - (h - 4)
                            btn_frame = Frame(self.subframe, width=(w*UNIT),
                                              height=(h*UNIT))
                            btn_frame.pack_propagate(0)
                            kb = KeyButton(i, j, btn_frame, self)
                            kb.btn.pack(fill=BOTH, expand=1)
                            keylist.append(kb)
                            btn_frame.grid(row=tmpy, column=x, rowspan=h,
                                           columnspan=w)
                        else:
                            messagebox.showerror(
                                title="Can't load config",
                                message='Error: invalid keyboard_definition',
                                parent=self.root)
                            return
                        x += w
                    elif isinstance(keydef, int):
                        self.ignorelist.append((i, j))
                        if keydef > 0:
                            space_frame = Frame(self.subframe,
                                                width=(keydef*UNIT),
                                                height=(4*UNIT))
                            space_frame.grid(row=y, column=x, rowspan=4,
                                             columnspan=keydef)
                            x += keydef
                        else:
                            x += (-1 * keydef)
                    else:
                        messagebox.showerror(
                            title="Can't load config",
                            message='Error: invalid keyboard_definition',
                            parent=self.root)
                        return
                self.keys.append(keylist)
                y += 4
                x = 0
            elif isinstance(rowdef, int):
                w = config.display_width
                space_frame = Frame(self.subframe, width=(w*UNIT),
                                    height=(rowdef*UNIT))
                space_frame.grid(row=y, column=x, rowspan=rowdef, columnspan=w)
                y += rowdef
            else:
                messagebox.showerror(
                    title="Can't load config",
                    message='Error: invalid keyboard_definition',
                    parent=self.root)
                return
        self.subframe.pack()
        self.ledsubframe = Frame(self.ledframe)
        ledsubsubframe = Frame(self.ledsubframe)
        Label(ledsubsubframe, text="LEDs:").pack(side=LEFT)
        self.leds = []
        if len(config.led_definition) > 4:
            split = len(config.led_definition) - (len(config.led_definition)//2)
        else:
            split = 4
        for i, led_def in enumerate(config.led_definition):
            label, default = led_def
            if (i != 0) and (i % split == 0):
                ledsubsubframe.pack()
                ledsubsubframe = Frame(self.ledsubframe)
            setvar = StringVar()
            setvar.set(default)
            setvar.trace('w', self.updateled)
            self.leds.append(setvar)
            Label(ledsubsubframe, text='   '+label).pack(side=LEFT)
            setbox = Combobox(ledsubsubframe, width=12)
            setbox['values'] = sorted(led_assignments.keys())
            setbox['textvariable'] = setvar
            setbox.state(['readonly'])
            #setbox.bind('<<ComboboxSelected>>', self.updateled)
            setbox.pack(side=LEFT)
        ledsubsubframe.pack()
        self.ledsubframe.pack()

    def copylayer(self):
        if self.selectedconfig:
            if self.maps:
                layer = self.layervar.get()
                self.clipboard = (copy.deepcopy(self.maps[layer]),
                        copy.deepcopy(self.modes[layer]),
                        copy.deepcopy(self.actions[layer]),
                        copy.deepcopy(self.wmods[layer]))
        else:
            messagebox.showerror(title="Can't Copy",
                                 message='Create a keyboard first!',
                                 parent=self.root)

    def pastelayer(self):
        if self.clipboard is None:
            messagebox.showerror(title="Can't Paste",
                                 message='Clipboard is empty!',
                                 parent=self.root)
        else:
            if self.maps:
                layer = self.layervar.get()
                self.maps[layer] = copy.deepcopy(self.clipboard[0])
                self.modes[layer] = copy.deepcopy(self.clipboard[1])
                self.actions[layer] = copy.deepcopy(self.clipboard[2])
                self.wmods[layer] = copy.deepcopy(self.clipboard[3])
                self.unsaved_changes = True
                self.selectlayer()

    def getkeymap(self, keyboard_definition):
        keymap = []
        for rowdef in keyboard_definition:
            if isinstance(rowdef, list):
                rowlist = []
                for keydef in rowdef:
                    rowlist.append(keydef[2])
                keymap.append(rowlist)
            elif isinstance(rowdef, int):
                keymap.append([])
            else:
                raise Exception('Error: invalid keyboard_definition')
        return keymap

    def newfile(self):
        if self.askchanges():
            new_win = NewWindow(self.root, "Select type for new layout")
            if new_win.result:
                self.loadconfig(new_win.result, new_win.layout)
                config = configurations[new_win.result]
                #get the default keymap to start with
                self.maps = {}
                self.modes = {}
                self.actions = {}
                self.wmods = {}
                default_keymap = self.getkeymap(config.keyboard_definition)
                empty_keymap = [['0'] * len(x) for x in default_keymap]
                init_modes = [[default_mode] * len(x) for x in default_keymap]
                init_wmods = [[0] * len(x) for x in default_keymap]
                for layer in self.layers[:2]:
                    self.maps[layer] = copy.deepcopy(default_keymap)
                    self.modes[layer] = copy.deepcopy(init_modes)
                    self.actions[layer] = copy.deepcopy(empty_keymap)
                    self.wmods[layer] = copy.deepcopy(init_wmods)
                for layer in self.layers[2:]:
                    self.maps[layer] = copy.deepcopy(empty_keymap)
                    self.modes[layer] = copy.deepcopy(init_modes)
                    self.actions[layer] = copy.deepcopy(empty_keymap)
                    self.wmods[layer] = copy.deepcopy(init_wmods)
                self.layervar.set(default_layer)
                del self.password
                self.password = Password()
                self.selectlayer()
                self.resetmacros()
                self.unsaved_changes = False
                #alert the user of the use of their new layout
                if new_win.result == keymap.handwire.unique_id:
                    self.helphandwire()

    def openfile(self):
        if self.askchanges():
            filename = filedialog.askopenfilename(
                filetypes=[('Saved Layouts', '.dat')],
                parent=self.root)
            if not filename:
                return
            try:
                with open(filename, 'rb') as fdin:
                    data = pickle.load(fdin)
                    version = data[0]
                    if version < 12:
                        answer = messagebox.askokcancel(
                            title="Save file is incompatible",
                            message="The save file you have selected was saved"
                            " by an older version and will probably not work."
                            "  Are you sure this is what you want?",
                            parent=self.root)
                        if not answer:
                            return
                    unique_id = data[1]
                    if unique_id not in configurations:
                        messagebox.showerror(
                            title="Can't load save file",
                            message="This save file describes a configuration "
                            "that cannot be loaded.",
                            parent=self.root)
                        return
                    maps = data[2]
                    if len(data) > 8:
                        layoutmod = data[8]
                    else:
                        layoutmod = None
                    self.loadconfig(unique_id, layoutmod)
                    self.maps = maps
                    if version == 1:
                        self.adapt_v1()
                    if version <= 2:
                        self.adapt_v2()
                    if len(data) > 3:
                        self.resetmacros()
                        self.macros = data[3]
                        self.selectmacro(withsave=False)
                    if version >= 12:
                        if len(data) > 4:
                            self.actions = data[4]
                        if len(data) > 5:
                            self.modes = data[5]
                        if len(data) > 6:
                            self.wmods = data[6]
                        if len(data) > 7:
                            pass    # unused
                    else:
                        self.actions = {}
                        self.modes = {}
                        self.wmods = {}
                        config = configurations[self.selectedconfig]
                        default_keymap = self.getkeymap(config.keyboard_definition)
                        empty_keymap = [['0'] * len(x) for x in default_keymap]
                        init_modes = [[default_mode] * len(x) for x in default_keymap]
                        init_wmods = [[0] * len(x) for x in default_keymap]
                        for layer in self.layers:
                            self.modes[layer] = copy.deepcopy(init_modes)
                            self.actions[layer] = copy.deepcopy(empty_keymap)
                            self.wmods[layer] = copy.deepcopy(init_wmods)
                    self.layervar.set(default_layer)
                    self.selectlayer()
                    if len(data) > 9:
                        for i, a in enumerate(data[9]):
                            self.leds[i].set(a)
                    if len(data) > 10:
                        del self.password
                        self.password = Password(data[10])
                    if version <= 3:
                        self.adapt_v3()
                    if version <= 4:
                        self.adapt_v4()
                    if version <= 5:
                        self.adapt_v5()
                    if version <= 6:
                        self.adapt_v6()
                    if version <= 7:
                        self.adapt_v7()
                    if version <= 8:
                        self.adapt_v8()
                    if version <= 9:
                        self.adapt_v9()
                    if version <= 10:
                        self.adapt_v10()
                    if version <= 11:
                        self.adapt_v11()
                    self.scrub_scancodes()
                self.unsaved_changes = False
            except Exception as err:
                msg = str(err)
                if len(msg) == 0:
                    msg = str(type(err))
                messagebox.showerror(title="Can't open layout",
                                     message='Error: ' + msg,
                                     parent=self.root)

    def adapt_v1(self):
        print("Adapting save file v1->v2")
        newmaps = {}
        for layer in self.maps:
            newmaps[layer] = []
            for row in self.maps[layer]:
                newmaps[layer].append([x for x in row if x is not None])
        self.maps = newmaps

    def adapt_v2(self):
        print("Adapting save file v2->v3")
        remap = {'Top': 'Default', 'Fn': 'Fn', 'Special': 'Layer 2',
                 'Alt': 'Layer 3'}
        newmaps = {}
        for layer in self.maps:
            newname = remap[layer]
            newmaps[newname] = self.maps[layer]
        newmaps['Layer 4'] = copy.deepcopy(self.maps['Alt'])
        self.maps = newmaps

    def adapt_v3(self):
        print("Adapting save file v3->v4")
        for layer in master_layers:
            if layer not in self.maps:
                self.maps[layer] = \
                    copy.deepcopy(self.maps['Default'])
        extention = MACRO_NUM - len(self.macros)
        if extention > 0:
            self.macros.extend([''] * extention)

    def adapt_v4(self):
        print("Adapting save file v4->v5")

    def adapt_v5(self):
        print("Adapting save file v5->v6")

    def adapt_v6(self):
        print("Adapting save file v6->v7")

    def adapt_v7(self):
        print("Adapting save file v7->v8")

    def adapt_v8(self):
        print("Adapting save file v8->v9")
        del self.password
        self.password = Password()

    def adapt_v9(self):
        print("Adapting save file v9->v10")
        extention = MACRO_NUM - len(self.macros)
        if extention > 0:
            self.macros.extend([''] * extention)

    def adapt_v10(self):
        print("Adapting save file v10->v11")
        for var in self.leds:
            if var.get() == 'Fn Lock':
                var.set('Any Fn Active')

    def adapt_v11(self):
        print("Adapting save file v11->v12")

    def scrub_scancodes(self):
        for layer in self.maps:
            for row in self.maps[layer]:
                for i, k in enumerate(row):
                    if k == "SCANCODE_DEBUG":
                        row[i] = "SCANCODE_CONFIG"
                    elif k == "SCANCODE_LOCKINGCAPS":
                        row[i] = "HID_KEYBOARD_SC_LOCKING_CAPS_LOCK"
                    elif k not in scancodes:
                        row[i] = '0'

    def savefile(self):
        if self.selectedconfig:
            self.selectmacro()
            leds = [x.get() for x in self.leds]
            package = (VERSION, self.selectedconfig, self.maps,
                       self.macros, self.actions, self.modes,
                       self.wmods, None,
                       self.selectedlayoutmod, leds,
                       self.password.getstruct())
            filename = filedialog.asksaveasfilename(
                defaultextension=".dat",
                filetypes=[('Saved Layouts', '.dat')],
                parent=self.root)
            if not filename:
                return
            try:
                with open(filename, 'wb') as fdout:
                    pickle.dump(package, fdout, protocol=2)
                self.unsaved_changes = False
            except Exception as err:
                msg = str(err)
                if len(msg) == 0:
                    msg = str(type(err))
                messagebox.showerror(title="Can't save layout",
                                     message='Error: ' + msg,
                                     parent=self.root)
        else:
            messagebox.showerror(title="Can't save layout",
                                 message='Create a keyboard first!',
                                 parent=self.root)

    def generate(self):
        if self.selectedconfig:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[('Text Files', '.txt'),
                           ('C Files', '.c'),
                           ('C Files', '.h')],
                parent=self.root)
            if not filename:
                return
            try:
                with open(filename, 'w') as fdout:
                    fdout.write("const uint8_t PROGMEM LAYERS[NUMBER_OF_LAYERS]"
                                "[NUMBER_OF_ROWS][NUMBER_OF_COLS] = {\n")
                    for layer in self.layers:
                        fdout.write("{\n")
                        data = self.translate(self.maps[layer])
                        for row in data:
                            fdout.write("    { ")
                            for value in row:
                                fdout.write(value)
                                fdout.write(", ")
                            fdout.write("},\n")
                        fdout.write("},\n")
                    fdout.write("};\n")
                    fdout.write("const uint8_t PROGMEM ACTIONS[NUMBER_OF_LAYERS"
                                "][NUMBER_OF_ROWS][NUMBER_OF_COLS] = {\n")
                    for layer in self.layers:
                        fdout.write("{\n")
                        data = self.translate(self.modes[layer], default=default_mode)
                        data2 = self.translate(self.wmods[layer], default=0)
                        for row, row2 in zip(data, data2):
                            fdout.write("    { ")
                            for value, value2 in zip(row, row2):
                                fdout.write("%#04x" % (key_mode_map[value] | value2))
                                fdout.write(", ")
                            fdout.write("},\n")
                        fdout.write("},\n")
                    fdout.write("};\n")
                    fdout.write("const uint8_t PROGMEM TAPKEYS[NUMBER_OF_LAYERS"
                                "][NUMBER_OF_ROWS][NUMBER_OF_COLS] = {\n")
                    for layer in self.layers:
                        fdout.write("{\n")
                        data = self.translate(self.actions[layer])
                        for row in data:
                            fdout.write("    { ")
                            for value in row:
                                fdout.write(value)
                                fdout.write(", ")
                            fdout.write("},\n")
                        fdout.write("},\n")
                    fdout.write("};\n")
            except Exception as err:
                msg = str(err)
                if len(msg) == 0:
                    msg = str(type(err))
                messagebox.showerror(title="Can't generate code",
                                     message='Error: ' + msg,
                                     parent=self.root)
        else:
            messagebox.showerror(title="Can't generate code",
                                 message='Create a keyboard first!',
                                 parent=self.root)

    def checkforscancode(self, scancode):
        if self.maps:
            for keymap in self.maps.values():
                for row in keymap:
                    if scancode in row:
                        return True
        return False

    def translate(self, keymap, default='0'):
        config = configurations[self.selectedconfig]
        output = []
        for i in range(config.num_rows):
            output.append([default]*config.num_cols)
        for r, row in enumerate(keymap):
            for c, value in enumerate(row):
                if (r, c) in self.ignorelist:
                    continue
                if value is not None:
                    target = config.keyboard_definition[r][c][1]
                    if target is not None:
                        y, x = target
                        output[y][x] = value
        return output

    def gethintstrings(self):
        # print the keymap to a list of huge strings
        macro_list = []
        config = configurations[self.selectedconfig]
        layout = config.keyboard_definition
        layoutmod = self.selectedlayoutmod
        for layer in self.layers:
            string_list = []
            for i, rowdef in enumerate(config.keyboard_definition):
                if isinstance(rowdef, list):
                    for j, keydef in enumerate(rowdef):
                        if layoutmod:
                            keydef = self.getlayoutmod(
                                config.alt_layouts[layoutmod],
                                i, j, keydef[0])
                        else:
                            keydef = keydef[0]
                        if isinstance(keydef, tuple):
                            width = keydef[0]
                            assign = self.maps[layer][i][j]
                            text = scancodes[assign][2]
                            pad = width - len(text)
                            lf = pad // 2
                            rt = pad - lf
                            string_list.append(' ' * lf)
                            string_list.append(text)
                            string_list.append(' ' * rt)
                        elif isinstance(keydef, int):
                            string_list.append(' ' * abs(keydef))
                        # string_list.append('|')
                    string_list.append('\n')
            macro_list.append(''.join(string_list))
        return macro_list

    def build(self, debug=False):
        if self.selectedconfig:
            if ((not self.checkforscancode('SCANCODE_BOOT')) and
                    (self.selectedconfig != keymap.kmac.unique_id) and
                    (self.selectedconfig != keymap.orion.unique_id) and
                    (self.selectedconfig != keymap.lightsaver.unique_id)):
                answer = messagebox.askokcancel(
                    title="BOOT key not found",
                    message="You do not have a key bound to BOOT mode.  "
                    "Without it you can't easily reprogram your keyboard."
                    "  Are you sure this is what you want?",
                    parent=self.root)
                if not answer:
                    return
            config = configurations[self.selectedconfig]
            template = config.firmware + ".template"
            template_path = os.path.join(self.runpath, 'templates', template)
            filename = filedialog.asksaveasfilename(
                defaultextension=".hex",
                filetypes=[('Intel Hex Files', '.hex')],
                parent=self.root)
            if not filename:
                return
            try:
                with open(template_path, 'r') as fdin:
                    with open(filename, 'w') as fdout:
                        hexdata = intelhex.read(fdin)
                        start, bytes = hexdata[0]
                        # overwrite data for key maps
                        address = config.layers_map
                        offset = address - start
                        for layer in self.layers:
                            mapdata = self.translate(self.maps[layer])
                            for row in mapdata:
                                for value in row:
                                    if debug and value == NULL_SYMBOL:
                                        value = DEBUG_NULL_SYMBOL
                                    bytes[offset] = scancodes[value][1]
                                    offset += 1
                        # overwrite data for key actions
                        address = config.actions_map
                        offset = address - start
                        for layer in self.layers:
                            mapdata = self.translate(self.modes[layer], default=default_mode)
                            mapdata2 = self.translate(self.wmods[layer], default=0)
                            for row, row2 in zip(mapdata, mapdata2):
                                for value, value2 in zip(row, row2):
                                    bytes[offset] = (key_mode_map[value] | value2)
                                    offset += 1
                        # overwrite data for tap keys
                        address = config.tapkeys_map
                        offset = address - start
                        for layer in self.layers:
                            mapdata = self.translate(self.actions[layer])
                            for row in mapdata:
                                for value in row:
                                    bytes[offset] = scancodes[value][1]
                                    offset += 1
                        # overwrite data for macros
                        self.selectmacro()
                        self.assemblemacrodata(config, bytes, start)
                        # overwrite data for LED functions
                        overlay = [255] * (len(led_assignments)-2)
                        address = config.led_map
                        offset = address - start
                        for led_id, var in enumerate(self.leds):
                            assignment = var.get()
                            if ((assignment != unassigned_string) and
                              (assignment != backlight_string)):
                                index = led_assignments[assignment]
                                overlay[index] = led_id
                        for byte in overlay:
                            bytes[offset] = byte
                            offset += 1
                        # overwrite data for backlights
                        if config.backlighting:
                            address = config.bl_mask_map
                            offset = address - start
                            for led_id, var in enumerate(self.leds):
                                if var.get() == backlight_string:
                                    bytes[offset] = 1
                                else:
                                    bytes[offset] = 0
                                offset += 1
                        # overwrite data for password generators
                        if config.pw_defs_map is not None:
                            address = config.pw_defs_map
                            offset = address - start
                            s = self.password.getstring()
                            if s is not None:
                                end = offset + len(s)
                                bytes[offset:end] = array('B', s)
                        # overwrite ROW_LIST,COL_LIST,LED_LIST for handwire
                        if "Handwire" in config.description:
                            cfg_path = os.path.join(self.runpath, 'cfg', 'handwire_hardware.cfg')
                            cfg = cfghwparse.parse(cfg_path)
                            map = [('row', config.row_hw_map),
                                   ('col', config.col_hw_map),
                                   ('led', config.led_hw_map)]
                            for index, address in map:
                                offset = address - start
                                data = cfg[index]
                                for pin in data:
                                    for item in pin:
                                        bytes[offset] = item
                                        offset += 1
                        # finish up
                        intelhex.write(fdout, hexdata)
                        messagebox.showinfo(
                            title="Build complete",
                            message="Firmware saved successfully.",
                            parent=self.root)
            except Exception as err:
                msg = str(err)
                if len(msg) == 0:
                    msg = str(type(err))
                messagebox.showerror(title="Can't build binary",
                                     message='Error: ' + msg,
                                     parent=self.root)
        else:
            messagebox.showerror(title="Can't build binary",
                                 message='Create a keyboard first!',
                                 parent=self.root)

    def debugbuild(self):
        msg = ("You are building a debug version of the firmware.  "
               "Misconfigured keys will send a ' %s ' character rather than "
               "be ignored.  Report these occurrences in the Geekhack thread.")
        messagebox.showinfo(title="Debug Build",
                            message=(msg % scancodes[DEBUG_NULL_SYMBOL][0]),
                            parent=self.root)
        self.build(debug=True)

    def assemblemacrodata(self, config, bytes, start):
        try:
            macro_length = config.macro_length
        except:
            macro_length = DEFAULT_MACRO_LENGTH
        # convert all the macros to byte arrays and get the length of each
        extd = {'hints': self.gethintstrings()}
        macrodata = [macroparse.parse(m, externaldata=extd)
                        for m in self.macros]
        macrolen = [len(d) for d in macrodata]
        # figure out where the macros will fit inside the buffer
        index = MACRO_NUM
        macroindex = []
        for mlen in macrolen:
            if mlen <= 0:
                macroindex.append(macro_length-1)
            else:
                macroindex.append(index)
                index += ((mlen // 2) + 1)
                if index >= macro_length:
                    raise Exception("The macros have exceeded "
                                    "the allowable size.")
        if len(macroindex) != MACRO_NUM:
            raise Exception("The macro data is an inconsistent size.")
        # map the index table into the byte array
        offset = config.macro_map - start
        for index in macroindex:
            short_array = array('H', [index])
            byte_array = array('B', short_array.tostring())
            bytes[offset:offset+2] = byte_array[:]
            offset += 2
        # map the non-empty macros into the byte array
        for i in range(MACRO_NUM):
            if macrolen[i] > 0:
                end = offset+macrolen[i]
                bytes[offset:end] = macrodata[i][:]
                bytes[end:end+2] = array('B', [0, 0])[:]
                offset += (macrolen[i] + 2)
        # make sure the last spot of the byte array has a zero (terminator)
        last_spot = ((config.macro_map - start) + ((macro_length - 1) * 2))
        bytes[last_spot:last_spot+2] = array('B', [0, 0])[:]

    def showtext(self, path):
        if os.path.exists(path):
            filename = os.path.basename(path)
            with open(path, 'r') as fd:
                TextWindow(self.root, filename, fd.read())
        else:
            messagebox.showerror(title="Can't display document",
                                 message='File not found: ' + path,
                                 parent=self.root)

    def helpreadme(self):
        self.showtext(os.path.join(self.runpath, 'doc', 'readme.txt'))

    def helplayers(self):
        self.showtext(os.path.join(self.runpath, 'doc', 'functions.txt'))

    def helpmacros(self):
        self.showtext(os.path.join(self.runpath, 'doc', 'macros.txt'))

    def helpconsole(self):
        self.showtext(os.path.join(self.runpath, 'doc', 'console.txt'))

    def helppasswords(self):
        self.showtext(os.path.join(self.runpath, 'doc', 'passwords.txt'))

    def helphandwire(self):
        self.showtext(os.path.join(self.runpath, 'doc', 'handwire.txt'))

    def about(self):
        AboutWindow(self.root, 'About', ABOUT)


class KeyButton(object):

    """Represents one button on the keyboard."""

    def __init__(self, row, col, parent, gui):
        self.row = row
        self.col = col
        self.gui = gui
        self.display = StringVar()
        self.btn = Button(parent, textvariable=self.display,
                          command=self.on_press)
        self.btn.bind('<KeyPress>', gui.keypress)
        self.fnbound = False

    def on_press(self):
        self.gui.setactivekey(self)
        self.gui.pickerwindow.lift()

    def highlight(self):
        self.btn['style'] = "Gold.TButton"

    def normal(self):
        self.btn['style'] = "TButton"

    def set(self, scancode):
        self.display.set(scancodes[scancode][0])
        self.fnbound = False
        if scancode.startswith('SCANCODE_FN'):
            self.fnbound = True
        if scancode.startswith('HID_KEYBOARD_SC'):
            self.fnbound = True


class NewWindow(simpledialog.Dialog):

    """A dialog window to select from a list of available layouts."""

    def body(self, master):
        self.resizable(0, 0)
        Label(master, text="Available keyboard types: ").pack(side=TOP)
        self.selectionvar = StringVar()
        keyboards = sorted(configurations.keys())
        subframe = Frame(master)
        subsubframe = Frame(subframe)
        split = len(keyboards) - (len(keyboards)//2)
        for i,kb in enumerate(keyboards):
            if i == split:
                subsubframe.pack(side=LEFT)
                subsubframe = Frame(subframe)
            Radiobutton(subsubframe, text=configurations[kb].description,
                        command=self.selectionchanged,
                        variable=self.selectionvar,
                        value=kb).pack(side=TOP, fill=X)
        subsubframe.pack(side=LEFT)
        subframe.pack(side=TOP)
        Label(master, text="Available layouts: ").pack(side=TOP)
        self.layoutvar = StringVar()
        self.layoutbox = Combobox(master)
        self.layoutbox['values'] = []
        self.layoutbox['textvariable'] = self.layoutvar
        self.layoutbox.state(['readonly'])
        self.layoutbox.pack(side=TOP)

    def selectionchanged(self):
        config = configurations[self.selectionvar.get()]
        layouts = ["<All Keys>"]
        layouts.extend(sorted(config.alt_layouts.keys()))
        self.layoutbox['values'] = layouts
        self.layoutvar.set("<All Keys>")

    def validate(self):
        if self.selectionvar.get():
            return True
        return False

    def apply(self):
        self.result = self.selectionvar.get()
        self.layout = self.layoutvar.get()
        if self.layout == "<All Keys>":
            self.layout = None
        if self.layout == "":
            self.layout = None


class TextWindow(simpledialog.Dialog):

    """A dialog window to simply display text to the user."""

    def __init__(self, parent, title=None, text_data=None):
        self.text_data = text_data
        simpledialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        self.text = Text(master, height=40, width=80, wrap='none')
        self.text.grid(row=0, column=0, sticky=(N, E, W, S))
        scroll = Scrollbar(master, orient=VERTICAL, command=self.text.yview)
        scroll.grid(row=0, column=1, sticky=(N, S))
        self.text['yscrollcommand'] = scroll.set
        scroll = Scrollbar(master, orient=HORIZONTAL, command=self.text.xview)
        scroll.grid(row=1, column=0, sticky=(E, W))
        self.text['xscrollcommand'] = scroll.set
        self.text.insert('1.0', self.text_data)
        self.text['state'] = 'disabled'

    def buttonbox(self):
        #no buttons needed
        self.bind("<Escape>", self.cancel)


class AboutWindow(simpledialog.Dialog):

    """A dialog window to simply display a message to the user."""

    def __init__(self, parent, title=None, text_data=None):
        self.text_data = text_data
        simpledialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        Label(master, text=self.text_data).pack()

    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()


if __name__ == '__main__':
    GUI().go()
