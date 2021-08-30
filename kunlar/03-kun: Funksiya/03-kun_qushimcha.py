def amal(a, b): # a = 2, b = 1.
    return a, b


def kamal(x, y): # x = 1, y = 2
    a, b = amal(x, y) # x = 1, y = 2. a = 1, b = 2
    a, b = amal(b, a) # b= 2, a = 1. # a = 2, b = 1

    return x+a, y+b # 3, 3

a, b = amal(1,2) # a = 1
x, y = kamal(1,2) # x = 3, y = 3

print(a+y)
# N: 4
# U: 5 (XATO)