#Write a program to demonstrate a right angle triangle pattern?
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
for i in range(1,r+1):
    for j in range(1,c+1):
        print('*',end=" ")
    print()
