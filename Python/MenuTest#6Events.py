import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x: {event.x} y: {event.y}")

window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = "A button")
button.pack()

# events
# button.bind("<Alt-KeyPress-a>", lambda event: print(event))
# window.bind("<KeyPress>", lambda event: print(f"a button was pressed ({event.char})"))

# window.bind("<Motion>", get_pos)

entry.bind("<FocusIn>", lambda event: print("entry field was selected"))
entry.bind("<FocusOut>", lambda event: print("entry field was unselected"))

text.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

window.mainloop()