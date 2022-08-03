## Githubga fayl yuklash

* [Github nima](#github-nima)
* [Githubga fayl joylashtirish](#githubga-fayl-joylashtirish)
* [Yangi repo hosil qilish](#yangi-repo-hosil-qilish)
* [Tayanch tushunchalar](#tayanch-tushunchalar)


### Github nima
Github - shunday xizmatki - bu Git repozitoriylarini boshqarishga imkon beradigan 
bulutga asoslangan hosting xizmati.
Repozitoriylar bu yerda joylashgan barcha kod fayllarini o'z ichiga olgan papkaga o'xshaydi. GitHub dasturidan barcha dasturchilar keng foydalanib kelishadi.
Ular bu yerda o'zi yaratgan `code`larini `sharing` qilishadi va yangidan yangi g'oyalar olishlari mumkin bo'ladi.

<p>
    <img src=".\images\github_1.png">
</p> 

### Githubga fayl joylashtirish

Githubga fayl joylashtirish uchun bir qancha git buyruqlarini ko'rib chiqamiz. Birinchi navbatda biz faylni yuklashdan oldin
branch tekshirib olamiz. Branch yaratib olish uchun `git branch fayl_nomi` yoki `git checkout fayl_nomi`
kiritamiz.
```console
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt\GitHub_darslari> git branch
  03templates
  django_admin
  main
* terminal             `*` bu belgi - qaysi branchda ekanligimizni ko'rsatadi.
```
Agar yangi branch hosil qilishni istasak `git checkout -b [name]` kiritib olamiz.
Kiritilgan yangi branch o'chirish uchun esa `git branch -d [branch name]` kiritib olamiz.
```console
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt\GitHub_darslari> git checkout -b GitHub
Switched to a new branch 'GitHub' --- bu yerda yangi branch yaratildi.
```
<table>
  <tr>
    <th>github buyruqlari</th>
    <th>branch bilan ishlash</th>
  </tr>
  <tr>
    <td>git branch</td>
    <td>branchni tekshirish</td>
  </tr>
  <tr>
    <td>git checkout -b [name]</td>
    <td>branchni yaratish</td>
  </tr>
  <tr>
    <td>git branch -d</td>
    <td>branchni o'chirish</td>
  </tr>
</table>

Tassavur qilaylik🤔 sizda `my_work` deb nomlangan folder mavjud. Uning ichida esa, `my_project` deb nomlangan fayl bor.
Shuni biz GitHubga joylamoqchimiz. Hop, dast avval, `git init` kiritib my_work folderni kiritib olamiz. 
O'sha papkadagi barcha fayllarni joylash uchun esa, `git add .` dan foydalanamiz.

<p>
    <img src=".\images\github_2.png">
</p>

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
    <img src=".\images\GitHubga_fayl_yuklash.png">
</p>

### Yangi repo hosil qilish

Sizning repozitoriyingiz bu loyiha maydoningiz. U yerda siz papkalarni, barcha turdagi fayllar — rasmlar,
videolar, ma'lumotlar yig'ilmasi va boshqa barcha loyihangizga kerakli bo'lgan narsalarni saqlashingiz mumkin.
Git bilan ishlashdan oldin, siz loyihangiz uchun yangi repozitoriy ochishingiz kerak bo'ladi. Siz buni Githubning
veb-saytidan qilishingiz mumkin.
Repozitoriyingizda README faylini ochish juda yaxshi fikr, u yerda siz loyihangiz haqida ma'lumot yozib
qoldirishingiz mumkin. Siz bu faylni checkbox ustiga bosish orqali yaratishingiz mumkin (rasmga e'tibor bering).
<ul>
    <li>GitHub ning sayting o'ting, tepada o'ngda + belgisini bosing va "New repository" tugmasini bosing.
</li>
    <li>Repozitoriy nomini kiriting va u haqida kichik ma'lumot kiriting.
</li>
    <li>Bu repozitoriy ochiq yoki yopiq bo'lishi kerakligini hal qiling.
</li>
    <li>"Initialize this repository with a README" tugmasini README fayl ochmoqchi bo'lsangiz bosing. (Men
sizlarga bu faylni yaratishni juda maslahat beraman. Chunki barcha kirgan odamlar birinchi navbatda shu
faylni ko'zdan kechirishadi.)</li>
</ul>

<p>
    <img src=".\images\github_repo.png">
</p>
Paydo bo'lgan oynadan bo'sh joylani to'ldiramiz.

<ul>
    <li>Repository name - nom kiritamiz(misol uchun: git)
</li>
    <li>description - maqsadimizni yozib olamiz.(misol uchun: git bilan ishlash)
</li>
    <li>public yoki private - bunda ikkisidan birini tanlaymiz. Public - dunyo ko'rish uchun, private - shaxsiy foydalanish uchun
</li>
    <li>README.md faylni ham kiritib olamiz.
</li>
    <li>add gitingnore - bunda biz bazi faylllarni githubda userlarga ko'rsatmaslik uchun
</li>
    <li>choose a license - ma'lumotlarni foydalanuvchilar uchun qanday shaklda ko'rishi(misol uchun: hammaga ochiq holatda)
</li>
</ul>
<p>
    <img src=".\images\github_repo_1.png">
</p>

Yaratib olganimizdan so'ng quyidagi oyna hosil bo'ladi.
<p>
    <img src=".\images\github_repo_2.png">
</p>
Bu yerda githubga fayl joylashtirish uchun kerakli buyruq `code`lari berilgan
git remote add origin https://github.com/Mukhriddinoff/my_project.git
git branch -M main
git push -u origin main
Yuqoridagi buyruqlar orqali `repo`ni push qilsa bo'ladi.

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

