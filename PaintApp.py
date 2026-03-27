import tkinter as tk
from tkinter import ttk

def draw_on_screen(event):
    x = event.x
    y = event.y
    selected_name = colour_value.get()
    actual_colour = colours[selected_name]
    paintWindow.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = actual_colour, outline = actual_colour)

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4
    
    brush_size = max(0, min(brush_size, 50))


window = tk.Tk()
window.title("Simple Paint App")
window.geometry("600x400")

paintWindow = tk.Canvas(window, bg = "white", width = 500, height = 300)
paintWindow.pack()

brush_size = 2
paintWindow.bind("<B1-Motion>", draw_on_screen)
paintWindow.bind("<MouseWheel>", brush_size_adjust)

colours = {
    "Black": "black",
    "Red": "red",
    "Blue": "blue",
    "Yellow": "yellow",
    "Eraser": "white"
}

colour_value = tk.StringVar(value = "Black")
combo = ttk.Combobox(window, values = list(colours.keys()), textvariable = colour_value)
combo.pack()

label = ttk.Label(window, text = "Paint you foid", foreground = "black", font = "Times 24 bold")
label.pack()

window.mainloop()