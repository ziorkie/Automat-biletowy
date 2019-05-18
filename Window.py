from tkinter import *
from ticket import *
from coin import *
class negativeValueError(Exception):
    pass

class Application(Frame, Tickets, Coin):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Tickets.__init__(self)
        Coin.__init__(self)
        self.master = master
        self.pack()
        master.iconbitmap('images/mobileMPK_ico.ico')
        self.inicializephoto()
        self.viewedText = ""
        self.createWidgets()
        self.center()
        self.write("")



    def inicializephoto(self):
        self.photoz100 = PhotoImage(file="images/z100.png")
        self.photoz50 = PhotoImage(file="images/z50.png")
        self.photoz20 = PhotoImage(file="images/z20.png")
        self.photoz10 = PhotoImage(file="images/z10.png")
        self.photoz5 = PhotoImage(file="images/z5.png")
        self.photoz2 = PhotoImage(file="images/z2.png")
        self.photoz1 = PhotoImage(file="images/z1.png")
        self.photog50 = PhotoImage(file="images/g50.png")
        self.photog20 = PhotoImage(file="images/g20.png")
        self.photog10 = PhotoImage(file="images/g10.png")
        self.photoW= PhotoImage(file="images/wallet.png")
        self.photoC=PhotoImage(file="images/card.png")

    def center(self):
        # centrowanie okna na ekranie
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))



    def new_window(self):
        walletWindow= Toplevel(self)
        walletFrameLeft=Frame(walletWindow)
        walletFrameLeft.pack(side=LEFT, fill=Y)
        walletFrameMiddle=Frame(walletWindow)
        walletFrameMiddle.pack(side=LEFT, fill=Y)
        walletFrameRight=Frame(walletWindow)
        walletFrameRight.pack(side=LEFT, fill=Y)
        b_money1 = Button(walletFrameLeft, bg = "mint cream", image = self.photog10, overrelief = GROOVE, command = lambda: self.throwMoney("0.10",quantity.get()))
        b_money1.pack(anchor=N)
        b_money2=Button(walletFrameLeft, image=self.photog20, overrelief=GROOVE, command=lambda:self.throwMoney("0.20",quantity.get()))
        b_money2.pack(anchor=N)
        b_money3 = Button(walletFrameLeft, image=self.photog50, overrelief=GROOVE, command=lambda: self.throwMoney("0.50",quantity.get()))
        b_money3.pack(anchor=N)
        b_money4 = Button(walletFrameMiddle, image=self.photoz1, overrelief=GROOVE, command=lambda: self.throwMoney("1",quantity.get()))
        b_money4.pack(anchor=N)
        b_money5 = Button(walletFrameMiddle, image=self.photoz2, overrelief=GROOVE,
                          command=lambda: self.throwMoney("2",quantity.get()))
        b_money5.pack(anchor=N)
        b_money6 = Button(walletFrameMiddle, image=self.photoz5, overrelief=GROOVE,
                          command=lambda: self.throwMoney("5",quantity.get()))
        b_money6.pack(anchor=N)
        b_money7 = Button(walletFrameRight, image=self.photoz10, overrelief=GROOVE,
                          command=lambda: self.throwMoney("10",quantity.get()))
        b_money7.pack(anchor=N)
        b_money8 = Button(walletFrameRight, image=self.photoz20, overrelief=GROOVE,
                          command=lambda: self.throwMoney("20",quantity.get()))
        b_money8.pack(anchor=N)
        b_money9 = Button(walletFrameRight, image=self.photoz50, overrelief=GROOVE,
                          command=lambda: self.throwMoney("50",quantity.get()))
        b_money9.pack(anchor=N)
        b_money10 = Button(walletFrameRight, image=self.photoz100, overrelief=GROOVE,
                          command=lambda: self.throwMoney("100", quantity.get()))
        b_money10.pack(anchor=N)

        b_card=Button(walletFrameLeft, image=self.photoC, overrelief=GROOVE, width=150, command=lambda: self.calculateChangeCard())
        b_card.pack(expand=1, anchor=W)
        emptyLabel=Label(walletFrameMiddle, width=3, height=7)
        emptyLabel.pack(anchor=N)
        emptyLabel2=Label(walletFrameRight, width=3, height=2)
        emptyLabel2.pack(anchor=N)
        quantityLabel=Label(walletFrameMiddle, text="ILOŚĆ:")
        quantityLabel.pack(anchor=E)
        quantity=Spinbox(walletFrameRight, from_=1, to=100)
        quantity.pack(anchor=W)

    def addTicket(self, key):
        self.viewedText += str(self.addTickets(key))
        self.write("")

    def undoTickets(self):
        self.viewedText += str(self.undoTicket())
        self.write("")

    def buyTickets(self):
        self.byeText="Bilety zostaną wydrukowane.\nZapraszamy ponownie!\n\n\n\n\n\n"
        self.screen.insert(0.0, self.byeText)

    def calculateChange(self):
        try:
            change=self.cashtempAmount-self.toPay
            if change<=0 and self.toPay==0:
                raise negativeValueError
            if change<0:
                raise negativeValueError
        except negativeValueError:
            self.write("")
            self.screen.insert(0.0,"Za mało pieniędzy!\n")
        else:
            self.chosenTickets.clear()
            for key in self.cashTemp.keys():
                self.cashTemp[key]=0
            self.cashtempAmount=0
            self.toPay=0
            self.screen.delete(0.0, END)
            self.screen.insert(0.0, "Twoja reszta to:"+str(change)+"\n")
            self.buyTickets()
            self.viewcashtempAmount.set("Wrzucono:"+str(round(self.cashtempAmount,2))+" zł")
    def calculateChangeCard(self):
        try:
            change=self.cashtempAmount-self.toPay

            if self.toPay<=0:
                raise negativeValueError
        except negativeValueError:
            self.write("")
            self.screen.insert(0.0,"Wybierz najpierw bilet!\n")
        else:
            self.chosenTickets.clear()
            for key in self.cashTemp.keys():
                self.cashTemp[key]=0
            self.cashtempAmount=0
            self.toPay=0
            self.screen.delete(0.0, END)
            self.screen.insert(0.0, "\n")
            self.buyTickets()
            self.viewcashtempAmount.set("Wrzucono:"+str(round(self.cashtempAmount,2))+" zł")



    def write(self, text):
        self.viewedText=text
        self.toPay = round(self.toPay, 2)
        self.screen.delete(0.0, END)
        self.screen.insert(0.0,self.viewedText +"Wybrano bilety:"+str(self.chosenTickets)+ "\nDo Zapłaty: " + str(self.toPay) + " zl")

    def createWidgets(self):
        leftFrame = Frame(self)
        leftFrame.pack(side=LEFT, fill=Y)
        middleFrame = Frame(self)
        middleFrame.pack(side=LEFT, fill=Y)
        rightFrame = Frame(self)
        rightFrame.pack(side=LEFT, fill=Y)
        moneyFrame1 = Frame(self)
        moneyFrame1.pack(side=LEFT, fill=Y)
        moneyFrame2 = Frame(self)
        moneyFrame2.pack(side=RIGHT, fill=Y)

        self.master.title("Automat biletowy MPK")
        b_ticket1 = Button(leftFrame, text="Bilet normalny 20 min\n2,80zł", height=4, width=20, bg="gray65",
                           overrelief=GROOVE, command=lambda: self.addTicket(2.80))
        b_ticket1.pack(anchor=N)
        b_ticket2 = Button(middleFrame, text="Bilet ulgowy 20 min\n1,40zł", height=4, width=20, bg="gray65",
                           overrelief=GROOVE, command=lambda: self.addTicket(1.40))
        b_ticket2.pack(anchor=N)
        b_ticket3 = Button(leftFrame, text="Bilet normalny 40 min\n3,80zł", height=4, width=20, bg="gray75",
                           overrelief=GROOVE, command=lambda: self.addTicket(3.80))
        b_ticket3.pack(anchor=N)
        b_ticket4 = Button(middleFrame, text="Bilet ulgowy 40 min\n1,90zł", height=4, width=20, bg="gray75",
                           overrelief=GROOVE, command=lambda: self.addTicket(1.90))
        b_ticket4.pack(anchor=N)
        b_ticket5 = Button(leftFrame, text="Bilet normalny 60 min\n6,00zł", height=4, width=20, bg="gray85",
                           overrelief=GROOVE, command=lambda: self.addTicket(6.00))
        b_ticket5.pack(anchor=N)
        b_ticket6 = Button(middleFrame, text="Bilet ulgowy 60 min\n3,00zł", height=4, width=20, bg="gray85",
                           overrelief=GROOVE, command=lambda: self.addTicket(3.00))
        b_ticket6.pack(anchor=N)

        self.screen = Text(rightFrame, width=25, height=10, wrap=WORD)
        self.screen.pack(fill=Y, anchor=N)

        l_viewAmount=Label(rightFrame, textvariable=self.viewcashtempAmount)
        l_viewAmount.pack()

        b_returnMoney=Button(rightFrame, text="ZWRÓĆ PIENIĄDZE", height=2, width=20, bg="mint cream", overrelief=GROOVE,
                             command=lambda: self.returnMoney())
        b_returnMoney.pack(anchor=N)
        b_undoTicket=Button(rightFrame, text="COFNIJ BILET", height=2, width=20, bg="mint cream", overrelief=GROOVE,
                            command=lambda: self.undoTickets())
        b_undoTicket.pack(anchor=N)

        b_buyTicket=Button(rightFrame, text="KUP BILETY", height=2, width=20, bg="mint cream", overrelief=GROOVE,
                           command=lambda: self.calculateChange())
        b_buyTicket.pack(anchor=N)
        b_wallet= Button(moneyFrame1, image=self.photoW, overrelief=GROOVE, command=self.new_window)
        b_wallet.pack()






