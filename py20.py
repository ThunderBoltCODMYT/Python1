#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def add(a,b):
    c = a + b
    return c
def sub(a,b):
    c = a - b
    return c
def mul(a,b):
    c = a * b
    return c
def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    c = a / b
    return c
print("please select the operation to be performed")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter your choice (1/2/3/4): ")
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
if choice == '1':
    print(n1,"+",n2,"=", add(n1, n2))
elif choice == '2':
    print(n1,"-",n2,"=", sub(n1, n2))
elif choice == '3':
    print(n1,"*",n2,"=", mul(n1, n2))
elif choice == '4':
    print(n1,"/",n2,"=", div(n1, n2))
else:
    print("Invalid choice! Please select a valid operation.")
# End of code snippet
