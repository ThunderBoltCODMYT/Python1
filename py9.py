#Write a program to print all the prime numbers which come in the range entered by the user?
n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))
for n in range(n1,n2+1):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
