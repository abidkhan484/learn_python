import turtle

t = turtle.Turtle()
m = turtle.Screen()

def spiral(t, length):
    if length:
        t.forward(length)
        t.left(90)

        spiral(t, length-2)

spiral(t, 100)
m.exitonclick()
