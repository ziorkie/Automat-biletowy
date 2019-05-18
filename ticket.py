from tkinter import *
from tkinter import messagebox
class negativeValueError(Exception):
    pass

class Tickets:

    def __init__(self):
        self.toPay=0
        self.ticket = {1.40: "20 minutowy ulgowy", 2.80:"20 minutowy normalny", 1.90:"40 minutowy ulgowy", 3.80:"40 minutowy normalny", 3.00:"60 minutowy ulgowy", 6.00:"60 minutowy normalny"}
        self.chosenTickets = []

    def addTickets(self, key):
        self.chosenTickets.append(key)
        self.toPay+=key
        return self.chosenTickets

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
            return self.chosenTickets
