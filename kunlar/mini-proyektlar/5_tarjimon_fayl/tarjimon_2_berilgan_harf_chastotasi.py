from tarjimon_1_fayl import fayl2suzlar, suzlar2dict


# Kiritilgan harflar bo'yicha topilgan so'zlar sonini chiqarish
# foydalanuvchi harflarni kiritadi, usha harfdan boshlangan so'zlarni sonini chiqardi.
# Bunda, foydalanuvchi toki # stop degan suzni bosgunga qadar ishlashi kerak

joy="destination_ B1_ uzbekcha_tarjimasi.txt"
print("Berilgan fayldan ", joy, "suzlar o'qildi.")
_suzlar = fayl2suzlar(fayl_joyi=joy)

print("So'zlar dictga o'tkazildi")
ing_uzb_dict = suzlar2dict(_suzlar)

jami = 0
while True:
   harf = input("Harfni kirit: ")
   if harf == "stop":
      break

   sana = 0
   for ing in ing_uzb_dict.keys():
      if ing[0].upper() == harf.upper():
         sana += 1
   jami = jami + sana
   print(harf, "lar soni: ", sana)


