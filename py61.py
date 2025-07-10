class Computer:
    def __init__(self):
        self.__maxprice = 900
        self.cprice = 700
    def sell(self):
        print("Selling Price : ",self.__maxprice)
        print("Cost Price : ",self.cprice)

    def setMaxPrice(self , sprice , cprice):
        self.__maxprice = sprice
        self.cprice = cprice

c = Computer()
c.sell()

#Change the price
c.__maxprice = 1000
c.cprice = 2000
c.sell()

#using setter function
c.setMaxPrice(1000, 2000)
c.sell()