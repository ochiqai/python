 ## PRdan keyingi holat

* [Kommentariyada sharh qoldirish](#kommentariyada-sharh-qoldirish)
* [Md faylga qo'shimchalar kiritish](#md-faylga-qo'shimchalar-kiritish)
* [Tayanch tushunchalar](#tayanch-tushunchalar)

<p>
    <img src=".\images\GitHub_tag.png">
</p>

### Kommentariyada sharh qoldirish

* Faylni GitHubda PR(pull request) qilganimizdan so'ng, uningustida bir qancha ishlar olib borsak bo'ladi.
Bunda yuklangan faylni user(foydalanuvchilar) tomonidan o'z fikrlarini yoki fayldagi kamchilik - xatolarni
ko'rsatishi mumkin bo'lishadi. Bunday holatda biz faylga komment qoldirish orqali yuqoridagi amallarni bajarrish imkoniga ega bo'lamiz.
Dastlabgi qadamda `pull request`ga borib olib PR qilingan fayl ichiga kirib olamiz.

<p>
    <img src=".\images\img.png">
</p>

* Shundan so'ng `Commits` borib, fayl ichiki qismiga kirib olamiz.

<p>
    <img src=".\images\img_1.png">
</p>

* Birinchi navbatda yuklangan faylni to'liqligicha o'qib chiqamiz va agar bior nuqtasi tushunarsiz yoki o'z fikrmizni bildirishimiz uchun komment qoldirishimiz ham mumkin bo'ladi.
Bunda fayl ichida `+` qismini bosamiz va komment uchun joy ochiladi. U yerda biz o'z fikrlarimizni qoldirib
`Start a review` tugmasini bosamiz. 

<p>
    <img src=".\images\img_2.png">
</p>

* Keyingi qadamda esa, `Conversation` qismiga o'tib o'z kommentimiz va boshqa userlar qoldirgan kommentlarini ko'rishimiz mumkin bo'ladi.

<p>
    <img src=".\images\img_3.png">
</p>

### Md faylga qo'shimchalar kiritish

>>> Biz qanday qilib githubda yuklangan md faylda o'zgarishlar kiritishimiz mumkin ?........

* Hop unda biz avvalo `Conversation` qismidagi kommentlarga javob qayatamiz va md faylni `PyCharm`da qo'shimchalarni kiritamiz.
<p>
    <img src=".\images\img_4.png">
</p>

* Bu kabi o'zgarishlarni amalga oshirish uchun, `PyCharm`ga qaytib md faylga o'zgarishlar kiritamiz.
Misol uchun 1 - kommentda 52 - qatordagi va 2 - kommentda esa 71 - qatordagi so'zlarni olib tashlash maslahat berildi.
Buning uchun `PyCharm`ga qaytib, o'sha md fayl ochib olamiz. (Bundan sal oldinroq, hozir siz qaysi branchda ekanligi tekshirib olishingizni maslahat beramiz!!)
52 - va 71 qatorlardagi so'zlarni o'chirib tashlaymiz. O'zgarishlar kiritib bo'lgandan so'ng esa, avvalgiday md faylni
githubga yuklash buyruqlarini bajarib olamiz.

```consule
1 - git add "fayl_nomi"
2 - git status - o'zgarishlarni tekshirish uchun
3 - git commit -m"o'zgarishlar haqida qisqacha sharh"
4 - git push - githubga yuklash uchun
```
* Bu kabi buyruqlarni bajarganimidan so'ng, kommentda shunday o'zgarish bo'ladi. Komment yuqorisidagi
`Outdated` bo'lishi kommentga o'zgarish kiritilgani bildiradi.

<p>
    <img src=".\images\PR_komment.png">
</p>

### Tayanch tushunchalar
<ul>
    <li>PR - pull request</li>
    <li>Commits - userlar uchun sharh qoldirish</li>
</ul>


