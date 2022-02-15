# list obyekti
mashinalar = list()
mashinalar.append("Neksiya")
mashinalar.append("Tiko")
mashinalar.append("Damas")
mashinalar.sort()
print(mashinalar[0])

# hamma imkoniyatlari
mashinalar = list()
print(dir(mashinalar))

# class
class Ishchi:
    def __init__(self, ism, familiya, sharif, yosh):
        self.ism = ism
        self.familiya = familiya
        self.sharif = sharif
        self.yosh = yosh

    def fish(self):
        print("{} {} {}, {} yoshda".format(self.familiya, self.ism, self.sharif, self.yosh))


# metodni chaqirish
ishchi = Ishchi("Ahmad", "Aliyev", "Shakar o'gli", 25)
ishchi.fish()


# turini tekshirish
print("Turi", type(ishchi))
print("Turi", type(ishchi.ism))
print("Turi", type(ishchi.yosh))


## ko'plik obyektlar
ishchi_1 = Ishchi("Tesha", "Boltayev", "Qilich o'gli", 5)
ishchi_2 = Ishchi("Guli", "Anorava", "Anor o'gli", 7)

ishchi_1.fish()
ishchi_2.fish()

## Meros
class Ishchi:
    def __init__(self, ism, familiya, sharif, yosh):
        self.ism = ism
        self.familiya = familiya
        self.sharif = sharif
        self.yosh = yosh

    def fish(self):
        print("{} {} {}, {} yoshda".format(self.familiya, self.ism, self.sharif, self.yosh))

class Shafyor(Ishchi):
    def __init__(self, ism, familiya, sharif, yosh, ser_nomer):
        self.ism = ism
        self.familiya = familiya
        self.sharif = sharif
        self.yosh = yosh
        self.ser_nomer = ser_nomer

    def sertfikat_nomeri(self):
        print("Haydovchilik guvohnomasi nomeri: ",self.ser_nomer)


shafyor = Shafyor("Sardor", "Ibragimov", "Xo'lmo'min o'g'li", 26, "AA4567Q")
shafyor.fish()
shafyor.sertfikat_nomeri()