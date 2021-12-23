from tkinter import *
from openpyxl import load_workbook
from PIL import Image, ImageTk
from pyautogui import *
import tkcap
import pyperclip
from functools import partial

file_end = os.listdir("Screenshots")
for i in file_end:
    if i.endswith(".png"):
        os.remove("Screenshots/" + i)
print(os.getcwd())
class app_6_3_8:
    # Ввод переменных
    wb = load_workbook(filename='logic.xlsx', read_only=True)
    ws = wb['6_3_8']

    descriptSig = []
    nameSig = []
    diapSig = []

    im = 'Indication_6_3_8/Var4.png'

    logic = open('logic_text/logic_6_3_8.txt', encoding='utf-8').readlines()
    logic = ''.join(logic)

    for i in ws.rows:
        for k in i:
            if k == i[0]:
                descriptSig.append(k.value)
            elif k == i[1]:
                nameSig.append(k.value)
            elif k == i[2]:
                diapSig.append(k.value)

    k: IntVar = 0
    count = 1

    def chek_b1(self):
        v_s = []
        p_s = []
        for l in range(len(app_6_3_8.descriptSig)):
            exec('v_s.append(self.var{}.get())'.format(str(l)))
            exec('p_s.append(self.txt{}.get())'.format(str(l)))

        self.im = app_6_3_8.logik_of_indication(v_s, p_s)
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        # c_image = canvas.create_image(60, 160, anchor=NW, image=photo)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    def logik_of_indication(v_s, p_s):
        if 0 <= p_s[0] <= 24 and 0 <= p_s[1] <= 24 and 0 <= p_s[2] <= 36 and 0 <= p_s[3] <= 36 and 0 <= p_s[4] <= 1 \
                and 0 <= p_s[5] <= 1 and 0 <= p_s[6] <= 1 and 0 <= p_s[7] <= 1 and 0 <= p_s[8] <= 6 and 0 <= p_s[9] <= 4 \
                and 0 <= p_s[10] <= 1 and 0 <= p_s[11] <= 1 and 0 <= p_s[12] <= 1:
            if v_s[8] == 1 and (v_s[0] == 1 or v_s[1] == 1) and (v_s[2] == 1 or v_s[3] == 1) and v_s[8] == 1 and p_s[
                10] == 1:


                if p_s[8] == 0 and p_s[9] == 0:  # СУМК = 0 РУМК = 0
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 0 or p_s[1] == 0) and (p_s[2] == 0 or p_s[3] == 0):
                            print('Вариант 4 | FLAP 0 - надпись отсутствует')
                            im = "Indication_6_3_8/Var4.png"

                        else:
                            print('Вариант 5 | FLAP 0 - цвет голубой')
                            im = "Indication_6_3_8/Var5.png"
                    else:
                        print('Вариант 6 | FLAP 0 - цвет янтарный')
                        im = "Indication_6_3_8/Var6.png"

                elif p_s[8] == 1 and p_s[9] == 0:  # СУМК = 1 РУМК = 0
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 0 or p_s[1] == 0) and (p_s[2] == 1 or p_s[3] == 1):
                            print('Вариант 21 | FLAP ICE - зеленый')
                            im = "Indication_6_3_8/Var21.png"
                        else:
                            print('Вариант 20 | FLAP ICE - цвет голубой')
                            im = "Indication_6_3_8/Var20.png"
                    else:
                        print('Вариант 22 | FLAP ICE - цвет янтарный')
                        im = "Indication_6_3_8/Var22.png"

                elif p_s[8] == 2 and p_s[9] == 1:  # СУМК 2 РУМК = 1
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 18 or p_s[1] == 18) and (p_s[2] == 3 or p_s[3] == 3):
                            print('Вариант 7 | FLAP 1 - зеленый')
                            im = "Indication_6_3_8/Var7.png"
                        else:
                            print('Вариант 8 | FLAP 1 - цвет голубой')
                            im = "Indication_6_3_8/Var8.png"
                    else:
                        print('Вариант 9 | FLAP 1 - цвет янтарный')
                        im = "Indication_6_3_8/Var9.png"

                elif p_s[8] == 3 and p_s[9] == 1:  # СУМК = 3 РУМК = 1
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 18 or p_s[1] == 18) and (p_s[2] == 9 or p_s[3] == 9):
                            print('Вариант 10 | FLAP 1 + F - зеленый')
                            im = "Indication_6_3_8/Var10.png"
                        else:
                            print('Вариант 11 | FLAP 1 + F - цвет голубой')
                            im = "Indication_6_3_8/Var11.png"
                    else:
                        print('Вариант 12 | FLAP 1 + F - цвет янтарный')
                        im = "Indication_6_3_8/Var12.png"

                elif p_s[8] == 4 and p_s[9] == 2:  # СУМК = 4 РУМК = 2
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 16 or p_s[3] == 16):
                            print('Вариант 13 | FLAP 2 - зеленый')
                            im = "Indication_6_3_8/Var13.png"
                        else:
                            print('Вариант 14 | FLAP 2 - цвет голубой')
                            im = "Indication_6_3_8/Var14.png"
                    else:
                        print('Вариант 15 | FLAP 2 - цвет янтарный')
                        im = "Indication_6_3_8/Var15.png"

                elif p_s[8] == 5 and p_s[9] == 3:
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 25 or p_s[3] == 25):
                            print('Вариант 16 | FLAP 3 - зеленый')
                            im = "Indication_6_3_8/Var16.png"
                        else:
                            print('Вариант 17 | FLAP 3 - цвет голубой')
                            im = "Indication_6_3_8/Var17.png"
                    else:
                        print('Вариант 18 | FLAP 3 - цвет янтарный')
                        im = "Indication_6_3_8/Var18.png"
                elif p_s[8] == 6 and p_s[9] == 4:
                    if (p_s[4] == 0 or p_s[5] == 0) and (p_s[6] == 0 or p_s[7] == 0):
                        if (p_s[0] == 24 or p_s[1] == 24) and (p_s[2] == 36 or p_s[3] == 36):
                            if p_s[11] == 1:
                                if v_s[10] == 1 and v_s[11] == 1 and p_s[12] == 1:
                                    print('Вариант 23 | FULL-S/A - цвет зеленый')
                                    im = "Indication_6_3_8/Var23.png"
                                else:
                                    print('Вариант 24 | FULL-S/A - цвет янтарный')
                                    im = "Indication_6_3_8/Var24.png"
                            else:
                                print('Вариант 1 | FULL - цвет зеленый')
                                im = "Indication_6_3_8/Var1.png"
                        else:
                            print('Вариант 2 | FULL - цвет синий')
                            im = "Indication_6_3_8/Var2.png"
                    else:
                        print('Вариант 3 | FULL - цвет янтарный')
                        im = "Indication_6_3_8/Var3.png"
                else:
                    print('Вариант 3 | FULL - цвет янтарный')
                    im = "Indication_6_3_8/Var3.png"
            else:
                print('Вариант 19 | XXXX')
                im = "Indication_6_3_8/Var19.png"
        else:
            im = "Indication_6_3_8/Error.png"
        # print(v_s, "\n", p_s)
        return im

    def screen(self):
        cap = tkcap.CAP(self.win)
        cap.capture("Screenshots/Screen{}.png".format(str(self.count)))
        self.count += 1

    def copy(self):
        #f = open("../../Test_log.txt", "w")
        #f.write(app_6_3_8.logic)
        #f.close()
        pyperclip.copy(app_6_3_8.logic)
        return 0

    def open_main(self):
        self.win.destroy()
        import help
        return 0

    def go_away(self):
        self.win.withdraw()

    def come_back(self):
        self.win.deiconify()

    def tests(self, a):
        if a == 1:
            self.txt0.set(0) # DPK1
            self.txt1.set(0) # DPK2
            self.txt2.set(1) # DZK1
            self.txt3.set(1) # DZK2
            self.txt4.set(0) # FLAPS_1_FAULT
            self.txt5.set(0) # FLAPS_2_FAULT
            self.txt6.set(0) # SLATS_1_FAULT
            self.txt7.set(0) # SLATS_2_FAULT
            self.txt8.set(1) # X_MHZN
            self.txt9.set(0) # X_FCM
            self.txt10.set(1) # X_FCM_valid
            self.txt11.set(0) # S/A
            self.txt12.set(0) # S/A_FEEDBACK
        elif a == 2:
            self.txt0.set(18)  # DPK1
            self.txt1.set(18)  # DPK2
            self.txt2.set(3)  # DZK1
            self.txt3.set(3)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(2)  # X_MHZN
            self.txt9.set(1)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
        elif a == 3:
            self.txt0.set(18)  # DPK1
            self.txt1.set(18)  # DPK2
            self.txt2.set(9)  # DZK1
            self.txt3.set(9)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(3)  # X_MHZN
            self.txt9.set(1)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
        elif a == 4:
            self.txt0.set(24)  # DPK1
            self.txt1.set(24)  # DPK2
            self.txt2.set(16)  # DZK1
            self.txt3.set(16)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(4)  # X_MHZN
            self.txt9.set(2)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
        elif a == 5:
            self.txt0.set(24)  # DPK1
            self.txt1.set(24)  # DPK2
            self.txt2.set(25)  # DZK1
            self.txt3.set(25)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(5)  # X_MHZN
            self.txt9.set(3)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK
        elif a == 6:
            self.txt0.set(24)  # DPK1
            self.txt1.set(24)  # DPK2
            self.txt2.set(36)  # DZK1
            self.txt3.set(36)  # DZK2
            self.txt4.set(0)  # FLAPS_1_FAULT
            self.txt5.set(0)  # FLAPS_2_FAULT
            self.txt6.set(0)  # SLATS_1_FAULT
            self.txt7.set(0)  # SLATS_2_FAULT
            self.txt8.set(6)  # X_MHZN
            self.txt9.set(4)  # X_FCM
            self.txt10.set(1)  # X_FCM_valid
            self.txt11.set(0)  # S/A
            self.txt12.set(0)  # S/A_FEEDBACK


    def __init__(self):
        # Create window
        self.win = Tk()
        self.win.title("Логика индикации конфигурации механизации крыла")

        self.img1 = Image.open("logo.png")
        self.img2 = Image.open("ssj1.png")
        self.img3 = Image.open("ssj2.png")

        self.width = 400

        self.ratio = (self.width / 3000)
        self.height = int((float(self.img1.size[1]) * float(self.ratio)))
        self.imag1 = self.img1.resize((300, self.height), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.imag1)

        self.imag2 = self.img2.resize((self.width, 150), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.imag2)

        self.imag3 = self.img3.resize((self.width, 150), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.imag3)

        self.fr_back = Frame(self.win)
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
        self.filemenu.add_command(label="Main", command=self.open_main)
        self.filemenu.add_command(label="Screenshot", command=self.screen)
        self.filemenu.add_command(label="Close", command=self.win.quit)

        self.menu_bar.add_cascade(label="File", menu=self.filemenu)

        # Начало таблицы
        # Создание заголовков таблицы
        self.fr_main = Frame(self.win, relief=GROOVE, bd=4)
        self.fr = Frame(self.fr_main, relief=RIDGE, bd=1, width=70)
        self.lbl0 = Label(self.fr, text="Описание\nвходного параметра", font=("Times New Roman", 11), width=23,
                          height=2)
        self.lbl1 = Label(self.fr, text="Название входного\nпараметра", font=("Times New Roman", 11), width=16,
                          height=2)
        self.lbl2 = Label(self.fr, text="Валидность\nсигнала", font=("Times New Roman", 11), width=12, height=2)
        self.lbl3 = Label(self.fr, text="Значение\nсигнала", font=("Times New Roman", 11), width=9, height=2)
        self.lbl4 = Label(self.fr, text="Физический\nдиапазон", font=("Times New Roman", 11), width=9, height=2)

        self.fr_main.pack(side=LEFT)
        self.fr.pack(side=TOP)
        self.lbl0.pack(side=LEFT)
        self.lbl1.pack(side=LEFT)
        self.lbl2.pack(side=LEFT)
        self.lbl3.pack(side=LEFT)
        self.lbl4.pack(side=LEFT)

        # Циклическое создание таблицы
        for i in range(len(app_6_3_8.descriptSig)):
            exec('self.txt{} = DoubleVar()'.format(str(i)))
            exec('self.var{} = IntVar()'.format(str(i)))
            exec('self.var{}.set(1)'.format(str(i)))

            # Начало рамки для табличных значений #############################################
            exec('self.fr{} = Frame(self.fr_main, relief="ridge", bd=1, width=70)'.format(str(i)))

            # Ячейка с описанием параметра
            exec('self.text{} = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=23, wrap=WORD)'.format(
                str(i), str(i)))
            exec('self.text{}.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.text{}.insert(1.0, "{}")'.format(str(i), app_6_3_8.descriptSig[i]))
            exec('self.text{}.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.text{}.config(state=DISABLED)'.format(str(i)))

            # Ячейка с именем параметра
            exec('self.lbl{} = Label(self.fr{}, text="{}", font=("Times New Roman", 11), width=16, height=2)'.format(
                str(i), str(i), app_6_3_8.nameSig[i]))

            # Ячейка с выбором валидности сигнала
            exec(
                "self.chb{} = Checkbutton(self.fr{}, text='Валиден', cursor='exchange', font=('Times New Roman', 11), variable=self.var{}, onvalue=1, offvalue=0, width=12, height=2)".format(
                    str(i), str(i), str(i)))

            # Ячейка с вводом значения параметра
            exec(
                "self.ent{} = Entry(self.fr{}, textvariable=self.txt{}, font=('Times New Roman', 11), relief=RIDGE, width=8)".format(
                    str(i), str(i), str(i)))

            # Ячейка диапазоном возможных значений
            exec('self.text{}1 = Text(self.fr{}, font=("Times New Roman", 11), height=2, width=9, wrap=WORD)'.format(
                str(i), str(i)))
            exec('self.text{}1.tag_configure("center", justify="center")'.format(str(i)))
            exec('self.text{}1.insert(1.0, "{}")'.format(str(i), app_6_3_8.diapSig[i]))
            exec('self.text{}1.tag_add("center", "1.0", "end")'.format(str(i)))
            exec('self.text{}1.config(state=DISABLED)'.format(str(i)))

            # Расположение Виджетов
            exec("self.fr{}.pack(side=TOP)".format(str(i)))
            exec('self.text{}.pack(side=LEFT)'.format(str(i)))
            exec("self.lbl{}.pack(side=LEFT)".format(str(i)))
            exec("self.chb{}.pack(side=LEFT)".format(str(i)))
            exec("self.ent{}.pack(side=LEFT)".format(str(i)))
            exec("self.text{}1.pack(side=LEFT)".format(str(i)))
        # Конец таблицы ###################################################

        self.fr_results = Frame(self.win, relief=GROOVE, bd=4)
        self.fr_start = Frame(self.fr_results, relief="raised", bd=4, bg="black")
        self.fr_tests = Frame(self.fr_results, relief="raised", bd=2, bg="black")
        self.fr_tests_l = Frame(self.fr_tests, relief="raised", bd=2, bg="black")
        self.fr_tests_r = Frame(self.fr_tests, relief="raised", bd=2, bg="black")
        self.fr_copy = Frame(self.fr_results, relief="raised", bd=4)
        self.fr_screen = Frame(self.fr_results, relief="raised", bd=4)
        self.fr_logic = Frame(self.win, relief=RIDGE, bd=6)

        self.start_bt = Button(self.fr_start, text="START", font=("Times New Roman", 20), fg="red",
                               activeforeground="#ADFF2F", cursor="hand1", command=self.chek_b1, width=11)
        self.test1 = Button(self.fr_tests_l, text="FLAP ICE", font=("Times New Roman", 14), fg="green",
                               activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 1), width=9)
        self.test2 = Button(self.fr_tests_r, text="FLAP 1", font=("Times New Roman", 14), fg="green",
                            activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 2), width=9)
        self.test3 = Button(self.fr_tests_l, text="FLAP 1+F", font=("Times New Roman", 14), fg="green",
                            activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 3), width=9)
        self.test4 = Button(self.fr_tests_r, text="FLAP 2", font=("Times New Roman", 14), fg="green",
                            activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 4), width=9)
        self.test5 = Button(self.fr_tests_l, text="FLAP 3", font=("Times New Roman", 14), fg="green",
                            activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 5), width=9)
        self.test6 = Button(self.fr_tests_r, text="FULL", font=("Times New Roman", 14), fg="green",
                            activeforeground="#ADFF2F", cursor="hand1", command=partial(self.tests, 6), width=9)
        self.copy_bt = Button(self.fr_copy, text="Copy", font=('Times New Roman', 20), command=self.copy, width=11)
        self.scr_and_sv = Button(self.fr_screen, text="Save screen", font=("Times New Roman", 20), cursor="pirate",
                                 command=self.screen, width=11)
        self.canvas = Canvas(self.fr_results, relief="ridge", bd=4, height=47, width=138)

        self.text = Text(self.fr_logic, font=("Times New Roman", 12), width=90)
        self.text.insert(END, app_6_3_8.logic)
        self.text["state"] = DISABLED
        self.scr = Scrollbar(self.fr_logic)

        self.chb10["state"] = DISABLED
        self.txt10.set(1)

        self.fr_results.pack(side=LEFT, fill=BOTH)
        self.canvas.pack(side=TOP)

        # Добавим изображение
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, image=self.photo, anchor='nw')

        # print(im, image, photo, c_image, sep='\n')

        self.fr_start.pack(side=TOP)
        self.start_bt.pack()
        self.fr_tests.pack(side=TOP)
        self.fr_tests_l.pack(side=LEFT, padx=3)
        self.fr_tests_r.pack(side=RIGHT, padx=3)
        self.test1.pack()
        self.test2.pack()
        self.test3.pack(pady=4)
        self.test4.pack(pady=4)
        self.test5.pack()
        self.test6.pack()
        self.fr_screen.pack(side=BOTTOM)
        self.scr_and_sv.pack()
        self.fr_copy.pack(side=BOTTOM)
        self.copy_bt.pack()
        self.fr_logic.pack(side=LEFT, fill=BOTH)
        self.scr.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=BOTH)

        self.win.config(menu=self.menu_bar)
        self.win.mainloop()


app = app_6_3_8()


