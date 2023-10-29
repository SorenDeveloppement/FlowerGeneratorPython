import math
import turtle as t
import tkinter as tk
from tkinter import ttk


# TODO: Create an export flower function that return a base64 string with whole of the flower settings


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

        self.__layer_values: list[list[int | str]] = []

        ttk.Label(self, text="Flower settings", font=("Lucida Console", 20)).place(x=0, y=0)

        ttk.Label(self, text="Petal layers:", font=("Lucida Console", 15)).place(x=0, y=55)
        self.__petal_layers_int = tk.IntVar()
        self.__petal_layers_int.set(3)
        self.__petal_layers = ttk.Entry(self, width=10, textvariable=self.__petal_layers_int, validate="focusout",
                                        validatecommand=self.__check_valid_entry)
        self.__petal_layers.place(x=0, y=80)

        # ----------------------------------------------------------------------------------
        ttk.Label(self, text="Layer settings:", font=("Lucida Console", 15)).place(x=0, y=125)
        self.__layer_settings_frame = ttk.Frame(self)
        self.__layer_settings_frame.place(x=0, y=155, relwidth=1, relheight=2 / 3)

        self.__frame_canvas = tk.Canvas(self.__layer_settings_frame)

        self.__frame_scrollbar = ttk.Scrollbar(self.__layer_settings_frame, orient="vertical",
                                               command=self.__frame_canvas.yview)

        self.__frame_canvas.config(yscrollcommand=self.__frame_scrollbar.set)

        self.__create_scrollpane_content(self.__petal_layers_int.get())
        # ----------------------------------------------------------------------------------

        self.place(x=800, y=0, relwidth=1 / 3, relheight=1)

    def __check_valid_entry(self):
        assert self.__petal_layers_int.get() != ""
        if int(self.__petal_layers_int.get()) >= 10:
            raise ValueError("You must enter an integer value !")
        else:
            self.__create_scrollpane_content(self.__petal_layers_int.get())
        return True

    def __create_scrollpane_content(self, layer_number: int):
        self.__layer_values.clear()
        self.__frame_canvas.delete("all")

        self.__canvas_frame = ttk.Frame(self.__frame_canvas)
        self.__frame_canvas.grid()
        self.__frame_canvas.bind("<Configure>",
                                 lambda e: self.__frame_canvas.configure(scrollregion=self.__frame_canvas.bbox("all")))
        self.__frame_canvas.create_window((0, 0), anchor="nw", window=self.__canvas_frame, width=400)
        self.__frame_scrollbar.grid(row=0, column=1, sticky="ns")

        for i in range(0, layer_number * 8, 8):
            ttk.Label(self.__canvas_frame, text=f"Layer {i // 8 + 1}:", font=("Lucida Console", 15)).grid(row=i * 2)
            ttk.Label(self.__canvas_frame, text=f"Length:", font=("Lucida Console", 10)).grid(row=i * 2 + 1)
            ttk.Entry(self.__canvas_frame, width=30).grid(row=i * 2 + 2)
            ttk.Label(self.__canvas_frame, text=f"Height:", font=("Lucida Console", 10)).grid(row=i * 2 + 3)
            ttk.Entry(self.__canvas_frame, width=30).grid(row=i * 2 + 4)
            ttk.Label(self.__canvas_frame, text=f"Color:", font=("Lucida Console", 10)).grid(row=i * 2 + 5)
            ttk.Entry(self.__canvas_frame, width=30).grid(row=i * 2 + 6)
            ttk.Label(self.__canvas_frame, text=f"Fill color:", font=("Lucida Console", 10)).grid(row=i * 2 + 7)
            ttk.Entry(self.__canvas_frame, width=30).grid(row=i * 2 + 8)


def flower_petal(tu: t.RawTurtle, length: int, height: int, color: tuple[int, int, int] = (0, 0, 0),
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
    # Calculation of the radius : (c² + t²) / 2 * t
    # Where c is the half of the chord length and t is the length of the arrow of the arc
    rayon: float = ((length / 2) ** 2 + height ** 2) / (2 * height)
    # Calculation of the angle : 2 * asin(/R)
    # Where c is the half of the chord length and R the radius of the circle
    angle: float = math.degrees(2 * math.asin((length / 2) / rayon))
    tu.pendown()

    # Set pen settings
    tu.pensize(2)
    tu.color(color)
    tu.fillcolor(fill_color)

    tu.forward(length)

    # Draw the left petal section
    tu.begin_fill()
    tu.left(180 - angle / 2)
    tu.circle(rayon, angle)

    # Draw the right petal section
    tu.left(180 - angle)
    tu.circle(rayon, angle)
    tu.end_fill()

    # Draw the central vein of the petal
    tu.left(180 - angle / 2)
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
        flower_petal(tu, 250, 15, (20, 20, 200), (50, 50, 255))

    for j in range(nb_petal1):
        tu.setheading(0)
        alpha = (360 // nb_petal1)
        tu.left(j * alpha + alpha / 2)
        flower_petal(tu, 150, 15, (133, 31, 235), (153, 51, 255))

    nb_petal2 = 20
    for h in range(nb_petal2):
        tu.setheading(0)
        tu.left(h * (360 // nb_petal2))
        flower_petal(tu, 50, 5, (31, 184, 235), (51, 204, 255))

    # Reset the position of the turtle
    tu.setheading(0)
    tu.forward(15)
    tu.setheading(90)

    flower_pistil(tu, 15, (255, 102, 255), (250, 197, 250))


# create_flower()
FlowerApp()

# Create the mainloop of the window
# t.mainloop()
