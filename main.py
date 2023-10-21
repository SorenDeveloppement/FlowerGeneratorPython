import math
import turtle as t

t.speed(0)
t.colormode(255)


# t.hideturtle()


def centered_circle(x: int, y: int, radius: int | float) -> None:
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.forward(radius)
    t.setheading(90)
    t.pendown()

    p = 2 * math.pi * radius
    length = p / 360
    for i in range(360):
        t.forward(length)
        t.left(1)


def flower_petal(length: int, color: tuple[int, int, int] = (0, 0, 0),
                 fill_color: tuple[int, int, int] = (255, 255, 255)) -> None:
    t.pendown()

    t.pensize(2)
    t.color(color)
    t.fillcolor(fill_color)

    t.forward(length)

    t.begin_fill()
    rayon = 2 * length
    angle = math.degrees(length / (2 * rayon))
    t.left(180 - angle)
    t.circle(rayon, 2 * angle)

    t.left(180 - angle * 2)
    t.circle(rayon, 2 * angle)
    t.end_fill()

    t.left(180 - angle)
    t.forward(length)

    t.penup()


def flower_pistil(radius: int, color: tuple[int, int, int] = (0, 0, 0),
                  fill_color: tuple[int, int, int] = (255, 255, 255)) -> None:
    t.pendown()

    t.pensize(2)
    t.color(color)
    t.fillcolor(fill_color)

    t.begin_fill()
    centered_circle(0, 0, radius)
    t.end_fill()

    t.penup()


def create_flower() -> None:
    nb_petal = 12
    for i in range(nb_petal):
        t.setheading(0)
        t.left(i * (360 // nb_petal))
        flower_petal(250, (235, 235, 65), (255, 255, 75))

    t.setheading(0)
    t.forward(50)

    flower_pistil(15, (0, 255, 255), (255, 0, 255))


create_flower()

t.mainloop()
