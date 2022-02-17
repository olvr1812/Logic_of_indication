# pyinstaller \
# -w -F -i 'gss_app.ico' Test_GUI.py

from pandas import *
import os
import random
import sys
from tkinter import *
from PIL import Image, ImageTk

class GuessingGame():
    # Определение пути
    # config_name = 'myapp.cfg'

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    config_path = os.path.join(application_path)
    # Конец определения пути
    xl_new = read_excel(config_path +'/logic.xlsx')

    descriptSig = xl_new['Описание входного параметра'].tolist()
    nameSig = xl_new['Название входного параметра'].tolist()
    rangeSig = xl_new['Физический диапазон'].tolist()

    def __init__(self, master):
        # get script directory where also the csv file is.
        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        self.path = application_path


        self.master = master
        master.title("Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.guess = None
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)
        self.lbl = Label(master, text=self.nameSig[0])

        vcmd = master.register(self.validate)  # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.guess_button = Button(master, text="<b>Guess</b>", command=self.guess_number)
        self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)

        self.label.pack()
        self.entry.pack()
        self.guess_button.pack()
        self.reset_button.pack()
        self.lbl.pack()

        self.img1 = Image.open(GuessingGame.config_path + "/logo.png")
        self.img2 = Image.open(GuessingGame.config_path + "/ssj1.png")
        self.img3 = Image.open(GuessingGame.config_path + "/ssj2.png")

        self.width = 400

        self.ratio = (self.width / 3000)
        self.height = int((float(self.img1.size[1]) * float(self.ratio)))
        self.imag1 = self.img1.resize((300, self.height), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.imag1)

        self.imag2 = self.img2.resize((self.width, 150), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.imag2)

        self.imag3 = self.img3.resize((self.width, 150), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.imag3)

        self.fr_back = Frame(master)
        self.fr_back.pack(side=TOP, fill=X)

        self.panel2 = Label(self.fr_back, image=self.image2)
        self.panel2.pack(side=LEFT)

        self.panel1 = Label(self.fr_back, image=self.image1)
        self.panel1.pack(side=LEFT, expand=YES)

        self.panel3 = Label(self.fr_back, image=self.image3)
        self.panel3.pack(side=RIGHT)


    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.guess = None
            return True

        try:
            guess = int(new_text)
            if 1 <= guess <= 100:
                self.guess = guess
                return True
            else:
                return False
        except ValueError:
            return False


    def guess_number(self):

        self.num_guesses += 1

        if self.guess is None:
            self.message = os.getcwd()

        elif self.guess == self.secret_number:
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)

        elif self.guess < self.secret_number:
            self.message = "It's low guess"
        else:
            self.message = "It's high guess"

        self.label_text.set(self.message)


    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 100)
        self.guess = 0
        self.num_guesses = 0

        self.message = "<b>Guess</b> a number from 1 to 100"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)


if __name__ == "__main__" :
    root = Tk()
    my_gui = GuessingGame(root)
    root.mainloop()
