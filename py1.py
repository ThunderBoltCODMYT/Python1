#Write a program to calculate the sum of whole numbers.
n=int(input("Enter n: "))
sum=0
for x in range(1,n+1):
    sum=sum+x
    print("the Summation of ",n,"whole numbers = ",sum)