#Group 93: Vagdevi Kondeti, Srida Saraogi, Kameron Akbar, Bhavani Jaladanki

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pymysql
from datetime import datetime
#from dateutil import parser
import random
import calendar
from collections import OrderedDict

class UserSelected(Checkbutton):
    def __init__(self,*args,**chargs):
        self.var = IntVar()
        self.text = chargs['text']
        self.roomtuple = None
        chargs['variable'] = self.var
        Checkbutton.__init__(self,*args,**chargs)

    def pickRoom(self, roomtuple):
        self.roomtuple = roomtuple

    def is_checked(self):
        return self.var.get()

    def toString(self):
        return self.text

    def selectRoom(self):
        if self.roomtuple:
            return self.roomtuple

class Part_Three:
    def __init__(self,primaryWin):
        self.primaryWin = primaryWin
        self.Login()
        self.primaryWin.title("Login")
        self.custOrManag = ""
        self.name = ""
        self.totalCost = 0


        self.newUserWindow = Toplevel()
        self.Register()
        self.newUserWindow.title("New User Registration")
        self.newUserWindow.withdraw()
        self.newUserWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.primaryWindow = Toplevel()
        self.primaryWindow.title("Welcome "+self.username.get())
        self.primaryWindow.withdraw()
        self.primaryWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.findAvailWindow= Toplevel()
        self.findAvailWindow.title("Search Rooms")
        self.findAvailWindow.withdraw()
        self.findAvailWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.createResWindow= Toplevel()
        self.createResWindow.title("Make Reservation")
        self.createResWindow.withdraw()
        self.createResWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.detWindow= Toplevel()
        self.detWindow.title("Check Details")
        self.detWindow.withdraw()
        self.detWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.finalResWindow= Toplevel()
        self.finalResWindow.title("Confirmation")
        self.finalResWindow.withdraw()
        self.finalResWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)


        self.putIDCancelWindow= Toplevel()
        self.putIDCancelWindow.title("Cancel Reservation")
        self.putIDCancelWindow.withdraw()
        self.putIDCancelWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.cancResWindow= Toplevel()
        self.cancResWindow.title("Cancel Reservation")
        self.cancResWindow.withdraw()
        self.cancResWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.insertDatWindows = Toplevel()
        self.insertDatWindows.title("Update Reservation")
        self.insertDatWindows.withdraw()
        self.insertDatWindows.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.updateResWindow= Toplevel()
        self.updateResWindow.title("Update Reservation")
        self.updateResWindow.withdraw()
        self.updateResWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.finalDatesWindow= Toplevel()
        self.finalDatesWindow.title("Update Reservation")
        self.finalDatesWindow.withdraw()
        self.finalDatesWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.creditCardWin1 = Toplevel()
        self.creditCardWin1.title("Add Card")
        self.creditCardWin1.withdraw()
        self.creditCardWin1.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.creditCardWin2 = Toplevel()
        self.creditCardWin2.title("Delete Card")
        self.creditCardWin2.withdraw()
        self.creditCardWin2.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.seeRepWindow = Toplevel()
        self.seeRepWindow.title("View Report")
        self.seeRepWindow.withdraw()
        self.seeRepWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.popResReportWindow = Toplevel()
        self.popResReportWindow.title("Popular Report")
        self.popResReportWindow.withdraw()
        self.popResReportWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.seeReportWindow = Toplevel()
        self.seeReportWindow.title("Delete Card")
        self.seeReportWindow.withdraw()
        self.seeReportWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.provideReviewWindow = Toplevel()
        self.provideReviewWindow.title("Give Review")
        self.provideReviewWindow.withdraw()
        self.provideReviewWindow.protocol("WM DELETE WINDOW", self.closeWindow)

        self.tyWindow = Toplevel()
        self.tyWindow.title("Thank You")
        self.tyWindow.withdraw()
        self.tyWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.seeRevWindow = Toplevel()
        self.seeRevWindow.title("View Review")
        self.seeRevWindow.withdraw()
        self.seeRevWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)



    def closeWindow(self):
        self.primaryWin.withdraw()

    def Connect(self):
        try:
            db = pymysql.connect(host="academic-mysql.cc.gatech.edu", passwd="MgdNYI5e", user="cs4400_Group_93",db="cs4400_Group_93")
            return db
        except:
            messagebox.showerror("Error", "Check Internet Connection")

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
        b2=Button(frame2, text ="New User? Create Account", command=self.switchToRegister)
        b2.pack(side=LEFT)

    def loginCredentials(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Fields cannot be left blank")
            return

        db = self.Connect()
        cursor = db.cursor()
        sql = "SELECT * FROM CUSTOMER \
               WHERE Username = '%s' AND Password = '%s'" % (self.username.get(), self.password.get())
        cursor.execute(sql)
        results = cursor.fetchall()
        sql = "SELECT * FROM MANAGER \
               WHERE Username = '%s' AND Password = '%s'" % (self.username.get(), self.password.get())

        cursor.execute(sql)
        results1 = cursor.fetchall()

        if len(results) != 0:
            print("Customer")
            self.custOrManag = "customer"
            for row in results:
                self.name = row[0]
            self.switchtoMainMenu()

        elif len(results1) != 0:
            self.custOrManag = "manager"
            for row in results1:
                self.name = row[0]
            self.switchtoMainMenu()

        else:
            messagebox.showerror("Error", "User does not exist, or wrong login credentials")


    def mainMenu(self):

        self.primaryWindow.title("Welcome " + self.username.get())
        buttonsFrame = Frame(self.primaryWindow)
        buttonsFrame.pack()
        if self.custOrManag == "customer":
            b1 = Button(buttonsFrame, text ="Make a new reservation", command=self.searchRooms)
            b1.pack(side=TOP)
            b2 = Button(buttonsFrame, text ="Update your reservation",command=self.updateResv)
            b2.pack(side=TOP)
            b3 = Button(buttonsFrame, text ="Cancel Reservation",command=self.cancelResv)
            b3.pack(side=TOP)
            b4 = Button(buttonsFrame, text ="Provide feedback", command=self.provideFB)
            b4.pack(side=TOP)
            b5 = Button(buttonsFrame, text ="View feedback" ,command=self.viewFB)
            b5.pack(side=TOP)
        else:
            b6 = Button(buttonsFrame, text ="View Reservation report",command=self.viewReport)
            b6.pack(side=BOTTOM)
            b7 = Button(buttonsFrame, text ="View Popular room category report",command=self.viewPopReport)
            b7.pack(side=BOTTOM)
            b8 = Button(buttonsFrame, text ="View revenue report",command=self.viewRevenue)
            b8.pack(side=BOTTOM)


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
        label2 = Label(frame,text ="Password")
        label3 = Label(frame,text = "Confirm Password")
        label4 = Label(frame,text ="Email")
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

        b_reg=Button(frame3, text ="Submit", command=self.registerCredentials)
        b_reg.pack(side=BOTTOM)

    def registerCredentials(self):
        if self.registeredUser.get() == "" or self.registeredPass.get() == "" or self.registeredPassConfirm.get() == "" or self.registerEmail.get() == "":
            messagebox.showerror("Error", "Cannot leave fields blank")
            return
        if self.registeredPass.get() != self.registeredPassConfirm.get():
            messagebox.showerror("Error", "Passwords do not match")
            return
        db = self.Connect()
        cursor = db.cursor()
        sql = "SELECT * FROM CUSTOMER, MANAGER \
               WHERE CUSTOMER.Username = '%s' OR MANAGER.Username = '%s'" % (self.registeredUser.get(),self.registeredUser.get())
        print(sql)
        cursor.execute(sql)
        x = cursor.fetchall()
        print(x)
        cursor.execute(sql)
        if len(x) != 0:
            messagebox.showerror("Error", "This username is already being used")
            return

        sql = "INSERT INTO CUSTOMER(Username, Password, Email) \
               VALUES ('%s', '%s', '%s')" % (self.registeredUser.get(), self.registeredPass.get(), self.registerEmail.get())
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        self.switchToLogin()

    def searchRooms(self):
        self.primaryWindow.withdraw()
        self.findAvailWindow.deiconify()

        self.findAvailWindow.title("Search Rooms")
        frame1=Frame(self.findAvailWindow)
        frame1.pack()

        location= Label(frame1,text = "Location")
        start_date= Label(frame1,text ="Start Date (MM/DD/YYYY)")
        end_date= Label(frame1,text ="End Date (MM/DD/YYYY)")
        self.startDateEntry = Entry(frame1, textvariable = start_date, width = 30)
        self.endDateEntry = Entry(frame1, textvariable = end_date, width = 30)

        self.cityVar = StringVar()
        choices = ["Atlanta", "Charlotte", "Savannah", "Orlando", "Miami"]
        self.cityVar.set(choices[0])
        option=OptionMenu(frame1, self.cityVar, choices[0], *choices)
        option.grid(row=0,column=1,sticky=E)

        location.grid(row = 0, column = 0,sticky=E)
        start_date.grid(row = 1, column = 0,sticky=E)
        end_date.grid(row = 2, column = 0,sticky=E)
        self.startDateEntry.grid(row = 1, column = 1)
        self.endDateEntry.grid(row = 2, column = 1)

        b=Button(frame1, text ="Submit", command=self.makeReservation)
        b.grid(row=3,column=1,sticky=E)

    def makeReservation(self):
        start_date = datetime.strptime(self.startDateEntry.get(), '%m/%d/%Y')
        end_date = datetime.strptime(self.endDateEntry.get(), '%m/%d/%Y')
        if start_date > end_date or start_date < datetime.now():
            messagebox.showerror("Error", "Invalid Date (Either in the past or start > end)")
        else:
            self.findAvailWindow.withdraw()
            self.createResWindow.deiconify()

            frame = Frame(self.createResWindow)

            frame.pack()

            tree = self.getRoomTree(frame)

            chosenCity = self.cityVar.get()
            sql = "SELECT * FROM ROOM WHERE LOCATION = '%s' AND NOT EXISTS \
                    (SELECT Room_Number \
                    FROM RESERVATION_HAS_ROOM NATURAL JOIN RESERVATION \
                WHERE ROOM.Room_Number = RESERVATION_HAS_ROOM.Room_Number AND ROOM.LOCATION = RESERVATION_HAS_ROOM.LOCATION AND RESERVATION.Is_Cancelled = '0' AND (('%s' >= Start_Date \
                AND '%s' <= End_Date) OR ('%s' >= Start_Date AND '%s' <= End_Date) OR ('%s' >= Start_Date AND '%s' <= End_Date)))" % (chosenCity, start_date, end_date, start_date, start_date, end_date, end_date)
            print('Getting all rooms associated with city: %s' % (sql))
            db = self.Connect()
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            i = 0
            self.checkButtonsReserve = []
            for result in results:
                tree.insert('', i, text='', values=result)
                reserveButton = UserSelected(frame, text ="Room "+ str(result[0]), onvalue=1, offvalue=0)
                reserveButton.pack(side=LEFT)
                self.checkButtonsReserve.append(reserveButton)
                i += 1

            checkDetailsButton = Button(frame, text='Check Details', command=self.checkDetailsFunc)
            checkDetailsButton.pack(side=BOTTOM)

    def getRoomTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("r#",'loc',"costperday","#persons","rcat", "costextrabed")
        tree.heading("r#", text= "Room number")
        tree.heading("loc", text= "Location")
        tree.heading("costperday", text= "Cost Per Day")
        tree.heading("#persons", text= "#persons allowed")
        tree.heading("rcat", text= "Room category")
        tree.heading("costextrabed", text= "Cost of Extra Bed per day")
        return tree

    def checkDetailsFunc(self):
        self.createResWindow.withdraw()
        self.detWindow.deiconify()
        start_date = datetime.strptime(self.startDateEntry.get(), '%m/%d/%Y')
        end_date = datetime.strptime(self.endDateEntry.get(), '%m/%d/%Y')
        frame = Frame(self.detWindow)
        frame.pack()
        checkedRooms = [button.toString() for button in self.checkButtonsReserve if button.is_checked()]
        location = self.cityVar.get()
        db = self.Connect()
        cursor = db.cursor()
        tree = self.getRoomTree(frame)
        self.checkButtonsInDetails = []
        for room in checkedRooms:
            sqlToGetRoom = "SELECT * FROM ROOM WHERE Location = '%s' AND Room_Number = '%s'" % (location, int(room.split()[1]))
            print(sqlToGetRoom)
            cursor.execute(sqlToGetRoom)
            results = cursor.fetchall()
            i = 0
            for result in results:
                tree.insert('', i, text='', values=result)
                i += 1
                checkButton = UserSelected(frame, text ="Extra Bed For Room:"+ str(result[0]), onvalue=1, offvalue=0)
                checkButton.pack(side=TOP)
                checkButton.pickRoom(result)
                self.checkButtonsInDetails.append(checkButton)

        self.numDays = (end_date - start_date).days
        self.totalCostVarLabel = Label(frame,text ="Total Cost")
        self.checkDetailsFrame = frame

        CalculateCostButton = Button(frame, text='Calculate Cost', command=self.getCost)
        CalculateCostButton.pack(side=TOP)

        useCardLabel = Label(frame, text='Use Card')
        useCardLabel.pack(side=TOP)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM PAYMENT_INFORMATION WHERE Username='%s'" % (self.name))
        self.cardChoice = StringVar()
        choices = [card[0] for card in cursor.fetchall()]
        if len(choices) > 0:
            cardOption = OptionMenu(frame, self.cardChoice, choices[0], *choices)
            cardOption.pack(side=TOP)
        else:
            choices = []
            cardOption = OptionMenu(frame, self.cardChoice, '', *choices)
            cardOption.pack(side=TOP)

        AddCardButton = Button(frame, text='Add Card', command=self.addCard)
        DeleteCardButton = Button(frame, text='Delete Card', command=self.deleteCard)
        submitButton = Button(frame, text='Submit', command=self.processReservation)
        DeleteCardButton.pack(side=BOTTOM)
        AddCardButton.pack(side=BOTTOM)
        submitButton.pack(side=BOTTOM)


    def getCost(self):
        total = 0
        for button in self.checkButtonsInDetails:
            if button.is_checked():
                total += button.selectRoom()[5]
            total += button.selectRoom()[2]
        self.totalCost = total*self.numDays
        totallabel5 = Label(self.checkDetailsFrame, text=str(self.totalCost))
        self.totalCostVarLabel.pack(side=TOP)
        totallabel5.pack(side=TOP)

    def addCard(self):
        self.detWindow.withdraw()
        self.creditCardWin1.deiconify()
        self.creditCardWin1.title("Add Card")
        frame = Frame(self.creditCardWin1)
        frame.pack()
        frameButton = Frame(self.creditCardWin1)
        frameButton.pack()
        cardNameLabel = Label(frame, text="Name on Card")
        cardNumberLabel = Label(frame, text="Card Number")
        expirationDateLabel = Label(frame, text="Expiration Date (YYYY/MM/DD)")
        cvvLabel = Label(frame, text="CVV")

        cardNameLabel.grid(row = 0, column = 0,sticky=E)
        cardNumberLabel.grid(row = 1, column = 0,sticky=E)
        expirationDateLabel.grid(row = 2, column = 0,sticky=E)
        cvvLabel.grid(row = 3, column = 0,sticky=E)

        self.cardName= Entry(frame, textvariable = cardNameLabel, width=30)
        self.cardNumber= Entry(frame, textvariable = cardNumberLabel, width=30)
        self.expDate = Entry(frame, textvariable = expirationDateLabel, width=30)
        self.cvv = Entry(frame, textvariable = cvvLabel, width=30)

        self.cardName.grid(row=0, column=1)
        self.cardNumber.grid(row=1, column=1)
        self.expDate.grid(row=2, column=1)
        self.cvv.grid(row=3, column=1)

        saveButton=Button(frameButton, text="Save",  command=self.checkAddCardFunc)
        saveButton.pack(side=BOTTOM)

    def checkAddCardFunc(self):
        expDate = datetime.strptime(self.expDate.get(), '%Y/%m/%d')
        db = self.Connect()
        cursor=db.cursor()
        sql = "SELECT * FROM PAYMENT_INFORMATION \
               WHERE Card_Number = '%s'" % (self.cardNumber.get())
        cursor.execute(sql)
        results = cursor.fetchall()

        if len(results) != 0:
            messagebox.showerror("Error", "Card number already exists, choose different one")
        elif self.expDate.get() == "" or self.cardName.get() == "" or self.cardNumber.get() == "" or self.cvv.get() == "":
            messagebox.showerror("Error", "Fields cannot be empty")
        elif len(self.cardNumber.get()) != 10:
            messagebox.showerror("Error", "Please enter 10 digits for card number")
        elif len(self.cvv.get()) != 3:
            messagebox.showerror("Error", "Please enter 3 digits for CVV")
        elif expDate < datetime.now():
            messagebox.showerror("Error", "Invalid Expiration Date (In the past")
        else:
            db = self.Connect()
            cursor = db.cursor()
            sql = "INSERT INTO PAYMENT_INFORMATION(Card_Number, Name, Exp_Date, CVV, Username) \
            VALUES ('%s', '%s', '%s', '%s', '%s')" % (self.cardNumber.get(), self.cardName.get(), self.expDate.get(),self.cvv.get(), self.name)
            print(sql)
            cursor.execute(sql)
            self.switchtoCheckDetails()

    def switchtoCheckDetails(self):
        self.creditCardWin1.withdraw()
        self.detWindow.deiconify()

    def switchtoCheckDetails2(self):
        self.creditCardWin2.withdraw()
        self.detWindow.deiconify()

    def deleteCard(self):
        self.primaryWindow.withdraw()
        self.creditCardWin2.deiconify()
        self.creditCardWin2.title("Delete Card")
        frame = Frame(self.creditCardWin2)
        frame.pack()

        cardNumberLabel = Label(frame, text='Delete Card')
        cardNumberLabel.pack(side=TOP)
        db = self.Connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM PAYMENT_INFORMATION WHERE Username='%s'" % (self.name))
        self.cardChoice = StringVar()
        choices = [card[0] for card in cursor.fetchall()]
        if len(choices) > 0:
            cardOption = OptionMenu(frame, self.cardChoice, choices[0], *choices)
            cardOption.pack(side=TOP)
        else:
            choices = []
            cardOption = OptionMenu(frame, self.cardChoice, '', *choices)
            cardOption.pack(side=TOP)

        DeleteButton = Button(frame, text='Delete', command=self.deleteCardCheck)
        DeleteButton.pack(side=TOP)

    def deleteCardCheck(self):
        db = self.Connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM RESERVATION WHERE Card_Number ='%s'" %(self.cardChoice.get()))
        results = cursor.fetchall()

        for row in results:
            self.endDate = row[3]
            endDate = datetime.strptime(self.expDate.get(), '%Y/%m/%d')
            if endDate > datetime.now():
                messagebox.showerror("Error", "Cannot delete this card, being used for existing reservation")

        cursor = db.cursor()
        cursor.execute("DELETE FROM PAYMENT_INFORMATION WHERE Card_Number='%s'" % (self.cardChoice.get()))
        self.switchtoCheckDetails2()

    def processReservation(self):
        self.getCost()
        sqlToCheckDuplicate = "SELECT * FROM RESERVATION WHERE \
                                Username='%s' AND Card_Number='%s' AND Start_Date='%s'" % (self.name, self.cardChoice.get(), self.startDateEntry.get())
        db = self.Connect()
        cursor = db.cursor()
        cursor.execute(sqlToCheckDuplicate)
        if len(cursor.fetchall()) > 0:
            results = cursor.fetchall()
            for result in results:
                if result[4] == 0:
                    messagebox.showerror("Error", "Duplicate Reservation")
        else:
            sqlToGetids_from_user = "SELECT * FROM RESERVATION"
            cursor = db.cursor()
            cursor.execute(sqlToGetids_from_user)
            ids_from_user = set([])
            for result in cursor.fetchall():
                ids_from_user.add(result[0])
            self.rid = random.randint(12040, 13000)
            while self.rid in ids_from_user:
                self.rid = random.randint(12040, 13000)
            startDate = parser.parse(self.startDateEntry.get()).strftime('%Y/%m/%d')
            endDate = parser.parse(self.endDateEntry.get()).strftime('%Y/%m/%d')
            if len(self.cardChoice.get()) == 0:
                 messagebox.showerror("Error", "Card cannot be blank")
            else:
                insert_reservation = "INSERT INTO RESERVATION(ReservationID, \
                            Start_Date, Total, End_Date, Is_Cancelled, Username, Card_Number) \
                            VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (self.rid, startDate, self.totalCost, endDate,
                                                                                  str(0), self.name, self.cardChoice.get())
                cursor = db.cursor()
                cursor.execute(insert_reservation)
                for b in self.checkButtonsInDetails:
                    if b.is_checked():
                        roomNum = b.toString().split(':')[1]
                        sql = "INSERT INTO RESERVATION_HAS_ROOM(ReservationID, Room_Number, Location, Has_extra_bed) \
                        VALUES ('%s', '%s', '%s', 1)" % (self.rid, roomNum, self.cityVar.get())
                        print(sql)
                        cursor = db.cursor()
                        cursor.execute(sql)
                    else:
                        roomNum = b.toString().split(':')[1]
                        sql = "INSERT INTO RESERVATION_HAS_ROOM(ReservationID, Room_Number, Location, Has_extra_bed) \
                        VALUES ('%s', '%s', '%s', 0)" % (self.rid, roomNum, self.cityVar.get())
                        print(sql)
                        cursor = db.cursor()
                        cursor.execute(sql)
                self.switchToConfirmation()

    def cancelResv(self):
        self.primaryWindow.withdraw()
        self.putIDCancelWindow.deiconify()
        self.putIDCancelWindow.title("Cancel Reservation")
        frame = Frame(self.putIDCancelWindow)
        frame.pack()
        frameButton = Frame(self.putIDCancelWindow)
        frameButton.pack()

        label1 = Label(frame,text = "Reservation ID")
        label1.grid(row = 0, column = 0,sticky=E)
        self.reservIDStrCancel = StringVar()
        self.reservIDCancel = Entry(frame, textvariable = self.reservIDStrCancel, width = 30)
        self.reservIDCancel.grid(row = 0, column = 1)

        searchButton=Button(frameButton, text ="Search", command=self.checkReservCancel)
        searchButton.pack(side=RIGHT)

    def checkReservCancel(self):
        sql = "SELECT ReservationID FROM RESERVATION \
               WHERE Username = '%s' AND ReservationID = '%s' AND Is_Cancelled = '0'" % (self.name, self.reservIDStrCancel.get())
        db = self.Connect()
        cursor=db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            messagebox.showerror("Error", "ReservationID does not exist")
        else:
            self.putIDCancelWindow.withdraw()
            self.cancResWindow.deiconify()
            self.cancelRes3()

    def getCancelTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("r#",'rcat',"#persons","costperday", 'costExtraBed', "selectExtra")
        tree.heading("r#", text= "Room number")
        tree.heading("rcat", text= "Room category")
        tree.heading("#persons", text= "#persons allowed")
        tree.heading("costperday", text= "Cost Per Day")
        tree.heading("costExtraBed", text="Cost of Extra Bed")
        tree.heading("selectExtra", text= "Has Extra Bed")
        return tree

    def cancelRes3(self):
        self.cancResWindow.title("Cancel Reservation")
        frame = Frame(self.cancResWindow)
        frame.pack()
        frameButton = Frame(self.cancResWindow)
        frameButton.pack()
        sql = "UPDATE RESERVATION \
               SET Is_Cancelled = '1' WHERE ReservationID = '%s'" % (self.reservIDStrCancel.get())
        db = self.Connect()
        cursor=db.cursor()
        cursor.execute(sql)

        sql = "SELECT  Room_Number, Room_Category, Number_People, Cost_Day, Cost_of_Extra_Bed, Has_extra_bed, Start_Date, End_Date FROM (RESERVATION NATURAL JOIN RESERVATION_HAS_ROOM) NATURAL JOIN ROOM WHERE ReservationID = '%s'" % (self.reservIDStrCancel.get())
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        tree = self.getCancelTree(frame)
        i = 0
        startDate, endDate = None, None
        for result in results:
            tree.insert('', i, text='', values=result[:len(result) - 2])
            startDate, endDate = result[-2], result[-1]
            i += 1
        label1 = Label(frame, text="Start date:")
        label1.pack(side=TOP)
        label2 = Label(frame, text=startDate)
        label2.pack(side=TOP)
        label3 = Label(frame, text="End date:")
        label3.pack(side=TOP)
        label4 = Label(frame, text=endDate)
        label4.pack(side=TOP)

        sql = "SELECT Total from RESERVATION WHERE ReservationID='%s'" % (self.reservIDStrCancel.get())
        cursor = db.cursor()
        cursor.execute(sql)
        total = cursor.fetchone()[0]
        day_diff = (startDate - datetime.now().date()).days
        refund = total
        if day_diff <= 1:
            refund = 0
        elif day_diff <= 3:
            refund = total * 0.8
        label5 = Label(frame, text="Total Cost: " + str(total))
        label5.pack(side = TOP)
        label6 = Label(frame, text="Date of Cancellation: " + str(datetime.now()).split()[0])
        label6.pack(side=TOP)
        label7 = Label(frame, text="Refund Amount: " + str(refund))
        label7.pack(side=TOP)

        sql = "DELETE FROM RESERVATION_HAS_ROOM where ReservationID='%s'" % (self.reservIDStrCancel.get())
        cursor = db.cursor()
        cursor.execute(sql)

    def updateResv(self):
        self.primaryWindow.withdraw()
        self.updateResWindow.deiconify()
        self.updateResWindow.title("Update Reservation")
        frame = Frame(self.updateResWindow)
        frame.pack()
        frameButton = Frame(self.updateResWindow)
        frameButton.pack()

        label1 = Label(frame,text = "Reservation ID")
        label1.grid(row = 0, column = 0,sticky=E)
        self.reservIDStr = StringVar()
        self.reservID = Entry(frame, textvariable = self.reservIDStr, width = 30)
        self.reservID.grid(row = 0, column = 1)

        searchButton=Button(frameButton, text ="Search", command=self.checkReserv)
        searchButton.pack(side=RIGHT)


    def checkReserv(self):
        sql = "SELECT ReservationID FROM RESERVATION \
               WHERE Username = '%s' AND ReservationID = '%s' AND Is_Cancelled = '0'" % (self.name, self.reservIDStr.get())
        db = self.Connect()
        cursor=db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            messagebox.showerror("Error", "ReservationID does not exist")
        else:
            sql = "SELECT Start_Date FROM RESERVATION WHERE ReservationID = '%s'" % (self.reservIDStr.get())
            cursor = db.cursor()
            cursor.execute(sql)
            startDate = cursor.fetchone()[0]
            day_diff = (startDate - datetime.now().date()).days
            if day_diff < 0:
                messagebox.showerror('Error', 'Start Date in the past')
            elif day_diff <= 3:
                messagebox.showerror('Error', 'Cant update within 3 days')
            else:
                self.switchtoUpdateScreen()

    def switchtoUpdateScreen(self):
        self.updateResWindow.withdraw()
        self.insertDatWindows.deiconify()
        self.updateDate()

    def updateDate(self):
        self.insertDatWindows.title("Update Reservation")
        frame = Frame(self.insertDatWindows)
        frame.pack()
        frameButton = Frame(self.insertDatWindows)
        frameButton.pack()
        sql = "SELECT * FROM RESERVATION \
               WHERE Username = '%s' AND ReservationID = '%s'" % (self.name, self.reservIDStr.get())
        db = self.Connect()
        cursor=db.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        start = result[1]
        end = result[3]

        label1 = Label(frame, text="Current start date:")
        label1.grid(row = 0, column = 0,sticky=E)
        label2 = Label(frame, text=start)
        label2.grid(row = 0, column = 1,sticky=E)
        label3 = Label(frame, text="Current end date:")
        label3.grid(row = 1, column = 0,sticky=E)
        label4 = Label(frame, text=end)
        label4.grid(row = 1, column = 1,sticky=E)
        newStart = Label(frame, text="New start date (MM/DD/YYYY):")
        newStart.grid(row = 2, column = 0,sticky=E)
        self.newStartString = StringVar()
        self.newDateS = Entry(frame, textvariable = self.newStartString, width = 15)
        self.newDateS.grid(row = 2, column = 1)
        newEnd = Label(frame, text="New end date (MM/DD/YYYY):")
        newEnd.grid(row = 3, column = 0,sticky=E)
        self.newEndString = StringVar()
        self.newDateE = Entry(frame, textvariable = self.newEndString, width = 15)
        self.newDateE.grid(row = 3, column = 1)

        searchButton=Button(frameButton, text ="Search Availibility", command=self.checkNewDates)
        searchButton.pack(side=RIGHT)

    def checkNewDates(self):
        db = self.Connect()
        if self.newDateS.get() == '' or self.newDateE.get() == '':
            messagebox.showerror('Error', 'Cannot leave fields blank')
        else:
            self.insertDatWindows.withdraw()
            self.finalDatesWindow.deiconify()
            frame = Frame(self.finalDatesWindow)
            frame.pack()
            start_date = datetime.strptime(self.newDateS.get(), '%m/%d/%Y')
            end_date = datetime.strptime(self.newDateE.get(), '%m/%d/%Y')
            changedStartDate = parser.parse(self.newDateS.get()).strftime('%Y/%m/%d')
            changedEndDate = parser.parse(self.newDateE.get()).strftime('%Y/%m/%d')
            if start_date > end_date or start_date < datetime.now():
                messagebox.showerror("Error", "Invalid Date (Either the dates are in the past or the start date is after the end date)")
            sql = "SELECT Room_Number, Location FROM RESERVATION NATURAL JOIN RESERVATION_HAS_ROOM where ReservationID='%s'" % (self.reservIDStr.get())
            cursor = db.cursor()
            cursor.execute(sql)

            results = cursor.fetchall()
            toDisplay = True
            for result in results:
                sql = "SELECT * FROM RESERVATION_HAS_ROOM NATURAL JOIN RESERVATION where Room_Number = '%s' AND Location = '%s' AND \
                (('%s' >= Start_Date AND '%s' <= End_Date) OR ('%s' >= Start_Date AND '%s' <= End_Date) \
                 OR ('%s' >= Start_Date AND '%s' <= End_Date))" % (result[0], result[1], changedStartDate, changedEndDate, changedStartDate, changedStartDate, changedEndDate, changedEndDate)
                cursor = db.cursor()
                cursor.execute(sql)
                allRooms = cursor.fetchall()
                if len(allRooms) != 0:
                    toDisplay = False

            if toDisplay:
                tree = self.getCancelTree(frame)
                sql = "SELECT Room_Number, Room_Category, Number_People, Cost_Day, Cost_of_Extra_Bed, Has_extra_bed FROM (RESERVATION NATURAL JOIN RESERVATION_HAS_ROOM) NATURAL JOIN ROOM WHERE ReservationID = '%s'" % (self.reservIDStr.get())
                cursor = db.cursor()
                cursor.execute(sql)
                results = cursor.fetchall()
                cost = 0
                i = 0
                for result in results:
                    if result[5] == 1:
                        cost += result[4]
                    cost += result[3]
                    tree.insert('', i, text='', values=result)
                    i += 1
                cost *= (end_date - start_date).days
                updatedCost = Label(frame, text="Total Cost Updated: " + str(cost))
                updatedCost.pack(side = TOP)
                sql = "UPDATE RESERVATION SET Start_Date='%s', End_Date='%s', Total='%s' where ReservationID='%s'" % (changedStartDate, changedEndDate, cost, self.reservIDStr.get())
                cursor = db.cursor()
                cursor.execute(sql)
            else:
                messagebox.showerror('Error', 'All booked up')

    def switchToConfirmation(self):
        self.detWindow.withdraw()
        self.finalResWindow.deiconify()
        self.finalResWindow.title("Confirm Reservation")
        frame = Frame(self.finalResWindow)
        frame.pack()
        frameButton = Frame(self.finalResWindow)
        frameButton.pack()
        label1 = Label(frame, text="Your Reservation ID:")
        label1.grid(row = 0, column = 0,sticky=E)
        label2 = Label(frame, text=self.rid)
        label2.grid(row = 1, column = 0,sticky=E)
        label3 = Label(frame, text="Please save this reservation id")
        label3.grid(row = 2, column = 0,sticky=E)
        b=Button(frame, text ="Back", command=self.backtoMainScreen)
        b.grid(row=3,column=1,sticky=E)

    def backtoMainScreen(self):
        self.finalResWindow.withdraw()
        self.primaryWindow.deiconify()

    def reservationTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("Month",'Location',"Total number of reservations")
        tree.heading("Month", text= "Month")
        tree.heading("Location", text= "Location")
        tree.heading("Total number of reservations", text= "Total number of reservations")
        return tree

    def popTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("Month",'Top Room-Category','Location',"Total number of reservations for room category")
        tree.heading("Month", text= "Month")
        tree.heading("Top Room-Category", text = "Top Room-Category")
        tree.heading("Location", text= "Location")
        tree.heading("Total number of reservations for room category", text= "Total number of reservations for room category")
        return tree

    def revenueTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("Month",'Location',"Total revenue")
        tree.heading("Month", text= "Month")
        tree.heading("Location", text= "Location")
        tree.heading("Total revenue", text= "Total revenue")
        return tree

    def viewReport(self):
        self.primaryWindow.withdraw()
        self.seeRepWindow.deiconify()
        self.seeRepWindow.title("Reservation Report")
        frame = Frame(self.seeRepWindow)
        frame.pack()
        tree=self.reservationTree(frame)
        db = self.Connect()
        cursor = db.cursor()
        sql = "SELECT MONTH(Start_Date), Location, COUNT(Location)\
                FROM RESERVATION_HAS_ROOM NATURAL JOIN RESERVATION  WHERE Month(Start_Date) LIKE '8' OR Month(Start_Date) LIKE '9' GROUP BY  MONTH(Start_Date), Location"
        cursor.execute(sql)
        locations = ['Atlanta', 'Savannah', 'Orlando', 'Miami','Charlotte']
        finalReportDict = OrderedDict()
        results = cursor.fetchall()
        for result in results:
            month, city, numReservations = result
            monthName = calendar.month_name[month]
            if not finalReportDict.get(monthName):
                finalReportDict[monthName] = {location:{'count' : 0} for location in locations}
            finalReportDict[monthName][city] = {'count' : numReservations}
        i = 0
        for monthName, cityDict in finalReportDict.items():
            for city, countDict in cityDict.items():
                count = countDict['count']
                if i % 5 == 0:
                    tree.insert('',i,text='',values=(monthName, city, count))
                else:
                    tree.insert('',i,text='',values=('', city, count))
                i += 1
    def viewPopReport(self):
        self.primaryWindow.withdraw()
        self.popResReportWindow.deiconify()
        self.popResReportWindow.title("Popular Room-Category")
        frame = Frame(self.popResReportWindow)
        frame.pack()
        tree=self.popTree(frame)
        db = self.Connect()
        sql = "SELECT t.currMonth, MAX(t.Room_Category), MAX(t.Location), MAX(t.room_count) \
                FROM (SELECT MONTH(Start_Date) AS currMonth, Room_Category, Location, COUNT(Room_Category) AS \
                room_count FROM (RESERVATION NATURAL JOIN RESERVATION_HAS_ROOM) NATURAL JOIN ROOM  WHERE Month(Start_Date) LIKE '8' OR Month(Start_Date) LIKE '9' GROUP BY MONTH(Start_Date),\
                Room_Category, Location) AS t GROUP BY currMonth, Location"
        locations = ['Atlanta', 'Savannah', 'Orlando', 'Miami','Charlotte']
        finalReportDict = OrderedDict()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            monthName = calendar.month_name[result[0]]
            category, city, count = result[1:]
            if not finalReportDict.get(monthName):
                finalReportDict[monthName] = {location:{'category': 'SUITE', 'count' : 0} for location in locations}
            finalReportDict[monthName][city] = {'category': category, 'count': count}
        i = 0
        for monthName, cityDict in finalReportDict.items():
            for city, roomDict in cityDict.items():
                category, count = roomDict['category'], roomDict['count']
                if i % 5 == 0:
                    tree.insert('',i,text='',values=(monthName, category, city, count))
                else:
                    tree.insert('',i,text='',values=('', category, city, count))
                i += 1
    def viewRevenue(self):
        self.primaryWindow.withdraw()
        self.seeReportWindow.deiconify()
        self.seeReportWindow.title("Revenue Report")
        frame = Frame(self.seeReportWindow)
        frame.pack()
        tree = self.revenueTree(frame)
        db = self.Connect()
        cursor = db.cursor()
        finalReportDict = OrderedDict()
        sql = "SELECT Month(Start_Date), Location, SUM(Total) FROM RESERVATION_HAS_ROOM NATURAL JOIN RESERVATION \
         WHERE Month(Start_Date) LIKE '8' OR Month(Start_Date) LIKE '9' GROUP BY Location, MONTH(Start_Date) order by Month(Start_date)"
        cursor.execute(sql)
        results = cursor.fetchall()
        locations = ['Atlanta', 'Savannah', 'Orlando', 'Miami','Charlotte']
        for result in results:
            month, city, total = result
            monthName = calendar.month_name[month]
            if not finalReportDict.get(monthName):
                finalReportDict[monthName] = {location:{'sum' : 0} for location in locations}
            finalReportDict[monthName][city] = {'sum' : total}
        i = 0
        for monthName, cityDict in finalReportDict.items():
            for city, countDict in cityDict.items():
                count = countDict['sum']
                if i % 5 == 0:
                    tree.insert('',i,text='',values=(monthName, city, count))
                else:
                    tree.insert('',i,text='',values=('', city, count))
                i += 1
    def provideFB(self):
        self.primaryWindow.withdraw()
        self.provideReviewWindow.deiconify()
        frame = Frame(self.provideReviewWindow)
        frame.pack()

        self.feedbackVar = StringVar()
        choices = [ "Excellent", "Good", "Bad", "Very Bad", "Neutral"]
        self.feedbackVar.set(choices[0])
        option = OptionMenu(frame, self.feedbackVar, choices[0], *choices)
        option.grid(row = 1, column = 2)
        ratingLabel = Label(frame, text = "Rating")
        ratingLabel.grid(row = 1, column = 1)
        self.cityVar = StringVar()
        choices = [ "Atlanta", "Charlotte", "Savannah", "Orlando", "Miami"]
        self.cityVar.set(choices[0])
        option2=OptionMenu(frame, self.cityVar, choices[0], *choices)
        option2.grid(row=0,column=2)
        locationLabel = Label(frame, text = "Hotel Location")
        locationLabel.grid(row = 0, column = 1)
        commentLabel = Label(frame, text = "Comment")
        commentLabel.grid(row = 2, column = 1)
        self.comment= StringVar()
        self.commentEntry = Entry(frame, textvariable = self.comment, width = 30)
        self.commentEntry.grid(row = 2, column = 2)
        submitButton = Button(frame, text='Submit', command=self.submitRev)
        submitButton.grid(row = 3, column = 4)



    def submitRev(self):
        frame = Frame(self.tyWindow)
        frame.pack()
        ThanksLabel = Label(frame, text = "Thank you for your feedback. Please stay with us again.")
        ThanksLabel.grid(row = 1, column = 1)
        contButton = Button(frame, text = "Continue", command = self.backtoMain)
        contButton.grid(row = 2, column = 2)


        sql2 = "SELECT COUNT(Review_Number) FROM HOTEL_REVIEW"

        db = self.Connect()

        cursor = db.cursor()
        cursor.execute(sql2)
        count = cursor.fetchone()[0]
        sql = "INSERT INTO HOTEL_REVIEW ( Review_Number, Comment, Rating, Location, Username)\
                      VALUES ('%s','%s', '%s', '%s', '%s')" % ( count + 1, self.commentEntry.get(), self.feedbackVar.get(),self.cityVar.get(), self.name)
        cursor.execute(sql)
        self.provideReviewWindow.withdraw()
        self.tyWindow.deiconify()

    def backtoMain(self):
        self.tyWindow.withdraw()
        self.primaryWindow.deiconify()
    def viewFB(self):
        self.primaryWindow.withdraw()
        self.seeRevWindow.deiconify()
        frame = Frame(self.seeRevWindow)
        frame.pack()
        self.cityVar = StringVar()
        choices = [ "Atlanta", "Charlotte", "Savannah", "Orlando", "Miami"]
        self.cityVar.set(choices[0])
        option2=OptionMenu(frame, self.cityVar, choices[0], *choices)
        option2.grid(row=0,column=2)
        locationLabel = Label(frame, text = "Hotel Location")
        locationLabel.grid(row = 0, column = 1)
        CheckRevButton = Button(frame, text = "Check Reviews", command = self.checkRev)
        CheckRevButton.grid(row = 1, column = 3)

    def checkRev(self):
        sql = "SELECT Rating,Comment FROM HOTEL_REVIEW WHERE Location = '%s'" %self.cityVar.get()
        db = self.Connect()
        cursor = db.cursor()
        cursor.execute(sql)
        comments = cursor.fetchall()
        frame2 = Frame(self.seeRevWindow)
        frame2.pack()
        tree=Treeview(frame2)
        tree.pack()
        tree["columns"]=("Rating",'Comments')
        tree.heading("Rating", text= "Rating")
        tree.heading("Comments", text= "Comments")
        numofrev = len(comments)
        alist = list(range(0,numofrev))
        for x in alist:
            tree.insert("",x, text = "Review_"+ str(x), values = (comments[x][0],comments[x][1]))

        GoBackButton = Button(frame2, text = "Go Back to Main Menu", command = self.BacktoMainmenu)
        GoBackButton.pack()
        return tree

    def BacktoMainmenu(self):
        self.seeRevWindow.withdraw()
        self.primaryWindow.deiconify()



mw = Tk()
app = Part_Three(mw)
mw.mainloop()
