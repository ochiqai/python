# List


## List bu ketma-etlik

Stringga o'xshash, `list` ham qiymatlar ketma-ketligi. Stringda 
qiymatlar asosan belgi bo'ladi, `List`da esa ular har qanday turda
bo'lishligi mumkin. Listdagi qiymatlar **elementlar** deb ataladi. 
Pythonda, `element` yoki `item` deb ataladi. 

`List`larni yaratishning bir necha turi mavjud. Eng osoni 
elementlarni kvadrat qavsga olinib qilinadi.

```python
ballar = [55, 80, 70, 84, 91]
ismlar = ['Ulugbek', 'Nuriddin', 'Davron']
```

Birinchi misol, 5 ta butun songa tegishli elementlardan iborat va
ular `ballar` o'zgaruvchisiga yuklangan.
Ikinnchi misol 3 ta stringdan iborat. 

List barcha elementlari bir turga mavjud bo'lishligi shart emas.

```python
aralash = ['salom', 3.14, 10, 20]
```

List ichida yana list ham bo'lishligi mumkin

```python
ichki_list = [1, [10, 20], 10]
```
Bu Pythonda **nested** list deb ataladi.

Hech qanday elementga ega bo'lmagan list bo'sh list deb ataladi.
`[]` operatori orqali bo'sh listni hosil qilishimiz mumkin.

```python
bush = []
```

## List o'zgaradigan

Elementlarni ajratib olish xuddi stringdagi belgilarni ajratib 
olish kabi `[indeks]` orqali amalga oshiriladi. Yodda tutamiz
indeks `0`dan boshlanadi.

```python
print(ismlar[0])
```

```commandline
--------
Ulugbek
```

Stringlardan farqli tarafi shundaki, list elementlarini o'zgartirish mumkin.
Yani, 

```python
sonlar = [1,2,3,4]
print(sonlar)
sonlar[0] = 44
print(sonlar)
```

```commandline
[1, 2, 3, 4]
[44, 2, 3, 4]
```

Yuqorida 0 indeksidagi elementni 44 ga o'zgartirayapmiz.

Listlarni biz indeks va elementlarni boglaydigan vosita deb 
atashimiz mumkin. Bu narsa, pythonda `mapping` deb ataladi.

List indekslari xuddi string indekslari kabidir: 
- indeks butun son bo'lishi kerak
- indeks elementlar sonidan oshib ketmasligi kerak aks holda 
  `IndeksError` indeks xato ro'y beradi.
- agar indeks manfiy bo'lsa, list orqa tarafidan keladi.

`in` operatori ham xuddi stringdagi kabi ishlayveradi.

```python
katta_harflar = ['A', 'B', 'C']
print('A' in katta_harflar)
print('K' in katta_harflar)
```

```commandline
-----
True
False
```


## List traversali

Listlarni traversal qilishning qulay yo'li `for` halqasi orqalidir.
Va xuddi stringdagidek bo'ladi:

```python
for harf in katta_harflar:
    print(harf)
```

Agar siz elementlarni o'zgartirmoqchi bo'lsangiz, `range` va `len`
funksiyalaridan foydanlansak qulay bo'ladi:

```python
sonlar = [1, 2, 3]
for i in range(len(sonlar)):
    sonlar[i] = sonlar[i] + 10
```

Bunda `for` halqasi listni traversal qiladi va har bir elementni 
yangilaydi. Yani 10 qo'shadi. `len` list umumiy sonini bildiradi.
`range` 0 dan n - 1 gacha indekslarni qaytaradi. Bu yerda `n` 
list elementlari umumiy sonidir. Har bir iteratsiyada `i` keyingi
element indeksini oladi. Tanadagi ifoda esa `i`dan foydalanib
elementning eski qiymatini oladi va yangi qiymatni yuklaydi.

Agar list bo'sh bo'lsa, halqa tanasi ishlamaydi.

```python
bush = []
for x in bush:
    print('Hech qachon ishlamaydi')
```

Yuqorida kurganimizdek list o'z elementi sifatida yana listni 
olishligi ham mumkin. Bunda ichki list nested list ham deb 
atalishini bildik. Lekin listdagi elementlarning umumiy sonini
olayotganimizda biz nested listni 1 ta element de qabul qilamiz.

```python
x = [1, 2, 3, [1, 2, 3]]
print(len(x))
```
```commandline
--
4
```


## List operatorlari

`+` operatori listlarni bir-biriga bog'laydi.

```python
a = [1, 2]
b = [3, 4]
c = a + b
print(c)
```

```commandline
-------------
[1, 2, 3, 4]
```

`*` operatori berilgan son marta qaytaradi.

```python
nollar = [0] * 5
print(nollar)
alar = ['a'] * 5
print(nollar)
print(alar)
```

```commandline
-------------------------
[0, 0, 0, 0, 0]
['a', 'a', 'a', 'a', 'a']
```


## Listlarni bo'laklash

Bo'laklash xuddi string kabi ishlaydi

```python
alphabet = ['a', 'b', 'c', 'd', 'e']
print(alphabet[:4])
print(alphabet[1:4])
print(alphabet[4:])
```

```commandline
--------------------
['a', 'b', 'c', 'd']
['b', 'c', 'd']
['e']
```

## List metodlari

Listlar ustida ishlashni qulaytirish uchun Pythonda tayyor metodlar bor.
Masalan,
Listga yangi element qo'shmoqchi bo'lsangiz, `append` dan foydalanamiz

```python
harflar = ['a', 'b', 'c']
harflar.append('d')
print(harflar)
```

```commandline
--------------------
['a', 'b', 'c', 'd']
```

`sort` metodi listni sartirovka qiladi: kichikdan kattagacha.

```python
a = [3, 2, 1, 4]
a.sort()
print(a)
```

```commandline
------------
[1, 2, 3, 4]
```

List metodlari hech narsa qaytarmaydi. 



## Elementlarni o'chirish

Listdan elementlarni o'chirishda vaziyatga qaraladi.
Agar indeks berilgan bo'lsa, `pop` metodidan foydalansak 
bo'ladi. 

```python
sonlar = [0, 1, 2]
x = sonlar.pop(1)
print(sonlar)
print(x)
```

```commandline
------
[0, 2] # sonlar listida 1 soni o'chirilda va 2 ta son qoldi
1 # o'chirilgan son
```

Agar indeks berilmasa, `pop` oxirgi elementni o'chiradi va o'sha 
o'chirilgan elementni qaytaradi.

Agar sizga qaytarilgan element kerak bo'lmasa, `del` operatoridan
foydalanamiz:

```python
del sonlar[1]
print(sonlar)
```

```commandline
------
[0, 2] 
```

Agar siz indeksni bilmay, qiymatni bilsangiz unda `remove` dan 
foydalanasiz. 

```python
sonlar = ['a', 'b', 'c']
sonlar.remove('a')
print(sonlar)
```
```commandline
-----------
['b', 'c']
```

Agar birdan ortiq elementlarni o'chirmoqchi bo'lsangiz, bo'lakdan 
foydalansangiz bo'ladi.

```python
sonlar = ['a', 'b', 'c']
del sonlar[:2]
print(sonlar)
```
```commandline
-----------
['c']
```

Odatdagidek `2` soni kirmaydi, balki o'shangacha bo'lgan son kiradi.


## List va funksiyalar

List ustida keng qo'llaniladigan tayyor funksiyalar mavjud.

- `len`: list uzunligini qaytaradi
- `min`: list elementlaridan eng kichigini chiqaradi
- `max`: list elementlaridan eng kattasini chiqaradi
- `sum`: barcha list elementlarini qo'shadi. List elementlari faqat son 
  bo'lishligi kerak.

```python
sonlar = [1, 2, 3, 4, 5, 6, 7]
print(len(sonlar))
print(min(sonlar))
print(max(sonlar))
print(sum(sonlar))
```

```commandline
---
7
1
7
28
```

## Listlar va stringlar

String - bu belgilar ketma-ketligi. List - bu qiymatlar ketma ketligi.
belgilar listim belgilar ketma -ketligidan farq qiladi.
Stringni listga konvert qilish uchun `list` funksiyasidan 
foydalanamiz.

```python
x = 'salom'
y = list(x)
print(x)
```

```commandline
-------------------------
['s', 'a', 'l', 'o', 'm']
```

Eslatma: `list` bu kalit so'z bo'lganligi uchun o'zgaruvchi nomi sifatida
foydalanmislik kerak.

`list` funsksiyani berilgan stringni yuqorida bo'larlarga bo'ldi.
`split` funksiyasi bilan gapni so'zlarga ajratishimiz mumkin

```python
gap = "O'zbekiston keljagi buyuk davlat"
suzlar = gap.split()
print(suzlar)
```

```commandline
---------------------------------------------
["O'zbekiston", 'keljagi', 'buyuk', 'davlat']
```


Aplit boshqa hollarda ham qo'llashimiz mumkin. Xususan
quyidagi suzni olaylik: `ke-la-jak-python`. Ushbu so'zni
`-` asosan bo'laklashimiz mumkin.

```python
s = "ke-la-jak-python"
s.split('-')
```

```commandline
-----------------------------
['ke', 'la', 'jak', 'python']
```

Xo'sh `split` beilgan narsani bo'lar ekan. Unda bizga bo'lingan narsa 
bo'lsa uni qanday qilib qo'shamiz?
Bu holatda `join`dan foydalanamiz.

```python
x = ['ke', 'la', 'jak', 'python']
s = '-'.join(x)
print(s)
```
```commandline
----------------
ke-la-jak-python
```


## Obyektlar va qiymatlar
Agar quyidagini ishlatsak,

```python
a = 'olma'
b = 'olma'
```

Bilamizki `a` va `b` o'zgaruvchilariga `olma` qiymati 
yuklanayapti. Lekin, biz bilmaymiz ushbu o'zgaruvchilar
aynan bir xil `olma` qiymati yuklanayaptimi?

Bunda 2 holat bo'ladi.
- 1) a va b larga ikki xil obyekt faqat bir xil qiymat yuklanayapti
- 2) ular aynan bir xil obyektga yuklanayapti.
    
Buni quyidagicha tekshirimiz uchun `is` operatoridan foydalanamiz.

```python
a = 'olma'
b = 'olma'
print(a is b)
```
```commandline
-----
True
```

Misoldan, Python faqatgina 1 ta obyekt yaratgan. Ikkala a va b lar
o'sha obyekt yuklatilgan.

Lekin, 2 ta `list` hosil qilsak ularda 2 ta obyek bo'ladi!

```python
a = [1, 2]
b = [1, 2]
print(a is b)
```
```commandline
------
False
```

Bunda holatda, ikkala list ekvivalent chunki ularda bir xil elementlar
bor. Lekin ular aynan bir xil emas chunki ular aynan bir xil obyekt emas.

Obyekt va qiymatning farqini aniqlashtirsak: obyekda qiymatga 
bo'ladi. Yani, `a = [1, 2]`.  Bu yerda `a`ga list obyektini 
yuklanayapti. `list` obyekti qiymati bir necha elementlardan 
tashkil topadi `[1, 2]`.


## Taxallus

Quyidagi kodda **taxallus** qilinayapti.

```python
a = [1, 2, 3]
b = a
print(b is a)
```
```commandline
----
True
```

Bu yerda, a va b aynan bir xil obyektga yo'naltirilayapti.
O'zgaruvchini obyektga bog'lash referns (reference) deb ataladi.
Yuqoridagi misolda, 2 ta referns bitta obyektga yo'naltirilayapti.

Agar obyektga birdan ortiq referns bo'lsa aytamizki bu obyekt 
taxalluslandi. 

Agar taxalluslanadigan obyekt mutable (o'zgaradigan) bo'lsa,
refernslardining birining o'zgarishi boshqalariga ham ta'sir qiladi.

```python
a = [1, 2, 3]
b = a
b[2] = 55
print(a)
```
```commandline
----
[1, 2, 55]
```
Bunday o'zgarish ko'pincha kodlashda xatoliklarni keltirib
chiqaradi.  O'shaning uchun o'zgaradigan (mutable) obyektlar bilan
ishlaganda, iloji boricha taxalluslashdan 
foydalanmasligimiz kerak.

O'garmaydigan (immutable) o'zgaruvchilar bilan ishlaganda esa,
taxalluslash muammo emas, chunki birini o'zgartirsangiz boshqalariga
ta'sir qilmaydi.



## List argumentlari

Qachonki funksiyaga listni argument sifatida bersak, funksiya 
listga referns oladi. Agar funksiya listni o'gartirsa, 
tashqarida ham o'zgaradi. Masalan, birinchi elementni o'chiradigan 
funksiyani kodlaylik:

```python
def birinchi_uchir(a):
    del a[0]
sonlar = [1, 2, 3, 4, 5, 6]
birinchi_uchir(sonlar)
print(sonlar)
```
```commandline
---------------
[2, 3, 4, 5, 6]
```

Parameter a va sonlar aynana bir xil obyektga taxallus qilingan.


Listni o'zgartiradigan va yangi list hosil qiladigan 
operatorlarni farqlash muhim. Masalan, `append` metodi, listni 
o'zgartiradi, lekin `+` yangi list hosil qiladi.

- `append`

```python
a = [1, 2]
b = a.append(3)
print(a)
print(b)
```
```commandline
------
[1, 2, 3]
None
```

- `+`

```python
a = [1, 2]
b = a + [3]
print(a)
print(b)
```
```commandline
------
[1, 2]
[1, 2, 3]
None
```




## Foydali terminal

- **taxalluslash (aliasing)**: 2 va undan ortiq o'zgaruvchilarning 1 ta obyektga
  bog'lanishi
- **element**: list qiymatlaridan biri
- **ekvivalent**: bir xil qiymatlarni olish
- **indeks**: list elementini oladigan butun son
- **list**: qiymatlar ketma-ketligi
- **list traversal**: list elemenlarini birma bir ko'rish
- **nested list**: list ichida yana list
- **obyekt**: o'zgaruvchi ko'rsatiladigan joy
- *referns***: o'zgaruvchi va uning qiymatini boglaydigan bo'g'in



## Problem solving

1. List nima?
2. Obyekt nima?
3. Referns nima?
4. Nested list nima?
5. Element nima?
6. taxallushlash nima?
7. Ekvivalent nima?
8. List traversal nima?
9. `x = [103, 32, 3, 40, 5, 6]` eng katta qiymatni toping.
10. `x = [103, 32, 3, 40, 5, 6]` eng kichik qiymatni toping.
11. `x = [103, 32, 3, 40, 5, 6]` barcha elementlar yig'indisini toping.
12. `x = [103, 32, 3, 40, 5, 6]` barcha elementlar ko'paytmasini toping.
13. `s = ['a', 'b', 'c']` 2-elementni `B` ga konvert qiling.
14. `s = ['a', 'b', 'c']` 2-elementni `2` ga konvert qiling.
15. List oxirgi elementini o'chiradigan funksiya tuzing.
16. `range` funsksiyasi nima qiladi?
17. `len` funksiyasi nima qiladi?
