## Django Templates 
  * [Nimaga templates](#nimaga-templates)
  * [Templates yaratish jarayoni](#templates-yaratish-jarayoni)
  * [Blogga xabarlar qo'yish](#blogga-xabarlar-qo-yish)
  * [Sayt sarlavhasi bilan ishlash](#sayt-sarlavhasi-bilan-ishlash)
  * [Takrorlanishga qarshi](#takrorlanishga-qarshi)
  * [Blog bosh sahifasini yaxshilash](#blog-bosh-sahifasini-yaxshilash)

### Nimaga templates

Avvalgi darsimizda biror matnni foydalanuvchiga ko'rinadigan qilib ko'rgandik. 
Bunda biz funksiya yordamida amalga oshirgan edik. 
Keyinchalik darsturimiz kattalashib ketgach, biz ko'plab kod yozishimizga to'g'ri keladi.
Bu amallarni funksiya yordamida bajarsak, kodlarimiz tushunarsiz va tartibsiz bo'lib qoladi. 
Bu kabi muammolar bo'lmasligi uchun biz `templates`lardan foydalanamiz.


### Templates yaratish jarayoni

`blog` appini davom ettiramiz. `blog` papkasidan, templatelar uchun  yangi `templates` nomli papka yaratamiz.
Uning ichidan `blog` appimizga tegishli yangi `blog` nomli papka yaratib olamiz. Papka nomi app nomi bilan 
bir xil bo'lishi kerak.

```
django_project      
│   manage.py
└───blog
    │   __init__.py
    │   admin.py
    │   apps.py
    │   models.py
    │   tests.py
    │   views.py
    └───templates
        └───blog

```

`blog` appimizga tegishli barcha `templates`larni shu yerda bajaramiz.

Foydalanuchiga asosiy sahifada ko'rinadigan `Blog home!` matnini ko'rsatish jarayonini ko'rib chiqamiz. 
Buning uchun yangi `home.html` faylini yaratib olamiz. (templates papka ichidagi blog papkasi ichidan) 
`home.html` fayli ichi quyidagicha bo'ladi:

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

`blog` appimiz ichidagi `apps.py` faylidan class nomidan nusxa olib, `django_project` loyihamiz 
ichidagi `settings.py` ga `INSTALLED_APPS` qismiga quyidagicha appimizni qo'shib qo'yamiz. 

```console
# settings.py fayli
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

Yaratgan applarimizni shu yerda qo'shib ketishimiz kerak. Bu yerdan biz yaratgan appimizga bog'lanib, 
ma'lumotlarni uzatadi. Endi `blog` papka ichidagini `views.py` fayliga borib quyidagi ishni amalga oshiramiz.

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "blog/home.html")
```

Qachonki funksiyani chaqirganimizda `render` orqali `blog` papka ichidagi `home.html`dagi ma'lumotlarni 
foydalanuvchiga qaytaradi. Terminalga borib serverni ishlatamiz 

```console
ochiqai@com:~$ python manage.py runserver
```

<p align="center">
    <img src="./image/blog_home.png" width="250">
</p>

Keling yana boshqa fayl yaratamiz `about.html` nomli. 
`home.html` joylaylashgan papkada `about.html` ni hosil qilib olamiz. Unga quyidagi kodni yozamiz:


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

Bunda `About Page` so'zini chiqarayapmiz.

`about.html` ni ham `home.html` kabi `blog` appimiz ichidagi `views.py` ga borib quyidagi ishni amalga oshiramiz:

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")
```

Ishlab turgan serverdan, `http://127.0.0.1:8000/` dan so'ng `about` so'zini yozib ishlatsak, quyidagicha oyna hosil bo'ladi:

<p align="center">
    <img src="./image/about_page.png" width="500">
</p>


### Blogga xabarlar qo'yish

`views.py`ga quyidagicha o'zgarishlar qilamiz:
 1. Har bir blogning sarlavhasi, muallifi, matni va qachon yozilganligi haqida malumot bo'ladi. Ushbu narsalarni 
    mujasammlashtirgan o'zgaruvchi xosil qilamiz. Uni nomini `xabarlar` deb ataymiz:  

    ```python
    bloglar = [
        {
            'muallif': 'Nuriddin',
            'sarlavha': 'Programma nima?',
            'matn': 
                """Programma bu aniq bir muammoni yechish uchun ko'rsatmalar ketma keltligidir. 
                    Programmalash esa mana shu ko'rsatmalarni ishlab shiqishdir. Shuning uchun, 
                    programmist uchun eng muhim kerak bo'ladigan mahorat bu berilgan muammoni hal qilish ketma-ketligini 
                    o'ylab topish. Yechim ko'rsatmalari aniq va to'g'ri bo'lishi shart. Bu mahorat, programma tuzish orqali 
                    shakllantiriladi. Qancha ko'p programma tuzsangiz shuncha yaxshi, ko'p o'qish yoki kino ko'rish bilan emas :).
                """,
            'sana': '28 Avgust, 2021'
        },
        {
            'muallif': 'Muhriddin',
            'sarlavha': 'Funksiya haqida',
            'matn': 
                """Biz programma ko'rsatmalardan tashkil topishini bildik. Kattaroq programma tuzayotganimizda, ko'rsatmalar 
                    ko'payib ketadi. Ularni ixchamlashtirish uchun, soddalashtirish uchun biron nima qilishimiz kerak.
                    Tasavvur qiling bir 999 varaqli kitob bor. Uning na mundarijasi, na bobi bor. Na bo'limi, na varaq 
                    nomeri bor. Boshidan oxirigacha hammasi tekst. Kitobni o'qiyotgan odam o'qib ketaveradi. Lekin u 
                    yerdan qaysi betga kelgani, o'qiyotgan joyi asosan nima uchunligi bilmay o'qib ketaveradi. Bu 
                    kitobxonga juda katta qiyinchilik bo'ladi. Mana shu va boshqa muammolarni hal qilish uchun 
                    kitoblarda quyidagilar qilingan:
                """,
            'sana': '17 Sentabr 2021'
        }
    ]
    ```
    
    Bu yerda, 2-ta elementi bo'lgan `list` yaratdik. Har bir elementi dict dan tashkil topgan. 
    Mana shu xabarlarni bosh sahifada chiqaramiz. Buning uchun, `home` nomli funksiyaga quyidagicha o'zgartisihlar kiritamiz.

    ```python
    def home(request):
        kontekst = {
            "bloglar": bloglar
        }
        return render(request, "blog/home.html", kontekst)
    ```
    Funksiyada `kontekst` degan o'zgaruvchiga `bloglar`ni yuklaymiz. Keyin, `kontekst` `render`ning uchunchi argument sefatida
    beramiz. Bu yerda shunday qilayapmizki, request

    `home.html` da quyidagi ishni bajaramiz.

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
    <img src="./image/post.png" width="400">
</p>

### Sayt sarlavhasi bilan ishlash

`title`ga sarlavha yozishni ko'ramiz. `home.html`ga quyidagilarni bajarsak `title` o'zgarganini ko'ramiz:

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

`about.html` ga quyidagicha yozamiz:

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
    return render(request, "blog/about.html", {'title': " ochiqai"})
```

Bu yerda `"ochiqai"` yozuvi `home.html` va `about.html`ga ketayapti.

<p align="center">
    <img src="./image/home_title.png" width="350">
</p>

<p align="center">
    <img src="./image/title_about.png" width="350">
</p>

E'tibor bersangiz `title` qismimizning sarlavhasini o'zgartirdik.


### Takrorlanishga qarshi 

Ko'pincha  `html` fayllar yaratganimizda bir xil kodlarni qayta qayta yozishga to'g'ri keladi. Shu maqsadda kodni
minimallashtirish uchun merosxo'rlik usuli bor. Bu nafaqat kodni kamaytirishga balki kodni tartibli va xatolarni kamaytirishga 
hizmat qiladi. Buning uchun birinchi `blog/templates` da `base.html` ni yaratamiz va unga quyidagicha yozamiz:

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

Shu bilan asosiy htmlni yaratib oldik. Endi, boshqa fayllarni shu faylga solishtiramiz va 
 o'xshash qismlarini olib tashlaymiz va quyidagicha o'zgartirishlar qilamiz.

`home.html` `base.html`ga qarshi

```python
{% extends 'blog/base.html' %}

{% block content %}
    {% for xabar in xabarlar %}
        <h1>{{ xabar.sarlavha}}</h1>
    {% endfor %}
    <h1>Blog home</h1>
{% endblock content %}
```

`extends` modulidan foydalanib `base.html` chaqirgan holda kodlarimizni osonroq ko'rinishga keltiramiz.

`about.html` `base.html`ga qarshi

```python
{% extends 'blog/base.html' %}

{% block content %}
    <h1>About home</h1>
{% endblock content %}
```

Serverni qayta ishlatsangiz avvalgidek ishlayveradi.

<p align="center">
    <img src="./image/home_view.png" width="350">
</p>

<p align="center">
    <img src="./image/about_view.png" width="350">
</p>



### Blog bosh sahifasini yaxshilash

Hozirgacha qilingan web sahilarimiz ko'rinishi oddiy, va blogga o'xshamaydi. Ozroq ko'rinishini yaxshilaymiz. Ko'rinishni
yaxshilash maqsadida bir necha tayyor templatelar bor. Shulardan biri `bootstrap` deb ataladi. Hozir bootstrapdan foydalanishni ko'rib 
chiqamiz. [Man shu](https://getbootstrap.com/docs/5.2/getting-started/rtl/#starter-template) manzilga borib, kerakil qismlarni
ko'chirishni boshlaymiz:

<p align="center">
    <img src="./image/head_bootstrap.png" width="600">
</p>

Yuqorida ko'rsatilgan qismni olib, `base.html`ning `head`tagiga tashlaymiz. `title`dan nusxa olmadik, 
chunki `base.html`da `title` qismi mavjud.

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

Xuddi shunday qilib `body` qismidagi kodlarni `base.html`ning  `body` qismiga tashlaymiz:

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

Shu bilan `bootstrap`ni fayllarga qo'shib bo'ldik.  Endi, `base.html`ning `body` qismidagi `block content`ni 
alohida `div`ga olib `class`ga `container` yuklaymiz va serverni ishlatib ko'ramiz.

```html
<div class="container">
{% block content %}  {% endblock content %}
</div>
```

<p align="center">
    <img src="./image/home_bts.png" width="400">
</p>

Foydalanuvchiga `views.py`dagi `xabarlar ` qismidan `muallif`, `sarlavha` va `matn`  ma'lumotlarini taqdim qilish ko'ramiz. 
Buning uchun `home.html`ga quyidagi o'zgartirishni kiritamiz holos.
```html
{% extends 'blog/base.html' %}

{% block content %}
    {% for xabar in xabarlar %}
        <h1>{{ xabar.muallif}}</h1>
        <h2>{{ xabar.sarlavha}}</h2>
        <h2>{{ xabar.matn}}</h2>
    {% endfor %}
    <h1>Blog home</h1>
{% endblock content %}
```
Biz yuqorida o'zgarishda `muallif` va  `matn` qismlarini qo'shib qo'yamiz holos. <br>
Serverimizni yangilasak quyidagicha ko'rinish hosil bo'ladi.

<p align="center">
    <img src="./image/newHomePage.png" width="600">
</p>

Saytimizni yanada chiroyliroq qilish uchun `base.html`ga quyidagi ishlarni bajarib o'tamiz.

<details>
<summary>base.html</summary>

```html
<!DOCTYPE html>
<html>
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
<body>
        <header class="site-header">
          <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
            <div class="container">
              <a class="navbar-brand mr-4" href="/">Django Blog</a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                  <a class="nav-item nav-link" href="/">Home</a>
                  <a class="nav-item nav-link" href="/about">About</a>
                </div>
                <!-- Navbar Right Side -->
                <div class="navbar-nav">
                  <a class="nav-item nav-link" href="#">Login</a>
                  <a class="nav-item nav-link" href="#">Register</a>
                </div>
              </div>
            </div>
          </nav>
        </header>
        <main role="main" class="container">
          <div class="row">
            <div class="col-md-8">
              {% block content %}{% endblock %}
            </div>
            <div class="col-md-4">
              <div class="content-section">
                <h3>Our Sidebar</h3>
                <p class='text-muted'>You can put any information here you'd like.
                  <ul class="list-group">
                    <li class="list-group-item list-group-item-light">Latest Posts</li>
                    <li class="list-group-item list-group-item-light">Announcements</li>
                    <li class="list-group-item list-group-item-light">Calendars</li>
                    <li class="list-group-item list-group-item-light">etc</li>
                  </ul>
                </p>
              </div>
            </div>
          </div>
        </main>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
    -->

</body>
</html>
```
</details>
Yuqorida `header` va `main` teglarida mavjud kodlarni qo'shdik va `container` div qismidagi `content` block qismini olib tashladik.

* `blog` appimiz ichidan `static` nomli papka yaratib olamiz. `static` papkadan esa `blog` nomli papka yaratib olamiz. Shu joydan `blog` appimizga tegishli `css` kodlarini barajaramiz. Va `main.css` nomli `css` faylini yaratib olamiz.

<p align="center">
    <img src="./image/main_css.png" width="600">
</p>

`main.css`da quyidagi kodlarni `copy` qilib tashlaymiz.

<details>
<summary>main.css</summary>

```html 
body {
  background: #fafafa;
  color: #333333;
  margin-top: 5rem;
}

h1, h2, h3, h4, h5, h6 {
  color: #444444;
}

ul {
  margin: 0;
}

.bg-steel {
  background-color: #5f788a;
}

.site-header .navbar-nav .nav-link {
  color: #cbd5db;
}

.site-header .navbar-nav .nav-link:hover {
  color: #ffffff;
}

.site-header .navbar-nav .nav-link.active {
  font-weight: 500;
}

.content-section {
  background: #ffffff;
  padding: 10px 20px;
  border: 1px solid #dddddd;
  border-radius: 3px;
  margin-bottom: 20px;
}

.article-title {
  color: #444444;
}

a.article-title:hover {
  color: #428bca;
  text-decoration: none;
}

.article-content {
  white-space: pre-line;
}

.article-img {
  height: 65px;
  width: 65px;
  margin-right: 16px;
}

.article-metadata {
  padding-bottom: 1px;
  margin-bottom: 4px;
  border-bottom: 1px solid #e3e3e3
}

.article-metadata a:hover {
  color: #333;
  text-decoration: none;
}

.article-svg {
  width: 25px;
  height: 25px;
  vertical-align: middle;
}

.account-img {
  height: 125px;
  width: 125px;
  margin-right: 20px;
  margin-bottom: 16px;
}

.account-heading {
  font-size: 2.5rem;
}
```
</details>

`base.html`ga `main.css` faylini quyidagicha qo'shib qo'yamiz.

<details>
<summary>base.html</summary>

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.rtl.min.css" integrity="sha384-dc2NSrAXbAkjrdm9IYrX10fQq9SDG6Vjz7nQVKdKcJl3pC+k37e7qJR5MVSCS+wR" crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

    {% if title %}
        <title>django-blog/{{title}}</title>
    {% else %}
        <title>django-blog/</title>
    {% endif %}
</head>
<body>
        <header class="site-header">
          <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
            <div class="container">
              <a class="navbar-brand mr-4" href="/">Django Blog</a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                  <a class="nav-item nav-link" href="/">Home</a>
                  <a class="nav-item nav-link" href="/about">About</a>
                </div>
                <!-- Navbar Right Side -->                <div class="navbar-nav">
                  <a class="nav-item nav-link" href="#">Login</a>
                  <a class="nav-item nav-link" href="#">Register</a>
                </div>
              </div>
            </div>
          </nav>
        </header>
        <main role="main" class="container">
          <div class="row">
            <div class="col-md-8">
              {% block content %}{% endblock %}
            </div>
            <div class="col-md-4">
              <div class="content-section">
                <h3>Our Sidebar</h3>
                <p class='text-muted'>You can put any information here you'd like.
                  <ul class="list-group">
                    <li class="list-group-item list-group-item-light">Latest Posts</li>
                    <li class="list-group-item list-group-item-light">Announcements</li>
                    <li class="list-group-item list-group-item-light">Calendars</li>
                    <li class="list-group-item list-group-item-light">etc</li>
                  </ul>
                </p>
              </div>
            </div>
          </div>
        </main>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
    -->

</body>
</html>
```
</details> 

Yuqorida biz `base.html`ga `{% load static %}` va `<link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">` kodlarini kiritib o'tdik. 
`{% load static %}`bu komanda orqali `static` faylini yuklab olamiz, `<link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">` bu komanda orqali esa `href=""` qismiga `css` faylimiz joylashgan manzilini berib o'tdik.

* Serverimizni to'xtatib qayta ishlatib ko'rsak quyidagi oyna hosil bo'ladi.

<p align="center">
    <img src="./image/homePageWithCss.png" width="400">
</p>

* Block contentlarimiz ajralib chiroyli ko'rinishi uchun `home.html`ga quyidagi o'zgartirishlarni qilib o'tamiz.

```html
{% extends 'blog/base.html' %}

{% block content %}
    {% for xabar in xabarlar %}
        <article class="media content-section">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="#">{{ xabar.muallif }}</a>
              <small class="text-muted">{{ xabar.sana }}</small>
            </div>
            <h2><a class="article-title" href="#">{{ xabar.sarlavha}}</a></h2>
            <p class="article-content">{{ xabar.matn}}</p>
          </div>
        </article>
    {% endfor %}
    <h1>Blog home</h1>
{% endblock content %}
```

Serverimizni qaytadan yangilasak, quyidagi oyna hosil bo'ladi.

<p align="center">
    <img src="./image/homePageblogs.png" width="400">
</p>

```html
            <div class="container">
              <a class="navbar-brand mr-4" href="/">Django Blog</a>   <----- 
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                  <a class="nav-item nav-link" href="/">Home</a>  <-----
                  <a class="nav-item nav-link" href="/about">About</a>   <-----
                </div>
                <!-- Navbar Right Side -->                <div class="navbar-nav">
                  <a class="nav-item nav-link" href="#">Login</a>
                  <a class="nav-item nav-link" href="#">Register</a>
                </div>
              </div>
```
So'ngi bajaradigan ishimiz `base.html` yuqorida `<-----` bilan ko'rsatilgan qatorlarni quyidagicha o'zgartiramiz.

```html
            <div class="container">
              <a class="navbar-brand mr-4" href="{% url 'blog-home' %}">Django Blog</a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                  <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a>
                  <a class="nav-item nav-link" href="{% url 'blog-about' %}">About</a>
                </div>
                <!-- Navbar Right Side -->
                <div class="navbar-nav">
                  <a class="nav-item nav-link" href="#">Login</a>
                  <a class="nav-item nav-link" href="#">Register</a>
                </div>
              </div>
            </div>
```

* Serverni yangilasak quyidagi oyna hosil bo'ladi.

<p align="center">
    <img src="./image/saytKurinishi.png" width="400">
</p>

