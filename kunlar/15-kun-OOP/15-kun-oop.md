# Obyektga Orientirlangan Programmalash

Obyektga Orientirlangan Programmalash qisqacha qilib OOP deb ataladi. OOPning asosiy maqsadlaridan
biri shundaki - bunda kod yozilayotganda uning tushunarliligini oshirishga hizmat qiladi. 
Programma qatori qanchalik ko'p bo'lsa (minglab, millionlab qatorlar bo'lib ketsa), kodni tushunish qiyinlashadi
chunki hamma qatorni miyyadan saqlab qolish uchun programmistdan ko'p energiya talab etiladi. Quyida
OOPga oid bir necha asosiy terminlar va konsepsiyalarni ko'rib chiqamiz.

## Obyektlardan foydalanish
Aslida shu paytgacha biz obyektlardan foydalandik. Lekin shu paytgacha obyekt deb atamadik.
Python ko'p obyektlarni taqdim qilgan. Pythondda umman olganda hamma narsa obyekt hisoblanadi.
O'shaning obyekt tushunchasi juda muhim. Masalan, listni olaylik

```python
mashinalar = list()
mashinalar.append("Neksiya")
mashinalar.append("Tiko")
mashinalar.sort()
```

Yuqorida kodda OOP jihatdan quyidagilar ro'y berayapti:

- 1-qatorda list turiga tegishli obyekt yaratilayapti (`list()`) va u `mashinalar` o'zgaruvchisaga 
yuklanayapti
- 2-qatorda `append` metodi chaqirilayapti.
- 3-qatorda `sort` metodi chaqirilayapti.

Biz bu yerda obyektga tegishli 2 ta metodni keltirib o'tdik. Agar hamma imkoniyatlarini
bilmoqchi bo'lsak `dir` funksiyasidan foydalansak bo'ladi.

```python
mashinalar = list()
print(dir(mashinalar))
```
Va `list` ning quyidagi juda ko'p imkoniyatlarga ekanligini bilishimiz mumkin
```commandline
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', 
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 
'insert', 'pop', 'remove', 'reverse', 'sort']
```





## Shaxsiy birinchi Obyektimiz
Umuman olganda obyekt nima desak, oddiy qilib obyekt bu 
- bir necha satrlardan iborat kod va data strukturalardan tashkil topadi 
- to'liq programmaning bir parchasi hisoblanadi

Obyekt funksiya va malumatlardan tashkil topishi mumkin. Funksiya `metod` deb ataladi. Va metodlar malumotlardan 
foydalanishi mumkin. Malumotlar `attribut`lar deb ham ataladi.

O'zimiz biron obyektni belgilamoqchi bo'lsak `class` kalit so'zidan foydalanamiz. 
Bu xuddi funksiya yaratganimizda `def` dan foydalanganimizdek. 

Keling `Ishchi` deb atalgan class kodini yozamiz,

```python
class Ishchi:
    def __init__(self, ism, familiya, sharif, yosh):
        self.ism = ism
        self.familiya = familiya
        self.sharif = sharif
        self.yosh = yosh

    def fish(self):
        print("{} {} {}, {} yoshda".format(self.familiya, self.ism, self.sharif, self.yosh))
```

Quyidagilarni o'rganishimiz mumkin
- `Ishchi` klasi aniqlandi
- Unda iikita metod bor: `__init__` va `fish`. 
- `__init__`da attributlar e'lon qilingan. Mn: ism, familiya va yoshi.
- `fish` metodi attributlardan foydalanib ishning to'liq ismini chiqaradi.
- Etibor qilishimiz klassni aniqlash degani obyektni yaratdik degani emas. Klass bu xuddi andoza o'xshaydi.
Mn: g'isht quyayotganimizda qolipdan foydalanamiz. Qolipning o'zi klassga misol bo'ladi.


Endi bu classni chaqiramiz xuddi funksiyaga o'xshatib, yani

```python
ishchi = Ishchi("Ahmad", "Aliyev", "Shakar o'gli", 25)
```

Mana endi obyekt yaratildi va u `ishchi` o'zgaruvchisiga yuklandi.
Agar `ishchi.fish()` ni ishlatsak, quyidagi natija chiqadi

```commandline
Aliyev Ahmad Shakar o'gli, 25 yoshda
```

E'tibor qilingki obyektga tegishli metod yoki attributlardan foydalanish uchun `.` belgisidan foydalandik.


## Klasslar bu Yangi Tur

Bilamizki Pythonda bir necha o'zgaruvchilar turi mavjud (butun sonlar - int, stringlar).  Biron bir 
o'zgaruvchining qaysi turga tegishliligi bilmoqchi bo'lsak, `type` funksiyasidan foydalanardik. Klasslarga ham 
ushbu funksiyani bemalol foydalansak bo'laveradi: 

```python
print("Turi", type(ishchi))
print("Turi", type(ishchi.ism))
print("Turi", type(ishchi.yosh))
```

Natija:

```commandline
Turi <class '__main__.Ishchi'>
Turi <class 'str'>
Turi <class 'int'>
```



## Obyekt hayoti

Biz yuqorida `class`ni elon qildik va u shunchaki qolip vazifasizini ham bajarishini bildik. 
Keyin `class` qolipi orqali obyekt yaratishni ham ko'rdik. Qachonki programma ishlashdan tugaganida 
hamma `class`ga tegishli maumotlar o'chib ketadi. Odatda biz o'zgavruvchilar yaratilishi va 
programma ishlab bo'lgandan keyin o'chib ketishligi haqida gapirmaymiz. Lekin obyektlar murakkablashgan sari
bu haqida o'ylashimizga to'g'ri keladi. Asosan obyekt yaratilish bosqichida.

Keling quyida yana yuqoridagi misolni yana qarab chiqamiz. `__init__` funksiyasiga 
`print('Obyekt yaratildi')` deb qo'shimcha kiritamiz.   

```python
class Ishchi:
    def __init__(self, ism, familiya, sharif, yosh):
        print('Obyekt yaratildi')
        self.ism = ism
        self.familiya = familiya
        self.sharif = sharif
        self.yosh = yosh
        

    def fish(self):
        print("{} {} {}, {} yoshda".format(self.familiya, self.ism, self.sharif, self.yosh))
```

Va bu `class`dan obyekt yaratsak,

```python
ishchi = Ishchi("Ahmad", "Aliyev", "Shakar o'gli", 25)
```

Natija 

```commandline
Obyekt yaratildi
```

Etibor beringki, `class`dan obyek yaratayotganimizda eng birinchi bo'lib `__init__` metodi ishlar ekan.
Shu bois `class`ga tegishli attributlarni boshlangich holatini mana shu yerda belgilash tavsiya etiladi.


## Ko'p obyektlar

Hozirgacha, `class`ni e'lon qildik, va faqat bitta obyekt yaratidk, ishlatdik va programma tugagandan keyin 
xotiradan o'chib ketdi. LEkin, OOPning haqiqiy kuchi, bitta `class`dan bir necha ko'plab obyektlar yaratishda
namoyon bo'ladi. 

Qachonki biz bir necha obyektlarni classdan hosil qilayotganimizda, har safar attributlarga
boshqacha malumot berishimiz mumkin. Ya'ni, quyida 2 ta obyekt yaratdik, ularga har xil attributlar berdik.


```python
ishchi_1 = Ishchi("Tesha", "Boltayev", "Qilich o'gli", 5)
ishchi_2 = Ishchi("Guli", "Anorava", "Anor o'gli", 7)
ishchi_1.fish()
ishchi_2.fish()
```



## Meros

OOP ning yana bir afzallik tarafi chundaki, yangi class boshqa classdan meros olish mumkin. Bunda, 
meros berayotgan klass `ona class` deb, merosni olayotgan klass esa `bola class` deb ataladi.

Masalan `Ishchi class`ni kengaytirish orqali yangi class yaratamiz

```python
class Ishchi:
    def __init__(self, ism, familiya, sharif, yosh):
        print('Obyekt yaratildi')
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

```

Yuqorida `Shafyor` nomli klass e'lon qildik. Merosligini bildirish uchun `Shafyor(Ishchi)` - qavs ichida
qaysi klassdan meros olayotganimizni bildiradi. Etibor bersangiz `Shafyor` klassda `fish` metodi yo'q.
Lekin, meros tufayli undan foydalansak bo'ladi

```python
shafyor = Shafyor("Sardor", "Ibragimov", "Xo'lmo'min o'g'li", 26, "AA4567Q")
shafyor.fish()
shafyor.sertfikat_nomeri()
```

Natija

```python
Ibragimov Sardor Xo'lmo'min o'g'li, 26 yoshda
Haydovchilik guvohnomasi nomeri:  AA4567Q
```


## Xulosa

Biz bugun classni ko'rib chiqdik, va eng asosiy malumotlarni bildik. Albatta bu o'rganlarimiz boshlanishi holos.
Jumdladan quyidagilarni o'rgandik:

- attribut classga tegishli bo'lgan o'zgaruvchi
- class qolip - obyektni elon qilish uchun ishlatiladi
- bola class mavjud classdan yangi class yaratilishi. Mavjud class ona class ham deb ataldi 
- meros yangi (bola) class boshqa (ona) classdan meros qilinib yaratilishi. Bunda, bola class
 ona classga tegishlig bo'lgan barcha attributlar va metodlarni o'z ichiga oladi, hamda qo'shimcha atributlar 
 va metodlarga ega bo'ladi 
- metod class ichida elon qilingan funksiya
- obyekt classning chaqirishdan hosil bo'ladi.















