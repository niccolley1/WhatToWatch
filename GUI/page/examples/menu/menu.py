#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.6
# In conjunction with Tcl version 8.6
#    Feb 11, 2016 06:35:17 PM
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

import menu_support

def vp_start_gui():
    '''Starting point when module is the main routine.
       This class configures and populates the toplevel window'''
    global val, w, root
    root = Tk()
    menu_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    menu_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    menu_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    menu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''top is the toplevel containing window'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}' 
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2' 
        font11 = "-family {Droid Sans Mono} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("600x450+654+215")
        top.title("New Toplevel 1")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font=font11,bg='#ff0000',fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.file = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.file,
                background="#00ffff",
                compound="left",
                font=('Purisa',12,'normal','roman',),
                foreground="#000000",
                label="File")
        self.file.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ffff00",
                command=menu_support.save,
                foreground="#000000",
                label="Save")
        self.file.add_separator(
                background="#ffff00")
        self._img0 = PhotoImage(file="stop.gif")
        self.file.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ffff00",
                command=menu_support.quit,
                compound="top",
                foreground="#000000",
                image=self._img0,
                label="Quit")
        self.edit = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.edit,
                background="#990000",
                font=('Purisa',12,'normal','roman',),
                foreground="#ffff00",
                label="Edit")
        self.edit.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ff0000",
                command=menu_support.cut,
                foreground="#000000",
                label="Cut")
        self.edit.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ff0000",
                command=menu_support.copy,
                foreground="#000000",
                label="Copy")
        self.edit.add_separator(
                background="#ff0000")
        self.edit.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ff0000",
                command=menu_support.paste,
                foreground="#000000",
                label="Paste")
        self.other = Menu(top,tearoff=0)
        self.edit.add_cascade(menu=self.other,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ff0000",
                foreground="#000000",
                label="Other")
        self.other.add_command(
                background="#ffff00",
                label="Post")
        self.other.add_command(
                background="#ffff00",
                label="Sync")
        self.still = Menu(top,tearoff=0)
        self.other.add_cascade(menu=self.still,
                background="#ffff00",
                label="Still")
        self.still.add_command(
                background="#ff0000",
                label="Yes")
        self.still.add_command(
                background="#ff0000",
                label="No")
        self.still.add_checkbutton(
                variable=menu_support.IRS,
                background="#ff0000",
                label="IRS")
        self.still.add_checkbutton(
                variable=menu_support.Charity,
                background="#ff0000",
                label="Charity")
        self.more = Menu(top,tearoff=0)
        self.still.add_cascade(menu=self.more,
                background="#ff0000",
                label="More")
        self.more.add_radiobutton(
                value="Radio_A",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ffff00",
                command=menu_support.radio_a,
                foreground="#000000",
                label="Radio-A")
        self.more.add_radiobutton(
                value="Radio_B",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#00ff00",
                command=menu_support.radio_b,
                foreground="#000000",
                label="Radio-B")
        self._img1 = PhotoImage(file="openfold.gif")
        self.more.add_checkbutton(
                selectcolor="#990000",
                variable=menu_support.Check_1,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ff0000",
                command=menu_support.check1,
                compound="left",
                foreground="#000000",
                image=self._img1,
                label="Check 1")
        self.more.add_checkbutton(
                variable=menu_support.Check_2,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#ff0000",
                command=menu_support.check2,
                foreground="#000000",
                label="Check 2")







if __name__ == '__main__':
    vp_start_gui()



