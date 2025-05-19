#Write a program to check if the persons age is between 10 to 20  
U=input("Enter your age: ")
if U.lower():
    U=int(U)
    if U>=10 and U<=20:
        print("Your age is between 10 to 20")
    else:
        print("Your age is not between 10 to 20")