from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
"""leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)"""
leo.color(255, 51, 249)
leo.penup()
leo.goto(0, 0)
leo.pendown()
leo.speed(50)
leo.begin_fill()
# code for shape to be filled 
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120) 
    i += 1
leo.end_fill()
leo.hideturtle()
done()