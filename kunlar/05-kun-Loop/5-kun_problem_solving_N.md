## Problem solving javoblari

1. Inkrement nima?
2. Dekriment nima?
3. O'zgaruvchilarni yangilash nima?
4. `while` yordamida 30 dan 0 gacha bo'lgan sonlarni chiqaring, kamayish tartibida.
      
   <details> <summary>Javob</summary>
      
      ```python
      i=30
      while i>0:
          print(i, end=" ")
          i=i-1
      ```
      </details> 
5. `for` yordamidan 1 dan 15 gacha bo'lgan sonlarni chiqaring.
   
   <details> <summary>Javob</summary>
     
   ```python
      for c in range(1,16,1):
          print(c, end=" ")
      ```    
   
   </details> 
6. Shunday programma yozingki, u foydalanuvchidan sonlarni qabul qilsin agar son kiritilmay 
   harf kiritilsa, foydalanuvchiga "son kiriting" deb ogohlantirsin va davom etsin. Qachonki 
   foydalanuvchi `tamom` deb yozsa. O'shanda, shu paytgacha bo'lgan sonlarni hammasi qo'shib 
   konsolga chiqarsin.
   ```commandline
   Raqam kiriting: 4 
   Raqam kiriting: 6
   Raqam kiriting: 5
   Raqam kiriting: nuriddin
   son kiriting
   Raqam kiriting: 10
   Raqam kiriting: tamom
   yigindi: 20
   ```

   <details> <summary>Javob</summary>
     
   ```python
      summa=0
      while True:
          son=input("son kiriting: ")
          if son=="tamom":
              break
          try:
              son_int=int(son)
              summa=summa+son_int
              print(son_int)
          except:
              print("Iltimos, son kiriting!")
              continue
      print(f"yigindi: {summa}") 
   ```    
   
   </details> 
   
7. Shunday programma yozingki, u foydalanuvchidan sonlarni qabul qilsin agar son kiritilmay 
   harf kiritilsa, foydalanuvchiga "son kiriting" deb ogohlantirsin va davom etsin. Qachonki 
   foydalanuvchi `tamom` deb yozsa. O'shanda, shu paytgacha kirtilgan sonlar umumiysini 
   konsolga chiqarsin.
   
   ```commandline
   Raqam kiriting: 4 
   Raqam kiriting: 6
   Raqam kiriting: 5
   Raqam kiriting: nuriddin
   son kiriting
   Raqam kiriting: 10
   Raqam kiriting: tamom
   soni: 4
   ```

8. Shunday programma yozingki, u foydalanuvchidan sonlarni qabul qilsin agar son kiritilmay 
   harf kiritilsa, foydalanuvchiga "son kiriting" deb ogohlantirsin va davom etsin. Qachonki 
   foydalanuvchi `tamom` deb yozsa. O'shanda, shu paytgacha kirtilgan sonlar o'rtachasini 
   konsolga chiqarsin.
   
   ```commandline
   Raqam kiriting: 4 
   Raqam kiriting: 6
   Raqam kiriting: 5
   Raqam kiriting: nuriddin
   son kiriting
   Raqam kiriting: 10
   Raqam kiriting: tamom
   soni: 5
   ```
   
9. Shunday programma tuzingki konsolga quyiga chiqsin.

```commandline
x    pow(x, 2)  pow(x, 3)   Farqi
-    ---------  ---------   -----
1.0  1.0        1.0         0.0
2.0  4.0        8.0         4.0  
```