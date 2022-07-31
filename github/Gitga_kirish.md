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

Avvalo, gitdan foydalanishimiz uchun uni kompyuterimizga yuklab olishimiz(Asosan Git Bushdan foydalanish) yoki darsimiz davomida foydalanadigan `PyCharm`dagi
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
```consule
pwd — sizning fayl sistemadagi joylashgan yo'lingizni ko'rsatadi.
ls — joriy papkadagi barcha fayl va boshqa papkalarning ro'yxatini ko'rsatadi.
cd [ yo'nalish ] — ko'rsatilgan yo'nalishdagi papkaga ko'chadi.
mkdir [ papka-nomi ] — kiritilgan nom bo'yicha papka yaratadi.
```
<h3>Gitda branchlar</h3>
Branchlar bizga faylimizni tayyor bo'lamagunicha ya'ni `main`ga merge qilinmaguncha saqlash imkoni beradi.

<p>
    <img src=".\images\git_3.png">
</p>

<h3>Global name</h3>
```console
PS D:\ochiqai\python> git --version
git version 2.36.1.windows.1
```

```consule
git config global user.name "Mukhriddin.B"
git config glaobal user.email "Mukhriddin@gmail.com"
git config --list
```
### Tayanch tushunchalar
<ul>
<li>git add "fayl nomi" - faylni yuklash uchun ishlatiladi</li>
<li>git status - o'zgarishlarni tekshirish</li>
<li>git checkout -b "yangi branch nomi" - yangi branch hosil qilish uchun</li>
<li>git commit -m - faylni saqlash uchun</li>
<li>git push - githubga joylashtirish uchun</li>
</ul>