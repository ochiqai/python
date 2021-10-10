# s = "salom"
# s_list = ['s', 'a', 'l', 'o', 'm']
#
# list1 = [10, 20, 30, 40, 50]
# list2 = ["Samarqand", "Surxondaryo", "Toshkent"]
# list_aralash = [10, "samarqand", 'baholar', 50.5]
#
# print(s_list)
# print(list1)
# print(list2)
# print(list_aralash)
#
# print(25 in list1)
# print(50 in list1)
#
#
# s = "harflar"
# for c in s:
#     print(c)
#
# for element in list1:
#     print(element)
#
# print("\n")
# list1 = [10, 20, 30, 40, 50]
# # list1[0] = list1[0] + 10
# # list1[1] = list1[1] + 10
# # list1[2] = list1[2] + 10
# # list1[3] = list1[3] + 10
# # list1[4] = list1[4] + 10
#
# for idx in range(0, len(list1), 1):
#     list1[idx] = list1[idx] + 10
#     print(list1[idx])
#
# bush_st = ""
# print(bush_st)
#
# bush_int = 0
# bush_float = 0.0
#
# bush_list = []
# print(bush_list)
#
# for ele in bush_list:
#     print(ele)
#
# l = [[1], [2], [3], [4], [5]]
# print(len(l))
#
#
# # list operatorlari
# a = [1, 2]
# b = [3, 4]
# c = a + b
# print(c)
#
# a = ['a', 'b']
# c = a * 4
# print(c)
#
# nollar = [0] * 10
# print(nollar)
#
# print(list1)
# print(list1[1:])
# print(list1[:len(list1)-1])
#
# print(list1[1:4])
#
# # list metordlari
# l = [1,2,3,4,5]
# l.append(6)
# l_st = ['a', 'b']
# l_st.append('c')
# print(l)
# print(l_st)
#
# l = [100, 45, 30, 23, 89, 21]
# l.sort()
# print(l)
#
# l = [100, 45, 30, 23, 89, 21]
# l.pop(1)
# l.pop()
#
# del l[0]
# print(l)
#
# mevalar = ["anor", 'pichoq', 'olma']
# mevalar.remove("pichoq")
# print(mevalar)
#
#
# del l[:3] # ko'p elementlarni o'chirish
#
#
# l = [10, 32, 13, 4, 5]
# print(len(l))
# print(min(l))
# print(max(l))
# print(sum(l))
#
# # list va string
#
# print("\n\n\n")
# s = "salom"
# s_list = list(s)
# print(s_list)
#
# s = "O'zbekiton kelajagi buyuk davlat"
# l_s = [s]
# suzlar = s.split()
# print(suzlar)
#
# s = "O'zbekiton-kelajagi-buyuk-davlat"
# suzlar = s.split("-")
# print(suzlar)
#
# st = " ".join(suzlar)
# print(st)
#
# ism = "Ibragimov Ulugbek"
# yozuzlar = ism.split()
# boshharflar = yozuzlar[0][0] + yozuzlar[1][0]
# print(boshharflar)


a = 'olma'
b = 'olma'

print(a is b)

a = [1, 2]
b = [1, 2]

print(a is b)

# taxallus (alias)

a = [1, 2, 3]
b = a
print(a is b)

b[2] = 60
print(b)
print(a)

def ayt(a):
    a = 50
    return a
a = 45
print(ayt(a))
print(a)


def ayt_list(l):
    del l[0]
    return l

l = [1, 2, 3, 4]
print(ayt_list(l))
print(l)



