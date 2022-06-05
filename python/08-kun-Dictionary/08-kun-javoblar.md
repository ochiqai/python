## Problem solving

1. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`. `value`si 10 da kichik bo'lgan dikshnri
elementlarini chiqaring.

      <details> <summary>Javob</summary>
        
      ```python
      harflar_soni = {'a': 15, 'b': 2, 'c': 6, 'd': 19}
      for key, value in harflar_soni.items():
          if value < 10:
              print(f"{key} : {value}")
      ```    
      
      </details> 

2. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`. `value`si 10 da kichik bo'lgan dikshnri
elementlar sonini toping. 

      <details> <summary>Javob</summary>
        
      ```python
         harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}
         soni = 0
         for key, value in harflar_soni.items():
             if value < 10:
                soni = soni + 1
         print(soni)
      ```    
      
      </details> 

3. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`. `value`si 10 da kichik bo'lgan dikshnri
elementlarini ko'paytmasini toping.

      <details> <summary>Javob</summary>
        
      ```python
      harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}
      kopaytma = 1
      for key, value in harflar_soni.items():
          if value < 10:
              kopaytma = kopaytma * value
      print(kopaytma)
      ```    
      
      </details> 

4. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`. `value`si 10 da kichik bo'lgan dikshnri
elementlari yig'indisini toping.

      <details> <summary>Javob</summary>
        
      ```python
      harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}
      yigindi = 0
      for key, value in harflar_soni.items():
          if value < 10:
              yigindi = yigindi + value
      print(yigindi)
      ```    
      
      </details> 

5. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`.   `'b'` ni o'chiring va 
qolganlarini konsolga chiqaring.

      <details> <summary>Javob</summary>
        
      ```python
      harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}
      del harflar_soni['b']
      print(harflar_soni)
      ```    
      
      </details> 

6. `harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}`.   `'d'` ni 29 ga o'zgartiring.

      <details> <summary>Javob</summary>
        
      ```python
      harflar_soni = {'a': 15, 'b': 2, 'c':6, 'd': 19}
      harflar_soni['d'] = 29
      print(harflar_soni)
      ```    
      
      </details> 

7. `a = "aaaabbbbcccdd"` har bir harf necha marta ishtirok etganini toping.

      <details> <summary>Javob</summary>
        
      ```python
      from collections import Counter
   
   
      a = "aaaabbbbcccdd"
      print(Counter(a))
      ```    
      
      </details> 