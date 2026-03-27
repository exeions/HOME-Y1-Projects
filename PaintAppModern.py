import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

## TIME - IN FUNCTION FOR LINE DELAY - LESS LAG
import time
last_time = 0

## FUNCTIONS
def on_press(event):
    canvas.lastx, canvas.lasty = event.x, event.y

def on_drag(event):
    global last_time
    now = time.time()
    if now - last_time > 0.01:
        x, y = event.x, event.y
        line = canvas.create_line(canvas.lastx, canvas.lasty, x, y, width = brush_size, fill = selected.get(), capstyle = tk.ROUND, smooth = True)
        lines.append(line)
        canvas.lastx, canvas.lasty = x, y
        last_time = now

def adjust_brush_size(event):
    global brush_size
    global last_time
    now = time.time()

    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4
    
    brush_size = max(0, min(brush_size, 500))
    
    x, y = canvas.winfo_pointerx() - canvas.winfo_rootx(), canvas.winfo_pointery() - canvas.winfo_rooty()

    if now - last_time > 0.2:
        temp_brush = canvas.create_oval(x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2, outline = "gray", width = 2)
        window.after(200, lambda: canvas.delete(temp_brush))
        last_time = now

def adjust_brush_colour(_):
    colourConfigWindow = ttk.Toplevel(window)
    colourConfigWindow.title("Adjust Brush Colour")
    colourConfigWindow.geometry("250x75")

    title = ttk.Label(colourConfigWindow, text = "Pick colour from dropdown: ")
    title.pack()
    
    selection = ttk.Combobox(colourConfigWindow, values = list(colours.keys()), textvariable = selected, state="readonly")
    selection.pack()

    selection._colour = selected

    if selection["values"]:
        selection.current(0)

    selection.update_idletasks()

    selectedLabel = ttk.Label(colourConfigWindow)
    selectedLabel.config(text = f"Selected colour: {selected.get()}")
    selection.bind("<<ComboboxSelected>>", lambda event: selectedLabel.config(text = f"Selected colour: {selected.get()}"))
    selectedLabel.pack()

def canvas_clear(_):
    for i in lines:
        canvas.delete(i)

## WINDOW ROOT
window = tk.Tk()
window.title("Modern Paint App")
window.geometry("600x400")

## LINES
lines = []

## COLOURS
colours = {
    "Black": "black",
    "Red": "red",
    "Green": "green",
    "Blue": "blue",
    "Yellow": "yellow"
}

## INTERNAL VARIABLES
brush_size = 5

## TK VARIABLES
selected = tk.StringVar(value = "Black")

## CANVAS WIDGET
canvas = tk.Canvas(window, bg = "white")
canvas.pack(fill = "both", expand = True)

control_text = "PRESS F4 FOR CLEAR\nPRESS F5 FOR COLOUR OPTIONS"
canvas.create_text(10, 10, text = control_text, anchor = "nw", font = ("Arial", 12), fill = "black")

## EVENTS
canvas.bind("<ButtonPress-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<MouseWheel>", adjust_brush_size)
window.bind("<KeyPress-F5>", adjust_brush_colour)
window.bind("<KeyPress-F4>", canvas_clear)

## RUN
window.mainloop()
