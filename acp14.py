class BMW:
    def __init__(self,n,a):
        self.name=n
        self.mileage=a
    def info(self):
        print("Hey,this is BMW our cars are known for looks and Speed. My name is ",self.name , "and my mileage is ",self.age)

class Toyota:
    def __init__(self,n,a):
        self.name=n
        self.mileage=a
    def info(self):
        print("hey this is Toyota our cars are known for durability and reliability. My name is ",self.name , "and my mileage is ",self.mileage)

o1=BMW("BMW M5 Competition",2.5)
o1.info()

o2=Toyota("Toyota Supra MK-4",9)
o2.info()

for car in (o1, o2):
    car.info()
    car.sound()