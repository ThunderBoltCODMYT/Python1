class cat:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print("Hey i am a cat my name is ",self.name , "and my age is ",self.age)
    def sound(self):
        print("I say meow")
class dog:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print("Hey i am a dog my name is ",self.name , "and my age is ",self.age)
    def sound(self):
        print("I bark loudly")
class lion:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def info(self):
        print("Hey i am a lion my name is ",self.name , "and my age is ",self.age)
    def sound(self):
        print("I roar loudly")
o1=cat("Mini",2.5)
o1.info()
o1.sound()

o2=dog("Dodo",6)
o2.info()
o2.sound()

o3=lion("Kenz",9)
o3.info()
o3.sound()

for animal in (o1, o2, o3):
    animal.info()
    animal.sound()