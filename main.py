'''
Author: Matthew Boatright
Project: C- Compiler
'''

from Tkinter import *
from ScrolledText import *

def main():
    print

    master = Tk()

    Label(master, text="First").grid(row=0)
    Label(master, text="Second").grid(row=1)

    textPad = ScrolledText(master, width=50, height=40)
    e2 = Entry(master)
    e2.config(state=DISABLED)

    textPad.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    master.mainloop()

if __name__ == '__main__':
    main()