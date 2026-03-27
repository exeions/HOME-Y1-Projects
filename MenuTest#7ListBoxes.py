import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Combo and Spin")

# Combobox
items = ("Ice cream", "Pizza", "Broccoli")
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo["values"] = items
combo.pack()

# events
combo.bind("<<ComboboxSelected>>", lambda event: combo_label.config(text = f"Selected value: {food_string.get()}"))

combo_label = ttk.Label(window, text = "Select a value")
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
    window, 
    from_ = 3, 
    to = 20, 
    increment = 3,
    command = lambda: print(spin_int.get()),
    textvariable = spin_int)
spin.bind("<<Increment>>", lambda event: print("Up"))
spin.bind("<<Decrement>>", lambda event: print("Down"))
# spin["value"] = (1,2,3,4,5)
spin.pack()

## exercise:

letters = ("A", "B", "C", "D", "E")

spin_str = tk.StringVar(value = letters[0])
spinbox = ttk.Spinbox(window, textvariable = spin_str, values = letters)
spinbox.bind("<<Decrement>>", lambda event: print(spin_str.get()))
spinbox.pack()

window.mainloop()