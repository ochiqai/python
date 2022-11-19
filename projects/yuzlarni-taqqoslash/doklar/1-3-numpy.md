# Numpy 
___

* [Numpy nima](#numpy-nima)
* [Arraylar bilan ishlash](#arraylar-bilan-ishlash)
* [Arraylarning bir qancha funksiyalari](#arraylarning-bir-qancha-funksiyalari)
* [Tayanch tushunchalar](#tayanch-tushunchalar)

```Console
-------
|
|    |      |
|  --|--   
|    |      |
|
-------
```
## Numpy nima
___

* NumPy (==Numerical Python==) - bu python kutubxonasidan biri bo'lib, u arraylar (matritsa) bilan ishlashga yordam beradi.
```python
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
```
* Dastlabki qadamda biz NumPy o'rnatib olamiz.
```pyhton
conda install numpy
```
* Keyingi qadamda biz Numpydan foydalanishni boshlaymiz.
> kutubnona chaqirish : import numpy as np
> > array yaratishimiz uchun esa : arr = np.array([ ])
> > > uni ekaranga chiqarish : print(arr)

## Arraylar bilan ishlash
___
> Arraylarni o'chamlari cheklanmagan : ([1, 2, 3, 4, n])

* Arraylarning ishlatilishi listlar bilan ishlashga o'xshab ketadi. Uni typeni aniqlash uchun quyidagini kiritamiz.
```python


arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
# natija : <class 'numpy.ndarray'>
```
* Arraylar obyetlardan tashkil topgan. Bu obyektlar `ndarray` deb ataladi va u `dimensions` lardan tashkil topgan. Xalq tilida
bular 0D, 1D, 2D, 3D (uning ma'nosi 1 o'lchamli, 2 o'lchamli, 3 o'lchamli manoda keladi) va hklar deb yuritilib kelinadi.
* Bularning eng sodda ko'rinish: `0-d array`
```python


arr = np.array(42)

print(arr)
# natijasi: 42 
```
* `1D array`
```python


arr = np.array([1, 2, 3, 4, 5])

print(arr)
# natija : [1 2 3 4 5]
```
> arr = np.array([1, 2, 3, 4, 5]) # arraylarni hosil qilishda numpy yoki qisaqacha np kiritib, array yoziladi va () qavs ichiga `[ ]` kiritiladi. Arrayni obyetlari oshib borgan sari `[]` ham qo'shimcha kiritiladi.

* `2D array`
```python


arr = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])

print(arr)
# natija : [[1 2 3]
#           [4 5 6]]
```
* `3D array`
```python


arr = np.array([
    [[1, 2, 3], [4, 5, 6]], 
    [[1, 2, 3], [4, 5, 6]]
])

print(arr)
# natija : [[1, 2, 3], [4, 5, 6]], 
#          [[1, 2, 3], [4, 5, 6]]
```
| NumPydagi `Oltin qoida`ni doim esda saqlsh kerak |
|--------------------------------------------------|
```console
arr = np.array([
        [1, 2, 3],
        [1, 2] 
])
Yuqoridagi array bizga hech qanaqa natija qaytarmaydi.

Avvalo biz ularni tenglashtirishimiz kerak bo'ladi:
arr = np.array([
        [1, 2, 3],
        [1, 2, 3] 
])
Yana ba'zi narsalarni esdan chiqarmasligimiz kerak:
                    1 - holat
arr = np.array([
        [],
        [] 
])
                    2 - holat
arr = np.array([
        [],
        [1, 2, 3] 
])
Yuqoridagi 1 - holatda arraylar 0 natija qaytaradi.
2 - holatda esa natija qaytarmaydi. 
```
## Arraylarning bir qancha funksiyalari
___
* Arraylarni indexni aniqlsh uchun huddi listda qilingan amalarni bajaramiz
```python


arr = np.array([1, 2, 3, 4])

print(arr[0])
# natija : 1

# 2D


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('1-qatorning 2-elementini oladi: ', arr[0, 1])
# natija : 2

# 3D


arr = np.array([
    [[1, 2, 3], [4, 5, 6]],     
    [[7, 8, 9], [10, 11, 12]]
])

print(arr[0, 1, 2])
# natija : 6
# Bu yerda qanday qilib 6 soni chiqdi.
# (arr[0, 1, 2]) 
# bunda 0 - [[1, 2, 3], [4, 5, 6]], 
# bunda 1 - [4, 5, 6]],
# bunda 2 - [4, 5, 6] indexda 6 raqami olinadi.
```
| Yodda saqlash zarur : Pythonda sonlar ketma ketligi 0, 1, 2, 3 va hk |
|----------------------------------------------------------------------|

* Arraylar o'lchamini aniqlsh uchun `shape`dan foydalanamiz.
```python


arr = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])

print(arr.shape)
# natija : (2, 3)
# bu yerda 2 - qatorlar soni
# bu yerda 3 - ustunlar soni hisoblanadi.
```
* Yodda tuting:
```Console
                        1 - holat


arr = np.array([
    [],
    []
])
print(arr.shape)
Natija : 2 qaytaradi yani bu yerda 2 qator mavjud degani
                        2 - holat


arr = np.array([
    [1],
    [1]
])

print(arr.shape)
Natija : (2, 1) yani 2 qator 1 ta ustunda iborat bo'ladi.
```
* Arraylarning yig'indisini topish uchun esa `sum`dan foydalanamiz
```python


arr = np.array([1, 2, 3, 4, 5])

print(arr.sum())
# Natija : 15
```

 

## Tayanch tushunchalar
___
<ul>
<li>import - faylni tashqi kutubxondan olib kelish </li>
<li>array - matritsalar</li>
<li> dimension- array o'lchamlari</li>
<li>shape - qator va ustunlar sonini aniqlash uchun</li>
</ul>