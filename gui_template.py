# Шаблон для создания логики индикации
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

class app_5_10_1:
    # Ввод переменных
    wb = load_workbook(filename='logic.xlsx', read_only=True)
    ws = wb['5_10_1']

    descriptSig = []
    nameSig = []
    diapSig = []

    im = 'Indication_5_10_1/Var1.png'

    logic = open('logic_text/logic_5_10_1.txt', encoding='utf-8').readlines()
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
        for l in range(len(app_5_8_3.descriptSig)):
            exec('v_s.append(self.var{}.get())'.format(str(l)))
            exec('p_s.append(self.txt{}.get())'.format(str(l)))

        self.im = app_5_8_3.logik_of_indication(v_s, p_s)
        self.image = Image.open(self.im)
        self.photo = ImageTk.PhotoImage(self.image)
        # c_image = canvas.create_image(60, 160, anchor=NW, image=photo)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    def logik_of_indication(v_s, p_s):
        if -27.8 <= p_s[0] <= 22.8 and 0 <= p_s[1] <= 1 and 0 <= p_s[2] <= 1 and 0 <= p_s[3] <= 1:
            if v_s[0] == 1 and v_s[1] == 1 and (v_s[2] == 1 or v_s[3] == 1):
                if p_s[1] == 0 and p_s[2] == 0:
                    if p_s[0] == 0:
                        print("Вариант 1")
                        im = "Indication\Var"
                        txt = "Вариант 1"

                    else:
                        if p_s[0] < -27:
                            print("Вариант 3 | Индицируется минимальное значение (-27)")
                            txt = "Вариант 3 | Индицируется минимальное значение (-27)"
                        else:
                            if p_s[0] < 0:
                                print("Вариант 3 | Линейно пропорционально значению параметра ELEV_L_CONS")
                            else:
                                if p_s[0] > 22:
                                    print("Вариант 2 | Индицируется максимальное значение (22)")
                                else:
                                    print("Вариант 2 | Линейно пропорционально значению параметра ELEV_L_CONS")
                else:
                    if p_s[0] == 0:
                        print("Вариант 4")
                    else:
                        if p_s[0] < -27:
                            print("Вариант 6 | Индицируется минимальное значение (-27)")
                        else:
                            if p_s[0] < 0:
                                print("Вариант 6 | Линейно пропорционально значению параметра ELEV_L_CONS")
                            else:
                                if p_s[0] > 22:
                                    print("Вариант 5 | Индицируется максимальное значение (22)")
                                else:
                                    print("Вариант 5 | Линейно пропорционально значению параметра ELEV_L_CONS")
            else:
                print("Вариант 7")

        # print(v_s, "\n", p_s)
        return im

    def screen(self):
        cap = tkcap.CAP(self.win)
        cap.capture("Screenshots/Screen{}.png".format(str(self.count)))
        self.count += 1

    def copy(self):
        # f = open("../../Test_log.txt", "w")
        # f.write(app_6_3_8.logic)
        # f.close()
        pyperclip.copy(app_6_3_8.logic)
        return 0

    def open_main(self):
        self.win.destroy()
        import help
        return 0