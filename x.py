#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
U=int(input("Enter the number of units consumed: "))
if U<50:
    cost=U*2.60
    tax=25
elif U<100:
    cost=U*3.25
    tax=35
elif U<200:
    cost=U*5.26
    tax=45
else:
    cost=U*8.45
    tax=75
bill_amount = cost + tax
print("Your electricity bill is: ", bill_amount)