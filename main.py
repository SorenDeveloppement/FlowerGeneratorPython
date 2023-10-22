import math
import turtle as t
import tkinter as tk
from tkinter import ttk


class FlowerApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Lanceolate Flower Generation")
        self.geometry("1200x800")
        self.resizable = False

        self.turtle_frame = TurtleFrame(self)
        self.turtle = self.turtle_frame.get_turtle()
        self.turtle_screen = self.turtle_frame.get_turtle_screen()

        self.menu = Menu(self, self.turtle)

        self.set_turtle_settings()

        create_flower(self.turtle)

        self.mainloop()

    def set_turtle_settings(self) -> None:
        # self.turtle_screen.setworldcoordinates(1, 1, 0, 0)
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle_screen.colormode(255)
        self.turtle_screen.bgcolor((0, 0, 0))


class TurtleFrame(ttk.Frame):
    def __init__(self, parent: tk.Tk) -> None:
        super().__init__(parent)
        self.__canvas = tk.Canvas(self, width=800, height=800)
        self.__canvas.pack()
        self.__turtle_screen = t.TurtleScreen(self.__canvas)
        self.__turtle = t.RawTurtle(self.__turtle_screen)
        self.place(x=0, y=0, relwidth=2 / 3, relheight=1)

    def get_turtle(self) -> t.RawTurtle:
        return self.__turtle

    def get_turtle_screen(self) -> t.TurtleScreen:
        return self.__turtle_screen


class Menu(ttk.Frame):
    def __init__(self, parent: tk.Tk, tu: t.RawTurtle) -> None:
        super().__init__(parent)
        ttk.Label(self, background="blue").pack(expand=True, fill="both")
        self.place(x=800, y=0, relwidth=1 / 3, relheight=1)


def flower_petal(tu: t.RawTurtle, length: int, color: tuple[int, int, int] = (0, 0, 0),
                 fill_color: tuple[int, int, int] = (255, 255, 255)) -> None:
    """
    Draw a flower petal wit a lanceolate shape
    :param tu: The turtle raw screen
    :param length: Length of the petal
    :param color: Outline color of the flower petal
    :param fill_color: Fill color of the flower petal
    :return:
    """
    tu.pendown()

    # Set pen settings
    tu.pensize(2)
    tu.color(color)
    tu.fillcolor(fill_color)

    tu.forward(length)

    # Draw the left petal section
    tu.begin_fill()
    rayon = 2 * length
    angle = math.degrees(length / (2 * rayon))
    tu.left(180 - angle)
    tu.circle(rayon, 2 * angle)

    # Draw the right petal section
    tu.left(180 - angle * 2)
    tu.circle(rayon, 2 * angle)
    tu.end_fill()

    # Draw the central vein of the petal
    tu.left(180 - angle)
    tu.forward(length)

    tu.penup()


def flower_pistil(tu: t.RawTurtle, radius: int, color: tuple[int, int, int] = (0, 0, 0),
                  fill_color: tuple[int, int, int] = (255, 255, 255)) -> None:
    """
    Draw a flower pistil

    :param tu: The turtle raw screen
    :param radius: Radius of the pistil
    :param color: Outline color of the pistil
    :param fill_color: Fill color of the pistil
    :return:
    """
    tu.pendown()

    # Set pen settings
    tu.pensize(2)
    tu.color(color)
    tu.fillcolor(fill_color)

    # Draw the pistil circle
    tu.begin_fill()
    tu.circle(radius)
    tu.end_fill()

    tu.penup()


def create_flower(tu: t.RawTurtle) -> None:
    """
    Create the whole flower
    :param tu: The turtle raw screen
    :return:
    """
    nb_petal1 = 12
    for i in range(nb_petal1):
        tu.setheading(0)
        tu.left(i * (360 // nb_petal1))
        flower_petal(tu, 250, (20, 20, 200), (50, 50, 255))

    for j in range(nb_petal1):
        tu.setheading(0)
        alpha = (360 // nb_petal1)
        tu.left(j * alpha + alpha / 2)
        flower_petal(tu, 150, (133, 31, 235), (153, 51, 255))

    nb_petal2 = 20
    for h in range(nb_petal2):
        tu.setheading(0)
        tu.left(h * (360 // nb_petal2))
        flower_petal(tu, 50, (31, 184, 235), (51, 204, 255))

    # Reset the position of the turtle
    tu.setheading(0)
    tu.forward(15)
    tu.setheading(90)

    flower_pistil(tu, 15, (255, 102, 255), (250, 197, 250))


# create_flower()
FlowerApp()

# Create the mainloop of the window
# t.mainloop()
