#Class Creation
class myClass:

    #private variable
    __privateVar, var = 27,20

    #private method
    def __privMeth(self):
        print("I'm inside class myClass")

    #Function to print value of private variable
    def hello(self):
        print("Private Variable value : ", myClass.__privateVar)

#Object creation and method call
foo = myClass()
foo.hello()
#foo.__privMeth()
foo.var=30
print(foo.var)
foo.__privateVar = 30
print(foo.__privateVar)