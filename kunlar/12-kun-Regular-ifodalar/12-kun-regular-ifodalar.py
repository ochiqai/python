import re


# # ^ karet bilan ishlash, qator boshini bildiradi
# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("^Jumladan", qator):
#         print(qator)

# #  nuqtalar bilan ishlash, nuqtalar ixtiyoriy belgiga ruhsat borligini bildiradi
# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("y..i", qator):
#         print(qator)


# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("^From:.+@", qator):
#         print(qator)


# \S+@\S+: berilgan stringdan shunday substringlarni qidiringki, undagi substringlar boshlanish belgilardan bulib
# undan keyin @ belgi bo'lib va undan keyin yana belgilar bo'lishi kerak
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# s = 'Biz xabarni ulugbek@gmail.com dan oldik, keyin uni nuriddin@gmail.com ga yubordik'
# lst = re.findall('\S+@\S+', s)
# print(lst)
#
# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall('\S+@\S+', qator)
#     if lst != []:
#         print(lst)
#
#
# tozaroq email addresslarni chiqarish
# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', qator)
#     if lst != []:
#         print(lst)

# # tozaroq email addresslarni chiqarish
# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     # lst = re.search('^X\S*: [0-9.]+]', qator)
#     if re.search('^X\S*: [0-9.]+', qator):
#         print(qator)


# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall('^X\S*: ([0-9.]+)', qator)
#     if len(lst) > 0:
#         print(lst)

# # Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall('^Details: \S*rev=([0-9]+)', qator)
#     if len(lst) > 0:
#         print(lst)

# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     lst = re.findall('^From .* ([0-9][0-9]):', qator)
#     if len(lst) > 0:
#         print(lst)

# maxsus belgilar bilan ishlash uchun, \ (backslash) dan foydalanamiz
x = 'We just received $10.00 for cookies.'
lst = re.findall("$.[0-9.]+", x)
print(lst)










