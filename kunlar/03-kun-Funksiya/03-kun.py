def kattasini_aniqlash():
    kattasi  = max(1, 23)
    print(kattasi)

def math_modulidan_foydalanish():
    import math

    ildiz = math.sqrt(49)
    print(ildiz)

    daraja = math.pow(10, 2)
    print(daraja)


# print("yangi funksiyalar ----------------------------")

def ayirish(a, b):
    natija = a - b

    return natija

n = ayirish(70, 10)
print(n)

# # chiziqli funksiya
def chiziq(x):
    y = x + 3
    return y

q = chiziq(3)
print(q)

def salomlashish():
    print("Salom, Pythonjon")

salomlashish()
salomlashish()
salomlashish()
salomlashish()
salomlashish()


# mevais funksiyani chqairsal nima bo'ladi? >> None yuq narsa qaytaradi
yuq_nara = salomlashish()
print(yuq_nara)

def ism():
    a = 'ichki'
    print(a)

a = 'tashqi'
ism()
print(a)

def ism():
    a = 'ichki'
    return a

b = ism() #'ichki'
print(b)


def bir():
    return 1

def ikki():
    return 2

a = bir() + ikki()

a = 1 + 2
print(a)


def qaysi(a):
    a = a
    b = bir() + ikki()
    return b

print(qaysi(1))





# def hi():
#     a = 1
#
# a = hi()
# print(a)


def hi():
    a = 1

a = hi()
print(a)





















