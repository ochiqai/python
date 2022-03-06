import time
import turtle as t
import math


t.shape("turtle")
t.pensize(5)
t.pencolor("green")

h_katta = 100
h_kichik = 50
h_dumli = 50

masofa = 10


t.speed(100)
# O harfi
def o_harf():
    t.circle(50)
    t.penup()

# c harfi
def c_harf():
    t.goto(masofa + 100, 50)
    t.pendown()
    t.right(180)
    for _ in range(3 * 23):
        t.forward(1.1)
        t.left(2.5)
    t.penup()

# h harfi
def h_harf():
    t.goto(masofa + 110, 100)
    t.pendown()
    t.setheading(0)
    t.right(90)
    t.forward(100)
    t.penup()
    t.goto(masofa + 110, 50)
    t.left(90)
    t.pendown()
    t.forward(30)
    t.right(90)
    t.forward(50)

# i harf
def i_harf():
    t.penup()
    t.goto(masofa + 110 + 40, 50)
    t.pendown()
    t.forward(50)

    t.penup()
    t.goto(masofa + 110 + 40, 98)
    t.pendown()
    t.circle(2)
    t.hideturtle()

# q harf
def q_harf():
    t.showturtle()
    t.penup()
    t.goto(2*masofa + 110 + 40, 25)

    t.pendown()
    t.circle(25)
    t.penup()
    t.goto(2*masofa + 110 + 40 + 50, 25)
    t.pendown()
    t.forward(75)

def A_harf():
    t.penup()
    t.goto(2*masofa + 110 + 40 + 50 + 40, 100)
    t.pendown()
    t.right(13)
    gipo = 100 / math.cos(13)
    t.forward(gipo)
    t.penup()
    t.goto(2*masofa + 110 + 40 + 50 + 40, 100)
    t.pendown()
    t.left(26)
    t.forward(gipo)

def I_harf():
    t.penup()
    t.goto(3 * masofa + 110 + 40 + 50 + 40 + 30, 100)
    t.pendown()
    t.setheading(0)
    t.right(90)
    t.forward(100)
    t.hideturtle()



o_harf()
c_harf()
h_harf()
i_harf()
q_harf()

A_harf()
I_harf()



# turtle.penup()
# turtle.goto(-370,0)
# turtle.pendown()
#
# # # C harfi
# turtle.circle(100, -180, 150)
#
#
# turtle.penup()
# turtle.goto(-210,200)
# turtle.pendown()
# # H harfi
# turtle.left(90)
# turtle.forward(200)
# turtle.back(100)
# turtle.right(90)
# turtle.forward(90)
# turtle.right(90)
# turtle.forward(100)
# turtle.back(200)
#
#
# turtle.penup()
# turtle.goto(-160,200)
# turtle.pendown()
# # i harhi
# turtle.right(180)
# turtle.forward(200)
#
#
#
# turtle.penup()
# turtle.goto(-135, 100)
# turtle.pendown()
# # Q harfi
# turtle.circle(100)
# turtle.penup()
# turtle.goto(-10, 50)
# turtle.pendown()
# turtle.left(45)
# turtle.forward(74)
#
#
# turtle.penup()
# turtle.goto(80,0)
# turtle.pendown()
# turtle.circle(5)
#
# turtle.penup()
# turtle.goto(120,0)
# turtle.pendown()
# turtle.left(110)
# turtle.forward(200)
# turtle.right(135)
# turtle.forward(200)
# turtle.back(70)
# turtle.right(110)
# turtle.forward(94)
#
#
# turtle.penup()
# turtle.goto(300,185)
# turtle.pendown()
# # i harhi
# turtle.left(90)
# turtle.forward(200)
#

t.exitonclick()

