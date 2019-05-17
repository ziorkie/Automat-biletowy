from time import sleep
class Coin:
    def __init__(self):
        self.cashStash={"100":0, "50":5, "20":10, "10":10, "5":10, "2":50, "1":100,"0.50":200,"0.20":200,"0.10":200}
        self.cashtempAmount=0
        self.cashTemp = {"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0, "0.50": 0, "0.20": 0,"0.10":0}
    def throwMoney(self, key):

        self.cashStash[key] +=1
        self.cashtempAmount+=float(key)
        self.cashTemp[key] +=1

    def returnMoney(self):
        if self.cashtempAmount<=0:
            print("Nie wrzuciłeś pieniędzy!")
            raise ValueError()
        for k in self.cashTemp:
            self.cashStash[k]=self.cashStash[k]-self.cashTemp[k]
            self.cashTemp[k]=0
        self.cashtempAmount=0


    def throwMultiMoney(self, amount, key):
        try:
            if amount<=0:
                raise ValueError()
        except ValueError:
            print("Podaj dodatnią ilość monet!")
        else:
            for i in range(0, amount):
                print("huj")
                self.throwMoney(key)




    def getCashAmount(self):
        return self.cashtempAmount
    def getCashTemp(self):
        return self.cashTemp
    def getCashStash(self):
        return self.cashStash

#testy

test = Coin()
#test.throwMoney('1')
#test.throwMoney('10')
#test.throwMoney('0.10')
#print(test.getCashAmount())
#print(test.getCashTemp())
#print("\n", test.getCashStash())
#test.returnMoney()
#print(test.getCashAmount())
#print(test.getCashTemp())
#print("\n", test.getCashStash())
print("test multi")
test.throwMultiMoney(10, '100')
sleep(0.1)
print(test.getCashAmount())
print(test.getCashTemp())
print("\n", test.getCashStash())
test.returnMoney()
print(test.getCashAmount())
print(test.getCashTemp())
print("\n", test.getCashStash())