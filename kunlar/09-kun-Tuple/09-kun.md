# tuple 
> taapl o'qilishi

* [`tuple` o'zgaruvchilari](#-tuple--o-zgaruvchilari)
* [Ketma-ketliklar](#ketma-ketliklar)
* [Foydali terminlar](#foydali-terminlar)
* [Problem solving](#problem-solving)


`tuple` (taapl) listga juda o'xshaydi. Eng asosiy farqi `list` `o'zgaradigan` strukturaga (mutable)
kiradi. `tuple` esa `o'zgarmaydigan` struktura (immutable). Yana bir farqi `tuple` `()` qavsga olinib yoziladi. 
List esa `[]`. Mn:

```python
x = ('A', 'B', 'C')
```

Yagona elementga ega bo'ladigan `tuple` qilmoqchi bo'lsak, `,` vergul bilan ajratishim shart. Mn:

```python
x = ('A', )
```

Agar vergulni unutsangiz, u string bo'lib qoladi.
Boshqa usuli, `tuple` funksiyasini chaqirish orqali bo'ladi.

```python
x = tuple('abc')
print(x)
```

```commandline
---------------
('a', 'b', 'c')
```

Deyarli `list`da ishlatiladigan hamma operatorlar `tuple`ga ham bo'laveradi.

Lekin, `tuple` o'zgarmaydigan (`immutable`) struktura bo'lganligi uchun, elementlarni o'zgartirib 
bo'lmaydi. Mn:

```python
x = ('a', 'b', 'c')
x[0] = 'k'
```

```python
--------------------------------------------------
TypeError: object doesn't support item assignment
```

Bu xato `tuple`ga qiymat yuklab bo'lmaydi degani.




## `tuple` o'zgaruvchilari

Aytaylik, ushbu `list` berilgan `x = ['A', 'B']`. Topshiriq shundayki, listning ikkala elementini
ikkita o'zgaruvchiga joylashtirish. Xo'sh qanday qilamiz? 

`tuple` da ajoyib qilsa bo'ladi,

```python
m = ['A', 'B']
x, y = m
print(x)
print(y)
```
```commandline
A
B
```

Mana shu xususiyat 2 ta o'zgaruvchi qiymatlarini almashtirishda ayni muddao:

```python
a = 5
b = 10
print(a, b)
a, b = b, a
print(a, b)
```


```commandline
5, 10
10, 5
```

Bunday amallarni bajarayotganimizda, chap va o'ng tarafdagi ifodalar soni teng bo'lishligi kerak.

```python
a, b = 1, 2, 3
```

Ushbu xato ro'y beradi. Yani, qiymatlar soni ko'p o'zgaruvchilar soniga nisbatan.

```commandline
-------------------------------------
ValueError: too many values to unpack
```


## Ketma-ketliklar

Shu paytgacha biz `list`, `dictonary` va `tuple`larni ko'rdik. Ular `data struktura`lari deb ataladi.
Guvohi bo'lganingizdek, datalar (qiymatlar/malumotlar) hammasida har xil joylashtirilayapti. Bunga katta 
sabab bor va buni bilish har bir programmist uchun o'ta muhim. Lekin hozir buni muhokama qilmaymiz. 
Alloh nasib qilsa kelajakda albatta.



## Foydali terminlar

- **data struktura**: bir-biriga bog'liq qiymatlarning to'plami, Mn: `list`, `dictionary`, `tuple`.
- **tuple**: o'zgarmaydigan va ketma ket tartibda kelgan elementlar.
- **tuple yuklash**: birdan ortiq o'zgaruvchilarga bir daniga qiymat yuklash.


## Problem solving

1. `m = 'A', n = 'B'` o'zgaruvchi qiymatlarini almashtiring.
2. `x = ('1', '2', '3', '4')` `for` dan foydalanib element qiymatlarini konsolga chiqaring.
3. `x = ('1', '2', '3', '4')` `for` dan foydalanib element sonini chiqaring.
4. `tuple()` funksiyasi nima qiladi?
