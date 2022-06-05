## Problem solving

0. Agar operatori nima uchun kerak?
1. Programma yarating. Agar berilgan son 100 bo'lsa, 90 dan `"90 dan katta"` deb chiqsin,
aks holda `90 dan kichik` deb chiqsin.
   <details><summary>Javob</summary>

     ```python
        x = 100
        if x > 90:
           print("90 dan katta")
        else:
           print("90 dan kichik")
     ```
   </details>
2. Sonning juft yoki toqligini aniqlang.
   <details><summary>Javob</summary>

     ```python
        x = 7
        if x % 2 == 0:
            print("x juft son")
        else:
            print("x toq son")
     ```
    </details>
3. Programma tuzing. Foydalanuvchi faqat son kiritsin, agar string kiritsa. `Son kiriting, iltimos`
    deb chiqsin. `try\except` dan foydalaning.
   <details><summary>Javob</summary>

     ```python
        x = input("sonni kiriting: ")
        try:
          y = int(x)
        except:
             print("iltimos son kiriting") 
     ```
    </details>
4. Programma tuzing. Agar, foydalanuvchi, 
   - 5 kiritsa `alo`  
   - 4 kiritsa `yaxshi`
   - 3 kiritsa `yomon`
   - 2 kiritsa `qoniqarsiz`
    deb chiqarsin 
   <details><summary>Javob</summary>

     ```python
        x = int(input())
        if x == 5:
             print('alo')
        if x == 4:
             print('yaxshi')
        if x == 3:
             print(yomon)
        if x == 2:
             print('qoniqarsiz')
     ```
    </details>
5. Boolean ifodalar ishlash yo'nalishi qanday? misol keltiring. 
6. Holat bosh qismi nima?
7. Holat tana qismi nima?
8. Zanjirli (chain) holat nima?
9. Ichki (nested) holatlar nima?
10. Interaktive kiritish qanaqa bo'ladi?
11. Mantiqiy amallarda qisqa tutashuv hodisasini tushuntiring?
12. Odatdagidan tashqari holat yani "try/except" ni tushuntiring.
13. Necha xil boolean ifodalar bor?