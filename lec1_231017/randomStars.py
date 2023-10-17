import turtle as t
import random

t.bgcolor("black")
t.pensize(2)
t.pencolor("yellow")
t.speed(500) # 0.5초


for k in range(30):
    t.penup()
    x= random.randint(-350,350)
    y = random.randint(0, 350)
    starsize= random.randint(10,30)
    t.goto(x,y)
    t.pendown()
    for i in range(5):
        t.forward(starsize)
        t.right(144)

t.mainloop()