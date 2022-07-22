## Githubda Pr qilish

* [Pr nima](#pr nima)
* [Faylni githubda pr qilish](#faylni githubda pr qilish)
* [Tayanch tushunchalar](#tayanch tushunchalar)


### Pr nima

* `Pr` bu - github platformasiga yangi branch orqali biror bir faylni joylashtirish orqali, bu yangi faylni 
boshqa userlarga yangi fayl haqida xabar berish hisoblanadi. Yangi branchda pr bir marotaba qilinadi va 
userlar unga kommentariya orqali xato - kamchiliklarini va o'z fikrlarini bildirishadi. Biz pr qilingan branchlarni
github platformasidagi `pull requests` dan ko'rishimiz mumkin bo'ladi. 

### Faylni githubda pr qilish

* Fayllarni githubda pr qilish uchun githubning maxsus kommandalari orqali `git bush` yoki `PyCharm` terminalidan foydalanamiz.
Hop, dastlabki qadamda biz yangi `branch` hosil qilib olishimiz kerak bo'ladi. Buning uchun biz `PyCharm` terminalidan foydalanamiz. 
Terminalda yangi branch hosil qilish uchun `git checkout -b [yaratmoqchi bo'lgan branch nomi]` kiritamiz.
Barcha branchlarni ko'rish uchun esa `git branch` dan foydalanamiz.
```Console
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt> git checkout -b Pr
Switched to a new branch 'Pr'
```
* Biz o'z faylimizni githubga yuklash uchun esa, `git add <fayl_nomi>` kiritamiz. Bunda faqatgina o'sha fayl
githubga yuklanadi. Agar biz `git add .` qiladigan bo'lsak bo'lsak barcha fayllardagi o'zgarishlar yuklanishi mumkin.
```Console
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt> git add my_work.md
```
Kiritilgan faylimizni tekshirib olishimiz uchun `git status` dan foydalanamiz.
```Consule
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt> git status
On branch Pr
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   my_work.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../../../github/github_pr_qilish.md
```
Faylimizni saqlab qolish uchun esa, `git commit -m`dan foydalanamiz. 

```Consule
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt> git commit -m"Pr qo'shildi"
[Pr 292ff81] Pr qo'shildi
 1 file changed, 1 insertion(+)
 create mode 100644 django/01-blog-websayt/blog-proyekt/my_work.md
```
Faylni githubga birlashtirish uchun esa, `git push`ni kiritamiz.

```Consule
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt> git push
fatal: The current branch Pr has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin Pr

```

Bu yerda `git push --set-upstream origin Pr` buyrug'i paydo bo'ladi. Buning ma'nosi githubga yangi branch 
kiritayotgamizda github buni hali tanimaydi, uni ta'nitish uchun o'sha buyruqni qata kiritamiz.

```Consule
PS D:\ochiqai\python\django\01-blog-websayt\blog-proyekt> git push --set-upstream origin Pr
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 464 bytes | 12.00 KiB/s, done.
Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote:
remote: Create a pull request for 'Pr' on GitHub by visiting:
remote:      https://github.com/ochiqai/python/pull/new/Pr
remote:
To https://github.com/ochiqai/python.git
 * [new branch]      Pr -> Pr
branch 'Pr' set up to track 'origin/Pr'.
```
Bunda bizga yangi branch qo'shilganligi haqida ma'lumot berilmoqda. Keyingi qadamda biz, yuborilgan xabardagi 
birinchi manzilga `remote:      https://github.com/ochiqai/python/pull/new/Pr` boramiz.

Borgan manzilimizda bu ko'rinishdagi oyna hosil bo'ladi.

<p>
    <img src=".\images\Pr.png">
</p>

Yuqorida oynada biz branch bog'lash uchun, komment qoldirishimz va reviewers taggida qaysi userlar bu fayl ko'rish ekanligi belgilaymiz.

<p>
    <img src="D:\ochiqai\python\github\images\Pr_1.png">
</p>

Keyingi qadamda oynadagi  yashil rangdagi `Create pull request` bosamiz.

Keyinchalik biz bu branchni github platformasidagi `pull request`ga borib ko'rishimiz mumkin bo'ladi.

<p>
    <img src="D:\ochiqai\python\github\images\Pr_2.png"> 
</p>

Shundan so'ng biz, fayl haqida o'z fikrlarimizni qoldirish uchun `Commits` borib, matn boshidagi `+` bosamiz, va u yerda 
koment qoldirish uchun joy ochiladi.

<p>
    <img src="D:\ochiqai\python\github\images\Pr_3.png">
</p>

Shunda so'ng biz, `Start a review` bosamiz, komentlarni ko'rish uchun esa ortga qaytamiz. 

<p>
    <img src="D:\ochiqai\python\github\images\Pr_4.png">
</p>

>>> We have finished

### Tayanch tushunchalar

<ul>
<li>git add "fayl nomi" - faylni yuklash uchun ishlatiladi</li>
<li>git status - o'zgarishlarni tekshirish</li>
<li>git chekout -b "yangi branch nomi" - yangi branch hosil qilish uchun</li>
<li>git commit -m - faylni saqlash uchun</li>
<li>git push - githubga joylashtirish uchun</li>
</ul>


