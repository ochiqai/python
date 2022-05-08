#### Djangoni o'rnatish va ishga tushirish.


1. Terminalga quyidagicha yozish orqali djangoni o'rnatamiz.

    `pip install django`

2. Django versiyasi tekshirish.

    `python -m django --version`
3. Djangoda mavjud bo'lgan buyruqlarni ko'rishni quyidagicha amalga oshiramiz.

<p align="center">
    <img src="./image/django_admin.png">
</p>
<br>
djangoda mavjud kichik buyruqlar
<p align="center">
    <img src="./image/django_buyruqlari.png">
</p>
4. Quyidagi buyruq orqali yangi project yaratamiz.

   `django-admin startproject django_project`
 <br>
bu yerda `django_project` proyektimiz nomi hisoblanadi.
   
<p align="center">
    <img src="./image/django_install.png">
</p>
   
 
   E'tibor bersangiz 02-kun faylimiz ichida `django_project` hosil bo'ldi.

5. Djangoni o'rnatib bo'lgach serverda ishlatib ko'ramiz.
   Birinchi `manage.py` fayli joylashgan papkaga `cd papka_nomi` buyrug'i orqali boramiz. <br>
 

6. Qora ekranga quyidagicha yozamiz.
`python manage.py runserver` <br>


<p align="center">
<img src="./image/project_url.png">
</p>

`http://127.0.0.1:8000/` quyidagi manzilni internetda ishlatib ko'ramiz.

<p align="center">
   <img src="./image/django_working.png">
</p>
