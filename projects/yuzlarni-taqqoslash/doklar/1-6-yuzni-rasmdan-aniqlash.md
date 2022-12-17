## Yuzlarni rasmdan aniqlash

<!-- TOC -->
  * [Yuzlarni rasmdan aniqlash](#yuzlarni-rasmdan-aniqlash)
    * [Foydalanadigan kutibxonalar](#foydalanadigan-kutibxonalar)
    * [Model joyini aniqlash](#model-joyini-aniqlash)
    * [Rasmni o'qib olish](#rasmni-oqib-olish)
    * [Yuz qismlari va koordinatalarini aniqlash](#yuz-qismlari-va-koordinatalarini-aniqlash)
    * [Aniqlangan yuzlarni chizib olish](#aniqlangan-yuzlarni-chizib-olish)
<!-- TOC -->

### Foydalanadigan kutibxonalar

* Kerakli kutibxonalarni yuklab (`import`) olamiz.

    ```python
    import cv2 # rams ustida amallar uchun
    import insightface # yuzni aniqlash uchun
    from insightface.app.common import Face # yuz klassi uchun
    from insightface.app import FaceAnalysis # yuz uchun
    import matplotlib.pyplot as plt # vizualizatsiya uchun
    ```

### Model olish va joyini aniqlash

Biz foydalanadigan modul yuz qismini aniqlab beradigan funksiya kabi tushunsak bo'ladi.
Avvalo quiyidagi klassni chaqiramiz

  ```python
  app = FaceAnalysis()
  ```
Bu kod bir nechta modellarni yuklaydi. Shundan yuzni aniqlaydigan (`detection`) model joyini bilib olamiz:

  ```shell
  ...
  find model: /home/nuriddin/.insightface/models/buffalo_l/det_10g.onnx detection [1, 3, '?', '?'] 127.5 128.0
  ...
  ``` 

Yuqorida `detection` qismida `model joyi` berilgan. Va uni `model_joyi` o'zgaruvchisiga yuklaymiz:

  ```python
  model_joyi = "/home/nuriddin/.insightface/models/buffalo_l/det_10g.onnx"
  ```

Model joyini aniqlab oldik, endi uni `insightface` orqali chaqirib olamiz va modelimizni 
`yuz aniqlagich` o'zgaruvchisiga yuklaymiz.

  ```python
  yuz_aniqlagich = insightface.model_zoo.get_model(model_joyi)
  ```
Rasmni `640 vs 640` o'lchamga keltirib olamiz. Bunda ixtiyoriy kiritilgan rasm (640, 640) o'lchamga o'tkaziladi.

  ```python
  yuz_aniqlagich.prepare(ctx_id=0, input_size=(640, 640))
  ```
  
### Rasmni o'qib olish

* Aytaylik bizda rasm bor, `uz_prez.jpg`. `cv2` kutubxonasining `imread` funksiyasi orqali o'qib olamiz.

  ```python
  rasm_joyi = "rasmlar/uz_prez.jpg"
  rasm = cv2.imread(rasm_joyi)
  ```
  * Rasmni `print` orqali chiqarib ko'rsak, uni [0, 255] oraliqdagi sonlardan tashkil topganini ko'rishimiz mumkin.

### Yuz qismlari va koordinatalarini aniqlash

* `yuz_aniqlagich` modelining `detect` funksiya orqali yuz qismlari, koordinatalarini aniqlab olamiz.

  ```python
  yuz_koordinatalari, yuz_qismlari = yuz_aniqlagich.detect(rasm)
  ```
  
* Endi biz yuz koordinatalarini o'zgartirib olishimiz kerak. Buning uchun yangi o'zgaruvchi yaratib olamiz.

  ```python
  yuz_koordinatalari_uzgartirilgan = []
  ```

*  Yuz koordinatalari qanday berilganini tushunib olishimiz kerak

    ```python
    print(yuz_koordinatalari.shape)
    ```
    ```commandline
    (19, 5)
    ```
* `shape` funsksiya orqali nimalar mavjudligini bilib oldik. `19` rasmlar sonini anglatadi, 
  `5` esa nimani anglatishini tushunib olishimiz uchun, birinchi rasmni o'zini chiqarib ko'raylik.

  ```shell
  print(yuz_koordinatalari[0,:])
  ```
  ```commandline
  array([479.86224  ,  41.49642  , 578.2567   , 165.86041  ,   0.9085071],
        dtype=float32)
  ```

* Yuqorida dastlabki 4 ta son birinchi yuzning koordinatalarini anglatadi. 
`0.9085071` bu sonni esa koordinatalarning ishonchlilik darajasi deb qarasak bo'ladi. 

* Hozirgacha bo'lgan malumotlarni `Face` klasiga mutonosib qilishimiz kerak, chunki vizualizatsiya qilishimiz uchun
kerak bo'ladi:

    ```python
    for i in range(yuz_koordinatalari.shape[0]):
        koordinata = yuz_koordinatalari[i, 0:4]
        ishonch = yuz_koordinatalari[i, 4]
        yuz_qism = yuz_qismlari[i]
  
        yuz = Face(bbox=koordinata, kps=yuz_qism, det_score=ishonch)
        yuz_koordinatalari_uzgartirilgan.append(yuz)
    ```
    
    * `yuz_koordinatalari.shape[0]` - bu yuzlar soniga qarab son qaytaradi (4 ta yuzni aniqlasa `4` qaytaradi va h.k).
    * `koordinata = yuz_koordinatalari[i, 0:4]` - rasmdagi yuz koordinatalar qismi.
    * `ishonch = yuz_koordinatalari[i, 4]` - ishonchlilik qismi. (0.9085071)
    * `koordinata`, `ishonch` va `yuz_qismlari` ni aniqlab olib `Face` klassiga yozib olib, uni `yuz` o'zgaruvchisiga yuklaymiz.
    * `yuz_koordinatalari_uzgartirilgan` listiga `append` orqali har bir `yuz`ni qo'shib boramiz.

### Aniqlangan yuzlarni chizib olish

* Rasmdan yuzlarni aniqlab bo'lgandan keyin, vizualizatsiya qilamiz. Bunda yuz va yuz qism tasvirlanadi. 

  ```python
  chizilgan_rasm = app.draw_on(rasm, yuz_koordinatalari_uzgartirilgan)
  ```
  * `app.draw_on` bizga aniqlangan yuzlarni chizib, rasm ko'rinishida qaytaradi.

  * Rasmni `rgb`ga o'tkazib olib, `matplotlib` yordamida `chizilgan_rasm`ni ko'rishimiz mumkin.

  ```python
  chizilgan_rasm = cv2.cvtColor(chizilgan_rasm, cv2.COLOR_BGR2RGB)
  plt.imshow(chizilgan_rasm)
  plt.show()
  ```
  
* Dasturning umumiy ko'rinishi:

  ```python
  import cv2
  import insightface
  from insightface.app.common import Face
  from insightface.app import FaceAnalysis
  import matplotlib.pyplot as plt
  
  
  app = FaceAnalysis()
  # /home/ochiqai/.insightface/models/buffalo_l/det_10g.onnx
  
  model_joyi = "/home/ochiqai/.insightface/models/buffalo_l/det_10g.onnx"
  yuz_aniqlagich = insightface.model_zoo.get_model(model_joyi)
  # (640, 640) ixtiyoriy kiritilgan rasmni ushbu o'lchamga o'tkazadi.
  yuz_aniqlagich.prepare(ctx_id=0, input_size=(640, 640))
  
  rasm_joyi = "rasmlar/uz_prez.jpg"
  rasm = cv2.imread(rasm_joyi) # [0, 255]
  
  yuz_koordinatalari, yuz_qismlari = yuz_aniqlagich.detect(rasm)
  
  yuz_koordinatalari_uzgartirilgan = []
  for i in range(yuz_koordinatalari.shape[0]):
      koordinata = yuz_koordinatalari[i, 0:4]
      ishonch = yuz_koordinatalari[i, 4]
      yuz_qism = yuz_qismlari[i]
  
      yuz = Face(bbox=koordinata, kps=yuz_qism, det_score=ishonch)
      yuz_koordinatalari_uzgartirilgan.append(yuz)
  
  chizilgan_rasm = app.draw_on(rasm, yuz_koordinatalari_uzgartirilgan)
  chizilgan_rasm = cv2.cvtColor(chizilgan_rasm, cv2.COLOR_BGR2RGB)
  plt.imshow(chizilgan_rasm)
  plt.show()
  ```
  
* Dasturni ishlatamiz, va natijani ko'rishimiz mumkin.

  <p align="center">
      <img src="./rasm/rasmdan_yuzni_aniqlash/rasmdan_yuzni_aniqlash.png">
  </p>

