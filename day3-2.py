import turtle
fu=turtle.Turtle()
ck=turtle.Screen()
ck.bgcolor("white")
fu.color("black")
fu.shape("turtle")
for c in range(5):  
    for c in range(4):  
        fu.forward(100)
        fu.left(90)
        fu.circle(100)
    fu.right(90)
    for c in range(4):  
        fu.forward(100)
        fu.left(90)
        fu.circle(100)