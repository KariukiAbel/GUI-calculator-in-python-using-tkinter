from tkinter import *
import parser

root = Tk()
root.title('Calculator')

#adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)


root.mainloop()
