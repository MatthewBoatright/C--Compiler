from Tkinter import *
from ScrolledText import *

def construct():
    master = Tk()
    master.title("C- Compiler")

    # Labels
    Label(master, text="Input").grid(row=0, column=0)
    Label(master, text="Output").grid(row=0, column=1)

    # Buttons
    lexButton = Button(master, text='LEX').grid(row=1, column=1)

    # Text Boxes
    inputBox = ScrolledText(master, width=50, height=40)
    displayBox = ScrolledText(master, width=50, height=40)
    displayBox.configure(state=DISABLED)

    inputBox.grid(row=2, column=0)
    displayBox.grid(row=2, column=1)

    master.mainloop()