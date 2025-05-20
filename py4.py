#Power Calculator
#Write a program to calculate the n number power of a given number?
x=int(input("Enter the number : "))
y=int(input("Enter the power : "))
res=1
for i in range(1,y+1):
    res=res*x
print(res)