from driver import *
from Database.pythonbasiccourse import python_basic_course
large_font = ('spacemono', 16, 'bold')
mid_font = ('spacemono', 14)
small_font = ('spacemono', 12)

class Window2:
    def __init__(self, master, Email):
        self.Email = Email
        self.master = master
        master.title("dev.py")
        master.geometry('1366x768')
        master.configure(bg="#FFFFFF")

        self.topframe = Frame(master, width=1366, height=70, bg="#E0F0FF")
        self.topframe.grid(row=0, column=0, columnspan=3)

        self.leftframe = Frame(master, width=200, height=698, bg="#E0F0FF")
        self.leftframe.grid(row=1, column=0)

        self.mframe = Frame(master, width=800, height=698,  bg="#E0F0FF")
        self.mframe.grid(row=1, column=1)

        self.mcanvas = Canvas(self.mframe, height=550, width=780,bd=0, highlightthickness=0, relief='ridge', bg="#E0F0FF")
        self.mcanvas.place(relx = 0.5, rely = 0.462, anchor= CENTER)
        # (bd=0, highlightthickness=0, relief='ridge') will remve the light border across canvas.
        my_image1 = PhotoImage(file='/home/biky/Desktop/devdotpy/images/mcanvasbg.png')
        self.mcanvas.create_image(390, 275, image=my_image1, anchor=CENTER)

        self.rightframe = Frame(master, width=366, height=698, bg="#E0F0FF")
        self.rightframe.grid(row=1, column=2)

        self.rcanvas = Canvas(self.rightframe, height=550, width=340,bd=0, highlightthickness=0, relief='ridge', bg="#E0F0FF")
        self.rcanvas.place(relx=0.5, rely=0.462, anchor=CENTER)
        my_image2 = PhotoImage(file='/home/biky/Desktop/devdotpy/images/rcanvasbg.png')
        self.rcanvas.create_image(170, 275, image=my_image2, anchor=CENTER)

        vector1line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector1.png")
        vector2line = Label(self.topframe, image=vector1line)
        vector2line.image = vector1line
        vector2line.place(relx=0.5, rely=1, anchor=CENTER)

        vector1111line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector4.png")
        vector2222line = Label(self.leftframe, image=vector1111line)
        vector2222line.image = vector1111line
        vector2222line.place(relx=0.1, rely=0.14)

        # from here decoration start of upper frame.

        dash1board = PhotoImage(file="/home/biky/Desktop/devdotpy/images/DashboardButtoninactive.png")
        dash2board = Label(self.topframe, image=dash1board, bg="#E0F0FF")
        dash2board.image = dash1board
        dash2board.place(relx=0.19, rely=0.69, anchor=CENTER)
        dash2board.bind("<Button-1>", self.dashboardpanel)

        class1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/ClassesButtoninactive.png")
        class2button = Label(self.topframe, image=class1button, bg="#E0F0FF")
        class2button.image = class1button
        class2button.place(relx=0.35, rely=0.69, anchor=CENTER)
        class2button.bind("<Button-1>", self.classpanel)

        resource1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/ResorcesButtoninactive.png")
        resource2button = Label(self.topframe, image=resource1button, bg="#E0F0FF")
        resource2button.image = resource1button
        resource2button.place(relx=0.51, rely=0.69, anchor=CENTER)
        resource2button.bind("<Button-1>", self.resourcepanel)

        relax1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/relaxationbuttoninactive.png")
        relax2button = Label(self.topframe, image=relax1button, bg="#E0F0FF")
        relax2button.image = relax1button
        relax2button.place(relx=0.67, rely=0.69, anchor=CENTER)
        relax2button.bind("<Button-1>", self.relaxpanel)

        self.dashboardpanel(self)

        master.mainloop()



################################################## DASHBOARD PANEL ###########################################



    def dashboardpanel(self, event):
        # This will clear the mframe-frame
        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        for widget in self.rcanvas.winfo_children():
            widget.destroy()

        for widget in self.leftframe.winfo_children():
            widget.destroy()

        dash1board = PhotoImage(file="/home/biky/Desktop/devdotpy/images/DashboardButtonactive.png")
        dash2board = Label(self.leftframe, image=dash1board, bg="#E0F0FF")
        dash2board.image = dash1board
        dash2board.place(relx=0.5, rely=0.1, anchor=CENTER)

        vector1111line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector4.png")
        vector2222line = Label(self.leftframe, image=vector1111line)
        vector2222line.image = vector1111line
        vector2222line.place(relx=0.1, rely=0.14)

        settings1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/settingsbutton.png")
        settings2button = Label(self.leftframe, image=settings1button, bg="#E0F0FF")
        settings2button.image = settings1button
        settings2button.place(relx=0.5, rely=0.66, anchor=CENTER)
        settings2button.bind("<Button-1>", self.settingpanel)

        feedback1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/feedbackbutton.png")
        feedback2button = Label(self.leftframe, image=feedback1button, bg="#E0F0FF")
        feedback2button.image = feedback1button
        feedback2button.place(relx=0.5, rely=0.74, anchor=CENTER)
        feedback2button.bind("<Button-1>", self.feedbackpanel)

        aboutus1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/aboutusbutton.png")
        aboutus2button = Label(self.leftframe, image=aboutus1button, bg="#E0F0FF")
        aboutus2button.image = aboutus1button
        aboutus2button.place(relx=0.5, rely=0.82, anchor=CENTER)
        aboutus2button.bind("<Button-1>", self.aboutuspanel)



           ########3######      Profile  will be shown in dashboard panel.     ###################

        con = mysql.connect(host="localhost", user="root", password="", database="py_dev")
        self.cursor = con.cursor()
        self.cursor.execute("select * from DETAIL_TABLE where Email = '" + self.Email + "' ")
        rows = self.cursor.fetchall()

        for row in rows:
            self.Name = row[0]
            self.Gender = row[1]
            self.Emailid = row[2]

        if self.Gender == 'm' or self.Gender == 'M':
            user1image = PhotoImage(file="/home/biky/Desktop/devdotpy/images/malecharacter.png")
            user2image = Label(self.rcanvas, image=user1image, bg="#FFFFFF")
            user2image.image = user1image
            user2image.place(relx=0.5, rely=0.3, anchor=CENTER)
        else:
            user1image = PhotoImage(file="/home/biky/Desktop/devdotpy/images/femalecharacter.png")
            user2image = Label(self.rcanvas, image=user1image, bg="#FFFFFF")
            user2image.image = user1image
            user2image.place(relx=0.5, rely=0.3, anchor=CENTER)

        username = Label(self.rcanvas, text=self.Name, bg="#FFFFFF", font=large_font)
        username.place(relx=0.5, rely=0.52, anchor=CENTER)

        username = Label(self.rcanvas, text=self.Email, bg="#FFFFFF", font=mid_font)
        username.place(relx=0.5, rely=0.58, anchor=CENTER)


#############################################  CLASS PANEL #####################################


    def classpanel(self, event):
        # This will clear the mframe-frame
        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        for widget in self.leftframe.winfo_children():
            widget.destroy()

        class1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/ClassesButtonactive.png")
        class2button = Label(self.leftframe, image=class1button, bg="#E0F0FF")
        class2button.image = class1button
        class2button.place(relx=0.5, rely=0.1, anchor=CENTER)

        vector1111line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector4.png")
        vector2222line = Label(self.leftframe, image=vector1111line)
        vector2222line.image = vector1111line
        vector2222line.place(relx=0.1, rely=0.14)

        settings1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/settingsbutton.png")
        settings2button = Label(self.leftframe, image=settings1button, bg="#E0F0FF")
        settings2button.image = settings1button
        settings2button.place(relx=0.5, rely=0.66, anchor=CENTER)
        settings2button.bind("<Button-1>", self.settingpanel)

        feedback1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/feedbackbutton.png")
        feedback2button = Label(self.leftframe, image=feedback1button, bg="#E0F0FF")
        feedback2button.image = feedback1button
        feedback2button.place(relx=0.5, rely=0.74, anchor=CENTER)
        feedback2button.bind("<Button-1>", self.feedbackpanel)

        aboutus1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/aboutusbutton.png")
        aboutus2button = Label(self.leftframe, image=aboutus1button, bg="#E0F0FF")
        aboutus2button.image = aboutus1button
        aboutus2button.place(relx=0.5, rely=0.82, anchor=CENTER)
        aboutus2button.bind("<Button-1>", self.aboutuspanel)

        basic1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/basicsButton.png")
        basic2button = Label(self.leftframe, image=basic1button, bg="#E0F0FF")
        basic2button.image = basic1button
        basic2button.place(relx=0.5, rely=0.2, anchor=CENTER)
        basic2button.bind("<Button-1>", self.basicbuttonclicked)

        intermediate1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/intermediateButton.png")
        intermediate2button = Label(self.leftframe, image=intermediate1button, bg="#E0F0FF")
        intermediate2button.image = intermediate1button
        intermediate2button.place(relx=0.5, rely=0.3, anchor=CENTER)
        intermediate2button.bind("<Button-1>", self.intermediatebuttonclicked)

        professional1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/professionalButton.png")
        professional2button = Label(self.leftframe, image=professional1button, bg="#E0F0FF")
        professional2button.image = professional1button
        professional2button.place(relx=0.5, rely=0.4, anchor=CENTER)

        intro1classtext = PhotoImage(file="/home/biky/Desktop/devdotpy/images/introtocourse.png")
        intro2classtext = Label(self.mcanvas, image=intro1classtext, bg="#F6F7F8")
        intro2classtext.image = intro1classtext
        intro2classtext.place(relx=0.5, rely=0.5, anchor=CENTER)


        ################################# BASIC PANEL #######################################

    def basicbuttonclicked(self, event):

        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        pythonbasic1link = PhotoImage(file="/home/biky/Desktop/devdotpy/images/pythonenrol.png")
        pythonbasic2link = Label(self.mcanvas, image=pythonbasic1link, bg="#F6F7F8")
        pythonbasic2link.image = pythonbasic1link
        pythonbasic2link.place(relx=0.25, rely=0.2, anchor=CENTER)
        pythonbasic2link.bind("<Button-1>", self.to_python)

        cbasic1link = PhotoImage(file="/home/biky/Desktop/devdotpy/images/cenrol.png")
        cbasic2link = Label(self.mcanvas, image=cbasic1link, bg="#F6F7F8")
        cbasic2link.image = cbasic1link
        cbasic2link.place(relx=0.75, rely=0.45, anchor=CENTER)

        jsbasic1link = PhotoImage(file="/home/biky/Desktop/devdotpy/images/jsenrol.png")
        jsbasic2link = Label(self.mcanvas, image=jsbasic1link, bg="#F6F7F8")
        jsbasic2link.image = jsbasic1link
        jsbasic2link.place(relx=0.25, rely=0.7, anchor=CENTER)



    def to_python(self, event):

        self.master.destroy()

        root = Tk()
        python_basic_course(root)


         ###########################################  INTERMEDIATE PANEL #######################################

    def intermediatebuttonclicked(self, event):
        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        pythoninter1link = PhotoImage(file="/home/biky/Desktop/devdotpy/images/pythonienrol.png")
        pythoninter2link = Label(self.mcanvas, image=pythoninter1link, bg="#F6F7F8")
        pythoninter2link.image = pythoninter1link
        pythoninter2link.place(relx=0.3, rely=0.3, anchor=CENTER)

        cinter1link = PhotoImage(file="/home/biky/Desktop/devdotpy/images/cienrol.png")
        cinter2link = Label(self.mcanvas, image=cinter1link, bg="#F6F7F8")
        cinter2link.image = cinter1link
        cinter2link.place(relx=0.7, rely=0.7, anchor=CENTER)


######################################## RESOURCE PANEL ################################################################




    def resourcepanel(self, event):
        # This will clear the mframe-frame
        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        for widget in self.leftframe.winfo_children():
            widget.destroy()

        resource1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/ResorcesButtonactive.png")
        resource2button = Label(self.leftframe, image=resource1button, bg="#E0F0FF")
        resource2button.image = resource1button
        resource2button.place(relx=0.5, rely=0.1, anchor=CENTER)

        vector1111line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector4.png")
        vector2222line = Label(self.leftframe, image=vector1111line)
        vector2222line.image = vector1111line
        vector2222line.place(relx=0.1, rely=0.14)

        settings1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/settingsbutton.png")
        settings2button = Label(self.leftframe, image=settings1button, bg="#E0F0FF")
        settings2button.image = settings1button
        settings2button.place(relx=0.5, rely=0.66, anchor=CENTER)
        settings2button.bind("<Button-1>", self.settingpanel)

        feedback1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/feedbackbutton.png")
        feedback2button = Label(self.leftframe, image=feedback1button, bg="#E0F0FF")
        feedback2button.image = feedback1button
        feedback2button.place(relx=0.5, rely=0.74, anchor=CENTER)
        feedback2button.bind("<Button-1>", self.feedbackpanel)

        aboutus1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/aboutusbutton.png")
        aboutus2button = Label(self.leftframe, image=aboutus1button, bg="#E0F0FF")
        aboutus2button.image = aboutus1button
        aboutus2button.place(relx=0.5, rely=0.82, anchor=CENTER)
        aboutus2button.bind("<Button-1>", self.aboutuspanel)




################################################## SETTINGS PANEL ###########################################

    def settingpanel(self, event):
        # This will clear the mframe-frame
        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        for widget in self.leftframe.winfo_children():
            widget.destroy()

        settings1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/settingsbuttonactive.png")
        settings2button = Label(self.leftframe, image=settings1button, bg="#E0F0FF")
        settings2button.image = settings1button
        settings2button.place(relx=0.5, rely=0.1, anchor=CENTER)

        vector1111line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector4.png")
        vector2222line = Label(self.leftframe, image=vector1111line)
        vector2222line.image = vector1111line
        vector2222line.place(relx=0.1, rely=0.14)

        settings1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/settingsbutton.png")
        settings2button = Label(self.leftframe, image=settings1button, bg="#E0F0FF")
        settings2button.image = settings1button
        settings2button.place(relx=0.5, rely=0.66, anchor=CENTER)
        settings2button.bind("<Button-1>", self.settingpanel)

        feedback1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/feedbackbutton.png")
        feedback2button = Label(self.leftframe, image=feedback1button, bg="#E0F0FF")
        feedback2button.image = feedback1button
        feedback2button.place(relx=0.5, rely=0.74, anchor=CENTER)
        feedback2button.bind("<Button-1>", self.feedbackpanel)

        aboutus1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/aboutusbutton.png")
        aboutus2button = Label(self.leftframe, image=aboutus1button, bg="#E0F0FF")
        aboutus2button.image = aboutus1button
        aboutus2button.place(relx=0.5, rely=0.82, anchor=CENTER)
        aboutus2button.bind("<Button-1>", self.aboutuspanel)


######################################  FEEDBACK PANEL ###############################################




    def feedbackpanel(self, event):
        # This will clear the mframe-frame
        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        for widget in self.leftframe.winfo_children():
            widget.destroy()

        feedback1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/feedbackbuttonactive.png")
        feedback2button = Label(self.leftframe, image=feedback1button, bg="#E0F0FF")
        feedback2button.image = feedback1button
        feedback2button.place(relx=0.5, rely=0.1, anchor=CENTER)

        vector1111line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector4.png")
        vector2222line = Label(self.leftframe, image=vector1111line)
        vector2222line.image = vector1111line
        vector2222line.place(relx=0.1, rely=0.14)

        settings1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/settingsbutton.png")
        settings2button = Label(self.leftframe, image=settings1button, bg="#E0F0FF")
        settings2button.image = settings1button
        settings2button.place(relx=0.5, rely=0.66, anchor=CENTER)
        settings2button.bind("<Button-1>", self.settingpanel)

        feedback1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/feedbackbutton.png")
        feedback2button = Label(self.leftframe, image=feedback1button, bg="#E0F0FF")
        feedback2button.image = feedback1button
        feedback2button.place(relx=0.5, rely=0.74, anchor=CENTER)
        feedback2button.bind("<Button-1>", self.feedbackpanel)

        aboutus1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/aboutusbutton.png")
        aboutus2button = Label(self.leftframe, image=aboutus1button, bg="#E0F0FF")
        aboutus2button.image = aboutus1button
        aboutus2button.place(relx=0.5, rely=0.82, anchor=CENTER)
        aboutus2button.bind("<Button-1>", self.aboutuspanel)



################################################# ABOUTUS PANEL ################################################




    def aboutuspanel(self, event):
        # This will clear the mframe-frame
        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        for widget in self.leftframe.winfo_children():
            widget.destroy()

        aboutus1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/aboutusbuttonactive.png")
        aboutus2button = Label(self.leftframe, image=aboutus1button, bg="#E0F0FF")
        aboutus2button.image = aboutus1button
        aboutus2button.place(relx=0.5, rely=0.1, anchor=CENTER)

        vector1111line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector4.png")
        vector2222line = Label(self.leftframe, image=vector1111line)
        vector2222line.image = vector1111line
        vector2222line.place(relx=0.1, rely=0.14)

        settings1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/settingsbutton.png")
        settings2button = Label(self.leftframe, image=settings1button, bg="#E0F0FF")
        settings2button.image = settings1button
        settings2button.place(relx=0.5, rely=0.66, anchor=CENTER)
        settings2button.bind("<Button-1>", self.settingpanel)

        feedback1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/feedbackbutton.png")
        feedback2button = Label(self.leftframe, image=feedback1button, bg="#E0F0FF")
        feedback2button.image = feedback1button
        feedback2button.place(relx=0.5, rely=0.74, anchor=CENTER)
        feedback2button.bind("<Button-1>", self.feedbackpanel)

        aboutus1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/aboutusbutton.png")
        aboutus2button = Label(self.leftframe, image=aboutus1button, bg="#E0F0FF")
        aboutus2button.image = aboutus1button
        aboutus2button.place(relx=0.5, rely=0.82, anchor=CENTER)
        aboutus2button.bind("<Button-1>", self.aboutuspanel)



##################################################### RELAX PANEL ###########################################



    def relaxpanel(self, event):
        # This will clear the mframe-frame
        for widget in self.mcanvas.winfo_children():
            widget.destroy()

        for widget in self.leftframe.winfo_children():
            widget.destroy()

        relax1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/relaxationbuttonactive.png")
        relax2button = Label(self.leftframe, image=relax1button, bg="#E0F0FF")
        relax2button.image = relax1button
        relax2button.place(relx=0.5, rely=0.1, anchor=CENTER)

        vector1111line = PhotoImage(file="/home/biky/Desktop/devdotpy/images/Vector4.png")
        vector2222line = Label(self.leftframe, image=vector1111line)
        vector2222line.image = vector1111line
        vector2222line.place(relx=0.1, rely=0.14)

        settings1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/settingsbutton.png")
        settings2button = Label(self.leftframe, image=settings1button, bg="#E0F0FF")
        settings2button.image = settings1button
        settings2button.place(relx=0.5, rely=0.66, anchor=CENTER)
        settings2button.bind("<Button-1>", self.settingpanel)

        feedback1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/feedbackbutton.png")
        feedback2button = Label(self.leftframe, image=feedback1button, bg="#E0F0FF")
        feedback2button.image = feedback1button
        feedback2button.place(relx=0.5, rely=0.74, anchor=CENTER)
        feedback2button.bind("<Button-1>", self.feedbackpanel)

        aboutus1button = PhotoImage(file="/home/biky/Desktop/devdotpy/images/aboutusbutton.png")
        aboutus2button = Label(self.leftframe, image=aboutus1button, bg="#E0F0FF")
        aboutus2button.image = aboutus1button
        aboutus2button.place(relx=0.5, rely=0.82, anchor=CENTER)
        aboutus2button.bind("<Button-1>", self.aboutuspanel)

    ######################### TO PYTHON COURSE ##########################