import tkinter as tk
from datetime import date

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
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
        tk.Label(self, text="Choose Login Or Register", width="30", height="2", font=("Calibri", 13)).pack() 
        tk.Label(self, text="").pack()

        tk.Button(self, text="Sign In", width="30", height="2", command=lambda: self.loginPage()).pack()
        tk.Label(self, text="").pack()

        tk.Button(self, text="Register", width="30", height="2", command=lambda: self.registerPage()).pack()
        tk.Label(self, text="").pack()

    def loginPage(self):
        self.clearWidgets()

    def registerPage(self):
        self.clearWidgets()

        def registeruser(ue, pe, ee, pne, dobe, username, password, email, phonenum, dob):
            username = ue.get()
            password = pe.get()
            email = ee.get()
            phonenum = pne.get()
            #dob = dobe.get()
            print(username + "\n" + password  + "\n" +  email  + "\n" + phonenum + "\n" + dob.strftime("%m-%d-%Y"))

        username = ""
        password = ""
        email = ""
        phonenum = ""
        dob = date(1800,1,1)

        tk.Label(self, text="Enter the following information then click register").pack()
        tk.Label(self, text="").pack()

        tk.Label(self, text="Username").pack()
        ue = tk.Entry(self, textvariable=username).pack()
        tk.Label(self, text="").pack()

        tk.Label(self, text="Password").pack()
        pe = tk.Entry(self, textvariable=password).pack()
        tk.Label(self, text="").pack()

        tk.Label(self, text="Email Address").pack()
        ee = tk.Entry(self, textvariable=email).pack()
        tk.Label(self, text="").pack()

        tk.Label(self, text="Phone Number").pack()
        pne = tk.Entry(self, textvariable=phonenum).pack()
        tk.Label(self, text="").pack()

        tk.Label(self, text="Date of Birth").pack()
        dobe = None
        tk.Label(self, text="").pack()

        tk.Button(self, text="Register", width=30, height=2, command=lambda: registeruser(ue,pe,ee,pne,dobe,username,password,email,phonenum,dob)).pack()
        tk.Label(self, text="").pack()
