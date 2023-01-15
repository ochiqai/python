import gradio as gr
import cv2

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq
)

##### Proyekt:


####


BAZA = {
    0: "Bu O'zbekiston prezidenti Shavkat Mirziyoyev",
    1: "Bu Rassiya prezidenti Vladimir Putin",
    2: "Bu Amerika prezidenti Joe Biden",
}



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

def max_joyi(yaqinliklar):
    """
        sonlar ichidagi maksimal sonni indeksini qaytaradi
    :param yaqinliklar: list
        yaqinliklar
    :return: int
        indeks
    """
    max_value = -float('inf')
    max_index = -1
    for i, value in enumerate(yaqinliklar):
        if value > max_value:
            max_value = value
            max_index = i
    return max_index

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

    max_index = max_joyi(yaqinliklar)

    limit = 0.15
    if yaqinliklar[max_index] < limit:
        return "Bu inson bazadagi prezidentlarga mos kelmadi"

    return BAZA[max_index] + "yaqinlik: {}".format(yaqinliklar[max_index])


# gradio qismi
with gr.Blocks() as demo:
    name= gr.Image(label="Test rasm")
    output_text = gr.Textbox(label="Malumot")
    tugma = gr.Button("Bosing")
    tugma.click(fn=dastur, inputs=name, outputs=output_text)
demo.launch(share=True)

