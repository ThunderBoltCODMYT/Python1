#Write a program to reverse the string entered by the user.
s=input("enter a string: ")
rs=""
for ch in s:
    rs=ch+rs
    print("reverse of string ",s," is ",rs)
    