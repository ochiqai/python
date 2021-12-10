#### Main branchdagi xatoni to'g'irlash
Vazifa shundan iboratki biz main branchdan biror xatoni to'g'irlamoqchimiz (yoki main branchga o'zgartirish kiritmoqchimiz). <br>
Buning uchun qanday ishlarni amalga oshiramiz.

1. Yangi branch ochib olamiz. Quyidagi buyruq orqali yangi branch ochiladi va shu branchga o'tadi.  <br>
    ```codeline
    git checkout -b 10-kun_xatosi
    ```
2. Xatoni to'g'irlaymiz.
3. Quyidagi buyruqni bajarib, qilgan o'zgarishimizni ko'rishimiz mumkin.
    ```codeline
    git status 
    ```
4. Quyidagi buyruqni bajarib, o'zgartirganlarimizni branchga qo'shamiz.
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
   
    <img src="https://user-images.githubusercontent.com/85432617/144699521-c63f69e3-170c-45b1-8678-96ef44d9d645.png" width=600>

8. Yuqoridagi manzilga kirganimizdan so'ng, qilgan ishimiz haqida izoh qoldiramiz. Write qismiga qanday tekshirish kerakligi haqida izoh qoldiramiz.

    <img src="https://user-images.githubusercontent.com/85432617/144699595-fc26a7ef-2616-4310-a983-4177d648113a.png" width=600>

9. `Create pull request`  tugmasini bosamiz.

10. `Reviewers` qismiga borib tekshiruvchilarni tanlaymiz.

    <img src="https://user-images.githubusercontent.com/85432617/144699650-de5fc569-a449-4292-875a-f81346b1e469.png" width=600> <br>
    <img src="https://user-images.githubusercontent.com/85432617/144699653-2996a8a4-96ef-47e2-bbbd-2972aa4522ae.png" width=350>

   Xulosa: <br>
   Biz agar main branchdan xato topsak, yangi branch ochib olamizda xatoni to'g'irlab PR yuboramiz. Kegin Reviewerslar tekshiradi, to'g'ri bo'lsa merge qiladi.
   Nafaqat main branch, balki boshqa branchlarga ham shu tarzda ishlarni amalga oshiramiz. 



