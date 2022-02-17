"""My doll's house drawn with turtle."""

__author__ = "730478408"

from turtle import Turtle, colormode, tracer, update, done
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
    """Add a beautiful blue sky to beautify my scene using the given width and height with its top-left corner located at sky_x, sky_y."""
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


def draw_sun(sun_turtle: Turtle, sun_x: float, sun_y: float, sun_radius: float) -> None: 
    """Place a bright circular sun in my sky using the radius sun_radius with its top-left corner located at sun_x, sun_y."""""
    sun_turtle.penup()
    sun_turtle.goto(sun_x, sun_y)
    sun_turtle.pendown()
    sun_turtle.color(255, 215, 0)
    sun_turtle.begin_fill()
    sun_turtle.circle(sun_radius)
    sun_turtle.end_fill()
    # sun_turtle.goto(-320, 225)
    # sun_turtle.circle(35)


def draw_first_window(first_window_turtle: Turtle, first_window_x: float, first_window_y: float, first_window_width: float) -> None:
    """Draw a window in my house using the given width with its top-left corner located at first_window_x, first_window_y."""
    first_window_turtle.penup()
    first_window_turtle.goto(first_window_x, first_window_y)
    first_window_turtle.pendown()
    first_window_turtle.color("black", "white")
    first_window_turtle.begin_fill()
    i: int = 0
    while i < 4:
        first_window_turtle.forward(first_window_width)
        first_window_turtle.left(90)
        i += 1
    first_window_turtle.end_fill()


def draw_second_window(second_window_turtle: Turtle, second_window_x: float, second_window_y: float, second_window_width: float) -> None:
    """Draw another window in my house using the given width with its top-left corner located at second_window_x, second_window_y."""
    second_window_turtle.penup()
    second_window_turtle.goto(second_window_x, second_window_y)
    second_window_turtle.pendown()
    second_window_turtle.right(90)
    second_window_turtle.color("black", "white")
    second_window_turtle.begin_fill()
    i: int = 0
    while i < 4:
        second_window_turtle.forward(second_window_width)
        second_window_turtle.left(90)
        i += 1
    second_window_turtle.end_fill()
    #  window_turtle.goto(-80, 0)
    #  window_turtle.forward(50)
    #  window_turtle.left(90)


def draw_half_cloud(cloud_turtle: Turtle, cloud_x: float, cloud_y: float, cloud_m: float, cloud_n: float, cloud_radius: float) -> None:
    """A function I will repeat by calling twice at different points to draw two halves of my cloud that form a complete shape."""
    cloud_turtle.penup()
    cloud_turtle.goto(cloud_x, cloud_y)
    cloud_turtle.pendown()
    cloud_turtle.color("white")
    cloud_turtle.begin_fill()
    cloud_turtle.circle(cloud_radius)
    cloud_turtle.end_fill()
    cloud_turtle.penup()
    cloud_turtle.goto(cloud_m, cloud_n)
    cloud_turtle.pendown()
    cloud_turtle.begin_fill()
    cloud_turtle.circle(cloud_radius)
    cloud_turtle.end_fill()
    # 1stcloud_turtle.goto(200, 200)
    # 1stcloud_turtle.circle(25)
    # cloud_turtle.goto(220, 240)
    # cloud_turtle.circle(25)


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    my_turtle: Turtle = Turtle()
    my_turtle.speed(50)
    turtle.Screen().bgcolor("green")
    turtle.title("Ann's Doll House")
    draw_sky(my_turtle, -400, -100, "lightskyblue", 800, 500)
    draw_sun(my_turtle, -320, 225, 35)
    draw_half_cloud(my_turtle, 200, 200, 220, 240, 25)
    draw_half_cloud(my_turtle, 230, 215, 180, 220, 25)
    draw_house_base(my_turtle, -100, -100, 170)
    draw_first_window(my_turtle, -40, -100, -50)
    draw_second_window(my_turtle, 10, -100, 50)
    my_turtle.hideturtle()
    update()
    done()


# TODO: Define the procedures for other components in your scene here.
if __name__ == "__main__":
    main()