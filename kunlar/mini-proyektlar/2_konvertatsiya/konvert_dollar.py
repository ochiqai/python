import urllib.request, urllib.parse, urllib.error
import ssl
import gradio as gr
import re


def dollar_kursi():
    """
    Ushbu funksiya dollar kursini https://daryo.uz/ saytga borib oladi va uni qaytaradi
    :return: kursni qaytaradi, turi haqiqiy son
    """
    # ushbu 3 qator, hozircha muhim emas. Ular netga bog'langanda
    # shunchaki malumot beradi
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # web address (url)
    url = "https://daryo.uz/"
    # web addressni ochish
    html = urllib.request.urlopen(url, context=ctx)
    # Ochilgan web adressni o'qish, odatdan ikkilik (binary) ko'rinishda bo'ladi
    html_och = html.read()
    # o'qilganni ikkilikdan stringga o'tkazish
    html_string = html_och.decode()

    # berilgan stringdan dollar kurisni topish
    # 1 usul: string funksiyalaridan foydalanib qilish
    # index = html_string.find("<strong>USD</strong><span>") #
    # kurs = float(html_string[index + len("<strong>USD</strong><span>"):index + len("<strong>USD</strong><span>") + 8])

    # 2-usul: regular ifodalardan foydalanib qilish
    lst = re.findall("USD</strong><span>([0-9.]+)", html_string)
    kurs = lst[0]
    return float(kurs)


def konvert(dollar):
    """
    Foydalanivchidan dollarni oladi, va uni so'mga o'tkazadi
    :param dollar: miqdor foydalanichni tomonidan. Masalan, 60
    :return: 2 ta qaytaradi: 1) kurs 2) jami
    """

    # joriy kursni olish
    _dollar_kursi = dollar_kursi()

    # joriy kurs bo'yicha, so'mga o'tkazish
    jami = dollar * _dollar_kursi

    return _dollar_kursi, jami

# Qora ekranda ishlatish
ulug = 50
_, som = konvert(50)
print(som)

# Gradioda ishlatish
iface = gr.Interface(fn=konvert, inputs=["number"], outputs=["number", "number"])
iface.launch(share=True)