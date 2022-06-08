from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from pandas import *
from functools import partial
from pyautogui import *
import pyperclip
import tkcap

#import Main_GUI
#from Main_GUI import Main_app
import Main_GUI


class app_6_3_6:
    # Определение рабочей папки
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    config_path = os.path.join(application_path) + "/appdata"

    # Очистка папки Screenshots
    file_end = os.listdir(config_path + "/Screenshots")
    for i in file_end:
        if i.endswith(".png"):
            os.remove(config_path + "/Screenshots/" + i)
    count = 1

    # Ввод переменных
    xl_new = read_excel(config_path + '/logic.xlsx', sheet_name='6_3_6')

    descriptSig = xl_new['Описание входного параметра'].tolist()
    nameSig = xl_new['Название входного параметра'].tolist()
    rangeSig = xl_new['Физический диапазон'].tolist()

    im = config_path + '/Images/Indication_6_3_6/Var4.png'

    logic = open(config_path + '/logic_text/logic_6_3_6.txt', encoding='utf-8').readlines()
    logic = ''.join(logic)

    txt_results = "kj"

    def chek_b1(self):
        v_s = []
        p_s = []
        for l in range(len(app_6_3_6.descriptSig)):
            exec('v_s.append(self.var{}.get())'.format(str(l)))
            exec('p_s.append(self.txt{}.get())'.format(str(l)))
        print(v_s, p_s, sep="\n")

        self.im = app_6_3_6.logik_of_indication(self, v_s, p_s)
        print(self.im)
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        self.x = self.photo.width()
        self.y = self.photo.height()
        self.canvas.delete("all")
        self.canvas.config(width=self.x, height=self.y)
        self.canvas.create_image(6, 6, image=self.photo, anchor=NW)

    def logik_of_indication(self, v_s, p_s):
        if 0 <= p_s[0] <= 36 and 0 <= p_s[1] <= 36 and 0 <= p_s[2] <= 5 and 0 <= p_s[3] <= 1 and 0 <= p_s[4] <= 6 and 0 <= p_s[5] <= 1 and 0 <= p_s[6] <= 1:
            if v_s[0] == 1 and v_s[1] == 1:
                if p_s[0] <= 0 or p_s[1] <= 0:
                    if v_s[4] == 1 and p_s[3] == 1 and (p_s[5] == 0 or p_s[6] == 0):
                        if p_s[4] < 1:
                            im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var1.png"
                            self.result_lbl.config(text="Вариант 1", foreground="black")
                        else:
                            im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var2.jpeg"
                            self.result_lbl.config(text="Вариант 2", foreground="black")
                    else:
                        im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var5.png"
                        self.result_lbl.config(text="Вариант 5\nПропорционально значениям параметра", foreground="black")
                elif p_s[0] <= 3 or p_s[1] <= 3:
                    if v_s[4] == 1 and p_s[3] == 1 and (p_s[5] == 0 or p_s[6] == 0):
                        im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var2.jpeg"
                        self.result_lbl.config(text="Вариант 2", foreground="black")
                    else:
                        im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var5.png"
                        self.result_lbl.config(text="Вариант 5\nПропорционально значениям параметра", foreground="black")
                elif p_s[0] <= 17.3 or p_s[1] <= 17.3:
                    if v_s[4] == 1 and p_s[3] == 1 and (p_s[5] == 0 or p_s[6] == 0):
                        im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var3.png"
                        self.result_lbl.config(text="Вариант 3\nПропорционально значениям параметра", foreground="black")
                    else:
                        im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var5.png"
                        self.result_lbl.config(text="Вариант 5\nПропорционально значениям параметра", foreground="black")
                elif v_s[4] == 1 and p_s[3] == 1 and (p_s[5] == 0 or p_s[6] == 0):
                    im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var4.png"
                    self.result_lbl.config(text="Вариант 4\nПропорционально значениям параметра", foreground="black")
                else:
                    im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var6.png"
                    self.result_lbl.config(text="Вариант 6\nПропорционально значениям параметра", foreground="black")
            else:
                im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Var7.jpeg"
                self.result_lbl.config(text="Вариант 7", foreground="black")
        else:
            im = app_6_3_6.config_path + "/Images/Indication_6_3_6/Error.png"
            self.result_lbl.config(text="Неверное значение", foreground="black")
        return im

    def screen(self):
        cap = tkcap.CAP(self.win)
        cap.capture(app_6_3_6.config_path + "/Screenshots/Screen{}.png".format(str(self.count)))
        self.count += 1

    def copy(self):
        pyperclip.copy(app_6_3_6.logic)
        return 0

    def tests(self, a):
        if a == 1:
            self.txt0.set(0)
            self.txt1.set(0)
            self.txt2.set(0)
            self.txt3.set(1)
            self.txt4.set(1)
            self.txt5.set(0)
            self.txt6.set(0)
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
        elif a == 2:
            self.txt0.set(5)
            self.txt1.set(5)
            self.txt2.set(0)
            self.txt3.set(1)
            self.txt4.set(1)
            self.txt5.set(0)
            self.txt6.set(0)
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
        elif a == 3:
            self.txt0.set(19)
            self.txt1.set(19)
            self.txt2.set(0)
            self.txt3.set(1)
            self.txt4.set(1)
            self.txt5.set(0)
            self.txt6.set(0)
            self.var0.set(1)
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            self.var6.set(1)
        elif a == 4:
            self.txt0.set(19)
            self.txt1.set(19)
            self.txt2.set(0)
            self.txt3.set(1)
            self.txt4.set(1)
            self.txt5.set(0)
            self.txt6.set(0)
            self.var0.set(0)
            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.var5.set(0)
            self.var6.set(0)

    def __init__(self, master, txt_results=None):
        self.win = master
        # Create window
        self.win.title("Логика индикации конфигурации механизации крыла")

        # Style for button
        style = ttk.Style()
        style.configure("TButton", font=("Times New Roman", 14))
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'green')],
                  )

        # Label menu
        self.img1 = Image.open(app_6_3_6.config_path + "/logo.png")
        self.img2 = Image.open(app_6_3_6.config_path + "/ssj1.png")
        self.img3 = Image.open(app_6_3_6.config_path + "/ssj2.png")

        self.width = 400

        self.ratio = (self.width / 3000)
        self.height = int((float(self.img1.size[1]) * float(self.ratio)))
        self.imag1 = self.img1.resize((300, self.height), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.imag1)

        self.imag2 = self.img2.resize((self.width, 150), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.imag2)

        self.imag3 = self.img3.resize((self.width, 150), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.imag3)

        self.fr_back = Frame(self.win, bg='#ececec')
        self.fr_back.pack(side=TOP, fill=X)

        self.panel2 = Label(self.fr_back, image=self.image2)
        self.panel2.pack(side=LEFT)

        self.panel1 = Label(self.fr_back, image=self.image1)
        self.panel1.pack(side=LEFT, expand=YES)

        self.panel3 = Label(self.fr_back, image=self.image3)
        self.panel3.pack(side=RIGHT)

        # Создание панели меню
        self.menu_bar = Menu(self.win)

        self.filemenu = Menu(self.menu_bar)
        self.filemenu.add_command(label="Screenshot", command=self.screen)
        self.filemenu.add_command(label="Close", command=self.close_windows)

        self.menu_bar.add_cascade(label="File", menu=self.filemenu)

        # Начало таблицы
        # Создание заголовков таблицы
        self.fr_main = Frame(self.win, relief=GROOVE, bd=2, bg='black')

        # Настройка скролла для окна ввода данных
        self.canvas_scroll = Canvas(self.fr_main)
        self.scroll_bar = Scrollbar(self.fr_main, orient="vertical", command=self.canvas_scroll.yview)
        self.fr_with_date = Frame(self.canvas_scroll)

        self.fr_with_date.bind(
            "<Configure>",
            lambda e: self.canvas_scroll.configure(
                scrollregion=self.canvas_scroll.bbox("all"),
                width=452,
                height=470
            )
        )

        self.canvas_scroll.create_window((0, 0), window=self.fr_with_date, anchor="nw")

        self.canvas_scroll.configure(yscrollcommand=self.scroll_bar.set)

        self.canvas_scroll.pack(side=LEFT, fill=BOTH, expand=1)
        self.scroll_bar.pack(side=RIGHT, fill=Y)

        self.fr = Frame(self.fr_with_date, relief=RIDGE, bd=1, width=150, bg='black')
        self.lbl0 = Label(self.fr, text="Описание\nвходного параметра", font=("Times New Roman", 11), width=24,
                          height=2, bg='#ececec')
        self.lbl1 = Label(self.fr, text="Название входного\nпараметра", font=("Times New Roman", 11), width=16,
                          height=2, bg='#ececec')
        self.lbl2 = Label(self.fr, text="Валидность\nсигнала", font=("Times New Roman", 11), width=12, height=2, bg='#ececec')
        self.lbl3 = Label(self.fr, text="Значение\nсигнала", font=("Times New Roman", 11), width=9, height=2, bg='#ececec')
        self.lbl4 = Label(self.fr, text="Физический\nдиапазон", font=("Times New Roman", 11), width=9, height=2, bg='#ececec')

        self.fr.pack(side=TOP)
        self.lbl0.pack(side=LEFT)
        self.lbl1.pack(side=LEFT)
        self.lbl2.pack(side=LEFT)
        self.lbl3.pack(side=LEFT)
        self.lbl4.pack(side=LEFT)
        self.fr_main.pack(side=LEFT, fill=BOTH)

        # Циклическое создание таблицы
        for i in range(len(app_6_3_6.descriptSig)):
            exec('self.txt{} = DoubleVar()'.format(str(i)))
            exec('self.var{} = IntVar()'.format(str(i)))
            exec('self.var{}.set(1)'.format(str(i)))

            # Начало рамки для табличных значений #############################################
            exec('self.fr{} = Frame(self.fr_with_date, relief=GROOVE, bd=1, width=70, bg="black")'.format(str(i)))

            # Ячейка с описанием параметра
            exec('self.text{} = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=23, wrap=WORD, '
                 'bg ="#ececec")'.format(str(i), str(i)))
            exec('self.text{}.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.text{}.insert(1.0, "{}")'.format(str(i), app_6_3_6.descriptSig[i]))
            exec('self.text{}.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.text{}.config(state=DISABLED)'.format(str(i)))

            # Ячейка с именем параметра
            exec('self.lbl{} = Label(self.fr{}, text="{}", font=("Times New Roman", 11), width=16, height=2)'.format(
                str(i), str(i), app_6_3_6.nameSig[i]))

            # Ячейка с выбором валидности сигнала
            exec(
                "self.chb{} = Checkbutton(self.fr{}, text='Валиден', cursor='exchange', font=('Times New Roman', 11), variable=self.var{}, onvalue=1, offvalue=0, width=12, height=2)".format(
                    str(i), str(i), str(i)))

            # Ячейка с вводом значения параметра
            exec(
                "self.ent{} = Entry(self.fr{}, textvariable=self.txt{}, font=('Times New Roman', 11), relief=GROOVE, width=8)".format(
                    str(i), str(i), str(i)))

            # Ячейка c диапазоном возможных значений
            exec('self.text{}1 = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=9, wrap=WORD, bg="#ececec")'.format(
                str(i), str(i)))
            exec('self.text{}1.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.text{}1.insert(1.0, "{}")'.format(str(i), app_6_3_6.rangeSig[i]))
            exec('self.text{}1.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.text{}1.config(state=DISABLED)'.format(str(i)))

            # Расположение Виджетов
            exec('self.text{}.pack(side=LEFT)'.format(str(i)))
            exec("self.lbl{}.pack(side=LEFT, fill=Y)".format(str(i)))
            exec("self.chb{}.pack(side=LEFT)".format(str(i)))
            exec("self.ent{}.pack(side=LEFT, fill=Y)".format(str(i)))
            exec("self.text{}1.pack(side=LEFT, fill=Y)".format(str(i)))
            exec("self.fr{}.pack(side=TOP)".format(str(i)))
        # Конец таблицы ###################################################

        self.fr_results = Frame(self.win, bg='#ececec')

        self.fr_tests = Frame(self.fr_results, relief=GROOVE)
        self.fr_tests_l = Frame(self.fr_tests)
        self.fr_tests_r = Frame(self.fr_tests)
        self.fr_copy_and_screen = Frame(self.fr_results)
        self.fr_logic = Frame(self.win, relief=GROOVE, bd=2, bg='black')

        self.start_bt = ttk.Button(self.fr_results, text="START", cursor="hand1", command=self.chek_b1,
                                   style="C.TButton")

        self.result_lbl = Label(self.fr_results, text=txt_results)

        self.test1 = ttk.Button(self.fr_tests_l, text="Вариант 1", cursor="hand1", command=partial(self.tests, 1),
                                style="C.TButton")
        self.test2 = ttk.Button(self.fr_tests_r, text="Вариант 3", cursor="hand1", command=partial(self.tests, 2),
                                style="C.TButton")
        self.test3 = ttk.Button(self.fr_tests_l, text="Вариант 5", cursor="hand1", command=partial(self.tests, 3),
                                style="C.TButton")
        self.test4 = ttk.Button(self.fr_tests_r, text="Вариант 7", cursor="hand1", command=partial(self.tests, 4),
                                style="C.TButton")
        self.btn_copy = Button(self.fr_copy_and_screen, text="Copy", font=('Times New Roman', 14), command=self.copy,
                               width=11, cursor="hand1")
        self.btn_screenshot = Button(self.fr_copy_and_screen, text="Save screen", font=("Times New Roman", 14),
                                     cursor="hand1", command=self.screen, width=11)

        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        self.x = self.photo.width()
        self.y = self.photo.height()
        self.canvas = Canvas(self.fr_results, relief="ridge", bd=4, height=self.y, width=self.x)

        self.scr = Scrollbar(self.fr_logic, orient=VERTICAL)
        self.text = Text(self.fr_logic, font=("Times New Roman", 12), width=70, yscrollcommand=self.scr.set)
        self.text.insert(END, app_6_3_6.logic)
        self.text["state"] = DISABLED

        self.scr.config(command=self.text)

        self.fr_results.pack(side=LEFT, fill=BOTH)
        self.canvas.pack(side=TOP)

        # Добавим изображение
        self.c_image = self.canvas.create_image(6, 6, image=self.photo, anchor='nw')

        self.start_bt.pack()
        self.result_lbl.pack()
        self.fr_tests.pack(side=TOP)
        self.fr_tests_l.pack(side=LEFT)
        self.fr_tests_r.pack(side=RIGHT)
        self.test1.pack(fill=BOTH)
        self.test2.pack(fill=BOTH)
        self.test3.pack(fill=BOTH)
        self.test4.pack(fill=BOTH)
        self.fr_copy_and_screen.pack(side=BOTTOM)
        self.btn_screenshot.pack(side=LEFT)
        self.btn_copy.pack(side=LEFT)
        self.fr_logic.pack(side=LEFT, fill=BOTH)
        self.scr.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=BOTH)

        self.win.config(menu=self.menu_bar)

    def close_windows(self):
        self.win.destroy()
