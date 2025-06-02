from tkinter import *

window = Tk()
window.geometry("310x280")
window.title("Calculator")

entrybox = Entry(window, width=45, borderwidth=3)
entrybox.place(x=10,y=0)

def click(num):
    result = entrybox.get()
    entrybox.delete(0, END)
    entrybox.insert(0, str(result)+ str(num))

# BUTTONS
b = Button(window, text="1", width=10, command=lambda : click(1))
b.place(x=10,y=40)
b = Button(window, text="2", width=10, command=lambda : click(2))
b.place(x=110,y=40)
b = Button(window, text="3", width=10, command=lambda : click(3))
b.place(x=210,y=40)

b = Button(window, text="4", width=10, command=lambda : click(4))
b.place(x=10,y=80)
b = Button(window, text="5", width=10, command=lambda : click(5))
b.place(x=110,y=80)
b = Button(window, text="6", width=10, command=lambda : click(6))
b.place(x=210,y=80)

b = Button(window, text="7", width=10, command=lambda : click(7))
b.place(x=10,y=120)
b = Button(window, text="8", width=10, command=lambda : click(8))
b.place(x=110,y=120)
b = Button(window, text="9", width=10, command=lambda : click(9))
b.place(x=210,y=120)
b = Button(window, text="0", width=10, command=lambda : click(0))
b.place(x=110,y=160)

def add():
    n1 = entrybox.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    entrybox.delete(0, END)


b = Button(window, text="+", width=10, command=add)
b.place(x=10,y=160)


def subtract():
    n1 = entrybox.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    entrybox.delete(0, END)


b = Button(window, text="-", width=10, command=subtract)
b.place(x=210,y=160)


def multiply():
    n1 = entrybox.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    entrybox.delete(0, END)

b = Button(window, text="*", width=10, command=multiply)
b.place(x=10,y=200)

def divide():
    n1 = entrybox.get()
    global math
    math = "division"
    global i
    i = int(n1)
    entrybox.delete(0, END)

b = Button(window, text="/", width=10, command= divide)
b.place(x=110,y=200)

def equal():
    n2 = entrybox.get()
    entrybox.delete(0, END)
    if math == "addition":
        entrybox.insert(0,i + int(n2))
    elif math == "subtraction":
        entrybox.insert(0,i - int(n2))
    elif math == "multiplication":
        entrybox.insert(0,i * int(n2))
    elif math == "division":
        entrybox.insert(0,i / int(n2))


b = Button(window, text="=", width=10, command=equal)
b.place(x=210,y=200)

def clear():
    entrybox.delete(0, END)


b = Button(window, text="Clear", width=30, command=clear)
b.place(x=30,y=240)


mainloop()
