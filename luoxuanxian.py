#luoxuanxian.py
import turtle
turtle.setup(400,400,400,400)
turtle.pensize(2)
turtle.bgcolor("black")
colors = ['red', 'yellow', 'purple', 'blue','orange','green']
for i in range(300):
    turtle.forward(2*i)
    turtle.color(colors[i % 6])
    turtle.left(59)
done()
