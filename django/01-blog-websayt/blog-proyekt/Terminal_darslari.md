## Terminalga kirish

 * [Terminal tushunchasi](#terminal tushunchasi)
 * [Terminalni ishga tushurish](#terminalni ishga tushurish)
 * [Terminaldagi asosiy buyruqlar](#terminaldagi asosiy buyruqlar)
 * [Tayanch tushunchalar](#tayanch tushunchalar)

### Terminal tushunchasi
* Terminal bu - `yozuv` ko'rinishdagi `interface` bo'lib, unda kompyuterni boshqarishga imkon yaratadi. Bu kabi terminallardan eng mashhurlari 'Linux terminal', 'Apple'dagi `Bash and Z shell` va 'Windows' opiratsion tizimida esa `PowerShell interface` dan foydalanib kelinmoqda. Biz darsmiz davomida terminal buyruqlarini `PyCharm` dasturidagi terminaldan foydalanamiz.

### Terminalni ishga tushurish
* Terminalni ishga tushurushda biz avvalo kompyuter qaysi operatsion sistemada ekanligi e'tibor qaratib olmamiz. Agar `Windows` bo'lsa, `pusk` tugmasi orqali `Windows PowerShell`qidirib topib olamiz va ishga tushuramiz.

<p align="center">
    <img src="D:\ochiqai\python\django\01-blog-websayt\blog-proyekt\image\PowerShell.png">
</p>

### Terminaldagi asosiy buyruqlar

* Terminaldagi asosiy buyruqlardan bir - birma ko'rib chiqamiz. 

```
PS C:\Users\user> ... Buyruqlarni shu yerdan yozib boshlaymiz.
```

* Terminalda joylashgan joriy katalogning ichiki fayllarni ko'rish uchun `ls` buyrug'ini kiritamiz.`ls -a` barcha fayllarni chiqarish hizmat qiladi.
```Terminal
PS C:\Users\user\Terminal_darslari> ls
    Каталог: C:\Users\user\Terminal_darslari
Mode                LastWriteTime         Length Name                                                                                      
----                -------------         ------ ----                                                                                      
-a----       06.01.2020     19:32          59310 photo.jpg                                                                                 
-a----       06.01.2020     19:27          56536 photo_2020-01-06_19-27-12.jpg                                                             
-a----       06.01.2020     19:28          29399 photo_2020-01-06_19-28-07.jpg                                                             
-a----       06.01.2020     19:30          38287 photo_2020-01-06_19-30-12.jpg                                                             
-a----       06.01.2020     19:31         157378 photo_2020-01-06_19-31-38.jpg               
```
* Terminaldan biz qaysi yo'nalishda ekanligimizni aniqlab olishimiz uchun esa, `pwd` buyrug'ni kirtamiz.

```Terminal
Path                           
----                           
C:\Users\user\Terminal_darslari
```

* Terminal ichida folder yaratish uchun `mkdir` buyrug'idan foydalanamiz.

```Terminal
PS C:\Users\user> mkdir Terminal_buyruqlari

    Каталог: C:\Users\user

Mode                LastWriteTime         Length Name                                                                                      
----                -------------         ------ ----                                                                                      
d-----       12.07.2022      8:26                Terminal_buyruqlari                                                                       
```

* Terminalda folderning kirish uchun `cd` buyrug'i va folder nomi kiritiladi, ortga qaytish uchun esa `cd ..` kiritiladi.
```Terminal
PS C:\Users\user> cd .\Terminal_buyruqlari
PS C:\Users\user\Terminal_buyruqlari> cd ..
PS C:\Users\user> 
```
* Folder biror file yaratib olish uchun `New-Item` buyrug'idan foydalanamiz. Agar linux bo'lsangiz `touch` buyrug'idan foydalaning.
```Terminal
PS C:\Users\user\Terminal_buyruqlari> New-Item notes.txt
    Каталог: C:\Users\user\Terminal_buyruqlari
Mode                LastWriteTime         Length Name                                                                                      
----                -------------         ------ ----                                                                                      
-a----       12.07.2022      8:42              0 notes.txt 
```

* Yaratagan faylmizni o'chirib tashlash uchun `rm` buyrug'idan foydalanamiz. Papkalarni o'chirish uchun esa `rm -fd` buyruqni ishlatamiz.
```
PS C:\Users\user\Terminal_buyruqlari> rm notes.txt
```

* Terminalda `echo` buyrug'i kiritgan yozuvlaringizni ekanranga chiqaradi. Agar bu yozuvlarmizni biror - bir faylga ko'chirish uchun esa yozuvdan keyin `>` belgi va fayl nomini kirtamiz. Ikkinchi qator uchun esa `>>` va fayl nomini kiritamiz. 
```Terminal
PS C:\Users\user\Terminal_buyruqlari> echo salom
salom
PS C:\Users\user\Terminal_buyruqlari> echo "Salom, bugun biz django darslarni boshlaymiz" > notes.txt

PS C:\Users\user\Terminal_buyruqlari> cat notes.txt
Salom, bugun biz django darslarni boshlaymiz

PS C:\Users\user\Terminal_buyruqlari> echo "Terminal darslari boshlandi." >> notes.txt

PS C:\Users\user\Terminal_buyruqlari> cat notes.txt
Salom, bugun biz django darslarni boshlaymiz
Terminal darslari boshlandi.
```

* Bundan tashqari terminalda `whoami` buyrug'i user name aniqlash uchun ishlatiladi.
```Terminal
PS C:\Users\user\Terminal_buyruqlari> whoami
win-9ci2c94pjr8\user
```

* Terminalda faylni ishga tushurish uchun `start` yoki `invoke-item` foydalanamiz. Agar linuxda bo'lsangiz `vim` dan foydalaning.
```Terminal
PS C:\Users\user\Terminal_buyruqlari> start notes.txt
PS C:\Users\user\Terminal_buyruqlari> Invoke-Item notes.txt
```

* Fayl ichida nima bor ekanligini ko'rish uchun esa `cat` buyrug'idan foydalanamiz.
```Terminal
PS C:\Users\user\Terminal_buyruqlari> cat notes.txt
salom
```

* Terminalda yozilgan buyruqlarni yozuviga boshiga borish uchun esa `home` ortga qaytarish uchun esa `end` kiritamiz.

* Terminalda `man` funksiya bo'lib, agar biror - bir buyruq nomidan yozilsa, u haqida to'liqroq ma'lumot beradi.
```Terminal
PS C:\Users\user\Terminal_buyruqlari> man rm

ИМЯ
    Remove-Item
    
СИНТАКСИС
    Remove-Item [-Path] <string[]>  [<CommonParameters>]
    
    Remove-Item  [<CommonParameters>]
    
ПСЕВДОНИМЫ
    ri
    rm
    rmdir
    del
    erase
    rd
```
* Terminalda ikkita faylni farqini aniqlash uchun `diff` dan foydalanamiz.
```Terminal
PS C:\Users\user\Terminal_buyruqlari> diff notes.txt notes.ppt

InputObject SideIndicator
----------- -------------
notes.ppt   =>           
notes.txt   <=    
```

* Terminalda faqat txt faylni chiqarish uchun `ls *.txt` dan foydalanmiz. `*` dan keyin xohlagan fayl turini kirtsak ham bo'ladi. (Misol uchun `ls *.ppt`) 
```Terminal
PS C:\Users\user\Terminal_buyruqlari> ls *.txt

    Каталог: C:\Users\user\Terminal_buyruqlari

Mode                LastWriteTime         Length Name                                                                                      
----                -------------         ------ ----                                                                                      
-a----       12.07.2022      9:55            154 notes.txt    
```

* Terminlda biror - bir faylni nomini o'zgartirish uchun `mv` buyrug'idan foydalanmiz.
```Terminal
PS C:\Users\user\Terminal_buyruqlari> mv notes_one.txt lesson_one.txt
PS C:\Users\user\Terminal_buyruqlari> ls

    Каталог: C:\Users\user\Terminal_buyruqlari

Mode                LastWriteTime         Length Name                                                                                      
----                -------------         ------ ----                                                                                      
d-----       12.07.2022     10:17                lesson_one.txt                                                                            
-a----       12.07.2022      9:09              0 notes.ppt                                                                                 
-a----       12.07.2022      9:55            154 notes.txt
```

* Terminalda biror - bir faylni nusxa ko'chirish uchun `cp` buyrug'idan foydalanamiz.
```Terminal
PS C:\Users\user\Terminal_buyruqlari> cp notes.txt Terminal_darslari/
PS C:\Users\user\Terminal_buyruqlari> cd .\Terminal_darslari
PS C:\Users\user\Terminal_buyruqlari\Terminal_darslari> ls
    Каталог: C:\Users\user\Terminal_buyruqlari\Terminal_darslari
Mode                LastWriteTime         Length Name                                                                                      
----                -------------         ------ ----                                                                                      
-a----       12.07.2022      9:55            154 notes.txt 
```

### Tayanch tushunchalar

<ul>
<li>cd - fayllarni ochish va ortga qaytish uchun</li>
<li>ls - joriy katalog tarkibini ro'yxatlash</li>
<li>mkdir - yangi folder yaratish uchun</li>
<li>rm - faylni o'chirish uchun</li>
<li>echo - Terminalda yozuv amallarini olib borish uchun</li>
<li>whoami - userni aniqlab olish uchun</li>
<li>start - faylni ochish uchun</li>
<li>man - buyruqlar haqida ma'lumot beradi</li>
<li>diff - fayllarni farqini ko'rsatadi</li>
<li>mv - fayl nomini o'zgartirish uchun</li>
</ul>


