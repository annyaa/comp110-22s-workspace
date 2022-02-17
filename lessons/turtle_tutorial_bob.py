from turtle import Turtle, colormode, done
colormode(255)
bob: Turtle = Turtle()
bob.color(16, 14, 16)
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.speed(75)
bob.begin_fill()
# code for shape to be filled 
i: int = 0
while i < 3:
    bob.forward(300)
    bob.left(120) 
    i += 1    
bob.end_fill()

j: int = 0
bob.color(16, 14, 16)
bob.penup()
bob.goto(-180, -120)
bob.pendown()
bob.speed(75)
# code for shape to be filled 
while j < 3:
    bob.forward(300)
    bob.left(120) 
    j += 1    

side_length: int = 300
j: int = 0
bob.color(16, 14, 16)
bob.penup()
bob.goto(-180, -120)
bob.pendown()
bob.speed(75)
# code for shape to be filled 
while j < 10:
    side_length = side_length * 0.965
    bob.forward(side_length)
    bob.left(121.5) 
    j += 1 
done()