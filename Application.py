from tkinter import *
from datetime import date
from random import randint
from Databases import *

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.users = Users()
        self.posts = Posts()
        self.events = Events()
        self.attractions = Attractions()

        self.master = master
        self.pack()
        self.initpage()

    def clearWidgets(self):
        widgets = self.winfo_children()
        for item in widgets:
            if item.winfo_children():
                widgets.extend(item.winfo_children())
        for item in widgets:
            item.pack_forget()

    def initpage(self):
        self.clearWidgets()
        Label(self, text="Choose Login Or Register", width="30", height="2", font=("Calibri", 13)).pack() 
        Label(self, text="").pack()

        Button(self, text="Sign In", width="30", height="2", command=lambda: self.loginPage()).pack()
        Label(self, text="").pack()

        Button(self, text="Register", width="30", height="2", command=lambda: self.registerPage()).pack()
        Label(self, text="").pack()

    def loginPage(self):
        self.clearWidgets()

        username = ""
        password = ""

    def registerPage(self):
        self.clearWidgets()

        username = ""
        password = ""
        email = ""
        phonenum = ""

        Label(self, text="Enter the following information then click register").pack()
        Label(self, text="").pack()

        Label(self, text="Username").pack()
        usernameentry = Entry(self, textvariable=username)
        usernameentry.pack()
        Label(self, text="").pack()

        Label(self, text="Password").pack()
        passwordentry = Entry(self, textvariable=password)
        passwordentry.pack()
        Label(self, text="").pack()

        Label(self, text="Email Address").pack()
        emailentry = Entry(self, textvariable=email)
        emailentry.pack()
        Label(self, text="").pack()

        Label(self, text="Phone Number").pack()
        phonenumentry = Entry(self, textvariable=phonenum)
        phonenumentry.pack()
        Label(self, text="").pack()

        def registeruser():
            username = usernameentry.get()
            password = passwordentry.get()
            email = emailentry.get()
            phonenum = phonenumentry.get()
            uid = randint(100000000000,999999999999)
            self.users.addUser(uid,username,password,email,phonenum)
            self.initpage()

        Button(self, text="Register", width=30, height=2, command=lambda: registeruser()).pack()
        Label(self, text="").pack()