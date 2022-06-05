# boolean ifodalar
ulugbek = 27
nuriddin = 21

tengmi = "(ulugbek == nuriddin)"
# tengme2 = (5 == 5)
print(tengmi)
# print(tengme2)

print(type(27))
print(type("27"))

# bool: True, False
print(type(27))

son1 = 14
son2 = 25

# natija = (14 == 25)
# natija = (14 != 25)
# natija = (14 > 15)
# natija = (14 < 15)
# natija = (14 >= 15)
# natija = (14 <= 15)
# # natija = (14 is 15)
# # natija = (14 is not 15)
#
# # print(natija)
#
# # mantiqiy operatorlar: and, or, not
# # and
# ismi = 'nuriddin'
# yoshi = 24
#
# natija = (ismi == "ulugbek") and (yoshi == 24)
#
# natija = (ismi == "ulugbek") or (yoshi == 24)
#
# natija = not (ismi == "nuriddin")
#
# print(natija)
#
#
# # if
# x = 10
# y = 0
#
# if y == 0:
#     pass
#
# if y != 0:
#     natija = x / y
#     print(natija)
# else:
#     print("y nolga teng o'shaning uchun bo'lish mumkinmas.")
#
#
# son = int(input("Sonni kiriting: "))
#
# if son > 0:
#     print("musbat!")
# else:
#     print("manfiy!")
#
# if son % 2 == 0:
#     print("juft son")
# else:
#     print("toq son")
#
# x = int(input("x ni kiriting: "))
# y = int(input("y ni kiriting: "))
#
# if x > y:
#     print("x soni y sonidan katta")
# elif x < y:
#     print("x soni y sonidan kichik")
# else:
#     print("x va y sonlari bir-biriga teng")
#
# if x > y:
#     print("x y dan katta")
# else:
#     if x < y:
#         print("x y dan kichik")
#     else:
#         print("x y ga teng")

# x = int(input("x ni kirting"))
# y = int(input("y ni kirting"))
#
# try:
#     natija = x / y
#     print(natija)
# except:
#     print("xatolik kettdi")

#natija = (10 < 5) and (10/0 > 3)
#natija = (10/0 > 3) and (10 < 5)
# natija = (10 < 5) or (10/0 > 3)
# print(natija)
#
#


# Programma tuzing. Foydalanuvchi faqat son kiritsin, agar string kiritsa.
# Son kiriting, ilitmos deb chiqsin. try\except dan foydalaning.

son = input("Son kiriting: ")
try:
    a = int("a")
    print(a)
except:
    print("Iltimos son kiriting")




























#
#
# tengmi = (5 == 7)
# print(tengmi)
#
# x = 1
# shart = not (x > 10)
# print(shart)
#
#
# def bulish(a, b):
#     natija = a / b
#     return natija
#
# # funksiyani chaqiramiz
#
# c = bulish(10, 2)  # 10/5
# print(c)
# print("Nolga bo'lish mumkin emas!")
#
#
# natija = (10 < 5) and (10/0 > 3)
# print(natija)
#
#
# birinchi = input("1-sonni kiriting: ")
# ikkinchi = input("2-sonni kiriting: ")
# natija_string = birinchi + ikkinchi
# natija_butun = int(birinchi) + int(ikkinchi)
# print('Butun songa konvert qilinMAdi: ', natija_string)
# print('Butun songa konvert qilindi:', natija_butun)