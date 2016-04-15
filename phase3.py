#Arthi Nithi, Anjani Agrawal, Alan Chiang, Alaap Murali

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pymysql


class Phase_three:
    def __init__(self,primaryWin):
        self.primaryWin = primaryWin
        self.Login()

        self.newUserWindow = Toplevel()
        self.Register()
        self.newUserWindow.title("New User Registration")
        self.newUserWindow.withdraw()
#       self.newUserWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.primaryWindow = Toplevel()
        self.primaryWindow.title("Welcome "+self.username.get())
        self.primaryWindow.withdraw()
 #       self.primaryWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.schoolInfoWin= Toplevel()
        self.schoolInfoWin.title("Add School Info")
        self.schoolInfoWin.withdraw()
 #       self.schoolInfo.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.trainSchWin= Toplevel()
        self.trainSchWin.title("View Train Schedule")
        self.trainSchWin.withdraw()
 #       self.schoolInfo.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.findAvailWindow= Toplevel()
        self.findAvailWindow.title("Search Rooms")
        self.findAvailWindow.withdraw()
 #       self.findAvailWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

    def Login(self):
        self.primaryWin.title("Login")
        frame = Frame(self.primaryWin)
        frame.pack()
        frame2 = Frame(self.primaryWin)
        frame2.pack()

        label1 = Label(frame,text = "Username")
        label2 = Label(frame,text ="Password")
        label1.grid(row = 0, column = 0,sticky=E)
        label2.grid(row = 1, column = 0,sticky=E)
        self.username = StringVar()
        self.password = StringVar()
        entry1 = Entry(frame, textvariable = self.username, width = 30)
        entry1.grid(row = 0, column = 1)
        entry2 = Entry(frame, textvariable = self.password, width = 30)
        entry2.grid(row = 1, column = 1)

        b1=Button(frame2, text ="Login", command=self.loginCredentials)
        b1.pack(side=LEFT)
        b2=Button(frame2, text ="Register", command= self.switchToRegister)
        b2.pack(side=LEFT)

    '''def loginCredentials(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Invalid input")
            return

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT * FROM CUSTOMER \
               WHERE Username = '%s' AND Password = '%s'" % (self.username.get(), self.password.get())
        cursor.execute(query)
        result1 = cursor.fetchall()
        query = "SELECT * FROM MANAGER \
               WHERE Username = '%s' AND Password = '%s'" % (self.username.get(), self.password.get())

        cursor.execute(query)
        result2 = cursor.fetchall()

        if len(result1) != 0:
            print("Customer")
            self.custOrManag = "customer"
            for row in results:
                self.name = row[0]
            self.switchtoMainMenu()
        elif len(result2) != 0:
            self.custOrManag = "manager"
            for row in results1:
                self.name = row[0]
            self.switchtoMainMenu()
        else:
            messagebox.showerror("Error", "Invalid username or password")'''

    def mainMenu(self):

        self.primaryWindow.title("Choose Functionality ")
        buttonsFrame = Frame(self.primaryWindow)
        buttonsFrame.pack()
 #       if self.custOrManag == "customer":
        b1 = Button(buttonsFrame, text ="View Train Schedule", command = self.trainSchedule)
        b1.pack(side=TOP)
        b2 = Button(buttonsFrame, text ="Make a new reservation", command = self.searchTrain)
        b2.pack(side=TOP)
        b3 = Button(buttonsFrame, text ="Update a reservation")
        b3.pack(side=TOP)
        b4 = Button(buttonsFrame, text ="Cancel a reservation")
        b4.pack(side=TOP)
        b5 = Button(buttonsFrame, text ="Give review")
        b5.pack(side=TOP)
        b6 = Button(buttonsFrame, text ="Add school information (student discount)", command = self.schoolInfo)
        b6.pack(side=TOP)

 #       else:
 #           b7 = Button(buttonsFrame, text ="View revenue report")
#            b7.pack(side=BOTTOM)
#            b8 = Button(buttonsFrame, text ="View popular route report")
#            b8.pack(side=BOTTOM)
        b9 = Button(buttonsFrame, text ="Log out")
        b9.pack(side=BOTTOM)

    def switchToRegister(self):
        self.primaryWin.withdraw()
        self.newUserWindow.deiconify()

    def switchToLogin(self):
        self.newUserWindow.withdraw()
        self.primaryWin.deiconify()
        print("YES")


    def switchtoMainMenu(self):
        self.primaryWin.withdraw()
        self.primaryWindow.deiconify()
        self.mainMenu()


    def Register(self):
        self.newUserWindow.title("New User Registration")
        frame2 = Frame(self.newUserWindow)
        frame2.pack()
        frame=Frame(self.newUserWindow)
        frame.pack()
        frame3=Frame(self.newUserWindow)
        frame3.pack(side=RIGHT)

        label1 = Label(frame,text = "Username")
        label2 = Label(frame,text ="Email Address")
        label3 = Label(frame,text = "Password")
        label4 = Label(frame,text ="Confirm Password")
        label1.grid(row = 0, column = 0,sticky=W)
        label2.grid(row = 1, column = 0,sticky=W)
        label3.grid(row = 2, column = 0,sticky=W)
        label4.grid(row = 3, column = 0,sticky=W)
        self.registeredUser = StringVar()
        self.registeredPass = StringVar()
        self.registeredPassConfirm = StringVar()
        self.registerEmail = StringVar()
        self.uentry = Entry(frame, textvariable = self.registeredUser, width = 30)
        self.uentry.grid(row = 0, column = 1)
        self.password_entry = Entry(frame, textvariable = self.registeredPass, width = 30)
        self.password_entry.grid(row = 1, column = 1)
        self.confirm_password_entry = Entry(frame, textvariable = self.registeredPassConfirm, width = 30)
        self.confirm_password_entry.grid(row = 2, column = 1)
        self.email_entry = Entry(frame, textvariable = self.registerEmail, width = 30)
        self.email_entry.grid(row = 3, column = 1)

        b_reg=Button(frame3, text ="Create", command=self.registerCredentials)
        b_reg.pack()

    '''def registerCredentials(self):
        if self.registeredUser.get() == "" or self.registeredPass.get() == "" or self.registeredPassConfirm.get() == "" or self.registerEmail.get() == "":
            messagebox.showerror("Error", "Invalid input")
            return

        if self.registeredPass.get() != self.registeredPassConfirm.get():
            messagebox.showerror("Error", "Passwords must match")
            return

        server = self.Connect()
        cursor = server.cursor()
        query1 = "SELECT * FROM CUSTOMER, MANAGER \
               WHERE CUSTOMER.Username = '%s' OR MANAGER.Username = '%s'" % (self.registeredUser.get(), self.registeredUser.get())
        print(query1)
        cursor.execute(query1)
        result1 = cursor.fetchall()
        print(result1)
        cursor.execute(query1)
        if len(result1) != 0:
            messagebox.showerror("Error", "Username already in use")
            return

        query2 = "INSERT INTO CUSTOMER(Username, Password, Email) \
               VALUES ('%s', '%s', '%s')" % (self.registeredUser.get(), self.registeredPass.get(), self.registerEmail.get())
        print(query2)
        cursor.execute(query2)
        result2 = cursor.fetchall()
        self.switchToLogin()'''



    def schoolInfo(self):
        self.primaryWindow.withdraw()
        self.schoolInfoWin.deiconify()
        self.schoolInfoWin.title("Add School Info")
        frame1 = Frame(self.schoolInfoWin)
        frame2 = Frame(self.schoolInfoWin)
        frame1.pack(side = TOP)
        frame2.pack(side = BOTTOM)
        self.emailaddress = StringVar()
        self.entry = Entry(frame1, textvariable = self.emailaddress, width = 30)
        self.entry.pack(side=RIGHT)
        label1 = Label(frame1,text = "School Email Address")
        label1.pack(side=TOP)
        label2 = Label(frame1,text = "Your school email adress ends with .edu")
        label2.pack(side=BOTTOM)

        b1 = Button(frame2, text ="Back")
        b1.pack(side=LEFT)
        b2 = Button(frame2, text ="Submit")
        b2.pack(side=RIGHT)

    def trainSchedule(self):
        self.primaryWindow.withdraw()
        self.trainSchWin.deiconify()
        self.trainSchWin.title("View Train Schedule")
        frame1 = Frame(self.trainSchWin)
        frame2 = Frame(self.trainSchWin)
        frame1.pack(side = TOP)
        frame2.pack(side = BOTTOM)
        self.trainName = StringVar()
        self.entry = Entry(frame1, textvariable = self.trainName , width = 30)
        self.entry.pack(side=RIGHT)
        label1 = Label(frame1,text = "Train Number")
        label1.pack(side=LEFT)


        b1 = Button(frame2, text ="Search")
        b1.pack(side=LEFT)

    def searchTrain(self):
        self.primaryWindow.withdraw()
        self.findAvailWindow.deiconify()

        self.findAvailWindow.title("Search Train")
        frame = Frame(self.findAvailWindow)
        frame.pack(side=TOP)
        frame1=Frame(self.findAvailWindow)
        frame1.pack(side=TOP)
        frame2=Frame(self.findAvailWindow)
        frame2.pack(side=TOP)
        frame3=Frame(self.findAvailWindow)
        frame3.pack(side=TOP)

        location= Label(frame,text = "Departs From")
        location.pack(side=LEFT)
        self.city = StringVar()
        choices = ["Atlanta", "Charlotte", "Savannah", "Orlando", "Miami"]
        self.city.set(choices[0])
        option=OptionMenu(frame, self.city, choices[0], *choices)
        option.pack(side=RIGHT)

        arriveAt= Label(frame1,text ="Arrives At")
        arriveAt.pack(side=LEFT)
#        start_date= Label(frame,text ="Start Date (MM/DD/YYYY)")
#       self.startDateEntry = Entry(frame1, textvariable = start_date, width = 30)
#        self.endDateEntry = Entry(frame1, textvariable = end_date, width = 30)

        depDate= Label(frame2,text ="Departure Date")
        depDate.pack(side=LEFT)
        self.date = StringVar()
        choices = ["Atlanta", "Charlotte", "Savannah", "Orlando", "Miami"]
        self.date.set(choices[0])
        option=OptionMenu(frame2, self.date, choices[0], *choices)
        option.pack(side=RIGHT)

        b=Button(frame3, text ="Find Trains")
        b.pack(side=RIGHT)




mw = Tk()
app = Phase_three(mw)
mw.mainloop()
