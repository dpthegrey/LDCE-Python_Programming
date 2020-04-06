from tkinter import *

root = Tk(className="button_click_label")
root.geometry("200x200")

message = StringVar()
message.set('hi')

l1 = Label(root, text="hi")
l1.pack()


def press():
    l1.config(text="hello")


b1 = Button(root, text="clickhere", command=press).pack()

root.mainloop()
