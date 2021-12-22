import re

# ^ Karet bilan ishlash, qator boshini bildiradi.

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("^Jumladan", qator):
#         print(qator)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("^Received", qator):
#         print(qator)


# nuqtalar bilan ishlash, nuqtalar ixtiyoriy belgiga ruhsat borligini bildiradi.
# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("C.....t", qator):
#         print(qator)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("R....t", qator):
#         print(qator)


# .+ Nuqta plus
# biz nuqtani kordik. u foydali qachonki biz uzunlikni bilsak.
# Lekin kop hollarda biz bilmaymiz. Shunday vaqtda .+ belgisi qo'l keladi.

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("^From:.+@", qator):
#         print(qator)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("^Author:.+@", qator):
#         print(qator)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("^gradebook/.+java", qator):
#         print(qator)


# findall va \S


# \S+@\S+: berilgan stringdan shunday substringlarni qidiringki, undagi substringlar boshlanish belgilardan bulib
# undan keyin @ belgi bo'lib va undan keyin yana belgilar bo'lishi kerak

# s = 'Biz xabarni ulugbek@gmail.com dan oldik, keyin uni nuriddin@gmail.com ga yubordik'
# lst = re.findall('\S+@\S+', s)
# print(lst)

# x = ' Bu sayt azolari elyorcv@gmail.com , ulugbek@gmail.com va nuridin@gmail.com'
# lst = re.findall("\S+@\S+", x)
# print(lst)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall("\S+@\S+", qator)
#     if lst != []:
#         print(lst)

# a = "ali@gmail.com siz o'tkan safar darsga qatnashmadingiz. dilshod@gmail.com siz o'tkan darsdagi eng yaxshi o'quvchisiz"
# lst = re.findall("\S+@\S+", a)
# print(lst)

# #tozaroq elektron addresslarni chiqarish
# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', qator)
#     if lst != []:
#         print(lst)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall("^X\S*: [0-9.]+", qator)
#     if lst != []:
#         print(lst)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall("^X\S*: ([0-9.]+)", qator)
#     if lst != []:
#         print(lst)

# Maxsus belgilar bilan ishlash $

# x = 'We just received $100.00 for cokking.'
# lst = re.findall("\$[0-9.]+", x)
# print(lst)
#
# x = 'We just received $100.00 for cokking.'
# lst = re.findall("\$.[0-9.]+", x)
# print(lst)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall("^Details: \S*rev=[0-9.]+", qator)
#     if len(lst)>0:
#         print(lst)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall("^Details: \S*rev=([0-9.]+)", qator)
#     if len(lst)>0:
#         print(lst)

# fayl = open("regifoda.txt", 'r', encoding="utf8")
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall('^From .* ([0-9][0-9]):', qator)
#     if len(lst) > 0:
#         print(lst)







