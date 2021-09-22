"""Create Notepad using Tkinter."""

from tkinter import *
from tkinter import messagebox
from tkinter.constants import END, NONE


def YesClick():
    global Name
    Name = str(FileName.get()) + ".txt"
    save = open(str(Name), "a")
    save.write(text_area.get("1.0", END))
    text_area.delete("1.0", END)
    new_win.destroy()


def SaveClick():
    global Name
    Name = str(FileName.get()) + ".txt"
    save = open(str(Name), "w")
    save.write(text_area.get("1.0", END))
    new_win.destroy()


def NewSheet():
    ans = messagebox.askyesno("Question:", "Do you wish to save the file?")
    if ans:
        global new_win
        new_win = Tk()
        new_win.title("Enter file Name")
        new_win.geometry("200x80")
        Label(new_win, text="Enter the file Name").pack()
        global FileName
        FileName = Entry(new_win)
        FileName.pack(pady=10)
        Button(new_win, text="Yes", command=YesClick).pack()
    else:
        text_area.delete("1.0", END)


def SaveFile():
    global new_win
    new_win = Tk()
    new_win.title("Enter file name")
    new_win.geometry("200x80")
    Label(new_win, text="Enter the file name").pack()
    global FileName
    FileName = Entry(new_win)
    FileName.pack(pady=10)
    Button(new_win, text="Yes", command=SaveClick).pack()


root = Tk()
root.title("Simple Notepad")
root.geometry("1280x720")

ribbon = Menu(root)
root.config(menu=ribbon)

ribbon.add_cascade(label="New", command=lambda: NewSheet())
ribbon.add_cascade(label="Save", command=lambda: SaveFile())
ribbon.add_cascade(label="Exit", command=root.quit())

scroll = Scrollbar(root)
scroll.pack(side="right", fill="y")

text_area = Text(root, yscrollcommand=scroll.set, font=("Arial", 12))
text_area.pack(fill="both", expand="true")

scroll.config(command=text_area.yview)

root.mainloop()



