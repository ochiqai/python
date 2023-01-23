import cv2
import gradio as gr
from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq
)
#----------------------- Proyekt: ------------------------------------
# Kamera orqali rasm kiritiladi, uni bazadagi rasmlar bilan solishtiradi.
#   Agar: kiritilgan rasm bazada mavjud bo'lsa
#       uni kimligini qaytaradi
#   Aks holsa: kiritilgan rasm bazada mavjud bo'lmasa
#       'Bu inson bazadagi odamlarga mos kelmadi' matnni qaytaradi
#----------------------------------------------------------------------


#---------------------- Algoritim -------------------------------------
#    1. Kerakli modellarni yuklaymiz. (detection, embedding)
#    2. Rasmlarning kordinatasi (rasm, bazadagi rasmlar)
#    3. Rasmlarning embeddinglarini olamiz
#    4. Vektorlarni taqqoslash funksiyasi orqali yaqinliklarni aniqlab olamiz

#----------------------------------------------------------------------

font = cv2.FONT_HERSHEY_SIMPLEX
org = (40, 50)
fontScale = 0.8
color = (255, 0, 0)
thickness = 1

baza_rasm = cv2.imread("./gradio_apps/refaktor/rasmlar/Orif.png")

def kamera(rasm):
    """
    Kameradan rasmni olib bazadagi rasm bilan solishtiradi
    Parameters
    ----------
    rasm:'numpy.ndarray'

    Returns
    -------
    natija qaytariladi
    """

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
    if yaqinlik > 0.15:

        natija = cv2.putText(rasm, "Salom Orif " + str(yaqinlik), org, font,
                           fontScale, color, thickness, cv2.LINE_AA)

    else:
        natija = cv2.putText(rasm, "Bu inson bazadagi odamlarga mos kelmadi" + str(yaqinlik), org, font,
                             fontScale, color, thickness, cv2.LINE_AA)
    return natija

demo = gr.Interface(
    kamera,
    gr.Image(source="webcam", streaming=True),
    "image",
    live=True
)

demo.launch()






