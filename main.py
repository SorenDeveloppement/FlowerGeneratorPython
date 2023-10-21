import math
import turtle as t

t.speed(0)
t.colormode(255)
t.hideturtle()


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
    # centered_circle(0, 0, radius)
    t.circle(radius)
    t.end_fill()

    t.penup()


def create_flower() -> None:
    nb_petal1 = 12
    for i in range(nb_petal1):
        t.setheading(0)
        t.left(i * (360 // nb_petal1))
        flower_petal(250, (20, 20, 200), (50, 50, 255))

    for j in range(nb_petal1):
        t.setheading(0)
        alpha = (360 // nb_petal1)
        t.left(j * alpha + alpha / 2)
        flower_petal(150, (133, 31, 235), (153, 51, 255))

    nb_petal2 = 20
    for h in range(nb_petal2):
        t.setheading(0)
        t.left(h * (360 // nb_petal2))
        flower_petal(50, (31, 184, 235), (51, 204, 255))

    t.setheading(0)
    t.forward(15)
    t.setheading(90)

    flower_pistil(15, (255, 102, 255), (250, 197, 250))


create_flower()

t.mainloop()
