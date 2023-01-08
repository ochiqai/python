import gradio as gr
import cv2
import math

# ------------------------

def ildiz(x):
    """
    Sonni ildizini oladi, masalan: 49 bersak, 7 qaytadi
    """
    return math.sqrt(x)


def surat(a, b):
    """
    a va b listlarni olib elementlarini bir biriga
    ko'paytirib qo'shamiz.

    Parameters
    ----------
    a : list
    b : list

    Returns
    -------
    float
        yig'indi
    """
    kasr_surati, i = 0, 0
    while i < len(a):
        kasr_surati += (a[i] * b[i])
        i += 1
    return kasr_surati


def maxraj(a, b):
    """
    a va b listni olib, har birining modulini olib, ularni
    ko'paytmasini qaytaramiz
    Parameters
    ----------
    a : list
    b : list

    Returns
    -------
    float
        ko'paytma
    """
    i = modul_a = modul_b = 0
    while i < len(a):
        modul_a += (a[i] * a[i])
        modul_b += (b[i] * b[i])
        i += 1

    modul_a = ildiz(modul_a)
    modul_b = ildiz(modul_b)
    kasr_maxraji = modul_a * modul_b
    return kasr_maxraji


def vector_taq(a, b):
    """
    Bu funksiya 2 ta listni taqqoslaydi. Taqqoslash kosinus teoremasi
    asosida. Yoki  boshqacha nomda kosinus o'xshashlik:
    https://en.wikipedia.org/wiki/Cosine_similarity

    Parameters
    ----------
    a : list
        birinchi list
    b : list
        ikkinchi list

    Returns
    -------
    float
        berilgan vektorlar yaqinligini qaytaradi
    """

    if len(a) == len(b):
        yaqinlik = surat(a, b) / maxraj(a, b)
        return yaqinlik
    else:
        print("Elementlar soni teng bo'lish kerak!")

# --------------------------

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, piksel_olish
)

# -----------------------------------------------------------------
# dastur jarayoni
# ---------- Algoritm --------------------
# 1. yuz aniqlagich modelini yuklaymiz
# 2. rasm kordinatalarini aniqlab olamiz
# 3. embedding modelini yuklaymiz
# ----------------------------------------

def dastur(baza_rasm_1, baza_rasm_2, baza_rasm_3, test_rasm):

    aniqlagich_model = model_yuklash(turi="aniqlagich")
    embedding_model = model_yuklash(turi="embedding")
    kordinatalar_format = aniqlash(
        model=aniqlagich_model,
        rasm=baza_rasm_1
    )
    baza_embedding_1 = embedding_model.get(baza_rasm_1, kordinatalar_format[0])

    kordinatalar_format = aniqlash(
        model=aniqlagich_model,
        rasm=baza_rasm_2
    )
    baza_embedding_2 = embedding_model.get(baza_rasm_2, kordinatalar_format[0])

    kordinatalar_format = aniqlash(
        model=aniqlagich_model,
        rasm=baza_rasm_3
    )
    baza_embedding_3 = embedding_model.get(baza_rasm_3, kordinatalar_format[0])

    kordinatalar_format_test = aniqlash(
        model=aniqlagich_model,
        rasm=test_rasm
    )
    test_embedding = embedding_model.get(test_rasm, kordinatalar_format_test[0])

    baza_list = [baza_embedding_1, baza_embedding_2, baza_embedding_3]

    yaqinlik = vector_taq(test_embedding.tolist(), baza_list[0].tolist())
    if yaqinlik > 0.1:
        return "Bu O'zbekiston prezidenti Shavkat Mirziyoyev"
    yaqinlik = vector_taq(test_embedding.tolist(), baza_list[1].tolist())
    if yaqinlik > 0.1:
        return "Bu Rassiya prezidenti Vladimir Putin"
    yaqinlik = vector_taq(test_embedding.tolist(), baza_list[2].tolist())
    if yaqinlik > 0.1:
        return "Bu Amerika prezidenti Joe Biden"
    else:
        return "Bu inson prezident emas"

# ------------------------------------------------------------------------
# gradio

with gr.Blocks() as demo:
    name1 = gr.Image(label="Baza rasm 1")
    name2 = gr.Image(label="Baza rasm 2")
    name3 = gr.Image(label="Baza rasm 3")
    name4 = gr.Image(label="Test rasm")
    output_text = gr.Textbox(label="Malumot")
    tugma = gr.Button("Bosing")
    tugma.click(fn=dastur, inputs=[name1, name2, name3, name4], outputs=output_text)

demo.launch(share=True)

# -------------------------------------------------------------------------



