import re


# ^ caret bilan ishlash, qator boshini bildiradi
# fayl = open("regifoda.txt", 'r')
# for qator in fayl.readlines():
#     qator = qator.rstrip()
#     if re.search("^Jumladan", qator):
#         print(qator)

# #  nuqtalar bilan ishlash, nuqtalar ixtiyoriy belgifa ruhsat borligini bildiradi
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


import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

fayl = open("regifoda.txt", 'r')
for qator in fayl.readlines():
    qator = qator.rstrip()
    lst = re.findall('\S+@\S+', qator)
    if lst != []:
        print(lst)