import math
import json
import turtle as t
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import ImageGrab, Image


class FlowerApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Lanceolate Flower Generation")
        self.geometry("1400x800")
        self.resizable(False, False)

        self.turtle_frame: TurtleFrame = TurtleFrame(self)
        self.turtle: t.RawTurtle = self.turtle_frame.get_turtle()
        self.turtle_screen: t.TurtleScreen = self.turtle_frame.get_turtle_screen()

        self.menu: Menu = Menu(self, self.turtle, self.turtle_screen)

        self.set_turtle_settings()

        self.mainloop()

    def set_turtle_settings(self) -> None:
        """
        Set the turtle settings
        :return:
        """
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle_screen.colormode(255)
        self.turtle_screen.bgcolor((0, 0, 0))


class TurtleFrame(ttk.Frame):
    def __init__(self, parent: tk.Tk) -> None:
        super().__init__(parent)
        self.__canvas: tk.Canvas = tk.Canvas(self, width=800, height=800)
        self.__canvas.pack()
        self.__turtle_screen: t.TurtleScreen = t.TurtleScreen(self.__canvas)
        self.__turtle: t.RawTurtle = t.RawTurtle(self.__turtle_screen)
        self.place(x=0, y=0)

    def get_turtle(self) -> t.RawTurtle:
        """
        Return the turtle
        :return:
        """
        return self.__turtle

    def get_turtle_screen(self) -> t.TurtleScreen:
        """
        Return the turtle screen
        :return:
        """
        return self.__turtle_screen


class Menu(ttk.Frame):
    def __init__(self, parent: tk.Tk, tu: t.RawTurtle, screen: t.TurtleScreen) -> None:
        super().__init__(parent)

        self.tu: t.RawTurtle = tu
        self.__parent: tk.Tk = parent
        self.__turtle_screen: t.TurtleScreen = screen
        self.__layer_values: list[list[int | str]] = []

        ttk.Label(self, text="Flower settings", font=("Lucida Console", 20)).place(x=0, y=0)

        self.__help_text = ttk.Label(self, text="❔", font=("Lucida Console", 20))
        self.__help_text.place(x=550, y=5)
        self.__help_text.bind("<Button-1>", self.__open_help_panel)

        # ___________________________________Tree View___________________________________
        ttk.Label(self, text="Layer settings:", font=("Lucida Console", 15)).place(x=0, y=55)
        self.__layer_settings_frame: ttk.Frame = ttk.Frame(self)

        # Tree scrollbar
        self.tree_scroll: tk.Scrollbar = tk.Scrollbar(self.__layer_settings_frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Treeview
        self.layers_table: ttk.Treeview = ttk.Treeview(self.__layer_settings_frame, yscrollcommand=self.tree_scroll.set)
        self.layers_table.place(x=0, y=0, relwidth=0.95, relheight=1)

        # Tree settings
        self.layers_table["column"] = (
            "layer_id", "layer_length", "layer_height", "layer_color", "layer_fillcolor", "nb_petal", "lag")

        self.layers_table.column("#0", width=0, stretch=False)

        self.layers_table.column("layer_id", anchor=tk.CENTER, width=40)
        self.layers_table.heading("layer_id", text="ID", anchor=tk.CENTER)

        self.layers_table.column("layer_length", anchor=tk.CENTER, width=40)
        self.layers_table.heading("layer_length", text="Length", anchor=tk.CENTER)

        self.layers_table.column("layer_height", anchor=tk.CENTER, width=40)
        self.layers_table.heading("layer_height", text="Height", anchor=tk.CENTER)

        self.layers_table.column("layer_color", anchor=tk.CENTER, width=100)
        self.layers_table.heading("layer_color", text="Color", anchor=tk.CENTER)

        self.layers_table.column("layer_fillcolor", anchor=tk.CENTER, width=100)
        self.layers_table.heading("layer_fillcolor", text="Fill Color", anchor=tk.CENTER)

        self.layers_table.column("nb_petal", anchor=tk.CENTER, width=50)
        self.layers_table.heading("nb_petal", text="Petal Number", anchor=tk.CENTER)

        self.layers_table.column("lag", anchor=tk.CENTER, width=50)
        self.layers_table.heading("lag", text="Lag °", anchor=tk.CENTER)

        self.tree_scroll.config(command=self.layers_table.yview)

        self.__layer_settings_frame.place(x=0, y=105, relwidth=1, relheight=1 / 2)

        # ______________________________________________________________________________

        ttk.Label(self, text="Layer input:", font=("Lucida Console", 15)).place(x=0, y=525)

        ttk.Label(self, text="Length", font=("Lucida Console", 10)).place(x=0, y=565)
        ttk.Label(self, text="Height", font=("Lucida Console", 10)).place(x=90, y=565)
        ttk.Label(self, text="Color", font=("Lucida Console", 10)).place(x=180, y=565)
        ttk.Label(self, text="Fill color", font=("Lucida Console", 10)).place(x=300, y=565)
        ttk.Label(self, text="Nb petal", font=("Lucida Console", 10)).place(x=420, y=565)
        ttk.Label(self, text="Lag", font=("Lucida Console", 10)).place(x=510, y=565)

        self.__length_entry_var: tk.IntVar = tk.IntVar()
        self.__length_entry: ttk.Entry = ttk.Entry(self, textvariable=self.__length_entry_var)
        self.__length_entry.place(x=0, y=590, relwidth=0.15)

        self.__height_entry_var: tk.IntVar = tk.IntVar()
        self.__height_entry: ttk.Entry = ttk.Entry(self, textvariable=self.__height_entry_var)
        self.__height_entry.place(x=90, y=590, relwidth=0.15)

        self.__color_entry_var: tk.StringVar = tk.StringVar()
        self.__color_entry: ttk.Entry = ttk.Entry(self, textvariable=self.__color_entry_var)
        self.__color_entry.place(x=180, y=590, relwidth=0.2)

        self.__fillcolor_entry_var: tk.StringVar = tk.StringVar()
        self.__fillcolor_entry: ttk.Entry = ttk.Entry(self, textvariable=self.__fillcolor_entry_var)
        self.__fillcolor_entry.place(x=300, y=590, relwidth=0.2)

        self.__petal_number_entry_var: tk.IntVar = tk.IntVar()
        self.__petal_number_entry: ttk.Entry = ttk.Entry(self, textvariable=self.__petal_number_entry_var)
        self.__petal_number_entry.place(x=420, y=590, relwidth=0.15)

        self.__lag_entry_var: tk.IntVar = tk.IntVar()
        self.__lag_entry: ttk.Entry = ttk.Entry(self, textvariable=self.__lag_entry_var)
        self.__lag_entry.place(x=510, y=590, relwidth=0.13)

        self.__add_button: ttk.Button = ttk.Button(self, text="Add", command=self.__add_input)
        self.__add_button.place(x=0, y=620, relwidth=0.24)

        self.__modify_button: ttk.Button = ttk.Button(self, text="Modify", command=self.__modify_input)
        self.__modify_button.place(x=148, y=620, relwidth=0.24)

        self.__remove_button: ttk.Button = ttk.Button(self, text="Remove", command=self.__remove_input)
        self.__remove_button.place(x=296, y=620, relwidth=0.24)

        self.__clear_button: ttk.Button = ttk.Button(self, text="Clear", command=self.__clear_inputs)
        self.__clear_button.place(x=444, y=620, relwidth=0.24)

        # ______________________________________________________________________________

        ttk.Label(self, text="Pistil settings:", font=("Lucida Console", 15)).place(x=0, y=660)

        ttk.Label(self, text="Radius", font=("Lucida Console", 10)).place(x=0, y=690)
        ttk.Label(self, text="Color", font=("Lucida Console", 10)).place(x=197, y=690)
        ttk.Label(self, text="Fill color", font=("Lucida Console", 10)).place(x=394, y=690)

        self.pistil_radius_entry_var: tk.IntVar = tk.IntVar()
        self.__pistil_radius_entry = ttk.Entry(self, textvariable=self.pistil_radius_entry_var)
        self.__pistil_radius_entry.place(x=0, y=710, relwidth=0.3)

        self.pistil_color_entry_var: tk.StringVar = tk.StringVar()
        self.__pistil_color_entry = ttk.Entry(self, textvariable=self.pistil_color_entry_var)
        self.__pistil_color_entry.place(x=197, y=710, relwidth=0.3)

        self.pistil_fillcolor_entry_var: tk.StringVar = tk.StringVar()
        self.__pistil_fillcolor_entry = ttk.Entry(self, textvariable=self.pistil_fillcolor_entry_var)
        self.__pistil_fillcolor_entry.place(x=394, y=710, relwidth=0.3)

        # ______________________________________________________________________________

        self.__create_flower_button: ttk.Button = ttk.Button(self, text="Create Flower", command=self.create_flower)
        self.__create_flower_button.place(x=0, y=770, relwidth=0.23)

        self.__export_flower_button: ttk.Button = ttk.Button(self, text="Export Flower", command=self.__export_flower)
        self.__export_flower_button.place(x=147, y=770, relwidth=0.23)

        self.__import_flower_button: ttk.Button = ttk.Button(self, text="Import Flower", command=self.__import_flower)
        self.__import_flower_button.place(x=304, y=770, relwidth=0.23)

        self.__save_flower_button: ttk.Button = ttk.Button(self, text="Save Picture", command=self.__save_picture)
        self.__save_flower_button.place(x=451, y=770, relwidth=0.23)

        # ______________________________________________________________________________

        self.place(x=810, y=0, width=590, relheight=1)

    @staticmethod
    def __open_help_panel(callback) -> None:
        info_win = tk.Tk()
        info_win.title("Help Window")
        info_win.geometry("600x490")
        info_win.resizable(False, False)
        info_win.attributes('-topmost', 'true')

        ttk.Label(info_win, text="How to use the application ?", font=("Lucida Console", 20)).place(x=0, y=0)
        ttk.Label(info_win, text="Inputs:\n\nWhen an entry content is equal to 0, you need to write an integer.\n"
                                 "Otherwise, you need to write a RGB color (ex: 255,255,255).",
                  font=("Lucida Console", 11)).place(x=0, y=50)
        ttk.Label(info_win, text="Tree view:\n\nThe \"Add\" button append the tree view when all the entry\nare correct"
                                 ". Else, an error message will pop up.\nThe \"Remove\" button delete the selected "
                                 "tree view row.\nThe \"Modify\" button will change the content of the selected row by"
                                 "\nthe new entries content.\nFinally, the \"Clear\" button will "
                                 "delete all of the rows.",
                  font=("Lucida Console", 11)).place(x=0, y=150)
        ttk.Label(info_win, text="Flower:\n\nThe \"Create Flower\" button will create the turtle flower draw.\n"
                                 "The \"Export Flower\" button will create a export.json\nfile in the selected "
                                 "directory which contains all the flower\nsettings.\nThe \"Import Flower\" button will"
                                 " import the whole flower\nsettings of the selected json file.\nThe \"Save Picture\" "
                                 "button will take a screenshot of the turtle\nflower draw and save it in the selected "
                                 "directory.",
                  font=("Lucida Console", 11)).place(x=0, y=310)

        info_win.mainloop()

    def __check_valid_petal_entries(self) -> bool:
        """
        Check if the entries have a correct value inside
        :return:
        """
        length_val: int = self.__length_entry_var.get()
        height_val: int = self.__height_entry_var.get()
        color_val: str = self.__color_entry_var.get()
        fillcolor_val: str = self.__fillcolor_entry_var.get()
        petal_number_val: int = self.__length_entry_var.get()
        lag_val: int = self.__height_entry_var.get()
        if '' not in (color_val, fillcolor_val) \
                and (len(color_val.split(',')) and len(fillcolor_val.split(','))) == 3 \
                and (type(length_val) and type(height_val) and type(petal_number_val) and type(lag_val)) == int:
            return True
        else:
            messagebox.showerror("Input Error",
                                 "The values on the petal entries aren't correct.\n"
                                 "Click on the question mark button to see help")
            raise (ValueError("The values on the petal entries aren't correct"))

    def __check_valid_pistil_entries(self) -> bool:
        """
        Check if the entries have a correct value inside
        :return:
        """
        radius_val: int = self.pistil_radius_entry_var.get()
        color_val: str = self.pistil_color_entry_var.get()
        fillcolor_val: str = self.pistil_fillcolor_entry_var.get()

        if '' not in (color_val, fillcolor_val) \
                and type(radius_val) == int:
            return True
        else:
            messagebox.showerror("Input Error",
                                 "The values on the pistil entries aren't correct.\n"
                                 "Click on the question mark button to see help")
            raise (ValueError("The values on the pistil entries aren't correct"))

    def __add_input(self) -> None:
        """
        Add the item to the tree view
        :return:
        """
        if self.__check_valid_petal_entries():
            self.layers_table.insert(parent='', index="end", text='', values=(
                len(self.layers_table.get_children()), self.__length_entry_var.get(), self.__height_entry_var.get(),
                self.__color_entry_var.get(), self.__fillcolor_entry_var.get(), self.__petal_number_entry_var.get(),
                self.__lag_entry_var.get()))

    def __modify_input(self) -> None:
        """
        Modify the selected item in the tree view
        :return:
        """
        focussed: str = self.layers_table.focus()
        if focussed:
            if self.__check_valid_petal_entries():
                self.layers_table.item(focussed, values=(
                    self.layers_table.item(focussed)["values"][0], self.__length_entry_var.get(),
                    self.__height_entry_var.get(),
                    self.__color_entry_var.get(), self.__fillcolor_entry_var.get(), self.__petal_number_entry_var.get(),
                    self.__lag_entry_var.get()))

    def __remove_input(self) -> None:
        """
        Remove the selected item in the tree view
        :return:
        """
        if self.layers_table.focus():
            self.layers_table.delete(self.layers_table.focus())
            self.__actualize_table_ids()

    def __clear_inputs(self) -> None:
        """
        Clear the treeview
        :return:
        """
        for child in self.layers_table.get_children():
            self.layers_table.delete(child)

    def __actualize_table_ids(self) -> None:
        """
        Actualize the tree view ids
        :return:
        """
        for i, child in enumerate(self.layers_table.get_children()):
            child_item = self.layers_table.item(child)["values"]
            self.layers_table.item(child, values=(
                i, child_item[1], child_item[2], child_item[3], child_item[4], child_item[5], child_item[6]))

    def create_flower(self) -> None:
        """
        Create the flower
        :return:
        """
        self.tu.goto(0, 0)
        self.tu.setheading(0)
        self.tu.clear()
        if self.__check_valid_pistil_entries():
            create_flower(self)

    def __export_flower(self) -> None:
        """
        Export the flower settings as a json file
        :return:
        """
        folder_selected: str = filedialog.askdirectory()
        with open(f"{folder_selected}/export.json", "w+") as f:
            f.write("{")
            f.write(f"\n\t\"layers\": {len(self.layers_table.get_children())},")

            for i, child in enumerate(self.layers_table.get_children()):
                f.write(f'\n\t"layer_{i}": ')
                f.write(str(self.layers_table.item(child)["values"]).replace("'", '"'))
                f.write(",")

            f.write(f'\n\t"radius": {str(self.pistil_radius_entry_var.get())},')
            f.write(f'\n\t"color": "{str(self.pistil_color_entry_var.get())}",')
            f.write(f'\n\t"fillcolor": "{str(self.pistil_fillcolor_entry_var.get())}"')

            f.write("\n}")
            f.close()

    def __import_flower(self) -> None:
        """
        Import the flower settings from a json file
        :return:
        """
        file_selected: str = filedialog.askopenfilename(filetypes=[('JSON Files', '*.json')])
        data: any = json.loads(open(file_selected).read())

        for item in self.layers_table.get_children():
            self.layers_table.delete(item)

        for i in range(data["layers"]):
            self.layers_table.insert(parent='', index="end", text='', values=data[f"layer_{i}"])

        self.pistil_radius_entry_var.set(data["radius"])
        self.pistil_color_entry_var.set(data["color"])
        self.pistil_fillcolor_entry_var.set(data["fillcolor"])

    def __save_picture(self) -> None:
        """
        Take a screenshot of the turtle canvas
        :return:
        """
        folder_selected = filedialog.askdirectory()
        x0: int = self.__parent.winfo_rootx() + self.__turtle_screen.getcanvas().winfo_x() + 2
        y0: int = self.__parent.winfo_rooty() + self.__turtle_screen.getcanvas().winfo_y() + 2
        x1: int = x0 + self.__turtle_screen.getcanvas().winfo_width() - 4
        y1: int = y0 + self.__turtle_screen.getcanvas().winfo_height()
        screenshot: Image = ImageGrab.grab(bbox=(x0, y0, x1, y1))
        screenshot.save(f"{folder_selected}/turtle_screenshot.png")


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


def create_flower(menu: Menu) -> None:
    """
    Create the whole flower
    :param menu: Menu class to access to some values
    :return:
    """
    tu: t.RawTurtle = menu.tu
    layers_table: ttk.Treeview = menu.layers_table

    for child in layers_table.get_children():
        item = layers_table.item(child)
        petal_number: int = item["values"][5]
        petal_color_rgb: list[str] = item["values"][3].split(',')
        petal_fillcolor_rgb: list[str] = item["values"][4].split(',')
        for i in range(petal_number):
            tu.setheading(0)
            tu.left(i * (360 // petal_number) + item["values"][6])
            flower_petal(tu, item["values"][1], item["values"][2],
                         (int(petal_color_rgb[0]), int(petal_color_rgb[1]), int(petal_color_rgb[2])),
                         (int(petal_fillcolor_rgb[0]), int(petal_fillcolor_rgb[1]), int(petal_fillcolor_rgb[2])))

    pistil_radius: int = menu.pistil_radius_entry_var.get()
    pistil_color: list[str] = menu.pistil_color_entry_var.get().split(',')
    pistil_fillcolor: list[str] = menu.pistil_fillcolor_entry_var.get().split(',')

    tu.setheading(0)
    tu.forward(pistil_radius)
    tu.setheading(90)

    flower_pistil(tu, pistil_radius, (int(pistil_color[0]), int(pistil_color[1]), int(pistil_color[2])),
                  (int(pistil_fillcolor[0]), int(pistil_fillcolor[1]), int(pistil_fillcolor[2])))


if __name__ == '__main__':
    FlowerApp()
