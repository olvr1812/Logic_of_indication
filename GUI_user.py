from tkinter import *

import rm as rm
from openpyxl import load_workbook
from PIL import Image, ImageTk
from pyautogui import *
import tkcap
import pyperclip

# Ввод переменных
wb = load_workbook(filename='logic.xlsx', read_only=True)
ws = wb['6_3_8']

descriptSig = []
nameSig = []
diapSig = []

im = 'Indication/Var19.png'

logic = open('logic_text/logic_6_3_8.txt', encoding='utf-8').readlines()
logic = ''.join(logic)

for i in ws.rows:
    #break
    for k in i:
        if k == i[0]:
            descriptSig.append(k.value)
        elif k == i[1]:
            nameSig.append(k.value)
        elif k == i[2]:
            diapSig.append(k.value)

k: IntVar = 0
v_s = []
p_s = []
count = 1

def chek_b1():
    global p_s
    global v_s
    global c_image
    global im
    global canavas
    v_s = []
    p_s = []
    for l in range(len(descriptSig)):
        exec('v_s.append(var{}.get())'.format(str(l)))
        exec('p_s.append(txt{}.get())'.format(str(l)))

    im = logik_of_indication(v_s, p_s)
    image = Image.open(im)
    photo = ImageTk.PhotoImage(image)
    c_image = canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack(side=TOP)

def logik_of_indication(v_s, p_s):
        global im
        if 0 <= p_s[0] <= 24 and 0 <= p_s[1] <= 24 and 0 <= p_s[2] <= 36 and 0 <= p_s[3] <= 36 and 0 <= p_s[4] <= 1 \
                and 0 <= p_s[5] <= 1 and 0 <= p_s[6] <= 1 and 0 <= p_s[7] <= 1 and 0 <= p_s[8] <= 6 and 0 <= p_s[9] <= 4 \
                and 0 <= p_s[10] <= 1 and 0 <= p_s[11] <= 1 and 0 <= p_s[12] <= 1:
            if v_s[8] == 1 and (v_s[0] == 1 or v_s[1] == 1) and (v_s[2] == 1 or v_s[3] == 1) and v_s[8] == 1 and p_s[
                10] == 1:

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
                print('Вариант 19 | XXXX')
                im = "Indication/Var19.png"
        else:
            im = "Indication/Error.png"
        print(v_s, "\n", p_s)
        return im

def screen():
    global count
    count += 1
    cap = tkcap.CAP(win)
    cap.capture("Screenshots/Screen{}.png".format(str(count)))

def copy():
    f = open("../../Test_log.txt", "w")
    f.write(logic)
    f.close()
    pyperclip.copy(logic)
    return 0

def open_main():
    win.destroy()
    import help
    return 0

def go_away():
    win.withdraw()

def come_back(self):
    win.deiconify()

win = Tk()
# Начало таблицы
# Создание заголовков таблицы
fr_main = Frame(win)
fr = Frame(fr_main, relief=RIDGE, bd = 1, width=70)
lbl0 = Label(fr, text="Описание\nвходного параметра", font=("Times New Roman", 11), width=23, height=2)
lbl1 = Label(fr, text="Название входного\nпараметра", font=("Times New Roman", 11), width=16, height=2)
lbl2 = Label(fr, text="Валидность\nсигнала", font=("Times New Roman", 11), width=12, height=2)
lbl3 = Label(fr, text="Значение\nсигнала", font=("Times New Roman", 11), width=9, height=2)
lbl4 = Label(fr, text="Физический\nдиапазон", font=("Times New Roman", 11), width=9, height=2)

fr_main.pack(side=LEFT)
fr.pack(side=TOP)
lbl0.pack(side=LEFT)
lbl1.pack(side=LEFT)
lbl2.pack(side=LEFT)
lbl3.pack(side=LEFT)
lbl4.pack(side=LEFT)

# Циклическое создание таблицы
for i in range(len(descriptSig)):
    exec('txt{} = DoubleVar()'.format(str(i)))
    exec('var{} = IntVar()'.format(str(i)))
    exec('var{}.set(1)'.format(str(i)))

    # Начало рамки для табличных значений #############################################
    exec('fr{} = Frame(fr_main, relief="ridge", bd=1, width=70)'.format(str(i)))

     # Ячейка с описанием параметра
    exec('text{} = Text(fr{}, font=("Times New Roman", 11), height=2, width=23, wrap=WORD)'.format(str(i), str(i)))
    exec('text{}.tag_configure("center", justify="center")'.format(str(i)))
    exec('text{}.insert(1.0, "{}")'.format(str(i), descriptSig[i]))
    exec('text{}.tag_add("center", "1.0", "end")'.format(str(i)))
    exec('text{}.config(state=DISABLED)'.format(str(i)))

    # Ячейка с именем параметра
    exec('lbl{} = Label(fr{}, text="{}", font=("Times New Roman", 11), width=16, height=2)'.format(str(i), str(i), nameSig[i]))

    # Ячейка с выбором валидности сигнала
    exec("chb{} = Checkbutton(fr{}, text='Валиден', cursor='exchange', font=('Times New Roman', 11), variable=var{}, onvalue=1, offvalue=0, width=12, height=2)".format(str(i), str(i), str(i)))

    # Ячейка с вводом значения параметра
    exec("ent{} = Entry(fr{}, textvariable=txt{}, font=('Times New Roman', 11), relief=RIDGE, width=8)".format(str(i), str(i), str(i)))

    # Ячейка диапазоном возможных значений
    exec('text{}1 = Text(fr{}, font=("Times New Roman", 11), height=2, width=9, wrap=WORD)'.format(str(i), str(i)))
    exec('text{}1.tag_configure("center", justify="center")'.format(str(i)))
    exec('text{}1.insert(1.0, "{}")'.format(str(i), diapSig[i]))
    exec('text{}1.tag_add("center", "1.0", "end")'.format(str(i)))
    exec('text{}1.config(state=DISABLED)'.format(str(i)))

    # Расположение Виджетов
    exec("fr{}.pack(side=TOP)".format(str(i)))
    exec('text{}.pack(side=LEFT)'.format(str(i)))
    exec("lbl{}.pack(side=LEFT)".format(str(i)))
    exec("chb{}.pack(side=LEFT)".format(str(i)))
    exec("ent{}.pack(side=LEFT)".format(str(i)))
    exec("text{}1.pack(side=LEFT)".format(str(i)))
# Конец таблицы ###################################################

fr_results = Frame(win)
fr_start = Frame(fr_results, relief="raised", bd=4, bg="black")
fr_copy = Frame(fr_results, relief="raised", bd=4)
fr_screen = Frame(fr_results, relief="raised", bd=4)
fr_logic = Frame(win, relief=RIDGE, bd=6)

start_bt = Button(fr_start, text="START", font=("Times New Roman", 20), fg="red", activeforeground="#ADFF2F", cursor="hand1", command=chek_b1, width=11)
copy_bt = Button(fr_copy, text="Copy", font=('Times New Roman', 20), command=copy, width=11)
scr_and_sv = Button(fr_screen, text="Save screen", font=("Times New Roman", 20), cursor="pirate", command=screen, width=11)
canvas = Canvas(fr_results, relief="ridge", bd=4, height=47, width=138)

text = Text(fr_logic, font=("Times New Roman", 12), width=90)
text.insert(END, logic)

scr = Scrollbar(fr_logic)

chb10["state"] = DISABLED


        # Добавим изображение
image = Image.open(im)
photo = ImageTk.PhotoImage(image)
c_image = canvas.create_image(60, 160, anchor='nw', image=photo)

fr_results.pack(side=LEFT, fill=BOTH)
canvas.pack(side=TOP)
fr_start.pack(side=TOP)
start_bt.pack()
fr_screen.pack(side=BOTTOM)
scr_and_sv.pack()
fr_copy.pack(side=BOTTOM)
copy_bt.pack()
fr_logic.pack(side=LEFT, fill=BOTH)
scr.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=BOTH)

win.mainloop()


