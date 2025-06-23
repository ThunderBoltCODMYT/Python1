s1={6,9,1,6,2,0,2}
s1.add(40)
print('s1 : ',s1)

s2={2,4,0}
print('s2 : ',s2)

print(s1.difference(s2))# removes common elements from s1
print(s1.symmetric_difference(s2))#combine ele of s1 and then write common ele
print(s1.union(s2))#takes all the elements from both the sides
print(s1.intersection(s2))#only common elements