#Arthi Nithi, Anjani Agrawal, Alan Chiang, Alaap Murali

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pymysql
import calendar
import datetime
from math import *
import time
class Phase_three:
    def __init__(self,primaryWin):
        self.primaryWin = primaryWin
        self.Login()
        self.results1 = []
        self.entrys=[]
        self.newUserWindow = Toplevel()
        #self.Register()
        self.newUserWindow.title("New User Registration")
        self.newUserWindow.withdraw()

        self.primaryWindow = Toplevel()
        self.primaryWindow.title("Welcome "+self.username.get())
        self.primaryWindow.withdraw()

        self.schoolInfoWin= Toplevel()
        self.schoolInfoWin.title("Add School Info")
        self.schoolInfoWin.withdraw()

        self.trainSchWin= Toplevel()
        self.trainSchWin.title("View Train Schedule")
        self.trainSchWin.withdraw()

        self.scheduleWin= Toplevel()
        self.scheduleWin.title("View Train Schedule")
        self.scheduleWin.withdraw()

        self.findAvailWindow= Toplevel()
        self.findAvailWindow.title("Search Train")
        self.findAvailWindow.withdraw()

        self.departureWin = Toplevel()
        self.departureWin.title("Select Departure")
        self.departureWin.withdraw()

        self.passengerInfoWin = Toplevel()
        self.passengerInfoWin.title("Travel Extras & Passenger Info")
        self.passengerInfoWin.withdraw()

        self.reservationWin = Toplevel()
        self.reservationWin.title("Make Reservation")
        self.reservationWin.withdraw()

        self.paymentIWin = Toplevel()
        self.paymentIWin.title("Add Card")
        self.paymentIWin.withdraw()

        self.paymentIWin2 = Toplevel()
        self.paymentIWin2.title("Delete Card")
        self.paymentIWin2.withdraw()

        self.confirm = Toplevel()
        self.confirm.title("Confirmation")
        self.confirm.withdraw()

        self.updateWin = Toplevel()
        self.updateWin.title("Update Reservation")
        self.updateWin.withdraw()

        self.updateWin2 = Toplevel()
        self.updateWin2.title("Update Reservation")
        self.updateWin2.withdraw()

        self.updateWin3 = Toplevel()
        self.updateWin3.title("Update Reservation")
        self.updateWin3.withdraw()

        self.cancelWin = Toplevel()
        self.cancelWin.title("Cancel Reservation")
        self.cancelWin.withdraw()

        self.cancelWin2 = Toplevel()
        self.cancelWin2.title("Cancel Reservation")
        self.cancelWin2.withdraw()

        self.viewReviewWin = Toplevel()
        self.viewReviewWin.title("View review")
        self.viewReviewWin.withdraw()

        self.viewReviewWin2 = Toplevel()
        self.viewReviewWin2.title("View review")
        self.viewReviewWin2.withdraw()

        self.giveReviewWin = Toplevel()
        self.giveReviewWin.title("Give Review")
        self.giveReviewWin.withdraw()

        self.viewRevenueReport = Toplevel()
        self.viewRevenueReport.title("View Revenue Report")
        self.viewRevenueReport.withdraw()

        self.viewpopRRWin = Toplevel()
        self.viewpopRRWin.title("View Popular Route Report")
        self.viewpopRRWin.withdraw()

    def Connect(self):
        try:
            db = pymysql.connect(host="academic-mysql.cc.gatech.edu",  user="cs4400_Team_48", passwd="dwet2rPC",db="cs4400_Team_48")
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
        b2=Button(frame2, text ="Register", command= self.switchToRegister)
        b2.pack(side=LEFT)

    def loginCredentials(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Invalid input")
            return

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT Username FROM CUSTOMER \
               WHERE (CUSTOMER.Username = '%s' AND (SELECT Password FROM USER WHERE CUSTOMER.Username = USER.Username) = '%s')" % (self.username.get(), self.password.get())
        cursor.execute(query)
        result1 = cursor.fetchall()
        query = "SELECT Username FROM MANAGER \
               WHERE (MANAGER.Username = '%s' AND (SELECT Password FROM USER WHERE MANAGER.Username = USER.Username) = '%s')" % (self.username.get(), self.password.get())

        cursor.execute(query)
        result2 = cursor.fetchall()

        if len(result1) != 0:
            self.custOrManag = "customer"
            for row in result1:
                self.name = row[0]
            self.switchtoMainMenu()
        elif len(result2) != 0:
            self.custOrManag = "manager"
            for row in result2:
                self.name = row[0]
            self.switchtoMainMenu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def mainMenu(self):
        self.primaryWindow = Toplevel()
        self.primaryWindow.title("Choose Functionality ")
        buttonsFrame = Frame(self.primaryWindow)
        buttonsFrame.pack()
        if self.custOrManag == "customer":
            b1 = Button(buttonsFrame, text ="View Train Schedule", command = self.trainSchedule)
            b1.grid(row = 0, column = 0, columnspan = 2, sticky = EW)
            b2 = Button(buttonsFrame, text ="Make a new reservation", command = self.searchTrain)
            b2.grid(row = 1, column = 0, columnspan = 2, sticky = EW)
            b3 = Button(buttonsFrame, text ="Update a reservation", command = self.updateReservation)
            b3.grid(row = 2, column = 0, columnspan = 2, sticky = EW)
            b4 = Button(buttonsFrame, text ="Cancel a reservation", command = self.cancelRes)
            b4.grid(row = 3, column = 0, columnspan = 2, sticky = EW)
            b5 = Button(buttonsFrame, text ="Give review", command = self.giveReview)
            b5.grid(row = 4, column = 0, columnspan = 2, sticky = EW)
            b6 = Button(buttonsFrame, text ="Add school information (student discount)", command = self.schoolInfo)
            b6.grid(row = 5, column = 0, columnspan = 2, sticky = EW)
            b7 = Button(buttonsFrame, text ="Log out", command = self.logout)
            b7.grid(row = 6, column = 0, columnspan = 2, sticky = EW)
        elif self.custOrManag == "manager":
            b8 = Button(buttonsFrame, text ="View revenue report", command = self.viewRevenueRep)
            b8.grid(row = 0, column = 0, columnspan = 2, sticky = EW)
            b9 = Button(buttonsFrame, text ="View popular route report", command = self.viewpopRR)
            b9.grid(row = 1, column = 0, columnspan = 2, sticky = EW)
            b10=Button(buttonsFrame, text ="Log out", command = self.logout)
            b10.grid(row = 2, column = 0, columnspan = 2, sticky = EW)

    def switchToRegister(self):
        self.primaryWin.withdraw()
        self.newUserWindow.deiconify()
        self.Register()
        #self.primaryWin.withdraw()

    def switchToLogin(self):
        self.newUserWindow.withdraw()
        self.primaryWin.deiconify()

    def switchtoMainMenu(self):
        self.primaryWin.withdraw()
        #self.primaryWindow.deiconify()
        self.mainMenu()

    def Register(self):
        self.newUserWindow.title("New User Registration")
        frame=Frame(self.newUserWindow)
        frame.pack()
        frame2=Frame(self.newUserWindow)
        frame2.pack(side = BOTTOM)

        label1 = Label(frame,text = "Username", justify = LEFT)
        label1.grid(row = 0, column = 0, sticky = W)
        self.registeredUser = StringVar()
        self.uentry = Entry(frame, textvariable = self.registeredUser, width = 30, justify = RIGHT)
        self.uentry.grid(row = 0, column = 1, sticky = W)

        label2 = Label(frame,text ="Email Address", justify = LEFT)
        label2.grid(row = 1, column = 0, sticky = W)
        self.registerEmail = StringVar()
        self.email_entry = Entry(frame, textvariable = self.registerEmail, width = 30, justify = RIGHT)
        self.email_entry.grid(row = 1, column = 1, sticky = W)

        label3 = Label(frame,text = "Password", justify = LEFT)
        label3.grid(row = 2, column = 0, sticky = W)
        self.registeredPass = StringVar()
        self.password_entry = Entry(frame, textvariable = self.registeredPass, width = 30, justify = RIGHT)
        self.password_entry.grid(row = 2, column = 1, sticky = W)

        label4 = Label(frame,text ="Confirm Password", justify = LEFT)
        label4.grid(row = 3, column = 0, sticky = W)
        self.registeredPassConfirm = StringVar()
        self.confirm_password_entry = Entry(frame, textvariable = self.registeredPassConfirm, width = 30, justify = RIGHT)
        self.confirm_password_entry.grid(row = 3, column = 1, sticky = W)

        b_reg=Button(frame2, text ="Create", command = self.registerCredentials)
        b_reg.pack(side = BOTTOM)

    def registerCredentials(self):
        if self.registeredUser.get() == "" or self.registeredPass.get() == "" or self.registeredPassConfirm.get() == "" or self.registerEmail.get() == "":
            messagebox.showerror("Error", "Invalid input")
            return

        if self.registeredPass.get() != self.registeredPassConfirm.get():
            messagebox.showerror("Error", "Passwords must match")
            return

        db = self.Connect()
        cursor = db.cursor()
        query1 = "SELECT * FROM USER \
               WHERE USER.Username = '%s'" % (self.registeredUser.get())

        cursor.execute(query1)
        result1 = cursor.fetchall()


        if len(result1) != 0:
            messagebox.showerror("Error", "Username already in use")
            return

        querypatch = "INSERT INTO USER(Username, Password) VALUES ('%s' , '%s')" % (self.registeredUser.get(), self.registeredPass.get())
        cursor.execute(querypatch)
        result3 = cursor.fetchall()

        query2 = "INSERT INTO CUSTOMER(Username, Email) \
            VALUES ('%s', '%s')" % (self.registeredUser.get(), self.registerEmail.get())
        cursor.execute(query2)
        result2 = cursor.fetchall()

        cursor.close()
        db.commit()
        db.close()
        self.switchToLogin()

    def schoolInfo(self):
        self.primaryWindow.destroy()
        self.schoolInfoWin = Toplevel()
        self.schoolInfoWin.title("Add School Info")
        frame1 = Frame(self.schoolInfoWin)
        frame2 = Frame(self.schoolInfoWin)
        frame1.pack(side = TOP)
        frame2.pack(side = BOTTOM)
        self.emailaddress = StringVar()
        self.entry = Entry(frame1, textvariable = self.emailaddress, width = 30)
        self.entry.grid(row = 0, column = 1)
        label1 = Label(frame1,text = "School Email Address")
        label1.grid(row = 0, column = 0)
        label2 = Label(frame1,text = "Your school email adress ends with .edu")
        label2.grid(row = 1, column = 0)

        b1 = Button(frame2, text ="Back", command = self.sMAINMENU)
        b1.grid(row = 2, column = 0)
        b2 = Button(frame2, text ="Submit", command = self.writeToDB)
        b2.grid(row = 2, column = 1)

    def writeToDB(self):
        server = self.Connect()
        cursor = server.cursor()
        query = "UPDATE CUSTOMER SET Email = '%s' WHERE Username = '%s'" % (self.emailaddress.get(),self.username.get())
        cursor.execute(query)
        if self.emailaddress.get()[-4:] == ".edu":
            query = "UPDATE CUSTOMER SET Is_student = 1 WHERE Username = '%s'" % (self.username.get())
            cursor.execute(query)
        server.commit()
        cursor.close()
        server.close()

        self.schoolInfoWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def logout(self):
        self.primaryWindow.destroy()
        self.primaryWin = Toplevel()
        self.Login()

    def sMAINMENU(self):
        self.schoolInfoWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def trainSchedule(self):
        self.primaryWindow.destroy()
        self.trainSchWin = Toplevel()
        self.trainSchWin.title("View Train Schedule")
        frame1 = Frame(self.trainSchWin)
        frame2 = Frame(self.trainSchWin)
        frame1.pack(side = TOP)
        frame2.pack(side = BOTTOM)
        label1 = Label(frame1,text = "Train Number")
        label1.pack(side=LEFT)

        self.trainNumber = IntVar()
        self.entry = Entry(frame1, textvariable = self.trainNumber, width = 10)
        self.entry.pack(side=RIGHT)

        b1 = Button(frame2, text ="Search", command = self.schedule)
        b1.pack(side=LEFT)

    def getTrainTree(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["show"] = "headings"
        tree["columns"]=("train","arrv","dept","stat")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("arrv", text= "Arrival Time")
        tree.heading("dept", text= "Departure Time")
        tree.heading("stat", text= "Station")
        return tree

    def schedule(self):
        self.trainSchWin.destroy()
        self.scheduleWin = Toplevel()
        self.scheduleWin.title("View Train Schedule")

        frame1 = Frame(self.scheduleWin)
        frame1.pack()

        tree = self.getTrainTree(frame1)
        server = self.Connect()
        cursor = server.cursor()

        trainNum = self.trainNumber.get()
        query1 = "SELECT * FROM STOP WHERE Train_Number = '%d'" % (trainNum)

        cursor.execute(query1)
        results = cursor.fetchall()
        i = 0
        for result in results:
            tree.insert('', i, text='', values=(result[2], result[0],result[1], result[3]))
            i += 1

        b1 = Button(frame1, text ="Back", command = self.switchToMainMenu)
        b1.pack(side= BOTTOM)

    def switchToMainMenu(self):
        self.scheduleWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def searchTrain(self):
        self.primaryWindow.withdraw()
        self.findAvailWindow = Toplevel()

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
        location.grid(row = 0, column = 0, sticky = E)
        self.city = StringVar()

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT Name FROM STATION"
        cursor.execute(query)
        results = cursor.fetchall()

        option=OptionMenu(frame, self.city, results[0], *results)
        option.grid(row = 0, column = 1, sticky = W)

        arriveAt= Label(frame1,text ="Arrive At")
        arriveAt.grid(row = 1, column = 0, sticky = E)
        self.arrv = StringVar()

        option=OptionMenu(frame1, self.arrv, results[0], *results)
        option.grid(row = 1, column = 1, sticky = W)

        depDate= Label(frame2,text ="Departure Date (YYYY-MM-DD)")
        depDate.grid(row = 2, column = 0, sticky = E)
        self.date = StringVar()

        self.startDateEntry = Entry(frame2, textvariable = self.date, width = 10)
        self.startDateEntry.grid(row = 2, column = 1, sticky = W)

        b=Button(frame3, text ="Find Trains", command = self.departureInfo)
        b.pack(side=RIGHT)

    def selected(self):
        if self.v.get() %2 == 0:
            self.value  = (floor(self.v.get()/2)) -1
        else:
            self.value  = (floor(self.v.get()/2))

    def departureInfo(self):
        start_date = datetime.strptime(self.startDateEntry.get(), '%Y-%m-%d')
        if start_date < datetime.now():
            messagebox.showerror("Error", "Invalid Date (Either in the past or start > end)")
        else:
            self.findAvailWindow.withdraw()
            self.departureWin = Toplevel()
            self.departureWin.title("Select Departure")

            frame = Frame(self.departureWin)
            frame.pack(side=TOP)

            chosenCity = self.city.get()[2: len(self.city.get())-3]
            chosenArrv = self.arrv.get()[2: len(self.arrv.get())-3]
            chosenDate = self.date.get()

            server = self.Connect()
            cursor = server.cursor()

            stop1 = "CREATE VIEW Stop1 (Train_Number) AS SELECT Train_Number FROM STOP WHERE STOP.Name = '%s'" % (chosenCity)
            stop2 = "CREATE VIEW Stop2 (Train_Number) AS SELECT Train_Number FROM STOP WHERE STOP.Name = '%s'" % (chosenArrv)
            stops = "CREATE VIEW Stops (Train_Number) AS SELECT Train_Number FROM Stop2 NATURAL JOIN Stop1"
            query = "SELECT STOP.Train_Number, STOP.Departure_Time, STOP.Arrival_Time, STOP.Name, TRAIN_ROUTE.First_Class_Price, TRAIN_ROUTE.Second_Class_Price FROM STOP, TRAIN_ROUTE, Stops \
            WHERE (STOP.Train_Number = Stops.Train_Number) AND (TRAIN_ROUTE.Train_Number = Stops.Train_Number) AND (STOP.Name = '%s' OR STOP.Name = '%s')" % (chosenCity, chosenArrv)

            cursor.execute(query)
            results = cursor.fetchall()

            departTime = []
            arriveTime = []

            for row in results:
                if str(row[3]) == chosenCity:
                    departTime.append((row[1], row[3], row[0], row[4], row[5]))
                if str(row[3]) == chosenArrv:
                    arriveTime.append((row[2], row[3], row[0], row[4], row[5]))
            self.duration = []
            for pair1 in departTime:
                for pair2 in arriveTime:
                    if pair1[1] == chosenCity and pair2[1] == chosenArrv and pair1[2] == pair2[2]:
                        self.duration.append((pair1[2],pair1[0],pair2[0],pair2[0] - pair1[0],pair1[3],pair1[4], pair1[1], pair2[1]))
                        # 0: Train_Number, 1: Departure_Time, 2: Arrival_Time, 3: Duration, 4: First_Class_Price, 5: Second_Class_Price, 6: chosenCity, 7: chosenArrv

            l1 = Label(frame,text = "Train(Train Number)").grid(row = 0, column = 0)
            l2 = Label(frame,text = "Time(self.Duration)").grid(row = 0, column = 2)
            l3 = Label(frame,text = "1st Class Price").grid(row = 0, column = 4)
            l4 = Label(frame,text = "2nd Class Price").grid(row = 0, column = 6)

            a = 1
            b = 1
            c = 2
            self.v = IntVar()
            for result in self.duration:
                Label(frame, text = str(result[0]), anchor = "w").grid(row = a, column = 0, sticky = "ew")
                Label(frame, text = str(result[1]) + "-" + str(result[2]) + "\n" + str(result[3]), anchor = "w").grid(row = a, column = 2, sticky = "ew")
                Radiobutton(frame, text = str(result[4]), variable = self.v, value = b, command = self.selected).grid(row = a, column = 4, sticky = "ew")
                Radiobutton(frame, text = str(result[5]), variable = self.v, value = c, command = self.selected).grid(row = a, column = 6, sticky = "ew")
                a += 1
                b += 2
                c += 2

            self.row = a
            self.value1 = b
            self.value2 = c

            b1=Button(frame, text ="Back", command = self.switchtoSearchTrain)
            b1.grid(row = a, column = 0)
            b2=Button(frame, text ="Next", command = self.passengerInfo)
            b2.grid(row = a, column = 1)

    def switchtoSearchTrain(self):
        self.departureWin.destroy()
        self.findAvailWindow.deiconify()

    def passengerInfo(self):
        self.departureWin.withdraw()
        self.passengerInfoWin = Toplevel()
        self.passengerInfoWin.title("Travel Extras & Passenger Info")

        frame = Frame(self.passengerInfoWin)
        frame.pack(side=TOP)
        frame2 = Frame(self.passengerInfoWin)
        frame2.pack(side=TOP)
        frame3 = Frame(self.passengerInfoWin)
        frame3.pack(side=TOP)
        frame4 = Frame(self.passengerInfoWin)
        frame4.pack(side=TOP)

        baggage= Label(frame,text = "Number of Baggage")
        baggage.pack(side=LEFT)
        self.bags = IntVar()
        choices = ["1", "2", "3", "4"]
        option=OptionMenu(frame, self.bags, choices[0], *choices)
        option.pack(side=RIGHT)
        disclamer = Label(frame2,text = "Every passenger can bring upto 4 baggage. 2 free of charge, 2 for $30 per bag")
        disclamer.pack()

        passName= Label(frame3,text ="Passenger Name")
        passName.pack(side=LEFT)
        self.name2 = StringVar()
        nameEnt = Entry(frame3, textvariable = self.name2, width = 10)
        nameEnt.pack(side = RIGHT)

        if self.v.get() % 2 == 0:
            self.classChosen = 2
        else:
            self.classChosen = 1

        b1=Button(frame4, text ="Back", command = self.switchToDepartureInfo)
        b1.pack(side=LEFT)
        b2=Button(frame4, text ="Next", command=self.updateTrainList)
        b2.pack(side=RIGHT)

    def switchToDepartureInfo(self):
        self.passengerInfoWin.destroy()
        self.departureWin.deiconify()

    def updateTrainList(self):
        price = 0
        if self.bags.get() < 3:
            bagPrice = 0
        else:
            extraBags = self.bags.get() - 2
            bagPrice = extraBags * 30
        if self.v.get()%2 == 0: #(if even 2nd class)
            self.chosenClass = 2
            price = self.duration[self.value][5]
        else:
            self.chosenClass = 1
            price = self.duration[self.value][4]

        self.price = StringVar()
        self.price = price + bagPrice
        self.trainChosen = self.duration[self.value][0]
        self.results1.append((self.trainChosen, self.duration[self.value][1], self.duration[self.value][2], self.duration[self.value][3],
            self.duration[self.value][6],self.duration[self.value][7],
            self.chosenClass, self.price, self.bags.get(), self.name2.get()))
        self.makeReservation()

    def makeReservation(self):
        self.passengerInfoWin.withdraw()
        self.reservationWin = Toplevel()
        self.reservationWin.title("Make Reservation")

        frame = Frame(self.reservationWin)
        frame.pack(side=TOP)
        frame2 = Frame(self.reservationWin)
        frame2.pack(side=TOP)

        selected = Label(frame,text = "Currently Selected")
        selected.grid(row = 0, column = 0)

        l1 = Label(frame,text = "Train(Train Number)").grid(row = 1, column = 0)
        l2 = Label(frame,text = "Time(Duration)").grid(row = 1, column = 1)
        l3 = Label(frame,text = "Departs From").grid(row = 1, column = 2)
        l4 = Label(frame,text = "Arrives At").grid(row = 1, column = 3)
        l5 = Label(frame,text = "Class").grid(row = 1, column = 4)
        l6 = Label(frame,text = "Price").grid(row = 1, column =5)
        l7 = Label(frame,text = "# of baggages").grid(row = 1, column = 6)
        l8 = Label(frame,text = "Passenger Name").grid(row = 1, column = 7)
        l9 = Label(frame,text = "Remove").grid(row = 1, column = 8)


        a = 2
        b = 1
        self.w = IntVar()

        for result in self.results1:
            lb1=Label(frame, text = str(result[0]), anchor = "w")
            lb1.grid(row = a, column = 0, sticky = "ew")
            lb2=Label(frame, text = str(result[1]) + "-" + str(result[2]) +"\n" + str(result[3]), anchor = "w")
            lb2.grid(row = a, column = 1, sticky = "ew")
            lb3=Label(frame, text = str(result[4]), anchor = "w")
            lb3.grid(row = a, column = 2, sticky = "ew")
            lb4=Label(frame, text = str(result[5]), anchor = "w")
            lb4.grid(row = a, column = 3, sticky = "ew")
            lb5=Label(frame, text = str(result[6]), anchor = "w")
            lb5.grid(row = a, column = 4, sticky = "ew")
            lb6=Label(frame, text = str(result[7]), anchor = "w")
            lb6.grid(row = a, column = 5, sticky = "ew")
            lb7=Label(frame, text = str(result[8]), anchor = "w")
            lb7.grid(row = a, column = 6, sticky = "ew")
            lb8 = Label(frame, text = str(result[9]), anchor = "w")
            lb8.grid(row = a, column = 7, sticky = "ew")
            r1 = Radiobutton(frame, text = "Remove", variable = self.w, value = b, command = self.select2)
            r1.grid(row = a, column = 8,sticky = "ew")
            a = a + 1
            b += 9

        server = self.Connect()
        cursor = server.cursor()

        query = "SELECT Student_Discount FROM SYSTEM_INFO"
        cursor.execute(query)
        res = cursor.fetchall()
        discount = res[0][0]

        query = "SELECT Is_student FROM CUSTOMER WHERE Username = '%s'" % (self.username.get())
        cursor.execute(query)
        result3 = cursor.fetchone()
        temp_price = 0
        for entry in self.results1:
            temp_price += entry[7]
        self.price = temp_price
        print(result3[0])
        if result3[0] == 1:
            self.price = self.price*(1-discount/100)


        stuDis= Label(frame2,text = "Student Discount Applied.")
        stuDis.grid(row = 0, column = 0)
        totalC= Label(frame2, text = "Total Cost")
        totalC.grid(row = 1, column = 0)
        #cost = StringVar()
        costEnt = Label(frame2, text = self.price, width = 10)
        costEnt.grid(row = 1, column = 1)

        useCard= Label(frame2, text = "Use Card")
        useCard.grid(row = 4, column = 0)

        query = "SELECT Card_Number FROM PAYMENT_INFO WHERE Username = '%s'" % (self.username.get())
        cursor.execute(query)
        results = cursor.fetchall()
        newRes = []
        for res in results:
            newRes.append(int(res[0]))

        self.card = IntVar()
        option=OptionMenu(frame2, self.card, newRes[0], *newRes)
        option.grid(row = 4, column = 1)

        b5=Button(frame2, text ="Delete Card", command = self.deleteCard)
        b5.grid(row = 4, column =2)
        b1=Button(frame2, text ="Add Card", command = self.addCard)
        b1.grid(row = 4, column =3)

        b2=Button(frame2, text ="Continue adding a train", command = self.switchToSearch)
        b2.grid(row = 5, column = 0)

        b3=Button(frame2, text ="Back", command = self.switchToPassengerInfo)
        b3.grid(row = 6, column = 0)
        b4=Button(frame2, text ="Submit", command = self.confirmation)
        b4.grid(row =6, column = 1)

    def switchToSearch(self):
        self.reservationWin.destroy()
        self.searchTrain()

    def switchToPassengerInfo(self):
        self.reservationWin. destroy()
        self.passengerInfoWin.deiconify()

##    def getCost(self):
##        total = 0
##        for button in self.checkButtonsInDetails:
##            if button.is_checked():
##                total += button.selectRoom()[5]
##            total += button.selectRoom()[2]
##        self.totalCost = total*self.numDays
##        totallabel5 = Label(self.checkDetailsFrame, text=str(self.totalCost))
##        self.totalCostVarLabel.pack(side=TOP)
##        totallabel5.pack(side=TOP)

    def addCard(self):
        self.reservationWin.withdraw()
        self.paymentIWin = Toplevel()
        self.paymentIWin.title("Add Card")

        frame = Frame(self.paymentIWin)
        frame.pack(side=TOP)
        frame2 = Frame(self.paymentIWin)
        frame2.pack(side=TOP)
        frame3 = Frame(self.paymentIWin)
        frame3.pack(side=TOP)
        frame4 = Frame(self.paymentIWin)
        frame4.pack(side=TOP)
        frame5 = Frame(self.paymentIWin)
        frame5.pack(side=TOP)

        l1= Label(frame,text = "Name on Card")
        l1.pack(side=LEFT)
        l2= Label(frame2,text = "Card Number")
        l2.pack(side=LEFT)
        l3= Label(frame3,text = "CVV")
        l3.pack(side=LEFT)
        l4= Label(frame4,text = "Expiration Date")
        l4.pack(side=LEFT)

        self.name = StringVar()
        cardName = Entry(frame, textvariable = self.name, width = 10)
        cardName.pack(side = RIGHT)

        self.num = StringVar()
        cardNum = Entry(frame2, textvariable = self.num, width = 10)
        cardNum.pack(side = RIGHT)

        self.CVVnum = StringVar()
        Cvv = Entry(frame3, textvariable = self.CVVnum, width = 10)
        Cvv.pack(side = RIGHT)

        self.date1 = StringVar()
        expdate = Entry(frame4, textvariable = self.date1, width = 10)
        expdate.pack(side = RIGHT)

        b4=Button(frame5, text ="Submit", command = self.addCardCheck)
        b4.pack(side=LEFT)

        #start_date = datetime.strptime(self.startDateEntry.get(), '%Y-%m-%d')
        #    if start_date < datetime.now():


    def addCardCheck(self):
        self.expDate = datetime.strptime(self.date1.get(), '%Y-%m-%d')
        if self.expDate <= datetime.now():
            messagebox.showerror("Error, your card is expired.")

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT * FROM PAYMENT_INFO \
               WHERE Card_Number = '%s'" % (self.num.get())
        cursor.execute(query)
        results = cursor.fetchall()
        if len(results) != 0:
            messagebox.showerror("Error", "Card number already in use")
            return
        elif self.expDate == "" or self.name.get() == "" or self.num.get() == "" or self.CVVnum.get() == "":
            messagebox.showerror("Error", "Expiration Date, Name, Number, and CVV must be filled")
            return
        elif len(self.num.get()) != 10:
            messagebox.showerror("Error", "Card Number must be 10 digits")
            return
        elif len(self.CVVnum.get()) != 3:
            messagebox.showerror("Error", "CVV must be 3 digits")
            return

        server = self.Connect()
        cursor = server.cursor()
        query = "INSERT INTO PAYMENT_INFO(Card_Number, CVV, Exp_Date, Name_on_card, Username) VALUES ('%s', '%s', '%s', '%s', '%s')" % (self.num.get(), self.CVVnum.get(), self.expDate, self.name.get(), self.username.get())
        cursor.execute(query)
        result = cursor.fetchall()

        server.commit()
        cursor.close()
        server.close()
        self.paymentIWin.destroy()
        self.makeReservation()

    def deleteCard(self):
        self.reservationWin.withdraw()
        self.paymentIWin2= Toplevel()
        self.paymentIWin2.title("Delete Card")

        frame = Frame(self.paymentIWin2)
        frame.pack(side=TOP)
        frame2 = Frame(self.paymentIWin2)
        frame2.pack(side=BOTTOM)
        cardNum = Label(frame, text = "Card Number")
        cardNum.pack(side=LEFT)

        server = self.Connect()
        cursor = server.cursor()
        query1 = "SELECT Card_Number FROM PAYMENT_INFO WHERE Username = '%s'" % (self.username.get())
        cursor.execute(query1)
        results = cursor.fetchall()

        self.cardNum = StringVar()
        self.cardNum.set(results[0][0])

        option=OptionMenu(frame, self.cardNum, results[0], * results)
        option.pack(side=RIGHT)

        b1=Button(frame2, text ="Submit", command = self.deleteCardCheck)
        b1.pack(side=BOTTOM)

        self.cardNum = int(self.cardNum.get()[1:11])

    def deleteCardCheck(self):
        server = self.Connect()
        cursor = server.cursor()
        query1 = "SELECT Is_cancelled, Departure_Date FROM RESERVATION NATURAL JOIN RESERVES WHERE Card_Number ='%s'" % (self.cardNum)
        cursor.execute(query1)
        results = cursor.fetchall()
        for row in results:
            self.departDate = row[1]
            if self.departDate >= datetime.today() and row[0] == 0:
                messagebox.showerror("Error", "Card is being used for existing reservation")
                return

        query2 = "DELETE FROM PAYMENT_INFO WHERE Card_Number = '%s'" % (self.cardNum)
        cursor.execute(query2)

        server.commit()
        cursor.close()
        server.close()
        self.paymentIWin2.destroy()
        self.makeReservation()

    def switchToConfirm1(self):
        self.paymentIWin.withdraw()
        self.confirmation()

    def switchToConfirm2(self):
        self.paymentIWin2.withdraw()
        self.confirmation()

    def backToMain(self):
        self.confirm.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def select2(self):
        self.index = floor(self.w.get()/9)
        self.results1.remove(self.results1[self.index])
        self.reservationWin.destroy()
        self.makeReservation()

    def confirmation(self):
        server = self.Connect()
        cursor = server.cursor()
        #self.CARD = int(self.card.get())

        query = "SELECT MAX(ReservationID) FROM RESERVATION"
        cursor.execute(query)
        maxID = cursor.fetchall()
        self.newReservationID = maxID[0][0] + 1;

        query1 = "INSERT INTO RESERVATION(ReservationID, Is_cancelled, Username, Card_Number) VALUES ('%d', 0, '%s', '%d')" % (self.newReservationID, self.username.get(),self.card.get())
        cursor.execute(query1)

        for res in self.results1:
            query2 = "INSERT INTO RESERVES(ReservationID, Train_Number, Class, Departure_Date, Passenger_Name, Number_of_Bags, Departs_From, Arrives_At, Total_Cost) \
                VALUES ('%d', '%d', '%d', '%s', '%s', '%d', '%s', '%s', '%f')" % (self.newReservationID, self.trainChosen, self.classChosen, self.date.get(), res[9], res[6], res[4], res[5], res[7])
            cursor.execute(query2)

        self.reservationWin.destroy()
        self.confirm = Toplevel()
        self.confirm.title("Confirmation")

        frame = Frame(self.confirm)
        frame.pack()

        label1 = Label(frame, text = "Reservation ID:")
        label1.grid(row = 0, column = 0,sticky=E)
        e1 = Label(frame, text = self.newReservationID, width = 10)
        e1.grid(row = 0, column = 1)
        label3 = Label(frame, text="Thank you so much for your purchase! Please save the reservation ID for your records.")
        label3.grid(row = 2, column = 0, columnspan = 2)

        query = "SELECT ReservationID FROM RESERVATION WHERE Card_Number = '%d'" % (self.card.get())
        cursor.execute(query)
        results = cursor.fetchall()

        server.commit()
        cursor.close()
        server.close()

        self.entries = []
        self.results1 = []

        b=Button(frame, text ="Go back to choose functionality", command=self.backToMain)
        b.grid(row=3,column=1,sticky=E)

    def updateReservation(self):
        self.primaryWindow.destroy()
        self.updateWin = Toplevel()
        self.updateWin.title("Update Reservation")
        frame = Frame(self.updateWin)
        frame.pack()
        self.resID = IntVar()
        l1 = Label(frame, text = "Reservation ID")
        l1.grid(row = 0, column = 0, sticky = E)
        e1 = Entry(frame, textvariable = self.resID, width = 10)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Search", command = self.updateReservation2)
        b1.grid(row = 0, column = 2, sticky = E)
        b2 = Button(frame, text = "Back", command = self.switchMainMenu)
        b2.grid(row = 1, column = 1, sticky = E)

    def switchMainMenu(self):
        self.updateWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def update1(self):
        self.index = floor(self.w.get()/9)
#####################table info, new dept date, change fee, updated cost,#################
    def updateReservation2(self):
        self.updateWin.withdraw()
        self.updateWin2 = Toplevel()
        self.updateWin2.title("Update Reservation")

        frame = Frame(self.updateWin2)
        frame.pack()
        frame2 = Frame(self.updateWin2)
        frame2.pack()

        l0 = Label(frame,text = "Select").grid(row = 1, column = 0)
        l1 = Label(frame,text = "Train(Train Number)").grid(row = 1, column = 1)
        l2 = Label(frame,text = "Date").grid(row = 1, column = 2)
        l3 = Label(frame,text = "Departs From").grid(row = 1, column = 3)
        l4 = Label(frame,text = "Arrives At").grid(row = 1, column = 4)
        l5 = Label(frame,text = "Class").grid(row = 1, column = 5)
        l6 = Label(frame,text = "Price").grid(row = 1, column =6)
        l7 = Label(frame,text = "# of baggages").grid(row = 1, column = 7)
        l8 = Label(frame,text = "Passenger Name").grid(row = 1, column = 8)

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT * FROM RESERVES WHERE ReservationID = '%s'" % (self.resID.get())
        cursor.execute(query)
        self.results = cursor.fetchall()

        a = 2
        b = 1
        self.w = IntVar()
        print(self.results)
        for result in self.results:
            Radiobutton(frame, variable = self.w, value = b, command = self.update1).grid(row = a, column = 0)
            Label(frame, text = str(result[1]), anchor = "w").grid(row = a, column = 1, sticky = "ew")

            l11 = Label(frame, text = str(result[3]), anchor = "w")
            l11.grid(row = a, column = 2, sticky = "ew")
            l12 = Label(frame, text = str(result[6]), anchor = "w")
            l12.grid(row = a, column = 3, sticky = "ew")
            l13 = Label(frame, text = str(result[7]), anchor = "w")
            l13.grid(row = a, column = 4, sticky = "ew")
            l14 = Label(frame, text = str(result[2]), anchor = "w")
            l14.grid(row = a, column = 5, sticky = "ew")
            l15 =Label(frame, text = str(result[8]), anchor = "w")
            l15.grid(row = a, column = 6, sticky = "ew")
            l16 = Label(frame, text = str(result[5]), anchor = "w")
            l16.grid(row = a, column = 7, sticky = "ew")
            l17 = Label(frame, text = str(result[4]), anchor = "w")
            l17.grid(row = a, column = 8, sticky = "ew")
            a = a + 1
            b += 9

        b1 = Button(frame2, text = "Back", command = self.switchUpdateReservation)
        b1.pack(side = LEFT)
        b2 = Button(frame2, text = "Next", command = self.updateReservation3)
        b2.pack(side = RIGHT)

    def switchUpdateReservation(self):
        self.updateWin2.destroy()
        #self.updateWin = Toplevel()
        self.updateReservation()

    def switchUpdateReservation2(self):
        self.updateWin3.destroy()
        self.updateReservation2()

    def updateTree2(self, frame):
        tree=Treeview(frame)
        tree.grid(row = 2, column = 0)
        tree["show"] = "headings"
        tree["columns"]=("train","date", "dept", "arrv", "class", "pr", "bag", "name")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("date", text = "Date")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of Baggages")
        tree.heading("name", text= "Passenger Name")
        return tree

    def updateTree3(self, frame):
        tree=Treeview(frame)
        tree.grid(row = 4, column = 0, sticky = E)
        tree["show"] = "headings"
        tree["columns"]=("train", "dept", "arrv", "class", "pr", "bag", "name")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of Baggages")
        tree.heading("name", text= "Passenger Name")
        return tree

    def updateDepartureDate(self):
        self.updatedDate = datetime.strptime(self.date.get(), '%Y-%m-%d')


    def updateReservation3(self):
        self.updateWin2.withdraw()
        self.updateWin3 = Toplevel()
        self.updateWin3.title("Update Reservation")

        frame = Frame(self.updateWin3)
        frame.pack()
        frame2 = Frame(self.updateWin3)
        frame2.pack()
        frame3 = Frame(self.updateWin3)
        frame3.pack()
        frame4 = Frame(self.updateWin3)
        frame4.pack()
        frame5 = Frame(self.updateWin3)
        frame5.pack()

        updateIndex = floor(self.w.get()/9)
        updateTuple = self.results[updateIndex]

        l1 = Label(frame, text = "Current Train Ticket")
        l1.grid(row = 1, column = 1, sticky = E)

        i = 0
        tree = self.updateTree2(frame2)
        tree.insert('', i, text='', values=(updateTuple[1], updateTuple[3],updateTuple[6],updateTuple[7], updateTuple[2], updateTuple[8], updateTuple[5],updateTuple[4]))
        newdepDate= Label(frame3,text ="New Departure Date")
        newdepDate.grid(row = 0, column = 0, sticky = E)
        self.date = StringVar() ## assume YYYY-MM-DD
        e1= Entry(frame3,textvariable = self.date, width = 10)
        e1.grid(row = 0, column = 1, sticky = EW)
        self.updatedDate = updateTuple[3]
        b1 = Button(frame3, text = "Search availability", command = self.updateDepartureDate)
        b1.grid(row = 0, column = 2, sticky = EW)


        l2 = Label(frame3, text = "Updated Train Ticket")
        l2.grid(row = 1, column = 1, sticky = E)

        i = 0
        tree2 = self.updateTree3(frame4)
        tree2.insert('', i, text='', values=(updateTuple[1],updateTuple[6],updateTuple[7], updateTuple[2], updateTuple[8], updateTuple[5],updateTuple[4]))



        server = self.Connect()
        cursor = server.cursor()
        query2 = "SELECT Change_fee FROM SYSTEM_INFO"
        cursor.execute(query2)
        changefee = cursor.fetchone()
        change_fee = changefee[0]
        query4 = "SELECT * FROM RESERVES WHERE ReservationID = '%s'" % (self.resID.get())
        cursor.execute(query4)
        self.results = cursor.fetchall()
        query3 = "SELECT Total_Cost FROM RESERVES WHERE ReservationID='%d' AND Train_Number='%d'" % (self.resID.get(), self.results[self.index][1])
        cursor.execute(query3)
        totalcost = cursor.fetchone()
        self.total_cost = totalcost[0]
        self.total_cost = self.total_cost + change_fee
        print (type(self.total_cost))

        changeFee = Label(frame5,text ="Change Fee")
        changeFee.grid(row = 0, column = 0, sticky = E)
        self.value = StringVar()
        e2 = Label(frame5,text = change_fee, width = 10)
        e2.grid(row = 0, column = 1, sticky = E)
        updatedCost = Label(frame5,text ="Updated Total Cost")
        updatedCost.grid(row = 1, column = 0, sticky = E)
        e3 = Label(frame5, text = self.total_cost, width = 10)
        e3.grid(row = 1, column = 1)


        b2=Button(frame5, text ="Back", command = self.switchUpdateReservation2)
        b2.grid(row =2, column = 0, sticky = E)
        b3=Button(frame5, text ="Submit", command = self.submit)
        b3.grid(row =2, column = 1, sticky = E)


    def submit(self):
        self.updateWin3.destroy()
        server = self.Connect()
        cursor = server.cursor()
        query1 = "UPDATE RESERVES SET RESERVES.Departure_Date = '%s', RESERVES.Total_Cost = '%d' WHERE ReservationID='%d' AND Train_Number='%d'" % (self.updatedDate, self.total_cost, self.resID.get(), self.results[self.index][1])
        cursor.execute(query1)
        cursor.close()
        server.commit()
        server.close()
        self.mainMenu()

################## reservation id search, table/ total cost, date, amount to be refunded#######################
    def cancelRes(self):
        self.primaryWindow.withdraw()
        self.cancelWin = Toplevel()
        self.cancelWin.title("Cancel Reservation")

        frame = Frame(self.cancelWin)
        frame.pack()

        l1 = Label(frame, text = "Reservation ID")
        l1.grid(row = 0, column = 0, sticky = E)
        e1 = Entry(frame, width = 10)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Search", command = self.cancelRes2)
        b1.grid(row = 0, column = 2, sticky = E)
        b2 = Button(frame, text = "Back", command = self.switchToMain)
        b2.grid(row = 1, column = 1, sticky = E)

    def switchToMain(self):
        self.cancelWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def updateTree4(self, frame):
        tree=Treeview(frame)
        tree.grid(row = 0, column = 0, sticky = E)
        tree["show"] = "headings"
        tree["columns"]=("train","time","dept", "arrv", "class", "pr", "bag", "name")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("time", text= "Time (Duration)")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of Baggages")
        tree.heading("name", text= "Passenger Name")
        return tree

    def cancelRes2(self):
        self.cancelWin.destroy()
        self.cancelWin2 = Toplevel()
        self.cancelWin2.title("Cancel Reservation")

        frame = Frame(self.cancelWin2)
        frame.pack()
        frame2 = Frame(self.cancelWin2)
        frame2.pack()
        frame3 = Frame(self.cancelWin2)
        frame3.pack()

        tree = self.updateTree4(frame)

        l1= Label(frame2,text ="Total Cost of Reservation")
        l1.grid(row = 1, column = 0, sticky = E)
        e1= Label(frame2,text = self.price, width = 10)
        e1.grid(row = 1, column = 1, sticky = EW)

        self.cancelDate = date.today()
        l2 = Label(frame2, text = "Date of Cancellation")
        l2.grid(row = 2, column = 0, sticky = E)
        e2= Label(frame2,text = self.cancelDate.get(), width = 10)
        e2.grid(row = 2, column = 1, sticky = EW)

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT Is_cancelled, MIN(Departure_Date) FROM RESERVATION, RESERVES WHERE ReservationID = '%d'" % (self.resCancelID.get())
        cursor.execute(query)
        results = cursor.fetchall()

        #fix the dates here

        if self.cancelDate < (results[1] - datetime.timedelta(days=7)):
            self.refund = self.price * 0.8 - 50
        elif self.cancelDate > (results[1] - datetime.timedelta(days=7)) and self.cancelDate < (results[1] + datetime.timedelta(days=1)):
            self.refuned = self.price * 0.5 - 50
        elif self.cancelDate > (results[1] - datetime.timedelta(days=1)):
            self.refund = 0
            print("Cannot cancel reservation within a day of departure date")
            return

        if self.refund < 0:
            self.refund = 0

        self.price = self.price - self.refund.get()

        l3 = Label(frame2, text = "Amount to be Refunded")
        l3.grid(row = 3, column = 0, sticky = E)
        e2= Label(frame2,text = self.refund().get(), width = 10)
        e2.grid(row = 3, column = 1, sticky = EW)

        b2=Button(frame3, text ="Back", command = self.switchCancelRes1)
        b2.grid(row =4, column = 0, sticky = E)

        if results[0] == 1:
            print("Reservation already cancelled, cannot cancel again")
            return
        else:
            queryCancel = "UPDATE RESERVATION SET Is_cancelled = 1 WHERE ReservationID = '%d'" % (self.resCancelID.get())
            b3=Button(frame3, text ="Submit", command = self.switchTC)
            b3.grid(row =4, column = 1, sticky = E)

    def switchCancelRes1(self):
        self.cancelWin2.destroy()
        self.cancelRes()

    def switchTC(self):
        self.cancelWin2.destroy()
        self.confirmation()

    def viewReview(self):
        self.primaryWindow.withdraw()
        self.viewReviewWin = Toplevel()
        self.viewReviewWin.title("View Review")

        frame = Frame(self.viewReviewWin)
        frame.pack()

        l1 = Label(frame, text = "Train Number")
        l1.grid(row = 0, column = 0, sticky = W)
        e1 = Entry(frame, textvariable = self.TrainReviewNumber, width = 20)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Back", command = self.backMain)
        b1.grid(row = 1, column = 0)
        b2 = Button(frame, text = "Next", command = self.viewReview2)
        b2.grid(row = 1, column = 1)

    def backMain(self):
        self.viewReviewWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def viewTree(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["show"] = "headings"
        tree["columns"]=("select","train","time","dept", "arrv", "class", "pr", "bag", "name")
        tree.heading("select", text= "Select")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("time", text= "Time (Duration)")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of baggages")
        tree.heading("name", text= "Passenger Name")
        return tree

    def viewReview2(self):
        self.viewReviewWin.withdraw()
        self.viewReviewWin2 = Toplevel()
        self.viewReviewWin2.title("View Review")

        frame = Frame(self.viewReviewWin2)
        frame.pack()

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT Comment, Rating FROM REVIEW WHERE REVIEW.Train_Number = '%d'" % (TrainReviewNumber)
        cursor.execute(query)
        results = cursor.fetchall()

        tree = self.viewTree(frame)

        b1 = Button(frame, text = "Back to Choose Functionality", command = self.switchMainMenu)
        b1.pack(side = BOTTOM)

    def switchMainMenu(self):
        self.viewReviewWin2.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def giveReview(self):
        self.primaryWindow.destroy()
        self.giveReviewWin = Toplevel()
        self.giveReviewWin.title("Give Review")

        frame = Frame(self.giveReviewWin)
        frame.pack()

        self.trainNo = IntVar()
        l1 = Label(frame, text = "Train Number")
        l1.grid(row = 0, column = 0, sticky = W)
        e1 = Entry(frame, textvariable = self.trainNo, width = 20)
        e1.grid(row = 0, column = 1)

        l2 = Label(frame, text = "Rating")
        l2.grid(row = 1, column = 0, sticky = W)
        self.rating = StringVar()
        self.cho = ["Very Good", "Good", "Neutral", "Bad", "Very Bad"]

        option = OptionMenu(frame, self.rating, self.cho[0], *self.cho)
        option.grid(row = 1, column = 1)

        self.comment = StringVar()
        l3 = Label(frame, text = "Comment")
        l3.grid(row = 2, column = 0, sticky = W)
        e3 = Entry(frame, textvariable = self.comment, width = 20)
        e3.grid(row = 2, column = 1)

        b1=Button(frame, text ="Submit", command = self.verifyRev)
        b1.grid(row = 3, column = 1)


    def verifyRev(self):
        if self.trainNo == "":
            messagebox.showerror("Error", "Enter a train number")
        if self.trainNo == "" or self.rating == "":
            messagebox.showerror("Error", "Train Number and Rating cannot be left blank.")
        else:
            self.rate = 5
            if self.rating.get() == self.cho[0]:
                self.rate = 5
            elif self.rating.get() == self.cho[1]:
                self.rate = 4
            elif self.rating.get() == self.cho[2]:
                self.rate = 3
            elif self.rating.get() == self.cho[3]:
                self.rate = 2
            elif self.rating.get() == self.cho[4]:
                self.rate = 1

            server = self.Connect()
            cursor = server.cursor()
            queryFrom = "SELECT MAX(Review_Number) FROM REVIEW"
            cursor.execute(queryFrom)
            result = cursor.fetchall()

            query = "INSERT INTO REVIEW(Review_Number, Comment, Rating, Username, Train_Number) VALUES ('%d', '%s', '%d', '%s', '%d')" % (result[0][0] + 1, self.comment.get(), self.rate, self.username.get(), self.trainNo.get())
            cursor.execute(query)
            server.commit()
            cursor.close()
            server.close()
            self.giveReviewWin.destroy()
            self.primaryWindow = Toplevel()
            self.mainMenu()
    ################ check to see if the train number is valid###############################
    def mainBack(self):
        if self.trainNo == "":
            messagebox.showerror("Error", "Enter a train number")
        ######elif ##train number isnt correct:
        else:
            self.giveReviewWin.destroy()
            self.primaryWindow = Toplevel()
            self.mainMenu()
            ###########write the rating to a DB#################


    def viewTree2(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["show"] = "headings"
        tree["columns"]=("mon","rev")
        tree.heading("mon", text= "Month")
        tree.heading("rev", text= "Revenue")
        return tree

    def viewRevenueRep(self):
        self.primaryWindow.withdraw()
        self.viewRevenueReport = Toplevel()
        self.viewRevenueReport.title("View Revenue Report")

        frame = Frame(self.viewRevenueReport)
        frame.pack()

        current = datetime.datetime.now().strftime("%Y-%m-01")
        backOne = (datetime.datetime.now() - datetime.timedelta(30)).strftime("%Y-%m-01")
        backTwo = (datetime.datetime.now() - datetime.timedelta(60)).strftime("%Y-%m-01")
        backThree = (datetime.datetime.now() - datetime.timedelta(90)).strftime("%Y-%m-01")


        if backOne == "01":
            backOneShow = "January"
        if backOne == "02":
            backOneShow = "February"
        if backOne == "03":
            backOneShow = "March"
        if backOne == "04":
            backOneShow = "April"
        if backOne == "05":
            backOneShow = "May"
        if backOne == "06":
            backOneShow = "June"
        if backOne == "07":
            backOneShow = "July"
        if backOne == "08":
            backOneShow = "August"
        if backOne == "09":
            backOneShow = "September"
        if backOne == "10":
            backOneShow = "October"
        if backOne == "11":
            backOneShow = "November"
        if backOne == "12":
            backOneShow = "December"


        if backTwo == "01":
            backTwoShow = "January"
        if backTwo == "02":
            backTwoShow = "February"
        if backTwo == "03":
            backTwoShow = "March"
        if backTwo == "04":
            backTwoShow = "April"
        if backTwo == "05":
            backTwoShow = "May"
        if backTwo == "06":
            backTwoShow = "June"
        if backTwo == "07":
            backTwoShow = "July"
        if backTwo == "08":
            backTwoShow = "August"
        if backTwo == "09":
            backTwoShow = "September"
        if backTwo == "10":
            backTwoShow = "October"
        if backTwo == "11":
            backTwoShow = "November"
        if backTwo == "12":
            backTwoShow = "December"

        if backThree == "01":
            backThreeShow = "January"
        if backThree == "02":
            backThreeShow = "February"
        if backThree == "03":
            backThreeShow = "March"
        if backThree == "04":
            backThreeShow = "April"
        if backThree == "05":
            backThreeShow = "May"
        if backThree == "06":
            backThreeShow = "June"
        if backThree == "07":
            backThreeShow = "July"
        if backThree == "08":
            backThreeShow = "August"
        if backThree == "09":
            backThreeShow = "September"
        if backThree == "10":
            backThreeShow = "October"
        if backThree == "11":
            backThreeShow = "November"
        if backThree == "12":
            backThreeShow = "December"

        server = self.Connect()
        cursor = server.cursor()
        query1 = "SELECT SUM(Total_Cost) FROM RESERVES WHERE Departure_Date > '%s' AND Departure_Date < '%s'" % (backThree, backTwo)
        query2 = "SELECT SUM(Total_Cost) FROM RESERVES WHERE Departure_Date > '%s' AND Departure_Date < '%s'" % (backTwo, backOne)
        query3 = "SELECT SUM(Total_Cost) FROM RESERVES WHERE Departure_Date > '%s' AND Departure_Date < '%s'" % (backOne, current)
        cursor.execute(query1)
        result1 = cursor.fetchall()
        cursor.execute(query2)
        result2 = cursor.fetchall()
        cursor.execute(query3)
        result3 = cursor.fetchall()

        tree = self.viewTree2(frame)
        tree.insert('', 0, text='', values=(backThreeShow, result1[0][0]))
        tree.insert('', 1, text='', values=(backTwoShow, result2[0][0]))
        tree.insert('', 2, text='', values=(backOneShow, result3[0][0]))

        b1 = Button(frame, text = "Back", command = self.switchMain)
        b1.pack(side = BOTTOM)

    def switchMain(self):
        self.viewRevenueReport.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def viewTree3(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["show"] = "headings"
        tree["columns"]=("mon","num","rsv")
        tree.heading("mon", text= "Month")
        tree.heading("num", text= "Train number")
        tree.heading("rsv", text= "#of Reservations")
        return tree

    def viewpopRR(self):
        #to store in tree somehow

        #Month  -               Route   -      Reservations
        #backThreeShow      results1[0][0]    results1[0][1]
        #                   results1[1][0]    results1[1][1]
        #                   results1[2][0]    results1[2][1]
        #backTwoShow        results2[0][0]    results2[0][1]
        #                   results2[1][0]    results2[1][1]
        #                   results2[2][0]    results2[2][1]
        #backOneShow        results3[0][0]    results3[0][1]
        #                   results3[1][0]    results3[1][1]
        #                   results3[2][0]    results3[2][1]

        self.primaryWindow.withdraw()
        self.viewpopRRWin = Toplevel()
        self.viewpopRRWin.title("View Popular Route Report")
        frame = Frame(self.viewpopRRWin)
        frame.pack()

        current = datetime.datetime.now().strftime("%Y-%m-01")
        backOne = (datetime.datetime.now() - datetime.timedelta(30)).strftime("%Y-%m-01")
        backTwo = (datetime.datetime.now() - datetime.timedelta(60)).strftime("%Y-%m-01")
        backThree = (datetime.datetime.now() - datetime.timedelta(90)).strftime("%Y-%m-01")

        backOneM = backOne[5:7]
        backTwoM = backTwo[5:7]
        backThreeM = backThree[5:7]
        backOneShow = ""
        backTwoShow = ""
        backThreeShow = ""

        if backOneM == "01":
            backOneShow = "January"
        if backOneM == "02":
            backOneShow = "February"
        if backOneM == "03":
            backOneShow = "March"
        if backOneM == "04":
            backOneShow = "April"
        if backOneM == "05":
            backOneShow = "May"
        if backOneM == "06":
            backOneShow = "June"
        if backOneM == "07":
            backOneShow = "July"
        if backOneM == "08":
            backOneShow = "August"
        if backOneM == "09":
            backOneShow = "September"
        if backOneM == "10":
            backOneShow = "October"
        if backOneM == "11":
            backOneShow = "November"
        if backOneM == "12":
            backOneShow = "December"


        if backTwoM == "01":
            backTwoShow = "January"
        if backTwoM == "02":
            backTwoShow = "February"
        if backTwoM == "03":
            backTwoShow = "March"
        if backTwoM == "04":
            backTwoShow = "April"
        if backTwoM == "05":
            backTwoShow = "May"
        if backTwoM == "06":
            backTwoShow = "June"
        if backTwoM == "07":
            backTwoShow = "July"
        if backTwoM == "08":
            backTwoShow = "August"
        if backTwoM == "09":
            backTwoShow = "September"
        if backTwoM == "10":
            backTwoShow = "October"
        if backTwoM == "11":
            backTwoShow = "November"
        if backTwoM == "12":
            backTwoShow = "December"

        if backThreeM == "01":
            backThreeShow = "January"
        if backThreeM == "02":
            backThreeShow = "February"
        if backThreeM == "03":
            backThreeShow = "March"
        if backThreeM == "04":
            backThreeShow = "April"
        if backThreeM == "05":
            backThreeShow = "May"
        if backThreeM == "06":
            backThreeShow = "June"
        if backThreeM == "07":
            backThreeShow = "July"
        if backThreeM == "08":
            backThreeShow = "August"
        if backThreeM == "09":
            backThreeShow = "September"
        if backThreeM == "10":
            backThreeShow = "October"
        if backThreeM == "11":
            backThreeShow = "November"
        if backThreeM == "12":
            bakcThreeShow = "December"

        server = self.Connect()
        cursor = server.cursor()
        queryMonth1 = "CREATE VIEW Month1 (Reservations, TNumber) AS SELECT ReservationID, Train_Number FROM RESERVATION NATURAL JOIN RESERVES WHERE Is_cancelled = '%d' AND Departure_Date > '%s' AND Departure_Date < '%s'" % (0, backThree, backTwo)
        cursor.execute(queryMonth1)
        queryHere1 = "SELECT TNumber, COUNT(DISTINCT Reservations) FROM Month1 GROUP BY TNumber"
        cursor.execute(queryHere1)
        tempResults1 = cursor.fetchall()
        queryPerTrain1 = "CREATE TABLE PerTrain1(Route INT(10), Num INT(10))"
        cursor.execute(queryPerTrain1)
        for result in tempResults1:
            self.TNumber = result[0]
            self.countReservations = result[1]
            queryFillTrain1 = "INSERT INTO PerTrain1(Route, Num) VALUES ('%d', '%d')" % (self.TNumber, self.countReservations)
            cursor.execute(queryFillTrain1)
            server.commit()
        queryUltimate1 = "SELECT * FROM PerTrain1"
        cursor.execute(queryUltimate1)
        preResults11 = cursor.fetchall()
        maxNum11 = 0
        maxTup11 = (0,0)
        for result in preResults11:
            if result[1] > maxNum11:
                maxNum11 = result[1]
                maxTup11 = (result[0], result[1])
        results1 = []
        results1.append(maxTup11)
        if len(results1) < 3:
            queryNext = "DELETE FROM PerTrain1 ORDER BY Num DESC LIMIT 1"
            cursor.execute(queryNext)
            queryPenultimate1 = "SELECT * FROM PerTrain1"
            cursor.execute(queryPenultimate1)
            preResults12 = cursor.fetchall()
            maxNum12 = 0
            maxTup12 = (0,0)
            for result in preResults12:
                if result[1] > maxNum12:
                    maxNum12 = result[1]
                    maxTup12 = (result[0], result[1])
            results1.append(maxTup12)
            if len(results1) < 3:
                queryNext = "DELETE FROM PerTrain1 ORDER BY Num DESC LIMIT 1"
                cursor.execute(queryNext)
                queryAntepenultimate1 = "SELECT * FROM PerTrain1"
                cursor.execute(queryAntepenultimate1)
                preResults13 = cursor.fetchall()
                maxNum13 = 0
                maxTup13 = (0,0)
                for result in preResults13:
                    if result[1] > maxNum13:
                        maxNum13 = result[1]
                        maxTup13 = (result[0], result[1])
                results1.append(maxTup13)
                #insert table stuff here;  results1[0][0] = route num, results[0][1] = max # of reservations, etc, up to results1[2][1]
            else:
                pass
                #insert table stuff here;  results1[0][0] = route num, results[0][1] = max # of reservations, etc, up to results1[2][1]
        else:
            pass
            #insert table stuff here;  results1[0][0] = route num, results[0][1] = max # of reservations, etc, up to results1[2][1]

        queryMonth2 = "CREATE VIEW Month2 (Reservations, TNumber) AS SELECT ReservationID, Train_Number FROM RESERVATION NATURAL JOIN RESERVES WHERE Is_cancelled = '%d' AND Departure_Date > '%s' AND Departure_Date < '%s'" % (0, backTwo, backOne)
        cursor.execute(queryMonth2)
        queryHere2 = "SELECT TNumber, COUNT(DISTINCT Reservations) FROM Month2 GROUP BY TNumber"
        cursor.execute(queryHere2)
        tempResults2 = cursor.fetchall()
        queryPerTrain2 = "CREATE TABLE PerTrain2(Route INT(10), Num INT(10))"
        cursor.execute(queryPerTrain2)
        for result in tempResults2:
            self.TNumber = result[0]
            self.countReservations = result[1]
            queryFillTrain2 = "INSERT INTO PerTrain2(Route, Num) VALUES ('%d', '%d')" % (self.TNumber, self.countReservations)
            cursor.execute(queryFillTrain2)
            server.commit()
        queryUltimate2 = "SELECT * FROM PerTrain2"
        cursor.execute(queryUltimate2)
        preResults21 = cursor.fetchall()
        maxNum21 = 0
        maxTup21 = (0,0)
        for result in preResults21:
            if result[1] > maxNum21:
                maxNum21 = result[1]
                maxTup21 = (result[0], result[1])
        results2 = []
        results2.append(maxTup21)
        if len(results2) < 3:
            queryNext = "DELETE FROM PerTrain2 ORDER BY Num DESC LIMIT 1"
            cursor.execute(queryNext)
            queryPenultimate2 = "SELECT * FROM PerTrain2"
            cursor.execute(queryPenultimate2)
            preResults22 = cursor.fetchall()
            maxNum22 = 0
            maxTup22 = (0,0)
            for result in preResults22:
                if result[1] > maxNum22:
                    maxNum22 = result[1]
                    maxTup22 = (result[0], result[1])
            results2.append(maxTup22)
            if len(results2) < 3:
                queryNext = "DELETE FROM PerTrain2 ORDER BY Num DESC LIMIT 1"
                cursor.execute(queryNext)
                queryAntepenultimate2 = "SELECT * FROM PerTrain2"
                cursor.execute(queryAntepenultimate2)
                preResults23 = cursor.fetchall()
                maxNum23 = 0
                maxTup23 = (0,0)
                for result in preResults23:
                    if result[1] > maxNum13:
                        maxNum23 = result[1]
                        maxTup23 = (result[0], result[1])
                results2.append(maxTup23)
                #insert table stuff here;  results2[0][0] = route num, results2[0][1] = max # of reservations, etc, up to results2[2][1]
            else:
                pass
                #insert table stuff here;  results2[0][0] = route num, results2[0][1] = max # of reservations, etc, up to results2[2][1]
        else:
            pass
            #insert table stuff here;  results2[0][0] = route num, results2[0][1] = max # of reservations, etc, up to results2[2][1]

        queryMonth3 = "CREATE VIEW Month3 (Reservations, TNumber) AS SELECT ReservationID, Train_Number FROM RESERVATION NATURAL JOIN RESERVES WHERE Is_cancelled = '%d' AND Departure_Date > '%s' AND Departure_Date < '%s'" % (0, backOne, current)
        cursor.execute(queryMonth3)
        queryHere3 = "SELECT TNumber, COUNT(DISTINCT Reservations) FROM Month3 GROUP BY TNumber"
        cursor.execute(queryHere3)
        tempResults3 = cursor.fetchall()
        queryPerTrain3 = "CREATE TABLE PerTrain3(Route INT(10), Num INT(10))"
        cursor.execute(queryPerTrain3)
        for result in tempResults3:
            self.TNumber = result[0]
            self.countReservations = result[1]
            queryFillTrain3 = "INSERT INTO PerTrain3(Route, Num) VALUES ('%d', '%d')" % (self.TNumber, self.countReservations)
            cursor.execute(queryFillTrain3)
            server.commit()
        queryUltimate3 = "SELECT * FROM PerTrain3"
        cursor.execute(queryUltimate3)
        preResults31 = cursor.fetchall()
        maxNum31 = 0
        maxTup31 = (0,0)
        for result in preResults31:
            if result[1] > maxNum31:
                maxNum31 = result[1]
                maxTup31 = (result[0], result[1])
        results3 = []
        results3.append(maxTup31)
        if len(results3) < 3:
            queryNext = "DELETE FROM PerTrain3 ORDER BY Num DESC LIMIT 1"
            cursor.execute(queryNext)
            queryPenultimate3 = "SELECT * FROM PerTrain3"
            cursor.execute(queryPenultimate3)
            preResults32 = cursor.fetchall()
            maxNum32 = 0
            maxTup32 = (0,0)
            for result in preResults32:
                if result[1] > maxNum32:
                    maxNum32 = result[1]
                    maxTup32 = (result[0], result[1])
            results3.append(maxTup32)
            if len(results3) < 3:
                queryNext = "DELETE FROM PerTrain3 ORDER BY Num DESC LIMIT 1"
                cursor.execute(queryNext)
                queryAntepenultimate3 = "SELECT * FROM PerTrain3"
                cursor.execute(queryAntepenultimate3)
                preResults33 = cursor.fetchall()
                maxNum33 = 0
                maxTup33 = (0,0)
                for result in preResults33:
                    if result[1] > maxNum13:
                        maxNum33 = result[1]
                        maxTup33 = (result[0], result[1])
                results3.append(maxTup33)
                #insert table stuff here;  results1[0][0] = route num, results[0][1] = max # of reservations, etc, up to results1[2][1]
            else:
                pass
                #insert table stuff here;  results1[0][0] = route num, results[0][1] = max # of reservations, etc, up to results1[2][1]
        else:
            pass
            #insert table stuff here;  results1[0][0] = route num, results[0][1] = max # of reservations, etc, up to results1[2][1]

        queryDrop11 = "DROP VIEW Month1"
        queryDrop12 = "DROP TABLE PerTrain1"
        queryDrop21 = "DROP VIEW Month2"
        queryDrop22 = "DROP TABLE PerTrain2"
        queryDrop31 = "DROP VIEW Month3"
        queryDrop32 = "DROP TABLE PerTrain3"
        cursor.execute(queryDrop11)
        cursor.execute(queryDrop12)
        cursor.execute(queryDrop21)
        cursor.execute(queryDrop22)
        cursor.execute(queryDrop31)
        cursor.execute(queryDrop32)
        server.commit()
        cursor.close()
        server.close()

        tree = self.viewTree3(frame)
        tree.insert('', 0, text='', values=(backThreeShow, results1[0][0], results1[0][1]))
        tree.insert('', 1, text='', values=(backThreeShow, results1[1][0], results1[1][1]))
        tree.insert('', 2, text='', values=(backThreeShow, results1[2][0], results1[2][1]))
        tree.insert('', 3, text='', values=(backTwoShow, results2[0][0], results2[0][1]))
        tree.insert('', 4, text='', values=(backTwoShow, results2[1][0], results2[1][1]))
        tree.insert('', 5, text='', values=(backTwoShow, results2[2][0], results2[2][1]))
        tree.insert('', 6, text='', values=(backOneShow, results3[0][0], results3[0][1]))
        tree.insert('', 7, text='', values=(backOneShow, results3[1][0], results3[1][1]))
        tree.insert('', 8, text='', values=(backOneShow, results3[2][0], results3[2][1]))


    def swtMain(self):
        self.viewpopRRWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

mw = Tk()
app = Phase_three(mw)
mw.mainloop()
