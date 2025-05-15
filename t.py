#and-or operators
a,b,c,d=3,8,0,0
if a and b:
    print(a , "and" , b , "are true values")
elif a or b:
    print("Either" , a , "or" , b , "is true values")
else:
    print( a ,"and" , b , "both are false")

if b and c:
    print(b , "and" , c , "are true values")
elif b or c:
    print("Either" , b , "or" , c , "is true values")
else:
    print( b ,"and" , c , "both are false")

if d and c:
    print(d , "and" , c , "are true values")
elif d or c:
    print("Either" , d , "or" , c , "is true values")
else:
    print( d ,"and" , c , "both are false")

print("value of b = " , b , "and value of not b = " , not b)
print("value of c = " , c , "and value of not c = " , not c)