#### Main branchdagi xatoni to'g'irlash
Vazifa shundan iboratki biz main branchdan biror xatoni to'girlamoqchimiz (yoki main branchga o'zgartirish kiritmoqchimiz). <br>
Buning uchun qanday ishlarni amalga oshiramiz.

1. Yangi branch ochib olamiz. 
    ```codeline
    git checkout -b 10-kun_xatosi
    ```
   Bu buyruq orqali 10-kun_xatosi nomli yangi branch hosil qilib oldik. <br>
2. Xatoni to'g'irlaymiz.
3. Quyidagi buyruqni bajarib, qilgan o'zgarishimizni ko'rishimiz mumkin.
    ```codeline
    git status 
    ```
4. Quyidagi buyruqni bajarib, qilgan o'zgarishimizni 10-kun_xatosi nomli branchga qo'shamiz.
    ```codeline
    git add --all
    ```
5. Quyiagi buyruqni bajarib, qanday o'zgartirish qilganimiz haqida xabar qoldiramiz.
    ```codeline
    git commit -m"10-kun python kodlari vertikal jihatdan to'g'irlab chiqildi."
    ```
6. `git push` buyrug'i orqali qilgan o'zgartirishimizni git hub ga joylaymiz.
    ```shell
    git push
    ```
7. Biz yangi branchga birinchi marta `git push` qilganimiz sababli quyidagi buyruqdan foydalanishimiz kerak.
    ```shell
    git push --set-upstream origin 10-kun_xatosi
    ```
   `git push` qilib bo'lgandan so'ng, manzil beriladi. 
    ```shell
    https://github.com/ochiqai/python/pull/new/10-kun_xatosi
    ```
   
<img src="1.png" width=600>

8. Yuqoridagi manzilga kirganimizdan so'ng, qilgan ishimiz haqida izoh qoldiramiz. Write qismiga qanday tekshirish kerakligi haqida izoh qoldiramiz.

<img src="2.png" width=600>

9. `Create pull request`  tugmasini bosamiz.

10. `Reviewers` qismiga borib kerakli odamlarni belgilaymiz.

<img src="3.png" width=600> <br>
<img src="4.png" width=600>

   Xulosa: <br>
   Biz agar main branchdan xato topsak, yangi branch ochib olamizda xatoni to'g'irlab PR yuboramiz. Kegin Reviewerslar tekshiradi, to'g'ri bo'lsa merge qiladi.



