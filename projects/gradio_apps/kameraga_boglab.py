import cv2
import gradio as gr
import numpy as np

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, chizish, vector_taq
)
#
# aniqlagich_model = model_yuklash(turi="aniqlagich")
# embedding_model = model_yuklash(turi="embedding")
#
# baza_rasm = cv2.imread("/home/ubuntuuser/proyektlar/python/projects/gradio_apps/refaktor/rasmlar/Orif.png")
#
# baza_rasm_kordinata = aniqlash(aniqlagich_model, baza_rasm)
# baza_embedding = embedding_model.get(baza_rasm, baza_rasm_kordinata)
#
# #
rasm1 = "/home/ubuntuuser/proyektlar/python/projects/gradio_apps/refaktor/rasmlar/Nuriddin.jpg"
def embedding_olish(rasm, model_aniq, model_emb):
    """
    Rasmdan yuz kordinatalari va embeddinglarini qaytaradi
    """
    koordinatalar = aniqlash(model_aniq, rasm)[0]
    embedding = model_emb.get(rasm, koordinatalar)
    return embedding, koordinatalar







def flip(rasm):

    yuz_aniqlagich_modul = model_yuklash(turi="aniqlagich")
    embedding_modul = model_yuklash(turi="embedding")

    rasm1_embedding, rasm1_koordinatalar = embedding_olish(rasm1, yuz_aniqlagich_modul, embedding_modul)
    rasm_embedding, rasm_koordinatalar = embedding_olish(rasm, yuz_aniqlagich_modul, embedding_modul)
    yaqinlik_embedding = vector_taq(rasm1_embedding.tolist(), rasm_embedding.tolist())

    return rasm ,yaqinlik_embedding

demo = gr.Interface(
    flip,
    gr.Image(source="webcam", streaming=True),
    "image",

    live=True

)
demo.launch()
