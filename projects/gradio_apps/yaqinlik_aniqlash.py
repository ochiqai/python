import gradio as gr
import cv2

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

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq
)

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
    for kord in kordinatalar:
        x1 = int(kord["bbox"][0])
        y1 = int(kord["bbox"][1])
        x2 = int(kord["bbox"][2])
        y2 = int(kord["bbox"][3])
        yuz_i = rasm[y1:y2, x1:x2]
        yuz_i = cv2.resize(yuz_i, (50, 50))
        # matrixdan vectorga o'tdik
        piksellar_i = yuz_i.reshape((1, 3*50*50))
        piksellar.append([piksellar_i.tolist()[0], yuz_i])
    return piksellar

def yaqinlik(rasm1, rasm2):
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
    rasm1_koordinatalar_formati = yuz_aniqlagich_rasm1[0]
    yuz_aniqlagich_rasm2 = aniqlash(
        model=yuz_aniqlagich_modul,
        rasm=rasm2
    )
    rasm2_koordinatalar_formati = yuz_aniqlagich_rasm2[0]
    rasm1_embedding = embedding_modul.get(rasm1, rasm1_koordinatalar_formati)
    rasm2_embedding = embedding_modul.get(rasm2, rasm2_koordinatalar_formati)
    yaqinlik_embedding = vector_taq(rasm1_embedding.tolist(), rasm2_embedding.tolist())
    # --------------------piksel qismi ------------------
    piksellar_rasm_1 = piksel_olish(
        rasm=rasm1,
        kordinatalar=rasm1_koordinatalar_formati
    )
    piksellar_rasm_2 = piksel_olish(
        rasm=rasm2,
        kordinatalar=rasm2_koordinatalar_formati
    )
    yaqinlik_piksel = vector_taq(piksellar_rasm_1[0], piksellar_rasm_2[0])
    return yaqinlik_embedding, yaqinlik_piksel

with gr.Blocks() as demo:
    name = gr.Image(label="Birinchi rasm")
    name2 = gr.Image(label="Ikkinchi rasm")
    output = gr.Textbox(label="Embedding natijasi yaqinligi")
    output2 = gr.Textbox(label="Piksel nitijasi yaqinligi")
    greet_btn = gr.Button("Dasturni ishlating")
    greet_btn.click(fn=yaqinlik, inputs=[name, name2], outputs=[output, output2])

demo.launch()
