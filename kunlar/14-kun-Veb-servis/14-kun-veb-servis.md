# Veb servislardan foydalanish

O'tgan kuni biz HTTP orqali malumotlarni olish va ulardan malumotlarni ajratib olishni ko'rdik.
Bu narsalar qiyinmasligini ham ko'rdik. 

Endi qanday qilib bu malumotlarni olib boshqa maxsus formatlarga o'tkazishni ko'ramiz. Sababi tarmoqda 
ishlaganimizda bizga maxsus formatlar kerak bo'ladi. Bu formatlar malumotlar almashuvini osonlashtiradi.

Umuman olganda, ikkita keng foydalaniladigan format turi mavjud:
- XML (eXtensible Markup Language): uzoq yillardan beri foydalanib kelinayotgan turi.   
- JSON (JavaScript Object Notation): agar programmalar bir-biri bilan dictionary, list va shunga o'xshash 
 malumotlarni almashganda foydaliniladi.



## XML

Masalan oddiy quyidagi teksnit `.txt` formatga yozsak, oddiy qilib quyidagicha yozamiz:

```commandline
Ulug'bek 1997 yilda tug'ilgan. Uning telefon nomeri +998930751753
```

Mana shu malumotni XML formatda quyidagicha yozishimiz mumkin,

```xml
<odam>
    <ismi>Ulug'bek</ismi>
    <yili>1997</yili>
    <tel_nomer type="intl">
        +998930751753
    </tel_nomer>
</odam>
```

Ko'rinib turganidek bunda malumot ancha o'zgarib ketdi. Umuman olganda strukturaga ega bo'ldi. 
Yuqorida oddiy tekstda esa shunchaki tekst. 

Endi, yozilishiga nazar solsak. XMLda _element_ tushunchasi mavjud. Bundga misol sifatida 
`<odam>` ochilish tagi deb ataladi va `</odam>` yopilish tagi deb ataladi. Tagni nomi bu yerda **odam**.
`<odam></odam` bu bitta element hisoblanadi. Har bir element biror tekst, attribute va bothqa ichma-ich elementlardan 
tashkil topadi. Masalan, `<odam></odam>` 3 ta ichki elementdan tashkil topgan: `<ism>, <yili> <tel_nomer>`.
`<ismi>` tagida _Ulug'bek_ degan tekst yozilgan.

XML dokumentni daraxt strukturasi yordamida tasvirlash qulay. Shunda, XML eng yuqorida joylashgan element (bu misolda: `odam`), 
va boshqa taglardan yani _bolalar_ (bu misolda: `ismi, yili, tel_nomer`) tashkil topadi. Eng yuqoridagi elementni 
'ona' yoki inglizchasiga parent deb ataladi. Va quyidagicha tasvirlashimiz mumkin:

<p align="center">
    <img src="./imgs/daraxt_xml.png" width=900>
</p>


## XMLdan malumotlarni olish

Quyidagi programmada, qanday qilib XMLdan malumotlarni olish ko'rsatilgan. 

```python
import xml.etree.ElementTree as ET
malumot = '''
<odam>
    <ismi>Ulug'bek</ismi>
    <yili>1997</yili>
    <tel_nomer type="intl">
        +998930751753
    </tel_nomer>
</odam>'''

daraxt = ET.fromstring(malumot)
print('Ismi:', daraxt.find('ismi').text)
print('Tel nomeri:', daraxt.find('tel_nomer').text.strip())
```

Birinchi biz XML dan malumot olish uchun yaratilgan `ElementTree` bibliotekasini chaqiramiz. Keyin xml `malumot`
hosil qilamiz. `'''` belgisi stringlarni bir necha qatorda yozishga ruhsat beradi. `"""` dan foydalansa ham bo'ladi. 
Keyin uni `fromstring` metodi orqali yuqorida aytib o'tilgan daraxt strukturasiga o'tkazib olamiz.
Sababi, XML daraxt strukturasida bo'lsa, biblioteka orqali bir necha amallarni oson bajarishimiz mumkin. 
Masalan, `find` metodi daraxtdan kerakli tagga mosini ajratib qaytaradi. 
`daraxt.find('ismi').text` : `daraxt`dan `ismi` tagini qidirib uni tekst (text) ni olib chiqarayapmiz.

Natija,

```commandline
Ismi: Ulug'bek
Tel nomeri: +998930751753
```


## XML elementlarini olish

Ko'pincha XML bir necha elementlardan tashkil topadi. Ularni protsess qilish uchun `loop` dab foydalanamiz.
Quyidagi programmada oilaning bolalar tagidagi elementlarni birin ketin chiqaradi.

```python
import xml.etree.ElementTree as ET
input = '''
<oila>
    <bolalar>
        <bola>
            <nomer>1</nomer>
            <ism>Ali</ism>
        </bola>
        <bola>
            <nomer>2</nomer>
            <ism>Vali</ism>
        </bola>
    </bolalar>
</oila>
'''
bolalar = ET.fromstring(input)
lst = bolalar.findall('bolalar/bola')
print('Bolalar soni:', len(lst))
print('-----------------------')
for element in lst:
    print('Ism', element.find('ism').text)
    print('Nomer', element.find('nomer').text)
```


`findall` metodi XMLdan `bola` tagiga oidlarini oladi va ularni listga yig'ib qaytaradi. Keyin, loop orqali
xar bir bola elementining `ism` va `nomer` tekstlarini chiqarayapmiz. 


Natija,

```commandline
Bolalar soni: 2
-----------------------
Ism Ali
Nomer 1
Ism Vali
Nomer 2
```

Muhim! 
> `findall` metodiga top elementni qo'yish kerak emas. Yani `'oila/bolalar/bola'` mumkin emas. Yana, 
> boshqa hamma kerakli taglarni qo'yish shart, masalan `'bola'` deb qo'yich mumkin emas. Aks holda to'g'ri
> malumot qaytarilmaydi.



## JSON

JSON ham XML kabi format hisoblanadi. Masalan quyida, yuqorida XML da yozilganning JSON varianti berilgan.

```json
{
 "ismi": "Ulug'bek",
 "yili": "1997",        
 "tel_nomer": "+998930751753"         
}
```

Bir necha farqini ko'rishimiz mumkin

- Taglar yo'q va ular `{}` qavslari bilan almashtirilgan
- JSONda faqat `key-value` juftligi bor, xuddi `dictionary`ga o'xshab
- Umuman olganda, JSON strukturasi ancha XMLnikidan osonroq
- JSON `key-value` juftligida bo'lganligi uchun, Pythondagi dictionary va list lar bilan to'gridan to'g'ri
  ishlayveradi. Bu esa programmistlar uchun juda qulay.

JSON XMLdan foydalanish jihatidan ancha ommalashgan.



## JSON dan malumot olish

JSONda malumot hosil qilish dictionary va listlarning kombinatsiyasi tufayli bo'ladi. Masalan, quyidagi JSON
malumot berilgan

```python
malumot = '''
[
    {   
        "nomer": "1",
        "ism": "Ali"    
    },
    {   
        "nomer": "2",
        "ism": "Vali"    
    },
]
'''
```

Demak bizda hozir bir necha `dictionary`lardan tashkil topgan list mavjud - JSON.

Quyidagi programmada, `json` bibliotekasidan foydalanib yuqoridagi `malumot` ni olamiz va uni o'qiymiz. 
Bu kodni yuqorida biz qilgan XML malumotni o'qib uni o'qishga solishtirishingiz mumkin. JSONda kod ancha sodda 
ko'rinadi.

```python
import json

malumot = '''
[
    {   
        "nomer": "1",
        "ism": "Ali"    
    },
    {   
        "nomer": "2",
        "ism": "Vali"    
    }
]
'''
olingan_data = json.loads(malumot)
print('Soni:', len(olingan_data))
print('------------------------')
for element in olingan_data:
    print('Ism: ', element['ism'])
    print('Nomeri: ', element['nomer'])
```

Bu yerda eng muhim eslab qolinishi kerak bo'ladigan metod `json.loads` hisoblanadi. Bu metodga malumot berilganda
u malumotni protsess qiladida Python list qaytaradi. Listning xar bir elementi esa dictionary bo'ladi. 
Listning olganimizdan so'ng undagi har bir elementni `for loop` orqali o'qib chiqarayapmiz.

Natija, 

```commandline
Soni: 2
------------------------
Ism:  Ali
Nomeri:  1
Ism:  Vali
Nomeri:  2
```

## API 

Biz bilamizki ikkita programma o'rtasida malumot almashish uchun HTTPdan foydalanamiz.
Sodda yoki murakkab malumotlarni yuborish va qabul qilish uchun esa XML va JSON 
formatlaridan foydalanishni ham bildik. 

Endi, ushbu texnikalardan foydalanib programmalar o'rtasida shartnoma (kontrakt) tuzishni boshlaymiz.
Programmadan programmaga kontrak atamasi umumiy olganda API deb ataladi. 
API bu Application Programming Interface - Programma Dasturlash Interfeysi. Biz API dan foydalanganimizda,
bitta programma bir necha servislar taqdim qiladi. Servislardan qanday foydalanish haqida yo'l yo'riqlar 
ham beriladi. Va bu servislar boshqa programmalar tomonidan foydalaniladi.

Qachonki biz programma tuzsak va programmamiz boshqa programmalar servisidan foydalansa, bunday usulda 
qilingan programmani servisga oid arxitektura deb ataymiz (inglizcha Servise-oriented architechture), 
qisqacha qilib SOA usuli deb ataladi. SOA usulida qilinga programma boshqa programmalar servisidan 
foydalanadi. SOA usulida qilinmagan programmalar esa boshqa programma servislaridan foydalanmaydi balki 
hamma funsiyalar o'zi mujassamlashgan.


SOA usulida qilingan programmalarni biz internetda juda ko'p ko'rishimiz mumkin. Aytaylik biz bitta 
veb sahifadan ham dollar kursini ham ob-havo malumotlarini ham yangiliklarni ko'rishimiz mumkin. Bunda
har bir malumot uch joydan API orqali keladi. Yani, uchta kompaniya bor biri dollar kursi haqida malumot
beruvchi servis qilgan, ikkinchisi, obhavo malumoti uchun servis yaratgan. Uchunchisi, yangiliklar servisini
taqdim qilgan. Biz shunday programma tuzganmizki, uchala servisdan foydalanib bitta veb sahida hammasini
ko'rishimiz mumkin. Quyida figuraga qarang.


<p align="center">
    <img src="./imgs/api.png" width=900>
</p>
 
Qachonki programma bir necha servislarini API orqali taqdim qilsa, bu servislarni biz **`veb servislar`** deb ataymiz.



## Xavfsizlik va APIdan foydalanish

Hozirda keng tarqalganki, API dan foydalanish uchun API kalit kerak bo'ladi. Chunki, API qilganlar 
hizmatdan kim foydalanayapti, qancha foydalanyapti degan savollarga qiziqadi. API lar pulli yoki tekin 
bo'lishligi mumkin. Yoki tekin bo'lib qandaydir cheklovlar bo'lishligi mumkin. Masalan Google geocoding veb servisi tekin, 
lekin bu degani odamlar xoxlaganicha foydalandi degani emas - yo'l yo'riqlari mavjud.

Bazi paytlarda xavfsizlikni oshirishga to'gri keladi. O'shaning uchun kriptografiya asosida maxsus kuchli
texnologiyalar yaratilgan. Internetda keng qo'llaniladiganlaridan biri [www.oauth.net](www.oauth.net). 
OAuth dan foydalanish uchun bir necha bibliotekalar mavjud, ular haqida ham [www.oauth.net](www.oauth.net)dan 
malumot topishingiz mumkin.




## Eslatma
- **API**: Application Program Interface - ikkita programma komponenetlarining qanday qilib bog'lanishi haqida 
   kontrakt/nizom.
- **XML**: Interda malumot almashish uchun faydalaniladigan format
- **JSON**: Interda malumot almashish uchun faydalaniladigan format 
- **SOA**: Service-oriented architechture. Programmaning bazi qismlar internetdaga boshqa programmalar 
    bilan malumot almashishi
- **ElementTree**: XML malumotni pars qilish uchun Python biblioteka
- **json**: json formatidagi malumotni pars qilish uchun Python biblioteka





