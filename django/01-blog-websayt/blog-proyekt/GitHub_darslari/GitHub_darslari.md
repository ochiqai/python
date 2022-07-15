## GitHub darslari
<p align="center">
    <img src=".\GitHub_images\GitHub.png">
</p>

* [GitHubga kirish](#githubga kirish)
* [GitHubga fayl joylashtirish](#githubga fayl joylashtirish)
* [Tayanch tushunchalar](#tayanch tushunchalar)

### GitHubga kirish

* GitHub bu shunday xizmatki - bu Git repozitoriylarini boshqarishga imkon beradigan 
bulutga asoslangan hosting xizmati.
Repozitoriylar bu yerda joylashgan barcha kod fayllarini o'z ichiga olgan papkaga o'xshaydi. GitHub dasturidan barcha dasturchilar keng foydalanib kelishadi.
Ular bu yerda o'zi yaratgan `code`larini `sharing` qilishadi va yangidan yangi g'oyalr olishlari mumkin bo'ladi.
Hop bu darsimi davomida `GitHub` ga qanday qilib biror - bir faylni yuklashni va bir qancha asosiy `kamandalarni` ko'rib chiqamiz. 

>>> So, Let's go bro...💪💪💪

### GitHubga fayl joshlashtirish 

* Hop, Githubga fayl jolashtirishdan oldin, biz bunga imkon beruvchi buyruqlani ko'rib chiqishimiz kerak bo'ladi.
Darsimiz davomida biz fayllarni `PyCharm` dasturi yordamida `md` fayl shaklida joshlashtirib boramiz.
Shuning uchun ham `GitHub`dan ro'yxatdan o'tish va boshqarish buyruqlarini `PyCharm`dagi terminalda ko'rib chiqamiz.

* Dastlab oddiy buyruqlarni ko'rib chiqamiz....

* Bular ☟

```console
pwd — sizning fayl sistemadagi joylashgan yo'lingizni ko'rsatadi.

ls — joriy papkadagi barcha fayl va boshqa papkalarning ro'yxatini ko'rsatadi.

cd [ yo'nalish ] — ko'rsatilgan yo'nalishdagi papkaga ko'chadi.

mkdir [ papka-nomi ] — kiritilgan nom bo'yicha papka yaratadi.
```

* Git buyruqalri esa...

* Bular

```console
git init
git status
git add
git commit -m " "
git push 
```

>>>keep going!!!🔥

* Hop, dastlab biz githubdan ro'yxatdan o'tib olishimiz kerak. Chunki hali bizni Git tanimaydi😂.
Shuning uchun ham biz terminalga o'tib `git init`ni kiritib olamiz. `git` buyrug'idan keyin har doim
bo'sh joy qoldirishni qoldirish kerak.Shundan so'ng bu buyruqni kiritamiz.
```console
git config --global user.name "<sizning_ismingiz_shu_yerda>"
```
* Shundan so'ng email ham kiritib olamiz.
```console
git config --global user.email "<emailingiz@email.com>"
```

* Endi kompyuter `GitHub` uchun tayyor!!!


* Endigi qadamda GitHubga fayllarni joylashtirishni ko'rib chiqamiz. To'g'ridan - to'g'ri fayllarni joylashtirishdan oldin qaysi
`branch`da turganimizni yoki yangi branch yaratib olishni ko'rib chiqamiz. Biz terminalda 
`git branch` kirtamiz.
```console
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt\GitHub_darslari> git branch
  03templates
  django_admin
  main
* terminal             `*` bu belgi - qaysi branchda ekanligimizni ko'rsatadi.
```

* Agar yangi branch hosil qilishni istasak `git checkout -b [name]` kiritib olamiz.
Kiritilgan yangi branch o'chirish uchun esa `git branch -d [branch name]` kiritib olamiz.
```console
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt\GitHub_darslari> git checkout -b GitHub
Switched to a new branch 'GitHub' --- bu yerda yangi branch yaratildi. 
```
* Tassavur qilaylik🤔 sizda `my_work` deb nomlangan folder mavjud. Uning ichida esa, `my_project` deb nomlangan fayl bor.
Shuni biz GitHubga joylamoqchimiz. Hop, dast avval, `git init` kiritib my_work folderni kiritib olamiz. 
O'sha papkadagi barcha fayllarni joylash uchun esa, `git add .` dan foydalanamiz.

```console
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt\my_work> git add .
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt\my_work> git commit -m"my_project"
[terminal abcdac3] my_project
 3 files changed, 1 insertion(+)
 create mode 100644 django/01-blog-websayt/blog-proyekt/GitHub_darslari/GitHub_darslari.md
 create mode 100644 django/01-blog-websayt/blog-proyekt/GitHub_darslari/GitHub_images/GitHub.png
 create mode 100644 django/01-blog-websayt/blog-proyekt/my_work/my_project.md
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt\my_work> git push
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (11/11), 298.66 KiB | 4.67 MiB/s, done.
Total 11 (delta 3), reused 1 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/ochiqai/python.git
   7f7c250..abcdac3  terminal -> terminal
```

* `my_project` fayli GitHubga o'rnatildi.

<p align="center">
    <img src=".\GitHub_images\GitHubga_fayl_yuklash.png">
</p>

>>> We have almost done!!!


### Tayanch tushunchalar 

<ul>
    <li>git init - barcha fayllarni joylashtirish uchun</li>
    <li>git add . - faylni yuklash uchun</li>
    <li>git commit -m"something" - commit qoldirish uchun</li>
    <li>git branch - qaysi branch turganlikni ko'rsatadi.</li>
    <li>git checkout -b - yangi branch hosil qilish uchun.(yoki git branch [name] ham qilsa bo'ladi.)</li>
    <li>git branch -d - branchni o'chirish uchun ishlatiladi.</li>
    <li>git rm - faylni o'chirishga xizmat qiladi</li>
    <li>git mv [file-original][file-renamed] - fayl nomini o'zgartirish uchun</li>
</ul>

