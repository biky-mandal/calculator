import doctest
from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox

from User import mainpage

large_font = ('spacemono', 12)


class Window1:

    def callbacktomainpage(self, event):
        # This will clear the left-frame
        for widget in self.lframe.winfo_children():
            widget.destroy()
        # This will clear the right-frame
        for widget in self.rframe.winfo_children():
            widget.destroy()

        self.master = self.master

        self.__init__(self.master)

    def __init__(self, master):

        self.master = master

        self.lframe = Frame(master, width=400, height=468, bg="#FFFFFF")
        self.lframe.grid(row=0, column=0)

        self.rframe = Frame(master, width=566, height=468, bg="#0A4350")
        self.rframe.grid(row=0, column=1)

        brand1photo = PhotoImage(file="/home/biky/Desktop/devdotpy/images/DEV.PY.png")
        brand2photo = Label(self.lframe, image=brand1photo, bg="#FFFFFF")
        brand2photo.image = brand1photo  # this will make a reference to tkinter object.
        brand2photo.place(relx=0.03, rely=0.02, anchor=NW)

        pylogo1photo = PhotoImage(file="/home/biky/Desktop/devdotpy/images/pylogo.png")
        pylogo2photo = Label(self.lframe, image=pylogo1photo, bg="#FFFFFF")
        pylogo2photo.image = pylogo1photo  # this will make a reference to tkinter object.
        """The problem is that the Tkinter/Tk interface doesn’t handle references to Image objects properly; 
        the Tk widget will hold a reference to the internal object, but Tkinter does not. 
        When Python’s garbage collector discards the Tkinter object, 
        Tkinter tells Tk to release the image. 
        But since the image is in use by a widget, Tk doesn’t destroy it. Not completely.
        It just blanks the image, making it completely transparent…"""
        pylogo2photo.place(relx=0.5, rely=0.15, anchor=CENTER)

        tag1photo = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Programming With Python.png")
        tag2photo = Label(self.lframe, image=tag1photo, bg="#FFFFFF")
        tag2photo.image = tag1photo
        tag2photo.place(relx=0.5, rely=0.30, anchor=CENTER)

        desk1design = PhotoImage(file="/home/biky/Desktop/devdotpy/images/deskregisterdesign.png")
        desk2design = Label(self.lframe, image=desk1design, bg="#FFFFFF")
        desk2design.image = desk1design
        desk2design.place(relx=0.5, rely=0.65, anchor=CENTER)

        # Here the rframe begins.

        welcome1text = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Welcome Friend!.png")
        welcome2text = Label(self.rframe, image=welcome1text, bg="#0A4350")
        welcome2text.image = welcome1text
        welcome2text.place(relx=0.5, rely=0.1, anchor=CENTER)

        # name

        enter1nametext = PhotoImage(file="/home/biky/Desktop/devdotpy/images/entername.png")
        enter2nametext = Label(self.rframe, image=enter1nametext, bg="#0A4350")
        enter2nametext.image = enter1nametext
        enter2nametext.place(relx=0.33, rely=0.34, anchor=CENTER)

        self.name1entry = Entry(self.rframe, font=large_font, bd="0", bg="#FFFFFF", fg="#0A4350",
                                justify=CENTER)
        self.name1entry.place(width=228, height=30, relx=0.419, rely=0.40, anchor=CENTER)

        # gender
        enter1gendertext = PhotoImage(file="/home/biky/Desktop/devdotpy/images/entergender.png")
        enter2gendertext = Label(self.rframe, image=enter1gendertext, bg="#0A4350")
        enter2gendertext.image = enter1gendertext
        enter2gendertext.place(relx=0.71, rely=0.34, anchor=CENTER)

        self.gender1entry = Entry(self.rframe, font=large_font, bd="0", bg="#FFFFFF", fg="#0A4350",
                                  justify=CENTER)
        self.gender1entry.place(width=80, height=30, relx=0.71, rely=0.40, anchor=CENTER)

        # Email

        enter1emailtext = PhotoImage(file="/home/biky/Desktop/devdotpy/images/enteremail.png")
        enter2emailtext = Label(self.rframe, image=enter1emailtext, bg="#0A4350")
        enter2emailtext.image = enter1emailtext
        enter2emailtext.place(relx=0.62, rely=0.49, anchor=CENTER)

        self.email1entry = Entry(self.rframe, font=large_font, bd="0", bg="#FFFFFF", fg="#0A4350",
                                 justify=CENTER)
        self.email1entry.place(width=320, height=30, relx=0.5, rely=0.55, anchor=CENTER)

        # password

        enter1passtext = PhotoImage(file="/home/biky/Desktop/devdotpy/images/enterpassword.png")
        enter2passtext = Label(self.rframe, image=enter1passtext, bg="#0A4350")
        enter2passtext.image = enter1passtext
        enter2passtext.place(relx=0.341, rely=0.64, anchor=CENTER)

        self.pass1entry = Entry(self.rframe, font=large_font, bd="0", bg="#FFFFFF", fg="#0A4350",
                                justify=CENTER)
        self.pass1entry.place(width=155, height=30, relx=0.353, rely=0.70, anchor=CENTER)

        # confirm pass

        confirm1passtext = PhotoImage(file="/home/biky/Desktop/devdotpy/images/confirmpassword.png")
        confirm2passtext = Label(self.rframe, image=confirm1passtext, bg="#0A4350")
        confirm2passtext.image = confirm1passtext
        confirm2passtext.place(relx=0.64, rely=0.64, anchor=CENTER)

        self.pass2entry = Entry(self.rframe, font=large_font, bd="0", bg="#FFFFFF",
                                fg="#0A4350",
                                show="*", justify=CENTER)
        self.pass2entry.place(width=155, height=30, relx=0.647, rely=0.70, anchor=CENTER)

        loginButton = Button(self.rframe, text="LOGIN", height=1, width=8, background="#5B8C44", foreground="#FFFFFF",
                             bd="0")
        loginButton.place(relx=0.1, rely=0.95, anchor=CENTER)
        loginButton.bind("<Button-1>", self.loginButtonclicked)

        # signup button

        finalsignupButton = Button(self.rframe, text="REGISTER", height=1, width=10, background="#5B8C44",
                                   foreground="#FFFFFF", bd="0")
        finalsignupButton.place(relx=0.69, rely=0.80, anchor=CENTER)
        finalsignupButton.bind("<Button-1>", self.RegisterButtonClicked)

    def RegisterButtonClicked(self, event):

        Name = self.name1entry.get()
        Gender = self.gender1entry.get()
        Email = self.email1entry.get()
        Password = self.pass1entry.get()
        ConPassword = self.pass2entry.get()

        if (Name == "" or Gender == "" or Email == "" or Password == "" or ConPassword == ""):
            messagebox.showinfo("Error!", "All fields are required")

        elif (Password != ConPassword):
            messagebox.showinfo("Error!", "Password didn't matched. Enter again")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="py_dev")
            self.cursor = con.cursor()
            self.cursor.execute(
                "insert into DETAIL_TABLE values('" + Name + "','" + Gender + "','" + Email + "','" + Password + "')")
            self.cursor.execute("commit")

            self.name1entry.delete(0, 'end')
            self.gender1entry.delete(0, 'end')
            self.email1entry.delete(0, 'end')
            self.pass1entry.delete(0, 'end')
            self.pass2entry.delete(0, 'end')

            messagebox.showinfo("Welcome Dear!", "Registration Complete Please Login Now.")

            con.close()

    # when login button is clicked this function will run..
    def loginButtonclicked(self, event):

        # This will clear the left-frame
        for widget in self.lframe.winfo_children():
            widget.destroy()

        # This will clear the right-frame
        for widget in self.rframe.winfo_children():
            widget.destroy()

        brand1photo = PhotoImage(file="/home/biky/Desktop/devdotpy/images/DEV.PY.png")
        brand2photo = Label(self.lframe, image=brand1photo, bg="#FFFFFF")
        brand2photo.image = brand1photo  # this will make a reference to tkinter object.
        brand2photo.place(relx=0.03, rely=0.02, anchor=NW)

        pylogo1photo = PhotoImage(file="/home/biky/Desktop/devdotpy/images/pylogo.png")
        pylogo2photo = Label(self.lframe, image=pylogo1photo, bg="#FFFFFF")
        pylogo2photo.image = pylogo1photo  # this will make a reference to tkinter object.
        pylogo2photo.place(relx=0.5, rely=0.15, anchor=CENTER)

        tag1photo = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Programming With Python.png")
        tag2photo = Label(self.lframe, image=tag1photo, bg="#FFFFFF")
        tag2photo.image = tag1photo
        tag2photo.place(relx=0.5, rely=0.30, anchor=CENTER)

        desk1design = PhotoImage(file="/home/biky/Desktop/devdotpy/images/deskdesign.png")
        desk2design = Label(self.lframe, image=desk1design, bg="#FFFFFF")
        desk2design.image = desk1design
        desk2design.place(relx=0.5, rely=0.65, anchor=CENTER)

        # right side frmae is from here

        back1photo = PhotoImage(file="/home/biky/Desktop/devdotpy/images/backbutton.png")
        back2photo = back1photo.subsample(3, 3)
        backbutton = Button(self.rframe, image=back2photo, text="Back", height=22, width=70, border="0", compound=LEFT,
                            background="#FFFFFF", foreground="#0A4350")
        backbutton.image = back2photo
        backbutton.place(relx=0.1, rely=0.05, anchor=CENTER)
        backbutton.bind("<Button-1>", self.callbacktomainpage)

        login1image = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Enter details to Login.png")
        login2image = Label(self.rframe, image=login1image, bg="#0A4350")
        login2image.image = login1image
        login2image.place(relx=0.5, rely=0.20, anchor=CENTER)

        enter1emailtext = PhotoImage(file="/home/biky/Desktop/devdotpy/images/enteremail.png")
        enter2emailtext = Label(self.rframe, image=enter1emailtext, bg="#0A4350")
        enter2emailtext.image = enter1emailtext
        enter2emailtext.place(relx=0.33, rely=0.34, anchor=CENTER)

        # # # # # # # # # # # # # # # # # # # #

        self.email1entry = Entry(self.rframe, font=large_font, bd="0", bg="#FFFFFF", fg="#0A4350",
                            justify=CENTER)
        self.email1entry.place(width=250, height=30, relx=0.5, rely=0.40, anchor=CENTER)

        enter1passtext = PhotoImage(file="/home/biky/Desktop/devdotpy/images/enterpass.png")
        enter2passtext = Label(self.rframe, image=enter1passtext, bg="#0A4350")
        enter2passtext.image = enter1passtext
        enter2passtext.place(relx=0.35, rely=0.49, anchor=CENTER)

        self.pass1entry = Entry(self.rframe, font=large_font, bd="0", bg="#FFFFFF", fg="#0A4350",
                           show="*", justify=CENTER)
        self.pass1entry.place(width=250, height=30, relx=0.5, rely=0.55, anchor=CENTER)

        forgotpassButton = Button(self.rframe, text="Forgot Password", height=1, width=15, background="#8C4444",
                                  foreground="#FFFFFF",
                                  bd="0")
        forgotpassButton.place(relx=0.409, rely=0.65, anchor=CENTER)

        finalloginButton = Button(self.rframe, text="LOGIN", height=1, width=7, background="#5B8C44",
                                  foreground="#FFFFFF",
                                  bd="0")
        finalloginButton.place(relx=0.65, rely=0.65, anchor=CENTER)
        finalloginButton.bind("<Button-1>", self.finalloginbuttonclicked)

    def finalloginbuttonclicked(self, event):
        Email = self.email1entry.get()
        Password = self.pass1entry.get()

        if (Email == "" or Password == ""):
            messagebox.showinfo("Error!", "All fields are required")
        else:
            try:
                self.con = mysql.connect(host="localhost", user="root", password="", database="py_dev")
            except:
                messagebox.showinfo("Error!", "Connection failed.")

            self.cursor = self.con.cursor()
            self.cursor.execute("select * from DETAIL_TABLE where Email = '" + Email + "' ")
            rows = self.cursor.fetchall()

            for row in rows:
                if row[3] != self.pass1entry.get():
                    messagebox.showinfo("Error !", "Enter Correct Email or Password.")
                    self.con.close()
                else:
                    finalpage(self.master, Email)


def finalpage(root, Email):
    root.destroy()  # this line will destroy the previous window..

    # from here new window starts.
    root = Tk()
    mainpage.Window2(root, Email)




def Main():  # run mainloop
    root = Tk()
    app = Window1(root)
    root.title("dev.py")
    root.resizable(0, 0)
    root.mainloop()


if __name__ == '__main__':
    Main()
