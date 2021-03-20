from tkinter import *

class python_basic_course:
    def __init__(self, root):

        root.title("Py DEV")
        root.geometry('1366x768')
        root.configure(bg="#FFFFFF")

        self.top = Canvas(root, width=1366, height=60,bd=0, highlightthickness=0, relief='ridge', bg="#004D5E")
        self.top.grid(row=1, column=0, columnspan=1)

        self.mid2 = Canvas(root, width=1366, height=600, bd=0, highlightthickness=0, relief='ridge',  bg="#F5F4F4")
        self.mid2.grid(row=2, column=0, columnspan=1)

        self.down = Frame(root, width=1366, height=108, bg="#0A4350")
        self.down.grid(row=3, column=0, columnspan=1)

        root.mainloop()