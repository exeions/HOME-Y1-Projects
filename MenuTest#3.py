import tkinter as tk
from tkinter import ttk
from tkinter import *

def button_func():
    print(string_var.get())
    string_var.set("button pressed")

window = tk.Tk()
window.title("Tkinter Variables")

string_var = tk.StringVar(value = "start value")
string_var2 = tk.StringVar(value = "test")

label = ttk.Label(master = window, text = "label", textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = "button", command = button_func)
button.pack()

entry2 = ttk.Entry(master = window, textvariable = string_var2)
entry2.pack()

entry3 = ttk.Entry(master = window, textvariable = string_var2)
entry3.pack()

label2 = ttk.Label(master =  window, textvariable = string_var2)
label2.pack()

window.mainloop()