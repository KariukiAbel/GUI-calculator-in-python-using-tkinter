from tkinter import *
import parser

root = Tk()
root.title('Calculator')

# adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

# adding buttons to the calculator
Button(root, text="1").grid(row=2, column=0)
Button(root, text="2").grid(row=2, column=1)
Button(root, text="3").grid(row=2, column=2)

root.mainloop()
