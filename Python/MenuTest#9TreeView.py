import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from random import choice

window = ttk.Window(themename = "darkly")
window.geometry("600x400")
window.title("Treeview")

first_names = ["Bob", "Maria", "Alex", "James", "Susan", "Henry", "Lisa", "Anna", "Lisa"]
last_names = ["Smith", "Brown", "Wilson", "Thomson", "Cook", "Taylor", "Walker", "Clark"]

# treeview
table = ttk.Treeview(window, columns = ("first", "last", "email"), show = "headings")
table.heading("first", text = "First name")
table.heading("last", text = "Surname")
table.heading("email", text = "Email")
table.pack(fill = "both", expand = True)

# insert values into a table
#table.insert(parent = "", index = 0, values = ("John", "Doe", "JohnDoe@gmail.com"))

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f"{first[0]}{last}@gmail.com"
    data = (first, last, email)
    table.insert(parent = "", index = 0, values = data)

table.insert(parent = "", index = tk.END, values = ("XXXXX", "YYYYY", "ZZZZZ"))

def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)["values"])
    #table.item(table.selection())

def delete_items(_):
    print("deleted")
    for i in table.selection():
        table.delete(i)

def add_items(_):
    def add_item():
        name = Entry1.get()
        last = Entry2.get()
        email = Entry3.get()
        if name and last and email:
            table.insert(parent = "", index = tk.END, values = (name, last, email))
            newWindow.destroy()
        else:
            print("Please fill out all 3 fields.")

    
    newWindow = ttk.Toplevel(window)
    newWindow.title("Add Items")
    newWindow.geometry("300x220")
    newWindow

    label = ttk.Label(newWindow, text = "Add Items", font = "Arial 16 bold")
    label.pack()

    label2 = ttk.Label(newWindow, text = "Type name here")
    label2.pack()

    Entry1 = ttk.Entry(newWindow)
    Entry1.pack()

    label3 = ttk.Label(newWindow, text = "Type surname here")
    label3.pack()

    Entry2 = ttk.Entry(newWindow)
    Entry2.pack()

    label4 = ttk.Label(newWindow, text = "Type email here")
    label4.pack()

    Entry3 = ttk.Entry(newWindow)
    Entry3.pack()

    my_style = ttk.Style()
    my_style.configure("success.TButton", font=("Helvetica", 10), padding=(4, 1))

    button = ttk.Button(newWindow, text = "Add Values", bootstyle = "success", style = "success.TButton", command = add_item)
    button.pack(pady=5)



table.bind("<<TreeviewSelect>>", item_select)
table.bind("<Delete>", delete_items)
window.bind("<Control-f>", add_items)

window.mainloop()