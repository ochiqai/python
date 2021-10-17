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
7. bo'sh string nima? Javobni konsolga chiqaring.
8. Indeks nima? Javobni konsolga chiqaring.
9. string methodlaridan biri bo'lmish `strip` nima qiladi?
10. string methodlaridan biri bo'lmish `replace` nima qiladi?
11. string methodlaridan biri bo'lmish `lower` nima qiladi?
12. string methodlaridan biri bo'lmish `upper` nima qiladi?
13. string methodlaridan biri bo'lmish `count` nima qiladi?
14. palindrom degan funksiya programmasini tuzing. Palindrom degani bir so'zning
    to'g'ri va teskarisi bir zil degani. Masalan , katak, bob.

    <details>
    
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
16. Quyidagi Python kodni olingda, `find` va bo'laklashdan foydalanib son bor joyni ajratib oling.
keyin uni haqiqiy songe `float` dan foydalanib o'tkazing. NAtijani konsolga chiqaring
    
```python
massa = "Kompyuter:6.78 kg"
```
   <details> <summary>Javob</summary>

   ```python
      massa = "Kompyuter:6.78 kg"
      x=massa.find("6")
      a=float(massa[x:14])
      print(a)
   ```
   </details> 


