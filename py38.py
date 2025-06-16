#lists in python
L=[]#Empty List
print(L)
L=list()#empty list
print(L)

#list of numbers
L=[9,1,20,9,3,5,9,20,2]
print(L[2])
print(L[2:7])

L=[9,1,2,9,3,5,9,20,2]
print(L.count(1))
print(L.count(9))

#add ele
L.append(30)
print(L)
L.extend([6,1,9])
print(L)
L.insert(2,100)
print(L)


#remove ele
x=L.pop(2)
print(L)
print(x)

L.remove(2)
print(L)

L.clear()
print(L)

L=[9,1,2,9,3,5,9,20,2]
L.reverse()
print(L)

L.sort()
print(L)
L.sort(reverse=True)
print(L)
