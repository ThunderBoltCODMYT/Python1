try:
    n1,n2=eval(input("Enter two numbers seperated by a comma: "))
    res=n1/n2
    print("res is ",res)
except SyntaxError:
    print("Comma is missing")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("this will execute independent of exception")
