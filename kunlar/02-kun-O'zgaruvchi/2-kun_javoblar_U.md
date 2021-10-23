 1. O'rganganimizdek, o'zgaruvchilar quyidagicha e'lon qilinadi, `x = 12`. Agar. `12=x` 
    qilinsa nima bo'ladi?

    <details><summary>Javob</summary>
        O'zgaruvchi nomi son bolishi mumkin emas.
    </details>
    
 2. `x = 1/0` ishlating va natijani tushuntiring?

     <details><summary>Javob</summary>

      Nolga bo'lish mumkin emas.

    </details>
 
 
 3. `x = y = z = 111` ishlating va `x, y, z` larni ekranga chiqaring.
   
    <details><summary>Javob</summary>

     ```python
      x = y = z = 111
      print(x, y, z)
     ```
    `x, y, z` hammasi 111 ni oladi.
    </details>


 5. `x = 1` va `y = 2` ikkita o'zgaruvchni ko'paytiring, bo'ling, qo'shing, ayiring, darajaga oshiring
    Natijalarni ekranga (konsolga) chiqaring.
    <details><summary>Javob</summary>

    ```python
      
    x = 1
    y = 2
    z = x * y
    b = x / y
    q = x + y
    a = x - y
    d = x ** y
    print(z, b, q, a, d)

    ```
    
    </details>
    
 6. `a = 2, b = 1, c = 5` quyidagini hisoblang va konsolga chiqaring
    
    <p align="center">
    <img src="https://user-images.githubusercontent.com/24993718/122658278-2654ef00-d163-11eb-95be-817d63587a00.png" height=50>
    </p>

    <details><summary>Javob</summary>

     ```python
    # 1-usul
    a = 2
    b = 10
    c = 5
    x1 = -(-b + (b ** 2 - 4 * c * a) ** (1 / 2)) / (2 * a)
    x2 = -(-b - (b ** 2 - 4 * c * a) ** (1 / 2)) / (2 * a)
    
    print(x1, x2)
    
    # x1 = 0.5635083268962915 x2 = 4.436491673103708
    
    
    # 2-usul
    
    ildiz = (b ** 2 - 4 * c * a) ** (1 / 2)
    maxraj = 2 * a
    
    x1 = -(-b + ildiz)/maxraj
    x2 = -(-b - ildiz)/maxraj
    
    print(x1, x2)
    
    # x1 = 0.5635083268962915 x2 = 4.436491673103708
     ```
    </details>
    


 7. 27 ning 15% ni toping, natijani 'miqdor' ga yuklang.
    <details><summary>Javob</summary>

     ```python
      
    a = 27
    b = 15
    miqdor = (a * b) / 100
    print(miqdor)
    # 4.05

     ```
    </details>
 

 8. 30 ni 0.25 ko'paytiring va natiajni `x` ga yuklang.
    <details><summary>Javob</summary>

     ```python
      x = 30 * 0.25
      print(x)
     ```
    </details>
 

 9. Konsolga `Assalomu Alaykum` deb 100 marta chiqaring.
    <details><summary>Javob</summary>

     ```python
      
    x = "Assalomu Alaykum"
    b = x * 100
    print(b)

     ```
    </details>

 10. `s1="1"` va `s2="2"`. `z = s1 + s2`? `z = s2 + s1` ? `z = s2 * s1`? `z = s2 - s1`?
    <details><summary>Javob</summary>

     ```python
      
       s1 = "1"
       s2 = "2"
       z = s1 + s2  12
       z = s2 + s1  21
       z = s2 * s1  kopaytirib bolmaydi
       z = s1 - s2   ayirib bolmaydi
     
      print(x)

     ```
     </details>
  
 12. Quyigani ishlatish va tushuntiring?
     
```python
s = "salom"
s = s + s
print(s) 
salomsalom
```
 12. Konsolga `oltin baliq` deb deb chiqaring.
    <details><summary>Javob</summary>

     ```python
      
     x = "oltin baliq"
     
      print(x)

     ```
    </details>

 14. Konsolga 'salom salom salom' deb chiqaring.
    <details><summary>Javob</summary>

     ```python
      
       x = "salom"
       y = " "
     z = (x + y) * 3
     
      print(x)
     salom salom salom

     ```
    </details>
 15. Operator bilan qiymatning nima farqi bor?
```python
4 + 5 = 9
operator + 
qiymat  9
```

 17. Quyidagilardan qaysi biri o'zgaruvchi va qaysi biri string?
```python
yashik       ozgaruvchi
'yashik'     string
```

 16. o'zgaruvchi turlarini sanang?
 str float int
 17. Man bu programmani ishlating. Xato bo'lsa to'g'irlang.

   ```python
    print(2 + '2')
togirlash print('2' + '2') # 22 yoki print(2 + 2) # 4