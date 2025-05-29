import turtle
sc=turtle.Screen()
sc.setup(1000,1000)
sc.bgcolor("white")
sc.title("Welcome to turtle window")
T=turtle.Turtle()
colors=["red", "green", "blue", "pink", "orange", "yellow"]
T.speed('fastest')
T.hideturtle()
while True:
    i=0
    for x in range(200):
        T.pencolor(colors[i])
        if i<(len(colors)-1):
            i+=1
        else:
            i=0
        T.width(x/100 + 1)
        T.forward(x)
        T.left(59)