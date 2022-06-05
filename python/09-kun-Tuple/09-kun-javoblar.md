##  Problem solving

1. `m = 'A', n = 'B'` o'zgaruvchi qiymatlarini almashtiring.
   
   <details> <summary>Javob</summary>
    
    ```python
    m = 'A'
    n = 'B'
    print('m =',m)
    print('n =',n)
    
    print("--------------")
    
    m, n = n, m
    print('m =',m)
    print('n =',n)
    
    # Javob:
    # m = A
    # n = B
    # --------------
    # m = B
    # n = A
    ```
    
    </details> 
2. `x = ('1', '2', '3', '4')` `for` dan foydalanib element qiymatlarini konsolga chiqaring.
      
   <details> <summary>Javob</summary>
    
    ```python
    x = ('1', '2', '3', '4')
    for c in x:
        print(c)
    # Javob:
    # 1
    # 2
    # 3
    # 4
    ```
    
    </details>
   
3. `x = ('1', '2', '3', '4')` `for` dan foydalanib element sonini chiqaring.
   
   <details> <summary>Javob</summary>
    
    ```python
   x = ('1', '2', '3', '4')
   soni = 0
   for c in x:
       soni = soni + 1
   print(soni)
   # Javob:
   # 4
    ```
    
   </details>
   
4. `tuple()` funksiyasi nima qiladi?