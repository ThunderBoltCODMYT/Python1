#tuples
#empty tuple
T=()
print(T)
T=tuple()
print(T)

#single element
T=(30)
print(T,type(T))
T=(30,)
print(T,type(T))

T=(30)#not a tuple but it is a number
print(T,type(T))


#Tuple with many elements
T=(6,1,8,1,2,9,10)#tuple : immutable non changeable
L=[6,1,8,1,2,9,10]#list : mutable changeable
L[2]=100
print(L)

T[2]=100 #will give error

T=(6,1,8,1,2,9,10)
print(sum(T))
print(max(T))
print(min(T))

t=(5,7,4)
a,b,c=t
print(b)
T=1,a,2,0,2,c
print(T)
#create list from tuple
#method 1
L=list(T)

#method 2
L=[]
for x in T:
    L.append(x)