from Tkinter import *
from ScrolledText import *
from lexical import *

def construct():

    def callback():
        input = inputBox.get(1.0, END)
        message, output = lexical(input)
        displayBox.configure(state=NORMAL)
        displayBox.delete(1.0, END)
        displayBox.insert(INSERT, message + output)
        displayBox.configure(state=DISABLED)

    def callback2():
        input = inputBox.get(1.0, END)
        message, output = lexical(input)
        displayBox.configure(state=NORMAL)
        displayBox.delete(1.0, END)
        displayBox.insert(INSERT, message)
        displayBox.configure(state=DISABLED)

    def callback3():
        print 'Semantics'

    master = Tk()
    master.title("C- Compiler")

    # Frames
    buttonFrame = Frame(master)
    buttonFrame.grid(row=1, column=1)

    # Labels
    Label(master, text="Input").grid(row=0, column=0)
    Label(master, text="Output").grid(row=0, column=1)

    # Buttons
    lexButton = Button(buttonFrame, text='Lexical', command=callback)
    lexButton.grid(row=0, column=0)
    syntaxButton = Button(buttonFrame, text="Syntax", command=callback2)
    syntaxButton.grid(row=0, column=1)
    semanticsButton = Button(buttonFrame, text='Semantics', command=callback3)
    semanticsButton.grid(row=0, column=2)
    semanticsButton.configure(state=DISABLED)

    # Text Boxes
    inputBox = ScrolledText(master, width=50, height=40)
    inputBox.grid(row=2, column=0)
    displayBox = ScrolledText(master, width=50, height=40)
    displayBox.grid(row=2, column=1)
    displayBox.configure(state=DISABLED)

    master.mainloop()