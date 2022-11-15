### Pytohnda vektorlar haqida tushuncha va ularning taqqoslanishi.


#### Vektor nima?

Oddiy so'z bilan aytganda vektorni bir o'lchovli massiv deb hisoblash mumkin. Python tiliga kelsak, vektor ro'yxatlarning bir o'lchovli massividir. U elementlarni Python ro'yxatiga o'xshash tarzda egallaydi.

#### Pythonda vektor yaratish

Python NumPy moduli vektor yaratish uchun ishlatiladi. Bir o'lchovli massiv, ya'ni vektor yaratish uchun numpy.array() usulidan foydalanamiz.

Syntax:

```python
numpy.array(list)
```

Example 1: Gorizontal vektor

```python
import numpy as np 

lst = [10,20,30,40,50] 

vctr = np.array(lst) 

print("List buyicha yaratilgan vektor:") 
print(vctr)
```
Output:
```terminal
List buyicha yaratilgan vektor:
[10 20 30 40 50]
```

Example 2: Vertikal Vector

```python
import numpy as np 

lst = [[2], 
        [4], 
        [6],
          [10]]  

vctr = np.array(lst) 

print("List buyicha yaratilgan vektor:") 
print(vctr)
```

Output:
```python
List buyicha yaratilgan vektor:
[[ 2]
 [ 4]
 [ 6]
 [10]]
```

#### Python vektorida asosiy operatsiyalar

Vektorni yaratgandan so'ng, keling, endi ushbu Vektorlar ustida bir nechta asosiy operatsiyalarni bajaramiz! <br>
Quyidagilar vektorda bajarilishi mumkin bo'lgan asosiy operatsiyalar ro'yxati - 

* Addition (qo'shish)
* Subtraction (ayirish)
* Multiplication (ko'paytirish)
* Division (bo'lish)
* Dot Product (nuqta amali) va boshqalar

#### 1. Python vektorida qo'shish operatsiyasini bajarish

Bunda ikki vektorning elementlari buyicha amal bajariladi va ikkala vektorning ham uzunligi bir xil buladi.

Example:

```python
import numpy as np 

lst1 = [10,20,30,40,50] 
lst2 = [1,2,3,4,5]


vctr1 = np.array(lst1) 

vctr2= np.array(lst2) 


print("list 1 dan vektor yaratildi:") 
print(vctr1) 
print("list 2 dan vektor yaratildi:") 
print(vctr2) 

vctr_add = vctr1+vctr2
print("Vektorlarning yig'indisi: ",vctr_add)
```

Output:
```console
list 1 dan vektor yaratildi:
[10 20 30 40 50]
list 2 dan vektor yaratildi:
[1 2 3 4 5]
Vektorlarning yig'indisi:  [11 22 33 44 55]
```

#### 2. Python vektorida ayirish operatsiyasini bajarish

Example:

```python
import numpy as np 

lst1 = [10,20,30,40,50] 
lst2 = [1,2,3,4,5]


vctr1 = np.array(lst1) 

vctr2= np.array(lst2) 


print("list 1 dan vektor yaratildi:") 
print(vctr1) 
print("list 2 dan vektor yaratildi:") 
print(vctr2) 

vctr_sub = vctr1-vctr2
print("Vektorlarning ayirmasi: ",vctr_sub)
```

Output:
```console
list 1 dan vektor yaratildi:
[10 20 30 40 50]
list 2 dan vektor yaratildi:
[1 2 3 4 5]
Vektorlarning ayirmasi:  [ 9 18 27 36 45]
```

#### 3. Python vektorida ko'paytirish operatsiyasini bajarish

Bunda ikki vektor elementlari ko'paytiriladi va ikkila vektor uzunligi teng bo'ladi.

Keling, ko'paytirish amalini tasavvur qilishga harakat qilaylik:  <br>
x = [10, 20] va y = [1, 2] ikkita vektor mavjud. Shunday qilib, mahsulot vektori v[ ] bo'ladi, <br>

v[0] = x[0] * y[0] <br>
v[1] = x[1] * y[1]

Quyidagi kodni ko'rib chiqing!

```python
import numpy as np 

lst1 = [10,20,30,40,50] 
lst2 = [1,2,3,4,5]

vctr1 = np.array(lst1) 

vctr2= np.array(lst2) 

print("list 1 dan vektor yaratildi:") 
print(vctr1) 
print("list 2 dan vektor yaratildi:") 
print(vctr2) 

vctr_mul = vctr1*vctr2
print("Vektorlaring ko'paytmasi: ",vctr_mul)
```

Output:
```console
list 1 dan vektor yaratildi:
[10 20 30 40 50]
list 2 dan vektor yaratildi:
[1 2 3 4 5]
Vektorlaring ko'paytmasi:  [ 10  40  90 160 250]
```

#### 4. Python vektorida bo'lish operatsiyasini bajarish

Yaxshiroq tushunish uchun quyidagi misolni ko'rib chiqing.

x = [10, 20] va y = [1, 2] ikkita vektor mavjud. Shunday qilib, mahsulot vektori v[ ] bo'ladi, <br>

v[0] = x[0] / y[0] <br>
v[1] = x[1] / y[1]

Example:
```python
import numpy as np 
 
lst1 = [10,20,30,40,50] 
lst2 = [10,20,30,40,50]
 
vctr1 = np.array(lst1) 
 
vctr2= np.array(lst2) 
 
print("list 1 dan vektor yaratildi:") 
print(vctr1) 
print("list 2 dan vektor yaratildi:") 
print(vctr2) 
 
vctr_div = vctr1/vctr2
print("Vektorlar bo'linmasi: ",vctr_div)
```

Output:
```console
list 1 dan vektor yaratildi:
[10 20 30 40 50]
list 2 dan vektor yaratildi:
[10 20 30 40 50]
Vektorlar bo'linmasi:  [ 1 1 1 1 1 ]
```

#### Vektor Dot 

Bu amalda biz ikki vektorning elementlari buyicha bajaramiz.
<br>
`Vektor Dot` amalini tushunib olish uchun quyidagi misolga e'tibor bering: <br>
`vector c = x . y = (x1 * y1 + x2 * y2)`

Example:
```python
import numpy as np 

lst1 = [10,20,30,40,50] 
lst2 = [1,1,1,1,1]


vctr1 = np.array(lst1) 

vctr2= np.array(lst2) 


print("list 1 dan vektor yaratildi:") 
print(vctr1) 
print("list 2 dan vektor yaratildi:") 
print(vctr2) 

vctr_dot = vctr1.dot(vctr2)
print("Vektor Dot amalinining natijasi: ",vctr_dot)
```

Output:
```console
list 1 dan vektor yaratildi:
[10 20 30 40 50]
list 2 dan vektor yaratildi:
[1 1 1 1 1]
Vektor Dot amalinining natijasi: 150
```

* Vektorlar haqida tushuncha hosil qilib oldik, endi vektorlarning qanday taqqoslanishini ko'rib chiqamiz.

#### Vektorlarni taqqoslash

Vektorlarni taqqoslanishini bir nechta usullari mavjud.
Masalan: 
Euclidean, Cosine, Hamming, Manhattan va boshqalar.

<p align="center">
    <img src="./image/vektor_taqqoslash_usullari.jpg">
</p>


Biz `cosine similarity` formulasi orqali vektorlarni taqqoslashni ko'rib o'tamiz.

<p align="center">
    <img src="./image/cosine_formulasi.png">
</p>

* Formuladagi amallarni pythonda tartib buyicha bajarib ko'ramiz.
<br>
* Vektorlarni hosil qilib olamiz.
```python
v1 = [1, 2, 3, 4, 5]
v2 = [1, 2, 3, 4, 5]
v3 = [1, 2, 3, 4, 6]
v4 = [100, 2, 3, 4, 5]
```
* Keling birinchi kasrning surat qismini bajarib olamiz. Bunda biz A va B vektorlarning elementlarini ko'paytirib qushib borishimiz kerak. Bu jarayonni `while` yordamida bajarib o'tamiz. Tushunarli bo'lishi uchun har bir jarayonni funksiya orqali bajarib o'tamiz.

```python
def surat(a,b):
    i = 0
    kasr_surati = 0
    while i < len(a):
        kasr_surati += (a[i] * b[i])
        i += 1
    return kasr_surati
```

* E'tibor bersangiz formulamizning maxraj qismida ildiz amali mavjud. Bu amalni bajarish uchun `ildiz` nomli funksiya yaratib o'tamiz va kerakli joyda funksiyani chaqirib ishlatamiz.

```python
def ildiz(x):
    return math.sqrt(x)
```

* Kasrning maxraj qismida bizdan vektorlarimizning xar bir elementini olib, va uni kvadratga oshirib, qushib borishimizni talab qilmoqda. Hosil bo'lgan yig'indilarni ildizlarining ko'paytmasini bajarib o'tishimiz lozim.
<br>
Maxraj qismining ishlanishi:

```python
def maxraj(a,b):
    # modul
    i = 0
    modul_a = 0
    modul_b = 0
    while i < len(a):
        modul_a += (a[i] * a[i])
        modul_b += (b[i] * b[i])
        i += 1

    modul_a = ildiz(modul_a)
    modul_b = ildiz(modul_b)
    kasr_maxraji = modul_a * modul_b
    return kasr_maxraji
```

* Endi biz `vector_taq` nomli yangi funksiya hosil qilib olamiz. Kasrning surat qismini maxraj qismiga bo'lsak yetarli.

```python
def vector_taq(a, b):
    # kosinus o'xshashlik https://en.wikipedia.org/wiki/Cosine_similarity
    # 1*1 + 2*2 + 2*2 + 1*2 + 1*1 + 1*1
    if len(a) == len(b):
        yaqinlik = surat(a,b) / maxraj(a,b)
        return yaqinlik
    else:
        print("Elementlar soni teng bo'lish kerak!")
```
* Yuqorida vektorlarning uzunliklari teng bulishligi lozim deb shart berib otdik. 

* Bajargan jarayonlarimizning umumiy ko'rinishi.

```python
import math

def surat(a,b):
    i = 0
    kasr_surati = 0
    while i < len(a):
        kasr_surati += (a[i] * b[i])
        i += 1
    return kasr_surati

def ildiz(x):
    return math.sqrt(x)

def maxraj(a,b):
    # modul
    i = 0
    modul_a = 0
    modul_b = 0
    while i < len(a):
        modul_a += (a[i] * a[i])
        modul_b += (b[i] * b[i])
        i += 1

    modul_a = ildiz(modul_a)
    modul_b = ildiz(modul_b)
    kasr_maxraji = modul_a * modul_b
    return kasr_maxraji

def vector_taq(a, b):
    # kosinus o'xshashlik https://en.wikipedia.org/wiki/Cosine_similarity
    # 1*1 + 2*2 + 2*2 + 1*2 + 1*1 + 1*1
    if len(a) == len(b):
        yaqinlik = surat(a,b) / maxraj(a,b)
        return yaqinlik
    else:
        print("Elementlar soni teng bo'lish kerak!")


v1 = [1, 2, 3, 4, 5]
v2 = [1, 2, 3, 4, 5]
v3 = [1, 2, 3, 4, 6]
v4 = [100, 2, 3, 4, 5]


natija1 = vector_taq(v1, v2)
natija2 = vector_taq(v1, v3)
natija3 = vector_taq(v1, v4)

print(natija1)
print(natija2)
print(natija3)
```

* Bajarib o'tkan dasturimizni ishlatib o'tsak quyidagi natijani olamiz.

```console
1.0
0.9958591954639383
0.20709515355464156
```

#### Vektorlarni taqqoslash uchun tayyor kutibxonadan foydalanish

* Vektorlarni taqqoslashda biz tayyor kutibxonadan foydalanishni ko'ramiz. Buning uchun biz `cosine_similarity` va `numpy` kutubxonalarini `import` qilib olishimiz lozim.

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

v1 = [1, 2, 3, 4, 5]
v2 = [1, 2, 3, 4, 5]
v3 = [1, 2, 3, 4, 6]
v4 = [100, 2, 3, 4, 5]

natija1 = cosine_similarity(np.array(v1).reshape(1, -1), np.array(v2).reshape(1, -1))[0][0]
natija2 = cosine_similarity(np.array(v1).reshape(1, -1), np.array(v3).reshape(1, -1))[0][0]
natija3 = cosine_similarity(np.array(v1).reshape(1, -1), np.array(v4).reshape(1, -1))[0][0]

print(natija1)
print(natija2)
print(natija3)
```
* Yuqorida bajarib o'tkanimizdek bunda ham bir xil natijani olamiz.

```console
1.0
0.9958591954639383
0.2070951535546416
```
