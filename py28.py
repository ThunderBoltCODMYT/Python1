try:
    n=int(input("Enter a number: "))
    print("The Number entered is ",n)
except ValueError as x:
    print("Exception: ",x)