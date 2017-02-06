# -*- coding: utf8 -*-
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

john = turtle.Turtle()
john.pensize(3)
john.color("hotpink")
size = 50

def draw_square(t, size):
        for i in range(4):
                t.forward(size)
                t.left(90)
               


for i in range(10):
    draw_square(john, 50)
    size = size + 100
    john.penup()
    john.left(315)
    john.forward(30)
    john.pendown()


window.exitonclick()             # 等待使用者關閉視窗
