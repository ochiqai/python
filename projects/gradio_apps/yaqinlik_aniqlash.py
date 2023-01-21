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


def embedding_olish(rasm, model_aniq, model_emb):
    """
    Rasmdan yuz kordinatalari va embeddinglarini qaytaradi
    """
    koordinatalar = aniqlash(model_aniq, rasm)[0]
    embedding = model_emb.get(rasm, koordinatalar)
    return embedding, koordinatalar

def yaqinlik_olish(rasm1, rasm2):
    """
    2 ta rasm o'rtasidagi yaqinlik
    Parameters
    ----------
    rasm1: np, uint8
        matritsa [h, w, 3]
    rasm2: np, uint8
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


