from tkinter import *
from tkinter import messagebox
class negativeValueError(Exception):
    pass

class Tickets:

    def __init__(self):
        self.toPay=0
        self.ticket = {1.40: "20 minutowy ulgowy", 2.80:"20 minutowy normalny", 1.90:"40 minutowy ulgowy", 3.80:"40 minutowy normalny", 3.00:"60 minutowy ulgowy", 6.00:"60 minutowy normalny"}
        self.chosenTickets = []
        self.viewToPay = StringVar()
        self.viewToPay.set("Do zapłaty:" + str(round(self.toPay, 2)) + " zł")

    def addTickets(self, key, amount):
        try:
            tmp=int(amount)
            if tmp<0:
                raise negativeValueError
        except negativeValueError:
            messagebox.showerror("Błąd!", "Podaj dodatnią wartość!")
        except ValueError:
            messagebox.showerror("Błąd!", "Podaj liczbę całkowitą!")
        else:
            for i in range(tmp):
                self.chosenTickets.append(key)
                self.toPay+=key
                self.viewToPay.set("Do zapłaty:" + str(round(self.toPay, 2)) + " zł")
                #return self.chosenTickets

    def undoTicket(self):
        try:
            tempLen = len(self.chosenTickets) - 1
            if tempLen<0:
                raise negativeValueError
        except negativeValueError:
            messagebox.showerror("Błąd!", "Brak biletów do wycofania!")
        else:
            lastVal = self.chosenTickets[tempLen]
            self.chosenTickets.pop()
            self.toPay -= lastVal
            self.viewToPay.set("Do zapłaty:" + str(round(self.toPay, 2)) + " zł")
            return self.chosenTickets
