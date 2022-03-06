from tarjimon_1_fayl import fayl2suzlar, suzlar2dict


# Alfabet bo'yicha boshlanadigan harflar bilan berilgan so'zlar sonini topish

joy="destination_ B1_ uzbekcha_tarjimasi.txt"
print("Berilgan fayldan ", joy, "suzlar o'qildi.")
_suzlar = fayl2suzlar(fayl_joyi=joy)

print("So'zlar dictga o'tkazildi")
ing_uzb_dict = suzlar2dict(_suzlar)

harflar = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

harflar_soni = []
for harf in harflar:
   sana = 0
   for ing in ing_uzb_dict.keys():
      if ing[0].upper() == harf:
         sana += 1
   harflar_soni.append(sana)
   print(harf, "lar soni: ", sana)



import matplotlib.pyplot as plt

# bar chartni ekranda chiqarish
# plt.bar(harflar, harflar_soni)
# plt.title("Harflar bilan boshlanadigan so'zlar soni")
# plt.xlabel("Harflar")
# plt.ylabel("Soni")
# plt.show()


# 2 ta bar chartni. 1 ta ekranda chiqarish
# plt.subplot(1, 2, 1)
# plt.bar(harflar, harflar_soni)
# plt.title("O'zbek")
# plt.xlabel("Harflar")
# plt.ylabel("Soni")

# plt.subplot(1, 2, 2)
# plt.bar(harflar, harflar_soni)
# plt.title("Ingliz")
# plt.xlabel("Harflar")
# plt.ylabel("Soni")


# y = x^2 + 5*x funksiya uchun, quyidagi x kordinatalar  berilgan
x = [-20, -10, -9, -7, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 7, 9, 10, 20]

y = []
for xi in x:
   yi = xi**2 + 5*xi
   y.append(yi)

# koordinatalarga nuqtalarni joylash
# plt.plot(x, y)
plt.scatter(x, y)
plt.text(x[0]+2, y[0], "({}, {})".format(x[0], y[0]))

# koordinatalarga nuqtalarni joylash (xar xil rangda)
y = [] # koordinatalar
plt.show()
for xi in x:
   yi = 5*xi**2 - xi
   y.append(yi)
   plt.scatter(xi, yi)
plt.show()

# pie chat
plt.pie([50, 50])
plt.title("Pie chart")
# plt.show()

















