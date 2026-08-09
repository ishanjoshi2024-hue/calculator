import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.geometry("300x400")



def calculate(operator):

    num1 = float(entry1.get())
    num2 = float(entry2.get())

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    resultlabel.config(text="Result = " + str(result))


# Title
title = tk.Label(
    root,
    text="Simple Calculator",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)


# First number
entry1 = tk.Entry(root)
entry1.pack(pady=10)


# Second number
entry2 = tk.Entry(root)
entry2.pack(pady=10)


# Buttons
add = tk.Button(
    root,
    text="+",
    width=10,
    command=lambda: calculate("+")
)
add.pack(pady=5)


sub = tk.Button(
    root,
    text="-",
    width=10,
    command=lambda: calculate("-")
)
sub.pack(pady=5)


multiply = tk.Button(
    root,
    text="*",
    width=10,
    command=lambda: calculate("*")
)
multiply.pack(pady=5)


divide = tk.Button(
    root,
    text="/",
    width=10,
    command=lambda: calculate("/")
)
divide.pack(pady=5)


# Result
resultlabel = tk.Label(
    root,
    text="Result = ",
    font=("Arial", 14)
)

resultlabel.pack(pady=20)


root.mainloop()