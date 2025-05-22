#Write a program to check if the number entered by the user is an Armstrong number or not?
n=int(input("Enter number n : "))
sum=0
m=n
while n!=0:
    r=n%10
    sum=sum+r*r*r
    n=n//10
if m==sum:
    print(m,"is armstrong number")
else:
    print(m,"is not armstrong number")