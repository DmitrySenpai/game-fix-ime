import os
import sys
import pyperclip
import keyboard
import json
from ahk import AHK

ahk = AHK(executable_path='AutoHotkey\\AutoHotkey.exe')

with open('config.json') as json_file:
    json_setting = json.load(json_file)

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support



def start_ime():
    while True:
        keyboard.wait(json_setting["call_key"])
        vp_start_gui()
        break

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.focus_force()
    root.wm_attributes("-topmost", 1)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:

    def text_write(self):
        get_text = input_text.get()
        gui_support.destroy_window()
        pyperclip.copy(get_text)
        ahk.send_input('^v')
        start_ime()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.overrideredirect(True)
        top.geometry("210x45+" + json_setting["location"])
        top.minsize(120, 1)
        top.maxsize(3604, 1061)
        top.resizable(1,  1)
        top.title("IME text")
        top.configure(background="#d9d9d9")
        top.attributes('-alpha', json_setting["transparency"])
        

        self.Entry1 = tk.Entry(top)
        self.Entry1.bind('<Return>', Toplevel1.text_write)
        self.Entry1.place(relx=0.0, rely=0.0, height=50, relwidth=1.019)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        #self.Entry1.focus_set()

        global input_text

        input_text = self.Entry1

if __name__ == '__main__':
    os.system("title Game Fix IME - v1.0 [Alpha]")
    print('"Game Fix IME" service started.')
    print("GitHub: https://github.com/DmitrySenpai")
    start_ime()