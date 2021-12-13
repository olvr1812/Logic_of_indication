from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


def clicked1():
    res = "Valid signals = {}".format(txt.get())
    lbl.configure(text=res)

window = Tk() # Создаем окно
window.title("Отработка логики индикации") # Название окна
window.geometry('800x400') # Размер окна

btn = Button(window, text = 'START', bg='black', fg='red', command=clicked1, font=("Times New Roman", 14)) # Кнопка и ее параметры
btn.grid(column=2, row=0)

lbl = Label(window, text='Valid signal:')
lbl.grid(column=1, row=2)

txt = Entry(window, width=50, font=('Times New Roman', 14))
txt.grid(column=0,row=2)
txt.focus

combo = Combobox(window, font=("Times New Roman", 14), width=50, values=["Обозначение индикации состояния предкрылков", "Обозначение индикации состояния закрылков", "Индикация положения РУМК", "Индикация положения РУМК"])
combo.current(0)
combo.grid(column=0,row=1)

window.mainloop()
