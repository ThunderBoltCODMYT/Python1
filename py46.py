#Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
n1 =[1,2,3]
n2=[4,5,6]
res=map(lambda x,y:x+y,n1,n2)
print("Addition of two lists : ")
print(list(res))

#using the map() function
n=[3,9,1,2]
def sq(n):
    return n*n;
x=list(map(sq,n))
print("square of number in list : /n ",x)
