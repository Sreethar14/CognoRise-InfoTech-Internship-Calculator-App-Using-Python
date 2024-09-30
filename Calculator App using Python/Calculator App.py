# Importing necessary libraries
from tkinter import *

# Creating the GUI window
window = Tk()
window.title("Calculator App")

# Global variable to store the current math expression
expression = ""

# Function to update the expression variable
def update_expression(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the math expression
def evaluate():
    global expression
    try:
        result = eval(expression)
        equation.set(result)
        expression = str(result)
    except Exception as e:
        equation.set("Error")
        expression = ""

# Function to clear the calculator
def clear():
    global expression
    expression = ""
    equation.set("")

# Creating the entry field for displaying the math expression
equation = StringVar()
entry_field = Entry(window, textvariable=equation, width=20)
entry_field.grid(row=0, column=0, columnspan=4)

# Creating number buttons
button_1 = Button(window, text="1", command=lambda: update_expression(1))
button_1.grid(row=1, column=0)
button_2 = Button(window, text="2", command=lambda: update_expression(2))
button_2.grid(row=1, column=1)
button_3 = Button(window, text="3", command=lambda: update_expression(3))
button_3.grid(row=1, column=2)

button_4 = Button(window, text="4", command=lambda: update_expression(4))
button_4.grid(row=2, column=0)
button_5 = Button(window, text="5", command=lambda: update_expression(5))
button_5.grid(row=2, column=1)
button_6 = Button(window, text="6", command=lambda: update_expression(6))
button_6.grid(row=2, column=2)

button_7 = Button(window, text="7", command=lambda: update_expression(7))
button_7.grid(row=3, column=0)
button_8 = Button(window, text="8", command=lambda: update_expression(8))
button_8.grid(row=3, column=1)
button_9 = Button(window, text="9", command=lambda: update_expression(9))
button_9.grid(row=3, column=2)

button_0 = Button(window, text="0", command=lambda: update_expression(0))
button_0.grid(row=4, column=0)

# Creating operator buttons
button_add = Button(window, text="+", command=lambda: update_expression("+"))
button_add.grid(row=1, column=3)
button_subtract = Button(window, text="-", command=lambda: update_expression("-"))
button_subtract.grid(row=2, column=3)
button_multiply = Button(window, text="*", command=lambda: update_expression("*"))
button_multiply.grid(row=3, column=3)
button_divide = Button(window, text="/", command=lambda: update_expression("/"))
button_divide.grid(row=4, column=3)

button_equals = Button(window, text="=", command=evaluate)
button_equals.grid(row=4, column=2)
button_clear = Button(window, text="C", command=clear)
button_clear.grid(row=4, column=1)

# Starting the GUI event loop
window.mainloop()