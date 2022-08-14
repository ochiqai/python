# # a = "salomlar"
# #
# # # 1. Harflarni katta harfga o'tkazish.
# # print(a.upper())
# #
# # # 2. Harflarni kichik hargga o'tkazish.
# # print(a.lower())
# #
# # # 3. 'l' harfi necha marta takrorlanayotganini aniqlash.
# # print(a.count('l'))
# #
# # # 4. 'l' harfi necha marta takrorlanayotganini aniqlash.
# # # for orqali aniqlash.
# # t = 0
# # for i in a:
# #     if i == 'a':
# #         t += 1
# # print(t)
# #
# # # 5. 'm' harfni indeksini topish.
# # print(a.find('m'))
#
# # ism = input("Ismingizni kiriting: ")
# # familya = input("familyangizni kiriting: ")
# # print(f"{ism.title()} {familya.title()} [{ism[0].title()}{familya[0].title()}]")
#
# # suz = 'oyatvasuralar'
# # print(suz[0:4])
# # print(suz[6:10])
#
# # son = int(input())
# # print(type(son))
# # a = 7
# # print(a)
#
# # s = 0
# # while True:
# #     son = input("raqam kiriting kiriting: ")
# #     if son == 'tamom':
# #         break
# #     try:
# #         son = int(son)
# #         s = s + son
# #     except:
# #         print("son kiriting")
# #
# # print(s)
#
# # harf = input("harf kiriting: ")
# # unli_harflar = ['a', 'i', 'u', 'o', 'e']
# # if harf in unli_harflar:
# #     print("bu harf unli")
# # else:
# #     print("bu undosh harf")
#
# # son = int(input("son kiriting: "))
# # if son % 2 == 0:
# #     print("JUFT")
# # else:
# #     print("TOQ")
#
# # yosh = int(input("Yoshingiz nechida: "))
# # if yosh > 15:
# #     print("Siz topshirishingiz mumkin")
# # else:
# #     print("Mumkin emas")
#
# # davlatlar = ["UZBEKISTAN", "RUSSIA", "USA"]
# # print(davlatlar)
#
# # viloyatlar = ['Samarqand', 'Toshkent', 'Surxondaryo', 'Qashqadaryo']
# #
# # # har bir elementni chiqaring.
# # for i in viloyatlar:
# #     print(i)
# # print("----")
# # # faqat boshidagi 3 elementni chiqaring.
# # for i in range(3):
# #     print(viloyatlar[i])
# # print("----")
# # # oxirgi elementni chiqaring.
# # print(viloyatlar[-1])
# # # Birinchi elementni `"Andijon"` ga o'zgartiring.
# # viloyatlar[0] = 'Andijon'
# # print(viloyatlar)
#
# # viloyatlar = []
# # viloyatlar.append("Toshkent")
# # viloyatlar.append("Surxondaryo")
# # viloyatlar.append("Samarqand")
# # print(viloyatlar)
#
# # son = []
# # t = 1
# # while t < 6:
# #     print(t, '-', end=' ')
# #     a = int(input('sonni kiriting = '))
# #     son.append(a)
# #     t += 1
# #
# # print(son)
#
# # sonlar = [.2, .4, .6, .7, .10, .11]
# # yangi_sonlar = []
# # i = 0
# # while i < len(sonlar):
# #     son = sonlar[i] * 100
# #     yangi_sonlar.append(son)
# #     i = i + 1
# #
# # print(yangi_sonlar)
#
# # def foydalanuvchi_kiritgan(x):
# #     print("Siz", x,"ni kiritingiz")
# # foydalanuvchi_kiritgan(input('Son kiriting = '))
#
# # def uch_max(a, b, c):
# #     print(max(a, b, c))
# #
# # uch_max(10, 20, 30)
#
# # def uzunlik(x):
# #     print(len(x))
# #
# # uzunlik("Ibrohim")
#
#
# # def yigindi(a):
# #     t = 0
# #     for i in a:
# #         t += i
# #     print(t)
# #
# # x = yigindi(list(map(int, input().split())))
# #
# # def kopaytma(a):
# #     t = 1
# #     for i in a:
# #         t *= i
# #     print(t)
# #
# # y = kopaytma(list(map(int, input().split())))
#
# # def teskari(x):
# #     print(x[::-1])
# #
# # teskari("salom")
# #
# # def palindrommi(x):
# #     if x == x[::-1]:
# #         print(True)
# #     else:
# #         print(False)
# #
# # palindrommi("katak")
#
# # def azomi(l, x):
# #     i = 0
# #     while i < len(l):
# #         if x == l[i]:
# #             return True
# #             break
# #         i = i + 1
# #     return False
# #
# #
# # print(azomi(['Ali', 'Bobur', 'Ibrohim'], 'Alisher'))
#
# # def bir_xil(list1, list2):
# #     i = 0
# #     while i < len(list1):
# #         if list1[i] in list2:
# #             return True
# #             break
# #         i = i + 1
# #     return False
# # print(bir_xil([1,2,3], [10, 777, 1]))
#
# # def n_takror_harf(a, b):
# #     print(a * b)
# #
# # n_takror_harf(5, 'a')
#
# # def histogram(l_list):
# #     i = 0
# #     while i < len(l_list):
# #         print('*' * l_list[i])
# #         i = i + 1
# #
# # histogram([1, 3, 5, 2])
#
# # def max_list(l_list):
# #     print(max(l_list))
# #
# # max_list([1,20, 45, 90, 32, 100])
#
# # def yulduzcha(qator):
# #     while qator > 0:
# #         print("*" * qator)
# #         qator = qator - 1
# #
# # yulduzcha(6)
#
# # def yulduzlar(qator):
# #     i = 1
# #     while i < qator+1:
# #         print('*' * i)
# #         i = i + 1
# #
# # yulduzlar(6)
#
#
# # def listdan_songa(list_suzlar):
# #     sonli_list = []
# #     i = 0
# #     while i < len(list_suzlar):
# #         sonli_list.append(len(list_suzlar[i]))
# #         i = i + 1
# #     return max(sonli_list)
# #
# # print(listdan_songa( ['salom', 'yaxshi', 'bir']))
#
# # def filter_uzun_suzlar(l,n):
# #     filter_list = []
# #     i = 0
# #     while i < len(l):
# #         if len(l[i]) > n:
# #             filter_list.append(l[i])
# #         i = i + 1
# #     return filter_list
# # list_suzlar = ['salom', 'yaxshi', 'bir']
# # print(filter_uzun_suzlar(list_suzlar,3))
#
# # harflar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # katta_harflar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# # def panagrammi(suz):
# #     indeks = 0
# #     while indeks < len(harflar):
# #         if (harflar[indeks] in suz or katta_harflar[indeks] in suz) == False:
# #             return False
# #         indeks = indeks + 1
# #     return True
# #
# # javob = panagrammi("abcdefghijklmn opqrsTuvwxyz")
# # print(javob)
# # i = 1
# # while i < 8:
# #     print(i, 'ta quy')
# #     i = i + 1
#
# # def sonlar(chegara):
# #     i = 1
# #     s = 0
# #     while i < chegara + 1:
# #         if i % 3 == 0 or i % 5 == 0:
# #             s = s + i
# #             i = i + 1
# #     return s
# #
# # print(sonlar(20))
#
# i = 1
# s = 0
# chegara = 20
# while i < chegara + 1:
#     if i % 3 == 0 or i % 5 == 0:
#         s = s + i
#         i = i + 1
#
# print(s)
# def sonlar(chegara):
#     i = 1
#     s = 0
#     while i <= chegara:
#         if i % 3 == 0 or i % 5 == 0:
#             s = s + i
#         i = i + 1
#     return s
#
# print(sonlar(20))

# def sonlar(chegara):
#     i = 0
#     while i <= chegara:
#         if i % 2 == 0:
#             print(i, "Juft")
#         else:
#             print(i, "Toq")
#         i = i + 1
#
# sonlar(3)

# def tezlik(v):
#     if v <= 70:
#         return 'OK.'
#     elif v > 70 and v < 80:
#         return 'Ogohlantirish.'
#     else:
#         return 'Litzensiyadan mahrum qilinsin.'
#
# print(tezlik(82))

# def fizz_buzz(son):
#     if son % 3 == 0 and son % 5 == 0:
#         return "FizzBuzz"
#     elif son % 3 == 0:
#         return "Fizz"
#     elif son % 5 == 0:
#         return "Buzz"
#     else:
#         return son
#
# print(fizz_buzz(55))

# L = ["Mario", "Bowser", "Luigi"]
#
# birinchi_element = L.pop(0)
# ohirgi_element = L.pop()
# # L listga birinchi elementni ohirga o'tkazib oldik.
# L.append(birinchi_element)
# # L listning ohirgi elementini yangi listning birinchi elementiga qushib olamiz.
# yangi_list = []
# yangi_list.append(ohirgi_element)
# # Yangi listga L listdagi elementlarni qushib ketaveramiz.
# i = 0
# while i < len(L):
#     yangi_list.append(L[i])
#     i = i + 1
#
# print(yangi_list)

# def ikkinchini_tanla(L):
#     ikkinchi_element = L.pop(1)
#     return ikkinchi_element
#
# print(ikkinchini_tanla(["olma", "nok", "gilos", "banan"]))

from collections import Counter

def harf_soni(x):
    print(Counter(x))

harf_soni("aaaabbbc")





