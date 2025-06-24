#Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary
x=[1,9,3]
y=['x','y','z']
z=list(zip(x,y))
print(z)

L1=[10,20,30,40]
L2=[100,200,300,400]
for x,y in zip(L1,L2[::-1]):
    print(x,y)
names=["Pranav","Priyank",'Durga','Sam','Dev']
percent=[80,71,53,92,68,40]
Di={names:percent for names,percent in zip(names,percent)}
print(Di)
