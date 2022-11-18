# Matplotlib 

* [Matplotlib nima](#matplotlib-nima)
* [Matplotlib funksiyalari](#matplotlib-funksiyalari)
* - [pyplot](#pyplot)
* - [Line](#line)
* - [Labels](#labels)
* - [Subplot](#subplot)
* [Tayanch tushunchalar](#tayanch-tushunchalar)



## Matplotlib nima 

* Matplotlib bu - pythondagi kutubxonalardan biri bo'lib, grafikalarni yasashga hizmat qiladi.

* Misol uchun ekranga shunday chiqaramiz

<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img.png">

</p>

* Dastlabki qadamda biz maplotibni o'rnatib olamiz.
```md
pip install matplotlib yoki conda install matplotlib 
```
* Biz uni ishlatishda `import matplotlib` qilib chaqirib olamiz.

## Matplotlib funksiyalari
___
## Pyplot 
* Pyplot bu - bizga line graflarni chizishga imkon beruvchi funksiyalardan biri. Keyingi ishlarda uni deyarli hamma vaqtda qo'llaymiz.
`import matplotlib.pyplot as plt` qilinadi. Keyin diagrammalarimizda biz arralardan foydalanamiz, shuning uchun numpyni ham import qilib
olamiz `import numpy as np`. Diagramma asosi ikki o'qdan tashkil topadi 1- x o'qi, misol uchun `x = np.array([0, 6])`
2 - y o'qi, misol uchun `y = np.array([0, 250])`. Keyin ikkala o'qlarni plt.plotda birlashtiramiz `plt.plot(x, y)`.
So'nggi qadamda diagrammamizni ekranga chiqarib olamiz, buning uchun `plt.show()` komandasidan foydalanamiz.

```python
import matplotlib.pyplot as plt 
import numpy as np

x = np.array([0, 6])
y = np.array([0, 250])

plt.plot(x, y)
plt.show()
```
* Siz ish jarayonida `import matplotlib.pyplot as plt` va `import numpy as np` bir marta import qilishingiz kifoya qiladi.
* Natijasi: Shu holatda namayon bo'ladi. Bunda `x o'qi(0, 6)`, `y o'qi(0, 250)` tashkil etadi.

<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_1.png">
</p>

* Biz bundan tashqari biz x va y o'qlarga bir qancha qiymatlar berib ham foydalanishimiz mumkin.
```console
x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
```
<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_2.png">
</p>

* Biz bazi vaqtlarda x o'qi tushurib qoldirishimiz ham mumkin bo'ladi. Bunday holatda agar y o'qi nechta qiymat olishiga qarab
x o'qi ham shuncha qiymat oladi.
* Bunda x o'qi (0, 1, 2, 3, 4 .. n) shaklida boshlanadi
```console
y = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
```
<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_3.png">
</p>

## Line

* Yuqoridagi misollarda biz bittalik linelarni ko'rib chiqdik, endi ir diagrammada bir dan ko'p ham bo'lishi mumkin, keling birgalikda ko'ramiz
* Misol uchun
```console
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
```
* Pastdagi natijadan ko'rinib turibdiki, y1 va y2 o'qlarni yaratib olib ikkita `plt.plot()` ham qilib oldik.

<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_4.png">
</p>

* Bundan tashqari biz ikkta x o'qi va ikkita y o'qini ham brib o'tishimiz mumkin.
```console
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2) bunda o'qlarni bitta joyga jamlanganligi ko'rib turibsiz
plt.show()

```
<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_5.png">
</p>

## Labels

* Bundan tashqari biz giagrammalar ichiki qismi title hamda x va y o'qlariga nom berishimiz ham mumkin.
```Console
x = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
y = np.array([240, 200, 290, 315, 220, 100, 160, 410, 600, 330, 220])

plt.plot(x, y)

plt.title("Mashina Savdosi") - Bu diagrammani eng yuqirisindan o'rin oladi
plt.xlabel("Davr") - bu x o'qi uchun nom
plt.ylabel("Sotib olingan mashinalar soni") - bu y o'qi uchun nom

plt.show()
```
* Natijasi:
<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_6.png">
</p>

* Agar biz diagrammamizga grid line qo'shmoqchi bo'lsak, `plt.grid()` foydalanmiz.
* Misol uchun diagramma shunday shaklga keladi.

<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_7.png">
</p>

## Subplot 
* Subplot yordamida biz bir vaqtning o'zida ikkita diagramma qilish imkoni beradi.
```console
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) - bunda 1 butun, 2 esa butun yarmi, oxiridagi 1 esa butun yarmini 1 - qismi 
plt.plot(x,y)
plt.title("Sotuvlar")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)- bunda 1 butun, 2 esa butun yarmi, oxiridagi 2 esa butun yarmini 2 - qismi
plt.plot(x,y)
plt.title("Daromat")

plt.show()
```

<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_8.png">
</p>

* Agar biz `plt.subplot()` qavs ichiga miqdor bermasdan yozsak, natijada ikki bo'lak birlashadi.

* Natijasi: Shunday ko'rinishga ega bo'ladi.
<p>
    <img src="D:\ochiqai\python\projects\matplotib_images\img_9.png">
</p>

## Tayanch tushunchalar
<ul>
<li>import - faylni tashqi kutubxondan olib kelish </li>
<li>plot - x va y o'qlarini yashash</li>
<li> show - ekranga namoyish qilish</li>
<li>subplot - ikkita diagramma hosil qilish</li>
</ul>

Bazi rasmlar va ma'lumotlar  [w3shools.com](https://www.w3schools.com/) dan olingan.

