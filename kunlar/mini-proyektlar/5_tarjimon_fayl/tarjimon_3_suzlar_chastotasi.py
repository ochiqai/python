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

inx = harflar_soni.sort()
print(inx)

