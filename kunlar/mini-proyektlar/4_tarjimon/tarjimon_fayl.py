f = open("Destination B1 özbekcha tarjimasi bilan..txt")
qatorlar = f.readlines()

suzlar = []
for qator in qatorlar:
   _list = qator.split("\n")
   if _list[0] != '':
      if '-' in _list[0] or '–' in _list[0]:
         suzlar.append(_list[0])

print("Jami suzlar soni: ", len(suzlar))

lugat_ing2uzb = {}
for suz in suzlar:
   if suz == '':
       continue
   try:
      x = suz.split("–")
      if len(x) == 1:
         x = suz.split("-")
      ingliz = x[0].rstrip().lstrip()
      uzbek = x[1].lstrip().rstrip()
   except:
      print(x)

   lugat_ing2uzb[ingliz] = uzbek

# ing_suz = input("Inglizcha so'zni kiriting: ")
# tarjima = lugat_ing2uzb[ing_suz]
# print("tarjimasi: ", tarjima)

## hamma harfdan boshlanadigan suzlar bormi?
harflar = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

harflar_soni = []
for harf in harflar:
   sana = 0
   for ing in lugat_ing2uzb.keys():
      if ing[0].upper() == harf:
         sana += 1
   harflar_soni.append(sana)
   print(harf, "lar soni: ", sana)

inx = harflar_soni.sort()
print(inx)



## foydalanuvchi harflarni kiritadi, usha harfdan boshlangan so'zlarni sonini chiqardi.
# Bunda, foydalanuvchi toki # stop degan suzni bosgunga qadar ishlashi kerak

jami = 0
while True:
   harf = input("Harfni kirit: ")
   if harf == "stop":
      break

   sana = 0
   for ing in lugat_ing2uzb.keys():
      if ing[0].upper() == harf.upper():
         sana += 1
   jami = jami + sana
   print(harf, "lar soni: ", sana)


