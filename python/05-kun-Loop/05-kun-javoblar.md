## Problem solving

1. Inkrement nima? <br>
   Inkrement bu - O'zgaruvchi eski qiymatini birga oshirib o'zgartirish.
   ```python
   # Inkrementga misol: 
   x = 1
   x = x + 1 
   ```
2. Dekriment nima? <br>
   Dekriment bu - O'zgaruvchi eski qiymatini birga kamaytirib o'zgartirish.
   ```python
   # Dekrimentga misol: 
   x = 1
   x = x - 1 
   ```
3. O'zgaruvchilarni yangilash nima?
4. `while` yordamida 15 dan 0 gacha bo'lgan sonlarni chiqaring, kamayish tartibida.
      
   <details> <summary>Javob</summary>
      
      ```python
      i = 15
      while i > 0:
          print(i)
          i = i - 1
      # Javob: 
      # 15
      # 14
      # 13
      # 12
      # 11
      # 10
      # 9
      # 8
      # 7
      # 6
      # 5
      # 4
      # 3
      # 2
      # 1
      ```
      </details> 
5. `for` yordamida 1 dan 10 gacha bo'lgan sonlarni chiqaring.
   
   <details> <summary>Javob</summary>
     
   ```python
   for c in range(1, 10, 1):
       print(c)
   # Javob: 
   # 1
   # 2
   # 3
   # 4
   # 5
   # 6
   # 7
   # 8
   # 9
   ```    
   
   </details> 
6. Shunday programma yozingki, u foydalanuvchidan sonlarni qabul qilsin agar son kiritilmay 
   harf kiritilsa, foydalanuvchiga " Iltimos son kiriting " deb ogohlantirsin va davom etsin. Qachonki 
   foydalanuvchi `tamom` deb yozsa. O'shanda, shu paytgacha bo'lgan sonlarni hammasi qo'shib 
   konsolga chiqarsin.
   ```commandline
   Son kiriting: 4 
   Son kiriting: 6
   Son kiriting: 5
   Son kiriting: nuriddin
   Iltimos son kiriting 
   Son kiriting: 10
   Son kiriting: tamom
   yigindi: 20
   ```

   <details> <summary>Javob</summary>
     
   ```python
   summa = 0
   while True:
       son = input("son kiriting: ")
       if son == "tamom":
           break
       try:
           son_int = int(son)
           summa = summa + son_int
           print(son_int)
       except:
           print("Iltimos, son kiriting")
           continue
   print(f"yigindi: {summa}") 
   # Javob:
   # son kiriting: 12
   # 12
   # son kiriting: 37
   # 37
   # son kiriting: ulugbek
   # Iltimos, son kiriting
   # son kiriting: 99
   # 99
   # son kiriting: tamom
   # yigindi: 148
   ```    
   
   </details> 
   
7. Shunday programma yozingki, u foydalanuvchidan sonlarni qabul qilsin agar son kiritilmay 
   harf kiritilsa, foydalanuvchiga " Iltimos son kiriting" deb ogohlantirsin va davom etsin. Qachonki 
   foydalanuvchi `tamom` deb yozsa. O'shanda, shu paytgacha kirtilgan sonlar umumiysini 
   konsolga chiqarsin.
   
   ```commandline
   Son kiriting: 4 
   Son kiriting: 6
   Son kiriting: 5
   Son kiriting: nuriddin
   Iltimos son kiriting
   Son kiriting: 10
   Son kiriting: tamom
   soni: 4
   ```
   <details> <summary>Javob</summary>
     
   ```python
   sana = 0
   while True:
       son = input("son kiriting: ")
       if son == "tamom":
           break
       try:
           son_int = int(son)
           sana = sana + 1
           print(son_int)
       except:
           print("Iltimos, son kiriting")
           continue
   print(f"soni: {sana}") 
   # Javob:
   # son kiriting: 10
   # 10
   # son kiriting: 25
   # 25
   # son kiriting: 42
   # 42
   # son kiriting: Ibrohim
   # Iltimos, son kiriting
   # son kiriting: 78
   # 78
   # son kiriting: tamom
   # soni: 4
   ```    
   
   </details> 
   
8. Shunday programma yozingki, u foydalanuvchidan sonlarni qabul qilsin agar son kiritilmay 
   harf kiritilsa, foydalanuvchiga " Iltimos son kiriting " deb ogohlantirsin va davom etsin. Qachonki 
   foydalanuvchi `tamom` deb yozsa. O'shanda, shu paytgacha kirtilgan sonlar o'rtachasini 
   konsolga chiqarsin.
   
   ```commandline
   Son kiriting: 4 
   Son kiriting: 6
   Son kiriting: 5
   Son kiriting: nuriddin
   Iltimos son kiriting
   Son kiriting: 10
   Son kiriting: tamom
   soni: 6.25
   ```
   
   <details> <summary>Javob</summary>
     
   ```python
   sana = 0
   yigindi = 0
   while True:
       son = input("son kiriting: ")
       if son == "tamom":
           break
       try:
           son_int = int(son)
           yigindi = yigindi + son_int
           sana = sana + 1
           print(son_int)
       except:
           print("Iltimos, son kiriting")
           continue
   print(f"o`rtacha qiymat: {yigindi / sana}")
   # Javob:
   # son kiriting: 2
   # 2
   # son kiriting: 10
   # 10
   # son kiriting: cdd
   # Iltimos, son kiriting
   # son kiriting: 5
   # 5
   # son kiriting: tamom
   # o`rtacha qiymat: 5.666666666666667 
   ```    
   
   </details> 
   
9. Shunday programma tuzingki konsolga quyidagicha chiqsin.

   ```commandline
   x    pow(x, 2)  pow(x, 3)   Farqi
   -    ---------  ---------   -----
   1.0  1.0        1.0         0.0
   2.0  4.0        8.0         4.0  
   ```
   
      <details> <summary>Javob</summary>
        
      ```python
      print(" x    pow(x,2)    pow(x,3)  Farqi")
      print(" -    -------     --------  -----")
      x = 1.0
      while x <= 2:
          print(f"{x}    {pow(x, 2)}         {pow(x, 3)}       {pow(x, 3) - pow(x, 2)}")
          x = x + 1
      # Javob:
      #  x    pow(x,2)    pow(x,3)  Farqi
      #  -    -------     --------  -----
      # 1.0    1.0         1.0       0.0
      # 2.0    4.0         8.0       4.0
      ```    
      
      </details> 