#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.7
# In conjunction with Tcl version 8.5
#    Apr 07, 2016 12:49:27 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import TestProject_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Test_Form (root)
    TestProject_support.init(root, top)
    root.mainloop()

w = None
def create_Test_Form(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Test_Form (w)
    TestProject_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Test_Form():
    global w
    w.destroy()
    w = None


class Test_Form:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+311+132")
        top.title("Test Form")
        top.configure(background="#d9d9d9")



        self.Button1 = Button(top)
        self.Button1.place(relx=0.08, rely=0.89, height=28, width=51)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background=_bgcolor)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text='''Exit''')






if __name__ == '__main__':
    vp_start_gui()


