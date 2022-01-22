def dars_1():
    l = list()
    l.append("olma") # method, metod
    l.append("anor") # # method, metod
    l.sort() # method, metod
    print(l[0]) # retrieve, olish
    print(l.__getitem__(0)) # retrieve, olish
    print(list.__getitem__(l, 0)) # retrieve, olish

    # capabilities
    print(dir(list))
    print(len(dir(list)))

    # class
    class PartyAnimal:
        x = 10
        def party(self) :
            self.x = self.x + 1
            print("So far", self.x)

    an = PartyAnimal()
    an.party()
    an.party()
    an.party()
    PartyAnimal.party(an)

    print("Type: ", type(an))
    print("Dir: ", dir(an))
    print("Type: ", type(an.x))
    print("Type: ", type(an.party))



from kutubxona import Calculator

class NurCalculator(Calculator):
    def __init__(self):
        print("Nuriddin Kalkulator yaratildi")
    def ayirish(self, x, y):
        return x - y

    def __str__(self):
        return "Nuriddin kalkulyator obyekti"



cal = Calculator()
print(cal.x)
print(cal.qushish(10, 20))
print(cal.x)

print("Orginal Kalkulyator imkoniyatlari: ", dir(cal))

nurcal = NurCalculator()
print(nurcal.qushish(10, 20))
print(nurcal.ayirish(10, 20))
print(nurcal)

print("Nuriddin Kalkulyator imkoniyatlari: ", dir(nurcal))








