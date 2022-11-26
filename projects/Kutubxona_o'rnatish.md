# Kerakli kutubxonalarni yuklab olish va undan foydalanish

* [Pythonda kutubxona nima](#pythonda-kutubxona-nima)
* [Kutubxonani o'rnatish va foydalanish](#kutubxonani-o'rnatish-va-foydalanish)

## Pythonda kutubxona nima
* Python dasturidan foydalanayotganimizda yordamchi dastur sifatida bir qacha kutubxonalardan foydalanishimiz mumkin.
Bular asosan ma'lum maqsad uchun yaratilgan kutubxonalar sanaladi. Misol uchun `numpy` vektorlar bilan ishlash uchun mo'ljallangan, 
`matplotlib` esa visual diagrammalarni hosil qilish uchun mo'ljallangan dastur hisoblanadi.

## Kutubxonani o'rnatish va foydalanish
* keling unda ularni birma - bir yuklab olishni ko'rib chiqamiz. Yuklab olish uchun:
```md
pip install numpy yoki conda install numpy 
```
qilib kiritib olishigiz kerak bo'ladi.
* Natijasi esa: Terminalda shu ko'rinishda ko'rinadi
```
Collecting numpy
  Downloading numpy-1.23.5-cp310-cp310-win_amd64.whl (14.6 MB)
     |████████████████████████████████| 14.6 MB 26 kB/s
Installing collected packages: numpy
Successfully installed numpy-1.23.5
WARNING: You are using pip version 21.1.2; however, version 22.3.1 is available.
You should consider upgrading via the 'C:\Users\user\PycharmProjects\pythonProject1\pythonProje
ct\pythonProject\4_dars\venv\Scripts\python.exe -m pip install --upgrade pip' command.

```
* Mana numpy ham yuklab olindi va u ishlatish uchun tayyor hisoblanadi. Uni ishaltish uchun esa
```md
import numpy as np
```
* Yuqoridagi shaklda chaqirib olinadi va undan foydalanish mumkin bo'ladi.
* Misol uchun:

```md
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)
```
* Yuqorida shaklda foydalanishni boshlasak bo'ladi.

* Bundan tashqari esa `matplotlib` ham shunday shaklda yuklab olishimiz mumkin bo'ladi.
```md
pip install matplotlib yoki conda install matplotlib
```
* Va uning natijasi esa:
```md
Collecting matplotlib 
  Downloading matplotlib-3.6.2-cp310-cp310-win_amd64.whl (7.2 MB) 
     |████████████████████████████████| 7.2 MB 2.2 MB/s
Requirement already satisfied: numpy>=1.19 in c:\users\user\pycharmprojects\pythonproject1\pythonproject\pythonproject\4_dars\venv\lib\site-packages (from matplotlib) (1.23.5) 
Collecting python-dateutil>=2.7 
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB) 
Collecting packaging>=20.0 
  Using cached packaging-21.3-py3-none-any.whl (40 kB) 
Collecting pyparsing>=2.2.1 
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB) 
Collecting fonttools>=4.22.0 
  Using cached fonttools-4.38.0-py3-none-any.whl (965 kB) 
Collecting cycler>=0.10 
  Using cached cycler-0.11.0-py3-none-any.whl (6.4 kB) 
  Downloading contourpy-1.0.6-cp310-cp310-win_amd64.whl (163 kB)
     |████████████████████████████████| 163 kB 3.3 MB/s
Collecting pillow>=6.2.0
  Using cached Pillow-9.3.0-cp310-cp310-win_amd64.whl (2.5 MB)
Collecting kiwisolver>=1.0.1
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pyparsing, python-dateutil, pillow, packaging, kiwisolver, fonttools, 
cycler, contourpy, matplotlib
Successfully installed contourpy-1.0.6 cycler-0.11.0 fonttools-4.38.0 kiwisolver-1.4.4 matplotlib-3.6.2 pa
ckaging-21.3 pillow-9.3.0 pyparsing-3.0.9 python-dateutil-2.8.2 six-1.16.0
WARNING: You are using pip version 21.1.2; however, version 22.3.1 is available.
You should consider upgrading via the 'C:\Users\user\PycharmProjects\pythonProject1\pythonProject\pythonPr
oject\4_dars\venv\Scripts\python.exe -m pip install --upgrade pip' command.
```
* Uni ham ishlatishimi uchun ham `import matplotlib` dan foydalnamiz.
* Misol sifatida

```md
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```
* Bunda tashqari yana ko'plab kutubxonalar mavjud va ular ham shu shaklda yuklab olib, foydalanish mumkin bo'ladi.





















