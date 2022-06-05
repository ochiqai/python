## Problem solving

1. Sequence nima? Javobni konsolga chiqaring.
   ```python
   print("Javob: ketma-ket tartibda kelgan beligilar to'plami")
   ```   
2. Immutable nima? Javobni konsolga chiqaring.
3. search nima? Javobni konsolga chiqaring.
4. Kaunter nima? Javobni konsolga chiqaring.
5. Invocation nima? Javobni konsolga chiqaring.
6. slice nima? Javobni konsolga chiqaring.
   ```python
   ism = "Ibrohim"
   print(ism[2:5]) 
   # Javob:
   # roh
   ```
7. bo'sh string nima? Javobni konsolga chiqaring.
   ```python 
   bush = " " # bo'sh string 
   ```
8. Indeks nima? Javobni konsolga chiqaring.
9. string methodlaridan biri bo'lmish `strip` nima qiladi?
10. string methodlaridan biri bo'lmish `replace` nima qiladi?
11. string methodlaridan biri bo'lmish `lower` nima qiladi?
    ```python 
    viloyat = "SAMARQAND"
    print(viloyat.lower())
    # Javob:
    # samarqand
    ```
12. string methodlaridan biri bo'lmish `upper` nima qiladi?
    ```python 
    viloyat = "toshkent"
    print(viloyat.upper())
    # Javob:
    # TOSHKENT
    ```
13. string methodlaridan biri bo'lmish `count` nima qiladi?
14. Palindrom degan funksiya programmasini tuzing. Palindrom degani bir so'zning
    to'g'ri va teskarisi bir zil degani. Masalan , katak, bob.
    
   <details> <summary>Javob</summary>

   ```python
   def palindrom(x):
       if x == x[::-1]:
           natija = "palindrom"
       else:
           natija = "palindrom emas"
   return natija
   print(palindrom("katak"))
   ```
   </details> 
15. Mana bu funksiya nima qiladi?

   ```python
   def harqanday_kichikharf(s):
       for c in s:
           if c.islower():
               return True
           else:
               return False
   ```
      <details> <summary>Javob</summary>

   ```python
   # islower.
   # Matnda hamma harf kichik bo'lsa True qaytaradi
   # Matnda bir donagina katta harf bulsa ham False qaytaradi.
   ism = "It is a pen"
   print(ism.islower()) # False
   
   ism = "it is a pen"
   print(ism.islower()) # True
   
   ism = "This is Nuriddin"
   print(ism.islower()) # False
   
   ism = "this is Nuriddin"
   print(ism.islower()) # False
   # Javob:
   #False
   #True
   #False
   #False
   
   # 15-misol
   def harqanday_kichikharf(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
   yozuv="I am a student"
   natija = harqanday_kichikharf(yozuv)
   print(yozuv.islower())
   # Javob:
   # False
   ```
   </details>
16. Quyidagi Python kodni olingda, `find` va bo'laklashdan foydalanib son bor joyni ajratib oling.
Keyin uni haqiqiy songe `float` dan foydalanib o'tkazing. Natijani konsolga chiqaring
    
   ```python
   massa = "Kompyuter:6.78 kg"
   ```
   <details> <summary>Javob</summary>

   ```python
   massa = "Kompyuter:6.78 kg"
   x = massa.find("6")
   y = massa.find("8")
   son_qismi = float(massa[x:y+1])
   print(son_qismi)
   ```
   </details> 


