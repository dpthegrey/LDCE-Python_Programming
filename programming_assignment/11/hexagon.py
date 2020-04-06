import turtle

t = turtle.Turtle()
t.fillcolor('orange')
t.begin_fill()
for i in range(6):
    t.forward(150)
    t.right(60)
t.end_fill()
