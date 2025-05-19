#Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
U=input("Enter your ride preference: ")
if U.lower() == 'bike' :
    B = input("Enter the type of bike you prefer to ride: ")
    if B.lower() == 'sports' :
        print("You have selected a sports bike")
        print("it will cost you 150")
    elif B.lower() == 'cruiser' :
        print("You have selected a cruiser bike")
        print("it will cost you 200")
if U.lower() == 'car' :
    C = input("Enter the type of car you prefer to ride: ")
    if C.lower() == 'sedan' :
        print("You have selected a sedan car")
        print("it will cost you 350")
    elif C.lower() == 'suv' :
        print("You have selected an SUV car")
        print("it will cost you 500")
