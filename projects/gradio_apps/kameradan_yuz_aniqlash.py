import cv2
import gradio as gr

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq
)

baza_rasm = cv2.imread("./prezident_image_baza/nuriddin.jpg")

def kamera(rasm):
    aniqlagich_model = model_yuklash(turi="aniqlagich")
    embedding_modul = model_yuklash(turi="embedding")
    rasm_kordinatalar = aniqlash(
        model=aniqlagich_model,
        rasm=rasm
    )
    baza_rasm_kordinata = aniqlash(aniqlagich_model, baza_rasm)

    rasm_embedding = embedding_modul.get(rasm, rasm_kordinatalar)
    baza_rasm_embedding = embedding_modul.get(baza_rasm, baza_rasm_kordinata)

    yaqinlik = vector_taq(rasm_embedding.tolist(), baza_rasm_embedding.tolist())

    return yaqinlik

demo = gr.Interface(
    kamera,
    gr.Image(source="webcam", streaming=True),
    "text",
    live=True
)

demo.launch()