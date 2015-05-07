from main import *
from Tkinter import *
from ScrolledText import *
from lexical import lexical
from syntax import syntax
from semantic import semantic
import ttk


def construct():

    sample_prog = '''int main (void)
{
    int x;
    int y;

    x = 1 * (2 + 3);
    y = x + 1;

    return x + y;
}'''

    def callback():

        input = inputBox.get(1.0, END)

        # Lexical tab
        message, output, tokens = lexical(input)
        lexTab = tabs['Lexical']
        lexTab.configure(state=NORMAL)
        lexTab.delete(1.0, END)
        lexTab.insert(INSERT, message + output)
        lexTab.configure(state=DISABLED)

        # Syntax tab
        message, output, root, syn_pass = syntax(tokens)
        synTab = tabs['Syntax']
        synTab.configure(state=NORMAL)
        synTab.delete(1.0, END)
        synTab.insert(INSERT, message + output)
        synTab.configure(state=DISABLED)

        # Semantics tab
        if syn_pass:
            message = semantic(root)
        else:
            message = "Couldn't perform semantic analysis"
        semTab = tabs['Semantics']
        semTab.configure(state=NORMAL)
        semTab.delete(1.0, END)
        semTab.insert(INSERT, message)
        semTab.configure(state=DISABLED)

    master = Tk()
    master.title("C- Compiler")

    # Frames
    buttonFrame = Frame(master)
    buttonFrame.grid(row=1, column=1)

    # Labels
    Label(master, text="Input").grid(row=0, column=0)
    Label(master, text="Output").grid(row=0, column=1)

    # Buttons
    compileButton = Button(buttonFrame, text='Compile', command=callback)
    compileButton.grid(row=0, column=0)

    # Text Boxes
    inputBox = ScrolledText(master, width=50, height=40)
    inputBox.grid(row=2, column=0)
    inputBox.insert(INSERT, sample_prog)

    # Notebook to hold tabs
    notebook = ttk.Notebook(master)
    notebook.grid(row=2, column=1)
    tabs = {"Lexical": [], "Syntax": [], "Semantics": []}
    tab_order = ["Lexical", "Syntax", "Semantics"]

    for tabname in tab_order:
        tab = ScrolledText(notebook, width=50, height=40)
        tab.configure(state=DISABLED)
        tabs[tabname] = tab
        notebook.add(tab, text=tabname)

    master.mainloop()