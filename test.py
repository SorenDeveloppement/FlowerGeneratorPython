from tkinter import ttk
import tkinter as tk


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


def __create_scrollpane_content(self, layer_number: int):
    self.__layer_values.clear()
    if self.__frame_canvas:
        self.__frame_canvas.destroy()

    self.__frame_canvas = tk.Canvas(self.__layer_settings_frame)

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
