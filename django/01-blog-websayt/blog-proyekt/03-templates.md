## Django Templates 

#### Kirish

Avvalgi darsimizda biror matnni foydalanuvchiga ko'rinadigan qilib ko'rgandik. 
Bunda biz funksiya yordamida amalga oshirgan edik. 
Keyinchalik darsturimiz kattalashib ketgach, biz ko'plab kod yozishimizga to'g'ri keladi.
Bu amallarni funksiya yordamida bajarsak, kodlarimiz tushunarsiz va tabtibsiz bo'lib qoladi. 
Bu kabi muammolar bo'lmasligi uchun biz `templates`lardan foydalanamiz.


#### Templates yaratish jarayoni.

* 03-kunda biz `blog` nomli app yaratib olgandik. `blog` nomli papkamizdan, templatelar uchun  yangi `templates` nomli papka yaratib olamiz.
* Yaratgan `templates` nomli papkamiz ichidan `blog` appimizga tegishli yangi `blog` nomli papka yaratib olamiz.

<p align="center">
    <img src="./image/templates_folder.png">
</p>

`blog` appimizga tegishli barcha `templates`larni shu yerda bajaramiz.

* Foydalanuchiga asosiy sahifada ko'rinadigan `Blog home!` matnini ko'rsatish jarayonini ko'rib chiqamiz. Buning uchun yangi `home.html` faylini yaratib olamiz. (templates papka ichidagi blog papkasi ichidan) 
* `home.html` fayli ichida quyidagi ishni amalga oshiramiz.
```
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <h1>Blog home!</h1>
</body>
</html>
```
* `blog` nomli appimiz ichidagi `apps.py` nomli faylidan class nomidan nusxa olib, `django_project` loyihamiz ichidagi `settings.py` ga `INSTALLED_APPS` qismiga quyidagicha appimizni qo'shib qo'yamiz. 

```console
INSTALLED_APPS = [
    'blog.apps.BlogConfig', <--- [shu qatorni qo'shib qo'yamiz.]
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

* Yaratgan applarimizni shu yerda qo'shib ketishimiz kerak. Bu yerdan biz yaratgan appimizga bog'lanib, ma'lumotlarni uzatadi.

* Endi `blog` papka ichidagini `views.py` fayliga borib quyidagi ishni amalga oshiramiz.

```python
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"blog/home.html")
```

Qachonki funksiyani chaqirganimizda `render` orqali `blog` papka ichidagi `home.html`dagi ma'lumotlarni foydalanuvchiga qartaradi.
* Terminalga borib `python manage.py runserver` komandasi orqali serverni ishlatib ko'ramiz.

<p align="center">
    <img src="./image/blog_home.png">
</p>

`home.html` joylaygan papkadan `about.html` nomli yangi fayl hosil qilib olamiz.

`about.html` ga borib quyidagi ishni bajaramiz.
Ya'ni `About Page` so'zini chiqarib ko'ramiz.
```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>

    <h1>About Page</h1>

</body>
</html>
```

* `about.html` ni ham `home.html` kabi `blog` appimiz ichidagi `views.py` ga borib quyidagi ishni amalga oshiramiz.

```python
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"blog/home.html")

def about(request):
    return render(request,"blog/about.html")
```

* `http://127.0.0.1:8000/` manzilimizdan so'ng `about` so'zini yozib ishlatsak, quyidagicha oyna hosil bo'ladi.

<p align="center">
    <img src="./image/about_page.png">
</p>

* `views.py` quyidagicha xabar yozamiz.

```python
xabarlar = [
    {
        'muallif': 'Ulugbek',
        'sarlavha': 'Toshkent haqida',
        'matn': 'Toshkent Uzbekistanni poytaxti',
        'sana': 'may 28, 2022'
    },
    {
        'muallif': 'Orif',
        'sarlavha': 'Samarkand haqida',
        'matn': 'Samarkand Uzbekistanni shaharchasi',
        'sana': 'may 29, 2022'
    }
]
```

`home` nomli funksiyaga quyidagicha o'zgartisihlar kiritamiz.

```python
def home(request):
    context = {
        "xabarlar":xabarlar
    }
    return render(request,"blog/home.html",context)
```

`home.html` ga quyidagi ishni bajaramiz.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
        {% for xabar in xabarlar %}
            <h1>{{ xabar.sarlavha}}</h1>
        {% endfor %}
        <h1>Blog home</h1>
</body>
</html>
```
`{% %}` bu belgilarning o'rtasida biz python kodlarini yozishimiz kerak. 
Serverni ishlatib ko'rsak quyidagi oyna hosil bo'ladi.


<p align="center">
    <img src="./image/post.png">
</p>

`Title`ga sarlavha yozishni ko'ramiz.
Quyidagi ishlarni bajarsangiz `title` o'zgarganini ko'rasiz.
* `home.html` ga quyidagicha yozamiz.


```html
<!DOCTYPE html>
<html>
<head>
        {% if title %}
        <title>django-blog/{{title}}</title>
        {% else %}
            <title>django-blog/</title>
        {% endif %}
</head>
<body>
        {% for xabar in xabarlar %}
            <h1>{{ xabar.sarlavha}}</h1>
        {% endfor %}
        <h1>Blog home</h1>
</body>
</html>
```

* `about.html` ga quyidagicha yozamiz.

```html
<!DOCTYPE html>
<html>
<head>
        {% if title %}
        <title>django-blog/{{title}}</title>
        {% else %}
            <title>django-blog/</title>
        {% endif %}
</head>
<body>
        <h1>About home</h1>
</body>
</html>
```

`views.py`dan `about` funksiyaga boramiz va `title` ga `ochiqai` deb argument beramiz.
```python
def about(request):
    return render(request,"blog/about.html",{'title':" ochiqai"})
```

<p align="center">
    <img src="./image/home_title.png">
</p>

<p align="center">
    <img src="./image/title_about.png">
</p>

E'tibor bersangiz `title` qismimizning sarlavhasini o'zgartirdik.

* Ba'zida  `html`kengaytmali fayllar yaratganimizda bir xil kodlarni qayta qayta yozishizga to'g'ri keladi. Endi biz buning osonroq yo'lini ko'ramiz.
Buning uchun birinchi `templates` ichidagi `blog` faylidan `base.html` nomli yangi html kengaytmali fayl yaratib olamiz.

* `base.html` ga quyidagicha ishni amalga oshiramiz.

```html
<!DOCTYPE html>
<html>
<head>
    {% if title %}
        <title>django-blog/{{title}}</title>
    {% else %}
        <title>django-blog/</title>
    {% endif %}
</head>
<body>
{% block content %}

{% endblock content %}

</body>
</html>
```

`home.html` dan `base.html` ga o'xshash qismlarini olib tashlaymiz va quyidagicha o'zgartirishlar qilamiz.

```python
{% extends 'blog/base.html' %}

{% block content %}
    {% for xabar in xabarlar %}
        <h1>{{ xabar.sarlavha}}</h1>
    {% endfor %}
    <h1>Blog home</h1>
{% endblock content %}
```
`extends` funksiyadan foydalanib `base.html` chaqirgan holda kodlarimizni osonroq ko'rinishga keltiramiz.

* `about.html` ga ham huddi shu tarzda o'zgartiramiz.

```python
{% extends 'blog/base.html' %}

{% block content %}
    <h1>About home</h1>
{% endblock content %}
```
* Serverni qayta ishlatsangiz avvalgidek ishlayveradi.

<p align="center">
    <img src="./image/home_view.png">
</p>

<p align="center">
    <img src="./image/about_view.png">
</p>

#### Boostrapdan foydalanish.

https://getbootstrap.com/docs/5.2/getting-started/rtl/#starter-template quyidagi manzilga borib, saytimizni chiroyliroq ko'rinishga keltirish uchun ma'lum qismini o'zimizga ko'chirib olamiz.

<p align="center">
    <img src="./image/head_bootstrap.png">
</p>

* Yuqorida ko'rsatilgan qismdan nusxa olib, `base.html` faylimizning `head` qismiga tashlaymiz. `title` dan nusxa olmadik, chunki `base.html`da `title` qismi mavjud.
```html
<head>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.rtl.min.css" integrity="sha384-dc2NSrAXbAkjrdm9IYrX10fQq9SDG6Vjz7nQVKdKcJl3pC+k37e7qJR5MVSCS+wR" crossorigin="anonymous">

    {% if title %}
        <title>django-blog/{{title}}</title>
    {% else %}
        <title>django-blog/</title>
    {% endif %}
</head>
```

* Huddi shunday qilib `body` qismidagi kodlarni `base.html` faylimizning `body` qismiga nusxa olib tashlaymiz.

```html
<body>

    <div class="container">
    {% block content %}  {% endblock content %}
    </div>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
    -->

</body>
```

* `bootstrap` ni ishlatganimizdan so'ng, ko'p o'zgarishlar bo'ladi.

* `body` qismidagi `block content` alohida `div`ga olib `class`ga `container` nomini berib serverimizni ishlatib ko'ramiz.
```python
<div class="container">
{% block content %}  {% endblock content %}
</div>
```
<p align="center">
    <img src="./image/home_bts.png">
</p>

