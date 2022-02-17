"""My doll's house drawn with turtle."""

__author__ = "730478408"

from turtle import Turtle, colormode, done
import turtle
colormode(255)


# Base of house:
def draw_house_base(base_turtle: Turtle, base_x: float, base_y: float, base_width: float) -> None:
    """Draw a square base for my house of using the given width with its top-left corner located at base_x, base_y."""
    base_z: list[int] = [1, 2, 3, 4]
    base_turtle.penup()
    base_turtle.goto(base_x, base_y) 
    base_turtle.setheading(0.0)
    base_turtle.pendown()
    base_turtle.pencolor(240, 160, 80)
    base_turtle.fillcolor(240, 160, 80)
    base_turtle.begin_fill()
    for a in base_z:
        base_turtle.forward(base_width)
        base_turtle.right(90)
    base_turtle.end_fill()
    draw_house_roof(base_turtle, "brown", 170)


def draw_house_roof(roof_turtle: Turtle, roof_color: str, roof_width: float) -> None:
    """Draw a triangualar roof for my house of using the given width with its top-left corner located at base_x, base_y."""
    roof_z: list[int] = [1, 2, 3]
    roof_turtle.color(roof_color)
    roof_turtle.begin_fill()
    for i in roof_z:
        roof_turtle.forward(roof_width)
        roof_turtle.left(120)
    roof_turtle.end_fill()


def draw_sky(sky_turtle: Turtle, sky_x: float, sky_y: float, sky_color: str, sky_width: float, sky_height: float) -> None:
    sky_z: list[int] = [1, 2]
    sky_turtle.penup()
    sky_turtle.goto(sky_x, sky_y)
    sky_turtle.pendown()
    sky_turtle.color(sky_color)
    sky_turtle.begin_fill()
    for i in sky_z:
        sky_turtle.forward(sky_width)
        sky_turtle.left(90)
        sky_turtle.forward(sky_height)
        sky_turtle.left(90)
    sky_turtle.end_fill()



def draw_door(door_turtle: Turtle, door_x: float, door_y: float, door_width: float, door_height: float) -> None:
    # Door
    door_turtle.penup()
    door_turtle.goto(door_x, door_y)
    door_turtle.pendown()
    door_turtle.right(90)
    door_turtle.color(138, 98, 74)
    door_turtle.begin_fill()
    i: int = 0
    while i < 2:
        door_turtle.forward(door_width)
        door_turtle.left(90)
        door_turtle.forward(door_height)
        door_turtle.left(90)
        i += 1
    door_turtle.end_fill()
    # door_turtle.goto(-40, -97)
    # door_turtle.forward(50)
    # door_turtle.left(90)
    # door_turtle.forward(80)
    # door_turtle.left(90)

    
def main() -> None:
    """The entrypoint of my scene."""
    my_turtle: Turtle = Turtle()
    turtle.Screen().bgcolor("green")
    draw_sky(my_turtle, -400, -100, "lightskyblue", 800, 500)
    draw_house_base(my_turtle, -100, -100, 170)
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    done()


# TODO: Define the procedures for other components in your scene here.
if __name__ == "__main__":
    main()