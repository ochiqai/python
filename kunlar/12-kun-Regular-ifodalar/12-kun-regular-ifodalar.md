# Regular ifodalar 

Biz programmalash davomida tekstlarni protses qilishimizga to'g'ri keladi. Bunday holat 
ko'p uchraydi. Masalan, ko'p tekstlardan faqat o'zimizga kerak bo'ladigan elektron adresslarni olish yoki sonlarni 
olish kabi amallarni bajarishimiz mumkin. Albatta, bu amallarni o'rgangan fayldan o'qib va undan keyin `string` ni 
qo'llasak bo'ladi. Lekin bunday qilish ko'p vaqt va energiya ketadi. Shu sababli pythonda `regular ifodalar` deb 
nomlangan biblioteka bor. Va biz ushbu bibliotekani qisman o'rganamiz. Bu mavzu juda katta hisoblanadi
bu haqida xatto butun kitoblar yozilgan.


## `import re`

Pythonda regular ifoda `import re` orqali bo'ladi. `re` (ko'rinib turgandek) kengaytmasi 
regular expression deb ataladi. 

Masalan quyidagi faylni olaylik, [regifoda.txt](regifoda.txt). Orginal tekst [manbai](http://www.py4inf.com/code/mbox-short.txt).  

<details><summary>regifoda.txt dan parcha</summary>
Oliy Majlis Qonunchilik palatasida 3-dekabr kuni “O‘zbekiston Respublikasining Jinoyat kodeksiga korrupsiyaga oid jinoyatlar uchun javobgarlik muqarrarligini ta’minlashga qaratilgan o‘zgartish va qo‘shimchalar kiritish to‘g‘risida”gi qonun loyihasi birinchi o‘qishda qabul qilindi. Bu haqda Senat axborot xizmati xabar qildi.
Ma’lum qilinishicha, mansabdor shaxslarning jinoyatlari oqibatida davlat va jamiyat manfaatlariga 2018-yilda 556 milliard so‘m, 2019-yilda 1,858 trillion so‘m, 2020-yilda 500,1 milliard so‘m, 2021-yilning 9 oyida 658 milliard so‘m moddiy zarar yetkazilgan. Mazkur qonun loyihasi bilan mansabdor shaxslarga nisbatan choralar kuchaytirilmoqda.
Jumladan, “Hokimiyat yoki mansab vakolatini suiiste’mol qilish”, “Hokimiyat yoki mansab vakolati doirasidan chetga chiqish”, “Hokimiyat harakatsizligi”, “Mansab soxtakorligi” va “Hokimiyatni suiiste’mol qilish, hokimiyat vakolatidan tashqariga chiqish yoki hokimiyat harakatsizligi” jinoyatlar agar “g‘arazgo‘ylik” niyatida sodir etilsa, korrupsiyaviy jinoyat hisoblanishi belgilanib, mazkur harakatlar uchun og‘irroq jazolar belgilangan.
Shuningdek, o‘zlashtirish yoki rastrata yo‘li bilan firibgarlik qilish, soliq va boshqa majburiy to‘lovlarni to‘lashdan bosh tortish uchun hukm qilingan, biroq yetkazilgan zararni to‘liq qoplamagan shaxslarga va poraxo‘rlik bilan bog‘liq jinoyatni sodir etgan shaxslarga nisbatan jazodan muddatidan ilgari shartli ravishda ozod qilish yoki jazoni yengilrog‘i bilan almashtirish tatbiq qilinmasligi nazarda tutilgan.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.90])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Sat, 05 Jan 2008 09:14:16 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Sat, 05 Jan 2008 09:14:16 -0500
Received: from holes.mr.itd.umich.edu (holes.mr.itd.umich.edu [141.211.14.79])
	by flawless.mail.umich.edu () with ESMTP id m05EEFR1013674;
	Sat, 5 Jan 2008 09:14:15 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY holes.mr.itd.umich.edu ID 477F90B0.2DB2F.12494 ;
	 5 Jan 2008 09:14:10 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 5F919BC2F2;
	Sat,  5 Jan 2008 14:10:05 +0000 (GMT)
Message-ID: <200801051412.m05ECIaH010327@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 899
          for <source@collab.sakaiproject.org>;
          Sat, 5 Jan 2008 14:09:50 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id A215243002
	for <source@collab.sakaiproject.org>; Sat,  5 Jan 2008 14:13:33 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m05ECJVp010329
	for <source@collab.sakaiproject.org>; Sat, 5 Jan 2008 09:12:19 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m05ECIaH010327
	for source@collab.sakaiproject.org; Sat, 5 Jan 2008 09:12:18 -0500
Date: Sat, 5 Jan 2008 09:12:18 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
To: source@collab.sakaiproject.org
From: stephen.marquard@uct.ac.za
Subject: [sakai] svn commit: r39772 - content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Sat Jan  5 09:14:16 2008
X-DSPAM-Confidence: 0.8475
X-DSPAM-Probability: 0.0000
</details>

## `^` Karet 
> `^` caret (ingliz tilida) 

Eng birinchi `^` belgisini o'rganamiz. Bu belgini dehqonchasiga `qator boshidan qidir` deb
tarjima qilishimiz mumkin. Quyidagi programmada, `regifoda.txt` faylini o'qib, `re.search` funksiyasi 
orqali har bir qatordan `Jumladan` degan so'zni qidirayapmiz. Agar qidirayotgan so'zimiz, qatorda bo'lsa
o'sha qatorni ekranga konsolga chiqargin deyapmiz,

```python
# ^ karet bilan ishlash, qator boshini bildiradi
import re

fayl = open("regifoda.txt", 'r')
for qator in fayl.readlines():
    qator = qator.rstrip()
    if re.search("^Jumladan", qator):
        print(qator)
```

Konsolda
```commandline
Jumladan, “Hokimiyat yoki mansab vakolatini suiiste’mol qilish”, “Hokimiyat yoki mansab vakolati doirasidan chetga chiqish”, “Hokimiyat harakatsizligi”, “Mansab soxtakorligi” va “Hokimiyatni suiiste’mol qilish, hokimiyat vakolatidan tashqariga chiqish yoki hokimiyat harakatsizligi” jinoyatlar agar “g‘arazgo‘ylik” niyatida sodir etilsa, korrupsiyaviy jinoyat hisoblanishi belgilanib, mazkur harakatlar uchun og‘irroq jazolar belgilangan.
```

## `.` Nuqta 
> `.`  period, full stop (ingliz)

Nuqta belgisi ixtiyoriy xarf bo'lishi mumkin degan ma'noni bildiradi. Masalan,  
boshlanishi `y` va tugashi `i` belgisi bilan tugaydigan qatorlarni konsolga chiqarish
kerak bo'lsin. Unda biz quyidagicha yozamiz `y..i`, yani ikki nuqta o'rniga ixtiyoriy harflar bo'lishi
mumkinligini bildiradi. Buni quyidagi programmada qo'llasak,

```python
#  nuqtalar bilan ishlash, nuqtalar ixtiyoriy belgiga ruhsat borligini bildiradi
fayl = open("regifoda.txt", 'r')
for qator in fayl.readlines():
    qator = qator.rstrip()
    if re.search("y..i", qator):
        print(qator)
```

Konsolda
```commandline
Jumladan, “Hokimiyat yoki mansab vakolatini suiiste’mol qilish”, “Hokimiyat yoki mansab vakolati doirasidan chetga chiqish”, “Hokimiyat harakatsizligi”, “Mansab soxtakorligi” va “Hokimiyatni suiiste’mol qilish, hokimiyat vakolatidan tashqariga chiqish yoki hokimiyat harakatsizligi” jinoyatlar agar “g‘arazgo‘ylik” niyatida sodir etilsa, korrupsiyaviy jinoyat hisoblanishi belgilanib, mazkur harakatlar uchun og‘irroq jazolar belgilangan.
Shuningdek, o‘zlashtirish yoki rastrata yo‘li bilan firibgarlik qilish, soliq va boshqa majburiy to‘lovlarni to‘lashdan bosh tortish uchun hukm qilingan, biroq yetkazilgan zararni to‘liq qoplamagan shaxslarga va poraxo‘rlik bilan bog‘liq jinoyatni sodir etgan shaxslarga nisbatan jazodan muddatidan ilgari shartli ravishda ozod qilish yoki jazoni yengilrog‘i bilan almashtirish tatbiq qilinmasligi nazarda tutilgan.
Received: from eyewitness.mr.itd.umich.edu (eyewitness.mr.itd.umich.edu [141.211.93.142])
	by mission.mail.umich.edu () with ESMTP id m04JoHJi019755;
	BY eyewitness.mr.itd.umich.edu ID 477E8DF2.67B91.5278 ;
Subject: [sakai] svn commit: r39765 - in gradebook/trunk/app: business/src/java/org/sakaiproject/tool/gradebook/business business/src/java/org/sakaiproject/tool/gradebook/business/impl ui ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/beans ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/entity ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/params ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/producers ui/src/webapp/WEB-INF ui/src/webapp/WEB-INF/bundle ui/src/webapp/content/templates
Received: from eyewitness.mr.itd.umich.edu (eyewitness.mr.itd.umich.edu [141.211.93.142])
	BY eyewitness.mr.itd.umich.edu ID 477D8300.AC098.32562 ;
```
`y..i` ga o'shashso'zlar yuqoridagi qatorlarda quyidagicha kelgan:
 - 1-qatorda `yoki` kelgan. Ikki nuqta o'rniga `ok` kelgan.
 - 2-qator 1-qatorga o'xshash
 - 3-qatorda `yewi`
 - 4-qatorda `y mi`
 - vahokazo


## .+ Nuqta plus
Biz yuqorida nuqta belgisini ko'rib o'tdik. U foydali qachonki biz qidiryotgan narsamizning uzunligini
bilsak. Lekin, ko'p hollarda biz bilmaymiz. Shunday vaqtda, `.+` belgisi qo'l keladi. Quyidagi programmaga etibor bering.

```python
import re

fayl = open("regifoda.txt", 'r')
for qator in fayl.readlines():
    qator = qator.rstrip()
    if re.search("^From:.+@", qator):
        print(qator)
```

`"^From:.+@"` ni tarjima qilsak
> (^)So'z boshidan `From:` va undan keyin birdan ortiq belgilar kelsin 
> va undan keyin @ (kuchukcha) belgisi kelsin

Konsolga quyidagi chiqadi:

```commandline
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: zqian@umich.edu
From: gsilver@umich.edu
From: wagnermr@iupui.edu
From: zqian@umich.edu
From: antranig@caret.cam.ac.uk
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: ray@media.berkeley.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
```

Natijadan ko'rishimiz mumkinki hamma qator `From:` dan boshlangan va `@` belgisi bor.


## `findall` va `\S`

Shu paytgacha biz `re.search` funksiyasidan foydalandik. Endi `findall` funksiyasidan foydalanamiz
hamda `\S` operatoridan foydalanishni ko'ramiz. Bu funksiya berilgan kalit so'z orqali tekstdan qidiradi
va topilganlarni `list` shaklida qaytaradi. Masalan, quyidagi tekstni olaylik
```python
# \S+@\S+: berilgan stringdan shunday substringlarni qidiringki, undagi substringlar boshlanish belgilardan bulib
# undan keyin @ belgi bo'lib va undan keyin yana belgilar bo'lishi kerak
s = 'Biz xabarni ulugbek@gmail.com dan oldik, keyin uni nuriddin@gmail.com ga yubordik'
lst = re.findall('\S+@\S+', s)
print(lst)
```

`re.findall` ga `'\S+@\S+'` maxsus belgilarni joyladik. `'\S+@\S+'` degani, shunday so'zlarni teksdan qidiringki
- `\S+` ularni boshi belgilardan tashkil topsin, lekin belgilar birortasi bo'sh belgi (`" "`) bo'lmaligi kerak 
- `@` undan keyin kuchukcha belgisi bo'lsin
- `\S+` ularni oxiri belgilardan tashkil topsin, lekin belgilar birortasi bo'sh belgi (`" "`) bo'lmaligi kerak

Ishlatsak konsolga quyidagicha natija chiqadi:

```commandline
['ulugbek@gmail.com', 'nuriddin@gmail.com']
```

Xuddi shu maxsus belgilarni faylga qo'llasak, quyidagicha bo'ladi:

```python
fayl = open("regifoda.txt", 'r')
for qator in fayl.readlines():
    qator = qator.rstrip()
    lst = re.findall('\S+@\S+', qator)
    if lst != []:
        print(lst)
```

Konsolga

```commandline
['stephen.marquard@uct.ac.za']
['<postmaster@collab.sakaiproject.org>']
['<200801051412.m05ECIaH010327@nakamura.uits.iupui.edu>']
['<source@collab.sakaiproject.org>;']
['<source@collab.sakaiproject.org>;']
['<source@collab.sakaiproject.org>;']
['apache@localhost)']
```

Yuqoridagi natija elektron adreslarni chiqarishdir. Lekin, etibor bersak
bazilarida xar xil biz xoxlamaydigan belgilar mavjud xususan `<;>`. 

> Qanday qilib, ushbu belgilarni olish tashlaymiz? 

Bunda bizga tor'burchak qavs yordamga keladi - `[]` to'rtburchak qavs. Bunda
biz nimani xoxlashimizni oydinlashtirishimiz mumkin. Masalan, yuqoridagini aytishimiz mumkin
faqat kichik, yoki katta yoki sonlardan tashkil topsin deb

```python
[a-zA-Z0-9]
```
Ya'ni
- a-z: a dan z gacha bo'lgan harflar bo'lishi mumkin. Qisqacha hamma kichik harflar
- A-Z: A dan Z gacha bo'lgan harflar bo'lishi mumkin. Qisqacha hamma Katta harflar
- 0-9: 0 dan 9 gacha bo'lgan sonlar bo'lishi mumkin

 Shundan foydalin quyidagi programmani yozishimiz mumkin

```python
tozaroq elektron addresslarni chiqarish
fayl = open("regifoda.txt", 'r')
for qator in fayl.readlines():
    qator = qator.rstrip()
    lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', qator)
    if lst != []:
        print(lst)
```

E'tibor bering biz bu yerda `+` o'rniga * ko'paytirish belgisini qo'ydik, chunki `[]` belgisi 1 ta xarf
o'rniga o'tadi. `*` belgi bittadan ortiq belgilar uchun qo'llaniladi.

Konsolga:

```commandline
['stephen.marquard@uct.ac.za']
['postmaster@collab.sakaiproject.org']
['200801051412.m05ECIaH010327@nakamura.uits.iupui.edu']
['source@collab.sakaiproject.org']
['source@collab.sakaiproject.org']
['source@collab.sakaiproject.org']
['apache@localhost']
['source@collab.sakaiproject.org']
['stephen.marquard@uct.ac.za']
['source@collab.sakaiproject.org']
['stephen.marquard@uct.ac.za']
['stephen.marquard@uct.ac.za']
['louis@media.berkeley.edu']
['postmaster@collab.sakaiproject.org']
['200801042308.m04N8v6O008125@nakamura.uits.iupui.edu']
['source@collab.sakaiproject.org']
['source@collab.sakaiproject.org']
['source@collab.sakaiproject.org']
['apache@localhost']
['source@collab.sakaiproject.org']
```


## `()` Qavs

Shunday holatlar bo'ladiki. Biz nafaqat biron nimani qidiramiz
balki birion malumotni ajratib olishimizga ham to'g'ri keladi. Shunday holatlarda, qavs (`()`) dan 
foydalanamiz. Keling birinchi quyidagi programmani ishlataylik. Bu yerda maxsus beligilar - 
`^X\S*: [0-9.]+` shuni anglatadiki: qator boshi `X` bilan boshlansin, va undan keyin bo'shliq bo'lmagan
bir necha belgilarkelsin toki `:`, va undan keyin ixtoyoriy haqiqiy sonlar kelsin [0-9.]+,

```python
fayl = open("regifoda.txt", 'r')
for qator in fayl.readlines():
    qator = qator.rstrip()
    lst = re.findall('^X\S*: [0-9.]+', qator)
    if len(lst) > 0:
        print(lst)
```

Konsolda

```commandline
['X-DSPAM-Confidence: 0.8475']
['X-DSPAM-Probability: 0.0000']
['X-DSPAM-Confidence: 0.6178']
['X-DSPAM-Probability: 0.0000']
['X-DSPAM-Confidence: 0.6961']
['X-DSPAM-Probability: 0.0000']
['X-DSPAM-Confidence: 0.7565']
['X-DSPAM-Probability: 0.0000']
['X-DSPAM-Confidence: 0.7626']
```

Yuqoridagi natijadan qanday qilib sonlarni ajratib olish mumkin?

`()` yordamida biz uni ajratib olishimiz mumkin, yani:

```python
fayl = open("regifoda.txt", 'r')
for qator in fayl.readlines():
    qator = qator.rstrip()
    lst = re.findall('^X\S*: ([0-9.]+)', qator)
    if len(lst) > 0:
        print(lst)
```

Konsolda,

```commandline
['0.8475']
['0.0000']
['0.6178']
['0.0000']
['0.6961']
['0.0000']
['0.7565']
['0.0000']
['0.7626']
```


## Maxsus belgilar bilan ishlash `$`
Maxsus belgilar bilan ishlash uchun, \ (backslash) dan foydalanamiz

```python
x = 'We just received $100.00 for cokking.'
lst = re.findall("\$.[0-9.]+", x)
print(lst)
```

Konsolda,

```commandline
['$10.00']
```

Agar, `\`ni olib tashlasangiz natija bo'lmaydi

```python
x = 'We just received $100.00 for cokking.'
lst = re.findall("$.[0-9.]+", x)
print(lst)
```

Konsolda,

```commandline
[]
```

## Mashqlar

 1. Quyidagini ishlating
    ```python
    fayl = open("regifoda.txt", 'r')
    for qator in fayl.readlines():
        qator = qator.rstrip()
        lst = re.findall('^Details: \S*rev=([0-9]+)', qator)
        if len(lst) > 0:
            print(lst)
    ```

 2. Quyidagini ishlating
    ```python
    fayl = open("regifoda.txt", 'r')
    for qator in fayl.readlines():
        qator = qator.rstrip()
        lst = re.findall('^From .* ([0-9][0-9]):', qator)
        if len(lst) > 0:
            print(lst)
    ```














