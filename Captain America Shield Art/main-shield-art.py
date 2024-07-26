import turtle as t

galu = t. Turtle()
win = t.Screen()
win.bgcolor("black")
galu.color("white")
galu.speed("fast")

galu.begin_fill()
galu.color("red")
galu.penup()
galu.setposition(10, -400)
galu.pendown()
galu.circle(350)
galu.end_fill()

galu.begin_fill()
galu.color("white")
galu.penup()
galu.setposition(10, -350)
galu.pendown()
galu.circle(300)
galu.end_fill()

galu.begin_fill()
galu.color("red")
galu.penup()
galu.setposition(10, -290)
galu.pendown()
galu.circle(233)
galu.end_fill()

galu.begin_fill()
galu.color("blue")
galu.penup()
galu.setposition(10, -210)
galu.pendown()
galu.circle(150)
galu.end_fill()


galu.penup()
galu.setposition(-25, 0)
galu.pendown()
galu.begin_fill()
galu.color("white")


for i in range(5):
    galu.left(60)
    galu.forward(100)
    galu.right(133)
    galu.forward(100)

galu.end_fill()
win.exitonclick()