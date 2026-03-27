import tkinter as tk
from tkinter import ttk
from tkinter import *

def button_func():
    entry_text = entry.get()

    label["text"] = entry_text
    entry["state"] = "disabled"

def reset_text():
    label["text"] = "Some text"
    entry["state"] = "enabled"
    entry.delete(0, END)

window = tk.Tk()
window.title("Getting and setting widgets")

label = ttk.Label(master = window, text = "Some text")

entry = ttk.Entry(master = window)

button = ttk.Button(master = window, text = "Click Me!", command = button_func)

button2 = ttk.Button(master = window, text = "Reset", command = reset_text)

label.pack()
entry.pack()
button.pack()
button2.pack()

window.mainloop()