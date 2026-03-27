import tkinter as tk
from tkinter import ttk

def button_func(string):
    print("a button was pressed")
    print(string.get())

def outer_func(parameter):
    def inner_func():
        print("a button was pressed")
        print(parameter.get())
    return inner_func

window = tk.Tk()
window.title("buttons, functions and arguments")

entry_string = tk.StringVar(value = "test")
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

button = ttk.Button(window, text = "button", command = lambda: button_func(entry_string))
button.pack()

window.mainloop()