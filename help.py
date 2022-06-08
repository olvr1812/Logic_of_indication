from tkinter import *
from openpyxl import load_workbook
from PIL import Image, ImageTk
from pyautogui import *
import tkcap
import pyperclip
from functools import partial
from tkinter.ttk import Combobox
import Indicate_6_3_8



class Main_app():

    def __init__(self):
        self.win = Tk()
        self.win.title("Окно выбора логики для анализа")
        self.win.geometry("800x200+300+300")
        self.fr = Frame(self.win, relief=RIDGE, bd=2)
        self.fr1 = Frame(self.win, relief=RIDGE, bd=2)
        # Создание комбобокса
        self.comboExample = Combobox(self.fr,
                                values=[
                                    "Логика индикации конфигурации механизации крыла",
                                    "February",
                                    "March",
                                    "April"])

        # Создание и настройка кнопок

        self.btn = Button(self.fr, text="Open", command=self.open)
        self.btn1 = Button(self.fr1, text="Закрыть", command=self.close)


        # Расположение виджетов
        self.fr.pack(side=TOP)
        self.fr1.pack(side=TOP)
        self.comboExample.pack(side=LEFT)
        self.btn.pack(side=LEFT)
        self.btn1.pack(side=TOP)

        self.comboExample.bind("<<ComboboxSelected>>", self.choose_new)

        self.win.mainloop()

    def close(self):
        self.win.destroy()

    def choose_new(self, event):
        print(self.comboExample.current(), self.comboExample.get())

    def open(self):
        return indicate_6_3_8.app_6_3_8

        #indicate_6_3_8.win.deiconify()


app = Main_app()