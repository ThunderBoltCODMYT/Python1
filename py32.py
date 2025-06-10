#Number Game
import random as rd
x=True
n=str(rd.randint(10,20))
print("I will generate a number from 10 to 20 and you will have to guess it")
print("the game ends when you have one hero!")
c=0
while x:
    c+=1
    g=input("give me your best guess: ")
    if n==g:
        print("You have won the game in ",c," attempts")
        print("the number was ",n)
        break
    else:
        print("You lost the game..Try Again \n\n")

