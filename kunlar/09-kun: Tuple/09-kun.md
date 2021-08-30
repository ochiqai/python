# Tuple 

`tapl` (tuple) listga juda o'xshaydi. Eng asosiy farqi `list` `o'zgaradigan` strukturaga
kiradi. `tapl` esa `o'zgarmaydigan` struktura. Yana bir farqi `tapl` `()` qavsga olinib yoziladi. 
List esa `[]`. Mn:

```python
x = ('A', 'B', 'C')
```

Yagona elementga ega bo'ladigan `tapl` qilmoqchi bo'lsak, `,` vergul bilan ajratishim shart. Mn:

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

Deyarli `list`da ishlatiladigan hamma operatorlar `tapl`ga ham bo'laveradi.

Lekin, `tapl` o'zgarmaydigan (`immutable`) struktura bo'lganligi uchun, elementlarni o'zgartirib 
bo'lmaydi. Mn:

```python
x = ('a', 'b', 'c')
x[0] = 'k'
```

```python
--------------------------------------------------
TypeError: object doesn't support item assignment
```

Bu xato `tapl`ga qiymat yuklab bo'lmaydi degani.




## `tapl` o'zgaruvchilari

Aytaylik, ushbu `list` berilgan `x = ['A', 'B]`. Topshiriq shundayki, listning ikkala elementni
ikkita o'zgaruvchiga joylashtirish. Xo'sh qanday qilamiz? `tapl` yordamga keladi,

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

Mana shu xususiyat 2 ta o'zgaruvchi qiymatlarini almashtirishda juda qulay

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

Bunday amallarni bajarayotganimizda, chap va o'ng tarafdagilar teng bo'lishligi kerak.

```python
a, b = 1, 2, 3
```

Ushbu xato ro'y beradi. Yani, qiymtlar soni ko'p, o'zgaruvchilar soniga nisbatan.

```commandline
-------------------------------------
ValueError: too many values to unpack
```


## Ketma-ketliklar

Shu paytgacha biz `list`, `dkshnri` va `tapl`larni ko'rdik. Ular `data struktura`lari deb ataladi. 



## Foydali terminlar

- **data struktura**: bir-biriga bogliq qiymatlarning to'plami, Mn: `list`, `dkshnri`, `tapl`.
- **tapl**: o'zgarmaydigan va ketma ket tartibda kelgan elementlar.
- **tapl yuklash**: birdan ortiq o'zgaruvvhilarga bir daniga qiymat yuklash.


## Problem solving

1. `m = 'A', n = 'B'` o'zgaruvchi qiymatlarini almashtiring.
2. `x = ('1', '2', '3', '4')` `for` dan foydalanib element qiymatlarini konsolga chiqaring.
3. `x = ('1', '2', '3', '4')` `for` dan foydalanib element sonini chiqaring.
4. `tuple()` funksiyasi nima qiladi?
