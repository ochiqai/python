## Gitga kirish

* [Git nima](#git-nima)
* [Gitga ulanish va asosiy buyruqlar](#gitga-ulanish-va-asosiy-buyruqlar)
* [Tayanch tushunchalar](#tayanch-tushunchalar)


### Git nima

<p>
    <img src=".\images\Git_1.png">
</p>

Git bu - fayllarni saqlashga, o'zgartirishga imkon beruvchu tizim hisoblanadi. Git bilan birgalikda bir
qancha developerlar bir vaqting o'zida ishlash imkon beradi. Git orqali juda ko'plab parallel branchlar hosil qilib 
ishlash imkoniyatini yaratadi.

<h3>Gitning asosiy qismlari</h3>
<ul>
<li>tarix</li>
<li>tekin va ochiq manbalar</li>
<li>non-liner developmentga yordam berish</li>
<li>backup yaratish</li>
<li>kuchli kompyuter tizimi bilan bog'lanish imkoniyati</li>
<li>developerlar bilan fikr almashish imkoniyati</li>
<li>branch yaratish osonligi</li>
<li>loyhalarning taqsimlanishi</li>
</ul>
<p>
    <img src=".\images\git_2.png">
</p>

### Gitga ulanish va asosiy buyruqlar

Avvalo, gitdan foydalanishimiz uchun uni kompyuterimizga yuklab olishimiz yoki darsimiz davomida foydalanadigan `PyCharm`dagi
terminaldan foydalansak ham bo'ladi. Biz asosiy buyruqlarni `PyCharm` terminalida ko'rib o'tamiz.

<h3>Gitning asosiy buyruqlari</h3>

<table>
  <tr>
    <th>Repositor yaratish</th>
    <th>O'zgarishlar qilish</th>
    <th>Branchlar bilan ishlash</th>
    <th>Sync o'zgarishlar</th>
  </tr>
  <tr>
    <td>git init</td>
    <td>git add file_name</td>
    <td>git branch</td>
    <td>git push</td>
  </tr>
     <tr>
    <td></td>
    <td>git commit -m" "</td>
    <td>git checkout branch_name</td>
    <td>git pull</td>
    </tr>
     <tr>
    <td></td>
    <td>git status</td>
    <td>git merge</td>
    <td>git add origin</td>
    </tr>
     <tr>
    <td></td>
    <td>git rm</td>
    <td>git branch -d branch_name</td>
    <td></td>
  </tr>
</table>
 * buyruqlar yozilayotganda doim ajratilib yoziladi. Misol uchun `git --version`

<h3>Oddiy Git Bash buyruqlari</h3>
Quydagi link orqali olish mumkin(https://github.com/ochiqai/python/blob/main/terminal/terminal_windows.md)
```consule
pwd — sizning fayl sistemadagi joylashgan yo'lingizni ko'rsatadi.
qolgani yuqoridagi linkda
```
<h3>Gitda branchlar</h3>
Branchlar bizga faylimizni tayyor bo'lamagunicha ya'ni `main`ga merge qilinmaguncha saqlash imkoni beradi.

<p>
    <img src=".\images\git_branch.png">
</p>

<h3>Global name</h3>
```console
PS D:\ochiqai\python> git --version
git version 2.36.1.windows.1
```
`git log`(agar bir qatorda chiqarmoqchi bo'lsangiz `git log --oneline`) orqali biz git o'zgarishlarni, commitlarni qachin amalga oshirgan ekanligimiz ko'rib borish imkoniga ega bo'lamiz.
Bu misolda qachon commit qoldirgan ekanligimizni ko'rish mumkin. `HEAD` - bu git hozir qayerda turgaligini
ko'ratish uchun
```console
PS D:\ochiqai\python\github> git log
commit b59525983f4bd08f80f4a8c34dd3391febf31827 (HEAD -> github, origin/github) 
Author: Mukhriddinoff <muxboysariyev231999@mail.ru>                             
Date:   Sun Jul 31 19:03:55 2022 +0500                                          
                                                                                
    gitga kirish yuklandi                                                       
                                                                                
commit 1d712359ee9cda25385f167fc4d69752e16cb665                                 
Author: Mukhriddinoff <muxboysariyev231999@mail.ru>                             
Date:   Sun Jul 31 10:28:06 2022 +0500                                          
                                                                                
    O'zgarishlar kiritildi                                                      
                                                                                
commit e6d29329c1a538a9ee3d63a86ecc825122137c42                                 
Author: Mukhriddinoff <muxboysariyev231999@mail.ru>
Date:   Fri Jul 29 12:27:58 2022 +0500

    Rasmlar qo'shildi

```
`git log --oneline --graph` orqali o'zgarishlar qulayroq ko'rinadi.
```console
* b595259 (HEAD -> github, origin/github) gitga kirish yuklandi
* 1d71235 O'zgarishlar kiritildi
* e6d2932 Rasmlar qo'shildi
* 16a3326 PRdan keyingi holat yuklandi
* 1e4ef42 Xatolar tuzatildi
* 6f936ee Qo'shimchalar kiritildi
* 3348f16 Rasmlar qayta nomlandi
* 99f8e99 Xatolar to'g'irlandi va o'zgarishlar kiritildi
* a93b57e pr md yozildi
* 197788a Pr yozildi
* 4743db9 pr qilish uchun
* 2f0178b github
```
`git log --oneline --graph --decorate --all` ham qulaylashtiradi
```console
PS D:\ochiqai\python\github> git log --oneline --graph --decorate --all
* b595259 (HEAD -> github, origin/github) gitga kirish yuklandi 
* 1d71235 O'zgarishlar kiritildi
* e6d2932 Rasmlar qo'shildi
* 16a3326 PRdan keyingi holat yuklandi
| * a293dd6 (origin/git, git) Xatolar tugirlandi
| * 32b6478 O'zgarishlar kiritildi
| * 0274191 Yangi dars qo'shildi
|/
| *   0ed90a1 (origin/main, origin/HEAD, main) Merge pull request #36 from ochiqai/github 
| |\
| |/
|/|

```

```consule
git config global user.name "Mukhriddin.B"
git config glaobal user.email "Mukhriddin@gmail.com"
git config --list
```

Biz gitda `mkdir fayl_nomi` buyrug'i orqali folder hosil qilamiz. O'sha folderga borib `ls` buyrug'ini berganimizda
bo'sh narsani qaytaradi. Uning ichiq biror bir fayl yaritib olishimiz ucgun esa `git init`dan foydalanamiz. Bu akbi fayl 
yashirin fayl deb ataladi.
```console
PS D:\ochiqai\darslar> ls
PS D:\ochiqai\darslar> git init
Reinitialized existing Git repository in D:/ochiqai/darslar/.git/
PS D:\ochiqai\darslar>  
```
<p>
    <img src=".\images\git_4.png">
</p>

Bundan tashqari bizga git fayllarimizni saqlashga imkon yaratadi. Misol uchun siz 1 - oyga mo'ljallagan loyiha
ustida ishlamoqdasiz, siz uni 30 kunga taqsimlab yozib borasiz, gitda saqlab qoyasiz. Har bir kuni yozib borib saqlab qo'ya olasiz.
pastdagi buyruqlar orqali biz ularni har kunlik qo'shib borishni amalga oshiramiz.
`git log` berish orqali qilayotgan o'zgarishlarni ko'rib borasiz. `git restore --staged loyiha.txt` qilsak faylimizni saqlamasdan
ortga qaytaradi.
```console
PS D:\ochiqai\darslar> ls
    Каталог: D:\ochiqai\darslar
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       03.08.2022     10:11              0 loyiha.txt
PS D:\ochiqai\darslar> git add loyiha.txt
PS D:\ochiqai\darslar> git status -o'zgarishlarni tekshrish uchun
PS D:\ochiqai\darslar> git commit -m"loyiha saqlandi"
```
Biror bir faylni oldingiz holati bilan solishtirish uchun `git diff` buyrug'idan foydalanamiz.
```console
PS D:\ochiqai\python\github> git diff Gitga_kirish.md
diff --git a/github/Gitga_kirish.md b/github/Gitga_kirish.md 
index d9f8f86..52c295f 100644
--- a/github/Gitga_kirish.md
+++ b/github/Gitga_kirish.md
```
>2 - darsimiz githubga kirish

### Tayanch tushunchalar
<ul>
<li>git - fayllarni saqlovchi tizim </li>
<li>branch - fayllarni vaqtincha saqlovchi</li>
<li>git log - fayldagi o'zagrishlarni kuzatishga yordam beradi</li>
</ul>
