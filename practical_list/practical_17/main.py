data = ""
from tkinter import *


# display the clicked button data

def OnClick(number):
    global data
    data = data + str(number)
    Operands.set(data)


# clearing the display

def Clear():
    global data
    data = ''
    Operands.set(data)


# evalating the final result

def Equals():
    global data
    data = eval(data)
    Operands.set(data)


# layout


root = Tk()

Operands = StringVar()

s = Entry(root, textvariable=Operands)
s.grid(row=0, columnspan=4)

b1 = Button(root, text='7', command=lambda: OnClick(7))
b1.grid(row=1)

b2 = Button(root, text='8', command=lambda: OnClick(8))
b2.grid(row=1, column=1)

b3 = Button(root, text='9', command=lambda: OnClick(9))
b3.grid(row=1, column=2)

b4 = Button(root, text='4', command=lambda: OnClick(4))
b4.grid(row=2)

b5 = Button(root, text='5', command=lambda: OnClick(5))
b5.grid(row=2, column=1)

b6 = Button(root, text='6', command=lambda: OnClick(6))
b6.grid(row=2, column=2)

b7 = Button(root, text='1', command=lambda: OnClick(1))
b7.grid(row=3)

b8 = Button(root, text='2', command=lambda: OnClick(2))
b8.grid(row=3, column=1)

b9 = Button(root, text='3', command=lambda: OnClick(3))
b9.grid(row=3, column=2)

b0 = Button(root, text='0', command=lambda: OnClick(0))
b0.grid(row=4, column=1)

c = Button(root, text='C', command=Clear)
c.grid(row=4)

e = Button(root, text='=', command=Equals)
e.grid(row=4, column=2)

a = Button(root, text='+', command=lambda: OnClick('+'))
a.grid(row=1, column=3)

s = Button(root, text='-', command=lambda: OnClick('-'))
s.grid(row=2, column=3)

m = Button(root, text='*', command=lambda: OnClick('*'))
m.grid(row=3, column=3)

d = Button(root, text='/', command=lambda: OnClick('/'))
d.grid(row=4, column=3)

root.mainloop()
