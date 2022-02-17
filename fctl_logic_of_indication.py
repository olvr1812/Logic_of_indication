from tkinter import *
from pyautogui import *
from PIL import Image, ImageTk
from pandas import *

import indicate_5_10_1
import indicate_6_3_8


class fctl_logic:

    def __init__(self, master):
        # Определение рабочей папки
        self.newWindow = None
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path) + "/appdata"

        xl_new = read_excel(config_path + '/List_indication.xlsx')
        FCTL_logic = xl_new['Индикация FCTL'].dropna().tolist()

        self.choose_indicate = 'Индикация не выбрана'
        self.acts = FCTL_logic

        # Create image list
        self.img_list = []
        img_path = config_path + "/FCTL_img"
        for root, dirs, files in os.walk(img_path):
            files.sort()
            for file in files:
                print(files)
                self.img_list.append(os.path.join(root, file))

        self.img_of_selected_logic = Image.open(self.img_list[0])
        self.w, self.h = self.img_of_selected_logic.size
        self.k_resize = self.w / self.h
        self.img_of_selected_logic = self.img_of_selected_logic.resize((int(159 * self.k_resize), int(159)),
                                                                       Image.ANTIALIAS)
        self.img_of_selected_logic = ImageTk.PhotoImage(self.img_of_selected_logic)

        self.height = self.img_of_selected_logic.height()
        self.width = self.img_of_selected_logic.width()

        self.img_FCTL = Image.open(config_path + '/FCTL.png')
        self.img_FCTL = self.img_FCTL.resize((564, 422), Image.ANTIALIAS)
        self.fctl = ImageTk.PhotoImage(self.img_FCTL)

        # Create window.
        self.win = master
        self.win.title('Индикация FCTL')
        self.win.geometry('850x422')

        # Create frames.
        self.fr_main = Frame(self.win)
        self.fr_list_box = LabelFrame(self.fr_main, text="Выбор логики индикации")

        # Button for close.
        self.btn_close = Button(self.fr_main, text='Close', command=self.close_window)

        self.canvas = Canvas(self.win, width=564, height=422)
        self.image = self.canvas.create_image(0, 0, image=self.fctl, anchor=NW)

        self.scroll_x = Scrollbar(self.fr_list_box, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.fr_list_box, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.pack(side=BOTTOM, fill=X)

        self.canv_selected_logic = Canvas(self.fr_main, width=self.width, height=self.height, bg='grey')
        self.selected_logic = self.canv_selected_logic.create_image(0, 0, image=self.img_of_selected_logic, anchor=NW)

        self.lb = Listbox(self.fr_list_box, xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set, width=30)

        self.scroll_y.config(command=self.lb.yview)
        self.scroll_x.config(command=self.lb.xview)

        for i in self.acts:
            self.lb.insert(END, i)

        self.lb.bind("<<ListboxSelect>>", self.select_indicate)
        self.lb.pack(fill=BOTH)

        self.var = StringVar()
        self.btn_open_logic = Button(self.fr_main, text='Open')
        self.btn_open_logic.bind('<Button-1>', self.open_indicate)
        self.btn_open_logic.bind('<Return>', self.open_indicate)
        self.btn_open_logic.pack()

        self.fr_main.pack(side=LEFT, fill=Y)
        self.canvas.pack(side=RIGHT)
        self.fr_list_box.pack(fill=BOTH)
        self.btn_close.pack()
        self.canv_selected_logic.pack(expand=1)

    def open_indicate(self, event):
        if self.choose_indicate == 'Индикация положения РУМК':
            self.newWindow = Toplevel(self.win)
            self.app = indicate_6_3_8.app_6_3_8(self.newWindow)
        elif self.choose_indicate == 'Индикация состояния первого канала системы дистанционного управления':
            self.newWindow = Toplevel(self.win)
            self.app = indicate_5_10_1.app_5_10_1(self.newWindow)
        else:
            self.var.set('Данный параметр не задан')

    def select_indicate(self, val):
        sender = val.widget
        idx = sender.curselection()
        self.choose_indicate = sender.get(idx)
        self.img_of_selected_logic = Image.open(self.img_list[idx[0]])
        self.w, self.h = self.img_of_selected_logic.size

        if self.w < self.h:
            self.k_resize = self.w / self.h
            self.img_of_selected_logic = self.img_of_selected_logic.resize((int(159 * self.k_resize), int(159)), Image.ANTIALIAS)
        else:
            self.k_resize = self.h / self.w
            self.img_of_selected_logic = self.img_of_selected_logic.resize((int(159), int(159 * self.k_resize)),
                                                                           Image.ANTIALIAS)
        self.img_of_selected_logic = ImageTk.PhotoImage(self.img_of_selected_logic)
        height = self.img_of_selected_logic.height()
        width = self.img_of_selected_logic.width()
        self.canv_selected_logic.delete("all")
        self.canv_selected_logic.config(height=height, width=width)
        self.canv_selected_logic.create_image(0, 0, image=self.img_of_selected_logic, anchor=NW)

        self.canv_selected_logic.pack(expand=1)
        self.btn_open_logic.focus_set()



    def close_window(self):
        self.win.destroy()
