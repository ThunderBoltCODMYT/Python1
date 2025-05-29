import turtle
sc=turtle.Screen()
sc.setup(400,300)
sc.bgcolor("pink")
sc.title("Welcome to turtle window")
T=turtle.Turtle()
print("Enter your choice: /n 1. Square /n 2. triangle /n 3. Octagon /n 4.hexagon")
choice=int(input("Enter your choice: "))
if choice== 1:
    for i in range(4):
        T.forward(100)
        T.right(360/4)
elif choice== 2:
    for i in range(3):
        T.forward(100)
        T.right(360/3)
elif choice== 3:
    for i in range(8):
        T.forward(100)
        T.right(360/8)
elif choice== 4:
    for i in range(6):
        T.forward(100)
        T.right(360/6)
else:
    print("Invalid Choice")
sc.exitonclick()