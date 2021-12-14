from tkinter import *

main_window_page = Tk()
main_window_page.title("GA")
main_window_page.geometry("600x600")

global entername #make it a global string variable
entername = StringVar()
enterpassword = StringVar()

Username=Label(text="Username")
Username.pack(pady=1,padx=1)
EnterName=Entry(bd=4,textvariable=entername)
EnterName.pack(pady=5,padx=5)

def clearFunc():
    entername.set("")

Reset=Button(text="Reset",command=clearFunc)
Reset.pack(pady=13,padx=13)

main_window_page.mainloop()