## Problem solving 

1. List nima?
2. Obyekt nima?
3. Referns nima?
4. Nested list nima?
5. Element nima?
6. taxallushlash nima?
7. Ekvivalent nima?
8. List traversal nima?
9. `x = [103, 32, 3, 40, 5, 6]` eng katta qiymatni toping.
   
   <details> <summary>Javob</summary>
   
   ```python
   x = [103, 32, 3, 40, 5, 6]
   print(max(x))
   ```
   
   </details> 
   
10. `x = [103, 32, 3, 40, 5, 6]` eng kichik qiymatni toping.

    <details> <summary>Javob</summary>
   
    ```python
    x = [103, 32, 3, 40, 5, 6]
    print(min(x))
    ```
   
    </details> 
    
11. `x = [103, 32, 3, 40, 5, 6]` barcha elementlar yig'indisini toping.
    
    <details> <summary>Javob</summary>
     
    ```python
    x = [103, 32, 3, 40, 5, 6]
    summa = 0
    for c in x:
        summa = summa + c
    print(summa)
    ```
    </details> 

12. `x = [103, 32, 3, 40, 5, 6]` barcha elementlar ko'paytmasini toping.

    <details> <summary>Javob</summary>
    
    ```python
    x = [103, 32, 3, 40, 5, 6]
    kopaytma = 1
    for c in x:
        kopaytma = kopaytma * c
    print(kopaytma)
    ```
    
    </details> 

13. `s = ['a', 'b', 'c']` 2-elementni `B` ga konvert qiling.

    <details> <summary>Javob</summary>
    
    ```python
    s = ['a', 'b', 'c']
    s[1] = 'B'
    print(s)
    ```
    
    </details> 

14. `s = ['a', 'b', 'c']` 2-elementni `2` ga konvert qiling.

    <details> <summary>Javob</summary>
    
    ```python
    s = ['a', 'b', 'c']
    s[1] = '2'
    print(s)
    ```
    
    </details> 

15. List oxirgi elementini o'chiradigan funksiya tuzing.

    <details> <summary>Javob</summary>
    
    ```python
    def oxirgi_elementini_uchir(c):
        del c[-1]
    sonlar = [44, 666, 768, 59]
    oxirgi_elementini_uchir(sonlar)
    print(sonlar)
    ```
    
    </details> 

16. `range` funsksiyasi nima qiladi?
    
    ```python 
    sonlar = list(range(1, 11 , 1))
    print(sonlar)
    # Javob:
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ```
    
17. `len` funksiyasi nima qiladi?
    
    ```python
    cars = ['Nexia', 'Gentra', 'Kobalt', 'Spark']
    print(len(cars))
    # Javob: 4
    ```

