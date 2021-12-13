from tkinter import *
from PIL import Image, ImageTk



class Indication_6_3_8:


    def __init__(self):
        # Входные переменные


        # Создание окна
        self.im= "Indication/Var4.png"
        self.win = Tk()
        self.win.title("Логика индикации конфигурации механизации крыла")
        self.win.geometry("430x800+300+250")

        self.var1 = IntVar()
        self.var2 = IntVar()

        # Создание областей для виджетов
        self.fr_main = Frame(self.win)
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
        self.fr_last = Frame(self.win, relief="raised", bd=1)


        # Создание виджетов
        self.lbl1 = Label(self.fr, text="Название входного\nпараметра", width=14, height=2)
        self.lbl2 = Label(self.fr, text="Валидность\nсигнала", width=12, height=2)
        self.lbl3 = Label(self.fr, text="Значение\nсигнала", width=9, height=2)
        self.lbl4 = Label(self.fr, text="Физический\nдиапазон", width=10, height=2)

        self.lbl11 = Label(self.fr1, text="DPK1", width=14, height=2)
        self.chb11 = Checkbutton(self.fr1, text="Валиден", variable=self.var1, onvalue=1, offvalue=0, width=12, height=2)
        self.ent11 = Entry(self.fr1, relief="ridge", width=8)
        self.lbl12 = Label(self.fr1, text="[0...24] град.", width=10, height=2)

        self.lbl21 = Label(self.fr2, text="DPK2", width=14, height=2)
        self.chb21 = Checkbutton(self.fr2, text="Валиден", variable=self.var2, onvalue=1, offvalue=0, width=12, height=2)
        self.ent21 = Entry(self.fr2, relief="ridge", width=8)
        self.lbl22 = Label(self.fr2, text="[0...24] град.", width=10, height=2)

        self.lbl31 = Label(self.fr3, text="DZK1", width=14, height=2)
        self.chb31 = Checkbutton(self.fr3, text="Валиден", relief="ridge", width=12, height=2)
        self.ent31 = Entry(self.fr3, relief="ridge", width=8)
        self.lbl32 = Label(self.fr3, text="[0...24] град.", width=10, height=2)

        self.lbl41 = Label(self.fr4, text="DZK2", width=14, height=2)
        self.chb41 = Checkbutton(self.fr4, text="Валиден", relief="ridge", width=12, height=2)
        self.ent41 = Entry(self.fr4, relief="ridge", width=8)
        self.lbl42 = Label(self.fr4, text="[0...24] град.", width=10, height=2)

        self.lbl51 = Label(self.fr5, text="FLAPS_1_FAULT", width=14, height=2)
        self.chb51 = Checkbutton(self.fr5, text="Валиден", width=12, height=2)
        self.ent51 = Entry(self.fr5, relief="ridge", width=8)
        self.lbl52 = Label(self.fr5, text="True - 1\nFalse - 1", width=10, height=2)

        self.lbl61 = Label(self.fr6, text="FLAPS_2_FAULT", width=14, height=2)
        self.chb61 = Checkbutton(self.fr6, text="Валиден", width=12, height=2)
        self.ent61 = Entry(self.fr6, relief="ridge", width=8)
        self.lbl62 = Label(self.fr6, text="True - 1\nFalse - 1", width=10, height=2)

        self.lbl71 = Label(self.fr7, text="SLATS_1_FAULT", width=14, height=2)
        self.chb71 = Checkbutton(self.fr7, text="Валиден", width=12, height=2)
        self.ent71 = Entry(self.fr7, relief="ridge", width=8)
        self.lbl72 = Label(self.fr7, text="True - 1\nFalse - 1", width=10, height=2)

        self.lbl81 = Label(self.fr8, text="SLATS_2_FAULT", width=14, height=2)
        self.chb81 = Checkbutton(self.fr8, text="Валиден", width=12, height=2)
        self.ent81 = Entry(self.fr8, relief="ridge", width=8)
        self.lbl82 = Label(self.fr8, text="True - 1\nFalse - 1", width=10, height=2)

        self.lbl91 = Label(self.fr9, text="X_MHZN", width=14, height=2)
        self.chb91 = Checkbutton(self.fr9, text="Валиден", width=12, height=2)
        self.ent91 = Entry(self.fr9, relief="ridge", width=8)
        self.lbl92 = Label(self.fr9, text="[0;6]", width=10, height=2)

        self.lbl101 = Label(self.fr10, text="X_FCM", width=14, height=2)
        self.chb101 = Checkbutton(self.fr10, text="Валиден", width=12, height=2)
        self.ent101 = Entry(self.fr10, relief="ridge", width=8)
        self.lbl102 = Label(self.fr10, text="[0;4]", width=10, height=2)

        self.lbl111 = Label(self.fr11, text="X_FCM_valid", width=14, height=2)
        self.chb111 = Checkbutton(self.fr11, text="Валиден", width=12, height=2)
        self.ent111 = Entry(self.fr11, relief="ridge", width=8)
        self.lbl112 = Label(self.fr11, text="True - 1\nFalse - 1", width=10, height=2)

        self.lbl121 = Label(self.fr12, text="S/A", width=14, height=2)
        self.chb121 = Checkbutton(self.fr12, text="Валиден", width=12, height=2)
        self.ent121 = Entry(self.fr12, relief="ridge", width=8)
        self.lbl122 = Label(self.fr12, text="True - 1\nFalse - 1", width=10, height=2)

        self.lbl131 = Label(self.fr13, text="S/A_FEEDBACK", width=14, height=2)
        self.chb131 = Checkbutton(self.fr13, text="Валиден", width=12, height=2)
        self.ent131 = Entry(self.fr13, relief="ridge", width=8)
        self.lbl132 = Label(self.fr13, text="True - 1\nFalse - 1", width=10, height=2)

        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self.fr_last, height=60, width=130)
        self.c_image = self.canvas.create_image(0, 0, anchor='e', image=self.photo)

        self.start = Button(self.fr_last, text="START", font=("Times New Roman", 20), command=self.chek_b1)


        # Расположение виджетов
        self.fr_main.pack()
        self.fr.pack(side=TOP)
        self.lbl1.pack(side=LEFT)
        self.lbl2.pack(side=LEFT)
        self.lbl3.pack(side=LEFT)
        self.lbl4.pack(side=LEFT)


        self.fr1.pack(side=TOP)
        self.lbl11.pack(side=LEFT)
        self.chb11.pack(side=LEFT)
        self.ent11.pack(side=LEFT, padx=2)
        self.lbl12.pack(side=LEFT)

        self.fr2.pack(side=TOP)
        self.lbl21.pack(side=LEFT)
        self.chb21.pack(side=LEFT)
        self.ent21.pack(side=LEFT, padx=2)
        self.lbl22.pack(side=LEFT)

        self.fr3.pack(side=TOP)
        self.lbl31.pack(side=LEFT)
        self.chb31.pack(side=LEFT)
        self.ent31.pack(side=LEFT, padx=2)
        self.lbl32.pack(side=LEFT)

        self.fr4.pack(side=TOP)
        self.lbl41.pack(side=LEFT)
        self.chb41.pack(side=LEFT)
        self.ent41.pack(side=LEFT, padx=2)
        self.lbl42.pack(side=LEFT)

        self.fr5.pack(side=TOP)
        self.lbl51.pack(side=LEFT)
        self.chb51.pack(side=LEFT)
        self.ent51.pack(side=LEFT, padx=2)
        self.lbl52.pack(side=LEFT)

        self.fr6.pack(side=TOP)
        self.lbl61.pack(side=LEFT)
        self.chb61.pack(side=LEFT)
        self.ent61.pack(side=LEFT, padx=2)
        self.lbl62.pack(side=LEFT)

        self.fr7.pack(side=TOP)
        self.lbl71.pack(side=LEFT)
        self.chb71.pack(side=LEFT)
        self.ent71.pack(side=LEFT, padx=2)
        self.lbl72.pack(side=LEFT)

        self.fr8.pack(side=TOP)
        self.lbl81.pack(side=LEFT)
        self.chb81.pack(side=LEFT)
        self.ent81.pack(side=LEFT, padx=2)
        self.lbl82.pack(side=LEFT)

        self.fr9.pack(side=TOP)
        self.lbl91.pack(side=LEFT)
        self.chb91.pack(side=LEFT)
        self.ent91.pack(side=LEFT, padx=2)
        self.lbl92.pack(side=LEFT)

        self.fr10.pack(side=TOP)
        self.lbl101.pack(side=LEFT)
        self.chb101.pack(side=LEFT)
        self.ent101.pack(side=LEFT, padx=2)
        self.lbl102.pack(side=LEFT)

        self.fr11.pack(side=TOP)
        self.lbl111.pack(side=LEFT)
        self.chb111.pack(side=LEFT)
        self.ent111.pack(side=LEFT, padx=2)
        self.lbl112.pack(side=LEFT)

        self.fr12.pack(side=TOP)
        self.lbl121.pack(side=LEFT)
        self.chb121.pack(side=LEFT)
        self.ent121.pack(side=LEFT, padx=2)
        self.lbl122.pack(side=LEFT)

        self.fr13.pack(side=TOP)
        self.lbl131.pack(side=LEFT)
        self.chb131.pack(side=LEFT)
        self.ent131.pack(side=LEFT, padx=2)
        self.lbl132.pack(side=LEFT)

        self.fr_last.pack(side=TOP, anchor=E)
        self.start.pack(side=RIGHT, anchor=E)
        self.canvas.pack(expand=1)


        self.win.mainloop()

    def chek_b1(self):
        vals = []
        vals.append(self.var1.get())
        vals.append(self.var2.get())
        print(vals)


app = Indication_6_3_8()