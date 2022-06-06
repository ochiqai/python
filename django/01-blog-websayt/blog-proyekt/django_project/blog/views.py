from django.shortcuts import render
from django.http import HttpResponse

xabarlar = [
    {
        'muallif': 'Ulugbek',
        'sarlavha': 'Toshkent haqida',
        'matn': 'Toshkent Uzbekistanni poytaxti',
        'sana': 'may 28, 2022'
    },
    {
        'muallif': 'Orif',
        'sarlavha': 'Samarkand haqida',
        'matn': 'Samarkand Uzbekistanni shaharchasi',
        'sana': 'may 29, 2022'
    }
]


def home(request):
    context = {
        "xabarlar":xabarlar
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html",{'title':" ochiqai"})


def ochiqai(request):
    return HttpResponse('<h1>Ochiq AI ga xush kelibsiz! </h1>')