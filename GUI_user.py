from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

i: IntVar = 0
k: IntVar = 0
win = Tk()
win.geometry("600x400")
while i != 5:
    exec("fr{} = Button(win, text='Значение i = {}')".format(str(i), str(i)))
    exec("fr{}.pack(side=TOP)".format(str(i)))
    i += 1
win.mainloop()
