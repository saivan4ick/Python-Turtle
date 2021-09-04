# Радужная анимация завихрения

import turtle

colors = ['red', 'blue', 'purple', 'green',
          'orange', 'yellow']

t = turtle.Pen()
turtle.bgcolor('black')
t.hideturtle()

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
