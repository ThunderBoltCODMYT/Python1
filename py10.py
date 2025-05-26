#Write a program to calculate the product of the middle digits of a number?
n=int(input("Enter a number: "))
t=n
L=0
while t>0:
    L=L+1
    t=t//10
if L>=4:
    L=L//2
    c=0
    while n>0:
        r=n%10
        if c==L:
            m1=r
        elif c==(L-1):
            m2=r
        n=n//10
        c=c+1
        p=m1*m2
        print("product of mid digits=",p)
else:
    print("Number isn't Valid")
        
        
  
