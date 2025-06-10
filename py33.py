#rock paper scissors game
import random as rd
points=0
while True:
    uchoice=input("Enter your choice [Rock(R),Paper(P),scissors(S)]: ")
    L=['R','P','S']
    cchoice=rd.choice(L)
    print("You chose: ",uchoice, "and computer chose: ",cchoice)
    if uchoice==cchoice:
        print("its a tie!")
    elif uchoice=='R':
        if cchoice=='S':
            print("You won!")
            points+=1
        else:
            print("You lost!")
            point-=1
    elif uchoice=='P':
        if cchoice=='R':
            print("You won!")
            points+=1
        else:
            print("You lost!")
            points-=1
        x=input("Do you wanna continue playing? [Y/N]: ")
        if x=='n' or x=='N':
            print("your score is: ", points)
            break