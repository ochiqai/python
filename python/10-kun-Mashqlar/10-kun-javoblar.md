# Problems
> Ushbu mashqlar oson bajarganlar uchun koni foyda <br >
> Asosiy maqsad ko'nikma hosil qilish 9 kun davomida o'rgangan narsalarni <br >
> Mashqlar soni 134 ta, lekin oshib boraveradi vaqtga qarab. <br >

1. Quyidagi qiymatlarning turlarini ayting?

   1. 100
   2. 0
   3. Python
   4. 4.0
   5. 3.0
   6. 2017
   
   <details><summary>Javob</summary>
   
   ```python
   print(type(100))
   ```
   </details>

2. Konsolga `"Salom Python"` deb chiqaring.

   <details><summary>Javob</summary>
   
   ```python
   print("Salom Python")
   ```
   </details>

3. Konsolga `"Salom 'Python'"` deb chiqaring.

   <details><summary>Javob</summary>
   
   ```python
   print("Salom 'Python'")
   ```
   </details>

4. Konsolga `"Salom *Python*"` deb chiqaring. 

   <details><summary>Javob</summary>
   
   ```python
   print("Salom *Python*")
   ```
   </details>

5. O'zgaruvchidan foydalanib `"Salom Python"` ni konsolga chiqaring.

   <details><summary>Javob</summary>
   
   ```python
   xabar = "Salom Python"
   print(xabar)
   ```
   </details>

6. Define two variables `a = 11` and `b = 599`. Quyidagilarni hsioblab konsolga chiqaring:

    1. a + b
    2. a − b
    3. a · 10
    4. b/4
    5. a + 15 − b · 3

7. Quyidagilarning qaysisi to'g'ri
    1. solinadiganlar = Milk, flour, eggs
    2. london-population = 8800000
    3. n = 3.14159
    4. string = 100
    5. apples amount = 10
    6. uk capital = London
    7. 123456 = 123456

8. Programma tuzing. U foydalanuvchidan ismni kiritishni so'rasin. Keyin, kiritilganni konsolga chiqarsin.

   <details><summary>Javob</summary>
   
   ```python
   ism = input("ismingizni kiriting: ")
   print(ism)
   ```
   </details>
   
9. Berilgan ushbu stringda `a = "salomlar"`, quyidagi amallarni bajaring:
    
       1. Harflarni katta harfga o'tkazing
       2. Harflarni kichik hargga o'tkazing
       3. `'l'` harfi necha marta takrorlanayotganini aniqlang
       4. `'a'` harfichi?
       5. `'m'` harfi indeksini toping 

       Quyidagi tayyor funksiyalardan foydalaning. `upper(), lower(), count(), and find()` 
      
      <details><summary>Javob</summary>
      
      ```python
      a = "salomlar"
      
      # 1. Harflarni katta harfga o'tkazish.
      print(a.upper())

      # 2. Harflarni kichik hargga o'tkazish.
      print(a.lower())

      # 3. 'l' harfi necha marta takrorlanayotganini aniqlash.
      print(a.count('l'))

      # 4. 'l' harfi necha marta takrorlanayotganini aniqlash.
      # for orqali aniqlash.
      t = 0
      for i in a:
          if i == 'a':
              t += 1
      print(t)
      
      # 5. 'm' harfni indeksini topish.
      print(a.find('m'))
      ```
      </details>


10. Programma tuzing. U foydalanuvchi ismi va qaysi mamlakatdan ekanligini so'rasin. Keyin konsolga quyidagini chiqarsin

    ```python
    Ali Qulov (UZ)
    ```
    Yordamchi funksiyalar: `input()` (foydalanuvchidan kiritishni so'rash uchun). `upper()` (harflarni katta qilish uchun).
 
11. Quyidagi kodga qarang

    ```python
    # foydalanuvchidan so'rang
    ism = input("Iltimos ismni kiriting: ")
    familiya = input("Iltimos familiyani kiriting: ")
    yosh = input("Iltimos yoshingizni kiriting: ")
    ```

    ```python
    Iltimos ismni kiriting: Usmon  
    Iltimos familiyani kiriting: Nosirov
    Iltimos yoshingizni kiriting: 20
    ```
    
    ```python
    natija = familiya.upper()
    natija = natija + ', '
    natija = natija + ism
    natija = natija + " ("
    natija = natija + yosh
    natija = natija + ")"
    print(natija) 
    ```

    `natija` nima bo'ladi. Birinchi yodda bajaring. Keyin, kodni yozing va javoginzni solishtirich? 

12. Quyidagi string berilgan, `'yuksaklikdan'`. Bundan, `a, y, s` harflarini ajratib konsolga chiqaring.

13. Foydanlanuchidan ism va fmiliyaisni so'rangda, quyidagicha konsolga chiqaring.

    ```python
    Usmon Nosir [UN]
    ```

    Yani, kiritilgan ism va familyani hamda ularning birinchi harflarini olingda to'rtburchak qavsga olib chiqaring - 1 qatorda chiqsin.

       <details><summary>Javob</summary>
       
       ```python
       ism = input("Ismingizni kiriting: ")
       familya = input("familyangizni kiriting: ")
       print(f"{ism.title()} {familya.title()} [{ism[0].title()}{familya[0].title()}]")
       ```
       </details>

14. `oyatvasuralar` stringidan `oyat` va `sura` ni ajratib konsolga chiqaring.

       <details><summary>Javob</summary>
       
       ```python
       suz = 'oyatvasuralar'
       print(suz[0:4])
       print(suz[6:10])
       ```
       </details>

15. Quyidagi amallarni hisoblang va konsolga chiqaring.

    - 15 + 35.6 + 20.78 − 0.01
    - 0.5 + (0.8 · 0.5) − 0.333
    - (0.5 + 0.8) · (0.5 − 0.333)
    - 100/(400 · 4)
    - 100/400 · 4
    - 2.0 5 + 100
    - 2.0 (5+100)


16. Quyidagi kod berilgan:

    ```python
    son1 = 10
    son2 = 20
    son3 = 30
    son4 = -10
    son5 = 0.0
    son6 = 9999
    ```

    Solishtirish operatorlari orqali, quyidagilarni aniqlang,

    - (a) `son1` `son2` dan kichikmi?
    - (b) `son2` `son3` dan kattami?
    - (c) `son3` `son4` ga tengmi?
    - (b) `son4` `son4` ga teng yoki kattami?
    - (b) `son5` `son2` ga teng yoki kichikmi?
    - (b) `son2` `son3` sonlar bir xilmi?

17. Quyidagi kod berilgan:

    ```python
    son1 = 10
    son2 = 20
    son3 = 30
    son4 = -10
    son5 = 0.0
    son6 = 9999
    ```

    Matematik library orqali, quyidagilarni bajaring.

- (1) `son1` ni kvadraga oshiring.
- (2) `son2` ni ildizini toping.
- (3) `son3` ni modulini toping.
- (4) `son4` va `son1`larning modul qiymatlari bir xilmi? 
- (5) `son5` ning 3-darajasi `son1` dan kattami?
- (6) `son6` ni ildizi `son3` dan katta yoki tengmi?
- (7) `son6` ni 2 marta ildizga oling. Natija `son1`dan kattami?

    Eslatma, matematik modulni quyidagicha chaqirasiz va undan biron funksiyani quyidagicha chaqiramiz:

    ```python
    import math
    x = math.sqrt(son1)
    ```

18. Quyidagi formulalarga kod yozib, `y` ni hisoblang.

    - `x = 10`, `y = `$10x^2 + 5x + 1$
    - `x = 0.5`, `y = `$x^5 + 0.2$
    - `m1 = 0.5, m2 = 1.5`,  ` y = `$6.8*\frac{m1 * m2}{2}$

19. Mantiqiy operatorlar. Quyidagi jadvalni to'ldiring

    ![](.10-kun_images/mantiqiy_operatorlar.png)

20. Ushbu kod uchun 

    ```python
    son1 = 10
    son2 = 20
    son3 = 30
    son4 = -10
    son5 = 0.0
    son6 = 9999
    ```

    Quyidagilarni dilda bajaring. So'ngra kodda bajarib, dilingizdagi bilan solishtiring.

    - `(son1 > son2) or (son3 < son4)`
    - `(son6 == son1) and (son2 == son3)`
    - `((son1 + son2) > son4) or (son5 < son2)` 
    - `not (son1 != son6)`

21. Programma yozing. U foydalanuvchidan son kiritishni so'rasin. Agar, son musbat (noldan katta) bo'lsa `"musbat"` deb konsolga chiqarsin. Agar, manfiy (noldan kichik) bo'lsa `"manfiy"` deb chiqarsin. Agar ikkalasi ham bo'lmasa, `0` chiqarsin.
    
       <details><summary>Javob</summary>
       
       ```python
       son = int(input("son kiriting: "))
       if son > 0:
           print("musbat")
       elif son < 0:
           print("manfiy")
       else:
       print(0)
       ```
       </details>


22. Programma tuzig. U foydalanuvchidan harflarni kiritishni so'rasin. Agar harf unli bo'lsa, `"bu harf unli"` deb, aks holda `"bu undosh harf"` deb chiqarsin. Eslatma. Unli harflar: `a, i, u, o  e`.
     
       <details><summary>Javob</summary>
       
       ```python
       harf = input("harf kiriting: ")
       unli_harflar = ['a', 'i', 'u', 'o', 'e']
       if harf in unli_harflar:
           print("bu harf unli")
       else:
           print("bu undosh harf")
       ```
       </details>

23. Programma tuzing. U foydalanuvchidan sonlarni kiritishni so'rasin. Agar juft bo'lsa `"JUFT"`, aks holda `"TOQ"` deb chiqarsin. Eslatma. Son 2 ga bo'linsa, demak u juft son.
    
       <details><summary>Javob</summary>
       
       ```python
       son = int(input("son kiriting: "))
       if son % 2 == 0:
           print("JUFT")
       else:
           print("TOQ")
       ```
       </details>
 
24. Programma tuzing. U foydalanuvchidan yoshini so'rasin. Agar yoshi 15 dan katta bo'lsa, `Siz topshirishingiz mumkin`, aks holda `Mumkin emas` deb konsolga chiqarsin.
   
       <details><summary>Javob</summary>
       
       ```python
       yosh = int(input("Yoshingiz nechida: "))
       if yosh > 15:
           print("Siz topshirishingiz mumkin")
       else:
           print("Mumkin emas")
       ```
       </details>
  
25. Shunday list yarating, unda siz yoqtirgan 3 ta mamlakat yoki kitob yoki ism yoki sonlar bo'lsin. Va u listni `print()` orqali konsolga chiqaring.
     
       <details><summary>Javob</summary>
       
       ```python
       davlatlar = ["UZBEKISTAN", "RUSSIA", "USA"]
       print(davlatlar)
       ```
       </details>

26. Quyidagi berilgan
	```python
	viloyatlar = ['Samarqand', 'Toshkent', 'Surxondaryo', 'Qashqadaryo']
	```

	Konsolga:
	- har bir elementni chiqaring.
	- faqat boshidagi 3 elementni chiqaring.
	- oxirgi elementni chiqaring.
- Birinchi elementni `"Andijon"` ga o'zgartiring.
       
  <details><summary>Javob</summary>
       
   ```python
   viloyatlar = ['Samarqand', 'Toshkent', 'Surxondaryo', 'Qashqadaryo']
       
   # har bir elementni chiqaring.
   for i in viloyatlar:
       print(i)
   # faqat boshidagi 3 elementni chiqaring.
   for i in range(3):
       print(viloyatlar[i])
   # oxirgi elementni chiqaring.
   print(viloyatlar[-1])
   # Birinchi elementni `"Andijon"` ga o'zgartiring.
   viloyatlar[0] = 'Andijon'
   print(viloyatlar)
   ```
   </details>


27. 26-mashqda listni biz birdaniga yaratdik, to'rtburchak `[]` va `,` lardan foydalanib. Endi listni `append` funksiyasi orqali qiling. Keyin, listni hamma elementlarini konsolga chiqaring.
     
       <details><summary>Javob</summary>
       
       ```python
       viloyatlar = []
       viloyatlar.append("Toshkent")
       viloyatlar.append("Surxondaryo")
       viloyatlar.append("Samarqand")
       print(viloyatlar)
       ```
       </details>


28. Quyidagi list berilgan

    ```python
    sonlar = [1, 2, 3, 4, 5]
    ```

    `append()` funksiyasi  yordamida, quyidagini hosil qiling:

    ```python
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

       <details><summary>Javob</summary>
       
       ```python
       sonlar = [1, 2, 3,  4, 5]

       for i in range(6,10):
           sonlar.append(i)
       print(sonlar)
       ```
       </details>

29. Quyidagi list berilgan:

    ```python
    sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```
    
    Programma qiling. U foydalanuvchidan son kiritishni so'rasin. Agar kiritlgan son listda mavjud bo'lsa, `"bor"` deb chiqsin, aks holda "`yo'q`" deb chiqsin.

       <details><summary>Javob</summary>
       
       ```python
       sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]

       a = int(input('sonni kiriting = '))
       
       if a in sonlar:
           print('bor')
       else:
           print('yoq')
       ```
       </details>

30. `while` takrorlash operatoridan foydalanib, konsolga `salom python` deb 50 marta chiqaring.
    
       <details><summary>Javob</summary>
       
       ```python
       t = 0
       while t < 50:
           print('salom python ')
       t += 1
       ```
       </details>
 
31. Quyidagi list berilgan,

    ```python
    sonlar = [2, 4, 6, 7, 10, 11]
    ```
    
    `for` takrorlash operatori orqali list elementlarini konsolga chiqaring. 

       <details><summary>Javob</summary>
       
       ```python
       sonlar = [2, 4, 6, 7, 10, 11]
       for i in sonlar:
           print(i)
       ```
       </details>

32. `while` takrorlovchi operatori orqali, shunday list hosil qilingki unda `1` dan `199` gacha bo'lgan sonlar bo'lsin. Eslatma, `append()` dan foydalanishingiz mumkin.
    
       <details><summary>Javob</summary>
       
       ```python
       sonlar = []
       t = 1
       while t < 200:
           sonlar.append(t)
           t += 1
       print(sonlar)
       ```
       </details>
 
33. Programma qiling, foydalanuvchidan 5 ta yoqtirgan sonni so'rasin. Ularni `son` degan listga yuklab boring. `while` da foydalaning. 
   
       <details><summary>Javob</summary>
       
       ```python
       son = []
       t = 1
       while t < 6:
           print(t, '-', end=' ')
           a = int(input('sonni kiriting = '))
           son.append(a)
           t += 1

       print(son)
       ```
       </details>
  
34. Shunday programma qilingki, unda list elementlari 1 dan 20 gacha bo'lgan sonlarning kvadrati bo'lsin. Mn, `[1, 4, 9, 16, 25, ...]`.
   
       <details><summary>Javob</summary>
       
       ```python
       a = []
       t = 1
       
       while t < 21:
           a.append(t ** 2)
           t += 1
       print(a)
       ```
       </details>
  
35.  Quyidagi list berilgan,


```python
sonlar = [.2, .4, .6, .7, .10, .11]
```

List har bir elementini 100 ga ko'paytiring va konsolga chiqaring.     



   <details><summary>Javob</summary>

   ```python
   sonlar = [.2, .4, .6, .7, .10, .11]
   yangi_sonlar = []
   i = 0
   while i < len(sonlar):
       son = sonlar[i] * 100
       yangi_sonlar.append(son)
       i = i + 1

   print(yangi_sonlar)
   ```
   </details>

36.  Quyidagi list berilgan,

```python
sonlar = [.2, .4, .6, .7, .10, .11]
```

`yangi_sonlar` degan list hosil qiling. Ammo, bunda 
elementlar yuqoridagi list elemenlarini 100 ga ko'paytirishdan hosil qilinsin,
Yani, `yangi_sonlar = [20, 40, 60, 70, 10, 110]`

   <details><summary>Javob</summary>

   ```python
   sonlar = [.2, .4, .6, .7, .10, .11]
   yangi_sonlar = []
   i = 0
   while i < len(sonlar):
       son = int(sonlar[i] * 100)
       yangi_sonlar.append(son)
       i = i + 1

   print(yangi_sonlar)
   ```
   </details>

37. `salom_python()` nomli funksiya yarating. Chaqirilganda, konsolga `Salom Python` xabari chiqsin.
     
       <details><summary>Javob</summary>
    
       ```python
       def salom_python():
           print('Salom Python?')
       salom_python()
       ```
       </details>


38. `foydalanuchikiritgan(x)` nomli funksiya yarating. Foydalanuvchi kiritganini olib, konsolga `Siz x ni kiritdingiz` deb chiqsin. 

       <details><summary>Javob</summary>
    
       ```python
       def foydalanuvchi_kiritgan(x):
           print("Siz", x,"ni kiritingiz")
       foydalanuvchi_kiritgan(input('Son kiriting = '))
       ```
       </details>


39. Quyidagi `yigindi(a, b, c, d)` nomli funksiya yarating. Va u argumentlar yig'indisini qaytarsin. Mn: `yigindi(1, 0, 2, 10)` deb chaqirilganda 13 ni qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def yigindi(a, b, c, d):
           print(a + b + c + d)
    
       yigindi(1, 0, 2, 10)
       ```
       </details>


40. `yoshhisobi(yil)` nomli funksiya yarating. Va u `yil` parametri tug'ilgan yilni olsinda, yoshni qaytarsin. Mn: `1989` uchun `Siz 32 yoshdasiz` deb chiqarsin.  

       <details><summary>Javob</summary>
    
       ```python
       def yosh_hisobi(yil):
       yoshi = 2022 - yil
       return yoshi

       x = yosh_hisobi(int(input('tug`ulgan yilingizni kiriting = ')))
       print('siz', x, 'yoshdasiz')
       ```
       </details>


41. Sonlardan iborat list berilgan. Undan eng katta sonni qaytaring. Mn `a = [1, 30, 2]` uchun 30 qaytarsin.
     
       <details><summary>Javob</summary>
    
       ```python
       a = [1, 30, 2]
       print(max(a))
       ```
       </details>


42. Sonlardan iborat list berilgan. Undan eng kichik sonni qaytaring. Mn `a = [1, 30, 2]` uchun 1 qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       a = [5, 7, 9, 10]
       print(min(a))
       ```
       </details>
  

43. `ikki_max` nomli funksiya tuzing. Argument sifatida ikkita sonni olsin va ulardan kattasini qaytarsin. `if-else` dan foydalaning. (Bilamizki, Pythonda `max` degan funksiya mavjud, lekin undan foydalanmang).

       <details><summary>Javob</summary>
    
       ```python
       def ikki_max(a, b):
       if a > b:
           print(a)
       else:
           print(b)

       x = ikki_max(4, 10)
       ```
       </details>


44. `uch_max` nomli funksiya yarating. Uchta argument olsin va eng kattasini qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def uch_max(a, b, c):
           print(max(a, b, c))

       uch_max(10, 20, 30)
       ```
       </details>


45. `uzunlik` nomli funksiya yarating. Argument sifatida `list` yoki `string` turiga tegishli o'zgaruvchi qabul qilib uning uzunligini qaytarsin. (Bilamizki, Pythonda `len` degan funksiya mavjud, lekin undan foydalanmang).

       <details><summary>Javob</summary>
    
       ```python
       def uzunlik(x):
           t = 0
           for i in x:
               t += 1
           print(t)

       x = uzunlik(str(input()))
       ```
       </details>


46. `unlimi` nomli funksiya yarating. Funksiya argumenti sifatida stringda bo'lgan bitta harf olsin mn., 'a', 'b'. Agar argument unli bo'lsa, funksiya `True` aks holda `False` qaytarsin. 

       <details><summary>Javob</summary>
    
       ```python
       def unlimi(a):
           if a == 'a' or a == 'A' or a == 'i' or a == 'I' or a == 'o' or a == 'O' or a == 'E' or a == 'e' or a == 'U' or a == 'u':
               print('True')
           else:
               print('False')
       x = unlimi(input('harfni kiriting = '))
       ```
       </details>


47. `tarjima` degan funksiya yarating. `book` deb argumentga berilganda `kitob` deb qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       
       ```
       </details>


48. `yigindi` nomli funksiya yarating va u berilgan `list` yig'indisini topsin. Mn, `yigindi([1, 2, 4])` desak `7` qaytarish kerak. Shunga o'xshash, `kupaytma` degan funksiya ham yarating, va u verilgan list elementlarini bir-biriga ko'paytirsin. Mn, `kupaytma([1, 2, 3])`  `6` qaytarsin.  

       <details><summary>Javob</summary>
    
       ```python
       def yigindi(a):
           t = 0
           for i in a:
               t += i
           print(t)
       
       x = yigindi(list(map(int, input().split())))
       
       def kopaytma(a):
           t = 1
           for i in a:
               t *= i
           print(t)

       y = kopaytma(list(map(int, input().split())))
       ```
       </details>


49. `teskarisi` nomli funksiya yarating. Argument sifatida string olsin, va uni teskarisini chiqarsin. Mn, `teskarisi('salom')` desak `molas` deb qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def teskari(x):
           return x[::-1]
       
       print(teskari("salom"))
       ```
       </details>


50. `palindrommi` nomli funksiya yarating. Palindrom deb o'ngga ham chapga ham bir xil o'qiladigan so'zlarga aytiladi; mn., katak, non. Funksiya argument sifatida  string olsin va uni palindrom ekanligini aniqlasin. Agar palindrom bo'lsa `True`, aks holda `False` qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def palindrommi(x):
           if x == x[::-1]:
               print(True)
           else:
               print(False)
    
       palindrommi("katak")
       ```
       </details>


51. `azomi` nomli funksiya yarating. Bunda funksiya 2 ta argument qabul qilsin: biri list va ikkinchisi qiymat bo'lsin. Funksiya berilga qiymat listda bor yo'qligi aniqlansin. Agar bo'lsa `True` aks holda `False` qaytarsin. (Bilamizki mana xuddi shu maqsadda `in` operatori mavjud, lekin undan foydalanmang).

       <details><summary>Javob</summary>
    
       ```python
       def azomi(l, x):
           i = 0
           while i < len(l):
               if x == l[i]:
                   return True
                   break
               i = i + 1
           return False


       print(azomi(['Ali', 'Bobur', 'Ibrohim'], 'Alisher'))
       ```
       </details>


52. `bir_xil` nomli funksiya yarating. Argument sifatida 2 ta list olsin. Va ular ustida shunday amal bajarsinki, agar kamida 1 ta element ikkala listda ham bo'lsa funksiya `True` aks holda `False` qaytarsin. Bunda yuqorida `azomi` funksiyasidan foydalansangiz ham bo'ladi. Mn, `bir_xil([1,2,3], [10, 777, 1])` deb ishlatsak `True` qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def bir_xil(list1, list2):
           i = 0
           while i < len(list1):
               if list1[i] in list2:
                   return True
                   break
               i = i + 1
           return False
       print(bir_xil([1,2,3], [10, 777, 1]))
       ```
       </details>


53. `n_takror_harf` nomli funksiya yarating. Argument sifatida butun son `n`, va string `harf` parametrlari bo'lsin. `n_takror_harf(5, 'a')` deb chaqirsak, `aaaaa` deb string qaytarsin. 

       <details><summary>Javob</summary>
    
       ```python
       def n_takror_harf(a, b):
           print(a * b)

       n_takror_harf(5, 'a')
       ```
       </details>


54. `histogram` degan funksiya yarating. U argument sifatida list olsin, va histogramni konsolga chiqarsin. Mn, histogram( [1, 3, 5, 2] ) uchun quyidagini chiqarsin:

    ```python
    *
    ***
    *****
    **
    ```

       <details><summary>Javob</summary>
    
       ```python
       def histogram(l_list):
           i = 0
           while i < len(l_list):
               print('*' * l_list[i])
               i = i + 1

       histogram([1, 3, 5, 2])
       ```
       </details>


55. Yuqorida, `ikki_max` va `uch_max` funksiyalari faqat 2 va 3 ta son uchun ishlaydi. Lekin tasavvur qiling bizda 100-1000 lab sonlar bor. Unda kattasini qanday qidiramiz (topamiz). `max_list` degan funksiya yarating, va u argumentga list olsinda, litsda elementlardan eng kattasini qaytarsin. Mn, `max_list( [1,20, 45, 90, 32, 100] )` desak 100 qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def max_list(l_list):
           print(max(l_list))

       max_list([1,20, 45, 90, 32, 100])
       ```
       </details>


56. `listdan_songa(list_suzlar)` nomli funksiya yarating. Va u har bir sonning uzunligini list qilib qaytarsin. Mn, `list_suzlar = ['salom', 'yaxshi', 'bir']` desak, `[5, 6, 3]` ni qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def listdan_songa(list_suzlar):
           sonli_list = []
           i = 0
           while i < len(list_suzlar):
               sonli_list.append(len(list_suzlar[i]))
               i = i + 1
           return sonli_list
       
       print(listdan_songa( ['salom', 'yaxshi', 'bir']))
       ```
       </details>


57. `eng_uzun_suz` nomli funksiya yarating. Bunda funksiya argumentiga list olsin va eng uzun so'z uzunligini qaytarsin. Mn, `list_suzlar = ['salom', 'yaxshi', 'bir']` desak, `6` ni qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def listdan_songa(list_suzlar):
           sonli_list = []
           i = 0
           while i < len(list_suzlar):
               sonli_list.append(len(list_suzlar[i]))
               i = i + 1
           return max(sonli_list)

       print(listdan_songa( ['salom', 'yaxshi', 'bir']))
       ```
       </details>


58. `filter_uzun_suzlar` nomli funksiya yarating. Ikkita argument qabul qilsin. 1-si bir necha so'zlardan tashkil topgan list. 2-si butun son `n`. Funksiya uzunlig `n`dan katta bo'lgan so'zlar listini qayatarsin. Mn, `list_suzlar = ['salom', 'yaxshi', 'bir']` `filter_uzun_suzlar(list_suzlar, 3)` desak `['salom', 'yaxshi']` ni qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       def filter_uzun_suzlar(l,n):
           filter_list = []
           i = 0
           while i < len(l):
               if len(l[i]) > n:
               filter_list.append(l[i])
               i = i + 1
           return filter_list
       list_suzlar = ['salom', 'yaxshi', 'bir']
 
       print(filter_uzun_suzlar(list_suzlar,3))
       ```
       </details>


59. `panagrammi` nomli funksiya yarating. Argumentga string olsin va agar berilgan string panagram bo'lsa `True`, aks holda `False` qaytarsin. Eslatma: panagram degani berilgan gapda hamma harflar ishtirok etgan bo'ladi. 

       <details><summary>Javob</summary>
    
       ```python
       harflar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
       katta_harflar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
       def panagrammi(suz):
           indeks = 0
           while indeks < len(harflar):
               if (harflar[indeks] in suz or katta_harflar[indeks] in suz) == False:
                   return False
               indeks = indeks + 1
           return True

       javob = panagrammi("abcdefghijklmn opqrsTuvwxyz")
       print(javob)
       ```
       </details>


60. Ekranga quyidagini chiqaring. 
    ```python
    1 ta quy
    2 ta quy
    3 ta quy
    4 ta quy
    5 ta quy
    6 ta quy
    7 ta quy
    ```

       <details><summary>Javob</summary>
    
       ```python
       i = 1
       while i < 8:
           print(i, 'ta quy')
           i = i + 1
       ```
       </details>

61. Quyidagi dictionary ni olingda 
    ```python
    {
        'kitob': 'book',
        'bu': 'this',
        'qimmat': 'expensive'
    }
    ```
    `uz_ingliz` nomli funksiya yarating. Va argumentga `Bu kitob qimmat` ni olsinda o'zbekcha tarjimasini qaytarsin.

       <details><summary>Javob</summary>
    
       ```python

       ```
       </details>


62. `harf_soni` nomli funksiya yarating. Berilgan stringdan harflarni necha martadan ishtirok etganini qaytarsin. dictionarydan foydalaning.  Mn, `harf_soni("aaaabbbc")` ni ishlatsak, `{'a': 4, 'b': 3, 'c': 1}` ni qaytarsin.

       <details><summary>Javob</summary>
    
       ```python
       from collections import Counter
       
       def harf_soni(x):
           print(Counter(x))

       harf_soni("aaaabbbc")
       ```
       </details>


63. Kriptografiyada, Sezr sifri degan oddiy enkriptsiya usuli mavjud. Bunda, berilgan harf boshqa harf bilan almashtiriladi. Boshqa harf o'zidan keyingi 1 yoki ixtiyoriy harfdan keyin kelguvchi harf bilan almashtirilishi mumkin. Mn, `ada` so'zi `beb` sifrlanishi mumkin. Qadimda Sezr ushbu sifrlashni o'zining generallari bilan mahfiy muloqot qilish uchun ishlatgan. Vazifa shundan iboratki, quyidagi dictionary berilgan, bunda har bir harf keying 13 harfdan keyin kelguvchi harf bilan almashtirilishi ko'rsatilayapti. 

    ```python
    key = 
    {
    'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u','i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'
    }
    ```

  2 ta funksiya yarating. Birini `enkoder` deb atang, bunda u quyidagi so'zni sifrlasin: `men ertaga qaytaman`. 2-sini esa `dekoder` deb atang, sifrlagan so'zingizni yana o'z holiga qaytarsin.


   <details><summary>Javob</summary>

   ```python

   ```
   </details>


64. `>, <, >=, <=` belgilarni int va stringlarni taqqoslash uchun ishlating. Nima bo'ldi?


65. Quyidagi arifmetik progressiyani  `while` orqali hosil qiling, 

    ```python
    -2, 1, 4, 7, 10, 13
    ```

       <details><summary>Javob</summary>
    
       ```python
       i = -2
       while i<=13:
           print(i, end=' ')
           i = i + 3
       ```
       </details>


66. Quyifagi arifmetik progressiyani  `for` orqali hosil qiling, 

    ```python
    -2, 1, 4, 7, 10, 13
    ```
    
       <details><summary>Javob</summary>
    
       ```python
       for i in range(-2, 14, 3):
           print(i, end=' ') 
       ```
       </details>


67. Quyidagi arifmetik progressiyani  `range` orqali hosil qiling, 

    ```python
    -2, 1, 4, 7, 10, 13
    ```

       <details><summary>Javob</summary>
    
       ```python
       print(list(range(-2, 14, 3)))
       ```
       </details>


68. Quyidagi kodda nima sintaks xato? Ishlatmay topishga harakat qiling.

    ```python
    # snippet 1:
    def greeting()
        print('hello')
    
    # snippet 2:
    num = 5
    if num = 4:
        print('what is going on?!')
    
    # snippet 3:
    greeting = “hi”
    ```



69.  `son` nomli funksiya yarating. `int`, `float` va `str` turlarni argument sifatida olsin, qolgan turlar argument sifatida berilsa xato bersin. Mn,

	    ```python
	    # int 
	    >>> son(3)
	    3
	    # float 
	    >>> son(3.32)
	    3.32
	    # str 
	    >>> son('12')
	    12

	    # xato tur
	    >>> son(['1', '2.3'])
	    TypeError: not a valid input data type

	    # string intga o'zgartira olinmaydi
	    >>> son('salom')
	    ValueError: could not convert string to int or float
	    ```


70. `harflar = tuple('salom')` berilgan. `harflar[0]` nima qaytaradi. `harflar[0] = S` qilsak nima bo'ladi?

71. Berilgan `tub_sonlar = (2, 3, 5, 7, 11)`. Quyidagi holatlarni tekshiring.

    * nima bo'ladi agar `primes[5]`?
    * nima bo'ladi agar `primes[-6]`?
    * nima bo'ladi agar `primes[:5]`?
    * nima bo'ladi agar `primes[-6:]`?
    

72. Berilgan `nums = (1, 2)`. Quyidagi holatlarni tekshiring. 

    ```python
    a, b, c = nums
    a, *b, c = nums
    *a, *b = nums
    ```

73. Quyidagi funksiya nima qiladi?

    ```python
    def sum_nums(args):
        total = 0
        for n in args:
            total += n
        return total
    ```

74. Berilgan `fruits = {'banana':12, 'papaya':5, 'mango':10, 'apple':100}`. Tekshiring `a, *b, c = fruits`?

75. Berilgan `sonlar = [1, 4, 6, 22, 3, 5, 4, 3, 6, 2, 1, 51, 3, 1]`. Shunday qilingki, faqat sonlar bir martadan ishtirok etsin va ketma-ketlik saqlanib qolsin. Mn, `[1, 4, 6, 22, 3, 5, 2, 51]`.

       <details><summary>Javob</summary>
       
       ```python
       sonlar = [1, 4, 6, 22, 3, 5, 4, 3, 6, 2, 1, 51, 3, 1]
       
       yangi_sonlar = []
       
       i = 0
       while i < len(sonlar):
           if (sonlar[i] in yangi_sonlar) != True:
               yangi_sonlar.append(sonlar[i])
           i = i + 1
       
       print(yangi_sonlar)
       ```
       </details>


76. Quyidagining natijasi nima bo'ladi? `print('concatena'+'tion')`

77. Quyidagi kodni o'qing va nimani konsolga chiqarishini toping. Keyin kodni pycharmda ishlating va o'zingizning natijangiz bilan taqqoslang.

    ```python
    spam_amount = 0
    print(spam_amount)
    
    # Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
    spam_amount = spam_amount + 4
    
    if spam_amount > 0:
        print("But I don't want ANY spam!")
    
    viking_song = "Spam " * spam_amount
    print(viking_song)
    ```

78. Quyidagi kodning oltinchi qatorini kommentlang,

    ```python
    spam_amount = 0
    print(spam_amount)
    
    # Ordering Spam, egg, Spam, Spam, 
    # bacon and Spam (4 more servings of Spam)
    spam_amount = spam_amount + 4
    
    if spam_amount > 0:
        print("But I don't want ANY spam!")
    
    viking_song = "Spam " * spam_amount
    print(viking_song)
  
    ```
    Keyin ishlating, natija nima bo'ldi?
    
    ```shell
    | Operator | Name           | Description                                    |
    |----------|----------------|------------------------------------------------|
    | a + b    | Addition       | Sum of a and b                                 |
    | a - b    | Subtraction    | Difference of a and b                          |
    | a * b    | Multiplication | Product of a and b                             |
    | a / b    | True division  | Quotient of a and b                            |
    | a // b   | Floor division | Quotient of a and b, removing fractional parts |
    | a % b    | Modulus        | Integer remainder after division of a by b     |
    | a ** b   | Exponentiation | a raised to the power of b                     |
    | -a       | Negation       | The negative of a                              |
    ```

79. Quyidagi programma natijasi nima bo'ladi

    ```python
    mystery = print()
    print(mystery)
    ```

80. Quyidagi ikki funksiyalarni natijasini ishlatmay toping. 

    ```python
    def add(a, b):
        """
        Add two numbers and
        return the result 
        """
        result = a + b
        return  result
    
    result = add(2, 3) 
    print(result)
    
    def add_without_return(a, b):
        """
        Add two numbers and
        return nothing
        """
        result = a + b
    
    result = add_without_return(2, 3) 
    print(result) 
    ```

81. Quyidagi amalning natijasi nima bo'ladi?

    ```python
    True or True and False
    ```


    | Operation | Description               |   | Operation | Description                  |
    |-----------|---------------------------|---|-----------|------------------------------|
    | a == b    | a equal to b              |   | a != b    | a not equal to b             |
    | a < b     | a less than b             |   | a > b     | a greater than b             |
    | a <= b    | a less than or equal to b |   | a >= b    | a greater than or equal to b |


82 Quyidagining natijasi nima bo'ladi? 

 ```python
 print(3.0 == 3)
 print('3' == 3)
```
83. Quyidagilarni natijasini ayting, Va natijani pycharmda ishlatib solishtiring.

    ```python
    print(bool("")) 
    print(bool(0))
    print(bool("abc"))
    print(bool(1))
    print(bool("A"))
    print(bool(6.2))
    ```

84. Quyidagi kodni shunday o'zgartiringki, kodlar qatori kamaysin. Lekin, natija bir xil bo'lsin

    ```python
    def is_negative(number):
        if number < 0:
            return True
        else:
            return False
    ```

85. Quyidagi programmani to'ldiring. Yani `pass` o'rniga shunday o'qzgaritish qilingki funksiya `L` listning 2-chi elementini qaytarsin.

    ```python
    def ikkinchini_tanla(L):
        
        pass
    ```      

       <details><summary>Javob</summary>
       
       ```python
       def ikkinchini_tanla(L):
           ikkinchi_element = L.pop(1)
           return ikkinchi_element

       print(ikkinchini_tanla(["olma", "nok", "gilos", "banan"]))
       ```
       </details>


86. List berilgan `L = ["Mario", "Bowser", "Luigi"]`. Shunday programma tuzingki, `["Luigi", "Bowser", "Mario"]` bo'lsin. Yani, birinchi va oxirgi elementlar almashsin.

       <details><summary>Javob</summary>
       
       ```python
       L = ["Mario", "Bowser", "Luigi"]
       
       birinchi_element = L.pop(0)
       ohirgi_element = L.pop()
       # L listga birinchi elementni ohirga o'tkazib oldik.
       L.append(birinchi_element)
       # L listning ohirgi elementini yangi listning birinchi elementiga qushib olamiz.
       yangi_list = []
       yangi_list.append(ohirgi_element)
       # Yangi listga L listdagi elementlarni qushib ketaveramiz.
       i = 0
       while i < len(L):
           yangi_list.append(L[i])
           i = i + 1

       print(yangi_list)
       ```
       </details>


87. Quyidagi listlarning uzunligini toping.

    ```python
    a = [1, 2, 3]
    b = [1, [2, 3]]
    c = []
    d = [1, 2, 3][1:]
    ```

88. Quyidagi kodda nima bo'layapti?
    ```pthon
    [1, 2, 3, 4] > 2
    ```

       <details><summary>Javob</summary>
       
       ```python
       TypeError: '>' not supported between instances of 'list' and 'int'
       ```
       </details>


89. Quyidagi dictionaryning birinchi elementini oling.

    ```python
    alifbedan_songa = {'a', 1, 'b', 2}
    ```

90. Quyidagi dictionaryni kengaytiring. Yani, `c` kalit yaratib unga `3` qiymatini yuklab uni dictionaryga qo'shing.

    ```python
    alifbedan_songa = {'a', 1, 'b', 2}
    ```

91. Quyidagini konsolga for loopdan foydalanib ekranga chiqaring.

    ```python
    sonlar = {'bir':1, 'ikki':2, 'uch':3}
    ```

       <details><summary>Javob</summary>
       
       ```python
       sonlar = {'bir':1, 'ikki':2, 'uch':3}

       for key, value in sonlar.items():
           print(key, value)
       ```
       </details>


92. Quyidagi stringlarning uzunligini toping. Keyin kodini pycharmda yozingda natijangizni solishtiring.

    ```python
    a = ""
    b = ''
    c = "\n"
    d = 'it\'s ok'
    e = """ana"""
    ```

93. `s = 'Mergan'` string berilgan. `s[0] = 'T'` qilsak nima bo'ladi?

94. Quyidagining natijasi nima bo'ladi? `print(2**4)`

95. Konsolga nima chiqadi? 

    ```python
    exampleVar = 55
    print(exampleVar)
    ```
    
96. Quyidagini ishlatsak konsolga nima chiqadi:
    ```python
    condition = 1
    
    while condition < 10:
        print(condition)
        condition += 1
    ```

97. Quyidagini ishlatsak konsolga nima chiqadi:

    ```python
    condition = '4'
    
    while condition > 6:
        print 'test'
    ```    

98. Quyidagini ishlatsak konsolga nima chiqadi:

    ```python
    while True:
        print('doing stuff!!')
    ```

99. Quyidagini ishlatsak konsolga nima chiqadi:

    ```python
    exampleList = [1, 5, 6, 6, 2, 1, 5, 2, 1, 4]
    for x in exampleList:
        print(x)
    ```

100. Quyidagini ishlatsak konsolga nima chiqadi:

	    ```python
	    for x in range(1, 11, 3):
		print(x)
	    ```

       <details><summary>Javob</summary>
       
       ```python
       IndentationError: expected an indented block
       ```
       </details>


101. Quyidagini ishlatsak konsolga nima chiqadi:

     ```python
     x = 5
     y = 10
     z = 22
    
     if x > y:
         print('x is greater than y')
     elif x == z:
         print('x is less than z')
     elif 5 == 2:
         print('5 is greater than 2')
     else:
         print('if and elif(s) never ran')
     ```

102. Quyidagini ishlatsak ekranga nima chiqadi?

	    ```python
	    x = 5
	    y = 8

	    if x < y:
		print('x is greater than y')
	    if x > 55:
		print('x is greater than 55')
	    else:
		print('x is not greater than y or 55')
	    ```

103. Ushbu funksiyani ishlating.
    
		```python

		def example():
		print('kodlar')
		x = 13 + 19
		print(x)

		```

104. Quyidagini ishlatmay natijani ayting. Keyin ishlating va solishtiring?

	    ```python
	    def simple_addition(s1, s2):
		javob = s1 + s2
		print('s1: ', s1)
		print(javob)

	    simple_addition(5,3)
	    ```

105. Aytaylik, `name = "Ahmad Dilshodov"`, `name[1]` nima qaytaradi?  name[-2] chi? name[1:-1] chi?

106. Qanday qilib ism uzunligni bilamiz?

107. Quyidagini natjasi nima bo'ladi `f"{2+2}+{10%3}"`?

108. Berilgan `name = "Ahmad Dilshodov"`, `name.title()` nima qaytaradi?

109. Berilgan `name = "Ahmad Dilshodov"`, `name.strip()` nima qiladi?

110. Berilgan `name = "Ahmad Dilshodov"`, `name.find("Smith")` nima qaytaradi?

111. Berilgan `name = "Ahmad Dilshodov"`, `name.replace("j", "k")` `name` qiymati o'zgardimi?

112. Berilgan `name = "Ahmad Dilshodov"`, qanday qilib `"Ahmad"` stringi `name` o'zgaruvchisida bor yo'qligini qanday tushuntiramiz?

       <details><summary>Javob</summary>
       
       ```python
       name = "Ahmad Dilshodov"
       
       print('Ahmad' in name)
       ```
       </details>


113. Quyidagilarning farqi nima `10 / 3` va `10 // 3`?

114. `10 ** 6` natijasi qanday?

115. Aytaylik `x = 2`, `x += 2`ning natijasi nima?

116. `float(1)` - natijasi nima?

117. `bool("False")` - natijasi nima?

118. `10 == "10"`

119. "sen" > "men" natijasi nima?

120. `not(True or False)` natijasi nima?

121. Qachon quyidagi ifoda `"18 <= age < 65"` `True` qaytaradi?

122. `range(1, 10, 2)` nima qaytaradi?

123. Parameter va argument farqini ayting.

124. Pythonda hamma funksiyalar nima qaytaradi?

125. `fizz_buzz` nomli funksiya yarating. Bitta parameterdan tashkil topsin. Agar argument `3` ga bo'linadigan bo'lsa, `"Fizz"` deb qaytarsin. Agar `5` ga bo'linsa `"Buzz"` ni qaytarsin. Agar ham `3` ham `5` ga bo'linadigan bo'lsa, `"FizzBuzz"` qaytarsin. Hech qanday shart bajarilmasa, argument qiymatining o'zini qaytarsin. 

       <details><summary>Javob</summary>
       
       ```python
       def fizz_buzz(son):
           if son % 3 == 0 and son % 5 == 0:
               return "FizzBuzz"
           elif son % 3 == 0:
               return "Fizz"
           elif son % 5 == 0:
               return "Buzz"
           else:
               return son
    
       print(fizz_buzz(55))
       ```
       </details>

126. `tezlik` nomli funksiya yarating va u bitta parameter olsin tezlikni bildirish uchun. Agar berilgan tezlik `70` dan kichik bo'lsa `"OK."` deb qaytarsin. Agar tezlik `70` dan katta bo'lsa `"Ogohlantirish."` ni qaytarsin. Agar `80` dan katta bo'lsa, `"Litzensiyadan mahrum qilinsin."`

       <details><summary>Javob</summary>
       
       ```python
       def tezlik(v):
           if v <= 70:
               return 'OK.'
           elif v > 70 and v < 80:
               return 'Ogohlantirish.'
           else:
               return 'Litzensiyadan mahrum qilinsin.'
       print(tezlik(82))
       ```
       </details>


127. `sonlar` nomli funksiya yarating. Va `chegara` degan parameter olsin. Shunday qilsinki, funskiya 0 dan `chegara`gacha bo'lgan sonlarni qaytarsin va ularining toq yoki juftligini ham qaytarsin. Masalan `chegara` qiymati `3` bo'lsa, quyidagicha bo'lsin:

		```python
		0 Juft
		1 Toq
		2 Juft
		3 Toq
		```

       <details><summary>Javob</summary>
       
       ```python
       def sonlar(chegara):
           i = 0
           while i <= chegara:
               if i % 2 == 0:
                   print(i, "Juft")
               else:
                   print(i, "Toq")
               i = i + 1

       sonlar(3)
       ```
       </details>


128. `sonlar` nomli funksiya yarating. Va `chegara` degan parameter olsin. Shunday qilsinki, funskiya 0 dan `chegara`gacha bo'lgan sonlarning faqat 3 va 5 ga bo'linadiganlarini qaytarsin. Va ularning yig'indisini ham qaytarsin. Mn, `chegara=20` it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

       <details><summary>Javob</summary>
       
       ```python
       def sonlar(chegara):
           i = 1
           s = 0
           while i <= chegara:
               if i % 3 == 0 or i % 5 == 0:
               s = s + i
               i = i + 1
           return s

       print(sonlar(20))
       ```
       </details>


129. `yulduzlar` nomli funksiya yarating. Va u `qator` nomili parameter olsin. Agar `qator`ga 6 berilsa. Quyidagini chiqarsin:
     ```python
     * 
     **
     ***
     ****
     *****
     ****** 
     ```

       <details><summary>Javob</summary>
       
       ```python
       def yulduzlar(qator):
       i = 1
       while i < qator+1:
           print('*' * i)
           i = i + 1

       yulduzlar(6)
       ```
       </details>



130. `yulduzkam` nomli funksiya yarating. Va u `qator` nomili parameter olsin. Agar `qator`ga 6 berilsa. Quyidagini chiqarsin:
        ```python
        ******
        *****
        ****
        ***
        **
        *
        ```
     
       <details><summary>Javob</summary>
       
       ```python
       def yulduzkam
     (qator):
           while qator > 0:
               print("*" * qator)
               qator = qator - 1

       yulduzcha(6)
       ```
       </details>


131. `yulduzcha` nomli funksiya yarating. Va u `qator` nomili parameter olsin. Agar `qator`ga 6 berilsa. Quyidagini chiqarsin:
        ```python
        ******
        ******
        ******
        ******
        ******
        ******
        ```
     
       <details><summary>Javob</summary>
       
       ```python
       def yulduzcha(qator):
       i = 0
       while i < qator:
           print("******")
           i = i + 1
       
       yulduzcha(6)
       ```
       </details>


132. Create a function that takes two numbers as arguments and return their sum.
        ```python
        Examples
        addition(3, 2) ➞ 5
        
        addition(-3, -6) ➞ -9
        
        addition(7, 3) ➞ 10
        ```
133. Create a function that takes a number as an argument, increments the number by +1 and returns the result.
        ```python
        Examples
        addition(0) ➞ 1 
        addition(9) ➞ 10
        addition(-3) ➞ -2
        ```
134. Quyidagi kodni ishlating. Agar ishlamasa to'g'irlang.
        ```python
        def cubes(a):
            retunr a ** 3
        ```























<!-- **SHU YERDAMAN**

133. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


47. Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

48. With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


49. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

50. Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24 


51. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world


52. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world


53. Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3

54. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9

55. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106


56. A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1


57. Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

58. Write a method which can calculate square value of number


59. Define a function which can compute the sum of two numbers.





60. Define a function that can convert a integer into a string and print it in console.





61. Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.





62. Define a function that can accept two strings as input and concatenate them and then print it in console.





63. Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.



64. Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.





65. Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.




66. Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).





67. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.




68. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.




69. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.




70. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).


71. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.


72. Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).



73. Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".


74. Write a function to compute 5/0 and use try/except to catch the exceptions.


75. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

john

76. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

google

77. Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example: If the following words is given as input to the program:

2 cats and 3 dogs.
Then, the output of the program should be:

['2', '3']


78. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5
Then, the output of the program should be:

3.55


79. Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example: If the following n is given as input to the program:

35 + 3
Then, the output of the program should be:

38

80. Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

81. By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].


82. Please write a program which count and print the numbers of each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

83. Please write a program which accepts a string from console and print it in reverse order.

Example: If the following string is given as input to the program:*

rise to vote sir
Then, the output of the program should be:

ris etov ot esir


84. Please write a program which accepts a string from console and print the characters that have even indexes.

Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:

Helloworld


85. Write a Python program that accepts a string and calculate the number of digits and letters.

Input

Hello321Bye360
Output

Digit - 6
Letter - 8




116. Create a function that takes a string and returns it as an integer.
string_int("6") ➞ 6

string_int("1000") ➞ 1000

string_int("12") ➞ 12


117. Write a function that takes the base and height of a triangle and return its area.

tri_area(3, 2) ➞ 3

tri_area(7, 4) ➞ 14

tri_area(10, 10) ➞ 50

S = (base * height) / 2


118. Create a function that takes length and width and finds the perimeter of a rectangle.

find_perimeter(6, 7) ➞ 26

find_perimeter(20, 10) ➞ 60

find_perimeter(2, 9) ➞ 22

119. Create a function that takes a boolean variable flag and returns it as a string.
bool_to_string(True) ➞ "True"

bool_to_string(False) ➞ "False"

120. Quyidagi kodni to'g'rilang,

```
def squaed(b):
	return a * a
```

Keyin ishlatganingizda 
squared(5) ➞ 25
squared(9) ➞ 81
squared(100) ➞ 10000


121. Create a function that takes a list containing only numbers and return the first element.

get_first_value([1, 2, 3]) ➞ 1

get_first_value([80, 5, 100]) ➞ 80

get_first_value([-500, 0, 50]) ➞ -500

122. Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

wins get 3 points
draws get 1 point
losses get 0 points

football_points(3, 4, 2) ➞ 13

football_points(5, 0, 2) ➞ 15

football_points(0, 0, 1) ➞ 0

123. In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.

animals(2, 3, 5) ➞ 36

animals(1, 2, 3) ➞ 22

animals(5, 2, 8) ➞ 50


124. 
def name_string(name):
	  b == "Edabit"
	  result == name + b
	  return result

 A student learning Python was trying to make a function. His code should concatenate a passed string name with string "Edabit" and store it in a variable called result. He needs your help to fix this code.

Examples
name_string("Mubashir") ➞ "MubashirEdabit"

name_string("Matt") ➞ "MattEdabit"

name_string("python") ➞ "pythonEdabit"


125. Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.

Examples
convert(1, 3) ➞ 3780

convert(2, 0) ➞ 7200

convert(0, 0) ➞ 0

126. Write two functions:

to_int() : A function to convert a string to an integer.
to_str() : A function to convert an integer to a string.

to_int("77") ➞ 77

to_int("532") ➞ 532

to_str(77) ➞ "77"

to_str(532) ➞ "532"

127. Write a function that returns the string "something" joined with a space " " and the given argument a.

Examples
give_me_something("is better than nothing") ➞ "something is better than nothing"

give_me_something("Bob Jane") ➞ "something Bob Jane"

give_me_something("something") ➞ "something something"

128. Create a function that returns True when num1 is equal to num2; otherwise return False.

is_same_num(4, 8) ➞ False

is_same_num(2, 2) ➞  True

is_same_num(2, "2") ➞ False

129. Create a function that takes a number as its only argument and returns True if it's less than or equal to zero, otherwise return False.
less_than_or_equal_to_zero(5) ➞ False

less_than_or_equal_to_zero(0) ➞ True

less_than_or_equal_to_zero(-2) ➞ True

130. Create a function that takes a list of numbers. Return the largest number in the list.

findLargestNum([4, 5, 1, 3]) ➞ 5

findLargestNum([300, 200, 600, 150]) ➞ 600

findLargestNum([1000, 1001, 857, 1]) ➞ 1001

131. Create a function that takes a list of numbers and returns the smallest number in the list.

find_smallest_num([34, 15, 88, 2]) ➞ 2

find_smallest_num([34, -345, -1, 100]) ➞ -345

find_smallest_num([-76, 1.345, 1, 0]) ➞ -76

find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) ➞ -0.9999

find_smallest_num([7, 7, 7]) ➞ 7

132. def is_seven(x):
	return False if x=7 elif True

Fix the code in the Code tab so the function returns true if and only if x is equal to 7. Try to debug code and pass all the tests.

is_seven(4) ➞ False

is_seven(9) ➞ False

is_seven(7) ➞ True

133. Create a function that takes a list and returns the difference between the biggest and smallest numbers.


difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# Smallest number is -50, biggest is 32.

difference_max_min([44, 32, 86, 19]) ➞ 67
# Smallest number is 19, biggest is 86.

134. Create a function to concatenate two integer lists.

concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]

concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2]

concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]

135. Given a list of integers, return the difference between the largest and smallest integers in the list.

difference([10, 15, 20, 2, 10, 6]) ➞ 18
# 20 - 2 = 18

difference([-3, 4, -9, -1, -2, 15]) ➞ 24
# 15 - (-9) = 24

difference([4, 17, 12, 2, 10, 2]) ➞ 15

136. Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.
less_than_100(22, 15) ➞ True
# 22 + 15 = 37

less_than_100(83, 34) ➞ False
# 83 + 34 = 117

less_than_100(3, 77) ➞ true

137. Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.

Examples
get_last_item([1, 2, 3]) ➞ 3

get_last_item(["cat", "dog", "duck"]) ➞ "duck"

get_last_item([True, False, True]) ➞ True

get_last_item([7, "String", False]) ➞ False

138. Create a function that takes a name and returns a greeting in the form of a string.

hello_name("Gerald") ➞ "Hello Gerald!"

hello_name("Tiffany") ➞ "Hello Tiffany!"

hello_name("Ed") ➞ "Hello Ed!"

139. Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.

divisible_by_five(5) ➞ True

divisible_by_five(-55) ➞ True

divisible_by_five(37) ➞ False

140. Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.

divisible_by_five(5) ➞ True

divisible_by_five(-55) ➞ True

divisible_by_five(37) ➞ False

141. Create a function that takes a list and returns the sum of all numbers in the list.


get_sum_of_elements([2, 7, 4]) ➞ 13

get_sum_of_elements([45, 3, 0]) ➞ 48

get_sum_of_elements([-2, 84, 23]) ➞ 105

142. Create a function that takes an integer and return True if it's divisible by 100, otherwise return False.

divisible(1) ➞ False

divisible(1000) ➞ True

divisible(100) ➞ True


143. Write a function that returns True if k^k == n for input (n, k) and return False otherwise.

k_to_k(4, 2) ➞ True

k_to_k(387420489, 9) ➞ True
# 9^9 == 387420489

k_to_k(3124, 5) ➞ False

k_to_k(17, 3) ➞ False

144. Quyidagini kodni to'g'irlang
def max_num(n1, n2):
	if n1 > n2:
		return n2
	elif:
		return n1

mana bular to'g'ri ishlasin
max_num(3, 7) ➞ 7

max_num(-1, 0) ➞ 0

max_num(1000, 400) ➞ 1000


145. Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

comp("AB", "CD") ➞ True

comp("ABC", "DE") ➞ False

comp("hello", "edabit") ➞ False

146. Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.

divides_evenly(98, 7) ➞ True
# 98/7 = 14

divides_evenly(85, 4) ➞ False
# 85/4 = 21.25

147. Create a function that takes a string; we'll say that the front is the first three characters of the string. If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies of the front.
front3("Python") ➞ "PytPytPyt"

front3("Cucumber") ➞ "CucCucCuc"

front3("bioshock") ➞ "biobiobio"

148. Create a function that returns True if a string is empty and False otherwise.

is_empty("") ➞ True

is_empty(" ") ➞ False

is_empty("a") ➞ False

149. Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.
makes10(9, 10) ➞ True

makes10(9, 9) ➞ False

makes10(1, 9) ➞ True

150. Create a recursive function that takes two parameters and repeats the string n number of times. The first parameter txt is the string to be repeated and the second parameter is the number of times the string is to be repeated.

repetition("ab", 3) ➞ "ababab"

repetition("kiwi", 1) ➞ "kiwi"

repetition("cherry", 2) ➞ "cherrycherry"

151. Create a function that takes a number n and returns the nth even number.

nth_even(1) ➞ 0
# 0 is first even number

nth_even(2) ➞ 2
# 2 is second even number

nth_even(100) ➞ 198

152. Xatoni to'grilang

def sum_lst(lst):
	total
	for i in range(0,lst):
		total += lst[i]
  return total

  Keyin, suhbular ishlasin
  sum_lst([1, 2, 3, 4, 5]) ➞ 15

sum_lst([-1, 0, 1]) ➞ 0

sum_lst([0, 4, 8, 12]) ➞ 24

152. Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.

ist_less_than_100([5, 57]) ➞ True

list_less_than_100([77, 30]) ➞ False

list_less_than_100([0]) ➞ True

153. Given two strings, first_name and last_name, return a single string in the format "last, first".

concat_name("First", "Last") ➞ "Last, First"

concat_name("John", "Doe") ➞ "Doe, John"

concat_name("Mary", "Jane") ➞ "Jane, Mary"

154. Creates a function that takes a string and returns the concatenated first and last character.

first_last("ganesh") ➞ "gh"

first_last("kali") ➞ "ki"

first_last("shiva") ➞ "sa"

first_last("vishnu") ➞ "vu"

first_last("durga") ➞ "da"

155. Given a string, return True if its length is even or False if the length is odd.

odd_or_even("apples") ➞ True
# The word "apples" has 6 characters.
# 6 is an even number, so the program outputs True.

odd_or_even("pears") ➞ False
# "pears" has 5 letters, and 5 is odd.
# Therefore the program outputs False.

odd_or_even("cherry") ➞ True


156. Given two arguments, return a list which contains these two arguments.

make_pair(1, 2) ➞ [1, 2]

make_pair(51, 21) ➞ [51, 21]

make_pair(512124, 215) ➞ [512124, 215]

157. Create a function that returns True if two lists contain identical values, and False otherwise.

To solve this question, your friend writes the following code:

def check_equals(lst1, lst2):
    if lst1 is lst2:
        return True
    else:
        return False
But testing the code, you see that something is not quite right. Running the code yields the following results:

check_equals([1, 2], [1, 3]) ➞ False
# Good so far...

check_equals([1, 2], [1, 2]) ➞ False
# Yikes! What happened?
Rewrite your friend's code so that it correctly checks if two lists are equal. To be equal, the lists must have the same elements in the same order. The tests below should pass:

Examples
check_equals([1, 2], [1, 3]) ➞ False

check_equals([1, 2], [1, 2]) ➞ True

check_equals([4, 5, 6], [4, 5, 6]) ➞ True

check_equals([4, 7, 6], [4, 5, 6]) ➞ False


158. def greeting(name):
	return "Hello, " + name + "!"
	if name == "Mubashir":
		return "Hello, my Love!"
Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir, and would like to greet him slightly differently. She added a special case in her function, but she made a mistake.

Can you help her?

Examples
greeting("Matt") ➞ "Hello, Matt!"

greeting("Helen") ➞ "Hello, Helen!"

greeting("Mubashir") ➞ "Hello, my Love!"


159. Given a list of integers, determine whether the sum of its elements is even or odd.

The return value should be a string ("odd" or "even").

If the input list is empty, consider it as a list with a zero ([0]).

Examples
even_or_odd([0]) ➞ "even"

even_or_odd([1]) ➞ "odd"

even_or_odd([]) ➞ "even"

even_or_odd([0, 1, 5]) ➞ "even"

160. Create a function that takes a number as an argument and returns negative of that number. Return negative numbers without any change.

return_negative(4) ➞ -4

return_negative(15) ➞ -15

return_negative(-4) ➞ -4

return_negative(0) ➞ 0

161. XAtoni to'g'irlang. def print_list(n):
	result=[]
	i=1
	while i<=n:
		result+=[i]
	return result

    Mubashir created an infinite loop! Help him by fixing the code in the code tab to pass this challenge. Look at the examples below to get an idea of what the function should do.

Examples
print_list(1) ➞ [1]

print_list(3) ➞ [1, 2, 3]

print_list(6) ➞ [1, 2, 3, 4, 5, 6]


162. Éowyn has written the function is_odd() to check if a given number is odd or not. Unfortunately, the function does not return the correct result for all the inputs. Help her fix the error.

def is_odd(num):
  return num % 1 == 1 or 2
Examples
is_odd(-5) ➞ True

is_odd(25) ➞ True

is_odd(0) ➞ False

163. Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.

Examples
num_to_dashes(1) ➞ "-"

num_to_dashes(5) ➞ "-----"

num_to_dashes(3) ➞ "---"

164. Write a function to check if a list contains a particular number.

Examples
check([1, 2, 3, 4, 5], 3) ➞ True

check([1, 1, 2, 1, 1], 3) ➞ False

check([5, 5, 5, 6], 5) ➞ True

check([], 5) ➞ False

165. Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.

isEvenOrOdd(3) ➞ "odd"

isEvenOrOdd(146) ➞ "even"

isEvenOrOdd(19) ➞ "odd"

166. Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".

Examples
is_plural("changes") ➞ True

is_plural("change") ➞ False

is_plural("dudes") ➞ True

is_plural("magic") ➞ False

167. Create a function that takes a string (a random name). If the last character of the name is an "n", return True, otherwise return False.

is_last_character_n("Aiden") ➞ True

is_last_character_n("Piet") ➞ False

is_last_character_n("Bert") ➞ False

is_last_character_n("Dean") ➞ True

168. Create a function that takes a word and returns the new word without including the first character.

Examples
new_word("apple") ➞ "pple"

new_word("cherry") ➞ "herry"

new_word("plum") ➞ "lum"

169. Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") as input and calculates the area of that shape.

Examples
area_shape(2, 3, "triangle") ➞ 3

area_shape(8, 6, "parallelogram") ➞ 48

area_shape(2.9, 1.3, "parallelogram") ➞ 3.77
Notes
Area of a triangle is 0.5 * b * h
Area of a parallelogram is b * h

170. def check_equals(lst1, lst2):
	if [lst1[::] === lst2[::]]:
		print(true)
	else:
		print(false)

    Programmer Pete is trying to create a function that returns True if two lists share the same length and have identical numerical values at every index, otherwise, it will return False.

However, the solution his function gives is in an unexpected format. Can you fix Pete's function so that it behaves as seen in the examples below?

Examples
check_equals([1, 2], [1, 3]) ➞ False

check_equals([1, 2], [1, 2]) ➞ True

check_equals([4, 5, 6], [4, 5, 6]) ➞ True

check_equals([4, 7, 6], [4, 5, 6]) ➞ False

check_equals([1, 12], [11, 2]) ➞ False

171. Create a function that returns True if the combined weight of a car car and the weight of the passengers p in the car is less than the maximum weight max_weight the car is allowed to carry. Otherwise, return False. The weight of the car and the weight of the passengers are given in pounds. The maximum weight is given in kilograms.

Examples
weight_allowed(3000, [150, 201, 75, 88, 195], 1700) ➞ True

weight_allowed(3200, [220, 101, 115, 228, 15], 1700) ➞ False

weight_allowed(2900, [225, 171, 300, 274, 191], 1850) ➞ True

172. Create a function that takes a string txt and a number n and returns the repeated string n number of times.

If given argument txt is not a string, return Not A String !!

Examples
repeat_string("Mubashir", 2) ➞ "MubashirMubashir"

repeat_string("Matt", 3) ➞ "MattMattMatt"

repeat_string(1990, 7) ➞ "Not A String !!"

173. Write a function that takes an integer and returns a string with the given number of "a"s in Edabit.

Examples
how_many_times(5) ➞ "Edaaaaabit"

how_many_times(0) ➞ "Edbit"

how_many_times(12) ➞ "Edaaaaaaaaaaaabit"

174. Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).

Examples
min_max([1, 2, 3, 4, 5]) ➞ [1, 5]

min_max([2334454, 5]) ➞ [5, 2334454]

min_max([1]) ➞ [1, 1]

175. Create a function that returns True if a string contains any spaces.

Examples
has_spaces("hello") ➞ False

has_spaces("hello, world") ➞ True

has_spaces(" ") ➞ True

has_spaces("") ➞ False

has_spaces(",./!@#") ➞ False

176. Write a function that returns the sum of elements greater than 5, in the given list.

Examples
sum_five([1, 5, 20, 30, 4, 9, 18]) ➞ 77

sum_five([1, 2, 3, 4]) ➞ 0

sum_five([10, 12, 28, 47, 55, 100]) ➞ 252

177. Create a function that counts how many D's are in a sentence.

Examples
count_d("My friend Dylan got distracted in school.") ➞ 4

count_d("Debris was scattered all over the yard.") ➞ 3

count_d("The rodents hibernated in their den.") ➞ 3

178. Create a function that takes as a parameter a list of "stringified" numbers and returns a list of numbers.

Example:

["1", "3", "3.6"] ➞ [1, 3, 3.6]
Examples
to_number_list(["9.4", "4.2"]) ➞ [9.4, 4.2]

to_number_list(["99", "20"]) ➞ [99, 20]

to_number_list(["9.5", "8.8"]) ➞ [9.5, 8.8]

179. Some basic Python operators are +, -, *, /, and %. In this challenge you will be given three parameters, num1, num2, and an operator. Use the operator on number 1 and 2.

Examples
operate(1, 2, "+") ➞ 3
# 1 + 2 = 3

operate(7, 10, "-") ➞ -3
# 7 - 10 = -3

operate(20, 10, "%") ➞ 0
# 20 % 10 = 0

180. Create a function that takes a list of values and returns the first and last values in a new list.

Examples
first_last([5, 10, 15, 20, 25]) ➞ [5, 25]

first_last(["edabit", 13, None, False, True]) ➞ ["edabit", True]

first_last([None, 4, "6", "hello", None]) ➞ [None, None]


181. Create a function that returns a list of all the integers between two given numbers start and end.

Examples
range_of_num(2, 4) ➞ [3]

range_of_num(5, 9) ➞ [6, 7, 8]

range_of_num(2, 11) ➞ [3, 4, 5, 6, 7, 8, 9, 10]





182. Create a function which validates whether a bridge is safe to walk on (i.e. has no gaps in it to fall through).

Examples
is_safe_bridge("####") ➞ True

is_safe_bridge("## ####") ➞ False

is_safe_bridge("#") ➞ True


183. The abs() function returns the absolute value of a number. This means it returns a number's positive value. You can think of it as the distance away from zero.

Create a function that recreates this functionality.

Examples
absolute(-5) ➞ 5Create a function that will put the first argument, a character, between every word in the second argument, a string.

Examples
add("R", "python is fun") ➞ "pythonRisRfun"

add("#", "hello world!") ➞ "hello#world!"

add("#", " ") ➞ "#"

184. Write a function that returns 0 if the input is 1, and returns 1 if the input is 0.

flip(1) ➞ 0

flip(0) ➞ 1

185. Given a list, rotates the values clockwise by one (the last value is sent to the first position).

Check the examples for a better understanding.

Examples
rotate_by_one([1, 2, 3, 4, 5]) ➞ [5, 1, 2, 3, 4]

rotate_by_one([6, 5, 8, 9, 7]) ➞ [7, 6, 5, 8, 9]

rotate_by_one([20, 15, 26, 8, 4]) ➞ [4, 20, 15, 26, 8]

186. In this challenge, you have to implement a function that returns the given distance kilometers converted into miles. You have to round the result up to the fifth decimal digit.

Examples
km_to_miles(2) ➞ 1.24274

km_to_miles(6) ➞ 3.72823

km_to_miles(8) ➞ 4.97097
Notes
1 kilometer = 0.621371 miles.

187. Create a function to return the amount of potatoes there are in a string.

Examples
potatoes("potato") ➞ 1

potatoes("potatopotato") ➞ 2

potatoes("potatoapple") ➞ 1

188. Write a function that returns True if a dictionary contains the specified key, and False otherwise.

Examples
has_key({ "a": 44, "b": 45, "c": 46 }, "d") ➞ False

has_key({ "craves": True, "midnight": True, "snack": True }, "morning") ➞ False

has_key({ "pot": 1, "tot": 2, "not": 3 }, "not") ➞ True

189. Create a function that takes a list. This list will contain numbers represented as strings.

Your function should split this list into two new lists. The first list should contain only even numbers. The second only odd. Then, wrap these two lists in one main list and return it.

Return an empty list if there are no even numbers, or odd.

Examples
clean_up_list(["8"]) ➞ [[8], []]

clean_up_list(["11"]) ➞ [[], [11]]

clean_up_list(["7", "4", "8"]) ➞ [[4, 8], [7]]

clean_up_list(["9", "4", "5", "8"]) ➞ [[4, 8], [9, 5]]

190. def remove_numbers(string):
    return "".join(i for i in string if int(i))

Mubashir wants to remove numbers from a given string!

Help him by fixing the code in the code tab to pass this challenge. Look at the examples below to get an idea of what the function should do.

Examples
remove_numbers("mubashir1") ➞ "mubashir"

remove_numbers("12ma23tt") ➞ "matt"

remove_numbers("e1d2a3b4i5t6") ➞ "edabit"

absolute(-3.14) ➞ 3.14

absolute(250) ➞ 250

191. Given an index using INTEGER division and a list, return the value of the list with the given index.

Examples
value_at([1, 2, 3, 4, 5, 6], 10 // 2) ➞ 6

value_at([1, 2, 3, 4, 5, 6], 8.0 // 2) ➞ 5

value_at([1, 2, 3, 4], 6.535355314 // 2) ➞ 4

192. Check if a string txt is a title text or not. A title text is one which has all the words in the text start with an upper case letter.

Examples
check_title("A Mind Boggling Achievement") ➞ True

check_title("A Simple Python Program!") ➞ True

check_title("Water is transparent") ➞ False

193. Create a function that returns the last value of the last item in a list or string.

Examples
last_ind([0, 4, 19, 34, 50, -9, 2]) ➞ 2

last_ind("The quick brown fox jumped over the lazy dog") ➞ "g"

last_ind([]) ➞ None

194. Kinetic energy can be calculated with the following formula:

KE = 1/2mv²

m is mass in kg
v is velocity in m/s
KE is kinetic energy in J
Return the Kinetic Energy in Joules, given the mass and velocity. For the purposes of this challenge, round answers to the nearest integer.

Examples
calc_kinetic_energy(60, 3) ➞ 270

calc_kinetic_energy(45, 10) ➞ 2250

calc_kinetic_energy(63.5, 7.35) ➞ 1715

195. Create a function that takes a number as an argument and returns the square root of that number cubed.

Examples
cube_squareroot(81) ➞ 729

cube_squareroot(1646089) ➞ 2111932187

cube_squareroot(695556) ➞ 580093704

196. Given a set containing one element, return the element.

Examples
element_from_set({"edabit"}) ➞ "edabit"

element_from_set({True}) ➞ True

element_from_set({11037}) ➞ 11037

197. Create a function that takes a list of numbers lst and returns an inverted list.

Examples
invert_list([1, 2, 3, 4, 5]) ➞ [-1, -2, -3, -4, -5]

invert_list([1, -2, 3, -4, 5]) ➞ [-1, 2, -3, 4, -5]

invert_list([]) ➞ []

198. Write a function that returns True if a dictionary is empty, and False otherwise.

Examples
is_empty({}) ➞ True

is_empty({ "a": 1 }) ➞ False

199. Given a letter and a list of words, return whether the letter does not appear in any of the words.

Examples
forbidden_letter("r", ["rock", "paper", "scissors"]) ➞ False

forbidden_letter("a", ["spoon", "fork", "knife"]) ➞ True

forbidden_letter("m", []) ➞ True

200. Write a function that validates whether two strings are identical. Make it case insensitive.

Examples
match("hello", "hELLo") ➞ True

match("motive", "emotive") ➞ False

match("venom", "VENOM") ➞ True

match("mask", "mAskinG") ➞ False

201. Create a function that takes a list of integers and strings. Convert integers to strings and return the new list.

Examples
parse_list([1, 2, "a", "b"]) ➞ ["1", "2", "a", "b"]

parse_list(["abc", 123, "def", 456]) ➞ ["abc", "123", "def", "456"]

parse_list([1, 2, 3, 17, 24, 3, "a", "123b"]) ➞ ["1", "2", "3", "17", "24", "3", "a", "123b"]

parse_list([]) ➞ []


202. Given a fraction as a string, return whether or not it is greater than 1 when evaluated.

Examples
greater_than_one("1/2") ➞ False

greater_than_one("7/4") ➞ True

greater_than_one("10/10") ➞ False

203. Given a sandwich (as a list), return a list of fillings inside the sandwich. This involves ignoring the first and last elements.

Examples
get_fillings(["bread", "ham", "cheese", "ham", "bread"]) ➞ ["ham", "cheese", "ham"]

get_fillings(["bread", "sausage", "tomato", "bread"]) ➞ ["sausage", "tomato"]

get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]) ➞ ["lettuce", "bacon", "tomato"]

204. Create a function that flips M's to W's (all uppercase).

Examples
wumbo("I LOVE MAKING CHALLENGES") ➞ "I LOVE WAKING CHALLENGES"

wumbo("MEET ME IN WARSAW") ➞ "WEET WE IN WARSAW"

wumbo("WUMBOLOGY") ➞ "WUWBOLOGY"

205. Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.

Examples
oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}) ➞ "Emma"

oldest({
  "Max": 9,
  "Josh": 13,
  "Sam": 48,
  "Anne": 33
}) ➞ "Sam"


206. Given a list with an even amount of numbers, return True if the sum of two numbers in the list is even and False if the sum of two numbers in the list is odd.

To illustrate:

11, 15, 6, 8, 9, 10
11 + 15 = 26 = True
15 + 6 = 21 = False
6 + 8 = 14 = True
Examples
odd_sum_list([11, 15, 6, 8, 9, 10]) ➞ [True, False, True, False, False]

odd_sum_list([12, 21, 5, 9, 65, 32]) ➞ [False, True, True, True, False]

oddSumArr([1, 2, 3, 4, 5, 6]) ➞ [False, False, False, False, False]

207. You have two lists. One shows the names of the people names, while the other shows their occupation jobs. Your task is to create a dictionary displaying each person to their respective occupation.

Person	Job
Annie	Teacher
Steven	Engineer
Lisa	Doctor
Osman	Cashier
 -->
