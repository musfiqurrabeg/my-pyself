import turtle as t

meow = t.Turtle()
screen = t.Screen()
meow.pensize(5)

def move_forward():
    meow.forward(10)

def move_back():
    meow.backward(10)

def turn_right():
    new_heading = meow.heading() - 10
    meow.setheading(new_heading)

def turn_left():
    new_heading = meow.heading() + 10
    meow.setheading(new_heading)

def clear():
    meow.clear()
    meow.penup()
    meow.home()
    meow.pendown()
    
screen.listen()
screen.onkey(key="w" , fun=move_forward)
screen.onkey(key="s" , fun=move_back)
screen.onkey(key="a" , fun=turn_left)
screen.onkey(key="d" , fun=turn_right)
screen.onkey(key="c" , fun=clear)
screen.exitonclick()


















