import gradio as gr
import cv2

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq, rasm_olish
)



# ---------- Dastur haqida -----------------------------------
# gradio orqali ikkita rasm kiritiladi.
# Rasmlarni embedding va piksellar orqali yaqinligini qaytaradi.
#-------------------------------------------------------------

#---------- Algoritim Embedding ------------------------------
# 1. Kerakli modullarni yuklab olamiz +
# 2. Kordinatalarni aniqlaymiz +
# 3. Embeddinglarni aniqlaymiz +
#-------------------------------------------------------------

#---------- Algoritim Piksellar ------------------------------
# piksellarni aniqlaymiz
#-------------------------------------------------------------



def piksel_olish(rasm, kordinatalar):
    """
    Berilgan rasmdan kordinatalar bo'yicha yuz rasmini qirqib,
    undan pilsellarni olib listga o'tkazamiz

    Parameters
    ----------
    rasm : numpy
    kordinatalar : list

    Returns
    -------
    list
        kordinatalar bo'yicha barcha yuzga tegishli piksellar
    """
    rasm = cv2.cvtColor(rasm, cv2.COLOR_BGR2RGB)
    piksellar = []

    kord = kordinatalar["bbox"]
    x1 = int(kord[0])
    y1 = int(kord[1])
    x2 = int(kord[2])
    y2 = int(kord[3])
    yuz = rasm[y1:y2, x1:x2]
    yuz = cv2.resize(yuz, (50, 50))
    # matrixdan vectorga o'tdik
    piksellar_i = yuz.reshape((1, 3*50*50))
    piksellar.append([piksellar_i.tolist()[0], yuz])
    return piksellar

def kordinata_formati(model, rasm):
    """
    Funksiya berilgan rasmning kordinatasini qaytaradi
    :param model:
        aniqlagich model (detection)
    :param rasm:
        rasm
    :return: list
        rasm kordinatasi
    """
    yuz_aniqlagich = aniqlash(
        model=model,
        rasm=rasm
    )
    kordinata = yuz_aniqlagich[0]
    return kordinata

def piksel(rasm, kordinatalar):
    """
    Funksiya rasm pikselini qaytaradi
    :param rasm:
        rasm
    :param kordinatalar:
        rasm kordinatasi
    :return:
        rasm pikseli
    """
    rasm_pikseli = piksel_olish(
        rasm=rasm,
        kordinatalar=kordinatalar
    )
    return rasm_pikseli

def dastur(rasm1, rasm2):
    """
    :param rasm1:
        gradio orqali birinchi rasm kiritiladi
    :param rasm2:
        gradio orqali ikkinchi rasm kiritiladi
    :return:
        embeddinglar va piksellar orqali ikkita rasmning yaqinligi
    """
    yuz_aniqlagich_modul = model_yuklash(
        turi="aniqlagich"
    )
    embedding_modul = model_yuklash(
        turi="embedding"
    )

    rasm1_koordinatalar_formati = kordinata_formati(yuz_aniqlagich_modul, rasm1)
    rasm2_koordinatalar_formati = kordinata_formati(yuz_aniqlagich_modul, rasm2)

    rasm1_embedding = embedding_modul.get(rasm1, rasm1_koordinatalar_formati)
    rasm2_embedding = embedding_modul.get(rasm2, rasm2_koordinatalar_formati)
    yaqinlik_embedding = vector_taq(rasm1_embedding.tolist(), rasm2_embedding.tolist())

#--------------------piksel orqali aniqlash------------------

    piksellar_rasm_1 = piksel(rasm1, rasm1_koordinatalar_formati)
    piksellar_rasm_2 = piksel(rasm2, rasm2_koordinatalar_formati)

    yaqinlik_piksel = vector_taq(piksellar_rasm_1[0][0], piksellar_rasm_2[0][0])
    return yaqinlik_embedding, yaqinlik_piksel

with gr.Blocks() as demo:
    kiritish1 = gr.Image(label="Birinchi rasm")
    kiritish2 = gr.Image(label="Ikkinchi rasm")
    chiqish1 = gr.Textbox(label="Embedding natijasi yaqinligi")
    chiqish2 = gr.Textbox(label="Piksel nitijasi yaqinligi")
    greet_btn = gr.Button("Dasturni ishlating")
    greet_btn.click(fn=dastur, inputs=[kiritish1, kiritish2], outputs=[chiqish1, chiqish2])
demo.launch()
