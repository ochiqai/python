# Fayl 
> File inglizchasiga

Bugun fayllar bilan ishlashni o'rganamiz.

* [Faylni o'qish](#faylni-oqish)
* [Fayl va `for`](#fayl-va-for)
* [Faylga yozish](#faylga-yozish)
* [`with` operatori](#with-operatori)
* [Xulosa](#xulosa)
  


## Faylni o'qish 
Ataylik bizda `kundalik.txt` nomli fayl bo'lsin. Unda quyidagicha yozilgan bo'lsin:

```text
Ertalab turib nonushta qildim
Inglizcha lug'at yodladim
Keyin aylanib keldim
va boshqa narsalar
```

Pythonda fayl ochish uchun `open` (ochish) funksiyasidan foydalanamiz. Ya'ni quyidagicha

```python
fayl_och = open(fayl_joylashgan_joy, 'r')
```
 - Bunda `fayl_joylashgan_joy` ga fayl qayerda bo'lsa o'shani ko'rsatishimiz kerak. Aytaylik, fayl joylashgan joy 
`C:\Users\ochiqai\kundalik.txt` bo'lsin. Unda quyidagicha ochamiz
 - `'r'` argumenti faylni o'qishlilikni bildiradi `r` degani `read` ya'ni o'qish degani.

```python
fayl_och = open("C:\\Users\\ochiqai\\kundalik.txt", "r")
```

yoki

```python
fayl_och = open(r"C:\Users\ochiqai\kundalik.txt", "r")
```

Binobarin, keling `kundalik.txt` faylni ochamiz va uni ichidagini o'qib ekranga chiqaramiz

```python
fayl_och = open(r"kundalik.txt", "r")
tekst = fayl_och.read()
print(tekst)
fayl_och.close()
```

```commandline
Ertalab turib nonushta qildim
Inglizcha lug'at yodladim
Keyin aylanib keldim
va boshqa narsalar
```
E'tibor bering, biz ochilgan faylni `fayl_och.close()` orqali yopayapmiz. Xuddi bu faylni ochdik undan foydalandik va keyin 
yopdik degandek gap. 

Yuqorida biz fayl ichidagi hamma tekstlarni `birdaniga` o'qib chiqarib yubordik. Bunday qilishimiz kichik fayllar uchun durust,
Lekin katta fayllar bilan ishlaganimizda ko'p xotira talab qiladi hamda sekin ishlaydi. Shuning uchun qatorma qator o'qish uchun 
`readline` funksiyaisni mavjud (`line` bu yerda qator ma'nosida kelayapti). Ya'ni,

```python
fayl_och = open(r"kundalik.txt", "r")
tekst = fayl_och.readline()
print(tekst)
fayl_och.close()
```

```commandline
Ertalab turib nonushta qildim
```

Yuqoridagi misol faqat birinchi qatorni o'qiydi. Hamma qatorni o'qish uchun esa `readlines` funksiyasidan foydalanamiz.
Bunda qatordagi tekstlarning hammasi listga joylanadi. 

```python
fayl_och = open(r"kundalik.txt", "r")
tekst = fayl_och.readlines()
print(tekst)
fayl_och.close()
```

```commandline
['Ertalab turib nonushta qildim\n', "Inglizcha lug'at yodladim\n", 'Keyin aylanib keldim\n', 'va boshqa narsalar']
```


## Fayl va `for`

Fayl tekslarini `for` loopi orqali ham o'qishimiz mumkin,

```python
# faylni ochib, for orqali tesktni o'qish
fayl_och = open(r"kundalik.txt", "r")
for qator in fayl_och:
    print(qator)
fayl_och.close()
```
```commandline
Ertalab turib nonushta qildim

Inglizcha lug'at yodladim

Keyin aylanib keldim

va boshqa narsalar
```
Shu paytgacha fayldan o'qishni ko'rdik, endi faylga yozishni ko'ramiz.


## Faylga yozish

Fayl yozish uchun yuqoridagi `open` funksiyasiga bitta o'zgartirish kiritamiz xolos!
Ya'ni `r` o'rniga `w` qo'yamiz. `w` write ya'ni yozish demakdir. Misol,
```python
fayl_och = open(r"tun.txt", "w")
fayl_och.write("Bu faylga yozish edi xolos.")
fayl_och.close()
```
Fayl ochdik `tun.txt` nomli, va uni ichiga `write` funksiyasi orqali `""Bu faylga yozish edi xolos."` deb yozdik
Ishni tugatganimizdan so'ng faylni yopdik `fayl_och.close()`.

Agar string listi bo'lsa `write` o'rniga `writelines` funksiyasidan foydalaning.


## `with` operatori

Yuqorida biz har doim fayl ochganimizda `close` qilib yopardik, va bu narsa esdan chiqmaslik kerak edi. Qulaylikni (va bosha narsalar)
 ni oshirish uchun `with` operatori qo'llaniladi.

```python
with open(r"kundalik.txt", "r") as fayl_och:
    text = fayl_och.read()
print(text)
fayl_och.close()
```
Umuman olganda juda o'xshaydi, taqqoslashni o'zingiz qilasiz.

## Xulosa
 - Fayldan qanday qilib tekstni o'qishni (read) bilasiz.
 - Faylga qanday qilib tekst yozishni (write) bilasiz.
 - Va `with` operatoridan ham xabardor bo'ldingiz.