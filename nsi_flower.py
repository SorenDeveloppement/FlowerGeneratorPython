import math
import turtle as t

t.speed(0)
t.colormode(255)
t.hideturtle()
t.bgcolor("black")


def flower_petal(length: int, height: int, color: tuple[int, int, int] = (0, 0, 0),
                 fill_color: tuple[int, int, int] = (255, 255, 255)) -> None:
    """
    Draw a flower petal wit a lanceolate shape
    :param tu: The turtle raw screen
    :param length: Length of the petal
    :param height: Arrow of the arc
    :param color: Outline color of the flower petal
    :param fill_color: Fill color of the flower petal
    :return:
    """
    # Calculate the radius and the angle of the angle of the arc
    rayon: float = ((length / 2) ** 2 + height ** 2) / (2 * height)
    angle: float = math.degrees(2 * math.asin((length / 2) / rayon))
    t.pendown()

    # Set pen settings
    t.pensize(2)
    t.color(color)
    t.fillcolor(fill_color)

    t.forward(length)

    # Draw the left petal section
    t.begin_fill()
    t.left(180 - angle / 2)
    t.circle(rayon, angle)

    # Draw the right petal section
    t.left(180 - angle)
    t.circle(rayon, angle)
    t.end_fill()

    # Draw the central vein of the petal
    t.left(180 - angle / 2)
    t.forward(length)

    t.penup()


def flower_pistil(radius: int, color: tuple[int, int, int] = (0, 0, 0),
                  fill_color: tuple[int, int, int] = (255, 255, 255)) -> None:
    """
    Draw a flower pistil
    :param radius: Radius of the pistil
    :param color: Outline color of the pistil
    :param fill_color: Fill color of the pistil
    :return:
    """
    t.pendown()

    # Set pen settings
    t.pensize(2)
    t.color(color)
    t.fillcolor(fill_color)

    # Draw the pistil circle
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    t.penup()


def create_flower() -> None:
    """
    Create the whole flower
    :return:
    """
    nb_petal1 = 12
    for i in range(nb_petal1):
        t.setheading(0)
        t.left(i * (360 // nb_petal1))
        flower_petal(250, 15, (20, 20, 200), (50, 50, 255))

    for j in range(nb_petal1):
        t.setheading(0)
        alpha = (360 // nb_petal1)
        t.left(j * alpha + alpha / 2)
        flower_petal(150, 15, (133, 31, 235), (153, 51, 255))

    nb_petal2 = 20
    for h in range(nb_petal2):
        t.setheading(0)
        t.left(h * (360 // nb_petal2))
        flower_petal(50, 5, (31, 184, 235), (51, 204, 255))

    # Reset the position of the turtle
    t.setheading(0)
    t.forward(15)
    t.setheading(90)

    flower_pistil(15, (255, 102, 255), (250, 197, 250))


create_flower()

# Create the mainloop of the window
t.mainloop()
