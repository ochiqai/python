import turtle


turtle.shape("turtle")  # shakli

# kvadrat
def kvadrat():
    for sikl in range(4):
        for i in range(100):
            turtle.forward(1)   # oldinga
        turtle.right(90)


# turtburchak
def turtburchak():
    for sikl in range(1, 5):
        if sikl % 2 == 0:
            for i in range(50): # qadam
                turtle.forward(1)   # oldinga
        else:
            for i in range(100): # qadam
                turtle.forward(1)   # oldinga

        turtle.right(90)



i = 1
i = i * (-1)
print(i)
i = i * (-1)
print(i)
i = i * (-1)
print(i)
i = i * (-1)
print(i)
print("--------------------------------------")
x = 200
y = 200
for idx in range(1, 5):
    x = x * (-1)
    turtle.penup()

    if idx == 1 or idx == 4:
        turtle.goto(x, -y)
    else:
        turtle.goto(x, y)

    turtle.pendown()
    kvadrat()
    print(x)




# for _ in range(4):

# turtle.penup()
# turtle.goto(-200, -200)
# turtle.pendown()
# kvadrat()

# turtle.penup()
# turtle.goto(200, 200)
# turtle.pendown()
# kvadrat()


# turtle.penup()
# turtle.goto(-200, 200)
# turtle.pendown()
# kvadrat()
#
# turtle.penup()
# turtle.goto(200, -200)
# turtle.pendown()
# kvadrat()




# turtle.penup()
# turtle.goto(400, -20)
# turtle.pendown()
#
# turtburchak()









# O
# for x in range(200):
#     turtle.forward(3)
#     turtle.right(2)

# # c
# turtle.penup()
# turtle.goto(400, -20)
# turtle.pendown()

# for x in range(130):
#     turtle.backward(3)
#     turtle.left(2)
#
# # h
# turtle.penup()
# turtle.goto(400, 00)
# turtle.pendown()
#
# turtle.right(90)
# for x in range(130):
#     turtle.forward(100)
#

turtle.exitonclick()

