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


suzlar = baza_rasvo.split("\n")
lugat_ing2uzb = {}
for suz in suzlar:
   if suz == '':
       continue
   x = suz.split("–")
   ingliz = x[0].rstrip().lstrip()
   uzbek = x[1].lstrip().rstrip()

   lugat_ing2uzb[ingliz] = uzbek

print(lugat_ing2uzb)



ing_suz = input("so'zni kiriting: ")
tarjima = lugat_ing2uzb[ing_suz]
print("tarjimasi: ", tarjima)


