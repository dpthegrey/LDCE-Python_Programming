import turtle

t = turtle.Turtle()
t.fillcolor('aqua')
t.begin_fill()

t.forward(100)  # draw base
for i in range(2):
    t.left(120)
    t.forward(100)
t.end_fill()
