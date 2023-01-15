import gradio as gr
import cv2

ASLIDA = [
    "Bu O'zbekiston prezidenti Shavkat Mirziyoyev",
    "Bu Rassiya prezidenti Vladimir Putin",
    "Bu Amerika prezidenti Joe Biden",
]

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq
)

def kordinata_format(model, rasm):
    """
        Funksiya rasmning kordinatasini qaytaradi
    :param model:
         aniqlagich model
    :param rasm:
        rasm
    :return:
        rasm kordinatasi
    """
    kordinata = aniqlash(
        model=model,
        rasm=rasm
    )
    return kordinata[0]

baza_rasm_1 = cv2.imread("./prezident_image_baza/mirziyoyev.jpg")
baza_rasm_2 = cv2.imread("./prezident_image_baza/putin.jpg")
baza_rasm_3 = cv2.imread("./prezident_image_baza/bayden.jpg")

def dastur(test_rasm):
    # modellarni yuklash
    aniqlagich_model = model_yuklash(turi="aniqlagich")
    embedding_model = model_yuklash(turi="embedding")
    # bazadagi rasmlar
    baza_rasmlar = [baza_rasm_1, baza_rasm_2, baza_rasm_3]
    # bazadagi rasmlarning embeddingni olish
    baza_embeddinglar = []
    for baza_rasm in baza_rasmlar:
        baza_rasm_kordinata = kordinata_format(aniqlagich_model, baza_rasm)
        baza_embedding = embedding_model.get(baza_rasm, baza_rasm_kordinata)
        baza_embeddinglar.append(baza_embedding)
    # test rasm embedding olish
    test_rasm_kordinata = kordinata_format(aniqlagich_model, test_rasm)
    test_embedding = embedding_model.get(test_rasm, test_rasm_kordinata)

    yaqinliklar = []
    for idx in range(0, len(baza_embeddinglar)):
        yaqinlik = vector_taq(test_embedding.tolist(), baza_embeddinglar[idx].tolist())
        yaqinliklar.append(yaqinlik)
    max_value = -float('inf')
    max_index = -1  # 88
    for i, value in enumerate(yaqinliklar):
        if value > max_value:
            max_value = value
            max_index = i
    if yaqinlik < 0:
        return "Bu inson prezident emas", yaqinlik
    return ASLIDA[max_index], yaqinlik

# gradio qismi
with gr.Blocks() as demo:
    name= gr.Image(label="Test rasm")
    output_text = gr.Textbox(label="Malumot")
    tugma = gr.Button("Bosing")
    tugma.click(fn=dastur, inputs=name, outputs=output_text)
demo.launch(share=True)





