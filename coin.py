class Coin:
    def __init__(self):
        self.cashStash={"100":0, "50":5, "20":10, "10":10, "5":10, "2":50, "1":100,"0.50":200,"0.20":200,"0.10":200}
        self.cashtempAmount=0
        self.cashTemp = {"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0, "0.50": 0, "0.20": 0,"0.10":0}
    def throwMoney(self, key):
        self.cashStash[key] +=1
        self.cashtempAmount+=float(key)
        self.cashTemp[key] +=1

    def returnMoney(self, key):
        if  self.cashtempAmount<=0:
            print("Nie wrzuciłeś pieniędzy!")
            raise ValueError()

    def getCashAmount(self):
        return self.cashtempAmount
    def getCashTemp(self):
        return self.cashTemp
    def getCashStash(self):
        return self.cashStash



test = Coin()
test.throwMoney('1')
test.throwMoney('10')
test.throwMoney('0.10')
print(test.getCashAmount())
print(test.getCashTemp())
print("\n", test.getCashStash())
