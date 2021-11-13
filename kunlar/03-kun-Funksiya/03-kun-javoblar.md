## Problem solving
1. `+` belgisini chiqaradigan funksiya yozing. Funksiya nomini `add` deb nomlang.
   <details><summary>Javob</summary>

     ```python
     def add():
         print("+")
     add()
     # +
     ```
    </details>

2. `horizontal` nomli funksiya yarating. Va u konsolga quyidagini chiqarsin
   ```commandline
    -------------------------
    ```
   <details><summary>Javob</summary>

     ```python
     def horizontal():
          print("-"*10)
     horizontal()
     #----------
     ```
    </details>
3. `vertical` nomli funksiya yarating. Va u konsolga quyidagini chiqarsin
    ```commandline
       |
       |
       |
       |
       |
     ```

   <details><summary>Javob</summary>

     ```python    
      def horizontal():
             print("|")
      horizontal()
     ```
    </details>
4. `deraza` nomli funksiya yarating. Va u konsolga quyidagini chiqarsin

    ```commandline
      +------+-------+
      |      |       |
      |      |       |
      +------+-------+
      |      |       |
      |      |       |
      +------+-------+
    ```
   <details><summary>Javob</summary>

    ```python
       def deraza():
           print('+------+-------+')
           print('|      |       |')
           print('|      |       |')
           print('+------+-------+')
           print('|      |       |')
           print('|      |       |')
           print('+------+-------+')
       deraza()
  </details>

   
5. `def` kalit so'zi nima uchun ishlatiladi?
   <details><summary>Javob</summary>

     ```python
        Yangi funksiya tuzish uchun
     ```
    </details>
6. Quyidagi programma natijasi nima bo'ladi?
    ```python
       def fred():
           print("Zap")
       def jane():
           print("ABC")
       jane()
       fred()
       jane()
   
       ABC
       Zap
       ABC
    ```
   <details><summary>Javob</summary>

    ```python
       ABC
       Zap
       ABC
    ```
7. `baholar` degan funksiya yarating. Va u uni ishlaganimizda, quyidagilarni chiqarsin.

    ```commandline
    Ism        Baho
    Ulugbek    3
    Nuriddin   5
  <details><summary>Javob</summary>

   ```python    
      def baholar():
          print("Ism       Baho")
          print("Ulugbek    3")
          print("Nuriddin   5")
    baholar()
   ```
  </details>
8. `chapga` degan funksiya yarating. U `<` ni qaytarsin. Keyin `o'ngga` degan funksiyani yarating, u `>` ni 
   qaytarsin. Shu ikki funksiyadan foydalanib, konsolga quyidagini chiqaring.
   
  ```commandline
    >
    >
    <
    >
    >
    > 
   ```
  <details><summary>Javob</summary>

   ```python
        def chapga():
            return '>'
        def ongga():
           return '<'
       print(ongga())
       print(ongga())
       print(chapga())
       print(ongga())
       print(ongga())
       print(ongga())
   ```
  </details>
 9. 1 dan 5 gacha sonlarni qaytaradigan funksiyalar qiling. Masalan: `bir`, `ikki`, ... `besh`.
     Va qyidagini ishlating.
   
```python         
    kup = bir() + ikki()
    print(kup)
```
Amin bo'lingki, konsolga natija 3 chiqsin. 
```commandline
    ----
    3
```
  <details><summary>Javob</summary>  
 
   ```python
      def bir():
          return 1
      def ikki():
          return 2
      def uch():
          return 3
      def tort():
          return 4
      def besh():
          return 5
      kup = bir() + ikki()
      print(kup) 
      # 3
   ```
  </details>

  
    


