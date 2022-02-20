# Ushbu programma berilgan stringdan dictionary yasaydi

baza_rasvo = """beat – yengmoq
board game – doska oyini
captain – sardor(kapitan)
challenge – chaqiruv(musobaqaga)
champion – champion
cheat – g’irromlik qilmoq
classical music – mumtoz musiqa
club – club
coach – murabbiy
competition – musobaqa
concert – konsert
defeat – g’alaba (qozonmoq)
entertaining – ko’ngilochar
folk music – folklor musiqa
group – guruh
gym – zal (gimnaziya zali)
have fun – xursandchilik qilmoq
interest – qiziqtirmoq
member – a’zo
opponent – raqib
organize – tashkillashtirmoq
pleasure –rohat
referee – hakam
rhythm – maqom; marom
risk – tavakkal (qilmoq)
score – ochko (ishlamoq) (gol kiritmoq)
support – qo’llab quvatla(sh)
team – jamoa
train – trenirovka qilmoq
video game – video oyin (komp o’yini)
"""


def yozuv2dict(yozuvlar_bazasi):
   """
   Bu funksiya yozublarni olib lug'at ko'rinishda dictionaryga o'tkazadi
   :param yozuvlar_bazasi: bu string
   :return: dictionary
   """

   # berilgan yozuvlarni qator bo'yicha bo'lib chiqamiz. '\n' yangi qatorni bildiradi
   yakka_suzlar = yozuvlar_bazasi.split("\n")

   # bo'sh dictionary ochamiz
   lugat_ing2uzb = {}

   # har bir so'zlar ustida ishlaymiz
   for suz in yakka_suzlar:
      # agar so'zimiz ''ga teng bo'lsa, bu degani so'z yo'q degani
      # o'shaning uchun ushbu suz dictinoaryga qo'shilmaydi
      if suz == '':
          continue

      # so'zlar "X - Y" ko'rinishda bo'lganligi uchun, ular '-' bo'yicha bo'layapmiz (split)
      x = suz.split("–")

      # bazida so'zlardan keyin va oldin bo'shliq mavjuda, o'shalarni bartaraf qilayapmiz
      ingliz = x[0].rstrip().lstrip()  # "beat " >>> "beat"
      uzbek = x[1].lstrip().rstrip()  # " yengnmoq" >>> "yengnmoq"

      # endi ingliz va uzbek so'zlarini oldik yuqoridan, shular bo'yicha dictionary tuzamiz
      lugat_ing2uzb[ingliz] = uzbek

   return lugat_ing2uzb


# funksiyani chaqiramiz, va bazani beramiz
lugat_ing2uzb = yozuv2dict(baza_rasvo)

# foydanuvchidan ingliz so'zni kiritishni so'raymiz
ing_suz = input("Ingliz so'zni kiriting: ")

# kiritilgan so'z bo'yicha, o'zbekchasi beriladi
tarjima = lugat_ing2uzb[ing_suz]
print("tarjimasi: ", tarjima)


