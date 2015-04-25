from Tkinter import *
from ScrolledText import *
from lexical import *

def construct():

    def callback():
        input = inputBox.get(1.0, END)
        output = lexical(input)
        displayBox.configure(state=NORMAL)
        displayBox.delete(1.0, END)
        displayBox.insert(INSERT, output)
        displayBox.configure(state=DISABLED)


    master = Tk()
    master.title("C- Compiler")

    # Labels
    Label(master, text="Input").grid(row=0, column=0)
    Label(master, text="Output").grid(row=0, column=1)

    # Buttons
    lexButton = Button(master, text='LEX', command=callback)
    lexButton.grid(row=1, column=1)

    # Text Boxes
    inputBox = ScrolledText(master, width=50, height=40)
    inputBox.grid(row=2, column=0)
    displayBox = ScrolledText(master, width=50, height=40)
    displayBox.grid(row=2, column=1)
    displayBox.configure(state=DISABLED)

    master.mainloop()