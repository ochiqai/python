from django.shortcuts import render
from django.http import HttpResponse

bloglar = [
    {
        'muallif': 'Nuriddin',
        'sarlavha': 'Programma nima?',
        'matn':
            """Programma bu aniq bir muammoni yechish uchun ko'rsatmalar ketma keltligidir. 
                Programmalash esa mana shu ko'rsatmalarni ishlab shiqishdir. Shuning uchun, 
                programmist uchun eng muhim kerak bo'ladigan mahorat bu berilgan muammoni hal qilish ketma-ketligini 
                o'ylab topish. Yechim ko'rsatmalari aniq va to'g'ri bo'lishi shart. Bu mahorat, programma tuzish orqali 
                shakllantiriladi. Qancha ko'p programma tuzsangiz shuncha yaxshi, ko'p o'qish yoki kino ko'rish bilan emas :).
            """,
        'sana': '28 Avgust, 2021'
    },
    {
        'muallif': 'Muhriddin',
        'sarlavha': 'Funksiya haqida',
        'matn':
            """Biz programma ko'rsatmalardan tashkil topishini bildik. Kattaroq programma tuzayotganimizda, ko'rsatmalar 
                ko'payib ketadi. Ularni ixchamlashtirish uchun, soddalashtirish uchun biron nima qilishimiz kerak.
                Tasavvur qiling bir 999 varaqli kitob bor. Uning na mundarijasi, na bobi bor. Na bo'limi, na varaq 
                nomeri bor. Boshidan oxirigacha hammasi tekst. Kitobni o'qiyotgan odam o'qib ketaveradi. Lekin u 
                yerdan qaysi betga kelgani, o'qiyotgan joyi asosan nima uchunligi bilmay o'qib ketaveradi. Bu 
                kitobxonga juda katta qiyinchilik bo'ladi. Mana shu va boshqa muammolarni hal qilish uchun 
                kitoblarda quyidagilar qilingan:
            """,
        'sana': '17 Sentabr 2021'
    }
]


def home(request):
    kontekst = {
        "bloglar": bloglar
    }
    return render(request, "blog/home.html", kontekst)

def about(request):
    return render(request, "blog/about.html", {'title': "ochiqai"})


def ochiqai(request):
    return HttpResponse('<h1>Ochiq AI ga xush kelibsiz! </h1>')

