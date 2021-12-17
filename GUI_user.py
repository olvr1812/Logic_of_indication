from tkinter import *
from openpyxl import load_workbook

wb = load_workbook(filename='logic.xlsx', read_only=True)
ws = wb['6_3_8']
descriptSig = []
nameSig = []
diapSig = []
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

def chek_b1():
    global p_s
    global v_s

    v_s = []
    p_s = []
    for l in range(len(descriptSig)):
        exec('v_s.append(var{}.get())'.format(str(l)))
        exec('p_s.append(txt{}.get())'.format(str(l)))
    print(p_s, "\n", v_s)

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



test = Button(win, text="Test", command=chek_b1)
test.pack(side=TOP)

win.mainloop()


