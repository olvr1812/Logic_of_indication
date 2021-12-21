from tkinter import *
from PIL import Image, ImageTk
from pyautogui import *
import tkcap
import pyperclip


class Indication_6_3_8:
    count = 0
    im = 'Indication/Var4.png'

    def __init__(self):

        # Создание окна
        self.im = "Indication/Var4.png"
        self.win = Tk()
        self.win.title("Логика индикации конфигурации механизации крыла")
        self.win.geometry("1180x625+0+0")
        self.win.resizable(False, False)

        # Входные переменные
        self.var1 = IntVar()
        self.var1.set(1)
        self.var2 = IntVar()
        self.var2.set(1)
        self.var3 = IntVar()
        self.var3.set(1)
        self.var4 = IntVar()
        self.var4.set(1)
        self.var5 = IntVar()
        self.var5.set(1)
        self.var6 = IntVar()
        self.var6.set(1)
        self.var7 = IntVar()
        self.var7.set(1)
        self.var8 = IntVar()
        self.var8.set(1)
        self.var9 = IntVar()
        self.var9.set(1)
        self.var10 = IntVar()
        self.var10.set(1)
        self.var11 = IntVar()
        self.var11.set(1)
        self.var12 = IntVar()
        self.var12.set(1)
        self.var13 = IntVar()
        self.var13.set(1)
        self.logic = open('logic_text/logic_6_3_8.txt', encoding='utf-8').readlines()
        self.logic = ''.join(self.logic)

        self.txt1 = DoubleVar()
        self.txt2 = DoubleVar()
        self.txt3 = DoubleVar()
        self.txt4 = DoubleVar()
        self.txt5 = IntVar()
        self.txt6 = IntVar()
        self.txt7 = IntVar()
        self.txt8 = IntVar()
        self.txt9 = IntVar()
        self.txt10 = IntVar()
        self.txt11 = IntVar()
        self.txt11.set(1)
        self.txt12 = IntVar()
        self.txt13 = IntVar()

        # Создание панели меню
        self.menu_bar = Menu(self.win)

        self.filemenu = Menu(self.menu_bar)
        self.filemenu.add_command(label="Main", command=self.open_main)
        self.filemenu.add_command(label="Screenshot", command=self.screen)
        self.filemenu.add_command(label="Close", command=self.win.quit)

        self.menu_bar.add_cascade(label="File", menu=self.filemenu)

        # Создание областей для виджетов
        self.fr_main = Frame(self.win)
        self.fr_results = Frame(self.win)
        self.fr = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr1 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr2 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr3 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr4 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr5 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr6 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr7 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr8 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr9 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr10 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr11 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr12 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr13 = Frame(self.fr_main, relief="ridge", bd=1)
        self.fr_start = Frame(self.fr_results, relief="raised", bd=4, bg="black")
        self.fr_copy = Frame(self.fr_results, relief="raised", bd=4)
        self.fr_screen = Frame(self.fr_results, relief="raised", bd=4)
        self.fr_logic = Frame(self.win, relief=RIDGE, bd=6)

        # Создание и настройка виджетов
        self.lbl0 = Label(self.fr, text="Описание\nвходного параметра", font=("Times New Roman", 11), width=23,
                          height=2)
        self.lbl1 = Label(self.fr, text="Название входного\nпараметра", font=("Times New Roman", 11), width=16,
                          height=2)
        self.lbl2 = Label(self.fr, text="Валидность\nсигнала", font=("Times New Roman", 11), width=12, height=2)
        self.lbl3 = Label(self.fr, text="Значение\nсигнала", font=("Times New Roman", 11), width=9, height=2)
        self.lbl4 = Label(self.fr, text="Физический\nдиапазон", font=("Times New Roman", 11), width=10, height=2)

        self.lbl10 = Label(self.fr1, text="Текущее\nположение\nпредкрылков (квор) 1 п/к", font=("Times New Roman", 11),
                           width=23, height=3)
        self.lbl11 = Label(self.fr1, text="DPK1", font=("Times New Roman", 12), width=16, height=2)
        self.chb11 = Checkbutton(self.fr1, text="Валиден", cursor="exchange", font=("Times New Roman", 11),
                                 variable=self.var1, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent11 = Entry(self.fr1, textvariable=self.txt1, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl12 = Label(self.fr1, text="[0...24] град.", font=("Times New Roman", 11), width=10, height=2)

        self.lbl20 = Label(self.fr2, text="Текущее\nположение\nпредкрылков (квор) 2 п/к", font=("Times New Roman", 11),
                           width=23, height=3)
        self.lbl21 = Label(self.fr2, text="DPK2", font=("Times New Roman", 11), width=16, height=2)
        self.chb21 = Checkbutton(self.fr2, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                 variable=self.var2, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent21 = Entry(self.fr2, textvariable=self.txt2, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl22 = Label(self.fr2, text="[0...24] град.", font=("Times New Roman", 11), width=10, height=2)

        self.lbl30 = Label(self.fr3, text="Текущее\nположение\nзакрылков (квор) 1 п/к", font=("Times New Roman", 11),
                           width=23, height=3)
        self.lbl31 = Label(self.fr3, text="DZK1", font=("Times New Roman", 11), width=16, height=2)
        self.chb31 = Checkbutton(self.fr3, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                 variable=self.var3, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent31 = Entry(self.fr3, textvariable=self.txt3, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl32 = Label(self.fr3, text="[0...36] град.", font=("Times New Roman", 11), width=10, height=2)

        self.lbl40 = Label(self.fr4, text="Текущее\nположение\nзакрылков (квор) 2 п/к", font=("Times New Roman", 11),
                           width=23, height=3)
        self.lbl41 = Label(self.fr4, text="DZK2", font=("Times New Roman", 11), width=16, height=2)
        self.chb41 = Checkbutton(self.fr4, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                 variable=self.var4, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent41 = Entry(self.fr4, textvariable=self.txt4, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl42 = Label(self.fr4, text="[0...36] град.", font=("Times New Roman", 11), width=10, height=2)

        self.lbl50 = Label(self.fr5, text="Отказ 1 п/к\nзакрылков", font=("Times New Roman", 11), width=23, height=3)
        self.lbl51 = Label(self.fr5, text="FLAPS_1_FAULT", font=("Times New Roman", 11), width=16, height=2)
        self.chb51 = Checkbutton(self.fr5, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                 variable=self.var5, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent51 = Entry(self.fr5, textvariable=self.txt5, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl52 = Label(self.fr5, text="True - 1\nFalse - 0", font=("Times New Roman", 11), width=10, height=2)

        self.lbl60 = Label(self.fr6, text="Отказ 2 п/к\nзакрылков", font=("Times New Roman", 11), width=23, height=3)
        self.lbl61 = Label(self.fr6, text="FLAPS_2_FAULT", font=("Times New Roman", 11), width=16, height=2)
        self.chb61 = Checkbutton(self.fr6, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                 variable=self.var6, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent61 = Entry(self.fr6, textvariable=self.txt6, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl62 = Label(self.fr6, text="True - 1\nFalse - 0", font=("Times New Roman", 11), width=10, height=2)

        self.lbl70 = Label(self.fr7, text="Отказ 1 п/к\nпредкрылков", font=("Times New Roman", 11), width=23, height=3)
        self.lbl71 = Label(self.fr7, text="SLATS_1_FAULT", font=("Times New Roman", 11), width=16, height=2)
        self.chb71 = Checkbutton(self.fr7, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                 variable=self.var7, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent71 = Entry(self.fr7, textvariable=self.txt7, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl72 = Label(self.fr7, text="True - 1\nFalse - 0", font=("Times New Roman", 11), width=10, height=2)

        self.lbl80 = Label(self.fr8, text="Отказ 2 п/к\nпредкрылков", font=("Times New Roman", 11), width=23, height=3)
        self.lbl81 = Label(self.fr8, text="SLATS_2_FAULT", font=("Times New Roman", 11), width=16, height=2)
        self.chb81 = Checkbutton(self.fr8, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                 variable=self.var8, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent81 = Entry(self.fr8, textvariable=self.txt8, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl82 = Label(self.fr8, text="True - 1\nFalse - 0", font=("Times New Roman", 11), width=10, height=2)

        self.lbl90 = Label(self.fr9, text="Положение\nмеханизации", font=("Times New Roman", 11), width=23, height=3)
        self.lbl91 = Label(self.fr9, text="X_MHZN", font=("Times New Roman", 11), width=16, height=2)
        self.chb91 = Checkbutton(self.fr9, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                 variable=self.var9, onvalue=1, offvalue=0,
                                 width=12, height=2)
        self.ent91 = Entry(self.fr9, textvariable=self.txt9, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl92 = Label(self.fr9, text="[0;6]", font=("Times New Roman", 11), width=10, height=2)

        self.lbl100 = Label(self.fr10, text="Положение\nРУМК", font=("Times New Roman", 11), width=23, height=3)
        self.lbl101 = Label(self.fr10, text="X_FCM", font=("Times New Roman", 11), width=16, height=2)
        self.chb101 = Checkbutton(self.fr10, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                  variable=self.var10, onvalue=1, offvalue=0,
                                  width=12, height=2)
        self.ent101 = Entry(self.fr10, textvariable=self.txt10, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl102 = Label(self.fr10, text="[0;4]", font=("Times New Roman", 11), width=10, height=2)

        self.lbl110 = Label(self.fr11, text="Валидность\nсигнала\nположения РУМК", font=("Times New Roman", 12),
                            width=23, height=3)
        self.lbl111 = Label(self.fr11, text="X_FCM_valid", font=("Times New Roman", 11), width=16, height=2)
        self.chb111 = Checkbutton(self.fr11, text="Валиден", font=("Times New Roman", 11), width=12, height=2)
        self.ent111 = Entry(self.fr11, textvariable=self.txt11, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl112 = Label(self.fr11, text="True - 1\nFalse - 0", font=("Times New Roman", 11), width=10, height=2)

        self.lbl120 = Label(self.fr12, text="Статус захода\nпо крутой\nглиссаде от САУ", font=("Times New Roman", 12),
                            width=23, height=3)
        self.lbl121 = Label(self.fr12, text="S/A", font=("Times New Roman", 11), width=16, height=2)
        self.chb121 = Checkbutton(self.fr12, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                  variable=self.var12, onvalue=1, offvalue=0,
                                  width=12, height=2)
        self.ent121 = Entry(self.fr12, textvariable=self.txt12, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl122 = Label(self.fr12, text="True - 1\nFalse - 0", font=("Times New Roman", 11), width=10, height=2)

        self.lbl130 = Label(self.fr13, text="Обратная связь\nот FCC при получении\nстатуса захода",
                            font=("Times New Roman", 11),
                            width=23, height=3)
        self.lbl131 = Label(self.fr13, text="S/A_FEEDBACK", font=("Times New Roman", 11), width=16, height=2)
        self.chb131 = Checkbutton(self.fr13, text="Валиден", font=("Times New Roman", 11), cursor="exchange",
                                  variable=self.var13, onvalue=1, offvalue=0,
                                  width=12, height=2)
        self.ent131 = Entry(self.fr13, textvariable=self.txt13, font=("Times New Roman", 11), relief="ridge", width=8)
        self.lbl132 = Label(self.fr13, text="True - 1\nFalse - 0", font=("Times New Roman", 11), width=10, height=2)

        self.start = Button(self.fr_start, text="START", font=("Times New Roman", 20), fg="red",
                            activeforeground="#ADFF2F", cursor="hand1", command=self.chek_b1, width=11)
        self.copy = Button(self.fr_copy, text="Copy", font=('Times New Roman', 20), command=self.copy, width=11)
        self.scr_and_sf = Button(self.fr_screen, text="Save screen", font=("Times New Roman", 20), cursor="pirate",
                                 command=self.screen, width=11)
        self.canvas = Canvas(self.fr_results, relief="ridge", bd=4, height=47, width=138)

        self.text = Text(self.fr_logic, font=("Times New Roman", 12), width=200)
        self.text.insert(END, self.logic)

        self.scr = Scrollbar(self.fr_logic)

        # Блокирование виджетов
        self.chb111["state"] = DISABLED
        self.text["state"] = DISABLED

        # Добавим изображение
        self.image = Image.open(Indication_6_3_8.im)
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(60, 160, anchor='nw', image=self.photo)
        print(self.image, "\n", self.photo, "\n", self.c_image)

        # Расположение виджетов
        self.fr_main.pack(side=LEFT, fill=Y)
        self.fr.pack(side=TOP)
        self.lbl0.pack(side=LEFT)
        self.lbl1.pack(side=LEFT)
        self.lbl2.pack(side=LEFT)
        self.lbl3.pack(side=LEFT)
        self.lbl4.pack(side=LEFT)

        self.fr1.pack(side=TOP)
        self.lbl10.pack(side=LEFT)
        self.lbl11.pack(side=LEFT)
        self.chb11.pack(side=LEFT)
        self.ent11.pack(side=LEFT, padx=2)
        self.lbl12.pack(side=LEFT)

        self.fr2.pack(side=TOP)
        self.lbl20.pack(side=LEFT)
        self.lbl21.pack(side=LEFT)
        self.chb21.pack(side=LEFT)
        self.ent21.pack(side=LEFT, padx=2)
        self.lbl22.pack(side=LEFT)

        self.fr3.pack(side=TOP)
        self.lbl30.pack(side=LEFT)
        self.lbl31.pack(side=LEFT)
        self.chb31.pack(side=LEFT)
        self.ent31.pack(side=LEFT, padx=2)
        self.lbl32.pack(side=LEFT)

        self.fr4.pack(side=TOP)
        self.lbl40.pack(side=LEFT)
        self.lbl41.pack(side=LEFT)
        self.chb41.pack(side=LEFT)
        self.ent41.pack(side=LEFT, padx=2)
        self.lbl42.pack(side=LEFT)

        self.fr5.pack(side=TOP)
        self.lbl50.pack(side=LEFT)
        self.lbl51.pack(side=LEFT)
        self.chb51.pack(side=LEFT)
        self.ent51.pack(side=LEFT, padx=2)
        self.lbl52.pack(side=LEFT)

        self.fr6.pack(side=TOP)
        self.lbl60.pack(side=LEFT)
        self.lbl61.pack(side=LEFT)
        self.chb61.pack(side=LEFT)
        self.ent61.pack(side=LEFT, padx=2)
        self.lbl62.pack(side=LEFT)

        self.fr7.pack(side=TOP)
        self.lbl70.pack(side=LEFT)
        self.lbl71.pack(side=LEFT)
        self.chb71.pack(side=LEFT)
        self.ent71.pack(side=LEFT, padx=2)
        self.lbl72.pack(side=LEFT)

        self.fr8.pack(side=TOP)
        self.lbl80.pack(side=LEFT)
        self.lbl81.pack(side=LEFT)
        self.chb81.pack(side=LEFT)
        self.ent81.pack(side=LEFT, padx=2)
        self.lbl82.pack(side=LEFT)

        self.fr9.pack(side=TOP)
        self.lbl90.pack(side=LEFT)
        self.lbl91.pack(side=LEFT)
        self.chb91.pack(side=LEFT)
        self.ent91.pack(side=LEFT, padx=2)
        self.lbl92.pack(side=LEFT)

        self.fr10.pack(side=TOP)
        self.lbl100.pack(side=LEFT)
        self.lbl101.pack(side=LEFT)
        self.chb101.pack(side=LEFT)
        self.ent101.pack(side=LEFT, padx=2)
        self.lbl102.pack(side=LEFT)

        self.fr11.pack(side=TOP)
        self.lbl110.pack(side=LEFT)
        self.lbl111.pack(side=LEFT)
        self.chb111.pack(side=LEFT)
        self.ent111.pack(side=LEFT, padx=2)
        self.lbl112.pack(side=LEFT)

        self.fr12.pack(side=TOP)
        self.lbl120.pack(side=LEFT)
        self.lbl121.pack(side=LEFT)
        self.chb121.pack(side=LEFT)
        self.ent121.pack(side=LEFT, padx=2)
        self.lbl122.pack(side=LEFT)

        self.fr13.pack(side=TOP)
        self.lbl130.pack(side=LEFT)
        self.lbl131.pack(side=LEFT)
        self.chb131.pack(side=LEFT)
        self.ent131.pack(side=LEFT, padx=2)
        self.lbl132.pack(side=LEFT)

        # self.close.pack(side=LEFT, anchor=W)
        self.fr_results.pack(side=LEFT, fill=BOTH)
        self.canvas.pack(side=TOP)
        self.fr_start.pack(side=TOP)
        self.start.pack()
        self.fr_screen.pack(side=BOTTOM)
        self.scr_and_sf.pack()
        self.fr_copy.pack(side=BOTTOM)
        self.copy.pack()
        self.fr_logic.pack(side=LEFT, fill=BOTH)
        self.scr.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=BOTH)

        self.win.config(menu=self.menu_bar)

        self.win.mainloop()

    def logik_of_indication(v_s, p_s):
        if 0 <= p_s[0] <= 24 and 0 <= p_s[1] <= 24 and 0 <= p_s[2] <= 36 and 0 <= p_s[3] <= 36 and 0 <= p_s[4] <= 1 \
                and 0 <= p_s[5] <= 1 and 0 <= p_s[6] <= 1 and 0 <= p_s[7] <= 1 and 0 <= p_s[8] <= 6 and 0 <= p_s[9] <= 4 \
                and 0 <= p_s[10] <= 1 and 0 <= p_s[11] <= 1 and 0 <= p_s[12] <= 1:
            if v_s[8] == 1 and (v_s[0] == 1 or v_s[1] == 1) and (v_s[2] == 1 or v_s[3] == 1) and v_s[8] == 1 and p_s[10] == 1:

                if p_s[8] == 0 and p_s[9] == 0:  # СУМК = 0 РУМК = 0
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 0 or p_s[1] == 0) and (p_s[2] == 0 or p_s[3] == 0):
                            print('Вариант 4 | FLAP 0 - надпись отсутствует')
                            im = "Indication/Var4.png"

                        else:
                            print('Вариант 5 | FLAP 0 - цвет голубой')
                            im = "Indication/Var5.png"
                    else:
                        print('Вариант 6 | FLAP 0 - цвет янтарный')
                        im = "Indication/Var6.png"

                elif p_s[8] == 1 and p_s[9] == 0:  # СУМК = 1 РУМК = 0
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 0 or p_s[1] == 0) and (p_s[2] == 1 or p_s[3] == 1):
                            print('Вариант 21 | FLAP ICE - зеленый')
                            im = "Indication/Var21.png"
                        else:
                            print('Вариант 20 | FLAP ICE - цвет голубой')
                            im = "Indication/Var20.png"
                    else:
                        print('Вариант 22 | FLAP ICE - цвет янтарный')
                        im = "Indication/Var22.png"

                elif p_s[8] == 2 and p_s[9] == 1:  # СУМК 2 РУМК = 1
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 18 or p_s[1] == 18) and (p_s[2] == 3 or p_s[3] == 3):
                            print('Вариант 7 | FLAP 1 - зеленый')
                            im = "Indication/Var7.png"
                        else:
                            print('Вариант 8 | FLAP 1 - цвет голубой')
                            im = "Indication/Var8.png"
                    else:
                        print('Вариант 9 | FLAP 1 - цвет янтарный')
                        im = "Indication/Var9.png"

                elif p_s[8] == 3 and p_s[9] == 1:  # СУМК = 3 РУМК = 1
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 18 or p_s[1] == 18) and (p_s[2] == 9 or p_s[3] == 9):
                            print('Вариант 10 | FLAP 1 + F - зеленый')
                            im = "Indication/Var10.png"
                        else:
                            print('Вариант 11 | FLAP 1 + F - цвет голубой')
                            im = "Indication/Var11.png"
                    else:
                        print('Вариант 12 | FLAP 1 + F - цвет янтарный')
                        im = "Indication/Var12.png"

                elif p_s[8] == 4 and p_s[9] == 2:  # СУМК = 4 РУМК = 2
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 16 or p_s[3] == 16):
                            print('Вариант 13 | FLAP 2 - зеленый')
                            im = "Indication/Var13.png"
                        else:
                            print('Вариант 14 | FLAP 2 - цвет голубой')
                            im = "Indication/Var14.png"
                    else:
                        print('Вариант 15 | FLAP 2 - цвет янтарный')
                        im = "Indication/Var15.png"

                elif p_s[8] == 5 and p_s[9] == 3:
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 25 or p_s[3] == 25):
                            print('Вариант 16 | FLAP 3 - зеленый')
                            im = "Indication/Var16.png"
                        else:
                            print('Вариант 17 | FLAP 3 - цвет голубой')
                            im = "Indication/Var17.png"
                    else:
                        print('Вариант 18 | FLAP 3 - цвет янтарный')
                        im = "Indication/Var18.png"
                elif p_s[8] == 6 and p_s[9] == 4:
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 36 or p_s[3] == 36):
                            if p_s[11] == 1:
                                if v_s[10] == 1 and v_s[11] == 1 and p_s[12] == 1:
                                    print('Вариант 23 | FULL-S/A - цвет зеленый')
                                    im = "Indication/Var23.png"
                                else:
                                    print('Вариант 24 | FULL-S/A - цвет янтарный')
                                    im = "Indication/Var24.png"
                            else:
                                print('Вариант 1 | FULL - цвет зеленый')
                                im = "Indication/Var1.png"
                        else:
                            print('Вариант 2 | FULL - цвет синий')
                            im = "Indication/Var2.png"
                    else:
                        print('Вариант 3 | FULL - цвет янтарный')
                        im = "Indication/Var3.png"
                else:
                    print('Вариант 3 | FULL - цвет янтарный')
                    im = "Indication/Var3.png"

            else:
                print('Вариант 19 | XXXX')
                im = "Indication/Var19.png"
        else:
            im = "Indication/Error.png"
        return im

    def chek_b1(self):
        global im
        v_s = []
        p_s = []
        v_s.append(self.var1.get())
        v_s.append(self.var2.get())
        v_s.append(self.var3.get())
        v_s.append(self.var4.get())
        v_s.append(self.var5.get())
        v_s.append(self.var6.get())
        v_s.append(self.var7.get())
        v_s.append(self.var8.get())
        v_s.append(self.var9.get())
        v_s.append(self.var10.get())
        v_s.append(self.var12.get())
        v_s.append(self.var13.get())

        p_s.append(self.txt1.get())
        p_s.append(self.txt2.get())
        p_s.append(self.txt3.get())
        p_s.append(self.txt4.get())
        p_s.append(self.txt5.get())
        p_s.append(self.txt6.get())
        p_s.append(self.txt7.get())
        p_s.append(self.txt8.get())
        p_s.append(self.txt9.get())
        p_s.append(self.txt10.get())
        p_s.append(self.txt11.get())
        p_s.append(self.txt12.get())
        p_s.append(self.txt13.get())

        self.im = Indication_6_3_8.logik_of_indication(v_s, p_s)
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack(side=TOP)
        #print(self.im, self.image, self.photo, self.c_image, sep='\n')
        print(v_s, '\n', p_s)


    def load_image(name):
        img = Image.open(name)
        img.thumbnail((200, 200), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def screen(self):
        self.count += 1
        cap = tkcap.CAP(self.win)
        cap.capture("Screenshots/Screen{}.png".format(str(self.count)))

    def copy(self):
        self.f = open("../../Test_log.txt", "w")
        self.f.write(self.logic)
        self.f.close()
        pyperclip.copy(self.logic)

    def open_main(self):
        self.win.destroy()
        import help

    def go_away(self):
        self.win.withdraw()

    def come_back(self):
        self.win.deiconify()

app = Indication_6_3_8()
