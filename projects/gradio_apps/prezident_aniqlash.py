import gradio as gr
import cv2
import math
ASLIDA = [
    "Bu O'zbekiston prezidenti Shavkat Mirziyoyev",
    "Bu Rassiya prezidenti Vladimir Putin",
    "Bu Amerika prezidenti Joe Biden",
]

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq
)

baza_rasm_1 = cv2.imread("./prezident_image_baza/mirziyoyev.jpg")
baza_rasm_2 = cv2.imread("./prezident_image_baza/putin.jpg")
baza_rasm_3 = cv2.imread("./prezident_image_baza/bayden.jpg")
def dastur(test_rasm):

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
    yaqinliklar = []
    for idx in range(0, len(baza_list)):
        yaqinlik = vector_taq(test_embedding.tolist(), baza_list[idx].tolist())
        yaqinliklar.append(yaqinlik)
        # 0.007, 0.12, 0.4
    max_yaqinlik = max(yaqinliklar) # 0.4
    for i in range(len(yaqinliklar)):
        if yaqinliklar[i] == max_yaqinlik: # i = 2
            return ASLIDA[i], yaqinlik
    return "Bu inson prezident emas"

# gradio
with gr.Blocks() as demo:
    name= gr.Image(label="Test rasm")
    output_text = gr.Textbox(label="Malumot")
    tugma = gr.Button("Bosing")
    tugma.click(fn=dastur, inputs=name, outputs=output_text)

demo.launch(share=True)





