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

def yaqinlik(rasm1_joy, rasm2_joy):
    """

    :param rasm1: str
        rasm joyi. masalan: home/1.jpg
    :param rasm2:
    :return:
    """
    rasm1 = rasm_olish(rasm1_joy)
    rasm2 = rasm_olish(rasm2_joy)
    yuz_aniqlagich_modul = model_yuklash(
        turi="aniqlagich"
    )
    embedding_modul = model_yuklash(
        turi="embedding"
    )
    yuz_aniqlagich_rasm1 = aniqlash(
        model=yuz_aniqlagich_modul,
        rasm=rasm1
    )
    yuz_aniqlagich_rasm2 = aniqlash(
        model=yuz_aniqlagich_modul,
        rasm=rasm2
    )

    rasm1_koordinatalar_formati = yuz_aniqlagich_rasm1[0]
    rasm2_koordinatalar_formati = yuz_aniqlagich_rasm2[0]

    rasm1_embedding = embedding_modul.get(rasm1, rasm1_koordinatalar_formati)
    rasm2_embedding = embedding_modul.get(rasm2, rasm2_koordinatalar_formati)
    yaqinlik_embedding = vector_taq(rasm1_embedding.tolist(), rasm2_embedding.tolist())

    # # --------------------piksel qismi ------------------
    piksellar_rasm_1 = piksel_olish(
        rasm=rasm1,
        kordinatalar=rasm1_koordinatalar_formati
    )
    piksellar_rasm_2 = piksel_olish(
        rasm=rasm2,
        kordinatalar=rasm2_koordinatalar_formati
    )
    yaqinlik_piksel = vector_taq(piksellar_rasm_1[0][0], piksellar_rasm_2[0][0])
    return yaqinlik_embedding, yaqinlik_piksel

# rasm1 = "/home/ochiqai/work/ochiqai/git/python/projects/gradio_apps/rasmlar/1.jpg"
# rasm2 = "/home/ochiqai/work/ochiqai/git/python/projects/gradio_apps/rasmlar/1.jpg"
#
# print(yaqinlik(rasm1, rasm2))

with gr.Blocks() as demo:
    name = gr.Image(label="Birinchi rasm")
    name2 = gr.Image(label="Ikkinchi rasm")
    output = gr.Textbox(label="Embedding natijasi yaqinligi")
    output2 = gr.Textbox(label="Piksel nitijasi yaqinligi")
    greet_btn = gr.Button("Dasturni ishlating")
    greet_btn.click(fn=yaqinlik, inputs=[name, name2], outputs=[output, output2])

demo.launch()
