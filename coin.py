from time import sleep
from tkinter import *
from tkinter import messagebox
class negativeValueError(Exception):
    pass

class Coin:
    def __init__(self):
        self.cashStash={"100":0, "50":5, "20":10, "10":10, "5":10, "2":50, "1":100,"0.50":200,"0.20":200,"0.10":200}
        self.cashtempAmount=0
        self.cashTemp = {"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0, "0.50": 0, "0.20": 0,"0.10":0}
        self.viewcashtempAmount=StringVar()
        self.viewcashtempAmount.set("Wrzucono:"+str(round(self.cashtempAmount,2))+" zł")

    def throwMoney(self, key, amount):
        try:
            tmp=int(amount)
            if tmp<0:
                raise negativeValueError
        except negativeValueError:
            messagebox.showerror("Błąd!", "Podaj dodatnią wartość!")
        except ValueError:
            messagebox.showerror("Błąd!", "Podaj liczbę całkowitą!")
        else:
            for i in range (tmp):
                self.cashStash[key] +=1
                self.cashtempAmount+=float(key)
                self.cashTemp[key] +=1
                self.viewcashtempAmount.set("Wrzucono:"+str(round(self.cashtempAmount,2))+" zł")

    def returnMoney(self):
        try:
            if self.cashtempAmount<=0:

                raise negativeValueError
        except negativeValueError:
            messagebox.showerror("Błąd!","Nie wrzuciłeś pieniędzy!")
        else:
            for k in self.cashTemp:
                self.cashStash[k] = self.cashStash[k] - self.cashTemp[k]
                self.cashTemp[k] = 0
            self.cashtempAmount = 0
            self.viewcashtempAmount.set("Wrzucono:" + str(round(self.cashtempAmount, 2)) + " zł")



    def getCashAmount(self):
        return self.cashtempAmount
    def getCashTemp(self):
        return self.cashTemp
    def getCashStash(self):
        return self.cashStash
