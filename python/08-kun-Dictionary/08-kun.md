# Dictionary 
> o'qilishi dkshnri

* [Dictionary traversal](#dictionary-traversal)
* [Foydali terminlar](#foydali-terminlar)
* [Problem solving](#problem-solving)

`list`dagi elementlarni ko'rich uchun indekslardan foydalangandik. Va indeks butun sonlar bo'lishi 
kerak. Xo'sh biz agar indekslarni faqat butun sonlardan emas balki ixtiyoriy turga tegishli qilsak
bo'ladimi?

Bo'ladi!  **`dictionary`** yordamida. `list`ni indeks va qiymatni bog'laydigan 
tur dedik. `dictionary`lar ham xuddi shunday. Faqat indeks nomlanishi boshqacha. Yani uni `key`
deyiladi. Qiymatni `value` deyiladi. Ikkalasini birgalikda `key-value` juftlik deyiladi.

Masalan, ingliz-o'zbek lug'at tuzmoqchi bo'lsak ushbu `dictionary` turini qo'llasak bo'ladi.
Bunda `key`lar ingliz so'zi bo'lsa. `value`lar esa o'zbek so'zi bo'ladi.

`dictionary` hosil qilish uchun `dict` funksiyasidan foydalanamiz. 


```python
ingliz_dan_uzbek_ga = dict()
print(ingliz_dan_uzbek_ga)
```

```commandline
---
{}
```

`{}` qavslar bo'sh `dictionary` yaratilganligini bildiradi. Unda hech qanday `key` ham `value` (qiymat)
ham yo'q. Element qo'shish uchun kvadrat qavsdan foydalanamiz:

```python
ingliz_dan_uzbek_ga['book'] = 'kitob'
```

Hozir, bu yerda 'book' so'zi (string turida), o'zbekchada 'kitob' so'ziga bog'landi. 

Endi yana `dictionary`ni konsolga chiqarsak.

```python
print(ingliz_dan_uzbek_ga)
```

```commandline
-----------------
{'book': 'kitob'}
```

Boshqacha usulda ham kiritishimiz mumkin, 

```python
ingliz_dan_uzbek_ga = {'book': 'kitob'}
```

Bir necha so'zlarni birdaniga ham kiritishimiz mumkin.

```python
ingliz_dan_uzbek_ga = {'book': 'kitob', 'red': 'qizil', 'python': 'katta ilon'}
```

`list`da elementlar birin ketin kelgandi. O'shaning uchun indeksga `0` bersak u listda birinchi 
elementni olardi, agar 1-ni bersak ikkinchi elementni olardi vahokazo. `dictionary`da bunda ketma ketlik yo'q.

Agar 'red' ni uzbekchada nimaligini bilmoqchi bo'lsangiz, quyidagicha qilasiz

```python
print(ingliz_dan_uzbek_ga['red'])
```

```commandline
-----
qizil
```

Bordiyu berilgan `key` lug'atda bo'lmasa. `KeyError` degan  xato ro'y beradi. Mn:

```python
print(ingliz_dan_uzbek_ga['amazing'])
```

```commandline
-------------------
KeyError: 'amazing'
```
> `key` xatoligi ro'y berdi

`len` funksiyasi dictionarylarga ham qo'llasa bo'ladi. U `key-value` juftliklar sonini beradi.
Mn: `ingliz_dan_uzbek_ga`da 3 elementdan tashkil topgan.

```python
print(len(ingliz_dan_uzbek_ga))
```

```commandline
--
3
```

`in` operatori ham dictionaryda ishlaydi. Bunda berilgan `key` dictionaryda bor yo'qligini aniqlaydi.
Agar bor bo'lsa `True` aks holda `False` qaytaradi. Mn:

```python
print('book' in ingliz_dan_uzbek_ga)
print('amazing' in ingliz_dan_uzbek_ga)
```
```commandline
-----
True
False
```

Agar `value`(qiymat) ning dictionaryda bor yoki yo'qligini bilmoqchi bo'lsangiz, u holda `values` nomli
metoddan foydalanasiz. Bunda `values` metodi dictionaridagi barcha qiymatlarni qaytaradi. Keyin esa 
ularni `list` ga konvert qilsak bo'ladi.

```python
qiymatlar = list(ingliz_dan_uzbek_ga.values())
```

`qiymatlar` list bo'lganligi uchun bemalol `in` operatoridan foydalansak bo'ladi.


## Dictionary traversal 

Dictionaryda qanday qilib traversal qilamiz? albatta `for` aka orqali. 

```python
gollar_soni = {'Ronaldo': 600, 'Pele': 70, 'Messi': 500}
for key in gollar_soni:
    print(key, gollar_soni[key])
```

```commandline
------------
Ronaldo 600
Pele 70
Messi 500
```

Har xil amallarni bajarishimiz mumkin. Aytaylik qiymati 100 dan katta bo'lgan dictionary elementlarni chiqarish.

```python
gollar_soni = {'Ronaldo': 600, 'Pele': 70, 'Messi': 500}
for key in gollar_soni:
    if gollar_soni[key] > 100:
        print(key, gollar_soni[key])
```

```commandline
------------
Ronaldo 600
Messi 500
```

Aytaylik alfabet bo'yicha chiqarmoqchi bo'lsak, nima qilamiz?

- 1. Dictionaridagi `key`larni `keys` metodi orqali olamiz
- 2. listga o'tkazamiz
- 3. Listni sortirovka qilamiz
- 4. listni `for` orqali traversal qilib, har bir `key`ga qarashli qiymatini chiqaramiz

```python
gollar_soni = {'Ronaldo': 600, 'Pele': 70, 'Messi': 500}
list_soni = list(gollar_soni.keys())
list_soni.sort()
for key in list_soni:
    print(key, gollar_soni[key])
```

```commandline
------------
Messi 500
Pele 70
Ronaldo 600
```

Etibor bersak, `Messi > Pele > Ronaldo`.





## Foydali terminlar

- **key**: listga o'xshash indeks, lekin bunda nafaqat butun son balki boshqa tur ham bo'lishi mumkin.



## Problem solving

1. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`. `value`si 10 dan kichik bo'lgan dictionary
elementlarini chiqaring.
2. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`. `value`si 10 dan kichik bo'lgan dictionary
elementlar sonini toping. 
3. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`. `value`si 10 dan kichik bo'lgan dictionary
elementlarini ko'paytmasini toping.
4. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`. `value`si 10 dan kichik bo'lgan dictionary
elementlari yig'indisini toping.
5. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`.   `'b'` ni o'chiring va 
qolganlarini konsolga chiqaring.
6. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`.   `'d'` ni 29 ga o'zgartiring.
7. `a = "aaaabbbbcccdd"` har bir harf necha marta ishtirok etganini toping.
