import gradio as gr
import cv2

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq, rasm_olish,
    piksel_olish
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



def kordinata_olish(model, rasm):
    """
    berilgan rasmning kordinatasini qaytaradi
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

def embedding_olish(rasm, model_aniq, model_emb):
    """

    Parameters
    ----------
    model
    kordinatalar

    Returns
    -------

    """
    koordinatalar = kordinata_olish(model_aniq, rasm)
    embedding = model_emb.get(rasm, koordinatalar)
    return embedding, koordinatalar

def yaqinlik_olish(rasm1, rasm2):
    """
    Parameters
    ----------
    rasm1: rasm
        matritsa [h, w, 3]
    rasm2: rasm
        matritsa [h, w, 3]
    Returns
    -------
    float
        yaqinlik qaytradi, 0.2
    """
    yuz_aniqlagich_modul = model_yuklash(
        turi="aniqlagich"
    )
    embedding_modul = model_yuklash(
        turi="embedding"
    )

    rasm1_embedding, rasm1_koordinatalar = embedding_olish(rasm1, yuz_aniqlagich_modul, embedding_modul)
    rasm2_embedding, rasm2_koordinatalar = embedding_olish(rasm2, yuz_aniqlagich_modul, embedding_modul)
    yaqinlik_embedding = vector_taq(rasm1_embedding.tolist(), rasm2_embedding.tolist())

    # --------------------piksel orqali aniqlash------------------

    rasm1_piksellar = piksel_olish(rasm1, rasm1_koordinatalar)
    rasm2_piksellar = piksel_olish(rasm2, rasm2_koordinatalar)
    yaqinlik_piksel = vector_taq(rasm1_piksellar[0][0], rasm2_piksellar[0][0])

    return yaqinlik_embedding, yaqinlik_piksel

with gr.Blocks() as demo:
    gr.Markdown(
    """
    
    # Yuzlarni taqqoslash  
    <br>
    """
    )

    rasm1 = gr.Image(label="Birinchi rasm")
    rasm2 = gr.Image(label="Ikkinchi rasm")
    chiqish_embedding = gr.Textbox(label="Embedding natijasi yaqinligi")
    chiqish_piksel = gr.Textbox(label="Piksel nitijasi yaqinligi")
    greet_btn = gr.Button("Dasturni ishlating")
    greet_btn.click(fn=yaqinlik_olish, inputs=[rasm1, rasm2], outputs=[chiqish_embedding, chiqish_piksel]),


demo.launch()


