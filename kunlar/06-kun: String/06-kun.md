# String

Stringlar bu sonlar yoki mantiqiy amallardan ajralib turadi. String bu ketma-ket 
__tartibda__ kelgan belgilardir.

## String bu ketma-ketlik

String bu ketma-ket kelgan belgilardir. Belgilardan xoxlaganinigiz bilan ishlash uchun 
braket `[]` operatori orqali bo'ladi. 
Masalan

```python
ism = `Nuriddin`
belgi = ism[1]
```

Dehqonchasiga, ism o'zgaruvchisi qiymatining birinchi belgisini olib, uni `belgi` o'zgaruvchisiga
ga yuklagin.

Braket ichidagi son **indeks** deb ataladi. Indeks belgilardan aynan qaysiligini bildiradi.

```python
print(belgi)
```

```commandline
---
'u'
```

Lekin etibor bergan bo'lsangiz, indeks `1` ga teng. Lekin, bizda `u` belgisi konsolga chiqdi.
Buni sababi, pythonda sanash, indekslash, `0` dan boshlanadi, 0, 1, 2, vahokazo.

```python
belgi = ism[0]
print(belgi)
```

```commandline
---
'N'
```

Indeks sifatida, biz o'zgaruvchi hamda ifodalardan foydalansak bo'ladi.

```python
i = 0
print(ism[i])
print(ism[i+1])
```

```commandline
'N'
'u'
```

Lekin, indeks qiymati har doim **butun son** bo'lishligi shart. Aks holda ERROR

```python
belgi = ism[1.7]
```

```commandline
------------------------------------------
TypeError: string indices must be integers
```
Tarjimasi: Turda xato ketayapti: string indekslari butun son bo'lishi shart.

## len

Bu funksiya stringda nechta belgi borligini hisoblab qaytaradi.

```python
ism = `Nuriddin`
uzunligi = len(ism)
print(uzunligi)
```

```commandline
--
8
```

Stringdagi oxirgi begini olish uchun nima qilgan bo'lardingiz? 

Odatda, shoshilib biz quyidagicha qilishimiz mumkin,

```python
oxirgi_belgi = ism[uzunligi]
```

Ishlatsak quyidagi xatoni olamiz. 

```commandline
-------------------------------------
IndexError: string index out of range
```

Tarjimasi: indeks xatosi: indeks chegaradan oshib ketdi. 

Sabab shundaki, `ism` qiymatining 8-indeksida belgi yo'q. Chunki, pythonda sanash 0 dan boshlanadi. Yani
0 dan toki 7 gacha bo'ladi. Oxirgi belgini olish uchun butun uzunlikdan `1` ni ayirishimiz kerak,

```python
oxirgi_belgi = ism[uzunligi]
print(oxirgi_belgi)
```
```commandline
---
'n'
```

Yoki, manfiy butun sondan foydalansangiz bo'ladi. Bunda stringning oxiridan boshlab sanagandek
bo'ladi. Oxirgini letterni olish uchun `ism[-1]` qilamiz bo'ldi.


## `for` orqali belgidan belgiga o'tish

Ko'pincha hisoblashlar birin ketin, bitta belgidan amalga oshirilib boriladi. Stringnig birinchi belgisini 
olamiz. U ustida biron amal bajramiz. Keyingi belgiga o'tamiz. Shunday qilib oxirgi belgigacha boramiz.
Bunday holat **traversal** deb ataladi. 

Traversal qilishning, bir usuli biz o'tgan `while` dan foydalansak bo'ladi

```python
indeks = 0
while indeks < len(ism):
   belgi = ism[indeks]
   print(belgi)
   indeks = indeks + 1
```

Bunda, boshida indeks `0` bo'lgan. `while` shartida `indeks < len(ism)` yani indeks qachonki string 
uzunligiga teng bo'lsa, shart buziladi va `while` tana qismi ishlamaydi.

Boshqacha usuli, `for` orqali:

```python
for belgi in ism:
    print(belgi)
```

`for` bunda yuqoridagi `while` bilan bir xil ishni bajarayapti. `for` tushunishga ancha sodda.
Dehqonchasiga, `ism` qiymatini belgisini birin-ketin `belgi` o'zgaruchisiga yukla va 
konsolga chiqargin.



## Stringni bo'laklash

String bo'lagi **slays** deb ataladi.  Bo'lakni tanlash ham belgini tanlashga o'xshaydi.

```python
ism = 'Nuriddin'
bulak = ism[0:3]
print(bulak)
```

```commandline
----
'Nur'
```

`[m:n]` operatori m dan n gacha bo'lgan belgilarni chiqaradi. Yodda tutish kerak, n-belgi bo'lakga kirmaydi 
va `m` kiradi. 

Agar, `m` olib tashlasak, python demak stringning boshidan boshlayman deb tushunadi. 
Agar `n` olib tashlasak, bo'lak string oxirigacha ekanligini bildiradi.

```python
ism = 'Nuriddin'
print(ism[:3])
print(ism[3:])
```

```commandline
-----
'Nur'
'iddin'
```

Agar, `m` va `n` teng bo'lsa, u xolda nataja **bo'sh string** bo'ladi.

```python
print(ism[3:3])
```

```commandline
--
''
```

Bo'sh stringda hech qanday belgi bo'lmaydi va uzunligi `0` ga teng.


## String bu `immutable`

Quyidagi programma berilgan bo'lsin,

```python
ism = 'sardor'
```

Shu o'zgaruvchining birinchi harfini kattasiga o'zgartirmoqchimiz (s ni S). Bunda

```python
ism[0] = 'S'
```

Lekin bunday qilish mumkin emas. Agar ishlatsangiz, quyidagi xatoni olasiz

```commandline
--------------------------------------------------------
TypeError: 'str' object does not support item assignment
```

Tarjimasi: turda xato ro'y berdi, stringga yuklab bo'lmaydi. 

Sababi string **immutable** bo'lganligi uchun. Immutable o'zgarmaydigan degani. 

Baribir yuqoridagi muammoni yechmoqchi bo'lsangiz, quyidagicha qilishingiz mumkin

```python
ism = 'sardor'
yangi_ism = 'S' + ism[1:]
print(yangi_ism)
```

```commandline
------
Sardor
```

Bunda biz yangi belgi olaytapmizda, uni `ism`dan bo'lak olib ulashtirayapmiz. Keyin, uni `yangi_ism`ga 
yuklayapmiz. Asl ism o'zgaruvchisiga tasir ko'rstaganimiz yo'q.



## Qidirish

Quyidagi programma nima qiladi deb o'ylaysiz?

```python
def qidir(yozuv, harf):
   indeks = 0
   while indeks < len(yozuv):
        if yozuv[indeks] == harf:
            return indeks
        indeks = indeks + 1
   return -1
```

Yuqorida `[]` operatori orqali belgini (harf) olgandik. Yani indeks olib usha indeksda turgan harfni
ajratadi. `qidir` funsksiyasida esa, xuddi shuning aksini qiladi. Biz harf beramiz va harf turgan 
indeksni qaytaradi (`return indeks`). Agar harf topilmasa, `-1` qaytaradi.

`qidir` funksiyasida biz o'rgangan bilimlarimizdan ko'pi qo'llanilayapti. 

`if yozuv[indeks] == harf` agar yozuv indeksdagi belgi `harf` ga teng bo'lsa, loop shu yerda tugaydi 
keyin `return indeks` indeksni qaytaradi.

Agar belgi (harf) yozuvda bo'lmasa, programma loopdan odatdagidek chiqib ketadi va `-1` ni qaytaradi.

Man shunday hsioblash jarayoni **search** deb ataladi. Tilimizda esa **qidirish**.


## Belgilarni sanash

Quyidagi programma berilgan stringga `r` belgisi necha marta ishtirok sanaydi.

```python
ism = 'Sardor'
sana = 0
for belgi in ism:
    if belgi == 'r':
        sana = sana + 1

print(count)
```

```commandline
--
6
```

Bu programma programistlar ko'p ishlatadigan yana bir ko'nikmaga misoldir. Bu `counter` (kaunter, sanash) 
deb ataladi.

`sana` o'zgaruvchisiga 0 yuklandi. Keyin agar qidirilayotgan belgi mavjud bo'lsa inkrement qilindi.
Loop tanadan chiqganida `sana` o'zgaruvchisi umumiy `r` sonini o'z ichiga oladi.


## String metodlari

Stringda bir necha ko'p qo'llaniladigan foydali metodlar mavjud. Masalan, `upper` metodi.

```python
ism = 'Sardor'
yangi_ism = ism.upper()
print(yangi_ism)
```

```commandline
------
SARDOR
```

Bunda, `.` kerakli metodni chaqirishga yo'l ochadi yani `upper` bu holatda. Bo'sh qavslar esa `()`
bu metod hech qanday argumentlar olmasligini bildiradi.


Metodlarni bunday chaqirish **invocation** deb ataladi. Yani, biz `ism`ga `upper` methodini 
chaqirayapmiz.  

Qiziq, stringda biz yuqirida ko'rib o'tgan **qidir** funksiyasiga o'xshash metod bor. U `find` deb
ataladi. 

```python
indeks = ism.find('S')
print(indeks)
```

```commandline
0
```

Bu misolda, `find` metodini `ism`dan chaqirib, qidirayotgan belgini (`'S'`) argument sifatida berayapmiz.

Aslida, `find` `qidir`ga nisabatan ko'proq holatlarda ishlaydi.

Xususan, `find` bo'laklarni ham qidira oladi.

```python
indeks = ism.find('do')
print(indeks)
```

```commandline
-
3
```

`find` ikkinchi argumentni ham olishi mumkin. Bunda, 2-argument qidirish boshlangich nuqtasini taminlaydi.

```python
ism.find('do', 4)
```

```commandline
--
-1
```
`-1` chiqganligi sababi `'do'` 4-indeksdan keyin mavjud emasligi.



## `in` operatori

`in` operatori boolean operotori hisoblanadi. Masalan biz biron belgining biron yozuv ichida borligini
bilishimizga to'gri keladi. Masalan, 'a' belgisi bilan boshlanadigan mevalarni aniqlash programmasi
kerak bo'lsin. Qanday qilamiz? 

Bunda albatta bizga solishtishimiz uchun qandaydir operator kerak.

Stringlar uchun shu maqsadda `in` operatori qo'llaniladi.

```python
print('d' in ism)
print('k' in ism)
```

```commandline
-----
True
False
```

Agar birinchi belgi (`'d'`) `ism` da mavjud bo'lsa `True` aks holda `False` qaytaradi.



## Stringlarni taqqoslash

- `==` ni qo'llasak bo'ladi. 2 stringni taqqoslash 
   ```python
   if ism == 'Mahmud':
        print('Adash!')     
   ```
- boshqa taqqoslashlar `<` yoki `>` esa alphabet tartibi bo'yicha solishtiradi.
- Katta harflar har doim kichik harflardan oldin keladi.
   ```commandline
   Kun, Biz, ajoyib, yashil 
   ```
  
Ko'pincha biz stringlarni solishtirdan oldin, hammasini katta harfga yoki kichik harfga 
o'tkazib olamiz.


## Foydali terminlar

- **sequence**: ketma-ket tartibda kelgan beligilar to'plami
- **index**: indeks, butun sonli qiymat. Stringdan belgilarni tanlashda qo'llaniladi. Masalan so'zdan harfni
ajratish uchun.
- **slice**: bo'laklash. Stringning bir bo'lagi. Odatda, bo'lak `[m:n]` orqali olinadi.
- **bo'sh string**: belgisiz string va uzunligi 0 ga teng. `''` bilan belgilanadi.
- **invocation**: metodni chaqirish. 
- **search**: qidirish. 
- **traverse**: string belgilariga birma-bir tashrif buyurish. 
- **immutable**: o'zgarmaydigan. Ketma-ketlik xususiyati bo'lib ketma-ketlik o'zgarmasligini bildiradi.
- **counter**: kaunter. Sanash uchun ishlatiladigan o'zgaruvchi. Odatda `0` dan boshlanib va keyin inkrement 
  qilinib boriladi.
  


## Problem solving
1. Sequence nima? Javobni konsolga chiqaring.
   ```python
   print("Javob: ketma-ket tartibda kelgan beligilar to'plami")
   ```   
2. Immutable nima? Javobni konsolga chiqaring.
3. search nima? Javobni konsolga chiqaring.
4. Kaunter nima? Javobni konsolga chiqaring.
5. Invocation nima? Javobni konsolga chiqaring.
6. slice nima? Javobni konsolga chiqaring.
7. bo'sh string nima? Javobni konsolga chiqaring.
8. Indeks nima? Javobni konsolga chiqaring.
9. string methodlaridan biri bo'lmish `strip` nima qiladi?
10. string methodlaridan biri bo'lmish `replace` nima qiladi?
11. string methodlaridan biri bo'lmish `lower` nima qiladi?
12. string methodlaridan biri bo'lmish `upper` nima qiladi?
13. string methodlaridan biri bo'lmish `count` nima qiladi?
14. palindrom degan funksiya programmasini tuzing. Palindrom degani bir so'zning
    to'g'ri va teskarisi bir zil degani. Masalan , katak, bob.

15. Mane bu funksiya nima qiladi?

   ```python
   def harqanday_kichikharf(s):
       for c in s:
           if c.islower():
               return True
           else:
               return False
   ```
16. Quyidagi Python kodni olingda, `find` va bo'laklashdan foydalanib son bor joyni ajratib oling.
keyin uni haqiqiy songe `float` dan foydalanib o'tkazing. NAtijani konsolga chiqaring
    
```python
massa = "Kompyuter:6.78 kg"
```

