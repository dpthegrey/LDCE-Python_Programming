from tkinter import *
from random import choice
top = Tk()
top.title("background color")
C = Canvas(top, height=250, width=400)
button1 = Button(top, text="red", anchor=W,
                 command=lambda: C.configure(bg="red"))
button1.configure(width=10, activebackground="red", relief=FLAT)

button2 = Button(top, text="blue", anchor=W,
                 command=lambda: C.configure(bg="blue"))
button2.configure(width=10, activebackground="blue", relief=FLAT)

button3 = Button(top, text="green", anchor=W,
                 command=lambda: C.configure(bg="green"))
button3.configure(width=10, activebackground="green", relief=FLAT)


button1_window = C.create_window(10, 10, anchor=NW, window=button1)
button2_window = C.create_window(50, 10, anchor=NW, window=button2)
button3_window = C.create_window(100, 10, anchor=NW, window=button3)
C.pack()
top.mainloop()
