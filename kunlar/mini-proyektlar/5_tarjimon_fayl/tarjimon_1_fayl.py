"Ushbu programma faylni olib lug'at yasaydi"


def fayl2suzlar(fayl_joyi):
   """
   Ushbu funksiya berilgan fayldan so'zlarni o'qib uni qaytaradi
   :return: list
   """

   # faylni ochamiz
   f = open(fayl_joyi)

   # faylni qator bo'yicha o'qiymiz
   qatorlar = f.readlines()

   # qatarlardan hamma so'zlarni olayapmiz
   suzlar = []
   for qator in qatorlar:
      # qatorni "\n" bo'yicha bo'laklarga bo'layapmiz.
      # Chunki, qatorlar yangi qator ("\n") belgisi bilan tugagan ularni hisobga olmasligimiz
      # kerak.
      _list = qator.split("\n")

      # Agar qatorni birinchi elementi bo'shliq ('') bo'lmasa, bu degani so'z bor degani.
      # So'z deganda "beat - yengmoq" nazarda tutilyapti. Yani ham ingliz ham uzbek suzlari mavjud.
      if _list[0] != '':
         # so'zlarni orasida '-' yoki '–' belgilari borligini tekshirayapmiz.
         # agar bo'lsa suzlar listiga qo'shayapmiz
         if '-' in _list[0] or '–' in _list[0]:
            suzlar.append(_list[0])

   print("Jami suzlar soni: ", len(suzlar))
   return suzlar


def suzlar2dict(suzlar):
   """
   Ushbu funksiya suzlarni olib dictga o'tkazadi
   :return: lugat_ing2uzb
   """

   # bo'sh dict yaratamiz
   lugat_ing2uzb = {}
   # xar bir suzni suzlardan olamiz
   for suz in suzlar:
      # agar suz bo'shliq bo'lsa yani yo'q bo'lsa uni hisobga olmaymiz
      if suz == '':
          continue

      # '–' bo'yicha suzlarni bo'l
      x = suz.split("–")

      # agar so'zlar bo'linmasa, yana '-' belgisi orqali bo'lishga harat qilamiz
      if len(x) == 1:
         x = suz.split("-")

      # bazida so'zlardan keyin va oldin bo'shliq mavjuda, o'shalarni bartaraf qilayapmiz
      ingliz = x[0].rstrip().lstrip()  # "beat " >>> "beat"
      uzbek = x[1].lstrip().rstrip()  # " yengnmoq" >>> "yengnmoq"
      lugat_ing2uzb[ingliz] = uzbek

   return lugat_ing2uzb


if __name__ == "__main__":
   # funksiyalardan foydalanamiz
   joy="destination_ B1_ uzbekcha_tarjimasi.txt"
   print("Berilgan fayldan ", joy, "suzlar o'qildi.")
   _suzlar = fayl2suzlar(fayl_joyi=joy)

   print("So'zlar dictga o'tkazildi")
   ing_uzb_dict = suzlar2dict(_suzlar)

   ing_suz = input("\nInglizcha so'zni kiriting: ")
   tarjima = ing_uzb_dict[ing_suz]
   print("Tarjima: ", tarjima)

