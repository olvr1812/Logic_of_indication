from tkinter import *
import openpyxl
import pandas as pd

x1 = pd.ExcelFile('logic.xlsx')
x2 = pd.read_excel('./logic.xlsx')
x2.head()

#for i in range(1, 18)

print(x1.sheet_names)
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

#wb = openpyxl.reader.excel.load_workbook(filename="logic.xlsx")
#wb.active = 0
#print(wb.sheetnames)

#sheet = wb.active
#print(sheet['A1'].value)


i: IntVar = 1
k: IntVar = 0
descriptSig = ["Текущее положение предкрылков (квор) 1 п/к", "Текущее положение предкрылков (квор) 2 п/к"]
nameSig = ["DPK1", "DPK2"]
validSig = ["Валиден", "Валиден"]
diapSig = ["[0...24] град.", "[0...24] град."]
v_s = []
p_s = []

def chek_b1():
    global p_s
    global v_s

    v_s = []
    p_s = []
    for l in range(1, i):
        exec('v_s.append(var{}.get())'.format(str(l)))
        exec('p_s.append(txt{}.get())'.format(str(l)))
    print(p_s, "\n", v_s)

win = Tk()
win.geometry("600x400")


fr_main = Frame(win)
fr = Frame(fr_main, relief=RIDGE, bd = 1)
lbl0 = Label(fr, text="Описание\nвходного параметра", font=("Times New Roman", 11), width=23, height=2)
lbl1 = Label(fr, text="Название входного\nпараметра", font=("Times New Roman", 11), width=16, height=2)
lbl2 = Label(fr, text="Валидность\nсигнала", font=("Times New Roman", 11), width=12, height=2)
lbl3 = Label(fr, text="Значение\nсигнала", font=("Times New Roman", 11), width=9, height=2)
lbl4 = Label(fr, text="Физический\nдиапазон", font=("Times New Roman", 11), width=10, height=2)

fr_main.pack(side=LEFT)
fr.pack(side=TOP)
lbl0.pack(side=LEFT)
lbl1.pack(side=LEFT)
lbl2.pack(side=LEFT)
lbl3.pack(side=LEFT)
lbl4.pack(side=LEFT)

while i < 3:
    exec('txt{} = DoubleVar()'.format(str(i)))
    exec('var{} = IntVar()'.format(str(i)))
    exec('var{}.set(1)'.format(str(i)))

    exec('fr{} = Frame(fr_main, relief="ridge", bd=1)'.format(str(i)))
    exec('text{} = Text(fr{}, font=("Times New Roman", 11), height=2, width=23, wrap=WORD)'.format(str(i), str(i)))
    exec('text{}.insert(END, "{}")'.format(str(i), descriptSig[i-1]))
    exec('text{}.config(state=DISABLED)'.format(str(i)))
    exec('lbl{}1 = Label(fr{}, text="{}", font=("Times New Roman", 11), width=16, height=2)'.format(str(i), str(i), nameSig[i-1]))
    exec("chb{} = Checkbutton(fr{}, text='{}', cursor='exchange', font=('Times New Roman', 11), variable=var{}, onvalue=1, offvalue=0, width=12, height=2)".format(str(i), str(i), validSig[i -1], str(i)))
    exec("ent{} = Entry(fr{}, textvariable=txt{}, font=('Times New Roman', 11), relief=RIDGE, width=8)".format(str(i), str(i), str(i)))
    exec("lbl{}2 = Label(fr{}, text='{}', font=('Times New Roman', 11), width=10, height=2)".format(str(i), str(i), diapSig[i-1]))

    exec("fr{}.pack(side=TOP)".format(str(i)))
    exec('text{}.pack(side=LEFT)'.format(str(i)))
    exec("lbl{}1.pack(side=LEFT)".format(str(i)))
    exec("chb{}.pack(side=LEFT)".format(str(i)))
    exec("ent{}.pack(side=LEFT)".format(str(i)))
    exec("lbl{}2.pack(side=LEFT)".format(str(i)))
    i += 1

test = Button(win, text="Test", command=chek_b1)
test.pack(side=TOP)

win.mainloop()


